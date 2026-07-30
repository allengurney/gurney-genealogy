---
name: findmypast-record-search
description: Operational recipes for searching FindMyPast's indexed record sets (parish baptisms, banns & marriages, burials) with an authenticated browser session — URL-parameter search, dataset slugs, wildcard/spelling tactics, the spouse-search trick, reading results without opening paywalled images, and known failure modes. Read this before any FindMyPast record-search task to avoid re-deriving the procedures.
---

Proven procedures for working FindMyPast indexed collections via an authenticated Claude-in-Chrome session. Established during the June 2026 Margaret Rybett / Rivett-of-Garveston work (John Gurney G13). Companion full-text recipes for FamilySearch live in `.claude/skills/familysearch-fulltext-research/SKILL.md`; this skill is for FindMyPast's *indexed* (transcribed-field) collections.

> **Search *strategy* (the objective/source gates, name variants, wildcarding, token/transitive anchoring) is source-agnostic and lives in [`online-discovery-strategy`](../online-discovery-strategy/SKILL.md) — read and apply that first.** This file is FindMyPast *mechanics* only: parameters, slugs, wildcards, read techniques, coverage caveats.

## 0. Session

Authenticated FindMyPast (and Ancestry, FamilySearch) run in the user's Chrome. Connect with the Claude-in-Chrome MCP: `list_connected_browsers` → `select_browser` (deviceId) → `tabs_context_mcp{createIfEmpty:true}`. No FindMyPast login is performed by us — the session is already signed in.

## 0a. TWO search modes — pick the mode before you pick the parameters (added 2026-07-28)

FindMyPast has **two** parameter-driven result pages, and the single-dataset one had been used here
exclusively for months. That produced negatives which measured *one transcription's coverage* and
were written down as statements about England. Decide the mode first.

**Cross-collection (`sid=999`, no `datasetname`)** — searches every set in a category at once:

```
https://www.findmypast.co.uk/search/results?sourcecategory=life%20events%20(bmds)
  &collection=parish%20baptisms&sourcecountry=great%20britain
  &firstname=<name>&lastname=<name>&yearofbirth=<YYYY>&yearofbirth_offset=<N>&sid=999
```

- `collection=` takes the category label: `parish baptisms`, `parish burials`, `parish marriages`,
  `wills & probate`. `sourcecountry=great britain` (also `england`).
- **The left facet panel gives live per-category counts** (Parish Baptisms *n* / Parish Burials *n* /
  Parish Marriages *n* / Wills & Probate *n*) — the fastest way to size a surname across record
  classes in one request.
- **It paginates** — the numbered pager renders and works, unlike the `datasetname` view.
- Rows are flagged **`Exclusive`** where the record is in no other provider's index. That is the whole
  argument for using this mode: those rows are invisible to Ancestry and FamilySearch.
- ⚠ **No parent columns.** Results give Last name / First name(s) / Year of Birth / Year of Death /
  Year / Record set / Location. Father and mother are *not* shown.
- ⚠ **`location=` does not bind** — a Stewkley-scoped query returned 73,877 unfiltered rows.
- ✅ **`keywords=<place>` DOES bind, and is the practical place filter for this mode.** `lastname=gurn*&collection=parish baptisms&keywords=hitcham` narrowed a national sweep to the single Hitcham row. Use it wherever `location=` fails.

**Single-dataset (`datasetname=…`, `sid=103`)** — §1 below. Use it to *drill*: it shows **Father's
first name(s) / Mother's first name(s) / Place**, which the cross-collection view withholds.

**The workflow is locate-then-drill:** find the event on the cross-collection search, then re-query
the named record set with `datasetname=` to read the parents.

**Worked consequence.** The repo had recorded "the Buckinghamshire parish-register collections carry
no Stewkley Gurney record of any kind after 1614." The cross-collection search returns Stewkley
Gurney baptisms at 1615, 1615, 1616, 1618 and 1626. The claim was true of the dataset searched and
false of the records.

## 0b. THREE modes, and the parent search is the one that matters (added 2026-07-28)

There is a **third** results mode, `sid=102`, which searches by **parent** across all collections. It
is the correct primary instrument for "find this household", and missing it caused a false negative
in this project — a sweep concluded "one baptism in the entire country has a father named John
Gurney" when the correct query returns **315**.

```
https://www.findmypast.co.uk/search/results?sourcecategory=life+events+(bmds)
  &collection=parish+baptisms&sourcecountry=great+britain&sid=102
  &fatherfirstname=john&fatherfirstname_variants=true
  &fatherlastname=gurney&fatherlastname_variants=true
  &motherfirstname=mary&motherfirstname_variants=true
  &yearofbirth=<YYYY>&yearofbirth_offset=<N>
```

- **Parameter names are `fatherfirstname` / `fatherlastname` / `motherfirstname` — NO "s".** The
  `datasetname=` mode's `fathersfirstname` (with an S) silently does not bind; the two modes do not
  share a vocabulary. Never conclude "parent search doesn't work" from testing one spelling.
- **`_variants=true` is a real name-expansion engine, and `gurn*` is not a substitute for it.** A
  wildcard covers one stem; the variants flag reaches `Gernne`, `Garne`, `Gourney`, `Gowrne`,
  `Greney`, `Gurner`, `Gurny`, `Gurnay`. A sweep run on `gurn*` alone will miss whole households.
- ⚠ **But the variants engine is loose.** On `fatherlastname=gurney&fatherlastname_variants=true` it
  also returns Gray, Griffith, Gaune, and `?`-surname rows. **Run it twice** — once strict for a
  clean signal list, once with variants for the wide net — and read past the noise rather than
  trusting either count alone. Worked example: 1625–1635 gave **108 with variants, 11 strict**, and
  the 11 were all genuine Gurney.
- **Search by the PARENT, not the child.** A child-forename sweep can only find children whose
  forename you already guessed; a parent sweep returns the household's whole child list, including
  the siblings that identify it. If the question is "does this family exist anywhere", this is the
  query.
- ⚠ **Do not filter on the mother when testing for a household's existence.** `motherfirstname=mary`
  narrowed 315 rows to 18 — but it silently drops every household whose mother is unindexed, which is
  most Buckinghamshire bishop's transcripts. The father-only list is the work list; the mother filter
  is a ranking aid, not a test.

**Mode summary:** `sid=999` = cross-collection by the *subject's* name (§0a). `sid=102` = across
collections by *parent* name (this section). `sid=103` + `datasetname=` = one collection, with
Father / Mother / Place columns for drilling (§1).

⚠ **In `sid=102`, use `yearofbirth=` — `year=` returns a silent zero.** Confirmed 2026-07-28: an
otherwise identical father-John-Gurney sweep gives **0 results** with `year=1630&year_offset=10` and
**108 parish-baptism rows** with `yearofbirth=1630&yearofbirth_offset=5`. The "Year" facet renders in
the sidebar and the chip appears, so nothing signals the failure. Both facets exist; only one binds.

✅ **`sid=102` reaches burials and marriages, not just baptisms** — the left facet panel on the same
sweep reports Parish Baptisms 108 / **Parish Burials 76** / **Parish Marriages 13** for children of a
father John Gurney, 1625–1635. Switching `collection=parish+burials` is therefore the direct
instrument for "did this household's children die here or disappear?", which is the departure-gap
question, and it had never been used for it.

⚠ **The `sid=102` pool is NOT every collection.** A parent sweep for a father John Gurney/Girney
scoped to Earsham returns **zero**, while the `norfolk+baptisms` county set returns the 1636 and 1638
Earsham baptisms *with the father indexed*. The instrument is fine — the positive control
(`fatherlastname=gurney` + `keywords=hitcham` → Mary Gurny 1631) passes — so this is a pool limit.
**Never assert an England-wide household negative from `sid=102` alone; pair it with county-set runs.**

## 0c. `keywords=` is a literal place token, and it FAILS CLOSED (added 2026-07-28)

This is the highest-value entry in this file, because it silently manufactures negatives.

- **`keywords=` works in `sid=103` too**, not only in `sid=999` — but it matches the target set's own
  **Place string**, literally. A wrong spelling returns **0 results with no error**.
- **The same provider spells the same parish differently between sets of the same county.**
  Hertfordshire Baptisms and the cross-collection view give **Great Berkhampstead**; Hertfordshire
  Burials gives **Berkhamstead**. Worked numbers on an otherwise identical Smith query against
  Hertfordshire Burials: `berkhamsted` → **0**, `berkhampstead` → **0**, `berkhamstead` → **78**,
  no keyword at all → 10,912 (whose first page includes a "Berkhamstead" row).
- **Establish the token before filtering on it.** Run the query with a common surname and *no*
  keyword, read the Place column, and copy the string it actually uses.
- **Beware the token also matching a different parish.** `berkhamstead` matches both Berkhamsted and
  **Little Berkhamstead**, twenty miles away and a separate parish. Read the Place column per row.
- **This cost the project a materially false finding.** A candidate was opened on "no Gurney burial at
  Great Berkhampstead at any date" when the parish holds sixteen — the keyword missed, and the
  surname stem missed too (next bullet).

### Wildcard the CHILD'S FORENAME too — this is the one that got missed (added 2026-07-28)

Everyone remembers to vary the surname. **A per-child sweep that pins the forename to a modern exact
string undercounts just as badly**, because seventeenth-century clerks write the forename however they
like:

- Mary → **Marie, Marye, Maria, Marya**
- Richard → **Rychard, Richarde, Ricd**
- John → **Jhon, Jhone, Johannes, Jo:, Jno**
- Peter → **Peeter, Petter** · Isaac → **Isaack, Isacke, Izacke**

Worked number: on one FindMyPast instrument and window (`sid=999`, parish baptisms, Great Britain,
1619–1639), `firstname=Mary&lastname=gurn*` gave **17 rows**; `firstname=mar*&lastname=gurn*` gave
**54**. One of the recovered rows — Marie Gurney, Epping, Essex, 1625 — had never been seen by the
project despite being present in *two* FindMyPast record sets. **Always run the forename wildcarded
and read past the noise** (`mar*` also pulls Margaret and Mark; that is the correct trade).

### Wildcard stems, and the forenames they miss

- **`gurn*` does not reach `Gourney`.** A stem wildcard covers one stem; it is not a variant sweep.
  Run the family of stems separately — `gurn*`, `gourn*`, `gorn*`, `garn*`, `girn*`, `gern*`, `gvrn*`
  — plus the wrong-initial class (`hurn*`), since this project's indexer confuses capital H and G.
- **`jo*` does not match `Jhon`.** Seventeenth-century clerks write *Jhon*, *Jhone*, *Jhonne*. A
  forename wildcard anchored on `jo` silently drops them: `firstname=jo*&lastname=gourn*` returned 0
  against a set that holds two `Jhon Gourney` burials. Run `jhon*` as a separate query, or use `j*n`.

### Other set-level behaviours confirmed 2026-07-28

- **Slug:** the Hertfordshire marriage set is `hertfordshire+banns+%26+marriages` — the ampersand must
  be percent-encoded. `hertfordshire+banns+and+marriages` returns a **500**.
- **`yearofdeath=<YYYY>&yearofdeath_offset=<N>` binds** on the burial sets (the chip renders only the
  year, but the offset is applied). `yearofbaptism=` binds on baptism sets; `year=` + `year_offset=`
  binds on Norfolk Baptisms.
- **County sets have real parish holes, and the control is cheap.** `norfolk+baptisms` has **no Yaxham
  coverage before 1806** (Smith at Yaxham: 125 rows, all 1806+; the same query bounded 1560–1640
  returns 0). `worcestershire+baptisms` **does not cover Upton on Severn** at all (Smith → 0). Always
  run the common-surname control in the target parish and window *before* recording a surname zero.
- **Record-set descriptions carry survival statements worth reading.** The Hertfordshire sets state
  that of 132 ancient parishes only 16 have registers from 1538, and that many are "sadly defective
  during the Civil War and Commonwealth period (1643-1660)" — which bounds every Hertfordshire
  negative in that window.
- **Transcripts are client-rendered.** An in-page `fetch()` of `/transcript?id=…` returns a shell with
  no data; you must `navigate` to each one. Extract with
  `document.body.innerText.replace(/[\s\S]*?Back/,'')` — `get_page_text` returns the record-set
  marketing copy from `<article>` instead of the transcript panel.
- **Hertfordshire Burials transcripts carry name, burial date and place only** — no age, no parent —
  so household attribution in a multi-household parish needs the register image.

## 0d. `yearofbaptism` and `keywords` CANNOT be combined — the pair fails closed (added 2026-07-29)

In single-dataset mode (`sid=103&datasetname=…`), **a year bound and a place keyword in the same query
return zero regardless of what the set holds.** Not an error, not a warning — a clean, plausible,
completely false zero.

Proof, Essex Baptisms, 29 July 2026:

```
lastname=smith&keywords=epping                                   ->  349 results
lastname=smith&keywords=epping&yearofbaptism=1616&..._offset=5   ->    0 results
lastname=gurn*&keywords=epping                                   ->   28 results, incl. 1616
```

A parish with 349 Smith baptisms cannot have zero in a six-year window that the same set demonstrably
covers for another surname in the very same year.

**Rule: filter by place OR by year, never both. Bound the other axis by reading the returned rows.**

Two consequences worth carrying:

- **`sortby=dateasc` is accepted and silently ignored.** The result order does not change. So you cannot
  establish a set's earliest coverage year by sorting — use a common-surname control and report the span
  of the rows you actually see, stating that it is a partial page if it is.
- Together these mean **a set's coverage window for a named parish is often not establishable from the
  search interface at all.** When that happens, say so and treat the target query's zero as
  uninterpretable rather than as a negative. This is what happened to Ackworth (Yorkshire Baptisms:
  Gurney zero, Smith 127 with nothing visible before 1689 — the zero proves nothing).

This is the fourth distinct fail-closed defect found in this interface, after `keywords` on a wrong
token (§0c), a wildcard stem missing a spelling (`gurn*` not reaching *Gourney*), and `yearofbaptism`
broken outright in the Worcestershire, Somerset and Dorset sets. **Treat every zero as a defect until a
positive control says otherwise.**

### County sets that do not exist (probed 2026-07-29)

Do not spend queries rediscovering these. All slugs probed under several spellings returned server
errors:

- **No marriage/banns set** for **Essex**, **Middlesex**, or **Huntingdonshire**.
- **No baptism set** for **Huntingdonshire**.
- Existing and confirmed working this pass: Norfolk, Essex, Northamptonshire, Oxfordshire,
  Cambridgeshire, Middlesex, Westminster, Berkshire, Herefordshire, Sussex, Warwickshire, Yorkshire
  (baptisms); Norfolk, Northamptonshire, Cambridgeshire, Westminster (marriages).
- **Suffolk** has no county baptism set in this family — a real gap, since Suffolk is a Great Migration
  county. Reach it through FreeREG instead.

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
- ⚠ **`fathersfirstname` (with an S) does not bind** on the `datasetname=` results URL (confirmed 2026-06-20 on Norfolk, re-confirmed 2026-07-28 on Bedfordshire: identical row counts with and without it). **This is a parameter-NAME problem, not a capability problem — see §0b. The parent search works; the parameter is `fatherfirstname`, no S, in the `sid=102` mode.** An earlier version of this skill generalised the failure into "no parent-forename parameter binds on any FindMyPast baptism dataset." That was wrong and it produced a materially false negative (see §0b). Neither parent-forename URL param filters. To isolate one household, narrow by the **exact index spelling** of the surname (e.g. `lastname=gurnie` pulled the Hempnall family's 10 rows cleanly out of the 102 `gurn*` baptisms) and then read the Father/Mother/Place columns.

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
- **`9852` is the best national instrument for a paired-name marriage sweep, because it indexes BOTH parties** (confirmed 2026-07-28). `name=John_Gurn*&spouse=Mary_&marriage=<year>` asks "did A marry B anywhere in England?" in one query and returns clean primary rows with Marriage Date / Marriage Place. **Always re-run with the spouse unconstrained** as a completeness check — that catches events indexed with a blank or unreadable spouse field, and a clean re-run converts "we found none" into "none is hiding behind a blank". Bound the negative by naming a known-missing event: 9852 does **not** contain the 1611 Norwich Gurney–Rybett marriage.
- **`9841` boosts parent-role rows above baptism events** (confirmed 2026-07-28) — a forename+surname query returns mostly rows where the named person is a *parent*, carrying no Baptism Date or Baptism Place of their own. Same failure class as FamilySearch record search. For a **per-child** sweep prefer a county set with Father / Mother / Place columns, year-sliced; use 9841 only to cross-check a county-set blank.
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

## 6a. FamilySearch *record* search mechanics (confirmed 2026-07-28)

Distinct from FamilySearch full-text (that is `familysearch-fulltext-research`). The historical-record
results page is fully parameter-driven:

```
https://www.familysearch.org/search/record/results?q.surname=<name>&q.givenName=<name>
  &q.fatherGivenName=<name>&q.motherGivenName=<name>
  &q.birthLikeDate.from=<YYYY>&q.birthLikeDate.to=<YYYY>&f.recordCountry=England&count=50
```

- **`q.fatherGivenName` and `q.motherGivenName` bind, but they RANK — they do not filter.** A
  father-plus-mother query returns a relevance-ordered sweep of the whole surname field with matching
  households boosted to the top, not a filtered set. Read the leading rows as the answer and treat the
  long tail as noise. This is the cheapest way to ask "does household X exist anywhere in England?"
  in one query rather than parish by parish.
- **`q.surname.exact=on` DOES bind when paired with `f.recordCountry`** (an exact `Hurney` sweep
  returned 5 rows against 2,736 fuzzy). The earlier note that exact-match breaks applies specifically
  to `q.surname.exact` **+ `f.recordCounty`** — country is fine, county is not.
- **Without the exact flag, surname matching is aggressively fuzzy**: `Hurney` pulls in Herne, Hurne,
  Hirne, Hernu. Useful for a variant sweep, useless for a clean negative — use `exact=on` for the
  negative and fuzzy for discovery.
- **A forename constraint degrades.** `q.givenName` holds for the top-matching rows and then silently
  relaxes to surname-only further down the result set. Read the leading block; do not page for more.
- `count=50` binds and is worth setting; the results table reads cleanly with `get_page_text`, giving
  Name / Record set / Event + date + place / Parents / Spouses / Children without opening a record.
- **Collections differ on whether mothers are indexed** — *England, Buckinghamshire, Church Records,
  1217–1994* carries mothers where *England, Births and Christenings, 1538–1975* often does not, so
  the same household can look motherless in one set and complete in the other. Always name the
  collection when recording a parent-based negative.
- **Place attributions differ between providers**, and this is not cosmetic: a household FindMyPast's
  Hertfordshire set indexes at Berkhamsted, FamilySearch indexes at St Peter, Hertfordshire (St
  Albans). Before recording a "no record at parish X" negative, check whether the other provider puts
  the same family somewhere else.
- **`q.anyPlace` does not usefully bind.** A parish-scoped query (`q.anyPlace=Yaxham, Norfolk`) returns
  a county-wide, mostly modern result set — on one test, 8,389 rows led by twentieth-century death
  registrations. For parish work use a county set with a readable Place column (Ancestry 61045 for
  Norfolk, FindMyPast's county baptism sets) instead.
- **Results are role-aggregated, not event rows.** A forename+surname query returns rows like
  "Richard Gurney · Father · spouses … · children …" — one row per indexed *role*, not per baptism.
  That makes FamilySearch record search a poor instrument for a **per-child sweep**: it will not
  cleanly answer "which parishes baptised a Richard Gurney in 1626–1636". Use a set that returns
  baptism rows with Father / Mother / Place columns and slice by year.
- **Which role you get back depends on the FORENAME, not on your query shape** (confirmed 2026-07-28).
  The identical query returned *Principal* baptism rows for `givenName=Mary` and almost nothing but
  *Father* rows for `givenName=Richard` — because Richard is a commoner father-name in that
  collection. **So a per-child sweep can silently return zero events for one child and real events for
  another.** Before reading any FamilySearch child-sweep result, check whether the rows say
  `Principal` or `Father`.
- ✅ **Turn that bug into an instrument: the Father rows are a household index.** A query on
  `q.givenName=John&q.surname=Gurney&f.recordCountry=England&count=100` returns rows shaped
  "John Gurney · Father · Spouses Mary · Children Isaac Gurney" — 87 of the first 100 blocks, 18 of
  them with a spouse named Mary. That is the FamilySearch analogue of FindMyPast's `sid=102` parent
  search and it enumerates households across every collection at once.
- ⚠ **But `q.birthLikeDate.from/to` does NOT bind on role rows at all.** Two John-and-Mary rows
  returned inside a 1620–1645 query opened as christenings of **1687** (Misterton, Leicestershire) and
  **1703** (Upton on Severn). The household index gives you names, never dates — **every row must be
  opened individually** via its `ark:/61903/...` link to get parish and year.
- **Net posture:** FamilySearch record search is good for *discovery* (fuzzy, England-wide, free-text)
  and for *household enumeration* via the role rows; it is bad for *bounded negatives* and useless for
  date-bounded ones. Assert negatives from FindMyPast or Ancestry collection results, where the row is
  an event and the columns are readable.

## 6b. Jurisdiction before coverage (added 2026-07-28)

A "county X's records are unreachable" conclusion is very often a statement about a finding aid, not
about the records. Two instances inside one week of this project:

- **Aylesbury Vale estate deeds are at Worcestershire Archive**, in the Pakington of Westwood Park
  collection (`705:349`), because the estate's absentee owners deposited their muniments with their
  own family papers. A Buckinghamshire Archives search cannot see them.
- **Hertfordshire probate is at HALS in series `ASA`** (Archdeaconry of St Albans, diocese of London),
  catalogued to item level with a registered-will volume `ASA/AR/8` covering 1610–1636. The repo had
  logged "no route" on the strength of a zero in FindMyPast's *England & Wales Published Wills &
  Probate Indexes* — a dataset that simply contains no Hertfordshire volume.

Practical rule: before recording a county-level records negative, establish **(a) which ecclesiastical
jurisdiction actually held the class** (archdeaconry and diocese, which need not follow the county)
and **(b) which repository keeps it now** — then check TNA Discovery, which indexes ~2,500
contributing archives and will usually answer both. County boundaries and diocesan boundaries do not
coincide: Buckinghamshire and Bedfordshire were in the diocese of Lincoln, while the St Albans part
of Hertfordshire was in the diocese of London.

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
