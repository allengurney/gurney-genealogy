# Git workflow — OneDrive checkout health checks

The repo layout, OneDrive split rationale, and "why git internals stay outside OneDrive" are in `AGENTS.md` §10 (Local environment).

The branch-and-PR publish workflow for fragile Windows-ARM credential cases is in `.claude/skills/connector-publish/SKILL.md`. This rule covers only the always-applicable health checks.

## Health checks before blaming the repo

If git behaves strangely, check these in order:

1. `Get-Content .git` should point to `C:/Users/allen/GitDirs/gurney-genealogy.git`.
2. `git status --short --branch` should run from the durable checkout.
3. `git fetch origin --prune` should run; if it fails with a permissions error, check writable roots and permissions on `C:\Users\allen\GitDirs`.
4. `git config --global --get-all safe.directory` should include the durable checkout when the sandbox user differs from the Windows user.
5. `git config --global --get-regexp "credential.*helper"` should not route GitHub pushes through `gh` if Codex is expected to push.

## AI operating model — local

- Work from the durable checkout (`C:\Users\allen\OneDrive\Documents\GitHub\gurney-genealogy`) unless the user explicitly directs otherwise.
- Do not modify `main` directly for substantive work; create a branch first.
- Local commits are reliable. Local remote push/auth is the fragile part on this layout; switch to the connector-publish skill or hand off to GitHub Desktop / user PowerShell rather than retrying.

## Mandatory related rules
None — this rule is always-loaded and its narrow scope (git operations) is not shared by any other rule.

## See also
- `AGENTS.md` §10 (Local environment — OneDrive + git layout) — the durable repo layout
- `.claude/skills/connector-publish/SKILL.md` — branch-and-PR publish recipe + Windows ARM credential failure modes
