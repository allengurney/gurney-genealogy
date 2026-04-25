# Website Refactor Baseline

This note captures the initial baseline for moving from the current Eleventy site toward the new website design in `site/New website design/`.

## Working decisions
- Branch work only; do not modify `main` directly.
- Keep the current manual Cloudflare Pages upload workflow for now.
- Use `data/ancestors v26.json` as the canonical ancestor source.
- Use `data/places.json` and `data/places_detail.json` as the canonical place spine.
- Treat `_data/ancestors.json` and prototype `data/ancestors.js` as presentation data until they are regenerated from canonical files.
- Keep KISS: stabilize build, validation, and content mapping before visual replacement.

## Target site shape
- Homepage: adopt the new design direction, with the catalog as the primary entry point.
- People view: one combined ancestor catalog/table experience.
- Catalog default: clean quick view similar to the prototype.
- Catalog detailed mode: denser view comparable to the current ancestor table.
- Places view: future first-class route that lets readers browse places and move between places and associated people.
- Fact sheets: remain the core published ancestor pages.
- Research companions: publish as light HTML pages with the standard research disclaimer and site-wide menu.

## Current baseline additions
- `npm run validate` checks basic JSON, navigation, route, map, and highlights-file readiness.
- `npm run package` runs validation, builds Eleventy, and creates a dated zip under `dist/` for manual Cloudflare upload.
- `research/highlights.md` provides the editable highlights source requested for the new homepage.
- `research/research.11tydata.js` and `layouts/research.njk` provide a lightweight default publishing path for research markdown.

## Refactor sequence
1. Keep the existing Eleventy project as the production base.
2. Move the new design CSS and page structure into Eleventy layouts/templates.
3. Generate site-friendly people data from canonical v26 data instead of copying the prototype slice.
4. Build the catalog quick/detailed toggle in one page, not separate table and catalog pages.
5. Preserve the standalone ancestor map until the new map view proves complete.
6. Add place-centered browsing after people-centered catalog data mapping is stable.
7. Add research companion pages from root `research/people/` once source routing and privacy expectations are confirmed.

## Preservation list
Keep these public surfaces available during the refactor unless explicitly retired:
- `/key-research/john-gurney-case-file.html`
- `/key-research/brigadier-general-william-gurney.html`
- `/key-research/east-dereham-ai-assistant-procedure.html`
- `/key-research/using-gen-ai-in-genealogy.html`
- `/maps-and-lists/ancestor-map.html`
- existing `/fact-sheets/*.html`
- existing redirect pages

The current `/maps-and-lists/ancestor-table.html` can be retired only after the new catalog detailed mode covers the same information cleanly.
