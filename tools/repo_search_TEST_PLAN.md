# `repo_search.py` Comparative Test Plan

## Purpose

Evaluate whether the tool improves context efficiency without reducing
research comprehensiveness, evidence precision, citation fidelity, or
functional reliability.

The evaluation compares:

1. Direct repository search using ripgrep and manual file reads.
2. `repo_search.py` manifest plus staged volumes.
3. The tool's exhaustive `all-results.jsonl` and `exact-matches.jsonl`.

## Success criteria

### Comprehensiveness

- 100% of known decisive files appear in `all-results.jsonl`.
- 100% of direct entity files appear for `map`.
- Every exact ripgrep matching line appears in `exact-matches.jsonl`.
- The tool reports every searched and excluded scope.
- Historical intake remains discoverable when it contains the only match.
- Ambiguous ancestors never resolve silently.

### Precision and reading order

- At least 80% of benchmark-designated decisive sections appear in the first
  manifest or first applicable volume.
- At least one current research/publication result and one source-side result
  appear early when both exist.
- Historical patchsets do not displace stronger current research unless they
  contain distinct evidence or an application gap.
- Filename-only matches are identified as locator signals, not evidence.

### Token and output efficiency

- Immediate command output is under 6,000 characters for normal searches.
- Staged readable output is at least 70% smaller than unbounded raw repository
  output for broad benchmarks.
- The first applicable volume is normally 8,000-12,000 characters, except
  where preserving a complete section and its footnotes requires more.
- Full retrieval remains available on disk regardless of staged-output size.

For comparison, estimate tokens as both:

```text
characters / 4
```

and, when a tokenizer is available, the tokenizer's actual count.

### Citation and structure fidelity

- Every locally defined Markdown/HTML footnote referenced by a staged section
  is attached.
- Footnote text is not truncated.
- Source IDs remain visible and resolvable.
- Daniel Gurney results retain printed-page markers.
- Supplement page markers below 725 produce a warning.
- Distinct source witnesses are not collapsed into one evidentiary claim.

### Functionality and resilience

- Incremental refresh indexes only changed/added/removed files.
- `index --check` detects a changed file before refresh.
- Exact ripgrep retrieval still works after deleting/rebuilding SQLite.
- `runs`, `resume`, and `expand` work across new processes.
- Cache cleanup respects the 90-day policy.
- `site/` never appears in the inventory or results.
- Windows paths, Unicode, CRLF, and long files work.

## Benchmark matrix

### B1: Thin ancestor entity map

```powershell
repo_search.py map --ancestor G5
```

Expected:

- G5 fact sheet and companion complete.
- Related G4/G3 material ranked as supporting, not conflated.
- Relevant source sidecars visible.
- Output materially smaller than a broad `rg "Lester Sawyer Gurney"`.

### B2: Thick ancestor targeted search

```powershell
repo_search.py search --ancestor G13 --terms Tyng Braintree leasehold --variants none
```

Known decisive locations:

- G13 companion, `Land and property records`.
- G13 case file where Tyng/Braintree evidence is discussed.
- Relevant source/inventory objects.

Expected:

- These rank before generic John Gurney material.
- All partial matches remain in `all-results.jsonl`.
- Readable volumes do not expand every one-term background match.

### B3: Ambiguous repeated ancestor name

```powershell
repo_search.py search --ancestor "Benjamin Gurney" --terms probate
```

Expected: stop and list G9, G10, and G11 with dates.

### B4: Place-aware search

```powershell
repo_search.py search --place "Great Ellingham" --terms "pre-Lovell" Gurnay --variants none
```

Known decisive location:

- `research/places/great-ellingham.md`, structural significance section.

Expected:

- Canonical Great Ellingham resolves ahead of Old Hall.
- Place aliases are available.
- Current place research ranks ahead of historical patchsets.

### B5: Source-aware Daniel Gurney search

```powershell
repo_search.py search --source dg-rec-pt2 --terms Filby Cobald --variants none
```

Expected:

- Part II page 395 result.
- Printed-page marker retained.
- Source inventory record included as a direct object.
- Great Ellingham citation appears as supporting use.

### B6: Daniel Gurney OCR expansion

```powershell
repo_search.py search --source dg-rec-pt1 --terms Basilia --variants broad
```

Expected:

- Query records `Basiha` expansion.
- Both exact and OCR-expanded matches remain distinguishable.

### B7: Lead integration

```powershell
repo_search.py search --lead L-138
```

Expected:

- Live row comes from `research_leads.py`.
- Source-reference research and relevant corpus files appear.
- Raw lead CSV is not treated as an independently indexed prose corpus.

### B8: Historical-only match

Choose a unique phrase present only in `sources/intake/new/` or
`sources/intake/done/`.

Expected:

- Historical bucket reports it.
- Manifest labels the result as historical/audit.
- Exact ledger proves the current layers had no match.

### B9: Exact negative search

Use a deliberately impossible identifier.

Expected:

- Zero exact matches.
- Zero grouped sections unless a fuzzy/path signal genuinely applies.
- Inventory and exclusions remain stated.
- Negative conclusion remains conditioned on applicable variant/scope choices.

### B10: Filename/path locator

Search a distinctive filename fragment.

Expected:

- File is discoverable.
- Result clearly identifies path/heading signal.
- Filename match is not described as content evidence.

## Comparative procedure

For each benchmark:

1. Run a direct `rg` baseline with equivalent literal terms and exclusions.
2. Save raw baseline output to a temporary file; record characters, lines,
   files, runtime, and known decisive-file coverage.
3. Run `repo_search.py`.
4. Record:
   - command-output characters;
   - manifest characters;
   - staged-volume characters;
   - exhaustive JSONL characters;
   - exact lines/files;
   - grouped/staged/shown counts;
   - runtime and incremental-index changes.
5. Check every known decisive file and passage.
6. Review the first manifest and first applicable volume for precision.
7. Confirm lower-ranked baseline matches remain addressable in JSONL.
8. Record false positives, false negatives, ranking problems, and footnote
   attachment errors.

## Staleness and backstop tests

1. Build a fresh index.
2. Modify a fixture file without running search.
3. Confirm `index --check` reports stale.
4. Run search and confirm automatic refresh.
5. Confirm the new exact match appears in both ledgers.
6. Delete the SQLite database.
7. Re-run search; confirm reconstruction and matching results.
8. Compare exact-match ledger hashes before and after rebuild.

## Regression tests

Run:

```powershell
.\.venv\Scripts\python.exe -m unittest tools.tests.test_repo_search
.\.venv\Scripts\python.exe tools\repo_search.py variants validate
.\.venv\Scripts\python.exe tools\repo_search.py variants table
.\.venv\Scripts\python.exe tools\repo_search.py index --check
```

Variant boundary and behavior checks:

- G13 auto-selects `Modern`; G14 and G28 select `English`; G29 and G37 select
  `Norman`.
- A raw search with `--name-variants auto` remains literal.
- `broad` contains the conservative family plus its broad additions.
- Whole-token `Gurne` does not match `Gurney`.
- Phrase forms such as `de Gournay` remain intact.
- Collision-prone forms produce manifest warnings.
- Daniel Gurney OCR variants are retrieved only from configured source paths.

Also run normal repository validation after implementation:

```powershell
Set-Location site\website
npm.cmd run validate
```

The website build does not depend on the machine-local search cache. Search
freshness belongs to repository-search and intake/research closeout workflows,
not public-site generation.

## Evaluation report

Record final results in a dated file under `tools/evaluations/` containing:

- Tool version/commit.
- Corpus inventory and index statistics.
- Benchmark table.
- Recall and early-precision observations.
- Character/token comparisons.
- Runtime and cache size.
- Footnote/source fidelity.
- Known limitations.
- Recommended ranking/variant adjustments.
