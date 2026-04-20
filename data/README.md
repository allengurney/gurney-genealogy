# data/

Canonical structured data for the research-library spine.

## Files

- `ancestors v{XX}.json` where {xx} is the version number (V26 at the time of writing) — Ancestor registry with embedded location arrays.  USE THE LATEST VERSION - DO NOT USE OLDER VERSIONS.
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
