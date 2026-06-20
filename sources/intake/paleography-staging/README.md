# Paleography staging — open brief

This folder stages manuscript-image briefs for outsourced transcription. 

> **Source terms:** all images are FamilySearch-sourced (17th-c. manuscript, public-domain content under FamilySearch viewing terms). Masters live in `sources/media/<set>/_local/` (off GitHub) or, for in-progress packets, in `images/`.

## Process notes (read before staging or incorporating a batch)

Two distinct roles run through this folder. Keep them separate.

**Outsourcer (this repo / the maintainer) — staging a brief and incorporating the result:**
- **Give the subcontractor every image the question needs.** When the question is "who is the testator," the brief must include the will's **opening** page, not only the continuation that carries the name of interest — packets 16a/16b could not name their testators because only continuation pages were staged (the fix became Packet 20). Rather than costly over-analysis to determine exact pages, it is acceptable to include pages before or after the target (no more than 10 buffer images total). When available, provide the machine transcription text for location purposes-only. The outsourcer should include questions that the transcription may answer and may include context, terminology, or names that may help in the paleographic work.
- **Masters belong in `sources/media/<set>/_local/`, never long-term in this folder's `images/`.** `images/` is a transient handoff staging area; FamilySearch masters must not sit committed here. On incorporation, move every relied-on master into the right `sources/media/<set>/_local/` folder (gitignored) and document it in that folder's committed `README.md`.
- **When incorporating into research after analysis, each promoted finding needs the full chain:** a citation in the research/corpus file → a `sourceId` in `data/sources.json` (the `familysearch-fulltext-search` catch-all is fine for FTS image reads; mint a dedicated sourceId only for a discrete named document, e.g. a specific will) → a corpus extract in `sources/corpus_supplement/` for any rich primary text → the relied-on images in `sources/media/<set>/_local/`. **The packet report in `done/` is transient — preserve full transcriptions in `corpus_supplement`, not only in the report.**
- **Record negatives and false positives as findings** (e.g. packet 16c = Robert Webber, not a Gurney; packet 14f "Cropley" = formulaic Latin), and route open follow-ups to the subject file or a lead — do not accumulate a parallel to-do list in this README.
- When the subcontractor self-locates a missing image (packet 21b admon, packet 23 1758 recital), **verify the located page actually matches the intended record** (parish, name, date) before trusting it.
- **Do not re-stage a page that has already been worked to exhaustion** (e.g. East Dereham register img 725 has deep-analysis + two second-opinion passes; the East Dereham court 1662/65 "Margaret" page is image-confirmed degraded). Re-stage only when something genuinely new is supplied (a different enhancement, additional context pages, or a specialist tier) — not in the hope of a different result from the same image.

**Subcontracted paleography (the outsourced AI reader) — its job and its limits:**
- It transcribes the provided images, attempts to find any images the brief left out, and returns a `packet-NN-*.md` report with best-effort transcription, confidence notes, and explicit negatives. Its report is a finding aid for the outsourcer to verify and incorporate — not itself a citable source layer.
- **Dense Latin manorial/secretary court hand routinely defeats it** (Cawston death presentments, the East Dereham 1662/65 page). Treat "blocked / unresolved" as an expected outcome for those and either flag for a specialist or accept the negative; do not re-stage the same hard page expecting a different result.
- **Watch the Syon↔Lyon trap** (the looped opening long-S): the Earsham family forename is **Syon/Sion**, repeatedly misreadable as Lyon (recognition note already logged).
- Treat machine/OCR snippets as locators only; the surname/forename at the exact point of interest is usually where the OCR fails, so it must come from the image.

---

## Open packets — batch staged 2026-06-20

> **Image-download status.** The fresh targets in this batch are **medieval muster/retinue membranes** held by AALT (Anglo-American Legal Tradition, `aalt.law.uh.edu`) and one French collection (BnF). **AALT was offline at staging time** (connection refused on all mirrors), so the membrane JPGs are **not yet downloaded into `images/`**. The briefs below carry the exact TNA/BnF references and the AALT path convention so the images can be pulled mechanically once AALT is reachable. Packet 30 is a **locate-first** task (no image exists until the parish entry is indexed). Until images are in `images/<packet>/`, these packets are *specified but not yet dispatchable*.

These four soldier packets share a source (medievalsoldier.org index → AALT membrane image) and a method: **the index row is already known; the membrane read is for the man's neighbours and any origin/status tag, to site him Norfolk (our West-Barsham/Harpley axis) vs. West-Country/Somerset vs. an exclusion zone.** They are *not* full-transcription jobs — the muster Latin is formulaic; the ask is name-spotting along the membrane and reading any locative byname. Subject grounding: `research/topics/gurney-medieval-soldier-database.md`.

### Packet 26 — Richard Gurney esquire, 1387 Arundel naval expedition (lead L-72)
- **Processed 2026-06-20:** access attempt timed out; no image available. Blocked report: `done/packet-26-richard-gurney-1387-arundel.md`.
- **Target image(s):** TNA **E101/40/34, membrane 1** (AALT path convention: `aalt.law.uh.edu/AALT#/…/E101_40_34/` → IMG of m1; pull m1 plus the membrane before/after for retinue context). **Also check** TNA **E101/41/5 m5** (1388) — the medievalsoldier database carries the 1387 record but *not* a 1388 one, so the lead's second citation needs verification against the original.
- **Index data (finding aid, from the *Soldier in Later Medieval England* DB, confirmed 2026-06-20):** "Gurney, Richard — Esquire — Man-at-Arms — Naval Service (expedition) — captain: Edward Courtenay, earl of Devon — commander: Richard FitzAlan, earl of Arundel — service date 13 March 1387 — TNA E101/40/34 m1i."
- **Questions:** (1) Whose retinue/sub-retinue is Richard listed under, and who are his membrane neighbours (names + any "of <place>" tags)? (2) Any locative byname or county for Richard himself? (3) Confirm the rank "esquire" and forename "Richard" against the membrane. (4) Does E101/41/5 m5 (1388) carry a second Richard Gurney record, and under whom?
- **Why it matters:** Richard esquire is unplaced in both the Norfolk and Somerset Gournay pedigrees; he served under Arundel, the very magnate Edmund G23 was steward for. Membrane geography would test whether Daniel Gurney's hedged "Robert" for G22 might in fact be a Richard.

### Packet 27 — John Gournay, Harfleur garrison 1417/1418 (lead L-73)
- **Processed 2026-06-20:** access attempt timed out; no images available. Blocked report: `done/packet-27-john-gournay-harfleur.md`.
- **Target image(s):** TNA **E101/48/17** (1417) and **E101/48/19** (1418), AALT; and for comparison **E101/48/6** (G21 Thomas Gournay I's own 1418 Harfleur service).
- **Index data (finding aid):** "John Gournay, man-at-arms, Harfleur garrison under Thomas Beaufort / Sir Hugh Luttrell, 1417–18."
- **Questions:** (1) Is this John Gournay listed in the **same retinue or on the same membrane** as Thomas Gournay I (G21) at Harfleur? (2) Any rank/status or locative tag distinguishing him? (3) Membrane neighbours.
- **Why it matters:** a John Gournay alongside G21 Thomas's documented 1418 Harfleur service would test a brother/cousin/son in the same Lancastrian garrison.

### Packet 28 — John Gurnay, 1422 Poissy/Pont-Meulan, Harling retinue (lead L-74)
- **Processed 2026-06-20:** BnF/Gallica attempt did not return the image. Blocked report: `done/packet-28-john-gurnay-harling-retinue.md`.
- **Target image(s):** **BnF, MS Français 25766, no. 816** (Quittances et pièces diverses). Check BnF **Gallica** for a digitisation of Fr. 25766; if not online, this is a BnF reading-room/microfilm pull (flag as not-online).
- **Index data (finding aid):** "John Gurnay, man-at-arms, garrison of Poissy / Pont-Meulan, retinue of Sir Robert Harling of East Harling, Norfolk (nephew of Sir John Fastolf), 1422."
- **Questions:** (1) Confirm the surname spelling/forename on the piece. (2) Any locative byname? (3) Retinue context — is Harling's Norfolk affinity visible in the co-listed names?
- **Why it matters:** Sir Robert Harling's retinue is a Norfolk-gentry military network tied to the Fastolf circle already threaded through the repo's Heylesdon/Saxthorpe story; tests a Norfolk cadet near G21/G22 (but East Harling is the SE/Breckland zone, not our NW axis).

### Packet 29 — John Gurnay archer, 1385 naval expedition, Percy retinue (lead L-154)
- **Processed 2026-06-20:** access attempt timed out; no image available. Blocked report: `done/packet-29-john-gurnay-1385-percy.md`.
- **Target image(s):** TNA **E101/40/39, membrane 2**, AALT.
- **Index data (finding aid, confirmed 2026-06-20):** "Gurnay, John — Archer — Naval Service (expedition) — captain & commander: Thomas Percy, earl of Worcester — service date 30 April 1385 — TNA E101/40/39 m2."
- **Questions:** (1) Membrane neighbours and any locative tag. (2) Status (the DB gives no status — confirm archer rank). (3) Any link to the same naval theatre as Richard's 1387 service two years later.
- **Why it matters:** a second Gurney in royal naval service in the same decade as Richard esquire (1387); both naval. Surfaced 2026-06-20 via the medievalsoldier database; not previously in the soldier-database companion.

### Packet 30 — St Ann Blackfriars 1615 baptism, father "F" or "P" Gurney (lead L-16) — LOCATE-FIRST
- **Processed 2026-06-20:** no register image available. Existing FamilySearch index `JW7Y-C3B` reads the father as `Wm.`; original-image verification remains blocked. Report: `done/packet-30-st-ann-blackfriars-1615.md`.
- **Status:** no image staged. The entry must first be **located** in an index (Ancestry "London, England, Church of England Births and Baptisms 1813… / IGI", or the LMA register **P69/…** for St Anne Blackfriars, baptisms c.1615), then the **register image** pulled (LMA images are served via Ancestry, not FamilySearch das/v2).
- **Question:** read the father's forename initial — is it **"F"** (Francis) or **"P"** (Peter/Philip)? Early-17th-c. F/P confusion is the whole question; the original register image has never been examined.
- **Why it matters:** bears on the emigrant-John origin hypotheses (a London/Blackfriars Gurney household c.1615).

### Packet 31 — Maldon borough court, the 1630 & 1636 "Gournay" entries (leads L-97, L-8) — DISPATCHABLE (FamilySearch)
- **Processed 2026-06-20:** the 1630 page names `Franciscus Gournay gent.` among the jurors. The supposed 1636 page is explicitly dated **1676** and names Francis Gournay, gentleman, as a borough bailiff. Report: `done/packet-31-maldon-gournay-courts.md`.
- **Status:** **IMAGES DOWNLOADED 2026-06-20** → `images/packet-31-maldon-gournay-courts/maldon-court-1630-YTV.jpg` and `maldon-court-1636-BQG.jpg` (full-res das/v2 masters). Surfaced by FTS query `+Gournay +Maldon` (92 Maldon hits; 26 pre-1700). Ready to dispatch.
- **Target image(s):** Maldon, Essex borough court — **1630** (ark `3:1:9Q97-YSLK-YTV`) and **1636** (ark `3:1:9Q97-YSLZ-BQG`), now staged. (The 1669–1676 cluster — arks `…YSL8-9VG`, `…YSLK-2HT`, `…YSLZ-B78`, etc. — is the *son* Francis Gournay of Maldon, d.1677, already biographied by Bernau; lower priority, pull only if the early pair points to a continuous holding.)
- **Index data (finding aid, machine transcript — salad, locator only):** 1630 (`YTV`): a court/jury list — "*…Quinto Anno Dm 1630 Thomas Brayley … John Rallingford Jur[ors] … Gournay … Samuel London … Robt Feninger …*". 1636 (`BQG`): names "**Francis Gournay**" explicitly — "*…Anno Dm 16[3]6 … Francis Gournay …*" (the OCR date digit is unreliable; confirm 1636 vs 1676 from the image, since 1676 would make it the son not G14). The forename and substance must come from the image.
- **Questions:** (1) Who is the Gournay named in the **1630** and **1636** Maldon courts — forename, status, the matter (admission, presentment, debt, office)? (2) Is it **Francis Gournay (G14, the Merchant Taylor / John G13's father)**, who married Anne Browning of the Maldon Browning family — i.e. is he at Maldon by 1630, while his St Benet Fink (London) children still run to 1637? Or a distinct earlier Maldon Gournay?
- **Why it matters:** Francis G14's post-1637 whereabouts and death are unlocated (lead L-8); the standing assumption is London or a Maldon move. A securely-read Francis Gournay in the 1630/1636 Maldon courts would place the direct line's G14 at Maldon a decade before his children's London baptisms end — reshaping where to hunt his will (Essex Commissary, not Norwich).
