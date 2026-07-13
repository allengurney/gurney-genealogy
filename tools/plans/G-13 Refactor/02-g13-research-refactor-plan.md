# G13 companion and research-dump refactor

## 1. Purpose

Replace the oversized, fragile G13 research companion with a coherent
topic-structured research package while preserving:

- Every substantive current finding.
- Every useful detail and anecdote.
- Every citation and source relationship.
- Conflicting and negative evidence.
- Open questions and source-coverage limitations.
- The raw research dump and its discovery trail.

The refactor is not a coarse three-file split. It uses enough narrow topical
units that projected 50% growth does not recreate today's oversized document,
while the graph/context layer prevents AI from having to read every unit.

## 2. Current scale

Measured July 2026:

- G13 companion: 18,799 words, 617 lines, 36 headings, 67 footnotes.
- Average other companion: approximately 3,053 words.
- G13 ratio: 6.16 times the average.
- G13 at 25% growth: approximately 23,499 words.
- G13 at 50% growth: approximately 28,198 words.
- John Gurney case file: approximately 21,233 words.
- Seven G13/John topic files: approximately 24,269 words.
- Current G13 companion HTML: approximately 176 KB.

The surrounding ecosystem proves that moving material sideways into a few large
files does not solve grounding or discoverability.

## 3. Staged and final layouts

### During development

```text
research/people/_staging/g13-john-gurney/
  README.md
  manifest.json
  coverage/
    legacy-companion-map.csv
    dump-findings-map.csv
    source-and-citation-map.csv
  topics/
    00-current-state-and-navigation.md
    colonial/
    family/
    origin/
    identity/
    research-state/

tools/g13_graph/            # CLI, modules, DDL, migrations, synthetic fixtures
data/context-graphs/g13/
  exports/
    current.ndjson          # git-ignored, OneDrive-protected recovery
    snapshots/              # versioned milestone exports, git-tracked
  build-report.json

# Live canonical SQLite is outside OneDrive/Git at the dedicated GitDirs path
# in Plan 01 §7. It is not a cache. Entities and items are DB rows, not JSON.
```

The existing companion stays untouched at its current path.

### After approved cutover

```text
research/people/
  g13-john-gurney-fact-sheet.research.md   # compact substantive hub
  g13-john-gurney/
    manifest.json
    colonial/
    family/
    origin/
    identity/
    research-state/

  # Tracked graph code/schema lives under tools/g13_graph/.
  # Versioned G13 recovery exports live under data/context-graphs/g13/exports/.

  _legacy/g13-pre-refactor/
    g13-john-gurney-fact-sheet.research.md # exact preserved legacy copy
    checksums.json
    coverage-report.md
```

The conventional `g13-john-gurney-fact-sheet.research.md` entry path is preserved,
but the substantive front door is the research library's own intro
(`topics/00-research-library.md`); see §6. At cutover the legacy path becomes a
compact pointer to the promoted research library rather than a second authored hub.

## 4. Topic design

Initial proposed units:

```text
topics/
  00-current-state-and-navigation.md

  colonial/
    01-arrival-chronology.md
    02-weymouth-community.md
    03-braintree-community.md
    04-frontier-rights.md
    05-material-life.md
    06-record-coverage.md

  family/
    10-wives-marriages.md
    11-family-group.md
    12-mendon-descendants.md
    13-colonial-collaterals.md

  origin/
    20-age-baptism.md
    21-trade-training.md
    22-migration-network.md
    23-wardship-network.md
    24-bury-connections.md
    25-origin-traditions.md

  identity/
    30-candidate-overview.md
    31-aylesbury-candidate.md
    32-norfolk-parentage.md
    33-berkhamsted-candidate.md
    34-london-candidate.md
    35-ackworth-candidate.md
    36-other-candidates.md
    37-identity-assessment.md

  research-state/
    40-source-coverage.md
    41-open-questions.md
    42-conclusion-history.md
```

This is a starting taxonomy, not a mechanical quota. The two-tier
group/topic structure is intentional: broad reader-facing domains contain many
narrow research units. Merge genuinely small units; split a unit when it
becomes conceptually mixed or exceeds the target band.

The ~30-file skeleton above is **illustrative, not binding**. Derive the actual
units from the frozen inventory (§7–§8), not the other way around: do **not**
pre-create empty stubs to match the skeleton, and let the real content dictate how
many units emerge (expected ~15–20). A skeleton file with no assimilated content
is a defect, not a placeholder.

Colonial false friends and search variants are repository-wide discovery
method, not a G13 ancestor topic. Keep the durable registry in a cross-cutting
topic or search-variant artifact and retain only concise G13-relevant warnings
and links where they affect a specific finding.

Candidates A, B, C, and D each require their own identity unit. Candidate B
(`norfolk-parentage.md`) may also depend on several origin/network units;
Candidates A, C, and D should absorb their existing standalone topic files into
the package. Retain old repository pointer stubs and public redirects until
inbound links are migrated. Ackworth and residual candidates remain separate
enough to avoid recreating an oversized identity file.

Target size:

- Normal unit: 800–2,500 words.
- Review threshold: 3,500 words.
- Split threshold: approximately 5,000 words unless the material is one
  indivisible argument or transcription.

At the 50% growth assumption, roughly 15–20 substantive units should remain
well below the present companion size.

## 5. Boundary rules

The logical G13 companion becomes the root hub plus its subject-owned package.
This requires updating the research rule (`.claude/rules/research-files.md`) from
a flat-file assumption to a package-aware convention. **That rule edit lands at
cutover, not during staging or the pilot** — editing it earlier changes live
behavior for every people file, and the analysis/pilot phases must not mutate
persistent guidance (per `.claude/rules/continual-improvement.md`).

**Single home per conclusion.** Each conclusion has exactly one canonical home;
every other surface (root hub, case file, fact sheet, topic unit, graph item)
*cites or summarizes* it rather than restating it in full. This is the guard
against fact-sheet / case-file / hub / topic / graph-item quintuplication, which
the package makes newly possible. When a conclusion must appear in more than one
place, the fuller treatment is the home and the others carry a compact,
independently-cited summary that points to it.

Keep:

- G13-specific working research in the G13 package.
- Cross-cutting methodology and multi-subject analysis in `research/topics/`.
- Candidate A, B, C, D, Ackworth, and residual-candidate research in separate
  subject-owned identity units inside the G13 package.
- Place-specific analysis in `research/places/`.
- Source extracts and media in `sources/`.
- The case file as the polished, user-directed published argument.

The package may summarize an external topic and link it, but must not duplicate
its full treatment.

The current rule placing low-probability alternative candidates under
`research/topics/` must be revised at implementation: a package-aware G13
companion now provides their natural subject-owned home.

### Stable identity versus filename

Topic identity, repository path, and public URL are separate:

```text
topicId:     g13-identity-candidate-a
path:        identity/aylesbury-candidate.md
publicSlug:  candidates/aylesbury
```

Graph relationships and manifests use `topicId`; the website uses
`publicSlug`. Filenames may change freely during staging and later require only
a manifest-path update plus raw-link maintenance. Public URLs need not change.

Coverage and routing ledgers must also use `topicId`, not numbered shorthand,
so renaming or reordering a file cannot silently change its destination.

## 6. The root hub

> **Revised 2026-07-13 (Allen's direction): no separate root hub — the research
> library's own intro is the single front door.** Superseding the 2026-07-12
> extra-light-hub revision below, the separate `hub.md` companion is retired.
> Even an extra-light hub with a footnoted identity/lineage banner proved to be a
> mini fact sheet — a second copy of the biography to keep in sync. The
> research-library landing intro (`topics/00-research-library.md`, manifest
> `website.introFile`) is used as-is and is now the single front door for both
> surfaces: the website annex landing page and, after cutover, the substantive
> entry point for the promoted research library at `research/people/g13-john-gurney/`.
> It already carries a condensed identity/lineage summary plus the three-layer
> framing (fact sheet, case file, research library) and the Context Graph Explorer,
> and it needs no footnotes — its facts are summaries of findings the linked topic
> pages cite in full. No separate hub is authored and no additional footnoted
> banner is added. The conventional `g13-john-gurney-fact-sheet.research.md`
> path is replaced at cutover by a compact pointer to the promoted research
> library, preserving the entry path without duplicating prose. The companion rule
> is satisfied by the research library itself, not by a separate authored hub.
>
> **Prior revision, 2026-07-12 (superseded):** an extra-light root-hub stub
> (~300–800 words) staged as `hub.md` (manifest `website.rootHubFile`), carrying a
> condensed footnoted identity/lineage banner, an orientation block to the
> library / fact sheet / case file / direct-line father-son companions, and an
> external-canonical identity-status statement (the ~65% figure lives in the case
> file, not restated here). Retired 2026-07-13 for the reason above.

**Superseded original design** — `g13-john-gurney-fact-sheet.research.md` after
cutover was to contain:

- Identity and lineage-status summary.
- Current probability assessment and date.
- Compact known-facts table.
- Current conclusions by domain.
- Material conflicts.
- Highest-value open questions.
- Topic map with "read when" guidance.
- Links to case file, fact sheet, external candidate topics, places, sources,
  and the graph coverage view.

It must carry enough substance to satisfy the companion rule. It must not merely
say "see another file."

Target: 2,500–4,000 words.

## 7. Coverage-ledger method

Refactoring will be controlled by three ledgers.

### 7.1 Legacy companion map

One row per current heading or independently meaningful block:

```text
legacy_path
legacy_heading
line_start_at_inventory
content_hash
destination_topic
disposition
research_item_ids
source_ids
notes
```

Disposition:

- `moved`
- `synthesized`
- `retained_in_hub`
- `external-canonical`
- `superseded-but-preserved`
- `duplicate`
- `needs-decision`

### 7.2 Dump findings map

One row per dump finding/input/negative ledger:

```text
dump_file
finding_id
finding_heading
destination_type
destination_path
disposition
source_registration_required
research_item_ids
lead_action
lead_ids
notes
```

### 7.3 Source and citation map

For every staged research unit:

- All cited `sourceId` values.
- Unregistered sources requiring deliberate registration.
- Exact locator availability.
- Media/corpus artifact path.
- Findings supported, contradicted, or qualified.

No staged unit may be approved while it contains an untracked citation gap.

### 7.4 Coverage checker (mechanized, not manual)

Losslessness is enforced by a small checker, not by manual CSV vigilance. A script
(Codex or Fable, against a frozen spec) reads the three ledgers plus the frozen
inventory and:

- flags any legacy heading/block or dump finding with **no disposition**;
- reports coverage as a percentage and lists the gaps;
- flags any staged unit citing a `sourceId` absent from the source-and-citation
  map.

The checker must report zero un-dispositioned items and zero untracked citation
gaps before cutover (§14, §15).

## 8. Research dump assimilation

The dump contains session-oriented prose, unresolved leads, later corrections,
duplicated material, images, and large OCR captures. It must be assimilated,
not copied wholesale into topical research.

The inventory must capture more than factual findings. Classify each substantive
dump item as:

- Source evidence.
- Factual finding.
- Objective analysis or reasoning.
- Interpretation.
- Hypothesis.
- Speculation worth preserving.
- Evidence conflict.
- Negative result.
- Open question.
- Actionable lead.
- Search-method lesson.
- Source artifact.
- Correction or supersession.
- User-supplied reasoning.
- Rejected path that prevents repeated work.

Analysis is not a synonym for hypothesis. Analysis may compare records,
construct chronology, weigh evidence, or explain implications without promoting
one proposed answer. Hypotheses remain explicit proposed explanations or
identities.

### Required sequence

1. Freeze an inventory and hashes against a **specific clean git commit ref** as
   a hard cutoff; do not alter the dump. If the working tree is not clean, a
   commit ref is insufficient because it omits modified and untracked inputs:
   either commit the complete dump first or preserve a content-addressed
   immutable inventory/copy of every input. Material added after the cutoff is
   queued for a later round, not folded into this refactor.
2. Identify duplicate and overlapping files.
3. Extract every finding and negative-result ledger into the dump map.
4. Mark later resolutions against earlier tentative findings.
5. Identify destination by subject, not by session.
6. Register or verify sources before promoting new research.
7. Move source extracts/media to their canonical source destinations only in a
   later approved implementation phase.
8. Draft topical synthesis using current best conclusions.
9. Preserve discovery history in research-item relations, footnotes, HTML comments, or
   legacy/dump references rather than visible dated update blocks.
10. Do not delete the dump until Allen separately decides its archival
    disposition.
11. Route theories, analysis, hypotheses, speculation, and user reasoning
    deliberately; do not extract only factual findings.
12. Reconcile every actionable open item with the live leads catalog.

### Known reconciliation points

- Round 1 F2's "Jane" Bundy bride is later resolved to Ruth; preserve the error
  path but publish the corrected conclusion.
- Round 1 F3 "Jane Gurnet" is later resolved into the Dorchester Gurnell/Gornell
  false-friend family.
- Round 1's Cheny/Gurney conflict is materially advanced by the Braintree
  manuscript images and the "John Girny, Senior" reading.
- Round 1's Arch. 45 petition lead is found and imaged in round 4.
- The former `temp999.md` was deliberately deleted after its useful material
  was reconciled into the named dumps. Do not expect or recreate it; the frozen
  inventory begins from the post-cleanup dump state.
- Round-3 part 1 left some ledgers unpopulated; reconstruct them from its
  finding text before assimilation.
- The Hobart journal transcription is a source/transcription artifact with
  scoped negative and false-positive findings; it is not ordinary companion
  prose.
- Round 5 is primarily G14–G37 but includes network and collateral material that
  may bear on G13; route each finding to its actual subject.
- Large OCR files are source candidates, not research narrative.

## 9. Initial dump-to-topic routing

| Dump theme | Likely canonical destination |
|---|---|
| Braintree Girny/Grizzell manuscript evidence | `g13-family-wives-marriages` |
| 1646 Braintree meadows petition | `g13-colonial-braintree-community` |
| Complete MBCR/Boston record-class negatives | `g13-colonial-record-coverage` and `g13-research-source-coverage` |
| Weymouth/Braintree associate networks | `g13-colonial-weymouth-community` and `g13-colonial-braintree-community` |
| John Jr., Ruth Bundy, descendant disambiguation | `g13-family-mendon-descendants` |
| Colonial Gurnell/Garnet/Gardner false friends | Cross-cutting repository method, with only finding-specific warnings in affected G13 units |
| Winthrop/Gurdon/wardship network | `g13-origin-wardship-network` and external G14/G15/place files |
| Migration/reception network classes | `g13-origin-migration-network` and immigration topic |
| East Dereham/Bury/Boston conduit evidence | `g13-origin-age-baptism`, `g13-origin-bury-connections`, and other affected units as warranted |
| Candidate-B probability synthesis | `g13-identity-candidate-b` and `g13-identity-assessment` |
| G14–G37 findings | their own people/place/topic destinations, with only G13 bearing summarized here |
| OCR books and manuscript images | sources corpus/media after source review |
| Gated or unfinished routes | research-state/41 and leads catalog |
| Objective reasoning and synthesis | relevant substantive topic as analysis |
| Testable proposed explanations | relevant topic as hypothesis |
| Non-actionable but valuable speculation | topic research note with explicit status |

This table is provisional. The coverage ledger records the final decision.

## 10. Citation migration

- Move each factual cluster with its supporting footnotes.
- Rebuild footnote labels locally within each topic file.
- Do not create a global bibliography that separates evidence from findings.
- When a hub summary repeats a conclusion, cite it independently and compactly.
- Preserve every aligned source, not merely one representative source.
- Maintain source-role distinctions in the graph.
- Keep exact quotations and transcriptions in the relevant topic or source
  artifact.
- Validate all footnote references, URLs, source IDs, and repo links.

## 11. Research-item integration

The paragraph/cluster-level bridge from narrative prose to research items,
including Evidence markers and reader exploration, is specified in
[Plan 2a](02a-narrative-graph-evidence-markers.md).

Research items are **rows in the canonical SQLite graph** (Plan 01 §6), authored
through the graph artifact or the one-time seed loader — not JSON files. Author
prose and items **together, per topic, in a single pass**: read the source
material once, write the topic file, and register its items in the same sitting.
This avoids the double-read that a prose-first-then-graph-second sequence would
force, and is the efficiency reason to not defer all graph work to a separate
phase.

Each substantive topic section should map to one or more stable research-item
IDs: source evidence, findings, analyses, hypotheses, conflicts, negative
results, open questions, or project statements.

Requirements:

- Every discrete finding, material analysis, hypothesis, and open question is
  mapped or explicitly marked `context-only`.
- The graph item contains a compact statement; the topic file carries the full
  evidence and analysis.
- A research item may cite multiple sources.
- One source may support multiple findings.
- Research findings list their source-evidence and analysis dependencies.
- Project statements in fact sheets/case files map to the findings they express.
- Negative results use structured search scope.
- Paragraph-level footnotes with uncertain fact/source alignment use collective
  evidence groups rather than invented direct edges.
- Source-evidence items normally represent one identifiable source record or
  witness. Multi-source synthesis is a finding or analysis, not one blended
  source-evidence item.
- Plausible and probable date ranges are both preserved. A derived
  `chronologyKey` may order items but is never displayed as historical evidence.
- Research-item IDs are kind-neutral (`G13-RI-...`) so review may reclassify an
  item without changing its identity.
- Every item and evidence excerpt receives an explicit publication-visibility
  decision before static export.

The graph must not dictate prose structure. Topic files remain readable,
finding-first research notes.

### Topic-level cross-store checkpoint

Markdown and SQLite cannot participate in one transaction. At the end of each
co-authoring unit:

1. Save the topic prose.
2. Save the corresponding graph edits transactionally.
3. Run topic-scoped research-location, source, relation, and citation validation.
4. Atomically refresh the current recovery export.
5. Record the topic/DB revision in the coverage ledger.
6. Commit prose, ledger changes, schema changes if any, and the appropriate
   versioned export snapshot together at the review milestone.

A topic is not review-complete while either store is ahead of the checkpoint.

## 12. Leads management during assimilation

Every dump item receives one operational disposition:

- Assimilated into research.
- Updates an existing lead.
- Closes an existing lead.
- Creates a new lead.
- Superseded by later work.
- Preserved as a source artifact.
- Preserved as non-actionable speculation.
- Routed to another ancestor/topic/place.

Requirements:

- Use `research_leads.py`; do not rewrite the full CSV.
- Search for an existing lead before creating one.
- Store the dump finding ID, destination topic ID, research-item IDs, and
  relevant source IDs in the coverage ledger.
- When closing a lead, record where the result landed.
- When updating a lead, preserve desired outcome, what was checked, remaining
  delta, access limitations, and deeper-context path.
- Do not turn every speculative thought into a lead; create one only for
  actionable future work.
- An `open_question` research item may link to a lead handle, but the leads
  catalog remains the canonical operational queue.
- Keep lead handles out of visible research prose except in footnotes or HTML
  comments where they preserve discovery trail.

## 13. Review workflow

Review by domain rather than waiting for the entire package:

1. Colonial chronology/property.
2. Family and descendants.
3. English origin and Candidate B.
4. Candidate comparison.
5. Negative searches/open questions.
6. Root hub and crosslinks.

For each domain:

- Compare staged topic against mapped legacy blocks and dump findings.
- Check research-item/source alignment.
- Check conflicts and uncertainty.
- Check for duplicative treatment in case/topic/place files.
- Run link/footnote validation.
- Record approval in the coverage ledger.

## 14. Acceptance criteria

### Losslessness

- Every legacy block has a disposition.
- Every dump finding has a disposition.
- Every dump analysis, hypothesis, speculation, open question, and lead has a
  disposition.
- Every active factual finding has a source.
- Superseded conclusions remain traceable.
- Raw dump and legacy companion remain available.

### Structure

- No staged topic is an unassimilated session log.
- No topic exceeds the size threshold without a documented reason.
- The hub provides a complete map and substantive current state.
- External topic/place/case-file boundaries remain clear.

### AI

- Default G13 grounding uses the hub plus a graph context package.
- A task can identify the relevant detailed units without reading the entire
  package.
- Exhaustive work receives a coverage ledger.

### Human

- A reader can follow each topic without reconstructing session order.
- Citations remain close to supported facts.
- Conflicts and probabilities are explicit.

## 15. Cutover

Cutover is a separate approved operation:

1. Freeze and validate staged package.
2. Generate final coverage and difference reports.
3. Copy the exact current companion into `_legacy/g13-pre-refactor/`.
4. Promote staged topics to `research/people/g13-john-gurney/`.
5. Replace the legacy root companion (`g13-john-gurney-fact-sheet.research.md`)
   with a compact pointer to the promoted research library — the library's own
   intro (`00-research-library.md`) is the substantive front door (§6).
6. Switch the website from legacy to package mode.
7. Rebuild repository search indexes; migrate or repoint and validate the
   canonical graph DB, then refresh only its derived FTS/context/site exports.
8. Validate site, citations, links, research items, and source IDs.
9. Keep rollback instructions and legacy content in place until Allen accepts
   the result.

See `support/staging-cutover-and-rollback.md`.
