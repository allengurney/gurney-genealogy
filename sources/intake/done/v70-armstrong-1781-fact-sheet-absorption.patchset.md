**Done:** 2026-05-28 19:17 PT

# v70 patchset — Armstrong 1781 findings absorbed into fact sheets (G15, G17, G18)

Prepared: 2026-05-28  
Phase: 1 preparation  
Scope: embed the substantively new published-narrative findings from `v69-armstrong-norfolk-1781-vol5-selected-gurney-references.patchset.md` into the affected fact sheets, so the new facts (Edward Gourney's Aug 1641 death + 1637 JP attestation; G17 Anthony's 1541-42 Irstead purchase and 1540 Merton sale; the Heydon sisters' marriage network) are present where human readers will find them — not buried in the corpus supplement.

This is one of three companion patchsets to v69: v70 covers **fact sheets** (this file); v71 will cover **research companions + place files**; v72 will cover **topic files + new research leads + stub housekeeping**.

## Dependency on v69

This patchset assumes the v69 source-entry `armstrong-norfolk-1781` has been added to `data/sources.json` and the corpus supplement is at `sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md`. Phase 2 application of v69 must run first, or in tandem.

## Findings absorbed in v70

| # | Fact sheet | Finding | Armstrong location |
|---|---|---|---|
| 1 | `g15-henry-gurney-fact-sheet.md` | Edward Gournay (G15's grandson, the West Barsham heir) died **August 1641**; full Latin chancel epitaph at West Barsham church names parents Thomas Gourney + Martha Lewknor. | vol. 5 p. ~19 |
| 2 | `g15-henry-gurney-fact-sheet.md` | **Edward Gournay served as a Norfolk Justice of the Peace** — sat at General Sessions at Walsingham Parva, 12 Oct 1637 (13 Charles I), alongside Sir Hamon L'Estrange and Robert Baron, on a Hunstanton rates dispute. First known administrative office attestation for Edward. | vol. 9 p. ~16 |
| 3 | `g17-anthony-gurney-fact-sheet.md` | G17 Anthony Gurney **purchased the manor of Irstead by fine from Sir Richard Southwell in 33 Henry VIII (1541-42)**, with lands in Barton, Neatishead, and Smalburgh — and **died lord of Irstead on 4 Jan 1555/6**. Independently corroborates the death date already cited from Blomefield and supplies the Irstead-acquisition mechanism. | vol. 9 p. ~17 area |
| 4 | `g17-anthony-gurney-fact-sheet.md` | G17 Anthony **sold Merton manor (with the Trinity Church advowson and lands in Riling, Cranworth, Hingham, Carbrooke, and Little Ellingham) to Sir Richard Southwell c. 1540** — the counter-direction estate-rationalisation pair with the 1541-42 Irstead purchase. | vol. 9 p. ~25 |
| 5 | `g17-anthony-gurney-fact-sheet.md` | G17 Anthony was contemporaneously known as **"Anthony Gurney, esq. of North Barsham"** in the Great Ellingham descent (vol. 8 p. ~254) — not solely "of West Barsham" as the project's published narrative tends to render him. The 1525 Great Ellingham inheritance via Margaret Lovell carried the North Barsham seat into the same hands. | vol. 8 p. ~254 |
| 6 | `g18-william-gurney-v-fact-sheet.md` | The **Heydon sister-marriage network** as listed by Armstrong (vol. 3 p. ~120): Amy → Sir Roger Townshend of Hunstanton; Dorothy → Sir Thomas Brook (heir of Lord Cobham); Elizabeth → Walter Hobart of Hales-hall; Ann → William Gurney (G18); Bridget → Sir William Paston. Supplies the four-sister network already implicit in the G18 narrative. | vol. 3 p. ~120 |

Items 1, 2, 3, and 4 are substantively new published-narrative facts; items 5 and 6 are corroborating-citation enrichments.

## Phase 2 operations

### 1. G15 — child-table row 1 (Thomas III note) gets Edward's death date

File: `fact-sheets/g15-henry-gurney-fact-sheet.md`.

```str_replace
old_string:
      <td>Thomas Gurney III</td>
      <td>b. 1572 – d. 1614</td>
      <td>Eldest son. Baptised 15 May 1572 at West Barsham. Married Martha Lewknor of Denham, Suffolk. Died <em>vita patris</em>. His son Edward Gournay (b. 1608) eventually succeeded Henry as heir of West Barsham and Great Ellingham. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup></td>
new_string:
      <td>Thomas Gurney III</td>
      <td>b. 1572 – d. 1614</td>
      <td>Eldest son. Baptised 15 May 1572 at West Barsham. Married Martha Lewknor of Denham, Suffolk. Died <em>vita patris</em>. His son Edward Gournay (b. 1608) eventually succeeded Henry as heir of West Barsham and Great Ellingham; Edward died in August 1641 and is commemorated by a Latin chancel monument at West Barsham church. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup><sup class="fn"><a href="#n19" id="ref-19">19</a></sup></td>
```

### 2. G15 — narrative paragraph absorbs Edward d. 1641 + 1637 JP attestation

File: `fact-sheets/g15-henry-gurney-fact-sheet.md`.

```str_replace
old_string:
Of his twelve children who lived to adulthood, three would shape the family's onward history beyond Norfolk. His eldest son Thomas (sometimes called Thomas III) married Martha Lewknor of Denham, Suffolk, but died in 1614 — a year before his father — leaving Henry's eventual succession to fall on Henry's grandson Edward Gournay (b. 1608). His third son Edmund became one of the more openly Puritan-leaning Norfolk clergy of the early Stuart period, the man whom Thomas Fuller would later remember as the rector who, when told he must always wear his surplice, "came home, and rode a journey with it on." His sixth son Francis (twin to Anthony, G14 in the direct line) was apprenticed to a London Merchant Taylor and would become the bridge to the family's eventual American descent.
new_string:
Of his twelve children who lived to adulthood, three would shape the family's onward history beyond Norfolk. His eldest son Thomas (sometimes called Thomas III) married Martha Lewknor of Denham, Suffolk, but died in 1614 — a year before his father — leaving Henry's eventual succession to fall on Henry's grandson Edward Gournay (b. 1608). Edward succeeded to West Barsham and Great Ellingham; he sat as a Norfolk Justice of the Peace at the General Sessions at Walsingham Parva on 12 October 1637, alongside Sir Hamon L'Estrange of Hunstanton and Robert Baron, four years before his own death in August 1641. The West Barsham seat then passed to Edward's son Henry II for the twenty years until the line failed in 1661; Great Ellingham, by contrast, descended through Henry G15's daughter Margaret (Gurney) Davy of Great Ellingham, and from her through Sir Roger Potts, bart., onward — a divergence in the post-1641 succession of the two principal Gurney manors. <sup class="fn"><a href="#n19" id="ref-19">19</a></sup> His third son Edmund became one of the more openly Puritan-leaning Norfolk clergy of the early Stuart period, the man whom Thomas Fuller would later remember as the rector who, when told he must always wear his surplice, "came home, and rode a journey with it on." His sixth son Francis (twin to Anthony, G14 in the direct line) was apprenticed to a London Merchant Taylor and would become the bridge to the family's eventual American descent.
```

### 3. G15 — append new footnote n19 covering Edward d. 1641 + 1637 JP + Great Ellingham descent

File: `fact-sheets/g15-henry-gurney-fact-sheet.md`.

```str_replace
old_string:
  <li id="n18">William J. Thoms, ed., <em>Anecdotes and Traditions, Illustrative of Early English History and Literature, Derived from MS. Sources</em>, Camden Society, old series, vol. 5 (London: Printed for the Camden Society by J. B. Nichols and Son, 1839), p. 6, no. XI, "A Mathematician Defined," from L'Estrange no. 30; introductory identification of "Parson Edmund Gurney" as Francis Gurney's brother at pp. xviii–xx. <a href="https://archive.org/details/anecdotestraditi00thomrich/">Internet Archive</a>. Source ID: <code>thoms-anecdotes-traditions-1839</code>. <a class="citation-back" href="#ref-18">↩</a></li>
</ol>
new_string:
  <li id="n18">William J. Thoms, ed., <em>Anecdotes and Traditions, Illustrative of Early English History and Literature, Derived from MS. Sources</em>, Camden Society, old series, vol. 5 (London: Printed for the Camden Society by J. B. Nichols and Son, 1839), p. 6, no. XI, "A Mathematician Defined," from L'Estrange no. 30; introductory identification of "Parson Edmund Gurney" as Francis Gurney's brother at pp. xviii–xx. <a href="https://archive.org/details/anecdotestraditi00thomrich/">Internet Archive</a>. Source ID: <code>thoms-anecdotes-traditions-1839</code>. <a class="citation-back" href="#ref-18">↩</a></li>
  <li id="n19">Edward Gournay's August 1641 death is recorded by the Latin chancel monument at West Barsham church, transcribed by Mostyn John Armstrong in <em>The History and Antiquities of the County of Norfolk</em>, vol. 5 (Norwich, 1781), in the Gallow Hundred entry for West Barsham: "Caducum hoc aeternat Marmor Edwardus Gourney, filius et heres Tho. Gourney Armig. et Marthe filie Edu. Lewkenor de Denham, in Com. Suff, Militis, obiit Aug. 1641." Edward as Norfolk Justice of the Peace: Armstrong, vol. 9, Smithdon Hundred, prints the General Sessions order of 12 October 13 Charles I (1637) at Walsingham Parva — "coram Hammone L'Estrange milite, Roberto Baron, et Edwardo Gournay armigeris justiciariis dicti domini regis ad pacem" — on a Hunstanton parish-rates dispute. The post-1641 divergence of West Barsham (Henry II → 1661 extinction) and Great Ellingham (Margaret Gurney → Henry Davy → Mary Davy → Sir Roger Potts, bart. → Francis Colman of Norwich) is recorded by Armstrong in his Great Ellingham parish entry (vol. 8, Shropham Hundred): "After 1641 it went to Margaret Gurney, his aunt, who married Mr. Henry Davy, of Great Ellingham, whose sole daughter and heiress, Mary, married Sir Roger Potts, bart." Armstrong's body-text reading "Edmund died seised of it in the year 1641" at West Barsham is an editorial slip for "Edward," contradicted by the chancel monument printed three paragraphs later on the same page; the corpus extract (`sources/corpus_supplement/armstrong-norfolk-1781-selected-gurney-references.md`) records the slip. Internet Archive items <code>bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5</code>, <code>..._1781_8</code>, and <code>..._1781_9</code>. Source ID: <code>armstrong-norfolk-1781</code>. <a class="citation-back" href="#ref-19">↩</a></li>
</ol>
```

### 4. G15 — extend the Hingham tenure footnote (n3) with Armstrong's 1715 Larwood successor

The existing G15 narrative records Henry as lord of Hingham's "Gurney's Manor" in 1572 (via Blomefield, cited in n3). Armstrong adds the post-Gurney successor by 1715 (Mr. William Larwood, merchant of Norwich). Light-touch addition to n3.

File: `fact-sheets/g15-henry-gurney-fact-sheet.md`.

```str_replace
old_string:
  <li id="n3">Tenures from three separate Blomefield parish entries: Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. i (London: William Miller, 1805), "Hundred of Shropham: Great Elingham," pp. 482–490 — "he was lord in 1572, and at his death it went to Edm. Gurney, Esq. his son and heir ... Henry Gurney, Esq. his son and heir, who held Irsted manor of the Bishop Norwich, Elingham manor of the Lord Bardolf's heirs, West Barsham of the manor of Castle-Acre, by one fee, Gurney's manor in Hingham, of the heirs of Henry Lord Morley, as of his manor of Hingham, and the advowson of the third part of Attleburgh." Blomefield, vol. ii (1805), "Hundred of Forehoe: Hingham," pp. 422–445 — "Henry Gurney was lord in 1572." Blomefield, vol. vii (1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42–47. All three available via British History Online. The "last member ... born a Roman Catholic" tradition is in Daniel Gurney, <em>Supplement</em> (1858), p. 875. <a class="citation-back" href="#ref-3">↩</a></li>
new_string:
  <li id="n3">Tenures from three separate Blomefield parish entries: Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. i (London: William Miller, 1805), "Hundred of Shropham: Great Elingham," pp. 482–490 — "he was lord in 1572, and at his death it went to Edm. Gurney, Esq. his son and heir ... Henry Gurney, Esq. his son and heir, who held Irsted manor of the Bishop Norwich, Elingham manor of the Lord Bardolf's heirs, West Barsham of the manor of Castle-Acre, by one fee, Gurney's manor in Hingham, of the heirs of Henry Lord Morley, as of his manor of Hingham, and the advowson of the third part of Attleburgh." Blomefield, vol. ii (1805), "Hundred of Forehoe: Hingham," pp. 422–445 — "Henry Gurney was lord in 1572." Blomefield, vol. vii (1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42–47. All three available via British History Online. Mostyn John Armstrong, <em>The History and Antiquities of the County of Norfolk</em>, vol. 4 (Norwich, 1781), Forehoe Hundred entry for Hingham, independently records Gurney's Manor at Hingham as "part of the great manor, granted to a younger branch of the family before the forfeiture; it continued always in the family of that name, residing at Barsham and Great Ellingham, in this county; Henry Gurney was lord in 1572; how it passed afterwards we do not find; but in 1715 it was owned by Mr. Larwood, of Norwich, merchant" — supplying the post-extinction Hingham successor not in Blomefield. Source ID: <code>armstrong-norfolk-1781</code>. The "last member ... born a Roman Catholic" tradition is in Daniel Gurney, <em>Supplement</em> (1858), p. 875. <a class="citation-back" href="#ref-3">↩</a></li>
```

### 5. G17 — Occupation/Status vital absorbs Irstead 1541-42 + Merton 1540 transactions

File: `fact-sheets/g17-anthony-gurney-fact-sheet.md`.

```str_replace
old_string:
    <div class="fact-value">Lord of West Barsham (held by one knight's fee of the manor of Castleacre, "lord in 1514" per Blomefield), Great Ellingham, Harpley, Hingham-Gurneys, Hardingham, Wattlefield, and (after 1525) the Lovell Mortimer-of-Attleborough estates that came in through his wife. Leading Norfolk gentleman. Foreman of the Norfolk grand jury that indicted Henry Howard, Earl of Surrey, on 7 January 1546/7 (the indictment that led to Surrey's execution two weeks later). <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
new_string:
    <div class="fact-value">Lord of West Barsham (held by one knight's fee of the manor of Castleacre, "lord in 1514" per Blomefield), Great Ellingham, Harpley, Hingham-Gurneys, Hardingham, Wattlefield, North Barsham, Irstead (purchased by fine from Sir Richard Southwell in 1541-42 with lands in Barton, Neatishead, and Smalburgh), and (after 1525) the Lovell Mortimer-of-Attleborough estates that came in through his wife. He also rationalised the estate in 1540 by selling Merton manor (with the Trinity church advowson and lands in Riling, Cranworth, Hingham, Carbrooke, and Little Ellingham) to the same Sir Richard Southwell. Leading Norfolk gentleman. Foreman of the Norfolk grand jury that indicted Henry Howard, Earl of Surrey, on 7 January 1546/7 (the indictment that led to Surrey's execution two weeks later). <sup class="fn"><a href="#n3" id="ref-3">3</a></sup><sup class="fn"><a href="#n14" id="ref-14">14</a></sup></div>
```

### 6. G17 — Died vital absorbs the "lord of Irstead" attestation

File: `fact-sheets/g17-anthony-gurney-fact-sheet.md`.

```str_replace
old_string:
    <div class="fact-value"><strong>4 January 1555 Old Style (= January 1556 modern reckoning)</strong>. The precise day is recorded by Francis Blomefield in his parish entry for West Barsham: "Anthony Gournay, Esq. ... died January 4, 1555, leaving Henry, his grandson and heir, aged twenty-one years." <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
new_string:
    <div class="fact-value"><strong>4 January 1555 Old Style (= January 1556 modern reckoning)</strong>. The precise day is recorded by Francis Blomefield in his parish entry for West Barsham: "Anthony Gournay, Esq. ... died January 4, 1555, leaving Henry, his grandson and heir, aged twenty-one years." The same date is independently attested by Mostyn John Armstrong in the Tunstead Hundred entry for Irstead, which records that Anthony "died lord [of Irstead] on January 4, in the 2d and 3d of Philip and Mary" (= 4 Jan 1555/6). <sup class="fn"><a href="#n2" id="ref-2">2</a></sup><sup class="fn"><a href="#n14" id="ref-14b">14</a></sup></div>
```

### 7. G17 — narrative paragraph 128 absorbs the Irstead + Merton transactions

File: `fact-sheets/g17-anthony-gurney-fact-sheet.md`.

```str_replace
old_string:
Anthony's known landholdings as Norfolk gentleman in the 1520s–1550s therefore included: West Barsham (the principal seat, held by one knight's fee of Castleacre per Blomefield); Great Ellingham (after 1525); Hingham-Gurneys (held of the heirs of Henry Lord Morley); Harpley; Hardingham; Wattlefield; and "Gurney's Place" — a town house in St Julian's parish, Norwich. He also appears in the published household and privy purse accounts of the Lestranges of Hunstanton (1519–1578) as a regular Norfolk visitor and dinner companion of the Lestrange family.
new_string:
Anthony's known landholdings as Norfolk gentleman in the 1520s–1550s therefore included: West Barsham (the principal seat, held by one knight's fee of Castleacre per Blomefield); Great Ellingham (after 1525); Hingham-Gurneys (held of the heirs of Henry Lord Morley); Harpley; Hardingham; Wattlefield; North Barsham (where Mostyn John Armstrong's Great Ellingham parish entry names him as "Anthony Gurney, esq. of North Barsham" at the moment of the 1525 inheritance); and "Gurney's Place" — a town house in St Julian's parish, Norwich. He also appears in the published household and privy purse accounts of the Lestranges of Hunstanton (1519–1578) as a regular Norfolk visitor and dinner companion of the Lestrange family.

A pair of 1540–1542 transactions with Sir Richard Southwell rationalised the estate. In 1540 Anthony sold Merton manor (Watton area), together with the advowson of Trinity church and lands in Riling, Cranworth, Hingham, Carbrooke, and Little Ellingham, to Southwell. In 33 Henry VIII (1541-42) the same Southwell sold to Anthony the manor of Irstead (Tunstead Hundred), with lands in Barton, Neatishead, and Smalburgh — the same Irstead manor that Anthony's grandson Henry G15 would later hold of the bishop of Norwich. The two transactions read as a deliberate counter-direction exchange between two of mid-Tudor Norfolk's larger landholders, exchanging a south-Norfolk Watton-area holding for a north-east-Norfolk Broads holding. Anthony died holding Irstead in 1555/6.
```

### 8. G17 — add timeline rows for the 1540 Merton sale and 1541-42 Irstead purchase

File: `fact-sheets/g17-anthony-gurney-fact-sheet.md`.

```str_replace
old_string:
      <tr><td>1525</td><td>Henry Spelman the elder of "Mickle Elyngham" dies without issue; Great Ellingham descends to Anthony in right of his wife Margaret (Blomefield, vol. i).</td></tr>
      <tr><td>1519–1555</td><td>Appears regularly in the Lestrange of Hunstanton household and privy purse accounts.</td></tr>
      <tr><td>c. 1536</td><td>Wife Margaret Lovell dies (per Pease).</td></tr>
new_string:
      <tr><td>1525</td><td>Henry Spelman the elder of "Mickle Elyngham" dies without issue; Great Ellingham descends to Anthony in right of his wife Margaret (Blomefield, vol. i; Armstrong, vol. 8).</td></tr>
      <tr><td>1519–1555</td><td>Appears regularly in the Lestrange of Hunstanton household and privy purse accounts.</td></tr>
      <tr><td>c. 1536</td><td>Wife Margaret Lovell dies (per Pease).</td></tr>
      <tr><td>1540</td><td>Sells Merton manor (Watton area; Trinity church advowson; lands in Riling, Cranworth, Hingham, Carbrooke, Little Ellingham) to Sir Richard Southwell (Armstrong, vol. 9).</td></tr>
      <tr><td>1541–42 (33 Hen. VIII)</td><td>Buys the manor of Irstead by fine from Sir Richard Southwell, with lands in Barton, Neatishead, Smalburgh (Armstrong, vol. 9).</td></tr>
```

### 9. G17 — append new footnote n14 covering the Armstrong-witness chain (Irstead, Merton, North Barsham, death-date corroboration)

File: `fact-sheets/g17-anthony-gurney-fact-sheet.md`.

```str_replace
old_string:
  <li id="n13">Pease/Pennyghael Gurney genealogy (Charles E. G. Pease, 2016), naming three children: Francis, Ela, and one further child not named in the source consulted. <a class="citation-back" href="#ref-13">↩</a></li>
</ol>
new_string:
  <li id="n13">Pease/Pennyghael Gurney genealogy (Charles E. G. Pease, 2016), naming three children: Francis, Ela, and one further child not named in the source consulted. <a class="citation-back" href="#ref-13">↩</a></li>
  <li id="n14">Mostyn John Armstrong, <em>The History and Antiquities of the County of Norfolk</em>, vol. 9 (Norwich, 1781), Tunstead Hundred entry for Irstead: "In the 33rd of Henry VIII, Sir Richard Southwell, knt. conveyed by fine to Anthony Gourney, esq. the manor of Irstead, with lands in Barton, Neatishead, Smalburgh, &c. and the said Anthony died lord on January 4, in the 2d and 3d of Philip and Mary, whose grandson, Henry, is said, by Mr. Parkin, to hold his manor of the bishop of Norwich." The same Sir Richard Southwell appears on the opposite side of the c. 1540 Merton sale: Armstrong, vol. 9, South Greenhoe Hundred entry for Merton — "from that time [1402, Mortimer estate division] it went with Ellingham-hall manor till 1540, and then was sold by Anthony Gurnay, esq. to Sir Richard Southwell, with the advowson of Trinity church here, and Sir Edward Chamberlain released his right in it. It extended then into Riling, Cranworth, Hingham, Carbrooke, and little Ellingham." Armstrong's Great Ellingham parish entry (vol. 8, Shropham Hundred) names Anthony as "Anthony Gurney, esq. of North Barsham, in right of Margaret his wife, one of the daughters and coheiresses of Sir Robert Lovell, by Ela Conyers his wife, who was sister to Ann Conyers, mother to Henry Spelman" — the "of North Barsham" naming preserved here because, by 1525, the North Barsham seat had become a working alternative residence to West Barsham. Internet Archive items <code>bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_8</code> and <code>..._1781_9</code>. Source ID: <code>armstrong-norfolk-1781</code>. <a class="citation-back" href="#ref-14">↩</a></li>
</ol>
```

### 10. G18 — Heydon-sister marriage network corroboration (light touch)

The G18 narrative already records Anne Heydon's family network (the Boleyn, Paston, Cobham, Lestrange kinships are present); Armstrong supplies one explicit four-sister list in one paragraph. Add as a sentence-level reinforcement under the Marriage vital, citing the existing Heydon-marriage footnote n5.

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`.

Locate the Marriage vital block — search for the substring `Anne Heydon` followed by the spouse paragraph that mentions "After William V's death, Anne remarried Sir Lionel Dymoke." Append a closing sentence immediately before the footnote reference, naming the four Heydon sisters and their husbands.

Operation:

```str_replace
old_string:
        <div><strong>Anne Heydon</strong> — daughter of <strong>Sir Henry Heydon</strong> of Baconsthorpe Castle (Privy Councillor to Henry VII, builder of Baconsthorpe) and his wife <strong>Anne Boleyn the elder</strong> of Blickling (sister of Sir William Boleyn, grandfather of Queen Anne Boleyn). Anne Heydon married William V "shortly after 28 May 1484" per modern Heydon scholarship reading Sir Henry's will of 1503/4. After William V's death, Anne remarried Sir Lionel Dymoke of Ashby, Lincolnshire, and died c. 1521. The marriage brought into the Gurney line direct kinship to Anne Boleyn the elder, the Pastons, the Cobhams, the Lestranges of Hunstanton, and the wider Heydon-Boleyn-Howard cousinage of late 15th and early 16th century Norfolk. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
new_string:
        <div><strong>Anne Heydon</strong> — daughter of <strong>Sir Henry Heydon</strong> of Baconsthorpe Castle (Privy Councillor to Henry VII, builder of Baconsthorpe) and his wife <strong>Anne Boleyn the elder</strong> of Blickling (sister of Sir William Boleyn, grandfather of Queen Anne Boleyn). Anne Heydon married William V "shortly after 28 May 1484" per modern Heydon scholarship reading Sir Henry's will of 1503/4. After William V's death, Anne remarried Sir Lionel Dymoke of Ashby, Lincolnshire, and died c. 1521. The marriage brought into the Gurney line direct kinship to Anne Boleyn the elder, the Pastons, the Cobhams, the Lestranges of Hunstanton, and the wider Heydon-Boleyn-Howard cousinage of late 15th and early 16th century Norfolk. Mostyn John Armstrong, in his 1781 Norfolk volumes, lists Anne Heydon's four sisters and their husbands in a single paragraph: Amy (Sir Roger Townshend of Hunstanton), Dorothy (Sir Thomas Brook, heir of Lord Cobham), Elizabeth (Walter Hobart of Hales-hall), and Bridget (Sir William Paston) — placing William V's marriage inside one of the densest North Norfolk gentry-alliance networks of the late 15th century. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```

### 11. G18 — append the Armstrong sibling-list witness to existing footnote n5

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`.

```str_replace
old_string: Sir Lionel Dymoke (d. 17 August 1519) was of Ashby, Lincolnshire, hereditary King's Champion. Anne died c. 1521. <a class="citation-back" href="#ref-5">↩</a></li>
new_string: Sir Lionel Dymoke (d. 17 August 1519) was of Ashby, Lincolnshire, hereditary King's Champion. Anne died c. 1521. The four-Heydon-sister marriage-list given by Mostyn John Armstrong, <em>The History and Antiquities of the County of Norfolk</em>, vol. 3 (Norwich, 1781), North Erpingham Hundred, names Anne's marriage to William Gurney V inside the cluster Amy / Sir Roger Townshend of Hunstanton; Dorothy / Sir Thomas Brook of Cobham; Elizabeth / Walter Hobart of Hales-hall; Bridget / Sir William Paston. Source ID: <code>armstrong-norfolk-1781</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

## Validation checklist

- [ ] `fact-sheets/g15-henry-gurney-fact-sheet.md` — child-table row 1 cites Edward d. Aug 1641 with footnotes 12 + 19; narrative paragraph names Edward as 1637 JP and references the West Barsham–Great Ellingham post-1641 split; new footnote n19 covers Armstrong vols. 5 + 8 + 9; footnote n3 carries the Armstrong 1715 Larwood successor at Hingham.
- [ ] `fact-sheets/g17-anthony-gurney-fact-sheet.md` — Occupation/Status vital lists Irstead and North Barsham and references the 1540 Merton sale; Died vital cites Armstrong as a second witness to 4 Jan 1555/6; narrative paragraph 128 absorbs the 1540 + 1541-42 Southwell counter-direction pair; timeline gains 1540 and 1541-42 rows; new footnote n14 anchors the Armstrong witness chain.
- [ ] `fact-sheets/g18-william-gurney-v-fact-sheet.md` — Marriage vital absorbs the Armstrong four-Heydon-sister sentence; existing n5 footnote carries the Armstrong vol. 3 citation as a corroborating witness.
- [ ] No `data/sources.json` change in this patchset (v69 already adds `armstrong-norfolk-1781`).
- [ ] No `research/`, `sources/`, or place-file changes in this patchset (v71 covers those).

## Phase 2 completion step

After application:

```bash
python - <<'PY'
from pathlib import Path
src = Path("sources/intake/processed/v70-armstrong-1781-fact-sheet-absorption.patchset.md")
dst = Path("sources/intake/done/v70-armstrong-1781-fact-sheet-absorption.patchset.md")
body = src.read_text(encoding="utf-8")
dst.write_text("**Done:** 2026-05-28 HH:MM PT\n\n" + body, encoding="utf-8")
src.unlink()
PY
```

Replace `HH:MM` with the actual completion time.
