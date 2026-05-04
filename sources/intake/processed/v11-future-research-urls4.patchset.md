# Intake patchset v11 - Future research urls 4

```yaml
patchset_id: v11
created: 2026-05-03
intake_file: C:\Users\allen\Downloads\Future research urls4.md
phase: 1 intake preparation only
phase_2_rule: Execute the operations below verbatim. Source reasoning, destination decisions, and proposed research blocks are already resolved here.
```

## Standard

- Five distinct leads. All five are retained.
- Two are direct G13/G12 evidence (Torrey index entries; History of Weymouth Vol. 3 genealogy of Weymouth families).
- Two are same-name elimination candidates for the John Gurney case file (St Mary Harrow burials 1668/9; St Giles Cripplegate burial Dec 1640).
- One is a derivative-source confirmation of John Gurney-1's burial location plus another instance of the problematic 1615/London origin tradition (Find a Grave memorial 252975617).
- New sourceIds are minted for items 1, 2, 3, and 4. Item 5 updates the existing `history-of-weymouth` entry rather than creating a new one.
- Conflicts (Richard G12 death year 1691 vs 1719; Find a Grave 1615 birth) are preserved as conflicts, not silently merged.

## Coverage inventory

| # | Lead | Outcome | Source handling | Research destinations |
| --- | --- | --- | --- | --- |
| 1 | Torrey, *New England Marriages Prior to 1700*, page 331 Gurney entries | Promote | Add `torrey-new-england-marriages-prior-1700` | `research/people/g13-john-gurney-fact-sheet.research.md`; `research/people/g12-richard-gurney-fact-sheet.research.md`; `research/case-files/john-gurney-case-file-v4.md` |
| 2 | St Mary, Harrow on the Hill, burials Jan/Feb 1668/9, John & Mary Gurney of Okington | Promote (elimination) | Add `lma-st-mary-harrow-register-dro003` | `research/case-files/john-gurney-case-file-v4.md` (elimination table); `research/people/g13-john-gurney-fact-sheet.research.md` (origin/elimination work) |
| 3 | St Giles Cripplegate burial 15/16 Dec 1640, John Garney son of Francis Garney, joiner | Promote (elimination + clarification of two/three Francis Gurneys) | Add `lma-st-giles-cripplegate-register-p69-gis-a-002` | `research/case-files/john-gurney-case-file-v4.md` (Other Johns + Two Francises); `research/people/g13-john-gurney-fact-sheet.research.md` (TNA/elimination context) |
| 4 | Find a Grave memorial 252975617, John Gurney 1615-1663, Elm Street Cemetery, Braintree | Promote (derivative; Elm Street Cemetery datum + 1615 tradition) | Add `findagrave-john-gurney-252975617` | `research/people/g13-john-gurney-fact-sheet.research.md`; `research/case-files/john-gurney-case-file-v4.md` |
| 5 | History of Weymouth, MA, Vol. 3, "Genealogy of Weymouth families," John Gurney Sr. and Richard Gurney | Promote | Update existing `history-of-weymouth`; create corpus extract | `research/people/g13-john-gurney-fact-sheet.research.md`; `research/people/g12-richard-gurney-fact-sheet.research.md`; `research/case-files/john-gurney-case-file-v4.md` |

## Source registry operations

Update `data/sources.json` in place. Update `meta.lastUpdated` to the phase 2 application date. Insert the four new entries near related New England, parish-register, and derivative-source entries (suggested adjacency: torrey near `tag-10-70`/`nehgr-62-94`; LMA registers near `st-mary-maldon-register`; findagrave near `american-biography-cyclopedia-v26-gurney-1926`).

### New entry 1 - Torrey

```json
"torrey-new-england-marriages-prior-1700": {
  "shortTitle": "Torrey, New England Marriages Prior to 1700",
  "citation": "Torrey, Clarence Almon. New England Marriages Prior to 1700. Baltimore, MD: Genealogical Publishing Co., 2004. Page 331, Gurney entries. Accessed via Ancestry.com, U.S., New England Marriages Prior to 1700 (Provo, UT: Ancestry.com Operations Inc., 2012), database collection 3824.",
  "archive": "Ancestry.com collection 3824 / Genealogical Publishing Co. print",
  "url": "https://www.ancestry.com/imageviewer/collections/3824/images/gpc_newenglandmarriages-0347?pId=51825",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md",
  "mediaPath": null,
  "validationPath": "sources/validations/torrey-new-england-marriages-prior-1700.md",
  "notes": "Standard Torrey marriage compendium. Page 331 Gurney block: John (-1663) & 1/wf, b 1628 Weymouth; John (1603-1663) & 2/wf Grezell (Fletcher)(Jewell)(Griggs) Kibbee (-1669), w Thomas, w Humphrey, w Henry, m/5 John Burge 1667; 12 Nov 1661 Braintree; John (-1675?) & Ruth ?Retchell, m/2 John Bundy 1676, m/3 Guydo Bailey, b 1671(2?) Mendon (had John, Samuel, Mary); John3 & Elizabeth [Green] (1664-) b 1689 Weymouth; John3 (-1723) & Sarah (Thornton)[Fields] (-1714), w Zachariah, dates b 1701?/1706/aft 4 Feb 1696/b 1714 Providence; Richard (-1691) & Rebecca [Taylor] b 1656(7?) Weymouth; Samuel3 (1671-) & Sarah Atkins/Staples/Shapley dau Thomas, 26 Oct 1693 Boston/Little Compton RI; Zachariah3 & Mary [Benson] of Hull, MA, b 1695 Weymouth. Use as supplemental cross-check on the John1 family group, on Grezell Kibbee's marriage sequence, and on Richard's death year (Torrey: 1691)."
}
```

### New entry 2 - St Mary Harrow on the Hill register

```json
"lma-st-mary-harrow-register-dro003": {
  "shortTitle": "St Mary, Harrow on the Hill, parish register (LMA DRO/003)",
  "citation": "Parish register, St Mary, Harrow on the Hill, Middlesex. Burials 1668/9. London Metropolitan Archives, Reference Number DRO/003/A/01/005. Accessed via Ancestry.com, London, England, Church of England Baptisms, Marriages and Burials, 1538-1812 (Lehi, UT: Ancestry.com Operations, Inc., 2010), database collection 1624.",
  "archive": "London Metropolitan Archives / Ancestry.com collection 1624",
  "url": "https://www.ancestry.com/search/collections/1624/records/602728549?tid=181885695&pid=192416501054&ssrc=pt",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/lma-st-mary-harrow-register-dro003.md",
  "notes": "Two Gurney burial entries on page 139, right-hand page, under heading 'Buryed 1668' (Old Style; modern year 1669): 'Janry 30 - Ann/Anne daughter of John & Mary Gurney of Okington' and 'Feby 8 - Isaac son of John & Mary Gurney of Okington.' Place name reads 'Okington' or possibly 'Oakington.' User-supplied ChatGPT page-image transcription only; original image not retrieved in phase 1. Use as English same-name elimination context (a John & Mary Gurney still active in England in early 1669, six years after John Gurney-1's 1662/3 Braintree death)."
}
```

### New entry 3 - St Giles Cripplegate parish register

```json
"lma-st-giles-cripplegate-register-p69-gis-a-002": {
  "shortTitle": "St Giles Cripplegate, parish register (LMA P69/GIS/A/002/MS06419/003)",
  "citation": "Parish register, St Giles Cripplegate, City of London. Burials 1634-1646. London Metropolitan Archives, Reference Number P69/GIS/A/002/MS06419/003. Accessed via Ancestry.com, London, England, Church of England Baptisms, Marriages and Burials, 1538-1812 (Lehi, UT: Ancestry.com Operations, Inc., 2010), database collection 1624.",
  "archive": "London Metropolitan Archives / Ancestry.com collection 1624",
  "url": "https://www.ancestry.com/search/collections/1624/records/6607796",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/lma-st-giles-cripplegate-register-p69-gis-a-002.md",
  "notes": "Page 77 burial entry, indexed Burial Date 16 Dec 1640, Mother 'Francis Garney.' User-supplied ChatGPT image assessment reads the entry as 'John sonne of ffrancis Garney Joyner - 15' under the heading 'Burials in December 1640,' with the date possibly 15 rather than 16 December. The 'mother' index field is almost certainly the father's name; the trailing 'Joyner/Joiner' is the father's occupation, not part of the surname. Use as an English same-name elimination candidate and as a clarification on the multiple London Francis Gurneys/Garneys in the Cripplegate area in the late 1630s and early 1640s. Garney is a plausible Gurney variant within the Gurney/Gurny/Gourney/Garney spelling cluster."
}
```

### New entry 4 - Find a Grave John Gurney 252975617

```json
"findagrave-john-gurney-252975617": {
  "shortTitle": "Find a Grave memorial 252975617 - John Gurney, Braintree, MA",
  "citation": "Find a Grave, memorial 252975617, John Gurney, Elm Street Cemetery, Braintree, Norfolk County, Massachusetts.",
  "archive": "Find a Grave",
  "url": "https://www.findagrave.com/memorial/252975617/john-gurney",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/findagrave-john-gurney-252975617.md",
  "notes": "Derivative memorial. Birth: 29 Sep 1615, 'London Borough of Brent, Greater London, England' (anachronistic place name; Brent is a 1965 London borough). Death: 16 Mar 1663 (consistent with the SPR Case #338 inventory date 16 Mar 1662/63). Burial: Elm Street Cemetery, Braintree, Norfolk County, Massachusetts (https://www.findagrave.com/cemetery/1960540/elm-street-cemetery). Use as a derivative cross-check for the Elm Street Cemetery burial location (new datum for the G13 file) and as a second instance of the problematic 1615/London birth tradition already preserved from American Biography vol. 26."
}
```

### Update to existing entry - history-of-weymouth

Replace the existing `history-of-weymouth` block with the following. Preserve key ordering relative to the surrounding entries.

```json
"history-of-weymouth": {
  "shortTitle": "History of Weymouth, Massachusetts (1923)",
  "citation": "History of Weymouth, Massachusetts. 4 vols. Weymouth, Mass.: Weymouth Historical Society, under direction of the town, 1923. Vol. 3: Genealogy of Weymouth families, John Gurney Sr. and Richard Gurney entries.",
  "archive": "Weymouth Historical Society / Ancestry.com collection 21610 (database History of Weymouth, Massachusetts, Provo, UT: Ancestry.com Operations Inc., 2005)",
  "url": "https://www.ancestry.com/imageviewer/collections/21610/images/dvm_LocHist007443-00634-1",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/history-of-weymouth-vol3-gurney.md",
  "mediaPath": null,
  "validationPath": "sources/validations/history-of-weymouth.md",
  "notes": "Standard four-volume town history of Weymouth, Norfolk County, Massachusetts. Vol. 3 'Genealogy of Weymouth families' provides the John Gurney Sr. and Richard Gurney family group used throughout the G13/G12 research. John Sr. b. c. 1603 (1653 deposition), Braintree before 1645, Weymouth land grants 'in the East field,' 'in the mill field,' and 'on the east side of Great Pond' as early as 3 Feb. 1651-52 later granted to others, sold Braintree land 12 Feb. 1661, wife (name unknown) d. Braintree 20 Sept. 1661, m. (2) Braintree 12 Nov. 1661 widow Grissell Kibbee successively widow of Thomas Jewell, Henry Griggs, Henry Kibbee of Dorchester (her fifth husband John Burge of Weymouth, Chelmsford, and Dorchester), d. 1662-63 inventory 16 Mar. 1662-63, tailor by trade. Children: Mary b. near 1628, m. Daniel Shed who called John Gurney father; Richard b. near 1630; John b. near 1633, settled in Mendon; Peter b. near 1635; Isaac b. near 1640. Richard2 m. Rebecca Taylor (probably daughter of John and Phebe Taylor of Weymouth), made freeman 1681, surname found Garey/Garry/Gerry/Gurny, d. Weymouth Oct. 1719 (conflicts with Torrey '-1691'). Richard's children at Weymouth: Richard3 b. 18 Jan. 1656; John b. near 1658; Zachariah b. near 1660. John3 (Richard,2 John1) m. Elizabeth Green dau. of Joseph and Elizabeth (Whitman) Green b. Weymouth 5 Oct. 1664 (Joseph's will dated 8 Sept. 1691 named her 'my daughter Elizabeth Gurney'); children Elizabeth b. 5 May 1689, John b. May 1699. Zachariah3 (Richard,2 John1) b. near 1660, d. Weymouth 27 Oct. 1732, m. Mary -- (perhaps Mary Gurney d. Weymouth 14 Feb. 1736); children Zachariah4 b. 19 Nov. 1695, Joseph b. 7 Mar. 1697-98, Nathan b. 15 Oct. 1702, Jacob b. 31 Oct. 1706, Mary b. 24 Nov. 1711 m. 3 Jan. 1733-34 John Pratt of Weymouth. Zachariah4 b. 19 Nov. 1695 m. Weymouth 26 Sept. 1726 Sarah Jackson (probably dau. of Edmund and Mary (-) Jackson); children Sarah b. 7 May 1727, Zachariah b. 7 Mar. 1729, Elisha b. 30 June 1731. Page numbers as transcribed; the existing G13/G12 references to 'Weymouth Hist 3:251' should be reconciled against the section's true paging when the page image is captured."
}
```

## File operations

Copy the raw lead file into the archive after phase 2 content edits are applied:

```powershell
Copy-Item -LiteralPath 'C:\Users\allen\Downloads\Future research urls4.md' -Destination 'sources\intake\archive\v11-future-research-urls4.md'
```

Create two new corpus files using direct file write (no PDF or OCR processing required; both are user-supplied transcripts):

Create `sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md` with the following exact content:

```markdown
# Torrey, New England Marriages Prior to 1700 - page 331 Gurney block

Source ID: `torrey-new-england-marriages-prior-1700`
Scope: page 331, Gurney section, as transcribed from Ancestry collection 3824 image gpc_newenglandmarriages-0347 (pId=51825).

GURNEY, John' (-1663) & 1/wf ? (-1661); b 1628; Weymouth
GURNEY, John (1603-1663) & 2/wf Grezell (FLETCHER) (JEWELL) (GRIGGS) KIBBEE (-1669), w Thomas, w Humphrey, w Henry, m/5 John BURGE 1667; 12 Nov 1661; Braintree
GURNEY, John" (-1675?) & Ruth ?RETCHELL, m/2 John BUNDY 1676, m/3 Guydo BAILEY; b 1671(2?); Menden (had John, Samuel, Mary)
GURNEY, John3 & Elizabeth [GREEN] (1664-); b 1689; Weymouth
GURNEY, John3 (-1723) & Sarah (THORNTON) [FIELDS] (-1714), w Zachariah; b 1701?, b 1706, aft 4 Feb 1696, b 1714; Providence
GURNEY, Richard (-1691) & Rebecca [TAYLOR]; b 1656(7?), b 1654; Weymouth
GURNEY, Samuel3 (1671-) & Sarah ATKINS? STAPLES/SHAPLEY, dau Thomas, w ?; 26 Oct 1693; Boston/Little Compton, RI
GURNEY, Zachariah3 & Mary [BENSON] of Hull, MA; b 1695; Weymouth
```

Create `sources/corpus_supplement/history-of-weymouth-vol3-gurney.md` with the following exact content:

```markdown
# History of Weymouth, Massachusetts (1923) - Vol. 3 Genealogy of Weymouth families - Gurney entries

Source ID: `history-of-weymouth`
Scope: Vol. 3, Genealogy of Weymouth families, John Gurney Sr. and Richard Gurney family-group entries, as transcribed from Ancestry collection 21610 image dvm_LocHist007443-00634-1.

## 1. JOHN GURNEY, Sr.

JOHN GURNEY, Sr., was born according to his deposition, made in 1653, about 1603. He was in Braintree before 1645. Lands were granted to him in Weymouth "in the East field," "in the mill field" and "on the east side of Great Pond" as early as 3 Feb. 1651-52. These lands were subsequently granted to others. (Weymouth Land Grants, 258, 270, 278, 282.) Whether he ever resided in Weymouth is a matter of doubt. He owned land in Braintree, which he sold 12 Feb. 1661. His wife, whose name is apparently unknown, died at Braintree, 20 Sept. 1661. He married (2) at Braintree, 12 Nov. 1661, widow Grissell Kibbee, successively the widow of Thomas Jewell, Henry Griggs, and Henry Kibbee of Dorchester. Her fifth husband was John Burge (Burgess), sometime of Weymouth, but later of Chelmsford and Dorchester. John Gurney died in 1662-63, and the inventory of his estate was taken 16 Mar. 1662-63. He was by trade a tailor, and probably was father to the following children. This family is exceedingly obscure.

Children:
- Mary, b. near 1628, m. Daniel Shed, who called John Gurney father.
- Richard, b. near 1630.
- John, b. near 1633; settled in Mendon.
- Peter, b. near 1635.
- Isaac, b. near 1640.

## 2. RICHARD2 GURNEY (John1)

RICHARD2 GURNEY (John1) of Weymouth married Rebecca Taylor, probably daughter of John and Phebe Taylor of Weymouth. He was made a freeman, 1681. This surname is found spelled Garey, Garry, Gerry, and Gurny. He died at Weymouth in Oct. 1719.

Children, born at Weymouth:
- Richard,3 b. 18 Jan. 1656.
- 3. John, b. near 1658.
- 4. Zachariah, b. near 1660.

## 3. JOHN3 GURNEY (Richard,2 John1)

JOHN3 GURNEY (Richard,2 John1) was born at Weymouth near 1658; married Elizabeth Green, daughter of Joseph and Elizabeth (Whitman) Green, born at Weymouth, 5 Oct. 1664. Her father in his will, dated 8 Sept. 1691, called her "my daughter Elizabeth Gurney."

Children, born at Weymouth:
- Elizabeth,4 b. 5 May, 1689.
- John, b. May. 1699.

## 4. ZACHARIAH3 GURNEY (Richard,2 John1)

ZACHARIAH3 GURNEY (Richard,2 John1) was born at Weymouth near 1660; died at Weymouth, 27 Oct. 1732. He married Mary -, perhaps the Mary Gurney who died at Weymouth, 14 Feb. 1736.

Children, born at Weymouth:
- Zachariah,4 b. 19 Nov. 1695.
- Joseph, b. 7 Mar. 1697-98.
- Nathan, b. 15 Oct. 1702.
- Jacob, b. 31 Oct. 1706.
- Mary, b. 24 Nov. 1711; m. 3 Jan. 1733-34, John Pratt of Weymouth.

## 5. ZACHARIAH4 GURNEY (Zachariah,3 Richard,2 John1)

ZACHARIAH4 GURNEY (Zachariah,3 Richard,2 John1) was born at Weymouth, 19 Nov. 1695; married at Weymouth, 26 Sept. 1726, Sarah Jackson, probably daughter of Edmund and Mary (-) Jackson of Weymouth.

Children, born at Weymouth:
- Sarah,5 b. 7 May, 1727.
- Zachariah, b. 7 Mar. 1729.
- Elisha, b. 30 June, 1731.
```

No media files to stage. No OCR or PDF processing required.

## Validation files

Create `sources/validations/torrey-new-england-marriages-prior-1700.md`:

```markdown
# Source validation: Torrey, New England Marriages Prior to 1700

Source ID: `torrey-new-england-marriages-prior-1700`
Patchset: `sources/intake/processed/v11-future-research-urls4.patchset.md`

## Scope examined

- Ancestry collection 3824 record image gpc_newenglandmarriages-0347 (pId=51825), page 331, Gurney block.
- User-supplied transcription used; full page image not separately retrieved in phase 1.

## Status

Usable as supplemental compendium. Full transcribed Gurney block in `sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md`.

## Findings landed

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/people/g12-richard-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`
```

Create `sources/validations/lma-st-mary-harrow-register-dro003.md`:

```markdown
# Source validation: St Mary, Harrow on the Hill, parish register

Source ID: `lma-st-mary-harrow-register-dro003`
Patchset: `sources/intake/processed/v11-future-research-urls4.patchset.md`

## Scope examined

- LMA reference DRO/003/A/01/005, page 139, right-hand page, burials 1668 (Old Style; modern year 1669).
- Ancestry collection 1624 record 602728549.
- User-supplied ChatGPT page-image transcription only; original page image not separately retrieved in phase 1.

## Status

Usable for English same-name elimination work. Place name reads "Okington" or possibly "Oakington."

## Findings landed

- `research/case-files/john-gurney-case-file-v4.md`
- `research/people/g13-john-gurney-fact-sheet.research.md`
```

Create `sources/validations/lma-st-giles-cripplegate-register-p69-gis-a-002.md`:

```markdown
# Source validation: St Giles Cripplegate, parish register

Source ID: `lma-st-giles-cripplegate-register-p69-gis-a-002`
Patchset: `sources/intake/processed/v11-future-research-urls4.patchset.md`

## Scope examined

- LMA reference P69/GIS/A/002/MS06419/003, page 77, right-hand page, "Burials in December 1640."
- Ancestry collection 1624 record 6607796.
- User-supplied ChatGPT image assessment used for the page text; original page image not separately retrieved in phase 1.

## Status

Usable for English same-name elimination work and for clarifying multiple Cripplegate-area Gurney/Garney households in the late 1630s and early 1640s. The Ancestry index field "Mother: Francis Garney" almost certainly captures the father's name; the trailing "Joyner" is the father's occupation.

## Findings landed

- `research/case-files/john-gurney-case-file-v4.md`
- `research/people/g13-john-gurney-fact-sheet.research.md`
```

Create `sources/validations/findagrave-john-gurney-252975617.md`:

```markdown
# Source validation: Find a Grave memorial 252975617 - John Gurney

Source ID: `findagrave-john-gurney-252975617`
Patchset: `sources/intake/processed/v11-future-research-urls4.patchset.md`

## Scope examined

- Find a Grave memorial 252975617, https://www.findagrave.com/memorial/252975617/john-gurney
- Linked cemetery: Elm Street Cemetery, Braintree, Norfolk County, Massachusetts (https://www.findagrave.com/cemetery/1960540/elm-street-cemetery)
- User-supplied transcript only; live page not separately retrieved in phase 1.

## Status

Usable as a derivative source. The Elm Street Cemetery burial location is a new datum for the G13 file. The 1615 birth at "London Borough of Brent" reproduces the same problematic origin tradition already preserved from American Biography vol. 26 and is anachronistic on its face (Brent is a 1965 London borough).

## Findings landed

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`
```

Create `sources/validations/history-of-weymouth.md` (the existing entry's `validationPath` is null; this fills the gap):

```markdown
# Source validation: History of Weymouth, Massachusetts (1923)

Source ID: `history-of-weymouth`
Patchset: `sources/intake/processed/v11-future-research-urls4.patchset.md`

## Scope examined

- Vol. 3, Genealogy of Weymouth families, John Gurney Sr., Richard2 Gurney, John3 Gurney, Zachariah3 Gurney, and Zachariah4 Gurney entries.
- Ancestry collection 21610 image dvm_LocHist007443-00634-1.
- User-supplied transcription used; full page image not separately retrieved in phase 1.
- Earlier project notes used "Weymouth Hist 3:251" for the family-group entry; the page image will need to be inspected to confirm whether the John Gurney Sr. entry begins on p. 251 or on a different page in Vol. 3.

## Status

Usable. Full transcribed extract in `sources/corpus_supplement/history-of-weymouth-vol3-gurney.md`.

## Findings landed

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/people/g12-richard-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`
```

## Research operations - G13 John Gurney

In `research/people/g13-john-gurney-fact-sheet.research.md`, append this subsection to the `### American Biography, colonial arms, and the Norfolk-line memory` block (insert immediately before the existing `[^american-biography-g13]` footnote definitions):

```markdown
### Find a Grave memorial 252975617 - Elm Street Cemetery and the recurring 1615 tradition

The Find a Grave memorial 252975617 for John Gurney records two things worth keeping. The new datum is the burial location: "Elm Street Cemetery, Braintree, Norfolk County, Massachusetts." That place was not previously named in this file or in the case file. The recurring datum is the same problematic origin tradition already preserved from *American Biography* vol. 26: birth 29 September 1615 in "London Borough of Brent, Greater London, England," and death 16 March 1663 at Braintree. The 1615 birth conflicts with the older-father chronology favored here; the "London Borough of Brent" place name is anachronistic, since Brent is a 1965 London administrative creation and cannot describe a seventeenth-century parish. Treat the cemetery line as a citation-worthy derivative datum to chase against parish or town records, and treat the 1615/Brent line as another instance of the late tradition rather than a controlling fact.[^findagrave-g13]

[^findagrave-g13]: Find a Grave, memorial 252975617, John Gurney, Elm Street Cemetery, Braintree, Norfolk County, Massachusetts, https://www.findagrave.com/memorial/252975617/john-gurney; cemetery page https://www.findagrave.com/cemetery/1960540/elm-street-cemetery. Source ID: `findagrave-john-gurney-252975617`.
```

In the same G13 file, append this subsection immediately after the `### The Newgate apprenticeship / 1636 record - de-conflated` block (i.e., before the `---` separator and the `## Known Facts` heading):

```markdown
### Torrey marriage compendium - John1 family group cross-check

Torrey's *New England Marriages Prior to 1700*, page 331, gives a one-page cross-check of the John1 family group used in this file. The relevant Gurney lines on that page are:

- "GURNEY, John' (-1663) & 1/wf ? (-1661); b 1628; Weymouth"
- "GURNEY, John (1603-1663) & 2/wf Grezell (FLETCHER) (JEWELL) (GRIGGS) KIBBEE (-1669), w Thomas, w Humphrey, w Henry, m/5 John BURGE 1667; 12 Nov 1661; Braintree"
- "GURNEY, John\" (-1675?) & Ruth ?RETCHELL, m/2 John BUNDY 1676, m/3 Guydo BAILEY; b 1671(2?); Menden (had John, Samuel, Mary)"

The first two lines independently support the working chronology: John1 born about 1603, his unnamed first wife dying in 1661, his marriage to widow Grezell Kibbee on 12 November 1661 at Braintree, and his death in 1663. The Kibbee marriage chain is given here as Fletcher (maiden) - Jewell - Griggs - Kibbee - Burge (1667), with the Humphrey Griggs identification matching the form used elsewhere in this file rather than the older "Henry Greggs." The third line is the John Jr. who settled in Mendon; Torrey gives him a 1671/2 marriage to Ruth and three children John, Samuel, and Mary, which adds detail not previously preserved in this file's children section. Use Torrey as a supplemental compendium, not a primary record.[^torrey-g13]

[^torrey-g13]: Clarence Almon Torrey, *New England Marriages Prior to 1700* (Baltimore: Genealogical Publishing Co., 2004), p. 331, Gurney entries; Ancestry.com collection 3824 image gpc_newenglandmarriages-0347 (pId=51825), https://www.ancestry.com/imageviewer/collections/3824/images/gpc_newenglandmarriages-0347?pId=51825; transcribed extract at `sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md`. Source ID: `torrey-new-england-marriages-prior-1700`.
```

In the same G13 file, append this subsection immediately after `### Margaret Rovett / Rybett Ancestry death lead` (before `## Sources Consulted`):

```markdown
### English same-name elimination - St Mary Harrow 1668/9 and St Giles Cripplegate 1640

Two London-area parish-register burial entries reinforce that several English John Gurneys with overlapping wife names continued to live, marry, and bury children in England well after the 1641 Massachusetts emigrant record. Each is a small but real elimination check rather than a candidate for the emigrant.

St Mary, Harrow on the Hill (LMA DRO/003/A/01/005) records two burials in early 1669 (Old Style 1668) under the heading "Buryed 1668": "Janry 30 - Ann/Anne daughter of John & Mary Gurney of Okington" and "Feby 8 - Isaac son of John & Mary Gurney of Okington." A John Gurney with a wife named Mary, still parenting and burying children in England in early 1669, cannot be John Gurney-1, who died at Braintree in 1662/3. The "Okington/Oakington" residence is most likely Oakington, Cambridgeshire, but the second-syllable letters are partly obscured. Keep this John & Mary Gurney as a separate English household for any future Mary-named-wife John Gurney work.[^lma-harrow-1669]

St Giles Cripplegate, City of London (LMA P69/GIS/A/002/MS06419/003) records a burial in December 1640: "John sonne of ffrancis Garney Joyner - 15," indexed as 16 December 1640 with "Mother: Francis Garney." The index field is almost certainly the father's name, and "Joyner/Joiner" is the father's occupation, not part of the surname. This is a London child burial of a John, son of Francis Garney, joiner, in the same St Giles Cripplegate parish where the case file already records a separate Francis B "the laceweaver" Cripplegate cluster active 1638-1640. The trade difference (joiner vs laceweaver) means this Francis Garney is almost certainly a third Cripplegate-area Gurney/Garney, not the same Francis B already eliminated in the case file. Garney sits inside the Gurney/Gurny/Gourney/Garney spelling cluster and should be retained when searching same-name London households.[^lma-cripplegate-1640]

[^lma-harrow-1669]: Parish register, St Mary, Harrow on the Hill, Middlesex, burials 1668/9, London Metropolitan Archives DRO/003/A/01/005; Ancestry.com collection 1624 record 602728549, https://www.ancestry.com/search/collections/1624/records/602728549?tid=181885695&pid=192416501054&ssrc=pt; user-supplied page-image transcription. Source ID: `lma-st-mary-harrow-register-dro003`.
[^lma-cripplegate-1640]: Parish register, St Giles Cripplegate, City of London, burials 1634-1646, London Metropolitan Archives P69/GIS/A/002/MS06419/003; Ancestry.com collection 1624 record 6607796, https://www.ancestry.com/search/collections/1624/records/6607796; user-supplied page-image assessment. Source ID: `lma-st-giles-cripplegate-register-p69-gis-a-002`.
```

In the same G13 file, in the `## Sources Consulted` table, append the following rows (preserve the existing table format):

```markdown
| `torrey-new-england-marriages-prior-1700` | Page 331 Gurney block | `sources/validations/torrey-new-england-marriages-prior-1700.md` |
| `history-of-weymouth` | Vol. 3 Genealogy of Weymouth families, John1, Richard2, John3, Zachariah3, Zachariah4 entries | `sources/validations/history-of-weymouth.md` |
| `lma-st-mary-harrow-register-dro003` | Burials 1668/9, John & Mary Gurney of Okington, two children | `sources/validations/lma-st-mary-harrow-register-dro003.md` |
| `lma-st-giles-cripplegate-register-p69-gis-a-002` | Burial Dec 1640, John son of Francis Garney joiner | `sources/validations/lma-st-giles-cripplegate-register-p69-gis-a-002.md` |
| `findagrave-john-gurney-252975617` | Memorial 252975617, Elm Street Cemetery and 1615/Brent tradition | `sources/validations/findagrave-john-gurney-252975617.md` |
```

In the same G13 file, in the `## Negative Results and Exclusions` list, append:

```markdown
- **No primary record yet supports the recurring 1615 birth tradition.** Both *American Biography* vol. 26 and Find a Grave memorial 252975617 give 29 September 1615; both are derivative; the 1653 deposition's "aged about 50 years" remains the controlling age evidence.
```

## Research operations - G12 Richard Gurney

In `research/people/g12-richard-gurney-fact-sheet.research.md`, append this section before the `---` separator above `## Open Questions`:

```markdown
### Children list and death-year conflict from History of Weymouth and Torrey

The 1923 *History of Weymouth*, Vol. 3, "Genealogy of Weymouth families," gives Richard Gurney a children-list and a death year that both conflict with this file and with the G13 companion. Weymouth says Richard "died at Weymouth in Oct. 1719" and lists three Weymouth-born children: Richard3 b. 18 Jan. 1656; John b. near 1658; Zachariah b. near 1660. Torrey's *New England Marriages Prior to 1700*, page 331, gives Richard's death year as 1691 and his marriage to Rebecca Taylor "b 1656(7?), b 1654" at Weymouth.

The conflicts are real and should be preserved rather than silently merged:

- Death year. Torrey: -1691. *History of Weymouth*: Oct. 1719. The G13 companion currently follows Torrey ("Died intestate October 1691"). The Weymouth 1719 date may reflect the death of his son Richard3 (b. 18 Jan. 1656) being conflated with the father, or it may be a separate well-grounded town-record date. Plymouth County or Suffolk County probate is the right next step before changing the preferred year.
- Children list. The G13 companion currently lists Richard's children as John (killed at the Mendon massacre 1675), Zachariah, Joseph (b. 22 Feb. 1664/65), Mary (b. 9 Sept. 1667), and Benjamin (G11, c. 1676). Weymouth gives only Richard, John, and Zachariah. Joseph, Mary, and Benjamin are absent from Weymouth's three-child list. Treat Weymouth as a confirmed-eldest-three sequence with explicit Weymouth-recorded birth dates rather than a closed list.
- Surname spellings. Weymouth notes the surname "is found spelled Garey, Garry, Gerry, and Gurny." Use this when searching New England town and probate records for Richard.
- Wife. Weymouth gives "Rebecca Taylor, probably daughter of John and Phebe Taylor of Weymouth." This is the first explicit Phebe Taylor parent name preserved here for Rebecca and matches the existing 1688 Taylor will lead.[^history-of-weymouth-g12][^torrey-g12]

[^history-of-weymouth-g12]: *History of Weymouth, Massachusetts*, 4 vols. (Weymouth, Mass.: Weymouth Historical Society, 1923), Vol. 3, Genealogy of Weymouth families, Richard Gurney entry; Ancestry.com collection 21610 image dvm_LocHist007443-00634-1, https://www.ancestry.com/imageviewer/collections/21610/images/dvm_LocHist007443-00634-1; transcribed extract at `sources/corpus_supplement/history-of-weymouth-vol3-gurney.md`. Source ID: `history-of-weymouth`.
[^torrey-g12]: Clarence Almon Torrey, *New England Marriages Prior to 1700* (Baltimore: Genealogical Publishing Co., 2004), p. 331, Richard Gurney entry; Ancestry.com collection 3824 image gpc_newenglandmarriages-0347 (pId=51825), https://www.ancestry.com/imageviewer/collections/3824/images/gpc_newenglandmarriages-0347?pId=51825; transcribed extract at `sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md`. Source ID: `torrey-new-england-marriages-prior-1700`.
```

In the same G12 file, in the `## Open Questions` list, append:

```markdown
6. **Reconcile Richard's death year**: Torrey gives -1691; *History of Weymouth* gives Oct. 1719. Plymouth County and Suffolk County probate, plus Weymouth town-meeting and vital records, are the right places to test which year belongs to Richard2 the father and which (if either) belongs to Richard3 his son b. 18 Jan. 1656.
7. **Children of Richard2**: confirm whether Joseph (b. 22 Feb. 1664/65), Mary (b. 9 Sept. 1667), and Benjamin (G11, c. 1676) belong to Richard2 alongside the Weymouth-listed Richard3 (b. 18 Jan. 1656), John (b. near 1658), and Zachariah (b. near 1660); examine the underlying Weymouth town and church records.
```

In the same G12 file, in the `## Sources Consulted` block, append:

```markdown
- *History of Weymouth, Massachusetts*, Vol. 3 Genealogy of Weymouth families, Richard Gurney entry. Source ID `history-of-weymouth`. Transcribed extract at `sources/corpus_supplement/history-of-weymouth-vol3-gurney.md`.
- Clarence Almon Torrey, *New England Marriages Prior to 1700*, p. 331, Richard Gurney entry. Source ID `torrey-new-england-marriages-prior-1700`. Transcribed extract at `sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md`.
```

## Research operations - John Gurney case file v4

The case file uses HTML footnotes with explicit numeric IDs. Use the next available footnote numbers in sequence after the highest existing `n66`. The instructions below use `NN1`, `NN2`, `NN3`, `NN4`, and `NN5` as placeholders; phase 2 must replace each placeholder with the next sequential integer (almost certainly 67, 68, 69, 70, 71 in this file's current state) and update both the `id="nNN"` attributes and the matching `ref-NN` superscripts.

### 1. Add Find a Grave row to "10.7 Evidence Summary - For Candidate B" table

In the `#### For Candidate B` table, immediately after the existing row 17 (American Gurney arms), append:

```markdown
| 18 | Find a Grave 252975617 burial at Elm Street Cemetery, Braintree | Weak positive (location); weak negative (1615/Brent tradition) | Memorial gives Elm Street Cemetery as the burial place, a new datum to test against parish/town records. The same memorial repeats the problematic 1615/London tradition (anachronistic "Borough of Brent"), reinforcing that this tradition is derivative rather than primary. |
```

### 2. Add Torrey + Weymouth supplementary block to "10.7 Evidence Summary"

Insert this block in `### 10.7 Evidence Summary`, immediately before the `#### Against Candidate B` heading. Replace `NN1` with the next available footnote number.

```html
<h4>Torrey and History of Weymouth: cross-checks on the John1 family group</h4>
<p>Two compiled New England sources independently restate the John1 / Richard2 family group used in this case file. Torrey's <em>New England Marriages Prior to 1700</em>, p. 331, gives John (1603-1663) married 12 Nov. 1661 at Braintree to widow Grezell (Fletcher)(Jewell)(Griggs) Kibbee, with her later marrying John Burge in 1667. The same page lists John Jr. of Mendon (-1675?) married to Ruth, with three children John, Samuel, and Mary. The 1923 <em>History of Weymouth</em>, Vol. 3 "Genealogy of Weymouth families," gives John Sr. b. c. 1603, Braintree before 1645, the Weymouth land-grant cluster (East field, mill field, east side of Great Pond, dated as early as 3 Feb. 1651-52, later granted to others), the 12 Feb. 1661 Braintree land sale, the 20 Sept. 1661 death of his unnamed first wife at Braintree, the 12 Nov. 1661 marriage to widow Grissell Kibbee, the 1662-63 death and 16 Mar. 1662-63 inventory, and a five-child sequence: Mary b. near 1628 (m. Daniel Shed, who called John Gurney father); Richard b. near 1630; John b. near 1633, settled in Mendon; Peter b. near 1635; Isaac b. near 1640. Neither source identifies Mary's maiden name. Both are compiled, derivative cross-checks rather than primary record evidence, but together they confirm the family-group skeleton already in this case file. The Mary-Daniel Shed "called John Gurney father" detail is a small but useful relationship statement that should be preserved alongside the existing Sprague p. 695 family-group note.<sup class="fn"><a href="#nNN1" id="ref-NN1">NN1</a></sup></p>
```

### 3. Add Find a Grave + American Biography heading immediately above the existing supplemental heraldic block

Insert immediately above the existing `<h4>Supplemental heraldic family-memory lead: American Gurney arms</h4>` paragraph, in `### 10.7 Evidence Summary`, before the `#### Against Candidate B` table. Replace `NN2` with the next available footnote number.

```html
<h4>Supplemental burial-place lead: Elm Street Cemetery, Braintree</h4>
<p>Find a Grave memorial 252975617 records John Gurney's burial at Elm Street Cemetery, Braintree, Norfolk County, Massachusetts. This is a new datum for this case file; previously only the death year and the 16 Mar. 1662/63 inventory date were preserved. The same memorial gives a 29 September 1615 birth in "London Borough of Brent, Greater London, England," the same tradition repeated in <em>American Biography</em> vol. 26. The "Borough of Brent" place name is anachronistic (Brent is a 1965 London administrative creation) and the 1615 birth is incompatible with the older-father chronology developed in this case file from the 1653 "aged about 50" deposition. Treat the cemetery line as a citation-worthy lead for a Braintree town or burial-ground record search; treat the 1615/Brent line as a recurring derivative tradition rather than a controlling fact.<sup class="fn"><a href="#nNN2" id="ref-NN2">NN2</a></sup></p>
```

### 4. Add two same-name eliminations to "8. PROCESS OF ELIMINATION"

In the `<h2 id="s9">8. PROCESS OF ELIMINATION: OTHER JOHN GURNEYS</h2>` section, append the following rows to the same-name elimination table that begins at `| John Gurney | Location | Wife | Status | Primary Elimination Reason |`. Replace `NN3` and `NN4` with the next two available footnote numbers.

```markdown
| Harrow on the Hill, Middlesex / "Okington" | Middlesex (residence "Okington/Oakington") | **Mary** | **ELIMINATED** | A John & Mary Gurney "of Okington" buried two children at St Mary Harrow on the Hill in early 1669 (Old Style 1668): Ann/Anne 30 Jan. 1668/9 and Isaac 8 Feb. 1668/9. Active in England in 1669, six years after John Gurney-1's 1662/3 Braintree death.<sup class="fn"><a href="#nNN3" id="ref-NN3">NN3</a></sup> |
| St Giles Cripplegate, London (Francis Garney *joiner*) | London | — | **ELIMINATED** | Burial 15/16 Dec 1640 of "John sonne of ffrancis Garney Joyner." A London child burial; father's trade is joiner, distinct from the case file's existing Francis B "laceweaver" Cripplegate cluster.<sup class="fn"><a href="#nNN4" id="ref-NN4">NN4</a></sup> |
```

### 5. Add a clarifying sentence to "9. SEPARATING THE TWO FRANCIS GURNEYS"

Append the following paragraph immediately after the table in `<h2 id="s10">9. SEPARATING THE TWO FRANCIS GURNEYS</h2>` and immediately after the existing sentence "This distinction, first identified by Walter Rye, is essential for avoiding false attributions." Replace `NN5` with the next available footnote number.

```html
<p>A 1640 St Giles Cripplegate burial entry adds a likely third Francis to the same parish neighborhood. The entry "John sonne of ffrancis Garney Joyner - 15" buries a London child of a Francis Garney whose trade is joiner, not laceweaver. The Garney spelling sits inside the Gurney/Gurny/Gourney/Garney cluster, and the trade difference means this Francis is not the laceweaver Francis B already eliminated above. Keep him visible as a separate Cripplegate-area Francis Gurney/Garney when searching London same-name households.<sup class="fn"><a href="#nNN5" id="ref-NN5">NN5</a></sup></p>
```

### 6. Add five citation entries to the CITATION INDEX

Append the following five `<li>` entries to the `<ol class="endnotes">` block at `<h2 id="citation-index">CITATION INDEX</h2>`, in the same `NN1`-`NN5` order used above. Replace each `NN` placeholder with the matching sequential integer.

```html
<li id="nNN1" value="NN1">Clarence Almon Torrey, <em>New England Marriages Prior to 1700</em> (Baltimore: Genealogical Publishing Co., 2004), p. 331, Gurney entries; Ancestry.com collection 3824 image gpc_newenglandmarriages-0347, pId=51825, <a href="https://www.ancestry.com/imageviewer/collections/3824/images/gpc_newenglandmarriages-0347?pId=51825">https://www.ancestry.com/imageviewer/collections/3824/images/gpc_newenglandmarriages-0347?pId=51825</a>; <em>History of Weymouth, Massachusetts</em>, 4 vols. (Weymouth, Mass.: Weymouth Historical Society, 1923), Vol. 3, Genealogy of Weymouth families, John Gurney Sr. and Richard Gurney entries; Ancestry.com collection 21610 image dvm_LocHist007443-00634-1, <a href="https://www.ancestry.com/imageviewer/collections/21610/images/dvm_LocHist007443-00634-1">https://www.ancestry.com/imageviewer/collections/21610/images/dvm_LocHist007443-00634-1</a>; transcribed extracts at <code>sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md</code> and <code>sources/corpus_supplement/history-of-weymouth-vol3-gurney.md</code>. Source IDs: <code>torrey-new-england-marriages-prior-1700</code>; <code>history-of-weymouth</code>. <a class="backref" href="#ref-NN1">↩</a></li>
<li id="nNN2" value="NN2">Find a Grave, memorial 252975617, John Gurney, Elm Street Cemetery, Braintree, Norfolk County, Massachusetts, <a href="https://www.findagrave.com/memorial/252975617/john-gurney">https://www.findagrave.com/memorial/252975617/john-gurney</a>; cemetery page <a href="https://www.findagrave.com/cemetery/1960540/elm-street-cemetery">https://www.findagrave.com/cemetery/1960540/elm-street-cemetery</a>; cross-reference <em>American Biography: A New Cyclopedia</em>, illustrated vol. 26 (New York: The American Historical Society, Inc., 1926), David Allston Gurney/Gurney family entry, pp. 230-255. Source IDs: <code>findagrave-john-gurney-252975617</code>; <code>american-biography-cyclopedia-v26-gurney-1926</code>. <a class="backref" href="#ref-NN2">↩</a></li>
<li id="nNN3" value="NN3">Parish register, St Mary, Harrow on the Hill, Middlesex, burials 1668 (Old Style; modern year 1669), London Metropolitan Archives DRO/003/A/01/005, page 139; Ancestry.com collection 1624 record 602728549, <a href="https://www.ancestry.com/search/collections/1624/records/602728549?tid=181885695&amp;pid=192416501054&amp;ssrc=pt">https://www.ancestry.com/search/collections/1624/records/602728549</a>. Source ID: <code>lma-st-mary-harrow-register-dro003</code>. <a class="backref" href="#ref-NN3">↩</a></li>
<li id="nNN4" value="NN4">Parish register, St Giles Cripplegate, City of London, burials 1634-1646, London Metropolitan Archives P69/GIS/A/002/MS06419/003, page 77; Ancestry.com collection 1624 record 6607796, <a href="https://www.ancestry.com/search/collections/1624/records/6607796">https://www.ancestry.com/search/collections/1624/records/6607796</a>. Source ID: <code>lma-st-giles-cripplegate-register-p69-gis-a-002</code>. <a class="backref" href="#ref-NN4">↩</a></li>
<li id="nNN5" value="NN5">Parish register, St Giles Cripplegate, City of London, P69/GIS/A/002/MS06419/003, page 77, burial of "John sonne of ffrancis Garney Joyner" December 1640. Source ID: <code>lma-st-giles-cripplegate-register-p69-gis-a-002</code>. <a class="backref" href="#ref-NN5">↩</a></li>
```

### 7. Add Find a Grave / Elm Street Cemetery item to "13.2 Primary Source Records"

Append this row to the `### 13.2 Primary Source Records` table at the end of section 13:

```markdown
| 11 | John Gurney burial - Elm Street Cemetery, Braintree | Find a Grave memorial 252975617 | Burial place lead |
```

## Open issues for phase 2

- The `Sprague, p. 695` John Gurney family-group statement is currently cited inside `n8` of the case file. The History of Weymouth Vol. 3 transcript above re-confirms the same five-child sequence and adds Daniel Shed's "called John Gurney father" detail. Phase 2 may, but is not required to, expand `n8`'s text to mention the Weymouth source explicitly; this is a citation-strengthening pass and can be left to a later citation-rigour run.
- The "Weymouth Hist 3:251" citation form used in the existing G13 and G12 files does not match the page-image transcribed here (Vol. 3, Genealogy of Weymouth families). If the page image is later captured directly, update the page reference in the existing files and in the case file's text accordingly; do not change the page number speculatively in this phase.
- The Richard G12 death-year conflict (Torrey 1691 vs Weymouth 1719) is preserved as a conflict, not resolved. No `data/ancestors v26.json` change is requested in this phase.
- The St Mary Harrow place name "Okington/Oakington" is preserved as transcribed; do not silently normalize to Oakington, Cambridgeshire.
- No `sources/media/` files are staged in this patchset (all extracts are from user-supplied transcripts of online record images).
- No `data/ancestors v26.json`, `data/places.json`, or `data/places_detail.json` edits are part of this patchset.

## Phase 2 application checklist

- [ ] Update `data/sources.json`: insert four new entries; replace `history-of-weymouth` block; bump `meta.lastUpdated`.
- [ ] Create `sources/corpus_supplement/torrey-new-england-marriages-prior-1700-page-331-gurney.md`.
- [ ] Create `sources/corpus_supplement/history-of-weymouth-vol3-gurney.md`.
- [ ] Create `sources/validations/torrey-new-england-marriages-prior-1700.md`.
- [ ] Create `sources/validations/lma-st-mary-harrow-register-dro003.md`.
- [ ] Create `sources/validations/lma-st-giles-cripplegate-register-p69-gis-a-002.md`.
- [ ] Create `sources/validations/findagrave-john-gurney-252975617.md`.
- [ ] Create `sources/validations/history-of-weymouth.md`.
- [ ] Apply five edits to `research/people/g13-john-gurney-fact-sheet.research.md` (Find a Grave block, Torrey block, same-name elimination block, Sources Consulted rows, Negative Results bullet).
- [ ] Apply three edits to `research/people/g12-richard-gurney-fact-sheet.research.md` (children/death conflict block, two Open Questions rows, two Sources Consulted bullets).
- [ ] Apply seven edits to `research/case-files/john-gurney-case-file-v4.md` (For Candidate B row 18, Torrey/Weymouth h4 block, Find a Grave h4 block, two Other Johns rows, Two Francises paragraph, five citation index entries, Primary Source Records row 11). Resolve the `NN1`-`NN5` placeholders by allocating the next sequential integers after the highest existing footnote ID in the file.
- [ ] Copy raw lead file to `sources/intake/archive/v11-future-research-urls4.md`.
