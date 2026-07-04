# Plan 2a — Narrative-to-graph evidence markers and exploratory navigation

Status: approved design direction, revised 2026-07-04 after Opus review (see
"Revisions" below); implementation not started.

This plan extends:

- Plan 01's canonical SQLite research-item contract.
- Plan 02 §11's requirement that substantive prose map to research items.
- Plan 03's readable, static, non-graph research annex.
- Plan 04's evidence-marker and finding-drawer concept.

It does not replace any of those plans. It defines the missing bridge between
research prose and the graph, then carries that bridge into a reader experience
that supports non-linear exploration without exposing raw database machinery.

Decisions accepted 2026-07-03:

1. Markdown uses an invisible marker token; the site generates the visible
   Evidence link.
2. Markers attach to conceptual evidence clusters, normally about 3–8 per topic,
   rather than every factual sentence or only whole headings.
3. The visible link is the compact word **Evidence**. Counts and explanatory
   detail belong in its accessible label and opened view.

## Revisions (2026-07-04, Opus review)

These adjustments were made after the Phase G3 Braintree increment
(`03-braintree-community.md`, items `G13-RI-000008..000017`) and the G5 static
export were built and run. They refine the plan; they do not change its direction.

1. **Retire the coarse item-range comment when a topic gets markers.** Each staged
   topic currently opens with an HTML comment like `G13-RI-000008..000017 map
   somewhere into this topic`. Once a topic has markers, that comment is **removed**
   — markers become the passage→item map, so the mapping lives in exactly one place
   (SQLite), not two (comment + markers). See §3.1.
2. **Keep `contextual` membership genuinely exceptional.** Add a validator warning
   when a `contextual` marker member is already reachable by a single relation hop
   from the primary item — the relation graph already explains it. See §10.
3. **A marker is an additional anchor, not a re-home.** `primary_item_id` is a finer
   narrative anchor; it never replaces an item's `research_unit_id` assignment. See §3.2.
4. **Stage the build; defer the reader/editor surfaces.** Implement **M0–M3 only**
   now (canonical marker storage, validation, static `marker-bundles` export, and the
   Braintree authoring pilot). **Defer the editor Narrative-Markers surface (§9) and
   the reader drawer/pivot experience (M4–M5) until the topic-structured website
   (Plan 03) is actually being built** — otherwise the drawer JS is written against a
   site that does not yet exist. During G3, markers are authored **as each topic is
   written**, via the `author-batch` load path (`tools/g13_graph/authoring.py`),
   not through an editor UI. See §13.

## 1. Problem

The first G13 topic/graph increments co-authored prose and research items, but
their connection is currently coarse. For example,
`03-braintree-community.md` declares in one opening HTML comment that
`G13-RI-000008..000017` map somewhere into the topic, while every item points
back only to the topic file and its top-level heading.

That proves topic-level coverage but does not answer:

- Which sentence or paragraph expresses a particular finding?
- Which graph items should open from a particular passage?
- How can a reader distinguish an ordinary source footnote from a graph-based
  explanation of the project's reasoning?
- How can the site offer useful pivots through sources, places, people,
  questions, and conflicts without presenting a bewildering raw graph?
- How can the same design expand beyond G13 without making graph participation
  mandatory for every fact on the site?

The bridge must preserve the adopted source-of-truth boundaries:

- Markdown remains canonical for prose and exact narrative placement.
- SQLite remains canonical for structured graph content and relationships.
- `data/sources.json`, source artifacts, ancestor records, and place records
  remain canonical in their existing layers.
- Static website files remain derived.

## 2. Reader contract: footnotes and Evidence links

Footnotes and Evidence links coexist because they answer different questions.

### Footnote

> Where did this information come from?

The footnote provides the conventional citation, exact locator, source title,
and retrievable trail. The research annex remains complete and credible when
all graph JavaScript and exports are removed.

### Evidence link

> Why does the project believe this conclusion, and what supports, qualifies,
> or challenges it?

The Evidence view may show:

- The current finding or analysis expressed by the prose.
- Direct source-evidence items.
- Reasoning that connects source evidence to the finding.
- Conflicts, negative results, limitations, and supersession.
- Confidence and review state.
- Related questions and publication impact.
- Pivots to sources, places, people, events, and related research.

An Evidence view must not merely repeat the adjacent footnote. If a simple fact
has one source and the graph adds no reasoning, conflict, relationship, or
useful exploration, the footnote alone is sufficient. Markers are selective
explanatory affordances, not mandatory ornaments after every citation.

The annex landing page and the first marker's accessible help should explain:

> Footnotes identify sources. Evidence links explain how the sources support,
> qualify, or challenge the conclusion.

## 3. Canonical marker contract

### 3.1 Markdown owns placement

The topic file contains one stable marker token at the point where the supported
prose cluster ends:

```markdown
John continued to lease the Tyng farm until 1662.[^nps-clr][^suffolk-deeds]<!-- graph-marker: G13-PM-000003 -->
```

The token contains only a stable marker ID. It does **not** contain a
hand-maintained list of research-item IDs.

Placement semantics:

- After a clause: the marker applies to the immediately preceding clause.
- At sentence end: it applies to that sentence.
- At paragraph end: it applies to that paragraph or conceptual evidence cluster.
- In a table cell or list item: it applies to that cell or item.

Place the token after applicable footnote references and before the paragraph
break. Do not put graph markers in footnote definitions.

The token is invisible in ordinary Markdown rendering. The package/site
preprocessor replaces it with the reader-facing link only in graph-enabled
preview or package builds.

**Retire the coarse item-range comment.** A staged topic today opens with an
HTML comment naming the topic's item-ID range (e.g. `G13-RI-000008..000017 map
into this topic`). That comment proved topic-level coverage before markers
existed. Once a topic has markers, **remove it**: the markers are the passage→item
map, and keeping both invites a Markdown list drifting out of sync with SQLite.
The topic's HTML comment header may still carry the `topicId` and a one-line note,
but not a hand-maintained item list.

### 3.2 SQLite owns structured mapping

Add canonical graph tables conceptually equivalent to:

```sql
prose_markers(
  marker_id PRIMARY KEY,
  research_unit_id,
  primary_item_id,
  visibility,             -- repo_only | public | restricted
  status,                 -- active | suppressed | retired
  created_at,
  updated_at
);

prose_marker_items(
  marker_id,
  item_id,
  marker_role,            -- primary | expressed | contextual
  display_order,
  PRIMARY KEY(marker_id, item_id)
);

marker_revisions(
  revision_id PRIMARY KEY,
  marker_id,
  database_revision,
  changed_at,
  changed_by,
  change_kind,
  before_json,
  after_json
);
```

The exact DDL belongs in a reviewed migration. The required semantics are:

- One stable, kind-neutral marker ID.
- Exactly one primary item per active marker.
- Zero or more additional expressed/contextual items.
- Foreign keys to the research unit and research items.
- Transactional edits and an in-model audit trail.
- Inclusion in deterministic recovery exports and milestone snapshots.
- Explicit publication visibility.

`item_publications` should not be overloaded for this purpose. It records
publication impact or appearance; a prose marker identifies an exact narrative
expression and may group several items.

A marker is an **additional, finer narrative anchor** — it does not re-home an
item. `primary_item_id` never replaces an item's `research_unit_id` assignment;
an item still belongs to its research unit, and a marker points at the exact place
in that unit's prose where the item is expressed. A marker's primary/expressed
items should normally belong to the marker's `research_unit_id` (a cross-unit
item requires an explicit reviewed reason — see §10).

Initial IDs may use the G13 namespace (`G13-PM-000001`). The schema and tools
must not assume that only G13 can own markers.

### 3.3 Why the split is stable

- Moving or rewriting prose moves one short token with it.
- Reclassifying, adding, or removing graph items changes SQLite, not Markdown.
- Multiple items can support one narrative cluster.
- Markdown does not become a second graph database.
- SQLite does not need to store or hash prose text.
- Cosmetic prose changes do not create drift.

Markdown and SQLite still cannot share one transaction. Marker work therefore
uses the same topic-level cross-store checkpoint already required by Plan 02:
save prose, save graph changes transactionally, validate the marker bridge,
refresh recovery, and record the reviewed revision.

## 4. Marker granularity

Default to one marker per conceptual evidence cluster, normally 3–8 markers per
topic. This is a target band, not a quota.

Create a marker when the graph adds at least one of:

- Multi-source synthesis.
- Analysis connecting evidence to a conclusion.
- Material qualification or contradiction.
- Bounded negative evidence.
- Identity or chronology reasoning.
- A useful pivot to related people, places, sources, events, or questions.

Avoid:

- A marker after every factual sentence.
- One omnibus marker for an entire long topic.
- Repeating the same marker on every summary and detailed restatement.
- Mapping every indirectly related graph item into the marker itself.

Map items the prose directly expresses. Supporting and opposing items normally
arrive through graph relations. Use `contextual` marker membership only when the
relation graph cannot otherwise explain why the item belongs in the opened
view.

## 5. Non-linear reader exploration

The reader experience is an entry point plus pivots, **not a prescribed
hierarchy**. Humans should be able to follow the question that interests them:
from a finding to a source, from that source to another finding, onward to a
place, person, conflict, event, or open question, then back through their own
path.

### 5.1 Initial Evidence view

Open with a compact orientation:

- Current finding or analysis.
- Status and confidence.
- Direct support, qualification, and conflict.
- Sources and exact locators.
- Material limitations.

This is the comprehensible starting neighborhood, not the end of navigation.

### 5.2 Available pivots

Where public data exists, allow pivots to:

- Research items.
- Sources.
- People.
- Places.
- Events.
- Research topics/units.
- Conflicts and negative results.
- Open questions.
- Publication appearances.

Each pivot opens a reader-facing neighborhood, not a raw table row. Translate
relationship vocabulary:

- Supported by.
- Also supports.
- Qualified by.
- Conflicts with.
- Depends on.
- Superseded by.
- Rules out.
- Appears in.

### 5.3 Complexity control without enforced linearity

Use progressive disclosure rather than prohibiting exploration:

- Show the strongest 3–5 relationships in each category initially.
- Provide **View all** for the complete public neighborhood.
- Keep a simple breadcrumb/history stack of the reader's pivots.
- Preserve browser back/forward behavior.
- Give every item, marker bundle, source, place, and person a permanent URL when
  it has a public page.
- Allow opening a pivot in a new tab.
- Keep search available from the expanded evidence experience.

A visual node-link graph is not the default reader interface. It may be tested
later as an optional view, but lists, grouped relationships, history, and
permanent pages deliver most of the non-linear value with less cognitive cost.

## 6. Sources, places, and people

The graph should enrich existing canonical pages rather than create competing
identity systems.

### Sources

A public source page may show:

- Human-readable bibliography.
- Public URL and artifact availability.
- Relevant locators and publishable excerpts.
- Findings that cite, qualify, or conflict through the source.
- People, places, and events connected through public items.

Publication rights and visibility govern whether an artifact or excerpt is
shown. Repository-only paths and restricted labels must not leak.

Footnote source titles may link to these pages. The same source reached through
an Evidence view lands on the same canonical page.

### Places

Graph pivots land on the existing canonical place page. That page may gain a
derived **Related research** section grouped by person, event, and finding.
Coordinates and place identity continue to come from the existing place data
layer.

### People

Ancestor and subject pages remain canonical. Graph-derived related findings,
sources, places, and conflicts appear as optional evidence/research sections,
not as replacement biographies.

This creates a reusable full-site pattern without requiring the whole site to
be graph-authored at once.

## 7. Exact prose range: single token versus paired tags

Paired start/end tags are not the default.

They would provide machine-explicit ranges but introduce:

- Mismatched or orphaned tags.
- Overlap and nesting rules.
- Fragility during prose revision.
- More complex Markdown parsing.
- Pressure to compare or hash prose text.

The marker's exact inline position already identifies the end of its scope, and
ordinary prose structure supplies the beginning. That is sufficient for a link
or button inserted after a clause, sentence, table cell, list item, or
paragraph.

Paired range tags may be reconsidered only if a later reader feature must
visually highlight the exact supported words or support overlapping markers
inside one sentence. That feature would require a separate design and must not
become mandatory for ordinary markers.

## 8. Generated static architecture

Extend the G5 static export with:

```text
markers.json
marker-bundles/<marker_id>.json
```

Generate permanent fallback pages:

```text
/research/evidence/g13-pm-000003/
/research/findings/g13-ri-000012/
```

The marker bundle page handles the important case where one prose cluster
expresses several items. The primary item remains its title/orientation; the
other expressed items and related evidence remain visible without JavaScript.

The topic-page build:

1. Scans Markdown for marker tokens.
2. Resolves each token through the static marker export.
3. Emits a normal hyperlink.
4. Adds `data-marker-id` for the drawer enhancement.
5. Leaves the surrounding prose and footnotes unchanged.

The visible text is **Evidence**. Its accessible name may include generated
counts, for example:

> Evidence for this statement: 2 findings and 4 sources

Counts must include only public data. Do not expose hidden-item counts.

If graph enhancement is disabled, comments disappear and the complete
footnoted annex remains. Legacy mode remains byte-equivalent to its prior
behavior.

## 9. Authoring artifact additions

Add a Narrative Markers surface to the graph editor:

- List markers using the selected item.
- Create/edit/retire marker.
- Choose primary, expressed, and contextual items.
- Choose visibility.
- Preview generated Evidence summary and public-readiness state.
- Copy the exact Markdown token.
- Filter for active items that are unmapped and not `context-only`.
- Navigate from marker to research unit and all mapped items.
- Show marker revision history.

The editor does not directly rewrite Markdown. This preserves the explicit
cross-store checkpoint and prevents a database authoring action from silently
changing prose.

## 10. Validation

Marker validation must check:

- Every Markdown marker token exists in SQLite.
- Every active SQLite marker has exactly one Markdown token in its research unit.
- Marker IDs are unique.
- Research-unit path and heading resolve.
- Every marker has exactly one primary item.
- Every mapped item exists.
- Every primary/expressed item belongs to the same research unit, or carries an
  explicit reviewed cross-unit reason.
- Every substantive active item is mapped or explicitly `context-only`.
- **Warn (do not fail) when a `contextual` marker member is reachable by a single
  relation hop from the marker's primary item** — the relation graph already
  explains why it belongs in the opened view, so `contextual` membership is
  redundant there. Reserve `contextual` for items the relation graph cannot
  otherwise surface; this stops the escape hatch from accreting.
- Public markers map only to public items.
- Public marker exports contain no restricted/repo-only IDs, labels, counts, or
  relation endpoints.
- The marker's direct source-evidence items align with nearby footnote
  `Source ID`s, or a reviewed collective evidence group explains the mismatch.
- Broken footnote anchors still fail the ordinary citation validator.
- Cosmetic prose edits do not create graph drift.

Citation/source comparison should distinguish errors from review warnings:

- A direct source-evidence item whose source is absent from the prose citations
  is normally an error.
- An extra contextual source in a footnote is a warning for review, not an
  automatic failure.
- Collective paragraph/source alignment remains represented by evidence groups;
  the validator must not invent one-to-one edges.

## 11. Publication safety

- New markers default to `repo_only`.
- A public marker requires an explicit visibility decision.
- Every primary/expressed item in a public marker must be public.
- Evidence excerpts require their separate publishability flag.
- Only relationships with public endpoints are exported.
- Source pages expose only public metadata/artifacts.
- Place/person pivots expose only existing public pages and public graph items.
- If a marker is not public, the site emits no link and no hidden count; the
  footnoted prose remains intact.

Publication filtering must fail closed. Preview/package validation reports an
intended public marker that cannot be emitted; it must not silently publish a
partial and misleading bundle.

## 12. Braintree pilot

Pilot the contract on
`topics/colonial/03-braintree-community.md` before broader backfill:

| Prose cluster | Primary/expressed graph items |
|---|---|
| Residence and 1652/3 deposition | `G13-RI-000008`, `G13-RI-000010` |
| 1645 petition and primary-source question | `G13-RI-000009`, `G13-RI-000017` |
| Tyng tenancy and leasehold conclusion | `G13-RI-000011`, `G13-RI-000012` |
| Monatiquot freehold and property distinction | `G13-RI-000013`, `G13-RI-000014` |
| Community standing | `G13-RI-000015`, `G13-RI-000016` |

The opening summary repeats several conclusions already treated below. Leave it
without a marker during the pilot unless reader testing shows that an overview
bundle adds value rather than duplicate visual furniture.

## 13. Implementation sequence

### M0 — Contract and fixture

- Approve this plan.
- Freeze marker vocabulary, ID format, and DDL.
- Add synthetic marker fixtures and migration/recovery tests.

### M1 — Canonical storage and validation

- Add marker tables, constraints, revisions, and deterministic export/restore.
- Add topic-scoped marker validation (§10), including the `contextual`-redundancy
  warning.
- Extend the `author-batch` load path (`tools/g13_graph/authoring.py`) to accept
  `markers` / `marker_items` in a batch, so markers are authored **as each topic is
  written**, transactionally, alongside its items.
- **Deferred to Plan 03 build (not M1):** the editor Narrative-Markers surface
  (§9) and the reader drawer/pivot experience (M4–M5). During G3, markers are
  created through `author-batch`, not an editor UI (Revision 4).

### M2 — Braintree authoring pilot

- Create the five Braintree marker records.
- Place the five Markdown tokens.
- Verify footnote/source alignment.
- Review marker density and authoring friction.

### M3 — Static export and fallback

- Export marker bundles and public neighborhoods.
- Generate permanent marker and finding pages.
- Test visibility and restricted-data non-leakage.

> **M4–M5 are deferred until the Plan 03 topic-structured website is being built**
> (Revision 4). The marker *data* (M0–M3) and per-topic authoring proceed now; the
> reader-facing JavaScript below is designed and built against the real site, not
> ahead of it.

### M4 — Annex preview experience

- Replace tokens only in graph-enabled preview.
- Add the accessible Evidence link, drawer/bottom sheet, history stack, and
  public pivots.
- Test no-JavaScript fallback, browser navigation, keyboard use, and mobile
  behavior.

### M5 — Evaluation and bounded expansion

- Test with general readers.
- Decide whether the opening-summary marker adds value.
- Evaluate source, place, and person pivots.
- Backfill additional G13 topics only after the Braintree pilot passes.
- Consider other ancestors only after G13 demonstrates sustainable authoring
  and reader value.

## 14. Acceptance criteria

The design succeeds when:

- A reader understands the difference between a footnote and Evidence link.
- The annex remains complete with graph enhancement removed.
- A marker opens the exact conceptual evidence cluster intended by the author.
- Readers can pivot non-linearly through public findings, sources, places,
  people, conflicts, and questions without encountering raw database terms.
- Back/forward navigation and permanent URLs preserve exploratory context.
- The first view is comprehensible without preventing deeper traversal.
- Marker authoring does not duplicate item lists in Markdown.
- Marker and graph edits remain transactional and recoverable.
- Prose wording changes do not create false drift.
- Public exports fail closed against restricted-data leakage.
- The Braintree topic remains readable and visually restrained.
- The architecture can later support other ancestors without requiring
  graph participation for every sourced fact.

## 15. Deferred questions

- Which source metadata and artifacts are safe and useful on public source pages?
- Should an optional visual graph explorer be offered after list-based
  navigation proves itself?
- At what scale should G13-specific graph storage become a broader repository
  graph, if ever?
- Should search span all public graph entities or remain scoped to the active
  research library?
- Is exact text highlighting valuable enough to justify optional paired range
  tags later?
