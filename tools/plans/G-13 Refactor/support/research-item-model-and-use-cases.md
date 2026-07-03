# Research-item model and mocked use cases

This file captures the concrete examples used to design the finding/source
layer, date model, analysis type, and AI context behavior.

> **Note (2026-07-03):** The JSON blocks below illustrate the **shape and fields
> of a research-item record** — the columns/attributes persisted as **rows in the
> canonical SQLite graph.** They are *not* canonical on-disk JSON files.
> Structured graph content is stored in the database and edited through the
> artifact; see Plan 01 §1, §6, §14. The data model shown here is unchanged by
> that storage decision.

## 1. Missing middle

Current conceptual flow:

```text
source record ----------------> citation embedded in prose
```

Proposed flow:

```text
source -> source evidence -> finding/analysis -> project statement
                      \-> conflict/hypothesis/open question
```

`data/sources.json` answers: What is this source?

Research-item records answer: What does the project believe the evidence
establishes, how was it analyzed, how strongly, and with what opposition or
limitation?

Research prose answers: How do the evidence and reasoning fit together?

Fact sheets and case files answer: What is durable enough to publish, and in
what narrative form?

## 2. Mock research items

### G13-E001 — June 1641 source evidence

```json
{
  "id": "G13-E001",
  "kind": "source_evidence",
  "subjectEntityId": "ancestor-g13-john-gurney-1",
  "statement": "John Gurney was associated with Weymouth by 2 June 1641, when the Massachusetts General Court remitted his gunpowder fine.",
  "dateEnvelope": {
    "plausibleStart": "1641-06-02",
    "plausibleEnd": "1641-06-02",
    "probableStart": "1641-06-02",
    "probableEnd": "1641-06-02",
    "precision": "day"
  },
  "status": "active",
  "assessmentConfidence": {"label": "high", "value": 0.98},
  "transcriptionConfidence": 0.99,
  "researchLocation": {
    "path": "research/people/_staging/g13-john-gurney/topics/colonial/01-arrival-chronology.md",
    "headingId": "june-1641-record"
  },
  "sourceLinks": [
    {
      "sourceId": "massachusetts-bay-records-v1-1853",
      "role": "supports",
      "locator": "volume 1, page 331",
      "alignmentNote": "Supports presence by this date; does not establish arrival year."
    }
  ],
  "supports": ["G13-F004"]
}
```

`researchLocation` is where the item is explained. The source link supplies
evidentiary provenance.

### G13-N002 — 1636 bounded negative result

```json
{
  "id": "G13-N002",
  "kind": "negative_result",
  "statement": "John is absent from the reviewed 1636 Weymouth property list.",
  "status": "active",
  "negativeStrength": "bounded",
  "coverageLimitations": [
    "The list is not proof of every resident.",
    "Absence supports an arrival bound but does not prove absence from every Weymouth record."
  ],
  "supports": ["G13-F004"]
}
```

### G13-E003 — Weymouth-parcel source evidence

```json
{
  "id": "G13-E003",
  "kind": "source_evidence",
  "statement": "Three Weymouth parcels were recorded as first granted to John and were in later holders' hands by the c.1643 possession compilation.",
  "status": "active",
  "assessmentConfidence": {"label": "high", "value": 0.95},
  "sourceLinks": [
    {"sourceId": "weymouth-land-grants-book-ms", "role": "supports", "locator": "manuscript pages 12, 23, 31"},
    {"sourceId": "nash-historical-sketch-weymouth-1885", "role": "supports", "locator": "pages 258, 270, 278, 281-282"}
  ],
  "supports": ["G13-F004"]
}
```

### G13-A006 — objective analysis

```json
{
  "id": "G13-A006",
  "kind": "analysis",
  "statement": "The 1636 property-list absence, June 1641 court appearance, and pre-1643 parcel history together create a bounded arrival window but do not identify an exact arrival year.",
  "status": "active",
  "analyzes": ["G13-E001", "G13-N002", "G13-E003"],
  "informs": ["G13-F004"],
  "promotesSpecificHypothesis": false
}
```

This is reasoning, not a hypothesis. It explains chronology and evidentiary
effect without proposing a particular identity or causal explanation.

### G13-F004 — arrival finding with two date ranges

```json
{
  "id": "G13-F004",
  "kind": "research_finding",
  "statement": "John plausibly arrived during 1636 to 1641, probably during 1638 to 1640, and lived at Weymouth before moving to Braintree.",
  "status": "active",
  "assessmentConfidence": {"label": "moderate-high", "value": 0.78},
  "dateEnvelope": {
    "plausibleStart": "1636",
    "plausibleEnd": "1641",
    "probableStart": "1638",
    "probableEnd": "1640",
    "precision": "year",
    "originalDisplay": "plausibly 1636-1641; probably 1638-1640"
  },
  "chronologyKey": {
    "value": 1639.0,
    "basis": "probable_midpoint",
    "manualOverride": false
  },
  "dependsOn": ["G13-E001", "G13-N002", "G13-E003", "G13-A006"],
  "tensions": ["G13-S005"],
  "publicationLinks": [
    {"path": "fact-sheets/g13-john-gurney-fact-sheet.md", "status": "published"},
    {"path": "research/case-files/john-gurney-case-file-v4.md", "status": "published"}
  ]
}
```

The outer range is plausible; the nested range is probable. `chronologyKey`
uses the probable midpoint solely to order timelines and lists. It must never be
displayed as though John arrived in 1639.

### G13-S005 — Anderson published-source statement

```json
{
  "id": "G13-S005",
  "kind": "published_source_statement",
  "statement": "Robert Charles Anderson assigns John an arrival year of 1636 and gives his English origin as unknown.",
  "status": "active-source-statement",
  "transcriptionConfidence": 0.99,
  "assessmentConfidence": null,
  "relations": [
    {
      "type": "QUALIFIES",
      "target": "G13-F004",
      "explanation": "The assigned year is in tension with the property-list reasoning but may not be a direct contradiction depending on list date and Anderson's basis."
    }
  ]
}
```

### G13-H001 — Candidate B identity hypothesis

```json
{
  "id": "G13-H001",
  "kind": "identity_hypothesis",
  "statement": "The Massachusetts John Gurney was the son of Francis Gurney and Margaret Rybett.",
  "status": "active",
  "assessmentConfidence": {
    "label": "probable",
    "value": 0.65,
    "basis": "Working rounded assessment, not a calculated probability."
  },
  "supportingItems": [
    "East Dereham source evidence",
    "Francis-Rybett household finding",
    "trade analysis",
    "migration/reception-network analysis"
  ],
  "opposingItems": [
    "1653 age tension",
    "absence of son Francis",
    "formal trade-admission negatives",
    "bounded John-Mary marriage negative",
    "remaining unknown-candidate space"
  ]
}
```

### G13-X008 — Grizzell evidence conflict

```json
{
  "id": "G13-X008",
  "kind": "evidence_conflict",
  "statement": "The traditional Grizzell Gurney marriage corresponds to a printed Braintree entry naming John Cheny, while manuscript evidence favors a Girny/Gurney reading.",
  "status": "unresolved-but-reweighted",
  "dependsOn": [
    "traditional published-source statements",
    "1886 printed Braintree reading",
    "Braintree manuscript image reading",
    "Pope head-form evidence"
  ],
  "openQuestion": "Whether the remaining letterform evidence warrants final resolution."
}
```

## 3. Soft evidence group

If one paragraph contains four facts and its footnote cites three sources
collectively, preserve that uncertainty:

```text
Finding 1 --\
Finding 2 ---- supported collectively by Evidence Group EG17
Finding 3 ----                                  |
Finding 4 --/                                   +-- Source A
                                                +-- Source B
                                                +-- Source C
```

Do not fabricate individual fact-to-source assignments. Later review can split
the collective group into direct links.

## 4. Mock use case — Weymouth grounding

Request:

> Research John's earliest Weymouth presence and whether his land implies
> residence.

Compact context:

```text
CURRENT FINDING
John plausibly arrived during 1636-1641, probably during 1638-1640. His three
parcels were granted before the c.1643 possession compilation and had passed to
later holders by that compilation.

DIRECT RESEARCH ITEMS
G13-E001 — June 1641 gunpowder record. Source evidence.
G13-N002 — Absent from reviewed 1636 property list. Bounded negative.
G13-E003 — Three parcels first granted to John. Source evidence.
G13-A006 — The evidence establishes a window, not an exact year. Analysis.
G13-F004 — Plausible and probable arrival ranges. Finding.

TENSION
G13-S005 — Anderson assigns 1636; underlying basis unresolved.

NOT EXPANDED
Migration-association cluster; Buckinghamshire settler cohort; detailed
Richard Porter and James Ludden research.
```

Outcome: complete logical grounding in hundreds rather than thousands of
tokens, with exact routes to expand.

## 5. Mock use case — new 1638 record

New source evidence:

```text
G13-E009 — John appears in a Weymouth record dated September 1638.
```

Impact query:

```text
DIRECTLY AFFECTED
- G13-F004: revise the date envelope and derived chronology key.
- G13-E001: remains valid but is no longer earliest known record.
- G13-N002: remains compatible if the property list predates arrival.

PUBLICATION REVIEW
- G13 fact sheet "first recorded June 1641."
- Website chronology.
- Case-file migration discussion.

UNAFFECTED
- Candidate A elimination.
- Candidate D elimination.
- Grizzell conflict.
- Tyng lease chronology.
```

Outcome: conceptual dependencies identify stale statements even when wording
differs.

## 6. Mock use case — comprehensive review

Illustrative coverage output:

```text
Source evidence           82 items    9 collective alignments
Research findings         51 items    4 potentially stale
Analysis                  37 items    6 needing review
Identity hypotheses        8 items    5 residual candidates
Evidence conflicts        11 items    3 unresolved
Negative results          47 items   12 coverage-limited
Open questions            19 items    7 linked to live leads
Project statements        31 items    4 potentially stale
```

AI reads every compact research item, then expands unresolved,
low-confidence, publication-impacting, or task-relevant evidence. Comprehensive
means every item was accounted for, not that every prose sentence remained
simultaneously in context.

## 7. Website expression

Narrative:

> John probably arrived at Weymouth during 1638-1640, within a wider plausible
> window of 1636-1641. **Evidence: 4 findings**

The evidence marker later opens a static drawer showing related source
evidence, analysis, findings, external statements, citations, and
relationships. The graph therefore benefits AI, maintenance, and reader-facing
evidence navigation from the same validated research-item model.
