**Done:** 2026-05-27 21:30 PT

# v66 patchset — G23-G27 citation realignment supplement

Prepared: 2026-05-28
Phase: 1 preparation
Scope: surgical supplement to `v65-g23-g27-factsheet-citation-realignment.patchset.md`

## Application order

Apply `sources/intake/processed/v65-g23-g27-factsheet-citation-realignment.patchset.md` first. Then apply this supplement.

This supplement does not replace v65. It tightens a few prose sentences that still read too academic, adds better non-Daniel-Gurney citation representation, and records the open-pull results from the previous audit list.

## Source tracking

Checked broader repo material in `sources/intake/done/`, `sources/intake/processed/Ready/`, `sources/validations/`, `research/places/harpley.md`, `research/topics/anderson-yvery-harpetre-gournay-collateral.md`, `sources/corpus/`, `sources/corpus_supplement/`, and `data/sources.json`.

No new `data/sources.json` entries are required. This supplement adds or strengthens citations to already-registered non-DG sources:

- `history-of-parliament-online-gurney-1386-1421`
- `hop-gurney`
- `blomefield-norfolk`
- `norwich-records-hudson-tingey-vol2`
- `ggm-benefice-harpley-church-history`
- `explore-west-norfolk-harpley-st-lawrence`
- `national-churches-trust-harpley-st-lawrence`
- `history-ac-uk-markets-fairs-gazetteer`
- `farrer-honors-knights-fees-v3-gurnay-extracts`
- `anderson-yvery-1742`

## Open-pull results

- **G23 Bishop's Lynn counsel:** no local primary record was found in the repo or quick web pass. The best current non-DG support is L. S. Woodger's History of Parliament biography of Sir John Gurney (d.1408), which states that Edmund's counsel had been sought by Norwich and Bishop's Lynn. This supplement makes that explicit in notes `n7` and `n8`.
- **G27 Harpley trial-by-battle primary:** Anderson's 1742 citation to *Placita de Banco*, Norfolk, 3 Edward I, "de Ecclesia de Harpeli" remains the best available path. The original plea-roll entry was not found digitized in the repo or quick web pass. This supplement keeps Anderson as an attributed non-DG source and tags the plea roll as the future primary pull.
- **G24/G25 Harpley place-memory:** repo-local place research already preserves non-DG Harpley church and market/fair sources. This supplement adds a compact footnote for that material instead of leaving Harpley as only a DG/Blomefield name.

## Outcomes

| Item | File | Outcome |
|---|---|---|
| 1 | `fact-sheets/g23-edmund-gurney-fact-sheet.md` | promote |
| 2 | `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md` | promote |
| 3 | `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md` | promote |
| 4 | `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md` | promote |
| 5 | `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md` | promote |

## Item 1 — G23 Edmund Gournay

### 1A. Make the John of Gaunt paragraph more reader-facing

File: `fact-sheets/g23-edmund-gurney-fact-sheet.md`

```str_replace
old_string:
John of Gaunt needs context. In the 1370s and 1380s, as Edward III declined and the young Richard II struggled to establish himself, Gaunt was effectively the most powerful figure in English public life — controlling revenues, military resources, and political influence on a scale no other subject approached. To be his estate steward for any region was to operate at the highest level of administrative England; Edmund did this for East Anglia for about fifteen years.<sup class="fn"><a href="#n7" id="ref-7c">7</a></sup>
new_string:
Edmund's Gaunt connection is the key to his leap in status. Gaunt was not just another noble employer: in the 1370s and 1380s he was the royal uncle whose lands, household, and political reach made him one of the strongest forces in England. Edmund's job was to help make that East Anglian machinery work.<sup class="fn"><a href="#n7" id="ref-7c">7</a></sup>
```

### 1B. Replace the HoP note with a full non-DG citation

File: `fact-sheets/g23-edmund-gurney-fact-sheet.md`

```str_replace
old_string:
  <li id="n7">History of Parliament Online: Edmund Gurney, d. 1387; stewardship of John of Gaunt's East Anglian estates, 1372–1387. <a class="citation-back" href="#ref-7">↩</a></li>
new_string:
  <li id="n7">L. S. Woodger, "GURNEY, John (d.1408), of Harpley and West Barsham, Norf.," in J. S. Roskell, L. Clark, and C. Rawcliffe, eds., <em>The History of Parliament: The House of Commons 1386-1421</em> (Cambridge: Cambridge University Press, 1993), <a href="https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408">History of Parliament Online</a>. The biography states that Sir John's father Edmund "served John of Gaunt as either steward or joint steward" of the East Anglian estates almost continuously from 1372 to 1387, and also supplies the non-DG support for Edmund's counsel being sought by Norwich and Bishop's Lynn. Source IDs: <code>history-of-parliament-online-gurney-1386-1421</code>, <code>hop-gurney</code>. <a class="citation-back" href="#ref-7">↩</a></li>
```

### 1C. Replace the Norwich/Lynn note ending

File: `fact-sheets/g23-edmund-gurney-fact-sheet.md`

```str_replace
old_string:
  <li id="n8">Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 359: "these two, Clipesby and Gurney, were the standing council for the city of Norwich, in the nature of recorder and steward." The underlying primary record is in the City Treasurers' Accounts at William Hudson and John Cottingham Tingey, eds., <em>The Records of the City of Norwich</em> (Norwich and London: Jarrold, 1910), vol. ii, "Selected Records of the City of Norwich," pp. 44 and 47, recording payment of 20 shillings yearly to "Edmund Gornay for his fee this year" in the same fee paragraph as the 20 shillings paid to Edmund de Clipesby. Internet Archive: <a href="https://archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt">archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt</a>. Bishop's Lynn: cited in project knowledge base and JSON from prior research. <a class="citation-back" href="#ref-8">↩</a></li>
new_string:
  <li id="n8">Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 359: "these two, Clipesby and Gurney, were the standing council for the city of Norwich, in the nature of recorder and steward." The underlying Norwich record is William Hudson and John Cottingham Tingey, eds., <em>The Records of the City of Norwich</em> (Norwich and London: Jarrold, 1910), vol. ii, "Selected Records of the City of Norwich," pp. 44 and 47, recording 20s. yearly to "Edmund Gornay for his fee this year" in the same fee paragraph as Edmund de Clipesby. Internet Archive: <a href="https://archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt">archive.org/stream/recordsofcityofn02norwuoft/recordsofcityofn02norwuoft_djvu.txt</a>. For Bishop's Lynn, use the History of Parliament biography cited in note 7; a local Lynn primary account for the counsel phrase has not yet been isolated. Source IDs: <code>norwich-records-hudson-tingey-vol2</code>, <code>history-of-parliament-online-gurney-1386-1421</code>. <a class="citation-back" href="#ref-8">↩</a></li>
```

## Item 2 — G24 John de Gournay IV

### 2A. Replace the opening paragraph with a lighter version

File: `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`

```str_replace
old_string:
John de Gournay IV is one of those ancestors who can be described with confidence but only briefly: the sources give us his parentage, his seat, a specific date in his life, and his son — and little else. He appears first in a deed of his great-uncle John the Rector in 1331, and he appears again in 1332 (probably) as the presenter to the Harpley church living.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup> His main documentary moment is the court roll of 9 August 1354, when he sat in judgment at Harpley as lord of the manor for the first time — a record Daniel Gurney traces to Additional Manuscripts at the British Library.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>
new_string:
John IV leaves a narrow paper trail, but it has one unusually sharp scene. He appears first in a deed of his great-uncle John the Rector in 1331, and he appears again in 1332 (probably) as the presenter to the Harpley church living.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup> Then comes 9 August 1354: John holding court at Harpley as lord of the manor, not as a name in a pedigree but as the man presiding over tenants, disputes, and local business.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>
```

### 2B. Replace the plague-context paragraph with Harpley place-memory

File: `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`

```str_replace
old_string:
He lived through the mid-14th century's violent disruptions: the early Hundred Years' War campaigns and the Black Death of 1348–49. No record of John IV's personal experience of either survives, so the safest picture is not battlefield drama but a Norfolk manor still functioning after plague, with its lord holding court in 1354.<sup class="fn"><a href="#n5" id="ref-5c">5</a></sup>
new_string:
Harpley gives that spare record some texture. St Lawrence church was not just the nearest parish building; it was the family stage where Gurnays presented clergy, built, prayed, and left their arms in the fabric. Modern church-history sources still preserve that local memory, while Blomefield supplies the older topographical frame.<sup class="fn"><a href="#n9" id="ref-9">9</a></sup>
```

### 2C. Add Harpley place-memory citation

File: `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`

```str_replace
old_string:
  <li id="n8">Daniel Gurney, <em>Record</em> (1848), p. 279; Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, pp. 357–358 (Edmund Gurney chapter). History of Parliament Online: Edmund Gurney, d. 1387. <a class="citation-back" href="#ref-8">↩</a></li>
</ol>
new_string:
  <li id="n8">Daniel Gurney, <em>Record</em> (1848), p. 279; Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, pp. 357–358 (Edmund Gurney chapter). History of Parliament Online: Edmund Gurney, d. 1387. <a class="citation-back" href="#ref-8">↩</a></li>
  <li id="n9">Francis Blomefield, "Freebridge Hundred and Half: Harpley," in <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. 8 (London, 1808), pp. 452–459, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol8/pp452-459">British History Online</a>; "Harpley Church History," GGM Benefice, Harpley, St Lawrence; "The Church of St. Lawrence, Harpley," Explore West Norfolk; and "Harpley St Lawrence," National Churches Trust. These non-DG sources support the Harpley church/place-memory frame: Gurnay patronage, Rector John de Gurnay's chancel association, visible Gurnay/Gurney arms, and the church as the family parish setting. Source IDs: <code>blomefield-norfolk</code>, <code>ggm-benefice-harpley-church-history</code>, <code>explore-west-norfolk-harpley-st-lawrence</code>, <code>national-churches-trust-harpley-st-lawrence</code>. <a class="citation-back" href="#ref-9">↩</a></li>
</ol>
```

## Item 3 — G25 John de Gournay III

### 3A. Replace the first paragraph with a more narrative opening

File: `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
John de Gournay III is the generation that restored continuity. His father had, for reasons that remain unrecorded, transferred the family estates to a clerical brother in 1294 — an act that interrupted the normal path of inheritance for nearly four decades. When Rector John died in 1332, John III stood as nephew and heir, receiving back the manors of Harpley, Swathings in Hardingham, Hingham-Gurneys, and associated holdings.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>
new_string:
John III's story is quieter than his grandfather's rebellion or his son's rise, but it has a satisfying turn: the Harpley lands went sideways to a priest, then came back to the nephew who could carry the family forward. When Rector John died in 1332, John III stood as heir and received back the manors of Harpley, Swathings in Hardingham, Hingham-Gurneys, and associated holdings.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>
```

### 3B. Replace the Jane de Lexham paragraph with clearer source logic

File: `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
He had married Jane de Lexham — daughter of Edmund de Lexham — by 1324 at the latest, and probably by the 1315/16 fine if Blomefield's account is read literally. This marriage gave John III a son, John IV (G24), who appears in the 1331 deed and became lord of Harpley in his turn by 1354.<sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>
new_string:
Jane de Lexham gives this otherwise spare generation one human anchor. She is named in Daniel Gurney's pedigree, and Blomefield's Harpley account independently places John and Jane together in the 1315/16 settlement. Their son John IV (G24) appears in the 1331 deed and became lord of Harpley in his turn by 1354.<sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>
```

## Item 4 — G26 Sir William de Gournay III

### 4A. Replace the 1294 transfer paragraph with a less academic version

File: `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
Then, in 1294, he did something unusual. He conveyed all his estates to his brother John, a priest who was Rector and Patron of Harpley, in exchange for an annuity. The deed transferring these properties survives in Daniel Gurney's account, and it bears William's seal: an engrailed cross, the first surviving physical impression of the Gournay arms that Daniel Gurney was able to identify. William's father Sir John I had borne the same arms in an ancient roll of arms, but the seal is the earliest document Daniel found to carry them.<sup class="fn"><a href="#n6" id="ref-6b">6</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>
new_string:
Then the story takes its odd turn. In 1294 William handed the whole landed package to his brother John, a priest and Rector of Harpley, in return for an annuity. That deed survives in Daniel Gurney's account, and it carries the detail that makes William memorable: his seal, an engrailed cross, the earliest surviving physical impression of the Gournay arms Daniel could identify. William's father Sir John I had already borne the same arms in an ancient roll, but William's seal is the first document Daniel found with the family cross pressed into wax.<sup class="fn"><a href="#n6" id="ref-6b">6</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>
```

### 4B. Add a compact Harpley church citation to the transfer aftermath paragraph

File: `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
The long-term result was fortunate. When Rector John died in 1332 without issue, the estates descended to William's son John III — bypassing the celibate clergyman's generation and returning smoothly to the direct line. The Gournay name, the Harpley seat, and the engrailed cross all continued.<sup class="fn"><a href="#n8" id="ref-8c">8</a></sup>
new_string:
The long-term result was fortunate. When Rector John died in 1332 without issue, the estates descended to William's son John III — bypassing the celibate clergyman's generation and returning smoothly to the direct line. Harpley still remembers that clerical brother: modern church-history sources associate Rector John with the early-14th-century chancel, and the visible Gurnay/Gurney arms keep the family presence in the church fabric.<sup class="fn"><a href="#n8" id="ref-8c">8</a></sup><sup class="fn"><a href="#n12" id="ref-12">12</a></sup>
```

### 4C. Add Harpley church citation

File: `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
  <li id="n11">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (1858), Note 114, p. 787, citing <em>Rotuli Hundredorum</em>, 2 Edward I (1274), vol. I, p. 499: William de Gurnay claimed warren in Hardingham, with the jurors saying they did not know by what warrant. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-11">↩</a></li>
</ol>
new_string:
  <li id="n11">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (1858), Note 114, p. 787, citing <em>Rotuli Hundredorum</em>, 2 Edward I (1274), vol. I, p. 499: William de Gurnay claimed warren in Hardingham, with the jurors saying they did not know by what warrant. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-11">↩</a></li>
  <li id="n12">"Harpley Church History," GGM Benefice, Harpley, St Lawrence; "The Church of St. Lawrence, Harpley," Explore West Norfolk; and "Harpley St Lawrence," National Churches Trust. These local and church-profile sources preserve the tradition that Rector John de Gurnay held the living 1294–1332 and was associated with the early-14th-century chancel; Explore West Norfolk also notes visible Gurney shields in the church fabric. Source IDs: <code>ggm-benefice-harpley-church-history</code>, <code>explore-west-norfolk-harpley-st-lawrence</code>, <code>national-churches-trust-harpley-st-lawrence</code>. <a class="citation-back" href="#ref-12">↩</a></li>
</ol>
```

## Item 5 — G27 Sir John de Gournay I

### 5A. Replace the opening sentence with a less academic line

File: `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`

```str_replace
old_string:
Sir John de Gournay I is the most vivid personality in the junior Norfolk branch since Gerard the Crusader — a man whose career moved, improbably, from armed rebellion against the crown to royal Crusader in the space of a few years, and who left behind him a coat of arms that his descendants bore for the next four centuries.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>
new_string:
Sir John de Gournay I is the page-turner of the junior Norfolk branch: rebel, confiscated landholder, restored royal crusader, and the first man in the line whose red engrailed cross can be pinned to a named person.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>
```

### 5B. Replace the Harpley authority paragraph with a livelier version

File: `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`

```str_replace
old_string:
John's authority at Harpley was not only manorial but ecclesiastical. In 3 Edward I (1274/5), James Anderson's 1742 *House of Yvery* records a suit between John and the Prior of Lewes over the right of presentation to Harpley church. Trial by battle was appointed; the parties came armed into the field; and the Prior yielded the advowson to John and his successors. The account is late printed testimony rather than the original plea roll, but it predates Daniel Gurney by more than a century and fits the Harpley tenure pattern documented in the Hundred Rolls.<sup class="fn"><a href="#n12" id="ref-12b">12</a></sup>
new_string:
Harpley adds another memorable scene. In 3 Edward I (1274/5), James Anderson's 1742 <em>House of Yvery</em> says John and the Prior of Lewes came armed into the field over the right to present the rector of Harpley. The Prior yielded, and the advowson passed to John and his successors. The original plea roll is still the prize to pull, but Anderson's account is an independent pre-DG witness and fits the Harpley tenure pattern documented in the Hundred Rolls.<sup class="fn"><a href="#n12" id="ref-12b">12</a></sup>
```

### 5C. Strengthen the South Wootton/Evesham note with Farrer

File: `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`

```str_replace
old_string:
  <li id="n5">Daniel Gurney, <em>Record</em> (1848), p. 279, and Appendix LXI p. 341. DG-Supp Note 112 (pp. 781–783): full Latin text of the 1264/65 plea (Placita coram Rege, 49 Henry III, No. 124): "<em>quia idem Johannes fuit in conflictu de Lewes contra dominum Regem et alibi post eundem conflictum</em>" -- John de Gurney was in the conflict of Lewes against the lord King and elsewhere after the same conflict. Independently corroborated by William Farrer, <em>Honors and Knights' Fees</em>, vol. 3 (1923–25), Honor of Arundel, p. 142, which records that John de Bulemer answered Alice de Balesham (1265) that he had seized John de Gurney's manor at South Wootton because John "was in the conflict of Evesham against the king" -- naming Evesham where DG's longer plea emphasises Lewes plus post-Lewes resistance. Together the two attestations document the same rebel arc from Lewes 1264 through post-Evesham forfeiture. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>farrer-honors-knights-fees-v3-gurnay-extracts</code>. <a class="citation-back" href="#ref-5">↩</a></li>
new_string:
  <li id="n5">Daniel Gurney, <em>Record</em> (1848), p. 279, and Appendix LXI p. 341. DG-Supp Note 112 (pp. 781–783): full Latin text of the 1264/65 plea (Placita coram Rege, 49 Henry III, No. 124), including the South Wootton livestock and grain seizure and the explanation that John de Gurney was in the conflict of Lewes against the king and elsewhere after it. Independent control: William Farrer, <em>Honors and Knights' Fees</em>, vol. 3 (1923–25), Honor of Arundel, p. 142, records that John de Bulemer answered Alice de Balesham in 1265 that he had seized John de Gurney's South Wootton manor because John "was in the conflict of Evesham against the king." Together the two attestations document the same rebel arc from Lewes through post-Evesham forfeiture pressure. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>farrer-honors-knights-fees-v3-gurnay-extracts</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

### 5D. Strengthen the Anderson note and keep the primary pull visible

File: `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`

```str_replace
old_string:
  <li id="n12">Anderson, James, <em>Genealogical History of the House of Yvery</em>, Vol. II (London, 1742), p. 478, citing <em>Placita de Banco</em>, Norfolk, 3 Edw. I, "de Ecclesia de Harpeli." Predates Daniel Gurney by 106 years. Source ID: <code>anderson-yvery-1742</code>. <a class="citation-back" href="#ref-12">↩</a></li>
new_string:
  <li id="n12">James Anderson, <em>Genealogical History of the House of Yvery: In its Different Branches of Yvery, Luvel, Perceval, and Gournay</em>, vol. II (London: H. Woodfall, Jun., 1742), p. 478, brief Norfolk aside on Matthew, William, and John de Gournay. Anderson says John had a suit with the Prior of Lewes over the right of presentation to Harpley church in 3 Edward I; trial by battle was appointed; both parties came armed into the field; and the Prior yielded the advowson to John and his successors. Anderson cites <em>Placita de Banco</em>, Norfolk, 3 Edward I, "de Ecclesia de Harpeli"; the original plea-roll entry remains the next primary-source pull. Source ID: <code>anderson-yvery-1742</code>. <a class="citation-back" href="#ref-12">↩</a></li>
```

## Remaining audit pulls

- G23 Bishop's Lynn counsel local primary (Unknown online): likely borough/corporation accounts or a HoP note-chain source. Current fact-sheet support should be HoP, not vague project memory.
- G27 *Placita de Banco*, Norfolk, 3 Edward I, "de Ecclesia de Harpeli" (Unknown online): likely TNA CP 40 series. Needed to confirm Anderson's trial-by-battle account at the primary level.
- G25 Lexham background (Available online in part): Daniel Gurney cites Blomefield in Lexham, and public scans of Blomefield vol. 10 appear online. A future patchset can extract the exact Blomefield Lexham parish text if the fact sheet needs more than Jane's name and the Harpley fine.

## Phase 2 validation checklist

- Apply v65 first, then this supplement.
- Run a targeted anchor sweep for G23-G27 after both patchsets: every `href="#n..."` target exists; every `id="ref-..."` is unique; no duplicate note IDs.
- Confirm no `Daniel Gurney, <em>Supplement</em> (1858), p. 3xx` labels remain in G23-G27.
- Run `git diff --check`.
- Run `npm.cmd run validate` from `site/website`.
- Run `npm.cmd run package` from `site/website`.
