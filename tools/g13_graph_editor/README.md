# G13 graph-editing artifact — Phase G4

A small **loopback-only** local backend (Python stdlib `http.server`, reusing the
repo `.venv`) plus a browser UI for viewing, navigating, and editing the
canonical G13 SQLite context graph. It implements the fixed §14 contract in
`tools/plans/G-13 Refactor/01-sqlite-context-graph-design.md`.

The artifact reads and **writes the canonical SQLite database directly**. There
is no JSON import/export in the edit path and no second store. It reuses the
accepted G1B plumbing under `tools/g13_graph/` — validation, revisions, exporter,
status, drift — so G1B validation improvements flow into the editor automatically.

## Architecture

```
browser UI  ──HTTP/JSON──▶  tools/g13_graph_editor/server.py   (loopback only)
                                     │
                                     ▼
                        tools/g13_graph/editor.py              (save/validate/diff)
                                     │  reuses
   mutations.apply_item_update · validation.validate_connection · revisions ·
   exporter (recovery/snapshot/restore) · lifecycle.refresh_after_commit · status
                                     │
                                     ▼
                    canonical SQLite context graph (single store)
                       + in-model item_revisions (audit trail)
                       + automatic recovery export / milestone snapshot
```

- `server.py` — HTTP handler: static UI + JSON API. Binds `127.0.0.1` only;
  enforces a loopback `Host`-header allowlist (defeats DNS-rebinding) and a
  loopback `Origin` check on writes.
- `editor.py` (in the core package) — the transactional save service and the
  read surface for the editing UI. This is the tested unit.
- `static/` — `index.html`, `app.js`, `styles.css` (vanilla JS, no build step).
  UI polish is a later, separate Fable pass; this delivers the functional contract.

## Running

Development must run against a **staging copy**, never the live canonical DB.
Seed a staging copy from the current recovery export/snapshot, then launch:

```powershell
# 1. seed a staging DB from a committed export (does not touch the live DB)
.\.venv\Scripts\python.exe tools\g13_graph.py --db <staging.sqlite> `
    --export-dir <staging-exports> restore `
    --from data\context-graphs\g13\exports\snapshots\g13-context-r000003.ndjson

# 2. launch the editor against the staging copy
.\.venv\Scripts\python.exe tools\g13_graph_editor.py `
    --db <staging.sqlite> --export-dir <staging-exports> --port 8765
# open http://127.0.0.1:8765/
```

The server **refuses to open the live canonical database** unless `--allow-live`
is passed explicitly. `GURNEY_G13_GRAPH_DB` / `GURNEY_G13_GRAPH_EXPORT_DIR` /
`GURNEY_G13_GRAPH_SOURCES` overrides are honoured (same as the CLI).

## Save semantics (§14)

- **Validate before save, delta-based.** A change is staged inside a single
  transaction and validated *before* commit. Only error codes the change itself
  *introduces* block it, so a pre-existing warning or an unrelated error never
  prevents an otherwise-valid edit. Derived-artifact staleness
  (`derived_indexes_stale` / `recovery_export_stale`) is expected mid-edit and
  never blocks; it is resolved by the post-commit refresh.
- **Single transaction, rollback on any failure** (validation, integrity,
  exception) — the DB is never left partially edited.
- **Human-readable before/after diff** is computed from current DB state and
  shown in the confirm modal before committing (`POST /api/preview`).
- **Audit every accepted change**: create/update/supersede/review/delete write an
  `item_revisions` row with before/after row state, in the same transaction.
- **Never lose an accepted edit**: the content transaction commits first; the
  derived refresh (FTS reindex + recovery export) runs after. A derived-step
  failure marks the artifact **stale** (`stale: true`) and surfaces an
  unsafe-backup banner, but does **not** roll back the committed content edit.
- After each accepted change the rolling recovery export is refreshed; the status
  bar shows when the DB is **ahead of** the recovery export or latest milestone
  snapshot, and offers a "Milestone snapshot" action.

## Editing surface

- Item detail: statement, kind, status, confidence, visibility, excerpt
  publishability, provenance, research location, subject entity, sources with
  roles/locators/excerpts, incoming/outgoing relations, linked entities, dates,
  negative-result scope, publication impact, revision history, duplicate warnings.
- Navigate person/place/source/unit/item neighborhoods by clicking any linked id.
- Filter by kind, status, confidence, visibility, review state, unit, source,
  unresolved conflict, publication impact, and pending-publication-decision.
- Pick lists for every controlled vocabulary; source/entity autocomplete
  (sources from the registered `source_registry`; entities from the `entities`
  table). Only registered `sourceId`s can be linked (DB-enforced).
- Machine-suggested **review queue** with batch accept/reject.
- Undo (revert an item to its previous audited state) and discard (cancel a
  staged change in the modal). Retire = soft-delete (kept in the audit trail;
  hard delete is intentionally impossible once an item carries revisions).
- Publication readiness advisory: visibility + excerpt-publishability decisions
  are surfaced per item so they can be made before a future static export (G5).

## JSON API

Read: `GET /api/status`, `/api/picklists`, `/api/items?<filters>`,
`/api/item/<id>`, `/api/impact/<id>`, `/api/neighborhood?kind=&id=`,
`/api/review-queue`, `/api/sources?q=`, `/api/entities?q=`, `/api/units`,
`/api/search?terms=`, `/api/source-hashes`.

Write: `POST /api/preview` (stage → validate → diff → rollback),
`POST /api/commit` (validate → apply → audit → refresh),
`POST /api/snapshot`, `POST /api/export-recovery`. A blocked commit returns
`409` with `blocking_errors`; a constraint violation returns `400`.

Change payload shape: `{ "op": "<op>", "params": { ... }, "changed_by": "..." }`.
Supported ops: `create_item`, `update_item`, `supersede_item`, `retire_item`,
`set_review_state`, `undo_item`, `add_relation` / `update_relation` /
`remove_relation`, `add_source_link` / `update_source_link` /
`remove_source_link`, `add_entity_link` / `remove_entity_link`, `create_entity` /
`update_entity`, `set_dates`, `set_negative_scope`, `add_publication` /
`remove_publication`.

## Tests

`tools/g13_graph/tests/test_editor.py` covers transactional save/rollback,
revision logging, validate-before-save (delta blocking), post-save
recovery-export refresh (including the derived-step-failure stale path),
create/relation/source round-trips, unregistered-source rejection, and batch
review-queue accept.

```powershell
.\.venv\Scripts\python.exe -m unittest tools.g13_graph.tests.test_editor
```
