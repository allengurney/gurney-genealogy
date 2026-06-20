# `repo_search.py` Comprehensive Design

## 1. Objective

Build an AI-agnostic, repository-specific search system that:

- Searches comprehensively without flooding an AI context window.
- Uses local compute aggressively because it is inexpensive.
- Preserves every result locally; presentation limits never become search limits.
- Understands this repository's ancestor, place, topic, source, research, citation, corpus, and intake structures.
- Produces compact, structured output optimized for AI ingestion but readable by humans.
- Supports reliable follow-up expansion and auditable negative-result claims.
- Excludes `site/`.
- Runs well on Windows using `.\.venv\Scripts\python.exe`.

The central principle:

> Search broadly and losslessly; stage what enters context. Ranking determines reading order, not truth or permanent exclusion.

---

## 2. Core Architecture

```text
Repository files and structured indexes
                 |
                 v
       Inventory and object resolver
                 |
                 v
    Parser and incremental SQLite index
                 |
       +---------+----------+
       |                    |
       v                    v
 SQLite FTS5            ripgrep
 word + trigram         exact backstop
       |                    |
       +---------+----------+
                 |
                 v
  Variant expansion and result fusion
                 |
                 v
 Grouping, deduplication, source joining
                 |
                 v
 Complete saved search package
                 |
                 v
 Small manifest -> paged result volumes
```

A search always produces a complete local package. The terminal receives only the compact manifest and package path.

### V1 load-bearing invariants

The following are core functionality, not optional optimization:

- Structure-aware parsing and footnote attachment.
- Persistent saved packages with stable search IDs.
- Completeness accounting on every search.
- An exact ripgrep result ledger as the exhaustiveness backstop.
- SQLite as an accelerator whose state is refreshed and checked, never as the
  sole basis for a negative-result or completeness claim.

Every result must make subset status explicit, for example:

```text
Exact lexical matches: 284
Grouped result sections: 67
Sections staged in readable volumes: 24
Sections shown in this manifest: 12
Full result set: all-results.jsonl
Exact-match ledger: exact-matches.jsonl
Referenced footnotes attached: yes
```

---

## 3. Repository Object Model

The tool will classify results into repository-aware objects.

### Top-level objects

1. **Ancestors**
   - Canonical record.
   - Fact sheet.
   - Research companion.
   - Biography or case file when applicable.
   - Linked places.
   - Cited source objects.
   - Related topics.
   - Live leads.

2. **Places**
   - Canonical place record.
   - Place detail record.
   - Place research file.
   - Aliases from `place-ids.csv`.
   - Linked ancestors.
   - Relevant source objects and topics.

3. **Topics**
   - Topic research file.
   - Linked ancestors, places, sources, and leads.

4. **Sources**
   - `data/sources.json` inventory entry.
   - `source-ids.csv` locator.
   - Corpus extract.
   - Corpus supplement.
   - Validation.
   - Media directory and sidecars.
   - Files citing the source.
   - Daniel Gurney adapter where applicable.

5. **Research**
   - People.
   - Places.
   - Topics.
   - Case files.
   - Biography.
   - Fact sheets as publication peers.

### Second tier

6. **Live research leads**
   - Retrieved through `research_leads.py`.
   - Joined to their source-reference files.
   - Presented separately from established research.

### Historical/audit tier

7. **Intake and completed patchsets**
   - Searched by default.
   - Compressed into a distinct historical bucket.
   - Elevated when current research lacks the same finding, a staged item remains unapplied, or the query concerns provenance/history.

### Locator signals

8. **Filenames, paths, and headings**
   - Indexed and ranked strongly.
   - Used for discovery and classification.
   - Never treated as factual evidence by themselves.

---

## 4. Supported Commands

### `search`

Run exhaustive retrieval and create a saved package.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --ancestor G13 `
  --terms '"leasehold origin"' Tyng Braintree
```

Other examples:

```powershell
# Textual search across every generation
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --terms '"Benjamin Gurney"' probate

# Place-aware search
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --place "Great Ellingham" `
  --terms Gurnay will

# Source-aware search
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --source dg-rec-pt2 `
  --terms Filby Cobald

# Research-lead-aware search
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --lead L-138

# Exact phrase without automatic variants
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --terms '"Gvrney"' `
  --exact `
  --variants none
```

### `expand`

Read selected results or volumes from a saved package.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py expand <search-id> `
  --results 2 5 8

.\.venv\Scripts\python.exe tools\repo_search.py expand <search-id> `
  --volume 03

.\.venv\Scripts\python.exe tools\repo_search.py expand <search-id> `
  --file research/people/g13-john-gurney-fact-sheet.research.md `
  --section "Land and property records"
```

### `map`

Produce a compact repository map without requiring search terms.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py map --ancestor G13
.\.venv\Scripts\python.exe tools\repo_search.py map --place "Great Ellingham"
.\.venv\Scripts\python.exe tools\repo_search.py map --source dg-rec-pt2
```

### `index`

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py index --status
.\.venv\Scripts\python.exe tools\repo_search.py index --update
.\.venv\Scripts\python.exe tools\repo_search.py index --rebuild
.\.venv\Scripts\python.exe tools\repo_search.py index --check
```

Normal searches update stale files incrementally. Explicit rebuilding should rarely be necessary.

### `clean`

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py clean
.\.venv\Scripts\python.exe tools\repo_search.py clean --older-than 90
.\.venv\Scripts\python.exe tools\repo_search.py clean --all
```

Default retention: 90 days.

### `runs` and `resume`

List and reopen saved searches across threads:

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py runs
.\.venv\Scripts\python.exe tools\repo_search.py runs --limit 25
.\.venv\Scripts\python.exe tools\repo_search.py resume <search-id>
```

Search IDs are stable directory names containing a timestamp and query slug.
`runs` returns the ID, creation time, one-line query summary, resolved entity,
match counts, and package path. `resume` returns the saved manifest without
rerunning the search.

### `variants`

Initially read-only because canonical variants remain manually maintained.

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py variants list
.\.venv\Scripts\python.exe tools\repo_search.py variants show gurney
.\.venv\Scripts\python.exe tools\repo_search.py variants test Gurney --era medieval
.\.venv\Scripts\python.exe tools\repo_search.py variants validate
```

No automatic modification or suggestion-writing in v1.

---

## 5. Entity Resolution

### Ancestors

`data/indexes/ancestor-ids.csv` is authoritative.

Accepted selectors:

- `G13`
- `g13`
- Canonical record ID.
- Unique ancestor name.

Generation selectors resolve immediately.

An ambiguous name stops before searching:

```text
Ambiguous ancestor: Benjamin Gurney

G9   Benjamin Gurney (1730-1805)
G10  Benjamin Gurney (c.1704-1771)
G11  Benjamin Gurney (c.1676-1738)

Requery with --ancestor G9, G10, or G11.

To search the text across all generations, omit --ancestor:
  repo_search.py search --terms '"Benjamin Gurney"' probate
```

This prevents silent generational conflation.

### Places

Resolution uses:

- Canonical place ID.
- Canonical name.
- Filename.
- Aliases from `place-ids.csv`.
- RapidFuzz only for candidate resolution, not evidence retrieval.

Ambiguous place names similarly require selection.

### Sources

Resolution uses:

- `sourceId`.
- Short title.
- Corpus path.
- Validation path.
- Media path.
- Fuzzy title matching for interactive disambiguation.

### Leads

Lead lookup delegates to `research_leads.py`, preferably through an importable API introduced during implementation or its compact JSON CLI output.

The search tool must not duplicate lead-catalog parsing logic.

---

## 6. Search Semantics

### Terms

Quoted text means phrase search:

```text
--terms '"Clement Gurney"' testator
```

Unquoted terms use normalized lexical matching.

Default multi-term behavior:

- Results containing all concepts rank highest.
- Partial matches remain in a clearly labeled supporting bucket.
- No partial result is silently discarded.

Controls:

```text
--require-all
--any
--exact
--regex
--near 10
```

### Ancestor expansion

For `--ancestor G13`:

Automatically searched:

- Canonical ancestor name.
- Curated applicable name variants.
- Generation and record ID as repository locators.
- User-supplied terms.

Used as ranking signals:

- Paired fact sheet and companion.
- Biography/case-file mapping.
- Parents, spouse, children, and associated families.
- Linked places.
- Sources already cited by the ancestor files.
- Related topics.

Optional broadening:

```text
--expand-places
--expand-family
--expand-sources
```

An ancestor-only query is valid and behaves like an evidence-oriented map.
For `map --ancestor`, the package includes every section of the ancestor's
direct fact sheet, research companion, configured biography/case file, and
canonical record, plus deduplicated linked place, topic, source, and lead
objects. The completeness ledger distinguishes direct-entity coverage from
repository-wide textual matches.

### Place expansion

Automatically searched:

- Canonical name.
- Structured aliases.
- Place ID and research filename.

Linked ancestors rank higher but do not become automatic text terms unless requested.

### Variants

Profiles:

```text
--variants none
--variants conservative
--variants broad
```

Default: `conservative`.

- `none`: user terms only.
- `conservative`: attested spelling and language variants appropriate to context.
- `broad`: OCR, transcription confusion, typography, fragments, and noisier forms.

The manifest always records every expanded term.

### OCR handling

Default normalization:

- Unicode normalization.
- Case folding.
- Soft line-break and hyphenation repair.
- Whitespace normalization.
- Curly/straight punctuation equivalence.
- Ligature normalization where safe.

Broad OCR mode adds:

- Curated character confusions.
- Trigram retrieval.
- Prefix/fragment searches.
- Source-specific quirks.
- Era-appropriate surname variants.

No indiscriminate fuzzy match across every corpus token.

---

## 7. Variant Registry

Path:

```text
data/search-variants.json
```

Implemented shape:

```json
{
  "schemaVersion": 2,
  "nameVariantFamilies": [
    {
      "id": "modern",
      "label": "Modern",
      "kind": "surname",
      "generationRange": {"minimum": 1, "maximum": 13},
      "conservative": [
        {"term": "Gurney", "matchMode": "whole-token"}
      ],
      "broadAdditions": [
        {"term": "Gurnoe", "matchMode": "whole-token",
         "collisionWarning": "Frequently a distinct surname."}
      ]
    }
  ]
}
```

Three surname families are implemented:

- `Modern`, G1–G13.
- `English`, G14–G28.
- `Norman`, G29–G37.

`--name-variants auto` infers the family for ancestor searches. Raw searches
remain literal unless `modern`, `english`, `norman`, or `all` is explicitly
selected. The expansion profile remains independent:

- `conservative` uses the core family list.
- `broad` is cumulative and adds OCR, transcription, rare documentary, and
  collision-prone forms.
- `none` disables expansion.

Whole-token matching is the default for surname forms. Territorial names use
phrase matching. Source-specific OCR variants carry path restrictions, and
collision-prone forms emit manifest warnings.

Place variants remain authoritative in `place-ids.csv`; the new file should not duplicate them.

Source-specific OCR patterns such as Daniel Gurney's `Wilham` and `Basiha`
remain separate from surname families.

---

## 8. Index Design

Machine-local database and packages, outside the OneDrive working tree by
default:

```text
%USERPROFILE%/GitDirs/gurney-genealogy-search-cache/index/repo-search.sqlite3
```

The default may be overridden by configuration or `GURNEY_REPO_SEARCH_CACHE`.

### File inventory

Use:

```powershell
git ls-files -co --exclude-standard
```

Then apply repository exclusions:

- Exclude `site/`.
- Exclude `.git/`.
- Exclude `.search-cache/`.
- Exclude binary media content from textual indexing.
- Index textual sidecars and metadata associated with media.
- Exclude generated/transient files unless explicitly useful.
- Include relevant untracked files.

### SQLite tables

Conceptual schema:

```text
files
  id
  path
  layer
  object_type
  object_id
  source_id
  mtime
  size
  content_hash
  indexed_at

sections
  id
  file_id
  heading
  heading_path
  start_line
  end_line
  body
  normalized_body
  page_marker
  language_hint

footnotes
  id
  file_id
  footnote_key
  start_line
  end_line
  body
  source_ids

section_footnotes
  section_id
  footnote_id

relationships
  subject_type
  subject_id
  relation
  object_type
  object_id

search_runs
  search_id
  query_json
  created_at
  index_version
  package_path
```

### FTS indexes

1. Word-oriented FTS5:
   - Unicode tokenizer.
   - BM25 ranking.
   - Phrase, prefix, Boolean, and proximity search.

2. Trigram FTS5:
   - Partial terms.
   - OCR fragments.
   - Filename fragments.
   - Joined/split text.

3. Ripgrep backstop:
   - Exact literal and regex verification.
   - Negative-result auditing.
   - Index diagnostics.
   - Searches of unusual text not represented properly in FTS.

Before each search, the tool incrementally refreshes the SQLite index from the
Git-aware inventory. The exact ripgrep ledger is then generated independently
for the effective lexical terms. A stale or unavailable index may reduce
ranking quality or speed, but must not silently reduce exact-match
completeness.

---

## 9. Parsing

The parser recognizes:

- Markdown headings and hierarchy.
- Paragraph boundaries.
- Lists.
- Blockquotes.
- Fenced transcription blocks.
- Footnote references.
- Footnote definitions.
- Source IDs.
- HTML comments where useful.
- Daniel Gurney page markers.
- File-level metadata.
- CSV and JSON records through purpose-specific adapters.

The initial parser should be repository-specific and lightweight rather than a generalized Markdown engine.

### Footnotes

When a displayed passage references footnotes:

- Include every referenced footnote definition in full.
- Footnotes have a separate display allowance.
- Deduplicate repeated footnotes within a volume.
- Resolve any `Source ID:` through `source-ids.csv`.
- Report associated corpus, supplement, validation, and media paths.

Footnotes remain attached to the passage even if that causes a volume to exceed its normal pagination target.

---

## 10. Source Joining

A source should appear as one object rather than several independent results.

Example:

```text
Source object: dg-rec-pt2
Title: Daniel Gurney, Record, Part II

Inventory:
  data/sources.json

Corpus:
  sources/corpus/daniel-gurney-part-2.md

Validation:
  none

Media:
  none

Cited by:
  G14 companion
  G15 companion
  Great Ellingham place research

Matching passages:
  Part II, p. 412
  Part II, p. 438
```

Ranking should distinguish:

- A match in original corpus text.
- A match in inventory metadata.
- A match in validation.
- A citation to the source in research.
- A filename-only match.

These are related, but not evidentially equivalent.

---

## 11. Daniel Gurney Adapter

Dedicated source family:

```text
dg-rec-pt1
dg-rec-pt2
dg-rec-pt3
dg-rec-pt4
dg-supplement
```

Capabilities:

- Search all parts or selected parts.
- Preserve printed-page and scan markers.
- Return citations using printed page numbers.
- Recognize Part IV's mapped sections.
- Keep the Supplement separate.
- Flag any Supplement citation below page 725 as invalid.
- Use known OCR variants selectively:
  - `William` <-> `Wilham`
  - `Basilia` <-> `Basiha`
- Search French and Latin text without forcing English stemming.
- Group multiple matches on the same printed page.
- Avoid presenting a page-marker match as prose evidence.
- Report whether a hit came from:
  - 1848 Parts I-IV.
  - 1858 Supplement.
  - Preliminary/end matter.
- Leave an extension point for the unavailable Rye appendix.

Example:

```powershell
.\.venv\Scripts\python.exe tools\repo_search.py search `
  --source-family daniel-gurney `
  --ancestor G15 `
  --terms Basilia Attleborough
```

---

## 12. Ranking and Fusion

Ranking determines reading order only.

Signals include:

- Exact phrase match.
- All concepts present.
- Term proximity.
- Heading match.
- Filename match.
- Entity match.
- Ancestor's paired files.
- Linked place/source/topic.
- Current research over historical intake.
- Corpus evidence over metadata-only references.
- Footnote/source alignment.
- Distinct-source diversity.
- Variant distance from the explicit query.

### Diversity controls

The first result volume should not be monopolized by one large file.

It should attempt to include:

- The paired ancestor research.
- Published treatment where relevant.
- At least one source-side result.
- Relevant place/topic evidence.
- Conflicts or negative findings.
- A lead result when materially relevant.
- A historical result only when it adds distinct value.

### Historical intake

Historical results rank below current research by default but are elevated when:

- No current equivalent exists.
- The intake item is unprocessed or staged.
- The current file references the historical item.
- A discrepancy suggests an application gap.
- The query explicitly concerns provenance or prior work.

---

## 13. Saved Search Package

Default path:

```text
%USERPROFILE%/GitDirs/gurney-genealogy-search-cache/runs/<timestamp>-<slug>/
```

Files:

```text
00-manifest.md
01-core-results.md
02-supporting-results.md
03-source-and-corpus-results.md
04-leads.md
05-historical-audit-results.md
all-results.jsonl
exact-matches.jsonl
query.json
inventory.json
```

Volumes are created only when needed.

### Pagination

Target volume size: approximately 8,000-12,000 characters.

This is not a hard cap:

- Do not split a passage from its footnotes.
- Do not split one short Markdown section unnecessarily.
- Do not truncate the complete result collection.
- Large coherent units may exceed the target.

### Manifest

`00-manifest.md` should remain compact, ideally 2,000-5,000 characters.

It contains:

- Search ID and timestamp.
- Original query.
- Resolved ancestor/place/source.
- Expanded terms and variant profile.
- Layers searched.
- Match totals before and after grouping.
- Volume descriptions.
- Recommended reading order.
- Warnings and ambiguity.
- Negative-result requirements.
- Paths to exhaustive results.
- Exact lexical match count, grouped-section count, shown subset count, and
  attached-footnote status.
- Direct-entity completeness counts for `map` searches.

Example:

```text
Search completed: 284 matches across 37 files and 18 source objects.

Recommended:
1. Read 01-core-results.md.
2. Read 03-source-and-corpus-results.md before assessing source evidence.
3. Read 02-supporting-results.md before making an identity conclusion.

Optional:
4. Read 04-leads.md if planning future work.
5. Read 05-historical-audit-results.md only for intake gaps or provenance.

A negative-result conclusion requires reviewing volumes 01-05 or the
all-results manifest for applicable scopes.
```

### Noise control

Audit metadata should not dominate the manifest. Put detailed inventories in `inventory.json`.

The visible manifest needs only:

- Searched scopes.
- Important exclusions.
- Counts.
- Any failures or stale-index warning.

---

## 14. Output Formats

Default:

```text
--format ai
```

Other formats:

```text
--format human
--format json
--format jsonl
--format paths
```

`ai` is compact Markdown optimized for ingestion.

`human` adds slightly more explanation.

`json/jsonl` support mechanical follow-up and optional future rerankers.

`paths` returns only classified file/section locators.

---

## 15. Cache and Retention

Behavior:

- Incremental index retained indefinitely unless rebuilt.
- Search-run packages retained 90 days.
- Automatic cleanup can occur at startup no more than once per day.
- Never delete a package currently referenced by an active command.
- `clean --all` does not remove the canonical variant registry or repository files.
- Search packages contain no presigned URLs or intentionally sensitive credentials.
- Cache defaults outside OneDrive to avoid synchronization churn.

Storage should be modest because the indexed text corpus is only tens of megabytes.

---

## 16. Dependencies

### Required

- Python standard library.
- SQLite with FTS5.
- Git.
- ripgrep.

### Proposed third-party dependency

- RapidFuzz.

Before adding it:

- Confirm active maintenance.
- Pin it in `tools/requirements.txt`.
- Verify Windows wheel installation in `.venv`.
- Use only for bounded entity/heading/filename resolution.

### Deferred extension points

Interfaces but no implementation in v1:

```python
class SearchReranker(Protocol):
    def rerank(self, query, candidates): ...

class SemanticRetriever(Protocol):
    def search(self, query, scope): ...

class SearchSummarizer(Protocol):
    def summarize(self, result_group): ...
```

Possible future implementations:

- Claude Haiku reranker.
- Codex subagent.
- Local embedding model.
- `sqlite-vec`.
- QMD bridge.

Deterministic output must remain fully usable without them.

---

## 17. Configuration

Repository profile:

```text
tools/repo_search_config.json
```

Possible contents:

```json
{
  "schemaVersion": 1,
  "cacheRoot": "%USERPROFILE%/GitDirs/gurney-genealogy-search-cache",
  "excludedPaths": [
    "site/**",
    ".search-cache/**"
  ],
  "objectRoots": {
    "factSheets": "fact-sheets",
    "researchPeople": "research/people",
    "researchPlaces": "research/places",
    "researchTopics": "research/topics",
    "caseFiles": "research/case-files",
    "corpus": "sources/corpus",
    "corpusSupplement": "sources/corpus_supplement",
    "validations": "sources/validations",
    "media": "sources/media",
    "intake": "sources/intake"
  },
  "specialPublications": [
    {
      "id": "william-gurney-biography",
      "role": "biography",
      "path": "research/case-files/..."
    },
    {
      "id": "john-gurney-case-file",
      "role": "case-file",
      "path": "research/case-files/john-gurney-case-file-v4.md"
    }
  ],
  "cacheRetentionDays": 90
}
```

The exact biography path should be confirmed during implementation.

This keeps repository-specific knowledge visible and reviewable rather than hidden in Python conditionals.

---

## 18. Search Fidelity Guarantees

The tool should explicitly guarantee:

1. Display pagination does not restrict retrieval.
2. Every grouped result remains in `all-results.jsonl`; every exact lexical line remains in `exact-matches.jsonl`.
3. Ranking never proves absence.
4. Filename matches are locator evidence only.
5. Semantic extensions cannot suppress lexical results.
6. Variant expansion is recorded.
7. Negative conclusions require scope review.
8. Historical intake remains searchable.
9. Distinct source witnesses are not deduplicated into one evidentiary result.
10. Footnotes remain attached to displayed prose.
11. Ambiguous ancestors do not silently resolve.
12. Exact ripgrep verification remains available.

---

## 19. Testing Strategy

### Unit tests

- Ancestor resolution.
- Ambiguous repeated names.
- Place alias resolution.
- Source joining.
- Markdown heading parsing.
- Footnote attachment.
- Source-ID extraction.
- Variant filtering by profile and era.
- Daniel Gurney page parsing.
- Supplement page guard.
- Result deduplication.
- Pagination without footnote separation.
- Cache expiry.
- Site exclusion.
- Stable run listing and resume.
- Completeness-ledger arithmetic.
- Exact ripgrep ledger independence from SQLite.
- Whole-entity direct-file completeness.

### Fixture repository

Create small fixtures under:

```text
tools/tests/fixtures/repo-search/
```

Include:

- Two ancestors with the same name.
- One fact sheet and companion.
- One place with aliases.
- One source with corpus and validation.
- Duplicate intake and current-research findings.
- OCR variants.
- Footnotes.
- French text.
- Daniel Gurney-style page markers.

### Golden-result tests

Representative real queries:

- G13 + Braintree leasehold.
- Benjamin Gurney ambiguity.
- Great Ellingham + pre-Lovell Gurnay.
- Daniel Gurney + Basilia.
- A lead-ID query.
- A source-ID query.
- A query whose only result is historical intake.
- A negative exact search.
- OCR-broad search versus conservative search.

### Evaluation metrics

- Known decisive-file recall.
- Known decisive-passage recall.
- Source diversity in first volume.
- Raw output versus displayed output.
- Search-package completeness.
- False entity conflation.
- Variant noise.
- Number of expansion calls needed.
- Search/index runtime.

Target: at least 70% reduction in immediate context output while retaining 100% of known decisive files in the manifest or saved result set.

---

## 20. Implementation Phases

### Phase 1: Foundation

- CLI and configuration.
- Git-aware inventory.
- Exact ripgrep completeness ledger.
- Stable search IDs, `runs`, and `resume`.
- Saved-package output and completeness accounting.
- Markdown sections and footnotes.

### Phase 2: Indexed acceleration

- SQLite schema.
- Incremental indexing.
- Word-oriented FTS5.
- `search`, `expand`, `map`, `index`, and `clean`.

### Phase 3: Repository intelligence

- Ancestor resolution.
- Place resolution.
- Source-object joining.
- Lead-tool integration.
- Fact-sheet/companion relationships.
- Biography/case-file parity.
- Current versus historical classification.

### Phase 4: Retrieval quality

- Trigram index.
- RapidFuzz entity resolution.
- Variant registry.
- OCR profiles.
- Ranking fusion and diversity.
- Ripgrep verification.

### Phase 5: Specialized sources

- Daniel Gurney adapter.
- Page-aware corpus extraction.
- Supplement safeguards.
- French/Latin handling.
- Source-family search.

### Phase 6: Evaluation and tuning

- Real-query benchmark suite.
- Compare against direct `rg`.
- Adjust ranking weights.
- Validate token savings and recall.
- Update AI-facing documentation.

### Deferred Phase 7

- Optional LLM reranking.
- Optional semantic vectors.
- Optional subagent integration.
- No dependency on these for normal operation.

---

## 21. Documentation Changes During Implementation

Likely files:

- New `tools/repo_search.py`
- New `tools/repo_search_config.json`
- New `tools/repo_search_README.md`
- New `data/search-variants.json`
- New tests and fixtures
- Update `tools/requirements.txt`
- Update `tools/README.md`
- Add concise signposting to `AGENTS.md`

Proposed AGENTS.md guidance:

> For context-heavy repository discovery, use staged retrieval: let local tools search, rank, group, and deduplicate broadly; return compact locators or manifests first, then open the most relevant passages and widen as needed. Efficiency must not reduce required scope, suppress conflicting or negative evidence, or substitute ranking for verification.

And:

> For canonical ancestor, place, source, or record-ID lookup, search `data/indexes/` before opening the larger canonical JSON files. Use `tools/repo_search.py` for broad repository discovery and `tools/research_leads.py` for lead-catalog operations.
