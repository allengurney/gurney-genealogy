# England landholding catalog gap findings — direct ancestors G18–G31

Working research file for identifying England landholdings that are missing from, under-linked in, or insufficiently described by the places catalog. This is **not** a catalog patchset. It is a source-backed finding file intended to support a later Phase 1 intake patchset for `data/places.json`, `data/places_detail.json`, and related place narratives.

## Scope

- **Ancestors reviewed:** direct-line G18 through G31.
- **Geography:** England only. Normandy/France findings are out of scope except where they help separate English holdings from Norman holdings.
- **Evidence threshold:** include places where the ancestor appears to have had ownership, controlling interest, lordship, residence, estate operation, court/oversight role, feoffee/trustee role, or a compelling estate-related interaction.
- **Catalog baseline:** checked against `data/places.json` on 2026-05-26. Existing major English entries include West Barsham, Harpley, Hardingham/Swathings, Hingham/Gurney's Manor, Runhall, Irstead, King's Lynn, Saxthorpe, Hellesdon, Burnham Thorpe, Great Ellingham/Old Hall, City of London, Norfolk, Suffolk, and several earlier Domesday/senior-line localities.
- **Online enrichment pass:** 2026-05-26/27. Priority was official heritage/church/archaeology references first, then parish and local-history references. This pass found stronger church and deserted-medieval-village anchors than surviving manor-house evidence for most properties.

## Status key

| Status | Meaning |
|---|---|
| **A — Missing likely place entry** | Strong candidate for a new catalog place record or place-detail record. |
| **B — Existing place, likely under-linked or under-described** | Place exists in catalog, but the direct-line ancestor relationship or sub-manor detail is not adequately represented. |
| **C — Research lead / feoffee / trustee / disputed claim** | Useful place-memory lead, but not necessarily a new landholding entry unless later evidence supports ownership/control. |
| **D — No direct catalog action** | Already adequately represented or not attributable to the direct ancestor. |
| **H — Heritage/church anchor found** | Online pass found a useful surviving church, listed building, deserted-medieval-village, or heritage-record lead. This does not itself prove the manor-house site. |

---

## Online heritage / archaeology / church sweep — summary

### Practical conclusion

The online sweep did **not** identify a secure surviving medieval manor-house site for most of the newly identified landholdings. It did, however, identify several strong **place anchors**:

1. **Church anchors** — useful because advowsons, burial directives, church presentations, and parish geography often survive even where manor houses have disappeared.
2. **Deserted-medieval-village / settlement archaeology leads** — useful for North Barsham, Pockthorpe, Letton, and Thuxton, but these must be verified against Norfolk Historic Environment Record (NHER/NHER-style) entries before geocoding.
3. **Official Historic England listing anchors** — strongest for Houghton St Giles, where the church is Grade I and the official list gives the exact National Grid Reference.

### Online lead table

| Place / site | Online enrichment finding | Evidence value for catalog work |
|---|---|---|
| **Houghton St Giles / Houghton in the Dale, Norfolk** | Strongest official hit. Historic England lists **Church of St Giles**, Walsingham Road, Grade I, List Entry 1049418, NGR TF 92372 35362. Description: parish church, largely C14 fabric rebuilt in 1877 by William Eden Nesfield, C14 tower, Perpendicular rood screen with painted dado.[^online-houghton-he] | High-value church anchor and likely resolution of the Houghton ambiguity toward **Houghton St Giles / Houghton-in-the-Dale** in the Barsham cluster. Does **not** by itself locate the manor house. |
| **Denver, Norfolk** | Online pass found a surviving St Mary church anchor: the Denver summary identifies St Mary's as C13 with an earlier foundation and cites Historic England List Entry 1342310. It also points to later listed heritage features such as Denver Sluice and Denver Mill, which are not medieval Gurney evidence.[^online-denver] | Good parish/church anchor. Manor site remains unresolved. Phase 1 should not conflate later sluice/mill heritage with the Wauncy/Gurney manor. |
| **North Barsham, Norfolk** | A lost-settlement index identifies North Barsham as a probable deserted medieval village and points toward an NHER-style heritage lead.[^online-lost-settlements] | High-value archaeology lead. Needs direct NHER verification before coordinates/current status are asserted. |
| **Pockthorpe, Norwich** | The lost-settlement index identifies Pockthorpe as a deserted medieval settlement site.[^online-lost-settlements] | Important current-state caution: Pockthorpe is not just an absorbed suburb; it may have a medieval settlement archaeology context. Exact site of The Lathes / Hassets' Hall remains unresolved. |
| **St Gregory's parish, Norwich** | Online pass found St Gregory's Church as a Grade I redundant medieval church between Pottergate and St Benedict's Street; the church body is described as largely C14 with an older tower and a 1394 rebuilt passage under the chancel.[^online-st-gregory] | Good parish anchor for G20's Norwich house/tenements. It does **not** identify the Gurney property parcel. |
| **Drayton, Hellesdon, Saxthorpe, South Wootton** | Diocese/parish references confirm surviving medieval church anchors: St Margaret Drayton, St Mary Hellesdon, St Andrew Saxthorpe, and St Mary South Wootton are all useful parish anchors.[^online-diocese][^online-south-wootton] | Good church-survival angle for later place pages, but not manor-site evidence. |
| **Letton and Thuxton** | The lost-settlement index flags Letton and Thuxton as deserted-medieval-settlement leads; both appear as appurtenant-place names in the G18/G19 IPM/trust geography.[^online-lost-settlements] | Useful for mapping estate extent around Swathings/Hardingham and the IPM appurtenances, not automatic standalone landholding entries. |
| **Depden, Suffolk** | No secure online heritage/manor-house/church hit was found in this pass. A lower-value windmill history lead exists, but it is post-medieval and not directly useful for the Gurney manor. | Keep as high-priority place entry because repo evidence is strong; current-state and church/manor-site work remains open. |
| **Dunton, Norfolk** | No secure current-state/heritage hit was found. The place-name needs locality disambiguation before geocoding. | Hold for Phase 1 research, not immediate precise mapping. |

---

## Highest-priority findings

### 1. North Barsham, Norfolk — Wauncy/Gurney inheritance and later trust portfolio

- **Status:** A/H — Missing likely place entry; online archaeology lead found.
- **Ancestor(s):** G23 Edmund Gournay; G21 Thomas Gournay I; G19 William Gurney IV; G18 William Gurney V. Probably also G20 Thomas Gournay II by continuity, but the reviewed G20 file does not separately list North Barsham.
- **Catalog issue:** `West Barsham` exists, but `North Barsham` does not appear as a distinct place entry.
- **Relationship:** North Barsham enters the family in the Wauncy inheritance stream. The G23 companion records Blomefield's North Barsham corroboration that, in Edward III's reign, North Barsham came to Edmund Gournay through Katherine de Wauncy and remained in the family. The G18 companion's IPM/trust notes later place North Barsham in the 1505 trust portfolio with West Barsham, Houghton, and Denver.[^g23-north-barsham][^g18-ipm-trusts]
- **Repo source:** `research/people/g23-edmund-gurney-fact-sheet.research.md`; `research/people/g18-william-gurney-v-fact-sheet.research.md`.
- **Underlying source:** Francis Blomefield, *History of Norfolk*, vol. vii, "North-Barsham" and "West-Barsham" entries; Daniel Gurney, *Supplement*, Note 132/IPM material. Source ID: `blomefield-norfolk`; `[DG-Supp]`.
- **Online heritage/current-state lead:** A lost-settlement index identifies North Barsham as a probable deserted medieval village. Treat this as a strong archaeology lead, but verify against NHER directly before assigning exact coordinates or current-site status.[^online-lost-settlements]
- **Phase 1 implication:** Add as a locality/place entry with a cautious `currentSiteStatus` such as `probable deserted medieval village lead; exact manor parcel unresolved` only after direct NHER confirmation.

### 2. Depden, Suffolk — Wauncy inheritance manor with advowson

- **Status:** A — Missing likely place entry.
- **Ancestor(s):** G23 Edmund Gournay; G21 Thomas Gournay I; G20 Thomas Gournay II; G19 William Gurney IV; G18 William Gurney V.
- **Catalog issue:** `Suffolk, England` exists only as a regional entry; no Depden place entry was found.
- **Relationship:** Depden was part of the Wauncy-derived portfolio. G23's landholding table lists Depden as a Wauncy inheritance through Katherine. G21's nine-manor list includes Depden. G20's will confirmed grants to sons John and Edmund out of the manor of Depden. G18's IPM/trust notes list the Suffolk manor of Depden with the advowson of St Mary.[^g23-landholdings][^g21-landholdings][^g20-will-depden][^g18-ipm-trusts]
- **Repo source:** `research/people/g23-edmund-gurney-fact-sheet.research.md`; `research/people/g21-thomas-gournay-i-fact-sheet.research.md`; `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`; `research/people/g18-william-gurney-v-fact-sheet.research.md`.
- **Underlying source:** Daniel Gurney, *Record*, pp. 279-282 and pedigree pp. 286-287; Daniel Gurney, *Supplement*, Note 132/IPM material; Blomefield West Barsham will extract. Source IDs: `[DG-I]`, `[DG-Supp]`, `blomefield-norfolk`.
- **Online heritage/current-state lead:** No secure manor-house, archaeology, or church heritage reference was found in this pass. The place remains a strong catalog candidate based on repo evidence, but requires targeted Suffolk HER / Historic England / parish-church follow-up before current-state details are asserted.
- **Phase 1 implication:** Add as a Suffolk manor/locality candidate with no exact building status. Preserve the advowson detail and schedule a specific Suffolk HER/HE search task.

### 3. Denver, Norfolk — Wauncy/Gurney manor and annuity base

- **Status:** A/H — Missing likely place entry; church anchor found.
- **Ancestor(s):** G23 Edmund Gournay; G21 Thomas Gournay I; G19 William Gurney IV; G18 William Gurney V. Likely portfolio continuity through G20, but G20's reviewed landholding table does not separately list Denver.
- **Catalog issue:** No Denver, Norfolk place entry was found.
- **Relationship:** The G23 fact sheet states that Katherine de Wauncy was daughter of Sir William de Wauncy of West Barsham, lord of Depden and Denver, and that a 1357 grant of 100 marks per year from the West Barsham and Denver manors was settled on Edmund and Katherine. G18's IPM/trust notes place Denver in the 1505 trust with West Barsham, North Barsham, and Houghton.[^g23-factsheet-wauncy][^g18-ipm-trusts]
- **Repo source:** `fact-sheets/g23-edmund-gurney-fact-sheet.md`; `research/people/g18-william-gurney-v-fact-sheet.research.md`.
- **Underlying source:** Daniel Gurney, *Record* and *Supplement*; Blomefield, West Barsham. Source IDs: `[DG-I]`, `[DG-Supp]`, `blomefield-norfolk`.
- **Online heritage/current-state lead:** St Mary's church at Denver is identified online as physically dating from the 13th century with an earlier foundation and as a listed church under Historic England List Entry 1342310. Later listed heritage features at Denver — Denver Sluice and Denver Mill — are useful locality context but not evidence for the medieval Wauncy/Gurney manor.[^online-denver]
- **Phase 1 implication:** Add Denver as a locality/manor candidate and use St Mary's as a cautious parish/church anchor. Do not attach the Gurney manor to the sluice, mill, or any modern hall without additional evidence.

### 4. Houghton St Giles / Houghton in the Dale, Norfolk — Nerford moiety / 1505 trust property

- **Status:** A/H — Missing likely place entry; strong church anchor found.
- **Ancestor(s):** G21 Thomas Gournay I; G19 William Gurney IV; G18 William Gurney V.
- **Catalog issue:** No Houghton entry was found. The catalog has Norfolk region and nearby major Gurney seats, but not Houghton.
- **Relationship:** G21's landholding table lists "Houghton, Norfolk (Nerford moiety)," purchased by Sir John V in 1399 and inherited through the collateral-succession portfolio. G18's IPM/trust notes place Houghton in the 1505 trust with West Barsham, North Barsham, and Denver and also identify lands in Harpley/Houghton tied to the directly held Harpley manor.[^g21-landholdings][^g18-ipm-trusts]
- **Repo source:** `research/people/g21-thomas-gournay-i-fact-sheet.research.md`; `research/people/g18-william-gurney-v-fact-sheet.research.md`.
- **Underlying source:** DG-Supp Note 121/IPM succession context; DG-Supp Note 132/IPM/trust material; Blomefield West Barsham. Source IDs: `[DG-Supp]`, `blomefield-norfolk`.
- **Online heritage/current-state lead:** The online pass strongly suggests this should be treated as **Houghton St Giles / Houghton-in-the-Dale** in the Barsham parish cluster, not an unrelated Norfolk Houghton. Historic England lists Church of St Giles, Walsingham Road, as Grade I, List Entry 1049418, NGR TF 92372 35362; the official description records largely C14 fabric, a C14 tower, 1877 rebuilding by William Eden Nesfield, and a Perpendicular rood screen with painted dado.[^online-houghton-he]
- **Additional church/pilgrimage context:** Houghton St Giles is also associated with the Slipper Chapel / Catholic National Shrine of Our Lady. This is useful local heritage context, but it is not direct Gurney manor evidence.[^online-houghton-context]
- **Phase 1 implication:** Rename/normalize the lead as `Houghton St Giles / Houghton in the Dale, Norfolk` unless primary manorial evidence proves a different Houghton. Use the church as a high-confidence parish anchor, not the manor-house site.

### 5. Drayton, Norfolk — Heylesdon inheritance manor and advowson

- **Status:** A/H — Missing likely place entry; church anchor found.
- **Ancestor(s):** G21 Thomas Gournay I; possibly G18-G20 only if later continuity can be shown.
- **Catalog issue:** Hellesdon exists but Drayton does not.
- **Relationship:** The G21 companion records the Heylesdon settlement that came through Alice Heylesdon and Sir John Gurney V: manors of Hellesdon and Drayton, advowsons of both parish churches, chantries, Norwich houses, and La Selde Coronata. After Sir John's son Edmund died without issue, the inheritance crisis moved the estates to Thomas I as nephew of blood, though Alice Heylesdon later sold the bulk of the Heylesdon inheritance to Sir John Fastolf in 1433.[^g22-heylesdon-settlement][^g21-landholdings]
- **Repo source:** `research/people/g22-robert-gournay-fact-sheet.research.md`; `research/people/g21-thomas-gournay-i-fact-sheet.research.md`.
- **Underlying source:** History of Parliament Online, "GURNEY, John (d.1408), of Harpley and West Barsham"; Calendar of Close Rolls references cited there. Source ID: `hop-gurney`.
- **Online heritage/current-state lead:** St Margaret, Drayton is listed in the Norwich North deanery material as a medieval church. This is a useful church-survival angle because the Heylesdon settlement explicitly included the advowson of Drayton church.[^online-diocese]
- **Phase 1 implication:** Add Drayton as a place candidate with separate fields for `manor` and `church/advowson` context. Exact manor site remains unresolved.

### 6. Hellesdon, Norfolk — existing place, but direct-line G21 relationship likely underlinked

- **Status:** B/H — Existing place, likely under-linked; church anchor found.
- **Ancestor(s):** G21 Thomas Gournay I.
- **Catalog issue:** `Hellesdon, Norfolk` exists but is linked only to collateral Sir John Gurney d.1408, not to G21 Thomas I.
- **Relationship:** G21's landholding table includes Hellesdon as part of the Heylesdon inheritance, while G22's companion explains how the settlement moved through Sir John V's failed male line into Thomas I's collateral succession, subject to later Alice Heylesdon/Fastolf alienation issues.[^g21-landholdings][^g22-heylesdon-aftermath]
- **Repo source:** `research/people/g21-thomas-gournay-i-fact-sheet.research.md`; `research/people/g22-robert-gournay-fact-sheet.research.md`.
- **Underlying source:** History of Parliament Online, Sir John Gurney d.1408; Blomefield references cited by HoP. Source ID: `hop-gurney`.
- **Online heritage/current-state lead:** St Mary, Hellesdon is listed in the Norwich North deanery material as a medieval church. This is useful because the Heylesdon settlement included the Hellesdon manor, church advowson, and chantry context.[^online-diocese]
- **Phase 1 implication:** Add a direct-line G21 relationship only after the Fastolf-sale timing is described clearly. Enrich Hellesdon with church/advowson context.

### 7. Saxthorpe / Loundhall, Norfolk — existing place, but direct-line relationship underrepresented

- **Status:** B/H — Existing place, likely under-linked and under-described; church anchor found.
- **Ancestor(s):** G23 Edmund Gournay; G21 Thomas Gournay I; G19 William Gurney IV.
- **Catalog issue:** `Saxthorpe, Norfolk` exists but is linked only to collateral Sir John Gurney d.1408.
- **Relationship:** DG-Supp Note 117 places Saxthorpe/Loundhall in the Gournay orbit: it was held by Rector John and later by Sir John V, and Edmund's £20/year annuity to John de Mereworthe likely reflects a settlement around the manor. G21's landholding table includes Saxthorpe/Loundhall in the inherited portfolio. G19's fact sheet preserves the strongest narrative event: in 1472 William IV tried to hold a manorial court at Saxthorpe and was obstructed by John Paston; he tried again with Henry Heydon backing him, before Henry Heydon bought Saxthorpe and Titchwell from Bishop Waynflete.[^g23-saxthorpe][^g21-landholdings][^g19-saxthorpe]
- **Repo source:** `research/people/g23-edmund-gurney-fact-sheet.research.md`; `research/people/g21-thomas-gournay-i-fact-sheet.research.md`; `fact-sheets/g19-william-gurney-iv-fact-sheet.md`; `research/people/g19-william-gurney-iv-fact-sheet.research.md`.
- **Underlying source:** DG-Supp Note 117; Paston Letters, Gairdner edition; Blomefield/HoP context. Source IDs: `[DG-Supp]`, `paston-letters-gairdner`, `blomefield-norfolk`.
- **Online heritage/current-state lead:** St Andrew, Saxthorpe is a surviving parish church anchor in the diocesan material. This supports a parish-centered mapping approach while the exact Loundhall manor site remains unresolved.[^online-diocese]
- **Phase 1 implication:** Enrich existing Saxthorpe with direct-line narrative and a `Loundhall` alias/detail. Do not assign the court episode to a specific parcel until Loundhall is located.

### 8. South Wootton, Norfolk — G27 forfeited/rebel manor

- **Status:** A/H — Missing likely place entry; village/church anchor found.
- **Ancestor(s):** G27 Sir John de Gournay I.
- **Catalog issue:** No South Wootton entry was found.
- **Relationship:** The G27 companion and fact sheet preserve the 1264/65 plea in which John de Bolemer seized livestock and chattels on the manor of South Wootton because John de Gurney had been in the conflict of Lewes against the king and in resistance afterward. Alice de Balesham sued because the seized stock belonged to her under a twelve-year lease from John to Stephen de Balesham beginning Michaelmas 1258. Farrer independently corroborates the episode, naming the manor of John de Gurney at South Wootton and associating the forfeiture with the Evesham/rebel arc.[^g27-south-wootton][^g27-farrer]
- **Repo source:** `research/people/g27-sir-john-de-gournay-i-fact-sheet.research.md`; `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`.
- **Underlying source:** DG-I Appendix LXI p. 341; DG-Supp Note 112 pp. 781-783; Placita coram Rege, 49 Henry III, No. 124; William Farrer, *Honors and Knights' Fees*, vol. 3, Honor of Arundel, p. 142. Source IDs: `dg-rec-pt1`, `dg-rec-supp`, `farrer-honors-knights-fees-v3-gurnay-extracts`.
- **Online heritage/current-state lead:** The current village lies about two miles northeast of King's Lynn; the older part of the village grew around the green and St Mary the Virgin church. This supplies a village/church anchor but not a secure medieval manor-house site.[^online-south-wootton]
- **Phase 1 implication:** Add South Wootton as a strong place candidate. The `currentSiteStatus` should state `parish/village anchor identified; exact medieval manor site unresolved`.

### 9. Pockthorpe-by-Norwich / The Lathes / Hassets' Hall — G19 town residence through Calthorpe kinship

- **Status:** A/C/H — Missing place entry; lost-settlement archaeology lead found.
- **Ancestor(s):** G19 William Gurney IV.
- **Catalog issue:** No Pockthorpe, The Lathes, or Hassets' Hall entry was found.
- **Relationship:** The G19 fact sheet states that William IV was "of West Barsham and Pockthorpe" and maintained a town residence at Pockthorpe-by-Norwich. The G19 narrative explains the likely mechanism: the house was almost certainly the same complex held by William IV's brother-in-law William Calthorpe of Pockthorpe, later known as The Lathes and, under the Blennerhassets, as Hassets' Hall. This makes the place important for residence and Calthorpe marriage-network geography, but not necessarily a separate Gurney acquisition.[^g19-pockthorpe-factsheet][^g19-pockthorpe-research]
- **Repo source:** `fact-sheets/g19-william-gurney-iv-fact-sheet.md`; `research/people/g19-william-gurney-iv-fact-sheet.research.md`.
- **Underlying source:** Daniel Gurney, *Record*, pedigree p. 287 and p. 281; DG-Supp Note 131 p. 817; Blomefield/Calthorpe material cited in G19 file. Source IDs: `[DG-I]`, `[DG-Supp]`, `blomefield-norfolk`.
- **Online heritage/current-state lead:** Pockthorpe is identified in a lost-settlement index as a deserted medieval settlement site. This makes an archaeology-first follow-up important before geocoding The Lathes or Hassets' Hall.[^online-lost-settlements]
- **Phase 1 implication:** Add Pockthorpe as a residence/locality lead with a caution that (a) Gurney relationship is residence/kinship-use, not proven ownership, and (b) exact hall site is unresolved.

### 10. Norwich, St Gregory's parish town house and tenements — G20 residence and sale to G19

- **Status:** A/H — Missing likely place-detail record; strong parish church anchor found.
- **Ancestor(s):** G20 Thomas Gournay II; G19 William Gurney IV as purchaser/heir from his father's will.
- **Catalog issue:** No Norwich place entry was found in the catalog except broader City of London and King's Lynn entries. This house should not be conflated with Pockthorpe; it is St Gregory's parish, Norwich.
- **Relationship:** G20's fact sheet and companion state that Thomas II had three residences: West Barsham, Harpley, and a Norwich town house in St Gregory's parish. Blomefield's will extract adds that all tenements in Norwich were to be sold to William his son for 80 marks, and that the house was in St Gregory's parish.[^g20-three-residences][^g20-blomefield-will]
- **Repo source:** `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`; `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`.
- **Underlying source:** Daniel Gurney, *Record*, pp. 280-282; Blomefield, *History of Norfolk*, vol. vii, West Barsham will extract; NRO NCC will register Jekkys, fol. 211. Source IDs: `[DG-I]`, `blomefield-norfolk`, `nro-ncc-wills-registers`.
- **Online heritage/current-state lead:** St Gregory's Church survives as a Grade I redundant medieval church between Pottergate and St Benedict's Street. The church is a parish anchor, not proof of the Gurney house parcel. Online summaries describe a largely C14 body, older tower, wall paintings, and a public passage under the chancel rebuilt in 1394.[^online-st-gregory]
- **Phase 1 implication:** Add a Norwich / St Gregory's parish place-detail candidate. Use the church as the initial coordinate anchor only with a precision note such as `parish anchor only; Gurney tenement parcel unidentified`.

### 11. Dunton, Norfolk — lands settled on William Gurney junior

- **Status:** A/C — Missing lead; needs exact locality confirmation.
- **Ancestor(s):** G19 William Gurney IV; G18 William Gurney V.
- **Catalog issue:** No Dunton, Norfolk entry was found.
- **Relationship:** The G19 companion and fact sheet note a 1497/98 Blomefield record in which lands in Dunton were settled on William Gurney junior, distinct from the better-known 1485 and 1505 trust deeds. This likely concerns G18 William V, eldest son of G19 William IV.[^g19-dunton]
- **Repo source:** `research/people/g19-william-gurney-iv-fact-sheet.research.md`; `fact-sheets/g19-william-gurney-iv-fact-sheet.md`.
- **Underlying source:** Blomefield, West Barsham entry. Source ID: `blomefield-norfolk`.
- **Online heritage/current-state lead:** No secure current-state/heritage hit was found in this pass. The correct Dunton must be disambiguated before coordinates are assigned.
- **Phase 1 implication:** Hold as a research lead unless Blomefield/locality evidence resolves the precise Dunton.

### 12. Hingham Gurney's / Gurney's Manor, Hingham — existing place but early-generation links incomplete

- **Status:** B — Existing place, likely under-linked or requiring relationship qualifiers.
- **Ancestor(s):** G31 Walter de Gournay; G30 William de Gournay I; possibly G27 Sir John de Gournay I and later early lords.
- **Catalog issue:** `Hingham, Norfolk` and `Gurney's Manor, Hingham` exist, but current ancestor links are later-focused and do not appear to include the early junior-branch founders G31/G30 or G27.
- **Relationship:** G31's companion quotes DG's junior-branch foundation passage: the Gournays of Swathings were subenfeoffed as mesne lords of the manors of Hingham Gurney's and Swathings in Hardingham before Hugh V's 1205 forfeiture. The G27 fact sheet also summarizes John as lord of Harpley, Hardingham, Hingham, and associated Norfolk manors.[^g31-hingham][^g27-factsheet-hingham]
- **Repo source:** `research/people/g31-walter-de-gournay-fact-sheet.research.md`; `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`.
- **Underlying source:** Daniel Gurney, *Record*, pp. 277-278 and pedigree p. 286. Source ID: `[DG-I]`.
- **Online heritage/current-state lead:** No new official source was added in this pass beyond the existing catalog's Hingham/Gurney's Manor information. This remains an internal catalog-linking issue rather than a new heritage discovery.
- **Phase 1 implication:** Decide whether early G31/G30/G27 links attach to `Hingham, Norfolk`, `Gurney's Manor, Hingham`, or both.

---

## Secondary / trustee / feoffee / appurtenant-place leads

### Feltwell and Mundford, Norfolk — G23 as trustee for John de Plays

- **Status:** C — Missing trustee/oversight lead.
- **Ancestor(s):** G23 Edmund Gournay.
- **Catalog issue:** No Feltwell or Mundford entries were found.
- **Relationship:** Close Rolls, 5 Richard II (1382), records John de Plays, knight, giving the manor of Feltwell and the manor of Mundford with the advowson to trustees including Edmund Gournay and several major knights. This is a significant legal-trust relationship, not proof of beneficial ownership by Edmund.[^g23-feltwell-mundford]
- **Repo source:** `research/people/g23-edmund-gurney-fact-sheet.research.md`.
- **Underlying source:** DG-Supp Note 117; Close Rolls 5 Richard II. Source ID: `[DG-Supp]`.
- **Geo/current-state lead:** Add only if the catalog includes trustee/feoffee places; otherwise preserve in a place-research note.

### Great Riburgh and Little Riburgh / Woodhall, Norfolk — Walsingham grantor/trustee context

- **Status:** C — Missing grantor/trustee/ecclesiastical-endowment lead.
- **Ancestor(s):** G23 Edmund Gournay.
- **Catalog issue:** No Riburgh/Woodhall or Walsingham Priory entry was found in the checked catalog excerpt.
- **Relationship:** In 1385 Edmund was named with Stephen de Hales, Oliver de Calthorpe, Ralph de Shelton, and William de Walsham in a license to grant the manors of Great Riburgh and Little Riburgh/Woodhall to the Prior and Convent of Walsingham.[^g23-riburgh]
- **Repo source:** `research/people/g23-edmund-gurney-fact-sheet.research.md`.
- **Underlying source:** DG-Supp Note 116; Patent Roll 8 Richard II, p. 2, m. 15; Monasticon Anglicanum, vol. VI, p. 74. Source IDs: `[DG-Supp]`, `[Dugdale-Mon]`.
- **Geo/current-state lead:** Treat as ecclesiastical grant/trustee context unless additional evidence shows Edmund's beneficial ownership.

### Berford's Manor, Cringleford, Norfolk — De la Pole feoffee network

- **Status:** C — Missing feoffee/oversight lead.
- **Ancestor(s):** G23 Edmund Gournay.
- **Catalog issue:** No Cringleford or Berford's Manor entry was found.
- **Relationship:** Blomefield records that Berford's Manor at Cringleford was settled on Edmund Gourney, William de Boyton, Thomas Spynk, and John le Latimer of Norwich as De la Pole feoffees. The manor extended into Hethersett, Eaton, Earlham, Little Melton, Colney, and the Cringleford watermill. By 1381 John le Latimer was sole lord and Edmund and the other feoffees released their right.[^g23-cringleford]
- **Repo source:** `research/people/g23-edmund-gurney-fact-sheet.research.md`.
- **Underlying source:** Blomefield, *History of Norfolk*, vol. 5, "Cringleford" / "Berford's Manor," pp. 33-39. Source ID: `blomefield-norfolk-vol5-pp33-cringleford-berford`.
- **Geo/current-state lead:** Good candidate for future mapping of Edmund's legal network, but not a direct Gurney landholding unless more evidence is found.

### East Barsham / Waldgraves, Norfolk — G20 seal on feoffment deed

- **Status:** C — Missing feoffee/seal/documentary-interaction lead.
- **Ancestor(s):** G20 Thomas Gournay II.
- **Catalog issue:** No East Barsham/Waldgraves entry was found.
- **Relationship:** A 1445 deed of feoffment preserved at Hunstanton Hall names Thomas Gurnay, Esq., among feoffees conveying the manor called Waldgraves in East Barsham to John Wode of Berston and others. The deed preserves Thomas's seal impression. This is highly valuable for heraldic/documentary reasons, but the reviewed evidence does not show Thomas owned Waldgraves beneficially.[^g20-waldgraves]
- **Repo source:** `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`.
- **Underlying source:** DG-Supp Note 126, p. 814. Source ID: `[DG-Supp]`.
- **Geo/current-state lead:** Research lead only unless later deed analysis shows beneficial ownership.

### La Selde Coronata, City of London — Heylesdon commercial warehouse

- **Status:** A/C — Missing specific sub-place, but uncertain direct-line retention.
- **Ancestor(s):** G21 Thomas Gournay I by collateral succession theory; collateral Sir John V / Alice Heylesdon definitely.
- **Catalog issue:** `City of London` exists, but the specific warehouse/commercial site `La Selde Coronata` is not represented.
- **Relationship:** G21's landholding table lists La Selde Coronata as a Heylesdon inheritance that may already have been alienated. The Heylesdon settlement included London property along with Hellesdon, Drayton, Norwich houses, advowsons, and chantries.[^g21-landholdings][^g22-heylesdon-settlement]
- **Repo source:** `research/people/g21-thomas-gournay-i-fact-sheet.research.md`; `research/people/g22-robert-gournay-fact-sheet.research.md`.
- **Underlying source:** History of Parliament Online, Sir John Gurney d.1408, citing Close Rolls 1405-1409 and 1409-1413. Source ID: `hop-gurney`.
- **Geo/current-state lead:** Needs London Husting/Close Roll work before any exact mapping. Avoid assigning a modern parcel prematurely.

### Appurtenant lands in the G18 IPM/trusts — Brandon, Reymerston, Corston, Rising, Thuxton, Hinghamberg, West Dereham, Fincham, Fordham, Downham, Larlingford

- **Status:** C/H — Appurtenant-place sweep; some settlement archaeology leads found.
- **Ancestor(s):** G18 William Gurney V; G19 William Gurney IV.
- **Catalog issue:** Some localities may be absent from the catalog, but they appear as appurtenances to larger manors/trust packages rather than necessarily separate controlled manors.
- **Relationship:** G18's IPM/trust notes list lands attached to Swathings/Rokelondtoftes/Hingham and the West Barsham/North Barsham/Houghton/Denver trust. These should be used for mapping estate extent, but not automatically promoted to independent landholding entries.[^g18-ipm-trusts]
- **Online heritage/current-state lead:** Letton and Thuxton are flagged in an online lost-settlement index as deserted-medieval-settlement leads. These are useful for Swathings/appurtenant-land mapping, but need direct NHER verification.[^online-lost-settlements]
- **Phase 1 implication:** Distinguish manor-level entries from appurtenant-place aliases. Letton/Cranworth may be best handled as Swathings extent details unless stronger evidence supports standalone place records.

### Little Cressingham / Hopton — rejected or low-confidence G22 lead

- **Status:** D/C — Not a direct-line catalog addition on current evidence.
- **Ancestor(s):** G22 Robert Gournay only as a rejected/low-confidence namesake lead.
- **Catalog issue:** No action recommended for direct G18-G31 catalog work unless the 1405 fine is later proved to identify G22.
- **Relationship:** A 1405 Little Cressingham fine names Robert Gurnay of Cressingham-Parva over parcels of land and foldcourse liberty in Little Cressingham and Hopton. The G22 companion explicitly says identification with G22 is not warranted; the place cluster is not otherwise associated with the Edmund-Gurney line, and later Hopton came to Anthony Gurnay by a fresh Lovel marriage.[^g22-cressingham]
- **Repo source:** `research/people/g22-robert-gournay-fact-sheet.research.md`.
- **Underlying source:** Blomefield, *History of Norfolk*, vol. vi, Little Cressingham entry. Source ID: `blomefield-norfolk`.
- **Geo/current-state lead:** Preserve as a rejected lead, not a catalog gap.

### Winburgh/Quineborghe, Stoke Bardolf, and Okebrook — uncertain John de Gurnay feoffee evidence

- **Status:** C/D — Probably collateral Rector John, not G25 John III.
- **Ancestor(s):** G25 John de Gournay III only as a possible but uncertain attribution.
- **Catalog issue:** No action recommended for direct-line catalog unless attribution changes.
- **Relationship:** G25's companion records a 1314 Escheat Roll entry naming John de Gurnay as feoffee of Bardolf baronial properties, including Winburgh/Quineborghe in Norfolk and Stoke Bardolf/Okebrook outside Norfolk. The companion says the date fits either G25 John III or Rector John, but Rector John is more likely as the more prominent John at that date.[^g25-bardolf]
- **Repo source:** `research/people/g25-john-de-gournay-iii-fact-sheet.research.md`.
- **Underlying source:** DG-Supp Note 115; Escheat Rolls 7 Edward II; Dodsworth MS. 57. Source ID: `[DG-Supp]`.
- **Geo/current-state lead:** Hold out of Phase 1 catalog patch unless the primary Escheat Roll clarifies attribution.

### Dore Abbey, Herefordshire — G28 charter-witness context, not landholding

- **Status:** C/D — Compelling interaction but not a landholding.
- **Ancestor(s):** G28 William de Gournay II.
- **Catalog issue:** No place patch recommended under landholdings objective unless the site is later used for broader "documentary appearance" mapping.
- **Relationship:** G28 witnessed Clifford charters to Dore Abbey in 1220 and related material, showing high-status Herefordshire network ties through the senior-line Clifford connection. No evidence shows William owned or controlled Dore Abbey property.[^g28-dore]
- **Repo source:** `research/people/g28-william-de-gournay-ii-fact-sheet.research.md`.
- **Underlying source:** DG-Supp Note 111; Dodsworth MS. 42; Dugdale, *Monasticon Anglicanum*, vol. V, p. 555. Source IDs: `[DG-Supp]`, `[Dodsworth]`, `[Dugdale-Mon]`.

---

## Per-ancestor sweep notes

### G18 — William Gurney V

Likely catalog actions: add/consider North Barsham, Houghton St Giles/Houghton in the Dale, Denver, Depden, Dunton if tied to William junior, and possibly place-detail aliases for Barkers/Bakers in Irstead and appurtenant lands. Existing entries already cover West Barsham, Harpley, Hardingham/Swathings, Hingham, and Irstead at the locality level.

### G19 — William Gurney IV

Likely catalog actions: Pockthorpe/The Lathes/Hassets' Hall; Dunton lands settled on William junior; Saxthorpe/Loundhall underlink; Denver/Depden/North Barsham/Houghton continuity through the trust portfolio. Existing entries already cover West Barsham, Harpley, Hardingham, Burnham Thorpe, and likely Hingham at a broad level.

### G20 — Thomas Gournay II

Likely catalog actions: Norwich St Gregory's parish town house/tenements; Depden; possibly East Barsham/Waldgraves as a feoffee/seal research lead. Existing entries cover West Barsham, Harpley, and Hardingham/Swathings.

### G21 — Thomas Gournay I

Likely catalog actions: Saxthorpe/Loundhall underlink; Houghton St Giles/Houghton in the Dale; Hellesdon underlink; Drayton; Depden; La Selde Coronata as a specific City of London sub-place if retained. Existing entries cover West Barsham, Harpley, Hardingham/Swathings, and Hellesdon at least partially.

### G22 — Robert Gournay

No direct catalog action recommended. Robert's specific holdings remain undocumented; the Little Cressingham/Hopton Robert Gurnay is a namesake lead but not attributable to G22. The Heylesdon settlement matters because it affects Robert's son Thomas I, not because Robert himself is documented as lord.

### G23 — Edmund Gournay

Likely catalog actions: North Barsham, Depden, Denver, Saxthorpe/Loundhall underlink. Secondary leads: Feltwell, Mundford, Great/Little Riburgh/Woodhall, Berford's Manor/Cringleford. Existing entries cover West Barsham, Harpley, Hardingham/Swathings, and King's Lynn.

### G24 — John de Gournay IV

No new missing England landholding found in the reviewed companion/fact-sheet evidence. Harpley and Hardingham/Swathings are already in catalog. The 1354 Harpley court is important source evidence for the Harpley place narrative.

### G25 — John de Gournay III

No high-confidence new direct landholding found. The Bardolf feoffee evidence at Winburgh/Quineborghe, Stoke Bardolf, and Okebrook is probably Rector John rather than G25 and should remain a research lead only. Harpley and Hardingham/Swathings are already represented.

### G26 — Sir William de Gournay III

No new missing England landholding found. Harpley and Hardingham/Swathings are already represented. The 1274 Hardingham warren claim should strengthen the Hardingham place narrative.

### G27 — Sir John de Gournay I

Likely catalog actions: South Wootton as a direct manor; Hingham/Gurney's Manor underlink or at least reconcile fact sheet claim to Hingham with existing catalog relationships. Existing entries cover Harpley, Hardingham/Swathings, Runhall, and Lewes battlefield context.

### G28 — William de Gournay II

No new direct England landholding found. Existing entries cover Harpley, Hardingham/Swathings, and Runhall. Dore Abbey is a valuable documentary-appearance lead, not a landholding.

### G29 — Matthew de Gournay

No new missing England landholding found. Existing entries cover Harpley, Hardingham/Swathings, and Runhall. The major catalog note is interpretive: Harpley entered the family by marriage to Rose de Burnham, arranged by Hameline Plantagenet / de Warenne. The place is present; the marriage-acquisition narrative should be preserved in the Harpley place narrative if not already.

### G30 — William de Gournay I

Likely catalog actions: evaluate whether the catalog should represent the unspecified Suffolk quarter knight's fee as a region-level source note or defer until localized; enrich Hardingham/Swathings with Swathings' extent across Hardingham, Letton, and Cranworth; consider early Hingham Gurney's linkage through the branch-foundation text. Existing entries cover Runhall, Hardingham/Swathings, and non-England Montigny-sur-Andelle.

### G31 — Walter de Gournay

Likely catalog actions: evaluate unspecified Suffolk quarter knight's fee; underlink early Hingham Gurney's if supported by DG's branch-foundation passage; possibly add Letton/Cranworth as Swathings extent details rather than separate landholdings. Existing entries cover Hardingham/Swathings and Runhall at a broad level.

---

## Suggested Phase 1 intake order

1. **Owned/residential high-confidence additions:** South Wootton; North Barsham; Depden; Denver; Houghton St Giles/Houghton in the Dale; Drayton; Norwich St Gregory's parish house/tenements; Pockthorpe/The Lathes; Dunton.
2. **Existing-place corrections/enrichments:** Saxthorpe/Loundhall direct-line links; Hellesdon G21 link; Hingham/Gurney's Manor early-generation links; Hardingham/Swathings extent details for Letton/Cranworth.
3. **Church/heritage anchors to research before geocoding:** St Giles Houghton; St Mary Denver; St Margaret Drayton; St Mary Hellesdon; St Andrew Saxthorpe; St Mary South Wootton; St Gregory Norwich; North Barsham DMV; Pockthorpe DMV.
4. **Trustee/feoffee research leads:** Feltwell; Mundford; Great/Little Riburgh/Woodhall; Berford's Manor/Cringleford; East Barsham/Waldgraves.
5. **Hold/reject unless new evidence appears:** Little Cressingham/Hopton Robert Gurnay; Bardolf feoffee properties for uncertain John de Gurnay; Dore Abbey.

---

## Footnotes

[^g23-north-barsham]: `research/people/g23-edmund-gurney-fact-sheet.research.md`, "Norwich civic counsel and North Barsham corroboration" and landholding notes. Underlying source: Francis Blomefield, "Gallow and Brothercross Hundreds: North-Barsham," *History of Norfolk*, vol. 7, pp. 47-52. Source ID: `blomefield-norfolk`.

[^g18-ipm-trusts]: `research/people/g18-william-gurney-v-fact-sheet.research.md`, IPM/trust material. Underlying source: Daniel Gurney, *Supplement to the Record of the House of Gournay* (1858), Note 132 / Inquisition Post Mortem of William Gurney senior, pp. 817-820. Source ID: `[DG-Supp]`.

[^g23-landholdings]: `research/people/g23-edmund-gurney-fact-sheet.research.md`, Landholdings table and Wauncy inheritance notes. Underlying sources: Daniel Gurney, *Record*, pp. 279, 357-363; Blomefield, West Barsham. Source IDs: `[DG-I]`, `blomefield-norfolk`.

[^g21-landholdings]: `research/people/g21-thomas-gournay-i-fact-sheet.research.md`, Landholdings table listing West Barsham, Harpley, Hardingham/Swathings, Saxthorpe/Loundhall, Houghton, Hellesdon, Drayton, Depden, and La Selde Coronata. Underlying sources: DG-I pp. 279-280; DG-Supp Note 121; HoP Sir John Gurney d.1408.

[^g20-will-depden]: `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`, Blomefield will extract preserving grants to sons John and Edmund out of Depden. Underlying source: Blomefield, West Barsham, pp. 42-47. Source ID: `blomefield-norfolk`.

[^g23-factsheet-wauncy]: `fact-sheets/g23-edmund-gurney-fact-sheet.md`, marriage/vitals section and narrative stating Katherine de Wauncy was associated with West Barsham, Depden, and Denver, with 100 marks per year from West Barsham and Denver settled in 1357.

[^g22-heylesdon-settlement]: `research/people/g22-robert-gournay-fact-sheet.research.md`, "Heylesdon settlement -- Hellesdon and Drayton manors, advowsons, chantries, Norwich houses." Underlying source: History of Parliament Online, "GURNEY, John (d.1408), of Harpley and West Barsham, Norf." Source ID: `hop-gurney`.

[^g22-heylesdon-aftermath]: `research/people/g22-robert-gournay-fact-sheet.research.md`, "Heylesdon-aftermath continuation: Alice Heylesdon's three marriages and 1433 Fastolf sale." Underlying source: HoP Sir John Gurney d.1408; Blomefield x.411, 426; NRO Reg. Surflete f.27.

[^g23-saxthorpe]: `research/people/g23-edmund-gurney-fact-sheet.research.md`, DG-Supp Note 117 discussion of Saxthorpe/Loundhall and Edmund's annuity to John de Mereworthe.

[^g19-saxthorpe]: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`, narrative section on the 1472 Saxthorpe Court episode; `research/people/g19-william-gurney-iv-fact-sheet.research.md`, Saxthorpe/Paston Letters notes. Underlying source: James Gairdner, ed., *The Paston Letters*, vol. II. Source ID: `paston-letters-gairdner`.

[^g27-south-wootton]: `research/people/g27-sir-john-de-gournay-i-fact-sheet.research.md`, "South Wootton seizure -- full plea text"; `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`, highlight and citation note. Underlying source: DG-I Appendix LXI; DG-Supp Note 112, Placita coram Rege 49 Henry III, No. 124.

[^g27-farrer]: `research/people/g27-sir-john-de-gournay-i-fact-sheet.research.md`, "Farrer corroboration: South Wootton, Evesham, and the rebel seizure." Underlying source: William Farrer, *Honors and Knights' Fees*, vol. 3, Honor of Arundel, p. 142. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.

[^g19-pockthorpe-factsheet]: `fact-sheets/g19-william-gurney-iv-fact-sheet.md`, vitals/highlights/narrative for "of West Barsham and Pockthorpe" and town house at Pockthorpe-by-Norwich.

[^g19-pockthorpe-research]: `research/people/g19-william-gurney-iv-fact-sheet.research.md`, Pockthorpe/Calthorpe notes identifying The Lathes / Hassets' Hall context. Underlying source: DG-Supp Note 131 p. 817 and related Blomefield material.

[^g20-three-residences]: `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`, highlights and citations on Thomas II's three residences; underlying source Daniel Gurney, *Record*, pp. 280-281.

[^g20-blomefield-will]: `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`, Blomefield full will extract: Norwich tenements sold to William for 80 marks and house in St Gregory's parish. Source ID: `blomefield-norfolk`.

[^g19-dunton]: `research/people/g19-william-gurney-iv-fact-sheet.research.md` and `fact-sheets/g19-william-gurney-iv-fact-sheet.md`, Blomefield 1497/98 note that William IV settled lands in Dunton on William junior. Underlying source: Blomefield, West Barsham. Source ID: `blomefield-norfolk`.

[^g31-hingham]: `research/people/g31-walter-de-gournay-fact-sheet.research.md`, DG-I Part II Preface quote: Swathings Gournays were subenfeoffed as mesne lords of Hingham Gurney's and Swathings in Hardingham before Hugh V's forfeiture. Underlying source: Daniel Gurney, *Record*, pp. 277-278.

[^g27-factsheet-hingham]: `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`, occupation/status field summarizing John as lord of Harpley, Hardingham, Hingham, and associated Norfolk manors.

[^g23-feltwell-mundford]: `research/people/g23-edmund-gurney-fact-sheet.research.md`, "Feltwell and Mundford trusts (DG-Supp Note 117)." Underlying source: Close Rolls 5 Richard II, cited via DG-Supp Note 117.

[^g23-riburgh]: `research/people/g23-edmund-gurney-fact-sheet.research.md`, "Walsingham 1385 charter -- Edmund named." Underlying source: Patent Roll 8 Richard II, p. 2, m. 15; Monasticon Anglicanum, vol. VI, p. 74.

[^g23-cringleford]: `research/people/g23-edmund-gurney-fact-sheet.research.md`, "Berford's Manor, Cringleford -- De la Pole feoffee, c.1370." Underlying source: Blomefield, *History of Norfolk*, vol. 5, pp. 33-39. Source ID: `blomefield-norfolk-vol5-pp33-cringleford-berford`.

[^g20-waldgraves]: `research/people/g20-thomas-gournay-ii-fact-sheet.research.md`, "Thomas II's seal -- Hunstanton Hall deed (DG-Supp Note 126)." Underlying source: DG-Supp Note 126 p. 814.

[^g22-cressingham]: `research/people/g22-robert-gournay-fact-sheet.research.md`, "Earliest Norfolk Robert Gurnay in G22's floruit window -- 1405 Cressingham-Parva fine." Underlying source: Blomefield, *History of Norfolk*, vol. vi, Little Cressingham entry.

[^g25-bardolf]: `research/people/g25-john-de-gournay-iii-fact-sheet.research.md`, "Norfolk feodary -- Swathings under Bardolf" and 1314 Escheat Roll feoffment notes. Underlying source: DG-Supp Note 115; Escheat Rolls 7 Edward II; Dodsworth MS. 57.

[^g28-dore]: `research/people/g28-william-de-gournay-ii-fact-sheet.research.md`, "Clifford charter witness, 1220 (DG-Supp Note 111)." Underlying sources: Dodsworth MS. 42; Dugdale, *Monasticon Anglicanum*, vol. V, p. 555.

[^online-houghton-he]: Online heritage sweep, 2026-05-26/27. Historic England, National Heritage List for England, "Church of St Giles," Walsingham Road, Barsham / Houghton St Giles, Grade I, List Entry 1049418, NGR TF 92372 35362. Official list description: parish church, largely C14 fabric rebuilt 1877 by William Eden Nesfield, C14 tower, Perpendicular rood screen with painted dado. URL: https://historicengland.org.uk/listing/the-list/list-entry/1049418

[^online-houghton-context]: Online heritage sweep, 2026-05-26/27. Houghton Saint Giles locality summary identifies the settlement as also called Houghton-le-Dale / Houghton-in-the-Hole, places it in the modern Barsham parish group with East, West, and North Barsham, and notes the Slipper Chapel / Catholic National Shrine context. Verify against Norfolk HER and shrine sources before site-page use.

[^online-denver]: Online heritage sweep, 2026-05-26/27. Denver locality summary identifies St Mary's church as C13 with an earlier foundation and cites Historic England List Entry 1342310; the same page cites later Denver heritage features including Denver Sluice and Denver Mill. URL checked as lead: https://en.wikipedia.org/wiki/Denver,_Norfolk. Direct Historic England page should be verified during Phase 1 before copying list detail into catalog fields.

[^online-lost-settlements]: Online heritage sweep, 2026-05-26/27. "List of lost settlements in Norfolk" identifies North Barsham as a probable deserted medieval village, Pockthorpe as a deserted medieval settlement site, and flags Letton and Thuxton as deserted-medieval-settlement leads. URL checked as lead: https://en.wikipedia.org/wiki/List_of_lost_settlements_in_Norfolk. Treat as an index to verify against Norfolk Historic Environment Record / Norfolk Heritage Explorer, not as final authority.

[^online-st-gregory]: Online heritage sweep, 2026-05-26/27. St Gregory's Church, Norwich summary identifies the church as a Grade I redundant medieval church between Pottergate and St Benedict's Street, with largely C14 body, older tower, wall paintings, and a public passage under the chancel rebuilt in 1394. URL checked as lead: https://en.wikipedia.org/wiki/St_Gregory%27s_Church,_Norwich. Verify against Historic England/Norwich Historic Churches Trust before precise catalog fields.

[^online-diocese]: Online heritage sweep, 2026-05-26/27. Diocese/parish-list material identifies St Margaret Drayton, St Mary Hellesdon, St Andrew Saxthorpe, and St Mary South Wootton as surviving parish churches in the relevant deaneries; Drayton and Hellesdon are explicitly marked medieval in the consulted list. URL checked as lead: https://en.wikipedia.org/wiki/Diocese_of_Norwich. Use as a quick church-anchor index; verify against diocesan, parish, and Historic England sources before final place-detail entries.

[^online-south-wootton]: Online heritage sweep, 2026-05-26/27. South Wootton locality summary places the village about two miles northeast of King's Lynn and notes that the older part of the village grew around the green and St Mary the Virgin church. URL checked as lead: https://en.wikipedia.org/wiki/South_Wootton. This is a parish/village anchor only, not a medieval manor-house identification.
