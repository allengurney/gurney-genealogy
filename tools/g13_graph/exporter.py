"""Deterministic NDJSON recovery export, snapshot, and restore."""

from __future__ import annotations

import json
import sqlite3
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import GraphConfig
from .constants import LOGICAL_TABLE_ORDER, SCHEMA_VERSION
from .db import connect, online_backup, transaction
from .schema_manager import current_schema_version, initialize_database
from .util import atomic_write, canonical_json, sha256_json


class ExportFormatError(ValueError):
    """Raised when an NDJSON export is incomplete or incompatible."""


@dataclass(frozen=True)
class ExportDocument:
    manifest: dict[str, Any]
    records: tuple[dict[str, Any], ...]


def _primary_key_columns(connection: sqlite3.Connection, table: str) -> list[str]:
    columns = sorted(
        (
            (int(row["pk"]), row["name"])
            for row in connection.execute(f'PRAGMA table_info("{table}")')
            if int(row["pk"]) > 0
        )
    )
    if not columns:
        raise RuntimeError(f"Logical table {table} has no primary key.")
    return [name for _, name in columns]


def _rows(connection: sqlite3.Connection, table: str) -> list[dict[str, Any]]:
    order = ", ".join(f'"{column}"' for column in _primary_key_columns(connection, table))
    return [
        dict(row)
        for row in connection.execute(f'SELECT * FROM "{table}" ORDER BY {order}')
    ]


def _logical_hash_payload(
    *,
    schema_version: int,
    database_revision: int,
    source_registry_hash: str | None,
    table_counts: dict[str, int],
    records: list[dict[str, Any]] | tuple[dict[str, Any], ...],
) -> dict[str, Any]:
    return {
        "schema_version": schema_version,
        "database_revision": database_revision,
        "source_registry_hash": source_registry_hash,
        "table_counts": table_counts,
        "records": records,
    }


def build_export(connection: sqlite3.Connection) -> ExportDocument:
    meta = dict(
        connection.execute(
            "SELECT * FROM graph_meta WHERE singleton_id=1"
        ).fetchone()
    )
    records: list[dict[str, Any]] = []
    counts: dict[str, int] = {}
    for table in LOGICAL_TABLE_ORDER:
        table_rows = _rows(connection, table)
        counts[table] = len(table_rows)
        records.extend(
            {"record_type": "row", "table": table, "row": row}
            for row in table_rows
        )
    logical_hash = sha256_json(
        _logical_hash_payload(
            schema_version=meta["schema_version"],
            database_revision=meta["database_revision"],
            source_registry_hash=meta["source_registry_hash"],
            table_counts=counts,
            records=records,
        )
    )
    manifest = {
        "record_type": "manifest",
        "format": "gurney-g13-graph-ndjson",
        "format_version": 1,
        "schema_version": meta["schema_version"],
        "database_revision": meta["database_revision"],
        # Using the revision's committed timestamp makes repeated exports of an
        # unchanged DB byte-for-byte deterministic.
        "export_timestamp": meta["updated_at"],
        "source_registry_hash": meta["source_registry_hash"],
        "table_counts": counts,
        "logical_content_hash": logical_hash,
    }
    return ExportDocument(manifest, tuple(records))


def _document_bytes(document: ExportDocument) -> bytes:
    lines = [canonical_json(document.manifest)]
    lines.extend(canonical_json(record) for record in document.records)
    return ("\n".join(lines) + "\n").encode("utf-8")


def export_recovery(config: GraphConfig) -> Path:
    connection = connect(config.db_path, read_only=True)
    try:
        document = build_export(connection)
    finally:
        connection.close()
    atomic_write(config.recovery_path, _document_bytes(document))
    return config.recovery_path


def export_snapshot(config: GraphConfig) -> Path:
    connection = connect(config.db_path, read_only=True)
    try:
        document = build_export(connection)
    finally:
        connection.close()
    revision = int(document.manifest["database_revision"])
    path = config.snapshots_dir / f"g13-context-r{revision:06d}.ndjson"
    content = _document_bytes(document)
    if path.exists() and path.read_bytes() != content:
        schema_version = int(document.manifest["schema_version"])
        path = (
            config.snapshots_dir
            / f"g13-context-s{schema_version:03d}-r{revision:06d}.ndjson"
        )
        if path.exists() and path.read_bytes() != content:
            raise RuntimeError(f"Snapshot schema/revision collision: {path}")
    if not path.exists():
        atomic_write(path, content)
    return path


def read_export(
    path: Path, *, expected_schema: int | None = SCHEMA_VERSION
) -> ExportDocument:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise ExportFormatError(f"Cannot read export: {path}") from exc
    if not lines:
        raise ExportFormatError("Export is empty.")
    try:
        manifest = json.loads(lines[0])
        records = tuple(json.loads(line) for line in lines[1:] if line.strip())
    except json.JSONDecodeError as exc:
        raise ExportFormatError(f"Invalid NDJSON: {exc}") from exc
    if (
        manifest.get("record_type") != "manifest"
        or manifest.get("format") != "gurney-g13-graph-ndjson"
        or manifest.get("format_version") != 1
    ):
        raise ExportFormatError("Missing or incompatible export manifest.")
    if (
        expected_schema is not None
        and manifest.get("schema_version") != expected_schema
    ):
        raise ExportFormatError(
            f"Export schema {manifest.get('schema_version')} is incompatible "
            f"with schema {expected_schema}."
        )
    seen_order: list[str] = []
    counts = {table: 0 for table in LOGICAL_TABLE_ORDER}
    for record in records:
        table = record.get("table")
        if (
            record.get("record_type") != "row"
            or table not in counts
            or not isinstance(record.get("row"), dict)
        ):
            raise ExportFormatError("Invalid row record.")
        if not seen_order or seen_order[-1] != table:
            seen_order.append(table)
        counts[table] += 1
    expected_order = [table for table in LOGICAL_TABLE_ORDER if counts[table]]
    if seen_order != expected_order:
        raise ExportFormatError("Logical tables are missing or out of order.")
    if manifest.get("table_counts") != counts:
        raise ExportFormatError("Manifest table counts do not match row records.")
    expected_hash = sha256_json(
        _logical_hash_payload(
            schema_version=manifest["schema_version"],
            database_revision=manifest["database_revision"],
            source_registry_hash=manifest.get("source_registry_hash"),
            table_counts=counts,
            records=records,
        )
    )
    if manifest.get("logical_content_hash") != expected_hash:
        raise ExportFormatError("Logical content hash mismatch.")
    if counts["graph_meta"] != 1:
        raise ExportFormatError("Export must contain exactly one graph_meta row.")
    meta_record = next(record for record in records if record["table"] == "graph_meta")
    if (
        meta_record["row"].get("schema_version") != manifest["schema_version"]
        or meta_record["row"].get("database_revision")
        != manifest["database_revision"]
        or meta_record["row"].get("source_registry_hash")
        != manifest.get("source_registry_hash")
    ):
        raise ExportFormatError("Manifest does not match graph_meta.")
    return ExportDocument(manifest, records)


def recovery_revision(
    path: Path, *, expected_schema: int | None = None
) -> int | None:
    if not path.exists():
        return None
    try:
        return int(
            read_export(path, expected_schema=expected_schema).manifest[
                "database_revision"
            ]
        )
    except (ExportFormatError, TypeError, ValueError):
        return None


def export_identity(path: Path) -> dict[str, int] | None:
    if not path.exists():
        return None
    try:
        manifest = read_export(path, expected_schema=None).manifest
        return {
            "schema_version": int(manifest["schema_version"]),
            "database_revision": int(manifest["database_revision"]),
        }
    except (ExportFormatError, TypeError, ValueError):
        return None


def latest_snapshot_identity(directory: Path) -> dict[str, int] | None:
    identities: list[dict[str, int]] = []
    if directory.is_dir():
        for path in directory.glob("*.ndjson"):
            identity = export_identity(path)
            if identity is not None:
                identities.append(identity)
    return (
        max(
            identities,
            key=lambda value: (
                value["database_revision"],
                value["schema_version"],
            ),
        )
        if identities
        else None
    )


def latest_snapshot_revision(directory: Path) -> int | None:
    identity = latest_snapshot_identity(directory)
    return None if identity is None else identity["database_revision"]


def _insert_row(
    connection: sqlite3.Connection, table: str, row: dict[str, Any]
) -> None:
    valid_columns = {
        value["name"] for value in connection.execute(f'PRAGMA table_info("{table}")')
    }
    if not row or not set(row) <= valid_columns:
        raise ExportFormatError(f"Export row for {table} contains invalid columns.")
    columns = tuple(row)
    names = ", ".join(f'"{column}"' for column in columns)
    placeholders = ", ".join("?" for _ in columns)
    connection.execute(
        f'INSERT INTO "{table}" ({names}) VALUES ({placeholders})',
        tuple(row[column] for column in columns),
    )


def restore_export(config: GraphConfig, source: Path) -> Path | None:
    document = read_export(source)
    incoming_revision = int(document.manifest["database_revision"])
    existed = config.db_path.exists()
    backup_path: Path | None = None
    if not existed:
        initialize_database(config)
    connection = connect(config.db_path)
    try:
        live_revision = int(
            connection.execute(
                "SELECT database_revision FROM graph_meta WHERE singleton_id=1"
            ).fetchone()[0]
        )
        if existed:
            live_schema = current_schema_version(connection)
            recovery = export_identity(config.recovery_path)
            if recovery != {
                "schema_version": live_schema,
                "database_revision": live_revision,
            }:
                raise RuntimeError(
                    "Refusing restore: current recovery export does not match "
                    f"database schema/revision {live_schema}/{live_revision}."
                )
        if incoming_revision < live_revision:
            raise RuntimeError(
                "Refusing restore: database_revision cannot move backward "
                f"from {live_revision} to {incoming_revision}."
            )
        if existed:
            backup_path = config.db_path.with_name(
                f"{config.db_path.stem}.pre-restore-r{live_revision:06d}-"
                f"{uuid.uuid4().hex[:8]}.sqlite"
            )
            online_backup(connection, backup_path)
        records_by_table = {table: [] for table in LOGICAL_TABLE_ORDER}
        for record in document.records:
            records_by_table[record["table"]].append(record["row"])
        with transaction(connection):
            for table in reversed(LOGICAL_TABLE_ORDER):
                connection.execute(f'DELETE FROM "{table}"')
            for table in LOGICAL_TABLE_ORDER:
                for row in records_by_table[table]:
                    _insert_row(connection, table, row)
            violations = list(connection.execute("PRAGMA foreign_key_check"))
            if violations:
                raise ExportFormatError(
                    f"Restored content violates foreign keys: {violations}"
                )
    except BaseException:
        connection.close()
        if not existed:
            for suffix in ("", "-wal", "-shm"):
                candidate = Path(f"{config.db_path}{suffix}")
                if candidate.exists():
                    candidate.unlink()
        raise
    else:
        connection.close()
    from .lifecycle import refresh_after_commit

    refresh_after_commit(config)
    return backup_path
