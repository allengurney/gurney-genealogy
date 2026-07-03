"""Deterministic G1B build/health report."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .config import GraphConfig
from .constants import LOGICAL_TABLE_ORDER
from .db import connect
from .drift import source_hash_state
from .indexes import derived_index_state
from .status import graph_status
from .util import atomic_write, canonical_json
from .validation import issues_as_dicts, validate_connection


def _group_counts(connection: Any, column: str) -> dict[str, int]:
    return {
        row[0]: int(row[1])
        for row in connection.execute(
            f'SELECT "{column}", count(*) FROM research_items '
            f'GROUP BY "{column}" ORDER BY "{column}"'
        )
    }


def build_report(config: GraphConfig) -> dict[str, Any]:
    if not config.db_path.exists():
        return {
            "format": "gurney-g13-graph-build-report",
            "format_version": 1,
            "status": graph_status(config),
            "validation_issues": [],
        }
    connection = connect(config.db_path, read_only=True)
    try:
        meta = dict(
            connection.execute(
                "SELECT * FROM graph_meta WHERE singleton_id=1"
            ).fetchone()
        )
        issues = validate_connection(connection, config)
        table_counts = {
            table: int(
                connection.execute(f'SELECT count(*) FROM "{table}"').fetchone()[0]
            )
            for table in LOGICAL_TABLE_ORDER
        }
        report = {
            "format": "gurney-g13-graph-build-report",
            "format_version": 1,
            "generated_from_revision_at": meta["updated_at"],
            "schema_version": meta["schema_version"],
            "database_revision": meta["database_revision"],
            "application_version": meta["application_version"],
            "status": graph_status(config),
            "table_counts": table_counts,
            "research_items": {
                "by_kind": _group_counts(connection, "item_kind"),
                "by_status": _group_counts(connection, "status"),
                "by_visibility": _group_counts(connection, "visibility"),
                "by_review_state": _group_counts(connection, "review_state"),
            },
            "derived_indexes": derived_index_state(connection),
            "source_hashes": source_hash_state(connection, config),
            "validation_issues": issues_as_dicts(issues),
        }
        return report
    finally:
        connection.close()


def write_build_report(
    config: GraphConfig, output: Path | None = None
) -> Path:
    path = (output or config.build_report_path).resolve()
    content = (canonical_json(build_report(config)) + "\n").encode("utf-8")
    atomic_write(path, content)
    return path
