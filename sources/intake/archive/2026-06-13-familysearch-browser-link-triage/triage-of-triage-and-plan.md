# Triage-of-triage + work plan — 2026-06-13 FamilySearch browser-link batch

Second-pass review of the other AI's triage (`triage-summary.md`). Purpose: correct
dispositions, eliminate dead/duplicate items, identify what genuinely needs work,
and stage outsourceable bundles so the work survives a timeout.

Source list: `../13June2026-family-search-browser-links.md`
First-pass captures: `records/`, `images/`, `batch-results.json`, `triage-summary.md`

## Headline corrections to the first pass

1. **Item 20 (Spilman 1524 will naming "Antony Gurney … executor") is NOT a new lead — it is already in the repo.** The G17 companion captured it on 2026-06-11 (footnote `spilman-1524`: same film 008480295, image 149, ark `3Q9M-C39V-K2VN`, register "Cons: Alabaster 1520-3: 231"), flagged by Allen as lead L-101. The first pass ranked it a top-two "High" lead. **Disposition: reject (duplicate).** The image confirms it is a *typed abstract*, not manuscript — no paleography was ever needed here.
2. **Item 23 (Great Ellingham "Harney/Gurney") is almost certainly Harvey/Harney, not Gurney.** The page is saturated with a single Great Ellingham yeoman family — "Isacke Harney," "James Harney," "Abraham Harney," plus "James Harvey," "Mary Harvey," "Sarah Harvey." That is one family (Harvey/Harney) with OCR scatter into Carney/Larney, not a Gurney. **Disposition: reject pending a 30-second confirm** (folded into the paleography bundle as a cheap yes/no, not a standalone task).
3. **The single highest-leverage action in this batch is not in the first pass's "best leads" at all:** a systematic Gurney-variant sweep of the **typescript Norfolk will-abstract films** (008480295 and its sibling index/abstract volumes). These are *typed*, legible, and FTS-indexed; one sweep would harvest every Norfolk Gurney will abstract 1370–1763 at once. The Spilman 1524 and Wymondham 1475 hits already on the G17 file are two incidental fruits of a volume that has never been swept end-to-end. See "Broad-sweep candidates" below.
4. **The genuinely new, promotable English manuscript lead is Item 1 (the "Anne Gurney my daughter" will), and the first pass mis-framed it.** The image shows the testator is **not** a Gurney (a "Robert Gr—", will opening "In the name of God Amen"); "Anne Gurney my daughter" therefore means Anne is a *married-in* Gurney, i.e. this is the will of the **father-in-law of an unidentified Gurney man**, c. 1599–1601 Archdeaconry of Norwich. So Allen's "daughter of Henry G15" hypothesis is unlikely (that would make Anne a Gurney by birth). Still worth a full read — it would name a Gurney marriage in the right place and window. **Disposition: paleography bundle (primary).**

## Re-disposition table (my call)

Legend — **Reject** (no value / dead / duplicate), **Park** (logged, low priority, revisit only on a related gap), **Paleography** (needs expert manuscript read — outsource), **Pull-underlying** (index/pointer page; fetch the record it points to), **Sweep** (belongs to a broad film sweep).

| # | Source (DGS, image) | First pass | My call | Reason |
|---|---|---|---|---|
| 1 | Archd. Norwich Wills v.28, 008077025, img 339–340 | High | **Paleography (primary)** | New. Testator not a Gurney; will names "Anne Gurney my daughter" — a Gurney marriage c.1600 Norfolk. Bundle 01. |
| 2 | Norwich Court 1636–46, 004397113, img 275 | Moderate | **Park** | Lone "Fr. Gurney" in OCR salad; no context. Revisit only if a Norwich-court arc opens. |
| 3 | London Occupation Rec., 008960701, img 271 | Low | **Reject** | No usable Gurney snippet. |
| 4 | Costessey Manorial 1633–35, 004389191, img 162 | Moderate, caution | **Verify-then-park** | "John Gurney rental." Costessey is a *known* locus — check `research/people/gurney-family-costessey-manorial.md` for dup/known false-positive before any work. Costessey Gurney = the laceweaver Francis's circle (AGENTS §6.4). |
| 5 | Norfolk/Norwich Court 1630–36, 004397070, img 231 | Low | **Reject** | No clear hit. |
| 6 | Norwich Deposition 1639, 004389254, img 318 | Low-mod | **Reject** | "The Gurney" in word salad. |
| 7 | Norfolk/Norwich Court 1630–36, 004397070, img 127 | Low | **Reject** | "Folk Gurney" — corrupt. |
| 8 | Norfolk/Norwich Court 1619–30, 004397533, img 304 | Moderate | **Park** | "Noble Gurney" name-list, ambiguous (person/place/artifact). Low certainty. |
| 9 | Bridgewater Prop. Settlement, 007009746, img 62 | Low-context | **Reject** | Ames/Bridgewater narrative; not a Gurney source. |
| 10 | Plymouth Dir./Norfolk-Dedham VR, 007548965, img 4 | Low-context | **Reject** | No hit. |
| 11 | Suffolk MA Probate, 105278058, img 788 | Moderate | **Reject** | Nathan Gurney of Boston, Judge of Probate, 1837 — 19th-c. collateral; `research/people/nathan-gurney-abington.research.md` already exists. Not the direct arc. |
| 12 | Braintree VR index, 007009769, img 72 | Moderate | **Park (pointer)** | Alphabetical "Gurney John" index; L-11 already covers the Braintree manuscript VRs. Use only as a finding-aid into L-11. |
| 13 | Burke's Landed Gentry 1858, 008087638, img 262 | Moderate (orientation) | **Reject (dup lead)** | Tertiary; L-71 already tracks the Burke 1858 Gurney/de Gournay pedigree. Nothing new. |
| 14 | UK/Ireland Genealogies 1847, 008881667, img 273 | Low | **Reject** | Hit is Gurdon/Gun, not Gurney. |
| 15 | Norwich Deeds **1910** index, 004389182, img 45 | Moderate | **Park** | "Gurnell (orig. written Gurney) Jno." is interesting onomastically but 1910 is far too late for the ancestral line. No pre-1700 value. |
| 16 | Norfolk Wills 1370–1763, 008085264, img 800 | Low | **Reject as a page / Sweep as a film** | Robert Sayer abstract, no Gurney *here* — but this is a **sibling abstract/index volume** to 008480295. Add the film to the sweep, not the page. |
| 17 | Norwich Deposition **1608**, 004389252, img 104 | Moderate | **Paleography (secondary, optional)** | Manuscript "said Gurney" in a deposition — depositions can preserve neighbourhood/litigation detail. Single-token, low certainty; only worth a read if a paleographer has spare capacity. Bundle 01 appendix. |
| 18 | Norwich Wills 1626–29 etc., 008477113, img 766 | Low | **Reject** | No hit. |
| 19 | Suffolk MA Probate, 102907158, img 964 | Moderate | **Pull-underlying / Paleography (American, easy)** | "John Gurney land" in an inventory/account — possibly G13-era John Gurney of Braintree. American secretary hand (easier). Route to the John Gurney G13 arc. Bundle 02. |
| 20 | Norfolk Wills 1370–1763, 008480295, img 149 | **High** | **Reject (DUPLICATE)** | Already in G17 companion as `spilman-1524` (L-101). See headline #1. |
| 21 | Conway Cemetery index, 008977901, img 303 | Low | **Reject** | Later American cemetery index; no current gap. |
| 22 | Suffolk MA Deeds 1661–72 index, 007442495, img 631 | Moderate | **Pull-underlying** | Grantee index: "12 June 1668, Richard [Thayer?] ← John Gurney, Deed." Points to a deed in vol. 4–7. G13-era American land transaction. Pull the deed page; route to the John Gurney case file. Bundle 02. |
| 23 | Norfolk Wills 1660–61 (vol.135), 008472225, img 175 | Moderate, uncertain | **Reject (confirm-only)** | Harvey/Harney family of Great Ellingham, not Gurney (headline #2). 30-sec confirm in Bundle 01, else drop. |

### Net result
- **Reject:** 3, 5, 6, 7, 9, 10, 11, 13, 14, 18, 20, 21, 23 (13 items — including the one "High" duplicate).
- **Park / verify:** 2, 4, 8, 12, 15 (5 items).
- **Real work:** 1 (paleography, primary), 19 + 22 (American pull-underlying, John Gurney G13 arc), 17 (optional paleography).
- **Bigger prize than any single item:** the will-abstract film sweep.

## Outsourcing bundles (hand-off artefacts)

Prepared as self-contained markdown so the external paleography agent — or a fresh
session after a timeout — can pick them up cold.

- **Bundle 01 — `paleography-bundle-01.md`** — Item 1 (Anne Gurney will, Archd. Norwich v.28, imgs 338–340). Primary. Appendices: Item 23 confirm-and-reject (Harvey/Harney), Item 17 optional 1608 deposition. *Status: written this session.*
- **Bundle 02 — American John Gurney pulls (Items 19 + 22)** — *not yet written.* Lower priority and not paleography-blocked (legible American hands / index → deed pull). Belongs to the John Gurney G13 case-file arc; defer until Allen confirms he wants the American strand advanced now. Stub assignment in "Next actions" below.

Paleography agents/sessions: the committed `images/*.jpg` are 2-page spreads at
moderate resolution and **may be too low for confident secretary-hand work**. Re-pull
full-resolution single-page images via the FTS image-download recipe in
`.claude/skills/familysearch-fulltext-research/SKILL.md` using the ARK + image number +
DGS recorded in each `records/NN-*.md`. Authenticated FamilySearch (Allen's Chrome/Edge)
required.

## Broad-sweep candidates (the high-leverage item)

All **Available online** (FamilySearch FTS; authenticated session, browser-driven —
this is what timed out on the first pass, so it needs the Chrome MCP against Allen's
logged-in session, not a headless run).

1. **Typescript Norfolk will-extracts series — full Gurney sweep. ✅ DONE 2026-06-13 — see `will-abstract-sweep-results.md`.** Resolved the source to the 6-reel **Bradfer-Lawrence "Norfolk wills extracts, 1370–1763"** (catalog `koha:1056823`) and swept all six (5 FTS-indexed; reel 1 `008100792` is a coverage gap). **Three new promotable gentry-marriage finds:** Sir William Calthorpe's 1494 will naming a Gurney son-in-law ("Son Gurney"); Sir Roger Lestrange's 1505 will naming a "sister Gurnay"; and William Smith of Gt Massingham's 1643 will naming "Edm: Gurnay / Ellen Gournay" (likely Edmund the Divine + a candidate wife-name). Plus moderate mentions (1606 sister Joan Gurney, 1514–17 John Gurney of Kenton, 1654 Elizabeth Gournay, 1683 Gourney Crowe), two confirmed duplicates (Spilman 1524, Wymondham 1475), and Gurnell false positives. Six full-res abstract images saved as `images/sweep-*.jpg`. Promotion pending a Phase-1 patchset + placement decisions.
2. **Archdeaconry of Norwich Wills v.28 (008077025) — scoped sweep around img 339–340.** While Bundle 01 is read, sweep the same register for other Gurney wills/legatees in the 1599–1601 window (manuscript, so lower-confidence FTS, but cheap to try with `Gurn*`/`Gourn*` and snippet fragments).
3. **Lower priority:** the Norwich court/deposition films behind parked items (004397113, 004397070, 004397533, 004389252, 004389254) — only worth a scoped sweep if a Norwich-civic arc is opened; expected yield low given the OCR-salad quality.

## Non-FamilySearch items (separate mini-triage — not yet done)

From the source list; the first pass did not touch these. **Potentially the best medieval leads in the whole batch** and they should be checked against existing research before any patchset:

- `archive.org/details/bim_eighteenth-century_catalogue-des-rolles-gas_carte-thomas_1743_2` (Carte, *Catalogue des rolles gascons*, q=gourney) — **Available online (archive.org).** Cross-channel/Gascon rolls; check against the Norman/early-line topic files.
- NRO catalogue `gurney-gernays-john-cap-de-lodne-holy-trinity` — **Available online (NRO catalogue).** Allen's note: a **1373 will** (John Gurnay/Gernays of Loddon, Holy Trinity). Check vs. the G23/medieval-Norfolk leads (cf. L-68 central-Norfolk collaterals, L-34 1387 will arc).
- NRO catalogue `gurnay-thomas-of-great-ellingham-norfolk` — **Available online.** Thomas Gurnay of Great Ellingham; cf. L-68 (Thomas Gurnay of Great Ellingham, Aleyn 19, 1454 admon) — likely the same and possibly already logged in `research/places/great-ellingham.md`.
- NRO catalogue `gurney-gurnay-alice-formerly-wife-of-william-gurnay-of-heygham-juxta-norwich` — **Available online.** Alice, widow of William Gurnay of Heigham juxta Norwich — a named Gurney marriage; check vs. central-Norfolk collateral cluster.

## Next actions (timeout-resilient checklist)

Each carries an availability tag and an owner suggestion.

1. **[Outsource — paleography agent]** Bundle 01: transcribe the Anne Gurney will (imgs 338–340), confirm/deny Item 23 surname, optional Item 17. *Available online — FamilySearch (auth).* Deliverable: transcription + identity notes back into this folder.
2. **[Browser session — Chrome MCP, Allen authenticated]** Broad sweep #1 (will-abstract films 008480295 + 008085264) for all Gurney variants. *Available online — FamilySearch (auth).* This is the single highest-value pull.
3. **[Quick verify — any session]** Item 4 against `gurney-family-costessey-manorial.md`; Item 12 against L-11. Resolve dup-vs-new. *Available online.*
4. **[Mini-triage — any session]** The four non-FamilySearch links above, checked against existing medieval/Great-Ellingham research. *Available online.* The 1373 Loddon will and the Heigham Alice marriage are the ones to prioritise.
5. **[Defer until Allen confirms American strand]** Bundle 02 (Items 19 + 22) into the John Gurney G13 case-file arc. *Available online — FamilySearch (auth).*

## What is NOT ready for a patchset

Nothing in this batch is promotable as-is. The one item that *was* directly
promotable (Item 20) is already in the repo. Everything else needs either a
paleography read (Item 1), an underlying-record pull (Items 19, 22), a dup-check
(Items 4, 12), or the broad sweep. Patchsets follow once those return content —
they are not warranted yet.

<!-- Process trail: second-pass triage of the 2026-06-13 FamilySearch browser-link batch.
Dedup checks run against research/ for Spelman/Turrell/1524 (item 20 → g17 spilman-1524),
Nathan Gurney (item 11 → nathan-gurney-abington), Costessey (item 4 → gurney-family-costessey-manorial),
and the John Gurney G13 American arc (items 19, 22). Images 01 and 20 read directly. -->
