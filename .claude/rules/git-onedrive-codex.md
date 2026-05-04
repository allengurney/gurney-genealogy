---
paths:
  - ".git"
  - ".claude/**/*"
  - "README.md"
  - "site/**/*"
  - "data/**/*"
  - "research/**/*"
  - "sources/**/*"
  - "fact-sheets/**/*"
---

# Git, OneDrive, and Codex workflow

This repository is intentionally split between a OneDrive working tree and a Git directory outside OneDrive.

## Local layout
- Working tree: `C:\Users\allen\OneDrive\Documents\GitHub\gurney-genealogy`
- Git directory: `C:\Users\allen\GitDirs\gurney-genealogy.git`
- The repo-root `.git` path is a small pointer file, not a normal `.git` directory.
- The pointer file should contain:

```text
gitdir: C:/Users/allen/GitDirs/gurney-genealogy.git
```

## Why this exists
- OneDrive is mandatory for the user's recovery/audit workflow.
- Git internals should stay outside OneDrive to avoid lock, sync, and permission churn.
- Do not move Git internals back into the OneDrive working tree unless the user explicitly requests a new Git layout.
- Do not reclone into a temporary workspace as a substitute for fixing the durable checkout.

## Claude and Codex AI operating model
- Work from the durable checkout unless the user explicitly directs otherwise.
- Do not modify `main` directly for substantive work; create a branch first.
- AI can fetch, inspect status, create local branches, and make local commits in this layout.
- Push through local Git is expected to happen through GitHub Desktop or the user's PowerShell unless credentials are deliberately reconfigured for Codex.
- If the user asks Codex to complete "push/PR/etc.", avoid local `git push` / `gh auth` first and prefer the GitHub connector/API publish path when available.
- Connector-backed publish path: create or update the remote branch from the local committed tree using GitHub API objects/refs, then open the PR through the GitHub connector. Verify the remote branch or PR head SHA before reporting success.
- Do not repeatedly test local remote push/auth from Codex. One failed local remote authentication or GitHub CLI credential check is enough to stop local Git/CLI remote operations and switch to the connector/API path.
- If a Windows dialog appears or is reported for `git-remote-https.exe`, `git-credential-manager.exe`, GitHub CLI, or a similar Git authentication helper, stop all local remote Git/CLI operations immediately. Do not retry with tracing, alternate shells, or repeated `git push`/`gh auth` probes.
- If the GitHub connector/API path is unavailable or fails, then hand off the already-created local branch and commit to GitHub Desktop or user PowerShell with exact branch and commit details.

## Health checks before blaming the repo
If Git behaves strangely, check these in order:
1. `Get-Content .git` should point to `C:/Users/allen/GitDirs/gurney-genealogy.git`.
2. `git status --short --branch` should run from the durable checkout.
3. `git fetch origin --prune` should run; if it fails with a permissions error, check Codex writable roots and permissions on `C:\Users\allen\GitDirs`.
4. `git config --global --get-all safe.directory` should include the durable checkout when the sandbox user differs from the Windows user.
5. `git config --global --get-regexp "credential.*helper"` should not route GitHub pushes through `gh` if Codex is expected to push.

## Credential note
GitHub Desktop / user PowerShell is the preferred push path. A Codex-readable token or credential file should only be used if the user explicitly chooses that risk.

## Remote completion pattern
When work is complete and committed locally:
1. Report the branch name, commit SHA, and validation result.
2. If the user asked for push/PR completion, use the GitHub connector/API path to publish the committed tree and open the PR when available.
3. Verify the remote branch or PR head matches the intended local commit/tree before saying the PR is ready.
4. If connector/API publishing is unavailable or fails, tell the user to push the current branch through GitHub Desktop or their own PowerShell session, then ask them to say when the branch is pushed so Codex can verify the remote SHA and PR.
