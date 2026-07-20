# Kickoff prompt — Online discovery round 3 (G8–G37)

Work in main. Read AGENTS.md first; read path-scoped rules before substantive edits. **No repo edits of existing content** — write all output as you work to a NEW dump file `sources/intake/dump-files/dump-<TODAY>-round3.md`, with any images AND raw text extracts saved via file operations into a sibling `dump-<TODAY>-files-round3/` folder. Include actual URLs for every web object. Chrome is authenticated for FamilySearch.org, FindMyPast.co.uk, and Ancestry.com.

TOPIC: Online genealogy research for ancestors G8 to G37 — round 3 of the discovery campaign.

CONTEXT — rounds 1–2 (dumps `dump-2026-07-18-round1.md`, `dump-2026-07-18-round2.md`):
- Round 2 built a **complete in-window (1585–1650) Norfolk Gurney probate census** from **Ancestry collection 62679** (`?name=_Gurn*&f-F0003=norfolk&count=50`; sourceId `norfolk-wills-probate-index-1371-1858`). The record-detail page is FREE and carries a **Notes = residence** field + an **NRO catalogue permalink** — cheap enrichment route. Three NEW records surfaced, all verified new: **Margery Gurney (Gurnye) widow of EAST DEREHAM, will 1602-03** (John G13's birthplace, a decade pre-baptism — highest-value G13 anchor); **Thomas Gurnay Esquire of GREAT ELLINGHAM, inventory 1615-16** (L-136 foster-hearth uncle Thomas candidate); **Alexander Gurney of TASBURGH, admon 1617** (S-Norfolk cluster).
- **Out-of-band progress:** L-174 BHO search partially completed since round 2 (no longer part of this campaign).

Before designing searches: read the online-discovery-strategy skill + `data/search-variants.json` and the FS-FTS / FMP / BHO skills. Ground each lead with `tools/research_leads.py context` and repo_search before working it; never grep repo content.

HARD PROCESS CONSTRAINTS (carry forward): (1) **Breadth is the deliverable** — 8–10 distinct topics, text-first, soft cap ~10–12 tool calls per topic on the first pass; deepen only 2–3 chaining discoveries after the breadth pass. (2) **Zero-token image handling** — never relay presigned S3/image URLs through output; validate a file-based pipeline in ≤10 calls or STAGE an exact ark list for a Codex/CDP pull and move on. (3) Stop-after-two-failures per mechanism; negative-results ledger; [REC]/[GATED] roll-ups with human URLs; stage paleography packets (next: 53).

PRIORITY MENU for round 3 (favor the chaining discoveries first):
1. **East Dereham Margery Gurney (Gurnye) widow will 1602-03** — read the will image/abstract (NRO permalink `nrocatalogue.norfolk.gov.uk/index.php/gurney-gurnye-margery-of-east-dereham-widow`; Ancestry 62679/257086). Does it name children/kin? Connect to Francis G14's Dereham residence or the later Margaret/Margery copyhold (1662-94)? Highest-value G13-origin target.
2. **Thomas Gurnay Esq. of Great Ellingham, inventory 1615-16** (62679/155780; NRO permalink) — relate to G15 Henry (brother? father/?G16); an intestate inventory implies an admon/guardianship. Feeds L-136.
3. **Alexander Gurney of Tasburgh admon 1617** (62679/105314) + the **pre-1600 residues** (Robert Gurney inv 1588/admon 1591, Anne Gurnay admon 1595, John Gurne inv 1593, [-] inv 1599) — detail-read residences via 62679 record pages; map the collateral geography.
4. **Packet 53 staged-ark pull** — validate a zero-token image pipeline (or stage for Codex). Dereham DGS 004389483 undated Gurney `3:1:S3HY-D1S9-CYG`, `3:1:S3HY-D1S9-7DQ`; Earsham DGS 004389278 1719 Syon `3:1:S3HY-6XP3-H4R`, 1728 Lyon `3:1:S3HY-6XP3-HMJ`/`…C89`.
5. **L-245 decisive test** — archive.org full-text: Millican, *Register of the Freemen of Norwich 1548-1713* + Norwich apprentice indentures, for `Rivett`/`Ryvett` sons of Francis of Garveston.
6. **Creative Ideation** — Be innovative and identify and conduct research with at least one new source not previously consulted in the repo. 
7. **Providence vols 14 & 20** — Google Books `WMUTAAAAYAAJ` (vol 14) / HathiTrust; complete the 21-vol sweep.
8. **NEHH (Congregational Library)** Gurney name-search — Braintree First Church 1707-1871 + Hingham First Parish 1635-1806 transcriptions (Weymouth is a confirmed NEHH gap). https://www.congregationallibrary.org/nehh/main
9. **L-174 BHO** L&P/State-Papers variant sweep + Dec-1602 Cecil entry — retry when the challenge clears (live-browser search; content-page WebFetch).
10. **NROCAT** item-level dates for Whinburgh surrenders NRS 21256–21355 (does a piece cover 1597 / 1604-1626?) — feeds L-128 GATED plan. https://nrocat.norfolk.gov.uk
11. **L-158** Norfolk CP25/1 Gurnay feet of fines on AALT (Robert #64 + unattributed set vs Rye's calendar); **L-135** Anne Browning (thin residual); **L-136** NRO-held Gt Ellingham/W.Barsham manorial (mostly GATED).

GOALS: max research via online discovery, minimal tokens; expert reasoning on analysis, not mechanics. End the turn with: dump complete (structured for assimilation, with placement labels), memory updated, packet 53 staged/pulled if images, and a round-4 kickoff prompt if this is the thread's last round.
TURN SIZE: ~100–120 tool calls; breadth pass first, depth second.
