# data/

Canonical structured data for the research spine.

## Files
- `ancestors.json` — canonical ancestor registry
- `places.json` — canonical place registry
- `places_detail.json` — supplemental place detail layer
- `sources.json` — bibliography and citation registry
- `familysearch-ids.csv` — FamilySearch PID-to-generation crosswalk
- `search-variants.json` — manually curated spelling, language, OCR, and transcription variants used by `tools/repo_search.py`; place aliases remain in the place registry/index

## Working principle
This layer stays compact, canonical, and joinable. Narrative discussion, open questions, and long reasoning live in `research/`. Source references stay aligned with `sources.json`. Site-local JSON under `site/website/_data/` is generated from this directory by the build — not a source of truth.

## AI / automation guidance
- `.claude/rules/data-json.md` (edit discipline, source discipline, cross-file integrity, geography model)
- `.claude/rules/citations.md`
