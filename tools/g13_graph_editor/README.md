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

## Running

### Double-click launcher (recommended)

From the repository root, double-click:

```text
Launch-G13-Graph-Editor.cmd
```

The launcher checks the repository `.venv`, editor files, live database,
recovery export, source mirror, validation state, derived indexes, recovery
state, and port availability. It then opens the editor in the default browser
after the loopback server answers. The visible console reports the selected
database and remains the shutdown control: press `Ctrl+C` there to stop.

Its menu offers:

- **Staging / test** (default) — creates staging from the current live recovery
  export when absent. If staging is behind live, it offers to archive the old
  staging DB/export pair and refresh it.
- **Refresh staging** — archives, rather than deletes, the current staging pair,
  then restores a clean copy from live.
- **Live / production** — requires typing `LIVE`; the editor still receives the
  required `--allow-live` flag and the live DB/export paths explicitly.
- **Status only** — compares live and staging without starting a server.

For scripted checks:

```powershell
.\tools\launch_g13_graph_editor.ps1 -Mode Staging -CheckOnly
.\tools\launch_g13_graph_editor.ps1 -Mode Status
.\tools\launch_g13_graph_editor.ps1 -Mode Staging -Port 8766
```

The editor does not need a Windows tray process or background service. It is
used intermittently, starts quickly, and its visible console makes the active
database and shutdown state unambiguous.

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
  negative-result scope, publication impact, prose markers, revision history,
  duplicate warnings.
- Navigate person/place/source/unit/item/marker neighborhoods by clicking any
  linked id.
- Prose markers (Plan 2a `<!-- graph-marker: G13-PM-… -->` tokens in topic
  files) are first-class: the item detail lists the markers that map an item;
  the marker view shows the prose location + copyable token, the mapped items
  in display order with roles, status/visibility editing, membership editing
  (add / remove / make-primary), and the `marker_revisions` audit trail.
  Marker edits are validated by the reused G1B marker validators — e.g. an
  active marker cannot be created before its token exists in the unit's
  Markdown file (`marker_token_count_invalid` blocks it).
- Filter by kind, status, confidence, visibility, review state, unit, source,
  unresolved conflict, publication impact, and pending-publication-decision.
  A `G13-PM-…` id pasted into the text filter matches the items that marker
  maps; the Search tab resolves pasted ids (items, markers, entities, units,
  sources) directly, ahead of FTS matches.
- Pick lists for every controlled vocabulary; source/entity autocomplete
  (sources from the registered `source_registry`; entities from the `entities`
  table). Only registered `sourceId`s can be linked (DB-enforced).
- Machine-suggested **review queue** with batch accept/reject.
- Undo (revert an item to its previous audited state) and discard (cancel a
  staged change in the modal). Retire = soft-delete (kept in the audit trail;
  hard delete is intentionally impossible once an item carries revisions).
- Publication readiness advisory: visibility + excerpt-publishability decisions
  are surfaced per item so they can be made before a future static export (G5);
  the confirm modal also warns when the edited item is already mapped into
  published prose.

## UI affordances

- Item kinds are color-coded (chip + list-row left border); source roles and
  relation types carry supports/contradicts/qualifies semantics in color.
- Source-role chips on the item detail use reader-facing directional phrasing
  ("supported by", "contradicted by", "mentioned in", …) because the stored
  role reads source → item and a chip in front of the source id would invert
  it; the canonical vocabulary value stays in the chip tooltip. The source
  neighborhood's "Cited by" list keeps the raw verb (direction reads correctly
  there).
- Keyboard: `/` focuses the filter or search box, `↑`/`↓` move through result
  lists, `Enter` opens; `←`/`→` move between tabs; the confirm modal traps
  focus, defaults to **Commit** (or **Discard** when blocked) and closes on
  `Escape`. Blocking errors render as a red panel, advisory warnings as amber.
- Selection is deep-linkable: `#item/<id>` or `#marker/<id>` in the URL
  restores the view on reload (and tells a paired AI session what is on
  screen).
- **Copy AI context** on the item header copies a self-contained markdown
  block (statement, sources, relations, dates, publication mappings, DB path
  and revision, API/edit-tooling pointers) for pasting into a Claude session
  when a revision needs AI help.

## JSON API

Read: `GET /api/status`, `/api/picklists`, `/api/items?<filters>`,
`/api/item/<id>`, `/api/marker/<id>`, `/api/impact/<id>`,
`/api/neighborhood?kind=&id=` (kind: item | source | unit | entity | marker),
`/api/review-queue`, `/api/sources?q=`, `/api/entities?q=`, `/api/units`,
`/api/search?terms=` (direct id hits merged ahead of FTS matches),
`/api/source-hashes`.

Write: `POST /api/preview` (stage → validate → diff → rollback),
`POST /api/commit` (validate → apply → audit → refresh),
`POST /api/snapshot`, `POST /api/export-recovery`. A blocked commit returns
`409` with `blocking_errors`; a constraint violation returns `400`.

Change payload shape: `{ "op": "<op>", "params": { ... }, "changed_by": "..." }`.
Supported ops: `create_item`, `update_item`, `supersede_item`, `retire_item`,
`set_review_state`, `undo_item`, `add_relation` / `update_relation` /
`remove_relation`, `add_source_link` / `update_source_link` /
`remove_source_link`, `add_entity_link` / `remove_entity_link`, `create_entity` /
`update_entity`, `create_research_unit` / `update_research_unit`, `set_dates`,
`set_negative_scope`, `add_publication` / `remove_publication`, `create_marker` /
`update_marker` / `set_marker_primary`, `add_marker_item` /
`update_marker_item` / `remove_marker_item`. Marker ops audit into
`marker_revisions` (snapshots include the member rows); `set_marker_primary`
performs the demote/promote/repoint atomically because the schema's deferred FK
requires all three in one transaction. Whole-topic increments (a unit +
entities + items + relations + markers in one transaction) go through
`tools/g13_graph/authoring.py` / the `author-batch` CLI, which reuses these ops
for creation; post-hoc marker maintenance is what the editor ops are for
(author-batch only creates).

## Tests

`tools/g13_graph/tests/test_editor.py` covers transactional save/rollback,
revision logging, validate-before-save (delta blocking), post-save
recovery-export refresh (including the derived-step-failure stale path),
create/relation/source round-trips, unregistered-source rejection, batch
review-queue accept, and the marker surface (item-detail/marker reads, id
lookup, membership ops with `marker_revisions` audit, token-gated marker
creation).

```powershell
.\.venv\Scripts\python.exe -m unittest tools.g13_graph.tests.test_editor
```
