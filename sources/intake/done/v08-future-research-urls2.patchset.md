# Intake patchset v08 - Future research URLs 2

> AUDIT CORRECTION: apply `sources/intake/processed/v08a-future-research-urls2-audit-supplement.patchset.md` with this patchset. Where v08 and v08a conflict, v08a supersedes v08. In particular, v08a promotes the user-supplied Baxter image extract, 1066 Gournay text, and HCommons/JNR text; removes the incorrect "verify against book image" language for Baxter; and expands the missing Hardingham, Braintree, Flushing, Gournay, and Henry Gurney findings.

```yaml
patchset_id: v08
created: 2026-05-02
intake_file: C:\Users\allen\Downloads\Future research urls2.md
repo_ref_inspected: main @ 753cd196c5dcd2d39f0fc61c1978d52c2b46995f
branch_written: codex/research-intake-future-urls2
phase: 1 intake preparation only
phase_2_rule: Apply the operations below; do not re-triage the URLs unless a listed hold-review item is being resolved.
```

## Coverage inventory

| # | Lead | Access | Outcome | Destination |
|---|---|---|---|---|
| 1 | Hardingham aliases, parish history, Blomefield, Faden map | accessed; Faden site itself not reached, local image viewed | promote | `research/places/hardingham.md`; `data/places.json`; `data/places_detail.json`; `data/sources.json` |
| 2 | Munsell 1882 Flushing, "the Alley" / John Bird woolen mill | accessed | promote | `research/places/flushing-ny.md`; `research/case-files/brigadier-general-william-gurney.md`; `data/sources.json` |
| 3 | NFWF Little Neck Bay report, p. 13 | accessed via indexed PDF text | promote | same Flushing/G6 destinations |
| 4 | New York State Military Museum, 127th Infantry | accessed | promote | `research/case-files/brigadier-general-william-gurney.md`; `data/sources.json` |
| 5 | Rigler, *The Gurney family from Aaron to Zuinglius* | metadata accessed; book not readable | source-only | `data/sources.json`; optional G4-G13 source catalog notes |
| 6 | Anderson, *The Great Migration Begins*, Gregory Baxter profile | archive metadata accessed; item access-restricted; user supplied extract | promote with access note | `research/people/g13-john-gurney-fact-sheet.research.md`; `data/sources.json` |
| 7 | NEHGR 62:94, John Gurney deposition note | accessed through indexed page text | promote | update existing `nehgr-62-94`; `research/people/g13-john-gurney-fact-sheet.research.md` |
| 8 | Hazen, *History of Billerica* p. 33 | accessed | promote | `research/people/g13-john-gurney-fact-sheet.research.md`; create `research/places/billerica-ma.md`; add place registry entry |
| 9 | NEHGR vol. 49 part 2, John Lewis of Nevis will / Mary Gurney | user extract only; page not cleanly retrieved | hold-review, source lead | `research/people/g13-john-gurney-fact-sheet.research.md` open lead |
| 10 | 1066 Mosaic DVD people/gournay page | blocked by verification page | hold-review | add source lead only if desired; no research insertion |
| 11 | 1066 Battle Roll Gurnay page | accessed; already represented | duplicate/reinforcing | update exact URL for `cleveland-battle-abbey-roll-v2-gurnay` and validation if useful |
| 12 | May, "Henry Gurney, A Norfolk Farmer..." / ResearchGate / DOI | abstract accessed through Spenser Online; ResearchGate page not needed | promote | `research/people/g15-henry-gurney-fact-sheet.research.md`; `data/sources.json` |
| 13 | MARCO / Bodleian MS Tanner 175 | URL did not render in this pass; existing companion already identifies MS | source lead | `data/sources.json`; G15 companion source list |
| 14 | HCommons Henry Gurney lead | URL did not render; no independent content extracted | hold-review | no research insertion |

## Source registry operations

### Use existing source IDs

- `hardingham-parish-history-2026` for the Hardingham local-history page.
- `blomefield-norfolk` for British History Online, Blomefield vol. 10, pp. 221-227.
- `nehgr-62-94` for the NEHGR 62:94 John Gurney Braintree deposition note, but update the entry below.
- `cleveland-battle-abbey-roll-v2-gurnay` for the 1066 Battle Roll Gurnay page, but update the URL below.

### Update existing source entries

Update `data/sources.json` entry `nehgr-62-94`:

```json
"nehgr-62-94": {
  "shortTitle": "NEHGR 62:94",
  "citation": "\"Notes: Braintree, Mass., Items.\" New England Historical and Genealogical Register, vol. 62 (January 1908), p. 94.",
  "archive": "Internet Archive / Wikimedia Commons scan",
  "url": "https://archive.org/details/newenglandhisto19unkngoog/page/94/mode/2up",
  "corpusStatus": "partial",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/nehgr-62-94.md",
  "notes": "Pulled from the Braintree, Massachusetts notes on Suffolk Court Files item no. 188. The page lists John Gurney of Braintree as aged about 50 and dated 17-1-1652/3. This corrects the former not-yet-obtained status and the intake typo that read age 60."
}
```

Update `data/sources.json` entry `cleveland-battle-abbey-roll-v2-gurnay` URL from the volume landing/index URL to the exact Gurnay entry URL:

```json
"url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html"
```

### Add new `data/sources.json` entries

Insert these source objects near related web, New England, and Gurney-family sources. Update `meta.lastUpdated` to the phase 2 date.

```json
"faden-map-norfolk-1797-hardingham": {
  "shortTitle": "Faden map of Norfolk - Hardingham extract",
  "citation": "Faden, William. A Topographical Map of the County of Norfolk, surveyed by Thomas Donald and Thomas Milne, published London: W. Faden, 1797. Hardingham-area extract.",
  "archive": "User-supplied local image from Faden's Map of Norfolk website",
  "url": "http://www.fadensmapofnorfolk.co.uk/",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": "sources/media/Hardingham c1790 Faden Map.png",
  "validationPath": "sources/validations/faden-map-norfolk-1797-hardingham.md",
  "notes": "Map extract shows Hardingham, Old Hall, Manson Green, Hardingham Low Common, and surrounding roads/watercourses. Use as visual place context, not as evidence for medieval Swathings identity by itself. Faden's Norfolk map was published in 1797 after surveying in the 1790s."
},
"munsell-history-queens-flushing-1882": {
  "shortTitle": "Munsell, History of Queens County - Flushing",
  "citation": "\"The Town and Village of Flushing.\" In History of Queens County, with illustrations, portraits & sketches of prominent families and individuals. New York: W. W. Munsell & Co., 1882, pp. 74-143.",
  "archive": "Brooklyn Genealogy Information Page transcription",
  "url": "https://bklyn-genealogy-info.stevemorse.org/Queens/history/flushing.html",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/munsell-history-queens-flushing-1882.md",
  "notes": "Flushing local-history source. Relevant here for the statement that John Bird built and operated a woolen mill at the Alley until the 1850 fire, with a reported 10000 dollar loss."
},
"nfwf-little-neck-bay-history-ecology-2008": {
  "shortTitle": "History and Ecology of Little Neck Bay",
  "citation": "History and Ecology of Little Neck Bay. Final report hosted by the National Fish and Wildlife Foundation, 2008.",
  "archive": "National Fish and Wildlife Foundation PDF",
  "url": "https://www.nfwf.org/sites/default/files/finalreports1/7460_2008-0065-004_Report_History_and_Ecology_of_Little_Neck_Bay.pdf",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/nfwf-little-neck-bay-history-ecology-2008.md",
  "notes": "Local environmental/history report. Page 13 provides compact context for Alley Creek/Little Neck Bay navigation, two mills, tavern, blacksmith, wheelwright, general store, first Flushing post office, Van Zandt's 1826 causeway, and the John Baird/Bird woolen mill fire."
},
"ny-state-military-museum-127th-infantry": {
  "shortTitle": "NYS Military Museum - 127th Infantry Regiment",
  "citation": "\"127th Infantry Regiment.\" New York State Military Museum and Veterans Research Center.",
  "archive": "New York State Military Museum website",
  "url": "https://museum.dmna.ny.gov/unit-history/infantry-2/127th-infantry-regiment",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/ny-state-military-museum-127th-infantry.md",
  "notes": "Regimental summary drawing from Phisterer and The Union Army. Confirms William Gurney's authority to raise the regiment, 8 September 1862 muster-in, service in Washington/Virginia/South Carolina/Charleston, 30 June 1865 muster-out, and regimental losses."
},
"rigler-gurney-family-aaron-zuinglius-1994": {
  "shortTitle": "Rigler, Gurney family from Aaron to Zuinglius",
  "citation": "Rigler, Jean Gurney. The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary; Some Descendants of Richard Gurney Who Settled at Weymouth, MA before 1656. Rev. and expanded ed. Honolulu, Hawaii: J. G. Rigler, 1994.",
  "archive": "Internet Archive / Open Library metadata",
  "url": "https://archive.org/details/gurneyfamilyfrom00rigl",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md",
  "notes": "Key compiled genealogy for descendants of Richard Gurney of Weymouth, Massachusetts. Internet Archive item is not readable in this pass; use as a source-control and future-pull entry until pages are checked. Especially relevant to G4-G13 American-line work."
},
"anderson-great-migration-begins-v1-baxter": {
  "shortTitle": "Anderson, Great Migration Begins vol. 1 - Gregory Baxter",
  "citation": "Anderson, Robert Charles. The Great Migration Begins: Immigrants to New England, 1620-1633. Vol. 1. Boston: New England Historic Genealogical Society, 2012, Gregory Baxter profile.",
  "archive": "Internet Archive print-disabled item; user-supplied extract",
  "url": "https://archive.org/details/greatmigrationbe0001robe",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/anderson-great-migration-begins-v1-baxter.md",
  "notes": "User-supplied extract from the Gregory Baxter profile reports John Gurney as a witness to Baxter's 1659 will/codicil and as one of the inventory takers. The Internet Archive item is access-restricted; verify against the book image when available."
},
"hazen-billerica-1883": {
  "shortTitle": "Hazen, History of Billerica",
  "citation": "Hazen, Henry A. History of Billerica, Massachusetts, with a Genealogical Register. Boston: A. Williams and Co., 1883.",
  "archive": "Internet Archive",
  "url": "https://archive.org/details/historyofbilleri00hazen",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/hazen-billerica-1883.md",
  "notes": "On historical p. 33 / image p. 54, Hazen prints the 10 September 1659 rate list for half payment of the Dudley Farm purchase; John Gurney appears with an assessment of 2-5-10."
},
"nehgr-49-genealogical-gleanings-john-lewis": {
  "shortTitle": "NEHGR 49 - Genealogical Gleanings, John Lewis will",
  "citation": "Waters, Henry F. \"Genealogical Gleanings in England.\" New England Historical and Genealogical Register, vol. 49, part 2, John Lewis of Nevis will abstract.",
  "archive": "Internet Archive lead; user-supplied extract",
  "url": "https://archive.org/details/newenglandhistorv49p2wate/",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/nehgr-49-genealogical-gleanings-john-lewis.md",
  "notes": "User-supplied extract from John Lewis of Nevis will, dated 21 December 1699 and proved 9 July 1701, includes a reference to Mary Gurney, daughter of John Gurney. Treat as a same-name/relationship lead until the page image and surrounding punctuation are checked."
},
"may-henry-gurney-spenser-2005": {
  "shortTitle": "May, Henry Gurney reads Spenser",
  "citation": "May, Steven W. \"Henry Gurney, A Norfolk Farmer, Reads Spenser and Others.\" Spenser Studies: A Renaissance Poetry Annual, vol. 20 (2005).",
  "archive": "Spenser Online abstract / DOI and ResearchGate leads",
  "url": "https://www.english.cam.ac.uk/spenseronline/spenserstudies/abstracts/",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/may-henry-gurney-spenser-2005.md",
  "notes": "Modern academic article on Henry Gurney and Bodleian MS Tanner 175. Spenser Online lists the article in vol. 20 and summarizes Gurney as poet, critic, bibliophile, owner/compiler of MS Tanner 175, and reader of Spenser, Foxe, Southwell, Hakluyt, and others. Reconcile page range before final citation: existing companion says pp. 183-223; Spenser Online displays the May abstract under pp. 169-181 and the next article under pp. 183-223."
},
"bodleian-ms-tanner-175-marco": {
  "shortTitle": "Bodleian MS Tanner 175 - MARCO",
  "citation": "Bodleian Library, MS Tanner 175. MARCO manuscript catalogue record.",
  "archive": "MARCO / Bodleian manuscript catalogue",
  "url": "https://marco.ox.ac.uk/ark:29072/x0n870zq56b5",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/bodleian-ms-tanner-175-marco.md",
  "notes": "Catalogue lead for Henry Gurney's manuscript commonplace book. The MARCO page did not render in this pass, but the URL should be retained as the direct manuscript-control lead for future review."
}
```

## File operations

1. Keep the existing local file `sources/media/Hardingham c1790 Faden Map.png` and stage it in phase 2 if not already tracked.
2. Copy the same image to `site/website/media/places/hardingham-faden-map.png` only if the site should display it on the Hardingham place page.
3. Do not archive or move `C:\Users\allen\Downloads\Future research urls2.md` during phase 2 unless the raw intake file is first copied into `sources/intake/new/v08-future-research-urls2.md`.

## Data operations

### `data/places.json`

Update `place-hardingham-norfolk-england` aliases to:

```json
"aliases": [
  "Hardingham, Norfolk",
  "Swathing",
  "Swathings",
  "Low Street",
  "Low Street, Hardingham",
  "Manor of Gurneys & Swathing",
  "Gurneys & Swathing"
]
```

Update `place-flushing-queens-new-york-usa` aliases to include:

```json
"The Alley",
"Alley Creek",
"Alley Pond",
"Little Neck Bay",
"Ireland Road"
```

Add a compact Billerica place record:

```json
{
  "placeId": "place-billerica-massachusetts-usa",
  "name": "Billerica, Massachusetts, USA",
  "aliases": [
    "Billerica, MA",
    "Shawshin",
    "Dudley Farm"
  ],
  "shortDescription": "Dudley Farm purchase-rate context",
  "placeType": "locality",
  "coordinate": {
    "lat": 42.5584,
    "lng": -71.2689
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
  "filename": "billerica-ma.md"
}
```

### `data/places_detail.json`

Update `place-hardingham-norfolk-england`:

```json
"longDescription": "Hardingham parish in central Norfolk, including the Swathing / Swathings / Low Street place-memory and the Manor of Gurneys & Swathing. The parish history places Old Hall opposite St George's Church and treats the church/Old Hall area as the early village core.",
"siteName": "Hardingham / Low Street / Old Hall context",
"extantStatus": "village and historic landscape extant",
"extantStatusDescription": "Hardingham remains a parish village; Low Street survives as a hamlet name, and the local parish history identifies Old Hall opposite St George's Church as late 16th century.",
"imageUrl": "/media/places/hardingham-faden-map.png",
"imageTitle": "Hardingham area on Faden's 1797 map of Norfolk",
"reviewNotes": [
  "Do not treat the Hardingham village centroid as a precise coordinate for Swathing/Low Street or Old Hall.",
  "Faden map extract is visual context; use parish history, White 1845, and Blomefield for the Swathing/Gurneys manorial claims."
]
```

Add `place-billerica-massachusetts-usa`:

```json
{
  "placeId": "place-billerica-massachusetts-usa",
  "placeName": "Billerica, Massachusetts, USA",
  "longDescription": "Town and Dudley Farm purchase context where John Gurney appears in Hazen's printed 1659 rate list for the half payment of the purchase.",
  "siteName": "",
  "streetAddress": "",
  "extantStatus": "town extant",
  "extantStatusDescription": "",
  "coordinateBasis": "town centroid",
  "imageUrl": "",
  "imageTitle": "",
  "heritageUrl": "",
  "heritageLabel": "",
  "reviewNotes": [
    "Town-level aggregate only; the Dudley Farm rate-list entry does not by itself identify a precise John Gurney parcel or residence site."
  ]
}
```

## Research operations

### `research/places/hardingham.md`

Replace the opening one-sentence description and the first paragraph after it with:

```markdown
Village and civil parish in central Norfolk, England, about 12 miles west of Norwich. Coordinates: **52.5708, 0.8508**.

Hardingham matters here as a layered place: the modern parish, the remembered outlier of Swathing or Swathings, the later hamlet name Low Street, and the Manor of Gurneys & Swathing all sit in the same local historical frame. The parish history says that Hardingham itself is absent from Domesday, while Flockthorpe appears; it identifies Swathing with modern Low Street and places the Manor of Gurneys & Swathing alongside the De Camois manor before Flockthorpe became Hardingham in 1210.[^hardingham-parish]
```

Add this paragraph after the existing "Swathing, Low Street, and the Gurneys & Swathings manor" section:

```markdown
The parish history also gives the Hardingham village core a useful built-landscape anchor: Old Hall stands opposite St George's Church, is considered late sixteenth century, and is presented as part of the area around which the village originally formed. Faden's 1797 Norfolk map extract reinforces the same orientation visually by showing "Old Hall" immediately by Hardingham and near the church symbol, with Manson Green and Hardingham Low Common also visible in the surrounding landscape.[^faden-hardingham]

[^faden-hardingham]: William Faden, *A Topographical Map of the County of Norfolk* (London: W. Faden, 1797), Hardingham-area extract, local file `sources/media/Hardingham c1790 Faden Map.png`. Source ID: `faden-map-norfolk-1797-hardingham`.
```

Remove the open item "Check Blomefield for the Hardingham entry and any additional Swathings manorial detail" because that Blomefield material is now already in the file.

### `research/places/flushing-ny.md`

Add this section above the generated place-registry block:

```markdown
## The Alley, Alley Creek, and William Gurney's apprenticeship landscape

The Alley was a small commercial and waterway settlement within the Flushing/Little Neck Bay landscape rather than a separate town. Munsell's 1882 history places John Bird's woolen mill at the Alley and says Bird operated it until a destructive 1850 fire ended manufacturing there.[^munsell-alley] A later Little Neck Bay history gives a broader neighborhood frame: navigable Little Neck Bay and Alley Creek supported two mills, a tavern, blacksmith and wheelwright, a general store, the first Flushing post office, and about a dozen homes; it also notes Wyant Van Zandt's 1826 causeway over the creek and marshes.[^nfwf-alley]

This context strengthens the existing William Gurney biography rather than changing its chronology. The 1837 St George's Church canvass places young William with Mr. Bird on Ireland Road; these two local histories explain why that placement mattered. Bird's mill sat in a working waterside node tied to cloth, transport, post-office traffic, and Quaker Flushing networks, not in an isolated rural backwater.

[^munsell-alley]: "The Town and Village of Flushing," in *History of Queens County* (New York: W. W. Munsell & Co., 1882), Flushing section, Brooklyn Genealogy Information Page transcription, https://bklyn-genealogy-info.stevemorse.org/Queens/history/flushing.html. Source ID: `munsell-history-queens-flushing-1882`.
[^nfwf-alley]: *History and Ecology of Little Neck Bay*, final report hosted by the National Fish and Wildlife Foundation, p. 13, https://www.nfwf.org/sites/default/files/finalreports1/7460_2008-0065-004_Report_History_and_Ecology_of_Little_Neck_Bay.pdf. Source ID: `nfwf-little-neck-bay-history-ecology-2008`.
```

### `research/case-files/brigadier-general-william-gurney.md`

Add source footnotes to the existing Alley/Bird paragraphs rather than rewriting the biography. At the end of the existing sentence ending "reported loss of $10,000," add:

```markdown
[^munsell-alley][^nfwf-alley]
```

At the end of the existing paragraph beginning "The Alley was not an isolated backwater," add:

```markdown
[^nfwf-alley]
```

Add source footnotes near the 127th regiment section. After the sentence "The result was the 127th New York Volunteer Infantry," add:

```markdown
[^nysmm-127th]
```

After the sentence "The 127th New York Volunteers were mustered out of the United States service on 30 June 1865 at Charleston, South Carolina," add:

```markdown
[^nysmm-127th]
```

Add footnotes near the existing footnote area:

```markdown
[^munsell-alley]: "The Town and Village of Flushing," in *History of Queens County* (New York: W. W. Munsell & Co., 1882), Flushing section, Brooklyn Genealogy Information Page transcription, https://bklyn-genealogy-info.stevemorse.org/Queens/history/flushing.html. Source ID: `munsell-history-queens-flushing-1882`.
[^nfwf-alley]: *History and Ecology of Little Neck Bay*, final report hosted by the National Fish and Wildlife Foundation, p. 13, https://www.nfwf.org/sites/default/files/finalreports1/7460_2008-0065-004_Report_History_and_Ecology_of_Little_Neck_Bay.pdf. Source ID: `nfwf-little-neck-bay-history-ecology-2008`.
[^nysmm-127th]: "127th Infantry Regiment," New York State Military Museum and Veterans Research Center, https://museum.dmna.ny.gov/unit-history/infantry-2/127th-infantry-regiment. Source ID: `ny-state-military-museum-127th-infantry`.
```

### `research/people/g13-john-gurney-fact-sheet.research.md`

In "Colonial / New England Record Detail", add:

```markdown
### Community records in Braintree and Billerica

The NEHGR 62:94 source pull confirms the age evidence already carried in this companion. In Suffolk Court Files item no. 188, John Gurney of Braintree is listed as about 50 years old and dated 17 March 1652/3, making this a strong chronological anchor for a birth around 1602/3 if the age was close, or more generally for the current c.1609-12 working range if the age was rounded loosely.[^nehgr-62-94]

The Gregory Baxter probate extract adds a second Braintree-community witness for 1659. Anderson's Baxter profile reports John Gurney as one of the witnesses when Gregory Baxter altered his will on 19 June 1659, and as one of the men who took Baxter's inventory on 7 July 1659. This does not prove kinship with Baxter, but it places John in a trusted local probate role shortly before his own final years.[^anderson-gmb-baxter]

Hazen's Billerica history adds a land-assessment lead outside the usual Weymouth-Braintree frame. In the 10 September 1659 rate for the half payment of the Dudley Farm purchase, John Gurney appears with an assessment of 2-5-10. Treat this as a Billerica/Dudley Farm purchase-context record until the underlying town record is checked; it does not by itself prove residence at Billerica.[^hazen-billerica]

[^nehgr-62-94]: "Notes: Braintree, Mass., Items," *New England Historical and Genealogical Register*, vol. 62 (January 1908), p. 94, https://archive.org/details/newenglandhisto19unkngoog/page/94/mode/2up. Source ID: `nehgr-62-94`.
[^anderson-gmb-baxter]: Robert Charles Anderson, *The Great Migration Begins: Immigrants to New England, 1620-1633*, vol. 1 (Boston: New England Historic Genealogical Society, 2012), Gregory Baxter profile; user-supplied extract from Internet Archive item https://archive.org/details/greatmigrationbe0001robe. Source ID: `anderson-great-migration-begins-v1-baxter`.
[^hazen-billerica]: Henry A. Hazen, *History of Billerica, Massachusetts, with a Genealogical Register* (Boston: A. Williams and Co., 1883), historical p. 33, Internet Archive, https://archive.org/details/historyofbilleri00hazen. Source ID: `hazen-billerica-1883`.
```

Add to "Children - working notes", under Mary:

```markdown
**Mary:** Married Daniel Shed. A separate 1699/1701 John Lewis of Nevis will abstract reportedly names "Mary Gurney the daughter of John Gurney." This is not yet identified with John Gurney-1's daughter Mary; preserve it as a same-name lead until the NEHGR vol. 49 page image and surrounding will context are checked.[^nehgr-49-john-lewis]

[^nehgr-49-john-lewis]: Henry F. Waters, "Genealogical Gleanings in England," *New England Historical and Genealogical Register*, vol. 49, part 2, John Lewis of Nevis will abstract; user-supplied extract from https://archive.org/details/newenglandhistorv49p2wate/. Source ID: `nehgr-49-genealogical-gleanings-john-lewis`.
```

Update "Target Source Pulls / Not Yet Searched":

- Change `NEHGR 62:94` status from `Not yet pulled` to `Pulled in v08; update research text and validation`.
- Add `Hazen, History of Billerica, p. 33` with status `Pulled in v08; underlying town record still unpulled`.
- Add `Anderson GMB vol. 1, Gregory Baxter profile` with status `User extract captured; restricted book image still to verify`.
- Add `NEHGR 49 John Lewis of Nevis will abstract` with status `Hold-review; page image and context not yet verified`.

### Create `research/places/billerica-ma.md`

```markdown
# Billerica, Massachusetts, USA

Billerica enters the John Gurney-1 research library through the Dudley Farm purchase-rate context rather than through a proved residence or family event.

## John Gurney and the 1659 Dudley Farm rate

Hazen's printed Billerica history gives the 10 September 1659 rate list for the half payment of the Dudley Farm purchase. John Gurney appears in the list with an assessment of 2-5-10.[^hazen-billerica]

This is a useful expansion of John Gurney's Massachusetts geography, but it should be handled carefully. The printed list shows participation in a purchase-rate assessment connected to Billerica; it does not, without the underlying town record and related land records, prove that John permanently resided there or held a specific parcel.

[^hazen-billerica]: Henry A. Hazen, *History of Billerica, Massachusetts, with a Genealogical Register* (Boston: A. Williams and Co., 1883), historical p. 33, Internet Archive, https://archive.org/details/historyofbilleri00hazen. Source ID: `hazen-billerica-1883`.

## Open items

- [ ] Pull the underlying Billerica town record for the 10 September 1659 Dudley Farm rate.
- [ ] Check whether John Gurney appears in any Billerica land, tax, or proprietors' records after the 1659 assessment.
- [ ] Reconcile this Billerica lead with the existing Weymouth/Braintree chronology before adding stronger residence language.

<!-- GENERATED:PLACE-REGISTRY:START -->
## Place registry

- `placeId`: `place-billerica-massachusetts-usa`
- Short description: Dudley Farm purchase-rate context
- Place type: locality
- Aliases: Billerica, MA, Shawshin, Dudley Farm
- Coordinate: 42.5584, -71.2689 (low)
- Roles: landholding / property reference
- Detail: Town and Dudley Farm purchase context where John Gurney appears in Hazen's printed 1659 rate list for the half payment of the purchase.

### Linked ancestors

- G13 John Gurney-1 - landholding / property reference

### Review notes

- Town-level aggregate only; the Dudley Farm rate-list entry does not by itself identify a precise John Gurney parcel or residence site.

<!-- GENERATED:PLACE-REGISTRY:END -->
```

### `research/people/g15-henry-gurney-fact-sheet.research.md`

Under "What Bodleian MS Tanner 175 contains", replace the opening sentence with:

```markdown
Per Steven W. May's modern article and the manuscript-catalogue lead for Bodleian MS Tanner 175, Henry's commonplace book is the central primary corpus for his literary life. The Spenser Online abstract of May's article describes Henry as an Elizabethan poet, critic, and bibliophile working from Great Ellingham, and summarizes the manuscript as preserving his library inventory, more than 600 poems, and verse "censures" of borrowed books.[^may-spenser][^tanner-175-marco]
```

Add footnotes near the existing G15 source notes:

```markdown
[^may-spenser]: Steven W. May, "Henry Gurney, A Norfolk Farmer, Reads Spenser and Others," *Spenser Studies: A Renaissance Poetry Annual*, vol. 20 (2005); abstract at Spenser Online, https://www.english.cam.ac.uk/spenseronline/spenserstudies/abstracts/. Source ID: `may-henry-gurney-spenser-2005`. Note for review: the existing companion gives pp. 183-223, while Spenser Online displays the May abstract under pp. 169-181.
[^tanner-175-marco]: Bodleian Library, MS Tanner 175, MARCO manuscript catalogue lead, https://marco.ox.ac.uk/ark:29072/x0n870zq56b5. Source ID: `bodleian-ms-tanner-175-marco`.
```

In "Open Questions for Future Research", revise item 1 to:

```markdown
1. **Direct examination of Bodleian MS Tanner 175** - highest-value path. The MARCO catalogue lead is now captured as `bodleian-ms-tanner-175-marco`, but the manuscript record did not render during v08 intake; review the Bodleian catalogue and any digitized images directly.
```

Add a source-list note:

```markdown
- Steven W. May's article and the Spenser Online abstract are now source-registry targets; reconcile the article page range before treating the citation as final.
```

### 1066 Battle Roll and blocked Mosaic person page

Do not add new research prose from `https://www.1066.co.nz/Mosaic%20DVD/text/people/gournay.htm` in phase 2. The page returned a verification shell only.

For `https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html`, do not duplicate the full existing source extraction. Update the exact URL as noted above. Optional compact note to add to `sources/validations/cleveland-battle-abbey-roll-v2-gurnay.md`:

```markdown
- v08 follow-up: exact Gurnay-entry URL is https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html. The separate Mosaic people/gournay page was not accessible in v08.
```

## Validation note bodies

Create these thin validation notes only for promoted sources not already validated. Keep them short; do not paste the research blocks into validations.

### `sources/validations/faden-map-norfolk-1797-hardingham.md`

```markdown
# Faden map of Norfolk - Hardingham extract validation

- Examined: local image `sources/media/Hardingham c1790 Faden Map.png`, viewed 2026-05-02.
- Source URL lead: http://www.fadensmapofnorfolk.co.uk/.
- Scope: Hardingham-area extract from Faden's 1797 Norfolk map.
- Findings recorded in: `research/places/hardingham.md`; structured media/source tracking in `data/sources.json` and optional `data/places_detail.json`.
- Limitation: map is visual place context; it does not independently prove the medieval Swathings/Gurneys manorial descent.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/munsell-history-queens-flushing-1882.md`

```markdown
# Munsell History of Queens County - Flushing validation

- Examined: https://bklyn-genealogy-info.stevemorse.org/Queens/history/flushing.html, accessed 2026-05-02.
- Scope: Flushing section, especially the Alley / John Bird woolen mill passage.
- Findings recorded in: `research/places/flushing-ny.md` and source citations for `research/case-files/brigadier-general-william-gurney.md`.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/nfwf-little-neck-bay-history-ecology-2008.md`

```markdown
# History and Ecology of Little Neck Bay validation

- Examined: NFWF-hosted PDF, page 13 text surfaced through indexed PDF extraction, accessed 2026-05-02.
- Scope: Alley Creek / Little Neck Bay navigation and early commercial-settlement paragraph.
- Findings recorded in: `research/places/flushing-ny.md` and source citations for `research/case-files/brigadier-general-william-gurney.md`.
- Limitation: page text appears OCR-derived and contains small typographic errors; verify against the PDF image if exact quotation is needed.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/ny-state-military-museum-127th-infantry.md`

```markdown
# NY State Military Museum - 127th Infantry validation

- Examined: https://museum.dmna.ny.gov/unit-history/infantry-2/127th-infantry-regiment, accessed 2026-05-02.
- Scope: regimental summary, Phisterer-derived service paragraph, Union Army summary, and loss figures.
- Findings recorded in: source citations for `research/case-files/brigadier-general-william-gurney.md`.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md`

```markdown
# Rigler Gurney family from Aaron to Zuinglius validation

- Examined: Internet Archive/Open Library metadata, accessed 2026-05-02.
- Scope: bibliographic control only; full book text was not available in this pass.
- Findings recorded in: no research prose yet; source retained as a key future pull for G4-G13 American-line work.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/anderson-great-migration-begins-v1-baxter.md`

```markdown
# Anderson Great Migration Begins vol. 1 - Gregory Baxter validation

- Examined: Internet Archive metadata and user-supplied extract, accessed 2026-05-02.
- Scope: Gregory Baxter profile extract mentioning John Gurney as will/codicil witness and inventory taker in 1659.
- Findings recorded in: `research/people/g13-john-gurney-fact-sheet.research.md`.
- Limitation: Internet Archive item is access-restricted; verify against book image when available.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/hazen-billerica-1883.md`

```markdown
# Hazen History of Billerica validation

- Examined: https://archive.org/details/historyofbilleri00hazen and full-text extraction, accessed 2026-05-02.
- Scope: historical p. 33 / image p. 54, 10 September 1659 Dudley Farm half-payment rate list.
- Findings recorded in: `research/people/g13-john-gurney-fact-sheet.research.md` and `research/places/billerica-ma.md`.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/nehgr-62-94.md`

```markdown
# NEHGR 62:94 validation

- Examined: NEHGR vol. 62, p. 94 via indexed scan text, accessed 2026-05-02.
- Scope: "Notes: Braintree, Mass., Items," Suffolk Court Files item no. 188, John Gurney of Braintree age note.
- Findings recorded in: `research/people/g13-john-gurney-fact-sheet.research.md`.
- Limitation: v08 confirms the printed extract; the underlying Suffolk Court Files paper is still unpulled.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/nehgr-49-genealogical-gleanings-john-lewis.md`

```markdown
# NEHGR 49 John Lewis will abstract validation

- Examined: user-supplied extract from https://archive.org/details/newenglandhistorv49p2wate/, 2026-05-02.
- Scope: John Lewis of Nevis will abstract, dated 21 December 1699 and proved 9 July 1701, including Mary Gurney daughter of John Gurney lead.
- Findings recorded in: open lead under `research/people/g13-john-gurney-fact-sheet.research.md`.
- Limitation: page image and surrounding punctuation were not verified in this pass; do not identify Mary with G13's daughter without further review.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/may-henry-gurney-spenser-2005.md`

```markdown
# May Henry Gurney reads Spenser validation

- Examined: Spenser Online abstract page and user-supplied ResearchGate/DOI lead, accessed 2026-05-02.
- Scope: article metadata and abstract-level findings about Henry Gurney, MS Tanner 175, library inventory, poems, and verse censures.
- Findings recorded in: `research/people/g15-henry-gurney-fact-sheet.research.md`.
- Limitation: full article was not obtained; page range conflict between existing companion and Spenser Online should be reconciled before final citation cleanup.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

### `sources/validations/bodleian-ms-tanner-175-marco.md`

```markdown
# Bodleian MS Tanner 175 MARCO validation

- Examined: user-supplied URL https://marco.ox.ac.uk/ark:29072/x0n870zq56b5, attempted 2026-05-02.
- Scope: manuscript catalogue lead for Bodleian MS Tanner 175.
- Findings recorded in: source list and open-item update for `research/people/g15-henry-gurney-fact-sheet.research.md`.
- Limitation: MARCO page did not render in this pass; review the catalogue directly in phase 2 or a later source pull before treating catalogue metadata as checked.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v08-future-research-urls2.patchset.md`.
```

## Holds and blockers

- Superseded by v08a: `https://www.1066.co.nz/Mosaic%20DVD/text/people/gournay.htm` has user-supplied text and should be promoted as a derivative source.
- Superseded by v08a: `https://jnr2.hcommons.org/2016/4231/` has user-supplied text in `C:\Users\allen\Downloads\Chetham's Library MS A.4.15 an Inns of Court Manuscript.md` and should be promoted.
- Still open: `https://marco.ox.ac.uk/ark:29072/x0n870zq56b5` did not render in the tooling. Retain as source lead, not as reviewed catalogue text, unless phase 2 has direct access.
- Superseded by v08a: The John Lewis / Mary Gurney lead from NEHGR vol. 49 should be retained as a user-supplied will-abstract lead in G13 research, with identification still unresolved.
- Superseded by v08a: The Great Migration Begins Baxter extract is supported by the user-supplied page image. Do not require later book-image verification for the facts retained from that image; note only that OCR/normalization should be checked against the supplied crop if wording is quoted.

## Phase 2 validation

After applying the patchset:

1. Validate JSON syntax for `data/sources.json`, `data/places.json`, and `data/places_detail.json`.
2. Run the repo's brief site/content validation from `site/website` if data or generated place blocks are changed.
3. Confirm no unrelated pre-existing file is staged accidentally; `sources/media/Hardingham c1790 Faden Map.png` was already untracked before this patchset was written.
