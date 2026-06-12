---
name: familysearch-fulltext-research
description: Operational recipes for FamilySearch Full-Text Search (FTS) research — query syntax and URL parameters, film/image-group (DGS) constructs, full-resolution image download API, browser extraction techniques, and known failure modes. Read this before any FamilySearch FTS task to avoid re-deriving the procedures.
---

Proven procedures for working FamilySearch Full-Text Search with an authenticated browser session (Claude-in-Chrome or equivalent). Established and battle-tested across the June 2026 John Gurney (G13) campaign. The companion *content-reliability* notes (what machine transcripts can and cannot be trusted for, catalogued false positives) live in `sources/validations/familysearch-fulltext-search.md`.

## 1. Query construction (URL-driven — no UI needed)

Results page accepts everything as URL parameters:

```
https://www.familysearch.org/en/search/full-text/results?count=100&q.text=<TERMS>[&q.groupName=<DGS>][&c.recordYear1=on&f.recordYear0=<CENTURY>]
```

- `q.text` — the search terms, URL-encoded. Operators:
  - `*` root wildcard (`Gurn*`), `?` single character (`Jens?n`)
  - `+term` = REQUIRED. **Space-separated terms are ranked-OR, not AND** — for co-occurrence always `+` every term: `%2BGurn%2A%20%2BDereham`
  - `"exact phrase"` (encode quotes `%22`). Rare-name exact phrases are the highest-yield probe type (`"Lyon Gurney"`).
- `q.groupName=<DGS>` — scopes the query to one film/image group (e.g. `004389277`). This is the film-sweep workhorse.
- `f.recordYear0=1600&c.recordYear1=on` — century filter (here: 1600s). Years are OCR-read from document text, so the filter is approximate in both directions.
- `count=100` — max results per page.
- If the URL form ever errors, the landing-page form at `/en/search/full-text` has "Keywords" and "Image Group Number (DGS)" fields — but its collection-title autocomplete does not respond to scripted input; don't fight it.

**Getting a film's DGS number:** open any FTS result from the film and click the Information button on the record page; match `Image Group Number ... (\d+)` in the page text. (Group IDs like `M9S7-H4T` in result URLs are *not* DGS numbers.)

**Wildcard calibration:** `Gurn*` + `Gourn*` + `Garn*` outperforms hand-built spelling lists (a nine-variant manual sweep added nothing). But `G?rn?*` is too broad — swamped by *Garner*.

## 2. Reading results and record pages (shadow DOM)

All FTS content renders in nested shadow roots; `get_page_text` and plain `innerText` return only the chrome. Use a recursive shadow-root text walker via the JavaScript tool:

```js
function dT(root, depth) {
  if (depth > 25) return '';
  let out = '';
  const walk = (n) => {
    if (n.nodeType === Node.TEXT_NODE) { out += n.textContent + ' '; return; }
    if (n.nodeType !== Node.ELEMENT_NODE) return;
    if (['SCRIPT','STYLE','NOSCRIPT'].includes(n.tagName)) return;
    if (n.shadowRoot) out += dT(n.shadowRoot, depth+1);
    n.childNodes.forEach(walk);
  };
  root.childNodes && root.childNodes.forEach(walk);
  return out;
}
```

- **Results page parsing:** slice the deep text between `'Edit Search'` and `'Results per page'`; split on `/Matches \(\d+\)/` — each chunk is one card (title … snippet … `Years : …`). Card-title anchors (deep-walk `A` tags with non-empty text and href containing `ark:/61903/3:1`) align one-to-one with cards, in order.
- **Record page parsing:** the machine transcript begins right after the marker `'Editing is unavailable'` and ends at `'Feedback'`. The image number is the numeric `INPUT` value (deep-walk inputs). The match's character offset within the transcript approximates its physical position on the page (a match at ~96% of the text flow = bottom of the right-hand page) — use this to target crops for paleography.
- Tool results truncate long strings around ~1,000 characters — return transcripts in slices, or stash in `window.__x` and read in chunks.
- Clicking the Information tab switches the view and unloads the transcript — extract the transcript *before* opening Information.

## 3. Full-resolution image downloads (the das/v2 API)

The viewer's own download dialog is unreliable under automation. The working path:

1. From any logged-in familysearch.org page, fire (per image): `fetch('https://www.familysearch.org/das/v2/<3:1:ARK-ID>/dist.jpg', {credentials:'include'})`. The fetch *throws* (CORS at the redirect) — expected and harmless.
2. The das request 503-redirects to a **presigned S3 URL** (`...s3.amazonaws.com/...TH-.../dist.jpg?X-Amz-...`, ~1-hour expiry). Read it from the browser network log (`read_network_requests`, pattern `dist.jpg`). Requests appear in fire order, so a sequential loop over many ark IDs (600 ms apart) maps das→S3 pairs reliably — batch all images in one pass.
3. Download each presigned URL with PowerShell `Invoke-WebRequest -Uri $u -OutFile ...` (no auth needed; URL carries the signature). **TLS note:** if `Invoke-WebRequest` fails with an SSL/TLS channel error on Windows PowerShell 5.1, set `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12` first.
4. Images come down at full archival resolution (typically 3,500–5,600 px wide, 0.7–2 MB JPG).

The deepzoom tile URLs visible in the viewer (`.../deepzoomcloud/dz/v1/apid:TH-.../image_files/...`) expose the current image's apid but not its neighbours'.

**Neighbour-page navigation (gap closed 2026-06-11):** the *standard image viewer* (the ark URL **without** `?view=fullText`) has "Next Image" / "Previous Image" buttons that DO respond to scripted `.click()`. Each click updates the URL to the neighbour's ark with `i=<0-based index>` — so from any carded hit, walk to an arbitrary image number and harvest its ark for transcript reads or das/v2 pulls. Clicks can be looped inside one JS call (~700 ms apart; keep batches ≤ ~18 to stay under the CDP timeout). (The fullText view lacks these buttons; arrow keys and the image-number input still ignore scripted events; the filmstrip is virtualized and resists scripted scrolling; passing `?i=N` in the URL is display-only and does NOT jump.)

**Entering a film at image 1 (no search hit needed):** the Explore Images app result page `/records/images/search-results?imageGroupNumbers=<DGS>` carries a single `/ark:/61903/3:1:…` link — the film's FIRST image. Open it in the standard viewer and Next-click forward. This makes any film walkable from the front even when FTS returns no usable card (e.g., medieval Latin registers). Worked example: Register Harsyk (DGS 008076261) — entry ark 3:1:3Q9M-CSN8-1WMR-R; note its interleaved modern annotation pages (testator names + years per folio) index well in FTS even where the medieval text is salad.

**Other operational notes:**
- **Zero hits ≠ negative until coverage is confirmed.** A film absent from FTS returns zero for *every* query. Before logging a film-scoped negative, probe a common word (`%2Bwife`) scoped to the same DGS; a healthy hit list confirms coverage.
- **One DGS can carry several collections** (e.g. 004389278 = Earsham + Docking + Diss court records). `q.groupName` scopes to the physical film, so triage cards by collection title.
- **Mapping a register series to DGS numbers:** the catalog film-number search `/search/catalog/results?q.filmNumber=<DGS, no leading zeros>` resolves to the parent catalog record; its Film/Digital Notes table (set the rows-per-page `<select>` to 100; "Go to next Page" buttons are clickable) enumerates every volume with film + DGS. Used to map the whole NCC registered-copy-wills year series in one pass (record `koha:278818`).

## 4. Paleography staging convention

For images needing expert transcription: stage under `sources/intake/paleography-staging/` — full-res JPGs in `images/`, one README with a TOC and per-packet briefs (citation + ark links, the machine-transcript snippet as a finding aid, position-targeting hints from §2, and the specific questions to answer). Results come back as `packet-NN-*.md` files in the same directory and are integrated into research companions.

**Disposition when a batch completes** (treat `sources/intake/done/` as a recycle bin — nothing referenced long-term may live only there): packet reports → `sources/corpus_supplement/paleo-<YYYY-MM>-packet-NN-<slug>.md`; master images → `sources/media/<record-set-slug>/_local/` with a committed `README.md` stub per folder (filenames, FamilySearch-terms reason, retrieval arks); diagnostic crops (derivative, regenerable) → `sources/media/_local/<batch-slug>-working-crops/`; the briefs README → a dated folder under `sources/intake/done/`; then fix every repo reference from the staging paths to the durable ones (grep `paleography-staging`). Precedent: the 2026-06 batch (`paleo-2026-06-packet-01..09`).

## 5. Failure modes (check before believing a hit)

Full catalogue with examples in `sources/validations/familysearch-fulltext-search.md`. Headlines: Latin court hand transcribes as word salad (thin hit counts ≠ absence); lookalike names are systematic (*Jernegan*→"Gurney" at Costessey, *Atturney*→"At-Gurney", place-name *Gurnet's Nose*; real distinct surnames Gurnell/Garnsey/Garner ride the wildcards); card year-lists mix document dates with stray numbers; never promote a forename or kinship from a Latin-entry transcript without an image read.

## See also
- `sources/validations/familysearch-fulltext-search.md` — content-reliability notes and false-positive catalogue
- `research/people/g13-john-gurney-fact-sheet.research.md` — campaign session entries (worked examples of every technique above)
- `.claude/skills/familysearch-export-review/SKILL.md`, `.claude/skills/familysearch-tree-updates/SKILL.md` — the tree/export-side FamilySearch skills
