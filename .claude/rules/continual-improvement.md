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
- one-off content choices that depend on the specific ancestor (e.g., "for G14 specifically, use the laceweaver framing in the Highlights bullet" — does not generalize)
- task-scoped routing decisions ("put this finding under the John Gurney case file" — task-scoped, not a future rule)
- transient operational preferences ("today, skip the Phase-2 done-stamp" — situational)
- single-instance corrections that do not imply a pattern
- the user's judgement call on a specific document where the same call could plausibly go the other way next time

## Bias toward restraint
When in doubt about rule-worthiness, default to **not** writing a rule. Two reasons:

1. Reactive rules with absolutes cause oscillation (see "Avoid reactive absolutes" below) — a one-off feedback that becomes a rule often produces the opposite mistake on the next turn.
2. Rule accretion is the dominant drift pressure. Each unnecessary rule adds reconciliation cost across the rule surface. A rule that fires once a year and is wrong half the time is a net loss.

When unsure, capture the user's specific guidance in the work itself (the fact sheet, companion, or patchset), not in `.claude/rules/`. If the same correction recurs across multiple unrelated tasks, that recurrence is the signal it has become rule-worthy.

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

## Avoid reactive absolutes — prefer target bands
When the user gives directional feedback ("too long," "too short," "too much
Wikipedia," "too operational"), the rule update should record a **target band
with a soft heuristic**, not an absolute prohibition.

Reactive absolutes cause oscillation: the next turn often produces the
opposite mistake (purged context after "too long context"; purged Wikipedia
after "too much Wikipedia"). Bands resist this by leaving judgment room.

When phrasing a rule, ask: would acting on this rule in the most literal way
produce a defect the user would flag next turn? If yes, soften to a band.

## Consolidation passes
Rule files accumulate by accretion. When a new rule duplicates or
contradicts an existing one across files, or roughly every ~10 substantive
rule updates, run a consolidation pass:

- identify duplicated guidance across files (e.g., citation-placement rules
  appearing in both `fact-sheets.md` and `citations.md`)
- pick one canonical location for each piece of guidance
- replace duplicates with cross-references
- prune obsolete or contradictory rules

Consolidation passes are explicitly in scope under continual improvement.
They preserve the lessons accumulated in earlier updates while keeping the
aggregate rule surface tractable. Disclose the consolidation as a single
batched rule update.

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
- `.claude/rules/sources.md` — even when not writing a patchset, the
  promotion-writing standard ("lead with the knowledge; keep intake/process
  mechanics out of visible prose") applies
- `.claude/skills/research-intake-prep/SKILL.md` — the research-block style
  (lead with the finding, compact wording, no caveat inflation) is the right
  default for any new prose, patchset or not

The pre-edit reflection should be short — naming the relevant rule(s) in
thought, not in the output — but it must happen. The goal is that a direct
edit and an applied patchset produce indistinguishable prose quality.

## Mandatory related rules (share path scope)
None — this rule is always-loaded (`paths: **/*`); no other rule shares an equivalent universal scope.

## See also
This rule governs how all other rules change. The most active surfaces for continual improvement are `citations.md`, `fact-sheets.md`, `research-files.md`, `research-writing-style.md`, and `sources.md`.
