---
name: findmypast-record-search
description: Operational recipes for searching FindMyPast's indexed record sets (parish baptisms, banns & marriages, burials) with an authenticated browser session — URL-parameter search, dataset slugs, wildcard/spelling tactics, the spouse-search trick, reading results without opening paywalled images, and known failure modes. Read this before any FindMyPast record-search task to avoid re-deriving the procedures.
---

Proven procedures for working FindMyPast indexed collections via an authenticated Claude-in-Chrome session. Established during the June 2026 Margaret Rybett / Rivett-of-Garveston work (John Gurney G13). Companion full-text recipes for FamilySearch live in `.claude/skills/familysearch-fulltext-research/SKILL.md`; this skill is for FindMyPast's *indexed* (transcribed-field) collections.

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
- `page=<n>` paginates.
- `spouselastname` (marriages set) — see §3.
- ⚠ **`mothersfirstname` does not bind** on the baptisms results URL — a `mothersfirstname=` filter returns the full unfiltered result set (confirmed June 2026). Filter baptisms by reading the **Mother** column, or constrain via father's-first-name / year / place instead.

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

Authenticated Ancestry in the same browser. The most reliable automation path is a **collection-scoped results URL**, not the global search:

```
https://www.ancestry.co.uk/search/collections/<dbid>/?name=<First>_<Last>&birth=<year>_<place>&f-<FACET>=<value>
```

- **Useful collection dbids:** `9841` = England, Select Births and Christenings 1538–1975 (IGI); `9852` = England, Select Marriages 1538–1973 (IGI). These IGI sets cover parishes FMP's Norfolk FHS sets omit (incl. Great Yarmouth).
- **`name=First_Last`** (underscore separates forename/surname; leave forename blank as `_Gurney` for a surname-only search).
- **Marriages:** add the partner with **`spouse=_Anne`**. Father filter in births works via a facet param (e.g. `f-F0005A1A=Edward`) but the param id is collection-specific and brittle — prefer reading the **Relatives** column (it shows father/mother) over trusting the facet.
- **Do NOT set exact flags when you want to see candidates.** Appending `_x=0-0-0` / `_x=...1` (the "Exact" toggles) makes Ancestry return *"zero good matches"* whenever nothing matches exactly — it fails closed. Search **non-exact** and filter the result table yourself by the Baptism/Marriage Place and Year columns.
- The **place in `birth=`/`marriage=` does not hard-filter** — it only re-ranks; non-matching parishes still appear far down the list. Read the Place column to confirm, exactly as with FMP.
- **Reading results:** `get_page_text` on the results tab returns the table cleanly (Name / Date / Place / Relatives / Primary). Right after `navigate`, the first `get_page_text` can return empty — wait ~2s and retry. The URL silently localizes to `.com`; that's fine.

## Continual improvement

This skill is a living interface cheat-sheet. **When new FindMyPast (or adjacent Ancestry record-search) interface behaviour is uncovered — a new working `datasetname`/`sid`, a parameter that does or doesn't bind, a wildcard quirk, a coverage gap, a reliable read technique, or a failure mode — add it here in the same turn and note it plainly in the response.** Keep entries terse and operational; prune anything later found wrong. Confirmed-true mechanics are the bar; speculation stays out.
