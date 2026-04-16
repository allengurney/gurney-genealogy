# Migration Tracker

Tracks the migration of prior research findings (project knowledge documents and chat transcripts) into the new repo structure. Goal: ensure no prior finding is re-discovered or lost.

**Status as of:** 2026-04-16 (end of day)

## How to use this tracker

- One row per source document or chat scope
- **Status**: `not started` | `in progress` | `migrated` | `partial` | `superseded`
- **Migration target**: where the content was placed in the repo
- **Notes**: gaps, follow-ups, decisions made
- Update this file in the same commit as the migration work it tracks

When everything is `migrated`, this file can be archived or deleted.

---

## Phase 1 — Project knowledge documents — REDIRECTED

> **Decision (2026-04-15):** Phase 1 documents are NOT the migration starting point. They are distillations with weak citations, originated in prior chat sessions. We start from Phase 2 (chat transcripts) instead, which preserves primary-source-level context, exact record details, and reasoning trails. Phase 1 docs remain available as cross-check references — if a finding surfaces in transcripts, we can verify whether the Phase 1 doc captured it and whether it added anything.

| Source | Status | Notes |
|---|---|---|
| `Gurney_CandidateB_CaseFile_V2.md` | cross-check ref | Compare against transcript-sourced candidate-b.md content |
| `Gurney_Research_Findings_V7.md` | cross-check ref | Verify coverage after transcript migration |
| `Gurney_ProtestationReturns_Analysis.md` | cross-check ref | Verify coverage after transcript migration |
| `Gurney_Children_Matrix_V2.docx` | cross-check ref | Verify coverage after transcript migration |
| `Gurney_Johns_Table_V2.docx` | cross-check ref | Verify coverage after transcript migration |
| `Gurney_John_Validation_V3.docx` | cross-check ref | Verify coverage after transcript migration |
| `Gurney_Sources_Citations_V3.md` | cross-check ref | Mine for any sourceIds not in sources.json after transcripts done |
| `Gurney_Research_KnowledgeBase_1.md` | cross-check ref | Final cross-check sweep |
| `Gurney_AncestorTable_V3_WithLandHoldings.docx` | superseded | Already in `data/ancestors v23.json` (landholdings v3 content now also in `research/places/` as markdown, 2026-04-16) |

## Phase 2 — Chat transcripts (PRIMARY MIGRATION SOURCE)

### By topic scope

| Scope | Status | Sessions reviewed | Notes |
|---|---|---|---|
| East Dereham register paleographic analysis | not started | | High-value; parish record details, Entry A–E findings, paleographic tests |
| Daniel Gurney corpus exploration | not started | | OCR quirks, page-specific cross-references, source extract details |
| Source evaluations (Anderson, Banks, Herald & Genealogist, etc.) | **partial** | 324600c7 | Anderson, Banks, Nichols H&G evaluations migrated. Earlier Banks discussion in cf816e20 not yet reviewed. |
| Candidate B hypothesis sessions | not started | | Reasoning trail, evidence weighting, probability adjustments |
| Fact sheet production sessions (Batch 1, 2, partial 3) | **partial — G20–G37 complete for transcript-only findings; landholdings complete; row-by-row narrative vs. transcript detail review still TODO** | bcb40001 | See per-session entry below for current state. |
| Negative results & eliminated candidates | not started | | Children search eliminations, failed register searches |
| Lineage restructuring (March 2026) | not started | | Junior Norfolk branch correction, new G21–G31 entries |
| Mary Gurney / John's wife research | not started | | Haberdashers 1632, Mary deep dive, case file v3.0 |
| Allen's corrections / pushback patterns | not started | | Mostly in AI-Rules §6; verify completeness |
| Architecture/meta sessions | skip | | Repo structure, site build — not research content |

### Per-session detail

| Chat ID | Date | Title | Status | Findings migrated | Notes |
|---|---|---|---|---|---|
| cf816e20 | 2026-03-22 | Protestation Returns, Coleman Street | not started | | Children Matrix V1, V6 findings, county survival table, Coleman Street network |
| 6fb94e9d | 2026-03-22 | Norwich searches, Francis death correction | not started | | FreeREG death confirmation, Gurley/Furrier lead, DG file mapping, 532a/b pages |
| 9b85696c | 2026-03-23 | Birth date revision, children re-eval | not started | | Eliminated/restored candidates, revised c.1633–1640 window |
| e98a0160 | 2026-04-02 | Main Thread (DG validation, East Dereham, CaseFile V2, **JSON landholdings**) | **partial** | Landholdings locations data (lat/lng) migrated 2026-04-16 into 17 `research/places/` files; data-pollution bugs logged in `research/topics/ancestors-json-audit.md` | Largest session. Paleography, Margaret Rybett, BRS tax, ancestors.json restructuring still pending in text form. |
| **bcb40001** | **2026-04-03** | **Fact sheet batches 1–3 (G37–G22)** | **partial** | G29 (Hameline ID, 1204 hook, Pipe Roll), G23 (will details, Gaunt phrasing flag, citation fix), G22 (name uncertainty, Cook Clarenceux, citation fix); G24/G25/G26 citation fixes; topic file `dg-citation-audit.md`; **17 `research/places/` files + Landholdings tables in all 17 G20–G37 companions** | Row-by-row transcript-vs-fact-sheet compression review (where fact sheet narrative compresses transcript findings) still TODO. |
| 324600c7 | 2026-04-08 | Source evaluations (Anderson, Banks, H&G) | migrated v2 | Findings on g13 research file; thin validation files; sources.json v1.3.0 | Pilot v1 corrected: findings now routed to subject (g13 research file) per AI-Rules §3 findings-vs-provenance rule. |
| 317a1ade | 2026-04-14 | Mary Gurney, Haberdashers, case file v3.0 | not started | | Haberdashers 1632 (father William, laborer — eliminated), Mary deep dive, Westminster Gurley, BSE conflation, 66 footnotes |
| e8c5f494 | 2026-04-16 | Artifacts discussion | skip | | Meta/architecture |

## Phase 3 — Cleanup & validation

| Task | Status |
|---|---|
| Cross-check Phase 1 docs against transcript-migrated content | not started |
| Audit `data/sources.json` for orphans (sources with no facts citing them) | not started |
| Audit fact sheet companions for missing § Sources Consulted entries | not started |
| **Sweep all research companions for "Supplement" miscitation pattern** | **partial** (G20–G37 complete; G15–G19 + G04–G05 still TODO) |
| **G20–G37 Landholdings sections in research companions** | **complete** (2026-04-16) |
| **`research/places/` files for G20–G37 holdings** | **complete** (17 files, 2026-04-16) |
| **`data/ancestors v23.json` data-pollution cleanup** | **flagged** in `research/topics/ancestors-json-audit.md`; cleanup is a bulk-script job, not urgent |
| Verify all 8 critical corrections (AI-Rules §7) are reflected in target fact sheets | not started |
| Retire this tracker when all rows are `migrated` or `superseded` | not started |

## Migration observations

### Pilot v1 (2026-04-15, chat 324600c7)
Source-evaluation session. Initial migration miscategorized findings as source-provenance content. Corrected after Allen's pushback: findings about subjects now go to subject files; source files are thin audit trail. AI-Rules §3 updated with findings-vs-provenance distinction.

### Pilot v2 (2026-04-16, chat bcb40001)
Fact-sheet-production session. Different pattern from v1: most session content already made it into the repo as the fact sheets themselves (G37–G22 narrative files). What was missing was the *meta-content*: flags carried forward, source-attribution caveats, narrative-only contextual hooks not in the research companions. Three companions enriched initially (G29, G23, G22); citation-audit pattern surfaced, then fixed across G24/G25/G26.

### Pilot v2 expansion (2026-04-16 afternoon, Allen pushback)
Allen correctly challenged the initial "nothing more to find" assessment: fact sheets are by definition compressions of transcript content, and the `ancestors v23.json` landholding data (lat/lng coordinates for every G20–G37 holding, populated in chat e98a0160) had never reached the research companions or a place-file directory. Response:

- Created 17 place files in `research/places/` covering every G20–G37 landholding: Gournay-en-Bray, Montigny-sur-Andelle, La Ferté-en-Bray, Le Bec-Hellouin, Lessingham, Harpley, Hardingham, West Barsham, Runhall, King's Lynn, Liston, Fordham, Ardleigh, Suffolk, Lewes, Caister-on-Sea, Cantley.
- Added a Landholdings section to all 17 G20–G37 research companions, each linking to the corresponding place files with period-held notes.
- Logged JSON data-pollution bugs (concatenated `eventDate`/`sourceQuote` fields; incorrect West-Barsham-on-G~37 entry) in `research/topics/ancestors-json-audit.md`.
- Fixed AI-Rules filename reference `ancestors_v23.json` → `ancestors v23.json` (space).

What's still TODO from bcb40001: the row-by-row narrative-vs-transcript compression review. Each fact sheet narrative is shorter than the transcript detail it drew on; systematic line-by-line review would surface further compressed detail for the companions. Not yet done.

### Process notes
- **Per-session yield varies enormously.** v1 produced ~3 commits of net-new content. v2 produced 4 commits initially, then 5 more after expansion-to-landholdings. Sessions like e98a0160 will be larger still.
- **Read the existing research companion BEFORE searching the transcript.** This was the v2 efficiency win. Knowing what's already there narrows the search to what's missing.
- **Citation errors are the most valuable thing transcripts catch.** When a fact sheet says DG-II and the companion says Supplement, the companion is wrong — the transcript shows the original session correctly cited DG-II. These errors are invisible without going back to the source-of-truth conversation.
- **The JSON is its own stream.** Chat-session outputs can land in JSON (landholding coordinates, structured locations), in fact sheets (narrative prose), or in research companions (working notes). Each stream needs its own migration check; the fact sheet being complete does not mean the JSON landholding data reached markdown.
- **Don't mark a transcript "partial" when you've only examined what a fact sheet compressed.** The transcript also produced JSON, structured data, and auxiliary material that lives outside the fact sheet. Until all of those streams are checked, "partial" understates the work remaining.
