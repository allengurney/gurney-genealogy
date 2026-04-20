---
paths:
  - "sources/intake/**/*.md"
  - "sources/intake/**/*"
---

# Sources intake rules

Human-facing overview:
- `sources/README.md`

## Purpose
`sources/intake/` is the raw intake queue for newly captured research material awaiting triage and promotion.

## Directory lifecycle
- `new/` holds active intake sessions and raw files
- `processed/` holds processed session reports
- `archive/` holds archived raw session bundles after processing

## Intake session rule
- Use one markdown file per session: `vNN.md`
- Entries are separated by `---`
- Keep referenced files in the same `new/` folder until processed

## Processing rule
- Intake items are not publication-ready by default
- Promotion into research files should be traceable and source-tracked
- Preserve the raw originals in the archive bundle

## Citation and traceability
- Every promoted item must keep a path back to:
  - original intake session
  - original file
  - normalized promoted file
  - URL when available
  - validation note
  - `data/sources.json` entry

## Cross-reference
See:
- `.claude/skills/research-intake-session-processor/SKILL.md`
- `.claude/rules/citations.md`
- `.claude/rules/sources-validations.md`
