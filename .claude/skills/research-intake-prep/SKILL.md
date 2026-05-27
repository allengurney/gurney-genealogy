---
name: research-intake-prep
description: Analyze one intake session from sources/intake/new/, inspect files and URLs, extract or OCR content as needed, determine relevance and research destination, and write a repo-ready patchset without directly editing research, data, or media files.
argument-hint: [path to intake session markdown file]
disable-model-invocation: true
---

Phase 1 of intake. Workflow + checklist. The patchset content rules (operational discipline, rich-content-must-land-in-repo, validation default-on, cadence, etc.) live canonically in `.claude/rules/sources.md` and auto-load when this skill writes a patchset file at `sources/intake/processed/`.

## Read first
- `.claude/CLAUDE.md`
- `sources/README.md` (destination decisions for the source-side layers)
- `research/README.md` (destination decisions for the research-side layers)
- `.claude/rules/sources.md` (patchset standard — operational, audit, content rules)
- `.claude/rules/research-writing-style.md` (research-block prose style)
- `.claude/rules/citations.md` (citation discipline)
- `.claude/rules/data-json.md` (sourceId discipline)

## Workflow
For each intake entry:
1. Parse the freeform entry.
2. Identify the files, pages, URLs, and named subjects.
3. **Check existing content before treating an extract as new.** Scan `sources/corpus_supplement/` and `sources/media/` for the source. A patchset that re-extracts content already preserved there is wasted work.
4. Inspect and extract text or OCR as needed.
5. Decide one outcome per item: `promote` or `reject`. (No `hold-review`; see `sources.md`.)
6. Determine the destination(s) for the finding. Multi-destination is normal — see `research/README.md` and `sources/README.md`.
7. Reconcile an existing `sourceId` or propose a new compliant one per `data-json.md`.
8. Use the current `sources/intake/processed/stub-vNN.md` as the next patchset number; rename it to `vNN-topic.patchset.md`; immediately create `stub-v(NN+1).md`.

## Patchset-prep checklist (run before finalizing the patchset)
- [ ] Did I check `sources/corpus_supplement/` and `sources/media/` for already-captured content?
- [ ] For every fact-sheet or research-file edit, did I Read the target file and write a literal `str_replace` with verbatim `old_string` and `new_string`?
- [ ] For every new file, did I write an explicit `new file write` action with the full content body?
- [ ] Does every quoted extract over ~150 words have a `sources/corpus_supplement/{slug}.md` file write action (not just a quote inside the patchset)?
- [ ] Does every new `sourceId` have either a `sources/validations/{sourceId}.md` file write action or a brief justification for skipping?
- [ ] Are all item outcomes `promote` or `reject` — no `hold-review`, no conditional language inside item bodies?
- [ ] Is the patchset's context-to-action proportion within the ~1:2 to ~1:3 band? (Soft check; varies by patchset type.)
- [ ] If a research arc spans 2-3 turns, am I bundling into one patchset rather than drafting prematurely?

## Out of scope for Phase 1
- Do not update `research/...`
- Do not update `data/sources.json`
- Do not move or copy files into `sources/media/`
- Do not archive the session

Those are Phase 2 work, governed by `.claude/skills/research-intake-apply-patch/SKILL.md`.

## Success condition
A second tool can apply the patchset mechanically — executing the listed `str_replace` and `new file write` operations verbatim — without reading the source URLs, opening referenced files to locate footnote anchors, or making any authoring decision.
