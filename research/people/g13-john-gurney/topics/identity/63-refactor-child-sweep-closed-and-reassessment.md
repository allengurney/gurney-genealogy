<!-- July 2026 refactor working round. Its findings are carried in the permanent identity units
     30- to 39-, which are the current account; this file is retained as the working record,
     including its own correction and retraction trail, which is deliberate and belongs to the
     research layer. Not yet in the G13 context graph — graph-bearing content is tracked in
     sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# The child angle closed, the wills searched from the inside, and a reassessment

> **RETRACTION, 2026-07-28, same day.** This unit originally reported that "one baptism in the whole
> country belongs to a household whose father is a John." **That is false.** The sweep behind it
> searched by *child* forename with the surname stem `gurn*`, and the correct instrument — a
> **parent-name** search across all collections — returns **315 parish-baptism rows for children of a
> John Gurney (variants) in Great Britain, 1611–1651**. See §1a. The substantive conclusion below —
> that no *new* John-and-Mary household with a colonial-shaped child set has surfaced — is unaffected
> in the tight window but is **no longer fully established**, and the probability move it supported
> has been withdrawn (§3).

## 1a. The retraction, and what it changes

Three compounding errors produced the false claim, and they are worth recording because each is a
general trap.

**The parameter-name error.** FindMyPast's `datasetname=` mode ignores `fathersfirstname` (with an
S). Testing that spelling and finding it inert, this file concluded that *no* parent-forename
parameter binds on *any* FindMyPast baptism dataset, and wrote that into the search skill. The
parent search works perfectly well — the parameters are `fatherfirstname`, `fatherlastname`,
`motherfirstname`, **no S**, in a third results mode (`sid=102`) this project had not found.[^sid102]

**The wildcard-as-variant error.** `gurn*` covers one stem. FindMyPast's `_variants=true` engine
reaches **Gernne, Garne, Gourney, Gowrne, Greney, Gurner** — spellings a `gurn*` query cannot match.
This repo registers eighty-seven surname variants and the sweep used one prefix. Households missed
outright for that reason alone include Toddington's **John Gernne** and Compton Abdale's **John
Garne**.

**The axis error, which is the substantive one.** Searching by *child* forename can only find
children whose forename was guessed in advance. Searching by *parent* returns the household's whole
child list — including the siblings that identify it. If the question is "does this family exist
anywhere", the parent search is the query, and it should have been the first one run.

**What the correct instrument shows.** Father John Gurney with variants, parish baptisms, Great
Britain: **315 rows across 1611–1651**, and **108 for the tight 1625–1635 window**. Run again with the
surname *strict* rather than variant-expanded, 1625–1635 returns **11** — and those eleven are all
households the case file already carries: Toddington (Elizabeth 1625, Anne 1628, Audrey 1634), East
Claydon (Elinor 1632, Samuel 1636), Weston Turville (Elyzabethe 1627), Chesham (Andtr, Martha),
Eythorne (Thomas 1635).[^strict] The 108-minus-11 difference is largely variant-engine noise — the
expansion also returns Gray, Griffith and Gaune — but not entirely.

**Households the file does not have, surfaced by the variant-expanded run and not yet worked:**

```
1621  Tilsworth, Beds          John Gurney        father John Gurney
1640  Luton, Beds              John Gurney        father Jn. Gurney,  mother Eliz.
1631  Toddington, Beds         John Gernne        father John Gernne
1649  Kinnersley, Herefs       John Gowrne        father John Gowrne
1638  Compton Abdale, Glos     Marye Garne        father John Garne
1612  Ryton, Durham            Margaret Greney    father John Greney
```

**And the mother filter is a trap of its own.** Adding `motherfirstname=mary` narrows 315 rows to
18 — but it silently drops every household whose mother is unindexed, which is most Buckinghamshire
bishop's transcripts. Hitcham itself, whose mother is unindexed, does not appear in the
mother-filtered list. The father-only list is the work list; the mother filter is a ranking aid, not
a test. Of the 18, the genuine John-and-Mary households are **Eythorne** (already eliminated), a
**John Gurley and Mary at Westminster** with children Eliz 1627, Ellynor 1628, Alexander 1629, Mary
1631 and Sara 1633, and a Hungerford, Berkshire family of 1652.[^mother]

**Net.** In the tight 1625–1635 window under the strict spelling, no household appears that the case
file does not already carry — so the working conclusion survives there. But it does **not** yet hold
across the full 1611–1651 range or across the variant spellings, and it must not be reported as
though it does until the 315 are read.

## 1. Every named hit's father, resolved

The per-child sweep is now finished: five forenames, surname wildcarded, no parent constraint, every
parish-baptism collection in Great Britain, with the **father read for every named hit**.[^sweep]

| Child | Records | Fathers found |
|---|---|---|
| Mary 1624–34 | 17 | **Hitcham 1631 — John**; Linslade 1633; Kelham (Notts) 1630; Bishop's Stortford 1629; Eythorne (Kent) 1633; London 1624, 1627, 1634; Norwich St Giles 1625 |
| Richard 1625–35 | 9 | Stewkley 1626 — **Robert**; Norwich St Lawrence 1630 — **William**; **Luton St Mary 1635 — Richard, mother Joyce**; Berkhampstead 1626 and 1635 — Candidate C's household; Toddington 1636; London 1628 |
| John 1629–39 | 27 | Cheddington 1634 — **Isaac and Martha**; Aston Abbotts 1637 — **Robert and Sarah**; Wingrave 1624 — **Thomas**; Toddington 1630 — **Thomas**; Aylesbury 1638 — Candidate A(ii); Eythorne 1638 — Kent; Clapham and Houghton Regis, Beds |
| Peter 1627–47 | **0** | — |
| Isaac 1632–52 | **0** | — |

~~One baptism in the whole country belongs to a household whose father is a John: Hitcham, 1631.~~
**Retracted — see §1a.** What survives of this is narrower and still useful: **of the baptisms
carrying one of the colonial child forenames, Hitcham 1631 is the only one whose father is a John.**
That is a statement about a child-forename sweep, not about England. Separately, Hitcham does yield
**exactly one Gurney-variant baptism in 1611–1651** on a place-keyword run across every collection,
so the file's "single indexed event" for that parish is confirmed nationally.[^hitcham]

**On the possibility that a wrong father is a transcription error.** It is the right question to ask —
this project has already caught an indexer reading H as G — but it does not rescue much here. The
fathers that block these households are **Robert, William, Isaac, Thomas** and **Richard**. In a
secretary hand *John* is short, two-syllable and distinctive; none of those five is a plausible
misreading of it, and the abbreviated forms that *could* confuse (`Jo:` against `Ja:` or `Ju:`) do not
occur in any of the returned rows. The escape route is narrow and should be recorded as narrow rather
than left open as a hope.

## 2. Searching the wills from the inside

The sweeps so far have searched *indexes*. FamilySearch Full-Text Search reads the **document text**,
which makes possible the one question no index can answer: **is a John Gurney named as somebody's son
inside a will?** That is the record class that would settle the identification outright.

Every phrasing of it returns nothing:[^fts]

```
"my sonne John Gurney"    0        "sonne John Gurnye"       0
"sonne John Gurney"       0        "sonne John Gurnie"       0
"sonne John Gurny"        0        "John Gurney my sonne"    0
```

Loosening to co-occurrence, `+"John Gurney" +sonne` returns 26, of which five are pre-1700: a 1559
English will, a 1621 Cheshire will, a 1638–39 Cambridgeshire will, and two Bury St Edmunds parish
records of 1634 and 1653. **None names a John Gurney as anyone's son.**

**The trade probe is a clean negative too.** `"John Gurney taylor"` and `"John Gurney tailor"` each
return eight hits — every one of them eighteenth-century or later, led by Norwich St Martin at Oak
tax rolls of 1729 and 1730. **No John Gurney is styled tailor anywhere in the full-text corpus before
1700.** The colonial deed remains the only attestation of the trade in existence.

**One small positive.** The 1634 Bury St Edmunds hit resolves, on the transcript, to **"Juda Gurney"**
in a list of parishioners.[^juda] The file's Bury material begins in 1653; this pushes a documented
Gurney presence at Bury back to **1634**, inside the emigration window and at the parish Banks named.
It does not name a John and it does not support Banks's attribution directly — but it shows Banks was
pointing at a parish that actually held Gurneys in the right decade, which is more than the file
could previously say.

**Coverage bound, and it is a real one.** The same instrument returns **zero pre-1700 hits** for
`"Michael Gurney" + Dereham` and for `Gurney + Yaxham`. FamilySearch's full-text coverage of Norfolk
parish and manorial material before 1700 is thin and its Latin court hand transcribes as salad, so
these are *instrument* negatives, not record negatives, and they leave the Yaxham test (action R-23)
exactly where it was — an index-and-image job, not a full-text one.

## 3. Reassessment

Six weeks of work in one week has moved four things. Stated as the direction each cuts:

**Against Candidate B.** It has lost its exclusive claim on the "why East Dereham" evidence, which is
symmetric between a gentleman moving in and a propertied local family already there. Its Norfolk
residence anchor is contestable, since nothing places Francis-A in the parish except the children at
issue. The register can test neither reading — 1596–1607 and 1611–15 are both lost. Nothing positive
surfaced for it in the largest untested classes: Chancery, Requests, Star Chamber, certificates of
residence, Exchequer depositions, or the wills read from the inside. And §11's stated reason for
ranking a hypothesised man above documented ones — that B alone carries an evidenced emigration
link — is not supportable while two of John's own Weymouth land-neighbours are Aylesbury-Vale men.

**For the "documented but never assembled" reading.** This is the row the week's work most supports,
and it now rests on a **demonstrated false negative** rather than an argument: the file recorded no
Stewkley Gurney record after 1614, and there are five. Alongside it, four households nobody had
assembled surfaced from one afternoon in free catalogues — Stoke Mandeville 1621–25, Broughton in
Bierton 1592–98/9, Aston Abbotts, Farnham Royal now dated to 1629 — and an entire county, with 141
Gurney baptisms in the window, has never been swept.

**For the surviving Buckinghamshire men, modestly.** Hitcham is now the only 1-of-3 child hit in
England after a properly run national test. The Cheddington prediction is more robust than the case
file allows, because the naming custom counts sons and daughters separately and Sarah cannot displace
Richard from the eldest-son slot. Weston Turville goes the other way, drawn into the Aylesbury-hundred
Pakington tenantry rather than standing apart.

**Against the "no record survives" reading, slightly.** The nets that failed this week were genuinely
strong — a both-parties-indexed national marriage index, a wildcarded national baptism sweep, and the
wills searched from the inside. But the same week proved that a chunk of the apparent silence was
*search* rather than survival. Mass should move out of this row into the unassembled one, not
accumulate in it.

### The revised table

> **Superseded within the day by the Berkhamsted split.** Working the parent-name sweep as
> *households* rather than counting rows produced a new named candidate — **C(ii), the younger Great
> Berkhampstead John, fathering 1624–1637, born c.1598–1602, about 51 in 1653, with three colonial
> child forenames and a departure-shaped gap after two child deaths in 1639**. See
> [`64-refactor-berkhamsted-reopened.md`](64-refactor-berkhamsted-reopened.md). The table below is the
> current one and already carries him; the pre-Berkhamsted draft (assembled 28%, B 12%, C 1%) should
> not be used.

| Candidate / category | Was | **Now** | What moved it |
|---|---:|---:|---|
| **Documented but never assembled** | 22% | **22%** | Three proven false negatives now — Stewkley's registers, the parent-search mode, and the Berkhamsted merge. The row would have risen sharply, but **C(ii) has been carved out of it as a named row**, which is exactly what this category is *for*: it converts to named candidates when worked. |
| **No record survives or is indexed** | 24% | **18%** | Every time this file has claimed silence, part of it has been search technique. Three demonstrations in one week is a pattern, and the residual genuinely-unrecorded mass is smaller than it looked. |
| **B — son of Francis and Margaret Rybett** | 18% | **11%** | "Why East Dereham" no longer favours it; residence anchor contestable; §11's ranking rationale unsupportable; nothing positive in the largest untested classes — and it is now outranked on the child-name test by a documented household |
| **C(ii) — the younger Great Berkhampstead John** | *(inside C, 1%)* | **9%** | **New named row.** Documented man, born c.1598–1602 from his own first child, about 51 in 1653; **John 1624, Richard 1626, Sarah 1634** — three colonial forenames, more than any other English household; two children dead in Feb–March 1639; household stops in 1637 with **no burial for anyone in the family at Berkhamsted, ever**. Blocked by a missing Mary and by early dates; the burial negative needs a coverage check. See `64-`. |
| **Ackworth (Gurnoe × Mary Burton)** | 6% | **7%** | The only unaccounted-for John × Mary marriage in England before 1660, on a both-parties-indexed national instrument |
| **Hitcham head** | 3% | **4%** | *Revised down from a provisional 6% after the §1a retraction.* The "only 1-of-3 hit in England" claim that justified 6% rested on the flawed child-forename sweep. What survives is thinner: the only colonial-forename baptism with a father John, and a parish confirmed nationally to hold a single Gurney event. That is worth a point, not three. |
| **Cheddington 1608 (son of Richard)** | 5% | **6%** | The naming prediction survives the Sarah objection intact; Isaac and John both attested in that parish's Gurney household |
| **Bucks / Herts / Beds heads cleared as a group** | 3% | **6%** | Group materially larger; the class has a colonial-side reception channel at Weymouth that B lacks |
| **A(1603) — Stewkley baptism** | 5% | **4%** | Stewkley's Gurneys demonstrably kept baptising — but that is Robert's household, and the 1603 John still has no trail of his own |
| **D — London Old Change draper** | 4% | **4%** | Unchanged |
| **§8.5 Newgate apprentice** | 3% | **3%** | Unchanged |
| **Weston Turville head** | 4% | **3%** | Drawn into the Aylesbury-hundred tenantry rather than standing apart |
| **C(i) — the elder Great Berkhampstead John** | 1% | **1%** | Fathering from 1597, so born c.1570–75. The case file's age elimination applies to him exactly and is sound |
| **Stewkley 1611 (son of Robert)** | 1% | **1%** | Unchanged |
| **Other and out-of-corridor** | 1% | **1%** | Unchanged; the six unworked households the parent-name sweep surfaced sit inside the unassembled row until they are worked |

**Reading.** The identification is more open than it was, not less, and the shape of the answer has
changed. **"Documented but never assembled" is the leading row at 22%**, and it earned that on
evidence: three separate claims of silence in this file turned out to be search technique in a single
week. Candidate B, at 11%, is no longer the leading named candidate either — **C(ii), the younger
Berkhamsted John, is within two points of it at 9%**, and beats it on the one test B has never
passed: a documented household whose children's names match.

The honest statement is now that the single most likely answer is *a man already sitting in records
we have gathered whom nobody has assembled* — and that C(ii) is what that looks like when the work is
actually done. Three of the file's most confident negatives (Stewkley's registers, Berkhamsted's
elimination, "one household with a father John") failed in one week. That is the base rate to apply
to the remaining ones.

**What would move these numbers.** C(ii) rises sharply if the Berkhamsted burial register survives
intact for 1600–1660 and still holds no Gurney, or if a Mary Gurney baptism turns up there c.1620–24;
it falls sharply if the burial series is simply missing, or if the younger John is found buried or
proved in Hertfordshire. B rises on a document naming a John as Francis's son, or on a Yaxham
child-list with no Francis in it; it falls if Arthur Gurney's household produces a Francis. Hitcham
and Cheddington rise on a marriage licence in the south-Midlands archdeaconry series. The unassembled
row converts to named rows as it is worked — which is what just happened.

## Crosslinks

- [`62-refactor-the-per-child-sweep.md`](62-refactor-the-per-child-sweep.md) — the sweep this closes
- [`56-refactor-the-east-dereham-gurney-family.md`](56-refactor-the-east-dereham-gurney-family.md) · [`58-refactor-weymouth-reception-reweighed.md`](58-refactor-weymouth-reception-reweighed.md) · [`61-refactor-where-the-records-actually-live.md`](61-refactor-where-the-records-actually-live.md) — the findings behind the movements
- [`59-refactor-open-actions.md`](59-refactor-open-actions.md) — open actions
- Graph tracker: [`sources/intake/g13-graph-breadcrumb.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/intake/g13-graph-breadcrumb.md)

[^sid102]: FindMyPast parent-name search across collections, authenticated session, 28 July 2026. Working URL form: `https://www.findmypast.co.uk/search/results?sourcecategory=life+events+(bmds)&collection=parish+baptisms&sourcecountry=great+britain&sid=102&fatherfirstname=john&fatherfirstname_variants=true&fatherlastname=gurney&fatherlastname_variants=true&yearofbirth=<YYYY>&yearofbirth_offset=<N>`. Note `sid=102` and the parameter names **without** a medial "s" — the `datasetname=`/`sid=103` mode's `fathersfirstname` is a different, non-binding parameter. Returns 315 parish-baptism rows for 1611–1651 and 108 for 1625–1635. Mechanics recorded at `.claude/skills/findmypast-record-search/SKILL.md` §0b. Source ID: `findmypast-uk-parish-baptisms`.
[^strict]: Same instrument and window with `fatherlastname=gurney` and **no** `fatherlastname_variants` flag: 11 rows for 1625–1635 — Chesham (Andtr, Martha), Toddington (Elizabeth 1625 ×2, Anne 1628 ×2, Audrey 1634), East Claydon (Elinor 1632, Samuel 1636), Weston Turville (Elyzabethe 1627), Eythorne (Thomas 1635). The variant-expanded run's extra rows include genuine expansions (Gernne, Garne, Gowrne, Greney, Gourney) and substantial noise (Gray, Griffith, Gaune, `?`-surname rows), so both runs are needed and neither count can be trusted alone. Source IDs: `findmypast-uk-parish-baptisms`; `findmypast-bucks-baptism-index`; `findmypast-bedfordshire-baptisms`.
[^mother]: Same instrument with `motherfirstname=mary&motherfirstname_variants=true`, 1611–1651: 18 parish-baptism rows. Genuine John-and-Mary Gurney households: Eythorne, Kent (Thomas 1635, John 1638, Edward 1641, across three surname spellings) — already eliminated; **John Gurley and Mary at Westminster** (Eliz 1627, Ellynor 1628, Alexander 1629, Mary 1631, Sara 1633); and a Hungerford, Berkshire baptism of 1652 (Mary Garmye/Garneye). Hitcham does **not** appear, because its mother is unindexed — which is the reason the mother filter cannot be used as a test of a household's existence. Source ID: `findmypast-uk-parish-baptisms`.
[^sweep]: FindMyPast cross-collection parish-baptism searches and county-set drill-downs, 28 July 2026; totals and query forms at [`62-refactor-the-per-child-sweep.md`](62-refactor-the-per-child-sweep.md). Luton St Mary 1635 read from *Bedfordshire Baptisms*, `lastname=gurn*&firstname=rich*`: "Rich Gurney, 1635, father Rich, mother Joyce, Luton" with its duplicate row "Richard Gurney, 1635, father Richard, mother Joyce, Luton, St Mary". Source IDs: `findmypast-uk-parish-baptisms`; `findmypast-bedfordshire-baptisms`; `findmypast-bucks-baptism-index`; `findmypast-norfolk-baptisms-index`.
[^hitcham]: Same instrument with a place keyword — `lastname=gurn*&collection=parish baptisms&sourcecountry=england&yearofbirth=1631&yearofbirth_offset=20&keywords=hitcham` — returns one row: Mary Gurny, 1631, Buckinghamshire Baptism Index, Hitcham. Mechanically useful: **`keywords=` does bind on the cross-collection search**, where `location=` does not, and is the practical place filter for that mode. Source ID: `findmypast-bucks-baptism-index`.
[^fts]: FamilySearch Full-Text Search, authenticated session, 28 July 2026, via the JSON service endpoint `/service/search/fulltext/search`. Phrase probes returning zero: "my sonne John Gurney", "sonne John Gurney", "sonne John Gurny", "sonne John Gurnye", "sonne John Gurnie", "John Gurney my sonne". Co-occurrence probes: `+"John Gurney" +sonne` = 26 (five pre-1700: a 1559 English will, a 1621 Cheshire will, a 1638–39 Cambridgeshire will, Bury St Edmunds parish records of 1634 and 1653); `+"John Gurny" +sonne` = 1 (Bury St Edmunds 1653); `"brother John Gurney"` = 21 (earliest pre-1700 rows 1663 Philadelphia and 1693 Lancashire); `"John Gurney gentleman"` = 4. Trade probes: `"John Gurney taylor"` and `"John Gurney tailor"` = 8 each, every row 1729 or later, led by Norwich St Martin at Oak tax rolls of 1729 and 1730. Norfolk coverage probes: `+"Michael Gurney" +Dereham` = 8 and `+"Gurney" +Yaxham` = 130, **none pre-1700** — an instrument limit, not a record negative. Source ID: `familysearch-fulltext-search`.
[^juda]: Same session: FamilySearch Full-Text Search ark `3:1:3QS7-89C5-3ZNK`, Bury St Edmunds, Suffolk, 1634, record type Parish. The machine transcript reads, in a run of parishioners, "… John Cuppur sonne of John . **Juda Gurney**, William Maulton, John Russilles sonne of Edmund …". Transcript level; the image has not been read, and "Juda" should be treated as a machine reading of Judah or Judith until it is. Source ID: `familysearch-fulltext-search`.
