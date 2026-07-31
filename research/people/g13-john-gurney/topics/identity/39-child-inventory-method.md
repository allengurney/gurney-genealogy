<!-- topicId: g13-identity-inventory-method. Prose markers (schema v3) are the passage→item map; no item-range comment. Scope: the method governing any further round of the same-name / child-inventory search — sources, catalogue, household assembly, scoring, stopping rule and self-checks. Not argued here: findings (30-38). This is the file that governs how a future round should work. -->

# Identity — method for a complete child inventory

This is a method document, not a findings document. It governs how any further round of the same-name and child-inventory search is run, and it exists because three consecutive rounds in July 2026 failed in ways that a method would have caught.

## Why it exists

The failures were: a sweep by **child forename on one surname stem** (`gurn*`) in one provider, reported as an England-wide result, which missed households indexed Gernne, Garne, Gourney, Gowrne and Greney; a **wrong parameter name** generalised into "no parent search works" and written into the search skill as a durable rule, where the correct query returns 315 rows against the flawed one's single household; and **counting rows instead of assembling households**, which left a father-and-son split sitting visible in data already in hand.

A fourth failure sits underneath all three: **the project's own prior work was never read.** The March 2026 children matrix already carried Berkhamsted as a priority target expected to "rise dramatically with additional matches," already held the England-wide Peter negative, and already listed households — Bishop's Cleeve, Upton upon Severn, Earsham — that the July sweeps never surfaced.[^v3]

The pattern is not bad luck. It is executing without a method and correcting at the mechanical layer only.

## 1. Source inventory — what must be consulted

A complete inventory is not one provider's index. Parish baptisms reach us through **several independent transcriptions of overlapping originals**, plus the originals themselves. Each must be named, and each catalogued record must carry which one it came from.

| # | Instrument | What it actually is | Independence |
|---|---|---|---|
| S1 | FindMyPast county sets (Bucks Baptism Index, Beds, Herts, Norfolk, Kent …) | County FHS / archive transcriptions; carry Father, Mother and Place columns and archive references | Independent per county |
| S2 | FindMyPast *England Births & Baptisms 1538–1975* | National aggregate; carries rows flagged **Exclusive** that exist in no other provider | Partly independent |
| S3 | FindMyPast cross-collection (`sid=999`) and parent search (`sid=102`) | Query modes over S1+S2, not new data — but they reach rows the single-dataset mode cannot | Access layer |
| S4 | Ancestry collection 9841, *England Select Births & Christenings* | IGI-derived | Independent of S1 |
| S5 | Ancestry county collections (61045 Norfolk; Herts; Bucks) | Archive-partnership, **image-linked** | Independent; the image is the point |
| S6 | FamilySearch *England Births and Christenings 1538–1975* | IGI-derived; overlaps S4 but is not identical, and **carries death dates S4 often lacks** | Partly independent |
| S7 | FamilySearch county Church Records (e.g. Buckinghamshire 4380170) | Archive-partnership; **indexes mothers where the older sets do not** | Independent |
| S8 | **FreeREG** | Volunteer parish-level transcription with **explicit per-parish coverage statements** | Independent; the only one that tells you what it has |
| S9 | FamilySearch Full-Text Search | Reads document text, not an index | Wholly independent |
| S10 | **Bishop's transcripts** | A *second contemporary witness* to the same register; survives where registers do not | **Independent of the register** |
| S11 | Printed register transcripts (Phillimore; parish register societies) | Nineteenth-century transcriptions of originals since damaged | Independent |
| S12 | The register images themselves | The record | Authority |
| S13 | The project's own prior work | The March 2026 matrix, the case file, topic files, coverage CSVs | **Read first, not last** |
| S14 | **`data/sources.json` notes** | The source registry's per-set annotations, recording what each instrument returned and when | **Independent of the research layer, and it has been right when the research layer was wrong** |

**S14 was earned.** The Berkhamsted burial negative that opened Candidate C(ii) was contradicted by the registry's own entry for the Hertfordshire burial set, which had recorded the two seventeenth-century Jhon Gourney burials since 9 May 2026. Nobody read it, because "read the repo first" had only ever meant the research layer. The registry is a different witness: it records what an instrument returned on a given date, which is exactly the thing a fresh sweep is at risk of getting wrong.

**S10 deserves emphasis.** Several Buckinghamshire rows carry archive references of the form `D/A/T/nn` — those are **bishop's transcripts**, not parish registers. Where a register is lost the transcript may survive; where both survive they are two witnesses and can disagree. **No county is done until both series are accounted for**, and the point is demonstrated rather than asserted: FindMyPast's Buckinghamshire Baptism Index is bishop's transcripts, FreeREG transcribes parish registers, and the two return materially different Gurney event sets for the same county and window.<!-- graph-marker: G13-PM-000131 -->

## 2. Catalogue — one row per record instance

Findings live in `research/people/g13-john-gurney/coverage/child-record-catalog.csv`. **One row per record instance, not per child** — the same baptism indexed by four providers is four rows, because the disagreements between them are evidence.

Columns: `record_id`, `child_forename_as_indexed`, `child_surname_as_indexed`, `event_type`, `event_date_as_indexed`, `parish`, `county`, `father_forename_as_indexed`, `father_surname_as_indexed`, `mother_forename_as_indexed`, `source_code` (S1–S14), `collection_name`, `archive_ref`, `exclusive_flag`, `household_id`, `query_date`, `notes`.

**Rules.** Record names **exactly as indexed** — normalising to "Gurney" destroys the variant evidence this work repeatedly needs. No row enters without `source_code` and `query_date`. A row seen in two providers gets two rows sharing a `household_id`.

## 3. Household assembly — the discipline the splits were missing

Four households have been split on plausibility arguments, and each split was then treated as a finding. **A split is a hypothesis about record shape, and record shape is exactly what is uncertain.**

- A household is **a set of catalogued rows plus an explicit shape hypothesis**, never a bare assertion.
- When a baptism run is too long for one father, **enumerate the alternatives rather than choosing one**: (a) one man, two wives; (b) father and son; (c) two unrelated same-name men in one parish; (d) an index conflating two parishes; (e) a mis-transcribed father forename in some rows.
- Record **which evidence would discriminate** — a marriage, a burial, a will naming children, a transcript/register disagreement — and hold the shape open until it exists.
- **Never build a probability on an unresolved shape.** Where a row rests on a split, label it conditional on that shape.

## 4. Scoring rubric

Scored against the colonial signature: children **Mary** (hard bound, born by 1631), **Richard** (c.1630, compiled) and **John Jr.** (c.1633, compiled); wife **Mary**, married by about 1630, living to 1661; father born c.1598–1608, gone from England 1637–41.

| Signal | Points |
|---|---|
| Each of Mary / Richard / John present as a child | **+2** each |
| That child's baptism within ±2 years of expectation | **+2** |
| …within ±5 years | **+1** |
| Birth **order** Mary → Richard → John preserved | **+2** |
| Birth order violated | **−2** |
| Mother indexed **Mary** (or Marie, Marye, Maria, Marya, Mria) | **+3** |
| Mother indexed **Margaret / Margarett / Margret / `Marg.` / `Mgt`** | **+2** (substantial soft hit) |
| Mother indexed **Margery / Margerie** | **+1** (partial) |
| Mother indexed otherwise, but a remarriage window exists | **0** |
| Mother indexed otherwise with no remarriage window | **−3** |
| Father indexed in the **John** family | **+3** |
| Father indexed otherwise — **not an elimination** | **−2**, and flag for a transcription check |
| Father's implied birth year 1598–1608 | **+3** |
| Father's implied birth year outside that band | **−3** |
| Household's last record falls 1635–41 **in a parish whose burials are demonstrably covered** | **+3** |
| Household demonstrably continues past 1641 | **−5** |
| Head's English burial or probate after 1641 | **−10** (effective elimination) |
| Each additional child with a non-colonial forename | **−1** |

**Six rules govern how the rubric is applied.**

**Mary's date is a primary bound; the others are not.** She married Daniel Shed at Braintree in 1647, so at a minimum marriage age of sixteen she was born by 1631. Richard c.1630 and John c.1633 rest entirely on compiled estimates with no primary record behind them and must weigh less.[^mary-bound]

**The Mary and Margaret forms are a weighted scale, not a filter.** In seventeenth-century hands `g` and `y` carry near-identical looping descenders, and *Margaret* was routinely contracted to `Marg.` or `Mgt.`, so the one letter distinguishing the written token from *Mary* is exactly the letter most likely to be ambiguous — and **the corruption is introduced by the transcription chain and runs in both directions.** Molly and Polly stay excluded as eighteenth-century hypocorisms that cannot appear in a 1620s register.

**The John family on the father axis includes `Jone` and `Joan`.** Score John, Jhon, Jon, Jno, Joh, Johis, Joh[ann]is, Johannes, Johan, Johane and Johanne — and treat an indexed `Jone` or `Joan` in a *father* field as a probable contracted or Latin Johannes rather than a woman, since these indexes demonstrably put such tokens there and demonstrably put mothers' names in the father column outright.[^parentfields]

**Never score an undated role row as an in-window household.** Date it on a second instrument first. Three such households were carried for a week and then dated: they resolved to **1687, 1704 and 1710** — three for three outside the window by six decades or more.

**Peter, Isaac and Sarah must not be scored against a candidate.** No Peter Gurney-variant baptism exists in Great Britain 1627–47 and no Isaac 1632–52; both first appear in colonial records, so their English absence is expected. Sarah has no primary record anywhere and is absent from Torrey.

**A non-John father is a flag, not a verdict** — this project has already proved that an indexer misreads a capital H as G, so a genuine Gurney can sit in an index as *Hurney*. Any household scoring six or more on the child signals alone gets its father's forename checked against the image regardless of what the index says.

The fifteen-attribute shape the rubric implements, and the matrix scoring every candidate against it, are in [`38-the-shape-and-the-two-families.md`](38-the-shape-and-the-two-families.md).<!-- graph-marker: G13-PM-000132 -->

## 5. Stopping rule — what "done" means

The inventory is done when **all** of these hold, and not before:

1. **Every instrument S1–S12 has been run** for father John Gurney (variant-expanded) and for each of child Mary, Richard and John (variant-expanded), window 1615–1645, England and Wales.
2. **Positive controls pass on every instrument** (§6).
3. **Every returned row is catalogued** with provenance and assigned a `household_id`.
4. **Every household is scored**, with its shape hypothesis and discriminating evidence recorded.
5. **A coverage statement exists per county worked**: which register and transcript series survive for the window, and which provider indexes each.
6. **The residual is named** — a list of parishes whose registers are known lost for 1620–1640, so the unsearchable remainder is a stated quantity rather than an unknown.

## 6. Self-checks

Every one of the original three failures would have been caught by **C2**.

- **C1 — Read the project's own record first, including the source registry.** Before any external search, search the research layer **and** `data/sources.json` notes. The March 2026 matrix answered several of July's "new" findings, and the registry's Hertfordshire-burials note held the Berkhamsted burials that a July sweep reported as non-existent.
- **C2 — Positive control on every sweep.** Each query must return a record already known to exist and in scope. If a national Mary sweep does not return **Hitcham 1631**, or a Richard sweep does not return **Berkhamsted 1626**, *the query is broken* — do not read the result as a finding. This is the cheapest check and it fails loudly.
- **C2a — Match the place token to the target set, not to the parish's name.** A keyword place filter is a literal token match and **fails closed**: a wrong spelling returns zero, not an error. The same county provider spells one parish *Great Berkhampstead* in its baptism set and *Berkhamstead* in its burial set. Establish the token from a common-surname control before filtering on it.
- **C2b — Check the surname stem actually reaches the spelling in use.** `gurn*` does not match *Gourney*. A wildcard covers one stem; it is not a variant sweep, and this has produced two false England-wide negatives.
- **C2c — Do not combine a year bound with a place keyword in a single-dataset query. The combination fails closed.** Proven: 349 Smith baptisms at Epping with no year bound, **zero** with a 1616 bound, in a set that demonstrably holds a 1616 Epping baptism under another surname. Filter by place *or* by year, then bound the other axis by reading the returned rows. **Any negative in the existing record that rests on both parameters at once is void and must be re-run.** Related: `sortby` is accepted and silently ignored, so a set's earliest coverage year cannot be established by sorting — establish it from a common-surname control's returned span, and say so when the span is only a partial page.[^void]
- **C3 — Pre-register the expectation.** State the expected order of magnitude before running. A result off by ten times is a query defect until proven otherwise.
- **C4 — Two-instrument rule.** No negative is recorded from one provider. **No index is complete and the gaps do not coincide**, tested cell by cell.[^incomplete]
- **C5 — Two-axis rule.** Every question asked by **child** and by **parent**, and by **place** where a parish is named. And note that a national parent pool may not reach every county set, so any England-wide negative from it needs pairing with county-set runs.
- **C5a — Weight the variant; never exclude a surname as a class.** Variant forms sit on a sliding scale of plausibility and the weight attaches to the **individual record**, not to the spelling as a category. *Gurne* and *Gurn* are near-certain contractions; *Gurnard* and *Gurnat* carry a **documented alias** and the family's own canting gurnard crest; *Gorne*, *Garne* and *Gernne* are ordinary vowel drift; *Gurnett*, *Gurnel* and *Gurner* are recognised surnames in their own right and rate lower — **but lower is never zero.** An index spelling is a transcriber's reading of one clerk's hand on one day; only the register image and the hand can settle it. **Do not infer a family from a later century's settled spelling**, and do not assume that rows sharing a parish across three generations share a family — four Gurney households have been proved in one parish at Berkhamsted and two at Stewkley.[^variants]
- **C5b — Weight against shape, not against volume.** The object is never a count of Gurney records. It is whether an **individual record** matches a corner of the colonial shape. A low-weight surname form on a record that matches the shape is worth more than a high-weight form on one that does not. **Report matches and partial matches, not totals.**
- **C6 — Shape enumeration.** No household collapses to one shape without the alternatives written down (§3).
- **C7 — Stop-and-reset trigger.** **After two corrections in the same domain, stop executing and rebuild the method.** This is the check that was missing; three corrections ran before the reset.
- **C8 — Provenance completeness.** A finding without `source_code` and `query_date` is not a finding.<!-- graph-marker: G13-PM-000133 -->

## 7. The departure test has an instrument, and it has never been run

The natural inversion of the search — *which John Gurney household's records stop between 1635 and 1641 without a burial or probate for the head?* — has been treated as something to do parish by parish. It is not. **The parent-name search runs over burials as well as baptisms.** A father-John-Gurney sweep for 1625–1635 reports, in the same facet panel, 108 parish baptisms, 76 parish burials and 13 parish marriages. Switching the collection to parish burials therefore asks, in one query, *which children of a John Gurney were buried in England* — and the households whose children appear in the baptism arm but not the burial arm are exactly the departure-shaped gaps.

Two mechanics have to be right first. The year parameter in this mode is `yearofbirth=`, because `year=` renders a chip and then returns a silent zero. And the pool excludes some county sets, so the burial arm needs pairing with county-set runs exactly as the baptism arm does.[^facets]

**This is the highest-value single query left on the child inventory, and it has never been executed.** The wider point is what the method was written for: this work has repeatedly gained more from establishing that an instrument said what it appeared to say than from running more searches. **Method work keeps outperforming search volume on this problem.**

## Crosslinks

- [`38-the-shape-and-the-two-families.md`](38-the-shape-and-the-two-families.md) — the shape the rubric implements
- [`37-identity-assessment.md`](37-identity-assessment.md) — the probability model the scoring feeds
- Catalogue: `research/people/g13-john-gurney/coverage/child-record-catalog.csv`
- [`65-refactor-child-inventory-method.md`](65-refactor-child-inventory-method.md) — the working round in which the method was built, with its correction trail

---

[^v3]: *John Gurney Children Matrix V3*, compiled March 2026, at [`research/case-files/Initial foundation work for john-gurney-case-file/John_Gurney_Children_Matrix_V3.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/Initial%20foundation%20work%20for%20john-gurney-case-file/John_Gurney_Children_Matrix_V3.md). Carries Berkhamsted at "2/5 … No disqualifying evidence … PRIORITY SEARCH: marriage register + Mary/John Jr./Peter baptisms … could rise dramatically with additional matches"; the England-wide Peter negative for 1620–1645; and households absent from the July 2026 sweeps — Maria Gorne, 2 March 1627, Bishop's Cleeve, Gloucestershire, father John Gorne; Mary Gurney, 7 September 1629, Upton upon Severn, Worcestershire, mother Mary with no father named; John Girney, 23 December 1636, Earsham, Norfolk, father John Girney. The matrix also names the Berkhamsted parish as "St Peter's, Berkhamsted," which settles a provider disagreement that was briefly treated as a parish discrepancy: St Peter's is Berkhamsted's own parish church. Cross-reference to prior project work, not a source; the underlying records are the parish registers it cites.

[^mary-bound]: Mary Gurney's 1647 marriage to Daniel Shed at Braintree is in Samuel A. Bates, ed., *Records of the Town of Braintree, 1640 to 1793* (1886), and in Torrey, *New England Marriages Prior to 1700*. The compiled estimates are Sprague, *Genealogies of the Families of Braintree* (2001), p. 695, and the *History of Weymouth* (1923), vol. 3, p. 251. Source IDs: `braintree-records-1640-1793-1886`; `torrey-new-england-marriages-prior-1700`; `sprague-braintree`; `history-of-weymouth`.

[^parentfields]: FindMyPast county baptism sets, 29 July 2026: at Norwich St Giles in 1618 the father of Joseph Garnam is indexed `Jone`; at King's Lynn St Margaret with St Nicholas in 1615 the *father* of Gregorye Gurnall is indexed `Katheryne`. Tittleshall with Godwick, Norfolk, 1620 returns the same child twice, father Henry in both, with the mother indexed **Anne** in one transcript and **Mary** in the other. Source IDs: `findmypast-county-baptism-sets-2026-07-sweep`; `findmypast-norfolk-baptisms-index`.

[^void]: FindMyPast *Essex Baptisms* (`sid=103`), authenticated session, 29 July 2026: `lastname=smith&keywords=epping` with no year bound returns 349 results; the same query with `yearofbaptism=1616&yearofbaptism_offset=5` returns 0, and with `yearofbaptism=1600&yearofbaptism_offset=5` returns 0, in a set that demonstrably holds a 1616 Epping baptism under another surname. `sortby=dateasc` leaves the result order unchanged. Recorded as a reusable instrument defect in `.claude/skills/findmypast-record-search/SKILL.md` §0d. Source ID: `findmypast-county-baptism-sets-2026-07-sweep`.

[^incomplete]: Tested cell by cell across four providers: Ancestry's IGI-derived set lacks Hitcham 1631, Great Berkhampstead 1626, Stewkley 1626 and Aylesbury 1638; FreeREG lacks Hitcham, Berkhampstead and Aylesbury but holds Stewkley; FindMyPast and FamilySearch hold all four. FreeREG's non-soundex surname matching is **exact** — a *Gurney* query returns only rows spelled `GURNEY` — so a single-spelling search there sees roughly a quarter of the record set, and variant spellings are mandatory rather than optional on that instrument. Source IDs: `ancestry-england-select-births-christenings-9841`; `freebmd-freereg`; `findmypast-uk-parish-baptisms`; `fs-england-births-christenings`.

[^variants]: Heralds' Visitation of London, 1634 (Harleian MS 1476), printed in Daniel Gurney, *The Record of the House of Gournay*, Part III (1848), p. 533: letters patent of 26 July 1633 to "Richard Gurny, *alias* Gurnard, Sheriff of London." The Norfolk line's canting gurnard-fish crest was borne by Thomas Gournay I before 1465. The retraction of the earlier binary test — "is it even the same surname?" — is at [`69-refactor-essex-tested-and-the-surname-confusion.md`](69-refactor-essex-tested-and-the-surname-confusion.md). Source IDs: `dg-rec-pt3`; `heralds-visit-london-1633`.

[^facets]: FindMyPast cross-collection parent search, authenticated session, 28 July 2026: `sid=102&fatherfirstname=john&fatherfirstname_variants=true&fatherlastname=gurney&fatherlastname_variants=true&collection=parish+baptisms&sourcecountry=great+britain&yearofbirth=1630&yearofbirth_offset=5`. The facet panel reports Parish Baptisms 108, Parish Burials 76, Parish Marriages 13, Wills & Probate 0. The variants engine is loose, so the row list mixes genuine Gurney households with Gray, Griffith, Gaune and unreadable-surname rows; the counts are an upper bound and the rows must be read. On the same instrument, `year=1630&year_offset=10` returns 0 results while rendering a "Year 1630" chip, whereas `yearofbirth=1630&yearofbirth_offset=5` returns 108. Source ID: `findmypast-uk-parish-baptisms`.
