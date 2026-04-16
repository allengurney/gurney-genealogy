# research/people/

Research files for people — ancestors, spouses, non-ancestor research subjects, and candidate matches. This is the single directory for accumulated research about a person, whether or not they have a fact sheet.

See AI-Rules.md §3 for the paired-file rule and the findings-vs-source-provenance distinction.

## What belongs here

### Ancestor research companions (paired to a fact sheet)

Filename: `g{NN}-{slug}-fact-sheet.research.md`

One per direct-line ancestor who has a published fact sheet in `fact-sheets/`. The fact sheet is the stable published narrative; the companion is the lab notebook — working notes, open questions, sources consulted, conflicting information, negative results, conjectures, raw transcriptions.

**Example:** `g23-edmund-gurney-fact-sheet.research.md` pairs with `fact-sheets/g23-edmund-gurney-fact-sheet.md`.

### Pre-fact-sheet ancestor staging

Filename: `g{NN}-{slug}.md` (no `-fact-sheet.research` suffix)

For direct-line ancestors who don't yet have a fact sheet but need a home for accumulating research. When a fact sheet is eventually produced in `fact-sheets/`, rename the staging file to `g{NN}-{slug}-fact-sheet.research.md`.

**Example:** `g13-john-gurney-1.md` — John Gurney-1, Candidate B probable (~55–60%), no published fact sheet yet.

### Non-ancestor research subjects

Filename: descriptive slug, no generation prefix

People who will not get a fact sheet but warrant a research file:
- Spouses with independent research (Katherine de Wauncy, Edith de Warenne)
- Candidate matches under investigation (Bury St Edmunds apprentice, Earsham John Girney 1636)
- Disambiguation targets (the laceweaver Francis, distinct from Francis G14)
- Context figures referenced across multiple ancestor files (Margaret Rybett, Ann Gurney of Hingham)

**Examples:**
- `margaret-rybett.md` — Francis G14's first wife
- `francis-gurney-laceweaver.md` — the other Francis
- `hingham-ann-gurney.md` — possible sibling of John-1

## What does NOT belong here

- Published narrative for a direct-line ancestor → `fact-sheets/g{NN}-{slug}-fact-sheet.md`
- Geographic findings (parish-wide, county-wide) → `research/places/{place}.md`
- Cross-cutting analyses (Protestation Returns coverage, two-Francis disambiguation methodology) → `research/topics/{topic}.md`
- Long-form hypothesis case files (Candidate B, Candidate A) → `research/case-files/{case}.md`
- Source audit trail (what was examined, scope) → `sources/validations/{source-id}.md`

## Structure inside the file

Standard sections (use what applies; not every file needs all):

```
# {Name}

{One-line summary: relationship to direct line, dates, geography, lineage status.}

## Working Notes
## Known facts
## Open questions
## Sources consulted
## Conflicting information
## Negative results
## Working hypotheses
## Raw data / transcriptions
## Crosslinks
```

## On the filename suffix

Ancestor companions carry the `-fact-sheet.research.md` suffix as an artifact of the original local split script. Pre-fact-sheet stubs and non-ancestors don't. A future cleanup pass could drop `-fact-sheet` from companion filenames for cleaner naming; deferred for now to avoid bulk rename.
