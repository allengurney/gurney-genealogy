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

## Generated ID indexes
Generated lookup indexes live in `data/indexes/`:

- `all-ids.csv` — compact locator for ancestor, related, era, place, and source IDs
- `ancestor-ids.csv` — `recordId` lookup for `data/ancestors.json`
- `place-ids.csv` — `placeId` lookup for `data/places.json`
- `source-ids.csv` — source-key lookup for `data/sources.json`

Use these indexes for ID discovery before opening large canonical JSON files. Search the relevant index first, then open only the canonical record or line range needed for the task.

Do not edit generated index files by hand. Use `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --check` for a lightweight freshness check. Use `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write` to run integrity validations and regenerate the index files.

The indexes are locators only. Canonical facts remain in `data/*.json`; generated site data under `site/website/_data/` remains presentation output.

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
- When repairing a missing `corpusPath` or `mediaPath`, first use `repo_search.py`
  to find where the file or content moved, searching by filename, source ID, and
  extrapolated source details before nulling the path or falling back to a
  validation worksheet.
- `sources.json` `notes` fields are brief catalogue annotations (what the source is,
  why it is relevant, what kinds of information it carries — roughly 2–4 sentences).
  Evidence, extracts, negative-search results, and findings belong in research
  markdown or `sources/corpus_supplement/`; a short finding may be duplicated into
  `notes` only when it is already carried in a research file.
  `tools/lint_source_notes.py` enforces a soft cap (600 chars) with a frozen
  allowlist for grandfathered pre-existing entries.

## Cross-file integrity
- When place references change, keep `places.json` and `places_detail.json` aligned (one row per `placeId` in each).
- A place↔ancestor link is bidirectional — write it on **both** sides: `ancestorLinks[].recordId` in `places.json` (feeds the website places catalog and place pages) **and** that ancestor's `placeRefs` in `ancestors.json` (feeds the ancestor's map markers in the pedigree drawer and ancestor map). Updating only one side makes a place appear in the catalog but not on the maps, or the reverse. A new place also needs a `research/places/<filename>.md` companion to match its `filename`. The `site/website` validator (`npm run validate`) warns on either-side drift, dangling refs, and orphan links.
- Keep ancestor relationships and source references consistent when records change.
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
