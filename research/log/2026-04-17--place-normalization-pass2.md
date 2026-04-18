# 2026-04-17 — place normalization pass 2

Second cleanup pass on the normalized place spine.

Updated:
- `data/places.json` — cleaned short descriptions, roles ordering, and ancestor links for selected places
- `data/places_detail.json` — cleaned long descriptions, extant-status descriptions, and review notes
- `data/ancestors v24.json` — place refs regenerated from the cleaned canonical place set
- `research/places/*.md` — generated blocks refreshed with cleaner linked-ancestor summaries and reduced noise

Key cleanup actions:
- removed the incorrect West Barsham landholding link from G~37 Eudes
- replaced merged/concatenated popup text for high-value places with cleaned canonical descriptions
- converted several remaining records into explicit town-level or region-level umbrella notes where appropriate
- suppressed review notes that no longer added value after cleanup

Remaining follow-up:
- optional deeper parcel-level split for some Massachusetts town records if needed later
- optional future separation of City of London and Normandy sub-sites if those become first-class research objects

