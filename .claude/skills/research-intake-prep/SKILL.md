---
name: research-intake-prep
description: Analyze one intake session from sources/intake/new/, inspect files and URLs, extract or OCR content as needed, determine relevance and research destination, and write a repo-ready patchset without directly editing research, data, or media files.
argument-hint: [path to intake session markdown file]
disable-model-invocation: true
---

Use this skill for phase 1 of intake.

## Read first
- `.claude/CLAUDE.md`
- `.claude/rules/repo-file-resolution.md`
- `.claude/rules/research-writing-style.md`
- `.claude/rules/citations.md`
- `.claude/rules/data-json.md`
- `.claude/rules/sources-intake.md`
- `.claude/rules/sources-media.md`
- `.claude/rules/sources-validations.md`

## Check before drafting
Before treating any extract as "new content," check whether it already lives in `sources/corpus_supplement/` or `sources/media/`. The corpus supplement holds full-text extracts of primary and secondary sources that the project has already captured; a patchset that re-extracts and re-promotes content from a corpus-supplement file it didn't read is a wasted patchset.

## What this skill does
For each intake entry:
1. parse the freeform entry
2. identify the files, pages, and URLs
3. inspect and extract text or OCR content as needed
4. decide one outcome: promote, hold-review, duplicate, or reject
5. determine the best research destination(s)
6. reconcile an existing sourceId or propose a new compliant one
7. use the current `sources/intake/processed/stub-vNN.md` as the next patchset number
8. rename that stub to the real patchset filename, for example `vNN-topic.patchset.md`
9. create the next stub immediately, incremented by one

Do not recursively scan `sources/intake/**` for routine version assignment. If the stub is missing, duplicated, or stale, repair it with the shallow-scan fallback in `.claude/rules/sources-intake.md`.

## What this skill does not do
- do not update `research/...`
- do not update `data/sources.json`
- do not move or copy files into `sources/media/`
- do not archive the session

Those belong to phase 2.

## Patchset standard
The patchset is an operational script. Phase 2 follows it; Phase 2 does not interpret it.

For each retained item include:
- outcome (`promote` or `reject`; no `hold-review` — see below)
- exact destination file path or paths
- exact sourceId match or exact new source entry block
- exact literal file operations — for each edit, an explicit `str_replace` with verbatim `old_string` and `new_string`, or an explicit `new file write` with full content body
- exact research markdown block to insert, with the full verbatim source quote embedded — not a summary
- exact validation note body only when needed

Use fenced code blocks for verbatim content to add. Never write "Phase 2 should locate…", "the apply step constructs the block from the source-authority text quoted above…", or "subject to user approval." All of these are signs the item is not yet operational and the prep step is not done.

## Rich content must land in the repo
Quoted source material is an asset. If the patchset preamble quotes a will, a letter, a charter, or a multi-paragraph extract for context, that text must also be in the action steps — written somewhere durable, not left to evaporate when the patchset is moved to `sources/intake/done/`.

The two durable homes:
- **Research companion** (`research/people/*.md`, `research/places/*.md`, `research/topics/*.md`) — the going-deeper layer that humans actually read. The Working Notes entry should carry the verbatim quote, not just a summary, plus the analysis.
- **Source corpus supplement** (`sources/corpus_supplement/*.md`) — the searchable-extracts layer. Create or extend a file there when the extract is long enough or rich enough that the research companion would bloat carrying it inline.

A useful heuristic: under ~150 words of quoted text → research companion only. Over ~150 words, or a complete document (will, charter, letter) → corpus supplement file + companion summary cross-linking the file.

## No hold-review
`hold-review` is not a valid item outcome. If a candidate cannot be made operational, either (a) finish the research that would make it operational, (b) ask the user the resolving question before drafting, or (c) drop it from this patchset and record it as a documented lead. The patchset is for actions, not for parked questions.

## Cadence
Patchsets bundle the cumulative findings of a research arc, not the work of a single turn. A research arc that spans 2-3 turns produces one patchset, not three. Premature drafting forces context-heavy preambles, duplicated source apparatus across patchsets, and operational items that depend on each other in fragile ways. Wait until a coherent batch of findings is in hand.

## Research block style
Write proposed research blocks as ordinary research notes:
- lead with the finding
- carry the verbatim quote (not a summary) when the extract is short enough to live in the companion
- when the extract is long enough to need a corpus-supplement file, the companion block summarises the finding and cross-links the supplement file
- no visible intake, process, AI procedure, or provenance narration in the body prose
- no generic caveating
- add analysis only when it adds real knowledge or language clarification / translation
- keep citations close to the fact

## Success condition
The patchset is good enough that a second tool can apply it mechanically — by executing the listed `str_replace` and `new file write` operations verbatim — without reading the source URLs, opening referenced fact sheets to find footnote anchors, or making any authoring decision.
