# L-34 resolved — Edmund G23's 1387 will: leaf lost since the 18th c., text already in the repo

For patchset v91. Cleanup only — the will's content is already captured; this fixes provenance and a stale folio citation.

## What was established (2026-06-12/13)

The Norwich Consistory Court register entry for Edmund Gurnay (G23)'s 1387 will is **Harsyk folio 84**, and the folio is **lost** — the Norfolk Record Office catalogue (confirmed by Allen at the searchroom catalogue, 2026-06-13) records it as: "Gurney (Gurnay), Edmund, 1387 … **Index entry only. Folio missing. Not to be produced to the searchroom.** Finding aid: Norfolk Record Society vol. 16 (A–Hi). Use microfilm MF 23 or MF/RO 137."

Daniel Gurney explains the loss directly (Record, Part II, p. 363): "This will is given in Blomefield; but **in the time of Mr. Norris the part of the register which contained it was utterly rotted and destroyed**." Antiquary Anthony Norris died 1786, so the leaf has been gone since the eighteenth century — long before any microfilming. The FamilySearch film (DGS 008076261) and the NRO shelf-films (MF 23 = ff.1–157, MF/RO 137 = ff.1–249) all post-date the loss and reproduce only the surviving folios; **none holds folio 84.** The lead's original aim (pull the leaf for the Latin text) is therefore impossible — and unnecessary.

## The text already survives in the repo

The full will is preserved through two antiquarian witnesses who saw it before the folio rotted, both already in the repo:
- **Daniel Gurney's Supplement, Note 118** (full Latin) — already transcribed into the G23 companion: proved **1 August 1387 with a codicil annexed**; **four executors** (wife Katherine, son John, Osbert de Mundeford, Thomas Kempe); Katherine to have her full dower, all household utensils, and her share of all goods; £8 to the poor on the burial day; burial in the church of the Assumption of the Blessed Virgin, West Barsham.
- **Daniel Gurney's Record, Part II, p. 363** (English abstract) — adds: will dated at West Barsham **"Thursday the feast of the Ascension"** 1387 (= 16 May 1387); witnesses **William de Mildenhall, Vicar of West Barsham, and Nicholas de Barsham**; issue by Katherine de Wauncy: **John (heir), a second son believed Robert, and a daughter Jeanne who married Osbert Mundeford of Hockwold** (one of the executors). DG also cites Blomefield, vol. vii, p. 42.
- (DG's own fuller transcript is at his **Appendix LXV**, cited in the same passage, if an even fuller text is wanted later.)

## Cleanup operations for the patchset

**G23 companion (`research/people/g23-edmund-gurney-fact-sheet.research.md`) — DONE directly 2026-06-13** at Allen's request to perfect the will treatment, so the patchset must NOT re-apply these: corrected "fol. 34" → fol. 84 at the will-register bullet and the Sources list; revised the index-confirmation note to record fol. 84 as authoritative, the "folio missing / not produced to searchroom" status, and the Norris-era destruction provenance; and enriched the full-Latin section with the funeral feast, the two tapers, the "other sons" (*aliis filiis*) clause, John as son of Edmund *and* Katherine, the high-altar + church-repair bequests, the *voluntas*-vs-*testamentum* two-instrument distinction (resolving the penny-each vs £8 figures), and the restitution-under-blessing nuance — all from DG-Supp Note 118 (`sources/corpus/daniel-gurney-supplement.md`, lines ~2016–2068).

Remaining for the patchset:

1. **`research/places/west-barsham.md` — folio + provenance.** Correct the stale "fol. 34" at the body line (~26, "preserved in **Reg. Harsyke, fol. 34**") and the Sources line (~74, "Reg. Harsyke, fol. 34 … cited by DG-II") to **fol. 84** (Norwich Consistory Court; Norfolk Record Society vol. 16, A–Hi; Daniel Gurney's Record misprints the folio as 34). Add a one-line provenance note that the register folio was "utterly rotted and destroyed" by Anthony Norris's time (d. 1786) and the will survives only through the Dewes 1637 copy and Blomefield — cite Daniel Gurney, *Record* Part II, p. 363 (`sources/corpus/daniel-gurney-part-2.md`, lines ~4821–4835). Optionally enrich the west-barsham burial/Edmund section with the funeral-feast and high-altar/church-repair detail now in the G23 companion.
2. **L-34 → Resolved/closed** in the leads CSV (done in-line).

## Note on the FamilySearch session

FamilySearch authentication and the browser path were re-verified working on 2026-06-13 (the earlier four-subagent failure was the Anthropic account session limit, compounded by a FamilySearch auth timeout — both since cleared). No film walk was performed for L-34 because the documentary record (DG: folio destroyed in the 18th c.) makes it pointless. The working session is available for the other open browser leads (Harsyk is now closed; Visitation cross-check for L-112, colonial L-95/L-96 finish remain).
