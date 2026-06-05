# research/places/

Canonical place-memory files.

## Authority split
- `data/places.json` — canonical place registry
- `data/places_detail.json` — supplemental detail layer
- `research/places/*.md` — narrative place research and interpretive context

## Wiring a place into the site (both sides required)
A fully rendered place needs four pieces:
1. `data/places.json` — registry entry (coordinate, roles, `ancestorLinks`).
2. `data/places_detail.json` — matching detail row (same `placeId`).
3. `research/places/<filename>.md` — companion matching the entry's `filename`.
4. `data/ancestors.json` — the `placeId` added to each linked ancestor's `placeRefs`.

The ancestor link is **bidirectional**: `ancestorLinks` (in `places.json`) drives the website places catalog and place pages; `placeRefs` (in `ancestors.json`) drives the ancestor's map markers in the pedigree drawer and ancestor map. Write both sides, or a place shows in the catalog but not on the maps (or vice versa). Detail: `.claude/rules/data-json.md` (Cross-file integrity).

## Use this layer for
- why the place matters
- place-specific record context
- event clustering
- unresolved place-identity issues
- links to affected people and topics

## Where this fits
See `research/README.md` for the cross-subdirectory destination guidance.

## AI / automation guidance
- `.claude/rules/research-files.md` (people, places, topics — shared and per-subdirectory discipline)
- `.claude/rules/data-json.md`
- `.claude/rules/citations.md`
