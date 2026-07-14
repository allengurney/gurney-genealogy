---
name: g13-graph-authoring
description: Author a bounded G13 research-topic increment (Plan 2 / Phase G3) — staged topic prose co-authored with kind-neutral research items in the canonical SQLite context graph. Use when asked to add or extend a G13 topic unit, load research items into the graph, or continue the John Gurney topic refactor. Covers grounding, source verification, the transactional author-batch load, validation, backup, and manifest discipline.
argument-hint: [topic to author, e.g. "colonial/weymouth-community" or "family/wives-marriages"]
disable-model-invocation: true
---

Reusable procedure for one **bounded** G13 topic increment: staged topic prose +
its research items in the canonical graph, authored together in one pass (Plan 01
§16 Phase G3; Plan 02 §11). Keep each run to **1–2 topic units** unless directed
otherwise — depth and correctness over breadth.

## CLI invocation — read this before running anything
Use the **PowerShell** tool, not Bash: the Bash tool silently mangles Windows
paths like `.\.venv\Scripts\python.exe` (git-bash strips the backslashes, giving
`..venvScriptspython.exe: command not found` without flagging it as an error).
The entry point is the **top-level wrapper** `tools\g13_graph.py` — a sibling of
the `tools\g13_graph\` package directory, not a file inside it. Running anything
inside the package directly (`tools\g13_graph\cli.py`, or a guessed
`tools\g13_graph\g13_graph.py`) fails: the former with
`ImportError: attempted relative import with no known parent package`, the
latter with `No such file or directory`. Example status check:
`.\.venv\Scripts\python.exe tools\g13_graph.py status`. Full command list in
`tools/g13_graph/README.md` §CLI.

## Read first
- `tools/g13_graph/README.md` — tool mechanics: the `author-batch` batch shape,
  `validate` / `status` / `export --snapshot` / `hash-sources`, and the
  publication-safety contract. **This skill owns the workflow; the README owns the commands.**
- `tools/plans/G-13 Refactor/01-sqlite-context-graph-design.md` §8 (item kinds,
  fields, dates, evidence links, negative-result scope), §10 (schema).
- `tools/plans/G-13 Refactor/02-g13-research-refactor-plan.md` §5 (single home per
  conclusion), §11 (research-item integration + the topic-level checkpoint).
- `tools/plans/G-13 Refactor/02a-narrative-graph-evidence-markers.md` — the
  passage→item marker contract (relevant once Plan 2a M1 is built; see "Markers" below).
- `.claude/rules/research-files.md` + `.claude/rules/citations.md` — the prose you
  stage is `research/people/**` content and must follow them (finding-first,
  every fact cited, every aligned source shown).
- `tools/plans/G-13 Refactor/02b-source-lossless-topic-assimilation.md` — the
  source-lossless contract (§2), the tiered checker (§8), and the revised
  authoring checkpoint (§9) this skill implements.
- `research/people/g13-john-gurney/coverage/README.md` + the **four**
  ledgers there (`legacy-companion-map.csv`, `dump-findings-map.csv`,
  `source-and-citation-map.csv`, `supplemental-surfaces-map.csv`) and the
  checker `tools/g13_coverage_check.py` — you add rows to these every increment
  (step 9); the cutover gate is zero un-dispositioned items, zero untracked
  citation gaps, and zero Plan 2b source-journey/parity gaps.

## Non-destructive invariant (Plan 02)
Work only in the promoted G13 topic tree `research/people/g13-john-gurney/` and
the canonical graph/coverage artifacts it names. Do **not** edit the legacy
companion `research/people/g13-john-gurney-fact-sheet.research.md`, the
`sources/intake/dump-files/`, or the public site. Reading them for context is
expected; editing them is not part of G13 topic authoring.

## Workflow

1. **Ground before authoring (work the delta).** Establish what the repo already
   knows: `repo_search.py infile research/people/g13-john-gurney-fact-sheet.research.md --terms ...`
   for the topic, plus the relevant place/topic companions and the dump. Read the
   `manifest.json` to see which topics + item IDs already exist — never duplicate.
   **Plan 2b §9: identify every input block routed to this topic across ALL
   source-bearing surfaces** — legacy companion, dumps, the published fact sheet,
   the case file, and the pre-existing G13 topic files (enumerated in Plan 2b
   §3.3) — and inventory each block's complete source set before designing items.
   A source may not vanish because it is derivative, duplicate, superseded,
   discovery-only, or attached to a publication surface (Plan 2b §2).
2. **Pick a bounded, well-sourced topic.** Prefer property/civic/record-coverage
   material over identity disambiguation (Cheny/Girny and same-person questions are
   "expensive and hard to reverse" — §18; leave them for a dedicated, reviewed pass).
3. **Verify every source is registered.** You may cite only `sourceId`s present in
   `data/sources.json` (FK-enforced). Pull exact `Source ID` + locator from the
   companion footnotes; confirm each exists in the `source_registry`. Register a
   genuinely new source in `data/sources.json` deliberately first (+ its
   `sources/validations/*.md` worksheet) — do not invent IDs.
   **Registry `notes` are a catalogue annotation, not an evidence surface** — 2–4
   sentences (soft target ≤500 chars; lint threshold 600) saying what the source is,
   why it is relevant, and what kinds of information it carries. Transcriptions,
   extracts, catalogue readings, negative-search results, and project-original
   identifications go in the topic prose/footnotes (or `sources/corpus_supplement/`);
   the validation worksheet records scope and where findings landed. A one-line
   finding may appear in `notes` only when the same finding is already carried in a
   research-plane file. After any registry edit, run
   `.\.venv\Scripts\python.exe tools\lint_source_notes.py` (expect PASS).
4. **Write the topic prose** in `topics/<group>/<nn>-<slug>.md`: finding-first lede,
   topical sections, footnotes local to the file, an HTML-comment header noting the
   `topicId` and the item-ID range. The H1 must slug-match the unit `heading_id`.
5. **Design the items** (kind-neutral `G13-RI-######`, continue the sequence):
   - Split by kind: `source_evidence` (one identifiable record each), `research_finding`
     (supported conclusion, usually sourced *via relations* from evidence, not directly),
     `analysis` (reasoning, not an advocated identity), `open_question`,
     `negative_result` (requires structured scope + limitations), etc.
   - **Confidence = band label only** (`high`/`moderate-high`/`moderate`/…); never a
     numeric value used as a probability.
   - Dates: keep the probable range inside the plausible range; pair every
     `chronology_key` with a `chronology_key_basis`.
   - Relations carry the argument (`SUPPORTS`/`DEPENDS_ON`/`QUALIFIES`/`SYNTHESIZES`/
     `CONTEXTUALIZES`/…); don't restate evidence as prose-only.
   - **Publication mappings must be truthful** — map an item to a fact-sheet/case-file
     path only after confirming that surface actually asserts it; `publication_path`
     must resolve.
6. **Build the batch JSON** (shape in the README) and **dry-run it**:
   `author-batch --file <batch.json> --dry-run` → confirm `can_commit: true` and read
   the diff. Fix any `blocking_errors` before committing.
7. **Commit the batch:** `author-batch --file <batch.json>` (one transaction; writes
   `item_revisions`; refreshes the recovery export).
8. **Baseline + snapshot + validate:** `hash-sources` (baseline newly-cited local
   sources), `export --snapshot` (milestone), `validate` (**expect 0 errors**), `status`
   (all three backup tiers aligned; DB not ahead of recovery/snapshot), and — if the
   increment registered or edited any source — tools\lint_source_notes.py (PASS).
9. **Add coverage-ledger rows (do not skip — this is how the cutover gate closes).**
   For each legacy companion block and each dump finding this topic assimilated, add a
   row to `coverage/legacy-companion-map.csv` / `coverage/dump-findings-map.csv` with
   its disposition, destination `topicId`, `G13-RI` ids, and **complete** source ids
   (semicolon-separated — the checker mechanically compares them against what the
   frozen block actually cites); for fact-sheet/case-file/existing-topic blocks in
   scope, add rows to `coverage/supplemental-surfaces-map.csv` with disposition,
   friction, and mapped items; add the unit's cited `sourceId`s to
   `coverage/source-and-citation-map.csv` (Plan 02 §7; Plan 2b §6, §9). A prose
   citation deliberately carried without an item link in this unit needs a
   `context_only`/`cross_unit` role on its citation-map row, or parity fails.
   Then run `tools/g13_coverage_check.py` and check the per-increment gates below.
10. **Update `manifest.json`** (new topic + its `researchItemIds`) and the promoted
    topic-tree `README.md`. Optionally show the increment through `context --terms <topic> --mode grounding`.

## Revising an already-committed increment (edits, not creation)

Review corrections — a missing source witness, a softened claim, a reworded
statement, a date/scope fix, a new cross-unit relation, marker maintenance — are a
**recurring** second workflow, distinct from creation. `author-batch` only
*creates* (it collides on an existing `item_id` and refuses); every edit to a live
item goes through the editor's `commit_change` ops. Do **not** hand-write a one-off
script each time — use the packaged runner.

1. **Scope the edit against the publication surfaces, not just the graph.** For each
   touched finding, list what the fact sheet / case file / companion footnotes
   actually cite and confirm the item's **direct** `item_sources` carry every one of
   those witnesses. A finding "sourced via relations" can silently omit a witness the
   published surface names, and `g13_coverage_check.py` will **not** catch it — it
   only checks each `sourceId` journeys *somewhere* in the unit, not per-finding
   completeness. (This is the class of miss that a review pass usually surfaces.)
2. **Look up current values first** — `item <id>`, or read `item_sources` for the
   `item_source_id` that `update_source_link`/`remove_source_link` need. There is
   **no dry-run** for editor ops, so a wrong id fails mid-run.
3. **Write an ops JSON** (a list of `{op, params}`) and apply it:
   `.\.venv\Scripts\python.exe .claude/skills/g13-graph-authoring/apply-graph-edits.py <ops.json> [--changed-by claude-...]`.
   Common ops: `update_item` (`params.changes` = field→value over
   `ALLOWED_ITEM_FIELDS`, incl. `statement`, `assessment_confidence_label`);
   `add_source_link` / `update_source_link` (needs `item_source_id`) /
   `remove_source_link`; `set_dates`; `set_negative_scope` (**`limitations` is a real
   JSON list here** — the runner encodes it; unlike `author-batch`, where
   `limitations_json` must be a pre-encoded string); `add_relation` /
   `update_relation` / `remove_relation`; `add_publication` / `remove_publication`;
   marker ops `create_marker` / `update_marker` / `set_marker_primary` /
   `add_marker_item` / `update_marker_item` / `remove_marker_item`. Full param shapes
   live in `tools/g13_graph/editor.py` (`_op_*`) and `tools/g13_graph_editor/README.md`.
4. **Each op is its own transaction** — this is *not* atomic like `author-batch`. If
   op N fails, ops 1..N-1 are already committed and the revision has advanced; order
   ops so an earlier one can't strand a later one. `add_source_link` without a
   `locator` raises a non-blocking `source_locator_missing` warning on
   `source_evidence` items — pass `locator` in the same op.
5. **Reconcile the paired `.md` file and the ledgers in the same pass.** The graph and
   the topic prose are two representations of one edit: mirror every source
   add/removal, statement change, and reordering into the topic `.md` footnotes/prose,
   and update the affected `source-and-citation-map.csv` rows (findings_supported)
   and, if scope/disposition changed, the other ledgers / `manifest.json` /
   `README.md`. Reordering prose sections does not change the graph, but the marker
   tokens move with their sections (still exactly one token per active marker).
6. **Close out** exactly as for creation: `hash-sources` (only if new local sources
   were cited), `export --snapshot`, `validate` (**0/0**), `status` (tiers aligned),
   then re-run `g13_coverage_check.py` and confirm the per-increment gates still hold.

*(Tooling note: the ideal permanent fix is a first-class `g13_graph.py edit --file`
CLI with a `--dry-run` preview, mirroring `author-batch` — that is Codex plumbing
(§18). Until it lands, `apply-graph-edits.py` is the supported path.)*

## Markers (Plan 2a M1 is live as of 2026-07-03)

Author markers **as you write each topic**, in the same pass — not as a later
backfill. Marker storage plus the `author-batch` `markers`/`marker_items` extension
have landed (migration `0003_prose_markers.sql`), so markers are **in scope for
every increment**:
- Identify **3–8 conceptual evidence clusters** per topic (Plan 2a §4) — a cluster
  earns a marker only where the graph adds synthesis, analysis, qualification,
  conflict, negative evidence, or a useful pivot; not after every sentence.
- Place an invisible token `<!-- graph-marker: G13-PM-###### -->` at the **end** of
  each cluster's prose (after its footnote refs, before the paragraph break). The
  token carries only the marker ID — never a hand-maintained item list.
- Add `markers` + `marker_items` to the same `author-batch` payload: one **primary**
  item per marker, plus `expressed`/`contextual` members. Use `contextual` only when
  a relation hop can't already surface the item (the validator warns otherwise).
- **Retire the item-range HTML comment** in the topic header once markers exist —
  keep only the `topicId` and a one-line note. Markers are now the passage→item map.
- Markers default to `repo_only`; a public marker needs an explicit visibility
  decision and all its primary/expressed items must be public (fail-closed).

## Guardrails / lessons
- **Never write evidence into `data/sources.json` `notes`.** The 2026-07 remediation
  (plan 02c) relocated campaign findings that had accreted there. The registry note
  states relevance and content-type only; `tools/lint_source_notes.py` enforces the
  cap. If you are writing dates, quoted text, or reasoning into `notes`, stop — it
  belongs in the topic file.
- **Dry-run every batch first** — it is the cheap check that catches bad dates,
  unregistered sources, dangling FKs, and unresolved research locations before they
  touch the canonical DB.
- The pre-commit validator treats derived-index/recovery staleness as non-blocking;
  only content errors block (the `author-batch` path already handles this).
- One conclusion has exactly one canonical home (Plan 02 §5); other surfaces cite or
  summarize it. The graph item holds a compact statement; the topic file holds the
  full evidence.
- If the gate question ("is this materially smaller and as complete as loading the
  companion for the same task?") fails for the topic, stop and report rather than
  padding the graph.
- **One `from_item` may carry several relations in a batch — this is supported.**
  `item_revisions` still has a UNIQUE key on `(database_revision, item_id, change_kind)`,
  and each `add_relation` writes one `update` intent for its `from_item`, so two
  relations sharing a `from_item` produce two `update` intents for the same item. Those
  intents are now *coalesced* into a single audit row (earliest `before`, latest `after`,
  merged summary) in both `author-batch` and `--dry-run`, so a topic whose one evidence
  item SUPPORTS several findings commits cleanly. `--dry-run` mirrors the write exactly:
  its `would_write_revisions` and diff reflect the coalesced rows, and it surfaces an
  `item_revision_collision` blocking error if any residual collision ever escapes
  coalescing — so dry-run and commit can no longer disagree. No need to flip edges or
  split the batch anymore.
- **Write the topic `.md` file — with its `graph-marker` tokens — before the batch.**
  Marker validation reads the unit file and requires exactly one Markdown token per
  active marker (a blocking `marker_token_count_invalid` error otherwise). Author the
  prose first, then the batch that registers the markers.
- **`negative_result` items need a structured `negative_result_scope` per item.** Add a
  `negative_result_scope` object to the item wrapper (sibling of `item`/`sources`) or the
  dry-run blocks with `negative_result_scope_missing`. Columns: `provider`,
  `collection_name`, `date_start?`, `date_end?`, `query_description`, `results_reviewed?`,
  `coverage_confirmed` (0/1), and `limitations_json` (non-empty array). The stager inserts
  the dict verbatim, so **`limitations_json` must be a pre-encoded JSON *string*, not a JSON
  array** — a Python list fails at commit with `Error binding parameter 8: type 'list' is
  not supported`. The item `statement` may summarize the scope but does not substitute for
  the structured object.
- **Controlled vocabularies live in schema CHECK constraints, not just `constants.py`.**
  `bearing` ∈ {`direct`,`indirect`,`contextual`,`methodological`}; `strength` is free-ish
  (`strong`/`moderate`/…); `SOURCE_ROLES`, `RELATION_TYPES`, `ITEM_KINDS`, marker roles
  are in `constants.py`; confidence is a band label (`high`/`moderate-high`/`moderate`/…),
  never numeric. `--dry-run` catches a bad enum, but check these first to avoid a retry.
- **Reuse existing entities; don't recreate them.** Query `entities` first — the John
  Gurney subject and the common place rows (e.g. `place-weymouth-massachusetts-usa`)
  already exist, and re-creating one collides. Add an `entities` row only for a genuinely
  new place/person.
- **Leads: update through `research_leads.py`; never hand-edit.** An increment may
  resolve or advance a lead, or give it a promoted G13 topic home. Run `--dry-run`
  first, then use `update` or `close`; keep `Status` to a standard value such as
  `Open` or `Partial`, put the current promoted topic path in `Source ref` when it
  is the lead's home, and keep any status note short. Never rewrite the CSV with an
  ad-hoc script. Keep the `L-###` discovery trail in the relevant topic footnote or
  HTML comment.
- **Coverage checker is whole-refactor and now a passing gate.** Run
  `g13_coverage_check.py` against `research/people/g13-john-gurney/coverage/`.
  After promotion, every reported gating failure is actionable. Per increment
  (Plan 2b §8.6), confirm:
  **0 citation gaps**, **0 unregistered**, **0 inventory** problems, and — for the
  topics you touched — **0 `input_source_set_gaps`**, **0 `source_journey_gaps`**,
  **0 `topic_graph_source_gaps`**, **0 `publication_mapping_gaps`**, no new
  `friction_needs_decision`, and no backlog increase. A topic is `source-lossless`
  when every input routed to it passes; record the current status as `coverageStatus`
  on its `manifest.json` entry. Multi-destination legacy rows that are only partly
  assimilated stay backlog — annotate the sub-part in `notes` rather than
  false-closing the row.

## See also
- `.claude/skills/online-discovery-strategy/SKILL.md` — if the increment needs new
  online discovery before authoring.
- Memory `g13-context-graph.md` — current phase status, live DB path, and open items.
