# Gurney Genealogy Library — Project README

**Version:** June 2026  
**Developer:** Allen Lawrence Gurney, Portland, OR  
**Stack:** [Eleventy (11ty)](https://www.11ty.dev/) static site generator, deployed to Cloudflare Pages

> New here? Read [`SITE-GUIDE.md`](../../SITE-GUIDE.md) in the repo root first — it is the plain-English orientation. This file is the detailed developer reference.

---

## What this project is

A static genealogy research site covering 37+ generations of the direct Gurney male line, from Allen Lawrence Gurney (b. 1972) back to Eudes de Gournay, a Viking companion of Rollo who received the Pays de Bray in Normandy at the Treaty of Saint-Clair-sur-Epte (c. 911 AD).

The published page set, grouped as in the site menu (`_data/navigation.js`):

| Section | Page | Source file | Purpose |
|---|---|---|---|
| — | Homepage | `index.njk` | Hero + dense ancestor spine table; entry point to all research |
| Key Research | John Gurney case file | `key-research/john-gurney-case-file.md` | Formal research case file for the G13–G14 origin hypothesis |
| Key Research | Brig. Gen. William Gurney bio | `key-research/brigadier-general-william-gurney.md` | Full biography of the G6 ancestor |
| Key Research | Heraldic Chain of Evidence | `key-research/gurney-heraldic-chain-of-evidence.njk` | Heraldic evidence chain for the medieval line |
| Key Research | AI paleographic analysis | `key-research/east-dereham-ai-assistant-procedure.md` | Workflow record supporting the John Gurney case file |
| Key Research | AI in genealogy | `key-research/using-gen-ai-in-genealogy.md` | Methodology essay on AI-assisted research |
| Key Research | Sources | `key-research/sources.njk` | Source catalog, generated from `data/sources.json` |
| Key Research | Misc. Topics | `key-research/misc-topics.njk` + generated `key-research/topics/*` | Select working research topics, published from `research/topics/` via `research/topics/_published-topics.csv` |
| Maps & Lists | Ancestor map | `maps-and-lists/ancestor-map.njk` | Interactive Leaflet map, generated from place/ancestor data via `assets/map-page.js` |
| Maps & Lists | Pedigree catalog | `maps-and-lists/ancestor-table.njk` | Full reference table with quick and detailed modes |
| Maps & Lists | Places catalog | `maps-and-lists/places.njk` | Browsable place index, generated from the place spine |
| Fact Sheets | One page per ancestor | `fact-sheets/g##-*-fact-sheet.md` | Compact structured fact sheets (G02–G37 and related figures) |
| Research notes | One page per fact sheet | generated from `research/people/*.research.md` | Public research companions at `/research/notes/` |
| Place pages | One page per place | `research/places/place-pages.njk` + `research/places/*.md` | Per-place narrative at `/research/places/` |

Fact sheets and research notes are generated in bulk during the build, so the
published total grows as new ancestors are written; it is not a fixed count.
A reusable, non-published starting point lives at `templates/ancestor-factsheet-TEMPLATE.md`.

---

## Architecture overview

> **Priority refactor:** The website currently syncs canonical repo content into `site/website/` before building. A future cleanup should make Eleventy read directly from the canonical root files (`data/`, `fact-sheets/`, and `research/people/`) so generated/synced duplicate Markdown no longer creates Git noise or stale-copy risk.

```
_data/                 ← GENERATED presentation data (do not hand-edit; rebuilt each build)
  ancestors.json       ← built from canonical data/ancestors.json + the place spine
  placesCatalog.json   ← built from data/places.json + data/places_detail.json
  placePages.json      ← built from the place spine + research/places/*.md
  sourcesCatalog.json  ← built from data/sources.json
_includes/
  layouts/
    base.njk           ← Layout for bio + case file pages
    home.njk           ← Layout for homepage
    case.njk           ← Layout for case file (dual-title, case-nav, footnotes)
  partials/
    siteheader.njk     ← Menu loop only; edit `_data/navigation.js` to add/change nav items
    sitefooter.njk     ← Footer copyright
assets/
  site.css             ← All styles
media/
  *.png, *.jpg         ← Images referenced in bio and case file
key-research/brigadier-general-william-gurney.md   ← Biography prose (edit in Typora)
key-research/john-gurney-case-file.md              ← Case file prose (edit in Typora)
fact-sheets/g14-francis-gurney-fact-sheet.md          ← Published fact sheet exemplar
key-research/east-dereham-ai-assistant-procedure.md   ← Technical workflow reference page
templates/ancestor-factsheet-TEMPLATE.md ← Non-published template for future fact sheets
index.njk                             ← Homepage template (loops over ancestors.json)
maps-and-lists/ancestor-table.njk                    ← Ancestor table template (loops over ancestors.json)
maps-and-lists/ancestor-map.njk                      ← Ancestor map template (generated; uses assets/map-page.js)
robots.txt                            ← hand-kept crawler file; sitemap.xml / llms.txt are generated at build
_site/                                ← BUILT OUTPUT — deploy this folder
```

**How it works:** Eleventy reads the source files, processes `.md` and `.njk` templates, and writes finished HTML to `_site/`. The ancestor data lives in `_data/ancestors.json`; Eleventy automatically exposes it as `ancestors` in every template. Both the homepage and ancestor table loop over the same JSON — editing one record updates both pages simultaneously.

---

## The ancestors.json data file

This is the central data file. Every ancestor and era divider is one record in a JSON array, ordered as they appear in the tables. Two record types:

**Era divider:**
```json
{
  "type": "era",
  "label": "Gilded Age & Civil War — New York",
  "cssClass": "era-gilded",
  "colorFrom": "#6a4f25",
  "colorTo": "#8a6d35"
}
```

**Ancestor:**
```json
{
  "type": "ancestor",
  "gen": "G6",
  "name": "Brigadier General William Gurney",
  "dates": "1821–1879",
  "geography": "Flushing, Queens NY · Manhattan · Charleston SC",
  "eraKey": "Gilded Age & Civil War",
  "lineageStatus": "Confirmed",
  "summary": "Wholesale merchant, Civil War colonel, commandant of Charleston 1865.",
  "notables": "Full paragraph for ancestor table...",
  "landHoldings": "Property details...",
  "spouses": [
    { "name": "Caroline (maiden name unknown)", "dates": "m. c.1840, d. c.1844–1845" },
    { "name": "Mary Jane Fisk", "dates": "1831–1900, m. 23 Sep 1847" }
  ],
  "children": [
    { "name": "Amos Willis Gurney", "dates": "b. 1842", "notes": "G5 ancestor" }
  ],
  "buttons": [
    { "label": "Click for biography", "url": "/key-research/brigadier-general-william-gurney.html", "style": "bio" }
  ],
  "locations": [
    {
      "place": "Flushing, Queens, New York, USA",
      "siteName": "",
      "eventType": "individual geography",
      "eventDate": "1821–1837",
      "lat": 40.7675,
      "lng": -73.8278,
      "geocodeBasis": "town centroid",
      "confidence": "High",
      "photoUrl": "", "photoTitle": "", "siteUrl": "", "siteLabel": ""
    }
  ]
}
```

**Field reference:**

| Field | Used by | Description |
|---|---|---|
| `type` | All templates | `"era"`, `"ancestor"`, or `"related"` |
| `gen` | Both tables | Generation number (G1, G6, G~31, etc.) |
| `name` | Both tables | Full display name |
| `dates` | Both tables | Birth–death or active dates |
| `geography` | Both tables | Display text for geography column |
| `eraKey` | Ancestor table | Era label shown in Era column |
| `lineageStatus` | Ancestor table | Confirmed / Probable / Direct / Gap in record / etc. |
| `summary` | Homepage | One-line summary shown in homepage table |
| `notables` | Ancestor table | Full notables paragraph |
| `landHoldings` | Ancestor table | Documented property and land holdings |
| `spouses` | Research ref | Array of `{name, dates, notes}` objects |
| `children` | Research ref | Array of `{name, dates, mother, notes}` objects |
| `buttons` | Homepage / ancestor table | Array of `{label, url, style}`. Internal site links use `"bio"` or `"research"`; third-party links use `"external"`; FamilySearch links use `"family-search"`. |
| `externalIds` | Generated data / future integrations | Compact cross-reference object for site IDs, currently `{ "familySearch": "ID" }` when known. |
| `locations` | Map / research | Geographic points from the ancestor map CSV; `{place, siteName, eventType, eventDate, lat, lng, ...}` |

**Adding new attributes to `ancestors.json` does not break anything.** Templates only reference the fields they use. New fields are silently ignored by existing templates until a template is written to use them.

**Related entries** (`"type": "related"`) are collateral or notable non-direct-line figures (e.g., Anne Boleyn at G17). They are carried in the JSON and rendered with a related-status marker; the generated data flags them with `isRelated: true`. Do not confuse this with direct-line lineage status — see `AGENTS.md` §5.

---

## Editing content

### Ancestor data (both tables update together)
Edit the canonical root file `data/ancestors.json`, then run the data generation/build step. The generated `_data/ancestors.json` file is a site artifact and should not be hand-edited for canonical changes.

### Homepage and ancestor table layout
Edit `index.njk` (homepage) or `maps-and-lists/ancestor-table.njk` (ancestor table). These are Nunjucks templates — the loop structure is at the bottom of each file.

### Adding a new ancestor
Add one JSON object to `ancestors.json` at the correct position in the array (between the right era divider and the next ancestor). Minimum fields: `type`, `gen`, `name`, `dates`, `geography`, `eraKey`, `lineageStatus`, `summary`, `notables`, `landHoldings`. All others can be empty arrays or empty strings.

### Adding a new detail page
1. Create the new Markdown page in the correct source directory (`key-research/` or `fact-sheets/`) with frontmatter `layout: layouts/base.njk`
2. Add or update the menu entry in `_data/navigation.js` only if the page should appear in the main menu
3. Add a `buttons` entry in `_data/ancestors.json` for the relevant ancestor(s) if the page should be reachable from the tables

### Adding a new ancestor fact sheet
1. Copy `templates/ancestor-factsheet-TEMPLATE.md` into `fact-sheets/` and rename it
2. Set `layout: layouts/base.njk` and `bodyClass: bio-page factsheet-page`
3. Use the existing compact fact-sheet pattern: Vital Records, Highlights, Children, Narrative, Citations — no section navigation block
4. Use a local hero image under `media/` whenever possible; avoid remote hotlinked images so deployments stay stable
5. Keep the page out of the main nav unless explicitly wanted; use ancestor-table/homepage buttons for access
6. Add the new fact-sheet button in `_data/ancestors.json` for the relevant ancestor
7. Rebuild — `sitemap.xml` and `llms.txt` regenerate automatically to include the new page

### Editing bio and case file prose
Open the relevant `.md` file in **Typora** (Windows, $15). Tables render as visual grids. Two image placement patterns:

**Floated figure (image + caption beside following text):**
```
{% figure "/media/filename.png", "Alt text", "Caption.", "float-figure" %}
```

**Image + prose in same paragraph (text wraps around image):**
```html
<p class="image-float-right">
  <img src="/media/filename.png" alt="Alt text">
  Prose text here...
  <span class="inline-caption">Optional caption.</span>
</p>
```

### Editing nav links
Edit `_data/navigation.js`. The header itself is a loop over navigation data; avoid hardcoding menu links in `_includes/partials/siteheader.njk`.

---

## Building and deploying

```bash
npm install          # first time only — installs Eleventy
npm run build        # syncs source content, regenerates data, cleans, and builds _site/
npm run validate     # checks generated data, companion pages, navigation, and route targets
npm run package      # full manual Cloudflare package into dist/
npm run watch        # rebuilds automatically as you edit
```

Deploy: use `npm run package`, then upload the dated zip from `dist/` to Cloudflare Pages.

The build is source-driven. Fact sheets are refreshed from root `fact-sheets/`, paired research companions are generated from `research/people/*.research.md`, published topics are mirrored from the files listed in `research/topics/_published-topics.csv` into `key-research/topics/` (Misc. Topics), and `_data/ancestors.json` is regenerated from `data/ancestors.json`, `data/places.json`, and `data/places_detail.json`.

**Note:** The public domain lives in `_data/site.json` (`url`). `sitemap.xml`,
`llms.txt`, and `_redirects` are generated from that during the build — do not
hand-maintain deployed copies. Only `robots.txt` is a hand-kept passthrough file.

---

## G13 research annex and Context Graph explorer (package mode)

The John Gurney (G13) research annex — the research library hub, topic pages,
permanent evidence/finding pages, the evidence drawer, and the **Context Graph
explorer** — is generated only when `G13_PACKAGE=staging|production` is set
(`npm run preview:g13` sets it and produces the deployable zip). An ordinary
legacy `npm run build` cleans all of it away, and `_data/navigation.js` gates
the two Key Research menu items ("John Gurney Context Graph Explorer",
"John Gurney Research Library") on the same env var so a legacy build never
carries dead links.

Data flow: `tools/g13_graph.py export-website` (repo root, run against the live
canonical SQLite graph) writes the public export to
`data/context-graphs/g13/exports/website-current/` (gitignored, derived). The
pre-cutover `website/` directory is retained for rollback. At build time
`scripts/sync-g13-package.js` copies it into `assets/g13-graph/` and generates
the annex pages under `research/g13-annex/` (also cleaned/derived).

The Context Graph explorer (`/research/notes/g13-john-gurney/explorer/`) is a
view-only, dependency-free three-area page:

- **Files:** `assets/g13-graph-explorer.js` (app), `assets/g13-graph-explorer.css`
  (dark theme mirroring `tools/g13_graph_editor/static/styles.css`, including the
  per-kind color palette), `_includes/layouts/g13-explorer.njk` (full-viewport
  layout below the site header), and the `writeExplorerPage`/`explorer.json`
  pieces of `scripts/sync-g13-package.js`.
- **Data it reads (all under `/assets/g13-graph/`):** `explorer.json`
  (`{items, sourceUsage}` — the findings index enriched with per-item year range
  and source count, plus sourceId→citing-item counts), `adjacency.json` (item↔item
  edges with relation type/strength/explanation), `findings/<ID>.json` (full item
  detail, fetched lazily), `sources.json` (compact citation lookup),
  `site-map.json` (topic/publication URL resolution), `manifest.json` (revision).
- **Area 1** mirrors the graph editor's Items tab: search plus kind / confidence /
  topic file / year (5-year buckets, 1600–1670, matched against each item's date
  range) filters.
- **Area 2** is an SVG map: with a selection, an ego view (incoming relations on
  the left, outgoing on the right, relation verbs from
  `assets/g13-graph-render.js` `RELATIONS`, the item's cited sources below with
  role verbs, and off-page stub lines with "+N" counts for a neighbor's or
  source's other connections; click any node — item or source — to recenter).
  Centering a **source** shows every research item that cites it (role verbs on
  the edges) and puts the source's citation, external link, and "Cited by" list
  in Area 3. With no selection, a force-layout overview of the filtered items
  (click = preview, click again = focus). `#item/G13-RI-######` and
  `#source/<sourceId>` hash deep-links restore the view.
- **Area 3** renders the selected item through the shared
  `G13GraphRender.renderFinding` — the same projection as the evidence drawer
  and permanent finding pages — restyled dark.
- **Embedded relationship map:** every permanent finding page carries a
  "Relationship map" section (before Technical details) with the same ego scene,
  drawn by the same script into `#g13x-embed` — item clicks navigate to that
  item's permanent page, source clicks open the explorer on the source, and the
  caption deep-links into the explorer. `research.njk` loads the explorer
  CSS/JS on all `g13Annex` pages; the script no-ops unless `#g13x-app` or
  `#g13x-embed` exists.
- **Printing:** an `@media print` block in the explorer CSS linearizes the app
  (hides the chrome and Area 1, re-themes the map and text light); permanent
  finding pages — now including the embedded map — are the print-preferred
  surface.
- **Gotchas:** every public page must have exactly one `h1` (the app bar brand
  is the explorer's); the shared `g13-*` finding markup is restyled inside
  `.g13x-app` at deliberately low selector specificity so the per-kind chip
  colors win; sources are not adjacency nodes — the per-item citation links come
  from each finding's detail JSON, which is why the list (Area 1) stays
  items-only (the source-centered ego view covers source navigation instead).
- **SEO / cutover:** index-readiness of the whole staged annex was validated
  2026-07-11; the checklist (sitemap/llms/canonicals/robots/redirects, the
  production-vs-preview zip distinction, post-deploy search-console steps) lives
  in `tools/plans/G-13 Refactor/prompts/cutover.md`.

---

## Full file map

Files marked **(generated)** are produced by the build from upstream sources and
should not be hand-edited. See §"Building and deploying" for how they are made.

```
gurney-eleventy/
├── _data/                      ← (generated) presentation data; see Architecture overview
│   ├── ancestors.json          ← (generated) from canonical data/ancestors.json + place spine
│   ├── placesCatalog.json      ← (generated) from the place spine
│   ├── placePages.json         ← (generated) from the place spine + research/places/*.md
│   ├── sourcesCatalog.json     ← (generated) from data/sources.json
│   ├── navigation.js           ← menu structure (edit this for nav changes)
│   └── site.json               ← site-wide settings incl. public URL
├── _includes/
│   ├── layouts/                ← base.njk, home.njk, case.njk, research.njk
│   └── partials/               ← siteheader.njk (menu loop), sitefooter.njk, favicon-links.njk
├── assets/                     ← site.css, explorer.css, refactor.css, phase2.css, *.js
├── media/                      ← images referenced by pages and fact sheets
├── scripts/                    ← build pipeline (see §Building and deploying)
│   ├── sync-site-content.js    ← mirrors fact sheets / companions / case files in
│   ├── generate-site-data.js   ← builds _data/*.json from canonical data/
│   ├── clean-site.js           ← clears _site/
│   ├── finalize-public-site.js ← URL/canonical fixup; generates sitemap, llms.txt, _redirects
│   ├── validate-site.js        ← data + route + meta-description checks
│   └── package-site.js         ← zips _site/ into dist/ for upload
├── key-research/               ← case file, bios, AI pages, sources page (.md and .njk)
├── fact-sheets/                ← (generated) copies synced from root fact-sheets/
├── research/                   ← (generated) companions + place pages
├── maps-and-lists/             ← ancestor-table.njk, ancestor-map.njk, places.njk
├── index.njk                   ← Homepage template
├── robots.txt                  ← Search and AI crawler permissions (hand-kept)
├── .eleventy.js                ← Eleventy config (shortcodes, passthroughs, transforms)
├── .eleventyignore             ← Excludes README.md etc. from processing
├── package.json
├── dist/                       ← (generated) dated upload zips from npm run package
└── _site/                      ← (generated) BUILT OUTPUT — deploy this folder
    ├── index.html, key-research/, maps-and-lists/, fact-sheets/, research/
    ├── assets/, media/, favicon*, robots.txt
    ├── sitemap.xml, llms.txt    ← (generated by finalize-public-site.js)
    └── _redirects               ← (generated) Cloudflare 301 redirect rules
```

---

## For a new AI assistant picking this up

The complete project source is self-contained. Key context for a new session:

1. Root `data/ancestors.json`, `data/places.json`, and `data/places_detail.json` are authoritative. `_data/ancestors.json` is generated presentation data.
2. The site uses Eleventy. The data-driven pages (`index.njk`, `ancestor-table.njk`) loop over generated `ancestors.json` using Nunjucks `{% for item in ancestors %}`.
3. The prose pages under `key-research/` are Markdown files with Nunjucks shortcodes. They do not pull from `ancestors.json`.
4. The ancestor map is generated from `maps-and-lists/ancestor-map.njk` and `assets/map-page.js`, reading the same place/ancestor data as the rest of the site. (A legacy standalone `ancestor-map.html` remains in the folder but is no longer built or deployed.)
5. Navigation structure lives in `_data/navigation.js`. All era colors are CSS classes defined in `assets/site.css` (`.era-modern`, `.era-gilded`, etc.).
6. To deploy: run `npm run package`, then upload the generated zip from `dist/` to Cloudflare Pages.

---

## SEO and AI crawler notes

- `robots.txt` — permits all crawlers including GPTBot, ClaudeBot, and PerplexityBot
- `sitemap.xml` — generated each build (`finalize-public-site.js`) listing every public page as a canonical extensionless URL
- `llms.txt` — AI-readable site description following the emerging llms.txt standard
- Schema.org `Person` JSON-LD — embedded in the William Gurney biography page
- Open Graph tags — on all templated pages
- All images have `alt` attributes
- All external links use `rel="noopener"`
- No insecure `http://` links in outbound hrefs


## Fact-sheet production standard

### Naming convention
- Markdown source: `g##-normalized-name-fact-sheet.md`
- Published permalink: `/g##-normalized-name-fact-sheet.html`
- Hero image: `/media/factsheets/g##-normalized-name-hero.<ext>`
- Other local assets: `/media/factsheets/g##-normalized-name-*`

Use two digits for the generation number so sorting remains stable.

### Division of responsibility
- `_data/ancestors.json` is the directory/index metadata source.
- Fact-sheet `.md` files are the page-content source.
- Keep JSON concise; do not duplicate full page prose in the JSON.

### JSON button contract
For any ancestor with a published fact sheet, add exactly one internal button:

```json
{
  "label": "Fact sheet",
  "url": "/g##-normalized-name-fact-sheet.html",
  "style": "bio"
}
```

For FamilySearch profile links, use the dedicated style and keep the ID in `externalIds`:

```json
{
  "buttons": [
    {
      "label": "FamilySearch",
      "url": "https://www.familysearch.org/tree/person/details/XXXX-XXX",
      "style": "family-search"
    }
  ],
  "externalIds": {
    "familySearch": "XXXX-XXX"
  }
}
```

### Required frontmatter
Every fact sheet should include a `factsheet` block for page identity and hero media:

```yaml
factsheet:
  gen: G##
  slug: g##-normalized-name-fact-sheet
  personName: Ancestor Name
  heroImage: /media/factsheets/g##-normalized-name-hero.png
  heroAlt: Historical image or associated site for Ancestor Name
  heroCaption: One-sentence caption.
  heroCredit: Source/credit note.
```

### Publishing checklist
- filename follows `g##-normalized-name-fact-sheet.md`
- permalink matches filename
- local hero image exists or is intentionally omitted
- no section navigation block
- body class is `bio-page factsheet-page`
- ancestor JSON includes a `Fact sheet` button
- page builds cleanly in Eleventy
- no broken images
- homepage row and ancestor-table row show the button
- `npm run validate` passes (this also regenerates `sitemap.xml` and `llms.txt`)

### Drafting handoff
See `templates/factsheet-drafting-handoff.md` for the clean handoff prompt and drafting rules for a separate chat session.


---

## Navigation and directory structure (April 2026)

The site now uses a **multi-level menu** with always-visible top-level items and click-to-open submenus. Keep navigation data in `_data/navigation.js`; do not hardcode menu links in `siteheader.njk` beyond the loop.

### Top-level menu structure
- `Home`
- `Key Research`
- `Maps & Lists`
- `Fact Sheets`
- `Placeholder` (planned only; keep hidden)

### Source directory structure
```
key-research/   ← case file, biographies, AI procedure, AI in genealogy page
maps-and-lists/ ← pedigree catalog (ancestor table), generated ancestor map, places catalog
fact-sheets/    ← all published ancestor fact-sheet Markdown files
templates/      ← non-published reusable templates and drafting handoff docs
redirects/      ← root-level backward-compatibility redirect pages
```

### URL structure
- Key research pages: `/key-research/...`
- Maps and lists: `/maps-and-lists/...`
- Fact sheets: `/fact-sheets/...`

### Menu editing rule
- Edit `_data/navigation.js` for all menu structure changes.
- Leave hidden future menu items in the data file with `visible: false` rather than deleting them if they are part of the plan.

### Fact-sheet headline navigation
Fact sheets render an automatic right-justified generation navigator in the headline row. The left arrow points to the nearest built **earlier** generation fact sheet; the right arrow points to the nearest built **later** generation fact sheet. This is driven from `_data/factsheetIndex.js` and `fact-sheets/fact-sheets.11tydata.js`.

### Ancestor map
The ancestor map at `/maps-and-lists/ancestor-map.html` is generated from
`maps-and-lists/ancestor-map.njk` plus `assets/map-page.js`, drawing on the same
place and ancestor data as the rest of the site (markers are built from
`placeRefs`/`ancestorLinks` in the canonical data). A legacy standalone
`maps-and-lists/ancestor-map.html` source file remains in the folder but is no
longer built or deployed.


## Research Appendix rule for fact sheets

- Fact-sheet source markdown may include a final `## Research Appendix` section for internal notes and unresolved questions.
- Place it after a horizontal rule (`---`) at the end of the source file.
- The appendix remains in source control but is suppressed from published `/fact-sheets/` HTML during build.
