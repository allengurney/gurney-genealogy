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

## Provenance
- If an image is important, ensure there is enough nearby context to understand what it is, where it came from, and what source it belongs to.
- If a high-resolution master lives elsewhere, keep the repo copy as the working-reference version and note the external location if needed.

## Cross-reference
See also:
- `.claude/rules/sources-validations.md`
- `sources/media/README.md`
