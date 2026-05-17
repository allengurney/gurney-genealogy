# Intake patchset v45 — site build / UX improvements

**Prepared:** 2026-05-16
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Status:** Draft patchset for review. **Do NOT apply until approved.**

This is a site / build patchset, not a research promotion. It only touches `site/website/` (templates, data, CSS). No `data/`, `research/`, `fact-sheets/`, or `sources/` content changes.

## Scope (four tasks)
1. Move fact-sheet research-companion button under the generation selector and rename to "View research notes". Keep it readable on tablet and mobile widths.
2. Make the Places Catalog row icons line up in a stable column rather than drifting with text length. Anchor the icon column center-left, not far right.
3. Make the header's "Updated DD Month YYYY by" date auto-update to the build date.
4. Sources page stats: rename "Full corpus" → "Library holdings", recalculate as corpus + corpus supplement + media counts, and add hover tooltips to all four stats.

## Files touched (final list)
- `site/website/_includes/layouts/base.njk` — move research-companion link into a stack under the generation nav, rename, fallback for non-factsheet pages.
- `site/website/_includes/partials/siteheader.njk` — render `{{ build.date }}` instead of per-page `{{ updated }}`.
- `site/website/_data/build.js` — **new** Eleventy data file returning the current build date.
- `site/website/_data/sourceStats.js` — add `libraryHoldingsCount` (corpus + corpus_supplement + media).
- `site/website/key-research/sources.njk` — rename stat, swap value, add `title` tooltips to all four stats.
- `site/website/assets/site.css` — add `.gen-stack` styling for the action link under the generation nav.
- `site/website/assets/explorer.css` — convert `.place-row` desktop layout from flex-with-margin-left:auto to a fixed grid so `.place-media` lives in a stable column.
- `site/website/assets/phase2.css` — mirror the same `.place-row` change (phase2.css overrides explorer.css; both must agree to avoid drift).
- Page front-matter cleanup (inert `updated:` keys removed) in: `site/website/index.njk`, `site/website/key-research/sources.njk`, `site/website/maps-and-lists/places.njk`, `site/website/maps-and-lists/ancestor-map.njk`, `site/website/maps-and-lists/ancestor-table.njk`, `site/website/research/places/place-pages.njk`, plus all `site/website/fact-sheets/g*-*.md`.

The per-page `updated:` front-matter becomes dead after task 3 (nothing reads it). Removal is a follow-on cleanup — see §7. If the reviewer prefers, this cleanup can be split into its own patchset and the v45 application can stop after §6.

---

## 1. Fact-sheet research-companion button moves under the generation selector

### 1a. `site/website/_includes/layouts/base.njk` — rewrite the `.page-head` block

**Old (lines 27–52):**

```njk
      <div class="page-head{% if factsheetNav %} page-head-with-gen-nav{% endif %}">
        {% if factsheetNav %}
          <div class="page-head-row">
            <h1>{{ pageHeading | safe }}</h1>
            <nav class="generation-nav" aria-label="Generation navigation">
              {% if factsheetNav.later %}
                <a class="gen-link gen-prev" href="{{ factsheetNav.later.url }}" title="Later generation: {{ factsheetNav.later.label }}">&larr;</a>
              {% else %}
                <span class="gen-link is-disabled">&larr;</span>
              {% endif %}
              <span class="gen-current">Generation {{ factsheetNav.current.genDisplay }}</span>
              {% if factsheetNav.earlier %}
                <a class="gen-link gen-next" href="{{ factsheetNav.earlier.url }}" title="Earlier generation: {{ factsheetNav.earlier.label }}">&rarr;</a>
              {% else %}
                <span class="gen-link is-disabled">&rarr;</span>
              {% endif %}
            </nav>
          </div>
        {% else %}
          <h1>{{ pageHeading | safe }}</h1>
        {% endif %}
        {% if subtitle %}<p>{{ subtitle }}</p>{% endif %}
        {% if researchCompanion %}
          <p class="page-action-row"><a class="page-action-link" href="{{ researchCompanion.url }}">View research companion</a></p>
        {% endif %}
      </div>
```

**New:**

```njk
      <div class="page-head{% if factsheetNav %} page-head-with-gen-nav{% endif %}">
        {% if factsheetNav %}
          <div class="page-head-row">
            <h1>{{ pageHeading | safe }}</h1>
            <div class="gen-stack">
              <nav class="generation-nav" aria-label="Generation navigation">
                {% if factsheetNav.later %}
                  <a class="gen-link gen-prev" href="{{ factsheetNav.later.url }}" title="Later generation: {{ factsheetNav.later.label }}">&larr;</a>
                {% else %}
                  <span class="gen-link is-disabled">&larr;</span>
                {% endif %}
                <span class="gen-current">Generation {{ factsheetNav.current.genDisplay }}</span>
                {% if factsheetNav.earlier %}
                  <a class="gen-link gen-next" href="{{ factsheetNav.earlier.url }}" title="Earlier generation: {{ factsheetNav.earlier.label }}">&rarr;</a>
                {% else %}
                  <span class="gen-link is-disabled">&rarr;</span>
                {% endif %}
              </nav>
              {% if researchCompanion %}
                <a class="page-action-link gen-action-link" href="{{ researchCompanion.url }}">View research notes</a>
              {% endif %}
            </div>
          </div>
        {% else %}
          <h1>{{ pageHeading | safe }}</h1>
        {% endif %}
        {% if subtitle %}<p>{{ subtitle }}</p>{% endif %}
        {% if researchCompanion and not factsheetNav %}
          <p class="page-action-row"><a class="page-action-link" href="{{ researchCompanion.url }}">View research notes</a></p>
        {% endif %}
      </div>
```

Notes:
- On fact sheets (factsheetNav present), the research-companion link now renders only inside `.gen-stack`. On any other page that happens to provide `researchCompanion`, the fallback row below the subtitle renders the same link with its old class. Both flavors use the new "View research notes" label.
- The class `page-action-link` is reused so existing pill styling carries over; `gen-action-link` is an additive modifier for size/alignment.

### 1b. `site/website/assets/site.css` — add `.gen-stack` rules

**Insert after the existing `.page-action-link:hover` rule (currently around line 626), before the `@media (max-width: 980px)` block at line 663:**

```css
.gen-stack{display:flex;flex-direction:column;align-items:flex-end;gap:6px;margin-left:auto;min-width:0}
.gen-stack .generation-nav{margin-left:0}
.gen-stack .gen-action-link{font-size:.72rem;padding:.26rem .58rem;white-space:nowrap;max-width:100%}
```

**Update the existing 980px breakpoint (lines 663–667):**

Old:
```css
@media (max-width: 980px){
  .topnav.multi-level{gap:6px}
  .page-head-row{flex-direction:column;align-items:flex-start}
  .generation-nav{margin-left:0}
}
```

New:
```css
@media (max-width: 980px){
  .topnav.multi-level{gap:6px}
  .page-head-row{flex-direction:column;align-items:flex-start}
  .generation-nav{margin-left:0}
  .gen-stack{align-items:flex-start;margin-left:0;width:100%}
}
@media (max-width: 540px){
  .gen-stack{width:100%}
  .gen-stack .gen-action-link{align-self:stretch;justify-content:center;text-align:center}
}
```

UX intent: on desktop the action link tucks under the right-aligned generation selector. At ≤980px the head row stacks vertically, generation nav sits flush-left, and the action link sits flush-left beneath it. At ≤540px the action link spans the full row width so the tap target is comfortable on phones.

### 1c. Reviewer-visible sanity points
- The Eleventy computed `researchCompanion` data is unchanged.
- `View research companion` legacy text disappears from all rendered pages; only "View research notes" remains.
- `.page-action-row` styling stays (still used by the non-factsheet fallback).

---

## 2. Places Catalog — stable icon column

### 2a. `site/website/assets/explorer.css` — desktop `.place-row` layout

**Old (lines 181–191):**

```css
.place-list{display:grid;grid-template-columns:1fr;gap:8px}
.place-row{display:flex;gap:14px;align-items:center;min-height:92px;padding:12px 16px;border:1px solid var(--explorer-rule);border-radius:8px;background:var(--explorer-paper);box-shadow:var(--explorer-shadow);cursor:pointer}
.place-row:hover,.place-row.is-active{background:#fbf7ef}
.place-marker{flex:0 0 auto;width:12px;height:12px;border-radius:50%;border:2px solid var(--explorer-accent);background:var(--explorer-paper)}
.place-main h2{font-family:var(--explorer-serif);font-size:1.1rem;line-height:1.15;margin:0 0 4px;color:var(--explorer-ink)}
.place-main p{font-family:var(--explorer-sans);font-size:12.5px;line-height:1.45;color:var(--explorer-muted);margin:0}
.place-meta{display:flex;gap:7px;flex-wrap:wrap;margin-top:8px;font-family:var(--explorer-sans);font-size:10.5px;color:var(--explorer-muted)}
.place-meta span,.place-count,.place-role{border:1px solid var(--explorer-rule-2);border-radius:999px;padding:2px 7px;background:#fdfbf6}
.place-main{flex:0 1 auto;width:fit-content;min-width:0;max-width:430px}
.place-count{flex:0 0 auto;margin-left:auto;font-family:var(--explorer-sans);font-size:11px;color:var(--explorer-muted);white-space:nowrap}
.place-media{flex:0 0 auto;display:flex;gap:8px;align-items:center;justify-content:flex-start;min-width:0;margin-left:6px}
```

**New:**

```css
.place-list{display:grid;grid-template-columns:1fr;gap:8px}
.place-row{display:grid;grid-template-columns:12px minmax(0,440px) auto 1fr auto;column-gap:14px;align-items:center;min-height:92px;padding:12px 16px;border:1px solid var(--explorer-rule);border-radius:8px;background:var(--explorer-paper);box-shadow:var(--explorer-shadow);cursor:pointer}
.place-row:hover,.place-row.is-active{background:#fbf7ef}
.place-marker{width:12px;height:12px;border-radius:50%;border:2px solid var(--explorer-accent);background:var(--explorer-paper);justify-self:start}
.place-main h2{font-family:var(--explorer-serif);font-size:1.1rem;line-height:1.15;margin:0 0 4px;color:var(--explorer-ink)}
.place-main p{font-family:var(--explorer-sans);font-size:12.5px;line-height:1.45;color:var(--explorer-muted);margin:0}
.place-meta{display:flex;gap:7px;flex-wrap:wrap;margin-top:8px;font-family:var(--explorer-sans);font-size:10.5px;color:var(--explorer-muted)}
.place-meta span,.place-count,.place-role{border:1px solid var(--explorer-rule-2);border-radius:999px;padding:2px 7px;background:#fdfbf6}
.place-main{min-width:0;max-width:none}
.place-media{display:flex;gap:8px;align-items:center;justify-content:flex-start;min-width:0}
.place-count{font-family:var(--explorer-sans);font-size:11px;color:var(--explorer-muted);white-space:nowrap;justify-self:end}
```

Layout intent:
- Column 1: marker (12px fixed).
- Column 2: text block (min 0, max 440px); long descriptions wrap inside it.
- Column 3: media icons (their natural width); now lives at a fixed horizontal offset from the row's left edge, ~ 12 + 14 + 440 + 14 ≈ 480px — center-left, never drifting with text length.
- Column 4: `1fr` spacer absorbing the empty middle.
- Column 5: count badge, right-justified.

DOM order is unchanged (`.place-marker`, `.place-main`, `.place-media`, `.place-count`) — grid auto-places them into columns 1–5 in source order, hitting the explicit grid track at column 4 (the spacer) only via auto-flow. To guarantee placement we set `justify-self` on count/marker; main and media accept default `stretch` / `start`.

Reviewer check: count sits at right edge of card, media icons sit a consistent distance from the left across rows regardless of title/description length.

### 2b. `site/website/assets/explorer.css` — mobile media query

**Old (lines 230–234, inside `@media (max-width:760px)`):**

```css
  .place-row{display:grid;grid-template-columns:18px minmax(0,1fr) auto;gap:10px;min-height:84px}
  .place-main{min-width:0;max-width:none}
  .place-media{grid-column:3;grid-row:1 / span 2;margin-left:0}
  .place-thumb,.place-map-button,.place-map-thumb{width:54px;height:54px}
  .place-count{grid-column:2;margin-left:0;justify-self:start}
```

**New:**

```css
  .place-row{display:grid;grid-template-columns:18px minmax(0,1fr) auto;column-gap:10px;row-gap:6px;min-height:84px}
  .place-main{min-width:0;max-width:none;grid-column:2;grid-row:1}
  .place-media{grid-column:3;grid-row:1 / span 2;justify-self:end}
  .place-thumb,.place-map-button,.place-map-thumb{width:54px;height:54px}
  .place-count{grid-column:2;grid-row:2;margin-left:0;justify-self:start}
```

Mobile keeps the 3-column compact form (marker | text/count | media) and explicitly pins each child to its grid cell, since the desktop grid now declares five columns.

### 2c. `site/website/assets/phase2.css` — same edits, kept in sync

phase2.css duplicates the explorer.css rules and is loaded last in `base.njk`, so it wins in the cascade. Mirror both edits in phase2.css verbatim.

- Lines 70–80 (block beginning `.place-list{display:grid;grid-template-columns:1fr;gap:8px}` and ending with the original `.place-media{flex:0 0 auto;...}`): replace with the new desktop block from §2a.
- Lines 133–137 (inside `@media (max-width:760px)`): replace with the new mobile block from §2b.

---

## 3. Header "Updated …" date auto-updates each build

### 3a. New file: `site/website/_data/build.js`

```js
module.exports = () => {
  const now = new Date();
  const formatter = new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "long", year: "numeric" });
  return { date: formatter.format(now) };
};
```

Format: `16 May 2026` — matches the prior hand-typed shape ("25 April 2026").

### 3b. `site/website/_includes/partials/siteheader.njk`

**Old (lines 28–32):**

```njk
      <span class="brand-title">Gurney Genealogy Library</span>
      <span class="brand-meta">
        Updated {{ updated }} by
        <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAdNpQL5UQVNMT1AzQjZQUEJQRlZJVUc0NFgzWkg1QS4u"
           target="_blank" rel="noopener">Allen Gurney</a>
      </span>
```

**New:**

```njk
      <span class="brand-title">Gurney Genealogy Library</span>
      <span class="brand-meta">
        Updated {{ build.date }} by
        <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAdNpQL5UQVNMT1AzQjZQUEJQRlZJVUc0NFgzWkg1QS4u"
           target="_blank" rel="noopener">Allen Gurney</a>
      </span>
```

After this change, the per-page `updated:` front-matter keys are no longer read. They are harmless but inert. §7 removes them.

### 3c. Reviewer note on caching

`build.js` is evaluated once per Eleventy run (each `npm run build`). The serve/watch dev modes will hold the value from the first build until the watcher restarts the process — that's fine; the public artefact is the build output.

---

## 4. Sources page stats — rename, recompute, add tooltips

### 4a. `site/website/_data/sourceStats.js`

**Old (entire file):**

```js
const sources = require("./sourcesCatalog.json");

module.exports = {
  sourceCount: sources.length,
  fullCorpusCount: sources.filter(source => source.corpusStatus === "full").length,
  externalLinkCount: sources.filter(source => source.url).length,
  validationCount: sources.filter(source => source.validationPath).length,
};
```

**New (entire file):**

```js
const sources = require("./sourcesCatalog.json");

const hasPath = (value, prefix) => typeof value === "string" && value.startsWith(prefix);

const corpusItemCount = sources.filter(source => hasPath(source.corpusPath, "sources/corpus/")).length;
const corpusSupplementItemCount = sources.filter(source => hasPath(source.corpusPath, "sources/corpus_supplement/")).length;
const mediaItemCount = sources.filter(source => hasPath(source.mediaPath, "sources/media/")).length;

module.exports = {
  sourceCount: sources.length,
  fullCorpusCount: sources.filter(source => source.corpusStatus === "full").length,
  corpusItemCount,
  corpusSupplementItemCount,
  mediaItemCount,
  libraryHoldingsCount: corpusItemCount + corpusSupplementItemCount + mediaItemCount,
  externalLinkCount: sources.filter(source => source.url).length,
  validationCount: sources.filter(source => source.validationPath).length,
};
```

Counting method (explicit so reviewer can sanity-check):
- corpus = sources whose `corpusPath` begins with `sources/corpus/`.
- corpus supplement = sources whose `corpusPath` begins with `sources/corpus_supplement/`.
- media = sources whose `mediaPath` begins with `sources/media/`.
- library holdings = sum of the three counts (an item with both a corpus file and an associated media asset is counted once per artefact, not deduped to a single source — this matches the "sum of what is in corpus, corpus supplement, and media" specification).
- `fullCorpusCount` is retained for any future callers (validate-site script does not currently reference it; left in place to avoid downstream breakage).

Current snapshot at v45 prep time, on the working tree `_data/sourcesCatalog.json`:
- corpusItemCount = 12
- corpusSupplementItemCount = 53
- mediaItemCount = 22
- libraryHoldingsCount = 87
- sourceCount = 203
- externalLinkCount = (existing calc, unchanged)
- validationCount = (existing calc, unchanged)

### 4b. `site/website/key-research/sources.njk` — stats strip

**Old (lines 18–23):**

```njk
  <div class="stats-strip compact-stats">
    <div class="stat"><span class="label">Sources</span><span class="value">{{ sourceStats.sourceCount }}</span></div>
    <div class="stat"><span class="label">Full corpus</span><span class="value">{{ sourceStats.fullCorpusCount }}</span></div>
    <div class="stat"><span class="label">External links</span><span class="value">{{ sourceStats.externalLinkCount }}</span></div>
    <div class="stat"><span class="label">Validations</span><span class="value">{{ sourceStats.validationCount }}</span></div>
  </div>
```

**New:**

```njk
  <div class="stats-strip compact-stats">
    <div class="stat" title="Total source registry entries — every cited source tracked in the library, whether the artefact is held locally or only referenced externally."><span class="label">Sources</span><span class="value">{{ sourceStats.sourceCount }}</span></div>
    <div class="stat" title="Full text of non-copyright works, text extracts, primary source imagery, and other media in the genealogy library."><span class="label">Library holdings</span><span class="value">{{ sourceStats.libraryHoldingsCount }}</span></div>
    <div class="stat" title="Sources reachable through an external URL — a publisher, archive, or institutional host page."><span class="label">External links</span><span class="value">{{ sourceStats.externalLinkCount }}</span></div>
    <div class="stat" title="Sources with a validation note in sources/validations/ recording what was examined and how identity was confirmed."><span class="label">Validations</span><span class="value">{{ sourceStats.validationCount }}</span></div>
  </div>
```

Wording note: the user-supplied "non-copyrights" was corrected to "non-copyright" in the published tooltip. Tooltip prose follows the user's intent (full text + extracts + imagery + other media). The exact strings above are what ship; reviewer should sign off on the wording.

Tooltips use the native `title` attribute. Accessibility uplift (visible `<details>` info badge or `aria-describedby`) is out of scope for v45; flag as a follow-on if desired.

---

## 5. Build / validation expectations

Phase 2 application should, after edits, run from `site/website/`:

```text
npm run build
npm run validate:site
```

Expected results:
- Build succeeds; no Nunjucks template error for undefined `build` or `researchCompanion`.
- `site/website/_site/index.html` and any factsheet HTML show `Updated <today's date> by Allen Gurney` in the header.
- Factsheet pages no longer show the bottom "View research companion" pill row; the upper-right area renders the generation selector with "View research notes" beneath it.
- `key-research/sources.html` shows `Library holdings` with value `87` (or current sum) and renders `title` tooltips on each of the four stat cells.
- `maps-and-lists/places.html` row icons line up vertically across rows regardless of title/description length.

If any check fails, stop and surface the failure with the failing file path and error message rather than re-running.

---

## 6. Out of scope for v45
- Accessibility enhancement of the stat tooltips beyond native `title`.
- A clickable info icon next to each stat label.
- Reordering of the four sources stats.
- Reformatting `sources/corpus_supplement/` paths or normalizing the empty-string `corpusStatus` row.
- Any change to `data/sources.json` schema.

---

## 7. Cleanup — remove inert `updated:` front-matter (optional, same patchset)

Once §3 lands, the per-page `updated:` keys are dead. Remove them in these files (one-line deletions in YAML front-matter):

- `site/website/index.njk` (line 5)
- `site/website/key-research/sources.njk` (line 10)
- `site/website/maps-and-lists/places.njk` (line 10)
- `site/website/maps-and-lists/ancestor-map.njk` (line 10)
- `site/website/maps-and-lists/ancestor-table.njk` (line 10)
- `site/website/research/places/place-pages.njk` (line 14)
- Every `site/website/fact-sheets/g*-*.md` that contains `updated: <date>` in its front-matter (identified by `grep -l "^updated:" site/website/fact-sheets/g*.md`).

Do **not** touch:
- `research/companions/*-fact-sheet.md` files where the date is part of body prose ("Captured 25 April 2026"). Those reference a real capture event, not a build date.
- `sources/...` files.
- `_site/` artefacts — these regenerate on the next build.

If the reviewer prefers to defer this cleanup, drop §7 and ship §§1–6 only; the inert keys will be ignored by Eleventy.

---

## 8. Reviewer questions
1. Is `87` the right magnitude for "Library holdings" as currently defined, or should the sum dedupe by sourceId (e.g., a source with both a corpus file and a media asset counted once)? Patchset currently counts artefacts, not sources.
2. Is the "non-copyright" rewording of "non-copyrights" acceptable? Patchset assumes yes.
3. Should §7 ship with v45 or be split into v46? Default: ship together.
4. Date format `16 May 2026` (day-month-year, no comma) — keep, or switch to `May 16, 2026`? Default: keep the day-month-year shape that matches what was hand-typed before.
