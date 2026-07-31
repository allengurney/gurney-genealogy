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
- live lead handles such as `L-112` in headings or visible body prose

Put that detail in HTML comments, footnotes, validations, or processed patchsets.
Lead handles may remain in footnotes or HTML comments as a discovery trail, especially after a lead closes.

## Reader contract — write for someone without your grounding

The default failure in this repo's prose is **assuming the reader already knows what the writer knows**. A finding stated without the context that makes it matter is not a finding to the reader; it is a sentence. Aim for prose that a capable general reader can follow start to finish without stopping to reconstruct anything.

- **Complete the logic thread.** State the finding, then the evidence, then why it changes anything. If a conclusion depends on two facts and an inference, all three should be visible. A reader should never have to supply a missing step from prior knowledge of the family or the project.
- **Identify people on first mention with a one-word role modifier** — "the historian Blomefield," "the genealogist Daniel Gurney," "the antiquary Walter Rye," "the compiler Sprague." Surnames alone are invisible to a reader meeting them for the first time, and this prose is already dense with the family's own names.
- **Plain contemporary language.** Prefer the word in ordinary modern use. Where a technical, legal, genealogical or period term genuinely carries the meaning, gloss it inline the first time ("joint seisin — the two men held the freehold together"). See `fact-sheets.md`, "Plain-English reader contract," for the fuller treatment; the same posture applies here at slightly lower intensity, since research prose may keep more technical vocabulary once glossed.
- **Bottom line up top, and in the headers.** Open a file, a section and usually a paragraph with the conclusion in plain language; details follow. Headers should carry the finding ("Essex is open, not closed") rather than name a topic ("Essex"). This matters most where the material is long: give the reader the answer before the apparatus.
- **Use lists where the material is a set.** Numbered or bulleted lists make dense enumerations — grounds for an elimination, what a candidate has and lacks, what would settle a question, coverage limits — far more consumable than the same content as continuous prose. Tables remain right for parallel records with shared columns. Reach for a list whenever a paragraph is carrying three or more parallel items.

Judgment applies: a short entry does not need a bottom-line header, and not every paragraph is a list. The band is *more structure and more glossing than feels necessary to the writer*, because the writer is the one reader who does not need it.

## Document the current state, not the file's own history

Research prose states what is true and what the evidence is. It does not narrate how the account got there.

- Avoid "the older account got this wrong," "this was previously thought," "has now been revised," "an earlier draft said," "what is new here is." Where a finding corrects an earlier statement, **rewrite the statement** — the correction should be invisible in the result.
- The **exception is deliberate and narrow**: a working round whose retraction trail is itself the record (the July 2026 `50-`–`75-` units are the standing example) keeps its corrections visible, because showing how a wrong turn was caught is the point of that layer. Files that carry a correction trail should say so in their header.
- Change over time *in the history* is fine and often essential — "the household stops baptising in 1637," "the manor later passed to." The prohibition is on signalling the project's own research timeline.

This restates for research prose what `fact-sheets.md` requires of published narrative ("Read as if written all at once"); the two should not diverge.

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
