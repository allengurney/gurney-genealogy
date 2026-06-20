#!/usr/bin/env python3
"""Lossless, staged repository search for gurney-genealogy.

Search broadly using a Git-aware inventory and an exact ripgrep ledger, then
rank and package structured sections so an AI can read results progressively.
SQLite FTS5 accelerates retrieval but is never the sole completeness backstop.
"""

from __future__ import annotations

import argparse
import base64
import csv
import datetime as dt
import fnmatch
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import textwrap
import unicodedata
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Sequence

try:
    from rapidfuzz import fuzz, process as fuzz_process
except ImportError:  # Optional graceful fallback; requirements pins RapidFuzz.
    fuzz = None
    fuzz_process = None


CONFIG_REL = Path("tools/repo_search_config.json")
VARIANTS_REL = Path("data/search-variants.json")
ANCESTOR_INDEX_REL = Path("data/indexes/ancestor-ids.csv")
PLACE_INDEX_REL = Path("data/indexes/place-ids.csv")
SOURCE_INDEX_REL = Path("data/indexes/source-ids.csv")
LEADS_REL = Path("research/future-research/research-leads.csv")
DONE_LEADS_REL = Path("research/future-research/research-leads-done.csv")
INDEX_SCHEMA_VERSION = 1
SEARCH_PACKAGE_VERSION = 2

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
PAGE_RE = re.compile(r"^##\s+p\.\s*(\d+)(?:\s+\(#(\d+)\))?", re.I)
SCAN_RE = re.compile(r"^##\s+scan\s+#(\d+)", re.I)
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)$")
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\]")
HTML_NOTE_DEF_RE = re.compile(r'<li\s+id=["\'](n[^"\']+)["\'][^>]*>(.*?)</li>', re.I | re.S)
HTML_NOTE_REF_RE = re.compile(r'href=["\']#(n[^"\']+)["\']', re.I)
SOURCE_ID_RE = re.compile(r"(?:Source ID|Source IDs):\s*`?([a-z0-9][a-z0-9._-]*)", re.I)
GEN_RE = re.compile(r"^G~?(\d+)\+?$", re.I)
LEAD_RE = re.compile(r"^L-\d+$", re.I)
WORD_RE = re.compile(r"[\w'-]+", re.UNICODE)


@dataclass
class FileRecord:
    path: str
    layer: str
    object_type: str
    object_id: str = ""
    size: int = 0
    mtime_ns: int = 0


@dataclass
class Footnote:
    key: str
    body: str
    start_line: int
    end_line: int
    source_ids: list[str] = field(default_factory=list)


@dataclass
class Section:
    path: str
    heading: str
    heading_path: str
    start_line: int
    end_line: int
    body: str
    layer: str
    object_type: str
    object_id: str = ""
    page_marker: str = ""
    footnote_keys: list[str] = field(default_factory=list)
    footnotes: list[Footnote] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)

    @property
    def key(self) -> str:
        return f"{self.path}:{self.start_line}:{self.end_line}"


@dataclass
class ExactMatch:
    path: str
    line_number: int
    line: str
    terms: list[str]


@dataclass
class SearchTermSpec:
    term: str
    match_mode: str = "substring"
    source_paths: list[str] = field(default_factory=list)
    origin: str = "explicit"
    family: str = ""
    profile: str = ""
    category: str = ""
    collision_warning: str = ""


@dataclass
class SearchResult:
    result_id: int
    section: Section
    score: float
    match_kinds: list[str]
    matched_terms: list[str]
    exact_lines: list[int]
    bucket: str
    excerpt: str
    warnings: list[str] = field(default_factory=list)


@dataclass
class Entity:
    kind: str
    id: str
    label: str
    generation: str = ""
    dates: str = ""
    paths: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    linked_ids: list[str] = field(default_factory=list)


def find_repo_root(start: Path | None = None) -> Path:
    candidates = [start or Path.cwd(), Path(__file__).resolve().parent.parent]
    for candidate in candidates:
        candidate = candidate.resolve()
        for path in [candidate, *candidate.parents]:
            if (path / "AGENTS.md").exists() and (path / "data").is_dir():
                return path
    raise SystemExit("Could not locate repository root.")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def load_config(repo_root: Path) -> dict[str, Any]:
    config = load_json(repo_root / CONFIG_REL)
    cache_override = os.environ.get("GURNEY_REPO_SEARCH_CACHE")
    raw_root = cache_override or config.get("cacheRoot", "%USERPROFILE%/GitDirs/gurney-genealogy-search-cache")
    expanded = os.path.expandvars(raw_root)
    if "%" in expanded:
        expanded = str(Path.home() / "GitDirs/gurney-genealogy-search-cache")
    config["cacheRootResolved"] = str(Path(expanded).resolve())
    return config


def normalize_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("\u00ad", "")
    value = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"[ \t]+", " ", value)
    return value.casefold()


def slugify(value: str, limit: int = 54) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", normalize_text(value)).strip("-")
    return (slug[:limit].rstrip("-") or "search")


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def path_excluded(path: str, patterns: Sequence[str]) -> bool:
    path = path.replace("\\", "/")
    for pattern in patterns:
        pattern = pattern.replace("\\", "/")
        prefix = pattern[:-3] if pattern.endswith("/**") else ""
        if (prefix and (path == prefix.rstrip("/") or path.startswith(prefix))) or fnmatch.fnmatch(path, pattern):
            return True
    return False


def classify_path(path: str) -> tuple[str, str]:
    p = path.replace("\\", "/")
    if "initial foundation work" in p.casefold():
        return "historical", "superseded-draft"
    if p.startswith("fact-sheets/"):
        return "publication", "fact-sheet"
    if p.startswith("research/case-files/"):
        return "publication", "case-file"
    if p.startswith("research/people/"):
        return "research", "person-research"
    if p.startswith("research/places/"):
        return "research", "place-research"
    if p.startswith("research/topics/"):
        return "research", "topic-research"
    if p.startswith("research/future-research/"):
        return "leads", "future-research"
    if p.startswith("sources/corpus_supplement/"):
        return "sources", "corpus-supplement"
    if p.startswith("sources/corpus/"):
        return "sources", "corpus"
    if p.startswith("sources/validations/"):
        return "sources", "validation"
    if p.startswith("sources/media/"):
        return "sources", "media-sidecar"
    if p.startswith("sources/intake/"):
        return "historical", "intake"
    if p.startswith("data/"):
        return "data", "canonical-data"
    if p.startswith("tools/"):
        return "tools", "tooling"
    return "other", "text"


def git_inventory(repo_root: Path, config: dict[str, Any]) -> list[FileRecord]:
    command = ["git", "ls-files", "-co", "--exclude-standard", "-z"]
    result = subprocess.run(command, cwd=repo_root, capture_output=True, check=True)
    extensions = {ext.casefold() for ext in config["textExtensions"]}
    excluded = config["excludedPaths"]
    records: list[FileRecord] = []
    for raw in result.stdout.decode("utf-8", errors="replace").split("\0"):
        if not raw:
            continue
        path = raw.replace("\\", "/")
        if path_excluded(path, excluded):
            continue
        if Path(path).suffix.casefold() not in extensions:
            continue
        if path in {str(LEADS_REL).replace("\\", "/"), str(DONE_LEADS_REL).replace("\\", "/")}:
            continue
        full = repo_root / path
        if not full.is_file():
            continue
        stat = full.stat()
        layer, object_type = classify_path(path)
        records.append(FileRecord(path=path, layer=layer, object_type=object_type, size=stat.st_size, mtime_ns=stat.st_mtime_ns))
    return sorted(records, key=lambda item: item.path.casefold())


def extract_source_ids(text: str) -> list[str]:
    found = SOURCE_ID_RE.findall(text)
    code_ids = re.findall(r"`([a-z0-9][a-z0-9._-]{3,})`", text)
    return sorted(set(found + [value for value in code_ids if "-" in value]))


def parse_footnotes(lines: list[str]) -> dict[str, Footnote]:
    notes: dict[str, Footnote] = {}
    i = 0
    while i < len(lines):
        match = FOOTNOTE_DEF_RE.match(lines[i])
        if not match:
            i += 1
            continue
        key, first = match.groups()
        body_lines = [first]
        start = i + 1
        i += 1
        while i < len(lines):
            if FOOTNOTE_DEF_RE.match(lines[i]) or HEADING_RE.match(lines[i]):
                break
            if lines[i].startswith(("    ", "\t")) or not lines[i].strip():
                body_lines.append(lines[i].strip())
                i += 1
                continue
            break
        body = "\n".join(body_lines).strip()
        notes[key] = Footnote(key=key, body=body, start_line=start, end_line=i, source_ids=extract_source_ids(body))
    joined = "\n".join(lines)
    for match in HTML_NOTE_DEF_RE.finditer(joined):
        key, body = match.groups()
        clean = re.sub(r"<[^>]+>", " ", body)
        clean = re.sub(r"\s+", " ", clean).strip()
        line_no = joined[: match.start()].count("\n") + 1
        notes[key] = Footnote(key=key, body=clean, start_line=line_no, end_line=line_no, source_ids=extract_source_ids(clean))
    return notes


def parse_markdown(record: FileRecord, text: str) -> list[Section]:
    lines = text.splitlines()
    notes = parse_footnotes(lines)
    boundaries: list[tuple[int, int, str, str]] = []
    heading_stack: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        heading = match.group(2).strip("# ").strip()
        heading_stack = [(lvl, value) for lvl, value in heading_stack if lvl < level]
        heading_stack.append((level, heading))
        boundaries.append((i, level, heading, " > ".join(value for _, value in heading_stack)))
    if not boundaries:
        boundaries = [(0, 1, Path(record.path).name, Path(record.path).name)]
    elif boundaries[0][0] > 0:
        boundaries.insert(0, (0, 1, Path(record.path).name, Path(record.path).name))

    sections: list[Section] = []
    for idx, (start, _level, heading, heading_path) in enumerate(boundaries):
        end = boundaries[idx + 1][0] if idx + 1 < len(boundaries) else len(lines)
        body_lines = lines[start:end]
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        refs = set(FOOTNOTE_REF_RE.findall(body))
        refs.update(HTML_NOTE_REF_RE.findall(body))
        attached = [notes[key] for key in sorted(refs) if key in notes]
        page_match = PAGE_RE.match(lines[start]) if start < len(lines) else None
        scan_match = SCAN_RE.match(lines[start]) if start < len(lines) else None
        page_marker = f"p. {page_match.group(1)}" if page_match else (f"scan #{scan_match.group(1)}" if scan_match else "")
        sections.append(
            Section(
                path=record.path,
                heading=heading,
                heading_path=heading_path,
                start_line=start + 1,
                end_line=end,
                body=body,
                layer=record.layer,
                object_type=record.object_type,
                object_id=record.object_id,
                page_marker=page_marker,
                footnote_keys=sorted(refs),
                footnotes=attached,
                source_ids=extract_source_ids(body + "\n" + "\n".join(note.body for note in attached)),
            )
        )
    return sections


def parse_json_file(record: FileRecord, text: str) -> list[Section]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return parse_markdown(record, text)
    sections: list[Section] = []
    if record.path == "data/sources.json" and isinstance(data, dict):
        items = data.get("sources", {}).items()
    elif record.path == "data/ancestors.json" and isinstance(data, list):
        items = ((item.get("recordId", f"record-{i}"), item) for i, item in enumerate(data))
    elif record.path in {"data/places.json", "data/places_detail.json"} and isinstance(data, list):
        items = ((item.get("placeId", f"place-{i}"), item) for i, item in enumerate(data))
    elif isinstance(data, dict):
        items = data.items()
    else:
        items = ((f"item-{i}", item) for i, item in enumerate(data if isinstance(data, list) else [data]))
    for i, (key, value) in enumerate(items, start=1):
        body = json.dumps(value, ensure_ascii=False, indent=2)
        sections.append(
            Section(
                path=record.path,
                heading=str(key),
                heading_path=str(key),
                start_line=i,
                end_line=i,
                body=body,
                layer=record.layer,
                object_type=record.object_type,
                object_id=str(key),
                source_ids=[str(key)] if record.path == "data/sources.json" else extract_source_ids(body),
            )
        )
    return sections


def parse_csv_file(record: FileRecord, text: str) -> list[Section]:
    lines = text.splitlines()
    if not lines:
        return []
    sections: list[Section] = []
    try:
        rows = list(csv.DictReader(lines))
    except csv.Error:
        rows = []
    if rows and len(rows) <= 5000:
        for i, row in enumerate(rows, start=2):
            label = next((row.get(key, "") for key in ("ID", "sourceId", "recordId", "placeId", "id", "name") if row.get(key)), f"row-{i}")
            body = json.dumps(row, ensure_ascii=False, indent=2)
            sections.append(
                Section(
                    path=record.path,
                    heading=label,
                    heading_path=label,
                    start_line=i,
                    end_line=i,
                    body=body,
                    layer=record.layer,
                    object_type=record.object_type,
                    object_id=label,
                    source_ids=extract_source_ids(body),
                )
            )
        return sections
    return parse_markdown(record, text)


def parse_file(repo_root: Path, record: FileRecord) -> list[Section]:
    path = repo_root / record.path
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    suffix = path.suffix.casefold()
    if suffix == ".json":
        return parse_json_file(record, text)
    if suffix == ".csv":
        return parse_csv_file(record, text)
    return parse_markdown(record, text)


class SearchIndex:
    def __init__(self, db_path: Path):
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.trigram_available = False
        self._create_schema()

    def close(self) -> None:
        self.conn.close()

    def _create_schema(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS files (
              path TEXT PRIMARY KEY, layer TEXT, object_type TEXT, object_id TEXT,
              size INTEGER, mtime_ns INTEGER, content_hash TEXT, indexed_at TEXT
            );
            CREATE TABLE IF NOT EXISTS sections (
              id INTEGER PRIMARY KEY, path TEXT, heading TEXT, heading_path TEXT,
              start_line INTEGER, end_line INTEGER, body TEXT, normalized_body TEXT,
              layer TEXT, object_type TEXT, object_id TEXT, page_marker TEXT,
              footnotes_json TEXT, source_ids_json TEXT
            );
            CREATE INDEX IF NOT EXISTS sections_path_idx ON sections(path);
            CREATE VIRTUAL TABLE IF NOT EXISTS sections_fts USING fts5(
              section_id UNINDEXED, path, heading, body,
              tokenize='unicode61 remove_diacritics 2'
            );
            """
        )
        try:
            self.conn.execute(
                "CREATE VIRTUAL TABLE IF NOT EXISTS sections_tri USING fts5("
                "section_id UNINDEXED, path, heading, body, tokenize='trigram case_sensitive 0')"
            )
            self.trigram_available = True
        except sqlite3.OperationalError:
            self.trigram_available = False
        self.conn.execute(
            "INSERT OR REPLACE INTO metadata(key,value) VALUES('schema_version',?)",
            (str(INDEX_SCHEMA_VERSION),),
        )
        self.conn.commit()

    def rebuild(self) -> None:
        self.conn.execute("DELETE FROM sections_fts")
        if self.trigram_available:
            self.conn.execute("DELETE FROM sections_tri")
        self.conn.execute("DELETE FROM sections")
        self.conn.execute("DELETE FROM files")
        self.conn.commit()

    def refresh(self, repo_root: Path, inventory: list[FileRecord], force: bool = False) -> dict[str, int]:
        existing = {row["path"]: row for row in self.conn.execute("SELECT * FROM files")}
        current = {record.path: record for record in inventory}
        removed = sorted(set(existing) - set(current))
        changed: list[FileRecord] = []
        unchanged = 0
        for record in inventory:
            old = existing.get(record.path)
            if force or old is None or old["size"] != record.size or old["mtime_ns"] != record.mtime_ns:
                changed.append(record)
            else:
                unchanged += 1
        with self.conn:
            for path in removed:
                self._delete_file(path)
            for record in changed:
                self._delete_file(record.path)
                sections = parse_file(repo_root, record)
                for section in sections:
                    cursor = self.conn.execute(
                        """
                        INSERT INTO sections(
                          path,heading,heading_path,start_line,end_line,body,normalized_body,
                          layer,object_type,object_id,page_marker,footnotes_json,source_ids_json
                        ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
                        """,
                        (
                            section.path,
                            section.heading,
                            section.heading_path,
                            section.start_line,
                            section.end_line,
                            section.body,
                            normalize_text(section.body),
                            section.layer,
                            section.object_type,
                            section.object_id,
                            section.page_marker,
                            json.dumps([asdict(note) for note in section.footnotes], ensure_ascii=False),
                            json.dumps(section.source_ids, ensure_ascii=False),
                        ),
                    )
                    section_id = cursor.lastrowid
                    values = (section_id, section.path, section.heading, section.body)
                    self.conn.execute("INSERT INTO sections_fts(section_id,path,heading,body) VALUES(?,?,?,?)", values)
                    if self.trigram_available:
                        self.conn.execute("INSERT INTO sections_tri(section_id,path,heading,body) VALUES(?,?,?,?)", values)
                self.conn.execute(
                    "INSERT INTO files(path,layer,object_type,object_id,size,mtime_ns,content_hash,indexed_at) VALUES(?,?,?,?,?,?,?,?)",
                    (
                        record.path,
                        record.layer,
                        record.object_type,
                        record.object_id,
                        record.size,
                        record.mtime_ns,
                        hash_file(repo_root / record.path),
                        dt.datetime.now(dt.timezone.utc).isoformat(),
                    ),
                )
        return {"changed": len(changed), "removed": len(removed), "unchanged": unchanged, "files": len(inventory)}

    def _delete_file(self, path: str) -> None:
        ids = [row[0] for row in self.conn.execute("SELECT id FROM sections WHERE path=?", (path,))]
        for section_id in ids:
            self.conn.execute("DELETE FROM sections_fts WHERE section_id=?", (section_id,))
            if self.trigram_available:
                self.conn.execute("DELETE FROM sections_tri WHERE section_id=?", (section_id,))
        self.conn.execute("DELETE FROM sections WHERE path=?", (path,))
        self.conn.execute("DELETE FROM files WHERE path=?", (path,))

    def stale(self, inventory: list[FileRecord]) -> list[str]:
        existing = {row["path"]: row for row in self.conn.execute("SELECT path,size,mtime_ns FROM files")}
        current = {record.path: record for record in inventory}
        stale = sorted(set(existing) ^ set(current))
        for path, record in current.items():
            old = existing.get(path)
            if old and (old["size"] != record.size or old["mtime_ns"] != record.mtime_ns):
                stale.append(path)
        return sorted(set(stale))

    def section_from_row(self, row: sqlite3.Row) -> Section:
        return Section(
            path=row["path"],
            heading=row["heading"],
            heading_path=row["heading_path"],
            start_line=row["start_line"],
            end_line=row["end_line"],
            body=row["body"],
            layer=row["layer"],
            object_type=row["object_type"],
            object_id=row["object_id"] or "",
            page_marker=row["page_marker"] or "",
            footnotes=[Footnote(**item) for item in json.loads(row["footnotes_json"] or "[]")],
            footnote_keys=[item["key"] for item in json.loads(row["footnotes_json"] or "[]")],
            source_ids=json.loads(row["source_ids_json"] or "[]"),
        )

    def get_section(self, section_id: int) -> Section:
        row = self.conn.execute("SELECT * FROM sections WHERE id=?", (section_id,)).fetchone()
        if row is None:
            raise KeyError(section_id)
        return self.section_from_row(row)

    def sections_for_path(self, path: str) -> list[tuple[int, Section]]:
        return [(row["id"], self.section_from_row(row)) for row in self.conn.execute("SELECT * FROM sections WHERE path=? ORDER BY start_line", (path,))]

    def all_sections(self) -> Iterable[tuple[int, Section]]:
        for row in self.conn.execute("SELECT * FROM sections"):
            yield row["id"], self.section_from_row(row)

    def lexical_search(self, terms: list[str], broad: bool = False) -> dict[int, float]:
        scores: dict[int, float] = {}
        query_parts = []
        for term in terms:
            words = WORD_RE.findall(term)
            if not words:
                continue
            query_parts.append('"' + " ".join(word.replace('"', '""') for word in words) + '"')
        if query_parts:
            query = " OR ".join(query_parts)
            try:
                for row in self.conn.execute(
                    "SELECT section_id,bm25(sections_fts,2.0,4.0,1.0) AS rank FROM sections_fts WHERE sections_fts MATCH ?",
                    (query,),
                ):
                    scores[int(row["section_id"])] = max(scores.get(int(row["section_id"]), 0.0), 25.0 + max(0.0, -float(row["rank"])))
            except sqlite3.OperationalError:
                pass
        if broad and self.trigram_available:
            for term in terms:
                if len(term.strip()) < 3:
                    continue
                try:
                    for row in self.conn.execute(
                        "SELECT section_id,bm25(sections_tri) AS rank FROM sections_tri WHERE sections_tri MATCH ?",
                        ('"' + term.replace('"', '""') + '"',),
                    ):
                        sid = int(row["section_id"])
                        scores[sid] = max(scores.get(sid, 0.0), 12.0 + max(0.0, -float(row["rank"])))
                except sqlite3.OperationalError:
                    continue
        return scores


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def fuzzy_candidates(query: str, choices: dict[str, str], limit: int = 8) -> list[tuple[str, str, float]]:
    if fuzz_process is None:
        query_norm = normalize_text(query)
        matches = [(key, label, 100.0 if normalize_text(label) == query_norm else 0.0) for key, label in choices.items()]
        return sorted(matches, key=lambda item: item[2], reverse=True)[:limit]
    labels = list(choices.values())
    lookup = {label: key for key, label in choices.items()}
    return [(lookup[label], label, float(score)) for label, score, _ in fuzz_process.extract(query, labels, scorer=fuzz.WRatio, limit=limit)]


def resolve_ancestor(repo_root: Path, selector: str, config: dict[str, Any]) -> Entity:
    rows = read_csv_rows(repo_root / ANCESTOR_INDEX_REL)
    ancestors = [row for row in rows if row.get("type") == "ancestor"]
    selector_norm = normalize_text(selector)
    gen_match = GEN_RE.match(selector.strip())
    matches: list[dict[str, str]] = []
    if gen_match:
        wanted = f"G{int(gen_match.group(1))}"
        matches = [row for row in ancestors if row.get("gen", "").upper().replace("~", "") == wanted]
    else:
        matches = [
            row
            for row in ancestors
            if normalize_text(row.get("recordId", "")) == selector_norm or normalize_text(row.get("name", "")) == selector_norm
        ]
    if len(matches) > 1:
        choices = "\n".join(f"{row.get('gen',''):4} {row.get('name','')} ({row.get('dates','')})" for row in matches)
        raise SystemExit(
            f"Ambiguous ancestor: {selector}\n\n{choices}\n\n"
            "Requery with --ancestor G<number>. For unrestricted textual search, omit --ancestor and put the name in --terms."
        )
    if not matches:
        candidates = fuzzy_candidates(selector, {row.get("recordId", ""): f"{row.get('gen','')} {row.get('name','')} {row.get('dates','')}" for row in ancestors})
        shown = "\n".join(f"  {label} [{score:.0f}%]" for _key, label, score in candidates[:5])
        raise SystemExit(f"Ancestor not resolved: {selector}\nClosest candidates:\n{shown}")
    row = matches[0]
    paths = [value for value in (row.get("factSheetPath", ""), row.get("researchPath", "")) if value]
    generation = row.get("gen", "")
    gen_match = GEN_RE.match(generation)
    if gen_match:
        prefix = f"g{int(gen_match.group(1)):02d}-"
        paths.extend(
            path.relative_to(repo_root).as_posix()
            for root in (repo_root / "fact-sheets", repo_root / "research/people")
            if root.exists()
            for path in root.glob(f"{prefix}*")
            if path.is_file() and path.suffix.casefold() == ".md"
        )
    for publication in config.get("specialPublications", []):
        if publication.get("ancestor", "").upper() == row.get("gen", "").upper():
            paths.append(publication["path"])
    return Entity(
        kind="ancestor",
        id=row.get("recordId", ""),
        label=row.get("name", ""),
        generation=row.get("gen", ""),
        dates=row.get("dates", ""),
        paths=sorted(set(paths)),
        aliases=[row.get("name", "")],
    )


def resolve_place(repo_root: Path, selector: str) -> Entity:
    rows = read_csv_rows(repo_root / PLACE_INDEX_REL)
    selector_norm = normalize_text(selector)
    matches = []
    preferred = []
    for row in rows:
        values = [row.get("placeId", ""), row.get("name", ""), row.get("filename", "")]
        values.extend(row.get("aliases", "").split(";"))
        if any(normalize_text(value) == selector_norm for value in values if value):
            matches.append(row)
        primary_name = row.get("name", "").split(",", 1)[0]
        if normalize_text(primary_name) == selector_norm:
            preferred.append(row)
    if len(preferred) == 1:
        matches = preferred
    if len(matches) > 1:
        raise SystemExit("Ambiguous place:\n" + "\n".join(f"{row['placeId']}  {row['name']}" for row in matches))
    if not matches:
        candidates = fuzzy_candidates(selector, {row.get("placeId", ""): row.get("name", "") for row in rows})
        shown = "\n".join(f"  {key}: {label} [{score:.0f}%]" for key, label, score in candidates[:5])
        raise SystemExit(f"Place not resolved: {selector}\nClosest candidates:\n{shown}")
    row = matches[0]
    filename = row.get("filename", "")
    path = f"research/places/{filename}" if filename else ""
    return Entity(
        kind="place",
        id=row.get("placeId", ""),
        label=row.get("name", ""),
        paths=[path] if path else [],
        aliases=[item for item in row.get("aliases", "").split(";") if item],
        linked_ids=[item for item in row.get("linkedRecordIds", "").split(";") if item],
    )


def resolve_source(repo_root: Path, selector: str) -> Entity:
    rows = read_csv_rows(repo_root / SOURCE_INDEX_REL)
    selector_norm = normalize_text(selector)
    matches = []
    for row in rows:
        values = [row.get("sourceId", ""), row.get("shortTitle", ""), row.get("corpusPath", ""), row.get("validationPath", "")]
        if any(normalize_text(value) == selector_norm for value in values if value):
            matches.append(row)
    if len(matches) > 1:
        raise SystemExit("Ambiguous source:\n" + "\n".join(f"{row['sourceId']}  {row['shortTitle']}" for row in matches))
    if not matches:
        candidates = fuzzy_candidates(selector, {row.get("sourceId", ""): row.get("shortTitle", "") for row in rows})
        shown = "\n".join(f"  {key}: {label} [{score:.0f}%]" for key, label, score in candidates[:5])
        raise SystemExit(f"Source not resolved: {selector}\nClosest candidates:\n{shown}")
    row = matches[0]
    paths = ["data/sources.json"]
    paths.extend(value for value in (row.get("corpusPath", ""), row.get("validationPath", "")) if value)
    media = row.get("mediaPath", "")
    if media:
        paths.append(media)
    return Entity(kind="source", id=row.get("sourceId", ""), label=row.get("shortTitle", ""), paths=sorted(set(paths)))


def load_variants(repo_root: Path) -> dict[str, Any]:
    return load_json(repo_root / VARIANTS_REL)


def generation_number(entity: Entity | None) -> int | None:
    if not entity or entity.kind != "ancestor":
        return None
    match = GEN_RE.match(entity.generation)
    return int(match.group(1)) if match else None


def select_name_variant_families(
    data: dict[str, Any],
    selection: str,
    entity: Entity | None = None,
) -> tuple[list[dict[str, Any]], str, bool]:
    families = data.get("nameVariantFamilies", [])
    by_id = {normalize_text(group.get("id", "")): group for group in families}
    choice = normalize_text(selection or "auto")
    inferred = False
    if choice == "auto":
        generation = generation_number(entity)
        if generation is None:
            return [], "none", False
        matches = [
            group
            for group in families
            if int(group.get("generationRange", {}).get("minimum", 0))
            <= generation
            <= int(group.get("generationRange", {}).get("maximum", -1))
        ]
        if len(matches) != 1:
            raise SystemExit(f"No unique name-variant family covers {entity.generation}.")
        return matches, normalize_text(matches[0].get("id", "")), True
    if choice == "none":
        return [], "none", False
    if choice == "all":
        return families, "all", False
    if choice not in by_id:
        raise SystemExit(f"Unknown name-variant family: {selection}")
    return [by_id[choice]], choice, inferred


def term_pattern(term: str, match_mode: str) -> str:
    escaped = re.escape(term)
    if match_mode == "phrase":
        escaped = escaped.replace(r"\ ", r"\s+")
    if match_mode in {"whole-token", "phrase"}:
        return rf"(?<![\p{{L}}\p{{N}}_]){escaped}(?![\p{{L}}\p{{N}}_])"
    return escaped


def replace_name_form(source: str, old: str, new: str) -> str:
    pattern = re.compile(
        rf"(?<![\w]){re.escape(old)}(?![\w])",
        flags=re.I,
    )
    return pattern.sub(new, source, count=1)


def _append_term_spec(specs: list[SearchTermSpec], spec: SearchTermSpec) -> bool:
    key = (normalize_text(spec.term), tuple(sorted(spec.source_paths)))
    for existing in specs:
        existing_key = (normalize_text(existing.term), tuple(sorted(existing.source_paths)))
        if existing_key != key:
            continue
        if existing.match_mode == "substring" and spec.match_mode != "substring":
            existing.match_mode = spec.match_mode
        if spec.collision_warning and not existing.collision_warning:
            existing.collision_warning = spec.collision_warning
        return False
    specs.append(spec)
    return True


def expand_variants(
    repo_root: Path,
    terms: list[str],
    profile: str,
    name_variants: str = "auto",
    entity: Entity | None = None,
) -> tuple[list[SearchTermSpec], list[dict[str, Any]], dict[str, Any]]:
    data = load_variants(repo_root)
    base_terms = list(terms)
    if entity and entity.label and not base_terms:
        base_terms.append(entity.label)
    if profile == "none":
        specs = [SearchTermSpec(term=term) for term in base_terms if term]
        return specs, [], {"requested": name_variants, "selected": "none", "inferred": False, "labels": []}

    families, selected, inferred = select_name_variant_families(data, name_variants, entity)
    specs: list[SearchTermSpec] = []
    expansions: list[dict[str, Any]] = []
    family_forms: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for family in families:
        variants = list(family.get("conservative", []))
        if profile == "broad":
            variants.extend(family.get("broadAdditions", []))
        all_forms = list(family.get("conservative", [])) + list(family.get("broadAdditions", []))
        all_forms.sort(key=lambda item: len(item.get("term", "")), reverse=True)
        family_forms.append((family, {"selected": variants, "recognition": all_forms}))

    for source_term in base_terms:
        recognized: list[tuple[dict[str, Any], dict[str, Any]]] = []
        for family, forms in family_forms:
            matched_form = next(
                (
                    form
                    for form in forms["recognition"]
                    if re.search(
                        rf"(?<![\w]){re.escape(form.get('term', ''))}(?![\w])",
                        source_term,
                        flags=re.I,
                    )
                ),
                None,
            )
            if matched_form:
                recognized.append((family, matched_form))
        _append_term_spec(
            specs,
            SearchTermSpec(
                term=source_term,
                match_mode="whole-token" if recognized else "substring",
            ),
        )
        for family, matched_form in recognized:
            selected_variants = next(forms["selected"] for candidate, forms in family_forms if candidate is family)
            conservative_terms = {normalize_text(item.get("term", "")) for item in family.get("conservative", [])}
            for variant in selected_variants:
                variant_term = variant.get("term", "")
                expanded_term = replace_name_form(source_term, matched_form.get("term", ""), variant_term)
                variant_profile = "conservative" if normalize_text(variant_term) in conservative_terms else "broad"
                spec = SearchTermSpec(
                    term=expanded_term,
                    match_mode=variant.get("matchMode", "whole-token"),
                    origin="name-variant",
                    family=family.get("id", ""),
                    profile=variant_profile,
                    category=variant.get("category", ""),
                    collision_warning=variant.get("collisionWarning", ""),
                )
                if _append_term_spec(specs, spec):
                    expansions.append(
                        {
                            "source": source_term,
                            "term": expanded_term,
                            "family": family.get("id", ""),
                            "category": spec.category,
                            "profile": variant_profile,
                            "matchMode": spec.match_mode,
                            "collisionWarning": spec.collision_warning,
                        }
                    )

    # Source-specific OCR sets remain independent of surname-family selection.
    for group in data.get("variantSets", []):
        if group.get("kind") != "source-specific-ocr":
            continue
        canonical = group.get("canonical", "")
        matching_terms = [term for term in base_terms if re.search(rf"(?<![\w]){re.escape(canonical)}(?![\w])", term, flags=re.I)]
        for variant in group.get("variants", []):
            variant_profile = variant.get("profile", "broad")
            if profile == "conservative" and variant_profile != "conservative":
                continue
            variant_term = variant.get("term", "")
            for source_term in matching_terms:
                expanded_term = replace_name_form(source_term, canonical, variant_term)
                spec = SearchTermSpec(
                    term=expanded_term,
                    match_mode=variant.get("matchMode", "whole-token"),
                    source_paths=list(group.get("sourcePaths", [])),
                    origin="source-specific-ocr",
                    profile=variant_profile,
                    category=variant.get("category", ""),
                )
                if expanded_term and _append_term_spec(specs, spec):
                    expansions.append(
                        {
                            "source": source_term,
                            "term": expanded_term,
                            "family": group.get("id", ""),
                            "category": variant.get("category", ""),
                            "profile": variant_profile,
                            "matchMode": spec.match_mode,
                            "sourcePaths": ";".join(spec.source_paths),
                        }
                    )
    selection = {
        "requested": name_variants,
        "selected": selected,
        "inferred": inferred,
        "labels": [family.get("label", family.get("id", "")) for family in families],
    }
    return specs, expansions, selection


_RG_CACHE: str | None = None
_RG_SEARCHED = False


def find_ripgrep() -> str | None:
    """Locate the ripgrep executable robustly, without relying on PATH alone.

    Resolution order:
    1. ``GURNEY_REPO_SEARCH_RG`` / ``RIPGREP_PATH`` env override (explicit path).
    2. PATH (``shutil.which``) for ``rg`` / ``rg.exe``.
    3. Common Windows install locations (winget shim + package dir, scoop,
       chocolatey, Program Files) so a freshly installed rg works without a
       shell restart or a PATH edit.
    4. Common Unix locations.

    The directory of the resolved binary is prepended to ``PATH`` so child
    processes and later calls in the same run resolve it identically. Result is
    cached for the process. Returns the path, or ``None`` if not found.
    """
    global _RG_CACHE, _RG_SEARCHED
    if _RG_SEARCHED:
        return _RG_CACHE

    candidates: list[Path] = []
    for env_var in ("GURNEY_REPO_SEARCH_RG", "RIPGREP_PATH"):
        override = os.environ.get(env_var)
        if override:
            candidates.append(Path(override))
    for name in ("rg", "rg.exe"):
        found = shutil.which(name)
        if found:
            candidates.append(Path(found))

    if os.name == "nt":
        local = os.environ.get("LOCALAPPDATA", "")
        program_files = os.environ.get("ProgramFiles", r"C:\Program Files")
        program_data = os.environ.get("ProgramData", r"C:\ProgramData")
        user_profile = os.environ.get("USERPROFILE", "")
        glob_roots: list[tuple[Path, str]] = []
        if local:
            candidates.append(Path(local) / "Microsoft" / "WinGet" / "Links" / "rg.exe")
            glob_roots.append((Path(local) / "Microsoft" / "WinGet" / "Packages", "*ripgrep*/**/rg.exe"))
        if user_profile:
            candidates.append(Path(user_profile) / "scoop" / "shims" / "rg.exe")
        if program_data:
            candidates.append(Path(program_data) / "chocolatey" / "bin" / "rg.exe")
        if program_files:
            glob_roots.append((Path(program_files), "ripgrep*/**/rg.exe"))
        for root, pattern in glob_roots:
            if root.is_dir():
                try:
                    candidates.extend(sorted(root.glob(pattern), reverse=True))
                except OSError:
                    pass
    else:
        for path in ("/usr/bin/rg", "/usr/local/bin/rg", "/opt/homebrew/bin/rg", "/snap/bin/rg"):
            candidates.append(Path(path))

    resolved: str | None = None
    for candidate in candidates:
        try:
            if candidate.is_file():
                resolved = str(candidate)
                break
        except OSError:
            continue

    if resolved:
        rg_dir = str(Path(resolved).parent)
        if rg_dir and rg_dir not in os.environ.get("PATH", "").split(os.pathsep):
            os.environ["PATH"] = rg_dir + os.pathsep + os.environ.get("PATH", "")

    _RG_CACHE = resolved
    _RG_SEARCHED = True
    return resolved


def run_exact_rg(repo_root: Path, term_specs: list[SearchTermSpec], config: dict[str, Any]) -> list[ExactMatch]:
    rg = find_ripgrep()
    if not rg:
        raise SystemExit(
            "ripgrep (rg) is required for exact completeness accounting but was not found.\n"
            "Install it (Windows: winget install BurntSushi.ripgrep.MSVC; "
            "macOS: brew install ripgrep; Linux: apt install ripgrep), or set "
            "GURNEY_REPO_SEARCH_RG to the full path of the rg executable."
        )
    if not term_specs:
        return []

    grouped: dict[tuple[str, ...], list[SearchTermSpec]] = {}
    for spec in term_specs:
        grouped.setdefault(tuple(sorted(spec.source_paths)), []).append(spec)
    merged: dict[tuple[str, int, str], ExactMatch] = {}
    for source_paths, specs in grouped.items():
        command = [rg, "--json", "-i", "--pcre2", "--no-messages"]
        for spec in specs:
            command.extend(["-e", term_pattern(spec.term, spec.match_mode)])
        for ext in config["textExtensions"]:
            command.extend(["--glob", f"*{ext}"])
        for pattern in config["excludedPaths"]:
            command.extend(["--glob", f"!{pattern}"])
        command.extend(["--glob", "!research/future-research/research-leads*.csv"])
        targets = [path for path in source_paths if (repo_root / path).is_file()] if source_paths else ["."]
        if not targets:
            continue
        command.extend(targets)
        process = subprocess.Popen(
            command,
            cwd=repo_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        assert process.stdout is not None
        for line in process.stdout:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") != "match":
                continue
            data = event["data"]
            path = data["path"]["text"].replace("\\", "/").lstrip("./")
            line_data = data.get("lines", {})
            if "text" in line_data:
                line_text = line_data["text"].rstrip("\r\n")
            elif "bytes" in line_data:
                line_text = base64.b64decode(line_data["bytes"]).decode("utf-8", errors="replace").rstrip("\r\n")
            else:
                continue
            matched = [
                submatch.get("match", {}).get("text", "")
                for submatch in data.get("submatches", [])
                if submatch.get("match", {}).get("text", "")
            ]
            key = (path, int(data["line_number"]), line_text)
            if key in merged:
                merged[key].terms = sorted(set(merged[key].terms + matched))
            else:
                merged[key] = ExactMatch(
                    path=path,
                    line_number=int(data["line_number"]),
                    line=line_text,
                    terms=sorted(set(matched)),
                )
        _stderr = process.communicate()[1]
        if process.returncode not in (0, 1):
            raise SystemExit(f"ripgrep failed with exit code {process.returncode}: {_stderr.strip()}")
    return sorted(merged.values(), key=lambda item: (item.path.casefold(), item.line_number, item.line))


def lexical_search_specs(index: SearchIndex, specs: list[SearchTermSpec], broad: bool = False) -> dict[int, float]:
    scores: dict[int, float] = {}
    unrestricted = [spec.term for spec in specs if not spec.source_paths]
    if unrestricted:
        scores.update(index.lexical_search(unrestricted, broad=broad))
    for spec in (item for item in specs if item.source_paths):
        allowed = set(spec.source_paths)
        for section_id, score in index.lexical_search([spec.term], broad=broad).items():
            try:
                section = index.get_section(section_id)
            except KeyError:
                continue
            if section.path in allowed:
                scores[section_id] = max(scores.get(section_id, 0.0), score)
    return scores


def text_matches_spec(text: str, spec: SearchTermSpec) -> bool:
    normalized_text = normalize_text(text)
    normalized_term = normalize_text(spec.term)
    if spec.match_mode == "substring":
        return normalized_term in normalized_text
    pattern = re.escape(normalized_term)
    if spec.match_mode == "phrase":
        pattern = pattern.replace(r"\ ", r"\s+")
    return re.search(rf"(?<!\w){pattern}(?!\w)", normalized_text, flags=re.I) is not None


def spec_applies_to_path(spec: SearchTermSpec, path: str) -> bool:
    return not spec.source_paths or path in spec.source_paths


def load_lead_sections(repo_root: Path, terms: list[str], lead_id: str | None = None) -> list[Section]:
    sys.path.insert(0, str(repo_root / "tools"))
    try:
        import research_leads  # type: ignore
    finally:
        if sys.path[0] == str(repo_root / "tools"):
            sys.path.pop(0)
    store = research_leads.LeadStore.load(repo_root / LEADS_REL, repo_root / DONE_LEADS_REL)
    wanted = normalize_text(lead_id) if lead_id else ""
    normalized_terms = [normalize_text(term) for term in terms]
    sections: list[Section] = []
    for row in store.rows:
        blob = "\n".join(f"{key}: {value}" for key, value in row.items())
        if wanted and normalize_text(row.get("ID", "")) != wanted:
            continue
        if normalized_terms and not any(term in normalize_text(blob) for term in normalized_terms):
            continue
        sections.append(
            Section(
                path=str(LEADS_REL).replace("\\", "/"),
                heading=row.get("ID", ""),
                heading_path=row.get("ID", ""),
                start_line=0,
                end_line=0,
                body=blob,
                layer="leads",
                object_type="lead",
                object_id=row.get("ID", ""),
                source_ids=extract_source_ids(blob),
            )
        )
    return sections


def bucket_for(section: Section, direct_paths: set[str], direct_object_id: str = "") -> str:
    if section.path in direct_paths or (direct_object_id and section.object_id == direct_object_id):
        return "core"
    if section.layer == "sources" or section.path == "data/sources.json":
        return "source-and-corpus"
    if section.layer == "leads":
        return "leads"
    if section.layer == "historical":
        return "historical-audit"
    return "supporting"


def excerpt_for(section: Section, exact_lines: list[int], entity_map: bool = False, width: int = 1800) -> str:
    if entity_map:
        return section.body
    lines = section.body.splitlines()
    if exact_lines:
        relative = [max(0, line - section.start_line) for line in exact_lines]
        selected: set[int] = set()
        for index in relative:
            selected.update(range(max(0, index - 3), min(len(lines), index + 5)))
        output = []
        previous = -2
        for index in sorted(selected):
            if index > previous + 1:
                output.append("...")
            output.append(lines[index])
            previous = index
        text = "\n".join(output).strip()
    else:
        text = section.body.strip()
    if len(text) > width:
        text = text[:width].rstrip() + "\n...[excerpt continues in all-results.jsonl or via expand]"
    return text


def daniel_warnings(section: Section, config: dict[str, Any]) -> list[str]:
    dg = config.get("danielGurney", {})
    if section.path != dg.get("supplementPath") or not section.page_marker.startswith("p. "):
        return []
    try:
        page = int(section.page_marker.split()[1])
    except (ValueError, IndexError):
        return []
    if page < int(dg.get("supplementFirstPage", 725)):
        return [f"Supplement page marker {page} is below 725 and may be OCR/miscitation noise."]
    return []


def build_results(
    index: SearchIndex,
    exact_matches: list[ExactMatch],
    fts_scores: dict[int, float],
    effective_terms: list[str],
    term_specs: list[SearchTermSpec],
    entity: Entity | None,
    entity_map: bool,
    config: dict[str, Any],
    lead_sections: list[Section],
    explicit_terms: list[str],
    require_all: bool = False,
    exact_only: bool = False,
    near: int | None = None,
) -> list[SearchResult]:
    exact_by_path: dict[str, list[ExactMatch]] = {}
    for match in exact_matches:
        exact_by_path.setdefault(match.path, []).append(match)
    direct_paths = set(entity.paths if entity else [])
    direct_object_id = entity.id if entity else ""
    candidate_ids = set(fts_scores)
    section_cache: dict[int, Section] = {}
    for section_id, section in index.all_sections():
        section_cache[section_id] = section
        if section.path in exact_by_path and any(section.start_line <= match.line_number <= section.end_line for match in exact_by_path[section.path]):
            candidate_ids.add(section_id)
        if any(
            spec_applies_to_path(spec, section.path)
            and text_matches_spec(section.path + " " + section.heading, spec)
            for spec in term_specs
        ):
            candidate_ids.add(section_id)
        if entity_map and section.path in direct_paths:
            candidate_ids.add(section_id)
        if direct_object_id and section.object_id == direct_object_id:
            candidate_ids.add(section_id)

    prelim: list[tuple[Section, float, list[str], list[str], list[int]]] = []
    for section_id in candidate_ids:
        section = section_cache.get(section_id)
        if section is None:
            # Another process may refresh the shared accelerator between the
            # FTS query and this snapshot. Exact ripgrep completeness remains
            # intact; omit the stale ranking-only row.
            continue
        local_matches = [match for match in exact_by_path.get(section.path, []) if section.start_line <= match.line_number <= section.end_line]
        exact_lines = sorted({match.line_number for match in local_matches})
        matched_terms = sorted({term for match in local_matches for term in match.terms})
        kinds = []
        score = fts_scores.get(section_id, 0.0)
        if local_matches:
            kinds.append("exact")
            score += 35.0 + min(30.0, len(local_matches) * 3.0)
        path_blob = normalize_text(section.path + " " + section.heading)
        path_hits = sum(
            1
            for spec in term_specs
            if spec_applies_to_path(spec, section.path) and text_matches_spec(path_blob, spec)
        )
        if path_hits:
            kinds.append("path-or-heading")
            score += 12.0 + path_hits * 3.0
        if section.path in direct_paths or (direct_object_id and section.object_id == direct_object_id):
            kinds.append("direct-entity")
            score += 45.0
        if section.layer == "historical":
            score -= 18.0
        elif section.layer == "sources":
            score += 8.0
        if entity and entity.id and (entity.id in section.body or entity.generation in section.path):
            score += 10.0
        direct = section.path in direct_paths or (direct_object_id and section.object_id == direct_object_id)
        normalized_blob = normalize_text(section.path + "\n" + section.heading + "\n" + section.body)
        normalized_terms = [normalize_text(term) for term in explicit_terms]
        coverage = sum(1 for term in normalized_terms if term in normalized_blob)
        if require_all and normalized_terms and coverage < len(normalized_terms) and not direct:
            continue
        if exact_only and not local_matches and not direct:
            continue
        if near and len(normalized_terms) > 1 and coverage == len(normalized_terms):
            positions = [normalized_blob.find(term) for term in normalized_terms]
            if max(positions) - min(positions) <= near * 12:
                score += 10.0
                kinds.append("near")
        prelim.append((section, score, sorted(set(kinds or ["fts"])), matched_terms, exact_lines))

    for section in lead_sections:
        prelim.append((section, 32.0, ["lead-tool"], effective_terms, []))

    prelim.sort(key=lambda item: (-item[1], item[0].path.casefold(), item[0].start_line))
    results: list[SearchResult] = []
    for number, (section, score, kinds, matched_terms, exact_lines) in enumerate(prelim, start=1):
        results.append(
            SearchResult(
                result_id=number,
                section=section,
                score=score,
                match_kinds=kinds,
                matched_terms=matched_terms,
                exact_lines=exact_lines,
                bucket=bucket_for(section, direct_paths, direct_object_id),
                excerpt=excerpt_for(section, exact_lines, entity_map=entity_map and section.path in direct_paths),
                warnings=daniel_warnings(section, config),
            )
        )
    return results


def render_result(result: SearchResult) -> str:
    section = result.section
    location = f"{section.path}:{section.start_line}"
    marker = f" ({section.page_marker})" if section.page_marker else ""
    lines = [
        f"## R{result.result_id}: {section.heading}{marker}",
        "",
        f"- Path: `{location}`",
        f"- Layer/object: `{section.layer}` / `{section.object_type}`",
        f"- Score/signals: {result.score:.1f}; {', '.join(result.match_kinds)}",
    ]
    if result.exact_lines:
        lines.append(f"- Exact match lines: {', '.join(str(value) for value in result.exact_lines)}")
    if section.source_ids:
        lines.append(f"- Source IDs: {', '.join(f'`{value}`' for value in section.source_ids)}")
    for warning in result.warnings:
        lines.append(f"- Warning: {warning}")
    lines.extend(["", result.excerpt.strip(), ""])
    if section.footnotes:
        lines.append("### Attached footnotes")
        lines.append("")
        for note in section.footnotes:
            lines.append(f"[^{note.key}]: {note.body}")
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def result_concept_coverage(result: SearchResult, terms: list[str]) -> int:
    if not terms:
        return 0
    blob = normalize_text(
        result.section.path + "\n" + result.section.heading + "\n" + result.section.body
    )
    return sum(1 for term in terms if normalize_text(term) in blob)


def select_staged_results(
    results: list[SearchResult],
    explicit_terms: list[str],
    entity_map: bool,
) -> list[SearchResult]:
    """Choose progressive-reading volumes without truncating saved retrieval.

    all-results.jsonl remains exhaustive. Volumes stage every direct/core
    result, every result covering all explicit concepts for multi-term queries,
    and a diverse high-ranked partial sample from each non-core bucket.
    """

    selected: dict[int, SearchResult] = {}
    term_count = len(explicit_terms)
    for result in results:
        coverage = result_concept_coverage(result, explicit_terms)
        if result.bucket == "core":
            selected[result.result_id] = result
        elif term_count > 1 and coverage == term_count:
            selected[result.result_id] = result

    per_bucket = 30 if term_count <= 1 else 20
    if entity_map:
        per_bucket = 35
    bucket_counts: dict[str, int] = {}
    file_counts: dict[tuple[str, str], int] = {}
    for result in results:
        if result.result_id in selected:
            continue
        bucket = result.bucket
        if bucket_counts.get(bucket, 0) >= per_bucket:
            continue
        file_key = (bucket, result.section.path)
        if file_counts.get(file_key, 0) >= 3:
            continue
        selected[result.result_id] = result
        bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
        file_counts[file_key] = file_counts.get(file_key, 0) + 1
    return [selected[key] for key in sorted(selected)]


def paginate_blocks(blocks: list[str], target: int) -> list[str]:
    pages: list[str] = []
    current: list[str] = []
    current_size = 0
    for block in blocks:
        if current and current_size + len(block) > target:
            pages.append("\n\n".join(current).strip() + "\n")
            current = []
            current_size = 0
        current.append(block)
        current_size += len(block)
    if current:
        pages.append("\n\n".join(current).strip() + "\n")
    return pages


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def create_search_id(summary: str) -> str:
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{stamp}-{slugify(summary)}"


def write_package(
    cache_root: Path,
    query: dict[str, Any],
    inventory: list[FileRecord],
    exact_matches: list[ExactMatch],
    results: list[SearchResult],
    config: dict[str, Any],
    index_stats: dict[str, int],
    entity: Entity | None,
) -> tuple[str, Path, str]:
    summary = query.get("summary", "search")
    search_id = create_search_id(summary)
    package = cache_root / "runs" / search_id
    suffix = 1
    while package.exists():
        package = cache_root / "runs" / f"{search_id}-{suffix}"
        suffix += 1
    search_id = package.name
    package.mkdir(parents=True)

    with (package / "exact-matches.jsonl").open("w", encoding="utf-8") as handle:
        for match in exact_matches:
            handle.write(json.dumps(asdict(match), ensure_ascii=False) + "\n")
    with (package / "all-results.jsonl").open("w", encoding="utf-8") as handle:
        for result in results:
            item = {
                "result_id": result.result_id,
                "score": result.score,
                "match_kinds": result.match_kinds,
                "matched_terms": result.matched_terms,
                "exact_lines": result.exact_lines,
                "bucket": result.bucket,
                "warnings": result.warnings,
                "section": asdict(result.section),
            }
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    query["searchId"] = search_id
    query["createdAt"] = dt.datetime.now(dt.timezone.utc).isoformat()
    query["packageVersion"] = SEARCH_PACKAGE_VERSION
    write_json(package / "query.json", query)
    write_json(
        package / "inventory.json",
        {
            "fileCount": len(inventory),
            "files": [asdict(record) for record in inventory],
            "indexRefresh": index_stats,
        },
    )

    staged_results = select_staged_results(
        results,
        query.get("originalTerms", []),
        bool(query.get("entityMap")),
    )
    write_json(package / "staged-result-ids.json", [result.result_id for result in staged_results])

    bucket_order = ["core", "supporting", "source-and-corpus", "leads", "historical-audit"]
    bucket_prefix = {"core": "01", "supporting": "02", "source-and-corpus": "03", "leads": "04", "historical-audit": "05"}
    volume_entries: list[dict[str, Any]] = []
    for bucket in bucket_order:
        blocks = [render_result(result) for result in staged_results if result.bucket == bucket]
        if not blocks:
            continue
        pages = paginate_blocks(blocks, int(config.get("volumeTargetChars", 10000)))
        for part, content in enumerate(pages, start=1):
            suffix_name = f"-part-{part:02d}" if len(pages) > 1 else ""
            filename = f"{bucket_prefix[bucket]}-{bucket}-results{suffix_name}.md"
            heading = f"# {bucket.replace('-', ' ').title()} results"
            note = f"> Volume {part} of {len(pages)} for this bucket. Complete results remain in `all-results.jsonl`."
            (package / filename).write_text(f"{heading}\n\n{note}\n\n{content}", encoding="utf-8")
            volume_entries.append({"file": filename, "bucket": bucket, "part": part, "parts": len(pages), "characters": len(content)})

    exact_paths = len({match.path for match in exact_matches})
    footnotes_needed = sum(len(result.section.footnote_keys) for result in results)
    footnotes_attached = sum(len(result.section.footnotes) for result in results)
    manifest_limit = int(config.get("manifestResultLimit", 12))
    shown = staged_results[:manifest_limit]
    direct_paths = set(entity.paths if entity else [])
    direct_indexed = {
        result.section.path
        for result in results
        if result.section.path in direct_paths
    }
    manifest_lines = [
        f"# Repository search `{search_id}`",
        "",
        f"Query: {query['summary']}",
        f"Package: `{package}`",
        "",
        "## Completeness ledger",
        "",
        f"- Inventory searched: {len(inventory)} text files; `site/` excluded.",
        f"- Exact lexical matching lines: {len(exact_matches)} across {exact_paths} files.",
        f"- Grouped result sections: {len(results)}.",
        f"- Sections staged in readable volumes: {len(staged_results)}; all {len(results)} remain in `all-results.jsonl`.",
        f"- Sections shown in this manifest: {len(shown)}.",
        f"- Exact-match ledger: `exact-matches.jsonl`.",
        f"- Referenced footnotes attached: {footnotes_attached}/{footnotes_needed}"
        + (" (complete)." if footnotes_attached == footnotes_needed else " (some references had no local definition)."),
        f"- SQLite refresh: {index_stats['changed']} changed, {index_stats['removed']} removed, {index_stats['unchanged']} unchanged.",
        "- Correctness invariant: SQLite ranks; ripgrep supplies the independent exact-match ledger.",
    ]
    if entity:
        manifest_lines.extend(
            [
                f"- Resolved {entity.kind}: {entity.generation + ' ' if entity.generation else ''}{entity.label} (`{entity.id}`).",
                f"- Direct entity files represented: {len(direct_indexed)}/{len(direct_paths)}.",
            ]
        )
    name_variants = query.get("nameVariants", {})
    selected_labels = ", ".join(name_variants.get("labels", [])) or "None"
    inferred_note = " (inferred from ancestor generation)" if name_variants.get("inferred") else ""
    manifest_lines.extend(
        [
            f"- Name-variant family: {selected_labels}{inferred_note}.",
            f"- Expansion profile: {query.get('variantProfile', 'none')}; "
            f"{len(query.get('variantExpansions', []))} variant expansion(s).",
        ]
    )
    collision_warnings = query.get("collisionWarnings", [])
    if collision_warnings:
        manifest_lines.extend(f"- Variant collision warning: {warning}" for warning in collision_warnings)
    manifest_lines.extend(["", "## Reading plan", ""])
    for bucket in bucket_order:
        volumes = [item for item in volume_entries if item["bucket"] == bucket]
        if not volumes:
            continue
        recommendation = "recommended" if bucket in {"core", "source-and-corpus"} else "read when relevant"
        total_chars = sum(item["characters"] for item in volumes)
        if len(volumes) == 1:
            manifest_lines.append(f"- `{volumes[0]['file']}` — {bucket}, {total_chars} chars; {recommendation}.")
        else:
            manifest_lines.append(
                f"- {bucket}: {len(volumes)} volumes, {total_chars} chars total "
                f"(`{volumes[0]['file']}` through `{volumes[-1]['file']}`); {recommendation}."
            )
    manifest_lines.extend(
        [
            "",
            "Before a negative-result, identity, chronology, or source-evidence conclusion, review every applicable volume or inspect the exhaustive JSONL ledgers.",
            "",
            "## Highest-ranked locators",
            "",
        ]
    )
    for result in shown:
        marker = f", {result.section.page_marker}" if result.section.page_marker else ""
        manifest_lines.append(
            f"- R{result.result_id} [{result.bucket}] `{result.section.path}:{result.section.start_line}`"
            f" — {result.section.heading}{marker} ({result.score:.1f})"
        )
    if len(staged_results) > len(shown):
        manifest_lines.append(f"- {len(staged_results) - len(shown)} additional staged sections are in the readable volumes.")
    if len(results) > len(staged_results):
        manifest_lines.append(
            f"- {len(results) - len(staged_results)} lower-ranked/partial sections are not expanded into volumes; "
            "they remain addressable in `all-results.jsonl` and via `expand --results`."
        )
    manifest = "\n".join(manifest_lines).strip() + "\n"
    (package / "00-manifest.md").write_text(manifest, encoding="utf-8")
    return search_id, package, manifest


def resolve_run(cache_root: Path, search_id: str) -> Path:
    exact = cache_root / "runs" / search_id
    if exact.is_dir():
        return exact
    matches = sorted((cache_root / "runs").glob(f"*{search_id}*")) if (cache_root / "runs").exists() else []
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(f"Search run not found: {search_id}")
    raise SystemExit("Ambiguous search ID:\n" + "\n".join(path.name for path in matches))


def terms_from_args(values: list[str] | None) -> list[str]:
    return [value.strip() for value in (values or []) if value.strip()]


def execute_search(args: argparse.Namespace, entity_map: bool = False) -> int:
    repo_root = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    config = load_config(repo_root)
    cache_root = Path(config["cacheRootResolved"])
    cache_root.mkdir(parents=True, exist_ok=True)
    inventory = git_inventory(repo_root, config)
    index = SearchIndex(cache_root / "index/repo-search.sqlite3")
    try:
        index_stats = index.refresh(repo_root, inventory)
        entity: Entity | None = None
        if args.ancestor:
            entity = resolve_ancestor(repo_root, args.ancestor, config)
        elif args.place:
            entity = resolve_place(repo_root, args.place)
        elif args.source:
            entity = resolve_source(repo_root, args.source)
        terms = terms_from_args(args.terms)
        if args.lead:
            terms.append(args.lead.upper())
        variant_profile = "none" if args.exact else args.variants
        name_variant_request = "none" if args.exact else args.name_variants
        term_specs, expansions, name_variant_selection = expand_variants(
            repo_root,
            terms,
            variant_profile,
            name_variant_request,
            entity,
        )
        effective_terms = [spec.term for spec in term_specs]
        if not effective_terms and not entity:
            raise SystemExit("Provide --terms or an entity selector.")
        exact_matches = run_exact_rg(repo_root, term_specs, config)
        fts_scores = lexical_search_specs(index, term_specs, broad=variant_profile == "broad")
        lead_terms = [spec.term for spec in term_specs if not spec.source_paths]
        lead_sections = load_lead_sections(repo_root, lead_terms, args.lead)
        results = build_results(
            index,
            exact_matches,
            fts_scores,
            effective_terms,
            term_specs,
            entity,
            entity_map,
            config,
            lead_sections,
            explicit_terms=terms,
            require_all=args.require_all,
            exact_only=args.exact,
            near=args.near,
        )
        summary_parts = []
        if entity:
            summary_parts.append(f"{entity.generation or entity.kind} {entity.label}")
        summary_parts.extend(terms or ["repository map"])
        query = {
            "summary": " | ".join(summary_parts),
            "originalTerms": terms,
            "effectiveTerms": effective_terms,
            "variantProfile": variant_profile,
            "nameVariants": name_variant_selection,
            "variantExpansions": expansions,
            "termSpecs": [asdict(spec) for spec in term_specs],
            "collisionWarnings": sorted(
                {
                    spec.collision_warning
                    for spec in term_specs
                    if spec.collision_warning
                }
            ),
            "entity": asdict(entity) if entity else None,
            "entityMap": entity_map,
            "lead": args.lead,
            "siteExcluded": True,
        }
        _search_id, _package, manifest = write_package(cache_root, query, inventory, exact_matches, results, config, index_stats, entity)
        print(manifest, end="")
        return 0
    finally:
        index.close()


def command_search(args: argparse.Namespace) -> int:
    return execute_search(args, entity_map=False)


def command_map(args: argparse.Namespace) -> int:
    return execute_search(args, entity_map=True)


def command_expand(args: argparse.Namespace) -> int:
    repo_root = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    config = load_config(repo_root)
    run = resolve_run(Path(config["cacheRootResolved"]), args.search_id)
    if args.volume:
        candidates = sorted(run.glob(f"{args.volume}*.md"))
        if not candidates:
            candidates = sorted(run.glob(f"*{args.volume}*.md"))
        if not candidates:
            raise SystemExit(f"No volume matching {args.volume!r}.")
        for path in candidates:
            print(path.read_text(encoding="utf-8"), end="\n")
        return 0
    wanted_results = set(args.results or [])
    wanted_file = args.file.replace("\\", "/") if args.file else ""
    wanted_section = normalize_text(args.section or "")
    found = 0
    with (run / "all-results.jsonl").open("r", encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            section = item["section"]
            if wanted_results and int(item["result_id"]) not in wanted_results:
                continue
            if wanted_file and section["path"] != wanted_file:
                continue
            if wanted_section and wanted_section not in normalize_text(section["heading_path"]):
                continue
            result = SearchResult(
                result_id=item["result_id"],
                section=Section(**{**section, "footnotes": [Footnote(**note) for note in section.get("footnotes", [])]}),
                score=item["score"],
                match_kinds=item["match_kinds"],
                matched_terms=item["matched_terms"],
                exact_lines=item["exact_lines"],
                bucket=item["bucket"],
                excerpt=section["body"],
                warnings=item.get("warnings", []),
            )
            print(render_result(result))
            found += 1
    if not found:
        raise SystemExit("No matching saved results.")
    return 0


def command_runs(args: argparse.Namespace) -> int:
    repo_root = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    config = load_config(repo_root)
    runs_root = Path(config["cacheRootResolved"]) / "runs"
    runs = sorted([path for path in runs_root.iterdir() if path.is_dir()], reverse=True) if runs_root.exists() else []
    for path in runs[: args.limit]:
        query_path = path / "query.json"
        if not query_path.exists():
            continue
        query = load_json(query_path)
        print(f"{path.name}\t{query.get('summary','')}\t{path}")
    return 0


def command_resume(args: argparse.Namespace) -> int:
    repo_root = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    config = load_config(repo_root)
    run = resolve_run(Path(config["cacheRootResolved"]), args.search_id)
    print((run / "00-manifest.md").read_text(encoding="utf-8"), end="")
    return 0


def command_index(args: argparse.Namespace) -> int:
    repo_root = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    config = load_config(repo_root)
    inventory = git_inventory(repo_root, config)
    index = SearchIndex(Path(config["cacheRootResolved"]) / "index/repo-search.sqlite3")
    try:
        if args.rebuild:
            index.rebuild()
            stats = index.refresh(repo_root, inventory, force=True)
            print(json.dumps({"status": "rebuilt", **stats}, indent=2))
        elif args.update:
            stats = index.refresh(repo_root, inventory)
            print(json.dumps({"status": "updated", **stats}, indent=2))
        elif args.check:
            stale = index.stale(inventory)
            print(json.dumps({"status": "fresh" if not stale else "stale", "staleCount": len(stale), "stalePaths": stale[:50]}, indent=2))
            return 1 if stale else 0
        else:
            stale = index.stale(inventory)
            files = index.conn.execute("SELECT COUNT(*) FROM files").fetchone()[0]
            sections = index.conn.execute("SELECT COUNT(*) FROM sections").fetchone()[0]
            print(json.dumps({"database": str(index.path), "files": files, "sections": sections, "staleCount": len(stale), "trigram": index.trigram_available}, indent=2))
        return 0
    finally:
        index.close()


def command_clean(args: argparse.Namespace) -> int:
    repo_root = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    config = load_config(repo_root)
    cache_root = Path(config["cacheRootResolved"])
    runs_root = cache_root / "runs"
    if not runs_root.exists():
        print("No saved search runs.")
        return 0
    cutoff = dt.datetime.now() - dt.timedelta(days=args.older_than)
    removed = 0
    for path in runs_root.iterdir():
        if not path.is_dir():
            continue
        modified = dt.datetime.fromtimestamp(path.stat().st_mtime)
        if args.all or modified < cutoff:
            shutil.rmtree(path)
            removed += 1
    if args.all and (cache_root / "index").exists():
        shutil.rmtree(cache_root / "index")
    print(f"Removed {removed} saved search run(s)." + (" Index removed." if args.all else ""))
    return 0


def command_variants(args: argparse.Namespace) -> int:
    repo_root = find_repo_root(Path(args.repo_root) if args.repo_root else None)
    data = load_variants(repo_root)
    families = data.get("nameVariantFamilies", [])
    source_groups = [
        group
        for group in data.get("variantSets", [])
        if group.get("kind") == "source-specific-ocr"
    ]
    if args.variants_command == "validate":
        errors: list[str] = []
        seen: set[str] = set()
        ranges: list[tuple[int, int, str]] = []
        for family in families:
            family_id = family.get("id", "")
            if not family_id or family_id in seen:
                errors.append(f"Missing or duplicate family id: {family_id!r}")
            seen.add(family_id)
            generation_range = family.get("generationRange", {})
            minimum = generation_range.get("minimum")
            maximum = generation_range.get("maximum")
            if not isinstance(minimum, int) or not isinstance(maximum, int) or minimum > maximum:
                errors.append(f"{family_id}: invalid generation range")
            else:
                ranges.append((minimum, maximum, family_id))
            local_terms: set[str] = set()
            for profile_key in ("conservative", "broadAdditions"):
                for variant in family.get(profile_key, []):
                    term = normalize_text(variant.get("term", ""))
                    if not term or term in local_terms:
                        errors.append(f"{family_id}: missing or duplicate term {variant.get('term')!r}")
                    local_terms.add(term)
                    if variant.get("matchMode") not in {"whole-token", "phrase", "substring"}:
                        errors.append(f"{family_id}: invalid match mode for {variant.get('term')!r}")
        ranges.sort()
        if ranges and ranges != [(1, 13, "modern"), (14, 28, "english"), (29, 37, "norman")]:
            errors.append(f"Unexpected name-variant generation ranges: {ranges!r}")
        for group in source_groups:
            group_id = group.get("id")
            if not group_id or group_id in seen:
                errors.append(f"Missing or duplicate id: {group_id!r}")
            seen.add(group_id)
            if group.get("kind") == "source-specific-ocr" and not group.get("sourcePaths"):
                errors.append(f"{group_id}: source-specific OCR set lacks sourcePaths")
            for variant in group.get("variants", []):
                if variant.get("profile") not in {"conservative", "broad"}:
                    errors.append(f"{group_id}: invalid profile for {variant.get('term')!r}")
        if errors:
            print("\n".join(errors))
            return 1
        print(f"OK: {len(families)} name-variant families and {len(source_groups)} source-specific set(s).")
        return 0
    if args.variants_command == "list":
        for family in families:
            generation_range = family.get("generationRange", {})
            conservative = len(family.get("conservative", []))
            broad_total = conservative + len(family.get("broadAdditions", []))
            print(
                f"{family.get('id')}\t{family.get('label')}\t"
                f"G{generation_range.get('minimum')}–G{generation_range.get('maximum')}\t"
                f"{conservative} conservative / {broad_total} broad total"
            )
        for group in source_groups:
            print(f"{group.get('id')}\t{group.get('canonical')}\t{len(group.get('variants', []))} source-specific variant(s)")
        return 0
    if args.variants_command == "table":
        wanted = normalize_text(args.name or "")
        selected = [
            family
            for family in families
            if not wanted or wanted in {normalize_text(family.get("id", "")), normalize_text(family.get("label", ""))}
        ]
        if not selected:
            raise SystemExit(f"Name-variant family not found: {args.name}")
        print("| Family | Generations | Conservative | Broad additions |")
        print("|---|---:|---|---|")
        for family in selected:
            generation_range = family["generationRange"]
            conservative = ", ".join(f"`{item['term']}`" for item in family.get("conservative", []))
            broad = ", ".join(f"`{item['term']}`" for item in family.get("broadAdditions", []))
            print(
                f"| {family.get('label')} | G{generation_range['minimum']}–G{generation_range['maximum']} "
                f"| {conservative} | {broad} |"
            )
        return 0
    wanted = normalize_text(args.name)
    matches = [
        group
        for group in [*families, *source_groups]
        if wanted
        in {
            normalize_text(group.get("id", "")),
            normalize_text(group.get("label", "")),
            normalize_text(group.get("canonical", "")),
        }
    ]
    if not matches:
        raise SystemExit(f"Variant set not found: {args.name}")
    if args.variants_command == "show":
        print(json.dumps(matches[0], ensure_ascii=False, indent=2))
        return 0
    profile = args.profile
    match = matches[0]
    if "conservative" in match:
        values = [item.get("term", "") for item in match.get("conservative", [])]
        if profile == "broad":
            values.extend(item.get("term", "") for item in match.get("broadAdditions", []))
    else:
        values = [match.get("canonical", "")]
        values.extend(
            item.get("term", "")
            for item in match.get("variants", [])
            if profile == "broad" or item.get("profile") == "conservative"
        )
    print("\n".join(value for value in values if value))
    return 0


def add_search_arguments(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--ancestor", help="Generation, record ID, or unique ancestor name.")
    group.add_argument("--place", help="Place ID, canonical name, filename, or alias.")
    group.add_argument("--source", help="Source ID, title, or associated path.")
    parser.add_argument("--lead", help="Live lead ID, e.g. L-138.")
    parser.add_argument("--terms", nargs="*", default=[], help="Search terms; quote phrases at the shell level.")
    parser.add_argument("--variants", choices=["none", "conservative", "broad"], default="conservative")
    parser.add_argument(
        "--name-variants",
        type=str.casefold,
        choices=["auto", "modern", "english", "norman", "all", "none"],
        default="auto",
        help="Surname family: auto infers from --ancestor; raw searches stay literal unless a family is selected.",
    )
    parser.add_argument("--exact", action="store_true", help="Disable variants and stage only exact-hit/direct-object sections.")
    parser.add_argument("--require-all", action="store_true", help="Require every explicit term in a section, except direct entity objects.")
    parser.add_argument("--any", action="store_true", help="Explicitly document normal any-term retrieval semantics.")
    parser.add_argument("--near", type=int, help="Boost sections whose explicit terms occur within roughly this many words.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", help="Override repository root.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Run exhaustive staged repository search.")
    add_search_arguments(p_search)
    p_search.set_defaults(func=command_search)

    p_map = sub.add_parser("map", help="Build a whole-entity repository knowledge package.")
    add_search_arguments(p_map)
    p_map.set_defaults(func=command_map)

    p_expand = sub.add_parser("expand", help="Read selected saved results or volumes.")
    p_expand.add_argument("search_id")
    p_expand.add_argument("--results", type=int, nargs="+")
    p_expand.add_argument("--volume")
    p_expand.add_argument("--file")
    p_expand.add_argument("--section")
    p_expand.set_defaults(func=command_expand)

    p_runs = sub.add_parser("runs", help="List recent saved searches.")
    p_runs.add_argument("--limit", type=int, default=20)
    p_runs.set_defaults(func=command_runs)

    p_resume = sub.add_parser("resume", help="Print a saved search manifest.")
    p_resume.add_argument("search_id")
    p_resume.set_defaults(func=command_resume)

    p_index = sub.add_parser("index", help="Inspect or maintain the local search index.")
    index_group = p_index.add_mutually_exclusive_group()
    index_group.add_argument("--status", action="store_true")
    index_group.add_argument("--update", action="store_true")
    index_group.add_argument("--rebuild", action="store_true")
    index_group.add_argument("--check", action="store_true")
    p_index.set_defaults(func=command_index)

    p_clean = sub.add_parser("clean", help="Remove expired saved search packages.")
    p_clean.add_argument("--older-than", type=int, default=90)
    p_clean.add_argument("--all", action="store_true")
    p_clean.set_defaults(func=command_clean)

    p_variants = sub.add_parser("variants", help="Inspect or validate curated search variants.")
    variants_sub = p_variants.add_subparsers(dest="variants_command", required=True)
    v_list = variants_sub.add_parser("list")
    v_list.set_defaults(func=command_variants)
    v_show = variants_sub.add_parser("show")
    v_show.add_argument("name")
    v_show.set_defaults(func=command_variants)
    v_test = variants_sub.add_parser("test")
    v_test.add_argument("name")
    v_test.add_argument("--profile", choices=["conservative", "broad"], default="conservative")
    v_test.set_defaults(func=command_variants)
    v_table = variants_sub.add_parser("table")
    v_table.add_argument("name", nargs="?")
    v_table.set_defaults(func=command_variants)
    v_validate = variants_sub.add_parser("validate")
    v_validate.set_defaults(func=command_variants)
    return parser


def _configure_stdio() -> None:
    """Make Unicode manifest/volume output survive a legacy Windows console.

    Repo content legitimately contains non-cp1252 characters (e.g. the '★'
    marker used in some research headings). Without this, the default Windows
    code page raises UnicodeEncodeError when the manifest is printed.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


def main(argv: Sequence[str] | None = None) -> int:
    _configure_stdio()
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
