# v78 — Medieval-soldier discovery: G22 + G21 fact-sheet promotions (story-led)

**Scope:** Phase 2 application. Rewrites the G22 Robert fact sheet's Highlights and Narrative into a plain-spoken, picture-painting account, and adds one affinity-continuity passage to G21. The aim for G22 (a lightly recorded younger son) is to *show the man through his context* rather than recite facts: that a second son's thin record is the normal shape of the evidence; that his exceptionally well-documented father, brother, and son let us see his world; that the family arms carry the line straight through him; and that the inter-family nexus (Lancaster + Arundel, Norwich + Lynn, soldiering, marriage, shared arms) is the genealogical foundation on which a sparsely recorded line rests securely.

Sources are already registered/queued: `walker-lancastrian-affinity-1361-1399`, `hop-gurney`, `medievalsoldier-database`, `dg-rec-pt1`, `dg-rec-pt2`. New G22 footnotes n9 (affinity), n10 (military), n11 (arms); new G21 footnote n13. No renumbering.

**G24 — recommended NOT promoted** (this arc): the G24 finding is *negative* — the soldier-database "Sir John de Gournay" knight is Sir John de Gourney of Harptree, Somerset, not G24. The disambiguation lives in the G24 companion (v76). A separate story-weaving pass on the G23, G24, and G29 narratives is queued (`stub-v79.md`) for after the G22 style is confirmed.

---

## Item 01 — Rewrite the G22 Highlights (`fact-sheets/g22-robert-gournay-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace` (replace the whole Highlights `<ul>` — three bullets become five, plain-spoken and story-led).

**old_string:**
```
<ul>
  <li><strong>Even his given name is uncertain.</strong> In his Edmund Gournay chapter, the genealogist Daniel Gurney wrote of "a second son, whom we believe was named Robert" — an explicit editorial hedge. The only other source he cites for Edmund's children is the 1622 pedigree by Cook, Clarenceux King of Arms. Robert is the most probable identification, not a confirmed one. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>The direct line descends through him because his brother's son died young.</strong> Robert's elder brother Sir John Gurney V (d. 4 December 1408) inherited all the family estates, was sheriff of Norfolk and Suffolk in 1399 and again at his death in 1408, sat in Parliament for the Coventry parliament of 1404, and married Alice Heylesdon — daughter and eventual sole heir of the wealthy London mercer and former alderman John Heylesdon — bringing into the family the manors of Hellesdon and Drayton, the advowsons of both parish churches, the two chantries founded in her father's memory, houses in Norwich, and the great London warehouse known as "La Selde Coronata" (a merchant's storehouse). Sir John appeared to be the main line. But his only son Edmund, aged ten at his father's death, "followed him to the grave not long afterwards." The estates passed to Robert's son Thomas I — making Robert the pivotal ancestor through whom the entire subsequent West Barsham Gurney family (and through Francis Gurney, probably the American Gurneys) descend. The full sequence is documented in the History of Parliament Online biography of Sir John Gurney d. 1408. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>His father was one of the most connected men in East Anglia.</strong> Born into a family at the height of its social and professional reach — father steward of John of Gaunt, mother heiress of West Barsham, elder brother heading toward a knighthood and a parliamentary career — Robert would have grown up in the most prosperous and well-connected household the family had known. What he did with that inheritance, in personal terms, is unrecorded. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
</ul>
```

**new_string:**
```
<ul>
  <li><strong>Even his name is a best guess.</strong> The genealogist Daniel Gurney could only write that Edmund Gournay had "a second son, whom we believe was named Robert," resting on a single herald's pedigree drawn up in 1622. "Robert" is the likeliest reading, not a certainty — a fitting start for the most lightly recorded man in the direct line. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>A second son — and that explains most of the silence.</strong> In Robert's England the eldest son took the land, the title, the offices, and the paperwork they generated. His elder brother John got West Barsham and a public career; Robert, the younger, was provided for quietly and left only a faint trail. The thinness of his record is exactly what you would expect of a gentry second son — not a gap in the story, but the normal shape of the evidence. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></li>
  <li><strong>The whole later family descends through him — by an accident of death.</strong> His brother Sir John Gurney V seemed to carry the line: sheriff of Norfolk and Suffolk, member of Parliament, husband of a rich London heiress. But Sir John's only son died as a boy, the senior line failed, and the entire estate passed sideways to Robert's son Thomas. A man who left almost no record of his own became the hinge on which the family turned. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>We can't see Robert, but we can see his world.</strong> His father Edmund was a leading lawyer retained by John of Gaunt — drawing a fee even from St Benet's Holme abbey — and the Norfolk steward of the earls of Arundel; his brother served Gaunt in Aquitaine in 1394; his son rode in John Holland's retinue at Agincourt in 1415. Robert lived his whole life inside that web of Lancaster-and-Arundel connection, Norwich and Lynn business, and family soldiering. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup><sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
  <li><strong>The family's red cross runs straight through him.</strong> The Gurney arms — a red <a href="https://en.wikipedia.org/wiki/Engrailed">engrailed</a> cross on silver — were borne by his crusader ancestor, sealed by his grandfather, and displayed by his father joined with his mother's Wauncy coat; his son carried them on and added a gurnard fish as a pun on the name. No seal of Robert's own survives, yet the heraldic thread is unbroken on both sides of him — a visible token of the continuity the pedigree records. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></li>
</ul>
```

---

## Item 02 — Rewrite the G22 Narrative (`fact-sheets/g22-robert-gournay-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace` (replace the full Narrative body — four paragraphs become five that paint the picture).

**old_string:**
```
Robert Gournay is, genealogically, one of the most important figures in the junior Norfolk branch — and one of the most elusive. He is the man through whom every subsequent generation descends, yet the genealogist Daniel Gurney himself was uncertain enough about his name to write only that Edmund Gournay had "a second son, whom we believe was named Robert." <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup> No deed bearing Robert's name, no court appearance, no will, no land transaction has been identified in the sources reviewed. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup> He exists in the record almost entirely as a relationship — son of Edmund, brother of Sir John, father of Thomas, husband of Joan de Norwich. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup><sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>

Robert's obscurity fits what the surviving evidence actually shows: his elder brother Sir John V carried the offices, manors, parliamentary service, and long administrative trail, while no deed, will, court appearance, or land transaction has been found that names Robert in his own right. <sup class="fn"><a href="#n3" id="ref-3c">3</a></sup><sup class="fn"><a href="#n6" id="ref-6e">6</a></sup> His marriage to Joan de Norwich may point toward the Norwich civic world that his father Edmund had served as standing counsel, but the sources only give her name; they do not identify her parents, family, or property. <sup class="fn"><a href="#n4" id="ref-4c">4</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>
The critical event of Robert's life — or rather of his family's life — was one over which he had no control: his nephew Edmund (son of Sir John V) died under age, leaving no heir. The History of Parliament biography of Sir John Gurney d. 1408 gives us the precise sequence: Sir John was reappointed sheriff of Norfolk and Suffolk on 15 November 1408, but died less than three weeks later, on 4 December 1408. His only son Edmund, then ten years old, followed him to the grave "not long afterwards." At that point the entire estate — West Barsham, Harpley, Hardingham, the Wauncy lands at Depden in Suffolk, the great London warehouse "La Selde Coronata" that Sir John had brought in by marriage to the wealthy mercer's daughter Alice Heylesdon, and the rest of the portfolio Edmund Gournay G23 had assembled — passed by right of inheritance to Robert's son Thomas I, as the surviving male-line heir. Robert may or may not have lived to see this; the dates are too uncertain to say. Sir John's widow Alice survived him by at least 25 years, sold "Loundhall" in Saxthorpe to John Wynter to pay her late husband's debts, then married twice more — first the Fitzalan retainer Sir John Wiltshire (d. 1428), then Richard Selling, esquire — and in 1433 sold the bulk of her Heylesdon inheritance to Sir John Fastolf KG, the Norfolk soldier-magnate of Caister Castle. <sup class="fn"><a href="#n6" id="ref-6c">6</a></sup>

The descent through Robert is supported by Daniel Gurney's pedigree and by the modern History of Parliament account of Sir John's succession crisis: when Sir John's son died under age, the estates passed to Sir John's nephew Thomas, Robert's son. Robert remains personally elusive, but his place in the descent rests on that broader succession evidence rather than on a surviving personal archive of his own. <sup class="fn"><a href="#n6" id="ref-6d">6</a></sup>
```

**new_string:**
```
Robert Gournay was the second son of Edmund Gournay, and in the England of his day that single fact explains most of what we will never know about him. Land, title, public office, and the records they threw off all passed to the eldest son — here, Robert's brother John. A younger son was settled more modestly and left a far fainter mark. So when the family's Victorian genealogist came to write Robert down five centuries later, he could manage only "a second son, whom we believe was named Robert." No deed, will, or court roll has been found in his name. That silence is the ordinary fate of a gentry younger son, not a sign that anything has gone missing. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup><sup class="fn"><a href="#n3" id="ref-3b">3</a></sup>

What we cannot see in Robert himself we can read clearly in the people around him, because they are unusually well documented — and they tell us what his world was like. His father Edmund was a lawyer of county-wide standing: retained by John of Gaunt to help run the Duke's East Anglian estates, drawing a fee even from the Broadland abbey of St Benet's Holme, steward to the earls of Arundel from whom the family held Harpley, and standing counsel to both Norwich and Bishop's Lynn. His mother Katherine was the heiress who had brought the manor of West Barsham into the family. Robert grew up, in other words, in the most prosperous and best-connected household the Gurneys had ever kept, moving in a world of lawyers, sheriffs, merchants, and magnate servants. <sup class="fn"><a href="#n7" id="ref-7b">7</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup>

The public face of his generation was his elder brother, Sir John Gurney V. While Robert kept to the background, Sir John was sheriff of Norfolk and Suffolk in 1399 and again at his death in 1408, escheator and justice of the peace, a friend of Sir Thomas Erpingham, and member of Parliament for Norfolk in the Coventry parliament of 1404. He married Alice Heylesdon, daughter and heir of a wealthy London mercer, and with her came the manors of Hellesdon and Drayton, houses in Norwich, and a City of London warehouse called "La Selde Coronata." He carried the family's Lancastrian loyalty into the field too, taking out letters for John of Gaunt's 1394 expedition to Aquitaine. Robert, for his part, married Joan de Norwich — a name that points toward the Norwich civic world his father served, though the records keep nothing of her beyond it. The two brothers are the story of this generation: one in the full light of the public record, the other almost entirely in its shadow. <sup class="fn"><a href="#n6" id="ref-6b">6</a></sup><sup class="fn"><a href="#n4" id="ref-4b">4</a></sup>

The family's own emblem ran straight through Robert even where its paperwork did not. The Gurney arms — argent, a cross engrailed gules, a red scalloped cross on a silver field — had been borne by his ancestor Sir John de Gournay on crusade with the future Edward I, sealed by his grandfather Sir William, and displayed by his father Edmund joined with the Wauncy coat his marriage had brought in, in glass at Norwich and at Denton church. Robert's own son Thomas would carry the same cross and add a gurnard fish for a crest, a pun on the family name. No seal of Robert's survives, but the heraldic line is unbroken immediately above and below him — a small, concrete sign that the pedigree's claim is sound. <sup class="fn"><a href="#n11" id="ref-11b">11</a></sup>

Then came the turn that made this near-invisible man matter. Sir John V was reappointed sheriff on 15 November 1408 and died less than three weeks later, on 4 December. His only son Edmund, just ten years old, "followed him to the grave not long afterwards," and the senior line failed with him. The whole estate Edmund Gournay had assembled — West Barsham, Harpley, Hardingham, the Suffolk lands at Depden, the London warehouse and the Heylesdon manors — passed by right of blood to Robert's son Thomas. Whether Robert lived to see it we cannot say; his dates are too vague. But that is the point: the line continued not because Robert achieved anything, but because of where he stood within it. And the dense lattice of family ties around him — to Lancaster and to Arundel, to Norwich and to Lynn, through marriage, soldiering, and shared arms — is exactly what lets us trust that line even though Robert's own archive is empty. The connections, not the deeds, are the foundation here. <sup class="fn"><a href="#n6" id="ref-6c">6</a></sup><sup class="fn"><a href="#n10" id="ref-10b">10</a></sup></section>
```

---

## Item 03 — Add footnotes n9, n10, n11 to the G22 citation list (`fact-sheets/g22-robert-gournay-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace` (insert before the closing `</ol>`).

**old_string:**
```
  <li id="n8">Daniel Gurney, <em>Record</em> (1848), p. 280. Daniel Gurney, <em>Supplement</em> (1858) (John V chapter) for the succession. <a class="citation-back" href="#ref-8">↩</a></li>
</ol>
```

**new_string:**
```
  <li id="n8">Daniel Gurney, <em>Record</em> (1848), p. 280. Daniel Gurney, <em>Supplement</em> (1858) (John V chapter) for the succession. <a class="citation-back" href="#ref-8">↩</a></li>
  <li id="n9">For Edmund's place in John of Gaunt's retained East Anglian affinity — "the principal legal adviser to the burgesses of Lynn," who took a fee from the abbey of St Benet's Holme — see Simon Walker, <em>The Lancastrian Affinity 1361–1399</em>, Oxford Historical Monographs (Oxford: Clarendon Press, 1990), note 19. For Edmund as steward of the Norfolk estates of Richard FitzAlan, earl of Arundel, "from whom the Gurneys held their manor at Harpley," see the History of Parliament Online biography of Sir John Gurney (d. 1408). Source IDs: <code>walker-lancastrian-affinity-1361-1399</code>, <code>hop-gurney</code>. <a class="citation-back" href="#ref-9">↩</a></li>
  <li id="n10">The family's Lancastrian military service is recorded in the AHRC <em>Soldier in Later Medieval England Online Database</em> (<a href="https://www.medievalsoldier.org/">www.medievalsoldier.org</a>): Sir John Gurney V, letters of attorney for John of Gaunt's Aquitaine expedition, 1394 (The National Archives C61/104, m. 7); Thomas Gournay I, man-at-arms in John Holland's retinue on the 1415 Agincourt campaign (The National Archives E101/45/7, m. 1, and E101/45/18, m. 2). John Holland, earl of Huntingdon, was a grandson of John of Gaunt through his mother Elizabeth of Lancaster. See the research note <em>Gurney / Gournay in the medieval soldier record</em> for the full analysis. Source ID: <code>medievalsoldier-database</code>. <a class="citation-back" href="#ref-10">↩</a></li>
  <li id="n11">The family arms — argent, a cross engrailed gules — are first attested for Sir John de Gournay I (G27), who accompanied the future Edward I to the Holy Land in 1270: Daniel Gurney, <em>Record of the House of Gournay</em> (1848), pp. 339–341 (citing Hearne's Leland's <em>Collectanea</em>, ii. 613). Sir William de Gournay III (G26) "seals with an engrailed cross" in 1294 (ibid., pedigree p. 286). Edmund Gournay (G23) bore the engrailed cross impaling the Wauncy coat (gules, three dexter hand-gloves argent), recorded in glass at Gurney's Place in St Julian's parish, Norwich, and at Denton church (ibid., Part II, p. 358). Thomas Gournay I (G21) used the same arms with a gurnard-fish crest, a pun on the surname (ibid., pedigree p. 286). Robert, as Edmund's son and Thomas's father, stands within this unbroken heraldic descent. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-pt2</code>. <a class="citation-back" href="#ref-11">↩</a></li>
</ol>
```

---

## Item 04 — Add the affinity-continuity passage to the G21 Narrative (`fact-sheets/g21-thomas-gournay-i-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace`.

**old_string:**
```
What has been found is a narrower but real record: service as a man-at-arms in France in 1415, 1418, and 1441, and a 1434-35 appearance as a feoffee (trustee) on an East Barsham land transfer with John Hunt. He took for his heraldic crest a gurnard — a spiny sea-fish whose name plays on "Gurney."<sup class="fn"><a href="#n12" id="ref-12">12</a></sup> The cumulative picture is of a quietly active Norfolk gentleman. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup>
He probably died before 1444, leaving his only recorded son Thomas II to continue the line.
```

**new_string:**
```
What has been found is a narrower but real record: service as a man-at-arms in France in 1415, 1418, and 1441, and a 1434-35 appearance as a feoffee (trustee) on an East Barsham land transfer with John Hunt. He took for his heraldic crest a gurnard — a spiny sea-fish whose name plays on "Gurney."<sup class="fn"><a href="#n12" id="ref-12">12</a></sup> The cumulative picture is of a quietly active Norfolk gentleman. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup>

That soldiering ran in the family's grain rather than against it. The Gurneys had been clients of the house of Lancaster for two generations before Thomas drew his sword: his grandfather Edmund had been a retained adviser in John of Gaunt's East Anglian circle, and his uncle Sir John Gurney V had taken out letters for Gaunt's expedition to Aquitaine in 1394. When Thomas mustered under John Holland — a grandson of Gaunt — for the Agincourt campaign of 1415, and again under Thomas Beaufort — a son of Gaunt — in the Harfleur garrison in 1418, he was following a path the family had walked for half a century. His war service was not a private adventure but the third generation of a Lancastrian connection. <sup class="fn"><a href="#n13" id="ref-13">13</a></sup>
He probably died before 1444, leaving his only recorded son Thomas II to continue the line.
```

---

## Item 05 — Add footnote n13 to the G21 citation list (`fact-sheets/g21-thomas-gournay-i-fact-sheet.md`)

**Outcome:** promote. **Operation:** `str_replace` (insert before the closing `</ol>`).

**old_string:**
```
  <li id="n12">Daniel Gurney, <em>Record of the House of Gournay</em> (1848), pedigree p. 286: "Thomas Gournay, Esq. I. ... used a gurnard fish in pale for a crest." A gurnard is a spiny marine fish; the device is canting — a visual pun on the family surname. Source ID: <code>dg-rec-pt2</code>. <a class="citation-back" href="#ref-12">↩</a></li></ol>
```

**new_string:**
```
  <li id="n12">Daniel Gurney, <em>Record of the House of Gournay</em> (1848), pedigree p. 286: "Thomas Gournay, Esq. I. ... used a gurnard fish in pale for a crest." A gurnard is a spiny marine fish; the device is canting — a visual pun on the family surname. Source ID: <code>dg-rec-pt2</code>. <a class="citation-back" href="#ref-12">↩</a></li>
  <li id="n13">The Lancastrian-affinity continuity behind Thomas I's French service: his grandfather Edmund Gournay (G23) was a retained adviser within John of Gaunt's East Anglian affinity (Simon Walker, <em>The Lancastrian Affinity 1361–1399</em> (Oxford: Clarendon Press, 1990), note 19), and his uncle Sir John Gurney V served on Gaunt's 1394 Aquitaine expedition (AHRC <em>Soldier in Later Medieval England Online Database</em>, The National Archives C61/104, m. 7). Thomas's captains John Holland, earl of Huntingdon (a grandson of Gaunt through Elizabeth of Lancaster), and Thomas Beaufort, duke of Exeter (a son of Gaunt by Katherine Swynford), were both of the Lancastrian line. Source IDs: <code>walker-lancastrian-affinity-1361-1399</code>, <code>medievalsoldier-database</code>. <a class="citation-back" href="#ref-13">↩</a></li></ol>
```

---

## Phase-2 follow-up (record in chat after application, not in this file)

After applying: footnote sweep on both fact sheets (G22 n9/n10/n11 and G21 n13 anchors resolve, back-links point to first ref, visible labels match; Highlights carry no archive codes). Confirm the G22 Highlights at five bullets and the Narrative at five paragraphs. Prepend the `**Done:** YYYY-MM-DD HH:MM PT` stamp and move to `sources/intake/done/`. Queued next (`stub-v79.md`): the same story-weaving pass on G23, G24, and G29 narratives, plus the optional G29 Matthew service-row promotion.
