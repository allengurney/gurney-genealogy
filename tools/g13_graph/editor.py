"""Transactional graph-editing service for the G13 context graph (Phase G4).

This module implements the §14 graph-editing artifact contract's *save
semantics* against the canonical SQLite database, reusing the accepted G1B
plumbing rather than reimplementing it:

- Field updates flow through :func:`mutations.apply_item_update`.
- Semantic checks reuse :func:`validation.validate_connection`, so every G1B
  validation improvement flows into the editor automatically.
- Revision audit rows are written with :func:`revisions.record_item_revision`.
- Derived refresh (FTS reindex + recovery export) reuses
  :func:`lifecycle.refresh_after_commit` and its stale semantics.
- Deterministic export/snapshot reuse :mod:`exporter`.

Save contract (§14):

- **Validate before save.** A change is applied inside a single transaction and
  validated *before* commit. Blocking is *delta-based*: only error codes the
  change itself introduces block the save, so a pre-existing warning or an
  unrelated error elsewhere in the graph never prevents an otherwise-valid edit.
  Derived-artifact staleness (``derived_indexes_stale`` /
  ``recovery_export_stale``) is expected mid-edit and never blocks — it is
  resolved by the post-commit refresh.
- **Single transaction, rollback on failure.** Any failure (validation, integrity,
  exception) rolls the whole change back; the DB is never left partially edited.
- **Audit every accepted change.** create/update/supersede/review/delete write an
  ``item_revisions`` row capturing before/after row state.
- **Human-readable before/after diff**, computed from current DB state vs. the
  proposed change, is available from :func:`preview_change` before committing.
- **Never lose an accepted edit.** The content transaction commits first; only
  then is the derived refresh attempted. A derived-step failure marks the
  artifact stale (``stale: True``) but does **not** roll back the committed edit.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, field
from typing import Any, Callable

from .config import GraphConfig
from .constants import (
    ITEM_KINDS,
    MARKER_ROLES,
    MARKER_STATUSES,
    RELATION_TYPES,
    SOURCE_ROLES,
    VISIBILITIES,
)
from .db import connect
from .lifecycle import PostCommitRefreshError, refresh_after_commit
from .mutations import apply_item_update
from .revisions import advance_revision, record_item_revision
from .util import canonical_json, utc_now
from .validation import MARKER_ID_RE, issues_as_dicts, validate_connection

# Error codes that describe *derived* artifacts (FTS indexes, recovery export)
# rather than content validity. They are expected to read stale between a content
# mutation and the post-commit refresh, so they never block a save.
NON_BLOCKING_CODES = frozenset({"derived_indexes_stale", "recovery_export_stale"})

# Controlled vocabularies for the editor's pick lists. Enumerations that live only
# in SQL CHECK constraints (statuses, review states, date precision, relation
# bearing/strength, evidence-group alignment, publication status, provenance,
# entity type) are mirrored here so the UI and the database agree; the shared
# item/relation/source vocabularies are imported from constants.py to stay single-
# sourced.
PICKLISTS: dict[str, tuple[str, ...]] = {
    "item_kind": ITEM_KINDS,
    "relation_type": RELATION_TYPES,
    "source_role": SOURCE_ROLES,
    "visibility": VISIBILITIES,
    "marker_role": MARKER_ROLES,
    "marker_status": MARKER_STATUSES,
    "status": ("active", "open", "resolved", "superseded", "rejected", "inactive"),
    "review_state": (
        "machine_suggested",
        "human_reviewed",
        "needs_revision",
        "rejected",
        "superseded",
    ),
    "date_precision": ("day", "month", "year", "range", "before", "after", "unknown"),
    "relation_bearing": ("direct", "indirect", "contextual", "methodological"),
    "relation_strength": ("strong", "moderate", "weak", "unknown"),
    "evidence_group_alignment": ("collective", "probable", "contextual", "unclear"),
    "publication_status": ("proposed", "published", "retired"),
    "provenance_origin": ("machine_suggested", "human_authored", "seed"),
    "entity_type": (
        "person",
        "place",
        "event",
        "source",
        "record_collection",
        "organization",
        "ship",
        "research_unit",
        "publication",
        "hypothesis",
    ),
    "confidence_label": (
        "high",
        "moderate-high",
        "probable",
        "moderate",
        "low-moderate",
        "low",
        "speculative",
    ),
}


class ChangeError(ValueError):
    """A change payload is malformed or references an unknown op."""


class ValidationBlocked(Exception):
    """A change was rejected because it introduces new blocking validation errors."""

    def __init__(self, blocking: list[dict[str, Any]]):
        super().__init__("Change introduces blocking validation errors.")
        self.blocking = blocking


@dataclass
class RevisionIntent:
    item_id: str
    change_kind: str  # create | update | supersede | review | delete
    field_summary: str
    before: dict[str, Any] | None
    after: dict[str, Any] | None


@dataclass
class MarkerRevisionIntent:
    marker_id: str
    change_kind: str  # create | update | retire | review | delete
    summary: str
    before: dict[str, Any] | None
    after: dict[str, Any] | None


@dataclass
class StagedChange:
    revisions: list[RevisionIntent] = field(default_factory=list)
    marker_revisions: list[MarkerRevisionIntent] = field(default_factory=list)
    summary: str = ""


def coalesce_revision_intents(
    intents: list[RevisionIntent],
) -> list[RevisionIntent]:
    """Merge intents that share ``(item_id, change_kind)`` into one, preserving
    first-seen order.

    ``item_revisions`` carries ``UNIQUE(database_revision, item_id, change_kind)``,
    so a single batch (one ``database_revision``) may write at most one row per
    ``(item_id, change_kind)``. But a legitimate batch can touch the same item
    several times with the same kind — e.g. one evidence item that SUPPORTS
    several findings produces one ``"update"`` intent per relation via
    :func:`_op_add_relation`. Left as-is, the second write collides on the UNIQUE
    key. Coalescing folds those into a single row whose ``before`` is the earliest
    snapshot, ``after`` the latest (so the row reflects the item's final state),
    and ``field_summary`` the concatenation of the distinct per-intent summaries.
    """
    order: list[tuple[str, str]] = []
    merged: dict[tuple[str, str], RevisionIntent] = {}
    summaries: dict[tuple[str, str], list[str]] = {}
    for intent in intents:
        key = (intent.item_id, intent.change_kind)
        current = merged.get(key)
        if current is None:
            order.append(key)
            merged[key] = RevisionIntent(
                intent.item_id,
                intent.change_kind,
                intent.field_summary,
                intent.before,
                intent.after,
            )
            summaries[key] = [intent.field_summary] if intent.field_summary else []
        else:
            # Earliest ``before`` is kept (set on first sight); take the latest
            # ``after`` so the coalesced row reflects the item's final state.
            current.after = intent.after
            if intent.field_summary and intent.field_summary not in summaries[key]:
                summaries[key].append(intent.field_summary)
    for key in order:
        merged[key].field_summary = " ".join(summaries[key])
    return [merged[key] for key in order]


# --------------------------------------------------------------------------- #
# Blocking-error delta
# --------------------------------------------------------------------------- #
def _blocking_error_keys(
    connection: sqlite3.Connection, config: GraphConfig
) -> set[tuple[str, str | None]]:
    return {
        (issue.code, issue.record_id)
        for issue in validate_connection(connection, config, include_recovery=False)
        if issue.severity == "error" and issue.code not in NON_BLOCKING_CODES
    }


# --------------------------------------------------------------------------- #
# Snapshot helpers (for audit before/after + diff)
# --------------------------------------------------------------------------- #
def _item_row(connection: sqlite3.Connection, item_id: str) -> dict[str, Any] | None:
    row = connection.execute(
        "SELECT * FROM research_items WHERE item_id=?", (item_id,)
    ).fetchone()
    return None if row is None else dict(row)


def _relations_snapshot(connection: sqlite3.Connection, item_id: str) -> dict[str, Any]:
    return {
        "relations": [
            dict(row)
            for row in connection.execute(
                """
                SELECT * FROM item_relations
                WHERE from_item_id=? OR to_item_id=?
                ORDER BY from_item_id, relation_type, to_item_id
                """,
                (item_id, item_id),
            )
        ]
    }


def _sources_snapshot(connection: sqlite3.Connection, item_id: str) -> dict[str, Any]:
    return {
        "sources": [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM item_sources WHERE item_id=? ORDER BY item_source_id",
                (item_id,),
            )
        ]
    }


def _entities_snapshot(connection: sqlite3.Connection, item_id: str) -> dict[str, Any]:
    return {
        "entities": [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM item_entities WHERE item_id=? ORDER BY entity_id, role",
                (item_id,),
            )
        ]
    }


def _publications_snapshot(
    connection: sqlite3.Connection, item_id: str
) -> dict[str, Any]:
    return {
        "publications": [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM item_publications WHERE item_id=? ORDER BY publication_id",
                (item_id,),
            )
        ]
    }


def _dates_snapshot(connection: sqlite3.Connection, item_id: str) -> dict[str, Any]:
    return {
        "dates": [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM item_dates WHERE item_id=? ORDER BY date_role",
                (item_id,),
            )
        ]
    }


def _negative_snapshot(connection: sqlite3.Connection, item_id: str) -> dict[str, Any]:
    row = connection.execute(
        "SELECT * FROM negative_result_scope WHERE item_id=?", (item_id,)
    ).fetchone()
    return {"negative_result_scope": None if row is None else dict(row)}


def _marker_snapshot(
    connection: sqlite3.Connection, marker_id: str
) -> dict[str, Any] | None:
    row = connection.execute(
        "SELECT * FROM prose_markers WHERE marker_id=?", (marker_id,)
    ).fetchone()
    if row is None:
        return None
    result = dict(row)
    result["items"] = [
        dict(member)
        for member in connection.execute(
            """
            SELECT * FROM prose_marker_items
            WHERE marker_id=?
            ORDER BY display_order, item_id
            """,
            (marker_id,),
        )
    ]
    return result


def next_marker_id(connection: sqlite3.Connection, prefix: str = "G13-PM-") -> str:
    pattern = prefix + "[0-9][0-9][0-9][0-9][0-9][0-9]"
    row = connection.execute(
        "SELECT marker_id FROM prose_markers WHERE marker_id GLOB ? "
        "ORDER BY marker_id DESC LIMIT 1",
        (pattern,),
    ).fetchone()
    nxt = 1 if row is None else int(row[0].rsplit("-", 1)[-1]) + 1
    return f"{prefix}{nxt:06d}"


def next_item_id(connection: sqlite3.Connection, prefix: str = "G13-RI-") -> str:
    pattern = prefix + "[0-9][0-9][0-9][0-9][0-9][0-9]"
    row = connection.execute(
        "SELECT item_id FROM research_items WHERE item_id GLOB ? "
        "ORDER BY item_id DESC LIMIT 1",
        (pattern,),
    ).fetchone()
    nxt = 1 if row is None else int(row[0].rsplit("-", 1)[-1]) + 1
    return f"{prefix}{nxt:06d}"


def next_entity_id(connection: sqlite3.Connection, prefix: str = "G13-ENT-") -> str:
    pattern = prefix + "[0-9][0-9][0-9][0-9][0-9][0-9]"
    row = connection.execute(
        "SELECT entity_id FROM entities WHERE entity_id GLOB ? "
        "ORDER BY entity_id DESC LIMIT 1",
        (pattern,),
    ).fetchone()
    nxt = 1 if row is None else int(row[0].rsplit("-", 1)[-1]) + 1
    return f"{prefix}{nxt:06d}"


# --------------------------------------------------------------------------- #
# Op handlers.  Each returns a StagedChange after mutating the open transaction.
# --------------------------------------------------------------------------- #
def _require(params: dict[str, Any], *keys: str) -> None:
    missing = [key for key in keys if params.get(key) in (None, "")]
    if missing:
        raise ChangeError(f"Missing required field(s): {', '.join(missing)}")


def _insert_row(connection: sqlite3.Connection, table: str, row: dict[str, Any]) -> None:
    valid = {r["name"] for r in connection.execute(f'PRAGMA table_info("{table}")')}
    payload = {k: v for k, v in row.items() if k in valid and v is not None}
    if not payload:
        raise ChangeError(f"No valid columns supplied for {table}.")
    names = ", ".join(f'"{c}"' for c in payload)
    placeholders = ", ".join("?" for _ in payload)
    connection.execute(
        f'INSERT INTO "{table}" ({names}) VALUES ({placeholders})',
        tuple(payload.values()),
    )


def _op_create_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    item = dict(params.get("item") or {})
    _require(item, "item_kind", "statement", "research_unit_id")
    item_id = item.get("item_id") or next_item_id(connection)
    item["item_id"] = item_id
    item.setdefault("status", "active")
    item.setdefault("visibility", "repo_only")
    item.setdefault("excerpt_publishable", 0)
    item.setdefault("review_state", "human_reviewed")
    item.setdefault("provenance_origin", "human_authored")
    item.setdefault("qualifiers_json", "[]")
    item.setdefault("tags_json", "[]")
    item["created_at"] = ts
    item["updated_at"] = ts
    item["revision"] = 1
    _insert_row(connection, "research_items", item)

    for date in params.get("dates") or []:
        date = {**date, "item_id": item_id}
        date.setdefault("date_role", "event")
        _insert_row(connection, "item_dates", date)
    for source in params.get("sources") or []:
        _insert_row(connection, "item_sources", {**source, "item_id": item_id})
    for link in params.get("entities") or []:
        _insert_row(connection, "item_entities", {**link, "item_id": item_id})
    if params.get("negative_result_scope"):
        _insert_row(
            connection,
            "negative_result_scope",
            {**params["negative_result_scope"], "item_id": item_id},
        )
    for pub in params.get("publications") or []:
        _insert_row(connection, "item_publications", {**pub, "item_id": item_id})

    after = _item_row(connection, item_id)
    return StagedChange(
        revisions=[
            RevisionIntent(
                item_id, "create", f"Created {item['item_kind']} item.", None, after
            )
        ],
        summary=f"Create item {item_id}",
    )


def _op_update_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id")
    changes = dict(params.get("changes") or {})
    before, after = apply_item_update(connection, params["item_id"], changes, timestamp=ts)
    return StagedChange(
        revisions=[
            RevisionIntent(
                params["item_id"],
                "update",
                ", ".join(sorted(changes)),
                before,
                after,
            )
        ],
        summary=f"Update item {params['item_id']}",
    )


def _op_supersede_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id", "superseded_by")
    item_id = params["item_id"]
    newer = params["superseded_by"]
    before, after = apply_item_update(
        connection,
        item_id,
        {"status": "superseded", "superseded_by": newer},
        timestamp=ts,
    )
    if params.get("add_relation", True):
        connection.execute(
            """
            INSERT OR IGNORE INTO item_relations(
                from_item_id, relation_type, to_item_id, bearing, strength,
                explanation, review_state
            ) VALUES (?, 'SUPERSEDES', ?, 'direct', 'strong', ?, 'human_reviewed')
            """,
            (newer, item_id, params.get("explanation")),
        )
    return StagedChange(
        revisions=[
            RevisionIntent(
                item_id, "supersede", f"Superseded by {newer}.", before, after
            )
        ],
        summary=f"Supersede {item_id} by {newer}",
    )


def _op_retire_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    """Soft-delete: item_revisions keeps a RESTRICT FK, so items are never hard
    deleted once they carry audit history; they are marked rejected/inactive."""
    _require(params, "item_id")
    status = params.get("status", "rejected")
    before, after = apply_item_update(
        connection,
        params["item_id"],
        {"status": status, "review_state": "rejected"},
        timestamp=ts,
    )
    return StagedChange(
        revisions=[
            RevisionIntent(
                params["item_id"], "delete", f"Retired (status={status}).", before, after
            )
        ],
        summary=f"Retire item {params['item_id']}",
    )


def _op_set_review_state(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    """Batch accept/reject for the machine-suggested review queue."""
    item_ids = params.get("item_ids") or ([params["item_id"]] if params.get("item_id") else [])
    if not item_ids:
        raise ChangeError("set_review_state requires item_id or item_ids.")
    _require(params, "review_state")
    review_state = params["review_state"]
    changes: dict[str, Any] = {"review_state": review_state}
    if params.get("status"):
        changes["status"] = params["status"]
    changes["reviewed_by"] = params.get("reviewed_by", by)
    changes["reviewed_at"] = ts
    staged = StagedChange(summary=f"Review {len(item_ids)} item(s) → {review_state}")
    for item_id in item_ids:
        before, after = apply_item_update(connection, item_id, dict(changes), timestamp=ts)
        staged.revisions.append(
            RevisionIntent(
                item_id, "review", f"review_state={review_state}", before, after
            )
        )
    return staged


def _op_undo_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    """Revert an item's editable fields to the ``before`` state of its most
    recent audited change. If that change was the item's creation, retire it."""
    _require(params, "item_id")
    item_id = params["item_id"]
    row = connection.execute(
        """
        SELECT database_revision, change_kind, before_json
        FROM item_revisions WHERE item_id=?
        ORDER BY revision_id DESC LIMIT 1
        """,
        (item_id,),
    ).fetchone()
    if row is None:
        raise ChangeError(f"No revision history to undo for {item_id}.")
    if row["before_json"] is None:
        return _op_retire_item(connection, {"item_id": item_id}, ts, by)
    before_state = json.loads(row["before_json"])
    from .mutations import ALLOWED_ITEM_FIELDS

    restore = {
        key: before_state[key]
        for key in ALLOWED_ITEM_FIELDS
        if key in before_state
    }
    before, after = apply_item_update(connection, item_id, restore, timestamp=ts)
    return StagedChange(
        revisions=[
            RevisionIntent(
                item_id,
                "update",
                f"Undo of revision {row['database_revision']}.",
                before,
                after,
            )
        ],
        summary=f"Undo last change to {item_id}",
    )


def _op_add_relation(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "from_item_id", "relation_type", "to_item_id")
    before = _relations_snapshot(connection, params["from_item_id"])
    connection.execute(
        """
        INSERT INTO item_relations(
            from_item_id, relation_type, to_item_id, bearing, strength,
            explanation, review_state
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            params["from_item_id"],
            params["relation_type"],
            params["to_item_id"],
            params.get("bearing", "direct"),
            params.get("strength", "unknown"),
            params.get("explanation"),
            params.get("review_state", "human_reviewed"),
        ),
    )
    after = _relations_snapshot(connection, params["from_item_id"])
    return StagedChange(
        revisions=[
            RevisionIntent(
                params["from_item_id"],
                "update",
                f"Add relation {params['relation_type']} → {params['to_item_id']}.",
                before,
                after,
            )
        ],
        summary="Add relation",
    )


def _op_update_relation(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "from_item_id", "relation_type", "to_item_id")
    before = _relations_snapshot(connection, params["from_item_id"])
    fields = {
        key: params[key]
        for key in ("bearing", "strength", "explanation", "review_state")
        if key in params
    }
    if not fields:
        raise ChangeError("update_relation requires at least one editable field.")
    assignments = ", ".join(f'"{k}"=?' for k in fields)
    connection.execute(
        f"""
        UPDATE item_relations SET {assignments}
        WHERE from_item_id=? AND relation_type=? AND to_item_id=?
        """,
        (*fields.values(), params["from_item_id"], params["relation_type"], params["to_item_id"]),
    )
    after = _relations_snapshot(connection, params["from_item_id"])
    return StagedChange(
        revisions=[
            RevisionIntent(params["from_item_id"], "update", "Update relation.", before, after)
        ],
        summary="Update relation",
    )


def _op_remove_relation(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "from_item_id", "relation_type", "to_item_id")
    before = _relations_snapshot(connection, params["from_item_id"])
    connection.execute(
        "DELETE FROM item_relations WHERE from_item_id=? AND relation_type=? AND to_item_id=?",
        (params["from_item_id"], params["relation_type"], params["to_item_id"]),
    )
    after = _relations_snapshot(connection, params["from_item_id"])
    return StagedChange(
        revisions=[
            RevisionIntent(params["from_item_id"], "update", "Remove relation.", before, after)
        ],
        summary="Remove relation",
    )


def _op_add_source_link(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id", "source_id", "role")
    item_id = params["item_id"]
    before = _sources_snapshot(connection, item_id)
    _insert_row(
        connection,
        "item_sources",
        {
            "item_id": item_id,
            "source_id": params["source_id"],
            "role": params["role"],
            "locator": params.get("locator", ""),
            "evidence_excerpt": params.get("evidence_excerpt"),
            "excerpt_publishable": params.get("excerpt_publishable", 0),
            "alignment_note": params.get("alignment_note"),
            "verification_level": params.get("verification_level"),
        },
    )
    after = _sources_snapshot(connection, item_id)
    return StagedChange(
        revisions=[
            RevisionIntent(
                item_id, "update", f"Add source link {params['source_id']}.", before, after
            )
        ],
        summary="Add source link",
    )


def _op_update_source_link(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_source_id")
    row = connection.execute(
        "SELECT item_id FROM item_sources WHERE item_source_id=?",
        (params["item_source_id"],),
    ).fetchone()
    if row is None:
        raise ChangeError(f"Unknown item_source_id {params['item_source_id']}.")
    item_id = row["item_id"]
    before = _sources_snapshot(connection, item_id)
    fields = {
        key: params[key]
        for key in (
            "role",
            "locator",
            "evidence_excerpt",
            "excerpt_publishable",
            "alignment_note",
            "verification_level",
        )
        if key in params
    }
    if not fields:
        raise ChangeError("update_source_link requires at least one editable field.")
    assignments = ", ".join(f'"{k}"=?' for k in fields)
    connection.execute(
        f"UPDATE item_sources SET {assignments} WHERE item_source_id=?",
        (*fields.values(), params["item_source_id"]),
    )
    after = _sources_snapshot(connection, item_id)
    return StagedChange(
        revisions=[RevisionIntent(item_id, "update", "Update source link.", before, after)],
        summary="Update source link",
    )


def _op_remove_source_link(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_source_id")
    row = connection.execute(
        "SELECT item_id FROM item_sources WHERE item_source_id=?",
        (params["item_source_id"],),
    ).fetchone()
    if row is None:
        raise ChangeError(f"Unknown item_source_id {params['item_source_id']}.")
    item_id = row["item_id"]
    before = _sources_snapshot(connection, item_id)
    connection.execute(
        "DELETE FROM item_sources WHERE item_source_id=?", (params["item_source_id"],)
    )
    after = _sources_snapshot(connection, item_id)
    return StagedChange(
        revisions=[RevisionIntent(item_id, "update", "Remove source link.", before, after)],
        summary="Remove source link",
    )


def _op_add_entity_link(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id", "entity_id", "role")
    item_id = params["item_id"]
    before = _entities_snapshot(connection, item_id)
    _insert_row(
        connection,
        "item_entities",
        {"item_id": item_id, "entity_id": params["entity_id"], "role": params["role"]},
    )
    after = _entities_snapshot(connection, item_id)
    return StagedChange(
        revisions=[
            RevisionIntent(
                item_id, "update", f"Link entity {params['entity_id']}.", before, after
            )
        ],
        summary="Add entity link",
    )


def _op_remove_entity_link(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id", "entity_id", "role")
    item_id = params["item_id"]
    before = _entities_snapshot(connection, item_id)
    connection.execute(
        "DELETE FROM item_entities WHERE item_id=? AND entity_id=? AND role=?",
        (item_id, params["entity_id"], params["role"]),
    )
    after = _entities_snapshot(connection, item_id)
    return StagedChange(
        revisions=[RevisionIntent(item_id, "update", "Unlink entity.", before, after)],
        summary="Remove entity link",
    )


def _op_create_research_unit(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    unit = dict(params.get("unit") or {})
    _require(unit, "unit_id", "path", "title")
    unit.setdefault("review_state", "human_reviewed")
    _insert_row(connection, "research_units", unit)
    # Research units are reference rows, not items; no item_revisions row (like
    # entities). The database_revision bump + recovery refresh record the change.
    return StagedChange(summary=f"Create research unit {unit['unit_id']}")


def _op_update_research_unit(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "unit_id")
    fields = {
        key: params[key]
        for key in ("path", "heading_id", "title", "scope_summary", "review_state")
        if key in params
    }
    if not fields:
        raise ChangeError("update_research_unit requires at least one editable field.")
    assignments = ", ".join(f'"{k}"=?' for k in fields)
    connection.execute(
        f"UPDATE research_units SET {assignments} WHERE unit_id=?",
        (*fields.values(), params["unit_id"]),
    )
    return StagedChange(summary=f"Update research unit {params['unit_id']}")


def _op_create_entity(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    entity = dict(params.get("entity") or {})
    _require(entity, "entity_type", "canonical_label")
    entity.setdefault("entity_id", next_entity_id(connection))
    _insert_row(connection, "entities", entity)
    # Entity reference data is not item-scoped, so it carries no item_revisions
    # row; the database_revision bump + recovery refresh still record the change.
    return StagedChange(summary=f"Create entity {entity['entity_id']}")


def _op_update_entity(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "entity_id")
    fields = {
        key: params[key]
        for key in ("entity_type", "canonical_label", "description", "repo_record_id")
        if key in params
    }
    if not fields:
        raise ChangeError("update_entity requires at least one editable field.")
    assignments = ", ".join(f'"{k}"=?' for k in fields)
    connection.execute(
        f"UPDATE entities SET {assignments} WHERE entity_id=?",
        (*fields.values(), params["entity_id"]),
    )
    return StagedChange(summary=f"Update entity {params['entity_id']}")


def _op_set_dates(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id", "precision")
    item_id = params["item_id"]
    date_role = params.get("date_role", "event")
    before = _dates_snapshot(connection, item_id)
    columns = {
        "item_id": item_id,
        "date_role": date_role,
        "plausible_start": params.get("plausible_start"),
        "plausible_end": params.get("plausible_end"),
        "probable_start": params.get("probable_start"),
        "probable_end": params.get("probable_end"),
        "precision": params["precision"],
        "original_display": params.get("original_display"),
        "calendar": params.get("calendar", "normalized-gregorian"),
        "chronology_key": params.get("chronology_key"),
        "chronology_key_basis": params.get("chronology_key_basis"),
        "manual_override": params.get("manual_override", 0),
    }
    names = ", ".join(f'"{c}"' for c in columns)
    placeholders = ", ".join("?" for _ in columns)
    updates = ", ".join(
        f'"{c}"=excluded."{c}"' for c in columns if c not in ("item_id", "date_role")
    )
    connection.execute(
        f"""
        INSERT INTO item_dates ({names}) VALUES ({placeholders})
        ON CONFLICT(item_id, date_role) DO UPDATE SET {updates}
        """,
        tuple(columns.values()),
    )
    after = _dates_snapshot(connection, item_id)
    return StagedChange(
        revisions=[RevisionIntent(item_id, "update", f"Set {date_role} date.", before, after)],
        summary="Set item dates",
    )


def _op_set_negative_scope(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id", "provider", "collection_name", "query_description")
    item_id = params["item_id"]
    before = _negative_snapshot(connection, item_id)
    limitations = params.get("limitations") or []
    columns = {
        "item_id": item_id,
        "provider": params["provider"],
        "collection_name": params["collection_name"],
        "date_start": params.get("date_start"),
        "date_end": params.get("date_end"),
        "query_description": params["query_description"],
        "results_reviewed": params.get("results_reviewed"),
        "coverage_confirmed": params.get("coverage_confirmed", 0),
        "limitations_json": canonical_json(limitations),
    }
    names = ", ".join(f'"{c}"' for c in columns)
    placeholders = ", ".join("?" for _ in columns)
    updates = ", ".join(f'"{c}"=excluded."{c}"' for c in columns if c != "item_id")
    connection.execute(
        f"""
        INSERT INTO negative_result_scope ({names}) VALUES ({placeholders})
        ON CONFLICT(item_id) DO UPDATE SET {updates}
        """,
        tuple(columns.values()),
    )
    after = _negative_snapshot(connection, item_id)
    return StagedChange(
        revisions=[RevisionIntent(item_id, "update", "Set negative-result scope.", before, after)],
        summary="Set negative-result scope",
    )


def _op_add_publication(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "item_id", "publication_path", "status")
    item_id = params["item_id"]
    before = _publications_snapshot(connection, item_id)
    _insert_row(
        connection,
        "item_publications",
        {
            "item_id": item_id,
            "publication_path": params["publication_path"],
            "heading_id": params.get("heading_id"),
            "assertion_summary": params.get("assertion_summary"),
            "status": params["status"],
            "visibility": params.get("visibility", "repo_only"),
            "excerpt_publishable": params.get("excerpt_publishable", 0),
        },
    )
    after = _publications_snapshot(connection, item_id)
    return StagedChange(
        revisions=[RevisionIntent(item_id, "update", "Add publication mapping.", before, after)],
        summary="Add publication mapping",
    )


def _op_remove_publication(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "publication_id")
    row = connection.execute(
        "SELECT item_id FROM item_publications WHERE publication_id=?",
        (params["publication_id"],),
    ).fetchone()
    if row is None:
        raise ChangeError(f"Unknown publication_id {params['publication_id']}.")
    item_id = row["item_id"]
    before = _publications_snapshot(connection, item_id)
    connection.execute(
        "DELETE FROM item_publications WHERE publication_id=?", (params["publication_id"],)
    )
    after = _publications_snapshot(connection, item_id)
    return StagedChange(
        revisions=[RevisionIntent(item_id, "update", "Remove publication mapping.", before, after)],
        summary="Remove publication mapping",
    )


# --------------------------------------------------------------------------- #
# Prose-marker ops (Plan 2a).  Markers are audited in marker_revisions, not
# item_revisions; snapshots include the member rows so before/after diffs show
# membership changes.  The prose token (<!-- graph-marker: ID -->) lives in the
# research unit's Markdown file and is enforced by marker_token_count_invalid,
# so an active marker cannot be created before its token exists in prose.
# --------------------------------------------------------------------------- #
def _require_marker(connection: sqlite3.Connection, marker_id: str) -> None:
    if connection.execute(
        "SELECT 1 FROM prose_markers WHERE marker_id=?", (marker_id,)
    ).fetchone() is None:
        raise ChangeError(f"Unknown marker_id {marker_id}.")


def _op_create_marker(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    marker = dict(params.get("marker") or {})
    _require(marker, "research_unit_id", "primary_item_id")
    marker_id = marker.get("marker_id") or next_marker_id(connection)
    if MARKER_ID_RE.fullmatch(marker_id) is None:
        raise ChangeError(
            f"Invalid marker ID {marker_id!r}; expected PREFIX-PM-000000."
        )
    marker["marker_id"] = marker_id
    marker.setdefault("visibility", "repo_only")
    marker.setdefault("status", "active")
    marker["created_at"] = ts
    marker["updated_at"] = ts
    _insert_row(connection, "prose_markers", marker)
    members = params.get("items") or [
        {"item_id": marker["primary_item_id"], "marker_role": "primary"}
    ]
    for order, member in enumerate(members):
        row = {"display_order": order, **member, "marker_id": marker_id}
        _insert_row(connection, "prose_marker_items", row)
    after = _marker_snapshot(connection, marker_id)
    return StagedChange(
        marker_revisions=[
            MarkerRevisionIntent(
                marker_id, "create", f"Created marker ({len(members)} member(s)).",
                None, after,
            )
        ],
        summary=f"Create marker {marker_id}",
    )


def _op_update_marker(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "marker_id")
    marker_id = params["marker_id"]
    _require_marker(connection, marker_id)
    fields = {
        key: params[key]
        for key in ("status", "visibility", "research_unit_id")
        if key in params
    }
    if not fields:
        raise ChangeError("update_marker requires at least one editable field.")
    before = _marker_snapshot(connection, marker_id)
    assignments = ", ".join(f'"{k}"=?' for k in fields)
    connection.execute(
        f'UPDATE prose_markers SET {assignments}, "updated_at"=? WHERE marker_id=?',
        (*fields.values(), ts, marker_id),
    )
    after = _marker_snapshot(connection, marker_id)
    kind = "retire" if params.get("status") == "retired" else "update"
    return StagedChange(
        marker_revisions=[
            MarkerRevisionIntent(
                marker_id, kind, ", ".join(sorted(fields)), before, after
            )
        ],
        summary=f"Update marker {marker_id}",
    )


def _op_set_marker_primary(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    """Repoint a marker's primary in one transaction: demote the current primary
    member to `expressed`, promote (or add) the new member as `primary`, and
    update prose_markers.primary_item_id — the deferred FK requires all three."""
    _require(params, "marker_id", "item_id")
    marker_id, item_id = params["marker_id"], params["item_id"]
    _require_marker(connection, marker_id)
    before = _marker_snapshot(connection, marker_id)
    # Repoint the marker row first: its deferred FK tolerates the not-yet-
    # existing (marker_id, item_id, 'primary') member until commit, and once
    # repointed, demoting the old primary member no longer cascades into
    # prose_markers.primary_role (which is CHECK-locked to 'primary').
    connection.execute(
        "UPDATE prose_markers SET primary_item_id=?, updated_at=? WHERE marker_id=?",
        (item_id, ts, marker_id),
    )
    connection.execute(
        "UPDATE prose_marker_items SET marker_role='expressed' "
        "WHERE marker_id=? AND marker_role='primary' AND item_id<>?",
        (marker_id, item_id),
    )
    existing = connection.execute(
        "SELECT 1 FROM prose_marker_items WHERE marker_id=? AND item_id=?",
        (marker_id, item_id),
    ).fetchone()
    if existing is None:
        order = connection.execute(
            "SELECT coalesce(max(display_order), -1) + 1 FROM prose_marker_items "
            "WHERE marker_id=?",
            (marker_id,),
        ).fetchone()[0]
        _insert_row(
            connection,
            "prose_marker_items",
            {
                "marker_id": marker_id,
                "item_id": item_id,
                "marker_role": "primary",
                "display_order": order,
                "cross_unit_reason": params.get("cross_unit_reason"),
                "cross_unit_reviewed_by": params.get("cross_unit_reviewed_by"),
            },
        )
    else:
        connection.execute(
            "UPDATE prose_marker_items SET marker_role='primary' "
            "WHERE marker_id=? AND item_id=?",
            (marker_id, item_id),
        )
    after = _marker_snapshot(connection, marker_id)
    return StagedChange(
        marker_revisions=[
            MarkerRevisionIntent(
                marker_id, "update", f"Set primary to {item_id}.", before, after
            )
        ],
        summary=f"Set primary of {marker_id} to {item_id}",
    )


def _op_add_marker_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "marker_id", "item_id", "marker_role")
    marker_id = params["marker_id"]
    _require_marker(connection, marker_id)
    before = _marker_snapshot(connection, marker_id)
    display_order = params.get("display_order")
    if display_order is None:
        display_order = connection.execute(
            "SELECT coalesce(max(display_order), -1) + 1 FROM prose_marker_items "
            "WHERE marker_id=?",
            (marker_id,),
        ).fetchone()[0]
    _insert_row(
        connection,
        "prose_marker_items",
        {
            "marker_id": marker_id,
            "item_id": params["item_id"],
            "marker_role": params["marker_role"],
            "display_order": display_order,
            "cross_unit_reason": params.get("cross_unit_reason"),
            "cross_unit_reviewed_by": params.get("cross_unit_reviewed_by"),
        },
    )
    connection.execute(
        "UPDATE prose_markers SET updated_at=? WHERE marker_id=?", (ts, marker_id)
    )
    after = _marker_snapshot(connection, marker_id)
    return StagedChange(
        marker_revisions=[
            MarkerRevisionIntent(
                marker_id,
                "update",
                f"Add member {params['item_id']} ({params['marker_role']}).",
                before,
                after,
            )
        ],
        summary=f"Add {params['item_id']} to {marker_id}",
    )


def _op_update_marker_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "marker_id", "item_id")
    marker_id = params["marker_id"]
    fields = {
        key: params[key]
        for key in (
            "marker_role",
            "display_order",
            "cross_unit_reason",
            "cross_unit_reviewed_by",
        )
        if key in params
    }
    if not fields:
        raise ChangeError("update_marker_item requires at least one editable field.")
    row = connection.execute(
        "SELECT 1 FROM prose_marker_items WHERE marker_id=? AND item_id=?",
        (marker_id, params["item_id"]),
    ).fetchone()
    if row is None:
        raise ChangeError(f"No member {params['item_id']} in {marker_id}.")
    before = _marker_snapshot(connection, marker_id)
    assignments = ", ".join(f'"{k}"=?' for k in fields)
    connection.execute(
        f"UPDATE prose_marker_items SET {assignments} WHERE marker_id=? AND item_id=?",
        (*fields.values(), marker_id, params["item_id"]),
    )
    connection.execute(
        "UPDATE prose_markers SET updated_at=? WHERE marker_id=?", (ts, marker_id)
    )
    after = _marker_snapshot(connection, marker_id)
    return StagedChange(
        marker_revisions=[
            MarkerRevisionIntent(
                marker_id,
                "update",
                f"Update member {params['item_id']} ({', '.join(sorted(fields))}).",
                before,
                after,
            )
        ],
        summary=f"Update member {params['item_id']} of {marker_id}",
    )


def _op_remove_marker_item(
    connection: sqlite3.Connection, params: dict[str, Any], ts: str, by: str
) -> StagedChange:
    _require(params, "marker_id", "item_id")
    marker_id = params["marker_id"]
    _require_marker(connection, marker_id)
    before = _marker_snapshot(connection, marker_id)
    connection.execute(
        "DELETE FROM prose_marker_items WHERE marker_id=? AND item_id=?",
        (marker_id, params["item_id"]),
    )
    connection.execute(
        "UPDATE prose_markers SET updated_at=? WHERE marker_id=?", (ts, marker_id)
    )
    after = _marker_snapshot(connection, marker_id)
    return StagedChange(
        marker_revisions=[
            MarkerRevisionIntent(
                marker_id, "update", f"Remove member {params['item_id']}.", before, after
            )
        ],
        summary=f"Remove {params['item_id']} from {marker_id}",
    )


OPS: dict[str, Callable[[sqlite3.Connection, dict[str, Any], str, str], StagedChange]] = {
    "create_item": _op_create_item,
    "update_item": _op_update_item,
    "supersede_item": _op_supersede_item,
    "retire_item": _op_retire_item,
    "delete_item": _op_retire_item,
    "set_review_state": _op_set_review_state,
    "undo_item": _op_undo_item,
    "add_relation": _op_add_relation,
    "update_relation": _op_update_relation,
    "remove_relation": _op_remove_relation,
    "add_source_link": _op_add_source_link,
    "update_source_link": _op_update_source_link,
    "remove_source_link": _op_remove_source_link,
    "add_entity_link": _op_add_entity_link,
    "remove_entity_link": _op_remove_entity_link,
    "create_entity": _op_create_entity,
    "update_entity": _op_update_entity,
    "create_research_unit": _op_create_research_unit,
    "update_research_unit": _op_update_research_unit,
    "set_dates": _op_set_dates,
    "set_negative_scope": _op_set_negative_scope,
    "add_publication": _op_add_publication,
    "remove_publication": _op_remove_publication,
    "create_marker": _op_create_marker,
    "update_marker": _op_update_marker,
    "set_marker_primary": _op_set_marker_primary,
    "add_marker_item": _op_add_marker_item,
    "update_marker_item": _op_update_marker_item,
    "remove_marker_item": _op_remove_marker_item,
}


# --------------------------------------------------------------------------- #
# Diff
# --------------------------------------------------------------------------- #
_DIFF_IGNORE = frozenset({"updated_at", "revision"})


def _field_diff(before: dict[str, Any] | None, after: dict[str, Any] | None) -> list[dict[str, Any]]:
    changes: list[dict[str, Any]] = []
    before = before or {}
    after = after or {}
    for key in sorted(set(before) | set(after)):
        if key in _DIFF_IGNORE:
            continue
        old = before.get(key)
        new = after.get(key)
        if old != new:
            changes.append({"field": key, "before": old, "after": new})
    return changes


def _diff_for_intents(staged: StagedChange) -> list[dict[str, Any]]:
    diff = [
        {
            "item_id": intent.item_id,
            "change_kind": intent.change_kind,
            "summary": intent.field_summary,
            "field_changes": _field_diff(intent.before, intent.after),
        }
        for intent in staged.revisions
    ]
    diff.extend(
        {
            "item_id": intent.marker_id,
            "change_kind": intent.change_kind,
            "summary": intent.summary,
            "field_changes": _field_diff(intent.before, intent.after),
        }
        for intent in staged.marker_revisions
    )
    return diff


# --------------------------------------------------------------------------- #
# Preview / commit
# --------------------------------------------------------------------------- #
def _dispatch(op: str) -> Callable[..., StagedChange]:
    handler = OPS.get(op)
    if handler is None:
        raise ChangeError(f"Unknown op: {op!r}")
    return handler


def preview_change(config: GraphConfig, change: dict[str, Any]) -> dict[str, Any]:
    """Stage a change, validate it, compute a before/after diff, then roll back.

    No content is committed. Returns the human-readable diff, the new blocking
    errors the change would introduce (empty when safe to commit), and the full
    post-change validation issue list.
    """
    op = change.get("op")
    if not op:
        raise ChangeError("Change is missing an 'op' field.")
    handler = _dispatch(op)
    params = change.get("params") or {}
    changed_by = change.get("changed_by", "g13-editor")
    connection = connect(config.db_path)
    try:
        connection.execute("BEGIN IMMEDIATE")
        try:
            before_keys = _blocking_error_keys(connection, config)
            ts = utc_now()
            staged = handler(connection, params, ts, changed_by)
            issues = issues_as_dicts(validate_connection(connection, config, include_recovery=False))
            after_keys = _blocking_error_keys(connection, config)
            new_keys = after_keys - before_keys
            blocking = [dict(zip(("code", "record_id"), key)) for key in sorted(new_keys)]
            diff = _diff_for_intents(staged)
        finally:
            connection.rollback()
    finally:
        connection.close()
    return {
        "op": op,
        "summary": staged.summary,
        "diff": diff,
        "blocking_errors": blocking,
        "can_commit": not blocking,
        "would_write_revisions": len(staged.revisions) + len(staged.marker_revisions),
        "affected_items": sorted({intent.item_id for intent in staged.revisions}),
        "affected_markers": sorted(
            {intent.marker_id for intent in staged.marker_revisions}
        ),
        "validation_issues": issues,
    }


def commit_change(
    config: GraphConfig, change: dict[str, Any], *, changed_by: str | None = None
) -> dict[str, Any]:
    """Validate and apply a change in a single transaction, log audit rows, and
    refresh derived artifacts.

    Raises :class:`ValidationBlocked` (rolled back) if the change introduces new
    blocking errors. On a derived-refresh failure the content edit stays
    committed and ``stale`` is True.
    """
    op = change.get("op")
    if not op:
        raise ChangeError("Change is missing an 'op' field.")
    handler = _dispatch(op)
    params = change.get("params") or {}
    by = changed_by or change.get("changed_by", "g13-editor")

    connection = connect(config.db_path)
    revision: int | None = None
    intents: list[RevisionIntent] = []
    marker_intents: list[MarkerRevisionIntent] = []
    summary = ""
    try:
        connection.execute("BEGIN IMMEDIATE")
        try:
            before_keys = _blocking_error_keys(connection, config)
            revision, ts = advance_revision(connection)
            staged = handler(connection, params, ts, by)
            after_keys = _blocking_error_keys(connection, config)
            new_keys = after_keys - before_keys
            if new_keys:
                raise ValidationBlocked(
                    [dict(zip(("code", "record_id"), key)) for key in sorted(new_keys)]
                )
            for intent in staged.revisions:
                record_item_revision(
                    connection,
                    database_revision=revision,
                    item_id=intent.item_id,
                    changed_by=by,
                    change_kind=intent.change_kind,
                    field_summary=intent.field_summary,
                    before=intent.before,
                    after=intent.after,
                    changed_at=ts,
                )
            for marker_intent in staged.marker_revisions:
                connection.execute(
                    """
                    INSERT INTO marker_revisions(
                        marker_id, database_revision, changed_at, changed_by,
                        change_kind, before_json, after_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        marker_intent.marker_id,
                        revision,
                        ts,
                        by,
                        marker_intent.change_kind,
                        None
                        if marker_intent.before is None
                        else canonical_json(marker_intent.before),
                        None
                        if marker_intent.after is None
                        else canonical_json(marker_intent.after),
                    ),
                )
            intents = staged.revisions
            marker_intents = staged.marker_revisions
            summary = staged.summary
        except BaseException:
            connection.rollback()
            raise
        else:
            connection.commit()
    finally:
        connection.close()

    stale = False
    refresh_error: str | None = None
    try:
        refresh_after_commit(config)
    except PostCommitRefreshError as exc:
        stale = True
        refresh_error = str(exc)
    return {
        "committed": True,
        "op": op,
        "summary": summary,
        "database_revision": revision,
        "revisions_written": len(intents) + len(marker_intents),
        "affected_items": sorted({intent.item_id for intent in intents}),
        "affected_markers": sorted(
            {intent.marker_id for intent in marker_intents}
        ),
        "stale": stale,
        "refresh_error": refresh_error,
    }


# --------------------------------------------------------------------------- #
# Read surface for the editing UI
# --------------------------------------------------------------------------- #
def _truthy(value: Any) -> bool:
    return str(value).lower() in ("1", "true", "yes", "on")


def list_items(config: GraphConfig, filters: dict[str, Any] | None = None) -> dict[str, Any]:
    filters = filters or {}
    clauses: list[str] = []
    args: list[Any] = []
    joins = ""
    if filters.get("kind"):
        clauses.append("i.item_kind=?")
        args.append(filters["kind"])
    if filters.get("status"):
        clauses.append("i.status=?")
        args.append(filters["status"])
    if filters.get("visibility"):
        clauses.append("i.visibility=?")
        args.append(filters["visibility"])
    if filters.get("review_state"):
        clauses.append("i.review_state=?")
        args.append(filters["review_state"])
    if filters.get("confidence"):
        clauses.append("i.assessment_confidence_label=?")
        args.append(filters["confidence"])
    if filters.get("unit"):
        clauses.append("i.research_unit_id=?")
        args.append(filters["unit"])
    if filters.get("subject"):
        clauses.append("i.subject_entity_id=?")
        args.append(filters["subject"])
    if filters.get("source"):
        clauses.append(
            "i.item_id IN (SELECT item_id FROM item_sources WHERE source_id=?)"
        )
        args.append(filters["source"])
    if filters.get("marker"):
        clauses.append(
            "i.item_id IN (SELECT item_id FROM prose_marker_items WHERE marker_id=?)"
        )
        args.append(filters["marker"])
    if filters.get("q"):
        # A pasted G13-PM-… id also matches the items mapped to that marker, so
        # the prose token in a topic file can be traced from the filter box.
        clauses.append(
            "(i.statement LIKE ? OR i.short_label LIKE ? OR i.item_id LIKE ? "
            "OR i.item_id IN (SELECT item_id FROM prose_marker_items "
            "WHERE marker_id LIKE ?))"
        )
        needle = f"%{filters['q']}%"
        args.extend([needle, needle, needle, needle])
    if _truthy(filters.get("conflict")):
        clauses.append(
            "(i.item_kind='evidence_conflict' OR i.item_id IN ("
            "SELECT from_item_id FROM item_relations WHERE relation_type='CONTRADICTS' "
            "UNION SELECT to_item_id FROM item_relations WHERE relation_type='CONTRADICTS'))"
        )
    if _truthy(filters.get("pub_impact")):
        clauses.append("i.item_id IN (SELECT item_id FROM item_publications)")
    if _truthy(filters.get("needs_pub_decision")):
        # Items carrying a source excerpt that has not been cleared for publication,
        # or public items — the decisions §14 requires before a static export.
        clauses.append(
            "(i.item_id IN (SELECT item_id FROM item_sources "
            "WHERE evidence_excerpt IS NOT NULL AND length(trim(evidence_excerpt))>0 "
            "AND excerpt_publishable=0) OR i.visibility='public')"
        )
    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    connection = connect(config.db_path, read_only=True)
    try:
        rows = [
            dict(row)
            for row in connection.execute(
                f"""
                SELECT i.item_id, i.item_kind, i.status, i.short_label, i.statement,
                       i.assessment_confidence_label, i.visibility, i.review_state,
                       i.provenance_origin, i.research_unit_id, i.subject_entity_id,
                       (SELECT count(*) FROM item_sources s WHERE s.item_id=i.item_id) AS source_count,
                       (SELECT count(*) FROM item_relations r
                        WHERE r.from_item_id=i.item_id OR r.to_item_id=i.item_id) AS relation_count,
                       (SELECT count(*) FROM item_publications p WHERE p.item_id=i.item_id) AS publication_count,
                       (SELECT count(*) FROM prose_marker_items m WHERE m.item_id=i.item_id) AS marker_count
                FROM research_items AS i
                {joins}
                {where}
                ORDER BY i.item_id
                """,
                args,
            )
        ]
        total = connection.execute("SELECT count(*) FROM research_items").fetchone()[0]
    finally:
        connection.close()
    return {"items": rows, "count": len(rows), "total_items": int(total), "filters": filters}


def _publication_readiness(item: dict[str, Any]) -> dict[str, Any]:
    """§14: visibility + excerpt-publishability decisions required before a static
    export. This flags what still needs a decision; it does not perform the G5
    export."""
    unpublishable_excerpts = [
        s
        for s in item.get("sources", [])
        if (s.get("evidence_excerpt") or "").strip() and not s.get("excerpt_publishable")
    ]
    blockers: list[str] = []
    if item.get("visibility") == "public" and unpublishable_excerpts:
        blockers.append(
            "Public item has evidence excerpts not marked excerptPublishable."
        )
    return {
        "visibility": item.get("visibility"),
        "excerpt_decisions_pending": len(unpublishable_excerpts),
        "export_blockers": blockers,
        "export_ready": item.get("visibility") in ("public", "repo_only", "restricted")
        and not blockers,
    }


def duplicate_candidates(
    connection: sqlite3.Connection,
    *,
    subject_entity_id: str | None,
    statement: str | None,
    short_label: str | None,
    exclude_id: str | None = None,
    limit: int = 5,
) -> list[dict[str, Any]]:
    text = " ".join(filter(None, [statement, short_label])).lower()
    tokens = {t for t in _tokenize(text) if len(t) > 3}
    if not tokens and not subject_entity_id:
        return []
    rows = connection.execute(
        "SELECT item_id, item_kind, short_label, statement, subject_entity_id "
        "FROM research_items"
    ).fetchall()
    scored: list[tuple[float, dict[str, Any]]] = []
    for row in rows:
        if exclude_id and row["item_id"] == exclude_id:
            continue
        other_text = " ".join(filter(None, [row["statement"], row["short_label"]])).lower()
        other_tokens = {t for t in _tokenize(other_text) if len(t) > 3}
        overlap = len(tokens & other_tokens)
        if not overlap:
            if subject_entity_id and row["subject_entity_id"] == subject_entity_id:
                score = 0.15
            else:
                continue
        else:
            union = len(tokens | other_tokens) or 1
            score = overlap / union
            if subject_entity_id and row["subject_entity_id"] == subject_entity_id:
                score += 0.15
        if score >= 0.25:
            scored.append((score, dict(row)))
    scored.sort(key=lambda pair: (-pair[0], pair[1]["item_id"]))
    return [
        {**row, "similarity": round(score, 3)} for score, row in scored[:limit]
    ]


def _tokenize(text: str) -> list[str]:
    return [t for t in "".join(c if c.isalnum() else " " for c in text).split() if t]


def get_item_detail(config: GraphConfig, item_id: str) -> dict[str, Any] | None:
    from .queries import get_item

    item = get_item(config, item_id)
    if item is None:
        return None
    connection = connect(config.db_path, read_only=True)
    try:
        item["publications"] = [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM item_publications WHERE item_id=? ORDER BY publication_id",
                (item_id,),
            )
        ]
        neg = connection.execute(
            "SELECT * FROM negative_result_scope WHERE item_id=?", (item_id,)
        ).fetchone()
        if neg is not None:
            record = dict(neg)
            try:
                record["limitations"] = json.loads(record.get("limitations_json") or "[]")
            except json.JSONDecodeError:
                record["limitations"] = []
            item["negative_result_scope"] = record
        if item.get("subject_entity_id"):
            subject = connection.execute(
                "SELECT * FROM entities WHERE entity_id=?", (item["subject_entity_id"],)
            ).fetchone()
            item["subject_entity"] = None if subject is None else dict(subject)
        item["markers"] = [
            dict(row)
            for row in connection.execute(
                """
                SELECT mi.marker_role, mi.display_order, mi.cross_unit_reason,
                       m.marker_id, m.research_unit_id, m.primary_item_id,
                       m.status, m.visibility, u.path AS unit_path
                FROM prose_marker_items AS mi
                JOIN prose_markers AS m ON m.marker_id=mi.marker_id
                JOIN research_units AS u ON u.unit_id=m.research_unit_id
                WHERE mi.item_id=?
                ORDER BY m.marker_id
                """,
                (item_id,),
            )
        ]
        item["revisions"] = [
            dict(row)
            for row in connection.execute(
                """
                SELECT revision_id, database_revision, changed_at, changed_by,
                       change_kind, field_summary
                FROM item_revisions WHERE item_id=?
                ORDER BY revision_id DESC LIMIT 25
                """,
                (item_id,),
            )
        ]
        item["duplicate_candidates"] = duplicate_candidates(
            connection,
            subject_entity_id=item.get("subject_entity_id"),
            statement=item.get("statement"),
            short_label=item.get("short_label"),
            exclude_id=item_id,
        )
    finally:
        connection.close()
    item["publication_readiness"] = _publication_readiness(item)
    return item


def review_queue(config: GraphConfig) -> dict[str, Any]:
    connection = connect(config.db_path, read_only=True)
    try:
        rows = [
            dict(row)
            for row in connection.execute(
                """
                SELECT item_id, item_kind, short_label, statement, status,
                       provenance_origin, review_state, research_unit_id
                FROM research_items
                WHERE review_state='machine_suggested'
                   OR (provenance_origin='machine_suggested' AND review_state<>'human_reviewed')
                ORDER BY item_id
                """
            )
        ]
    finally:
        connection.close()
    return {"queue": rows, "count": len(rows)}


def autocomplete_sources(config: GraphConfig, query: str, limit: int = 20) -> list[dict[str, Any]]:
    needle = f"%{query}%"
    connection = connect(config.db_path, read_only=True)
    try:
        return [
            dict(row)
            for row in connection.execute(
                """
                SELECT source_id, display_title, canonical_path
                FROM source_registry
                WHERE source_id LIKE ? OR display_title LIKE ?
                ORDER BY source_id LIMIT ?
                """,
                (needle, needle, limit),
            )
        ]
    finally:
        connection.close()


def autocomplete_entities(config: GraphConfig, query: str, limit: int = 20) -> list[dict[str, Any]]:
    needle = f"%{query}%"
    connection = connect(config.db_path, read_only=True)
    try:
        return [
            dict(row)
            for row in connection.execute(
                """
                SELECT entity_id, entity_type, canonical_label, repo_record_id
                FROM entities
                WHERE entity_id LIKE ? OR canonical_label LIKE ?
                ORDER BY entity_id LIMIT ?
                """,
                (needle, needle, limit),
            )
        ]
    finally:
        connection.close()


def list_units(config: GraphConfig) -> list[dict[str, Any]]:
    connection = connect(config.db_path, read_only=True)
    try:
        return [
            dict(row)
            for row in connection.execute(
                "SELECT unit_id, title, path, heading_id FROM research_units ORDER BY unit_id"
            )
        ]
    finally:
        connection.close()


def get_marker(config: GraphConfig, marker_id: str) -> dict[str, Any] | None:
    """Marker detail for the editing UI: marker row, unit location, mapped
    items in display order, and the recent marker_revisions audit trail."""
    connection = connect(config.db_path, read_only=True)
    try:
        row = connection.execute(
            """
            SELECT m.*, u.path AS unit_path, u.heading_id AS unit_heading,
                   u.title AS unit_title
            FROM prose_markers AS m
            JOIN research_units AS u ON u.unit_id=m.research_unit_id
            WHERE m.marker_id=?
            """,
            (marker_id,),
        ).fetchone()
        if row is None:
            return None
        marker = dict(row)
        marker["token"] = f"<!-- graph-marker: {marker_id} -->"
        marker["items"] = [
            dict(member)
            for member in connection.execute(
                """
                SELECT mi.marker_role, mi.display_order, mi.cross_unit_reason,
                       mi.cross_unit_reviewed_by, i.item_id, i.item_kind,
                       i.short_label, i.statement, i.status AS item_status,
                       i.visibility AS item_visibility,
                       i.research_unit_id AS item_unit_id
                FROM prose_marker_items AS mi
                JOIN research_items AS i ON i.item_id=mi.item_id
                WHERE mi.marker_id=?
                ORDER BY mi.display_order, i.item_id
                """,
                (marker_id,),
            )
        ]
        marker["revisions"] = [
            dict(rev)
            for rev in connection.execute(
                """
                SELECT revision_id, database_revision, changed_at, changed_by,
                       change_kind
                FROM marker_revisions WHERE marker_id=?
                ORDER BY revision_id DESC LIMIT 10
                """,
                (marker_id,),
            )
        ]
        return marker
    finally:
        connection.close()


# Record types with directly addressable ids, checked by lookup_ids in this
# order (research items first — they are the most common paste).
_ID_LOOKUPS = (
    ("research_item", "research_items", "item_id", "short_label", "statement"),
    ("prose_marker", "prose_markers", "marker_id", "research_unit_id", "primary_item_id"),
    ("entity", "entities", "entity_id", "canonical_label", "entity_type"),
    ("research_unit", "research_units", "unit_id", "title", "path"),
    ("source", "source_registry", "source_id", "display_title", "canonical_path"),
)


def lookup_ids(config: GraphConfig, terms: list[str]) -> list[dict[str, Any]]:
    """Direct id lookup for pasted identifiers (G13-RI-…, G13-PM-…, entity,
    unit, and source ids). Complements FTS, which indexes prose text only and
    therefore never matches a marker id."""
    hits: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    connection = connect(config.db_path, read_only=True)
    try:
        for term in terms:
            needle = term.strip()
            if len(needle) < 3:
                continue
            for record_type, table, id_col, label_col, extra_col in _ID_LOOKUPS:
                for row in connection.execute(
                    f"""
                    SELECT {id_col} AS record_id, {label_col} AS label,
                           {extra_col} AS extra
                    FROM {table}
                    WHERE {id_col} LIKE ? ORDER BY {id_col} LIMIT 5
                    """,
                    (f"%{needle}%",),
                ):
                    key = (record_type, row["record_id"])
                    if key in seen:
                        continue
                    seen.add(key)
                    hits.append(
                        {
                            "record_type": record_type,
                            "record_id": row["record_id"],
                            "rank": -1000.0,  # id hits sort ahead of FTS matches
                            "snippet": " · ".join(
                                str(v) for v in (row["label"], row["extra"]) if v
                            ),
                        }
                    )
    finally:
        connection.close()
    return hits


def neighborhood(config: GraphConfig, *, kind: str, node_id: str) -> dict[str, Any] | None:
    from .queries import get_impact, get_item, get_source, get_unit

    if kind == "marker":
        marker = get_marker(config, node_id)
        return None if marker is None else {"kind": "marker", "id": node_id, "marker": marker}
    if kind == "item":
        detail = get_item(config, node_id)
        impact = get_impact(config, node_id)
        if detail is None:
            return None
        return {"kind": "item", "id": node_id, "item": detail, "impact": impact}
    if kind == "source":
        source = get_source(config, node_id)
        return None if source is None else {"kind": "source", "id": node_id, "source": source}
    if kind == "unit":
        unit = get_unit(config, node_id)
        return None if unit is None else {"kind": "unit", "id": node_id, "unit": unit}
    if kind in ("entity", "place", "person"):
        connection = connect(config.db_path, read_only=True)
        try:
            entity = connection.execute(
                "SELECT * FROM entities WHERE entity_id=?", (node_id,)
            ).fetchone()
            if entity is None:
                return None
            items = [
                dict(row)
                for row in connection.execute(
                    """
                    SELECT DISTINCT i.item_id, i.item_kind, i.short_label, i.statement,
                           i.status, i.visibility
                    FROM research_items AS i
                    LEFT JOIN item_entities AS ie ON ie.item_id=i.item_id
                    WHERE i.subject_entity_id=? OR ie.entity_id=?
                    ORDER BY i.item_id
                    """,
                    (node_id, node_id),
                )
            ]
            aliases = [
                dict(row)
                for row in connection.execute(
                    "SELECT alias, alias_type FROM entity_aliases WHERE entity_id=? ORDER BY alias",
                    (node_id,),
                )
            ]
            return {
                "kind": "entity",
                "id": node_id,
                "entity": dict(entity),
                "aliases": aliases,
                "items": items,
            }
        finally:
            connection.close()
    raise ChangeError(f"Unknown neighborhood kind: {kind!r}")
