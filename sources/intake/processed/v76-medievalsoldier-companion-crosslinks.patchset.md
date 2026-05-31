# v76 — Medieval-soldier discovery: research-companion cross-links

**Scope:** Phase 2 application. Continues the 2026-05-30 medieval-soldier arc (see v75 for the topic file, the two new sources, and the G22/Somerset landings). This patchset lands the cross-links and resolutions in the three remaining direct-line companions: **G23 Edmund** (the Gaunt-affinity enrichment + resolution of the long-standing "separate earlier knight John de Gournay" question), **G24 John IV** (the soldier-database knight cluster is Somerset, not him), and **G21 Thomas I** (the Harfleur-parallel cadet cross-note).

No new sourceIds (all cited sources — `walker-lancastrian-affinity-1361-1399`, `hull-thesis-english-way-of-war-1360-1399`, `medievalsoldier-database`, `hop-gurney` — are already registered or queued in v75).

**Deferred to v77** (fact-sheet promotions): `fact-sheets/g23-edmund-gurney-fact-sheet.md` (Gaunt-retained adviser of Lynn / St Benet's Holme fee — the primary promotion) and, secondarily, `fact-sheets/g29-matthew-de-gournay-fact-sheet.md` (banneret service rows + Trevet kinship).

---

## Item 01 — Append Gaunt-affinity finding + knight-cluster resolution to `research/people/g23-edmund-gurney-fact-sheet.research.md`

**Outcome:** promote. **Operation:** `str_replace` (append after the final footnote in the file).

This both adds the new Walker finding and resolves the companion's existing Open Question 6 and the 1394-section note that an unidentified "separate, earlier knight John de Gournay" lay behind the 1370 Knolles captaincy.

**old_string:**
```
[^v71-armstrong-1373-west-barsham]: Armstrong, *Norfolk*, vol. 5, Gallow — West Barsham parish entry. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

**new_string:**
```
[^v71-armstrong-1373-west-barsham]: Armstrong, *Norfolk*, vol. 5, Gallow — West Barsham parish entry. Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.

---

### Edmund in John of Gaunt's retained East Anglian affinity — St Benet's Holme fee (added 2026-05-30)

Simon Walker's study of the Lancastrian affinity places Edmund inside John of Gaunt's retained body of East Anglian legal-administrative men, with detail beyond the History-of-Parliament "steward of Gaunt's East Anglian estates" framing already in this companion. Edmund was "the principal legal adviser to the burgesses of Lynn," and — with Edmund Clippesby — "took fees from the abbey of St. Benet's, Holme." Walker brackets the two in a cohort of Gaunt's retained Norfolk administrators: John Winter (the Wynter later central to the Loundhall/Saxthorpe enfeoffment), Robert Cayley (Exchequer attorney for Norwich and steward to the bishop of Norwich), Thomas Pinchbeck (steward to the bishop of Ely), and John Methwold (agent for the canons of West Dereham).[^v76-walker-edmund-affinity]

This sharpens the existing Edmund–Clippesby retainer-pair material in this companion (the Norwich Treasurers' fee paragraphs and the 1392 Clippesby murder). The pairing was not incidental: the two appear together both as Gaunt's St Benet's Holme fee-takers and as Norwich's standing counsel, which is why Clippesby's 1392 murder by Bishop Despenser's servants — and the death threat against Sir John V if he prosecuted — sat on the Gaunt-versus-Despenser fault line. Walker's note cites the primary records behind the fees (Staffordshire RO D.641/1/2/4 m.4; TNA E.403/478 m.16; HMC *MSS of the Corporations of Southampton and King's Lynn* (1887) pp.221-2; CPR 1381-5 p.380; KB 9/166/1 m.69), carried as lead L-77.

### The "separate, earlier knight John de Gournay" is resolved — Sir John de Gourney of Harptree, Somerset (added 2026-05-30)

The 1394 working note above, and Open Question 6, flagged that the 1370s "John de Gournay" knight entries — and in particular the 1370 captaincy in Sir Robert Knolles' chevauchée (TNA E101/30/25), "too senior to be the future Sir John V" — pointed to a "separate, earlier knight John de Gournay" whose identity was unresolved. That man is now identified: **Sir John de Gourney of (East) Harptree, Somerset**, owner of Harptree castle from 1343, who served in Ireland (1363, under Sir William de Windsor), captained his own small retinue under Knolles in 1370, and held the Calais garrison under Calveley (1376) and Brocas (1378); he married Elizabeth, widow of John Carew.[^v76-hull-harptree] He is a Somerset collateral, distinct from both Sir John Gurney V (the future d.1408) and from the regicide-line Sir Matthew de Gournay. The 1370 Knolles captaincy and the bulk of the 1363–1378 knight cluster therefore belong to the Somerset branch, not the Norfolk direct line; only the stray 1359 Reims protections (TNA C76/38) remain unattached by name and are most parsimoniously the same Harptree John. The full reasoning and the geography triage are in [`research/topics/gurney-medieval-soldier-database.md`](../topics/gurney-medieval-soldier-database.md); the Somerset knight is carried in [`research/places/somerset-gournay-collateral.md`](../places/somerset-gournay-collateral.md). Open Question 6 is resolved by this identification.

[^v76-walker-edmund-affinity]: Simon Walker, *The Lancastrian Affinity 1361–1399* (Oxford: Clarendon Press, 1990), n.19: Edmund Gournay "the principal legal adviser to the burgesses of Lynn," who with Edmund Clippesby "took fees from the abbey of St. Benet's, Holme," bracketed with John Winter, Robert Cayley, Thomas Pinchbeck, John Methwold; citing Staffordshire RO D.641/1/2/4 m.4; TNA E.403/478 m.16; HMC *MSS of the Corporations of Southampton and King's Lynn* (1887) pp.221-2; CPR 1381-5 p.380; KB 9/166/1 m.69. Source ID: `walker-lancastrian-affinity-1361-1399`.

[^v76-hull-harptree]: 'The English Way of War, 1360–1399' (PhD thesis, University of Hull), appendix p.340, entry "GOURNEYE John, Sir" (owner of Harptree castle, Somerset, 1343 underage; Ireland 1363 under William de Windsor; Knolles 1370 captain; Calais garrison 1376/1378 under Calveley/Brocas; m. Elizabeth widow of John Carew, CPR 1370-74 p.21) and Knolles retinue table p.341. Source ID: `hull-thesis-english-way-of-war-1360-1399`.
```

---

## Item 02 — Append knight-cluster clarification to `research/people/g24-john-de-gournay-iv-fact-sheet.research.md`

**Outcome:** promote. **Operation:** `str_replace` (append after the final line of the file).

**old_string:**
```
3. **Post-plague context:** A sentence noting that the 1354 court was held just five years after the Black Death would add historical weight.
```

**new_string:**
```
3. **Post-plague context:** A sentence noting that the 1354 court was held just five years after the Black Death would add historical weight.

---

### The soldier-database "Sir John de Gournay" knight is not G24 (added 2026-05-30)

A knight named Sir John de Gournay served in arms across 1359–1378 (Reims protections, a retinue captaincy under Sir Robert Knolles in 1370, the Calais garrison under Calveley and Brocas) and appears in the *Soldier in Later Medieval England* database. The chronology is a near-perfect fit for G24 — born c. 1330, he would have been about 29 at Reims, 40 under Knolles, and 48 at Calais, and the fact sheet's "died c. 1370 or later" leaves room — and the family had a knightly tradition (G27 Sir John de Gournay I, the crusader). G24 being recorded only as a Harpley manorial lord does not by itself exclude military service. The identification is nonetheless **negative**: the soldier knight is Sir John de Gourney of (East) Harptree, Somerset (owner of Harptree castle 1343; m. Elizabeth widow of John Carew), and his theatre — Reims, Knolles' northern-France chevauchée, the Calais garrison — is the royal northern theatre, not the Gascony/Aquitaine theatre of the Somerset banneret Sir Matthew.[^v76-hull-harptree-g24] G24 therefore remains a Harpley manorial lord with no confirmed military record; the tempting soldier cluster belongs to the Somerset collateral. See [`research/topics/gurney-medieval-soldier-database.md`](../topics/gurney-medieval-soldier-database.md).

[^v76-hull-harptree-g24]: 'The English Way of War, 1360–1399' (PhD thesis, University of Hull), appendix p.340, entry "GOURNEYE John, Sir." Source ID: `hull-thesis-english-way-of-war-1360-1399`. Full reasoning and the soldier-database row set in `research/topics/gurney-medieval-soldier-database.md` (sources `hull-thesis-english-way-of-war-1360-1399`, `medievalsoldier-database`).
```

---

## Item 03 — Append Harfleur-parallel cadet cross-note to `research/people/g21-thomas-gournay-i-fact-sheet.research.md`

**Outcome:** promote. **Operation:** `str_replace` (append after the final footnote in the file).

**old_string:**
```
[^v71-armstrong-1440-woolterton]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred, East Barsham — Woolterton's Manor (full text quoted above). Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.
```

**new_string:**
```
[^v71-armstrong-1440-woolterton]: Mostyn John Armstrong, *The History and Antiquities of the County of Norfolk*, vol. 5 (Norwich, 1781), Gallow Hundred, East Barsham — Woolterton's Manor (full text quoted above). Internet Archive item `bim_eighteenth-century_history-and-antiquities-_armstrong-mostyn-john_1781_5`. Source ID: `armstrong-norfolk-1781`.

---

### A second Gournay in the Harfleur garrison, 1417–18 — possible kinsman (added 2026-05-30)

Alongside Thomas I's own 1418 Harfleur muster under Thomas Beaufort (TNA E101/48/6, already documented above), the *Soldier in Later Medieval England* database carries a **John Gournay**, man-at-arms, in the Harfleur garrison in 1417 (TNA E101/48/17, under Beaufort) and 1418 (TNA E101/48/19, under Sir Hugh Luttrell).[^v76-msd-harfleur-john] A John Gournay holding the same bridgehead garrison as Thomas I, in the same two years, is a plausible brother, cousin, or son in the family's Lancastrian military orbit — but the surname-and-rank match is not by itself an identification, and the membrane (origin, neighbouring names) is the test. Held as lead L-73. This sits with the broader cadet cohort assembled in [`research/topics/gurney-medieval-soldier-database.md`](../topics/gurney-medieval-soldier-database.md), which also notes a John Gurnay under the Norfolk knight Sir Robert Harling at Poissy/Pont-Meulan in 1422 (L-74).

[^v76-msd-harfleur-john]: Soldier in Later Medieval England Online Database: John Gournay, man-at-arms, Harfleur garrison 1417 (TNA E101/48/17, captain/commander Thomas Beaufort) and 1418 (TNA E101/48/19, under Sir Hugh Luttrell); as compiled in `sources/intake/new/gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx`. Source ID: `medievalsoldier-database`.
```

---

## Phase-2 follow-up (record in chat after application, not in this file)

After applying: prepend the `**Done:** YYYY-MM-DD HH:MM PT` stamp and move this file to `sources/intake/done/`. **v77** carries the fact-sheet promotions (G23 Edmund — Gaunt-retained adviser of Lynn / St Benet's Holme; G29 Sir Matthew — banneret service rows + Trevet kinship) and, after that arc closes, archival of the `gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx` workbook out of `sources/intake/new/`.
