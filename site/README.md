# site/

Site-generation layer for the public genealogy site.

## Principle
This directory is presentation-oriented. Canonical facts and canonical prose live upstream in `data/`, `fact-sheets/`, and `research/`.

## Active working directories
- `gurney-eleventy-project_source_clean_2026-04-08_v23/` — current Eleventy source used to build deployable `_site/` output.
- `New website design/` — static design prototype for the next website refactor.
- `Map-Create-23April2026/` — map generation scripts and notes for the standalone ancestor map artifact.

## Data rule
Use the most recent canonical ancestor JSON from the repo root. As of this branch, that is `data/ancestors v26.json`, with places resolved through `data/places.json` and `data/places_detail.json`.

## Current state
Migration remains in progress. Avoid treating this folder as the authoritative content layer.

## AI / automation guidance
See:
- `.claude/rules/site-generation.md`
- `.claude/rules/data-json.md`
