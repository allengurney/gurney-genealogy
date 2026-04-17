# research/places/

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
