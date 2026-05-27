# gurney-genealogy

Genealogical research repository and website source material for the Gurney lineage.

Published output: [https://genealogy.allengurney.com/](https://genealogy.allengurney.com/)

## Repository structure
- `data/` — canonical structured data for ancestors, places, and sources
- `fact-sheets/` — published ancestor narratives
- `research/` — working research files, companions, topics, places, case files, and logs
- `sources/` — intake, source media, validation worksheets, archive material, and full-text extracts
- `site/` — site-generation layer (Eleventy)
- `tools/` — lineage-specific utilities and exploratory artifacts

## Working principle
Canonical facts live upstream in `data/` and the research layer. Published narratives live in `fact-sheets/`. Source validations record what was examined; substantive findings live on the relevant subject file.

## Entry points for AI work
- `AGENTS.md` — universal AI entry point: identity, lineage status vocabulary, standing facts (corrections that should not be re-derived), source-specific flags, verification order, plus an explicit enumeration of every rule and skill in the repo with its path scope. Read by Codex CLI by convention, by Claude Code via `@AGENTS.md` import from `.claude/CLAUDE.md`, and by Copilot via `.github/copilot-instructions.md` pointer. Other AIs and ChatGPT sessions should be seeded with "Read AGENTS.md."
- `.claude/CLAUDE.md` — Claude Code session-start; imports AGENTS.md, then adds Claude-Code-specific notes about path-scoping and the rule architecture.
- Directory READMEs (`data/README.md`, `research/README.md`, `sources/README.md`, `fact-sheets/README.md`) — destination guidance for what lives where.

README files remain human-facing repository guides; rules and skills under `.claude/` are AI-centric.
