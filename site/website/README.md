# Gurney Genealogy Library — Project README

**Version:** March 2026  
**Developer:** Allen Lawrence Gurney, Portland, OR  
**Stack:** [Eleventy (11ty)](https://www.11ty.dev/) static site generator, deployed to Cloudflare Pages

---

## What this project is

A static genealogy research site covering 37+ generations of the direct Gurney male line, from Allen Lawrence Gurney (b. 1972) back to Eudes de Gournay, a Viking companion of Rollo who received the Pays de Bray in Normandy at the Treaty of Saint-Clair-sur-Epte (c. 911 AD).

The site has seven published pages plus one non-published template:

| Page | Source file | Purpose |
|---|---|---|
| Homepage | `index.njk` | Dense ancestor spine table; entry point to all research |
| William Gurney bio | `key-research/brigadier-general-william-gurney.md` | Full biography of the G6 ancestor |
| John Gurney case file | `key-research/john-gurney-case-file.md` | Formal research case file for G13–G14 origin hypothesis |
| Ancestor table | `maps-and-lists/ancestor-table.njk` | Full reference table with land holdings and lineage status |
| Ancestor map | `maps-and-lists/ancestor-map.html` | Interactive Leaflet map passed through unchanged during deployment |
| AI Assistant Procedure | `key-research/east-dereham-ai-assistant-procedure.md` | Technical workflow record supporting the John Gurney case file |
| Francis Gurney fact sheet | `fact-sheets/g14-francis-gurney-fact-sheet.md` | Compact structured fact sheet exemplar for future ancestor fact sheets |
| Fact sheet template (not published) | `templates/ancestor-factsheet-TEMPLATE.md` | Reusable Markdown starting point for future ancestor fact sheets |

---

## Architecture overview

> **Priority refactor:** The website currently syncs canonical repo content into `site/website/` before building. A future cleanup should make Eleventy read directly from the canonical root files (`data/`, `fact-sheets/`, and `research/people/`) so generated/synced duplicate Markdown no longer creates Git noise or stale-copy risk.

```
_data/
  ancestors.json       ← SINGLE SOURCE OF TRUTH for all ancestor data
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
maps-and-lists/ancestor-map.html                     ← Passthrough — replace directly, do not inspect or modify during deployment
robots.txt / sitemap.xml / llms.txt   ← SEO and AI crawler files
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
| `type` | All templates | `"era"`, `"ancestor"`, or `"collateral"` |
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

**Collateral entries** (`"type": "collateral"`) — Ken Gurney, Soren & Ebba — are in the JSON for map reference but are filtered out of both tables by the `{% elif item.type == "ancestor" %}` condition in the templates.

---

## Editing content

### Ancestor data (both tables update together)
Edit the canonical root file `data/ancestors v26.json`, then run the data generation/build step. The generated `_data/ancestors.json` file is a site artifact and should not be hand-edited for canonical changes.

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
7. Update `sitemap.xml` and `llms.txt` when the page is published

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

The build is source-driven. Fact sheets are refreshed from root `fact-sheets/`, paired research companions are generated from `research/people/*.research.md`, and `_data/ancestors.json` is regenerated from `data/ancestors v26.json`, `data/places.json`, and `data/places_detail.json`.

**Note:** Update `sitemap.xml` and `robots.txt` with your actual Cloudflare Pages domain before deploying.

---

## Full file map

```
gurney-eleventy/
├── _data/
│   └── ancestors.json          ← All ancestor data; edit this for data changes
├── _includes/
│   ├── layouts/
│   │   ├── base.njk            ← Standard page layout (bio, case file, ancestor table)
│   │   ├── home.njk            ← Homepage layout (hero + table)
│   │   └── case.njk            ← Case file layout (dual titles, sidebar nav)
│   └── partials/
│       ├── siteheader.njk      ← Header/menu rendering loop
│       └── sitefooter.njk      ← Footer
├── assets/
│   └── site.css                ← All styles (era colors, table, buttons, layout)
├── media/
│   └── *.png, *.jpg            ← Images for bio and case file pages
├── key-research/brigadier-general-william-gurney.md   ← Biography prose (Markdown)
├── key-research/john-gurney-case-file.md              ← Case file prose (Markdown)
├── index.njk                             ← Homepage template
├── maps-and-lists/ancestor-table.njk                    ← Ancestor table template
├── maps-and-lists/ancestor-map.html                     ← Map page (passthrough, not managed here)
├── favicon.png
├── robots.txt                  ← Search and AI crawler permissions
├── sitemap.xml                 ← Update domain before deploying
├── llms.txt                    ← AI crawler content hints
├── .eleventy.js                ← Eleventy config (shortcodes, passthroughs)
├── .eleventyignore             ← Excludes README.md from processing
├── package.json
└── _site/                      ← Built output — DEPLOY THIS FOLDER
    ├── index.html
    ├── brigadier-general-william-gurney.html
    ├── john-gurney-case-file.html
    ├── ancestor-table.html
    ├── maps-and-lists/ancestor-map.html
    ├── assets/
    ├── media/
    ├── favicon.png
    ├── robots.txt
    ├── sitemap.xml
    └── llms.txt
```

---

## For a new AI assistant picking this up

The complete project source is self-contained. Key context for a new session:

1. Root `data/ancestors v26.json`, `data/places.json`, and `data/places_detail.json` are authoritative. `_data/ancestors.json` is generated presentation data.
2. The site uses Eleventy. The data-driven pages (`index.njk`, `ancestor-table.njk`) loop over generated `ancestors.json` using Nunjucks `{% for item in ancestors %}`.
3. The prose pages under `key-research/` are Markdown files with Nunjucks shortcodes. They do not pull from `ancestors.json`.
4. `maps-and-lists/ancestor-map.html` is a pre-built Leaflet map that passes through unchanged. Do not modify it without explicit instruction.
5. Navigation structure lives in `_data/navigation.js`. All era colors are CSS classes defined in `assets/site.css` (`.era-modern`, `.era-gilded`, etc.).
6. To deploy: run `npm run package`, then upload the generated zip from `dist/` to Cloudflare Pages.

---

## SEO and AI crawler notes

- `robots.txt` — permits all crawlers including GPTBot, ClaudeBot, and PerplexityBot
- `sitemap.xml` — lists the current published pages with monthly changefreq
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
- `sitemap.xml` updated
- `llms.txt` updated

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
maps-and-lists/ ← ancestor table and passthrough ancestor map
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

### Passthrough map rule
`maps-and-lists/ancestor-map.html` is a passthrough artifact. Copy/replace it directly and do not inspect or modify its internals during deployment unless explicitly requested.


## Research Appendix rule for fact sheets

- Fact-sheet source markdown may include a final `## Research Appendix` section for internal notes and unresolved questions.
- Place it after a horizontal rule (`---`) at the end of the source file.
- The appendix remains in source control but is suppressed from published `/fact-sheets/` HTML during build.
