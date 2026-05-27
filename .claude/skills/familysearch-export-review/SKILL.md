---
name: familysearch-export-review
description: Phase 0 review of a FamilySearch Family Group Record PDF export against existing repo knowledge. Produces a content-evaluation MD (additions, revisions, conflicts, URL triage) attached to chat as input to Phase 1 intake. Read-only with respect to research/, fact-sheets/, and data/.
argument-hint: [path to FS export PDF, e.g., sources/FS/<YYYYMMDD>Family<PID>.pdf]
disable-model-invocation: true
---

Use this skill for Phase 0 of a FamilySearch intake — content evaluation only.
The output is an assessment MD attached to chat, not committed to the repo.
The assessment is later the primary input to `research-intake-prep` (Phase 1).

## Read first
- `.claude/CLAUDE.md`
- `AGENTS.md` §4 (Repo file resolution — lookup order, direct-open known paths, destination discipline)
- `.claude/rules/research-writing-style.md`
- `.claude/rules/citations.md`
- `.claude/rules/sources.md` (intake + validations + media discipline, merged 2026-05-25)
- the target ancestor's `research/people/<g##>-...research.md` and `fact-sheets/<g##>-...md`
- the target's record in `data/ancestors.json` and the immediately adjacent generations
- any companion files already grabbed under `sources/FS/<PID>/` (third-party docs collected during prior URL crawls)

## What this skill does
For one FamilySearch Family Group Record PDF:
1. resolve the FS PID to its repo generation via `familysearch-ids.csv`
2. parse files in three layers (see "Three-layer PDF discipline" below)
3. cross-walk the export against the repo's existing research companion, fact sheet, and structured ancestor row
4. crawl every URL in the Sources sections (with triage; see "URL triage discipline" below) and incorporate net-new content
5. produce the assessment MD covering: source-format anatomy, concordant facts, net-new content (with verbatim transcripts), FS conflicts, spurious-content findings, FS Tree update suggestions, URL triage, patchset-readiness sketch, and open items

## What this skill does not do
- do not modify `research/...`, `fact-sheets/...`, `data/...`, or `site/...`
- do not write a Phase-1 patchset at `sources/intake/processed/vNN.patchset.md` (that is `research-intake-prep`)
- do not move, rename, or delete files
- do not stage, commit, or push

## Three-layer PDF discipline
A FamilySearch Family Group Record PDF bundles three content layers with very different trust profiles. Treat each layer differently — never collapse them.

| Layer | Trust | Treatment |
|---|---|---|
| Structured FGR table fields (husband/wife/children/dates/places/parents) | Low | Cross-walk for conflicts; surface conflicts even when our value is better, so the user can later update the FS tree. Identify whether claims are sourced. |
| Sources sections per person (URLs + embedded notes) | High when the embedded note is a transcript from a scholarly source (FMG MedLands, charter editions, peer-reviewed articles); medium-low when it is a community-tree paste | Always crawl the URL list. Treat embedded scholarly transcripts as primary content for the cross-walk. |
| Trailing Notes / free-form contributor pastes | Very low | Note presence, do not adopt as fact |

### Era variance
Calibrate expectations to the ancestor's era:
- **Medieval (pre-1300)**: usually carry FMG MedLands and Latin charter excerpts in the Sources layer. Pattou (Racines Histoire), Geni, WikiTree often appear as URL companions. Domesday and chronicle citations expected.
- **Late medieval / early modern (1300–1700)**: parish records, wills, heralds' visitations, IGI extracts. Look for *Visitations of Norfolk*, *Genealogist*, county histories.
- **Modern (post-1700)**: census records, BMD certificates, gravestone indexes, FindAGrave, naturalization records. Less embedded scholarly transcript, more record-image links.

If the era's expected primary-source layer is missing, that is itself a finding worth recording.

## Structured-field friction discipline
Even when the structured FGR fields are wrong, do not silently discard them. The FS Family Tree is a public artifact and the user may later update it to reduce future-pass friction. For each material discrepancy between the FS structured field and the repo:

- record the FS field value verbatim (date, place, name, PID where applicable)
- record the repo's competing value with its citation
- mark whether the FS value is **sourced** or **unsourced** within the export itself
  - **unsourced in FS** → flag for the "FS Tree update suggestions" section: candidate to push our value back to FS with our source
  - **sourced in FS** → name the FS-cited source and evaluate it against the repo's source(s). If the FS source is independently credible, keep the conflict open in research rather than collapsing it

Surface all of this as a top-level "FS Tree update suggestions" section in the assessment MD.

## URL triage discipline
URLs in the Sources section must be **crawled, not skipped**. FS exports routinely cite pages which carry material content beyond what the export embeds.

Sort each URL in the assessment MD into one of three buckets:

- **Bucket A — auto-fetched**: successfully retrieved via `WebFetch` or local download. Record what was new and what was redundant. Add a one-line note when a URL turned out to be richer than expected (e.g., scholarly chart-genealogy with critical apparatus).
- **Bucket B — needs human / login**: returned an auth wall, JS-only render, certificate error, paywall, FS-session requirement, or otherwise refused automation. List each one with: URL, expected content type, observed failure mode, suggested human action (browser visit, FS-logged-in fetch, paste contents back into chat). Bucket B is the **handoff list** for browser-plugin / Claude co-work / interactive follow-up. Keep it actionable.
- **Bucket C — redundant / low-value**: already substantively embedded in the FS PDF, already in the repo's source canon (e.g., Daniel Gurney, Hannay, Pettigrew, Farrer, Loyd, Keates-Rohan, Richardson), or a known-low-value aggregator (Ancestry tree links, RootsWeb WorldConnect). Justify the skip in one line.

When a URL matches an existing entry in `data/sources.json` (by `sourceId` or URL substring), say so explicitly.

## Detail-carrying discipline
The assessment MD must carry detail forward, not summarize it away. Specifically:

- entire passages and surrounding text where ancestors, places, and relevant content is mentioned 
- reproduce Latin charter excerpts and primary-source quotations **verbatim** where they appear in the export, with numbered references preserved (e.g., FMG's `[875]`, `[893]`)
- preserve specific dates (year, month, day where given), place spellings, witness lists, and chronological reasoning chains
- when a scholarly source brackets a date or claim as uncertain (`[...]`), preserve the brackets in the MD
- when an excerpt names multiple persons, preserve all names, not just the subject
- when a Latin / Old French quotation is given, preserve original orthography
- when there is scholar dissents from FMG, preserve **both** positions — do not pick a winner in the assessment MD

A reader of the assessment MD should be able to draft the Phase-1 patchset using only the MD plus the original PDF — without re-reading PDF pages for ordinary structural cross-walk facts. They may reopen the PDF for very long charter texts, but not for the cross-walk.

## Assessment MD shape
Use `assessment-template.md` next to this `SKILL.md` as the starting structure.

Top-level sections, in order:
1. **Source-format anatomy** — one paragraph noting layer peculiarities of this specific export, total page count, and the apparent dominant scholarly tradition (DG, FMG, Pattou, etc.)
2. **Cross-walk: FS export vs. repo**
   - 2.1 Concordant facts (FS confirms repo)
   - 2.2 Net-new content worth promoting — *with verbatim transcripts where applicable*
   - 2.3 FS conflicts with repo (FS likely wrong but worth recording)
   - 2.4 Spurious / over-claimed structured-field content (the "extra children" problem and similar generation-sliding errors)
3. **FS Tree update suggestions** — discrepancies where our value is better and FS is unsourced
4. **URL triage** — Bucket A summary, Bucket B handoff list, Bucket C justified skips
5. **Patchset readiness sketch** — what a Phase-1 patchset would probably do, by destination file. Sketch only; the actual patchset is `research-intake-prep`.
6. **Open items still requiring human judgment** — three-way scholarly disagreements, claims that depend on a primary source not yet obtained, etc.

## Batching note
When multiple FS exports are processed in series for a contiguous lineage segment (e.g., the Norman seigneurs G30–G37, or a Norfolk junior-line cluster), MedLands and Pattou pages are typically shared across the segment. In that case:

- cite shared transcripts once in a "shared sources" preamble at the top of the batched assessment MD
- keep per-ancestor cross-walk sections fully detailed (conflicts and additions are per-ancestor)
- run URL triage once at the batch level for shared URLs and per-ancestor for export-specific URLs

Recommended batch size is 3–5 contiguous ancestors in the same scholarly neighborhood. Beyond that, the cross-walk grows unwieldy for human review.

## Companion-file convention
Companion documents collected from URL crawls during this skill (e.g., a downloaded research PDF, a saved Geni page) live under `sources/FS/<PID>/` next to the originating FS export. They are committed alongside the export. The skill itself does not stage or commit; the user does that as a buttoning-up step.

## Success condition
The MD is good enough that a second pass (`research-intake-prep`) can produce a Phase-1 patchset using only the MD, with the URL triage Bucket B already actioned by the user via interactive browser session.
