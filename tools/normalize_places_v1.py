from __future__ import annotations

import copy
import json
import re
import statistics
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PLACES_DIR = ROOT / "research" / "places"
LOG_DIR = ROOT / "research" / "log"

ANCESTORS_V24 = DATA_DIR / "ancestors v24.json"
LOCATIONS_JSON = DATA_DIR / "locations.json"
PLACES_JSON = DATA_DIR / "places.json"
DATA_README = DATA_DIR / "README.md"
PLACES_README = PLACES_DIR / "README.md"
LOG_README = LOG_DIR / "README.md"

OLD_GEN_START = "<!-- GENERATED:LOCATION-REGISTRY:START -->"
OLD_GEN_END = "<!-- GENERATED:LOCATION-REGISTRY:END -->"
NEW_GEN_START = "<!-- GENERATED:PLACE-REGISTRY:START -->"
NEW_GEN_END = "<!-- GENERATED:PLACE-REGISTRY:END -->"

ATOMIC_LOG_NAME = "2026-04-17--place-normalization-v1.md"

STATE_ABBREV = {
    "Massachusetts": "ma",
    "New York": "ny",
    "Indiana": "in",
    "Oregon": "or",
    "Michigan": "mi",
    "South Carolina": "sc",
    "Missouri": "mo",
}

ALIASES_MAP = {
    "King's Lynn, Norfolk, England": ["Bishop's Lynn", "Lynn"],
    "Gournay-en-Bray, Normandy, France": ["Gournay"],
    "La Ferté-en-Bray, Normandy, France": ["La Ferte-en-Bray"],
    "Caister-on-Sea, Norfolk, England": ["Caister"],
    "Abington–Whitman line, Massachusetts, USA": ["Abington/Whitman line, Massachusetts, USA"],
    "Flushing, Queens, New York, USA": ["Flushing, NY", "Flushing, Queens, NY"],
    "Portland, Oregon, USA": ["Portland, OR"],
    "St. Louis, Missouri, USA": ["St. Louis, MO"],
    "Charleston, South Carolina, USA": ["Charleston, SC"],
    "Fort Wayne, Indiana, USA": ["Fort Wayne, IN"],
    "Marion, Indiana, USA": ["Marion, IN"],
    "Indianapolis, Indiana, USA": ["Indianapolis, IN"],
    "Dexter, Michigan, USA": ["Dexter, MI"],
    "Port Washington, New York, USA": ["Port Washington, NY"],
    "Weymouth, Massachusetts, USA": ["Weymouth, MA"],
    "Braintree, Massachusetts, USA": ["Braintree, MA"],
    "Cummington, Massachusetts, USA": ["Cummington, MA"],
    "Bridgewater, Massachusetts, USA": ["Bridgewater, MA"],
    "Middleborough, Massachusetts, USA": ["Middleborough, MA", "Middleboro, MA"],
    "Rochester, Massachusetts, USA": ["Rochester, MA"],
}

SUBSITE_NORMALIZATION = {
    "West Barsham Hall / manor site": "West Barsham Hall",
    "Collégiale Saint-Hildevert / historic centre": "Collégiale Saint-Hildevert",
    "Église Saint-Pierre-et-Saint-Paul / former core": "Église Saint-Pierre-et-Saint-Paul",
}

KNOWN_FILENAME_MAP = {
    "West Barsham, Norfolk, England": "west-barsham.md",
    "Gournay-en-Bray, Normandy, France": "gournay-en-bray.md",
    "Montigny-sur-Andelle, Normandy, France": "montigny-sur-andelle.md",
    "La Ferté-en-Bray, Normandy, France": "la-ferte-en-bray.md",
    "Le Bec-Hellouin, Normandy, France": "le-bec-hellouin.md",
    "Lessingham, Norfolk, England": "lessingham.md",
    "Harpley, Norfolk, England": "harpley.md",
    "Hardingham, Norfolk, England": "hardingham.md",
    "Runhall, Norfolk, England": "runhall.md",
    "King's Lynn, Norfolk, England": "kings-lynn.md",
    "Liston, Essex, England": "liston.md",
    "Fordham, Essex, England": "fordham.md",
    "Ardleigh, Essex, England": "ardleigh.md",
    "Suffolk, England": "suffolk.md",
    "Lewes, Sussex, England": "lewes.md",
    "Caister-on-Sea, Norfolk, England": "caister-on-sea.md",
    "Cantley, Norfolk, England": "cantley.md",
    "Braintree, Massachusetts, USA": "braintree-ma.md",
    "Hingham, Norfolk, England": "hingham-norfolk.md",
    "New York metropolitan area, USA": "new-york-metropolitan-area-usa.md",
    "Weymouth, Massachusetts, USA": "weymouth.md",
}

DATA_README_TEXT = """# data/

Canonical structured data for ancestor, mention, and place registries.

## Files

- `ancestors v23.json` — pre-extraction ancestor registry with embedded `locations`.
- `ancestors v24.json` — bridge-layer registry. Ancestor/collateral records retain `locationRefs` and now also carry normalized `placeRefs`.
- `locations.json` — raw location-mention registry extracted from `ancestors v23.json`. One entry per original embedded location object. Fidelity-first.
- `places.json` — normalized place registry. One canonical place record per place, with filename mapping, aliases, sub-sites, search terms, and reverse links to raw `locationIds`.
- `master.json` — broader canonical person/source registry used elsewhere in the repo.
- `sources.json` — bibliography and citation registry.

## Current model

The repo now uses a two-layer geography model:

1. **Raw mentions** in `locations.json`
   - preserves original note text, geocoding, dates, and inherited source fragments
   - each entry retains `locationId`
   - each entry points to a normalized `placeId`

2. **Canonical places** in `places.json`
   - one record per normalized place
   - authoritative `filename` for `research/places/`
   - aliases, sub-sites, search terms, linked records, and review flags

`ancestors v24.json` bridges to both layers:
- `locationRefs` → raw mention fidelity
- `placeRefs` → canonical place navigation

## Discipline

- Preserve raw inherited text in `locations.json` even when it is messy or partially contaminated.
- Put normalization decisions in `places.json` and in the generated place-file block.
- Do not guess at formal `sourceId` mapping during geography normalization; note issues for later cleanup instead.
- Treat `places.json` as the authoritative filename registry for place files. Do not invent filenames ad hoc once a place record exists.
"""

PLACES_README_TEXT = """# research/places/

Canonical place-memory files.

## Authority

`data/places.json` is the authoritative registry for:
- canonical place name
- `placeId`
- filename
- aliases
- search terms
- reverse links to location mentions

Do not infer filenames ad hoc when a place already exists in `data/places.json`.

## File shape

Narrative place files may contain hand-written research plus one generated block bounded by:

- `<!-- GENERATED:PLACE-REGISTRY:START -->`
- `<!-- GENERATED:PLACE-REGISTRY:END -->`

Older location-registry blocks are replaced during normalization.

## Current normalization discipline

- Preserve existing narrative research outside the generated block.
- Replace generic boilerplate introduced by the extraction pass with a concise normalized block.
- Keep sub-sites (cemeteries, churches, halls, ponds, addresses) within the parent place unless the research clearly treats them as standalone places.
- Record unresolved naming / contamination / citation issues as review notes instead of over-solving them in the first normalization pass.
"""

LOG_README_TEXT = """# research/log/

Atomic operational logs.

## Naming

Prefer small files:

- `YYYY-MM-DD--topic.md`

Multiple files per day are allowed and preferred over one large running file.

## Purpose

Each log file is a short operational pointer:
- what changed
- which files were added or updated
- what still needs review

Substantive research belongs in topical files (`people/`, `places/`, `topics/`), not in the log.

## Format

Keep entries short. A good atomic log records:
- scope
- files touched
- design decisions
- next cleanup steps
"""

LOG_TEXT = """# 2026-04-17 — place normalization v1

Normalized the geography layer after the v23 → v24 extraction merge.

Updated:
- `data/places.json` — NEW canonical place registry
- `data/locations.json` — raw mentions annotated with `placeId`, normalized sub-site names, and quality flags
- `data/ancestors v24.json` — ancestor/collateral records now also carry `placeRefs`
- `data/README.md` — two-layer raw-mention / canonical-place model documented
- `research/places/README.md` — `places.json` named as the filename authority
- `research/log/README.md` — switched to atomic log guidance
- `research/places/*.md` — generated blocks replaced with concise normalized place registry blocks

Design decisions:
- kept raw mentions intact for fidelity
- added a canonical place layer rather than overwriting the mention layer
- retained existing filenames where practical for continuity; authoritative mapping now lives in `data/places.json`
- flagged merged / contaminated inherited notes for later cleanup instead of forcing speculative repairs in this pass

Next:
- second-pass review of place files flagged for merged date spans, merged notes, or naming cleanup
- optional parent/child place hierarchy if city/address clustering becomes useful later
"""


def slugify(s: str) -> str:
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = s.lower().replace("&", " and ").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def clean_subsite(name: str | None) -> str:
    if not name:
        return ""
    return SUBSITE_NORMALIZATION.get(name, name)


def place_id(place: str) -> str:
    return f"place-{slugify(place)}"[:96]


def infer_place_class(place: str) -> str:
    parts = [p.strip() for p in place.split(",")]
    if re.match(r"^\d+\s", parts[0]):
        return "address"
    if len(parts) == 1:
        return "region"
    if parts[-1] == "USA" and len(parts) >= 3:
        return "locality"
    if parts[-1] in ("England", "France") and len(parts) >= 2:
        if parts[0] in ("Norfolk", "Normandy", "Essex", "Suffolk", "Bedfordshire", "Buckinghamshire", "Oxfordshire", "Scandinavia"):
            return "region"
        return "locality"
    return "place"


def previous_filename_map() -> dict[str, str]:
    if not PLACES_JSON.exists():
        return {}
    try:
        data = json.loads(PLACES_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for rec in data:
        if rec.get("canonicalName") and rec.get("filename"):
            out[rec["canonicalName"]] = rec["filename"]
    return out


def infer_filename(place: str, existing_name_map: dict[str, str], existing_files: set[str]) -> str:
    if place in KNOWN_FILENAME_MAP:
        return KNOWN_FILENAME_MAP[place]
    if place in existing_name_map:
        return existing_name_map[place]

    parts = [p.strip() for p in place.split(",")]
    candidates = [f"{slugify(place)}.md"]
    if parts[-1] in ("USA", "England", "France") and len(parts) > 1:
        candidates.append(f"{slugify(', '.join(parts[:-1]))}.md")
    if re.match(r"^\d+\s", parts[0]):
        candidates.append(f"{slugify(parts[0])}.md")
    if len(parts) >= 3 and parts[-1] == "USA":
        state = parts[-2]
        base = slugify(parts[0])
        candidates.extend([f"{base}.md", f"{base}-{STATE_ABBREV.get(state, slugify(state))}.md"])
    else:
        candidates.append(f"{slugify(parts[0])}.md")

    seen = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if candidate in existing_files:
            return candidate

    if re.match(r"^\d+\s", parts[0]):
        return f"{slugify(', '.join(parts[:-1] if parts[-1] in ('USA', 'England', 'France') else parts))}.md"
    if len(parts) >= 3 and parts[-1] == "USA":
        state = parts[-2]
        base = slugify(parts[0])
        return f"{base}-{STATE_ABBREV.get(state, slugify(state))}.md"
    return f"{slugify(parts[0])}.md"


def alias_list(place: str) -> list[str]:
    aliases = list(ALIASES_MAP.get(place, []))
    parts = [p.strip() for p in place.split(",")]
    if re.match(r"^\d+\s", parts[0]):
        aliases.append(parts[0])
    elif len(parts) >= 2 and parts[-1] in ("England", "France"):
        aliases.append(", ".join(parts[:-1]))
    elif len(parts) >= 3 and parts[-1] == "USA":
        aliases.append(f"{parts[0]}, {parts[-2].replace('Massachusetts','MA').replace('New York','NY').replace('Indiana','IN').replace('Oregon','OR').replace('Michigan','MI').replace('South Carolina','SC').replace('Missouri','MO')}")
    aliases = [a.strip() for a in aliases if a and a.strip() and a.strip() != place]
    deduped = []
    seen = set()
    for a in aliases:
        key = a.casefold()
        if key not in seen:
            seen.add(key)
            deduped.append(a)
    return deduped


def location_quality_flags(loc: dict) -> list[str]:
    flags: list[str] = []
    source_quote = loc.get("sourceQuote") or ""
    event_date = loc.get("eventDate") or ""
    if "||" in source_quote:
        flags.append("merged-source-note")
    if "|" in event_date:
        flags.append("merged-date-span")
    if str(loc.get("confidence", "")).lower() == "low":
        flags.append("low-geocode-confidence")
    if loc.get("siteName") and clean_subsite(loc.get("siteName")) != loc.get("siteName"):
        flags.append("subsite-name-normalized")
    return flags


def representative_coordinates(group: list[dict]) -> dict | None:
    coords = []
    for loc in group:
        try:
            lat = float(loc["lat"])
            lng = float(loc["lng"])
        except Exception:
            continue
        coords.append((lat, lng))
    if not coords:
        return None
    lat = round(statistics.median([c[0] for c in coords]), 6)
    lng = round(statistics.median([c[1] for c in coords]), 6)
    return {"lat": lat, "lng": lng}


def confidence_summary(group: list[dict]) -> str:
    vals = [str(loc.get("confidence") or "").strip() for loc in group if loc.get("confidence")]
    if not vals:
        return "unknown"
    counts = Counter(vals)
    if len(counts) == 1:
        return next(iter(counts))
    return "mixed (" + ", ".join(f"{k}:{v}" for k, v in counts.most_common()) + ")"


def geocode_basis_summary(group: list[dict]) -> str:
    vals = [str(loc.get("geocodeBasis") or "").strip() for loc in group if loc.get("geocodeBasis")]
    if not vals:
        return "unknown"
    counts = Counter(vals)
    return counts.most_common(1)[0][0]


def search_terms(place: str, aliases: list[str], sub_sites: list[str]) -> list[str]:
    terms = [place]
    terms.extend(aliases)
    terms.extend(sub_sites)
    parts = [p.strip() for p in place.split(",")]
    if parts:
        terms.append(parts[0])
    deduped = []
    seen = set()
    for t in terms:
        key = t.casefold()
        if key not in seen:
            seen.add(key)
            deduped.append(t)
    return deduped


def build_places(locations: list[dict], existing_name_map: dict[str, str], existing_files: set[str]) -> list[dict]:
    by_place: dict[str, list[dict]] = defaultdict(list)
    for loc in locations:
        by_place[loc["place"]].append(loc)

    places: list[dict] = []
    for canonical_name, group in sorted(by_place.items(), key=lambda kv: kv[0]):
        pid = place_id(canonical_name)
        for loc in group:
            loc["placeId"] = pid
            loc["siteNameNormalized"] = clean_subsite(loc.get("siteName"))
            loc["qualityFlags"] = location_quality_flags(loc)

        place_class = infer_place_class(canonical_name)
        raw_sub_sites = sorted({clean_subsite(loc.get("siteName")) for loc in group if clean_subsite(loc.get("siteName"))})
        if place_class == "address":
            first_segment = canonical_name.split(",")[0].strip()
            sub_sites = [s for s in raw_sub_sites if s != first_segment]
        else:
            sub_sites = raw_sub_sites
        aliases = alias_list(canonical_name)
        coords = representative_coordinates(group)

        flags: list[str] = []
        if any("merged-source-note" in loc["qualityFlags"] for loc in group):
            flags.append("contains merged inherited notes from source JSON; split or reverify in cleanup pass")
        if any("merged-date-span" in loc["qualityFlags"] for loc in group):
            flags.append("contains merged date spans / likely cross-generation contamination in at least one mention")
        if coords:
            distinct_coords = {(round(float(loc["lat"]), 4), round(float(loc["lng"]), 4)) for loc in group if loc.get("lat") is not None and loc.get("lng") is not None}
            if len(distinct_coords) > 1:
                flags.append("coordinates vary across mentions; representative coordinates are approximate")

        filename = infer_filename(canonical_name, existing_name_map, existing_files)
        if filename in existing_files and "-" not in filename.replace(".md", "") and canonical_name.endswith(", USA"):
            flags.append("filename retained for continuity; authoritative mapping now lives in data/places.json")

        place_record = {
            "placeId": pid,
            "canonicalName": canonical_name,
            "filename": filename,
            "placeClass": place_class,
            "region": Counter([loc.get("region") or "" for loc in group]).most_common(1)[0][0] if group else "",
            "aliases": aliases,
            "subSites": sub_sites,
            "representativeCoordinates": coords,
            "representativeGeocodeBasis": geocode_basis_summary(group),
            "confidenceSummary": confidence_summary(group),
            "locationIds": [loc["locationId"] for loc in group],
            "recordIds": sorted({loc["recordId"] for loc in group}),
            "recordLabels": sorted({f"{loc['recordGen']} {loc['recordName']}" for loc in group}),
            "searchTerms": search_terms(canonical_name, aliases, sub_sites),
            "reviewFlags": flags or ["none"],
        }
        places.append(place_record)
    return places


def annotate_ancestors(ancestors: list[dict], locations: list[dict]) -> list[dict]:
    place_refs_by_record: dict[str, list[str]] = defaultdict(list)
    for loc in locations:
        if loc.get("placeId"):
            place_refs_by_record[loc["recordId"]].append(loc["placeId"])
    out = []
    for rec in ancestors:
        rec2 = copy.deepcopy(rec)
        if rec2.get("type") in ("ancestor", "collateral"):
            rec2["placeRefs"] = sorted(dict.fromkeys(place_refs_by_record.get(rec2.get("recordId"), [])))
        out.append(rec2)
    return out


def format_links(loc: dict) -> str:
    links = []
    if loc.get("siteUrl"):
        label = loc.get("siteLabel") or loc.get("siteUrl")
        links.append(f"[{label}]({loc['siteUrl']})")
    if loc.get("photoUrl"):
        label = loc.get("photoTitle") or "photo"
        links.append(f"[{label}]({loc['photoUrl']})")
    return " · ".join(links)


def make_place_block(place: dict, mentions: list[dict]) -> str:
    lines: list[str] = []
    lines.append(NEW_GEN_START)
    lines.append("## Place registry")
    lines.append("")
    lines.append(f"- `placeId`: `{place['placeId']}`")
    lines.append(f"- Canonical filename: `{place['filename']}`")
    lines.append(f"- Place class: {place['placeClass']}")
    if place.get("aliases"):
        lines.append(f"- Aliases: {', '.join(place['aliases'])}")
    if place.get("subSites"):
        lines.append(f"- Sub-sites tracked here: {', '.join(place['subSites'])}")
    lines.append(f"- Mention count: **{len(mentions)}**")
    lines.append(f"- Linked records: {', '.join(place['recordLabels'])}")
    if place.get("representativeCoordinates"):
        coords = place["representativeCoordinates"]
        lines.append(f"- Representative coordinates: {coords['lat']}, {coords['lng']} ({place['representativeGeocodeBasis']}; {place['confidenceSummary']})")
    lines.append("")
    lines.append("### Mention ledger")
    lines.append("")
    for loc in sorted(mentions, key=lambda x: (x.get("recordGen") or "", x.get("recordName") or "", x.get("eventType") or "", x.get("eventDate") or "")):
        title = f"- `{loc['locationId']}` — **{loc['recordGen']} {loc['recordName']}** — {loc.get('eventType') or 'unspecified'}"
        if loc.get("eventDate"):
            title += f" — {loc['eventDate']}"
        lines.append(title)
        if loc.get("siteNameNormalized"):
            lines.append(f"  - Sub-site: {loc['siteNameNormalized']}")
        if loc.get("sourceQuote"):
            lines.append(f"  - Note: {loc['sourceQuote']}")
        if loc.get("qualityFlags"):
            lines.append(f"  - Flags: {', '.join(loc['qualityFlags'])}")
        links = format_links(loc)
        if links:
            lines.append(f"  - Links: {links}")
        lines.append("")
    lines.append("### Review notes")
    lines.append("")
    if place.get("reviewFlags") == ["none"]:
        lines.append("- None in normalization pass v1.")
    else:
        for flag in place["reviewFlags"]:
            lines.append(f"- {flag}")
    lines.append("")
    lines.append(NEW_GEN_END)
    return "\n".join(lines)


def remove_generated_blocks(text: str) -> str:
    patterns = [
        re.compile(re.escape(OLD_GEN_START) + r".*?" + re.escape(OLD_GEN_END), flags=re.DOTALL),
        re.compile(re.escape(NEW_GEN_START) + r".*?" + re.escape(NEW_GEN_END), flags=re.DOTALL),
    ]
    out = text
    for pat in patterns:
        out = pat.sub("", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip() + ("\n" if out.strip() else "")


def heading_name(text: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def is_generic_shell(text_without_generated: str, canonical_name: str) -> bool:
    generic_parts = [
        f"# {canonical_name}",
        "Structured place-memory file combining prior narrative research with extracted registry entries.",
        "## Genealogical significance",
        "This file now serves as the place-level aggregation point for structured location and landholding entries extracted from the ancestor registry. Narrative interpretation, source cleanup, negative-result research, and archival notes can be layered above or below the generated registry block over time.",
        "## Research notes",
        "- This file is intentionally compatible with a later normalization pass where multiple extracted registry entries can be merged into a canonical place record.",
        "- Formal `sourceId` linkage has not yet been imposed here. Inherited quotations and URLs are preserved to reduce loss during migration.",
    ]
    temp = text_without_generated
    for part in generic_parts:
        temp = temp.replace(part, "")
    temp = re.sub(r"\s+", "", temp)
    return temp == ""


def render_place_file(path: Path, canonical_name: str, block: str) -> str:
    if not path.exists():
        return f"# {canonical_name}\n\n{block}\n"
    existing = path.read_text(encoding="utf-8")
    stripped = remove_generated_blocks(existing)
    if is_generic_shell(stripped, canonical_name):
        return f"# {canonical_name}\n\n{block}\n"
    body = stripped.rstrip()
    if not body:
        return f"# {canonical_name}\n\n{block}\n"
    return body + "\n\n" + block + "\n"


def cleanup_stale_generated_files(target_files: set[str]) -> None:
    for path in PLACES_DIR.glob("*.md"):
        if path.name == "README.md" or path.name in target_files:
            continue
        existing = path.read_text(encoding="utf-8")
        stripped = remove_generated_blocks(existing)
        heading = heading_name(existing)
        if heading and is_generic_shell(stripped, heading):
            path.unlink()


def main() -> None:
    ancestors = json.loads(ANCESTORS_V24.read_text(encoding="utf-8"))
    locations = json.loads(LOCATIONS_JSON.read_text(encoding="utf-8"))

    existing_name_map = previous_filename_map()
    existing_files = {p.name for p in PLACES_DIR.glob("*.md") if p.name != "README.md"}

    places = build_places(locations, existing_name_map, existing_files)
    ancestors_out = annotate_ancestors(ancestors, locations)

    DATA_README.write_text(DATA_README_TEXT, encoding="utf-8")
    PLACES_README.write_text(PLACES_README_TEXT, encoding="utf-8")
    LOG_README.write_text(LOG_README_TEXT, encoding="utf-8")
    PLACES_JSON.write_text(json.dumps(places, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    LOCATIONS_JSON.write_text(
        json.dumps(
            sorted(locations, key=lambda x: (x["placeId"], x.get("recordGen") or "", x.get("recordName") or "", x.get("sourceLocationIndex", 0))),
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    ANCESTORS_V24.write_text(json.dumps(ancestors_out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    mentions_by_place: dict[str, list[dict]] = defaultdict(list)
    for loc in locations:
        mentions_by_place[loc["placeId"]].append(loc)

    target_files = {place["filename"] for place in places}
    for place in places:
        target = PLACES_DIR / place["filename"]
        block = make_place_block(place, mentions_by_place[place["placeId"]])
        content = render_place_file(target, place["canonicalName"], block)
        target.write_text(content, encoding="utf-8")

    cleanup_stale_generated_files(target_files)

    log_path = LOG_DIR / ATOMIC_LOG_NAME
    log_path.write_text(LOG_TEXT + "\n", encoding="utf-8")

    print(f"Wrote {PLACES_JSON.relative_to(ROOT)}")
    print(f"Updated {LOCATIONS_JSON.relative_to(ROOT)}")
    print(f"Updated {ANCESTORS_V24.relative_to(ROOT)}")
    print(f"Updated place files under {PLACES_DIR.relative_to(ROOT)}")
    print(f"Wrote {log_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
