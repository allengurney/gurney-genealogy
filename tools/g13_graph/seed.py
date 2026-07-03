"""One-time synthetic/bootstrap seed loader."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from .config import GraphConfig
from .constants import SEEDABLE_TABLES
from .db import connect, transaction
from .revisions import advance_revision, record_item_revision


def load_seed_records(path: Path) -> list[tuple[str, dict[str, Any]]]:
    records: list[tuple[str, dict[str, Any]]] = []
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            table = value.get("table")
            row = value.get("row")
            if table not in SEEDABLE_TABLES or not isinstance(row, dict):
                raise ValueError(f"Invalid seed record on line {line_number}.")
            records.append((table, row))
    return records


def _insert_row(
    connection: sqlite3.Connection, table: str, row: dict[str, Any]
) -> None:
    valid_columns = {
        value["name"] for value in connection.execute(f'PRAGMA table_info("{table}")')
    }
    if not row or not set(row) <= valid_columns:
        raise ValueError(f"Seed row for {table} contains invalid columns.")
    columns = tuple(row)
    placeholders = ", ".join("?" for _ in columns)
    names = ", ".join(f'"{column}"' for column in columns)
    connection.execute(
        f'INSERT INTO "{table}" ({names}) VALUES ({placeholders})',
        tuple(row[column] for column in columns),
    )


def seed_database(
    config: GraphConfig, path: Path, *, refresh_recovery: bool = True
) -> int:
    records = load_seed_records(path)
    connection = connect(config.db_path)
    try:
        if connection.execute("SELECT 1 FROM research_items LIMIT 1").fetchone():
            raise RuntimeError("Seed is one-time only: research_items is not empty.")
        with transaction(connection):
            inserted_items: list[dict[str, Any]] = []
            for table, row in records:
                _insert_row(connection, table, row)
                if table == "research_items":
                    inserted_items.append(row)
            revision, timestamp = advance_revision(connection)
            for row in inserted_items:
                stored = dict(
                    connection.execute(
                        "SELECT * FROM research_items WHERE item_id=?",
                        (row["item_id"],),
                    ).fetchone()
                )
                record_item_revision(
                    connection,
                    database_revision=revision,
                    item_id=row["item_id"],
                    changed_by="seed",
                    change_kind="create",
                    field_summary="Created by one-time seed loader.",
                    before=None,
                    after=stored,
                    changed_at=timestamp,
                )
    finally:
        connection.close()
    if refresh_recovery:
        from .lifecycle import refresh_after_commit

        refresh_after_commit(config)
    return revision
