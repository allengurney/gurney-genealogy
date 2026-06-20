#!/usr/bin/env python
"""PreToolUse guard: gate Bash/PowerShell commands that search repo content with
grep/find/rg/Select-String, steering toward the repo's repo_search-first tooling.

Reads the hook JSON on stdin, inspects tool_input.command, and emits a PreToolUse
"ask" decision (a confirm gate — grep remains a usable last resort, not blocked)
when the command invokes a content/file search tool. Allows the command silently
(exit 0, no output) when it explicitly targets a non-repo path (the ~/.claude
auto-memory area) or carries the opt-out marker `#grepok`.

Rule source: AGENTS.md s0a (repo_search-first). See .claude/CLAUDE.md.
"""
import sys
import json
import re

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)  # unparseable input -> do not block

cmd = ((data.get("tool_input") or {}).get("command") or "")
if not cmd:
    sys.exit(0)

# Explicit non-repo escape hatches: the auto-memory/config area, or an opt-out
# marker the model adds when it has consciously decided a non-repo grep is right.
if re.search(r"\.claude[\\/]projects", cmd) or "#grepok" in cmd:
    sys.exit(0)

# command-position prefix: start of line/command, or after a pipe/sep/xargs
PRE = r"(?:^|[|&;(]|\n|\bxargs\s+)\s*"
patterns = [
    PRE + r"(?:grep|egrep|fgrep|rg|ripgrep)\b",
    PRE + r"find\b(?=[^|&;\n]*\s-(?:i?name|path|regex)\b)",
    r"\bSelect-String\b",
    r"(?:Get-ChildItem|gci)\b[^|&;\n]*\s-[Rr]ec(?:urse)?\b",
]

if any(re.search(p, cmd, re.IGNORECASE) for p in patterns):
    reason = (
        "repo_search-first (AGENTS §0a): prefer `.venv/Scripts/python.exe "
        "tools/repo_search.py search --terms ...` for repo content and the Glob tool "
        "for filenames. grep / find / rg / Select-String are a LAST RESORT — only when "
        "repo_search genuinely can't answer the question. Confirm to run this one, or "
        "switch to repo_search. (Auto-allowed for non-repo paths like the ~/.claude "
        "auto-memory dir, or when the command carries the marker `#grepok`.)"
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": reason,
        }
    }))

sys.exit(0)
