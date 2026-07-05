# G13 graph editor — AI-assisted revisions and deferred improvements

Status: recommendation (2026-07-04), written alongside the first UI-polish pass
of `tools/g13_graph_editor/`. The §14 read/write contract is unchanged; nothing
here proposes changing it.

## 1. The workflow question

Use case: Allen is reviewing an item in the editor and concludes it needs a
structural revision — e.g. one item comingles two events, so the fix requires
re-grounding from the repo prose, splitting the item, rewriting relations, and
possibly creating one or two new items.

**Assessment: Claude Code (or Cowork) alongside the open editor is the right
mechanism, and it needs almost no new machinery.** The reasons it fits:

- The graph already has exactly one safe write path — the transactional editor
  ops (`update_item`, `supersede_item`, `create_item`, relation/source ops) via
  `tools/g13_graph/editor.py` and the `author-batch` CLI. An AI session in this
  repo can drive those directly, with validate-before-save, audit revisions,
  and the recovery-export refresh all applying automatically. No editor-side
  AI integration is needed for correctness.
- The evidence needed for re-grounding (research prose, sources, footnotes)
  lives in the repo, which is what a Claude Code session can read cheaply and
  the browser tool cannot.
- The human stays in the loop naturally: Claude commits through the same ops,
  and the editor's **Refresh** shows the result immediately; **Undo last** and
  `item_revisions` give per-item rollback if the AI change is wrong.

The only genuinely missing piece was the *handshake* — telling the AI which
item is on screen and what the human believes is wrong with it. Two small
UI affordances added in the polish pass close that gap:

1. **Deep-linkable selection** — the URL always carries `#item/<id>`, so
   "the item I'm looking at" is one paste away.
2. **Copy AI context** (item header) — copies a self-contained markdown block:
   statement, chips, research location, sources with excerpts, both relation
   directions, dates, publication mappings, DB path + revision, and pointers
   to the JSON API and the transactional edit tooling. Pasting that into a
   Claude session plus one sentence of intent ("I believe this is actually two
   events — split it and re-ground both halves from the topic file") is a
   complete work order.

### Recommended operating pattern

1. In the editor, select the item; click **Copy AI context**.
2. Paste into a Claude Code session (Cowork or terminal) with the intent
   sentence. Include the staging-vs-live caveat if relevant — the DB path in
   the context block already disambiguates.
3. Claude re-grounds from `research_path` (in the context block), proposes the
   split/rewrite as an explicit op list, and on approval applies it via
   `editor.commit_change` / `author-batch` against the same DB.
4. Back in the editor: **Refresh**, review the changed items (revision history
   card shows `changed_by`), and **Undo last** anything wrong.

Convention worth adopting: AI-applied changes should pass a distinctive
`changed_by` (e.g. `claude-cowork`) so the revision-history card makes AI edits
visually auditable later.

### Do not build (rejected alternatives)

- **An AI chat panel inside the editor** — duplicates Claude Code poorly,
  needs API keys in a loopback tool, and bloats a deliberately small artifact.
- **Editor-side "AI revision queue" tables** — a second coordination store the
  §14 contract deliberately avoids; `review_state = needs_revision` plus the
  notes field already model "flagged for rework".
- **Browser-automation-driven editing** (AI clicking the UI) — strictly worse
  than the ops layer it would end up calling anyway.

## 2. Small enablers already in place (no work needed)

- `review_state` picklist includes `needs_revision` — usable today as the
  "flagged for AI rework" state; the filter panel can already list them.
- `notes` field on every item — the natural place to record the human's
  diagnosis ("comingles the 1641 fine with the 1645 grant") before handing off;
  it travels inside the Copy-AI-context block automatically.
- `GET /api/item/<id>` — an AI session on the same machine can re-read the
  live item state mid-conversation if the editor server is running.

## 3. Deferred improvements (major — future passes)

Listed in rough value order; none are blocking.

1. **Guided split/merge flows.** A "split item" action that pre-stages
   `supersede_item` + two `create_item` drafts with relations carried over,
   shown in one combined preview. Highest-value structural edit; today it is
   exactly the case delegated to an AI session, so build only if it turns out
   to be frequent *and* mechanical.
2. **Multi-op staged batches in the modal.** The preview/commit path is
   one op per confirm. Batching (stage several ops, one diff, one commit)
   would need a server/editor extension — out of scope for UI-only passes.
   `author-batch` already covers the scripted case.
3. **Neighborhood mini-graph view.** A small SVG pane showing the selected
   item's 1–2-hop relation neighborhood (the Gephi export covers deep analysis;
   this would be for quick orientation while editing).
4. **Review-queue guided decisions.** §14 mentions multiple-choice guided
   review (merge/split, alignment, confidence). The queue currently offers
   accept/reject; guided flows are worth designing once machine-suggested
   volume actually grows.
5. **Marker awareness.** Prose markers (Plan 2a) are not surfaced in the item
   detail; a read-only "markers referencing this item" card would tighten the
   prose↔graph loop.
6. **Saved filter sets / session restore.** Filters reset on reload; a
   localStorage-persisted filter state (and last tab) is cheap but was left out
   to keep this pass presentation-only.
