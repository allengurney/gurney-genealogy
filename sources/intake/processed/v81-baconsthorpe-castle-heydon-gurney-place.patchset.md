# v81 - Baconsthorpe Castle / Heydon-Gurney place context

**Status:** Phase 1 patchset prepared 2026-06-01 PT.

## Scope

Promote Baconsthorpe Castle as a precise place record and research place note, using official English Heritage and Historic England pages. Add the castle as the physical Heydon family seat behind the G20-G19-G18 Gurney-Heydon alliance:

- G20 Thomas Gournay II named John Heydon of Baconsthorpe as supervisor of his 1471 will.
- G19 William Gurney IV was backed in 1472 by Henry Heydon's men-at-arms during the Saxthorpe Court dispute.
- G18 William Gurney V married Henry Heydon's daughter Anne Heydon shortly after 28 May 1484.
- Baconsthorpe's later Tudor wool operation gives a strong in-law/contextual parallel to the Gurney wool economy already documented in G20 Margaret's cloth bequest and G19 William IV's 700-sheep will clause.

## Source sweep

Outcome: **promote**.

Existing repo content already mentions Baconsthorpe Castle in G18, G19, G20, and the Baconsthorpe quarter topic, but no standalone place record or place research page exists for the castle. No existing `data/sources.json` entries were found for the English Heritage Baconsthorpe Castle pages or Historic England List Entry 1013093.

Official sources used:

- English Heritage, "History of Baconsthorpe Castle": Heydon family residence; site acquired from the Bacon family; castle built as main residence c.1450; John Heydon d.1479 began the inner gatehouse; Sir Henry Heydon d.1504 completed and extended it; wool industry and later demolition context.
- English Heritage, "The Rise and Fall of a Tudor Wool Factory": Heydon wool economy; Tudor sheep pastures; mid-16th-century wool-processing range; 20,000-30,000 sheep estimate; cloth sold in England and the Netherlands.
- Historic England, National Heritage List for England, List Entry 1013093: Scheduled Monument; National Grid Reference TG 12157 38117; site c.750m north of Baconsthorpe village; moated fortified house, remains, outer gatehouse, courtyards, mere, formal-garden earthworks; built on the earlier Wood Hall site acquired from the Bacon family by William Heydon in the earlier 15th century.

Coordinate for `data/places.json`: Historic England supplies National Grid Reference **TG 12157 38117**. Converted to WGS84 for the repo latitude/longitude fields: **52.8985961, 1.152825**. The place detail record preserves the NGR in `coordinateBasis`.

## Source tracking

Add three new source IDs:

- `english-heritage-baconsthorpe-castle-history`
- `english-heritage-baconsthorpe-castle-wool-factory`
- `historic-england-baconsthorpe-castle-1013093`

Each gets a validation file. Each gets a short `sources/corpus_supplement/` note preserving key source facts without creating a full copyrighted web-page copy.

## Phase 2 operations

### 1. Add `data/sources.json` entries

File: `data/sources.json`

Operation: `str_replace`

`old_string`:

```json
    "historic-england-old-hall-farmhouse-1077566": {
      "shortTitle": "Historic England - Old Hall Farmhouse (1077566)",
      "citation": "Historic England. \"Old Hall Farmhouse.\" National Heritage List for England, List Entry Number 1077566.",
      "archive": "Historic England, National Heritage List for England",
      "url": "https://historicengland.org.uk/listing/the-list/list-entry/1077566",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/historic-england-old-hall-farmhouse-1077566.md",
      "mediaPath": null,
      "validationPath": "sources/validations/historic-england-old-hall-farmhouse-1077566.md",
      "notes": "Grade II listing for Old Hall Farmhouse, Great Ellingham. Historic England describes the house as c.1570, timber framed with wattle and daub and some clay lump infill on a brick plinth, cross-wing plan, two storeys, central range flanked by gabled cross wings, and with original staircase surviving to attic. First listed 21 July 1951; most recent amendment 16 November 1983; NGR TM 01591 96491. Supports the extant-house component of the Great Ellingham current-site status."
    },
    "nher-great-ellingham-parish-summary": {
```

`new_string`:

```json
    "historic-england-old-hall-farmhouse-1077566": {
      "shortTitle": "Historic England - Old Hall Farmhouse (1077566)",
      "citation": "Historic England. \"Old Hall Farmhouse.\" National Heritage List for England, List Entry Number 1077566.",
      "archive": "Historic England, National Heritage List for England",
      "url": "https://historicengland.org.uk/listing/the-list/list-entry/1077566",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/historic-england-old-hall-farmhouse-1077566.md",
      "mediaPath": null,
      "validationPath": "sources/validations/historic-england-old-hall-farmhouse-1077566.md",
      "notes": "Grade II listing for Old Hall Farmhouse, Great Ellingham. Historic England describes the house as c.1570, timber framed with wattle and daub and some clay lump infill on a brick plinth, cross-wing plan, two storeys, central range flanked by gabled cross wings, and with original staircase surviving to attic. First listed 21 July 1951; most recent amendment 16 November 1983; NGR TM 01591 96491. Supports the extant-house component of the Great Ellingham current-site status."
    },
    "english-heritage-baconsthorpe-castle-history": {
      "shortTitle": "English Heritage - Baconsthorpe Castle history",
      "citation": "English Heritage. \"History of Baconsthorpe Castle.\" English Heritage.",
      "archive": "English Heritage site history",
      "url": "https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/english-heritage-baconsthorpe-castle-history.md",
      "mediaPath": null,
      "validationPath": "sources/validations/english-heritage-baconsthorpe-castle-history.md",
      "notes": "Official English Heritage history page for Baconsthorpe Castle. Supports the Heydon residence chronology: Baconsthorpe acquired from the Bacon family by William Baxter/Heydon in the early 15th century; John Heydon d.1479 began the earliest castle building; Sir Henry Heydon d.1504 completed and extended the castle; the castle was the Heydons' main residence from about 1450; later wool wealth and debt led to partial demolition in 1650."
    },
    "english-heritage-baconsthorpe-castle-wool-factory": {
      "shortTitle": "English Heritage - Baconsthorpe Tudor wool factory",
      "citation": "English Heritage. \"The Rise and Fall of a Tudor Wool Factory.\" English Heritage.",
      "archive": "English Heritage site history",
      "url": "https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/tudor-wool-factory/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/english-heritage-baconsthorpe-castle-wool-factory.md",
      "mediaPath": null,
      "validationPath": "sources/validations/english-heritage-baconsthorpe-castle-wool-factory.md",
      "notes": "Official English Heritage article on the Heydon family's Tudor wool economy at Baconsthorpe Castle. Supports contextual comparison with the Gurney wool economy: pasture surrounding the castle, major sheep flocks, mid-16th-century wool processing range, cloth sold in England and the Netherlands, and later debt-driven decline."
    },
    "historic-england-baconsthorpe-castle-1013093": {
      "shortTitle": "Historic England - Baconsthorpe Castle (1013093)",
      "citation": "Historic England. \"Baconsthorpe Castle moated site with fortified house, gatehouse, courtyards and formal gardens.\" National Heritage List for England, List Entry Number 1013093.",
      "archive": "Historic England, National Heritage List for England",
      "url": "https://historicengland.org.uk/listing/the-list/list-entry/1013093",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/historic-england-baconsthorpe-castle-1013093.md",
      "mediaPath": null,
      "validationPath": "sources/validations/historic-england-baconsthorpe-castle-1013093.md",
      "notes": "Official Historic England scheduled-monument entry for Baconsthorpe Castle. Supports precise current-site status and coordinates: Scheduled Monument, List Entry 1013093, first listed 4 Dec. 1924, amended 27 Sept. 1995, NGR TG 12157 38117. Describes the moated fortified house, remains, outer gatehouse, courtyards, mere, formal garden earthworks, and Wood Hall / Heydon acquisition context."
    },
    "nher-great-ellingham-parish-summary": {
```

### 2. Add `data/places.json` record

File: `data/places.json`

Operation: `str_replace`

`old_string`:

```json
  {
    "placeId": "place-attleborough-norfolk-england",
    "name": "Attleborough, Norfolk, England",
    "aliases": [
      "Attleborough, Norfolk"
    ],
    "shortDescription": "Advowson locality",
    "placeType": "locality",
    "coordinate": {
      "lat": 52.517,
      "lng": 1.015
    },
    "coordinatePrecision": "high",
    "roles": [
      "landholding / property reference"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g15-henry-gurney",
        "role": "landholding / property reference"
      }
    ],
    "filename": "attleborough.md"
  },
  {
    "placeId": "place-bedfordshire-england",
```

`new_string`:

```json
  {
    "placeId": "place-attleborough-norfolk-england",
    "name": "Attleborough, Norfolk, England",
    "aliases": [
      "Attleborough, Norfolk"
    ],
    "shortDescription": "Advowson locality",
    "placeType": "locality",
    "coordinate": {
      "lat": 52.517,
      "lng": 1.015
    },
    "coordinatePrecision": "high",
    "roles": [
      "landholding / property reference"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g15-henry-gurney",
        "role": "landholding / property reference"
      }
    ],
    "filename": "attleborough.md"
  },
  {
    "placeId": "place-baconsthorpe-castle-norfolk-england",
    "name": "Baconsthorpe Castle, Baconsthorpe, Norfolk, England",
    "aliases": [
      "Baconsthorpe Castle",
      "Baconsthorpe Hall",
      "Wood Hall, Baconsthorpe",
      "Baconsthorpe Castle moated site with fortified house, gatehouse, courtyards and formal gardens"
    ],
    "shortDescription": "Heydon family fortified manor house and Gurney in-law site",
    "placeType": "historic site",
    "coordinate": {
      "lat": 52.8985961,
      "lng": 1.152825
    },
    "coordinatePrecision": "high",
    "roles": [
      "spouse family seat",
      "in-law alliance context",
      "wool economy context",
      "heritage site"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g18-william-gurney-v",
        "role": "spouse family seat"
      },
      {
        "recordId": "ancestor-g19-william-gurney-iv",
        "role": "in-law alliance context"
      },
      {
        "recordId": "ancestor-g20-thomas-gournay-ii",
        "role": "in-law alliance context"
      }
    ],
    "filename": "baconsthorpe-castle.md"
  },
  {
    "placeId": "place-bedfordshire-england",
```

### 3. Add `data/places_detail.json` record

File: `data/places_detail.json`

Operation: `str_replace`

`old_string`:

```json
  {
    "placeId": "place-attleborough-norfolk-england",
    "placeName": "Attleborough, Norfolk, England",
    "longDescription": "Attleborough church-advowson context associated with Henry Gurnay.",
    "siteName": "",
    "streetAddress": "",
    "extantStatus": "unknown",
    "extantStatusDescription": "",
    "coordinateBasis": "town centroid",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "",
    "heritageLabel": "",
    "reviewNotes": []
  },
  {
    "placeId": "place-bedfordshire-england",
```

`new_string`:

```json
  {
    "placeId": "place-attleborough-norfolk-england",
    "placeName": "Attleborough, Norfolk, England",
    "longDescription": "Attleborough church-advowson context associated with Henry Gurnay.",
    "siteName": "",
    "streetAddress": "",
    "extantStatus": "unknown",
    "extantStatusDescription": "",
    "coordinateBasis": "town centroid",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "",
    "heritageLabel": "",
    "reviewNotes": []
  },
  {
    "placeId": "place-baconsthorpe-castle-norfolk-england",
    "placeName": "Baconsthorpe Castle, Baconsthorpe, Norfolk, England",
    "longDescription": "Baconsthorpe Castle is the moated fortified manor house that became the Heydon family's principal seat from about 1450. It matters to the direct Gurney line through the Gurney-Heydon alliance: Thomas Gournay II named John Heydon of Baconsthorpe supervisor of his 1471 will; Henry Heydon backed William Gurney IV during the 1472 Saxthorpe dispute; and William Gurney V married Henry's daughter Anne Heydon shortly after 28 May 1484. English Heritage and Historic England also make it a useful place-context anchor for East Anglia's wool economy.",
    "siteName": "Baconsthorpe Castle",
    "streetAddress": "",
    "extantStatus": "ruins and earthworks extant",
    "extantStatusDescription": "Historic England lists the site as a Scheduled Monument, with standing remains, buried remains, the moated fortified-house platform, outer gatehouse, courtyards, mere, and formal-garden earthworks. English Heritage manages the castle as extensive ruins. Much of the principal residence was demolished in the mid-17th century, but the outer gatehouse survived as Baconsthorpe Hall until 1920.",
    "coordinateBasis": "Historic England National Grid Reference TG 12157 38117, converted to WGS84 for latitude/longitude fields",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/",
    "heritageLabel": "English Heritage: Baconsthorpe Castle history",
    "reviewNotes": [
      "Keep the later Heydon-led Baconsthorpe Castle context distinct from the earlier Bacon/Baconsthorpe family question around G26 Katherine Baconsthorpe.",
      "Do not state that any named Gurney visit to Baconsthorpe Castle is directly recorded. Treat likely visits by William Gurney IV or William Gurney V as inference from the documented 1471-1484 alliance and marriage.",
      "Source IDs: english-heritage-baconsthorpe-castle-history, english-heritage-baconsthorpe-castle-wool-factory, historic-england-baconsthorpe-castle-1013093."
    ]
  },
  {
    "placeId": "place-bedfordshire-england",
```

### 4. Update `data/ancestors.json` place references

#### 4a. Add Baconsthorpe Castle to G18 placeRefs

File: `data/ancestors.json`

Operation: `str_replace`

`old_string`:

```json
    "placeRefs": [
      "place-hardingham-norfolk-england",
      "place-hingham-norfolk-england",
      "place-irstead-norfolk-england",
      "place-west-barsham-norfolk-england",
      "place-harpley-norfolk-england"
    ]
```

`new_string`:

```json
    "placeRefs": [
      "place-baconsthorpe-castle-norfolk-england",
      "place-hardingham-norfolk-england",
      "place-hingham-norfolk-england",
      "place-irstead-norfolk-england",
      "place-west-barsham-norfolk-england",
      "place-harpley-norfolk-england"
    ]
```

#### 4b. Add Baconsthorpe Castle to G19 placeRefs

File: `data/ancestors.json`

Operation: `str_replace`

`old_string`:

```json
    "placeRefs": [
      "place-burnham-thorpe-norfolk-england",
      "place-west-barsham-norfolk-england"
    ]
  },
  {
    "type": "ancestor",
    "gen": "G20",
```

`new_string`:

```json
    "placeRefs": [
      "place-baconsthorpe-castle-norfolk-england",
      "place-burnham-thorpe-norfolk-england",
      "place-west-barsham-norfolk-england"
    ]
  },
  {
    "type": "ancestor",
    "gen": "G20",
```

#### 4c. Add Baconsthorpe Castle to G20 placeRefs

File: `data/ancestors.json`

Operation: `str_replace`

`old_string`:

```json
    "placeRefs": [
      "place-harpley-norfolk-england",
      "place-west-barsham-norfolk-england"
    ]
  },
  {
    "type": "ancestor",
    "gen": "G21",
```

`new_string`:

```json
    "placeRefs": [
      "place-baconsthorpe-castle-norfolk-england",
      "place-harpley-norfolk-england",
      "place-west-barsham-norfolk-england"
    ]
  },
  {
    "type": "ancestor",
    "gen": "G21",
```

### 5. Write source corpus supplement files

#### 5a. New file: `sources/corpus_supplement/english-heritage-baconsthorpe-castle-history.md`

```markdown
# English Heritage - History of Baconsthorpe Castle

**Source ID:** `english-heritage-baconsthorpe-castle-history`

**Citation:** English Heritage, "History of Baconsthorpe Castle," English Heritage.

**URL:** https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/

## Record summary

- Baconsthorpe Castle is presented by English Heritage as the principal residence associated with the Heydon family's rise and fall.
- The site was acquired from the Bacon family in the early 15th century by William Baxter.
- William's son John, who later used the Heydon name and died in 1479, began the earliest castle building.
- Sir Henry Heydon, who died in 1504, completed and extended the castle.
- English Heritage dates the castle's role as the Heydons' main residence to about 1450.
- The page connects the family's later wealth to the wool industry and the later debt crisis to the demolition of much of the castle in 1650.

## Research value

This page supplies the castle-level context behind the direct-line Gurney-Heydon connection. Thomas Gournay II (G20) named John Heydon of Baconsthorpe supervisor of his 1471 will; Henry Heydon backed William Gurney IV (G19) in the 1472 Saxthorpe dispute; and Henry's daughter Anne Heydon married William Gurney V (G18) shortly after 28 May 1484. The source supports Baconsthorpe Castle as the physical Heydon seat behind that alliance, while not directly proving a named Gurney visit.
```

#### 5b. New file: `sources/corpus_supplement/english-heritage-baconsthorpe-castle-wool-factory.md`

```markdown
# English Heritage - The Rise and Fall of a Tudor Wool Factory

**Source ID:** `english-heritage-baconsthorpe-castle-wool-factory`

**Citation:** English Heritage, "The Rise and Fall of a Tudor Wool Factory," English Heritage.

**URL:** https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/tudor-wool-factory/

## Record summary

- English Heritage identifies the Tudor-period landscape around Baconsthorpe Castle as pasture supporting major Heydon sheep flocks.
- The article treats the wool trade as the basis of much of East Anglia's wealth and presents the Heydons as major participants.
- Sir John Heydon II, c.1470-1550, transformed the castle's east range into a wool-processing work space.
- English Heritage states that the cloth made at Baconsthorpe was sold both domestically and in the Netherlands.
- The article gives Sir Christopher Heydon I's Christmas entertainment of 30 head shepherds as evidence for very large Heydon flocks, estimated at 20,000 to 30,000 sheep.
- The article treats debt and extravagant living, rather than absence of wool wealth, as the cause of the later Heydon collapse.

## Research value

This page is a contextual comparator for the direct-line Gurney wool economy. William Gurney IV's 1507 will required 700 sheep to remain at West Barsham, and Thomas Gournay II's 1471 will preserved a household textile bequest to Margaret Jerningham. Baconsthorpe should be described as an in-law wool-economy parallel, not as proof that the Gurneys and Heydons operated a shared wool business.
```

#### 5c. New file: `sources/corpus_supplement/historic-england-baconsthorpe-castle-1013093.md`

```markdown
# Historic England - Baconsthorpe Castle (List Entry 1013093)

**Source ID:** `historic-england-baconsthorpe-castle-1013093`

**Citation:** Historic England, "Baconsthorpe Castle moated site with fortified house, gatehouse, courtyards and formal gardens," *National Heritage List for England*, List Entry Number 1013093.

**URL:** https://historicengland.org.uk/listing/the-list/list-entry/1013093

## Record summary

- List Entry Name: Baconsthorpe Castle moated site with fortified house, gatehouse, courtyards and formal gardens.
- List Entry Number: 1013093.
- Heritage Category: Scheduled Monument.
- Date first listed: 4 December 1924.
- Date of most recent amendment: 27 September 1995.
- County: Norfolk.
- District: North Norfolk.
- Parish: Baconsthorpe.
- National Grid Reference: TG 12157 38117.

## Description extract / paraphrase

Historic England places the site about 750 metres north of Baconsthorpe village. The protected monument includes the moated fortified house site, standing and buried remains, the outer gatehouse, courtyards, a mere, and formal-garden earthworks.

The entry describes Baconsthorpe Castle as a late medieval fortified house built on what is thought to be the earlier Wood Hall manor site. That earlier site was acquired from the Bacon family by William Heydon in the earlier 15th century. John Heydon I and Sir Henry Heydon built the main part of the house during the middle and later 15th century.

The entry also records that Baconsthorpe and surrounding manors were later farmed as a large sheep run; most buildings on the moated site were demolished in the mid-17th century; and the outer gatehouse was converted for use as Baconsthorpe Hall until about 1920.

## Research value

This listing supplies the structured-data anchor for Baconsthorpe Castle: official protected status, NGR, current extant ruins and earthworks, and a concise architectural/site-history frame. It also helps keep the later Heydon castle context distinct from the earlier Bacon/Baconsthorpe family question around Katherine Baconsthorpe in the G26 line.
```

### 6. Write validation files

#### 6a. New file: `sources/validations/english-heritage-baconsthorpe-castle-history.md`

```markdown
# Source validation: English Heritage - Baconsthorpe Castle history

**Source ID:** `english-heritage-baconsthorpe-castle-history`

**Source examined:** English Heritage, "History of Baconsthorpe Castle."

**Finding destination:** `research/places/baconsthorpe-castle.md`; `data/places.json`; `data/places_detail.json`; `fact-sheets/g19-william-gurney-iv-fact-sheet.md`; `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`.

## Validation result

Strong contextual source. English Heritage is the managing public heritage body for the castle and provides a suitable official public-history source for the Heydon residence chronology.

## Supports

- Baconsthorpe Castle as the Heydon family's principal residence from about 1450.
- Site acquired from the Bacon family in the early 15th century by William Baxter/Heydon.
- John Heydon d.1479 began the earliest castle building.
- Sir Henry Heydon d.1504 completed and extended the castle.
- Wool industry and later debt/demolition context.

## Limits

This source does not directly name any Gurney visitor at Baconsthorpe Castle. Use it for place context and the Heydon chronology; cite Daniel Gurney, Blomefield, and the Paston Letters for the Gurney-Heydon relationship itself.
```

#### 6b. New file: `sources/validations/english-heritage-baconsthorpe-castle-wool-factory.md`

```markdown
# Source validation: English Heritage - Baconsthorpe Tudor wool factory

**Source ID:** `english-heritage-baconsthorpe-castle-wool-factory`

**Source examined:** English Heritage, "The Rise and Fall of a Tudor Wool Factory."

**Finding destination:** `research/places/baconsthorpe-castle.md`; `fact-sheets/g19-william-gurney-iv-fact-sheet.md`; `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`.

## Validation result

Strong contextual source for the Heydon wool economy at Baconsthorpe Castle.

## Supports

- Tudor-period Baconsthorpe as a large pastoral and wool-processing estate.
- Sir John Heydon II's conversion of the east range into a wool-processing work space.
- English and Netherlands market context for Baconsthorpe cloth.
- Sir Christopher Heydon I's 30 head-shepherd Christmas dinner and the associated 20,000-30,000 sheep estimate.

## Limits

This source supports a wool-economy parallel between the Heydons and Gurneys. It does not prove a shared Gurney-Heydon wool enterprise. Keep the Gurney-side facts tied to Daniel Gurney's *Record* and the relevant G19/G20 wills.
```

#### 6c. New file: `sources/validations/historic-england-baconsthorpe-castle-1013093.md`

```markdown
# Source validation: Historic England - Baconsthorpe Castle (1013093)

**Source ID:** `historic-england-baconsthorpe-castle-1013093`

**Source examined:** Historic England, National Heritage List for England, List Entry Number 1013093.

**Finding destination:** `research/places/baconsthorpe-castle.md`; `data/places.json`; `data/places_detail.json`.

## Validation result

Strong source. Historic England is the official National Heritage List source for the scheduled monument designation and location.

## Supports

- Baconsthorpe Castle is a Scheduled Monument, List Entry 1013093.
- National Grid Reference TG 12157 38117.
- County Norfolk, District North Norfolk, Parish Baconsthorpe.
- Current extant status: standing remains, buried remains, moated fortified-house site, outer gatehouse, courtyards, mere, and formal-garden earthworks.
- Wood Hall / Bacon family / Heydon acquisition context.

## Limits

This source supports the site, designation, coordinates, and architectural description. It does not by itself support the Gurney-Heydon relationship; use the person/family sources for those claims.
```

### 7. Write place research file

New file: `research/places/baconsthorpe-castle.md`

```markdown
# Baconsthorpe Castle, Norfolk

Baconsthorpe Castle is the physical Heydon seat behind the late-15th-century Gurney-Heydon alliance. English Heritage describes the castle as the Heydons' main residence from about 1450: John Heydon, who died in 1479, began the earliest castle building, and his son Sir Henry Heydon, who died in 1504, completed and extended it.[^eh-baconsthorpe-history]

The direct Gurney line intersects the place in three linked steps. Thomas Gournay II (G20) named John Heydon of Baconsthorpe supervisor of his 1471 will. Within a year, Henry Heydon was ready with men-at-arms to support William Gurney IV (G19) during the Saxthorpe Court dispute. In 1484, the alliance became a marriage connection when Henry Heydon arranged the marriage of his daughter Anne Heydon to William Gurney V (G18). No surviving source examined here records a named Gurney visit to Baconsthorpe Castle, but the documented 1471-1484 legal, military, and marriage sequence makes visits by William IV and William V a reasonable inference rather than a proved event.[^gurney-heydon-sequence]

Anne Heydon is the direct-line wife most closely tied to the place. She was Sir Henry Heydon's daughter; Baconsthorpe was her father's principal family seat; and the castle was active as a high-status Heydon residence before her marriage to William Gurney V. It is therefore likely that Anne grew up with Baconsthorpe as part of her household world, although the surviving sources should not be made to say that she was born there or that she resided there continuously.[^eh-baconsthorpe-history][^g18-anne-heydon]

The wool economy gives Baconsthorpe another useful Gurney-facing context. English Heritage presents the Tudor Heydons as major East Anglian wool producers: by the mid-16th century the castle lay at the centre of a large pastoral and wool-processing estate, with an east range adapted for wool work and cloth sold in England and the Netherlands. This should be compared to, not merged with, the Gurney evidence: Thomas Gournay II's 1471 will left Margaret Jerningham the household's woollen and linen cloths as her work and that of her servants, and William Gurney IV's 1507 will required 700 sheep to remain at West Barsham. Together the records show two allied north-Norfolk gentry houses participating in the same broader wool landscape, not a documented joint enterprise.[^eh-baconsthorpe-wool][^gurney-wool-economy]

Historic England supplies the current-site anchor. Baconsthorpe Castle is a Scheduled Monument, List Entry 1013093, at National Grid Reference TG 12157 38117. The protected site includes the moated fortified-house remains, outer gatehouse, courtyards, mere, and formal-garden earthworks. Much of the principal residence was demolished in the mid-17th century, but ruins and earthworks remain extant.[^he-baconsthorpe-1013093]

Keep this place distinct from the earlier Bacon/Baconsthorpe family question. The castle site was acquired from the Bacon family in the early 15th century and became a Heydon seat. That is later than the probable G26 marriage of Sir William de Gournay III to Katherine Bacon/Baconsthorpe, daughter of Edmund Baconsthorpe, and should not be used as proof for or against that earlier marriage.[^baconsthorpe-quarter]

[^eh-baconsthorpe-history]: English Heritage, ["History of Baconsthorpe Castle"](https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/), English Heritage. Source ID: `english-heritage-baconsthorpe-castle-history`.

[^gurney-heydon-sequence]: 1471 supervisor: Francis Blomefield, *History of Norfolk*, vol. vii, "West-Barsham," pp. 42-47, [British History Online](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47), Source ID: `blomefield-norfolk`. 1472 Saxthorpe Court: James Gairdner, ed., *The Paston Letters* (1904), Introduction vol. I, Source ID: `paston-letters-gairdner`. 1484 marriage indentures and 1485 trust deed: Daniel Gurney, *Supplement to the Record of the House of Gournay* (King's Lynn: Thew & Son, 1858), Note 132, pp. 817-819, Source ID: `dg-rec-supp`.

[^g18-anne-heydon]: Daniel Gurney, *Record of the House of Gournay* (1848), pedigree p. 287; Daniel Gurney, *Supplement* (1858), Notes 132-133, pp. 817-822; and the existing G18 fact sheet treatment of Anne Heydon's parentage and marriage sequence.

[^eh-baconsthorpe-wool]: English Heritage, ["The Rise and Fall of a Tudor Wool Factory"](https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/tudor-wool-factory/), English Heritage. Source ID: `english-heritage-baconsthorpe-castle-wool-factory`.

[^gurney-wool-economy]: Daniel Gurney, *Record of the House of Gournay* (1848), p. 282, on Thomas II's textile bequest to Margaret, William IV's 700 sheep at West Barsham, and the wider Norfolk wool economy. Source ID: `dg-rec-pt2`.

[^he-baconsthorpe-1013093]: Historic England, ["Baconsthorpe Castle moated site with fortified house, gatehouse, courtyards and formal gardens"](https://historicengland.org.uk/listing/the-list/list-entry/1013093), *National Heritage List for England*, List Entry Number 1013093. Source ID: `historic-england-baconsthorpe-castle-1013093`.

[^baconsthorpe-quarter]: See `research/topics/baconsthorpe-quarter-scenario-analysis.md` for the separate Bacon/Baconsthorpe-family quarter problem around G26 Katherine Baconsthorpe. That file treats the earlier Bacon/Baconsthorpe marriage question as distinct from the later Heydon-led Baconsthorpe Castle context.
```

### 8. Update G19 fact sheet

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

#### 8a. Update opening narrative paragraph

Operation: `str_replace`

`old_string`:

```html
William Gurney IV is the man whose generation makes the West Barsham Gurneys feel substantial again, after a century in which his immediate predecessors are documented only as names and dates of death. He lived through nearly the whole of the Wars of the Roses (1455–85), through Bosworth, through the entire reign of Henry VII, and into the first months of Henry VIII's reign. He was a working sheep-farmer, a Crown officer, a council retainer to the Howard ducal house, and the head of a substantial extended family that produced a Prioress of Thetford, two cadet branches that would last into Tudor and Elizabethan England, and the eldest son, William V (G18), whose marriage to Anne Heydon of Baconsthorpe — granddaughter of Sir Geoffrey Boleyn, Lord Mayor of London — would make their son Anthony Gurney (G17) the second cousin of Queen Anne Boleyn and the second cousin once removed of Queen Elizabeth I (see the related Queen Anne Boleyn fact sheet at G17). <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup><sup class="fn"><a href="#n11" id="ref-11b">11</a></sup><sup class="fn"><a href="#n12" id="ref-12i">12</a></sup><sup class="fn"><a href="#n13" id="ref-13c">13</a></sup>
```

`new_string`:

```html
William Gurney IV is the man whose generation makes the West Barsham Gurneys feel substantial again, after a century in which his immediate predecessors are documented only as names and dates of death. He lived through nearly the whole of the Wars of the Roses (1455–85), through Bosworth, through the entire reign of Henry VII, and into the first months of Henry VIII's reign. He was a working sheep-farmer, a Crown officer, a council retainer to the Howard ducal house, and the head of a substantial extended family that produced a Prioress of Thetford, two cadet branches that would last into Tudor and Elizabethan England, and the eldest son, William V (G18), whose marriage to Anne Heydon, daughter of Sir Henry Heydon of Baconsthorpe Castle and granddaughter of Sir Geoffrey Boleyn, Lord Mayor of London, would make their son Anthony Gurney (G17) the second cousin of Queen Anne Boleyn and the second cousin once removed of Queen Elizabeth I (see the related Queen Anne Boleyn fact sheet at G17). <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup><sup class="fn"><a href="#n11" id="ref-11b">11</a></sup><sup class="fn"><a href="#n12" id="ref-12i">12</a></sup><sup class="fn"><a href="#n13" id="ref-13c">13</a></sup><sup class="fn"><a href="#n18" id="ref-18">18</a></sup>
```

#### 8b. Update wool-economy paragraph

Operation: `str_replace`

`old_string`:

```html
By his 1507 will William directed that 700 sheep should remain at West Barsham after his death. Genealogist Daniel Gurney described this as "a considerable flock in those days," and tied it to a wider Norfolk pattern: light, open sheep-walk country; gentlemen preparing or combing wool for market; and household women spinning yarn and sometimes weaving the prepared wool at home. <sup class="fn"><a href="#n8" id="ref-8c">8</a></sup> The claim is therefore not just that William owned many sheep, but that the flock places West Barsham inside the working economy that fed the Norwich woollen and worsted trades. The Gurneys at this period were not magnates, but they were a substantial gentry sheep-farming household, sufficiently established to support a town residence at Pockthorpe-by-Norwich and a country seat at West Barsham simultaneously. <sup class="fn"><a href="#n8" id="ref-8d">8</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup>
```

`new_string`:

```html
By his 1507 will William directed that 700 sheep should remain at West Barsham after his death. Genealogist Daniel Gurney described this as "a considerable flock in those days," and tied it to a wider Norfolk pattern: light, open sheep-walk country; gentlemen preparing or combing wool for market; and household women spinning yarn and sometimes weaving the prepared wool at home. <sup class="fn"><a href="#n8" id="ref-8c">8</a></sup> The claim is therefore not just that William owned many sheep, but that the flock places West Barsham inside the working economy that fed the Norwich woollen and worsted trades. Baconsthorpe, the Heydon seat into which William's son married, gives the same economic world a larger in-law parallel: English Heritage presents the Tudor Heydons as major wool producers whose castle estate later included wool-processing space and very large sheep flocks. <sup class="fn"><a href="#n19" id="ref-19">19</a></sup> The Gurneys at this period were not magnates, but they were a substantial gentry sheep-farming household, sufficiently established to support a town residence at Pockthorpe-by-Norwich and a country seat at West Barsham simultaneously. <sup class="fn"><a href="#n8" id="ref-8d">8</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup>
```

#### 8c. Update Saxthorpe / Heydon paragraph

Operation: `str_replace`

`old_string`:

```html
William IV himself makes his single most concrete appearance in the historical record in the famous *Paston Letters*. Within six months of his father's death, in January 1472, he entered the manor of Saxthorpe — one of the old Heylesdon-Gurney holdings that his great-grandmother Alice Heylesdon had sold off after Sir John V's 1408 death — and tried to hold a manorial court there as lord. John Paston walked into the court with a single companion, charged the tenants to stop, and when proceedings resumed sat down beside the steward and blotted the court book with his finger as the steward tried to write. William tried again on Holy Rood Day in May 1472, this time backed by Henry Heydon (son of his father's old ally John Heydon of Baconsthorpe), who had raised men-at-arms in case the encounter turned to force. John Paston defused the second attempt as well — and within weeks Henry Heydon went over both their heads and bought Saxthorpe and Titchwell outright from Bishop Waynflete of Winchester, leaving Margaret Paston to write to her son in dismay: "We beat the bushes, and have the loss and the disworship, and other men have the birds." It is the only sustained contemporary narrative for any pre-1500 Gurney, and it shows William IV as a Norfolk gentleman willing to press a disputed claim by force, backed by his Heydon allies. <sup class="fn"><a href="#n17" id="ref-17">17</a></sup>
```

`new_string`:

```html
William IV himself makes his single most concrete appearance in the historical record in the famous *Paston Letters*. Within six months of his father's death, in January 1472, he entered the manor of Saxthorpe — one of the old Heylesdon-Gurney holdings that his great-grandmother Alice Heylesdon had sold off after Sir John V's 1408 death — and tried to hold a manorial court there as lord. John Paston walked into the court with a single companion, charged the tenants to stop, and when proceedings resumed sat down beside the steward and blotted the court book with his finger as the steward tried to write. William tried again on Holy Rood Day in May 1472, this time backed by Henry Heydon (son of his father's old ally John Heydon of Baconsthorpe), who had raised men-at-arms in case the encounter turned to force. John Paston defused the second attempt as well — and within weeks Henry Heydon went over both their heads and bought Saxthorpe and Titchwell outright from Bishop Waynflete of Winchester, leaving Margaret Paston to write to her son in dismay: "We beat the bushes, and have the loss and the disworship, and other men have the birds." It is the only sustained contemporary narrative for any pre-1500 Gurney, and it shows William IV as a Norfolk gentleman willing to press a disputed claim by force, backed by his Heydon allies. Baconsthorpe Castle was the physical centre of that Heydon world: John Heydon had begun the fortified house by this point, Sir Henry Heydon would complete and extend it, and Henry's daughter Anne would marry William IV's son William V in 1484. No source names a Gurney visit there, but the legal alliance, armed support, and marriage arrangement make Baconsthorpe the likely setting of direct contact between the families. <sup class="fn"><a href="#n17" id="ref-17">17</a></sup><sup class="fn"><a href="#n18" id="ref-18b">18</a></sup>
```

#### 8d. Add G19 citation definitions

Operation: `str_replace`

`old_string`:

```html
  <li id="n17">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), Introduction in vol. I, narrating the Saxthorpe Court episode of January–May 1472 from Paston letters Nos. 779 (12 July 1471 trust release), 796 (January 1472 first interruption), and 801 (May 1472 second interruption), with the Margaret Paston letter of 5 June 1472 reporting Henry Heydon's purchase of Saxthorpe and Titchwell from Bishop Waynflete of Winchester. Project Gutenberg vol. I: <a href="https://www.gutenberg.org/cache/epub/43348/pg43348.txt">www.gutenberg.org/cache/epub/43348/pg43348.txt</a>. <a class="citation-back" href="#ref-17">↩</a></li>
```

`new_string`:

```html
  <li id="n17">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), Introduction in vol. I, narrating the Saxthorpe Court episode of January–May 1472 from Paston letters Nos. 779 (12 July 1471 trust release), 796 (January 1472 first interruption), and 801 (May 1472 second interruption), with the Margaret Paston letter of 5 June 1472 reporting Henry Heydon's purchase of Saxthorpe and Titchwell from Bishop Waynflete of Winchester. Project Gutenberg vol. I: <a href="https://www.gutenberg.org/cache/epub/43348/pg43348.txt">www.gutenberg.org/cache/epub/43348/pg43348.txt</a>. <a class="citation-back" href="#ref-17">↩</a></li>
  <li id="n18">English Heritage, <a href="https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/">"History of Baconsthorpe Castle,"</a> English Heritage, describing Baconsthorpe as the Heydons' main residence from about 1450, John Heydon d.1479 as builder of the earliest castle building, and Sir Henry Heydon d.1504 as completing and extending the castle. Historic England, <a href="https://historicengland.org.uk/listing/the-list/list-entry/1013093">"Baconsthorpe Castle moated site with fortified house, gatehouse, courtyards and formal gardens,"</a> <em>National Heritage List for England</em>, List Entry Number 1013093, identifies the site as a Scheduled Monument with extant remains and earthworks. Source IDs: <code>english-heritage-baconsthorpe-castle-history</code>, <code>historic-england-baconsthorpe-castle-1013093</code>. <a class="citation-back" href="#ref-18">↩</a> <a class="citation-back" href="#ref-18b">↩</a></li>
  <li id="n19">English Heritage, <a href="https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/tudor-wool-factory/">"The Rise and Fall of a Tudor Wool Factory,"</a> English Heritage, describing the Tudor Heydon wool economy at Baconsthorpe Castle: pasture surrounding the castle, wool-processing space in the east range, cloth sold in England and the Netherlands, and the head-shepherd / large-flock evidence for the scale of the estate. Source ID: <code>english-heritage-baconsthorpe-castle-wool-factory</code>. <a class="citation-back" href="#ref-19">↩</a></li>
```

### 9. Update G20 fact sheet

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

#### 9a. Update Heydon alliance paragraph

Operation: `str_replace`

`old_string`:

```html
The will named three sons. William IV was the heir; two further sons, John and Edmund, were confirmed in grants out of the Suffolk manor of Depden. The executors were Margaret his wife, John Jerningham (almost certainly Margaret's brother, of the Somerleyton Jerninghams), and Edmund Bokenham Esquire of Old Buckenham. The supervisor — the senior overseer of the executors — was John Heydon of Baconsthorpe, the most powerful Norfolk lawyer of the mid-fifteenth century and the principal antagonist of the Paston family in the famous *Paston Letters* correspondence. The Gurney-Heydon alliance documented in this 1471 will would be sealed thirteen years later by the marriage of Thomas's grandson William V (G18) to John Heydon's granddaughter Anne Heydon. <sup class="fn"><a href="#n13" id="ref-13">13</a></sup>
```

`new_string`:

```html
The will named three sons. William IV was the heir; two further sons, John and Edmund, were confirmed in grants out of the Suffolk manor of Depden. The executors were Margaret his wife, John Jerningham (almost certainly Margaret's brother, of the Somerleyton Jerninghams), and Edmund Bokenham Esquire of Old Buckenham. The supervisor — the senior overseer of the executors — was John Heydon of Baconsthorpe, the most powerful Norfolk lawyer of the mid-fifteenth century and the principal antagonist of the Paston family in the famous *Paston Letters* correspondence. Baconsthorpe was not only a surname-style or parish label: by Thomas's lifetime John Heydon had begun the fortified manor house that became the Heydons' principal seat, and his son Sir Henry Heydon would complete and extend it. <sup class="fn"><a href="#n16" id="ref-16">16</a></sup> The Gurney-Heydon alliance documented in this 1471 will would be backed in the field by Henry Heydon in 1472 and sealed thirteen years later by the marriage of Thomas's grandson William V (G18) to Henry's daughter Anne Heydon, who likely knew Baconsthorpe as her family home. <sup class="fn"><a href="#n13" id="ref-13">13</a></sup><sup class="fn"><a href="#n16" id="ref-16b">16</a></sup>
```

#### 9b. Update wool paragraph

Operation: `str_replace`

`old_string`:

```html
The will's most personal bequest is to Margaret. Thomas left all the household's "woolen and linen cloths" to his wife, Daniel Gurney noting specifically that these were "being her own work and that of her servants." <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup> Daniel Gurney uses this bequest alongside William IV's later 700-sheep will clause to describe a Norfolk wool economy in which gentlemen prepared wool for market and household women spun yarn or sometimes wove prepared wool at home. The stronger published claim is therefore not that Margaret's work can be quantified as a commercial business, but that the will gives rare household-level evidence for the textile labor behind a substantial Norfolk gentry estate. <sup class="fn"><a href="#n9" id="ref-9c">9</a></sup>
```

`new_string`:

```html
The will's most personal bequest is to Margaret. Thomas left all the household's "woolen and linen cloths" to his wife, Daniel Gurney noting specifically that these were "being her own work and that of her servants." <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup> Daniel Gurney uses this bequest alongside William IV's later 700-sheep will clause to describe a Norfolk wool economy in which gentlemen prepared wool for market and household women spun yarn or sometimes wove prepared wool at home. Baconsthorpe deepens that context on the in-law side: the Heydons later turned their castle estate into a major Tudor wool operation, with large flocks and dedicated wool-processing space. <sup class="fn"><a href="#n16" id="ref-16c">16</a></sup> The stronger published claim is therefore not that Margaret's work can be quantified as a commercial business, or that the Gurneys and Heydons ran a shared wool enterprise, but that both allied houses belonged to the same north-Norfolk wool landscape. <sup class="fn"><a href="#n9" id="ref-9c">9</a></sup><sup class="fn"><a href="#n16" id="ref-16d">16</a></sup>
```

#### 9c. Add G20 citation definition

Operation: `str_replace`

`old_string`:

```html
  <li id="n15">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew &amp; Son, 1858), Note 126, p. 814, records an 8 June 1445 deed in the charter room at Hunstanton Hall: Sir Thomas Kerdeston, Sir William Oldhalle, Thomas Gurnay, Esq., and others, to John Wode of Berston and others, of the manor called Waldgraves in East Barsham. Daniel Gurney notes Thomas Gurnay's red-wax seal on the fifth label. Daniel Gurney's <em>Supplement</em>, Note 123, separately states Thomas I was probably dead before 1444, so the 1445 sealer is most likely Thomas II. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-15">↩</a></li>
```

`new_string`:

```html
  <li id="n15">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew &amp; Son, 1858), Note 126, p. 814, records an 8 June 1445 deed in the charter room at Hunstanton Hall: Sir Thomas Kerdeston, Sir William Oldhalle, Thomas Gurnay, Esq., and others, to John Wode of Berston and others, of the manor called Waldgraves in East Barsham. Daniel Gurney notes Thomas Gurnay's red-wax seal on the fifth label. Daniel Gurney's <em>Supplement</em>, Note 123, separately states Thomas I was probably dead before 1444, so the 1445 sealer is most likely Thomas II. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-15">↩</a></li>
  <li id="n16">English Heritage, <a href="https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/">"History of Baconsthorpe Castle,"</a> English Heritage; English Heritage, <a href="https://www.english-heritage.org.uk/visit/places/baconsthorpe-castle/history/tudor-wool-factory/">"The Rise and Fall of a Tudor Wool Factory,"</a> English Heritage; Historic England, <a href="https://historicengland.org.uk/listing/the-list/list-entry/1013093">"Baconsthorpe Castle moated site with fortified house, gatehouse, courtyards and formal gardens,"</a> <em>National Heritage List for England</em>, List Entry Number 1013093. These sources support the castle as the Heydon family seat and later wool-estate context; they do not independently prove a named Gurney visit. Source IDs: <code>english-heritage-baconsthorpe-castle-history</code>, <code>english-heritage-baconsthorpe-castle-wool-factory</code>, <code>historic-england-baconsthorpe-castle-1013093</code>. <a class="citation-back" href="#ref-16">↩</a> <a class="citation-back" href="#ref-16b">↩</a> <a class="citation-back" href="#ref-16c">↩</a> <a class="citation-back" href="#ref-16d">↩</a></li>
```

### 10. Validation commands

After applying all operations:

1. Validate JSON:

```powershell
.\.venv\Scripts\python.exe -m json.tool data\sources.json > $null
.\.venv\Scripts\python.exe -m json.tool data\places.json > $null
.\.venv\Scripts\python.exe -m json.tool data\places_detail.json > $null
.\.venv\Scripts\python.exe -m json.tool data\ancestors.json > $null
```

2. Check new source/place references:

```powershell
rg -n "english-heritage-baconsthorpe-castle-history|english-heritage-baconsthorpe-castle-wool-factory|historic-england-baconsthorpe-castle-1013093|place-baconsthorpe-castle-norfolk-england" data sources research fact-sheets
```

3. Check fact-sheet placeholder and anchor hygiene:

```powershell
rg -n "NEW|ref-18[^a-z0-9\"]|ref-19[^a-z0-9\"]|ref-16[^a-z0-9\"]" fact-sheets/g19-william-gurney-iv-fact-sheet.md fact-sheets/g20-thomas-gournay-ii-fact-sheet.md
```

4. Run targeted whitespace check:

```powershell
git diff --check -- data/sources.json data/places.json data/places_detail.json data/ancestors.json sources/corpus_supplement/english-heritage-baconsthorpe-castle-history.md sources/corpus_supplement/english-heritage-baconsthorpe-castle-wool-factory.md sources/corpus_supplement/historic-england-baconsthorpe-castle-1013093.md sources/validations/english-heritage-baconsthorpe-castle-history.md sources/validations/english-heritage-baconsthorpe-castle-wool-factory.md sources/validations/historic-england-baconsthorpe-castle-1013093.md research/places/baconsthorpe-castle.md fact-sheets/g19-william-gurney-iv-fact-sheet.md fact-sheets/g20-thomas-gournay-ii-fact-sheet.md
```

5. Run site validation/package from `site/website`:

```powershell
cd site\website
npm.cmd run validate
npm.cmd run package
```

If `npm.cmd run package` hits a transient OneDrive `_site` permission lock, wait briefly and retry once.

## Completion housekeeping

When Phase 2 has applied this patchset and validation succeeds:

1. Prepend `**Done:** YYYY-MM-DD HH:MM PT` to this patchset.
2. Move this file to `sources/intake/done/`.
3. Leave `sources/intake/processed/stub-v82.md` as the next active stub.

