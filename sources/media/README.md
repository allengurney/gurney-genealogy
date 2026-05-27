# sources/media/

Source media organized by `sourceId`.

## Structure
One folder per `sourceId`, with descriptive filenames for originals, crops, and annotated images.

## File discipline
- PNG preferred for screenshots and text-bearing images
- JPG acceptable for photographs
- keep working-reference files reasonably small
- store oversized masters in `_local/` (see below)

## Local-only masters: `_local/`
Files larger than **35 MB**, copyright-restricted, or privacy-sensitive go in a `_local/` folder — either `sources/media/_local/` (loose) or `sources/media/<sourceId>/_local/` (per-source). Contents are gitignored; only the folder's `README.md` ships with the repo, recording what's parked locally and where the canonical master can be retrieved. See `sources/media/_local/README.md`.

## Where this fits
See `sources/README.md` for the cross-subdirectory destination guidance.

## AI / automation guidance
- `.claude/rules/sources.md` (intake + validations + media discipline)
