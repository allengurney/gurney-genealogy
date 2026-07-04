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
- `coverage/README.md` + the three ledgers (`legacy-companion-map.csv`,
  `dump-findings-map.csv`, `source-and-citation-map.csv`) and the checker
  `tools/g13_coverage_check.py` — you add rows to these every increment (step 9);
  the cutover gate is zero un-dispositioned items + zero untracked citation gaps.

## Non-destructive invariant (Plan 02)
Work only in `research/people/_staging/g13-john-gurney/`. Do **not** edit the live
companion `research/people/g13-john-gurney-fact-sheet.research.md`, the
`sources/intake/dump-files/`, or the public site. Reading them to assimilate is
expected; editing them is not (that happens only at an approved cutover).

## Workflow

1. **Ground before authoring (work the delta).** Establish what the repo already
   knows: `repo_search.py infile research/people/g13-john-gurney-fact-sheet.research.md --terms ...`
   for the topic, plus the relevant place/topic companions and the dump. Read the
   `manifest.json` to see which topics + item IDs already exist — never duplicate.
2. **Pick a bounded, well-sourced topic.** Prefer property/civic/record-coverage
   material over identity disambiguation (Cheny/Girny and same-person questions are
   "expensive and hard to reverse" — §18; leave them for a dedicated, reviewed pass).
3. **Verify every source is registered.** You may cite only `sourceId`s present in
   `data/sources.json` (FK-enforced). Pull exact `Source ID` + locator from the
   companion footnotes; confirm each exists in the `source_registry`. Register a
   genuinely new source in `data/sources.json` deliberately first (+ its
   `sources/validations/*.md` worksheet) — do not invent IDs.
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
   (all three backup tiers aligned; DB not ahead of recovery/snapshot).
9. **Add coverage-ledger rows (do not skip — this is how the cutover gate closes).**
   For each legacy companion block and each dump finding this topic assimilated, add a
   row to `coverage/legacy-companion-map.csv` / `coverage/dump-findings-map.csv` with
   its disposition, destination `topicId`, `G13-RI` ids, and source ids; add the unit's
   cited `sourceId`s to `coverage/source-and-citation-map.csv` (Plan 02 §7, §11
   checkpoint step 5). Then run `tools/g13_coverage_check.py` and confirm your rows land
   and no new citation gap appears.
10. **Update `manifest.json`** (new topic + its `researchItemIds`) and the staging
   `README.md`. Optionally show the increment through `context --terms <topic> --mode grounding`.

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

## See also
- `.claude/skills/online-discovery-strategy/SKILL.md` — if the increment needs new
  online discovery before authoring.
- Memory `g13-context-graph.md` — current phase status, live DB path, and open items.
