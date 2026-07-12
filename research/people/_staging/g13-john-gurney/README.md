# G13 John Gurney — staged research package (in progress)

Staging area for the G13 companion/dump refactor (Plan 02) and the context-graph
pilot (Plan 01). **Not canonical yet** — the live companion at
`research/people/g13-john-gurney-fact-sheet.research.md` remains untouched until
an approved cutover (Plan 02 §15).

Phase P pilot slice (2026-07-03): `topics/colonial/01-arrival-chronology.md`,
co-authored with research items `G13-RI-000001..000007` in the canonical SQLite
context graph. See `manifest.json` for the topic/graph map.

Phase G3 increment (2026-07-03, bounded): `topics/colonial/03-braintree-community.md`,
co-authored with research items `G13-RI-000008..000017` (John's Braintree
residence, the leased Tyng farm / future Adams seat, his Monatiquot freehold,
community standing, and one open question on the 1645 petition's primary source).
Loaded transactionally into the canonical graph at database revision 4; sources
baselined and a milestone snapshot written at revision 5
(`data/context-graphs/g13/exports/snapshots/g13-context-r000005.ndjson`).

Phase G3 increment (2026-07-04, bounded): `topics/colonial/02-weymouth-community.md`,
co-authored with research items `G13-RI-000018..000023` and four prose evidence
markers `G13-PM-000006..000009` (John's standing in the Weymouth town community:
inhabitant land grants — carrying the manuscript Land Grants book into the graph —
a 1644 credit tie to Rev. Thomas Jenner, his documented Weymouth associates
Ludden/Porter/Goodman King, and a first-class negative on active military service;
arrival dating stays in `01-arrival-chronology.md`). Loaded transactionally at
database revision 9; sources baselined and a milestone snapshot written at revision
10 (`data/context-graphs/g13/exports/snapshots/g13-context-r000010.ndjson`). The
massbay dump's §0 county-scope map ([AG][DIRECTIVE]) was routed to
`research/places/weymouth-ma.md`, not duplicated here.

Phase G3 increment (2026-07-04, bounded): `topics/colonial/04-frontier-rights.md`,
co-authored with research items `G13-RI-000024..000032` and four prose evidence
markers `G13-PM-000010..000013` (John's own frontier-plantation proprietary rights,
1659–1663: a Billerica house-lot taken up on condition and surrendered within four
months as an absentee "John Gurney of Braintree" share; the 1662 Mendon allotment
acceptance; and the unvalued "estate layd out in land at Quinapaug wch we know not"
frontier interest in his 1663 estate, decoded as a share in the Providence-jurisdiction
Quinapaug speculation — none of which became residence). Two new place entities
(`place-billerica-massachusetts-usa`, `place-mendon-massachusetts-usa`) carried into
the graph. Loaded transactionally at database revision 11; four new sources baselined
and a milestone snapshot written at revision 12
(`data/context-graphs/g13/exports/snapshots/g13-context-r000012.ndjson`). The post-1667
Mendon proprietor/widow stream (John Gurny + Grisel Gurney as lot-holders) is deliberately
deferred to `g13-family-mendon-descendants`, not duplicated here.

Phase G3 increment (2026-07-04, bounded): `topics/colonial/05-material-life.md`,
co-authored with research items `G13-RI-000033..000037` and four prose evidence
markers `G13-PM-000014..000017` (the material texture of John's life read from his
1663 estate inventory, SPR Case #338: an all-movable estate of £55 14s 6d with no
valued real estate; wealth concentrated in livestock and the working farm (~£34 of
the total in animals alone); a sparse but sufficient household; and a first-class
occupational negative — no shears, needles, pressing iron, or cloth despite the
"John Gurney, tailor" style of his 1661/2 deed). Both cited sources
(`spr-case-338-john-gurney-probate-1663`, `nehgr-12-suffolk-wills-1858`) were
already registered and baselined, so no new sources or entities were carried;
loaded transactionally at database revision 13 and a milestone snapshot written at
the same revision (`data/context-graphs/g13/exports/snapshots/g13-context-r000013.ndjson`).
The Quinapaug land line, the creditor network, and the Goodman King debt are the
estate's other facets and stay in `04-frontier-rights.md`,
`03-braintree-community.md`, and `02-weymouth-community.md` respectively, not
restated here.

Phase G3 increment (2026-07-04, bounded): `topics/colonial/06-record-coverage.md`,
co-authored with research items `G13-RI-000038..000042` and four prose evidence
markers `G13-PM-000018..000021` — a non-identity **record-coverage** meta-topic on the
shape of John's surviving documentary footprint: a continuous 1641–1663 trail dense in
civic, land, court, and probate record classes (finding RI-000038), corroborated by
Anderson's *Great Migration Directory* p. 158 (source_evidence RI-000039); the analysis
that the 1653 *Wilson v. Faxon* deposition is the only record attesting John's own person
rather than his property or office (RI-000040); and two first-class negatives — no vital
or church record fixes his birth, marriage, death, or burial (RI-000041), and no record
states his English origin (RI-000042, Anderson's "Unknown"). Built as a synthesis over
already-homed evidence (SYNTHESIZES the arrival gunpowder RI-000001, the deposition
RI-000010, and the probate RI-000027) plus one new coverage source; no new entities.
Two sources baselined (`anderson-gmd-2015`, `braintree-records-1640-1793-1886`); loaded
transactionally at database revision 16, sources baselined at revision 17, and a milestone
snapshot written at revision 17
(`data/context-graphs/g13/exports/snapshots/g13-context-r000017.ndjson`); validate 0/0.
The English-origin identification (Banks's Bury St Edmunds lead, the Candidate-B reading)
and the disputed 1661 Braintree "Cheny"/Kidbee marriage line are deferred to the dedicated
identity/origin work, not resolved here. The colony-level negative catalogue in the July
dump campaign (Boston First Church zero, Boston Book of Possessions, colony-level FTS
no-new-document, Providence/Garnet, dataset negatives) is **not** assimilated by this
bounded increment and remains backlog for a fuller `g13-research-source-coverage` /
follow-up record-coverage pass.

Plan 2b Thread 3 — source-lossless remediation (2026-07-05, bounded to
`01-arrival-chronology.md` + `02-weymouth-community.md`): reconciled the routed
fact-sheet, case-file, immigration-topic, and dump sources for the two units.
**Arrival:** Anderson's *Great Migration Directory* p. 158 published assessment
(arrival 1636, Boston/Braintree, origin "Unknown") is now carried in the arrival
graph as `published_source_statement` **G13-RI-000043** (QUALIFIES the 1638–early-1641
window RI-000006, DEPENDS_ON the 1641 court order RI-000001); the FamilySearch
full-text-search image read of the 30 May 1641 petition is linked as a second
representation on RI-000002 (supports) and RI-000007 (qualifies), resolving the
`same_record_multiple_representations` friction; and the Phase-P unit was backfilled
with four Plan 2a prose markers **G13-PM-000022..000025**. **Weymouth:** the
immigration-topic analytical depth is assimilated as three items — the 1636 Fresh
Pond great-lot absence negative **G13-RI-000044**, the 1651-52 proprietary-right-not-
residence + John Read comparator analysis **G13-RI-000045**, and the Aylesbury-Vale
Bucks neighbour-cluster reception analysis **G13-RI-000046** (Mass. Archives 129:16
deposition, via `history-of-weymouth`) — with markers **G13-PM-000026..000028**.
Loaded transactionally (arrival batch + two editor source-links + Weymouth batch)
across database revisions 18–21; snapshot at revision 21
(`data/context-graphs/g13/exports/snapshots/g13-context-r000021.ndjson`); validate 0/0.
Both topics carry `coverageStatus: increment-complete` in `manifest.json` — their own
journey/parity/friction gaps are zero; the residual gaps on shared multi-destination
rows (Sprague, Adams, Suffolk probate index, FS Liber V) are Braintree/material/
frontier-scoped (Threads 4–5). Dump findings F11 (Hingham arrival-vector) and F-R4.5
(Jenner's Venn/Essex origin) were reviewed and explicitly retained as backlog to
record-coverage / migration-network (their Weymouth bearing already carried in RI-000020/021).

Leads bearing on this increment — **L-182** (Weymouth grants → RI-000019), **L-185**
(Ludden Old-Planter reception → RI-000022), **L-190** (Jenner credit tie → RI-000020/021) —
were tagged in the production catalog via `research_leads.py --append-status-note` with a
`[G13-STAGING 2026-07-04: …]` note (append-only; `Source ref` left production; backup in
`_local/backups/`). Find them with `research_leads.py search G13-STAGING`; at cutover, review
each, finalize via `update`/`close`, and strip the tag.

Plan 2b Thread 5 — source-lossless remediation (2026-07-05, bounded to
`04-frontier-rights.md`): closed both frontier gaps without adding items (the unit's
`G13-RI-000024..000032` identities were all sound). **Journey gap:** the Billerica block's
`braintree-records-1640-1793-1886` — the primary Braintree town record of the 1647 Daniel
Shed × Mary Gurney marriage (seven Shed births 1647–1658) that makes Daniel John's son-in-law,
behind the "in answer for his father John Gurney" surrender — is now linked `context_for`
**G13-RI-000029** as a second witness alongside the compiled `shedd-daniel-shed-genealogy-1920`;
the frontier `[^shedd]` footnote was expanded to cite both. **Parity gap (§4.1):** Nash's
Appendix C p.282 great lot no.16 (2 Feb 1651/2), cited in prose but linked to no item, is now
linked `context_for` **G13-RI-000031** as the earliest instance of the proprietary-right-without-
residence pattern (cross-unit comparator; its 1651-52 analysis home stays
`02-weymouth-community.md` RI-000045, landholding-context home `01-arrival-chronology.md`).
The John's-own-rights vs posthumous widow/descendant boundary is intact (1662 allotment RI-000026;
post-1667 print-stream chronology as the `open_question` RI-000032; the widow/descendant stream
stays backlog for `g13-family-mendon-descendants`). `suffolk-probate-index-v2-1895` (the Case #338
discovery/index trail) is coordinated to material-life (Thread 4), not linked in frontier. Loaded
as two `editor.commit_change add_source_link` transactions across database revisions 21→23;
snapshot at revision 23 (`data/context-graphs/g13/exports/snapshots/g13-context-r000023.ndjson`);
validate 0/0. `04-frontier-rights.md` carries `coverageStatus: increment-complete` in
`manifest.json` — its own journey/parity/citation/source-set gaps are zero.

Plan 2b Thread 4 + Thread 6 — source-lossless remediation of `03-braintree-community.md`
+ `05-material-life.md`, and Plan 2b closeout (2026-07-05). Thread 6's audit found Thread 4
had not been run: the checker still reported 11 source-journey gaps (Braintree/material-life)
and 6 record-coverage prose↔graph parity gaps. **Record-coverage parity:** the six
"six-record-basis" cross-links (`massachusetts-bay-records-v1-1853`, `suffolk-deeds-liber-iv-1888`,
`nehgr-62-94`, `spr-case-338…`, `nehgr-12-suffolk-wills-1858`, `anderson-great-migration-begins-v1-baxter`)
were tagged `cited_role=context_for` rather than the §8.4 exemption keyword; retagged
`→ cross_unit` (citation-ledger only). **Thread 4:** a new canonical occupation finding
**G13-RI-000047** ("a tailor by trade, a husbandman by economy") + marker **G13-PM-000029**
authored into **Braintree** — it DEPENDS_ON the 1661/2 tailor deed RI-000013 and, cross-unit,
the material-life no-tools negative RI-000036 and husbandry finding RI-000034, and carries
Sprague's compiled Braintree genealogy (`sprague-braintree`, supports) as published
corroboration. Six source links to existing items: the Suffolk Deeds Liber V registry copy
read via FamilySearch full-text (`familysearch-fulltext-search` → deed RI-000013, "John Gurney
of Braintry Taylor"); Adams's *History of Braintree* (1891) and "Genesis of the Massachusetts
Town" (1892) → Tyng-leasehold RI-000011 (Tyng's non-resident Mount Wollaston proprietorship);
and the FamilySearch probate file-papers image (`fs-suffolk-probate-1636-1915`, supports) +
George's 1895 Suffolk probate index (`suffolk-probate-index-v2-1895`, discovery_only) → the
material-life inventory RI-000033. Legacy row l.107 destination extended to material-life +
frontier to match the block's fan-out. Loaded across database revisions 24–35 (author-batch +
5 source-links + 5 locator fixes + hash-sources); snapshot at revision 35
(`data/context-graphs/g13/exports/snapshots/g13-context-r000035.ndjson`); validate 0/0, all
tiers aligned. **All Plan 2b source-lossless categories are now zero** (journey 0, parity 0,
publication 0, friction 0, inventory 0); backlog unchanged at 148 (the unauthored
family/origin/identity/research-state topics — the expected whole-refactor `RESULT: FAIL`).
All six colonial topics carry `coverageStatus: increment-complete`. **GO for resuming normal
G3 topic authoring.**

Phase G3 increment (2026-07-05, bounded): `topics/research-state/40-source-coverage.md`
(topicId `g13-research-source-coverage` — the first **research-state** topic), co-authored
with research items `G13-RI-000048..000053` and three prose evidence markers
`G13-PM-000030..000032`. A non-identity meta-topic on the **research-state coverage of the
online research infrastructure searched beyond the FamilySearch / Internet Archive / Google
corpus** — distinct from `06-record-coverage.md` (the shape of the surviving *colonial* record).
Assimilates the July 2026 full-text campaign's two single-home source-coverage findings (dump
round 4): **F-R4.7** — three Coldham/Ancestry emigrant-compilation negatives, *English
Adventurers and Emigrants 1609–1660* (RI-000048; only "Gurnard's Head" place hits), *Emigrants
in Bondage 1614–1775* (RI-000049; earliest Gurney 1683, out of window), and *Child Apprentices
… Christ's Hospital 1617–1778* (RI-000050; all 18th-c.) — and **F-R4.10** — New England's
Hidden Histories (RI-000051; no pre-1690 church book for John's towns) and Digital Commonwealth
(RI-000052; zero "Gurney Braintree"). All five `negative_within_scope` items SUPPORT the coverage
synthesis **RI-000053**, which CONTEXTUALIZES the record-coverage origin-silence negative
RI-000042 (cross-unit) and names the residual — Coldham's *Complete Book of Emigrants 1607–1660*
(not on Ancestry) + TNA E 157/20 — as the outstanding emigrant-record pull (lead **L-170**,
tagged via `research_leads.py --append-status-note` `[G13-STAGING 2026-07-05: …]`). Five new
sources registered in `data/sources.json` (v1.8.0) with validation worksheets and baselined:
`ancestry-english-adventurers-emigrants-1609-1660`, `ancestry-emigrants-in-bondage-1614-1775`,
`ancestry-child-apprentices-christs-hospital-1617-1778`,
`nehh-congregational-library-colonial-church-records`, `digital-commonwealth`. Loaded across
database revisions 36–38 (sync-sources + author-batch + hash-sources); milestone snapshot at
revision 38 (`data/context-graphs/g13/exports/snapshots/g13-context-r000038.ndjson`); validate
0/0, all tiers aligned. Per-increment gates hold: source-journey, topic-graph-source, publication,
and input-source-set gaps all 0; no new friction; backlog 148 → 146 (the two dump findings
dispositioned). `coverageStatus: increment-complete` in `manifest.json`. The colony-level
record-class negatives (Boston First Church, Book of Possessions, Providence/Garnet) and the
legacy Sources-Consulted / Negative-Results catalogue remain backlog — their primary homes are
`g13-colonial-record-coverage` and the identity/origin units, not this research-state topic.

Phase G3 increment (2026-07-05, bounded): `topics/research-state/41-open-questions.md`
(topicId `g13-research-open-questions` — the second **research-state** topic), co-authored
with research items `G13-RI-000054..000057` and four prose evidence markers
`G13-PM-000033..000036`. A non-identity meta-topic reconciling the **open research program**
for John Gurney against the canonical `research-leads.csv` index. It states the small set of
standing questions as `open_question` items — the English origin and parentage (RI-000054;
DEPENDS_ON the record-coverage origin-silence RI-000042; no candidate advocacy — disambiguation
stays with the dedicated identity/origin work), the first wife Mary's identity and English
marriage (RI-000055), and the untested Y-DNA discriminator (RI-000056; carries
`ftdna-gurney-ydna`, R1b-DF19 › R-Z27053 › R-FTD83678, kit 576097, discriminating test kit
365744) — and a reconciliation `analysis` (RI-000057) that SYNTHESIZES the three and
CONTEXTUALIZES the source-coverage emigrant residual RI-000053. The record-location residuals
already homed elsewhere (the emigrant-record pulls in `40-source-coverage.md`; the 1645 Braintree
petition primary source; the post-death Mendon stream) are cross-referenced, not re-homed. A
value-add WIP-leads table groups the not-yet-assimilated leads by the question they serve, with a
caveat lede that the leads catalogue is canonical and the table restates no lead detail. One new
source baselined (`ftdna-gurney-ydna`); loaded across database revisions 39–40 (author-batch +
hash-sources); milestone snapshot at revision 40
(`data/context-graphs/g13/exports/snapshots/g13-context-r000040.ndjson`); validate 0/0, all tiers
aligned. Per-increment gates hold: source-journey, topic-graph-source, publication, and
input-source-set gaps all 0; no new friction; backlog 146 → 142 (four routed blocks dispositioned —
the legacy Y-DNA block, dump §9.2, and the two immigration-topic next-work blocks). Prose cites
`anderson-gmd-2015` (cross_unit) and `banks-brownell-1937` (context_only). Leads **L-139** (first
wife Mary → RI-000055) and **L-145** (Y-DNA → RI-000056) tagged via `research_leads.py
--append-status-note` `[G13-STAGING 2026-07-05: …]` (append-only; `Source ref` left production).
`coverageStatus: increment-complete` in `manifest.json`. The multi-destination legacy blocks
("Open Questions", "Target source pulls", "Online and full-text lead dispositions") and dump §9.3
are only partly borne here and stay backlog (annotated, not false-closed); candidate
disambiguation, the Cheny/Kidbee 1661 marriage line, and the Edward/Agnes and Haberdashers threads
remain the identity/origin and G14 work.

Phase G3 increment (2026-07-06, bounded): `topics/family/10-wives-marriages.md`
(topicId `g13-family-wives-marriages` — the first **family** topic), co-authored with
research items `G13-RI-000058..000064` and four prose evidence markers
`G13-PM-000037..000040`. John Gurney's two marriages, depth over breadth. The evidential
core resolves the century-old "Cheny/Girny" reading of the 1661 Braintree town record: the
1886 print enters both John's second marriage and his first wife's death under a *Cheny*
surname (source_evidence **RI-000058**), but the fair-copy manuscript read at image level
(DGS 007009769) shows the groom in ink as "John Girny, Senior" with "Cheny/Kidbee" only a
later pencil margin note (source_evidence **RI-000059**), and Pope's 1900 *Pioneers of
Massachusetts* independently ruled the printed Cheny a typographical error
(published_source_statement **RI-000060**) — together resolving "John Cheny" to John Gurney
(research_finding **RI-000061**, ~85–90%; residual = the deaths-page letterform). The second
marriage to the much-married widow Grizzell (12 Nov 1661, **RI-000062**) and the first wife
Mary (maiden name unknown; married in England by the mid-1620s, bounded by daughter Mary's
1647 Shed marriage; died Braintree 20 Sep 1661, **RI-000063**) are carried with their
fact-sheet Vitals-Marriage(s) publication mappings; the unrecovered English marriage is a
wildcard-level `negative_result` (**RI-000064**). One cross-unit edge: RI-000062 QUALIFIES the
record-coverage "no vital record" negative RI-000041 — two Braintree town-record vital lines
do survive for John, under a misread surname. One new source registered
(`pope-pioneers-of-massachusetts-1900`, `data/sources.json` v1.9.0 + validation worksheet) and
baselined. Loaded across database revisions 41–43 (sync-sources + author-batch + hash-sources).
An Allen-review correction pass then applied six fixes via `editor.commit_change` ops across
revisions 45–53 (snapshot **r000053**): (1) topic file reordered so the wives read
chronologically — first wife Mary before the widow Grizzell; (2) the first-wife **forename
"Mary" sourced to Sprague's compiled Braintree genealogy**, with the primary death record and
Torrey both leaving her unnamed ("the wife of John"); (3) the "mother of all his children"
claim softened to a presumption, since no child's birth record survives; (4) the
English-marriage negative reframed so the Findmypast wildcard sweep reads as one rigorous
instance of a broader parish-collection search, not the whole of it; (5) the missing
primary-record witness added — `braintree-records` (p. 717) now cites the second-marriage
finding **RI-000062** directly, and Torrey added to first-wife **RI-000063**; (6) the confusing
"will not be moved by mis-indexing" phrase rewritten in plain terms (and RI-000064 reconciled to
the topic file's provider list). Milestone snapshot at revision 53
(`data/context-graphs/g13/exports/snapshots/g13-context-r000053.ndjson`); validate 0/0, all tiers
aligned. Per-increment gates hold: source-journey, topic-graph-source,
publication, and input-source-set gaps all 0; no new friction; backlog 142 → 137 (five routed
blocks dispositioned — the legacy Grizzell and Mary-English-birth blocks, dump F1/F7, and the
fact-sheet Marriage(s) row). Lead **L-11** (Braintree manuscript vital records) advanced via
`research_leads.py --append-status-note` `[G13-STAGING 2026-07-06: …]`. `coverageStatus:
increment-complete` in `manifest.json`. Deliberately not poached: John's children as a group
(`g13-family-family-group`), the post-1662 Grizzell / John-Jr.-Ruth Mendon proprietary and
descendant stream (`g13-family-mendon-descendants`), the daughter Mary's own English-birth
window and the English-origin identity question (identity/origin units) — the multi-destination
case-file s1/s6 rows are only partly borne here and stay backlog, annotated not false-closed.
Also carried as backlog: Pope's "[Arch. 45]" 1646 Braintree meadows petition (dump F1), routed
to braintree-community / record-coverage pending Massachusetts Archives vol. 45 registration.

Phase G3 increment (2026-07-06, bounded): `topics/family/11-family-group.md`
(topicId `g13-family-family-group` — the second **family** topic), co-authored with
research items `G13-RI-000065..000068` and two prose evidence markers
`G13-PM-000041..000042`. John Gurney's children reconstructed as a **family group**, depth
over breadth — the roster itself, not the per-child biographies. The core finding
(**RI-000065**, moderate-high) states a five-child group — Sarah, Mary, Richard (the
direct-line G12), John Jr., and Peter — with Isaac a probable but unproven sixth, all born
to first wife Mary, and no single colonial record enumerating the family: it is assembled
from the compiled Braintree and Gurney genealogies (`sprague-braintree`, `history-of-weymouth`,
`rigler-gurney-family-aaron-zuinglius-1994`) and per-child primary records. Torrey's one-page
John1 family-group cross-check is carried as source_evidence **RI-000066** (SUPPORTS the
roster). The unit's own depth is the **Isaac identification**: analysis **RI-000067**
(moderate) argues the young *Isacke Gurney* of the 1663/4–1667 colonial court cluster is most
plausibly John-1's son by elimination, QUALIFYING the roster, supported by the court-cluster
source_evidence **RI-000068** (Plymouth 1663/4 Scituate; Suffolk County file no. 792, 1667,
via FamilySearch full-text) — while the dedicated `research/people/isaac-gurney-scituate-boston.md`
subject file still holds him cautiously as a distinct person. RI-000065 publication-maps to the
fact-sheet Children section and case-file s1; RI-000067 to the fact-sheet Children note. No new
sources or entities were registered; `rigler-gurney-family-aaron-zuinglius-1994` was baselined at
hash-sources. Loaded across database revisions 54–55 (author-batch + hash-sources); milestone
snapshot at revision 55 (`data/context-graphs/g13/exports/snapshots/g13-context-r000055.ndjson`);
validate 0/0, all tiers aligned. Per-increment gates hold: source-journey, topic-graph-source,
publication, and input-source-set gaps all 0 for the touched topic; no new friction; backlog not
increased. `coverageStatus: increment-complete` in `manifest.json`. Deliberately not poached:
Mary's 1647 Shed marriage and the couple's English-marriage window (`g13-family-wives-marriages`,
`shedd` cited cross_unit); the post-1662 John-Jr./Ruth Mendon household, the descendant stream,
and Peter's King Philip's War service (`g13-family-mendon-descendants`, `bodge` cited cross_unit);
Richard's own line (the direct-line G12 subject, external); and the origin/identity use of the
roster as a matching criterion (identity units). The multi-destination fact-sheet Children and
case-file s1 rows are only partly borne here and stay backlog, annotated not false-closed.

Phase G3 increment (2026-07-06, bounded): `topics/origin/20-age-baptism.md`
(topicId `g13-origin-age-baptism` — the first **origin** topic; a new `origin` manifest
group), co-authored with research items `G13-RI-000069..000071` and two prose evidence
markers `G13-PM-000043..000044`. The chronology of John's own age and birth, depth over
breadth — deliberately the age question, not the identity/parentage argument. The evidential
anchor is his single primary same-person age datum: the 1652/3 *Wilson v. Faxon* Braintree
deposition, "John Gurney of Brayntree aged 50 Yeares or thereabouts" (Suffolk Court Files
no. 188), carried as source_evidence **RI-000069** and pointing to a birth c.1602/3. The
birth-window finding **RI-000070** (moderate; born c.1602–1610, probably c.1603–1608) is
SUPPORTED by the deposition and DEPENDS_ON the marriages-unit first-wife finding RI-000063
(the marriage-by-later-1620s bound from daughter Mary's 1647 Shed marriage), and
publication-maps to the fact-sheet Vitals-Born row (now its canonical home; the published
c.1607–1612 bracket, the East Dereham-baptism end, sits inside the finding's window).
Analysis **RI-000071** reconciles the deposition age against the identity work's probable
East Dereham baptism (c.1609/10), QUALIFYING RI-000070 and ANALYZING RI-000069. The
paleographic identification of Entry E and the whole Candidate-B parentage argument stay
external (identity units + the G14 Francis companion); the register reading is cited
`nro-pd-86-41` **cross_unit** with no in-unit item, as is `shedd` for the marriage bound.
No new sources or entities registered (all three cited ids already baselined). Loaded
transactionally at database revision 56; milestone snapshot at revision 56
(`data/context-graphs/g13/exports/snapshots/g13-context-r000056.ndjson`); validate 0/0, all
tiers aligned. Per-increment gates hold: source-journey, topic-graph-source, publication,
and input-source-set gaps all 0 for the touched topic; no new friction; backlog not
increased. `coverageStatus: increment-complete` in `manifest.json`. Deliberately not poached:
the East Dereham register review and sibling structure and the paleographic identification
(case-file s4/s5, identity/G14 — stay backlog, annotated not false-closed); daughter Mary's
own English-birth window (`g13-family-wives-marriages`); the recurring Find-a-Grave "1615"
memorial tradition (`g13-origin-traditions`); and the general colonial vital-/church-record
silence (`g13-colonial-record-coverage` RI-000041).

Phase G3 increment (2026-07-06, bounded): `topics/origin/21-trade-training.md`
(topicId `g13-origin-trade-training` — the second **origin** topic), co-authored with
research items `G13-RI-000072..000075` and four prose evidence markers
`G13-PM-000045..000048`. The origin/formation bearing of John's tailoring trade, depth over
breadth — what his trade says about his English training, not the occupation fact itself
(that stays `g13-colonial-braintree-community` RI-000047, cross-referenced in prose without
re-citing its deed/Sprague witnesses). The evidential core is a **double documentary silence
across the two surviving formal trade-transmission pathways**: the Merchant Taylors' Company
of London binding/freedom rolls 1583–1800 (Scott, UKDA-SN-9263) show no John-son-of-Francis
binding and zero Gurney patrimony freedoms (`negative_result` **RI-000072**), and the Norwich
freemen register (Millican 1934) and enrolled apprentice-indenture index (Rising & Millican,
NRS 29, 1959) show no John Gurney freedom or enrolled apprenticeship c.1615–1660 — the sole
17th-c Gurney being James, son of Francis of St Peter Parmentergate (bound 1627) — (`negative_result`
**RI-000073**). The synthesis finding **RI-000074** (moderate) reads the trade as learned by
informal or country training off the enrolled books, SYNTHESIZES both negatives, and DEPENDS_ON
the Braintree occupation finding RI-000047 (cross-unit). Analysis **RI-000075** (moderate-high)
carries the one enrolled "John Gurney" apprenticeship in the New England orbit — the 21 July 1636
Newgate indenture — as a de-conflated younger man (birth ~1615 vs the deposition's c.1602/3),
SUPPORTING RI-000074; the fuller two-Johns de-conflation stays with the identity work. Three
sources journeyed here (`ukda-9263-mt-apprentices-scott-2024`, `millican-register-freemen-norwich-1934`,
`rising-millican-norwich-apprentices-index-nrs29-1959`, `winthrop-history-new-england-addenda-1636`);
`ukda-9263`'s `corpusPath` was repointed to its Gurney-variants extract CSV (`data/sources.json`
v-bump) so the cited artifact resolves and hash-baselines. Loaded across database revisions 57–60
(author-batch + hash-sources + sync-sources + hash-sources); milestone snapshot at revision 60
(`data/context-graphs/g13/exports/snapshots/g13-context-r000060.ndjson`); validate 0/0, all tiers
aligned. Per-increment gates hold: source-journey, topic-graph-source, publication, and
input-source-set gaps all 0 for the touched topic; no new friction; backlog not increased.
`coverageStatus: increment-complete` in `manifest.json`. Two frozen legacy blocks are partly borne
here and stay backlog, annotated not false-closed: "The Newgate apprenticeship / 1636 record –
de-conflated" (l.306; `winthrop-addenda` journeys, the Newgate-not-Gurney negatives remain →
identity) and "Online and full-text lead dispositions" (l.393; the two Norwich sources journey,
the other eight lead-search sources remain → identity/origin + source-coverage). Deliberately not
poached: the colonial occupation fact and its deed/Sprague witnesses (`g13-colonial-braintree-community`
RI-000047); the tailor-without-tools inventory negative (`g13-colonial-material-life` RI-000036);
the Christ's Hospital emigrant-apprentice negative (`g13-research-source-coverage` RI-000050); and
the Candidate-B parentage argument that Francis Gurney was himself a Merchant Taylor (case file /
identity work, external-canonical). The Merchant Taylors' analysis file
(`research/topics/merchant-taylors-1583-1800-gurney-analysis.md`) is outside the Plan 2b frozen
inventory, so `ukda-9263` needs only a citation-map row, not a legacy/supplemental row.

Phase G3 increment (2026-07-06, bounded): `topics/origin/22-migration-network.md`
(topicId `g13-origin-migration-network` — the third **origin** topic; manifest `order` 40;
heading_id `origin-migration-and-reception-network` slug-matches H1 "Origin — migration and
reception network"), co-authored with research items `G13-RI-000076..000079` and three prose
evidence markers `G13-PM-000049..000051`. **Depth over breadth on the non-identity
reception-network reading of John's arrival — the §18 origin/parentage disambiguation stays
external to the identity units.** Finding-first: John left no record of his Atlantic crossing,
so his migration is knowable only as a reception pattern. Research finding **RI-000076**
(moderate) reads his colonial debut as reception into an already-established Weymouth community
(his 1641 co-named men Ludden and Richard Porter, and his residual creditor John King, were
settlers of a half-generation's standing) — SYNTHESIZES the Weymouth associate reading RI-000022
and DEPENDS_ON the arrival gunpowder record RI-000001, both cross-unit. Two first-class negatives
bound the crossing: **RI-000077** (moderate-high), no John Gurney variant on the three surviving
near-window passenger lists (Bevis 1638, Diligent 1638, Mary Anne 1637, via Banks and Drake), and
**RI-000078** (moderate), no Gurney in the Hingham town records by full-text search (the Hobart
journal untested/gated) — both SUPPORT RI-000076. Analysis **RI-000079** (moderate) QUALIFIES the
finding: the reception network fixes the mode of settlement but is a weak lever for English origin
(documented associates span Bucks/West-Country/Essex/Warwickshire/Suffolk/Norfolk), so the
origin-corridor question is held to the identity work. **Two new sources registered**:
`banks-planters-of-the-commonwealth-1930` and `drake-result-of-researches-1860` (`data/sources.json`
v1.9.0→**1.10.0** + thin validation worksheets), both baselined and journeying via RI-000077.
Loaded across database revisions 61–63 (sync-sources → author-batch r62 → hash-sources r63);
milestone snapshot at revision 63
(`data/context-graphs/g13/exports/snapshots/g13-context-r000063.ndjson`); validate 0/0, all tiers
aligned. Per-increment gates hold: source-journey, topic-graph-source, publication, and
input-source-set gaps all 0 for the touched topic; no new friction; backlog not increased.
`coverageStatus: increment-complete` in `manifest.json`. Assimilated: the immigration-topic
"Working interpretation" row (→ RI-000076/000079) and the Bevis/Diligent/Mary-Anne passenger-list
negative (→ RI-000077); the dump F11 Hingham FTS negative facet (→ RI-000078, the Hobart-journal
arrival-vector lead and record-coverage bearing stay backlog). Lead **L-188** advanced via
`[G13-STAGING 2026-07-06 …]` append-only. Deliberately **not** poached (reviewed, held external,
annotated not false-closed): the Candidate-B / Bucks-as-origin / Hingham-corridor-for-Candidate-B
threads (immigration topic, case-file s7 Ann Gurney × Gilman, legacy corridor blocks →
identity/origin units); the F-R5 English patronage/wardship-network class and F-R4.5 Jenner
eastern-counties origin (→ `g13-origin-wardship-network` / identity); the Weymouth-reception slice
already carried in `g13-colonial-weymouth-community` RI-000046. Cross-unit prose citations
(`suffolk-deeds-liber-iv-1888`, `shedd-daniel-shed-genealogy-1920`) carried `cited_role=cross_unit`
in the citation map (parity-exempt); no in-unit item link pulled for the colonial occupation/land
witnesses.

Phase 2 revision increment (2026-07-10, bounded): `topics/origin/22-migration-network.md`
(`g13-origin-migration-network`), assimilating the case-file §7 Ann Gurney × John Gilman connection —
the one input to this unit that had no staged home. Three new items via `author-batch` (rev 177):
source_evidence **RI-000189** (the Gilman–Gurney family record — Ann × John Gilman, worsted weaver,
married Hingham, Norfolk 1 Oct 1626; children baptised West Dereham and Hingham; Ann buried Hingham
23 Nov 1651; son John Gilman Jr. → Exeter, NH; cites `hingham-register` + `davis-abel-lunt-1963`);
open_question **RI-000190** (was Ann John's sister? — Pease's compiled claim held at **low** confidence,
qualified by the confounding West Dereham 1618/19 Woodcocke marriage `freebmd-freereg`, and the West-vs-East
Dereham twenty-mile trap); analysis **RI-000191** (moderate — the marriage as a concrete Gurney thread on
the Norfolk-to-New-England corridor, `blomefield-norfolk` for Hingham as Gurney manorial territory; SUPPORTS
the corridor finding RI-000091, DEPENDS_ON RI-000190). One new marker **G13-PM-000114**. All four case-file
§7 source ids journey in-unit; the case file is a cross-reference only. Snapshot `g13-context-r000177.ndjson`;
validate 0/0, all tiers aligned; per-increment gates all 0 (parity, source-journey, topic-graph-source,
publication, input-source-set, friction). **Left in backlog, reported not false-closed:** F-R4.5 (Rev. Thomas
Jenner) — his Weymouth credit tie stays in `g13-colonial-weymouth-community` RI-000020/021 and his own
Essex-origin/Coltishall-Norfolk-end track is identity content needing the unregistered Venn source; and the
Aylesbury-Vale Bucks neighbour cluster — its reception bearing is already homed (RI-000046 Weymouth, RI-000090
here), the residual Bucks-as-origin nuance is identity work. Note: F-R4.6 (Brackett brothers → Sudbury/Gurdon
vector) sits in backlog on this unit from the braintree increment's re-route but was outside this increment's
three-input scope; it remains for a future migration-network revision.

Phase G3 increment (2026-07-06, bounded): `topics/origin/23-wardship-network.md`
(topicId `g13-origin-wardship-network` — the fourth **origin** topic; manifest `order` 50;
heading_id `origin-wardship-and-patronage-network` slug-matches H1 "Origin — wardship and
patronage network"), co-authored with research items `G13-RI-000080..000085` and five prose
evidence markers `G13-PM-000052..000056`. This authors the F-R5 English patronage/wardship-network
class the migration-network increment deferred. **Depth over breadth, strict non-advocacy: the
unit assembles the ward-line network as origin-bearing context about the senior West Barsham
branch, and explicitly does NOT connect John to it — the Candidate-B identity question is held to
the case file (§18 "expensive and hard to reverse").** Finding-first: in John's emigration decade
the senior branch stood inside the Massachusetts founders' Court-of-Wards circle. Evidence items:
the 1627 Gurdon→Winthrop letter (**RI-000080**, the widowed "mrs. Gurny" presenting through
Winthrop and Downing at the Court of Wards); the wardship structure (**RI-000081** — Edward Gournay
a minor ward under his mother Martha Lewkenor, of age c.1628; Edward's 1641/2 IPM C 142/613/60);
and the Gurdon–Sedley–Lewkenor puritan matrix (**RI-000082**, Muskett). Finding **RI-000083**
(moderate-high) SYNTHESIZES 080/081/082; analysis **RI-000084** (moderate) QUALIFIES it as a weak
lever for John's own origin; open_question **RI-000085** carries the unidentified clergyman
"Warford" (Venn + Foster negatives; CCEd the remaining route), DEPENDS_ON 080. **Four new sources
registered** (`data/sources.json` v1.10.0→**1.11.0** + thin validation worksheets):
`mhs-winthrop-papers-gurdon-to-winthrop-1627`, `muskett-suffolk-manorial-families-v1-1900`,
`tna-ward-c142-west-barsham-gurney-inquisitions`, `foster-alumni-oxonienses-1500-1714`; existing
`armstrong-norfolk-1781`, `farrer-church-heraldry-norfolk`, `blomefield-norfolk`,
`alumni-cantabrigienses-venn`, and `familysearch-fulltext-search` also linked. **Review catch
(important):** the source dump read the WARD 7/57/157,/80 items (14–15 Jas I) as Thomas Gurney III's
death IPMs, dating him c.1616/17 — this **conflicts with the repo's verified finding** (lead
**L-113** / the G15 companion) that Thomas III was living in Henry G15's 1 May 1621 will and died
1621×1623 *vita patris*. Corrected RI-000081/RI-000083, the prose, and the source/validation notes:
Thomas III d. 1621×1623 (predeceasing Henry G15, d. 1623), Edward a minor at his 1623 succession;
the early WARD items held as catalogue leads; `familysearch-fulltext-search` (Henry's 1621 will)
added to RI-000081 as the chronology witness. Lead **L-113** advanced via `[G13-STAGING 2026-07-06 …]`
append-only. Loaded across database revisions 64–77 (sync-sources → author-batch r65 → hash r66 →
snapshot; Foster: sync r67 → add_source_link r68 → hash r69; corrections r70–75 → sync r76 →
hash `--accept-current` r77); milestone snapshot at revision 77
(`data/context-graphs/g13/exports/snapshots/g13-context-r000077.ndjson`); validate 0/0, all tiers
aligned. Per-increment gates hold: source-journey, topic-graph-source, publication, and
input-source-set gaps all 0 for the touched topic; no new friction; backlog **decreased** 132→127.
`coverageStatus: increment-complete` in `manifest.json`. Assimilated dump findings: Input-4
(TNA WARD → RI-000081), F-R3.1 (Muskett → RI-000082), F-R3.3 (Winthrop letter → RI-000080/000085),
F-R7 and F-R4.8 (Warford negatives → RI-000085). Multi-destination partials kept in backlog,
annotated not false-closed: F9 (Gurdon-letter flagship — Candidate-B identity bearing external),
F-R1 (direct-ancestor IPMs → English-line files), F-R3.2 (Martha Heigham will — identity bearing
external), F-R3.7 (Adam Winthrop diary detail not carried). **Visibility note for review:** items
and markers were authored `public`, matching the sibling origin topics and the migration-network
precedent for identity-adjacent-but-non-advocacy material; because the core finding is Candidate-B
senior-branch substrate, this publication call should be confirmed at the dedicated identity pass
and can be flipped to `repo_only` with one `set_visibility` batch if a review gate is preferred.

---

Phase G3 review-revision (2026-07-07, Opus): reworked the three already-authored
origin topics `topics/origin/20-age-baptism.md`, `topics/origin/21-trade-training.md`,
and `topics/origin/22-migration-network.md` after Allen's review, for cohesive plain-spoken
narrative and to add material that had been lost. **Age-baptism** was rebuilt around four
chronological handles of unequal strength: added a source_evidence item for the parents'
marriage (Francis Gurney × Margaret Rybett, 23 Sep 1611, St Martin at Palace, Norwich, `nro-pd-12-1`
+ `findmypast-norfolk-banns-marriages-index`) as **G13-RI-000086**, and an analysis item on the
decade-rounded ("age heaping") reading of the deposition age as **G13-RI-000087** (new source
`shepard-spicksley-worth-age-2011` registered; `data/sources.json` v1.11.0→**1.12.0**); revised the
birth-window finding RI-000070 and the reconciliation analysis RI-000071 to a probable (1604–1608)
vs possible (1602–1610) framing; embedded Allen's evidence-range figure at
`topics/origin/figures/john-gurney-birth-year-ranges.png`; markers **G13-PM-000057/000058** added,
RI-000070 removed from PM-000043. **Trade-training** gained an orientation item **G13-RI-000088**
(the father-son / family-textile expectation: Francis a Merchant Taylor, the 1622 King's Lynn
worsted-yarn scheme via `bho-hmc-kings-lynn-misc-writings` and `ukda-9263`, the Gurney Norfolk wool
setting) + marker **G13-PM-000059**, and plain-language cleanup throughout. (Note: Henry G15's 1621
will carries **no** wool-trade content — a farmer's/gentleman's will — so that recollection was not
asserted; the concrete textile links are Francis himself and the wider family setting.)
**Migration-network** was substantially expanded from ~10% to a fuller synthesis with links out to
`research/topics/g13-john-gurney-immigration-by-association.md` and
`research/topics/massachusetts-bay-passenger-lists-bevis-diligent-mary-anne.md`: added
**G13-RI-000089** (Great-Migration timing — passenger silence expected in the thin 1639–41 tail),
**G13-RI-000090** (the Weymouth land-and-neighbour reception network / immigration by association),
and **G13-RI-000091** (the Norfolk–Hingham reception corridor, the Diligent cohort out of the very
Gurney parishes — Great Ellingham, Hingham, Dereham) + markers **G13-PM-000060/000061/000062**;
RI-000078 moved from PM-000050 to PM-000062. Loaded across database revisions 78–86 (sync-sources
r78 → age-baptism author-batch r79 → editor ops r80–82 → trade-training author-batch r83 →
migration author-batch r84 → editor op r85 → hash-sources r86); milestone snapshot at revision 86
(`data/context-graphs/g13/exports/snapshots/g13-context-r000086.ndjson`); validate **0/0**, all
tiers aligned, `export-website` builds clean. Per-increment gates all 0 (source-journey, parity,
publication, input-source-set, friction); backlog unchanged (127). All new items/markers authored
`public`, matching the sibling origin topics. Deliberately not poached: the Candidate-B parentage
argument and the East Dereham paleography (identity work + G14 companion, cited cross-unit); the
Weymouth land-grant records (weymouth-community); the arrival dating (arrival-chronology).

Phase G3 increment (2026-07-07, bounded): `topics/origin/24-bury-connections.md`
(topicId `g13-origin-bury-connections` — the fifth **origin** topic; manifest `order` 60;
heading_id `origin-bury-connections` slug-matches H1 "Origin — Bury connections"), co-authored
with research items `G13-RI-000092..000097` and four prose evidence markers
`G13-PM-000063..000066`. **Depth over breadth, one unit: Charles Banks's "Bury St Edmunds"
origin attribution for John Gurney — the one specific English parish any published authority
ever named — resolved, with the Candidate-B identity conclusion held to (and linked to) the
case file, not advocated here.** Finding-first: the attribution rests only on "Banks Mss."
(source_evidence **RI-000092**, `banks-brownell-1937` p.151, with the genuine Bury emigrant
cohort); its cleanest mechanism is John Newgate of Horningsheath (~3 mi from Bury), master of
the 1636 runaway apprentice John Gurney (source_evidence **RI-000093**, `wikitree-newgate-14-horningsheath`);
and the Bury registers hold no natal Gurney household — the St James sweep finds only the too-late
Thomas × Lidda Broddish household (source_evidence **RI-000094**, `bury-st-james-registers`) and
the St Mary burials show a Bury "John Gurney" already buried in 1653 (source_evidence
**RI-000095**, `findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656`). Those two register
searches SUPPORT the `negative_result` **RI-000096** clearing Bury as the emigrant's birthplace,
and finding **RI-000097** (moderate-high) reads Banks's attribution as an unproven lead most
plausibly tracking Newgate's apprentice and consistent with the favoured Norfolk origin —
corroborated by Anderson's "Unknown" (`anderson-gmd-2015` p.158) and DEPENDING_ON, cross-unit,
the trade-training de-conflation RI-000075. RI-000092/093/095/096/097 publication-map to the
case file s8/s10 (which assert the Bury/Newgate/Banks readings); the published fact sheet carries
no Bury claim, so nothing was mapped there. **No new sources registered** — all eight cited ids
were already in `data/sources.json`; four were newly baselined at hash-sources
(`banks-brownell-1937`, `bury-st-james-registers`, `findmypast-bury-st-edmunds-st-mary-gurney-burials-1653-1656`,
`wikitree-newgate-14-horningsheath`). Loaded transactionally at database revision **88**
(author-batch) → hash-sources r89; milestone snapshot at revision 89
(`data/context-graphs/g13/exports/snapshots/g13-context-r000089.ndjson`); validate **0/0**, all
tiers aligned. Per-increment gates hold: source-journey, topic-graph-source, publication, and
input-source-set gaps all 0 for the touched topic; no new friction; backlog not increased.
`coverageStatus: increment-complete` in `manifest.json`. Assimilated: the legacy "Newgate
Horningsheath origin" block (→ RI-000093/000097), the Bury-St-James (L-96) sub-part of the
"Online and full-text lead dispositions" block (→ RI-000094/000096), and the Banks facets of the
"External compiler assessments" legacy block and case-file s8/s10 / candidate-others supplemental
rows (annotated, multi-destination rows not false-closed). **Deferred / re-routed (backlog,
annotated):** dump F-R3.11 (the Thomas Chaplin 1672 Bury will "Mary Gurney my servant" + Jeremy
Houchin New-England debt) — a Bury⇄Boston conduit datum that does not connect to the emigrant's
family — is deferred because its source is Muskett *Suffolk Manorial Families* **vol. 3**, and only
vol. 1 is registered; assimilating it needs a `muskett-…-v3` source + worksheet (a bounded future
increment). Dump F-R3.6 (West Barsham advowson) and F-R3.8 (Elizabeth Gournay × Bozoune Crowe) were
re-routed off this topic to `g13-origin-wardship-network` / `g13-identity-candidate-b` as Norfolk
senior-branch and new-person identity material, not Bury/Suffolk attribution content. Deliberately
not poached: the whole English-origin identity conclusion (John = son of Francis Gurney and Margaret
Rybett) stays in the [case file](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/john-gurney-case-file-v4.md)
§8.5/§10.2, linked from the topic prose; the maternal-Rivett and grandfather/great-uncle-wills legacy
blocks stay backlog to migration-network / research-source-coverage.

Phase G3 increment (2026-07-07, bounded): `topics/origin/25-origin-traditions.md`
(topicId `g13-origin-traditions` — the sixth **origin** topic; manifest `order` 70; heading_id
`origin-traditions` slug-matches H1 "Origin — traditions"), co-authored with research items
`G13-RI-000098..000103` and six prose evidence markers `G13-PM-000067..000072`. **Depth over
breadth, one unit: the American family-memory traditions about John Gurney, weighed for what
they are worth rather than argued into the identity question.** Three American sources —
*American Biography* (1926), the Lysander Franklin Gurney sketch (1912), and a Find a Grave
memorial (no. 252975617) — repeat an identical 29 September 1615 birth with an English place
name (source_evidence **RI-000098**, `american-biography-cyclopedia-v26-gurney-1926`;
`accessgenealogy-lysander-franklin-gurney`; `findagrave-john-gurney-252975617`). Analysis
**RI-000100** (moderate-high) shows the tradition is the true biography of the 1636 Newgate
apprentice — read backward, the court order's age-24-in-1639 clause implies the same 29
September 1615 birth — misattached to the older Braintree emigrant; it QUALIFIES RI-000098,
DEPENDS_ON the trade-training de-conflation **RI-000075** (cross-unit), and CONTEXTUALIZES the
age-baptism birth-window finding **RI-000070** (cross-unit). The same memorial supplies a
distinct, separately checkable datum: source_evidence **RI-000099** places John's burial at Elm
Street Cemetery, Braintree — a citation-worthy lead, publication-mapped to the fact sheet's
Buried field. A second, separate tradition concerns arms: source_evidence **RI-000101** carries
the American arms claim (`american-biography-cyclopedia-v26-gurney-1926`;
`accessgenealogy-lysander-franklin-gurney`) alongside the same blazon's genuine in-situ Norfolk
attestation (`pettigrew-collectanea-house-gournay-1871`; `farrer-church-heraldry-norfolk`;
`armstrong-norfolk-1781`), and `negative_result` **RI-000102** records that no early American
physical or manuscript witness has been found. RI-000101/RI-000102 publication-map to case file
§10 (the "American Gurney arms" evidence-table row, "Weak," conditional on a witness being
found); RI-000100 publication-maps to case file §8 (the elimination table's Newgate-apprentice
row). Finding **RI-000103** (moderate) synthesizes all four — family/compiler memory about John
tends to preserve real information misattached to the wrong subject rather than invent claims
outright — and CONTEXTUALIZES the parallel Bury-connections finding **RI-000097** (cross-unit).
**No new sources registered** — all seven cited ids were already in `data/sources.json`; four
were newly baselined at hash-sources (`accessgenealogy-lysander-franklin-gurney`,
`american-biography-cyclopedia-v26-gurney-1926`, `findagrave-john-gurney-252975617`,
`pettigrew-collectanea-house-gournay-1871`). Loaded transactionally at database revision **91**
(author-batch) → hash-sources r92; milestone snapshot at revision 92
(`data/context-graphs/g13/exports/snapshots/g13-context-r000092.ndjson`); validate **0/0**, all
tiers aligned. Per-increment gates hold: source-journey, topic-graph-source, publication, and
input-source-set gaps all 0 for the touched topic; no new friction; backlog not increased.
`coverageStatus: increment-complete` in `manifest.json`. Assimilated: the legacy "Find a Grave
memorial 252975617" block (synthesized → RI-000098/000099/000100), the tradition facets of the
"American Biography, colonial arms, and the Norfolk-line memory" legacy block (partial →
RI-000098/000101/000102; the Candidate-B identity-weight facet stays backlog to
`g13-identity-candidate-b`), the 1615-tradition sub-bullet of the "Negative Results and
Exclusions" legacy block (partial), and the fact-sheet Buried supplemental row (incorporated) plus
the case-file §8/§10 supplemental rows (partial, annotated). **Deferred/re-routed (backlog,
annotated):** dump F-R3.9 (the L'Estrange jest-book anecdotes upgraded to kin-sourced via the
Lewkenor tie) was re-routed to `g13-origin-wardship-network` — its substance is the West Barsham
senior-branch kinship network, and assimilating it needs a new `muskett-…-v2` source registration
(only vol. 1 is currently registered), a future bounded increment. Deliberately not poached: the
Candidate-B identity weight of the arms tradition (case file, external); Banks's own "Bury St
Edmunds" attribution and the Newgate-Horningsheath mechanism (`g13-origin-bury-connections`,
cited cross-unit); the 1636 apprentice de-conflation itself (`g13-origin-trade-training`, cited
cross-unit).

Phase G3 increment (2026-07-07, bounded): `topics/identity/30-candidate-overview.md`
(topicId `g13-identity-assessment` — the first **identity** topic; new manifest group
`identity`, order 40, between `origin` and `research-state`), co-authored with research items
`G13-RI-000104..000106` and three prose evidence markers `G13-PM-000073..000075`. **Depth over
breadth, one unit: the shared matching-criteria profile and elimination scaffold case file §8
applies across every alternative English John Gurney candidate — not the surviving candidate's
own case, which stays external.** Finding-first: analysis **RI-000104** states the shared
profile (tailor; wife Mary; children Sarah/Mary/Richard/John/Peter; birth c.1602–1610; gone from
English records by June 1641) — SYNTHESIZES five already-homed cross-unit findings (occupation
RI-000047, first-wife RI-000063, family roster RI-000065, birth window RI-000070, arrival window
RI-000006) rather than re-sourcing them. Analysis **RI-000105** (DEPENDS_ON RI-000104) states the
elimination scaffold itself — structural grounds (continuing English residence, wife-name
mismatch, child-set/chronology mismatch, wrong generation) vs. a low residual for single-
attestation households — SYNTHESIZES the Newgate-apprentice de-conflation already authored twice
in this graph (trade-training RI-000075, traditions RI-000100) as the same standard applied to a
same-name case. Finding **RI-000106** (moderate-high) SYNTHESIZES both and states the outcome: of
51 same-name households in case file §8, three principal alternatives (A, C, D) plus 45 further
clearance-sweep households are eliminated, five single-attestation households are held at a
combined ~8% residual, and Candidate B is the sole survivor; it CONTEXTUALIZES the record-coverage
origin-silence negative RI-000042 (elimination-by-profile is the only route to a candidate
conclusion because no record states John's origin directly) and cites `anderson-gmd-2015`
directly (p. 158's own bracketed documentary basis). **Per the explicit task instruction, the case
file's own §11 probability model (~65% for Candidate B) is held external-canonical** — RI-000106
publication-maps to case file §11 and cross-references it without restating the figure; the topic
prose states the current ~65% (v4.3) for the reader with a footnote back to §11 as the canonical
source, so a future case-file revision cannot go stale in the graph silently. RI-000104 and
RI-000105 publication-map to case file §1 and §8 respectively. Two legacy-companion blocks
dispositioned: "Combined Anderson + Banks assessment" (l.282, `synthesized` → RI-000106, the
candidate-standing table + cross-links to the six existing per-candidate topic files) and "Working
Hypotheses" (l.531, `external-canonical` — an exact duplicate of case-file §11's percentages,
explicitly self-described as "case file v4.3 aligned"). Loaded transactionally at database
revision 93 (author-batch; `anderson-gmd-2015` already baselined, no hash-sources needed);
milestone snapshot at revision 93
(`data/context-graphs/g13/exports/snapshots/g13-context-r000093.ndjson`); validate **0/0**, all
tiers aligned. Per-increment gates hold: source-journey, topic-graph-source, publication, and
input-source-set gaps all 0 for the touched topic; no new friction; backlog decreased.
`coverageStatus: increment-complete` in `manifest.json`. Deliberately not poached (reserved for
their own future dedicated identity increments, cross-referenced not restated): the per-candidate
archival detail in the six existing `research/topics/john-gurney-candidate-*.md` files and the
Bucks-cluster immigration-topic row (→ `g13-identity-candidate-a` / `g13-identity-london-candidate`
/ their own case-file-s8-section rows); the Candidate B parentage argument itself — trade,
corridor, motive, network, the East Dereham baptism reading, and its own probability synthesis
(case file §2, §5, §9, §10, §11 → `g13-identity-candidate-b`, unstaged). The case-file s1
family/religion partial row and s6/s10 identity partial rows are only partly borne here (the
matching-criteria facet only) and stay backlog, annotated not false-closed.

Phase G3 increment (2026-07-07, bounded): three dedicated identity topics —
`topics/identity/31-candidate-a-aylesbury.md` (topicId `g13-identity-candidate-a`),
`topics/identity/35-candidate-ackworth.md` (topicId `g13-identity-candidate-ackworth`, new),
and `topics/identity/36-other-eliminations.md` (topicId `g13-identity-other-eliminations`, new,
absorbing both the Earsham candidate file and the same-name clearance-sweep portion of the
"others" comparator file) — co-authored with research items `G13-RI-000107..000120` and eight
prose evidence markers `G13-PM-000076..000083`. **Depth over breadth, one bounded batch of three
small eliminations, each absorbing its `research/topics/john-gurney-candidate-*.md` source file.**
Aylesbury (Candidate A): source_evidence RI-000107 (the Stewkley-Bierton-Aylesbury family chain),
RI-000108 (the wider five-plus-household Bucks map), and RI-000109 (the 1661 Edlesborough
marriage) SYNTHESIZE into finding RI-000110 (Candidate A eliminated), which SYNTHESIZES
cross-unit into the shared elimination scaffold RI-000105. Ackworth: source_evidence RI-000111
(the 1636 marriage and 1637 baptism) grounds analysis RI-000112 (held at residual ~3%, capped by
the naming/birth-order mismatch and the colonial John's own pre-1628 marriage bound — CONTEXTUALIZES
cross-unit the five-child roster RI-000065) and open_question RI-000113 (the parish-register pull,
burial search, and the Mary Barton/Burton tradition-provenance test). Other eliminations + Earsham:
source_evidence RI-000114 (the 1638 Earsham will: wife Mary, son John a minor at fourteen, brother
Syon/Lyon) grounds finding RI-000115 (testator and son both the wrong generation; the family's own
forward-traced genealogy stays external-canonical on `research/people/john-gurney-earsham-will-1638.md`,
a deliberate subject-boundary decision, not backlog); source_evidence RI-000116 (the Gurnell
false-friend), RI-000117 (six-parish Norfolk household-density survey), negative_result RI-000118
(the Richard/Isaac cluster-anchor search, with a structured `negative_result_scope`), and
RI-000119 (the wider English parish/probate/muster clearance sweep — Harrow, Toddington,
Cripplegate, the TNA PCC probate corpus, the Protestation Returns) all SYNTHESIZE into finding
RI-000120 (the combined ~8% residual; Candidate B remains the sole survivor), which SYNTHESIZES
cross-unit into RI-000105. All fourteen sourceIds cited were already registered (no new source
registration this increment). Loaded transactionally at database revision 94 (author-batch);
sources baselined at revision 95 (`hash-sources`); milestone snapshot at revision 95
(`data/context-graphs/g13/exports/snapshots/g13-context-r000095.ndjson`); validate **0/0**, all
tiers aligned. Per-increment gates hold for all three touched topics: source-journey,
topic-graph-source, and publication-mapping gaps all 0; no new friction; backlog decreased
(`supplemental-surfaces-map.csv` rows for the Aylesbury whole-file banner and its three sub-sections,
the Ackworth whole-file row, the Earsham whole-file row, and the "same-name eliminators and
comparators" section of the others file all move to `incorporated`, with new `source-and-citation-map.csv`
rows for every cited sourceId). `coverageStatus: increment-complete` for all three in `manifest.json`.
Deliberately not poached, left backlog for future passes: the Aylesbury FS-Tree-profile caution and
its Medmenham/Richards non-leads; the others file's Costessey/Cawston/Providence/Isaac-Gurney/
Francis-of-Maldon material (each already has its own dedicated `research/people/*.md` subject file,
out of scope for this graph); the East Dereham copyhold-succession chain and NCC will sightings
(external G14 orbit, leads L-5/L-6); and the Margaret Rovett/Rybett open lead (no source id, pending
record review).

Phase G3 increment (2026-07-07, bounded): `topics/identity/34-london-draper.md`
(topicId `g13-identity-london-candidate`), absorbing the whole
`research/topics/john-gurney-candidate-london-draper.md` working file — co-authored
with research items `G13-RI-000121..000125` and four prose evidence markers
`G13-PM-000084..000087`. **One unit, depth over breadth: Candidate D — John Gurney,
son and executor of Robert Gurney, citizen and draper of Old Change — eliminated.**
The identity anchor (source_evidence **RI-000121**) carries Robert's 1625 will naming
John sole executor, Robert's Drapers' freedom since 1581, and John's own 1623/4
Drapers' freedom by redemption (not patrimony); it also folds in Robert's earlier,
pre-1611 St Augustine children, which weaken any assumption that Anne Morris (m. 1611)
was John's mother. Continuing-London-presence evidence (source_evidence **RI-000122**)
carries the 1638 St Augustine £10 rent return alongside the decisive 1662 hearth-tax
entry (1 hearth, "poore," TNA E 179/252/27) and the corroborating Boyd's card. The
elimination finding (**RI-000123**, SYNTHESIZES 121/122, cross-unit CONTEXTUALIZES the
colonial John's 1663 estate inventory RI-000033, cross-unit SYNTHESIZES the shared
elimination scaffold RI-000105) states the clean chronological ground: a London
householder assessed too poor to pay hearth tax in 1662 cannot be the colonial John
dying at Boston the same year. A `negative_result` (**RI-000124**) adds a second,
independent ground — no wife Mary or matching children, and no Anne Gurney widow
probate — and an `analysis` (**RI-000125**) explains the redemption-not-patrimony
anomaly via a probable prior Stationers' Company apprenticeship (the H-D1 hypothesis).
**Friction resolved:** the frozen working file hedged one citation to an unregistered
`ancestry-pcc-wills-1384-1858` placeholder ("existing source if applicable"); it is now
registered properly (`data/sources.json` v-bump + validation worksheet) and cited
directly on RI-000124, rather than left unresolved or duplicated against the existing
`tna-pcc-probate`/`tna-pcc-gurney-elimination-corpus` registrations. Two comparators
kept out of the elimination proper (an unrelated Richard Gurney haberdasher/alderman,
and the Hanging Houghton gentry family) and three still-unretrieved deferred pulls
(the 1661 poll tax, the 1640 Harvey list, the Arber Stationers' Registers raw entry —
no longer load-bearing since the 1662 hearth tax already confirms the elimination) are
carried in prose and linked `mentions` onto the nearest item via a short post-commit
editor pass, so every source_id the legacy file cites journeys into the graph. Loaded
across database revisions 96–106 (sync-sources r95→96 for the new registration,
author-batch r96, hash-sources r97, six editor source-link ops r98–105, hash-sources
r106); milestone snapshot at revision 106
(`data/context-graphs/g13/exports/snapshots/g13-context-r000106.ndjson`); validate
**0 errors** (2 pre-existing, unrelated warnings — missing local image files for two
already-registered LMA parish-register sources); all tiers aligned.
`tools/lint_source_notes.py` PASS. Per-increment gates hold: source-journey,
topic-graph-source, publication-mapping, and input-source-set gaps all 0 for the
touched topic; no new friction (the one pre-existing friction flag on this row is
resolved); backlog not increased (115, same as before this increment — six pre-existing
gaps closed by this pass without adding any). `coverageStatus: increment-complete` in
`manifest.json`. Assimilated: the whole `john-gurney-candidate-london-draper.md` file
(main content row and its Cross-references row, both `incorporated`). Deliberately not
poached, left backlog: the distinct William Gurney London hearth-tax cluster
(1664–1666), which bears on the case file's own "unknown corridor" residual reading,
not on Candidate D's elimination.

Phase G3 increment (2026-07-09, bounded): `topics/family/12-mendon-descendants.md`
(topicId `g13-family-mendon-descendants` — the third **family** topic), co-authored with
research items `G13-RI-000126..000135` and five prose evidence markers
`G13-PM-000088..000092`. **One unit, depth over breadth: John Gurney Jr.'s Mendon household
with his wife Ruth.** John Jr. had settled at Mendon by the early 1670s; the Mendon town book's
birth entry for Samuel (14 March 1671, source_evidence **RI-000126**) fixes his wife's name, and
the Plymouth Colony court's Taunton return plus the Taunton town's own vital records
(source_evidence **RI-000127**, two new sources) give the primary record of Ruth's remarriage to
John Bundy on 9 January 1676 — correcting Pope's misreading of the bride as "Jane." Finding
**RI-000128** (high) states the household and John Jr.'s death in the 14 July 1675 Mendon
massacre. A once-live ambiguity is resolved by analysis **RI-000129** (high): the 1675 casualty
is John Jr., not the identically-named eldest son of his brother Richard (G12), who was still
declining to administer Richard's estate in 1691 — the G12 companion's own primary record, cited
cross-unit. The post-1667 Mendon proprietors' records separately preserve two Gurney lot-holders
of the same generation — John Gurny, matching the resident John Jr. (source_evidence
**RI-000130**, his lot sold to Josiah Thayer in 1692), and Grisel Gurny, John Sr.'s widow in her
own right (source_evidence **RI-000131**, her will devising the lot to her son Joseph Juell,
confirming she had become John Burge's wife) — synthesized as finding **RI-000132**
(moderate-high), which CONTEXTUALIZES the wives-marriages Grizzell finding RI-000062 and the
frontier-rights 1662 allotment RI-000026 (both cross-unit). Peter's King Philip's War service is
carried in the same unit: source_evidence **RI-000133** (Bodge's muster/casualty-list entries)
SUPPORTS finding **RI-000134** (high) — he survived the Great Swamp Fight and was killed later in
the war, 1676. Open_question **RI-000135** carries two unresolved leads without advocacy: the
1699/1701 Nevis will's "Mary Gurney the daughter of John Gurney" as a possible John-Jr.-line
granddaughter, and the 1706 Taunton marriage of an Elizabeth Gurney to Timothy Cooper as a
possible further descendant. **Two new sources registered** (`data/sources.json` v1.12.1→**1.13.0**
+ validation worksheets): `plymouth-colony-records-vol8-shurtleff-pulsifer-1857`,
`taunton-vital-records-to-1850-vol2-marriages-1928`; both baselined at hash-sources. Loaded across
database revisions 114–116 (sync-sources r114 → author-batch r115 → hash-sources r116); milestone
snapshot at revision 116 (`data/context-graphs/g13/exports/snapshots/g13-context-r000116.ndjson`);
validate **0/0**, all tiers aligned. `tools/lint_source_notes.py` PASS. Per-increment gates hold:
source-journey, topic-graph-source, and publication-mapping gaps all 0 for the touched topic; no
new friction; backlog decreased — five legacy-companion rows (Grizzell's Mendon-widow aside,
the Billerica/Mendon/Jenner-debt block, the Suffolk-probate creditor-network block, the Nevis-will
lead, the Torrey compendium cross-check note), both F2/F2-RESOLVED dump findings, and three
supplemental-surfaces rows (fact-sheet Highlights, fact-sheet Children, case-file s1 and s10) all
move to closed or partial-with-remaining-facet-explicit. `coverageStatus: increment-complete` in
`manifest.json`. Deliberately not poached, left backlog: the "Jane Gurnet" 1664 Dorchester-will
false-friend thread (dump F3/F3-VERBATIM, decoupled from this household during the same 2026-07-01
campaign — routes to a future Dorchester-Gurnell collaterals topic); the Peter-as-reverse-tracer
Norfolk marriage-search material adjacent to the Nevis-will legacy block (Mary's own English birth
family, not the Mendon household — routes to origin/Mary's-origin work); and the `Surney`/`Garney`
colonial-spelling-variant addition to `data/search-variants.json` (dump recommendation, tooling
task, not a graph item).

Phase G3 increment (2026-07-10, bounded): `topics/family/13-colonial-collaterals.md`
(topicId `g13-family-colonial-collaterals` — the fourth **family** topic), co-authored with
research items `G13-RI-000136..000144` and four prose evidence markers
`G13-PM-000093..000096`. **One unit, depth over breadth: colonial-era same-surname
Gurneys with no documented tie to John's family.** The Providence, Rhode Island John
and Sarah Gurney (1695–1714) are a genuine but unconnected pair: source_evidence
**RI-000136** (the 1695–96 warning-out of a stranger named John Gurney) and
**RI-000137** (Sarah Gurney's 1714 will and inventory, her Gurney husband still
living) SUPPORT finding **RI-000138** (high) — no record ties either spouse to
John Gurney-1's children or grandchildren, and every one of Sarah's children carried
her prior husband's surname, Field. Analysis **RI-000139** (low) weighs Torrey's
independent "John3 ... Sarah (Thornton)[Fields] ... Providence" entry against a second
John3 (Elizabeth Green, 1689 Weymouth) and the already-identified Samuel3 (Mendon-born
son of John Jr. and Ruth, cross-unit CONTEXTUALIZES **RI-000128**): a plausible but
unconfirmed grandson reading, not a finding. A single unread Suffolk Deeds Liber I
index line, "Gurner, James, 5" (source_evidence **RI-000140**), stays exactly what it
is — open_question **RI-000141**, pending a read of printed page 5. And the dump's
long-carried "Jane Gurnet"/"Goodman Gurney of Dorchester" thread (F3/F3-VERBATIM/
F10/Input-5/F-R3, backlog since the 2026-07-01 campaign) is finally closed: source_
evidence **RI-000142** (Margery Laver's 1664 will) and **RI-000143** (the Dorchester
town-book, First Church, and 1676/7 Suffolk County Court "Goodman Gurney" stream,
three sources) SUPPORT negative_result **RI-000144** (high) — every Dorchester
"Gurney"-form record belongs to the unrelated Gurnell family, confirmed independently
across four printed sources. **Five new sources registered** (`data/sources.json`
v1.13.0→**1.14.0** + validation worksheets): `suffolk-deeds-liber-i-1880`,
`nehgr-13-abstracts-of-early-wills-1859`, `boston-record-commissioners-fourth-report-1880`,
`records-first-church-dorchester-1891`, `suffolk-county-court-records-1671-1680-csm-29-30`;
all baselined at hash-sources. Loaded across database revisions 117–119 (sync-sources
r117 → author-batch r118 → hash-sources r119); milestone snapshot at revision 119
(`data/context-graphs/g13/exports/snapshots/g13-context-r000119.ndjson`); validate
**0/0**, all tiers aligned. `tools/lint_source_notes.py` PASS. Per-increment gates hold:
source-journey, topic-graph-source, and publication-mapping gaps all 0 for the touched
topic; no new friction; backlog decreased — six dump-findings rows (F3, F3-VERBATIM, F4,
F10, the round-2 Input-5, and the round-2/round-3 F-R3) move to synthesized or partial-
with-remaining-facet-explicit. `coverageStatus: increment-complete` in `manifest.json`.
Deliberately not poached, left backlog: the cross-cutting "false-friends registry"
artifact itself (F-R3's other routing target does not exist as a repo artifact yet;
its content is fully discoverable via this topic and its sourceIds in the interim); the
Dedham "Goodman Gurney of Dorchester, a Tanner" fourth witness (F-R3.5, routed to the
same not-yet-built false-friends registry, not to this topic); and Isaac Gurney, already
treated as a probable son of John's own household in `g13-family-family-group` rather
than as a collateral.

Phase G3 increment (2026-07-09, bounded): `topics/identity/32-norfolk-parentage.md`
(topicId `g13-identity-candidate-b` — the sixth **identity** topic; manifest `order` 30;
heading_id `identity-candidate-b-norfolk-parentage`), co-authored with research items
`G13-RI-000145..000170` and eight prose evidence markers `G13-PM-000097..000104`.
**One unit, depth over breadth: the surviving candidate's own parentage case**, which
`30-candidate-overview.md` deliberately left external. The headline is
`identity_hypothesis` **RI-000145** (moderate): John Gurney of Braintree was probably the
son of Francis Gurney, Merchant Taylor of West Barsham, Norwich and London, by his first
wife Margaret Rybett. Its two primary records are the 23 September 1611 St Martin at
Palace marriage (source_evidence **RI-000151** → finding **RI-000152**, the first marriage
neither Daniel Gurney nor Bernau ever found) and the East Dereham Entry E baptism
(source_evidence **RI-000156**, re-read from the indexed "Nicholas Gorne" as "John the
sonne of ffrancis Gurnie" → finding **RI-000157**), with open_question **RI-000158**
holding the reading to a professional examination at the NRO and analysis **RI-000159**
carrying the baptism-before-marriage tension. Francis himself is fixed by **RI-000146**
(sixth son of Henry Gurnay of Great Ellingham and West Barsham), **RI-000147** (Merchant
Taylors' binding 1599, freedom 1606), **RI-000148** (the Lestrange agency), **RI-000149**
(the failed King's Lynn worsted venture), and **RI-000150** (the 11 July 1634 forced sale
of every acre — the emigration motive). The bride's family is **RI-000153**, and finding
**RI-000154** (moderate) puts her Rivett kin at Garveston and Gressenhall, two to three
miles from East Dereham, supplying both the maternal-kin upbringing after 1616/17 and the
name of John's son Richard. The sharpest objection is source_evidence **RI-000160** (the
1633 Heralds' Visitation naming Roger "eldest sonne," CONTRADICTS RI-000145), rebutted —
not dismissed — by finding **RI-000161** (the compilers' own child lists are fragmentary
and neither knew of the 1611 marriage) and supported by negative_result **RI-000162** (no
John among the seven St Benet Fink children of Francis and Anne Browning, 1619–1637: if a
son John exists, he belongs to the first marriage). Source_evidence **RI-000163**/**000164**
and finding **RI-000165** keep the claim attached to the right one of three same-named
Francis Gurneys. New this increment: **RI-000166**/**000167** (Muskett vol. 2 — Elizabeth
(Gournay) Crowe of East Bilney, five miles from East Dereham, and Frances Hovell as Edward
Gournay's widow, "Cozen Gurney" in Mary Goodwin's 1647 will) supporting finding
**RI-000168** (the senior West Barsham branch in the East Dereham orbit, its 1641
inquisition taken *at* East Dereham), with open_question **RI-000169** on the unimaged
Bozoune Crowe will (PROB 11/289/177, catalogued as "Bozann Crome"). Analysis **RI-000170**
(WEIGHS RI-000145) sets the four supports against the four offsets. **One new source
registered** (`data/sources.json` v-bump + validation worksheet):
`muskett-suffolk-manorial-families-v2-1900`. Two registry repairs, disclosed: `nro-pd-86-41`
had a `mediaPath` pointing at a nonexistent folder — repointed to its real validation
worksheet so the cited artifact resolves and hash-baselines; and two committed
citation-map rows carried an unquoted comma in `notes`, silently splitting the field —
requoted. Loaded across database revisions 120–124 (sync-sources → author-batch r123 →
hash-sources r124); milestone snapshot at revision 124
(`data/context-graphs/g13/exports/snapshots/g13-context-r000124.ndjson`); validate **0/0**,
all tiers aligned; `tools/lint_source_notes.py` PASS. Per-increment gates hold:
source-journey, topic-graph-source, publication-mapping, and input-source-set gaps all 0
for the touched topic; no new friction; backlog 103 → 92. `coverageStatus:
increment-complete` in `manifest.json`. RI-000145 and RI-000170 publication-map to the
fact sheet and case file §2/§10. **Retained friction (`confidence_mismatch`):** the fact
sheet publishes "roughly a sixty percent probability" while case file §11 now carries ~65%;
the unit states the lag plainly and leaves the publication decision open, since Plan 2b
authorizes no edit to either surface. Three prose citations are carried `cross_unit` with
no in-unit item link (`american-biography-cyclopedia-v26-gurney-1926`,
`mhs-winthrop-papers-gurdon-to-winthrop-1627`,
`tna-ward-c142-west-barsham-gurney-inquisitions`). Assimilated: legacy blocks l.219
(maternal Rivett kin) and l.379 (St Benet Fink, no John); case-file s2, s4, s5, s9; both
fact-sheet parentage rows; dump findings F-R3.8, F-R3.10, F-R4.4. Deliberately left
backlog, annotated not false-closed: legacy l.330 (only the Fischer corridor prior is
carried; the Hotten, Gilman/Diligent, Yarmouth, Shed-Finchingfield, and ROLLCO facets are
not), legacy l.262 (the arms facet is a prose-only cross-unit carry), and dump F9 / F-R3.2
/ F-R3.6 / F-R5, whose Candidate-B bearing — whether John emigrated *through* the
Winthrop/Gurdon patronage network — is an assessment question for `37-identity-assessment`,
not a parentage question. **Naming collision to resolve before E8:** `30-candidate-overview.md`
holds the unit_id `g13-identity-assessment`, which is the natural id for the eventual
synthesis unit; one of the two needs renaming. *(Resolved 2026-07-10 — see the next entry.)*

Phase G3 increment (2026-07-10, bounded): `topics/identity/37-identity-assessment.md`
(topicId `g13-identity-assessment` — the seventh and last **identity** topic; manifest
`order` 70; heading_id `identity-assessment`), co-authored with research items
`G13-RI-000171..000178` and six prose evidence markers `G13-PM-000105..000110`.
**One unit, depth over breadth: what the identity work adds up to.** Finding-first: John's
parentage is settled by elimination and circumstantial fit, not by a document — no record
made in his lifetime names his father. Analysis **RI-000177** (moderate-high) states why the
elimination is nonetheless stronger than most colonial origin attributions (every rival was
actively disproved, and the colonial record shows exactly one adult Gurney household in
Massachusetts before 1660) and why its weakness mirrors its strength (Candidate B predicts a
man who would leave almost no English paper, so missing confirmation is what the hypothesis
expects); it SYNTHESIZES RI-000106, RI-000145, and RI-000172, DEPENDS_ON the Dorchester-Gurnell
negative RI-000144 and the Providence finding RI-000138, and publication-maps to the fact sheet
and case-file §11.

**Candidate C (Berkhamsted) is eliminated here** — the last principal alternative and, per Plan 02
§4, the one with no unit of its own: source_evidence **RI-000171** (the eight indexed Berkhamsted
baptisms 1610–1636, and no John Gurney burial there 1640–1700) supports finding **RI-000172**
(high; wrong generation, three children with no colonial counterpart, no Mary or Peter, and three
shared names that miss by six to nine years), publication-mapped to case-file §8 and §11. That
absorbs `research/topics/john-gurney-candidate-berkhamsted-hertfordshire.md` whole.
Source_evidence **RI-000173** (eleven Gurney/Gurny households in the 1662–1666 London hearth-tax
returns) supports analysis **RI-000174** (moderate) — the unknown-corridor residual that the
eliminations do *not* clear, and the reason the estimate sits in the sixties rather than the
nineties. Open_question **RI-000175** carries the patronage question the wardship increment
deferred: whether John emigrated *through* the Gurdon–Winthrop Court of Wards network, with the
Norwich institution-book search named as the test that would close the chain. Analysis
**RI-000176** (moderate-high) reads Anderson's "Boston" settlement attribution as the same
conflation with the 1636 Newgate apprentice that produced the American 1615-birth tradition, and
records the user's transient-lodging scenario as possible but invisible in principle. Analysis
**RI-000178** (moderate) names the two realistic end-states (~85–90% on a Rivett-orbit marriage or
a 1650s Norfolk kin-mention; a ~65–70% plateau otherwise), the three levers, and the published
lag: the fact sheet still says "roughly a sixty percent probability" against the case file's ~65%.

**Naming collision resolved (13 audited editor ops, database revisions 125–141, no raw SQL).**
The overview unit at `30-candidate-overview.md` had been created under the unit_id
`g13-identity-assessment`. The id now names this synthesis unit, and the overview carries its own
id `g13-identity-candidate-overview`. Because a unique index forbids two units sharing a
`(path, heading_id)`, and validation forbids both a cross-unit marker member without a reviewed
reason and an active marker whose token count is not exactly one, the swap ran as: set a
transitional `cross_unit_reason` on the three marker members → retire `G13-PM-000073..000075` →
repoint `g13-identity-assessment` at the new file → create `g13-identity-candidate-overview` at the
old file → move `G13-RI-000104..000106` → move and reactivate the three markers → clear the
transitional reasons. The overview's own prose, manifest entry, ledger rows, and stale
cross-references (which still described Candidates C, D, and B as unauthored) were reconciled in
the same pass.

**No new sources registered** — all eleven cited ids were already in `data/sources.json`; two were
newly baselined at hash-sources (`findmypast-hertfordshire-baptisms`,
`findmypast-hertfordshire-burials`). Loaded across database revisions 125–143 (17 editor ops
r125–141 → author-batch r142 → hash-sources r143); milestone snapshot at revision 143
(`data/context-graphs/g13/exports/snapshots/g13-context-r000143.ndjson`); validate **0/0**, all
tiers aligned; `tools/lint_source_notes.py` PASS. Per-increment gates hold: input-source-set,
source-journey, topic-graph-source, and publication-mapping gaps all 0; no new friction; backlog
**92 → 85**. `coverageStatus: increment-complete` in `manifest.json` for both touched topics.
Assimilated: dump findings Input-2, §9.1, §9.4, F9, and F-R5; the Berkhamsted whole-file and the
London William Gurney hearth-tax supplemental rows; case-file s8 (the §8.2 facet) and s11; the
legacy "Working Hypotheses" block's assessment bearing. Five prose citations are carried
`cross_unit` with no in-unit item link (`findmypast-john-gurney-2026may-supplementary-same-name-sweep`,
`tna-pcc-gurney-elimination-corpus`, `blomefield-norfolk`, `nro-pd-86-41`, `ftdna-gurney-ydna`).
**Retained friction (`confidence_mismatch`, unchanged):** the fact sheet's sixty percent against the
case file's ~65% — now stated plainly in RI-000178 rather than only recorded in a ledger; Plan 2b
authorizes no edit to either published surface. Deliberately not poached, left backlog and
annotated: dump F-R4.2 (the Boston First Church zero, which would close Anderson's "Boston" on the
record rather than by inference — its home is `g13-colonial-record-coverage`, and it needs
`csm-39-boston-first-church` registered first); dump F-R3.2 and F-R3.6 (the Martha Heigham will and
the West Barsham advowson, both wardship-revision material); and the residual case-file s6/s10
identity facets.

**Two ledger regressions from the 2026-07-09 truncation repair were found and fixed** by diffing
Allen's pre-truncation copies against the restored files: `source-and-citation-map.csv` had lost the
`mentions` token from the Taunton vital-records row's `cited_role` (the graph carries both a
`supports` link on RI-000127 and a `mentions` link on RI-000135), and
`supplemental-surfaces-map.csv` had lost the case-file s10 annotation recording that the Nevis-will
facet is authored as RI-000135. No rows were lost in the original repair, and one apparent
discrepancy — the Pope row's `findings_contradicted` — was the repair *correcting* the pre-truncation
file, which had filed a contradicting witness under `findings_supported`.

## Case-file-as-source repair (2026-07-10, Opus; graph rev 144→160, snapshot r160)

Allen flagged that staged topic footnotes were citing `research/case-files/john-gurney-case-file-v4.md`
as the **source of truth** for evidence and findings. The case file is a publication surface, not a
source: all evidence must cite third-party records. Cross-references to it, for reader convenience,
are fine and are retained — now explicitly labelled.

**Topic files repaired (10).** Seventeen footnotes across `identity/30`, `31`, `32`, `34`, `35`, `36`,
`37`, `origin/24`, `origin/25`, and `research-state/41`. Every evidence footnote now leads with the
underlying third-party record(s) and a `Source ID`; every remaining case-file footnote opens with
"Cross-reference, not a source." Body prose that made the case file the grammatical actor of a
finding ("the case file eliminates a household…") was rewritten to state the finding directly.

**§8.6 collective-set exception (per Allen).** The dense clearance list of eliminated Johns is *not*
replicated household by household. `30-candidate-overview`, `31-candidate-a-aylesbury`, and
`36-other-eliminations` each carry the sweep as one collective finding, cite the record sweeps that
produced it, and name the case file's §8.3/§8.6 tables as the **master list** in a footnote explicitly
marked as a cross-reference.

**Graph (5 statements, 8 new source links).** `RI-000104`, `RI-000105`, `RI-000106`, `RI-000120`, and
`RI-000174` no longer name the case file as the authority for their own content. `RI-000106` and
`RI-000174` now link `findmypast-john-gurney-2026may-supplementary-same-name-sweep` and
`tna-pcc-gurney-elimination-corpus` directly; `RI-000120` links the sweep; `RI-000172` (Candidate C)
now carries its two Hertfordshire index witnesses directly rather than only through the relation
chain to `RI-000171`; `RI-000110` links the newly-registered certificate of residence.

**One source registered.** `tna-e115-180-113-certificate-of-residence-1641` (sources.json 1.12.1→1.15.0,
`corpusStatus: deferred`, not examined at image level), so Candidate A's 1641 move cites the archival
record rather than the case file. Registry fix in passing: the dangling `mediaPath` on
`findmypast-john-gurney-2026may-supplementary-same-name-sweep` pointed at an archived intake directory
and raised a `source_content_missing` warning the moment the graph cited it; nulled, so `canonical_path`
falls to the validation worksheet.

**Two open sourcing gaps, recorded not dropped.** (1) The 1650 Walgrave, Northamptonshire tenancy has
no located archival reference and no registered source; it is flagged in `31-candidate-a-aylesbury.md`
and nothing depends on it. (2) The certificate of residence itself is an unverified reference awaiting
a Discovery-catalogue confirmation.

**Content gap analysis.** The case-file citations were *not* hiding unassimilated content, with two
exceptions, both already scheduled: case file **§6** (children-search matrix, Peter naming gap, absence
of a son named Francis) and **§7** (Ann Gurney × John Gilman at Hingham) have no staged home. They are
Phase 2 items 5 and 6 in `tools/plans/G-13 Refactor/prompts/phase-1-and-2-prompts.md`.

Gates after the pass: validate **0/0**, tiers aligned, `input_source_set_gaps`, `source_journey_gaps`,
`topic_graph_source_gaps`, `publication_mapping_gaps`, `friction_needs_decision` all **0**; backlog
unchanged at 85.

## Wardship-network revision + Bury Chaplin fold-in (2026-07-10, Opus; graph rev 170→175, snapshot r175)

A bounded **revision** of `g13-origin-wardship-network` (four Norfolk senior-branch / Court-of-Wards
backlog rows) plus one conditional fold-in to `g13-origin-bury-connections`. Four new items
**G13-RI-000185..000188**, one new marker **G13-PM-000113**, three `add_marker_item` editor ops.

**F-R3.6 — West Barsham advowson (→ RI-000185).** Blomefield's parish-advowson sweep: the Gurneys held
the West Barsham vicarage advowson (Henry G15 patron in 1603), and the printed vicars list gaps
1603–1743, so the 1627–28 Warford institution is invisible there; Harpley (Edmund Gurnay B.D. under
Yelverton 1620–1648) and Great Ellingham (1628 Earl-of-Sussex presentation) are excluded as the 1627
living. `source_evidence` **RI-000185** QUALIFIES the open Warford question **RI-000085** — the
patron-side lever on that open question. Extended `23-wardship-network.md` §2 (marker PM-000053, expressed). West Barsham
vicars-list/advowson extract added to `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`.
`blomefield-norfolk` already registered.

**F-R3.7 — Adam Winthrop's diary (→ RI-000186).** Winthrop Papers I:153, Adam Winthrop's 3 Oct 1605
record of the deaths of Sir Edward Lewkenor of Denham and his wife Susan (Heigham) — Martha (Lewkenor)
Gurney's parents. `source_evidence` **RI-000186** SUPPORTS the founders-network finding **RI-000083**
(indirect): the Winthrop family personally memorialised the widowed Mrs. Gurney's own parents a
generation before the 1627 letter. **One source registered:** `mhs-winthrop-papers-adam-winthrop-diary-1605`
(sources.json 1.17.0→1.18.0 + validation worksheet; a distinct document from the already-registered
1627 letter). Extended §3 (marker PM-000054, expressed).

**F-R3.9 — L'Estrange kin-sourcing (→ RI-000187).** Sir Nicholas L'Estrange, 1st Bt. (the jest-book
compiler behind Thoms's 1839 anecdotes), married Anne Lewkenor of Denham — niece of Martha (Lewkenor)
Gurney and first cousin of Edward Gournay — so the West Barsham Gurney anecdotes are kin-sourced family
testimony. `research_finding` **RI-000187** CONTEXTUALIZES the pedigree evidence **RI-000081**; it
explains "Frances Hood" = Frances Hovell and shows the erroneous "1614" death circulated inside the
family (the wills place it 1621×1623). New subsection "Kin-sourced tradition: the L'Estrange
connection" with new marker **PM-000113** (primary). Sources `muskett-suffolk-manorial-families-v2-1900`
and `thoms-anecdotes-traditions-1839` both already registered.

**F-R3.2 — Martha Heigham's will: no new item.** Re-reviewed and confirmed the wardship-network /
puritan-matrix bearing is already fully homed in **RI-000082** (Muskett vol.1 prints the will; the
Denham sisters, Emmanuel College scholarship, and Geneva Bible to Denham church are all carried in
prose and the item). Nothing genuinely unhomed for this unit; the Candidate-B identity bearing stays
backlog for the identity pass (row annotated, not false-closed).

**F-R3.11 folded into `g13-origin-bury-connections` (→ RI-000188).** Phase 1 registered
`muskett-suffolk-manorial-families-v3-1900`, so the conditional fold-in landed. Thomas Chaplin's 1672
Bury St Edmunds will left £40 "to Mary Gurney my servant" beside a debt from "Jeremy Houchin, late in
New England." `source_evidence` **RI-000188** CONTEXTUALIZES the attribution finding **RI-000097** — a
concrete Bury⇄Boston corridor instance illustrating what Banks mistook for a birthplace. It names no
John Gurney and connects to no natal household; added to §"What the attribution is worth" (marker
PM-000066, expressed).

**Line held (per RI-000084 / task).** Every item attaches to the senior West Barsham branch, not to
John; nothing here identifies the emigrant. RI-000185 QUALIFIES the open Warford question; RI-000186/187
deepen the senior branch's Denham-Lewkenor kinship and its tie to the founders; RI-000188 stays firmly
on the Suffolk-migration milieu.

Loaded across database revisions **170–175** (sync-sources r170 for the new registration → author-batch
r171 → three `add_marker_item` editor ops r172–174 → hash-sources r175 baselining the two newly-cited
printed sources); milestone snapshot at revision 175
(`data/context-graphs/g13/exports/snapshots/g13-context-r000175.ndjson`). Both units keep
`coverageStatus: increment-complete`. Gates after the pass: validate **0/0**, tiers aligned, lint PASS;
`input_source_set_gaps`, `source_journey_gaps`, `topic_graph_source_gaps`, `publication_mapping_gaps`,
`friction_needs_decision` all **0**; dump-findings backlog **47→43** (the four assimilated rows), global
un-dispositioned backlog **72** (whole-refactor, expected). Remaining wardship/bury backlog: **F-R3.2**
(Candidate-B identity bearing of the Martha Heigham will).

## Case-file §6 fold-in: naming pattern + children-search matrix (2026-07-11, Opus; graph rev 177→180, snapshot r180)

A bounded **revision** across two already-committed units — `g13-identity-candidate-b`
(`topics/identity/32-norfolk-parentage.md`) and `g13-identity-assessment`
(`topics/identity/37-identity-assessment.md`) — homing the last substantive identity section with
no staged home, case file **§6**. Three new items **G13-RI-000192..000194** (two author-batches) and
two new markers **G13-PM-000115/000116**; one editor `add_relation` op. The ~65% probability model
stays external-canonical to the case file (cross-referenced, never restated as a graph fact); every
new item cites its own third-party record, not the case file.

**§6.2 Peter naming gap → `g13-identity-candidate-b` (analysis RI-000192).** Of twelve indexed
Peter-Gurney baptisms across Britain 1632–1642 (`findmypast-uk-parish-baptisms`), none was fathered
by a John Gurney; Peter is not absolutely absent from Norfolk Gurney households (the 1641 Smallburgh
Peter-son-of-Peter qualifier is carried), but the name enters John's branch most plausibly through
his wife Mary's kin — neither for nor against the parentage. CONTEXTUALIZES the standing first-wife
open question **RI-000055**.

**§6.3 Absence of a son named Francis → `g13-identity-candidate-b` (analysis RI-000193).** The
strongest naming-pattern argument against Candidate B, read off John's own roster (Sarah, Mary,
Richard, John Jr., Peter; `sprague-braintree`, `history-of-weymouth`). Authored as a first-class
negative that **QUALIFIES the parentage hypothesis RI-000145**, with the summary weighing
**RI-000170 now DEPENDS_ON it** (editor op, rev 180). The case file's four candidate explanations
(estrangement, name-ruin, maternal priority, dead earlier child) are carried explicitly as
undocumented hypotheses, not evidence. New prose section "The naming pattern: Peter and the missing
Francis" (marker **PM-000115**, primary RI-000193, expressed RI-000192).

**§6.1 Children-search matrix → `g13-identity-assessment` (negative_result RI-000194).** No indexed
English parish cluster matches the colonial John's full family signature (Sarah, Mary, Richard, John
Jr., Peter) 1620–1640 across 20+ Gurney baptisms in FamilySearch, Findmypast, and Ancestry
(`findmypast-uk-parish-baptisms`, `fs-england-births-christenings`, `ancestry-norfolk-1535-1812`),
with a structured `negative_result_scope` — a coverage gap, **not** a finding that the children were
born in Massachusetts; the wildcard marriage negative RI-000064 is cross-referenced, not re-authored.
SUPPORTS the record-shape analysis **RI-000177**. New section "The emigrant's own family leaves no
English trace" (marker **PM-000116**). The unit's offsets footnote (`[^bottom-line]`) was updated:
the "absence of a son named Francis" offset now points to the first-class item RI-000193, not only to
the roster item RI-000065.

**§10 residual-facet sweep (annotated on the s10 supplemental row, none newly authored).** Reviewed
against RI-000145..000170: the trade/corridor/motive/network narrative recap is already carried
(RI-000170 weighing + RI-000147/000150/000154/000168 threads + fischer via RI-000170 + migration
RI-000091); the John-of-Maldon second-son datum is carried on RI-000161 (the Maldon-specific
hearth-tax/administration/bachelor biography stays external G14 context); the Coleman Street adjacency
stays backlog, its corridor/network bearing already carried at finding level and its witnesses
(`protestation-returns`, `gibson-dell-protestation`) not identity-decisive — fuller home
`g13-origin-wardship-network` / the G14 companion.

**No new sources or entities registered** — all six cited ids were already registered and baselined
(hash-sources a no-op). Loaded across database revisions **178–180** (candidate-b author-batch r178 →
assessment author-batch r179 → editor `add_relation` RI-000170 DEPENDS_ON RI-000193 r180); milestone
snapshot at revision 180 (`data/context-graphs/g13/exports/snapshots/g13-context-r000180.ndjson`);
validate **0/0**, all tiers aligned. Both units keep `coverageStatus: increment-complete`. Ledgers:
5 new `source-and-citation-map.csv` rows + the `fs-england-births-christenings` assessment row updated
to reflect its second in-unit role (RI-000194); the case-file **s6** supplemental row moved to
`assimilated` (all three sub-parts homed), the **s10** identity row annotated with the facet sweep.
Per-increment gates hold: `input_source_set_gaps`, `source_journey_gaps`, `topic_graph_source_gaps`,
`publication_mapping_gaps`, `friction_needs_decision` all **0**; whole-refactor un-dispositioned
backlog **71→70** (the s6 row closed).

---

Root hub authored + hub-legacy-rows dispositioned (2026-07-12, Opus). Authored the root-hub
companion `hub.md` and wired it into `manifest.json` as `website.rootHubFile` (distinct from the
website-landing `introFile`; consumed at cutover step 4, not by the website build). **Design
decision (Allen, 2026-07-12): extra-light, not the Plan 02 §6 heavy hub.** With the 25-topic
library, the case file, and the website research-library landing page all carrying the substance,
a 2,500–4,000 word root synthesis is a redundant, higher-maintenance duplicate; the root companion
is instead an entry-point stub (~450 words incl. footnotes, ~270 of prose) — a condensed, footnoted identity/lineage banner, an
orientation block linking the research library / fact sheet / case file / direct-line father (G14)
and son (G12) companions, and an identity-status statement that references the case file's
probability model as external-canonical (the ~65% figure lives in the case file §11, not restated
as a project fact). It is written to read correctly after the cutover fact-sheet ~65% edit (no
"fact sheet lags" language). No known-facts table, per-domain synthesis, conflicts/open-questions
lists, topic index, or crosslink map are reproduced — those are owned by the topic units and
generated by the website. No graph items (the hub synthesizes nothing; the units own the research);
no new sources or entities.

**Plan updated to match** (per Allen): Plan 02 §6 revised with an extra-light band (~300–800 words)
and the superseded heavy design retained for the record; the cutover gate in `prompts/cutover.md`
updated to the new target.

**Card-length tidy (Allen's request):** of the ~26 website hub cards, the five longest topic
`summary` fields (113–128 words — Bury connections, Candidate B, wardship network, trade & training,
identity assessment) were shortened to ~74–90 words, bringing them into line with the pack (median
62; former outliers gone, new max 90). Content preserved, only condensed; the identity-assessment
card also dropped the now-stale "fact sheet lags at sixty percent" clause.

**Hub-destined legacy rows dispositioned** in `coverage/legacy-companion-map.csv` (§7.1 vocabulary):
the intro/lineage banner (l.1, `retained_in_hub` — condensed into the hub banner) and Crosslinks
(l.544, `retained_in_hub` — top-level + direct-line links kept, granular map not reproduced;
`source_ids` set to the four backtick catalogue ids the block names, §8.2 anchored-clean); the
Known Facts table (l.11, `synthesized` — each fact already assimilated with its citation into the
topic units) and the two structural containers "Life and records in New England" (l.30) and "Origin
question and candidate analysis" (l.217, both `synthesized` — dissolved, children owned by the topic
units, headings now the website group index). Checker (`g13_coverage_check.py`): legacy backlog
**18→13**; `input_source_set_gaps=0`, `source_journey_gaps=0`, `publication_mapping_gaps=0`. The
whole-refactor `RESULT: FAIL` and residual backlog are the expected pre-cutover state (non-hub
legacy rows, supplemental surfaces, and dump HOB rows remain for later passes; the single §8.4
parity gap is pre-existing, not introduced here).
