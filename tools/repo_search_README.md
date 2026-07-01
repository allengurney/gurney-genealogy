# Repository search tool

`repo_search.py` performs comprehensive local repository retrieval while
keeping raw result volume out of an AI conversation. It is AI-agnostic and
specific to this repository's ancestors, places, topics, sources, research,
leads, citations, corpus files, and intake history.

## Agent quickstart

Choose the command by task shape:

| Need | Use | Next step |
|---|---|---|
| Broad subject/source/place context | `search --ancestor G13 --terms ...`, `search --source <id> --terms ...`, or `map --ancestor/--place/--source ...` | Read the manifest, then `expand <search-id> --volume 01`. |
| Whole registered source package | `map --source <sourceId>` | Check corpus, validation, media, and citing-path results before source-evidence conclusions. |
| Go deep on one source file (corpus/transcript/OCR) | `infile <file> --terms ...` | Read the fuzzy, context-windowed passages; raise `--window`/lower `--threshold` to widen, `--exact` to tighten. |
| Exact edit anchor or known string | `locate "known string" --context 3` | Use the returned `path:line` for the edit block. |
| Scratch/tmp bulk triage | `locate <term> --path <dir> --context 1` | This searches live bytes outside the normal repo index. |
| Continue prior staged work | `runs`, then `resume <search-id>` or `expand <search-id> ...` | Avoid rerunning broad searches when a saved package already exists. |

Do not read `repo_search_DESIGN.md` for routine research. Use it only when
changing or auditing the search tool itself.

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

## Locate (exact `path:line`) and scratch triage

`search`/`map` rank *sections*; when you need the **exact `path:line`** of a known
string (e.g. to build an edit), use `locate`. It is a live ripgrep wrapper that
reuses the same text-extension and excluded-path filters, so it is the sanctioned
replacement for raw `grep` on repo content.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py locate '"rye-feet-of-fines-norfolk": {'
.\.venv\Scripts\python.exe tools\repo_search.py locate corpusPath --context 2   # ±2 verbatim lines
```

`--regex` (default is fixed-string), `--word`, `--case-sensitive` (default smart-case),
`--glob` (repeatable), `--max` (default 200; `0` = unlimited). Paths print
repo-relative with forward slashes.

**Scratch/tmp triage (`--path <dir>`):** point `locate` at a scratch directory to
triage a bulk download for just the hits you need instead of reading the whole blob
into context. It searches the directory **live** — ripgrep reads current bytes, so
results are always fresh (no persistent tmp index to stale, nothing to coordinate
across tools, no "files just landed" race), and scratch content never appears in a
normal repo search.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py locate Gurnay --path $env:TEMP\bulk --context 1
```

## Deep-read one file (`infile`)

`infile` searches **within named file(s)** instead of the whole repo, and returns
**fuzzy, context-windowed passages** rather than bare `path:line` rows. Use it to go
deeper on a single source — a corpus extract, an intake transcript, a freshly OCR'd
text — where you want to read the matching passages in context, not just locate a
string. It is the right tool when the file is the corpus you are mining.

```powershell
# Fuzzy is on by default; OCR-garbled and line-wrapped forms still surface.
.\.venv\Scripts\python.exe tools\repo_search.py infile `
  sources\corpus\daniel-gurney-part-2.md --terms Filby Harpley

# Search several files at once — and for a book too big to fetch inline, download its full text to scratch and infile it rather than making repeated partial web fetches.
.\.venv\Scripts\python.exe tools\repo_search.py infile `
  sources\intake\new\pdfs\historicalsketch00nash_0.txt --terms Gurnay Gurney

# Tighten to literal hits only, or widen to catch worse OCR.
.\.venv\Scripts\python.exe tools\repo_search.py infile <file> --terms Gurnay --exact
.\.venv\Scripts\python.exe tools\repo_search.py infile <file> --terms Gurnay --threshold 72 --window 3
```

Targets may be repo-relative, cwd-relative, or absolute (a corpus file often lives in
`sources/intake/` or a scratch directory, outside the Git inventory); a directory
expands to the text files beneath it. Matching uses the same OCR-aware normalization as
the index (NFKC, case-fold, soft-hyphen and line-break repair); fuzzy scoring is
RapidFuzz `partial_ratio`.

Options: `--context/-C` (lines around each passage, default 3), `--window` (consecutive
lines joined per match test for wrapped phrases, default 2), `--threshold` (minimum fuzzy
score, default 80), `--no-fuzzy` / `--exact` (literal only), `--variants` +
`--name-variants` (optional curated term expansion, default off), `--max` (passages per
file, default 60). `infile` prints straight to stdout and saves no package, so — like
`locate` — it is lightweight and does not take the cache lock.

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

The approved surname registry organizes variants into three descriptive
families:

| Family | Generations | Record environment |
|---|---:|---|
| `Modern` | G1–G13 | Modern American, colonial, and Massachusetts |
| `English` | G14–G28 | Tudor and medieval English |
| `Norman` | G29–G37 | Norman, Old French, Latin, and charter sources |

The family data is stored in `nameVariantFamilies`. Ancestor searches infer the
family from the generation, and explicit searches support
`--name-variants modern|english|norman|all|none`, independently of the
`conservative` or `broad` expansion profile.

The complete conservative/broad review matrix is in
`tools/evaluations/2026-06-19-search-variants-review.md`.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py variants list
.\.venv\Scripts\python.exe tools\repo_search.py variants table
.\.venv\Scripts\python.exe tools\repo_search.py variants show modern
.\.venv\Scripts\python.exe tools\repo_search.py variants test norman --profile broad
.\.venv\Scripts\python.exe tools\repo_search.py variants validate
```

Profiles:

- `none`: explicit terms only.
- `conservative`: attested forms suitable for normal expansion.
- `broad`: all conservative forms plus OCR, transcription, scribal, rare, and
  collision-prone discovery forms.

`--name-variants auto` is the default. It selects `Modern` for G1–G13,
`English` for G14–G28, and `Norman` for G29–G37. Without `--ancestor`, `auto`
does not expand a surname; choose a family or `all` explicitly.

Multiword names are expanded as names (`John Gurney` to `John Gurnay`), not as
bare surname sweeps. Variant spellings use whole-token matching, territorial
forms such as `de Gournay` use phrase matching, and source-specific OCR forms
remain restricted to their configured corpus paths. Place aliases remain
canonical in `place-ids.csv`.

## Index maintenance

Every search refreshes changed files automatically.

`search`, `map`, `index`, and `clean` use a simple cache-level lock so that one
repo-search command owns the shared SQLite/package cache at a time. A second
command waits twelve times in 5-second intervals; if the lock is still present,
it exits with the lock path and the recorded command metadata. If the recorded
owner PID is no longer active, the next lock-taking command removes that stale
lock automatically and continues. Malformed locks and locks owned by active
processes are never removed automatically. `locate`,
`infile`, `runs`, `resume`, and `expand` stay lightweight and do not take this
queue lock.

Incremental refreshes key both FTS tables by the canonical section ID, so
changed-file deletion uses indexed SQLite `rowid` lookups rather than scanning
the full word and trigram tables. A modification-time-only change with identical
content updates file metadata without reparsing or rebuilding its sections.

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
