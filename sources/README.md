# sources/

Source-related material beyond the bare bibliography entries in `data/sources.json`.

## Contents

- `media/` — source media (register scans, record extracts, screen captures), organized by sourceId. For now, stored in-repo since we're dealing primarily with small screengrabs.
- `validations/` — per-source validation worksheets. When a source is examined carefully (paleography of a register entry, reconciliation of conflicting citations, confirmation of an index entry against the original image), the worksheet lives here.
- `media-refs.md` — index for any media stored *outside* the repo (OneDrive, external archives), added later if and when repo storage becomes a concern.

## Media policy

Current rule: small screengrabs and record extracts live in `media/{sourceId}/`. If we start accumulating full high-resolution scans or large PDFs, we move those to OneDrive and leave low-res reference copies in the repo. Keeping media in the repo means commits are atomic — when a source is found and screenshotted, the image and its validation worksheet land in the same commit.

Monitor repo size periodically. GitHub's soft guidance is <1GB; we're well under and should stay under at current accumulation rates.
