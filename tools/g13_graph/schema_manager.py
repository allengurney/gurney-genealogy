"""Ordered schema creation and guarded migration."""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

from .config import GraphConfig
from .constants import APPLICATION_VERSION, SCHEMA_VERSION
from .db import connect
from .util import utc_now

MIGRATION_PATTERN = re.compile(r"^(?P<version>\d{4})_(?P<name>.+)\.sql$")


def migration_dir() -> Path:
    return Path(__file__).with_name("schema") / "migrations"


def migrations() -> list[tuple[int, str, Path]]:
    result: list[tuple[int, str, Path]] = []
    for path in sorted(migration_dir().glob("*.sql")):
        match = MIGRATION_PATTERN.match(path.name)
        if not match:
            continue
        result.append((int(match.group("version")), match.group("name"), path))
    if not result or result[-1][0] != SCHEMA_VERSION:
        raise RuntimeError("Migration set does not match declared schema version.")
    return result


def _has_table(connection: sqlite3.Connection, table: str) -> bool:
    return (
        connection.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)
        ).fetchone()
        is not None
    )


def current_schema_version(connection: sqlite3.Connection) -> int:
    if not _has_table(connection, "schema_migrations"):
        return 0
    row = connection.execute("SELECT COALESCE(MAX(version), 0) FROM schema_migrations").fetchone()
    return int(row[0])


def initialize_database(config: GraphConfig) -> int:
    if config.db_path.exists():
        raise FileExistsError(f"Database already exists: {config.db_path}")
    connection = connect(config.db_path)
    try:
        return _apply_pending(connection)
    except BaseException:
        connection.close()
        for suffix in ("", "-wal", "-shm"):
            candidate = Path(f"{config.db_path}{suffix}")
            if candidate.exists():
                candidate.unlink()
        raise
    finally:
        if connection:
            connection.close()


def migrate_database(config: GraphConfig) -> int:
    if not config.db_path.exists():
        return initialize_database(config)
    connection = connect(config.db_path)
    try:
        current = current_schema_version(connection)
        if current >= SCHEMA_VERSION:
            return 0
        if current > 0:
            from .exporter import recovery_revision

            live_revision = int(
                connection.execute(
                    "SELECT database_revision FROM graph_meta WHERE singleton_id=1"
                ).fetchone()[0]
            )
            if (
                recovery_revision(
                    config.recovery_path, expected_schema=current
                )
                != live_revision
            ):
                raise RuntimeError(
                    "Refusing migration: current recovery export does not match "
                    f"database revision {live_revision}."
                )
        return _apply_pending(connection)
    finally:
        connection.close()


def _apply_pending(connection: sqlite3.Connection) -> int:
    applied = 0
    current = current_schema_version(connection)
    for version, name, path in migrations():
        if version <= current:
            continue
        sql = path.read_text(encoding="utf-8")
        now = utc_now()
        try:
            connection.executescript("BEGIN IMMEDIATE;\n" + sql)
            connection.execute(
                "INSERT INTO schema_migrations(version, name, applied_at) VALUES (?, ?, ?)",
                (version, name, now),
            )
            if version == 1:
                connection.execute(
                    """
                    INSERT INTO graph_meta(
                        singleton_id, schema_version, database_revision,
                        created_at, updated_at, application_version
                    ) VALUES (1, ?, 0, ?, ?, ?)
                    """,
                    (version, now, now, APPLICATION_VERSION),
                )
            else:
                connection.execute(
                    """
                    UPDATE graph_meta
                    SET schema_version=?, updated_at=?, application_version=?
                    WHERE singleton_id=1
                    """,
                    (version, now, APPLICATION_VERSION),
                )
            if version >= 2:
                from .indexes import rebuild_derived_indexes

                rebuild_derived_indexes(connection)
            connection.commit()
        except BaseException:
            connection.rollback()
            raise
        current = version
        applied += 1
    return applied
