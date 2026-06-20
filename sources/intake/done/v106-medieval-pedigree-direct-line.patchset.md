**Done:** 2026-06-20 20:29 PT

# Patchset v106 — Medieval & pedigree direct line (soldier database, L'Estrange→William Gurney, 1463 Great Melton feoffment, Thomas Gurney III death)

Bundles the medieval/pedigree findings of the 2026-06-18→20 discovery arc. Companion patchset **v107** carries the emigrant-John / G14-family findings from the same arc. Net-new raw source extracts were written directly to `sources/corpus_supplement/` during the arc (per maintainer instruction): `rye-norwich-free-library-calendar-gurnay-extracts.md` (used by Item 3 below), plus `rollco-other-companies-gurney-1573-1653.md` and `maldon-borough-court-gournay-fts-1630-1706.md` (used by v107).

Lead-CSV updates for L-72, L-73, L-113, L-119, L-122, L-154 were already applied via `tools/research_leads.py` during the arc and are not repeated here.

---

## Item 1 — promote: Medieval Soldier database sweep (Richard esq. 1387 confirmed; new John Gurnay archer 1385; 1388 record absent)

**Destination:** `research/topics/gurney-medieval-soldier-database.md` (leads L-72, L-73, L-154).

**Finding.** A live sweep of the *Soldier in Later Medieval England* database (medievalsoldier.org), 2026-06-20, across the Gurney/Gurnay/Gournay spellings, confirmed the Richard-esquire index row exactly and surfaced one record not previously in this companion: **John Gurnay, archer, naval expedition, 30 April 1385, in the retinue of Thomas Percy, earl of Worcester (TNA E101/40/39 m2)** — a second Gurney in royal naval service the same decade as Richard esquire's 1387 service. The database returned **only the 1387 Richard record**, not a 1388 one, so the lead's second citation (E101/41/5 m5, 1388) needs verifying against the original membrane. Richard's full index data: esquire, man-at-arms, naval (expedition), captain **Edward Courtenay, earl of Devon**, commander **Richard FitzAlan, earl of Arundel**, 13 March 1387, E101/40/34 m1i. The Robert-archer 1415 row (E101/45/1 m14, Henry V) was also corroborated exactly.

**Action 1a — str_replace (update the Richard row):**

old_string:
```
| **Richard Gurney, esquire** (1387/88; E101/40/34, E101/41/5) | Unplaced in *both* the Norfolk and Somerset pedigrees; served under Arundel, the family's patron[^msd] | **Open — priority.** Gentry rank, right generation/affinity; if Daniel Gurney's hedged "Robert" for G22 is wrong, a Richard is conceivable. Needs the 1387/88 muster membrane (L-72). |
```

new_string:
```
| **Richard Gurney, esquire** (1387; E101/40/34 m1) | Unplaced in *both* the Norfolk and Somerset pedigrees; served under Arundel, the family's patron[^msd] | **Open — low priority.** Index data confirmed 2026-06-20: man-at-arms, naval expedition, 13 March 1387, captain Edward Courtenay earl of Devon, commander Richard FitzAlan earl of Arundel. Gentry rank, right generation/affinity; if Daniel Gurney's hedged "Robert" for G22 is wrong, a Richard is conceivable. The database carries only this 1387 record (no 1388 entry under any Gurney spelling), so the formerly-paired E101/41/5 m5 (1388) is treated as a stray citation, not a second record — the indexed data is trusted, no membrane re-verification pursued. The membrane-neighbour read (L-72) is held at **low priority**. |
| **John Gurnay, archer** (1385; E101/40/39 m2) | Naval expedition, retinue of Thomas Percy earl of Worcester[^msd] | **Comparator only — low priority.** Surfaced 2026-06-20. An *archer*, not a man-at-arms — a rank a direct-line gentry Gurney would not have held — so this is a same-name comparator, not a direct-line candidate (L-154, low priority). |
```

**Action 1b — str_replace (add a dated sweep note after the candidate-cohort table's summary paragraph):**

old_string:
```
Several of the workbook's louder leads (the Somerset knights, the London mercer, the Essex John) are thereby **excluded** as non-Norfolk, narrowing the genuine "undocumented child/relative" field to the Richard esquire and the cadet Johns. None is yet an identification; each turns on a manuscript membrane, carried as a dated lead.
```

new_string:
```
Several of the workbook's louder leads (the Somerset knights, the London mercer, the Essex John) are thereby **excluded** as non-Norfolk, narrowing the genuine "undocumented child/relative" field to the Richard esquire and the cadet Johns. None is yet an identification; each turns on a manuscript membrane, carried as a dated lead.

A direct re-query of the database (2026-06-20) confirmed the index data above. It also showed the database carries only the 1387 Richard record (no 1388 entry), and that the one genuinely new sighting — a 1385 John Gurnay — is an *archer*, a rank outside the direct line's gentry status. The earlier soldier-database review (which found no unusually-variant Gurney spellings) remains the controlling treatment and the indexed data is trusted; the AALT muster membranes would at most site these unplaced same-name men Norfolk-vs-West-Country, a marginal gain, so L-72/L-73/L-74/L-154 are held as **low-priority** leads, not an active step.[^msd]
```

---

## Item 2 — promote: L'Estrange "sister Gurnay" resolved to Ann (Heydon) Gurney, wife of William Gurney Esq. (G18)

**Destination:** `research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md` (lead L-122).

**Finding.** Blomefield's Heydon pedigree of Baconsthorp (vol. 6) reads, of Sir Henry Heydon's five daughters: Amy m. Sir Roger le Strange of Hunstanton; Dorothy m. Sir Thomas Brook; Elizabeth m. Walter Hobart; **"Ann to William Gurney, Esq."**; Bridget m. Sir William Paston. The "sister Gurnay" named in Sir Roger L'Estrange's 1505 will is therefore his **sister-in-law Ann (Heydon) Gurney**, wife of William Gurney Esq. (the repo's G18 William Gurney V, already recorded as married to Anne Heydon) — not an independent third Gurney marriage. The L'Estrange forename gap thus resolves to **William** via the Heydon sisterhood, consistent with the Calthorpe son-in-law also being a William (G19). This is a substantive genealogical claim traced to its authority (Blomefield, citing the Heydon pedigree), per the citation rule's trace-to-authority requirement.

**Action 2a — str_replace (close the "forename unresolved" framing):**

old_string:
```
Both abstracts give the Gurney **surname only**, so the husband's forename is unresolved. The two marriages sit in the documented Gurney–Heydon–Calthorpe–L'Estrange–Townshend–Lovell cousinage that the G17 line's Lovell/Spelman/Conyers connections already run through; whether the Calthorpe and L'Estrange husbands are West Barsham direct-line Gurneys (G18 William Gurney V is here recorded married to Anne Heydon), their brothers, or near collaterals is the open question. Pulling the two full wills for the forenames is the resolving step (lead L-122).[^calthorpe-1494][^lestrange-1505]
```

new_string:
```
Both abstracts give the Gurney **surname only**. The L'Estrange "sister Gurnay" is now resolved without the will image: Blomefield's Heydon pedigree of Baconsthorp names Sir Henry Heydon's five daughters and their husbands — Amy m. Sir Roger le Strange of Hunstanton, Dorothy m. Sir Thomas Brook, Elizabeth m. Walter Hobart, **"Ann to William Gurney, Esq.,"** Bridget m. Sir William Paston. Sir Roger L'Estrange's "sister Gurnay" (1505) is therefore his **sister-in-law Ann (Heydon) Gurney, wife of William Gurney Esq.** — the repo's G18 William Gurney V, already recorded married to Anne Heydon — viewed from the L'Estrange side, not an independent third marriage. Both the Calthorpe son-in-law (by inference, G19) and the L'Estrange "sister Gurnay" husband are thus **William** Gurney, embedding the West Barsham line in the Gurney–Heydon–Calthorpe–L'Estrange–Townshend–Lovell cousinage the G17 Lovell/Spelman/Conyers connections already run through. The Calthorpe will's literal forename still awaits its PCC image; the L'Estrange side is resolved.[^calthorpe-1494][^lestrange-1505][^heydon-baconsthorp-g18]
```

**Action 2b — new file write:** `sources/corpus_supplement/blomefield-baconsthorp-heydon-pedigree-gurney.md` is **not** required — the Heydon-pedigree quotation is a single short clause cited inline; recorded in the new footnote (Action 2c). (Skip justified per the corpus-extract threshold: the relevant extract is well under ~150 words.)

**Action 2c — str_replace (add the supporting footnote at the file's footnote block).** Append, after the existing `[^lestrange-1505]:` footnote, a new footnote:

new footnote text:
```
[^heydon-baconsthorp-g18]: Francis Blomefield, "Hundred of South Erpingham: Baconsthorp," *An Essay Towards a Topographical History of the County of Norfolk*, vol. 6, pp. 502–513, British History Online, https://www.british-history.ac.uk/topographical-hist-norfolk/vol6/pp502-513 — the Heydon pedigree, listing the five daughters of Sir Henry Heydon (d. 1503/4) by Anne Boleyn: "Amy" m. Sir Roger le Strange of Hunstanton, "Dorothy" m. Sir Thomas Brook, "Elizabeth" m. Walter Hobart, "Ann to William Gurney, Esq.," "Bridget" m. Sir William Paston. This identifies the "sister Gurnay" of Sir Roger L'Estrange's 1505 will as his sister-in-law Ann (Heydon) Gurney, wife of William Gurney Esq. (G18 William Gurney V). Source ID: `blomefield-norfolk`.
```

(Phase 2: place this footnote definition in the file's footnote section, adjacent to `[^lestrange-1505]`.)

---

## Item 3 — promote: 1463 Great Melton feoffment — earliest documented Gurnay–Calthorpe co-feoffment

**Destination:** `research/people/g19-william-gurney-iv-fact-sheet.research.md` (lead L-119), into the "1505 trust feoffees as a closed kinship-and-affinity circle" section as the earliest instance of the same relationship.

**Finding.** Walter Rye's calendar of the Norwich Free Library MSS (FamilySearch DGS 004389182; extract at `sources/corpus_supplement/rye-norwich-free-library-calendar-gurnay-extracts.md`) abstracts a **1463 feoffment of land in Argerysthorp field, Great Melton, Norfolk**, enfeoffing **Sir William Calthorp, William Gurnay, Thomas Bachecroft, John Wyndham and Simeon Bachecroft** (quitclaim of Robert Breton). A William Gurnay co-feoffing with Sir William Calthorpe (knight of the Bath, d. 1494 — the father of William IV's wife Anne Calthorpe) and John Wyndham in 1463 pre-dates the 1505 Gurnay–Calthorpe trust feoffment by ~42 years, making it the earliest documented node of the Gurney–Calthorpe feoffee relationship.

**Action 3a — str_replace (append the 1463 feoffment after the closed-circle summary):**

old_string:
```
This is a closed Calthorpe-Howard-Drury kinship-and-affinity circle — the inner social world into which William IV's marriage to Anne Calthorpe had embedded the West Barsham line.
```

new_string:
```
This is a closed Calthorpe-Howard-Drury kinship-and-affinity circle — the inner social world into which William IV's marriage to Anne Calthorpe had embedded the West Barsham line.

The Gurney–Calthorpe feoffee relationship is documented earlier still. A 1463 feoffment of land in Argerysthorp field, Great Melton, Norfolk — calendared in Walter Rye's catalogue of the Norwich Free Library MSS — enfeoffs **Sir William Calthorp, William Gurnay, Thomas Bachecroft, John Wyndham and Simeon Bachecroft** (with a quitclaim of Robert Breton). A William Gurnay (elsewhere in the calendar's index styled "Sir William Gurnay") thus co-feoffing with Sir William Calthorpe — knight of the Bath (d. 1494), father of William IV's wife Anne Calthorpe — and John Wyndham in 1463 places the two families in a shared trustee circle about forty years before the 1505 settlement, the earliest documented instance of the relationship that William IV's marriage later consolidated.[^melton-1463-feoffment]
```

**Action 3b — str_replace (add the footnote).** Append a new footnote to the file's footnote block:

new footnote text:
```
[^melton-1463-feoffment]: 1463 feoffment of 4 acres in Argerysthorp field, Great Melton, Norfolk (formerly of Thomas Chapeleyn), from Thomas Jermyn and Simon Bavet to Sir William Calthorp, William Gurnay, Thomas Bachecroft, John Wyndham and Simeon Bachecroft, with quitclaim of Robert Breton; abstracted in Walter Rye's *Calendar of the Topographical and Genealogical Books and MSS. in the Free Library at Norwich*, digitised as FamilySearch image group DGS 004389182, ark `3:1:S3HY-6DQ9-C91` (FamilySearch Full-Text Search, 2026-06-20). Calendar/abstract level; the original deed has not been examined. Full extract: `sources/corpus_supplement/rye-norwich-free-library-calendar-gurnay-extracts.md`. Source ID: `familysearch-fulltext-search`.
```

---

## Item 4 — promote: Thomas Gurney III died 1621×1623 vita patris (the "1614" is the date of Henry G15's revoked earlier will)

**Destination:** `research/people/g15-henry-gurney-fact-sheet.research.md` (lead L-113), resolving the conflict the companion itself flagged for tracing.

**Finding.** The conflict the companion flagged ("the 1614 tradition should be traced to its root, Daniel Gurney p. 287 / Pease") is resolved. Daniel Gurney's *Record* p. 283 (the narrative descent) says only that Henry G15 "died in 1623, and was succeeded… by Edward Gournay his grandson, **Thomas Gourney, his eldest son, having died in his life-time**" — giving **no death year** for Thomas. The "p. 287" the conflict cites is a *different* Thomas: DG's pedigree p. 287 entry is "Thomas Gurnet," William IV's (G19) son, ancestor of the Gurneys of Dartmouth/London/Essex (see the G19 companion). With Henry's 1 May 1621 will bequeathing to "my eldest sonne Thomas" (alive), **Thomas III (m. Martha Lewknor of Denham) died 1621×1623, vita patris**, and his son Edward succeeded Henry in 1623. The "1614" is the date of Henry's revoked earlier will, mis-transmitted by later genealogists as Thomas's death year. (The actual West Barsham burial date is not FamilySearch-indexed — the FMP Norfolk Burials set omits West Barsham — so the precise date awaits the West Barsham register image.)

**Action 4a — str_replace (rewrite the Thomas conflict from "not resolved" to resolved; preserve the Anthony conflict and the footnote):**

old_string:
```
**Two conflicts exposed (not resolved).** (1) **Thomas:** the family genealogies say the eldest son Thomas III died in 1614, *vita patris*; the 1621 will bequeaths to "my eldest sonne Thomas." Either Thomas was alive in May 1621 (and died 1621×1623, still before his father) and the 1614 date is wrong — possibly a confusion with the 1614 *will* — or the registered text carries a recital from the earlier will. The will is primary and the bequest reading is high-confidence; the 1614 tradition should be traced to its root (Daniel Gurney p. 287 / Pease) before the fact sheets pick a Thomas death year. (2) **Anthony:** the fact sheet carried Anthony (Francis's twin, b. 1581) as died *vita patris*; the probate clause shows him alive, administering, on 23 October 1623. The *vita-patris* claim is superseded.[^henry-will-conflicts]
```

new_string:
```
**Two conflicts, both now resolved.** (1) **Thomas:** the family genealogies say the eldest son Thomas III died in 1614, *vita patris*; the 1 May 1621 will bequeaths to "my eldest sonne Thomas," so Thomas was alive in May 1621 and **died 1621×1623, still before his father**. The "1614" is the date of Henry's revoked *earlier* will, mis-transmitted by later compilers as a death year. Tracing the 1614 claim to its root confirms this: Daniel Gurney's *Record* p. 283 (the narrative descent) says only that Henry "died in 1623, and was succeeded… by Edward Gournay his grandson, *Thomas Gourney, his eldest son, having died in his life-time*" — giving **no year** for Thomas; and the "p. 287" pedigree entry that the death-claim is sometimes hung on is a *different* Thomas, namely "Thomas Gurnet," William IV's (G19) son and ancestor of the Gurneys of Dartmouth/London/Essex (see the [G19 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g19-william-gurney-iv-fact-sheet.research.md)). So no source places Thomas III's death in 1614; he died 1621×1623, and his son Edward succeeded Henry in 1623. The precise West Barsham burial date is not FamilySearch-indexed (the FMP Norfolk Burials set omits West Barsham), so it awaits the register image. (2) **Anthony:** the fact sheet carried Anthony (Francis's twin, b. 1581) as died *vita patris*; the probate clause shows him alive, administering, on 23 October 1623. The *vita-patris* claim is superseded.[^henry-will-conflicts]
```

---

## Source tracking

- `medievalsoldier-database` — exists (`data/indexes/source-ids.csv`); Item 1 cites it via the file's existing `[^msd]` footnote. No new validation needed (validation already present for the soldier-database source set).
- `blomefield-norfolk` — exists; Item 2 cites the Baconsthorp Heydon pedigree under it (validation already exists for `blomefield-norfolk`).
- `familysearch-fulltext-search` — exists (catch-all for FTS image reads); Items 1 and 3 cite under it. Validation `sources/validations/familysearch-fulltext-search.md` already exists.
- No new `sourceId` is minted in this patchset; the Rye-calendar extract used by Item 3 is held under the FTS catch-all, with the discrete-document identity recorded in the corpus_supplement file rather than as a separate sourceId (the calendar's exact published title/editor is recorded there as Walter Rye's Norwich Free Library catalogue, attribution stated but not yet confirmed against a title page).

## Citation-rule note (per maintainer request to flag tension)

The current `citations.md` adds (a) "**Show every aligned source, not just one**" for 3+-source facts, and (b) a "**contextual colour vs. substantive claim**" band for tertiary sources. No tension here: Item 2's L'Estrange→William resolution is a *substantive* claim and is cited to its authority (Blomefield's Heydon pedigree), not left on the WikiTree/Geni collectors the prior text leaned on; the collectors are retained only as corroborating cross-references. Item 3's 1463 feoffment is cited at calendar/abstract level with that limitation stated. Flagged for review: the soldier-database rows cite a single `[^msd]` workbook footnote covering many witnesses — acceptable as a per-row finding aid, but if any row is promoted to a fact sheet it should carry the specific TNA membrane citation, not the omnibus `[^msd]`.
