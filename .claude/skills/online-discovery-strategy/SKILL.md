---
name: online-discovery-strategy
description: Source-agnostic strategy for any online or repo discovery — two reasoning gates (objective, source) and cause-matched query technique (variants, wildcarding, token-anchoring) to apply in proportion to how much names vary, transcripts are dirty, or the target resists searching. Read before designing any non-trivial search; per-source mechanics live in the source's own skill.
---

A thinking aid for *designing* a search — not a checklist to run. The point is to get the most out of an approach: reason about it, be creative, blend techniques, adapt as results come back — applying each below in proportion, a light touch in clean conditions and heavier, combined ones as the material gets messier. It's judgment, not a formula. The failure this guards against is the opposite — going mechanical, fixating on one query shape, and mistaking a miss for a dead end. When a search underperforms, the fix is almost always a smarter approach, not more of the same.

Up front, before querying, spend real thought enumerating *how the target could appear or hide* and *where it could live* — not only suffix/middle spelling but first-character and whole-word corruption, dictionary-"snapped" forms, the source's own index head-forms, and the record types, venues, and even web-indexes that might hold it — then size the objective and decompose, widen, or narrow it accordingly. Treat every list and example in this skill as a seed, not a ceiling: the dimensions are open-ended, so reason past the named techniques the first time rather than running them and stopping. A zero — or a single source or index checked — is a prompt to widen, because coverage is patchy and differs by source (by year, geography, and online vs offline), so confirm coverage before believing an absence.

## Gate A — Objective awareness

- **Goal, not tool.** Stay anchored to what you're actually after (the will, the person, the fact), not the source you happen to be in. The objective is an onion: a specific task at the core, wrapped in wider layers of discovery. A miss in one source is a signal to *pivot and widen outward*, not a negative.
- **Ground first.** Before searching online — and before drafting, editing, or auditing — establish what the repo already knows (via repo_search and the subject's companion/place/topic file). Usually the answer, or the precise open delta, is already held; work the delta after the known knowns. When a source fails, return here before concluding anything.

## Gate B — Source awareness, and matching the query to it

Characterise the source before choosing terms — and don't collapse it to "printed vs manuscript." Three independent dimensions drive the approach:
- **Capture fidelity** is a spectrum, not a binary: modern clean OCR → imperfect OCR of early-modern print (long-s, ligatures, broken type) → typed abstracts/indexes → variable manuscript transcription → untranscribed image. High fidelity supports exact terms and co-occurrence; low fidelity shatters the target into "salad."
- **Spelling and language** vary *independently of fidelity*: a perfectly-captured 1600s clerk still wrote "Gournay," in English/Latin/French forms with period conventions. Genuine spelling variance is not a capture error.
- **Index model** — extracted-name index vs raw OCR vs structured fields. This decides whether a name surfaces even when its surrounding text is salad, and which constraints help vs. hurt.

From that reading, **anticipate how the source is likely to hold your target, and choose terms to bridge the gap — reaching for each technique in proportion to how likely its gap is, and blending freely:**
- **The original may have spelled the name differently** (a property of the record itself, not its capture) → **name variants** from `data/search-variants.json`, by era + conservative/broad/all as a scalpel; widen the set as that likelihood grows. Enumerated and precise — prefer over a wildcard when the set is known, since a wildcard drags in unrelated surnames.
- **The rendering may be imperfect** (OCR or transcription error, which can fall anywhere in the word) → **wildcarding** placed where the error is likely — not just the suffix; internal/multi-position — plus the registry's "broad" mangle forms. Tune to geography: include snap-targets with no local family, exclude those with their own (`Gorn*` recovers mangled Gurneys; `Garn*` swamps with Garner).
- **The name may not survive as a searchable string at all** (salad, or simply not indexed under its name) → **token / transitive anchoring**: drop the target name and search the reliably-captured surroundings. Convert a manor to its parish (modern, period, and mangled spelling), then co-occur it with a distinctive forename or rare in-law surname — `+"<parish>" +<in-law>` finds the document the name-anchored query misses, often with no target term at all.
- **The container may be findable even when the person is not** → **container resolution**: when name-search underperforms — dirty transcripts, no name-extraction, or simply no will — resolve the *container* (the film/DGS number, the catalogue/fonds record, the manor and its Manorial Documents Register entry) and read it directly. Across the 2026-07 campaign, film-number and fonds lookups consistently out-performed name-search: the target sits in a known container whose catalogue entry carries the parish and year the name-index lacks. **MDR-first for no-will problems** — where no probate survives, the manor court that governed the copyhold names the heir at the tenant's death (surrender/admission), so resolve the manor and its court-roll fonds rather than hunting a will that was never made.

Two more disciplines from the same source reading:
- **Don't over-constrain dirty/partial data.** Multi-field AND queries (name + spouse + father) and tight date filters false-negative — the record often lacks those very attributes, and recorded dates are approximate or only partially indexed. Start with the fewest reliable constraints, widen, and confirm breadth before trusting a low/zero count.
- **Verify before believing a zero or promoting a hit.** Confirm the source was actually searchable for your target (in coverage, authenticated, correct index) before treating absence as evidence. Mine each hit's full text for places, forenames, and associated families to judge relevance and expose lookalikes; never promote a forename or kinship from a salad/Latin transcript without an image read.

## See also
- `data/search-variants.json` — the variant registry (eras; conservative/broad/all)
- `.claude/skills/familysearch-fulltext-research/SKILL.md` — FamilySearch FTS mechanics
- `.claude/skills/findmypast-record-search/SKILL.md` — FindMyPast mechanics
- `tools/repo_search_README.md` — repo search-and-access tool
