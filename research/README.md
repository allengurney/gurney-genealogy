# research/

Working knowledge: findings, extracts, analysis, negative results, and open questions. The going-deeper layer that humans read when a fact sheet's footnote points them here. Not the polished outputs (those are `fact-sheets/`).

## Subfolders
- `people/` — people-specific working research: ancestor companions paired with fact sheets, pre-fact-sheet ancestors, spouses, non-ancestor subjects, candidate identities, disambiguation targets. Sustained per-ancestor argument and competing hypotheses for a single ancestor live in that ancestor's companion here.
- `places/` — place-memory narrative and analysis above the canonical place registry in `data/places.json` / `data/places_detail.json`.
- `topics/` — cross-cutting analytical or methodological files that span multiple people, places, or sources.
- `case-files/` — user-initiated in-depth publication artefacts (problem statements, biographies). A human determination; AI does not promote findings here without explicit direction.
- `log/` — short operational pointers to where substantive changes landed. Not a research-content layer.

## Destination guidance — where does a research finding live?

Object-oriented. A finding about a person who lived somewhere will normally touch more than one file (primary home + secondary touches).

| Object | Primary home | Secondary touches |
|---|---|---|
| Direct ancestor — working research, source extracts, argument, open questions | `research/people/g{NN}-{slug}-fact-sheet.research.md` (paired companion to the fact sheet) | If durable enough for publication, the corresponding `fact-sheets/g{NN}-{slug}-fact-sheet.md`; if the place is significant in the ancestor's life, the relevant `research/places/{slug}.md` cross-links |
| Non-ancestor person (spouse, in-law, candidate identity) | `research/people/{slug}.md` (no g{NN} prefix) | Crosslinks from the ancestor companion(s) that touch this person |
| Place — significance, naming, events, record coverage | `research/places/{slug}.md` | `data/places.json` (canonical spine) + `data/places_detail.json` (rich descriptive fields); ancestor companions cross-link when the place matters to that ancestor's life |
| Cross-cutting topical analysis or methodological frame | `research/topics/{slug}.md` | Affected research/people/*.research.md companions cross-link the topic file |
| Sustained per-ancestor argument or competing hypotheses for one ancestor | Inside the ancestor's `research/people/g{NN}-{slug}.research.md` companion | — (a separate `research/case-files/` file is created only when the user directs an in-depth publication artefact) |
| User-directed in-depth publication artefact (problem statement, biography) | `research/case-files/{slug}.md` | The relevant ancestor companion notes the case file exists |
| Source-side artefacts (extracts, images, validations) | See `sources/README.md` | — |

Research-side rules: `.claude/rules/research-files.md` (people, places, topics — shared and per-subdirectory discipline), `.claude/rules/research-case-files.md`, `.claude/rules/research-writing-style.md`, `.claude/rules/citations.md`.

## Working principles
- Topical files hold the actual content. Logs point to those files. Findings belong on the relevant subject file, not buried in a source worksheet or log.
- Research files read like research notes, not workflow logs. Lead with the finding. Keep intake / processing / OCR / normalization / archival mechanics out of visible prose.
- Research files should still be source-traceable, especially for new findings, quotations, and inferential claims.
