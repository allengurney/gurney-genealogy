# Fact-sheet drafting handoff standard

Use this when drafting ancestor fact sheets in a separate chat session.

## Objective
Draft only the Markdown fact sheet content and the media manifest for one ancestor at a time. Do not modify site CSS, templates, JSON, or build files.

## Required filename convention
- Markdown: `g##-normalized-name-fact-sheet.md`
- Published permalink: `/fact-sheets/g##-normalized-name-fact-sheet.html`
- Hero image: `/media/factsheets/g##-normalized-name-hero.<ext>`
- Other local assets: `/media/factsheets/g##-normalized-name-*.{png,jpg,jpeg,webp,svg}`

Use two digits for the generation number, for example `g01`, `g06`, `g14`, `g37`.

## Division of responsibility
- `_data/ancestors.json` is the directory/index metadata source.
- Fact-sheet `.md` files are the page-content source.
- Do not try to duplicate long fact-sheet prose into the JSON.

## Required frontmatter contract
```yaml
---
layout: layouts/base.njk
permalink: /fact-sheets/g##-normalized-name-fact-sheet.html
title: Ancestor Name Fact Sheet
pageHeading: Ancestor Name (Birth–Death)
subtitle: "Ancestor fact sheet for G## in the direct Gurney line. One-sentence identity summary. Published MONTH YEAR."
description: "Compact fact sheet for Ancestor Name in the direct Gurney line."
bodyClass: bio-page factsheet-page
updated: DAY MONTH YEAR
factsheet:
  gen: G##
  slug: g##-normalized-name-fact-sheet
  personName: Ancestor Name
  heroImage: /media/factsheets/g##-normalized-name-hero.png
  heroAlt: Historical image or associated site for Ancestor Name
  heroCaption: One-sentence caption.
  heroCredit: Source/credit note.
---
```

## Required section order
1. Vital Records
2. Highlights
3. Children
4. Narrative
5. Citations

Side rail panels:
1. Hero image
2. Related Links
3. Timeline

## Rules
- Keep it compact and fact-sheet-like, not a long biography.
- No section navigation block.
- Use local citation numbering starting at `n1` on each page.
- Use local media assets whenever possible; do not rely on hotlinked images.
- Keep related links limited and relevant.
- Keep timeline entries concise.
- Keep language formal and consistent with the existing site.

## Required output from the drafting chat
1. Complete Markdown fact sheet
2. Short media manifest listing:
   - hero image filename
   - optional supporting image filenames
   - unresolved image needs
3. Optional unresolved research notes


## Site structure notes
- Key research pages publish under `/key-research/`.
- Maps and list pages publish under `/maps-and-lists/`.
- Fact sheets publish under `/fact-sheets/`.
- Old root-level URLs may exist only as redirects for backward compatibility.
- Fact sheets render a generation navigator in the headline row automatically; do not hand-code it in the Markdown.


## Research Appendix rule

- You may include a final `## Research Appendix` section for internal working notes.
- Keep it after a horizontal rule (`---`).
- It will remain in source markdown but is suppressed from published fact-sheet HTML.
