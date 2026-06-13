**Done:** 2026-06-13 15:55 PT

# Patchset v92 — English-line Gurney wills: Anthony G17 reconciliation (L-112), Edmund G23 folio (L-34), Henry Spilman 1524 / Antony Gurney executor (L-101, packet 12)

**Arc:** the 2026-06-11/13 sessions on the Tudor–medieval Gurney wills. This is the English-ancestral half of the arc; the colonial-emigrant half (Billerica L-104, PCC L-6, military L-95, Bury L-96) is a separate patchset (v93).

**What the repo already absorbed (do NOT re-apply):** `data/ancestors.json` G17 already carries the corrected death (early Dec. 1557), the daughters Elizabeth and Cicely, and "Francis G16 predeceased"; the **G16 companion** already carries the core L-112 reconciliation (Henry omitted as heir-at-law taking the descended third under the Statute of Wills; the six grandchildren matching Pease's six children for Francis). v92 does not touch those.

**What v92 promotes:**
1. **L-112** — finishes the reconciliation on the **G17 companion**: marks the three "conflicts" resolved, retires the now-stale JSON-friction note, and adds the one genuinely new piece — Blomefield's impossible "grandson Henry, aged twenty-one" reconciled as Henry's *livery* age c. 1570 via the fourteen-year trust ending 1571. A matching succession note on the **G15 companion**.
2. **L-101 / packet 12** — promotes the expert image-read of **Henry Spilman's 1524 will** (Antony Gurney executor) into the G17 companion and corpus supplement, with the finding that the testator is most likely the Spelman of Great Ellingham who died without issue, so Anthony executed the will of the man from whom the family inherited the manor.
3. **L-34** — the `west-barsham.md` cleanup (folio 34 → 84; the leaf is lost, text survives via Dewes/Blomefield). The G23 companion was already perfected directly 2026-06-13.
4. Paleography packet 12 disposition; a small `data/ancestors.json` G17 enrichment.

**Source tracking:** all promoted content cites the existing sourceId `familysearch-fulltext-search` (validation `sources/validations/familysearch-fulltext-search.md` exists) and Daniel Gurney's Record/Supplement (existing corpus). No new sourceId, hence no new validation file.

**Leads CSV:** L-112, L-101, and L-34 status updates are applied directly (allowed class), marked "promoted in v92."

---

## Item 01 (promote) — G17 companion: resolve the L-112 conflicts

**Target:** `research/people/g17-anthony-gurney-fact-sheet.research.md`

**Operation — str_replace.** Replace:

```
Three consequences, two of them conflicts to preserve rather than resolve:

1. **Death date conflict — the will vs Blomefield.** A will made 6 December and proved 10 December 1557 means Anthony died c. 6–10 December 1557. Blomefield (vol. vii) gives 4 January 1555[/6], the reading this companion previously preferred over the project JSON's "December 1556." The will is a primary record naming the same man, place, and status ("of greater Elingham … Esquier"), so it now carries the most weight — and curiously the JSON's discarded "December 1556" was closest in shape (December death, mid-1550s). Unless a second Anthony Gurney, Esq., of Great Ellingham existed in 1557 (no evidence of one), **the death date should move to early December 1557**. Fact-sheet and JSON implications flagged for review, not yet applied.
2. **No living son named — and no Henry among the grandchildren.** The will names no wife and no son. The forty-year trust and the education clause imply the heirs were minors and that Anthony's son — the pedigree's **Francis (G16)** — was either already dead by December 1557 or (less likely, since he is wholly absent) provided for by separate settlement. The grandchildren named are Anthony, Thomas, Elizabeth, ffrances, and Anne Gurney, plus Anthony Drury (a daughter's Drury marriage). **Henry (G15), Blomefield's "grandson Henry" who succeeded to Great Ellingham, does not appear in the list.** If G15 Henry was born c. 1548–50 he should have been a minor grandchild in 1557 — his absence is a genuine puzzle: possibilities include birth after the will (making his traditional birth year too early), separate provision as the designated heir of the entailed third, or a pedigree wrinkle between Anthony and Henry not yet understood. Preserved as an open conflict.
3. **The grandchild "ffrances Gurney"** may be Francis or Frances; either way the will places a ffrances in the generation *below* Anthony's children — worth holding against the visitation pedigree (Anthony → Francis of West Barsham → Henry of Great Ellingham) when the G16 generation is next reviewed.

The daughters Elizabeth (£200 — a substantial marriage portion, suggesting unmarried in 1557) and Cicely (£20) are new names for the family group; neither appears in the current fact-sheet children list.
```

with:

```
Three consequences, now resolved (lead L-112):

1. **Death date — resolved to early December 1557.** A will made 6 December and proved 10 December 1557 means Anthony died c. 6–10 December 1557; the will is primary and supersedes Blomefield's traditional 4 January 1555/6 (vol. vii), which descends from the Blomefield/Parkin compilation. `data/ancestors.json` now reads "d. early Dec. 1557," with the daughters Elizabeth and Cicely (below) added there.
2. **Why Henry is absent from the grandchildren — he is the heir at law.** The will names no living son: Anthony's eldest son **Francis (G16) had predeceased him** (Blomefield, the 1563/89/1613 visitation, and Daniel Gurney all state it; the will's silence confirms it), so the fourteen-year trust over two-thirds of the knight-service manors is the classic minority-management vehicle for a dead son's children. **Henry (G15), the grandson-and-heir, takes the descended third by law (Statute of Wills, 1540) and so needs no legacy** — which is exactly why he is omitted while the five Gurney grandchildren (Anthony, Thomas, Elizabeth, ffrances, Anne) and the Drury grandchild are funded. Setting Henry alongside the five named Gurney grandchildren gives **six grandchildren matching Pease's six-children list for Francis G16** — so the named grandchildren are Henry's own siblings, and the will independently corroborates the Anthony → Francis → Henry line rather than contradicting it. Full treatment on the [G16 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g16-francis-gurney-fact-sheet.research.md).
3. **Blomefield's "grandson Henry, aged twenty-one" reconciled.** Blomefield's parish entry collapses Anthony's death and Henry's succession into one sentence — "died January 4, 1555, leaving Henry, his grandson and heir, aged twenty-one years" — impossible against Henry's 1548/9 birth (he was ~9 in 1557, not 21). The fourteen-year trust resolves it: running from December 1557 it ends in **1571**, the year the minor heir Henry (b. 21 Jan 1548/9) turns 21 and takes livery. Blomefield's "aged twenty-one" is therefore Henry's **livery age, c. 1570**, telescoped onto the (also mis-dated) death — not his age at his grandfather's death. The trust is the wardship instrument bridging the gap. See the [G15 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g15-henry-gurney-fact-sheet.research.md).
4. **The grandchild "ffrances Gurney"** sits in the generation below Anthony's children, so it is a grandchild named Francis (for his father G16) or Frances — not Francis G16 himself.

The daughters Elizabeth (£200 — a full marriage portion, so probably unmarried in 1557) and Cicely (£20 — probably already settled) are now carried in `data/ancestors.json` as Anthony's children; a further daughter married a Drury (mother of the grandchild Anthony Drurye).
```

## Item 02 (promote) — G17 companion: retire the stale JSON-friction note

**Target:** `research/people/g17-anthony-gurney-fact-sheet.research.md`

**Operation — str_replace.** Replace:

```
1. **Death date.** The project `ancestors_v3.json` gives "December 1556." This is unsupported. Blomefield's independent witness gives **4 January 1555 Old Style (= January 1556 modern reckoning)**. The "December 1556" reading in the JSON appears to be a misreading or transposition. Recommend updating to "d. 4 January 1555/6 (per Blomefield, vol. vii)."
```

with:

```
1. **Death date — resolved.** Superseded by Anthony's own will (made 6 Dec., proved 10 Dec. 1557): he died early December 1557, not 4 January 1555/6 (Blomefield) or "December 1556" (the former JSON value). `data/ancestors.json` now reads "b. c. 1499 — d. early Dec. 1557." See the will entry and reconciliation in Working Notes above.
```

## Item 03 (promote) — G17 companion: promote the packet-12 expert read of the 1524 Spilman will (resolves L-101)

**Target:** `research/people/g17-anthony-gurney-fact-sheet.research.md`

**Operation — str_replace.** Replace:

```
- **1524 — "Antony Gurney" executor to Henry Spilman, Esq.** Abstract: "HENRY SPILLMAN, Esquier, to be buried in the Church of St. James in [Great?] Ellingham … my wif, Antony Gurney and John Turrell, executors. D: 17 Feb — P. 1524" (register cited as "Cons: Alabaster: 1520-3: 231"). An Anthony Gurney standing executor to a Spelman esquire of the Ellingham orbit in 1524 — within G17 Anthony's adult lifetime and at his wife's manor — is a personal Gurney–Spelman bond a full century before the antiquary Sir Henry Spelman held the manuscript Gurney pedigree (lead L-5), and complements the Lovell–Conyers–Spelman cousinage below.[^spilman-1524]
```

with:

```
- **1524 — Antony Gurney executor to Henry Spilman, Esq., of Great Ellingham.** The registered will was image-read in full (expert paleography, packet 12): "I Henry Spilman esquier … the xvij daie of February [1523/4] … my body to be buried in the chirch yarde of Saynte James in Ellyngham," with wife **Elizabeth** taking his movables (cattle, plate, corn in the barn, the year's sown crop) and a life interest in his lands, manors, and freehold (to be sold by the executors after her death), a 100-mark marriage portion to one Frances, twenty-shilling legacies through a local network (Brampton, Newman, Golding, Pyott, Stykes, and others), and executors **"my wyffe, Antony Gurney, and John Turrell,"** each given 20s and a black gown; **proved at Norwich, April 1524**. The "Antony Gurney" reading is secure; no relationship or style is attached to him in the legible text. Crucially, **the will names no children** — consistent with this being the Henry Spelman/Spilman of "Mickle Elyngham" who died without issue and through whose death (Blomefield dates it 1525) Great Ellingham passed to the Lovells and so, by Anthony's marriage to Margaret Lovell, to the Gurneys. On that reading **Anthony Gurney executed the will of the very man from whom his family inherited Great Ellingham** — a personal Gurney–Spelman bond a century before the antiquary Sir Henry Spelman held the manuscript Gurney pedigree (lead L-5), and the documentary join between the executor role and the inheritance. (The 1524-proved vs Blomefield's 1525 date, and the absence of a stated kinship between Henry Spilman and Antony Gurney, are the remaining open points.) Full transcription: [`sources/corpus_supplement/paleo-2026-06-packet-12-henry-spillman-great-ellingham-will.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/paleo-2026-06-packet-12-henry-spillman-great-ellingham-will.md). The typescript abstract that first flagged the lead reads "HENRY SPILLMAN, Esquier … my wif, Antony Gurney and John Turrell, executors. D: 17 Feb — P. 1524" (register "Cons: Alabaster: 1520-3: 231").[^spilman-1524]
```

## Item 04 (promote) — G15 companion: Henry's succession as a minor heir under the trust

**Target:** `research/people/g15-henry-gurney-fact-sheet.research.md`

**Operation — str_replace.** Replace:

```
## Working Notes

### 2026-06-11 — Henry's last will: made 1 May 1621, proved 23 October 1623 — the death date moves to 1621×1623
```

with:

```
## Working Notes

### Henry's succession — a minor heir under his grandfather's fourteen-year trust (lead L-112)

Henry inherited West Barsham and Great Ellingham not from his father but from his grandfather **Anthony G17**, because his father **Francis (G16) had predeceased** Anthony. Anthony's will (made 6 Dec., proved 10 Dec. 1557) set up a **fourteen-year executor trust** over two-thirds of the knight-service manors; running from December 1557 it ended in **1571**, the year Henry (b. 21 Jan 1548/9) turned 21 and could take livery. This resolves Blomefield's otherwise impossible statement that Anthony "died January 4, 1555, leaving Henry, his grandson and heir, **aged twenty-one years**" (Henry was ~9 in 1557): the "aged twenty-one" is Henry's **livery age, c. 1570**, telescoped by Blomefield onto the (also mis-dated) death. As grandson-and-heir Henry took the descended third by law and so is unnamed in the will's legacies — the five Gurney grandchildren it funds are his own siblings (children of Francis G16). See the [G17](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g17-anthony-gurney-fact-sheet.research.md) and [G16](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g16-francis-gurney-fact-sheet.research.md) companions.

### 2026-06-11 — Henry's last will: made 1 May 1621, proved 23 October 1623 — the death date moves to 1621×1623
```

## Item 05 (promote) — west-barsham.md: Edmund G23 folio correction and lost-leaf provenance (L-34)

**Target:** `research/places/west-barsham.md`

**Operation 05a — str_replace.** Replace:

```
Edmund Gournay (G23) is the true founder of West Barsham as the family's central residence. His will, dated in **1387** and preserved in **Reg. Harsyke, fol. 34**, was made at West Barsham and directed burial in the **church of the Assumption of the Blessed Virgin** there, with a bequest of **£8 to the poor on his burial day**. DG-II also preserves the names of his executors, **Osbert de Mundeford** and **Thomas Kemp**. [DG-II] [Edmund G23 companion]
```

with:

```
Edmund Gournay (G23) is the true founder of West Barsham as the family's central residence. His will, made at West Barsham on Thursday the feast of the Ascension **1387** and registered in **Reg. Harsyke, fol. 84** (Norwich Consistory Court; Norfolk Record Society vol. 16, A–Hi — Daniel Gurney's "fol. 34" is a misprint), directed burial in the **church of the Assumption of the Blessed Virgin** there, with **£8 to the poor on his burial day**, a funeral feast for the gentry and country folk, and bequests to the high altar and the repair of the church. His executors were his wife **Katherine (de Wauncy)**, his son **John**, **Osbert de Mundeford**, and **Thomas Kempe**. The register leaf is now lost — "in the time of Mr. Norris [d. 1786] the part of the register which contained it was utterly rotted and destroyed" (Daniel Gurney, *Record* II, p. 363) — so the text survives only through Sir Simonds Dewes's 1637 copy (DG-Supplement Note 118) and Blomefield; no microfilm can reproduce it. [DG-II] [Edmund G23 companion]
```

**Operation 05b — str_replace.** Replace:

```
- Reg. Harsyke, fol. 34 (Edmund Gournay's 1387 will), cited by DG-II. [DG-II]
```

with:

```
- Reg. Harsyke, fol. 84 (Edmund Gournay's 1387 will; folio now lost, text via the Dewes 1637 copy and Blomefield). Daniel Gurney cites it as "fol. 34," a misprint. [DG-II]
```

## Item 06 (promote) — data/ancestors.json: G17 Spilman-executor enrichment

**Target:** `data/ancestors.json`, record `ancestor-g17-anthony-gurney` (the `notables` string)

**Operation — str_replace.** Replace:

```
The marriage brought into the Gurneys the manor of Great Ellingham, after Henry Spelman the elder of \"Mickle Elyngham\" died without issue in 1525 (Blomefield, vol. i).
```

with:

```
The marriage brought Great Ellingham into the Gurneys, after Henry Spelman the elder of \"Mickle Elyngham\" died without issue c. 1525 (Blomefield, vol. i), whose 1524 will named Anthony Gurney an executor.
```

*Phase-2 check:* confirm `data/ancestors.json` still parses (`python -c "import json;json.load(open('data/ancestors.json',encoding='utf-8'))"`); regenerate `data/indexes/` per `data-json.md` if the freshness check flags drift.

## Item 07 (promote) — paleography packet 12 disposition

Per the disposition convention in `.claude/skills/familysearch-fulltext-research/SKILL.md` §4. Execute as literal file operations:

1. **Copy** `sources/intake/paleography-staging/packet-12-henry-spillman-great-ellingham-will.md` → `sources/corpus_supplement/paleo-2026-06-packet-12-henry-spillman-great-ellingham-will.md` (verbatim; this is the durable transcription the G17 companion footnote points to).
2. **Move** the two master images from `sources/intake/paleography-staging/images/` into the existing `sources/media/ncc-wills-registers/_local/`: `ncc-wills-1520-1524-img379-spilman-will.jpg` and `ncc-wills-1520-1524-img380-spilman-will.jpg`.
3. **Append** to `sources/media/ncc-wills-registers/_local/README.md` (or the folder's committed `README.md`) two rows:

```
| ncc-wills-1520-1524-img379-spilman-will.jpg | NCC regd. wills vol. 36 (1520–24, Reg. Alabaster, DGS 008076282) | 379 | 3:1:3Q9M-CSN8-T9QC-H | Henry Spilman will (Antony Gurney executor), opening |
| ncc-wills-1520-1524-img380-spilman-will.jpg | same | 380 | 3:1:3Q9M-CSN8-T93B-3 | Spilman will, probate (April 1524) |
```

4. **Move** the packet-12 working crops (`sources/intake/paleography-staging/working-snippets/packet-12-henry-spillman-will/`) → `sources/media/_local/paleo-2026-06-batch2-working-crops/` (derivative, regenerable).
5. The orphaned calibration/QA images may be dropped: `sources/intake/paleography-staging/images/_subagent-harsyk-img*.jpg` (Harsyk fol.-7–35 overviews, superseded — the will leaf is lost), `ncc-wills-harsyk-img037.jpg`, `ncc-wills-harsyk-img064.jpg`, `ncc-wills-1548-1550-img619-gurney-candidate.jpg` (a Freeman will, not a Gurney — false positive), and the `_crop*.jpg` targeting crops. None is referenced durably.
6. **Move** the staging README to `sources/intake/done/paleography-2026-06-batch2/` if not already moved with the v90 batch; then grep `paleography-staging` across the repo and fix any lingering references to moved files.

## Item 08 (promote) — confirm the L-101 lead text lands durably

The packet-12 transcription (Item 07.1) is the durable home for the Spilman will; the G17 companion (Item 03) carries the finding and the footnote pointer. No separate corpus file or sourceId is required (sourceId `familysearch-fulltext-search`; the abstract-volume citation in the existing `[^spilman-1524]` footnote is unchanged).

---

## Phase-2 sequencing note

Apply items 01 → 07 in order; Item 07 (file moves) last, after every reference to the staging paths is in final form. Item 06 touches `data/ancestors.json` — validate parse and regenerate indexes after. After application, prepend the Done stamp and move this patchset to `sources/intake/done/`.
