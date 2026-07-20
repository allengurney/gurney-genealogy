# Kickoff prompt — online discovery campaign round 4 (G8–G37)

Work in main. Read AGENTS.md first; read path-scoped rules before substantive edits. **No repo edits of existing content** — write all output to a NEW dump `sources/intake/dump-files/dump-<TODAY>-round4.md`, with images AND raw text extracts saved via file operations into a sibling `dump-<TODAY>-files-round4/` folder. Include actual URLs for every web object. Chrome is authenticated for FamilySearch, FindMyPast, Ancestry.

TOPIC: Round 4 — this round PIVOTS FROM DISCOVERY TO DEPTH. Rounds 1–3 built a complete in-window Norfolk Gurney probate census and located the three new humble probates to specific films/references. Round 4 should READ the staged high-value documents (packet 53) rather than widen the net further.

CONTEXT — read first: `dump-2026-07-18-round3.md` (esp. §1, §3, §6, §11) + `dump-2026-07-18-round2.md` §7 + memory `online-discovery-campaign-2026-07-18.md`. Ground each lead with `research_leads.py context` and repo_search before working it; never grep repo content. Before designing searches read online-discovery-strategy + FS-FTS + FMP + paleography skills.

PRIORITY MENU (depth-first — favor 1–3):

1. **⭐ Read Margery Gurney's will** — ANF register **v.35 (Offwood) 1602-1604, FamilySearch DGS 8045772 / Film 167091, folio ~191** (NRO MF 197). Image-only (not full-text — FTS coverage on 008045772 = 0). Open the film via `records/images/search-results?imageGroupNumbers=008045772`, load `window.__imgs`, calibrate folio→image (register ≈1 img/opening; pull 1 calibration leaf near img 191, read the written folio number, interpolate), then das/v2 → S3 → PowerShell pull the will leaf(s). Stage as a **paleography packet 53** for expert transcription. QUESTIONS: does the will name her late husband + children/kin? Does it connect to Francis G14's East Dereham presence (children bapt. there c.1609/10–1633) or explain WHY Francis settled his young family at Dereham (a pre-existing Gurney household)? This is the top G13-origin target.

2. **⭐ Read the Thomas Gurnay Esq. of Great Ellingham inventory 1615-16 (+ any accompanying admon/wardship)** — explore for potential G13 fostering leads and resolves a live CONFLICT: the g15 companion (2026-06-11) concluded Henry G15's eldest son Thomas was alive in the 1 May 1621 will and died 1621×1623 (debunking the older "Thomas d.1614"), but this primary inventory lands on the old date. DECISIVE TEST: is the administrator **Martha** (Thomas's widow, née Lewkenor) and/or the heir **Edward** (b.1608, then a minor)? If yes, Henry's eldest son Thomas died 1615-16 (overturns the companion) and it WEAKENS the L-136 uncle-Thomas fostering branch (but might offer other context clues). Get the NRO reference first (permalink `gurnay-thomas-esquire-of-great-ellingham-norfolk` — was 502 in R3; Ancestry 62679/155780) → identify court/register → FS film. Gentry style suggests NCC or ANW, not ANF.

3. **DO NOT PURSUE - ALREADY EXHAUSTIVELY RESEARCHED -- ⭐ FMP London Apprenticeship Abstracts 1442-1850 — open the 12 "John Gurney" rows (≈1605-1655)** for father="Francis" and/or company="Merchant Taylors'" (patrimony). `search.findmypast.co.uk/search-world-records/london-apprenticeship-abstracts-1442-1850?firstname=john&lastname=gurney`. Rows render in cross-origin iframes — open each record page interactively (authenticated) and read the transcription; do NOT fight the iframe from the parent frame. The untried "did John G13 apprentice in his father's London world?" test — a John-son-of-Francis binding would near-anchor the Francis→John link. Also check Merchant Taylors' Company apprentice/freedom records directly (ROLLCO does NOT cover Merchant Taylors').

4. Locate the **Alexander Gurney ANF admon act-book DGS** in FS catalog `koha:291384` film-notes and read fo.101 (administrator names kin?).

5. **L-245 Millican, Register of the Freemen of Norwich 1548-1713** (Rivett-son-of-Francis, decisive) — HathiTrust Record/010311933 full-text search for `Rivett`/`Ryvett`; or NRO online version; or FS book 609610. Plus **Rutledge, Great Yarmouth apprenticeship indentures 1563-1665** (FS koha:84018). (NFRO won't help — Phase 2 1317-1713 not loaded yet.)

6. **NEHH Quartex reads** — `congregationallibrary.quartexcollections.com/documents/search?search=Gurney`; read **Abington First Church 1714-1949** (NEW, Weymouth/Bridgewater orbit for G8-G12) + Braintree (1697-1871) + Hingham (1635-1806) transcriptions/finding-aids for Gurney entries.

7. Retry **NROCAT** (`nrocat.norfolk.gov.uk` / `nrocatalogue.norfolk.gov.uk`) when the server recovers (502 all of R3): Thomas Gt Ellingham reference; NRS 21256-21355 Whinburgh surrender item-dates (does a piece cover 1597 / 1604-1626? — L-128 GATED).  Note - Server is still down but expect recovery in a day or two. Keep as lead.

8. Creative / wildcard (2x) — at least two new sources not yet consulted 

9. Creative / wildcard (2x) — keep pursuing G13 origins (the "why East Dereham" question; G13's childhood; fostering hypothesis).

HARD CONSTRAINTS (carry forward): zero-token image handling (pull to disk via the das/v2 pipeline OR stage arks; never relay presigned S3/image URLs through output). Stop-after-two-failures per mechanism; negative-results ledger; [REC]/[GATED] roll-ups with human URLs; stage paleography packets. DATE HYGIENE: John G13's Dereham baptism is c.1609/10 (case-file v4), not 1616.

GOALS: read the staged documents (depth over breadth this round). End with: dump complete (structured for assimilation, placement labels), memory updated, packet 53 pulled/transcribed, and a round-5 kickoff prompt if this is the thread's last round.
