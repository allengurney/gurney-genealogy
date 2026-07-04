"""Transactional batch authoring for a research-topic increment (Phase G3 tool).

`seed` is one-time bootstrap and refuses a non-empty database, and the editor's
`commit_change` applies exactly one op per transaction. Authoring a whole topic
unit at once — a research unit, new entities, several items with their
dates/sources/entities/publications, and the relations between them — needs a
single atomic batch. That is what this module provides, reusing the editor's op
handlers, delta-blocking validation, audit, and post-commit refresh so batch and
single-op edits share one code path.

Batch shape (JSON)::

    {
      "units":     [ {unit_id, path, heading_id, title, scope_summary?, review_state?}, ... ],
      "entities":  [ {entity_id, entity_type, canonical_label, description?, repo_record_id?}, ... ],
      "items":     [ {"item": {...}, "dates": [...], "sources": [...],
                      "entities": [...], "publications": [...],
                      "negative_result_scope": {...}}, ... ],
      "relations": [ {from_item_id, relation_type, to_item_id, bearing?, strength?, explanation?}, ... ],
      "markers": [ {marker_id, research_unit_id, primary_item_id,
                     visibility?, status?}, ... ],
      "marker_items": [ {marker_id, item_id, marker_role, display_order,
                         cross_unit_reason?, cross_unit_reviewed_by?}, ... ]
    }

Ops run in dependency order (units → entities → items → relations → markers →
marker items) inside one `BEGIN IMMEDIATE` transaction. Validation is
delta-blocking exactly as in the
editor: only *newly introduced* blocking error codes abort the batch, and derived
staleness never blocks. On any failure the whole batch rolls back. `preview_batch`
runs the same staging and rolls back unconditionally — the built-in dry run.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .config import GraphConfig
from .constants import MARKER_ROLES, MARKER_STATUSES, VISIBILITIES
from .db import connect
from .editor import (
    OPS,
    ValidationBlocked,
    _blocking_error_keys,
    _diff_for_intents,
)
from .lifecycle import PostCommitRefreshError, refresh_after_commit
from .revisions import advance_revision, record_item_revision
from .util import canonical_json, utc_now
from .validation import MARKER_ID_RE, issues_as_dicts, validate_connection


def _batch_ops(batch: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    ops: list[tuple[str, dict[str, Any]]] = []
    for unit in batch.get("units", []):
        ops.append(("create_research_unit", {"unit": unit}))
    for entity in batch.get("entities", []):
        ops.append(("create_entity", {"entity": entity}))
    for item in batch.get("items", []):
        ops.append(("create_item", item))
    for relation in batch.get("relations", []):
        ops.append(("add_relation", relation))
    return ops


def _batch_count(batch: dict[str, Any]) -> int:
    count = len(_batch_ops(batch))
    count += len(batch.get("markers", []))
    count += len(batch.get("marker_items", []))
    if count == 0:
        raise ValueError(
            "Batch contains no units, entities, items, relations, markers, or marker_items."
        )
    return count


def _preflight_collisions(connection: Any, batch: dict[str, Any]) -> None:
    """Fail early with a clear message on IDs that already exist, so a re-run of
    an already-applied batch does not raise a cryptic IntegrityError."""
    collisions: list[str] = []
    for unit in batch.get("units", []):
        if connection.execute(
            "SELECT 1 FROM research_units WHERE unit_id=?", (unit.get("unit_id"),)
        ).fetchone():
            collisions.append(f"unit {unit.get('unit_id')}")
    for entity in batch.get("entities", []):
        if connection.execute(
            "SELECT 1 FROM entities WHERE entity_id=?", (entity.get("entity_id"),)
        ).fetchone():
            collisions.append(f"entity {entity.get('entity_id')}")
    for item in batch.get("items", []):
        item_id = (item.get("item") or {}).get("item_id")
        if item_id and connection.execute(
            "SELECT 1 FROM research_items WHERE item_id=?", (item_id,)
        ).fetchone():
            collisions.append(f"item {item_id}")
    for marker in batch.get("markers", []):
        marker_id = marker.get("marker_id")
        if marker_id and connection.execute(
            "SELECT 1 FROM prose_markers WHERE marker_id=?", (marker_id,)
        ).fetchone():
            collisions.append(f"marker {marker_id}")
    for member in batch.get("marker_items", []):
        marker_id = member.get("marker_id")
        item_id = member.get("item_id")
        if marker_id and item_id and connection.execute(
            """
            SELECT 1 FROM prose_marker_items
            WHERE marker_id=? AND item_id=?
            """,
            (marker_id, item_id),
        ).fetchone():
            collisions.append(f"marker item {marker_id}:{item_id}")
    if collisions:
        raise ValueError("Batch IDs already exist: " + ", ".join(sorted(collisions)))


def _insert_row(connection: Any, table: str, row: dict[str, Any]) -> None:
    valid = {
        value["name"]
        for value in connection.execute(f'PRAGMA table_info("{table}")')
    }
    payload = {
        key: value for key, value in row.items() if key in valid and value is not None
    }
    if not payload:
        raise ValueError(f"No valid columns supplied for {table}.")
    names = ", ".join(f'"{column}"' for column in payload)
    placeholders = ", ".join("?" for _ in payload)
    connection.execute(
        f'INSERT INTO "{table}" ({names}) VALUES ({placeholders})',
        tuple(payload.values()),
    )


def _marker_snapshot(connection: Any, marker_id: str) -> dict[str, Any]:
    marker = connection.execute(
        "SELECT * FROM prose_markers WHERE marker_id=?", (marker_id,)
    ).fetchone()
    if marker is None:
        raise ValueError(f"Marker does not exist after staging: {marker_id}")
    result = dict(marker)
    result["items"] = [
        dict(row)
        for row in connection.execute(
            """
            SELECT * FROM prose_marker_items
            WHERE marker_id=?
            ORDER BY display_order, item_id
            """,
            (marker_id,),
        )
    ]
    return result


def _stage_markers(
    connection: Any, batch: dict[str, Any], ts: str
) -> list[tuple[str, dict[str, Any]]]:
    marker_ids: list[str] = []
    for raw in batch.get("markers", []):
        marker = dict(raw)
        missing = [
            key
            for key in ("marker_id", "research_unit_id", "primary_item_id")
            if marker.get(key) in (None, "")
        ]
        if missing:
            raise ValueError(f"Marker missing required field(s): {', '.join(missing)}")
        if MARKER_ID_RE.fullmatch(marker["marker_id"]) is None:
            raise ValueError(
                f"Invalid marker ID {marker['marker_id']!r}; expected PREFIX-PM-000000."
            )
        marker.setdefault("visibility", "repo_only")
        marker.setdefault("status", "active")
        if marker["visibility"] not in VISIBILITIES:
            raise ValueError(f"Invalid marker visibility: {marker['visibility']!r}")
        if marker["status"] not in MARKER_STATUSES:
            raise ValueError(f"Invalid marker status: {marker['status']!r}")
        marker["created_at"] = ts
        marker["updated_at"] = ts
        _insert_row(connection, "prose_markers", marker)
        marker_ids.append(marker["marker_id"])
    for raw in batch.get("marker_items", []):
        member = dict(raw)
        missing = [
            key
            for key in ("marker_id", "item_id", "marker_role", "display_order")
            if member.get(key) in (None, "")
        ]
        if missing:
            raise ValueError(
                f"Marker item missing required field(s): {', '.join(missing)}"
            )
        if member["marker_id"] not in marker_ids:
            raise ValueError(
                "author-batch marker_items must belong to a marker created "
                f"in the same batch: {member['marker_id']}"
            )
        if member["marker_role"] not in MARKER_ROLES:
            raise ValueError(f"Invalid marker role: {member['marker_role']!r}")
        _insert_row(connection, "prose_marker_items", member)
    return [
        (marker_id, _marker_snapshot(connection, marker_id))
        for marker_id in marker_ids
    ]


def _stage(connection: Any, config: GraphConfig, batch: dict[str, Any], ts: str, by: str):
    intents = []
    for op, params in _batch_ops(batch):
        staged = OPS[op](connection, params, ts, by)
        intents.extend(staged.revisions)
    marker_intents = _stage_markers(connection, batch, ts)
    return intents, marker_intents


def preview_batch(config: GraphConfig, batch: dict[str, Any]) -> dict[str, Any]:
    """Stage the whole batch, validate, compute the item diff, then roll back.
    Nothing is committed — the built-in dry run."""
    op_count = _batch_count(batch)
    by = batch.get("changed_by", "g13-authoring")
    connection = connect(config.db_path)
    try:
        _preflight_collisions(connection, batch)
        connection.execute("BEGIN IMMEDIATE")
        try:
            before = _blocking_error_keys(connection, config)
            ts = utc_now()
            intents, marker_intents = _stage(connection, config, batch, ts, by)
            issues = issues_as_dicts(validate_connection(connection, config, include_recovery=False))
            new_keys = _blocking_error_keys(connection, config) - before
            blocking = [dict(zip(("code", "record_id"), key)) for key in sorted(new_keys)]

            class _S:
                revisions = intents

            diff = _diff_for_intents(_S())
        finally:
            connection.rollback()
    finally:
        connection.close()
    return {
        "op_count": op_count,
        "would_write_revisions": len(intents) + len(marker_intents),
        "affected_items": sorted({i.item_id for i in intents}),
        "affected_markers": sorted(marker_id for marker_id, _ in marker_intents),
        "blocking_errors": blocking,
        "can_commit": not blocking,
        "diff": diff,
        "validation_issues": issues,
    }


def author_batch(
    config: GraphConfig,
    batch: dict[str, Any],
    *,
    changed_by: str | None = None,
    refresh_recovery: bool = True,
) -> dict[str, Any]:
    """Apply the batch in one transaction, write item_revisions, refresh recovery.

    Raises :class:`ValidationBlocked` (rolled back) if the batch introduces new
    blocking validation errors, or ``ValueError`` on ID collisions / an empty
    batch. A post-commit refresh failure leaves the content committed and returns
    ``stale=True`` (mirrors the editor's never-lose-an-edit contract)."""
    _batch_count(batch)
    by = changed_by or batch.get("changed_by", "g13-authoring")
    connection = connect(config.db_path)
    revision: int | None = None
    intents = []
    marker_intents: list[tuple[str, dict[str, Any]]] = []
    try:
        _preflight_collisions(connection, batch)
        connection.execute("BEGIN IMMEDIATE")
        try:
            before = _blocking_error_keys(connection, config)
            revision, ts = advance_revision(connection)
            intents, marker_intents = _stage(connection, config, batch, ts, by)
            new_keys = _blocking_error_keys(connection, config) - before
            if new_keys:
                raise ValidationBlocked(
                    [dict(zip(("code", "record_id"), key)) for key in sorted(new_keys)]
                )
            for intent in intents:
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
            for marker_id, after in marker_intents:
                connection.execute(
                    """
                    INSERT INTO marker_revisions(
                        marker_id, database_revision, changed_at, changed_by,
                        change_kind, before_json, after_json
                    ) VALUES (?, ?, ?, ?, 'create', NULL, ?)
                    """,
                    (marker_id, revision, ts, by, canonical_json(after)),
                )
        except BaseException:
            connection.rollback()
            raise
        else:
            connection.commit()
    finally:
        connection.close()

    stale = False
    refresh_error: str | None = None
    if refresh_recovery:
        try:
            refresh_after_commit(config)
        except PostCommitRefreshError as exc:
            stale = True
            refresh_error = str(exc)
    return {
        "committed": True,
        "database_revision": revision,
        "revisions_written": len(intents) + len(marker_intents),
        "affected_items": sorted({i.item_id for i in intents}),
        "affected_markers": sorted(marker_id for marker_id, _ in marker_intents),
        "units": [u.get("unit_id") for u in batch.get("units", [])],
        "stale": stale,
        "refresh_error": refresh_error,
    }


def load_batch(path: Path) -> dict[str, Any]:
    import json

    with path.open("r", encoding="utf-8") as stream:
        batch = json.load(stream)
    if not isinstance(batch, dict):
        raise ValueError("Batch file must be a JSON object.")
    return batch
