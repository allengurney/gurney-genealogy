# Intake patchset v03.1 — Gurney’s Manor, Hingham / Harpley conflation; Great Ellingham Old Hall NHER

**Prepared:** 2026-04-26  
**Repo:** `allengurney/gurney-genealogy`  
**Repo ref inspected:** `main` @ `edbfe2d9a7207bd5f5ccab9583c4fadaaaec3ba1`  
**Patchset destination when applied:** `sources/intake/processed/v03.patchset.md`

## Scope

This redo supersedes `v03-gurneys-manor-great-ellingham-nher.patchset.md`.

It keeps all prior v03 changes and removes the earlier “capture pending” treatment for MNF9108 because the full Norfolk Heritage Explorer record text has now been supplied in the intake and is included below.

Promote both intake items:

1. **The DiCamillo Companion — Gurney’s Manor**  
   Place evidence for **Gurney’s Manor at Hingham, Norfolk**, with user-supplied coordinate `52.571755298216836, 0.9756833626995299`.

2. **Norfolk Historic Environment Record / Norfolk Heritage Explorer — Old Hall, Great Ellingham, NHER MNF9108**  
   Strong government-source evidence for **Old Hall, Great Ellingham**, with coordinate `52.5319, 0.9808`, map URL, parish summary URL, full record text, monument types, protected status, and source list.

## Source-access note

- The DiCamillo page was web-readable and supplied the Hingham Gurney’s Manor entry.
- The Norfolk Heritage Explorer parish summary was web-readable and independently corroborates the key Gurney sentence: Old Hall (NHER 9108) was built in the mid-sixteenth century for one of the Gurney family and stands on an earlier moated manor site.
- The full MNF9108 record text is now supplied in the intake and is included in `sources/corpus_supplement/nher-mnf9108-old-hall-great-ellingham.md`. Do not leave any “full record capture pending” caveat in this patchset.

---

## 1. `data/sources.json`

### 1.1 Update metadata date

Change the current prior value to:

```json
"lastUpdated": "2026-04-26"
```

### 1.2 Add source entry: DiCamillo — Gurney’s Manor

Insert near Norfolk place / Historic England / Blomefield sources:

```json
    "dicamillo-gurneys-manor": {
      "shortTitle": "DiCamillo — Gurney's Manor",
      "citation": "DiCamillo, Curt. \"Gurney's Manor.\" The DiCamillo Companion to British & Irish Country Houses.",
      "archive": "The DiCamillo Companion online house entry",
      "url": "https://www.thedicamillo.com/house/gurneys-manor/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/dicamillo-gurneys-manor.md",
      "mediaPath": null,
      "validationPath": "sources/validations/dicamillo-gurneys-manor.md",
      "notes": "Country-house entry for Gurney's Manor, Hingham, Norfolk. DiCamillo identifies the house as fully extant, Grade II, private, circa 1600 with circa 1700 and 1826 alterations/additions, with earliest elements possibly dating to the 1570s. Useful to correct any conflation between Hingham Gurney's Manor and Harpley."
    },
```

### 1.3 Add source entry: NHER MNF9108 Old Hall, Great Ellingham

```json
    "nher-mnf9108-old-hall-great-ellingham": {
      "shortTitle": "NHER MNF9108 — Old Hall, Great Ellingham",
      "citation": "Norfolk Historic Environment Service. \"MNF9108 — Old Hall, Great Ellingham.\" Norfolk Heritage Explorer.",
      "archive": "Norfolk Heritage Explorer / Norfolk Historic Environment Record",
      "url": "https://www.heritage.norfolk.gov.uk/record-details?MNF9108",
      "corpusStatus": "full",
      "corpusPath": "sources/corpus_supplement/nher-mnf9108-old-hall-great-ellingham.md",
      "mediaPath": null,
      "validationPath": "sources/validations/nher-mnf9108-old-hall-great-ellingham.md",
      "notes": "Government historic-environment record for Old Hall, Great Ellingham. Describes a medieval moated manorial site with a mid-16th-century great house within the main moat, additional moated enclosures and fishponds, 16th-century and 17th/18th-century barns, Grade II listing, and the statement that the first-floor hall is mid-16th century, said to be 1573 by Henry Gurney. Coordinate: 52.5319 N, 0.9808 E."
    },
```

### 1.4 Add source entry: NHER Great Ellingham parish summary

```json
    "nher-great-ellingham-parish-summary": {
      "shortTitle": "NHER Parish Summary — Great Ellingham",
      "citation": "Norfolk Historic Environment Service. \"Parish Summary: Great Ellingham.\" Norfolk Heritage Explorer. Piet Aldridge, 6 April 2006.",
      "archive": "Norfolk Heritage Explorer parish summary",
      "url": "https://www.heritage.norfolk.gov.uk/record-details?TNF342-Parish-Summary-Great-Ellingham-(Parish-Summary)",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/nher-great-ellingham-parish-summary.md",
      "mediaPath": null,
      "validationPath": "sources/validations/nher-great-ellingham-parish-summary.md",
      "notes": "Norfolk Heritage Explorer parish summary for Great Ellingham. Important contextual source for Great Ellingham's long occupation history, medieval church and residential buildings, and Old Hall (NHER 9108), described as a mid-16th-century house built for one of the Gurney family on the site of an earlier moated manor."
    },
```

---

## 2. New corpus / validation files

### 2.1 Create `sources/corpus_supplement/dicamillo-gurneys-manor.md`

```markdown
# DiCamillo — Gurney's Manor, Hingham, Norfolk

**Source ID:** `dicamillo-gurneys-manor`

**Citation:** Curt DiCamillo, "Gurney's Manor," *The DiCamillo Companion to British & Irish Country Houses*.

**URL:** https://www.thedicamillo.com/house/gurneys-manor/

## Extract

- Name: Gurney's Manor
- Place: Hingham, Norfolk, England
- Circa date: circa 1600 with circa 1700 and 1826 alterations and additions
- Status: fully extant
- House open to public: no
- Country house: yes
- House and family history: Gurney's Manor presents today as a red brick Georgian house, though its earliest elements may date to the 1570s.
- Bibliography: John Kenworthy-Browne, Peter Reid, Michael Sayer, and David Watkin, *Burke's & Savills Guide to Country Houses, Volume III: East Anglia* (London: Burke's Peerage, 1981), p. 123.
- Listings: house listed Grade II; park not listed.
- Past seat/home of: Hurnard family until circa 1920; T. J. A. Denny, late twentieth century.
- Current ownership type: individual / family trust.
- Primary current ownership use: private home.

## Research value

This is place evidence for Gurney's Manor at **Hingham**, not Harpley. It supports the existing Hingham place file's treatment of Gurney's Manor as a later Tudor / early Stuart physical survival and helps correct possible conflation in the Harpley place registry, where "Gurney's manor" language may be read as referring to the Hingham house.
```

### 2.2 Create `sources/validations/dicamillo-gurneys-manor.md`

```markdown
# Source validation: DiCamillo — Gurney's Manor

**Source ID:** `dicamillo-gurneys-manor`

**Source examined:** Curt DiCamillo, "Gurney's Manor," *The DiCamillo Companion to British & Irish Country Houses*.

**Scope checked:** Full accessible page text.

**Finding destinations:** `research/places/hingham-norfolk.md`; `research/places/harpley.md` as a conflation caution.

**Validation result:** Good for country-house identification, built-site description, listing/status context, approximate architectural dating, and bibliography.

**Limitations:** DiCamillo is a country-house reference site, not a manorial descent proof. Use for built-site identification and bibliography. Use Blomefield, Historic England, deeds, or manorial records for formal ownership/descent claims.
```

### 2.3 Create `sources/corpus_supplement/nher-mnf9108-old-hall-great-ellingham.md`

```markdown
# NHER MNF9108 — Old Hall, Great Ellingham

**Source ID:** `nher-mnf9108-old-hall-great-ellingham`

**Citation:** Norfolk Historic Environment Service, "MNF9108 — Old Hall, Great Ellingham," *Norfolk Heritage Explorer*.

**URL:** https://www.heritage.norfolk.gov.uk/record-details?MNF9108

**Map URL:** https://www.heritage.norfolk.gov.uk/map-record?scale=3385.5001277302295&lon=108065.87938898&lat=6896386.9675375&baseMapID=OSM&ck_MON1=true&ck_MON=true

**Coordinate:** 52.5319, 0.9808

## Record details

- NHER Number: 9108
- Type of record: Monument
- Name: Old Hall

## Summary

Medieval moated manorial site, with mid 16th century great house within the main moat. The remains of additional moated enclosures and fishponds are either extant earthworks or visible as partially levelled cropmarks. The great house, now a farmhouse, is timber framed with wattle and daub infill, the central part has two stories and the two cross wings of three storeys give the house a U-shaped plan. To the rear is an 18th century timber framed extension.

## Images

None.

## Location

- Grid Reference: TM 0161 9651
- Map Sheet: TM09NW
- Parish: Great Ellingham, Breckland, Norfolk

## Full description

Medieval moated site, mostly well preserved.

House is interesting and complex. First floor hall, mid 16th century (said to be 1573, by Henry Gurney) with well beneath floor and service extension with jettied (?) solar above.

Altered about 1590 with grand Elizabethan staircase, north crosswing and mullioned windows. Solar extended either at same time and later rebuilt, or extended late 17th century, to form south wing. Rear outshut 18th century.

Barn to southeast 16th century. Barn to northwest 17th/18th century.

See report (S1) in file. Architect's plans (S2) in file, as are press cuttings (S3), (S4), (S5) and (S6). Hall and the two barns are listed grade II, (S7).

E. Rose (NAU), 21 April 1988.

The central grid reference for this site has been altered from TM 0163 9648 to TM 0161 9653.

January 2013. Norfolk NMP.

The site of a medieval moated complex and Hall is visible on aerial photographs (S8-S10). The main component of the site consists of surviving moats and fish ponds (not mapped as depicted on modern Ordnance Survey mapping). The aerial photographs reveal the cropmark and earthwork traces of an additional substantial moated enclosure to the north of the main moat surrounding the Hall. The overall site is centred on TM 0161 9653, although the newly identified main moated components visible on the aerial photographs are centred on TM 0160 9659.

Although showing most clearly on the aerial photographs as lodged or very clear cropmarks, traces of the formerly substantial earthworks would appear to still present on the ground. The moated enclosure would have measured approximately 80m by 60m and was defined by broad ditches and accompanying banks. The Ordnance Survey Second Edition map (1902-8, 25 inch) map indicates that the eastern arm of the moat persisted as a relatively minor drainage channel until relatively recently.

S. Horlock (NMP), 24 January 2013.

## Monument types

- Fishpond (Medieval — 1066 AD to 1539 AD)
- Moat (Medieval — 1066 AD to 1539 AD)
- Barn (Post Medieval — 1540 AD to 1900 AD)
- Great House (Post Medieval — 1540 AD to 1900 AD)

## Associated finds

None.

## Protected status

- Listed Building
- Listed Building

## Sources and further reading

- Aerial Photograph: TM0196A-H.
- Record Card: Ordnance Survey Staff. 1933-1979?. Ordnance Survey Record Cards. TM 09 NW 9 [4].
- Record Card: NAU Staff. 1974-1988. Norfolk Archaeological Index Primary Record Card.
- Secondary File: Secondary File.
- Record Card: Clarke, R. R. and NCM Staff. 1933-1973. Norwich Castle Museum Record Card — Post-Medieval. Ellingham (Great).
- Collection: Norfolk Historic Environment Record Staff. 1975-[2000]. HER Record Notes. Norfolk Historic Environment Service.
- S1: Unpublished Document: Rose, E. NAU. 1988. Building Report. Building Report.
- S2: Illustration: Various. Various. Architectural plans.
- S3: Newspaper Article: *Diss Express*. 1986. [Sale advertisement for Gt. Ellingham Hall]. 3 October.
- S4: Newspaper Article: *Eastern Daily Press*. 1986. [Sale advertisement for Great Ellingham Hall]. 7 November.
- S5: Newspaper Article: *Eastern Daily Press*. 1993. [Sale advertisements for Great Ellingham Hall]. 16 April.
- S6: Newspaper Article: *Eastern Daily Press*. 2001. Records show history of hall. 16 July.
- S7: Designation: Historic England. National Heritage List for England. List Entry 1077567 and 1342457.
- S8: Oblique Aerial Photograph: Edwards, D. A. (NLA). 1976. NHER TM 0196A-C (NLA/54/AKR20-22) 01-AUG-1977.
- S9: Vertical Aerial Photograph: Ordnance Survey. 1976. OS/76018 132-3 19-APR-1976 (NMR).
- S10: Vertical Aerial Photograph: BKS Surveys Limited. 1988. BKS 8814-5 06-AUG-1988 (NCC 2002-3).

## Related records

None.

## Find out more

Parish Summary: Great Ellingham (Parish Summary).

## Research value

This is an outstanding source for Great Ellingham because it ties the Gurney family to a specific surviving / recordable historic-environment site: a medieval moated manorial complex with a mid-sixteenth-century great house, said to be 1573 by Henry Gurney, later altered in the Elizabethan period, with additional moated enclosures, fishponds, barns, aerial-photo evidence, and Grade II protected status. The record is much stronger than a generic county-history statement and should be treated as core place evidence.
```

### 2.4 Create `sources/validations/nher-mnf9108-old-hall-great-ellingham.md`

```markdown
# Source validation: NHER MNF9108 — Old Hall, Great Ellingham

**Source ID:** `nher-mnf9108-old-hall-great-ellingham`

**Source examined:** Norfolk Heritage Explorer record MNF9108; full record text supplied in intake.

**Scope checked:** Record details, summary, location, full description, monument types, protected status, source list, map URL, and parish-summary relationship.

**Finding destination:** `research/places/great-ellingham.md`.

**Coordinate:** 52.5319, 0.9808.

**Grid reference:** TM 0161 9651; site-centre note also gives TM 0161 9653 after correction from TM 0163 9648.

**Map URL:** https://www.heritage.norfolk.gov.uk/map-record?scale=3385.5001277302295&lon=108065.87938898&lat=6896386.9675375&baseMapID=OSM&ck_MON1=true&ck_MON=true

## Validation result

Strong source. This is a government historic-environment record from Norfolk Historic Environment Service. It supports:

- Old Hall as NHER 9108.
- Old Hall as a medieval moated manorial site.
- A mid-sixteenth-century great house within the main moat.
- House construction details: timber frame, wattle and daub, two-storey central part, three-storey cross wings, U-shaped plan, 18th-century rear extension.
- A mid-sixteenth-century first-floor hall, said to be 1573 by Henry Gurney.
- Alterations c.1590 and later.
- 16th-century and 17th/18th-century barns.
- Additional moated enclosures and fishponds visible as earthworks/cropmarks.
- Grade II listing for the hall and two barns.
- Historic England list entries 1077567 and 1342457 as further targets.

## Limitations / next checks

- The statement "said to be 1573, by Henry Gurney" should be used with the qualifier "said to be" unless the cited 1988 building report or NHLE record supplies firmer wording.
- Pull Historic England list entries 1077567 and 1342457 for architectural detail and protected-status confirmation.
- If possible, obtain the E. Rose (NAU) 1988 building report and architect's plans from the NHER file.
```

### 2.5 Create `sources/corpus_supplement/nher-great-ellingham-parish-summary.md`

```markdown
# NHER Parish Summary — Great Ellingham

**Source ID:** `nher-great-ellingham-parish-summary`

**Citation:** Norfolk Historic Environment Service, "Parish Summary: Great Ellingham," *Norfolk Heritage Explorer*, Piet Aldridge, 6 April 2006.

**URL:** https://www.heritage.norfolk.gov.uk/record-details?TNF342-Parish-Summary-Great-Ellingham-(Parish-Summary)

## Extract

The Breckland parish of Great Ellingham is situated in the southern part of Norfolk, next to Attleborough, about ten miles southwest of Norwich. The parish name comes from Old English for "the homestead of Ella's or Eli's people." The parish was established by the time of the Norman Conquest, and its population, land ownership, and productive resources were recorded in Domesday Book in 1086.

The parish summary describes evidence from the Palaeolithic through the Roman and Saxon periods, including flint tools, prehistoric burnt flint scatters, Bronze Age barrow remains and finds, Roman building-material and pottery concentrations, and Saxon finds such as tweezers, a sword pommel, brooches, an unusual key, and a wrist clasp.

For the medieval period, the summary identifies St James the Great's Church (NHER 4259) as the parish's oldest surviving building, mainly fourteenth century, with chequered flintwork, a battlemented west tower with lead spire, a fourteenth-century octagonal font with original lead lining, part of a fifteenth-century painted screen, and medieval wall paintings. It also notes medieval-origin residential buildings: Mill Farmhouse (NHER 24605), Tannery Farm (NHER 30928), and Ye Olde Thatche Shoppe (NHER 40344). It notes a moated-manor site at NHER 34571 and the vanished Tofts deserted medieval village (NHER 11925).

For the post-medieval period, the summary states:

> Of the surviving post medieval buildings in the parish, probably the oldest is Old Hall (NHER 9108). Built in the mid 16th century for one of the Gurney family, this is a house of great character and history, standing on the site of an earlier moated manor.

It also identifies Bury Hall (NHER 34180), Manor Farmhouse (NHER 35184), Rose Farmhouse (NHER 19427), Portwood Farm (NHER 17170), Church Farmhouse (NHER 23620), the Old Queen's Head (NHER 40806), a nineteenth-century brick tower mill south of Church Street (NHER 4258), and Deopham Green Airfield (NHER 4260).

## Research value

The Old Hall sentence is the primary Gurney-relevant value. The broader parish summary is useful context because it places Old Hall among Great Ellingham's medieval and post-medieval landscape: church, surviving medieval-origin houses, moated sites, and later manor/farm buildings.
```

### 2.6 Create `sources/validations/nher-great-ellingham-parish-summary.md`

```markdown
# Source validation: NHER Great Ellingham parish summary

**Source ID:** `nher-great-ellingham-parish-summary`

**Source examined:** Norfolk Heritage Explorer, "Parish Summary: Great Ellingham."

**Scope checked:** Full accessible page text.

**Finding destination:** `research/places/great-ellingham.md`.

**Validation result:** Useful and strong as a Norfolk Historic Environment Service parish-level synthesis. It independently corroborates that Old Hall (NHER 9108) was built in the mid-sixteenth century for one of the Gurney family and stands on an earlier moated manor site.

**Limitations:** Parish summaries are intentionally overviews; the page itself says they provide selected examples and are not detailed documentary research. Use the summary for context and for identifying NHER records to pull, but use the individual NHER record and primary/architectural sources for site-level detail.
```

---

## 3. `research/places/hingham-norfolk.md`

### 3.1 Replace `## Surviving physical site`

Replace the current section with:

```markdown
## Surviving physical site

The greatest value of Hingham in the present project is the survival of **Gurney's Manor** itself. DiCamillo identifies Gurney's Manor as a fully extant Grade II country house at Hingham, Norfolk: circa 1600, with circa 1700 and 1826 alterations/additions, and with earliest elements possibly dating to the 1570s. The house is private, not open to the public, and now presents as a red-brick Georgian house.[^dicamillo-gurneys-manor]

Use working coordinate **52.571755298216836, 0.9756833626995299** for the Gurney's Manor physical-site marker. This coordinate is close to Hingham and is not close to Harpley; therefore it should be treated as evidence that the DiCamillo/Historic England-style "Gurney's Manor" site belongs in the Hingham place file, not the Harpley place file.[^dicamillo-gurneys-manor]

That makes Hingham one of the rare places in the England set where the surviving built environment can still be tied closely to a named Gurney possession in the Tudor/Stuart transition. It remains a built-site witness, not by itself a full manorial-descent proof; Blomefield and manorial records remain the better sources for ownership chronology.

[^dicamillo-gurneys-manor]: Curt DiCamillo, "Gurney's Manor," *The DiCamillo Companion to British & Irish Country Houses*, https://www.thedicamillo.com/house/gurneys-manor/. Source ID: `dicamillo-gurneys-manor`.
```

### 3.2 Revise `## Open items`

Replace:

```markdown
- [ ] Add the Historic England list entry number and full building description directly into this file.
```

with:

```markdown
- [ ] Add the Historic England list entry number and full building description directly into this file, and reconcile it with the DiCamillo description.
```

### 3.3 Revise `## Sources`

Add:

```markdown
- Curt DiCamillo, "Gurney's Manor," *The DiCamillo Companion to British & Irish Country Houses*. [DiCamillo]
```

### 3.4 Revise generated place-registry block, if hand-editing generated content is acceptable

If generated blocks are permitted to be hand-updated, change:

```markdown
- Coordinate: 52.5764, 0.9656821626060168 (medium)
```

to:

```markdown
- Coordinate: 52.571755298216836, 0.9756833626995299 (medium)
```

and change:

```markdown
- Current-site status: unknown
```

to:

```markdown
- Current-site status: extant private Grade II country house; not open to public
```

If generated blocks are not hand-edited, leave the generated block and make the coordinate/status update in `data/places.json` / `places_detail.json` instead.

---

## 4. `research/places/harpley.md`

### 4.1 Add conflation caution after `## Interpretive note`

Insert:

```markdown
## Gurney's Manor name caution

Do not conflate Harpley's medieval Gurney manor with **Gurney's Manor, Hingham**. The DiCamillo Companion's Gurney's Manor entry is explicitly for Hingham, Norfolk, gives a Hingham-area location, and describes a fully extant Grade II country house with earliest elements possibly dating to the 1570s. That site is geographically separate from Harpley and belongs in `research/places/hingham-norfolk.md`.[^dicamillo-gurneys-manor-harpley]

Harpley remains a major medieval and Tudor Gurney manor, but the phrase "Gurney's manor in Harpley" should be used descriptively, not as a proper-name reference to the extant Hingham house.

[^dicamillo-gurneys-manor-harpley]: Curt DiCamillo, "Gurney's Manor," *The DiCamillo Companion to British & Irish Country Houses*, https://www.thedicamillo.com/house/gurneys-manor/. Source ID: `dicamillo-gurneys-manor`.
```

### 4.2 Revise generated place registry detail, if hand-editing generated content is acceptable

Current registry detail says:

```markdown
- Detail: Gurney's manor in Harpley, acquired c.1183 through Rose de Burnham and the Hameline de Warenne connection.
```

Replace with:

```markdown
- Detail: Harpley manor, a major medieval Gurney holding acquired c.1183 through Rose de Burnham and the Hameline de Warenne connection; do not conflate with the extant Gurney's Manor at Hingham.
```

If generated blocks are not hand-edited, revise `data/places.json` / `places_detail.json` instead.

### 4.3 Revise `## Open items`

Add:

```markdown
- Audit any generated display text that says "Gurney's manor in Harpley" so it cannot be mistaken for the extant Gurney's Manor at Hingham.
```

---

## 5. `research/places/great-ellingham.md`

### 5.1 Revise opening coordinate line

Change:

```markdown
Village in south-central Norfolk. Coordinates: **52.5453, 1.0091774978679044**.
```

to:

```markdown
Village in south-central Norfolk. Place coordinate: **52.5453, 1.0091774978679044**. Old Hall / NHER 9108 working coordinate: **52.5319, 0.9808**.
```

This preserves the broader village coordinate while adding the Old Hall site coordinate.

### 5.2 Add new section after `## Later descent`

```markdown
## Old Hall and the Gurney built landscape

Norfolk Heritage Explorer's **MNF9108** record identifies Old Hall as a medieval moated manorial site with a mid-sixteenth-century great house within the main moat. It describes additional moated enclosures and fishponds as extant earthworks or partially levelled cropmarks. The great house, now a farmhouse, is timber framed with wattle and daub infill; the central part has two storeys, and the two cross wings have three storeys, giving the house a U-shaped plan. The rear has an eighteenth-century timber-framed extension.[^nher-mnf9108-old-hall]

The detailed description is especially valuable for the Gurney line. It calls the house "interesting and complex" and describes a first-floor hall, mid-sixteenth century, "said to be 1573, by Henry Gurney," with a well beneath the floor and a service extension with jettied or possibly jettied solar above. The house was altered about 1590 with a grand Elizabethan staircase, a north crosswing, and mullioned windows. The solar was extended either at the same time and later rebuilt, or extended in the late seventeenth century to form the south wing. A southeast barn is sixteenth century, and a northwest barn is seventeenth/eighteenth century. The hall and both barns are listed Grade II.[^nher-mnf9108-old-hall]

Norfolk Heritage Explorer's parish summary independently contextualizes the site, describing Old Hall (NHER 9108) as probably the oldest surviving post-medieval building in Great Ellingham, built in the mid-sixteenth century for one of the Gurney family and standing on the site of an earlier moated manor.[^nher-old-hall-summary]

This is therefore a high-value place witness for Great Ellingham because it ties the Gurneys to a specific historic-environment site rather than only to county-history manorial descent. It also bridges the file's existing interpretation: Great Ellingham is a later gentry-manor and inheritance record, but Old Hall gives that inheritance geography a physical center.

Working Old Hall coordinate: **52.5319, 0.9808**. NHER location fields: grid reference **TM 0161 9651**, map sheet **TM09NW**, parish **Great Ellingham, Breckland, Norfolk**. The record also notes a corrected central grid reference from **TM 0163 9648** to **TM 0161 9653**, and a newly identified northern moated component centered on **TM 0160 9659**.[^nher-mnf9108-old-hall]

Norfolk Heritage Explorer map URL: https://www.heritage.norfolk.gov.uk/map-record?scale=3385.5001277302295&lon=108065.87938898&lat=6896386.9675375&baseMapID=OSM&ck_MON1=true&ck_MON=true

[^nher-mnf9108-old-hall]: Norfolk Historic Environment Service, "MNF9108 — Old Hall, Great Ellingham," *Norfolk Heritage Explorer*, https://www.heritage.norfolk.gov.uk/record-details?MNF9108. Source ID: `nher-mnf9108-old-hall-great-ellingham`.
[^nher-old-hall-summary]: Norfolk Historic Environment Service, "Parish Summary: Great Ellingham," *Norfolk Heritage Explorer*, accessed 26 April 2026, https://www.heritage.norfolk.gov.uk/record-details?TNF342-Parish-Summary-Great-Ellingham-(Parish-Summary). Source ID: `nher-great-ellingham-parish-summary`.
```

### 5.3 Add new section after `## Old Hall and the Gurney built landscape`

```markdown
## Old Hall earthworks, monument types, and protected status

The Norfolk National Mapping Programme update in the MNF9108 record says the medieval moated complex and hall are visible on aerial photographs. The main component consists of surviving moats and fishponds, while cropmark and earthwork traces reveal an additional substantial moated enclosure north of the main moat around the hall. The northern moated enclosure would have measured about 80m by 60m and was defined by broad ditches and accompanying banks. The Ordnance Survey Second Edition map (1902-8, 25 inch) indicates that the eastern arm of the moat survived as a minor drainage channel until relatively recently.[^nher-mnf9108-old-hall]

MNF9108 monument types are: fishpond, medieval; moat, medieval; barn, post-medieval; and great house, post-medieval. No associated finds are recorded. Protected status is listed building, with Historic England National Heritage List entries **1077567** and **1342457** cited for the hall and the two barns.[^nher-mnf9108-old-hall]

The source list is itself a useful research roadmap: E. Rose's 1988 NAU building report; architectural plans; sale advertisements from 1986, 1993, and 2001; Ordnance Survey and NAU record cards; NHER record notes; and aerial photographs from 1976 and 1988. These should be treated as downstream targets if Old Hall becomes a major feature in the Great Ellingham narrative.[^nher-mnf9108-old-hall]
```

### 5.4 Add new section after `## Old Hall earthworks, monument types, and protected status`

```markdown
## Parish archaeological context

The Norfolk Heritage Explorer parish summary is also useful broader context. It places Great Ellingham in the Breckland region near Attleborough, about ten miles southwest of Norwich, and derives the name from Old English for "the homestead of Ella's or Eli's people." It notes that the parish was established by the Norman Conquest and recorded in Domesday Book in 1086.[^nher-parish-summary]

The summary describes a long archaeological sequence: Palaeolithic and later flint finds; Bronze Age barrow evidence and metalwork; Roman-period concentrations of pottery and building material in the south of the parish; Saxon small finds; and medieval buildings and settlement evidence. For the Gurney file, the most important medieval and post-medieval context is St James the Great's Church (NHER 4259), mainly fourteenth century; surviving medieval-origin houses including Mill Farmhouse, Tannery Farm, and Ye Olde Thatche Shoppe; a moated-manor site at NHER 34571; and Old Hall (NHER 9108), built for one of the Gurneys on an earlier moated-manor site.[^nher-parish-summary]

[^nher-parish-summary]: Norfolk Historic Environment Service, "Parish Summary: Great Ellingham," *Norfolk Heritage Explorer*, Piet Aldridge, 6 April 2006. Source ID: `nher-great-ellingham-parish-summary`.
```

### 5.5 Revise `## Open items`

Replace:

```markdown
- [ ] Check whether St James the Apostle church at Great Ellingham preserves any Gurney heraldry, epitaph material, or monument evidence tied to Henry G15 or his descendants.
```

with:

```markdown
- [ ] Check whether St James the Great / St James the Apostle church at Great Ellingham preserves any Gurney heraldry, epitaph material, or monument evidence tied to Henry G15 or his descendants.
- [ ] Pull Historic England National Heritage List entries 1077567 and 1342457 for the hall and barns.
- [ ] Obtain or inspect the E. Rose (NAU) 1988 building report and architect's plans if Old Hall is promoted into a major visual / narrative site.
- [ ] Compare Old Hall against Blomefield's Great Ellingham entry and any manorial records.
- [ ] Determine whether Old Hall should become a separate sub-place in `data/places.json`, or remain as a site note under `place-great-ellingham-norfolk-england`.
```

Remove any open item saying the full MNF9108 record body still needs to be captured; it is now captured in the corpus supplement.

### 5.6 Revise `## Sources`

Add:

```markdown
- Norfolk Historic Environment Service, "MNF9108 — Old Hall, Great Ellingham," *Norfolk Heritage Explorer*. [NHER MNF9108]
- Norfolk Historic Environment Service, "Parish Summary: Great Ellingham," *Norfolk Heritage Explorer*. [NHER Parish Summary]
```

### 5.7 Revise generated place-registry block, if hand-editing generated content is acceptable

Change:

```markdown
- Current-site status: unknown
```

to:

```markdown
- Current-site status: Old Hall (NHER 9108) is a medieval moated manorial site with a mid-16th-century great house, said to be 1573 by Henry Gurney; hall and barns listed Grade II.
```

---

## 6. Optional structured-data updates

### 6.1 `data/places.json` — Hingham coordinate and status

Locate `place-hingham-norfolk-england`.

If the coordinate currently follows the research file (`52.5764, 0.9656821626060168`), update it to the user-supplied Gurney's Manor site coordinate only if `place-hingham-norfolk-england` is intended to represent the manor/site rather than the market town generally:

```json
"coordinate": {
  "lat": 52.571755298216836,
  "lon": 0.9756833626995299,
  "precision": "medium"
}
```

If the place record represents Hingham town as a whole, do not replace the town coordinate. Instead create or propose a sub-place:

```json
{
  "placeId": "place-gurneys-manor-hingham-norfolk-england",
  "name": "Gurney's Manor, Hingham, Norfolk, England",
  "shortDescription": "Extant Gurney manor house",
  "placeType": "building",
  "aliases": ["Gurney's Manor", "Gurneys Manor"],
  "coordinate": {
    "lat": 52.571755298216836,
    "lon": 0.9756833626995299,
    "precision": "medium"
  },
  "roles": ["landholding / property reference", "individual geography"],
  "detail": "Extant private Grade II country house at Hingham; DiCamillo dates it circa 1600 with circa 1700 and 1826 alterations/additions and earliest elements possibly in the 1570s.",
  "currentSiteStatus": "extant private Grade II country house; not open to public",
  "sourceIds": ["dicamillo-gurneys-manor"]
}
```

Preferred approach: **create the sub-place**, because the Hingham town coordinate and the Gurney's Manor house coordinate are not the same type of place evidence.

### 6.2 `data/places.json` — Harpley detail cleanup

Locate `place-harpley-norfolk-england`.

If the detail contains `Gurney's manor in Harpley`, revise to:

```text
Harpley manor, a major medieval Gurney holding acquired c.1183 through Rose de Burnham and the Hameline de Warenne connection; distinct from the extant Gurney's Manor at Hingham.
```

### 6.3 `data/places.json` — Great Ellingham / Old Hall

Locate `place-great-ellingham-norfolk-england`.

If this record represents the whole village, keep the existing village coordinate unless the coordinate currently represents Old Hall. Add Old Hall only in detail/status:

```text
Great Ellingham manor, later associated with the Lovell inheritance through Margaret Lovell; Norfolk Heritage Explorer identifies Old Hall (NHER 9108) as a medieval moated manorial site with a mid-16th-century great house, said to be 1573 by Henry Gurney, on the site of an earlier moated manor.
```

Preferred optional sub-place:

```json
{
  "placeId": "place-old-hall-great-ellingham-norfolk-england",
  "name": "Old Hall, Great Ellingham, Norfolk, England",
  "shortDescription": "Gurney-built Old Hall site",
  "placeType": "building",
  "aliases": ["Old Hall", "Old Hall, Great Ellingham", "NHER 9108", "MNF9108"],
  "coordinate": {
    "lat": 52.5319,
    "lon": 0.9808,
    "precision": "medium"
  },
  "roles": ["landholding / property reference", "individual geography"],
  "detail": "Norfolk Heritage Explorer identifies Old Hall as a medieval moated manorial site with a mid-16th-century great house inside the main moat, said to be 1573 by Henry Gurney, with fishponds, additional moated enclosures, barns, and Grade II listed hall and barns.",
  "currentSiteStatus": "NHER-recorded medieval moated manorial site and Grade II listed great-house/barn complex",
  "sourceIds": ["nher-mnf9108-old-hall-great-ellingham", "nher-great-ellingham-parish-summary"]
}
```

Preferred approach: **create the sub-place**, because the coordinate is for Old Hall / MNF9108, while the existing Great Ellingham coordinate is for the village.

### 6.4 `data/places_detail.json`

If `places_detail.json` carries richer per-place notes, add or revise:

- `place-gurneys-manor-hingham-norfolk-england`
- `place-old-hall-great-ellingham-norfolk-england`

with the same source IDs and short interpretive cautions:
- Hingham Gurney’s Manor is distinct from Harpley.
- Old Hall coordinate is a site coordinate, not a replacement for the village coordinate.
- "Said to be 1573, by Henry Gurney" should retain the qualifier until S1 / NHLE records are checked.

---

## 7. Optional ancestor companion crosslinks

### 7.1 `research/people/g15-henry-gurney-fact-sheet.research.md`

Add a compact place-note only if the file already has a place/property section for Hingham or Great Ellingham:

```markdown
### Built-site witnesses: Hingham and Great Ellingham

Two later Norfolk place records now provide stronger built-environment anchors for Henry Gurney's world. DiCamillo identifies Gurney's Manor at Hingham as a fully extant Grade II private country house, circa 1600 with later alterations and earliest elements possibly dating to the 1570s. Norfolk Heritage Explorer identifies Old Hall, Great Ellingham (MNF9108 / NHER 9108), as a medieval moated manorial site with a mid-sixteenth-century great house inside the main moat, "said to be 1573, by Henry Gurney," with fishponds, additional moated enclosures, barns, and Grade II protected status.[^dicamillo-gurneys-manor-g15][^nher-old-hall-g15]

[^dicamillo-gurneys-manor-g15]: Curt DiCamillo, "Gurney's Manor," *The DiCamillo Companion to British & Irish Country Houses*, https://www.thedicamillo.com/house/gurneys-manor/. Source ID: `dicamillo-gurneys-manor`.
[^nher-old-hall-g15]: Norfolk Historic Environment Service, "MNF9108 — Old Hall, Great Ellingham," *Norfolk Heritage Explorer*, https://www.heritage.norfolk.gov.uk/record-details?MNF9108. Source ID: `nher-mnf9108-old-hall-great-ellingham`.
```

Do not force this if the G15 file has no natural place to add it; the primary destinations are the place files.

---

## 8. Site mirrors

If site mirrors are still committed, copy updated canonical files to any existing corresponding site paths, for example:

```text
site/website/research/places/hingham-norfolk.md
site/website/research/places/harpley.md
site/website/research/places/great-ellingham.md
```

Only do this if the site actually contains these path equivalents. Do not invent new site paths.

---

## 9. Validation checklist

Run:

```bash
python -m json.tool data/sources.json >/tmp/sources-json-check.json

grep -R "dicamillo-gurneys-manor\|nher-mnf9108-old-hall-great-ellingham\|nher-great-ellingham-parish-summary" -n \
  data research sources site | head -100

grep -R "52.571755298216836\|0.9756833626995299\|52.5319\|0.9808\|MNF9108\|NHER 9108\|TM 0161 9651\|1077567\|1342457" -n \
  data research sources site | head -100
```

Manual checks:

- `research/places/hingham-norfolk.md` now contains the DiCamillo Gurney's Manor entry and site coordinate.
- `research/places/harpley.md` now explicitly says not to conflate Harpley manor with extant Gurney's Manor at Hingham.
- `research/places/great-ellingham.md` now includes Old Hall, NHER 9108 / MNF9108, the coordinate `52.5319, 0.9808`, the NHER map URL, the parish summary URL, and the substantive MNF9108 record details.
- `sources/corpus_supplement/nher-mnf9108-old-hall-great-ellingham.md` includes the full record text supplied in the intake and does **not** say capture is pending.
- If structured-data sub-places are created, the town/village coordinates are not overwritten by site-specific building coordinates unless that is the intended data model.
