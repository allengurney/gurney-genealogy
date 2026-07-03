"""Argument parsing and command dispatch for tools/g13_graph.py."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .config import load_config
from .exporter import export_recovery, export_snapshot, restore_export
from .queries import get_item
from .schema_manager import initialize_database, migrate_database
from .seed import seed_database
from .sources import sync_source_registry
from .status import graph_status
from .validation import issues_as_dicts, validate_database


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lifecycle tooling for the canonical G13 SQLite context graph."
    )
    parser.add_argument("--db", help="Override database path.")
    parser.add_argument("--export-dir", help="Override recovery export directory.")
    parser.add_argument("--sources", help="Override sources.json path.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("init", help="Create a new database and schema.")
    subparsers.add_parser("migrate", help="Apply pending guarded migrations.")
    subparsers.add_parser("sync-sources", help="Synchronize source_registry.")
    seed = subparsers.add_parser("seed", help="Load a one-time seed NDJSON file.")
    seed.add_argument("--file", required=True, type=Path)
    subparsers.add_parser("validate", help="Run structural and semantic validation.")
    subparsers.add_parser("status", help="Report database and backup-tier status.")
    export = subparsers.add_parser("export", help="Write deterministic NDJSON.")
    export_mode = export.add_mutually_exclusive_group(required=True)
    export_mode.add_argument("--recovery", action="store_true")
    export_mode.add_argument("--snapshot", action="store_true")
    restore = subparsers.add_parser("restore", help="Restore a validated NDJSON export.")
    restore.add_argument("--from", dest="source", required=True, type=Path)
    item = subparsers.add_parser("item", help="Read one joined research item.")
    item.add_argument("item_id")
    return parser


def _print(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_config(
        db_path=args.db, export_dir=args.export_dir, sources_path=args.sources
    )
    try:
        if args.command == "init":
            applied = initialize_database(config)
            path = export_recovery(config)
            _print({"database": str(config.db_path), "migrations_applied": applied, "recovery": str(path)})
        elif args.command == "migrate":
            applied = migrate_database(config)
            path = export_recovery(config)
            _print({"migrations_applied": applied, "recovery": str(path)})
        elif args.command == "sync-sources":
            revision = sync_source_registry(config)
            _print({"database_revision": revision, "sources": str(config.sources_path)})
        elif args.command == "seed":
            revision = seed_database(config, args.file)
            _print({"database_revision": revision, "seed": str(args.file)})
        elif args.command == "validate":
            issues = validate_database(config)
            _print({"valid": not any(issue.severity == "error" for issue in issues), "issues": issues_as_dicts(issues)})
            return 1 if any(issue.severity == "error" for issue in issues) else 0
        elif args.command == "status":
            _print(graph_status(config))
        elif args.command == "export":
            path = export_recovery(config) if args.recovery else export_snapshot(config)
            _print({"export": str(path)})
        elif args.command == "restore":
            backup = restore_export(config, args.source)
            _print({"restored_from": str(args.source), "safety_backup": None if backup is None else str(backup)})
        elif args.command == "item":
            item = get_item(config, args.item_id)
            if item is None:
                print(f"Item not found: {args.item_id}", file=sys.stderr)
                return 1
            _print(item)
        else:
            raise AssertionError(args.command)
    except Exception as exc:
        print(f"g13_graph: {exc}", file=sys.stderr)
        return 2
    return 0
