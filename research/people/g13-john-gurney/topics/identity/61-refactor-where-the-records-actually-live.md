<!-- WIP refactor unit, July 2026. Not yet in the G13 context graph; no prose markers. Graph-bearing
     content is tracked in sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# Where the south-Midlands records actually live — and a dead-end that isn't one

Twice now a search has failed because the records of a place are not kept in that place. The
Pakington family's Aylesbury Vale deeds sit at **Worcestershire** Archive, invisible to any
Buckinghamshire search. This unit records the same lesson applied to the ecclesiastical
jurisdictions, where it closes a standing dead-end.

## The candidate belt sits across three jurisdictions in two dioceses

The unaccounted-for men run across a compact stretch of country — Aylesbury Vale, the Chilterns, and
the Bedfordshire and Hertfordshire borders — that looks like one region and is not one jurisdiction:

| County | Archdeaconry | Diocese | Records held at |
|---|---|---|---|
| Buckinghamshire | **Buckingham** | Lincoln | Buckinghamshire Archives (D/A/We, D/A/Wf) |
| Bedfordshire | **Bedford** | Lincoln | Bedfordshire Archives, series **`AB`** |
| Hertfordshire (the St Albans part) | **St Albans** | **London** | Hertfordshire Archives and Local Studies, series **`ASA`**[^asa] |

The repo has read the Buckinghamshire tier at printed-index level and recorded the other two as gaps.
Neither is a gap in the records; both are gaps in the finding aids consulted.

## The Hertfordshire dead-end has a route, and it is catalogued

The standing action reads: *"Hertfordshire probate tier — find a route. No Hertfordshire volume exists
in the published-index dataset at all (a control search on a common surname also returns zero) … this
is a real gap."*[^r07] That is an accurate statement about the **FindMyPast published-probate-index
dataset**, and it was read as a statement about Hertfordshire probate. It is not.

**The Archdeaconry of St Albans series is catalogued to item level and reachable.** Its probate
records run in four principal series — registered wills `ASA/AR`, filed wills `ASA/AW`, inventories
`ASA25`, and probate and administration act books `ASA26` — with a further series of draft, probate
copy, office copy and original wills at `ASA27/5`, 1563–1700.[^asa-probate] The registered-will
volumes are individually described, and one of them lands exactly on the window that matters:

```
ASA/AR/6    1552-1574   Named after first testator. Wills 1553-1555 missing.
ASA/AR/8    1610-1636   Named after first testator. Testators whose filed wills are in
                        the series ASA/AW are ticked in red.
ASA/AR/10   1686-1717
ASA27/5     1563-1700   Draft, probate copy, office copy and original wills
ASA26/2     1660-1687; 1699-1714   Act book, with contemporary index to deceased persons' names
```

**`ASA/AR/8`, 1610–1636, is the volume that would hold Candidate C's household head** if he died in
the emigration window — and it carries a contemporary calendar of testators, so it is name-searchable
at the volume rather than requiring a folio walk.

## Why this converges with the Candidate C parish finding

The parallel finding in the family-matching sweep is that FamilySearch indexes Candidate C's
eight-child household not at Berkhamsted but at **St Peter, Hertfordshire — St Peter's, St
Albans.**[^stpeter] The two results line up: **St Peter's is in the Archdeaconry of St Albans.** If
the household is where FamilySearch puts it, then its probate jurisdiction is `ASA`, and both the
parish and the court are now identified after a year of the file recording each as a blank.

That is worth stating plainly as a methodological result. Two independent "not found" statements —
no Berkhamsted Gurney in the Hertfordshire parish collection, and no route to Hertfordshire probate —
were **both artefacts of looking in the wrong place**, one a parish attribution and one a finding
aid. Neither was a statement about the records.

It does not revive Candidate C, who is eliminated on his own age: fathering from 1610 puts his birth
at about 1585–90, thirteen to eighteen years off the colonial John. That ground is immune to both
errors. What it does is make the elimination checkable instead of resting on two mislaid negatives.

## Marriage licences: three separate series, none of them swept

The same split governs the record class that would settle the missing step for every Buckinghamshire
survivor — a **John Gurney × Mary marriage, c.1626–1635**. A licence, rather than banns, would sit in
whichever of the three jurisdictions the couple married under, and the surviving series are held
separately:

- **Archdeaconry of St Albans** — marriage licences appear both as a distinct series (`ASA23`) and
  entered in the act books (`ASA26/2` onward, "includes grants of marriage licences").[^asa-ml] The
  catalogued `ASA23` pieces cluster in the eighteenth century, so the seventeenth-century licences
  are most likely inside the act books rather than in a separate series — which is exactly the kind of
  thing a class-level search misses.
- **Archdeaconry of Bedford** — series `AB` at Bedfordshire Archives, whose own glossary of court
  terms describes act books as "registers of civil suits … testamentary and matrimonial cases".[^ab]
- **Archdeaconry of Buckingham** — at Buckinghamshire Archives, alongside the probate tier already
  read at printed-index level.

The repo's licence sweeps to date cover the **Norwich** church courts and the **Bishop of London's**
registry, both run for Francis G14, plus the national IGI marriage set.[^licence-sweeps] **None of
the three south-Midlands archdeaconry licence series has been searched**, and they are the natural
home of a licence for any of the Buckinghamshire, Bedfordshire or Hertfordshire candidates.

This is a coverage statement, not a finding. But it changes the standing of an existing negative: the
case file's "no John Gurney + Mary marriage 1620–1635 surfaces in eastern-England parish-marriage
indexes" is a statement about **parish registers and register-derived indexes**. Licences are a
different class, held elsewhere, and a couple marrying by licence away from their home parish is
precisely the case a parish-register sweep is worst at catching.

## What this is worth

Modest and concrete. Nothing here names a man. It converts two logged dead-ends into addressable
targets, identifies one volume that can be asked a direct question, and names a record class for the
leading rival group that has never been searched.

The generalisable lesson is the one the Pakington deeds already taught: **before recording that a
county's records are unreachable, establish which jurisdiction actually held them and which
repository actually keeps them.** Twice now the answer has been "not the county you were looking in."

## Crosslinks

- [`60-refactor-matching-by-family-not-by-man.md`](60-refactor-matching-by-family-not-by-man.md) — the St Peter, St Albans parish attribution this converges with
- [`52-refactor-bucks-herts-elimination.md`](52-refactor-bucks-herts-elimination.md) — the coverage limits this qualifies
- [`55-refactor-central-court-and-estate-records.md`](55-refactor-central-court-and-estate-records.md) — the Pakington deeds at Worcestershire, the first instance of the same lesson
- [`59-refactor-open-actions.md`](59-refactor-open-actions.md) — open actions arising
- Graph tracker: [`sources/intake/g13-graph-breadcrumb.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/intake/g13-graph-breadcrumb.md)

[^asa]: Hertfordshire Archives and Local Studies, `ASA`, "Records of the Archdeaconry of St Albans", 1415–1995, catalogued in the Discovery catalogue and read 28 July 2026. The diocesan attribution is confirmed independently by The London Archives, `A/CSC/1430`, 3 July 1641, a probate of the will of Susan Moffett of Chipping Barnet, Hertfordshire, widow, described as "proved in Archdeaconry of St. Albans, **diocese of London**". Buckinghamshire and Bedfordshire lay in the diocese of Lincoln in the same period. Source ID: `tna-discovery-catalogue`.
[^r07]: [`59-refactor-open-actions.md`](59-refactor-open-actions.md), action R-07, and [`52-refactor-bucks-herts-elimination.md`](52-refactor-bucks-herts-elimination.md) §"Coverage limits that bound these negatives", where the underlying negative is a FindMyPast search of "England & Wales Published Wills & Probate Indexes, 1300–1858" with `place=hertfordshire` returning zero alongside a zero control on a common surname — establishing that no Hertfordshire volume is in that dataset. Cross-reference, not a source.
[^asa-probate]: Hertfordshire Archives and Local Studies, series description for the `ASA` probate records: "The probate records consist of three principal series — registered wills (ASA/AR), filed wills (ASA/AW) and inventories (ASA25) — together with probate and administration act books (ASA26)." Individual registered-will volumes as catalogued: `ASA/AR/3` 1536–1557; `ASA/AR/4` 1536–1539; `ASA/AR/5` 1540–1546; `ASA/AR/6` 1552–1574 (wills 1553–1555 missing); **`ASA/AR/8` 1610–1636**; `ASA/AR/10` 1686–1717; `ASA/AR/14` 1808–1857. Also `ASA27/5`, "Draft, probate copy, office copy and original wills", 1563–1700. Catalogue level, read 28 July 2026. Source ID: `tna-discovery-catalogue`.
[^stpeter]: [`60-refactor-matching-by-family-not-by-man.md`](60-refactor-matching-by-family-not-by-man.md) §"Candidate C is indexed at St Albans, not Berkhamsted". Cross-reference, not a source.
[^asa-ml]: Same catalogue: `ASA23/1` (1743), `/5` (1747), `/8` (1750), `/10` (1752), `/12` (1754) and `/14` (1691), each described simply as "Marriage Licences"; and the act books `ASA26/3` (1687–1702), `ASA26/4` (1702–1732) and `ASA26/5` (1753–1797), each noted as including grants of marriage licences, `ASA26/4` carrying "Contemporary list … of marriage licences as issued". Source ID: `tna-discovery-catalogue`.
[^ab]: Bedfordshire Archives, `AB`, 1515–1990, whose catalogue carries a glossary of terms used in the archdeaconry court, defining act books as "Registers of civil suits between party and party. They comprise testamentory and matrimonal cases, suits for subtraction…". Source ID: `tna-discovery-catalogue`.
[^licence-sweeps]: [`51-refactor-francis-marriage-death-and-pease.md`](51-refactor-francis-marriage-death-and-pease.md) §"There is no earlier marriage", tabulating the sweeps of Ancestry's "London and Surrey, Marriage Bonds and Allegations, 1597–1921" (the Bishop of London's registry), Ancestry's "Norfolk, Indexes to Wills, Probate, Administrations and Marriage Licence Bonds, 1371–1858", FindMyPast's "Norfolk Banns and Marriages" (which includes Marriage Licence as an event type), and the England-wide IGI-derived "England, Select Marriages, 1538–1973"; and the offline Norwich licence residue at action R-06. Cross-reference, not a source.
