# data/

Canonical structured data for the research spine.

## Files
- `ancestors v26.json` — current canonical ancestor registry
- `ancestors v25.json` — legacy ancestor registry; do not use for new work
- `places.json` — primary canonical place registry
- `places_detail.json` — supplemental place detail layer
- `sources.json` — bibliography and citation registry

## Version rule
Use the most recent `ancestors vNN.json` file for new site and data work. As of this branch, that file is `ancestors v26.json`. If a newer version is added later, update this README and the matching `.claude` data rule in the same change.

## Discipline
- Keep this layer compact, canonical, and joinable.
- Put narrative discussion, open questions, and long reasoning in `research/`.
- Keep source references aligned with `sources.json`.
- Treat site-local data files as generated or presentation-specific derivatives unless a task explicitly says otherwise.

## AI / automation guidance
See:
- `.claude/rules/data-json.md`
- `.claude/rules/citations.md`
