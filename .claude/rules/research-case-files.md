---
paths:
  - "research/case-files/*.md"
---

# Research case-file rules

Human-facing overview:
- `research/README.md`

## Purpose
Case files are **user-initiated in-depth publication artefacts** — problem statements, biographies, and similar deliverables that the user directs into standalone treatment when a topic warrants it.

A case file is a human determination. The user decides when one is warranted. The repo's current case-file footprint is intentionally small (one identification problem statement and one biography at the time of writing).

## AI posture
- Do not promote findings into a case file without explicit user direction.
- Sustained per-ancestor argument, competing hypotheses, evidence weighing, and chronology for an individual ancestor go inside that ancestor's `research/people/g{NN}-{slug}.research.md` companion, not into a new case file.
- Cross-cutting analysis goes into a `research/topics/*.md` file.
- When a user directs a new case file, AI may help draft and edit it under the standards below.

## Expected shape (when one exists)
- the problem statement or biographical scope
- competing hypotheses or chronology, as relevant
- evidence ledger or structured analysis
- source discussion
- assessment of strengths and weaknesses
- current conclusion and confidence level
- open items

## Standards
- Do not compress uncertainty into false certainty.
- Preserve the argument trail.
- Keep rejected paths visible when they materially explain why a conclusion was reached.
- Cite every material evidentiary assertion and interpretive turning point. When a probability estimate is given, make the supporting basis visible nearby.
- Subject-level findings that belong on a person or place file should be crosslinked there. A case file is not a substitute for updating the relevant subject file.

## Mandatory related rules (share path scope)
- `.claude/rules/citations.md` — both scope `research/**/*.md` (case-files subdir); source-traceability applies

## See also
- `.claude/rules/research-files.md` — sustained per-ancestor argument and competing hypotheses live in the ancestor's `research/people/` companion, not here
- `.claude/rules/research-writing-style.md` — finding-first prose
