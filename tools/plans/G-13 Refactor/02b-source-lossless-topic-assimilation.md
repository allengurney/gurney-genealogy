# Plan 2b — Source-lossless topic assimilation and completed-work remediation

Status: proposed supplement to Plan 02, 2026-07-04. Revised r2 the same day
after independent review (see §14 revision notes); the §4.2 audit claims were
re-verified against snapshot r15 before acceptance.

This plan supplements
[Plan 02](02-g13-research-refactor-plan.md). It does not replace Plan 02's
topic structure, single-home rule, staging boundary, or cutover process.
[Plan 2a](02a-narrative-graph-evidence-markers.md) still governs the
prose-marker bridge.

Plan 2b closes a losslessness gap discovered after the first five colonial
topics were authored. Plan 02 correctly requires preservation of every citation
and source relationship, but the implemented coverage workflow currently proves
only that sources which survived into a staged topic are listed in that topic's
source ledger. It does not yet prove that every source relationship in the
input research ecosystem made the journey.

The governing priority is:

> **Maintaining source linkage is the most important requirement of the G13
> refactor. No source may disappear because it is repetitive, derivative,
> superseded, lower-weight, or attached to a publication surface rather than the
> legacy companion.**

## 1. Problem statement

The G13 refactor changes the working-research architecture from one oversized
companion into a topic-based package backed by a context graph. That change
creates a new completeness obligation.

The legacy companion was historically the pre-publication working layer. The
published fact sheet and the user-directed case file contain selected,
promoted, curated, and cited conclusions that may no longer be fully represented
in the current companion. Existing G13 topic files likewise contain developed
research that overlaps or extends the companion. The research dumps preserve
still more findings, source pulls, negatives, corrections, and discovery trails.

If topic files are built only from the companion and then checked only against
their own new citations, the resulting package can be internally consistent but
incomplete. A source can vanish before the checker ever sees it.

This is not merely a bibliography problem. Losing a source relationship means
losing information such as:

- Another compiler independently or derivatively reached the same conclusion.
- A later source repeated, refined, contradicted, or omitted an earlier claim.
- A discovery/index source explains how a primary record was found.
- Two editions or transcriptions preserve materially different readings.
- A source was reviewed and rejected for a particular proposition, preventing
  future researchers from repeating the same work.
- A published "gold" statement rests on a source stack not fully reproduced in
  the working companion.

The graph's usefulness depends on preserving these distinctions rather than
silently retaining only the strongest representative source.

## 2. Non-negotiable source contract

For every substantive claim, finding, analysis, conflict, negative result, open
question, or published project statement brought into the G13 package:

1. Preserve every known aligned source.
2. Preserve the exact locator when available.
3. Preserve whether the source directly states the matter, repeats another
   source, independently corroborates it, qualifies it, contradicts it, merely
   mentions it, supplies discovery provenance, or has been superseded.
4. Preserve same-record representations separately when they are separately
   useful: manuscript image, printed transcription, abstract, index, later
   compilation, and project transcription are not interchangeable.
5. Do not inflate evidentiary weight. Three sources derived from one deed remain
   three tracked witnesses or representations, but not three independent primary
   events.
6. Do not drop a source because a better source was later found. Retain the
   earlier source with the correct role.
7. A source is not preserved merely because its `sourceId` exists in
   `data/sources.json` or the graph's `source_registry`. It must remain linked to
   the relevant claim, item, evidence group, publication statement, or explicit
   disposition.
8. A completed topic must be understandable and source-complete without loading
   the fact sheet, case file, legacy companion, old G13 topic files, or dumps.

The last rule does not require visible prose to narrate discovery chronology or
repeat every source title in the body. Sources normally remain compactly visible
in footnotes, while graph roles and alignment notes carry the structured
distinctions.

## 3. How the fact sheet and case file participate

### 3.1 Fact sheet

The G13 fact sheet remains an independent published narrative. It is **not**
being collapsed into the topic package, rewritten as a set of topic files, or
treated as disposable after cutover.

It nevertheless must be inventoried as a source-bearing input to the refactor.
The fact sheet contains promoted "gold" findings and the source stacks selected
to support them. Because the new topic package replaces the old research
companion as the complete working-research layer, each promoted fact-sheet
finding must have a whole research home in a topic, including all known aligned
sources. Otherwise the topic package behaves like a lab notebook — a record of
selected work in progress — rather than the complete research foundation beneath
the published fact sheet.

The topic may contain a fuller or more qualified treatment than the fact sheet.
The fact sheet remains concise and unchanged unless a separate publication edit
is approved. The graph's publication mapping records which research finding the
fact sheet expresses.

### 3.2 Case file

The John Gurney case file also remains an independent, user-directed,
self-contained publication artifact. It is **not** being revised, dissolved, or
collapsed into the topic package under this plan.

The case file contains curated and vetted facts, source comparisons, negative
results, candidate eliminations, and argument-bearing source relationships. When
a case-file fact falls within a G13 topic's scope, the topic must incorporate the
substantive research and its complete aligned source set so that the topic is
whole. The case file may retain its polished argument and narrative organization;
the topic carries the canonical subject research needed outside that
publication-specific argument.

Case-file material that is genuinely argument-specific may remain
`external-canonical`, but that is an explicit disposition, not an omission.

### 3.3 Existing G13 topic files

The seven pre-existing G13/John topic files are also source-bearing inputs.
**Enumerate them explicitly — do not glob.** The pattern
`research/topics/g13-john-gurney-*.md` matches exactly **one** file; Plan 02
§2's "Seven G13/John topic files (~24,269 words)" are:

1. `research/topics/g13-john-gurney-immigration-by-association.md`
2. `research/topics/john-gurney-candidate-aylesbury-buckinghamshire.md`
3. `research/topics/john-gurney-candidate-berkhamsted-hertfordshire.md`
4. `research/topics/john-gurney-candidate-ackworth-yorkshire.md`
5. `research/topics/john-gurney-candidate-earsham-norfolk.md`
6. `research/topics/john-gurney-candidate-london-draper.md`
7. `research/topics/john-gurney-candidate-others.md`

A glob-driven freeze would have silently dropped six inputs — exactly the
failure class this plan exists to prevent. Thread 2 must freeze this explicit
list, sanity-check it against Plan 02 §2's word count, and scan
`research/topics/README.md` for any other file whose subject is G13 John
Gurney (e.g. the Bevis/Diligent/Mary-Anne passenger-list topic is a
*method/collection* topic, not a G13 subject file — include it only if review
shows it carries G13-specific source relationships not held elsewhere). They may be subdivided, retained as cross-cutting topics,
or absorbed into subject-owned G13 units, but every substantive claim and source
relationship requires a disposition.

## 4. Observations from the first five topics

The live graph at database revision 15 is structurally valid, but the
source-losslessness audit found gaps that structural validation does not detect.

### 4.1 Output-to-output checks are mostly healthy

For the five staged topics, prose source IDs, the
`source-and-citation-map.csv`, and graph source links generally agree. One known
exception is the frontier topic's Nash citation for the 1651/2 Weymouth great
lot: the prose and citation ledger carry
`nash-historical-sketch-weymouth-1885`, but no frontier item links that source.

This proves the need for topic-to-graph source parity validation.

### 4.2 Input-to-output checks are incomplete

Confirmed examples include:

- `sprague-braintree` supports John's occupation in both the fact sheet and case
  file but is registered without any graph item linkage.
- The full Suffolk Deeds Liber V registry copy confirms "John Gurney of Braintry
  Taylor" and is cited through `familysearch-fulltext-search` in the companion
  and case file, but it did not reach the Braintree topic or
  `G13-RI-000013`.
- `anderson-gmd-2015` identifies the 1641 Massachusetts record and carries a
  published arrival/settlement assessment, but it did not reach the arrival
  graph.
- `suffolk-probate-index-v2-1895` preserves the probate discovery/index trail
  but did not reach the material-life graph.
- The legacy row for "Further primary records surfaced by the full-text
  campaign" omits `familysearch-fulltext-search` from its recorded source set
  even though the underlying block cites it.

These examples are sufficient to show a process defect. They are not assumed to
be the complete gap list.

### 4.3 The dump ledger is preserving backlog, but completed topics are bounded

The dump map still correctly flags relevant unassimilated material, including:

- The imaged 1646 Braintree meadows petition.
- The Brackett brothers' Suffolk-origin association.
- The Hingham/arrival-vector negative.
- Record-coverage findings and negatives.

The first five topics should therefore be described as completed increments,
not fully closed topics, until Plan 2b remediation reconciles all frozen inputs.

### 4.4 Review and validation language currently overstates proof

"Zero citation gaps" currently means:

> Every source cited by a staged topic appears in the staged source ledger.

It does **not** mean:

> Every source attached to the topic in every input surface appears in the
> staged topic and graph.

Plan 2b reserves **source-lossless** and **topic-complete** for the second,
stronger condition.

## 5. KISS coverage design

A fully normalized, manually maintained row for every individual
claim-to-source witness would be precise but expensive, particularly midstream.
Plan 2b does not adopt that as the default.

Instead, use **block-level source-set reconciliation**:

- Existing input ledgers remain block/finding oriented.
- Each input row carries the complete set of aligned `sourceId`s for that block.
- SQLite remains canonical for exact item-to-source relationships.
- The checker compares the input source set with the destination topic and
  graph source sets.
- Human effort is spent only on routing, role distinctions, and genuine
  friction — not retyping one CSV row per source.

Escalate to a per-source exception row only when one source in a block has a
different destination or disposition that cannot be represented clearly in the
block's notes.

## 6. Coverage artifacts

### 6.1 Keep the three existing ledgers

Continue using:

- `legacy-companion-map.csv`
- `dump-findings-map.csv`
- `source-and-citation-map.csv`

Strengthen them as follows:

- Mechanically verify that each legacy row's `source_ids` equals the source IDs
  actually cited by its frozen block, including resolved footnote definitions.
- Add a `source_ids` column to the dump map so a dump finding cannot be
  dispositioned without its source set.
- Keep `source-and-citation-map.csv` as the destination-side list of sources
  cited by each staged unit.

### 6.2 Add one supplemental-surface map

Add:

```text
coverage/supplemental-surfaces-map.csv
```

It covers the fact sheet, case file, and seven existing G13 topic files. Use one
row per independently meaningful assertion or block, not one row per source.

Proposed columns:

```text
origin_path
origin_kind
origin_anchor
content_hash
destination_topic
disposition
research_item_ids
source_ids
friction
notes
```

`origin_kind`:

- `fact_sheet`
- `case_file`
- `existing_topic`

`disposition`:

- `incorporated`
- `summarized`
- `publication_only`
- `external_canonical`
- `superseded_but_preserved`
- `duplicate_but_preserved`
- `routed_elsewhere`
- `needs_decision`

**Separator normalization:** the legacy map already mixes hyphens and
underscores (`external-canonical` beside `retained_in_hub`). New ledgers use
underscores; the checker normalizes `-`/`_` when matching disposition values
so the historical rows do not need a rewrite.

`friction` is empty or a semicolon-separated controlled set:

- `claim_conflict`
- `confidence_mismatch`
- `source_alignment_unclear`
- `source_id_missing`
- `source_id_collision`
- `same_record_multiple_representations`
- `topic_boundary`
- `publication_wording`
- `graph_model_gap`
- `needs_source_pull`

The map does not authorize edits to any origin surface. It records how its
research and sources are represented in the new package.

### 6.3 Freeze the expanded input inventory

Add content hashes and inventory metadata for:

- `fact-sheets/g13-john-gurney-fact-sheet.md`
- `research/case-files/john-gurney-case-file-v4.md`
- The seven pre-existing G13 topic files **as enumerated in §3.3** (not a glob).

Preserve the existing cutoff inventory for the companion and dumps. Record a
separate Plan 2b cutoff for the added surfaces rather than pretending they were
part of the original freeze.

## 7. Source relationship modeling

Use the existing graph model before adding schema.

### Same underlying record, multiple representations

Link each useful representation to the same `source_evidence` item when they
express the same historical record:

- Manuscript image.
- Project transcription.
- Printed registry transcription.
- Abstract.
- Later quotation.

Use `role`, `verification_level`, and `alignment_note` to explain the
relationship and any difference in wording or completeness.

### External compiler or publication conclusion

Use `published_source_statement` when the fact that a compiler reached or
published a conclusion is itself worth retrieving. Connect it to the project
finding with the appropriate explained relation. This is the natural treatment
for sources such as Sprague when they preserve a compiled conclusion rather
than a distinct underlying event.

### Discovery/index source

Keep indexes, catalog entries, search systems, and discovery publications using
`discovery_only`, `mentions`, or `context_for` as appropriate. Finding the
primary record does not erase how it was found.

### Contradiction, qualification, and supersession

Retain both sides. Use source roles and research-item relations to expose the
conflict or later correction. Do not make an older source disappear merely
because the project no longer adopts it.

### Schema escalation rule

Do not add new source-derivation tables in the initial remediation. First use
the existing item kinds, source roles, alignment notes, and relations. Propose a
schema change only if the remediation demonstrates a repeated relationship that
cannot be represented without ambiguity.

## 8. Checker and validation changes

Extend `tools/g13_coverage_check.py` or add a narrowly focused helper invoked by
it. The final command surface should remain one coverage check.

### 8.0 Where the checker reads graph truth

The journey (§8.3) and parity (§8.4) checks need item→source links, which live
in the canonical SQLite DB outside the repo. The checker stays repo-only and
deterministic by reading the **newest tracked recovery snapshot**
(`data/context-graphs/g13/exports/snapshots/g13-context-*.ndjson`, highest
revision; `research_items.research_unit_id` + `item_sources` +
`item_publications`), overridable via `--graph-export`. Snapshot freshness is
procedural, not checked: the authoring checkpoint (§9 step 8) always snapshots
before the coverage check runs. If journey/parity checks are needed and no
snapshot exists, that is a gating `graph_export_missing` problem, not a silent
skip.

### 8.1 Frozen-input integrity

Verify mechanically:

- Every inventoried path exists.
- Content hashes match the appropriate cutoff.
- Every frozen input has at least one ledger row.

"Every independently meaningful block/assertion has a ledger row" is a
**human-review obligation**, not a mechanical check — the checker cannot judge
meaningfulness. Thread 2's block-boundary review carries it; the checker only
proves per-file enumeration and hash integrity.

### 8.2 Input source-set integrity

For each **dispositioned** input row (un-dispositioned rows are backlog, not
source-set gaps — otherwise adding the dump `source_ids` column instantly
manufactures 82 spurious failures):

1. Parse source IDs from the frozen block and its referenced footnote
   definitions.
2. Compare the parsed set with the row's `source_ids`.
3. Report missing, extra, malformed, and unregistered IDs.

HTML case-file/fact-sheet citations using `Source ID: <code>source-id</code>`
must be supported alongside Markdown backticks. (Verified: both publication
surfaces use the HTML form exclusively; bare `<code>` tags also carry
non-source content, so the extractor must anchor on the `Source ID:` label.)

**Block anchoring is tiered, and the tier is reported:**

- *Legacy rows* — derive each block span from `line_start_at_inventory` to the
  next row's start (last row → EOF) and verify the derived span reproduces the
  row's 16-hex `content_hash` prefix. A verified span gates; an unverified
  span (38/41 verify today; the 3 split sub-blocks do not) is extracted
  best-effort and reported as a non-gating `block_span_unverified` note whose
  source set is trusted from the ledger.
- *Dump rows* — anchor on the finding heading (`### F<id> — …`); the
  `finding_id` opens the heading text in every frozen dump. An unanchorable
  row is a non-gating `extraction_unanchored` note; its `source_ids` are
  trusted from the ledger and still journey-checked.
- *Supplemental rows* — anchor on `origin_anchor` (a heading line in the
  origin file); same unanchored fallback.

### 8.3 Source-journey integrity

For each dispositioned input row, verify that every input `sourceId` is:

- Linked to at least one mapped research item or evidence group in the
  destination topic; or
- Explicitly preserved through a reviewed disposition explaining why it remains
  publication-only, external-canonical, superseded, duplicate, or routed
  elsewhere.

Presence elsewhere in the graph is insufficient unless the row explicitly
routes there.

### 8.4 Topic-prose ↔ graph parity

For each staged topic:

- Every source cited in prose must link to an item/evidence group in that unit
  or carry an explicit reviewed cross-unit/context-only reason.
- Every source linked to an item in that unit must appear in the topic's
  citations or carry an explicit reviewed reason.
- Every source in `source-and-citation-map.csv` must agree with both sides.

### 8.5 Publication alignment

For every fact-sheet or case-file project statement within an authored topic:

- Map the assertion to the research finding(s) it expresses.
- Preserve the publication's aligned source set.
- Record any difference in confidence, wording, or scope as friction.

The **mechanical** projection of this (what the checker actually gates): a
supplemental row with `origin_kind` `fact_sheet`/`case_file` and disposition
`incorporated`/`summarized` must carry at least one `research_item_ids` value
that exists in the graph export, and its `source_ids` must pass §8.3. Whether
the mapped finding truly *expresses* the assertion remains human review;
cross-checking against the graph's `item_publications` rows is a warning-level
aid, not a gate.

### 8.6 Result vocabulary

Report separately:

- `input_inventory_gaps`
- `input_source_set_gaps`
- `source_journey_gaps`
- `topic_graph_source_gaps`
- `publication_mapping_gaps`
- `friction_needs_decision`
- `graph_export_missing` (gating when journey/parity checks are required)

Do not report `SOURCE-LOSSLESS: PASS` until every category is zero. Mid-refactor
backlog remains expected and should be stated plainly.

**Per-increment vs cutover gating.** The whole-refactor `RESULT` stays FAIL
until every topic lands — that is expected. The per-increment discipline
(skill Guardrails) reads specific categories: after an increment or a
remediation transaction, `input_source_set_gaps`, `source_journey_gaps`,
`topic_graph_source_gaps`, and `publication_mapping_gaps` must be zero **for
the topics touched**, backlog must not increase, and journey checks whose
destination topic is not yet staged are reported as deferred, not failed.

## 9. Revised topic-authoring checkpoint

Before authoring:

1. Identify every input block/assertion routed to the topic across the companion,
   dumps, fact sheet, case file, and existing G13 topics.
2. Read each input block once and inventory its complete source set.
3. Resolve or record source-registration and alignment friction.
4. Design the topic findings and source-evidence items.

During authoring:

5. Write complete topic prose with every aligned source shown.
6. Author graph items, source links, relations, and markers in the same pass.
7. Preserve derivative, duplicate, discovery, superseded, and conflicting
   sources with truthful roles.

At checkpoint:

8. Run the author-batch dry run, commit, source baselines, snapshot, graph
   validation, and status checks.
9. Update all applicable input ledgers and the destination citation map.
10. Run the expanded coverage checker.
11. Review every friction flag.
12. Call the topic `increment-complete` if only broader-refactor backlog remains;
    call it `source-lossless` only when every input routed to that topic passes.
    Record the status as a `coverageStatus` field on the topic's entry in the
    staging `manifest.json` so Thread 6 and the cutover gate read it from one
    place instead of thread handoffs.

## 10. Remediation of work completed to date

Do not discard or rebuild the graph. Remediate incrementally through reviewed
transactions, preserving existing IDs wherever the item identity remains sound.

### R0 — Freeze and diagnose

- Record revision 15 as the pre-Plan-2b audit baseline.
- Confirm current recovery and milestone snapshot health.
- Generate a machine-readable diagnostic of:
  - Topic prose sources.
  - Graph item sources.
  - Current source-and-citation rows.
  - Input-ledger source sets.
- Make no content changes in this step.

### R1 — Coverage plumbing

- Add the supplemental-surface inventory/map.
- Add dump `source_ids`.
- Implement source-set extraction and the new checker categories.
- Add synthetic fixtures for:
  - Markdown footnote source IDs.
  - HTML `<code>` source IDs.
  - Same-record multiple representations.
  - A derivative compiler source.
  - A discovery-only source.
  - A source lost between input and graph.
- Update the G13 authoring skill with the revised checkpoint.
- Do not remediate live research content in this step.

### R2 — Inventory fact sheet, case file, and existing topics

- Freeze the added surfaces at a Plan 2b cutoff.
- Populate the supplemental map mechanically first.
- Human-review block boundaries, topic routing, complete source sets, and
  friction.
- Do not edit the fact sheet, case file, or existing topic files.
- End with a report of source-journey gaps by destination topic.

### R3 — Remediate the first five topics

Work one bounded transaction/topic group at a time.

#### Arrival chronology

- Reconcile fact-sheet and case-file arrival statements and sources.
- Preserve Anderson's published assessment and its cited-record relationship.
- Reconcile Hingham/arrival-vector dump findings with either arrival or
  record-coverage.
- Backfill prose markers because the Phase P topic predates Plan 2a markers.
- Revisit the plausible/probable arrival envelope separately from source
  preservation.

#### Weymouth community

- Reconcile fact-sheet, case-file, existing-topic, and dump source stacks for
  inhabitant standing, associates, Jenner, and military negatives.
- Route the Jenner/Venn and reception-network findings to their correct topic
  homes without dropping their Weymouth bearing.
- Confirm every source representation is linked, not merely present in the
  registry.

#### Braintree community

- Carry Sprague's compiled occupation and Braintree statements with truthful
  published-source roles.
- Carry the full Liber V deed representation and retain Bates and the other
  printed/deed witnesses.
- Assimilate the 1646 Braintree meadows petition separately from the 1645
  petition.
- Reconcile the Brackett association material.
- Correct any compound source-evidence items where several distinct witnesses
  have been blended.

#### Frontier rights

- Link the cited Nash great-lot source to the relevant frontier analysis or
  create the missing evidence dependency.
- Reconcile all Billerica, Mendon, Quinapaug, probate-index, and discovery
  sources across surfaces.
- Preserve the distinction between John's rights and the posthumous
  widow/descendant stream.

#### Material life and occupation

- Create or identify the canonical occupation finding.
- Connect the direct deed evidence, Sprague's published statement, the inventory
  negative, and the husbandry finding without treating derivative sources as
  independent primary evidence.
- Carry the probate index/discovery trail.
- Capture the debt/net-estate conclusion if it remains in prose.
- Correct the "single most valuable possession" wording separately from the
  source-lossless repair.

### R4 — Cross-topic and publication audit

- Re-run the expanded checker over all five topics.
- Review source roles and cross-topic dependencies.
- Confirm every fact-sheet/case-file assertion in scope has a publication
  mapping or explicit disposition.
- Confirm no origin surface was modified.
- Produce a concise remediation report listing:
  - Added source links/items.
  - Preserved derivative/discovery sources.
  - Remaining friction.
  - Remaining topic backlog.

### R5 — Resume normal G3 authoring

Only after R4:

- Use the revised Plan 2b checkpoint for every new topic.
- Do not defer supplemental-surface reconciliation to cutover.
- Keep the global cutover gate at zero undispositioned input blocks/findings,
  zero source-journey gaps, zero topic/graph source gaps, and zero unresolved
  blocking friction.

## 11. Friction posture

Friction is expected when a publication surface and working research disagree.
Do not silently choose one.

Record:

- Exact conflicting wording.
- Each source stack.
- Which surface currently carries which confidence.
- Whether the difference is deliberate publication compression, stale content,
  or a true evidentiary conflict.
- The proposed canonical topic treatment.
- Whether publication revision is recommended later.

Plan 2b does not authorize fact-sheet or case-file revision. It produces the
evidence needed for a later publication decision.

## 12. Acceptance criteria

Plan 2b remediation succeeds when:

- Fact sheet, case file, legacy companion, dumps, and existing G13 topics are all
  in the frozen coverage denominator.
- Every meaningful input block/assertion has a disposition.
- Every input source set is mechanically verified.
- Every source has reached the correct topic/graph item or has an explicit
  preserved disposition.
- Duplicate and derivative sources remain visible without being misrepresented
  as independent primary evidence.
- Every topic's prose, graph links, and citation map agree.
- Fact-sheet and case-file project statements map to whole research findings.
- The fact sheet and case file remain unchanged.
- Friction is visible and reviewable.
- The five existing topics pass the new source-lossless checkpoint.
- The workflow adds only one supplemental map rather than a manually normalized
  source-witness ledger.

## 13. Thread sequence and initial prompts

These are separate threads but not fully parallel work. Threads 1 and 2 are
prerequisites. Topic-remediation threads write the same canonical SQLite
database and should run sequentially to avoid ID and revision conflicts.

### Thread 1 — Implement Plan 2b coverage plumbing

```text
Work in the current gurney-genealogy checkout. This is Plan 2b Thread 1:
coverage plumbing only.

Read first:
- AGENTS.md and README.md
- tools/plans/G-13 Refactor/02b-source-lossless-topic-assimilation.md
- Plan 02 sections 7, 10, 11, 14, and 15
- research/people/_staging/g13-john-gurney/coverage/README.md
- .claude/skills/g13-graph-authoring/SKILL.md
- tools/g13_coverage_check.py

Implement R1 only:
- Add the supplemental-surface inventory/map schema and documented empty or
  synthetic fixture shape.
- Add source_ids to the dump coverage model.
- Extend the checker with input-source-set, source-journey,
  topic-to-graph-source, publication-mapping, and friction categories.
- Support Markdown Source ID syntax and HTML <code> source IDs.
- Add synthetic tests for the Plan 2b cases.
- Update the G13 authoring skill to use the Plan 2b checkpoint.

Do not inventory or modify real fact-sheet/case-file/topic content yet.
Do not modify the live G13 SQLite research content, fact sheet, case file,
legacy companion, dumps, or site.
Use .\.venv\Scripts\python.exe for every Python command.
Run focused tests and the existing graph/coverage tests.
Do not commit unless asked.
Stop with a concise schema/checker/test report and any friction that requires
Allen's decision.
```

### Thread 2 — Freeze and inventory supplemental surfaces

```text
Work in the current gurney-genealogy checkout. This is Plan 2b Thread 2:
inventory and routing only.

Read Plan 2b and the completed Thread 1 implementation first. Freeze a Plan 2b
cutoff for:
- fact-sheets/g13-john-gurney-fact-sheet.md
- research/case-files/john-gurney-case-file-v4.md
- the seven G13/John topic files enumerated in Plan 2b section 3.3 (explicit
  list — do NOT glob research/topics/g13-john-gurney-*.md, which matches only
  one of them)

Populate coverage/supplemental-surfaces-map.csv mechanically, then review the
meaningful assertion/block boundaries. For every row, preserve the complete
source-ID set, route it to a stable topicId, and record friction. Include
publication-only/external-canonical dispositions where appropriate; do not
force all case-file prose into a topic.

Also audit source_ids in the existing legacy and dump maps against the frozen
input text and footnote definitions. Report every mismatch.

Do not edit the origin fact sheet, case file, existing topics, legacy
companion, dumps, staged topic prose, or live graph content.
Use repo_search.py first and .\.venv\Scripts\python.exe for Python.
Run the expanded checker and hand off a destination-by-destination remediation
manifest.
Do not commit unless asked.
```

### Thread 3 — Remediate arrival and Weymouth

```text
Work in the current gurney-genealogy checkout. This is Plan 2b Thread 3:
source-lossless remediation of only:
- g13-colonial-arrival-chronology
- g13-colonial-weymouth-community

Read AGENTS.md, Plan 2b, the G13 graph-authoring skill, the Thread 2 remediation
manifest, both staged topic files, and every routed input block before editing.

Reconcile all companion, dump, fact-sheet, case-file, and existing-topic
sources. Preserve derivative, duplicate, discovery, negative, and conflicting
sources with truthful roles. Backfill Plan 2a markers for arrival chronology.
Resolve or explicitly retain every friction row in scope. Do not edit any
origin surface or the site.

Author prose and graph changes together. Dry-run each author-batch first; then
commit the batch, hash new local sources, snapshot, validate, status-check, and
run the expanded coverage checker. Keep existing IDs where identity is stable.
Use .\.venv\Scripts\python.exe for Python.
Do not commit git changes unless asked.
Stop with source-set before/after counts, added relationships, and unresolved
friction.
```

### Thread 4 — Remediate Braintree, material life, and occupation

```text
Work in the current gurney-genealogy checkout. This is Plan 2b Thread 4:
source-lossless remediation of only:
- g13-colonial-braintree-community
- g13-colonial-material-life
- the cross-topic occupation finding

Read AGENTS.md, Plan 2b, the G13 graph-authoring skill, the Thread 2 remediation
manifest, both staged topics, and all routed input blocks.

Required checks include Sprague, Bates, Suffolk Deeds Liber IV/V, the
FamilySearch full-text deed representation, the 1645 and 1646 Braintree
petitions, Tyng evidence, Brackett associations, probate manuscript/abstract/
index sources, the tailoring-tool negative, and husbandry interpretation.

Create or identify one canonical occupation finding and connect all relevant
evidence and published-source statements without treating derivative witnesses
as independent primary records. Preserve every aligned source. Correct the
known material-life prose/item issues only where the routed evidence supports
the correction.

Do not edit the fact sheet, case file, legacy companion, dumps, existing topic
files, or site. Dry-run graph batches first; snapshot, validate, status-check,
and run the expanded coverage checker after each bounded transaction.
Use .\.venv\Scripts\python.exe for Python.
Do not commit git changes unless asked.
```

### Thread 5 — Remediate frontier rights

```text
Work in the current gurney-genealogy checkout. This is Plan 2b Thread 5:
source-lossless remediation of only g13-colonial-frontier-rights.

Read AGENTS.md, Plan 2b, the G13 graph-authoring skill, the Thread 2 remediation
manifest, the staged frontier topic, and all routed input blocks.

Reconcile every Billerica, Mendon, Quinapaug, Weymouth-great-lot,
probate-index, manuscript, printed, compiled, and discovery source. Repair the
known Nash prose-to-graph gap. Preserve the boundary between John's own rights
and the later widow/descendant stream. Record rather than suppress chronology
or source-alignment friction.

Do not edit origin surfaces or the site. Author prose and graph changes
together; dry-run first, then snapshot, validate, status-check, and run the
expanded coverage checker.
Use .\.venv\Scripts\python.exe for Python.
Do not commit git changes unless asked.
```

### Thread 6 — Plan 2b closeout and continuation gate

```text
Work in the current gurney-genealogy checkout. This is Plan 2b Thread 6:
read-only audit first, followed only by narrow fixes required to close the
approved five-topic remediation.

Read AGENTS.md, Plan 2b, all prior thread handoffs, the coverage ledgers, the
five staged topics, and the live graph status/report.

Run the expanded coverage checker and independently verify:
- frozen-input integrity;
- complete source sets for companion, dumps, fact sheet, case file, and
  existing G13 topics;
- source journey into the five topics and graph;
- topic prose / graph / citation-ledger parity;
- publication mappings;
- marker coverage;
- friction dispositions;
- recovery, snapshot, index, and source-hash health.

Do not broaden into unauthored topics. If narrow fixes are needed inside the
five approved topics or their graph records, state them, apply them through
the normal author-batch workflow, and re-run all checks. Do not edit the fact
sheet, case file, legacy companion, dumps, or site.

Conclude with an explicit GO / NO-GO recommendation for resuming normal G3
topic authoring. Do not commit unless asked.
```

## 14. Revision notes (r2, 2026-07-04)

Independent review before acceptance confirmed the plan's core diagnosis and
corrected the following. The §4.2 audit examples were re-verified directly
against snapshot r15: `sprague-braintree`, `anderson-gmd-2015`, and
`suffolk-probate-index-v2-1895` are registered with zero item links, and
`nash-historical-sketch-weymouth-1885` links to arrival/Weymouth items but no
frontier item. The block-level KISS design and the no-schema-escalation rule
were accepted unchanged.

Corrections:

1. **§3.3/§6.3/Thread 2** — the "seven `g13-john-gurney-*.md` files" glob
   matches exactly one file; the seven are now enumerated explicitly
   (immigration-by-association + six `john-gurney-candidate-*` files).
2. **§8.0 (new)** — the plan never said where the checker gets graph truth;
   it now reads the newest tracked snapshot NDJSON, with `graph_export_missing`
   as a gating category rather than a silent skip.
3. **§8.1** — block-boundary completeness is human review; the checker gates
   only file enumeration and hashes. The plan no longer implies mechanical
   proof of "every meaningful block has a row."
4. **§8.2** — source-set checks gate dispositioned rows only (un-dispositioned
   rows are backlog), and block anchoring is tiered with reported fallbacks
   (legacy spans self-verify against the 16-hex `content_hash`, 38/41 today;
   dump findings anchor on `### F<id>` headings).
5. **§6.2** — disposition separator normalization (`-`/`_`) instead of
   pretending the existing ledgers are consistent.
6. **§8.5** — the mechanical projection of publication alignment is defined;
   assertion-level expressiveness stays human.
7. **§8.6** — per-increment vs cutover gating is explicit, including deferred
   journey checks for not-yet-staged destination topics.
8. **§9 step 12** — per-topic `coverageStatus` lands in `manifest.json`, not
   in thread handoffs.
