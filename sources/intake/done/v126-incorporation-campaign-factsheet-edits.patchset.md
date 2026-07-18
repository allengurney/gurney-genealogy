**Done:** 2026-07-18 09:51 PT

# Patchset v126 — Incorporation campaign: fact-sheet edits (Wave 7)

**Context.** Wave 7 of the campaign at
`tools/plans/campaign-2026-07-16-incorporation/incorporation-plan-and-prompts.md`.
Waves 1–5 already assimilated the six-round non-G13 discovery campaign and the outsourced
paleography packets into the permanent research layer (companions, place files, topic files,
`sources/corpus_supplement/`, `data/sources.json`). This patchset carries the **fact-sheet-grade
deltas only** into the published narratives, per `.claude/rules/fact-sheets.md` (plain-English
contract, story-led-not-source-led, dates-in-years, read-as-if-written-all-at-once) and
`.claude/rules/citations.md`. It introduces **no new `data/sources.json` entries and no new
validation files** — every `sourceId` cited below already exists in the registry (registered by
Waves 1–3), verified before writing this patchset.

The companions are the source of truth; the fact sheets in several cases already carried most of
the will/charter content from earlier patchsets, so many campaign findings needed no promotion.
The edits below are the genuine remaining deltas.

**Scope note — what the campaign did NOT change on the fact sheets, and why (no operation):**

- **G20 will body** — the fact sheet already carried the burial triangle, three residences, the
  turquoise-ring/Walsingham confraternity, Margaret's textile clause, the John Bernard confessor,
  the executors and John Heydon supervisor, and sons William/John/Edmund (added in earlier
  patchsets v60–v63, refined v80–v82). Wave 7 corrects only the **Swathings disposal** (E3), adds
  the **community householder legacies**, **distinguishes the 1454 Great Ellingham namesake**, and
  **strengthens the will citation** to the now-read Jekkys register.
- **G34 (Hugh II)** — the W2 generational reconciliation (`g33` companion §3.4) retained the
  repo's Hugh II / Hugh III / Gerard ordering at ~85–90% and made no structural change. All the
  Hugh II evidence it rests on (the 1035 Barfleur expedition, Mortemer 1054, the pre-1066 Bayeux
  charters, Wace's "li vieil Hue," the epithet relocation to G34) is already on the G34 fact sheet.
  The two genuinely new W2 items (an un-pulled Avranches 1037×1048 attestation; a 1123×1128 "Hugo
  senex" recital that does not itself settle which Hugh) are not fact-sheet-grade. **No G34 edit.**
- **Milesent / Broughton dower / double seals (1167)** — this is Hugh IV's wife; Hugh IV is the
  senior (collateral) line, not the direct line. Per plan §C.4 collateral material is kept off the
  direct-ancestor fact sheets. **No edit** to promote Milesent to a direct-line fact sheet.
- **G13 (John Gurney)** — checked for any echo of the corrected Rivett "only Margaret of the right
  age" claim (rivett-family-of-garveston.md, corrected in Wave 3). The G13 fact sheet makes no such
  claim and no claim about Margaret's family origin. **No G13 edit.**
- **G32 Lessingham gift** — already present (timeline "Founds Lessingham Priory" + footnote 6, which
  already cites the Bec confirmations). The new record-level 1112 attestation firms the date but
  adds no fact-sheet-grade content. **No Lessingham operation.**

**Editorial posture.** Literal `str_replace` operations only; verbatim `old_string` / `new_string`.
Fact-sheet prose follows the plain-English contract. Where the campaign exposed a source conflict
(Swathings disposal), the fact sheet states it plainly rather than picking a side. Do **not** mirror
edited files to `site/` (the build handles the mirror; `.claude/rules/fact-sheets.md`).

**Phase-2 operations index.**
1. Item 1 — five `str_replace` edits: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`
2. Item 2 — three `str_replace` edits: `fact-sheets/g32-gerard-de-gournay-fact-sheet.md`
3. Item 3 — three `str_replace` edits: `fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`
4. Item 4 — three `str_replace` edits: `fact-sheets/g15-henry-gurney-fact-sheet.md`
5. Item 5 — two `str_replace` edits: `fact-sheets/g18-william-gurney-v-fact-sheet.md`
6. Item 6 — four `str_replace` edits: `fact-sheets/g14-francis-gurney-fact-sheet.md`
7. Closing (Phase 2 only): do **not** mirror to `site/`; prepend the `**Done:**` stamp and move this
   file to `sources/intake/done/`; then execute the campaign completion steps recorded at the end
   of this patchset (close the L-30 fact-sheet note; release packet 51 and the campaign residue to
   done/). These closing steps are **not** performed during Phase 1.

---

## Item 1 — G20 Thomas Gournay II (major)

Target file: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`. Five `str_replace` edits.
Source of truth: `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` (will treatment
reconciling the Jekkys register images × DG-I × Blomefield) and `research/places/great-ellingham.md`
(the 1454 namesake). Deltas **E1, E3**.

**1.1 — New Highlights bullet: the Swathings re-purchase (E3).** Adds a sixth bullet (the block
currently has five). Insert before the closing `</ul>` of the Highlights list.

`str_replace`
old_string:
```
the later 1471 choice of John Heydon as will supervisor. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup><sup class="fn"><a href="#n14" id="ref-14b">14</a></sup></li></ul>
```
new_string:
```
the later 1471 choice of John Heydon as will supervisor. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup><sup class="fn"><a href="#n14" id="ref-14b">14</a></sup></li>
  <li><strong>He bought back an ancestral manor his family had lost — then ordered it sold.</strong> Swathings in Hardingham had been a Gurney manor since the twelfth century before slipping out of the family's hands. Late in life Thomas repurchased it from a Catherine Sturmer, and in his will directed that it be sold again — a brief, deliberate reunion with a fragment of the family's medieval patrimony. <sup class="fn"><a href="#n12" id="ref-12i">12</a></sup></li></ul>
```

**1.2 — Narrative: correct the Swathings disposal and add the community householder legacies (E1, E3).**
The current text wrongly has Swathings "descend with the rest of the patrimony"; the will in fact
directed its sale, and the register and Blomefield diverge on the terms. The register-only
householder legacies are added.

`str_replace`
old_string:
```
The Norwich house was to be sold to his son William for 80 marks (about £53 in the money of the time), the first quantified valuation of any Gurney urban property. The Hardingham manor of Swathings, which Thomas had bought from a Catherine Sturmer at some earlier date, was to descend with the rest of the patrimony. Bequests of 40 shillings to the Norwich Greyfriars and 20 shillings each to the Augustinian Friars, the Dominicans, and the Carmelites placed Thomas inside the standard "all four orders" benefaction pattern of substantial Norfolk gentry.
```
new_string:
```
The manor of Swathings in Hardingham carried the will's most resonant back-story. A Gurney holding since the twelfth century, it had long since passed out of the family; Thomas had bought it back late in life from a Catherine Sturmer, and then directed in his will that it be sold again — a brief, deliberate reunion with a fragment of the medieval patrimony. Blomefield's summary has Swathings and the Norwich tenements sold together to his son William for 80 marks (about £53), the first cash valuation of any Gurney property in the family record; the register copy of the will instead has Swathings sold by the executors toward the will's charitable ends — a divergence the two witnesses leave open. <sup class="fn"><a href="#n12" id="ref-12j">12</a></sup> Beyond family and Church, Thomas remembered his neighbours: alongside gifts to the high altars of Harpley and West Barsham, he left twelvepence to every householder in West Barsham and a smaller sum to the householders of Harpley, a token to every family in his two home parishes. Bequests of 40 shillings to the Norwich Greyfriars and 20 shillings each to the Augustinian Friars, the Dominicans, and the Carmelites placed Thomas inside the standard "all four orders" benefaction pattern of substantial Norfolk gentry.
```

**1.3 — Citation n1: distinguish the 1454 Great Ellingham namesake.** Appends the disambiguation to
the identity footnote, with its record.

`str_replace`
old_string:
```
The "church of the friars minors" in Norwich is the Greyfriars (Franciscan) house at the eastern edge of the city, demolished at the Dissolution. <a class="citation-back" href="#ref-1">↩</a></li>
```
new_string:
```
The "church of the friars minors" in Norwich is the Greyfriars (Franciscan) house at the eastern edge of the city, demolished at the Dissolution. This Thomas Gournay, who lived until 1471, is distinct from a contemporaneous Thomas Gurnay of Great Ellingham in south Norfolk, who died intestate in 1454 leaving a widow, Alice (Norwich Consistory Court act book, administration of 5 August 1454) — a different man. <a class="citation-back" href="#ref-1">↩</a></li>
```

**1.4 — Citation n12: promote the will to a two-witness citation (Jekkys register + Blomefield).**
The register copy is now imaged and expert-read; the fact sheet is written as if the will were in
hand all along (no discovery framing). The expanded note also carries the Swathings divergence
apparatus that 1.1/1.2 reference.

`str_replace`
old_string:
```
  <li id="n12">Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42-47, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47">British History Online</a>. <a class="citation-back" href="#ref-12">↩</a></li>
```
new_string:
```
  <li id="n12">The will survives in two witnesses. The registered copy is Norwich Consistory Court will register Jekkys, folios 211v–212v (testament, last will, and probate of 27 July 1471), Norfolk Record Office. Its fullest English summary is Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42-47, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47">British History Online</a>. Register and summary agree on the burial alternative, the Walsingham and friary bequests, the West Barsham and Harpley householder legacies, the executors and John Heydon as supervisor, and the son Edmund's grant out of Depden; they differ over whether Swathings and the Norwich tenements passed to William for 80 marks (Blomefield) or Swathings was sold by the executors (register). Source IDs: <code>nro-ncc-wills-registers</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-12">↩</a></li>
```

**1.5 — Verification sweep (no text change beyond 1.1–1.4).** Phase 2: after applying 1.1–1.4,
confirm the new anchors `id="ref-12i"` and `id="ref-12j"` both point at existing `#n12`, that the
Highlights block now has six bullets, and that no `NEW`-style placeholder was introduced. (This is a
check step, not an edit.)

**End of Item 1.**

---

## Item 2 — G32 Gerard de Gournay (charter / attestation correction)

Target file: `fact-sheets/g32-gerard-de-gournay-fact-sheet.md`. Three `str_replace` edits.
Source of truth: `research/people/g32-gerard-de-gournay-fact-sheet.research.md` §2.12 — the
"Signum Girardi de Gornaco" is Gerard's subscription in the witness clause of a Richard de Redvers
benefaction (Deville's Charter XCIV), **not** a surviving pictorial seal. The fact sheet's "seal
survives / tangible physical evidence" overstates this and is corrected here.

**2.1 — Highlights bullet 2: recast "his seal survives" as his attestation.**

`str_replace`
old_string:
```
  <li><strong>Married the daughter of England's wealthiest earl — and his seal survives.</strong> The Warenne marriage brought Norfolk manors and the <a href="https://en.wikipedia.org/wiki/Caister-on-Sea">Caister-on-Sea</a> barony into the Gournay family. Gerard's own seal — "Signum Girardi de Gornaco" — is preserved in the Cartulary of <a href="https://en.wikipedia.org/wiki/Holy_Trinity_Abbey,_Rouen">La Trinité de Rouen</a>, tangible physical evidence of his authority as a Norman lord. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
```
new_string:
```
  <li><strong>Married the daughter of England's wealthiest earl — and his own witness-mark survives.</strong> The Warenne marriage brought Norfolk manors and the <a href="https://en.wikipedia.org/wiki/Caister-on-Sea">Caister-on-Sea</a> barony into the Gournay family. Gerard's mark as a witness — "Signum Girardi de Gornaco" — survives in the Cartulary of <a href="https://en.wikipedia.org/wiki/Holy_Trinity_Abbey,_Rouen">La Trinité de Rouen</a>, where he subscribed a benefaction of the great Anglo-Norman magnate Richard de Redvers — placing him among the first rank of the cross-Channel baronage. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
```

**2.2 — Citation n4: correct "seal" to the witness-subscription reading, with Deville's located charter.**

`str_replace`
old_string:
```
Daniel Gurney, <em>Supplement</em> (1858), Note 16, p. 735: Gerard's seal — "Signum Girardi de Gornaco" — in the Cartulary of La Trinité de Rouen (ed. Deville, Tome III, Charter No. 94).
```
new_string:
```
Daniel Gurney, <em>Supplement</em> (1858), Note 16, p. 735, records "Signum Girardi de Gornaco" in the Cartulary of La Trinité de Rouen (ed. Deville), now located as Charter XCIV: not a surviving pictorial seal but Gerard's subscription in the witness clause of a grant by Richard de Redvers to the abbey, alongside Hugh de Bellebeuf.
```

**2.3 — Citation n4: register Deville's cartulary in the note's Source-ID list.**

`str_replace`
old_string:
```
<code>recueil-actes-henri-ii-delisle-berger-vol-1</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```
new_string:
```
<code>recueil-actes-henri-ii-delisle-berger-vol-1</code>, <code>deville-cartulaire-sainte-trinite-rouen</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

**End of Item 2.**

---

## Item 3 — G33 Hugh de Gournay III (charter fact: the London holding)

Target file: `fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`. Three `str_replace` edits.
Source of truth: `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` §5.2 and §3.4
(the 1112/13 Bec confirmation and William I's earlier confirmation both recite Hugh III's London
holding "of King William"). Fordham is already on the fact sheet; the **London holding** is the new
charter fact. The W2 reconciliation retained the repo's generation ordering, so no structural change.

**3.1 — Narrative: add the London holding to the English-landholdings paragraph.**

`str_replace`
old_string:
```
His Domesday holdings were modest by the standards of the great earls, but they were held directly of the king, and they were the first English soil the Gournay family owned.
```
new_string:
```
His Domesday holdings were modest by the standards of the great earls, but they were held directly of the king, and they were the first English soil the Gournay family owned. He also held property in London of King William I himself — a city foothold recited a generation later, when a royal confirmation for the Abbey of Bec listed among the family's gifts what Hugh "had in London of King William, father of King Henry," together with the church of Fordham. <sup class="fn"><a href="#n10" id="ref-10c">10</a></sup>
```

**3.2 — Timeline: add the London-holding row after the 1086 Domesday row.**

`str_replace`
old_string:
```
      <tr><td>1086</td><td>Domesday Book records Essex manors: Liston, Fordham, Ardleigh.</td></tr>
```
new_string:
```
      <tr><td>1086</td><td>Domesday Book records Essex manors: Liston, Fordham, Ardleigh.</td></tr>
      <tr><td>by 1087</td><td>Holds property in London of King William I (recited in later Bec confirmations).</td></tr>
```

**3.3 — Citation n10: add the Bec confirmations that recite the London holding.**

`str_replace`
old_string:
```
recording the Cartulaire du Bec — tithes of "Fordham, Listhone, et Arlie" given by Hugh to Bec with patronage rights. Source IDs: <code>domesday-1086</code>, <code>opendomesday-org</code>, <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-10">↩</a></li>
```
new_string:
```
recording the Cartulaire du Bec — tithes of "Fordham, Listhone, et Arlie" given by Hugh to Bec with patronage rights. Henry I's confirmation for Bec of 11 February 1112/13, and William I's own earlier confirmation of Bec's English holdings, both recite the same Hugh's London property, held "of King William," alongside the church of Fordham. Source IDs: <code>domesday-1086</code>, <code>opendomesday-org</code>, <code>dg-rec-supp</code>, <code>deeds-utoronto-gournay-charter-extracts</code>. <a class="citation-back" href="#ref-10">↩</a></li>
```

**End of Item 3.**

---

## Item 4 — G15 Henry Gurney (Great Ellingham anchor touch)

Target file: `fact-sheets/g15-henry-gurney-fact-sheet.md`. Three `str_replace` edits.
Source of truth: `research/places/great-ellingham.md` — the surviving Old Hall great house (a
c.1570 timber-framed house, its first-floor hall bearing a 1573 date associated with Henry) and the
NCC register-Lawson-151 anchor for Henry's 1623 probate. Reinforces Great Ellingham as a durable
Gurnay anchor without overstating a continuous 170-year tenure (the pre-Lovell 1454 Great Ellingham
Thomas is not connected to this line — see Item 1.3).

**4.1 — Narrative: add the surviving Old Hall at Great Ellingham; recast the single-building superlative to a pair.**

`str_replace`
old_string:
```
The Hingham manor house substantially survives as **Gurney's Manor, Hingham**, a Grade II listed building (Historic England list entry 1170752) whose 17th-century rear wing with chambered ceiling beams was built around 1600, in Henry's own lordship — making it the most direct surviving physical link to G15 of any building in Norfolk.
```
new_string:
```
The Hingham manor house substantially survives as **Gurney's Manor, Hingham**, a Grade II listed building (Historic England list entry 1170752) whose 17th-century rear wing with chambered ceiling beams was built around 1600, in Henry's own lordship. A second building from his lordship also survives at Great Ellingham: **Old Hall**, a timber-framed great house of about 1570, still standing as Old Hall Farmhouse, whose first-floor hall carries a 1573 date associated with Henry himself. <sup class="fn"><a href="#n20" id="ref-20">20</a></sup> Together they make Hingham and Great Ellingham the most direct surviving physical links to Henry of any buildings in Norfolk.
```

**4.2 — Citation n2: name the register row (Lawson 151) the campaign fixed to Henry's probate.**

`str_replace`
old_string:
```
registered copy in the Norwich Consistory Court will register for 1621–1623, FamilySearch image group 008470484, images 594–596
```
new_string:
```
registered copy in the Norwich Consistory Court will register Lawson, folio 151 (register for 1621–1623), FamilySearch image group 008470484, images 594–596
```

**4.3 — New citation n20 for the Old Hall building.** Append after citation n19, before the list close.

`str_replace`
old_string:
```
Source ID: <code>armstrong-norfolk-1781</code>. <a class="citation-back" href="#ref-19">↩</a> <a class="citation-back" href="#ref-19b">↩</a></li>
```
new_string:
```
Source ID: <code>armstrong-norfolk-1781</code>. <a class="citation-back" href="#ref-19">↩</a> <a class="citation-back" href="#ref-19b">↩</a></li>
  <li id="n20">Old Hall, Great Ellingham: Historic England, "Old Hall Farmhouse," <em>National Heritage List for England</em>, List Entry Number 1077566 (a c.1570 timber-framed house, now farmhouse, on an earlier moated manorial site); Norfolk Historic Environment Service, "MNF9108 — Old Hall, Great Ellingham," Norfolk Heritage Explorer (a mid-sixteenth-century first-floor hall, said to be dated 1573 by Henry Gurney). Source IDs: <code>historic-england-old-hall-farmhouse-1077566</code>, <code>nher-mnf9108-old-hall-great-ellingham</code>. <a class="citation-back" href="#ref-20">↩</a></li>
```

**End of Item 4.**

---

## Item 5 — G18 William Gurney V (L-122: documented in his own right)

Target file: `fact-sheets/g18-william-gurney-v-fact-sheet.md`. Two `str_replace` edits.
Source of truth: `research/people/g18-william-gurney-v-fact-sheet.research.md` — the Calendar of
Inquisitions Post Mortem, Henry VII, names "William Gurnay the younger" as a feoffee on the Wynter
estate (the qualifier distinguishing him from his father William IV, "senior"), and the 1493
Ormesby feoffment of his father-in-law Sir Henry Heydon names a William Gurney among the trustees.
This gives the "lightly documented" G18 a documentary footprint of his own (lead L-122).

**5.1 — Narrative: qualify "matters less for what he himself did" with his own documentary trace.**

`str_replace`
old_string:
```
He matters in the lineage less for what he himself did than for whom he married, and for the network of cousinage that his marriage brought into the Gurney family. <sup class="fn"><a href="#n5" id="ref-5c">5</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup>
```
new_string:
```
He matters in the lineage less for what he himself did than for whom he married, and for the network of cousinage that his marriage brought into the Gurney family. <sup class="fn"><a href="#n5" id="ref-5c">5</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup> Even so, he leaves a documentary trace of his own. An inquisition of Henry VII's reign names "William Gurnay the younger" as a feoffee-to-uses on the Wynter estate — the qualifier "the younger" marking him off from his father, William IV — and in 1493 his own father-in-law Sir Henry Heydon placed a William Gurney among the trustees of the Heydon manor of Ormesby in the Flegg country. In his short adult life he was an active participant in the Norfolk gentry's land-trust circuit, not merely a name in a marriage settlement. <sup class="fn"><a href="#n14" id="ref-14">14</a></sup>
```

**5.2 — New citation n14.** Append after citation n13, before the list close.

`str_replace`
old_string:
```
<code>dg-rec-supp</code>, <code>hop-drury-robert-i-1456-1535</code>. <a class="citation-back" href="#ref-13">↩</a></li></ol>
```
new_string:
```
<code>dg-rec-supp</code>, <code>hop-drury-robert-i-1456-1535</code>. <a class="citation-back" href="#ref-13">↩</a></li>
  <li id="n14"><em>Calendar of Inquisitions Post Mortem: Series 2, Volume 1, Henry VII</em> (London: HMSO), the John Wynter inquisition, naming "William Gurnay the younger, esq." among the feoffees, <a href="https://www.british-history.ac.uk/inquis-post-mortem/series2-vol1/pp430-451">British History Online</a>; the qualifier "the younger" distinguishes him from his father, William Gurney IV (G19). The Ormesby feoffment of 25 March 1493 by Sir Henry Heydon, naming a William Gurney among the trustees: <em>A Descriptive Catalogue of Ancient Deeds in the Public Record Office</em>, vol. 4 (London: HMSO, 1902), A.7857, pp. 229–230. Source IDs: <code>bho-ipm-henry-vii-townshend-gurnay-feoffee</code>, <code>descriptive-catalogue-ancient-deeds</code>. <a class="citation-back" href="#ref-14">↩</a></li></ol>
```

**End of Item 5.**

---

## Item 6 — G14 Francis Gurney (Rivett update: Margaret's family corrected)

Target file: `fact-sheets/g14-francis-gurney-fact-sheet.md`. Four `str_replace` edits.
Source of truth: `research/people/rivett-family-of-garveston.md` (Wave 3) — Margaret Rybett was a
**Rivet of Garveston, Norfolk**, not one of the armigerous Suffolk Ryvetts of Rishangles. The parish
register yields two candidates of the right age (bp. 1586, dau. of Francis, ~55%; bp. 1577/8, dau. of
Robert, ~40%). "Rybett" was the 1611 clerk's one-off spelling. This corrects the published
"Fritton, Rishangles, and Stowmarket" attribution. Edit 6.3 is a same-file adjacent style fix
(removing discovery-date framing per the read-as-if-written-all-at-once rule), disclosed as such.

**6.1 — Vitals (Marriages): correct Margaret's family from the Suffolk Ryvetts to the Garveston Rivets.**

`str_replace`
old_string:
```
        <div><strong>Margaret Rybett</strong> — married 23 September 1611 at St Martin at Palace, Norwich, Norfolk. Norfolk/Suffolk gentry; the Rybett/Ryvett family of Fritton, Rishangles, and Stowmarket. Margaret probably died c. 1616–1617; her burial has not yet been located. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```
new_string:
```
        <div><strong>Margaret Rybett</strong> — married 23 September 1611 at St Martin at Palace, Norwich. She was a daughter of the Rivet family of Garveston, in mid-Norfolk; the parish register offers two candidates of the right age, baptized in 1586 and in 1577/8, and which of them she was is not settled. "Rybett" was the marriage clerk's spelling of the family's usual "Rivet." Margaret probably died c. 1616–1617; her burial has not been located. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```

**6.2 — Narrative: correct the family attribution in the marriage sentence.**

`str_replace`
old_string:
```
Francis married first Margaret Rybett in 1611, linking himself to established Norfolk and Suffolk gentry.
```
new_string:
```
Francis married first Margaret Rybett in 1611 — a daughter of the Rivet family of Garveston, in mid-Norfolk.
```

**6.3 — Highlights: remove the discovery-date framing (adjacent style fix, read-as-if-written-all-at-once).**

`str_replace`
old_string:
```
  <li><strong>First marriage identified in the original register in March 2026.</strong> The marriage of Francis Gurney and Margaret Rybett at St Martin at Palace, Norwich, on 23 September 1611 closes the long unexplained gap between Francis's freedom in 1606 and his first London child in 1619. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```
new_string:
```
  <li><strong>A first marriage at Norwich in 1611.</strong> The marriage of Francis Gurney and Margaret Rybett at St Martin at Palace, Norwich, on 23 September 1611 closes the long-unexplained gap between Francis's freedom in 1606 and his first London child in 1619. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

**6.4 — Citation n5: record the Garveston Rivet identification, its two candidates, and the corrected misattribution.**

`str_replace`
old_string:
```
  <li id="n5">Norfolk Record Office, St Martin at Palace, Norwich, marriage register, 23 September 1611, Francis Gurney and Margaret Rybett; supporting Rybett/Ryvett family context from Norfolk and Suffolk gentry sources. <a class="citation-back" href="#ref-5">↩</a></li>
```
new_string:
```
  <li id="n5">Norfolk Record Office, St Martin at Palace, Norwich, marriage register (PD 12/1), 23 September 1611, Francis Gurney and Margaret Rybett. The bride was a Rivet of Garveston, Norfolk; the Garveston register yields two Margarets of the right age — Margaret, daughter of Francis Rivet, baptized 21 May 1586 (working weight ~55%), and Margarett, daughter of Robert Rivet, baptized 1 February 1577/8 (~40%), with a small residual for an unrecorded third — and the identification between them is unsettled. She is not of the armigerous Suffolk Ryvetts of Rishangles and Rattlesden, an earlier misattribution; the fuller analysis is in the project's research on the Rivett family of Garveston. Source ID: <code>nro-pd-12-1</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

**End of Item 6.**

---

## Phase-2 closing steps (campaign completion — do NOT perform in Phase 1)

After the six items are applied and the `**Done:**` stamp is prepended and this file is moved to
`sources/intake/done/`:

1. **Do not** mirror any edited fact sheet to `site/` (`.claude/rules/fact-sheets.md`); the build
   handles the mirror.
2. **Close the L-30 fact-sheet note.** The G20 companion HTML comment records L-30 as closed
   2026-07-17 with "fact-sheet update deferred to the v126 patchset"; that deferral is now
   discharged. Confirm no open lead still points here (`tools/research_leads.py`); if a residual
   L-30 handle survives, close it.
3. **Release packet 51 and the campaign residue.** Move the packet-51 brief + report from
   `sources/intake/paleography-staging/` to its `done/` per plan §B.4, and move the remaining
   campaign residue to `done/` — the lossless-completion gate for the incorporation campaign.

These steps close out Wave 7 and the campaign; they are listed here for the Phase-2 operator and
are outside the fact-sheet edits above.
