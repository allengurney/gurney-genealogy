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

**Probable root cause:** The 1858 Supplement file in the project knowledge has been the most heavily extracted (it contains the Notes 181–209 with Francis Gurney content that drove the John-1 research). When the companions were generated in chat bcb40001, "Supplement" may have been substituted automatically for "DG" without verifying that the page numbers fell in the Supplement's range.

## G20–G37 sweep (2026-04-16)

Every research companion in the G20–G37 range reviewed. Results:

| File | Status | Notes |
|---|---|---|
| g37-eudes-de-gournay | clean | No DG-II citations; uses DG-I correctly. |
| g36-hugh-de-gournay-i | clean | DG-I only. |
| g35-renaud-de-gournay | clean | DG-I only. |
| g34-hugh-de-gournay-ii | clean | DG-I only. |
| g33-hugh-de-gournay-iii | clean | DG-I only. |
| g32-gerard-de-gournay | clean | DG-I only. |
| g31-walter-de-gournay | clean | DG-I only. |
| g30-william-de-gournay-i | clean | DG-I only. |
| g29-matthew-de-gournay | clean | DG-I + DG-II p. 310 (correct). |
| g28-william-de-gournay-ii | clean | DG-I only. |
| g27-sir-john-de-gournay-i | clean | DG-I + DG-Supp (pp. 785–786, in range). |
| **g26-sir-william-de-gournay-iii** | **fixed** | pp. 325–355 relabeled Supplement → DG-II. p. 786 Supp citation correctly retained. |
| **g25-john-de-gournay-iii** | **fixed** | pp. 355–357 and p. 356 relabeled Supplement → DG-II. |
| **g24-john-de-gournay-iv** | **fixed** | pp. 355–357 and 357–358 relabeled Supplement → DG-II. |
| **g23-edmund-gurney** | **fixed** | pp. 357–363 and Appendix LXIII (p. 364+) relabeled Supplement → DG-II. Fixed 2026-04-16 earlier commit. |
| **g22-robert-gournay** | **fixed** | p. 363 and pp. 374+ relabeled Supplement → DG-II/DG-I as appropriate. Fixed 2026-04-16 earlier commit. |
| g21-thomas-gournay-i | clean | DG-I + DG-Supp pp. 789–795 (in range). |
| g20-thomas-gournay-ii | clean | DG-I + DG-Supp pp. 814 ff. (in range). |

All narrative fact sheets in this range use the correct `DG-N` form — the error was contained to the research companions. Six files fixed total.

## Remaining scope

- [ ] Sweep G19–G15 (G19 William IV, G18 William V, G17 Anthony, G16 Francis, G15 Henry) research companions when they next need edits, or proactively.
- [ ] Sweep G04–G05 research companions (Lester Sawyer Gurney and Lester Sawyer Gurney Jr.) — these are much later and less likely to cite DG at all, but should be checked.
- [ ] Verify `sources/corpus/daniel-gurney-readme.md` reflects pagination grammar clearly so future sessions don't repeat the error.

## Action

- [x] Document the issue (this file).
- [x] Fix G23 and G22 (2026-04-16 earlier commit `1e48a5e`, `77fb9f4`).
- [x] Fix G24, G25, G26 (2026-04-16 commit `d57930b`).
- [x] Sweep G20–G37 research companions (this file).
- [ ] Sweep G15–G19 research companions.
- [ ] Sweep G04–G05 research companions.
- [ ] Verify the corpus DG readme reflects pagination grammar accurately.

## Related

- AI-Rules §4 (citation format) and §8 (DG source flags).
- `sources/corpus/daniel-gurney-readme.md` (pagination grammar).
