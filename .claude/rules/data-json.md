---
paths:
  - "data/*.json"
---

# Data JSON rules

Human-facing overview:
- `data/README.md`

## Role of this directory
`data/` is the canonical structured data spine for ancestors, places, and sources.

## Canonical files
- `data/ancestors.json` is the primary canonical ancestor data file.
- `places.json` is the primary place registry.
- `places_detail.json` is supplemental.
- `sources.json` is the source registry.

## Edit discipline
- Make the smallest safe edit that solves the task.
- Do not change schema casually.
- Do not rename keys, IDs, or references unless the task explicitly requires it.
- Preserve record ordering when there is no strong reason to change it.
- Do not reformat the entire file if only a few records changed.

## Source discipline
- Every source-dependent fact in structured data should map to a valid `sourceId`.
- Orphan facts and orphan sources are both defects.
- If a new source is needed, add it to `sources.json` deliberately and then reference it.

## Cross-file integrity
- When place references change, keep `places.json` and `places_detail.json` aligned.
- When ancestor references change, keep relationships, placeRefs, and source references consistent.
- Do not duplicate long narrative discussion inside JSON when it belongs in research markdown.

## Geography model
- `places.json` stays compact and canonical.
- `places_detail.json` carries richer descriptive detail.
- Do not synthesize derivative coordinates.
- Keep one best coordinate and one best precision level per place.
- Narrative and open questions belong in `research/places/*.md`, not in the JSON.

## Site-generation relationship
- Site-local files such as `_data/ancestors.json` or prototype `data/ancestors.js` are presentation artifacts unless explicitly promoted.
- New website work should derive people and place views from `data/ancestors.json`, `data/places.json`, and `data/places_detail.json` rather than copying facts by hand.

## Validation posture
Before finishing JSON work:
- check JSON validity
- scan for broken IDs/references introduced by the edit
- confirm that any new source IDs or place IDs actually exist

## Citation relationship
Structured data may not use markdown footnotes, but all source-bearing fields must still tie back to `sources.json`.
See `.claude/rules/citations.md` for repo-wide source-traceability expectations.

## Mandatory related rules (share path scope)
None — `data/*.json` is scoped only by this rule.

## See also
- `.claude/rules/citations.md` — source-traceability for source-bearing fields in `data/sources.json`
- `.claude/rules/sources.md` — sourceId discipline; new sourceId in `data/sources.json` triggers a corresponding `sources/validations/*.md` worksheet by default
- `data/README.md` — human-facing files-and-principles overview
