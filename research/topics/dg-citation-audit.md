# DG Citation Style Audit

Cross-cutting topic file. Tracks systematic citation issues identified across the repo for the Daniel Gurney *Record* and *Supplement* corpus.

---

## Issue: "Supplement" misattribution

**Identified:** 2026-04-16, during transcript migration from chat bcb40001 (2026-04-03 fact sheet batch session).

**Pattern:** Several research companion files cite `Daniel Gurney, *Supplement* (1858), pp. NNN–NNN` where the actual reference should be `DG-II` (or in some cases DG-I or DG-III) — i.e., the published Parts of the 1848 *Record*, not the 1858 *Supplement*.

**The page-range test:** The 1858 Supplement runs roughly pp. 725–1096 (per the corpus extraction). Any "Supplement" citation with a page number under 725 is almost certainly miscited. Per AI-Rules §4 and §8, citations to DG should use:
- `[DG-I-NNN]` for Part I
- `[DG-II-NNN]` for Part II
- `[DG-III-NNN]` for Part III
- `[DG-IV-NNN]` for Part IV
- `[DG-Supp-NNN]` for the 1858 Supplement only

**Confirmed instances (as of 2026-04-16):**
- `research/people/g23-edmund-gurney-fact-sheet.research.md` — pp. 357–363 cited as "Supplement"; should be **DG-II**. Same file: Appendix LXIII (Wauncy), p. 364+ cited as "Supplement"; should be **DG-II**.
- `research/people/g22-robert-gournay-fact-sheet.research.md` — p. 363 cited as "Supplement"; should be **DG-II**. Same file: pp. 374+ (John Gurney V chapter) cited as "Supplement"; should be **DG-II**.

The narrative fact sheets `g23-edmund-gurney-fact-sheet.md` and `g22-robert-gournay-fact-sheet.md` use the correct `DG-II` form — the error is contained to the research companions.

**Probable root cause:** The 1858 Supplement file in the project knowledge has been the most heavily extracted (it contains the Notes 181–209 with Francis Gurney content that drove the John-1 research). When the G23/G22 companions were generated in chat bcb40001, "Supplement" may have been substituted automatically for "DG" without verifying that the page numbers fell in the Supplement's range.

## Action

- [x] Document the issue (this file).
- [ ] Fix `research/people/g23-edmund-gurney-fact-sheet.research.md` — Supplement → DG-II.
- [ ] Fix `research/people/g22-robert-gournay-fact-sheet.research.md` — Supplement → DG-II.
- [ ] Sweep all other research companions for the same pattern. Quick test: any citation of the form `Daniel Gurney, *Supplement* (1858), pp. NNN` where NNN < 725 is suspect.
- [ ] Verify the corpus DG file pagination is reflected accurately in `sources/corpus/daniel-gurney-readme.md` so future sessions don't repeat the error.

## Related

- AI-Rules §4 (citation format) and §8 (DG source flags).
- `sources/corpus/daniel-gurney-readme.md` (pagination grammar).
