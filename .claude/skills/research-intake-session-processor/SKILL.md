---
name: research-intake-session-processor
description: Legacy intake coordinator. Default to two-phase intake: create a repo-ready patchset from sources/intake/new/, then apply it in a separate operational pass.
argument-hint: [path to intake session markdown file or patchset]
disable-model-invocation: true
---

Use this skill as the intake coordinator.

## Default policy
Default to the two-phase model:
1. `.claude/skills/research-intake-prep/SKILL.md`
2. `.claude/skills/research-intake-apply-patch/SKILL.md`

Do not use one-pass intake unless the user explicitly asks for it.

## If given a session file
Run the prep phase only:
- inspect files and URLs
- extract/OCR/retrieve as needed
- decide outcome and destination
- produce `sources/intake/processed/vNN.patchset.md`
- stop

## If given a reviewed patchset
Run the apply phase only:
- execute the explicit instructions in the patchset
- do not do new content analysis except trivial path correction
- stop and report what changed

## Non-negotiables
- `data/sources.json` remains mandatory for retained research items
- research prose must be knowledge-first
- validations stay thin
- routine process detail belongs in the patchset, not the research prose
