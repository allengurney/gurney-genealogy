# research/case-files/

**User-directed in-depth publication artefacts** — problem statements, biographies, and standalone investigations that Allen explicitly asks to maintain as case files. A case file is a human determination, not a default AI destination.

## Do not use this layer by default
Sustained per-ancestor argument, competing hypotheses, chronology, evidence weighing, and probability assessment for an individual ancestor normally belong in that ancestor's `research/people/g{NN}-{slug}-fact-sheet.research.md` companion. Cross-cutting analysis spanning multiple subjects goes in `research/topics/`.

Create or expand a case file only when Allen explicitly directs standalone treatment. The current repo footprint is intentionally small (one problem statement and one biography at the time of writing).

## Working principle
A case file is a self-contained publication artefact, but it should still cross-link back to the relevant people, places, topics, and source files. Subject-level findings cross-link there rather than being duplicated.

## AI / automation guidance
- `.claude/rules/research-case-files.md`
- `.claude/rules/citations.md`
