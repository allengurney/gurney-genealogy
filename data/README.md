# data/

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
