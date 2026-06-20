**Done:** 2026-06-19 10:47 PT

# Patchset v102 — online lead-discovery arc (heraldic, medieval, colonial)

Phase-1 patchset bundling the promotable findings of the June 2026 multi-turn online research
arc across the priority research-leads catalog (FamilySearch Full-Text + FindMyPast + Ancestry +
British History Online + Internet Archive sessions). Each item is a literal operation for Phase-2
mechanical application.

Written **directly to the repo during research** (not actions here — recorded for traceability):
- **Corpus supplements** (`sources/corpus_supplement/`): `blomefield-norfolk-vol5-pp63-70-newton-flotman.md` (new) and `suffolk-deeds-liber-xii-gurnell-dorchester.md` (new).
- **Leads** (`research/future-research/research-leads.csv` via `tools/research_leads.py`): updated L-8, L-28, L-69, L-70, L-93, L-94, L-99, L-109, L-119, L-122, L-129, L-130, L-134, L-148; added **L-152** (Hempnall Gurney family) and **L-153** (Mattishall Burgh Francis Gurnay marriage).
- **Held:** L-145 (FTDNA Y-DNA scoping) at user direction — not promoted.

## Source tracking

Two new `sourceId`s are introduced; both get a `sources/validations/{sourceId}.md` write below. All other promotions reuse existing sources (`blomefield-norfolk`; `familysearch-fulltext-search`; `fs-england-marriages-1538-1973`; `fs-england-births-christenings`; `findmypast-norfolk-baptisms-index`).

- **`suffolk-deeds-liber-12-1902`** — *Suffolk Deeds, Liber XII* (Boston: Rockwell and Churchill, 1902), Internet Archive `suffolkdeeds11suff`. Parallels the existing `suffolk-deeds-liber-iv-1888`. Backs Item 4 and the new corpus supplement.
- **`paston-letters-davis`** — Norman Davis, ed., *Paston Letters and Papers of the Fifteenth Century* (Internet Archive `ThePastonLetters`). Distinct from the existing `paston-letters-gairdner`. Backs Item 3.

**Phase-2 sources.json action:** add both `sourceId` objects to `data/sources.json` following the schema of the sibling entry `suffolk-deeds-liber-iv-1888` (title; type as appropriate; validation path `sources/validations/{sourceId}.md`).

---

## Item 1 — PROMOTE: L-134 Newton Flotman monument resolves the Blundeville–Gurney marriage → `research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md`

**Finding.** Blomefield's transcription of the surviving St Mary, Newton Flotman chancel monument reads "Radulphus Blondevile obiit Ano Dni. 1514, Etatis sue 45" — Ralph (Radulphus) Blundeville died 1514 aged 45 (b. c. 1469), confirming Rye's "ob. 1514" and correcting the secondary "†1541, aged 74" reading; the husband is Ralph/Rafe, not "Robert." The Gurnay impalement is physically present on both the church battlements and the monument. Dates G19 to c. 1440–1490.

`str_replace` in `research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md`:

old_string:
```
- **Blundeville–Gurney date conflict.** The already-held marriage (Constance, dau. of William
  Gurney of West Barsham, m. Rafe/Radulphus Blundeville of Newton Flotman) carries a death-date
  conflict: the Newton Flotman St Mary monument dates Ralph **†1541, aged 74** (b. ~1467),
  versus the Visitation's "ob. 1514" — almost certainly a 1514↔1541 digit transposition, with
  the tomb (primary) favouring 1541. This dates Constance's father, William Gurney of West
  Barsham, to c. 1460–1500 (lead L-134).
```

new_string:
```
- **Blundeville–Gurney marriage, resolved.** Constance Gurney, daughter of William Gurney of
  West Barsham (G19), married **Ralph (Radulphus) Blundeville of Newton Flotman**. Blomefield's
  transcription of the surviving St Mary chancel monument reads *"Radulphus Blondevile obiit Ano
  Dni. 1514, Etatis sue 45"* — Ralph died **1514, aged 45** (b. c. 1469), confirming Rye's
  Visitation "ob. 1514" and correcting the secondary "†1541, aged 74" reading; the husband is
  **Ralph/Rafe**, not the "Robert" of some compiled pedigrees. The **Gurnay impalement** is
  physically present among the church battlement arms ("Blundeville impaling Gurnay") and on the
  monument itself ("Ditto [Blundeville] impales Gurnay"), pairing the marriage with Ralph among
  the three commemorated generations. This dates Constance's father, William Gurney of West
  Barsham, to c. 1440–1490. One internal conflict in Blomefield survives: his manor-descent
  prose calls Richard (d. 1503) and Ralph (d. 1514) **brothers**, while the monument verse
  styles the three men "the Grandsire, Father, and the Sone" (Richard → Ralph → Edward, three
  generations) — preserve both rather than reconcile by fiat.[^blomefield-newton-flotman]
```

Add the footnote definition. `str_replace` in the same file:

old_string:
```
[^rye]: William Hervey, Robert Cooke, and John Raven, *The Visitacion of Norffolk*, ed. Walter Rye (London: Harleian Society, 1891), pp. 132, 140–141. Corpus supplement: `sources/corpus_supplement/rye-visitacion-norffolk-1891-gurney-selected-pages.md`. Source ID: `rye-visitacion-norffolk-1891`.
```

new_string:
```
[^blomefield-newton-flotman]: Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. 5 (London, 1806), "Hundred of Humble-Yard: Newton," pp. 63–70 (British History Online); the Newton Flotman St Mary chancel monument inscription and the Blundeville battlement/monument arms incl. "impaling Gurnay." Verbatim extract at [`sources/corpus_supplement/blomefield-norfolk-vol5-pp63-70-newton-flotman.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/blomefield-norfolk-vol5-pp63-70-newton-flotman.md). Source ID: `blomefield-norfolk`.
[^rye]: William Hervey, Robert Cooke, and John Raven, *The Visitacion of Norffolk*, ed. Walter Rye (London: Harleian Society, 1891), pp. 132, 140–141. Corpus supplement: `sources/corpus_supplement/rye-visitacion-norffolk-1891-gurney-selected-pages.md`. Source ID: `rye-visitacion-norffolk-1891`.
```

---

## Item 2 — PROMOTE: L-122 Calthorpe/L'Estrange forename status → `research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md`

**Finding.** The FamilySearch-reachable abstracts of the 1494 Calthorpe and 1505 L'Estrange wills give the surname only ("Son Gurney"; "sister Gurnay"), no forename. The Calthorpe son-in-law is identified as G19 by inference (Anne Calthorpe = G19's wife, 8 sources) reinforced by the Paston/Davis evidence (Item 3); the literal forenames still need the PCC register images.

`str_replace` in `research/topics/gurney-heraldry-and-pedigree-evidence-g17-g28.md`:

old_string:
```
- **Calthorpe son-in-law (L-122).** Derivative compiled trees (WikiTree Calthorpe-7; Geni)
  name Sir William Calthorpe's daughter **Anne as the wife of a William Gurney** — i.e. the
  "Son Gurney" executor of the 1494 will. This is a hypothesis to test, not yet authority: the
  PCC will (PROB 11/10/408, reg. Vox fol. 23) or a Calthorpe Visitation pedigree must confirm
  the forename. If correct, the husband is most plausibly the **William Gurney of West Barsham
  active c. 1460–1500** who also fathered Constance (below) — i.e. G19 William Gurney IV's
  generation.
```

new_string:
```
- **Calthorpe son-in-law — identified as G19 by inference.** The FamilySearch-reachable
  abstracts of the 1494 Calthorpe and 1505 L'Estrange wills give the surname only ("Son Gurney …
  and my dr his wife"; "sister Gurnay") with **no forename**, so neither names the Gurney husband
  directly. The identification of the Calthorpe son-in-law as **William Gurney IV (G19)** rests on
  the eight independent Calthorpe-side sources making **Anne Calthorpe** G19's wife (see the
  [G19 companion](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g19-william-gurney-iv-fact-sheet.research.md)),
  reinforced by the Paston/Davis evidence placing G19 squarely in the Calthorpe–Howard–Norfolk
  magnate circle (escheator of Norfolk and Suffolk; retainer of the Duke of Norfolk). The literal
  forename in the Calthorpe will, and the forename of the Gurnay who married a L'Estrange sister
  by 1505, still require the **PCC register images** (PROB 11/10 reg. Vox fol. 23; reg. Adeane
  fol. 2), which are not in FamilySearch full-text. Derivative compiled trees (WikiTree
  Calthorpe-7; Geni) independently name the daughter Anne and her husband a William Gurney,
  consistent with the inference.[^calthorpe-1494]
```

---

## Item 3 — PROMOTE: L-28 Paston "Gurney of Tharston" = G19 → `research/people/g19-william-gurney-iv-fact-sheet.research.md`

**Finding.** Norman Davis's Paston edition identifies "William Gurney, esq., of Tharston" as escheator of Norfolk and Suffolk 1465–6, retainer of the Duke of Norfolk, on commissions 1484 and 1491, d. 1505 — the escheator office matching G19's 1466 Acle Paston IPM, fixing the identification and answering the standing "Council to Duke of Norfolk" question.

`str_replace` in `research/people/g19-william-gurney-iv-fact-sheet.research.md` (append a subsection after the Acle section):

old_string:
```
John Paston I was the husband of Margaret Paston (the most prolific letter-writer of the *Paston Letters*) and the central figure in the Paston-Heydon-Fastolf disputes of the 1460s. William IV's role in his IPM is therefore a high-prestige Norfolk gentry connection that the existing G19 fact-sheet Escheator highlight could be strengthened to surface, after a cross-check of the *Paston Letters* Gairdner edition (vol. IV/V) confirms no mention of William Gurney as escheator at the 1466 Paston inquisition. Deferred to a future patchset.
```

new_string:
```
John Paston I was the husband of Margaret Paston (the most prolific letter-writer of the *Paston Letters*) and the central figure in the Paston-Heydon-Fastolf disputes of the 1460s. William IV's role in his IPM is therefore a high-prestige Norfolk gentry connection that the existing G19 fact-sheet Escheator highlight could be strengthened to surface, after a cross-check of the *Paston Letters* Gairdner edition (vol. IV/V) confirms no mention of William Gurney as escheator at the 1466 Paston inquisition. Deferred to a future patchset.

### William Gurney of Tharston — the Paston correspondent identified as G19

The "William Gurney, esq., of Tharston" who appears in the Paston correspondence is **William Gurney IV himself**. Norman Davis's edition identifies him in an editorial note: *"William Gurney, esq., of Tharston, 5 miles west of Topcroft. He was a retainer of the Duke of Norfolk. He had been escheator of Norfolk and Suffolk 1465–6, served on commissions in 1484 and 1491, and died in 1505."* The escheator-of-Norfolk-1465/6 office is the same one under which G19 took the John Paston I inquisition at Acle in October 1466 (above), fixing the identification. The note adds three facts to G19's record: a **Tharston** seat (south Norfolk, near Topcroft); service as **escheator of Suffolk** as well as Norfolk; and — answering the standing "Council to the Duke of Norfolk" question — that he was a **retainer of the Duke of Norfolk**, the affinity behind both the Saxthorpe episode and the family's Yorkist alignment. One conflict to preserve: Davis dates his death **1505**, whereas his inquisition post mortem (Daniel Gurney *Supplement* Note 132) records death **16 February 1507/8** — the IPM is the primary record and is preferred, with Davis's 1505 noted as a secondary editorial date.[^davis-tharston-g19]

[^davis-tharston-g19]: Norman Davis, ed., *Paston Letters and Papers of the Fifteenth Century* (Internet Archive item `ThePastonLetters`, full text), editorial note: "William Gurney, esq., of Tharston, 5 miles west of Topcroft. He was a retainer of the Duke of Norfolk. He had been escheator of Norfolk and Suffolk 1465–6, served on commissions in 1484 and 1491, and died in 1505." The escheator-of-Norfolk-1465/6 office matches the 1466 Acle Paston IPM presided over by William Gurney IV (Daniel Gurney *Supplement* Note 129). Source ID: `paston-letters-davis`.
```

`str_replace` in the same file (resolve open question 2):

old_string:
```
2. **Council to Duke of Norfolk (1477):** The fact sheet mentions this. What is the source? DG-I or DG-Supp?
```

new_string:
```
2. **Council to / retainer of the Duke of Norfolk — resolved.** Norman Davis's Paston editorial note states William IV "was a retainer of the Duke of Norfolk" (see the Tharston subsection above), supplying the affinity source the fact-sheet line lacked.
```

---

## Item 4 — PROMOTE: L-99 Suffolk Deeds 1678–83 = Dorchester Gurnell, not the direct line → `research/people/g12-richard-gurney-fact-sheet.research.md`

**Finding.** Read against the printed *Suffolk Deeds, Liber XII* (1902), the 1678–83 deeds' only G-surname family is the distinct **Gurnell of Dorchester** (John Gurnell, tanner dec'd; executrix Jane; index Anne/George/John/Richard at pp. 84/200/256/308/309/310). No Elizabeth of the surname and nothing at p. 343 — the indexed "Elizabeth Gourney, 343" is a machine-transcript artifact; John³ Gurney and Elizabeth Green do not appear.

`str_replace` in `research/people/g12-richard-gurney-fact-sheet.research.md`:

old_string:
```
A supporting trace for the eldest son: the Suffolk County (Boston-registry) deeds volume for 1678–1683 indexes a deed of **John Gourney at p. 80** and one of **Elizabeth Gourney at p. 343** — the right window and names for Richard's son John and his wife Elizabeth Green. Page-level pulls are lead L-99.[^suffolk-deeds-1678-83-gourney]
```

new_string:
```
A FamilySearch full-text index of the 1678–1683 Suffolk County (Boston-registry) deeds had surfaced apparent "Gourney" entries (a John at p. 80, an Elizabeth at p. 343), raising the prospect of deeds by Richard's son John and his wife Elizabeth Green. Read against the printed *Suffolk Deeds, Liber XII* (1902), this resolves **negatively for the direct line**: the only G-surname family in the 1678–1683 deeds (Libers XI–XII) is the distinct **Gurnell family of Dorchester** — John Gurnell, tanner (deceased by 1682), and his widow and sole executrix **Jane Gurnell**, with index members **Anne, George, John, and Richard Gurnell** at Lib. XII pp. 84, 200, 256, 308, 309, 310. The printed indexes carry **no Elizabeth** of the surname and **nothing of it at p. 343**, so the indexed "Elizabeth Gourney, 343" is a FamilySearch machine-transcript artifact, not a genuine record; John³ Gurney and Elizabeth Green of Weymouth do **not** appear as parties in these deeds. (The Gurnell↔Gurney visual/OCR confusion is what generated the false "Gourney" index reading.) Verbatim extracts: [`sources/corpus_supplement/suffolk-deeds-liber-xii-gurnell-dorchester.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/suffolk-deeds-liber-xii-gurnell-dorchester.md).[^suffolk-deeds-1678-83-gourney]
```

`str_replace` in the same file (update the footnote):

old_string:
```
[^suffolk-deeds-1678-83-gourney]: Suffolk County, Massachusetts, Deeds 1678–1683, volume index entries "Gourney, John, 80" and "[Gourney,] Elizabeth, 343," located 2026-06-09 via FamilySearch Full-Text Search ("Gourney," 1600s bucket); deed pages not yet read. Source ID: `familysearch-fulltext-search`.
```

new_string:
```
[^suffolk-deeds-1678-83-gourney]: *Suffolk Deeds, Liber XII* (Boston: Rockwell and Churchill, 1902), the printed edition of the manuscript registry deed book covering c. 1681–1684 (Internet Archive `suffolkdeeds11suff`); the only G-surname presence is the Gurnell family of Dorchester (John Gurnell, tanner, dec'd; executrix Jane Gurnell; index Anne/George/John/Richard at pp. 84/200/256/308/309/310). No "Gourney"/"Gurney" and no Elizabeth of the surname appears; the earlier FamilySearch full-text index entries "Gourney, John, 80" / "Elizabeth, 343" (located 2026-06-09) are machine-transcript artifacts over this Gurnell material. Verbatim extract at [`sources/corpus_supplement/suffolk-deeds-liber-xii-gurnell-dorchester.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/suffolk-deeds-liber-xii-gurnell-dorchester.md). Source IDs: `suffolk-deeds-liber-12-1902`; `familysearch-fulltext-search`.
```

---

## Item 5 — PROMOTE: L-129 Podmer mother + L-130 Richard Rivet origin → `research/people/rivett-family-of-garveston.md`

**Finding.** Francis Rivet married Elizabeth Podmer at Garveston 2 July 1584 (22 months before Margaret's 1586 christening), so Elizabeth Podmer is the probable mother of Margaret Rivet; the IGI attributes a fuller child set to Francis & Elizabeth (incl. Francis 1609), with an Elen-1593-father conflict (IGI Francis vs repo image-read Edmund) to resolve. Richard Ryvett of Gressenhall's origin candidate is Richard Rivet bp 30 Nov 1575 Garveston, son of Robert.

`str_replace` in `research/people/rivett-family-of-garveston.md` (the Finding section — add the Podmer mother):

old_string:
```
Margaret Rybett is **Margaret Rivet, baptized 21 May 1586 at Garveston, Norfolk, daughter of
Francis Rivet** — now confirmed at register-image level: the Garveston register reads *"Margaret
Rivet daughter of ffrancis christened the xxjth of May,"* naming the father but **not the
mother**.[^fs][^reg-p19]
```

new_string:
```
Margaret Rybett is **Margaret Rivet, baptized 21 May 1586 at Garveston, Norfolk, daughter of
Francis Rivet** — now confirmed at register-image level: the Garveston register reads *"Margaret
Rivet daughter of ffrancis christened the xxjth of May,"* naming the father but **not the
mother**.[^fs][^reg-p19] Francis Rivet's own marriage most likely supplies her: **Francis Rivet
married Elizabeth Podmer at Garveston on 2 July 1584**, twenty-two months before Margaret's 1586
christening, so **Elizabeth Podmer is the probable mother of Margaret Rivet**.[^francis-podmer-1584]
```

`str_replace` in the same file (L-129 bullet — wife and child set):

old_string:
```
- L-129 — map Francis Rivet's full child set (Margaret's siblings) and his wife. The register
  read separates **at least three Rivet households in the parental generation — Francis (Margaret
  1586, Grace 1603), Edmund (Elen, bp 11 Apr 1593; likely the Edmund of the 1613–14 inventory),
  and Robert (a child bp Oct 1571; likely the Robert of the 1597 admon, whose widow was Agnes
  Ryvett)** — but **no register entry names a mother**, so Francis Rivet's wife (= Margaret's
  mother) is still unidentified and Margaret's full sibling set is not separable from the
  unattributed christenings. The batch-2 register (1627–1675) added no further Rivett entry and
  no wife/mother name.[^reg-p19] (Register available online via FamilySearch; not text-indexed —
  visual browse, now substantially worked.)
```

new_string:
```
- L-129 — Francis Rivet's wife and child set. **Francis Rivet's wife is most likely Elizabeth
  Podmer** (m. 2 July 1584 Garveston; see the Finding above). The IGI indexes attribute to Francis
  Rivet of Garveston a child set of **Margaret (1586), Marye (1588), Elen (1593), Thomas (1595),
  Grace (1603), Alice (1606), and Francis (1609)**, the last two explicitly to "Francis and
  Elizabeth."[^francis-podmer-1584] **Conflict to resolve at image level:** the IGI gives **Elen
  (1593)**'s father as Francis, whereas the repo's register image-read gives the Elen-1593 father
  as **Edmund** — the image read controls until re-examined, so the remaining indexed child
  assignments need image comparison before the full sibling set is fixed. The register's batch-2
  pages (1627–1675) add no further Rivett entry.[^reg-p19] (IGI index level; the Garveston register
  image is substantially worked and names no mother in the christening entries, so the Podmer
  identification rests on the 1584 marriage, not the baptisms.)
```

`str_replace` in the same file (L-130 bullet — add origin):

old_string:
```
- L-130 — Richard Ryvett of Gressenhall's origin, wives, and relation to the Garveston Rivetts.
  **An image read of the 1630/31 Gressenhall will (now transcribed) corrects the earlier
  inference.**
```

new_string:
```
- L-130 — Richard Ryvett of Gressenhall's origin, wives, and relation to the Garveston Rivetts.
  **His origin candidate is now identified: Richard Rivet, baptized 30 November 1575 at Garveston,
  son of Robert** (IGI), who fits the 1602 Gressenhall marriage at age 27 and ties Richard of
  Gressenhall back into the **Garveston Rivetts** — Robert's line beside Margaret's father
  Francis's line. If Robert and Francis Rivet of Garveston were brothers, Richard of Gressenhall
  and Margaret Rivet (Francis Gurney's wife) were **first cousins**, which would account for John
  Gurney G13 naming a son **Richard** after his mother's Gressenhall kinsman.[^richard-rivet-1575]
  **An image read of the 1630/31 Gressenhall will (now transcribed) corrects the earlier
  inference.**
```

`str_replace` in the same file (add the two footnote definitions before the `[^thornton-will]` definition):

old_string:
```
[^thornton-will]: Will of John Thornton of Gressenhall, husbandman, dated 16 May 1629, proved 6 February 1630/31 before Thomas Browne, surrogate;
```

new_string:
```
[^francis-podmer-1584]: Francis Rivet m. Elizabeth Podmer, 2 July 1584, Garveston, Norfolk — Ancestry "England, Select Marriages, 1538–1973" (IGI), record 33546675 (FHL film 1702622, item 11); the bride's surname "Podmer" from the FHL film index. The same IGI set carries children of Francis Rivet and Elizabeth at Garveston, incl. a son Francis christened 4 February 1609. Index level (no register image examined). Source IDs: `fs-england-marriages-1538-1973` (marriage); `fs-england-births-christenings` (christenings).
[^richard-rivet-1575]: Richard Rivet, christened 30 November 1575, Garveston, Norfolk, father Robert — Ancestry "England, Select Births and Christenings, 1538–1975" (IGI). Index level. The Robert is plausibly the Robert Rivett of Garveston whose 1597 administration (widow Agnes Ryvett) is recorded above. Source ID: `fs-england-births-christenings`.
[^thornton-will]: Will of John Thornton of Gressenhall, husbandman, dated 16 May 1629, proved 6 February 1630/31 before Thomas Browne, surrogate;
```

---

## Item 6 — PROMOTE: L-109 Syon forename + Earsham register baptisms → `research/people/john-gurney-earsham-will-1638.md`

**Finding.** The rare Syon/Lyon forename traces to Syon Gurnie bp 1593 Hempnall (father John); the 1638 testator's household appears in the Earsham register (father John → sons John 1635, John 1636, Henry 1638; brother Sion → Susan 1638), corroborating the will's "son John, a minor" and brother Syon at register level.

`str_replace` in `research/people/john-gurney-earsham-will-1638.md` (append a subsection after the "Reading:" paragraph):

old_string:
```
That parish coincidence does not connect the families by blood, but it puts a Waveney-family Gurney inside the Norwich parish the project watches most closely, and it is the right thread to pull when the Parmentergate Gurneys are next reviewed.
```

new_string:
```
That parish coincidence does not connect the families by blood, but it puts a Waveney-family Gurney inside the Norwich parish the project watches most closely, and it is the right thread to pull when the Parmentergate Gurneys are next reviewed.

## Parish-register traces — the Syon forename and the Earsham baptisms

The family's distinctive forename **Syon (Sion / Lyon)** and the 1638 testator's household both appear in parish-register baptisms. The earliest instance of the forename is **Syon Gurnie, christened 1593 at Hempnall** (south Norfolk, ~10 miles from Earsham), son of a **John** Gurney — rooting the rare name in a south-Norfolk John-Gurney household by 1593; the same Hempnall family recurs with father-John children (Anna 1640, Elizabeth 1641).[^hempnall-syon-1593] At Earsham itself, the testator's own household shows in the register: **father John Gurney** with sons **John (1635), John (1636)** and **Henry (1638)**, and a brother **Sion Gurney** with a daughter **Susan (1638)** — corroborating the 1638 will's "son John, a minor" and contingent-devisee brother **Syon** at register level.[^earsham-baptisms] What remains open is the identity of **Sarah Gurney's husband** (the later-generation Lyon's father): her children John/Thomas/Lyon/Mary fall in the Bungay/Mettingham (Suffolk) area outside FindMyPast's Norfolk coverage, so that step needs the Suffolk registers (Ancestry).

[^hempnall-syon-1593]: Syon Gurnie, christened 1593, Hempnall, Norfolk, father John — FindMyPast "Norfolk Baptisms"; the same Hempnall John-Gurney household has children Anna (1640) and Elizabeth (1641, mother Jane). Index level. Source ID: `findmypast-norfolk-baptisms-index`.
[^earsham-baptisms]: FindMyPast "Norfolk Baptisms," Earsham: John Gurney s. John (1635), John Gurney s. John (1636), Henry Gurney s. John (1638), and Susan Gurney dau. Sion (1638). Index level. Source ID: `findmypast-norfolk-baptisms-index`.
```

---

## Item 7 — PROMOTE: L-119 medieval Gurnay deeds → `research/places/great-ellingham.md`

**Finding.** A clean-OCR printed calendar of Norfolk deeds (DGS 004389182) records two medieval Gurnay landholding sightings: John Gurnay's tenement at St George at Gates, Norwich, and "Gurnay, Elys, [John] Stuteville, of E[llingham], … Trustees" in Somerton and Sloley — extending the dispersed pre-Lovell central-Norfolk Gurnay cluster.

`str_replace` in `research/places/great-ellingham.md`:

old_string:
```
None is yet tied to the West Barsham line or to one another; they are logged as collateral sightings for future tracing.[^bradfer-collateral-oneliners]
```

new_string:
```
None is yet tied to the West Barsham line or to one another; they are logged as collateral sightings for future tracing.[^bradfer-collateral-oneliners]

A printed calendar of medieval Norfolk deeds (digitised as FamilySearch image group DGS 004389182; clean OCR) adds two further medieval Gurnay landholding sightings in the same dispersed central-Norfolk/Norwich pattern: a **tenement of John Gurnay at St George at Gates, Norwich**, recited alongside Giles le Armourer and Margaret (formerly wife of John Lungespe); and **"Gurnay, Elys, [and] John Stuteville, of E[llingham], … Trustees"** of property in **Somerton and Sloley**. The "of E." (Ellingham) trustee tag places this Gurnay in the same Great Ellingham orbit as the wills above, and the Stuteville/Elys co-trustees set the family in a medieval Norfolk trustee network. Calendar entry numbers (Gurnay 3, 41; John Gurnay 16) are recorded for retrieval; the calendar's exact published title is not yet confirmed, so the deeds are held at catalogue level pending the original.[^medieval-gurnay-deeds-calendar]
```

`str_replace` in the same file (add the footnote definition before the `[^bradfer-collateral-oneliners]` definition):

old_string:
```
[^bradfer-collateral-oneliners]: <em>Norfolk wills extracts, 1370–1763</em> (Bradfer-Lawrence collection, typescript), Gurney-variant sweep 2026-06-13:
```

new_string:
```
[^medieval-gurnay-deeds-calendar]: A printed calendar/index of Norfolk deeds digitised as FamilySearch image group DGS 004389182 (clean-OCR; catalogued by FamilySearch as Norwich deeds), entries naming John Gurnay's tenement at St George at Gates, Norwich (assoc. Giles le Armourer) and "Gurnay, Elys, [John] Stutevyle, of E., … Trustees" in Somerton and Sloley; index nos. Gurnay 3, 41 and John Gurnay 16. Surfaced June 2026 via a film-scoped full-text sweep. The exact published title/editor of the calendar is unconfirmed; held at catalogue level. Source ID: `familysearch-fulltext-search`.
[^bradfer-collateral-oneliners]: <em>Norfolk wills extracts, 1370–1763</em> (Bradfer-Lawrence collection, typescript), Gurney-variant sweep 2026-06-13:
```

---

## Item 8 — PROMOTE: L-69/L-70 exhausted-online pursuit → `research/people/francis-gurney-of-maldon.md`

**Finding.** The Kent 1633–36 "Francis Gurnay" probate did not resurface via Google, Ancestry's full cross-collection search, or FamilySearch's indexed record search (plus FTS with widened variants); chronology makes it most plausibly a Kent-local Gurnay. The St Peter le Poer/St Benet Fink poor rate is not on Ancestry/FMP and is corroborative-only.

`str_replace` in `research/people/francis-gurney-of-maldon.md`:

old_string:
```
- **Kent, England Probate 1633–1636** — a probate hit on "Francis Gurnay"; test whether it touches Francis G14 or this Maldon Francis.
- **St Peter le Poer with St Benet Fink, London — Poor Rate** — Francis G14's own London parish; a rate naming Francis Gurnay could fix residence and civic standing.
- **Norfolk, England History Records 1701, 1825** — later compiled Norfolk material naming a Francis Gurnay.
```

new_string:
```
- **Kent, England Probate 1633–1636** — a probate hit on "Francis Gurnay." A June 2026 pursuit across other providers (Google, Ancestry's full cross-collection search, and FamilySearch's regular indexed record search, in addition to FamilySearch full-text with the widened surname-variant set) **did not resurface it** — no Kent "Francis Gurnay" probate appears outside the Center-restricted FamilySearch collection. Chronology rules out Francis G14 (died at St Botolph Bishopsgate, London, 1646/7) and this Maldon Francis (born 1628), so a 1633–36 Kent probate Francis Gurnay is most plausibly a **Kent-local Gurnay** (cf. the documented Eythorne, Kent Gurney presence), not the direct line; full recovery needs Center/affiliate access.
- **St Peter le Poer with St Benet Fink, London — Poor Rate** — Francis G14's own London parish; not mirrored on Ancestry or FindMyPast, so it likewise remains Center-restricted. It would only corroborate Francis G14's already-firmly-documented St Benet Fink residence (his children's baptisms there; "Merchant Taylor of St Benet Fink"), so it is low-yield corroboration.
- **Norfolk, England History Records 1701, 1825** — later compiled Norfolk material naming a Francis Gurnay.
```

---

## Item 9 — NEW FILE: validation for `suffolk-deeds-liber-12-1902`

`new file write` → `sources/validations/suffolk-deeds-liber-12-1902.md`:

```
# Validation — Suffolk Deeds, Liber XII (1902)

Source ID: `suffolk-deeds-liber-12-1902`

**Source.** *Suffolk Deeds, Liber XII* (Boston: Rockwell and Churchill, 1902) — printed edition of the manuscript Suffolk County (Massachusetts) registry deed book Liber XII, c. 1681–1684. Internet Archive `suffolkdeeds11suff` (full djvu text); public domain.

**Examined.** Full djvu OCR text searched for the surname Gurney/Gourney/Gurnell (35 occurrences, all "Gurnell") and the printed grantor/grantee indexes. Liber XI (`suffolkdeeds09suff`) checked and carries no Gurney/Gurnell occurrence.

**What it establishes.** The only G-surname family in the 1678–1683 Suffolk deeds is the Gurnell family of Dorchester (John Gurnell, tanner, dec'd; executrix Jane Gurnell; index Anne/George/John/Richard at pp. 84, 200, 256, 308, 309, 310). No Elizabeth of the surname; nothing of the surname at p. 343.

**Unexamined / limits.** Manuscript registry images (FamilySearch) not separately read; OCR-level quotation of the deed body only.

**Findings landed in.** `research/people/g12-richard-gurney-fact-sheet.research.md` (L-99 resolution); verbatim extract at `sources/corpus_supplement/suffolk-deeds-liber-xii-gurnell-dorchester.md`.
```

---

## Item 10 — NEW FILE: validation for `paston-letters-davis`

`new file write` → `sources/validations/paston-letters-davis.md`:

```
# Validation — Paston Letters and Papers (Norman Davis edition)

Source ID: `paston-letters-davis`

**Source.** Norman Davis, ed., *Paston Letters and Papers of the Fifteenth Century*. Consulted via Internet Archive item `ThePastonLetters` (full text).

**Examined.** The editorial note identifying "William Gurney, esq., of Tharston" (escheator of Norfolk and Suffolk 1465–6; retainer of the Duke of Norfolk; commissions 1484, 1491; d. 1505).

**What it establishes.** Identifies the Paston correspondent William Gurney of Tharston as William Gurney IV (G19) via the matching escheator office, and supplies the Duke of Norfolk retainer affinity and a (secondary) 1505 death date.

**Unexamined / limits.** Single editorial note read; the underlying Paston letter text not transcribed here. Davis's 1505 death date conflicts with the primary IPM (16 Feb 1507/8); the IPM is preferred.

**Findings landed in.** `research/people/g19-william-gurney-iv-fact-sheet.research.md` (Tharston subsection; open question 2).
```

---

## Deferred to v103 (documented, not actioned here)

- **L-148 (Robert Gvrney × Mary Lame, Norwich 1622).** Comparator household: m. 27 Jul 1622 Norwich (IGI; `fs-england-marriages-1538-1973`); children Samuel (bp 1623 Norwich St Stephen) and Katherine (bp 1639 Norwich St Benedict, mother Mary) — `findmypast-norfolk-baptisms-index`. Promote into the same-name comparator section of `research/people/g13-john-gurney-fact-sheet.research.md` (large file; anchor to be read at drafting). Not a candidate (wrong groom forename; bride's maiden name Lame).
- **L-93 (Costessey April 1659 court).** Anthony Dobbs of Marsham confirmed in film DGS 004389191; the court's manor name survives only as machine-transcript salad ("in Burton"). This is an image-read/paleography target, not transcript-promotable — keep on the lead, no companion edit.
- **Skill note (FindMyPast).** The `mothersfirstname` URL parameter does not bind (returns unfiltered results); filter by the Mother column instead. Candidate addition to `.claude/skills/findmypast-record-search/SKILL.md` per the skill's continual-improvement clause.

## Phase-2 close-outs (after application)

After application, close the resolved leads (promotion landed): **L-134**, **L-28**, **L-99** (move thin rows to `research-leads-done.csv`; scrub open-language from the companions where present). Leave L-122, L-129, L-130, L-109, L-119 as **Partial** (residual image/forename steps noted in-companion); L-69/L-70/L-8/L-93/L-94 as **Partial** (access/route-limited).
