<!-- July 2026 refactor working round. Its findings are carried in the permanent identity units
     30- to 39-, which are the current account; this file is retained as the working record,
     including its own correction and retraction trail, which is deliberate and belongs to the
     research layer. Not yet in the G13 context graph — graph-bearing content is tracked in
     sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# Four instruments, compared — and why the child sweep undercounted

## The finding in one line

**The big four indexes are an overlapping Venn diagram, not four views of one dataset** — and the July
2026 per-child sweep undercounted on its own instrument before provider coverage was even reached,
because it constrained the surname stem, the child's forename, and the place token, each of which
fails closed.

## The coverage matrix

Every cell below was tested directly this pass, not inferred. ✓ = the instrument returns the record;
✗ = it does not.

| Control record | FindMyPast | FamilySearch | Ancestry 9841 | FreeREG |
|---|:--:|:--:|:--:|:--:|
| **Mary Gurny, Hitcham, Bucks, 1631** (father John) | ✓ | ✓ | **✗** | **✗** |
| **Richard, Great Berkhampstead, 1626** (father John) | ✓ | ✓ | **✗** | **✗** |
| **John, Aylesbury St Mary, 1638** (father John) | ✓ | ✓ | **✗** | **✗** |
| **Marie Gurney, Epping, Essex, 1625** (father Robert) | ✓ | — | — | ✓ |
| **Mary Gourny, St Vedast, London, 1624** (father Richard) | ✓ | — | — | ✓ |
| **Mary Gurney, Upton on Severn, 1629** (mother Mary, no father) | ✓ | — | ✓ | — |
| **Richard Gurney, Stewkley, 1626** (father Robert) | ✓ | — | **✗** | ✓ |

**No instrument is complete, and the gaps do not coincide.** Ancestry's IGI-derived set is missing all
three of the father-John controls that FindMyPast and FamilySearch both hold. FreeREG is missing the
same three but holds Stewkley, which Ancestry does not. Any negative asserted from one of these is a
statement about that index, and the file has been treating such statements as statements about
England.

## The three ways the July sweep failed closed

This is the more important half, because it is a defect in query construction rather than in the
sources, and it is repairable.

1. **Surname stem.** `lastname=gurn*` does not reach `Gourny`, `Gourney`, `Gorne`, `Garne`, `Gernne`
   or `Gowrne`. This alone hid the St Vedast household — and, in unit 66, the entire Berkhamsted
   burial series.
2. **Child's forename.** The sweep constrained the forename to the exact string **`Mary`**. Registers
   of this period give **Marie, Marye, Maria, Marya** — forms already present in this project's own
   catalogue as *Marie Gurney* (Ashwellthorpe), *Marye Garne* (Compton Abdale) and *Maria Gorne*
   (Bishop's Cleeve). Re-run on the identical instrument and window with `firstname=mar*`, the count
   goes from **17 to 54**.[^marwild] Epping 1625, indexed *Marie*, was invisible for this reason alone.
3. **Place token.** Established in unit 66: a keyword place filter is a literal match against the
   target set's own spelling, and the same provider spells one parish differently between its baptism
   and burial sets.

**Consequence for the recorded totals.** The July figures — Mary 17, Richard 9, John 27, **Peter 0,
Isaac 0** — are floors on their own instrument. The Peter and Isaac zeros were run as exact forenames
and are the weakest of the set: *Peeter*, *Petter*, *Isaack*, *Isacke* and *Izacke* are all ordinary
period spellings. **Those two zeros currently carry an argument in the case file about which children
were English-born, and they should not carry it until they are re-run wildcarded.**

## What the pass actually recovered

### Fathers read for the first time on three catalogue rows

Three rows sat in the catalogue with `father not yet read`. All three are now read, and none is a John:

- **CR-053, Mary Gurney, Linslade, Bucks, 1633 — father Ezechiell**, from FamilySearch's
  *Buckinghamshire Church Records*.[^fs] This ties the row to the Ezechiell-and-Alice Linslade
  household already surfaced in July, rather than leaving it an unattached Mary in the target county.
- **CR-054, Mary Gurney, Kelham, Notts, 1630 — father William**, confirmed independently by
  FamilySearch and Ancestry.[^fs] [^anc]
- **CR-055, Mary Gurnard, Bishop's Stortford, Herts, 1629 — father Henry, mother Mary**, from
  Ancestry.[^anc]

Removing three unattached Marys from the open list is a real narrowing of the child inventory: the
count of Mary baptisms in window whose father is unknown, and therefore might be a John, drops to zero
among the catalogued rows.

### Households the file did not have

| Household | Evidence | Bearing |
|---|---|---|
| **Richard Gourny, St Vedast Foster-Lane, London** — Mary 1624, **Anne 1626** | FreeREG + FindMyPast Middlesex Baptisms | A Richard Gurney household in a City parish in the emigrant's generation. Enters the Richard-household comparator set behind the §6.3a naming prediction |
| **Robert Gurney and Sarra, Epping, Essex** — Marie 1625/6 | FreeREG (parents named) + FindMyPast Essex Baptisms | Essex, the colonial network's own county. Closed on a named father |
| **Henery Gurney and Mary, Middlesex** — Mary 1634 | FamilySearch | A Gurney household with a **wife Mary** in the window; probably the London Henry Gurney already in §8.8 |
| **Edward Gurnel/Gurnet and Winefret, Allhallows London Wall** — Mary 1627, Richard 1628 | Ancestry | Gurnel/Gurnet, likely a distinct surname; two colonial-name children to a non-John father |
| **Thomas Gurney and Elizabeth, St Martin in the Fields** — John 1633 | Ancestry | New London household |
| **William Gurner and Marlin, Buckland near Dover, Kent** — John 1636 | Ancestry | New Kent household |
| **John Gurney and Mary, Sussex** — Elizabeth, Grace | FamilySearch role rows, **undated** | A John-and-Mary household in a county the file has only touched through two probates. **Undated and unworked — the single most important loose end from this pass** |
| **John Gurney and Margaret, Herefordshire** — Mary | FamilySearch role rows, undated | Unworked |
| **John Gurney, Warwickshire** — Ann, Anne | FamilySearch role rows, undated | Unworked |

### Provider disagreements on the same event

Two, both worth carrying because the method treats index disagreement as evidence:

- **Kelham 1630**: Ancestry gives **11 October**, FamilySearch gives **27 October**.[^anc] [^fs]
- **Upton on Severn 1629**: Ancestry gives **13 September**; the March 2026 matrix gives **7
  September**.[^anc]

## Bedfordshire, swept as a county at last

Bedfordshire sits between the Aylesbury Vale cluster and Toddington and has been flagged since July as
materially unworked — reached only through three parishes that a Gurney happened to be indexed in.
Swept properly, the county baptism set holds **127 Gurney-variant baptisms for 1610–1650**.[^beds]

Filtered to the colonial child names, and deduplicated across the paired index rows, it returns
**seven events and not one has a father John**:

| Child | Year | Parish | Father | Mother |
|---|---|---|---|---|
| Mary Gurnie | 1617 | Toddington | Richard | — |
| Margaret Gurnie | 1626 | Clapham | Robert | — |
| Richard Gurney | 1635 | Luton, St Mary | Richard | Joyce |
| Mary Gurney | 1638 | Luton, St Mary | Richard | **Joan** in one index row, **Joyce** in the other |
| Mary Gurney | 1640 | Toddington | Thomas | — |
| Richard Gurnney | 1636 | Toddington | Thomas | — |
| Mary Gurney | 1640 | Wootton | Daniel | — |

The county's father-John presence is the **Toddington household of John Gurney and Elizabeth Moreton**
— Ann 1628, Audrey 1634 — already eliminated, its head buried at Toddington in 1641. Households new
to the file, none of them father-John: Alexander Gurney at **Woburn** (1622), Edward and Sibell at
**Luton** (1636), Henry and Elizabeth at **Luton** (1642), Robert at **Clapham**, Edward at
**Houghton Regis** (1612), Philip Garner/Gurner at **Potton** (1615).

**Bedfordshire is now swept and it produces no candidate.** The Wootton 1640 Mary confirms, on a
second instrument, the row FreeREG supplied the same day.

**One stale catalogue row exposed.** CR-020 recorded "John Gernne, 13 February 1631, Toddington,
father **John**". The Bedfordshire county set indexes the same event as "John Gernne Or Gurney, 1630,
Toddington, father **Thomas**", agreeing with unit 62's own July reading that Toddington 1630 resolves
to Thomas. The catalogue row was stale against the file's own later work and is corrected.

## A usable technique found by accident

FamilySearch's results are **role-aggregated** — a row can be the person as *Principal* or as *Father*
— and which you get depends on the forename, because a common father-name floods the parent rows. A
`Richard` query with a date range returns almost nothing but "Richard Gurney · Father · Spouses Joyce ·
Children John Gurney" rows, which is why it appeared to return zero baptisms.

Read the other way, **those parent rows are a household index**. A query on `q.givenName=John` +
`q.surname=Gurney` returns 87 father-rows in the first hundred, each naming a spouse and a child —
**eighteen of them with a wife named Mary**.[^fsroles] That is the FamilySearch analogue of
FindMyPast's `sid=102` parent search, and it had never been used.

Its limitation is severe and must be recorded: **the date range does not bind on role rows at all.**
Two of the John-and-Mary rows carrying a daughter Mary resolve, when opened, to christenings of **1687
at Misterton, Leicestershire** and **1703 at Upton on Severn** — both far outside the requested
1620–1645 window.[^fsdates] So the technique enumerates households but cannot date them; each row has
to be opened. The Sussex, Herefordshire and Warwickshire households above are unresolved for exactly
this reason.

## Consequences

1. **Restate every per-child total as a floor**, and say why: three query constraints plus four
   partial indexes.
2. **Re-run Peter and Isaac wildcarded before either zero is used again.** The claim that Peter and
   Isaac were American-born currently rests on exact-forename zeros on one provider.
3. **Work the Sussex John-and-Mary household.** It is the only new John-and-Mary household this pass
   produced, and it is undated only because of a FamilySearch interface limitation.
4. **No probability row moves.** Nothing found promotes or demotes a candidate. What changes is the
   weight the file may place on its negatives, which should fall again.

## Crosslinks

- [`67-refactor-freereg-second-instrument.md`](67-refactor-freereg-second-instrument.md) — the FreeREG arm and the correction that led here
- [`66-refactor-berkhamsted-burials-and-the-departure-gap.md`](66-refactor-berkhamsted-burials-and-the-departure-gap.md) — the place-token and surname-stem defects
- [`62-refactor-the-per-child-sweep.md`](62-refactor-the-per-child-sweep.md) · [`63-refactor-child-sweep-closed-and-reassessment.md`](63-refactor-child-sweep-closed-and-reassessment.md) — the sweep this qualifies
- [`65-refactor-child-inventory-method.md`](65-refactor-child-inventory-method.md) — the method
- Catalogue: `research/people/g13-john-gurney/coverage/child-record-catalog.csv`

[^beds]: FindMyPast *Bedfordshire Baptisms*, authenticated session, 28 July 2026: `datasetname=bedfordshire+baptisms&sid=103&lastname=gurn*&yearofbaptism=1630&yearofbaptism_offset=20` → **127 results** for 1610–1650, read with the Father's first name(s), Mother's first name(s) and Place columns; each event is indexed twice, once under the short place name and once under the church. Forename-filtered runs `firstname=mar*` (10 rows) and `firstname=ric*` (4 rows) over the same window supply the colonial-name table above. Source ID: `findmypast-bedfordshire-baptisms`.
[^marwild]: FindMyPast cross-collection search, authenticated session, 28 July 2026: `sid=999&collection=parish+baptisms&sourcecountry=great+britain&firstname=mar*&lastname=gurn*&yearofbirth=1629&yearofbirth_offset=10` → **54 results** for 1619–1639, against the 17 recorded in July 2026 for the exact forename *Mary*. The wildcard also admits Margaret and Mark rows, so 54 is not a corrected Mary count; it demonstrates that the exact-forename constraint was excluding genuine Marie/Marye/Maria rows, of which Epping 1625 is one. Source ID: `findmypast-uk-parish-baptisms`.
[^fs]: FamilySearch historical-record search, authenticated session, 28 July 2026: `q.surname=Gurney&q.givenName=Mary&q.birthLikeDate.from=1622&q.birthLikeDate.to=1636&f.recordCountry=England&count=100`, in-window Principal baptism rows read from the results table — "Mary Gurney, England, Buckinghamshire, Church Records 1217-1994, Baptism 19 May 1633, Linslade, Buckinghamshire, Parents Ezechiell Gurney"; "Mary Gurney, England, Nottinghamshire, Church Records 1578-1937, Baptism 27 October 1630, Kelham, Nottinghamshire, Parents William Gurney"; "Mary Gurney, England, Middlesex, Parish Registers 1539-1988, Baptism 5 September 1634, Middlesex, Parents Mary Gurney, Henery Gurney"; and the control "Mary Gurny, England, Buckinghamshire, Church Records 1217-1994, Baptism 22 January 1631, Hitcham, Buckinghamshire, Parents John Gurny". Source IDs: `fs-england-buckinghamshire-church-records-1217-1994`; `fs-england-births-christenings`.
[^anc]: Ancestry, *England, Select Births and Christenings, 1538-1975*, collection 9841, authenticated session, 28 July 2026, collection-scoped searches `name=Mary_Gurn*&birth=1630`, `name=Richard_Gurn*&birth=1631` and `name=John_Gurn*&birth=1634`, rows read from the Baptism Date / Baptism Place / Relatives columns. In-window Mary rows: Marye Gurney, 11 Oct 1630, Kelham, Nottingham, relative William; Mary Gurnard, 12 Apr 1629, Saint Michael's Bishops-Stortford, Hertford, relatives Henry and Mary; Marye Gurney, 13 Sep 1629, Upton on Severn, Worcester, relative Mary only; Mary Gurnel, 21 Jan 1627, Allhallows London Wall, relatives Edward and Winefret; Mary Gurner/Gurnte, 28 Nov 1633, Eythorne, Kent, relative John. In-window Richard rows: one only — Richard Gurnet, 1 Jun 1628, Allhallows London Wall, relatives Edward and Winefret. In-window John rows: John Gurney, 14 Dec 1634, Cheddington, Buckingham, relatives Isaac and Martha; John Gurney, 17 Nov 1633, St Martin in the Fields, Westminster, relatives Thomas and Elizabeth; John Gurnell, 27 Jan 1633, St Botolph Bishopsgate, relatives James and Elizabeth; John Gurner, 22 Jan 1636, Buckland near Dover, Kent, relatives William and Marlin; John Thomas Gurnoe, 19 Jan 1637, Ackworth, York. Neither Hitcham 1631, Great Berkhampstead 1626, Stewkley 1626 nor Aylesbury St Mary 1638 appears in any of the three runs. Source ID: `ancestry-england-select-births-christenings-9841`.
[^fsroles]: Same FamilySearch session: `q.surname=Gurney&q.givenName=John&q.birthLikeDate.from=1620&q.birthLikeDate.to=1645&f.recordCountry=England&count=100` → 494 results, of which 87 of the first hundred blocks are rows where John Gurney appears in the **Father** role, carrying a spouse and a child but no event date; 18 of those name a spouse **Mary**, resolving to 14 distinct household strings. A parallel run with `q.fatherGivenName=John&q.motherGivenName=Mary` and the same date range returns four in-window Principal baptisms, all already in the catalogue: Eythorne 1638, Weston Turville 1627, Haddenham 1622 and the Hitcham 1631 control. Source ID: `fs-england-births-christenings`.
[^fsdates]: FamilySearch record pages `ark:/61903/1:1:J9M5-W5Q` (Mary Gurney, christening 30 April 1687, Misterton, Leicestershire, father John, mother Mary) and `ark:/61903/1:1:NBC3-DRV` (Mary Gurney, christening 30 April 1703, Upton on Severn, Worcestershire, father John, mother Mary), both returned inside a search bounded to 1620–1645. Source ID: `fs-england-births-christenings`.
