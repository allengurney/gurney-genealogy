# Extended FTS discovery campaign — creative search strategies (2026-06-13)

Per Allen's steer: test creative full-text strategies for the 1300–1650 window — Gurney
**place names** (era spellings), **associated families**, **Latin forms**, heavier
**wildcarding** — to beat the corrupt manuscript transcripts. Bottom line up front: **the
typed will-extracts sweep was the productive vein; co-occurrence probes do not surface new
pre-1660 Norfolk manuscript records for this corpus.** Documented here so the negative is
not re-run from scratch.

## Method gain — the FTS JSON API (reusable)

The results UI calls a clean JSON endpoint:
`https://www.familysearch.org/service/search/fulltext/search?count=N&m.defaultFacets=on&m.queryRequireDefault=on&offset=0&q.text=<encoded>`
fetched with `credentials:'include'`. Response: `results` = total hit count; `entries[]`
each with `id` (ark), `collectionTitle`, and `content.{recordDate, recordType, recordPlace,
title, textDocument (full transcript), highlightTexts (snippets)}`. **One `javascript_tool`
call can batch dozens of probes** (fetch loop, ~400 ms apart) and parse structured results —
far faster than navigating the shadow-DOM UI per query. Added to the FTS skill.

## Probe matrix run (unscoped full-text, count=50)

| Probe | Total hits | Useful? |
|---|---|---|
| `+Gurn* +"West Barsham"` | 18 | All printed "Biographies" books + cross-collection noise (Italy, Oklahoma) |
| `+Gourn* +"West Barsham"` | 16 | Same — printed pedigrees |
| `+Gurn* +"Great Ellingham"` | 143 | Noise-dominated |
| `+Gourn* +"Great Ellingham"` | 9 | Printed + noise |
| `+Gurn* +Harpley` | 181 | Noise |
| `+Gurn* +Saxthorpe` | 55 | Noise |
| `+Gurn* +Hardingham` | 650 | Noise |
| `+Gurn* +Hingham` | 4022 | Hingham too common — unusable |
| `+Gurn* +Lovell` | 4563 | Lovell too common — unusable |
| `+Gurn* +Calthrop*` | 68 | One "Norfolk, Properties" hit + a 1633 "Legal" label (= the printed 1633 Visitation, known L-24) |
| `+Gurn* +Wauncy` | 3 | All noise (Oklahoma deed, Italy births) despite Wauncy being rare |
| `"de Gournay"` | 4907 | Dominated by printed de-Gournay pedigree books |
| `"de Gurnay"` | 77 | Mostly Liège/Belgium "de Gurnay" (a Walloon name) — false positives |

**Aggregate manuscript filter** (recordType ∈ Legal/Properties/Land/Court/Probate/Deed/
Manor/Fine, pre-1660, across every probe above): **3 hits — all Liège/Belgium "de Gurnay"
court records, none Norfolk.** Zero new pre-1660 Norfolk manuscript records.

## Why co-occurrence fails here (the durable lesson)

1. **Place + surname can't co-occur in corrupt transcripts.** A manuscript Norfolk court roll
   or fine naming a Gurnay of West Barsham transcribes the *place* and the *surname* as Latin/
   secretary-hand salad, so a `+Gurn* +"West Barsham"` AND never fires on the manuscript — only
   on clean **printed** books that happen to mention both.
2. **The clean hits are already-known printed pedigrees** — Burke's *Landed Gentry* (L-71),
   the Norfolk Visitations (L-24, L-64), Blomefield, county histories — surfacing under the
   FamilySearch "Biographies/Heraldry/Genealogy" digitized-book collections.
3. **Wildcards drag cross-collection false positives** — `Gurn*` → *Garner/Gurnell*; `"de
   Gurnay"` → the Liège Walloon family; common second terms (*Hingham*, *Lovell*) return
   thousands. Tightening the surname (`Gurnay`/`Gournay` exact) trades recall for precision but
   still lands in printed books.

**Corollary:** the **typed-abstract collections are the high-yield FTS vector** because their
OCR is clean. The Bradfer-Lawrence "Norfolk wills extracts 1370–1763" (6 reels) was exactly
that, and is now fully mined. The remaining productive moves are **targeted manuscript pulls**
(not FTS discovery) and **finding other typed-abstract/index typescripts**.

## Round 2 — fuzzy / dictionary-snapping calibration (refines the above)

The "co-occurrence fails" conclusion is about **unscoped** AND-probes biased to printed
text. A second principle, from Allen: *the more structured the query, the more it favours
clean printed OCR over variably-transcribed handwriting* — so to reach manuscripts, go
**fuzzier and scope to a film.** Tested on **DGS 004397070** (Norfolk/Norwich Court Records
1630–36):

- **Fuzzy `~N` is supported but only usable scoped.** Unscoped `Gurney~2` = **472 million**
  hits (matches the corpus); `Gurney` plain = 419k. Scope to a film and it becomes usable:
  on 004397070, `Gurn* Gourn* Gorn*` = 64, `Gurney~1` = 92, `G?rn*` = 99, `Gu?n*` = 21.
- **But looser ≠ better recall here.** The `Gurney~1` extras were mostly literal "Gurney"
  again (past the result cap); the `G?rn*` extras were **Garner/Garnett/Gernon/Garnesly** —
  *genuine* East-Anglian surnames, not Gurney variants.

**The dictionary-snapping principle (the key calibration).** These collections' OCR was
**name-dictionary-aided**, so a poorly-read handwritten surname is snapped to the nearest
*dictionary* surname. A single Norwich name on this one film transcribes as a spray:

| Snap target | Count | Established Norfolk surname? | Verdict |
|---|---|---|---|
| Gurney / Gorney / Gorne / Gorner / Gurnee | 39/12/12/9/7 | no (Gorn- forms aren't a family) | **Gurney — recover via `Gorn*`** |
| Gornesly, Gornet, Gornes, Gorness, Gorneses, Gornery, Gornerlynett | 2–3 each | no | **Gurney garbles — recovered by `Gorn*`** |
| Garner, Garnett, Garnsey, Garnsby, Gernon | 1–6 | **yes** (real families) | **genuine — EXCLUDE; `Garn*` would swamp** |
| Guinea, Gunnery, Gunnel, Gunner | 1 each | n/a (Gunn / words) | unrelated |

So the calibration rule: **build the term set from snap-targets that are NOT an established
surname in that geography** (here `Gorn*` is safe because no "Gorney" family exists in
Norfolk), and **exclude snap-targets that have their own local population** (`Garn*` →
Garner). This is **geography-specific** — in a county with a real Gorney/Garnsey family the
same wildcard would be unsafe. It also explains *why* the long-standing `Gurn*/Gourn*/Gorn*`
set is well-tuned for Norfolk: it harvests the Gurney dictionary-snaps without dragging a
genuine Garner population.

**Actionable upside — scoped sweeps massively out-recall manual browsing.** The manual
browser-tab pass flagged ~1–2 pages per manuscript film; the scoped `Gurn*/Gourn*/Gorn*`
sweep finds far more (these are raw hit counts — real Gurney/Gorn-snaps, minus Garn*, but
may count one person across many pages and include some salad; an upper bound):

| Manuscript film (DGS) | Collection | Raw Gurn*/Gourn*/Gorn* hits |
|---|---|---|
| 004397070 | Norfolk/Norwich Court 1630–36 | 64 |
| 004397533 | Norfolk/Norwich Court 1619–30 | 50 |
| 004389252 | Norwich Depositions 1608 | 31 |
| 004389182 | Norwich Deeds | 30 |
| 004389191 | Costessey Manorial 1633–35 | 26 (⚠ Jernegan false-positive zone — skill §5) |
| 004397113 | Norwich Court 1636–46 | 13 |
| 004389254 | Norwich Depositions 1639 | 7 |

The early-17th-c. **Norwich civic/court/deposition** records carry a substantial Gurney
presence (relevant to John Gurney G13's Norwich context and the Norwich Gurneys generally)
— but the transcripts are salad, so these are **image-read / paleography targets**, not
promotable from the transcript. Triage by reading, dedup persons across pages, and screen
for the Garner/Jernegan look-alikes before promoting. Good candidates to **fold into the
paleography outsource alongside Bundle 01** once specific high-value pages are picked.

## Round 3 — re-reading the sweep hits *by transcript context* (not binary match)

Per Allen: don't treat the match string as a binary hit — read each hit's **full transcript
(`content.textDocument`)** for buried place names, forenames, or associated families that
signal relevance even amid garble. Implemented as a context-scan over the manuscript-film
hits (mine the whole page text for `Barsham|Ellingham|Harpley|Hardingham|…` and
`Lovell|Spelman|Calthorpe|Lestrange|Heydon|…`). Results:

- **Manuscript Norwich court/deposition films: near-zero context signal.** Scanning 100
  hits across the two big court films (004397070, 004397533) flagged only 2 pages; **both
  were false positives on reading** — `S3HY-DRBC-LF` "Gornsey" = **Guernsey** (a Lyme-Regis
  maritime entry), and `S3HY-DRBH-HM` "Hardingham" = a juror's **surname** ("Wm
  Hardingham"), not the manor, with the G-token a garble ("Gornburgly"). The 1608
  depositions film flagged **zero**. The lesson holds: salad transcripts rarely preserve a
  clean place token, so context-mining can't rescue them — and **reading the context is
  what catches the false positives** a binary place-match would mis-promote.
- **Clean-OCR printed films light up.** All 19 context flags came from **DGS 004389182**,
  which despite its "Norwich Deeds 1910" label is a **clean printed calendar/index** whose
  *content* spans medieval–Tudor Norfolk. New leads it exposed:
  - **Holkham MSS catalogue** entry: "...collections of Le Neve and the late **D. Gurney**...
    3276 originals" — points to **Daniel Gurney's own manuscript collection** (with the Le
    Neve papers) catalogued at Holkham. An archival lead beyond DG's *published* Record.
    *Unknown online* (the Holkham MSS catalogue itself; this is the 1910 printed notice).
  - A medieval Norfolk **name-list index** entry: "...Heydon ... Haveningham, **Gurnay** Elys
    Stutevyle Jno of E. ..." — an index to older Norfolk deeds/charters naming a Gurnay in a
    Heydon/Stuteville context. *Available online (this film).*

**Takeaway:** context-reading is the correct triage discipline, but its *yield* tracks OCR
quality — it rescues relevance from **clean** text (printed calendars/indexes) and exposes
false positives in **manuscript** text. The actionable redirect: **DGS 004389182 is itself a
clean-OCR Norfolk deeds calendar/index** (medieval–Tudor content) — a will-extracts-style
sweep target in its own right, not the throwaway "1910 deeds" the first pass logged (item 15).

### DGS 004389182 index sweep — Gurney content (context-read)

30 hits; reading the Gurney-context windows:
- **Medieval Gurnay deeds (line-relevant):** "...Heydon ... Haveningham, **Gurnay** Elys
  Stutevyle Jno, of E[llingham], & ors., Trustees"; "of **John Gurnay** mentioned ... Blithe,
  Multon [Moulton], Nolothe, Somerton" — Gurnay in medieval Norfolk trustee/deed contexts.
- **Tudor:** "**Gurnell (orig. written Gurney) Jno** ... St. Jno. Sepulchre ... 1556" — a John
  Gurney/Gurnell of St John Sepulchre, Norwich, 1556.
- **Printed pedigree pointer:** "**The Gurneys of Norwich, pp. 68–96**" — a substantial
  Norwich-Gurney section to identify and read (which volume?). *Unknown online.*
- **Daniel Gurney's MSS:** "...the late **D. Gurney** ... 3276 original letters" (with the Le
  Neve collection) — DG's own manuscript/letter collection catalogued at Holkham.

### Third caution — large local surname populations (compounds the dictionary-snapping one)

The later 004389182 entries are the **Norwich Quaker banking Gurneys** — "Hudson Gurney,"
"John Gurney of Norwich, merchant," "May Gurney & Co." That family is large, famous, and
exhaustively documented — and **entirely distinct from the West Barsham gentry line.** So in
Norwich records a "Gurney" hit is *more* likely the Quaker family than ours. Combined with
the dictionary-snapping caution, the rule for Norwich-geography hits is: **disambiguate the
family (Quaker bankers vs. West Barsham line vs. unconnected townsfolk) before promoting** —
period and parish help (the Quaker line rises in the later 17th c.; the medieval/Tudor
entries above predate it).

## Productive next vectors (replacing the co-occurrence approach)

1. **Pull the manuscript wills the catalogue already names** (forenames/kin the abstracts omit):
   - Calthorpe 1494 (PCC PROB 11/10, reg. Vox; NCC reg. Wolman) — *the* Gurney son-in-law's forename. *Available online.*
   - Lestrange 1505 (PCC reg. Adeane) — which Gurnay the sister married. *Available online (TNA).* 
   - The NRO-catalogued NCC wills: Loddon 1373 (reg. Heydon 32), Heigham 1434 (reg. Surflete 162). Resolve their DGS films from the NCC registered-copy-wills catalog (`koha:278818`) and image-walk, as was done for Harsyk. *Available online (film) — pending DGS resolution.*
2. **Hunt other typed Norfolk abstract/index typescripts** (the clean-OCR vector): e.g. printed/typescript indexes to the Norwich Consistory & Archdeaconry wills, Blomefield's manuscript collections, Rye's calendars — search the FamilySearch catalog for "Norfolk wills index/calendar/abstracts" beyond Bradfer-Lawrence.
3. **Scope FTS to specific manuscript films at Gurney loci** and read by image, accepting transcripts are only a finding aid — this is the original-browser-link approach (Norwich court/deposition, Costessey manorial); low yield per the corrupt-transcript problem, so reserve for a known target rather than open discovery.

<!-- Campaign run 2026-06-13 via the FTS JSON API (batched probes) against Allen's authenticated
session. No new pre-1660 Norfolk manuscript records found; result is a methodological negative
plus the API-batch technique. Concrete finds remain those in will-abstract-sweep-results.md and
non-familysearch-catalogue-leads.md. -->
