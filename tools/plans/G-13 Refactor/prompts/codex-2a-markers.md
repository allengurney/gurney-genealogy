# Prompt — Codex: implement Plan 2a marker plumbing (M0, M1, M3)

Give this to Codex GPT-5. It is deterministic graph plumbing (§18 Codex lane).
It builds the marker *data* spine and static export; it does **not** author the
real Braintree markers (that is Opus M2) and does **not** build the editor UI (§9)
or reader JS (M4–M5), which are deferred to the Plan 03 site build.

```
Work in main. Implement Plan 2a marker plumbing, milestones M0, M1, and M3 only,
per tools/plans/G-13 Refactor/02a-narrative-graph-evidence-markers.md (revised
2026-07-04 — read the Revisions section first). Read also Plan 01 §6/§10/§11
(canonical-SQLite model, schema, deterministic export/restore), tools/g13_graph/
README.md (batch shape, LOGICAL_TABLE_ORDER, recovery/snapshot), and
tools/g13_graph/authoring.py.

This is plumbing. Do NOT author real research prose or the Braintree markers
(Opus owns M2), do NOT build the editor Narrative-Markers UI (§9) or reader
drawer JS (M4–M5), and do NOT touch the live companion, dump, or public site.

M0 — Contract and fixtures:
- Freeze marker vocabulary, the kind-neutral ID format (G13-PM-000001), and the
  DDL for prose_markers, prose_marker_items, marker_revisions (§3.2).
- Add synthetic marker fixtures (extend tests/fixtures) covering: a public marker,
  a repo_only marker, a multi-item marker (primary + expressed + contextual), and
  a contextual member that IS reachable by one relation hop (to exercise the new
  warning).

M1 — Canonical storage, validation, and batch authoring:
- Add the three tables as a reviewed migration to schema v3, with FKs to
  research_units and research_items, exactly-one-primary-per-active-marker
  enforced, transactional edits, and marker_revisions audit rows.
- Add them to LOGICAL_TABLE_ORDER so they round-trip through deterministic
  recovery export/snapshot/restore; add export/restore equivalence tests.
- Implement topic-scoped marker validation (§10), including: every active marker
  has exactly one primary; every mapped item exists and (primary/expressed)
  shares the marker's research unit unless a reviewed cross-unit reason is set;
  public markers map only to public items; the WARNING when a contextual member
  is reachable by one relation hop from the primary (Revision 2). Marker validation
  must be opt-in/no-op when a topic has no markers, and must not slow ordinary
  validate at G13 scale.
- Extend tools/g13_graph/authoring.py (author-batch) to accept "markers" and
  "marker_items" in a batch and load them transactionally with the rest — this is
  how Opus will author markers as each topic is written. Note: a marker's Markdown
  token is placed in prose by the author (Opus), not by this loader; the loader
  only writes the SQLite rows. Validation that "every SQLite marker has exactly one
  Markdown token in its unit" scans the unit file for the token id (existence, not
  text equality — no prose hashing).

M3 — Static export and fallback:
- Extend tools/g13_graph/website.py (G5) with markers.json and
  marker-bundles/<marker_id>.json, plus permanent fallback pages for public
  markers and findings (§8). Public-only, fail-closed: no restricted/repo_only ids,
  labels, counts, or relation endpoints; a public marker that cannot be fully
  emitted is reported, never partially published.
- Byte-deterministic output; keep the isolation from repo_search.

Test everything with the synthetic fixtures (unittest, matching test_website.py /
test_authoring.py style). Keep schema/migrations reversible. Leave a short note in
tools/g13_graph/README.md. Stop for Opus review before M2/site work; do not commit
unless asked.
```
