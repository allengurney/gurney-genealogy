# research/places/

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
