---
paths:
  - "sources/validations/*.md"
---

# Source validation rules

Human-facing overview:
- `sources/README.md`
- `sources/validations/README.md`

## Purpose
Validation files record what source was examined, what portion was examined, and where findings landed.

## These files are deliberately thin
They should answer:
- what source was examined
- what portion was examined
- what remains unexamined or uncertain
- where substantive findings were recorded
- where the detailed execution trail lives, if a patchset exists

They should not become the main home for person/place/topic findings.

## Keep process centralized
- If `sources/intake/processed/vNN.patchset.md` already records extraction method, triage, and exact file operations, validations may point to it rather than repeat it.
- Do not turn validations into mini research files or patch transcripts.

## Good content here
- page/image/folio scope
- concise method note when it matters
- OCR or image limitations when material
- whether index was checked against image, if relevant
- links/pointers to media files
- pointers to target research files
- pointer to the processed patchset when applicable

## Citation posture
- The validation file itself should still identify the source precisely.
- If the validation file states a substantive conclusion, cite it.
- Prefer to move substantive conclusions to the relevant subject file and leave only a pointer here.

## Cross-reference
See also:
- `.claude/rules/citations.md`
- `.claude/rules/sources-media.md`
- `.claude/rules/research-writing-style.md`
