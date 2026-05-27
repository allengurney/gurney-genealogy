---
name: connector-publish
description: Publish a local branch and open a PR via the GitHub Connector / API when shell-launched git push/auth is fragile on this Windows ARM + OneDrive layout. Codex-driven flow; preferred over local git push when credential handling fails.
argument-hint: [branch name to publish]
disable-model-invocation: true
---

Use this skill when an AI is asked to push a local branch and open a PR, and the local git push / auth path is fragile or has already failed. Most common trigger: Codex publishing a worked branch on the Windows ARM + OneDrive layout where `git-remote-https.exe` / Git Credential Manager / GitHub CLI fail with credential or memory-write errors.

## When to use this skill

- The user asks "push and open a PR" and the working tree is the OneDrive checkout at `C:\Users\allen\OneDrive\Documents\GitHub\gurney-genealogy`.
- The GitHub Connector or API tools are available to the AI session (Codex with connector access; Claude Code with `gh` MCP or similar).
- A prior `git push` attempt in this session returned `SEC_E_NO_CREDENTIALS`, `Missing DESKTOP_PORT`, "remote-https" missing, GitHub CLI `config.yml: Access is denied`, or a Windows credential helper dialog.

If shell-launched git push is working and credentials are present, prefer the normal push path; this skill is the fallback.

## When NOT to use this skill

- The user has not asked for push/PR completion. Local commit is enough; stop after the commit and hand off.
- The connector/API tools are not available in this session. Hand the already-created local branch and commit to GitHub Desktop or user PowerShell with exact branch and commit details.

## Workflow

1. **Create the local branch and commit normally.** Local commits are allowed and reliable; only the remote push/auth is fragile.

2. **Record before publishing:**
   - branch name
   - local `HEAD` SHA
   - local `HEAD^{tree}` SHA
   - parent/base SHA, usually `HEAD^` when the branch started from current `main`
   - changed file list from `git diff-tree --no-commit-id --name-only -r HEAD`

3. **Do not call** `git push`, `gh auth`, or `gh pr create`. Skip directly to the connector path.

4. **For every changed UTF-8 text file**, read the local file content and create a GitHub blob with the connector/API. For binary files, use base64 blob creation if available; otherwise stop and hand off to GitHub Desktop / user PowerShell.

5. **Create a GitHub tree** with `base_tree_sha` set to the parent/base tree and one tree entry per changed file: `{ path, mode: "100644", type: "blob", sha }`. Do not pass the local `HEAD^{tree}` SHA to GitHub; GitHub does not know local-only Git objects until their blobs/tree are uploaded.

6. **Create a GitHub commit** from that tree with parent set to the base/parent commit. This connector-created commit may have a different SHA from the local commit because metadata differs, but its tree should match the local committed tree.

7. **Create or update the remote branch ref** to the connector-created commit.

8. **Open the PR** through the GitHub connector.

9. **Verify before reporting success:**
   - PR head branch is the intended branch
   - PR head SHA is the connector-created commit SHA
   - PR head tree SHA matches local `HEAD^{tree}` or the GitHub compare/file list matches the local committed file list
   - validation commands already passed locally

## When the connector path fails

If the connector/API tools expose blob/tree/commit/ref creation but cannot practically accept the changed local file contents (size, encoding, count), hand off the already-created local branch to the **GitHub Desktop app**. Desktop's UI has its own credential-helper session and has successfully pushed this repo's branches; shell-launched git does not inherit that session and may fail with `Missing DESKTOP_PORT`, missing `remote-https`, or `SEC_E_NO_CREDENTIALS`.

**Do not use** system git at `C:\Program Files\Git\cmd\git.exe`, GitHub CLI, or shell-launched GitHub Desktop git for remote push/auth in this failure mode.

If all connector/API and GitHub Desktop app handoff paths are unavailable, stop and report the exact blocker plus branch, local commit SHA, and validation result. Do not fall back to repeated local system-git push/auth attempts.

## Credential note

GitHub Desktop / user PowerShell is the preferred push path. A Codex-readable token or credential file should only be used if the user explicitly chooses that risk.

## One-failure rule

Do not repeatedly test local remote push/auth from Codex. One failed local remote authentication or GitHub CLI credential check is enough to stop local git/CLI remote operations and switch to the connector/API path or hand off. If a Windows dialog appears or is reported for `git-remote-https.exe`, `git-credential-manager.exe`, GitHub CLI, or a similar git authentication helper, stop all local remote git/CLI operations immediately. Do not retry with tracing, alternate shells, or repeated `git push` / `gh auth` probes.

## Remote completion pattern

When work is complete and committed locally:
1. Report the branch name, commit SHA, and validation result.
2. If the user asked for push/PR completion, use the connector/API path to publish the committed tree and open the PR when available.
3. Verify the remote branch or PR head matches the intended local commit tree before saying the PR is ready. If the connector-created remote commit has a different SHA than the local commit, report both SHAs and verify the tree/diff equivalence.
4. If connector/API publishing is unavailable or fails, tell the user to push the current branch through GitHub Desktop or their own PowerShell session, then ask them to say when the branch is pushed so the AI can verify the remote SHA and PR.

## Mandatory related rules
- `.claude/rules/git-onedrive-codex.md` — OneDrive working-tree health checks (always-loaded; pairs with this skill)

## See also
- `AGENTS.md` §10 (Local environment — OneDrive + git layout) for the durable repo layout that motivates this skill
