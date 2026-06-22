**Done:** 2026-06-21 19:44 PT

# Patchset v110 — route the feet-of-fines findings to each subject companion (multi-source)

Phase-1 patchset correcting v109's destination error (it bundled the whole Norfolk feet-of-fines harvest into the **G22** companion). Per `research-files.md`, each finding routes to its subject's companion. **Principle applied here, which v109 got wrong:** a corroborating source is *added*, not skipped, even when the fact pre-exists from another source — multiple witnesses reinforce a fact (so the existing prose gains the Rye feet-of-fines citation as an additional/primary witness); and a finding whose ancestor-match is uncertain is **attached to the likely ancestor with an explicit disclaimer**, not dropped. v108/v109 are not modified. (This supersedes my earlier same-turn v110 draft, which under-applied the principle.)

A thread-wide multi-source pass on the **v108** findings (Newgate→add Savage; the marriage-negative→add Norfolk FHS *Banns & Marriages* + the marriage-licence-bond witness; Yarmouth Edward→add Norfolk B&M + the St Botolph Aldgate 1622 Edward&Anne Gourney datum; Gilman→add the three genealogies read; Mary Gurney × John Allen 1622 → Norwich comparator) is **queued as v111** (v108 can't be edited).

---

## Item 1 — G20 Thomas Gournay II: the "Thomas Gurnay, Armiger, & Margaret" fine

**Outcome: promote.** `str_replace` in `research/people/g20-thomas-gournay-ii-fact-sheet.research.md` — append a Landholdings row.

**old_string:**
`| Depden, Suffolk | c. 1430–1471 | Wauncy inheritance |`

**new_string:**
`| Depden, Suffolk | c. 1430–1471 | Wauncy inheritance |
| West & East Lexham, Castleacre, Newton, Great Dunham, Norfolk | (feet-of-fines concord, 15th c.) | A final concord, **"Thomas Gurnay, Armiger, and Margaret his wife"** v. Nicholas Bokkyng and John Aleyn of Castleacre, in West Lexham, East Lexham, Castleacre, Newton, and Great Dunham (Rye, *Feet of Fines for Norfolk*, Pt II, entry 200). The rank "esquire," the named wife **Margaret**, and the West-Norfolk cluster on the West-Barsham/Harpley axis fit **Thomas II and Margaret Jerningham**; the fine's regnal year is unread, so the identification is provisional and a 14th-century Thomas namesake is not fully excluded (lead L-164).[^rye-thomas-margaret-2026] |

[^rye-thomas-margaret-2026]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Part II (Internet Archive [\`ashortcalendarf00ryegoog\`](https://archive.org/details/ashortcalendarf00ryegoog)), entry 200; harvest at [\`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md). Underlying TNA CP 25/1 (Norfolk), AALT. Source ID: \`rye-feet-of-fines-norfolk\`.`

---

## Item 2 — G29 Matthew: Rye corroborates the Harpley fine

**Outcome: promote.** `str_replace` in `research/people/g29-matthew-de-gournay-fact-sheet.research.md` — add Rye as an additional witness to the existing Harpley-fine fact.

**old_string:**
`This independently corroborates Daniel Gurney and Armstrong (1781) on the Matthew + Rose de Burnham acquisition, supplies the engrailed-cross arms as a Harpley-church witness (relevant to the American-arms question), and fixes the manor's departure from the family c. 1535.[^blomefield-harpley-1810]`

**new_string:**
`This independently corroborates Daniel Gurney and Armstrong (1781) on the Matthew + Rose de Burnham acquisition, supplies the engrailed-cross arms as a Harpley-church witness (relevant to the American-arms question), and fixes the manor's departure from the family c. 1535.[^blomefield-harpley-1810] A feet-of-fines witness sits behind the narrative: Rye's *Short Calendar of the Feet of Fines for Norfolk* (Pt I, entry 236) calendars a Harpley concord, **"Emma de Herpelay v. Matthew de Gurnay, in Harpley"** — alongside Blomefield's "fine of 30 Henry II" that settled the manor on Matthew. Whether #236 is that same concord or a related one, and its exact reign, are unread, so a later-Matthew reading is not fully excluded; but as a Harpley Matthew-de-Gurnay fine it corroborates the holding.[^rye-matthew-harpley-2026]

[^rye-matthew-harpley-2026]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Part I (Internet Archive [\`ashortcalendarf02ryegoog\`](https://archive.org/details/ashortcalendarf02ryegoog); local PDF [\`sources/corpus/rye-feet-of-fines-norfolk-part1.pdf\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus/rye-feet-of-fines-norfolk-part1.pdf)), entry 236. Source ID: \`rye-feet-of-fines-norfolk\`.`

---

## Item 3 — G23 Edmund: the de Morle / Hingham trusteeship fine (new)

**Outcome: promote.** `str_replace` in `research/people/g23-edmund-gurney-fact-sheet.research.md`.

**old_string:**
`2026-04-18 — Close Rolls, 5 Richard II (1382): John de Plays, knight, gave to a group of trustees including Edmund Gournay the manor of Feltwell in Norfolk and the manor of Mundford with the advowson. The co-trustees: William de Beauchamp, John Marmyon, John de Burgh, Stephen de Hales (all knights). This confirms Edmund's role as a legal trustee for major Norfolk landholders.`

**new_string:**
`2026-04-18 — Close Rolls, 5 Richard II (1382): John de Plays, knight, gave to a group of trustees including Edmund Gournay the manor of Feltwell in Norfolk and the manor of Mundford with the advowson. The co-trustees: William de Beauchamp, John Marmyon, John de Burgh, Stephen de Hales (all knights). This confirms Edmund's role as a legal trustee for major Norfolk landholders.

A third trustee instance survives in the Norfolk feet of fines: **Edmund Gournay, with William Pette (parson of Hawardyn), William Cursun, and John R[…] of Rougham, v. William de Morle, knight, of the manor of Hengham [Hingham]** (Rye, *Feet of Fines for Norfolk*, Pt II, entry 1526) — Edmund as feoffee in a Hingham settlement involving the Morley lordship, consistent with the Feltwell/Mundford (1382) and Riburgh (1385) trusts.[^rye-edmund-hingham-2026]

[^rye-edmund-hingham-2026]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Part II (Internet Archive [\`ashortcalendarf00ryegoog\`](https://archive.org/details/ashortcalendarf00ryegoog)), entry 1526; harvest at [\`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md). Source ID: \`rye-feet-of-fines-norfolk\`.`

---

## Item 4 — G23 Edmund: Rye is the primary fine behind Armstrong's Heylesdon reports

**Outcome: promote.** `str_replace` in `research/people/g23-edmund-gurney-fact-sheet.research.md` — add the Rye witness to the already-documented 1395-96 Winter conveyance.

**old_string:**
`And again at Taverham (vol. 9, Freebridge entry for Taverham): "In 1395, the advowson of one of these portions was settled by fine on John Winter, &c. by John Gournay and Alice his wife, with Drayton and Hellesden manors."`

**new_string:**
`And again at Taverham (vol. 9, Freebridge entry for Taverham): "In 1395, the advowson of one of these portions was settled by fine on John Winter, &c. by John Gournay and Alice his wife, with Drayton and Hellesden manors."

The fine itself is calendared by Rye (*Feet of Fines for Norfolk*, Pt II, entry 262): **John Wynter, John Yelverton, Richard Creyk, and Thomas de Lexham v. John Gournay and Alicia his wife, of the manors of Heylesdon and Drayton, and the advowsons of the said manors** — i.e. a primary feet-of-fines witness standing behind Armstrong's three topographical reports of the same conveyance (and behind the G22-companion Heylesdon-settlement narrative for Sir John V × Alice Heylesdon).[^rye-heylesdon-2026]

[^rye-heylesdon-2026]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Part II (Internet Archive [\`ashortcalendarf00ryegoog\`](https://archive.org/details/ashortcalendarf00ryegoog)), entry 262; harvest at [\`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md). Source ID: \`rye-feet-of-fines-norfolk\`.`

---

## Item 5 — G23 Edmund: Rye corroborates the Rector-John Saxthorpe / Harpley footprint

**Outcome: promote.** `str_replace` in `research/people/g23-edmund-gurney-fact-sheet.research.md`.

**old_string:**
`DG-Supp Note 117 also notes the Saxthorpe (Loundhall) manor: "John de Mereworthe was lord of the manor of Saxthorpe, which had been held by John Gurnay II [Rector], as it afterwards was by John Gurnay V [Sir John, d.1408]." The £20/year annuity from Edmund to John de Mereworthe was "probably in consequence of some agreement between them" — likely a buyout or settlement related to Saxthorpe.`

**new_string:**
`DG-Supp Note 117 also notes the Saxthorpe (Loundhall) manor: "John de Mereworthe was lord of the manor of Saxthorpe, which had been held by John Gurnay II [Rector], as it afterwards was by John Gurnay V [Sir John, d.1408]." The £20/year annuity from Edmund to John de Mereworthe was "probably in consequence of some agreement between them" — likely a buyout or settlement related to Saxthorpe.

Rye's feet of fines independently witness both holdings of the Rector-John line: **John de Gurney, of the manor of Saxthorp** (Pt I, entry 837, with Simon de Creppinge) and **John Gurnay, parson of the church of Harpele [Harpley], of the manor of Harpley and land in Gaywood** (Pt II, entry 489) — feet-of-fines corroboration of the Saxthorpe/Harpley footprint that DG records for John Gurnay II the Rector (and Sir John V at Saxthorpe). Which John-generation each fine names is not closed by the calendar alone.[^rye-saxthorp-harpley-2026]

[^rye-saxthorp-harpley-2026]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Parts I and II (Internet Archive [\`ashortcalendarf02ryegoog\`](https://archive.org/details/ashortcalendarf02ryegoog), [\`ashortcalendarf00ryegoog\`](https://archive.org/details/ashortcalendarf00ryegoog)), entries 837 and 489; harvest at [\`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md). Source ID: \`rye-feet-of-fines-norfolk\`.`

---

## Item 6 — reconciliation instruction for v109 (apply-order note)

When the patchsets are applied, **trim v109's Item 2** (the G22 "Norfolk feet-of-fines harvest") to its G22-proper content — Robert's 1405 fine (#64) and the Germye/Gereneye candidate leads (L-162/L-163) — and replace the per-other-ancestor list with a one-line pointer: *"The wider Gurnay-fines harvest is routed to each subject companion (Thomas II G20 #200; Matthew G29 #236; Edmund G23 #1526/#262/#837/#489) via patchset v110; the unattributed same-name fines remain in `sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md`."* (Stated as an instruction because v108/v109 are not edited here.)

## Not yet ancestor-attributable (named candidate + disclaimer, kept in the corpus)
These same-name fines lack a confident single ancestor and so stay in the corpus harvest rather than being forced onto a companion — each with its best candidate noted there:
- **#1593 John de Gurney, in Hardingham & Reymerston** — Hardingham is a line manor (G29 → G20); the John-generation (G27 Sir John I / G24/G25) is undetermined.
- **#148 William de Gurnai, in Burnham** — Burnham ties to the Rose-de-Burnham/Harpley root; a William of the line (G30 William I or G28 William II) is possible but unfixed.
- **#146 Wm. fil. Phi. de Gurnay & Elena, in Reymerston** — "son of Philip," a forename outside the main male line → most likely collateral.
- **#1059 John de Gurnay (Hillington); #504 Mabil widow of Ludovic de Gurnay; Hugh de Gurnay (Cantley/Carleton); de Gornay & Katrine (Habelund); Gurney & Havisia (Duneston)** — collateral or unplaced same-name; no safe direct-line attribution.

Promote any of these to a companion only once a date/identity is fixed (image read / regnal year).
