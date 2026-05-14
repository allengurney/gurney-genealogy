# John Gurney Candidate D AI-ready working packet v15

```yaml
created: 2026-05-14
supersedes: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v14.md
source_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
review_note: sources/intake/john-gurney-2026May/john-gurney-candidate-d-ai-consumption-review-v15.md
research_prompt: sources/intake/john-gurney-2026May/john-gurney-candidate-d-claude-code-research-prompt-v15.md
purpose: Focus a later analysis/research pass on Candidate D reasoning and online record pursuit, with repo logistics separated into Phase 1 patchsets.
phase_1_patchsets_to_apply_first:
  - sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md
  - sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md
```

## How to use this packet

Read this packet first for the source map, triage framing, priority research plan, and unresolved issues. Use the original v13 packet for full transcriptions and detailed section text. The user intends to apply v32 and v33 before the deeper research pass, so the next researcher should assume source handles are in place once that application is complete and should not spend the main research turn re-solving repo logistics.

The central research question is whether Candidate D can be supported or eliminated as John Gurney of Braintree:

```text
Candidate D:
John Gurney, adult son and executor of Robert Gurney,
Robert being citizen and draper of London / tailor of Old Change,
with John made free of the Drapers' Company by redemption on 11 Feb. 1623/4.
```

Keep the analysis objective. Do not start with a probability matrix or a forced pro/con scoring table. Build findings from source results, preserve tension, and separate direct Candidate D evidence from broad same-name/comparator density.

## Repo source map

The source IDs below are proposed by v32/v33 and should be treated as intended repo handles unless Phase 2 discovers an existing duplicate.

| Packet section | Evidence block | Intended source ID |
|---:|---|---|
| 1-5 | Boyd's Inhabitants selected Gurney/Garney/Gourney cards | `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards` |
| 6-7 | ROLLCO Drapers' Company Robert/John Gurney cluster | `rollco-drapers-gurney-old-change-cluster` |
| 8-9 | Robert Gurney will and religious wording | `acl-robert-gurney-will-1625` |
| 10 | Old Change / St Augustine / London Archives / context pages | `candidate-d-london-context-web-bundle` |
| 13 | Harleian Society St Vedast / St Michael le Quern registers | `harleian-st-vedast-st-michael-le-quern-registers` |
| 14-17 | St Augustine Watling Street original-register image reviews | `lma-st-augustine-watling-register-candidate-d-images` |
| 18, 19.2 | St Magnus the Martyr marriage and John Grone burial images | `lma-st-magnus-martyr-register-candidate-d-images` |
| 20 | St Swithin, London Stone John Grine marriage image | `lma-st-swithin-london-stone-register-john-grine-1640` |
| 21 | St Giles Cripplegate John Grone baptism lead | `lma-st-giles-cripplegate-register-john-grone-1630` |
| 22.1 | St Mary Magdalen Old Fish Street John Grene image | `lma-st-mary-magdalen-old-fish-street-john-grene-1634` |
| 19.1, 22.2, 23 | Index-only Grine/Grene comparator leads | `candidate-d-london-grine-grene-index-leads-bundle` |

Existing repo source to elevate:

| Source ID | Use |
|---|---|
| `bho-london-inhabitants-st-augustine-1638` | Top discriminator. Lists John Gurney in the St Augustine parish/rents return in 1638, in the rents section at 10 pounds. Because Candidate D's Robert/John cluster is specifically St Augustine / Old Change, this is no longer just a generic same-name London lead. It needs targeted correlation. |

## Core established facts from v13

Robert Gurney is strongly established as a London textile/trade figure in the Old Change / St Augustine orbit:

- Boyd's card places Robert Gurny/Gurney at St Augustine with wife Anne Morris and child John.
- ROLLCO places Robert Gurney, tailor, Old Change, as a Drapers' Company apprenticeship master in 1617.
- Robert's will identifies him as citizen and draper of London.
- Robert's will places his dwelling/business premises in Old Change.
- Robert's will names wife Anne and son John.

Candidate D John is strongly established as Robert's adult son by 1623/4-1625:

- ROLLCO identifies John Gurney as Drapers' Company new freeman by redemption on 11 February 1623/4, father Robert Gurney.
- Robert's 1625 will names son John and makes him sole executor.
- The probate clause was proved by John Gurney as son and executor on 23 September 1625.
- The 1630 ROLLCO John Gurney apprenticeship-master event is probably the same John because the name/company/timing fit the 1623/4 freeman sequence, but full event detail should still be pulled to confirm roles and related persons.

St Augustine child chronology now matters:

- A first John, son of Robert Gurny, was baptized at St Augustine 18 February 1595/6 and buried 4 February 1599/1600.
- Marye/Mary, daughter of Robert, was baptized 12 March 1597/8 and buried 25 January 1600/1.
- An unnamed stillborn son of Robert was buried 8 April 1601.
- No replacement John baptism was found in the supplied St Augustine christening images through 1610. This is not a conflict with the broader search; the user searched inclusively beyond the target range to avoid missing adjacent evidence.
- No first-wife burial was found in the supplied St Augustine burial images from 1601 through 1612.

Anne Morris should not be assumed to be Candidate D John's biological mother:

- Robert married Anne Morris at St Magnus the Martyr on 4 April 1611 by licence.
- Robert already had children in St Augustine before 1611.
- The will confirms Anne as wife/widow-beneficiary, not mother of John.

## Top discriminator: 1638 St Augustine John Gurney

The existing source `bho-london-inhabitants-st-augustine-1638` must be treated as one of the first research tasks. It sits directly at the intersection of Candidate D's strongest geography and the migration timeline.

Known current repo treatment:

- Source entry: `data/sources.json`, source ID `bho-london-inhabitants-st-augustine-1638`.
- Corpus note: `sources/corpus_supplement/bho-london-inhabitants-st-augustine-1638.md`.
- Validation note: `sources/validations/bho-london-inhabitants-st-augustine-1638.md`.
- Current research note: `research/people/g13-john-gurney-fact-sheet.research.md`, "London St Augustine same-name lead, 1638."
- Place note: `research/places/city-of-london.md`, "St Augustine John Gurney and Haberdashers' Gournay charity."

Why it matters:

- Robert Gurney's household/business is tied to St Augustine / Old Change by Boyd, ROLLCO, and the will.
- Candidate D John is son/executor in 1625.
- A John Gurney appears in St Augustine in 1638.
- The colonial John Gurney is expected in New England by about 1641, so 1638 is compatible only if followed by disappearance/emigration rather than continued London residence.

Research tasks:

1. Re-read the BHO page and capture the exact John Gurney row plus surrounding St Augustine rent context.
2. Determine whether the 10-pound rent entry looks like a substantial household, business premises, parish rent, or another category.
3. Search for St Augustine / Old Change rate, tithe, poor-rate, churchwarden, vestry, inhabitant, Protestation, subsidy, or assessment records between 1625 and 1641.
4. Treat the 1638 entry as a checkpoint in a sequence, not an isolated proof.
5. Ask whether this John appears before 1638, after 1638, or only in this one return.

Interpretive posture:

- If the 1638 John can be tied to Robert's son and then disappears before the colonial record horizon, it strengthens Candidate D.
- If the same John remains visible in St Augustine/London after 1641, it likely eliminates Candidate D.
- If the 1638 John belongs to a separate London John Gurney, it becomes comparator-density evidence rather than Candidate D evidence.

## Religion and migration-corridor framing

Religious motivation should be handled with nuance. The wording in Robert Gurney's will is not enough by itself to prove Puritan identity, nonconformity, or emigration intent. However, religion was a prevailing rationale for Massachusetts Bay migration, and professional emigrant-origin work often follows religious/parish corridors for exactly that reason.

Therefore:

- Do not overweight formulaic Protestant will language.
- Do not ignore religion just because the will language is not decisive.
- Search for stronger catalysts or corridor evidence: godly ministers, lecturers, parish networks, nonconforming associates, Coleman Street or other known migration-neighborhood links, church discipline, recusancy/nonconformity records, or named New England-connected associates.
- If no religious or migration-network catalyst appears, that absence should affect Candidate D's plausibility, especially when compared with Candidate B's stronger emigration-corridor framework.

Old Change should remain a trade/parish/search-geography clue unless stronger evidence links it to a religious-emigration network.

## Main reasoning tasks for next analysis

Prioritize questions that can support or eliminate Candidate D rather than expanding every nearby-name lead.

1. Determine whether Candidate D John remains visible in London after the likely migration window.
2. Determine whether Candidate D John had a wife Mary and children matching Sarah, Mary, Richard, John, and Peter.
3. Pull full ROLLCO details and test whether the 1630 apprenticeship-master result is the same John as the 1623/4 freeman.
4. Correlate `bho-london-inhabitants-st-augustine-1638` with Candidate D as the first external checkpoint.
5. Search for Robert's first marriage, possible first-wife burial, and Candidate D John's baptism only where they materially change the identity argument.
6. Look for religious/migration-network catalysts, but keep them separate from proof of parentage.

## Highest-value online research plan

### Tier 1: direct Candidate D discriminators

1. St Augustine / Old Change continuity, 1625-1641:
   - John Gurney marriage.
   - Children of John Gurney.
   - Anne Gurney burial/remarriage.
   - John Gurney burial.
   - Rate/tax/inhabitant continuity before and after the 1638 BHO checkpoint.
   - Protestation, subsidy, poor-rate, churchwarden, vestry, or assessment material if available.

2. BHO 1638 St Augustine source:
   - Capture exact row and nearby context.
   - Identify whether 10 pounds is a rent/value amount and how it compares with neighbors.
   - Decide whether this is likely Candidate D, a separate John, or indeterminate.

3. ROLLCO event exports/detail pages:
   - John Gurney freedom by redemption, 11 February 1623/4, father Robert Gurney.
   - Robert Gurney apprenticeship master, 1617, tailor, Old Change.
   - John Gurney apprenticeship master, 1630.
   - Robert Gurney freedom-event master, 1629.

4. London probate and administrations for John/Anne/Robert-linked Gurney variants after 1625:
   - John Gurney of St Augustine / Old Change.
   - Anne Gurney widow of Robert.
   - Dunnell/Henscott network probate if it clarifies kinship.

### Tier 2: family reconstruction and missing baptism

5. St Augustine marriages before 1595:
   - Robert Gurny/Gurney first marriage.

6. St Augustine burials before 1601:
   - Possible first wife of Robert.

7. Nearby parishes around Old Change / Cheapside / Watling Street:
   - All Hallows Bread Street.
   - St Mary Magdalen Old Fish Street.
   - St Mary le Bow.
   - St Faith under St Paul.
   - St Peter Cheap.
   - St Matthew Friday Street.
   - St Benet Sherehog and other immediate-neighborhood parishes if direct searches fail.

### Tier 3: controlled comparator and density work

These leads should not contaminate the source registry or Candidate D claim unless stronger evidence appears, but they can show how many John/Gurne/Grine/Grene-like records exist in overlapping communities.

8. Pull original image for Jhon Grine at St Mary-at-Hill, 6 March 1603/4, only if it becomes efficient.
9. Pull original image for John Grene son of Robart Grene at All Hallows Bread Street, 31 August 1600, if practical.
10. Search St Swithin after the 24 January 1640/1 John Grine / Mary marriage for children or burials that keep that couple in London.
11. Revisit St Giles Cripplegate John Grone 1630 only with a tighter crop or higher-resolution image.
12. Keep the St Magnus John Grone burial as a possible different-name/density record and as an exclusionary note for Candidate D if the reading remains John Grone buried 5 July 1625.

## Scratch-file protocol

Use scratch files only when they reduce context load or prevent duplicated searching. Do not create busy-work logs that merely restate the packet.

Recommended minimum:

- A lean lead tracker if more than about eight active searches are underway.
- A parking lot only for leads intentionally deferred.
- Interim findings only when a research round produces enough new evidence that chat context may become fragile.

Suggested lean lead-tracker columns:

```text
lead | direct/comparator/context | sourceId | searched where | result | Candidate D impact | next action
```

## Parking lot

These are worth preserving but should not dominate the first research round:

- Richard Gourney of St Vedast, father of Anne baptized 1626.
- Jane Gurney / Richard Cobham, St Vedast marriage 1658.
- Later St Vedast Elizabeth/Hannah Gurney material.
- Sir Richard Gurney / Elizabeth monument note.
- St Mary Whitechapel John Grene son of Rich Grene, 1610/11.
- St Mary Magdalen Old Fish Street John Grene son of Jeames, 1634, unless parish-wide searches surface stronger Gurney links.

## Current issues to remember

- The packet is source-rich but mixes confirmed records, analysis, locator context, and comparator leads. Keep those lanes separate.
- The St Augustine post-1601 replacement-John baptism is not found in supplied images; do not imply it is proven.
- The broad St Augustine search range was inclusive by design and should not be framed as an internal contradiction.
- The 1611 Anne Morris marriage is confirmed but does not prove Anne was Candidate D John's mother.
- The 1630 ROLLCO John Gurney apprenticeship-master event is likely the same John but should still be verified with full event detail.
- The Robert Gurney will image `31787_A002570-00422.jpg` has now been copied into the intake folder and should be moved by v32 Phase 2.
- Many section 13-23 images/PDFs are lower-probability or comparator material. They need not be moved into the repo unless they become necessary.
- The St Swithin John Grine / Mary lead is attractive because of wife Mary and date, but the surname does not strongly read as Gurney.
- The St Magnus John Grone burial on 5 July 1625 is probably not Candidate D because Candidate D John proved Robert's will on 23 September 1625, but it may still be useful for same-name/different-name density.
- Avoid a decision matrix at this stage. Let the research stay objective until the new evidence warrants structured weighing.
