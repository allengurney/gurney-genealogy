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

ATOMIC_LOG_NAME = "2026-04-17--place-normalization-pass2.md"

STATE_ABBREV = {
    "Massachusetts": "ma",
    "New York": "ny",
    "Indiana": "in",
    "Oregon": "or",
    "Michigan": "mi",
    "South Carolina": "sc",
    "Missouri": "mo",
}

ROLE_ORDER = {
    "landholding / property reference": 10,
    "residence": 20,
    "address reference": 30,
    "individual geography": 40,
    "associated place": 90,
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

PASS2_OVERRIDES = {
    "West Barsham, Norfolk, England": {
        "shortDescription": "Principal family seat",
        "longDescription": "Principal Gurney family seat from 1372 until Francis Gurney sold the Norfolk lands in 1634.",
        "extantStatus": "extant",
        "extantStatusDescription": "Surviving north wing of West Barsham Hall still marks the historic manor site.",
        "reviewNotes": [],
        "removeAncestorLinks": [("ancestor-g-37-eudes-odon-de-gournay", "landholding / property reference")],
    },
    "Gournay-en-Bray, Normandy, France": {
        "shortDescription": "Ancestral fortress town",
        "longDescription": "Ancestral fortress town and seigneury of the Gournay family in the Pays de Bray.",
        "extantStatus": "extant",
        "extantStatusDescription": "Modern town survives; the church site is used as the best historic anchor for the lost fortress town.",
        "reviewNotes": [],
    },
    "City of London, England": {
        "shortDescription": "Historic commercial site",
        "longDescription": "City of London commercial context linked to St Benet Fink parish and the La Selde Coronata warehouse tradition.",
        "extantStatus": "site only",
        "extantStatusDescription": "St Benet Fink church is lost; the historic site lies within the modern Bank of England east-wing area.",
        "reviewNotes": ["City-level record aggregates more than one London sub-site; keep the narrative file for separation."],
    },
    "King's Lynn, Norfolk, England": {
        "longDescription": "St James's Chapel site in King's Lynn, leased for a failed textile-manufacture venture in the early seventeenth century.",
        "extantStatusDescription": "Ruins of St James's Chapel survive and provide the historic site anchor.",
        "reviewNotes": [],
    },
    "Harpley, Norfolk, England": {
        "longDescription": "Gurney's manor in Harpley, acquired c.1183 through Rose de Burnham and the Hameline de Warenne connection.",
        "reviewNotes": [],
    },
    "Hardingham, Norfolk, England": {
        "longDescription": "Swathings in Hardingham, a long-running junior-line holding documented from the Henry II period onward.",
        "reviewNotes": [],
    },
    "Hingham, Norfolk, England": {
        "longDescription": "Manor of Hingham-Gurneys, an ancient junior-line holding later held of the Bardolf and Morley interests.",
        "reviewNotes": [],
    },
    "Irstead, Norfolk, England": {
        "longDescription": "Irstead manor, a primary documented later junior-line holding in Norfolk.",
        "reviewNotes": [],
    },
    "Great Ellingham, Norfolk, England": {
        "longDescription": "Great Ellingham manor, later associated with the Lovell inheritance through Margaret Lovell.",
        "reviewNotes": [],
    },
    "Braintree, Massachusetts, USA": {
        "longDescription": "Massachusetts town where immigrant John Gurney held land, including acreage noted in his possession in 1653, and sold property in 1661.",
        "reviewNotes": ["Possession versus ownership should stay explicit in later source cleanup."],
    },
    "Weymouth, Massachusetts, USA": {
        "longDescription": "Early Massachusetts grants in Weymouth included the East Field, Mill Field, and land near Great Pond.",
        "reviewNotes": ["Town-level record aggregates multiple field and pond-side grants rather than a single parcel."],
    },
    "Bridgewater, Massachusetts, USA": {
        "longDescription": "Bridgewater-area holdings tied to the Benjamin/Richard Gurney line, including the Richard Williams farm and other town-level parcel references.",
        "reviewNotes": ["Town-level record aggregates multiple parcels and named sub-places; parcel-level cleanup remains possible."],
    },
    "Cummington, Massachusetts, USA": {
        "longDescription": "Cummington farm holdings associated with the Benjamin/Amos Gurney family after their move from Abington.",
        "reviewNotes": ["Town-level record aggregates several family-era parcels and later cemetery context."],
    },
    "Flushing, Queens, New York, USA": {
        "longDescription": "Probable residential base of the Willis/William Gurney family before later Manhattan addresses; ownership versus rental remains unresolved.",
        "reviewNotes": ["Residence versus ownership status remains unresolved and should be revisited with directory and property work."],
    },
    "Middleborough, Massachusetts, USA": {
        "longDescription": "Middleborough land purchases and later sales associated with the Benjamin Gurney family in the 1730s and 1740s.",
        "reviewNotes": ["Town-level record aggregates multiple deeded parcels."],
    },
    "Norfolk, England": {
        "shortDescription": "County-level holdings context",
        "longDescription": "County-level umbrella record for dispersed Norfolk holdings; use individual manor and village files for site-specific work.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
    },
    "Normandy, France": {
        "shortDescription": "Regional holdings context",
        "longDescription": "Regional umbrella record for Norman holdings and priory contexts not yet assigned to a tighter single place.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
    },
    "Oxfordshire, England": {
        "shortDescription": "Regional holdings context",
        "longDescription": "County-level umbrella record for scattered Oxfordshire holdings documented in royal and exchequer records.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
    },
    "New York metropolitan area, USA": {
        "shortDescription": "Regional family geography",
        "longDescription": "Regional umbrella record for the family's broader New York-area geography before and beyond specific city addresses.",
        "reviewNotes": ["Regional umbrella record, not a single site."],
    },
    "Scandinavia": {
        "longDescription": "Broad Scandinavian origin context, more specifically Denmark or Norway, without a tighter attested locality.",
        "reviewNotes": ["Origin-region record only; no tighter locality is established yet."],
    },
}

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
- Record unresolved cleanup items as review notes only when they still matter after cleanup.
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

LOG_TEXT = """# 2026-04-17 — place normalization pass 2

Second cleanup pass on the normalized place spine.

Updated:
- `data/places.json` — cleaned short descriptions, roles ordering, and ancestor links for selected places
- `data/places_detail.json` — cleaned long descriptions, extant-status descriptions, and review notes
- `data/ancestors v24.json` — place refs regenerated from the cleaned canonical place set
- `research/places/*.md` — generated blocks refreshed with cleaner linked-ancestor summaries and reduced noise

Key cleanup actions:
- removed the incorrect West Barsham landholding link from G37 Eudes
- replaced merged/concatenated popup text for high-value places with cleaned canonical descriptions
- converted several remaining records into explicit town-level or region-level umbrella notes where appropriate
- suppressed review notes that no longer added value after cleanup

Remaining follow-up:
- optional deeper parcel-level split for some Massachusetts town records if needed later
- optional future separation of City of London and Normandy sub-sites if those become first-class research objects
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


def is_merged_field(value: str | None) -> bool:
    text = value or ""
    return "|" in text or "||" in text


def split_fragments(value: str | None) -> list[str]:
    text = value or ""
    if not text:
        return []
    parts = [p.strip(" .") for p in re.split(r"\s*\|\|?\s*", text) if p.strip()]
    return parts


def choose_best_mention(mentions: list[dict]) -> dict:
    def score(item: dict) -> tuple:
        return (
            1 if item.get("lat") is not None and item.get("lng") is not None else 0,
            1 if not is_merged_field(item.get("sourceQuote")) else 0,
            1 if not is_merged_field(item.get("eventDate")) else 0,
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


def sort_roles(values: list[str]) -> list[str]:
    return sorted(values, key=lambda v: (ROLE_ORDER.get(v, 80), v))


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
    text = re.sub(r"\s+", " ", text).strip()
    return text


def best_quote_for_place(mentions: list[dict]) -> str:
    clean_quotes = []
    for mention in mentions:
        quote = mention.get("sourceQuote") or ""
        if quote and not is_merged_field(quote):
            clean_quotes.append(clean_note(quote))
    if clean_quotes:
        return max(clean_quotes, key=lambda q: len(q.split()))
    fragments = []
    for mention in mentions:
        fragments.extend(split_fragments(mention.get("sourceQuote")))
    if fragments:
        return max((clean_note(f) for f in fragments), key=lambda q: len(q.split()))
    return ""


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


def extant_status_description(mention: dict, status: str) -> str:
    if status == "unknown":
        return ""
    quote = best_quote_for_place([mention])
    if quote:
        return truncate_words(quote, 22)
    basis = (mention.get("geocodeBasis") or "").strip()
    if basis:
        return basis[:1].upper() + basis[1:]
    return ""


def short_description(place_name: str, place_type: str, roles: list[str], primary: dict) -> str:
    subsite = clean_subsite(primary.get("siteName"))
    roles_lower = " | ".join(r.lower() for r in roles)
    if place_name in PASS2_OVERRIDES and PASS2_OVERRIDES[place_name].get("shortDescription"):
        return PASS2_OVERRIDES[place_name]["shortDescription"]
    if place_type == "address":
        return "Historic street address"
    if place_type == "region":
        return "Regional holdings context"
    if "landholding" in roles_lower and any(k in subsite.lower() for k in ("hall", "manor", "abbey", "estate", "fortress")):
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


def generic_long_description(place_name: str, place_type: str, mentions: list[dict], primary: dict, short_desc: str) -> str:
    override = PASS2_OVERRIDES.get(place_name, {})
    if override.get("longDescription"):
        return override["longDescription"]
    quote = best_quote_for_place(mentions)
    if quote:
        return truncate_words(quote, 36)
    basis = primary.get("geocodeBasis") or ""
    site = clean_subsite(primary.get("siteName"))
    if place_type == "address":
        return primary.get("place") or place_name
    parts = [short_desc]
    if site:
        parts.append(site)
    if basis:
        parts.append(basis)
    return truncate_words(" — ".join(p for p in parts if p), 28)


def review_notes(place_name: str, place_type: str, mentions: list[dict]) -> list[str]:
    override = PASS2_OVERRIDES.get(place_name, {})
    if "reviewNotes" in override:
        return override["reviewNotes"]
    notes = []
    site_names = dedupe([clean_subsite(m.get("siteName")) for m in mentions if clean_subsite(m.get("siteName"))])
    if place_type == "region":
        notes.append("Regional umbrella record, not a single site.")
    elif place_type == "locality" and len(site_names) > 1:
        notes.append("Multiple sub-site labels are still grouped under one canonical place.")
    if not best_quote_for_place(mentions) and any(is_merged_field(m.get("sourceQuote")) for m in mentions):
        notes.append("Source JSON still preserves merged chronology fragments; use the narrative place file for nuance.")
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


def apply_link_cleanup(place_name: str, group: list[dict]) -> list[dict]:
    removals = set(PASS2_OVERRIDES.get(place_name, {}).get("removeAncestorLinks", []))
    if not removals:
        return group
    return [m for m in group if (m["recordId"], m["role"]) not in removals]


def build_place_records(mentions: list[dict]) -> tuple[list[dict], list[dict], dict[str, list[str]]]:
    by_place = defaultdict(list)
    for mention in mentions:
        by_place[mention["place"]].append(mention)

    places = []
    details = []
    place_refs_by_record = defaultdict(list)

    for place_name in sorted(by_place):
        group = apply_link_cleanup(place_name, by_place[place_name])
        if not group:
            continue
        pid = place_id(place_name)
        place_type = infer_place_type(place_name)
        primary = choose_best_mention(group)
        roles = sort_roles(dedupe([m["role"] for m in group if m.get("role")]))

        ancestor_links = []
        seen_links = set()
        for mention in sorted(group, key=lambda m: (m["recordGen"] or "", m["recordName"] or "", ROLE_ORDER.get(m["role"], 80), m["role"])):
            link = (mention["recordId"], mention["role"])
            if link not in seen_links:
                seen_links.add(link)
                ancestor_links.append({"recordId": mention["recordId"], "role": mention["role"]})
                place_refs_by_record[mention["recordId"]].append(pid)

        coords = None
        if primary.get("lat") is not None and primary.get("lng") is not None:
            coords = {"lat": primary["lat"], "lng": primary["lng"]}

        short_desc = short_description(place_name, place_type, roles, primary)
        detail_desc = generic_long_description(place_name, place_type, group, primary, short_desc)
        status = PASS2_OVERRIDES.get(place_name, {}).get("extantStatus") or extant_status(primary)
        status_desc = PASS2_OVERRIDES.get(place_name, {}).get("extantStatusDescription")
        if status_desc is None:
            status_desc = extant_status_description(primary, status)

        heritage_url = first_nonempty([m.get("siteUrl") for m in group if m.get("siteUrl")])
        heritage_label = first_nonempty([m.get("siteLabel") for m in group if m.get("siteUrl")]) if heritage_url else ""
        image_url = first_nonempty([m.get("photoUrl") for m in group if m.get("photoUrl")])
        image_title = first_nonempty([m.get("photoTitle") for m in group if m.get("photoUrl")]) if image_url else ""
        site_name = PASS2_OVERRIDES.get(place_name, {}).get("siteName")
        if site_name is None:
            site_name = first_nonempty([m.get("siteName") for m in group if m.get("siteName")])

        places.append(
            {
                "placeId": pid,
                "name": place_name,
                "aliases": alias_list(place_name),
                "shortDescription": short_desc,
                "placeType": place_type,
                "coordinate": coords,
                "coordinatePrecision": precision_label(primary.get("confidence"), primary.get("geocodeBasis")),
                "roles": roles,
                "ancestorLinks": ancestor_links,
                "filename": infer_filename(place_name),
            }
        )

        street_address = place_name.split(",")[0].strip() if place_type == "address" else ""
        details.append(
            {
                "placeId": pid,
                "placeName": place_name,
                "longDescription": detail_desc,
                "siteName": site_name,
                "streetAddress": street_address,
                "extantStatus": status,
                "extantStatusDescription": status_desc,
                "coordinateBasis": primary.get("geocodeBasis") or "",
                "imageUrl": image_url,
                "imageTitle": image_title,
                "heritageUrl": heritage_url,
                "heritageLabel": heritage_label,
                "reviewNotes": review_notes(place_name, place_type, group),
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
    if detail.get("extantStatus") and detail['extantStatus'] != "unknown":
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
    grouped = defaultdict(list)
    for link in place.get("ancestorLinks", []):
        grouped[link["recordId"]].append(link["role"])
    for record_id_key, roles in sorted(grouped.items(), key=lambda kv: record_labels.get(kv[0], kv[0])):
        label = record_labels.get(record_id_key, record_id_key)
        lines.append(f"- {label} — {', '.join(sort_roles(dedupe(roles)))}")
    lines.append("")
    lines.append("### Review notes")
    lines.append("")
    notes = detail.get("reviewNotes") or []
    if not notes:
        lines.append("- None in cleanup pass 2.")
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
    places, details, place_refs_by_record = build_place_records(mentions)
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
