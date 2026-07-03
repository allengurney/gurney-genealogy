"""Small transactional mutation contract used by tests and the later editor."""

from __future__ import annotations

from typing import Any

from .config import GraphConfig
from .db import connect, transaction
from .revisions import advance_revision, record_item_revision


def update_item(
    config: GraphConfig,
    item_id: str,
    changes: dict[str, Any],
    *,
    changed_by: str = "g13_graph",
    refresh_recovery: bool = True,
) -> int:
    allowed = {
        "item_kind",
        "statement",
        "short_label",
        "summary",
        "status",
        "assessment_confidence_label",
        "assessment_confidence_value",
        "transcription_confidence_value",
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
    if not changes or not set(changes) <= allowed:
        raise ValueError("Changes contain no fields or unsupported fields.")
    connection = connect(config.db_path)
    try:
        with transaction(connection):
            before_row = connection.execute(
                "SELECT * FROM research_items WHERE item_id=?", (item_id,)
            ).fetchone()
            if before_row is None:
                raise KeyError(item_id)
            before = dict(before_row)
            revision, timestamp = advance_revision(connection)
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
