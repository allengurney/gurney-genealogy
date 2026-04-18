# 2026-04-17 — place normalization v1

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

