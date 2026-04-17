from __future__ import annotations

import copy
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PLACES_DIR = ROOT / "research" / "places"
LOG_DIR = ROOT / "research" / "log"

ANCESTORS_V23 = DATA_DIR / "ancestors v23.json"
ANCESTORS_V24 = DATA_DIR / "ancestors v24.json"
PLACES_JSON = DATA_DIR / "places.json"
PLACES_DETAIL_JSON = DATA_DIR / "places_detail.json"
LEGACY_LOCATIONS_JSON = DATA_DIR / "locations.json"
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

CANONICAL_PLACE_MAP = {
    "Abington/Whitman line, Massachusetts, USA": "Abington–Whitman line, Massachusetts, USA",
}

SUBSITE_NORMALIZATION = {
    "West Barsham Hall / manor site": "West Barsham Hall",
    "Collégiale Saint-Hildevert / historic centre": "Collégiale Saint-Hildevert",
    "Église Saint-Pierre-et-Saint-Paul / former core": "Église Saint-Pierre-et-Saint-Paul",
}

US_FILENAME_OVERRIDES = {
    "Braintree, Massachusetts, USA": "braintree-ma.md",
    "Weymouth, Massachusetts, USA": "weymouth-ma.md",
    "Flushing, Queens, New York, USA": "flushing-ny.md",
    "Port Washington, New York, USA": "port-washington-ny.md",
    "Portland, Oregon, USA": "portland-or.md",
    "Indianapolis, Indiana, USA": "indianapolis-in.md",
    "Marion, Indiana, USA": "marion-in.md",
    "Fort Wayne, Indiana, USA": "fort-wayne-in.md",
    "Dexter, Michigan, USA": "dexter-mi.md",
    "Charleston, South Carolina, USA": "charleston-sc.md",
    "St. Louis, Missouri, USA": "st-louis-mo.md",
    "New York metropolitan area, USA": "new-york-metropolitan-area-ny.md",
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
    "Hingham, Norfolk, England": "hingham-norfolk.md",
}
KNOWN_FILENAME_MAP.update(US_FILENAME_OVERRIDES)

DATA_README_TEXT = """# data/

Canonical structured data for the research-library spine.

## Files

- `ancestors v23.json` — legacy ancestor registry with embedded location arrays.
- `ancestors v24.json` — normalized ancestor registry with stable `recordId` values and `placeRefs`.
- `places.json` — primary canonical place registry. Lightweight and optimized for navigation, AI consumption, website tables, and joins.
- `places_detail.json` — supplemental place detail registry for map popups and richer site context.
- `master.json` — broader canonical person/source registry used elsewhere in the repo.
- `sources.json` — bibliography and citation registry.

## Geography model

Use a two-layer place model:

1. `places.json`
   - one row per canonical place
   - compact fields only
   - canonical filename, aliases, coordinate, place type, short description, and ancestor/place-role links

2. `places_detail.json`
   - one row per canonical place
   - supplemental fields only
   - long description, site / address detail, extant-status detail, selected image / heritage links, and normalization review notes

This is not a rigid relational database. Keep it small, navigable, and easy to join.

## Discipline

- `places.json` is the primary place spine.
- `places_detail.json` must not duplicate place datasets that already exist in `places.json`.
- Normalize multiple prior occurrences of the same place into one canonical record.
- Choose one best coordinate and one best precision level per place. Do not synthesize derivative coordinates.
- Keep rich narrative, citation discussion, and open questions in `research/places/*.md`.
"""

PLACES_README_TEXT = """# research/places/

Canonical place-memory files.

## Authority

`data/places.json` is the authoritative registry for:
- canonical place name
- `placeId`
- filename
- aliases
- coordinate
- place type
- ancestor/place-role links

`data/places_detail.json` carries the supplemental map/detail layer.

## File shape

Narrative place files may contain hand-written research plus one generated block bounded by:

- `<!-- GENERATED:PLACE-REGISTRY:START -->`
- `<!-- GENERATED:PLACE-REGISTRY:END -->`

Older extraction blocks are replaced during normalization.

## Current normalization discipline

- Preserve existing narrative research outside the generated block.
- Keep generated content concise.
- Keep sub-sites and street-address detail in `places_detail.json` unless the research clearly treats them as standalone places.
- Record unresolved cleanup items as review notes for pass 2.
- For U.S. place filenames, use a trailing two-letter state code even for pre-statehood places.
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
- which files were added, updated, renamed, or deleted
- what still needs review

Substantive research belongs in topical files (`people/`, `places/`, `topics/`), not in the log.
"""

LOG_TEXT = """# 2026-04-17 — place normalization v1

Refactored the geography model into a lighter two-file place spine.

Updated:
- `data/places.json` — lightweight canonical place spine
- `data/places_detail.json` — supplemental map/detail layer
- `data/ancestors v24.json` — normalized ancestor records with `placeRefs`
- `data/README.md` — revised lightweight place-spine model documented
- `research/places/README.md` — place/detail registry contract documented
- `research/log/README.md` — atomic log guidance retained
- `research/places/*.md` — generated blocks simplified to canonical place summaries

Removed / replaced:
- `data/locations.json` — retired in favor of a per-place detail layer
- mention-ledger style generated content in place files

Design decisions:
- flattened multiple occurrences of a place into one canonical record
- chose one best coordinate per place rather than synthesizing representative coordinates
- moved extant-status and richer map-popup content to `places_detail.json`
- standardized U.S. place filenames to include a trailing two-letter state code

Next:
- pass 2 cleanup of flagged place files
- review any renamed U.S. files for link/citation updates outside the generated block
"""


def slugify(value: str) -> str:
    value = value.replace("–", "-").replace("—", "-").replace("−", "-")
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.lower().replace("&", " and ").replace("'", "")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def clean_subsite(value: str | None) -> str:
    if not value:
        return ""
    return SUBSITE_NORMALIZATION.get(value, value)


def canonical_place_name(place: str) -> str:
    return CANONICAL_PLACE_MAP.get(place, place)


def place_id(place: str) -> str:
    return f"place-{slugify(place)}"[:96]


def record_id(rec: dict) -> str:
    rtype = rec.get("type", "record")
    gen = slugify(rec.get("gen", "no-gen"))
    name = slugify(rec.get("name") or rec.get("label") or rtype)
    return f"{rtype}-{gen}-{name}"[:120]


def infer_place_type(place: str) -> str:
    parts = [p.strip() for p in place.split(",")]
    head = parts[0] if parts else place
    if re.match(r"^\d+\s", head):
        return "address"
    if len(parts) == 1:
        return "region"
    if parts[-1] == "USA":
        return "locality"
    if parts[-1] in ("England", "France"):
        if head in ("Norfolk", "Normandy", "Essex", "Suffolk", "Bedfordshire", "Buckinghamshire", "Oxfordshire", "Scandinavia"):
            return "region"
        return "locality"
    return "place"


def alias_list(place: str) -> list[str]:
    aliases = list(ALIASES_MAP.get(place, []))
    parts = [p.strip() for p in place.split(",")]
    if re.match(r"^\d+\s", parts[0]):
        aliases.append(parts[0])
    elif len(parts) >= 2 and parts[-1] in ("England", "France"):
        aliases.append(", ".join(parts[:-1]))
    elif len(parts) >= 3 and parts[-1] == "USA":
        state = parts[-2]
        short = STATE_ABBREV.get(state)
        if short:
            aliases.append(f"{parts[0]}, {short.upper()}")
        if len(parts) >= 4:
            aliases.append(f"{parts[0]}, {parts[1]}")
    out = []
    seen = set()
    for alias in aliases:
        key = alias.casefold()
        if alias and alias != place and key not in seen:
            seen.add(key)
            out.append(alias)
    return out


def infer_filename(place: str) -> str:
    if place in KNOWN_FILENAME_MAP:
        return KNOWN_FILENAME_MAP[place]
    parts = [p.strip() for p in place.split(",")]
    if parts and parts[-1] == "USA":
        state = None
        for token in reversed(parts[:-1]):
            if token in STATE_ABBREV:
                state = token
                break
        base = slugify(parts[0])
        if state:
            return f"{base}-{STATE_ABBREV[state]}.md"
        return f"{base}-us.md"
    return f"{slugify(parts[0])}.md"


def legacy_filename_candidates(place: str, target: str) -> list[str]:
    parts = [p.strip() for p in place.split(",")]
    candidates = [f"{slugify(place)}.md"]
    if parts:
        candidates.append(f"{slugify(parts[0])}.md")
    if parts and parts[-1] in ("USA", "England", "France") and len(parts) > 1:
        candidates.append(f"{slugify(', '.join(parts[:-1]))}.md")
    out = []
    seen = set()
    for candidate in candidates:
        if candidate != target and candidate not in seen:
            seen.add(candidate)
            out.append(candidate)
    return out


def normalize_role(value: str | None) -> str:
    if not value:
        return "associated place"
    return value.strip()


def confidence_rank(value: str | None) -> int:
    text = (value or "").strip().lower()
    if text == "exact":
        return 40
    if text == "high":
        return 30
    if text == "medium":
        return 20
    if text == "low":
        return 10
    return 0


def precision_label(value: str | None, basis: str | None) -> str:
    basis_text = (basis or "").lower()
    conf = (value or "").strip().lower()
    if "exact" in basis_text or conf == "exact":
        return "exact"
    if conf in ("high", "medium", "low"):
        return conf
    if "approx" in basis_text or "anchor" in basis_text or "centre" in basis_text or "center" in basis_text:
        return "approximate"
    return "unknown"


def basis_rank(value: str | None) -> int:
    text = (value or "").lower()
    if "exact extant" in text:
        return 100
    if "exact abbey site" in text or "exact hall site" in text or "exact church site" in text:
        return 95
    if "exact" in text:
        return 90
    if "ruin" in text:
        return 85
    if "extant" in text:
        return 80
    if "historic site" in text or "former core" in text:
        return 70
    if "anchor" in text:
        return 60
    if "town centre" in text or "town center" in text or "village centre" in text or "village center" in text:
        return 45
    if "county" in text or "region" in text:
        return 20
    return 50 if text else 0


def choose_best_mention(mentions: list[dict]) -> dict:
    def score(item: dict) -> tuple:
        return (
            1 if item.get("lat") is not None and item.get("lng") is not None else 0,
            basis_rank(item.get("geocodeBasis")),
            confidence_rank(item.get("confidence")),
            1 if item.get("siteUrl") else 0,
            1 if item.get("photoUrl") else 0,
            len((item.get("sourceQuote") or "").split()),
        )
    return max(mentions, key=score)


def dedupe(values: list[str]) -> list[str]:
    out = []
    seen = set()
    for value in values:
        if not value:
            continue
        key = value.casefold()
        if key not in seen:
            seen.add(key)
            out.append(value)
    return out


def first_nonempty(values: list[str]) -> str:
    for value in values:
        if value:
            return value
    return ""


def truncate_words(text: str, max_words: int) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]).rstrip(",;:") + "…"


def clean_note(text: str) -> str:
    if not text:
        return ""
    text = text.replace("||", " | ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extant_status(mention: dict) -> str:
    combined = " ".join([mention.get("geocodeBasis") or "", mention.get("sourceQuote") or "", mention.get("siteName") or ""]).lower()
    if "ruin" in combined or "ruins" in combined:
        return "ruins"
    if "surviving" in combined or "extant" in combined or "still stands" in combined:
        return "extant"
    if "memorial" in combined:
        return "memorial"
    if "former" in combined or "site" in combined or "footprint" in combined or "boundary" in combined:
        return "site only"
    if "demolished" in combined or "lost" in combined or "no longer extant" in combined:
        return "lost"
    if "approx" in combined or "anchor" in combined or "town center" in combined or "town centre" in combined:
        return "approximate area"
    return "unknown"


def extant_status_description(mention: dict) -> str:
    quote = clean_note(mention.get("sourceQuote") or "")
    if quote:
        return truncate_words(quote, 28)
    basis = (mention.get("geocodeBasis") or "").strip()
    if basis:
        return basis[:1].upper() + basis[1:]
    return ""


def short_description(place_type: str, roles: list[str], primary: dict) -> str:
    subsite = clean_subsite(primary.get("siteName"))
    roles_lower = " | ".join(r.lower() for r in roles)
    if place_type == "address":
        return "Historic street address"
    if "landholding" in roles_lower and any(k in subsite.lower() for k in ("hall", "manor", "abbey", "estate")):
        return "Historic landholding site"
    if "landholding" in roles_lower:
        return "Ancestral landholding"
    if "residence" in roles_lower:
        return "Family residence site"
    if any(k in subsite.lower() for k in ("church", "chapel", "abbey", "collégiale", "eglise")):
        return "Historic ecclesiastical site"
    if "address reference" in roles_lower:
        return "Referenced street address"
    return "Associated ancestral place"


def long_description(primary: dict, short_desc: str) -> str:
    quote = clean_note(primary.get("sourceQuote") or "")
    if quote:
        return truncate_words(quote, 45)
    basis = primary.get("geocodeBasis") or ""
    site = clean_subsite(primary.get("siteName"))
    status_desc = extant_status_description(primary)
    parts = [short_desc]
    if site:
        parts.append(f"focused on {site}")
    if basis:
        parts.append(f"geocoded from {basis}")
    if status_desc:
        parts.append(status_desc)
    return truncate_words(". ".join(p for p in parts if p), 45)


def review_notes(mentions: list[dict]) -> list[str]:
    notes = []
    quotes = [m.get("sourceQuote") or "" for m in mentions]
    if any("||" in q for q in quotes):
        notes.append("Merged inherited note text detected; verify and split in pass 2 if needed.")
    if any("|" in (m.get("eventDate") or "") for m in mentions):
        notes.append("Merged date span detected; verify whether multiple generations were compressed together.")
    coords = {(m.get("lat"), m.get("lng")) for m in mentions if m.get("lat") is not None and m.get("lng") is not None}
    if len(coords) > 1:
        notes.append("Multiple coordinate candidates existed; normalized record uses the strongest single anchor.")
    site_names = dedupe([clean_subsite(m.get("siteName")) for m in mentions if clean_subsite(m.get("siteName"))])
    if len(site_names) > 1:
        notes.append("Multiple sub-site labels were merged under one canonical place.")
    return notes


def extract_mentions(records: list[dict]) -> tuple[list[dict], dict[str, str]]:
    mentions = []
    labels = {}
    for rec in records:
        rid = record_id(rec)
        if rec.get("type") in ("ancestor", "collateral"):
            labels[rid] = f"{rec.get('gen')} {rec.get('name')}"
            for idx, loc in enumerate(rec.get("locations") or []):
                place = canonical_place_name((loc.get("place") or "").strip())
                mentions.append(
                    {
                        "recordId": rid,
                        "recordGen": rec.get("gen"),
                        "recordName": rec.get("name"),
                        "place": place,
                        "role": normalize_role(loc.get("eventType")),
                        "eventDate": loc.get("eventDate") or "",
                        "siteName": clean_subsite(loc.get("siteName")),
                        "lat": loc.get("lat"),
                        "lng": loc.get("lng"),
                        "geocodeBasis": loc.get("geocodeBasis") or "",
                        "confidence": loc.get("confidence") or "",
                        "sourceQuote": loc.get("sourceQuote") or "",
                        "siteUrl": loc.get("siteUrl") or "",
                        "siteLabel": loc.get("siteLabel") or "",
                        "photoUrl": loc.get("photoUrl") or "",
                        "photoTitle": loc.get("photoTitle") or "",
                        "sourceIndex": idx,
                    }
                )
    return mentions, labels


def build_place_records(mentions: list[dict], labels: dict[str, str]) -> tuple[list[dict], list[dict], dict[str, list[str]]]:
    by_place = defaultdict(list)
    for mention in mentions:
        by_place[mention["place"]].append(mention)

    places = []
    details = []
    place_refs_by_record = defaultdict(list)

    for place_name in sorted(by_place):
        group = by_place[place_name]
        pid = place_id(place_name)
        primary = choose_best_mention(group)
        roles = dedupe([m["role"] for m in group if m.get("role")])
        ancestor_links = []
        seen_links = set()
        for mention in sorted(group, key=lambda m: (m["recordGen"] or "", m["recordName"] or "", m["role"] or "")):
            link = (mention["recordId"], mention["role"])
            if link not in seen_links:
                seen_links.add(link)
                ancestor_links.append({"recordId": mention["recordId"], "role": mention["role"]})
                place_refs_by_record[mention["recordId"]].append(pid)

        coords = None
        if primary.get("lat") is not None and primary.get("lng") is not None:
            coords = {"lat": primary["lat"], "lng": primary["lng"]}

        short_desc = short_description(infer_place_type(place_name), roles, primary)
        detail_desc = long_description(primary, short_desc)

        places.append(
            {
                "placeId": pid,
                "name": place_name,
                "aliases": alias_list(place_name),
                "shortDescription": short_desc,
                "placeType": infer_place_type(place_name),
                "coordinate": coords,
                "coordinatePrecision": precision_label(primary.get("confidence"), primary.get("geocodeBasis")),
                "roles": roles,
                "ancestorLinks": ancestor_links,
                "filename": infer_filename(place_name),
            }
        )

        street_address = place_name.split(",")[0].strip() if infer_place_type(place_name) == "address" else ""
        heritage_url = first_nonempty([m.get("siteUrl") for m in group if m.get("siteUrl")])
        heritage_label = first_nonempty([m.get("siteLabel") for m in group if m.get("siteUrl")]) if heritage_url else ""
        image_url = first_nonempty([m.get("photoUrl") for m in group if m.get("photoUrl")])
        image_title = first_nonempty([m.get("photoTitle") for m in group if m.get("photoUrl")]) if image_url else ""

        details.append(
            {
                "placeId": pid,
                "placeName": place_name,
                "longDescription": detail_desc,
                "siteName": first_nonempty([m.get("siteName") for m in group if m.get("siteName")]),
                "streetAddress": street_address,
                "extantStatus": extant_status(primary),
                "extantStatusDescription": extant_status_description(primary),
                "coordinateBasis": primary.get("geocodeBasis") or "",
                "imageUrl": image_url,
                "imageTitle": image_title,
                "heritageUrl": heritage_url,
                "heritageLabel": heritage_label,
                "reviewNotes": review_notes(group),
            }
        )

    for rid in list(place_refs_by_record):
        place_refs_by_record[rid] = dedupe(place_refs_by_record[rid])

    return places, details, place_refs_by_record


def normalize_ancestors(records: list[dict], place_refs_by_record: dict[str, list[str]]) -> list[dict]:
    out = []
    for rec in records:
        rec2 = copy.deepcopy(rec)
        rec2["recordId"] = record_id(rec)
        if rec2.get("type") in ("ancestor", "collateral"):
            rec2.pop("locations", None)
            rec2.pop("locationRefs", None)
            rec2["placeRefs"] = place_refs_by_record.get(rec2["recordId"], [])
        out.append(rec2)
    return out


def format_links(detail: dict) -> list[str]:
    links = []
    if detail.get("heritageUrl"):
        label = detail.get("heritageLabel") or detail["heritageUrl"]
        links.append(f"[{label}]({detail['heritageUrl']})")
    if detail.get("imageUrl"):
        label = detail.get("imageTitle") or "image"
        links.append(f"[{label}]({detail['imageUrl']})")
    return links


def make_place_block(place: dict, detail: dict, record_labels: dict[str, str]) -> str:
    lines = [NEW_GEN_START, "## Place registry", ""]
    lines.append(f"- `placeId`: `{place['placeId']}`")
    lines.append(f"- Short description: {place['shortDescription']}")
    lines.append(f"- Place type: {place['placeType']}")
    if place.get("aliases"):
        lines.append(f"- Aliases: {', '.join(place['aliases'])}")
    if place.get("coordinate"):
        coord = place["coordinate"]
        lines.append(f"- Coordinate: {coord['lat']}, {coord['lng']} ({place['coordinatePrecision']})")
    if place.get("roles"):
        lines.append(f"- Roles: {', '.join(place['roles'])}")
    if detail.get("siteName"):
        lines.append(f"- Site name: {detail['siteName']}")
    if detail.get("streetAddress"):
        lines.append(f"- Street address: {detail['streetAddress']}")
    if detail.get("longDescription"):
        lines.append(f"- Detail: {detail['longDescription']}")
    if detail.get("extantStatus"):
        status_line = f"- Current-site status: {detail['extantStatus']}"
        if detail.get("extantStatusDescription"):
            status_line += f" — {detail['extantStatusDescription']}"
        lines.append(status_line)
    links = format_links(detail)
    if links:
        lines.append(f"- Links: {' · '.join(links)}")
    lines.append("")
    lines.append("### Linked ancestors")
    lines.append("")
    for link in place.get("ancestorLinks", []):
        label = record_labels.get(link["recordId"], link["recordId"])
        lines.append(f"- {label} — {link['role']}")
    lines.append("")
    lines.append("### Review notes")
    lines.append("")
    notes = detail.get("reviewNotes") or []
    if not notes:
        lines.append("- None in normalization pass v1.")
    else:
        for note in notes:
            lines.append(f"- {note}")
    lines.append("")
    lines.append(NEW_GEN_END)
    return "\n".join(lines)


def remove_generated_blocks(text: str) -> str:
    patterns = [
        re.compile(re.escape(OLD_GEN_START) + r".*?" + re.escape(OLD_GEN_END), flags=re.DOTALL),
        re.compile(re.escape(NEW_GEN_START) + r".*?" + re.escape(NEW_GEN_END), flags=re.DOTALL),
    ]
    out = text
    for pattern in patterns:
        out = pattern.sub("", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip() + ("\n" if out.strip() else "")


def heading_name(text: str) -> str | None:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


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


def find_legacy_source(target_name: str, canonical_name: str) -> Path | None:
    for candidate_name in legacy_filename_candidates(canonical_name, target_name):
        candidate = PLACES_DIR / candidate_name
        if candidate.exists():
            return candidate
    return None


def render_place_file(target: Path, canonical_name: str, block: str) -> tuple[str, Path | None]:
    source = target
    legacy_source = None
    if not source.exists():
        legacy_source = find_legacy_source(target.name, canonical_name)
        if legacy_source:
            source = legacy_source
    if not source.exists():
        return f"# {canonical_name}\n\n{block}\n", legacy_source

    existing = source.read_text(encoding="utf-8")
    stripped = remove_generated_blocks(existing)
    if is_generic_shell(stripped, canonical_name):
        return f"# {canonical_name}\n\n{block}\n", legacy_source

    body = stripped.rstrip()
    if not body:
        return f"# {canonical_name}\n\n{block}\n", legacy_source
    return body + "\n\n" + block + "\n", legacy_source


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
    records = json.loads(ANCESTORS_V23.read_text(encoding="utf-8"))
    mentions, record_labels = extract_mentions(records)
    places, details, place_refs_by_record = build_place_records(mentions, record_labels)
    ancestors_v24 = normalize_ancestors(records, place_refs_by_record)

    DATA_README.write_text(DATA_README_TEXT, encoding="utf-8")
    PLACES_README.write_text(PLACES_README_TEXT, encoding="utf-8")
    LOG_README.write_text(LOG_README_TEXT, encoding="utf-8")
    PLACES_JSON.write_text(json.dumps(places, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    PLACES_DETAIL_JSON.write_text(json.dumps(details, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    ANCESTORS_V24.write_text(json.dumps(ancestors_v24, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if LEGACY_LOCATIONS_JSON.exists():
        LEGACY_LOCATIONS_JSON.unlink()

    detail_by_place = {detail["placeId"]: detail for detail in details}
    target_files = set()
    consumed_legacy = set()

    for place in places:
        target = PLACES_DIR / place["filename"]
        target_files.add(target.name)
        block = make_place_block(place, detail_by_place[place["placeId"]], record_labels)
        content, legacy_source = render_place_file(target, place["name"], block)
        target.write_text(content, encoding="utf-8")
        if legacy_source and legacy_source != target:
            consumed_legacy.add(legacy_source)

    for legacy in consumed_legacy:
        if legacy.exists():
            legacy.unlink()

    cleanup_stale_generated_files(target_files)

    log_path = LOG_DIR / ATOMIC_LOG_NAME
    log_path.write_text(LOG_TEXT + "\n", encoding="utf-8")

    print(f"Wrote {PLACES_JSON.relative_to(ROOT)}")
    print(f"Wrote {PLACES_DETAIL_JSON.relative_to(ROOT)}")
    print(f"Updated {ANCESTORS_V24.relative_to(ROOT)}")
    print(f"Updated place files under {PLACES_DIR.relative_to(ROOT)}")
    print(f"Wrote {log_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
