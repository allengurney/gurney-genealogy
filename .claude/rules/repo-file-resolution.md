---
paths:
  - "**/*"
---

# Repo file resolution

## Preferred lookup order
1. Exact repo-relative path on the current branch/ref
2. Explicit file attached to the current chat
3. Explicit file in another connected workspace/project
4. External URL

## Rules
- If the exact repo path is known, open that path directly.
- Do not hunt for a public GitHub URL when the file lives in the repo.
- Do not use search to rediscover a known path.
- Carry the exact branch/ref through the whole task.
- Resolve filename ambiguity once, then use the exact path thereafter.
- Say which source you are using when the same filename may exist in more than one place.

## Canonical repo anchors
- Structured data: `data/`
- Published narratives: `fact-sheets/`
- Working knowledge: `research/`
- Intake queue and patchsets: `sources/intake/`
- Source artifacts: `sources/media/`
- Validation notes: `sources/validations/`

## Destination discipline
- Put new knowledge in `research/`, not in validations or logs.
- Use validations for source/method notes.
- Use intake patchsets for step-by-step execution instructions.

## Mandatory related rules (share path scope)
None — this rule is always-loaded; lookup discipline applies repo-wide.

## See also
- `AGENTS.md` §3 — explicit enumeration of every rule and skill
- Directory READMEs (`research/README.md`, `sources/README.md`, `data/README.md`, `fact-sheets/README.md`) — destination guidance when a finding could land in more than one place
