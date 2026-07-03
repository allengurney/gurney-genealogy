"""Path configuration for the durable graph and its tracked recovery tier."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

DB_ENV = "GURNEY_G13_GRAPH_DB"
EXPORT_ENV = "GURNEY_G13_GRAPH_EXPORT_DIR"
SOURCES_ENV = "GURNEY_G13_GRAPH_SOURCES"

DEFAULT_DB = Path(
    r"C:\Users\allen\GitDirs\gurney-genealogy-g13-graph\g13-context.sqlite"
)


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__)).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "AGENTS.md").is_file() and (candidate / "data").is_dir():
            return candidate
    raise RuntimeError("Could not locate repository root.")


@dataclass(frozen=True)
class GraphConfig:
    repo_root: Path
    db_path: Path
    export_dir: Path
    sources_path: Path

    @property
    def recovery_path(self) -> Path:
        return self.export_dir / "current.ndjson"

    @property
    def snapshots_dir(self) -> Path:
        return self.export_dir / "snapshots"


def load_config(
    *,
    db_path: str | Path | None = None,
    export_dir: str | Path | None = None,
    sources_path: str | Path | None = None,
    repo_root: str | Path | None = None,
) -> GraphConfig:
    root = Path(repo_root).resolve() if repo_root else find_repo_root()
    db = Path(db_path or os.environ.get(DB_ENV) or DEFAULT_DB).resolve()
    exports = Path(
        export_dir
        or os.environ.get(EXPORT_ENV)
        or root / "data" / "context-graphs" / "g13" / "exports"
    ).resolve()
    sources = Path(
        sources_path or os.environ.get(SOURCES_ENV) or root / "data" / "sources.json"
    ).resolve()
    return GraphConfig(root, db, exports, sources)
