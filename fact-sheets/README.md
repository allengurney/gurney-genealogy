# fact-sheets/

**Published-only.** This directory holds ancestor narratives that Eleventy builds into the website. No research notes, no companions, no staging files.

Research companions for ancestors live at `research/people/g{NN}-{slug}-fact-sheet.research.md`. See AI-Rules.md §3 for the paired-file rule.

## Naming

Generation number is zero-padded. Slug is short, hyphenated, disambiguating:

```
fact-sheets/g14-francis-gurney-fact-sheet.md       ← published narrative
fact-sheets/g23-edmund-gurney-fact-sheet.md
…
```

## What belongs here

- YAML front matter, vitals, highlights, children table, narrative prose, citations, sidebar timeline, related links.
- Allen's wordsmithed work. Stable. Edits happen only when published content changes.

## What does NOT belong here

- Working notes → `research/people/g{NN}-{slug}-fact-sheet.research.md`
- Source extracts longer than an inline quote → companion or `sources/corpus/`
- Open questions, conjectures, negative results → companion
- Non-ancestor research subjects → `research/people/{slug}.md`

## Relationship to data/

Structured facts come from `data/ancestors_v23.json`. Citations reference `sourceId` values in `data/sources.json`. The narrative file holds the prose; the research companion (in `research/people/`) holds the detail and analytical trail.
