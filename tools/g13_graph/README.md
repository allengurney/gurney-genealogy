# G13 SQLite context graph — core package (Phases G1B–G5)

This standalone module implements the plumbing contract in
`tools/plans/G-13 Refactor/01-sqlite-context-graph-design.md`. It does not read,
write, or synthesize G13 research prose and it is not integrated with
`repo_search.py`.

## Storage and configuration

The default canonical database is:

```text
C:\Users\allen\GitDirs\gurney-genealogy-g13-graph\g13-context.sqlite
```

It is deliberately outside OneDrive, Git, the repo-search cache, and temporary
directories. Override it for tests or staging with `GURNEY_G13_GRAPH_DB`.
`GURNEY_G13_GRAPH_EXPORT_DIR` and `GURNEY_G13_GRAPH_SOURCES` similarly override
the recovery-export directory and source registry.

Every connection enables foreign keys and a five-second busy timeout. Writable
connections use WAL with `synchronous=FULL`; WAL is appropriate because the
durable database is outside OneDrive. Tests isolate the database and its
`-wal`/`-shm` sidecars in a temporary directory.

All writes use explicit `BEGIN IMMEDIATE` transactions. A failed write rolls
back completely. Live database files are never copied for backup; restore uses
SQLite's online backup API before destructive replacement.

## Durable contracts

- Ordered SQL migrations under `schema/migrations/` are the canonical schema.
- Research-item IDs are stable and kind-neutral. Reclassification changes
  `item_kind`, not `item_id`.
- `source_registry` is a derived, hashed mirror of `data/sources.json`.
  `canonical_path` deterministically prefers `corpusPath`, then `mediaPath`,
  `validationPath`, and finally the source URL; `registry_source_path` is
  repository-relative when the configured registry is inside the checkout.
- Every accepted content transaction increments `database_revision`.
- Item changes write `item_revisions` in the same transaction.
- A committed content transaction is not rolled back if the subsequent
  recovery export fails. The command returns nonzero, `status` reports the DB
  ahead, and restore/migration safety checks require a current recovery export.
- `current.ndjson` is atomically replaced through a narrowly ignored
  `current.ndjson.tmp-*` file.
- Versioned snapshots are named `g13-context-rNNNNNN.ndjson`.
- Cited local source artifacts can receive content-hash baselines. Validation
  detects drift by comparing current artifact bytes to the stored baseline; it
  never hashes prose research text.
- FTS5 indexes for items, entities/aliases, and research units are derived,
  revision-stamped, excluded from recovery exports, and rebuilt after restore.

## Recovery format

Deterministic NDJSON is the sole authoritative logical restore format. The first
record is a manifest containing schema version, database revision, source
registry hash, table counts, a revision timestamp, and a logical-content hash.
Every logical table follows in the fixed order declared by
`constants.LOGICAL_TABLE_ORDER`; rows are ordered by primary key and JSON keys
are sorted. Repeated exports of an unchanged revision are byte-identical because
the export timestamp is the database revision's committed timestamp. FTS or
other rebuildable indexes are excluded.

Restore validates format, schema, counts, table order, graph metadata, and the
logical-content hash before opening a write transaction. It refuses to move the
database revision backward or replace an existing DB whose rolling recovery
export is stale.

## CLI

```powershell
.\.venv\Scripts\python.exe tools\g13_graph.py init
.\.venv\Scripts\python.exe tools\g13_graph.py migrate
.\.venv\Scripts\python.exe tools\g13_graph.py sync-sources
.\.venv\Scripts\python.exe tools\g13_graph.py seed --file <fixture>
.\.venv\Scripts\python.exe tools\g13_graph.py validate
.\.venv\Scripts\python.exe tools\g13_graph.py status
.\.venv\Scripts\python.exe tools\g13_graph.py export --recovery
.\.venv\Scripts\python.exe tools\g13_graph.py export --snapshot
.\.venv\Scripts\python.exe tools\g13_graph.py restore --from <snapshot>
.\.venv\Scripts\python.exe tools\g13_graph.py export-website [--out <dir>]
.\.venv\Scripts\python.exe tools\g13_graph.py item <item-id>
.\.venv\Scripts\python.exe tools\g13_graph.py source <source-id>
.\.venv\Scripts\python.exe tools\g13_graph.py unit <unit-id>
.\.venv\Scripts\python.exe tools\g13_graph.py impact <item-id>
.\.venv\Scripts\python.exe tools\g13_graph.py search --terms <term> [...]
.\.venv\Scripts\python.exe tools\g13_graph.py reindex
.\.venv\Scripts\python.exe tools\g13_graph.py hash-sources
.\.venv\Scripts\python.exe tools\g13_graph.py report [--output <path>]
.\.venv\Scripts\python.exe tools\g13_graph.py context --terms earliest Weymouth presence --mode grounding --budget 12000
.\.venv\Scripts\python.exe tools\g13_graph.py context --ids <item-id> --mode research --relation-types SUPPORTS DEPENDS_ON
.\.venv\Scripts\python.exe tools\g13_graph.py context --entity-ids <entity-id> --mode audit
.\.venv\Scripts\python.exe tools\g13_graph.py context --mode exhaustive
```

Command output is written as UTF-8 regardless of the Windows console code page,
so quoted transcriptions and en-dashes survive a redirect or pipe.

Global `--db`, `--export-dir`, and `--sources` overrides are also available and
must precede the subcommand.

The seed loader is one-time bootstrap input, not an editable JSON truth layer.
Tests use only `tests/fixtures/synthetic-seed.ndjson` and its synthetic source
registry.

## Context compiler (Phase G2)

`context` seeds active/open research items by conjunctive `--terms`, explicit
`--ids`, or `--entity-ids`, then traverses graph relations in both directions.
`--relation-types` restricts both traversal and returned edges. Modes control
scope:

- `grounding` (default) — one relation hop.
- `research` — two relation hops.
- `audit` — the complete connected component.
- `exhaustive` — every active/open item, including disconnected items.

The coverage ledger names every active/open item considered, every seed and
expanded item, every compactly included item, and every omitted item with a
reason. It also reports unresolved explicit IDs, detail omissions, graph
distance, and the route by which each item was expanded. Review-state,
knowledge-window, relation-review, and source-hash warnings travel with the
package.

`--budget` is a character budget over deterministic compact JSON. Detail is
shed only in the Plan 01 §12 order: evidence excerpts, context-only item detail,
low-bearing related entities, then full source metadata already addressable by
`sourceId`. Item IDs and short statements always survive. Evidence-conflict
records, negative-result scope/limitations, and coverage/omission notices are
protected. If the protected minimum exceeds the budget, the compiler returns
the complete protected package with `within_budget: false`; it never silently
truncates.

`hash-sources` captures only missing local-source baselines by default.
`--accept-current` is an explicit reviewed-drift operation: it replaces changed
baselines and writes `review` entries for directly citing research items.

`report` writes a deterministic health/build report containing graph counts,
validation issues, source-hash state, derived-index state, and backup-tier
status. The default destination is `data/context-graphs/g13/build-report.json`;
tests use `--output` in a temporary directory.

## Static website export (Phase G5)

`export-website` writes a deterministic, read-only public export for the future
graph-enhanced website under `<export-dir>/website` (override with `--out`):
`manifest.json`, a `findings.json` index, an `adjacency.json` node/edge slice,
and one `findings/<item_id>.json` page per public item. It never mutates the
database, prose, or source files.

Publication safety is enforced at the export boundary (Plan 01 §14, §16 G5):

- **Public items only** — only `visibility='public'` research items are emitted;
  `repo_only`/`restricted` items and every repo-internal field (research
  location, reviewer, notes, restriction reason, the numeric confidence mirror)
  are omitted.
- **Publishable excerpts only** — a source `evidence_excerpt` is emitted only
  when `excerpt_publishable` is set; `sourceId` and locator are always safe.
- **Edges only between public endpoints** — an adjacency edge is emitted only
  when both items are public, so a restricted id/label cannot leak through a
  relation; publication mappings are emitted only for `published` status.
- **Band confidence only** — the confidence label is exported, never the numeric
  value (§8.2).

The export is byte-deterministic (item/edge ordering, sorted keys, revision-
timestamped manifest), mirroring the recovery export. `test_website.py` proves
the safety contract by injecting rows the validator would reject (public→
non-public edge, non-publishable excerpt on a public item, retired publication)
and asserting they are stripped. With the current staged graph carrying no public
items yet, the live export is intentionally empty until items are marked public.

## Phase boundary

G2 (context compiler), G4 (graph editor, `tools/g13_graph_editor/`), and G5
(static website export) are implemented. Real G13 content covers the accepted
Phase P colonial-arrival slice plus the Phase G3 colonial-Braintree increment
(`research/people/_staging/g13-john-gurney/`, items `G13-RI-000001..000017`);
broader G3 research assimilation continues topic by topic.
