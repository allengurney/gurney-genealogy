# G13 John Gurney research refactor

Status: approved architecture direction; implementation not started.

This packet preserves the design decisions and reasoning from the July 2026
architecture discussion so implementation does not depend on the original chat
thread.

## Decisions

1. Build a lightweight SQLite context graph for G13. **The SQLite database is the
   canonical store for structured graph content** (research items, relations,
   evidence links, dates, negative-result scope, entities). Prose research and
   source metadata/artifacts remain canonical files. The DB is edited through the
   artifact and backed up via automatic recovery exports plus versioned
   milestone snapshots; there is no
   hand-authored JSON items layer. (Updated 2026-07-03 — supersedes the earlier
   derived/disposable-cache framing; see Plan 01 §1, §6.)
2. Refactor the oversized G13 research companion into a topic-structured
   research package and assimilate the current research dump.
3. Preserve the current companion and website implementation during
   development. Build the replacement in isolated staging paths, compare old
   and new, and cut over with an explicit switch.
4. Build the topic-structured website first without graph features.
5. Treat the graph-enhanced website as a later progressive enhancement. Its
   current concept is evidence markers in prose opening a finding drawer or
   mobile bottom sheet, backed entirely by static finding pages and JSON.
6. Allen expects Claude (Opus 4.8) to build a separate crisp artifact for viewing,
   navigating, and editing the graph. It is database-driven because it reads and
   writes the canonical SQLite directly — each validated save is a transactional
   DB write with an in-model revision entry, plus an automatic recovery export.
   No JSON import/export step.

## Plans

- [01-sqlite-context-graph-design.md](01-sqlite-context-graph-design.md) —
  complete design and implementation plan for the canonical SQLite graph,
  context compiler, validation, and graph-editing artifact contract.
- [02-g13-research-refactor-plan.md](02-g13-research-refactor-plan.md) —
  complete design and migration plan for restructuring the companion and
  assimilating the research dump without loss.
- [03-topic-structured-website-plan.md](03-topic-structured-website-plan.md) —
  complete design and implementation plan for publishing the refactored topic
  package without graph capabilities.
- [04-graph-enhanced-website-concept.md](04-graph-enhanced-website-concept.md) —
  concept stub for later finding drawers, static finding pages, and relationship
  navigation. This is deliberately not yet a full UI specification.

Supporting design material:

- [support/current-state-and-dump-inventory.md](support/current-state-and-dump-inventory.md)
- [support/research-item-model-and-use-cases.md](support/research-item-model-and-use-cases.md)
- [support/staging-cutover-and-rollback.md](support/staging-cutover-and-rollback.md)

## Non-destructive invariant

Until an explicit cutover is approved:

- Do not edit, rename, or delete
  `research/people/g13-john-gurney-fact-sheet.research.md`.
- Do not edit or delete the raw files under `sources/intake/dump-files/`.
- Do not point production tooling, indexes, or the public site at the staging
  graph database until cutover. (The staging DB is canonical for the *staged*
  graph only; the live G13 companion and site remain unchanged until then.)
- Do not change the current public G13 companion route.
- Do not make the site build consume staged content by default.
- Do not silently move findings between G13, G14, place, topic, case-file, or
  source layers.

The staged implementation may be retired without affecting the current
repository or website behavior, but the staged canonical DB is not disposable
cache: create a current recovery export before archival/removal.

## Recommended implementation order

1. Establish staging paths, manifests, identifiers, and coverage ledgers.
2. Inventory every current companion section and every dump finding.
3. Complete the plumbing-only contract and minimal database foundation using
   synthetic fixtures (Plan 01 G0/G1A). Do not assimilate research content yet.
4. After independent review, run the colonial-arrival **pilot slice** (Plan 01
   Phase P) as the first real-content touch and early go/no-go gate.
5. Complete the remaining database/context plumbing only if the pilot passes.
6. Refactor the research content into staged topic files, **co-authoring prose
   and research items per topic in one pass** (not two separate reads).
7. Build the non-graph topic-structured website preview.
8. Compare legacy and staged research for coverage, citations, and conclusions.
9. Approve and execute the content/site cutover.
10. Build the graph-editing artifact against the stable research-item contract.
11. Design and implement the graph-enhanced public website experience.

Ownership and the Codex → Opus review/test-drive checkpoints are specified in
Plan 01 §18. In brief: Codex builds the deterministic plumbing (each deliverable
followed by an Opus review + test drive); Opus 4.8 owns research synthesis and
the graph-editing artifact; Fable 5 handles frozen-spec mechanical passes.

## Success in one sentence

A new AI session, human researcher, or website visitor can identify what the
project currently believes about John Gurney, why it believes it, what conflicts
or remains open, and where the full evidence lives—without loading or reading
the entire G13 research ecosystem.
