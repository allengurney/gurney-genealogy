---
name: research-intake-apply-patch
description: Apply a reviewed intake patchset by performing only the explicit file and content operations it specifies, without redoing content analysis.
argument-hint: [path to vNN.patchset.md]
disable-model-invocation: true
---

Use this skill for phase 2 of intake.

## Read first
- `.claude/CLAUDE.md`
- `AGENTS.md` §4 (Repo file resolution — lookup order, direct-open known paths, destination discipline)
- `.claude/rules/research-writing-style.md`
- `.claude/rules/citations.md`
- `.claude/rules/data-json.md`
- `.claude/rules/sources.md` (intake + validations + media discipline, merged 2026-05-25)

## Core rule
The patchset is the source of truth for this run.

Do not redo OCR, extraction, destination analysis, or prose generation except for trivial path or formatting fixes required to apply the instructions safely.

## Allowed work
- create, move, or copy normalized files
- add sidecar text files when the patchset says to
- update `data/sources.json`
- update `research/...`
- create thin `sources/validations/...` notes
- archive the raw session bundle
- create the next blank session file when instructed
- add a brief `**Done:** YYYY-MM-DD HH:MM PT` top-line stamp to newly completed patchsets
- move completed patchsets to `sources/intake/done/`

## Not allowed
- no fresh content analysis
- no rewriting of proposed research blocks beyond trivial markdown cleanup
- no broad refactoring
- no fact-sheet edits unless the patchset explicitly says so and the user approved that scope

## Validation note standard
Keep validations thin. If the patchset already records method, extraction details, and file operations, the validation note may point to the patchset instead of repeating them.

## If the patchset is ambiguous
Stop and surface the ambiguity rather than inventing content or destinations.

## Success condition
All explicit instructions in the patchset are applied, and the summary reports:
- files changed
- sourceIds added or matched
- research files updated
- validations created
- archive and rollover actions completed
- patchset moved to `sources/intake/done/`

After content, source, or research-path changes, run
`.\.venv\Scripts\python.exe tools\repo_search.py index --update` followed by
`.\.venv\Scripts\python.exe tools\repo_search.py index --check`. This refreshes
the machine-local retrieval accelerator; exact repository-search completeness
still comes from the tool's independent ripgrep ledger.
