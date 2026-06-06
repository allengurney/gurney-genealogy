# v88 — MACRIS Cummington Gurney houses (CUM.151, CUM.115)

Phase-1 patchset. Promotes two examined MACRIS Form B inventory records into the
data spine, place layer (both sides), and G9 research companion.

## Context

The Massachusetts Historical Commission Form B PDFs for the two Cummington Gurney
houses were reviewed in full (text layer + visual review of the handwritten forms,
sketch maps, and photographs). They are the only two of seven downloaded MACRIS
Gurney records that touch the **direct line**:

- **CUM.151 — Gurney, Asa House, 75 Mount Rd (built 1808).** Its typed history page
  independently corroborates direct ancestor **Benjamin Gurney (G9)**: "Benjamin
  Gurney first purchased land in Lot No. 59-1 on November 5, 1770… in 1787 Benjamin
  Gurney and Philip Shaw purchased each other's farms," matching the repo's
  Foster & Streeter / Rigler facts, and adding lot-level geography (Lot 59-1 → the
  hill; village parcel No. 404, southerly **Minot Grant**). Built by **Asa Gurney**
  (G9's son, brother of G8 Amos) on his own 1795 Commonwealth purchase of Lots 5 & 6.
  "The oldest homestead in the town that is still in the original family name";
  Gurney-owned into the 1970s (Harriet Gurney; later kin John Wesley Gurney and the
  USDA entomologist Ashley B. Gurney).
- **CUM.115 — Gurney, "Ase" House, 51 Main St (built 1816).** Handwritten original
  owner **Asa Gurney**; stands on the Gurney Main Street village land (the southerly
  Minot Grant parcel G9 moved to in 1787). Later the home of Prof. William Ward
  Mitchell (President of the Day, Cummington Centennial 1879) — hence the MACRIS
  common name "Mitchell, William Ward House."

Both houses are built by Asa (one step off the direct line); they are linked to
**G9** as the documented founder of the Cummington Gurney landholding, with the
built-by-Asa fact recorded in the place detail and review notes. The five other
downloaded forms (EBR.27, RCK.252, WHI.283, WHI.305, WHI.307) are collateral and are
**not** promoted; EBR.27 is additionally downgraded (Gurney ownership only from Seth
Gurney 1824 of an existing 1794 Reniff house).

Geocoordinates obtained from current mailing address via Nominatim (OpenStreetMap),
street-level matches:
- 75 Mount Road → 42.4418878, -72.8810358 (single rooftop match).
- 51 Main Street → 42.4622397, -72.8991742 (plain street match; an alternate
  "Cummington Farm Village" candidate at 42.4622550, -72.8954650 was rejected — flagged
  in the detail review note for later deed/parcel confirmation).

## Source tracking

Two new child sourceIds under the existing umbrella `macris-mhc`:
`macris-cum-151-gurney-asa-house`, `macris-cum-115-gurney-ase-house`. Both get a
`sources/validations/*.md` worksheet (default-on) and share one
`sources/corpus_supplement/` extract holding the transcribed form text. The umbrella
`macris-mhc` note is updated to point to the child sources. PDFs are public-domain
government records under 35 MB → committed under each `mediaPath` (no `_local`).

---

## Step 1 — `data/sources.json`: add two child source records

`str_replace`:

old_string:
```
      "validationPath": "sources/validations/cummington-vital-records.md",
      "notes": "Contemporary town register page 213 records the Cummington Gurney births under 'G,' including the five in-sequence children of Amos & Ruth Gurney (Amos 5 Nov 1792, Willard 6 Mar 1794, Hannah 7 May 1795, Ruth 4 Jan 1800, Nathan 2 Apr 1802) and a sixth, Willis, entered out of sequence at the foot of the section with the year flagged by the clerk's own question mark ('Feb 23 1793 (?)'). Confirms the Amos G8 child set and frames the contested Willis G7 birth. Page image supplied via chat (Ancestry), held local-only under mediaPath/_local."
    },
    "ny-war-1812-payroll-abstracts": {
```

new_string:
```
      "validationPath": "sources/validations/cummington-vital-records.md",
      "notes": "Contemporary town register page 213 records the Cummington Gurney births under 'G,' including the five in-sequence children of Amos & Ruth Gurney (Amos 5 Nov 1792, Willard 6 Mar 1794, Hannah 7 May 1795, Ruth 4 Jan 1800, Nathan 2 Apr 1802) and a sixth, Willis, entered out of sequence at the foot of the section with the year flagged by the clerk's own question mark ('Feb 23 1793 (?)'). Confirms the Amos G8 child set and frames the contested Willis G7 birth. Page image supplied via chat (Ancestry), held local-only under mediaPath/_local."
    },
    "macris-cum-151-gurney-asa-house": {
      "shortTitle": "MACRIS CUM.151 - Gurney, Asa House (75 Mount Rd, Cummington)",
      "citation": "Massachusetts Historical Commission, Inventory of Historic Assets of the Commonwealth, Form B - Building, inventory no. CUM.151, 'Gurney, Asa House,' 75 Mount Road, Cummington, Hampshire County, Massachusetts (built 1808). Recorded by W.W.S. [William W. Streeter], Cummington Historical Commission, 30 January 1975. Massachusetts Cultural Resource Information System (MACRIS).",
      "archive": "Massachusetts Historical Commission / MACRIS; scanned Form B PDF",
      "url": "https://mhc-macris.net/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/macris-cummington-gurney-houses-extract.md",
      "mediaPath": "sources/media/macris-cum-151-gurney-asa-house/",
      "validationPath": "sources/validations/macris-cum-151-gurney-asa-house.md",
      "notes": "MHC Form B for the Asa Gurney homestead, lookup key CUM.151 in MACRIS. The typed history page independently corroborates Benjamin Gurney G9's documented Cummington land transactions (Lot 59-1 purchase 5 Nov 1770; 1787 Philip Shaw farm exchange; move to the village/southerly Minot Grant) and dates son Asa's purchase of Lots 5 & 6 (1795) and the present house (1808). Sources cited on the form: 'Only One Cummington' (Foster & Streeter), deeds, tax records. Handwritten margin adds later family members John Wesley Gurney (Hillside Agricultural Society) and Ashley B. Gurney (USDA entomologist); homestead still in the family name (Harriet Gurney) at survey."
    },
    "macris-cum-115-gurney-ase-house": {
      "shortTitle": "MACRIS CUM.115 - Gurney, Ase House (51 Main St, Cummington)",
      "citation": "Massachusetts Historical Commission, Inventory of Historic Assets of the Commonwealth, Form B - Building, inventory no. CUM.115, 'Gurney, Ase House' (common name 'Mitchell, William Ward House'), 51 Main Street, Cummington Center, Hampshire County, Massachusetts (built 1816). Recorded by W.W.S. [William W. Streeter], Cummington Historical Commission, 14 November 1974. Massachusetts Cultural Resource Information System (MACRIS).",
      "archive": "Massachusetts Historical Commission / MACRIS; scanned Form B PDF",
      "url": "https://mhc-macris.net/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/macris-cummington-gurney-houses-extract.md",
      "mediaPath": "sources/media/macris-cum-115-gurney-ase-house/",
      "validationPath": "sources/validations/macris-cum-115-gurney-ase-house.md",
      "notes": "MHC Form B for Asa Gurney's village house, lookup key CUM.115 in MACRIS. Handwritten original owner Asa Gurney; the house sits on the Gurney Main Street land within the southerly Minot Grant parcel Benjamin Gurney G9 settled in 1787. Later home of Prof. William Ward Mitchell (President of the Day, Cummington Centennial 1879), source of the common name. Sources cited on the form: 'Only One Cummington,' History of the Connecticut Valley (1879), deeds."
    },
    "ny-war-1812-payroll-abstracts": {
```

## Step 2 — `data/sources.json`: update umbrella `macris-mhc` note

`str_replace`:

old_string:
```
CUM.115 and CUM.151 (Asa Gurney houses, Cummington) as candidate seats of the direct line's Cummington branch;
```

new_string:
```
CUM.115 and CUM.151 (Asa Gurney houses, Cummington) - examined and promoted, see child sources macris-cum-115-gurney-ase-house and macris-cum-151-gurney-asa-house;
```

## Step 3 — `data/places.json`: add two building records

`str_replace`:

old_string:
```
      "filename": "cummington-ma.md"
  },
  {
    "placeId": "place-dexter-michigan-usa",
```

new_string:
```
      "filename": "cummington-ma.md"
  },
  {
    "placeId": "place-75-mount-road-cummington-massachusetts-usa",
    "name": "75 Mount Road, Cummington, Massachusetts, USA",
    "aliases": [
      "Gurney, Asa House",
      "75 Mount Rd, Cummington",
      "MACRIS CUM.151"
    ],
    "shortDescription": "Asa Gurney homestead (1808); oldest Cummington house in the family name",
    "placeType": "building",
    "coordinate": {
      "lat": 42.4418878,
      "lng": -72.8810358
    },
    "coordinatePrecision": "high",
    "roles": [
      "landholding / property reference"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g9-benjamin-gurney",
        "role": "landholding / property reference"
      }
    ],
    "filename": "75-mount-rd-cummington-ma.md"
  },
  {
    "placeId": "place-51-main-street-cummington-massachusetts-usa",
    "name": "51 Main Street, Cummington, Massachusetts, USA",
    "aliases": [
      "Gurney, Ase House",
      "Mitchell, William Ward House",
      "51 Main St, Cummington",
      "MACRIS CUM.115"
    ],
    "shortDescription": "Asa Gurney's village house (1816) on the Gurney Main Street land",
    "placeType": "building",
    "coordinate": {
      "lat": 42.4622397,
      "lng": -72.8991742
    },
    "coordinatePrecision": "high",
    "roles": [
      "landholding / property reference"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g9-benjamin-gurney",
        "role": "landholding / property reference"
      }
    ],
    "filename": "51-main-st-cummington-ma.md"
  },
  {
    "placeId": "place-dexter-michigan-usa",
```

## Step 4 — `data/places_detail.json`: add two detail records

`str_replace`:

old_string:
```
    "reviewNotes": [
      "G10 and G11 were removed from this place link; Cummington belongs to the G9 frontier line rather than the G10/Sarah Morse Rochester homestead branch."
    ]
  },
  {
    "placeId": "place-dexter-michigan-usa",
```

new_string:
```
    "reviewNotes": [
      "G10 and G11 were removed from this place link; Cummington belongs to the G9 frontier line rather than the G10/Sarah Morse Rochester homestead branch."
    ]
  },
  {
    "placeId": "place-75-mount-road-cummington-massachusetts-usa",
    "placeName": "75 Mount Road, Cummington, Massachusetts, USA",
    "longDescription": "Federal-era farmhouse built in 1808 by Asa Gurney (b. 24 Oct. 1758), son of the direct-line ancestor Benjamin Gurney (G9) and brother of Amos Gurney (G8). Asa bought the southerly half of Lot 5 and the northerly half of Lot 6 (Plymouth grant lots) from the Commonwealth in 1795, reportedly built a log cabin first, then the present house in 1808. The MACRIS Form B (CUM.151) calls it 'the oldest homestead in the town that is still in the original family name' and records the founding of the Cummington Gurney line: Benjamin Gurney (G9) first bought Lot 59-1 on 5 November 1770 and in 1787 exchanged farms with Philip Shaw, moving to 100 acres of the southerly Minot Grant in the village. The homestead remained Gurney-owned into the 1970s (Harriet Gurney); later family members noted on the form include John Wesley Gurney (Hillside Agricultural Society) and the USDA entomologist Ashley B. Gurney.",
    "siteName": "Gurney, Asa House (MACRIS CUM.151)",
    "streetAddress": "75 Mount Road, Cummington, MA 01026",
    "extantStatus": "extant",
    "extantStatusDescription": "Standing; recorded by MHC, not demolished.",
    "coordinateBasis": "street-address geocode (Nominatim / OpenStreetMap), rooftop match",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "https://mhc-macris.net/",
    "heritageLabel": "MACRIS CUM.151",
    "reviewNotes": [
      "House built by Asa Gurney (G9's son), not a direct-line ancestor; linked to G9 as the documented founder of the Cummington Gurney landholding the form narrates. Lots 5 & 6 were Asa's own 1795 Commonwealth purchase, distinct from G9's Lot 59-1 / village Minot Grant parcels."
    ]
  },
  {
    "placeId": "place-51-main-street-cummington-massachusetts-usa",
    "placeName": "51 Main Street, Cummington, Massachusetts, USA",
    "longDescription": "Federal two-story house built in 1816, original owner Asa Gurney (b. 1758), son of direct-line ancestor Benjamin Gurney (G9). It stands in Cummington Center on the Gurney village land - the 100 acres of the southerly Minot Grant that Benjamin Gurney (G9) moved to after the 1787 farm exchange with Philip Shaw; the family gave away free Main Street acre-lots to encourage building (reportedly houses Nos. 223, 226, 227, 228). Later the home of Prof. William Ward Mitchell - fifty-year teacher, selectman, state representative, and President of the Day for the Cummington Centennial (1879) - hence the MACRIS common name 'Mitchell, William Ward House.' Twentieth-century owners Franklin and Florence Strutton ran a trucking company and a Hereford cattle farm.",
    "siteName": "Gurney, Ase House (MACRIS CUM.115)",
    "streetAddress": "51 Main Street, Cummington, MA 01026",
    "extantStatus": "extant",
    "extantStatusDescription": "Standing; recorded by MHC, not demolished.",
    "coordinateBasis": "street-address geocode (Nominatim / OpenStreetMap)",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "https://mhc-macris.net/",
    "heritageLabel": "MACRIS CUM.115",
    "reviewNotes": [
      "House built 1816 by Asa Gurney (G9's son), not a direct-line ancestor; linked to G9 via the village Minot-Grant land he settled in 1787. Geocode returned two '51 Main Street' candidates; used the plain street match (42.4622397, -72.8991742) over the 'Cummington Farm Village' candidate (42.4622550, -72.8954650) - verify against deed/parcel if a tighter fix is wanted."
    ]
  },
  {
    "placeId": "place-dexter-michigan-usa",
```

## Step 5 — `data/ancestors.json`: bidirectional link on G9 `placeRefs`

`str_replace`:

old_string:
```
    "recordId": "ancestor-g9-benjamin-gurney",
    "placeRefs": [
      "place-abington-massachusetts-usa",
      "place-abington-whitman-line-massachusetts-usa",
      "place-bridgewater-massachusetts-usa",
      "place-braintree-massachusetts-usa",
      "place-cummington-massachusetts-usa"
    ]
  },
```

new_string:
```
    "recordId": "ancestor-g9-benjamin-gurney",
    "placeRefs": [
      "place-abington-massachusetts-usa",
      "place-abington-whitman-line-massachusetts-usa",
      "place-bridgewater-massachusetts-usa",
      "place-braintree-massachusetts-usa",
      "place-cummington-massachusetts-usa",
      "place-75-mount-road-cummington-massachusetts-usa",
      "place-51-main-street-cummington-massachusetts-usa"
    ]
  },
```

## Step 6 — new file `research/places/75-mount-rd-cummington-ma.md`

`new file write`:
```
# 75 Mount Road, Cummington, Massachusetts, USA

The Asa Gurney homestead (MACRIS CUM.151), a Federal-era farmhouse built in 1808 and
"the oldest homestead in the town that is still in the original family name." Asa
Gurney (b. 24 Oct. 1758), son of the direct-line ancestor [[g09-benjamin-gurney-fact-sheet]]
and brother of [[g08-amos-gurney-fact-sheet]], bought the southerly half of Lot 5 and
northerly half of Lot 6 from the Commonwealth in 1795 and built the present house in
1808. The MACRIS Form B also narrates the founding of the Cummington Gurney line by
Benjamin Gurney (G9): the 5 November 1770 purchase of Lot 59-1 and the 1787 farm
exchange with Philip Shaw that moved the family to the southerly Minot Grant in the
village - independent corroboration of facts otherwise carried from Foster & Streeter's
*Only One Cummington* and Rigler (1994). The homestead stayed in Gurney hands into the
1970s; the form's handwritten margin records later kin John Wesley Gurney (who
single-handedly incorporated the Hillside Agricultural Society) and Ashley B. Gurney, a
retired USDA entomologist. See [[cummington-ma]] for the town-level context.

Source: MACRIS CUM.151 (`macris-cum-151-gurney-asa-house`); transcription in
`sources/corpus_supplement/macris-cummington-gurney-houses-extract.md`.

<!-- GENERATED:PLACE-REGISTRY:START -->
## Place registry

- `placeId`: `place-75-mount-road-cummington-massachusetts-usa`
- Short description: Asa Gurney homestead (1808); oldest Cummington house in the family name
- Place type: building
- Aliases: Gurney, Asa House; 75 Mount Rd, Cummington; MACRIS CUM.151
- Coordinate: 42.4418878, -72.8810358 (high)
- Roles: landholding / property reference
- Site name: Gurney, Asa House (MACRIS CUM.151)
- Street address: 75 Mount Road, Cummington, MA 01026
- Detail: Built 1808 by Asa Gurney (G9's son, G8's brother) on his 1795 Commonwealth purchase of Lots 5 & 6; form corroborates Benjamin Gurney G9's 1770/1787 Cummington land history. Geocode basis: street-address (Nominatim), rooftop match.

### Linked ancestors

- G9 Benjamin Gurney - landholding / property reference

<!-- GENERATED:PLACE-REGISTRY:END -->
```

## Step 7 — new file `research/places/51-main-st-cummington-ma.md`

`new file write`:
```
# 51 Main Street, Cummington, Massachusetts, USA

Asa Gurney's village house (MACRIS CUM.115), a Federal two-story house built in 1816,
original owner Asa Gurney (son of the direct-line ancestor
[[g09-benjamin-gurney-fact-sheet]]). It stands in Cummington Center on the Gurney Main
Street land - the 100 acres of the southerly Minot Grant that Benjamin Gurney (G9)
settled after the 1787 farm exchange with Philip Shaw. The Gurneys gave away free
Main Street acre-lots to encourage building (reportedly houses Nos. 223, 226, 227,
228). The house was later the home of Prof. William Ward Mitchell - fifty-year teacher,
selectman, state representative, and President of the Day for the Cummington Centennial
(1879) - which is why MACRIS carries the common name "Mitchell, William Ward House."
Twentieth-century owners Franklin and Florence Strutton ran a trucking company and a
Hereford cattle farm. See [[cummington-ma]] for the town-level context and
[[75-mount-rd-cummington-ma]] for the Asa Gurney homestead on Mount Road.

Source: MACRIS CUM.115 (`macris-cum-115-gurney-ase-house`); transcription in
`sources/corpus_supplement/macris-cummington-gurney-houses-extract.md`.

<!-- GENERATED:PLACE-REGISTRY:START -->
## Place registry

- `placeId`: `place-51-main-street-cummington-massachusetts-usa`
- Short description: Asa Gurney's village house (1816) on the Gurney Main Street land
- Place type: building
- Aliases: Gurney, Ase House; Mitchell, William Ward House; 51 Main St, Cummington; MACRIS CUM.115
- Coordinate: 42.4622397, -72.8991742 (high)
- Roles: landholding / property reference
- Site name: Gurney, Ase House (MACRIS CUM.115)
- Street address: 51 Main Street, Cummington, MA 01026
- Detail: Built 1816 by Asa Gurney (G9's son) on the Gurney village land within G9's 1787 southerly Minot Grant parcel; later the William Ward Mitchell house. Geocode basis: street-address (Nominatim); plain street match used over a "Cummington Farm Village" candidate.

### Linked ancestors

- G9 Benjamin Gurney - landholding / property reference

<!-- GENERATED:PLACE-REGISTRY:END -->
```

## Step 8 — `research/places/cummington-ma.md`: append homestead narrative

`str_replace`:

old_string:
```
<!-- GENERATED:PLACE-REGISTRY:END -->
```

new_string:
```
<!-- GENERATED:PLACE-REGISTRY:END -->

## Gurney homestead continuity (MACRIS)

Two surviving Cummington houses carry the family's nineteenth-century continuity, both
built by **Asa Gurney** (b. 1758), son of the direct ancestor Benjamin Gurney (G9) and
brother of Amos Gurney (G8):

- **[[75-mount-rd-cummington-ma]]** (MACRIS CUM.151, built 1808) - the homestead on
  Mount Road, "the oldest homestead in the town that is still in the original family
  name," Gurney-owned into the 1970s.
- **[[51-main-st-cummington-ma]]** (MACRIS CUM.115, built 1816) - Asa's village house on
  the Gurney Main Street land, later the Prof. William Ward Mitchell house.

The CUM.151 Form B independently documents G9's founding of the Cummington Gurney line:
the 5 November 1770 purchase of Lot 59-1 (the hill) and the 1787 farm exchange with
Philip Shaw, after which Gurney moved to 100 acres of the southerly **Minot Grant** in
the village (parcel No. 404) while Shaw took the hill (No. 302). G9, both his wives, and
his son Benjamin are buried at Dawes Cemetery, Cummington.
```

## Step 9 — `research/people/g09-benjamin-gurney-fact-sheet.research.md`: add corroboration section

`str_replace`:

old_string:
```
The 1790 federal census summary for Cummington still requires image-level rechecking. The currently carried 3-0-3 household structure is consistent with a later-life farm household but may not include son Amos in the expected older male category. Treat this as a check item rather than a resolved household reconstruction.
```

new_string:
```
The 1790 federal census summary for Cummington still requires image-level rechecking. The currently carried 3-0-3 household structure is consistent with a later-life farm household but may not include son Amos in the expected older male category. Treat this as a check item rather than a resolved household reconstruction.

## MACRIS inventory corroboration (CUM.151 / CUM.115)

The Massachusetts Historical Commission Form B for the Asa Gurney homestead at 75 Mount Road, Cummington (MACRIS CUM.151, recorded 1975) independently corroborates G9's documented Cummington land history and adds lot-level geography. Its typed history reads: "Benjamin Gurney first purchased land in Lot No. 59-1 on November 5, 1770. The records indicate that in 1787 Benjamin Gurney and Philip Shaw purchased each other's farms. Gurney moved to the village (No. 404) to 100 acres of the southerly part of Minot Grant, while Shaw moved to the hill (No. 302) in Lot No. 59-1."[^macris-cum151] The 5 November 1770 purchase and the 1787 Shaw exchange match the dates already carried from Foster & Streeter and Rigler (1994); the form newly specifies the parcels (Lot 59-1 on the hill; the southerly Minot Grant in the village) and cites *Only One Cummington*, deeds, and tax records.

Son **Asa Gurney** (b. 24 Oct. 1758) bought the southerly half of Lot 5 and northerly half of Lot 6 from the Commonwealth in 1795 and built the present homestead in 1808; it was "the oldest homestead in the town that is still in the original family name," held by Harriet Gurney at survey.[^macris-cum151] A second form, for Asa's 1816 village house at 51 Main Street (MACRIS CUM.115), names Asa as original owner; it sits on the Gurney Main Street land within G9's southerly Minot Grant parcel and was later the home of Prof. William Ward Mitchell, President of the Day for the Cummington Centennial of 1879.[^macris-cum115] The CUM.151 form's handwritten margin carries the line forward to John Wesley Gurney (who incorporated the Hillside Agricultural Society) and Ashley B. Gurney, "a retired entomologist for the U.S. Gov't."[^macris-cum151]

[^macris-cum151]: Massachusetts Historical Commission, Inventory of Historic Assets, Form B - Building, inventory no. CUM.151, "Gurney, Asa House," 75 Mount Road, Cummington (built 1808); recorded by W.W.S. [William W. Streeter], Cummington Historical Commission, 30 Jan. 1975. Transcription at [`sources/corpus_supplement/macris-cummington-gurney-houses-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/macris-cummington-gurney-houses-extract.md); scanned form at `sources/media/macris-cum-151-gurney-asa-house/`. Source ID: `macris-cum-151-gurney-asa-house`. Availability: **Available online** (MACRIS, https://mhc-macris.net/).
[^macris-cum115]: Massachusetts Historical Commission, Inventory of Historic Assets, Form B - Building, inventory no. CUM.115, "Gurney, Ase House" (common name "Mitchell, William Ward House"), 51 Main Street, Cummington Center (built 1816); recorded by W.W.S. [William W. Streeter], Cummington Historical Commission, 14 Nov. 1974. Transcription at [`sources/corpus_supplement/macris-cummington-gurney-houses-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/macris-cummington-gurney-houses-extract.md); scanned form at `sources/media/macris-cum-115-gurney-ase-house/`. Source ID: `macris-cum-115-gurney-ase-house`. Availability: **Available online** (MACRIS, https://mhc-macris.net/).
```

## Step 10 — new file `sources/corpus_supplement/macris-cummington-gurney-houses-extract.md`

`new file write`:
```
# MACRIS Cummington Gurney houses — Form B extracts

Transcribed text from the Massachusetts Historical Commission Form B inventory records
for the two Asa Gurney houses in Cummington. Source IDs: `macris-cum-151-gurney-asa-house`,
`macris-cum-115-gurney-ase-house`. Scanned PDFs under each source's `mediaPath`.

## CUM.151 — Gurney, Asa House, 75 Mount Road (built 1808)

Header (form no. 412): "Lots No. 5 & 6 PL / Harriet Gurney." Original owner: Asa Gurney.
Original use: dwelling. Recorded by W.W.S., Cummington Historical Commission, 30 Jan. 1975.

Typed history (verbatim):

> This is the oldest homestead in the town that is still in the original family name.
> Benjamin Gurney first purchased land in Lot No. 59-1 on November 5, 1770. The records
> indicate that in 1787 Benjamin Gurney and Philip Shaw purchased each other's farms.
> Gurney moved to the village (No. 404) to 100 acres of the southerly part of Minot
> Grant, while Shaw moved to the hill (No. 302) in Lot No. 59-1. In 1795 Asa Gurney
> purchased the southerly half of Lot No. 5 PL and the northerly half of Lot No. 6 PL
> from the Commonwealth of Massachusetts. He probably built a log cabin first as it is
> said he built the present house in 1808. The Gurneys owned land in the village and as
> an incentive to the development of Main Street offered a free acre of land to anyone
> who would build a house there. Some of the houses are said to be Nos. 223, 226, 227,
> 228. It is believed there were other [text cut off].

Handwritten margin note (verbatim):

> John Wesley Gurney was interested in having the Hillside Agricultural Society
> incorporated so that it could buy a permanent fairground. He called a meeting but no
> one else came. Not to be discouraged, he named himself President, Secretary,
> Treasurer, etc. and then worked at getting other people to join him. Ashley Gurney is
> at present a retired entomologist for the U.S. Gov't.

Sources cited on the form: *Only One Cummington* (Foster & Streeter); deeds; tax records.

## CUM.115 — Gurney, Ase House, 51 Main Street (built 1816)

Common name: Mitchell, William Ward House. Neighborhood: Cummington Center (Area CUM.C),
Local No. 285. Original owner: Asa Gurney. Original use: dwelling. Present owner (1974):
Florence Strutton. Recorded by W.W.S., Cummington Historical Commission, 14 Nov. 1974.

Handwritten history (verbatim):

> This house has some interesting architectural details not usually found in Cummington
> including triple windows upstairs over the front doorway and a fan-form portico with
> sidelights by the door. It was the home of Professor William Ward Mitchell, who was a
> teacher for fifty years, a selectman, a state representative, and the President of the
> Day for the Cummington Centennial Celebration in 1879. Recent owners were Franklin and
> Florence Strutton who operated a trucking company and a farm still polled Hereford
> beef cattle.

Sources cited on the form: *Only One Cummington*; History of the Connecticut Valley
(1879); deeds.
```

## Step 11 — new file `sources/validations/macris-cum-151-gurney-asa-house.md`

`new file write`:
```
# Validation — MACRIS CUM.151 (Gurney, Asa House)

- **Source ID:** `macris-cum-151-gurney-asa-house`
- **Examined:** Full 3-page scanned Form B PDF — text layer plus visual review of the handwritten form front, building photograph, and sketch map.
- **Scope:** Typed history page (Asa Gurney homestead, 75 Mount Rd, built 1808) and handwritten margin notes; form header (Lots 5 & 6 PL, owner Harriet Gurney); recorder W.W.S., 30 Jan. 1975.
- **Findings landed:** `research/people/g09-benjamin-gurney-fact-sheet.research.md` (MACRIS corroboration section); `research/places/75-mount-rd-cummington-ma.md`; `data/places.json` + `data/places_detail.json` (`place-75-mount-road-cummington-massachusetts-usa`). Verbatim text in `sources/corpus_supplement/macris-cummington-gurney-houses-extract.md`.
- **Geolocation:** 75 Mount Road, Cummington, MA 01026 → 42.4418878, -72.8810358 (Nominatim/OpenStreetMap, rooftop street match).
- **Unexamined / uncertain:** Deed/parcel confirmation of Lots 5 & 6 vs. the rooftop pin not done; the form's "house Nos. 223, 226, 227, 228" Main Street claim not independently checked.
- **Media:** `sources/media/macris-cum-151-gurney-asa-house/CUM.151.pdf` (public domain, committed).
- **Patchset:** `sources/intake/done/v88-macris-cummington-gurney-houses.patchset.md`.
```

## Step 12 — new file `sources/validations/macris-cum-115-gurney-ase-house.md`

`new file write`:
```
# Validation — MACRIS CUM.115 (Gurney, Ase House)

- **Source ID:** `macris-cum-115-gurney-ase-house`
- **Examined:** Full 3-page scanned Form B PDF — text layer plus visual review of the handwritten form front, building photograph (winter view), and sketch map.
- **Scope:** Handwritten history page (Asa Gurney's village house, 51 Main St, built 1816; later the William Ward Mitchell house); form front (owner Florence Strutton, Area CUM.C, Local No. 285); recorder W.W.S., 14 Nov. 1974.
- **Findings landed:** `research/people/g09-benjamin-gurney-fact-sheet.research.md` (MACRIS corroboration section); `research/places/51-main-st-cummington-ma.md`; `data/places.json` + `data/places_detail.json` (`place-51-main-street-cummington-massachusetts-usa`). Verbatim text in `sources/corpus_supplement/macris-cummington-gurney-houses-extract.md`.
- **Geolocation:** 51 Main Street, Cummington, MA 01026 → 42.4622397, -72.8991742 (Nominatim/OpenStreetMap). Two street-level candidates returned; the plain "51 Main Street" match was used over a "Cummington Farm Village" candidate (42.4622550, -72.8954650). Confirm against deed/parcel if a tighter fix is wanted.
- **Unexamined / uncertain:** Which Nominatim candidate is the historic-district house not yet resolved against parcel data.
- **Media:** `sources/media/macris-cum-115-gurney-ase-house/CUM.115.pdf` (public domain, committed).
- **Patchset:** `sources/intake/done/v88-macris-cummington-gurney-houses.patchset.md`.
```

## Step 13 — media: copy the two committed PDFs

Shell (Bash):
```
mkdir -p sources/media/macris-cum-151-gurney-asa-house sources/media/macris-cum-115-gurney-ase-house
cp "sources/intake/processed/Mass-property/CUM.151.pdf" sources/media/macris-cum-151-gurney-asa-house/CUM.151.pdf
cp "sources/intake/processed/Mass-property/CUM.115.pdf" sources/media/macris-cum-115-gurney-ase-house/CUM.115.pdf
```

## Step 14 — retain the intake bundle

Move the whole download folder (the five collateral PDFs stay as the intake record):
```
mkdir -p sources/intake/done
git mv "sources/intake/processed/Mass-property" "sources/intake/done/Mass-property"  # or plain mv if not yet tracked
```

## Step 15 — regenerate indexes and validate integrity

```
.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write
```
Then run the site validator to confirm no place↔ancestor drift or dangling refs:
```
cd site/website && npm run validate
```
Expect the two new `place-*-cummington-massachusetts-usa` IDs to appear in
`data/indexes/place-ids.csv` and the G9 link to validate on both sides.

## Step 16 — close out

Prepend `**Done:** YYYY-MM-DD HH:MM PT` to this file and move it to
`sources/intake/done/v88-macris-cummington-gurney-houses.patchset.md`.

---

## Not promoted (recorded for traceability)

- **EBR.27** (Henry Gurney House, E. Bridgewater) — collateral and downgraded: house
  built 1794 by John Reniff on John Edson's grant; Gurney ownership only from Seth Gurney
  (1824) → Henry Gurney (1845–1895, selectman). Not Gurney-built; no direct-line tie.
- **RCK.252** (Samuel Gurney House, Rockland, c.1830) — collateral; no established tie.
- **WHI.283** (Jonathan Reed Gurney, son of Noah Gurney Jr. & Molly Reed), **WHI.305**
  (Daniel Gurney & Deborah Ramsdell), **WHI.307** (Nathan Gurney 1769–1850 & Martha
  Pullman) — the collateral South Abington / Whitman branch. WHI.307's Nathan is already
  noted in `data/ancestors.json` (foster-father Nathan record) as the foster-father
  Nathan's great-grandson; a minor date check remains (repo "d. 1851" vs. form "1769–1850").
  These five PDFs are retained under `sources/intake/done/Mass-property/`.
```
