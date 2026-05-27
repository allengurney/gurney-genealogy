# GitHub Copilot instructions

This repository's primary AI instructions live in **[AGENTS.md](../AGENTS.md)** at root. Read that first — it carries the project knowledge (identity, lineage status, standing facts, source-specific flags, verification order, tone, efficiency) plus an explicit enumeration of every rule and skill in the repo with its path scope.

The rules under `.claude/rules/` and skills under `.claude/skills/` are AI-agnostic content. Copilot may consult any of them by name as needed; AGENTS.md §3 lists each one with its purpose and path scope so you can pick the relevant ones for the work at hand.

Directory READMEs (`data/README.md`, `research/README.md`, `sources/README.md`, `fact-sheets/README.md`) carry destination guidance — "where does this finding belong, including multi-destination cases."
