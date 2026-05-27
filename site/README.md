# site/

Site-generation layer for the public genealogy site. Published output: [https://genealogy.allengurney.com/](https://genealogy.allengurney.com/)

## Principle
This directory is presentation-oriented. Canonical facts and canonical prose live upstream in `data/`, `fact-sheets/`, and `research/`.

## Active working directories
- `website/` — current Eleventy source used to build deployable `_site/` output and the manual upload package.
- `New website design/` — static design prototype/archive for the baseline refactor.
- `Map-Create-23April2026/` — map generation scripts and notes for the standalone ancestor map artifact.

## Data rule
Use the canonical ancestor JSON at `data/ancestors.json`, with places resolved through `data/places.json` and `data/places_detail.json`. Site-local JSON under `site/website/_data/` is generated/presentation output, not the source of truth.

## Current state
Migration remains in progress. Avoid treating this folder as the authoritative content layer.

## AI / automation guidance
See:
- `.claude/rules/site-generation.md`
- `.claude/rules/data-json.md`
