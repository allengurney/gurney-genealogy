# fact-sheets/

Every direct-line ancestor gets a paired set of files here.

## The paired-file rule

**Narrative** (`g{NN}-{slug}-fact-sheet.md`):
- Published content: YAML front matter, vitals, highlights, children table, narrative prose, citations, sidebar timeline.
- Allen's wordsmithed work. Stable. Changes only when published content changes.
- Built by Eleventy into the genealogy site.

**Research companion** (`g{NN}-{slug}-fact-sheet.research.md`):
- Lab notebook for this ancestor. Working notes, open questions, sources consulted, negative results, conflicting information, working hypotheses, raw transcriptions.
- Grows during research sessions. Frequent small commits.
- Skipped by Eleventy build (*.research.md excluded).

See AI-Rules.md §3 for full rules on what goes where.

## Naming

Generation number is zero-padded. Slug is short, hyphenated, disambiguating:

```
g14-francis-gurney-fact-sheet.md            ← narrative
g14-francis-gurney-fact-sheet.research.md   ← research companion
g23-edmund-gurney-fact-sheet.md
g23-edmund-gurney-fact-sheet.research.md
```

## Relationship to data/

Structured facts come from `data/ancestors_v23.json` (future `master.json`). The narrative file holds the prose. The research companion holds the detail, source extracts, and analytical trail. The JSON, narrative, and companion are linked by generation/ancestor ID.
