"""Synchronize the derived source_registry mirror from data/sources.json."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import GraphConfig
from .db import connect, transaction
from .revisions import advance_revision, current_revision
from .util import sha256_bytes, sha256_json, utc_now


@dataclass(frozen=True)
class SourceMirror:
    registry_hash: str
    rows: tuple[dict[str, str], ...]


def _canonical_path(entry: dict[str, Any]) -> str:
    for key in ("corpusPath", "mediaPath", "validationPath", "url"):
        value = entry.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def _registry_source_label(path: Path, repo_root: Path | None) -> str:
    if repo_root is not None:
        try:
            return path.resolve().relative_to(repo_root.resolve()).as_posix()
        except ValueError:
            pass
    return str(path)


def load_source_registry(path: Path) -> SourceMirror:
    raw = path.read_bytes()
    data = json.loads(raw.decode("utf-8-sig"))
    sources = data.get("sources")
    if not isinstance(sources, dict):
        raise ValueError("Source registry must contain an object-valued 'sources' key.")
    rows: list[dict[str, str]] = []
    for source_id, entry in sorted(sources.items()):
        if not isinstance(entry, dict):
            raise ValueError(f"Source entry {source_id!r} is not an object.")
        title = entry.get("shortTitle") or entry.get("fullTitle") or entry.get("citation")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Source entry {source_id!r} has no human-readable title.")
        rows.append(
            {
                "source_id": source_id,
                "display_title": title.strip(),
                "canonical_path": _canonical_path(entry),
                "registry_entry_hash": sha256_json(entry),
            }
        )
    return SourceMirror(sha256_bytes(raw), tuple(rows))


def mirror_state(
    connection: sqlite3.Connection,
    source_path: Path,
    *,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    expected = load_source_registry(source_path)
    meta = connection.execute(
        "SELECT source_registry_hash FROM graph_meta WHERE singleton_id=1"
    ).fetchone()
    actual_rows = {
        row["source_id"]: row["registry_entry_hash"]
        for row in connection.execute(
            "SELECT source_id, registry_entry_hash FROM source_registry"
        )
    }
    stored_paths = {
        row[0]
        for row in connection.execute(
            "SELECT DISTINCT registry_source_path FROM source_registry"
        )
    }
    expected_rows = {
        row["source_id"]: row["registry_entry_hash"] for row in expected.rows
    }
    synchronized = (
        meta is not None
        and meta["source_registry_hash"] == expected.registry_hash
        and actual_rows == expected_rows
        and stored_paths
        in ({_registry_source_label(source_path, repo_root)}, set())
    )
    return {
        "state": "current" if synchronized else "stale",
        "expected_hash": expected.registry_hash,
        "stored_hash": None if meta is None else meta["source_registry_hash"],
        "expected_count": len(expected_rows),
        "stored_count": len(actual_rows),
    }


def sync_source_registry(config: GraphConfig, *, refresh_recovery: bool = True) -> int:
    mirror = load_source_registry(config.sources_path)
    connection = connect(config.db_path)
    try:
        if mirror_state(
            connection, config.sources_path, repo_root=config.repo_root
        )["state"] == "current":
            revision = current_revision(connection)
            if refresh_recovery:
                from .lifecycle import refresh_after_commit

                refresh_after_commit(config)
            return revision
        with transaction(connection):
            now = utc_now()
            expected_ids = {row["source_id"] for row in mirror.rows}
            for row in mirror.rows:
                connection.execute(
                    """
                    INSERT INTO source_registry(
                        source_id, display_title, canonical_path,
                        registry_entry_hash, registry_source_path, synchronized_at
                    ) VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(source_id) DO UPDATE SET
                        display_title=excluded.display_title,
                        canonical_path=excluded.canonical_path,
                        registry_entry_hash=excluded.registry_entry_hash,
                        registry_source_path=excluded.registry_source_path,
                        synchronized_at=excluded.synchronized_at
                    """,
                    (
                        row["source_id"],
                        row["display_title"],
                        row["canonical_path"],
                        row["registry_entry_hash"],
                        _registry_source_label(config.sources_path, config.repo_root),
                        now,
                    ),
                )
            existing_ids = {
                row[0] for row in connection.execute("SELECT source_id FROM source_registry")
            }
            for source_id in sorted(existing_ids - expected_ids):
                connection.execute(
                    "DELETE FROM source_registry WHERE source_id=?", (source_id,)
                )
            connection.execute(
                """
                UPDATE graph_meta
                SET source_registry_hash=?, source_registry_synced_at=?
                WHERE singleton_id=1
                """,
                (mirror.registry_hash, now),
            )
            revision, _ = advance_revision(connection, changed_at=now)
    finally:
        connection.close()
    if refresh_recovery:
        from .lifecycle import refresh_after_commit

        refresh_after_commit(config)
    return revision
