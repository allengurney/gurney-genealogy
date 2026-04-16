# Migration Tracker

Tracks the migration of prior research findings (project knowledge documents and chat transcripts) into the new repo structure. Goal: ensure no prior finding is re-discovered or lost.

**Status as of:** 2026-04-15

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
| `Gurney_AncestorTable_V3_WithLandHoldings.docx` | superseded | Already in `data/ancestors_v23.json` |

## Phase 2 — Chat transcripts (PRIMARY MIGRATION SOURCE)

### By topic scope

| Scope | Status | Sessions reviewed | Notes |
|---|---|---|---|
| East Dereham register paleographic analysis | not started | | High-value; parish record details, Entry A–E findings, paleographic tests |
| Daniel Gurney corpus exploration | not started | | OCR quirks, page-specific cross-references, source extract details |
| Source evaluations (Anderson, Banks, Herald & Genealogist, etc.) | **partial** | 324600c7 | Anderson, Banks, Nichols H&G evaluations migrated to `sources/validations/`. Earlier Banks discussion in cf816e20 not yet reviewed. |
| Candidate B hypothesis sessions | not started | | Reasoning trail, evidence weighting, probability adjustments |
| Fact sheet production sessions (Batch 1, 2, partial 3) | not started | | May contain research detail that didn't fit fact sheets |
| Negative results & eliminated candidates | not started | | Children search eliminations, failed register searches |
| Lineage restructuring (March 2026) | not started | | Junior Norfolk branch correction, new G21–G31 entries |
| Mary Gurney / John's wife research | not started | | Haberdashers 1632, Mary deep dive, case file v3.0 |
| Allen's corrections / pushback patterns | not started | | Mostly in AI-Rules §6; verify completeness |
| Architecture/meta sessions | skip | | Repo structure, site build — not research content |

### Per-session detail (pilot + future tracking)

| Chat ID | Date | Title | Status | Findings migrated | Notes |
|---|---|---|---|---|---|
| cf816e20 | 2026-03-22 | Protestation Returns, Coleman Street | not started | | Children Matrix V1, V6 findings, county survival table, Coleman Street network |
| 6fb94e9d | 2026-03-22 | Norwich searches, Francis death correction | not started | | FreeREG death confirmation, Gurley/Furrier lead, DG file mapping, 532a/b pages |
| 9b85696c | 2026-03-23 | Birth date revision, children re-eval | not started | | Eliminated/restored candidates, revised c.1633–1640 window |
| e98a0160 | 2026-04-02 | Main Thread (DG validation, East Dereham, CaseFile V2) | not started | | Largest session. Paleography, Margaret Rybett, BRS tax, ancestors.json restructuring |
| bcb40001 | 2026-04-03 | Fact sheet batches 1–3 | not started | | G37–G22 production. Research detail in narrative that may not be in companions. |
| **324600c7** | **2026-04-08** | **Source evaluations (Anderson, Banks, H&G)** | **migrated** | 3 validation files, sources.json v1.3.0 | **PILOT.** Anderson entry text + pull list, Banks entry + cluster + citation, Nichols v4 negative + v3 p.9 heraldic note. Case file draft text noted but deferred (no candidate-b.md yet). |
| 317a1ade | 2026-04-14 | Mary Gurney, Haberdashers, case file v3.0 | not started | | Haberdashers 1632 (father William, laborer — eliminated), Mary deep dive, Westminster Gurley, BSE conflation, 66 footnotes |
| e8c5f494 | 2026-04-16 | Artifacts discussion | skip | | Meta/architecture |

## Phase 3 — Cleanup & validation

| Task | Status |
|---|---|
| Cross-check Phase 1 docs against transcript-migrated content | not started |
| Audit `data/sources.json` for orphans (sources with no facts citing them) | not started |
| Audit fact sheet companions for missing § Sources Consulted entries | not started |
| Verify all 8 critical corrections (AI-Rules §7) are reflected in target fact sheets | not started |
| Retire this tracker when all rows are `migrated` or `superseded` | not started |

## Pilot Observations (2026-04-15)

Session 324600c7 was the pilot. Observations for scaling:

1. **Validation files are the cleanest migration target.** Source evaluations map 1:1 to files in `sources/validations/`. Each evaluation is self-contained with entry text, assessment, and open items.
2. **sources.json updates pair naturally.** When a validation file is created, the corresponding sources.json entry gets `validationPath` and any missing citation detail (publisher, city, page).
3. **Case file content is deferred.** The session produced drafted prose for `research/case-files/candidate-b.md`, but that file doesn't exist yet and would need content from multiple sessions. Creating the skeleton and populating it is a separate task — probably after the highest-value transcripts (e98a0160, cf816e20) are processed.
4. **One session ≈ 3–5 commits** at this granularity. Scaling to 7 research sessions ≈ 20–35 commits.
5. **Context window is the constraint.** The `conversation_search` tool returns snippets, not full transcripts. For sessions with dense record-by-record detail (e98a0160 especially), multiple targeted searches will be needed per session.
