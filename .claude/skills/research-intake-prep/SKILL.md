---
name: research-intake-prep
description: Analyze one intake session from sources/intake/new/, inspect files and URLs, extract or OCR content as needed, determine relevance and research destination, and write a repo-ready patchset without directly editing research, data, or media files.
argument-hint: [path to intake session markdown file]
disable-model-invocation: true
---

Use this skill for phase 1 of intake.

## Read first
- `.claude/CLAUDE.md`
- `.claude/rules/repo-file-resolution.md`
- `.claude/rules/research-writing-style.md`
- `.claude/rules/citations.md`
- `.claude/rules/data-json.md`
- `.claude/rules/sources-intake.md`
- `.claude/rules/sources-validations.md`

## What this skill does
For each intake entry:
1. parse the freeform entry
2. identify the files, pages, and URLs
3. inspect and extract or OCR content as needed
4. decide one outcome: promote, hold-review, duplicate, or reject
5. determine the best research destination
6. reconcile an existing sourceId or propose a new compliant one
7. write an explicit patchset at `sources/intake/processed/vNN.patchset.md`

## What this skill does not do
- do not update `research/...`
- do not update `data/sources.json`
- do not move or copy files into `sources/media/`
- do not archive the session

Those belong to phase 2.

## Patchset standard
The patchset must be operational, not narrative.

For each retained item include:
- outcome
- exact destination file path or paths
- exact sourceId match or exact new source entry block
- exact file operations
- exact research markdown block or blocks to add or revise
- exact validation note body only when needed
- unresolved issues only when they block application

Use fenced code blocks for verbatim content to add.

## Research block style
Write proposed research blocks as ordinary research notes:
- lead with the finding
- keep wording compact
- no visible intake, process, OCR, or provenance narration
- no generic caveating
- add analysis only when it adds real knowledge
- keep citations close to the fact

## Hold-review rule
Use hold-review when identification or extraction is not good enough for compliant source tracking or a clean research insertion.

## Success condition
The patchset is good enough that a second tool can apply it without redoing content analysis.
