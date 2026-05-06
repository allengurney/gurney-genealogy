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
- `processed/` = repo-ready patchsets and brief outcome summaries
- `archive/` = archived raw session bundles after application

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
- write `sources/intake/processed/vNN.patchset.md`

Phase 2 = application.
- execute the patchset
- perform file moves/copies
- update `data/sources.json`
- update `research/...`
- keep validations thin

## FamilySearch exports — Phase 0
FamilySearch Family Group Record PDF exports (under `sources/FS/`) get a content-evaluation pass before Phase 1. The output is an assessment MD attached to chat (not committed) that becomes the input to a Phase-1 patchset. See `.claude/skills/familysearch-export-review/SKILL.md`.

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
- processed patchset

## Cross-reference
See:
- `.claude/rules/research-writing-style.md`
- `.claude/rules/citations.md`
- `.claude/rules/sources-validations.md`
- `.claude/skills/research-intake-prep/SKILL.md`
- `.claude/skills/research-intake-apply-patch/SKILL.md`
