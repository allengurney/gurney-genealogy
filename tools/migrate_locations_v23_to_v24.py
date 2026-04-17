#!/usr/bin/env python3
from __future__ import annotations

import copy
import datetime as dt
import hashlib
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
PLACES_DIR = ROOT / "research" / "places"
LOG_DIR = ROOT / "research" / "log"

SOURCE_JSON = DATA_DIR / "ancestors v23.json"
TARGET_ANCESTORS = DATA_DIR / "ancestors v24.json"
TARGET_LOCATIONS = DATA_DIR / "locations.json"
DATA_README = DATA_DIR / "README.md"
PLACES_README = PLACES_DIR / "README.md"

GEN_START = "<!-- GENERATED:LOCATION-REGISTRY:START -->"
GEN_END = "<!-- GENERATED:LOCATION-REGISTRY:END -->"

KNOWN_PLACE_FILE_MAP = {
    'West Barsham, Norfolk, England':'west-barsham.md',
    'Gournay-en-Bray, Normandy, France':'gournay-en-bray.md',
    'Montigny-sur-Andelle, Normandy, France':'montigny-sur-andelle.md',
    'La Ferté-en-Bray, Normandy, France':'la-ferte-en-bray.md',
    'Le Bec-Hellouin, Normandy, France':'le-bec-hellouin.md',
    'Lessingham, Norfolk, England':'lessingham.md',
    'Harpley, Norfolk, England':'harpley.md',
    'Hardingham, Norfolk, England':'hardingham.md',
    'Runhall, Norfolk, England':'runhall.md',
    "King's Lynn, Norfolk, England":'kings-lynn.md',
    'Liston, Essex, England':'liston.md',
    'Fordham, Essex, England':'fordham.md',
    'Ardleigh, Essex, England':'ardleigh.md',
    'Suffolk, England':'suffolk.md',
    'Lewes, Sussex, England':'lewes.md',
    'Caister-on-Sea, Norfolk, England':'caister-on-sea.md',
    'Cantley, Norfolk, England':'cantley.md',
    'Braintree, Massachusetts, USA':'braintree-ma.md',
    'Hingham, Norfolk, England':'hingham-norfolk.md',
    'Weymouth, Massachusetts, USA':'weymouth.md',
}
STATE_ABBREV = {
    'Massachusetts':'ma','New York':'ny','Indiana':'in','Oregon':'or',
    'Michigan':'mi','South Carolina':'sc','Missouri':'mo'
}

DATA_README_TEXT = """# data/

Canonical structured data. Preserve source fidelity first; normalize second.

## Files

- `ancestors v23.json` — pre-migration ancestor registry with embedded `locations` arrays.
- `ancestors v24.json` — same registry after extraction. Embedded `locations` removed from ancestor/collateral records and replaced with `locationRefs`.
- `locations.json` — lossless extracted location registry. One entry per former embedded location object.
- `master.json` — canonical person/source registry used by the broader research system.
- `sources.json` — bibliography and citation registry.

## Extraction model

Current phase uses a **lossless extraction** model rather than a deduplicated place registry.

Each extracted entry in `locations.json` preserves:
- original place/site/event/geocode fields
- provenance back to the source record in `ancestors v23.json`
- `locationId` for stable cross-reference
- `canonicalPlaceKey` / `placeSlug` fields to prepare for a later normalization pass

Each ancestor/collateral record in `ancestors v24.json` preserves the original record shape except:
- `locations` removed
- `locationRefs` added
- `recordId` added for stable joins

## Discipline

- Do not edit `ancestors v23.json` except to preserve history.
- Use `ancestors v24.json` + `locations.json` as the active bridge layer until a later normalization pass produces a true shared place registry.
- Preserve inherited citation text even when it is incomplete. Formal `sourceId` cleanup is a later task.
"""

PLACES_README_TEXT = """# research/places/

Place files are the durable research-memory layer for geography, landholdings, and site-specific context.

## Naming

- Prefer stable kebab-case filenames.
- Reuse established filenames when already present.
- Use geographic disambiguation only when needed (`braintree-ma.md`, `hingham-norfolk.md`).

## Structure

Each place file may now contain two layers:

1. Narrative research sections maintained manually.
2. A generated block bounded by:
   - `<!-- GENERATED:LOCATION-REGISTRY:START -->`
   - `<!-- GENERATED:LOCATION-REGISTRY:END -->`

The generated block is populated from `data/locations.json`-compatible extracted entries.

## Current migration discipline

- Preserve existing narrative research when updating a file.
- Replace only the generated block when regenerating.
- If a place has no prior file, create a minimal file with the generated block plus a short research-notes section.
- Preserve inherited quotations, URLs, and note text exactly unless a separate source-cleanup task is underway.
"""

LOG_SECTION = """
## {date} — location extraction v23 → v24 (embedded locations split out)

Converted embedded ancestor-location data into a bridge-layer registry.

Added / updated:
- `data/locations.json` — NEW lossless extracted location registry
- `data/ancestors v24.json` — NEW ancestor registry with `recordId` + `locationRefs`
- `data/README.md` — extraction model documented
- `research/places/README.md` — generated-block contract documented
- `research/places/*.md` — structured location registry blocks created or refreshed for place files referenced by extracted entries

Design notes:
- Chose Option A lossless extraction for fidelity and lower migration risk.
- Added `canonicalPlaceKey` and `placeSlug` to each extracted location entry to reduce friction for a later Option B normalization pass.
- Preserved inherited citation text / URLs verbatim where present; no `sourceId` normalization attempted in this step.

Next:
- Resolve duplicate or overlapping place files created by naming drift, if any.
- Normalize extracted entries into a shared place registry once citation cleanup rules are agreed.
""".strip()


def slugify(s: str) -> str:
    s = s.replace('–', '-').replace('—', '-').replace('−', '-')
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = s.lower().replace('&', ' and ').replace("'", '')
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s


def record_id(rec: dict) -> str:
    rtype = rec.get('type', 'record')
    gen = slugify(rec.get('gen', 'no-gen'))
    name = slugify(rec.get('name') or rec.get('label') or rtype)
    return f"{rtype}-{gen}-{name}"[:120]


def place_to_filename(place: str) -> str:
    if place in KNOWN_PLACE_FILE_MAP:
        return KNOWN_PLACE_FILE_MAP[place]
    parts = [p.strip() for p in place.split(',')]
    if len(parts) >= 3 and parts[-1] == 'USA':
        state = parts[-2]
        if re.search(r'\d', parts[0]):
            return f"{slugify(', '.join(parts[:-1]))}.md"
        if 'metropolitan area' in parts[0].lower():
            return f"{slugify(parts[0])}.md"
        if len(parts) >= 4 and parts[1] in ('Queens', 'Manhattan'):
            return f"{slugify(parts[0])}-{STATE_ABBREV.get(state, slugify(state))}.md"
        if parts[0] in ('Port Washington', 'Fort Wayne', 'Portland', 'Indianapolis', 'St. Louis', 'Dexter', 'Charleston', 'Marion', 'Mendon', 'Flushing'):
            return f"{slugify(parts[0])}-{STATE_ABBREV.get(state, slugify(state))}.md"
        if parts[0].startswith('Abington'):
            return f"{slugify(parts[0])}-{STATE_ABBREV.get(state, slugify(state))}.md"
        return f"{slugify(parts[0])}.md"
    if len(parts) >= 2 and parts[-1] == 'England':
        return f"{slugify(parts[0])}.md"
    if len(parts) >= 2 and parts[-1] == 'France':
        return f"{slugify(parts[0])}.md"
    return f"{slugify(place)}.md"


def source_status(loc: dict) -> str:
    has_explicit = bool(loc.get('siteUrl') or loc.get('siteLabel'))
    quote = loc.get('sourceQuote', '')
    if any(x in quote for x in ('DG Record', 'NEHGR', 'Plym.', 'Hist. of', 'Blomefield', 'History of Parliament', 'Domesday', 'charter', 'will', 'deed', 'Reg.', 'GS film', 'p.')):
        has_explicit = True
    return 'explicit citation text present in inherited note' if has_explicit else 'no formal citation preserved in source JSON; inherited note retained verbatim'


def make_location_block(locs: list[dict]) -> str:
    lines: list[str] = []
    linked = sorted({f"{l['recordGen']} {l['recordName']}" for l in locs})
    lines.append(GEN_START)
    lines.append("## Structured location registry")
    lines.append("")
    lines.append("Derived from `data/ancestors v23.json` and intended as the bridge layer to `data/locations.json` / `data/ancestors v24.json`.")
    lines.append("")
    lines.append("### Place summary")
    lines.append("")
    lines.append(f"- Registry entries: **{len(locs)}**")
    lines.append(f"- Linked records: {', '.join(linked)}")
    if any(l.get('siteName') for l in locs):
        sites = sorted({l['siteName'] for l in locs if l.get('siteName')})
        lines.append(f"- Named sub-sites: {', '.join(sites)}")
    lines.append("")
    lines.append("### Registry entries")
    lines.append("")
    for l in sorted(locs, key=lambda x: (x.get('recordGen') or '', x.get('recordName') or '', x.get('eventType') or '', x.get('eventDate') or '')):
        lines.append(f"#### {l['recordGen']} {l['recordName']} — {l.get('eventType', 'unspecified')}")
        lines.append("")
        lines.append(f"- `locationId`: `{l['locationId']}`")
        lines.append(f"- `recordId`: `{l['recordId']}`")
        lines.append(f"- `eventDate`: {l.get('eventDate') or '—'}")
        if l.get('siteName'):
            lines.append(f"- `siteName`: {l['siteName']}")
        lines.append(f"- `region`: {l.get('region') or '—'}")
        lines.append(f"- `coordinates`: {l.get('lat')}, {l.get('lng')}")
        lines.append(f"- `geocodeBasis`: {l.get('geocodeBasis') or '—'}")
        lines.append(f"- `confidence`: {l.get('confidence') or '—'}")
        lines.append(f"- Source / citation status: {source_status(l)}")
        if l.get('sourceQuote'):
            lines.append(f"- Inherited note / quote: {l['sourceQuote']}")
        if l.get('siteUrl'):
            label = l.get('siteLabel') or l['siteUrl']
            lines.append(f"- External reference: [{label}]({l['siteUrl']})")
        if l.get('photoUrl'):
            label = l.get('photoTitle') or 'Photo'
            lines.append(f"- Media reference: [{label}]({l['photoUrl']})")
        lines.append("")
    lines.append("### Crosslinks")
    lines.append("")
    for rec in linked:
        gen, name = rec.split(' ', 1)
        lines.append(f"- `data/ancestors v24.json` → `{gen}` / `{name}`")
    lines.append("")
    lines.append(GEN_END)
    return "\n".join(lines)


def make_place_file(place: str, locs: list[dict]) -> str:
    return "\n".join([
        f"# {place}",
        "",
        "Structured place-memory file combining prior narrative research with extracted registry entries.",
        "",
        "## Genealogical significance",
        "",
        "This file now serves as the place-level aggregation point for structured location and landholding entries extracted from the ancestor registry. Narrative interpretation, source cleanup, negative-result research, and archival notes can be layered above or below the generated registry block over time.",
        "",
        make_location_block(locs),
        "",
        "## Research notes",
        "",
        "- This file is intentionally compatible with a later normalization pass where multiple extracted registry entries can be merged into a canonical place record.",
        "- Formal `sourceId` linkage has not yet been imposed here. Inherited quotations and URLs are preserved to reduce loss during migration.",
        "",
    ])


def replace_or_append_generated_block(existing: str, new_block: str) -> str:
    pattern = re.compile(re.escape(GEN_START) + r'.*?' + re.escape(GEN_END), flags=re.DOTALL)
    if pattern.search(existing):
        return pattern.sub(new_block, existing)
    existing = existing.rstrip() + "\n\n"
    return existing + new_block + "\n"


def main() -> None:
    with SOURCE_JSON.open('r', encoding='utf-8') as f:
        records = json.load(f)

    ancestors_v24: list[dict] = []
    all_locations: list[dict] = []

    for rec in records:
        rec2 = copy.deepcopy(rec)
        rec2['recordId'] = record_id(rec)
        if rec.get('type') in ('ancestor', 'collateral'):
            refs: list[str] = []
            for idx, loc in enumerate(rec.get('locations', []) or []):
                key = f"{rec2['recordId']}|{idx}|{loc.get('place', '')}|{loc.get('eventType', '')}|{loc.get('eventDate', '')}"
                lid = 'loc-' + hashlib.sha1(key.encode('utf-8')).hexdigest()[:12]
                refs.append(lid)
                locrec = {
                    'locationId': lid,
                    'recordId': rec2['recordId'],
                    'recordType': rec.get('type'),
                    'recordGen': rec.get('gen'),
                    'recordName': rec.get('name'),
                    'placeSlug': slugify(loc.get('place', '')),
                    'canonicalPlaceKey': slugify(loc.get('place', '').strip()),
                    'sourceFile': 'data/ancestors v23.json',
                    'sourceRecordName': rec.get('name'),
                    'sourceLocationIndex': idx,
                    'origin': 'extracted-from-embedded-locations',
                }
                locrec.update(loc)
                all_locations.append(locrec)
            rec2.pop('locations', None)
            rec2['locationRefs'] = refs
        ancestors_v24.append(rec2)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PLACES_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    TARGET_ANCESTORS.write_text(json.dumps(ancestors_v24, indent=2, ensure_ascii=False) + "\n", encoding='utf-8')
    TARGET_LOCATIONS.write_text(
        json.dumps(sorted(all_locations, key=lambda x: (x['place'], x.get('recordGen') or '', x.get('recordName') or '', x.get('sourceLocationIndex', 0))), indent=2, ensure_ascii=False) + "\n",
        encoding='utf-8',
    )
    DATA_README.write_text(DATA_README_TEXT, encoding='utf-8')
    PLACES_README.write_text(PLACES_README_TEXT, encoding='utf-8')

    place_groups: dict[str, list[dict]] = defaultdict(list)
    for loc in all_locations:
        place_groups[loc['canonicalPlaceKey']].append(loc)

    for locs in place_groups.values():
        place = locs[0]['place']
        target = PLACES_DIR / place_to_filename(place)
        generated_block = make_location_block(locs)
        if target.exists():
            existing = target.read_text(encoding='utf-8')
            updated = replace_or_append_generated_block(existing, generated_block)
        else:
            updated = make_place_file(place, locs)
        target.write_text(updated, encoding='utf-8')

    today = dt.date.today().isoformat()
    log_path = LOG_DIR / f"{today}.md"
    section = LOG_SECTION.format(date=today)
    if log_path.exists():
        current = log_path.read_text(encoding='utf-8')
        if section not in current:
            log_path.write_text(current.rstrip() + "\n\n" + section + "\n", encoding='utf-8')
    else:
        log_path.write_text(f"# {today}\n\n{section}\n", encoding='utf-8')

    print(f"Wrote {TARGET_ANCESTORS.relative_to(ROOT)}")
    print(f"Wrote {TARGET_LOCATIONS.relative_to(ROOT)}")
    print(f"Updated {DATA_README.relative_to(ROOT)}")
    print(f"Updated {PLACES_README.relative_to(ROOT)}")
    print(f"Updated {len(place_groups)} place files")
    print(f"Updated {log_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
