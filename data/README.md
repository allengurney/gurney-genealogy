# data/

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
