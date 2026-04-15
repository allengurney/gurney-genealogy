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

## Phase 1 — Project knowledge documents

| Source | Status | Migration target | Notes |
|---|---|---|---|
| `Gurney_CandidateB_CaseFile_V2.md` | not started | `research/case-files/candidate-b.md` | The central research doc on John Gurney-1 origin. Highest priority. |
| `Gurney_Research_Findings_V7.md` | not started | distributed: fact-sheet companions, topic files | Findings consolidated; need to identify what's not yet captured elsewhere |
| `Gurney_ProtestationReturns_Analysis.md` | not started | `research/topics/protestation-returns.md` | Cross-cutting analysis; topic file is right home |
| `Gurney_Children_Matrix_V2.docx` | not started | `research/case-files/john-children-matrix.md` (or supporting attachment to candidate-b) | Convert .docx to .md in migration |
| `Gurney_Johns_Table_V2.docx` | not started | `research/case-files/john-candidates-comparison.md` | Convert .docx to .md |
| `Gurney_John_Validation_V3.docx` | not started | `research/case-files/john-validation.md` | Convert .docx to .md |
| `Gurney_Sources_Citations_V3.md` | not started | augment `data/sources.json` | Merge any citations not already in sources.json |
| `Gurney_Research_KnowledgeBase_1.md` | not started | distributed | Cross-cutting; mine after others done so we know what's already captured |
| `Gurney_AncestorTable_V3_WithLandHoldings.docx` | superseded | `data/ancestors_v23.json` | Already in JSON form |

## Phase 2 — Chat transcripts

| Scope | Status | Notes |
|---|---|---|
| Daniel Gurney corpus exploration | not started | Look for paleographic findings, OCR quirks, page-specific cross-references |
| Source evaluations (Anderson, Banks, etc.) | not started | Capture in `sources/validations/{sourceId}.md` |
| East Dereham register paleographic analysis | not started | High-value; goes in `sources/validations/nro-pd-86-41.md` |
| Allen's corrections / pushback patterns | not started | Mostly captured in AI-Rules §6. Verify completeness. |

## Phase 3 — Cleanup & validation

| Task | Status |
|---|---|
| Audit `data/sources.json` for orphans (sources with no facts citing them) | not started |
| Audit fact sheet companions for missing § Sources Consulted entries | not started |
| Verify all 8 critical corrections (AI-Rules §7) are reflected in target fact sheets | not started |
| Retire this tracker when all rows are `migrated` or `superseded` | not started |
