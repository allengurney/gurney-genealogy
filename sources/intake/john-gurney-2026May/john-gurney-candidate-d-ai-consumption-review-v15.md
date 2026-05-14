# Candidate D working packet AI-consumption review v15

```yaml
created: 2026-05-14
supersedes: sources/intake/john-gurney-2026May/john-gurney-candidate-d-ai-consumption-review-v14.md
reviewed_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
ai_ready_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v15.md
research_prompt: sources/intake/john-gurney-2026May/john-gurney-candidate-d-claude-code-research-prompt-v15.md
phase_1_patchsets:
  - sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md
  - sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md
```

## 1. AI-consumption assessment

The v13 packet is usable but too dense for a first-pass research agent if the agent also has to handle repo logistics, source creation, media movement, and citation normalization. Its strongest content is the detailed record-by-record extraction. Its weakest structure is that confirmed evidence, working inference, context-source strategy, and broad comparator material are interleaved.

The v15 optimization keeps the evidence intact and adds a control layer:

1. A source map from packet sections to stable repo `sourceId`s.
2. A top-discriminator block for the 1638 St Augustine BHO source.
3. A direct Candidate D lane and a controlled comparator-density lane.
4. Clear non-goals for the next research pass.
5. A scratch-file protocol that is efficiency-driven rather than automatic busy work.

## 2. Highest-value changes before deeper analysis

1. Apply v32 and v33 before the research pass.
   - User confirmed this will happen.
   - The next researcher should assume those source handles are available after Phase 2, then spend research time on evidence rather than repo plumbing.

2. Elevate `bho-london-inhabitants-st-augustine-1638` as a top discriminator and add prior-chat pre-work.
   - Existing repo source lists John Gurney in the St Augustine rents section in 1638 at 10 pounds.
   - Because Candidate D is St Augustine / Old Change anchored, this is not just a generic same-name London lead.
   - Research task: treat 1638 as one checkpoint and search for St Augustine / Old Change rate, tithe, poor-rate, churchwarden, vestry, inhabitant, Protestation, subsidy, or assessment records between 1625 and 1641.

3. Split the next research into direct and comparator lanes.
   - Direct: Robert/John/Drapers/St Augustine/Old Change.
   - Comparator: Grine/Grene/Grone records not yet connected to Robert, Old Change, or Drapers.
   - Comparator records can demonstrate density of overlapping names/communities without contaminating the Candidate D claim.

4. Use a lead tracker only if it improves efficiency.
   - Do not create redundant scratch files.
   - If used, keep it lean: lead, lane, sourceId, searched where, result, Candidate D impact, next action.

5. Make post-1625 London continuity the first support/elimination test.
   - If Candidate D remains active as a Drapers/St Augustine London resident after 1641, he is likely eliminated.
   - If he disappears from the London record while matching wife/children or migration signals emerge, he strengthens.

## 3. Revisions to issues and cautions

1. Broad St Augustine post-1601 searching was intentionally inclusive.
   - Do not frame the negative post-1601 replacement-John search as an internal conflict. The broader date range was searched to avoid missing adjacent evidence.

2. Anne Morris wording should stay precise.
   - Use "Robert's wife Anne Morris" or "later wife Anne Morris."
   - Do not call her Candidate D John's mother unless a primary record proves maternity.

3. The 1630 ROLLCO John Gurney master event is probably the same John but still needs full detail.
   - Current evidence supports prevalence/likelihood because the name, company, and sequence fit the 1623/4 freeman.
   - Pull full event detail to confirm, not to re-litigate from scratch.

4. The will image is now copied into intake.
   - Current untracked file: `sources/intake/john-gurney-2026May/31787_A002570-00422.jpg`.
   - v32 already says to move it into `sources/media/acl-robert-gurney-will-1625/` during Phase 2 if available.

5. Lower-probability section 13-23 images/PDFs should not be forced into the repo.
   - They can remain available outside the repo unless needed.
   - Do not claim media retention for absent comparator images.

6. Religion should be treated as a real migration-corridor factor without overstating the will wording.
   - Robert's will language is not enough by itself to prove Puritan identity.
   - But religion was a prevailing rationale for Massachusetts Bay migration; lack of a religious catalyst or corridor should affect comparison with Candidate B.
   - Search for stronger religious/parish-network indicators rather than relying on formulaic will language.

7. The St Swithin John Grine / Mary record remains attractive but risky.
   - Wife Mary and January 1640/1 matter.
   - The surname reading and very tight migration window keep it in comparator status unless bridged.

8. The St Magnus John Grone burial should remain in scope as density/exclusionary context.
   - It is probably not Candidate D because Candidate D John proved Robert's will on 23 September 1625.
   - It can still demonstrate how many similar John-name records exist in overlapping communities.

9. Old Change is important but not yet an emigration corridor.
   - Treat it as trade/parish/search geography unless stronger religious or migration-network evidence is found.

10. Avoid a decision matrix for now.
   - A matrix risks introducing bias too early.
   - Keep the next pass as objective research with findings, negative results, and clearly separated lanes.

## 4. Deliverables created in v15

- `sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v15.md`
- `sources/intake/john-gurney-2026May/john-gurney-candidate-d-ai-consumption-review-v15.md`
- `sources/intake/john-gurney-2026May/john-gurney-candidate-d-claude-code-research-prompt-v15.md`

## 5. Recommended next sequence

1. Apply v32.
2. Apply v33.
3. Use `john-gurney-candidate-d-claude-code-research-prompt-v15.md` to launch the next research pass.
4. Keep the first research round centered on St Augustine / Old Change continuity, BHO 1638 context, ROLLCO details, and wife/children evidence.
