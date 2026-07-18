---
name: familysearch-fulltext-research
description: Operational recipes for FamilySearch Full-Text Search (FTS) research — query syntax and URL parameters, film/image-group (DGS) constructs, full-resolution image download API, browser extraction techniques, and known failure modes. Read this before any FamilySearch FTS task to avoid re-deriving the procedures.
---

Proven procedures for working FamilySearch Full-Text Search with an authenticated browser session (Claude-in-Chrome or equivalent). Established and battle-tested across the June 2026 John Gurney (G13) campaign. The companion *content-reliability* notes (what machine transcripts can and cannot be trusted for, catalogued false positives) live in `sources/validations/familysearch-fulltext-search.md`.

> **Search *strategy* (name variants, wildcarding, token/transitive anchoring, source-awareness) is source-agnostic and lives in [`online-discovery-strategy`](../online-discovery-strategy/SKILL.md) — read that first.** This file is FamilySearch FTS *mechanics* only: endpoints, parameters, extraction, image download, DGS mapping.

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
- `q.fullName=<surname>` — searches FamilySearch's **extracted person-name index**, not raw OCR. This is the high-yield vector for finding a person in the manuscript-salad era: a name can surface from a 1600–1640 will/deed/court roll even when the surrounding text transcribes as court-hand salad, because the name entity was extracted separately. Works on the JSON service too (`&q.fullName=rivett`). For a windowed search use the year filter on **`q.text`** (not `q.fullName`, which takes only the century filter): activate with `c.recordYear1=on`, then `f.recordYear0=<base>` **before** `f.recordYear1=<start>~<end>`, repeating the pair for multiple windows (order and the toggle both matter — omit either and it returns zero). **Caveat — absence from `q.fullName` is not absence:** name-extraction coverage is partial. (Worked 2026-06: a `fullName=rivett` 1600–1638 sweep cleanly surfaced a 1630 Gressenhall NCC will where "Richard Rivett" appears only as a witness/son-in-law — but the 1584/1597 NCC Garveston Rivett wills, present in Ancestry's Norfolk probate index, are *not* name-extracted in FTS, so a `fullName` miss still needs the film/original.)
- `f.recordYear0=1600&c.recordYear1=on` — century filter (here: 1600s). Years are OCR-read from document text, so the filter is approximate in both directions.
- `count=100` — max results per page.
- If the URL form ever errors, the landing-page form at `/en/search/full-text` has "Keywords" and "Image Group Number (DGS)" fields — but its collection-title autocomplete does not respond to scripted input; don't fight it.

**Verify authentication once, at the start of FTS work.** An unauthenticated session silently truncates results into false negatives: `q.fullName=gurney` returns ≈ 348k authenticated vs ~460 unauthenticated. Re-confirm any FTS negative under an authenticated session before trusting it. (The general posture — a source miss is a pivot, not a negative — is in `online-discovery-strategy`.)

**Getting a film's DGS number:** open any FTS result from the film and click the Information button on the record page; match `Image Group Number ... (\d+)` in the page text. (Group IDs like `M9S7-H4T` in result URLs are *not* DGS numbers.)

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
- Tool results truncate long strings around ~1,000 characters — return transcripts in slices, or stash in `window.__x` and read in chunks. **Or swap the text into the page body** (`document.body.innerText = window.__x`) and read it with `get_page_text`: that reads the rendered DOM, not a JS return value, so it bypasses the ~1,000-char return cap in one call.
- Clicking the Information tab switches the view and unloads the transcript — extract the transcript *before* opening Information.

**JSON API — batch many probes without the UI (added 2026-06-13).** The results page calls a clean JSON endpoint; hit it directly with `fetch(..., {credentials:'include'})` from any logged-in familysearch.org tab and skip the shadow-DOM entirely:

```
https://www.familysearch.org/service/search/fulltext/search?count=50&m.defaultFacets=on&m.queryRequireDefault=on&offset=0&q.text=<URL-encoded query>
```

Response shape: `results` = total hit count; `entries[]`, each with `id` (the `3:1:` ark), `collectionTitle`, and `content.{recordDate, recordType, recordPlace, title, textDocument (full machine transcript), highlightTexts (match snippets array)}`. One `javascript_tool` call can loop dozens of `q.text` probes (~400 ms apart), stash raw results in `window.__x`, and return a compact triage digest — far faster than navigating per query. Filter/triage client-side on `recordType` (e.g. Legal/Probate/Properties), `recordPlace`, and a parsed year from `recordDate`. `count` and `offset` paginate. Same `q.text` operators/`q.groupName` scoping as the URL form. **Cap: a single request returns at most ~100 entries — `count=300` returns an empty `entries` array (and no `results` field). Page with `offset` in steps of 100 rather than requesting a larger `count`.** (Also: build `q.text` with `encodeURIComponent` on the *raw* query — do not pre-encode `+` to `%2B` and then `encodeURIComponent` it again, or the AND-operator double-encodes and the probe returns zero.)

## 3. Full-resolution image downloads (the das/v2 API)

The viewer's own download dialog is unreliable under automation. The working path:

1. From any logged-in familysearch.org page, fire (per image): `fetch('https://www.familysearch.org/das/v2/<3:1:ARK-ID>/dist.jpg', {credentials:'include'})`. The fetch *throws* (CORS at the redirect) — expected and harmless.
2. The das request 503-redirects to a **presigned S3 URL** (`...s3.amazonaws.com/...TH-.../dist.jpg?X-Amz-...`, ~1-hour expiry). Read it from the browser network log (`read_network_requests`, pattern `dist.jpg`). Requests appear in fire order, so a sequential loop over many ark IDs (600 ms apart) maps das→S3 pairs reliably — batch all images in one pass.
3. Download each presigned URL with PowerShell `Invoke-WebRequest -Uri $u -OutFile ...` (no auth needed; URL carries the signature). **TLS note:** if `Invoke-WebRequest` fails with an SSL/TLS channel error on Windows PowerShell 5.1, set `[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12` first.
4. Images come down at full archival resolution (typically 3,500–5,600 px wide, 0.7–2 MB JPG).

The deepzoom tile URLs visible in the viewer (`.../deepzoomcloud/dz/v1/apid:TH-.../image_files/...`) expose the current image's apid but not its neighbours'.

**Batch many images per round trip — fire the das requests *concurrently* (the throughput unlock, 2026-06).** Under the Claude-in-Chrome MCP the network log surfaces only ~one fresh das→S3 redirect per *sequential, awaited* das fetch, and the das/v2 response is cacheable, so a sequential loop re-reads the cache and only the first ark redirects. Two fixes together make batching reliable: (a) fire all arks at once with `Promise.all(arks.map(a => fetch(\`https://www.familysearch.org/das/v2/${a}/dist.jpg?cb=${Date.now()}_${i}\`, {credentials:'include', cache:'no-store'}).catch(()=>null)))` — concurrent firing logs *all* the S3 redirects; the `?cb=` cache-buster + `cache:'no-store'` defeats the das cache. (b) To pull "image N" without returning arks past the browser MCP's privacy guard, look the ark up from `window.__imgs[N-1]` *inside* the page and fetch it there, returning only a fired-count; then read the presigned S3 URLs from the network log (they carry `TH-…` ids, not arks/query-bearing FS URLs, so they pass the guard). The S3 requests appear in **fire order**, so map `TH-id → image number` positionally. One `read_network_requests` (pattern `pipe-storage-das-cloud-prod-dasS3`) then yields ~6–14 presigned URLs to hand to one PowerShell `Invoke-WebRequest` loop. Net cost ≈ fire + one network read + one download ≈ 0.3–0.5 tool calls per image.

**Caveat — the in-memory `window.__imgs` index can be off by ~one leaf from the manuscript page.** Confirmed 2026-06: opening ark `…SXB` placed it at array index 1709 and the "preceding" ark `…3Z` resolved (via das) to the *same scan* already pulled as the "image 1710" SXB target — i.e. the array's index-to-leaf alignment, and das's ark-to-scan mapping, can both drift by one and can collapse adjacent arks onto one physical scan. **Anchor on a confirmed ark, not the image number:** verify `window.__imgs[N-1].ark` against a known page before trusting the label, and treat duplicate byte-sizes across "adjacent" pulls as a collapsed/duplicate scan.

**Neighbour-page navigation (gap closed 2026-06-11):** the *standard image viewer* (the ark URL **without** `?view=fullText`) has "Next Image" / "Previous Image" buttons that DO respond to scripted `.click()`. Each click updates the URL to the neighbour's ark with `i=<0-based index>` — so from any carded hit, walk to an arbitrary image number and harvest its ark for transcript reads or das/v2 pulls. Clicks can be looped inside one JS call (~700 ms apart; keep batches ≤ ~18 to stay under the CDP timeout). (The fullText view lacks these buttons; arrow keys and the image-number input still ignore scripted events; the filmstrip is virtualized and resists scripted scrolling; passing `?i=N` in the URL is display-only and does NOT jump.)

**Entering a film at image 1 (no search hit needed):** the Explore Images app result page `/records/images/search-results?imageGroupNumbers=<DGS>` carries a single `/ark:/61903/3:1:…` link — the film's FIRST image. Open it in the standard viewer and Next-click forward. This makes any film walkable from the front even when FTS returns no usable card (e.g., medieval Latin registers). Worked example: Register Harsyk (DGS 008076261) — entry ark 3:1:3Q9M-CSN8-1WMR-R; note its interleaved modern annotation pages (testator names + years per folio) index well in FTS even where the medieval text is salad.

**Jump to a specific image NUMBER — the in-page image array (the fast unlock, added 2026-06-16).** When the target is "image N of a film" (a known image number / folio, e.g. an inventory at image 516, a will at a register folio) and you do NOT already have that image's ark, do NOT Next-walk hundreds of pages and do NOT reverse-engineer the viewer's network/Apollo layer. The standard viewer holds the film's **entire image list in memory** as a JS array of `{src, alt, id, p200, ark, index}` objects (one per image, in order). Recipe:
1. Open the film's first image in the standard viewer (`/ark:/61903/3:1:<FIRST-ARK>?i=0`; get `<FIRST-ARK>` from the Explore results page above). Wait ~3 s for the viewer to hydrate.
2. Walk the React fiber tree to find that array (it lives in a viewer component's `memoizedProps`/`memoizedState`) and stash it on `window.__imgs`:
   ```js
   (async()=>{ await new Promise(r=>setTimeout(r,3000));
     const all=[]; (function dE(root,d){ if(d>18)return; root.querySelectorAll&&root.querySelectorAll('*').forEach(n=>{ all.push(n); if(n.shadowRoot) dE(n.shadowRoot,d+1); }); })(document,0);
     const seen=new Set();
     const looksImg=it=>{ if(!it||typeof it!=='object')return false; for(const k in it){ let v;try{v=it[k];}catch(e){continue;} if(typeof v==='string'&&(v.includes('3:1:')||v.includes('TH-')))return true; } return false; };
     const find=(o,d)=>{ if(!o||typeof o!=='object'||d>7||seen.has(o))return null; seen.add(o);
       if(Array.isArray(o)) return (o.length>=50&&o.length<5000&&looksImg(o[0]))?o:null;
       for(const k in o){ let v;try{v=o[k];}catch(e){continue;} if(v&&typeof v==='object'){ const r=find(v,d+1); if(r)return r; } } return null; };
     for(const el of all){ const fk=Object.keys(el).find(k=>k.startsWith('__reactFiber')); if(!fk)continue; let f=el[fk],h=0;
       while(f&&h<50){ for(const o of [f.memoizedProps,f.memoizedState]){ seen.clear(); const arr=find(o,0); if(arr){ window.__imgs=arr; return JSON.stringify({len:arr.length, keys:Object.keys(arr[0]).slice(0,10)}); } } f=f.return; h++; } }
     return 'no array'; })();
   ```
3. The array is **0-based and `index`-aligned: image *N* = `window.__imgs[N-1]`** (confirm once: `window.__imgs[0].ark` is the same first ark you opened). Read the target ark(s) directly, e.g. `window.__imgs[515].ark` for image 516. Then run the normal das/v2 → presigned-S3 download on those arks.

This collapses "pull image 516" and "pull register folio 399" to two tool calls. Caveats: the privacy guard on the browser MCP blocks any tool RESULT containing query strings — when reading arks back, return only the bare `3:1:…` ark tokens (no URLs). For a **folio**-targeted pull (register page numbered by folio, not image), the array gives index↔ark but not the folio written on the page; pull one calibration image near your estimate, read its folio number, then interpolate — register imaging is often ~1 image per folio-opening, so image ≈ folio + a small front-matter offset, but confirm rather than assume.

**Other operational notes:**
- **Zero hits ≠ negative until coverage is confirmed.** A film absent from FTS returns zero for *every* query. Before logging a film-scoped negative, probe a common word (`%2Bwife`) scoped to the same DGS; a healthy hit list confirms coverage.
- **One DGS can carry several collections** (e.g. 004389278 = Earsham + Docking + Diss court records). `q.groupName` scopes to the physical film, so triage cards by collection title.
- **Mapping a register series to DGS numbers:** the catalog film-number search `/search/catalog/results?q.filmNumber=<DGS, no leading zeros>` resolves to the parent catalog record; its Film/Digital Notes table (set the rows-per-page `<select>` to 100; "Go to next Page" buttons are clickable) enumerates every volume with film + DGS. Used to map the whole NCC registered-copy-wills year series in one pass (record `koha:278818`). The vol→DGS mapping is offset-ambiguous in the flattened table text; anchor on a confirmed pair (vol. 116–118 / 1621–1623 = DGS 008470484) to fix the offset. The 1624–1637 gap (vols 119–130), resolved 2026-06-14: 1624–25=008470970, 1626=008219670, 1627–28=008076511, 1629=008076512, 1630=008076513, 1631–32=008076514, 1633=008472222, 1634=008076861, 1635=008472223, 1636=008076860, 1637=008076859 (1638–39=008076858; 1643–46=008402405; 1647–51=007904832).

**Ancestry's full-image analog (the das/v2 equivalent for an Ancestry record collection, added 2026-07).** Ancestry's tiled viewer also serves a single full-resolution JPEG at `https://www.ancestry.com/api/media/retrieval/v2/image/namespaces/<dbid>/media/<mediaId>.jpg?securitytoken=<TOK>&imagequality=HighQuality&client=imageviewer-ui`. The `<TOK>` is **per-media** (32-hex) and mintable only by loading that image in the viewer — harvest it from any already-fired tile request: `performance.getEntriesByType('resource')` → filter `…_files/…securitytoken=` → regex `securitytoken=([a-f0-9]+)`. It is **cookie-bound**: works only in-page with `credentials:'include'`; PowerShell/`Invoke-WebRequest` returns 401/404. Returns ~1.3 MB at ~3464×2552. **Renderer-freeze caveat (claude-in-chrome):** the imageviewer tab freezes on any *awaited* fetch chain (`await fetch…await blob`), and Save-to-computer throttles to one-per-page-session; the only semi-reliable pull is fire-and-forget (`fetch(img).then(blob).then(POST to a local receiver)` — no awaits, no `window.__x` writes in the same JS call), and even that landed inconsistently. Clean route next time: a dedicated non-frozen tab, or standard Save-to-computer one leaf at a time. **A bound register's image order does NOT run monotonically by date** (marriage/baptism/burial sections are interleaved) — calibrate leaf-by-leaf from the year-headings, never extrapolate image-by-date. (Ancestry *search*/URL mechanics live in `findmypast-record-search` §6.)

## 4. Paleography staging convention

For crop generation, enhancement sheets, transcription posture, and durable handwriting lessons, also read `.claude/skills/paleography-analysis/SKILL.md`.

For images needing expert transcription: stage under `sources/intake/paleography-staging/` — full-res JPGs in `images/`, one README with a TOC and per-packet briefs (citation + ark links, the machine-transcript snippet as a finding aid, position-targeting hints from §2, and the specific questions to answer). Results come back as `packet-NN-*.md` files in the same directory and are integrated into research companions.

**Disposition when a batch completes** (treat `sources/intake/done/` as a recycle bin — nothing referenced long-term may live only there): packet reports → `sources/corpus_supplement/paleo-<YYYY-MM>-packet-NN-<slug>.md`; master images → `sources/media/<record-set-slug>/_local/` with a committed `README.md` stub per folder (filenames, FamilySearch-terms reason, retrieval arks); diagnostic crops (derivative, regenerable) → `sources/media/_local/<batch-slug>-working-crops/`; the briefs README → a dated folder under `sources/intake/done/`; then fix every repo reference from the staging paths to the durable ones (grep `paleography-staging`). Precedent: the 2026-06 batch (`paleo-2026-06-packet-01..09`).

## 5. Failure modes (check before believing a hit)

Full catalogue with examples in `sources/validations/familysearch-fulltext-search.md`. Headlines: Latin court hand transcribes as word salad (thin hit counts ≠ absence); lookalike names are systematic (*Jernegan*→"Gurney" at Costessey, *Atturney*→"At-Gurney", place-name *Gurnet's Nose*; real distinct surnames Gurnell/Garnsey/Garner ride the wildcards); card year-lists mix document dates with stray numbers; never promote a forename or kinship from a Latin-entry transcript without an image read.

**Image-restricted (index-only) collections — the index hit is real but the image is not pullable on FS.** Confirmed 2026-06 for **"England, Norfolk, Parish Registers (County Record Office), 1510–1997"**: indexed christening/burial records (e.g. the Shimpling Wales entries `VNN6-7MQ`, `VNN6-7S2`, `VNN6-D2B`) resolve to a record page that shows **"Image Unavailable"** — the NRO-contract collection exposes the index only, so the das/v2 path returns nothing and there is no viewer image to walk. Confirm a target is image-bearing (open one record and check for a viewable image) before staging a pull; for index-only Norfolk-CRO parish registers the image route is FindMyPast, Ancestry, or the Norfolk Record Office, not FamilySearch.

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
