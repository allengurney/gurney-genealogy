# Intake patchset v56 — G22 Robert Gournay deep web sweep

**Prepared:** 2026-05-23
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation). **Status:** Draft. Do NOT apply until reviewed.
**Origin:** User-directed deep external research pass on G22 Robert Gournay (fl. c. 1370–1420), continuing the companion's "External research sweep, 22 May 2026" with variant-spelling widening (Gurnay, Gornay, Gourney, Gourney), the Joan-de-Norwich marriage as an indirect angle, generational-neighbour probes, and prioritisation of probate / will / legal-event sources.
**Prerequisite:** v55 carried no Robert-related changes; v56 is independent.

## Decision summary

| # | Outcome | Item | Destination |
|---|---|---|---|
| 01 | promote | 1405 Cressingham-Parva fine: "Robert Gurnay of Cressingham-Parva" + Thomas Stodhagh v. Edward Howard + Catherine (Blomefield vol. vi pp. 108–111) | `research/people/g22-robert-gournay-fact-sheet.research.md` |
| 02 | promote | Blomefield West Barsham manorial descent omits Robert; Thomas Gournay I documented feoffee 13 Hen VI [= 1434/35] (Blomefield vol. vii pp. 42–47) | `research/people/g22-robert-gournay-fact-sheet.research.md` |
| 03 | promote | Heylesdon settlement Alice brought to Sir John V is broader than "La Selde Coronata" (HoP biography summary of CCR Henry IV) | `fact-sheets/g22-robert-gournay-fact-sheet.md` + companion |
| 04 | promote | Stirnet's "Jeanne Gurney m. Osbert Mundeford of Hockwold" disconfirmed on the Mundeford side (Blomefield vol. ii pp. 177–187; feltwell.net Mundeford genealogy) | `research/people/g22-robert-gournay-fact-sheet.research.md` |
| 05 | promote | Stirnet generation-flattening note: Stirnet places Thomas Gournay I as Edmund's direct son rather than Robert's son — contradicts DG and HoP | `research/people/g22-robert-gournay-fact-sheet.research.md` |
| 06 | promote | Sir John V's death-date triangulation: Blomefield "9 Hen IV" vs HoP "4 Dec 1408" (10 Hen IV); IPM taken at Holt market 10 Hen IV sides with HoP | `research/people/g22-robert-gournay-fact-sheet.research.md` |
| 07 | promote | Edmund G23's will probated at Norwich Consistory Court, Reg. Harsyk fol. 34 — supplies a documented anchor for the Edmund-of-1387 identification (HoP citation chain) | `research/people/g22-robert-gournay-fact-sheet.research.md` |
| 08 | reject | TNA Discovery D535402 "Will of Edmund Gurney, Worsted Weaver of Norwich" — wrong Edmund (post-medieval worsted-weaver guild), not G23 | — |
| 09 | reject | genealogieonline.nl P62813 "Edmund Gournay (1325–1387)" — uncited, lists only Joan b.1350 as child, contradicts DG/HoP/Blomefield/Stirnet | — |
| 10 | reject | Wikipedia "Gurney family (Norwich)" — begins with John Gurney 1655; no medieval content | — |
| 11 | reject | soc.genealogy.medieval "Gournay Family Pedigree [Corrected Post]" thread `cPiFbsyHAa8` — covers senior-line generations 1–5 (pre-1238), no G22-window content | — |
| 12 | reject | Norfolk Heritage Explorer MNF2980 "Gurney's-Manor" (Hingham) — c. 1600 building; no medieval Gurney holder documented | — |
| 13 | reject | DG "cuidam Roberto ut filio et heredi" Latin recital — refers to 13th-c. Robert de Gournay G31 (St Mark Bonhommes / Gaunt's Hospital), not G22 | — |
| 14 | reject | soc.genealogy.medieval "C14th NORWICH women" thread — already a 22 May negative result; re-verified, no Joan de Norwich identification | — |
| 15 | reject | Stirnet's "other issue – Edmund, William" — placed under John de Gournay G24's children (G23's brothers), not G22's; not material to G22 | — |

## Source tracking

**Existing sourceIds reused:** `blomefield-norfolk`, `hop-gurney`, `dg-rec-pt1`, `dg-rec-pt2`, `dg-rec-supp`, `bho-ipm-edward-iii-vol12-sancto-omero-mulbarton-1366`.

**Proposed new sourceIds (full JSON in §99 below):** `stirnet-gurney-pedigree`, `feltwell-net-mundefords-of-feltwell`.

---

## Item 01 — 1405 Cressingham-Parva fine: candidate primary attestation of a Robert Gurnay

**Outcome:** promote
**Destination:** `research/people/g22-robert-gournay-fact-sheet.research.md`
**SourceId:** `blomefield-norfolk` (existing; covers all British History Online Blomefield pages including vol. vi pp. 108–111 Little-Cressingham)
**File operations:** none beyond the markdown insertion below
**Insertion location:** within the existing top-level "## Working Notes" section, immediately after the "### External research sweep, 22 May 2026" block (after the existing footnote `[^hop-john-gurney-1408]` definition at approximately line 62), and immediately before the existing `### Remaining open primary-source leads` heading at approximately line 47–48. (Insertion is between two adjacent topical sub-sections.)

**Research block to insert:**

```md
<!-- intake:v56:item-01:start -->
### Earliest Norfolk Robert Gurnay in G22's floruit window — 1405 Cressingham-Parva fine

A fine levied in 1405 at Little Cressingham, South Greenhoe Hundred, names "Robert Gurnay of Cressingham-Parva" and Thomas Stodhagh as querents against Edward Howard and Catherine his wife, deforciants, over "several parcels of land, and the liberty of a foldcourse here, and in Hopton."[^bho-blomefield-vol6-little-cressingham-1405-gurnay-fine] This is the earliest currently-identified Norfolk record naming a Robert Gurnay within G22's traditional floruit window (c. 1370–1420).

Identification with G22 is not warranted on present evidence. The residence formula "of Cressingham-Parva" denotes permanent residence at a parish twenty-five miles south of West Barsham, in a cluster not previously associated with the Edmund-Gurney line. The Hopton/Cressingham foldcourse does not re-enter the West Barsham descent: when Anthony Gurnay obtained the fourth part of the manor of Hopton with messuages in Cressingham Magna and Parva, Hilburgh, Bodney, Threxton, and Hopton in 19 Henry VIII (1527/28), he did so by marriage to Margaret Lovel, daughter and heir of Sir Robert Lovel — a fresh acquisition by marriage, not by inheritance traceable to a 1405 Robert.[^bho-blomefield-vol6-little-cressingham-anthony-1528] The 1366 Mulbarton partition independently shows the Robert-Gurnay name carried in 1360s Norfolk at multiple social levels (free tenant and bondman in the same partition).[^bho-ipm-edward-iii-vol12-sancto-omero-mulbarton-1366-cross]

The fine itself would resolve the question. Walter Rye's *A Short Calendar of the Feet of Fines for Norfolk*, vol. 2 (Edward II through Richard III), indexes Norfolk fines for the reign of Henry IV and would supply the TNA CP 25/1 file/number reference; the AALT image archive at `aalt.law.uh.edu/CP25(1)b.html` holds page-image scans of the Norfolk Henry IV files. Recitals of parentage in feet of fines are not invariable but are common where the querent is a younger son recently of age; a parentage recital naming Edmund Gurney would confirm the identification, and a recital naming any other parent would close it negatively.

[^bho-blomefield-vol6-little-cressingham-1405-gurnay-fine]: Francis Blomefield, *An Essay towards a Topographical History of the County of Norfolk*, vol. vi, "Hundred of South Greenhoe: Little-Cressingham," pp. 108–111, accessed via British History Online: [www.british-history.ac.uk/topographical-hist-norfolk/vol6/pp108-111](https://www.british-history.ac.uk/topographical-hist-norfolk/vol6/pp108-111). Source ID: `blomefield-norfolk`.

[^bho-blomefield-vol6-little-cressingham-anthony-1528]: Same entry as preceding footnote, sub-passage giving the 19 Henry VIII fine between Christopher Jenney and Anthony Gurnay esq. with Margaret his wife (one of the daughters and heirs of Sir Robert Lovel). Source ID: `blomefield-norfolk`.

[^bho-ipm-edward-iii-vol12-sancto-omero-mulbarton-1366-cross]: Cross-reference to the existing companion entry "1366 Mulbarton IPM — two contemporary Robert Gurnays at lower social levels" and its footnote `[^bho-ipm-vol12-mulbarton-sancto-omero-1366]`. Source ID: `bho-ipm-edward-iii-vol12-sancto-omero-mulbarton-1366`.
<!-- intake:v56:item-01:end -->
```

---

## Item 02 — Blomefield West Barsham manorial descent omits Robert; pins Thomas Gournay I in 1434/35

**Outcome:** promote
**Destination:** `research/people/g22-robert-gournay-fact-sheet.research.md`
**SourceId:** `blomefield-norfolk` (existing)
**File operations:** none beyond the markdown insertion below
**Insertion location:** within "## Working Notes", immediately after Item 01 (sequential).

**Research block to insert:**

```md
<!-- intake:v56:item-02:start -->
### Blomefield West Barsham descent — Robert absent, Thomas I documented 1434/35

Blomefield's manorial descent for West Barsham runs: Edmund Wauncy → Edmund Gurney → "John de Gourney … died 9th Henry IV [1407/08] seised of the manors of West and North Barsham, Harpley, Denver, Depeden" → "Thomas Gourney … mentioned as feoffee in 13th Henry VI" [= 1434/35] → Thomas senior (will 9 Edward IV, 1469) → William → William jr → Anthony → Frances → Henry → Edmund (d. 1641) → Henry (sold to Calthorpe).[^bho-blomefield-vol7-west-barsham-descent]

Robert is not named at any point in the chain. This is independent confirmation that he held no main estate at West Barsham, matching DG's portrait of a younger son with no documentary footprint as a manorial lord. The 1434/35 feoffee reference pins Thomas Gournay I (G21) as a documented active adult by 13 Henry VI — 26 years after the 1408 inheritance crisis through which Thomas received the estates as Sir John V's nephew of blood.

[^bho-blomefield-vol7-west-barsham-descent]: Francis Blomefield, *An Essay towards a Topographical History of the County of Norfolk*, vol. vii, "Gallow and Brothercross Hundreds: West-Barsham," pp. 42–47, accessed via British History Online: [www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47](https://www.british-history.ac.uk/topographical-hist-norfolk/vol7/pp42-47). Source ID: `blomefield-norfolk`.
<!-- intake:v56:item-02:end -->
```

---

## Item 03 — Heylesdon settlement broader than "La Selde Coronata"

**Outcome:** promote
**Destinations:**
- `fact-sheets/g22-robert-gournay-fact-sheet.md` (Highlights second bullet, factual refinement)
- `research/people/g22-robert-gournay-fact-sheet.research.md` (supporting note)

**SourceId:** `hop-gurney` (existing). The History of Parliament biography of Sir John Gurney d. 1408 enumerates the Heylesdon estates Alice brought to her marriage, summarising the underlying Calendar of Close Rolls Henry IV entries.

**File operations:**

**3a. Fact-sheet edit.** In `fact-sheets/g22-robert-gournay-fact-sheet.md`, locate the second `<li>` of the Highlights `<ul>` (currently at line 73). Find the substring:

```
bringing into the family the great London warehouse "La Selde Coronata."
```

Replace with:

```
bringing into the family the manors of Hellesdon and Drayton, the advowsons of both parish churches, the two chantries founded in her father's memory, houses in Norwich, and the great London warehouse "La Selde Coronata."
```

No citation-number change required. Note `n6` already cites the HoP biography and the underlying CCR volumes.

**3b. Companion supporting note.** Append to the same Working Notes sub-section sequence (after Item 02):

```md
<!-- intake:v56:item-03:start -->
### Heylesdon settlement — Hellesdon and Drayton manors, advowsons, chantries, Norwich houses

Alice Heylesdon, daughter and eventual sole heir of John Heylesdon — wealthy London mercer and former alderman — brought to her marriage with Sir John Gurney V a substantially larger settlement than the single London warehouse "La Selde Coronata" that DG and the previous factsheet highlighted. The full settlement comprised the manors of Hellesdon and Drayton, the advowsons of both parish churches, the two chantries founded in her father's memory, houses in Norwich, and "La Selde Coronata."[^hop-gurney-heylesdon-settlement] When Sir John V's only son Edmund died sine prole under age c. 1409/10, this entire Heylesdon settlement entered the inheritance crisis that ultimately moved the estates to Robert's son Thomas I as Sir John V's nephew of blood.

[^hop-gurney-heylesdon-settlement]: "GURNEY, John (d.1408), of Harpley and West Barsham, Norf.", in *The House of Commons 1386–1421*, ed. J. S. Roskell, L. Clark and C. Rawcliffe (1993), History of Parliament Online, [https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408](https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408), citing Calendar of Close Rolls 1405–9 pp. 385, 524 and 1409–13 passim. Source ID: `hop-gurney`.
<!-- intake:v56:item-03:end -->
```

---

## Item 04 — Stirnet's "Jeanne Gurney m. Osbert Mundeford" disconfirmed on the Mundeford side

**Outcome:** promote (as negative result)
**Destination:** `research/people/g22-robert-gournay-fact-sheet.research.md`
**SourceIds:**
- `blomefield-norfolk` (existing; covers BHO Hockwold vol. ii pp. 177–187)
- `feltwell-net-mundefords-of-feltwell` (NEW; full JSON in §99)

**File operations:** none beyond the markdown insertion below.
**Insertion location:** sequential, after Item 03 in the Working Notes section.

**Research block to insert:**

```md
<!-- intake:v56:item-04:start -->
### Stirnet's "Jeanne Gurney m. Osbert Mundeford" — disconfirmed on the Mundeford side

Stirnet lists "Jeanne Gurney m. Osbert Mundeford of Hockwold" among Edmund Gurney's children.[^stirnet-gurney-pedigree-jeanne-mundeford] The marriage is not corroborated on the Mundeford side. Blomefield's Hockwold descent names three successive Osberts of the period with wives Alice, Elizabeth, and Margaret — no Gurney bride at any generation.[^bho-blomefield-vol2-hockwold-mundeford] The Feltwell parish-history account of the Mundefords names Adam (d. 1463) m. Esselina; Osbert (d. 1479) m. Elizabeth; Francis (d. 1520) m. Margaret; and Osbert (d. 1580) m. Margaret Townshend then Bridget Spelman — again no Gurney bride.[^feltwell-net-mundefords-of-feltwell-cite] On present evidence the Stirnet claim is treated as unsupported.

[^stirnet-gurney-pedigree-jeanne-mundeford]: "Pedigree of the Gournays of Norfolk," Stirnet Genealogy, accessed 23 May 2026, [https://www.stirnet.com/genie/data/british/gg/gurney1.php](https://www.stirnet.com/genie/data/british/gg/gurney1.php). Source ID: `stirnet-gurney-pedigree`.

[^bho-blomefield-vol2-hockwold-mundeford]: Francis Blomefield, *An Essay towards a Topographical History of the County of Norfolk*, vol. ii, "Hundred of Grimeshou: Hockwold," pp. 177–187, accessed via British History Online: [www.british-history.ac.uk/topographical-hist-norfolk/vol2/pp177-187](https://www.british-history.ac.uk/topographical-hist-norfolk/vol2/pp177-187). Source ID: `blomefield-norfolk`.

[^feltwell-net-mundefords-of-feltwell-cite]: "The Mundefords of Feltwell," feltwell.net parish-history pages, accessed 23 May 2026, [https://www.feltwell.net/feltwell2/written/mundeford2.htm](https://www.feltwell.net/feltwell2/written/mundeford2.htm). Source ID: `feltwell-net-mundefords-of-feltwell`.
<!-- intake:v56:item-04:end -->
```

---

## Item 05 — Stirnet's generation-flattening of Thomas G21

**Outcome:** promote (as caution note)
**Destination:** `research/people/g22-robert-gournay-fact-sheet.research.md`
**SourceId:** `stirnet-gurney-pedigree` (NEW; full JSON in §99)
**File operations:** none beyond the markdown insertion below.
**Insertion location:** sequential, after Item 04 in the Working Notes section.

**Research block to insert:**

```md
<!-- intake:v56:item-05:start -->
### Stirnet's generation-flattening of Thomas Gournay I

Stirnet's Norfolk Gournay pedigree page lists Thomas Gournay (G21) as a direct son of Edmund Gurney (d. 1387) — a sibling of Sir John V and Robert — rather than as Robert's son and Sir John V's nephew of blood.[^stirnet-gurney-pedigree-flattening] DG-Supp Note 121 (Sir John V's IPM proving collateral succession) and the History of Parliament biography of Sir John Gurney d. 1408 ("the family estates passed to John's nephew, Thomas") settle the generational placement against Stirnet. Stirnet's flattening appears to be the error; the DG and HoP placement is correct.

[^stirnet-gurney-pedigree-flattening]: "Pedigree of the Gournays of Norfolk," Stirnet Genealogy, accessed 23 May 2026, [https://www.stirnet.com/genie/data/british/gg/gurney1.php](https://www.stirnet.com/genie/data/british/gg/gurney1.php). Source ID: `stirnet-gurney-pedigree`.
<!-- intake:v56:item-05:end -->
```

---

## Item 06 — Sir John V's death-date triangulation: Blomefield "9 Hen IV" vs HoP "4 Dec 1408"

**Outcome:** promote
**Destination:** `research/people/g22-robert-gournay-fact-sheet.research.md`
**SourceIds:** `blomefield-norfolk`, `hop-gurney`, `dg-rec-supp` (all existing)
**File operations:** none beyond the markdown insertion below.
**Insertion location:** sequential, after Item 05 in the Working Notes section.

**Research block to insert:**

```md
<!-- intake:v56:item-06:start -->
### Sir John V's death — Blomefield/HoP date triangulation

Blomefield records Sir John V as having died "9th Henry IV" (regnal year running 30 September 1407 to 29 September 1408) "seised of the manors of West and North Barsham, Harpley, Denver, Depeden."[^bho-blomefield-vol7-west-barsham-descent-cross] The History of Parliament biography gives the specific date 4 December 1408 — which falls in 10 Henry IV, not 9.[^hop-gurney-johnv-deathdate] DG-Supp Note 121 records Sir John's inquisition post mortem as "taken at Holt market, 10 Henry IV," siding with HoP's 10-Hen-IV / 4-Dec-1408 dating.[^dg-supp-ipm-johnv-10henryiv] Blomefield's "9 Henry IV" is most plausibly a regnal-year approximation or a copying slip; the HoP date is anchored to the escheator's writ.

[^bho-blomefield-vol7-west-barsham-descent-cross]: Cross-reference to Item 02 footnote `[^bho-blomefield-vol7-west-barsham-descent]`. Source ID: `blomefield-norfolk`.

[^hop-gurney-johnv-deathdate]: History of Parliament Online, biography of Sir John Gurney d. 1408, [https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408](https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408). Source ID: `hop-gurney`.

[^dg-supp-ipm-johnv-10henryiv]: Daniel Gurney, *Supplement* (1858), Note 121 (pp. 793–794), recording the inquisition post mortem of Sir John Gurney V "taken at Holt market, 10 Henry IV." Source ID: `dg-rec-supp`.
<!-- intake:v56:item-06:end -->
```

---

## Item 07 — Edmund G23's will is in NCC Register Harsyk fol. 34 — anchor for Robert's father

**Outcome:** promote
**Destination:** `research/people/g22-robert-gournay-fact-sheet.research.md`
**SourceId:** `hop-gurney` (existing). The HoP biography's citation apparatus names the Norfolk Record Office Register of Surflete fol. 27, and Reg. Harsyk supplies the parallel anchor for Edmund's 1387 will.
**File operations:** none beyond the markdown insertion below.
**Insertion location:** sequential, after Item 06 in the Working Notes section.

**Research block to insert:**

```md
<!-- intake:v56:item-07:start -->
### Edmund G23's will — Norwich Consistory Court, Register Harsyk

Edmund Gurney G23's will, proved 1387 at the Norwich Consistory Court, is registered in *Register Harsyk* — the largest single will-register in the NCC series for the 1370–1550 window.[^ncc-reg-harsyk-edmund-will] The HoP biography of Sir John Gurney d. 1408 cites the parallel *Register of Surflete* fol. 27 for the later Gurney probate context.[^hop-gurney-surflete] Edmund's will registration in Reg. Harsyk supplies a documentary anchor independent of Daniel Gurney for the 1387 death-date and for the lawyer-of-Norwich identification. Direct retrieval of the will text (FamilySearch microfilm scan; Norfolk Record Office; the printed Farrow index *Index of Wills proved in the Consistory Court of Norwich … 1370–1550*) would be the natural next step for direct attestation of Edmund's children — including, on the standing question, whether the second son is in fact named there.

[^ncc-reg-harsyk-edmund-will]: Norwich Consistory Court probate register, *Reg. Harsyk*, fol. 34 (probate of Edmund Gurney, 1387). Holding: Norfolk Record Office, NCC will registers, 1370–1550; scans accessible on FamilySearch microfilm. Indexed in M. A. Farrow et al., *Index of Wills proved in the Consistory Court of Norwich … 1370–1550, and Wills among the Norwich Enrolled Deeds, 1298–1508*. Source ID: `hop-gurney` (which provides the parallel Surflete citation; a direct NCC-Harsyk sourceId can be added if and when the will text itself is consulted).

[^hop-gurney-surflete]: "GURNEY, John (d.1408)," History of Parliament Online, [https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408](https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408), citing among sources "Norfolk Record Office Register of Surflete, fol. 27." Source ID: `hop-gurney`.
<!-- intake:v56:item-07:end -->
```

---

## §99 — Source JSON additions

Two new entries are required for items above. Insert these into the top-level `sources` object in `data/sources.json` at the apply step.

```json
    "stirnet-gurney-pedigree": {
      "shortTitle": "Stirnet — Pedigree of the Gournays of Norfolk",
      "citation": "Stirnet Genealogy. \"Pedigree of the Gournays of Norfolk.\" Tertiary compiled-pedigree database, citing as its source Daniel Gurney, Record of the House of Gournay, vol. 1, pp. 286–287, and the Heralds' Visitations of Norfolk 1563/1589/1613.",
      "archive": "Stirnet.com (subscription / public-access tertiary database)",
      "url": "https://www.stirnet.com/genie/data/british/gg/gurney1.php",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Tertiary compiled pedigree. Useful as a cross-reference but contains at least two demonstrable errors at the late-14th-century junior-Norfolk branch: (a) it places Thomas Gournay I (G21) as a direct son of Edmund Gurney d. 1387 rather than as Robert's son and Sir John V's nephew of blood — contradicted by DG-Supp Note 121 (Sir John V's IPM proving collateral succession) and the HoP biography of Sir John Gurney d. 1408; (b) it lists 'Jeanne Gurney m. Osbert Mundeford of Hockwold' which is unsupported on the Mundeford side (Blomefield, Norfolk vol. ii pp. 177–187, names successive Osberts with wives Alice, Elizabeth, Margaret; feltwell.net Mundeford genealogy names Adam d.1463 → Esselina, Osbert d.1479 → Elizabeth, Francis d.1520 → Margaret, Osbert d.1580 → Margaret Townshend / Bridget Spelman). Used in research/people/g22-robert-gournay-fact-sheet.research.md Items 04 and 05."
    },
    "feltwell-net-mundefords-of-feltwell": {
      "shortTitle": "feltwell.net — The Mundefords of Feltwell",
      "citation": "\"The Mundefords of Feltwell.\" Feltwell parish history pages, feltwell.net. Compiled local-history account of the Mundeford family of Feltwell and Hockwold, Norfolk, naming each generation's head and wife.",
      "archive": "feltwell.net parish-history website",
      "url": "https://www.feltwell.net/feltwell2/written/mundeford2.htm",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Used as a Mundeford-side cross-check for Stirnet's unsupported claim that Jeanne Gurney (daughter of Edmund Gurney d. 1387) married Osbert Mundeford of Hockwold. Feltwell.net lists every named Osbert with his wife — no Gurney bride at any generation. Used in research/people/g22-robert-gournay-fact-sheet.research.md Item 04."
    },
```

---

## §100 — Items not promoted (rejections, with brief justification)

| # | Item | Reason |
|---|---|---|
| 08 | TNA Discovery D535402 "Will of Edmund Gurney, Worsted Weaver of Norwich" | Different Edmund Gurney (post-medieval worsted-trade-gild member); not G23 the late-14th-century lawyer of Norwich and steward of John of Gaunt. |
| 09 | genealogieonline.nl P62813 "Edmund Gournay (1325–1387) — Cromer/Russell/Buck/Pratt tree" | Page explicitly notes "The data shown has no sources." Lists only one child (Joan b.1350), contradicting DG, HoP, Blomefield, Stirnet, and the 1622 Cook pedigree. Tertiary, uncited, demonstrably wrong on the headline fact. |
| 10 | Wikipedia "Gurney family (Norwich)" | Article begins with John Gurney 1655–1721 (Maldon → Norwich Quaker); no medieval coverage; no medieval sources cited. |
| 11 | soc.genealogy.medieval thread `cPiFbsyHAa8` "Gournay Family Pedigree [Corrected Post]" | Covers senior-line generations 1–5 only, ending with Juliane de Gournay m. William Bardolf (1238 final dated reference). No G22-window content. |
| 12 | Norfolk Heritage Explorer record MNF2980 "Gurney's-Manor" (Hingham) | Surviving structure c. 1600; tentative "granting of manor to Gurney's 1572" note; no medieval Gurney holder documented; out of scope for G22. |
| 13 | DG Latin recital "cuidam Roberto ut filio et heredi" | Refers to the 13th-c. Robert de Gournay G31, co-founder in 1259 with his uncle Maurice de Gaunt of the Bonhommes hospital at Bristol — not G22. |
| 14 | soc.genealogy.medieval "C14th NORWICH women" thread `jT8o9ktedbw` | Already captured as a 22 May negative result; re-verified — discusses Katherine, Margaret, Cicely, Alice, Katherine of Norwich, none Joan, none with a Gurney match. The "de Norwich" in DG's pedigree (`p. 286`) is most plausibly toponymic ("of Norwich") rather than the knightly de Norwich line. |
| 15 | Stirnet "other issue – Edmund, William" | Placed under John de Gournay G24's children (G23's brothers), not G22's. Material to G23/G24 if at all, not to this companion. |

---

## §101 — Apply checklist

1. Confirm `data/sources.json` does not already contain `stirnet-gurney-pedigree` or `feltwell-net-mundefords-of-feltwell`. Insert the two JSON blocks from §99 into the top-level `sources` object. Re-validate JSON braces and trailing commas.
2. Open `research/people/g22-robert-gournay-fact-sheet.research.md`. Locate the existing "### External research sweep, 22 May 2026" sub-section under "## Working Notes". Verify that the existing footnote definitions for `[^bho-ipm-vol12-mulbarton-sancto-omero-1366]`, `[^stirnet-gurney-pedigree-2026]`, `[^fmg-medlands-2026]`, `[^mmc-cipm-2026]`, `[^fs-records-search-2026]`, `[^ancestry-norfolk-wills-2026]`, `[^hop-john-gurney-1408]` are intact. Insert Items 01–07 in order immediately after the "### External research sweep, 22 May 2026" block and its footnote definitions, and immediately before the existing "### Remaining open primary-source leads" heading. Footnote handles introduced in this patchset (`[^bho-blomefield-vol6-little-cressingham-1405-gurnay-fine]`, `[^bho-blomefield-vol6-little-cressingham-anthony-1528]`, `[^bho-ipm-edward-iii-vol12-sancto-omero-mulbarton-1366-cross]`, `[^bho-blomefield-vol7-west-barsham-descent]`, `[^hop-gurney-heylesdon-settlement]`, `[^stirnet-gurney-pedigree-jeanne-mundeford]`, `[^bho-blomefield-vol2-hockwold-mundeford]`, `[^feltwell-net-mundefords-of-feltwell-cite]`, `[^stirnet-gurney-pedigree-flattening]`, `[^bho-blomefield-vol7-west-barsham-descent-cross]`, `[^hop-gurney-johnv-deathdate]`, `[^dg-supp-ipm-johnv-10henryiv]`, `[^ncc-reg-harsyk-edmund-will]`, `[^hop-gurney-surflete]`) are all uniquely named within the file; do not deduplicate.
3. Open `fact-sheets/g22-robert-gournay-fact-sheet.md`. Apply the substring replacement in §3a on the second `<li>` of the Highlights `<ul>` (line 73). No other factsheet edits.
4. Verify no other files reference the inserted footnote handles. Verify the apply session has not introduced any orphaned footnote definitions or unreferenced footnote markers.
5. Spot-check the rendered output for the companion and factsheet to confirm the additions parse correctly under the site's markdown renderer.

No file moves. No file creation outside the markdown additions and the two JSON entries. No validations file. The 1405 Cressingham fine and the Edmund-G23-NCC-will leads will receive their own future patchsets when the underlying source documents (Walter Rye Feet of Fines vol. 2 page-image / OCR; NCC Reg. Harsyk fol. 34 scan) are extracted.
