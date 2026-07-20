#!/usr/bin/env python
"""PreToolUse guard: gate Bash/PowerShell commands that search repo content with
grep/find/rg/Select-String, steering toward the repo's repo_search-first tooling.

Reads the hook JSON on stdin, inspects tool_input.command, and emits a PreToolUse
"allow" decision with a top-level `systemMessage` warning (visible in the chat
transcript, but non-blocking — no approval prompt) when the command invokes a
content/file search tool against the filesystem. grep remains a usable last
resort; this guard nudges toward repo_search without stopping execution.
Allows the command silently (exit 0, no output) when it explicitly targets a
non-repo path (the ~/.claude auto-memory area), carries the opt-out marker
`#grepok`, or **reads from a pipe** (`cmd | grep ...`) — a piped search filters
another command's OUTPUT, not repo content, so it is not the behavior this guard
exists to steer. Only a standalone search command (line start, or after ; && & (
or xargs) is gated.

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

# command-position prefix: start of line/command, or after ; && & ( newline or
# xargs — but NOT after a pipe. A search tool fed by a pipe ("cmd | grep foo")
# is filtering command OUTPUT, not searching repo content, so it is intentionally
# left silent (the common false-positive that prompted on benign output filtering).
PRE = r"(?:^|[&;(]|\n|\bxargs\s+)\s*"
patterns = [
    PRE + r"(?:grep|egrep|fgrep|rg|ripgrep)\b",
    PRE + r"find\b(?=[^|&;\n]*\s-(?:i?name|path|regex)\b)",
    PRE + r"Select-String\b",
    PRE + r"(?:Get-ChildItem|gci)\b[^|&;\n]*\s-[Rr]ec(?:urse)?\b",
]

if any(re.search(p, cmd, re.IGNORECASE) for p in patterns):
    warning = (
        "⚠️ repo_search-first (AGENTS §0a): this command used grep/find/rg/Select-String "
        "directly. Prefer `.venv/Scripts/python.exe tools/repo_search.py search --terms ...` "
        "for repo content and the Glob tool for filenames — grep is a LAST RESORT. Allowed "
        "to run (not blocked). (Auto-silent for non-repo paths like the ~/.claude auto-memory "
        "dir, or when the command carries the marker `#grepok`.)"
    )
    print(json.dumps({
        "systemMessage": warning,
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "additionalContext": warning,
        }
    }))

sys.exit(0)
