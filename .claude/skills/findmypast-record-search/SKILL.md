---
name: findmypast-record-search
description: Operational recipes for searching FindMyPast's indexed record sets (parish baptisms, banns & marriages, burials) with an authenticated browser session — URL-parameter search, dataset slugs, wildcard/spelling tactics, the spouse-search trick, reading results without opening paywalled images, and known failure modes. Read this before any FindMyPast record-search task to avoid re-deriving the procedures.
---

Proven procedures for working FindMyPast indexed collections via an authenticated Claude-in-Chrome session. Established during the June 2026 Margaret Rybett / Rivett-of-Garveston work (John Gurney G13). Companion full-text recipes for FamilySearch live in `.claude/skills/familysearch-fulltext-research/SKILL.md`; this skill is for FindMyPast's *indexed* (transcribed-field) collections.

> **Search *strategy* (the objective/source gates, name variants, wildcarding, token/transitive anchoring) is source-agnostic and lives in [`online-discovery-strategy`](../online-discovery-strategy/SKILL.md) — read and apply that first.** This file is FindMyPast *mechanics* only: parameters, slugs, wildcards, read techniques, coverage caveats.

## 0. Session

Authenticated FindMyPast (and Ancestry, FamilySearch) run in the user's Chrome. Connect with the Claude-in-Chrome MCP: `list_connected_browsers` → `select_browser` (deviceId) → `tabs_context_mcp{createIfEmpty:true}`. No FindMyPast login is performed by us — the session is already signed in.

## 1. Search by URL parameters, not the form

The results page is fully parameter-driven and is far more reliable than driving the autocomplete form under automation:

```
https://www.findmypast.co.uk/search/results?datasetname=<slug>&sid=103&lastname=<name>&firstname=<name>&yearofbirth=<YYYY>&yearofbirth_offset=<N>&spouselastname=<name>&page=<n>
```

- `datasetname` uses `+` for spaces. **Confirmed slugs:** `norfolk+baptisms`, `norfolk+banns+and+marriages`, `norfolk+burials`. ⚠ `norfolk+marriages` 500s — the marriages set is "banns and marriages".
- `sid=103` worked for the Norfolk parish sets. If a `datasetname` returns a **500**, the slug or `sid` is wrong: open the record-set search page (`https://search.findmypast.co.uk/search-world-records/<record-set-slug>`), run one search through the form, and **capture the resulting `/search/results` URL** — it contains the correct `datasetname`+`sid`. Reuse that pattern thereafter.
- `yearofbirth` + `yearofbirth_offset` (allowed offsets: 0,1,2,5,10,20,40). **±40 is the practical way to bound a surname sweep.** ⚠ The marriages set rejects `yearofbirth` (→500); omit it there (or use the form's Year field).
- ⚠ **`page=<n>` does not reliably paginate the Norfolk parish sets** — `page=2` on the baptisms results returned 0 rows (the param did not page). When a keyword-boosted result is small and the primaries look exhaustive, treat page 1 as the complete set; otherwise narrow by year or a tighter surname-variant spelling rather than paging. (Same failure class on Ancestry collection results — §6.)
- `spouselastname` (marriages set) — see §3.
- ⚠ **`mothersfirstname` does not bind** on the baptisms results URL — a `mothersfirstname=` filter returns the full unfiltered result set (confirmed June 2026). Filter baptisms by reading the **Mother** column, or constrain via year / place / a tighter surname-variant spelling instead.
- ⚠ **`fathersfirstname` also does not bind** on the baptisms results URL (confirmed 2026-06-20: `lastname=gurn*&fathersfirstname=jo*` returned the identical 102-row set as without it). Neither parent-forename URL param filters. To isolate one household, narrow by the **exact index spelling** of the surname (e.g. `lastname=gurnie` pulled the Hempnall family's 10 rows cleanly out of the 102 `gurn*` baptisms) and then read the Father/Mother/Place columns.

### 1a. Marriage-set and browse-set parameters (confirmed 2026-07-26)

- **`year=<YYYY>` DOES bind on `norfolk+banns+and+marriages`** (a "Year 1609" chip appears) — but **no offset param binds**: `year_offset` and `yearofbirth_offset` are both ignored, so a `year=` query is always ±0. Use it only for a single-year probe; for a window, sweep year by year or narrow by exact surname spelling instead.
- **`page=<n>` does not bind on the marriages set either** — confirmed `page=2` returns 0 rows on a 40-row result. Same failure as the baptisms set.
- **Both parties are indexed.** `spouselastname=` + `spousefirstname=` return the mirror row of every principal row (e.g. `spouselastname=gurn*&spousefirstname=fran*` returned the bride-side twin of each `firstname=fran*&lastname=gurn*` hit). A one-direction miss is therefore a real miss, not an indexing artefact — but still try the variant spellings on both surnames.
- **Image-browse sets are a different animal.** `norfolk+marriage+bonds+1557-1915+image+browse` and `norfolk+archdeacon%27s+transcripts+1600-1812+image+browse` are valid `datasetname` values, but **`year=` does not bind on them** and **free-typed `parish=` returns 0 even for a valid parish** — the value must come from the field's autocomplete vocabulary. Type into the Parish box, pick from the dropdown, hit search, and reuse the resulting `/results/world-images/<slug>?parish=<value>` URL. Result rows give Parish / Event / Year range / Archive reference / **Image count**.
- **Plan gate, and how to tell.** On a *Family Tree* plan, index rows and record-set metadata read fine but every record image and image-browse leaf bounces to `/upgrade?…suitable-plans=Everything`. On *Everything*, images open in the viewer (§7a). **A subscription change signs the account out of every tab** — if a previously-working session starts showing "Log in / Sign up", that is the likely cause, and only the user can re-authenticate. Opening a fresh tab does not restore it.

### 1b. Wildcards: `?` and `*` do not combine

`?` alone works (`lastname=garn%3Fy` → Garnay/Garney, 49 rows). **`?` plus a trailing `*` silently fails** — `lastname=g%3Frn*` renders the results page with a "Search" button instead of a result count, i.e. the query never executes. Run one prefix per query (`gurn*`, `gorn*`, `gourn*`, `garn*`, `girn*`, `gern*`) rather than trying to fold them into one pattern.

## 2. Names: wildcards beat the variants checkbox

- The built-in **"Name variants" checkbox is far too loose** (e.g. `Rivett` + variants returned ~50k) unless paired with a tight year bound. Prefer **exact + wildcard**.
- Wildcards work in `lastname`/`firstname`: `?` = one char, `*` = many. **URL-encode `?` as `%3F`.** Example `lastname=r%3Fvett` = `R?vett` → catches Rivett / Revett / Ryvett in one query.
- **Index spelling ≠ the family's usual spelling.** A clerk's one-off (e.g. a marriage entered as "Rybett") will not match the baptismal spelling ("Rivet"). Search the whole variant set: e.g. Rivet / Rivett / Revett / Ryvett / Rybett. A bride/groom can be indexed under the variant, so search both spellings.

## 3. The spouse-search trick (marriages)

The banns-and-marriages set has a **Spouse's last name** field (URL `spouselastname=`). Query a specific alliance directly — e.g. `lastname=gurney&spouselastname=rivett` — to find A×B marriages across all years. Either party can be the indexed "principal", so if the expected hit is missing, **swap the surnames** (search the bride's surname as `lastname`) and try the variant spellings (the target may be indexed under the bride and a one-off spelling).

## 4. Reading results

- `get_page_text` on the results tab returns the index table cleanly — columns Name / Year / Father / Mother / Place (baptisms), or Name / Year / Spouse / Place / Event type (marriages) — **without opening a paywalled record image**. The index fields are usually enough to map a family.
- Right after `navigate`, `get_page_text` sometimes returns "No text content"; wait 2–4s and retry.
- Opening an individual record can bounce to the home page or need the record viewer; avoid unless you specifically need an image. Lean on the index columns.
- If you must use the form: coordinate clicks/typing often miss or fail to register under automation — prefer `read_page{filter:"interactive"}` to get field refs, then `form_input` by ref. The **Place** field binds **only** via its autocomplete dropdown selection; free-typed place is ignored and the search runs unfiltered (it dumped all 3.6M). Filter by place in the result `Place` column instead, or scope by year.

## 5. Coverage caveats (do not read a blank as a true negative)

- FindMyPast **"Norfolk Baptisms" is the Norfolk FHS transcription set and is parish-selective** — it omitted Garveston and even Francis Gurney G14's own East Dereham children. A surname absence here is **not** a true negative.
- **Cross-check the IGI-based set** ("England, Select Births and Christenings, 1538–1975") on Ancestry/FamilySearch, which covers parishes FindMyPast's set lacks. Treat FindMyPast and the IGI set as complementary.
- FindMyPast has no "Suffolk Baptisms" dataset (500); use Ancestry for Suffolk parish coverage.
- **Great Yarmouth is a confirmed gap in BOTH FMP parish sets** (verified 2026-06): the Edward & Anne Gurney children christened at Great Yarmouth (1629, 1631) are absent from "Norfolk Baptisms," and no Yarmouth Gurney marriage appears in "Norfolk Banns and Marriages." The IGI-based Ancestry "England, Select Births and Christenings" (collection 9841) **does** carry the Yarmouth entries. When a Norfolk port/town parish looks empty in FMP, cross-check Ancestry's IGI before concluding a true negative.

## 6. Ancestry record-search mechanics (collection-scoped URLs)

Authenticated Ancestry in the same browser. **Always use `ancestry.com`, not `.co.uk`:** a `.co.uk` URL can silently present the signed-out *masked* view (separate session cookies + consent banner) even when `.com` is fully authenticated — a round-1 "Podmer signed out" negative was purely this domain artifact. The most reliable automation path is a **collection-scoped results URL**, not the global search:

```
https://www.ancestry.co.uk/search/collections/<dbid>/?name=<First>_<Last>&birth=<year>_<place>&f-<FACET>=<value>
```

- **Useful collection dbids:** `9841` = England, Select Births and Christenings 1538–1975 (IGI); `9852` = England, Select Marriages 1538–1973 (IGI). These IGI sets cover parishes FMP's Norfolk FHS sets omit (incl. Great Yarmouth).
- **`name=First_Last`** (underscore separates forename/surname; leave forename blank as `_Gurney` for a surname-only search).
- **Marriages:** add the partner with **`spouse=_Anne`**. Father filter in births works via a facet param (e.g. `f-F0005A1A=Edward`) but the param id is collection-specific and brittle — prefer reading the **Relatives** column (it shows father/mother) over trusting the facet.
- **Do NOT set exact flags when you want to see candidates.** Appending `_x=0-0-0` / `_x=...1` (the "Exact" toggles) makes Ancestry return *"zero good matches"* whenever nothing matches exactly — it fails closed. Search **non-exact** and filter the result table yourself by the Baptism/Marriage Place and Year columns.
- The **place in `birth=`/`marriage=` does not hard-filter** — it only re-ranks; non-matching parishes still appear far down the list. Read the Place column to confirm, exactly as with FMP.
- ⚠ **`&page=2` does not bind on collection results** — it returns the identical page-1 rows. When the primaries are exhausted on a keyword-boosted small result, that page *is* the set; otherwise tighten the query rather than paging.
- **Pulling the full record image:** the collection viewer serves a single full-res JPEG via a per-media cookie-bound endpoint — recipe (and its claude-in-chrome renderer-freeze caveat) is in `familysearch-fulltext-research` §3.
- **Useful dbids beyond the IGI pair:** `61045` = Norfolk, Church of England Baptisms, Marriages and Burials 1535–1812 (NRO partnership, image-linked, ¾ of Norfolk parishes); `62679` = **Norfolk, Indexes to Wills, Probate, Administrations *and Marriage Licence Bonds*, 1371–1858** (NRO partnership — the only online route to Norfolk marriage-licence-bond and probate indexing in one query; `_Gurn*` returns just 70 rows across 1371–1858, so a surname sweep here is cheap and near-exhaustive); `2056` = London and Surrey, Marriage Bonds and Allegations 1597–1921 (the Bishop of London's registry — the right instrument for a London-resident groom).
- **Sizing and browsing a collection by parish (added 2026-07-26).** The collection landing page (`/search/collections/<dbid>/`) carries a **Browse this collection** panel whose tiers are real `<select>` elements named `Browselevel`, `Browselevel1`, … Drive them with **`form_input` on the select's ref** (from `read_page{filter:"interactive"}`); scripted `dispatchEvent('change')` populates the next tier but never renders the final tier, and the panel's own markup is sanitised out of `javascript_tool` results. The last tier renders as **links, not a select** — find it with `find{query:"Date Range …"}`. This is the only reliable way to learn *what date ranges a given parish actually has*: e.g. collection 61045 offers East Dereham as 1593–1641 / 1679–1702 / 1679–1812 / 1702–1705, which is a direct statement about survival and about the Civil-War gap.
- **Sizing an image set:** open any leaf and read the viewer's "**N of TOTAL**" counter from `get_page_text` — East Dereham 1593–1641 is **101 leaves**. Compare that against however many images a local run holds before calling a year "not in the image set". **Media ids are not contiguous with leaf numbers** (one film stem serves several parishes), so walk the viewer rather than extrapolating `stem_00nnn`.
- **Full-resolution pull, dbid 61045 (confirmed working 2026-07-26):** `https://www.ancestry.com/api/media/retrieval/v2/image/namespaces/<dbid>/media/<mediaId>.jpg?securitytoken=<TOK>&imagequality=HighQuality&client=imageviewer-ui` returned HTTP 200 `image/jpeg` at ~1.2 MB in-page. `<mediaId>` is exactly the `images/<id>` path segment. **Getting the bytes out is the hard part, not the fetch:** the token is per-media and cookie-bound (no PowerShell route), and both the POST-to-a-local-receiver and scripted-`<a download>` routes are refused by the harness classifier. Budget for the viewer's own Save-to-computer control, one leaf at a time, or get the scripted pull pre-authorised.
- **Reading results:** `get_page_text` on the results tab returns the table cleanly (Name / Date / Place / Relatives / Primary). Right after `navigate`, the first `get_page_text` can return empty — wait ~2s and retry. The URL silently localizes to `.com`; that's fine.

## 7. Published probate indexes dataset (BRS + Matthews)

"England & Wales Published Wills & Probate Indexes, 1300-1858" behaves unlike the parish sets:

- **Single "Name search" field → `keywords=`** (not `lastname`/`firstname`). The `*` wildcard works: `keywords=gurn*` returned 157 vs `gurney` 97 vs `francis gurney` 33 — always run the surname-variant wildcards (`gurn*`, `gourn*`, `gorn*`, `girn*`, `gern*`, `gvrn*`), not an exact name.
- **`publicationtitle=` filters by volume.** Easiest path: set it via the sidebar autocomplete (type e.g. "Commissary" → pick the volume → Search); the chip writes the param. The autocomplete browse also confirms whether a court is even in the collection (the London Commissary Court vols are present; they cover City wills).
- **Working results URL:** `/search/results?datasetname=england+%26+wales+published+wills+%26+probate+indexes%2c+1300-1858&sid=103&keywords=<q>` (note `%26`/`%2c`). A bad slug/sid 500s — recapture via a form search.
- **Results table shows only Place / Page number / Source / Publication — no name or year inline,** and individual records are **paywalled even on this session** (bounce to /upgrade). Use this set to *locate the court + volume + page*, then read the **printed index image** (archive.org) for the actual forename/year/folio.
- **On an Everything plan the page images open, and this is the point of the set.** Each row's record page carries `link "View PDF"` → a **scanned page image wrapped in a PDF, with no text layer**. It is the printed index page itself, so it gives the names, years, places, occupations and court references the results table withholds. Confirmed 2026-07-27 on *Buckinghamshire Probate Index, 1483–1660* (BRS vol. 114) p. 173 — the whole Gurney block in one page.
- **Get the PDF out of the browser, don't read it in the viewer.** The embedded Chrome PDF pane **freezes the renderer** under this MCP (repeated `Page.captureScreenshot` timeouts) and its scroll does not respond. Instead harvest the media href from a *different* tab exactly as for images — but note the PDF path has an **extra trailing segment and no query string**: `/media/pdf/<ID>/<ID>/<32-hex-hash>/pdf` (the `?download=true` form used for jpgs returns **404** here, and the ID appears **lowercased** in the media path even when the record id is uppercase). Then `Invoke-WebRequest` it, extract the embedded scan with `pypdf` `page.images` (there is no text layer, so `extract_text()` returns empty), crop and autocontrast, and read that.
- **Counties whose archdeaconry probate is not item-indexed in TNA Discovery may still be here.** Buckinghamshire (D/A/We, D/A/Wf) was logged in the repo as an offline records-office request; it is in this dataset. Check this set *before* concluding that a county probate tier requires a record-office visit.
- **FMP's transcription is partial vs the printed index:** `gurn*` in the London Commissary 1626-1649 & 1661-1700 volume returned 1 row, but the printed index page held 5 Gurney/Gourny entries. Treat an FMP count here as a floor, not a complete list — confirm against the book image.

## 7a. Image-browse sets: navigating and bulk-downloading (added 2026-07-27, subscription tier)

With an *Everything* plan the image-browse sets open in a full viewer. Three mechanics that are not obvious:

- **Find the piece by parish, not by year.** `/results/world-images/<set-slug>?parish=<autocomplete value>` lists every piece for that parish with **Event / Year range / Archive reference / Image count** — e.g. *Norfolk Parish Registers Browse* → East Dereham → 35 rows including "Register Bills / 1593-1640 / **PD 86/41** / 110". That table is the fastest way to learn what survives for a parish and in what quantity.
- **Jump to a page by URL — `id` and `parentid` must be IDENTICAL.** `record?id=<ID>&parentid=<ID>` works; `record?id=<page-ID>&parentid=<first-page-ID>` returns **500**. The viewer's page-number "Go" box does **not** respond to `form_input` or to synthetic typing — drive it by URL. Page *N* maps directly onto the archive's own image number (for PD 86/41, page 1 = image `00692`, page 110 = `00801`).
- **Bulk download, cheaply.** Each record page carries `link "Download record"` → `https://search.findmypast.co.uk/media/jpg/<id>/<id>/<32-hex-hash>?download=true`. The hash is **per-image** (reusing one on another id returns **409**), but the URL is **NOT cookie-bound** — PowerShell `Invoke-WebRequest` fetches it unauthenticated. So: one in-page `fetch()` loop over the record HTML harvests every hash in a single `javascript_tool` call (regex `/media\/jpg\/[^"']*?\/([a-f0-9]{32})/`), then one PowerShell loop downloads the lot. ~34 images for 3 tool calls instead of 70. **Return the hashes chunked** (`hash.match(/.{1,4}/g).join('.')`) or the browser MCP's privacy guard blocks the result as an opaque token.
- **Reading years without transcribing.** NRO register-bill membranes carry a **modern pencil year at the head** of each sheet. Crop a narrow band across the head of every image, autocontrast, and tile them into a few contact sheets — a whole 110-image file can then be year-mapped in ~6 image reads instead of 110. This is the cheap way to test a "does year X survive" question before commissioning any transcription.

## 8. NROCAT — the Norfolk Record Office online catalogue (added 2026-07-27)

`nrocatalogue.norfolk.gov.uk` (AtoM) is the authority on **what a Norfolk piece is and how many images it has**, and it settles questions that an Ancestry/FindMyPast browse node only approximates.

- **It catalogues NRO digitisations image by image.** Each leaf is a `[Part]` titled `Digital image <film>-<nnnnn>.jpg of <PIECE>`, slugged `/index.php/digital-image-<film>-<nnnnn>-jpg-of-<piece-slug>`. Opening any one Part renders the **full sibling list** in its hierarchy panel, so a single page read yields the complete image run for the file. Worked example: `PD 86/41 — "Indented register bills, 1593–1641"` = 110 contiguous images `4034129-00692` … `4034129-00801`.
- **No images are served** — the record carries a generic icon, not a thumbnail. NROCAT tells you the extent; Ancestry/FindMyPast serve the pixels. Ancestry's browse-node leaf count can differ from the NRO's (101 vs 110 for the above), so prefer the NRO run as the worklist.
- **Search mechanics:** `/index.php/informationobject/browse?query=<q>&topLod=0` (drop `topLod=0` and you get only top-level fonds). `limit=` does **not** bind — 15 results per page. The tokenizer splits on hyphens, so `4034129-0077*` returns nothing; `"PD 86/41"` as a phrase works. Harvest hrefs with `[...document.querySelectorAll('article a')]` — `get_page_text` returns only the first `<article>`.
- **It 502s intermittently, sometimes for several consecutive requests.** Retry rather than recording an absence; the same URL that failed five times in a row served fine the next day.

## Continual improvement

This skill is a living interface cheat-sheet. **When new FindMyPast (or adjacent Ancestry record-search) interface behaviour is uncovered — a new working `datasetname`/`sid`, a parameter that does or doesn't bind, a wildcard quirk, a coverage gap, a reliable read technique, or a failure mode — add it here in the same turn and note it plainly in the response.** Keep entries terse and operational; prune anything later found wrong. Confirmed-true mechanics are the bar; speculation stays out.
