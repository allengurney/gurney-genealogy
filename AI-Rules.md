# AI-Rules.md

Operating rules for Claude working in this repo. **Read before first substantive response in any session.** Rules are living — edit in place when warranted; no confirmation needed for minor refinements. Flag significant changes in commit message.

---

## 0. Session start

On new session: read `AI-Rules.md`, `README.md`, most recent `research/log/*.md`. Check if `data/sources.json` changed since last reference. For a specific ancestor, read both `fact-sheets/g{NN}-{slug}-fact-sheet.md` and `research/people/g{NN}-{slug}-fact-sheet.research.md`.

---

## 1. Identity

User: Allen Lawrence Gurney, b. 1972, Portland OR. Dual projects: biography of Brig. Gen. William Gurney (1821–1879, G6); 37-generation genealogy site at genealogy.allengurney.com. Not a professional genealogist; accepts reasoned deduction from indirect evidence when noted. Reviews output critically; corrections are authoritative and incorporated immediately.

---

## 2. Repo map

```
data/            sources.json, places.json, places_detail.json, ancestors v24.json (canonical structured data)
fact-sheets/
  g{NN}-{slug}-fact-sheet.md    ← PUBLISHED narrative only (stable, polished, Allen's prose)
research/
  people/        ← RESEARCH for ancestors AND non-ancestors
    g{NN}-{slug}-fact-sheet.research.md   ← paired research companion to each fact sheet
    g{NN}-{slug}.md                        ← pre-fact-sheet staging (no fact sheet yet)
    {descriptive-slug}.md                  ← non-ancestor subjects (Margaret Rybett, etc.)
  places/        one file per geographic locus
  topics/        cross-cutting problems (Protestation Returns, two-Francis, etc.)
  case-files/    long-form investigations (candidate-b.md)
  log/           YYYY-MM-DD.md — INDEX ONLY, points into target files
  migration-tracker.md
sources/
  corpus/        full-text source extracts (text preferred over PDF)
  media/{id}/    screengrabs, record crops (in-repo while small)
  validations/   per-source audit trail: WHAT was examined, scope/limitations — NOT findings
site/            Eleventy source (output excluded via .gitignore)
tools/           lineage-specific artifacts (pedigree-explorer.html)
```

**Key structural principle:** `fact-sheets/` is published-only. All research — for ancestors with fact sheets, ancestors without fact sheets, and non-ancestors — lives under `research/people/` (or `places/`, `topics/`, `case-files/` as appropriate).

---

### What goes where — narrative vs. research companion

**Narrative file** — crisp ancestor summary. A sentence or two per event. The published view.

**Research companion** — everything that supports, elaborates, or complicates the narrative:
- Full source extracts (e.g., the fact sheet describes an event in two sentences; the companion has the multi-paragraph source passage and additional details from a second source).
- Lesser facts: important for research continuity but not for an ancestor summary.
- Triangulation detail: how sources were cross-referenced, which details align or conflict.
- Negative results, conjectures, raw transcriptions.

No promotion workflow. New findings go directly where they belong: if it's a fact-sheet-level finding (corrects a date, fills a gap, same weight as existing content), update the narrative. If it's detail, context, source extract, or supporting material, it goes in the companion. This is a judgment call, not a rule engine.

### Log discipline
`research/log/YYYY-MM-DD.md` = index only. Points into target files. **If substantive content is accumulating in a log entry, move it to the target file.**

---

## 5. Lineage status values

- **Direct** — G1 (Allen himself)
- **Confirmed** — multiple independent primary or highly reliable sources
- **Probable** — best-supported hypothesis; active case file
- **Uncertain** — attestation exists but evidentiary gap
- **Tradition** — transmitted family lore without contemporary document
- **End of Record** — explicitly beyond the knowable
- **Related** — (also collateral) never confuse with direct-line status.

---

## 6. Principles

### Uncertainty is quantified, not hedged
"Probable (~55–60%)" beats "fairly likely." Attach to specific claims, not whole documents.

### Negative results are first-class
"Searched X, found nothing" is a finding. Log it **on the subject's file**, not on the source's. Examples: Peter absent from all England Gurney records; no John Gurney in Bucks Protestation Returns (London/Essex non-surviving, so Francis's absence uninformative).

### Conclusions don't outrun evidence
Overclaiming is the cardinal sin. Rejected patterns: "no one left for New England is not provable"; Sunday-baptism test; tight 1618 timeline without basis.

### Conflicting sources exposed, not reconciled by fiat
Document the conflict. Preserve both positions until primary evidence resolves.

### Confidence conservation for living people
G0–G2 and living collaterals: minimize detail in public files. Birth year, general geography OK; no addresses, no sensitive detail.

---

## 7. Standing facts (don't re-derive)

### The 8 critical corrections
1. Francis G14 died **9 Jan 1646/7** (FreeREG) — NOT 1641 (Boyd) or 1650.
2. Junior Norfolk branch through **Walter (G31)** — NOT Hugh IV/V (collateral).
3. **Sir John Gurney (d.1408)** is collateral. Direct: Edmund G23 → Robert G22 → Thomas I G21 → Thomas II G20.
4. **Two Francis Gurneys** coexist: G14 Merchant Taylor (St Benet Fink) + laceweaver (St Giles Cripplegate, wife Mary). Costessey = laceweaver.
5. **Margaret Rybett died c.1616–17**, not c.1618.
6. **John Gurney-1 born c.1609–12** (revised from c.1603).
7. **"Peter"** absent from all Gurney families; from wife Mary's unknown family.
8. **Eudes (G~37)** is Tradition, not Confirmed.

### Structural facts
- G1 = Allen. Numbers increase going back.
- West Barsham entered via Wauncy inheritance (Edmund G23's wife Katherine); held until 1661.
- Francis G14 = sixth son of Henry G15.
- `data/ancestors v24.json` = current canonical ancestor data file. `ancestors v23.json` is legacy — DO NOT USE. See `research/topics/ancestors-json-audit.md` for known data-quality issues inherited from v23.
- `data/places.json` + `data/places_detail.json` = canonical two-layer place spine. `locations.json` was retired.

---

## 8. Source-specific flags

### Daniel Gurney, *Record* (1848)
Primary secondary source G15–G35. Text in `sources/corpus/daniel-gurney-part-{1,2,3,4}.md`. OCR: "Wilham"/"William" ~6%, "Basiha"/"Basilia" ~16%. Page markers: `## p. N (#M) ##` (cite N). Parts I/II/III/IV present. Supplement text extracted (Google Books OCR) into `sources/corpus/daniel-gurney-supplement.md` — OCR quality varies, especially for Latin passages and marginal notes. Rye appendix NOT yet in corpus (text extraction pending).

**Supplement vs. Parts I–III pagination test.** The 1858 Supplement runs pp. 725–1096. Any "Supplement" citation with a page number below 725 is miscited (should be DG-I, DG-II, or DG-III). See `research/topics/dg-citation-audit.md` for the 2026-04-16 sweep that caught and fixed six G20–G37 companion miscitations.

### Anderson, *Great Migration Directory* (2015)
"Unknown" origin = implicit rejection of Banks. Arrival 1636 vs. Weymouth 1641 — unresolved.

### Banks/Brownell (1937)
East Anglian placement weakens Candidate A more than B.

### Ancestry Norfolk collections
Bishop's transcripts + IGI, not original registers. Negative ≠ closed.

### Boyd's marriage index
Known misreads (Francis death 1641 → 1646/7). Verify against images.

### Pennyghael (pennyghael.org.uk/Gurney.pdf)
Ryvett claim confirmed against NRO PD 12/1 (March 2026).

---

## 9. Verification order

1. Primary source image — gold standard
2. Primary source transcription (validated)
3. Scholarly compiled work (DG, Blomefield, HoP)
4. Indexed databases (Anderson, Boyd, Ancestry — flag index-not-image)
5. User-submitted trees — leads only, never citable

---

## 12. Tone

Concise, direct, honest. Pushback over sycophancy. "I was wrong" when wrong. No filler.

---

## 13. Efficiency — don't over-engineer

### Stop retrying

If a tool call fails or produces an unexpected result, try **once** more with a clear correction. If the second attempt also fails, stop and surface the problem rather than grinding through attempts 3+. Allen's time is more valuable than the work being done.

### Directory listings

Don't fetch full directory listings unless you actually need them. Knowing that `fact-sheets/` contains G04–G37 is sufficient for most tasks; the actual file list is only needed when looking for something specific.
