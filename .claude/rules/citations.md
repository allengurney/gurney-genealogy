---
paths:
  - "fact-sheets/*.md"
  - "research/**/*.md"
  - "sources/validations/*.md"
---

# Citation and sourcing rules

Human-facing overview:
- `fact-sheets/README.md`
- `research/README.md`
- `sources/validations/README.md`

## Purpose
These rules apply whenever Claude edits or creates citation-bearing markdown in this repo.

## Core standard
- Put the citation footnote as close as practical to the fact or finding it supports.
- Prefer sentence-level or tightly bounded clause-level citation placement.
- Do not let one footnote float ambiguously over a long paragraph unless the entire paragraph derives from the same source set.

## Fact-sheet standard
- Nearly every factual sentence should have a footnote or clearly share one with the immediately adjacent sentence.
- Avoid omnibus end-of-paragraph notes unless the paragraph is genuinely one-source and one-claim.
- When a sentence has multiple materially relevant sources, include multiple adjacent footnotes.

### Example
`Francis Gurney married Margaret Rybett in 1611.[^12][^13]`

## Research-file standard
- New findings, quotations, transcriptions, and inferential claims should be cited.
- Research files may contain denser note-taking than fact sheets, but they should still be source-traceable.
- When a claim is provisional, say so explicitly and cite the basis.
- No research content should be inserted from intake unless it is tied to an existing or newly created `data/sources.json` entry.

## Footnote content
Each footnote should generally include:
- full source title or repository/source description
- creator/author when known
- specific page, folio, entry, or image detail when known
- date or year when useful
- URL when available
- access note if relevant for unstable web resources
- enough detail to find the exact source again

## Abbreviations
- Avoid unexplained abbreviations in the visible citation text.
- Short handles such as `sourceId` values are acceptable internally, but the footnote itself should normally expand to a human-readable citation.
- If a repo-specific shorthand is helpful, expand it in full in the note.

## SourceId alignment
- If a cited source exists in `data/sources.json`, the footnote must align with that source.
- Prefer to include `Source ID: <sourceId>.` at the end of the footnote when it materially helps traceability.
- Do not invent new `sourceId` values casually; add them deliberately in `data/sources.json`.

## Multiple-source claims
- If one statement depends on more than one source, include all material sources.
- Prefer adjacent separate footnotes over one blended omnibus footnote when the sources are distinct.
- A blended footnote is acceptable when all cited works support the same narrow proposition and the note remains readable.

## Quotations and transcriptions
- Quotations must point to the exact page/entry/image when possible.
- Preserve original spelling only when relevant.
- If silently normalizing OCR or obvious character confusion in prose, do not present the normalized form as a verbatim quote.

## Online sources
- Include URL when available and stable enough to be useful.
- Prefer the page URL for the exact record, article, or source entry.
- If a source is only reachable through a search-result flow, cite the stable collection or record URL if one exists.

## Unsupported claims
- If a claim cannot be sourced confidently, either:
  - remove it from the fact sheet, or
  - keep it in research only and mark it as unresolved.

## Citation cleanup behavior
When editing a file:
- preserve existing good citations
- improve weak citations in place
- collapse duplicate notes only when clarity improves
- do not renumber gratuitously unless the file is already being normalized

## Related skill
For heavy citation audit or normalization, invoke:
- `.claude/skills/citation-rigour/SKILL.md`
