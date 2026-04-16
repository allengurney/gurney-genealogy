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
data/            sources.json, locations.json, ancestors v23.json (canonical structured data; note space in filename)
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

## 3. Workflow

### Default mode: Claude commits via MCP

Allen rarely wants to run things locally. Claude proceeds via MCP for all ongoing research work — committing findings, notes, fact updates, new files, edits to research companions. Don't ask Allen to do something locally that MCP can do.

### The one exception: bulk file restructures

For one-time bulk operations across 10+ files (splitting, renaming, restructuring), a tested local script is acceptable when MCP would require dozens of round-trip tool calls. Claude provides the script; Allen runs it once and pushes. After that, all subsequent commits to the restructured files go through MCP.

This is a narrow exception. The default is MCP. If in doubt, do it via MCP.

### The paired-file rule: every ancestor gets two files

Each direct-line ancestor has a paired set:

**Narrative file** (`fact-sheets/g{NN}-{slug}-fact-sheet.md`):
- YAML front matter, vitals, highlights, children table, narrative prose, citations, related links.
- Allen's wordsmithed work. Respect the prose — edit only when facts change.
- Published to the website via Eleventy. Stable. Changes only when the published content changes.

**Research companion** (`research/people/g{NN}-{slug}-fact-sheet.research.md`):
- The lab notebook. All accumulated research detail for this ancestor.
- Sections: Working Notes, Open Questions, Sources Consulted, Conflicting Information, Search Notes & Next Steps, Working Hypotheses, Raw Data / Transcriptions.
- This is the file that grows during research sessions. Frequent small commits here.
- Eleventy build skips `*.research.md` files — no HTML comment markers needed.

**Why split — and why the companion lives in `research/people/`:** The narrative file stays small and stable (~5–15KB) in `fact-sheets/`, which is a clean published-content directory. The research companion absorbs frequent commits in `research/people/` alongside non-ancestor research (Margaret Rybett, laceweaver Francis, candidate matches). A researcher looking at a person — ancestor or not — finds all accumulated research in one place.

*Filename note:* existing companions carry the `-fact-sheet.research.md` suffix as an artifact of the original local split. New files created for ancestors who don't yet have a fact sheet should use `g{NN}-{slug}.md` (pre-fact-sheet staging convention). If and when they get a fact sheet, rename to `g{NN}-{slug}-fact-sheet.research.md`.

### What goes where — narrative vs. research companion

**Narrative file** — crisp ancestor summary. A sentence or two per event. The published view.

**Research companion** — everything that supports, elaborates, or complicates the narrative:
- Full source extracts (e.g., the fact sheet describes an event in two sentences; the companion has the multi-paragraph source passage and additional details from a second source).
- Lesser facts: important for research continuity but not for an ancestor summary.
- Triangulation detail: how sources were cross-referenced, which details align or conflict.
- Negative results, conjectures, raw transcriptions.

No promotion workflow. New findings go directly where they belong: if it's a fact-sheet-level finding (corrects a date, fills a gap, same weight as existing content), update the narrative. If it's detail, context, source extract, or supporting material, it goes in the companion. This is a judgment call, not a rule engine.

### Findings vs. source provenance — the critical distinction

**Findings go to the subject. Source files are thin audit trail.**

When examining a source (parish register, published compilation, archival document), the evaluation produces two kinds of output that land in different places:

1. **Findings about a person, place, or topic** → go to that subject's file:
   - Facts established → `research/people/g{NN}-{slug}-fact-sheet.research.md` (or pre-fact-sheet stub, or non-ancestor file)
   - Geographic findings → `research/places/{place}.md`
   - Cross-cutting analysis → `research/topics/{topic}.md`
   - Long-form hypothesis work → `research/case-files/{case}.md`
   - Open items / action items → on the subject's file, not the source's
   - Negative results → on the subject's file (a negative about John goes on John's file)

2. **Source provenance** → `sources/validations/{source-id}.md`:
   - WHAT was examined (which volume, which pages, what scope)
   - HOW it was examined (image analysis, text search, paleographic review)
   - Scope limitations (what was NOT examined)
   - Pointer(s) to where findings landed

The validation file is deliberately thin. It answers "what did we do with this source?" It does NOT answer "what did we learn about John?" — that answer lives on John's file.

**Example:** Evaluating Anderson's *Great Migration Directory* entry for John Gurney-1 produces:
- John's file gets: "Anderson GMD p. 158 gives origin Unknown, arrival 1636, settlements Boston + Braintree only" + the 6-source citation pull list + open items (pull TAG, pull NEHGR, reconcile 1636 vs 1641).
- Anderson's validation file gets: "Examined p. 158 extract on 2026-04-08. Full directory not extracted. Findings logged at `research/people/g13-john-gurney-1.research.md`."

This prevents findings from being buried where no one researching the subject would look.

### Working Notes section (in research companion)

The Working Notes section is a running field journal. Rules:

**Include actual content.** Not "found a register entry" but the entry itself: dates, names, parish, transcription, what it establishes. If Allen shares a record, capture the substance.

**Organize by topic/finding/source, not by date.** Group related observations under descriptive sub-headings. Use date stamps within entries when useful for the trail, but the primary structure is thematic. If no obvious topic grouping, fall back to chronological.

Example structure:
```
## Working Notes

### East Dereham sibling search
2026-04-14 — Searched Ancestry Norfolk parish collection for siblings of Francis G14.
Entry A: "Edward son of ffrancis Gurney" bpt. [date], East Dereham. Confirmed.
Entry C: "Agnes daughter of ffrancis Gurney" bpt. [date]. Confirmed.
No match for Peter in any East Dereham entry 1580–1640 (expected negative).

### Basilia Flaitel connection
2026-04-14 — DG-I-48 names Basilia's niece Anfride at Bec alongside Eva (wife of 
William Crispin). Anfride not in the pedigree. Who is she? Possible Flaitel 
collateral worth tracing if Flaitel scholarship exists.

### OCR quirk log
"Basiha" appears 10× in DG corpus vs. 52 correct "Basilia." Flag when quoting.
```

### research/people/ — both ancestors and non-ancestors

This directory holds:
- **Ancestor research companions** (paired to fact sheets): `g{NN}-{slug}-fact-sheet.research.md`
- **Pre-fact-sheet ancestors:** `g{NN}-{slug}.md` — when an ancestor doesn't yet have a fact sheet but research is accumulating (e.g., John Gurney-1 at G13 while Candidate B is still probable-not-confirmed)
- **Non-ancestor research subjects:** Margaret Rybett, laceweaver Francis, Ann Gurney of Hingham, candidate matches, disambiguation targets — use descriptive slugs without generation prefix

### Commit cadence
Commit in the moment when durable content surfaces — not at session end. Atomic commits (one logical change each). Descriptive message. Don't batch unrelated changes.

### Log discipline
`research/log/YYYY-MM-DD.md` = index only. Points into target files. **If substantive content is accumulating in a log entry, move it to the target file.**

---

## 4. Citation discipline

### Citation key format
- `[DG-I-278]` = Daniel Gurney, *Record*, Part I, p.278
- `[DG-II-524]` = Part II, p.524
- `[DG-III-525]` = Part III, p.525
- `[DG-Supp-{page}]` = 1858 Supplement
- `[NRO-PD12/1]` = Norfolk Record Office, PD 12/1
- `[HoP-Gurney]` = History of Parliament Online
- `[Blom-Harpley]` = Blomefield, *History of Norfolk*, Harpley entry
- `[Anderson-GMD]` = Anderson, *Great Migration Directory* (2015)
- `[Banks-Brownell]` = Banks/Brownell, *Topographical Dictionary* (1937)

### Rules
- Every fact in `data/` with a source dependency cites a `sourceId` defined in `data/sources.json`.
- Orphan facts (no source) and orphan sources (no facts cite them) are both bugs.
- When quoting Daniel Gurney text from `sources/corpus/`, cite book page (the `N` in `## p. N (#M) ##`), not scan sequence.
- **Flag OCR variant characters** when quoting: "Wilham" (→William), "Basiha" (→Basilia), hyphenation breaks. Normalize silently when quoting is not the point.
- Index entries (Boyd's, Ancestry, etc.) require image verification before treatment as established. See §9.

---

## 5. Lineage status values

- **Direct** — G1 (Allen himself)
- **Confirmed** — multiple independent primary or highly reliable sources
- **Probable** — best-supported hypothesis; active case file; e.g., John Gurney-1 (G13)
- **Uncertain** — attestation exists but evidentiary gap; e.g., Hugh de Gournay I (G36)
- **Tradition** — transmitted family lore without contemporary document; e.g., Eudes (G~37)
- **End of Record** — explicitly beyond the knowable
- **Collateral** — never confuse with direct-line status.

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
- `data/ancestors v23.json` = current ancestor data file (note space in filename). See `research/topics/ancestors-json-audit.md` for known data-quality issues and the filename-vs-convention question.

---

## 8. Source-specific flags

### Daniel Gurney, *Record* (1848)
Primary secondary source G15–G35. Text in `sources/corpus/daniel-gurney-part-{1,2,3}.md`. OCR: "Wilham"/"William" ~6%, "Basiha"/"Basilia" ~16%. Page markers: `## p. N (#M) ##` (cite N). Parts I/II/III present. Supplement + Rye appendix NOT yet in corpus.

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

## 10. Open threads (April 2026)

- **Candidate B** ~55–60%. Case file to be built: `research/case-files/candidate-b.md`.
- **Anderson 1636 vs. Weymouth 1641** — unresolved.
- **East Dereham Entry E** — paleographic: ffrancis > Nicholas; further validation useful.
- **Tier 1 pulls**: TAG 10:70–73, NEHGR 62:94 — not yet obtained.
- **Fact sheets remaining**: G21–G15 (G14 exists; G13 John Gurney-1 pre-fact-sheet).
- **Supplement + Rye** — corpus extraction pending.
- **Landholdings and places** — 17 place files for the G20–G37 range created 2026-04-16; linked from each research companion. See `research/places/`.

---

## 11. Tooling

- **GitHub MCP** is the default for all commits — see §3 "Default mode."
- **Eleventy** build skips `*.research.md` files. Cloudflare Pages deploys from repo on push.

---

## 12. Tone

Concise, direct, honest. Pushback over sycophancy. "I was wrong" when wrong. No filler.

---

## 13. Efficiency — don't over-engineer

### Transcript migration: row-by-row, not inventory-first

When processing a chat transcript for migration, the fast path is:

1. **One or two** `conversation_search` calls to surface the relevant content. Stop when you have the material.
2. Step through the transcript linearly. For each substantive row/finding, decide its target file and add it.
3. Commit in batches of related changes (one subject file = one commit; multiple small subject files = one batched commit is also fine).
4. Move on.

Do NOT build a comprehensive inventory table before writing anything. Do NOT run 5+ searches "to make sure." The transcript is what it is; search it enough to find the material, then process it.

### Small file edits: just write the file

For files under ~50KB (sources.json, any markdown research file, fact sheets):
- `get_file_contents` to fetch
- edit inline
- `create_or_update_file` with the full new content and the returned SHA

Do NOT write a Python script to surgically edit a 20KB JSON file. The full-paste round-trip is faster and more reliable than scripting around edge cases.

For files over ~200KB or operations across many files, consider `push_files` (multi-file commit) or the §3 bulk-script exception.

### Stop retrying

If a tool call fails or produces an unexpected result, try **once** more with a clear correction. If the second attempt also fails, stop and surface the problem rather than grinding through attempts 3+. Allen's time is more valuable than the work being done.

### Directory listings

Don't fetch full directory listings unless you actually need them. Knowing that `fact-sheets/` contains G04–G37 is sufficient for most tasks; the actual file list is only needed when looking for something specific.
