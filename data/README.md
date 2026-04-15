# data/

Canonical structured data. The single source of truth for ancestor facts, citations, and shared registries. Outputs (fact sheets, the Eleventy site, the pedigree explorer) are generated *from* these files and should never be the place where new facts are first recorded.

## Files

- `master.json` — ancestor records with stable IDs, linked to sources.
- `sources.json` — bibliography of every citable document: archives, URLs, validation status, and media references.
- `locations.json` — shared geographic registry (lat/lng, place names), referenced by `master.json` rather than duplicated per ancestor.

## Discipline

Every fact in `master.json` that depends on a source cites a `sourceId` defined in `sources.json`. Orphan facts (no source) and orphan sources (no fact cites them) are both detectable and should be resolved.
