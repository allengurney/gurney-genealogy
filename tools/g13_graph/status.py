"""Revision-aware graph status reporting."""

from __future__ import annotations

from typing import Any

from .config import GraphConfig
from .db import connect
from .drift import source_hash_state
from .exporter import export_identity, latest_snapshot_identity
from .indexes import derived_index_state
from .schema_manager import current_schema_version
from .sources import mirror_state
from .validation import validate_connection


def _tier_state(
    live_revision: int,
    live_schema: int,
    backup: dict[str, int] | None,
) -> str:
    if backup is None:
        return "missing"
    if (
        backup["database_revision"] < live_revision
        or (
            backup["database_revision"] == live_revision
            and backup["schema_version"] < live_schema
        )
    ):
        return "behind"
    if (
        backup["database_revision"] > live_revision
        or (
            backup["database_revision"] == live_revision
            and backup["schema_version"] > live_schema
        )
    ):
        return "ahead"
    return "current"


def graph_status(config: GraphConfig) -> dict[str, Any]:
    result: dict[str, Any] = {
        "database_path": str(config.db_path),
        "database_exists": config.db_path.exists(),
        "schema_version": None,
        "database_revision": None,
        "source_registry_state": "unavailable",
        "recovery_export_revision": None,
        "recovery_export_schema_version": None,
        "latest_snapshot_revision": None,
        "latest_snapshot_schema_version": None,
        "recovery_state": "unavailable",
        "snapshot_state": "unavailable",
        "database_ahead_of_recovery": False,
        "database_ahead_of_snapshot": False,
        "validation_state": "unavailable",
        "validation_errors": 0,
        "validation_warnings": 0,
        "derived_index_state": "unavailable",
        "source_hash_counts": {},
    }
    recovery = export_identity(config.recovery_path)
    snapshot = latest_snapshot_identity(config.snapshots_dir)
    if recovery:
        result["recovery_export_revision"] = recovery["database_revision"]
        result["recovery_export_schema_version"] = recovery["schema_version"]
    if snapshot:
        result["latest_snapshot_revision"] = snapshot["database_revision"]
        result["latest_snapshot_schema_version"] = snapshot["schema_version"]
    if not config.db_path.exists():
        return result
    connection = connect(config.db_path, read_only=True)
    try:
        live_schema = current_schema_version(connection)
        result["schema_version"] = live_schema
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
        result["recovery_state"] = _tier_state(
            live_revision, live_schema, recovery
        )
        result["snapshot_state"] = _tier_state(
            live_revision, live_schema, snapshot
        )
        result["database_ahead_of_recovery"] = (
            result["recovery_state"] in {"missing", "behind"}
        )
        result["database_ahead_of_snapshot"] = (
            result["snapshot_state"] in {"missing", "behind"}
        )
        result["derived_index_state"] = derived_index_state(connection)["state"]
        result["source_hash_counts"] = source_hash_state(connection, config)["counts"]
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
