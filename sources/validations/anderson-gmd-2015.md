# Anderson, *Great Migration Directory* (2015) — Validation

**Source:** `anderson-gmd-2015` in `data/sources.json`

Audit trail for what has been examined from this source and where findings landed. Findings themselves live with the research subjects; this file is thin by design.

---

## Scope of examination

- 2026-04-08 (chat 324600c7) — page 158 extract (John Gurney-1 entry) examined by Allen and Claude.

## What was examined

The one-line entry for John Gurney on p. 158, including all six cited references:
- WJ 2:422 (Winthrop's Journal)
- MBCR 1:331 (Massachusetts Bay Colony Records)
- NEHGR 62:94
- SPR Case #338 (Suffolk Probate Records)
- Weymouth Hist 3:251
- TAG 10:70–73

Entry text as extracted: *Gurney, John: Unknown; 1636; Boston, Braintree [refs above].*

Corpus extract committed at `sources/corpus/The Great Migration Directory 2025 Page 158.txt` (partial; full directory not extracted).

## Scope limitations

- Only p. 158 has been examined. The directory's methodology sections and any other Gurney or Gourney entries have not been reviewed.
- None of the six sources Anderson cites have been pulled. TAG 10:70–73 and NEHGR 62:94 are Tier 1 open items (AI-Rules §10); the other four are lower priority but also unreviewed.
- Anderson's "Banks Mss." context — whether Anderson examined Banks's original manuscripts or worked only from Brownell's 1937 edition — is not established.

## Where findings landed

| Finding | Destination |
|---|---|
| All John Gurney-1 findings (origin "Unknown" as implicit Banks rejection; 1636 arrival discrepancy; Boston+Braintree settlements; pull list with priorities; 6 open items) | `research/people/g13-john-gurney-1.md` |
| Tier 1 pull priorities (TAG, NEHGR) | `research/people/g13-john-gurney-1.md` and AI-Rules §10 |
| Standing interpretive principles (Anderson "Unknown" = implicit Banks rejection; 1636 vs. 1641 discrepancy) | AI-Rules §8 and `data/sources.json` notes |
