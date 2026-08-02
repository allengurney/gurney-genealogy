# Research dump — 2026-07-31 FMP-expiry campaign

**Status:** active research record. Findings are not yet promoted to research companions, place files, or fact sheets.

**Scope and method.** This campaign starts with the live lead catalog and concentrates on work for which an authenticated Findmypast session provides an irreplaceable or materially better route. Each lead was grounded with `research_leads.py context`, `repo_search.py`, its named research unit, the existing child-record catalog, and `data/search-variants.json` before the live search. Searches used the three Findmypast modes deliberately: parent search (`sid=102`) to find households, county sets for parent columns and images, and individual transcripts for the exact fields. An index result is recorded as an index result; it is not silently promoted to an image reading.

**Initial FMP-priority queue.** The rank combines catalog priority with direct dependence on Findmypast collections, exclusive rows, image browse, or the FMP parent-search instrument: L-282 (95), L-283 (94), L-291 (92), L-292 (92), L-285 (88), L-293 (86), L-294 (84), L-297 (76), L-296 (74), L-300 (70), L-298 (68), L-303 (64), L-330 (60), L-255/L-257/L-314 (55), and L-324 (46). The first two were begun because they are respectively the highest-value national FMP instrument and a single, potentially decisive FMP/Bucks image target.

## 1. L-282 — England-wide burial-arm parent search: one new Norwich household record, no departure conclusion

### Objective

Test the method question: which father-John-Gurney household appears in the baptism arm but not the burial arm during the migration window? This is a **household-comparison** test, not a search for every person called John Gurney.

### Live FMP evidence

The strict and variant-expanded parent-burial searches were run with `sid=102`, `collection=parish burials`, `fatherfirstname=john`, `fatherlastname=gurney`, `yearofbirth=1630`, and `yearofbirth_offset=5`. The strict query displayed 41 rows; adding the provider's father-name and father-surname variant flags displayed 76. **Those counts are only an exploratory discoverability observation, not a date-bounded result set:** the later instrument check in section 16 establishes that this parameter admits burials with blank birth fields and event dates far outside the nominal range. The substantive record below was retained after transcript-level inspection, not inferred from a valid 1625–1635 comparison:

> **John Gurny**, burial 10 February 1639, St Peter Mancroft, Norwich, Norfolk; father **John Gurny**; mother **“Marg.”**; *England Deaths & Burials 1538–1991*.

Human transcript URL: <https://www.findmypast.co.uk/transcript?id=R_272863566>.

The transcript’s explicit fields are important: the deceased is a child named John, not the father; the father is John Gurny; and the mother is only abbreviated `Marg.`. It therefore cannot be the colonial adult John Gurney’s own burial, and it does not establish that this English father is the colonial John. It is a new family-level record worth retaining because it sits inside the correct broad time/place corridor and carries a real parent pair.

### Deliberate pivots and bounds

1. An exact-`Gurny` parent-baptism search (`sid=102`, father John Gurny, 1630 ±10) produced three baptisms only: Mary at Hitcham (1631), Sara at Berkhamsted (1634), and Alece at Longdon-by-Upton-on-Severn (1641). It produced no Norwich baptism. This is **not** a negative for the Norwich household: the national parent pool is known not to reach every county set.
2. The single-dataset *Norfolk Baptisms* search for `Gurny` returned nine rows. Its early Norwich entries are Richard Gurny, son of William, in 1630 at St Lawrence and St John Maddermarket; it contains no John-and-Margaret household and no St Peter Mancroft event. Again, that set’s selective coverage prevents a household-negative conclusion.
3. The existing `coverage/child-record-catalog.csv` has no 1639 John Gurny burial, no St Peter Mancroft record, and no transcript ID `R_272863566`. It does already hold the nearby 1630 Norwich Richard Gurny as a **William**-father household, so the new record must not be merged with it merely because both are Norwich Gurnys.

### Current result

The live FMP search has added a traceable **Norwich John Gurny × Marg. child-burial record** and shown that the L-282 parent-search method can surface a household the prior catalog did not contain. It has **not** yet performed the full baptism-arm/burial-arm household comparison, nor established a connection to John Gurney of Weymouth/Braintree. Keep L-282 partial. The next bounded step is to catalogue this record as a separate provisional household, then pair the national result with the relevant Norwich county/parish instruments and image coverage rather than treating the absence of a FMP baptism row as a result.

Source tracking: this is a short indexed transcript, not a corpus extract. Before promotion, recheck the source registry for the appropriate Findmypast death/burial source object; no new source object is warranted merely to preserve this dump-stage result.

## 2. L-283 — Stewkley, 21 September 1615: the index confirms the target but does not decide elder versus son

### Live FMP evidence

The unbounded, event-year-sorted *Buckinghamshire Burial Index* search returns the expected entry:

> **John Gurney**, buried 21 September 1615, Stewkley, Buckinghamshire; archive reference **D/A/T/160**; document type **Bishop’s transcripts**; no age, relationship, residence, or image supplied.

Human transcript URL: <https://www.findmypast.co.uk/transcript?id=GBPRS%2FBUCKINGHAMSHIRE%2FBUR%2F000386897>.

The FMP transcript independently confirms the existing catalog row CR-170. Its related-record panel offers 1602 and 1611 baptism records for men named John Gurney, but that is a name-level association generated by the provider, not proof that either was the deceased man.

### Important query defect, reproduced in this live session

The seemingly exact query `datasetname=buckinghamshire+burial+index&sid=103&lastname=gurney&firstname=john&year=1615` returned **zero**. Removing `year=1615`, retaining the names, and sorting ascending exposes the 1615 Stewkley entry. In this dataset, the visible generic `Year` query parameter fails closed for this event. Do not use it to exclude a record; either search unbounded and read/sort the results, or use a source-specific bound that has a positive control.

### Current result

The target index event and its bishop’s-transcript provenance are firmly re-verified, but FMP provides no image and no discriminating language. The actual unresolved question remains exactly the old one: does the original entry say “elder,” “younger,” “son of,” or nothing? It cannot be resolved by probability, nearby burials, or the provider’s related-record suggestions.

The archive route is now more specific. The [FamilySearch Catalog entry 760791](https://www.familysearch.org/en/search/catalog/760791) describes **Bishop's transcripts for Stewkley, 1575–1835** and explicitly includes burial coverage for 1607–1618, the interval containing 21 September 1615; its online catalog page requires sign-in before image access. Buckinghamshire Council states that Buckinghamshire Archives holds baptism, marriage, and burial registers from most county parish churches and provides a [parish-register-entry request route](https://www.buckinghamshire.gov.uk/schools-libraries-and-parks/archives/discover-your-family-history/). These are two routes to the primary wording, not independent evidence of what the entry says.

Keep L-283 partial and prioritize one retained image or archive-supplied copy of **D/A/T/160** before any candidate probability change. No new corpus extract is appropriate yet: the retained evidence is an indexed one-line record, already covered by the existing `findmypast-bucks-burial-index` source tracking.

## 3. Re-ranked active work after the Essex and county-set checks

1. **L-285 (P88):** the FMP *Hertfordshire Burials* collection explicitly supplies both its transcript and the register image, and includes Berkhamsted from 1538. The 28 June 1638 Richard Gurney image is consequently the highest-value genuinely FMP-accessible item now that the higher-ranked parent and Bucks checks have been advanced.
2. **L-293 (P86):** wildcard Mary/Richard/John on the remaining independent instruments, preserving parent columns and positive controls.
3. **L-294 (P84):** national-set and Worcestershire work; it remains materially advantaged by FMP but is not an image discriminator as direct as L-285.
4. **L-292 (P92, already substantially worked):** do not repeat the completed eight-county sweep. Its FMP residue is specifically Berkshire marriages and the capped high-noise result pages; those are bounded follow-up work, not an open England-wide rerun.
5. **L-291 (P92 overall, but not FMP-image dependent):** FMP's *Essex Baptisms* page describes this collection as transcripts created from original registers. The provider lists Epping Upland among its parish coverage, but it does not promise a register image for this collection. The actual image route is Essex Archives Online/ERO: the archive states that it has digitised all parish registers and that subscription access exposes the full-size images. Treat this as a high-value **ERO image** task, not as a reason to consume remaining FMP time.

## 4. Promotion constraints

- Add the Norwich record only as a distinct, low-to-moderate-weight provisional household in the child-record catalog; preserve the exact indexed surname `Gurny`, `Marg.` abbreviation, transcript URL, collection, and search date.
- Do not add it to a published narrative or use it to alter the G13 identity probabilities without a household-level comparison and at least one independent witness.

## 5. L-291 — Essex source geometry corrected; image target remains unexamined

### Finding

The previous priority wording overstated Findmypast's role. Findmypast's public description of *Essex Baptisms* says the collection contains **transcripts created from original parish registers** and reports that it can provide baptism date/place and parent names. Its 2021 release note confirms that *Epping Upland, All Saints* is among the collection's added parish coverage. That supports the existing indexed corpus, including Richard Gurnat, 1616, father John; it does **not** establish that an FMP register image is available to read.

The original-register route is distinct. The Essex Record Office states that it holds the parish registers and that all its parish registers have been digitised. Essex Archives Online says a subscription permits full-size images of almost all its Anglican parish registers and describes direct image navigation. This is the right source for the questions that the FMP transcript cannot answer: the hand's surname reading, Richard's omitted mother, and whether the Epping register covers 1600–1610.

### Evidence already established

- The existing FMP/Essex-FHS transcription run is still the correct index evidence: `lastname=gurn*&keywords=epping`, unbounded, produced 28 provider results but only 14 events because every Epping event is indexed twice, as Epping and Epping Upland. The seventeenth-century sequence is Richard Gurnat 1616 (father John); John Gurne 1622 (father Robert, mother Sara); Richard Gurnet 1649 (father Richard); John Gurnet 1654 (father John); Elisabeth Gurnet 1659 (father John, mother Anne). The index cannot establish a pre-1616 absence because a year bound plus a place keyword has been proven to fail closed in this exact set.
- ERO target references already preserved by the research layer are **D/P 32/1** for Epping and **D/P 61/1** for North Weald Bassett. The image reading should cover Epping 1590–1620 first, then the 1616, 1622, and 1625 entries side-by-side; North Weald is a comparison household, not a substitute for the Epping question.
- No historical conclusion changes. The Epping line remains a 3% untested candidate because the alternation John → Richard (1616), Richard → Richard (1649), John → John (1654) is suggestive but does not identify a family without the manuscript record.

### Source and access boundary

Public source descriptions checked 31 July 2026:

- Findmypast, [Essex Baptisms](https://www.findmypast.co.uk/discover/birth-marriage-death-and-parish-records/parish-baptisms/essex-baptisms) (public collection description; searchable page returned HTTP 403 to non-authenticated retrieval).
- Findmypast, [Epping Upland added to Essex Baptisms](https://www.findmypast.co.uk/blog/new/essex-kent-parish-records).
- Essex Record Office, [Archive collections](https://www.essexrecordoffice.co.uk/research/our-collections/archive-collections/) (states all parish registers digitised).
- Essex Archives Online, [Understanding parish registers](https://www.essexarchivesonline.co.uk/getpage.aspx?id=113) (subscription image access and navigation).

L-291 is advanced to **Partial** because the source route and its exact evidence boundary are now corrected.

## 6. L-292 — county-set phase verified as complete; bounded FMP residue remains

The lead's central premise is now historical rather than current: the parent-search pool is indeed only a floor, but the required pairing work has already been done. The retained 29 July ledger records **705 captured rows** from eight FMP county sets, against `gurn*`, `gourn*`, `gorn*`, `gern*`, `girn*`, and `garn*`; 68 in-window rows carry a father. It found no father-John/mother-Margaret household at any date and no father-John/mother-Mary household in the window beyond the national pool. Its father-John rows include the known Earsham and Epping records, confirming the county sets supply material the pool misses.

This does not justify closure. The ledger states the remaining coverage limits precisely: no FMP marriage set for Essex, Middlesex, or Huntingdonshire; no Huntingdonshire baptism set; no Suffolk baptism set in this set family; Berkshire marriages not attempted; and high-noise pages capped for several stems. It also preserves the critical methodological defect: place keyword plus year bound fails closed in `sid=103`, so the capped-result residue needs selective page work, not a superficially tidy year-filter rerun. L-292 is advanced to **Partial** and is deprioritised below image work because its large enumeration has already occurred.

## 7. L-285 — FMP image target: no defensible relationship reading yet

Findmypast's current public description of *Hertfordshire Burials* says that **each record includes an image of the register book and a transcript**. Its parish-list search result lists **Berkhamstead, 1538–1865**, encompassing the 28 June 1638 burial. The collection's public search results also expose a distinct *Hertfordshire, Parish Registers Browse, 1538–1988* set. This independently confirms that L-285 is a genuine FMP image task, rather than an index-only request like the 1615 Stewkley bishop's-transcript lead.

The decisive target is Findmypast transcript `GBPRS/D/72723126`: Richard Gurney, buried at Berkhamstead, 28 June 1638. Its linked register image is page 165 of 175 in the browse run, with stable record URL <https://search.findmypast.co.uk/record?id=GBPRS%2FHERT%2F007567815%2F00277&parentid=GBPRS%2FD%2F72723126>. **No source master was downloaded, retained in media, or processed through the paleography workflow before an earlier viewer-based assertion assigned Richard to Thomas Gurney. That assertion is withdrawn.** The current evidence permits only the existing index facts: Richard Gurney was buried at Berkhamstead on 28 June 1638, while two locally baptised Richard candidates remain (1626 to John; 1635 to Thomas). No parentage, candidate-score change, or correction to the current companion follows until a retained master supports two independent readings.

The same collection is not uniformly available from a direct browse URL: an attempt to open adjacent image page 164 redirected to the provider's subscription route. That is a source-access boundary, not evidence about the entries on that page. It leaves the 1637–1643 neighbouring-burial attributions unread and prevents treating the one successful Richard image as a complete image-run review.

Public source checked 31 July 2026: Findmypast, [Hertfordshire Burials](https://www.findmypast.co.uk/discover/birth-marriage-death-and-parish-records/parish-burials/hertfordshire-burials); [Hertfordshire parish-list search result](https://www.findmypast.co.uk/search/historical-records?location=hertfordshire&order_by=relevance&order_direction=desc&page=1&region=world).

## 8. L-293 — FMP wildcard arm was already completed; only Ancestry and FamilySearch remain

### Correction to the lead's active scope

L-293 should not consume remaining Findmypast time. Its source unit records the FMP arm as complete: every one of the five child names was searched across Great Britain parish baptisms with a surname wildcard and no parent constraint, then positive hits were drilled into county sets for parent columns. The active remainder is the same wildcarded run on **Ancestry collection 9841** and **FamilySearch**, which are independent transcriptions; it is not a repeat FMP search.

### Completed FMP result retained from the source unit

| Child | FMP search window | Results | Consequence |
|---|---:|---:|---|
| Mary | 1624–1634 | 17 | The only father-John candidate hit is Hitcham, Buckinghamshire, Mary Gurny 1631; her mother is unindexed. |
| Richard | 1625–1635 | 9 | No father-John/mother-Mary household identified. |
| John | 1629–1639 | 27 | No father-John/mother-Mary household identified. |
| Peter | 1627–1647 | 0 | A Findmypast-only zero until the independent instruments are run. |
| Isaac | 1632–1652 | 0 | A Findmypast-only zero until the independent instruments are run. |

The exact control demonstrates why this run matters: `firstname=mary&lastname=gurney&yearofbirth=1629&yearofbirth_offset=5` yielded six records, whereas `lastname=gurn*` yielded seventeen and recovered the already-known **Mary Gurny, Hitcham, 1631**, which an exact surname misses. The query therefore proves the earlier exact totals were floors; it does not prove the FMP result is exhaustive across all instruments.

The remaining issue is also narrower than the lead text implies. FMP's search has already handled `Mary`, `Richard`, `John`, `Peter`, and `Isaac`; Sarah was deliberately deferred because she has no primary date against which to bound a baptism search. Ancestry and FamilySearch must be run with the same child-name variants and record-set-specific positive controls. L-293 is advanced to **Partial**.

## 9. L-294 — Upton is a national-index household-assembly task, not a Worcestershire county-set task

The FMP national cross-collection search already returns **118** `gurn*` parish-baptism rows under `keywords=severn`; almost all are at Upton upon Severn or Longdon by Upton upon Severn and span from Annes Gurney in 1582 into the later nineteenth century. That establishes a continuous local presence and makes the 1629 Mary row a household-assembly question rather than an isolated father-John/mother-Mary hit.

The county-set route has a tested coverage failure: *Worcestershire Baptisms*, `lastname=smith&keywords=upton`, returns zero. It cannot be used as either a positive or a negative witness for Upton. The open work is to enumerate the **1620s–1640s national-set Upton/Longdon rows**, record each displayed parent/relative field and collection, then compare the 1629 Mary index date (7 September in the prior matrix; 13 September in Ancestry) to the relevant register/archival image. The source unit already cautions that a parish with surname continuity should be downgraded, not silently eliminated. L-294 is advanced to **Partial** because the correct collection, coverage boundary, and local-continuity context are now explicit.

## 10. Revised FMP-expiry order after repository and provider verification

1. **L-285 (P88)** — the 28 June 1638 Berkhamsted image is a confirmed FMP image and could decisively identify Richard's father.
2. **L-282 (P95)** — finish the already-started burial-arm parent sweep and compare household baptism and burial arms; it is a genuinely FMP-specific discovery instrument.
3. **L-300 (P70)** — run the completely unattempted Berkshire marriages set, then retrieve the missing rows from the five specifically capped parent-search years: 1627 (one row), 1628 (seven), 1633 (one), 1634 (five), and 1637 (three). Do not use `page=2`, which is known broken in that mode; narrow by a second controlled axis or inspect a supported result-navigation route.
4. **L-296 (P74)** — Bedfordshire Baptisms has 141 Gurney-variant rows for 1605–1645 but only the first page was read. Continue through the remaining pages and then pair baptisms with burials and marriages. Its known first-page households include Hockliffe, Luton, Clapham, Leighton Buzzard, and Houghton Regis; read parent columns rather than relying on URL parent fields, which are known not to bind.
5. **L-294 (P84)** — assemble the 1620s–1640s Upton national rows and identify the 1629 Mary entry's collection/parent context.
6. **L-297 (P76)** — audit existing database-negative claims against the named four axes only after the decisive image and gap searches above; it is necessary control work but lower immediate discovery yield.

L-291 is no longer in this FMP-specific sequence because its decisive resource is ERO, L-283 needs a Bucks original/browse rather than the index transcript, L-292 is largely completed, and L-293's FMP arm is complete.

## 11. L-300 — Berkshire Marriages Index completed

Objective: test the previously unsearched FMP *Berkshire Marriages Index* for conservative-to-broad `Gurn*` surname renderings, then inspect the pre-departure period rather than treating an exact `Gurney` search as exhaustive. The set says it consists primarily of transcripts made from original parish registers and bishops' transcripts held by Berkshire Archives and The National Archives; only some Phillimore entries carry images. It therefore supplies useful named-couple evidence but does not itself prove an identity without following the register or a linked household.

Live Findmypast search executed:

```
datasetname=berkshire marriages index
lastname=gurn*
sourcecategory=life events (bmds)
sourcecountry=great britain
sort=eventyear ascending
```

The unbounded wildcard result set contained **88** rows. Sorting chronologically gave these only relevant 1600–1649 rows:

| Date | Indexed party | Parish | FMP transcript ID | Reading |
|---|---|---|---|---|
| 18 Jun 1616 | Johannis Gurney / Marie Tow | St Michael, Bray, Berkshire | `GBPRS/M/251030761/1` | Direct FMP transcript reads: by banns; no birth year or marital status. A groom already marrying in 1616 cannot be the colonial John born c. 1605; it is, at most, a possible older generation or separate Berkshire line. |
| 1616 (duplicate rendering) | Gurnet Johnnis | Bray | `GBPRS/BERKSHIRE/MAR/000244840/1` | Same couple/event under a source-specific surname rendering; do not count as an independent marriage. |
| 1643 | John Gurney | Winkfield, Berkshire | `GBPRS/M/251341139/1` | After the colonial John was already established in New England, so it does not answer his pre-departure marriage/origin question. It remains a distinct local line until a register image or household work says otherwise. |

The index also showed 1601 Elizabeth Gurne at Wokingham and 1579 Rychard Gurner at Binfield, which demonstrate why the wildcard was necessary but do not produce a 1620s–1630s parent-pair candidate. No Gurn*/Gurney Berkshire marriage was indexed in 1617–1642, including the likely c. 1625–1635 union window. This is a **set-specific index result only**: it should not be promoted to a countywide negative because FMP's coverage is collection-bound and the surviving record may be outside the indexed parishes or under a still more remote rendering.

The broad `yearofmarriage=1600&yearofmarriage_offset=50` URL did **not** retain the offset in the FMP record-set view; it behaved as a 1600-only query and returned zero. The unbounded, chronologically sorted wildcard result is the valid coverage check here.

L-300 has been changed from **Open** to **Partial**. Its Berkshire-marriage component is complete. Its still-open component is the five specifically capped parent-baptism result slices: 1627 (one omitted row), 1628 (seven), 1633 (one), 1634 (five), and 1637 (three). Those are index-completeness work and remain worth doing, but they are no longer conflated with unsearched Berkshire marriages.

## 12. L-296 — Bedfordshire pivot: narrowed John-father households and a new Eaton Bray candidate

The original July count of 141 Bedfordshire Gurney-variant baptisms cannot be repeated verbatim from the current FMP interface: the same broad national-set query now returns **227** rows. This is a material database/index behavior change, not an increase that should be read as 86 newly discovered events. The valid current result is a focused household screen:

```
collection=parish baptisms
fatherfirstname=john (variants enabled)
fatherlastname=gurn*
keywordsplace=bedfordshire
yearofbirth=1605; offset=40
sid=999
```

That returned **15 baptism rows**, one visible result page. It includes several duplicate or near-duplicate index renderings and also events outside the nominal 1605–1645 window (1592, 1594, 1596, 1599). Thus FMP's birth-year plus offset needs to be treated as ranking/recall assistance, not a hard date filter, and every conclusion below is based on the displayed event dates.

### New candidate: Eaton Bray

`R_951758452`, *Bedfordshire Baptisms*, is a free visible FMP transcript:

| Field | Value |
|---|---|
| Child | John Gurney |
| Baptism | 26 Sep 1606 |
| Parish | Eaton Bray, Bedfordshire |
| Father | John Gurney |
| Mother | not named in the transcript |

This is an **unresolved candidate**, not a proposed identity. Its 1606 date is chronologically compatible with the colonial John's approximate age; Eaton Bray is also geographically adjacent to the existing Bucks/Cheddington field. Nothing yet links this baptised child to a 1620s marriage, Mary, tailoring, a departure, or New England. The next correct move is to reconstruct the Eaton Bray father John household (siblings, marriage, burial/probate, and any later John), then test the 1606 son against the English 1637–1661 exclusion rule.

### Bedfordshire adult-John marriage screen

The related FMP parish-marriage search for `firstname=john`, `lastname=gurn*`, Bedfordshire, with 1625 and 15-year offset produced four index rows:

| Year | Parish | Transcript ID | Meaning |
|---|---|---|---|
| 1624 | Toddington, St George | `XAUTO/FHS/BEDFORDSHIRE/MAR/00004507/1` | locked behind FMP's upgrade screen; spouse and image remain unread. |
| 1624 | Toddington (duplicate spelling `Gurnye`) | `R_843282649` | probably the same marriage/event, but must be compared once accessible. |
| 1639 | Luton, St Mary | `XAUTO/FHS/BEDFORDSHIRE/MAR/00041738/1` | after the likely 1637–1641 crossing window; separately identifiable English John. |
| 1640 | Houghton Regis | `R_857639514` | likewise post-dates the possible departure window. |

The focused baptism screen attaches a John Gurney father to Toddington baptisms of Elizabeth (1625), Anne (1628; two index representations), Audrey (1634), and William (1637). The marriage index's John Gurney at Toddington in 1624 is therefore a strong **household-level lead for an English John fathering through 1637**, but its spouse and exact linkage cannot yet be asserted because the underlying marriage transcript is locked and the baptism entries do not name a mother. It should be checked before turning the adjacency into an elimination.

Other focused-screen anchors: a John Gurney father appears with Isaac (1594), John (1592), and Thomas (1596) at Leighton Buzzard; with Alice (1599) and Marey (1596) at Houghton Regis; with John (1621) at Tilsworth; with John (1640) and Edward (1643) at Luton. These are separate potential households until their transcripts and register context are read. The result set is small enough to finish, but L-296 is not yet a county sweep: 227 broad rows, all remaining parent forenames, the burial set, and the marriage set still need a careful parish/household reconstruction.

L-296 has been changed from **Open** to **Partial**. The immediate high-value sublead is now the free Eaton Bray 1606 baptism, followed by the currently locked 1624 Toddington marriage and Toddington child set.

## 14. Correction to Toddington inference; L-300 page-two recovery tested successfully

### Toddington: what is and is not now proved

The 1624 Toddington marriage has an accessible alternate FMP transcript, `R_857638519`: **Jn Gurney and Eliz Moreton**, married **12 Oct 1624** at Toddington, Bedfordshire. The spelling is `Jn`; the transcript supplies neither ages nor parents.

A separate free National Burial Index transcript, `BMD/NBI/00691020`, records **John Gurney**, buried **23 Sep 1641** at St George, Toddington. Its page suggested records of the same name and locality, including the 1624 marriage, but those “other records featuring that name” links are automatic same-name suggestions—not a relationship assertion. They cannot by themselves join the 1624 groom, the 1641 burial, or every Toddington baptismal father into one man.

This was tested rather than assumed. A focused FMP baptism query for father John Gurn*, mother Eliz*, Toddington, 1624 ±20 returned **zero baptism rows**. That is not an affirmative disproof of the marriage household: the available baptism transcripts often omit the mother, and the geographical filter is proximity-based. It does establish that FMP has not supplied a named John-and-Elizabeth child linkage. The previously observed Toddington baptisms to a father John Gurney (Elizabeth 1625, Anne 1628, Audrey 1634, William 1637) remain a nearby possible household, not attached to Elizabeth Moreton without a record that states the mother or another individualising link.

The focused FMP marriage lookup using `keywordsplace=eaton bray` also returned Houghton Regis 1640–41 entries. Treat `keywordsplace` as a proximity/relevance aid, not as an exact parish constraint. No marriage result currently associates the **Eaton Bray John baptised 1606** with a later English household. He remains an unresolved, chronologically possible candidate, not a preferred identity.

### L-300: two capped yearly result sets recovered through visible FMP pagination

The prior campaign note said `page=2` was broken. That needs refinement: manually constructed second-page navigation was unreliable, but the visible numbered page control works. Each recovery used the page-two link exposed in the result page, not a guessed URL.

Base query: `collection=parish baptisms; sid=102; fatherfirstname=john (variants); fatherlastname=gurney (variants); yearofbirth=<target>; offset=0`.

| Target year | Count | Page-two recovery | Result |
|---|---:|---|---|
| 1628 | 27 | 7 rows retrieved | Most are deliberately broad-variant/field-noise records. One real Gurney-variant result is **Edward Gourney**, baptised **13 Jul 1628**, Aylesbury, father **Jon Gourney**, no mother stated (`R_958482780`). It cannot be assigned to either already-eliminated Aylesbury John without an individualising link. |
| 1634 | 25 | 5 rows retrieved | Gurner Johes, 1634 Bromsgrove; Gourneye Sarah, 1634 Great Berkhamsted; an illegible Guernsey row; Johannes `G.Ontet`, 1635 Warfield; and a Wiltshire initials row. Nothing connects a father John Gurney to Mary/Margaret, the colonial child pattern, or departure. |

The parent-field variant expansion is demonstrably high-noise: it admits records whose child surname is unrelated or nearly illegible because some indexed parent token matches the loose criteria. It is useful for recall but no count may be treated as an identity inference. Every retained candidate needs a transcript-level parent check. The two recovered pages close the pagination gap for 1628 and 1634; they do not turn either annual set into a valid all-spelling/all-parish negative.

The five rows just identified were subsequently recovered in section 15. This paragraph is retained as the pre-recovery state only; it is not current work.

## 13. L-300 — recovery of every explicitly recorded capped parent-search result

The five parent-search result sets described in section 14 were recovered by the visible Findmypast pagination controls, rather than by an inferred URL or a raw endpoint. Each query held the national *Parish Baptisms* collection, a `John Gurney` (variants enabled) father, and the exact target baptism year. The result totals and page-two rows are now fully recorded:

| Baptism year | Total rows | Page-two rows newly checked | Outcome |
|---|---:|---|---|
| 1627 | 21 | 1 — `G J`, Wiltshire Baptisms Index, Broad Hinton, `PRS/WILT/BAPS/BH/0598159` | Initial-only/high-noise index row; no usable Gurney household evidence. |
| 1628 | 27 | 7 — mostly broad-stem or field-noise rows; the only legible near-name was Edward Gourney, bap. 13 July 1628, Aylesbury, father Jon. Gourney, `R_958482780` | No John with mother Mary or Margaret; Edward is not the colonial target. |
| 1633 | 21 | 1 — the same initials-only Broad Hinton row, `PRS/WILT/BAPS/BH/0598159` | No usable Gurney household evidence. |
| 1634 | 25 | 5 — Gurner Johes (Bromsgrove), Gourneye Sarah (Berkhamsted), an illegible Guernsey row, G. Ontet Johannes (Warfield), and a Wiltshire initial row | No John–Mary/Margaret candidate. |
| 1637 | 23 | 3 — two duplicate-like `G? Charles`, 1637 Edinburgh, Scotland Parish Births & Baptisms (`SCOT/OPR/BAP/0548329`; `SCOT/OPR/BAP/4283447`), plus the Broad Hinton initials row | All high-noise/non-target evidence. |

**Result.** The 17 rows omitted by the five first-page caps (1 + 7 + 1 + 5 + 3) have now all been recovered and evaluated. None supplies a baptism or household that weakens the working negative result for a John Gurney born about 1605 to John and Mary/Margaret in the searched English county sets. This is a bounded finding: it says the previously known *parent-search* pagination defect is closed; it does not turn a search index into a proof of absence.

**Important scope correction.** This closes those five parent-search caps only. The historical L-300 account separately says that *nine high-noise county-sweep queries* were capped, principally broad `garn*` stems. Those are not necessarily the same five queries. L-300 must therefore remain **Partial** until the archived sweep ledger identifies and either processes or deliberately re-scopes those nine county-query deficits.

## 14. L-282 — national burial-arm test: instrument correction and a Norfolk household pivot

### 16.1 The proposed date-limited national burial comparison is not valid as written

The L-282 wording called for a national `sid=102` *Parish Burials* query with father `John Gurney` (name variants enabled), 1625–1641, using `yearofbirth=` rather than `year=`. I tested both parameter families directly in the authenticated Findmypast interface.

| Query treatment | Visible Findmypast outcome | Interpretation |
|---|---|---|
| `yearofbirth=1625&yearofbirth_offset=16` with the father-name fields and `collection=parish burials` | **85 results**. The visible result table included events in 1654, 1671, 1714, 1729 and 1734, with blank displayed birth fields. | The chip appears, but the filter admits records without an indexed birth year. It is not a valid 1625–1641 event or child-birth boundary for this burial set. |
| `year=1625&year_offset=16` with the same fields | **0 results**, with the Year chip visibly applied. | Fails closed, as the earlier method note warned. It cannot supply a negative result. |
| Same father-name search with no year filter, sorted by event year ascending | **165 parish-burial results**. | This is the finite, usable national pool. It can be inspected from the beginning through the relevant years, but it is not an automatically date-bounded comparison. |

This changes the method, not the evidence standard. The old formulation—“run both arms over 1625–1641”—cannot be claimed complete from either date parameter. A defensible residual method is to inspect the early event-year segment of the unbounded 165-row burial pool, pair its identifiable households with the baptism inventory, and retain the already documented county-set exclusion (notably the Norfolk baptism set is outside `sid=102`). L-282 remains **Partial** with that corrected scope.

### 16.2 Earliest event-year segment of the unbounded burial pool

The first visible page of the event-year-sorted pool runs from 1549 through 1670. Its only 1625–1641 rows were:

| Event | FMP record | What the transcript shows | Research consequence |
|---|---|---|---|
| 1629, Castle Sowerby with Sebergham, Cumberland — `John G` | `FS/CUMBRIA/3154704/BUR/0227009` | Child John, father indexed only as `John G`; surname indexed only as `G`; no mother; burial date only `? ? 1629`. | High-noise partial-index hit, not usable as a Gurney household. |
| 1639, Norwich, Norfolk — `John Gurny` | `R_272863566` | Already recorded in this campaign: John Gurny, buried 10 February 1639, father John Gurny, mother Marg. | A child, not the emigrant target; retained as a local household fact, not a departure gap. |
| 6 April 1640, Hempnall, Norfolk — `Anna Gurney` | `R_272831910` | Anna Gurney, daughter of **Johannis Gurney**, buried at Hempnall. | New concrete household pivot; see below. |
| 1640, Sussex — `G* John` | `FS/SUSSEX/1465706/BUR/0354374` | Wildcard/initial surname only in the national result table. | High-noise; not a usable Gurney household. |

No additional row in the 1625–1641 slice supplies a John-and-Mary/Margaret household or a plausible candidate for the colonial John. The finding is bounded to the `sid=102` national pool and does not erase its known county coverage limits.

### 16.3 Hempnall: Anna Gurney is a real indexed baptism-and-burial pair, but not yet the target household

The Hempnall burial was pursued through the Norfolk county baptism set, rather than treating the national parent-search result as sufficient.

- `R_272831910`, *England Deaths & Burials 1538–1991*: **Anna Gurney**, female; father **Johannis Gurney**; burial 6 April 1640; Hempnall, Norfolk.
- `GBPRS/NORFOLK/BAP/003025053`, *Norfolk Baptisms*: **Anna Gurney**, 1640, father **Johannes**, mother blank in the index; Hempnall and the Hempnall Group of Parishes. Findmypast exposes the original Norfolk Record Office register page `GBPRS/NORFOLK/PD_436-1/01890` for this entry.
- A surname-plus-place inventory (`lastname=gurney`, variants enabled, Hempnall location) returned 14 rows. In the relevant period it includes only Anna (1640, Johannes, mother blank) and **Elizabeth Gurney** (1641, father John, mother Jane; `GBPRS/NORFOLK/BAP/003025103`). The next closest earlier named children are a separate late-sixteenth-century Gurnie presence: Henricus 1576 (Johanis and Margr), Margaret 1596 (John, mother blank), Susana 1590 (John, mother blank), and others.

The linked record establishes that an original-image route exists, but no source master was retained and no image-content conclusion is used here. The exact Anna line and maternal wording remain untranscribed. Do **not** infer that the nearby 1641 Elizabeth with mother Jane is Anna's sister: the different/blank parent fields leave that unproved. Anna also cannot be promoted as an answer to the colonial-John question merely because her father's Latin forename is Johannes; she is a distinct female child who died in 1640.

### 16.4 L-300 ledger correction and a focused high-noise control

The archived county-sweep `PROGRESS.md` does not support treating “nine capped queries” as a ready-made exhaustive worklist. Its summary says nine high-noise caps, but a row-by-row reconciliation finds **31** query rows whose status field is exactly `CAPPED`: **18 non-`garn*` rows** and **13 `garn*` rows**, across Norfolk, Essex, Northamptonshire, Oxfordshire, Cambridgeshire, Middlesex, Westminster, and Berkshire. The 31 rows report 13,764 raw results, of which 509 first-page/sample rows were retained, leaving a raw-row lower bound of 13,255 unreviewed; 10,044 of those lie in the 13 high-noise `garn*` queries. “Nine” is therefore neither the complete `garn*` count nor a complete CAPPED-query count.

This makes the next FMP work finite and prioritizable rather than falsely small. Start with the seven smallest non-`garn*` tails — Norfolk marriages `gorn*` (8), Essex baptisms `gern*` (14), Norfolk baptisms `gern*` (16), Norfolk baptisms `gorn*` (18), Norfolk marriages `gern*` (19), Northamptonshire baptisms `gurn*` (26), and Essex baptisms `gorn*` (30) — **131 raw result rows** in all. They are the shortest high-recall continuation set and should be read transcript-by-transcript with parent columns preserved. The larger non-`garn*` and all `garn*` tails require an explicitly narrowed surname/place/period plan before enumeration; raw result counts are not distinct people or candidate households.

As a targeted control—not a replacement for that reconciliation—I ran *Norfolk Baptisms*, 1605 ±35, father John, father surname `Garn*` (variants enabled). Findmypast returned **0 results**. This reduces the chance that the extreme Norfolk `garn*` noise conceals a straightforward father-John match in the target birth window, but it is not a comprehensive surname-stem enumeration and is recorded only as a bounded negative.

## 15. L-294 — Upton upon Severn 1629: partial-parent row checked against its immediate parish context

The focused Findmypast national-aggregate query was:

`collection=parish baptisms; lastname=Gurn*` (variants on); keyword `Severn`; `yearofbirth=1630` with ±20; Great Britain; `sid=999`.

It returned four baptism rows, not the 118 all-date surname/place results reported in the original sweep:

| Child | Date/year | Parish | Parents as Findmypast now transcribes | FMP record |
|---|---|---|---|---|
| Margaret Gurney | 1616 | Longdon by Upton on Severn | parent fields not displayed in result row | `R_942363786` |
| Elizabeth Gurney | **24 June 1629** | Upton on Severn | **Francis Gurney and Mary** | `R_960590015` |
| Marye Gurney | **13 September 1629** | Upton on Severn | father `-`; **mother Mary Gurney** | `R_960590641` |
| Alece Gurny | 1641 | Longdon by Upton on Severn | parent fields not displayed in result row | `R_942363765` |

The Marye transcript directly confirms the earlier source description: its father is not merely blank in a results table; the transcript gives father's first and last name as `-`, while it gives mother **Mary Gurney**, baptism date 13 September 1629, Upton on Severn. The revised date must be carried: it differs from the older 7 September matrix reading but matches the prior note that Ancestry gave 13 September.

Elizabeth is the critical contextual comparator. She is an independently transcribed Upton baptism only eleven weeks earlier, with **Francis Gurney** and **Mary** both named. This makes it plausible that Marye could be another child in a Francis-and-Mary household whose father was omitted in a derivative index. It does **not** prove that relationship: the two children need a register-image or archive transcription connection, and no basis exists to substitute John for Francis. On the present evidence Upton remains a continuous local Gurney parish and a low-probability, partially resolved alternative—not a John-and-Mary candidate.

L-294 remains **Partial**. The remaining high-value work is original-register/archival assembly of the 1620s–1640s Upton entries, specifically to test whether Marye's omitted father can be read and whether the Francis-and-Mary household has other linked children.

### 15.1 Upton source-survival and date audit

Worcestershire Archive & Archaeology Service's current parish-register list records **Upton upon Severn, Old Church** baptisms from **1546–1945**, marriages from 1550, and burials from 1551. The 1629 baptism therefore lies within the archive's stated surviving baptism run; this establishes an original-register route, not the contents of any particular entry. The archive's public [parish-register guide](https://www.explorethepast.co.uk/wp-content/uploads/2024/07/Parish-Registers.pdf) should be used to direct an image or copy request.

There is also a contained date conflict requiring correction at the later promotion pass. The directly rechecked Findmypast transcript `R_960590641` displays **Marye Gurney, Upton, 13 September 1629**, mother Mary Gurney, father field blank. Four active G13 research units still repeat the earlier inherited **7 September 1629** index date: `36-other-eliminations.md`, `39-child-inventory-method.md`, `59-refactor-open-actions.md`, and `66-refactor-berkhamsted-burials-and-the-departure-gap.md`. The March matrix is the apparent upstream copy. Until the original register is read, this is a conflict between derivative renderings, not a reason to invent a parentage or declare either day definitive beyond the currently rechecked FMP transcript. The later promotion must replace the stale current-prose date with **13 September 1629 (Findmypast transcript)** and retain the need for original-image verification.

This source-survival result makes L-294 more operationally defined, but it does not make the Worcestershire county set usable: the existing Smith control remains zero for Upton, and that set cannot supply a parish negative.

## 16. L-291 — Epping / North Weald image-work resumption package

No new Epping or North Weald image has been read in this campaign. The precise existing evidence and the remaining delta are recorded here so the next authenticated session starts with the real question rather than re-running the index sweep.

- Findmypast *Essex Baptisms* query already established: `lastname=gurn*&keywords=epping`, **no year bound**, returns 28 rendered rows that are 14 distinct events because each is indexed both as Epping, All Saints and Epping Upland, All Saints.
- The seventeenth-century sequence is: **Richard Gurnat 1616, father John**; John Gurne 1622, father Robert and mother Sara; Richard Gurnet 1649, father Richard; John Gurnet 1654, father John; and Elisabeth/Elizabeth Gurnet 1659, father John and mother Anne. North Weald adds Susan Gurnard 1627 to Robert and Ann.
- The key prediction is not that Richard 1616 is the emigrant John. It is that an original register image might distinguish a true Gurney/Gurnard-family spelling, supply a mother or residence/status detail, and establish whether the adjacent records are one family or several.
- The index cannot settle whether a John born about 1603 is absent. In this set, combining an Epping keyword with `yearofbaptism` fails closed even for a Smith control; the unbounded `sortby=dateasc` parameter is ignored. Therefore no date-plus-place index negative may be used against the line.
- The next image session should read Epping / Epping Upland D/P 32/1 and North Weald Bassett D/P 61/1 around the 1616 Richard and 1622/1625 Robert-and-Sara entries, then compare letterforms and parent wording before altering the present 3% candidate weight.

## 17. Critical adversarial audit of this FMP-expiry campaign

### Audit standard and bottom-line judgment

This review tests the work as if it had been submitted by another researcher seeking to establish the origin of John Gurney of Weymouth, rather than giving it the benefit of its own intentions. It covers the research design, source-model choices, search execution, claims, lead maintenance, and dump quality through the current section. **The earlier audit itself was incomplete: it treated a viewer impression of L-285 as a decisive primary-source reading even though no master had been retained or independently read. That claim is now withdrawn.** The campaign has source-route corrections and bounded index findings, but no new image-derived relationship conclusion. The errors were methodological, not merely stylistic: a date field was trusted before it was controlled; progress in a result set was sometimes presented as progress on an identity question; a viewer impression was treated as a transcription; and stale interim text was left beside later corrections.

### A. Strategy and reasoning: where the work fell short

1. **The campaign initially optimized for Findmypast activity, not for the actual discriminating question.** The useful question is not “what more can FMP return?” but “which action most sharply changes the probability of a specific household?” L-285 should therefore have been first from the outset: one original entry could distinguish two named children if its wording is legible and relationship-bearing. It is now correctly ordered first, but the image has not yet been retained and read to that standard. In contrast, a broad parent-burial sweep could only generate hypotheses unless every source-specific field and coverage boundary had been validated.

2. **The distinction between an index discovery and an identity conclusion was insufficiently enforced.** A mother field, a surname variant, or a same-parish row is not a household reconstruction. The Upton Marye row is a concrete example: it supports a Francis-and-Mary hypothesis more naturally than a John-and-Mary hypothesis, but proves neither. The dump now states that boundary explicitly and does not convert the omitted father into John.

3. **The work inherited, and briefly repeated, a faulty premise that a displayed date chip is a date filter.** In the national burial set, `yearofbirth` is a recall/ranking aid that lets through blank birth fields, while generic `year` fails closed. The original 41/76 counts could never substantiate a 1625–1635 or 1625–1641 household comparison. Section 14 corrects that; section 1 is now explicitly downgraded to an exploratory discovery observation.

4. **A lead status was allowed to signal effort rather than evidence-state.** “Partial” is appropriate only when a defined portion of the evidence question has actually been done. The current statuses are now tied to concrete results: L-285 has a confirmed image route but no retained reading; L-283 has a verified transcript-only boundary; L-282 has a disproved instrument premise; L-296 has a focused screen rather than a county sweep. No lead is claimed closed merely because a query was run.

5. **The campaign did not begin with a rigorous source-characterisation table for every top lead.** That would have separated (a) FMP image-backed registers, (b) FMP derivative indexes, (c) archive-original tasks, and (d) non-FMP archive tasks. The result was wasted narrative around access mechanics and an avoidable delay before the image-backed L-285 record. Those mechanics have been removed from this research dump because they are not genealogy evidence and were not a valid substitute for source analysis.

### B. Discovery and search execution: specific defects and corrections

| Audit finding | Why it matters | Correction made in this round |
|---|---|---|
| National parent-burial date parameters were not positive-controlled before result counts were discussed. | A non-working or leaky filter makes both positive counts and zeroes unfit for chronological inference. | Section 14 records the 85 leaky `yearofbirth` result, the zero `year` result, and the 165-row unbounded pool. L-282 is Partial with a narrower method. |
| A viewer impression of the L-285 register page was reported as a relationship reading without a downloaded master, crop workflow, or blind re-read. | It recreates the exact affirmation-bias failure the project has previously identified: a plausible expected phrase is mistaken for evidence. | The Thomas-son assertion is withdrawn from this dump and L-285. The image must be retained and independently read before any relationship claim. |
| The early L-300 pagination notes were superseded but still read as a live gap. | A reader could believe five page-two rows were missing after they had been retrieved. | The obsolete wording now points to section 13, which records all 17 explicitly identified page-two rows. |
| “Nine capped queries” was treated as a finite backlog even though the retained ledger has more `CAPPED` rows. | It risks an unjustified claim that all high-noise residue has been enumerated. | L-300’s description and section 14 now require ledger reconciliation before any exhaustive statement. |
| Bedfordshire was described from a changed 141/227-result interface as though it were a completed county screen. | The existing evidence is a targeted John-father screen, not a complete baptism/burial/marriage reconstruction. | L-296’s lead description now says exactly that: 15 focused rows, 227 broad rows, and a still-unfinished finite enumeration. |
| The 1615 Stewkley item was framed as an FMP image pull without first checking the actual record affordance. | The FMP transcript does not expose an image; repeating the same route cannot solve the age/relationship ambiguity. | The transcript is now pinned as `GBPRS/BUCKINGHAMSHIRE/BUR/000386897`; the 1602 John is independently pinned as `.../BAP/000880759`; L-283 now directs the question to Buckinghamshire Archives’ original. |
| The Upton date discrepancy was carried as an unresolved inherited difference. | A basic event date must be settled before interpreting the household. | Direct transcript `R_960590641` confirms 13 September 1629, father fields `-`, mother Mary Gurney. The older 7 September matrix value is superseded for future promotion. |
| Place and spelling behavior were sometimes learned after, rather than before, interpreting a search. | Berkhamsted/Berkhamstead and Gurney/Gourney are demonstrated failure modes. | The audit preserves the exact collection-specific place spelling and treats every broad variant query as high recall pending transcript inspection. |

### C. Findings and documentation: what stands, what does not

**L-285 is unresolved.** The earlier viewer-based Thomas-son assertion did not meet source-capture or paleographic standards and is withdrawn. The current research companion and case file correctly preserve the two candidate children and the need for the register image; they must not be changed on the basis of the withdrawn assertion. A later capture must retain the page-165 master, produce reproducible crops, and obtain a blind second reading before it can alter the candidate analysis.

**L-283 remains genuinely unresolved.** The FMP record is precise about date, parish, archive reference, and document class, and imprecise where it matters: it gives no age, relationship, residence, or image. Its surrounding 1614–1618 cluster establishes contemporary Gurney mortality but does not identify John. The 1602 baptism is a real father-John child and makes the “boy or father” fork concrete; chronology alone cannot choose between them.

**L-282’s Norfolk pivot is only a lead, not a recovered household.** The Anna Gurney event adds a father Johannes, but she is a female child who died in 1640. It must not be promoted as evidence about the colonial John or merged with the 1641 Elizabeth merely on parish proximity.

**L-294 has been narrowed rather than solved.** Marye’s mother Mary is genuine in the derivative transcript; Elizabeth’s contemporaneous Francis-and-Mary parentage makes one local household plausible. The source does not name Marye’s father, and the substantial continuous Upton presence makes a departure hypothesis weak. No relationship to the colonial family is claimed.

**No broad negative is complete merely because it was run in FMP.** The FMP national pool omits some county-set material; record sets have different place tokens, index coverage, and displayed field semantics. The dump therefore distinguishes (i) an observed result, (ii) a bounded result-set negative, and (iii) an all-source negative. Only the first two occur here, and only with their stated limitations.

### D. Immediate corrections applied, and residual completeness boundary

- Removed all operational access narrative from this dump. It now contains only genealogical evidence, record routes, method limits, and corrections.
- Rewrote the contradictory L-282 framing; removed stale L-300 “still to recover” wording; renumbered the document after removing the irrelevant access section.
- Withdrew the prior L-285 viewer-based relationship assertion and restored its correct evidence boundary: exact transcript and image route known; no retained master or defensible parentage reading yet.
- Rechecked L-283 in the live FMP collection, captured the exact transcript IDs and the source’s image limitation, and rewrote its lead description so the next researcher does not retry the same non-discriminating route.
- Corrected L-296’s lead description to prevent its focused screen from being mistaken for a county-wide completion.
- Reconfirmed the Upton Marye transcript directly and preserved the date/parent-field wording exactly enough to test against an archival register.
- Recorded the Buckinghamshire Burial Index’s set-specific generic-`year=` failure mode in the Findmypast search skill, so a future zero is not mistaken for an event-year negative.
- Corrected the older Hertfordshire-burials validation note: its 48-result and “only pre-1700 Berkhamsted entries” wording applies to its stated **John-forename** search, not to a complete all-forename parish sweep. The validation now points separately to the later broader Berkhamsted work.

The campaign is **not** an exhaustive Findmypast closeout. The honest remaining boundary is finite but nontrivial: L-285 needs a retained page-165 master and independent paleographic readings; the L-300 archive ledger must be reconciled; county-set and non-FMP coverage gaps remain; L-291 needs the Essex images; L-283 needs the Bucks original; and any household theory generated from high-recall parent searches still needs an original or an independently sourced household assembly. The present dump is intentionally sufficient for a later intake pass to make those promotions and corrections without recreating the research session.

## 18. Source-capture remediation audit — L-285 has not crossed the evidence gate

The media target `sources/media/findmypast-hertfordshire-burials/_local/` exists but contains no master image. The registered `findmypast-hertfordshire-burials` source therefore correctly remains `corpusStatus: none`, `corpusPath: null`, and `mediaPath: null`; no corpus supplement, media README, hash, transcript sidecar, or source-index change may be claimed for the 28 June 1638 entry. The empty target directory is not evidence retention.

When the original page is actually obtained, the promotion gate is all-or-nothing:

1. Retain the unmodified register-page master locally under the existing source ID, with a stable record URL, transcript ID, page number, filename, SHA-256, retrieval date, and rights restriction in `_local/README.md`.
2. Run the paleography workbench on the retained master: metadata inspection, whole-page grid, line-location grid, crop ladder with line strips, enhancement sheet, and manifest. Keep the master, the final inspection sheet, and the manifest; keep derivative crops local.
3. Make two independent line readings before consulting prior expectations or the FMP transcript, then make an adversarial comparison that specifically tests **John**, **Thomas**, a relationship word, and the possibility that no relationship is written. A third check that merely repeats the expected reading does not count.
4. Only if the image supports a stable reading, create a neutral corpus-supplement extract tied to `findmypast-hertfordshire-burials`, update the source registry's corpus/media fields, and preserve the exact image reading separately from any identity inference. The companion and lead can then distinguish what the register says from which baptism candidate it may fit.

The same gate applies to L-283, L-286, L-291, and L-294: an archive route, index transcript, thumbnail, or visual impression is not a downloaded primary source and does not substitute for retained media plus reproducible reading.

## 19. L-294 — Upton cluster extended to a three-generation local sequence

This round rechecked the two 1629 entries already noted above and then tested
the surrounding Upton-on-Severn surname cluster as a structured local sequence,
not as a name-only search. The resulting Findmypast *England Births & Baptisms
1538–1975* window (surname Gurney with variants; Upton on Severn; the interface's
displayed 1595–1645 birth-year window) has seven rows. Four are parish entries
that bear directly on the Gurney cluster:

| FMP transcript | Indexed baptism | Indexed parents | Evidentiary limit |
|---|---|---|---|
| [`R_960587515`](https://www.findmypast.co.uk/transcript?id=R_960587515&tab=this) | **Fraunc. Gurney**, 09 Oct 1597 | Richard Gurney; mother `-` | Derivative index; not a register image. |
| [`R_960589747`](https://www.findmypast.co.uk/transcript?id=R_960589747&tab=this) | **John Gorney**, 13 Jun 1622 | Francis Gorney; mother `-` | Spelling and omitted mother are index fields. |
| [`R_960590015`](https://www.findmypast.co.uk/transcript?id=R_960590015&tab=this) | **Elizabeth Gurney**, 24 Jun 1629 | Francis Gurney and Mary Gurney | Directly establishes those two indexed parents for Elizabeth only. |
| [`R_960590641`](https://www.findmypast.co.uk/transcript?id=R_960590641&tab=this) | **Marye Gurney**, 13 Sep 1629 | father `-`; mother Mary Gurney | Does not identify the omitted father. |

The sequence supplies a materially better explanation for the Marye entry than
the former loose John-and-Mary hypothesis: a Francis recorded at Upton in 1622
and a Francis-and-Mary couple recorded there in June 1629 form a coherent local
context. The 1597 Fraunc. entry to Richard is chronologically compatible with
the same parish line, but the index alone does not prove that its child Francis
is the adult father of the 1622 and 1629 children. Likewise, proximity, a shared
surname, and a shared indexed mother make Marye **compatible with** the
Francis-and-Mary household; they are not evidence that the register named Francis
as Marye's father.

This is a local household reconstruction problem, not a migration identification.
It weakens any attempt to treat Marye as a free-standing John-and-Mary candidate
and reinforces the need to obtain and read the surviving Upton parish-register
entry. The original-record objective is now specific: determine whether Marye's
entry names Francis, another father, or no father, and check whether the 1622 and
1629 entries share wording, residence, or other identifying detail. The source
artifact is retained as
`sources/corpus_supplement/findmypast-upton-gurney-baptisms-1597-1629.md`; it
records only the derivative transcript fields, while this section carries the
inference boundary.

## 20. L-296 — Eaton Bray controlled three-record-class review: a real early Gurney pocket, but no reconstructed 1606 household

This round treated the 26 September 1606 Eaton Bray baptism as a **candidate
event**, then tested its immediately available parish context across separate
Findmypast baptism, burial, and marriage searches.  The searches used the
cross-collection parish-record mode, `lastname=gurn*`, `keywords=Eaton Bray`,
and event-year ascending sort. `keywords` is a location/relevance term rather
than proof of an exact-parish boundary, so only rows whose displayed location is
Eaton Bray / St Mary the Virgin are used below. The selected results prove that
the index has pre-1607 Eaton Bray coverage, but do not prove uninterrupted
coverage or identify any household from shared surname and parish alone.

### Directly rechecked transcript facts

| FMP transcript | Record class | Indexed event and fields | What it establishes — and what it does not |
|---|---|---|---|
| [`R_857650986`](https://www.findmypast.co.uk/transcript?id=R_857650986) | *Bedfordshire Marriages* | **Richarde Gurney** and **Margaret Sandan**, married **14 Nov 1594**, Eaton Bray, Bedfordshire | A named Gurney–Sandan marriage at the parish. It does not identify the later John Gurney who appears as father in the 1606 baptism. |
| [`R_951759235`](https://www.findmypast.co.uk/transcript?id=R_951759235) | *Bedfordshire Baptisms* | **Thomas Gurney**, baptised **1603**, Eaton Bray; the results row has no parents and the transcript is a derivative index | A second early Gurney child/event. It cannot be attached to Richarde and Margaret, or to the 1606 child's father John, from this index alone. |
| [`R_951758452`](https://www.findmypast.co.uk/transcript?id=R_951758452) | *Bedfordshire Baptisms* | **John Gurney**, baptised **26 Sep 1606**, Eaton Bray; father **John Gurney**; mother `-` | A genuine father-and-son index assertion for this child only. It is chronologically compatible with the colonial John's approximate age, but supplies neither mother nor a later life link. |

The same ascending `gurn*` baptism result has Thomas 1603 and John 1606 as its
only displayed Eaton Bray baptisms before 1704 (each additionally has a
duplicate rendition at St Mary the Virgin). A focused `Father's first
name(s)=John` screen, with the provider's five-mile Eaton Bray proximity
setting visibly retained, produces 19 rows. Of those, the only row before 1805
is the same **John Gurney, 1606, father John** record and its duplicate. Thus
the present index does **not** supply a visible sibling group to the elder John
in that proximity screen. This is a bounded index observation, not a claim that
the parish register contains no siblings: other entries may omit the parent,
use another surname rendering, or sit outside the index coverage/normalisation.

### What the other two record classes change

The sorted marriage result begins with the 1594 Richarde–Margaret Sandan event
and the next displayed Gurney-variant marriage is 1671 at Hockliffe; no
1618–1641 Eaton Bray Gurney marriage appears in this query's early block. The
sorted burial result begins with **Margaret Gurney, 1596**, Eaton Bray / St Mary
the Virgin (`XAUTO/FHS/BEDFORDSHIRE/BUR/00247215`; duplicate National Burial
Index `BMD/NBI/00270045`), with the next displayed Gurney burial in 1717. The
1594 marriage and 1596 burial are plausibly compatible as a short local
Richard-and-Margaret sequence, but the source does not identify that Margaret
as Margaret Sandan, so even that couple-level connection remains unproved.

These results create a useful **source-geometry correction**. Eaton Bray is not
a pure search artefact: the marriage index, baptism index, and burial index each
return an early event at the named parish. But their early Gurney records are
sparse and have missing parent/spouse fields. The 1606 John therefore remains
an unresolved, low-weight Bedfordshire candidate; the review gives no evidence
of his marriage, English children, death, or departure. It does not change the
current identity weighting.

### Next discriminating move

Do not continue paging the 198-row all-date baptism result as if it were a
1603–1645 household file. Obtain the underlying Eaton Bray register or a
reproducible archival image/entry for the 1594 marriage, 1603 Thomas, 1606 John,
and 1596 Margaret; then make a line-by-line household comparison. The decisive
question is whether a primary entry supplies mother, residence, occupation,
witnesses, or a distinct parental wording. Until then, retain the three
transcript facts independently and do not infer that Thomas is John's brother,
that Richard is John's father, or that Margaret Sandan is the 1596 burial.

## 21. L-300 — seven smallest non-`garn*` county-set continuations enumerated; no John-and-Mary/Margaret household recovered

This round completed the recommended first continuation of the reconciled
county-sweep ledger.  It used the page URLs exposed by Findmypast's visible
pagination controls for the seven smallest non-`garn*` CAPPED rows, rather than
guessing or constructing pagination parameters.  The live
result counts were Norfolk Banns and Marriages `gorn*` 26; Essex Baptisms `gern*`
27; Norfolk Baptisms `gern*` 35 and `gorn*` 38; Norfolk Banns and Marriages
`gern*` 31; Northamptonshire Baptisms `gurn*` 46; and Essex Baptisms `gorn*` 49.
That is 252 displayed result-table rows across the seven complete result sets.
It resolves the ledger's **131-row lower-bound continuation** for these seven
queries, while retaining the important distinction that the 131 count was
`total_results − rows_captured`, so it includes rows previously excluded from the
old sample through duplicate handling.  The larger non-`garn*` rows and all
`garn*` rows are still unenumerated.

All observations below are **indexed transcript/table evidence only**.  No
original image was opened for interpretation, downloaded, or retained; no
media, corpus, or source-registry change follows from this round.  The displayed
result tables preserve the event, parent fields where the set indexes them,
place, and transcript ID.  Result counts should not be read as people or as
households.

### Relevant early rows after full pagination

| Collection and stem | Indexed row(s) relevant to the 1600–1645 question | Boundary |
|---|---|---|
| *Norfolk Baptisms*, `gorn*` | Luke **Gornett**, baptised 11 Oct 1606, Great Ryburgh, father John, mother Johan, [`PRS/NORFOLK/AT/BAP/GREAT-RYBURGH/00026`](https://www.findmypast.co.uk/transcript?id=PRS%2FNORFOLK%2FAT%2FBAP%2FGREAT-RYBURGH%2F00026); John **Gorner**, 1616, South Walsham, father John, mother blank, `GBPRS/NORFOLK/BAP/001680765`. | The first has a non-target indexed mother and surname; the second is an earlier child with no indexed mother. Neither identifies the colonial John or a John-and-Mary/Margaret family. |
| *Norfolk Baptisms*, `gern*` | Jane **Gerner**, baptised 17 Aug 1623, Thursford, father John, mother `-`, [`PRS/NORFOLK/AT/BAP/THURSFORD/00048`](https://www.findmypast.co.uk/transcript?id=PRS%2FNORFOLK%2FAT%2FBAP%2FTHURSFORD%2F00048); John **Gerney**, baptised 11 Jul 1635, Earsham, father John, mother not indexed, [`GBPRS/NORFOLK/BAP/003389512`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FNORFOLK%2FBAP%2F003389512). | These are genuine father-John index rows, but neither gives Mary or Margaret.  The 1635 Earsham event does not establish a relationship to the already known 1636/1638 Earsham entries merely through parish and surname proximity. |
| *Essex Baptisms*, `gorn*` | Elizabeth **Gorne**, 1623, Harwich, father John, mother Elizabeth, `GBPRS/ESSEX-BAP/0351821`; Anna **Gornell**, 1652, Matching, father John, mother blank, `XAUTO/FHS/ESSEX/BAP/00037553`. | The named mother is Elizabeth in the 1623 row; the 1652 row is later and motherless. Neither matches the target parent pair. |
| *Northamptonshire Baptisms*, `gurn*` | William **Gurnett**, 1641, Abthorpe, father John, mother blank, `XAUTO/FHS/NORTHAMPTONSHIRE/BAP/00000322`. | A late, motherless father-John row. It is an index lead only, not a reconstructed household. |
| *Norfolk Banns and Marriages*, `gorn*`/`gern*`; *Essex Baptisms*, `gern*` | The fully paginated early rows have other named couples or fathers: for example John Gornie–Margaret (Hempnall, 1575), Agnes Gornor–Josef (Heckingham, 1608), Margaret/Thomas Gernsey (Romford, 1597/1599, father Robert), and Margaret Gerne–Robert (Norwich St Stephen, 1602). | They help expose the index's spelling breadth but give no father-John/mother-Mary-or-Margaret household in the target window. |

### Direct transcript checks

The three linked rows were opened as individual Findmypast transcripts to check
that the table had not collapsed their fields.  The transcript pages confirm the
dates, places, collection names, archive/document classes, and parent fields
printed above: Great Ryburgh is an Archdeacon's Transcript, `AT GREAT RYBURGH`;
Thursford is an Archdeacon's Transcript, `AT THURSFORD`; and Earsham is a parish
register entry, Norfolk Record Office `PD 519/1`.  None supplies an indexed
mother of Mary or Margaret.  This is a transcript check, not a reading of the
linked original record.

### Result and remaining boundary

Across all seven fully paginated result sets, no displayed baptism has a father
John with an indexed mother Mary or Margaret.  That is a useful **bounded
continuation result**, not an England-wide negative and not proof that no such
household existed: Findmypast's county sets vary in coverage and indexing, and
blank parent fields are common.  It also does not convert a Gorn/Gern/Gerney
spelling, a shared parish, or a provider suggestion into an identity claim.

L-300 remains **Partial**.  Its next highest-value FMP work is an explicit,
source-characterized plan for the remaining eleven non-`garn*` CAPPED rows and
the thirteen high-noise `garn*` rows, rather than treating the seven completed
tails as the whole ledger or beginning an unbounded name sweep.

## 22. L-300 — three further smallest non-`garn*` county-set tails completed; two unlinked early marriage entries retained

The next three smallest remaining non-`garn*` CAPPED rows were enumerated with
unbounded `lastname` searches and event-year ascending sort, again following
only page links exposed by the live Findmypast result interface.  No event-year
parameter was used, because this campaign has already demonstrated that those
parameters can fail closed or leak in individual FMP collections.  The complete
result sets were: *Northamptonshire Marriages*, `gurn*`, **60** rows;
*Cambridgeshire Marriages*, `gurn*`, **57** rows; and *Westminster Baptisms*,
`gorn*`, **58** rows.  Their 175 displayed rows add the ledger continuation
lower bounds of 40, 40, and 46 respectively.  Together with section 21, the
ten completed non-`garn*` result sets now total **427 displayed rows** and
resolve **257** lower-bound continuation rows.

These are all index/transcript findings.  No original image was opened for
interpretation, downloaded, or retained; no media, source registry, corpus, or
paleography work follows.  The FMP collection pages characterise the first two
sets as local-society transcriptions: Northamptonshire Family History Society
for the Northamptonshire entries, and Cambridgeshire and Huntingdonshire Family
History Society for Cambridgeshire.  The Cambridgeshire collection is explicitly
transcript-only and covers about 80 parishes.  Westminster reports transcripts
of originals held by City of Westminster Archives Centre, across more than 50
Westminster parishes.  Those source scopes make a collection result useful but
not an all-parish or all-England absence claim.

### Completed result sets and relevant early rows

| Collection and stem | Complete chronological result | Relevant transcript/table evidence | Boundary |
|---|---:|---|---|
| *Northamptonshire Marriages*, `gurn*` | 60 rows; the first row is 1575 and the next is 1703. | [`GBPRS/M/611065708/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FM%2F611065708%2F1): **John Gurney**, 10 Jul 1575, spouse **Margaret Hunt**, indexed marriage place Northampton All Saints; the transcript also indexes parish “Huntington St Mary's Hun” and the spouse as servant. | This isolated early entry is far too early to identify the c.1605 target.  Its conflicting displayed marriage-place/parish fields are a transcript/index issue to preserve, not a basis for geographic inference.  The fully sorted set has no `gurn*` marriage dated 1600–1645. |
| *Cambridgeshire Marriages*, `gurn*` | 57 rows in three pages (20 + 20 + 17). | [`GBPRS/M/324084154/3`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FM%2F324084154%2F3): **Elizabeth Gurney** married **Thomas Blackabee**, 11 Jan 1636, Cambridge St Peter.  The transcript supplies no parent field for Elizabeth.  Other 1600–1645 table rows are Gurner variants at Ickleton, Thriplow, and Hinxton. | A dated exact-surname marriage lead, not a parentage or migration link.  It neither names a father John nor connects Elizabeth to the colonial family.  Same-county or spelling proximity cannot supply that link. |
| *Westminster Baptisms*, `gorn*` | 58 rows in three pages (20 + 20 + 18); earliest event 1624. | [`GBPRS/B/492001300/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FB%2F492001300%2F1): **Charles Gornige**, baptised 1624, St Margaret, Westminster, father **George**, mother blank.  The next early indexed family is Elizabeth Gorner, 1664/1665, father Daniel, mother Ann. | The complete `gorn*` result contains no baptism through 1645 with an indexed father John and mother Mary or Margaret.  That is a source-and-stem-specific table result only; it does not eliminate omitted parents, other renderings, or unindexed Westminster material. |

The Cambridgeshire Elizabeth marriage and the Northamptonshire 1575 John
marriage are retained as **unlinked record facts**, not candidate identities.
Neither record supplies the target parents, later English household, New England
appearance, or departure evidence.  The Westminster Charles row is likewise a
non-target father-George event.  No relationship claim follows from surname,
spelling, parish, or the provider's record layout.

### Updated completeness position

The ledger contains 18 non-`garn*` and 13 `garn*` CAPPED rows.  Completing ten
of the 18 non-`garn*` rows is **55.6%** of that lower-noise subgroup and ten of
the full 31-row CAPPED backlog is **32.3%**.  Eight non-`garn*` rows remain:
Cambridgeshire Baptisms `gurn*` (93 lower-bound continuation rows), Berkshire
Baptisms `gurn*` (103), Westminster Baptisms `gurn*` (292), Middlesex Baptisms
`gurn*` (342), Westminster Marriages `gurn*` (368), Essex Baptisms `gurn*`
(473), Norfolk Marriages `gurn*` (514), and Norfolk Baptisms `gurn*` (769).
All 13 `garn*` rows remain high-noise and account for most of the raw backlog.

The next proportionate FMP action is **Cambridgeshire Baptisms `gurn*`**, the
smallest remaining non-`garn*` tail.  Before interpreting any negative from it,
characterise that collection's parent-field and parish coverage and enumerate
the complete unbounded result set; do not replace it with a date-filtered zero.

## 23. L-300 — Cambridgeshire and Berkshire `gurn*` baptism tails fully enumerated; a Bray father-John entry remains unlinked

The two next non-`garn*` CAPPED baptism rows were completed with an unbounded
`lastname=gurn*` search, event-year ascending sort, and only the page links
visible in the Findmypast result interface.  *Cambridgeshire Baptisms* returned
**107** rows in six pages (20 + 20 + 20 + 20 + 20 + 7); *Berkshire Baptisms
Index* returned **117** rows in six pages (20 + 20 + 20 + 20 + 20 + 17).
They add their ledger continuation lower bounds of 93 and 103.  The twelve
completed non-`garn*` result sets across sections 21–23 now comprise **651
displayed rows** and resolve **453** lower-bound continuation rows.

Both collections were source-characterised before the result sets were read.
Cambridgeshire is a transcript-only collection, transcribed by the
Cambridgeshire and Huntingdonshire Family History Society, covering about 80
parishes/registrar places plus some Cambridgeshire and Huntingdonshire births at
the British Lying-In Hospital in London.  Berkshire is a transcript collection
from Berkshire Family History Society / Findmypast / College of Arms material;
its own description says field completeness varies, and the opened 1619 record
is a Berkshire Archives **Bishop's Transcript**.  Thus the following are
collection-and-index findings only.  No original image was opened for
interpretation, downloaded, or retained; no media, corpus, source-registry, or
paleography action follows.

### Relevant 1600–1645 records

| Collection and stem | Directly checked transcript/table facts | Evidence boundary |
|---|---|---|
| *Cambridgeshire Baptisms*, `gurn*` | The chronological 1600–1645 block is predominantly an Ickleton Gurner group.  [`GBPRS/B/323087513/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FB%2F323087513%2F1) is **John Gurner**, baptised **19 Dec 1613**, Ickleton; father **William**, mother `-`.  [`GBPRS/B/323087934/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FB%2F323087934%2F1) is a second **John Gurner**, baptised **9 Feb 1645**, Ickleton; father **William**, mother **Luce**.  The other early table rows have fathers Francacus/Francis, William, or Robert. | Neither John has a father John or mother Mary/Margaret.  The complete `gurn*` table has no 1600–1645 baptism indexed with father John.  That does not eliminate spellings outside this stem, omitted parents, uncovered parishes, or a record outside the collection. |
| *Berkshire Baptisms Index*, `gurn*` | [`GBPRS/BERKSHIRE/BAP/001677302`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FBERKSHIRE%2FBAP%2F001677302): **Gulielmi Gurnet**, baptised **8 Jun 1619**, Bray, Berkshire; father **Johis Gurnet**, mother `-`; archive Berkshire Archives; document type Bishop's Transcript; stated year range 1607–1635.  The full sorted set has early entries through 1619 and then its next result at 1658. | This is a genuine indexed father-John (Latin/contracted `Johis`) event, but the child is Gulielmi/William, the mother is unindexed, and the surname is Gurnet.  It cannot be attached to the colonial John, to any Mary/Margaret, or to a wider Bray family without a primary register or independent household evidence. |

The Berkshire entry is retained as a **source-specific household lead**, not a
candidate identity.  It is not a counterexample to the no-`John +
Mary/Margaret` finding, because the maternal field is literally blank.  The
provider's related-record links and the shared parish/surname are not used as
relationship evidence.

### Updated completeness position

Twelve of the 18 non-`garn*` CAPPED rows are now complete (**66.7%** of the
lower-noise subgroup), or 12 of the full 31-row CAPPED ledger (**38.7%**).
Six non-`garn*` rows remain: Westminster Baptisms `gurn*` (292 lower-bound
continuation rows), Middlesex Baptisms `gurn*` (342), Westminster Marriages
`gurn*` (368), Essex Baptisms `gurn*` (473), Norfolk Marriages `gurn*` (514),
and Norfolk Baptisms `gurn*` (769).  All 13 high-noise `garn*` rows remain.

The next proportionate FMP work is **Westminster Baptisms `gurn*`**, the
smallest remaining non-`garn*` tail.  Its collection has already been
characterised in section 22; enumerate its unbounded chronological result set,
record parent fields and transcript IDs for any pre-1645 rows, and do not use a
date-filtered zero as a negative.

## 24. L-300 — Westminster Baptisms `gurn*`: target-period screen completed; full 304-row tail remains open

The unbounded, event-year-ascending *Westminster Baptisms* `gurn*` result set
contains **304** rows.  Its first chronological page spans 1560–1706, so it
fully displays this stem's 1600–1645 window without relying on FMP's unreliable
date parameters.  Pages 1–5 (100 displayed rows) were traversed; pages 6–16
remain unenumerated.  Therefore this section records a **complete
target-period table screen**, but explicitly does **not** close the 292-row
continuation tail or the CAPPED query.

The collection itself reports transcripts of original registers held by City of
Westminster Archives Centre, from more than 50 Westminster parishes.  No image
was opened, downloaded, or retained.  The following is index/table evidence;
the source description's usual parent fields do not cure a literal blank field
in an individual result.

| Indexed event from the complete 1600–1645 first-page block | Parent fields and transcript ID | Boundary |
|---|---|---|
| Thomas **Gurnell**, 1619, St Margaret, Westminster | father **John**; mother `-`; [`GBPRS/B/491998458/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FB%2F491998458%2F1) | A father-John, motherless Gurnell entry.  It is not a John-and-Mary/Margaret family and does not identify the colonial John. |
| Steephen **Gurney**, 1625, St Mary-le-Strand | father **Steeven**; mother **Frances**; [`GBPRS/B/492300708/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FB%2F492300708%2F1) | Exact surname but non-target parents.  No relationship claim follows from location or surname. |
| Mary **Gurney**, 1643, St Margaret, Westminster | father **Walter**; mother **Mary**; [`GBPRS/B/492011329/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FB%2F492011329%2F1) | A named Mary occurs, but with father Walter—not John. |
| Walter **Gurnell**, 1645, St Margaret, Westminster | father **Walt**; mother **Mary**; [`GBPRS/B/492012380/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FB%2F492012380%2F1) | The result sits at the edge of the stated period and also has no father John. |

Within the full first chronological page there is no baptism dated 1600–1645
with indexed father John and indexed mother Mary or Margaret.  This is a useful
**Westminster-collection, `gurn*`-stem, target-window result** only.  It does
not exclude a differently rendered surname, an omitted parent, an uncovered
parish, or a record absent from the transcript set.  It also does not attach
Thomas Gurnell to any other Westminster household merely because his father is
named John.

The next FMP action is to resume page 6 of this exact chronological result set
and enumerate through page 16 before changing its CAPPED status.  The next
independent lower-noise tail remains Middlesex Baptisms `gurn*` (342 lower-bound
continuation rows).

### Completion update - 1 August 2026

Pages 6 through 16 have now been read through the visible chronological result
interface.  The complete set is 304 rows in 16 pages (15 pages of 20 and a
final page of 4).  The 204 rows on pages 6 through 16 begin with John Gurnell,
1777, and end with Ann Gurney, 1916; no row in that continuation falls in
1600-1645.  This closes the Westminster Baptisms `gurn*` CAPPED query.  The
13 completed non-`garn*` rows now total 955 displayed rows and resolve 745
lower-bound continuation rows: 13 of 18 lower-noise CAPPED rows (72.2%) and
13 of all 31 CAPPED rows (41.9%).

Five lower-noise rows remain: Middlesex Baptisms `gurn*` (342 lower-bound
continuation rows), Westminster Marriages `gurn*` (368), Essex Baptisms
`gurn*` (473), Norfolk Marriages `gurn*` (514), and Norfolk Baptisms `gurn*`
(769).  All 13 high-noise `garn*` rows remain.  The next proportionate FMP
action is Middlesex Baptisms `gurn*`, not a repeat Westminster search.

## 25. Source-retention remediation — selected county-sweep transcripts are now durable evidence, not dump-only observations

The campaign's earlier county-tail sections recorded potentially relevant FMP
results in this dump but did not retain the displayed transcript fields as a
source artifact. That was an inadequate boundary: a row count, an ID, and a
researcher's paraphrase do not make the provider's actual index evidence
inspectable. On 1 August 2026, twelve selected records were reopened and their
complete displayed data fields were retained in
[`sources/corpus_supplement/findmypast-county-gurney-variant-baptism-transcripts-1606-1643.md`](../../corpus_supplement/findmypast-county-gurney-variant-baptism-transcripts-1606-1643.md),
registered under the existing source ID
`findmypast-county-baptism-sets-2026-07-sweep`.

The retained set contains the county-tail entries with indexed father
John/Johis — Luke **Gornett** (Great Ryburgh, 1606), John **Gorner** (South
Walsham, 1616), Jane **Gerner** (Thursford, 1623), John **Gerney** (Earsham,
1635), Thomas **Gurnell** (St Margaret, Westminster, 1619), and Gulielmi
**Gurnet** (Bray, 1619) — plus direct target-period comparison entries that
show different indexed parent pairs: John **Gurner** (Ickleton, 1613; father
William), Steephen **Gurney** (St Mary-le-Strand, 1625; parents Steeven and
Frances), and Mary **Gurney** (St Margaret, Westminster, 1643; parents Walter
and Mary). The subsequent full transcript capture also retains Elizabeth
**Gorne** (Harwich, 1623; parents John and Elizabeth) and William **Gurnett**
(Abthorpe, 1641; father John, no mother field displayed). Each exact FMP
transcript ID, stable URL, archive metadata, date, place, and literal blank
field is preserved there.

The subsequently completed Middlesex Baptisms `gurn*` screen adds Joan
**Gurney** (Laleham, 1600; father John, no mother field displayed), so the
durable selected set is now twelve records.

This is deliberately a **selected record set**, not an assertion that every
reviewed county-sweep row is a candidate. Clearly remote, post-window, or
unrelated-name rows are not promoted into the corpus. Conversely, the retained
index fields do not create a family: shared surname, same parish, a father named
John, an FMP related-record suggestion, and a literal `-` in a parent field are
all insufficient for a relationship claim. No original-record link was opened,
no image was downloaded, and no paleographic inference has been made.

## 26. L-300 — Middlesex Baptisms `gurn*`: full live result set enumerated; one retained father-John entry

The archived CAPPED ledger gave Middlesex Baptisms `gurn*` a 342-row
lower-bound continuation. On 1 August 2026, the live unbounded `sid=103`
result, sorted through the visible interface by event year ascending, reported
**361 results** across 19 result pages. This is a live provider-count change,
not evidence that the prior lower-bound was erroneous or that the extra 19
records are necessarily new. The 19th page had one record result after an
interface promotion; the chronology runs from 1558 on page 1 to 1910 on that
last record page.

All 1600–1645 results occur on the first chronological page. The target-window
rows were: Joan Gurney, 1600, Laleham, father John; Robert Gurner, 1601,
Isleworth, father Edward; Mary Gurnard, 1613, St Vedast Foster Lane, father
Richard; Richard Gurnard, 1615, St Vedast, father Richard; Cundall Gurnendall,
1617, St Lawrence, father Charles; John Gurnard, 1618, St Vedast, father
Richard; Elizabeth Gurnard, 1620, St Vedast, father Richard; Thomas Gurney,
1628, Uxbridge, parents Daniel and Alice; Christopher Gurner, 1629, Isleworth,
parents Christopher and Mary; and two indexed 1630 George Gurnell records,
Hayes, father George. The next page begins in 1671; pages 2–19 were still read
to completion, and contain no 1600–1645 row.

The potentially relevant direct-surname/father-John row has been reopened and
retained in the county-sweep corpus supplement as Findmypast transcript
`GBPRS/B/907011843/1`: **Joan Gurney**, baptised 11 May 1600 at Laleham,
Middlesex, relationship Daughter, father John; the transcript displays no
mother field. It is index/transcript evidence only and neither identifies the
father nor links Joan to any other entry. In particular, this screen found no
1600–1645 row with indexed father John and indexed mother Mary or Margaret.

This completes a fourteenth lower-noise CAPPED row. The 14 completed
non-`garn*` rows now represent 1,316 live displayed rows and resolve 1,087
archived lower-bound continuation rows: 14 of 18 lower-noise rows (**77.8%**)
and 14 of all 31 CAPPED rows (**45.2%**). Four lower-noise rows remain:
Westminster Marriages `gurn*` (368 lower-bound continuation rows), Essex
Baptisms `gurn*` (473), Norfolk Marriages `gurn*` (514), and Norfolk Baptisms
`gurn*` (769). All 13 high-noise `garn*` rows remain.

## 27. L-285 — retained Berkhamsted register image resolves the 28 June 1638 Richard burial

Fresh explicit authority on 1 August 2026 permitted a new source-master pull.
The FMP viewer record
[`GBPRS/HERT/007567815/00277`](https://search.findmypast.co.uk/record?id=GBPRS%2FHERT%2F007567815%2F00277&parentid=GBPRS%2FD%2F72723126)
(transcript `GBPRS/D/72723126`) opened directly at page **165 of 175**. The
viewer displayed a `Download record` media link and the rights notice “©
Hertfordshire Archives & Local Studies. Not to be reproduced without
permission.” Chrome itself could expose the image and link but could not place
the master in the repository; after the generic web fetch refused the binary
URL, the same visible media URL was retrieved through the repository-local
Python HTTP client. That was the disclosed, limited non-Chrome capability used
only to transfer the source bytes.

The unmodified master is retained locally at
`sources/media/findmypast-hertfordshire-burials/_local/gbprs_hert_007567815_00277_page-165.jpg`:
3,716 × 3,780 px; 883,438 bytes; retrieval 1 August 2026; SHA-256
`21beb9013d738bef7980f8b1a1da3af0e109213ccbcbfadf53bc7db80cfd46e5`.
It and its working derivatives remain `_local/` because of the stated rights
restriction. The source-facing transcription and reproducibility coordinates
are retained in
[`findmypast-hertfordshire-berkhamsted-burial-page-165-1638.md`](../../corpus_supplement/findmypast-hertfordshire-berkhamsted-burial-page-165-1638.md);
the source registry and validation worksheet now point to it.

### Paleography workflow and reading

The master was inspected before transcription. A full-page grid located the
1638 entries on the right-hand page; a June band ladder (`x=1900`, five
overlapping 1,600 × 240 px bands from `y=1700` through `y=2420`) located the
target; then a target crop ladder and enhancement sheet were made. The core
target-line crop uses `1900,2360,1600,110` on the unmodified master. Raw,
gray, autocontrast, sharpen, unsharp, CLAHE, threshold, and invert-auto views
were compared; the raw, autocontrast, and sharpen views preserve the writing
most clearly, while threshold is supporting contrast only.

Because the Findmypast index already exposed the name and date, these were not
epistemically blind readings. To prevent the earlier withdrawn assertion from
deciding the result, I made two separately composed visual readings from the
raw crop and the wider/enhancement set before comparing either with the index.
They agree:

1. Raw target-line pass: `Richard the sonne of Thomas Gurney was buried the
   xxviij of June.`
2. Wider-context and enhancement pass: `Richard the sonne of Thomas Gurney
   was buried the xxviij of June.`

The adversarial comparison was whether the father's name could be **John**,
which would have attached the burial to the 1626 Richard. It cannot: the entry
visibly reads the six-letter `Thomas`, followed by `Gurney`; the immediately
adjacent 1638 June context confirms this is one continuous burial list. The
same image supplies no age, residence, or additional identity attribute, so it
does not by itself identify this Richard with a particular baptism. It does,
however, decisively exclude the John-fathered 1626 Richard from this burial and
directly assigns the buried Richard to a father named Thomas. Given the existing
parish reconstruction has the other Richard baptised in 1635 to Thomas, this
is the expected Thomas-household burial rather than a new connection to the
John household.

The earlier unsupported statement that the entry had been read as Thomas's son
is therefore no longer a viewer impression: it is now supported by a retained
source master and reproducible image work. No wider Candidate C probability
change is made here because campaign policy keeps this finding in the dump for
later promotion; the limited L-285 question is resolved.

## 28. L-300 — Westminster Marriages `gurn*`: live-count correction and controlled stop

The archived ledger’s 368-row continuation lower bound was checked against the
live, unbounded `sid=103` Findmypast result, sorted in the visible interface by
event year ascending. On 1 August 2026 it reported **383 results**, not 368.
That is a provider-state/count correction, not evidence that fifteen records
were newly created or that the historic lower-bound ledger was wrong.

The first chronological result page had two undated rows (Eliz Gurney / Wm
Smith and Thos Gurney / Rachel Keely, both St Clement Danes); then Elizabeth
Gurne / John Wright (24 Aug 1591, St Mary-le-Strand), two Henry Gurney /
Margaret rows (17 Jun 1592, St Clement Danes), and the following 1600–1645
rows: Dorethy Gurnett / William Brittay (09 Nov 1605, St Mary-le-Strand);
Anthoney Gurney / Anne Spurnil (12 Jul 1614, St Margaret, Westminster);
William Gurney / Rosamund Mansfield (25 Jun 1622, St Margaret, Westminster);
John Gurney / Joane Maxfeild and John Gurney / Joane Maxfield (09 Feb 1625,
St Clement Danes); Isabell Gurnell / William Bickorse (12 Nov 1626, St Clement
Danes); William Gurnett / Ffrizwith Cogger (20 Nov 1628, St Margaret,
Westminster); and Walter Gurney / Mary Hammond (01 Jun 1642, St Margaret,
Westminster).

On 1 August 2026, a fresh Chrome-extension session reopened and retained the
complete displayed fields for all thirteen first-page transcripts, including
the two undated rows and the 1591/1592 rows. They are now in
`sources/corpus_supplement/findmypast-westminster-marriages-gurney-transcripts-1591-1642.md`.
The transcript IDs are `GBPRS/WSMTN/MAR/0200341/2`,
`GBPRS/WSMTN/MAR/0199998/1`, `GBPRS/M/492346126/2`,
`GBPRS/M/492044358/1`, `GBPRS/M/492161735/1`, `GBPRS/M/492347200/2`,
`GBPRS/M/492309830/1`, `GBPRS/M/492310597/1`, `GBPRS/M/492046061/1`,
`GBPRS/M/492163436/1`, `GBPRS/M/492046127/2`, `GBPRS/M/492311304/1`, and
`GBPRS/M/492313039/1`. Every transcript displays county Middlesex, country
England, both residences as `-`, and no parent, age, or occupation field.
The Henry pair and John pair have matching event-level fields but spelling
variation in the spouse surname; both IDs are retained rather than silently
merged. This is transcript/index evidence only; no original register image was
opened and no relationship claim follows from the place, surname, or a blank
field.

The visible pagination was then completed in a fresh Chrome-extension session:
19 pages of 20 displayed rows and a final page of three rows, exactly
reconciling to the live **383**. Pages 2–20 span 1665–1941. Their chronological
first/last values were: p2 1665–1721; p3 1725–1753; p4 1754–1769; p5
1769–1777; p6 1781–1787; p7 1787–1790; p8 1790–1795; p9 1795–1804; p10
1804–1813; p11 1813–1818; p12 1819–1824; p13 1824–1828; p14 1828–1837;
p15 1837–1847; p16 1847–1857; p17 1858–1870; p18 1871–1900; p19 1901–1926;
and p20 1932–1941. Therefore every dated 1600–1645 row in this exact live,
unbounded `gurn*` result is on the retained first page. The two first-page
transcripts with provider year/date `-` cannot be assigned a date from the
index, so they remain retained but outside that chronological conclusion.

This completes the Westminster Marriages `gurn*` CAPPED tail: 15 completed
lower-noise rows now represent 1,699 live displayed rows and resolve 1,455
archived lower-bound continuation rows (15 of 18 lower-noise rows, **83.3%**;
15 of all 31 CAPPED rows, **48.4%**). The remaining lower-noise tails are
Essex Baptisms `gurn*` (473 archived lower-bound continuation rows), Norfolk
Marriages `gurn*` (514), and Norfolk Baptisms `gurn*` (769); all 13 high-noise
`garn*` rows still remain. These are query/backlog measures, not a claim that
Findmypast is complete for a parish, a surname, or a migration window.

## 29. L-300 — Essex Baptisms `gurn*` fully enumerated; Epping John-Gurnat row remains transcript-only

### Search design and collection boundary

This continuation used the single-dataset *Essex Baptisms* index only for what
it displays: child, event year, indexed parents, and place. The unbounded
`lastname=gurn*` result was opened without a year or place parameter, then
sorted through the provider's visible **Baptism year** ascending control
(`o=eventyear&d=asc`). This avoids the demonstrated fail-closed combination of
`yearofbaptism` with `keywords`, and it does not convert a parameterized zero
into a record-set negative. The exact live query returned **492** rows, not the
473-row archived lower bound.

Visible pagination was completed through the provider's own links: 24 pages of
20 rows and a final page of 12, reconciling exactly to 492. The chronological
page spans were p1 1560–1621; p2 1622–1649; p3 1649–1672; p4 1673–1691; p5
1693–1715; p6 1715–1722; p7 1724–1734; p8 1736–1759; p9 1760–1774; p10
1774–1790; p11 1790–1800; p12 1800–1814; p13 1815–1818; p14 1818–1825; p15
1826–1835; p16 1835–1842; p17 1842–1847; p18 1848–1850; p19 1850–1859; p20
1859–1868; p21 1868–1885; p22 1886–1893; p23 1893–1906; p24 1906–1914; and
p25 1914–1919. Thus the collection's visible 1600–1645 `gurn*` screen is
confined to pages 1–2; the two 1649 entries straddle pages 2–3.

This is a fully enumerated result for this exact live index query, not a
complete Essex-parish-register search and not an all-spelling negative. The
provider itself says its baptism transcripts derive from original registers but
are not comprehensive; parish coverage and fields vary. No original image was
opened in this continuation.

### Early entries and retained transcript evidence

The direct father-John finding remains **Richard Gurnat**, baptised 13 October
1616. The accessible Essex Record Office-labelled transcript
`GBPRS/ESSEX-BAP/0972474` gives archive ref `D/P 302/1/2`, place **Epping, All
Saints**, and father **John Gurnat**; the separate `R_21667615243` transcript
has the same date and parental fields but a blank place. Neither displays a
mother. The source therefore identifies only a father John under the rendering
Gurnat. It supplies no link to the colonial John, no Mary/Margaret, and no
household relationship beyond the displayed father-child field.

The other retained 1600–1645 index records demonstrate separate or unresolved
local groups rather than a John-and-Mary/Margaret solution: William Gurney,
1613, Aveley, father George; John Gurnye, 1616, and Tamzing Gurny, 1621, Little
Dunmow, fathers Willam/Will; John Gurne, 1622, Epping, father Robert and mother
Sara; Marie Gurney, 1625, Epping, father Robert and mother Sarra; Joan Gurney,
1628, and Marie Gurney, 1637, North Weald Bassett, father Robert and mother
Anne; John Gurney, 1641, Shenfield, father Thomas and mother Joane; Sarah
Gurnet, 1643, Fyfield, father field “William Clemence”; and the 1644 Francis
Gurnett (father Richard) and Thomas Gurnett (father Thomas, mother Joane) rows.
Their full displayed fields and stable transcript URLs are retained in
[`findmypast-county-gurney-variant-baptism-transcripts-1606-1643.md`](../../corpus_supplement/findmypast-county-gurney-variant-baptism-transcripts-1606-1643.md).

Four duplicate/provider-alternate IDs were visible in the results but currently
opened only to FMP's “Subscribe to unlock exclusive records” page:
`GBPRS/ESSEX-BAP/1881555` (the other 1610 George Gurnett row),
`XAUTO/FHS/ESSEX/BAP/00085043` (1616 Richard Gurnat at Epping Upland),
`XAUTO/FHS/ESSEX/BAP/00085177` (1622 John Gurnie at Epping Upland), and
`XAUTO/FHS/ESSEX/BAP/00085234` (1625 Marie Gurney at Epping Upland). Their
result-row fields are not retained as transcript text; the accessible matching
provider records above are retained instead. This is an access boundary, not a
claim that an underlying original is absent.

### Result for L-300

Across the complete visible 1600–1645 segment of this exact `gurn*` query, no
row displays both a father named John and a mother named Mary or Margaret. That
is a narrow **index-field result**, not a negative about an Essex household:
many rows omit mothers, `gurn*` is only one spelling stem, and no original
register has been read. Same-parish proximity, the Epping paired records, and
the provider's related-record affordances are not used to assert any
relationship.

This completes the sixteenth lower-noise CAPPED row. Completed lower-noise
queries now total **2,191** live displayed rows and resolve **1,928** archived
lower-bound continuation rows: 16 of 18 lower-noise rows (**88.9%**) and 16 of
the 31-row CAPPED ledger (**51.6%**). The only lower-noise continuations left
are Norfolk Marriages `gurn*` (514 archived lower-bound rows) and Norfolk
Baptisms `gurn*` (769); all 13 high-noise `garn*` rows remain. Those counts are
backlog measures, not a claim of Findmypast-wide, countywide, or familywide
completeness.

## 30. L-296 — Bedfordshire recheck: bounded Eaton Bray transcript retention, not a county sweep

### Why FMP remains useful here, and why it is not decisive

FMP remains an efficient **index/transcript discovery and field-comparison
tool** for this lead: it can put the two closely dated Eaton Bray entries and
their indexed parents in a single, reproducible worklist. It is not, however,
the sole or decisive route. The original Eaton Bray register is needed to test
whether the blank/omitted fields are readable and to establish any household
connection; nothing in this FMP work proves a relationship between same-parish
entries.

The live single-dataset *Bedfordshire Baptisms* interface is materially too
noisy for a county-negative. An unbounded `lastname=gurn*` query returned
**2,342** rows, including alternate/compound-surname rows (for example,
`Gernne Or Gurney`), while an exact `lastname=gurney` query still returned
**2,091** rows with repeated provider renderings. These are not distinct-event
counts. The exact result did sort correctly by the visible **Baptism year**
header (`o=eventyear&d=asc`), and its first two pages span only 1559–1588,
so chronological pagination is functioning; the worklist is nevertheless too
large and duplicate-heavy to call a completed Bedfordshire sweep.

### Positive-control year screen and retained records

To test a small early slice rather than interpret a zero, I ran the known
positive control `datasetname=bedfordshire+baptisms; sid=103;
lastname=gurney; yearofbaptism=1606; yearofbaptism_offset=5`. It returned
**19** visible rows, all on one page, and included the known Eaton Bray 1606
John. Thus this *Bedfordshire Baptisms* date parameter supplied a working
positive result in this bounded use; it is not generalized to other FMP sets
or used for a negative.

Two accessible provider transcripts have now been retained in the county-set
corpus supplement, each as displayed index/transcript evidence only:

| FMP record | Displayed transcript facts | Boundary |
|---|---|---|
| `R_951759235` | Thomas Gurney, male; bap. **26 Jun 1603**, Eaton Bray; father's first name `-`, father's last name Gurney, mother `-`; *Bedfordshire Baptisms* | Same parish and close date make it relevant to the Eaton Bray worklist, but blank fields do not make Thomas John's brother. |
| `R_951758452` | John Gurney, male; bap. **26 Sep 1606**, Eaton Bray; father John Gurney, mother `-`; *Bedfordshire Baptisms* | Chronologically possible only. It gives no mother, later life, migration, occupation, or tie to the colonial John. |

The result page also showed `XAUTO/FHS/BEDFORDSHIRE/BAP/00223086`, an
alternate provider rendering of the 1606 John, but its transcript opens only
to FMP's subscription screen. It is an access boundary, not a second event or
evidence of an original-image reading. The accessible `R_951758452` record is
the retained transcript for that event. The 1594 Richard Gurney–Margaret Sandan
marriage and 1596 Margaret burial remain contextual index leads only; this
recheck did not use them to manufacture an Eaton Bray household.

### Consequence and next step

L-296 remains **Partial**. The high-value FMP contribution is now bounded:
confirming the exact transcript fields for the 1603/1606 Eaton Bray entries
and demonstrating that the year slice is usable as a positive control. The
next decisive work is the **original Eaton Bray register** (or an archive
transcription/copy), followed by a documentary check for the 1606 John's later
English life. Do not retry an all-rows FMP Bedfordshire enumeration while its
duplicate/alternate-name model remains this large.

## 31. L-300 -- Norfolk Banns and Marriages `gurn*` fully enumerated; two early transcripts retained

### Search design and collection boundary

The remaining marriage tail was run as an **unbounded** `lastname=gurn*`
search in Findmypast's *Norfolk Banns and Marriages* collection (`sid=103`),
with the visible result list sorted by **event year ascending**. No date,
place, or parent-name parameter was used, because the project has already
demonstrated collection-specific fail-closed and leaky parameter behaviour.
The live interface reported **533** displayed rows, rather than the archived
514-row CAPPED lower-bound continuation. All **27** visible pages were read
through the site's own pagination (26 pages of 20 and a final page of 13); the
final page ends at a 1940 marriage and exposes no page 28. This is a complete
enumeration of this live query, not a count of distinct marriages: the set
visibly includes marriage/banns duplicates and variant surname renderings.

The chronological sweep places the dated 1600-1645 rows on pages 1-3: page 2
runs 1606-1630 and page 3 runs 1631-1671. Page 1 also contains provider
entries carrying broad year ranges (including 1538-1653), which cannot be
assigned to a particular event year from the result table and are not treated
as target-period events. Page 4 begins in 1673; pages 5-27 then continue to
1940. Thus no later page can add a dated 1600-1645 marriage.

### Retained provider transcripts and exact boundary

Only two actual transcripts were retained. They add durable source text rather
than a broad wildcard hit list; neither is an original-register reading, and
the linked `View original record` affordances were not opened.

| FMP record | Complete-provider result of the check | Evidence boundary |
|---|---|---|
| [`GBPRS/NORFOLK/MAR/000794131/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FNORFOLK%2FMAR%2F000794131%2F1&tab=this) | **Sion Gurney**, male, married **Amia Davison**, 12 Sep 1636, Saxlingham Nethergate with Saxlingham Thorpe; Norfolk Record Office `PD 281/1`; parish register; Diocese of Norwich. | This independently provider-pins the already known Sion/Amia marriage in the Hempnall/Waveney comparator work. It supplies no parents and does not turn the plausible multi-generation Sion sequence into a proved father-son chain. |
| [`GBPRS/NORFOLK/MAR/000368005/1`](https://www.findmypast.co.uk/transcript?id=GBPRS%2FNORFOLK%2FMAR%2F000368005%2F1&tab=this) | **John Gurny**, male, married **Jane Wright**, 09 Mar 1639, Norwich St Benedict; original parish **Hempnall**; Norfolk Record Office `PD 191/1`; parish register; Diocese of Norwich. | This is a real adult John-Gurny event with a useful original-parish index field, but no parents, age, residence, occupation, migration evidence, or connection to the Massachusetts emigrant. Hempnall proximity and the shared surname are not a relationship claim. |

Their full displayed fields and stable transcript links are retained in
[`findmypast-county-gurney-variant-baptism-transcripts-1606-1643.md`](../../corpus_supplement/findmypast-county-gurney-variant-baptism-transcripts-1606-1643.md).
The many other early `gurn*` result rows were ordinary adult marriages or
variant-name hits without a discriminating parent, locality, or target-family
marker; retaining them as a corpus would create noise rather than evidence.

The collection itself says it contains transcripts and images, but this round
read **transcripts only**. In particular, FMP's generic explanatory text says
that original marriage registers may hold additional fields; it does not mean
that an unindexed field is absent from `PD 281/1` or `PD 191/1`. Any attempt to
identify this John, assess the 1639 Hempnall connection, or assemble a family
must use the original registers or independent documentary evidence.

### L-300 reconciliation and FMP-routing audit

This is the seventeenth completed lower-noise CAPPED row. Completed lower-noise
queries now total **2,724** live displayed rows and resolve **2,442** archived
lower-bound continuation rows: **17 of 18** lower-noise rows (**94.4%**) and
**17 of all 31** CAPPED rows (**54.8%**). The only lower-noise continuation is
**Norfolk Baptisms `gurn*`** (769 archived lower-bound rows); all 13 high-noise
`garn*` rows remain. These are workload-completeness measures, never a claim
of county, parish, surname, or migration-window completeness.

Before beginning that last broad baptism tail, the other high-value questions
were re-routed explicitly. FMP is no longer the decisive route for L-285
(retained Berkhamsted original image), L-283 (Buckinghamshire original), L-291
(Essex Archives Online/ERO images), or L-294 (Upton original register). For
L-296 it has now supplied the useful bounded Eaton Bray transcript comparison
and a positive-control result; the original register remains decisive. The
remaining FMP value is therefore chiefly the final Norfolk baptism enumeration
and narrowly targeted transcript comparison, not repeat searches of routes
whose source boundary is already known.

### QC handoff: checks a later reviewer should make before promotion

1. Recompute the 17/18 and 17/31 arithmetic against the CAPPED ledger and
   confirm that the 533 live count remains a visible-interface count, not a
   distinct-event count.
2. Inspect the two retained tables against the displayed FMP transcript pages;
   check especially `Original parish: Hempnall` for `000368005/1` and
   `Archive reference: PD 281/1` for `000794131/1`.
3. Keep the Sion transcript as corroborative index/transcript evidence only;
   its marriage is already held from the Ancestry/NRO collection, and neither
   provider proves the inferred intervening generations.
4. Do not promote the 1639 John into the emigrant's file as an identity,
   parent, or residence fact. It is a bounded comparator lead whose next
   evidentiary step is `PD 191/1`, not same-name reasoning.
5. If any later original image is read, begin a new source-capture workflow:
   retain the unmodified master in the required `_local/` directory, record
   URL/record/page/date/hash/rights, and use the paleography workflow. This
   transcript-only round created no image, media object, or paleographic text.
