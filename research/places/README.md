# research/places/

Place files are the durable research-memory layer for geography, landholdings, and site-specific context.

## Naming

- Prefer stable kebab-case filenames.
- Reuse established filenames when already present.
- Use geographic disambiguation only when needed (`braintree-ma.md`, `hingham-norfolk.md`).

## Structure

Each place file may now contain two layers:

1. Narrative research sections maintained manually.
2. A generated block bounded by:
   - `<!-- GENERATED:LOCATION-REGISTRY:START -->`
   - `<!-- GENERATED:LOCATION-REGISTRY:END -->`

The generated block is populated from `data/locations.json`-compatible extracted entries.

## Current migration discipline

- Preserve existing narrative research when updating a file.
- Replace only the generated block when regenerating.
- If a place has no prior file, create a minimal file with the generated block plus a short research-notes section.
- Preserve inherited quotations, URLs, and note text exactly unless a separate source-cleanup task is underway.
