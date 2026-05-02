# Intake patchset v08a - Future research URLs 2 audit supplement

```yaml
patchset_id: v08a
created: 2026-05-02
parent_patchset: sources/intake/processed/v08-future-research-urls2.patchset.md
phase: 1 audit supplement only
reason: Correct under-extracted facts and demoted user-supplied source text in v08.
rule: Apply this supplement with v08; where instructions conflict, v08a supersedes v08.
```

## Audit corrections

1. User-supplied extracts are acceptable evidence for intake promotion when the source association is clear. Do not mark them as "unverified" solely because the external site or book image was inaccessible to tooling.
2. For the Baxter extract, the supplied image is the book image. Do not require later image verification. If quoting exact wording, check the quote against the supplied crop and normalize OCR slips only outside quotation marks.
3. Promote the supplied 1066 Gournay people-page text and the supplied HCommons/JNR Chetham article text.
4. Add `rigler-gurney-family-aaron-zuinglius-1994` as a key source for the G4-G13 American-line ancestors, even though the book text was not readable in this pass.
5. Expand research blocks so all lead facts are represented in research, not just in validations.

## Source registry corrections

### Update `anderson-great-migration-begins-v1-baxter`

Replace the v08 source object with:

```json
"anderson-great-migration-begins-v1-baxter": {
  "shortTitle": "Anderson, Great Migration Begins vol. 1 - Gregory Baxter",
  "citation": "Anderson, Robert Charles. The Great Migration Begins: Immigrants to New England, 1620-1633. Vol. 1. Boston: New England Historic Genealogical Society, 2012, Gregory Baxter profile, p. 138.",
  "archive": "Internet Archive print-disabled item; user-supplied book-image crop",
  "url": "https://archive.org/details/greatmigrationbe0001robe",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/anderson-great-migration-begins-v1-baxter-user-extract.md",
  "mediaPath": null,
  "validationPath": "sources/validations/anderson-great-migration-begins-v1-baxter.md",
  "notes": "User-supplied image crop from the Gregory Baxter profile shows John Gurney as a witness to Baxter's 1659 will and as one of the 7 July 1659 inventory takers. No later book-image verification is required for the retained facts; quote wording should be checked against the supplied crop."
}
```

### Update `rigler-gurney-family-aaron-zuinglius-1994`

Replace the v08 notes field with:

```json
"notes": "Key compiled genealogy for descendants of Richard Gurney of Weymouth, Massachusetts. Treat as a standing key source for G4-G13 American-line research companions and the G6 William Gurney case file. Internet Archive item text was not readable in v08; use as a source-control and future-pull entry until pages are checked."
```

### Add `mosaic-dvd-hugue-de-gournay`

```json
"mosaic-dvd-hugue-de-gournay": {
  "shortTitle": "1066 Mosaic DVD - Hugue de Gournay",
  "citation": "\"Hugue de Gournay.\" 1066 Mosaic DVD people text page.",
  "archive": "1066.co.nz / user-supplied text",
  "url": "https://www.1066.co.nz/Mosaic%20DVD/text/people/gournay.htm",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/mosaic-dvd-hugue-de-gournay-user-text.md",
  "mediaPath": null,
  "validationPath": "sources/validations/mosaic-dvd-hugue-de-gournay.md",
  "notes": "Derivative people-page summary for Hugue/Hugo de Gournay, Battle Abbey Roll context, the senior Gournay line, and the Somerset and Norfolk younger branches. Use as corroborative derivative synthesis only."
}
```

### Add `swann-chethams-library-ms-a4-15-2016`

```json
"swann-chethams-library-ms-a4-15-2016": {
  "shortTitle": "Swann, Chetham's Library MS A.4.15",
  "citation": "Swann, Joel. \"Chetham's Library MS A.4.15: an Inns of Court Manuscript?\" Journal of the Northern Renaissance, 13 February 2016.",
  "archive": "Journal of the Northern Renaissance / HCommons user-supplied capture",
  "url": "https://jnr2.hcommons.org/2016/4231/",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/jnr-chethams-library-ms-a4-15-henry-gurney.md",
  "mediaPath": null,
  "validationPath": "sources/validations/swann-chethams-library-ms-a4-15-2016.md",
  "notes": "Modern manuscript-culture article. Relevant to Henry Gurney's poetry in Chetham's Library MS A.4.15, MC15's Norfolk/East Anglian connections, and transmission between Great Ellingham and wider literary manuscript networks."
}
```

### Update `may-henry-gurney-spenser-2005`

Keep the source, but replace the v08 notes field with:

```json
"notes": "Modern academic article on Henry Gurney and Bodleian MS Tanner 175. User-supplied ResearchGate metadata gives January 2004, Spenser Studies 19:183-216, DOI 10.1086/SPSv20p183. The existing companion and the Chetham/JNR bibliography give Spenser Studies 20 (2005), pp. 183-223. Do not drop either metadata variant; reconcile by DOI/full article before citation cleanup. The abstract says Henry was a poet, critic, and bibliophile at Great Ellingham; MS Tanner 175 preserves his library inventory, more than 600 poems, and verse censures of borrowed books including Foxe, Southwell, Hakluyt, The Faerie Queene, and Mother Hubberds Tale."
```

### Update `cleveland-battle-abbey-roll-v2-gurnay`

Keep the existing source ID. Update the URL to the exact entry URL if not already done:

```json
"url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html"
```

Update the source notes to say:

```json
"notes": "Late-19th-century derivative account of the Gurnay/Gournay lineage. Useful as a synthesis and cross-check, not primary authority. The exact 1066.co.nz Gurnay entry was supplied in v08a and includes substantial detail on the Pays de Bray, Mortemar, Domesday Essex holdings, Gerard/Edith Warenne, the senior line's end, Somerset collateral Gournays, and the Norfolk mesne-lord branch."
```

## Corpus supplement operations

These files have already been prepared in this branch and should be retained/staged in phase 2:

- `sources/corpus_supplement/anderson-great-migration-begins-v1-baxter-user-extract.md`
- `sources/corpus_supplement/mosaic-dvd-hugue-de-gournay-user-text.md`
- `sources/corpus_supplement/jnr-chethams-library-ms-a4-15-henry-gurney.md`

Update `sources/corpus_supplement/hardingham-parish-history-2026.md` by adding:

```markdown
## Supplemental extraction - v08a

The accessible Hardingham parish history page supports these specific facts:

- Hardingham is not named in Domesday, while Flockthorpe is.
- The page identifies the outlier "Mantatestone" with modern Manson Green.
- The page identifies the outlier "Swathing" with modern Low Street.
- Between 1066 and 1210, the page identifies two lordships: the De Camois manor of Flockthorpe and the Manor of Gurneys & Swathing.
- In 1210, Flockthorpe became Hardingham.
- The page explains "ham" as a Saxon word for a small village or settlement.
- The Old Hall, opposite the church, is considered late sixteenth century, and the page says the village must originally have formed around this church/Old Hall area.
```

## Research operations

### `research/places/hardingham.md`

Replace the v08 proposed introductory block with this fuller block. Put it near the top, before or at the opening of the existing "Swathing, Low Street, and the Gurneys & Swathings manor" section:

```markdown
Hardingham is now a civil parish in Norfolk's Breckland district, about 12 miles west of Norwich, but the research value of the place is older and more layered than the modern parish name. The Hardingham parish history says Hardingham itself is not named in Domesday, while Flockthorpe is. It identifies the Domesday outlier "Mantatestone" with modern Manson Green, identifies "Swathing" with modern Low Street, and says that between 1066 and 1210 there were two lordships in the local frame: the De Camois manor of Flockthorpe and the Manor of Gurneys & Swathing. In 1210, Flockthorpe became Hardingham, and the page explains "ham" as a Saxon word for a small village or settlement.[^hardingham-parish]

That makes Swathing/Swathings more than a loose alias. In the local-history layer, it is a remembered outlier or settlement name now associated with Low Street; in the manorial layer, it is paired with the Gurney name as the Manor of Gurneys & Swathing; and in the medieval evidence summarized by Blomefield, it appears in land, tenure, free-warren, mill, fold-course, pasture, and life-estate contexts tied to the Gurney descent.[^hardingham-parish][^blomefield-hardingham]

The current parish-history page does not itself state that Swathings was a Saxon parish including parts of Hardingham, Letton, and Cranworth. Preserve that as a source-needed locality lead unless the phase 2 operator has the source for the Letton/Cranworth wording. If sourced, add it here rather than leaving it in validation.

The church/Old Hall setting gives the place a later built-landscape anchor. The parish history places Old Hall opposite St George's Church, considers it late sixteenth century, and says the village must originally have formed around that area. The Faden map extract adds visual context by showing Hardingham, Old Hall, Manson Green, Hardingham Low Common, the church symbol, roads, and watercourses in the late eighteenth-century landscape.[^hardingham-parish][^faden-hardingham]
```

Use these footnotes:

```markdown
[^hardingham-parish]: "A History of Hardingham," Hardingham Parish Council / Hardingham Parish website, https://hardinghamparish.wixsite.com/home/history-of-hardingham-1. Source ID: `hardingham-parish-history-2026`.
[^faden-hardingham]: William Faden, *A Topographical Map of the County of Norfolk*, surveyed by Thomas Donald and Thomas Milne, published London: W. Faden, 1797, Hardingham-area extract supplied at `sources/media/Hardingham c1790 Faden Map.png`; source website http://www.fadensmapofnorfolk.co.uk/. Source ID: `faden-map-norfolk-1797-hardingham`.
```

### `research/places/flushing-ny.md`

Replace the v08 proposed Flushing block with this fuller block:

```markdown
### The Alley, Alley Creek, and the mill landscape

The Alley belongs in the Flushing place file as a working waterfront/creek settlement, not merely as a label in William Gurney's apprenticeship context. Munsell's 1882 Flushing history says a woolen mill was built at "the Alley" by John Bird, who operated it until the mill was destroyed by fire in 1850, causing a reported $10,000 loss and ending the place's manufacturing interests.[^munsell-alley]

The Little Neck Bay history report gives a broader landscape for the same place. Because Little Neck Bay and Alley Creek were navigable, the Alley supported small businesses: two mills, a tavern, a blacksmith and wheelwright, a general store, the first Flushing post office, and about a dozen homes. In 1826 Wyant Van Zandt built a causeway across the creek and salt marshes between Bayside and Douglaston and donated Zion Episcopal Church, which he had built, to local residents.[^nfwf-alley]

The two secondary accounts conflict on the woolen-mill fire. Munsell names John Bird and dates the fire to 1850; the Little Neck Bay report names John Baird and dates the loss of the Alley's large industry to 1827, saying the woolen mill was later replaced by a grist mill. Keep both forms, Bird/Baird and 1850/1827, until a primary local record resolves the discrepancy.[^munsell-alley][^nfwf-alley]

The Little Neck Bay report also carries the Alley forward after the mill era. In 1858 William Buhrmann and his wife Mary Loweree bought the general store, which included the post office and an adjoining mill. The store could be reached by boat and by road, carried dry goods, grain, groceries, hardware, and small goods, and the Buhrmann Homestead stood on the west side of Alley Pond.[^nfwf-alley]
```

Use these footnotes:

```markdown
[^munsell-alley]: "The Town and Village of Flushing," in *History of Queens County* (New York: W. W. Munsell & Co., 1882), Flushing section, Brooklyn Genealogy Information Page transcription, https://bklyn-genealogy-info.stevemorse.org/Queens/history/flushing.html. Source ID: `munsell-history-queens-flushing-1882`.
[^nfwf-alley]: *History and Ecology of Little Neck Bay*, final report hosted by the National Fish and Wildlife Foundation, p. 13, https://www.nfwf.org/sites/default/files/finalreports1/7460_2008-0065-004_Report_History_and_Ecology_of_Little_Neck_Bay.pdf. Source ID: `nfwf-little-neck-bay-history-ecology-2008`.
```

### `research/case-files/brigadier-general-william-gurney.md`

Add or revise the Flushing/Alley apprenticeship context so it includes the Bird/Baird conflict and the fuller place facts above. Also add a military-service source block using the New York State Military Museum page:

```markdown
The New York State Military Museum page for the 127th Infantry gives a compact official-service frame for Gurney's regiment. Colonel William Gurney received authority on 10 July 1862 to raise the regiment in New York City. It organized on Staten Island, mustered into United States service for three years on 8 September 1862, and left New York on 10 September. Companies were recruited principally from New York City, Brooklyn, Staten Island/Long Island communities, Huntington, Southampton, Greenport, Riverhead, Sag Harbor, Southold, Mattituck, Orient, Babylon, and Bridgehampton.[^nysmm-127th]

The regiment served first in the defenses of Washington, then in Virginia, and then in South Carolina. The Museum's Phisterer-derived summary places it in the defenses of Washington and Abercrombie's Division, 22nd Corps, from September 1862; Hughston's Brigade, Gurney's Division, Department of Virginia, from April 1863; the 4th, 11th, and 10th Corps in 1863; Folly and Morris Islands and the District of Beaufort from October 1864; Potter's Brigade, Coast Division, Department of the South, from November 1864; and Charleston from March 1865. It was honorably discharged and mustered out at Charleston on 30 June 1865, still commanded by Colonel Gurney.[^nysmm-127th]

The Union Army summary on the same page gives the battle narrative: the 127th served in the Suffolk siege in spring 1863, minor affairs at Diascund Bridge and Nine-mile Ordinary, operations around Charleston Harbor including Fort Wagner and Fort Sumter, Bull's Island, Fort Johnson, Honey Hill, and Deveaux Neck. After Charleston's evacuation, General Sherman ordered the regiment retained as permanent city garrison because of its discipline, and Gurney became post commander. The same summary says the regiment left for war about 1,000 strong and returned with 25 officers and 530 men.[^nysmm-127th]

Loss figures should be preserved in both versions because the page gives two source traditions. Phisterer reports deaths of 23 enlisted men killed in action, 14 enlisted men from wounds, and 1 officer plus 94 enlisted men from disease or other causes, for an aggregate of 132, including 7 enlisted men who died in enemy hands. The Union Army summary gives 35 men killed in action, 1 officer and 94 men dead of disease and other causes, for a total of 130.[^nysmm-127th]
```

Add an open pull under the case-file source leads:

```markdown
- [ ] Pull the "General Orders no. 153 from Headquarters, Department of the South, 1864 November 7" item listed on the New York State Military Museum 127th page. The Museum abstract says it concerns the failed July 1864 attack on Forts Johnson and Simpkins and specifically names Colonel Gurney as the 127th commanding officer on Morris Island who did not accompany the expedition. Do not narrate fault or blame beyond the abstract until the order itself is read.
```

Use this footnote:

```markdown
[^nysmm-127th]: "127th Infantry Regiment," New York State Military Museum and Veterans Research Center, drawing from Frederick Phisterer, *New York in the War of the Rebellion*, 3rd ed. (1912), and *The Union Army*, vol. 2 (1908), https://museum.dmna.ny.gov/unit-history/infantry-2/127th-infantry-regiment. Source ID: `ny-state-military-museum-127th-infantry`.
```

### `research/people/g13-john-gurney-fact-sheet.research.md`

Replace the v08 "Community records in Braintree and Billerica" block with this fuller block:

```markdown
### Community and probate records in Braintree, Billerica, and Suffolk County

The NEHGR 62:94 source pull gives a compact age and court-file anchor for John Gurney. Under Suffolk Court Files item no. 188, the printed note reads: "22d paper. John Gurney of Brayntree aged 50 Yeares or therea-abouts. Dated 17-1-[16]52-3." The age corrects the intake typo that read 60. If the court-file dating follows old-style month numbering, the date is 17 March 1652/3. The record is a strong chronological anchor for a birth around 1602/3 if the stated age was close, and at minimum a direct same-place age witness for John in Braintree in 1652/3.[^nehgr-62-94]

The Gregory Baxter profile in Anderson's *Great Migration Begins* places John Gurney in a 1659 Suffolk probate context. Gregory Baxter's 19 June 1659 will/codicil sequence voided a bequest to "my son Dearing" and gave that land to Baxter's son John. John Gurney witnessed the will with Moses Payne and Richard Brackett; Payne and Brackett also witnessed the codicil. Anderson reports the will as sworn 14 [sic] June 1659, probably 24 June, citing Suffolk Probate Records 1:323.[^anderson-gmb-baxter]

The same Baxter profile says the inventory was taken 7 July 1659 by John Gurney, Moses Paine, and Edmund Quinsey. It totaled 417 pounds 19 shillings, including 315 pounds in real estate: dwelling house, barn, orchard, and 2 1/2 acres of pasture; twenty acres of marsh; twenty-four acres of upland; six acres of plowland; and eighty acres of woodland. The inventory was sworn by Margaret Baxter, Gregory Baxter's widow, and John Baxter, their son, citing Suffolk Probate Records 3:146. For John Gurney, the value is not land ownership but community standing: he was trusted as both probate witness and inventory taker in another household's estate.[^anderson-gmb-baxter]

Hazen's Billerica history gives a separate 1659 town-finance context. On the 10 September 1659 rate for the half payment of the Dudley Farm purchase, John Gurney appears with an assessment of 2-5-10. Hazen explains that the Dudley Farm price was 110 pounds and that the remaining balance of the 55-pound half payment was probably assessed on later town purchasers. This links John to the Billerica purchase-rate context, but it should not be inflated into proof of permanent Billerica residence without the underlying town and land records.[^hazen-billerica]
```

Add a separate same-name/will lead under children or open leads, not as a dismissal:

```markdown
### Mary Gurney / John Lewis of Nevis will lead

The NEHGR vol. 49 "Genealogical Gleanings in England" extract for John Lewis of Nevis, merchant, preserves a same-name family lead that belongs in this companion even though the Mary is not yet identified. The will was dated 21 December 1699 and proved 9 July 1701. It names Lewis's sister Elizabeth Lewis, father Thomas Lewis, kinswoman Grisell Lloyd daughter of James Lloyd of New England, friends Arthur Plomer and William Ling of Nevis as executors in trust, Henry Lloyd of Bristol as sole executor, and witness Thomas Nowell. In the middle of that abstract appears the phrase "Mary Gurney the daughter of John Gurney." Keep this as an unresolved Mary Gurney lead, not as proof that she is John Gurney-1's daughter Mary Shed.[^nehgr-49-john-lewis]
```

Use these footnotes:

```markdown
[^nehgr-62-94]: "Notes: Braintree, Mass., Items," *New England Historical and Genealogical Register*, vol. 62 (January 1908), p. 94, Suffolk Court Files item no. 188, https://archive.org/details/newenglandhisto19unkngoog/page/94/mode/2up. Source ID: `nehgr-62-94`.
[^anderson-gmb-baxter]: Robert Charles Anderson, *The Great Migration Begins: Immigrants to New England, 1620-1633*, vol. 1 (Boston: New England Historic Genealogical Society, 2012), Gregory Baxter profile, p. 138; user-supplied book-image crop transcribed at `sources/corpus_supplement/anderson-great-migration-begins-v1-baxter-user-extract.md`. Source ID: `anderson-great-migration-begins-v1-baxter`.
[^hazen-billerica]: Henry A. Hazen, *History of Billerica, Massachusetts, with a Genealogical Register* (Boston: A. Williams and Co., 1883), historical p. 33 / image p. 54, Internet Archive, https://archive.org/details/historyofbilleri00hazen. Source ID: `hazen-billerica-1883`.
[^nehgr-49-john-lewis]: Henry F. Waters, "Genealogical Gleanings in England," *New England Historical and Genealogical Register*, vol. 49, part 2, John Lewis of Nevis will abstract; user-supplied extract from https://archive.org/details/newenglandhistorv49p2wate/. Source ID: `nehgr-49-genealogical-gleanings-john-lewis`.
```

Update "Target Source Pulls / Not Yet Searched":

```markdown
- `Anderson GMB vol. 1, Gregory Baxter profile, p. 138` - user-supplied book image captured in v08a; no later image verification required for retained facts, but pull Suffolk Probate Records 1:323 and 3:146 when possible.
- `NEHGR 49 John Lewis of Nevis will abstract` - user extract captured in v08a; identify the Mary Gurney relationship if possible.
```

### `research/places/billerica-ma.md`

In the v08 create-file block, expand the Billerica paragraph to:

```markdown
Hazen's printed Billerica history gives the 10 September 1659 rate list for the half payment of the Dudley Farm purchase. John Gurney appears in the list with an assessment of 2-5-10. Hazen frames the list as fulfilling the agreement that later inhabitants should repay the original farm proprietors one-half of the farm's cost. The Dudley Farm price was 110 pounds, so the half-payment target was 55 pounds; Hazen adds that the balance of that 55 pounds was probably assessed on later town purchasers.[^hazen-billerica]
```

### `research/people/g04-lester-sawyer-gurney-jr-fact-sheet.research.md` through `research/people/g13-john-gurney-fact-sheet.research.md`

Add `rigler-gurney-family-aaron-zuinglius-1994` as a key compiled source for every available G4-G13 American-line research file:

- `research/people/g04-lester-sawyer-gurney-jr-fact-sheet.research.md`
- `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`
- `research/case-files/brigadier-general-william-gurney.md` for G6 William Gurney
- `research/people/g07-willis-gurney-fact-sheet.research.md`
- `research/people/g08-amos-gurney-fact-sheet.research.md`
- `research/people/g09-benjamin-gurney-fact-sheet.research.md`
- `research/people/g10-benjamin-gurney-fact-sheet.research.md`
- `research/people/g11-benjamin-gurney-fact-sheet.research.md`
- `research/people/g12-richard-gurney-fact-sheet.research.md`
- `research/people/g13-john-gurney-fact-sheet.research.md`

Use this compact wording in each "Sources Consulted", source catalog, or equivalent source section:

```markdown
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994). Key compiled genealogy for descendants of Richard Gurney of Weymouth, Massachusetts; source ID `rigler-gurney-family-aaron-zuinglius-1994`. Full page-level audit still pending.
```

### `research/topics/anderson-yvery-harpetre-gournay-collateral.md`

Replace the existing short "Cleveland's Battle Abbey Roll as derivative synthesis" section with a fuller extraction:

```markdown
### Cleveland and the 1066 Mosaic pages as derivative Gournay syntheses

The Duchess of Cleveland's *Battle Abbey Roll* entry and the 1066 Mosaic Hugue de Gournay people page are derivative, but together they preserve a dense late-antiquarian synthesis of the senior Gournay tradition and the two younger English branches. They should be used as comparison sources, not as controlling proof where Daniel Gurney, Anderson 1742, Blomefield, or primary records are more precise.[^topic-cleveland][^topic-mosaic-hugue]

Cleveland places the family in the Pays de Bray, in the frontier district of the ancient Forest of Lyons, with Gournay as the head of the barony. The entry says this fief had been allotted to their ancestor by Rollo and that the family held it until Philip Augustus seized it in King John's time. It also preserves the castle tradition of "La Tour Hue," with triple wall and fosse, and presents the castle as an emblem of the frontier strength of the barony.[^topic-cleveland]

Both derivative pages place Hugh/Hue de Gournay at Mortemar/Mortimer in 1054 and at Hastings. Cleveland adds that Wace mentions "li viel Hue de Gornai" at Hastings and says Hugh had earlier invaded England with the fleet supporting the Saxon prince Edward after Canute's death. The people page says Hugo/Hugue bore arms "pure sable," joined William at Hastings, and held Essex manorial grants at Domesday.[^topic-cleveland][^topic-mosaic-hugue]

Cleveland gives useful caution around the Domesday-era Hugh. Norman accounts place "Hue le vieil" mortally wounded at Cardiff in 1074, while Welsh accounts put that battle nearly twenty years later; Cleveland therefore treats him as probably dead before Domesday and the Domesday Essex baron as likely his son. The same entry says this second Hugh ended his life as a monk at Bec.[^topic-cleveland]

For Gerard de Gournay, Cleveland says that in 1089 he was baron of Yarmouth and supported William Rufus against Robert Curthose, surrendering Gournay and other strongholds to Rufus and trying to bring neighboring districts to the king's obedience. In 1096, when Robert pledged Normandy to Rufus and went to the Holy Land, Gerard went with his wife Edith and died on the journey. Cleveland identifies Edith or Editha de Warenne as the Conqueror's granddaughter and gives their children as Hugh, Gundreda the Fair wife of Nigel de Albini, and an unnamed daughter married to Richard Talbot. The 1066 people page gives the same broad family pattern, though its wording about Editha as daughter of William de Warren should be checked against better sources.[^topic-cleveland][^topic-mosaic-hugue]

Cleveland then follows the senior line through later Hughs: the Henry I kinsman whose rights were restored by royal mandate; the rebel of Stephen's reign; the Hugh whose castle was burned in Prince Henry's rebellion in 1173 and who died in 1185; the Hugh at Acre with Richard I; and the later Hugh who lost estates by siding with the barons against King John. The principal line ends with Julian/Juliana de Gournay, wife of William Bardolph; the 1066 people page similarly says the chief male line ended with Julia de Gournay, bride of William Rudolph, baron of Wormegay.[^topic-cleveland][^topic-mosaic-hugue]

The Somerset branch is treated as a collateral line, seated at Englishcombe and Barrow Gurney/Barew-Gurney from Domesday, later associated with Harptree, Farringdon Gurney, and Sir Thomas and Sir Matthew de Gournay. Cleveland stresses confusion around the Harptree/Gournay inheritance and the adoption of the Gournay name in that collateral setting. This belongs with the existing Anderson/Yvery caution: the Somerset material is important Gournay context but not the same as the direct Norfolk junior branch.[^topic-cleveland]

The Norfolk branch is the direct-line-relevant part. Cleveland says the Norfolk Gurneys, who continued in the male line, were originally mesne lords under their baronial cousins and first appear in Norfolk in Henry II's time. It identifies Harpley as coming to Matthew through Rose de Burnham or de Warenne and West Barsham as brought by the Wauncy heiress to Edmund Gourney in the reigns of Edward III and Richard II. It then jumps forward to John Gurney, Norwich silk merchant about 1679, as the refounder of the later Quaker/Norwich banking family through his son Joseph. The people page compresses the same Norfolk branch as the Gurneys of Harpley and West Barsham, with a younger son leading to the Norfolk Gurneys represented by Hudson Gurney of Keswick.[^topic-cleveland][^topic-mosaic-hugue]
```

Add footnote:

```markdown
[^topic-mosaic-hugue]: "Hugue de Gournay," 1066 Mosaic DVD people text page, user-supplied text from https://www.1066.co.nz/Mosaic%20DVD/text/people/gournay.htm. Source ID: `mosaic-dvd-hugue-de-gournay`.
```

### `research/people/g15-henry-gurney-fact-sheet.research.md`

Replace the v08 Henry/Spenser block with this fuller block:

```markdown
### Henry Gurney's manuscripts, library, and poetic circulation

Steven W. May's article on Henry Gurney and Bodleian MS Tanner 175 remains the central modern scholarly source for Henry's literary life. The supplied abstract describes Henry as a previously unknown Elizabethan poet, critic, and bibliophile at Great Ellingham, Norfolk. In the last decade of Elizabeth's reign he entered into Tanner 175 both an inventory of his library and more than 600 of his own poems. Several poems explain his standards for judging good and bad poetry, and he transcribed verse "censures" of more than twenty borrowed books, including works by John Foxe, Robert Southwell, Richard Hakluyt, Edmund Spenser's *The Faerie Queene*, and "Mother Hubberds Tale."[^may-spenser]

The article metadata needs reconciliation rather than simplification. The user-supplied ResearchGate/DOI lead gives January 2004, *Spenser Studies: A Renaissance Poetry Annual* 19:183-216, DOI 10.1086/SPSv20p183. The existing companion and Swann's bibliography cite May 2005, *Spenser Studies* 20:183-223. Preserve both metadata variants until the DOI/full article is checked; do not drop the finding while resolving the citation.[^may-spenser]

Joel Swann's article on Chetham's Library MS A.4.15 adds a second modern manuscript context for Henry's poems. MC15 contains Henry Gurney's poetry on folios 69r-80r in the main poetry section, where the anthology shifts from metropolitan, witty, and Inns-of-Court-associated material to didactic, practical, rural poems on household, family, conduct, seasons, animals, wives, and agriculture. Swann identifies Henry as an amateur poet/farmer, born 1549 and died 1616.[^swann-chetham]

Swann summarizes May's findings in geographic and social terms: Henry began writing poetry in the 1590s at age 43, from the manor of Great Ellingham, just under 20 miles southwest of Norwich and about 100 miles northeast of London. He circulated poems and lent books to a circle of at least two dozen nearby people, with the most distant about 30 miles away in Suffolk. Outside MC15, the poems survive only in Henry's own notebook, though other copies were made, and Henry himself prepared copies for friends and relatives.[^swann-chetham]

The MC15 copies are themselves important. Swann says the Chetham manuscript preserves thirteen of the seventeen agricultural poems found in Henry's own anthology, drawing from poems scattered through Bodleian MS Tanner 175, folios 49v-232v. The MC15 versions are more coherent and organized than their Tanner 175 originals, suggesting at least one intermediary stage between Henry's notebook and the Chetham manuscript. Swann also notes that Henry may have had a London correspondent, giving a plausible route for Great Ellingham verse to enter wider manuscript circulation.[^swann-chetham]

MC15 also changes the scale of Henry's cultural setting. Swann argues that the manuscript should not be read as only an Inns of Court artifact: it has London, Inns, Norfolk, and East Anglian poles. The Gurney poems were copied by hand D, one of the important hands shaping the manuscript, and the ownership trail may point toward Norfolk book-trade or Norfolk ownership contexts before the manuscript reached Richard Farmer and then Chetham's Library. This makes Henry's rural Norfolk poetry part of the manuscript's social background, not merely an odd insertion into a London collection.[^swann-chetham]
```

Use these footnotes:

```markdown
[^may-spenser]: Steven W. May, "Henry Gurney, A Norfolk Farmer, Reads Spenser and Others," *Spenser Studies: A Renaissance Poetry Annual*; user-supplied ResearchGate/DOI lead gives January 2004, vol. 19, pp. 183-216, DOI 10.1086/SPSv20p183; Swann bibliography and existing companion give vol. 20 (2005), pp. 183-223. Source ID: `may-henry-gurney-spenser-2005`.
[^swann-chetham]: Joel Swann, "Chetham's Library MS A.4.15: an Inns of Court Manuscript?" *Journal of the Northern Renaissance*, 13 February 2016, paragraphs 2-4 and 20-38, https://jnr2.hcommons.org/2016/4231/; user-supplied markdown capture summarized at `sources/corpus_supplement/jnr-chethams-library-ms-a4-15-henry-gurney.md`. Source ID: `swann-chethams-library-ms-a4-15-2016`.
```

## Validation note corrections

### `sources/validations/anderson-great-migration-begins-v1-baxter.md`

Replace the v08 limitation with:

```markdown
- Source basis: user-supplied book-image crop from Anderson, *The Great Migration Begins*, vol. 1, Gregory Baxter profile, p. 138. The crop is sufficient for the retained facts. No later image verification is required unless quoting exact wording or resolving OCR/typographic uncertainty.
```

### `sources/validations/nehgr-49-genealogical-gleanings-john-lewis.md`

Replace the v08 limitation with:

```markdown
- Source basis: user-supplied extract from the John Lewis of Nevis will abstract. The extract is sufficient to preserve the Mary Gurney daughter-of-John-Gurney lead in research. Identification with G13's daughter Mary remains unresolved.
```

### `sources/validations/mosaic-dvd-hugue-de-gournay.md`

Create:

```markdown
# 1066 Mosaic DVD Hugue de Gournay validation

- Examined: user-supplied text from https://www.1066.co.nz/Mosaic%20DVD/text/people/gournay.htm, 2026-05-02.
- Scope: derivative summary for Hugue/Hugo de Gournay, Battle Abbey Roll context, the senior Gournay line, and the Somerset and Norfolk younger branches.
- Findings recorded in: `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.
- Limitation: derivative synthesis; use for comparison and source control, not as primary proof where stronger records exist.
- Corpus supplement: `sources/corpus_supplement/mosaic-dvd-hugue-de-gournay-user-text.md`.
```

### `sources/validations/swann-chethams-library-ms-a4-15-2016.md`

Create:

```markdown
# Swann Chetham's Library MS A.4.15 validation

- Examined: user-supplied markdown capture of Joel Swann, "Chetham's Library MS A.4.15: an Inns of Court Manuscript?", *Journal of the Northern Renaissance*, 13 February 2016, https://jnr2.hcommons.org/2016/4231/.
- Scope: Henry Gurney poetry in MC15, relation to Bodleian MS Tanner 175, Great Ellingham literary circle, Norfolk/East Anglia manuscript circulation, and MC15 provenance.
- Findings recorded in: `research/people/g15-henry-gurney-fact-sheet.research.md`.
- Corpus supplement: `sources/corpus_supplement/jnr-chethams-library-ms-a4-15-henry-gurney.md`.
```

## Remaining clarification needed

- The current accessible Hardingham parish page supports Swathing/Low Street and Manor of Gurneys & Swathing, but not the specific wording that Swathings was a Saxon parish once including parts of Hardingham, Letton, and Cranworth. If that wording comes from another source, attach or identify it and phase 2 should promote it as sourced research.
