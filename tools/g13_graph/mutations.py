"""Small transactional mutation contract used by tests and the graph editor.

`apply_item_update` is the single reusable item-field UPDATE path. Both the
standalone `update_item` helper (which owns its own transaction and recovery
refresh) and the graph editor's transactional save orchestration (`editor.py`)
call it, so field-update semantics live in exactly one place.
"""

from __future__ import annotations

import sqlite3
from typing import Any

from .config import GraphConfig
from .db import connect, transaction
from .revisions import advance_revision, record_item_revision

# Fields the editor and CLI may set directly on a research item. Managed columns
# (item_id, created_at, updated_at, revision, provenance_origin) are excluded:
# identity and provenance never change through an ordinary field edit, and the
# timestamp/revision bookkeeping is applied by the write path itself.
ALLOWED_ITEM_FIELDS = frozenset(
    {
        "item_kind",
        "subject_entity_id",
        "statement",
        "short_label",
        "summary",
        "status",
        "assessment_confidence_label",
        "assessment_confidence_value",
        "transcription_confidence_value",
        "knowledge_valid_from",
        "knowledge_valid_to",
        "research_unit_id",
        "superseded_by",
        "visibility",
        "excerpt_publishable",
        "restriction_reason",
        "review_state",
        "reviewed_by",
        "reviewed_at",
        "qualifiers_json",
        "tags_json",
        "notes",
    }
)


def apply_item_update(
    connection: sqlite3.Connection,
    item_id: str,
    changes: dict[str, Any],
    *,
    timestamp: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Apply a validated field update to one item inside an open transaction.

    Returns the (before, after) row snapshots for revision logging. Raises
    ``ValueError`` for empty/unsupported field sets and ``KeyError`` for an
    unknown item. The caller owns the surrounding transaction, revision advance,
    and audit write.
    """
    if not changes or not set(changes) <= ALLOWED_ITEM_FIELDS:
        raise ValueError("Changes contain no fields or unsupported fields.")
    before_row = connection.execute(
        "SELECT * FROM research_items WHERE item_id=?", (item_id,)
    ).fetchone()
    if before_row is None:
        raise KeyError(item_id)
    before = dict(before_row)
    assignments = ", ".join(f'"{key}"=?' for key in changes)
    connection.execute(
        f"""
        UPDATE research_items
        SET {assignments}, updated_at=?, revision=revision+1
        WHERE item_id=?
        """,
        (*changes.values(), timestamp, item_id),
    )
    after = dict(
        connection.execute(
            "SELECT * FROM research_items WHERE item_id=?", (item_id,)
        ).fetchone()
    )
    return before, after


def update_item(
    config: GraphConfig,
    item_id: str,
    changes: dict[str, Any],
    *,
    changed_by: str = "g13_graph",
    refresh_recovery: bool = True,
) -> int:
    connection = connect(config.db_path)
    try:
        with transaction(connection):
            revision, timestamp = advance_revision(connection)
            before, after = apply_item_update(
                connection, item_id, changes, timestamp=timestamp
            )
            record_item_revision(
                connection,
                database_revision=revision,
                item_id=item_id,
                changed_by=changed_by,
                change_kind="update",
                field_summary=", ".join(sorted(changes)),
                before=before,
                after=after,
                changed_at=timestamp,
            )
    finally:
        connection.close()
    if refresh_recovery:
        from .lifecycle import refresh_after_commit

        refresh_after_commit(config)
    return revision
