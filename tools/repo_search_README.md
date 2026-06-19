# Repository search tool

`repo_search.py` performs comprehensive local repository retrieval while
keeping raw result volume out of an AI conversation. It is AI-agnostic and
specific to this repository's ancestors, places, topics, sources, research,
leads, citations, corpus files, and intake history.

## Core guarantee

Search and presentation are separate:

- Git and ripgrep define the exact lexical search inventory.
- SQLite FTS5 accelerates section retrieval and ranking.
- Every grouped result is saved to `all-results.jsonl`.
- Every exact matching line is saved to `exact-matches.jsonl`.
- Readable Markdown volumes contain the strongest/direct results plus a
  diverse partial-match sample.
- The manifest always states how many results were found, staged, and shown.
- A stale index may affect speed or ranking, but cannot silently erase the
  independent ripgrep ledger.

The cache lives outside OneDrive at:

```text
%USERPROFILE%\GitDirs\gurney-genealogy-search-cache
```

Override with `GURNEY_REPO_SEARCH_CACHE`.

## Common commands

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --ancestor G13 --terms Tyng Braintree leasehold

.\.venv\Scripts\python.exe tools\repo_search.py search `
  --place "Great Ellingham" --terms "pre-Lovell" Gurnay

.\.venv\Scripts\python.exe tools\repo_search.py search `
  --source dg-rec-pt2 --terms Filby Cobald

.\.venv\Scripts\python.exe tools\repo_search.py search --lead L-138
.\.venv\Scripts\python.exe tools\repo_search.py map --ancestor G5
```

Entity selectors disambiguate identity. An ambiguous ancestor name stops and
lists generation choices; textual searching across names remains available by
putting the name in `--terms` instead.

## Reading saved results

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py runs
.\.venv\Scripts\python.exe tools\repo_search.py resume <search-id>
.\.venv\Scripts\python.exe tools\repo_search.py expand <search-id> --volume 01
.\.venv\Scripts\python.exe tools\repo_search.py expand <search-id> --results 1 4 8
```

The manifest is the handoff point between agents or threads. For identity,
chronology, source-evidence, or negative-result conclusions, read all
applicable volumes or inspect the exhaustive ledgers.

## Variants

Curated variants live in `data/search-variants.json`.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py variants list
.\.venv\Scripts\python.exe tools\repo_search.py variants show surname-gurney
.\.venv\Scripts\python.exe tools\repo_search.py variants test surname-gurney --profile broad
.\.venv\Scripts\python.exe tools\repo_search.py variants validate
```

Profiles:

- `none`: explicit terms only.
- `conservative`: attested forms suitable for normal expansion.
- `broad`: OCR, transcription, scribal, and noisier forms.

Multiword names are expanded as names (`John Gurney` to `John Gurnay`), not as
bare surname sweeps. Place aliases remain canonical in `place-ids.csv`.

## Index maintenance

Every search refreshes changed files automatically.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py index --status
.\.venv\Scripts\python.exe tools\repo_search.py index --check
.\.venv\Scripts\python.exe tools\repo_search.py index --update
.\.venv\Scripts\python.exe tools\repo_search.py index --rebuild
```

`--check` exits nonzero when the machine-local index is stale. It does not
alter canonical repository content.

Saved runs are retained for 90 days:

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py clean
```

## Repository behavior

- `site/`, `.claude/`, `.codex/`, and `tools/` are excluded from normal
  genealogy retrieval.
- Tracked and relevant untracked text files are included.
- Binary media is excluded; textual media sidecars are indexed.
- Live leads are retrieved through `research_leads.py`, not by independently
  reimplementing the lead catalog.
- Intake history is searched but staged separately.
- Markdown footnotes referenced by a result are attached in full.
- Source IDs are retained for source-object navigation.
- Daniel Gurney page markers and Supplement pagination warnings are preserved.

See `tools/repo_search_DESIGN.md` for the full architecture and
`tools/repo_search_TEST_PLAN.md` for comparative evaluation.
