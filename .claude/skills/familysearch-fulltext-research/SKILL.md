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

**JSON API — batch many probes without the UI (added 2026-06-13).** The results page calls a clean JSON endpoint; hit it directly with `fetch(..., {credentials:'include'})` from any logged-in familysearch.org tab and skip the shadow-DOM entirely:

```
https://www.familysearch.org/service/search/fulltext/search?count=50&m.defaultFacets=on&m.queryRequireDefault=on&offset=0&q.text=<URL-encoded query>
```

Response shape: `results` = total hit count; `entries[]`, each with `id` (the `3:1:` ark), `collectionTitle`, and `content.{recordDate, recordType, recordPlace, title, textDocument (full machine transcript), highlightTexts (match snippets array)}`. One `javascript_tool` call can loop dozens of `q.text` probes (~400 ms apart), stash raw results in `window.__x`, and return a compact triage digest — far faster than navigating per query. Filter/triage client-side on `recordType` (e.g. Legal/Probate/Properties), `recordPlace`, and a parsed year from `recordDate`. `count` and `offset` paginate. Same `q.text` operators/`q.groupName` scoping as the URL form. **Cap: a single request returns at most ~100 entries — `count=300` returns an empty `entries` array (and no `results` field). Page with `offset` in steps of 100 rather than requesting a larger `count`.** (Also: build `q.text` with `encodeURIComponent` on the *raw* query — do not pre-encode `+` to `%2B` and then `encodeURIComponent` it again, or the AND-operator double-encodes and the probe returns zero.)

**Co-occurrence caveat (calibrated 2026-06-13):** `+Gurn* +"<place>"` AND-probes do **not** surface corrupt-transcript manuscript records — place + surname only co-occur in *clean-OCR printed* books (Burke, Visitations, Blomefield) and cross-collection false positives (e.g. Liège "de Gurnay", a Walloon family). The high-yield FTS vector for a Norfolk surname is **typed abstract/index typescripts** (clean OCR), not place/Latin co-occurrence over manuscript films. See `sources/intake/.../extended-fts-discovery-campaign.md` (2026-06 batch) for the full probe matrix and negative.

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
- **Mapping a register series to DGS numbers:** the catalog film-number search `/search/catalog/results?q.filmNumber=<DGS, no leading zeros>` resolves to the parent catalog record; its Film/Digital Notes table (set the rows-per-page `<select>` to 100; "Go to next Page" buttons are clickable) enumerates every volume with film + DGS. Used to map the whole NCC registered-copy-wills year series in one pass (record `koha:278818`). The vol→DGS mapping is offset-ambiguous in the flattened table text; anchor on a confirmed pair (vol. 116–118 / 1621–1623 = DGS 008470484) to fix the offset. The 1624–1637 gap (vols 119–130), resolved 2026-06-14: 1624–25=008470970, 1626=008219670, 1627–28=008076511, 1629=008076512, 1630=008076513, 1631–32=008076514, 1633=008472222, 1634=008076861, 1635=008472223, 1636=008076860, 1637=008076859 (1638–39=008076858; 1643–46=008402405; 1647–51=007904832).

## 4. Paleography staging convention

For crop generation, enhancement sheets, transcription posture, and durable handwriting lessons, also read `.claude/skills/paleography-analysis/SKILL.md`.

For images needing expert transcription: stage under `sources/intake/paleography-staging/` — full-res JPGs in `images/`, one README with a TOC and per-packet briefs (citation + ark links, the machine-transcript snippet as a finding aid, position-targeting hints from §2, and the specific questions to answer). Results come back as `packet-NN-*.md` files in the same directory and are integrated into research companions.

**Disposition when a batch completes** (treat `sources/intake/done/` as a recycle bin — nothing referenced long-term may live only there): packet reports → `sources/corpus_supplement/paleo-<YYYY-MM>-packet-NN-<slug>.md`; master images → `sources/media/<record-set-slug>/_local/` with a committed `README.md` stub per folder (filenames, FamilySearch-terms reason, retrieval arks); diagnostic crops (derivative, regenerable) → `sources/media/_local/<batch-slug>-working-crops/`; the briefs README → a dated folder under `sources/intake/done/`; then fix every repo reference from the staging paths to the durable ones (grep `paleography-staging`). Precedent: the 2026-06 batch (`paleo-2026-06-packet-01..09`).

## 5. Failure modes (check before believing a hit)

Full catalogue with examples in `sources/validations/familysearch-fulltext-search.md`. Headlines: Latin court hand transcribes as word salad (thin hit counts ≠ absence); lookalike names are systematic (*Jernegan*→"Gurney" at Costessey, *Atturney*→"At-Gurney", place-name *Gurnet's Nose*; real distinct surnames Gurnell/Garnsey/Garner ride the wildcards); card year-lists mix document dates with stray numbers; never promote a forename or kinship from a Latin-entry transcript without an image read.

**Dictionary-snapped OCR + local surname populations (calibrated 2026-06-13).** These collections' handwriting OCR is **name-dictionary-aided**, so a poorly-read surname snaps to the nearest *dictionary* surname — one manuscript "Gurney" sprays across `Gorney/Gorne/Gorner/Gurnee/Gornesly/Gorness/Gorneses` on a single page. Two consequences for building a term set:
- **Include snap-targets that are NOT an established surname in that geography** (Norfolk has no "Gorney" family, so `Gorn*` safely recovers mangled Gurneys) and **exclude snap-targets that have their own local population** (`Garn*` → the real Garner/Garnett family; this is why the long-standing `Gurn*/Gourn*/Gorn*` set is well-tuned and `Garn*` swamps). The safe set is **geography-specific** — re-judge it per county.
- **Disambiguate large same-surname populations before promoting.** In Norwich, most "Gurney" hits are the famous **Quaker banking Gurneys** (Hudson Gurney, John Gurney merchant, "May Gurney & Co"), a family distinct from the West Barsham gentry line — so a Norwich hit is *more* likely them than the target line. Use period/parish to separate (the Quaker line rises in the later 17th c.).

**Read the whole transcript for context, don't binary-match the surname.** The match string alone (`Gurney`) is a weak signal in salad; mine each hit's full `content.textDocument` for buried **place names, forenames, and associated families** (`+Barsham|Ellingham|Harpley|… | Lovell|Spelman|Calthorpe|Lestrange|…`) to judge relevance. This both rescues relevance the surname alone misses **and** exposes false positives a binary place-match would mis-promote (e.g. "Gornsey" = *Guernsey*, not Gurney; "Hardingham" as a juror's **surname**, not the manor). Yield tracks OCR quality: context-mining rescues **clean printed** calendars/indexes but rarely manuscript salad — and a "1910 deeds" film can in fact be a clean-OCR medieval–Tudor deeds *calendar* worth a full sweep (DGS 004389182).

## See also
- `sources/validations/familysearch-fulltext-search.md` — content-reliability notes and false-positive catalogue
- `research/people/g13-john-gurney-fact-sheet.research.md` — campaign session entries (worked examples of every technique above)
- `.claude/skills/familysearch-export-review/SKILL.md`, `.claude/skills/familysearch-tree-updates/SKILL.md` — the tree/export-side FamilySearch skills

## Appendix: Codex-specific access notes

Use this as the standard Codex path for FamilySearch browser work. Start here; do not spend time trying to attach to an arbitrary existing Chrome window unless the user has explicitly already opened a remote-debug Chrome.

### Default access procedure

1. Launch a dedicated Chrome profile on the default Codex port (`9223`) from PowerShell:

```powershell
$chrome = "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
$profile = Join-Path $env:TEMP "codex-familysearch-chrome-profile"
Start-Process -FilePath $chrome -ArgumentList "--remote-debugging-port=9223 --user-data-dir=`"$profile`" --no-first-run --new-window https://www.familysearch.org/en/search/full-text"
```

2. Have the user sign into FamilySearch in that visible Chrome window. If Chrome opens a first-run or Google-sync page, open the FamilySearch URL in the same window and continue there.
3. Verify the DevTools endpoint before any CDP work:

```powershell
Invoke-RestMethod http://127.0.0.1:9223/json/version
Invoke-RestMethod http://127.0.0.1:9223/json/list
```

The endpoint is usable only if `/json/version` returns browser metadata. A visible Chrome window is not evidence of a usable DevTools listener.

4. In Codex `node_repl`, attach with Playwright CDP:

```js
const { chromium } = await import("playwright");
const browser = await chromium.connectOverCDP("http://127.0.0.1:9223");
const context = browser.contexts()[0];
const page = context.pages().find(p => p.url().includes("familysearch.org")) || context.pages()[0];
```

5. Run FamilySearch reads inside that authenticated page: use the recursive shadow-DOM walker from this skill for page text, use the JSON FTS endpoint with `credentials:'include'` for batch probes, and extract the transcript before opening the Information tab.

### Bounded recovery

- If `/json/version` or `/json/list` returns `404`, the port is not a DevTools endpoint. Do not retry CDP. Relaunch once with a fresh profile and port `9224`; if that also fails, stop and report the access problem.
- If port `9223` is occupied, check `/json/version`. If it is usable, attach to it; if not, use `9224` with profile folder `codex-familysearch-chrome-profile-9224`.
- If `Start-Process` opens Chrome but no listener appears, keep the Chrome flags as one explicit argument string as shown above; do not split them into a PowerShell array for this workflow.
- If the Node bridge cannot write into the OneDrive checkout (`EPERM`), write captures to `nodeRepl.tmpDir`, then copy completed files into the repo with PowerShell.

### Image downloads

1. Trigger the DAS request from the authenticated FamilySearch tab:

```js
await page.evaluate(ark => fetch(`https://www.familysearch.org/das/v2/${ark}/dist.jpg`, { credentials: "include" }).catch(() => null), "3:1:ARK-HERE");
```

Use the full `3:1:` ARK prefix; omitting it can return `404`.

2. Capture the redirected presigned S3 `dist.jpg` URL from CDP network events.
3. Download that S3 URL with PowerShell:

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Uri $signedUrl -OutFile $outFile
```

If PowerShell cannot download it, open the captured S3 URL in the CDP-connected Chrome with `page.goto(...)`, read `response.body()`, write the bytes under `nodeRepl.tmpDir`, then copy the finished JPG into the repo.

Do not keep signed S3 URL manifests as durable artefacts; the tokens expire and are sensitive-ish noise. Keep downloaded JPGs plus ARK, DGS, image number, and citation. Before keeping duplicate `fullres` files, compare byte sizes with existing JPGs; the existing browser capture may already be the same DAS-resolution image.

### Navigation and batching

- For neighbor pages, prefer the standard viewer. If Previous/Next buttons are awkward in Codex automation, click grid buttons such as `Go to image 339` to obtain the neighboring ARK.
- Chunk long extraction runs and checkpoint after each record or small batch. Broad DGS sweeps can time out before returning any usable result.
