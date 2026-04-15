# tools/

Lineage-specific tools and interactive artifacts. Currently Gurney-only; when a tool proves generally useful, it gets extracted to a cross-lineage repo.

## Contents

- `pedigree-explorer.html` — interactive pedigree explorer, G1 → G37. Standalone HTML with `ancestors_v23.json` embedded. To regenerate after data changes, rebuild from `data/master.json`.

## Planned

- A browser tool over `data/master.json` and `data/sources.json` for finding orphan facts, orphan sources, and coverage gaps.
- A Candidate B timeline visualizer once the case file stabilizes.
