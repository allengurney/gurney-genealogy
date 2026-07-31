# G13 context-graph breadcrumb — standing tracker

**Nothing here is applied to the graph.** This file is a **pointer and tracker**, not a store of
content: it says *what has changed, where the prose now lives, and which existing graph items are
affected*, so an increment can be authored later without re-deriving anything. It deliberately does not
restate the findings — follow the pointers.

**When authoring:** derive live RI/PM ids from the database, not from this file. The graph is deliberately
being held while the July 2026 refactor stabilises.

## Index of entries

| Entry | Date | Bearing |
|---|---|---|
| [West Barsham PCC wills and the PCC index sweep](#2026-07-22--west-barsham-pcc-wills-and-the-pcc-index-sweep) | 2026-07-22 | Fostering branch, Court of Wards, collateral siblings, PCC negative, three elimination rows |
| [`G13-RI-000153` carries a superseded claim](#added-2026-07-22-second-pass--a-superseded-claim-carried-in-the-graph) | 2026-07-22 | Rybett family / marriage parish |
| [East Dereham register limits and the Candidate B reversal](#2026-07-27--east-dereham-register-limits-and-the-candidate-b-reversal) | 2026-07-27 | Entry E, register extent, probability model |
| [Buckinghamshire elimination on individuating records](#2026-07-27--buckinghamshire-elimination-on-individuating-records) | 2026-07-27 | §8 candidate rows, occupational argument |
| [The naming convention read forwards](#2026-07-27--the-naming-convention-read-forwards-and-a-new-candidate) | 2026-07-27 | Richard-naming argument, new Cheddington row |
| [The central-court and estate-archive sweep](#2026-07-28--the-central-court-and-estate-archive-sweep) | 2026-07-28 | East Dereham household identity, certificate class, two new Bucks households |
| [The East Dereham Gurney family, and three corrections](#2026-07-28-second-pass--the-east-dereham-gurney-family-and-three-corrections) | 2026-07-28 | Register extent pre-1610, a named local family, Sarah, the §11 rationale |
| [The Berkhamsted burials, and a candidate reduced](#2026-07-28-tenth-pass--the-berkhamsted-burials-and-a-candidate-reduced) | 2026-07-28 | **Retraction of the departure gap; C(ii) 9→4%; §11 revised again; R-47 resolved; sid=102 pool limit** |
| [The second instrument, and a negative downgraded to a floor](#2026-07-28-eleventh-pass--the-second-instrument-and-a-negative-downgraded-to-a-floor) | 2026-07-28 | FreeREG (S8) first run; the child negative is a floor; Stewkley splits. **Its "FindMyPast does not hold" claim is corrected by the twelfth pass** |
| [Four instruments compared, and the sweep's own undercount](#2026-07-28-twelfth-pass--four-instruments-compared-and-the-sweeps-own-undercount) | 2026-07-28 | **Exact-forename constraint undercounted (17→54); no index complete; three fathers read; new Sussex John+Mary household; Peter/Isaac on hold** |
| [The FreeREG sweep completed, and a Sussex lead closed](#2026-07-28-thirteenth-pass--the-freereg-sweep-completed-and-a-sussex-lead-closed) | 2026-07-28 | **585 records, 20 spellings; no father-John + mother-Mary anywhere; four new father-John households; Sussex closes at Horsham 1702** |
| [Essex tested](#2026-07-28-fourteenth-pass--essex-tested-and-a-surname-confusion-in-the-candidate-pool) | 2026-07-28 | Essex swept for the first time; Maldon branch corroborated. **Its variant-exclusion claim and its "Essex closes" conclusion are both retracted by the fifteenth pass** |
| [The variant retraction](#2026-07-29-fifteenth-pass--the-variant-retraction-and-what-it-changes) | 2026-07-29 | **Gurnard is a documented Gurney alias (Visitation 1634); variants are per-record weights not classes; counting is the wrong metric; Essex inverts to OPEN** |
| [Weymouth first; the West Country swept](#2026-07-29-sixteenth-pass---weymouth-first-a-withdrawn-norfolk-reading-and-the-west-country-swept) | 2026-07-29 | **Ludden's Norfolk reading WITHDRAWN (both claims unsourced); Dorset and Somerset swept for the first time and empty of shape-matches** |
| [Every candidate scored against the shape](#2026-07-29-twentieth-pass---every-candidate-scored-against-the-shape) | 2026-07-29 | **Candidates split into two disjoint families - households with the wrong shape vs men with no household; Hitcham 5->3 on the Farnham Royal alternative; five rubric corrections** |
| [The funnel closed; the unassembled row split](#2026-07-29-nineteenth-pass---the-funnel-closed-on-births-and-marriages-the-unassembled-row-split) | 2026-07-29 | **Marriage arm finished on a 5th instrument (no John x Mary); mother axis swept 1st time (Eythorne only); assembled 30->17 and a new 9% coverage row; Ackworth 9, Hitcham 5** |
| [The parent-name sweep completed](#2026-07-29-eighteenth-pass---the-parent-name-sweep-completed) | 2026-07-29 | **598 rows, 1615-1649. Hitcham 1631 is the ONLY unaccounted-for colonial-name child to a father John in Britain. No row moves** |
| [Burials as the elimination instrument](#2026-07-29-seventeenth-pass---burials-as-the-elimination-instrument-two-rows-move) | 2026-07-29 | **Four rows move: A(1603) 4->2 on a Stewkley burial the file said did not exist; Hitcham 5->4 on hollow coverage; Cheddington 7->6 and Bucks group 6->5 on an empty two-sided county marriage sweep** |

---

## 2026-07-22 — West Barsham PCC wills and the PCC index sweep

## Source anchors to register first

| Source ID | What it is |
|---|---|
| `tna-pcc-west-barsham-gournay-wills` | PROB 11/188/136 (Edward Gournay, pr. 8 Feb 1642) and PROB 11/303/284 (Henry Gourney, pr. 11 Feb 1661), both read in full |
| `ukda-4816-pcc-wills-index` | PCC will index 1384–1858; 212 Gurney-variant testators extracted |

## Candidate findings with a G13 bearing

1. **The paternal-uncle fostering branch is materially weakened.** The childhood-household
   topic flagged that if Thomas Gurnay died c. 1615, his household could not have fostered
   the motherless John (b. c. 1609/10). That conditional has now largely resolved: the Norris
   memorandum of 23 March 1615 (Daniel Gurney, *Record* Pt II, p. 370) records Thomas already
   dead, his widow Martha holding the evidences, and his son and heir aged about five with an
   inquisition pending. With the indexed 1615–16 inventory and Edward's succession as a minor,
   three witnesses converge on death by early 1615. Bearing: **downgrade** the Thomas-household
   branch of the fostering hypothesis; the paternal-uncle route now runs better through
   Anthony, Henry, or Edmund.

2. **The 1627 Court of Wards "Mrs Gurny" identification is corroborated.** Edward Gournay's
   will asks to be buried near **Martha Gournay** at West Barsham — his mother, the widow of
   the 1615 memorandum. That is the same Martha (Lewkenor) already read into the Gurdon–
   Winthrop letter of 20 October 1627 as guardian of her near-majority son Edward. The
   guardian/ward pair is now documented from two independent directions.

3. **A new collateral sibling group at the senior seat.** Edward's will names brother
   **Thomas** and sisters **Susan, Dorothy, Elizabeth, Ellin, Margarett** — children of Thomas
   Gurnay and Martha, i.e. first cousins of John G13's father Francis G14's generation once
   removed. These are new people, and they independently corroborate the L'Estrange anecdote
   roster (which names Ed./Ned Gurney, Tho. Gurney "his brother", Dol. Gurney "Dorothy, his
   sister, died single", and Fra. Gurney as "an uncle of Edward").

4. **A clean structural negative for the elimination plane.** No direct-line ancestor appears
   anywhere in the PCC index across 1384–1858. The Norfolk line proved in the Norwich
   Consistory Court; the absence is jurisdictional, not evidential. This is worth carrying as
   an explicit negative so future work does not re-run the search.

5. **Three §8-relevant elimination rows may rest on wrong places.** The SN 4816 index and the
   repository's earlier scan readings disagree on PROB 11/335 (Aylesbury, Bucks vs Albury,
   Herts), PROB 11/241 + 11/242 (East Claydon, Bucks vs East Chiltington, Sussex), and
   PROB 11/252 (East Greenwich, Kent vs East Grinstead). These were used as elimination rows.
   The Aylesbury reading is the one that matters most, because it touches the live
   Aylesbury-candidate topic. Tracked as lead L-260. **Do not restate the affected elimination
   rows in the graph until this is settled.**

6. **A bounded backlog worth a coverage node.** Thirty-one of the forty-nine pre-1700 PCC
   Gurney-variant wills have never been examined, fully enumerated in the corpus supplement.
   The pre-1620 London merchant/draper cluster (PROB 11/46, 11/75, 11/89, 11/132) sits on the
   London-draper candidate thread. Tracked as lead L-262.

## Added 2026-07-22 (second pass) — a superseded claim carried in the graph

**`G13-RI-000153` states something the maternal-family research has overturned.** It says the
Rybett/Ryvett family "were Norfolk and Suffolk gentry" and that "St Martin at Palace was their
own Norwich parish, with Rivett entries running 1539–1603, so Margaret almost certainly
married from her family's church." Its sources are the Suffolk Visitation pedigrees, FreeREG
transcriptions of St Martin at Palace, and `nro-pd-12-1` described as "the Rybett family's
parish."

The later Garveston work establishes Margaret as a **Rivet of Garveston** — a **copyhold**
family in a village about fifteen miles west of Norwich, whose relationship to the Suffolk
gentry Ryvetts is explicitly unresolved (lead L-133) and whose status marker points *against*
the connection: the Suffolk Ryvetts generated Court of Wards business because they held land
in chief, and no mid-Norfolk Rivett appears in that series at all. "Rybett" is the 1611
clerk's one-off spelling; the family writes itself *Rivet*. The Garveston companion states
plainly that the marriage was "not Garveston, East Dereham, or any parish either family is
otherwise documented in."

There may well be Rivetts at St Martin at Palace 1539–1603, but they are **Norwich city
Rivetts**, and nothing links them to the Garveston copyholders. The inference "her family's
church" only held while Margaret was believed to be a gentry Ryvett.

**Graph actions when the increment is authored:** revise or retire `G13-RI-000153`'s middle
clause; the marriage-parish question should become an open question rather than a settled
explanation. `G13-RI-000086` already handles the chronological friction correctly and needs no
change. The same superseded sentence appears in the identification case file at §2.2 and
should be corrected there in the same pass.

### Where that prose lives

- `sources/corpus_supplement/pcc-wills-gurney-variants-1384-1858.md` — full testator list and coverage status
- `sources/corpus_supplement/tna-pcc-west-barsham-gournay-wills.md` — the two transcriptions
- `research/people/g15-henry-gurney-fact-sheet.research.md` — the succession, the Thomas re-weighting, the Chancery identifications
- `research/places/west-barsham.md`, `research/places/north-barsham.md` — estate and Scotts Hall
- Leads: L-113, L-115, L-258 updated; L-260, L-261, L-262 opened

---

## 2026-07-27 — East Dereham register limits and the Candidate B reversal

**Bearing: substantial. Several graph items assert things the register can no longer support.**

Prose lives at
[`research/people/g13-john-gurney/topics/identity/50-refactor-east-dereham-register-limits.md`](../../research/people/g13-john-gurney/topics/identity/50-refactor-east-dereham-register-limits.md)
and
[`51-refactor-francis-marriage-death-and-pease.md`](../../research/people/g13-john-gurney/topics/identity/51-refactor-francis-marriage-death-and-pease.md).
Register structure and coverage: `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md`.
Masters: `sources/media/nro-pd-86-41/_local/`.

What an increment must handle:

1. **The "John son of ffrancis Gurnie" baptism does not exist.** Any item asserting it, or resting a
   date or a probability on it, needs retiring or restating. Named in the earlier audit as affecting
   `G13-RI-000158`, `G13-PM-000100`, `G13-PM-000109` and the probability passages — **verify against the
   live database before editing; those ids were read from a stale note.**
2. **PD 86/41 is complete at 110 images and the 1611–1615 returns are lost**, with no bishop's or
   archdeacon's transcript before 1698 and no bound register 1596–1679. This is a permanent evidentiary
   limit and probably deserves its own item rather than a caveat on an existing one.
3. **Edward's baptism is upgraded to D-class, 27 May 1610**, fixed by an in-parchment heading. Any item
   holding it at ±2–3 years on the "modern marginal annotation" premise is wrong on the premise.
4. **The chronology-lattice rows for 1617–1619 are interpolations from a false assumption**, and
   "page 00725 = the 1615 register year" cannot stand. Dates derived from either need re-deriving.
5. **The Pease tradition is unsourced in Pease** and did not come from Philis Wainford. Any item that
   treats the Ryvett/John detail as externally corroborated needs restating.
6. **Francis G14's probate is negative in four jurisdictions**, with the Archdeaconry of London
   outstanding; his burial date rests on a transcript-level FreeREG entry. Worth an explicit
   coverage/negative item so the search is not re-run.

## 2026-07-27 — Buckinghamshire elimination on individuating records

**Bearing: the §8 candidate rows and the occupational argument.**

Prose lives at
[`52-refactor-bucks-herts-elimination.md`](../../research/people/g13-john-gurney/topics/identity/52-refactor-bucks-herts-elimination.md);
extract at `sources/corpus_supplement/bucks-probate-index-brs114-gurney-variants-to-1660.md`;
new source `england-wales-published-probate-indexes`.

What an increment must handle:

1. **Three new individuating English deaths** — John Gurney of Monks Risborough 1623, of Hulcott
   (yeoman) 1630, of Southcott in Linslade 1636 — each eliminating a household the register work could
   not resolve.
2. **Candidate A splits into two men.** TNA E 115/180/113 (1641) is verified and shows a move to
   Northamptonshire; the St Mary Aylesbury baptisms run to 1653. One row should become two.
3. **The Stewkley household did not end in 1614** — Stewkley Gurney probates at 1618, 1631 and 1651.
   Any item asserting the household went silent is describing a register-coverage artefact.
4. **A Buckinghamshire Gurney tailoring trade exists** across five testators 1571–1633, and the colonial
   John was a tailor. The occupational argument is currently framed as exclusive to Candidate B; it is
   not.
5. **Two new named candidates** — the Weston Turville and Hitcham heads — currently sit inside a
   group-cleared block and fit the deposition age better than several rows that already exist.
6. **Coverage statements worth carrying as negatives:** Hertfordshire is absent from the published
   probate-index dataset entirely; Northamptonshire is covered only from 1677 and only for
   administrations.

## 2026-07-27 — the naming convention read forwards, and a new candidate

**Bearing: a new §8 row, and a correction to how the Richard-naming argument is stated.**

Prose lives at
[`54-refactor-naming-convention-and-the-cheddington-household.md`](../../research/people/g13-john-gurney/topics/identity/54-refactor-naming-convention-and-the-cheddington-household.md).

What an increment must handle:

1. **The "Richard honours Richard Ryvett of Gressenhall" explanation is structurally unavailable** as
   currently stated. A maternal grandfather belongs in the second-son slot; Richard is the eldest known
   son. Any item asserting the Ryvett reading needs the dependency on Sarah's existence made explicit.
2. **A new candidate:** John Gurney baptised Cheddington 5 August 1608, son of Richard Gurney and Jane
   Founteine, father's probate 1626. Reached by prediction from the naming custom rather than by name
   match. Roughly on a level with the other Buckinghamshire survivors.
3. **A second naming signal:** Isaac is a Buckinghamshire Gurney name and not a Norfolk one, and the
   colonial John's youngest son was Isaac.
4. **Buckinghamshire apprenticeship records are a structural absence**, not an unrun search — no county
   livery companies, and TNA IR 1 begins 1710. Worth an explicit coverage node so it is never logged as
   a negative result.
5. **A colonial-side dependency worth its own item:** the whole inference turns on Sarah, the supposed
   eldest child, not existing. Her existence rests on compiled tradition with no primary record.

## 2026-07-28 — the central-court and estate-archive sweep

**Bearing: the "why East Dereham" finding, the Candidate A rows, the occupational argument, and the
coverage plane.**

Prose lives at
[`55-refactor-central-court-and-estate-records.md`](../../research/people/g13-john-gurney/topics/identity/55-refactor-central-court-and-estate-records.md);
extract at `sources/corpus_supplement/tna-discovery-gurney-equity-and-estate-records-1590-1685.md`;
new sources `tna-discovery-catalogue` and `worcs-archives-pakington-westwood-park`.

What an increment must handle:

1. **The East Dereham Gurney household of the previous generation is now named.** Chancery
   C 2/Eliz/G13/62 gives Michael Gourney, dead by about 1602, his widow **Margery** — all but
   certainly the 1602–03 Archdeaconry testatrix already in the graph — and his adult son **Arthur**,
   father and son jointly seised of freehold tenements in East Dereham, with a £100 legacy. Items
   asserting the Margery finding as support for "why East Dereham" need restating: the fact is
   symmetric, and a propertied local family producing adult sons around 1600 is equally an
   alternative source for the "ffrancis Gurney" baptising there in 1610 and 1618. The identity of the
   East Dereham Francis should become an explicit open question rather than an unstated assumption.
2. **The certificate-of-residence class is swept and thin.** Nine Gurney-variant certificates in
   E 115 across the whole class; two name a John, both 1641, both Northamptonshire — the second,
   E 115/175/147, is new. Worth an explicit coverage/negative item: no certificate individuates any
   other John Gurney in England, and none survives for Francis G14.
3. **Two Buckinghamshire households not previously in any item.** A John Gourney litigating over
   property in Stoke Mandeville, Aylesbury and Walton 1621–25 (C 3/352/66); and John Gurney of
   Broughton in Bierton, husbandman, holding Weston Turville meadow 1592–1598/9 (Worcestershire
   705:349/12946/501417 and /501389). The second weakens the Stewkley→Bierton merge and ties the
   Weston Turville survivor into the Aylesbury-hundred tenantry.
4. **The Aylesbury Vale Gurneys were Pakington estate tenants and burgesses of Aylesbury from 1399.**
   The occupational argument gains context: Luke Gurney the Aylesbury tailor dealt in land directly
   with Sir Thomas Pakington. Worth a coverage node that Aylesbury Vale estate muniments are partly
   deposited outside the county.
5. **D-X_202 Marsworth names no John before 1660** — Thomas dead by 1615/6, his son and heir Henry,
   Elizabeth and her brother Richard, then Richard elder and younger. Closes part of an open action.
6. **Bedfordshire is an unswept adjacent county** — Gurney landholders at Hockliffe from 1590, five
   miles from Cheddington. Worth carrying as a named coverage gap rather than a silent one.

## 2026-07-28 (second pass) — the East Dereham Gurney family, and three corrections

**Bearing: substantial. Touches the register-extent items, the "why East Dereham" finding, the
colonial child roster, and the §11 rationale.**

Prose lives at
[`56-refactor-the-east-dereham-gurney-family.md`](../../research/people/g13-john-gurney/topics/identity/56-refactor-the-east-dereham-gurney-family.md),
[`57-refactor-colonial-attributes-audit.md`](../../research/people/g13-john-gurney/topics/identity/57-refactor-colonial-attributes-audit.md)
and
[`58-refactor-weymouth-reception-reweighed.md`](../../research/people/g13-john-gurney/topics/identity/58-refactor-weymouth-reception-reweighed.md).

What an increment must handle:

1. **PD 86/41's pre-1610 extent, read from the headings.** Only four annual returns survive before
   1610 — 1593-4, 1595-6, 1601, 1608-9 — with twelve missing between 1594 and 1608, **including
   1602-3, the year Margery Gurney's will was proved**. Any item treating the file as a continuous
   1593–1641 series is wrong. The existing 1611–15 loss item should be paired with this one: both
   hypotheses are shielded by register loss, and neither may draw comfort from the other's silence.
2. **A named East Dereham Gurney family, three generations before Francis's children.** Michael
   Gurney of East Dereham, m. Marion Waggestar, widow, at St Stephen's Norwich, 1543 (Rye); his
   widow Margery, the 1602–03 ANF testatrix already in the graph; his son **Arthur Gurney,
   gentleman, of Yaxham** — two miles from East Dereham — married by licence 1584, buying a Norwich
   house in 1591, suing for a £100 legacy out of freehold East Dereham tenements. **The court-choice
   reading that this was a humble household is wrong about the family**, and the graph's Margery item
   should stop being carried only as support for "why Francis settled there."
3. **No Gurney entry in any surviving pre-1610 return**, with per-return confidence: 1593-4 and
   1595-6 clean; 1608-9 read at 4×; **1601 a weak negative** (doubly flagged faded and soiled).
4. **Sarah is doubtful, and she never carried the weight assigned to her.** She is the only member
   of the roster with no primary record; Torrey's compendium has no Sarah Gurney marriage. But the
   naming custom counts son-slots and daughter-slots separately, so **a daughter cannot displace
   Richard from the eldest-son position** — the case file's "one colonial-side check now carries
   unusual weight" is a logical error and should be retired.
5. **Two unread naming predictions:** John Jr as second son puts the wife Mary's father at **John**;
   Peter as third son, his slot already spent, most plausibly honours an uncle.
6. **Isaac's parentage is inference only**, so the Cheddington argument's second leg is softer than
   its first is now firmer. The two do not compound.
7. **The tailor label stands** (primary, single attestation, user-affirmed); what weakens is the
   inference chain built on it. The 1663 inventory carries plough irons, oxen and grain and **no
   tailoring tools**, with an ordinary explanation.
8. **§11's asymmetry rationale is not supportable as written.** Two of John's own Weymouth
   land-neighbours came from Wendover and Ashton Clinton, three to five miles from the Gurney
   households; Weymouth had a documented Aylesbury-Vale stream and no Norfolk stream. The
   subordination of that observation was decided against a Candidate B resting on the East Dereham
   baptism, which no longer exists, and has never been re-run.

## 2026-07-28 (third pass) — matching by family, and a corrected overstatement

**Bearing: the §6.1 children matrix, Candidate C's parish, the variant registry, and one correction
to the second-pass entry above.**

Prose lives at
[`60-refactor-matching-by-family-not-by-man.md`](../../research/people/g13-john-gurney/topics/identity/60-refactor-matching-by-family-not-by-man.md),
with a correction folded into
[`56-refactor-the-east-dereham-gurney-family.md`](../../research/people/g13-john-gurney/topics/identity/56-refactor-the-east-dereham-gurney-family.md).

What an increment must handle:

1. **Correction to entry 2 of the second pass.** The local-family reading would **not** collapse
   Candidate B. Francis G14's own identity and geography are documented and independent of East
   Dereham (West Barsham 1581, London apprenticeship 1599–1606, Norwich from c.1606, Norwich marriage
   1611, St Benet Fink from 1619), and **Edward's 1610 and Marye's 1618 baptisms survived the
   deviation audit intact** — only John's vanished. What the local reading would remove is Candidate
   B's *Norfolk residence anchor*, not Candidate B. Any item drafted from the earlier phrasing needs
   this correction.
2. **Losing John's baptism relieved a chronological strain.** It no longer has to sit before the
   September 1611 marriage from a father bound apprentice until 1606. The friction now sits wholly on
   where a John born c.1603–1608 came from.
3. **The child-sequence negative is now England-wide and two-parent.** No John-and-Mary Gurney
   household in England baptises Mary, Richard and John 1627–1634. Replaces the parish-by-parish
   §6.1 statement.
4. **The Peter negative is widened to 1628–1652 England-wide — and may be irrelevant.** No Peter
   Gurney baptism of any kind in that span; but a c.1635–40 Peter may be American-born, in which case
   the rare-name discriminator does not bear on the English search.
5. **Candidate C's parish is contested.** FamilySearch indexes the eight-child family at **St Peter,
   Hertfordshire** (St Albans), FindMyPast at Berkhamsted. Two of the three supporting negatives were
   run against Berkhamsted. C stays eliminated on the father's age, which is immune.
6. **The variant registry has a structural blind spot.** All 87 registered forms are G-initial,
   though the audit proved this indexer confuses G and H. Tested clean for `Hurney`, but every
   "all variants" negative in the file covered only one initial.

## 2026-07-28 (fourth pass) — jurisdictions, and a Hertfordshire dead-end reopened

**Bearing: the Hertfordshire coverage negative, the Candidate C elimination, and the marriage-licence
coverage plane.**

Prose at
[`61-refactor-where-the-records-actually-live.md`](../../research/people/g13-john-gurney/topics/identity/61-refactor-where-the-records-actually-live.md);
R-23 first-pass results folded into
[`56-refactor-the-east-dereham-gurney-family.md`](../../research/people/g13-john-gurney/topics/identity/56-refactor-the-east-dereham-gurney-family.md).

What an increment must handle:

1. **The Hertfordshire probate "gap" is a finding-aid artefact.** The zero was in FindMyPast's
   published-probate-index dataset, which holds no Hertfordshire volume. The **Archdeaconry of St
   Albans** records at HALS (`ASA`) are catalogued to item level, and **`ASA/AR/8` covers 1610–1636**
   with a contemporary calendar of testators. Any item asserting Hertfordshire probate is unreachable
   needs restating.
2. **The candidate belt spans three archdeaconries in two dioceses** — Buckingham and Bedford in
   Lincoln, St Albans in **London** (confirmed by a 1641 London Archives probate describing the
   Archdeaconry of St Albans as being in the diocese of London). Worth a coverage node, because it
   governs where every licence, transcript and probate for these men lives.
3. **No south-Midlands marriage-licence series has ever been searched.** The repo's licence sweeps
   cover Norwich and the Bishop of London only. This qualifies the standing "no John Gurney + Mary
   marriage 1620–1635" negative, which is a statement about parish registers and register-derived
   indexes, not about licences.
4. **Arthur Gurney is absent from the Norfolk probate-and-marriage-licence-bond index entirely**
   (1371–1858, all spellings), so Rye's 1584 licence is an offline pull in the Norwich licence layer
   already documented at R-06, and his Great Dunham link stays his own hedge.
5. **A Tacolneston Gurney household enters the Norfolk comparator set** — George Gurney, parson of
   Tacolneston, "and his sons," with seven baptisms 1583–1611. Never assessed.
6. **Method, worth carrying as a coverage caution:** FamilySearch record search returns
   role-aggregated rows rather than baptism events, its parent parameters rank rather than filter,
   and its place parameter does not bind. Negatives asserted from it are weaker than they look.

## 2026-07-28 (fifth pass) — the marriage, swept England-wide

**Bearing: the §6.1 marriage negative, the Ackworth row, and the Farnham Royal household.**

Prose folded into
[`60-refactor-matching-by-family-not-by-man.md`](../../research/people/g13-john-gurney/topics/identity/60-refactor-matching-by-family-not-by-man.md)
§"The marriage, swept England-wide on a spouse-indexed instrument". New sources
`ancestry-england-select-marriages-9852` and `ancestry-england-select-births-christenings-9841`,
validation at `sources/validations/ancestry-england-select-igi-9841-9852.md`.

What an increment must handle:

1. **Exactly two John Gurney × Mary marriages exist in England before 1660** — Eythorne, Kent,
   6 November 1632, and Ackworth, Yorkshire, 6 June 1636. Both are already in the file. The negative
   should be restated at this strength: it is now a single England-wide test on a **both-parties-indexed**
   instrument, not a patchwork of county sets.
2. **A completeness re-run with the bride unconstrained finds no John Gurney marriage near 1630 with
   a blank spouse field**, so nothing was hiding behind unindexed brides.
3. **Ackworth is the sole unaccounted-for John × Mary marriage in England before 1660.** Its block
   should be restated on the better footing: daughter Mary married Daniel Shed at Braintree in 1647,
   so at a minimum marriage age of sixteen her parents married by about 1630 — a **primary** record,
   not a compiled birth estimate. A June 1636 marriage cannot produce her.
4. **John Gurney of Farnham Royal married Susan on 30 March 1629** — dating a household the
   Buckinghamshire deed sweep found only through a 1633 conveyance naming Susan as daughter of Oliver
   Cogeram. Small positive; worth carrying.
5. **Coverage caution to attach to any negative from collection 9852:** it does not contain the 1611
   Norwich Gurney–Rybett marriage, a direct measure of its incompleteness.
6. **Four England-wide negatives now stack**: no John+Mary household baptising Mary/Richard/John
   1627–34; no Peter Gurney baptism 1628–52; two John × Mary marriages before 1660, both accounted
   for; none with an unindexed bride. An English marriage of about 1626–1630 that leaves no trace in
   any of them is now the central fact of the English side.

## 2026-07-28 (sixth pass) — a false negative, and the search mode that hid it

**Bearing: the Stewkley statement, the §6.1 children matrix, and the reliability of every
"collections carry no record" negative in the file.**

Prose at
[`62-refactor-the-per-child-sweep.md`](../../research/people/g13-john-gurney/topics/identity/62-refactor-the-per-child-sweep.md);
correction applied in place at
[`52-refactor-bucks-herts-elimination.md`](../../research/people/g13-john-gurney/topics/identity/52-refactor-bucks-herts-elimination.md).

What an increment must handle:

1. **The Stewkley register-silence claim is false and must be retired.** "The Buckinghamshire
   parish-register collections carry no Stewkley Gurney record of any kind after 1614" was true of one
   dataset. Stewkley has Gurney baptisms at **1615 (two, one Anthony), 1616 (Anne), 1618, and 1626
   (Richard)**, the named ones all to a father **Robert** — the same household as the 1618, 1631 and
   1651 Stewkley probates. Any item asserting a Stewkley register silence, or citing probate as
   *correcting* one, is wrong on the premise.
2. **The reliability of a whole class of negatives drops.** FindMyPast has a cross-collection mode
   (`sid=999`, no `datasetname`) that searches every parish-baptism set at once and flags records
   *Exclusive* to it; the file's sweeps used the single-dataset mode. A "collections carry no record"
   statement is a claim about one transcription until re-run. Worth a coverage node rather than a
   silent fix.
3. **Richard and Mary swept England-wide (exact spelling):** Richard 1625–1635 = three records
   (Stewkley 1626 s. Robert, ×2 index rows; Luton St Mary 1635, father unread). Mary 1624–1634 = six
   records (London 1624; Norwich St Giles 1625 ×2; Kelham, Notts 1630; Linslade, Bucks 1633; Holborn
   1634). **Neither is a colonial match.**
4. **Those figures are floors, not counts** — the case file's own Hitcham *Mary Gurny* 1631 is absent
   from the national sweep because the index spells it `Gurny`. Any exact-spelling negative in the
   graph should carry that caveat.
5. **Matching threshold correction:** requiring Mary + Richard + John in one household is a filter
   built to return nothing against seventeenth-century registers. One child of the right name in the
   right window is the threshold; two is a strong hit.
6. **Bedfordshire is a materially unworked county** — 141 Gurney baptisms 1605–1645, households at
   Hockliffe, Luton, Clapham, Leighton Buzzard and Houghton Regis. **Hockliffe is now
   register-attested** (Alice, daughter of Thomas, 1619), corroborating the 1590 Requests suit over
   lands in Hockliffe, five miles from Cheddington.

## 2026-07-28 (seventh pass) — the per-child sweep completed on FindMyPast

**Bearing: the §1 baseline child list, the §6.1 children matrix, the Hitcham row, and the Cheddington
household.**

Prose at
[`62-refactor-the-per-child-sweep.md`](../../research/people/g13-john-gurney/topics/identity/62-refactor-the-per-child-sweep.md).

What an increment must handle:

1. **Peter and Isaac were probably born in New England.** No Peter Gurney-variant baptism anywhere in
   Great Britain 1627–1647; no Isaac 1632–1652 — wildcarded, all parish-baptism collections. Both
   first appear in colonial records. **The §1 baseline list of children "born in England" needs
   revising**: the English set is Mary, Richard, John and possibly Sarah. Also retires the Peter
   rare-name argument as an English search lever.
2. **Hitcham is the only 1-of-3 hit in England.** Across the whole sweep, exactly one baptism is to a
   father John with a colonial child-name in window — Mary Gurny, Hitcham, Bucks, 1631. That is a
   change in *relative* standing, not in strength: still a single indexed event with no mother and
   nothing before or after.
3. **Sweep totals, wildcarded, England-wide:** Mary 17, Richard 9, John 27, Peter 0, Isaac 0. Every
   other named hit resolves to a wrong father — Stewkley 1626 Robert, Norwich St Lawrence 1630
   William, Cheddington 1634 Isaac & Martha, Aston Abbotts 1637 Robert & Sarah, Wingrave 1624 and
   Toddington 1630 Thomas.
4. **The exact-vs-wildcard control belongs in the coverage plane.** Mary exact = 6, Mary `gurn*` =
   17, and the wildcard run is the one that contains the file's own Hitcham record. Every
   exact-spelling negative in the graph is a floor.
5. **Cheddington gains a son John** — John, baptised 14 December 1634, son of Isaac and Martha,
   absent from the Buckinghamshire county index and present in the national set. Sharpens the
   naming-unit point that Isaac and John were both live forenames in that household in the
   emigrant's generation.
6. **The Berkhamsted / St Albans provider split is confirmed from both sides** — FindMyPast
   Berkhampstead, FamilySearch St Peter (St Albans), same child, both surname spellings.

## 2026-07-28 (eighth pass) — child sweep closed, wills read from the inside, probabilities revised

**Bearing: §11 probability table and its rationale, the trade attestation, the Bury attribution, and
the coverage plane.**

Prose at
[`63-refactor-child-sweep-closed-and-reassessment.md`](../../research/people/g13-john-gurney/topics/identity/63-refactor-child-sweep-closed-and-reassessment.md).

What an increment must handle:

0a. **NEW NAMED CANDIDATE — C(ii), the younger Great Berkhampstead John.** Worked as *households*
   rather than counted as rows, the parent-name sweep splits Candidate C in two. The Great
   Berkhampstead baptisms to a father John Gurney run **1597 to 1637 — forty years**, which is not one
   man. **C(i)** (Hugh 1597 … Sara 1615) is born c.1570–75 and the case file's age elimination applies
   to him exactly. **C(ii)** (Jhon 1624, Richard 1626, Elizabeth 1629, Michaell 1631, Sarah 1634,
   Francis 1636/7) is **born c.1598–1602 and about 51 in 1653**, carries **three colonial child
   forenames**, loses two children in February–March 1639, and then **stops — with no Gurney burial at
   Great Berkhampstead at any date**. The case file eliminated the father and never assessed the son.
   Third same-name merge caught in this file after Aylesbury and Stewkley. Blocked by a missing Mary
   and by a burial negative that may be a coverage artefact. Prose at
   [`64-refactor-berkhamsted-reopened.md`](../../research/people/g13-john-gurney/topics/identity/64-refactor-berkhamsted-reopened.md).

0. **RETRACTION, same day — read first.** The claim "one baptism in the whole country has a father
   named John Gurney" was **false**. It came from a child-forename sweep on the stem `gurn*`. The
   correct instrument is a **parent-name** search (`sid=102`, `fatherfirstname`/`fatherlastname` — no
   medial "s" — with `_variants=true`), which returns **315 parish-baptism rows, Great Britain
   1611–1651**. Three errors compounded: a wrong parameter name generalised into a false rule; a
   wildcard stem mistaken for a variant sweep; and searching by child rather than by parent. In the
   tight 1625–1635 window the strict-spelling run gives 11 rows, all already carried — so the working
   conclusion survives there but is **not** established across the full range. Six unworked
   households surfaced: Tilsworth 1621, Luton 1640, Toddington (Gernne) 1631, Kinnersley 1649,
   Compton Abdale 1638, Ryton 1612. **Do not carry the pre-retraction numbers.**
1. **The §11 table is superseded — use only the final version.** Documented but never assembled
   22→**22%** and now the leading row; no record survives 24→**18%**; **Candidate B 18→11%**; **new
   row C(ii) at 9%**; Ackworth 6→**7%**; Cheddington 5→**6%**; Bucks/Herts/Beds group 3→**6%**;
   Hitcham 3→**4%**; A(1603) 5→**4%**; D 4%; Newgate 3%; Weston Turville 4→**3%**; **C(i) 1%**;
   Stewkley 1611 1%; other 1%. Sums to 100. Two earlier drafts were superseded the same day — ignore
   any version with assembled at 26% or 28%, or C at 1% undivided.
2. **The child angle is closed only for the child-forename axis.** Every named hit's father was read;
   of the baptisms bearing a colonial child forename, only Hitcham 1631 has a father John. The wrong
   fathers (Robert, William, Isaac, Thomas, Richard) are not plausible misreadings of John, so that
   escape is narrow. But the parent axis (item 0) is the open one.
3. **No will anywhere names a John Gurney as a son.** Every phrase form of "my sonne John Gurney"
   returns zero in FamilySearch Full-Text; the pre-1700 co-occurrence hits name no John Gurney as
   anyone's son. This is the strongest form yet of the "no document names him" negative and deserves
   its own item.
4. **No John Gurney is styled tailor in the full-text corpus before 1700** — eight hits, all 1729 or
   later. The colonial 1661/2 deed remains the sole attestation of the trade in existence.
5. **A Gurney at Bury St Edmunds in 1634** — "Juda Gurney" in a parishioner list, twenty years before
   anything the file holds for Bury, at the parish Banks named. Transcript level; forename unread.
6. **Coverage caution:** FamilySearch Full-Text has effectively no pre-1700 coverage for East Dereham
   or Yaxham (`"Michael Gurney" + Dereham` and `Gurney + Yaxham` both zero pre-1700). Yaxham stays an
   index-and-image job.

## 2026-07-28 (ninth pass) — method reset for the child inventory

**Bearing: method, not findings — plus one correction to the eighth pass and one to unit 61.**

Prose at
[`65-refactor-child-inventory-method.md`](../../research/people/g13-john-gurney/topics/identity/65-refactor-child-inventory-method.md);
catalogue at `research/people/g13-john-gurney/coverage/child-record-catalog.csv`.

What an increment must handle:

1. **A method now exists** for the child inventory: thirteen named sources (S1–S13), a
   record-instance catalogue with mandatory provenance, a household-shape discipline, a scoring
   rubric, a stopping rule, and eight self-checks at the plan layer. Worth a coverage/method node.
2. **Correction — the Berkhamsted parish "discrepancy" was an error of mine.** St Peter's *is*
   Berkhamsted's parish church; FindMyPast and FamilySearch mean the same place. **Unit 61's
   convergence argument (Candidate C's parish sitting inside the Archdeaconry of St Albans) was built
   on the misreading** and must be re-checked before it is carried into the graph.
3. **Three households from the March 2026 children matrix were never in the July sweeps** — Bishops
   Cleeve (Maria Gorne 1627, father John Gorne), Upton upon Severn (Mary Gurney 1629, **mother Mary,
   no father named**), Earsham (John Girney 1636, father John Girney). The prior repo layer is a
   source in its own right and was not read.
4. **Household shape is the soft joint in this whole file.** Three splits in one month — Aylesbury,
   Stewkley, Berkhamsted — each asserted rather than evidenced. Any graph item resting on a split
   household should carry the shape hypothesis explicitly and be marked conditional on it. **The
   Berkhamsted 9% is conditional on shape (b), father-and-son.**

## 2026-07-28 (tenth pass) — the Berkhamsted burials, and a candidate reduced

**Bearing: substantial. The C(ii) row, the §11 table and its rationale, three R-47 households, the
coverage plane, and the reliability of the parent-name sweep.**

Prose at
[`66-refactor-berkhamsted-burials-and-the-departure-gap.md`](../../research/people/g13-john-gurney/topics/identity/66-refactor-berkhamsted-burials-and-the-departure-gap.md),
with corrections applied in place at
[`64-refactor-berkhamsted-reopened.md`](../../research/people/g13-john-gurney/topics/identity/64-refactor-berkhamsted-reopened.md)
and an amendment to
[`65-refactor-child-inventory-method.md`](../../research/people/g13-john-gurney/topics/identity/65-refactor-child-inventory-method.md).
New source `findmypast-hertfordshire-banns-marriages` with validation; `findmypast-hertfordshire-burials`
notes rewritten. Catalogue now 100 rows.

What an increment must handle:

0. **RETRACTION — read first. The claim "no Gurney burial at Great Berkhampstead at any date" is
   false.** The parish holds **sixteen** Gurney-variant burials 1579–1643. Two compounding query
   defects produced the zero: `lastname=gurn*` does not reach the *Gourney* spelling the parish uses,
   and the burial set's place token is `Berkhamstead`, which neither `berkhampstead` nor `berkhamsted`
   matches. **Do not carry the departure-shaped-gap argument into any item.**
1. **C(ii) falls 9% → 4%, and the §11 table is revised again.** Documented-but-never-assembled
   22→**25%** and remains first; no-record **18%**; **B 11%**; Ackworth 6→**7%**; Cheddington
   6→**7%**; Bucks/Herts/Beds group **6%**; Hitcham 4→**5%**; **C(ii) 9→4%**; A(1603) **4%**; D **4%**;
   Newgate **3%**; Weston Turville **3%**; C(i) **1%**; Stewkley 1611 **1%**; other **1%**. Sums to 100.
   **This supersedes the eighth-pass table** — ignore any version with C(ii) at 9%.
2. **Great Berkhamsted held four contemporaneous Gurney households**, fathers John, Thomas, Edward and
   William — not one family and not two men. Any item resting on the two-man reading should carry that
   the split was derived from a father-filtered query, not from the parish. The father/son split does
   gain its first real evidence: a **Jhon Gourney buried 1620**, between C(i)'s last child (1615) and
   C(ii)'s first (1624).
3. **C(ii)'s children Elizabeth and Francis are buried at Berkhamsted**, 21 February and 9 March
   1638/9, matching the FamilySearch death dates to the day — and a **Richard Gurney was buried there
   28 June 1638**, who is either C(ii)'s son of 1626 or Thomas's son of 1635. The register image is the
   discriminator (new action R-49).
4. **Two hard negatives to carry:** no Mary Gurney baptism at Berkhamsted at any date under any
   spelling or any father, 1544–1888; and no John Gurney-variant marriage anywhere in Hertfordshire
   1600–1654.
5. **R-47 resolved.** **Bishop's Cleeve is not a Gurney household** — the surname is **Garne**, a
   settled Cotswold family baptising there 1629–1714; this also retires the Compton Abdale row.
   **Earsham closes** on a mother indexed "Alex" not Mary, plus the 1639 will. **Upton upon Severn is
   downgraded**, sitting inside a Gurney presence running 1582 to the nineteenth century.
6. **A material qualification on the 315-row parent sweep (R-42): the `sid=102` pool does not include
   every county set.** It returns zero for the Earsham household that the Norfolk county set carries
   with the father indexed. Its positive control passes, so this is coverage, not a query defect. Any
   England-wide negative from it needs a county-set pair.
7. **Coverage items worth their own nodes:** FindMyPast Norfolk Baptisms has **no Yaxham coverage
   before 1806**, so the R-23 test of Arthur Gurney's household has never actually been run;
   Worcestershire Baptisms does not cover Upton on Severn; Hertfordshire registers are widely
   defective 1643–1660 by the provider's own statement, which bounds every Herts burial negative in
   that window.
8. **Method amendment (S14).** Check C1 now covers `data/sources.json` notes as well as the research
   layer. Both the registry **and** `37-identity-assessment.md` already recorded the 1612 and 1620
   Berkhamsted Jhon Gourney burials, and a July sweep contradicted both without noticing.

## 2026-07-28 (eleventh pass) — the second instrument, and a negative downgraded to a floor

**Bearing: the §6.1 child negative and every "England-wide" statement resting on it; the Stewkley
household shape; the coverage plane.**

Prose at
[`67-refactor-freereg-second-instrument.md`](../../research/people/g13-john-gurney/topics/identity/67-refactor-freereg-second-instrument.md).
Catalogue now 113 rows, with source code **S8 represented for the first time** (13 rows).

What an increment must handle:

1. **The England-wide child negative is a floor, not a bound, and must be restated.** FreeREG holds
   **two Mary Gurney baptisms FindMyPast's England-wide sweep does not** — Epping, **Essex**,
   12 February 1625/6, and St Vedast Farringdon, London, 28 October 1624. FindMyPast holds Hitcham
   1631 and Berkhamsted 1626, which FreeREG does not. Neither instrument contains the other, so no
   sweep run on either is a statement about England.
2. **No candidate moves.** Both new Marys have wrong fathers — **Robert**, with a mother **Sarra**, at
   Epping; **Richard** at St Vedast. The Epping row is the one that mattered, because Essex is the
   colonial network's own county, and it closes on a named father rather than by inference.
3. **The C2 control fails on FreeREG**, informatively. Hitcham is in FreeREG's Buckinghamshire place
   index but returns no Gurney record for 1600–1700, and FreeREG carries no Berkhamsted Gurney
   baptism either. Any FreeREG negative is a statement about its covered parishes.
4. **The Stewkley household splits on its own evidence** — the fourth same-name or same-household
   merge caught in this file. **Robert Gurney married Joan Fenn at Stewkley on 10 July 1626**, six
   months *after* Richard was baptised there on 25 January 1625/6, so Joan is not Richard's mother and
   Robert had two wives. Also new: Walter Gurney × Joan Coalls, Stewkley 1620; Richd. Gowrney × Anne
   Liscombe, Stone 1625; a **second Stewkley Richard baptised June 1624**; Robert Gurney buried
   Stewkley 30 August 1631, matching the 1631 Stewkley probate.
5. **No John Gurney fathers anywhere in Buckinghamshire in FreeREG's holdings 1620–1649** — the only
   John rows are a Chesham baptism of 1600 and the Aston Abbotts child of 1637/8 already carried.
6. **The bishop's-transcript versus parish-register distinction is now demonstrated rather than
   asserted.** FindMyPast's Buckinghamshire Baptism Index is `D/A/T/` bishop's transcripts; FreeREG
   transcribes parish registers; the two return materially different Gurney event sets for the same
   county and window.
7. **Coverage items:** FreeREG's Buckinghamshire 1600–1700 run is capped at its 500-row display limit
   and must be re-sliced before any county negative; Name Soundex on "Gurney" collides with "Green"
   (both G650); the John arm exceeds FreeREG's hundred-second limit and has never run.

## 2026-07-28 (twelfth pass) — four instruments compared, and the sweep's own undercount

**Bearing: every per-child total in the file; the §6.1 negative; three catalogue fathers; the
Peter/Isaac American-born argument.**

Prose at
[`68-refactor-four-instruments-compared.md`](../../research/people/g13-john-gurney/topics/identity/68-refactor-four-instruments-compared.md),
with a same-pass correction folded into
[`67-refactor-freereg-second-instrument.md`](../../research/people/g13-john-gurney/topics/identity/67-refactor-freereg-second-instrument.md).
Catalogue now 124 rows across six of the thirteen method sources.

What an increment must handle:

0. **CORRECTION to the eleventh pass — read first.** That entry said FreeREG returned two Mary
   baptisms "FindMyPast does not hold". **False.** FindMyPast holds both — Epping 1625 in *England
   Births & Baptisms* and twice in *Essex Baptisms*, St Vedast 1624 in *Middlesex Baptisms* with a
   previously unknown sister **Anne Gourney 1626**. The records were missed by the **sweep**, not
   absent from the **source**.
1. **The July per-child sweep failed closed three ways, all in query construction.** The surname stem
   `gurn*` misses *Gourny/Gourney*; the **child's forename was an exact string** where registers give
   Marie/Marye/Maria; and the place keyword is a literal token. On the same instrument and window,
   `firstname=mar*` returns **54 rows against the sweep's 17**. **Every per-child total is a floor
   before provider coverage is even reached.**
2. **No index is complete, and the gaps do not coincide** — tested cell by cell. Ancestry 9841 lacks
   Hitcham 1631, Great Berkhampstead 1626, Stewkley 1626 and Aylesbury 1638; FreeREG lacks Hitcham,
   Berkhampstead and Aylesbury but holds Stewkley; FindMyPast and FamilySearch hold all four.
3. **Three catalogue fathers read for the first time, none a John** — Linslade 1633 = **Ezechiell**
   (FamilySearch); Kelham 1630 = **William** (FamilySearch and Ancestry); Bishop's Stortford 1629 =
   **Henry**, wife **Mary** (Ancestry). No catalogued Mary baptism in window now has an unread father.
4. **A new John-and-Mary household in Sussex**, from FamilySearch role rows (children Elizabeth and
   Grace) — **undated**, because the date range does not bind on role rows. New action R-53. Also
   unresolved: John + Margaret in Herefordshire, and a Warwickshire John household.
5. **Six further households new to the file:** Richard Gourny at St Vedast (Mary 1624, Anne 1626);
   Robert Gurney and Sarra at Epping, Essex; Henery Gurney and **Mary** in Middlesex; Edward
   Gurnel/Gurnet and Winefret at Allhallows London Wall (Mary 1627, Richard 1628); Thomas Gurney and
   Elizabeth at St Martin in the Fields; William Gurner and Marlin at Buckland, Kent.
6. **The Peter and Isaac zeros are put on hold.** Both are exact-forename, single-provider results and
   currently carry the case-file claim that those two children were American-born. That claim must not
   be published until the wildcarded re-run (R-54).
7. **Technique worth a method node:** FamilySearch's role-aggregated rows are a **household index** —
   a John Gurney query returns 87 father-rows per hundred, 18 with a wife Mary — but they carry no
   date and the date filter does not bind on them, so each must be opened individually.
8. **Provider disagreements to carry:** Kelham 1630 is 11 October on Ancestry and 27 October on
   FamilySearch; Upton on Severn 1629 is 13 September on Ancestry and 7 September in the March matrix.

## 2026-07-28 (thirteenth pass) — the FreeREG sweep completed, and a Sussex lead closed

**Bearing: the English-side child negative at its strongest form; four new father-John households;
two corrections to the eleventh/twelfth passes.**

Prose folded into
[`67-refactor-freereg-second-instrument.md`](../../research/people/g13-john-gurney/topics/identity/67-refactor-freereg-second-instrument.md)
§"The complete sweep". Raw capture at `sources/intake/archive/g13-july-2026-sweeps/freereg-g13-sweep-2026-07-28/`
(585-row TSV, per-query log). Catalogue now **147 rows** across seven of the thirteen method sources.

What an increment must handle:

1. **The strongest form yet of the English negative.** Twenty surname spellings × three event types ×
   all counties × 1600–1660 = sixty FreeREG queries, **585 records captured with parents**. **Not one
   has both a father John and a mother Mary** — 38 father-John rows, 31 mother-Mary rows, nil
   intersection. Bounded by FreeREG's parish coverage, which excludes Hitcham and Great Berkhamsted.
2. **FreeREG's non-soundex surname matching is EXACT** — a *Gurney* query returns only rows spelled
   `GURNEY`. A single-spelling search on this instrument sees roughly a quarter of the record set.
   Worth a coverage/method node: variant spellings are mandatory here, not optional.
3. **Four father-John households new to the file**, all eliminated on wife's name or continuing
   residence: **Lamport, Northamptonshire** (John + **Anne**, seven children 1630–1640 — the largest
   unrecorded father-John household found this month); **Longdon, Worcestershire** (John + Dorothy,
   then + Isabell, to 1641); **Oldswinford, Worcestershire**; and **Earsham extended** — a *first* son
   John baptised 1635 who must have died, plus Henry 1638 to a mother **"Ales"**, which FindMyPast
   indexes as "Alex". Two instruments now agree the Earsham wife is Alice, not Mary.
4. **CORRECTION to the eleventh pass.** The June 1624 Stewkley Richard is **not** a reused name in
   Robert's household — his father is **Walter**, mother **Joan**, tying him to the Walter Gurney ×
   Joan Coalls marriage at Stewkley in 1620. Two Stewkley households, not one man reusing a name.
5. **CORRECTION to the Denton row (CR-034).** The father conflict resolves **against John**: FreeREG
   independently reads **Josias**, mother Rachell, agreeing with Ancestry 61045's *Josiah* against
   FindMyPast's *John*. Denton should stop being carried as a father-John household.
6. **The Sussex John-and-Mary lead is closed.** Opened, it is **Horsham, Sussex — Elizabeth christened
   11 June 1702 and Grace 5 August 1704**. It looked live only because FamilySearch's date range does
   not bind on role rows.
7. **Method disclosure worth carrying:** the sixty-query sweep was issued by script against FreeREG's
   anonymous public form and record endpoints rather than by driving the browser, because of the
   volume of detail pages. No login and no paywalled content. The headline counts were re-derived
   independently from the raw TSV rather than accepted from the run's own summary.

## 2026-07-28 (fourteenth pass) — Essex tested, and a surname confusion in the candidate pool

**Bearing: the Essex reception-network argument, the Maldon branch, sixteen catalogue rows, and every
published Gurney-variant total.**

Prose at
[`69-refactor-essex-tested-and-the-surname-confusion.md`](../../research/people/g13-john-gurney/topics/identity/69-refactor-essex-tested-and-the-surname-confusion.md).
Method amended with a new check C5a. Catalogue now 153 rows, 16 reclassified.

What an increment must handle:

0. **CORRECTION applied 2026-07-29 — items 1, 3 and 4 below were written on a claim that has been
   retracted. Read the fifteenth-pass entry with this one.**
1. **Essex has now been swept for the first time, and it is OPEN, not closed.** The county the colonial
   associations point at hardest — Tyng of Stanford Rivers, Shed of Finchingfield, Braintree Essex,
   Browning of Maldon — had **never been searched**, and "Ongar" appeared nowhere in `research/`.
   **Finchingfield holds 1 Gurn\*-variant baptism in its whole run and Stanford Rivers none** — so the
   two parishes the colonial evidence names directly are empty. **But the Epping – North Weald Bassett
   – Fyfield triangle four miles from the Tyng estate holds a Gurney-plausible cluster right through
   the window, including Richard Gurnat, Epping 1616, to a father JOHN.** The original conclusion
   ("no Gurney household anywhere in Essex in the window") depended on excluding the Gurnat/Gurne/
   Gurnard rows as other surnames, and that exclusion is withdrawn. **Next step is register images for
   Epping and North Weald Bassett, not more index searching.**
2. **The Maldon branch gains register-level corroboration.** *Gourn\** in Essex is concentrated at
   **Maldon, St Mary the Virgin**: Francis Gourney and Ann, children John 1655, Jane 1656, Francis
   1657, George 1659, **Thomas 1660**, Charles 1662, Richard 1664, Francis 1665, Anna 1666, Henry
   1667. That supplies a John and a Thomas matching the bachelor John of Maldon (d. 1681) whose
   administration went to brother Thomas — a claim that had rested on Daniel Gurney and Bernau. Starts
   1655, so it bears on G14's descendants, not on the colonial John. New action R-57.
3. **RECLASSIFICATION — several "Gurney variants" are distinct surnames with their own lineages.**
   *Garne* (Glos), *Gurnett/Gurnat/Gurne* (Essex), *Gurnard* (Herts/Essex), *Gurnel/Gurnell* (London),
   *Gurner* (Kent/Sussex/Hants/Worcs). **Epping is the demonstration**: one family indexed Gurnat 1616
   → Gurne 1622 → **Gurney 1625** → Gurnet 1649 → Gurnett 1724, baptising continuously to 1726. The
   1625 row is the "Marie Gurney, Epping" that the eleventh and twelfth passes treated as a strong new
   Essex candidate. **It is a Gurnett.** Sixteen catalogue rows reclassified.
4. **Consequence for the graph: every published Gurney-variant count needs a caveat**, because the
   87-form variant registry is right for discovery and wrong for counting. New action R-56. Note the
   tension with the D8 finding that an indexer misreads H as G — breadth is still needed for
   discovery; what must change is how counts are reported.
5. **New method check C5a** — settled spelling plus parish continuity as the test of whether a variant
   hit belongs to the surname at all.

## 2026-07-29 (fifteenth pass) — the variant retraction, and what it changes

**Bearing: the fourteenth-pass Essex conclusion, sixteen catalogue rows, the method, and how every
variant negative in the file should be read.**

Prose folded into
[`69-refactor-essex-tested-and-the-surname-confusion.md`](../../research/people/g13-john-gurney/topics/identity/69-refactor-essex-tested-and-the-surname-confusion.md);
method checks C5a and C5b rewritten in
[`65-refactor-child-inventory-method.md`](../../research/people/g13-john-gurney/topics/identity/65-refactor-child-inventory-method.md).

What an increment must handle:

1. **RETRACTION. "Several Gurney variants are other surnames" was conjecture, not a finding.** It
   rested on five Epping index rows spanning three or more generations, with no register image read,
   assuming a single family and letting a spelling of 1724 govern the reading of an entry of 1625.
2. **Gurnard is specifically rehabilitated, on the repo's own corpus.** The Heralds' Visitation of
   London 1634 (Harleian MS 1476, in Daniel Gurney, *Record* Pt III p. 533) records letters patent of
   26 July 1633 to **"Richard Gurny, *alias* Gurnard, Sheriff of London"**, and **"Burton Gurny,
   *alias* Gurnard, descended from the Gurneys of Kendall"**. Reinforced by the Norfolk line's own
   **canting gurnard-fish crest**, borne by Thomas Gournay I before 1465. Gurnard is a Gurney form
   with formal standing.
3. **Variant plausibility is a per-record weight, not a surname class.** Gurne/Gurn high;
   Gurnard/Gurnat moderate-high; Gorne/Garne/Gernne moderate; Gurnett/Gurnel/Gurner lower —
   **and lower is never exclusion**. The sixteen "reclassified" catalogue rows are restated as
   weighted; none removed.
4. **Counting is the wrong metric.** The object is an individual record matching a corner of the
   colonial shape, not a total of Gurney baptisms. New method check **C5b**. Any graph item phrased as
   a variant *count* should be restated as a match/partial-match statement.
5. **Consequence for Essex — the fourteenth pass inverts.** See that entry's item 0.

## 2026-07-29 (sixteenth pass) - Weymouth first, a withdrawn Norfolk reading, and the West Country swept

**Bearing: the corridor argument, the migration-network unit, and how compiled-claim corroboration
should be handled.**

Prose at
[`70-refactor-weymouth-first-and-the-ludham-thread.md`](../../research/people/g13-john-gurney/topics/identity/70-refactor-weymouth-first-and-the-ludham-thread.md).

What an increment must handle:

1. **Weymouth, not Braintree, is the right place to work association evidence for origin.** John's
   first colonial record is the Weymouth petition of 30 May 1641; every Braintree tie post-dates it.
   And the petition **names the men he was with**, which no Braintree record does. Men named beside
   him outrank **land-neighbours**, who were acquired after arrival by where a parcel lay.
2. **RETRACTION within this pass. A Norfolk origin for James Ludden is withdrawn.** It was produced by
   matching an **unsourced** FamilySearch tree ("Little Plumstead, Norfolk") to a Ludham household
   found at that very parish - corroboration by construction, the R1/R2 failure of the deviation audit
   in miniature.
3. **Neither competing claim is sourced.** William B. Scarpelli's 2022 Town of Hanover research paper
   says "Born in 1611 in Dorsetshire" - and **that sentence carries no footnote**; the notes around it
   cover the settlement's name and the marriages. The date most likely descends from the title of
   Wallace Ludden's 1971 compiled genealogy. Two compiled claims, two counties, no source either side.
4. **What is documented leans West Country**: arrival at Wessagusset **September 1623 with the Robert
   Gorges company**; later wife **Alice Kinham** on **Rev. Joseph Hull's company out of Weymouth,
   Dorset, 30 March 1635**. **Net: Ludden gives no support to the Norfolk corridor** - the opposite of
   what this pass first concluded.
5. **The West Country has now been swept for Gurney households - the first time - and it is empty of
   shape-matches.** 1610-1650: **Somerset 2 baptisms**, **Dorset 2**, both Gurnard at **Owermoigne**,
   seven miles from Weymouth Dorset. The Owermoigne household runs fathers **Martin, Nicholas, Robert**
   across 1574-1625, **no John, no colonial-name child**. Worth a coverage node: the corridor the
   Weymouth reception evidence made live is now closed on record.
6. **Instrument note:** `datasetname=somerset+baptisms` / `dorset+baptisms` with `yearofbaptism`
   returns zero **even on a Smith control** - broken for those counties; use the cross-collection route
   with `keywords=<county>`.

## 2026-07-29 (seventeenth pass) - burials as the elimination instrument; two rows move

**Bearing: the §11 table, §8.7's framing, and the reliability of every "unaccounted for" verdict.**

Prose at
[`71-refactor-burials-as-the-elimination-instrument.md`](../../research/people/g13-john-gurney/topics/identity/71-refactor-burials-as-the-elimination-instrument.md).
Catalogue now 178 rows.

What an increment must handle:

1. **Reframing worth its own node: §8.7 leans on "no probate in either tier", and probate is the wrong
   instrument.** Probate exists only for men with property worth proving. The record that individuates
   an ordinary man is his **burial** - and burial coverage varies sharply parish by parish, so every
   burial negative needs a common-surname control in that parish.
2. **A(1603) Stewkley falls 4% -> 2%.** The case file states he has "no burial". **False.** The
   Buckinghamshire Burial Index records **John Gurney buried at Stewkley 21 September 1615**
   (bishop's transcript **D/A/T/160**), with no age and no relationship, inside a cluster with
   Elizabeth 1614, Martha 1615 and Robert 1618. It is either this man at twelve or his father; the
   parish is demonstrably covered. **One image (R-63) resolves it to elimination or survival.**
3. **Hitcham falls 5% -> 4%.** Its "no burial, no probate" support is **hollow**: the parish has no
   seventeenth-century burial coverage in that index at all - the Smith control returns a single
   burial dated **1827**. Being "unaccounted for" is informative only where the records would have
   accounted for him. What the row still rests on is unchanged and real: the single Mary baptism to a
   father John, still the only such record in England.
4. **Weston Turville holds at 3% and its negative is now genuine** - the parish IS covered, with
   Gurney burials at 1621, 1625 and 1633 twice, and the 1627 father is not among them.
5. **Ackworth holds at 7%, with both sides now sharper.** The departure gap is **controlled for the
   first time**: 170 Smith burials in the parish, **zero** Gurney burials, and the entire Gurney
   presence is two records. But the household is thinner than the file states - the **1637 baptism
   names no father and no mother**, so its attachment to the 1636 marriage is inference, and
   **"John Thomas Gurnoe" may be "John son of Thomas Gurnoe"**, the artefact already caught at
   Toddington. New action R-64.
6. **A conditional worth carrying:** the file's block on Ackworth - daughter Mary's 1647 marriage
   putting her parents' marriage by about 1630 - is decisive **only if the 1636 marriage was John's
   first**. The record gives no marital status. Labelled speculation, but the block is presented as
   conclusive and it is not.
7. **Cheddington's burial question is unanswerable from any index** (two now tried, both with
   unproven window coverage) and needs the parish register. **Candidate D's St Augustine Watling
   Street burial search is not reachable by keyword** in the FMP burial corpus and must be routed
   through Boyd's London Burials or LMA.
8. **The Buckinghamshire marriage tested from BOTH sides, and it is empty.** Every John Gurney
   marriage in the county 1572-1704: Alice 1572, Elizabeth 1573, **Alice 1628, Susan 1629, Elizabeth
   1630, Avis 1638, Rebecca 1640**, Mary 1663, Susannah 1691, Anne 1699/1700, Elizabeth 1704. **Five
   in the emigration window, not one bride a Mary.** From the bride side the earliest Mary to marry a
   John Gurney in the county is **Mary Kidgell, Edlesborough, 1663** - two years after the colonial
   Mary died at Braintree. **Three independent instruments now agree** the colonial marriage is not in
   the Bucks/Herts belt (Ancestry 9852 England-wide: two John x Mary marriages before 1660; Herts
   county set: no John Gurney marriage 1600-1654). It tightens rather than eliminates, since grooms
   married in the bride's parish - which is what R-00c and R-33 exist to test. **Cheddington 7 -> 6,
   Bucks/Herts/Beds group 6 -> 5.**
9. **Table now:** assembled **30**, no-record 18, B 11, Ackworth 7, Cheddington **6**, Bucks/Herts/Beds
   group **5**, Hitcham **4**, C(ii) 4, D 4, Newgate 3, Weston Turville 3, **A(1603) 2**, C(i) 1,
   Stewkley 1611 1, other 1. Sums to 100.

## 2026-07-29 (eighteenth pass) - the parent-name sweep completed

**Bearing: closes R-42 and R-59; converts the central English-side claim from assertion to bounded
statement.**

Prose at
[`72-refactor-the-parent-sweep-completed.md`](../../research/people/g13-john-gurney/topics/identity/72-refactor-the-parent-sweep-completed.md).
Raw capture at `sources/intake/archive/g13-july-2026-sweeps/fmp-parent-sweep-2026-07-28/` (598 rows, per-query log).

What an increment must handle:

1. **The parent-name sweep is complete for 1615-1649** - every year sliced individually because
   `page=2` is broken on that mode, strict and variant-expanded, **598 rows**.
2. **The statement it licenses, which replaces the file's fragmentary version:** across Great Britain
   1615-1649, **exactly one baptism to a father named John Gurney gives a colonial child forename in
   window and belongs to no otherwise-accounted-for household - Mary Gurny, Hitcham, 22 January
   1631.** In the 1626-1636 band the sweep returns 149 rows, 68 with a Gurney-cluster surname, and
   every one resolves to a household already carried.
3. **It remains a FLOOR, for three stated reasons:** the `sid=102` pool does not reach every county
   set (it misses the Norfolk FHS transcription and with it Earsham); no single index is complete;
   and five year-slices lost 1-7 rows each to the pagination defect.
4. **No probability row moves.** A completed enumeration returning no new candidate is a result. It
   leaves Hitcham carrying the only unexplained colonial-name child in the country, on a row whose
   other support was shown the same day to be a coverage artefact.
5. **Three households new to the file**, none disturbing: Edward Gourney, Aylesbury 1628 (a child to
   a father John a decade before the 1638-53 Aylesbury run, worth a look against A(i)'s April 1628
   Bierton marriage); Johes. Gurner, Bromsgrove 1634; Ellinor Gornie, Rochester 1636.
6. **Two unreadable-surname rows worth naming rather than dismissing** - "G. John", Norton,
   **Suffolk**, 1635 (corridor county, and FindMyPast has no Suffolk baptism set) and "G?th John",
   Wooburn, **Buckinghamshire**, 1632. Both are image questions. The rest of the unreadable tail is
   dominated by Cornwall Baptisms, where surnames are routinely unindexed.

## 2026-07-29 (nineteenth pass) - the funnel closed on births and marriages; the unassembled row split

**Bearing: substantial. The §11 table gains a row and loses thirteen points off its leading one; the
marriage and mother axes close; the child inventory is finished on the axes that stand alone.**

Prose at
[`73-refactor-the-funnel-closed-and-the-unassembled-row.md`](../../research/people/g13-john-gurney/topics/identity/73-refactor-the-funnel-closed-and-the-unassembled-row.md).
Catalogue now 192 rows.

What an increment must handle:

1. **The marriage arm is finished on a fifth instrument.** FreeREG's record URLs carry **both parties'
   names in the slug**, so its 178 marriage rows yield 97 unique Gurney-cluster events 1615-1645
   without opening a record. **Every John Gurney-cluster groom 1600-1660 is now named with his bride,
   and not one marries a Mary** - the only John x Mary being John *Garne* x Mary White, Brigstock,
   1659. The negative is sharper than "none found": **nine Gurney men married Marys** in the same
   holdings, so it is specifically the Johns who have none.
2. **New from the marriage arm:** the **Earsham marriage is dated - John Girney x Elizabeth Singler,
   9 October 1632**, confirming the wife is not Mary from a second direction; **Longdon,
   Worcestershire has two John marriages** (Fraunces Price 1602, Dorothy Tuffley 1625) plus a third
   wife Isabell by 1639, so that household is a father and son; and a **John Gurney marriage at
   Greenwich, Kent, 27 October 1642** is new.
3. **The mother axis was swept for the first time**, which is odd given a wife named Mary is one of the
   firmest facts about the household. Result: **across Great Britain 1620-1640 exactly one Gurney
   household is recorded with a father John AND a mother Mary - Eythorne, Kent**, already eliminated.
   The Holborn household does not survive the father filter.
4. **THE ROW SPLIT - the important structural change.** *Documented but never assembled* was carrying
   two different propositions. Split them: **assembled 30 -> 17**, and a **new row, "documented but in
   a source or class not yet searched", at 9**. The second is evidenced, not speculative - the parent
   pool misses whole county sets (proven: it returns neither Lamport, Northants nor Earsham, both held
   by FreeREG), there is no FMP Suffolk baptism set, Hitcham has no seventeenth-century burial
   coverage, the south-Midlands licence series is unsearched, East Dereham's 1611-15 returns are lost,
   Hertfordshire registers are defective 1643-60.
5. **Why the assembled row FELL rather than grew.** It had been raised on every merge defect found -
   Candidate A, Stewkley, Berkhamsted, Denton, Toddington, Linslade, Kelham, Bishop's Stortford -
   **but every one was found AND resolved, which drains the row rather than filling it.** With the
   father axis enumerated to completion, the mother axis swept, and the marriage settled on five
   instruments, the searched corpus holds exactly **two** unaccounted-for households in the window,
   and both already carry named rows. There is no third thing for a residue to be.
6. **Ackworth 7 -> 9 and Hitcham 4 -> 5**, not on new supporting evidence but because the funnel closed
   around them: Ackworth holds the only unaccounted-for John x Mary marriage in England before 1660,
   Hitcham the only unaccounted-for colonial-name child to a father John in Britain. Both remain
   single-record candidates with real blocks. **Candidate B does NOT gain** - it would benefit from an
   emptied corpus only through its absence-explaining auxiliary, which the file's own rule forbids.
7. **Best partial match found, and it fails:** **John GURLEY and Mary at St Clement Danes,
   Westminster** - Eliz 1627, Ellynor 1628, Alexander 1629, **Mary 1631**, **Sara 1633**, father John
   and mother Mary on all five, confirmed on the county set. Four corners of the signature including
   the hard 1631 bound. **Fails on the child set regardless of surname** - no Richard, no John Jr,
   three children with no colonial counterpart. Recorded as weighted, not promoted.
8. **Table now (16 rows):** no-record **19**, assembled **17**, B 11, Ackworth **9**, not-yet-searched
   **9**, Cheddington 6, Bucks/Herts/Beds group 5, Hitcham **5**, C(ii) 4, D 4, Newgate 3, Weston
   Turville 3, A(1603) 2, C(i) 1, Stewkley 1611 1, other 1. Sums to 100. **Three record-state rows now
   hold 45% between them and the leading row is not a person.**

## 2026-07-29 (twentieth pass) - every candidate scored against the shape

**Bearing: the whole candidate roster, the scoring rubric, and one row move. Closing analytical pass
of the July 2026 refactor.**

Prose at
[`74-refactor-candidates-scored-against-the-shape.md`](../../research/people/g13-john-gurney/topics/identity/74-refactor-candidates-scored-against-the-shape.md);
rubric corrections folded into
[`65-refactor-child-inventory-method.md`](../../research/people/g13-john-gurney/topics/identity/65-refactor-child-inventory-method.md)
new section 4a. Catalogue now 196 rows.

What an increment must handle:

1. **A 15-attribute shape specification now exists** (surname, the three children and their dates, a
   father John, a mother Mary, the father's age, two alternative marriage windows, a grandfather
   Richard, migration region, Weymouth connection, the tailor trade, and a 1636-39 push event). Every
   non-zero candidate is scored against it in a matrix. Worth carrying as the evaluation frame.
2. **THE STRUCTURAL FINDING - the candidates fall into two disjoint families and no candidate is in
   both.** *Documented households with the wrong shape*: C(ii), Hitcham, Ackworth, and the eliminated
   Eythorne all have a father, sometimes a mother, and children with dates, but the wrong children.
   *Documented men with no household at all*: Candidate B, Cheddington 1608, A(1603), Candidate D and
   Weston Turville each score zero on the four child attributes. **The emigrant needs a man of the
   right age AND his household; every candidate supplies one half.** That is a stronger argument for
   the record-state rows than anything the file had: the man's own baptism and his household's
   baptisms are probably not in the same searchable place.
3. **Hitcham falls 5% -> 3%; no-record rises 19% -> 21%.** Hitcham is a true singleton with **no mother
   recorded**, and **John Gurney married Susan at Farnham Royal on 30 March 1629** - five miles and
   twenty-two months away - with **no child recorded to a John-and-Susan Gurney household anywhere
   before 1770**, and no John Gurney children at Farnham Royal itself. A documented alternative
   parentage whose mother is not a Mary.
4. **Attribute-level notes worth carrying:** C(ii) is strongest on the household core and on the
   1636-39 push event (two children buried within three weeks in Feb-Mar 1638/9) but has **no Mary in
   the parish at any date**; Ackworth is the **only** candidate scoring father-John and mother-Mary
   together, and the second-marriage window is its strongest card; Weston Turville is quietly best on
   the contextual attributes (age, a Weymouth settler parish two miles off, and a Gurney tailor who
   died in the parish in 1633); Candidate B is **contradicted** by the grandfather-Richard attribute,
   its thesis being a father Francis.
5. **Five scoring corrections adopted into the rubric (method 4a):** ~~Margaret is **not** a variant of
   Mary~~ **- RETRACTED in pass 20; Margaret is a substantial soft hit on the mother axis** - Molly/Polly are anachronistic; Mary's date is a **primary bound (born by 1631)** while
   Richard c.1630 and John c.1633 rest only on compiled estimates and must weigh less; Peter, Isaac
   and Sarah must **not** be scored against a candidate; add a departure attribute **with its parish
   coverage control attached**; add a surplus-children penalty.
6. **Table now (16 rows):** no-record **21**, assembled 17, B 11, Ackworth 9, not-yet-searched 9,
   Cheddington 6, Bucks/Herts/Beds group 5, C(ii) 4, D 4, Newgate 3, Weston Turville 3, **Hitcham 3**,
   A(1603) 2, C(i) 1, Stewkley 1611 1, other 1. Sums to 100. **Record-state rows now hold 47%.**

## Pass 20 - 29 July 2026: the Margaret retraction, R-66 closed, three loose ends dated

Unit `75-refactor-margaret-county-sets-and-loose-ends.md`.

1. **Margaret is admitted to the mother axis as a substantial soft hit, retracting the rule adopted
   only one pass earlier.** The claim that "clerks did not swap them" was an unevidenced assertion
   about scribal behaviour - the same error as the surname-variant retraction of unit 69, one field to
   the left. The mechanism that defeats it: `g` and `y` carry near-identical looping descenders, and
   *Margaret* was routinely contracted to `Marg.` or `Mgt.`, so the distinguishing letter is the
   ambiguous one and **the transcription chain corrupts in both directions**. Method 4a bullet 2 and
   unit 74 feedback point 1 both rewritten. The John family on the father axis likewise includes
   **`Jone` and `Joan`**, which these indexes demonstrably use for a contracted Johannes.
2. **The Margaret axis then searched, and it is empty.** FreeREG (585 rows, five Margaret-family
   mothers, none to a father John), the eight county sets (705 rows, seven Margaret mothers, none to a
   father John at any date), and the national parent search (8 rows, not one a genuine Gurney) - the
   last **with a passing Eythorne positive control on the identical query shape**. No candidate score
   changes, but the reason is now evidence rather than assertion.
3. **R-66 executed and empty.** Eight county sets, six surname stems, 705 rows, 68 in-window with a
   father named, **no new father-John household with a mother Mary or Margaret**. The coverage row
   falls 9 to 5; its residue is now listable (Suffolk has no FMP set; Essex, Middlesex and
   Huntingdonshire have no marriage set; Berkshire marriages unrun; nine queries capped).
4. **Three undated FamilySearch role-row households dated on a second instrument and all eliminated:**
   Sussex John x Mary at Horsham **1704** (unit 68 had called it "the single most important loose
   end"), Herefordshire John x Margaret at Stoke Lacy **1687**, Warwickshire John at Coleshill
   **1710**. Three for three outside the window by six decades or more - now a scoring rule: an undated
   role row is not evidence of an in-window household until dated elsewhere.
5. **A claim corrected:** "across Great Britain 1620-1640 exactly one Gurney household has a father
   John and a mother Mary" was overstated. A second appears at the outer edge of the variant scale -
   **John and Mary Gurley of Westminster**, children Eliz 1627, Ellynor 1628, Alexander 1629, **Mary
   1631**, Sara 1633, record stopping 1633. Right parents, right eldest daughter, right departure
   pattern; **no Richard and no John**, and `Gurley` needs an `n`-to-`l` confusion.
6. **Epping enters at 3% on a naming argument:** its Gurn- line **alternates John and Richard across
   three generations** (Richard 1616 to a father John, Richard 1649 to a father Richard, John 1654 to a
   father John), in the Great Migration's own county. It is the first candidate that is mostly *untested*
   rather than *absent*.
7. **Two instrument defects, one retroactive.** A year bound and a place keyword **cannot be combined**
   in a single-dataset query - proven by 349 Smith baptisms at Epping with no year bound against
   **zero** for 1616, in a set holding a 1616 Epping baptism. Every negative resting on both parameters
   is **void** (R-71). `sortby` is accepted and ignored. Consequence: **Ackworth cannot be tested on
   FindMyPast at all** and holds at 9% as untestable rather than weakened.
8. **Table now (18 rows):** no-record **22**, assembled 17, B 11, Ackworth 9, Cheddington 6,
   not-yet-searched **5**, C(ii) 4, D 4, **Epping 3**, Newgate 3, Weston Turville 3, Hitcham 3,
   Bucks/Herts/Beds group **3**, A(1603) 2, **Gurley 2**, C(i) 1, Stewkley 1611 1, other 1. Sums to
   100. Record-state rows hold **44%**.

## Standing note

**Resolved 30 July 2026.** The July 2026 refactor units, numbered `50-` through `75-` under
`research/people/g13-john-gurney/topics/identity/`, have been **promoted into the permanent identity
sequence and retained as the working record**. Their findings now live in `30-` to `39-`, which are the
current account:

| Unit | Scope |
|---|---|
| `30-candidate-overview.md` | the shared test, the three procedural corrections, the candidate landscape |
| `31-candidate-a-aylesbury.md` | Candidate A split into A(i)/A(ii), and the whole Buckinghamshire cluster |
| `32-norfolk-parentage.md` | Candidate B |
| **`33-berkhamsted-candidates.md`** *(new)* | C(i) and C(ii), split out of the assessment unit |
| `34-london-draper.md` | Candidate D |
| `35-candidate-ackworth.md` | Ackworth |
| `36-other-eliminations.md` | the variant scale, Essex, the West Country, the cleared field |
| `37-identity-assessment.md` | the assessment and the 18-row probability model |
| **`38-the-shape-and-the-two-families.md`** *(new)* | the 15-attribute shape, the matrix, the disjoint-families finding |
| **`39-child-inventory-method.md`** *(new)* | the method governing any further round |

The `50-`–`75-` units keep their own correction and retraction trails, which belong to the research
layer, and their headers now say so. **None of them is in the graph, and neither are `33-`, `38-` and
`39-`** — those three are new topicIds (`g13-identity-candidate-c`, `g13-identity-shape-matrix`,
`g13-identity-inventory-method`) that the increment must create. The prose markers carried in `30-`–`37-`
are unchanged in identifier but several now sit over rewritten passages, so **expect restatements, not
only additions**, and derive live RI/PM ids from the database at authoring time.
