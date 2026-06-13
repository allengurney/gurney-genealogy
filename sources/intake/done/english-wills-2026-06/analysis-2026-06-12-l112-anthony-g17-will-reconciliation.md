# L-112 — reconciling Anthony G17's 1557 will with Blomefield and the pedigree

Analysis only (no new source pulls); reasons over the already-captured Anthony G17 will (1557), the new Henry G15 will (1621, packet 10), Blomefield, and the Visitation pedigree. Destined for the **G17 companion** (primary), with consequences flagged for the **G16 and G15** companions and `data/ancestors.json`. To be folded into patchset v91.

## The keystone: the fourteen-year trust dissolves all three puzzles together

Anthony G17's will (made 6 Dec, proved 10 Dec 1557) sets up a **fourteen-year executor trust** over two-thirds of his knight-service manors and all his socage lands, the income to pay debts and legacies and fund "the educacion and bringing upp of" six named grandchildren, with the overplus divided at the term's end among those then living. A fourteen-year trust from December 1557 ends in **1571**. Read against the secure birth of the heir Henry G15 — 21 January 1548/9, from his own commonplace book — Henry turns 21 in 1569/70, i.e. **the trust is a minority-management (wardship) vehicle timed to expire exactly as the heir comes of age and takes livery.** Once that is seen, the three "conflicts" the will appeared to raise resolve as facets of one coherent settlement.

## 1. Death date — the will is primary; Blomefield is garbled, not merely wrong

A will proved 10 December 1557 means Anthony died c. 6–10 December 1557 (the four-day gap reads as a deathbed will). Blomefield (vol. vii) gives "died January 4, 1555, leaving Henry, his grandson and heir, aged twenty-one years" — wrong on the date by ~2 years and, taken literally, impossible on the age (Henry, b. 1548/9, was ~9 in 1557, not 21). **Both errors are explained by a single telescoping:** Blomefield's source was almost certainly a livery/proof-of-age record from c. 1569–71 (when Henry, the ward, proved his age at 21 and took the estate as the trust ended), and Blomefield collapsed *death → minority → livery* into one sentence, mis-dating the death and attaching the livery age ("aged twenty-one") to it. The fourteen-year trust (to 1571 ≈ Henry's majority) corroborates this independently. **Resolution: Anthony G17 died early December 1557.** The "aged 21" is the heir's age at livery c. 1570, not at the grandfather's death.

(Note the discarded project-JSON reading "December 1556" was closest in *shape* — a December death in the mid-1550s — though a year early.)

## 2. The absent son Francis G16 — the will confirms he predeceased

The will names no wife and no living son. The pedigree's only son of Anthony is **Francis (G16)** of West Barsham, m. Ellen Holdich, father of Henry G15. The fact sheet already infers Francis G16 died *vita patris* before 1556; the will now **corroborates that inference at primary level** — a living eldest son would ordinarily head the dispositions, so his total absence places his death before December 1557. The whole-estate trust for minor grandchildren is exactly the structure a testator adopts when the next generation (his son) is already dead and the heirs are children. **Resolution: Francis G16 died before December 1557, in his father's lifetime — now will-corroborated, not merely traditional.**

## 3. The absent heir Henry G15 — omitted *because* he is the heir-at-law

Henry G15 is missing from the six named grandchildren — and that is the expected pattern, not an anomaly. The will's beneficiaries are precisely those who do **not** take the real estate: two unmarried/younger daughters (cash portions, below) and six grandchildren (education trust + overplus). The lands themselves, after the fourteen-year trust, revert to the heir **by entail/descent** and so require no legacy clause — which is why the heir is unnamed. As grandson-and-heir through the predeceased eldest son Francis, **Henry took the entailed manors automatically; an heir taking real property by descent is routinely given no personal bequest.** The trust is the management vehicle for that ~9-year-old heir's minority. His omission from the legacy list is therefore positive evidence that he *was* the heir, consistent with Blomefield and the Visitation, not evidence against the pedigree.

### The six grandchildren are most economically Henry's siblings (children of Francis G16)

Five are Gurney-surnamed — **Anthony, Thomas, Elizabeth, ffrannces, and Anne Gurney** — i.e. children of a son; the only son in the pedigree is Francis G16, so these read as **Henry G15's younger siblings**. The sixth, **Anthony Drurye**, is surnamed Drury — a child of a daughter of Anthony G17 who married a Drury. On this reading Francis G16 had at least six children (Henry the heir + Anthony, Thomas, Elizabeth, ffrances, Anne) — a materially fuller G16 family than the repo currently records, which gives essentially only Henry.

Two independent supports raise this from possible to probable:
- **Naming echo in Henry's own 1621 will.** Henry G15 named his children **Anthony, Thomas, Elizabeth, Anne** (alongside Francis, Edward, Henry, Abigail) — the same cluster as the 1557 grandchildren. A man naming his children after his grandfather (Anthony G17) and his own siblings is exactly what the sibling hypothesis predicts; the repetition is corroborating, not coincidental.
- **The "ffrannces Gurney" puzzle dissolves.** Whether normalized Francis or Frances, the will fixes this person in the *grandchild* generation, so it is **not** Francis G16 — removing any temptation to read the will as naming the son Francis. A grandson Francis (named for his father G16) would be ordinary practice.

**Testable prediction for verification:** the Visitation of Norfolk (Harleian Soc. 32, p. 141) entry for Francis G16 should list children matching some of Anthony/Thomas/Elizabeth/ffrances/Anne alongside Henry. This cross-check was not run here (the G15-companion visitation note recorded Henry's *own* children, not Francis's siblings-set) and is the single highest-value confirmation step — Available online (Internet Archive `visitacionievisi32ryew`).

## New family members from the will (G17's own children)

The will yields two daughters of Anthony G17 not in the current fact sheet: **Elizabeth Gurney** (£200 — a full marriage portion, so probably unmarried in 1557) and **Cicely Gurney** (£20 — a token, so probably already married/settled). They are Henry G15's aunts. A daughter of Anthony also married a **Drury** (mother of the grandchild Anthony Drurye). So Anthony G17's children now stand as: Francis (G16, predeceased), Elizabeth, Cicely, and at least one further daughter (Mrs Drury).

## Confidence and consequences

- December 1557 death: **high (~90%)** — primary will vs a secondary topographer.
- Francis G16 predeceased (before Dec 1557): **high (~85%)** — will-corroborated inference.
- Henry omitted as heir-at-law: **high (~85%)** — standard testamentary pattern + the minority-trust fit.
- Six grandchildren = Francis G16's children (Henry's siblings): **probable (~70%)** — pending the Visitation cross-check.

**Fact-sheet / data consequences to carry in the patchset:**
1. **G17 fact sheet + `ancestors.json`:** death date → early December 1557 (will-proved 10 Dec 1557), superseding Blomefield's 4 Jan 1555/6 and the JSON's "December 1556"; add daughters Elizabeth and Cicely (and the unnamed Drury-married daughter); reframe Blomefield's "aged 21 at succession" as the heir's livery age c. 1570 (the 14-year trust to 1571).
2. **G16 fact sheet/companion:** Francis G16's death is now will-corroborated as before December 1557 (*vita patris*); flag the probable expanded child-set (Henry + five siblings) pending the Visitation cross-check — do not promote the sibling names to confirmed until that check is run.
3. **G15 fact sheet/companion:** Henry's succession reframed — minor heir under a wardship trust 1557–1571, livery at 21 c. 1570; resolves the long-standing internal inconsistency where Blomefield's "aged 21 at his grandfather's death" contradicted Henry's 1548/9 birth.
4. **Remaining open:** run the Visitation cross-check on Francis G16's children (closes consequence 2); identify Robert Notary, esquire (co-executor); the £200/£20 daughters' later marriages.
