---
name: research-intake-session-processor
description: Process one genealogy intake session from sources/intake/new/, inspect files, extract text or OCR as needed, triage relevance, normalize filenames, update data/sources.json, create validation notes, and add new research intake to the appropriate research markdown files.
argument-hint: [path to intake session markdown file]
disable-model-invocation: true
---

Use this skill to process one genealogy intake session file in `sources/intake/new/`.

The purpose is to convert raw source captures into tracked, traceable research with the least practical friction while preserving reversibility.

This skill is designed for:
- screenshot snippets
- clipped images
- PDFs
- saved source files
- quick source captures with URL and optional notes, questions, or ancestor names

## Core principles

1. Preserve traceability to the original captured file and source URL.
2. Get useful research into the relevant research markdown file with low friction.
3. Track every retained research item in `data/sources.json`.
4. Use the standard citation process already defined for this repo.
5. Keep all intake-derived additions easy to review, refine, move, or delete later.
6. Do not bypass source tracking.

## Expected intake layout

- `sources/intake/new/v01.md`
- `sources/intake/new/v02.md`
- `sources/intake/new/v03.md`

Referenced files are typically stored in the same `sources/intake/new/` folder.

Processed outputs:
- `sources/intake/processed/`
- `sources/intake/archive/`
- `sources/media/...`
- `sources/validations/...`
- `research/...`
- `data/sources.json`

## Session file assumptions

The intake session file is freeform.

The only required structural assumption is:
- entries are separated by `---`

An entry may contain any combination of:
- URL
- file name
- ancestor name
- place
- topic
- question
- notes
- observations
- pasted text
- freeform narrative

Use `freeform-intake-guidance.md` when interpreting entries.

A formal mini-template is allowed but not required.

## Read before starting

1. Read `.claude/CLAUDE.md`
2. Read `.claude/rules/citations.md`
3. Read:
   - `.claude/rules/data-json.md`
   - `.claude/rules/research-people.md`
   - `.claude/rules/research-places.md`
   - `.claude/rules/research-topics.md`
   - `.claude/rules/research-case-files.md`
   - `.claude/rules/sources-validations.md`
4. Read the citation skill:
   - `.claude/skills/citation-rigour/SKILL.md`
   - `.claude/skills/citation-rigour/checklist.md`
   - `.claude/skills/citation-rigour/footnote-template.md`
5. Read this skill’s support files

## What this skill does

For each intake entry:

1. Parse the freeform entry.
2. Identify the referenced file or infer the best candidate file when unambiguous.
3. Inspect the file.
4. Extract text directly when possible.
5. OCR when needed.
6. Evaluate the result using `decision-rules.md`.
7. Assign one triage outcome:
   - `promote`
   - `hold-review`
   - `duplicate`
   - `reject`
8. For retained items, reconcile source tracking in `data/sources.json`:
   - match an existing source entry, or
   - create a new compliant source entry
9. For promoted items:
   - create a normalized human-readable file copy under `sources/media/`
   - save OCR/extracted text beside it when useful
   - create a thin validation note in `sources/validations/`
   - add concise new research intake content to the best-fit research markdown file using the standard citation process
10. For `hold-review` items:
   - create or update source tracking in `data/sources.json` when enough metadata exists to do so compliantly
   - record the item in the processed report
   - create a validation note when useful
11. For `duplicate` items:
   - map to the existing source entry where possible
   - identify the overlap in the processed report
12. For `reject` items:
   - record the reason in the processed report
13. Write a processed report for the full session.
14. Archive the original session bundle.
15. Create the next blank intake session file in `sources/intake/new/`.

## JSON source tracking is mandatory

No research content should be added to a research markdown file unless it has an applicable `data/sources.json` entry.

This means:
- if an existing source entry fits, use it
- if no existing entry fits, create a new compliant entry
- if a compliant entry cannot yet be created because the source cannot be identified adequately, do not promote the item into research; keep it as `hold-review`

This rule is mandatory.

Follow `sources-json-requirements.md`.

## Citation behavior

This skill must use the repo’s standard citation process.

Do not invent a separate intake citation style.

When inserting research:
- follow `.claude/rules/citations.md`
- follow the citation skill guidance
- use nearby footnotes tied closely to the supported fact or finding
- avoid abbreviations unless already established and still human-readable
- include URL when available
- include multiple sources when the claim depends on multiple sources

## Research insertion behavior

Do not add a large custom “provisional workflow” wrapper.

Instead:
- add ordinary research content in the appropriate research file
- use a simple heading such as:
  - `## New research intake`
  - `### Intake new research — {short title}`
- keep the insertion concise and useful
- include normal citation footnotes
- preserve quiet machine traceability using HTML comment markers only

Use `research-insertion-pattern.md`.

## Destination and naming policy

For promoted files:
- preserve the original raw file in the archived session bundle
- create a normalized working copy under `sources/media/`
- use concise, human-readable, lowercase hyphenated filenames

Naming pattern:
- `{principal-subject}-{document-type}-{source-short}-{year}`

Examples:
- `william-gurney-obituary-nyt-1870.png`
- `john-gurney-parish-register-dereham-1611.jpg`

## Choosing the research destination

Use the best-fit destination:

- person-specific finding → `research/people/...`
- place-specific finding → `research/places/...`
- cross-cutting issue → `research/topics/...`
- contested identity or argument-heavy issue → `research/case-files/...`

If no good destination exists:
- create a new research file only when confidence is good and the item is clearly worth retaining
- otherwise use `hold-review`

## Triage outcomes

### `promote`
Use when text extraction or visual reading was sufficiently successful and the item can be meaningfully connected to current research.

### `hold-review`
Use when:
- text extraction was not successful enough
- identification was not successful enough
- relevance is plausible but too uncertain
- the item may matter but should not yet be inserted into research markdown

### `duplicate`
Use when the item materially overlaps an already tracked source artifact or research item.

### `reject`
Use when the item is outside scope, accidental, or too weak to retain.

Follow `decision-rules.md`.

## Validation-note policy

Each promoted item should get a thin validation note under `sources/validations/`.

The note should capture:
- intake session
- original file name
- normalized file name
- URL
- extraction/OCR method
- sourceId used or created
- destination research file(s)
- unresolved issues

## Processed report

For each session create:
- `sources/intake/processed/vNN.processed.md`

Include:
- summary counts by outcome
- promoted items
- hold-review items
- duplicates
- rejects
- source entries created or matched
- any manual follow-up needed
- any failures

Do not skip entries silently.

## Archive and rollover

After processing:
- archive the original session markdown file and original raw files under `sources/intake/archive/vNN/`
- create the next blank session file in `sources/intake/new/`

Example:
- processed `v07.md`
- archive bundle at `sources/intake/archive/v07/`
- next blank file created: `sources/intake/new/v08.md`

## Default boundaries

### Allowed by default
- OCR and text extraction
- normalized media copies
- OCR sidecar text files
- validation-note creation
- research markdown insertion
- `data/sources.json` updates
- processed report creation
- archive creation
- next blank session file creation

### Not allowed by default
- fact-sheet edits
- broad narrative rewrites
- silent deletion of archive originals
- silent skipping of failed entries

## Success condition

A session is successful when:
- every intake entry has been processed
- every retained research item is source-tracked in `data/sources.json`
- promoted items have stable filenames and traceable locations
- useful research has been added to the correct research markdown file(s) with standard citations
- a processed report exists
- the raw session is archived
- the next blank session file exists
