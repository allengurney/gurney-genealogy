<!-- July 2026 refactor working round. Its findings are carried in the permanent identity units
     30- to 39-, which are the current account; this file is retained as the working record,
     including its own correction and retraction trail, which is deliberate and belongs to the
     research layer. Not yet in the G13 context graph — graph-bearing content is tracked in
     sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# The second instrument: what FreeREG holds that FindMyPast does not

## Why this matters more than the rows it produced

> **CORRECTION, made within this same pass — read before the tables below.** This unit originally said
> FreeREG had returned two Mary Gurney baptisms that **FindMyPast does not hold**. That is **false**,
> and I caught it only by going back to verify a load-bearing claim rather than letting it stand.
> FindMyPast holds both — Marie Gurney at Epping, Essex 1625 appears in *England Births & Baptisms*
> **and** in *Essex Baptisms*, three index rows; Mary Gourny at St Vedast Foster-Lane 1624 appears in
> *Middlesex Baptisms*, alongside a sibling **Anne Gourney, 1626**, which nobody had.[^fmpholds]
>
> **The corrected finding is sharper than the wrong one**, and it is about the sweep, not the source
> — see the next section.

The case file's central English-side negative — *no John-and-Mary Gurney household in England baptises
a Mary, a Richard and a John* — has been carried as an England-wide statement. It is not one, but the
reason is not that the provider lacks the records. **The reason is that the sweep was run with three
constraints that each fail closed**, and FreeREG's value was in exposing them.

## Why the July sweep missed records its own provider held

Three independent narrowing errors, each of which silently returns fewer rows rather than an error:

1. **The surname stem.** `lastname=gurn*` does not reach `Gourny` or `Gourney`. That is why St Vedast
   1624 never appeared — the same defect that hid the Berkhamsted burials.
2. **The child's forename.** The sweep constrained the forename to **`Mary`**. Seventeenth-century
   clerks write **Marie, Marye, Maria, Marya**, and this project's own catalogue already contains
   "Marie Gurney", "Marye Garne" and "Maria Gorne". Epping 1625 is indexed **Marie**. Re-run on the
   same instrument and the same window with `firstname=mar*`, the count goes from the July sweep's
   **17** to **54**.[^marwild]
3. **The place token**, as established in unit 66 — a keyword filter is a literal match on the target
   set's own spelling of the parish.

**Three ways to fail closed on one query shape.** The July per-child totals — Mary 17, Richard 9, John
27, Peter 0, Isaac 0 — are therefore floors on their own instrument, before any question of
cross-provider coverage arises. The Peter and Isaac zeros in particular were run as exact forenames
and should be re-run wildcarded before they carry any weight.

**FreeREG's independent value stands**, and so does the reverse test: FreeREG **fails to return Hitcham
1631**, which FindMyPast and FamilySearch both hold, and carries no Great Berkhamsted Gurney baptism at
all. Neither instrument contains the other. **The negative is a floor, not a bound**, and it should be
restated that way wherever it appears — but the largest single cause of the undercount was query
construction, not provider coverage.

## The Mary sweep — the load-bearing child

Mary is the hard-bounded colonial child: she married Daniel Shed at Braintree in 1647, so she was born
by about 1631 whatever the compiled tradition says. A FreeREG baptism sweep for Mary, surname Gurney
with Name Soundex, England-wide, 1622–1636, returns **205 rows**, of which five belong to the Gurney
surname cluster:[^marysweep]

| Baptism | Person | Parish | Father | Status |
|---|---|---|---|---|
| 28 Oct 1624 | Mary **GOURNY** | St Vedast, Farringdon, London (City) | **Richard** | New to the file; **present in FindMyPast's Middlesex Baptisms**, missed by the `gurn*` stem |
| 10 Apr 1625 | Mary **GARNN** | Norton, Gloucestershire | — | Garne cluster; set aside on the household, not the surname (see unit 69) |
| 12 Feb 1625/6 | Marie **GURNEY** | **Epping, Essex** | **Robert**, mother **Sarra** | New to the file; **present in FindMyPast's Essex Baptisms**, missed by the `Mary` forename constraint |
| 12 Mar 1625/6 | Mary **GURNEY** | Norwich St Giles, Norfolk | — | Counted in the July totals, never catalogued |
| 2 Mar 1627/8 | Marie **GURNEY** | Ashwellthorpe, Norfolk | Willyam | Yes — CR-045 |

**Both new households resolve to the wrong father, and both are worth recording anyway.**

**Epping, Essex** was the one that had to be checked immediately, because Essex is where the colonial
evidence actually points — the son-in-law Daniel Shed of Finchingfield, the Tyng estate of Stanford
Rivers that John leased at Braintree, Braintree Massachusetts itself named for Braintree Essex, and
Anne Browning's Maldon connections. A Mary Gurney baptised in an Essex parish in February 1625/6 would
have been the best-placed candidate child the project had ever seen. The record names her father
**Robert** and her mother **Sarra**.[^epping] That closes it, and it closes it cleanly rather than by
inference.

**St Vedast Foster Lane** names a father **Richard** — a Gurney household in a City parish in 1624.[^vedast]
It bears on the §6.6 prediction only obliquely: the naming custom predicts a paternal grandfather
named Richard for the colonial John, and this is a Richard Gurney fathering in London in the right
generation. It is not a child of a John, so it does not enter the child inventory; it enters the
Richard-household comparator set, alongside the Salisbury Richard of 1630 and the Luton Richard of
1635. London had prominent Gurneys — Sir Richard Gurney was Lord Mayor in 1641–2 — so a St Vedast
Richard most plausibly belongs to that milieu rather than to a country tailor's line.

## The control fails, and the failure is informative

Method check C2 requires a national Mary sweep to return **Hitcham 1631**. FreeREG's does not.

That is not a broken query. **Hitcham is listed in FreeREG's own Buckinghamshire place index**, so the
parish is nominally covered — but a full FreeREG sweep of Buckinghamshire Gurney records, all three
event types, 1600–1700, returns **no Hitcham entry of any kind**.[^bucksfree] FreeREG's holdings for
that parish do not reach the 1631 baptism.

This is exactly why the method document singles FreeREG out as "the only one that tells you what it
has." The instrument declares its own gaps, and the gap here is real. **The FreeREG Mary sweep is
therefore a statement about FreeREG's covered parishes, not about England** — and the same is now
demonstrably true of the FindMyPast sweep, which misses Epping and St Vedast.

## The Richard sweep

England-wide, 1624–1638, same instrument: **116 results, three in the Gurney cluster**, and none to a
father John:[^richardsweep]

- Richard GURNEY, baptised **June 1624**, Stewkley — **new**; distinct from the January 1625/6 Richard
- Richard GURNEY, baptised 25 Jan 1625/6, Stewkley — CR-029, father Robert
- Richard GURNY, baptised 24 Oct 1630, Norwich St Lawrence — CR-047, father William

Two Richards at Stewkley eighteen months apart implies the first died in infancy and the name was
reused, which is ordinary — but it is a household detail the file did not have, and it is a reminder
that the Stewkley household is denser than the index rows suggested.

**Berkhamsted's Richard of 1626 is absent from FreeREG entirely**, confirming from a second direction
that FreeREG does not cover that parish.

## The John arm did not complete

FreeREG imposes a hundred-second search limit. A John sweep across England 1628–1642 exceeds it both
with Name Soundex on and with it off, and returns to the form without an error message.[^johnfail] The
John arm needs county-slicing to run at all. It is the least discriminating of the three children —
John is ubiquitous, and every named John hit on FindMyPast already resolved to a wrong father — so
this is a real gap but not an urgent one. **Recorded so it is not mistaken for a completed negative.**

## Buckinghamshire, read on the independent instrument

The densest candidate county is the one where a second transcription should pay most, because
FindMyPast's *Buckinghamshire Baptism Index* is drawn from the **bishop's transcripts** (its archive
references are `D/A/T/…`) while FreeREG transcribes **parish registers**. Where one series is lost the
other may survive; where both survive they are two witnesses and can disagree. That is the S10 point
in the method document, and this is the first time it has been acted on.

FreeREG's Buckinghamshire Gurney corpus, all event types 1600–1700, returns 499 rows — **the display
cap, so the run is incomplete** — of which 73 are Gurney-cluster and 29 fall in 1620–1649.[^bucksfree]
What that window contains:

**Stewkley dominates, and gains three events the file did not have.**

- **Walter ("Water") Gurney married Joan Coalls at Stewkley, 4 May 1620.**
- **Robert Gurney married Joan Fenn at Stewkley, 10 July 1626** — and Richard was baptised there on
  **25 January 1625/6, six months before that marriage**. So Joan Fenn is not Richard's mother; the
  March 2026 matrix gives the mother as Jane, and Robert therefore had two wives, the second married
  in mid-1626. **The Stewkley household splits on its own evidence** — a fourth same-name-or-same-household
  merge caught in this file, after Aylesbury, Berkhamsted and Candidate A.
- **Richd. Gowrney married Anne Liscombe at Stone, 10 November 1625.**
- Robert Gurney buried Stewkley 30 August 1631, matching the 1631 Stewkley probate of Robert
  Gorny/Gerny, husbandman; Richard Gurney buried Stewkley 29 April 1649 and again 16 July 1649;
  Richard Gourney buried Chesham 29 December 1631.

**And the negative that matters: no John Gurney is fathering anywhere in Buckinghamshire in FreeREG's
holdings across 1620–1649.** The only John rows in the whole county window are John Gourney baptised
at Chesham in 1600 and John Gurney baptised at Aston Abbotts on 11 January 1637/8 — the latter a child
of Robert and Sarah, already carried as CR-050. Hitcham, Weston Turville, Aylesbury St Mary and
Cheddington produce nothing in this instrument for the window.

## The complete sweep — 20 spellings, 3 event types, 585 records

The exploratory runs above were followed by an exhaustive pass: **twenty surname spellings × baptisms,
marriages and burials × all counties × 1600–1660**, sixty queries in all, no soundex.[^sweepmethod]
It captured **585 Gurney-cluster records**, held at
`sources/intake/archive/g13-july-2026-sweeps/freereg-g13-sweep-2026-07-28/results.tsv` — 232 baptisms, 178 marriages, 175
burials. No query hit the 500-row cap; the largest was *Gurney*/Baptism at 143.

**A calibration finding that justifies the whole approach: FreeREG's non-soundex surname matching is
exact.** A *Gurney* baptism query for 1600–1660 returns 143 rows, every one indexed literally
`GURNEY` — no *Gurny*, no *Gourney*, no *Gurnie*. So on this instrument the spelling variants are not
optional, and a single-spelling FreeREG search sees roughly a quarter of the Gurney record set.

### The central result

**Across all 585 records — every spelling, every event type, sixty years — not one has both a father
named John and a mother named Mary.** Thirty-eight records name a father John; thirty-one name a
mother Mary; the two sets do not intersect. The mother-Mary records have fathers named Robert, James,
Walter, Edward, Richard, William or Henry.

That is the strongest form the English-side negative has yet taken, because it is the one instrument
where the surname variance has been handled exhaustively rather than by a wildcard stem. It remains a
statement about FreeREG's covered parishes — which demonstrably exclude Hitcham and Great Berkhamsted
— but within that coverage it is complete.

### Father-John households the file did not have

| Household | Children | Bearing |
|---|---|---|
| **Lamport, Northamptonshire — John Gurney/Gournay + *Anne*** | John 1630, Thomas 1632, Steven 1634, Francis 1636, Charles 1637, Anne 1639, Katharine 1640 | The largest unrecorded father-John household found anywhere this month. **Eliminated**: wife Anne, and the household continues baptising to 1640 with no gap |
| **Longdon, Worcestershire — John Gurney + *Dorothy*, then + *Isabell*** | Giles and Rafe 1627 (Dorothy); Frances 1639, Alice 1641 (Isabell) | Two wives, neither Mary; continues past 1641 |
| **Oldswinford, Worcestershire — John Garney** | Humfry 1628, Elizabeth 1629 | Mother unindexed; no colonial-name child |
| **Earsham, Norfolk — John Girney** *(extends the known household)* | **John 1635, John 1636**, Henry 1638 (mother ***Ales***) | Two sons named John a year apart, so the first died. **"Ales" is Alice** — and FindMyPast indexes the same mother as "Alex", so two instruments agree the Earsham wife is not Mary. Earsham's closure is now doubly grounded |

### Two corrections to earlier work in this same file

**1. The June 1624 Stewkley Richard is not a reused name — his father is Walter.** Earlier in this
unit I inferred that two Richards at Stewkley eighteen months apart implied an infant death and reuse
inside Robert's household. The detail rows disprove it: **Richard, June 1624, father *Walter*, mother
*Joan***, against **Richard, 25 January 1625/6, father *Robert*, mother *Jane***. Two different
households — and Walter's ties directly to the marriage of **Walter Gurney and Joan Coalls at Stewkley
on 4 May 1620** already recorded above. The marriage and the child now join up, and the inference was
wrong.

**2. The Denton 1638 father conflict resolves against John.** Catalogue row CR-034 carried Mary
Gurney, Denton, Norfolk, 1638, with FindMyPast reading the father as *John* and Ancestry as *Josiah* —
logged as unresolved. FreeREG independently reads **Josias, mother Rachell**. Two of three instruments
now give Josias/Josiah. **Denton is not a father-John household** and should stop being carried as one.

### Further households new to the file

Marie Gurney, **North Weald Bassett, Essex**, 25 June 1637, father Robert, mother Anne — the parish
adjoins Epping, where a Robert Gurney and Sarra baptised Marie in 1625/6, so this is either the same
man remarried or a second Essex Robert. John Gurner, Crondall, Hampshire, 1625, father Robte. John
Gurner, Clayton, Sussex, 1634, father Thomas. John Gurner, Mamble and Bayton, Worcestershire, 1637,
father Thomas, mother Margery. John Gurney, Houghton Regis, Bedfordshire, 1638, father Joseph. Mary
Gurney, Wootton, Bedfordshire, 1640, father Dan.

## Consequences

**1. Restate the child negative as a floor.** The §6.1 statement and the unit-60 England-wide
formulation should both carry that the sweep behind them is one provider's, that a second provider
holds baptisms the first does not, and that the second in turn misses records the first holds. Two
partial instruments that each catch what the other drops do not add up to a complete one; they
establish a lower bound on how many Gurney baptisms existed and nothing about the upper bound.

**2. The Epping and St Vedast rows are closed but must stay catalogued.** Both are in the right window
for the colonial Mary and both would have been live candidates had their fathers not been read. Under
the catalogue rule they are record instances with provenance and are entered as such.

**3. The Stewkley household is two marriages, not one.** Robert Gurney's 1626 marriage to Joan Fenn
post-dates a child of his by six months. Any statement resting on the Stewkley household's shape
should be marked conditional, per §3 of the method.

**4. The bishop's-transcript versus parish-register distinction is now demonstrated, not just
asserted.** FreeREG's Buckinghamshire holdings and FindMyPast's Buckinghamshire Baptism Index return
materially different Gurney event sets for the same county and window. Neither is the county's record.

**No probability row moves on this pass.** Nothing here promotes or demotes a candidate: the two new
Marys have wrong fathers, and the Buckinghamshire negative is consistent with what the file already
held. What moves is the **confidence attached to the negatives**, which should fall.

## Coverage statements arising

- **FreeREG does not cover Great Berkhamsted** for the seventeenth century — no Berkhamsted Gurney
  baptism, including the 1626 Richard that FindMyPast's Hertfordshire set carries.
- **FreeREG's Buckinghamshire holdings contain no Hitcham Gurney record** for 1600–1700, though
  Hitcham appears in its place index.
- **FreeREG's Buckinghamshire run is capped at the 500-row display limit** for 1600–1700, so it must be
  re-run in narrower windows before any county-level FreeREG negative is asserted.
- **Name Soundex on "Gurney" collides with "Green"** — both are Soundex G650 — so a soundex sweep is
  dominated by Green/Greene rows and hits the display cap quickly. Useful for discovery, useless for
  counting.

## Crosslinks

- [`65-refactor-child-inventory-method.md`](65-refactor-child-inventory-method.md) — the method; S8 is executed here for the first time
- [`66-refactor-berkhamsted-burials-and-the-departure-gap.md`](66-refactor-berkhamsted-burials-and-the-departure-gap.md) — the previous pass
- [`62-refactor-the-per-child-sweep.md`](62-refactor-the-per-child-sweep.md) · [`60-refactor-matching-by-family-not-by-man.md`](60-refactor-matching-by-family-not-by-man.md) — the FindMyPast per-child sweep this qualifies
- [`59-refactor-open-actions.md`](59-refactor-open-actions.md) — actions arising
- Catalogue: `research/people/g13-john-gurney/coverage/child-record-catalog.csv`

[^sweepmethod]: FreeREG (freereg.org.uk), swept 28 July 2026 across twenty surname spellings — Gurney, Gurny, Gurnie, Gourney, Gourny, Gorney, Gurnay, Gournay, Garney, Girney, Gerney, Gernne, Gowrney, Gorne, Garne, Gurnoe, Gurner, Greney, Gowrne, Hurney — each run separately for Baptism, Marriage and Burial, all counties, 1600–1660, Name Soundex off. Sixty queries; one (`bap-gurnoe`) timed out and succeeded on retry; none reached the 500-row display cap. Results, per-query log and method notes at `sources/intake/archive/g13-july-2026-sweeps/freereg-g13-sweep-2026-07-28/` (`results.tsv`, `PROGRESS.md`, `_summary.txt`). **Method disclosure:** the volume of detail pages made driving the browser impractical, so the queries were issued by script against the same anonymous, unauthenticated public form and record endpoints the browser session uses; no login, no paywalled content, and the record-detail fields recorded are those FreeREG displays publicly. The 585-row total, the 38 father-John rows and the nil intersection of father-John with mother-Mary were re-derived independently from the raw TSV rather than taken from the run's own summary. Source ID: `freebmd-freereg`.
[^fmpholds]: FindMyPast cross-collection search, authenticated session, 28 July 2026. `sid=999&collection=parish+baptisms&sourcecountry=great+britain&firstname=mar*&lastname=gurn*&keywords=epping` returns "Gurney Marie, 1625, Epping, Essex" three times — once in *England Births & Baptisms 1538–1975* and twice in *Essex Baptisms* (Epping All Saints and Epping Upland All Saints). `lastname=gourn*&keywords=vedast` returns two rows in *Middlesex Baptisms*: "Gourny Mary, 1624, St Vedast Foster-Lane, London" and "Gourney Anne, 1626, St Vedast Foster-Lane, London". The *Essex Baptisms* and *Middlesex Baptisms* record sets are reached here through the cross-collection view and are not separately registered; they are covered by the general parish-baptism source. Source ID: `findmypast-uk-parish-baptisms`.
[^marwild]: Same instrument and session: `sid=999&collection=parish+baptisms&sourcecountry=great+britain&firstname=mar*&lastname=gurn*&yearofbirth=1629&yearofbirth_offset=10` (1619–1639) returns **54 results**, against the 17 recorded for the exact forename *Mary* in the July 2026 sweep. The wildcard also admits Margaret/Margret/Mark rows, so 54 is not a corrected Mary count — it is a demonstration that the exact-forename constraint was excluding real Marie/Marye/Maria rows. Source ID: `findmypast-uk-parish-baptisms`.
[^marysweep]: FreeREG (freereg.org.uk), parish-register transcriptions by volunteer transcribers, searched 28 July 2026: surname Gurney, forename Mary, baptisms, 1622–1636, all counties, Name Soundex on — 205 results, listed by date. The five Gurney-cluster rows are as tabulated; the remainder are Green/Greene/Grime/Groome/Gorham rows returned by the Soundex collision. Source ID: `freebmd-freereg`.
[^epping]: FreeREG record detail, Essex, Epping, All Saints, Parish Register: "Baptism date 12 Feb 1625/6; Person forename Marie; Person sex F; Father forename Robert; Mother forename Sarra; Father surname GURNEY", transcribed by Julie Harold, file line 1373. Source ID: `freebmd-freereg`.
[^vedast]: FreeREG record detail, London (City), Farringdon, St Vedast, Other Transcript: "Baptism date 28 Oct 1624; Person forename Mary; Person sex F; Father forename Richard; Father surname GOURNY", transcribed by Pat Lawrence, file line 622. No mother is recorded. Source ID: `freebmd-freereg`.
[^bucksfree]: FreeREG, searched 28 July 2026: surname Gurney, county Buckinghamshire, all three record types, 1600–1700, Name Soundex on — **499 results, which is the display cap**, of which 73 are Gurney-cluster and 29 fall in 1620–1649. Hitcham appears in FreeREG's Buckinghamshire place index (99 places listed) but returns no Gurney record in this run. Source ID: `freebmd-freereg`.
[^richardsweep]: FreeREG, searched 28 July 2026: surname Gurney, forename Richard, baptisms, 1624–1638, all counties, Name Soundex on — 116 results, three in the Gurney cluster. Source ID: `freebmd-freereg`.
[^johnfail]: FreeREG, 28 July 2026: surname Gurney, forename John, baptisms, 1628–1642, all counties, attempted with Name Soundex on and again with it off. Both attempts returned to the search form without a results page or an error message, consistent with the stated hundred-second search limit being exceeded. Not a negative result. Source ID: `freebmd-freereg`.
