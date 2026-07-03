# G13 SQLite context graph — Phase G0/G1A

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
.\.venv\Scripts\python.exe tools\g13_graph.py item <item-id>
```

Global `--db`, `--export-dir`, and `--sources` overrides are also available and
must precede the subcommand.

The seed loader is one-time bootstrap input, not an editable JSON truth layer.
Tests use only `tests/fixtures/synthetic-seed.ndjson` and its synthetic source
registry.

## G1A boundary

This phase does not implement a context compiler, relationship-budget
expansion, FTS, the graph editor, website exports, or any real G13 content.
