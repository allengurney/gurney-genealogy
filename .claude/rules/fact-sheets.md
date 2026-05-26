---
paths:
  - "fact-sheets/*.md"
---

# Fact-sheet rules

Human-facing overview:
- `fact-sheets/README.md`

## Purpose
`fact-sheets/` holds published ancestor narratives.

## Content boundary
Allowed here:
- stable narrative
- polished prose
- vitals
- highlights
- children table
- concise contextual narrative
- citations
- related links

Not allowed here:
- open questions
- raw source extracts longer than brief quotation
- negative search results
- unresolved conflicts without concise framing
- staging notes
- exploratory reasoning dumps

## Editorial posture
- Respect Allen’s prose yet offer suggestions for improvement.
- Fact sheets are engaging, insightful, and enjoyable to read. Readers are not subject matter experts.
- Fact sheets are concise yet include interesting anecdotes and stories, historically significant events and people, and unexpected findings.   
- Edit only when a fact, citation, clarity issue, or structural improvement warrants it.
- Prefer light-touch revision over stylistic churn.
- Preserve the published feel.
- For terms which require subject matter expertise the reader may not have (particularly pre-1900), hyperlink the term to a definition or reference such as wikipedia. No more than 10 such hyperlinks per fact sheet.

## Plain-English reader contract
- Write for a general reader. Avoid jargon that requires subject-matter expertise unless it is glossed inline.
- Do not use repository-internal vocabulary in reader-facing prose: "repo," "the repo's numbering," "FS structured field," "structured data," "intake," "patchset," and similar terms belong in research/validation/patchset files, not in fact sheets.
- When a meaningful ordering or naming choice needs to be explained, phrase it as a reader-facing convention (e.g., "Ordinal numbering of ancestors such as 'II' in 'Hugh II' on this site follows..."), not as a fact about the repository.
- Do not use unexplained Latin or French quotations. Keep the original phrase when it adds flavor or fidelity, but follow it with a plain-English meaning ("*mort sans postérité* — died without descendants"; "*un vieux manuscrit* — an old manuscript").
- Do not use acronyms or repo-internal shorthand on the visible page: spell out **Daniel Gurney's *Record of the House of Gournay*** rather than **DG-I**; **FamilySearch** rather than **FS**; **the family-tree compilation at our-royal-titled-noble-and-commoner-ancestors.com** rather than **TNG site**; **Foundation for Medieval Genealogy MedLands** rather than **FMG MedLands**. Existing acronyms in research files may stay; do not introduce new ones in fact sheets.
- Non-English quotes and quotes that use terminology not in common modern usage should be explained or translated for plain English consumption.
- Highly technical, genealogical, or historical terms which are not in common modern usage should either be a hyperlink to a definition or explanatory source (e.g. wikipedia.org), explained in the prose, a parenthetical synonym, or otherwise avoided for plain English consumption.

## Lineage-status vocabulary
- Reader-facing status language should be plain. Prefer phrases like "historically recorded but limited," "confirmed by contemporary document," "rests on later tradition" over single-word labels like "Tradition" or "Uncertain" without context.
- "Direct line" is the right reader-facing tag for direct ancestors. Do not use "COLLATERAL" or other internal status labels in the children table; describe non-direct-line children in plain prose (e.g., "founder of the Somerset cadet line," "third son said to have died without descendants") and do not flag them with an all-caps label.

## Citation placement
- Page numbers, manuscript identifiers, and multi-source provenance chains belong in footnotes, not in the body.
- Rule of thumb: if a sentence reaches the point of citing a page number or a manuscript shelfmark, that material should move to a footnote — even if the surrounding sentence already has another footnote, prefer a second adjacent footnote over an inline citation.

## Finding-in-main, sources-in-footnote
- The **core finding** stays in the main content (Vitals, Highlights, Children table notes, or Narrative). A footnote can carry complex supporting detail to keep the primary read clean, but the finding itself — what a reader would describe as "the new thing learned" — must be visible on the page without expanding any footnote.
- Footnotes are **source-heavy**, not content-heavy. They carry citations, provenance chains, exact quotations, page numbers, alternate readings, and the apparatus a curious reader needs to verify the finding. Substantive findings that arrived in research are not "buried" in footnotes during promotion.
- Test for a candidate placement: if removing the footnote would leave the body text non-informative on a specific finding, the footnote is carrying the finding and should be partly lifted to the body.
- For complex multi-source claims, it is acceptable for the body to assert the finding compactly and the footnote to carry the full apparatus — but the body must still assert.

## Highlights block discipline
- Highlights are reader-facing **headline bullets**, not paragraphs.
- Target **4-6 bullets**. Three reads thin; seven or more reads overstuffed.
- If a new finding genuinely warrants a seventh bullet, shorten or consolidate the others rather than adding indefinitely. Bullet count and bullet length move together — more bullets means each must be shorter.
- Each bullet leads with a **bold headline phrase** (one short sentence or fragment) followed by one or two short evidence/context sentences. The bullet should read like a magazine pull-quote, not a research note.
- Concrete, ancestor-specific punch beats generic historical context. Wars-of-the-Roses overviews and generic Henry-VI-minority framing belong in Narrative, not Highlights.
- The **full story** — multi-step argument, source chain, supporting detail — belongs in the **Narrative** section, not in the Highlights bullet. Treat each bullet as a pointer into the Narrative for readers who want more.
- No inline page numbers, manuscript shelfmarks, archive codes (e.g. "TNA E101/48/6"), or multi-source provenance chains inside a Highlights bullet. Those go in the footnote, per the Citation placement rule above.
- See `sources/intake/processed/Ready/v05-patchset-highlight-updates.md` for the worked-example style across G16-G37.

## Vitals overflow goes to Narrative, not to footnote
- Vitals cells stay short (one or two short sentences; three is the exception).
- When a vital has a longer "story" — the contested birth bracket, the death tradition with three independent variants, the post-event monastic career — the long version goes in the Highlights or Narrative section of the same fact sheet, **not into the vital cell's footnote**.
- The footnote on a vital should carry citations and the apparatus that verifies the brief vital text, not narrative content that a reader would expect to encounter in the body.

## Do not manually mirror fact-sheet edits to `site/`
- `fact-sheets/` is the canonical published narrative. The website build process handles the mirror into `site/website/fact-sheets/` automatically.
- Do **not** copy edited fact-sheet files into `site/website/fact-sheets/` as a separate step after editing. The same applies to other site-mirror artefacts under `site/website/_data/` (`ancestors.json`, `sourcesCatalog.json`, etc.) — these are presentation artefacts produced by the build, not files to keep in sync by hand.
- This saves a step and keeps the canonical-vs-generated boundary clean per `.claude/rules/site-generation.md`: `data/` and `fact-sheets/` are upstream; `site/` is generated.
- If a fact-sheet change requires immediate visible verification before the next build, ask the user rather than mirror by hand.

## Vitals block discipline
- The Vitals grid (Born / Died / Occupation / Buried / Marriage(s)) is a compact reference block, not a narrative.
- Keep each cell short. One or two short sentences is the norm; three is the exception.
- Detail and color belong in Highlights or Narrative, not in vitals.
- When a vital is genuinely uncertain or contested, summarise the bracket (e.g., "after 911, before c. 932") and put the apparatus in a footnote.
- Internal consistency: if Born = c. 970 and a son is born c. 985, that implies fathering at 15. Adjust the parent's birth estimate or surface the conflict; do not publish an implausible age silently.

## Citation rigor
- Every factual sentence or tight factual cluster should have a nearby footnote.
- Use full-form footnotes, not cryptic abbreviations.
- Include URL when available. URL to a website should be a hyperlink when possible.
- Include all material supporting sources when a claim is supported by more than one source.
- If a sentence is inferential rather than directly attested, make that visible in the prose and cite accordingly.

## Relationship to research files
- Do not bury evidentiary detail in the fact sheet.
- If a passage needs long support discussion, conflict resolution, or transcription detail, move that supporting material to the companion in `research/people/`.
- Fact-sheet edits should stay consistent with the corresponding research file.

## Promotion standard
Before adding a new claim to a fact sheet, ask:
- Is this claim durable enough for publication?
- Is the evidence strong enough or appropriately and objectively phrased?
- Is the claim phrased at the right confidence level?
- Would a future reader be able to trace the support quickly?

If not, keep it in research instead.

## Pairing rule
For an ancestor with a fact sheet, there should normally also be a paired research companion in `research/people/`.

## Cross-reference
See also:
- `.claude/rules/citations.md`
- `.claude/rules/research-people.md`
