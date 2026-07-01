**Done:** 2026-06-30 16:28 PT

# v120 — G13 John Gurney colonial property: Weymouth land-grants manuscript + NPS Adams CLR (sources, corpus, media, packet-40 disposition, place spine)

Phase 1 patchset. Promotes the property/place research from the June 2026 thread into the source layer and the place spine. Companion/topic narrative, the chronology table, and the Billerica/Boston promotions are a **separate patchset (v121)**; the G-13 fact sheet is **v122**. This patchset is self-contained and lossless for the source + place-spine work below.

**Sources touched:** `weymouth-land-grants-book-ms` (new), `nps-adams-nhp` (update), plus existing `nash-historical-sketch-weymouth-1885`, `history-of-weymouth`, `suffolk-deeds-liber-iv-1888`, `nehgr-30-432`, `bates-ancient-iron-works-braintree-1898` (already registered; cited only).

**Two-presidents context (for the companion/fact-sheet, recorded here so it is not lost):** the NPS *Cultural Landscape Report* establishes that the 45-acre Braintree farm John Gurney leased from William Tyng in 1647 became, ~130 years later, the **Adams family seat** — the northern portion of "the Gurney farm" was the site of the Adams property; "The Old House" (Peace field) was first acquired by the Adams family in 1787, and the Adams Birthplaces nearby are the birthplaces of John Adams (2nd U.S. president) and John Quincy Adams (6th). High-precision coordinate for the northern end of the Gurney farm, supplied by Allen Gurney: **42.239204, -71.003610**.

---

## Item 1 — Register source `weymouth-land-grants-book-ms` (Weymouth proprietors' Land Grants book, manuscript) — PROMOTE

The packet-40 paleographic read produced a manuscript-level corpus_supplement that already exists in the working tree (`sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md`) but is not yet registered. Register it.

**1a. `data/sources.json` — insert a new source object.** `str_replace`:

`old_string`:
```
    "nps-adams-nhp": {
      "shortTitle": "NPS Adams National Historical Park CLR",
```
`new_string`:
```
    "weymouth-land-grants-book-ms": {
      "shortTitle": "Weymouth Land Grants book (MS)",
      "citation": "Weymouth, Massachusetts. Proprietors' early Land Grants book (\"the old town book\"), manuscript. FamilySearch film/DGS 007009659.",
      "archive": "FamilySearch",
      "url": "https://www.familysearch.org/search/film/007009659",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md",
      "mediaPath": null,
      "validationPath": "sources/validations/weymouth-land-grants-book-ms.md",
      "notes": "Manuscript of the 1643 Weymouth possession survey transcribed in print by Nash (1885 App. C). Packet-40 image read (images 00128-00145, ms pp. 9-32) confirms John Gurney as original grantee of three parcels: two 2-acre East Field lots (p.12 under Robert Randoll, 'John Gurny'; p.23 under Nathaniel Addames, 'John Gurnie') and one 4-acre Mill Field lot (p.31 under Thomas Richardes, 'John Gurnie'). Grants undated; all reassigned to other men by the survey."
    },
    "nps-adams-nhp": {
      "shortTitle": "NPS Adams National Historical Park CLR",
```

**1b. New file — `sources/validations/weymouth-land-grants-book-ms.md`:**
```
# Validation — Weymouth proprietors' Land Grants book (manuscript)

**Source ID:** `weymouth-land-grants-book-ms`

**What was examined.** FamilySearch film/DGS 007009659, images 007009659_00128–00145 (manuscript pp. 9–32), the continuous 1643 possession survey. Packet-40 paleographic read, June 2026; Nash's 1885 printed transcription (Appendix C) used as a reading aid against the manuscript images.

**What portion.** The three John Gurney clauses image-confirmed: p. 12 (image 00135, "John Gurny" under Robert Randoll), p. 23 (image 00140, "John Gurnie" under Nathaniel Addames), p. 31 (image 00144, "John Gurnie" under Thomas Richardes). Owner headings, page sequence, and many parcel lines checked against the images.

**What remains uncertain.** Much of the manuscript is badly faded; the continuous text is Nash-assisted, not a fresh diplomatic transcription of every letter. The packet does not contain the 1636 First Division or the 2 February 1651–52 great-lot list (those are on later images not staged).

**Where findings landed.** `sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md`; promoted to `research/places/east-field-weymouth-ma.md`, `research/places/mill-field-weymouth-ma.md`, and the G13 companion (patchset v121). Packet-40 staging report/transcript moved to `sources/intake/done/`.
```

(The corpus_supplement file itself already exists in the working tree and needs no rewrite. It contains no lead handles, per source-layer rules.)

---

## Item 2 — Update source `nps-adams-nhp`; add CLR corpus extract + media — PROMOTE

The NPS *Cultural Landscape Report, Adams National Historic Site* (1997) is the source behind the "45 acres / John Gurney / Adams property" finding. The PDF and a text layer were downloaded to `sources/intake/new/pdfs/clr-1997.pdf` and `clr-1997.txt` (U.S. Government work, no copyright). The PDF is 38.4 MB (over the 35 MB media cap → `_local/`).

**2a. `data/sources.json` — update the `nps-adams-nhp` object.** `str_replace`:

`old_string`:
```
      "citation": "National Park Service. Cultural Landscape Report, Adams National Historical Park, Quincy, Massachusetts.",
      "archive": "National Park Service",
      "url": null,
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Independent non-genealogical source identifying John Gurney among early Braintree tenants within the future park boundaries. Reports John died with no land."
```
`new_string`:
```
      "citation": "National Park Service. Cultural Landscape Report, Adams National Historic Site, Quincy, Massachusetts. 1997.",
      "archive": "National Park Service (npshistory.com)",
      "url": "https://npshistory.com/publications/adam/clr-1997.pdf",
      "corpusStatus": "full",
      "corpusPath": "sources/corpus/nps-adams-clr-1997.txt",
      "mediaPath": "sources/media/nps-adams-nhp/",
      "validationPath": "sources/validations/nps-adams-nhp.md",
      "notes": "1997 Cultural Landscape Report, Adams National Historic Site (npshistory.com). Site Chronology pp. 12-13 and Figure 1 ('William Tyng's 45-acre farm, Braintree, 1649', by Ezekiel Sargent) record: 1647 Tyng leased John Gurney a 45-acre Braintree farm for ten years; Gurney continued leasing it from Tyng's daughters Bethia and Mercy until 1662; the northern portion of 'the Gurney farm' became the Adams Old House property (central Quincy). Authority = Ezekiel Sargent MSS, Quincy Historical Society, 'Land Formerly of William Tyng.'"
```

**2b. New file — `sources/corpus_supplement/nps-adams-clr-1997-gurney-tyng-extracts.md`:**
```
# NPS Adams CLR (1997) — John Gurney / William Tyng farm extracts

Extracts from the National Park Service, *Cultural Landscape Report, Adams National Historic Site*, Quincy, Massachusetts (1997), bearing on John Gurney's leased Tyng farm. Source ID: `nps-adams-nhp`. Full PDF: https://npshistory.com/publications/adam/clr-1997.pdf (U.S. Government work, no copyright). The report's colonial chronology rests on the Ezekiel Sargent manuscripts, Quincy Historical Society ("Land Formerly of William Tyng").

## Historical background of the property and community (report pp. 1-2 / PDF pp. 10-11), verbatim

> The earliest European settlement of Quincy, albeit temporary, occurred in 1625 when Captain Wollaston arrived in Quincy Bay from an unknown port in England. … a portion of his company remained in the area and the Wollastons were later recorded as residents of Braintree.

> In 1634, the Mount Wollaston region, which included Braintree and what would become Quincy, Holbrook and Randolph, was annexed by the City of Boston in an effort to provide additional room for the establishment of large estates. The earliest land grants, including 600 or more acres, were made to Boston residents Edmund Quincy, Atherton Houghton, John Wilson and William Coddington; later allotments were based on a formula of 4 acres per family member. The current site of the Adams National Historic Site was included within the great Quincy-Coddington Grant of 1635.

> A commercial center was developed in 1640 in the area that is now Quincy Center, which was included within the bounds of the newly established First Parish of Braintree. A meeting house near the intersection of Hancock Street and the Town Brook was built in 1640 … By 1640 a town burial ground had also been established at Hancock Cemetery …

> Settlement along these early routes consisted primarily of farmsteads, of which the John Quincy Adams Birthplace (1663) and the John Adams Birthplace (1681) are two extant examples. … Now designated Adams, Hancock, School and Franklin Streets, this road served as the primary link between Boston and the coastal communities to the south.

> In 1708 Braintree was divided into the North Precinct (now Quincy) and the South Precinct (now Braintree, Holbrook and Randolph). … In 1792 the North Precinct of Braintree was incorporated into the Town of Quincy.

> Deeds of sale for the property prior to its acquisition by the Adamses in 1787 describe it as including a house lot of 6 to 12 acres with associated farmland of 45 to 70 acres extending north over Furnace Brook and south across Adams Street to what is now Presidents Hill. … A journal entry by John Adams in 1769 … noted that the land south of Adams Street, known as Stony Field Hill, was planted with corn and fruit.

## Site Chronology up to 1787 (pp. 12-13), verbatim

> 1639-41 — A large portion of the Coddington property was purchased by a Boston merchant named William Tyng, who divided the property into two farms.

> 1647 — William Tyng leased a section of 45 acres to John Gurney for ten years. According to the records left by Ezekiel Sargent of Quincy, the northern portion of the Gurney farm was later the site of the Adams property.

> 1653 — William Tyng died January 10. The inventory of his estate lists "45 acres of land, upland and marsh in the possession of John Gurney."

> 1657 — Gurney continued to lease the farm from Tyng's daughters, Bethia and Mercy until 1662.

> 1662-1710 — There is no available documentation of ownership of the Old House property during this period. Gurney moved away from Braintree and apparently abandoned the farm since the inventory taken at his death showed no land holdings.

## Figure 1 caption (p. 3 list of figures; map at p. 13)

> William Tyng's 45-acre farm, Braintree, Massachusetts, 1649. By Ezekial Sargent, Quincy, Massachusetts. Quincy Historical Society, Sargent MSS Collection, "Land Formerly of William Tyng".

The Sargent map labels the 45-acre parcel "William Tyng / John Gurney (Lease) / Gregory Belcher," with "Salters Farm — William Tyng — Gregory Belcher (lease)" to the northeast, "Stoney Field" southwest, "Edmund Quincy" southeast, "Crosby" north, "the Plain Land" south, along Adams Street.

## Site Chronology, later owners (pp. 13-14), summarized

> 1710 — The property was listed in the ownership of Nathaniel Spear, a cooper of Braintree. 1717 — Nathaniel Spear sold to Thomas Crosby several tracts including the Old House property, "one being the Homestead containing about ten acres … through which the country road runs," with a dwelling house, barn and corn house. 1730 — Thomas Crosby sold the 10-acre Old House tract to Leonard Vassall, a sugar planter from Jamaica then living in Boston. 1731 — date commonly assigned to the Vassall mansion (the Adams Old House). 1787 — John Adams purchased the Vassall-Borland property.

## End Notes — source apparatus for the colonial chronology (p. 79), verbatim

The colonial chronology entries above are footnoted to these sources (notes 1-9, in order):

> Historical information on Quincy is adapted from the National Register Nomination for the Quincy Multiple Resource Area, 1989. // William Churchill Edwards, *Historic Quincy, Massachusetts* (Quincy, MA: 1955, privately printed). // Helen Skeen, *Documentary Narrative of Buildings Shown on Historic Base Map of the Adams National Historic Site* (unpublished report, National Park Service, Adams National Historic Site, 1965): 4. // Suffolk County Registry of Deeds, State House, Boston, MA. Cited in Wilhelmina Harris, *Furnishings Report for the Old House*, Vol. 9 (1966-68): 815. // Helen L. Nelson, *Historical Research Report: The Structural History of the Old House, Adams National Historic Site* (unpublished report, National Park Service, 1963): 2. // Suffolk County Probate Records, State House, Boston, Libra 2, Folio 98. Cited in Nelson, *Structural History of the Old House*, p. 2. // Suffolk County Registry, Libra 4, Folio 5. Cited in Nelson, p. 2. // Ezekiel Sargent MSS Collection, Quincy Historical Society, "Quincy Centre" p. 26. Cited in Nelson, p. 2. // Suffolk County Registry, Libra 44, Folio 128 (cited in Charles Peterson, *Historic Structures Report, Part 1: The Adams Mansion*, 1963, 8).

The 1653 Tyng inventory (the "45 acres … in the possession of John Gurney" entry) is thus citable one level deeper to **Suffolk County Probate Records, Liber 2, folio 98** (via Nelson 1963), and the 1647 lease / 1657 continuation to the Sargent MSS and Suffolk Registry Liber 4 folio 5.

## Source notes

The CLR reads the 1653 Tyng inventory as "45 acres"; the *NEHGR* vol. 30 (1876) p. 432 abstract of the same inventory reads "48 Akers." The figure 45 is used consistently in the CLR and the Sargent map. The CLR labels the northernmost 10 acres of the 45-acre farm "Salter's farm," which does not match the genealogical sources' use of "Salter's Farm" for the separate ~500-acre Mount Wollaston farm (leased to John Read 1639-49 and Gregory Belcher from 1657-8) — a naming discrepancy between the two source streams.
```

**2c. New file — `sources/validations/nps-adams-nhp.md`:**
```
# Validation — NPS Adams National Historic Site Cultural Landscape Report (1997)

**Source ID:** `nps-adams-nhp`

**What was examined.** National Park Service, *Cultural Landscape Report, Adams National Historic Site* (1997), 85-page PDF (npshistory.com/publications/adam/clr-1997.pdf). Site Chronology pp. 12-13 and Figure 1 read in full for the John Gurney / William Tyng material.

**What portion.** The colonial chronology entries 1639-41, 1647, 1653, 1657, 1662-1710, and the Figure 1 caption. The remainder of the report concerns the Adams-era landscape (post-1730) and was not mined.

**What remains uncertain.** The 1647 lease date, ten-year term, and "northern portion = Adams property" trace to the Ezekiel Sargent manuscripts (Quincy Historical Society), a 20th-century compilation; the underlying 1647 lease deed has not been located. The CLR's "45 acres" vs NEHGR's "48 acres" for the 1653 Tyng inventory is unresolved (decisive = the inventory image, Suffolk Probate Liber 8:62).

**Where findings landed.** `sources/corpus_supplement/nps-adams-clr-1997-gurney-tyng-extracts.md`; `research/places/gurney-tyng-farm-quincy-ma.md` (new); `research/places/braintree-ma.md`; the G13 companion (patchset v121). Media: `sources/media/nps-adams-nhp/`.

**Media note.** The 38.4 MB source PDF exceeds the 35 MB repo media cap and is parked in `sources/media/nps-adams-nhp/_local/` (canonical copy retrievable from the npshistory.com URL). The committed working-reference image is the Sargent 45-acre-farm map (Figure 1), extracted as PNG.
```

**2d. Media operations (Phase 2).**
- Move `sources/intake/new/pdfs/clr-1997.pdf` → `sources/media/nps-adams-nhp/_local/clr-1997.pdf` (oversize; `_local/`).
- Move `sources/intake/new/pdfs/clr-1997.txt` → `sources/corpus/nps-adams-clr-1997.txt` (full text layer of the CLR; public-domain U.S. Government work; this is the searchable corpus copy referenced by `corpusPath`). The curated Gurney/Tyng extract `sources/corpus_supplement/nps-adams-clr-1997-gurney-tyng-extracts.md` (Item 2b) is the companion supplement.
- Extract Figure 1 (the Ezekiel Sargent "William Tyng's 45-acre farm" map, p. 13 region of `clr-1997.pdf`) to `sources/media/nps-adams-nhp/sargent-tyng-45-acre-farm-1649-gurney-lease.png`.
- New file — `sources/media/nps-adams-nhp/_local/README.md`:
```
# nps-adams-nhp local-only masters

- `clr-1997.pdf` — National Park Service, Cultural Landscape Report, Adams National Historic Site (1997). Reason: oversize (38.4 MB > 35 MB cap). U.S. Government work, no copyright. Canonical copy: https://npshistory.com/publications/adam/clr-1997.pdf
```

---

## Item 3 — Packet-40 paleographic work: final disposition — PROMOTE

The packet-40 manuscript read (Weymouth Land Grants book) is complete and promoted (Items 1, 4, 5, 7). Preserve the source text and the images; archive only the analysis brief and report.

**3a. Preserve the full transcript as a corpus supplement.** Move and register the full working transcription:
- `sources/intake/paleography-staging/packet-40-weymouth-land-grants-1643-1651-gurney.transcript.md` → `sources/corpus_supplement/weymouth-land-grants-book-1643-full-transcript.md` (the full Nash-assisted manuscript transcription of pp. 9-32, with the manuscript-to-Nash page map). Ties to `weymouth-land-grants-book-ms`. On the move, strip any process/review framing per the source-layer rules (corpus files carry no lead handles or research-status language); keep the verbatim transcription. Both this full transcript and the curated `weymouth-land-grants-book-1643-gurney-manuscript-extracts.md` belong to the same source.

**3b. Images to media.**
- `sources/intake/paleography-staging/images/packet-40-weymouth-land-grants-1643-1651-gurney/007009659_00128.jpg`–`00145.jpg` (original page masters) → `sources/media/weymouth-land-grants-book-ms/_local/` (full raw set is oversize; canonical copy is FamilySearch film 007009659).
- Keep as **committed** working-reference crops in `sources/media/weymouth-land-grants-book-ms/`: the two faint-clause reading sheets `packet40-p23-john-gurnie-east-field-sheet.png` and `packet40-p31-john-gurnie-mill-field-sheet.png`, plus the clear p.12 Randoll/`John Gurny` token crop. Discard the remaining intermediate workbench derivations (line-strips, contact sheets, manifests) — they are reproducible and need not be retained.
- New file — `sources/media/weymouth-land-grants-book-ms/_local/README.md`:
```
# weymouth-land-grants-book-ms local-only masters

- Packet-40 raw page images (`007009659_00128.jpg`–`00145.jpg`). Reason: oversize raw set. Canonical: FamilySearch film 007009659 (https://www.familysearch.org/search/film/007009659). Committed working-reference crops for the two faint Gurney clauses and the p.12 token are kept one level up in `sources/media/weymouth-land-grants-book-ms/`.
```

**3c. Archive the analysis artefacts to `done/`.**
- `sources/intake/paleography-staging/packet-40-weymouth-land-grants-1643-1651-gurney.report.md` → `sources/intake/done/`
- `sources/intake/paleography-staging/packet-40-weymouth-land-grants-1643-1651-gurney.md` (the original packet brief) → `sources/intake/done/`

No packet-40 source content is lost: the full transcript becomes a corpus supplement (3a), the page images are preserved in media (3b), and the curated extract (Item 1) and place files (Item 7) carry the findings.

---

## Item 4 — `data/places.json`: fix Weymouth field dates; add two new Braintree-area places — PROMOTE

**4a. East Field — correct the date in `shortDescription`** (the East/Mill Field grants are the c.1639–41 parcels, not 1651–52; 1651–52 is the Whitman's-Pond great lot). `str_replace`:

`old_string`:
```
    "name": "East Field, Weymouth, Massachusetts, USA",
    "aliases": [
      "The East Field, Weymouth"
    ],
    "shortDescription": "John Gurney Sr. land grant, 1651–52; parcel unlocated",
```
`new_string`:
```
    "name": "East Field, Weymouth, Massachusetts, USA",
    "aliases": [
      "The East Field, Weymouth"
    ],
    "shortDescription": "John Gurney Sr. original grantee of two East Field lots, c. 1639–41 (reassigned by 1643); parcels unlocated",
```

**4b. Mill Field — correct the date in `shortDescription`.** `str_replace`:

`old_string`:
```
    "name": "Mill Field, Weymouth, Massachusetts, USA",
    "aliases": [
      "The Mill Field, Weymouth"
    ],
    "shortDescription": "John Gurney Sr. land grant, 1651–52; parcel unlocated",
```
`new_string`:
```
    "name": "Mill Field, Weymouth, Massachusetts, USA",
    "aliases": [
      "The Mill Field, Weymouth"
    ],
    "shortDescription": "John Gurney Sr. original grantee of a 4-acre Mill Field lot, c. 1639–41 (reassigned by 1643); parcel unlocated",
```

**4c. Add two new place objects** (the Tyng leasehold and the Monatiquot freehold), inserted after the Billerica entry. `str_replace`:

`old_string`:
```
    "filename": "billerica-ma.md"
  },
  {
    "placeId": "place-collegiale-saint-hildevert-gournay-en-bray-normandy-france",
```
`new_string`:
```
    "filename": "billerica-ma.md"
  },
  {
    "placeId": "place-gurney-tyng-farm-quincy-massachusetts-usa",
    "name": "John Gurney's leased Tyng farm (later the Adams Old House), Braintree/Quincy, Massachusetts, USA",
    "aliases": [
      "William Tyng's 45-acre farm, Braintree",
      "the Gurney farm, Braintree",
      "Adams Old House / Peace field",
      "Mount Wollaston, Braintree"
    ],
    "shortDescription": "45-acre farm John Gurney leased from William Tyng 1647–1662; its northern part became the Adams family seat",
    "placeType": "locality",
    "coordinate": {
      "lat": 42.239204,
      "lng": -71.00361
    },
    "coordinatePrecision": "high",
    "roles": [
      "landholding / property reference"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g13-john-gurney-1",
        "role": "landholding / property reference"
      }
    ],
    "filename": "gurney-tyng-farm-quincy-ma.md"
  },
  {
    "placeId": "place-gurney-monatiquot-freehold-braintree-massachusetts-usa",
    "name": "John Gurney's Monatiquot River freehold, Braintree, Massachusetts, USA",
    "aliases": [
      "Gurney house and orchard, Monatiquot",
      "Monotecott, Braintree"
    ],
    "shortDescription": "House, orchard, and ~5.5 acres on the Monatiquot River that John Gurney owned and sold to Richard Thayer, 1661/2",
    "placeType": "locality",
    "coordinate": {
      "lat": 42.21,
      "lng": -70.992
    },
    "coordinatePrecision": "low",
    "roles": [
      "landholding / property reference"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g13-john-gurney-1",
        "role": "landholding / property reference"
      }
    ],
    "filename": "gurney-monatiquot-freehold-braintree-ma.md"
  },
  {
    "placeId": "place-collegiale-saint-hildevert-gournay-en-bray-normandy-france",
```

---

## Item 5 — `data/places_detail.json`: update Weymouth field detail; add two new detail entries — PROMOTE

**5a. East Field detail — record the two parcels (manuscript-confirmed).** `str_replace`:

`old_string`:
```
    "longDescription": "An open-field division of early Weymouth in which John Gurney Sr. (G13) held a two-acre grant recorded in Nash's 1643 property list (Historical Sketch of Weymouth, Appendix C, p. 258) as 'first granted to John Gurny' — by then held by Robert Randoll, a Wendover, Buckinghamshire emigrant. The East Field lay in the original North/East Weymouth settlement: its lots are bounded in the records 'with the sea,' the Back River, and 'a greate pond' (Whitman's Pond), placing it east of the first settlement toward the water. The exact bounds are not established from sources to hand.",
```
`new_string`:
```
    "longDescription": "An open-field division of early Weymouth in which John Gurney Sr. (G13) was the original grantee of two separate two-acre lots, confirmed by the manuscript Land Grants book (film 007009659): one (ms p. 12, 'John Gurny') by 1643 held by Robert Randoll of Wendover, Buckinghamshire, bounded east by Edmond Hart and the highway, west by Robert Cooke, north and south by Nathaniel Addames; a second (ms p. 23, 'John Gurnie') held by Nathaniel Addames, bounded east by Jeffery Staple, west by Robert Randoll, north by a cedar swamp, south by the highway. Both were 'first granted/given to' John and reassigned by the 1643 survey. The East Field lay in the original North/East Weymouth settlement, its lots bounded 'with the sea,' the Back River, and 'a greate pond' (Whitman's Pond). Exact bounds are not established from sources to hand.",
```

**5b. Mill Field detail — link the manuscript read.** `str_replace`:

`old_string`:
```
    "coordinateBasis": "general East Weymouth area near Whitman's Pond, Mill River, and the Hingham line, per neighboring Mill Field grants; parcel unlocated",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "",
    "heritageLabel": "",
    "reviewNotes": [
      "Low precision: coordinate is the field's general area (East Weymouth, near Mill River and the Hingham line), not a documented parcel. Locating it requires the Weymouth proprietors' land-grant records; see research lead."
    ]
  },
  {
    "placeId": "place-billerica-massachusetts-usa",
```
`new_string`:
```
    "coordinateBasis": "general East Weymouth area near Whitman's Pond, Mill River, and the Hingham line, per neighboring Mill Field grants; parcel unlocated",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "",
    "heritageLabel": "",
    "reviewNotes": [
      "Low precision: coordinate is the field's general area (East Weymouth, near Mill River and the Hingham line), not a documented parcel. The four-acre Gurney lot is image-confirmed in the manuscript Land Grants book (film 007009659, ms p. 31) but not surveyed; see research lead L-182."
    ]
  },
  {
    "placeId": "place-billerica-massachusetts-usa",
```

**5c. Add two new detail entries**, inserted after the Billerica detail entry. `str_replace`:

`old_string`:
```
    "reviewNotes": [
      "Town-level aggregate only; the Dudley Farm rate-list entry does not by itself identify a precise John Gurney parcel or residence site."
    ]
  },
  {
    "placeId": "place-collegiale-saint-hildevert-gournay-en-bray-normandy-france",
    "placeName": "Collégiale Saint-Hildevert, Gournay-en-Bray, Normandy, France",
```
`new_string`:
```
    "reviewNotes": [
      "Town-level aggregate only; the Dudley Farm rate-list entry does not by itself identify a precise John Gurney parcel or residence site."
    ]
  },
  {
    "placeId": "place-gurney-tyng-farm-quincy-massachusetts-usa",
    "placeName": "John Gurney's leased Tyng farm (later the Adams Old House), Braintree/Quincy, Massachusetts, USA",
    "longDescription": "In 1647 William Tyng leased John Gurney a 45-acre farm in Braintree (the Mount Wollaston / north-precinct area, now central Quincy) for ten years; Gurney continued leasing it from Tyng's daughters Bethia and Mercy until 1662. It is the holding in Tyng's 1653 probate inventory recorded as land 'in the possession of John Gurney' (45 acres per the NPS/Sargent reading, 48 acres per the NEHGR abstract). The northern portion of this 'Gurney farm' later became the Adams family seat: 'The Old House' (Peace field), first acquired by the Adams family in 1787, and the nearby Adams Birthplaces of John Adams and John Quincy Adams. Per the NPS Cultural Landscape Report (1997, citing the Ezekiel Sargent MSS). The same record stream notes the larger ~500-acre Tyng farm (Salter's Farm / Mount Wollaston) was leased to John Read then Gregory Belcher.",
    "siteName": "Adams Old House / 'the Gurney farm'",
    "streetAddress": "",
    "extantStatus": "site extant (Adams National Historical Park)",
    "extantStatusDescription": "The northern end of the leased farm is now within Adams National Historical Park, Quincy.",
    "coordinateBasis": "northern end of the 45-acre Gurney/Tyng farm (Adams Birthplaces / Old House vicinity), per the NPS CLR and the Sargent map; high precision per supplied coordinate",
    "imageUrl": "",
    "imageTitle": "Ezekiel Sargent, 'William Tyng's 45-acre farm, Braintree, 1649' (Quincy Historical Society)",
    "heritageUrl": "https://www.nps.gov/adam",
    "heritageLabel": "Adams National Historical Park",
    "reviewNotes": [
      "High precision: coordinate is the northern end of the leased farm (Adams property vicinity, central Quincy). The 45 vs 48 acre figure differs between the NPS/Sargent reading and the NEHGR abstract of the same 1653 inventory."
    ]
  },
  {
    "placeId": "place-gurney-monatiquot-freehold-braintree-massachusetts-usa",
    "placeName": "John Gurney's Monatiquot River freehold, Braintree, Massachusetts, USA",
    "longDescription": "A house, orchard, a five-acre parcel on the Monatiquot River ('at Monotecott'), and an adjoining half-acre that John Gurney owned outright in the Braintree middle precinct (now Braintree center/East Braintree) and sold to Richard Thayer, planter, for £14 on 12 February 1661/2 (possession given 16 April 1662). The five-acre parcel was bounded by the Monatiquot River on the south and the lands of Richard Thayer, Nathaniel Mott, and John Hodman (east), Symond Crosby (north), and George Oldredge (west). This freehold was distinct from, and several miles from, the Tyng leasehold up at Mount Wollaston.",
    "siteName": "Gurney house & orchard, Monatiquot",
    "streetAddress": "",
    "extantStatus": "unknown",
    "extantStatusDescription": "",
    "coordinateBasis": "north bank of the Monatiquot River in Braintree center/East Braintree, per the deed's 'at Monotecott' and the river as the parcel's south bound; parcel not surveyed",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "",
    "heritageLabel": "",
    "reviewNotes": [
      "Low precision: located to the Monatiquot River in Braintree (south bound = the river); the exact parcel is unsurveyed. Prior owner of the parcel is unrecorded (research lead L-189)."
    ]
  },
  {
    "placeId": "place-collegiale-saint-hildevert-gournay-en-bray-normandy-france",
    "placeName": "Collégiale Saint-Hildevert, Gournay-en-Bray, Normandy, France",
```

---

## Item 6 — `data/ancestors.json`: add the two new placeRefs to G13 (bidirectional link) — PROMOTE

`str_replace`:

`old_string`:
```
      "place-east-field-weymouth-massachusetts-usa",
      "place-mill-field-weymouth-massachusetts-usa"
    ]
  },
```
`new_string`:
```
      "place-east-field-weymouth-massachusetts-usa",
      "place-mill-field-weymouth-massachusetts-usa",
      "place-gurney-tyng-farm-quincy-massachusetts-usa",
      "place-gurney-monatiquot-freehold-braintree-massachusetts-usa"
    ]
  },
```

---

## Item 7 — Place files: update Weymouth fields; add two new place companions; two-way linkages — PROMOTE

**7a. `research/places/east-field-weymouth-ma.md`** — fix the generated registry date, record two parcels, add manuscript source. `str_replace`:

`old_string`:
```
- Short description: John Gurney Sr. land grant, 1651–52; parcel unlocated
```
`new_string`:
```
- Short description: John Gurney Sr. original grantee of two East Field lots, c. 1639–41 (reassigned by 1643); parcels unlocated
```

And `str_replace` (research-notes paragraph, to record both parcels at manuscript level):

`old_string`:
```
**What we know.** John Gurney Sr. held a two-acre grant "in the East field," recorded in Nash's **1643** property list under "the land of Robert Randoll" as a parcel "first granted to John Gurny" — so an original Gurney grant already passed to Randoll by 1643 — bounded east by the land of Edmond Hart and the highway, west by Robert Cooke, north by Nathaniel Adams (Nash, *Historical Sketch of Weymouth*, Appendix C, p. 258; a second East Field reference under Nathaniel Adams' land, p. 270, bounds another two-acre Gurney parcel by Jeffery Staple, Robert Randoll, a cedar swamp, and the highway).
```
`new_string`:
```
**What we know.** John Gurney Sr. was the original grantee of **two** separate two-acre lots in the East Field, both confirmed at manuscript level in the Weymouth Land Grants book (film 007009659): the first (ms p. 12, "John Gurny") by 1643 held by Robert Randoll, bounded east by Edmond Hart and the highway, west by Robert Cooke, north and south by Nathaniel Addames; the second (ms p. 23, "John Gurnie") held by Nathaniel Addames, bounded east by Jeffery Staple, west by Robert Randoll, north by a cedar swamp, south by the highway (Nash's printed transcription, *Historical Sketch of Weymouth*, Appendix C, pp. 258, 270, matches the manuscript). Both were "first granted/given to" John and reassigned by 1643.[^eastfield-msbook]
```

And append a footnote + linkage at the end of the file. `str_replace`:

`old_string`:
```
See the [John Gurney (G13) case file](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/john-gurney-case-file-v4.md) and verbatim extracts in [`nash-…-gurney-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md).
```
`new_string`:
```
See the [John Gurney (G13) companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g13-john-gurney-fact-sheet.research.md) and [case file](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/john-gurney-case-file-v4.md), the printed extracts in [`nash-…-gurney-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md), and the manuscript read in [`weymouth-land-grants-book-1643-gurney-manuscript-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md). Related places: [Mill Field](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/mill-field-weymouth-ma.md), [Great Lots east of Whitman's Pond](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/whitmans-pond-east-side-weymouth-ma.md).

[^eastfield-msbook]: Weymouth proprietors' Land Grants book (manuscript), FamilySearch film 007009659, images 00135 (ms p. 12) and 00140 (ms p. 23); extract at [`sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md). Printed transcription: Gilbert Nash, *Historical Sketch of the Town of Weymouth* (1885), Appendix C, pp. 258, 270. Source IDs: `weymouth-land-grants-book-ms`; `nash-historical-sketch-weymouth-1885`.
```

**7b. `research/places/mill-field-weymouth-ma.md`** — fix the generated registry date and add the manuscript link. `str_replace`:

`old_string`:
```
- Short description: John Gurney Sr. land grant, 1651–52; parcel unlocated
```
`new_string`:
```
- Short description: John Gurney Sr. original grantee of a 4-acre Mill Field lot, c. 1639–41 (reassigned by 1643); parcel unlocated
```

And `str_replace` the closing cross-reference line:

`old_string`:
```
See the [John Gurney (G13) case file](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/john-gurney-case-file-v4.md) and verbatim extracts in [`nash-…-gurney-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md).
```
`new_string`:
```
See the [John Gurney (G13) companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g13-john-gurney-fact-sheet.research.md), the printed extracts in [`nash-…-gurney-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/nash-historical-sketch-weymouth-1885-gurney-extracts.md), and the manuscript read in [`weymouth-land-grants-book-1643-gurney-manuscript-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/weymouth-land-grants-book-1643-gurney-manuscript-extracts.md) (film 007009659, ms p. 31; Source ID `weymouth-land-grants-book-ms`). Related place: [East Field](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/east-field-weymouth-ma.md).
```

**7c. New file — `research/places/gurney-tyng-farm-quincy-ma.md`:**
```
# John Gurney's leased Tyng farm (later the Adams Old House), Braintree/Quincy, Massachusetts, USA

<!-- GENERATED:PLACE-REGISTRY:START -->
## Place registry

- `placeId`: `place-gurney-tyng-farm-quincy-massachusetts-usa`
- Short description: 45-acre farm John Gurney leased from William Tyng 1647–1662; its northern part became the Adams family seat
- Place type: locality
- Aliases: William Tyng's 45-acre farm, Braintree; the Gurney farm, Braintree; Adams Old House / Peace field; Mount Wollaston, Braintree
- Coordinate: 42.239204, -71.003610 (high)
- Roles: landholding / property reference
- Site name: Adams Old House / "the Gurney farm"
- Detail: In 1647 William Tyng leased John Gurney (G13) a 45-acre Braintree farm for ten years; Gurney continued leasing it from Tyng's daughters Bethia and Mercy until 1662. The northern portion later became the Adams family seat.

### Linked ancestors

- G13 John Gurney - landholding / property reference

### Review notes

- High precision: coordinate is the northern end of the leased farm (Adams Birthplaces / Old House vicinity, central Quincy).
<!-- GENERATED:PLACE-REGISTRY:END -->

## Research notes

**John Gurney worked this land ~130 years before it became the home of presidents.** In **1647 William Tyng leased John Gurney a 45-acre farm** in Braintree (the Mount Wollaston / north-precinct area, now central Quincy) **for ten years**; Gurney went on leasing it from Tyng's daughters **Bethia and Mercy until 1662**. This is the holding in William Tyng's 1653 probate inventory recorded as land "in the possession of John Gurney" — **45 acres** by the National Park Service / Ezekiel Sargent reading, **48 acres** in the *NEHGR* abstract of the same inventory (a transcription discrepancy to settle against the inventory image). It is one continuous tenancy ~1647–1662 (the original ten-year term from William Tyng, then renewed from his daughters), the same property documented in the 1653 inventory and the 28 March 1661 Tyng estate-division indenture.[^tyngfarm-clr][^tyngfarm-nehgr]

**The northern portion of "the Gurney farm" became the Adams seat.** Per the Ezekiel Sargent manuscripts and the NPS *Cultural Landscape Report*, the northern part of the parcel was later the site of the Adams property — "The Old House" (Peace field), first acquired by the Adams family in 1787, and the nearby Adams Birthplaces of **John Adams** (2nd U.S. president) and **John Quincy Adams** (6th). The Sargent map of 1649 labels the parcel "William Tyng / John Gurney (Lease) / Gregory Belcher," with Salter's Farm to the northeast, Stoney Field southwest, Edmund Quincy southeast, Crosby north, and "the Plain Land" south, along Adams Street.[^tyngfarm-clr]

The separate, larger ~500-acre Tyng farm (Salter's Farm / Mount Wollaston, leased to John Read 1639–49 and Gregory Belcher from 1657–8) is a different property; see the [John Gurney (G13) companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g13-john-gurney-fact-sheet.research.md) and [Braintree](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/braintree-ma.md). John's own freehold was elsewhere, on the [Monatiquot River](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/gurney-monatiquot-freehold-braintree-ma.md).

[^tyngfarm-clr]: National Park Service, *Cultural Landscape Report, Adams National Historic Site* (1997), pp. 12–13 (Site Chronology) and Figure 1, "William Tyng's 45-acre farm, Braintree, Massachusetts, 1649," citing the Ezekiel Sargent manuscripts (Quincy Historical Society, "Land Formerly of William Tyng"); [npshistory.com/publications/adam/clr-1997.pdf](https://npshistory.com/publications/adam/clr-1997.pdf); extract at [`sources/corpus_supplement/nps-adams-clr-1997-gurney-tyng-extracts.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/nps-adams-clr-1997-gurney-tyng-extracts.md). Source ID: `nps-adams-nhp`.
[^tyngfarm-nehgr]: Capt. William Tyng inventory abstract, *New England Historical and Genealogical Register*, vol. 30 (1876), p. 432; *Suffolk Deeds, Liber IV* (1888), pp. 6, 89a–90 (the 28 March 1661 estate-division recital, the messuage "in the Occupation and by lease in the hands of John Gurney"). Source IDs: `nehgr-30-432`; `suffolk-deeds-liber-iv-1888`.
```

**7d. New file — `research/places/gurney-monatiquot-freehold-braintree-ma.md`:**
```
# John Gurney's Monatiquot River freehold, Braintree, Massachusetts, USA

<!-- GENERATED:PLACE-REGISTRY:START -->
## Place registry

- `placeId`: `place-gurney-monatiquot-freehold-braintree-massachusetts-usa`
- Short description: House, orchard, and ~5.5 acres on the Monatiquot River that John Gurney owned and sold to Richard Thayer, 1661/2
- Place type: locality
- Aliases: Gurney house and orchard, Monatiquot; Monotecott, Braintree
- Coordinate: 42.210, -70.992 (low)
- Roles: landholding / property reference
- Site name: Gurney house & orchard, Monatiquot
- Detail: The freehold John Gurney owned in Braintree center (the middle precinct), on the Monatiquot River, sold to Richard Thayer in 1661/2 — distinct from his Tyng leasehold up at Mount Wollaston.

### Linked ancestors

- G13 John Gurney - landholding / property reference

### Review notes

- Low precision: located to the Monatiquot River in Braintree (south bound = the river); exact parcel unsurveyed.
<!-- GENERATED:PLACE-REGISTRY:END -->

## Research notes

John Gurney owned a freehold in the Braintree middle precinct (now Braintree center/East Braintree): a house, orchard, a **five-acre parcel on the Monatiquot River** ("at Monotecott"), and an adjoining half-acre. He sold it to **Richard Thayer**, planter, for **£14** on 12 February 1661/2, giving possession "by turffe & Twigg" on 16 April 1662; he signed by mark, witnessed by Peter Brackett and John Rockwell. The five-acre parcel was bounded by the Monatiquot River (south) and the lands of Richard Thayer, Nathaniel Mott, and John Hodman (east), Symond Crosby (north), and George Oldredge (west) — Thayer was assembling a contiguous riverside holding. No record names who held the parcel before John.[^monatiquot-deed]

This freehold was several miles from, and a different precinct than, John's leased [Tyng farm at Mount Wollaston](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/gurney-tyng-farm-quincy-ma.md). See the [John Gurney (G13) companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g13-john-gurney-fact-sheet.research.md) and [Braintree](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/braintree-ma.md).

[^monatiquot-deed]: *Suffolk Deeds, Liber V* (registry transcription), pp. 457–459, John Gurney of Braintree, tailor, to Richard Thayer, sealed 12 February 1661/2, recorded 12 June 1668; Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.* (1898), p. 10; full transcript at [`sources/corpus_supplement/suffolk-deeds-lib5-457-459-john-gurney-thayer-deed.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/suffolk-deeds-lib5-457-459-john-gurney-thayer-deed.md). Source IDs: `bates-ancient-iron-works-braintree-1898`; `familysearch-fulltext-search`.
```

**7e. `research/places/braintree-ma.md`** — the "John Gurney's two Braintree properties" research note was added directly during the thread; link the two new place files into it. `str_replace`:

`old_string`:
```
**The Tyng leasehold (north precinct, now central Quincy).** In **1647 William Tyng leased John Gurney a 45-acre farm for ten years**;
```
`new_string`:
```
**The Tyng leasehold (north precinct, now central Quincy)** — full place record at [`gurney-tyng-farm-quincy-ma.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/gurney-tyng-farm-quincy-ma.md). In **1647 William Tyng leased John Gurney a 45-acre farm for ten years**;
```

And `str_replace`:

`old_string`:
```
**The Monatiquot freehold (middle precinct, now Braintree center).** A house, orchard, a five-acre parcel on the **Monatiquot River**,
```
`new_string`:
```
**The Monatiquot freehold (middle precinct, now Braintree center)** — full place record at [`gurney-monatiquot-freehold-braintree-ma.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/places/gurney-monatiquot-freehold-braintree-ma.md). A house, orchard, a five-acre parcel on the **Monatiquot River**,
```

---

## Item 8 — Regenerate ID indexes — PROMOTE

After the JSON edits, Phase 2 runs `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write` to refresh `data/indexes/place-ids.csv`, `all-ids.csv`, and `source-ids.csv` (do not hand-edit). Then `npm run validate` (or the site validator) to confirm no place↔ancestor link drift and no dangling refs.

---

## Source tracking

| sourceId | action | validation |
|---|---|---|
| `weymouth-land-grants-book-ms` | new (Item 1) | new `sources/validations/weymouth-land-grants-book-ms.md` |
| `nps-adams-nhp` | update — url, edition (1997), corpus, media, notes (Item 2) | new `sources/validations/nps-adams-nhp.md` |
| `nash-historical-sketch-weymouth-1885`, `history-of-weymouth`, `nehgr-30-432`, `suffolk-deeds-liber-iv-1888`, `bates-ancient-iron-works-braintree-1898`, `familysearch-fulltext-search` | cited only; already registered | existing |

New corpus_supplement files: `nps-adams-clr-1997-gurney-tyng-extracts.md` (Item 2b). Existing-in-tree, now registered: `weymouth-land-grants-book-1643-gurney-manuscript-extracts.md`.

## Leads (already updated live in the thread; recorded here for traceability)

- **L-182** — Weymouth grants: matured (manuscript read complete; three parcels / ~8 acres).
- **L-144** — Tyng leasehold origin: near-resolved (1647 lease, ten-year term, continued from Bethia & Mercy to 1662; located at the Adams Old House/birthplace area). Residual: 45 vs 48 acre figure (inventory image); the primary 1647 lease deed.
- **L-192** — locate the leasehold + pin the NPS CLR: resolved (1997 CLR pp.12-13 + Fig.1; coordinate 42.239204,-71.003610). Residual: `nps-adams-nhp` url/edition (done in Item 2a); the 1669 Leventhal plat is the other (Shepard) Mount Wollaston farm.
- **L-193** — survey pre-1650 Boston / "Boston-related" / Mass Bay record collections for Gurney variants (Boston Town Records 1634–1660 + Book of Possessions = done-negative).
