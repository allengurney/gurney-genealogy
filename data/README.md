# data/

Canonical structured data for the research spine.

## Files
- `ancestors v24.json` — current canonical ancestor registry
- `ancestors v23.json` — legacy file; do not use for new work
- `places.json` — primary canonical place registry
- `places_detail.json` — supplemental place detail layer
- `master.json` — broader canonical registry used elsewhere in the repo
- `sources.json` — bibliography and citation registry

## Discipline
- Keep this layer compact, canonical, and joinable.
- Put narrative discussion, open questions, and long reasoning in `research/`.
- Keep source references aligned with `sources.json`.

## AI / automation guidance
See:
- `.claude/rules/data-json.md`
- `.claude/rules/citations.md`
