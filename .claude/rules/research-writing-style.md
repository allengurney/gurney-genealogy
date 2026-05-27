---
paths:
  - "**/*"
---

# Research writing style

## Purpose
Research files are for substantive findings, extracts, and analysis.
They are not workflow diaries.

## Default standard
- Lead with the finding itself.
- Prefer direct declarative prose.
- Keep entries compact.
- Use headings only when they improve retrieval.
- Include documented anecdotes and details which humanize and add detail and context.
- Do not overly summarize as details provide value.
- Include quotes and lengthy text extracts when high value.

## Keep process out of visible prose
Do not mention the following in ordinary research prose unless the detail materially affects interpretation:
- intake
- processing
- OCR
- normalization
- review state
- archival mechanics
- workflow stage

Put that detail in HTML comments, footnotes, validations, or processed patchsets.

## Caveat discipline
- Trust the provided source association and metadata unless there is a concrete reason not to.
- Add a visible caveat only when uncertainty materially changes meaning, identity, chronology, place, or interpretation.
- Prefer specific uncertainty over generic caution.

## Preferred entry shape
1. Sentence stating the finding.
2. Optional label such as `Working transcription:` or `Extract:`.
3. Optional quotation block.
4. Optional 1–2 sentence analysis only when it adds real knowledge.
5. Footnote(s).

## Analysis threshold
Add analysis only when it identifies a person/place/relationship, sharpens chronology, links to an existing hypothesis, explains a conflict, or adds substantive context.

## Knowledge density preference
When choosing between a sentence about genealogy or AI process and a sentence that preserves a concrete historical fact, prefer the concrete historical content unless omitting the process note would materially mislead the reader.

## Mandatory related rules (share path scope)
None — this rule is always-loaded; prose discipline applies to research and fact-sheet work alike.

## See also
- `.claude/rules/citations.md` — citation discipline that pairs with finding-first prose
- `.claude/rules/research-files.md` — entry-level discipline for working notes
- `.claude/rules/fact-sheets.md` — finding-in-main / sources-in-footnote discipline for published narrative
- `.claude/rules/sources.md` — promotion writing standard ("lead with the knowledge") when intake content lands in research files
