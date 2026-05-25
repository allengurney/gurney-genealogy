---
paths:
  - "**/*"
---

# Continual improvement of rules and prose

## Purpose
Rules in `.claude/` and prose under `fact-sheets/`, `research/`, and `data/`
should improve as feedback arrives. This rule binds AI to capture that
feedback durably rather than relying on it being repeated.

## When to update a rule
When the user gives a **critical correction or durable guidance** that would
plausibly apply to future work, update the matching rule file in the same turn
as the work that triggered the feedback.

Treat as rule-worthy:
- corrections to writing style, vocabulary, or reader-facing tone
- corrections to citation, footnote, or sourcing posture
- corrections to layer discipline (what belongs in fact sheet vs. research vs. validation vs. data)
- corrections to how AI should handle ambiguity, disclosure, or escalation

Treat as **not** rule-worthy:
- one-off content choices that depend on the specific ancestor
- task-scoped routing decisions
- transient operational preferences

## Permission posture
- The user does **not** need to re-grant permission for the rule update when the
  feedback itself is the rule. Apply the update in the same turn.
- AI must **disclose** the rule update plainly in the response: which file
  changed, what the new guidance is, and which user feedback drove it.
- If the feedback is ambiguous between "one-off" and "rule-worthy," ask before
  writing the rule.

## Correcting things found along the way
When working on a directed task, AI may **correct related issues found in the
same files** without separate permission, provided:

- the correction is narrow and follows existing rules
- the correction does not change a substantive factual claim without evidence
- AI **discloses** each such correction in the response (file, what changed, why)

Examples of in-scope adjacent corrections:
- typo, broken anchor, dead footnote reference, or stale internal link
- acronym expansion consistent with `.claude/rules/fact-sheets.md`
- removal of internal-mechanics vocabulary ("repo," "FS structured field," etc.) from reader-facing prose
- citation moved from body to footnote when the citation rules already require it
- duplicate or contradictory phrasing within the same file

Out of scope (still ask first):
- adding new factual claims
- materially rewriting paragraphs
- changing sourceIds or `data/` content
- changes that span more than the file(s) directly in the task

## Focus area: writing and narrative
Writing-style rules are the most active surface for continual improvement.
When the user gives feedback on phrasing, vocabulary, footnote placement, or
reader-facing tone, the corresponding rule (`fact-sheets.md`,
`research-writing-style.md`, `citations.md`) should usually absorb it.

## Classify every "pull" by online availability
Whenever AI lists future research pulls (in a research file, a patchset, an
open-questions section, a summary, or anywhere else), each pull must carry an
explicit availability tag — one of:

- **Available online** — AI knows for sure the source is accessible online,
  because AI has verified the URL, fetched the page, or has a recent reliable
  pointer to a digitised copy (HathiTrust, Internet Archive, Gallica, archive
  catalogue, university repository, etc.).
- **Unknown online** — AI does not know whether the source is online. Use this
  as the default when AI has not actually tried to find a digitised copy.
- **Not online** — AI has explicitly looked and found references indicating
  the source is not digitised, the manuscript is in private hands, the
  archive has restricted access, or the only known copy is held in a physical
  repository without a digital edition.

The tag goes inline with each pull, e.g.: "EYC vol. 8, pp. 6–7 (Available
online — archive.org)" or "Cordier MS *Histoire de Gournay* (Not online — held
privately, never published in transcription beyond Potin 1842 extracts)."

This lets the user decide which pulls AI can pursue immediately vs. which
require library access or other manual work.

## Direct edits still defer to intake-layer thinking
Direct edits to `fact-sheets/`, `research/`, or `data/` (i.e., not going
through `sources/intake/`) do not exempt the work from the discipline encoded
in the intake skills and rules.

Before a direct substantive edit, AI should briefly reflect on:
- `.claude/rules/citations.md` — citation placement and source alignment
- `.claude/rules/fact-sheets.md` or the matching path-scoped rule for the file being edited
- `.claude/rules/sources-intake.md` — even when not writing a patchset, the
  promotion-writing standard ("lead with the knowledge; keep intake/process
  mechanics out of visible prose") applies
- `.claude/skills/research-intake-prep/SKILL.md` — the research-block style
  (lead with the finding, compact wording, no caveat inflation) is the right
  default for any new prose, patchset or not

The pre-edit reflection should be short — naming the relevant rule(s) in
thought, not in the output — but it must happen. The goal is that a direct
edit and an applied patchset produce indistinguishable prose quality.

## Cross-reference
- `.claude/CLAUDE.md`
- `.claude/rules/fact-sheets.md`
- `.claude/rules/research-writing-style.md`
- `.claude/rules/citations.md`
