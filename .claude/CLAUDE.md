# Claude working guide for `gurney-genealogy`

This file holds always-on instructions for Claude Code in this repo.
Directory-specific behavior lives in `.claude/rules/`.
Manual workflows live in `.claude/skills/`.

## Read order on substantive work
1. Read this file.
2. Read the relevant directory README.
3. Read the matching path-scoped rule(s).
4. Read the target file(s).
5. Then analyze or edit.

## Repo resolution
- Work from exact repo-relative paths and the explicit branch/ref in play.
- Prefer the repo connector or local filesystem over public GitHub URLs when a file lives in the repo.
- Do not search or hunt for a file when the exact path is already known.
- If a filename is ambiguous, resolve it once, then use the exact path thereafter.
- Distinguish clearly between:
  - repo files
  - files attached to the current chat
  - files in another project/workspace
  - external web sources

See `.claude/rules/repo-file-resolution.md`.

## Canonical locations
- `data/` = canonical structured spine
- `fact-sheets/` = published narrative only
- `research/` = working knowledge layer
- `sources/intake/` = raw intake queue and processed patchsets
- `sources/media/` = working reference artifacts
- `sources/validations/` = thin source-validation notes
- `site/` = generated/presentation layer

## Core rules

### Bind rules to nested artifacts and subtasks
- A larger task can contain smaller artifacts or workflow steps with their own rules.
- Apply the rule for the thing being authored or executed, even when it is embedded inside another deliverable.
  - Proposed `sources/validations/*.md` content inside an intake patchset must follow the validation rules, not the patchset-writing style.
  - Proposed `research/...` content inside an intake patchset must follow the relevant research rules, not validation or process-note style.
  - Git, branch, commit, push, or PR work remains governed by `.claude/rules/git-onedrive-codex.md` even when publication is only the final subtask of a larger research or site task.
- Do not let the outer task type override the inner artifact or workflow rule.

### Edit narrowly
- Prefer targeted edits over wholesale rewrites.
- Preserve established prose unless fact, citation, structure, or clarity requires change.
- For markdown and JSON files under roughly 50 KB, direct in-place editing is preferred over over-engineered scripting.

### Put findings in the right layer
- Person findings -> `research/people/`
- Place findings -> `research/places/`
- Cross-cutting analysis -> `research/topics/`
- Sustained argument / competing hypotheses -> `research/case-files/`
- Logs and validations stay thin.

### Research prose is knowledge-first
- Visible research prose should preserve findings, extracts, and real analysis.
- Keep intake, processing, OCR, normalization, archival, and workflow mechanics out of visible research prose unless they materially affect interpretation.
- Prefer specific caveats only when uncertainty changes meaning, identity, date, place, or interpretation.
- Put routine provenance mechanics in footnotes, validations, or processed patchsets.

See `.claude/rules/research-writing-style.md`.

### Citation baseline
- Put the footnote as close as practical to the supported fact.
- Prefer full-form, human-readable notes with URL when available.
- Align with `data/sources.json` when a source has a `sourceId`.
- No research content should be inserted from intake unless it ties to an existing or newly created `data/sources.json` entry.

See `.claude/rules/citations.md`.

### Evidence discipline
- Do not overclaim.
- Preserve conflicts until resolved.
- Negative results are findings.
- When a source-linked image, excerpt, or trustworthy associated metadata is supplied, write the finding directly.
- Add a visible qualification only when the uncertainty materially changes the claim.

### Continual improvement
- When the user offers a critical correction or durable guidance, update the matching rule file in the same turn — no separate permission is required when the feedback itself is the rule.
- Disclose the rule update plainly: which file, what changed, which feedback drove it.
- While working a directed task, AI may correct narrow adjacent issues found in the same files (typos, broken anchors, acronym expansions, internal-mechanics vocabulary, citation placement) without separate permission, with disclosure.
- See `.claude/rules/continual-improvement.md`.

## Related
- `README.md`
- `.claude/rules/repo-file-resolution.md`
- `.claude/rules/research-writing-style.md`
- `.claude/rules/continual-improvement.md`
- `.claude/skills/familysearch-export-review/SKILL.md`
- `.claude/skills/research-intake-prep/SKILL.md`
- `.claude/skills/research-intake-apply-patch/SKILL.md`
- `.claude/skills/citation-rigour/SKILL.md`
