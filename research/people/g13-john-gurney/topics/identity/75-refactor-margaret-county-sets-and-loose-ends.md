<!-- July 2026 refactor working round. Its findings are carried in the permanent identity units
     30- to 39-, which are the current account; this file is retained as the working record,
     including its own correction and retraction trail, which is deliberate and belongs to the
     research layer. Not yet in the G13 context graph — graph-bearing content is tracked in
     sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# 75 — The Margaret axis, the county sets, and three loose ends closed

Final research round of the July 2026 refactor. Four things happened: a scoring rule I had asserted
was overturned and then tested properly; the county-set sweep (action R-66) completed and returned
empty; three undated households that had sat unworked since unit 68 were dated and eliminated; and a
John-and-Mary household turned up that falsifies a claim made two units ago.

## 1. Margaret is admitted to the mother axis, at reduced weight

Unit 74 asserted that "Margaret is not a variant of Mary … clerks did not swap them," and used that
assertion to set aside the Herefordshire John-and-Margaret household without searching it. **The
assertion was wrong, and the reasoning behind it was the same kind of reasoning the variant retraction
in unit 69 was supposed to have cured** — a confident claim about scribal behaviour with no
paleographic work behind it.

The mechanism that defeats it is specific and ordinary:

- In seventeenth-century hands **`g` and `y` are frequently written with almost identical looping
  descenders**, so the terminal letter that distinguishes *Marg* from *Mary* is precisely the letter
  most likely to be ambiguous.
- Clerks abbreviated heavily to save paper and ink. **Margaret is normally contracted to `Marg.` or
  `Mgt.`** in registers of this period, so the written token is usually four letters plus a mark of
  suspension, not the full name.
- A `Marg.` written with a looping `g` is therefore readable as **Mary** by a later clerk, a
  nineteenth-century transcriber, or a modern indexer — and the converse holds, a *Mary* being
  extended to *Margaret*. The corruption runs in both directions and it is introduced by the
  transcription chain, not by the original clerk.

This is the sliding-scale principle applied to a forename instead of a surname. The correct treatment
is the same: **not a binary in-or-out, but a weight.** Adopted rule:

| Mother token | Weight on attribute 6 | Basis |
|---|---|---|
| Mary, Marie, Marye, Maria, Marya, Mria | full | orthographic variants of one name |
| **Marg**, **Marg.**, **Mgt**, **Margaret**, **Margarett**, **Margret** | **substantial (soft hit)** | `g`/`y` descender ambiguity plus routine abbreviation; corruption runs both ways |
| Margery, Margerie | partial | shares the abbreviated stem `Marg.` but is a distinct name |
| Molly, Polly | excluded in this period | eighteenth-century hypocorisms; anachronistic before c.1700, so not a scoring option for a 1620s register |

The same logic was applied to the **father** axis, and had already been in force in the sweeps: the
John family is scored across `John`, `Jhon`, `Jon`, `Jno`, `Joh`, `Johis`, `Joh[ann]is`, `Johannes`,
`Johan`, `Johane`, `Johanne`, and — importantly — **`Jone` and `Joan`**, which in these indexes are
sometimes a Latin or contracted *Johannes* misread as the female *Joan* rather than a woman's name.
The county-set data contains a live instance: at Norwich St Giles in 1618 the father of Joseph Garnam
is indexed **`Jone`**, and in 1615 at King's Lynn the *father* of Gregorye Gurnall is indexed
**`Katheryne`** — an index that has put a mother's name in the father column.[^cnty] Neither field can
be trusted as a filter without allowing for this.

## 2. The Margaret axis then searched, with a passing control

Admitting Margaret changes nothing about the candidate set, but for a different and defensible reason:
**it was searched, and it is empty.**

**FreeREG, 585 rows re-cut.** Five households in the corpus have a mother in the Margaret family —
Norwich 1638 (father Will, mother Margret), Bardwell, Suffolk 1643 and 1645 (father Edward, mother
Margarett), and Mamble and Bayton, Worcestershire 1637 (father Thomas, mother Margery). **None has a
father in the John family.**[^freereg]

**The eight FindMyPast county baptism sets, 705 rows.** Seven rows carry a Margaret-family mother, to
fathers Robert, Edward, Michael and William, plus one with no father indexed. **None has a father in
the John family, at any date.**[^cnty]

**FindMyPast national cross-collection parent search.** Father John (variant-expanded) with mother
Margaret (variant-expanded) under the Gurney surname family, bounded 1610–1650, returns **eight rows,
not one of which is a genuine Gurney** — the surname column reads `?`, `Fosse`, `G...Ds` and `G?`,
these being fuzzy-match noise from Cornwall, Cheshire and Scotland.[^fmpnat]

The negative is interpretable because **the identical query shape with mother Mary returns the known
Eythorne, Kent household** — John 1638, Thomas 1635, plus the Gorney Edward 1641 and Gurnay John 1638
duplicate transcriptions.[^fmpnat] The instrument was working when it returned nothing for Margaret.

## 3. Three undated households dated, and all three eliminated

Unit 68 listed three FamilySearch households as unworked, one of them described there as "the single
most important loose end from this pass." All three were undated role rows. Dating them on a second
instrument — the FindMyPast county baptism sets, which carry an event year and both parent columns —
disposes of all three:

| Household (as unit 68 had it) | Now dated to | Verdict |
|---|---|---|
| **John Gurney and Mary, Sussex** — Elizabeth, Grace | **Grace, Horsham, 1704** (father John, mother Mary; indexed three times, as Gurne twice and Gurney once) | A century late. Eliminated |
| **John Gurney and Margaret, Herefordshire** — Mary | **Mary, Stoke Lacy, 1687** (father John, mother Margaret) | Sixty years late. Eliminated |
| **John Gurney, Warwickshire** — Ann, Anne | **Ann/Anne, Coleshill, 1710** (father John, mother not indexed) | A century late. Eliminated |

Sources: FindMyPast Sussex Baptisms, Herefordshire Baptisms and Warwickshire Baptisms respectively.[^cset]

Note what closed the Herefordshire household: **not the Margaret rule, which was wrong, but its
date.** Had the rule been allowed to stand, the household would have been dismissed for a bad reason
and would have had to be reopened later. It is eliminated on evidence instead.

**Method consequence.** All three undated FamilySearch role rows resolved to **1687, 1704 and 1710** —
every one of them late, none within a century of the window. That is a pattern, and it is now a
scoring rule: **an undated FamilySearch role row is not evidence of an in-window household. Date it on
a second instrument before it is allowed to carry any weight.** The role-row aggregation behaviour
already documented in the method file (role assignment varies with the forename queried, and a date
range does not bind on role rows) is what produces these; three for three late is the empirical
consequence.

## 4. A John-and-Mary household the earlier claim missed

Unit 73 and the case file stated that **across Britain 1620–1640 exactly one Gurney household has a
father John and a mother Mary** — Eythorne, Kent. **That is not correct as written.** The positive
control in §2 above returned Eythorne and also returned a second household:

**John and Mary Gurley, Westminster** — Eliz 1627, Ellynor 1628, Alexander 1629, **Mary 1631**,
Sara 1633. Five children in seven years, and **the recorded baptisms stop in 1633**.[^fmpnat] [^gurley]

Against the shape this is a genuine partial and a genuine failure at the same time:

- Attribute 5 (father John) and attribute 6 (mother Mary) are both satisfied outright.
- Attribute 2 is satisfied **on the primary bound rather than the traditional date** — Mary Gurley is
  baptised in 1631, and Mary Gurney's 1647 marriage to Daniel Shed requires only that she was born by
  1631. Hitcham's Mary of January 1630/1 sits in exactly the same position.
- The departure attribute is satisfied in form: the household's records stop in 1633, inside the
  1635–41 band's tolerance and before the migration.
- **It fails the boys completely.** There is no Richard and no John. The son is Alexander, and
  Alexander is not a name anywhere in the colonial family. Attributes 3 and 4 score zero, and
  attribute 1's ordering — Mary, then Richard, then John — cannot be built from this sibship at all.
- Surplus children: three (Eliz, Ellynor, Sara) beyond anything the colonial record wants, against a
  household of five.
- Attribute 0 is weak. **Gurley is a lower-plausibility variant than the Gurn-/Gourn-/Gorn- family**:
  it requires `n`→`l`, which is not one of the well-attested confusions, and unlike Gurnard it has no
  documented alias attaching it to a Gurney. The surname reached this result set only because
  FindMyPast's own variant expansion on the Gurney family reaches it.

Verdict: a documented household with the right parents, the right daughter, the right stopping date,
and the wrong sons under a doubtful surname. It enters the table at **2%** — small, but it is a real
household and it is more than several named candidates can show.

The corrected claim is: **exactly one household with the surname securely in the Gurney family has a
father John and a mother Mary in the window (Eythorne, and it is eliminated on other grounds); a
second (Gurley of Westminster) appears once the surname is expanded to the outer edge of the variant
scale.**

## 5. Epping: a line that alternates John and Richard

Attribute 10 predicts that John's own father was named Richard, inferred from his naming a son
Richard. Fully enumerated, Epping's Gurn- corpus does something suggestive.[^epping]

Every row in the Essex Baptisms set is double-indexed — once as *Epping, All Saints* and once as
*Epping Upland, All Saints* — so the twenty-eight results are fourteen distinct events. The
seventeenth-century sequence:

| Year | Child | Father | Mother |
|---|---|---|---|
| 1616 | **Richard** Gurnat | **John** | — |
| 1622 | John Gurne | Robert | Sara |
| 1649 | **Richard** Gurnet | **Richard** | — |
| 1654 | John Gurnet | John | — |
| 1659 | Elisabeth Gurnet | John | Anne |

**The line alternates John and Richard across three generations** — a John naming a Richard in 1616, a
Richard naming a Richard in 1649, a John naming a John in 1654. That is precisely the naming behaviour
attribute 10 is built on, in the county with the strongest Great Migration weight and the county of
Braintree's own name.

What it does not contain is a **John baptised c.1603**. The set's earliest Epping Gurn- row is 1616.
Whether that is absence or absent coverage **cannot be settled on this instrument**, for the reason in
§7 below. Epping enters the table at **3%** on attributes 10, 11 and 12, with attributes 1 through 6
untested rather than failed — and R-58, the Essex Record Office register itself, becomes the action
that would resolve it.

## 6. What R-66 measured, and what it returned

R-66 existed to measure one row of the probability table: *documented, but in a source or class not yet
searched.* The test was direct — **every household the county sets return that the national
cross-collection pool did not is a measurement of that row.**

Executed: **eight county sets, 705 captured rows** across Norfolk, Essex, Northamptonshire,
Oxfordshire, Cambridgeshire, Middlesex, Westminster and Berkshire, each run against six surname stems
(`gurn*`, `gourn*`, `gorn*`, `gern*`, `girn*`, `garn*`) for baptisms and, where the set exists, for
marriages and banns.[^cnty]

Of those rows, **68 fall in 1615–1650 and carry a father's name** — the in-window household pool this
sweep was built to produce. Within it:

- **No father-John, mother-Margaret household. None, at any date, in any of the eight sets.**
- **No father-John, mother-Mary household in the window** that the national pool had not already seen.
- The father-John rows in window are the ones already catalogued: Earsham (1636, 1638), Epping (1616),
  Harwich (1623, mother Elizabeth), Thursford (1623), Hingham (1626), Abthorpe (1641), St Lawrence
  Jewry (1620), Oakington (1648, mother Anne), Kidlington and Banbury.

**The row falls.** It does not fall to zero, because the sweep also mapped the boundary of what the
instrument can reach, and that boundary is real:

- **No FindMyPast marriage set exists for Essex, Middlesex or Huntingdonshire** — three slugs each
  probed under several spellings, all returning server errors. Huntingdonshire has no baptism set
  either.
- **Berkshire marriages were never run** (the sweep ran out of budget at that row).
- **Suffolk** has no county baptism set in this family, and Suffolk is where FreeREG's Bardwell
  Margaret household sits — an adjacent Great Migration county reachable on one instrument only.
- Nine of the queries were **capped at the first result page** by high-noise stems (`garn*` alone
  returns 2,913 rows in Norfolk), so those are samples, not enumerations.

Residual coverage risk therefore concentrates in **marriages for three populous counties, Suffolk
baptisms, and the capped high-noise stems** — a specific, listable remainder rather than an open-ended
hope. The row moves from 9% to **5%**.

## 7. Two instrument defects, one of them retroactive

**`yearofbaptism` and `keywords` cannot be combined in a single-dataset (`sid=103`) query. The
combination fails closed.** Proven: Essex Baptisms holds Richard Gurnat at Epping in 1616, confirmed by
a query with `keywords=epping` and no year. The same set, `lastname=smith&keywords=epping`, returns
**349 results** with no year bound — and **zero** with `yearofbaptism=1616&yearofbaptism_offset=5`.
A parish with 349 Smith baptisms cannot have none in a six-year window that the same set demonstrably
covers for another surname.[^defect]

This is retroactive. **Any negative in this project's record that rests on a `sid=103` query carrying
both a year bound and a place keyword is void** and must be re-run without the year. The defect joins
the three already documented — `keywords` failing closed on a wrong place token, place tokens differing
between sets of the same county, and `yearofbaptism` broken outright in the Worcestershire, Somerset
and Dorset sets.

**`sortby=dateasc` is not honoured.** The parameter is accepted and ignored; results stay in the
default order. Any attempt to establish a set's earliest coverage year by sorting is invalid, which is
why the Epping and Ackworth coverage questions below stay open.

**Consequence for Ackworth.** Ackworth is the second-ranked named candidate at 9%, and it **cannot be
tested on FindMyPast's Yorkshire Baptisms set.** `lastname=gurn*&keywords=ackworth` returns zero; the
control, `lastname=smith&keywords=ackworth`, returns **127 results, of which none on the visible page
falls earlier than 1689**.[^ackworth] With the year parameter unusable and `sortby` ignored, the set's
Ackworth coverage in the 1630s is unproven, and **the Gurney zero is uninterpretable — it is not
evidence that the Ackworth household had no children.** The candidate is neither strengthened nor
weakened by this pass; it is simply out of reach of this instrument, and R-64 (the parish register at
West Yorkshire Archive Service) remains the only way to settle it. Ackworth holds at 9%.

## 8. Transcription noise on the mother axis, observed directly

The county sets contain a clean demonstration of why the mother field must be scored as a scale rather
than a filter. **Tittleshall with Godwick, Norfolk, 1620** returns the same child twice — Katerine
Gurnay and Katherine Gurnay, father Henry in both — with the mother indexed **`Anne` in one transcript
and `Mary` in the other**.[^cnty] One event, one clerk's original, two indexed mothers with different
names.

Nothing about the Tittleshall household bears on the emigrant (the father is Henry). Its value is
methodological: it is a worked example, inside this corpus, of the mother forename being unstable
between witnesses to the same record. Any negative that turns on a single index's reading of a mother's
name is weaker than it looks — which is the general case that the Margaret argument in §1 is a
particular instance of.

## 9. What moved

| Change | From | To | Driver |
|---|---|---|---|
| Documented, in a source not yet searched | 9% | **5%** | R-66 executed across 8 county sets; empty, with a listable residual |
| No record survives or is indexed anywhere | 21% | **22%** | the mass leaving the coverage row has to go somewhere |
| Unnamed Bucks/Herts/Beds household | 5% | **3%** | those three counties now repeatedly swept and empty |
| **Gurley of Westminster** | — | **2%** (new) | documented John × Mary, Mary 1631, records stop 1633; no Richard, no John |
| **Epping/North Weald Gurnat–Gurnet line** | — | **3%** (new) | John→Richard 1616 alternation; Essex; coverage negative void |
| Ackworth | 9% | **9%** (held) | untestable on the available instrument, not weakened |

The case-file table now carries **18 rows summing to 100**. "Other named and out-of-corridor
candidates" is deliberately held at 1% rather than retired: the two new rows are specific households,
and naming two does not exhaust the unenumerated remainder.

Unchanged and still the largest single row: **documented and assembled but not recognised, 17%.**

Three eliminations were also recorded (Sussex 1704, Herefordshire 1687, Warwickshire 1710); they
removed nothing from the table because all three had been carried as unworked loose ends rather than
as probability mass.

## 10. Open after this round

R-58 (Epping and North Weald registers, Essex Record Office) is now the highest-value single action,
because §5 gives it a specific prediction to test and §7 shows the index cannot settle it. R-64
(Ackworth register) is second for the same reason. The full list, with the new items added this round,
is in unit 59.

[^freereg]: FreeREG (Free UK Genealogy), sweep of 28 July 2026, 585 captured rows across the Gurney
surname family; working dataset at `sources/intake/archive/g13-july-2026-sweeps/freereg-g13-sweep-2026-07-28/results.tsv` with
per-query coverage in the accompanying `PROGRESS.md`. Margaret-family mothers re-cut 29 July 2026:
Norwich 12 August 1638 (Ellin, father Will, mother Margret); Bardwell, Suffolk 18 June 1643 and 18 May
1645 (Robert, father Edward, mother Margarett); Mamble and Bayton, Worcestershire 17 September 1637
(John Gurner, father Thomas, mother Margery). Source ID: `freebmd-freereg`.

[^cnty]: Findmypast, authenticated session, county baptism and marriage index sets, sweep of 29 July
2026; 705 captured rows across Norfolk, Essex, Northamptonshire, Oxfordshire, Cambridgeshire,
Middlesex, Westminster and Berkshire, each against stems `gurn*`, `gourn*`, `gorn*`, `gern*`, `girn*`,
`garn*`. Working dataset and per-query coverage ledger at
`sources/intake/archive/g13-july-2026-sweeps/fmp-county-sweep-2026-07-29/results.tsv` and `PROGRESS.md`. Tittleshall with
Godwick duplicate: Norfolk Baptisms Index, 1620, Katerine/Katherine Gurnay, father Henry, mother
indexed Anne in one row and Mary in the other. Norwich St Giles 1618, Joseph Garnam, father indexed
`Jone`; King's Lynn St Margaret with St Nicholas 1615, Gregorye Gurnall, father indexed `Katheryne`.
Source IDs: `findmypast-county-baptism-sets-2026-07-sweep`; `findmypast-norfolk-baptisms-index`;
`findmypast-norfolk-banns-marriages-index`.

[^fmpnat]: Findmypast, authenticated session, 29 July 2026. Cross-collection parent search
(`sid=102`, Great Britain, parish baptisms), father forename John and surname Gurney both
variant-expanded, bounded `yearofbirth=1630&yearofbirth_offset=20`. With `motherfirstname=margaret`
variant-expanded: 8 results, surnames `?`, `Fosse`, `G...Ds`, `G?`, from Cornwall, Cheshire and
Scotland — no Gurney-family surname among them. With `motherfirstname=mary` variant-expanded: 16
results including Eythorne, Kent (John 1638, Thomas 1635, and the duplicate transcriptions Gorney
Edward 1641, Gurnay John 1638, Gurner Thomas 1635) and the Westminster Gurley household. The Mary
query is the positive control for the Margaret query: same shape, same bounds, known household
returned. Source ID: `findmypast-uk-parish-baptisms`.

[^gurley]: Findmypast, authenticated session, 29 July 2026, cross-collection parent search with
`fatherfirstname=john&fatherlastname=gurley` unexpanded, bounded 1613–1653: six results, of which five
are the Westminster household (Eliz 1627, Ellynor 1628, Alexander 1629, Mary 1631, Sara 1633, all to
father John and mother Mary, in *England Births and Baptisms 1538–1975*) and the sixth is an unrelated
John Gurley at Berwick-upon-Tweed, Northumberland, 1625. No Gurley baptism to this father is recorded
after 1633. Source ID: `findmypast-uk-parish-baptisms`.

[^cset]: Findmypast, authenticated session, 29 July 2026, single-dataset queries (`sid=103`).
*Sussex Baptisms*, `lastname=gurn*&firstname=grace`: 3 results, all Grace, Horsham 1704, father John,
mother Mary (indexed twice as Gurne, once as Gurney). *Herefordshire Baptisms*,
`lastname=gurn*&firstname=mar*`: 57 results, among them Mary Gurney, Stoke Lacy 1687, father John,
mother Margaret. *Warwickshire Baptisms*, `lastname=gurn*&firstname=ann*`: 16 results, among them
Ann and Anne Gurney, Coleshill 1710, father John, mother not indexed. Each dates a household that
unit 68 carried as an undated FamilySearch role row. Source ID:
`findmypast-county-baptism-sets-2026-07-sweep`.

[^epping]: Findmypast, authenticated session, 29 July 2026. *Essex Baptisms*,
`lastname=gurn*&keywords=epping`, no year bound: 28 results, every event double-indexed as both
*Epping, All Saints* and *Epping Upland, All Saints*, giving 14 distinct events. Seventeenth-century
entries: Richard Gurnat 1616 (father John); John Gurne 1622 (father Robert, mother Sara); Richard
Gurnet 1649 (father Richard); John Gurnet 1654 (father John); Elisabeth/Elizabeth Gurnet 1659 (father
John, mother Anne). Later entries to a father John run 1691–1726. No Gurn- baptism earlier than 1616
appears in the set for either parish. Source ID:
`findmypast-county-baptism-sets-2026-07-sweep`.

[^defect]: Findmypast, authenticated session, 29 July 2026. *Essex Baptisms* (`sid=103`):
`lastname=smith&keywords=epping` with no year bound returns 349 results;
`lastname=smith&keywords=epping&yearofbaptism=1616&yearofbaptism_offset=5` returns 0, and
`yearofbaptism=1600&yearofbaptism_offset=5` returns 0, in a set that demonstrably holds a 1616 Epping
baptism under another surname. `sortby=dateasc` on the unbounded Smith query leaves the result order
unchanged (first rows returned 1835–1894), so the parameter is accepted and ignored. Recorded as a
reusable instrument defect in `.claude/skills/findmypast-record-search/SKILL.md`. Source ID:
`findmypast-county-baptism-sets-2026-07-sweep`.

[^ackworth]: Findmypast, authenticated session, 29 July 2026. *Yorkshire Baptisms* (`sid=103`):
`lastname=gurn*&keywords=ackworth` returns 0; the control `lastname=smith&keywords=ackworth` returns
127 results, of which the twenty on the visible page span 1689–1814 with none earlier. Because
`yearofbaptism` cannot be combined with `keywords` in this query mode and `sortby` is ignored, the
set's Ackworth coverage before 1689 is unproven and the Gurney zero is uninterpretable. The Ackworth
1637 baptism and 1636 marriage themselves are registered separately. Source IDs:
`findmypast-county-baptism-sets-2026-07-sweep`;
`findmypast-ackworth-gurnoe-baptism-1637-john-thomas`;
`findmypast-ackworth-gurnoe-burton-marriage-1636`.
