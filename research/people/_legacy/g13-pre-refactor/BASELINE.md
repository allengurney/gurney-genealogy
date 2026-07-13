# G13 pre-refactor legacy baseline

Captured at cutover start: `2026-07-13T17:25:55Z`.

This directory is the Level 2 rollback source for the former root companion.
It is intentionally retained through the acceptance window; it is not a source
of current G13 research prose.

## Companion copy

| Item | Value |
|---|---|
| Original path | `research/people/g13-john-gurney-fact-sheet.research.md` |
| Copy path | `research/people/_legacy/g13-pre-refactor/g13-john-gurney-fact-sheet.research.md` |
| SHA-256 (original and verified copy) | `41189a50f694ca749e40f3ae5cd870e8423949ad6d8de4bc50dabaf2fccef364` |
| Lines | 407 |
| Words | 18,799 |
| Headings | 36 |
| Footnotes | 67 |
| Cutover-start commit | `a732718ed935bc572bb60b743c0667eec7c53b66` |

## Graph recovery baseline

The live SQLite database is deliberately external to Git and OneDrive. Its
logical recovery artifacts are the rollback backup; the database binary is not
copied directly.

| Store | Revision | Recovery / snapshot | SHA-256 |
|---|---:|---|---|
| Canonical graph | 218 | `data/context-graphs/g13/exports/current.ndjson` and `snapshots/g13-context-r000218.ndjson` | `1063811379d1694c17caf09b1873bb596a4a8aa16234967c2349a63c7e338038` |
| Archived staging graph | 194 | `C:\\Users\\allen\\GitDirs\\gurney-genealogy-g13-graph\\staging-exports\\current.ndjson` and `snapshots/g13-context-r000194.ndjson` | `562fe3a9ac7ef01c5c62ecd3df46dfd18ba6f968c5f386eb550f0c141bc8a2cf` |

The archived staging database's binary SHA-256 at capture was
`c0e5e9fb11e3598e3a1ce931ab09ad6f53cc3201e823eb09af79e9bf0ba1782f`.
It is retained as an archive, not as a valid current graph: its source registry
is stale against the current source registry.

## Rollback use

- **Level 1:** change the site content mode back to `legacy`.
- **Level 2:** restore the copied companion to its original root path.
- **Level 3:** retain/quarantine the promoted library, restore this companion,
  select legacy mode, and restore/retire the canonical graph from its recorded
  recovery snapshot rather than deleting it.
