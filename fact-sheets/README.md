# fact-sheets/

Polished narrative markdown for each ancestor. These are hand-wordsmithed — the research voice and the considered phrasing matter, and this folder is where that work lives and is revised.

## Naming convention

`g{NN}-{slug}.md`, e.g.:

- `g06-william-brigadier.md`
- `g13-john-gurney-1.md`
- `g14-francis-gurney.md`

Generation number is zero-padded so files sort correctly. The slug is short, hyphenated, and disambiguating where the name alone isn't unique (two Francis Gurneys, several Benjamins).

## Structure

Each fact sheet follows the established template: YAML front matter, vitals, highlights, children table, narrative prose, citations referencing `sources.json` IDs, research appendix, and sidebar timeline data. See existing sheets for the canonical shape.

## Relationship to data/

Facts come from `data/master.json`. The *prose* — the narrative, anecdotes, family memorial quotes, considered framing — lives here and is edited here directly. The two are linked by generation/ancestor ID; changes in one should be reflected in the other.
