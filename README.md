# gurney-genealogy

Genealogical research repository and website source material for the Gurney lineage.

Published output: [](https://genealogy.allengurney.com/)

## Repository structure
- `data/` — canonical structured data for ancestors, places, and sources
- `fact-sheets/` — published ancestor narratives
- `research/` — working research files, companions, topics, places, case files, and logs
- `sources/` — intake, source media, validation worksheets, and archive material
- `site/` — site-generation layer
- `tools/` — lineage-specific utilities and exploratory artifacts

## Working principle
Canonical facts live upstream in `data/` and the research layer. Published narratives live in `fact-sheets/`. Source validations record what was examined, while substantive findings live on the relevant subject files.

## Repo path resolution
- Prefer exact repo-relative paths and the current branch/ref.
- Prefer the repo connector or local filesystem over public GitHub URLs when the file lives in this repo.
- Once a path is known, reuse it instead of searching again.
- Keep repo files, attached-chat files, and external URLs distinct.

## AI / automation guidance
For Claude Code behavior, see:
- `.claude/CLAUDE.md`
- `.claude/rules/`
- `.claude/skills/`
- `.claude/rules/repo-file-resolution.md`
- `.claude/rules/research-writing-style.md`

README files remain human-facing repository guides.
