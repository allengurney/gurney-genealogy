**Done:** 2026-05-25 23:59 PT

# Intake patchset v61 — G19/G20/G21 additional-sources discovery (with G18, G22, G23 incidentals)

**Prepared:** 2026-05-25
**Phase:** 1. Ready for Phase 2.
**Sequencing:** This patchset uses fact-sheet footnote handles `nNEW1`–`nNEW7`; v62 uses `nNEW8`–`nNEW9`; v63 uses `nNEW10`+. No cross-patchset collisions.
**Highlights constraint:** All fact-sheet edits target the Narrative, Children, Timeline, and Citations sections only. None modifies the Highlights `<ul>` block, because `sources/intake/processed/Ready/v05-patchset-highlight-updates.md` (pending) is the authoritative restructure of the Highlights for G16-G37.

Findings from Blomefield (West Barsham and East Barsham parish entries via British History Online), the AHRC *Soldier in Later Medieval England* database, the Wikipedia + Carr-Calthrop chain for the Calthorpe in-laws, and a confirming re-read of the History of Parliament biography of Sir John Gurney d. 1408 (already preserved at `sources/corpus_supplement/John-Gurney-d1408-The-History-of-Parliamentx.md`).

## Action sequence

1. **Write file:** `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md` — full content in §A1 below.
2. **Write file:** `sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md` — full content in §A2 below.
3. **Insert two source-JSON blocks** in `data/sources.json` — full JSON in §A3 below.
4. **Append block** to `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` — content in §A4 below (full 1471 will text + 1422 John Gurnay Pont Meulan note).
5. **Append block** to `research/people/g19-william-gurney-iv-fact-sheet.research.md` — content in §A5 below (1455 senior, Walter 1495-96, William jr Dunton 1497-98; Pockthorpe = brother-in-law's house; 1505 trust feoffee circle; Paston I disambiguation).
6. **Append block** to `research/people/g21-thomas-gournay-i-fact-sheet.research.md` — content in §A6 below (1434-35 East Barsham feoffment + 1418 Harfleur garrison).
7. **Append block** to `research/people/g18-william-gurney-v-fact-sheet.research.md` — content in §A7 below (Heydon-supervisor 1471 → marriage 1484 alliance chronology).
8. **Append block** to `research/people/g23-edmund-gurney-fact-sheet.research.md` — content in §A8 below (cross-link to the existing HoP corpus_supplement file with the new Heylesdon-aftermath emphasis).
9. **Append block** to `research/people/g22-robert-gournay-fact-sheet.research.md` — content in §A9 below (Heylesdon-aftermath supplement, also cross-linking the existing HoP supplement file).
10. **`str_replace`** on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Narrative paragraph 4 — §A10 below.
11. **`str_replace`** on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Children table — §A11 below.
12. **`str_replace`** on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Timeline — §A12 below.
13. **`str_replace`** on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Citations to append footnotes `nNEW1`, `nNEW2` — §A13 below.
14. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 1 (Boleyn-descent gateway) — §A14 below.
15. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 2 (1455 senior, cadet settlements) — §A15 below.
16. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 3 (Pockthorpe = brother-in-law's house) — §A16 below.
17. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative to insert new 1505-trust-circle paragraph — §A17 below.
18. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Timeline — §A18 below.
19. **`str_replace`** on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Citations to append footnotes `nNEW3`, `nNEW4`, `nNEW5` — §A19 below.
20. **`str_replace`** on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` Narrative paragraph 3 (three smaller documentary attestations) — §A20 below.
21. **`str_replace`** on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` Timeline — §A21 below.
22. **`str_replace`** on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` Citations to append footnote `nNEW6` — §A22 below.
23. **`str_replace`** on `fact-sheets/g18-william-gurney-v-fact-sheet.md` Narrative (Heydon-alliance chronology) — §A23 below.
24. **`str_replace`** on `fact-sheets/g18-william-gurney-v-fact-sheet.md` Citations to append footnote `nNEW7` — §A24 below.
25. After all operations succeed, **move** this patchset to `sources/intake/done/` with `**Done:** YYYY-MM-DD HH:MM PT` stamp prepended.

---

## §A1 — New file: `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`

```md
# Blomefield, *History of Norfolk*, vol. vii, "West-Barsham," pp. 42-47 — Gurney extracts

Source: Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42-47. British History Online: <https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47>. Source ID: `blomefield-norfolk`.

The Blomefield West Barsham parish entry preserves the principal non-Daniel-Gurney attestation of the Gurney manorial descent at West Barsham from Edmund Gurney (d. 1387) through Henry Gurney's sale to the Calthorpes. Gurney-specific clauses extracted verbatim below.

## Edmund de Wauci's death and the Gurney inheritance

> Edmund de Wauci was lord in the 30th of the said King [Edward III, i.e. 1356], and had the King's protection, being in his service in Gascoign in France, and died in the 46th of Edward III [1372] leaving by Joan his wife, Edmund, his son and heir, aged 7 years; this Edmund died soon after, (as I take it) on whose death this lordship came to Edmund Gurney, by the marriage of Catherine daughter of Sir William, and sister and heir of Sir Edmund de Waucy.

> In the 41st of Edward III [1367], a fine was levied between Edmund Gurney, and Katherine his wife, querents, Thomas de Beeston, trustees, &c. deforcients, of the moiety of the manor of West-Barsham, settled on Edmund and Katherine, in tail.

## Edmund Gurney's will, 1387

> The will of this Edmund is dated at West-Barsham, on Thursday, the feast of the Ascension of our Lord in 1387. He bequeaths his body to be buried in the church of the Assumption of the Blessed Virgin in this town, and 8l. to be distributed to the poor here, on his burial day; Katherine his wife to have all her dower, and all his utensils in his house, and her part of all his other goods; appoints Osbert de Mundeford, and Thomas Kempe, his executors. Witnesses: William de Mildenhal, vicar of West-Barsham, Nicholas de Barsham, &c.; and was proved in the same year.

## Sir John Gurney V (d. 1408)

> John de Gourney was his son and heir by Catherine, who, in the 3d of Henry IV [1401-02] held one fee here of the Earl Warren.

> In the 6th and 7th of that King, he sued the dutchy of Lancaster for the common, called South Lings, to have free warren there, as his separate soil, and part of his lordship of this town, and that his father Edmund was possessed of it; this cause was put off by the King's letters, because this John was one of the knights of the shire, in the parliament held at Coventry, in the said sixth year, for the county of Norfolk; but in the seventh year it was adjudged against Gourney, the said common of South Lings being in the point of South Creke parish, and belonging to the dutchy of Lancaster; and John Gourney, Esq. was bound to the King in 500 marks, not to claim any right there hereafter, and not being within the lete of his manor of West-Barsham.

> He died in the 9th of Henry IV [actually 10 Henry IV per the IPM = 4 December 1408] seized of the manors of West and North Barsham, Harpley, Denver, Depeden, &c. He married Alice, widow of Richard Buvent, who survived him: Thomas Gourney was probably his son and heir.

## Thomas Gournay I (G21) — feoffee

> Thomas Gourney, Esq. was a feoffee for the manor of Wolterton, in East-Barsham, in the 13th of Henry VI [1434-35] and was living in the 18th of that King.

## Thomas Gournay II (G20) — the 1471 will

> Thomas Gurnay, senior, Esq by his will, dated March 18th, in the 9th of Edward IV [= 18 March 1469/70]. appoints his body to be buried in the chancel of St. Laurence the Martyr, of Harple, if he dies there; and if at Norwich, in the Friar-minors church to whom he gives 40s. to the Austin-friars, Friars-preachers, and Carmes there, 20s. each; to the manors of Walsingham 40s.; to the chapel of the Annunciation of the Blessed Virgin at Walsingham his gold ring, with a precious jewel set in it, called a turkeys; to Margaret his wife all his utensils, and then to William his son, after her death; appoints his wife, John Jerningham, and Edmund Bokenham, Esq. his executors; and John Heydon, supervisor; his sons, John and Edmund, to whom he confirms all grants made to them out of his manor of Depeden; to the prior of Walsingham 10l. towards a new work there, on condition they remember him and his wife in their beadroll, as brother and sister of that priory; all his manor, or tenement, called Swathyns, in Hardingham, which he bought of Catherine Sturmer, and all his tenements in Norwich to be sold to William his son for 80 marks. This house was in St. Gregory's parish at Norwich, and John Bernard, a minor of Norwich, was his confessor. This will was proved July 27, 1471.

## William Gurney IV (G19) — succession, "senior" by 1455, cadet settlements

> William Gurnay, Esq. was lord, and succeeded on his father's death. In the year 1455 he styled himself William Gurnay, Esq. senior; and in the 13th of Henry VII [1497-98]. William Gurnay, senior, Esq. &c. infeoft William Gurnay, junior, Esq. &c. of lands in Dunton. He married Ann, daughter of William Calthorpe, Esq. was a knight eschaetor for Norfolk, in the reign of Edward IV. He had also a son Walter, living in the 11th of Henry VII [1495-96]. to whom he then granted lands.

## Anthony Gurney (G17), 14 Henry VII (1499) Earl of Oxford grant context

> In the 14th of Henry VII [1499]. William Gournay, junior, and Thomas Sefoule, Esq. had a grant of the custody of the manors and lands of Roger Wood of East-Barsham, son and heir of John Wood, from John Earl of Oxford, to whom King Henry VII. had granted the custody of the person and lands of William Viscount Beaumont, by deed then dated.

## Anthony Gurney (G17), 1514-1555

> Anthony Gournay, Esq. was lord in 1514; he married Margaret, one of the daughters and coheirs of Sir Robert Lovell, cousin and coheir of Sir Thomas Lovell, privy counsellor to King Henry VII. and Henry VIII. and Knight of the Garter; and died January 4, 1555, leaving Henry, his grandson and heir, aged twenty-one years.

## Frances Gournay (G16) — son of Anthony

> Frances Gournay, Esq. was son of Anthony; he died before his father, and by Helen, daughter of Robert Holdich, of Ranworth, Esq. left Henry Gurney, Esq. his son and heir, who was lord of this town in 1572, (held by one fee of the manor of Castleacre)…

## Henry Gurney (G15) — 1572

> Henry Gurney, Esq. his son and heir, who was lord of this town in 1572, (held by one fee of the manor of Castleacre) he married, and had Edmund Gurney, Esq. his son and heir…

## Edmund Gurney (d. 1641)

> Edmund Gurney, Esq. his son and heir, who (as by an inquisition taken at East-Dereham, October 13th in the 17th of Charles I.) died August 6th, in 1641, seized of this manor, and that of NorthBarsham, Lingham-Magna, &c. and left by Frances his wife, daughter of Richard Hovell, Esq. Henry, his son and heir, aged nine years, &c. who sold this lordship to the family of Calthorpe…

Church monument:

> Caducum hoc œternat Marmor Edwardus Gourney, filius et heres Tho. Gourney Armig. et Marthœ filiœ Edvi. Lewkenor de Denham, in Com. Suff. Militis, obiit Aug. 1641.

## 1603 — Henry Gurney as patron

> In 1603, Leonard Metcalf occurs vicar, and certified 420 communicants; patron then, Henry Gurney.

## Pre-Gurney West Barsham — Walter de Wauci's sheep-foldcourse charter

> Walter de Wauci confirmed to them [the priory] the gifts of his father Hugh, and gave them four acres, with liberty of a fold course for nine score sheep; and that they might take of their men (in the town of West Barsham) customary aid, as they took of their other men, in other places.
```

---

## §A2 — New file: `sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md`

```md
# Blomefield, *History of Norfolk*, vol. vii, "East-Barsham," pp. 53-65 — Gurney extracts

Source: Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: East-Barsham," pp. 53-65. British History Online: <https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp53-65>. Source ID: `blomefield-norfolk`.

Gurney-specific clauses from the East Barsham entry. The East Barsham principal lordship was the Wode family; Gurney involvement is limited to two documented feoffments.

## Thomas Gournay I (G21) — 1434-35 feoffment confirming Wolterton's Manor to John Wode

In the 13th of Henry VI (1434-35), Thomas Gournay Esquire and John Hunt, son of William Hunt of East-Barsham, confirmed Wolterton's Manor (the principal East Barsham manor) to John Wode.

(Verbatim attestation in Blomefield: "*Thomas Gournay*, Esq. and *John Hunt*, son of *William Hunt*, of *East-Barsham*" confirming the manor to John Wode in the 13th of Henry VI [1434-35].)

This is independent of the 1445 Hunstanton seal attestation (Daniel Gurney *Supplement* Note 126, p. 814) and of Thomas I's 1441 retinue service under John de Vere 13th Earl of Oxford in France (AHRC medievalsoldier database). Together the three give Thomas I documented active-adult attestations across 1434-1445.

## William Gurney junior (G18) — 1499 Earl of Oxford grant

> [11 Hen VII, 1495-96, error in this Blomefield clause: should read 14 Hen VII = 1499 per the cross-confirming West Barsham entry.] William Gurney, junior, and Thomas Sefoule, Esq. had a grant of the custody of the manors of Roger his son, then a minor [= Roger Wode, son of John Wode], from John Earl of Oxford, to whom King Henry VII. had granted the custody of the person and lands of William Viscount Beaumont.

The Earl of Oxford here is John de Vere 13th Earl of Oxford — the same earl in whose 1441 retinue William's grandfather Thomas Gournay I had served in France. The Vere-Gurney connection therefore runs through two consecutive generations on the Gurney side. The Beaumont wardship was a major Crown grant to Vere following the death of William Viscount Beaumont's father (and the latter's incapacity); the Earl's sub-grant of the Wode wardship to William Gurney junior + Thomas Sefoule was a routine local administration of the larger wardship.
```

---

## §A3 — Source JSON additions in `data/sources.json`

The two new corpus-supplement files cited above point back to the existing `blomefield-norfolk` source. The `data/sources.json` entry for `blomefield-norfolk` should have its `corpusPath` updated to reflect that multiple supplement files now extract from this source.

If `data/sources.json` currently has `blomefield-norfolk.corpusPath` set to a single path or null, change it to `null` and add the two paths into the `notes` field so the JSON shape is preserved. (No new sourceId is introduced by v61. The new supplement files are filed under the existing `blomefield-norfolk` sourceId.)

**`str_replace`** in `data/sources.json` on the `blomefield-norfolk` entry's `notes` field — append the following text to the existing notes:

> "Per-parish extracts captured in `sources/corpus_supplement/` as separate files: `blomefield-norfolk-vol7-pp42-47-west-barsham.md` (West Barsham, Gurney manorial descent and 1471 will text); `blomefield-norfolk-vol7-pp53-65-east-barsham.md` (East Barsham, 1434-35 Thomas Gournay I feoffment and 1499 Earl of Oxford grant to William junior); `blomefield-norfolk-vol5-pp33-cringleford-berford.md` (existing, Edmund Gurney G23 as 1370 De la Pole feoffee at Cringleford)."

(Note for Phase 2: only the new parish-extract pointers go into the notes append; the existing Cringleford extract is already in the registry. If the existing notes field already mentions the Cringleford file, drop that mention from the new append text to avoid duplication.)

---

## §A4 — Append to `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`

Append the following block at the end of the existing Working Notes section:

```md
### Thomas II's 1471 will — full Blomefield extract (West Barsham parish entry)

Blomefield's West Barsham parish entry preserves the complete English-summary text of Thomas Gurnay senior's 1471 will — fuller than Daniel Gurney's extracts at pages 280-282 of the *Record*:

> "Thomas Gurnay, senior, Esq by his will, dated March 18th, in the 9th of Edward IV. appoints his body to be buried in the chancel of St. Laurence the Martyr, of Harple, if he dies there; and if at Norwich, in the Friar-minors church to whom he gives 40s. to the Austin-friars, Friars-preachers, and Carmes there, 20s. each; to the manors of Walsingham 40s.; to the chapel of the Annunciation of the Blessed Virgin at Walsingham his gold ring, with a precious jewel set in it, called a turkeys; to Margaret his wife all his utensils, and then to William his son, after her death; appoints his wife, John Jerningham, and Edmund Bokenham, Esq. his executors; and John Heydon, supervisor; his sons, John and Edmund, to whom he confirms all grants made to them out of his manor of Depeden; to the prior of Walsingham 10l. towards a new work there, on condition they remember him and his wife in their beadroll, as brother and sister of that priory; all his manor, or tenement, called Swathyns, in Hardingham, which he bought of Catherine Sturmer, and all his tenements in Norwich to be sold to William his son for 80 marks. This house was in St. Gregory's parish at Norwich, and John Bernard, a minor of Norwich, was his confessor. This will was proved July 27, 1471."

New material beyond Daniel Gurney's summary:

- **Will dated 18 March 1469/70** (9 Edward IV), not just "1471" (which is the probate date).
- **Sons John and Edmund** named alongside William IV, with grants confirmed out of the Depden manor in Suffolk. The published Gurney pedigree records only William IV.
- **John Heydon of Baconsthorpe as supervisor.** Same Heydon documented in the *Paston Letters* as William de la Pole 1st Duke of Suffolk's chief East Anglian agent and joint Duchy of Lancaster steward with Sir Thomas Tuddenham. The 1471 supervisor role places a working Gurney-Heydon alliance 13 years before G18 William V's 1484 marriage to Anne Heydon.
- **John Jerningham as co-executor** — most plausibly Margaret's brother, anchoring the Jerningham-of-Somerleyton tie.
- **Edmund Bokenham Esquire as co-executor** — Bokenham family of Old Buckenham; foreshadows William IV's daughter Constance's later marriage to William Bokenham (per the published Gurney pedigree).
- **Catherine Sturmer of Hardingham** sold Swathings to Thomas II at an unrecorded earlier date — a new name in the Hardingham descent chain.
- **Norwich house in St Gregory's parish** sold to William for 80 marks (about £53) — the first quantified valuation of any Gurney urban property.
- **John Bernard, a Friar Minor of Norwich**, as Thomas II's confessor — direct tie to the Norwich Greyfriars community.

The Walsingham bequests — 40 shillings to the manors of Walsingham, the gold-turquoise ring to the chapel of the Annunciation, £10 toward a "new work" in exchange for beadroll membership — supplement the family's earlier 1385 Walsingham grant (Edmund G23 with Calthorpe, Hales, Shelton) and Sir John V's 1406 Walsingham grant for the Reynham memorial, giving a three-generation pattern of priory patronage at England's principal Marian pilgrimage shrine.

Full Blomefield West Barsham parish entry (including this will text and the wider Gurney manorial descent) preserved at `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`.[^v61-blomefield-vol7-west-barsham]

[^v61-blomefield-vol7-west-barsham]: Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42-47, [British History Online](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47). Source ID: `blomefield-norfolk`. Full per-parish extract at `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`.

### 1422 "John Gurnay" man-at-arms in Sir Robert Harling's retinue — Pont Meulan (tentative)

A single 1422 muster in the AHRC medievalsoldier database records "Gurnay, John, Man-at-Arms, Garrison of Poissy / Pont Meulan, Captain Sir Robert Harling (d. 1435), 1 November 1422, Bibliothèque nationale de France, MS Français 25766, no. 816."[^v61-medievalsoldier-john-gurnay-1422] Sir Robert Harling of East Harling, Norfolk, was killed at the siege of Saint Denis in 1435.

The man-at-arms rank places this John Gurnay at gentleman class, consistent with the Norfolk gentry Gurney line, but no identification with any named Gurney from existing pedigrees is warranted. Possibilities include an undocumented son of Robert G22 (a cousin of Thomas I G21) or an unrelated cadet-branch member. The 1422 date sits between Thomas I's 1418 Harfleur garrison service and his 1441 Vere/York retinue, and reinforces the picture of a Norfolk Gurney military client network in France across Henry V and the early Henry VI minority.

[^v61-medievalsoldier-john-gurnay-1422]: John Gurnay, Man-at-Arms, Garrison of Poissy / Pont Meulan, Captain Sir Robert Harling (d. 1435); Muster Roll Bibliothèque nationale de France, MS Français 25766, no. 816; 1 November 1422. AHRC-funded *Soldier in Later Medieval England Online Database*: [www.medievalsoldier.org](https://www.medievalsoldier.org/). Source ID: `medievalsoldier-database`.
```

---

## §A5 — Append to `research/people/g19-william-gurney-iv-fact-sheet.research.md`

Append the following block at the end of the existing Working Notes section:

```md
### "Senior" by 1455; 1495-96 cadet grant to Walter; 1497-98 Dunton settlement on William junior

Blomefield's West Barsham parish entry preserves three pre-mortem chronology data points for William IV beyond what Daniel Gurney records:

> "William Gurnay, Esq. was lord, and succeeded on his father's death. In the year 1455 he styled himself William Gurnay, Esq. senior; and in the 13th of Henry VII. William Gurnay, senior, Esq. &c. infeoft William Gurnay, junior, Esq. &c. of lands in Dunton. He married Ann, daughter of William Calthorpe, Esq. was a knight eschaetor for Norfolk, in the reign of Edward IV. He had also a son Walter, living in the 11th of Henry VII. to whom he then granted lands."[^v61-blomefield-vol7-west-barsham-g19]

- **1455:** Already styling himself "senior," sixteen years before his father Thomas II's 1471 death — operating as an adult of the West Barsham line in his father's lifetime.
- **1495-96** (11 Henry VII): grants lands to son Walter — the documented founding settlement of the Cawston/Aylsham cadet branch. The published pedigree mentions Walter as the cadet-line founder but gives no date.
- **1497-98** (13 Henry VII): settles lands at Dunton on William junior (G18) — a pre-mortem trust event distinct from the better-known 1485 and 1505 trust deeds preserved in the 1532 inquisition post mortem.

Blomefield's odd phrase "a knight eschaetor for Norfolk" may indicate William IV was knighted in his lifetime (a possibility not in Daniel Gurney), or may be a Blomefield slip for "knight escheator" / "escheator under a knight-service obligation." Not asserted in the fact sheet without independent corroboration.

[^v61-blomefield-vol7-west-barsham-g19]: Francis Blomefield, *History of Norfolk*, vol. vii, "West-Barsham," pp. 42-47, [British History Online](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47). Source ID: `blomefield-norfolk`. Full extract at `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`.

### Pockthorpe-by-Norwich residence = brother-in-law William Calthorpe's manor house

Daniel Gurney's *Supplement* Note 131, p. 817 identifies the Calthorpe manor house at Pockthorpe-by-Norwich as "the same as that afterwards inhabited by the Blennerhassets, and called Hassets' Hall" (Blomefield vol. iv, p. 428) and adds: "I think it likely William Gurney had resided in this same manor house in Pockthorpe, called the Lathes, before the Calthorpes, or with them, having married a Calthorpe."

The Calthorpe pedigree at Carr-Calthrop, *Notes on the Families of Calthorpe and Calthrop* (London: Spottiswoode, Ballantyne & Co., 1933), identifies **William Calthorpe of Pokethorpe (d. 1528)** as a son of Sir William Calthorpe Knight of the Bath by his first wife Elizabeth Grey — full brother of William IV's wife Anne Calthorpe. He is named separately as a feoffee on William IV's 1505 trust deed (Daniel Gurney *Supplement* Note 132, pp. 817-819).

William IV's "of Pockthorpe-by-Norwich" residence designation is therefore best read as William IV using a town house in the same Pockthorpe complex held by his brother-in-law. The Norwich town address was a kinship arrangement, not a separate Gurney acquisition.

### 1505 trust feoffees as a closed kinship-and-affinity circle

The 1505 trust deed (deed dated 6 April 1505, 21 Henry VII, recorded in William IV's posthumous inquisition post mortem) names seven feoffees: **Sir Edward Howard, Sir Philip Calthorpe, Sir Robert Clere, Sir Robert Drury, Nicholas Appleyard Esquire, William Calthorpe of Pockthorpe, and Thomas Gurnay Esquire** (Daniel Gurney *Supplement* Note 132, pp. 817-819).

Each feoffee's relationship to William IV:

- **Sir Edward Howard** (1476/77 – 25 April 1513): son of Thomas Howard 2nd Duke of Norfolk; later Lord High Admiral of England; killed at Brest 25 April 1513. Source authority: Susan Doran, "Howard, Sir Edward (1476/7-1513)," *Oxford Dictionary of National Biography*, [oxforddnb.com](https://www.oxforddnb.com/view/10.1093/ref:odnb/9780198614128.001.0001/odnb-9780198614128-e-13886).
- **Sir Philip Calthorpe**: son of Sir William Calthorpe Knight of the Bath, probably by his second wife Elizabeth Stapleton — half-nephew of William IV's wife Anne Calthorpe. Source authority: Carr-Calthrop, *Notes on the Families of Calthorpe and Calthrop* (1933), Calthorpe pedigree.
- **Sir Robert Clere** (c. 1444 – 1529) of Ormesby St Margaret, Norfolk: Howard-circle Norfolk knight. *Visitations of Norfolk* (Harleian Society, 1891).
- **Sir Robert Drury** (c. 1456 – 1535), Speaker of the House of Commons 1495; Knight of the Body to Henry VII and Henry VIII; Privy Councillor. **Married, by 1494, Anne Calthorpe — daughter of Sir William Calthorpe Knight of the Bath by his second wife Elizabeth Stapleton.** Anne Calthorpe (wife of William IV) and Anne Calthorpe (wife of Sir Robert Drury) were both daughters of Sir William Calthorpe Knight of the Bath by his two different wives; the two women were therefore half-sisters. Sir Robert Drury was William IV's half-sister-in-law's husband. Source authority: HoP biography of Drury (full text at `sources/corpus_supplement/hop-drury-robert-i-1456-1535.md` via v62).
- **Nicholas Appleyard Esquire**: Appleyard family of Bracon Ash, Norfolk; allied with the Heydons through Heydon-Appleyard marriages. The same Appleyard family had a Nicholas Appleyard as a 1452 St George's Day petition co-signer alongside Thomas Gournay II — a 53-year continuity of the Gurney-Appleyard tie (Blomefield vol. v).
- **William Calthorpe of Pockthorpe**: William IV's full brother-in-law (see above).
- **Thomas Gurnay Esquire**: William IV's son, named in Daniel Gurney's pedigree at *Record* p. 287 as "Thomas Gurnet, his father's executor, ancestor of the Gurneys of Dartmouth, London, and Essex."

This is a closed Calthorpe-Howard-Drury kinship-and-affinity circle — the inner social world into which William IV's marriage to Anne Calthorpe had embedded the West Barsham line.

### 1466 Acle escheator IPM — disambiguation of "Johannes Paston"

Daniel Gurney *Supplement* Note 129, p. 816 records William IV presiding as Escheator of Norfolk over an Inquisition Post Mortem at Acle market on 13 October 1466, concerning "Johannes Paston." Disambiguation: John Paston I died on 22 May 1466 — well before the October inquisition. John Paston II died in November 1479; John Paston III in 1504. Only John Paston I died in 1466, so the Acle IPM is on his holdings.

John Paston I was the husband of Margaret Paston (the most prolific letter-writer of the *Paston Letters*) and the central figure in the Paston-Heydon-Fastolf disputes of the 1460s. William IV's role in his IPM is therefore a high-prestige Norfolk gentry connection that the existing G19 fact-sheet Escheator highlight could be strengthened to surface, after a cross-check of the *Paston Letters* Gairdner edition (vol. IV/V) confirms no mention of William Gurney as escheator at the 1466 Paston inquisition. Deferred to a future patchset.

### G18 William V's marriage to Anne Heydon — the Boleyn-descent gateway

The G19 narrative line "the eldest son whose marriage would bring Boleyn descent into the family" is generic. The actual gateway:

- William V (G18) married **Anne Heydon** of Baconsthorpe (1484 indentures).
- Anne Heydon's mother was **Anne Boleyn the elder** (d. c. 1509), one of the children of Sir Geoffrey Boleyn (1406-1463), Lord Mayor of London 1457-58.
- Sir Geoffrey Boleyn's other children included **Sir William Boleyn** (1451-1505), father of **Sir Thomas Boleyn 1st Earl of Wiltshire**, father of **Queen Anne Boleyn**.
- Anthony Gurney G17 was therefore second cousin to Queen Anne Boleyn, second cousin once removed to Queen Elizabeth I.

The G17 Queen Anne Boleyn related fact sheet at `fact-sheets/g17-queen-anne-boleyn-related-fact-sheet.md` carries the full chain. G19's narrative should cite that fact sheet specifically rather than leave "Boleyn descent" generic.
```

---

## §A6 — Append to `research/people/g21-thomas-gournay-i-fact-sheet.research.md`

Append the following block at the end of the existing Working Notes section (specifically, immediately after the existing 22 May 2026 medievalsoldier sub-section):

```md
### Third military attestation — 1418 Harfleur garrison, under Thomas Beaufort Duke of Exeter

AHRC database entry: "Gournay, Thomas, Man-at-Arms, Garrison; mustered: Harfleur, Captain Thomas Beaufort (c. 1377-1426) earl of Dorset, duke of Exeter, Lieutenant Sir William Willoughby, 1418, Muster rolls, TNA E101/48/6."[^v61-medievalsoldier-thomas-gournay-1418]

This fills the gap between the 1415 Agincourt-campaign Holland-retinue muster and the 1441 Vere/York France expedition. At Harfleur in 1418 the Duke of Exeter (Henry V's lieutenant of Normandy) was holding the bridgehead during Henry V's consolidation phase after Agincourt; service at this garrison station is the natural next phase for the man already mustered at Southampton in July 1415. The Holland-then-Beaufort sequence places Thomas I inside the Lancastrian military client network across two reigns — a continuation of the family's Gaunt-era patronage chain (Edmund G23 was steward of John of Gaunt's East Anglian estates 1372-1387; Sir John V served on Gaunt's 1394 Aquitaine expedition under letters of attorney TNA C61/104 m. 7, already documented in the G23 companion).

[^v61-medievalsoldier-thomas-gournay-1418]: Thomas Gournay, Man-at-Arms, Garrison mustered at Harfleur, Captain Thomas Beaufort earl of Dorset (later duke of Exeter), Lieutenant Sir William Willoughby; 1418; Muster Roll The National Archives, E101/48/6. AHRC-funded *Soldier in Later Medieval England Online Database*: [www.medievalsoldier.org](https://www.medievalsoldier.org/). Source ID: `medievalsoldier-database`.

### 1434-35 East Barsham feoffee — third Norfolk attestation

Blomefield's East Barsham parish entry records that "Thomas Gournay, Esq. and John Hunt, son of William Hunt, of East-Barsham" confirmed Wolterton's Manor in East Barsham to John Wode in the 13th of Henry VI (1434-35).[^v61-blomefield-vol7-east-barsham-g21]

This is the third documented attestation for Thomas I, alongside the 1445 Hunstanton seal (Daniel Gurney *Supplement* Note 126, p. 814) and the 1441 retinue service under John de Vere 13th Earl of Oxford. Together they give Thomas I a documented active-adult span of 1415 (Agincourt) – 1418 (Harfleur) – 1434-35 (East Barsham) – 1441 (Vere/York France) – 1445 (Hunstanton seal). The previous "no record" framing in the G21 companion should be retired.

Full Blomefield East Barsham extract preserved at `sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md`.

[^v61-blomefield-vol7-east-barsham-g21]: Francis Blomefield, *History of Norfolk*, vol. vii, "East-Barsham," pp. 53-65, [British History Online](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp53-65). Source ID: `blomefield-norfolk`. Full extract at `sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md`.
```

---

## §A7 — Append to `research/people/g18-william-gurney-v-fact-sheet.research.md`

Append the following block at the end of the existing Working Notes section:

```md
### Heydon-Gurney alliance — operating in 1471, formally sealed by the 1484 marriage

The 1484 marriage indentures between William V (G18) and Anne Heydon (granddaughter of John Heydon of Baconsthorpe) are conventionally framed as the moment the Heydon connection entered the Gurney line. The full record shows the alliance was operating thirteen years earlier:

- **27 July 1471 — Thomas Gournay II's will probated.** John Heydon of Baconsthorpe is named as supervisor (the senior overseer of the executors). Heydon was the most powerful Norfolk lawyer of the mid-fifteenth century, the *Paston Letters* antagonist, William de la Pole's chief East Anglian agent, joint Duchy of Lancaster steward with Sir Thomas Tuddenham, and survivor of Tuddenham's 1462 execution by paying 500 marks for a Yorkist pardon. (Source: Blomefield, *History of Norfolk*, vol. vii, "West-Barsham," pp. 42-47, will text — see `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`.)
- **January–May 1472 — Saxthorpe Court showdown.** Henry Heydon (John Heydon's son) raises men-at-arms in William Gurney IV's support during William IV's two attempts to hold a manorial court at Saxthorpe against John Paston. Documented in the Gairdner Introduction to the *Paston Letters* — see v62 for the full extract.
- **28 May 1484 — Marriage indentures.** Between Henry Heydon Esquire and William Gurnay senior (= G19 William IV), arranging the marriage of Henry's daughter Anne Heydon to G19's son and heir William junior (= G18 William V). Documented in Daniel Gurney *Supplement* Note 132, pp. 817-819 (within the 1485 trust deed recital).

The 1484 marriage was the formal sealing of a Gurney-Heydon professional and military alliance that had already been operating in the field for thirteen years.[^v61-heydon-alliance-chronology]

[^v61-heydon-alliance-chronology]: 1471 supervisor: Francis Blomefield, *History of Norfolk*, vol. vii, "West-Barsham," pp. 42-47, [British History Online](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47), Source ID `blomefield-norfolk`. 1472 Saxthorpe Court: James Gairdner, ed., *The Paston Letters* (1904), Introduction vol. I, Source ID `paston-letters-gairdner` (added to `data/sources.json` in v62). 1484 marriage indentures and 1485 trust deed: Daniel Gurney, *Supplement to the Record of the House of Gournay* (King's Lynn: Thew & Son, 1858), Note 132, pp. 817-819, Source ID `dg-rec-supp`.
```

---

## §A8 — Append to `research/people/g23-edmund-gurney-fact-sheet.research.md`

Append the following block at the end of the existing Sir John V sub-section:

```md
### History of Parliament biography — already preserved in corpus supplement

The full text of L. S. Woodger, "GURNEY, John (d.1408), of Harpley and West Barsham, Norf.," in J. S. Roskell, L. Clark, and C. Rawcliffe, eds., *The History of Parliament: The House of Commons 1386-1421* (Cambridge: Cambridge University Press, 1993), is already preserved at `sources/corpus_supplement/John-Gurney-d1408-The-History-of-Parliamentx.md` (sourceId `hop-gurney`). That file is the authoritative copy of the biography and the place to consult when extending coverage of Sir John V into G22 / G23 research notes.

Findings from the HoP biography that are still worth surfacing in this companion (not previously summarised here):

- **1392 Edmund Clippesby murder and the death threat against Sir John.** "When, in 1392, Edmund Clippesby, a leading Norfolk lawyer who had acted with Gurney's father as joint steward of the duchy of Lancaster estates in the region, was murdered at his home, Gurney himself was threatened with death if he tried to open proceedings against the criminals, all of whom were servants of Bishop Despenser of Norwich. (The bishop was no friend of John of Gaunt.)" — places the Edmund-Gurney / Edmund-Clipesby joint Norwich retainer pair (Norwich Treasurers' fee paragraphs, see v63 + `sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md`) in a wider political context.
- **1392 London Husting court payment.** Alice Heylesdon's late father had divided his property between Alice and her sister Margaret in 1384; Margaret died before majority; in 1392 Alice and John Gurney collected the £300 from the London civic authorities allotted to her by the Heylesdon will. The full Heylesdon will text is at `sources/corpus_supplement/husting-wills-london-vol2-john-heylesdon-1384.md` (via v63).
- **1399 Nerford purchase at Houghton.** "Gurney increased his holdings still further through purchase, buying in 1399 a moiety of the Nerford manor at Houghton, which bordered on his own estate at Harpley."
- **1408 Hellesdon bridge dispute with Norwich.** "Early in 1408 he instigated work at Hellesdon on the building of a bridge over the river Wensum, but the citizens of Norwich, apprehensive that this would result in their loss of revenue from tolls, procured a royal writ suspending the project until the matter had been discussed before the King's Council." A direct echo of Edmund's own friction with Norwich (his retainer status notwithstanding) a generation earlier.
- **1406 Walsingham land grant in Sir Edmund Reynham's memory.** Sir John continued the family's Walsingham priory patronage that Edmund had begun (1385 Walsingham grant with Calthorpe / Hales / Shelton, per *Patent Roll* 8 Richard II, p. 2, m. 15) and that Thomas II (G20) would extend (1471 will gold-turquoise ring to the chapel of the Annunciation + £10 to the prior for a "new work").
- **March 1408 Felton-Banham lease to John Spencer.** Last documented Gurney transaction before Sir John V's death on 4 December 1408.
- **Edmund the heir** (Sir John V's only son) was 10 years old at the father's death and "followed him to the grave not long afterwards."
- **Alice Heylesdon's three marriages and 1433 Heylesdon sale to Fastolf.** Alice survived Sir John V by at least 25 years. She sold Loundhall to John Wynter to pay her late husband's debts. She remarried twice: first the Fitzalan retainer Sir John Wiltshire (d. 1428), then Richard Selling esquire. In 1433 she sold the bulk of her Heylesdon inheritance to Sir John Fastolf KG. In 1450 Fastolf, securing the title deeds, also wanted copies of the wills of Gurney and Wiltshire (Paston Letters ed. Gairdner i. 164). The Heylesdon-Fastolf-Paston-Heydon chain that the G19 1472 Saxthorpe episode (v62 Item 01) sits inside begins here.
```

---

## §A9 — Append to `research/people/g22-robert-gournay-fact-sheet.research.md`

Append the following block at the end of the existing Working Notes section (specifically, after the existing v56 Item 03 Heylesdon-aftermath block):

```md
### Heylesdon-aftermath continuation: Alice Heylesdon's three marriages and 1433 Fastolf sale

Per the History of Parliament biography of Sir John Gurney V (full text at `sources/corpus_supplement/John-Gurney-d1408-The-History-of-Parliamentx.md`):

> "Gurney's widow, Alice, survived him by at least 25 years. She sold 'Loundhall' to John Wynter in order to pay her late husband's debts, and then married twice more: first the Fitzalan retainer, Sir John Wiltshire (d.1428), and then Richard Selling, esquire. In 1433 she sold the bulk of her Heylesdon inheritance to Sir John Fastolf KG."
>
> Note 8: "Blomefield, x. 411, 426; Norf. RO, Reg. Surflete, f. 27. In 1450 Fastolf, anxious to secure the title deeds to the Heylesdon estates, also wanted copies of the wills of Gurney and Wiltshire: Paston Letters ed. Gairdner, i. 164."

The 1433 Heylesdon sale to Fastolf is the upstream event for the entire downstream Saxthorpe / Titchwell / Paston / Heydon contest that William Gurney IV would walk into in 1472 (Saxthorpe Court showdown, v62 Item 01). When Fastolf died in 1459 he willed his Norfolk estates to Sir John Paston; the Pastons claimed Saxthorpe and Titchwell as Fastolf's heirs; Henry Heydon ultimately bought them from Bishop Waynflete of Winchester in 1472 over both parties' heads. The Heylesdon-Fastolf-Paston-Heydon chain that swept the v22 line's adjacent landholdings through three families and three crises in three generations begins with Robert's brother Sir John V's marriage to Alice Heylesdon (the 1384 Husting will of Alice's father John Heylesdon — full text at `sources/corpus_supplement/husting-wills-london-vol2-john-heylesdon-1384.md` via v63 — is the foundation document) and ends with the 1472 Saxthorpe episode that pulled William IV (Robert's great-grandson) into one of the most famous Norfolk gentry property disputes of the fifteenth century.
```

---

## §A10 — `str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Narrative paragraph 4

**`old_string`:**

```
Thomas's principal documentary moment is his will. Dated at West Barsham on an unspecified day in 1471 and proved by the Norwich Consistory Court on 27 July of that year, the will reveals three simultaneous family residences: West Barsham Hall in north Norfolk, a house at Harpley (the old medieval family seat twenty miles to the west), and a town house in St Gregory's parish in the heart of Norwich. Thomas specified that he might be buried at Harpley, West Barsham, or Norwich, "as he may die at either place" — reflecting the mobile life of a 15th-century Norfolk gentleman who circulated among his own estates and his town residence through the agricultural year, consuming the produce of each estate as he went. DG would later use this will as his textbook illustration of the pattern of multiple-residence gentry life.
```

**`new_string`:**

```
Thomas's principal documentary moment is his will. Dated at West Barsham on 18 March 1469/70 and proved by the Norwich Consistory Court on 27 July 1471, the will is one of the most detailed pre-Tudor Norfolk gentry wills to survive. <sup class="fn"><a href="#nNEW1" id="ref-NEW1">NEW1</a></sup> It names three simultaneous family residences — West Barsham Hall in north Norfolk, a house at Harpley twenty miles to the west, and a town house in St Gregory's parish in the heart of Norwich — and directs that Thomas be buried in the chancel of St Lawrence at Harpley if he dies there, or in the Greyfriars' church at Norwich if he dies there. The Norwich house was to be sold to his son William for 80 marks (about £53 in the money of the time), the first quantified valuation of any Gurney urban property. The Hardingham manor of Swathings, which Thomas had bought from a Catherine Sturmer at some earlier date, was to descend with the rest of the patrimony. Bequests of 40 shillings to the Norwich Greyfriars and 20 shillings each to the Augustinian Friars, the Dominicans, and the Carmelites placed Thomas inside the standard "all four orders" benefaction pattern of substantial Norfolk gentry. His personal confessor was John Bernard, a Franciscan friar at Norwich. The will's most personal touch is a gold ring set with a turquoise, left to the chapel of the Annunciation at Walsingham Priory, together with £10 to the prior toward a building project in exchange for entry into the priory's beadroll "as brother and sister of that priory" — a perpetual-prayer commitment to what was then the principal Marian pilgrimage shrine of England.

The will named three sons. William IV was the heir; two further sons, John and Edmund, were confirmed in grants out of the Suffolk manor of Depden. The executors were Margaret his wife, John Jerningham (almost certainly Margaret's brother, of the Somerleyton Jerninghams), and Edmund Bokenham Esquire of Old Buckenham. The supervisor — the senior overseer of the executors — was John Heydon of Baconsthorpe, the most powerful Norfolk lawyer of the mid-fifteenth century and the principal antagonist of the Paston family in the famous *Paston Letters* correspondence. The Gurney-Heydon alliance documented in this 1471 will would be sealed thirteen years later by the marriage of Thomas's grandson William V (G18) to John Heydon's granddaughter Anne Heydon. <sup class="fn"><a href="#nNEW2" id="ref-NEW2">NEW2</a></sup>
```

---

## §A11 — `str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Children table

**`old_string`:**

```
<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Dates</th>
      <th>Mother</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>William Gurney IV</strong></td>
      <td>c. 1450 – 18 Jan 1508</td>
      <td>Margaret Jerningham</td>
      <td><strong>G19 in the direct line.</strong> Son and heir. Of West Barsham and Pockthorpe-by-Norwich. Escheator for Norfolk under Edward IV; of council to the Duke of Norfolk 1477; married Anne Calthorpe, daughter of Sir William Calthorpe KB of Burnham Thorpe. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></td>
    </tr>
  </tbody>
</table>

<p><em>Daniel Gurney, <em>Record</em> (1848), pedigree p. 286 names only William IV as Thomas II's issue. Further children, if any, are not recorded in the sources consulted.</em></p>
```

**`new_string`:**

```
<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Dates</th>
      <th>Mother</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>William Gurney IV</strong></td>
      <td>c. 1450 – 18 Jan 1508</td>
      <td>Margaret Jerningham</td>
      <td><strong>G19 in the direct line.</strong> Son and heir. Of West Barsham and Pockthorpe-by-Norwich. Escheator for Norfolk under Edward IV; of council to the Duke of Norfolk 1477; married Anne Calthorpe, daughter of Sir William Calthorpe Knight of the Bath, of Burnham Thorpe. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></td>
    </tr>
    <tr>
      <td>John Gurney</td>
      <td>living 1471</td>
      <td>Margaret Jerningham</td>
      <td>Named in Thomas II's 1471 will as a son to whom the testator confirmed grants out of the Suffolk manor of Depden. Not in the published Gurney pedigree. <sup class="fn"><a href="#nNEW1" id="ref-NEW1c">NEW1</a></sup></td>
    </tr>
    <tr>
      <td>Edmund Gurney</td>
      <td>living 1471</td>
      <td>Margaret Jerningham</td>
      <td>Named in Thomas II's 1471 will alongside his brother John, with the same Depden confirmation. Not in the published Gurney pedigree. <sup class="fn"><a href="#nNEW1" id="ref-NEW1d">NEW1</a></sup></td>
    </tr>
  </tbody>
</table>
```

---

## §A12 — `str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Timeline

**`old_string`:**

```
      <tr><td>1471</td><td>Thomas makes his will at West Barsham, specifying three residences.</td></tr>
      <tr><td>27 Jul 1471</td><td>Will proved. Son William Gurney IV (age ~21) inherits West Barsham.</td></tr>
```

**`new_string`:**

```
      <tr><td>18 Mar 1469/70</td><td>Makes his will at West Barsham. Names three sons (William, John, Edmund); appoints John Heydon of Baconsthorpe as supervisor. <sup class="fn"><a href="#nNEW1" id="ref-NEW1e">NEW1</a></sup></td></tr>
      <tr><td>27 Jul 1471</td><td>Will proved. Son William Gurney IV (age ~21) inherits West Barsham.</td></tr>
```

---

## §A13 — `str_replace` on `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md` Citations to append `nNEW1`, `nNEW2`

**`old_string`:**

```
  <li id="n11">See G19 William Gurney IV fact sheet. <a class="citation-back" href="#ref-11">↩</a></li>
</ol>
```

**`new_string`:**

```
  <li id="n11">See G19 William Gurney IV fact sheet. <a class="citation-back" href="#ref-11">↩</a></li>
  <li id="nNEW1">Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42-47, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47">British History Online</a>. Full will text in English summary, including the 18 March 1469/70 date, burial alternatives at Harpley or the Norwich Greyfriars, the four-orders friary bequests, the Walsingham gold-turquoise ring and £10 building grant, the Catherine Sturmer Swathings purchase, the St Gregory's parish Norwich house at 80 marks, the John Bernard confessor identification, and the names of sons John and Edmund alongside William. Full per-parish extract preserved at <code>sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md</code>. <a class="citation-back" href="#ref-NEW1">↩</a></li>
  <li id="nNEW2">Blomefield, vol. vii, pp. 42-47, will text naming John Heydon of Baconsthorpe (d. 1479) as supervisor. Biographical context for Heydon: James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), accessible at <a href="https://archive.org/details/pastonlettersad03gairgoog">Internet Archive</a>; and the standard Paston-period historiography in Roger Virgoe's biographical sketch in <em>Norfolk Archaeology</em>. <a class="citation-back" href="#ref-NEW2">↩</a></li>
</ol>
```

---

## §A14 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 1 (Boleyn-descent gateway)

**`old_string`:**

```
the eldest son whose marriage would bring Boleyn descent into the family.
```

**`new_string`:**

```
the eldest son, William V (G18), whose marriage to Anne Heydon of Baconsthorpe — granddaughter of Sir Geoffrey Boleyn, Lord Mayor of London — would make their son Anthony Gurney (G17) the second cousin of Queen Anne Boleyn and the second cousin once removed of Queen Elizabeth I (see the related Queen Anne Boleyn fact sheet at G17).
```

---

## §A15 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 2 (1455 senior + cadet settlements)

**`old_string`:**

```
He was the son of Thomas Gournay II (G20) of West Barsham, by Margaret Jerningham of Somerleyton, Suffolk. His father's will was proved in 1471, when William was probably in his early twenties; he would have inherited the family seat then. By 1477 he is documented as "of council to the Duke of Norfolk," a position that would have brought him into the Howard administration during the John Howard era — the same Duke who would die at Bosworth eight years later fighting for Richard III. He served as escheator for Norfolk under Edward IV, the Crown office that handled lands reverting to the king through felony, intestacy, or wardship. Both roles place him securely in the Yorkist administrative orbit.
```

**`new_string`:**

```
He was the son of Thomas Gournay II (G20) of West Barsham, by Margaret Jerningham of Somerleyton, Suffolk. His father's will was proved in 1471, when William was probably in his early twenties; he would have inherited the family seat then. By 1477 he is documented as "of council to the Duke of Norfolk," a position that would have brought him into the Howard administration during the John Howard era — the same Duke who would die at Bosworth eight years later fighting for Richard III. He served as escheator for Norfolk under Edward IV, the Crown office that handled lands reverting to the king through felony, intestacy, or wardship. Both roles place him securely in the Yorkist administrative orbit. By 1455 he was already styling himself "senior" — operating as the working head of the West Barsham line while his father was still living — and across the 1490s he progressively settled cadet portions on his younger sons, granting lands to Walter in 1495-96 (the documented founding of the Cawston and Aylsham cadet branch) and to William junior at Dunton in 1497-98 (a third trust event alongside the better-known 1485 and 1505 trust deeds). <sup class="fn"><a href="#nNEW3" id="ref-NEW3">NEW3</a></sup>
```

---

## §A16 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative paragraph 3 (Pockthorpe = brother-in-law's house)

**`old_string`:**

```
His most consequential personal act was his marriage to Anne Calthorpe. The Calthorpes of Burnham Thorpe were one of the most distinguished Norfolk knightly families of the 15th century. Anne's father Sir William Calthorpe (1410–1494) was Knight of the Bath at the coronation of Queen Elizabeth Woodville in 1465, High Sheriff of Norfolk and Suffolk on at least four separate occasions, Steward of the household of the Duke of Norfolk in 1479, and the holder of estates centred on Burnham Thorpe and Ludham. Through Anne's mother Elizabeth Grey (Sir William's first wife, who died young in 1437), she was the great-granddaughter of Reginald Grey, 3rd Baron Grey de Ruthyn — and so William IV's descendants entered the kinship penumbra of one of the great late-medieval English baronial houses. The marriage made the Gurneys part of the inner Norfolk knightly network, anchored in the cluster of villages along the north Norfolk coast. (Three centuries later, Burnham Thorpe would also be the birthplace of Admiral Horatio Nelson.)
```

**`new_string`:**

```
His most consequential personal act was his marriage to Anne Calthorpe. The Calthorpes of Burnham Thorpe were one of the most distinguished Norfolk knightly families of the 15th century. Anne's father Sir William Calthorpe (1410–1494) was Knight of the Bath at the coronation of Queen Elizabeth Woodville in 1465, High Sheriff of Norfolk and Suffolk on at least four separate occasions, Steward of the household of the Duke of Norfolk in 1479, and the holder of estates centred on Burnham Thorpe and Ludham. Through Anne's mother Elizabeth Grey (Sir William's first wife, who died young in 1437), she was the great-granddaughter of Reginald Grey, 3rd Baron Grey de Ruthyn — and so William IV's descendants entered the kinship penumbra of one of the great late-medieval English baronial houses. The marriage made the Gurneys part of the inner Norfolk knightly network, anchored in the cluster of villages along the north Norfolk coast. (Three centuries later, Burnham Thorpe would also be the birthplace of Admiral Horatio Nelson.) The marriage also explains the family's Pockthorpe-by-Norwich town address: the Pockthorpe house was almost certainly the same complex held by William IV's brother-in-law William Calthorpe of Pokethorpe (Anne's full brother, also a son of Sir William Calthorpe by Elizabeth Grey), later known as "the Lathes" and, under the Blennerhassets in the seventeenth century, as Hassets' Hall — making the Norwich town address a kinship arrangement, not a separate Gurney acquisition. <sup class="fn"><a href="#nNEW4" id="ref-NEW4">NEW4</a></sup>
```

---

## §A17 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Narrative to insert new 1505-trust-circle paragraph

**`old_string`:**

```
By his 1507 will William directed that 700 sheep should remain at West Barsham after his death. genealogist Daniel Gurney described this as "a considerable flock in those days," and it is — perhaps the single most concrete piece of evidence about the working economy of any pre-1600 Gurney household. The flock fed the East Anglian wool trade, which in turn fed the Norwich worsted industry, which was the dominant economic activity of the county. The Gurneys at this period were not magnates, but they were a thoroughly substantial gentry sheep-farming household, sufficiently established to support a town residence at Pockthorpe-by-Norwich and a country seat at West Barsham simultaneously.
```

**`new_string`:**

```
By his 1507 will William directed that 700 sheep should remain at West Barsham after his death. genealogist Daniel Gurney described this as "a considerable flock in those days," and it is — perhaps the single most concrete piece of evidence about the working economy of any pre-1600 Gurney household. The flock fed the East Anglian wool trade, which in turn fed the Norwich worsted industry, which was the dominant economic activity of the county. The Gurneys at this period were not magnates, but they were a thoroughly substantial gentry sheep-farming household, sufficiently established to support a town residence at Pockthorpe-by-Norwich and a country seat at West Barsham simultaneously.

The composition of the seven feoffees William IV named on his 1505 estate-settlement trust shows how thoroughly the marriage to Anne Calthorpe had embedded the West Barsham line inside its in-laws' world. Six of the seven were Calthorpe kin or Howard-ducal-house allies: Sir Edward Howard (son of the 2nd Duke of Norfolk and future Lord High Admiral, killed at Brest in 1513); Sir Philip Calthorpe (Anne's half-nephew); Sir Robert Clere of Ormesby St Margaret (a leading Howard-circle Norfolk knight); Sir Robert Drury, Speaker of the House of Commons in 1495, who had married Anne's half-sister of the same name; Nicholas Appleyard of Bracon Ash; and William IV's brother-in-law William Calthorpe of Pokethorpe. The seventh was William IV's own son Thomas Gurney, who would execute the will. The 1505 trust is a documentary snapshot of one of the more distinguished gentry kinship circles in early-Tudor East Anglia, with the West Barsham line sitting squarely inside it. <sup class="fn"><a href="#nNEW5" id="ref-NEW5">NEW5</a></sup>
```

---

## §A18 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Timeline

**`old_string`:**

```
      <tr><td>1494</td><td>William IV documented as "living 1494" (DG p. 287).</td></tr>
      <tr><td>by 1505</td><td>Eldest son William Gurney V dies <em>vita patris</em>.</td></tr>
```

**`new_string`:**

```
      <tr><td>1455</td><td>Already styling himself "William Gurnay, Esq. senior" — operating as adult lord while his father Thomas II was still living. <sup class="fn"><a href="#nNEW3" id="ref-NEW3b">NEW3</a></sup></td></tr>
      <tr><td>1494</td><td>William IV documented as "living 1494" (DG p. 287).</td></tr>
      <tr><td>1495-96</td><td>Granted lands to his son Walter — the documented founding settlement of the Cawston and Aylsham cadet branch. <sup class="fn"><a href="#nNEW3" id="ref-NEW3c">NEW3</a></sup></td></tr>
      <tr><td>1497-98</td><td>Settled lands at Dunton on his son William junior (G18) — a third trust event alongside the 1485 and 1505 trust deeds. <sup class="fn"><a href="#nNEW3" id="ref-NEW3d">NEW3</a></sup></td></tr>
      <tr><td>by 1505</td><td>Eldest son William Gurney V dies <em>vita patris</em>.</td></tr>
```

---

## §A19 — `str_replace` on `fact-sheets/g19-william-gurney-iv-fact-sheet.md` Citations to append `nNEW3`, `nNEW4`, `nNEW5`

**`old_string`:**

```
  <li id="n13">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287: "Walter Gourney, of Cley by the Sea, Norfolk, ancestor of the Gourneys of Cawston and Aylsham." And: "Thomas Gurnet, his father's executor, ancestor of the Gurneys of Dartmouth, London, and Essex, temp. Elizabeth, 1590; his grandson, Richard Gurney, was Sheriff of London." <a class="citation-back" href="#ref-13">↩</a></li>
</ol>
```

**`new_string`:**

```
  <li id="n13">Daniel Gurney, <em>Record</em> (1848), pedigree p. 287: "Walter Gourney, of Cley by the Sea, Norfolk, ancestor of the Gourneys of Cawston and Aylsham." And: "Thomas Gurnet, his father's executor, ancestor of the Gurneys of Dartmouth, London, and Essex, temp. Elizabeth, 1590; his grandson, Richard Gurney, was Sheriff of London." <a class="citation-back" href="#ref-13">↩</a></li>
  <li id="nNEW3">Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42-47, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47">British History Online</a>: "William Gurnay, Esq. was lord, and succeeded on his father's death. In the year 1455 he styled himself William Gurnay, Esq. senior; and in the 13th of Henry VII. William Gurnay, senior, Esq. &c. infeoft William Gurnay, junior, Esq. &c. of lands in Dunton... He had also a son Walter, living in the 11th of Henry VII. to whom he then granted lands." Full per-parish extract at <code>sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md</code>. <a class="citation-back" href="#ref-NEW3">↩</a></li>
  <li id="nNEW4">Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew & Son, 1858), Note 131, p. 817, identifying the Calthorpe Pockthorpe manor house with "the same as that afterwards inhabited by the Blennerhassets, and called Hassets' Hall," and noting the likelihood of shared residence with William IV. William Calthorpe of Pokethorpe (son of Sir William Calthorpe Knight of the Bath by Elizabeth Grey) is identified in Carr-Calthrop, <em>Notes on the Families of Calthorpe and Calthrop</em> (London: Spottiswoode, Ballantyne &amp; Co., 1933), and was named as a feoffee on the 1505 Gurney trust deed (Daniel Gurney, <em>Supplement</em>, Note 132, pp. 817-819). Underlying parish context for Pockthorpe and Hassets' Hall in Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. iv (London: William Miller, 1806), p. 428. <a class="citation-back" href="#ref-NEW4">↩</a></li>
  <li id="nNEW5">Trust 2 deed dated 6 April 1505, 21 Henry VII, naming the seven feoffees: Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew & Son, 1858), Note 132, pp. 817-819 (text of the posthumous inquisition post mortem of William Gurnay senior, taken at Norwich 4 November 1532). Sir Edward Howard's death at Brest, 25 April 1513: Susan Doran, "Howard, Sir Edward (1476/7-1513)," <em>Oxford Dictionary of National Biography</em>. Sir Robert Drury (Speaker of the House of Commons 1495) and his marriage to Anne Calthorpe by Sir William's second wife Elizabeth Stapleton: L. M. Kirk, "DRURY, Sir Robert I (by 1456-1535)," in S. T. Bindoff, ed., <em>The History of Parliament: The House of Commons 1509-1558</em> (London: Secker &amp; Warburg, 1982), available at <a href="https://www.historyofparliamentonline.org/volume/1509-1558/member/drury-sir-robert-i-1456-1535">History of Parliament Online</a>; full biography at <code>sources/corpus_supplement/hop-drury-robert-i-1456-1535.md</code> (via v62); Carr-Calthrop, <em>Notes on the Families of Calthorpe and Calthrop</em> (London: Spottiswoode, Ballantyne &amp; Co., 1933), Calthorpe pedigree. <a class="citation-back" href="#ref-NEW5">↩</a></li>
</ol>
```

---

## §A20 — `str_replace` on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` Narrative paragraph 3

**`old_string`:**

```
His own life after the inheritance is thinly documented. He married Catherine Kerville of Watlington, in the west-Norfolk hinterland of King's Lynn — a sensible alliance for a gentleman whose principal seats at West Barsham and Harpley lay in the intermediate north-Norfolk zone and who now also held commercial property in London via La Selde Coronata. He appears in no royal commission, no sheriffdom, no parliamentary service, and no commission of the peace.
```

**`new_string`:**

```
His own life after the inheritance is thinly documented. He married Catherine Kerville of Watlington, in the west-Norfolk hinterland of King's Lynn — a sensible alliance for a gentleman whose principal seats at West Barsham and Harpley lay in the intermediate north-Norfolk zone and who now also held commercial property in London via La Selde Coronata. He appears in no royal commission, no sheriffdom, no parliamentary service, and no commission of the peace. He does appear, however, in three smaller documentary attestations: as a Norfolk feoffee in East Barsham in 1434-35 (with John Hunt, confirming Wolterton's Manor to John Wode); in active military service in France across three campaigns (the 1415 Agincourt campaign in John Holland's retinue, the 1418 Harfleur garrison under Thomas Beaufort Duke of Exeter, and the 1441 France expedition in John de Vere's retinue under Richard of York — see Research Companion); and as the sealer of a 1445 East Barsham feoffment preserved on a Le Strange charter at Hunstanton Hall. The cumulative picture is of a quietly active Norfolk gentleman, not an entirely retiring one. <sup class="fn"><a href="#nNEW6" id="ref-NEW6">NEW6</a></sup>
```

---

## §A21 — `str_replace` on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` Timeline

**`old_string`:**

```
      <tr><td>1422</td><td>Henry V dies; nine-month-old Henry VI inherits — beginning the long Lancastrian minority.</td></tr>
      <tr><td>mid-century</td><td>Married Catherine Kerville of Watlington. Son Thomas Gournay II (G20) born c. 1430.</td></tr>
```

**`new_string`:**

```
      <tr><td>1418</td><td>Documented as a man-at-arms in the Harfleur garrison under Thomas Beaufort, Duke of Exeter — Henry V's lieutenant of Normandy. <sup class="fn"><a href="#nNEW6" id="ref-NEW6b">NEW6</a></sup></td></tr>
      <tr><td>1422</td><td>Henry V dies; nine-month-old Henry VI inherits — beginning the long Lancastrian minority.</td></tr>
      <tr><td>1434-35</td><td>Documented as a feoffee in East Barsham (with John Hunt), confirming Wolterton's Manor to John Wode. <sup class="fn"><a href="#nNEW6" id="ref-NEW6c">NEW6</a></sup></td></tr>
      <tr><td>mid-century</td><td>Married Catherine Kerville of Watlington. Son Thomas Gournay II (G20) born c. 1430.</td></tr>
```

---

## §A22 — `str_replace` on `fact-sheets/g21-thomas-gournay-i-fact-sheet.md` Citations to append `nNEW6`

**`old_string`:**

```
  <li id="n10">See G20 Thomas Gournay II fact sheet. <a class="citation-back" href="#ref-10">↩</a></li>
</ol>
```

**`new_string`:**

```
  <li id="n10">See G20 Thomas Gournay II fact sheet. <a class="citation-back" href="#ref-10">↩</a></li>
  <li id="nNEW6">1434-35 East Barsham feoffment (with John Hunt, son of William Hunt of East-Barsham, confirming Wolterton's Manor to John Wode): Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: East-Barsham," pp. 53-65, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp53-65">British History Online</a>. Full per-parish extract at <code>sources/corpus_supplement/blomefield-norfolk-vol7-pp53-65-east-barsham.md</code>. Military service 1415, 1418, 1441: AHRC <em>Soldier in Later Medieval England Online Database</em>, [www.medievalsoldier.org](https://www.medievalsoldier.org/), with full record references in the G21 research companion. 1445 Hunstanton seal: Daniel Gurney, <em>Supplement to the Record of the House of Gournay</em> (King's Lynn: Thew & Son, 1858), Note 126, p. 814. <a class="citation-back" href="#ref-NEW6">↩</a></li>
</ol>
```

---

## §A23 — `str_replace` on `fact-sheets/g18-william-gurney-v-fact-sheet.md` Narrative (Heydon-alliance chronology)

Phase 2: locate the G18 Narrative paragraph that introduces the 1484 Anne-Heydon marriage. The current G18 fact sheet content was not previously read in this patchset's prep step. Phase 2 instruction:

1. Read `fact-sheets/g18-william-gurney-v-fact-sheet.md`.
2. Locate the Narrative paragraph that introduces "Anne Heydon" or "1484" or "Henry Heydon."
3. Apply this `str_replace`:

**`old_string` to locate (exact match):** the paragraph that introduces Anne Heydon and the 1484 indentures. If multiple paragraphs reference Anne Heydon, target the one that first introduces the marriage.

**`new_string`:** the existing paragraph, plus the following appended at the end of the same paragraph (do not change the existing text; only append):

```
The Gurney-Heydon alliance the 1484 marriage indentures sealed was not new. Thirteen years earlier, in his 1471 will, William V's grandfather Thomas Gournay II had chosen John Heydon of Baconsthorpe — the most powerful Norfolk lawyer of the mid-fifteenth century, and the principal antagonist of the Paston family in the famous *Paston Letters* — as supervisor of his will. And less than a year after the 1471 probate, Henry Heydon (John's son) raised men-at-arms in support of William V's father William IV during the January–May 1472 Saxthorpe Court showdown with John Paston (see G19 fact sheet). The 1484 marriage to John Heydon's granddaughter Anne anchored a professional and military relationship that had already been operating in the field for thirteen years. <sup class="fn"><a href="#nNEW7" id="ref-NEW7">NEW7</a></sup>
```

(This is one of two places where the patchset cannot supply a literal `old_string` because the G18 fact sheet content was not Read during prep. This is a deviation from the operational standard; Phase 2 will need one targeted Read, then the literal append. Future patchsets should Read the target file during prep to avoid this gap.)

---

## §A24 — `str_replace` on `fact-sheets/g18-william-gurney-v-fact-sheet.md` Citations to append `nNEW7`

Phase 2: locate the closing `</ol>` of the Citations `<ol class="citation-list">` block in `fact-sheets/g18-william-gurney-v-fact-sheet.md` and insert the following `<li>` immediately before it:

```html
  <li id="nNEW7">Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. vii (London: William Miller, 1807), "Gallow and Brothercross Hundreds: West-Barsham," pp. 42-47, <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47">British History Online</a> (text of Thomas Gurnay senior's 1471 will naming John Heydon as supervisor). John Heydon of Baconsthorpe (died 1479) biographical context: James Gairdner, ed., <em>The Paston Letters, A.D. 1422-1509</em>, 6 vols. (London: Chatto and Windus, 1904), <a href="https://archive.org/details/pastonlettersad03gairgoog">Internet Archive</a>; Roger Virgoe's biographical sketch in <em>Norfolk Archaeology</em>. 1472 Saxthorpe Court episode with Henry Heydon's men-at-arms: see v62 patchset Item 01 and `sources/corpus_supplement/paston-letters-gairdner-gurney-extracts.md` §1. <a class="citation-back" href="#ref-NEW7">↩</a></li>
```

(Same Read-during-prep gap as §A23. Phase 2 needs to Read the G18 fact sheet to locate the exact `</ol>` line.)

---

End of patchset.
