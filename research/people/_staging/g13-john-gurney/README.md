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
