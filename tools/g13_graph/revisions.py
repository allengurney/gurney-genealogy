"""Database revision and per-item audit helpers."""

from __future__ import annotations

import json
import sqlite3
from typing import Any

from .util import canonical_json, utc_now


def current_revision(connection: sqlite3.Connection) -> int:
    row = connection.execute(
        "SELECT database_revision FROM graph_meta WHERE singleton_id=1"
    ).fetchone()
    if row is None:
        raise RuntimeError("graph_meta is missing.")
    return int(row[0])


def advance_revision(connection: sqlite3.Connection, *, changed_at: str | None = None) -> tuple[int, str]:
    timestamp = changed_at or utc_now()
    revision = current_revision(connection) + 1
    connection.execute(
        """
        UPDATE graph_meta
        SET database_revision=?, updated_at=?
        WHERE singleton_id=1
        """,
        (revision, timestamp),
    )
    return revision, timestamp


def record_item_revision(
    connection: sqlite3.Connection,
    *,
    database_revision: int,
    item_id: str,
    changed_by: str,
    change_kind: str,
    field_summary: str,
    before: dict[str, Any] | None,
    after: dict[str, Any] | None,
    changed_at: str,
) -> None:
    connection.execute(
        """
        INSERT INTO item_revisions(
            database_revision, item_id, changed_at, changed_by, change_kind,
            field_summary, before_json, after_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            database_revision,
            item_id,
            changed_at,
            changed_by,
            change_kind,
            field_summary,
            None if before is None else canonical_json(before),
            None if after is None else canonical_json(after),
        ),
    )


def row_dict(row: sqlite3.Row | None) -> dict[str, Any] | None:
    return None if row is None else dict(row)
