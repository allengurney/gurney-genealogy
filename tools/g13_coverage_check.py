#!/usr/bin/env python3
"""Mechanized coverage checker for the G13 research refactor (Plan 02 §7.4 +
Plan 2b §8).

Losslessness of the G13 companion/dump refactor is enforced by a script, not by
manual CSV vigilance. This tool reads the four coverage ledgers plus the frozen
inventory (Plan 02 §7.1–§7.3, §8 step 1; Plan 2b §6) and reports:

- any legacy heading/block, dump finding, or supplemental-surface block with
  **no disposition** (backlog);
- coverage as a percentage per ledger, with the gap list;
- any staged unit that cites a ``sourceId`` absent from the source-and-citation
  map, and any ``sourceId`` not present in ``data/sources.json``;
- frozen-inventory integrity: every frozen input still hashes to its recorded
  SHA-256 and is enumerated into at least one ledger;
- Plan 2b §8.2 input source-set integrity: a dispositioned row's ``source_ids``
  must cover every source its frozen block actually cites (markdown backtick or
  HTML ``<code>`` form, footnote definitions resolved);
- Plan 2b §8.3 source-journey integrity: a journey-checked row's sources must
  be linked to items in the destination unit in the graph export, or carry a
  preserved disposition;
- Plan 2b §8.4 topic prose <-> graph source parity per staged unit;
- Plan 2b §8.5 publication-mapping projection for fact-sheet/case-file rows;
- Plan 2b §8.6 friction requiring a decision.

Graph truth is read from the newest tracked snapshot NDJSON (Plan 2b §8.0);
override with ``--graph-export``.

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
# Publication surfaces (fact sheet, case file) use the HTML form
# `Source ID: <code>x</code>` instead (Plan 2b §8.2); bare <code> tags also
# carry non-source content, so both forms anchor on the `Source ID:` label.
# Multi-source footnotes across every surface write the label once, plural,
# with several ids after it (`Source IDs: \`a\`; \`b\``); a few topic footnotes
# use a lowercase label with no colon (`source ID \`x\``). The extractor
# therefore matches a label run — `[Ss]ource ID(s)` + optional colon — and
# consumes every backtick/<code> token that follows it (Thread 2 fix,
# 2026-07-04: the original singular-label, single-token regexes silently
# missed every plural-form citation).
SOURCE_ID_RUN_RE = re.compile(
    r"[Ss]ource\s+IDs?\s*:?\s*"
    r"((?:(?:`[^`]+`|<code>\s*[^<]+?\s*</code>)\s*(?:[;,]|\band\b)?\s*)+)"
)
SOURCE_ID_TOKEN_RE = re.compile(r"`([^`]+)`|<code>\s*([^<]+?)\s*</code>")

# A frozen-inventory table row carries a whole-file SHA-256 (64 lowercase hex).
SHA256_RE = re.compile(r"\b([0-9a-f]{64})\b")
BACKTICK_RE = re.compile(r"`([^`]+)`")

# Footnote references/definitions — Markdown ([^ref] / [^ref]: ...) and the
# HTML pattern the case file uses (<a href="#n2"> refs, <li id="n2"> defs).
MD_FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")
MD_FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
HTML_FOOTNOTE_REF_RE = re.compile(r"href=\"#([A-Za-z0-9_-]+)\"")
HTML_ID_RE = re.compile(r"\bid=\"([A-Za-z0-9_-]+)\"")

STAGING_REL = Path("research/people/_staging/g13-john-gurney")
DEFAULT_COVERAGE_REL = STAGING_REL / "coverage"
DEFAULT_SOURCES_REL = Path("data/sources.json")
SNAPSHOT_DIR_REL = Path("data/context-graphs/g13/exports/snapshots")
SNAPSHOT_REVISION_RE = re.compile(r"r(\d+)\.ndjson$")


def _norm_disp(value: str) -> str:
    """Normalize a disposition/vocab token: the historical ledgers mix hyphen
    and underscore separators (Plan 2b §6.2)."""
    return value.strip().lower().replace("-", "_")


def _split_multi(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


# Plan 2b §6.2 supplemental-surface vocabulary (normalized form).
SUPPLEMENTAL_DISPOSITIONS = {
    "incorporated",
    "summarized",
    "publication_only",
    "external_canonical",
    "superseded_but_preserved",
    "duplicate_but_preserved",
    "routed_elsewhere",
    "needs_decision",
}

SUPPLEMENTAL_FRICTION = {
    "claim_conflict",
    "confidence_mismatch",
    "source_alignment_unclear",
    "source_id_missing",
    "source_id_collision",
    "same_record_multiple_representations",
    "topic_boundary",
    "publication_wording",
    "graph_model_gap",
    "needs_source_pull",
}

# Journey semantics (Plan 2b §8.3), keyed by normalized disposition. A
# journey-checked row's sources must reach the destination unit in the graph;
# a preserved disposition is itself the reviewed escape hatch.
JOURNEY_CHECKED = {
    "legacy": {"moved", "synthesized"},
    "dump": {"assimilated"},
    "supplemental": {"incorporated", "summarized"},
}
PRESERVED_DISPOSITIONS = {
    "legacy": {
        "retained_in_hub",
        "external_canonical",
        "superseded_but_preserved",
        "duplicate",
    },
    "dump": {
        "updates_lead",
        "closes_lead",
        "creates_lead",
        "superseded",
        "source_artifact",
        "speculation",
        "routed",
    },
    "supplemental": {
        "publication_only",
        "external_canonical",
        "superseded_but_preserved",
        "duplicate_but_preserved",
        "routed_elsewhere",
    },
}

# Citation-map `cited_role` tokens that exempt a (unit, source) pair from
# topic↔graph parity (Plan 2b §8.4): a reviewed, deliberate cross-unit or
# context-only citation that intentionally has no item link in this unit.
PARITY_EXEMPT_ROLES = {"context_only", "cross_unit"}


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
class GraphView:
    """The slice of the graph export the checker needs (Plan 2b §8.0)."""

    path: str = ""
    revision: int | None = None
    units: set[str] = field(default_factory=set)
    item_ids: set[str] = field(default_factory=set)
    unit_sources: dict[str, set[str]] = field(default_factory=dict)


@dataclass
class CoverageReport:
    legacy: LedgerCoverage
    dump: LedgerCoverage
    supplemental: LedgerCoverage
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
    # Plan 2b §8.2 input source-set integrity (gating: anchored rows only).
    input_source_set_gaps: list[dict[str, str]] = field(default_factory=list)
    extraction_notes: list[dict[str, str]] = field(default_factory=list)
    # Plan 2b §8.3 source-journey integrity.
    source_journey_gaps: list[dict[str, str]] = field(default_factory=list)
    journey_deferred: list[dict[str, str]] = field(default_factory=list)
    # Plan 2b §8.4 topic prose ↔ graph parity.
    topic_graph_source_gaps: list[dict[str, str]] = field(default_factory=list)
    # Plan 2b §8.5 publication alignment (mechanical projection).
    publication_mapping_gaps: list[dict[str, str]] = field(default_factory=list)
    # Plan 2b §8.6/§11 friction requiring a decision.
    friction_needs_decision: list[dict[str, str]] = field(default_factory=list)
    friction_open: list[dict[str, str]] = field(default_factory=list)
    # Plan 2b §8.0 graph export.
    graph_export_path: str = ""
    graph_revision: int | None = None
    graph_export_missing: bool = False
    # Non-fatal notes.
    warnings: list[str] = field(default_factory=list)

    @property
    def combined_total(self) -> int:
        return self.legacy.total + self.dump.total + self.supplemental.total

    @property
    def combined_dispositioned(self) -> int:
        return (
            self.legacy.dispositioned
            + self.dump.dispositioned
            + self.supplemental.dispositioned
        )

    @property
    def combined_pct(self) -> float:
        if self.combined_total == 0:
            return 100.0
        return round(100.0 * self.combined_dispositioned / self.combined_total, 1)

    @property
    def source_lossless_counts(self) -> dict[str, int]:
        """Plan 2b §8.6 category counts. SOURCE-LOSSLESS requires all zero."""
        return {
            "input_inventory_gaps": (
                len(self.hash_mismatches)
                + len(self.missing_inputs)
                + len(self.inputs_without_rows)
            ),
            "input_source_set_gaps": len(self.input_source_set_gaps),
            "source_journey_gaps": len(self.source_journey_gaps),
            "topic_graph_source_gaps": len(self.topic_graph_source_gaps),
            "publication_mapping_gaps": len(self.publication_mapping_gaps),
            "friction_needs_decision": len(self.friction_needs_decision),
            "graph_export_missing": 1 if self.graph_export_missing else 0,
        }

    @property
    def source_lossless(self) -> bool:
        return (
            all(v == 0 for v in self.source_lossless_counts.values())
            and self.legacy.backlog == 0
            and self.dump.backlog == 0
            and self.supplemental.backlog == 0
        )

    @property
    def gating_problem_count(self) -> int:
        return (
            self.legacy.backlog
            + self.dump.backlog
            + self.supplemental.backlog
            + len(self.unit_citation_gaps)
            + len(self.unregistered_sources)
            + len(self.hash_mismatches)
            + len(self.missing_inputs)
            + len(self.inputs_without_rows)
            + len(self.input_source_set_gaps)
            + len(self.source_journey_gaps)
            + len(self.topic_graph_source_gaps)
            + len(self.publication_mapping_gaps)
            + len(self.friction_needs_decision)
            + (1 if self.graph_export_missing else 0)
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
    ids: set[str] = set()
    for run in SOURCE_ID_RUN_RE.finditer(text):
        for backtick, code in SOURCE_ID_TOKEN_RE.findall(run.group(1)):
            token = (backtick or code).strip()
            if token:
                ids.add(token)
    return ids


# --- Plan 2b §8.2: block extraction with footnote resolution ------------------


def _md_footnote_defs(lines: list[str]) -> dict[str, str]:
    """Map markdown footnote label -> definition text (def line + indented
    continuation lines)."""
    defs: dict[str, str] = {}
    label = None
    buf: list[str] = []
    for line in lines:
        m = re.match(r"^\[\^([^\]]+)\]:", line)
        if m:
            if label is not None:
                defs[label] = "\n".join(buf)
            label = m.group(1)
            buf = [line]
        elif label is not None and (line.startswith(("    ", "\t")) or not line.strip()):
            buf.append(line)
        elif label is not None:
            defs[label] = "\n".join(buf)
            label = None
            buf = []
    if label is not None:
        defs[label] = "\n".join(buf)
    return defs


def _html_anchor_defs(lines: list[str], anchor_ids: set[str]) -> dict[str, str]:
    """Map HTML element id -> that element's text (its line plus following
    lines until the next id= line). Good enough for <li id="n2">…</li> footnote
    lists."""
    defs: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in lines:
        ids_here = [i for i in HTML_ID_RE.findall(line) if i in anchor_ids]
        if ids_here:
            if current is not None:
                defs[current] = "\n".join(buf)
            current = ids_here[0]
            buf = [line]
        elif current is not None:
            if HTML_ID_RE.search(line):
                defs[current] = "\n".join(buf)
                current = None
                buf = []
            else:
                buf.append(line)
    if current is not None:
        defs[current] = "\n".join(buf)
    return defs


def _strip_md_footnote_defs(block_text: str) -> str:
    """Remove markdown footnote-definition lines (def line + indented/blank
    continuations) from a block's text. The companion and dumps colocate
    shared definition blocks inside some spans; scanning those lines inline
    would credit the block with every neighboring block's citations (Thread 2
    fix, 2026-07-04). Referenced definitions are still resolved separately."""
    kept: list[str] = []
    in_def = False
    for line in block_text.splitlines():
        if re.match(r"^\[\^([^\]]+)\]:", line):
            in_def = True
            continue
        if in_def and (line.startswith(("    ", "\t")) or not line.strip()):
            continue
        in_def = False
        kept.append(line)
    return "\n".join(kept)


def _block_source_ids(block_text: str, file_lines: list[str]) -> set[str]:
    """Source IDs cited by a block: inline (both syntaxes, with colocated
    markdown footnote definitions masked) plus the IDs in any markdown/HTML
    footnote definitions the block references (Plan 2b §8.2 — definitions
    usually live outside the block's line span)."""
    body = _strip_md_footnote_defs(block_text)
    ids = _cited_source_ids(body)

    md_refs = set(MD_FOOTNOTE_REF_RE.findall(body))
    if md_refs:
        defs = _md_footnote_defs(file_lines)
        for ref in md_refs:
            ids.update(_cited_source_ids(defs.get(ref, "")))

    html_refs = set(HTML_FOOTNOTE_REF_RE.findall(block_text))
    if html_refs:
        defs = _html_anchor_defs(file_lines, html_refs)
        for ref in html_refs:
            ids.update(_cited_source_ids(defs.get(ref, "")))
    return ids


def _span_hash_matches(span_lines: list[str], want_prefix: str) -> bool:
    """A legacy block span self-verifies when some canonical text form of the
    derived span reproduces the ledger's 16-hex content_hash prefix."""
    if not want_prefix:
        return False
    joined = "\n".join(span_lines)
    for candidate in (joined, joined + "\n", joined.strip(), joined.strip() + "\n"):
        if hashlib.sha256(candidate.encode("utf-8")).hexdigest()[:16] == want_prefix:
            return True
    return False


_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


def _find_heading_block(
    lines: list[str], *, anchor: str
) -> tuple[int, int] | None:
    """Locate a block by heading: the first heading line whose text starts with
    `anchor` (dump finding_id like `F2-RESOLVED`, or a supplemental
    origin_anchor heading text). Block runs to the next heading of the same or
    higher level. Returns 0-based (start, end_exclusive) or None."""
    anchor_lower = anchor.strip().lower()
    if not anchor_lower:
        return None
    for i, line in enumerate(lines):
        m = _HEADING_RE.match(line)
        if not m:
            continue
        text = m.group(2).strip().lower()
        if text.startswith(anchor_lower) and (
            len(text) == len(anchor_lower)
            or not text[len(anchor_lower)].isalnum()
        ):
            level = len(m.group(1))
            for j in range(i + 1, len(lines)):
                m2 = _HEADING_RE.match(lines[j])
                if m2 and len(m2.group(1)) <= level:
                    return (i, j)
            return (i, len(lines))
    return None


# --- Plan 2b §8.0: graph export loading ---------------------------------------


def find_latest_snapshot(repo_root: Path) -> Path | None:
    snap_dir = repo_root / SNAPSHOT_DIR_REL
    if not snap_dir.is_dir():
        return None
    best: tuple[int, Path] | None = None
    for path in snap_dir.glob("g13-context-*.ndjson"):
        m = SNAPSHOT_REVISION_RE.search(path.name)
        if not m:
            continue
        rev = int(m.group(1))
        if best is None or rev > best[0]:
            best = (rev, path)
    return best[1] if best else None


def load_graph_export(path: Path) -> GraphView:
    """Read the slice of a recovery/snapshot NDJSON export needed for journey
    and parity checks: units, item ids, and unit -> linked-source sets."""
    view = GraphView(path=str(path))
    item_unit: dict[str, str] = {}
    links: list[tuple[str, str]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if rec.get("record_type") == "manifest":
                view.revision = rec.get("database_revision")
                continue
            if rec.get("record_type") != "row":
                continue
            table = rec.get("table")
            row = rec.get("row", {})
            if table == "research_units":
                view.units.add(row.get("unit_id", ""))
            elif table == "research_items":
                item_id = row.get("item_id", "")
                view.item_ids.add(item_id)
                unit = row.get("research_unit_id")
                if unit:
                    item_unit[item_id] = unit
            elif table == "item_sources":
                links.append((row.get("item_id", ""), row.get("source_id", "")))
    for item_id, source_id in links:
        unit = item_unit.get(item_id)
        if unit and source_id:
            view.unit_sources.setdefault(unit, set()).add(source_id)
    return view


# --- Core checks -------------------------------------------------------------


def _check_disposition_ledger(
    rows: list[dict[str, str]],
    *,
    name: str,
    label_fn,
    allowed: set[str],
) -> LedgerCoverage:
    cov = LedgerCoverage(name=name, total=len(rows), dispositioned=0)
    allowed_norm = {_norm_disp(a) for a in allowed}
    for row in rows:
        disposition = _cell(row, "disposition")
        label = label_fn(row)
        if not disposition:
            cov.gaps.append(label)
            continue
        cov.dispositioned += 1
        if _norm_disp(disposition) not in allowed_norm:
            cov.unknown_dispositions.append(f"{label} -> {disposition!r}")
    return cov


def run_check(
    *,
    coverage_dir: Path,
    sources_path: Path,
    repo_root: Path,
    graph_export: Path | None = None,
) -> CoverageReport:
    """Run every deterministic check and return a structured report."""

    staging_dir = coverage_dir.parent
    legacy_rows = _read_csv(coverage_dir / "legacy-companion-map.csv")
    dump_rows = _read_csv(coverage_dir / "dump-findings-map.csv")
    citation_rows = _read_csv(coverage_dir / "source-and-citation-map.csv")
    supplemental_path = coverage_dir / "supplemental-surfaces-map.csv"
    supplemental_rows = (
        _read_csv(supplemental_path) if supplemental_path.is_file() else []
    )

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
    supplemental_cov = _check_disposition_ledger(
        supplemental_rows,
        name="Supplemental surfaces map",
        label_fn=lambda r: f"{_cell(r, 'origin_anchor')} [{Path(_cell(r, 'origin_path')).name}]",
        allowed=SUPPLEMENTAL_DISPOSITIONS,
    )

    report = CoverageReport(
        legacy=legacy_cov, dump=dump_cov, supplemental=supplemental_cov
    )
    if not supplemental_path.is_file():
        report.warnings.append(
            "supplemental-surfaces-map.csv missing (Plan 2b R1 not applied here)"
        )

    # --- §7.3 citation map + sources.json registration -----------------------
    registered = _sources_index(sources_path)

    # (topic_id, source_id) pairs and per-source registration claims recorded in
    # the citation ledger. Roles feed the Plan 2b §8.4 parity exemptions.
    map_pairs: set[tuple[str, str]] = set()
    map_sources: set[str] = set()
    map_roles: dict[tuple[str, str], set[str]] = {}
    for row in citation_rows:
        topic = _cell(row, "topic_id")
        source = _cell(row, "source_id")
        if not source:
            continue
        map_pairs.add((topic, source))
        map_sources.add(source)
        map_roles.setdefault((topic, source), set()).update(
            _norm_disp(role) for role in _split_multi(_cell(row, "cited_role"))
        )
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
    unit_cited: dict[str, set[str]] = {}
    for topic in manifest.get("topics", []):
        topic_id = topic.get("topicId", "")
        rel = topic.get("path", "")
        unit_path = (repo_root / rel).resolve()
        if not unit_path.is_file():
            report.warnings.append(f"manifest topic path missing: {rel}")
            continue
        text = unit_path.read_text(encoding="utf-8")
        unit_cited[topic_id] = _cited_source_ids(text)
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
    supplemental_paths = {_cell(r, "origin_path") for r in supplemental_rows}
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
        if (
            rel not in legacy_paths
            and rel not in dump_files
            and rel not in supplemental_paths
        ):
            report.inputs_without_rows.append(rel)

    # --- Plan 2b §8.0: graph export -------------------------------------------
    export_path = graph_export or find_latest_snapshot(repo_root)
    graph: GraphView | None = None
    if export_path is not None and Path(export_path).is_file():
        graph = load_graph_export(Path(export_path))
        report.graph_export_path = str(export_path)
        report.graph_revision = graph.revision

    staged_topic_ids = {t.get("topicId", "") for t in manifest.get("topics", [])}

    def _file_lines(rel: str, cache: dict[str, list[str] | None] = {}) -> list[str] | None:
        if rel not in cache:
            target = (repo_root / rel).resolve()
            cache[rel] = (
                target.read_text(encoding="utf-8").splitlines()
                if target.is_file()
                else None
            )
        return cache[rel]

    def _check_source_set(
        *,
        ledger: str,
        label: str,
        parsed: set[str],
        listed: set[str],
        anchored: bool,
        anchor_note: str,
    ) -> None:
        """Plan 2b §8.2: parsed-but-unlisted IDs gate when the block anchored;
        listed-but-unparsed IDs are notes (a ledger may legitimately carry an
        aligned source the block text does not cite verbatim)."""
        missing = sorted(parsed - listed)
        extra = sorted(listed - parsed)
        if missing:
            entry = {
                "ledger": ledger,
                "row": label,
                "missing_in_ledger": ";".join(missing),
                "tier": "anchored" if anchored else anchor_note,
            }
            if anchored:
                report.input_source_set_gaps.append(entry)
            else:
                report.extraction_notes.append(entry)
        if extra:
            report.extraction_notes.append(
                {
                    "ledger": ledger,
                    "row": label,
                    "listed_not_parsed": ";".join(extra),
                    "tier": "anchored" if anchored else anchor_note,
                }
            )
        for sid in sorted(listed):
            if sid not in registered:
                report.unregistered_sources.append(
                    {"source_id": sid, "seen_in": f"{ledger}:{label}"}
                )

    def _check_journey(
        *,
        ledger: str,
        label: str,
        disposition: str,
        destinations: list[str],
        source_ids: list[str],
    ) -> None:
        """Plan 2b §8.3: a journey-checked row's sources must be linked in the
        destination unit's graph items; preserved dispositions are the reviewed
        escape hatch; needs_decision is friction."""
        disp = _norm_disp(disposition)
        if disp == "needs_decision":
            report.friction_needs_decision.append(
                {"ledger": ledger, "row": label, "reason": "disposition needs_decision"}
            )
            return
        if disp not in JOURNEY_CHECKED.get(ledger, set()):
            return
        if not source_ids:
            return
        staged_dests = [d for d in destinations if d in staged_topic_ids]
        if not destinations:
            report.source_journey_gaps.append(
                {
                    "ledger": ledger,
                    "row": label,
                    "source_id": ";".join(source_ids),
                    "reason": "journey-checked row has no destination topic",
                }
            )
            return
        if not staged_dests:
            report.journey_deferred.append(
                {"ledger": ledger, "row": label, "destinations": ";".join(destinations)}
            )
            return
        if graph is None:
            return  # graph_export_missing gates separately
        available: set[str] = set()
        for dest in staged_dests:
            available |= graph.unit_sources.get(dest, set())
        for sid in source_ids:
            if sid not in available:
                report.source_journey_gaps.append(
                    {
                        "ledger": ledger,
                        "row": label,
                        "source_id": sid,
                        "reason": f"not linked to any item in {';'.join(staged_dests)}",
                    }
                )

    # --- Plan 2b §8.2 + §8.3: legacy rows (span-anchored, self-verified) ------
    legacy_by_file: dict[str, list[dict[str, str]]] = {}
    for row in legacy_rows:
        if _cell(row, "line_start_at_inventory").isdigit():
            legacy_by_file.setdefault(_cell(row, "legacy_path"), []).append(row)
    for rel, rows in legacy_by_file.items():
        lines = _file_lines(rel)
        rows.sort(key=lambda r: int(_cell(r, "line_start_at_inventory")))
        for i, row in enumerate(rows):
            if not _cell(row, "disposition"):
                continue
            label = f"{_cell(row, 'legacy_heading')} (l.{_cell(row, 'line_start_at_inventory')})"
            listed = set(_split_multi(_cell(row, "source_ids")))
            destinations = _split_multi(_cell(row, "destination_topic"))
            _check_journey(
                ledger="legacy",
                label=label,
                disposition=_cell(row, "disposition"),
                destinations=destinations,
                source_ids=sorted(listed),
            )
            if lines is None:
                continue
            start = int(_cell(row, "line_start_at_inventory"))
            end = (
                int(_cell(rows[i + 1], "line_start_at_inventory")) - 1
                if i + 1 < len(rows)
                else len(lines)
            )
            span = lines[start - 1 : end]
            anchored = _span_hash_matches(span, _cell(row, "content_hash"))
            parsed = _block_source_ids("\n".join(span), lines)
            _check_source_set(
                ledger="legacy",
                label=label,
                parsed=parsed,
                listed=listed,
                anchored=anchored,
                anchor_note="block_span_unverified",
            )

    # --- Plan 2b §8.2 + §8.3: dump rows (heading-anchored on finding_id) ------
    dump_has_source_ids = bool(dump_rows) and "source_ids" in dump_rows[0]
    if dump_rows and not dump_has_source_ids:
        report.warnings.append(
            "dump-findings-map.csv lacks the Plan 2b source_ids column; "
            "dump source-set and journey checks skipped"
        )
    if dump_has_source_ids:
        for row in dump_rows:
            if not _cell(row, "disposition"):
                continue
            label = (
                f"{_cell(row, 'finding_id')} [{Path(_cell(row, 'dump_file')).name}]"
            )
            listed = set(_split_multi(_cell(row, "source_ids")))
            destinations = (
                _split_multi(_cell(row, "destination_path"))
                if _norm_disp(_cell(row, "destination_type")) == "topic"
                else []
            )
            _check_journey(
                ledger="dump",
                label=label,
                disposition=_cell(row, "disposition"),
                destinations=destinations,
                source_ids=sorted(listed),
            )
            lines = _file_lines(_cell(row, "dump_file"))
            if lines is None:
                continue
            block = _find_heading_block(lines, anchor=_cell(row, "finding_id"))
            if block is None:
                if listed:
                    report.extraction_notes.append(
                        {
                            "ledger": "dump",
                            "row": label,
                            "tier": "extraction_unanchored",
                        }
                    )
                continue
            parsed = _block_source_ids("\n".join(lines[block[0] : block[1]]), lines)
            _check_source_set(
                ledger="dump",
                label=label,
                parsed=parsed,
                listed=listed,
                anchored=True,
                anchor_note="",
            )

    # --- Plan 2b §8.2/§8.3/§8.5: supplemental rows ----------------------------
    for row in supplemental_rows:
        anchor = _cell(row, "origin_anchor")
        label = f"{anchor} [{Path(_cell(row, 'origin_path')).name}]"
        disposition = _cell(row, "disposition")
        listed = set(_split_multi(_cell(row, "source_ids")))
        for token in _split_multi(_cell(row, "friction")):
            norm = _norm_disp(token)
            if norm not in SUPPLEMENTAL_FRICTION:
                report.warnings.append(f"unknown friction value {token!r} on {label}")
            if norm == "needs_source_pull":
                report.friction_needs_decision.append(
                    {"ledger": "supplemental", "row": label, "reason": token}
                )
            else:
                report.friction_open.append(
                    {"ledger": "supplemental", "row": label, "friction": token}
                )
        if not disposition:
            continue
        _check_journey(
            ledger="supplemental",
            label=label,
            disposition=disposition,
            destinations=_split_multi(_cell(row, "destination_topic")),
            source_ids=sorted(listed),
        )
        lines = _file_lines(_cell(row, "origin_path"))
        if lines is not None:
            block = _find_heading_block(lines, anchor=anchor)
            if block is None:
                if listed:
                    report.extraction_notes.append(
                        {
                            "ledger": "supplemental",
                            "row": label,
                            "tier": "extraction_unanchored",
                        }
                    )
            else:
                parsed = _block_source_ids(
                    "\n".join(lines[block[0] : block[1]]), lines
                )
                _check_source_set(
                    ledger="supplemental",
                    label=label,
                    parsed=parsed,
                    listed=listed,
                    anchored=True,
                    anchor_note="",
                )
        # §8.5 mechanical projection of publication alignment.
        if _norm_disp(_cell(row, "origin_kind")) in {"fact_sheet", "case_file"} and _norm_disp(
            disposition
        ) in {"incorporated", "summarized"}:
            item_ids = _split_multi(_cell(row, "research_item_ids"))
            if not item_ids:
                report.publication_mapping_gaps.append(
                    {
                        "row": label,
                        "reason": "incorporated publication block maps no research items",
                    }
                )
            elif graph is not None:
                unknown = [i for i in item_ids if i not in graph.item_ids]
                if unknown:
                    report.publication_mapping_gaps.append(
                        {
                            "row": label,
                            "reason": f"mapped items not in graph: {';'.join(unknown)}",
                        }
                    )

    # --- Plan 2b §8.4: topic prose ↔ graph parity ------------------------------
    if graph is not None:
        for topic_id, prose_sources in sorted(unit_cited.items()):
            graph_sources = graph.unit_sources.get(topic_id, set())
            exempt = {
                source
                for (t, source), roles in map_roles.items()
                if t == topic_id and roles & PARITY_EXEMPT_ROLES
            }
            for sid in sorted(prose_sources - graph_sources - exempt):
                report.topic_graph_source_gaps.append(
                    {
                        "topic_id": topic_id,
                        "source_id": sid,
                        "direction": "cited in prose, linked to no item in unit",
                    }
                )
            for sid in sorted(graph_sources - prose_sources - exempt):
                report.topic_graph_source_gaps.append(
                    {
                        "topic_id": topic_id,
                        "source_id": sid,
                        "direction": "linked to item in unit, never cited in prose",
                    }
                )
            if topic_id not in graph.units:
                report.warnings.append(
                    f"staged topic {topic_id} has no research_units row in graph export"
                )

    # --- Plan 2b §8.0: was graph truth required but unavailable? ---------------
    journey_relevant = bool(report.source_journey_gaps) or any(
        _norm_disp(_cell(r, "disposition")) in JOURNEY_CHECKED[kind]
        for kind, rows in (
            ("legacy", legacy_rows),
            ("dump", dump_rows),
            ("supplemental", supplemental_rows),
        )
        for r in rows
    )
    if graph is None and (staged_topic_ids or journey_relevant):
        report.graph_export_missing = True

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
    out.append("G13 refactor coverage check (Plan 02 §7.4 + Plan 2b §8)")
    out.append("=" * 56)
    out.extend(_render_ledger_block(report.legacy, show_gaps=show_gaps))
    out.append("")
    out.extend(_render_ledger_block(report.dump, show_gaps=show_gaps))
    out.append("")
    out.extend(_render_ledger_block(report.supplemental, show_gaps=show_gaps))
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

    # Plan 2b §8 categories.
    if report.graph_export_path:
        out.append(
            f"Graph export: {Path(report.graph_export_path).name} "
            f"(revision {report.graph_revision})"
        )
    if report.graph_export_missing:
        out.append(
            "[FAIL] graph export missing: journey/parity checks require a "
            "snapshot NDJSON (Plan 2b §8.0)"
        )
    sets_status = "ok" if not report.input_source_set_gaps else "FAIL"
    out.append(
        f"[{sets_status}] Input source-set integrity (§8.2): "
        f"{len(report.input_source_set_gaps)} gap(s)"
    )
    for g in report.input_source_set_gaps:
        out.append(
            f"         - {g['ledger']}: {g['row']} block cites "
            f"{g['missing_in_ledger']} not in ledger source_ids"
        )
    journey_status = "ok" if not report.source_journey_gaps else "FAIL"
    out.append(
        f"[{journey_status}] Source-journey integrity (§8.3): "
        f"{len(report.source_journey_gaps)} gap(s), "
        f"{len(report.journey_deferred)} deferred (destination not yet staged)"
    )
    for g in report.source_journey_gaps:
        out.append(
            f"         - {g['ledger']}: {g['row']} `{g['source_id']}` — {g['reason']}"
        )
    parity_status = "ok" if not report.topic_graph_source_gaps else "FAIL"
    out.append(
        f"[{parity_status}] Topic prose <-> graph source parity (§8.4): "
        f"{len(report.topic_graph_source_gaps)} gap(s)"
    )
    for g in report.topic_graph_source_gaps:
        out.append(
            f"         - {g['topic_id']}: `{g['source_id']}` — {g['direction']}"
        )
    pub_status = "ok" if not report.publication_mapping_gaps else "FAIL"
    out.append(
        f"[{pub_status}] Publication mapping (§8.5): "
        f"{len(report.publication_mapping_gaps)} gap(s)"
    )
    for g in report.publication_mapping_gaps:
        out.append(f"         - {g['row']}: {g['reason']}")
    fric_status = "ok" if not report.friction_needs_decision else "FAIL"
    out.append(
        f"[{fric_status}] Friction needing a decision (§8.6): "
        f"{len(report.friction_needs_decision)}"
        + (f" (+{len(report.friction_open)} recorded, non-gating)" if report.friction_open else "")
    )
    for g in report.friction_needs_decision:
        out.append(f"         - {g['ledger']}: {g['row']} — {g['reason']}")
    if report.extraction_notes:
        out.append(
            f"[note] extraction tier notes ({len(report.extraction_notes)}): "
            "unverified spans / unanchored blocks / ledger-only source ids"
        )
        for n in report.extraction_notes:
            detail = n.get("missing_in_ledger") or n.get("listed_not_parsed") or ""
            out.append(
                f"         - {n['ledger']}: {n['row']} [{n['tier']}]"
                + (f" {detail}" if detail else "")
            )
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
    backlog = (
        report.legacy.backlog + report.dump.backlog + report.supplemental.backlog
    )
    out.append(
        f"RESULT: {verdict} — {report.gating_problem_count} gating problem(s) "
        f"({backlog} un-dispositioned, "
        f"{len(report.unit_citation_gaps) + len(report.unregistered_sources)} citation gap(s), "
        f"{inv_bad} inventory)"
    )
    sl = "PASS" if report.source_lossless else "PENDING"
    counts = report.source_lossless_counts
    out.append(
        f"SOURCE-LOSSLESS: {sl} — "
        + ", ".join(f"{k}={v}" for k, v in counts.items())
        + f", backlog={backlog}"
    )
    return "\n".join(out)


def report_to_dict(report: CoverageReport) -> dict[str, Any]:
    return {
        "ok": report.ok,
        "gating_problem_count": report.gating_problem_count,
        "source_lossless": report.source_lossless,
        "source_lossless_counts": report.source_lossless_counts,
        "graph_export": {
            "path": report.graph_export_path,
            "revision": report.graph_revision,
            "missing": report.graph_export_missing,
        },
        "input_source_set_gaps": report.input_source_set_gaps,
        "source_journey_gaps": report.source_journey_gaps,
        "journey_deferred": report.journey_deferred,
        "topic_graph_source_gaps": report.topic_graph_source_gaps,
        "publication_mapping_gaps": report.publication_mapping_gaps,
        "friction_needs_decision": report.friction_needs_decision,
        "friction_open": report.friction_open,
        "extraction_notes": report.extraction_notes,
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
            "supplemental": {
                "total": report.supplemental.total,
                "dispositioned": report.supplemental.dispositioned,
                "backlog": report.supplemental.backlog,
                "coverage_pct": report.supplemental.coverage_pct,
                "gaps": report.supplemental.gaps,
                "unknown_dispositions": report.supplemental.unknown_dispositions,
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
    parser.add_argument(
        "--graph-export",
        type=Path,
        default=None,
        help="Graph recovery/snapshot NDJSON used for journey and parity checks "
        "(default: newest data/context-graphs/g13/exports/snapshots/*.ndjson).",
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
        graph_export=args.graph_export,
    )

    if args.json:
        print(json.dumps(report_to_dict(report), indent=2, ensure_ascii=False))
    else:
        print(render_text(report, show_gaps=not args.no_gaps))

    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
