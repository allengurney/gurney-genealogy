#!/usr/bin/env python3
"""Lint data/sources.json notes fields for evidence bloat.

Registry notes are brief catalogue annotations (what the source is, why it is
relevant, what kinds of information it carries). Evidence, transcriptions,
negative-search results, and findings live in the research plane (topic files,
companions, fact sheets) or in sources/corpus_supplement/ - never in the
registry. This lint flags notes above the threshold unless the sourceId is in
the frozen allowlist of pre-existing long entries (grandfathered 2026-07; do
not add new ids without explicit user approval).

Usage:
  .\.venv\Scripts\python.exe tools\lint_source_notes.py                 # check; exit 1 on flags
  .\.venv\Scripts\python.exe tools\lint_source_notes.py --write-allowlist
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCES = REPO / "data" / "sources.json"
ALLOWLIST = REPO / "tools" / "lint_source_notes_allowlist.txt"
DEFAULT_THRESHOLD = 600


def notes_len(entry):
    return len(str(entry.get("notes", "") or ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    ap.add_argument(
        "--write-allowlist",
        action="store_true",
        help="Freeze every id currently over the threshold into the allowlist.",
    )
    args = ap.parse_args()

    sources = json.loads(SOURCES.read_text(encoding="utf-8"))["sources"]
    over = sorted(
        [(sid, notes_len(s)) for sid, s in sources.items() if notes_len(s) > args.threshold],
        key=lambda x: -x[1],
    )

    if args.write_allowlist:
        lines = [
            "# Grandfathered pre-existing long-notes sources (frozen 2026-07).",
            "# Do not add new ids without explicit user approval.",
            "",
        ]
        lines += [sid for sid, _ in over]
        ALLOWLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"allowlist frozen: {len(over)} ids > {args.threshold} chars")
        return 0

    allow = set()
    if ALLOWLIST.exists():
        allow = {
            ln.strip()
            for ln in ALLOWLIST.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")
        }

    flagged = [(sid, n) for sid, n in over if sid not in allow]
    for sid, n in flagged:
        print(f"FLAG {sid}: notes {n} chars > {args.threshold}")
    print(
        f"RESULT: {'FAIL' if flagged else 'PASS'} - {len(flagged)} flagged, "
        f"{len(over) - len(flagged)} grandfathered"
    )
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
