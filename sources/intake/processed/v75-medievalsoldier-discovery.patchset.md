# v75 — Medieval-soldier database evaluation + knight/affinity discovery

**Scope:** Phase 2 application of the 2026-05-30 research arc evaluating the `gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx` workbook (in `sources/intake/new/`) against the repo, plus the online discovery that resolved its key open clusters. This patchset lands the **cross-cutting analytical home** (new topic file), the two new sources, their validations, and the two highest-value subject-file additions (G22 companion, Somerset collateral).

**Deferred to v76** (companion cross-links + fact-sheet promotions): the G23 Edmund companion Gaunt-affinity entry, the G24 companion "C11 is Somerset, not G24" note, the G21 companion Harfleur-parallel cross-note, and fact-sheet promotions (G23 Edmund primary; G29 Matthew secondary). The topic file below already carries the full analysis, so the v76 companion edits are cross-links, not the only record.

**New sourceIds (Item 02), each with a default-on validation (Items 03, 04, 04b):**
- `hull-thesis-english-way-of-war-1360-1399` — the Knolles/Sir-John-of-Harptree prosopography
- `walker-lancastrian-affinity-1361-1399` — Edmund in Gaunt's retained affinity / St Benet's Holme
- `hop-berney` — Berney-side network corroboration (independent of `hop-gurney`)
- `trevor-john-erpingham-1970` — scholarly root of the Erpingham/Berney/Gurney bloc + the Gunton question
- `military-communities-knolles-1370` — published corroboration of the Knolles 1370 retinue
- `odnb-matthew-gournay` — independent modern authority for Sir Matthew's Somerset/regicide identity
- `gascon-rolls-project` — finding aid for the C61 Gascony protections
- `hop-harling` — biography of Sir Robert Harling (the 1422 cadet's captain)

These deliberately include **corroborating and related** sources, not only the single best one for each finding, per the multiple-source discipline: e.g. the Knolles identification is anchored to the Hull thesis but corroborated by the published Cambridge chapter; Sir Matthew's Somerset identity already rested on Pettigrew/Tyrwhitt and now also carries ODNB; the Berney network is documented from both `hop-gurney` and the independent `hop-berney`.

Both the soldier-database rows and the workbook are treated as valid per the user's 2026-05-30 instruction; no live re-verification was required.

**Open leads created this arc:** L-72 … L-83 in `research/future-research/research-leads.csv` (already appended).

---

## Item 01 — Create topic file `research/topics/gurney-medieval-soldier-database.md`

**Outcome:** promote. **Operation:** new file write with the full body below.

````markdown
# Gurney / Gournay in the medieval soldier record (c. 1349–1450)

Cross-cutting analysis of the Gurney/Gournay/Gurnay men in the *Soldier in Later Medieval England* database and adjacent military-prosopographical sources, evaluated for what they add to the direct Norfolk line (G24 John de Gournay IV → G23 Edmund → G22 Robert → G21 Thomas I → G20 Thomas II) and its collaterals. The companion data workbook is held at `sources/intake/new/gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx`.

The repo already records G21 Thomas Gournay I's confirmed service (1415 Holland retinue, 1418 Harfleur, 1441 Vere/York) and Sir John Gurney V's 1394 Gaunt service in the paired companions. This file consolidates the **new** findings and the disposition of every other Gournay/Gurney soldier in the dataset.

## The "Sir John de Gourney" knight cluster is Somerset, not the Norfolk line

The database carries a knight named John de Gournay/Gourney serving in arms across 1359–1378: letters of protection and attorney for the Reims theatre, the retinue of Sir Robert Knolles in 1370, and the Calais garrison under Sir Hugh Calveley (1376) and Sir Bernard Brocas (1378).[^msd] The retinue list for Knolles' 1370 expedition (TNA E101/30/25, mm.1–2) records him as a **captain of his own small retinue** (three men-at-arms), alongside Sir John Clanvowe, Sir Hugh le Despenser, Sir Thomas Fogg, and Sir Richard Fyton.[^hull-knolles]

This man is **Sir John de Gourney of (East) Harptree, Somerset** — not the Norfolk direct line. The Hull prosopography of English soldiers 1360–1399 gives his biographical entry: "1343: became owner of Harptree castle, Somerset, while underage; 1363: protection … in the retinue of William de Windsor in Ireland; 1370: protection and attorney for service on Knolles' campaign … 1376: … Calais garrison under Sir Hugh de Calvelay … 1378: … Calais garrison under Sir Bernard Brocas." It adds that he was "from a large and important noble family," married Elizabeth, late wife of John Carew, and is to be distinguished from a separate, later "John Gurney … described as a London mercer" active on the Scottish march in the 1380s–90s.[^hull-john] Harptree is the principal Somerset Gournay seat; the Carew marriage is a West-Country alliance. The whole 1363–1378 military cluster is his.

This resolves a tempting but false lead. The chronology of the Norfolk **G24 John de Gournay IV** (born c. 1330, lord of Harpley, holding his first manorial court there in 1354, death given as "c. 1370 or later") fits the cluster's dates almost exactly, and the family had a knightly tradition (G27 Sir John de Gournay I was a crusader). G24 being recorded only as a manorial lord does not by itself exclude military service. But the external prosopography anchors the soldier to Harptree, Somerset, by a defining property fact, and the cluster's theatre — Reims, Knolles in northern France, the Calais garrison — is the royal northern theatre, not the Gascony/Aquitaine theatre where the Somerset banneret Sir Matthew de Gournay operated. G24 therefore remains a Harpley manorial lord; he is **not** the soldier-database knight. The one residual ambiguity is the small set of 1359 Reims protections (TNA C76/38), which the Hull entry does not explicitly claim and which predate its 1363 starting point; they are most parsimoniously the same Harptree John (then ~30) but are not anchored to him by name.[^msd]

Sir John de Gourney of Harptree is a documented 14th-century Somerset Gournay knight distinct from Sir Matthew (d. 1406); both are collateral. He is carried into `research/places/somerset-gournay-collateral.md`.

## Edmund Gournay (G23) inside John of Gaunt's retained East Anglian affinity

Simon Walker's study of the Lancastrian affinity places **Edmund Gournay (G23)** among John of Gaunt's retained East Anglian legal-administrative men, and supplies detail beyond the repo's existing "steward of Gaunt's East Anglian estates" framing. Edmund was "the principal legal adviser to the burgesses of Lynn," and — with Edmund Clippesby — "took fees from the abbey of St. Benet's, Holme." He is bracketed in the same passage with **John Winter** (the Wynter family later central to the Loundhall/Saxthorpe enfeoffment), Robert Cayley (Exchequer attorney for Norwich and steward to the bishop of Norwich), Thomas Pinchbeck (steward to the bishop of Ely), and John Methwold (agent for the canons of West Dereham).[^walker]

Walker's note cites Staffordshire RO D.641/1/2/4 m.4; TNA E.403/478 m.16; HMC *MSS of the Corporations of Southampton and King's Lynn* (1887) pp.221–2; CPR 1381–5 p.380; and KB 9/166/1 m.69 — the primary records behind these fees, carried as lead L-77 for direct retrieval.

## Two patronage axes scaffold the line

The family sat on two overlapping magnate affinities, which is what makes the soldier records cohere rather than read as unrelated namesakes:

- **Lancaster / John of Gaunt.** Edmund G23 retained (above); Sir John V's 1394 Aquitaine service under Gaunt (TNA C61/104 m.7);[^msd] the 1406 Loundhall enfeoffment with Wynter, Berney, Erpingham, Shelton; and Thomas G21's 1415 service under John Holland (Gaunt's son-in-law's house) and at Harfleur under Thomas Beaufort.
- **FitzAlan / Arundel.** The Gurneys held Harpley from the earls of Arundel, and Edmund G23 was steward of Richard FitzAlan's Norfolk estates.[^hop-arundel] The cadet "Richard Gurney, esquire" served as a man-at-arms in Arundel's 1387 and 1388 naval expeditions (sub-captain Edward Courtenay, earl of Devon) — i.e. in his family's own patron's fleet.[^msd]

The practical implication, against the project's standing puzzle that G22 Robert is almost documentarily invisible: the network around Robert — a Gaunt-retained father, an Arundel-steward father, a Lancastrian elder brother, a Holland-serving son — is dense and continuous. Thomas G21's military career is the family following an affinity path Edmund helped lay a generation earlier, not a one-off.

## Candidate cohort and geography triage

Method: use each soldier's first name + service date to set a window, then let the geography of any primary record include or exclude the man against the family's footprint — *our* axis (Harpley, West Barsham, North/East Barsham, Hardingham/Swathings, Saxthorpe, Norwich–Lynn), versus *collateral Norfolk* branches (Runhall, Cawston), versus exclusion zones (Somerset, Essex, London, Wiltshire, Normandy place-names).

| Candidate (rank, date, reference) | Geography signal | Disposition for the direct line |
|---|---|---|
| Sir John de Gourney, knight (1359–78; C76/38–62, E101/30/25) | Harptree castle, Somerset; m. Carew[^hull-john] | **Excluded** — Somerset collateral |
| Sir Matthew de Gournay, banneret (1359–1401; C61, E101/40/26) | Stoke-sub-Hamdon / Harptree, Somerset[^msd][^odnb-matthew-topic] | **Excluded** — Somerset collateral (d. 1406) |
| John de Gourneye, mercer (1386; C71/66) | "of London"[^msd] | **Excluded** — London |
| John Gournay (1390; C71/69) | "of Colchester, Essex," under Mowbray[^msd] | **Excluded** — Essex |
| **Richard Gurney, esquire** (1387/88; E101/40/34, E101/41/5) | Unplaced in *both* the Norfolk and Somerset pedigrees; served under Arundel, the family's patron[^msd] | **Open — priority.** Gentry rank, right generation/affinity; if Daniel Gurney's hedged "Robert" for G22 is wrong, a Richard is conceivable. Needs the 1387/88 muster membrane (L-72). |
| **John Gurnay, man-at-arms** (1422; BNF Fr 25766 no.816) | Retinue of Sir Robert Harling of **East Harling, Norfolk** (nephew of Sir John Fastolf, captor of Meulan 1423)[^msd][^harling] | **Open** — Norfolk gentry military network, but East Harling is the SE/Breckland zone, not our NW axis. Membrane test (L-74). |
| John Gournay, man-at-arms (1417/18; E101/48/17, E101/48/19) | Harfleur garrison under Beaufort/Luttrell, alongside G21 Thomas I's own 1418 Harfleur service[^msd] | **Open** — possible brother/cousin/son in the same Lancastrian garrison (L-73). |
| Robert Gurney, valet-archer (1415; E101/45/1 m14) | None; low status[^msd] | **Hold** — the only exact "Robert Gurney" in G22's window, but yeoman rank argues against the gentleman G22 (L-75). |

Several of the workbook's louder leads (the Somerset knights, the London mercer, the Essex John) are thereby **excluded** as non-Norfolk, narrowing the genuine "undocumented child/relative" field to the Richard esquire and the cadet Johns. None is yet an identification; each turns on a manuscript membrane, carried as a dated lead.

The "Robert Grene" surname leads (1373 Warwick/Gaunt; 1417 Holland; 1430 Avranches) remain held as surname-risk context only: Henry Grene (knight) is Sir Henry Green of Drayton, and Thomas Grene is the archdeacon of Sudbury, so "Grene" is a genuine surname in the same Gaunt orbit and not a safe misreading of Gournay absent a roll image.[^msd]

## Sir Thomas Trevet — a Somerset-side kinship

The Hull prosopography records Sir Thomas Trevet (c. 1350–1388) as "the brother of John Trivet and the nephew of Sir Matthew Gournay," a kinship not previously captured.[^hull-trevet] Carried to the Somerset collateral file.

[^msd]: Soldier in Later Medieval England Online Database (AHRC, Bell/Curry/King/Simpkin), [www.medievalsoldier.org](https://www.medievalsoldier.org/); rows as compiled in `sources/intake/new/gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx`. Underlying references cited per row (TNA C61/C71/C76/E101; BNF MS. Fr./Clairambault/NAF; BL Add. Ch.). Source ID: `medievalsoldier-database`.
[^hull-knolles]: 'The English Way of War, 1360–1399' (PhD thesis, University of Hull), Table 4.2/4.3 and p.341, on Sir Robert Knolles' 1370 expedition (source TNA E101/30/25 mm.1–3, C76/53): "Sir John de Gourneye 3 3" among Knolles' sub-captains. The same expedition and its retinue structure are published in Adrian R. Bell, Anne Curry, Andy King and David Simpkin (eds.), *Military Communities in Late Medieval England* (Woodbridge: Boydell & Brewer, 2018), ch. 8, "Sir Robert Knolles' Expedition to France in 1370: New Perspectives." Source IDs: `hull-thesis-english-way-of-war-1360-1399`, `military-communities-knolles-1370`.
[^hull-john]: Hull thesis, appendix p.340, entry "GOURNEYE John, Sir": owner of Harptree castle, Somerset, 1343 (underage); Ireland 1363 under William de Windsor; Knolles 1370; France 1371–74; Calais garrison 1376 (Calveley) and 1378 (Brocas); n.27 — "From a large and important noble family. Married Elizabeth, late wife of John Carreu (C.P.R. 1370-74, 21)"; distinguished from a London-mercer John Gurney on the Scottish march 1386–90. Source ID: `hull-thesis-english-way-of-war-1360-1399`.
[^hull-trevet]: Hull thesis, p.351, on Sir Thomas Trevet (citing D. Green, 'The Household and Military Retinue of the Black Prince', Nottingham PhD 1998, ii.183): "brother of John Trivet and the nephew of Sir Matthew Gournay." Source ID: `hull-thesis-english-way-of-war-1360-1399`.
[^walker]: Simon Walker, *The Lancastrian Affinity 1361–1399* (Oxford: Clarendon Press, 1990), n.19: Edmund Gournay "the principal legal adviser to the burgesses of Lynn," who "took fees from the abbey of St. Benet's, Holme," bracketed with John Winter, Robert Cayley, Thomas Pinchbeck, John Methwold, Edmund Clippesby; citing Staffordshire RO D.641/1/2/4 m.4; TNA E.403/478 m.16; HMC *MSS of the Corporations of Southampton and King's Lynn* (1887) pp.221–2; CPR 1381–5 p.380; KB 9/166/1 m.69. Source ID: `walker-lancastrian-affinity-1361-1399`.
[^hop-arundel]: "GURNEY, John (d.1408), of Harpley and West Barsham, Norf.," *The House of Commons 1386–1421* (1993), History of Parliament Online — Edmund Gurney retained as steward of the Norfolk estates of Richard FitzAlan, earl of Arundel, "from whom the Gurneys held their manor at Harpley." Source ID: `hop-gurney`.
[^harling]: Sir Robert Harling of East Harling, Norfolk (d. 9 Sept. 1435 at the siege of Saint-Denis), nephew of Sir John Fastolf, bailli of Alençon, captor of the bridge at Meulan 1423. Standard biography: the History of Parliament life of Robert Harling and the modern summary in his Wikipedia entry (orienting only). Source ID: `hop-harling`.
[^odnb-matthew-topic]: Oxford Dictionary of National Biography, s.v. "Gournay [Gourney], Sir Matthew (d. 1406), soldier"; cf. DNB 1885-1900, "Gourney, Mathew" (Wikisource): fourth son of the regicide Sir Thomas Gurney of Englishcombe, of Stoke-sub-Hamdon, Somerset. Source ID: `odnb-matthew-gournay`.
````

---

## Item 02 — Register two new sources in `data/sources.json`

**Outcome:** promote. **Operation:** `str_replace`.

**old_string:**
```
    },
    "girders-net-medieval-gurney-abstracts": {
```

**new_string:**
```
    },
    "hull-thesis-english-way-of-war-1360-1399": {
      "shortTitle": "Hull PhD thesis — The English Way of War, 1360–1399",
      "citation": "'The English Way of War, 1360–1399' (PhD thesis, University of Hull); content file hull_9036a.pdf, Hull institutional repository (Worktribe output 4216021). Author and award year to be confirmed from the repository record (lead L-76). A prosopographical study of English military service 1360–1399 with a biographical appendix and retinue tables (incl. Tables 4.2–4.3 for Sir Robert Knolles' 1370 expedition; source TNA E101/30/25).",
      "archive": "University of Hull (institutional repository)",
      "url": "https://hull-repository.worktribe.com/output/4216021",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/hull-thesis-english-way-of-war-1360-1399.md",
      "notes": "Reviewed 2026-05-30 from the repository PDF (a copy was supplied to sources/intake/new/content-hull_9036a.pdf; not committed to corpus as a modern in-copyright thesis). Appendix p.340 identifies the soldier-database 'Sir John de Gourney' knight cluster (1359–1378) as Sir John de Gourney of Harptree, Somerset (owner of Harptree castle 1343 underage; m. Elizabeth widow of John Carew; Ireland 1363 under William de Windsor; Knolles 1370 captain, retinue of 3; Calais garrison 1376/1378). Also: Sir Thomas Trevet 'nephew of Sir Matthew Gournay' (p.351); Sir Matthew as banneret with a retinue of ~20 on the 1381 Iberian expedition. Used to exclude the knight cluster from the Norfolk direct line (G24). Full citation pending author confirmation."
    },
    "walker-lancastrian-affinity-1361-1399": {
      "shortTitle": "Walker, The Lancastrian Affinity 1361–1399",
      "citation": "Simon Walker, The Lancastrian Affinity 1361–1399, Oxford Historical Monographs (Oxford: Clarendon Press, 1990).",
      "archive": "Oxford University Press (Clarendon Press)",
      "url": "https://academic.oup.com/book/",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/walker-lancastrian-affinity-1361-1399.md",
      "notes": "Standard study of John of Gaunt's affinity. Used 2026-05-30 (n.19) for the East Anglian legal-administrative retainer cohort: Edmund Gournay (G23) 'the principal legal adviser to the burgesses of Lynn' and a fee-taker from the abbey of St Benet's Holme, bracketed with John Winter (Wynter), Robert Cayley, Thomas Pinchbeck, John Methwold, Edmund Clippesby. Walker's note cites Staffordshire RO D.641/1/2/4 m.4; TNA E.403/478 m.16; HMC MSS of the Corporations of Southampton and King's Lynn (1887) pp.221-2; CPR 1381-5 p.380; KB 9/166/1 m.69 (lead L-77). Text consulted 2026-05-30 via a digital reproduction of the affinity prosopography; the underlying authority is Walker."
    },
    "hop-berney": {
      "shortTitle": "History of Parliament — Berney, Sir Robert (c.1365-1415)",
      "citation": "\"BERNEY, Sir Robert (c.1365-1415), of Reedham and Gunton, Norf.,\" in J. S. Roskell, L. Clark and C. Rawcliffe (eds.), The History of Parliament: The House of Commons 1386-1421 (1993), History of Parliament Online.",
      "archive": "History of Parliament Trust",
      "url": "https://www.historyofparliamentonline.org/volume/1386-1421/member/berney-sir-robert-1365-1415",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/hop-berney.md",
      "notes": "Berney-side corroboration, independent of hop-gurney, of John Gurney V's place in the Lancastrian Norfolk affinity: Berney and Gurney as fellow Norfolk shire knights 1399, Erpingham co-trustees, and parties to the Saxthorpe/Loundhall feoffee circle (Erpingham/Wynter/Berney/Shelton). Also bears on whether the 'Sir Robert Gurney of Gunton, deputy at Dover 1400' phrasing is in fact Sir Robert Berney of Gunton. Full page text not yet captured (leads L-78, L-79)."
    },
    "trevor-john-erpingham-1970": {
      "shortTitle": "Trevor John, 'Sir Thomas Erpingham, East Anglian Society and the Dynastic Revolution of 1399' (1970)",
      "citation": "Trevor John, 'Sir Thomas Erpingham, East Anglian Society and the Dynastic Revolution of 1399', Norfolk Archaeology 35, no. 1 (1970): 96-108. DOI 10.5284/1078024.",
      "archive": "Norfolk and Norwich Archaeological Society / Archaeology Data Service",
      "url": "https://doi.org/10.5284/1078024",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/trevor-john-erpingham-1970.md",
      "notes": "Scholarly root of the Erpingham/Berney/Wynter/Shelton/Gurney Lancastrian Norfolk bloc and the likely source of the contested 'Sir Robert Gurney/Berney of Gunton, deputy at Dover 1400' reading. Registered as the cited authority for the network context; article not yet pulled (lead L-79)."
    },
    "military-communities-knolles-1370": {
      "shortTitle": "Military Communities in Late Medieval England — Knolles 1370 chapter",
      "citation": "Adrian R. Bell, Anne Curry, Andy King, and David Simpkin (eds.), Military Communities in Late Medieval England: Essays in Honour of Andrew Ayton (Woodbridge: Boydell & Brewer, 2018), ch. 8, 'Sir Robert Knolles' Expedition to France in 1370: New Perspectives.'",
      "archive": "Boydell & Brewer / Cambridge Core",
      "url": "https://www.cambridge.org/core/books/military-communities-in-late-medieval-england/sir-robert-knolles-expedition-to-france-in-1370-new-perspectives/6F33FEB10FAF2BCBC611C9746CCE8C12",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/military-communities-knolles-1370.md",
      "notes": "Published analysis of Sir Robert Knolles' 1370 retinue (source TNA E101/30/25), the same data underlying the Hull thesis Tables 4.2-4.3 in which Sir John de Gourney appears as a captain. Corroborating source for the C11 knight-cluster identification. Abstract/preview consulted 2026-05-30; full chapter behind paywall."
    },
    "odnb-matthew-gournay": {
      "shortTitle": "ODNB / DNB — Sir Matthew de Gournay (d. 1406), soldier",
      "citation": "Oxford Dictionary of National Biography, s.v. 'Gournay [Gourney], Sir Matthew (d. 1406), soldier' (Oxford University Press); cf. Dictionary of National Biography, 1885-1900, s.v. 'Gourney, Mathew' (freely available on Wikisource).",
      "archive": "Oxford University Press (ODNB) / Wikisource (DNB 1885-1900)",
      "url": "https://www.oxforddnb.com/view/10.1093/ref:odnb/9780198614128.001.0001/odnb-9780198614128-e-11163",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/odnb-matthew-gournay.md",
      "notes": "Authoritative biography corroborating Sir Matthew de Gournay (d. 1406) as the fourth son of Sir Thomas Gurney of Englishcombe (a murderer of Edward II), of Stoke-sub-Hamdon, Somerset — the regicide/Somerset collateral branch, distinct from the Norfolk direct line and from Sir John de Gourney of Harptree. Adds an independent modern authority to the existing Pettigrew/Tyrwhitt/CPR material in research/places/somerset-gournay-collateral.md."
    },
    "gascon-rolls-project": {
      "shortTitle": "The Gascon Rolls Project (1317-1468)",
      "citation": "The Gascon Rolls Project (1317-1468), eds. Universities of Oxford and Liverpool and King's College London, https://www.gasconrolls.org/. Calendar and edition of the Gascon Rolls (TNA C61).",
      "archive": "University of Oxford / University of Liverpool / King's Digital Lab",
      "url": "https://www.gasconrolls.org/",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/gascon-rolls-project.md",
      "notes": "Searchable calendar/edition of the C61 Gascon Rolls — the series behind the Gascony/Aquitaine letters of protection for Thomas de Gourney (1349, C61/61 m6), Sir Matthew de Gournay, and others in the soldier database. Finding aid for fuller calendared text of the Gascony protections (lead L-82); not yet systematically searched."
    },
    "hop-harling": {
      "shortTitle": "History of Parliament / biography — Sir Robert Harling (d.1435)",
      "citation": "Sir Robert Harling of East Harling, Norfolk (d. 9 September 1435), soldier; History of Parliament Trust biography and the modern Wikipedia summary, https://en.wikipedia.org/wiki/Robert_Harling_(knight).",
      "archive": "History of Parliament Trust / Wikipedia (orienting)",
      "url": "https://en.wikipedia.org/wiki/Robert_Harling_(knight)",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/hop-harling.md",
      "notes": "Network context for the cadet lead 'John Gurnay under Sir Robert Harling, 1422' (lead L-74): Harling was a Norfolk knight, nephew of Sir John Fastolf, captor of the bridge at Meulan in 1423, bailli of Alençon, killed at Saint-Denis 1435. Used only as orienting biography; any fact-sheet use should trace to the History of Parliament life or a primary record. Ties the cadet John into the Fastolf circle already woven through the repo's Heylesdon/Saxthorpe material."
    },
    "girders-net-medieval-gurney-abstracts": {
```

---

## Item 03 — Create validation `sources/validations/hull-thesis-english-way-of-war-1360-1399.md`

**Outcome:** promote. **Operation:** new file write.

````markdown
# Validation — Hull PhD thesis, 'The English Way of War, 1360–1399'

**Source ID:** `hull-thesis-english-way-of-war-1360-1399`

**Examined:** appendix biographical entries (pp. 339–341) and Knolles 1370 retinue tables (Tables 4.2–4.3, pp.157–165), from the repository PDF `content-hull_9036a.pdf` (383 pp.), reviewed 2026-05-30.

**What it establishes:** the soldier-database "Sir John de Gournay" knight cluster (1359–1378) is Sir John de Gourney of Harptree, Somerset (appendix p.340); Sir Thomas Trevet is named "nephew of Sir Matthew Gournay" (p.351); Sir Matthew appears as a banneret with a retinue of ~20 on the 1381 Iberian expedition.

**Unexamined / uncertain:** thesis author and award year not yet confirmed from the repository record (lead L-76); the full primary apparatus behind the appendix (CPR/C76/C71 references) not independently re-pulled.

**Findings recorded in:** `research/topics/gurney-medieval-soldier-database.md`; `research/places/somerset-gournay-collateral.md`. Execution trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

---

## Item 04 — Create validation `sources/validations/walker-lancastrian-affinity-1361-1399.md`

**Outcome:** promote. **Operation:** new file write.

````markdown
# Validation — Walker, The Lancastrian Affinity 1361–1399

**Source ID:** `walker-lancastrian-affinity-1361-1399`

**Examined:** the affinity passage and its note 19 (the East Anglian legal-administrative retainer cohort), via a digital reproduction of the affinity prosopography, 2026-05-30.

**What it establishes:** Edmund Gournay (G23) was retained in John of Gaunt's East Anglian affinity — principal legal adviser to the burgesses of Lynn and a fee-taker from St Benet's Holme abbey — bracketed with John Winter, Robert Cayley, Thomas Pinchbeck, John Methwold, and Edmund Clippesby.

**Unexamined / uncertain:** the primary records cited by Walker's note (Staffordshire RO D.641/1/2/4 m.4; TNA E.403/478 m.16; HMC Lynn pp.221–2; CPR 1381-5 p.380; KB 9/166/1 m.69) not yet pulled (lead L-77); whether any Gurney other than Edmund appears as a Gaunt annuitant in Walker's full appendix not yet checked.

**Findings recorded in:** `research/topics/gurney-medieval-soldier-database.md`; (v76) `research/people/g23-edmund-gurney-fact-sheet.research.md`. Execution trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

---

## Item 04b — Create validations for the five additional sources

**Outcome:** promote. **Operation:** five new file writes (thin, per the default-on validation rule).

`sources/validations/hop-berney.md`:
````markdown
# Validation — History of Parliament, Berney, Sir Robert (c.1365-1415)

**Source ID:** `hop-berney`

**Examined:** the History of Parliament Online biography summary (search-result level) 2026-05-30; full page text not yet captured (lead L-78).

**What it establishes:** Berney-side corroboration of John Gurney V as fellow Norfolk shire knight (1399), Erpingham co-trustee, and party to the Saxthorpe/Loundhall feoffee circle — independent of `hop-gurney`. Bears on the Gunton/Gurney-vs-Berney question.

**Findings recorded in:** `research/people/g22-robert-gournay-fact-sheet.research.md`; `research/topics/gurney-medieval-soldier-database.md`. Trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

`sources/validations/trevor-john-erpingham-1970.md`:
````markdown
# Validation — Trevor John, Erpingham and the 1399 Revolution (1970)

**Source ID:** `trevor-john-erpingham-1970`

**Examined:** citation/DOI identified 2026-05-30; article not yet pulled (lead L-79).

**What it establishes (expected):** the scholarly account of the Erpingham/Berney/Wynter/Shelton/Gurney Norfolk bloc and the origin of the "Gurney/Berney of Gunton at Dover 1400" reading.

**Findings recorded in:** `research/people/g22-robert-gournay-fact-sheet.research.md` (as the cited authority for the network context). Trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

`sources/validations/military-communities-knolles-1370.md`:
````markdown
# Validation — Military Communities in Late Medieval England, Knolles 1370 chapter

**Source ID:** `military-communities-knolles-1370`

**Examined:** abstract/preview (Cambridge Core) 2026-05-30; full chapter paywalled.

**What it establishes:** published analysis of Knolles' 1370 retinue (TNA E101/30/25), corroborating the Hull thesis Tables 4.2-4.3 in which Sir John de Gourney appears as a captain — a second authority for the C11 knight-cluster identification.

**Findings recorded in:** `research/topics/gurney-medieval-soldier-database.md`; `research/places/somerset-gournay-collateral.md`. Trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

`sources/validations/odnb-matthew-gournay.md`:
````markdown
# Validation — ODNB / DNB, Sir Matthew de Gournay (d. 1406)

**Source ID:** `odnb-matthew-gournay`

**Examined:** ODNB entry header + DNB 1885-1900 (Wikisource) text, 2026-05-30.

**What it establishes:** Sir Matthew de Gournay (d. 1406) was the fourth son of Sir Thomas Gurney of Englishcombe (regicide), of Stoke-sub-Hamdon, Somerset — the Somerset collateral branch, distinct from the Norfolk line and from Sir John de Gourney of Harptree. Independent modern authority alongside the existing Pettigrew/Tyrwhitt/CPR material.

**Findings recorded in:** `research/places/somerset-gournay-collateral.md`; `research/topics/gurney-medieval-soldier-database.md`. Trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

`sources/validations/gascon-rolls-project.md`:
````markdown
# Validation — The Gascon Rolls Project (1317-1468)

**Source ID:** `gascon-rolls-project`

**Examined:** project site / calendar interface, 2026-05-30; not yet systematically searched for Gournay (lead L-82).

**What it establishes (expected):** fuller calendared text of the C61 Gascony protections for Thomas de Gourney (1349), Sir Matthew de Gournay, and others, with named associates and lands.

**Findings recorded in:** `research/topics/gurney-medieval-soldier-database.md` (as the finding aid for the Gascony-theatre rows). Trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

`sources/validations/hop-harling.md`:
````markdown
# Validation — Sir Robert Harling (d.1435) biography

**Source ID:** `hop-harling`

**Examined:** History of Parliament / Wikipedia summary, 2026-05-30 (orienting only).

**What it establishes:** Sir Robert Harling of East Harling, Norfolk — Norfolk knight, nephew of Sir John Fastolf, captor of Meulan bridge 1423, killed at Saint-Denis 1435 — the captain of the 1422 retinue in which the cadet John Gurnay served (lead L-74).

**Findings recorded in:** `research/topics/gurney-medieval-soldier-database.md`; `research/people/g21-thomas-gournay-i-fact-sheet.research.md`. Trail: `sources/intake/done/v75-medievalsoldier-discovery.patchset.md`.
````

---

## Item 05 — Append Somerset knight + Matthew service rows to `research/places/somerset-gournay-collateral.md`

**Outcome:** promote. **Operation:** `str_replace` (append after the final footnote).

**old_string:**
```
[^v73-rudder-gaunts-urcot]: Rudder, *Gloucestershire* (1779), Almondsbury parish entry, Gaunt's Urcot section (Thornbury Hundred). Compare T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London, 1871), pp. 210-216, which gives the same Bilswick / Gaunt's Hospital foundation under Robert de Gournay II rather than Richard de Gourney. Source IDs: `rudder-gloucestershire-1779`, `pettigrew-collectanea-house-gournay-1871`.
```

**new_string:**
```
[^v73-rudder-gaunts-urcot]: Rudder, *Gloucestershire* (1779), Almondsbury parish entry, Gaunt's Urcot section (Thornbury Hundred). Compare T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London, 1871), pp. 210-216, which gives the same Bilswick / Gaunt's Hospital foundation under Robert de Gournay II rather than Richard de Gourney. Source IDs: `rudder-gloucestershire-1779`, `pettigrew-collectanea-house-gournay-1871`.

## Sir John de Gourney of Harptree — a second 14th-century Somerset knight (distinct from Sir Matthew)

A career knight named Sir John de Gourney, owner of Harptree castle from 1343 (succeeding while underage), is documented across 1359–1378 in the English military record and is distinct from Sir Matthew de Gournay (d. 1406). He took protection for service in Ireland in 1363 under Sir William de Windsor, served as a captain of his own small retinue (three men-at-arms) on Sir Robert Knolles' 1370 expedition to France, and held the Calais garrison under Sir Hugh Calveley (1376) and Sir Bernard Brocas (1378). He married Elizabeth, the widow of John Carew — a West-Country alliance — and is described as being "from a large and important noble family."[^v75-hull-sir-john-harptree] He is the true identity of the "Sir John de Gournay" knight cluster in the *Soldier in Later Medieval England* database (rows under TNA C76/38–62 and E101/30/25), which had otherwise looked chronologically tempting for the Norfolk G24 John de Gournay IV; the Harptree property anchor and the Carew marriage place him firmly in the Somerset branch. See `research/topics/gurney-medieval-soldier-database.md` for the full reasoning.

## Sir Matthew de Gournay — dated service rows behind the epitaph, and the Trevet kinship

The military record supplies dated service attestations that corroborate the Stoke-sub-Hamdon epitaph's campaign list. Matthew's identity as the fourth son of the regicide Sir Thomas Gurney of Englishcombe, seated at Stoke-sub-Hamdon, is independently set out in the Oxford Dictionary of National Biography — a modern authority alongside the Pettigrew and Tyrwhitt material already in this file.[^v75-odnb-matthew] He appears in the retinue of Edward, Lord Despenser, on Gaunt's 1373 chevauchée (TNA E101/32/26); as a **banneret commanding his own Calais garrison retinue** in 1386 (TNA E101/40/26, E101/42/14); and across the Gascony/Aquitaine protections (the C61 series, calendared in the Gascon Rolls Project) and the 1381 Iberian (Castile/Portugal) expedition under Edmund of Langley, earl of Cambridge, where he led a retinue of about twenty men-at-arms and twenty archers.[^v75-msd-matthew][^v75-gascon-rolls-matthew] A further kinship surfaces from the same prosopography: Sir Thomas Trevet (c. 1350–1388) is named "the brother of John Trivet and the nephew of Sir Matthew Gournay."[^v75-hull-trevet]

[^v75-hull-sir-john-harptree]: 'The English Way of War, 1360–1399' (PhD thesis, University of Hull), appendix p.340, entry "GOURNEYE John, Sir," and Knolles retinue table p.341 ("Sir John de Gourneye 3 3"); n.27 gives the Carew marriage (CPR 1370-74 p.21) and the "large and important noble family" description, and distinguishes him from a London-mercer John Gurney on the Scottish march. Harptree castle ownership 1343 per the same entry (citing Rickard, *Castle Community*, p.428; CPR 1361-64 p.428). Source ID: `hull-thesis-english-way-of-war-1360-1399`.

[^v75-msd-matthew]: Soldier in Later Medieval England Online Database, rows for Matthew de Gournay (TNA E101/32/26 Despenser retinue 1373; E101/40/26 and E101/42/14 Calais banneret 1386; C61/82–108 Gascony/Aquitaine; C76/65–66 Castile/Portugal 1381), as compiled in `sources/intake/new/gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx`. The 1381 retinue size (~20 men-at-arms / 20 archers) per the Hull thesis Cambridge-expedition tables (pp.192, 326). Source IDs: `medievalsoldier-database`, `hull-thesis-english-way-of-war-1360-1399`.

[^v75-hull-trevet]: Hull thesis p.351 (citing D. Green, 'The Household and Military Retinue of the Black Prince', Nottingham PhD 1998, ii.183): Sir Thomas Trevet "brother of John Trivet and the nephew of Sir Matthew Gournay." Source ID: `hull-thesis-english-way-of-war-1360-1399`.

[^v75-odnb-matthew]: Oxford Dictionary of National Biography, s.v. "Gournay [Gourney], Sir Matthew (d. 1406), soldier"; cf. Dictionary of National Biography, 1885-1900, s.v. "Gourney, Mathew" (Wikisource): fourth son of Sir Thomas Gurney of Englishcombe (a murderer of Edward II), of Stoke-sub-Hamdon, Somerset. Independent modern authority for the Somerset/regicide parentage already given here from Pettigrew and Tyrwhitt. Source ID: `odnb-matthew-gournay`.

[^v75-gascon-rolls-matthew]: The Gascon Rolls Project (1317-1468), [gasconrolls.org](https://www.gasconrolls.org/), calendaring the C61 Gascony/Aquitaine protections in which Matthew de Gournay recurs; a fuller calendared reading of these entries is held as lead L-82. Source ID: `gascon-rolls-project`.
```

---

## Item 06 — Append cadet-cohort + network notes to `research/people/g22-robert-gournay-fact-sheet.research.md`

**Outcome:** promote. **Operation:** `str_replace` (append after the final footnote).

**old_string:**
```
[^paston-cousin-gurney-tharston]: "Cousin Gurney" / "William Gurney, esq., of Tharston," with the editor's identification as a retainer of the Duke of Norfolk and former escheator of Norfolk, in the Paston correspondence; read in the Internet Archive text `ThePastonLetters` (index s.v. Gurney, William). The exact Gairdner letter and note numbers should be pinned before any fact-sheet use. Source ID: `paston-letters-gairdner`.
```

**new_string:**
```
[^paston-cousin-gurney-tharston]: "Cousin Gurney" / "William Gurney, esq., of Tharston," with the editor's identification as a retainer of the Duke of Norfolk and former escheator of Norfolk, in the Paston correspondence; read in the Internet Archive text `ThePastonLetters` (index s.v. Gurney, William). The exact Gairdner letter and note numbers should be pinned before any fact-sheet use. Source ID: `paston-letters-gairdner`.

### Medieval-soldier cadet cohort, and the "was G22 a Richard?" question (added 2026-05-30)

The *Soldier in Later Medieval England* database, evaluated in full at `research/topics/gurney-medieval-soldier-database.md`, yields a short cohort of otherwise-undocumented Gournay/Gurney men in the G23–G21 window who bear on whether Robert had brothers, sons, or cadets — and on whether his own name was even "Robert." None is an identification; each turns on a manuscript membrane.

The strongest is **Richard Gurney, esquire**, a man-at-arms in the 1387 and 1388 naval expeditions of Richard FitzAlan, earl of Arundel (sub-captain Edward Courtenay, earl of Devon).[^v75-richard-msd] Two facts make him worth pursuing as more than a namesake. First, his rank is gentry (esquire), his date and generation fit a son of Edmund G23, and he served under **Arundel — the very magnate the West Barsham Gurneys were Norfolk stewards for** (Edmund G23 was steward of FitzAlan's Norfolk estates).[^v75-arundel-hop] Second, he is **unplaced in both the Norfolk and the Somerset Gournay pedigrees**: no medieval Richard Gurney appears in Daniel Gurney's otherwise-exhaustive *Record* for the Norfolk line, and the Somerset Harptree line runs Anselm → John → Thomas with no Richard. Because Daniel Gurney himself hedged G22's given name ("whom we believe was named Robert"), an Arundel-affinity gentry esquire of exactly the right generation is a candidate for **G22 himself**, not merely a brother. The tempering consideration is the same clean negative: had Edmund's second son been a Richard, the Norfolk pedigree sources DG used would more likely have caught the name than left it blank-and-hedged. The discriminator is the 1387/88 muster membrane (TNA E101/40/34, E101/41/5), whose retinue neighbours would site Richard Norfolk versus West-Country — lead L-72.

Three further men are held as cadet leads: a **John Gurnay**, man-at-arms in the 1422 retinue of **Sir Robert Harling of East Harling** (a Norfolk knight, nephew of Sir John Fastolf, captor of Meulan in 1423) in the Poissy / Pont-Meulan garrison (L-74); a **John Gournay** in the Harfleur garrison in 1417–18 under Thomas Beaufort and Sir Hugh Luttrell, parallel to Thomas G21's own 1418 Harfleur service (L-73); and a low-status **Robert Gurney**, valet-archer on Henry V's 1415 sick list — the only exact-name "Robert Gurney" in G22's floruit window, though his yeoman rank argues against the gentleman G22 (L-75).[^v75-richard-msd]

The geography triage that produced this short list also **excludes** the louder soldier-database leads as non-Norfolk: the "Sir John de Gournay" knight cluster (Harptree, Somerset), Sir Matthew de Gournay (Somerset), a John Gourney "mercer of London," and a John Gournay "of Colchester, Essex." Details and the full disposition table are in the topic file.

### Berney-side network corroboration, and the Gunton caution (added 2026-05-30)

Independent of the Gurney biography, the History of Parliament life of **Sir Robert Berney (c. 1365–1415)** corroborates John Gurney V's place in the Lancastrian Norfolk bloc from the Berney side — fellow Norfolk shire knight in 1399 and Erpingham co-trustee — and documents the Saxthorpe/Loundhall feoffee circle (Erpingham, Wynter, Berney, Shelton) from a non-Gurney source.[^v75-hop-berney] The root scholarly treatment of that bloc is Trevor John's 1970 *Norfolk Archaeology* study of Erpingham and the 1399 revolution;[^v75-trevor-john] it is also the source to settle whether the much-repeated "Sir Robert Gurney of Gunton, deputy to Erpingham at Dover in 1400" is a Gurney or — far more likely — **Sir Robert Berney of Gunton**. Pending that check, the "Gurney of Gunton" reading is treated as a probable Berney/Gurney error and is **not** used as a Robert G22 lead.

[^v75-hop-berney]: "BERNEY, Sir Robert (c.1365-1415), of Reedham and Gunton, Norf.," *The House of Commons 1386-1421* (1993), History of Parliament Online, [historyofparliamentonline.org](https://www.historyofparliamentonline.org/volume/1386-1421/member/berney-sir-robert-1365-1415). Berney-side corroboration, independent of `hop-gurney`, of John Gurney V as fellow shire knight 1399 and Erpingham co-trustee within the Saxthorpe/Loundhall feoffee circle. Full page text not yet captured (lead L-78). Source ID: `hop-berney`.
[^v75-trevor-john]: Trevor John, "Sir Thomas Erpingham, East Anglian Society and the Dynastic Revolution of 1399," *Norfolk Archaeology* 35, no. 1 (1970): 96-108, DOI 10.5284/1078024. The scholarly account of the Erpingham/Berney/Wynter/Shelton/Gurney bloc and the origin of the "Gunton/Dover 1400" reading; not yet pulled (lead L-79). Source ID: `trevor-john-erpingham-1970`.

[^v75-richard-msd]: Soldier in Later Medieval England Online Database: Richard Gurney/Gourney, esquire, man-at-arms, Naval Service 1387 (TNA E101/40/34 m.1i) and 1388 (TNA E101/41/5 m.5), captain Edward Courtenay earl of Devon, commander Richard FitzAlan earl of Arundel; John Gurnay, man-at-arms, garrison of Poissy/Pont-Meulan 1422 under Sir Robert Harling (BNF MS Fr. 25766 no.816); John Gournay, man-at-arms, Harfleur garrison 1417/1418 (TNA E101/48/17, E101/48/19); Robert Gurney, valet-archer, 1415 sick list (TNA E101/45/1 m.14). As compiled in `sources/intake/new/gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx`. Source ID: `medievalsoldier-database`.
[^v75-arundel-hop]: "GURNEY, John (d.1408)," History of Parliament Online — Edmund Gurney steward of the Norfolk estates of Richard FitzAlan, earl of Arundel, "from whom the Gurneys held their manor at Harpley." Source ID: `hop-gurney`.
```

---

## Phase-2 follow-up (record in chat after application, not in this file)

After applying: prepend the `**Done:** YYYY-MM-DD HH:MM PT` stamp and move this file to `sources/intake/done/`. **v76** (next arc) carries: G23 Edmund companion Gaunt-affinity entry (+ St Benet's Holme); G24 companion note that the soldier-database knight cluster is Somerset (Harptree), not G24; G21 companion Harfleur-parallel cross-note; and fact-sheet promotions — G23 Edmund (Gaunt-retained adviser of Lynn / St Benet's Holme fee, the strongest promotion) and, secondarily, G29 Sir Matthew (banneret service rows + Trevet kinship). The `gurney_medievalsoldier_results_analysis_2026-05-30_v4.xlsx` workbook stays in `sources/intake/new/` until v76 closes the arc, then is archived.
