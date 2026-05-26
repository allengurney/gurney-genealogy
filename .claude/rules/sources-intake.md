---
paths:
  - "sources/intake/**/*.md"
  - "sources/intake/**/*"
---

# Sources intake rules

Human-facing overview:
- `sources/README.md`

## Purpose
`sources/intake/` is the raw queue for newly captured research awaiting triage and promotion.

## Directory lifecycle
- `new/` = active intake sessions and raw files
- `processed/` = active repo-ready patchsets awaiting review or Phase 2 application, plus the next-version stub
- `done/` = completed patchsets and closed intake materials
- `archive/` = archived raw session bundles after application

## Patchset version stub
- Keep one next-version stub in `sources/intake/processed/` named `stub-vNN.md`.
- To create a new patchset, rename the stub to the real patchset filename, for example `v62-topic.patchset.md`.
- Immediately create the next stub, incremented by one, for example `stub-v63.md`.
- The stub is the normal source of truth for the next patchset number. Do not recursively scan `sources/intake/**` for routine version assignment.
- If the stub is missing, duplicated, or obviously stale, repair it with a one-time shallow scan of patchset filenames in `sources/intake/processed/`, `sources/intake/processed/Ready/`, `sources/intake/processed/on-hold/`, and `sources/intake/done/`; take the highest `vNN` found and create `stub-v(NN+1).md`.

## Session rule
- Use one markdown session file per batch: `vNN.md`
- Entries are separated by `---`
- Keep referenced files in the same `new/` folder until applied

## Two-phase intake model
Phase 1 = preparation.
- inspect files and URLs
- OCR/extract/retrieve content as needed
- judge relevance and destination
- reconcile or propose source tracking
- rename the current `sources/intake/processed/stub-vNN.md` to the new `sources/intake/processed/vNN-topic.patchset.md`
- create the next stub immediately

Phase 2 = application.
- execute the patchset
- perform file moves/copies
- update `data/sources.json`
- update `research/...`
- keep validations thin
- after the explicit patchset instructions are complete, move the patchset file to `sources/intake/done/`
- for newly completed patchsets going forward, add a brief top-line completion stamp before moving, using `**Done:** YYYY-MM-DD HH:MM PT`; do not include commit or validation status in that stamp

## FamilySearch exports — Phase 0
FamilySearch Family Group Record PDF exports (under `sources/FS/`) get a content-evaluation pass before Phase 1. The output is an assessment MD attached to chat (not committed) that becomes the input to a Phase-1 patchset. See `.claude/skills/familysearch-export-review/SKILL.md`.

## Patchset standard (cross-reference)
The operational rules for what a patchset must contain are in `.claude/skills/research-intake-prep/SKILL.md` — the Patchset Standard, Rich-Content-Must-Land-In-The-Repo, No-Hold-Review, Cadence, and Research-Block-Style sections. The summary for this rule file:

- A patchset is an operational script that Phase 2 follows mechanically — no detective work, no `hold-review` items, no "subject to user approval" language.
- Quoted source material in the patchset preamble must also appear in the action steps, written to a durable destination (research companion + `sources/corpus_supplement/` for rich primary extracts). Patchset markdown is process scaffolding; once Phase 2 runs, it is archived.
- Patchsets bundle the findings of a research arc, not a single turn. Multiple turns of research → one patchset.
- Preamble supports the actions; action steps dominate the document.

Before treating any extract as new, check `sources/corpus_supplement/` and `sources/media/` to confirm it is not already captured.

## Promotion writing standard
- When promoting findings into `research/`, write ordinary research prose.
- Lead with the knowledge.
- Do not mention intake, processing, archival, normalization, or OCR mechanics in visible research text.
- Keep session/process traceability in HTML comments, footnotes, validations, and patchsets.

## Traceability
Every retained item should keep a path back to:
- session file
- original file
- source URL when available
- `data/sources.json`
- validation note if created
- completed patchset in `sources/intake/done/`, or active patchset in `sources/intake/processed/` while still awaiting application

## Cross-reference
See:
- `.claude/rules/research-writing-style.md`
- `.claude/rules/citations.md`
- `.claude/rules/sources-validations.md`
- `.claude/skills/research-intake-prep/SKILL.md`
- `.claude/skills/research-intake-apply-patch/SKILL.md`
