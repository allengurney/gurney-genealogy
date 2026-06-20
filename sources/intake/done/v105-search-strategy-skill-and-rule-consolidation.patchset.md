**Done:** 2026-06-20 04:14 PT

# Patchset v105 — search-strategy skill + governance consolidation

Governance changes only (AGENTS, rules, skills, the leads tool) — no `data/sources.json`, no `sourceId`, no leads, no validations. Two intents: (1) **add** a source-agnostic search-strategy skill and the small punch-list rules we aligned on; (2) **reduce** the governance surface by moving the agnostic strategy *out* of the FamilySearch skill (which keeps only mechanics) and de-duplicating fact-sheet citation rules. Item 6 is **optional** — strike it during review if not wanted.

Operations use `~~~old` / `~~~new` fences (tildes, so inline backticks inside the content are literal). Apply each as a verbatim `str_replace` (or new-file write) in the order given.

---

## Item 1 — promote — NEW FILE: `.claude/skills/online-discovery-strategy/SKILL.md`

New file write, full body:

~~~
---
name: online-discovery-strategy
description: Source-agnostic strategy for any online or repo discovery — two reasoning gates (objective, source) and cause-matched query technique (variants, wildcarding, token-anchoring) to apply in proportion to how much names vary, transcripts are dirty, or the target resists searching. Read before designing any non-trivial search; per-source mechanics live in the source's own skill.
---

A thinking aid for *designing* a search — not a checklist to run. The point is to get the most out of an approach: reason about it, be creative, blend techniques, adapt as results come back — applying each below in proportion, a light touch in clean conditions and heavier, combined ones as the material gets messier. It's judgment, not a formula. The failure this guards against is the opposite — going mechanical, fixating on one query shape, and mistaking a miss for a dead end. When a search underperforms, the fix is almost always a smarter approach, not more of the same.

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

Two more disciplines from the same source reading:
- **Don't over-constrain dirty/partial data.** Multi-field AND queries (name + spouse + father) and tight date filters false-negative — the record often lacks those very attributes, and recorded dates are approximate or only partially indexed. Start with the fewest reliable constraints, widen, and confirm breadth before trusting a low/zero count.
- **Verify before believing a zero or promoting a hit.** Confirm the source was actually searchable for your target (in coverage, authenticated, correct index) before treating absence as evidence. Mine each hit's full text for places, forenames, and associated families to judge relevance and expose lookalikes; never promote a forename or kinship from a salad/Latin transcript without an image read.

## See also
- `data/search-variants.json` — the variant registry (eras; conservative/broad/all)
- `.claude/skills/familysearch-fulltext-research/SKILL.md` — FamilySearch FTS mechanics
- `.claude/skills/findmypast-record-search/SKILL.md` — FindMyPast mechanics
- `tools/repo_search_README.md` — repo search-and-access tool
~~~

---

## Item 2 — promote — `AGENTS.md`: repo_search-as-tool + ground-first (§0a), and skills-table pointer (§3)

### str_replace 2a — §0a, replace the discovery/Grep paragraph

~~~old
For discovery and research tasks where exploring the repo *is* the work, breadth is appropriate. For broad, multi-file, or footnote-heavy discovery — "what does the repo know about X," grounding a subject before online work, negative-result checks — reach for `repo_search.py` (next paragraph) first, **not** raw Grep. Reserve Grep / Glob for narrow, known-target lookups: a specific symbol, a known path, an existence check. Sequential full-file reads of large directories should be rare.
~~~
~~~new
**`repo_search.py` is the default tool for searching and reading-in repo content** — use it for any non-trivial lookup, in preference to Grep / Glob (which are reserved for a narrow known-target match — a specific symbol, a known path, an existence check — where their output is genuinely superior). **Ground before acting:** before online discovery, drafting, editing, or auditing, first establish what the repo already knows about the subject with `repo_search.py` and the subject's companion/place/topic file; work the *delta after the known knowns*. This is the single biggest guard against duplicative work. Sequential full-file reads of large directories should be rare.
~~~

### str_replace 2b — §3 skills table, insert the new row after the FindMyPast row

~~~old
| `findmypast-record-search/` | Operational recipes for FindMyPast indexed record sets (parish baptisms, banns & marriages, burials): URL-parameter search, dataset slugs, wildcard/spelling tactics, the spouse-search trick, reading results without opening paywalled images, coverage caveats. Read before any FindMyPast record-search task. |
~~~
~~~new
| `findmypast-record-search/` | Operational recipes for FindMyPast indexed record sets (parish baptisms, banns & marriages, burials): URL-parameter search, dataset slugs, wildcard/spelling tactics, the spouse-search trick, reading results without opening paywalled images, coverage caveats. Read before any FindMyPast record-search task. |
| `online-discovery-strategy/` | Source-agnostic search *design* — the two reasoning gates (objective, source) and cause-matched technique selection (name variants / wildcarding / token-anchoring). Read before designing any non-trivial online or repo search; the FS/FMP skills hold the per-source mechanics. |
~~~

---

## Item 3 — promote/reduce — `.claude/skills/familysearch-fulltext-research/SKILL.md`: add strategy pointer + auth gate, fix year filter, remove the now-agnostic strategy blocks

### str_replace 3a — add the strategy pointer under the opening paragraph

~~~old
Proven procedures for working FamilySearch Full-Text Search with an authenticated browser session (Claude-in-Chrome or equivalent). Established and battle-tested across the June 2026 John Gurney (G13) campaign. The companion *content-reliability* notes (what machine transcripts can and cannot be trusted for, catalogued false positives) live in `sources/validations/familysearch-fulltext-search.md`.
~~~
~~~new
Proven procedures for working FamilySearch Full-Text Search with an authenticated browser session (Claude-in-Chrome or equivalent). Established and battle-tested across the June 2026 John Gurney (G13) campaign. The companion *content-reliability* notes (what machine transcripts can and cannot be trusted for, catalogued false positives) live in `sources/validations/familysearch-fulltext-search.md`.

> **Search *strategy* (name variants, wildcarding, token/transitive anchoring, source-awareness) is source-agnostic and lives in [`online-discovery-strategy`](../online-discovery-strategy/SKILL.md) — read that first.** This file is FamilySearch FTS *mechanics* only: endpoints, parameters, extraction, image download, DGS mapping.
~~~

### str_replace 3b — fix the year-filter sentence in the `q.fullName` bullet (N5)

~~~old
Works on the JSON service too (`&q.fullName=rivett`). Pair it with a **tight year range** `f.recordYear1=<century>~<range>&f.recordYear0=<century>` (e.g. `f.recordYear1=1600~1630&f.recordYear0=1600`) for a precise window — far sharper than the whole-century filter below.
~~~
~~~new
Works on the JSON service too (`&q.fullName=rivett`). For a windowed search use the year filter on **`q.text`** (not `q.fullName`, which takes only the century filter): activate with `c.recordYear1=on`, then `f.recordYear0=<base>` **before** `f.recordYear1=<start>~<end>`, repeating the pair for multiple windows (order and the toggle both matter — omit either and it returns zero).
~~~

### str_replace 3c — add the auth gate after the URL-params block (N4)

~~~old
If the URL form ever errors, the landing-page form at `/en/search/full-text` has "Keywords" and "Image Group Number (DGS)" fields — but its collection-title autocomplete does not respond to scripted input; don't fight it.

**Getting a film's DGS number:**
~~~
~~~new
If the URL form ever errors, the landing-page form at `/en/search/full-text` has "Keywords" and "Image Group Number (DGS)" fields — but its collection-title autocomplete does not respond to scripted input; don't fight it.

**Verify authentication once, at the start of FTS work.** An unauthenticated session silently truncates results into false negatives: `q.fullName=gurney` returns ≈ 348k authenticated vs ~460 unauthenticated. Re-confirm any FTS negative under an authenticated session before trusting it. (The general posture — a source miss is a pivot, not a negative — is in `online-discovery-strategy`.)

**Getting a film's DGS number:**
~~~

### str_replace 3d — remove the "Wildcard calibration" block (moved to the strategy skill)

~~~old
(Group IDs like `M9S7-H4T` in result URLs are *not* DGS numbers.)

**Wildcard calibration:** `Gurn*` + `Gourn*` + `Garn*` outperforms hand-built spelling lists (a nine-variant manual sweep added nothing). But `G?rn?*` is too broad — swamped by *Garner*.

## 2. Reading results and record pages (shadow DOM)
~~~
~~~new
(Group IDs like `M9S7-H4T` in result URLs are *not* DGS numbers.)

## 2. Reading results and record pages (shadow DOM)
~~~

### str_replace 3e — remove the "Co-occurrence caveat" block (moved to the strategy skill)

~~~old

**Co-occurrence caveat (calibrated 2026-06-13):** `+Gurn* +"<place>"` AND-probes do **not** surface corrupt-transcript manuscript records — place + surname only co-occur in *clean-OCR printed* books (Burke, Visitations, Blomefield) and cross-collection false positives (e.g. Liège "de Gurnay", a Walloon family). The high-yield FTS vector for a Norfolk surname is **typed abstract/index typescripts** (clean OCR), not place/Latin co-occurrence over manuscript films. See `sources/intake/.../extended-fts-discovery-campaign.md` (2026-06 batch) for the full probe matrix and negative.
~~~
~~~new

~~~

### str_replace 3f — remove the "Drop the target surname … anchor on a co-token" block (moved to the strategy skill)

~~~old

**Drop the target surname when it's mined-out or salad — anchor on a *reliable* co-token instead (calibrated 2026-06-15).** Two complementary moves when the family surname (Gurney) has either been exhausted on direct hits or transcribes as salad in manuscript films:
- **Convert a manor name into its parish/town/entity** before using it as a term. Manors rarely appear verbatim; the *parish* does. Map first (e.g. "Gurney's Manor" → **Hingham**; "Old Hall" → **Great Ellingham / Ellingham Magna / Mickle Ellingham**; the Irstead manor → **Irstead / Neatishead / Smalburgh / Barton**, Tunstead Hundred). The repo's place files and fact sheets hold these manor↔parish mappings. **Also spell the place the period/OCR way, not just the modern way** — a Latin or 16th–17th-c. clerk's form, or an OCR mangle, often indexes differently: `"Elyngham"` (one *l*, *-yng-*) surfaced a 1563 will-abstract naming a Gurney supervisor that `"Ellingham"`/`"Ellingham Magna"` both missed. Try the modern, the era (`Elyngham`, `Ellyngham`, `Mickle Ellingham`), and a corrupt single-consonant form (`Elingham`) — but watch that over-loose forms (`Elingham`) pull in modern/overseas noise, so pair them with a second required token.
- **Co-occur the parish with a token that survives bad OCR — a distinctive forename or an in-law surname — NOT the target surname.** A clean forename ("Henry", "Anthony") or a rare in-law name ("Blennerhassett", "Spelman", "Lovell", "Heydon", "Browning") often transcribes intact on a page where "Gurney" became salad, so `+"<parish>" +<inlaw>` surfaces the family document the surname-anchored probe misses. Worked 2026-06: `+"West Barsham" +Blennerhassett` returned a Gurney pedigree (*"Henry Gurney … and Ellen Blennerhassett his wife"*) with **no Gurney term in the query**. **Prefer rare co-tokens** — rare in-law surnames give low, workable totals; common forenames (Anthony/Henry/Lovell) are swamped by modern/US records, so add the century filter (`f.recordYear0=16<nn>&c.recordYear1=on`) and triage hard. This same vector is how digitised **manor-court films** surface by parish (e.g. Great Ellingham court business sits inside the Buckenham rolls DGS 004389550; the Irstead manor inside the Smalburgh/Neatishead Gimingham court barons) — but note such films often **post-date** the family's tenure, so confirm the coverage years before assuming the target era is captured.
~~~
~~~new

~~~

### str_replace 3g — remove the "Dictionary-snapped OCR" block (moved to the strategy skill)

~~~old

**Dictionary-snapped OCR + local surname populations (calibrated 2026-06-13).** These collections' handwriting OCR is **name-dictionary-aided**, so a poorly-read surname snaps to the nearest *dictionary* surname — one manuscript "Gurney" sprays across `Gorney/Gorne/Gorner/Gurnee/Gornesly/Gorness/Gorneses` on a single page. Two consequences for building a term set:
- **Include snap-targets that are NOT an established surname in that geography** (Norfolk has no "Gorney" family, so `Gorn*` safely recovers mangled Gurneys) and **exclude snap-targets that have their own local population** (`Garn*` → the real Garner/Garnett family; this is why the long-standing `Gurn*/Gourn*/Gorn*` set is well-tuned and `Garn*` swamps). The safe set is **geography-specific** — re-judge it per county.
- **Disambiguate large same-surname populations before promoting.** In Norwich, most "Gurney" hits are the famous **Quaker banking Gurneys** (Hudson Gurney, John Gurney merchant, "May Gurney & Co"), a family distinct from the West Barsham gentry line — so a Norwich hit is *more* likely them than the target line. Use period/parish to separate (the Quaker line rises in the later 17th c.).
~~~
~~~new

~~~

### str_replace 3h — remove the "Read the whole transcript for context" block (moved to the strategy skill)

~~~old

**Read the whole transcript for context, don't binary-match the surname.** The match string alone (`Gurney`) is a weak signal in salad; mine each hit's full `content.textDocument` for buried **place names, forenames, and associated families** (`+Barsham|Ellingham|Harpley|… | Lovell|Spelman|Calthorpe|Lestrange|…`) to judge relevance. This both rescues relevance the surname alone misses **and** exposes false positives a binary place-match would mis-promote (e.g. "Gornsey" = *Guernsey*, not Gurney; "Hardingham" as a juror's **surname**, not the manor). Yield tracks OCR quality: context-mining rescues **clean printed** calendars/indexes but rarely manuscript salad — and a "1910 deeds" film can in fact be a clean-OCR medieval–Tudor deeds *calendar* worth a full sweep (DGS 004389182).
~~~
~~~new

~~~

---

## Item 4 — reduce — `.claude/rules/fact-sheets.md`: de-duplicate the "Citation rigor" section against `citations.md`

### str_replace 4a — replace the whole `## Citation rigor` block

~~~old
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
~~~
~~~new
## Citation rigor
General footnote discipline — every factual sentence/cluster cited, full-form footnotes, URLs as hyperlinks, all material supporting sources, inferential claims phrased visibly — lives in `citations.md` and applies here. Fact-sheet-specific additions:
- Narrative paragraphs must not rely on vitals/highlights citations alone. During any edit, audit the Narrative sentence-by-sentence (or tight cluster) and add nearby footnotes; if support cannot be found, preserve the claim and ask rather than silently removing, softening, or forcing a citation.
- Every children-table row, plus any "no further children" note, carries a visible source footnote (a shared pedigree footnote may repeat across rows).
- Patchset placeholders (`nNEW1`, `ref-NEW1`, visible `NEW1`) never remain in a finished fact sheet. Before completing a citation batch, sweep: no `NEW` labels, all `href="#n..."`/`href="#ref-..."` anchors resolve, IDs unique, labels match numbers, Narrative/Children have coverage.
~~~

---

## Item 5 — promote — `tools/research_leads.py`: strengthen the pre-pull checklist (both occurrences)

### str_replace 5a — the dict/JSON checklist string

~~~old
                    "Read/grep the companion named in Source ref; the companion is more authoritative than stale CSV status.",
~~~
~~~new
                    "Ground first via repo_search + Read (not Grep): read the Source-ref companion AND the subject's ancestor/place companion before any online work; they are more authoritative than the CSV and usually already hold the answer or the exact delta.",
~~~

### str_replace 5b — the markdown checklist string

~~~old
            "- Read/grep the companion named in `Source ref`; the companion is more authoritative than stale CSV status.",
~~~
~~~new
            "- Ground first via repo_search + Read (not Grep): read the `Source ref` companion AND the subject's ancestor/place companion before any online work; they are more authoritative than the CSV and usually already hold the answer or the exact delta.",
~~~

---

## Item 6 — reduce — `.claude/rules/continual-improvement.md`: compress the availability section (**OPTIONAL — strike during review if not wanted**)

### str_replace 6a — replace the `## Classify every "pull" by online availability` section

~~~old
## Classify every "pull" by online availability
Whenever AI lists future research pulls (in a research file, a patchset, an
open-questions section, a summary, or anywhere else), each pull must carry an
explicit availability tag — one of:

- **Available online** — AI knows for sure the source is accessible online,
  because AI has verified the URL, fetched the page, or has a recent reliable
  pointer to a digitised copy (HathiTrust, Internet Archive, Gallica, archive
  catalogue, university repository, etc.).
- **Unknown online** — AI does not know whether the source is online. Use this
  as the default when AI has not actually tried to find a digitised copy.
- **Not online** — AI has explicitly looked and found references indicating
  the source is not digitised, the manuscript is in private hands, the
  archive has restricted access, or the only known copy is held in a physical
  repository without a digital edition.

The tag goes inline with each pull, e.g.: "EYC vol. 8, pp. 6–7 (Available
online — archive.org)" or "Cordier MS *Histoire de Gournay* (Not online — held
privately, never published in transcription beyond Potin 1842 extracts)."

This lets the user decide which pulls AI can pursue immediately vs. which
require library access or other manual work.
~~~
~~~new
## Tag every "pull" by online availability
Whenever AI lists future pulls (research file, patchset, open-questions, summary), tag each inline as **Available online** (URL/digitised copy verified), **Unknown online** (default — not yet checked), or **Not online** (looked; only physical/restricted/un-digitised). Example: "EYC vol. 8, pp. 6–7 (Available online — archive.org)." This lets the user split pursue-now from needs-library-access.
~~~

---

## Notes for Phase 2

- No `data/sources.json`, `sourceId`, validation, or lead changes.
- Item 1 is a new file; Items 2–6 are in-place `str_replace`s.
- Items 3e–3h delete blocks: the `~~~new` fence is intentionally empty (the leading blank line in each `~~~old` is part of the match, so the block and its preceding blank line are both removed).
- After applying, the FamilySearch skill should contain only mechanics; confirm the `online-discovery-strategy` cross-links resolve.
