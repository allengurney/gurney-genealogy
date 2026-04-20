---
paths:
  - "research/places/*.md"
---

# Research places rules

Human-facing overview:
- `research/README.md`
- `research/places/README.md`
- `data/README.md`

## Purpose
These files hold place-memory narrative and analysis that sits above the canonical place registry.

## Authority split
- `data/places.json` is the canonical place spine.
- `data/places_detail.json` is the supplemental detail layer.
- `research/places/*.md` holds narrative, relevance, record context, and unresolved questions.

## Do not duplicate the data layer
- Avoid copying compact canonical fields wholesale into narrative files unless needed for interpretation.
- Keep structured place attributes in the JSON layer.
- Keep analytical explanation and place significance here.

## Generated block discipline
- Preserve any bounded generated block conventions already in use.
- Preserve human-authored narrative outside those blocks.
- Replace older generated blocks cleanly rather than piling new ones on top.

## Scope
Good content here:
- why the place matters
- events tied to the place
- record availability/scope
- naming/normalization discussion
- unresolved place-identity questions
- links to affected people/topics

## Citation rigor
- Cite claims about place history, jurisdiction, location, or record coverage.
- Cite online gazetteer or archival pages when relevant.

## Cross-reference
See also:
- `.claude/rules/citations.md`
- `.claude/rules/data-json.md`
