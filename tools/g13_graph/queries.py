"""Basic joined item, source, unit, and direct-impact reads for G1B."""

from __future__ import annotations

from typing import Any

from .config import GraphConfig
from .db import connect


def get_item(config: GraphConfig, item_id: str) -> dict[str, Any] | None:
    connection = connect(config.db_path, read_only=True)
    try:
        row = connection.execute(
            """
            SELECT i.*, u.path AS research_path, u.heading_id AS research_heading
            FROM research_items AS i
            JOIN research_units AS u ON u.unit_id=i.research_unit_id
            WHERE i.item_id=?
            """,
            (item_id,),
        ).fetchone()
        if row is None:
            return None
        result = dict(row)
        result["dates"] = [
            dict(value)
            for value in connection.execute(
                "SELECT * FROM item_dates WHERE item_id=? ORDER BY date_role",
                (item_id,),
            )
        ]
        result["sources"] = [
            dict(value)
            for value in connection.execute(
                """
                SELECT s.*, r.display_title, r.canonical_path
                FROM item_sources AS s
                JOIN source_registry AS r ON r.source_id=s.source_id
                WHERE s.item_id=?
                ORDER BY s.source_id, s.role, s.locator
                """,
                (item_id,),
            )
        ]
        result["entities"] = [
            dict(value)
            for value in connection.execute(
                """
                SELECT ie.role, e.*
                FROM item_entities AS ie
                JOIN entities AS e ON e.entity_id=ie.entity_id
                WHERE ie.item_id=?
                ORDER BY e.entity_id, ie.role
                """,
                (item_id,),
            )
        ]
        result["outgoing_relations"] = [
            dict(value)
            for value in connection.execute(
                """
                SELECT * FROM item_relations
                WHERE from_item_id=?
                ORDER BY relation_type, to_item_id
                """,
                (item_id,),
            )
        ]
        result["incoming_relations"] = [
            dict(value)
            for value in connection.execute(
                """
                SELECT * FROM item_relations
                WHERE to_item_id=?
                ORDER BY relation_type, from_item_id
                """,
                (item_id,),
            )
        ]
        return result
    finally:
        connection.close()


def get_source(config: GraphConfig, source_id: str) -> dict[str, Any] | None:
    connection = connect(config.db_path, read_only=True)
    try:
        source = connection.execute(
            """
            SELECT r.*, h.content_hash, h.hashed_at
            FROM source_registry AS r
            LEFT JOIN source_content_hashes AS h ON h.source_id=r.source_id
            WHERE r.source_id=?
            """,
            (source_id,),
        ).fetchone()
        if source is None:
            return None
        result = dict(source)
        result["items"] = [
            dict(row)
            for row in connection.execute(
                """
                SELECT s.item_id, i.item_kind, i.short_label, i.statement,
                       s.role, s.locator, s.verification_level
                FROM item_sources AS s
                JOIN research_items AS i ON i.item_id=s.item_id
                WHERE s.source_id=?
                ORDER BY s.item_id, s.role, s.locator
                """,
                (source_id,),
            )
        ]
        result["evidence_groups"] = [
            dict(row)
            for row in connection.execute(
                """
                SELECT evidence_group_id, role, locator
                FROM evidence_group_sources
                WHERE source_id=?
                ORDER BY evidence_group_id, role, locator
                """,
                (source_id,),
            )
        ]
        return result
    finally:
        connection.close()


def get_unit(config: GraphConfig, unit_id: str) -> dict[str, Any] | None:
    connection = connect(config.db_path, read_only=True)
    try:
        unit = connection.execute(
            "SELECT * FROM research_units WHERE unit_id=?", (unit_id,)
        ).fetchone()
        if unit is None:
            return None
        result = dict(unit)
        result["items"] = [
            dict(row)
            for row in connection.execute(
                """
                SELECT item_id, item_kind, short_label, statement, status,
                       visibility, review_state
                FROM research_items WHERE research_unit_id=?
                ORDER BY item_id
                """,
                (unit_id,),
            )
        ]
        result["evidence_groups"] = [
            dict(row)
            for row in connection.execute(
                """
                SELECT * FROM evidence_groups
                WHERE research_unit_id=? ORDER BY evidence_group_id
                """,
                (unit_id,),
            )
        ]
        return result
    finally:
        connection.close()


def get_impact(config: GraphConfig, item_id: str) -> dict[str, Any] | None:
    """Return direct review surfaces without performing G2 graph expansion."""
    connection = connect(config.db_path, read_only=True)
    try:
        item = connection.execute(
            """
            SELECT item_id, item_kind, short_label, statement, status
            FROM research_items WHERE item_id=?
            """,
            (item_id,),
        ).fetchone()
        if item is None:
            return None
        relations = [
            {
                **dict(row),
                "direction": "outgoing",
                "related_item_id": row["to_item_id"],
            }
            for row in connection.execute(
                """
                SELECT * FROM item_relations
                WHERE from_item_id=?
                ORDER BY relation_type, to_item_id
                """,
                (item_id,),
            )
        ]
        relations.extend(
            {
                **dict(row),
                "direction": "incoming",
                "related_item_id": row["from_item_id"],
            }
            for row in connection.execute(
                """
                SELECT * FROM item_relations
                WHERE to_item_id=?
                ORDER BY relation_type, from_item_id
                """,
                (item_id,),
            )
        )
        publications = [
            dict(row)
            for row in connection.execute(
                """
                SELECT * FROM item_publications
                WHERE item_id=? ORDER BY publication_path, heading_id
                """,
                (item_id,),
            )
        ]
        shared_sources = [
            dict(row)
            for row in connection.execute(
                """
                SELECT DISTINCT mine.source_id, other.item_id,
                       other_item.item_kind, other_item.short_label,
                       other_item.statement
                FROM item_sources AS mine
                JOIN item_sources AS other
                  ON other.source_id=mine.source_id
                 AND other.item_id<>mine.item_id
                JOIN research_items AS other_item
                  ON other_item.item_id=other.item_id
                WHERE mine.item_id=?
                ORDER BY mine.source_id, other.item_id
                """,
                (item_id,),
            )
        ]
        return {
            "item": dict(item),
            "direct_relations": relations,
            "publication_review": publications,
            "shared_source_items": shared_sources,
            "scope": "direct-only",
        }
    finally:
        connection.close()
