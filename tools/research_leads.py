#!/usr/bin/env python3
"""
Research lead catalog utility for gurney-genealogy.

This tool intentionally keeps research/future-research/research-leads.csv as the
canonical store while giving humans and AI agents small, ID-based operations that
avoid reading or rewriting the entire CSV in ordinary work.

Design goals:
- robust CSV parsing and writing with Python's csv module;
- preserve unknown/manual columns when possible;
- warn, rather than block, on long narrative fields;
- block only values that are likely to corrupt manual CSV workflows;
- make online-reachable priority triage a first-class operation;
- keep done entries thin and remind the operator to promote facts to research
  files before closing a lead.
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import difflib
import json
import os
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Sequence

# Canonical repository-relative paths.
DEFAULT_OPEN_REL = Path("research/future-research/research-leads.csv")
DEFAULT_DONE_REL = Path("research/future-research/research-leads-done.csv")

# Canonical/open CSV column names documented in research/future-research/README.md.
REQUIRED_OPEN_FIELDS = [
    "ID",
    "Priority",
    "Gen",
    "Subject",
    "Lead/Source",
    "Description",
    "Online",
    "Status",
    "Source ref",
]

# Thin done archive. Do not put full research narratives here. The fifth column is
# named "Companion ref" to match the existing research-leads-done.csv; the value is
# carried over from the open row's "Source ref".
STANDARD_DONE_FIELDS = ["ID", "Subject", "Disposition", "Date", "Companion ref"]

# Controlled/recommended values. Existing CSV rows may be looser; new writes warn.
ONLINE_VALUES = {"Y", "Part", "N", "Unk"}
RECOMMENDED_STATUS_VALUES = {"Open", "Partial"}
ONLINE_REACHABLE_DEFAULT = {"Y", "Part"}

ID_RE = re.compile(r"^L-(\d+)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Non-blocking length guidance. These values are deliberately conservative:
# the goal is not schema purity; it is to remind AI agents not to turn the CSV
# into a narrative store.
FIELD_LENGTH_WARN = {
    "Subject": 90,
    "Lead/Source": 180,
    "Description": 360,
    "Status": 140,
    "Source ref": 160,
}
ROW_LENGTH_WARN = 900

# Columns the canonical CSV always quotes, even when the value needs no escaping.
# This preserves the file's hand-authored quoting style so a single-field edit
# diffs at one or two rows instead of reflowing every line. All other columns use
# minimal quoting (quote only when the value contains a comma/quote/newline).
ALWAYS_QUOTE_FIELDS = {"Subject", "Lead/Source", "Description"}
_QUOTE_TRIGGER_CHARS = (",", '"', "\n", "\r")

# Characters that are legal in CSV but risky for human/manual editing.
RISKY_TEXT_CHARS = {
    ",": "comma: csv module will quote it, but manual edits become easier to break",
    '"': "double quote: csv module will escape it, but review resulting diff carefully",
    "\t": "tab: usually accidental in CSV free text",
}

# Characters that can break tooling or produce multi-line CSV rows. Multi-line
# fields are technically valid CSV, but they are hostile to hand review and grep.
BLOCKED_CONTROL_CHARS = {"\x00": "NUL byte is not permitted"}
LINEBREAK_CHARS = {"\n", "\r"}


@dataclass
class WarningMessage:
    """Structured warning emitted by validation and write operations."""

    code: str
    message: str
    lead_id: str | None = None
    field: str | None = None

    def as_dict(self) -> dict[str, str]:
        data: dict[str, str] = {"code": self.code, "message": self.message}
        if self.lead_id:
            data["id"] = self.lead_id
        if self.field:
            data["field"] = self.field
        return data


@dataclass
class LeadStore:
    """In-memory view of the open and done lead CSVs."""

    open_path: Path
    done_path: Path
    headers: list[str]
    rows: list[dict[str, str]]
    load_warnings: list[WarningMessage] = field(default_factory=list)

    @classmethod
    def load(cls, open_path: Path, done_path: Path) -> "LeadStore":
        headers, rows, warnings = read_csv_dicts(open_path)
        missing = [field for field in REQUIRED_OPEN_FIELDS if field not in headers]
        for field_name in missing:
            warnings.append(
                WarningMessage(
                    "missing-required-column",
                    f"Open CSV is missing required column {field_name!r}.",
                    field=field_name,
                )
            )
        return cls(open_path=open_path, done_path=done_path, headers=headers, rows=rows, load_warnings=warnings)

    def find(self, lead_id: str) -> dict[str, str] | None:
        for row in self.rows:
            if row.get("ID") == lead_id:
                return row
        return None

    def ids(self) -> list[str]:
        return [row.get("ID", "") for row in self.rows if row.get("ID")]

    def next_id(self) -> str:
        max_num = 0
        for lead_id in self.ids():
            match = ID_RE.match(lead_id.strip())
            if match:
                max_num = max(max_num, int(match.group(1)))
        return f"L-{max_num + 1}"

    def sorted_rows(self, rows: Iterable[dict[str, str]] | None = None) -> list[dict[str, str]]:
        """Sort rows by descending priority, then numeric lead ID where possible."""

        source = list(self.rows if rows is None else rows)
        return sorted(source, key=lambda row: (-parse_priority(row.get("Priority", "")), id_sort_key(row.get("ID", ""))))

    def write_open(self, rows: list[dict[str, str]], *, dry_run: bool, backup: bool, verbose: bool = False) -> str | None:
        return write_csv_atomic(self.open_path, self.headers, rows, dry_run=dry_run, backup=backup, verbose=verbose)


def find_repo_root(start: Path | None = None) -> Path:
    """Find a plausible repo root by walking upward from cwd/script location."""

    candidates: list[Path] = []
    if start is not None:
        candidates.append(start.resolve())
    candidates.append(Path.cwd().resolve())
    candidates.append(Path(__file__).resolve().parent.parent)

    seen: set[Path] = set()
    for candidate in candidates:
        for path in [candidate, *candidate.parents]:
            if path in seen:
                continue
            seen.add(path)
            if (path / DEFAULT_OPEN_REL).exists():
                return path
    return Path.cwd().resolve()


def resolve_paths(args: argparse.Namespace) -> tuple[Path, Path, Path]:
    repo_root = Path(args.repo_root).resolve() if args.repo_root else find_repo_root()
    open_path = Path(args.leads).resolve() if args.leads else repo_root / DEFAULT_OPEN_REL
    done_path = Path(args.done).resolve() if args.done else repo_root / DEFAULT_DONE_REL
    return repo_root, open_path, done_path


def read_csv_dicts(path: Path) -> tuple[list[str], list[dict[str, str]], list[WarningMessage]]:
    """Read a CSV file robustly while preserving column order.

    Uses utf-8-sig so a Windows/Excel BOM will not poison the first header.
    Extra cells are recorded as load warnings. Missing cells are converted to
    empty strings so downstream operations do not fail with None values.
    """

    warnings: list[WarningMessage] = []
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, restkey="__EXTRA__", restval="")
        headers = list(reader.fieldnames or [])
        rows: list[dict[str, str]] = []
        if not headers:
            warnings.append(WarningMessage("missing-header", f"CSV file has no header: {path}"))
            return [], [], warnings

        for line_num, raw_row in enumerate(reader, start=2):
            extra = raw_row.pop("__EXTRA__", None)
            if extra:
                warnings.append(
                    WarningMessage(
                        "extra-cells",
                        f"Row {line_num} has {len(extra)} extra cell(s); likely unquoted comma or manual CSV damage.",
                        lead_id=raw_row.get("ID") or None,
                    )
                )
            row = {header: normalize_cell(raw_row.get(header, "")) for header in headers}
            rows.append(row)
    return headers, rows, warnings


def normalize_cell(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _truncate(value: str, width: int = 100) -> str:
    collapsed = " ".join((value or "").split())
    return collapsed if len(collapsed) <= width else collapsed[: width - 1] + "…"


def format_row_dry_run(path: Path, headers: Sequence[str], new_rows: Sequence[dict[str, str]]) -> str:
    """Compact dry-run: report only the rows that change, field by field.

    The full-file unified diff is hostile to review on this CSV (every row is one
    long line), so by default a single-field edit prints just that row's deltas.
    Pass --verbose to get the unified diff instead.
    """

    old_rows: list[dict[str, str]] = []
    if path.exists():
        _, old_rows, _ = read_csv_dicts(path)

    def by_id(rows: Sequence[dict[str, str]]) -> dict[str, dict[str, str]]:
        indexed: dict[str, dict[str, str]] = {}
        for position, row in enumerate(rows):
            indexed[row.get("ID") or f"__row{position}"] = row
        return indexed

    old, new = by_id(old_rows), by_id(new_rows)
    added = [lead_id for lead_id in new if lead_id not in old]
    removed = [lead_id for lead_id in old if lead_id not in new]
    changed: list[tuple[str, list[tuple[str, str, str]]]] = []
    for lead_id, row in new.items():
        prior = old.get(lead_id)
        if prior is None:
            continue
        deltas = [(name, prior.get(name, ""), row.get(name, "")) for name in headers if prior.get(name, "") != row.get(name, "")]
        if deltas:
            changed.append((lead_id, deltas))

    lines = [
        f"# dry-run: {len(changed)} changed, {len(added)} added, {len(removed)} removed; "
        "no file written. Use --verbose for the full unified diff."
    ]
    for lead_id, deltas in changed:
        lines.append(f"~ {lead_id}")
        for name, old_value, new_value in deltas:
            lines.append(f"    {name}: {_truncate(old_value)!r} -> {_truncate(new_value)!r}")
    for lead_id in added:
        row = new[lead_id]
        priority = row.get("Priority", "")
        label = f"P{priority}  " if priority else ""
        lines.append(f"+ {lead_id}  {label}{_truncate(row.get('Subject', ''), 60)}")
    for lead_id in removed:
        lines.append(f"- {lead_id}  {_truncate(old[lead_id].get('Subject', ''), 60)}")
    return "\n".join(lines)


def write_csv_atomic(path: Path, headers: Sequence[str], rows: Sequence[dict[str, str]], *, dry_run: bool, backup: bool, verbose: bool = False) -> str | None:
    """Atomically rewrite a CSV file, optionally retaining local backups for 30 days."""

    serialized = serialize_csv(headers, rows)
    if dry_run:
        if not verbose:
            return format_row_dry_run(path, headers, rows)
        before = path.read_text(encoding="utf-8-sig") if path.exists() else ""
        diff = difflib.unified_diff(
            before.splitlines(keepends=True),
            serialized.splitlines(keepends=True),
            fromfile=str(path),
            tofile=f"{path} (proposed)",
        )
        return "# dry-run: full unified diff (--verbose)\n" + "".join(diff)

    path.parent.mkdir(parents=True, exist_ok=True)
    if backup and path.exists():
        timestamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_dir = path.parent / "_local" / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = backup_dir / f"{path.name}.{timestamp}.bak"
        shutil.copy2(path, backup_path)
        cutoff = _dt.datetime.now().timestamp() - (30 * 24 * 60 * 60)
        for old_backup in backup_dir.glob(f"{path.name}.*.bak"):
            if old_backup.stat().st_mtime < cutoff:
                old_backup.unlink()

    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(serialized)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    return None


def _serialize_cell(field_name: str, value: str, *, is_header: bool) -> str:
    """Quote one cell, preserving the canonical CSV's per-column quoting style."""

    always = (not is_header) and bool(value) and field_name in ALWAYS_QUOTE_FIELDS
    if always or any(char in value for char in _QUOTE_TRIGGER_CHARS):
        return '"' + value.replace('"', '""') + '"'
    return value


def serialize_csv(headers: Sequence[str], rows: Sequence[dict[str, str]]) -> str:
    """Serialize rows with commas/quotes escaped, matching the canonical file's
    per-column quoting (always-quote narrative columns, minimal elsewhere).

    Output matches csv.writer escaping but keeps the always-quoted narrative
    columns quoted so routine single-field edits produce a one-row diff instead
    of reflowing the whole file. See ALWAYS_QUOTE_FIELDS.
    """

    header_names = list(headers)
    lines = [",".join(_serialize_cell(name, name, is_header=True) for name in header_names)]
    for row in rows:
        lines.append(",".join(_serialize_cell(name, row.get(name, ""), is_header=False) for name in header_names))
    return "\n".join(lines) + "\n"


def ensure_done_file(path: Path, dry_run: bool) -> tuple[list[str], list[dict[str, str]], list[WarningMessage]]:
    """Load the done CSV or prepare a new thin archive schema."""

    if path.exists():
        return read_csv_dicts(path)
    if dry_run:
        return STANDARD_DONE_FIELDS.copy(), [], [WarningMessage("done-file-missing", f"Done CSV would be created: {path}")]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(",".join(STANDARD_DONE_FIELDS) + "\n", encoding="utf-8")
    return read_csv_dicts(path)


# A lead is "stale-done" when its Status reads as a concluded disposition while
# the row still sits in the OPEN csv (it should have been moved to the done csv).
# The convention is that such a Status leads with the disposition verb, allowing a
# couple of qualifying words ("Probate clause DONE", "Blomefield part DONE").
STALE_DONE_RE = re.compile(r"^(?:\w+[\s\-]+){0,2}(done|resolved)\b", re.IGNORECASE)


def is_stale_done(status: str) -> bool:
    return bool(STALE_DONE_RE.match((status or "").strip()))


def parse_priority(value: str) -> int:
    try:
        return int(str(value).strip())
    except ValueError:
        return -1


def id_sort_key(lead_id: str) -> tuple[int, str]:
    match = ID_RE.match((lead_id or "").strip())
    if match:
        return (int(match.group(1)), "")
    return (10**9, lead_id or "")


def normalize_id(lead_id: str) -> str:
    value = lead_id.strip().upper()
    # Accept common human shorthand like "115".
    if value.isdigit():
        value = f"L-{value}"
    return value


def validate_text_value(field_name: str, value: str, *, allow_multiline: bool, lead_id: str | None = None) -> tuple[str, list[WarningMessage]]:
    """Validate one free-text value.

    Commas and quotes are not rejected because csv.writer handles them; warnings
    are emitted so an AI/human can pay attention to resulting diffs. Newlines are
    blocked by default because multi-line CSV cells are fragile for manual use.
    """

    warnings: list[WarningMessage] = []
    for char, reason in BLOCKED_CONTROL_CHARS.items():
        if char in value:
            raise ValueError(f"{field_name}: {reason}")

    if not allow_multiline and any(char in value for char in LINEBREAK_CHARS):
        raise ValueError(
            f"{field_name}: line breaks are not permitted by default because they create multi-line CSV cells. "
            "Replace them with spaces or pass --allow-multiline deliberately."
        )

    for char, reason in RISKY_TEXT_CHARS.items():
        if char in value:
            warnings.append(WarningMessage("risky-character", f"{field_name} contains {reason}.", lead_id=lead_id, field=field_name))

    if any(char in value for char in LINEBREAK_CHARS):
        warnings.append(WarningMessage("multiline-field", f"{field_name} contains line breaks; manual CSV editing will be fragile.", lead_id=lead_id, field=field_name))

    return value, warnings


def validate_row(row: dict[str, str], *, existing: bool) -> list[WarningMessage]:
    """Validate a row and return warnings. Existing rows warn rather than fail."""

    warnings: list[WarningMessage] = []
    lead_id = row.get("ID", "")

    if not ID_RE.match(lead_id):
        warnings.append(WarningMessage("bad-id", f"Lead ID {lead_id!r} does not match L-123 format.", lead_id=lead_id or None, field="ID"))

    priority = row.get("Priority", "")
    parsed_priority = parse_priority(priority)
    if parsed_priority < 1 or parsed_priority > 100:
        warnings.append(WarningMessage("bad-priority", f"Priority {priority!r} should be an integer 1-100.", lead_id=lead_id or None, field="Priority"))

    online = row.get("Online", "")
    if online and online not in ONLINE_VALUES:
        warnings.append(
            WarningMessage(
                "bad-online",
                f"Online value {online!r} is not one of {sorted(ONLINE_VALUES)}.",
                lead_id=lead_id or None,
                field="Online",
            )
        )

    status = row.get("Status", "")
    if status and status not in RECOMMENDED_STATUS_VALUES:
        severity = "existing non-standard" if existing else "new non-standard"
        warnings.append(
            WarningMessage(
                "non-standard-status",
                f"{severity} Status {status!r}; prefer Open or Partial and put narrative in research files.",
                lead_id=lead_id or None,
                field="Status",
            )
        )

    for field_name, max_len in FIELD_LENGTH_WARN.items():
        value = row.get(field_name, "")
        if len(value) > max_len:
            warnings.append(
                WarningMessage(
                    "long-field",
                    f"{field_name} length {len(value)} exceeds guidance {max_len}; keep CSV as an index, not narrative storage.",
                    lead_id=lead_id or None,
                    field=field_name,
                )
            )

    row_len = sum(len(row.get(field_name, "")) for field_name in REQUIRED_OPEN_FIELDS)
    if row_len > ROW_LENGTH_WARN:
        warnings.append(
            WarningMessage(
                "long-row",
                f"Lead row total text length {row_len} exceeds guidance {ROW_LENGTH_WARN}; consider moving narrative detail to the companion file.",
                lead_id=lead_id or None,
            )
        )

    return warnings


def validate_catalog(store: LeadStore, done_path: Path) -> list[WarningMessage]:
    warnings = list(store.load_warnings)

    seen: dict[str, int] = {}
    for index, row in enumerate(store.rows, start=2):
        lead_id = row.get("ID", "")
        if lead_id:
            if lead_id in seen:
                warnings.append(WarningMessage("duplicate-id", f"Lead ID {lead_id} appears more than once in open CSV.", lead_id=lead_id))
            seen[lead_id] = index
        warnings.extend(validate_row(row, existing=True))

    if done_path.exists():
        done_headers, done_rows, done_warnings = read_csv_dicts(done_path)
        warnings.extend(done_warnings)
        done_ids = {row.get("ID", "") for row in done_rows if row.get("ID")}
        overlap = sorted(set(seen) & done_ids, key=id_sort_key)
        for lead_id in overlap:
            warnings.append(WarningMessage("open-done-overlap", f"Lead ID {lead_id} appears in both open and done CSVs.", lead_id=lead_id))
        for field_name in STANDARD_DONE_FIELDS:
            if field_name not in done_headers:
                warnings.append(WarningMessage("done-missing-column", f"Done CSV is missing expected column {field_name!r}.", field=field_name))

    return warnings


def filter_rows(rows: Iterable[dict[str, str]], args: argparse.Namespace) -> list[dict[str, str]]:
    result = list(rows)

    if getattr(args, "status", None):
        statuses = set(args.status)
        result = [row for row in result if row.get("Status", "") in statuses]

    if getattr(args, "gen", None):
        gens = set(args.gen)
        result = [row for row in result if row.get("Gen", "") in gens]

    if getattr(args, "online", None):
        online_values = set(args.online)
        result = [row for row in result if row.get("Online", "") in online_values]

    if getattr(args, "online_reachable", False):
        result = [row for row in result if row.get("Online", "") in ONLINE_REACHABLE_DEFAULT]

    if getattr(args, "include_unknown", False):
        # Use after --online-reachable to include Unk without including physical N.
        allowed = ONLINE_REACHABLE_DEFAULT | {"Unk"}
        result = [row for row in rows if row.get("Online", "") in allowed]

    if getattr(args, "min_priority", None) is not None:
        result = [row for row in result if parse_priority(row.get("Priority", "")) >= args.min_priority]

    if getattr(args, "max_priority", None) is not None:
        result = [row for row in result if parse_priority(row.get("Priority", "")) <= args.max_priority]

    if getattr(args, "query", None):
        query = args.query.lower()
        searchable_fields = ["ID", "Gen", "Subject", "Lead/Source", "Description", "Status", "Source ref"]
        result = [
            row
            for row in result
            if any(query in row.get(field_name, "").lower() for field_name in searchable_fields)
        ]

    return result


def format_rows(rows: Sequence[dict[str, str]], *, output_format: str, fields: Sequence[str] | None = None, warnings: Sequence[WarningMessage] = ()) -> str:
    fields = list(fields or ["ID", "Priority", "Gen", "Subject", "Lead/Source", "Online", "Status", "Source ref"])

    if output_format == "json":
        return json.dumps(
            {
                "count": len(rows),
                "warnings": [warning.as_dict() for warning in warnings],
                "rows": [{field: row.get(field, "") for field in fields} for row in rows],
            },
            ensure_ascii=False,
            indent=2,
        )

    if output_format == "csv":
        return serialize_csv(fields, rows)

    if not rows:
        body = "No matching leads."
    elif output_format == "markdown":
        body = format_markdown_table(rows, fields)
    else:  # compact text
        body = "\n".join(format_compact_row(row) for row in rows)

    if warnings and output_format != "json":
        warning_text = "\n".join(f"WARNING [{w.code}]{' ' + w.lead_id if w.lead_id else ''}: {w.message}" for w in warnings)
        return f"{body}\n\n{warning_text}"
    return body


def format_markdown_table(rows: Sequence[dict[str, str]], fields: Sequence[str]) -> str:
    if not rows:
        return "No matching leads."

    def clean(value: str, width: int = 90) -> str:
        value = " ".join((value or "").split())
        if len(value) > width:
            return value[: width - 1] + "…"
        return value.replace("|", "\\|")

    header = "| " + " | ".join(fields) + " |"
    divider = "| " + " | ".join("---" for _ in fields) + " |"
    lines = [header, divider]
    for row in rows:
        lines.append("| " + " | ".join(clean(row.get(field, "")) for field in fields) + " |")
    return "\n".join(lines)


def format_compact_row(row: dict[str, str]) -> str:
    priority = row.get("Priority", "")
    online = row.get("Online", "")
    status = " ".join(row.get("Status", "").split())
    if len(status) > 80:
        status = status[:79] + "…"
    subject = " ".join(row.get("Subject", "").split())
    source = " ".join(row.get("Lead/Source", "").split())
    if len(source) > 120:
        source = source[:119] + "…"
    return f"{row.get('ID', '')} | P{priority} | {online} | {status} | {subject} — {source}"


def format_lead_detail(row: dict[str, str], *, output_format: str, warnings: Sequence[WarningMessage] = ()) -> str:
    if output_format == "json":
        return json.dumps({"warnings": [w.as_dict() for w in warnings], "row": row}, ensure_ascii=False, indent=2)

    if output_format == "csv":
        return serialize_csv(REQUIRED_OPEN_FIELDS, [row])

    lines = [
        f"## {row.get('ID', '')} — {row.get('Subject', '')}",
        "",
        f"- Priority: {row.get('Priority', '')}",
        f"- Gen: {row.get('Gen', '')}",
        f"- Online: {row.get('Online', '')}",
        f"- Status: {row.get('Status', '')}",
        f"- Source ref: {row.get('Source ref', '')}",
        "",
        "### Lead/Source",
        row.get("Lead/Source", ""),
        "",
        "### Description",
        row.get("Description", ""),
    ]
    if warnings:
        lines.extend(["", "### Tool warnings"])
        lines.extend(f"- [{w.code}] {w.message}" for w in warnings)
    return "\n".join(lines)


def format_context(row: dict[str, str], *, output_format: str, warnings: Sequence[WarningMessage] = ()) -> str:
    if output_format == "json":
        return json.dumps(
            {
                "warnings": [w.as_dict() for w in warnings],
                "lead": row,
                "pre_pull_checklist": [
                    "Check whether the source is already held in data/sources.json, data/indexes/source-ids.csv, sources/corpus, or sources/corpus_supplement.",
                    "Ground first via repo_search + Read (not Grep): read the Source-ref companion AND the subject's ancestor/place companion before any online work; they are more authoritative than the CSV and usually already hold the answer or the exact delta.",
                    "Scope work to the delta only; do not rework already-held material.",
                    "If closing the lead, first promote facts/findings to the appropriate research companion/case file.",
                ],
            },
            ensure_ascii=False,
            indent=2,
        )

    text = format_lead_detail(row, output_format="markdown", warnings=warnings)
    checklist = "\n".join(
        [
            "### Pre-pull checklist",
            "- Check whether the source is already held in `data/sources.json`, `data/indexes/source-ids.csv`, `sources/corpus/`, or `sources/corpus_supplement/`.",
            "- Ground first via repo_search + Read (not Grep): read the `Source ref` companion AND the subject's ancestor/place companion before any online work; they are more authoritative than the CSV and usually already hold the answer or the exact delta.",
            "- Scope work to the delta only; do not rework already-held material.",
            "- If closing the lead, first promote facts/findings to the appropriate research companion/case file.",
        ]
    )
    return f"{text}\n\n{checklist}"


def collect_update_fields(args: argparse.Namespace) -> dict[str, str]:
    mapping = {
        "priority": "Priority",
        "gen": "Gen",
        "subject": "Subject",
        "lead_source": "Lead/Source",
        "description": "Description",
        "online": "Online",
        "status": "Status",
        "source_ref": "Source ref",
    }
    updates: dict[str, str] = {}
    for attr, field_name in mapping.items():
        value = getattr(args, attr, None)
        if value is not None:
            updates[field_name] = str(value)
    return updates


def apply_text_validation_to_updates(updates: dict[str, str], *, allow_multiline: bool, lead_id: str | None) -> list[WarningMessage]:
    warnings: list[WarningMessage] = []
    for field_name, value in list(updates.items()):
        if field_name in {"Subject", "Lead/Source", "Description", "Status", "Source ref", "Gen"}:
            _, field_warnings = validate_text_value(field_name, value, allow_multiline=allow_multiline, lead_id=lead_id)
            warnings.extend(field_warnings)
    return warnings


def command_get(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    lead_id = normalize_id(args.id)
    row = store.find(lead_id)
    if not row:
        raise SystemExit(f"Lead not found: {lead_id}")
    warnings = validate_row(row, existing=True) if args.warnings else []
    print(format_lead_detail(row, output_format=args.format, warnings=warnings))
    return 0


def command_context(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    lead_id = normalize_id(args.id)
    row = store.find(lead_id)
    if not row:
        raise SystemExit(f"Lead not found: {lead_id}")
    warnings = validate_row(row, existing=True) if args.warnings else []
    print(format_context(row, output_format=args.format, warnings=warnings))
    return 0


def command_list(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    rows = filter_rows(store.rows, args)
    rows = store.sorted_rows(rows)
    if args.limit:
        rows = rows[: args.limit]
    fields = args.fields.split(",") if args.fields else None
    warnings = store.load_warnings if args.warnings else []
    print(format_rows(rows, output_format=args.format, fields=fields, warnings=warnings))
    return 0


def command_priority(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)

    # By default, priority triage is optimized for online work and excludes known physical/offline leads.
    # Use --include-offline to include Online=N; use --include-unknown to include Unk.
    if args.include_offline:
        allowed_online = ONLINE_VALUES
    elif args.include_unknown:
        allowed_online = ONLINE_REACHABLE_DEFAULT | {"Unk"}
    else:
        allowed_online = ONLINE_REACHABLE_DEFAULT

    # Status filter: an explicit --status uses exact match (legacy behaviour); the
    # default keeps every live lead and only drops concluded (stale-done) rows.
    # Exact matching on {"Open","Partial"} silently hid the 42 leads whose Status is
    # a narrative blob, which are exactly the highest-value in-flight ones.
    status_filtered = list(store.rows)
    if args.status:
        wanted = set(args.status)
        status_filtered = [row for row in status_filtered if row.get("Status", "") in wanted]
    else:
        status_filtered = [row for row in status_filtered if not is_stale_done(row.get("Status", ""))]
    if args.min_priority is not None:
        status_filtered = [row for row in status_filtered if parse_priority(row.get("Priority", "")) >= args.min_priority]

    rows = [row for row in status_filtered if row.get("Online", "") in allowed_online]
    rows = store.sorted_rows(rows)[: args.limit]
    fields = args.fields.split(",") if args.fields else ["ID", "Priority", "Gen", "Subject", "Lead/Source", "Online", "Status", "Source ref"]
    warnings = store.load_warnings if args.warnings else []

    # One-line banner: surface high-value offline leads that this online-optimized
    # view hides, so a quick `priority` triage does not silently miss them.
    if not args.include_offline and args.format in {"compact", "markdown"}:
        hidden = store.sorted_rows([row for row in status_filtered if row.get("Online", "") == "N"])
        if hidden:
            top = hidden[:2]
            ids = ", ".join(f"{r.get('ID', '')} (P{r.get('Priority', '')})" for r in top)
            print(
                f"# Note: {len(hidden)} offline lead(s) hidden (Online=N), highest {ids}. "
                "Use --include-offline to show."
            )

    print(format_rows(rows, output_format=args.format, fields=fields, warnings=warnings))
    return 0


def command_search(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    args.query = args.terms
    rows = filter_rows(store.rows, args)
    rows = store.sorted_rows(rows)
    if args.limit:
        rows = rows[: args.limit]
    print(format_rows(rows, output_format=args.format, fields=None, warnings=store.load_warnings if args.warnings else []))
    return 0


def command_next_id(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    print(store.next_id())
    return 0


def command_validate(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    warnings = validate_catalog(store, done_path)
    if args.format == "json":
        print(json.dumps({"warning_count": len(warnings), "warnings": [w.as_dict() for w in warnings]}, ensure_ascii=False, indent=2))
    else:
        if not warnings:
            print("OK: no validation warnings.")
        else:
            for warning in warnings:
                prefix = f"{warning.lead_id}: " if warning.lead_id else ""
                field = f" [{warning.field}]" if warning.field else ""
                print(f"WARNING {warning.code}{field}: {prefix}{warning.message}")
    return 1 if warnings and args.fail_on_warnings else 0


def command_audit(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    threshold = args.status_threshold

    stale = store.sorted_rows([row for row in store.rows if is_stale_done(row.get("Status", ""))])
    long_status = store.sorted_rows([row for row in store.rows if len(row.get("Status", "")) > threshold])

    if args.format == "json":
        result: dict[str, object] = {
            "threshold": threshold,
            "stale_done_count": len(stale),
            "long_status_count": len(long_status),
        }
        if args.verbose:
            result.update(
                {
                    "stale_done": [
                        {"ID": r.get("ID", ""), "Priority": r.get("Priority", ""), "Status": r.get("Status", "")}
                        for r in stale
                    ],
                    "long_status": [
                        {"ID": r.get("ID", ""), "Priority": r.get("Priority", ""), "status_len": len(r.get("Status", "")), "Subject": r.get("Subject", "")}
                        for r in long_status
                    ],
                }
            )
        print(
            json.dumps(
                result,
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    lines = [f"Stale-done — concluded Status still in open CSV (close these): {len(stale)}"]
    lines.append(f"Over-length Status — > {threshold} chars, move narrative to the companion: {len(long_status)}")
    if args.verbose:
        if stale:
            lines.append("")
            lines.append("Stale-done details:")
            for row in stale:
                lines.append(f"  {row.get('ID', ''):6s} P{row.get('Priority', ''):<3} {_truncate(row.get('Status', ''), 90)}")
        if long_status:
            lines.append("")
            lines.append("Over-length Status details:")
            for row in long_status:
                lines.append(f"  {row.get('ID', ''):6s} P{row.get('Priority', ''):<3} len={len(row.get('Status', '')):5d}  {_truncate(row.get('Subject', ''), 50)}")
    elif stale or long_status:
        lines.append("Use --verbose for lead details.")
    print("\n".join(lines))
    return 0


def command_add(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)

    lead_id = normalize_id(args.id) if args.id else store.next_id()
    if store.find(lead_id):
        raise SystemExit(f"Cannot add duplicate lead ID: {lead_id}")

    row = {header: "" for header in store.headers}
    row.update(
        {
            "ID": lead_id,
            "Priority": str(args.priority),
            "Gen": args.gen,
            "Subject": args.subject,
            "Lead/Source": args.lead_source,
            "Description": args.description,
            "Online": args.online,
            "Status": args.status,
            "Source ref": args.source_ref,
        }
    )

    warnings = apply_text_validation_to_updates(row, allow_multiline=args.allow_multiline, lead_id=lead_id)
    warnings.extend(validate_row(row, existing=False))
    rows = store.rows + [row]
    diff = store.write_open(rows, dry_run=args.dry_run, backup=not args.no_backup, verbose=getattr(args, "verbose", False))

    if args.format == "json":
        print(json.dumps({"action": "add", "id": lead_id, "dry_run": args.dry_run, "warnings": [w.as_dict() for w in warnings], "diff": diff}, ensure_ascii=False, indent=2))
    else:
        print(f"Added lead {lead_id}" + (" (dry-run)" if args.dry_run else ""))
        for warning in warnings:
            print(f"WARNING [{warning.code}]: {warning.message}", file=sys.stderr)
        if diff:
            print(diff)
    return 0


def command_update(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    lead_id = normalize_id(args.id)
    row = store.find(lead_id)
    if not row:
        raise SystemExit(f"Lead not found: {lead_id}")

    updates = collect_update_fields(args)
    if args.append_status_note:
        existing_status = row.get("Status", "")
        separator = " — " if existing_status else ""
        updates["Status"] = existing_status + separator + args.append_status_note

    if not updates:
        raise SystemExit("No updates supplied. Use --priority/--status/etc. or --append-status-note.")

    warnings = apply_text_validation_to_updates(updates, allow_multiline=args.allow_multiline, lead_id=lead_id)
    updated_row = dict(row)
    updated_row.update(updates)
    warnings.extend(validate_row(updated_row, existing=False))

    new_rows = [updated_row if existing.get("ID") == lead_id else existing for existing in store.rows]
    diff = store.write_open(new_rows, dry_run=args.dry_run, backup=not args.no_backup, verbose=getattr(args, "verbose", False))

    if args.format == "json":
        print(json.dumps({"action": "update", "id": lead_id, "dry_run": args.dry_run, "updates": updates, "warnings": [w.as_dict() for w in warnings], "diff": diff}, ensure_ascii=False, indent=2))
    else:
        print(f"Updated lead {lead_id}" + (" (dry-run)" if args.dry_run else ""))
        for warning in warnings:
            print(f"WARNING [{warning.code}]: {warning.message}", file=sys.stderr)
        if diff:
            print(diff)
    return 0


def command_close(args: argparse.Namespace) -> int:
    _, open_path, done_path = resolve_paths(args)
    store = LeadStore.load(open_path, done_path)
    lead_id = normalize_id(args.id)
    row = store.find(lead_id)
    if not row:
        raise SystemExit(f"Lead not found in open CSV: {lead_id}")

    close_date = args.date or _dt.date.today().isoformat()
    if not DATE_RE.match(close_date):
        raise SystemExit("--date must be YYYY-MM-DD")

    _, disposition_warnings = validate_text_value("Disposition", args.disposition, allow_multiline=args.allow_multiline, lead_id=lead_id)

    done_headers, done_rows, done_load_warnings = ensure_done_file(done_path, dry_run=args.dry_run)
    if lead_id in {done.get("ID", "") for done in done_rows}:
        raise SystemExit(f"Lead already exists in done CSV: {lead_id}")

    done_row = {header: "" for header in done_headers}
    done_row.update(
        {
            "ID": lead_id,
            "Subject": row.get("Subject", ""),
            "Disposition": args.disposition,
            "Date": close_date,
            "Companion ref": row.get("Source ref", ""),
        }
    )

    # The done CSV intentionally receives only a thin disposition. The full open
    # row is returned to the operator so substantive facts can be promoted before
    # relying on the close-out.
    new_open_rows = [existing for existing in store.rows if existing.get("ID") != lead_id]
    new_done_rows = done_rows + [done_row]

    verbose = getattr(args, "verbose", False)
    open_diff = store.write_open(new_open_rows, dry_run=args.dry_run, backup=not args.no_backup, verbose=verbose)
    done_diff = write_csv_atomic(done_path, done_headers, new_done_rows, dry_run=args.dry_run, backup=not args.no_backup, verbose=verbose)

    warnings = store.load_warnings + done_load_warnings + disposition_warnings

    caution = (
        "Caution: Record any facts and findings from the lead entry into the appropriate research file before relying "
        "on close-out; lead entry content is not retained in done status."
    )

    if args.format == "json":
        print(
            json.dumps(
                {
                    "action": "close",
                    "id": lead_id,
                    "dry_run": args.dry_run,
                    "caution": caution,
                    "done_row": done_row,
                    "original_lead_entry": row,
                    "warnings": [warning.as_dict() for warning in warnings],
                    "open_diff": open_diff,
                    "done_diff": done_diff,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"Closed lead {lead_id}" + (" (dry-run)" if args.dry_run else ""))
        print(caution)
        print("\nOriginal lead entry:")
        print(json.dumps(row, ensure_ascii=False, indent=2))
        for warning in warnings:
            print(f"WARNING [{warning.code}]: {warning.message}", file=sys.stderr)
        if open_diff:
            print("\nOpen CSV proposed diff:\n")
            print(open_diff)
        if done_diff:
            print("\nDone CSV proposed diff:\n")
            print(done_diff)
    return 0


def add_common_path_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo-root", help="Repository root. Defaults to upward search from current directory/script.")
    parser.add_argument("--leads", help=f"Open leads CSV path. Defaults to {DEFAULT_OPEN_REL} under repo root.")
    parser.add_argument("--done", help=f"Done leads CSV path. Defaults to {DEFAULT_DONE_REL} under repo root.")


def add_output_args(parser: argparse.ArgumentParser, *, default: str = "compact") -> None:
    parser.add_argument("--format", choices=["compact", "markdown", "json", "csv"], default=default, help="Output format.")
    parser.add_argument("--warnings", action="store_true", help="Include load/validation warnings in output.")


def add_filter_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--status", action="append", help="Filter by exact Status. Repeatable.")
    parser.add_argument("--gen", action="append", help="Filter by exact Gen. Repeatable.")
    parser.add_argument("--online", action="append", choices=sorted(ONLINE_VALUES), help="Filter by Online value. Repeatable.")
    parser.add_argument("--online-reachable", action="store_true", help="Filter to Online=Y or Part; excludes known physical/offline leads.")
    parser.add_argument("--include-unknown", action="store_true", help="When online-reachable triage is desired, include Online=Unk and still exclude N.")
    parser.add_argument("--min-priority", type=int, help="Minimum priority, inclusive.")
    parser.add_argument("--max-priority", type=int, help="Maximum priority, inclusive.")
    parser.add_argument("--limit", type=int, help="Maximum rows to return.")
    parser.add_argument("--fields", help="Comma-separated output fields.")


def add_write_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--dry-run", action="store_true", help="Show a unified diff instead of writing files.")
    parser.add_argument("--no-backup", action="store_true", help="Do not create timestamped .bak files before writing.")
    parser.add_argument("--allow-multiline", action="store_true", help="Permit line breaks inside CSV fields. Not recommended for manual workflows.")
    parser.add_argument("--verbose", action="store_true", help="With --dry-run, print the full unified diff instead of the compact per-row change summary.")
    parser.add_argument("--format", choices=["compact", "json"], default="compact", help="Output format.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read, triage, validate, and safely update research/future-research/research-leads.csv.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Common AI-safe usage:\n"
            "  python tools/research_leads.py context L-115\n"
            "  python tools/research_leads.py priority\n"
            "  python tools/research_leads.py update L-115 --status Partial --dry-run\n"
            "  python tools/research_leads.py close L-115 --disposition \"Resolved; companion updated.\" --dry-run\n"
        ),
    )
    add_common_path_args(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    p_get = sub.add_parser("get", help="Return one lead by ID.")
    p_get.add_argument("id", help="Lead ID, e.g. L-115 or 115.")
    add_output_args(p_get, default="markdown")
    p_get.set_defaults(func=command_get)

    p_context = sub.add_parser("context", help="Return one lead plus AI pre-pull checklist.")
    p_context.add_argument("id", help="Lead ID, e.g. L-115 or 115.")
    add_output_args(p_context, default="markdown")
    p_context.set_defaults(func=command_context)

    p_list = sub.add_parser("list", help="List/filter open leads, sorted by priority descending.")
    add_filter_args(p_list)
    add_output_args(p_list, default="compact")
    p_list.set_defaults(func=command_list)

    p_priority = sub.add_parser("priority", aliases=["get-priority", "top"], help="Return top priority leads, optimized for online research by default.")
    p_priority.add_argument("--limit", type=int, default=10, help="Number of leads to return. Defaults to 10.")
    p_priority.add_argument("--include-offline", action="store_true", help="Include Online=N physical/offline leads. Default excludes them.")
    p_priority.add_argument("--include-unknown", action="store_true", help="Include Online=Unk along with Y/Part. Default excludes Unk.")
    p_priority.add_argument("--status", action="append", help="Filter status. Repeatable. Defaults to Open and Partial.")
    p_priority.add_argument("--min-priority", type=int, help="Minimum priority, inclusive.")
    p_priority.add_argument("--fields", help="Comma-separated output fields.")
    add_output_args(p_priority, default="compact")
    p_priority.set_defaults(func=command_priority)

    p_search = sub.add_parser("search", help="Search lead text fields.")
    p_search.add_argument("terms", help="Case-insensitive search terms.")
    add_filter_args(p_search)
    add_output_args(p_search, default="compact")
    p_search.set_defaults(func=command_search)

    p_next = sub.add_parser("next-id", help="Print the next unused L-number from open CSV.")
    p_next.set_defaults(func=command_next_id)

    p_validate = sub.add_parser("validate", help="Validate open/done lead CSVs and print warnings.")
    p_validate.add_argument("--format", choices=["compact", "json"], default="compact", help="Output format.")
    p_validate.add_argument("--fail-on-warnings", action="store_true", help="Return exit code 1 if warnings exist. Default always exits 0.")
    p_validate.set_defaults(func=command_validate)

    p_audit = sub.add_parser("audit", help="Health audit: stale-done leads still open + over-length Status fields.")
    p_audit.add_argument("--status-threshold", type=int, default=FIELD_LENGTH_WARN["Status"], help=f"Flag Status longer than this many characters. Default {FIELD_LENGTH_WARN['Status']}.")
    p_audit.add_argument("--format", choices=["compact", "json"], default="compact", help="Output format.")
    p_audit.add_argument("--verbose", action="store_true", help="List affected leads. Default prints summary counts only.")
    p_audit.set_defaults(func=command_audit)

    p_add = sub.add_parser("add", help="Append a new open lead with the next ID unless --id is supplied.")
    p_add.add_argument("--id", help="Optional explicit lead ID. Normally omitted.")
    p_add.add_argument("--priority", type=int, required=True, help="Priority 1-100.")
    p_add.add_argument("--gen", required=True, help="Generation anchor or category.")
    p_add.add_argument("--subject", required=True, help="Subject/person/place/family.")
    p_add.add_argument("--lead-source", required=True, help="Specific source, record series, or repository.")
    p_add.add_argument("--description", required=True, help="One-line why/what-it-establishes description.")
    p_add.add_argument("--online", choices=sorted(ONLINE_VALUES), default="Unk", help="Online availability. Defaults to Unk.")
    p_add.add_argument("--status", default="Open", help="Status. Prefer Open or Partial. Defaults to Open.")
    p_add.add_argument("--source-ref", required=True, help="Repo file where the lead is documented.")
    add_write_args(p_add)
    p_add.set_defaults(func=command_add)

    p_update = sub.add_parser("update", help="Update one lead by ID.")
    p_update.add_argument("id", help="Lead ID, e.g. L-115 or 115.")
    p_update.add_argument("--priority", type=int, help="New priority 1-100.")
    p_update.add_argument("--gen", help="New generation/category.")
    p_update.add_argument("--subject", help="New subject.")
    p_update.add_argument("--lead-source", help="New Lead/Source value.")
    p_update.add_argument("--description", help="New Description value.")
    p_update.add_argument("--online", choices=sorted(ONLINE_VALUES), help="New Online value.")
    p_update.add_argument("--status", help="New Status value. Prefer Open or Partial.")
    p_update.add_argument("--source-ref", help="New Source ref value.")
    p_update.add_argument("--append-status-note", help="Append a brief note to Status. Use sparingly; put narrative in research files.")
    add_write_args(p_update)
    p_update.set_defaults(func=command_update)

    p_close = sub.add_parser("close", help="Move one lead from open CSV to thin done CSV.")
    p_close.add_argument("id", help="Lead ID, e.g. L-115 or 115.")
    p_close.add_argument("--disposition", required=True, help="Brief one-line disposition. Facts/findings belong in research files, not done CSV.")
    p_close.add_argument("--date", help="Close date YYYY-MM-DD. Defaults to today.")
    add_write_args(p_close)
    p_close.set_defaults(func=command_close)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except BrokenPipeError:
        return 1
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
