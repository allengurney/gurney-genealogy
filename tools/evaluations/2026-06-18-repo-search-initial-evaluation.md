# Initial `repo_search.py` evaluation — 2026-06-18

## Build under test

- Windows repository checkout with external GitDirs cache.
- Inventory: 827 normal-search text files after excluding `site/`, `.claude/`,
  `.codex/`, and `tools/`.
- Indexed sections: approximately 12,700 before final exclusion refresh.
- SQLite FTS5 word and trigram tables available.
- RapidFuzz 3.14.5 installed.

## B2 thick-ancestor targeted comparison

Query:

```text
G13 + Tyng + Braintree + leasehold; variants none
```

Equivalent direct ripgrep baseline:

| Measure | Direct ripgrep | `repo_search.py` |
|---|---:|---:|
| Exact matching lines | 913 | 913 |
| Files with exact matches | 120 | 120 |
| Immediate output characters | 414,431 | 3,486 manifest |
| Approx. immediate tokens (`chars / 4`) | 103,608 | 872 |
| Immediate-output reduction | — | 99.2% |
| Staged readable characters | — | 297,791 |
| Staged-output reduction vs. raw | — | 28.1% |
| Exhaustive grouped results retained | raw output only | 529 sections in `all-results.jsonl` |
| Exact ledger retained | raw output | 913 lines in `exact-matches.jsonl` |

Known decisive locations ranked first:

1. G13 companion, `Land and property records`.
2. G13 companion, Braintree/community section.
3. G13 fact sheet.
4. John Gurney case file.

The first implementation initially over-expanded the ancestor name and created
thousands of low-value results. The corrected behavior treats the resolved
ancestor as a scope/ranking signal when explicit search terms exist. Name
variants become full-name substitutions rather than bare-surname sweeps.

## B1 thin-ancestor map

Query:

```text
map --ancestor G5
```

Observed:

- 238 exact matching lines across 38 files.
- 210 grouped sections.
- 80 sections staged; all 210 retained.
- 3,738-character manifest.
- 20 readable volumes / 162,036 characters.
- Direct files represented: 2/2.
- G5 fact sheet and research companion ranked first.
- G4/G3 material appeared as supporting context rather than being silently
  conflated with G5.

This test identified and fixed a repository-data issue: several older
`ancestor-ids.csv` rows omit direct file paths. The resolver now supplements
the index using the canonical `gNN-` filename convention.

## B5 Daniel Gurney source search

Query:

```text
source dg-rec-pt2 + Filby + Cobald; variants none
```

Observed:

- Part II, printed p. 395 ranked first.
- The result retained `p. 395 (#435)` and exact lines.
- Great Ellingham's use of the passage ranked as supporting research.
- Live lead L-68 was retrieved through `research_leads.py`.
- Historical v96 material remained separately labeled.
- All referenced footnotes were attached.

## Ambiguity behavior

`--ancestor "Benjamin Gurney"` stopped and listed G9, G10, and G11 with
dates, directing the caller to requery by generation. No silent identity
selection occurred.

## Staleness lifecycle

A temporary new research file was added after indexing.

1. `index --check` returned nonzero and named the stale path.
2. Direct ripgrep found the unique token.
3. A normal search automatically indexed the file.
4. The manifest reported one changed file.
5. The exact and grouped ledgers each contained the new result.
6. The temporary file was removed and the index refreshed.

This confirms that index staleness is surfaced and normal searches self-heal.
Exact lexical accounting remains independent through ripgrep.

## Footnote and structure checks

- Unit test confirms Markdown footnote references attach their local
  definitions.
- Live B2 search reported 370/370 referenced footnotes attached.
- Live G5 map reported 230/230 attached.
- Daniel Gurney page-marker parsing passed.
- Oversized coherent result blocks are not split merely to meet pagination
  targets.

## Initial assessment

### Comprehensiveness

Strong for exact lexical retrieval: direct and tool exact line/file counts
matched on B2. Lower-ranked results remain available even when not staged.

### Precision

Strong after correcting entity-name expansion. Known decisive B2 and B5
locations ranked first. Broad one-term place/surname searches still produce
large exhaustive sets, but readable staging now limits that impact.

### Token efficiency

The primary objective is met for immediate AI ingestion: 99.2% reduction on
the heavy B2 baseline while preserving the complete local result package.

### Remaining evaluation work

- Run all benchmarks in `repo_search_TEST_PLAN.md` after normal use produces
  more representative queries.
- Tune source-object grouping beyond source IDs and associated paths.
- Improve HTML fact-sheet structural parsing so one page is not always one
  large section.
- Add explicit concept-coverage fields to JSONL for easier downstream audit.
- Measure conservative/broad variant precision across medieval and OCR-heavy
  corpora.
