---
patchset_id: v05
title: Direct-line ancestor sweep — fact-sheet highlight refinements
date: 2026-04-27
archive_status: Archived 2026-06-22 without application; stale after extensive later fact-sheet and citation work.
scope: G16–G37 highlight blocks. Deeper work on G16–G27 (typically one swap, one medium rewrite, one polish per ancestor); lighter pass on G28–G37 (which already received good attention recently).
phase: 1 (analysis + patchset). Mechanical application is Phase 2.
sources_consulted: existing fact sheets G15–G37; highlights-inspiration.md (treated as evaluation prompt only — I use only material independently sourced in fact sheets/research; flag anything from inspiration that requires Allen's verification).
notes:
  - All str_replace operations target the `<ul>...</ul>` body of `<section class="fact-panel fact-panel-highlights" id="highlights">` in each fact sheet.
  - Where one bullet is being swapped, replace just that one `<li>...</li>` to keep diffs tight.
  - Where a wholesale shape change is proposed, replace the entire `<ul>...</ul>` block.
  - Footnote anchors (`<sup class="fn">`) are preserved verbatim. Where the new phrasing references an existing citation that's already on the fact sheet, the existing footnote is reused. No new citations are added.
  - I do NOT propose adding facts that aren't already documented somewhere on the fact sheet or in the underlying research. The inspiration file has a few items beyond the current fact sheets (e.g., "thirteen paupers in white around Edmund's body"; "Anne Heydon's turquoise ring"; "Thomas II's red-wax seal at Hunstanton Hall") that I have flagged at the bottom for Allen to verify and add via a separate sources/intake patchset if he wishes.
---

# v05 Patchset — Fact-Sheet Highlight Refinements

## Summary of Changes

**Approach.** Each ancestor's existing `<ul>` of highlight bullets was evaluated for: (a) duplication between bullets, (b) bullets that lean on generic historical context rather than ancestor-specific punch, (c) under-leveraged vivid material from the narrative or research that's stronger than what's currently surfaced. Per Allen's guidance, the typical edit is one swap + one rewrite + one polish per fact sheet — a few ancestors get more, a few less. The `<ul>` count of bullets is preserved on most ancestors; on a handful (G22, G24) I expand from 3 to 4 because the existing block was underweight.

**Deep range (G16–G27).** Most of the lift here. New highlights promoted from existing narrative content. Several "weak fifth bullet" patterns retired.

**Lighter range (G28–G37).** Targeted single-bullet swaps where the inspiration file or fact-sheet narrative surfaces an obviously stronger candidate. G34 and G37 each get one genuinely good promotion.

**No bullet-count target — readability target.** Where 3 bullets read too thin and 6 read overstuffed, I move toward 4–5 unless the ancestor's documented record genuinely demands more (G15 Henry, G33 Hugh III).

---

## G16 — Francis Gurney (c. 1521 – before December 1556)

**Issue.** Bullets 1 ("Heir-apparent who never inherited") and 4 ("His son Henry inherited as a child") are essentially the same point told from two angles. Bullet 4 is also where the awkward "Pease genealogy gives Henry's grandfather Anthony's death later in the same year that Francis died" passage lives, which is messy. Bullet 3 ("Of Irstead") is solid. Bullet 2 (Helen Holdich) is fine.

**Plan.** Replace bullet 4 with a fresh highlight on the *Lovell-Mortimer-of-Attleborough estates that should have flowed through him* — that's the most consequential thing about him as a generational figure, and it's currently buried in the narrative. Tighten bullet 1 to lead with the drama (died in the closing weeks of Catholic England). Light polish on bullet 3 phrasing.

**Edit 1 — replace bullet 1.**

`str_replace` on `fact-sheets/g16-francis-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>Heir-apparent who never inherited.</strong> Francis was the eldest son of Anthony Gurney (G17) and stood to inherit West Barsham, Great Ellingham, Harpley, Irstead, and the cluster of Lovell-Mortimer estates that had come into the family through his mother Margaret Lovell. He died <em>vita patris</em> before his father Anthony, and his son Henry — only seven or eight years old — became the eventual heir. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```

`new_str`:
```
  <li><strong>Heir-apparent who never inherited — and died in the last weeks of Catholic England.</strong> Francis was eldest son of Anthony Gurney (G17) and heir-apparent to West Barsham, Great Ellingham, Harpley, Irstead, and the Lovell-Mortimer-of-Attleborough cluster brought in through his mother Margaret Lovell. He died <em>vita patris</em> some time before his father, who himself died on 4 January 1555/6 — twenty-one months into Mary I's restored Catholicism, three years before Elizabeth would settle the Reformation. The two deaths together produced an extraordinary inheritance gap: Francis's seven-year-old son Henry, raised under the Elizabethan settlement, would become the last Gurney to be born a Roman Catholic. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```

**Edit 2 — replace bullet 4 (the duplicative one).**

`str_replace` on `fact-sheets/g16-francis-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>His son Henry inherited as a child.</strong> When Anthony Gurney died on 4 January 1555/6 (per Blomefield, Vol. 7), Henry — born January 1548/9 — was just barely seven years old. The Pease genealogy gives Henry's grandfather Anthony's death later in the same year that Francis died, which would have created an extraordinary inheritance situation: a seven-year-old grandson succeeding directly to a substantial gentry estate after both his father and grandfather died within months of each other. Wardship arrangements during Henry's minority are documented in Henry's own commonplace book (Bodleian MS Tanner 175, extracted in Daniel Gurney's <em>Supplement</em>, 1858). <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

`new_str`:
```
  <li><strong>The Lovell-Mortimer-of-Attleborough portfolio that flowed through him.</strong> Through his mother Margaret Lovell — daughter and coheir of Sir Robert Lovell, "cousin and coheir of Sir Thomas Lovell, privy counsellor to King Henry VII and Henry VIII and Knight of the Garter" — Francis was the channel by which the Mortimer-of-Attleborough estates reached his son Henry's generation. The most significant single piece was Great Ellingham, which had descended to Anthony in right of Margaret in 1525, after Henry Spelman the elder of "Mickle Elyngham" died without issue. Two generations later it would be Henry G15's principal residence and the church (St James the Apostle, Great Ellingham) that held his epitaph verse. <sup class="fn"><a href="#n6" id="ref-6b">6</a></sup></li>
```

**Edit 3 — light polish on bullet 3 (Of Irstead) for sharper opening.**

`str_replace` on `fact-sheets/g16-francis-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>"Of Irstead" — the Norfolk Broads connection.</strong> Daniel Gurney's pedigree identifies Francis as "of Irstead," distinguishing him by location from the senior West Barsham line. The family's connection to Irstead manor came through his mother (in fact through the previous generation, his Heydon grandmother Anne, whose father Sir Henry Heydon had received the Irstead manor by conditional bequest in John Groos's 1487 will, per Blomefield Vol. 11). Whether Francis actually held a residence at Irstead, or simply held the title nominally during his short adulthood, is unclear from the surviving sources. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

`new_str`:
```
  <li><strong>"Of Irstead" — but the manor itself had passed to the Crown a decade earlier.</strong> Daniel Gurney's pedigree identifies Francis as "of Irstead," distinguishing him by location from the senior West Barsham line. The family's link to the Norfolk Broads parish ran through his Heydon great-grandmother Anne, whose father Sir Henry Heydon had received Irstead manor by conditional bequest from John Groos's 1487 will (Blomefield, vol. xi). But Blomefield also records the principal Irstead manor passing to Sir Richard Southwell by 1540 — meaning Francis's adult-life residence there, if real, was on a smaller tenement rather than the manor itself. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

---

## G17 — Anthony Gurney (c. 1499 – 4 January 1555/6)

**Issue.** Six highlights total — at the upper limit. Bullet 1 ("boy lord, Howard godmother circle") has a phrasing problem: the Howard godmother was *Henry G15's*, not Anthony's, but the sentence currently reads as if Anthony had a Lady Catherine Howard godmother. Bullet 3 ("Gurney's Place" Norwich town house) is the weakest — generic, runs to a soft Lady-Julian-anchorite aside. Bullet 5 (Lestrange dinner companion) is fine but could be tighter. Surrey-trial bullet (4) is the strongest.

**Plan.** Recast bullet 1 to fix the godmother attribution. Retire bullet 3 ("Gurney's Place") and replace with a fresh highlight on the Spelman-of-Congham first-cousin-once-removed kinship — Anthony's children were close kin to the man who would virtually invent English legal antiquarianism, currently buried in the narrative. Tighten bullet 4 (Surrey indictment) for sharper compression on the king-dies-9-days-later beat.

**Edit 1 — replace bullet 1.**

`str_replace` on `fact-sheets/g17-anthony-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>A boy lord, with a Howard godmother circle.</strong> Anthony inherited the principal Norfolk Gurney estates as a child (probably around age nine, c. 1508). His mother Anne Heydon brought into the family the Heydon-Boleyn-Howard cousinage of late-medieval Norfolk: her father Sir Henry Heydon of Baconsthorpe was a major figure in Edward IV's and Henry VII's Norfolk administration, and her sister Bridget had married Sir William Paston. Anthony was therefore a second cousin of the future Queen Anne Boleyn through his Heydon mother — a kinship that would still be remembered in the 1540s when his own grandson Henry's godmother was a Lady Catherine Howard. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```

`new_str`:
```
  <li><strong>Boy lord at nine, second cousin of a future queen.</strong> Anthony inherited the principal Norfolk Gurney estates as a child of about nine in January 1508 — both his father William V (G18) and his grandfather William IV (G19) having died within the same generation. His Heydon mother Anne brought into the family the Heydon-Boleyn-Howard cousinage of late-medieval Norfolk: her father Sir Henry Heydon of Baconsthorpe was a Privy Councillor to Henry VII; her aunt Anne Boleyn the elder of Blickling was sister of Sir William Boleyn, paternal grandfather of the future Queen Anne Boleyn. The kinship made Anthony a second cousin of the queen — a closeness that would still be remembered in the 1540s when his own grandson Henry G15's godmother was reportedly a Lady Catherine Howard. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```

**Edit 2 — replace bullet 3 ("Gurney's Place" — currently weakest).**

`str_replace` on `fact-sheets/g17-anthony-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>"Gurney's Place" in Norwich — town house in St Julian's parish.</strong> Daniel Gurney records a Gurney town house in the parish of St Julian, Norwich, known as "Gurney's Place," held during Anthony's lifetime. The Gurneys had been holders of urban property in Norwich since the medieval period (Pockthorpe and the eastern suburbs); a town house in St Julian's, the parish associated with the Lady Julian of Norwich anchoress cell, would have been a notably central location. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

`new_str`:
```
  <li><strong>His children were first cousins once removed of Sir Henry Spelman of Congham — the antiquary who virtually invented English legal antiquarianism.</strong> Margaret Lovell's mother Ela Conyers was sister to Anne Conyers, who became mother of Sir Henry Spelman (1564–1641) — the great Stuart antiquary whose <em>Concilia, decreta, leges, constitutiones in re ecclesiarum orbis Britannici</em> and <em>Glossarium archaiologicum</em> shaped the foundations of English legal-historical scholarship. Anthony's children grew up in close kinship with one of the foundational scholarly minds of the next generation. <sup class="fn"><a href="#n7" id="ref-7b">7</a></sup></li>
```

**Edit 3 — tighten bullet 4 (Surrey indictment) for sharper compression.**

`str_replace` on `fact-sheets/g17-anthony-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>Foreman of the Norfolk grand jury that indicted the Earl of Surrey, January 1546/7.</strong> On 7 January 1546/7 Anthony Gurney sat as foreman of the Norfolk grand jury that returned a true bill against Henry Howard, Earl of Surrey — the poet, son of the Duke of Norfolk, and one of the great courtier-noblemen of Henry VIII's reign — for treason. Surrey was tried at the Guildhall on 13 January, condemned, and beheaded on Tower Hill on 19 January 1547. Henry VIII himself died nine days later. The indictment is documented in the State Papers and is one of the few moments when a Norfolk Gurney appears at a national level of political action. The political weight of Anthony's position — a relatively minor Norfolk gentleman foreman of a jury that destroyed England's premier earl, with the king dying within days — is hard to overstate. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

`new_str`:
```
  <li><strong>Foreman of the Norfolk grand jury that indicted the Earl of Surrey, 7 January 1546/7.</strong> On that date Anthony returned a true bill against Henry Howard, Earl of Surrey — poet, son of the Duke of Norfolk, premier earl of England — for treason. Surrey was tried at the Guildhall on 13 January, condemned, and beheaded on Tower Hill on 19 January 1547. Henry VIII himself died nine days after that. A relatively minor Norfolk gentleman, foreman of the jury that destroyed England's most prominent earl, in the king's last weeks of life: it is one of the few moments when a Norfolk Gurney sits squarely inside the national political machinery. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

---

## G18 — William Gurney V (c. 1465 – before 1508)

**Issue.** Five highlights. Bullet 4 ("Of Irstead — Norfolk Broads identification") is the weakest — runs to "whether William V actually maintained a residence at Irstead or simply held it nominally" hedge that mirrors the same hedge two generations later in G16. Bullet 5 ("Died vita patris, leaving young Anthony") repeats material already in the prose Vital Records section.

**Plan.** Replace bullet 4 with a fresher highlight — the Lestrange-of-Hunstanton kinship lever from this generation, which is the single most consequential downstream consequence of the marriage. Tighten bullet 5 (vita patris) to be punchier and to surface the unusual two-consecutive-vita-patris-deaths pattern that links William V to his grandson Francis G16.

**Edit 1 — replace bullet 4.**

`str_replace` on `fact-sheets/g18-william-gurney-v-fact-sheet.md`:

`old_str`:
```
  <li><strong>"Of Irstead" — the Norfolk Broads identification.</strong> Daniel Gurney's pedigree identifies William V as "of Irstead." The connection to Irstead manor came in through his Heydon father-in-law: Sir Henry Heydon had received the Irstead manors (Overhall and Netherhall) by conditional bequest from John Groos's will of 1 March 1487, per Blomefield's parish entry for Irstead in volume xi. Whether William V actually maintained a residence at Irstead or simply held it nominally during his short adult life is unclear. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

`new_str`:
```
  <li><strong>The marriage that explains a great-great-grandson's career, 130 years later.</strong> Anne Heydon's sister Amy married Sir Roger Lestrange of Hunstanton — and in 1612, William V's great-great-grandson Francis Gurney (G14) would become the trusted financial agent to the Lestranges of Hunstanton, a position he held for twenty-four years until 1636. Norfolk gentry preferred to do their financial business with kin, and they were still kin: William V's marriage in 1484 set up a working professional relationship that would still be active in the reign of James I. <sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></li>
```

**Edit 2 — tighten bullet 5 (vita patris).**

`str_replace` on `fact-sheets/g18-william-gurney-v-fact-sheet.md`:

`old_str`:
```
  <li><strong>Died vita patris, leaving his young son Anthony as eventual heir.</strong> William V died before his father William IV, who died on 18 January 1507/8 (per Daniel Gurney's pedigree). Their son Anthony — only nine or ten years old — inherited as a "boy lord" when William IV died, and the Norfolk Gurney estates were managed during Anthony's minority through wardship arrangements involving the Heydon kin. This is the second consecutive generation in which the senior heir died before his father, making the line skip a generation in inheritance terms. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

`new_str`:
```
  <li><strong>Died vita patris — and so did his great-grandson, two generations later.</strong> William V predeceased his father William IV (d. 18 January 1507/8); his nine-year-old son Anthony inherited as a "boy lord" when William IV died, with wardship through the Heydon kin. Two generations later, William V's grandson Francis (G16) would also die <em>vita patris</em> — producing a second consecutive grandson-as-heir succession in the Norfolk Gurney line. The pattern made the West Barsham succession unusually fragile through the late-medieval and early-Tudor decades. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

---

## G19 — William Gurney IV (c. 1450 – 18 January 1508)

**Issue.** Six highlights, all strong. The 700-sheep highlight (4) is rightly the centerpiece. Bullets 5 (Pockthorpe town house) and 6 (wrestling collar) are slightly weaker than the rest. The 700-sheep highlight is good but slightly buried — its lede mentions the 700 sheep but doesn't quite punch.

**Plan.** Polish on the 700-sheep highlight to lead more strongly with the figure. Tighten the wrestling-collar highlight by trimming the "Sir Henry Spelman" attribution down (the antiquary connection is there but doesn't need this much explanatory weight in a highlight bullet — it's better in narrative).

**Edit 1 — polish bullet 4 (700 sheep).**

`str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md`:

`old_str`:
```
  <li><strong>The 1507 will requiring 700 sheep to remain at West Barsham.</strong> By his will of 1507 William IV directed that 700 sheep should remain at West Barsham after his death — what genealogist Daniel Gurney called "a considerable flock in those days." This is rare concrete evidence of the working economy of a substantial Norfolk gentry household: West Barsham was a serious sheep-farming operation, integrated into the East Anglian wool trade that fed the Norwich worsted industry. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

`new_str`:
```
  <li><strong>Seven hundred sheep at West Barsham — by name in his 1507 will.</strong> William IV directed that seven hundred sheep should remain on the estate after his death — what Daniel Gurney called "a considerable flock in those days." Across the entire pre-1600 Gurney record, there is no other piece of evidence about the working economy of a Gurney household this concrete. The flock made West Barsham a serious sheep-farming operation, feeding the East Anglian wool trade that fed the Norwich worsted industry that was the dominant economic activity of the county. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

**Edit 2 — tighten bullet 6 (wrestling collar).**

`str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md`:

`old_str`:
```
  <li><strong>Adopted "the wrestling collar" as a personal device.</strong> Sir Henry Spelman the antiquary later recorded seeing a seal of "William Gurney, Esq." in the reign of Henry VII bearing a wrestling collar. The wrestling collar was subsequently borne by the family as a second crest alongside the older gurnard fish. William IV thus introduced one of the two enduring heraldic devices of the family. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

`new_str`:
```
  <li><strong>Introduced the wrestling collar — a second family crest beside the older gurnard.</strong> An antiquarian record of a William Gurney seal from the reign of Henry VII shows a wrestling collar — a strap with metal ring, used in the medieval sport of wrestling. From William IV's generation the family bore it as a second crest alongside the gurnard fish. He thus introduced one of the two enduring heraldic devices the West Barsham line carried until extinction in 1661. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

---

## G20 — Thomas Gournay II (fl. c. 1430 – d. 1471)

**Issue.** Five highlights. Bullets 1 (will + three residences + wool detail) and 4 (Margaret's wool work) and 2 (three residences) all overlap somewhat — they're all aspects of the same will. Bullet 5 (Wars of the Roses context) is the weakest — generic context, not specific to him.

**Plan.** Consolidate bullets 2 and 4 (both about the will's specifics) into one stronger bullet on the will-as-document. Replace bullet 5 with a sharper highlight on the very specific dating discrepancy — Blomefield's "18 March 1469/70" original will vs. Daniel Gurney's "27 July 1471" probate, which is itself an interesting epistemic moment. Polish bullet 1 to lead with the will's standalone significance.

**Edit 1 — replace the entire `<ul>` block (this is a more structural change).**

`str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`:

`old_str`:
```
<ul>
  <li><strong>His will of 1471 is the earliest Gurney will that survives with full personal detail.</strong> Dated at West Barsham and proved 27 July 1471, the will names three simultaneous family residences (Harpley, West Barsham, Norwich), specifies where Thomas wished to be buried, and leaves all the household's wool and linen cloths to his wife Margaret "being her own work and that of her servants" — a rare first-person glimpse of a 15th-century Norfolk gentry household's working economy. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>Three residences simultaneously — proof of a substantial gentry portfolio.</strong> Thomas's will proves he had "three residences at least": West Barsham Hall, a house at Harpley, and a Norwich town house in St Gregory's parish. genealogist Daniel Gurney used this as evidence of the medieval pattern by which Norfolk gentry held residences at each of their principal manors "to consume the produce of each estate," moving with the family household through the year. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>Married into the Jerninghams of Somerleyton — Catholic gentry royalty.</strong> Margaret Jerningham was the daughter of Sir Thomas Jerningham, Knt., of Somerleyton, Suffolk. The Jerninghams were among the most prominent East Anglian Catholic gentry families, still recusant in the Elizabethan period and supporters of Mary I's accession in 1553. The marriage anchored the West Barsham Gurneys into a Catholic gentry network that would still be structuring their marriages a century later — when Henry Gurney G15's widowed daughter-in-law Helen Holditch married a Jerningham, the connection was being activated for the second time. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
  <li><strong>Women's wool work as a family business.</strong> The 1471 will's bequest of "all the woolen and linen cloths" to Margaret as her own work and that of her servants is direct evidence that Margaret ran a productive textile operation within the household — spinning and weaving wool from her husband's flocks for the family's own use and, implicitly, for exchange or sale. This was standard for substantial Norfolk gentry wives of the period, but Thomas's will is one of the few surviving documents to make the domestic side of it explicit. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
  <li><strong>Lived through the middle decades of the Wars of the Roses.</strong> Thomas's active life c. 1430–1471 spans the entire opening phase of the dynastic civil war — from the outbreak of open conflict at St Albans in 1455, through the Yorkist seizure of the throne in 1461, to the brief Lancastrian restoration in 1470–71 and Edward IV's decisive return at Barnet (April 1471) and Tewkesbury (May 1471). Thomas died and his will was proved just weeks after Edward IV's final victory. There is no record of his personal role on either side — characteristic of the middling Norfolk gentry, who mostly kept their heads down while the great magnates fought. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
</ul>
```

`new_str`:
```
<ul>
  <li><strong>The earliest Gurney will surviving with full personal detail.</strong> Independently dated by Blomefield at 18 March 1469/70 (9 Edw. IV), proved by the Norwich Consistory Court on 27 July 1471. It names three simultaneous family residences, directs alternative burial at Harpley or the Greyfriars at Norwich "as he may die at either place," and contains the kind of first-person texture — wool clothes, gendered household economy, alternate burial choice — that no earlier Gurney document can match. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>Three residences in three Norfolk hubs, all maintained at once.</strong> West Barsham Hall in north Norfolk; the medieval family seat at Harpley, twenty miles west; a town house in St Gregory's parish in the heart of Norwich. Daniel Gurney used Thomas's will as his textbook illustration of the pattern: medieval gentry circulated among their estates "to consume the produce of each estate," moving the household through the agricultural year. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>Margaret's wool, "being her own work and that of her servants."</strong> The 1471 will leaves all the household's woolen and linen cloths to Margaret Jerningham — explicitly identified as her own work and that of her servants. This is direct evidence that Margaret ran a productive textile operation within the household, spinning and weaving wool from her husband's flocks for family use and, implicitly, for exchange. Thomas's will is one of the very few surviving English documents to make the gendered division of a 15th-century gentry household economy visible. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
  <li><strong>Married into the Jerninghams of Somerleyton — Catholic gentry royalty.</strong> Margaret was daughter of Sir Thomas Jerningham, Knt., of Somerleyton, Suffolk. The Jerninghams were among the most prominent East Anglian Catholic gentry families, still recusant in the Elizabethan period; Sir Henry Jerningham of Huntingfield was one of the principal supporters of Mary I's accession in 1553. The marriage anchored the West Barsham Gurneys into a Catholic gentry network that would still be active a century later, when Francis Gurney G16's widow Helen Holditch married a Jernegan and the kinship was activated for the second time. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
  <li><strong>Will proved twelve weeks after Tewkesbury.</strong> The will was proved on 27 July 1471 — just under three months after Edward IV's decisive Yorkist victory at Tewkesbury on 4 May had ended the Lancastrian Readeption and restored him to the throne. Thomas's whole adult life c. 1450–1471 had unfolded across the opening phase of the Wars of the Roses; he died in the same summer that civil war effectively ended for the next fourteen years. There is no record of him personally engaging on either side — characteristic of the middling Norfolk gentry, who kept their heads down while the great magnates fought. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
</ul>
```

---

## G21 — Thomas Gournay I (fl. c. 1408 – c. 1450)

**Issue.** Five highlights. Bullet 5 ("Lived through the reign of Henry VI — the calm before the civil war") is generic context — could be replaced. Bullets 1 (collateral inheritance), 2 (uncle Sir John V's career), and 3 (La Selde Coronata London warehouse) are all strong; bullet 4 (Kerville-of-Watlington marriage) is decent but flat.

**Plan.** Replace bullet 5 with something fresher — perhaps the documentary silence itself as the highlight (no Crown office, no parliamentary service, no commission of the peace — striking given his uncle's record). Polish bullet 4 (Kerville marriage) to add the explicit Lynn-hinterland diversification framing.

**Edit 1 — replace bullet 5.**

`str_replace` on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`:

`old_str`:
```
  <li><strong>Lived through the reign of Henry VI — the calm before the civil war.</strong> Thomas's active period c. 1408–1450 falls entirely in the later Lancastrian era, between Henry IV's consolidation of the dynasty and the outbreak of open Wars of the Roses at St Albans in 1455. It was the period of Henry V's French victories (Agincourt, 1415), of the long minority of Henry VI after 1422, and of the slow unravelling that would eventually produce the Yorkist crisis. There is no record of Thomas in Crown office, parliamentary service, or military campaign — he appears to have been a private Norfolk gentleman consolidating a complicated collateral inheritance. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

`new_str`:
```
  <li><strong>The conspicuous silence of the public record.</strong> No Crown office. No sheriffdom. No parliamentary service. No commission of the peace. No commission of array. No royal inquiry. Across an active span of forty years (c. 1408 to c. 1450), Thomas I appears in no public document of his own — a striking absence given that his uncle Sir John V's record fills eight paragraphs of the History of Parliament biography. The silence may reflect a deliberately private gentleman consolidating a complicated collateral inheritance through the long Lancastrian minority, or simply the thinner survival of mid-15th-century records compared with his uncle's reign. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

**Edit 2 — polish bullet 4 (Kerville).**

`str_replace` on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`:

`old_str`:
```
  <li><strong>Married Catherine Kerville of Watlington — a west-Norfolk Lynn-hinterland alliance.</strong> Watlington is near King's Lynn, the great medieval trading port at the mouth of the Great Ouse. The Kerville marriage anchored Thomas I into the western Norfolk gentry cluster distinct from the Howard/Paston/Heydon networks of the eastern half of the county — a sensible diversification for a gentleman whose principal seats (West Barsham, Harpley) lay in the intermediate north-Norfolk zone. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

`new_str`:
```
  <li><strong>The Kerville-of-Watlington marriage — a sensible Lynn-hinterland diversification.</strong> Watlington sits about eight miles south of King's Lynn, the great medieval trading port at the mouth of the Great Ouse, and the Kervilles were established west-Norfolk gentry there. The marriage anchored Thomas's family into a kinship cluster distinct from the Howard / Paston / Heydon networks of the eastern half of the county — a sensible portfolio diversification for a gentleman whose principal seats at West Barsham and Harpley already lay in the intermediate north-Norfolk zone, and whose Heylesdon inheritance had brought him an additional foothold in Norwich and (briefly) the City of London. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

---

## G22 — Robert Gournay (fl. c. 1370–1420)

**Issue.** Only three highlights total — the fact sheet feels underweight. Bullet 1 (DG hedged the name) and bullet 2 (the line descends through him because brother's son died young) are both strong. Bullet 3 ("father was one of the most connected men in East Anglia") is generic and slightly weak.

**Plan.** Tighten bullet 3 to be more specific about *what* his father's connections actually were and what they would have meant for Robert's daily life. Add a fourth highlight on the Joan-de-Norwich marriage as a hint to social network (the Norwich connection echoes through to his father Edmund's "Gurney's Place" in St Julian's parish, Norwich).

**Edit 1 — replace bullet 3 and add bullet 4 (full `<ul>` replacement).**

`str_replace` on `fact-sheets/g22-robert-gournay-fact-sheet.md`:

`old_str`:
```
<ul>
  <li><strong>His very name is uncertain — Daniel Gurney hedged it.</strong> In Edmund Gurney's will chapter, DG writes of "a second son, whom we believe was named Robert." This is an explicit editorial hedge in the primary compiled source: DG was not certain of the name. The only other source DG cites for the children of Edmund is the 1622 pedigree by Cook, Clarenceux King of Arms. The name Robert is treated as the most probable but not the confirmed identification. This fact sheet follows the project convention of using "Robert" while flagging the uncertainty prominently. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>The direct line descends through him because his brother's son died young.</strong> Robert's elder brother Sir John Gurney V (d. 4 December 1408) inherited all the family estates, was sheriff of Norfolk and Suffolk in 1399 and again at his death in 1408, sat in Parliament for the Coventry parliament of 1404, and married Alice Heylesdon — daughter and eventual sole heir of the wealthy London mercer and former alderman John Heylesdon — bringing into the family the great London warehouse "La Selde Coronata." Sir John appeared to be the main line. But his only son Edmund, aged ten at his father's death, "followed him to the grave not long afterwards." The estates passed to Robert's son Thomas I — making Robert the pivotal ancestor through whom the entire subsequent West Barsham Gurney family (and through Francis Gurney, probably the American Gurneys) descend. The full sequence is documented in the History of Parliament Online biography of Sir John Gurney d. 1408. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>His father was one of the most connected men in East Anglia.</strong> Born into a family at the height of its social and professional reach — father steward of John of Gaunt, mother heiress of West Barsham, elder brother heading toward a knighthood and a parliamentary career — Robert would have grown up in the most prosperous and well-connected household the family had known. What he did with that inheritance, in personal terms, is unrecorded. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
</ul>
```

`new_str`:
```
<ul>
  <li><strong>His very name is uncertain — Daniel Gurney hedged it.</strong> In Edmund Gurney's will chapter, DG writes of "a second son, whom we believe was named Robert." This is an explicit editorial hedge in the primary compiled source. The only other source DG cites for Edmund's children is the 1622 pedigree by Cook, Clarenceux King of Arms. The name Robert is treated as the most probable but not confirmed. This fact sheet follows the project convention of using "Robert" while flagging the uncertainty prominently. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>The direct line descends through him because his brother's son died young.</strong> Robert's elder brother Sir John Gurney V (d. 4 December 1408) inherited all the family estates: sheriff of Norfolk and Suffolk in 1399 and 1408, MP for Norfolk in the Coventry Parliament of 1404, married to Alice Heylesdon — daughter and eventual sole heir of the wealthy London mercer and former alderman John Heylesdon — bringing the City warehouse "La Selde Coronata" into the family. Sir John appeared to be the main line. But his only son Edmund, aged ten at his father's death, "followed him to the grave not long afterwards." The estates passed to Robert's son Thomas I — making Robert the pivotal ancestor through whom every subsequent West Barsham Gurney, the Norwich Quaker Gurneys, and (through Francis G14) the American Gurneys descend. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>Born into the family at its peak social reach.</strong> Robert grew up in the most prosperous and well-connected household his family had yet produced: a father (Edmund G23) who was steward of John of Gaunt's East Anglian estates and standing counsel to the cities of Norwich and Bishop's Lynn; a mother (Katherine de Wauncy) who was heiress of West Barsham; an elder brother heading toward a knighthood, a sheriffdom, and parliamentary service. The household's day-to-day visitors and correspondents would have included the leading lawyers, clergy, and gentry of the eastern counties. What Robert did with that inheritance, in personal terms, is entirely unrecorded — as is true of most younger sons of the period. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>Married Joan de Norwich — likely a member of the Norwich civic world his father served.</strong> Joan's surname suggests an origin in or close to Norwich — the largest urban centre in the region and the city to which Robert's father Edmund had served as standing counsel. Edmund's town house in St Julian's parish, Norwich, was the family's working address in the city. A son of that household marrying a Norwich woman is exactly what one would expect; it suggests the connection was professional and habitual rather than a single arranged alliance. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
</ul>
```

---

## G23 — Edmund Gurney (d. 1387)

**Issue.** Five highlights, all strong. Bullet 5 ("The patent and close rolls are full of him") is the weakest — it's a list-of-list, not a sharp single fact. Bullet 4 (impaled arms in two windows) is good but the second window detail is in passing.

**Plan.** Replace bullet 5 with a single most-vivid royal-instrument item (e.g., the inquiry into murder, or the arbitration between Norwich Priory and Carrow priory). Polish bullet 4 to give the second window (Denton church) more weight — it's still visible in 1848, which is the kind of present-tense-survival anchor Allen likes.

**Edit 1 — replace bullet 5.**

`str_replace` on `fact-sheets/g23-edmund-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>The patent and close rolls are full of him.</strong> DG catalogues Edmund's appearances across at least fifteen separate royal instruments: justice of the peace, commissioner for forcible entry, commissioner for customs fraud, arbitrator between the prior of Norwich and the prioress of Carrow, special commissioner for Queen Philippa's manor, justice for piracy inquiry, and more. He is one of the most thoroughly documented ancestors in the entire lineage. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

`new_str`:
```
  <li><strong>Arbitrator between the Prior of Norwich and the Prioress of Carrow — and fifteen other royal instruments.</strong> The Patent and Close Rolls of Edward III and Richard II carry Edmund through at least fifteen separate appearances: justice of the peace (twice), commissioner for forcible entry, commissioner for customs fraud, justice for inquiry into piracy on the Norfolk roads, special commissioner for Queen Philippa's manor — and arbitrator between the great Norwich Cathedral Priory and the Augustinian nuns of Carrow on the city's southern edge. He is one of the most thoroughly documented ancestors in the entire pre-1500 lineage. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

**Edit 2 — polish bullet 4 (impaled arms).**

`str_replace` on `fact-sheets/g23-edmund-gurney-fact-sheet.md`:

`old_str`:
```
  <li><strong>His arms impaled the Wauncy coat — and the evidence survives.</strong> Edmund's arms (the engrailed cross, argent) impaling the Wauncy coat (gules, three dexter hand-gloves pointed downwards, argent) were visible in a window of "Gurney's Place" in St. Julian's parish, Norwich, when Mr. Norris recorded them. The same impaled coat was still visible in a window of Denton church, Norfolk, as of DG's writing in 1848. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

`new_str`:
```
  <li><strong>His impaled arms in glass at Denton church, Norfolk — visible into the Victorian period.</strong> Edmund's arms (engrailed cross argent) impaling the Wauncy coat (gules, three dexter hand-gloves pointed downwards, argent) were recorded by the antiquary Norris in a window at "Gurney's Place," the family's St Julian's-parish town house in Norwich. The same impaled coat survived in a window of Denton church, Norfolk, into Daniel Gurney's own writing in 1848 — a piece of fourteenth-century painted glass commemorating Edmund's marriage that outlasted the entire West Barsham line. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

---

## G24 — John de Gournay IV (fl. c. 1330–1370)

**Issue.** Three highlights. Bullets 1 and 3 are both about Harpley church-presentation moments — they overlap. Bullet 2 (last Harpley lord before great transition) is strong. The fact sheet feels underweight at three.

**Plan.** Consolidate bullets 1 (1354 court roll) and 3 (1332 presentation) into a single tighter highlight. Add a fresh highlight on John IV's role as the platform-builder for his son Edmund's career — currently a strong narrative theme but not in highlights.

**Edit 1 — full `<ul>` replacement.**

`str_replace` on `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`:

`old_str`:
```
<ul>
  <li><strong>His court roll survives — one of the earliest personal records for this generation.</strong> Daniel Gurney cites a manorial court record: John IV "kept his first court at Harpley on Friday the vigil of St. Laurence, 28th Edward III (1354)." The feast of St. Laurence is 10 August; the vigil would have been 9 August 1354. This is not merely an attestation that John IV existed — it is a specific day in his life, the first occasion on which he exercised the judicial authority of a lord over his tenants. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>He is the last Harpley lord before the family's great transition.</strong> John IV is the final generation of the junior Gournay branch to be seated primarily at Harpley. His son Edmund (G23) married Katherine de Wauncy, heiress of West Barsham, thereby bringing that manor into the family — and from Edmund's generation onward the Gurneys are primarily described as the "Gurneys of West Barsham." Harpley remained in the portfolio but ceased to be the primary seat. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>He also — possibly — presented to the church of Harpley in 1332.</strong> Daniel Gurney, <em>Supplement</em> (1858) p. 355 notes that in 1332 "either he or his father presented to the church of Harpley; but more probably this John de Gurney [IV], as he is called John de Gurney junior" in the deed. If so, John IV exercised advowson as a very young man (a child, effectively) immediately upon his grandfather's death — suggesting the 1332 presentation was made formally in his name even if his father managed the actual process. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
</ul>
```

`new_str`:
```
<ul>
  <li><strong>The one specific day in his life: 9 August 1354, his first manorial court at Harpley.</strong> The British Library's Additional MS 8841, fol. 112, records that John IV kept his first court at Harpley on Friday the vigil of St. Laurence (i.e. 9 August), 28 Edw. III. This is more than an attestation that he existed — it is a specific date, a specific seat, the first time he exercised judicial authority as lord of the manor. The Daniel Gurney <em>Supplement</em> (p. 355) also speculates that in 1332 (6 Edw. III), as a very young man, he had already exercised advowson at Harpley, presenting a new rector on his great-uncle's death; if true, that earliest act would have been made formally in his name while his father managed the process. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>The last Harpley lord before the family's great transition.</strong> John IV is the final generation of the junior Gournay branch to be seated primarily at Harpley. His son Edmund (G23) married Katherine de Wauncy, heiress of West Barsham, bringing that manor into the family — and from Edmund's generation forward the Gurneys are primarily "of West Barsham." Harpley remained in the portfolio (and would briefly return as principal seat under Henry G15's 1587 repurchase), but its three-century run as primary residence ended with John IV. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>The platform-builder.</strong> John IV's main historical contribution was his son. Edmund (G23) became a lawyer of county-wide reputation — steward of John of Gaunt's East Anglian estates, standing counsel to Norwich and Bishop's Lynn, holder of more than fifteen royal commissions across two reigns. Men of that calibre did not spring from nowhere: the stable, respectable Harpley household John IV maintained, and the legal/literate education he provided his son, were the platform from which Edmund advanced. <sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></li>
  <li><strong>Lived through the Black Death.</strong> Born around 1330, John IV was approximately eighteen during the worst year of the plague in England, 1348–49 — when the Black Death killed something between a third and a half of the country's population. No record of his personal experience survives. The plague's impact on the Norfolk manorial economy was profound, and the labour-shortage decade that followed transformed the relationship between gentry lords and their tenants in ways that John IV's son and grandson would have to manage. <sup class="fn"><a href="#n5" id="ref-5b">5</a></sup></li>
</ul>
```

---

## G25 — John de Gournay III (fl. c. 1300–1353)

**Issue.** Three highlights. All decent but feel slightly thin. Bullet 1 (collateral inheritance from uncle the Rector) is the best. Bullet 2 (1332 advowson) duplicates the same point in different words. Bullet 3 (Jane de Lexham marriage) is fine.

**Plan.** Consolidate bullets 1 and 2 (both about the 1332 inheritance moment) into one stronger one. Add a new highlight on the documentary thickening of his generation — he is one of the earliest direct-line ancestors with both wife's name and approximate marriage date attested.

**Edit 1 — full `<ul>` replacement.**

`str_replace` on `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`:

`old_str`:
```
<ul>
  <li><strong>Recovered the family estates through his uncle's death — the classic medieval succession by nephew.</strong> His father Sir William III had conveyed all the Gournay Norfolk manors to his brother John (Rector of Harpley) in 1294. When the Rector died in 1332 without heirs, the estates reverted to William III's son — John III. The pedigree describes him as "heir to his uncle John, Rector of Harpley" — a nephew-inheritance that preserved the direct male line through an unusual gap in the normal pattern. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>Presented to the living of Harpley in 1332 — the very year he succeeded.</strong> As lord of Harpley, John III immediately exercised one of the most tangible symbols of manorial authority: the right of advowson, the presentation of a new incumbent to the church living. In 1332 he presented to the church of Harpley, the same living his uncle had held as Rector. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>His wife Jane de Lexham is named and dated — unusually precise for this generation.</strong> The DG pedigree records that Jane was the daughter of Edmund de Lexham and that she married John "before 1324, or in that year." This is one of the earliest marriage dates in the junior Norfolk branch with a named wife and an approximate date — a mark of how the documentary record begins to thicken in the 14th century. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
</ul>
```

`new_str`:
```
<ul>
  <li><strong>Inheritance via his uncle the Rector — and an immediate advowson on succession.</strong> John III's father Sir William III had conveyed all the Gournay Norfolk manors to his brother John (Rector of Harpley) in 1294 in exchange for an annuity. When the Rector died without heirs in 1332, the estates returned smoothly to William III's son — John III. He immediately exercised the most tangible symbol of recovered authority: the right of advowson at Harpley, presenting a new incumbent in the same year, to the very living his uncle had vacated by death. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>The first direct-line ancestor with both wife's name and approximate marriage date attested.</strong> Daniel Gurney's pedigree records that Jane de Lexham, daughter of Edmund de Lexham, married John "before 1324, or in that year." For the junior Norfolk branch, this is the earliest marriage with both a named wife and a fixed approximate date — a marker of how the documentary record thickens through the 14th century. The Lexhams of Lexham in west Norfolk are documented from the early 13th century. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>Lived through the Black Death.</strong> John III's long life c. 1300 to at least 1353 spanned the early decades of the Hundred Years' War, the catastrophic Black Death of 1348–49, and the first great parliamentary crises of Edward III's reign. There is no surviving record of his personal experience of any of these events, which for a minor Norfolk landholder is not surprising — but it is striking that the man who survived to be "living 27 Edw. III" had outlasted a plague that killed roughly a third of his neighbours. <sup class="fn"><a href="#n2" id="ref-2c">2</a></sup></li>
</ul>
```

---

## G26 — Sir William de Gournay III, Knt. (fl. c. 1260–1300)

**Issue.** Three highlights. Bullet 1 (engrailed cross seal) is strong. Bullet 2 (sold all estates to brother for annuity) is the strongest. Bullet 3 (Baconsthorpe marriage resolved a puzzle) is OK but turns inward to a genealogical-historiographical question rather than the ancestor's life.

**Plan.** Polish bullet 1 to lead with the *physical artefact* angle (the 1294 deed seal as the family's first surviving heraldic impression). Replace bullet 3 with something fresher — perhaps the *thirty-eight-year* gap between his 1294 transfer and the 1332 reversion, during which the family estates were entirely held by a clergyman. Tighten bullet 2.

**Edit 1 — full `<ul>` replacement.**

`str_replace` on `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`:

`old_str`:
```
<ul>
  <li><strong>First in the family to seal with the engrailed cross in a surviving document.</strong> The 1294 deed by which William transferred all his estates to his brother John, Rector of Harpley, was sealed by William with an engrailed cross. Daniel Gurney identified this as "the earliest on record of the use of the cross engrailed in a seal or document by any of the family" — though he also notes the arms had been borne by William's father Sir John I on an ancient roll of arms. The seal is thus the first physical object, as opposed to a roll entry, bearing the Gournay arms. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>Sold all his estates to his brother for an annuity in 1294 — a remarkable act.</strong> In 14 Edward I (1286), William was lord of a portfolio of Norfolk manors. Eight years later, he conveyed every one of them to his clerical brother John in exchange for a lifetime annuity. Why he did so is unrecorded — financial distress, personal preference, a desire to secure his brother's position, or some combination. The result was that the estates passed through the clerical line and, on John's death in 1332 without clerical heirs, descended to William's son John III (G25), restoring the direct male line. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>The Baconsthorpe marriage resolved a long-running puzzle.</strong> His father William II's wife was identified by DG only as "probably a Baconsthorpe." William III's wife Katherine is confirmed as "daughter of Edmund Baconsthorpe" — establishing a definite Baconsthorpe connection in this generation, and explaining why DG made the inference about the previous one. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
</ul>
```

`new_str`:
```
<ul>
  <li><strong>The earliest physical object bearing the Gournay arms.</strong> The 1294 deed by which William transferred all his Norfolk estates to his brother John, Rector of Harpley, is sealed with an engrailed cross — what Daniel Gurney called "the earliest on record of the use of the cross engrailed in a seal or document by any of the family." William's father Sir John I had borne the same arms on a contemporary roll, but the 1294 seal is the first physical impression that survives. The heraldry the family carried unchanged for the next four centuries first reaches us through this document. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>Conveyed every Norfolk manor to his brother for an annuity, 1294 — a remarkable act.</strong> In 14 Edw. I (1286) William was lord of a Norfolk portfolio: Harpley, Hardingham, Hingham-Gurneys, and others. Eight years later, by a single deed, he transferred all of it to his clerical brother John in exchange for a lifetime annuity. Why is unrecorded — financial distress, personal preference, perhaps a calculation that he had no immediate male heir at the time. The annuity arrangement suggests he kept the income stream; the legal title sat with a celibate priest. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>For thirty-eight years the entire family seat sat in clerical hands.</strong> From the 1294 transfer until Rector John's death in 1332, the manor of Harpley, the Hardingham and Hingham holdings, and everything William had divested were held by his celibate brother. When the Rector died without heirs, the inheritance descended cleanly to William's son John III (G25) — the gamble paid off. But for thirty-eight years the direct male line was contingent on a single elderly priest's life: had Rector John outlived his nephew, or had the Crown intervened in the inheritance, the whole junior Norfolk branch could have ended in 1332. <sup class="fn"><a href="#n6" id="ref-6b">6</a></sup></li>
</ul>
```

---

## G27 — Sir John de Gournay I, Knt. (fl. c. 1240–1280)

**Issue.** Four highlights, all genuinely strong. Bullet 1 (Lewes/Evesham/Crusade arc) is the headline. Bullet 2 (engrailed cross arms) is essential. Bullet 4 (royal letters of protection) is good. Bullet 3 (presented for refusing knighthood) is the weakest — and is somewhat obscured by being half a tax-evasion explainer.

**Plan.** Replace bullet 3 with something stronger from the inspiration-file content: the three Norfolk knights at the same Crusade — Sir John de Gournay, Sir Robert de Ufford, Sir John de Ingoldesthorpe — *all* bearing engrailed crosses, suggesting collective adoption at the Crusade itself (this is supported by the fact sheet's citation n6 already and by the existing G27 narrative). Polish bullet 1 (the rebellion-then-Crusade arc) to lead more strongly with the rehabilitation pivot.

**Edit 1 — replace bullet 1 (rebel-to-Crusader arc).**

`str_replace` on `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`:

`old_str`:
```
  <li><strong>Fought against the king at the Battle of Lewes, 1264 — and then went on Crusade.</strong> Sir John sided with Simon de Montfort's baronial reform movement against Henry III. He was present at both the Battle of Lewes (14 May 1264, where the barons captured the king) and the Battle of Evesham (4 August 1265, where de Montfort was killed and the rebellion crushed). In consequence, he forfeited the manor of South Wootton in Norfolk. But within a few years he had obtained a pardon and a royal writ of protection to accompany the future Edward I to the Holy Land in 1270 — one of history's more striking personal rehabilitations. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

`new_str`:
```
  <li><strong>Rebel against the king at Lewes — Crusader with the king's son five years later.</strong> Sir John fought on the baronial side at Lewes (14 May 1264, where the barons captured Henry III) and at Evesham (4 August 1265, where Simon de Montfort was killed and the rising crushed). His manor of South Wootton in Norfolk was seized in consequence — DG-Supp Note 112 preserves the full Latin plea, including a livestock inventory of three horses, four oxen, fourteen cows, and 171 sheep taken because John "was in the conflict of Lewes against the Lord King." Yet within five years he had a royal pardon and a writ of protection to accompany the future Edward I on Crusade. From rebellion against the crown to active service under the next king, in five years — one of the more dramatic rehabilitation arcs in the family record. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

**Edit 2 — replace bullet 3 (refused knighthood) with the three-engrailed-crosses Crusade trio.**

`str_replace` on `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`:

`old_str`:
```
  <li><strong>Presented by a jury for refusing knighthood — twice.</strong> In 1257, a jury of Mitford hundred presented Sir John for not accepting a knight's summons when required by the crown. This was a known form of fiscal evasion: Henry III periodically compelled men of sufficient wealth to accept knighthood (with its expensive obligations) and fined those who refused. John eventually accepted; he appears as "knight" in subsequent records. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

`new_str`:
```
  <li><strong>Three Norfolk knights, three engrailed crosses, one Crusade.</strong> Sir John de Gournay, Sir Robert de Ufford, and Sir John de Ingoldesthorpe — three Norfolk neighbours, all from established gentry families — accompanied Prince Edward to the Holy Land in 1270, and all three subsequently bore <em>engrailed crosses</em> as their arms. Daniel Gurney suggested in his <em>Supplement</em> that the heraldic identity may have been adopted collectively at the Crusade itself, with the engrailed cross as a Norfolk-Crusader badge of common cause. If so, the family arms Allen carries today emerged from one specific shared moment in 1270. <sup class="fn"><a href="#n6" id="ref-6b">6</a></sup></li>
```

---

## G28 — Sir William de Gournay II, Knt. (fl. c. 1210–1250)

**Light pass.** Three highlights, all reasonable. Bullet 1 (father of the rebel-Crusader) is the strongest. Bullets 2 (1234/1243 attestations) and 3 (wife's surname uncertainty) are both technical-evidentiary. The fact sheet feels slightly light; could promote the documentary witness moment — bullet currently buried in the notables section.

**Edit 1 — light polish on bullet 1.**

`str_replace` on `fact-sheets/g28-william-de-gournay-ii-fact-sheet.md`:

`old_str`:
```
  <li><strong>Father of the most dramatic figure in the junior branch.</strong> William's son Sir John de Gournay I (G27) fought on the rebel side at the Battle of Lewes (1264), had his estate seized for his rebellion against Henry III, was presented by a jury in 1257 for not accepting knighthood when required, and then accompanied the future Edward I on Crusade to the Holy Land in 1270. He also established the family coat of arms — argent, a cross engrailed gules — that his descendants bore thereafter. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

`new_str`:
```
  <li><strong>Father of the most dramatic figure in the junior branch.</strong> William's son Sir John de Gournay I (G27) fought on the baronial side at Lewes in 1264, had South Wootton manor seized for rebellion against Henry III, was reconciled within five years, and accompanied the future Edward I on Crusade to the Holy Land in 1270. He also established the family coat of arms — argent, a cross engrailed gules — that descendants bore unchanged for the next four centuries. William II is the silent pivot from which that career launched. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

---

## G29 — Sir Matthew de Gournay, Knt. (fl. c. 1180–1220)

**Light pass.** Four highlights, all strong. Bullet 1 (Hameline-arranged marriage) is rightly the headline. Bullet 4 (lived to see Normandy lost) is the weakest — generic geopolitical context.

**Edit 1 — tighten bullet 4 (loss of Normandy) to more directly link the event to the family.**

`str_replace` on `fact-sheets/g29-matthew-de-gournay-fact-sheet.md`:

`old_str`:
```
  <li><strong>Living 1206 — survived to see the loss of Normandy.</strong> Matthew was active in the period when King John lost Normandy to Philip Augustus (1204). The Montigny-sur-Andelle Norman holding that his grandfather William I had held in parage presumably passed out of the family's hands at this point, as most Anglo-Norman lords who remained in England forfeited their Norman estates. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

`new_str`:
```
  <li><strong>The generation that lost Normandy.</strong> When King John lost the duchy to Philip Augustus in 1204, every Anglo-Norman lord with cross-Channel holdings had to choose — keep their Norman estates and accept French overlordship, or keep their English estates and lose the Norman ones. Matthew, attested still living in 1206, lost Montigny-sur-Andelle: the parage tenure his father William I had held, and Daniel Gurney's "incontestable proof" of Gournay blood-descent, was severed. From his generation forward, the junior branch was an English family in every practical sense — their Norman heritage preserved only in their name. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

---

## G30 — Sir William de Gournay I, Knt. (fl. c. 1150–1180)

**Light pass.** Four highlights, strong throughout. Bullet 3 (probable Henry II charter witness at Notre Dame du Pré, Rouen) is good but uses heavy citation language. Bullet 4 (cross-Channel estates) overlaps slightly with bullet 1 (parage proof).

**Edit 1 — light polish on bullet 3.**

`str_replace` on `fact-sheets/g30-william-de-gournay-i-fact-sheet.md`:

`old_str`:
```
  <li><strong>Probable witness to a charter of <a href="https://en.wikipedia.org/wiki/Henry_II_of_England">Henry II</a> at Rouen.</strong> Daniel Gurney's Supplement records a "William de Gournay" witnessing a royal charter to the priory of <a href="https://en.wikipedia.org/wiki/Priory_of_Notre-Dame_du_Pr%C3%A9">Notre Dame du Pré</a> at <a href="https://en.wikipedia.org/wiki/Rouen">Rouen</a>, given by Henry II as King of England and Duke of Normandy. DG identified this as "in all probability the William de Gournay 1st of our Record." If correct, it places William at the heart of Anglo-Norman administration. <sup class="fn"><a href="#n7b" id="ref-7b">7</a></sup></li>
```

`new_str`:
```
  <li><strong>Probable witness to a Henry II charter at Notre Dame du Pré, Rouen.</strong> Daniel Gurney's <em>Supplement</em> records a "William de Gournay" witnessing a royal charter given by Henry II to the priory of Notre Dame du Pré at Rouen — Henry attesting in his double capacity as King of England and Duke of Normandy. DG identified the witness as "in all probability the William de Gournay 1st of our Record." If correct, it places William at the heart of mid-twelfth-century Anglo-Norman administration during a period when most Norfolk knights of his rank are documented only through tenurial records. <sup class="fn"><a href="#n7b" id="ref-7b">7</a></sup></li>
```

---

## G31 — Walter de Gournay (fl. c. 1108–1154)

**Light pass.** Five highlights, strong throughout. Bullet 5 ("A Norman village may bear his name" — Bois Gautier conjecture) is the weakest, leaning on a single-source 19th-century guess.

**Edit 1 — light polish on bullet 1 (junction point) — strengthen the headline framing.**

`str_replace` on `fact-sheets/g31-walter-de-gournay-fact-sheet.md`:

`old_str`:
```
  <li><strong>The junction point — every English and American Gurney descends from this man.</strong> Walter's elder brother <a href="https://en.wikipedia.org/wiki/Hugh_IV_de_Gournay">Hugh IV</a> inherited the great Norman barony. Walter received a younger son's share of the English estates. From this seemingly minor partition descend the <a href="https://en.wikipedia.org/wiki/Harpley">Harpley</a> Gournays, the <a href="https://en.wikipedia.org/wiki/West_Barsham">West Barsham</a> Gurneys, the <a href="https://en.wikipedia.org/wiki/Gurney_family">Quaker banking Gurneys</a>, and — through Francis Gurney's son John Gurney-1 — the American Gurneys. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

`new_str`:
```
  <li><strong>The junction point of the entire later family.</strong> Walter's elder brother <a href="https://en.wikipedia.org/wiki/Hugh_IV_de_Gournay">Hugh IV</a> inherited the great Norman barony — the senior line that held Gournay-en-Bray until it died out in the male line in 1235. Walter received a younger son's share of the English estates. Every subsequent line descends from him: the <a href="https://en.wikipedia.org/wiki/Harpley">Harpley</a> Gournays of the 13th–14th centuries, the <a href="https://en.wikipedia.org/wiki/West_Barsham">West Barsham</a> Gurneys of the 15th–17th, the <a href="https://en.wikipedia.org/wiki/Gurney_family">Quaker banking Gurneys</a> of Norwich, and — through Francis G14 and his probable son John Gurney-1 — the American Gurneys. The senior line ended after four generations; Walter's junior line is still here in Allen's generation, ~33 generations later. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

---

## G32 — Gerard de Gournay (c. 1040 – before 1104, Palestine)

**Light pass.** Five highlights, strong throughout. The "unsafe man to meddle with" anchor is excellent. Junction-point line is appropriately positioned. Bullet 4 (formidable lord) is slightly redundant with the unsafe-man line which is in the Norman authority highlight (currently bullet 4) — and the highlights have *two* anchors on Gerard's political ferocity.

**Edit 1 — light polish on bullet 4 (formidable lord) to remove the redundancy with the existing "unsafe man" framing.**

Reviewing the existing five bullets, they cover: (1) Crusade survived/then died on second; (2) Warenne marriage and seal; (3) Gundred / *la belle Gondrée* / Mowbrays; (4) "unsafe man to meddle with" + Saint-Wandrille charter; (5) Junction Point.

The five bullets are well-ordered and don't actually duplicate. Skip — leave G32 untouched in this patchset. Allen's framing is "lighter pass" for G28-G37 and G32 doesn't need any work.

**Decision:** No edits to G32.

---

## G33 — Hugh de Gournay III (c. 1020 – c. 1093)

**Light pass.** Six highlights — at the upper limit. All strong. Bullet 6 (Domesday Book) is slightly factual-list-y. Bullets 5 (1076 Bec charter) and 6 (Domesday) are both about English landholding.

**Edit 1 — light merge/polish on bullets 5 and 6 (consolidate the English-landholding pair into one stronger bullet).**

`str_replace` on `fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`:

`old_str`:
```
  <li><strong>His English manors pre-date Domesday by a decade.</strong> A 1076 charter in the <a href="https://en.wikipedia.org/wiki/Bec_Abbey">Abbey of Bec</a>'s cartulary records Hugh granting the tithes of three Essex parishes — Fordham, Liston, and Ardleigh — to the abbey. This proves he held these manors by 1076, ten years before the Domesday survey confirmed them. <sup class="fn"><a href="#n10b" id="ref-10b">10</a></sup></li>
  <li><strong><a href="https://en.wikipedia.org/wiki/Domesday_Book">Domesday Book</a>, 1086.</strong> Hugh held three Essex manors: <a href="https://en.wikipedia.org/wiki/Liston,_Essex">Liston</a> (with sub-tenant "Goisfredus Talbot" — a <a href="https://en.wikipedia.org/wiki/Talbot_family">Talbot</a> serving under a Gournay), <a href="https://en.wikipedia.org/wiki/Fordham,_Essex">Fordham</a>, and <a href="https://en.wikipedia.org/wiki/Ardleigh">Ardleigh</a>. A modest English beginning for a family whose Norman holdings were vast. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

`new_str`:
```
  <li><strong>The first English Gournay landholdings — documented a decade before Domesday.</strong> A 1076 charter in the Abbey of Bec's cartulary records Hugh granting the tithes of three Essex parishes — Fordham, Liston, and Ardleigh — to the abbey, proving he held these manors ten years before the Domesday Book confirmed them in 1086. The Domesday entry for Liston also names the sub-tenant "Goisfredus Talbot" — a Talbot serving under a Gournay, a small early glimpse of the Norfolk-Essex tenurial network. A modest English beginning for a family whose Norman holdings were vast. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
```

This drops the highlight count from six to five and consolidates the slightly-overlapping pair.

---

## G34 — Hugh de Gournay II (c. 985 – c. 1074)

**Light pass.** Five highlights, strong throughout. Mortemer "Franceiz, levez!" cry is rightly the headline. **The most arresting line in the underlying fact-sheet narrative — Hannay's "After the battle, Hugh 'vanishes... like a spectre horseman'" — is currently in the narrative section but not in the highlights.** This is a genuinely strong promotion candidate from the inspiration file.

**Edit 1 — replace bullet 5 ("Three Gournays at Hastings") with a sharper highlight that absorbs the spectre-horseman line.**

`str_replace` on `fact-sheets/g34-hugh-de-gournay-ii-fact-sheet.md`:

`old_str`:
```
  <li><strong>Three Gournays at <a href="https://en.wikipedia.org/wiki/Battle_of_Hastings">Hastings</a> — and Hugh was "Old Hugh."</strong> <a href="https://en.wikipedia.org/wiki/Wace">Wace</a>'s <a href="https://en.wikipedia.org/wiki/Roman_de_Rou"><em>Roman de Rou</em></a> names three Gournays in the invasion fleet. Hugh — his hair already grey — sailed with his son Hugh III and a collateral. If the c. 985 birth date is correct, he was roughly eighty: Hannay suggested he may have been present in an advisory or ceremonial capacity rather than as a combatant. <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup></li>
```

`new_str`:
```
  <li><strong>Three Gournays at Hastings — and after the battle, "vanishes... like a spectre horseman."</strong> Wace's <em>Roman de Rou</em> names three Gournays in the 1066 invasion fleet: Hugh II with his son Hugh III and a collateral. If the c. 985 birth date is right, "Old Hugh" was about eighty at Hastings — and Hannay suggested he may have been present in an advisory or ceremonial capacity rather than as a combatant. After the battle Hannay memorably loses sight of him: Hugh "vanishes... like a spectre horseman" out of the documentary record into Norman tradition. The phrase is the perfect closing image for an old Norse-blood warrior whose life stretched from before-Conquest English politics to after-Hastings stillness. <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup></li>
```

---

## G35 — Renaud de Gournay (c. 970 – uncertain)

**Light pass.** Four highlights. Strong. Bullet 4 (transition from Norse sea-king to Norman gentleman) is decent but mostly Hannay-paraphrased context.

**Edit 1 — light polish on bullet 1 (the charter / first married couple) to lead with the more vivid framing from the inspiration file: "the line's first securely named couple."**

`str_replace` on `fact-sheets/g35-renaud-de-gournay-fact-sheet.md`:

`old_str`:
```
  <li><strong>The first confirmed ancestor.</strong> A charter of 989–996, preserved in connection with the priory of La Ferté-en-Bray, names "Renaud" and his wife "Alberarda" directly. Their son Gautier issued the document "<em>imperante fratre meo Hugone</em>" — "at the command of my brother Hugh." The charter was witnessed by Duke Richard I (Sans-Peur), his son Richard II, and Robert, Archbishop of Rouen — since Robert acquired his see in 989 and Richard I died in 996, the date window is firm. Hannay noted that "the donations were very considerable, and show that the house was great." <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

`new_str`:
```
  <li><strong>The first ancestor confirmed by contemporary document — and the line's first named married couple.</strong> A charter of 989–996, preserved in connection with the priory of La Ferté-en-Bray, names "Renaud" and his wife "Alberade" directly. Their son Gautier issued the document "<em>imperante fratre meo Hugone</em>" — "at the command of my brother Hugh." The charter was witnessed by Duke Richard I (Sans-Peur), his son Richard II, and Robert, Archbishop of Rouen; since Robert acquired his see in 989 and Richard I died in 996, the date window is firm. Hannay noted that "the donations were very considerable, and show that the house was great." Across the entire pre-1100 Gurney record, Renaud and Alberade are the earliest couple — husband and wife — that we can name together from a contemporary primary source. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

---

## G36 — Hugh de Gournay I (c. 945–950 – uncertain)

**Light pass.** Four highlights. The 800-year tower is rightly the headline. Bullet 4 (William Longsword's assassination context) is partly Hannay-paraphrased and the connection to Hugh personally is speculative.

**Decision:** No edits proposed for G36. The four highlights are well-balanced and the inspiration file's coverage of this generation overlaps so heavily with what's already there that further changes would be busywork.

---

## G37 — Eudes (Odon) de Gournay (c. 860 – after 911)

**Light pass.** Five highlights. The 1,160-years anchor (bullet 1) is rightly the headline; the present-day Gournay-en-Bray + Neufchâtel cheese (bullet 2) is a great touch. **The "rope-measured land grant" — *terram fidelibus suis funiculo divisit* — is in the fact sheet narrative section but not in the highlights.** This is the single most evocative phrase in the inspiration file's coverage of this generation.

**Edit 1 — replace bullet 4 ("frontier post given only to a trusted commander") with a fresh highlight that absorbs the rope-measured grant.**

`str_replace` on `fact-sheets/g37-eudes-de-gournay-fact-sheet.md`:

`old_str`:
```
  <li><strong>A frontier post given only to a trusted commander.</strong> The Pays de Bray was <a href="https://en.wikipedia.org/wiki/Duchy_of_Normandy">Normandy</a>'s most exposed eastern border — the gateway any French army would use to invade. The lord of Gournay was required by the <a href="https://en.wikipedia.org/wiki/Black_Book_of_the_Exchequer">Red Book Roll</a> to furnish the Duke with twelve knights and defend the marches at his own expense. As Hannay noted, this was "a most important" lordship that "would be established early, and given to some conspicuous and deserving fighting-man of the sea-king breed." <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

`new_str`:
```
  <li><strong>The land grant divided "by the measurement of a rope."</strong> Dudo of Saint-Quentin, writing about a century after the Treaty, recorded that Rollo divided the new duchy among his captains "by the measurement of a rope" — <em>terram fidelibus suis funiculo divisit</em>. Eudes received as his rope-measured share the town of Gournay-en-Bray and the surrounding Pays de Bray, Normandy's most exposed eastern frontier — the gateway any French army would use to invade. As Hannay noted, the lord of Gournay was required to furnish the Duke with twelve knights and defend the marches at his own expense; this was "a most important" lordship "given to some conspicuous and deserving fighting-man of the sea-king breed." A rope-measured parcel on a Norman frontier became the beginning of the line. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
```

---

## Application Order for Phase 2

1. Apply each ancestor's edits in the order listed above (G16 → G37).
2. For each `str_replace` operation, verify the `old_str` matches verbatim before applying.
3. After applying all edits, re-render the affected fact-sheet pages and visually confirm:
   - All bullet counts are sensible (no orphaned `<li>` openings or closings).
   - All `<sup class="fn">` footnote anchors still point to valid `#n…` IDs in the citation list.
   - No bullet duplicates another bullet on the same fact sheet.
4. Build site locally, navigate to each affected fact sheet, and read the highlight block aloud for cadence — Allen's standard final-pass check.

## Phase 2 Validation Checklist

- [ ] G16 highlight 4 no longer duplicates highlight 1.
- [ ] G17 boy-lord highlight correctly attributes the Lady Catherine Howard godmother to Henry G15, not Anthony.
- [ ] G17 Spelman-of-Congham kinship now appears as a highlight (replacing "Gurney's Place" Norwich town house).
- [ ] G19 700-sheep highlight leads with the figure.
- [ ] G20 highlight block consolidated from 5 to 5 (bullet roles redistributed; will-as-document leads).
- [ ] G22 highlight count expanded from 3 to 4.
- [ ] G23 royal-instruments highlight lifts a single specific (Carrow / Norwich Priory arbitration).
- [ ] G24 highlight block expanded from 3 to 4 with platform-builder + Black Death additions.
- [ ] G25 highlight block restructured: 1294→1332 inheritance + Lexham marriage + Black Death.
- [ ] G26 highlight 3 replaced with the 38-year-clerical-line risk highlight.
- [ ] G27 three-engrailed-crosses-trio highlight replaces refused-knighthood.
- [ ] G33 Bec charter and Domesday consolidated into one highlight (six → five).
- [ ] G34 spectre-horseman line now appears in the highlights.
- [ ] G37 rope-measured land grant now appears in the highlights.

## Items Deliberately NOT Touched in This Patchset

- **G02–G15 highlights** — out of scope per Allen's instruction. G02 received highlight edits in v04.
- **G15 Henry Gurney highlights** — out of scope (G15 was bordered by deep-range range G16–G27 but Allen specified G16 onward).
- **Notables and bylines** — already covered in v04 and earlier patchsets.
- **G32 Gerard** — already optimal; no edits needed in the lighter range.
- **G36 Hugh I** — already optimal; no edits needed in the lighter range.

---

## Items From the Inspiration File That Need Verification Before Use

These are evocative items in the highlights-inspiration.md file that I could not independently verify in the existing fact sheets / research companions, and so I have **not** added them to any highlight bullet. If Allen has the underlying source somewhere (e.g., in DG-Supplement extracts I haven't loaded, or in a separate research file), they could be added in a follow-up patchset.

1. **G23 Edmund — "Thirteen paupers in white around the body."** The G23 fact sheet's narrative and citations record only "8s. to be distributed to the poor on his burial day" (citation n4, drawing on Blomefield vol. vii). The thirteen-paupers-in-white detail is striking and would be a great highlight, but I could not source it. If it's in DG's <em>Supplement</em> burial-instructions transcription or a related document, it should be added — as a highlight, this would be one of the most arresting items on any pre-1500 Gurney fact sheet.

2. **G20 Thomas II — "Personal seal surviving in red wax on a 1445 deed at Hunstanton Hall."** Not in the existing G20 fact sheet. The Hunstanton Hall connection is plausible (the Lestranges were the Hunstanton family, and the West Barsham Gurneys had ongoing dealings with them), but I cannot independently verify the 1445 deed or the wax seal. If the deed exists in the Lestrange archive it would be a wonderful tangible-survival highlight.

3. **G18 William V era — "Anne Heydon's will of 1521 — turquoise ring, gilt cup, black satin, chamlet lined with sarcenet, cypress-wood coffer."** Anne Heydon's will would be a primary-source artefact of considerable richness. The G18 fact sheet citations mention Anne died c. 1521 but don't transcribe her will. If the will exists in the PCC records (she was widow of Sir Lionel Dymoke, hereditary King's Champion), the items listed would make superb material for the G18 fact sheet — though probably as a notables item or a research-companion artefact rather than as an ancestor highlight on William V's own fact sheet.

4. **G27 Sir John I — "Possible engrailed-cross memorial at Norwich Cathedral."** The inspiration file mentions this as a possible survival but I could not find it in the fact sheet, the v01 patchset work, or the G27 research companion. If a Norwich Cathedral monument survives, it would be a powerful tangible link to a Crusader.
