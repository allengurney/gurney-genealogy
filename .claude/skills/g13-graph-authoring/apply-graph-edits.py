#!/usr/bin/env python
"""Apply a sequence of g13-graph editor ops (edits to already-committed items).

`author-batch` only *creates* (a whole unit + items + relations + markers in one
transaction). Revising existing items — new source links, statement/date/scope
fixes, marker maintenance, publications — goes through the editor's
`commit_change` ops. This runner applies an ordered list of those ops against the
live DB (or `GURNEY_G13_GRAPH_DB`), one transaction per op, printing the revision
and audit summary for each.

Usage (from the repo root, repo venv):
    .\\.venv\\Scripts\\python.exe .claude/skills/g13-graph-authoring/apply-graph-edits.py <ops.json> [--changed-by NAME]

Ops file shape — a JSON list of op objects, OR an object with an "ops" list and an
optional top-level "changed_by":
    [
      {"op": "add_source_link", "params": {"item_id": "G13-RI-000062",
        "source_id": "braintree-records-1640-1793-1886", "role": "supports",
        "locator": "p. 717", "verification_level": "printed-transcription",
        "alignment_note": "..."}},
      {"op": "update_item", "params": {"item_id": "G13-RI-000063",
        "changes": {"statement": "...", "assessment_confidence_label": "moderate"}}},
      {"op": "update_source_link", "params": {"item_source_id": 74, "alignment_note": "..."}},
      {"op": "set_negative_scope", "params": {"item_id": "G13-RI-000064",
        "provider": "...", "collection_name": "...", "query_description": "...",
        "date_start": "1620", "date_end": "1634", "results_reviewed": 33,
        "coverage_confirmed": 0, "limitations": ["...", "..."]}}
    ]

IMPORTANT — this is NOT a single transaction. Each op commits independently and
advances the revision; if op N fails validation, ops 1..N-1 are already committed.
There is no built-in dry-run (unlike author-batch), so:
  * look up `item_source_id` / current values first (`g13_graph.py item <id>` or a
    direct read) — a wrong id fails mid-run;
  * order ops so an earlier op can't leave a later one un-appliable;
  * `set_negative_scope` takes `limitations` as a real JSON list here (the runner
    encodes it); this differs from author-batch, where limitations_json must be a
    pre-encoded string;
  * after the run, always `export --snapshot`, `validate` (expect 0/0), `status`
    (tiers aligned), and re-run `g13_coverage_check.py`.
Editing existing items is the ONLY path for this — do not try to "re-create" an
item with author-batch (it collides on the existing id and refuses).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Put the repo's tools/ on the path so `g13_graph` imports regardless of cwd.
_TOOLS = Path(__file__).resolve().parents[3] / "tools"
sys.path.insert(0, str(_TOOLS))

from g13_graph.config import load_config  # noqa: E402
from g13_graph.editor import commit_change  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ops_file", help="Path to the ops JSON (list or {ops, changed_by}).")
    parser.add_argument(
        "--changed-by",
        default=None,
        help="Audit author for item_revisions (default: from the file, else 'claude-graph-edit').",
    )
    args = parser.parse_args(argv)

    payload = json.loads(Path(args.ops_file).read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        ops = payload.get("ops") or []
        file_changed_by = payload.get("changed_by")
    else:
        ops = payload
        file_changed_by = None
    changed_by = args.changed_by or file_changed_by or "claude-graph-edit"

    if not ops:
        print("No ops found in file.", file=sys.stderr)
        return 2

    config = load_config()
    for i, change in enumerate(ops, 1):
        op = change.get("op", "<missing op>")
        try:
            res = commit_change(config, change, changed_by=changed_by)
        except Exception as exc:  # ValidationBlocked, ChangeError, sqlite errors
            print(
                f"[{i}/{len(ops)}] {op} FAILED: {type(exc).__name__}: {exc}",
                file=sys.stderr,
            )
            print(
                f"Stopped after {i - 1} successful op(s); those are already committed.",
                file=sys.stderr,
            )
            return 1
        print(
            f"[{i}/{len(ops)}] {op} -> rev {res.get('database_revision')} "
            f"stale={res.get('stale')} :: {res.get('summary', '')}"
        )
    print(f"DONE — {len(ops)} op(s) applied by '{changed_by}'.")
    print("Next: export --snapshot; validate (0/0); status (tiers aligned); g13_coverage_check.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
