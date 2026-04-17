# 2026-04-17 — place normalization v1

Normalized the geography layer after the v23 → v24 extraction merge.

Updated:
- `data/places.json` — NEW canonical place registry
- `data/locations.json` — raw mentions annotated with `placeId`, normalized sub-site names, and quality flags
- `data/ancestors v24.json` — ancestor/collateral records now also carry `placeRefs`
- `data/README.md` — two-layer raw-mention / canonical-place model documented
- `research/places/README.md` — `places.json` named as the filename authority
- `research/log/README.md` — switched to atomic log guidance
- `research/places/*.md` — generated blocks replaced with concise normalized place registry blocks

Design decisions:
- kept raw mentions intact for fidelity
- added a canonical place layer rather than overwriting the mention layer
- retained existing filenames where practical for continuity; authoritative mapping now lives in `data/places.json`
- flagged merged / contaminated inherited notes for later cleanup instead of forcing speculative repairs in this pass

Next:
- second-pass review of place files flagged for merged date spans, merged notes, or naming cleanup
- optional parent/child place hierarchy if city/address clustering becomes useful later

