# Prompt — Fable: G4 graph-editor UI polish

Give this to Fable 5. The §14 read/write contract is FIXED, so this is
frozen-spec UI work — styling, layout, and interaction polish only, no behavior,
API, or save-semantics changes (§18 Fable lane). It can happen any time; it is not
gated on 2a or cutover.

```
Work in main. Polish the G13 graph-editor browser UI — visual design, layout,
readability, and keyboard/interaction affordances only. The read/write contract is
fixed (Plan 01 §14); do NOT change the JSON API, save/validate/diff semantics,
ops, or any Python in tools/g13_graph/ or tools/g13_graph_editor/server.py.

Read tools/g13_graph_editor/README.md (architecture, save semantics, API) and
Plan 01 §14 first. Work only in tools/g13_graph_editor/static/ (index.html,
app.js, styles.css — vanilla JS, no build step; keep it build-step-free).

In scope:
- Clean, legible layout for the item detail view (statement, kind, status,
  confidence, visibility, sources with roles/locators/excerpts, incoming/outgoing
  relations, dates, publication impact, revision history, duplicate warnings).
- Clear visual distinction between item kinds and between blocking errors vs.
  advisory warnings in the preview/commit modal.
- The before/after diff and the publication-readiness advisory should be easy to
  scan before committing.
- Keyboard navigation for the filter list and the confirm/commit modal; visible
  focus states; sensible tab order; ARIA labels on controls.
- Responsive enough to be usable on a laptop screen; no horizontal scroll traps.

Out of scope (do not touch): the loopback/Host/Origin security, the transactional
save path, validation, exports, or any new feature. Do not add build tooling,
frameworks, or external CDN dependencies.

Develop against a STAGING copy, never the live canonical DB: seed a staging DB
from a committed snapshot via `g13_graph.py --db <staging.sqlite> --export-dir
<staging-exports> restore --from <snapshot>`, then launch
`g13_graph_editor.py --db <staging.sqlite> --export-dir <staging-exports>`
(the server refuses the live DB without --allow-live — do not pass it). Verify the
existing test_editor.py still passes. Do not commit unless asked.
```
