---
paths:
  - "fact-sheets/*.md"
  - "research/**/*.md"
  - "sources/validations/*.md"
---

# Citation and sourcing rules

Human-facing overview: `fact-sheets/README.md`, `research/README.md`.

These rules apply whenever Claude edits or creates citation-bearing markdown.

## Core standard
- Put the citation footnote as close as practical to the fact or finding it supports.
- Prefer sentence-level or tightly bounded clause-level citation placement.
- Do not let one footnote float ambiguously over a long paragraph unless the entire paragraph derives from the same source set.

## Fact-sheet standard
- Nearly every factual sentence should have a footnote or clearly share one with the immediately adjacent sentence.
- **A footnote that supports more than three sentences of body text is omnibus; split it** unless every covered sentence cites the same source set.
- When a sentence has multiple materially relevant sources, include multiple adjacent footnotes.

## Research-file standard
- **Every discrete fact or finding carries an explicit source.** Maintain the trail from each fact/finding to its source — not only for headline findings. Aim for full coverage, not the roughly half-coverage that accretes when entries are added quickly; new findings, quotations, transcriptions, and inferential claims must each be cited.
- **Show every aligned source, not just one.** When a fact is supported by three or more sources, cite all of them — adjacent footnotes, or a single footnote that names each witness — rather than citing one and leaving the rest implicit. A multiply-attested fact reads as stronger evidence when the reader can see the full stack; do not silently collapse a known 3+-source fact to a single citation.
- A pre-existing **in-line** citation already in research prose (the source named in the body text rather than in a footnote) is acceptable and need not be converted to a footnote solely for form. The requirement is an explicit, traceable source per fact in whatever placement — not a particular footnote style.
- **Never drop a fact or finding merely because its source is missing or weak.** Preserve it, flag the sourcing gap, and supply or strengthen the citation; do not delete under-cited but genuine content to tidy. (Restates the Unsupported-claims exception below for the research layer.)
- Keep body prose focused on the finding.
- Routine provenance mechanics should usually stay in the footnote rather than the body.
- No research content should be inserted from intake unless it is tied to an existing or newly created `data/sources.json` entry.
- Use explicit provisional language only when the uncertainty materially changes meaning.

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
- A supplied crop, screenshot, or transcription may be cited directly when its source association is clear.
- Do not add formulaic body-text caveats solely because the item is an extract rather than a full-page image.
- If the extract is materially ambiguous, describe the specific ambiguity.

## Online sources
- Include URL when available and stable enough to be useful.
- Prefer the page URL for the exact record, article, or source entry.
- If a source is only reachable through a search-result flow, cite the stable collection or record URL if one exists.
- Use citations to repo markdown artifacts only when necessary; include the visible path text and link it to the GitHub file when useful for readers. Never reference JSON files in fact sheets or research companions.

## Tertiary online sources (Wikipedia and similar)
- Wikipedia and similar compiled-pedigree / encyclopedic sites are **collectors**, not authorities. They have value as quick orientation and as pointers to the underlying primary or secondary literature their references cite.
- When a Wikipedia (or comparable tertiary) page is the proximate source for a finding, **trace it to the authority it cites** before publishing — the underlying History of Parliament biography, Calendar of Patent Rolls volume, parish-register entry, monograph, peer-reviewed article. Cite the authority, not the collector, in the fact-sheet footnote.
- Keeping the collector URL in a research-companion note as a discovery trail is fine. Do not let a Wikipedia citation stand alone in a fact sheet when the underlying authority is reachable.
- Same posture for Stirnet, FamilySearch Family Tree, Geni, WikiTree, Find a Grave memorial pages without primary documentation, and similar compiled-pedigree databases.
- A Wikipedia URL is acceptable as a supplementary cross-reference link in the related-links sidebar (orienting the reader to a famous in-law's biography) but it should not be the sole citation for any substantive factual claim.
- **Proportion rigour to the weight of the claim — contextual colour vs. substantive claim.** The trace-to-authority requirement above governs **substantive genealogical claims**: an ancestor's identity, dates, kinship, landholding, or actions. For **background and contextual material that makes no genealogical claim about the subject** — the history or significance of an employer, institution, regiment, place, or period setting that orients the reader — a reputable tertiary or encyclopedic source (Wikipedia, a company or operator history page, a heritage-site or government history page, a reference-work entry) may stand on its own, cited by title and URL, without tracing to a primary authority. Keep such a source clearly contextual and do not let it carry a substantive claim about the ancestor; when one sentence mixes both, cite the substantive part to its authority and the contextual part to the collector. This is a band, not a licence to under-source: the heavier a reader is likely to weigh a statement, the closer to a primary authority it should sit.

## Superseded drafts vs. later editions (same compiler)
When a source survives in both an earlier working form (manuscript, worksheet, draft) and a later published edition by the same compiler, the later edition normally supersedes, and where the two conflict the later edition wins. Treat a fact that appears in the earlier notes but is **absent from the later edition that covers the same subject** as lower-weight: the compiler may have dropped it as poorly founded or missing attributes, but the omission may equally be incompleteness or work-in-progress, so caveat the delta rather than assuming rejection — do not promote a worksheet-only "delta" fact to the same confidence as one the published edition confirms. Note the delta in the citation (e.g., "in Rigler's c. 1980 worksheet but not carried into the 1994 edition"). This test only applies when the later edition's coverage of that subject was actually examined; if the published entry for the person was not seen, say so rather than inferring an omission.

## Unsupported claims
- If a claim cannot be sourced confidently, either:
  - remove it from the fact sheet, or
  - keep it in research only and mark it as unresolved.
- Exception for citation-cleanup or user-directed restoration: do not silently remove or soften existing user-facing content merely because the citation is missing or weak. Preserve the claim, document the sourcing problem, and ask for direction rather than forcing a mismatched citation.

## Citation cleanup behavior
When editing a file:
- preserve existing good citations
- improve weak citations in place
- collapse duplicate notes only when clarity improves
- do not renumber gratuitously unless the file is already being normalized

For heavy citation audit or normalization, see `.claude/skills/citation-rigour/SKILL.md`.

## Mandatory related rules (share path scope)
- `.claude/rules/fact-sheets.md` — both scope `fact-sheets/*.md`; citation discipline applies inside fact-sheet edits
- `.claude/rules/research-files.md` — both scope `research/**/*.md`; citation discipline applies inside research-companion edits
- `.claude/rules/research-case-files.md` — both scope `research/**/*.md` (case-files subdir)
- `.claude/rules/sources.md` — both scope `sources/validations/*.md`; citation discipline applies inside validation worksheets

## See also
- `.claude/skills/citation-rigour/SKILL.md` — audit and normalization workflow
- `.claude/rules/research-writing-style.md` — finding-first prose discipline that pairs with citation discipline
