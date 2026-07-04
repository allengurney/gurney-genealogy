#!/usr/bin/env python
"""Entry point for the G13 graph-editing artifact (Phase G4).

Launches a loopback-only local backend + browser UI over the canonical SQLite
context graph. Development must run against a staging copy via
``GURNEY_G13_GRAPH_DB`` (or ``--db``); opening the live canonical database
requires the explicit ``--allow-live`` flag.

    .\\.venv\\Scripts\\python.exe tools\\g13_graph_editor.py --db <staging.sqlite> \\
        --export-dir <staging-exports>
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.g13_graph_editor.server import run  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="Loopback bind host.")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--db", help="Override database path (staging copy).")
    parser.add_argument("--export-dir", help="Override recovery export directory.")
    parser.add_argument("--sources", help="Override sources.json path.")
    parser.add_argument(
        "--allow-live",
        action="store_true",
        help="Permit opening the live canonical database (off by default).",
    )
    args = parser.parse_args(argv)
    run(
        host=args.host,
        port=args.port,
        db_path=args.db,
        export_dir=args.export_dir,
        sources_path=args.sources,
        allow_live=args.allow_live,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
