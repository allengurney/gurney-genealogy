#!/usr/bin/env python3
"""Mechanized coverage checker for the G13 research refactor (Plan 02 §7.4).

Losslessness of the G13 companion/dump refactor is enforced by a script, not by
manual CSV vigilance. This tool reads the three coverage ledgers plus the frozen
inventory (Plan 02 §7.1–§7.3, §8 step 1) and reports:

- any legacy heading/block or dump finding with **no disposition** (backlog);
- coverage as a percentage per ledger, with the gap list;
- any staged unit that cites a ``sourceId`` absent from the source-and-citation
  map, and any ``sourceId`` not present in ``data/sources.json``;
- frozen-inventory integrity: every frozen input still hashes to its recorded
  SHA-256 and is enumerated into at least one ledger.

It is deterministic and read-only. It never modifies a ledger or any
research/data file. It exits nonzero when it finds any un-dispositioned item,
any untracked citation gap, or any inventory-integrity failure, so it can gate
cutover (Plan 02 §14–§15).

Usage (from the repo root, in the repo .venv)::

    python tools/g13_coverage_check.py            # compact text report
    python tools/g13_coverage_check.py --json     # machine-readable report

Exit code is 0 only when the staged package is losslessly tracked.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Sequence


# --- Frozen spec constants (Plan 02) -----------------------------------------

# §7.1 legacy-companion disposition vocabulary.
LEGACY_DISPOSITIONS = {
    "moved",
    "synthesized",
    "retained_in_hub",
    "external-canonical",
    "superseded-but-preserved",
    "duplicate",
    "needs-decision",
}

# §12 operational disposition vocabulary for dump findings. Used only for a soft
# "unrecognized value" warning — an *empty* disposition is the gating backlog
# signal, per the ledger README.
DUMP_DISPOSITIONS = {
    "assimilated",
    "updates-lead",
    "closes-lead",
    "creates-lead",
    "superseded",
    "source-artifact",
    "speculation",
    "routed",
}

# Staged units mark each citation with a footnote trailer `Source ID: \`x\``.
SOURCE_ID_RE = re.compile(r"Source ID:\s*`([^`]+)`")

# A frozen-inventory table row carries a whole-file SHA-256 (64 lowercase hex).
SHA256_RE = re.compile(r"\b([0-9a-f]{64})\b")
BACKTICK_RE = re.compile(r"`([^`]+)`")

STAGING_REL = Path("research/people/_staging/g13-john-gurney")
DEFAULT_COVERAGE_REL = STAGING_REL / "coverage"
DEFAULT_SOURCES_REL = Path("data/sources.json")


# --- Report structures -------------------------------------------------------


@dataclass
class LedgerCoverage:
    """Disposition coverage for one row-per-item ledger."""

    name: str
    total: int
    dispositioned: int
    gaps: list[str] = field(default_factory=list)  # human labels of backlog rows
    unknown_dispositions: list[str] = field(default_factory=list)  # (row, value)

    @property
    def coverage_pct(self) -> float:
        if self.total == 0:
            return 100.0
        return round(100.0 * self.dispositioned / self.total, 1)

    @property
    def backlog(self) -> int:
        return self.total - self.dispositioned


@dataclass
class CoverageReport:
    legacy: LedgerCoverage
    dump: LedgerCoverage
    # §7.3 citation checks.
    unit_citation_gaps: list[dict[str, str]] = field(default_factory=list)
    unregistered_sources: list[dict[str, str]] = field(default_factory=list)
    registration_mismatches: list[dict[str, str]] = field(default_factory=list)
    map_sources_not_cited: list[dict[str, str]] = field(default_factory=list)
    # §8 step 1 frozen-inventory integrity.
    inventory_inputs: int = 0
    hash_mismatches: list[dict[str, str]] = field(default_factory=list)
    missing_inputs: list[str] = field(default_factory=list)
    inputs_without_rows: list[str] = field(default_factory=list)
    # Non-fatal notes.
    warnings: list[str] = field(default_factory=list)

    @property
    def combined_total(self) -> int:
        return self.legacy.total + self.dump.total

    @property
    def combined_dispositioned(self) -> int:
        return self.legacy.dispositioned + self.dump.dispositioned

    @property
    def combined_pct(self) -> float:
        if self.combined_total == 0:
            return 100.0
        return round(100.0 * self.combined_dispositioned / self.combined_total, 1)

    @property
    def gating_problem_count(self) -> int:
        return (
            self.legacy.backlog
            + self.dump.backlog
            + len(self.unit_citation_gaps)
            + len(self.unregistered_sources)
            + len(self.hash_mismatches)
            + len(self.missing_inputs)
            + len(self.inputs_without_rows)
        )

    @property
    def ok(self) -> bool:
        return self.gating_problem_count == 0


# --- Loading helpers ---------------------------------------------------------


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _cell(row: dict[str, str], key: str) -> str:
    return (row.get(key) or "").strip()


def parse_frozen_inventory(readme_path: Path) -> list[dict[str, str]]:
    """Extract the frozen-inventory table (path + whole-file SHA-256) from the
    ledger README (Plan 02 §8 step 1). A row is any markdown table line that
    carries a 64-hex SHA-256; the first backtick-wrapped file path in the row is
    the input path."""

    inputs: list[dict[str, str]] = []
    for line in readme_path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        sha_match = SHA256_RE.search(line)
        if not sha_match:
            continue
        path = ""
        for token in BACKTICK_RE.findall(line):
            token = token.strip()
            if "/" in token and token != sha_match.group(1):
                path = token
                break
        if not path:
            continue
        inputs.append({"path": path, "sha256": sha_match.group(1)})
    return inputs


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _sources_index(sources_path: Path) -> set[str]:
    data = json.loads(sources_path.read_text(encoding="utf-8-sig"))
    return set(data.get("sources", {}).keys())


def _cited_source_ids(text: str) -> set[str]:
    return {m.strip() for m in SOURCE_ID_RE.findall(text)}


# --- Core checks -------------------------------------------------------------


def _check_disposition_ledger(
    rows: list[dict[str, str]],
    *,
    name: str,
    label_fn,
    allowed: set[str],
) -> LedgerCoverage:
    cov = LedgerCoverage(name=name, total=len(rows), dispositioned=0)
    for row in rows:
        disposition = _cell(row, "disposition")
        label = label_fn(row)
        if not disposition:
            cov.gaps.append(label)
            continue
        cov.dispositioned += 1
        if disposition not in allowed:
            cov.unknown_dispositions.append(f"{label} -> {disposition!r}")
    return cov


def run_check(
    *,
    coverage_dir: Path,
    sources_path: Path,
    repo_root: Path,
) -> CoverageReport:
    """Run every deterministic check and return a structured report."""

    staging_dir = coverage_dir.parent
    legacy_rows = _read_csv(coverage_dir / "legacy-companion-map.csv")
    dump_rows = _read_csv(coverage_dir / "dump-findings-map.csv")
    citation_rows = _read_csv(coverage_dir / "source-and-citation-map.csv")

    legacy_cov = _check_disposition_ledger(
        legacy_rows,
        name="Legacy companion map",
        label_fn=lambda r: f"{_cell(r, 'legacy_heading')} (l.{_cell(r, 'line_start_at_inventory')})",
        allowed=LEGACY_DISPOSITIONS,
    )
    dump_cov = _check_disposition_ledger(
        dump_rows,
        name="Dump findings map",
        label_fn=lambda r: f"{_cell(r, 'finding_id')} :: {_cell(r, 'finding_heading')}"
        f"  [{Path(_cell(r, 'dump_file')).name}]",
        allowed=DUMP_DISPOSITIONS,
    )

    report = CoverageReport(legacy=legacy_cov, dump=dump_cov)

    # --- §7.3 citation map + sources.json registration -----------------------
    registered = _sources_index(sources_path)

    # (topic_id, source_id) pairs and per-source registration claims recorded in
    # the citation ledger.
    map_pairs: set[tuple[str, str]] = set()
    map_sources: set[str] = set()
    for row in citation_rows:
        topic = _cell(row, "topic_id")
        source = _cell(row, "source_id")
        if not source:
            continue
        map_pairs.add((topic, source))
        map_sources.add(source)
        claim = _cell(row, "registered_in_sources_json").lower()
        actually = source in registered
        if claim in {"yes", "no"} and (claim == "yes") != actually:
            report.registration_mismatches.append(
                {
                    "topic_id": topic,
                    "source_id": source,
                    "ledger_says": claim,
                    "actually_registered": str(actually).lower(),
                }
            )

    # (b) any sourceId in the citation map not present in data/sources.json.
    for source in sorted(map_sources):
        if source not in registered:
            report.unregistered_sources.append(
                {"source_id": source, "seen_in": "source-and-citation-map"}
            )

    # --- Staged-unit citations vs the map (§7.3) -----------------------------
    manifest_path = staging_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    cited_pairs: set[tuple[str, str]] = set()
    for topic in manifest.get("topics", []):
        topic_id = topic.get("topicId", "")
        rel = topic.get("path", "")
        unit_path = (repo_root / rel).resolve()
        if not unit_path.is_file():
            report.warnings.append(f"manifest topic path missing: {rel}")
            continue
        text = unit_path.read_text(encoding="utf-8")
        for source in sorted(_cited_source_ids(text)):
            cited_pairs.add((topic_id, source))
            # (a) unit cites a sourceId with no row in the citation map.
            if (topic_id, source) not in map_pairs:
                report.unit_citation_gaps.append(
                    {"topic_id": topic_id, "source_id": source, "path": rel}
                )
            # (b) unit cites a sourceId not registered in data/sources.json.
            if source not in registered:
                report.unregistered_sources.append(
                    {"source_id": source, "seen_in": f"unit:{topic_id}"}
                )

    # Non-gating: citation-map rows for a staged unit that the unit never cites.
    # Only meaningful for units whose prose is present in the manifest/staged set.
    staged_topic_ids = {t.get("topicId", "") for t in manifest.get("topics", [])}
    for topic_id, source in sorted(map_pairs):
        if topic_id not in staged_topic_ids:
            continue
        if (topic_id, source) not in cited_pairs:
            report.map_sources_not_cited.append(
                {"topic_id": topic_id, "source_id": source}
            )

    # --- §8 step 1 frozen-inventory integrity --------------------------------
    inventory = parse_frozen_inventory(coverage_dir / "README.md")
    report.inventory_inputs = len(inventory)
    legacy_paths = {_cell(r, "legacy_path") for r in legacy_rows}
    dump_files = {_cell(r, "dump_file") for r in dump_rows}
    for item in inventory:
        rel = item["path"]
        target = (repo_root / rel).resolve()
        if not target.is_file():
            report.missing_inputs.append(rel)
        else:
            actual = _sha256_file(target)
            if actual != item["sha256"]:
                report.hash_mismatches.append(
                    {"path": rel, "frozen": item["sha256"], "actual": actual}
                )
        if rel not in legacy_paths and rel not in dump_files:
            report.inputs_without_rows.append(rel)

    return report


# --- Rendering ---------------------------------------------------------------


def _render_ledger_block(cov: LedgerCoverage, *, show_gaps: bool) -> list[str]:
    status = "ok" if cov.backlog == 0 else "FAIL"
    lines = [
        f"[{status}] {cov.name}: {cov.dispositioned}/{cov.total} dispositioned "
        f"({cov.coverage_pct}%), {cov.backlog} backlog"
    ]
    if show_gaps and cov.gaps:
        lines.append(f"       un-dispositioned ({len(cov.gaps)}):")
        lines.extend(f"         - {g}" for g in cov.gaps)
    if cov.unknown_dispositions:
        lines.append(
            f"       [warn] unrecognized disposition values ({len(cov.unknown_dispositions)}):"
        )
        lines.extend(f"         - {u}" for u in cov.unknown_dispositions)
    return lines


def render_text(report: CoverageReport, *, show_gaps: bool = True) -> str:
    out: list[str] = []
    out.append("G13 refactor coverage check (Plan 02 §7.4)")
    out.append("=" * 44)
    out.extend(_render_ledger_block(report.legacy, show_gaps=show_gaps))
    out.append("")
    out.extend(_render_ledger_block(report.dump, show_gaps=show_gaps))
    out.append("")
    out.append(
        f"Combined disposition coverage: "
        f"{report.combined_dispositioned}/{report.combined_total} "
        f"({report.combined_pct}%)"
    )
    out.append("")

    # Citation checks.
    cite_status = "ok" if not report.unit_citation_gaps else "FAIL"
    out.append(
        f"[{cite_status}] Staged-unit citations tracked in source-and-citation map: "
        f"{len(report.unit_citation_gaps)} gap(s)"
    )
    for g in report.unit_citation_gaps:
        out.append(f"         - {g['topic_id']} cites `{g['source_id']}` (not in map) [{g['path']}]")

    reg_status = "ok" if not report.unregistered_sources else "FAIL"
    out.append(
        f"[{reg_status}] Cited sourceIds registered in data/sources.json: "
        f"{len(report.unregistered_sources)} gap(s)"
    )
    for g in report.unregistered_sources:
        out.append(f"         - `{g['source_id']}` unregistered (seen in {g['seen_in']})")
    out.append("")

    # Inventory integrity.
    inv_bad = len(report.hash_mismatches) + len(report.missing_inputs) + len(report.inputs_without_rows)
    inv_status = "ok" if inv_bad == 0 else "FAIL"
    out.append(
        f"[{inv_status}] Frozen inventory integrity: {report.inventory_inputs} input(s), "
        f"{len(report.hash_mismatches)} hash mismatch, "
        f"{len(report.missing_inputs)} missing, "
        f"{len(report.inputs_without_rows)} un-enumerated"
    )
    for m in report.hash_mismatches:
        out.append(f"         - hash drift: {m['path']}")
        out.append(f"             frozen {m['frozen']}")
        out.append(f"             actual {m['actual']}")
    for p in report.missing_inputs:
        out.append(f"         - missing input file: {p}")
    for p in report.inputs_without_rows:
        out.append(f"         - frozen input has no ledger rows: {p}")
    out.append("")

    # Non-fatal notes.
    if report.registration_mismatches:
        out.append(
            f"[warn] registration column disagrees with data/sources.json "
            f"({len(report.registration_mismatches)}):"
        )
        for m in report.registration_mismatches:
            out.append(
                f"         - {m['topic_id']}/`{m['source_id']}`: ledger says "
                f"{m['ledger_says']}, actually_registered={m['actually_registered']}"
            )
    if report.map_sources_not_cited:
        out.append(
            f"[warn] citation-map rows not cited by their staged unit "
            f"({len(report.map_sources_not_cited)}):"
        )
        for m in report.map_sources_not_cited:
            out.append(f"         - {m['topic_id']}/`{m['source_id']}`")
    for w in report.warnings:
        out.append(f"[warn] {w}")
    if report.registration_mismatches or report.map_sources_not_cited or report.warnings:
        out.append("")

    verdict = "PASS" if report.ok else "FAIL"
    out.append(
        f"RESULT: {verdict} — {report.gating_problem_count} gating problem(s) "
        f"({report.legacy.backlog + report.dump.backlog} un-dispositioned, "
        f"{len(report.unit_citation_gaps) + len(report.unregistered_sources)} citation gap(s), "
        f"{inv_bad} inventory)"
    )
    return "\n".join(out)


def report_to_dict(report: CoverageReport) -> dict[str, Any]:
    return {
        "ok": report.ok,
        "gating_problem_count": report.gating_problem_count,
        "ledgers": {
            "legacy": {
                "total": report.legacy.total,
                "dispositioned": report.legacy.dispositioned,
                "backlog": report.legacy.backlog,
                "coverage_pct": report.legacy.coverage_pct,
                "gaps": report.legacy.gaps,
                "unknown_dispositions": report.legacy.unknown_dispositions,
            },
            "dump": {
                "total": report.dump.total,
                "dispositioned": report.dump.dispositioned,
                "backlog": report.dump.backlog,
                "coverage_pct": report.dump.coverage_pct,
                "gaps": report.dump.gaps,
                "unknown_dispositions": report.dump.unknown_dispositions,
            },
            "combined": {
                "total": report.combined_total,
                "dispositioned": report.combined_dispositioned,
                "coverage_pct": report.combined_pct,
            },
        },
        "unit_citation_gaps": report.unit_citation_gaps,
        "unregistered_sources": report.unregistered_sources,
        "inventory": {
            "inputs": report.inventory_inputs,
            "hash_mismatches": report.hash_mismatches,
            "missing_inputs": report.missing_inputs,
            "inputs_without_rows": report.inputs_without_rows,
        },
        "warnings": {
            "registration_mismatches": report.registration_mismatches,
            "map_sources_not_cited": report.map_sources_not_cited,
            "other": report.warnings,
        },
    }


# --- CLI ---------------------------------------------------------------------


def _configure_stdio() -> None:
    """Force UTF-8 stdout/stderr so the report prints on Windows code pages."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


def build_parser() -> argparse.ArgumentParser:
    default_repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Mechanized coverage checker for the G13 refactor (Plan 02 §7.4).",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=default_repo_root,
        help="Repository root used to resolve inventory and manifest paths.",
    )
    parser.add_argument(
        "--coverage-dir",
        type=Path,
        default=None,
        help="Directory holding the three ledgers and the inventory README "
        "(default: <repo-root>/research/people/_staging/g13-john-gurney/coverage).",
    )
    parser.add_argument(
        "--sources",
        type=Path,
        default=None,
        help="Path to data/sources.json (default: <repo-root>/data/sources.json).",
    )
    parser.add_argument("--json", action="store_true", help="Emit a JSON report.")
    parser.add_argument(
        "--no-gaps",
        action="store_true",
        help="Suppress the per-row backlog lists in the text report.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    _configure_stdio()
    args = build_parser().parse_args(argv)
    repo_root: Path = args.repo_root.resolve()
    coverage_dir: Path = (
        args.coverage_dir.resolve()
        if args.coverage_dir is not None
        else (repo_root / DEFAULT_COVERAGE_REL)
    )
    sources_path: Path = (
        args.sources.resolve()
        if args.sources is not None
        else (repo_root / DEFAULT_SOURCES_REL)
    )

    report = run_check(
        coverage_dir=coverage_dir,
        sources_path=sources_path,
        repo_root=repo_root,
    )

    if args.json:
        print(json.dumps(report_to_dict(report), indent=2, ensure_ascii=False))
    else:
        print(render_text(report, show_gaps=not args.no_gaps))

    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
