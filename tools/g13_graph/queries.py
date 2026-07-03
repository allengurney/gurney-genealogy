"""Basic joined item reads for G1A."""

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
