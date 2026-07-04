"""Argument parsing and command dispatch for tools/g13_graph.py."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .config import load_config
from .context import compile_context
from .drift import capture_source_hashes
from .exporter import export_recovery, export_snapshot, restore_export
from .indexes import rebuild_database_indexes, search_graph
from .queries import get_impact, get_item, get_source, get_unit
from .report import write_build_report
from .schema_manager import initialize_database, migrate_database
from .seed import seed_database
from .sources import sync_source_registry
from .status import graph_status
from .validation import issues_as_dicts, validate_database
from .website import export_website


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
    website = subparsers.add_parser(
        "export-website",
        help="Write the G5 static public export (public items + publishable excerpts only).",
    )
    website.add_argument("--out", type=Path, default=None)
    item = subparsers.add_parser("item", help="Read one joined research item.")
    item.add_argument("item_id")
    source = subparsers.add_parser("source", help="Read one source and graph uses.")
    source.add_argument("source_id")
    unit = subparsers.add_parser("unit", help="Read one research unit and its items.")
    unit.add_argument("unit_id")
    impact = subparsers.add_parser(
        "impact", help="Read direct relation/publication impact for one item."
    )
    impact.add_argument("item_id")
    search = subparsers.add_parser("search", help="Search rebuildable FTS indexes.")
    search.add_argument("--terms", nargs="+", required=True)
    search.add_argument("--limit", type=int, default=25)
    subparsers.add_parser("reindex", help="Rebuild all derived FTS indexes.")
    hashes = subparsers.add_parser(
        "hash-sources", help="Capture content hashes for cited local sources."
    )
    hashes.add_argument("--source-id", action="append", default=[])
    hashes.add_argument(
        "--accept-current",
        action="store_true",
        help="Replace drifted baselines and write item review revisions.",
    )
    hashes.add_argument("--changed-by", default="g13_graph")
    report = subparsers.add_parser("report", help="Write deterministic build report.")
    report.add_argument("--output", type=Path)
    context = subparsers.add_parser(
        "context", help="Compile a G2 relationship- and budget-aware context package."
    )
    context.add_argument("--terms", nargs="*", default=[])
    context.add_argument("--ids", nargs="*", default=[])
    context.add_argument("--entity-ids", nargs="*", default=[])
    context.add_argument("--budget", type=int, default=None)
    context.add_argument("--relation-types", nargs="*", default=None)
    context.add_argument(
        "--mode",
        choices=("grounding", "research", "audit", "exhaustive"),
        default="grounding",
    )
    return parser


def _print(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def main(argv: Sequence[str] | None = None) -> int:
    # Force UTF-8 stdout/stderr so non-ASCII content (en-dashes, quoted
    # transcriptions) survives a Windows console/pipe whose default code page is
    # cp1252. The NDJSON export path already writes explicit UTF-8; this makes
    # the human/AI-facing command output equally deterministic.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except (AttributeError, ValueError):
            pass
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
        elif args.command == "export-website":
            path = export_website(config, args.out)
            _print({"website_export": str(path)})
        elif args.command == "item":
            item = get_item(config, args.item_id)
            if item is None:
                print(f"Item not found: {args.item_id}", file=sys.stderr)
                return 1
            _print(item)
        elif args.command == "source":
            source = get_source(config, args.source_id)
            if source is None:
                print(f"Source not found: {args.source_id}", file=sys.stderr)
                return 1
            _print(source)
        elif args.command == "unit":
            unit = get_unit(config, args.unit_id)
            if unit is None:
                print(f"Research unit not found: {args.unit_id}", file=sys.stderr)
                return 1
            _print(unit)
        elif args.command == "impact":
            impact = get_impact(config, args.item_id)
            if impact is None:
                print(f"Item not found: {args.item_id}", file=sys.stderr)
                return 1
            _print(impact)
        elif args.command == "search":
            _print(search_graph(config, args.terms, limit=args.limit))
        elif args.command == "reindex":
            _print({"indexes": rebuild_database_indexes(config)})
        elif args.command == "hash-sources":
            _print(
                capture_source_hashes(
                    config,
                    source_ids=args.source_id,
                    replace=args.accept_current,
                    changed_by=args.changed_by,
                )
            )
        elif args.command == "report":
            _print({"report": str(write_build_report(config, args.output))})
        elif args.command == "context":
            _print(
                compile_context(
                    config,
                    terms=args.terms,
                    ids=args.ids,
                    entity_ids=args.entity_ids,
                    budget=args.budget,
                    relation_types=args.relation_types,
                    mode=args.mode,
                )
            )
        else:
            raise AssertionError(args.command)
    except Exception as exc:
        print(f"g13_graph: {exc}", file=sys.stderr)
        return 2
    return 0
