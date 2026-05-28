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
- **Fact sheets are engaging, insightful, and enjoyable to read. Readers are not subject matter experts.** Fact sheets should be narrated more like an enjoyable leisure biography than a dense academic paper. 
- Fact sheets are concise yet include interesting anecdotes and stories, historically significant events and people, and unexpected findings.   
- Edit only when a fact, citation, clarity issue, or structural improvement warrants it.
- Prefer light-touch revision over stylistic churn.
- Preserve the published feel.
- For terms which require subject matter expertise the reader may not have (particularly pre-1900), hyperlink the term to a definition or reference such as wikipedia. No more than 10 such hyperlinks per fact sheet.

## Plain-English reader contract
- Write for a general reader. Avoid jargon that requires subject-matter expertise unless it is glossed inline.
- Do not use repository-internal vocabulary in reader-facing prose: "repo," "the repo's numbering," "FS structured field," "structured data," "intake," "patchset," "claim," and similar terms belong in research/validation/patchset files, not in fact sheets.
- When a meaningful ordering or naming choice needs to be explained, phrase it as a reader-facing convention (e.g., "Ordinal numbering of ancestors such as 'II' in 'Hugh II' on this site follows..."), not as a fact about the repository.
- Do not use unexplained Latin or French quotations. Keep the original phrase when it adds flavor or fidelity, but follow it with a plain-English meaning ("*mort sans postérité* — died without descendants"; "*un vieux manuscrit* — an old manuscript").
- Do not use acronyms or repo-internal shorthand on the visible page: spell out **Daniel Gurney's *Record of the House of Gournay*** rather than **DG-I**; **FamilySearch** rather than **FS**; **the family-tree compilation at our-royal-titled-noble-and-commoner-ancestors.com** rather than **TNG site**; **Foundation for Medieval Genealogy MedLands** rather than **FMG MedLands**. Existing acronyms in research files may stay; do not introduce new ones in fact sheets.
- Non-English quotes and quotes that use terminology not in common modern usage should be explained or translated for plain English consumption.
- Highly technical, genealogical, or historical terms which are not in common modern usage should either be a hyperlink to a definition or explanatory source (e.g. wikipedia.org), explained in the prose, a parenthetical synonym, or otherwise avoided for plain English consumption. Examples: "feoffee," "advowsons," "engrailed." 

## Lineage-status vocabulary
- Reader-facing status language should be plain. Prefer phrases like "historically recorded but limited," "confirmed by contemporary document," "rests on later tradition" over single-word labels like "Tradition" or "Uncertain" without context.
- "Direct line" is the right reader-facing tag for direct ancestors. Do not use "COLLATERAL" or other internal status labels in the children table; describe non-direct-line children in plain prose (e.g., "founder of the Somerset cadet line," "third son said to have died without descendants") and do not flag them with an all-caps label.

## Citation placement (fact-sheet-specific)
The general citation discipline lives in `citations.md`. Fact-sheet-specific additions:

- **Finding-in-main, sources-in-footnote.** The core finding stays in the main content (Vitals, Highlights, Children table notes, or Narrative). Footnotes are source-heavy, not content-heavy — they carry citations, provenance chains, exact quotations, page numbers, alternate readings. Substantive findings that arrived in research are not "buried" in footnotes during promotion. Test: if removing the footnote leaves the body text non-informative on a specific finding, the footnote is carrying the finding and should be partly lifted to the body.
- For complex multi-source claims, the body asserts the finding compactly while the footnote carries the full apparatus — but the body must still assert.

## Highlights block discipline
- Highlights are reader-facing **headline bullets**, not paragraphs.
- Target **4-6 bullets**. Three reads thin; seven or more reads overstuffed.
- If a new finding genuinely warrants a seventh bullet, shorten or consolidate the others rather than adding indefinitely. Bullet count and bullet length move together — more bullets means each must be shorter.
- Each bullet leads with a **bold headline phrase** (one short sentence or fragment) followed by one or two short evidence/context sentences. The bullet should read like a magazine pull-quote, not a research note.
- Concrete, ancestor-specific punch beats generic historical context. Wars-of-the-Roses overviews and generic Henry-VI-minority framing belong in Narrative, not Highlights.
- The **full story** — multi-step argument, source chain, supporting detail — belongs in the **Narrative** section, not in the Highlights bullet. Treat each bullet as a pointer into the Narrative for readers who want more.
- No inline page numbers, manuscript shelfmarks, archive codes (e.g. "TNA E101/48/6"), or multi-source provenance chains inside a Highlights bullet. Those go in the footnote.

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
- Internal consistency: if Born = c. 970 and a son is born c. 985, that implies fathering at 15; do not publish an implausible fact pattern silently.

## Citation rigor
- Every factual sentence or tight factual cluster should have a nearby footnote.
- Use full-form footnotes, not cryptic abbreviations.
- Include URL when available. URL to a website should be a hyperlink when possible.
- Include all material supporting sources when a claim is supported by more than one source.
- If a sentence is inferential rather than directly attested, make that visible in the prose and cite accordingly.
- Narrative paragraphs must not rely on vitals/highlights citations alone. During any fact-sheet edit, audit the Narrative section sentence-by-sentence or tight-cluster-by-tight-cluster and add nearby source footnotes from the fact sheet, companion, source registry, or validation layer. If exact support cannot be found during a citation-cleanup task, preserve the claim and ask for direction rather than silently removing, softening, or forcing a citation.
- Every children-table row, plus any "no further children" note, must carry a source footnote. If the table uses one pedigree source for multiple children, repeated references to the same footnote are acceptable, but each row still needs a visible citation.
- Temporary footnote handles such as `nNEW1`, `ref-NEW1`, or visible labels like `NEW1` are patchset placeholders only. Never leave them in a completed fact sheet. Normalize them into ordinary numeric footnotes before validation.
- Before completing a multi-fact-sheet citation batch, run a targeted footnote sweep: no `NEW` labels remain, all `href="#n..."` / `href="#ref-..."` anchors resolve, IDs are unique, visible footnote labels match their note numbers, and Narrative/Children sections have nearby citation coverage.

## Relationship to research files
- Do not bury evidentiary detail in the fact sheet. If a passage needs long support discussion, conflict resolution, or transcription detail, move that supporting material to the companion in `research/people/`.
- Fact-sheet edits should stay consistent with the corresponding research file.
- For an ancestor with a fact sheet, there should normally also be a paired research companion in `research/people/`.

## Promotion standard
Before adding a new claim to a fact sheet, ask: is this claim durable enough backed by source evidence? Is the evidence strong enough or appropriately and objectively phrased? Is the claim phrased at the right confidence level? Would a future reader be able to trace the support quickly? If not, keep it in research instead.

## Mandatory related rules (share path scope)
- `.claude/rules/citations.md` — both scope `fact-sheets/*.md`; citation placement, footnote rigour, omnibus limit

## See also
- `.claude/rules/research-files.md` — the paired research companion in `research/people/` carries the supporting evidence
- `fact-sheets/README.md` — human-facing overview of the directory
