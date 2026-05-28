**Done:** 2026-05-27 21:30 PT

# v65 patchset — G23-G27 fact-sheet citation realignment

Prepared: 2026-05-28
Phase: 1 preparation
Scope: `fact-sheets/g23-edmund-gurney-fact-sheet.md` through `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`

## Source tracking

Checked target fact sheets, paired research companions, `data/sources.json`, `sources/corpus/`, and `sources/corpus_supplement/`.

No new `data/sources.json` entries are required. The relevant source IDs already exist:

- `dg-rec-pt1`, `dg-rec-pt2`, `dg-rec-supp`
- `blomefield-norfolk`
- `blomefield-norfolk-vol5-pp33-cringleford-berford`
- `history-of-parliament-online-gurney-1386-1421`
- `hop-gurney`
- `norwich-records-hudson-tingey-vol2`
- `farrer-honors-knights-fees-v3-gurnay-extracts`
- `anderson-yvery-1742`

Important source correction for Phase 2: Daniel Gurney pages in the 300s are not the 1858 Supplement. They are Daniel Gurney, *Record of the House of Gournay* (1848), Part II. The actual Supplement starts at p. 725. Existing fact-sheet notes repeatedly say `Supplement (1858), p. 355-374`; those labels must be corrected while preserving the page references.

## Outcomes

| Item | File | Outcome |
|---|---|---|
| 1 | `fact-sheets/g23-edmund-gurney-fact-sheet.md` | promote |
| 2 | `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md` | promote |
| 3 | `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md` | promote |
| 4 | `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md` | promote |
| 5 | `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md` | promote |

## Item 1 — G23 Edmund Gournay

### 1A. Replace Narrative section

File: `fact-sheets/g23-edmund-gurney-fact-sheet.md`

```str_replace
old_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Edmund Gournay is the ancestor who transformed the family's position in Norfolk society. His predecessors at Harpley had been respectable minor gentry — knights and esquires of moderate standing. Edmund became something considerably more: a lawyer of county-wide reputation, retained by the city of Norwich (the Norwich City Treasurers' accounts record him at 20 shillings a year, paid in the same paragraph as Edmund de Clipesby — the lawyer who would be murdered in 1392 by servants of the Bishop of Norwich, with Edmund's son Sir John then threatened with death for trying to open proceedings), by the borough of Bishop's Lynn, and — most impressively of all — by John of Gaunt himself, as steward of the Duke's East Anglian estates.

John of Gaunt needs context. In the 1370s and 1380s, as Edward III declined and the young Richard II struggled to establish himself, Gaunt was effectively the most powerful figure in English public life — controlling revenues, military resources, and political influence on a scale no other subject approached. To be his estate steward for any region was to operate at the highest level of administrative England. Edmund did this for East Anglia for fifteen years.

At the same time, he was accumulating a dense record of royal commissions. The Patent and Close Rolls of Edward III and Richard II mention him repeatedly: appointing him justice of the peace (twice), commissioner for customs fraud, arbitrator between ecclesiastical houses, special commissioner for the queen's manor, and investigator of piracy in Norfolk roads. He was, in the language of the period, a man of business — the kind of trusted, legally trained professional whom both great lords and urban corporations needed to manage their affairs.

His most consequential personal act was his marriage to Katherine de Wauncy. Her family had held West Barsham since before Domesday Book. Through a tragedy of infant mortality — her brother Sir Edmund de Wauncy died in 1372 leaving only a seven-year-old son who also died soon after — the entire West Barsham estate came to Edmund in right of his wife. He became lord of West Barsham and moved the family's primary seat there from Harpley. In 1357 his father-in-law had already settled 100 marks per year from the West Barsham and Denver manors on Edmund and Katherine; by 1375, Edmund was leasing out the manor in a 180-year indenture signed at West Barsham, sealing with the engrailed cross.

He died in May 1387 at West Barsham, directing his burial in the parish church. His will left everything to Katherine, named Osbert de Mundeford and Thomas Kemp as executors, and distributed alms to the poor of the town. His son John V succeeded and built further on Edmund's legal foundations. His second son Robert — the direct ancestor — would in due course inherit when John's line failed.
</section>
new_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Edmund Gournay is the ancestor who transformed the family's position in Norfolk society. His predecessors at Harpley had been respectable minor gentry — knights and esquires of moderate standing. Edmund became something considerably more: a lawyer of county-wide reputation, retained by the city of Norwich (the Norwich City Treasurers' accounts record him at 20 shillings a year, paid in the same paragraph as Edmund de Clipesby), by the borough of Bishop's Lynn, and — most impressively of all — by John of Gaunt himself, as steward or joint steward of the Duke's East Anglian estates almost continuously from 1372 until Edmund's death.<sup class="fn"><a href="#n8" id="ref-8b">8</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>

John of Gaunt needs context. In the 1370s and 1380s, as Edward III declined and the young Richard II struggled to establish himself, Gaunt was effectively the most powerful figure in English public life — controlling revenues, military resources, and political influence on a scale no other subject approached. To be his estate steward for any region was to operate at the highest level of administrative England; Edmund did this for East Anglia for about fifteen years.<sup class="fn"><a href="#n7" id="ref-7c">7</a></sup>

At the same time, he was accumulating a dense record of royal commissions. The Patent and Close Rolls of Edward III and Richard II mention him repeatedly: appointing him justice of the peace, commissioner for customs fraud, arbitrator between ecclesiastical houses, special commissioner for the queen's manor, and investigator of piracy in Norfolk roads. He was, in the language of the period, a man of business — the kind of trusted, legally trained professional whom both great lords and urban corporations needed to manage their affairs.<sup class="fn"><a href="#n10" id="ref-10b">10</a></sup>

His most consequential personal act was his marriage to Katherine de Wauncy. Her family had held West Barsham since before Domesday Book. Through a tragedy of infant mortality — her brother Sir Edmund de Wauncy died in 1372 leaving only a seven-year-old son who also died soon after — the entire West Barsham estate came to Edmund in right of his wife. He became lord of West Barsham and moved the family's primary seat there from Harpley. In 1357 his father-in-law had already settled 100 marks per year from the West Barsham and Denver manors on Edmund and Katherine; by 1375, Edmund was leasing out the manor in a 180-year indenture signed at West Barsham, sealing with the engrailed cross.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>

He died in 1387 at West Barsham, directing burial in the parish church of the Assumption of the Blessed Virgin. The fuller Latin copy of his will names four executors — Katherine his wife, John his son, Osbert de Mundeford, and Thomas Kempe — and adds a vivid burial scene: thirteen poor men in white vestments holding torches around his body, with alms distributed to the poor present at the funeral. It also includes a striking restitution clause directing his heirs to compensate anyone he had unjustly disseised, injured, extorted, or wrongfully detained property from.<sup class="fn"><a href="#n15" id="ref-15">15</a></sup> His son Sir John V succeeded and built further on Edmund's legal foundations. Edmund's second son Robert — the direct ancestor — would in due course inherit when Sir John's line failed.<sup class="fn"><a href="#n11" id="ref-11b">11</a></sup><sup class="fn"><a href="#n12" id="ref-12b">12</a></sup>
</section>
```

### 1B. Correct DG labels in citation notes

File: `fact-sheets/g23-edmund-gurney-fact-sheet.md`

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 357
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 357
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 363
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 363
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), pp. 358–363
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, pp. 358–363
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), pp. 357–358
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, pp. 357–358
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 359
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 359
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 358
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 358
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 374
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 374
```

### 1C. Add full-will citation

File: `fact-sheets/g23-edmund-gurney-fact-sheet.md`

```str_replace
old_string:
  <li id="n14">Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. 5 (London: W. Miller, 1806), pp. 33–39, "Cringleford" / "Berford's Manor"; <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol5/pp33-39">British History Online</a>. Source ID: <code>blomefield-norfolk-vol5-pp33-cringleford-berford</code>. <a class="citation-back" href="#ref-14">↩</a></li>
</ol>
new_string:
  <li id="n14">Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. 5 (London: W. Miller, 1806), pp. 33–39, "Cringleford" / "Berford's Manor"; <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol5/pp33-39">British History Online</a>. Source ID: <code>blomefield-norfolk-vol5-pp33-cringleford-berford</code>. <a class="citation-back" href="#ref-14">↩</a></li>
  <li id="n15">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (1858), Note 118, pp. 789–791, full Latin copy of Edmund Gurnay's will from Harl. MSS. 10, fol. 144 / pencil 148, copied from the decayed Registrum Harsyke. Names Katherine his wife, John his son, Osbert de Mundeford, and Thomas Kempe as executors; specifies thirteen paupers in white vestments holding thirteen torches around the body; and includes the restitution clause for wrongfully detained, extorted, or disseised property. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-15">↩</a></li>
</ol>
```

## Item 2 — G24 John de Gournay IV

### 2A. Replace Narrative section

File: `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`

```str_replace
old_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

John de Gournay IV is one of those ancestors who can be described with confidence but only briefly: the sources give us his parentage, his seat, a specific date in his life, and his son — and little else. He appears first, as a very young child, in a deed of his great-uncle John the Rector in 1331, and he appears again in 1332 (possibly) as the presenter to the Harpley church living. His main documentary moment is the court roll of 9 August 1354, when he sat in judgment at Harpley as lord of the manor for the first time — a record that survives in the Additional Manuscripts of the British Library.

He lived through the mid-14th century's most violent disruptions. Born around the time of the early Hundred Years' War campaigns (Crécy was fought in 1346), he would have been approximately eighteen at the worst year of the Black Death in England (1348–49), which killed something between a third and a half of the country's population. No record of his personal experience of the plague survives.

What John IV's tenure did accomplish — in the most important sense — was to raise and launch his son Edmund into the legal career that would make the family's next great transformation possible. Edmund became a lawyer of sufficient eminence to be retained as steward of John of Gaunt's East Anglian estates and as counsel to the cities of Norwich and Bishop's Lynn (King's Lynn) — men of that calibre did not spring from nowhere, and the stable, respectable gentry household John IV maintained at Harpley provided the platform for Edmund's advancement.

And Edmund married Katherine de Wauncy, heiress of West Barsham — the alliance that brought a new manor, a new fortune, and a new geographic identity to the family. From John IV's death until Francis Gurney's departure for London more than a century later, the Gurneys would be the Gurneys of West Barsham.
</section>
new_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

John de Gournay IV is one of those ancestors who can be described with confidence but only briefly: the sources give us his parentage, his seat, a specific date in his life, and his son — and little else. He appears first in a deed of his great-uncle John the Rector in 1331, and he appears again in 1332 (probably) as the presenter to the Harpley church living.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup> His main documentary moment is the court roll of 9 August 1354, when he sat in judgment at Harpley as lord of the manor for the first time — a record Daniel Gurney traces to Additional Manuscripts at the British Library.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>

He lived through the mid-14th century's violent disruptions: the early Hundred Years' War campaigns and the Black Death of 1348–49. No record of John IV's personal experience of either survives, so the safest picture is not battlefield drama but a Norfolk manor still functioning after plague, with its lord holding court in 1354.<sup class="fn"><a href="#n5" id="ref-5c">5</a></sup>

What John IV's tenure did accomplish — in the most important sense — was to raise and launch his son Edmund into the legal career that made the family's next great transformation possible. Edmund became a lawyer of sufficient eminence to be retained as steward or joint steward of John of Gaunt's East Anglian estates and as counsel to Norwich and Bishop's Lynn (King's Lynn). Men of that calibre did not spring from nowhere; the stable, respectable gentry household John IV maintained at Harpley provided the platform for Edmund's advancement.<sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>

And Edmund married Katherine de Wauncy, heiress of West Barsham — the alliance that brought a new manor, a new fortune, and a new geographic identity to the family. From Edmund's generation onward, the family would be known principally as the Gurneys of West Barsham.<sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>
</section>
```

### 2B. Correct DG labels in citation notes

File: `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858) p. 356
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 356
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 356
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 356
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 355
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 355
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), pp. 357–358
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, pp. 357–358
```

## Item 3 — G25 John de Gournay III

### 3A. Replace Narrative section

File: `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

John de Gournay III is the generation that restored continuity. His father had, for reasons that remain unrecorded, transferred the entire family estate to a clerical brother in 1294 — an act that bypassed the normal path of inheritance for nearly four decades. When Rector John died in 1332, John III stepped forward as his nephew and heir, receiving back the manors of Harpley, Swathings in Hardingham, Hingham-Gurneys, and associated holdings.

The documentary record for John III is sparser than for his more dramatic predecessors, but it is clear and consistent. He first appears in a deed of his uncle John (Rector of Harpley) dated 6 Edward III (1331) — described in DG Part II as John de Gurney Junior, confirming he was alive before the succession. The following year he succeeded to the estates and exercised advowson at Harpley, presenting a new rector in place of his deceased uncle.

He had married Jane de Lexham — daughter of Edmund de Lexham — by 1324 at the latest. The Lexham family were established Norfolk gentry; the Lexhams of Lexham in Norfolk are documented from the early 13th century. This marriage gave John III a son, John IV (G24), who appears in the 1331 deed as a young man and became lord of Harpley in his turn c. 1354.

John III's long life — attested from c. 1300 to at least 1353 — spanned the early decades of the Hundred Years' War, the catastrophic Black Death of 1348–49 (which killed roughly a third of England's population), and the first great parliamentary crises of Edward III's reign. There is no surviving evidence that he participated directly in any of these events, which for a minor Norfolk landholder of the period is not surprising. His legacy was simpler and more durable: he re-established the Gournay line in possession of the Harpley estates and fathered the son who would connect the family to its most consequential medieval alliance — with Katherine de Wauncy and the West Barsham inheritance.
</section>
new_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

John de Gournay III is the generation that restored continuity. His father had, for reasons that remain unrecorded, transferred the family estates to a clerical brother in 1294 — an act that interrupted the normal path of inheritance for nearly four decades. When Rector John died in 1332, John III stood as nephew and heir, receiving back the manors of Harpley, Swathings in Hardingham, Hingham-Gurneys, and associated holdings.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>

The documentary record for John III is sparser than for his more dramatic predecessors, but it is clear and consistent. He first appears in a deed of his uncle John (Rector of Harpley) dated 6 Edward III (1331), and the 1315/16 fine recorded by Blomefield had already settled the Harpley estate on John and his wife Jane in tail.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup> The following year he succeeded to the estates and exercised advowson at Harpley, presenting a new rector in place of his deceased uncle.<sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>

He had married Jane de Lexham — daughter of Edmund de Lexham — by 1324 at the latest, and probably by the 1315/16 fine if Blomefield's account is read literally. This marriage gave John III a son, John IV (G24), who appears in the 1331 deed and became lord of Harpley in his turn by 1354.<sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>

John III's long life — attested from at least the early 14th century to 1353 — spanned the early decades of the Hundred Years' War and the catastrophic Black Death of 1348–49. No surviving record connects him personally to those events, so his documented legacy is simpler and more durable: he re-established the Gournay line in possession of the Harpley estates and fathered the son whose household would launch Edmund Gournay into the family's most consequential medieval alliance, the marriage with Katherine de Wauncy and the West Barsham inheritance.<sup class="fn"><a href="#n2" id="ref-2b">2</a></sup><sup class="fn"><a href="#n8" id="ref-8c">8</a></sup>
</section>
```

### 3B. Correct DG labels in citation notes

File: `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 356
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 356
```

```str_replace
old_string:
Daniel Gurney, <em>Supplement</em> (1858), p. 355
new_string:
Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, p. 355
```

## Item 4 — G26 Sir William de Gournay III

### 4A. Replace Narrative section

File: `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Sir William de Gournay III inherited Harpley and its associated manors from his father Sir John I and held them as a conventional Norfolk knight of the late 13th century. He appears in the records at 14 Edward I (1286) as lord of Gurney's manor in Harpley, Hardingham, and Hingham — the portfolio his family had held since Matthew's marriage to Rose de Burnham a century earlier.

Then, in 1294, he did something unusual. He sold — conveyed for an annuity — every one of his estates to his brother John, a priest who was Rector and Patron of Harpley. The deed transferring these properties survives, and it bears William's seal: an engrailed cross, the first surviving physical impression of the Gournay arms that Daniel Gurney was able to identify. William's father Sir John I had borne the same arms on the Crusade, recorded in a roll of arms, but the seal is the earliest document to carry them.

The motivation for the transfer is unrecorded. Financial difficulties are the most common reason a medieval landowner alienated an entire estate in a single transaction, but William was not destitute — the annuity arrangement suggests he retained a claim on the properties' income for the rest of his life. It may simply be that he had no direct male heir at the time (his son John III appears in a deed of the Rector John in 1331, suggesting he was young or recently born), and he trusted his brother's management of the family seat more than whatever alternative arrangement might have been possible.

The long-term result of the transfer was fortunate. When Rector John died in 1332 without issue, the estates descended to William's son John III — bypassing the celibate clergyman's generation and returning smoothly to the direct line. The Gournay name, the Harpley seat, and the engrailed cross all continued.
</section>
new_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Sir William de Gournay III inherited Harpley and its associated manors from his father Sir John I and held them as a conventional Norfolk knight of the late 13th century. Daniel Gurney's pedigree places him in 14 Edward I (1286) as lord of Gurney's manor in Harpley, Hardingham, and Hingham; the Supplement adds an earlier 1274 warren claim at Hardingham, showing him asserting manorial rights there while his father was still active.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n11" id="ref-11">11</a></sup>

Then, in 1294, he did something unusual. He conveyed all his estates to his brother John, a priest who was Rector and Patron of Harpley, in exchange for an annuity. The deed transferring these properties survives in Daniel Gurney's account, and it bears William's seal: an engrailed cross, the first surviving physical impression of the Gournay arms that Daniel Gurney was able to identify. William's father Sir John I had borne the same arms in an ancient roll of arms, but the seal is the earliest document Daniel found to carry them.<sup class="fn"><a href="#n6" id="ref-6b">6</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup>

The motivation for the transfer is unrecorded. Financial pressure remains plausible, but the surviving evidence is more precise than that: William retained an annuity, Rector John had no heirs of his own, and later settlements returned the estate path to William's son John III. The safest reading is therefore not simple failure but a family estate restructuring whose reasons are now lost.<sup class="fn"><a href="#n6" id="ref-6c">6</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>

The long-term result was fortunate. When Rector John died in 1332 without issue, the estates descended to William's son John III — bypassing the celibate clergyman's generation and returning smoothly to the direct line. The Gournay name, the Harpley seat, and the engrailed cross all continued.<sup class="fn"><a href="#n8" id="ref-8c">8</a></sup>
</section>
```

### 4B. Add 1274 warren note

File: `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`

```str_replace
old_string:
  <li id="n10">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: John III's siblings Edmund and William named; no further details. <a class="citation-back" href="#ref-10">↩</a></li>
</ol>
new_string:
  <li id="n10">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: John III's siblings Edmund and William named; no further details. <a class="citation-back" href="#ref-10">↩</a></li>
  <li id="n11">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (1858), Note 114, p. 787, citing <em>Rotuli Hundredorum</em>, 2 Edward I (1274), vol. I, p. 499: William de Gurnay claimed warren in Hardingham, with the jurors saying they did not know by what warrant. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-11">↩</a></li>
</ol>
```

## Item 5 — G27 Sir John de Gournay I

### 5A. Replace Narrative section

File: `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`

```str_replace
old_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Sir John de Gournay I is the most vivid personality in the junior Norfolk branch since Gerard the Crusader — a man whose career moved, improbably, from armed rebellion against the crown to royal Crusader in the space of a few years, and who left behind him a coat of arms that his descendants bore for the next four centuries.

The crisis of 1264 found many of the English baronage choosing sides in a conflict that had been building for years over the terms of the Provisions of Oxford and the limits of royal authority. John chose Simon de Montfort's side. At Lewes in May 1264, the baronial army captured Henry III himself — a stunning victory. Fourteen months later, at Evesham, de Montfort was killed and the rebellion collapsed. John paid with the forfeiture of South Wootton manor in Norfolk, but escaped more severe consequences that ended the careers of other rebels.

His rehabilitation was rapid and complete. In 1257, before the rebellion, he had already been cited by the Mitford jury for refusing to accept the summons to knighthood — an act that reads less as principled resistance than as a calculation that the costs of knighthood outweighed the benefits. He eventually accepted the rank, and by 1270 he was sufficiently restored to royal favour to join Prince Edward's Crusade to the Holy Land. The king's Patent Roll entry is a formal expression of royal trust: "We have taken into our protection and defence the same John, his men, lands, goods, revenues, and all his possessions." The formula is routine; the fact of its issue is not, for a man who had taken up arms against the crown six years earlier.

The engrailed cross he bore — argent, a cross engrailed gules — appears in an ancient roll of arms that DG judged to be contemporary with Sir John. Whether he adopted it at the Crusade, inherited it from a father who bore it earlier, or took it from the Norfolk heraldic environment (where engrailed crosses were common among families with Baconsthorpe and Ufford connections) is debated. What is certain is that Sir John is the earliest member of the family for whom the arms are attested, and that from him they passed unchanged to every subsequent generation of the Norfolk Gurneys.
</section>
new_string:
<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Sir John de Gournay I is the most vivid personality in the junior Norfolk branch since Gerard the Crusader — a man whose career moved, improbably, from armed rebellion against the crown to royal Crusader in the space of a few years, and who left behind him a coat of arms that his descendants bore for the next four centuries.<sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>

The crisis of 1264 found many of the English baronage choosing sides in a conflict that had been building for years over the terms of the Provisions of Oxford and the limits of royal authority. John chose Simon de Montfort's side. At Lewes in May 1264, the baronial army captured Henry III himself; after Evesham in August 1265, the rebellion collapsed and royalist officers treated John's South Wootton manor as the land of the king's enemy.<sup class="fn"><a href="#n5" id="ref-5b">5</a></sup> The South Wootton plea is unusually vivid: it records the seizure of horses, oxen, cows, sheep, grain, and other goods from the manor, and it preserves the explanation that John had been in the conflict of Lewes against the king and elsewhere afterward.<sup class="fn"><a href="#n5" id="ref-5c">5</a></sup>

His rehabilitation was rapid and complete. In 1257, before the rebellion, he had already been cited by the Mitford jury for refusing to accept the summons to knighthood — an act that reads less as principled resistance than as a calculation that the costs of knighthood outweighed the benefits. He eventually accepted the rank, and by 1270 he was sufficiently restored to royal favour to join Prince Edward's Crusade to the Holy Land. The king's Patent Roll entry is a formal expression of royal protection for John's men, lands, goods, revenues, and possessions during the expedition.<sup class="fn"><a href="#n7" id="ref-7b">7</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>

John's authority at Harpley was not only manorial but ecclesiastical. In 3 Edward I (1274/5), James Anderson's 1742 *House of Yvery* records a suit between John and the Prior of Lewes over the right of presentation to Harpley church. Trial by battle was appointed; the parties came armed into the field; and the Prior yielded the advowson to John and his successors. The account is late printed testimony rather than the original plea roll, but it predates Daniel Gurney by more than a century and fits the Harpley tenure pattern documented in the Hundred Rolls.<sup class="fn"><a href="#n12" id="ref-12b">12</a></sup>

The engrailed cross he bore — argent, a cross engrailed gules — appears in an ancient roll of arms that Daniel Gurney judged to be contemporary with Sir John. Whether he adopted it at the Crusade, inherited it from a father who bore it earlier, or took it from the Norfolk heraldic environment is debated. What is certain is that Sir John is the earliest member of the family for whom the arms are attested, and that from him they passed unchanged to every subsequent generation of the Norfolk Gurneys.<sup class="fn"><a href="#n6" id="ref-6c">6</a></sup>
</section>
```

## Audit / review list

These claims are not demoted by this patchset, but Phase 2 or a later audit should keep them visible:

- G23 Bishop's Lynn counsel: the fact sheet cites History of Parliament and project knowledge for Lynn, but the exact local primary/supporting extract is not isolated in the current note. Next pull: source behind HoP's Bishop's Lynn phrase, likely borough accounts or HoP note chain (Unknown online).
- G23 "John of Gaunt was the most powerful man in England after the king": historically reasonable contextual prose, but not itself source-attached beyond HoP's stewardship claim. No action needed unless the prose is later made more specific.
- G24 and G25 Black Death casualty framing: previous drafts used broad casualty estimates without a registered source. This patchset softens the prose to avoid needing a new general-history source.
- G25 Lexham family status: the previous narrative said the Lexhams were documented from the early 13th century. This patchset removes that unsupported specificity and keeps the directly sourced Jane de Lexham marriage.
- G26 transfer motive: previous prose leaned toward financial difficulty and "no direct male heir" logic. This patchset softens to a family estate restructuring because the motive is not directly recorded.
- G27 Anderson trial-by-battle account: strong enough to retain with attribution, but the underlying *Placita de Banco*, Norfolk, 3 Edward I, "de Ecclesia de Harpeli" remains the best primary pull (Unknown online; likely TNA CP 40 series).

## Phase 2 validation checklist

- Apply the literal replacements above.
- Run a targeted anchor sweep for G23-G27: every `href="#n..."` target exists; every `id="ref-..."` is unique; no duplicate note IDs.
- Confirm no `Daniel Gurney, <em>Supplement</em> (1858), p. 3xx` labels remain in G23-G27.
- Run `git diff --check`.
- Run `npm.cmd run validate` from `site/website`.
- Run `npm.cmd run package` from `site/website`.
