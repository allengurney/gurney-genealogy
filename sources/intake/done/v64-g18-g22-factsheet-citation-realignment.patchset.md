**Done:** 2026-05-27 21:30 PT

# v64 G18-G22 fact-sheet citation realignment patchset

Phase 1 patchset prepared 2026-05-27 on `main`.

## Scope

This patchset tightens source alignment in the G18-G22 fact sheets after the earlier citation-cleanup pass. It addresses claims flagged in `sources/intake/processed/g18-g22-factsheet-citation-cleanup-log.md`, with emphasis on:

- replacing unsupported causal or social-history phrasing with source-bounded claims
- expanding footnotes where an existing source directly supports the broader statement
- preserving useful narrative color when it can be tied to Daniel Gurney, Blomefield, Gairdner/Paston, History of Parliament, the AHRC medieval soldier database, Rye, or existing corpus supplements
- avoiding new `data/sources.json` entries because all cited sources below already have source IDs

Revision loop after user review: this version restores source-backed narrative where the first draft was too flattening, but keeps the standard that the footnote must support the factual claim. Two specific corrections are important for Phase 2: the G18 Anthony-minority/wardship language should prove the minority and executor-management problem without naming unsupported Heydon guardians, and the 1445 Hunstanton seal belongs to G20 Thomas II rather than G21 Thomas I.

## Source-tracking

No new source IDs are proposed. Existing source IDs used or strengthened:

- `dg-rec-pt2` / `dg-rec-pt3` / `dg-rec-supp`
- `blomefield-norfolk`
- `paston-letters-gairdner`
- `medievalsoldier-database`
- `rye-norfolk-antiquarian`
- `hop-drury-robert-i-1456-1535`
- `history-of-parliament-online-gurney-1386-1421` or the existing HoP source ID used in G22 footnote text

Existing preserved extracts checked:

- `sources/corpus/daniel-gurney-part-2.md`
- `sources/corpus/daniel-gurney-part-3.md`
- `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md`
- `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`
- `sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md`
- `sources/corpus_supplement/hop-drury-robert-i-1456-1535.md`
- `sources/corpus/norfolk-antiquarian-gurneys-of-norwich.md`

## Item 01 - G18: remove unsupported Lestrange causal claim from Highlight

Outcome: promote.

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li><strong>Anne's siblings married into the highest Norfolk gentry.</strong> Through Anne Heydon, William V's children gained a remarkable network of in-laws: Anne's sister Bridget Heydon married Sir William Paston of Caister (the Paston Letters family); her sister Dorothy married a Lord Cobham (a granddaughter of Dorothy and Lord Cobham, Elizabeth Brooke, would become the second wife of Sir Thomas Wyatt the poet); and her sister Amy married Sir Roger Lestrange of Hunstanton. The Lestrange marriage is the kinship that explains why two generations later William V's great-great-grandson Francis Gurney (G14) became the financial agent to the Lestranges of Hunstanton from 1612 to 1636 — they were distant cousins. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>

new_string:
  <li><strong>Anne's siblings married into the highest Norfolk gentry.</strong> Through Anne Heydon, William V's children gained a remarkable network of in-laws: Anne's sister Bridget Heydon married Sir William Paston of Caister (the Paston Letters family); her sister Dorothy married a Lord Cobham (a granddaughter of Dorothy and Lord Cobham, Elizabeth Brooke, would become the second wife of Sir Thomas Wyatt the poet); and her sister Amy married Sir Roger Lestrange of Hunstanton. The Lestrange marriage is a documented kinship link to Hunstanton; the later Francis Gurney (G14) agency for the Lestranges belongs to the Francis story, but the marriage itself is enough to show how wide Anne's sibling network reached. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

## Item 02 - G18: replace unsupported Calthorpe chain with documented trust-circle claim

Outcome: promote.

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
He was born around 1465 — Daniel Gurney's pedigree gives no birth year, and the Ancestry composite trees give c. 1468. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup> His father was William Gurney IV (G19), the Norfolk escheator and council member to the Duke of Norfolk; his mother was Anne Calthorpe, only daughter of Sir William Calthorpe of Burnham Thorpe, KB, by his first wife Elizabeth Grey of Ruthyn (whose own death in 1437 is independently documented in the Calthorpe family literature). <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup><sup class="fn"><a href="#n13" id="ref-13">13</a></sup> Through his Calthorpe mother, William V was a kinsman of one of the leading Norfolk gentry families of the late 15th century, with connections to the Drurys of Hawstead, the Hasildens, the Stapletons of Ingham, and ultimately to the de la Poles, Earls of Suffolk.

new_string:
He was born around 1465 — Daniel Gurney's pedigree gives no birth year, and the Ancestry composite trees give c. 1468. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup> His father was William Gurney IV (G19), the Norfolk escheator and council member to the Duke of Norfolk; his mother was Anne Calthorpe, only daughter of Sir William Calthorpe of Burnham Thorpe, KB, by his first wife Elizabeth Grey of Ruthyn (whose own death in 1437 is independently documented in the Calthorpe family literature). <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup><sup class="fn"><a href="#n13" id="ref-13">13</a></sup> Through his Calthorpe mother, William V belonged to a documented Calthorpe-Howard-Drury circle: his father's 1505 trust named Sir Edward Howard, Sir Philip Calthorpe, Sir Robert Clere, Sir Robert Drury, Nicholas Appleyard, William Calthorpe of Pockthorpe, and Thomas Gurnay as feoffees. <sup class="fn"><a href="#n13" id="ref-13b">13</a></sup>
```

## Item 03 - G18: soften Lestrange narrative paragraph to match sources

Outcome: promote.

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
Anne Heydon's siblings married into a remarkably wide network: her sister Bridget Heydon married Sir William Paston of Caister (the Paston Letters family); her sister Dorothy married a Lord Cobham (a granddaughter of whom, Elizabeth Brooke, would become the second wife of Sir Thomas Wyatt the poet); and her sister Amy Heydon married Sir Roger Lestrange of Hunstanton. <sup class="fn"><a href="#n8" id="ref-8c">8</a></sup> The Lestrange marriage is the kinship that explains why two generations later William V's great-great-grandson Francis Gurney (G14) would become the trusted financial agent to the Lestranges of Hunstanton from 1612 to 1636: they were distant cousins, and Norfolk gentry preferred to do their financial business with kin.

new_string:
Anne Heydon's siblings married into a remarkably wide network: her sister Bridget Heydon married Sir William Paston of Caister (the Paston Letters family); her sister Dorothy married a Lord Cobham (a granddaughter of whom, Elizabeth Brooke, would become the second wife of Sir Thomas Wyatt the poet); and her sister Amy Heydon married Sir Roger Lestrange of Hunstanton. <sup class="fn"><a href="#n8" id="ref-8c">8</a></sup> That Lestrange marriage gives a documented kinship route between the Gurney line and Hunstanton. Two generations later, Francis Gurney (G14) appears in the source layer as a merchant or agent handling Lestrange business; the sources support the kinship and the later agency, but not a simple causal claim that one directly explains the other. <sup class="fn"><a href="#n8" id="ref-8e">8</a></sup>
```

## Item 04 - G18: expand Lestrange footnote so the agency caveat is traceable

Outcome: promote.

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n8">Anne Heydon's siblings: WikiTree profile for Sir Henry Heydon, listing daughters Bridget (m. Sir William Paston of Caister); Dorothy (m. Lord Cobham); Amy (m. Sir Roger Lestrange of Hunstanton). The Cobham connection: see also the WikiTree profile of Elizabeth Brooke, second wife of Sir Thomas Wyatt the poet, identifying her grandmother as Dorothy Heydon. The Lestrange of Hunstanton marriage is independently documented in Daniel Gurney, "Extracts from the Household and Privy Purse Accounts of the Lestranges of Hunstanton, from A.D. 1519 to A.D. 1578," <em>Archaeologia</em> vol. 25 (1832), pp. 411–569. <a class="citation-back" href="#ref-8">↩</a></li>

new_string:
  <li id="n8">Anne Heydon's siblings: WikiTree profile for Sir Henry Heydon, listing daughters Bridget (m. Sir William Paston of Caister); Dorothy (m. Lord Cobham); Amy (m. Sir Roger Lestrange of Hunstanton). The Cobham connection: see also the WikiTree profile of Elizabeth Brooke, second wife of Sir Thomas Wyatt the poet, identifying her grandmother as Dorothy Heydon. The Lestrange of Hunstanton marriage is independently documented in Daniel Gurney, "Extracts from the Household and Privy Purse Accounts of the Lestranges of Hunstanton, from A.D. 1519 to A.D. 1578," <em>Archaeologia</em> vol. 25 (1832), pp. 411–569. Francis Gurney's later Lestrange agency is treated separately in Walter Rye, "The Gurneys of Norwich," <em>The Norfolk Antiquarian Miscellany</em>, which says Francis acted as banker or agent for the L'Estrange family in 1614 and appears at Hunstanton in 1615; the fact sheet should not imply that the Amy Heydon-Lestrange marriage by itself proves why that business relationship existed. Source IDs: <code>rye-norfolk-antiquarian</code>, <code>dg-rec-pt2</code>. <a class="citation-back" href="#ref-8">↩</a></li>
```

## Item 05 - G18: expand Calthorpe/Drury trust footnote

Outcome: promote.

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n13">Daniel Gurney, <em>Record</em> (1848), pp. 282, 287. Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew &amp; Son, 1858), pp. 816-820. <a class="citation-back" href="#ref-13">↩</a></li>

new_string:
  <li id="n13">Daniel Gurney, <em>Record</em> (1848), pp. 282, 287. Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew &amp; Son, 1858), Note 132, pp. 817-819, prints the 1505 trust deed naming Sir Edward Howard, Sir Philip Calthorpe, Sir Robert Clere, Sir Robert Drury, Nicholas Appleyard, William Calthorpe of Pockthorpe, and Thomas Gurnay as feoffees. Sir Robert Drury's marriage to Anne Calthorpe by Sir William Calthorpe's second wife Elizabeth Stapleton is independently supported by L. M. Kirk, "DRURY, Sir Robert I (by 1456-1535)," <em>History of Parliament: The House of Commons 1509-1558</em>, available at History of Parliament Online. Source IDs: <code>dg-rec-supp</code>, <code>hop-drury-robert-i-1456-1535</code>. <a class="citation-back" href="#ref-13">↩</a></li>
```

## Item 06 - G19: attribute wool/worsted context directly to Daniel Gurney

Outcome: promote.

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
By his 1507 will William directed that 700 sheep should remain at West Barsham after his death. Genealogist Daniel Gurney described this as "a considerable flock in those days," and it is — perhaps the single most concrete piece of evidence about the working economy of any pre-1600 Gurney household. <sup class="fn"><a href="#n8" id="ref-8c">8</a></sup> The flock fed the East Anglian wool trade, which in turn fed the Norwich worsted industry, which was the dominant economic activity of the county. The Gurneys at this period were not magnates, but they were a thoroughly substantial gentry sheep-farming household, sufficiently established to support a town residence at Pockthorpe-by-Norwich and a country seat at West Barsham simultaneously. <sup class="fn"><a href="#n8" id="ref-8d">8</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup>

new_string:
By his 1507 will William directed that 700 sheep should remain at West Barsham after his death. Genealogist Daniel Gurney described this as "a considerable flock in those days," and tied it to a wider Norfolk pattern: light, open sheep-walk country; gentlemen preparing or combing wool for market; and household women spinning yarn and sometimes weaving the prepared wool at home. <sup class="fn"><a href="#n8" id="ref-8c">8</a></sup> The claim is therefore not just that William owned many sheep, but that the flock places West Barsham inside the working economy that fed the Norwich woollen and worsted trades. The Gurneys at this period were not magnates, but they were a substantial gentry sheep-farming household, sufficiently established to support a town residence at Pockthorpe-by-Norwich and a country seat at West Barsham simultaneously. <sup class="fn"><a href="#n8" id="ref-8d">8</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup>
```

## Item 07 - G19: expand sheep/wool footnote

Outcome: promote.

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n8">Daniel Gurney, <em>Record</em> (1848), p. 282: "William Gurney, in 1507, desires by will that 700 sheep should remain at West Barsham after his death; a considerable flock in those days." Cross-reference Daniel Gurney, <em>Supplement</em> (1858), p. 817 ff. <a class="citation-back" href="#ref-8">↩</a></li>

new_string:
  <li id="n8">Daniel Gurney, <em>Record</em> (1848), p. 282: "William Gurney, in 1507, desires by will that 700 sheep should remain at West Barsham after his death; a considerable flock in those days." The same passage supplies the broader economic context: Norfolk's light, uninclosed sheep-walk country favored woollen manufactures; Norfolk gentlemen prepared or combed wool for market; and some prepared wool was woven by "the ladies and females at home," while yarn was spun by them. Daniel Gurney, <em>Record</em>, Part III (1848), pp. 512-514, separately summarizes Norwich's woollen and worsted manufacture from Henry II through the Flemish and Walloon textile revivals. Cross-reference Daniel Gurney, <em>Supplement</em> (1858), p. 817 ff. Source IDs: <code>dg-rec-pt2</code>, <code>dg-rec-pt3</code>, <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-8">↩</a></li>
```

## Item 08 - G20: make the 1452 political paragraph source-bounded

Outcome: promote.

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
A single dated letter places Thomas at the centre of Norfolk gentry politics in his early adulthood. On St George's Day 1452, Thomas signed a petition from Norwich to the Duke of Norfolk's deputy at Framlingham, complaining of "dyvers assaughtes and ryottes made be Charles Nowell and other ageyn the Kyngs lawe and peas… up on John Paston and other of owre kynne, frendes and neyghborys." The co-signers included Sir John Heveningham, John Ferrers, John Groos, William Rokewode, the two John Bakons, John Pagrave, Robert Mortimer, and Nicholas Appleyard — the Paston-side Norfolk gentry coalition standing against the Charles-Nowell faction operating under John Heydon and Sir Thomas Tuddenham as the Duke of Suffolk's East Anglian agents. Thomas was about 22, married into the Jerninghams, and visibly aligned against the Heydons. Yet nineteen years later — after the 1461 Yorkist accession had upended the East Anglian power map and John Heydon had bought his 1462 Yorkist pardon for 500 marks — Thomas's 1471 will would name John Heydon himself as supervisor. The realignment is one of the cleanest gentry-politics arcs in the surviving record. <sup class="fn"><a href="#n14" id="ref-14">14</a></sup>

new_string:
A single dated letter places Thomas inside Norfolk gentry politics in his early adulthood. On St George's Day 1452, Thomas signed a petition from Norwich to the Duke of Norfolk's deputy at Framlingham, complaining of "dyvers assaughtes and ryottes made be Charles Nowell and other ageyn the Kyngs lawe and peas… up on John Paston and other of owre kynne, frendes and neyghborys." The co-signers included Sir John Heveningham, John Ferrers, John Groos, William Rokewode, the two John Bakons, John Pagrave, Robert Mortimer, and Nicholas Appleyard. The letter shows Thomas with the Paston-friendly signers at that moment; the later contrast is that his 1471 will named John Heydon of Baconsthorpe as supervisor. That is enough to show a changed working relationship without making the fact sheet carry more factional analysis than the cited extract can support. <sup class="fn"><a href="#n14" id="ref-14">14</a></sup>
```

## Item 09 - G20: expand Paston footnote to explain what is sourced and what is interpretation

Outcome: promote.

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n14">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), vol. II, letter dated St George's Day (23 April) 1452, written from Norwich to the Duke of Norfolk's deputy at Framlingham. Project Gutenberg vol. II: <a href="https://www.gutenberg.org/cache/epub/40989/pg40989.txt">www.gutenberg.org/cache/epub/40989/pg40989.txt</a>. <a class="citation-back" href="#ref-14">↩</a></li>

new_string:
  <li id="n14">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), vol. II, letter dated St George's Day (23 April) 1452, written from Norwich to the Duke of Norfolk's deputy at Framlingham. The preserved extract at <code>sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md</code> names Thomas Gurnay among the signers and gives the complaint against Charles Nowell and others for assaults and riots against John Paston and his kin, friends, and neighbours. The later 1471 Heydon-supervisor contrast is from Blomefield's West Barsham will extract, cited in note 13; broader claims about factional realignment should remain cautious unless supported by a dedicated secondary source. Project Gutenberg vol. II: <a href="https://www.gutenberg.org/cache/epub/40989/pg40989.txt">www.gutenberg.org/cache/epub/40989/pg40989.txt</a>. Source IDs: <code>paston-letters-gairdner</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-14">↩</a></li>
```

## Item 10 - G20: tighten Margaret textile paragraph and footnote

Outcome: promote.

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
The will's most personal bequest is to Margaret. Thomas left all the household's "woolen and linen cloths" to his wife, Daniel Gurney noting specifically that these were "being her own work and that of her servants." <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup> Margaret, in other words, ran a productive textile operation within the household: spinning and weaving wool from her husband's flocks for the family's own use and, implicitly, for exchange. This was standard practice for substantial Norfolk gentry wives of the period — Norfolk's light soils made sheep-farming profitable, the women of the household did much of the yarn preparation, and the prepared wool and finished cloth fed into the Norwich worsted industry that dominated the county's economy. Thomas's will is one of the few surviving documents to make the gendered division of the household economy explicit. <sup class="fn"><a href="#n9" id="ref-9c">9</a></sup>

new_string:
The will's most personal bequest is to Margaret. Thomas left all the household's "woolen and linen cloths" to his wife, Daniel Gurney noting specifically that these were "being her own work and that of her servants." <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup> Daniel Gurney uses this bequest alongside William IV's later 700-sheep will clause to describe a Norfolk wool economy in which gentlemen prepared wool for market and household women spun yarn or sometimes wove prepared wool at home. The stronger published claim is therefore not that Margaret's work can be quantified as a commercial business, but that the will gives rare household-level evidence for the textile labor behind a substantial Norfolk gentry estate. <sup class="fn"><a href="#n9" id="ref-9c">9</a></sup>
```

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n9">Daniel Gurney, <em>Record</em> (1848), p. 282: "all the woolen and linen cloths are left to Margaret his wife, being her own work and that of her servants." <a class="citation-back" href="#ref-9">↩</a></li>

new_string:
  <li id="n9">Daniel Gurney, <em>Record</em> (1848), p. 282: "all the woolen and linen cloths are left to Margaret his wife, being her own work and that of her servants." The same page supplies the linked interpretation: Norfolk's sheep-walk landscape favored woollen manufacture; Norfolk gentlemen prepared or combed wool for market; and some prepared wool was woven by "the ladies and females at home," while yarn was spun by them. This supports household textile labor and wool-economy context, but not a quantified claim that Margaret sold cloth commercially. Source ID: <code>dg-rec-pt2</code>. <a class="citation-back" href="#ref-9">↩</a></li>
```

## Item 11 - G21: retire speculative privacy / "kept heads down" framing

Outcome: promote.

File: `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
His own life after the inheritance is thinly documented. He married Catherine Kerville of Watlington, in the west-Norfolk hinterland of King's Lynn — a sensible alliance for a gentleman whose principal seats at West Barsham and Harpley lay in the intermediate north-Norfolk zone and who now also held commercial property in London via La Selde Coronata. <sup class="fn"><a href="#n8" id="ref-8b">8</a></sup><sup class="fn"><a href="#n7" id="ref-7c">7</a></sup> He appears in no royal commission, no sheriffdom, no parliamentary service, and no commission of the peace. <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup> He does appear, however, in three smaller documentary attestations: as a Norfolk feoffee in East Barsham in 1434-35 (with John Hunt, confirming Wolterton's Manor to John Wode); in active military service in France across three campaigns (the 1415 Agincourt campaign in John Holland's retinue, the 1418 Harfleur garrison under Thomas Beaufort Duke of Exeter, and the 1441 France expedition in John de Vere's retinue under Richard of York); and as the sealer of a 1445 East Barsham feoffment preserved on a Le Strange charter at Hunstanton Hall. The cumulative picture is of a quietly active Norfolk gentleman, not an entirely retiring one. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup> This is a striking silence given his uncle's extensive record, and it suggests either that Thomas I was deliberately private (perhaps preferring to consolidate the collateral inheritance rather than take on Crown office) or that the documentary record is simply thinner for his generation than for Sir John's. The period he lived through — the reign of Henry V, the long minority of Henry VI, and the drift into the pre-war tensions of the 1440s — was one in which Norfolk gentry mostly kept their heads down while the great magnates fought.

new_string:
His own life after the inheritance is thinly documented, but it is no longer blank. He married Catherine Kerville of Watlington, in the west-Norfolk hinterland of King's Lynn — a useful westward alliance for a family whose principal seats were West Barsham and Harpley and whose inherited portfolio also touched London through La Selde Coronata. <sup class="fn"><a href="#n8" id="ref-8b">8</a></sup><sup class="fn"><a href="#n7" id="ref-7c">7</a></sup> No royal commission, sheriffdom, parliamentary service, or commission of the peace has yet been identified for him. <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup> What has been found is a narrower but real record: service as a man-at-arms in France in 1415, 1418, and 1441, followed by a 1434-35 East Barsham feoffee appearance with John Hunt. The 1445 Hunstanton Hall seal belongs in the G20 Thomas II fact sheet, not here, because the G20 companion already treats it as evidence that Thomas II was acting as head of the family by 1444-45. The cumulative picture for Thomas I is therefore still of a quietly active Norfolk gentleman, but the evidence should stop at the 1441/1434-35 cluster unless a direct record ties the 1445 deed back to him. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup>
```

## Item 12 - G22: replace younger-son generalization with documented negative / cautious inference

Outcome: promote.

File: `fact-sheets/g22-robert-gournay-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
The situation of a younger son in a late 14th-century Norfolk gentry family was often comfortable but obscure. The eldest son — here, Sir John V — inherited the title, the manor, the legal and political career, and the documentary footprint. The younger son received a provision (a cash settlement, perhaps a small landholding), made a respectable marriage, and lived out a quiet life in the county. Robert's marriage to Joan de Norwich suggests at least a connection to the Norwich civic world — the family his father Edmund had served as standing counsel — but it could equally reflect simply a woman whose family happened to be based in or near Norwich, which was by far the largest urban centre in the region. <sup class="fn"><a href="#n4" id="ref-4c">4</a></sup><sup class="fn"><a href="#n6" id="ref-6e">6</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>

new_string:
Robert's obscurity fits what the surviving evidence actually shows: his elder brother Sir John V carried the offices, manors, parliamentary service, and long administrative trail, while Robert has not yet been found in a deed, will, court appearance, or land transaction under his own name. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup><sup class="fn"><a href="#n6" id="ref-6e">6</a></sup> His marriage to Joan de Norwich may point toward the Norwich civic world that his father Edmund had served as standing counsel, but the sources only give her name; they do not identify her parents, family, or property. <sup class="fn"><a href="#n4" id="ref-4c">4</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>
```

## Item 13 - G22: remove internal lineage-status label from reader-facing close

Outcome: promote.

File: `fact-sheets/g22-robert-gournay-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
What is clear is that the descent through Robert is confirmed by Daniel Gurney's pedigree, which states explicitly that when Sir John's son died under age, "the estates passed to nephew Thomas" (son of Robert) — a statement grounded in the legal logic of medieval inheritance. Robert is thus classified as **Confirmed** in lineage status, even though almost no personal documentation survives, because his position in the succession is established by the broader pedigree evidence. <sup class="fn"><a href="#n6" id="ref-6d">6</a></sup>

new_string:
What is clear is that the descent through Robert is supported by Daniel Gurney's pedigree and by the modern History of Parliament account of Sir John's succession crisis: when Sir John's son died under age, the estates passed to Sir John's nephew Thomas, Robert's son. Robert remains personally elusive, but his place in the descent rests on that broader succession evidence rather than on a surviving personal archive of his own. <sup class="fn"><a href="#n6" id="ref-6d">6</a></sup>
```

## Item 14 - G18: keep Anthony's minority but remove unsupported Heydon wardship management

Outcome: promote.

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li><strong>Died vita patris, leaving his young son Anthony as eventual heir.</strong> William V died before his father William IV, who died on 18 January 1507/8 (per Daniel Gurney's pedigree). Their son Anthony — only nine or ten years old — inherited as a "boy lord" when William IV died, and the Norfolk Gurney estates were managed during Anthony's minority through wardship arrangements involving the Heydon kin. This is the second consecutive generation in which the senior heir died before his father, making the line skip a generation in inheritance terms. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>

new_string:
  <li><strong>Died vita patris, leaving his young son Anthony as eventual heir.</strong> William V died before his father William IV, who died on 18 January 1507/8 (per Daniel Gurney's pedigree). Their son Anthony — only nine or ten years old — inherited as a "boy lord" when William IV died; William IV's will explicitly shaped estate management around Anthony's minority by letting the executors take five years' profits from Harpley. The sources prove Anthony's minority and executor-management problem, but not a named Heydon-run wardship. This is the second consecutive generation in which the senior heir died before his father, making the line skip a generation in inheritance terms. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
William V died before his father William Gurney IV, who in turn died on 18 January 1507/8 (per Daniel Gurney's pedigree, supported by Blomefield's mention of "William Gournay, junior" in 14 Henry VII / 1499 — see the G19 fact sheet). <sup class="fn"><a href="#n10" id="ref-10b">10</a></sup> At William IV's death, the Norfolk Gurney estates passed to William V's young son Anthony — about nine years old — who inherited as a "boy lord." <sup class="fn"><a href="#n11" id="ref-11c">11</a></sup> Wardship arrangements during Anthony's minority would have involved his Heydon kinsmen; given that Anne Heydon had remarried Sir Lionel Dymoke of Ashby, Lincolnshire, by this date, Anthony's wardship was probably administered from Norfolk by his maternal uncles or by the Heydons of Baconsthorpe. <sup class="fn"><a href="#n5" id="ref-5e">5</a></sup>

new_string:
William V died before his father William Gurney IV, who in turn died on 18 January 1507/8 (per Daniel Gurney's pedigree, supported by Blomefield's mention of "William Gournay, junior" in 14 Henry VII / 1499 — see the G19 fact sheet). <sup class="fn"><a href="#n10" id="ref-10b">10</a></sup> At William IV's death, the Norfolk Gurney estates passed to William V's young son Anthony — about nine years old — who inherited as a "boy lord." <sup class="fn"><a href="#n11" id="ref-11c">11</a></sup> William IV's will shows that Anthony's minority had practical estate consequences: Daniel Gurney notes that a five-year Harpley-profits clause was made "in consequence of the minority of Anthony Gurney his grandson." The surviving citation layer does not identify the guardians or prove that Anthony's wardship was administered by Heydon kin. <sup class="fn"><a href="#n10" id="ref-10d">10</a></sup>
```

File: `fact-sheets/g18-william-gurney-v-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n10">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287, gives William IV's death as 18 January 1507/8 and William V's as <em>vita patris</em> before that date. <a class="citation-back" href="#ref-10">↩</a></li>

new_string:
  <li id="n10">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287, gives William IV's death as 18 January 1507/8 and William V's as <em>vita patris</em> before that date. Daniel Gurney, <em>Record</em>, Part II, pp. 404-405, prints William IV's will; a note to the Harpley-profits clause says the provision was made "in consequence of the minority of Anthony Gurney his grandson, who succeeded him." This supports Anthony's minority and executor-managed estate arrangements, but not a specific Heydon wardship administration. <a class="citation-back" href="#ref-10">↩</a></li>
```

## Item 15 - G19: tighten Burnham Thorpe inference and close Elizabeth/Thetford with DG's fuller evidence

Outcome: promote.

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
      <td><strong>Prioress of Thetford, 1518.</strong> A significant ecclesiastical position — Thetford had been one of the great Norfolk monastic houses. Her election to the prioress role on the eve of the Henrician dissolutions is the most distinguished individual achievement of any of William IV's children. <sup class="fn"><a href="#n12" id="ref-12h">12</a></sup></td>

new_string:
      <td><strong>Prioress of Thetford, 1518.</strong> Daniel Gurney separately says she was installed prioress of Thetford Nunnery in 1518 and died in 1519; this makes her one of the more individually visible daughters in the late-medieval Gurney pedigree, but her tenure was brief. <sup class="fn"><a href="#n12" id="ref-12h">12</a></sup></td>
```

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
He died at Burnham Thorpe on 18 January 1508 — a small but telling detail, suggesting he was visiting his Calthorpe in-laws in his last illness, or that he had some independent interest in the village that drew him there at the end of his life. <sup class="fn"><a href="#n2" id="ref-2c">2</a></sup> His eldest son William V had already died <em>vita patris</em>; his nine-year-old grandson Anthony succeeded as direct heir. <sup class="fn"><a href="#n11" id="ref-11c">11</a></sup> Of his other children, his son Walter founded the cadet line of Gurneys at Cley-next-the-Sea (and from there at Cawston and Aylsham), his son Thomas founded the line of Gurneys at Dartmouth, London, and Essex (whose grandson Richard Gurney would be Sheriff of London under Elizabeth I), his son Christopher became Rector of Harpley (the same living his ancestors had presented to since the 14th century), and his daughter Elizabeth became Prioress of Thetford in 1518 — on the very eve of the Henrician dissolution that would close her house within twenty years. <sup class="fn"><a href="#n12" id="ref-12j">12</a></sup><sup class="fn"><a href="#n13" id="ref-13d">13</a></sup>

new_string:
He died at Burnham Thorpe on 18 January 1508 — a sourceable place of death, and one that places him at the Calthorpe family's home village at the end of his life, though the record does not say whether he was visiting in-laws, resident there, or present for some other estate reason. <sup class="fn"><a href="#n2" id="ref-2c">2</a></sup> His eldest son William V had already died <em>vita patris</em>; his nine-year-old grandson Anthony succeeded as direct heir. <sup class="fn"><a href="#n11" id="ref-11c">11</a></sup> Of his other children, his son Walter founded the cadet line of Gurneys at Cley-next-the-Sea (and from there at Cawston and Aylsham), his son Thomas founded the line of Gurneys at Dartmouth, London, and Essex (whose grandson Richard Gurney would be Sheriff of London under Elizabeth I), his son Christopher became Rector of Harpley (the same living his ancestors had presented to since the 14th century), and his daughter Elizabeth was installed Prioress of Thetford in 1518 and died in 1519. <sup class="fn"><a href="#n12" id="ref-12j">12</a></sup><sup class="fn"><a href="#n13" id="ref-13d">13</a></sup>
```

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
That last detail is one of the more poignant in this stretch of the family history. Elizabeth Gurney was elected prioress of one of the great Norfolk monastic houses just as the entire English religious order was about to be swept away. She had no way of knowing in 1518 that the world she had entered would not survive her. <sup class="fn"><a href="#n12" id="ref-12k">12</a></sup>

new_string:
That last detail is still poignant, but in a narrower way than the earlier draft implied. Elizabeth Gurney did not live into the Dissolution crisis; Daniel Gurney says she died in 1519. What the record does show is that a Gurney daughter briefly reached the headship of a Norfolk religious house just before the Reformation generation began. <sup class="fn"><a href="#n12" id="ref-12k">12</a></sup>
```

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n12">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287, naming all surviving children. <a class="citation-back" href="#ref-12">↩</a></li>

new_string:
  <li id="n12">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287, naming all surviving children, including "Elizabeth, Prioress of Thetford, 1518." Daniel Gurney, <em>Record</em>, Part II, p. 425, separately says "Lady Elizabeth Gurney" was installed prioress of Thetford Nunnery in 1518 and died in 1519. This supports the office and brief tenure; it does not support wording that implies she lived to experience the Dissolution. Source ID: <code>dg-rec-pt2</code>. <a class="citation-back" href="#ref-12">↩</a></li>
```

File: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
      <tr><td>1518</td><td>Daughter Elizabeth elected Prioress of Thetford — twenty years before its dissolution.</td></tr>

new_string:
      <tr><td>1518-1519</td><td>Daughter Elizabeth installed Prioress of Thetford; Daniel Gurney says she died in 1519.</td></tr>
```

## Item 16 - G20: promote the 1445 Hunstanton Hall seal from research into the fact sheet

Outcome: promote.

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
Thomas was born around 1430, son and heir of Thomas Gournay I (G21) by Catherine Kerville of Watlington. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup> His father had himself inherited the West Barsham estates only recently — through the collateral succession that followed the death of Sir John Gurney V (the d. 1408 sheriff and MP) when John's only son Edmund died as a minor, sending the inheritance sideways to Sir John's nephew Thomas I. <sup class="fn"><a href="#n11" id="ref-11b">11</a></sup> This meant that by the time Thomas II came of age around 1451, the family had been in possession of West Barsham for about eighty years and of Harpley for more than a century — long enough for all three of the family's main residences to be treated as fully integrated family seats. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup>

new_string:
Thomas was born around 1430, son and heir of Thomas Gournay I (G21) by Catherine Kerville of Watlington. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup> His father had himself inherited the West Barsham estates only recently — through the collateral succession that followed the death of Sir John Gurney V (the d. 1408 sheriff and MP) when John's only son Edmund died as a minor, sending the inheritance sideways to Sir John's nephew Thomas I. <sup class="fn"><a href="#n11" id="ref-11b">11</a></sup> By 1445, a Thomas Gurnay, Esq., was one of the sealers of an East Barsham feoffment preserved at Hunstanton Hall; because Daniel Gurney's Supplement separately says Thomas I was probably dead before 1444, the G20 companion treats this as Thomas II's first known adult attestation and evidence that he was already acting in the family network by the mid-1440s. <sup class="fn"><a href="#n15" id="ref-15">15</a></sup>
```

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n14">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), vol. II, letter dated St George's Day (23 April) 1452, written from Norwich to the Duke of Norfolk's deputy at Framlingham. The preserved extract at <code>sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md</code> names Thomas Gurnay among the signers and gives the complaint against Charles Nowell and others for assaults and riots against John Paston and his kin, friends, and neighbours. The later 1471 Heydon-supervisor contrast is from Blomefield's West Barsham will extract, cited in note 13; broader claims about factional realignment should remain cautious unless supported by a dedicated secondary source. Project Gutenberg vol. II: <a href="https://www.gutenberg.org/cache/epub/40989/pg40989.txt">www.gutenberg.org/cache/epub/40989/pg40989.txt</a>. Source IDs: <code>paston-letters-gairdner</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-14">↩</a></li>

new_string:
  <li id="n14">James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), vol. II, letter dated St George's Day (23 April) 1452, written from Norwich to the Duke of Norfolk's deputy at Framlingham. The preserved extract at <code>sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md</code> names Thomas Gurnay among the signers and gives the complaint against Charles Nowell and others for assaults and riots against John Paston and his kin, friends, and neighbours. The later 1471 Heydon-supervisor contrast is from Blomefield's West Barsham will extract, cited in note 13; broader claims about factional realignment should remain cautious unless supported by a dedicated secondary source. Project Gutenberg vol. II: <a href="https://www.gutenberg.org/cache/epub/40989/pg40989.txt">www.gutenberg.org/cache/epub/40989/pg40989.txt</a>. Source IDs: <code>paston-letters-gairdner</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-14">↩</a></li>
  <li id="n15">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew &amp; Son, 1858), Note 126, p. 814, records an 8 June 1445 deed in the charter room at Hunstanton Hall: Sir Thomas Kerdeston, Sir William Oldhalle, Thomas Gurnay, Esq., and others, to John Wode of Berston and others, of the manor called Waldgraves in East Barsham. Daniel Gurney notes Thomas Gurnay's red-wax seal on the fifth label. The G20 research companion assigns this to Thomas II because DG-Supp Note 123 says Thomas I was probably dead before 1444. Source ID: <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-15">↩</a></li>
```

## Item 17 - G20: polish remaining highlight overextensions

Outcome: promote.

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li><strong>Women's wool work as a family business.</strong> The 1471 will's bequest of "all the woolen and linen cloths" to Margaret as her own work and that of her servants is direct evidence that Margaret ran a productive textile operation within the household — spinning and weaving wool from her husband's flocks for the family's own use and, implicitly, for exchange or sale. This was standard for substantial Norfolk gentry wives of the period, but Thomas's will is one of the few surviving documents to make the domestic side of it explicit. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>

new_string:
  <li><strong>Women's wool work in the household economy.</strong> The 1471 will's bequest of "all the woolen and linen cloths" to Margaret as her own work and that of her servants is direct evidence that Margaret and her servants produced valuable cloth within the household. Daniel Gurney places that bequest in a Norfolk wool economy where gentlemen prepared wool for market and household women spun yarn or sometimes wove prepared wool at home. Exchange or sale is possible, but the will itself proves household textile labor, not a quantified commercial business. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li><strong>Lived through the middle decades of the Wars of the Roses.</strong> Thomas's active life c. 1430–1471 spans the entire opening phase of the dynastic civil war — from the outbreak of open conflict at St Albans in 1455, through the Yorkist seizure of the throne in 1461, to the brief Lancastrian restoration in 1470–71 and Edward IV's decisive return at Barnet (April 1471) and Tewkesbury (May 1471). Thomas died and his will was proved just weeks after Edward IV's final victory. There is no record of his personal role on either side — characteristic of the middling Norfolk gentry, who mostly kept their heads down while the great magnates fought. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>

new_string:
  <li><strong>Lived through the middle decades of the Wars of the Roses.</strong> Thomas's active life c. 1430–1471 spans the opening phase of the dynastic civil war — from St Albans in 1455 through the Yorkist seizure of the throne in 1461, the brief Lancastrian restoration in 1470–71, and Edward IV's return at Barnet and Tewkesbury. Thomas died and his will was proved just weeks after Edward IV's final victory. No battlefield role has been found for him; his clearest political trace is instead local, in the 1452 Paston-side petition and the later 1471 choice of John Heydon as will supervisor. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup><sup class="fn"><a href="#n14" id="ref-14b">14</a></sup></li>
```

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
Thomas Gournay II is, for a 15th-century Norfolk gentleman, unusually well attested by the standards of his own generation — not through Crown office or court appearance, but through a single document: his will, dated at West Barsham and proved on 27 July 1471. That will, which genealogist Daniel Gurney drew on heavily in the <em>Record of the House of Gournay</em>, is the earliest Gurney will to survive with full personal detail, and it contains more about its maker's daily life than any other document in the early West Barsham sequence. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n12" id="ref-12g">12</a></sup>

new_string:
Thomas Gournay II is, for this stretch of the line, unusually well attested — not through Crown office or court appearance, but through a cluster of documents culminating in his will, dated at West Barsham and proved on 27 July 1471. That will, which genealogist Daniel Gurney drew on heavily in the <em>Record of the House of Gournay</em>, is the earliest Gurney will to survive with full personal detail, and it contains more about its maker's daily life than any other document in the early West Barsham sequence. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n12" id="ref-12g">12</a></sup>
```

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
Thomas's principal documentary moment is his will. Dated at West Barsham on 18 March 1469/70 and proved by the Norwich Consistory Court on 27 July 1471, the will is one of the most detailed pre-Tudor Norfolk gentry wills to survive. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup> It names three simultaneous family residences — West Barsham Hall in north Norfolk, a house at Harpley twenty miles to the west, and a town house in St Gregory's parish in the heart of Norwich — and directs that Thomas be buried in the chancel of St Lawrence at Harpley if he dies there, or in the Greyfriars' church at Norwich if he dies there. The Norwich house was to be sold to his son William for 80 marks (about £53 in the money of the time), the first quantified valuation of any Gurney urban property. The Hardingham manor of Swathings, which Thomas had bought from a Catherine Sturmer at some earlier date, was to descend with the rest of the patrimony. Bequests of 40 shillings to the Norwich Greyfriars and 20 shillings each to the Augustinian Friars, the Dominicans, and the Carmelites placed Thomas inside the standard "all four orders" benefaction pattern of substantial Norfolk gentry. His personal confessor was John Bernard, a Franciscan friar at Norwich. The will's most personal touch is a gold ring set with a turquoise, left to the chapel of the Annunciation at Walsingham Priory, together with £10 to the prior toward a building project in exchange for entry into the priory's beadroll "as brother and sister of that priory" — a perpetual-prayer commitment to what was then the principal Marian pilgrimage shrine of England. <sup class="fn"><a href="#n12" id="ref-12h">12</a></sup>

new_string:
Thomas's principal documentary moment is his will. Dated at West Barsham on 18 March 1469/70 and proved by the Norwich Consistory Court on 27 July 1471, it is one of the richest Gurney family documents before the Tudor period. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup> It names three simultaneous family residences — West Barsham Hall in north Norfolk, a house at Harpley twenty miles to the west, and a town house in St Gregory's parish in the heart of Norwich — and directs that Thomas be buried in the chancel of St Lawrence at Harpley if he dies there, or in the Greyfriars' church at Norwich if he dies there. The Norwich house was to be sold to his son William for 80 marks (about £53 in the money of the time), the first quantified valuation of any Gurney urban property. The Hardingham manor of Swathings, which Thomas had bought from a Catherine Sturmer at some earlier date, was to descend with the rest of the patrimony. Bequests of 40 shillings to the Norwich Greyfriars and 20 shillings each to the Augustinian Friars, the Dominicans, and the Carmelites placed Thomas inside the standard "all four orders" benefaction pattern of substantial Norfolk gentry. His personal confessor was John Bernard, a Franciscan friar at Norwich. The will's most personal touch is a gold ring set with a turquoise, left to the chapel of the Annunciation at Walsingham Priory, together with £10 to the prior toward a building project in exchange for entry into the priory's beadroll "as brother and sister of that priory" — a perpetual-prayer commitment to what was then the principal Marian pilgrimage shrine of England. <sup class="fn"><a href="#n12" id="ref-12h">12</a></sup>
```

## Item 18 - G20: restore a compelling but bounded 1452-to-1471 political arc

Outcome: promote.

File: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
A single dated letter places Thomas inside Norfolk gentry politics in his early adulthood. On St George's Day 1452, Thomas signed a petition from Norwich to the Duke of Norfolk's deputy at Framlingham, complaining of "dyvers assaughtes and ryottes made be Charles Nowell and other ageyn the Kyngs lawe and peas… up on John Paston and other of owre kynne, frendes and neyghborys." The co-signers included Sir John Heveningham, John Ferrers, John Groos, William Rokewode, the two John Bakons, John Pagrave, Robert Mortimer, and Nicholas Appleyard. The letter shows Thomas with the Paston-friendly signers at that moment; the later contrast is that his 1471 will named John Heydon of Baconsthorpe as supervisor. That is enough to show a changed working relationship without making the fact sheet carry more factional analysis than the cited extract can support. <sup class="fn"><a href="#n14" id="ref-14">14</a></sup>

new_string:
A single dated letter places Thomas inside Norfolk gentry politics in his early adulthood. On St George's Day 1452, Thomas signed a petition from Norwich to the Duke of Norfolk's deputy at Framlingham, complaining of "dyvers assaughtes and ryottes made be Charles Nowell and other ageyn the Kyngs lawe and peas… up on John Paston and other of owre kynne, frendes and neyghborys." The co-signers included Sir John Heveningham, John Ferrers, John Groos, William Rokewode, the two John Bakons, John Pagrave, Robert Mortimer, and Nicholas Appleyard. The letter shows Thomas with Paston-friendly signers at that moment; the later contrast is that his 1471 will named John Heydon of Baconsthorpe as supervisor. The source-backed arc is local rather than total: in 1452 Thomas appears in a Paston-side petition against violence by Charles Nowell and others; by 1471 he trusted the Heydon legal circle enough to make John Heydon the senior overseer of his will. <sup class="fn"><a href="#n14" id="ref-14">14</a></sup>
```

## Item 19 - G21: narrow death bracket and correct the 1445-seal attribution

Outcome: promote.

File: `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
pageHeading: Thomas Gournay I (fl. c. 1408 – c. 1450)

new_string:
pageHeading: Thomas Gournay I (fl. c. 1408 – probably before 1444)
```

File: `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
    <div class="fact-value">c. 1450. No will or probate date recorded. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>

new_string:
    <div class="fact-value">Probably before 1444. No will or probate date recorded. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

File: `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n2">Daniel Gurney, <em>Record</em> (1848) pedigree p. 286 gives neither a probate date nor a specific death year. Active period c. 1408 (when his uncle died) to c. 1450 (when his son Thomas II was approximately 20–25, preparing to succeed him within a generation). <a class="citation-back" href="#ref-2">↩</a></li>

new_string:
  <li id="n2">Daniel Gurney, <em>Record</em> (1848) pedigree p. 286 gives neither a probate date nor a specific death year. Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew &amp; Son, 1858), Note 123, p. 794, says the 1444 Boking fine was probably with Thomas Gurney II and Margaret Jernegan, and that Thomas Gurney I was therefore dead before 1444. This is a probable terminus ante quem, not a probate date. Source IDs: <code>dg-rec-pt2</code>, <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-2">↩</a></li>
```

File: `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
  <li id="n11">1434-35 East Barsham feoffment (with John Hunt, son of William Hunt of East-Barsham, confirming Wolterton's Manor to John Wode): Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: East-Barsham," pp. 53-65, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp53-65">British History Online</a>. Military service: AHRC <em>Soldier in Later Medieval England Online Database</em>, <a href="https://www.medievalsoldier.org/">www.medievalsoldier.org</a>, Thomas Gourney/Gournay records in John Holland's 1415 retinue (TNA E101/45/7, m. 1; TNA E101/45/18, m. 2), Thomas Beaufort's 1418 Harfleur garrison (TNA E101/48/6), and John de Vere's 1441 retinue under Richard of York (TNA E101/53/33, m. 1). 1445 Hunstanton seal: Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew &amp; Son, 1858), Note 126, p. 814. <a class="citation-back" href="#ref-11">↩</a></li>

new_string:
  <li id="n11">1434-35 East Barsham feoffment (with John Hunt, son of William Hunt of East-Barsham, confirming Wolterton's Manor to John Wode): Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: East-Barsham," pp. 53-65, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp53-65">British History Online</a>. Military service: AHRC <em>Soldier in Later Medieval England Online Database</em>, <a href="https://www.medievalsoldier.org/">www.medievalsoldier.org</a>, Thomas Gourney/Gournay records in John Holland's 1415 retinue (TNA E101/45/7, m. 1; TNA E101/45/18, m. 2), Thomas Beaufort's 1418 Harfleur garrison (TNA E101/48/6), and John de Vere's 1441 retinue under Richard of York (TNA E101/53/33, m. 1). The 1445 Hunstanton Hall seal is reassigned to G20 Thomas II in this patchset because the G20 companion already identifies it that way and DG-Supp Note 123 makes Thomas I probably dead before 1444. <a class="citation-back" href="#ref-11">↩</a></li>
```

File: `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
He died around 1450, leaving his only recorded son Thomas II to continue the line. By the time Thomas II in turn made his will in 1471, the family had spent roughly seventy years holding an estate that technically should have belonged to a cousin who died before his time. <sup class="fn"><a href="#n2" id="ref-2d">2</a></sup><sup class="fn"><a href="#n10" id="ref-10c">10</a></sup>

new_string:
He probably died before 1444, if Daniel Gurney's reading of the Boking fine is correct, leaving his only recorded son Thomas II to continue the line. By the time Thomas II in turn made his will in 1471, the family had spent roughly seventy years holding an estate that had come to them through the death of Sir John V's under-age son Edmund. <sup class="fn"><a href="#n2" id="ref-2d">2</a></sup><sup class="fn"><a href="#n10" id="ref-10c">10</a></sup>
```

File: `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Operation: `str_replace`

```text
old_string:
      <tr><td>c. 1450</td><td>Dies. Son Thomas II succeeds.</td></tr>

new_string:
      <tr><td>probably before 1444</td><td>Dies before the Boking fine if Daniel Gurney's attribution of that fine to Thomas II is correct. Son Thomas II succeeds.</td></tr>
```

## Validation instructions for Phase 2

After applying the replacements:

1. Run a targeted check that no `NEW` handles were introduced and that all modified `ref-*` anchors still resolve.
2. Run `git diff --check`.
3. Run `npm.cmd run validate` from `site/website`.
4. Run `npm.cmd run package` from `site/website`.

## Remaining review targets and revision decisions

- G18 still relies partly on Wikipedia/WikiTree for Heydon-Boleyn relationships. The patchset reduces the impact of that reliance but does not replace the Sir Henry Heydon / Anne Boleyn the elder source chain with a first-hand PCC will or scholarly pedigree.
- G19 Burnham Thorpe death-location interpretation is narrowed to what the record supports: place of death in the Calthorpe home village, with no stated reason for his presence there.
- G19 Elizabeth Gurney as Prioress of Thetford is source-closed for office, installation year, and death year using Daniel Gurney. Monastery-specific context could still be enriched later from Blomefield/British History Online, but this patchset removes the inaccurate implication that Elizabeth lived to see the Dissolution.
- G20 the "most detailed pre-Tudor Norfolk gentry will" formulation is narrowed to "richest Gurney family documents before the Tudor period." A future pass could still bring in a dedicated medieval-wills secondary source if broader comparative language is desired.
- G21 death bracket is narrowed to probably before 1444, and the 1445 Hunstanton Hall seal is moved to G20 Thomas II. The remaining optional improvement is a direct pull of the underlying muster rolls and Hunstanton deed image, not necessary for this Phase 1 patchset.
