# Graph-enhanced G13 website concept

Status: concept placeholder. Do not implement until the SQLite research-item contract,
topic refactor, non-graph annex, and graph-editing artifact are stable.

## 1. Concept

A sentence, clause, table row, or short prose cluster can display a restrained
evidence marker:

> John probably arrived at Weymouth between 1638 and early 1641.
> **Evidence: 4 findings**

Selecting the marker opens:

- A right-side drawer on desktop.
- A bottom sheet or full-height panel on mobile.
- A permanent ordinary finding page when JavaScript is unavailable.

The panel shows:

- The source evidence, finding, analysis, hypothesis, conflict, negative result,
  or project statement expressed by the prose.
- Kind shown in reader-friendly language.
- Status and confidence.
- Current equivalent of the footnote/source citation.
- Exact source locator and optional evidence excerpt.
- Supporting, contradicting, qualifying, dependency, and supersession
  relationships.
- Links to related research items.
- Link to the full research topic.
- Permanent finding URL.

## 2. Illustrative drawer

```text
Evidence

ARRIVAL AT WEYMOUTH

Current finding
John probably arrived between 1638 and early 1641.

Status: Active inference
Confidence: Moderate-high
Plausible range: 1636-1641
Probable range: 1638-1640

Supporting observations
  Confirmed — At Weymouth by 2 June 1641
  Bounded negative — Not in reviewed 1636 property list
  Confirmed — Original grantee of three pre-1643 parcels

Tension
  Anderson assigns arrival in 1636

Sources
  Massachusetts Bay Records, vol. 1, p. 331
  Weymouth Land Grants Book, pp. 12, 23, 31
  Nash, Historical Sketch, pp. 258–282

Related findings
  Weymouth residence
  Buckinghamshire settler cohort
  East Anglia migration hypothesis

Full research treatment | Permanent finding link
```

## 3. Static architecture

All data can be generated at build time:

```text
SQLite graph export
       |
       +--> /research/findings/G13-F004/index.html
       +--> /assets/findings/G13-F004.json
       +--> page-specific research-item manifest
       +--> optional G13 adjacency export
```

Small browser JavaScript:

1. Intercepts an evidence-marker click.
2. Loads embedded finding data or fetches static JSON.
3. Opens an accessible drawer/dialog.
4. Follows relationship links by loading another static research item.
5. Maintains a shareable URL or permanent-link escape hatch.

No database server, Cloudflare Worker, or runtime query API is required for
precomputed relationship navigation.

## 4. Progressive enhancement

Do not wrap whole paragraphs in links. Use a compact marker after the supported
clause, sentence, or cluster.

Every marker is also a normal hyperlink:

```html
<a class="evidence-link"
   href="/research/findings/G13-F004/"
   data-item-ids="G13-F004">
  Evidence: 4 findings
</a>
```

Without JavaScript, the reader reaches a complete static finding page.

## 5. Multiple research items

A sentence may express several findings or statements:

> John was a tailor who lived at Weymouth by 1641 and later leased the Tyng
> farm.

The marker can read:

> Evidence: 3 findings, 5 sources

The drawer separates:

1. Occupation.
2. Weymouth presence.
3. Tyng leasehold.

This is clearer than one omnibus footnote.

## 6. Public finding page

Each finding page should include:

- Stable ID and reader-facing title.
- Plain-language statement.
- Status, confidence, and qualifiers.
- Plausible and probable date ranges where applicable, plus project-revision
  date. The synthetic chronology key is never displayed as evidence.
- Sources with full citations and exact locators.
- Supporting/opposing/qualifying evidence, findings, and analyses.
- Superseded state where applicable.
- Research topic and publication appearances.
- Working-research disclaimer.

Finding pages provide:

- No-JavaScript fallback.
- Search and AI crawler visibility.
- Shareable citations.
- Browser back/forward behavior.
- A durable target for internal links.

## 7. Relationship navigation

Initial reader-facing labels:

- Supported by.
- Also supports.
- Qualified by.
- Conflicts with.
- Depends on.
- Superseded by.
- Rules out.
- Appears in.

Avoid exposing database vocabulary as unexplained uppercase edge names.

Selecting a related research item may replace the drawer contents while retaining a
simple breadcrumb/history stack.

## 8. Authoring artifact relationship

The Claude-built graph artifact is separate from the public website:

- Artifact: authenticated/local authoring, editing, validation, graph
  visualization, and Git diff.
- Website: read-only, static, restrained evidence navigation.

The website consumes validated static exports. It never writes graph data.

## 9. Deferred design questions

- Exact marker visual language.
- Whether markers replace, supplement, or coexist with numbered footnotes.
- Drawer history and deep-link URL behavior.
- Whether confidence is shown numerically, verbally, or both.
- Whether evidence excerpts are public by default.
- Whether some findings or analyses remain private/repository-only.
- Whether a visual graph explorer adds enough value beyond relationship lists.
- How finding revision history should appear to public readers.
- How to prevent evidence markers from overwhelming ordinary narrative.

## 10. Constraint for future design

The graph-enhanced experience must remain optional. Removing its JavaScript and
JSON must leave a complete, readable, navigable static research annex with
ordinary citations.
