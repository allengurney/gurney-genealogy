# sources/

Source-related material beyond the bibliography entries in `data/sources.json`. The bibliography itself lives in `data/sources.json`; this directory holds the artefacts, extracts, working captures, intake queue, and per-source worksheets that support what the bibliography references.

## Contents
- `corpus/` — Searchable full-text extracts of primary and secondary sources. The working-reference layer for citing, quoting, and verifying claims made in fact sheets and case files. Primarily English and European ancestors.
- `corpus_supplement/` — Additional full-text extracts. Higher concentration of North American ancestors; also the canonical home for rich primary extracts (wills, charters, letters, multi-paragraph passages) referenced from a research companion.
- `intake/` — Raw intake queue, processed patchsets, and archived session bundles. See `.claude/skills/research-intake-prep/SKILL.md`.
- `media/` — Source images, crops, text sidecars, and working-reference captures. One folder per `sourceId`.
- `validations/` — Thin per-source validation worksheets recording what was examined and where findings landed.
- `media-refs.md` — Optional index for media stored outside the repo.

## Destination guidance — where does a source-side artefact live?

Object-oriented. A source may touch more than one layer (primary home + secondary touches).

| Object | Primary home | Secondary touches |
|---|---|---|
| A **bibliography entry** for a source (book, charter, online record) — only if cited somewhere in the repo | `data/sources.json` entry with a `sourceId` | `sources/validations/{sourceId}.md` (default-on per `sources.md`); cited-from research companions or fact-sheet footnotes propagate as normal |
| A **primary text extract** longer than ~150 words (will, charter, letter, full record entry) | `sources/corpus_supplement/{slug}.md` (verbatim text + provenance + significance note) | Research companion carries the finding-summary + cross-link; corresponding `sources/validations/{sourceId}.md` notes the extract location |
| A **source image** or facsimile (page scan, monument photo, brass rubbing, seal impression) | `sources/media/{sourceId}/` (one folder per `sourceId`) | Companion sidecar transcription in the same folder if text-bearing; research companion cross-links the image |
| A **short quotation** under ~150 words from a cited source | In the research companion's Working Notes block, as a fenced quote with citation | No `corpus_supplement` file needed |
| A **session-level capture or raw download** | `sources/intake/new/` initially | Promoted through Phase 1 patchset → Phase 2 application to the appropriate destination above |

Source-side rules: `.claude/rules/sources.md` (intake + validations + media) and `.claude/rules/data-json.md` (the `sources.json` registry).

## Working principles
- Source-side files support research. Substantive person/place/topic findings belong on research files (`research/people/`, `research/places/`, `research/topics/`), not in source worksheets or media sidecars.
- Validation files are thin. They record what was examined, not the findings themselves. Findings cross-link to the relevant research file.
- A source that is never cited does not need a presence here. Only cited sources earn a `data/sources.json` entry and the default-on validation file.
- Patchsets in `sources/intake/processed/` carry the detailed step-by-step execution instructions; validations stay thin because the patchset is the audit trail.
