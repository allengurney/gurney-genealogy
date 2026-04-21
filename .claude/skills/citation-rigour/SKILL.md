---
name: citation-rigour
description: Audit, normalize, and strengthen citations in genealogy markdown files, especially fact sheets, research companions, topic files, and case files with many footnotes.
argument-hint: [path or paths]
disable-model-invocation: true
---

Use this skill when the task is to improve citation quality in one or more markdown files.

Typical uses:
- add missing citations
- move citations closer to the supported fact
- expand abbreviated citations into full human-readable notes
- add URL when available
- ensure multiple-source claims include all material sources
- align markdown footnotes with `data/sources.json`
- clean up duplicated, weak, or ambiguous notes
- audit a fact sheet or research file for unsupported claims
- locate the source (local, internet, or otherwise) in order to complete a citation when incorrect or missing.

## Core objective
Make the file more rigorous without rewriting it unnecessarily.

## Read first
1. Read `.claude/rules/citations.md`.
2. Read the relevant path-scoped rule for the target file.
3. Read the target markdown file(s).
4. If needed, read `data/sources.json`.
5. If the file is a fact sheet, also inspect the paired research companion when available.

## Operating rules
- Preserve good existing notes.
- Prefer targeted fixes over broad restyling.
- Keep footnotes close to the supported sentence or clause.
- For multiple-source claims, include all material sources.
- Prefer separate adjacent footnotes over one bloated omnibus footnote when that is clearer.
- Expand cryptic shorthand into readable footnotes.
- Include URL when available and useful.
- Keep source-page / entry / folio specificity whenever possible.
- Align cited sources with `sourceId` values when the source exists in `data/sources.json`.

## Workflow
1. Identify citation-bearing claims and citation gaps.
2. Flag unsupported or weakly supported claims.
3. Determine whether support exists in:
   - the same file
   - the paired research file
   - `data/sources.json`
   - nearby source-validation files
4. Improve or add footnotes.
5. Tighten ambiguous placement.
6. Normalize note style and completeness.
7. Leave a brief summary of:
   - what was fixed
   - what remains unsupported
   - which claims still need source work

## Constraints
- Do not invent support.
- If support is weak or absent, mark it clearly.
- Do not turn a polished fact sheet into a research dump.
- Do not delete meaningful caveats just to make the prose cleaner.

## Preferred footnote shape
See `footnote-template.md`.

## Audit checklist
See `checklist.md`.

## Output behavior
Unless asked otherwise:
- edit the file in place
- preserve prose tone
- make the smallest high-value improvements
- report unresolved citation problems at the end
