# Claude working guide for `gurney-genealogy`

This file holds always-on instructions for Claude Code in this repo.
Directory-specific behavior lives in `.claude/rules/`.
Manual workflows live in `.claude/skills/`.

## Human-facing repo docs
Read these as needed for directory purpose and naming:
- `README.md`
- `data/README.md`
- `fact-sheets/README.md`
- `research/README.md`
- `sources/README.md`
- `site/README.md`
- `tools/README.md`

## Repo architecture

### Canonical structured data
- `data/` is the canonical structured spine.
- `data/ancestors v24.json` is current canonical ancestor data.
- `ancestors v23.json` is legacy and must not be used for new work.
- `data/places.json` is the primary place registry.
- `data/places_detail.json` is the supplemental place-detail layer.
- `data/sources.json` is the bibliography and source registry.

### Published narrative
- `fact-sheets/` is published-only.
- Files there are concise, polished, and website-facing.
- Do not place open questions, raw transcriptions, negative results, or exploratory reasoning there.

### Working research
- `research/` is the working layer.
- Findings belong in the relevant subject file:
  - `research/people/`
  - `research/places/`
  - `research/topics/`
  - `research/case-files/`
- `research/log/` is an index and pointer layer, not a dumping ground for substantive findings.

### Source provenance
- `sources/validations/` records what source was examined, how it was examined, scope limits, and where findings landed.
- `sources/validations/` is not the primary home for biographical findings.
- `sources/media/` stores working-reference images and crops keyed by `sourceId`.

### Site generation
- `site/` is generated/presentation-oriented.
- Canonical facts remain upstream in `data/` and `fact-sheets/`.

## Core behavioral rules

### Edit narrowly
- Prefer targeted edits to existing files over wholesale rewrites.
- Preserve established prose unless a fact, citation, structure, or clarity issue requires change.
- For markdown and JSON files under roughly 50 KB, direct in-place editing is preferred over over-engineered scripting.

### Put findings in the right layer
- Findings about a person go in that person’s research file or fact sheet, depending on maturity and publication fitness.
- Findings about a place go in `research/places/`.
- Cross-cutting methodology or multi-subject analysis goes in `research/topics/`.
- Long-form argument and competing hypotheses go in `research/case-files/`.
- Source worksheets stay thin.

### Promote carefully
- Fact sheets hold durable, publishable conclusions.
- Research files hold the evidentiary trail, caveats, extracts, negative results, and open questions.
- Do not push unresolved or weakly supported claims into published narrative.

### Citation baseline
- Every factual claim in a fact sheet should have a nearby footnote or a clearly bounded supporting citation cluster.
- Research files should also be citation-rigorous, especially for new findings, quotations, and inferential claims.
- Prefer full-form citations in footnotes, not cryptic abbreviations.
- Include URL when available and relevant.
- When one claim is supported by multiple sources, include all supporting sources.
- Align citations with `data/sources.json` whenever a source has a `sourceId`.
- No research content should be inserted from intake unless it is tied to an existing or newly created `data/sources.json` entry.

See `.claude/rules/citations.md` for detailed citation behavior.

### Evidence discipline
- Do not overclaim.
- Preserve conflicts until resolved.
- Negative results are findings and belong in the relevant subject file.
- Index/database results require image-level verification before being treated as established.

### Human docs and AI rules
- README files remain human-facing.
- `.claude/rules/` files define Claude behavior.
- If a README and a rule ever conflict, update both so they converge.

## Session start pattern
On substantive work:
1. Read this file.
2. Read the relevant directory README.
3. Read the matching path-scoped rule(s).
4. Read the target file(s).
5. Only then propose edits or analysis.

## When not to bloat startup context
Do not copy large standing-facts lists into this file unless they are repeatedly causing mistakes.
If a repeated procedure emerges, prefer a skill.
If a rule only matters for one directory, prefer a path-scoped rule.

## Related
- Human-facing repo overview: `README.md`
- Citation playbook: `.claude/skills/citation-rigour/SKILL.md`
- Intake processing: `.claude/skills/research-intake-session-processor/SKILL.md`
