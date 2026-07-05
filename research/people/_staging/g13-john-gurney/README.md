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

Leads bearing on this increment — **L-182** (Weymouth grants → RI-000019), **L-185**
(Ludden Old-Planter reception → RI-000022), **L-190** (Jenner credit tie → RI-000020/021) —
were tagged in the production catalog via `research_leads.py --append-status-note` with a
`[G13-STAGING 2026-07-04: …]` note (append-only; `Source ref` left production; backup in
`_local/backups/`). Find them with `research_leads.py search G13-STAGING`; at cutover, review
each, finalize via `update`/`close`, and strip the tag.
