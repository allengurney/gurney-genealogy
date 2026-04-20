---
paths:
  - "site/**/*"
---

# Site generation rules

Human-facing overview:
- `site/README.md`

## Purpose
`site/` is a generated/presentation layer for the public site.

## Canonical-source rule
- Do not treat `site/` as the source of truth for facts.
- Canonical data lives in `data/`.
- Canonical published prose lives in `fact-sheets/`.
- `site/` should render from upstream sources rather than fork them.

## Editing posture
- Avoid hardcoding facts in templates when the same facts should come from upstream data or markdown.
- Prefer structural/template edits over duplicating content.
- Preserve clean separation between content and presentation.

## Current state
- This directory is still placeholder-oriented until migration is complete.
- Do not build assumptions into site files that conflict with upstream repo structure.

## Cross-reference
See also:
- `site/README.md`
- `.claude/rules/fact-sheets.md`
- `.claude/rules/data-json.md`
