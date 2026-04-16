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

| Scope | Status | Sessions reviewed | Notes |
|---|---|---|---|
| East Dereham register paleographic analysis | not started | | High-value; parish record details, Entry A–E findings, paleographic tests |
| Daniel Gurney corpus exploration | not started | | OCR quirks, page-specific cross-references, source extract details |
| Source evaluations (Anderson, Banks, Herald & Genealogist, etc.) | not started | | Capture in `sources/validations/` |
| Candidate B hypothesis sessions | not started | | Reasoning trail, evidence weighting, probability adjustments |
| Fact sheet production sessions (Batch 1, 2, partial 3) | not started | | May contain research detail that didn't fit fact sheets |
| Negative results & eliminated candidates | not started | | Children search eliminations, failed register searches |
| Lineage restructuring (March 2026) | not started | | Junior Norfolk branch correction, new G21–G31 entries |
| Allen's corrections / pushback patterns | not started | | Mostly in AI-Rules §6; verify completeness |
| Architecture/meta sessions | skip | | Repo structure, site build — not research content |

## Phase 3 — Cleanup & validation

| Task | Status |
|---|---|
| Cross-check Phase 1 docs against transcript-migrated content | not started |
| Audit `data/sources.json` for orphans (sources with no facts citing them) | not started |
| Audit fact sheet companions for missing § Sources Consulted entries | not started |
| Verify all 8 critical corrections (AI-Rules §7) are reflected in target fact sheets | not started |
| Retire this tracker when all rows are `migrated` or `superseded` | not started |
