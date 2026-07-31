<!-- July 2026 refactor working round. Its findings are carried in the permanent identity units
     30- to 39-, which are the current account; this file is retained as the working record,
     including its own correction and retraction trail, which is deliberate and belongs to the
     research layer. Not yet in the G13 context graph — graph-bearing content is tracked in
     sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# The Berkhamsted burials exist — the departure-shaped gap does not

## The finding

**Great Berkhamsted's burial register survives for 1600–1660, is transcribed, and contains sixteen
Gurney-variant burials.** The claim on which Candidate C(ii) was opened — *"no Gurney burial at Great
Berkhampstead at any date, in FindMyPast's entire parish-burial corpus"* — is false.[^unit64] Five
Gurneys were buried in the parish between November 1637 and March 1638/9, including **two of C(ii)'s
own children**, and a **Richard Gurney was buried there on 28 June 1638**.

The household did not vanish. It was dying.

## The positive control that settled it, and the two defects it exposed

The method's check C2 requires every sweep to return a record already known to exist and in scope.
Run on Hertfordshire Burials, a Smith sweep at Berkhamsted returns burials at 1583, 1592, 1630, 1633,
1643 and 1660 — so the series is present and transcribed across exactly the window C(ii) needs.[^control]

The July negative had been produced by two independent query defects, each of which fails closed:

1. **`lastname=gurn*` does not reach `Gourney`.** The Berkhamsted family is indexed in the burial set
   predominantly under *Gourney*, and a wildcard on the `gurn` stem cannot match it. The five
   seventeenth-century Gourney burials — Isabell 1601, Henry 1607, Jhon 1612, Jhon 1620, Elizabeth
   1639 — were invisible to the query that reported zero.[^gourn]
2. **The place token differs between the baptism and burial sets.** FindMyPast's Hertfordshire
   Baptisms and its cross-collection view label the parish *Great Berkhampstead*; **Hertfordshire
   Burials labels it `Berkhamstead`**. A `keywords=berkhampstead` filter returns zero against the
   burial corpus, and a `keywords=berkhamsted` filter also returns zero, while `keywords=berkhamstead`
   returns 78 Smith rows. The keyword is a literal token match, so both spellings tried in July missed
   a parish that is fully present.[^placetoken]

Neither defect is exotic. Both are the same failure the method document opens with — a sweep on one
surname stem in one view, reported as a statement about the record — and this is the second time the
`gurn*` stem alone has manufactured a false England-wide negative in eight days.

**The repo already held the answer, in two places.** `data/sources.json` has carried, since a walk of
9 May 2026, the note that the Hertfordshire Burials set holds "only two seventeenth-century
Berkhamsted entries, Jhon Gourney 1612 and 1620."[^registry] And unit `37-identity-assessment.md`
states the same thing in its own prose: *"the only seventeenth-century Berkhamsted burials under the
name are two entries for a Jhon Gourney, in 1612 and 1620."*[^unit37]

So the July sweep contradicted both the project's source registry **and** a graph-bearing research
unit, and reported the contradiction as a discovery. This is the fourth instance of the S13 failure —
prior repo work not read — and the first in which the overlooked material was not a stale side file
but the identity assessment itself. The correction is to widen check C1 from "the research layer" to
"the research layer and the source registry", which is recorded as an amendment in unit 65.

## The Berkhamsted Gurney burial roster

Sixteen burials, all at Berkhamsted (distinct from Little Berkhamstead, a separate parish twenty
miles east, which the same keyword also matches and which carries no Gurney entry in this
window).[^roster]

| Burial date | Name as indexed | Bearing |
|---|---|---|
| 1579 | Jhone Gernnye | Pre-dates the household |
| 1601 | Isabell Gourney | |
| 1607 | Henry Gourney | |
| 1612 | Jhon Gourney | An adult or child John, while C(i) is still fathering |
| 1620 | Jhon Gourney | **Candidate for C(i)'s own burial** — see the shape section |
| 1620 | Thomas Gorne | |
| 7 Nov 1637 | Joane Gurney | |
| 28 Jun 1638 | **Richard Gurney** | **The critical row** |
| 1 Oct 1638 | William Gurney | |
| 21 Feb 1638/9 | Elizabeth Gurney | **C(ii)'s daughter, baptised 2 Aug 1629** |
| 1639 | Elizabeth Gurnie | Probably a second index row for the same event |
| 9 Mar 1638/9 | **Francis Gurney** | **C(ii)'s son, baptised 1 Mar 1636/7** |
| 1639 | Thomas Gurney (two rows) | |
| 1643 | Margaret Gurney | |
| 1643 | Thomas Gurney | |

**Two of these are C(ii)'s children beyond reasonable doubt.** FamilySearch's *England, Births and
Christenings* records Elizabeth Gurnie, christened 2 August 1629, parents John Gurnie, dead 21
February 1639; and Francis Gurney, christened 1 March 1637, parents John Gurney, dead 9 March 1639.
The burial register gives burial dates of **21 Feb 1638** and **09 Mar 1638** — identical events in
Old Style reckoning.[^transcripts] Two providers, two record classes, the same two deaths. This is
what the deviation audit called a within-record corroboration rather than a comparator argument: the
dates were derived independently and match to the day.

## What this does to Candidate C(ii)

**The departure-shaped gap is gone.** C(ii) was opened on the deviation audit's own untried test —
*"which John Gurney household's records stop between 1635 and 1641 without a burial or probate?"* The
answer for Berkhamsted is that the records do not stop; the family is buried in the parish through
1643. A household that loses four or five members in eighteen months and then stops appearing in the
baptism register is displaying mortality, not departure.

**The Richard row is the sharpest single blow, and it must be stated conditionally.** If the Richard
buried 28 June 1638 is the Richard baptised at Berkhamsted 15 December 1626, then C(ii)'s
best name-match child died in England at eleven, while the colonial Richard Gurney of Weymouth was
alive and a freeman in 1681 — and C(ii) collapses outright. The alternatives, per the method's shape
discipline, are:

- **(a)** He is the Richard baptised 1626, son of John — C(ii) collapses.
- **(b)** He is **Richarde Gurney, baptised 1635, son of Thomas** — a three-year-old of the
  neighbouring Gurney household. Equally consistent with a June 1638 burial in a mortality year.
- **(c)** He is an adult Richard Gurney of the parish, unbaptised there.

**(c)** is weak: no Richard Gurney baptism at Berkhamsted other than 1626 and 1635 appears in the
whole run.[^bapts] Between **(a)** and **(b)** the index cannot discriminate — FindMyPast's
Hertfordshire Burials transcript carries name, burial date and place only, with no age and no
parent. **The discriminating evidence is the register image itself**, which for this period normally
gives "son of X"; it is the first action arising.

**Mary is absent at parish level, not merely at household level.** Across every surname stem and
every father, the Berkhamsted baptism corpus contains **no Mary Gurney at any date** between 1544 and
1888 — the only Mary is a 1730 burial.[^bapts] The single strongest objection to C(ii) is therefore
stronger than unit 64 recorded it: it is not that the John household lacks a Mary, it is that the
parish does.

**C(ii)'s head still has no burial**, and that is the one thread still holding. No John
Gurney-variant burial occurs at Berkhamsted after 1620, and none anywhere in Hertfordshire between
1620 and 1690 except Jonathan Gurney at Bovingdon in 1682–3.[^johnburials] But this cannot be read as
departure, because FindMyPast's own description of the Hertfordshire set states that **many
Hertfordshire registers are "sadly defective during the Civil War and Commonwealth period
(1643–1660)"** — and the Berkhamsted Gurney burials stop in 1643 and do not resume until 1711, which
is the signature of that defect rather than of an empty parish.[^defective] A head of household who
died between 1643 and 1660 would be invisible.

**Net: C(ii) falls from 9% to 4%.** He keeps the right age and an unburied head inside a defective
window. He loses the departure gap entirely, loses the parish-level Mary, probably loses Richard, and
gains a documented family catastrophe that explains the end of his baptism run without any crossing.

## Shape: the parish held four Gurney households, not one

Unit 64 read the Great Berkhampstead baptisms as a father-and-son pair because the parent-name sweep
returned only rows with a father named John. Read as a parish rather than as a query result, the
baptism corpus carries **four contemporaneous Gurney households**, distinguished by the father's
forename:[^bapts]

| Father | Children |
|---|---|
| **John / Jhon** | Hugh 1597, Anne 1599, Amye 1602, Bridgett 1606, Henrye 1610, Sara 1615 · Jhon 1624, Richard 1626, Elizabeth 1629, Michaell 1631, Sarah 1634, Francys/Francis 1636/7 |
| **Thomas** | John 1588, Eliz 1591, Willm 1594, Thomas 1604, Nicolas 1607, Richarde 1635, Thomas 1638, Thomas 1640 (mother Elizabeth) |
| **Edward / Edwarde** | James 1603, Elisabeth 1606, Susanna 1611 |
| **William / Willyam** | Anna/Anne 1594, Willyam 1632 |

This matters in three ways. It means the 1637–1643 burials **cannot be assigned wholesale to the John
line** — the Thomas household was actively baptising in 1638 and 1640 and is the more likely owner of
the Thomas burials. It supplies the alternative Richard at **(b)** above. And it shows that the
"forty years of fathering, therefore two men" argument was reasoning from a filtered view of a parish
that in fact held a Gurney kindred.

**The father/son split itself gains its first real evidence.** A **Jhon Gourney was buried at
Berkhamsted in 1620** — after C(i)'s last recorded child (Sara 1615) and before C(ii)'s first (Jhon
1624). That is exactly the shape hypothesis (b) predicts. It is not proof: a second Jhon Gourney was
buried in 1612 while C(i) was demonstrably still fathering, so the parish held more than one John,
and the 1620 burial could be a son, a cousin, or the John baptised 1588 to Thomas. The
discriminating evidence remains the elder John's will in the Archdeaconry of St Albans registered
volume `ASA/AR/8` (1610–1636), which is an offline pull at Hertfordshire Archives.

## The marriage: absent from the county, not just the parish

**No John Gurney-variant marriage occurs at Great Berkhamsted between 1582 and 1722.** The parish's
Gurney marriages in that span are all brides: Joan × Nicholas Benning 1582, Elizabeth × William
Foordan 1588, Anne × Isaac Thorne 1602, Alice Gourneye × John Androe 1616, Elisabeth Gourneye × John
Hunte 1617.[^marr] The two 1616/1617 rows briefly looked like John Gurney grooms; the mirror rows
resolve them as Gourney brides marrying men named John.

Widened to the county, **no John Gurn\*/Gourn\* marriage is recorded anywhere in Hertfordshire
between 1600 and 1654** — the set's John Gurney marriages begin at Tring in 1655, with John Gurnett
events at 1567 and 1646 bounding the negative on both sides.[^hertsmarr] Neither C(i) nor C(ii)
married in the county, which is unremarkable for grooms but does mean **C(ii)'s wife cannot be named
from Hertfordshire records**, and the test of her against a Mary cannot be run there. This is a
direct argument for R-33: the south-Midlands archdeaconry licence series is where a groom marrying
out of county would surface.

## R-47 — the three households the March 2026 matrix carried

**Bishop's Cleeve, Gloucestershire — not a Gurney household.** *Maria Gorne, 2 March 1627, father
John Gorne* belongs to a **Garne** family, a settled Cotswold surname distinct from Gurney. A
parent-name sweep on the household returns children of a John Garn/Garne at Bishop's Cleeve running
**Mathew 1629, John 1679, John 1681, James 1683, Frances 1687, Giles 1692, Mary 1712, Alce
1714**.[^garne] A lineage baptising in the same parish for eighty-five years across and beyond the
emigration window is not an emigrant household. The same reading disposes of **CR-022, Marye Garne
1638 at Compton Abdale**, twenty miles away in the same county. Both are retired from the candidate
set.

> **Corrected 2026-07-29.** This paragraph originally added "and the surname is not a Gurney variant,"
> and directed that both rows be reclassified from Gurney-variant to Garne. **The surname-class part is
> withdrawn** — *Garne* is a moderate-weight Gurney form and variant plausibility is a per-record
> weight, never a class boundary (unit 69). What retires these two rows is the household's own
> eighty-five-year continuity in one parish, which is unaffected.

**Earsham, Norfolk — eliminated on the wife's name and on a documented English death.** The Norfolk
Baptisms set carries four Girney baptisms at Earsham: **John 1636, father John**; **Henry 1638,
father John, mother "Alex"**; and two to a father *Sion* — Steven 1637 and Susan 1638.[^earsham] The
John Girney household therefore has a wife whose name is not Mary and a further son in 1638, and the
case file already records the will of John Gurney of Earsham proved in 1639. Two independent grounds;
Earsham closes.

**Upton upon Severn, Worcestershire — a deeply rooted local family, still open in its detail.** The
row that made this interesting — *Mary Gurney, 7 September 1629, mother Mary, no father named* — sits
inside a continuous Upton on Severn Gurney presence running from **Annes 1582** through 1666, 1709,
1713, 1715, 1757, 1768, 1779 and into the nineteenth century.[^upton] The case file separately records
John Gurney buried at Upton on Severn St Peter & St Paul on 19 January 1666. The "partial
transcription of a John-and-Mary household" reading remains formally possible, but it now has to be
read against a parish where the surname never leaves. Held as low priority rather than closed; the
1620s–1640s Upton rows have not been individually assembled, and the Worcestershire county set is
**not** the instrument for it (see coverage below).

## R-48 — the undated Buckinghamshire row is defective at source

Catalogue row CR-025 cannot be placed from the index, because the index does not hold the
information. The transcript reads: baptism date **"11 Jul ?"**, baptism year **"1575-1813"**, place
**blank**, archive reference **`D/A/T/`** with no piece number, father John Gourney.[^undated] The
year field is the register's date range standing in for a year the transcriber could not read, and
the archive reference is the bare bishop's-transcript series.

One narrowing is available. In the Buckinghamshire Baptism Index the *Gourney* spelling is
overwhelmingly a **Chesham** spelling — John Gourney entries at 1540 (father Rychard), 1569 (father
Willm), 1591 (father Ryc), 1600 (father Willm, mother Mary), against Stone 1718.[^bucksgourn] But
Chesham's register range in this index is recorded as 1576–1682, which does not match the 1575–1813
range on the undated row, so the spelling prior and the range evidence point in different directions.
The remaining route is a catalogue question — **which Buckinghamshire parish's D/A/T bishop's
transcripts run 1575–1813** — not a search question.

## Coverage statements arising

Recorded so these are never re-run as searches, per stopping-rule item 5.

- **FindMyPast Hertfordshire Burials covers Berkhamsted across 1583–1660 and again from 1711**, with a
  gap 1644–1710 consistent with the set's own statement that Hertfordshire registers are widely
  defective for 1643–1660.[^defective] Any Berkhamsted burial negative for 1644–1660 is inside a known
  defect and is not evidence.
- **FindMyPast Norfolk Baptisms has no Yaxham coverage before 1806.** A Smith control at Yaxham
  returns 125 rows, every one of them 1806 or later, and **zero rows for 1560–1640**.[^yaxham] The
  R-23 test of Arthur Gurney's household has therefore **never actually been run** on this
  instrument, and a Gurney zero at Yaxham from it means nothing. Route R-23 to Ancestry collection
  61045 (Norfolk Record Office partnership, image-linked) via its browse panel, or to NROCAT for
  register survival; Ancestry's `birth=` place parameter does not bind and cannot be used to scope it.
- **FindMyPast Worcestershire Baptisms does not cover Upton on Severn.** A Smith control returns
  zero.[^worcs] The Upton rows reach us only through *England Births & Baptisms 1538–1975*.
- **The `sid=102` parent-search pool does not include Norfolk Baptisms.** A parent sweep for a father
  John Gurney/Girney at Earsham returns zero, while the Norfolk county set returns the 1636 and 1638
  baptisms with the father indexed.[^earsham] The positive control passes on the same instrument —
  a parent sweep scoped to Hitcham returns Mary Gurny 1631 — so the instrument works and the pool is
  the limit.[^hitchamcontrol] **This materially qualifies R-42: the 315-row parent-name sweep is not
  England-complete, and any household it fails to return may simply sit in a county set outside its
  pool.**

## The departure-gap test has an instrument, and it was never used

The deviation audit's fourth recommendation — *invert the method: ask which John Gurney household's
records stop between 1635 and 1641 without a burial or probate* — has been treated as a thing to do
parish by parish. It is not. **The parent-name search runs over burials as well as baptisms.** A
father-John-Gurney sweep for 1625–1635 reports, in the same facet panel, **108 parish baptisms, 76
parish burials and 13 parish marriages**.[^facets] Switching `collection=parish+burials` therefore
asks, in one query, *which children of a John Gurney were buried in England* — and the households
whose children appear in the baptism arm but not the burial arm are exactly the departure-shaped
gaps.

That is the test C(ii) failed today, run at national scale instead of one parish at a time. It has
never been executed, and it is now the highest-value single query left on the child inventory. Two
mechanics have to be right first: the year parameter in this mode is **`yearofbirth=`**, because
`year=` renders a chip and then returns a silent zero;[^yearparam] and the pool excludes some county
sets, so the burial arm needs pairing with county-set runs exactly as the baptism arm does.

The wider point is the one the method document was written for. This pass spent most of its effort
establishing that an instrument said what it appeared to say, and the single reframing that came out
of it — that the departure question is a *burial-arm* query rather than a parish crawl — was worth
more than the searching. **Method work keeps outperforming search volume on this problem.**

## Consequence for the probability table

One row moves on evidence. **C(ii): 9% → 4%.** The five points released are redistributed to the rows
this pass indirectly strengthens, and that redistribution is normalisation rather than new evidence
for those rows — with one exception. *Documented but never assembled* rises on genuine evidence: this
pass found real records, in the project's own source registry, that a sweep had reported as absent,
which is precisely the mechanism that row describes.

| Row | Was | Now |
|---|---:|---:|
| Documented but never assembled | 22 | **25** |
| No record survives or is indexed | 18 | 18 |
| B — son of Francis & Margaret Rybett | 11 | 11 |
| Ackworth | 7 | 7 |
| Cheddington 1608 | 6 | **7** |
| Bucks/Herts/Beds group | 6 | 6 |
| Hitcham | 4 | **5** |
| **C(ii) — the younger Great Berkhampstead John** | **9** | **4** |
| A(1603) Stewkley | 4 | 4 |
| D — London draper | 4 | 4 |
| Newgate apprentice | 3 | 3 |
| Weston Turville | 3 | 3 |
| C(i) elder Berkhampstead | 1 | 1 |
| Stewkley 1611 | 1 | 1 |
| Other | 1 | 1 |

Sums to 100.

## A note on the method, under check C7

The method document's stop-and-reset trigger fires after two corrections in the same domain. This
pass produced two — the surname-stem defect and the place-token defect — inside a single test, and
both are instances of the failure class the method was written to prevent. The method itself held:
**check C2 caught both within three queries**, before any of the July work was extended. What failed
was that check C1's "read the repo first" had never been extended to `data/sources.json`, where the
answer had been sitting for eleven weeks. The correction to make is to the scope of C1, not to the
method's structure, and it is recorded as an amendment in unit 65's source inventory rather than as a
fresh reset.

## Crosslinks

- [`64-refactor-berkhamsted-reopened.md`](64-refactor-berkhamsted-reopened.md) — the unit this corrects
- [`65-refactor-child-inventory-method.md`](65-refactor-child-inventory-method.md) — the method executed here
- [`63-refactor-child-sweep-closed-and-reassessment.md`](63-refactor-child-sweep-closed-and-reassessment.md) — the superseded probability table
- [`59-refactor-open-actions.md`](59-refactor-open-actions.md) — actions arising
- Catalogue: `research/people/g13-john-gurney/coverage/child-record-catalog.csv`
- Graph tracker: [`sources/intake/g13-graph-breadcrumb.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/intake/g13-graph-breadcrumb.md)

[^unit64]: [`64-refactor-berkhamsted-reopened.md`](64-refactor-berkhamsted-reopened.md), footnote on burials. Cross-reference, not a source; the claim it makes is disproved by the record evidence cited below.
[^control]: Hertfordshire Burials, Hertfordshire Archives and Local Studies, served via FindMyPast; authenticated session, 28 July 2026. Query `datasetname=hertfordshire+burials&sid=103&lastname=smith&keywords=berkhamstead` — 78 rows, including burials at Berkhamstead in 1583, 1592, 1630, 1633, 1643 and 1660. Source ID: `findmypast-hertfordshire-burials`.
[^gourn]: Same set and session. Query `lastname=gourn*` (no place filter) — 9 rows, of which five are at Berkhamstead: Isabell Gourney 1601, Henry Gourney 1607, Jhon Gourney 1612, Jhon Gourney 1620, Elizabeth Gourney 1639. Source ID: `findmypast-hertfordshire-burials`.
[^placetoken]: Same set and session. `keywords=berkhamsted` → 0 rows; `keywords=berkhampstead` → 0 rows; `keywords=berkhamstead` → 78 rows, on an otherwise identical Smith query whose unfiltered form returns 10,912 rows including a Smith burial at "Berkhamstead" in 1583. Source ID: `findmypast-hertfordshire-burials`.
[^registry]: `data/sources.json`, entry `findmypast-hertfordshire-burials`, notes field as it stood before this pass, recording a walk of 9 May 2026: "only two seventeenth-century Berkhamsted entries, Jhon Gourney 1612 and 1620". Cross-reference to the project's own registry, not a source; the underlying record is the Hertfordshire Burials set cited above.
[^unit37]: [`37-identity-assessment.md`](37-identity-assessment.md), §"Candidate C — Berkhamsted, Hertfordshire". Cross-reference, not a source; the underlying record is the Hertfordshire Burials set cited above. Note that unit 37's wider statement — that these are the *only* seventeenth-century Berkhamsted Gurney burials — is itself too narrow, because it was made from a John-forename query; the parish holds eleven more under other forenames.
[^roster]: Hertfordshire Burials, authenticated session, 28 July 2026, compiled from `keywords=berkhamstead` runs on the stems `gurn*` (15 rows), `gourn*`, `gorn*` (1 row, Thomas Gorne 1620), `garn*` (2 rows, neither Gurney), `gern*` (1 row, Jhone Gernnye 1579), `girn*` (0 rows) and `hurn*` (1 row, John Hurnall 1820 — the wrong-initial class of R-30, tested and clean here). Source ID: `findmypast-hertfordshire-burials`.
[^transcripts]: FindMyPast transcripts `GBPRS/D/72723160` (Elizabeth Gurney, burial date 21 Feb 1638, Berkhamstead), `GBPRS/D/72723162` (Francis Gurney, 09 Mar 1638), `GBPRS/D/72723126` (Richard Gurney, 28 Jun 1638), `GBPRS/D/72723092` (Joane Gurney, 07 Nov 1637), `GBPRS/D/72723150` (William Gurney, 01 Oct 1638), read 28 July 2026. Against FamilySearch, *England, Births and Christenings, 1538–1975*: "Elyzabeth Gurnie, Christening 2 August 1629, St Peter, Hertfordshire, Death 21 February 1639, Parents John Gurnie"; "Francis Gurney, Christening 1 March 1637, St Peter, Hertfordshire, Death 9 March 1639, Parents John Gurney". Source IDs: `findmypast-hertfordshire-burials`; `fs-england-births-christenings`.
[^bapts]: Hertfordshire Baptisms, Hertfordshire Archives and Local Studies, served via FindMyPast; authenticated session, 28 July 2026. Queries `lastname=gurn*&keywords=berkhamstead` (19 rows) and `lastname=gourn*&keywords=berkhamstead` (18 rows), read with the Father's first name(s) and Mother's first name(s) columns. No Mary appears in either result set at any date. Source ID: `findmypast-hertfordshire-baptisms`.
[^johnburials]: Hertfordshire Burials, 28 July 2026. `firstname=jhon*&lastname=gourn*` (county-wide, no place filter) → 2 rows, Berkhamstead 1612 and 1620. `firstname=jo*&lastname=gurney&yearofdeath=1650&yearofdeath_offset=40` → 3 rows: Joane Gurney 1637 Berkhamstead, Jonathan Gurney 1682 and 1683 Bovingdon. Note that `jo*` does **not** match the seventeenth-century spelling `Jhon`, which is why the two stems must both be run. Source ID: `findmypast-hertfordshire-burials`.
[^defective]: FindMyPast, *Hertfordshire Burials* record-set description, read 28 July 2026: of Hertfordshire's 132 ancient parishes only 16 have registers surviving from 1538, and "many registers are sadly defective during the Civil War and Commonwealth period (1643-1660)." Source ID: `findmypast-hertfordshire-burials`.
[^marr]: Hertfordshire Banns & Marriages, served via FindMyPast; authenticated session, 28 July 2026. `lastname=gurn*&keywords=berkhamstead` → 19 rows; `lastname=gourn*&keywords=berkhamstead` → 3 rows (Anne Gourney × Isaac 1602; Alice Gourneye × John 1616; Elisabeth Gourneye × John 1617). The mirror query `spouselastname=gourn*&keywords=berkhamstead` names the husbands: John Androe 1616, John Hunte 1617, Isaac Thorne 1602. Source ID: `findmypast-hertfordshire-banns-marriages`.
[^hertsmarr]: Same set and session. `firstname=john&lastname=gurn*` (county-wide) → 57 rows; the earliest Gurney-surname events are John Gurnett × Alis, Cheshunt 1567 and John Gurnett × Elizt, St Albans Abbey 1646, then John Gurney × Elizabeth, Tring 1655. No John Gurney marriage falls between 1600 and 1654. Source ID: `findmypast-hertfordshire-banns-marriages`.
[^garne]: FindMyPast cross-collection parent search, authenticated session, 28 July 2026: `sid=102&fatherfirstname=john&fatherfirstname_variants=true&fatherlastname=gorne&fatherlastname_variants=true&keywords=cleeve` → 8 parish-baptism rows, all *England Births & Baptisms 1538–1975*, all at Bishop's Cleeve, Gloucestershire: Garne Mathew 1629, Garne John 1679, Garn John 1681, Garne James 1683, Garn Frances 1687, Garne Giles 1692, Garne Mary 1712, Garne Alce 1714. Source ID: `findmypast-uk-parish-baptisms`.
[^earsham]: FindMyPast Norfolk Baptisms (Norfolk Family History Society transcription), authenticated session, 28 July 2026. `lastname=girn*&keywords=earsham` → 4 rows: Henry Girney 1638, father John, mother "Alex"; John Girney 1636, father John; Susan Girney 1638, father Sion, mother Anna; Steven Girny 1637, father Sion, mother Amy. The corresponding parent search on the cross-collection instrument (`sid=102`, father John Gurney and father John Girney, both variant-expanded, `keywords=earsham`) returns zero. Source IDs: `findmypast-norfolk-baptisms-index`; `findmypast-uk-parish-baptisms`.
[^hitchamcontrol]: FindMyPast cross-collection parent search, 28 July 2026: `sid=102&fatherfirstname=john&fatherfirstname_variants=true&fatherlastname=gurney&fatherlastname_variants=true&keywords=hitcham` → 1 row, Mary Gurny 1631, Hitcham, Buckinghamshire, Buckinghamshire Baptism Index. This is the positive control named in the method document at check C2, and it passes. Source ID: `findmypast-uk-parish-baptisms`.
[^upton]: FindMyPast cross-collection search, 28 July 2026: `sid=999&collection=parish+baptisms&sourcecountry=great+britain&lastname=gurn*&keywords=severn` → 118 parish-baptism rows, the great majority at Upton on Severn and Longdon by Upton on Severn, Worcestershire, running from Annes Gurney 1582 to the later nineteenth century. Source ID: `findmypast-uk-parish-baptisms`.
[^worcs]: FindMyPast Worcestershire Baptisms, 28 July 2026: `lastname=smith&keywords=upton` → 0 rows, against `lastname=gurn*&keywords=upton` → 0 rows. The control failing establishes that the county set does not cover the parish. Source ID: `findmypast-uk-parish-baptisms`.
[^yaxham]: FindMyPast Norfolk Baptisms, 28 July 2026: `lastname=smith&keywords=yaxham` → 125 rows, the earliest 1806; the same query with `year=1600&year_offset=40` → 0 rows. `lastname=gurn*&keywords=yaxham` → 0 rows, which the control shows to be uninterpretable. Source ID: `findmypast-norfolk-baptisms-index`.
[^undated]: FindMyPast transcript `GBPRS/BUCKINGHAMSHIRE/BAP/001824427`, Buckinghamshire Baptism Index, read 28 July 2026: First name John, Last name Gourney, Father's first name John, Father's last name Gourney, Baptism date "11 Jul ?", Baptism year "1575-1813", Register year range 1575-1813, Place blank, Archive Buckinghamshire Archives, Archive reference "D/A/T/", register type "Baptisms, marriages & burials", denomination Anglican. Source ID: `findmypast-bucks-baptism-index`.
[^facets]: FindMyPast cross-collection parent search, authenticated session, 28 July 2026: `sid=102&fatherfirstname=john&fatherfirstname_variants=true&fatherlastname=gurney&fatherlastname_variants=true&collection=parish+baptisms&sourcecountry=great+britain&yearofbirth=1630&yearofbirth_offset=5`. The left facet panel reports Parish Baptisms 108, Parish Burials 76, Parish Marriages 13, Wills & Probate 0. The variants engine is loose, so the row list mixes genuine Gurney households (Chesham, Toddington, East Claydon, Weston Turville, Eythorne) with Gray, Griffith, Gaune and unreadable-surname rows; the counts are an upper bound and the rows must be read. Source ID: `findmypast-uk-parish-baptisms`.
[^yearparam]: Same instrument and session. `year=1630&year_offset=10` returns **0 results** while rendering a "Year 1630" chip; `yearofbirth=1630&yearofbirth_offset=5` returns 108. Both facets are present in the sidebar and neither errors. Source ID: `findmypast-uk-parish-baptisms`.
[^bucksgourn]: Same set and session: `lastname=gourn*&firstname=john` → 7 rows — Chesham 1540 (father Rychard), Chesham 1569 (father Willm), the undated row, Chesham 1591 (father Ryc, mother Jaane), Chesham 1600 (father Willm, mother Mary), Stone 1718 (father Richard, mother Dorothy, two index rows). Source ID: `findmypast-bucks-baptism-index`.
