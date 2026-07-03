# SQLite context graph for G13

## 1. Purpose

Build a lightweight, local context graph that lets AI and tooling retrieve a
complete, provenance-bearing slice of G13 research without rereading the full
companion, case file, topic set, and source corpus.

The graph addresses a representation problem, not merely a file-size problem.
Splitting 28,000 projected companion words among a few files would still force
AI to reconstruct the same evidence, findings, analyses, hypotheses, and
relationships from prose. The graph makes those research items, conflicts,
dependencies, and publication impacts explicit and queryable.

This is an implementation of a **canonical-SQLite** model. Structured graph
content lives in a real database; prose and sources remain canonical files.

> **KEY ARCHITECTURE DECISION — read before implementing (changed 2026-07-03).**
> An earlier draft made hand-authored JSON item files canonical and treated
> SQLite as a disposable, rebuildable cache. **That model is rejected.** Database
> content belongs in a database. The adopted model:
>
> - **SQLite is canonical** for all structured graph content — research items,
>   relations, evidence links, dates, negative-result scope, entities, and
>   aliases. The graph-editing artifact reads and **writes SQLite directly.**
>   There is **no hand-authored JSON layer** and **no JSON import/export in the
>   edit path.**
> - **Prose topic files** (`research/people/...`) remain canonical for the human
>   narrative — text, in the repo, git-tracked.
> - **`data/sources.json`** and `sources/` remain canonical for source metadata
>   and artifacts.
> - A **derived text export** (SQLite `.dump` and/or NDJSON snapshot) is produced
>   *from* the DB on a cadence/trigger and committed at milestones for **backup
>   and coarse audit history.** It is never hand-edited and never an edit surface.
> - Relational integrity (primary keys, foreign keys, uniqueness) is enforced
>   **by the database** — a primary reason for the change, since loose JSON
>   cannot enforce it.
>
> Do not reintroduce a canonical JSON items layer under another name (see §6, §7,
> §11, §14). A one-time developer **seed loader** may bootstrap an initial batch
> (§11), but the seed file is write-once, is not re-read on every build, and is
> not the source of truth.

```text
 Prose topic files                 data/sources.json + sources/
 (canonical narrative)             (canonical sources)
        \                                 /
         \        author/edit via        /
          \    artifact + prose files    /
                        |
                        v
        SQLite context graph  (CANONICAL structured store)
                        |
      +-----------------+---------+------------------+-------------+
      |                 |         |                  |             |
      v                 v         v                  v             v
 AI context     graph-editing   in-model         derived export   static
 compiler       artifact        item_revisions   snapshot         website
                (direct         (audit trail)    (backup + audit,  exports
                 SQLite R/W)                      committed)
```

## 2. Required outcomes

The implementation must support:

- Compact, task-specific AI grounding with an explicit token/character budget.
- Comprehensive coverage ledgers that show what was considered, expanded, and
  omitted.
- Finding/evidence-to-source traceability using existing `sourceId` values.
- Many-to-many source/finding relationships.
- Explicit supporting, contradicting, qualifying, dependency, elimination, and
  supersession relationships.
- Separate treatment of source evidence, research findings, objective analysis,
  identity hypotheses, bounded negative results, conflicts, published-source
  statements, and project statements.
- Historical event time distinct from project-knowledge/revision time.
- Impact queries: "What must be reviewed if this finding changes?"
- Static exports for the future website finding drawer.
- A stable read/write contract for a Claude-built graph editor.
- Deterministic schema rebuild, and exact content restore from the latest
  committed export snapshot (the DB content is not regenerated from prose).

## 3. Explicit non-goals

The first implementation will not:

- Replace canonical Markdown, source files, or `data/sources.json`.
- Automatically promote machine-extracted facts into the approved graph.
- Infer that same-name people are identical.
- Calculate lineage probabilities by adding evidence weights.
- Treat an unsuccessful search as proof that an event did not happen.
- Provide a general graph platform for every ancestor.
- Require Neo4j, Redis, Docker, a background service, or a cloud database.
- Implement the public finding-drawer experience.
- Write graph changes directly into published research prose.

## 4. Why SQLite

The repository already uses SQLite FTS5 in `repo_search.py`. SQLite supplies:

- A single local database file.
- Full-text indexing and ranking.
- Recursive common-table expressions for graph traversal.
- Transactional, deterministic rebuilds.
- Straightforward Python support inside the repository's `.venv`.
- No service operations.

Semantic embeddings are optional. Begin with explicit relationships, FTS5,
variants, and the existing fuzzy retrieval. Add a vector extension only if
evaluation proves that these are insufficient.

## 5. Architecture decision record

The thread considered several graph/retrieval approaches.

### Graphiti

Graphiti was a serious candidate because it supplies temporal facts,
provenance-bearing episodes, entity/relationship extraction, hybrid retrieval,
and an MCP server. It could fit either:

- A derived retrieval layer over canonical repository content; or
- A graph-native system where the graph becomes canonical.

It was not selected for the G13 first implementation because it introduces LLM
extraction and entity resolution at the point where this project most needs
determinism. Specific risks include:

- Conflating same-name John Gurneys.
- Converting inference into fact.
- Losing probability qualifiers.
- Treating a search miss as historical absence.
- Attaching a finding to the wrong citation.
- Requiring a graph backend and more surrounding operations.

Graphiti remains a future comparison point if the SQLite pilot proves that
automatic extraction or richer graph operations are necessary.

### LlamaIndex property graph

Potentially useful for a prototype, including disk-persisted simple property
graphs and graph/vector retrievers. It still adds a broad AI framework and does
not by itself enforce the project's genealogy-specific provenance, negative
evidence, or identity rules.

### PyOxigraph/RDF

Provides an embedded standards-based RDF/SPARQL graph. It is technically sound
but introduces ontology and query complexity without solving research-item extraction
or context assembly.

### FalkorDBLite

Provides embedded Cypher-capable graph storage without an externally managed
server. It is lighter operationally than a full graph service but still
supplies storage rather than the repository-specific finding and provenance
model.

### Decision

Use SQLite because the required capability is narrower than a general agent
memory platform:

- Explicit research items.
- Explicit relations.
- Provenance.
- Temporal/revision fields.
- Full-text retrieval.
- Graph traversal.
- Context assembly.

The project already owns the authoritative entities, sources, prose, and
variant-aware search machinery. The largest missing object is the explicit,
queryable research item: evidence, finding, analysis, hypothesis, conflict,
negative result, question, or project statement.

## 6. Source-of-truth boundaries

### Canonical

- Source metadata: `data/sources.json`.
- Source artifacts: `sources/`.
- Research prose: staged G13 topic package, later promoted to canonical
  `research/people/`.
- **Structured graph content: the SQLite database** — research items, relations,
  evidence links, dates, negative-result scope, entities, and aliases. This is
  the authoritative store for everything the graph model adds beyond prose and
  sources. It is edited through the artifact (§14), not by hand-editing files.
- Published narrative: `fact-sheets/` and the existing case file.

### Derived

- The **export snapshot** (SQLite `.dump` / NDJSON) — a backup and audit artifact
  generated *from* the canonical DB, committed on a cadence, never hand-edited.
- FTS indexes and embeddings (rebuildable inside the DB).
- Context packages.
- Static finding JSON and generated finding pages.
- Artifact working caches.

### Consequences (do not revert to the old model)

- The DB is **not** "safe to delete and rebuild from files." Its structured
  content exists nowhere else in editable form. Its recovery path is **restore
  from the latest export snapshot**, so backup discipline (§7, §11) must be in
  place *before* the DB holds anything valuable.
- What *can* be rebuilt deterministically is the **schema** and the **derived
  indexes/exports**; the **content** is restored from a snapshot, not
  regenerated from prose (prose is not machine-parsed back into items).
- Change history and provenance live **in the model** (`knowledge_valid_from/to`,
  `review_state`, `superseded_by`, and the `item_revisions` table — §10) plus the
  committed export snapshots — **not** in git line-`blame` of a JSON file. This
  is a richer, queryable history than git blame provided, and is an intended
  trade, not a loss.

## 7. Staging and storage

During development:

```text
research/people/_staging/g13-john-gurney/
  manifest.json
  topics/                      # canonical prose (staged), git-tracked
  graph/
    schema/                    # DDL + migrations (git-tracked; the schema source of truth)
    seed/                      # OPTIONAL one-time bootstrap input (see §11); NOT canonical
    exports/                   # committed backup/audit snapshots (.sql / .ndjson)
    build-report.json
```

Live database (git-ignored, OneDrive-ignored):

```text
<repo>/.graph-cache/g13/g13-context.sqlite     # or any convenient excluded path
```

Storage rules:

- The **live `.sqlite` is git-ignored and OneDrive-ignored.** A repo subdirectory
  is fine — *exclusion*, not physical location, is what matters. OneDrive-ignoring
  avoids the file-lock churn noted in AGENTS.md §9; git-ignoring avoids committing
  a binary blob on every change.
- The thing that lives in git/OneDrive for recovery is the **export snapshot**
  under `graph/exports/`, committed at milestones — not the live DB.
- The **schema DDL and migrations** under `graph/schema/` are git-tracked text:
  the reproducible definition of the database structure.
- There is **no `entities.json` / `items/*.json` canonical layer.** Entities and
  items are DB rows. (The earlier draft stored these as pretty-printed JSON
  grouped by topic; that is exactly the JSON-as-database pattern this project is
  moving away from — relational content with cross-references belongs in the
  relational store that can enforce integrity on it.)

## 8. Research-item model

### 8.1 User-facing vocabulary and item kinds

Controlled initial vocabulary:

| Kind | Reader-facing label | Meaning |
|---|---|---|
| `source_evidence` | Source evidence | What a named source explicitly says or shows |
| `research_finding` | Finding | A supported project conclusion |
| `analysis` | Analysis | Objective reasoning, comparison, synthesis, or evidentiary weighing without promoting one proposed explanation |
| `identity_hypothesis` | Identity hypothesis | A testable proposed identity, parentage, or same-person relationship |
| `negative_result` | Negative result | No qualifying result within documented search coverage |
| `evidence_conflict` | Evidence conflict | Two or more items cannot yet be reconciled |
| `published_source_statement` | Published-source statement | What an external compiler or publication states, separate from project adoption |
| `project_statement` | Project statement | What this project currently states in a fact sheet, case file, research hub, or website page |
| `open_question` | Open question | A defined unresolved question with dependencies, target evidence, or a lead |

`analysis` and `identity_hypothesis` are deliberately distinct. Analysis may
establish chronology, compare sources, explain implications, or weigh evidence
without advocating a particular unproven answer. A hypothesis proposes a
specific explanation or identity that can be tested.

The umbrella database/UI term is **research item**, not claim. Individual
screens should normally say Evidence, Finding, Analysis, Hypothesis, Conflict,
Negative Result, Project Statement, or Open Question.

### 8.2 Research-item fields

Required:

```json
{
  "id": "G13-E001",
  "kind": "source_evidence",
  "subjectEntityId": "ancestor-g13-john-gurney-1",
  "statement": "John Gurney was associated with Weymouth by 2 June 1641.",
  "status": "active",
  "assessmentConfidence": {
    "label": "high",
    "value": 0.98,
    "basis": "Direct printed transcription of the court record."
  },
  "researchLocation": {
    "path": "research/people/_staging/g13-john-gurney/topics/colonial/01-arrival-chronology.md",
    "headingId": "june-1641-gunpowder-record"
  }
}
```

Optional fields:

- `shortLabel`
- `summary`
- `dateEnvelope`
- `knowledgeValidFrom`, `knowledgeValidTo`
- `transcriptionConfidence`
- `negativeStrength`
- `coverageLimitations`
- `qualifiers`
- `tags`
- `reviewState`
- `reviewedBy`
- `reviewedAt`
- `supersededBy`
- `notes`

Do not overload one confidence value. At minimum distinguish:

- Confidence that the source was read/transcribed correctly.
- Confidence that the person or event was identified correctly.
- Confidence in the project's research finding or conclusion.

**Confidence is a coarse band, not a precise number.** The `label` (a controlled
band such as `high` / `moderate-high` / `probable`) is the primary field. The
numeric `value` is an optional convenience mirror of the band and **must never be
summed, thresholded, sorted, or otherwise treated as a computed probability** —
consistent with AGENTS.md §8 ("uncertainty is quantified, not hedged") and §8.6's
rule that relation weights are retrieval aids, not probability inputs. Prefer
storing only the band; if a `value` is stored, the schema/validator should treat
it as non-orderable display metadata. This guards against a future query silently
ranking findings by a false-precision float.

Reserve **provenance** for the chain from source artifact and exact locator
through source evidence to research finding and project statement.
`researchLocation` only identifies where the item is defined or explained in
the repository.

### 8.3 Date envelopes and chronology ordering

G13 frequently needs both an outer plausible range and a narrower probable
range. Store both:

```json
{
  "dateEnvelope": {
    "plausibleStart": "1636",
    "plausibleEnd": "1641",
    "probableStart": "1638",
    "probableEnd": "1640",
    "precision": "year",
    "originalDisplay": "plausibly 1636–1641; probably 1638–1640",
    "calendar": "normalized-gregorian"
  },
  "chronologyKey": {
    "value": 1639.0,
    "basis": "probable_midpoint",
    "manualOverride": false
  }
}
```

Rules:

- The probable range must fall within the plausible range.
- An exact date collapses both ranges to the same date.
- Open-ended dates (`before`, `after`) remain open-ended rather than receiving
  invented boundaries.
- Preserve original/Old Style wording separately from normalized values.
- `chronologyKey` is derived ordering metadata, not evidence and never a date
  displayed as though historically observed.
- Default key: exact date; otherwise probable midpoint; otherwise plausible
  midpoint; otherwise a documented manual ordering value.
- Store `chronologyKeyBasis` so sorting behavior is inspectable.
- Allow an explicit manual override for items whose inferred midpoint would
  produce misleading narrative order.

The artifact should provide paired plausible/probable date controls and validate
nesting. Timelines may sort on `chronologyKey` while displaying the actual date
envelope.

### 8.4 Evidence links

Each source connection records:

```json
{
  "itemId": "G13-E001",
  "sourceId": "massachusetts-bay-records-v1-1853",
  "role": "supports",
  "locator": "volume 1, page 331",
  "evidenceExcerpt": "optional short exact extract",
  "alignmentNote": "Supports presence by this date; does not establish arrival year.",
  "verificationLevel": "printed-primary-transcription"
}
```

Controlled roles:

- `supports`
- `contradicts`
- `qualifies`
- `mentions`
- `context_for`
- `negative_within_scope`
- `discovery_only`

### 8.5 Soft evidence groups

When a paragraph contains several facts and one footnote cites several sources
without fact-to-source alignment, do not invent direct edges. Create an
evidence group:

```text
Finding 1 --\
Finding 2 ---- supported collectively by Evidence Group E17
Finding 3 ----                                  |
Finding 4 --/                                   +-- Source A
                                                +-- Source B
                                                +-- Source C
```

The group records:

- `alignment`: `collective`, `probable`, `contextual`, or `unclear`.
- Confidence in the findings.
- Confidence that the source bundle supports the paragraph collectively.
- Whether individual source assignment remains unresolved.
- Research paragraph and footnote location.

Later review may replace a collective group with precise direct connections.

### 8.6 Research-item relationships

Controlled initial relationships:

- `SUPPORTS`
- `CONTRADICTS`
- `QUALIFIES`
- `DEPENDS_ON`
- `ELIMINATES`
- `SUPERSEDES`
- `CONTEXTUALIZES`
- `SAME_EVENT_AS`
- `POTENTIALLY_SAME_PERSON_AS`
- `DISTINCT_FROM`
- `PUBLISHED_AS`
- `SUMMARIZED_IN`
- `REQUIRES_REVIEW_OF`

Every relation may carry:

- `bearing`: direct, indirect, contextual, methodological.
- `strength`: strong, moderate, weak, unknown.
- `explanation`.
- `reviewState`.

Additional analysis-oriented relationships:

- `ANALYZES`
- `SYNTHESIZES`
- `WEIGHS`
- `INFORMS`

Relation weights are retrieval aids, not inputs to automatic probability
arithmetic.

### 8.7 Negative results

Negative-result items require structured scope:

```json
{
  "provider": "Findmypast",
  "collection": "England Marriages 1538-1973",
  "dateStart": "1620",
  "dateEnd": "1634",
  "queryDescription": "G*rn* with Mary/Marie/Maria/Marye/Margery",
  "resultCountReviewed": 37,
  "coverageConfirmed": false,
  "limitations": [
    "Unindexed parishes remain possible.",
    "Some spouse fields may be absent.",
    "Variants outside the wildcard remain possible."
  ]
}
```

The importer must reject a `negative_result` item that lacks scope and
limitations.

## 9. Entity model

Initial entity types:

- `person`
- `place`
- `event`
- `source`
- `record_collection`
- `organization`
- `ship`
- `research_unit`
- `publication`
- `hypothesis`

Prefer existing repository IDs:

- Ancestor record IDs from `data/indexes/ancestor-ids.csv`.
- Place IDs from `data/indexes/`.
- Source IDs from `data/sources.json`.

New graph-local entities use stable G13-prefixed IDs and an alias table.
Aliases do not imply identity. For example, `Gurney`, `Gurny`, `Girny`, and
`Gournet` may be names attached to one record or candidate without becoming
global equivalence rules.

## 10. SQLite schema

Conceptual tables:

```sql
graph_meta(
  schema_version,
  built_at,
  source_tree_hash,
  importer_version
);

research_units(
  unit_id PRIMARY KEY,
  path,
  heading_id,
  title,
  scope_summary,
  content_hash,
  review_state
);

research_items(
  item_id PRIMARY KEY,
  item_kind,
  subject_entity_id,
  statement,
  short_label,
  status,
  assessment_confidence_label,
  assessment_confidence_value,
  transcription_confidence_value,
  knowledge_valid_from,
  knowledge_valid_to,
  research_unit_id,
  superseded_by,
  review_state,
  created_at,
  updated_at,
  revision,
  provenance_origin       -- machine_suggested | human_authored | seed
);

item_dates(
  item_id,
  date_role,
  plausible_start,
  plausible_end,
  probable_start,
  probable_end,
  precision,
  original_display,
  calendar,
  chronology_key,
  chronology_key_basis,
  manual_override
);

entities(
  entity_id PRIMARY KEY,
  entity_type,
  canonical_label,
  description,
  repo_record_id
);

entity_aliases(
  entity_id,
  alias,
  alias_type,
  source_item_id
);

item_entities(
  item_id,
  entity_id,
  role
);

item_sources(
  item_id,
  source_id,
  role,
  locator,
  evidence_excerpt,
  alignment_note,
  verification_level
);

item_relations(
  from_item_id,
  relation_type,
  to_item_id,
  bearing,
  strength,
  explanation
);

evidence_groups(
  evidence_group_id PRIMARY KEY,
  research_unit_id,
  heading_id,
  paragraph_locator,
  footnote_locator,
  alignment,
  individual_assignment_resolved,
  explanation
);

evidence_group_items(
  evidence_group_id,
  item_id,
  role
);

evidence_group_sources(
  evidence_group_id,
  source_id,
  locator,
  role
);

item_publications(
  item_id,
  publication_path,
  heading_id,
  assertion_summary,
  status
);

negative_result_scope(
  item_id PRIMARY KEY,
  provider,
  collection_name,
  date_start,
  date_end,
  query_description,
  results_reviewed,
  coverage_confirmed,
  limitations_json
);

build_issues(
  severity,
  code,
  record_id,
  message
);

item_revisions(
  revision_id PRIMARY KEY,
  item_id,
  changed_at,
  changed_by,
  change_kind,            -- create | update | supersede | review | delete
  field_summary,          -- human-readable summary of what changed
  before_json,            -- compact snapshot of prior row state
  after_json,             -- compact snapshot of new row state
  export_snapshot_id      -- null until captured in a committed export
);

source_content_hashes(
  source_id PRIMARY KEY,
  content_hash,           -- hash of the cited source artifact/text
  hashed_at
);
```

Integrity and provenance notes:

- Structural integrity is enforced **by the database** — primary keys, foreign
  keys, and uniqueness make duplicate/malformed IDs, missing relation endpoints,
  and dangling source/entity references *unrepresentable*, not merely detected.
  This is a core reason for the canonical-SQLite decision (§6); do not rely on
  after-the-fact validation for what a constraint can prevent.
- `item_revisions` is the **in-model audit trail** written on every accepted edit
  (§14). It, plus committed export snapshots, replaces git-`blame` history for
  structured content.
- `source_content_hashes` backs **source drift** detection (§11): an item is
  flagged for re-review when a cited source's hash changes. Prose text is **not**
  hashed.

FTS5 indexes:

- Research-item statement, summary, analysis, qualifiers, and alignment notes.
- Entity labels and aliases.
- Research-unit titles and scope summaries.

Recursive queries traverse `item_relations`. Ordinary joins handle provenance,
source impact, publication impact, and entity neighborhoods.

## 11. Tooling: seed loader, exporter, validator, queries

The structured store is written primarily through the artifact (§14). The CLI
provides bootstrap, backup, validation, and read paths, implemented as a
standalone modular CLI:

```powershell
.\.venv\Scripts\python.exe tools\g13_graph.py init                                   # create/migrate schema
.\.venv\Scripts\python.exe tools\g13_graph.py seed --file graph/seed/initial.ndjson  # one-time bootstrap load
.\.venv\Scripts\python.exe tools\g13_graph.py export --to graph/exports/             # write backup/audit snapshot (.sql + .ndjson)
.\.venv\Scripts\python.exe tools\g13_graph.py restore --from graph/exports/<snapshot> # rebuild DB content from a snapshot
.\.venv\Scripts\python.exe tools\g13_graph.py validate
.\.venv\Scripts\python.exe tools\g13_graph.py status
.\.venv\Scripts\python.exe tools\g13_graph.py item G13-F004
.\.venv\Scripts\python.exe tools\g13_graph.py impact G13-F004
.\.venv\Scripts\python.exe tools\g13_graph.py context --terms Weymouth arrival --budget 12000
.\.venv\Scripts\python.exe tools\g13_graph.py export --format website
```

**Seed vs. canonical — do not confuse them.** `seed` is a *one-time bootstrap*
that loads an initial batch (the Phase G0 reviewed items, or test fixtures) into
an empty DB. The seed file is write-once developer input: it is **not** re-read
on every build, **not** kept in sync with the DB, and **not** the source of
truth. After bootstrap, the DB is authoritative and all edits go through the
artifact. The durable round-trip is **DB → export snapshot**, never seed → DB.
Do not turn `seed` into a de-facto canonical JSON layer.

**Backup discipline is a hard requirement.** Because the DB is canonical (§6),
`export` runs at milestones and before any risky operation, and the resulting
snapshot is committed. A destructive `init`/migration must **refuse to run**
unless a current export exists.

For reversibility, the CLI is a standalone `tools/g13_graph.py` backed by modules
under `tools/g13_graph/`. Any later `repo_search.py graph` entry is a thin,
optional command-registration shim. Graph removal requires deleting only that
module and the git-ignored live cache; ordinary `repo_search` behavior and its
schema remain untouched. (Removing the live graph does not delete committed
export snapshots or prose.)

### Integrity: DB-enforced vs. validator-enforced

Structural integrity is enforced by the **database** — primary keys, foreign
keys, and uniqueness make duplicate/malformed IDs, missing relation endpoints,
and dangling source/entity references *unrepresentable*. The `validate` command
covers the **semantic** rules the schema cannot:

- Cycles in `SUPERSEDES`.
- Active findings superseded by another active finding.
- Negative results without scope or limitations.
- Probable date ranges outside plausible ranges.
- Chronology keys without a declared basis.
- Source connections without locators where locators should exist.
- Research items whose `researchLocation` file or heading does not exist in the prose.
- Publication mappings whose paths or headings do not exist.
- Orphan research items not assigned to a research unit.
- Machine-suggested items not yet human-reviewed.
- **Source drift:** a cited source's content hash has changed since the item's
  last review (`source_content_hashes`), flagging the item for re-review.

### Drift detection — what it watches, and what it does not

Drift detection tracks **source content** (per-source hash) and a **human review
cadence** (`review_state` / `reviewed_at`). It does **not** hash prose text. An
item's `statement` is an independent compact assertion, not a mirror of a prose
sentence, so ordinary wordsmithing — punctuation, phrasing, reflow — of a topic
file **must never raise a drift flag.** `researchLocation` is validated for
*existence* (the file/heading resolves), never for textual equality. This
directly answers the concern that cosmetic edits would otherwise generate noise.

## 12. Context compiler

The context compiler is the main AI-facing outcome.

Input:

- Ancestor.
- Task terms or explicit research-item/entity IDs.
- Requested relation types.
- Budget.
- Optional mode: `grounding`, `research`, `audit`, or `exhaustive`.

Output:

1. Current conclusions relevant to the task.
2. Direct source evidence and research findings.
3. Relevant analysis and hypotheses.
4. Supporting, contradicting, qualifying, and dependency items.
5. Source IDs and exact locators.
6. Related research units available for expansion.
7. Coverage ledger:
   - considered,
   - included compactly,
   - expanded,
   - omitted with reason.
8. Staleness or review warnings.

The compiler must not quietly truncate. If the requested subgraph exceeds the
budget, it should preserve all research-item IDs and short statements, then
omit detail in a declared order:

1. Long evidence excerpts.
2. Context-only items.
3. Low-bearing related entities.
4. Full source citations already addressable by `sourceId`.

Conflicts, negative-result limitations, and omitted-coverage notices may not be
dropped to meet budget.

## 13. Representative queries

The first evaluation suite must include:

1. What establishes John's earliest Weymouth presence?
2. What supports and opposes Candidate B?
3. Which same-name John Gurneys have been eliminated, and why?
4. What is the Grizzell/Cheny/Girny conflict?
5. Which findings depend on the East Dereham baptism?
6. Which published G13 statements would change if an earlier colonial record
   were found?
7. Which negative searches concern Anderson's "Boston" attribution, and what
   were their coverage limits?
8. Which dump findings, analyses, hypotheses, and leads remain unassimilated?
9. Return a complete G13 coverage ledger without expanding all prose.

## 14. Graph-editing artifact contract

Allen expects Claude (**Opus 4.8**) to build a crisp artifact for graph viewing,
navigation, and editing. It is an authoring tool; the public website remains
read-only.

**Storage model:** the artifact reads and **writes the canonical SQLite database
directly.** There is no JSON export/import in the edit path and no intermediate
file representation of an edit. This is the deliberate simplification adopted
2026-07-03 (see §1, §6); it is also *simpler* to build than the rejected
JSON-round-trip design, not just preferred.

The artifact must:

- Use direct SQLite reads/writes for fast viewing, filtering, navigation, and
  in-context editing.
- Display an item with its sources, incoming/outgoing relations, evidentiary
  provenance, research location, status, confidence, and publication impact.
- Navigate person, place, source, topic, and research-item neighborhoods.
- Filter by item kind, status, confidence, unresolved conflict, source,
  research unit, and publication impact.

**Save semantics (direct-to-DB, transactional):**

- On Save: validate the proposed change; if valid, apply it to the DB in a
  **single transaction**; on any failure, roll back so the DB is never left
  partially edited.
- Write an `item_revisions` row for every accepted change
  (create/update/supersede/review), capturing before/after state — the in-model
  audit trail (§10).
- Show a **human-readable before/after diff** (computed from current DB state vs.
  the proposed change) *before* committing. This replaces the old git-JSON-diff
  review, which no longer applies.
- Never lose an accepted edit: an accepted, validated change commits to the DB
  transactionally; a later failure in a *derived* step (FTS reindex, export)
  marks the derived artifact stale but does not roll back the content edit.
- Offer, and on a cadence or on demand **trigger, an export snapshot** so the
  canonical DB has a committed backup. Prompt for an export when uncommitted
  changes accumulate past a threshold.

**Editing constraints:**

- Validate before saving; preserve stable IDs; allow a source connection only
  from a registered `sourceId` (autocomplete from `data/sources.json`).
- Mark items stale on **source drift** (§11); never on cosmetic prose edits.
- Provide pick lists for item kind, relation type, source role, confidence,
  review state, date precision, and date-envelope semantics; entity/source
  autocomplete; field validation; undo/discard; duplicate warnings; batch
  accept/reject; and contextual views of paragraph, footnote, source excerpt,
  and relationships.
- Treat initial machine extraction as a review queue with states such as
  `machine_suggested`, `human_reviewed`, `needs_revision`, `rejected`,
  `superseded`.
- Support multiple-choice guided review for common decisions (merge/split
  entity, direct/collective source alignment, relationship type, confidence).

**History/audit:** provided by `item_revisions` plus committed export snapshots —
not by a second invented history store and not by git blame of per-item files.

Suggested interface boundary:

```text
artifact  <->  canonical SQLite (direct read/write, transactional saves)
                     |
                     +--> in-model item_revisions   (audit trail)
                     +--> export snapshot on cadence (backup, committed to git/OneDrive)
                     +--> static website exports     (read-only, later)
```

**Runtime.** The artifact needs real database/filesystem access, so it is not a
static browser page. Target a small **local backend** (Python, reusing the repo
`.venv`) that owns the SQLite connection, validation, and export, with a browser
UI for the database-like experience — or an equivalent local host with the same
guarantees. Final runtime is confirmed at Phase G4; the read/write contract
above is fixed now.

## 15. Testing and acceptance

### Correctness

- Every returned item traces to a committed definition, research location, and
  evidentiary provenance where required.
- Every source link resolves to an existing `sourceId`.
- Same-name candidates remain distinct unless an explicit reviewed relation
  connects them.
- Conflicts remain visible.
- Negative results retain scope.
- Schema builds deterministically; a DB → export → restore cycle round-trips the
  exact same logical content.

### Retrieval

- The representative queries return all items in a manually prepared gold set.
- An exhaustive context request accounts for every active item.
- No item disappears merely because semantic similarity is low.
- Compact grounding is materially smaller than loading the current companion
  and related files.

### Safety

- Building, querying, or exporting the graph changes no prose or source file.
- Artifact edits require validation and are logged to `item_revisions`.
- A failed migration/import leaves the prior DB intact, or is recoverable from
  the latest export snapshot; destructive operations refuse to run without a
  current export.
- Deleting the live cache loses no committed export snapshot and no prose.

### Independent review

After Codex delivers plumbing (schema, seed loader, exporter/restore, validator,
context compiler), Opus 4.8 performs a separate code review and functional test
drive — on top of Codex's own tests — before dependent phases proceed. See §18.

### Performance

At G13 scale, correctness dominates latency. A local query target below one
second is reasonable, but no architectural complexity should be added solely
to improve already-interactive response times.

## 16. Implementation phases

Owners in brackets (see §18). Each Codex plumbing deliverable is followed by an
Opus review + test drive before dependent phases proceed. **Phase P is an early
pilot gate** that cuts a thin slice through the whole stack before the full
plumbing is built. Plumbing precedes bulk item-authoring because items are DB
rows that need the schema first — the pilot is the deliberate exception that
validates the approach cheaply.

### Phase G0 — Contract  [Opus]

- Finalize IDs, controlled vocabularies, schema versioning, staging paths, and
  the export/backup format.
- Prepare 10–15 reviewed items covering source evidence, finding, analysis,
  hypothesis, conflict, collective evidence, negative result, and project impact,
  as the seed/test fixture.
- Hand-label the expected-answer (gold) set for the §13 representative queries;
  retrieval acceptance (§15) is measured against it, so it must exist before G2.

### Phase P — Colonial-arrival vertical slice (pilot gate)  [Opus authors; Codex minimal harness]

Before committing to the full G1–G5 build, prove the two hardest questions on one
domain. Author the colonial-arrival topic prose **and** its ~6 research items
(the mock set G13-E001 / N002 / E003 / A006 / F004 / S005), load them via `seed`
into a minimal DB, and run one context-compiler query. Codex builds only a
**minimal schema/seed/one-query harness** here — a thin cut through G1–G2, not the
full plumbing. This is **touch #1 of the real work, not a throwaway**: the content
survives into the package.

**Gate — proceed to full G1–G5 only if:**

- Co-authoring prose + items in one pass is sustainable in practice, and
- The resulting context package is materially smaller than, and as complete as,
  loading the current companion for the same task.

If the gate fails, stop at the topic refactor and source/citation improvements
(consistent with §17) rather than expanding graph machinery.

### Phase G1 — Database  [Codex builds → Opus reviews]

- Implement schema + migrations, seed loader, exporter/restore, validation,
  build report, and basic queries.
- Enforce integrity via DB constraints; keep the graph isolated from
  `repo_search` behavior.
- **Opus review + test drive** of G1 before G2 proceeds.

### Phase G2 — Context compiler  [Codex builds → Opus reviews]

- Implement relationship expansion, budget handling, and coverage ledger.
- Evaluate against the representative queries (§13) and the gold set.
- **Opus review + test drive** of G2 before G3/G4 proceed.

### Phase G3 — Research integration  [Opus]

- Populate research items alongside the staged topical refactor — prose and items
  **co-authored per topic, one pass** (avoids double-reading the material).
- Add source and publication impact mappings.

### Phase G4 — Artifact  [Opus builds; Fable UI polish after the contract is met]

- Build the editing/navigational artifact against the §14 contract (direct
  SQLite, transactional saves, in-model revisions, export-on-cadence).
- Validate round-trip edits, revision logging, and export/restore behavior.

### Phase G5 — Static export  [Codex builds → Opus reviews]

- Export finding pages/JSON and adjacency slices for the later graph-enhanced
  website.

## 17. Go/no-go criteria

The **first** gate is Phase P (§16): do not build the full G1–G5 plumbing unless
the colonial-arrival pilot slice shows sustainable co-authoring and a materially
smaller, complete context package.

Proceed beyond the G13 pilot only if:

- Context packages materially reduce grounding size.
- Finding/evidence/source alignment is reliable, including collective soft
  relationships.
- Maintenance effort is acceptable during real research intake.
- The graph improves impact analysis and coverage assurance.
- Allen can comfortably inspect and correct the graph through the artifact.

If those tests fail, retain the topic refactor and source/citation improvements
without expanding graph usage.

## 18. Model and tool assignments

Matched to where errors are cheap (deterministic, machine-checkable) versus
expensive (judgment, corpus-corrupting).

| Work | Owner | Status | Rationale |
|---|---|---|---|
| Graph plumbing — schema, migrations, seed loader, exporter/restore, validator, context compiler, static export (§10–13, §15) | **Codex GPT-5** | Locked | Deterministic, testable Python; integrity is machine-checkable; cheapest tool for well-specified plumbing. |
| Graph-editing artifact core — architecture + transactional save/validate/diff/export path (§14) | **Opus 4.8** | Locked | Correctness-critical software touching the canonical store. |
| Research synthesis — dump/companion inventory, classification, routing, topic synthesis, research-item authoring (Plan 02 §7–9, §11; Phase G3) | **Opus 4.8** | Recommended | Judgment- and repo-knowledge-heavy; a wrong disambiguation (e.g. Cheny/Girny) is expensive and hard to reverse. |
| Mechanical passes — coverage-ledger rows from a frozen inventory, stub/manifest generation, link/footnote validation runs, artifact UI polish after the contract is fixed | **Fable 5** | Recommended | Well-specified, low-judgment work against a frozen spec; conserve scarce Fable for exactly this. |

Locked assignments reflect Allen's decision (2026-07-03). Recommended assignments
are the default unless Allen redirects per task.

### Review and test-drive protocol

Codex tests its own plumbing. **On top of that**, after each Codex deliverable
(G1, G2, G5), Opus 4.8 performs an independent code review and functional test
drive before dependent phases proceed:

- **Review:** schema/constraint correctness, integrity enforcement, validator
  coverage, drift semantics (no prose hashing), export/restore losslessness,
  isolation from `repo_search`.
- **Test drive:** seed → validate → query/compile → export → restore round-trip
  on the Phase G0 fixture; representative queries (§13) against the gold set;
  confirm the backup-refusal guard fires when no current export exists.
- Findings are returned to Codex for correction, or accepted with noted
  follow-ups. A phase advances only after Opus sign-off.
