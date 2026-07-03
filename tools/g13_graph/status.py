"""Revision-aware graph status reporting."""

from __future__ import annotations

from typing import Any

from .config import GraphConfig
from .db import connect
from .exporter import latest_snapshot_revision, recovery_revision
from .schema_manager import current_schema_version
from .sources import mirror_state
from .validation import validate_connection


def _tier_state(live: int, backup: int | None) -> str:
    if backup is None:
        return "missing"
    if backup < live:
        return "behind"
    if backup > live:
        return "ahead"
    return "current"


def graph_status(config: GraphConfig) -> dict[str, Any]:
    result: dict[str, Any] = {
        "database_path": str(config.db_path),
        "database_exists": config.db_path.exists(),
        "schema_version": None,
        "database_revision": None,
        "source_registry_state": "unavailable",
        "recovery_export_revision": recovery_revision(config.recovery_path),
        "latest_snapshot_revision": latest_snapshot_revision(config.snapshots_dir),
        "recovery_state": "unavailable",
        "snapshot_state": "unavailable",
        "database_ahead_of_recovery": False,
        "database_ahead_of_snapshot": False,
        "validation_state": "unavailable",
        "validation_errors": 0,
        "validation_warnings": 0,
    }
    if not config.db_path.exists():
        return result
    connection = connect(config.db_path, read_only=True)
    try:
        result["schema_version"] = current_schema_version(connection)
        live_revision = int(
            connection.execute(
                "SELECT database_revision FROM graph_meta WHERE singleton_id=1"
            ).fetchone()[0]
        )
        result["database_revision"] = live_revision
        try:
            result["source_registry_state"] = mirror_state(
                connection, config.sources_path, repo_root=config.repo_root
            )["state"]
        except (OSError, ValueError):
            result["source_registry_state"] = "unreadable"
        recovery = result["recovery_export_revision"]
        snapshot = result["latest_snapshot_revision"]
        result["recovery_state"] = _tier_state(live_revision, recovery)
        result["snapshot_state"] = _tier_state(live_revision, snapshot)
        result["database_ahead_of_recovery"] = (
            recovery is None or live_revision > recovery
        )
        result["database_ahead_of_snapshot"] = (
            snapshot is None or live_revision > snapshot
        )
        issues = validate_connection(connection, config)
        errors = sum(issue.severity == "error" for issue in issues)
        warnings = sum(issue.severity == "warning" for issue in issues)
        result["validation_errors"] = errors
        result["validation_warnings"] = warnings
        result["validation_state"] = (
            "invalid" if errors else ("warnings" if warnings else "valid")
        )
    finally:
        connection.close()
    return result
