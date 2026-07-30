# Packet 57 — Buckinghamshire John Gurney individuation

> **STATUS 2026-07-26 — read this first.**
>
> **Phase 1 (index re-query) is COMPLETE and is written up in full below.** It resolved the
> Buckinghamshire cluster into named men, recovered two John Gurney households the project had
> never assessed, corrected three misattributed Prerogative Court of Canterbury wills, and returned
> a firm negative on the departure-shaped-gap test.
>
> **Phase 2 (image capture) has NOT been executed. No images are staged.** `images/packet-57-bucks-john-gurney-individuation/`
> holds a README stub and nothing else. The image targets are specified in §Phase 2 below and are
> ready to pull, but the pull itself is outstanding work.
>
> **Phase 1 also found a cheaper route to the question Phase 2 was meant to answer.** See
> §Probate supersedes the image pull.
>
> **SUPERSEDED IN TWO PLACES, 2026-07-27 — see
> [`packet-57-supplement-2026-07-27-elimination-pass.md`](packet-57-supplement-2026-07-27-elimination-pass.md).**
> (1) The **Buckinghamshire archdeaconry probate tier is online**, not a records-office request: British
> Record Society vol. 114, *Buckinghamshire Probate Index, 1483–1660*, is on FindMyPast as page images.
> It has been read. It adds three individuating English deaths (Monks Risborough 1623, **Hulcott 1630**,
> **Linslade/Southcott 1636**) and returns a bounded negative for Stewkley after 1592, Haddenham, Weston
> Turville, Hitcham, Amersham, Ivinghoe and Bierton after 1559. (2) The **departure-shaped-gap test in
> §(c) has been re-run as an elimination** against a supplied arrival constraint (absent from the 1636
> Weymouth grant) and against the colonial wife Mary's survival to 1661. Six men are eliminated on
> individuating records; five survive.

## Navigation

| § | Section | What it holds |
|---|---|---|
| 1 | [Method and coverage](#method-and-coverage) | What was queried, how, and where it stops |
| 2 | [The record table](#the-record-table) | One row per event, by parish |
| 3 | [(a) Distinct men](#a-how-many-distinct-john-gurney-men-do-the-mothers-names-resolve) | Nine-plus Johns, named with wives and children |
| 4 | [(b) John + Mary](#b-is-there-a-john-gurney--wife-mary-household-in-bucksherts-before-1660) | Negative, and it now survives a better index |
| 5 | [(c) Departure-shaped gaps](#c-departure-shaped-gaps-1635-1641) | The inverted test, run for the first time |
| 6 | [(d) Cowheard vs Oliffe](#d-the-1638-cowheard-marriage--not-settled-and-why) | Not settled by the index; why, and the better route |
| 7 | [(e) The 1603 Stewkley John](#e-the-1603-stewkley-john--no-burial-no-marriage-no-probate) | Still unaccounted; one premise corrected |
| 8 | [PCC corrections](#three-prerogative-court-of-canterbury-wills-are-misattributed-in-the-repo) | Two Bucks wills the project files under other counties |
| 9 | [Phase 2 brief](#phase-2--image-targets-not-yet-pulled) | Target vs context images, questions, staging path |
| 10 | [Not covered](#what-this-pass-did-not-cover) | Explicit gaps |

## Method and coverage

Worked 2026-07-26 against FamilySearch's **England, Buckinghamshire, Church Records, 1217–1994**
(collection 4380170) — the collection that indexes mothers, as against the older *England, Births
and Christenings, 1538–1975* (collection 1473014), which does not. Supplemented with FamilySearch's
**England, Hertfordshire, Parish Registers, 1538–1912** (collection 2388825), the Findmypast
Buckinghamshire Marriage Index, and the National Archives Discovery catalogue for probate.

Surname variants were run separately against the Buckinghamshire collection with exact matching.
Counts are the collection's whole-run totals, all dates:

| Variant | Records | Variant | Records |
|---|---:|---|---:|
| Gurney | 4,334 | Gurnay | 7 |
| Gurny | 128 | Gurnie | 4 |
| Garney | 120 | Gurnoe | 0 |
| Gourney | 45 | Gernne | 0 |
| Gorney | 22 | | |
| Girney | 12 | | |

`Gurnoe` and `Gernne` return nothing in Buckinghamshire; both are Norfolk/Yorkshire forms. `Garney`
and `Girney` are productive and carry real Bucks entries — Isaac Garney of Cheddington and John
Girney of Stewkley are the same families as their Gurney-spelled neighbours.

**Coverage limits that bound every negative below.** FamilySearch's search service caps unique
results at roughly 1,500 per query however deep the paging goes, and its `q.birthLikeDate`,
`q.anyPlace`, and `q.spouseSurname` parameters *rank* rather than *filter*. The 4,334-record
Buckinghamshire Gurney set was therefore assembled by relevance-ranked sweeps plus a per-parish
sweep of all twenty named parishes, not by exhaustive enumeration. 359 records fall in 1570–1700.

**Two parishes are absent from the Buckinghamshire collection for the seventeenth century, and both
matter.** Every one of the 28 Aylesbury Gurney records in the collection is nineteenth-century; the
1638–1653 Saint Mary baptisms exist only in *England, Births and Christenings*, which carries the
father and no mother. Amersham is likewise uncovered for the period except through the marriage
index. Chenies and Great Kimble return no Gurney record at all.

For Hertfordshire, 546 of 1,437 Gurney records were harvested. **Berkhamsted has no seventeenth-century
Gurney record in that collection** — the four Berkhamsted entries it holds are 1888 and 1927 — so
Candidate C's household is not reachable through it and its mothers cannot be recovered this way.

## The record table

All FamilySearch identifiers are the record ark suffix under `https://www.familysearch.org/ark:/61903/1:1:`.
Parents as indexed; where a mother is named the collection carries her, where only a father appears
the index carries no mother.

### Marriages, Buckinghamshire, to 1700

| Date | Parish | Couple | Ark |
|---|---|---|---|
| 5 Nov 1573 | Bierton with Broughton | John Gurney × Elizabeth Goringe | `685J-M5BR` |
| 30 Nov 1576 | Waddesdon | Margery Gurney × Hughe Browne | `685J-X9LD` |
| 1609 | Weston Turville | Issabell Gurney × Thomas Bowden | `685J-XZNS` |
| 11 Nov 1613 | Wingrave | Thomas Gurney × Katherine Goodspeed | `685J-H274` |
| 17 Nov 1617 | Marsworth | Richard Gurney × Elenor Tomkins | `685N-PZYN` |
| 21 Oct 1627 | Linslade | Ezechiel Gurney × Alice | `685J-VK1Z` |
| **24 Apr 1628** | **Bierton with Broughton** | **John Gurney × Alice Oliffe** | `685J-4JZW` |
| **30 Oct 1630** | **East Claydon** | **John Gurney × Elizabeth Lyne** | `685J-4TTN` |
| 17 Feb 1633 | Ivinghoe | Marie Gurney × Rogerus Surrey | `685J-KYSB` |
| **7 Feb 1638** | **Amersham** | **John Gurney × Avis Carter** | Findmypast, Bucks Archives PR4/1/1; Bishop's transcript D/A/T/4 |
| 17 Oct 1639 | Princes Risborough | Margaret Gurney × Robert Stallwood | `685J-ZYR1` |
| **22 Oct 1640** | **Ivinghoe** | **Johannes Gurney × Rebecka Coker** | `685J-285V` |
| 1 Dec 1661 | Marsworth | Joyce Gurney × Richard Paige | `685N-F46V` |
| 25 Jan 1663 | Edlesborough | John Gurney × Mary Kidgell | `685J-S14P` |
| 1 Oct 1668 | Mursley | Frances Gurney × Thomas Woodward | `685J-4J1J` |
| 22 Jul 1673 | Cublington | Jane Gurney × Richard Worrell | `685J-874M` |
| 26 Jul 1691 | Dinton | John Gurney × Susannah Smyth | `685J-795T` |
| 26 Oct 1700 | Chesham | John Gurney × Anne | `685N-83MC` |

The Findmypast Buckinghamshire Marriage Index additionally carries John Gurney marriages at Denham
(1572), Aylesbury (1584, 1620, 1638, 1644) and Farnham Royal (1629). The Aylesbury and Denham
entries sit in indexes that carry no spouse in the result view; the 1638 Aylesbury entry is the
known Anne Cowheard marriage.

### Baptisms and burials naming a John Gurney, 1570–1700

| Parish | Date | Event | Person | Father | Mother | Ark |
|---|---|---|---|---|---|---|
| Bierton | 7 Dec 1571 | burial | John | — | — | `6854-78TF` |
| Bierton | 12 Dec 1578 | baptism | William | John | not indexed | `6853-S341` |
| Bierton | 12 Dec 1578 | baptism | Marie | John | not indexed | `6853-S3HG` |
| Bierton | 4 Jul 1581 | baptism | John | — | — | `685S-T9Q4` |
| Bierton | 28 Jul 1581 | burial | John | — | — | `685W-R4S6` |
| Bierton | 23 Dec 1581 | burial | John | — | — | `685W-5PV7` |
| Bierton | 28 Jan 1596 | baptism | Harrie | John | not indexed | `685S-R2N3` |
| Bierton | 27 Jul 1602 | burial | John | — | — | `685W-1LTM` |
| **Hulcott** | 3 Jun 1571 | baptism | Silvester Gourney | John Gourney | not indexed | `6859-JM6W` |
| **Hulcott** | **14 Aug 1603** | **baptism** | **Joyce Gourney** | **John Gourney** | **Alice / "Alis"** | `6853-M8Z6`, `6859-6GKS` |
| Mursley | 6 Jun 1602 | burial | John | — | — | `685W-LQWC` |
| **Stewkley** | **21 Feb 1602/3** | **baptism** | **Jhon** | **Jhon Gurney** | **not indexed** | `JMRS-DX6` (Births & Christenings) |
| **Stewkley** | **25 Feb 1604** | **baptism** | **Simeon** | **John** | **not indexed** | `685S-357C` |
| **Stewkley** | **25 Feb 1604** | **burial** | **Simon** | — | — | `685W-TK9C` |
| Stewkley | 3 Mar 1604 | baptism | Penelope | Robarte | not indexed | `6853-9CZR` |
| Stewkley | 11 Apr 1609 | baptism | Richardus | Roberti | not indexed | `685S-TG7M` |
| **Stewkley** | **25 Sep 1609** | **baptism** | **Maria** | **Johannes** | **not indexed** | `685S-Y38L` |
| Stewkley | 1 May 1611 | baptism | John | Robert | not indexed | `685S-RFNN` |
| **Stewkley** | **13 Jan 1613** | **baptism** | **Damaris Girney** | **John Girney** | **not indexed** | `685S-Y86W` |
| Stewkley | 3 Apr 1614 | baptism | Elizabeth | Robert | not indexed | `685S-B336` |
| Stewkley | 10 Dec 1614 | burial | Elizabeth | — | — | `6854-9X7G` |
| Weston Turville | 6 May 1604 | baptism | John | Thomas | not indexed | `6853-MM23` |
| Weston Turville | 4 Feb 1625 | burial | John | — | — | `6854-3T7M` |
| **Weston Turville** | **2 Sep 1627** | **baptism** | **Elyzabethe** | **John** | **not indexed** | `685S-VNLF` |
| **Haddenham** | **25 Feb 1620** | **baptism** | (forename not indexed) | **John** | not indexed | `685S-HRHZ` |
| Haddenham | 2 Apr 1621 | burial | John | — | — | `685W-VC78` |
| **Haddenham** | **26 Jan 1622** | **baptism** | **Joane** | **John** | not indexed | `685S-Q7B1` |
| Wingrave | 20 Feb 1624 | baptism | John | Thomas | not indexed | `685S-RBZF` |
| Cheddington | 14 Dec 1634 | baptism | John Garney | Isaac Garney | Martha | `6859-BT4S` |
| Cheddington | 3 Mar 1636 | baptism | Jane | Isaac Gurney | Martha | (Bucks collection) |
| **Hitcham** | **22 Jan 1631** | **baptism** | **Mary** | **John** | **not indexed** | `685S-ZMZ3` |
| **East Claydon** | **15 Apr 1632** | **baptism** | **Elinor** | **John** | **Elizabeth** | `6853-MWCB` |
| East Claydon | 9 Jul 1635 | burial | Jana | — | — | `6854-M3GG` |
| **East Claydon** | **20 Feb 1636** | **baptism** | **Samuel** | **John** | **Elizabeth** | `6853-956F` |
| **East Claydon** | **17 Apr 1654** | **burial** | **John** | — | — | `6854-Q1T4` |
| Linslade | 31 Jul 1636 | baptism | Frances | Ezechiell | Alice | (Bucks collection) |
| Linslade | 21 Jun 1638 | burial | Ezekiel Girney | — | — | `685W-PXLB` |
| Aston Abbots | 11 Jan 1637 | baptism | John | Rob | Sarah | `6853-8N1G` |
| Waddesdon | Oct 1638 | baptism | Avis | William | Elizabeth | (Bucks collection) |
| Waddesdon | 11 Nov 1638 | burial | Elizabeth | — | — | `685W-RNMN` |
| Mursley | 16 Mar 1646 | baptism | William | Richard | Anne | (Bucks collection) |
| **Wing** | **1650** | **baptism** | **James** | **John** | **Ann** | `685S-78TK` |
| **Wing** | **1652** | **baptism** | **Elizabeth** | **John** | **Anne** | `6859-ZXPM` |
| **Wing** | **5 Apr 1655** | **baptism** | **Anne** | **John** | **Anne** | `6859-B4FY` |
| Wing | 1657 | burial | Anne | — | — | `685W-L7SP` |
| Wing | 1 Sep 1658 | burial | "Widw" Gurney | — | — | `685W-VBLS` |
| Wing | 29 Aug 1685 | burial | John | — | — | `685W-V4WG` |
| **Cublington** | **27 Jan 1664** | **baptism** | **Isaac** | **John** | **Mary** | `685S-5LL8` |
| **Cublington** | **22 Nov 1666** | **baptism** | **John** | **John** | **Mary** | `6859-Y254` |
| **Cublington** | **18 Mar 1668** | **baptism** | **Richard** | **John** | **Mary** | `6859-1QZW` |
| **Cublington** | **30 Dec 1669** | **burial** | **Mary** | — | — | `685W-Q322` |
| **Cublington** | **17 Feb 1672** | **baptism + burial** | **Elizabeth** | **John** | **Elizabeth** | `685S-RRVZ`, `6854-9R1D` |
| **Chesham** | **7 Nov 1678** | **baptism** | **Hester** | **John** | **Elizabeth** | `6859-9PXW` |
| Chesham | 11 Jun 1678 | burial | John | — | — | `685W-67S7` |
| **Chesham** | **29 Apr 1681** | **baptism** | **Elizabeth** | **John** | **Elizabeth** | `685M-B6XT` |
| **Chesham** | **2 Dec 1687** | **baptism** | **Joseph** | **John** | **Elizabeth** | `6859-QZZV` |
| Edlesborough | 4 Oct 1597 | baptism | John Gorney | Rychard Gorney | not indexed | `6859-K8ZV` |
| Edlesborough | 4 Jan 1598 | baptism | John Gorney | Rychard Gorney | not indexed | `6859-5MT8` |
| Northall | 1 Aug 1688 | baptism | Thomas | John | not indexed | `6859-594V` |
| Northall | 13 May 1688 | burial | John | — | — | `685W-Q3SZ` |
| Whitchurch | 26 Nov 1671 | baptism | John | John | Abigaile | `685S-S11W` |
| Whitchurch | 3 Jun 1677 | baptism | Daniel | John | Abigall | `685S-M3BM` |
| High Wycombe | 3 Aug 1671 | baptism | John | Luke | Jane | `685S-D4QY` |
| Monks Risborough | 13 Jun 1689 | burial | John | — | — | `6854-4JC4` |
| Wingrave | 15 Oct 1699 | burial | John | — | — | `685W-1L8T` |

### Saint Mary, Aylesbury — fathers only, no mothers in any available index

From *England, Births and Christenings, 1538–1975*. Note **Joseph, 22 March 1648, which the project
has not previously carried** — the household is six indexed children, not five.

| Date | Child | Father | Ark |
|---|---|---|---|
| 3 Dec 1585 | Allice | John | `J3F5-54M` |
| 31 Oct 1588 | Willyam | John | `NBWK-Z91` |
| 25 Oct 1594 | Robert | John | `J73P-FHW` |
| 16 Dec 1638 | John | John | `J3F5-P4Q` |
| 22 Aug 1639 | Sarah | John | `N5NK-W8H` |
| 26 Dec 1645 | Daniell | John | `JWN5-W5B` |
| 22 Nov 1647 | Jonathan | John | `JMBC-P2G` |
| **22 Mar 1648** | **Joseph** | **John** | `J3F5-TZF` |
| 27 Aug 1649 | Sarah | Thomas | `N5NK-W8Z` |
| 12 Nov 1653 | Hannah | John | `N5NK-ZFM` |

### Hertfordshire, 1570–1700

The collection holds 29 Gurney records in the window, at Bishop's Stortford, Datchworth, Hitchin,
Kimpton, North Mimms, Northchurch, Puttenham, Rickmansworth and Tring. The John Gurney content is:

| Date | Parish | Event | Detail | Ark |
|---|---|---|---|---|
| 28 Mar 1608 | Northchurch | baptism | John, son of Willm | `QL9P-V94N` |
| 4 Nov 1655 | Tring | marriage banns | John Gurney × Elizabeth Shepard | `QL95-RSBG` |
| 6 Apr 1686 | North Mimms | baptism | Willm, of John and **Mary** | `QL9T-427H` |
| 1 May 1690 | North Mimms | baptism | John, of John and Sarah | `QL9T-4279` |
| 29 Jan 1692 | North Mimms | baptism | Grace, of John and Sarah | `QL9T-WMHH` |
| 25 May 1696 | Rickmansworth | baptism | John, of John and Jane | `QL9T-CFDG` |

## (a) How many distinct John Gurney men do the mothers' names resolve?

**At least nine men active in Buckinghamshire between 1600 and 1670, and the wives' names do the
separating for five of them.** Four to six further Johns remain un-individuated because their
parishes carry no mother in any available index.

**Resolved by a named wife:**

1. **John Gurney × Elizabeth Lyne, East Claydon.** Married 30 October 1630. Children Elinor
   (15 April 1632) and Samuel (20 February 1636), both indexed with mother Elizabeth. Jana Gurney
   buried 9 July 1635. **He was buried at East Claydon 17 April 1654 and his will was proved that
   month — John Gurney, shepherd, of East Claydon (PROB 11/241/246, duplicate registration
   PROB 11/242/723).** Marriage, both children's mothers, burial and probate all agree. This is the
   only Buckinghamshire John Gurney in the emigration window who is individuated end to end by
   records that name him personally rather than by continuity of the name in a register.

2. **John Gurney × Alice Oliffe, Bierton with Broughton**, married 24 April 1628 — Candidate A's
   household. No child of that marriage is indexed at Bierton.

3. **John Gurney × Avis Carter, Amersham**, married 7 February 1638. **New to the project.** Carried
   in both the Buckinghamshire Marriage Index from the register (Bucks Archives PR4/1/1, register
   1561–1661) and independently in the bishop's transcript (D/A/T/4, 1600–1722), so the marriage is
   doubly attested. No baptism, burial, or probate for this man has been located.

4. **Johannes Gurney × Rebecka Coker, Ivinghoe**, married 22 October 1640. **New to the project as a
   marriage** — the deviation audit carried "Ivinghoe 1640" as an unassembled single event with no
   household behind it. It has a household: a wife, named. No baptism, burial, or probate follows.

5. **John Gurney × Mary, then × Elizabeth, Cublington.** Isaac (27 January 1664), John (22 November
   1666) and Richard (18 March 1668), all with mother Mary; **Mary Gurney buried at Cublington
   30 December 1669**; then Elizabeth, baptised and buried the same day, 17 February 1672, with
   mother Elizabeth. The remarriage is visible in the index and had not been separated before.

**Resolved by household but not by wife — the mother is not indexed in these parishes:**

6. **John Gurney of Stewkley** (active 1602–1613). Jhon 21 February 1602/3; Simeon 25 February 1604;
   Maria 25 September 1609; Damaris 13 January 1613. A second, contemporaneous Stewkley household
   under Robert Gurney produced Penelope (1604), Richardus (1609), **John (1 May 1611)** and
   Elizabeth (1614) — so Stewkley alone held two John Gurneys of the same generation, one born 1603
   and one born 1611.

7. **John Gurney of Haddenham.** A child baptised 25 February 1620 (forename not indexed) and Joane
   26 January 1622. A John Gurney was buried at Haddenham 2 April 1621, between the two baptisms, so
   Haddenham also held more than one John.

8. **John Gurney of Weston Turville.** Elyzabethe baptised 2 September 1627. A John Gurney buried
   there 4 February 1625.

9. **John Gurney of Hitcham.** Mary baptised 22 January 1631. A single event with nothing before or
   after it.

**Not resolvable from any index — the Saint Mary Aylesbury household.** Six children 1638–1653 with
a father John and no mother anywhere. Two Aylesbury John Gurney marriages fall in the same span
(Anne Cowheard, 25 October 1638; a further marriage in 1644), and a third in 1620. The parish
demonstrably held more than one John Gurney at once and the index cannot say which children belong
to which man.

Later Buckinghamshire Johns, individuated but outside the window: **John × Ann, Wing** (James 1650,
Elizabeth 1652, Anne 1655; Anne buried 1657, a Gurney widow buried 1658, John buried 1685);
**John × Elizabeth, Chesham** (Hester 1678, Elizabeth 1681, Joseph 1687, against a John Gurney
buried there 11 June 1678, so two Chesham Johns); **John × Mary Kidgell, Edlesborough**, married
25 January 1663; **John × Abigail, Whitchurch** (1671, 1677); **John × Susannah Smyth, Dinton**, 1691.

Two households the deviation audit listed as first surfaced on 26 July are confirmed and gain a
wife: **Hulcott — John Gourney and Alice**, daughter Joyce baptised 14 August 1603, with a Silvester
Gourney baptised there to a John in 1571. Hulcott had not previously been counted at all.

## (b) Is there a John Gurney + wife Mary household in Bucks/Herts before 1660?

**No. Not one, in either county, in any collection searched.** The negative now rests on an index
that does carry mothers, so it is a finding rather than a metadata artifact — which is the specific
weakness the deviation audit flagged.

The Buckinghamshire John-and-Mary households all begin after the colonial John's wife Mary was
already dead. **Cublington** John and Mary baptise from January 1664 and Mary is buried at
Cublington 30 December 1669 — the Braintree Mary was buried 20 September 1661, so the two women are
not the same and the two Johns are not the same man. **Edlesborough** John Gurney married Mary
Kidgell 25 January 1663 (Phillimore's printed register gives 1661; the register index gives 1663,
and either date is after Braintree). In **Hertfordshire**, the earliest John-and-Mary is North Mimms
in April 1686.

The nearest pre-1660 approach is **Hulcott, 1603 — John Gourney and Alice**, which is not Mary.

Caveat that bounds the negative: Saint Mary Aylesbury and Amersham carry no mother in any index for
this period, and Berkhamsted is absent from the Hertfordshire collection entirely. A John-and-Mary
household could sit inside any of those three and be invisible. That is exactly the residue Phase 2
is for.

## (c) Departure-shaped gaps, 1635–1641

The test — which household's records *stop* inside the emigration window with no burial and no
probate — has now been run. It had not been run before.

**Result: no Buckinghamshire John Gurney household stops between 1635 and 1641 in the shape the
colonial John would leave.** The candidates and why each fails:

- **East Claydon** is the only John Gurney household whose *children* stop inside the window
  (Samuel, February 1636, is the last). It fails the test decisively: the head was buried at East
  Claydon 17 April 1654 and his will was proved in the Prerogative Court of Canterbury that October.
  He died in England, individuated by name, occupation and parish.
- **Linslade** (Ezechiel Gurney, last child July 1636) and **Waddesdon** (William and Elizabeth, last
  child October 1638) both stop inside the window, but neither head is a John, and both are followed
  by a burial — Ezekiel Girney 21 June 1638, Elizabeth Gurney 11 November 1638.
- **Amersham (1638)** and **Ivinghoe (1640)** are the only two John Gurneys whose entire record
  trail begins inside the window and then goes silent — a marriage, then no baptism, no burial, no
  probate. In pure form this is the departure signature. **Two things cut against reading it that
  way.** First, coverage: Amersham's seventeenth-century register is not indexed in the collections
  searched beyond the marriage index, and the Ivinghoe register yields no Gurney baptism between
  1633 and 1686, so the silence may be the index rather than the man. Second, and more decisive,
  chronology: the Braintree John had married Mary by about 1627 and had three or four English-born
  children by 1635. A man marrying for the first time in Buckinghamshire in 1638 or 1640 cannot be
  him. What these two records actually do is add two more John Gurneys to an already dense county —
  they deepen the masking problem rather than solving it.

**The households that genuinely end with no burial and no probate for the head all stop well before
the window:** Stewkley (1613), Haddenham (1622), Weston Turville (1627), Hitcham (1631). Each of
those men is unaccounted for from that date, and each could in principle be anywhere after it,
including Massachusetts. But none of them shows the *shape* the test was designed to catch, because
none of them was still generating records in the 1630s to stop.

Probate was checked against the National Archives Discovery catalogue for the whole Prerogative
Court of Canterbury series, 1590–1700. The complete John Gurney set is: East Claydon 1654
(PROB 11/241/246, PROB 11/242/723), East Greenwich, Kent 1656 (PROB 11/252/319), Aylesbury 1671
(PROB 11/335/425, with sentence PROB 11/337/37 and inventory PROB 4/69), Winkfield, Berkshire 1683
(PROB 11/372/123), and a merchant, 1686 (PROB 11/382/271). **There is no Prerogative Court will for
any John Gurney of Stewkley, Amersham, Ivinghoe, Hitcham, Haddenham or Weston Turville.**

That negative is bounded at one tier only. The Archdeaconry of Buckingham probate series held at
Buckinghamshire Archives (D/A/We, D/A/Wf) is **not item-level indexed in Discovery**, and most
Buckinghamshire husbandmen and shepherds proved in the archdeaconry court, not in Canterbury. A
Buckinghamshire archdeaconry will search is the outstanding action, and it is a records-office
request rather than an online query.

## (d) The 1638 Cowheard marriage — not settled, and why

**The better collection does not settle it, because the better collection does not contain Saint
Mary Aylesbury for the seventeenth century at all.** Every Aylesbury Gurney record in *England,
Buckinghamshire, Church Records, 1217–1994* is nineteenth-century. The 1638–1653 baptisms survive
only in *England, Births and Christenings*, which indexes the father and nothing else. Neither the
Cowheard marriage nor the Oliffe marriage attaches to any of the six children through an index.

So the repo's statement in `research/people/g13-john-gurney/topics/identity/31-candidate-a-aylesbury.md`
— that the point "cannot be settled from these records alone" — stands. But its stated *reason* is
wrong and should be corrected: FamilySearch does index mothers for Buckinghamshire; it simply does
not cover this parish in the collection that does. The distinction matters because it changes the
remedy from "no index will ever help" to "this specific parish needs an image or a different source."

### Probate supersedes the image pull

Phase 1 turned up a cheaper and more decisive route than the register images, and it is untried.

**John Gurney, ironmonger of Aylesbury, will proved 20 March 1671 — PROB 11/335/425 — with a probate
sentence, PROB 11/337/37, dated 7 April 1671, and an inventory, PROB 4/69.** His son Daniell Gurney
of Aylesbury has his own Prerogative Court will, PROB 11/347/122, proved 3 February 1675, and a
Daniell Gurney was baptised at Saint Mary, Aylesbury on 26 December 1645 to a father John.

A *sentence* is the court's judgement in a contested grant. Contested grants in this period
routinely turn on exactly the question at issue here — rival claims by children of a first and a
second marriage. A will that names a widow and children, backed by a sentence that names the parties
to the dispute, would settle the Oliffe/Cowheard question from probate rather than from paleography,
and would do it at higher evidential quality than a mother's name in a baptism entry. **Pull
PROB 11/335/425 and PROB 11/337/37 before pulling any register image.**

## (e) The 1603 Stewkley John — no burial, no marriage, no probate

**Nothing anywhere. Searched and negative on every axis available online.**

- **No Gurney burial at Stewkley 1600–1700** other than Simon, 25 February 1604, and Elizabeth,
  10 December 1614. No John Gurney burial at Stewkley in any year in the collection.
- **No Stewkley Gurney record of any kind after 1614.** All ten Stewkley Gurney records in the entire
  collection, across its full 1217–1994 run, fall between 1604 and 1614.
- **No marriage** at Stewkley or in the Buckinghamshire marriage index naming a John Gurney of
  Stewkley.
- **No Prerogative Court of Canterbury will** for any John Gurney of Stewkley, 1590–1700.

**One premise of the deviation audit needs correcting.** The audit treated the sibling Simeon,
baptised 25 February 1604, as evidence of "a settled Stewkley household" and reasoned that this cut
both ways — more reason the 1603 boy stayed, and a documented family he could be lost inside.
**Simeon was buried at Stewkley on 25 February 1604, the day of his baptism.** He did not survive
infancy. The settled-household inference still holds, but on different children: Maria, baptised
25 September 1609, and Damaris, baptised 13 January 1613, both to a John. The "lost inside a
documented family" reading loses its strongest single prop, because the brother it rested on lived
less than a day.

The 1603 John therefore remains exactly where the audit left him: the closest age match in the
corpus to a man deposing "aged about 50" in 1653, eliminated only by being merged into the Oliffe
household, with that merge still undocumented. **This pass neither broke the merge nor supported
it.** It did establish that if the 1603 boy is a separate man, he left no trace in Buckinghamshire
after 1603 — no marriage, no children, no burial, no Canterbury probate — which is compatible with
early death, with migration inside England, and with emigration equally.

## Three Prerogative Court of Canterbury wills are misattributed in the repo

Checked item by item against the National Archives Discovery catalogue on 2026-07-26. Two of the
three corrections are Buckinghamshire wills currently filed under other counties, and both bear
directly on this individuation.

| Reference | Discovery catalogue title | As carried in `data/sources.json` |
|---|---|---|
| PROB 11/241/246 | Will of John Gurney, **Shepherd of East Claydon, Buckinghamshire**, 28 October 1654 | "John Gurney, shepherd, of East Chilton / East Chiltington, **Sussex**, mid-1650s" |
| PROB 11/242/723 | Will of John Gurney, **Shepherd of East Claydon, Buckinghamshire**, 28 October 1654 | as above (counted as a second Sussex man) |
| PROB 11/335/425 | Will of John Gurney, **Ironmonger of Aylesbury, Buckinghamshire**, 20 March 1671 | "John Gurney, husbandman, of **Albury, Hertfordshire**, 1676" |
| PROB 11/252/319 | Will of John Gurney, **Gentleman of East Greenwich, Kent**, 29 January 1656 | "John Gurney, yeoman of **East Grinstead**, 24 February 1654/5" |

The same misattributions propagate into the `tna-pcc-probate` registry note, which summarises the
corpus as "7 John Gurneys confirmed in England post-1637 (St Botolph Aldgate, Winkfield, Aylesbury,
East Grinstead, Albury, East Chiltington x2)" — a list in which three of the seven place-names are
wrong and two Buckinghamshire men have been dispersed into Sussex and Hertfordshire.

**The correction strengthens the Buckinghamshire eliminations rather than weakening them.** The East
Claydon will converts that household from a register-continuity elimination — the weak kind, which
dense same-name clusters defeat — into a probate elimination naming the individual, his trade and
his parish. The Aylesbury will and its sentence do the same for the Aylesbury household, and open
the route described in §(d).

These are registry and case-file corrections. **No edits have been made to `research/`, the case
file, or the fact sheets by this pass** — the deviation audit already establishes that those
surfaces need one coordinated patchset, and this finding belongs in it.

## Phase 2 — image targets, not yet pulled

**Nothing has been staged. `images/packet-57-bucks-john-gurney-individuation/` contains a README
stub only.** What follows is the brief for the pull, written so it can be executed without
re-deriving Phase 1.

### The question the images must answer

For each Saint Mary, Aylesbury baptism 1638–1653 with a father John Gurney, **what mother's name, if
any, does the register entry give?** If the register names mothers, the six children divide between
the Alice Oliffe household (married Bierton, April 1628) and the Anne Cowheard household (married
Saint Mary Aylesbury, 25 October 1638), or prove to belong to one man throughout. If the register
names no mother, that is itself the finding and it closes the question against the register for good.

Secondary: **does any Aylesbury entry 1638–1671 identify a John Gurney as ironmonger?** That would
tie the register household to PROB 11/335/425 and to the contested grant.

### Target images

| Priority | Source | Pages | Target or context |
|---|---|---|---|
| 1 | Saint Mary, Aylesbury parish register, baptisms | 1638 (Dec), 1639 (Aug), 1645 (Dec), 1647 (Nov), 1648 (Mar), 1653 (Nov) | **TARGET** — the six baptism entries |
| 2 | Same register, baptisms | 1636–1638 and 1653–1656 | CONTEXT — bracket the run; catch unindexed children |
| 3 | Same register, marriages | 1638 (Oct), 1644, 1620 | **TARGET** — the Cowheard entry and the two other Aylesbury John Gurney marriages |
| 4 | Same register, burials | 1638–1675 | **TARGET** — an Alice Gurney burial between 1628 and 1638 would settle the remarriage without any letterform argument; a John Gurney burial 1671 would tie the household to the will |
| 5 | Amersham parish register PR4/1/1 (1561–1661), and bishop's transcript D/A/T/4 | Feb 1638 marriage; baptisms 1638–1650; burials 1638–1660 | **TARGET** — the John Gurney × Avis Carter household is entirely unexamined |
| 6 | Ivinghoe parish register | Oct 1640 marriage; baptisms and burials 1640–1660 | **TARGET** — the Johannes Gurney × Rebecka Coker household, likewise unexamined |
| 7 | Stewkley parish register | 1600–1625, baptisms, marriages and burials | CONTEXT — the index holds nothing after 1614; determine whether that is the register or the index |

Cap the batch at 100 images. Include the index transcript text for each image as a **localisation aid
only** — the name at the point of interest must be read off the image, per
[`README.md`](README.md) and the durable method lessons in the deviation audit.

### Constraints carried forward from the deviation audit

- **Record the master coordinates of every crop.** A crop without an address stops being evidence.
- **Transcribe the whole line before adjudicating any token.**
- **Allow a null verdict.** "Neither reading" must be available, or the test manufactures its answer.
- Do not adjudicate paleography in this packet beyond confirming a page is the right parish and year.

## What this pass did not cover

Stated plainly so that partial coverage is not read as complete.

- **No images were captured and none are staged.** Phase 2 is entirely outstanding.
- **Buckinghamshire archdeaconry probate (D/A/We, D/A/Wf) was not searched.** It is not item-level
  indexed in the National Archives Discovery catalogue. Every "no probate" statement above is
  bounded to the Prerogative Court of Canterbury.
- **The Findmypast Buckinghamshire Marriage Index transcript for the Ivinghoe 1640 marriage is
  behind a subscription tier the account does not hold.** The couple was recovered from FamilySearch
  instead; the Findmypast archive reference for that entry is unread.
- **Findmypast results were read to 1644.** Its pagination returned register-browse rows beyond that
  point, so Findmypast-only later events — including the Aylesbury 1669 marriage the case file
  carries — were not re-read this pass. The Denham 1572, Aylesbury 1584/1620/1644 and Farnham Royal
  1629 John Gurney marriages are listed above from the results table but their spouses were not
  retrieved.
- **A John Gurney burial at Little Brickhill** appears in the Findmypast Buckinghamshire Burial Index
  with a covering range of 1600–1834 and no date. Not resolved.
- **Hertfordshire coverage is partial** — 546 of 1,437 Gurney records — and **Berkhamsted has no
  seventeenth-century Gurney record in the Hertfordshire collection at all**, so Candidate C's
  household was not reachable and its mothers were not recovered.
- **Chenies and Great Kimble return no Gurney record** in the Buckinghamshire collection. The
  "Great Kimble 1619" and "Chenies" events the deviation audit lists as unassembled singletons come
  from Findmypast sets and were not reached.
- **The FamilySearch search service caps unique results at roughly 1,500 per query**, and its date,
  place and spouse parameters rank rather than filter. The 4,334-record Buckinghamshire Gurney set
  was covered by relevance-ranked and per-parish sweeps, not exhaustively. A Gurney record in a
  parish outside the twenty queried, ranked below the cut, would have been missed.
