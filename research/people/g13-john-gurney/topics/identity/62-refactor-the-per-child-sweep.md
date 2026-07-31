<!-- July 2026 refactor working round. Its findings are carried in the permanent identity units
     30- to 39-, which are the current account; this file is retained as the working record,
     including its own correction and retraction trail, which is deliberate and belongs to the
     research layer. Not yet in the G13 context graph — graph-bearing content is tracked in
     sources/intake/g13-graph-breadcrumb.md. Not linked from published pages. -->

# The per-child sweep — and what the single-dataset habit was hiding

Two method errors have been shaping this file's negatives, and both were mine rather than the
records'.

**The first is a search-mode error.** Every FindMyPast sweep recorded here has used the
single-dataset form — `datasetname=<one collection>` — which asks one transcription at a time.
FindMyPast also has a **cross-collection mode** that queries every parish-baptism set in Great
Britain at once: `sourcecategory=life events (bmds)` + `collection=parish baptisms` +
`sourcecountry=great britain` + `sid=999`, with **no** `datasetname`.[^xcoll] Some of what it returns
is flagged *Exclusive* to FindMyPast — records in no other provider's index. A single-dataset habit
was therefore producing negatives that measured one transcription's coverage and were being written
down as statements about England.

**The second is a threshold error.** The matching test has been "does a household baptise Mary **and**
Richard **and** John in the right window?" Against seventeenth-century registers — lost membranes,
illegible entries, wandering surname spellings — requiring all three is a filter engineered to return
nothing. **The right threshold is one child of the right name in the right window, then investigate
the household.** Two of three is a strong hit; three of three would be a gift.

## The wildcard control, and why it is not optional

Run twice on the same window, once exact and once wildcarded, **Mary Gurney 1624–1634 returns six
records and Mary Gurn\* returns seventeen** — and the seventeen include the case file's own
**Hitcham, Buckinghamshire, Mary Gurny, 1631, father John**, which the exact run misses because the
index spells the surname `Gurny`.[^mary]

A record the file already holds, absent from a national search of the exact name, is the cleanest
possible proof that **every exact-spelling figure in this project is a floor, not a count.** The
wildcard also pulls in `Gurnard`, `Gurnel`, `Gurner`, `Gurnett`, `Gurnte` and `Gurny` forms — six
spellings that a `Gurney` query never sees.

## The completed per-child sweep

Run per child forename, surname wildcarded, **no parent constraint**, across every parish-baptism
collection in Great Britain:[^sweep]

| Child | Window searched | Records in all GB | Any to a **John + Mary** household? |
|---|---|---|---|
| **Mary** | 1624–1634 | **17** | **Hitcham, Bucks, 1631** — father John, mother unindexed. The only one. |
| **Richard** | 1625–1635 | **9** | **None.** |
| **John** | 1629–1639 | **27** | **None identified.** |
| **Peter** | 1627–1647 | **0** | — |
| **Isaac** | 1632–1652 | **0** | — |

The households behind the named hits, with fathers read from the county sets:

```
Richard   1626  Stewkley, Bucks           father Robert           (Exclusive to FindMyPast)
Richard   1630  Norwich St Lawrence, Nfk  father William          (+ a twin row at St John Maddermarket)
Richard   1626  Berkhampstead, Herts      = Candidate C's household
Richard   1635  Berkhampstead, Herts      = same household
Richard   1636  Toddington, Beds          (Exclusive)
Richard   1635  Luton St Mary, Beds
Richard   1628  London
John      1634  Cheddington, Bucks        father Isaac, mother Martha
John      1637  Aston Abbotts, Bucks      father Robert, mother Sarah
John      1624  Wingrave, Bucks           father Thomas
John      1630  Toddington, Beds          father Thomas
John      1629  Clapham, Beds             (Exclusive)
John      1638  Houghton Regis, Beds      (Exclusive)
Mary      1631  Hitcham, Bucks            father John
Mary      1633  Linslade, Bucks
Mary      1630  Kelham, Notts
```

Three things fall out of it.

**Peter and Isaac are absolute zeros, and that is probably a fact about the colony, not the search.**
No Peter Gurney-variant baptism exists anywhere in Great Britain across 1627–1647, and no Isaac
across 1632–1652 — wildcarded, every collection. Set beside where those two men actually appear —
Peter first in a Weymouth muster of December 1675, Isaac first in a Plymouth court record of March
1663/4 — **the simplest reading is that both were born in New England.**

That is a correction to the case-file baseline, which lists the children "born in England" as Sarah,
Mary, Richard, John Jr. and Peter, with Isaac possible.[^baseline] On this evidence the English child
set is **Mary, Richard and John** — and, if she existed at all, Sarah. Two of the five have probably
been on the English side of the ledger by assumption. It also retires the Peter search as an English
question: the rare-name lever everyone reached for does not bear on England at all.

**Under the corrected one-child threshold, Hitcham is the sole survivor in England.** It is the only
baptism in the entire sweep to a household whose father is a John and whose child bears a colonial
name in the right window. That is not a strong candidate — a single indexed event, mother unindexed,
nothing before or after, and the file rates it ~3% — but it is now the **only** 1-of-3 hit in the
country, which is a materially different standing from "one of several weak Bucks rows."

**Everything else resolves to a household with the wrong father.** Stewkley 1626 is Robert's;
Norwich St Lawrence 1630 is William's; Cheddington 1634 is Isaac and Martha's; Aston Abbotts 1637 is
Robert and Sarah's; Wingrave 1624 and Toddington 1630 are Thomas's. None is a John.

## Two side-findings worth keeping

**The Cheddington household gains a son John.** The naming-convention unit describes the parish's
later Gurney entries as "Isaac Gurney and Martha, children Jane 1636 and Martha 1641."[^unit54] Add
**John, baptised 14 December 1634, son of Isaac and Martha**.[^chedd] That does not make him the
colonial John Jr. — the colonial John's father was a John — but it sharpens the unit's second
argument: **Isaac and John were both live forenames in the Cheddington Gurney household in the
emigrant's own generation**, which is the pairing the colonial family shows.

**The Berkhamsted / St Albans provider disagreement is confirmed from both sides.** FindMyPast
indexes the 1626 Richard at **Berkhampstead, Hertfordshire**; FamilySearch indexes the same child at
**St Peter, Hertfordshire** (St Albans). Both spellings of the surname appear — `Gurnie` 1626,
`Gurny` 1635 — and both providers carry the household. The discrepancy is specific and real, not an
artefact of one bad row.

## The Stewkley statement is wrong

The most consequential thing the corrected sweep turned up is not a candidate but a correction.

The file states, in the Buckinghamshire elimination unit and again in the case file: *"The
Buckinghamshire parish-register collections carry no Stewkley Gurney record of any kind after 1614,
which had been read as the household going silent. The probate index corrects it… the family
continued at Stewkley for another forty years and **the register silence was a coverage
artefact**."*[^unit52]

**There was no register silence.** The Buckinghamshire Baptism Index and England Births & Baptisms
between them carry, at Stewkley:

```
1615   [child, forename not transcribed]   father Robert   Buckinghamshire Baptism Index
1615   Anthony Gurney                      father Robert   Buckinghamshire Baptism Index
1616   Anne Gurney                         father Robert   Buckinghamshire Baptism Index
1618   [child, forename not transcribed]   —               England Births & Baptisms 1538-1975
1626   Richard Gurney                      father Robert   England Births & Baptisms / Bucks Baptism Index
```

The Stewkley Gurneys are in the parish registers continuously through the period the file describes
as blank. The probate evidence that was said to "correct" the silence — Robert Gurnie husbandman
1618, Robert Gorny/Gerny husbandman 1631, Robert Gurney yeoman 1651 — now reads as **the same Robert
household the baptisms name**, and the two Roberts of 1618 and 1631 are exactly what a father-and-son
sequence baptising in 1615–1616 and again in 1626 predicts.

So the argument stands but its basis changes, and the change matters: the file has been treating a
**search artefact** as a **coverage artefact**. One says the records are thin; the other says we
looked in one place. Everywhere the file says "the collections carry no record," that claim now needs
re-testing on the cross-collection instrument before it can be relied on.

**On the candidate itself:** Richard Gurney of Stewkley, 1626, is the son of **Robert**, not of a
John, so he is not the colonial Richard. But he sits in the same parish as the A(1603) baptism — the
closest age match in the entire corpus to "aged 50 or thereabouts" — and he shows that parish's
Gurney households were still actively baptising through the 1620s.

## Bedfordshire is a materially unworked county

The Bedfordshire Baptisms set returns **141 Gurney-variant baptisms for 1605–1645 alone**, with
father and mother columns and a high proportion flagged *Exclusive*.[^beds] The file's Bedfordshire
coverage to date is three parishes — Toddington, Lidlington and Houghton Regis — each reached because
a Gurney happened to surface there. The first page alone adds households at **Hockliffe, Luton,
Clapham, Leighton Buzzard and Houghton Regis**:

```
1609  Edmond / Edmund Gurnet   father Rose / Rise      Leighton Buzzard, All Saints
1612  [child]                  father Edward           Houghton Regis
1616  Alice Gurney             father Robert           Clapham, St Thomas a Becket
1619  Alice Gurney             father Thomas           Hockliffe, St Nicholas
1625  Anne Gurney              father Thomas           Toddington
1628  Ann / Anne Gurney        father John             Toddington, St George of England
1630  John Gernne or Gurney    father Thomas           Toddington
1634  Audrey Gurney            father John             Toddington, St George of England
1636  Alice Gurney             father Edward, mother Sibell    Luton, St Mary
1642  Daniel Gurney            father Henry, mother Elizabeth  Luton, St Mary
```

**The Hockliffe household is now register-attested** — Alice, daughter of Thomas, 1619 — which
independently corroborates the Elizabethan Court of Requests suit over *lands in Hockliffe* brought
by a Robert Gurney, and confirms Hockliffe as a genuine Gurney seat rather than a single later
butcher.[^hockliffe] Hockliffe is five miles from Cheddington and Edlesborough. The county sits
directly between the Aylesbury Vale cluster and the Toddington households, and it has never been
swept as a county.

## What is done and what is not

**Done:** all five children — Mary, Richard, John, Peter, Isaac — swept England-wide, surname
wildcarded, no parent constraint, across every parish-baptism collection on FindMyPast, with fathers
read from the county sets for every named hit. The Stewkley correction. A first page of Bedfordshire.

**Not done, and it should not be reported as done:** **Sarah** (deliberately deferred — she has no
primary record of any kind, so a baptism sweep for her has nothing to confirm against); the **Luton
1635 Richard's** father; the remaining seven pages of Bedfordshire; and the equivalent runs on
**Ancestry and FamilySearch**, which index different transcriptions again and will hold rows
FindMyPast does not. The Peter and Isaac zeros are FindMyPast zeros until those are run.

## Method notes worth keeping

- **`fathersfirstname` does not bind on the Bedfordshire baptisms URL either**, returning the
  identical 141 rows with and without it. The failure is not specific to the Norfolk set; assume no
  parent-forename URL parameter binds on any FindMyPast baptism dataset, and read the Father column
  instead.
- **`location=` does not bind on the cross-collection search** — a Stewkley-scoped query returned
  73,877 unfiltered rows. Location has to come from the field's autocomplete.
- **Cross-collection results carry no parent columns.** The workflow is therefore *locate* on the
  cross-collection search, then *drill* into the named record set with `datasetname=` to read Father
  and Mother.
- **The cross-collection view paginates** where the single-dataset view does not — the numbered pager
  renders and works, which is the opposite of the documented `datasetname` behaviour.

## Crosslinks

- [`60-refactor-matching-by-family-not-by-man.md`](60-refactor-matching-by-family-not-by-man.md) — the marriage half, settled; this is the baptism half
- [`52-refactor-bucks-herts-elimination.md`](52-refactor-bucks-herts-elimination.md) — the Stewkley statement corrected here
- [`57-refactor-colonial-attributes-audit.md`](57-refactor-colonial-attributes-audit.md) — how solid each child's name and date is
- [`59-refactor-open-actions.md`](59-refactor-open-actions.md) — open actions arising
- Graph tracker: [`sources/intake/g13-graph-breadcrumb.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/intake/g13-graph-breadcrumb.md)

[^xcoll]: FindMyPast cross-collection search, authenticated session, 28 July 2026. Working URL form: `https://www.findmypast.co.uk/search/results?sourcecategory=life%20events%20(bmds)&firstname=<name>&lastname=<name>&yearofbirth=<YYYY>&yearofbirth_offset=<N>&sourcecountry=great%20britain&collection=parish%20baptisms&sid=999`. Note `sid=999` and the absence of `datasetname`. The left-hand facet panel gives live counts per category (Parish Baptisms / Parish Burials / Parish Marriages / Wills & Probate), which is itself a fast way to size a surname across record classes.
[^mary]: Same instrument, 28 July 2026. `firstname=mary&lastname=gurney&yearofbirth=1629&yearofbirth_offset=5` returns **six** rows: London 1624; Norwich St Giles 1625 (two rows, Norfolk Baptisms); Kelham, Nottinghamshire 1630; Linslade, Buckinghamshire 1633; Holborn, London 1634. The same query with `lastname=gurn*` returns **seventeen**, adding Gurnard (Bishop's Stortford, Hertfordshire 1629, two sets), Gurnel (London 1627), Gurner (Eythorne, Kent 1633, four rows), Gurnett (Holborn 1634), Gurnte (Eythorne 1633, two rows) and **Gurny (Hitcham, Buckinghamshire 1631)** — the last being the baptism the case file already carries at §6.1 and §8.7 as Mary Gurny, 22 January 1631, father John. Source IDs: `findmypast-uk-parish-baptisms`; `findmypast-bucks-baptism-index`.
[^sweep]: FindMyPast cross-collection parish-baptism searches, all run 28 July 2026 with `lastname=gurn*`, no parent constraint, `sourcecountry=great britain`, `collection=parish baptisms`, `sid=999`: `firstname=mary&yearofbirth=1629&yearofbirth_offset=5` = 17; `firstname=richard&yearofbirth=1630&yearofbirth_offset=5` = 9; `firstname=john&yearofbirth=1634&yearofbirth_offset=5` = 27; `firstname=peter&yearofbirth=1637&yearofbirth_offset=10` = **0**; `firstname=isaac&yearofbirth=1642&yearofbirth_offset=10` = **0**. Fathers read by drilling into the county sets: *Buckinghamshire Baptism Index* (`lastname=gurn*&firstname=rich*` → Richard, father Robert, Stewkley; `&firstname=john&yearofbirth=1630&yearofbirth_offset=10` → John 1624 father Thomas at Wingrave, John 1637 father Robert mother Sarah at Aston Abbots, two rows) and *Norfolk Baptisms* (`lastname=gurny&firstname=rich*` → Richard Gurny 1630, father William, Norwich St Lawrence, with a twin row at Norwich St John Maddermarket). Source IDs: `findmypast-uk-parish-baptisms`; `findmypast-bucks-baptism-index`; `findmypast-norfolk-baptisms-index`; `findmypast-bedfordshire-baptisms`.
[^baseline]: [`research/case-files/john-gurney-case-file-v5.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/john-gurney-case-file-v5.md) §1 baseline table, "Children (born in England): Sarah (b unknown), Mary (bc.1628), Richard (bc.1630), John Jr. (bc.1633), Peter (bc.1635-40) + potentially Isaac (uncertain)". Cross-reference, not a source. The colonial first appearances are Bodge, *Soldiers in King Philip's War*, p. 114 ("Peeter Gurnay", Weymouth, Dedham muster 10 December 1675) and the Plymouth Colony court order of 1 March 1663/4 for Isacke Gurney. Source IDs: `bodge-soldiers-king-philips-war-1891`; `familysearch-fulltext-search`.
[^unit54]: [`54-refactor-naming-convention-and-the-cheddington-household.md`](54-refactor-naming-convention-and-the-cheddington-household.md) §"What the search found". Cross-reference, not a source.
[^chedd]: Ancestry.com, "England, Select Births and Christenings, 1538–1975" (collection 9841), searched 28 July 2026: John Gurney, baptism 14 December 1634, Cheddington, Buckinghamshire, relatives **Isaac** and **Martha**; with Ann Jane Gurney, 3 March 1636, same parish and parents. The 1634 baptism is absent from the *Buckinghamshire Baptism Index*, which carries only three John Gurn\* rows for 1620–1640 (Wingrave 1624, Aston Abbots 1637 ×2) — a further instance of one county transcription missing what the national sets hold. Source IDs: `ancestry-england-select-births-christenings-9841`; `findmypast-bucks-baptism-index`.
[^unit52]: [`52-refactor-bucks-herts-elimination.md`](52-refactor-bucks-herts-elimination.md) §"The Buckinghamshire probate tier", and case file §8.6. Cross-reference, not a source.
[^beds]: FindMyPast, *Bedfordshire Baptisms*, `datasetname=bedfordshire+baptisms&sid=103&lastname=gurn*&yearofbirth=1625&yearofbirth_offset=20`: 141 rows across 1605–1645, read at first page. Source ID: `findmypast-bedfordshire-baptisms`.
[^hockliffe]: The National Archives, Kew, REQ 2/27/189 and REQ 2/158/97 (1590), "Gurney v Saunders. Plaintiffs: Robert Gurney. Defendants: William Saunders. Subject: lands in Hockliffe. County: Bedfordshire"; with the Bedfordshire assize files of 1671–81 recording John Gurney of Hockliffe, butcher, and his son William. The 1619 baptism is FindMyPast, *Bedfordshire Baptisms*: Alice Gurney, 1619, father Thomas, Hockliffe, St Nicholas. Source IDs: `tna-discovery-catalogue`; `findmypast-bedfordshire-baptisms`.
