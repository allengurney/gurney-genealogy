<!-- WIP refactor unit, July 2026. Method document, not a findings document. Not yet in the G13 context
     graph. Graph-bearing content is tracked in sources/intake/g13-graph-breadcrumb.md. -->

# Method for a complete child inventory — sources, catalogue, scoring, and stopping rule

## Why this exists

The July 2026 child search failed three times in a row. Each failure was corrected mechanically and
the work continued; the method was never rebuilt. The failures were:

1. A sweep by **child forename on one surname stem** (`gurn*`) in one provider, reported as an
   England-wide result. It missed households indexed as Gernne, Garne, Gourney, Gowrne, Greney.
2. A **wrong parameter name** (`fathersfirstname`) generalised into "no parent search works" — and
   written into the search skill as a durable rule. The correct search returns 315 rows where the
   flawed one implied one household.
3. **Counting rows instead of assembling households.** The Berkhamsted split was visible in data
   already in hand and was not seen until it was pointed out.

A fourth failure sits underneath all three: **the repo's own prior work was never read.** The March
2026 children matrix already carried Berkhamsted as a priority target expected to "rise dramatically
with additional matches," already held the England-wide Peter negative, and already listed
households — Bishops Cleeve, Upton upon Severn, Earsham — that the July sweeps never surfaced.[^v3]

The pattern is not bad luck. It is executing without a method, and correcting at the mechanical layer
only. This document fixes the layer above.

## 1. Source inventory — what must be consulted

A "complete" inventory is not one provider's index. Parish baptisms reach us through **several
independent transcriptions of overlapping originals**, plus the originals themselves. Each must be
named, and each record must carry which one it came from.

| # | Instrument | What it actually is | Independence |
|---|---|---|---|
| S1 | FindMyPast county sets (Bucks Baptism Index, Beds Baptisms, Herts, Norfolk, Kent …) | County FHS / archive transcriptions; carry Father / Mother / Place columns and archive references | Independent per county |
| S2 | FindMyPast *England Births & Baptisms 1538–1975* | National aggregate; carries rows flagged **Exclusive** that exist in no other provider | Partly independent |
| S3 | FindMyPast cross-collection (`sid=999`) and parent search (`sid=102`) | Query modes over S1+S2, not new data — but they reach rows the single-dataset mode cannot | Access layer |
| S4 | Ancestry collection 9841, *England Select Births & Christenings* | IGI-derived | Independent of S1 |
| S5 | Ancestry county collections (61045 Norfolk; Herts; Bucks) | Archive-partnership, **image-linked** | Independent; the image is the point |
| S6 | FamilySearch *England Births and Christenings 1538–1975* | IGI-derived, overlaps S4 but not identical; **carries death dates S4 often lacks** | Partly independent |
| S7 | FamilySearch county Church Records (e.g. Buckinghamshire 4380170) | Archive-partnership; **indexes mothers where the older sets do not** | Independent |
| S8 | **FreeREG** | Volunteer parish-level transcription with **explicit per-parish coverage statements** | Independent; the only one that tells you what it has |
| S9 | FamilySearch Full-Text Search | Reads document text, not an index | Wholly independent |
| S10 | **Bishop's transcripts** | A *second contemporary witness* to the same register; survives where registers do not | **Independent of the register** |
| S11 | Printed register transcripts (Phillimore; parish register societies) | Nineteenth-century transcriptions of originals since damaged | Independent |
| S12 | The register images themselves | The record | Authority |
| S13 | The repo's own prior work | The March 2026 matrix, case-file §6.1, topic files, coverage CSVs | **Read FIRST, not last** |
| S14 | **`data/sources.json` notes** | The source registry's own per-set annotations, recording what each instrument returned and when | **Independent of the research layer, and it has been right when the research layer was wrong** |

**S14 is an amendment made 2026-07-28, and it was earned.** The Berkhamsted burial negative that opened
Candidate C(ii) was contradicted by the registry's own entry for `findmypast-hertfordshire-burials`,
which had recorded the two seventeenth-century Jhon Gourney burials since 9 May 2026. Nobody read it,
because "read the repo first" had only ever meant the research layer. The registry is a different
witness: it records what an instrument returned on a given date, which is exactly the thing a fresh
sweep is at risk of getting wrong.

**S10 deserves emphasis.** Several Buckinghamshire rows already in hand carry archive references
`D/A/T/90`, `D/A/T/106` — those are **bishop's transcripts**, not parish registers. Where a register
is lost, the BT may survive; where both survive, they are two witnesses and can disagree. No county
is "done" until both series are accounted for.

## 2. Catalogue — one row per record instance

Findings live in `research/people/g13-john-gurney/coverage/child-record-catalog.csv`. **One row per
record instance, not per child** — the same baptism indexed by four providers is four rows, because
the disagreements between them are evidence.

Columns: `record_id`, `child_forename_as_indexed`, `child_surname_as_indexed`, `event_type`,
`event_date_as_indexed`, `parish`, `county`, `father_forename_as_indexed`,
`father_surname_as_indexed`, `mother_forename_as_indexed`, `source_code` (S1–S13), `collection_name`,
`archive_ref`, `exclusive_flag`, `household_id`, `query_date`, `notes`.

**Rules.** Record names **exactly as indexed** — normalising to "Gurney" destroys the variant
evidence that this project keeps needing. No row enters without `source_code` and `query_date`. A row
seen in two providers gets two rows sharing a `household_id`.

## 3. Household assembly — the discipline the splits were missing

Three households have been split this month (Aylesbury, Stewkley, Berkhamsted) on plausibility
arguments, and each split was then treated as a finding. **A split is a hypothesis about record
shape, and record shape is exactly what is uncertain.** The discipline:

- A household is **a set of catalogued rows plus an explicit shape hypothesis**, never a bare
  assertion.
- When a baptism run is too long for one father, **enumerate the alternatives rather than choosing
  one**: (a) one man, two wives; (b) father and son; (c) two unrelated same-name men in one parish;
  (d) an index conflating two parishes; (e) a mis-transcribed father forename in some rows.
- Record **which evidence would discriminate** — a marriage, a burial, a will naming children, a
  BT/register disagreement — and hold the shape open until it exists.
- **Never build a probability on an unresolved shape.** The Berkhamsted 9% rests on shape (b) being
  right and should be labelled as conditional on it.

## 4. Scoring rubric

Scored against the colonial signature: children **Mary** (~1628, hard bound born by 1631 from her
1647 marriage), **Richard** (~1630), **John Jr** (~1633); wife **Mary**, married by ~1630, living to
1661; father born c.1598–1608, gone from England 1637–41. *Sarah is doubtful; Peter and Isaac are
probably American-born and are not scored.*

| Signal | Points |
|---|---|
| Each of Mary / Richard / John present as a child | **+2** each |
| That child's baptism within ±2 years of expectation | **+2** |
| …within ±5 years | **+1** |
| Birth **order** Mary → Richard → John preserved | **+2** |
| Birth order violated | **−2** |
| Mother indexed **Mary** | **+3** |
| Mother indexed otherwise, but a remarriage window exists | **0** |
| Mother indexed otherwise with no remarriage window | **−3** |
| Father indexed **John** | **+3** |
| Father indexed otherwise — **not an elimination** | **−2**, and flag for a transcription check |
| Father's implied birth year 1598–1608 | **+3** |
| Father's implied birth year outside that band | **−3** |
| Household's last record falls 1635–41 | **+3** |
| Household demonstrably continues past 1641 | **−5** |
| Head's English burial or probate after 1641 | **−10** (effective elimination) |
| Each additional child with a non-colonial forename | **−1** |

**A non-John father is a flag, not a verdict** — this project has already proved an indexer misreads
H as G. Any household scoring ≥6 on the child signals alone gets its father's forename checked
against the image regardless of what the index says.


## 4a. Scoring corrections adopted 2026-07-29

The rubric in §4 is superseded on five points by the shape specification and the scoring pass in
unit 74:

- **Mary's date is a primary bound, not a tradition.** She married Daniel Shed at Braintree in 1647,
  so at a minimum marriage age of sixteen she was **born by 1631**. Score against that. The "c.1628"
  is compiled tradition (Sprague 2001, *History of Weymouth* 1923), and **Richard c.1630 and John
  c.1633 rest entirely on the same compiled estimates with no primary record** - they must weigh less
  than Mary's bound.
- **Margaret belongs on the mother axis as a substantial soft hit** (revised 29 July 2026; the earlier
  text of this bullet asserted the opposite and was retracted — see unit 74 feedback point 1 and unit
  75 §1). Maria, Marie, Marye and Marya interchange with Mary freely and score at full weight.
  **Margaret, Margarett, Margret and the contractions `Marg.` and `Mgt.` score as substantial soft
  hits**, because `g` and `y` carry near-identical looping descenders in this period's hands and
  Margaret was routinely abbreviated — so the distinguishing letter is the ambiguous one, and the
  transcription chain corrupts in both directions. Margery scores partial (shares the `Marg.` stem, but
  a distinct name). Molly and Polly stay excluded as eighteenth-century hypocorisms that cannot appear
  in a 1620s register.
- **The John family on the father axis includes `Jone` and `Joan`.** Score John, Jhon, Jon, Jno, Joh,
  Johis, Joh[ann]is, Johannes, Johan, Johane and Johanne — and treat an indexed `Jone`/`Joan` in a
  *father* field as a probable contracted or Latin Johannes rather than a woman, since these indexes
  demonstrably put such tokens there (Norwich St Giles 1618) and demonstrably put mothers' names in the
  father column outright (King's Lynn 1615).
- **Never score an undated FamilySearch role row as an in-window household.** Date it on a second
  instrument first. Three such households carried since unit 68 were dated in July 2026 and resolved to
  **1687, 1704 and 1710** — three for three outside the window by six decades or more.
- **Peter, Isaac and Sarah must not be scored against a candidate.** No Peter Gurney-variant baptism
  exists in Great Britain 1627-47 and no Isaac 1632-52; both first appear in colonial records, so
  their English absence is expected. Sarah has no primary record anywhere and is absent from Torrey.
- **Add a departure attribute, with its coverage control attached:** the household's records stop
  1635-41 with no burial or probate for the head, **in a parish whose burials are demonstrably
  covered**. Without the control this produces false gaps - it has done so twice here.
- **Add a surplus-children penalty.** A household with the right three children and no others fits
  better than one with the right two and four extras.

## 5. Stopping rule — what "done" means

The inventory is done when **all** of these hold, and not before:

1. **Every instrument S1–S12 has been run** for: father John Gurney (variant-expanded); each of child
   Mary / Richard / John (variant-expanded); window 1615–1645; England and Wales.
2. **Positive controls pass on every instrument** (§6).
3. **Every returned row is catalogued** with provenance and assigned a `household_id`.
4. **Every household is scored**, with its shape hypothesis and discriminating evidence recorded.
5. **A coverage statement exists per county worked**: which register and BT series survive for the
   window, and which provider indexes each.
6. **The residual is named** — a list of parishes whose registers are known lost for 1620–1640, so the
   unsearchable remainder is a stated quantity rather than an unknown.

## 6. Self-checks — at the plan layer, not just the mechanical one

Every one of the three failures would have been caught by check **C2**.

- **C1 — Read the repo first, *including the source registry*.** Before any external search,
  `repo_search` the question across research **and** `data/sources.json` notes. The March 2026 matrix
  answered several of July's "new" findings, and the registry's `findmypast-hertfordshire-burials`
  note held the Berkhamsted burials that a July sweep reported as non-existent (S14).
- **C2a — Match the place token to the target set, not to the parish's name.** A keyword place filter
  is a literal token match and **fails closed**: a wrong spelling returns zero, not an error. The same
  county provider spells one parish *Great Berkhampstead* in its baptism set and *Berkhamstead* in its
  burial set. Establish the token from a common-surname control before filtering on it.
- **C2b — Check the surname stem actually reaches the spelling in use.** `gurn*` does not match
  *Gourney*. A wildcard covers one stem; it is not a variant sweep, and this has now produced two
  false England-wide negatives in this project.
- **C2c — Do not combine a year bound with a place keyword in a single-dataset query. The combination
  fails closed.** Proven on FindMyPast's Essex Baptisms set, 29 July 2026: 349 Smith baptisms at Epping
  with no year bound, **zero** with `yearofbaptism=1616&yearofbaptism_offset=5`, in a set that
  demonstrably holds a 1616 Epping baptism under another surname. Filter by place *or* by year, then
  bound the other axis by reading the returned rows. **Any negative in the existing record that rests
  on both parameters at once is void and must be re-run.** Related: `sortby` is accepted and ignored,
  so a set's earliest coverage year cannot be established by sorting — establish it from a
  common-surname control's returned span, and say so when the span is only a partial page.
- **C2 — Positive control on every sweep.** Each query must return a record already known to exist and
  fall in scope. If a national Mary sweep does not return **Hitcham 1631**, or a Richard sweep does
  not return **Berkhamsted 1626**, *the query is broken* — do not read the result as a finding. This
  is the single cheapest check and it fails loudly.
- **C3 — Pre-register the expectation.** State the expected order of magnitude before running. A
  result off by 10× is a query defect until proven otherwise.
- **C4 — Two-instrument rule.** No negative is recorded from one provider.
- **C5 — Two-axis rule.** Every question asked by **child** and by **parent**, and by **place** where
  a parish is named.
- **C5a — Weight the variant; never exclude a surname as a class.** Variant forms sit on a sliding
  scale of plausibility and the weight attaches to the **individual record**, not to the spelling as a
  category. *Gurne/Gurn* are near-certain contractions; *Gurnard/Gurnat* carry a **documented alias**
  (Heralds' Visitation of London 1634: "Richard Gurny, alias Gurnard, Sheriff of London") reinforced by
  the family's own canting gurnard-fish crest; *Gorne/Garne/Gernne* are ordinary vowel drift;
  *Gurnett/Gurnel/Gurner* are recognised surnames in their own right and rate lower — **but lower is
  not zero.** An index spelling is a transcriber's reading of one clerk's hand on one day; only the
  register image and the hand can settle it. **Do not infer a family from a later century's settled
  spelling**, and do not assume that rows sharing a parish across three generations share a family —
  this project has proved four Gurney households in one parish at Berkhamsted and two at Stewkley.
  *(This check replaced a binary "is it even the same surname?" test written 2026-07-28 and retracted
  the next day; the retraction is in unit 69.)*
- **C5b — Weight against shape, not against volume.** The object is never a count of Gurney records.
  It is whether an **individual record** matches a corner of the colonial shape — a Mary about 1628, a
  Richard about 1630, a John about 1633, a father John, a mother Mary, a household that stops
  1635–41. A low-weight surname form on a record that matches the shape is worth more than a
  high-weight form on one that does not. Report matches and partial matches, not totals.
- **C6 — Shape enumeration.** No household collapses to one shape without the alternatives written
  down (§3).
- **C7 — Stop-and-reset trigger.** **After two corrections in the same domain, stop executing and
  rebuild the method.** This is the check that was missing; three corrections ran before the reset.
- **C8 — Provenance completeness.** A finding without `source_code` and `query_date` is not a finding.

## 7. Correction arising from §S13

Reading the March 2026 matrix corrects a claim made in this refactor. Unit 60 and unit 64 record a
provider disagreement — FindMyPast indexing the Berkhamsted family at "Great Berkhampstead",
FamilySearch at "St Peter, Hertfordshire" — and unit 61 built a partial argument on it, reading
St Peter as St Albans. **The matrix names the parish "St Peter's, Berkhamsted", and St Peter's is
Berkhamsted's own parish church.** There is no parish discrepancy: both providers mean the same
church. The action opened to resolve it should be closed, and unit 61's convergence argument needs
re-checking on the point of which archdeaconry actually held Berkhamsted — that is now an open
question rather than a settled one.[^stpeter]

## Crosslinks

- [`64-refactor-berkhamsted-reopened.md`](64-refactor-berkhamsted-reopened.md) — the candidate this method must now test properly
- [`63-refactor-child-sweep-closed-and-reassessment.md`](63-refactor-child-sweep-closed-and-reassessment.md) — the probability table, conditional on the Berkhamsted shape
- [`59-refactor-open-actions.md`](59-refactor-open-actions.md) — open actions
- Catalogue: `research/people/g13-john-gurney/coverage/child-record-catalog.csv`

[^v3]: *John Gurney Children Matrix V3*, compiled March 2026, at [`research/case-files/Initial foundation work for john-gurney-case-file/John_Gurney_Children_Matrix_V3.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/Initial%20foundation%20work%20for%20john-gurney-case-file/John_Gurney_Children_Matrix_V3.md). Carries Berkhamsted at "2/5 … No disqualifying evidence … PRIORITY SEARCH: marriage register + Mary/John Jr./Peter baptisms … could rise dramatically with additional matches"; the England-wide Peter negative for 1620–1645; and households absent from the July 2026 sweeps — Maria Gorne, 2 March 1627, Bishops Cleeve, Gloucestershire, father John Gorne; Mary Gurney, 7 September 1629, Upton upon Severn, Worcestershire, mother Mary with no father named; John Girney, 23 December 1636, Earsham, Norfolk, father John Girney. Cross-reference to prior repo work, not a source; the underlying records are the parish registers it cites.
[^stpeter]: Same matrix, Table 2 and Table 3: "BERKHAMSTED, Herts **St. Peter's**"; "Richard Gurnie, 15 Dec 1626, **St. Peter, Berkhamsted**, Herts, John Gurnie"; "Sara Gurny, 18 May 1634, **St. Peter, Berkhamsted**, Herts, John Gurny". St Peter's, Great Berkhamsted is the parish church of Berkhamsted. Cross-reference, not a source.
