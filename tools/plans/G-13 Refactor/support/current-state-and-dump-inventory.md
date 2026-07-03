# Current state and research-dump inventory

Inventory snapshot date: 2026-07-03.

This is a planning inventory, not an assimilation decision or an exhaustive
freeze. The live dump continued changing during planning; implementation must
refresh filenames, hashes, findings, and source artifacts before creating the
baseline coverage ledger.

## Current primary artifacts

| Artifact | Approximate size | Role |
|---|---:|---|
| `research/people/g13-john-gurney-fact-sheet.research.md` | 18,799 words | Canonical G13 working companion |
| `research/case-files/john-gurney-case-file-v4.md` | 21,233 words | Published identification argument |
| Seven G13/John topic files | 24,269 words total | Candidate and immigration/topic analysis |
| Generated G13 companion HTML | 176 KB | Current public research-note page |

At 50% growth, the companion alone would reach approximately 28,198 words.

Known structural symptoms:

- Opening probability and later working-hypothesis probability are not aligned.
- A workflow-style "PROMOTE" heading remains visible.
- Footnotes are distributed throughout and partly collected at the end.
- Some G13 material is appropriately external, but the reader must already know
  which candidate/topic/place file to consult.

## Dump Markdown

| File | Words | Lines | Main scope |
|---|---:|---:|---|
| `dump-2026-07-01-g13-colonial-massbay-campaign.md` | 6,531 | 566 | Round 1 colonial campaign, Braintree manuscript, Winthrop/Gurdon, negatives |
| `dump-2026-07-01-g13-colonial-round2-ward-county.md` | 4,884 | 466 | Wardship, county framing, colonial false friends; includes reconciled material formerly held in the temporary dump |
| `dump-2026-07-02-g13-colonial-round3-english-network.md` | 2,215 | 197 | English ward/network findings |
| `dump-2026-07-02-g13-colonial-round3-part2.md` | 2,953 | 264 | West Barsham, Crowe, L'Estrange, Bury conduit |
| `dump-2026-07-02-g13-colonial-round4-arch45-and-network.md` | 8,562 | 681 | 1646 petition, Boston negative, network synthesis |
| `dump-2026-07-03-round5-G-14-to-G-37.md` | 10,533 | 322 | Primarily G14–G37; route G13-bearing network material carefully |
| `hobart-journal-pages-8-24-transcription.md` | 3,114 | 1,173 | Source transcription and scoped variant review |

`temp999.md` was deliberately deleted after reconciliation. It is not part of
the implementation baseline and must not be recreated.

## Dump media

### Braintree manuscript

- Births page.
- 1661 deaths page.
- Marriage page 174.
- `Girny/Grizell` crop.
- Wife-death enlargement.

These support the reassessment of the Cheny/Gurney printed-record conflict.

### Massachusetts Archives petition

- Images surrounding image 1403.
- Crops of the `Gournet/Gourney` line and signatures.

These support the 1646 Braintree meadows petition and paleographic questions.

### Retained text/source captures

- Brackett genealogy.
- New England historical volume.
- Venn volumes.
- *Pioneers of Massachusetts*.
- Plymouth Colony records.
- Boston record report.
- Suffolk manorial volumes.
- Winthrop papers.
- BHO/HMC Kings Lynn text.
- Farrer *Honors and Knights' Fees* text.
- EEBO/Threnodia OCR.

These are raw source candidates. They do not become research prose merely
because they are in the dump.

## Major finding families

### Colonial

- Braintree manuscript reading materially favors `Girny/Gurney` over the
  printed `Cheny` form.
- 1646 Braintree meadows petition found and imaged.
- Full MBCR, Boston, Plymouth, deed, church, and other record-class sweeps
  produce useful bounded negatives.
- John never being admitted freeman is a social-status finding.
- John Jr./Ruth Bundy and descendant lines require correction/disambiguation.
- Gurnell/Gornell, Garnet/Gardner, Garnsey, and other false friends are
  documented.

### English origin and networks

- 1627 Gurdon-to-Winthrop letter places the West Barsham heir in Winthrop's
  wardship/patronage network.
- Ward/IPM material refines the West Barsham succession.
- Lewkenor/Heigham/Gurdon/Sedley/Knyvett relationships deepen the network.
- Bozoune Crowe and Elizabeth Gournay add an East Bilney/East Dereham orbit.
- Jenner and Brackett evidence may inform reception networks.
- Bury St Edmunds/Boston conduit evidence includes Mary Gurney and a New
  England debt.

### Negative and unresolved

- Anderson's "Boston" attribution is pressured by broad Boston record-class
  negatives and the Newgate-apprentice conflation explanation.
- Warford/Walford remains unresolved after university searches.
- Some gated wills, IPMs, source images, and CCEd routes remain.
- Some empty ledgers in round 3 must be reconstructed from finding prose.

### Analysis, theories, and hypotheses

- The dumps contain objective synthesis and evidentiary analysis that is not
  reducible to factual findings.
- They also contain explicit hypotheses, speculation, probability discussion,
  and assessments of what would materially change the identity case.
- These require individual dispositions and must not disappear during
  fact-focused extraction.
- Analysis and hypothesis remain distinct: analysis explains or weighs;
  hypothesis proposes a testable direction.

## Reconciliation warnings

1. Do not promote an early tentative finding when a later dump resolves it.
2. Do not flatten source-coverage negatives into historical negatives.
3. Do not route G14–G37 findings into G13 merely because the session began from
   G13.
4. Do not leave large OCR files in the research layer.
5. Do not discard false-positive work that prevents expensive repeated
   searches; assimilate it into a compact false-friend/negative-search layer.
6. Do not infer that an unregistered source is ready for citation.
7. Do not extract facts while discarding analysis, theories, speculation, or
   user reasoning.
8. Reconcile actionable open items against the leads catalog.

## Required inventory outputs during implementation

- File hashes.
- Section-level duplicate comparison.
- One dump-map row per finding/input/negative ledger.
- Source registration status.
- Media disposition.
- Destination and research-item IDs.
- Supersession relationships.
- Lead update/create/close action and lead IDs.
- Human-review status.
