"""Rebuildable FTS5 indexes and graph-wide text search."""

from __future__ import annotations

import sqlite3
from typing import Any

from .config import GraphConfig
from .constants import DERIVED_INDEX_NAMES
from .db import connect, transaction
from .revisions import current_revision
from .util import utc_now


def rebuild_derived_indexes(connection: sqlite3.Connection) -> dict[str, int]:
    """Rebuild every non-canonical FTS table from relational graph content."""
    revision = current_revision(connection)
    rebuilt_at = utc_now()
    counts: dict[str, int] = {}

    connection.execute("DELETE FROM research_items_fts")
    for item in connection.execute(
        """
        SELECT item_id, statement, short_label, summary, qualifiers_json
        FROM research_items ORDER BY item_id
        """
    ):
        alignment = "\n".join(
            row[0]
            for row in connection.execute(
                """
                SELECT alignment_note FROM item_sources
                WHERE item_id=? AND alignment_note IS NOT NULL
                ORDER BY source_id, role, locator
                """,
                (item["item_id"],),
            )
        )
        connection.execute(
            """
            INSERT INTO research_items_fts(
                item_id, statement, short_label, summary, qualifiers,
                alignment_notes
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                item["item_id"],
                item["statement"],
                item["short_label"],
                item["summary"],
                item["qualifiers_json"],
                alignment,
            ),
        )
    counts["research_items_fts"] = int(
        connection.execute("SELECT count(*) FROM research_items_fts").fetchone()[0]
    )

    connection.execute("DELETE FROM entities_fts")
    for entity in connection.execute(
        "SELECT * FROM entities ORDER BY entity_id"
    ):
        aliases = "\n".join(
            row[0]
            for row in connection.execute(
                """
                SELECT alias FROM entity_aliases
                WHERE entity_id=? ORDER BY alias, alias_type
                """,
                (entity["entity_id"],),
            )
        )
        connection.execute(
            """
            INSERT INTO entities_fts(
                entity_id, canonical_label, description, aliases
            ) VALUES (?, ?, ?, ?)
            """,
            (
                entity["entity_id"],
                entity["canonical_label"],
                entity["description"],
                aliases,
            ),
        )
    counts["entities_fts"] = int(
        connection.execute("SELECT count(*) FROM entities_fts").fetchone()[0]
    )

    connection.execute("DELETE FROM research_units_fts")
    connection.execute(
        """
        INSERT INTO research_units_fts(unit_id, title, scope_summary)
        SELECT unit_id, title, scope_summary
        FROM research_units ORDER BY unit_id
        """
    )
    counts["research_units_fts"] = int(
        connection.execute("SELECT count(*) FROM research_units_fts").fetchone()[0]
    )

    for index_name in DERIVED_INDEX_NAMES:
        connection.execute(
            """
            INSERT INTO derived_index_meta(
                index_name, database_revision, rebuilt_at, row_count
            ) VALUES (?, ?, ?, ?)
            ON CONFLICT(index_name) DO UPDATE SET
                database_revision=excluded.database_revision,
                rebuilt_at=excluded.rebuilt_at,
                row_count=excluded.row_count
            """,
            (index_name, revision, rebuilt_at, counts[index_name]),
        )
    return counts


def rebuild_database_indexes(config: GraphConfig) -> dict[str, int]:
    connection = connect(config.db_path)
    try:
        with transaction(connection):
            return rebuild_derived_indexes(connection)
    finally:
        connection.close()


def derived_index_state(connection: sqlite3.Connection) -> dict[str, Any]:
    revision = current_revision(connection)
    tables = {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE name IN "
            "('research_items_fts','entities_fts','research_units_fts','derived_index_meta')"
        )
    }
    if len(tables) != 4:
        return {
            "state": "missing",
            "database_revision": revision,
            "index_revisions": {},
        }
    rows = {
        row["index_name"]: {
            "database_revision": int(row["database_revision"]),
            "row_count": int(row["row_count"]),
        }
        for row in connection.execute(
            "SELECT * FROM derived_index_meta ORDER BY index_name"
        )
    }
    expected_counts = {
        "research_items_fts": int(
            connection.execute("SELECT count(*) FROM research_items").fetchone()[0]
        ),
        "entities_fts": int(
            connection.execute("SELECT count(*) FROM entities").fetchone()[0]
        ),
        "research_units_fts": int(
            connection.execute("SELECT count(*) FROM research_units").fetchone()[0]
        ),
    }
    actual_counts = {
        index_name: int(
            connection.execute(f"SELECT count(*) FROM {index_name}").fetchone()[0]
        )
        for index_name in DERIVED_INDEX_NAMES
    }
    current = (
        set(rows) == set(DERIVED_INDEX_NAMES)
        and all(row["database_revision"] == revision for row in rows.values())
        and all(
            rows[index_name]["row_count"] == expected_counts[index_name]
            == actual_counts[index_name]
            for index_name in DERIVED_INDEX_NAMES
        )
    )
    return {
        "state": "current" if current else "stale",
        "database_revision": revision,
        "index_revisions": rows,
        "expected_counts": expected_counts,
        "actual_counts": actual_counts,
    }


def _fts_query(terms: list[str]) -> str:
    clean = [term.strip() for term in terms if term.strip()]
    if not clean:
        raise ValueError("At least one non-empty search term is required.")
    return " AND ".join(f'"{term.replace(chr(34), chr(34) * 2)}"' for term in clean)


def search_graph(
    config: GraphConfig, terms: list[str], *, limit: int = 25
) -> dict[str, Any]:
    if limit < 1:
        raise ValueError("Search limit must be positive.")
    query = _fts_query(terms)
    connection = connect(config.db_path, read_only=True)
    try:
        state = derived_index_state(connection)
        if state["state"] != "current":
            raise RuntimeError("Derived FTS indexes are not current; run reindex.")
        results: list[dict[str, Any]] = []
        specifications = (
            ("research_item", "research_items_fts", "item_id"),
            ("entity", "entities_fts", "entity_id"),
            ("research_unit", "research_units_fts", "unit_id"),
        )
        for record_type, table, id_column in specifications:
            for row in connection.execute(
                f"""
                SELECT {id_column} AS record_id, bm25({table}) AS rank,
                       snippet({table}, -1, '[', ']', ' … ', 18) AS snippet
                FROM {table}
                WHERE {table} MATCH ?
                ORDER BY rank, record_id
                LIMIT ?
                """,
                (query, limit),
            ):
                results.append(
                    {
                        "record_type": record_type,
                        "record_id": row["record_id"],
                        "rank": row["rank"],
                        "snippet": row["snippet"],
                    }
                )
        results.sort(key=lambda row: (row["rank"], row["record_type"], row["record_id"]))
        return {
            "terms": terms,
            "results": results[:limit],
            "result_count": min(len(results), limit),
        }
    finally:
        connection.close()
