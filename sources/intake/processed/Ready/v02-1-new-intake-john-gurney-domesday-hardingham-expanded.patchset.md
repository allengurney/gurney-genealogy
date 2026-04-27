# Intake patchset v02 — John Gurney tailor deed; Hugh de Gournay Open Domesday trio; Hardingham / Swathing

**Prepared:** 2026-04-26  
**Repo:** `allengurney/gurney-genealogy`  
**Repo ref inspected:** `main` @ `c8098bd5c73dc028ef64157e1472f9e452d50bf8`  
**Patchset destination when applied:** `sources/intake/processed/v02.patchset.md`

## Scope

Retain and promote all three intake items.

- **Item 1:** Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.* — page 10 deed extract for John Gurney, tailor.
- **Item 2:** Open Domesday records for Hugh of Gournay at Ardleigh, Fordham, and Liston.
- **Item 3:** Hardingham Parish Council / parish website history text for Hardingham, Flockthorpe, Swathing / Low Street, and the Manor of Gurneys & Swathing.

## Web/source verification notes

- The Internet Archive / Wikimedia PDF text for Bates was reachable through web search; container download failed due local DNS/network restrictions, so this patchset relies on the web-retrieved metadata plus the user-supplied page-10 quotation. Use the exact PDF URL for final validation if applying with a networked shell.
- Open Domesday pages were retrieved for Ardleigh, Fordham, Liston, Hugh of Gournay, and the Open Domesday About page.
- The Hardingham Parish website was retrieved at the supplied URL, and the user-supplied text matches the relevant history content to be promoted.

---

## 1. `data/sources.json`

### 1.1 Update metadata date

Change:

```json
"lastUpdated": "2026-04-19"
```

to:

```json
"lastUpdated": "2026-04-26"
```

### 1.2 Add source entry: Bates, *Ancient Iron Works at Braintree*

Insert under `"sources"` near the existing John Gurney / New England sources, preferably after `history-of-weymouth` or near `sprague-braintree`:

```json
    "bates-ancient-iron-works-braintree-1898": {
      "shortTitle": "Bates, Ancient Iron Works at Braintree",
      "citation": "Bates, Samuel A. The Ancient Iron Works at Braintree, Mass.: The First in America. South Braintree, Mass.: Frank A. Bates, 1898.",
      "archive": "Internet Archive / Library of Congress digitization; PDF at ia800605.us.archive.org",
      "url": "https://ia800605.us.archive.org/34/items/ancientironworks00bate/ancientironworks00bate.pdf",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/bates-ancient-iron-works-braintree-1898-john-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/bates-ancient-iron-works-braintree-1898.md",
      "notes": "Braintree local-history pamphlet. Page 10 preserves a 12 Feb. 1661 conveyance in which John Gurney is explicitly styled 'Taylor' and sells a house, orchard, five-acre parcel, and adjacent half-acre parcel to Richard Thayer. Useful independent confirmation of John Gurney-1's occupation and Braintree property description."
    },
```

### 1.3 Add or revise source entry: Open Domesday

Existing source `domesday-1086` is generic. Add a distinct Open Domesday source for the dataset / web edition, and then use this new `sourceId` for the new place entries.

```json
    "open-domesday-powell-smith": {
      "shortTitle": "Open Domesday",
      "citation": "Powell-Smith, Anna. Open Domesday. Data created by Professor J. J. N. Palmer and team at the University of Hull, using the Domesday Explorer dataset and Phillimore English translation.",
      "archive": "Open Domesday online dataset and page images",
      "url": "https://opendomesday.org/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/open-domesday-hugh-of-gournay-essex-trio.md",
      "mediaPath": null,
      "validationPath": "sources/validations/open-domesday-powell-smith.md",
      "notes": "Online edition / dataset for Domesday Book. The About page says Open Domesday was built by Anna Powell-Smith from data created by Professor J. J. N. Palmer and a University of Hull team; the site describes Domesday Book as a survey of landholdings and resources in AD 1086. Used here for Hugh of Gournay's Ardleigh, Fordham, and Liston entries."
    },
```

Optional: update existing `domesday-1086.notes` to say:

```text
For normalized Open Domesday data used in place files, see sourceId `open-domesday-powell-smith`.
```

### 1.4 Add source entry: Hardingham Parish history page

Insert near `blomefield-norfolk` or other Norfolk place sources:

```json
    "hardingham-parish-history-2026": {
      "shortTitle": "Hardingham Parish history page",
      "citation": "Hardingham Parish Council / Hardingham Parish website. \"History of Hardingham.\" Accessed 26 April 2026.",
      "archive": "Hardingham Parish website",
      "url": "https://hardinghamparish.wixsite.com/home/history-of-hardingham-1",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/hardingham-parish-history-2026.md",
      "mediaPath": null,
      "validationPath": "sources/validations/hardingham-parish-history-2026.md",
      "notes": "Local parish history page. Useful for Hardingham/Flockthorpe/Mantatestone/Manson Green and Swathing/Low Street identification; states that between 1066 and 1210 there were two lordships, including the Manor of Gurneys & Swathing. Treat as local historical source and cross-check against Blomefield, Norfolk HER, and manorial records for formal proof."
    },
```

---

## 2. New corpus / validation files

### 2.1 Create `sources/corpus_supplement/bates-ancient-iron-works-braintree-1898-john-gurney-extract.md`

```markdown
# Bates, Ancient Iron Works at Braintree (1898) — John Gurney extract

**Source ID:** `bates-ancient-iron-works-braintree-1898`

**Citation:** Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10.

**URL:** https://ia800605.us.archive.org/34/items/ancientironworks00bate/ancientironworks00bate.pdf

## Extract

> Feb. 12, 1661, John Gurney, Taylor, conveyed to Richard Thayer for fourteen pounds, one house and orchard on which the house stands, five acres of land bounded south on Monoticot river; east on Richard Thayer, Nathaniel Mott and John[— ? — ]; north on Simon Crosby; west on George Aldridge. Also one-half acre west of the last lot, river on the south, highway on the north, George Aldrich on the east.

Bates continues with contextual notes on neighbors:

> Nathaniel Mott was killed by the Indians in 1675, [and] George Aldrich and Daniel Lovett removed.

## Research value

This is a secondary printed extract of a colonial deed. It independently confirms John Gurney's occupation as tailor and gives a fuller Braintree property description than the current research file preserves.
```

### 2.2 Create `sources/validations/bates-ancient-iron-works-braintree-1898.md`

```markdown
# Source validation: Bates, Ancient Iron Works at Braintree

**Source ID:** `bates-ancient-iron-works-braintree-1898`

**Source examined:** Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), Internet Archive PDF.

**Scope checked:** Page 10 extract supplied for John Gurney's 12 Feb. 1661 conveyance to Richard Thayer.

**Finding destination:** `research/people/g13-john-gurney-fact-sheet.research.md`; `research/places/braintree-ma.md`.

**Limitations:** This is a printed secondary extract of a deed, not the deed image itself. The property and occupation should also be checked against Suffolk County deed books or published Braintree records if the original deed volume is later obtained.
```

### 2.3 Create `sources/corpus_supplement/open-domesday-hugh-of-gournay-essex-trio.md`

```markdown
# Open Domesday — Hugh of Gournay's Essex Domesday trio

**Source ID:** `open-domesday-powell-smith`

**Citation:** Anna Powell-Smith, *Open Domesday*, data created by Professor J. J. N. Palmer and team at the University of Hull.

**Home:** https://opendomesday.org/

**About:** https://opendomesday.org/about/

## Hugh of Gournay name page

Open Domesday lists Hugh of Gournay as tenant-in-chief in 1086 at three post-Conquest places: Ardleigh, Fordham, and Liston.

## Ardleigh

**URL:** https://opendomesday.org/place/TM0529/ardleigh/  
**Hundred:** Tendring  
**County:** Essex / Suffolk  
**Phillimore reference:** Essex 47,2

### Land of Hugh of Gournay

- Households: 7 villagers.
- Ploughland: 2 lord's plough teams; 3 men's plough teams.
- Other resources: meadow 3 acres; woodland 40 pigs; 2 mills.
- Livestock in 1066: 5 pigs; 30 sheep.
- Livestock in 1086: 7 cattle; 8 pigs; 44 sheep; 10 goats; 3 beehives.
- Annual value to lord: 4 pounds in 1086; 4 pounds when acquired by the 1086 owner; 6 pounds in 1066.
- Tenant-in-chief in 1086: Hugh of Gournay.
- Lord in 1086: Agnes.
- Lord in 1066: Osbert.

## Fordham

**URL:** https://opendomesday.org/place/TL9228/fordham/  
**Hundred:** Lexden  
**County:** Essex  
**Phillimore reference:** Essex 47,3

### Land of Hugh of Gournay

- Households: 7 villagers; 3 freemen; 11 smallholders; 4 slaves.
- Ploughland: 3 lord's plough teams; 3.5 men's plough teams.
- Other resources: meadow 12 acres; woodland 100 pigs; 1 mill.
- Livestock in 1066: 2 cobs; 3 cows; 8 pigs; 60 sheep; 12 goats; 10 beehives; 3 calves.
- Livestock in 1086: 2 cobs; 8 cattle; 10 pigs; 80 sheep; 25 goats; 6 beehives.
- Annual value to lord: 7 pounds in 1086; 7 pounds when acquired by the 1086 owner; 7 pounds in 1066.
- Tenant-in-chief in 1086: Hugh of Gournay.
- Lord in 1086: Geoffrey.
- Lord in 1066: Esbiorn.

## Liston

**URL:** https://opendomesday.org/place/TL8544/liston/  
**Hundred:** Hinckford  
**County:** Essex  
**Phillimore reference:** Essex 47,1

### Land of Hugh of Gournay

- Households: 5 smallholders.
- Ploughland: 2 lord's plough teams; 1 men's plough team.
- Other resources: meadow 30 acres; 0.5 mills.
- Livestock in 1066: 3 cows; 7 pigs; 12 sheep; 3 calves.
- Livestock in 1086: 3 cows; 22 sheep; 8 beehives; 3 other.
- Annual value to lord: 3 pounds 7 shillings and 12 pence in 1086; 3 pounds 7 shillings and 12 pence when acquired by the 1086 owner; 3 pounds 7 shillings and 12 pence in 1066.
- Tenant-in-chief in 1086: Hugh of Gournay.
- Lord in 1086: Geoffrey Talbot.
- Lord in 1066: one free man.
```

### 2.4 Create `sources/validations/open-domesday-powell-smith.md`

```markdown
# Source validation: Open Domesday — Hugh of Gournay entries

**Source ID:** `open-domesday-powell-smith`

**Source examined:** Open Domesday home/about pages; Hugh of Gournay name page; Ardleigh, Fordham, and Liston place pages.

**Scope checked:** Hugh of Gournay entries for Ardleigh, Fordham, and Liston.

**Finding destinations:** `research/places/ardleigh.md`, `research/places/fordham.md`, `research/places/liston.md`, and `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`.

**Limitations:** Open Domesday is a normalized online dataset and English-readable presentation of Domesday data, not the manuscript folio itself. The place files should still preserve Phillimore references and, if later needed, compare against the folio images and printed Phillimore text.
```

### 2.5 Create `sources/corpus_supplement/hardingham-parish-history-2026.md`

```markdown
# Hardingham Parish history page — Hardingham, Flockthorpe, Swathing

**Source ID:** `hardingham-parish-history-2026`

**Citation:** Hardingham Parish Council / Hardingham Parish website, "History of Hardingham," accessed 26 April 2026.

**URL:** https://hardinghamparish.wixsite.com/home/history-of-hardingham-1

## Extract

Hardingham is not mentioned in the Domesday Book, but Flockthorpe is. There was an outlier to the village called "Mantatestone" which today is known as Manson Green and another "Swathing" which is now called Low Street. Between 1066 and 1210 there were two Lordships, the family of De Camois were seised of the Manor of Flockthorpe, the second was the Manor of Gurneys & Swathing. In 1210 Flockthorpe became Hardingham. "Ham" is common Saxon name for a small village or settlement.

The Lordship of the Manor stayed in the Wodehouse/Kimberley family until 1985 when the previous Lord Kimberley sold it to William Shaughnessey of the U.S.A.

The village acreage is 2418 acres.

The moat, called the Roundabout at Gresham Farm, is estimated to date from 1066-1539 and considered the site of a residence for Sir Thomas Gresham. Looking at a map of Hardingham it can be noted that the Gresham moat is almost exactly the centre of the village and not the Church. The church is the oldest building in the village now.

The Old Hall on the opposite side of the road to the church is considered late 16th century and the village must have originally been round this area.

Now the village has hamlets at "Low Street", "Danemoor", "Manson Green", "Nordelph Corner" and "Hackford Road" as well as High Common, where there is a Village Hall on the Playing Field, which was given to the village by the Edwards family after the first world war.
```

### 2.6 Create `sources/validations/hardingham-parish-history-2026.md`

```markdown
# Source validation: Hardingham Parish history page

**Source ID:** `hardingham-parish-history-2026`

**Source examined:** Hardingham Parish Council / parish website, "History of Hardingham."

**Scope checked:** Local-history section identifying Flockthorpe, Mantatestone / Manson Green, Swathing / Low Street, and the Manor of Gurneys & Swathing.

**Finding destination:** `research/places/hardingham.md`.

**Limitations:** This is a local parish-history web page. It is suitable for place-file context and geolocation clues, but formal manorial claims should still be cross-checked against Blomefield, Norfolk Heritage Explorer, manorial documents, and parish/estate records.
```

---

## 3. `research/people/g13-john-gurney-fact-sheet.research.md`

### 3.1 Revise the land/property table row for 12 Feb 1661

Current row in **Land and property records**:

```markdown
| 12 Feb 1661 | Braintree land sale | Sold land in Braintree. Deed witnessed by son John Jr. | Braintree deed records |
```

Replace with:

```markdown
| 12 Feb 1661 | Braintree land sale | John Gurney, identified as "Taylor," conveyed to Richard Thayer for £14 a house and orchard, a five-acre parcel on the Monatiquot/Monoticot River, and an additional half-acre parcel west of the first lot. | Bates, *Ancient Iron Works at Braintree*, p. 10; Braintree deed records |
```

### 3.2 Add a new subsection under **Land and property records**

Insert after the land/property table and before the paragraph beginning `John appears to have died with no land.`:

```markdown
#### 1661 Braintree conveyance to Richard Thayer

The 12 February 1661 Braintree deed is another direct occupation witness: Bates prints the grantor as "John Gurney, Taylor." It also gives a fuller property description than the current summary preserves: Gurney conveyed to Richard Thayer, for fourteen pounds, "one house and orchard on which the house stands," plus five acres bounded south on the Monoticot River, east on Richard Thayer, Nathaniel Mott, and a partially unclear John-name neighbor, north on Simon Crosby, and west on George Aldridge. He also conveyed an adjacent half-acre west of the first lot, with the river to the south, the highway to the north, and George Aldrich on the east.[^bates-ironworks-gurney]

[^bates-ironworks-gurney]: Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, quoting the 12 Feb. 1661 conveyance from John Gurney to Richard Thayer. Source ID: `bates-ancient-iron-works-braintree-1898`.
```

---

## 4. `research/places/braintree-ma.md`

Replace the file body before the generated place-registry block with the following. Preserve the existing generated registry block unchanged unless a later structured-data rebuild is being performed.

```markdown
# Braintree, Massachusetts, USA

Braintree is a core New England locality for John Gurney-1 (G13). His Braintree record includes tenancy, land possession, and a 12 February 1661 conveyance in which he is explicitly identified as a tailor.

## John Gurney-1 at Braintree

John appears at Braintree as a working tradesman and landholder/tenant rather than as a large proprietor. The existing research file notes 48 acres at Braintree "in the possession of John Gurney" in the 25 May 1653 Tyng inventory, and Bates' later local-history extract adds an explicit 12 February 1661 conveyance by "John Gurney, Taylor."[^bates-braintree]

The 1661 deed description is useful for neighborhood reconstruction. Gurney conveyed to Richard Thayer, for £14, a house and orchard, a five-acre parcel bounded south by the Monoticot River, east by Richard Thayer, Nathaniel Mott, and another partially unclear John-name neighbor, north by Simon Crosby, and west by George Aldridge. He also conveyed a half-acre parcel west of that lot, with the river on the south, the highway on the north, and George Aldrich on the east.[^bates-braintree]

This source should be read as a printed secondary extract of a deed. It is strong enough to support the occupation and property-description note here, but the underlying deed book remains the best target for final primary-source validation.

[^bates-braintree]: Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, 12 Feb. 1661 conveyance from John Gurney to Richard Thayer. Source ID: `bates-ancient-iron-works-braintree-1898`.
```

---

## 5. Open Domesday place-file updates

### 5.1 `research/places/ardleigh.md`

#### Replace current `## Domesday detail` section

Replace from `## Domesday detail` through the end of the `## Open items` list with:

```markdown
## Domesday detail

Open Domesday records Ardleigh in the hundred of Tendring, mentioned in the chapters for Essex and Suffolk. The settlement had 38 recorded households in 1086 and is listed under five owners. Hugh of Gournay's Ardleigh entry is Phillimore reference Essex 47,2.[^open-domesday-ardleigh]

### Land of Hugh of Gournay

- Households: 7 villagers.
- Ploughland: 2 lord's plough teams; 3 men's plough teams.
- Other resources: meadow 3 acres; woodland for 40 pigs; 2 mills.
- Livestock in 1066: 5 pigs; 30 sheep.
- Livestock in 1086: 7 cattle; 8 pigs; 44 sheep; 10 goats; 3 beehives.
- Annual value to lord: £4 in 1086; £4 when acquired by the 1086 owner; £6 in 1066.
- Tenant-in-chief in 1086: Hugh of Gournay.
- Lord in 1086: Agnes.
- Lord in 1066: Osbert.

## Interpretive caution

Ardleigh is now no longer a thin project record: the Open Domesday pull supplies a concrete population, resource, livestock, valuation, and lordship profile. It still remains one member of the Essex Domesday trio and should be read with Fordham and Liston rather than in isolation.

## Open items

- [ ] Check whether Ardleigh remained in Gournay hands after Hugh III.
- [ ] Compare Ardleigh's valuations and dependencies against Fordham and Liston once the direct folio image / Phillimore text is checked.
```

#### Add source footnote before `## Sources`

```markdown
[^open-domesday-ardleigh]: Anna Powell-Smith, *Open Domesday*, Ardleigh, Tendring, Essex / Suffolk, "Land of Hugh of Gournay," Phillimore reference Essex 47,2, https://opendomesday.org/place/TM0529/ardleigh/. Data created by Professor J. J. N. Palmer and team at the University of Hull. Source ID: `open-domesday-powell-smith`.
```

#### Revise `## Sources`

Add:

```markdown
- Anna Powell-Smith, *Open Domesday*, Ardleigh, Tendring, Essex / Suffolk, "Land of Hugh of Gournay," Phillimore reference Essex 47,2. [Open Domesday]
```

Remove or revise the current open-item language that says the Domesday entry still needs to be pulled directly; Open Domesday has now been pulled.

### 5.2 `research/places/fordham.md`

#### Replace current `## Domesday detail` section through `## Open items`

```markdown
## Domesday detail

Open Domesday records Fordham in the hundred of Lexden, Essex. It had 31 recorded households in 1086, putting it in the largest 40% of Domesday settlements, and is listed under four owners. Hugh of Gournay's Fordham entry is Phillimore reference Essex 47,3.[^open-domesday-fordham]

### Land of Hugh of Gournay

- Households: 7 villagers; 3 freemen; 11 smallholders; 4 slaves.
- Ploughland: 3 lord's plough teams; 3.5 men's plough teams.
- Other resources: meadow 12 acres; woodland for 100 pigs; 1 mill.
- Livestock in 1066: 2 cobs; 3 cows; 8 pigs; 60 sheep; 12 goats; 10 beehives; 3 calves.
- Livestock in 1086: 2 cobs; 8 cattle; 10 pigs; 80 sheep; 25 goats; 6 beehives.
- Annual value to lord: £7 in 1086; £7 when acquired by the 1086 owner; £7 in 1066.
- Tenant-in-chief in 1086: Hugh of Gournay.
- Lord in 1086: Geoffrey.
- Lord in 1066: Esbiorn.

## Interpretive note

Fordham remains the most socio-economically textured of the Essex trio. The Open Domesday entry confirms a larger dependent population than Ardleigh or Liston, with villagers, freemen, smallholders, and slaves, plus meadow, woodland, a mill, and a stable £7 annual value across 1066, acquisition, and 1086.

## Primary-source hooks

- **Domesday Book (1086)** — Essex 47,3 for Fordham. Open Domesday supplies normalized data and folio/page links.

## Open items

- [ ] Check whether Fordham remained in Gournay hands after Hugh III.
- [ ] Compare the valuation and labour profile with Ardleigh and Liston against the folio image / Phillimore text.
```

#### Add footnote

```markdown
[^open-domesday-fordham]: Anna Powell-Smith, *Open Domesday*, Fordham, Lexden, Essex, "Land of Hugh of Gournay," Phillimore reference Essex 47,3, https://opendomesday.org/place/TL9228/fordham/. Data created by Professor J. J. N. Palmer and team at the University of Hull. Source ID: `open-domesday-powell-smith`.
```

#### Revise sources

Add:

```markdown
- Anna Powell-Smith, *Open Domesday*, Fordham, Lexden, Essex, "Land of Hugh of Gournay," Phillimore reference Essex 47,3. [Open Domesday]
```

Remove the current open item saying the Domesday Essex entry still needs to be pulled for valuation/full detail; replace with the folio-image / Phillimore verification item above.

### 5.3 `research/places/liston.md`

#### Replace current `## Domesday detail` section through `## Open items`

```markdown
## Domesday detail

Open Domesday records Liston in the hundred of Hinckford, Essex. It had 25 recorded households in 1086, putting it in the largest 40% of Domesday settlements, and is listed under two owners. Hugh of Gournay's Liston entry is Phillimore reference Essex 47,1.[^open-domesday-liston]

### Land of Hugh of Gournay

- Households: 5 smallholders.
- Ploughland: 2 lord's plough teams; 1 men's plough team.
- Other resources: meadow 30 acres; 0.5 mills.
- Livestock in 1066: 3 cows; 7 pigs; 12 sheep; 3 calves.
- Livestock in 1086: 3 cows; 22 sheep; 8 beehives; 3 other.
- Annual value to lord: £3 7s. 12d. in 1086; £3 7s. 12d. when acquired by the 1086 owner; £3 7s. 12d. in 1066.
- Tenant-in-chief in 1086: Hugh of Gournay.
- Lord in 1086: Geoffrey Talbot.
- Lord in 1066: one free man.

The named 1086 lord, Geoffrey Talbot, preserves the sub-tenancy signal already noted in this file, but the Open Domesday entry now supplies the fuller economic profile: smallholders only, two lord's plough teams, one men's plough team, substantial meadow, a half mill, sheep, beehives, and a stable valuation across 1066, acquisition, and 1086.

## Interpretive note

Liston remains especially useful for showing layered lordship beneath Hugh of Gournay. With Open Domesday added, it also becomes a concrete smallholder/manorial economy record rather than merely a Talbot sub-tenancy note.

## Primary-source hooks

- **Domesday Book (1086)** — Essex 47,1 for Liston. Open Domesday supplies normalized data and folio/page links.

## Open items

- [ ] Check whether the Liston holdings remained in Gournay hands after Hugh III, or whether they passed to another tenant-in-chief after his death c. 1093.
- [ ] Compare the Talbot sub-tenancy at Liston against any similar patterns in Fordham or Ardleigh using the folio image / Phillimore text.
```

#### Add footnote

```markdown
[^open-domesday-liston]: Anna Powell-Smith, *Open Domesday*, Liston, Hinckford, Essex, "Land of Hugh of Gournay," Phillimore reference Essex 47,1, https://opendomesday.org/place/TL8544/liston/. Data created by Professor J. J. N. Palmer and team at the University of Hull. Source ID: `open-domesday-powell-smith`.
```

#### Revise sources

Add:

```markdown
- Anna Powell-Smith, *Open Domesday*, Liston, Hinckford, Essex, "Land of Hugh of Gournay," Phillimore reference Essex 47,1. [Open Domesday]
```

Remove the current wording that says the Domesday entry is "cited via DG and Hannay, not independently verified"; it is now independently verified through Open Domesday, while the folio/Phillimore comparison remains a remaining item.

---

## 6. `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`

### 6.1 Add a new working note after the current `### Domesday folio reference` section

```markdown
### Open Domesday extraction — Ardleigh, Fordham, Liston

Open Domesday now supplies normalized data for all three Essex Domesday holdings of Hugh of Gournay. Its Hugh of Gournay name page lists him as tenant-in-chief in 1086 at exactly three post-Conquest places: Ardleigh, Fordham, and Liston.[^open-domesday-hugh]

- **Ardleigh, Tendring, Essex / Suffolk (Essex 47,2):** 7 villagers; 2 lord's plough teams; 3 men's plough teams; meadow 3 acres; woodland for 40 pigs; 2 mills; value £4 in 1086, £4 when acquired, £6 in 1066; 1086 lord Agnes; 1066 lord Osbert.[^open-domesday-ardleigh-g33]
- **Fordham, Lexden, Essex (Essex 47,3):** 7 villagers, 3 freemen, 11 smallholders, and 4 slaves; 3 lord's plough teams; 3.5 men's plough teams; meadow 12 acres; woodland for 100 pigs; 1 mill; value £7 in 1086, at acquisition, and in 1066; 1086 lord Geoffrey; 1066 lord Esbiorn.[^open-domesday-fordham-g33]
- **Liston, Hinckford, Essex (Essex 47,1):** 5 smallholders; 2 lord's plough teams; 1 men's plough team; meadow 30 acres; half a mill; value £3 7s. 12d. in 1086, at acquisition, and in 1066; 1086 lord Geoffrey Talbot; 1066 lord one free man.[^open-domesday-liston-g33]

Together, the three entries strengthen the point that Hugh's English footprint was compact but economically diverse: Fordham is the largest and most socially mixed entry, Ardleigh is mill-heavy for its size, and Liston is the clearest Talbot sub-tenancy record.

[^open-domesday-hugh]: Anna Powell-Smith, *Open Domesday*, "Hugh of Gournay," https://opendomesday.org/name/hugh-of-gournay/. Data created by Professor J. J. N. Palmer and team at the University of Hull. Source ID: `open-domesday-powell-smith`.
[^open-domesday-ardleigh-g33]: Anna Powell-Smith, *Open Domesday*, Ardleigh, Tendring, Essex / Suffolk, "Land of Hugh of Gournay," Phillimore reference Essex 47,2, https://opendomesday.org/place/TM0529/ardleigh/. Source ID: `open-domesday-powell-smith`.
[^open-domesday-fordham-g33]: Anna Powell-Smith, *Open Domesday*, Fordham, Lexden, Essex, "Land of Hugh of Gournay," Phillimore reference Essex 47,3, https://opendomesday.org/place/TL9228/fordham/. Source ID: `open-domesday-powell-smith`.
[^open-domesday-liston-g33]: Anna Powell-Smith, *Open Domesday*, Liston, Hinckford, Essex, "Land of Hugh of Gournay," Phillimore reference Essex 47,1, https://opendomesday.org/place/TL8544/liston/. Source ID: `open-domesday-powell-smith`.
```

### 6.2 Revise `## Sources Consulted`

Replace:

```markdown
- Domesday Book, Little Domesday vol. ii, p. 89 (Essex): Liston, Fordham, Ardleigh. Verified via Open Domesday (opendomesday.org). [Domesday]
```

with:

```markdown
- Anna Powell-Smith, *Open Domesday*: Hugh of Gournay; Ardleigh (Essex 47,2), Fordham (Essex 47,3), and Liston (Essex 47,1). Data created by Professor J. J. N. Palmer and team at the University of Hull. [Open Domesday]
- Domesday Book, Little Domesday vol. ii, p. 89 (Essex): Liston, Fordham, Ardleigh. [Domesday]
```

### 6.3 Revise relevant open question

Current open question:

```markdown
2. **Norfolk Domesday entries:** The fact sheet says "Norfolk manors" without specifics. The Domesday Book Norfolk entries for "Hugo de Gournai" should be searched in Open Domesday to identify which Norfolk manors, if any, are attributed to Hugh III vs. later family members.
```

Keep it, but add:

```markdown
   The Essex entries have now been extracted from Open Domesday; this remaining item is specifically about any Norfolk attribution and potential confusion with other Hugh/Nigel of Gournay entries.
```

---

## 7. `research/places/hardingham.md`

### 7.1 Add a new section after `## Why this place matters structurally`

```markdown
## Local place-name and manor tradition

The Hardingham parish history page supplies useful local-place context for the Swathings / Gurneys material. It states that Hardingham itself is not named in Domesday, though Flockthorpe is; that an outlier called "Mantatestone" is now Manson Green; and that another outlier, "Swathing," is now Low Street. This gives a concrete modern geolocation clue for Swathing: **Low Street, Hardingham**.[^hardingham-parish]

The same account says that between 1066 and 1210 there were two lordships: the De Camois family held the Manor of Flockthorpe, while the second was the **Manor of Gurneys & Swathing**. It further states that in 1210 Flockthorpe became Hardingham. This is local-history wording rather than a manorial record, but it is directly relevant to the Gurney place file because it names the Gurneys & Swathing manor as one of the two early lordship structures.[^hardingham-parish]

The page also preserves useful landscape context: the parish acreage is given as 2,418 acres; the Roundabout moat at Gresham Farm is estimated to date from 1066-1539 and is described as near the center of the village; the Old Hall opposite the church is considered late sixteenth century; and the modern village includes Low Street, Danemoor, Manson Green, Nordelph Corner, Hackford Road, and High Common.[^hardingham-parish]

[^hardingham-parish]: Hardingham Parish Council / Hardingham Parish website, "History of Hardingham," accessed 26 April 2026, https://hardinghamparish.wixsite.com/home/history-of-hardingham-1. Source ID: `hardingham-parish-history-2026`.
```

### 7.2 Revise `## Primary-source hooks`

Add this bullet:

```markdown
- Hardingham Parish Council / parish website history page — local place-name and manor tradition identifying Swathing with Low Street and naming the Manor of Gurneys & Swathing.
```

### 7.3 Revise `## Open items`

Add:

```markdown
- Cross-check the Hardingham Parish history statement on "Manor of Gurneys & Swathing" against Blomefield, Norfolk Heritage Explorer, and manorial records.
- Geolocate Swathing / Low Street within Hardingham for the place registry if the repository later tracks sub-place coordinates.
```

### 7.4 Revise `## Sources`

Add:

```markdown
- Hardingham Parish Council / Hardingham Parish website, "History of Hardingham," accessed 26 April 2026. [Hardingham Parish]
```

---

## 8. Optional structured data updates

### 8.1 `data/places.json` / `data/places_detail.json`

No mandatory schema change is required for this patchset if the repo does not yet model sub-places.

If applying a richer place-detail update, revise the Hardingham detail text for `place-hardingham-norfolk-england` to include:

```text
Swathings in Hardingham, a long-running junior-line holding documented from the Henry II period onward; local parish history identifies Swathing with modern Low Street and describes the early Manor of Gurneys & Swathing.
```

Do not synthesize new coordinates for Low Street unless a separate geocoding source is added.

### 8.2 `data/ancestors v26.json`

Locate the G33 Hugh de Gournay III record by `"gen": "G33"` and `"name": "Hugh de Gournay III"`.

If the current `"landHoldings"` field is brief, revise to something like:

```json
"landHoldings": "Gournay-en-Bray; English Domesday tenant-in-chief at Ardleigh, Fordham, and Liston in Essex/Suffolk, confirmed in Open Domesday as three post-Conquest holdings of Hugh of Gournay."
```

If the current `"summary"` field references Domesday holdings only generically, append:

```text
Open Domesday identifies his three post-Conquest tenant-in-chief holdings as Ardleigh, Fordham, and Liston.
```

Do not add long valuation data inside JSON; that belongs in the G33 companion and place files.

### 8.3 Site mirrors

If the site still relies on checked-in mirrors, copy updated canonical content to:

```text
site/website/research/companions/g13-john-gurney-fact-sheet.md
site/website/key-research/john-gurney-case-file.md
site/website/research/companions/g33-hugh-de-gournay-iii-fact-sheet.md
```

Only mirror files that correspond to canonical files actually changed. Do not edit generated `_data/*.json` by hand unless that is current repo practice.

---

## 9. Validation checklist

Run:

```bash
python -m json.tool data/sources.json >/tmp/sources-json-check.json

grep -R "bates-ancient-iron-works-braintree-1898\|open-domesday-powell-smith\|hardingham-parish-history-2026" -n \
  data research sources site | head -100
```

Manual checks:

- `research/people/g13-john-gurney-fact-sheet.research.md` now preserves the full useful John Gurney 1661 property description and occupation "Taylor."
- `research/places/braintree-ma.md` now has narrative content above the generated registry block.
- `research/places/ardleigh.md`, `fordham.md`, and `liston.md` no longer say the Domesday entries have not been pulled; each now has Open Domesday details and a remaining folio/Phillimore verification item only.
- `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` now summarizes all three Open Domesday entries.
- `research/places/hardingham.md` includes Swathing = Low Street and the Manor of Gurneys & Swathing language, while preserving that this is local-history evidence needing manorial cross-check.
- `data/sources.json` remains valid JSON and all newly used source IDs exist.


---

# Addendum v02.1 — requested case-file and Hardingham geolocation additions

This addendum is part of the same patchset and should be applied in addition to all v02 changes above.

## 10. `research/case-files/john-gurney-case-file-v4.md`

### 10.1 Section 1 baseline table: add Bates as an additional tailor source

In section 1, locate the baseline table row:

```markdown
| **Occupation** | Tailor | Sprague, p. 695 |
```

Replace with:

```markdown
| **Occupation** | Tailor | Sprague, p. 695; Bates, p. 10 |
```

Then, in the same section's citation index, add a new footnote for the Bates occupation/property source. Because the case file uses manually numbered HTML endnotes, use the next available number after `n65`, unless another patch has already added later notes. If applying to the inspected file, add `n66`:

```html
  <li id="n66">Samuel A. Bates, <em>The Ancient Iron Works at Braintree, Mass.: The First in America</em> (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, 12 Feb. 1661 conveyance in which "John Gurney, Taylor" conveyed property to Richard Thayer. Source ID: <code>bates-ancient-iron-works-braintree-1898</code>. <a class="backref" href="#ref-66">↩</a></li>
```

If the row is revised to include a visible footnote marker, use:

```markdown
| **Occupation** | Tailor | Sprague, p. 695; Bates, p. 10<sup class="fn"><a href="#n66" id="ref-66">66</a></sup> |
```

### 10.2 Section 1 baseline table: estate/property sentence

In section 1, immediately after the baseline table and before the paragraph beginning `**Key identifiers for matching:**`, add:

```markdown
The estate figure should be read alongside his Braintree land record: although John died intestate with a modest £55.14.6 estate, Bates preserves a 12 February 1661 conveyance in which "John Gurney, Taylor" sold Richard Thayer a house and orchard, a five-acre parcel on the Monoticot River, and an additional half-acre parcel west of that lot for £14.<sup class="fn"><a href="#n66" id="ref-66a">66</a></sup>
```

This satisfies the section-1 request for an additional estate/property sentence and ties the occupation witness to the property record.

### 10.3 Section 3 master timeline: add 1661 property detail

In section 3 master timeline, locate:

```markdown
| 12 Feb 1661 | — | Sells land in Braintree (deed witnessed by son John Jr.) |
```

Replace with:

```markdown
| 12 Feb 1661 | — | Sells Braintree property to Richard Thayer for £14: a house and orchard, five acres bounded south by the Monoticot River, and a separate half-acre parcel; deed styles him "John Gurney, Taylor." |
```

### 10.4 Section 13 bibliography / primary sources: add Bates as a secondary source

In section 13.3 Secondary Sources, append:

```markdown
• Bates, *The Ancient Iron Works at Braintree* (1898), p. 10, for the 12 Feb. 1661 Braintree conveyance identifying John Gurney as tailor and describing the house/orchard, five-acre parcel, and half-acre parcel sold to Richard Thayer.
```

If the punctuation style is being normalized, the resulting paragraph should read:

```markdown
Davis, *Ancestry of Abel Lunt* (1963). • Laslett, *World We Have Lost* (1965). • Fischer, *Albion's Seed* (1989). • Anderson, *New England's Generation* (1991). • Gibson & Dell, *Protestation Returns* (1995/2004). • VCH Bucks Vol. 3. • NPS Cultural Landscape Report, Adams NHP. • Bates, *The Ancient Iron Works at Braintree* (1898), p. 10, for the 12 Feb. 1661 Braintree conveyance identifying John Gurney as tailor and describing the house/orchard, five-acre parcel, and half-acre parcel sold to Richard Thayer.
```

### 10.5 Site mirror

If the site layer still mirrors the case file, copy the updated canonical file to:

```text
site/website/key-research/john-gurney-case-file.md
```

---

## 11. Additional update to `research/people/g13-john-gurney-fact-sheet.research.md`

The base v02 patchset already updates this file's land/property table and adds a `#### 1661 Braintree conveyance to Richard Thayer` subsection. Strengthen that subsection with the full quote, as requested.

### 11.1 Replace the proposed v02 subsection with this fuller version

Replace the v02 block titled `#### 1661 Braintree conveyance to Richard Thayer` with:

```markdown
#### 1661 Braintree conveyance to Richard Thayer

The 12 February 1661 Braintree deed is another direct occupation witness: Bates prints the grantor as "John Gurney, Taylor." It also gives a fuller property description than the current summary preserves.[^bates-ironworks-gurney]

> Feb. 12, 1661, John Gurney, Taylor, conveyed to Richard Thayer for fourteen pounds, one house and orchard on which the house stands, five acres of land bounded south on Monoticot river; east on Richard Thayer, Nathaniel Mott and John[— ? — ]; north on Simon Crosby; west on George Aldridge. Also one-half acre west of the last lot, river on the south, highway on the north, George Aldrich on the east.

Bates continues with neighbor context, noting that Nathaniel Mott was killed by Indians in 1675 and that George Aldrich and Daniel Lovett removed. The deed is useful because it independently repeats John's trade and places his Braintree property in a named neighborhood network: Richard Thayer, Nathaniel Mott, Simon Crosby, George Aldridge/Aldrich, and an unclear John-name neighbor.[^bates-ironworks-gurney]

[^bates-ironworks-gurney]: Samuel A. Bates, *The Ancient Iron Works at Braintree, Mass.: The First in America* (South Braintree, Mass.: Frank A. Bates, 1898), p. 10, quoting the 12 Feb. 1661 conveyance from John Gurney to Richard Thayer. Source ID: `bates-ancient-iron-works-braintree-1898`.
```

### 11.2 Keep the v02 land/property table revision

Retain the v02 replacement row:

```markdown
| 12 Feb 1661 | Braintree land sale | John Gurney, identified as "Taylor," conveyed to Richard Thayer for £14 a house and orchard, a five-acre parcel on the Monatiquot/Monoticot River, and an additional half-acre parcel west of the first lot. | Bates, *Ancient Iron Works at Braintree*, p. 10; Braintree deed records |
```

---

## 12. Hardingham geolocation addition

The base v02 patchset adds Swathing = Low Street as a geolocation clue in the Hardingham place file. This addendum promotes the user-supplied coordinate for Low Street.

### 12.1 `research/places/hardingham.md`: revise the new local place-name section

In the v02-added section `## Local place-name and manor tradition`, replace the first paragraph with:

```markdown
The Hardingham parish history page supplies useful local-place context for the Swathings / Gurneys material. It states that Hardingham itself is not named in Domesday, though Flockthorpe is; that an outlier called "Mantatestone" is now Manson Green; and that another outlier, "Swathing," is now Low Street. This gives a concrete modern geolocation clue for Swathing: **Low Street, Hardingham**, with working coordinate **52.611538, 1.020105**.[^hardingham-parish]
```

### 12.2 `research/places/hardingham.md`: add a specific geolocation note

Immediately after the v02-added section `## Local place-name and manor tradition`, add:

```markdown
## Swathing / Low Street geolocation

For working map purposes, use **52.611538, 1.020105** as the low-precision coordinate for Swathing / Low Street, Hardingham. This coordinate should be treated as a modern hamlet-road locator, not as the proven medieval manor-house site. The evidentiary chain is: Hardingham parish history identifies Swathing with modern Low Street; the coordinate places the Low Street locality in the Hardingham landscape.[^hardingham-parish]
```

### 12.3 `data/places.json` / `data/places_detail.json`

No mandatory new place ID is required if the repo is not yet modeling sub-places. If a sub-place is added, create it deliberately rather than overloading `place-hardingham-norfolk-england`.

Recommended optional new place record:

```json
{
  "placeId": "place-swathing-low-street-hardingham-norfolk-england",
  "name": "Swathing / Low Street, Hardingham, Norfolk, England",
  "shortDescription": "Swathing / Low Street locality",
  "placeType": "sub-locality",
  "aliases": ["Swathing", "Low Street", "Low Street, Hardingham"],
  "coordinate": {
    "lat": 52.611538,
    "lon": 1.020105,
    "precision": "low"
  },
  "roles": ["landholding / property reference"],
  "detail": "Hardingham parish history identifies Swathing, associated with the Manor of Gurneys & Swathing, with modern Low Street. Coordinate is a working modern Low Street locality marker, not a proven medieval manor-house site.",
  "currentSiteStatus": "working modern locality marker",
  "sourceIds": ["hardingham-parish-history-2026"]
}
```

If using the existing two-layer model, place the compact registry entry in `data/places.json` and any richer `detail`, `evidence`, or `notes` fields in `data/places_detail.json`, matching existing schema conventions.

### 12.4 `research/places/hardingham.md`: revise open items

In addition to the v02 open item:

```markdown
- Geolocate Swathing / Low Street within Hardingham for the place registry if the repository later tracks sub-place coordinates.
```

replace it with:

```markdown
- Decide whether Swathing / Low Street should become a separate sub-place in `data/places.json` using working coordinate 52.611538, 1.020105, or remain a note under `place-hardingham-norfolk-england`.
```

### 12.5 Validation note addition

In `sources/validations/hardingham-parish-history-2026.md`, add under **Scope checked** or **Limitations**:

```markdown
**Geolocation note:** The working coordinate 52.611538, 1.020105 was supplied for modern Low Street, Hardingham. Use as a low-precision locality marker only. The parish history supports the identification Swathing = Low Street, but it does not prove the exact medieval manor-house location.
```

---

## 13. Updated validation checklist

Add these checks to the v02 validation checklist:

```bash
grep -R "Bates, p. 10\|John Gurney, Taylor\|Monoticot\|52.611538\|1.020105" -n \
  research data sources site | head -100
```

Manual checks:

- `research/case-files/john-gurney-case-file-v4.md` section 1 now includes Bates as an occupation source.
- Section 1 also has a sentence linking the modest estate to the 1661 Braintree property sale.
- Section 3 timeline includes the fuller 12 Feb. 1661 property/occupation entry.
- `research/people/g13-john-gurney-fact-sheet.research.md` preserves the full useful Bates quotation, not just a summary.
- Hardingham research file includes `52.611538, 1.020105` as a low-precision Swathing / Low Street working coordinate.
```
