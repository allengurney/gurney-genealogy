@AGENTS.md

# Claude working guide for `gurney-genealogy`

Always-on instructions for Claude Code in this repo. Directory-specific behavior lives in `.claude/rules/` (path-scoped, auto-loaded by the harness when editing matching files). Manual workflows live in `.claude/skills/`.

## Read order on substantive work
1. Read this file.
2. Read the relevant directory `README.md`. The READMEs carry destination guidance — where a finding belongs, including multi-destination cases.
3. The matching path-scoped rule(s) auto-load when you open a target file. Trust them; re-read only on a genuine question.
4. Read the target file(s).
5. Then analyze or edit.

## Canonical locations
- `data/` = canonical structured spine (`ancestors.json`, `places.json`, `places_detail.json`, `sources.json`)
- `fact-sheets/` = published ancestor narratives
- `research/` = working knowledge layer — see `research/README.md` for destination guidance
- `sources/` = source artefacts, intake queue, validations — see `sources/README.md` for destination guidance
- `site/` = generated/presentation layer (do not hand-edit; the build mirrors from `fact-sheets/` and `data/`)

## Core rules

### Bind rules to nested artifacts and subtasks
A larger task can contain smaller artefacts with their own rules. Apply the rule for the thing being authored, even when it is embedded inside another deliverable. Proposed `sources/validations/*.md` content inside an intake patchset follows the validation rules, not the patchset-writing style. Proposed `research/...` content inside an intake patchset follows the research rules. Git, branch, commit, push, or PR work remains governed by `git-onedrive-codex.md` even when publication is only the final subtask of a larger task. Do not let the outer task type override the inner artefact or workflow rule.

### Edit narrowly
Prefer targeted edits over wholesale rewrites. Preserve established prose unless fact, citation, structure, or clarity requires change. For markdown and JSON under ~50 KB, direct in-place editing beats over-engineered scripting.

### Findings go on the subject file
Person findings → `research/people/`. Place findings → `research/places/`. Cross-cutting analysis → `research/topics/`. Sustained per-ancestor argument → the ancestor's people-companion (not a case file). Case files are user-initiated publication artefacts only. Logs and validations stay thin. Detailed multi-destination guidance is in `research/README.md` and `sources/README.md`.

### Continual improvement
When the user offers a critical correction or durable guidance, update the matching rule file in the same turn and disclose the update plainly. AI may correct narrow adjacent issues found in the same files (typos, broken anchors, acronym expansions, internal-mechanics vocabulary, citation placement) without separate permission, with disclosure. See `.claude/rules/continual-improvement.md` for the consolidation-pass discipline, avoid-reactive-absolutes guidance, and bias-toward-restraint check.
