# tools/

Lineage-specific tools and interactive artifacts.

## Current use
This directory holds exploratory or utility artifacts that support the genealogy workflow but are not themselves canonical research content.

## Notable tools

- **`research_leads.py`** — CLI for `research/future-research/research-leads.csv`: retrieve lead context by ID, list priority/online-reachable leads, search, validate, update, add, and close leads without reading or rewriting the full catalog manually.
- **`repo_search.py`** — lossless staged search across ancestors, places, topics, sources, research, leads, and intake history. It saves exhaustive local ledgers while returning compact manifests and paged, footnote-attached results for AI use; `locate` returns an exact `path:line`, and `infile` deep-reads a single named file with fuzzy, context-windowed passages. See `repo_search_README.md`.

- **`g13_graph.py`** — standalone lifecycle CLI for the canonical G13 SQLite
  context graph. Phase G1B provides schema migration, source-registry and
  source-hash synchronization, synthetic seeding, validation, rebuildable FTS,
  deterministic recovery export/restore, build reports, status, and basic
  item/source/unit/impact reads without changing `repo_search.py`. See
  `g13_graph/README.md`.

## Principle
If a tool becomes broadly reusable, consider moving it to a more general repo or toolset. None meet this criteria.

## AI / automation guidance
General repo behavior still applies.
See:
- `.claude/CLAUDE.md`
