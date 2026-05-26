---
paths:
  - "sources/media/**/*.md"
  - "sources/media/**/*"
---

# Source media rules

Human-facing overview:
- `sources/README.md`
- `sources/media/README.md`

## Purpose
`sources/media/` holds working-reference images, crops, and associated notes keyed by `sourceId`.

## Structure
- one folder per `sourceId`
- descriptive filenames
- original capture plus detail crops as needed
- optional context/provenance note

## File discipline
- Prefer PNG for screenshots and text-bearing captures.
- JPG is acceptable for photographs of physical documents.
- Keep files small enough for repo practicality.
- Use descriptive filenames, not opaque numbering.

## Local-only masters: `_local/`
Some artifacts should not be committed. Park them in a `_local/` folder; the `.gitignore` rule `sources/media/**/_local/` keeps the bytes off GitHub while letting the folder's `README.md` ship as a stub.

Place a file in `_local/` when any of these apply:
- **Oversize** — larger than **35 MB**. (GitHub's hard limit is 100 MB; 35 MB is the project threshold for "too bulky to commit.")
- **Copyright-restricted** — modern in-copyright works, paywalled subscription content, licensed databases (UK Data Service EUL, etc.) where redistribution is restricted.
- **Privacy-sensitive** — FamilySearch tree exports with living-person data, or any artifact carrying non-ancestor personal information.

Two valid locations:
- `sources/media/_local/` — loose staging for masters not yet sorted into a `sourceId` folder.
- `sources/media/<sourceId>/_local/` — per-source local-only masters, alongside committed working-reference crops/extracts for the same source.

When a file moves into `_local/`, update that folder's `README.md` (the one exception that *is* committed) with:
- filename
- reason (size / copyright / privacy)
- where the canonical master can be retrieved (URL, archive, physical repository)

Public-domain works under 35 MB are committed normally.

## Provenance
- If an image is important, ensure there is enough nearby context to understand what it is, where it came from, and what source it belongs to.
- If a high-resolution master lives elsewhere, keep the repo copy as the working-reference version and note the external location if needed.

## Cross-reference
See also:
- `.claude/rules/sources-validations.md`
- `sources/media/README.md`
- `sources/media/_local/README.md`
