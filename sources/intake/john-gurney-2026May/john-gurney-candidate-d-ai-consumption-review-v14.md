# Candidate D working packet AI-consumption review v14

```yaml
created: 2026-05-14
reviewed_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
ai_ready_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v14.md
phase_1_patchsets:
  - sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md
  - sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md
```

## 1. AI-consumption assessment

The v13 packet is usable but too dense for a first-pass research agent if the agent also has to handle repo logistics, source creation, media movement, and citation normalization. Its strongest content is the detailed record-by-record extraction. Its weakest structure is that confirmed evidence, working inference, context-source strategy, and false-positive parking-lot material are interleaved.

The best optimization is not to shorten the evidence. It is to add a thin control layer above it:

1. A source map from each packet section to a stable repo `sourceId`.
2. A prioritized discriminator list.
3. A parking-lot section for broad comparator leads.
4. Clear non-goals for the next research pass.
5. A scratch-file protocol so the next agent does not keep all intermediate reasoning in chat context.

That control layer is now drafted in `john-gurney-candidate-d-working-packet-ai-ready-v14.md`.

## 2. Highest-value changes to make before deeper analysis

1. Apply or approve the source-foundation patchsets first.
   - v32 creates the source handles for Boyd, ROLLCO, the Robert will, and context sources.
   - v33 creates the source handles for the Harleian/LMA/register/comparator records.
   - This lets later analysis cite `sourceId`s instead of re-solving repo logistics.

2. Put `bho-london-inhabitants-st-augustine-1638` into the next prompt as a top discriminator.
   - This existing repo source lists John Gurney in St Augustine in 1638.
   - It could strengthen Candidate D, complicate the migration timeline, or identify a separate London John.

3. Split the next research into "direct Candidate D" and "false-positive/comparator" lanes.
   - Direct: Robert/John/Drapers/St Augustine/Old Change.
   - Comparator: Grine/Grene/Grone records not yet connected to Robert, Old Change, or Drapers.

4. Require the next agent to produce a lead tracker during the run.
   - Columns should include lead, sourceId, status, searched where, result, Candidate D impact, next action.

5. Make "post-1625 London continuity" the first elimination/support test.
   - If Candidate D remains active as a Drapers/St Augustine London resident after 1641, he is likely eliminated.
   - If he disappears from the London record while matching wife/children or migration signals emerge, he strengthens.

## 3. Suggested prompt revision

Use this in place of the draft prompt:

```text
Deep analysis of `sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v14.md`, using `sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md` only for full transcriptions/details when needed.

First confirm whether Phase 1 source patchsets `sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md` and `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md` have already been applied. Do not spend the main research turn on repo logistics unless missing source handles block citation.

Focus on support or elimination of Candidate D as John Gurney of Braintree. Highest-value discriminators: (1) post-1625 London continuity or disappearance, especially St Augustine/Old Change records; (2) wife Mary and children Sarah, Mary, Richard, John, Peter; (3) full ROLLCO event details for John/Robert; (4) the existing repo source `bho-london-inhabitants-st-augustine-1638`; (5) St Augustine registers/rates/taxes after Robert's 1625 probate.

Conduct online searches over 2-3 research rounds. Treat the packet's transcriptions as accurate working evidence unless a specific point requires re-validation. Keep false-positive Grine/Grene/Grone comparator leads separate from Candidate D unless a direct bridge appears.

Create scratch files under the intake working area as needed: lead tracker, parking lot, interim source/corpus notes, and interim findings. At the end, output a Phase 2 patchset with source records, facts, findings, and proposed research/case-file updates from both the packet and new research. Do not immediately update the case file during the research rounds.
```

## 4. Inconsistencies, gaps, and issues to address now

1. Section 16 says no replacement John baptism was found through 1610, but the Candidate D model still uses a likely c.1601-1604/5 birth window.
   - This is not fatal, but the next packet should state the tension plainly: the most convenient baptism window has been searched negatively in the supplied St Augustine images.

2. The packet sometimes calls Anne Morris "mother" through the Boyd-card structure but later correctly treats her as likely later wife/possible stepmother.
   - Future analysis should use "Robert's wife Anne Morris" unless and until a primary record proves maternity.

3. The 1630 ROLLCO John Gurney apprenticeship-master event is high value but under-specified.
   - Full export/detail is needed before treating it as the same John.

4. The will image `31787_A002570-00422.jpg` is referenced but not present in the current repo checkout.
   - The source can be created from the transcription, but final publication should retain or at least validate against the image.

5. Section 13 and sections 14-23 reference many uploaded PDFs/images that are not present under the current repo checkout.
   - v33 reserves source/media paths, but Phase 2 should not claim media retention unless the files are actually supplied.

6. The religious-language section is useful but easy to overweight.
   - Keep it as minor context only; it does not prove Puritan identity or emigration intent.

7. The St Swithin John Grine / Mary record is attractive but risky.
   - Wife Mary and January 1640/1 timing are tempting, but the surname reading is weak and the migration window is very tight.

8. The St Magnus John Grone burial should be explicitly parked as exclusionary/false-positive.
   - Candidate D John was alive at Robert's probate on 23 September 1625, so a 5 July 1625 burial cannot be him unless one of the records is misidentified.

9. Old Change geography is important, but it should not be treated as an emigration corridor.
   - It is currently a trade/parish/search-geography clue, not a proven migration-network clue.

10. The current packet has no final "decision matrix."
   - Add or maintain a concise table with Candidate D support, neutral/unknown, and against/elimination conditions. This will help later agents avoid flattening unresolved tension.

## 5. Proposed decision matrix for later analysis

| Question | Strengthens Candidate D if... | Weakens/eliminates if... |
|---|---|---|
| Post-1625 London continuity | John disappears from London records before/around 1641 | John remains in St Augustine/Drapers/London after the colonial record horizon |
| Wife Mary | A John Gurney in this cluster marries Mary before the colonial children | Wife is another named woman or no Mary bridge emerges after focused search |
| Children | Sarah, Mary, Richard, John, Peter or close pattern appears | A non-matching continuous London child set appears after 1625 |
| ROLLCO 1630 | Same John, and no later London continuity follows | Same John remains embedded in London trade too late |
| 1638 St Augustine inhabitant | Same John and compatible with migration timing | Same John is still clearly London-resident too close to or after colonial records |
| Missing baptism | A nearby-parish Robert/John bridge appears | No bridge after targeted St Augustine/nearby parish searches |
