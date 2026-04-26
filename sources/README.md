# sources/

Source-related material beyond the bibliography entries in `data/sources.json`.

## Contents
- ` corpus/` - Searchable full-text extracts of primary and secondary sources. The working-reference layer for citing, quoting, and verifying claims made in fact sheets and case files. Primarily contains sources for English and European ancestors.
- `corpus_supplement/` - Additional corpus materials. earchable full-text extracts of primary and secondary sources. Higher concentration of sources for North American ancestors.
- `intake/` — raw intake queue, processed patchsets, and archived session bundles
- `media/` — source images, crops, text sidecars, and working-reference captures
- `validations/` — thin per-source validation worksheets
- `media-refs.md` — optional index for media stored outside the repo

## Intake model
- session files live in `sources/intake/new/` as `vNN.md`
- phase 1 writes `sources/intake/processed/vNN.patchset.md`
- phase 2 applies that patchset to `research/`, `sources/media/`, `sources/validations/`, and `data/sources.json`

## Working principle
Source validations record what was examined and where findings landed.
Substantive person/place/topic findings belong in research files, not here.
Patchsets hold detailed step-by-step execution instructions so validations can stay thin.

## AI / automation guidance
See:
- `.claude/rules/sources-intake.md`
- `.claude/rules/sources-validations.md`
- `.claude/rules/sources-media.md`
- `.claude/rules/citations.md`
- `.claude/rules/repo-file-resolution.md`
