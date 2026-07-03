"""Source-artifact hash baselines and source-drift detection."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .config import GraphConfig
from .db import connect, transaction
from .lifecycle import refresh_after_commit
from .revisions import (
    advance_revision,
    current_revision,
    record_item_revision,
)
from .util import sha256_bytes


def resolve_source_path(config: GraphConfig, value: str) -> Path | None:
    if not value or "://" in value:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = config.repo_root / path
    return path.resolve()


def _cited_sources(connection: Any) -> list[dict[str, Any]]:
    return [
        dict(row)
        for row in connection.execute(
            """
            SELECT DISTINCT r.source_id, r.canonical_path, h.content_hash,
                            h.hashed_at
            FROM source_registry AS r
            LEFT JOIN source_content_hashes AS h ON h.source_id=r.source_id
            WHERE r.source_id IN (SELECT source_id FROM item_sources)
               OR r.source_id IN (SELECT source_id FROM evidence_group_sources)
            ORDER BY r.source_id
            """
        )
    ]


def source_hash_state(
    connection: Any, config: GraphConfig
) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for row in _cited_sources(connection):
        path = resolve_source_path(config, row["canonical_path"])
        state = "unhashable"
        current_hash: str | None = None
        if path is not None:
            if path.is_file():
                current_hash = sha256_bytes(path.read_bytes())
                if row["content_hash"] is None:
                    state = "missing_baseline"
                elif row["content_hash"] == current_hash:
                    state = "current"
                else:
                    state = "drifted"
            else:
                state = "missing_file"
        records.append(
            {
                "source_id": row["source_id"],
                "canonical_path": row["canonical_path"],
                "resolved_path": None if path is None else str(path),
                "baseline_hash": row["content_hash"],
                "current_hash": current_hash,
                "hashed_at": row["hashed_at"],
                "state": state,
            }
        )
    counts: dict[str, int] = {}
    for record in records:
        counts[record["state"]] = counts.get(record["state"], 0) + 1
    return {"counts": counts, "sources": records}


def capture_source_hashes(
    config: GraphConfig,
    *,
    source_ids: list[str] | None = None,
    replace: bool = False,
    changed_by: str = "g13_graph",
    refresh_recovery: bool = True,
) -> dict[str, Any]:
    selected = set(source_ids or [])
    connection = connect(config.db_path)
    try:
        state = source_hash_state(connection, config)
        candidates = [
            record
            for record in state["sources"]
            if record["current_hash"] is not None
            and (not selected or record["source_id"] in selected)
            and (record["baseline_hash"] is None or replace)
            and record["baseline_hash"] != record["current_hash"]
        ]
        missing_requested = selected - {
            record["source_id"] for record in state["sources"]
        }
        if missing_requested:
            raise ValueError(
                "Requested sources are not cited/hashable graph sources: "
                + ", ".join(sorted(missing_requested))
            )
        if not candidates:
            return {
                "database_revision": current_revision(connection),
                "captured": [],
                "unchanged": True,
            }
        with transaction(connection):
            revision, timestamp = advance_revision(connection)
            accepted_sources: list[str] = []
            reviewed_items: dict[str, set[str]] = {}
            for record in candidates:
                connection.execute(
                    """
                    INSERT INTO source_content_hashes(source_id, content_hash, hashed_at)
                    VALUES (?, ?, ?)
                    ON CONFLICT(source_id) DO UPDATE SET
                        content_hash=excluded.content_hash,
                        hashed_at=excluded.hashed_at
                    """,
                    (record["source_id"], record["current_hash"], timestamp),
                )
                accepted_sources.append(record["source_id"])
                if replace and record["baseline_hash"] is not None:
                    for item in connection.execute(
                        """
                        SELECT i.* FROM research_items AS i
                        WHERE i.item_id IN (
                            SELECT s.item_id FROM item_sources AS s
                            WHERE s.source_id=?
                            UNION
                            SELECT gi.item_id
                            FROM evidence_group_sources AS gs
                            JOIN evidence_group_items AS gi
                              ON gi.evidence_group_id=gs.evidence_group_id
                            WHERE gs.source_id=?
                        )
                        ORDER BY i.item_id
                        """,
                        (record["source_id"], record["source_id"]),
                    ):
                        reviewed_items.setdefault(item["item_id"], set()).add(
                            record["source_id"]
                        )
            for item_id, item_sources in sorted(reviewed_items.items()):
                before = dict(
                    connection.execute(
                        "SELECT * FROM research_items WHERE item_id=?", (item_id,)
                    ).fetchone()
                )
                connection.execute(
                    """
                    UPDATE research_items
                    SET review_state='human_reviewed', reviewed_by=?,
                        reviewed_at=?, updated_at=?, revision=revision+1
                    WHERE item_id=?
                    """,
                    (changed_by, timestamp, timestamp, item_id),
                )
                after = dict(
                    connection.execute(
                        "SELECT * FROM research_items WHERE item_id=?", (item_id,)
                    ).fetchone()
                )
                record_item_revision(
                    connection,
                    database_revision=revision,
                    item_id=item_id,
                    changed_by=changed_by,
                    change_kind="review",
                    field_summary=(
                        "Accepted current source content hash: "
                        + ", ".join(sorted(item_sources))
                    ),
                    before=before,
                    after=after,
                    changed_at=timestamp,
                )
    finally:
        connection.close()
    if refresh_recovery:
        refresh_after_commit(config)
    return {
        "database_revision": revision,
        "captured": sorted(accepted_sources),
        "unchanged": False,
    }
