#!/usr/bin/env python3
"""Generate compact ID lookup indexes for canonical data JSON files.

The generated CSV files are locator indexes only. Canonical data remains in
`data/*.json`; generated indexes live in `data/indexes/` and should not be
edited by hand.

Modes:
  --check  Generate indexes in memory and compare them with checked-in files.
           This is intentionally lightweight and does not run deeper integrity
           validations.
  --write  Run integrity validations, then write deterministic index files.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
INDEX_DIR = DATA_DIR / "indexes"

ANCESTORS_PATH = DATA_DIR / "ancestors.json"
PLACES_PATH = DATA_DIR / "places.json"
SOURCES_PATH = DATA_DIR / "sources.json"

INDEX_SPECS = {
    "ancestor-ids.csv": [
        "recordId",
        "gen",
        "type",
        "name",
        "dates",
        "lineageStatus",
        "factSheetPath",
        "researchPath",
    ],
    "place-ids.csv": [
        "placeId",
        "name",
        "placeType",
        "filename",
        "linkedRecordIds",
        "aliases",
    ],
    "source-ids.csv": [
        "sourceId",
        "shortTitle",
        "corpusStatus",
        "corpusPath",
        "mediaPath",
        "validationPath",
    ],
    "all-ids.csv": [
        "id",
        "idType",
        "label",
        "canonicalFile",
    ],
}

ID_TYPE_ORDER = {
    "ancestor": 10,
    "related": 20,
    "era": 30,
    "place": 40,
    "source": 50,
}


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing required file: {repo_relative(path)}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {repo_relative(path)}: {exc}") from exc


def clean_cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value).replace("\r\n", " ").replace("\n", " ").strip()


def join_values(values: Iterable[Any]) -> str:
    return ";".join(clean_cell(value) for value in values if clean_cell(value))


def csv_text(fieldnames: Sequence[str], rows: Sequence[Mapping[str, Any]]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({field: clean_cell(row.get(field, "")) for field in fieldnames})
    return buffer.getvalue()


def gen_number(gen: Any) -> int:
    match = re.search(r"(\d+)", str(gen or ""))
    return int(match.group(1)) if match else 9999


def slug_from_fact_sheet_path(path_text: str) -> str:
    if not path_text:
        return ""
    return Path(path_text).name.removesuffix(".md")


def fact_sheet_path_for(item: Mapping[str, Any]) -> str:
    for button in item.get("buttons") or []:
        if not isinstance(button, Mapping):
            continue
        url = clean_cell(button.get("url"))
        label = clean_cell(button.get("label")).lower()
        if label == "fact sheet" and url.startswith("/fact-sheets/") and url.endswith(".html"):
            candidate = REPO_ROOT / "fact-sheets" / Path(url).name.replace(".html", ".md")
            return repo_relative(candidate) if candidate.exists() else ""
    return ""


def research_path_for(item: Mapping[str, Any], fact_sheet_path: str) -> str:
    slug = slug_from_fact_sheet_path(fact_sheet_path)
    if slug:
        candidate = REPO_ROOT / "research" / "people" / f"{slug}.research.md"
        if candidate.exists():
            return repo_relative(candidate)

    gen = clean_cell(item.get("gen"))
    name = clean_cell(item.get("name"))
    if gen and name:
        safe_name = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        candidate = REPO_ROOT / "research" / "people" / f"{gen.lower()}-{safe_name}-fact-sheet.research.md"
        if candidate.exists():
            return repo_relative(candidate)
    return ""


def build_ancestor_rows(ancestors: Sequence[Mapping[str, Any]]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for item in ancestors:
        record_id = clean_cell(item.get("recordId"))
        if not record_id:
            continue
        fact_sheet = fact_sheet_path_for(item)
        rows.append(
            {
                "recordId": record_id,
                "gen": clean_cell(item.get("gen")),
                "type": clean_cell(item.get("type")),
                "name": clean_cell(item.get("name") or item.get("label")),
                "dates": clean_cell(item.get("dates")),
                "lineageStatus": clean_cell(item.get("lineageStatus")),
                "factSheetPath": fact_sheet,
                "researchPath": research_path_for(item, fact_sheet),
            }
        )
    return sorted(rows, key=lambda row: (gen_number(row["gen"]), row["type"], row["name"].lower(), row["recordId"]))


def build_place_rows(places: Sequence[Mapping[str, Any]]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for place in places:
        linked_record_ids = []
        for link in place.get("ancestorLinks") or []:
            if isinstance(link, Mapping) and clean_cell(link.get("recordId")):
                linked_record_ids.append(clean_cell(link.get("recordId")))
        rows.append(
            {
                "placeId": clean_cell(place.get("placeId")),
                "name": clean_cell(place.get("name")),
                "placeType": clean_cell(place.get("placeType")),
                "filename": clean_cell(place.get("filename")),
                "linkedRecordIds": join_values(linked_record_ids),
                "aliases": join_values(place.get("aliases") or []),
            }
        )
    return sorted(rows, key=lambda row: (row["name"].lower(), row["placeId"]))


def build_source_rows(source_registry: Mapping[str, Any]) -> List[Dict[str, str]]:
    sources = source_registry.get("sources") or {}
    rows: List[Dict[str, str]] = []
    for source_id, source in sources.items():
        source_obj = source if isinstance(source, Mapping) else {}
        rows.append(
            {
                "sourceId": clean_cell(source_id),
                "shortTitle": clean_cell(source_obj.get("shortTitle") or source_id),
                "corpusStatus": clean_cell(source_obj.get("corpusStatus")),
                "corpusPath": clean_cell(source_obj.get("corpusPath")),
                "mediaPath": clean_cell(source_obj.get("mediaPath")),
                "validationPath": clean_cell(source_obj.get("validationPath")),
            }
        )
    return sorted(rows, key=lambda row: row["sourceId"])


def build_all_id_rows(
    ancestor_rows: Sequence[Mapping[str, str]],
    place_rows: Sequence[Mapping[str, str]],
    source_rows: Sequence[Mapping[str, str]],
) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for row in ancestor_rows:
        rows.append({"id": row["recordId"], "idType": row["type"] or "record", "label": row["name"], "canonicalFile": "data/ancestors.json"})
    for row in place_rows:
        rows.append({"id": row["placeId"], "idType": "place", "label": row["name"], "canonicalFile": "data/places.json"})
    for row in source_rows:
        rows.append({"id": row["sourceId"], "idType": "source", "label": row["shortTitle"], "canonicalFile": "data/sources.json"})
    return sorted(rows, key=lambda row: (ID_TYPE_ORDER.get(row["idType"], 999), row["label"].lower(), row["id"]))


def collect_unique_ids(records: Sequence[Mapping[str, Any]], id_field: str, label: str, errors: List[str]) -> set[str]:
    ids: set[str] = set()
    for index, record in enumerate(records, start=1):
        value = clean_cell(record.get(id_field))
        if not value:
            errors.append(f"{label} record {index} is missing {id_field}")
            continue
        if value in ids:
            errors.append(f"Duplicate {id_field} in {label}: {value}")
        ids.add(value)
    return ids


def parse_generated_csv(text: str) -> List[Dict[str, str]]:
    return list(csv.DictReader(io.StringIO(text)))


def validate_generated_indexes(
    generated: Mapping[str, str],
    record_ids: set[str],
    place_ids: set[str],
    source_ids: set[str],
    errors: List[str],
) -> None:
    all_rows = parse_generated_csv(generated["all-ids.csv"])
    all_pairs: set[Tuple[str, str]] = set()
    all_raw_ids: set[str] = set()
    all_by_type: Dict[str, set[str]] = {"ancestor": set(), "related": set(), "era": set(), "place": set(), "source": set()}

    for row in all_rows:
        raw_id = row.get("id", "")
        id_type = row.get("idType", "")
        pair = (id_type, raw_id)
        if pair in all_pairs:
            errors.append(f"Duplicate all-ids pair: {id_type}:{raw_id}")
        all_pairs.add(pair)
        if raw_id in all_raw_ids:
            errors.append(f"Duplicate raw ID in all-ids.csv: {raw_id}")
        all_raw_ids.add(raw_id)
        all_by_type.setdefault(id_type, set()).add(raw_id)

    all_record_ids = all_by_type.get("ancestor", set()) | all_by_type.get("related", set()) | all_by_type.get("era", set())
    if record_ids - all_record_ids:
        errors.append(f"Missing ancestor recordIds from all-ids.csv: {sorted(record_ids - all_record_ids)}")
    if place_ids - all_by_type.get("place", set()):
        errors.append(f"Missing placeIds from all-ids.csv: {sorted(place_ids - all_by_type.get('place', set()))}")
    if source_ids - all_by_type.get("source", set()):
        errors.append(f"Missing sourceIds from all-ids.csv: {sorted(source_ids - all_by_type.get('source', set()))}")


def validate_inputs(ancestors: Any, places: Any, source_registry: Any) -> None:
    errors: List[str] = []

    if not isinstance(ancestors, list):
        errors.append("data/ancestors.json must be a list")
        ancestors_list: List[Mapping[str, Any]] = []
    else:
        ancestors_list = [item for item in ancestors if isinstance(item, Mapping)]
        if len(ancestors_list) != len(ancestors):
            errors.append("data/ancestors.json contains non-object records")

    if not isinstance(places, list):
        errors.append("data/places.json must be a list")
        places_list: List[Mapping[str, Any]] = []
    else:
        places_list = [item for item in places if isinstance(item, Mapping)]
        if len(places_list) != len(places):
            errors.append("data/places.json contains non-object records")

    if not isinstance(source_registry, Mapping):
        errors.append("data/sources.json must be an object")
        sources: Mapping[str, Any] = {}
    else:
        sources = source_registry.get("sources") or {}
        if not isinstance(sources, Mapping):
            errors.append("data/sources.json must contain a sources object")
            sources = {}

    record_ids = collect_unique_ids(ancestors_list, "recordId", "data/ancestors.json", errors)
    place_ids = collect_unique_ids(places_list, "placeId", "data/places.json", errors)

    seen_source_ids: set[str] = set()
    for source_id, source in sources.items():
        source_id_text = clean_cell(source_id)
        if not source_id_text:
            errors.append("data/sources.json contains an empty source key")
        if source_id_text in seen_source_ids:
            errors.append(f"Duplicate sourceId in data/sources.json: {source_id_text}")
        seen_source_ids.add(source_id_text)
        if not isinstance(source, Mapping):
            errors.append(f"data/sources.json source {source_id!r} must be an object")

    for place in places_list:
        ancestor_links = place.get("ancestorLinks") or []
        if not isinstance(ancestor_links, list):
            errors.append(f"Place {place.get('placeId', '<missing>')} has non-list ancestorLinks")
            continue
        for link in ancestor_links:
            if not isinstance(link, Mapping):
                errors.append(f"Place {place.get('placeId', '<missing>')} has non-object ancestorLink")
                continue
            linked_record_id = clean_cell(link.get("recordId"))
            if linked_record_id and linked_record_id not in record_ids:
                errors.append(f"Place {place.get('placeId', '<missing>')} links to unknown recordId: {linked_record_id}")

    generated = build_indexes_from_loaded(ancestors_list, places_list, source_registry if isinstance(source_registry, Mapping) else {})
    validate_generated_indexes(generated, record_ids, place_ids, seen_source_ids, errors)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def build_indexes_from_loaded(
    ancestors: Sequence[Mapping[str, Any]],
    places: Sequence[Mapping[str, Any]],
    source_registry: Mapping[str, Any],
) -> Dict[str, str]:
    ancestor_rows = build_ancestor_rows(ancestors)
    place_rows = build_place_rows(places)
    source_rows = build_source_rows(source_registry)
    all_rows = build_all_id_rows(ancestor_rows, place_rows, source_rows)

    rows_by_file: Dict[str, Sequence[Mapping[str, str]]] = {
        "ancestor-ids.csv": ancestor_rows,
        "place-ids.csv": place_rows,
        "source-ids.csv": source_rows,
        "all-ids.csv": all_rows,
    }
    return {filename: csv_text(INDEX_SPECS[filename], rows_by_file[filename]) for filename in sorted(INDEX_SPECS)}


def build_indexes(validate: bool) -> Dict[str, str]:
    ancestors = load_json(ANCESTORS_PATH)
    places = load_json(PLACES_PATH)
    source_registry = load_json(SOURCES_PATH)
    if validate:
        validate_inputs(ancestors, places, source_registry)
    return build_indexes_from_loaded(
        ancestors if isinstance(ancestors, list) else [],
        places if isinstance(places, list) else [],
        source_registry if isinstance(source_registry, Mapping) else {},
    )


def check_indexes() -> int:
    generated = build_indexes(validate=False)
    missing: List[str] = []
    stale: List[str] = []

    for filename, expected in generated.items():
        path = INDEX_DIR / filename
        if not path.exists():
            missing.append(repo_relative(path))
            continue
        current = path.read_text(encoding="utf-8")
        if current != expected:
            stale.append(repo_relative(path))

    if missing or stale:
        print("ID indexes are missing or stale.", file=sys.stderr)
        for path in missing:
            print(f"- missing: {path}", file=sys.stderr)
        for path in stale:
            print(f"- stale: {path}", file=sys.stderr)
        print(r"Run: .\.venv\Scripts\python.exe tools\generate_id_indexes.py --write", file=sys.stderr)
        return 1

    print("ID indexes are current.")
    return 0


def write_indexes() -> int:
    generated = build_indexes(validate=True)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    for filename, text in generated.items():
        (INDEX_DIR / filename).write_text(text, encoding="utf-8")

    print("Generated ID indexes:")
    for filename in sorted(generated):
        row_count = max(0, len(generated[filename].splitlines()) - 1)
        print(f"- data/indexes/{filename}: {row_count} rows")
    print("Validation passed.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate compact data ID lookup indexes.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Compare generated indexes with checked-in files; no deep validations.")
    mode.add_argument("--write", action="store_true", help="Validate canonical JSON and write generated indexes.")
    args = parser.parse_args(argv)

    if args.write:
        return write_indexes()
    return check_indexes()


if __name__ == "__main__":
    raise SystemExit(main())
