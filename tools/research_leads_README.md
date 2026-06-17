# Research Leads Tool Draft

Draft files:

- `tools/research_leads.py`
- optional companion doc: `tools/research_leads_README.md` or `tools/research-leads/README.md`

This is a draft implementation for `gurney-genealogy`. It does not change the canonical data model: `research/future-research/research-leads.csv` remains the open lead catalog, and `research/future-research/research-leads-done.csv` remains a thin close-out archive.

---

## AI quick contract

Use this tool instead of reading or rewriting the full lead CSV for single-lead work.

Most common commands:

```bash
python tools/research_leads.py context L-115
python tools/research_leads.py priority
python tools/research_leads.py priority --include-unknown
python tools/research_leads.py priority --brief
python tools/research_leads.py get L-115 --format json --warnings
python tools/research_leads.py update L-115 --status Partial --dry-run
python tools/research_leads.py close L-115 --disposition "Resolved; companion updated." --dry-run
python tools/research_leads.py validate
```

Operational rules:

1. For priority research, start with `priority`; it defaults to top 10 `Online=Y|Part` leads, excludes known physical/offline `Online=N` leads, and returns tight source/description context for selection. Use `--brief` for one-line output.
2. Use `context L-123` before pursuing a lead; it returns the lead plus the pre-pull checklist.
3. Use `--dry-run` before any write unless the user explicitly asks for direct mutation.
4. `Status` should normally be `Open` or `Partial`. Do not append long research narratives to `Status`; put findings in the companion/case file.
5. `close` writes only a thin done-row. Its output returns the full original lead as a cautionary reminder; promote any facts/findings to research files before relying on close-out.
6. Commas and quotes in free text are allowed because Python `csv` handles them, but the tool warns. Line breaks are blocked by default because multi-line CSV cells are hostile to manual review.

---

## Human documentation

## Purpose

The lead catalog has grown large enough that AI assistants may waste tokens by reading or rewriting the entire CSV for simple operations. This tool keeps the CSV canonical but exposes small operations by lead ID, priority, online availability, and status.

It is intentionally conservative:

- no external Python dependencies;
- no SQLite or new canonical store;
- preserves unknown/manual columns when rewriting;
- uses `csv.DictReader` / `csv.DictWriter` for robust comma/quote handling;
- emits warnings for risky or overlong fields;
- creates timestamped backups by default on writes;
- supports `--dry-run` diffs for safe review.

## Installation

Place the script at:

```text
tools/research_leads.py
```

Optional: place this README at either:

```text
tools/research_leads_README.md
```

or:

```text
tools/research-leads/README.md
```

The script uses only the Python standard library. It should run with the repo's existing Python environment.

## Canonical files

Defaults are repository-relative:

```text
research/future-research/research-leads.csv
research/future-research/research-leads-done.csv
```

The tool finds the repo root by walking upward from the current directory and script location. You can override paths:

```bash
python tools/research_leads.py --repo-root C:\Users\allen\OneDrive\Documents\GitHub\gurney-genealogy priority
python tools/research_leads.py --leads path/to/research-leads.csv get L-115
python tools/research_leads.py --leads open.csv --done done.csv validate
```

## Read commands

### Get one lead

```bash
python tools/research_leads.py get L-115
python tools/research_leads.py get 115 --format json
python tools/research_leads.py get L-115 --warnings
```

`115` is normalized to `L-115`.

### Get AI context for one lead

```bash
python tools/research_leads.py context L-115
```

Returns the lead plus the pre-pull checklist:

- check whether the source is already held;
- check the companion named in `Source ref`;
- pursue only the delta;
- promote findings before close-out.

### List/filter leads

```bash
python tools/research_leads.py list
python tools/research_leads.py list --online-reachable --min-priority 60
python tools/research_leads.py list --online Y --online Part --status Open --limit 20
python tools/research_leads.py list --gen G13 --fields ID,Priority,Subject,Online,Status
```

Rows are sorted by descending priority, then by numeric lead ID.

### Priority triage

```bash
python tools/research_leads.py priority
```

Default behavior:

- returns top 10 leads;
- includes `Online=Y` and `Online=Part`;
- excludes `Online=N` physical/offline leads;
- excludes `Online=Unk` unless requested;
- includes `Status=Open` and `Status=Partial`, including legacy free-form values that begin with `Open` or `Partial`.

Useful variants:

```bash
python tools/research_leads.py priority --limit 25
python tools/research_leads.py priority --include-unknown
python tools/research_leads.py priority --include-offline
python tools/research_leads.py priority --brief
python tools/research_leads.py priority --min-priority 70
python tools/research_leads.py priority --format markdown
python tools/research_leads.py get-priority
python tools/research_leads.py top
```


Default `priority` output is more informative than the generic compact list. It includes ID, priority, generation, online status, status, subject, source, a truncated description, and source reference. This gives an AI enough context to choose a lead without loading the full CSV. Use `--brief` when token minimization is more important than selection context.

### Search

```bash
python tools/research_leads.py search Spelman
python tools/research_leads.py search "Great Ellingham" --limit 10
```

Searches `ID`, `Gen`, `Subject`, `Lead/Source`, `Description`, `Status`, and `Source ref`.

### Validate

```bash
python tools/research_leads.py validate
python tools/research_leads.py validate --format json
```

Validation emits warnings for:

- duplicate IDs;
- malformed IDs;
- missing required columns;
- bad priorities;
- bad `Online` values;
- non-standard `Status` values;
- long fields and long rows;
- extra cells, often caused by unquoted manual commas;
- IDs appearing in both open and done CSVs;
- missing expected done CSV columns.

By default validation exits `0` even when warnings exist, because this repo already has some pre-existing free-form status values. Use `--fail-on-warnings` if you want warnings to return exit code `1`.

```bash
python tools/research_leads.py validate --fail-on-warnings
```

## Write commands

All write commands support:

```bash
--dry-run        # print unified diff, do not write
--no-backup      # skip timestamped .bak backup
--allow-multiline # allow line breaks in fields; not recommended
--format json
```

Backups are enabled by default for writes.

### Add a lead

```bash
python tools/research_leads.py add \
  --priority 70 \
  --gen G13 \
  --subject "John Gurney emigrant" \
  --lead-source "Example record series" \
  --description "Would test X by checking Y." \
  --online Y \
  --source-ref "research/people/g13-john-gurney-fact-sheet.research.md" \
  --dry-run
```

The tool assigns the next `L-` ID unless `--id` is supplied.

### Update a lead

```bash
python tools/research_leads.py update L-115 --online Part --status Partial --dry-run
python tools/research_leads.py update L-115 --priority 65 --dry-run
python tools/research_leads.py update L-115 --source-ref research/people/g15-henry-gurney-fact-sheet.research.md --dry-run
```

`--append-status-note` exists for compatibility with existing free-form `Status`, but should be used sparingly:

```bash
python tools/research_leads.py update L-115 --append-status-note "Checked index; original still needed." --dry-run
```

The tool warns when `Status` becomes long or non-standard. It does not block pre-existing free-form status values.

### Close a lead

```bash
python tools/research_leads.py close L-115 \
  --disposition "Resolved; companion updated 2026-06-17." \
  --dry-run
```

Close behavior:

1. removes the row from `research-leads.csv`;
2. appends a thin row to `research-leads-done.csv` with `ID`, `Subject`, `Disposition`, `Date`, and `Source ref`;
3. prints a caution that facts/findings must be recorded in research files;
4. prints the full original lead entry in the command output, but does not store that full narrative in the done CSV.

The caution is deliberate:

```text
Caution: Record any facts and findings from the lead entry into the appropriate research file before relying on close-out; lead entry content is not retained in done status.
```

## Free-text and character handling

CSV can safely encode commas and quotes when written through `csv.writer`. The tool therefore allows them, but warns because they increase manual-edit risk.

Default behavior:

| Character/value | Behavior |
|---|---|
| Comma | Allowed, warning emitted |
| Double quote | Allowed, warning emitted |
| Tab | Allowed, warning emitted |
| Newline / carriage return | Blocked unless `--allow-multiline` |
| NUL byte | Blocked |
| Long field | Allowed, warning emitted |
| Long row | Allowed, warning emitted |

This is a compromise: it does not reject historically valid CSV content, but it discourages changes that make the catalog harder to review manually.

## Status handling

The recommended statuses for new writes are:

```text
Open
Partial
```

The tool recognizes that existing rows may already contain richer free-form status text. It does not fail validation for that condition; it emits warnings. For new edits, prefer:

- `Status = Open` for live, unworked leads;
- `Status = Partial` for leads with some work remaining;
- narrative detail in the companion/case file, not the CSV.

## Output formats

Most read commands support:

```bash
--format compact
--format markdown
--format json
--format csv
```

For AI agents, use `--format json` when a downstream mechanical step depends on exact field values. Use default Markdown/compact when the result is for human review.

## Known implementation tradeoffs

- The tool rewrites the CSV through Python's `csv` module. This may normalize optional quoting even on rows that were not semantically changed.
- It preserves unknown columns, but it does not preserve comments or custom formatting outside valid CSV rows.
- It is not a database and does not handle concurrent writers. Use Git discipline for conflict review.
- It intentionally keeps `research-leads.csv` canonical; no generated index is created by this draft.

## Suggested repo-level integration changes

These are not included in the draft artifacts because they modify existing repo files.

1. **Add the tool file**
   - New file: `tools/research_leads.py`.

2. **Add or place this README**
   - New file option: `tools/research_leads_README.md`.
   - Alternative new subdirectory option: `tools/research-leads/README.md`.

3. **Update `AGENTS.md`**
   - Add a short instruction under efficiency or future-research guidance:

   ```markdown
   For `research/future-research/research-leads.csv`, do not read or rewrite the full CSV for single-lead work. Use `python tools/research_leads.py context L-123`, `priority`, `update`, or `close` instead. Read the full CSV only for broad catalog audits or schema changes.
   ```

4. **Update `research/future-research/README.md`**
   - Add a short "Tooling" section documenting common commands.
   - Clarify that `Status` should remain concise (`Open` / `Partial` preferred), with narrative findings promoted to companion/case files.

5. **Update `tools/README.md`**
   - Add one bullet for `research_leads.py` as the lead-catalog CLI.

6. **Optional future generated index**
   - Add a later command or separate tool to generate compact read-only indexes, for example:
     - `data/indexes/research-leads-by-id.json`
     - `data/indexes/research-leads-high-priority.md`
   - Do this only if the CSV grows enough that `priority` / `context` are insufficient.

7. **Optional test fixture**
   - New folder: `tools/tests/fixtures/`.
   - Add small sample lead CSVs for validation of commas, quotes, bad IDs, duplicate IDs, long fields, and close-out behavior.

## Minimal acceptance test

From repo root:

```bash
python tools/research_leads.py validate
python tools/research_leads.py priority --limit 10
python tools/research_leads.py context L-115
python tools/research_leads.py update L-115 --status Partial --dry-run
python tools/research_leads.py close L-115 --disposition "Test close; do not apply." --dry-run
```

Expected:

- `validate` may warn about existing long/free-form rows but should not crash;
- `priority` should exclude `Online=N` leads by default;
- `context` should return one lead plus pre-pull checklist;
- `update --dry-run` should print a diff and not write;
- `close --dry-run` should print open/done diffs and the caution with the original lead entry.
