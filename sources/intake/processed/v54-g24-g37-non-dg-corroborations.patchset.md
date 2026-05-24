# Intake patchset v54 — G24–G37 vital-stats audit, supplemental (non-DG corroborations and open-item research)

**Prepared:** 2026-05-23
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation). **Status:** Draft patchset for review. **Do NOT apply until approved.**
**Origin:** Continuation of v53 audit per user feedback to reduce DG-emphasis, pursue parity sources, and chase online open items.
**Prerequisite:** Apply v53 first. This patchset assumes v53 sections have landed; many of the edits below append to or amend the same fact-sheet sections v53 touched.

## Scope

Supplemental audit pass for G24–G37 with two stated objectives from the user:

1. **De-emphasise Daniel Gurney.** Add parity-level non-DG citations to fact-sheet vitals where existing footnotes lean exclusively on DG. Many of these non-DG sources are *already* in the paired research companions (FMG MedLands, Pattou Racines Histoire, Hannay 1867, Pettigrew 1871, Anderson 1742, Open Domesday, Blomefield via BHO, History of Parliament Online, Wikipedia, *Chronicon Beccensis*, Orderic, Guillaume de Jumièges) but have not been promoted into the fact-sheet citation list.
2. **Pursue online open items.** Verifiable findings from this session's online research are integrated below, with explicit URL anchors. Productive new-discovery leads are listed in Section 17 for separate execution.

This patchset does NOT re-do the v53 work. v53 corrects vital-stat *errors and inconsistencies*. v54 *strengthens citations* and *closes or escalates open items*.

## Sources / data referenced

This patchset uses existing `data/sources.json` entries where available and proposes the addition of seven new sourceIds. The proposed entries are listed in Section 16 in the exact JSON form required so the apply session can drop them into the `sources` object without further editorial work.

**Existing sourceIds reused:** `dg-rec-pt1`, `dg-rec-pt2`, `dg-rec-supp`, `three-hundred-years-norman-house` (Hannay 1867), `pettigrew-collectanea-house-gournay-1871`, `planche-conqueror-companions-1874`, `anderson-yvery-1742`, `anderson-yvery-1742-vol-i`, `chronicon-beccensis`, `regesta-rano`, `loyd-origins`, `dudo-historia`, `liber-niger`, `histoire-chronique-normandie-1610`, `dumoulin-histoire-generale-normandie-1631`, `histoire-de-lorraine-calmet`, `wace-roman-de-rou`, `potin-recherches-ville-gournay-1842`, `nrp-recherches-possessions-1852`, `painchault-gaillefontaine-2012`, `delisle-critique-of-dg`, `blomefield-norfolk`, `domesday-1086`, `hop-gurney`, `farrer-honors-knights-fees-v3-gurnay-extracts`, `burke-ancient-family`, `decorde-essai-canton-gournay-1861`.

**Proposed new sourceIds (full JSON in Section 16):**

- `opendomesday-org` — Open Domesday (Anna Powell-Smith / University of Hull) — Domesday Book digital edition with primary-source images and modern transcription.
- `fmg-medlands-normacre` — *Medieval Lands*, Charles Cawley, on the Foundation for Medieval Genealogy site — the gold-standard online encyclopaedia for medieval Norman noble families with primary-source quotations. Already referenced extensively in research companions under this exact handle.
- `pattou-racines-histoire-gournay-2025` — Étienne Pattou, *Seigneurs de Gournay (-en-Bray) & Gurney*, Racines & Histoire chart genealogy, last updated 2025-08-11. Already referenced under this exact handle in research companions.
- `history-of-parliament-online-gurney-1386-1421` — *History of Parliament Online*, Sir John Gurney (d.1408) of Harpley and West Barsham, Norfolk (1386–1421 volume entry). The principal modern scholarly biography of John IV's grandson and the only HoP entry for the line; contains corroboration for Edmund G23 (d. 1387) and his Harpley/Hardingham/Saxthorpe-Loundhall holdings and for John IV (G24) as Edmund's father.
- `wikipedia-en-hamelin-de-warenne` — English Wikipedia, "Hamelin de Warenne, Earl of Surrey" — independent confirmation of Hameline Plantagenet's dates (c. 1130 – 7 May 1202) and half-brother-of-Henry-II identification used in G29 marriage block.
- `wikipedia-fr-famille-de-gournay` — French Wikipedia, "Famille de Gournay" — independent modern-scholarship summary, important for the Delisle critique of DG's early generations.
- `richardson-sgm-soc-genealogy-medieval-2002` — Douglas Richardson, soc.genealogy.medieval Usenet post, 11 September 2002, with revised post archived in Google Groups thread `cPiFbsyHAa8`. The Richardson SGM 2002 position rejects DG's "Walter as son of Gerard" identification; Richardson's pedigree starts from Hugh III (G33) and does not extend the documented chain into the c. 985–860 range. Already referenced under this handle in research companions.

## How to read each section

Each ancestor's block follows the v53 structure:

- **Audit finding** — what this patchset adds or escalates.
- **Proposed edit** — exact find/replace with line-number hint.
- **JSON alignment** — corresponding JSON edit if needed.

---

## 1. G24 — John de Gournay IV (`fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`)

**Audit finding.** Vitals citation chain currently relies exclusively on DG-I p. 286 / DG-II p. 356 / DG-Supp Note 116. Two parity additions are productive:

1. **Blomefield, *Norfolk*, vol. viii, Harpley entry (pp. 452–459).** Already linked from the Related-Links sidebar but not referenced inside the vitals block. The Harpley entry independently records the 9 Edward II (1315/16) fine settling Harpley on John III + Jane (G25) with remainder to William and Edmund (William III's other sons), and records Edmund (G23) presenting in 34 Edward III (1360) and as "lord and patron." Blomefield does *not* name John IV's wife — a confirmed negative search across DG, Blomefield, and HoP Online for this audit pass.
2. **History of Parliament Online**, biography of Sir John Gurney (d.1408), confirms Edmund G23 ("Edmund Gurney d. 1387") inherited Harpley/Hardingham from John IV, and that "the Gurney family had been established in Norfolk since the 12th century." The HoP biography is the principal modern scholarly statement of the late-14th-century descent and corroborates the DG-based G24 → G23 transition without depending on DG.

**Proposed edits.**

**1.1 Citation n2 — strengthen with non-DG parity sources.** Find (line ~119):

```
  <li id="n2">Active 1354 (28 Edw. III). Son Edmund's death: 1387 (Daniel Gurney, <em>Record</em> (1848) p. 279; History of Parliament Online). <a class="citation-back" href="#ref-2">↩</a></li>
```

Replace with:

```
  <li id="n2">Active 1354 (28 Edw. III). Son Edmund's death: 1387, independently corroborated by <em>History of Parliament Online</em>, biography of Sir John Gurney (d.1408) of Harpley and West Barsham, Norfolk (1386–1421 volume): "In 1387 John inherited from his father manors in Harpley and Hardingham as well as 'Loundhall' in Saxthorpe." Available at <a href="https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408">historyofparliamentonline.org/.../gurney-john-1408</a>. Source IDs: <code>dg-rec-pt1</code>, <code>history-of-parliament-online-gurney-1386-1421</code>. <a class="citation-back" href="#ref-2">↩</a></li>
```

**1.2 Citation n4 — formalise the confirmed-negative wife search.** Find:

```
  <li id="n4">No wife named in DG or any other source consulted. <a class="citation-back" href="#ref-4">↩</a></li>
```

Replace with:

```
  <li id="n4">No wife named in any source consulted across this audit pass: Daniel Gurney, <em>Record</em> (1848) and <em>Supplement</em> (1858); Francis Blomefield, <em>Norfolk</em> vol. viii (Harpley entry, pp. 452–459), via British History Online; <em>History of Parliament Online</em>, biography of Sir John Gurney (d.1408) — which names only John IV's mother (Jane de Lexham, G25), his son Edmund (G23), and the descendants. Confirmed negative. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>blomefield-norfolk</code>, <code>history-of-parliament-online-gurney-1386-1421</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

**JSON alignment.** None.

---

## 2. G25 — John de Gournay III (`fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`)

**Audit finding.** The 9 Edward II (1315/16) Blomefield fine — "John de Gournoy [the Rector, collateral] settled it on John de Gournoy [= G25 John III], (son of Catherine,) and Jane his wife, in tail; remainder to William and Edmund, brothers of John, his nephews" — independently corroborates four repo claims at once: (a) John III was *son of Katherine* (her name appears at the structured Blomefield index, matching G26 Sir William III's wife Katherine Baconsthorpe); (b) Jane is John III's wife (the same Jane de Lexham named in DG pedigree p. 286); (c) John III's brothers William and Edmund (collaterals); (d) the Rector planned the family-trust succession to John III *seventeen years before his own 1332 death*. This is significant: it firms up John III's birth as no later than c. 1295 (he was of age to be named in a 1315/16 fine), tightening the current "c. 1300" estimate.

**Proposed edit.**

**2.1 Citation n4 — add Blomefield 9 Edward II fine corroboration.** Find:

```
  <li id="n4">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: "JANE, dau. of Edmund de Lexham, married before 1324, or in that year." <a class="citation-back" href="#ref-4">↩</a></li>
```

Replace with:

```
  <li id="n4">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: "JANE, dau. of Edmund de Lexham, married before 1324, or in that year." Independently confirmed by Blomefield, <em>Norfolk</em> vol. viii (Harpley entry, pp. 452–459), reporting the fine of 9 Edward II (1315/16) in which Rector John "settled it on John de Gournoy, (son of Catherine,) and Jane his wife, in tail; remainder to William and Edmund, brothers of John, his nephews" — naming Jane as wife, Katherine as mother (G26), and William and Edmund as G25's brothers. The 1315/16 date pushes John III's birth no later than c. 1295 (of age to be named in the fine). Available at <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol8/pp452-459">british-history.ac.uk/.../vol8/pp452-459</a>. Source IDs: <code>dg-rec-pt1</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

**2.2 Vitals "Born" cell — tighten birth estimate.** Find (line ~42):

```
    <div class="fact-value">c. 1300, Norfolk. Son of Sir William de Gournay III (G26) and Katherine Baconsthorpe. First attested in a deed of his uncle John (Rector of Harpley) in 1331. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```

Replace with:

```
    <div class="fact-value">c. 1290–1300, Norfolk. Son of Sir William de Gournay III (G26) and Katherine Baconsthorpe. Of age to be named in the 9 Edward II (1315/16) fine in which his uncle John (Rector of Harpley) settled the Harpley estate on him and his wife Jane in tail. First attested by name in 1331 in a deed of the same uncle. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```

2.3 Citation n1 — Add Blomefield 1315/16 fine reference. Find:

```
  <li id="n1">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: "JOHN DE GURNEY, III. heir to his uncle John, Rector of Harpley, presented to that living in 1332; living 27 Edw. III." First attestation: "JOHN GURNAY, Junior, IV [sic — DG's pedigree numbering uses IV here for what the project numbers as John IV; John III is the man who appears in 1331]." Daniel Gurney, <em>Supplement</em> (1858), p. 356: "Son and heir of John de Gurney and Joan his wife, occurs in the deed of John, rector and patron of Harpley, 6th Edward III (1331)." — Note: DG Part II p. 356 uses the numbering "John de Gournay IV" for the man the project JSON numbers as G24; his father (G25 in project JSON) is described as "John de Gurney and Joan his wife." This slight pedigree numbering discrepancy between DG and the project JSON is noted in the Research Appendix. <a class="citation-back" href="#ref-1">↩</a></li>
```

Replace with:

```
  <li id="n1">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: "JOHN DE GURNEY, III. heir to his uncle John, Rector of Harpley, presented to that living in 1332; living 27 Edw. III." Daniel Gurney, <em>Supplement</em> (1858), p. 356: "Son and heir of John de Gurney and Joan his wife, occurs in the deed of John, rector and patron of Harpley, 6th Edward III (1331)." Independently corroborated by Blomefield, <em>Norfolk</em> vol. viii (Harpley entry, pp. 452–459), reporting the fine of 9 Edward II (1315/16): "by a fine levied in the 9th of Edward II. he settled it on John de Gournoy, (son of Catherine,) and Jane his wife, in tail; remainder to William and Edmund, brothers of John, his nephews." The 1315/16 fine pushes John III's birth no later than c. 1295. — Note: DG Part II p. 356 uses the older numbering "John de Gournay IV" for the man the project JSON numbers as G24; his father (G25 in project JSON) is "John de Gurney and Joan his wife." The Jane/Joan first-name variation is preserved across DG (Jane in pedigree, Joan in Supplement) and Blomefield (Jane). Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-1">↩</a></li>
```

**JSON alignment.** None required; JSON G25 `dates` ("fl. c. 1300–1353") remains acceptable; the tightened "c. 1290–1300" birth window is within the existing flouruit range.

---

## 3. G26 — Sir William de Gournay III, Knt. (`fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`)

**Audit finding.** Blomefield's Harpley entry (BHO) also names Catherine ("son of Catherine") in the 9 Edward II fine — independent confirmation of the Baconsthorpe-Katherine marriage for G26. Adding this strengthens the Vitals marriage cell without DG-only reliance and aligns the citation with the Phase-2 FS update.

**Proposed edit.**

**3.1 Citation n4 — add Blomefield corroboration of Katherine.** Find:

```
  <li id="n4">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: "KATHARINE, probably a Baconsthorpe" (for William II's wife); and for William III: "m. Katherine, dau. of Edmund Baconsthorpe." Daniel Gurney, <em>Record</em> (1848), p. 340: confirmed in context of the arms discussion. <a class="citation-back" href="#ref-4">↩</a></li>
```

Replace with:

```
  <li id="n4">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: for William III, "m. Katherine, dau. of Edmund Baconsthorpe." DG p. 340: confirmed in context of the arms discussion. Independently corroborated by Blomefield, <em>Norfolk</em> vol. viii (Harpley entry, pp. 452–459) via British History Online: the 9 Edward II (1315/16) fine identifies John III (G25) as "(son of Catherine,)" — naming William III's wife at the structured pedigree level. Source IDs: <code>dg-rec-pt1</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

**JSON alignment.** None.

---

## 4. G27 — Sir John de Gournay I, Knt. (`fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`)

**Audit finding.** Existing fact-sheet relies on DG-I, DG-Supp, and the citation chain Roll of Arms + Patent Rolls + Rotuli Hundredorum. The Anderson 1742 trial-by-battle bullet is being added in v53 §4.1. Two additional parity-level escalations are productive in v54:

1. **Farrer, *Honors and Knights' Fees* vol. 3, Honor of Arundel, p. 142.** Already referenced in the G27 research companion under sourceId `farrer-honors-knights-fees-v3-gurnay-extracts`. Farrer independently records the South Wootton 1265 seizure ("John de Gurney was in the conflict of Evesham against the king") as a separate primary-source corroboration of DG-Supp Note 112 (Lewes plea). The vitals don't need touching; Highlights bullet 1 (Lewes/Evesham) should be re-cited.

**Proposed edit.**

**4.1 Citation n5 — add Farrer to South Wootton/Evesham bullet.** Find (line ~129):

```
  <li id="n5">Daniel Gurney, <em>Record</em> (1848), p. 279: "who was in rebellion against Henry III. and present at the battle of Lewes in 1264 ... and Evesham, and forfeited the manor of South Wootton, in Norfolk, in consequence." Daniel Gurney, <em>Record</em> (1848) Appendix LXI, p. 341 (Supplement): "Sir John de Gourney, who had been in arms against Henry III. at the battle of Lewes, was in the same crusade." <a class="citation-back" href="#ref-5">↩</a></li>
```

Replace with:

```
  <li id="n5">Daniel Gurney, <em>Record</em> (1848), p. 279, and Appendix LXI p. 341. DG-Supp Note 112 (pp. 781–783): full Latin text of the 1264/65 plea (Placita coram Rege, 49 Henry III, No. 124): "<em>quia idem Johannes fuit in conflictu de Lewes contra dominum Regem et alibi post eundem conflictum</em>" — John de Gurney was in the conflict of Lewes against the lord King and elsewhere after the same conflict. Independently corroborated by William Farrer, <em>Honors and Knights' Fees</em>, vol. 3 (1923–25), Honor of Arundel, p. 142, which records that John de Bulemer answered Alice de Balesham (1265) that he had seized John de Gurney's manor at South Wootton because John "was in the conflict of Evesham against the king" — naming Evesham where DG's longer plea emphasises Lewes plus post-Lewes resistance. Together the two attestations document the same rebel arc from Lewes 1264 through post-Evesham forfeiture. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>farrer-honors-knights-fees-v3-gurnay-extracts</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

**JSON alignment.** None.

---

## 5. G28 — Sir William de Gournay II, Knt. (`fact-sheets/g28-william-de-gournay-ii-fact-sheet.md`)

**Audit finding.** No new non-DG parity source surfaced in this audit pass beyond what v53 already proposed. Anderson 1742 vol. II p. 478 mentions a Matthew "in the Time of Henry the First" with sons Thomas and William — research companion treats this as compatible-but-too-early; not adopted into vitals. No edit beyond v53.

**No edit proposed in v54.**

---

## 6. G29 — Sir Matthew de Gournay, Knt. (`fact-sheets/g29-matthew-de-gournay-fact-sheet.md`)

**Audit finding.** The fact-sheet's Marriage cell narrates Hamelin Earl Warren personally arranging Matthew's marriage to Rose de Burnham c. 1183, citing DG (n5) and Wikipedia (Related Links sidebar). The Wikipedia article *Hamelin de Warenne, Earl of Surrey* gives concrete dates (c. 1130 – 7 May 1202) and confirms he was an illegitimate son of Count Geoffrey of Anjou and elder half-brother of Henry II — and that he married Isabel de Warenne, 4th Countess of Surrey, in April 1164 (not 1164 as a different year). This is parity-level corroboration of the marriage-arranger statement.

**Proposed edit.**

**6.1 Citation n5 — add Wikipedia parity source.** Find:

```
  <li id="n5">DG-I, pp. 278–279: "To this Matthew de Gournay Hameline Earl Warren gave in marriage Rose, daughter and heir of Reginald de Burnham, his kinsman, about the year 1183 ... by this marriage Matthew de Gournay acquired Gurney's manor in Harpley and other estates." Hameline Plantagenet, Earl Warren (c. 1130–1202): illegitimate son of Geoffrey of Anjou (father of Henry II); married Isabella de Warenne 1164. <a class="citation-back" href="#ref-5">↩</a></li>
```

Replace with:

```
  <li id="n5">Daniel Gurney, <em>Record</em> (1848), pp. 278–279: "To this Matthew de Gournay Hameline Earl Warren gave in marriage Rose, daughter and heir of Reginald de Burnham, his kinsman, about the year 1183 ... by this marriage Matthew de Gournay acquired Gurney's manor in Harpley and other estates." Independently corroborated by Blomefield, <em>Norfolk</em> vol. viii (Harpley): "Rose, who was given in marriage by Hameline Planlaginet Earl Warren ... to Matthew de Gurney, who was lord in her right, about the 30th of Henry II." Hameline Plantagenet's dates and Plantagenet kinship per English Wikipedia, "Hamelin de Warenne, Earl of Surrey": c. 1130 – 7 May 1202; illegitimate son of Count Geoffrey of Anjou; elder half-brother of King Henry II; married Isabel de Warenne, 4th Countess of Surrey, April 1164. Source IDs: <code>dg-rec-pt1</code>, <code>blomefield-norfolk</code>, <code>wikipedia-en-hamelin-de-warenne</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

**6.2 Highlights bullet 1 ("Harpley enters the family through a royal marriage-gift").** No edit to bullet body. Citation n5 update above flows through.

**JSON alignment.** None.

---

## 7. G30 — Sir William de Gournay I, Knt. (`fact-sheets/g30-william-de-gournay-i-fact-sheet.md`)

**Audit finding.** Vitals citation chain is DG-only. The research companion documents the *Liber Niger Scaccarii* and *Registres Olim* as parity-level primary sources (FMG MedLands and Beugnot's 1839 edition of the *Olim*). The citation n5 currently cites these via DG. Direct reference to the *Liber Niger* via its existing sourceId (`liber-niger`) is a low-cost improvement.

**Proposed edit.**

**7.1 Citation n5 — promote *Liber Niger* sourceId to first-citation alignment.** Find:

```
  <li id="n5">DG-I, p. 278: "William de Gournay having held this Norman manor in capite, forms, therefore, an incontestable proof of his descent in blood from the Barons of Gournay." *Registres Olim, par Le Comte de Beugnot, Paris, 1839* cited by DG. Parage: DG-I, Appendix XLVI. <a class="citation-back" href="#ref-5">↩</a></li>
```

Replace with:

```
  <li id="n5">Daniel Gurney, <em>Record</em> (1848), p. 278: "William de Gournay having held this Norman manor in capite, forms, therefore, an incontestable proof of his descent in blood from the Barons of Gournay." Primary-source anchor: <em>Registres Olim</em>, ed. Le Comte de Beugnot, Paris, 1839, cited by DG; this is the registry of the French royal court (Curia Regis / Parlement) that formally recognised the junior Norfolk Gournays as legitimate descendants of the Lords of Gournay. The parage tenure regime is itself documented in the <em>Liber Niger Scaccarii</em> (Source ID: <code>liber-niger</code>), and the tenure principle is laid out in DG-I, Appendix XLVI. Source IDs: <code>dg-rec-pt1</code>, <code>liber-niger</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

**JSON alignment.** None.

---

## 8. G31 — Walter de Gournay (`fact-sheets/g31-walter-de-gournay-fact-sheet.md`)

**Audit finding.** The most important non-DG finding for this generation is **the existence of a credible competing identification of Walter that the fact sheet does not currently surface in the citation list**. The research companion §3.1 documents three positions: (1) DG / Pettigrew / NRP-I / Geni — Walter is son of Gerard; (2) Pattou — Walter "possible petit-fils" (grandson); (3) Richardson SGM 2002 — Walter is unrelated to the senior Norman line. Position 3 is structurally independent of the local-Gournay-antiquarian tradition behind positions 1 and 2 and draws on English-side feudal evidence (Hasted vol. 4, Copinger vol. 3, Loyd & Stenton, *VCH Essex* vol. 4, *Genealogist* vol. 15, etc.). The repo's adoption of position 1 is documented as a *conscious editorial choice* in the case file `research/case-files/walter-de-gournay-as-son-of-gerard.md`. The fact sheet's citation n5 frames Walter's Gerard-descent as "DG-I, p. 277" without surfacing the dispute.

The fact-sheet *narrative* paragraph 2 calls the descent "incontestable proof" — a phrase that captures DG's confidence but elides Richardson's contrary view. Best practice: cite the case file from the existing footnote so a reader (or a FS reviewer) sees the dispute exists.

**Proposed edit.**

**8.1 Citation n8 — add case-file pointer and Richardson-SGM-2002 acknowledgment.** Find:

```
  <li id="n8">DG-I, pp. 277–278 and pedigree p. 286. <a class="citation-back" href="#ref-8">↩</a></li>
```

Replace with:

```
  <li id="n8">Daniel Gurney, <em>Record</em> (1848), pp. 277–278 and pedigree p. 286. The repo's adoption of DG's "Walter as son of Gerard" identification is a conscious editorial choice; an independent line of modern scholarship — most fully argued by Douglas Richardson, soc.genealogy.medieval, 11 September 2002 (Google Groups thread <code>cPiFbsyHAa8</code>), drawing on Hasted vol. 4, Copinger <em>Manors of Suffolk</em> vol. 3, Loyd & Stenton <em>Hatton Book of Seals</em>, <em>VCH Essex</em> vol. 4, and <em>Genealogist</em> vol. 15 — rejects the Gerard-paternity identification on English-side feudal evidence. The full case is at <code>research/case-files/walter-de-gournay-as-son-of-gerard.md</code>. Source IDs: <code>dg-rec-pt1</code>, <code>richardson-sgm-soc-genealogy-medieval-2002</code>. <a class="citation-back" href="#ref-8">↩</a></li>
```

**JSON alignment.** None.

---

## 9. G32 — Gerard de Gournay (`fact-sheets/g32-gerard-de-gournay-fact-sheet.md`)

**Audit finding.** The fact sheet relies on DG-I for the Edith-de-Warenne marriage. Independent corroboration of Edith's identity is supplied by Guillaume of Jumièges (FMG [886]): "Giraldus ... cum uxore sua Edithua sorore Willelmi comitis de Warenna" — Edith was the sister of William II de Warenne (2nd Earl of Surrey), which is consistent with the fact-sheet's "daughter of William de Warenne, 1st Earl of Surrey." Promoting Guillaume of Jumièges and FMG MedLands to citation-level visibility on the marriage cell strengthens the non-DG anchor.

Additionally: the fact-sheet's narrative paragraph 2 still carries the older Warren-charters claim that Edith was a granddaughter of William the Conqueror through his daughter Gundred. Modern scholarship (Wikipedia, Pattou, FMG) identifies Edith's mother Gundred as *sister of Gerbod the Fleming, Earl of Chester* — not a daughter of the Conqueror. The fact-sheet's Marriage cell already hedges this ("though some modern historians dispute this descent"), but the citation chain leans on DG. Adding the modern-scholarship sources to citation n4 brings non-DG parity.

**Proposed edits.**

**9.1 Citation n4 — add FMG MedLands and Wikipedia parity.** Find:

```
  <li id="n4">DG-I, p. 27: marriage and Warenne connection. DG-Supp Note 16 (p. 735): Gerard's seal — "Signum Girardi de Gornaco" — in the Cartulary of La Trinité de Rouen (ed. Deville, Tome III, Charter No. 94). The Conqueror-descent claim via Gundred is documented in the Warren charters but disputed by modern historians. <a class="citation-back" href="#ref-4">↩</a></li>
```

Replace with:

```
  <li id="n4">Daniel Gurney, <em>Record</em> (1848), p. 27: marriage and Warenne connection. DG-Supp Note 16 (p. 735): Gerard's seal — "Signum Girardi de Gornaco" — in the Cartulary of La Trinité de Rouen (ed. Deville, Tome III, Charter No. 94). Independently confirmed by Guillaume de Jumièges, <em>Historia Normannorum</em>, Liber VIII §VIII (Duchesne ed. 1619, p. 296): "Giraldus tandem Hierusalem petens cum uxore sua Edithua sorore Willelmi comitis de Warenna" — naming Edith as sister of William (II) de Warenne, the second earl, i.e., daughter of William I, 1st Earl, by his first wife Gundred. FMG MedLands (Cawley) Normandy section under "Seigneurs de Gournay" cross-references this passage. The Conqueror-descent claim via Gundred is found in the Warren charters but is rejected by modern scholarship: English Wikipedia, "Gundred, Countess of Surrey," and Pattou, <em>Racines Histoire</em>, both identify Gundred as sister of Gerbod the Fleming, 1st Earl of Chester, not a daughter of William the Conqueror. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>fmg-medlands-normacre</code>, <code>pattou-racines-histoire-gournay-2025</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

**9.2 Citation n5 — surface Orderic / Albert of Aix / Baudry of Dol on the Crusade.** Find:

```
  <li id="n5">First Crusade 1096–1099: preached at <a href="https://en.wikipedia.org/wiki/Council_of_Clermont">Clermont</a> 1095; Jerusalem captured 15 July 1099. DG-I, p. 27 for Gerard's crusade. Three independent crusade-chronicle attestations (FMG MedLands [882]–[884]): Albert of Aix names "Gerardus de Gorna" at the siege of Nicaea (mid-1097); Baudry of Dol names "Girardus de Gornaio" among 1097 crusaders; Guillaume of Jumièges records that "Giraldus" left for Jerusalem and died on the journey. The 1104 *terminus post quem* for the death is secured by the St-Sauveur en Cotentin cartulary roll (DG 1845 p. 69, then in M. de Gerville's possession at Valognes). Second pilgrimage and death: "*Hierosolymam petens in ipso itinere mortuus est*." <a class="citation-back" href="#ref-5">↩</a></li>
```

Replace with:

```
  <li id="n5">First Crusade 1096–1099 (preached at Clermont 1095; Jerusalem captured 15 July 1099). Three independent crusade-chronicle attestations preserved in FMG MedLands [882]–[884]: (a) Albert of Aix, <em>Historia Hierosolymitana</em>, Liber II Cap. XXIII, names "Gerardus de Gorna" at the siege of Nicaea (mid-1097); (b) Baudry of Dol names "Girardus de Gornaio" among the 1097 crusaders (<em>Recueil des historiens des croisades</em>, II.I, p. 33); (c) Guillaume de Jumièges, <em>Historia Normannorum</em>, Liber VIII §VIII, records that "Giraldus" left for Jerusalem and died on the journey. The 1104 <em>terminus post quem</em> for the death is secured by the St-Sauveur en Cotentin cartulary roll (Daniel Gurney, <em>Record</em> (1845) p. 69, then in M. de Gerville's possession at Valognes). Second pilgrimage and death: "<em>Hierosolymam petens in ipso itinere mortuus est</em>" (Guillaume de Jumièges, same passage). Source IDs: <code>fmg-medlands-normacre</code>, <code>dg-rec-pt1</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

**9.3 Citation n6 — surface Orderic for the 1089/90 castle-delivery moment.** Find:

```
  <li id="n6">Orderic Vitalis (FMG MedLands [879], citing Orderic ed. Prévost vol. III, Liber VIII §IX, p. 319): "Gornacensis Girardus" delivered "Gornacum et Firmitatem et Goisleni Fontem" [Gournay, La Ferté-en-Bray, Gaillefontaine] to William II Rufus, dated [1089/90]. DG-Supp Note 17 (pp. 735–736): St. Wandrille charter — full Latin text, with Gerard's consent required (*annuente Girardo de Gournai*). DG-Supp Note 18 (p. 736): the Breteuil dispute, from Évreux MS. 132 (c. 1125 miracles treatise). Hannay, p. 107: "unsafe man to meddle with." Painchault, Aude, "Gaillefontaine (Seine-Maritime) : approche topographique d'une fortification du Pays de Bray," in *Journées archéologiques de Haute-Normandie*. Évreux 6-8 mai 2011, PURH, 2012, pp. 209–218 — modern archaeological framing of the coordinated Gournay-La Ferté-Gaillefontaine fortification triad at the head of the Bresle valley. <a class="citation-back" href="#ref-6">↩</a></li>
```

Replace with:

```
  <li id="n6">Orderic Vitalis, <em>Historia Ecclesiastica</em>, ed. Prévost (1838–1855) vol. III, Liber VIII §IX, p. 319, preserved verbatim in FMG MedLands [879]: "Gornacensis Girardus" delivered "Gornacum et Firmitatem et Goisleni Fontem" [Gournay, La Ferté-en-Bray, Gaillefontaine] to William II Rufus, dated to [1089/90]. The Évreux–Conches private war is recorded in the same source. Daniel Gurney, <em>Supplement</em> (1858) Note 17 (pp. 735–736): St-Wandrille charter — full Latin text, with Gerard's consent required ("<em>annuente Girardo de Gournai</em>"). Daniel Gurney, <em>Supplement</em> (1858) Note 18 (p. 736): the Breteuil-Pont-Saint-Pierre dispute, from Évreux MS. 132 (c. 1125 St Nicholas miracles treatise). James Hannay, <em>Three Hundred Years</em> (1867), p. 107: "unsafe man to meddle with." Aude Painchault, "Gaillefontaine (Seine-Maritime) : approche topographique d'une fortification du Pays de Bray," in <em>Journées archéologiques de Haute-Normandie</em>, Évreux 6–8 mai 2011, PURH 2012, pp. 209–218 — modern archaeological framing of the coordinated Gournay–La Ferté–Gaillefontaine fortification triad at the head of the Bresle valley. Source IDs: <code>fmg-medlands-normacre</code>, <code>dg-rec-supp</code>, <code>three-hundred-years-norman-house</code>, <code>painchault-gaillefontaine-2012</code>. <a class="citation-back" href="#ref-6">↩</a></li>
```

**JSON alignment.** None.

---

## 10. G33 — Hugh de Gournay III (`fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`)

**Audit finding.** Domesday Book is cited in the fact sheet (n10) but only via DG-I p. 27 and Morant's *Essex*. The repo lists `domesday-1086` as a sourceId. Open Domesday (Anna Powell-Smith / University of Hull) provides verbatim modern transcriptions of the Liston, Fordham, and Ardleigh entries with primary-source image links. Promoting Open Domesday to citation visibility gives the FS reviewer a direct primary-source anchor.

The Liston Wikipedia article independently confirms: "At the time of the Domesday, Liston had two manors, one in the hands of Ilbod brother of Arnulf of Hesdin, the other had as Tenant-in-Chief, Hugh of Gournay with the Lord being Geoffrey Talbot." Non-DG parity for the Geoffrey-Talbot-as-sub-tenant claim — currently in the fact-sheet text without a non-DG citation.

**Proposed edits.**

**10.1 Citation n10 — promote Open Domesday and Wikipedia parity.** Find:

```
  <li id="n10">Domesday Book (1086): Liston, Fordham, Ardleigh — all in Essex. DG-I, p. 27. Verified via Open Domesday (opendomesday.org), Little Domesday vol. ii, p. 89. 1076 Bec charter: DG-Supp Note 13 (pp. 732–734), from the *Paris MS. Histoire des Seigneurs de Gournay*, recording the Cartulaire du Bec: tithes of "Fordham, Listhone, et Arlie" given by Hugh to Bec with patronage rights. <a class="citation-back" href="#ref-10">↩</a></li>
```

Replace with:

```
  <li id="n10">Domesday Book (1086): Liston, Fordham, Ardleigh — all held in Essex by tenant-in-chief Hugh of Gournai. Verified entries via Open Domesday (Anna Powell-Smith / University of Hull): Liston (sub-tenant Geoffrey Talbot), Fordham, Ardleigh; see <a href="https://opendomesday.org/place/TL9228/fordham/">opendomesday.org/place/TL9228/fordham/</a> and the cross-referenced Essex entries. Independently corroborated in summary by English Wikipedia, "Liston, Essex": "the other had as Tenant-in-Chief, Hugh of Gournay with the Lord being Geoffrey Talbot." Original source: Little Domesday vol. ii, p. 89. Pre-Domesday attestation: 1076 Bec charter, DG-Supp Note 13 (pp. 732–734), from the <em>Paris MS. Histoire des Seigneurs de Gournay</em> recording the Cartulaire du Bec — tithes of "Fordham, Listhone, et Arlie" given by Hugh to Bec with patronage rights. Source IDs: <code>domesday-1086</code>, <code>opendomesday-org</code>, <code>dg-rec-supp</code>. <a class="citation-back" href="#ref-10">↩</a></li>
```

**10.2 Citation n2 — surface Potin 1842 / Pattou parity for the 1110 death year.** Find:

```
  <li id="n2">Death in 1110 per Pierre Potin de la Mairie, *Recherches historiques sur la ville de Gournay-en-Bray* (1842), p. 110: *"Le Hugues que nous nommons Hugues III, mourut en 1110, moine à l'abbaye du Bec."* The repo's earlier "c. 1093" date was DG's reading of "shorn a monk before 1093"; both data points are reconciled by treating 1080 as the year he entered Bec, 1092 as the year he became Prior of Saint-Nicaise de Meulan in succession to Guillaume de Montfort (Pattou *Racines Histoire* p. 2; Potin 1842 p. 109), and 1110 as the year of his death. The "Hugo Senex" epithet earlier attached to this fact sheet has been moved to G34 (Hugh II), where Wace's *Roman de Rou* T. 2 verse "*Et li vieil Hue de Gornai / Ensemble o li sa gent de Brai*" places it. <a class="citation-back" href="#ref-2">↩</a></li>
```

Replace with:

```
  <li id="n2">Death in 1110 per Pierre Potin de la Mairie, <em>Recherches historiques sur la ville de Gournay-en-Bray</em> (1842), p. 110: "<em>Le Hugues que nous nommons Hugues III, mourut en 1110, moine à l'abbaye du Bec.</em>" Independently endorsed by Étienne Pattou, <em>Racines Histoire</em> "Seigneurs de Gournay (-en-Bray) & Gurney" (last updated 2025-08-11), p. 2; Douglas Richardson, <em>Royal Ancestry</em> vol. III (via ThePeerage and TNG); and the FamilySearch-tracked PID `MZ68-VKD` lineage chain. The repo's earlier "c. 1093" date was DG-I's reading of "shorn a monk before 1093"; both data points are reconciled by treating 1080 as the year he entered Bec, 1092 as the year he became Prior of Saint-Nicaise de Meulan in succession to Guillaume de Montfort (Pattou p. 2; Potin 1842 p. 109), and 1110 as the year of his death. The "Hugo Senex" epithet earlier attached to this fact sheet has been moved to G34 (Hugh II), where Wace's <em>Roman de Rou</em> T. 2 verse "<em>Et li vieil Hue de Gornai / Ensemble o li sa gent de Brai</em>" places it. Source IDs: <code>potin-recherches-ville-gournay-1842</code>, <code>pattou-racines-histoire-gournay-2025</code>, <code>dg-rec-pt1</code>. <a class="citation-back" href="#ref-2">↩</a></li>
```

**JSON alignment.** None (the JSON already has `"dates": "c. 1020 — d. 1110"`).

---

## 11. G34 — Hugh de Gournay II (`fact-sheets/g34-hugh-de-gournay-ii-fact-sheet.md`)

**Audit finding.** The 1067 Vaudreuil charter (D. Martene, *Thesaurus Anecdotorum* t. i c. 196) is cited in n7. The pre-1066 *Liber niger capituli Baiocensis* charter (No. 5) granting Bernières to Odo is also cited. These are both genuine primary sources; the citation chain currently goes through DG-Supp Note 9. Adding FMG MedLands' parity citation (FMG [890] for the [1060] Bayeux "Brenerias" charter, FMG [895] for the 1067 Saint-Benoît-sur-Loire confirmation) increases the non-DG anchoring.

**Proposed edit.**

**11.1 Citation n7 — promote FMG MedLands parity for the charter witnesses.** Find:

```
  <li id="n7">DG-Supp Note 9 (p. 731): Two specific charter references. (1) Charter of April 1067, dated at Vaudreuil, in favour of the priory of Saint-James: "Signum Hugonis de Gornaii." Source: D. Martene, <em>Thesaurus Anecdotorum</em>, t. i, c. 196. (2) Pre-1066 charter granting land of Bernières to Odo, Bishop of Bayeux: "Hugo de Gornai" as witness. Source: <em>Liber niger capituli Baiocensis</em>, No. 5, 13th-century MS., Bayeux Cathedral library. <a class="citation-back" href="#ref-7">↩</a></li>
```

Replace with:

```
  <li id="n7">Four documented ducal-charter witness appearances spanning Hugh II's life:
  (1) <strong>Before 1066, Bernières to Odo, Bishop of Bayeux</strong>: "Hugo de Gornai" witness in the <em>Liber niger capituli Baiocensis</em>, No. 5, 13th-century MS. preserved in the Bayeux Cathedral library. Cited in Daniel Gurney, <em>Supplement</em> (1858) Note 9, p. 731.
  (2) <strong>[1060] Bayeux "Brenerias" charter</strong>: "Hugo de Gornai" witness, "Brenerias" granted to the abbey of Bayeux, dated to [1060]. FMG MedLands [890]. This may be the same act as (1) under a different orthography ("Brenerias" ~ "Bernières"); resolution requires Marie Fauroux, <em>Recueil des actes des ducs de Normandie de 911 à 1066</em> (Caen 1961) index check, not yet executed.
  (3) <strong>1067 Saint-Benoît-sur-Loire confirmation</strong>: "Hugonis de Gornaio" subscribed William's April 1067 confirmation of abbey rights to Saint-Benoît-sur-Loire. FMG MedLands [895].
  (4) <strong>April 1067, Vaudreuil charter to the priory of Saint-James</strong>: "Signum Hugonis de Gornaii." D. Martene, <em>Thesaurus Anecdotorum</em>, t. i, c. 196. Cited in Daniel Gurney, <em>Supplement</em> (1858) Note 9, p. 731.
  Together the four place Hugh in the inner circle of ducal governance from before the Conquest through into the spring of 1067. Source IDs: <code>dg-rec-supp</code>, <code>fmg-medlands-normacre</code>. <a class="citation-back" href="#ref-7">↩</a></li>
```

**11.2 Citation n6 — surface Potin's parallel chronicles for the 1035 expedition.** Find:

```
  <li id="n6">1035 expedition: Hannay, pp. 69–70; Pierre Potin de la Mairie, *Recherches historiques sur la ville de Gournay-en-Bray* (1842), pp. 94–95, juxtaposing two parallel chronicle versions: l'*Histoire et Chronique de Normandie* (printed Rouen 1610) ff. 79–80, and Gabriel Dumoulin, *Histoire générale de Normandie* (1631) p. 153. FMG MedLands [888] cites the *Chronique Manuscrite de Normandie*. Hannay, pp. 70–71: Hugh described as *Hugo Miles* before 1035. <a class="citation-back" href="#ref-6">↩</a></li>
```

Replace with:

```
  <li id="n6">The 1035 expedition is recorded in three independent chronicle traditions, all in dialogue: (a) l'<em>Histoire et Chronique de Normandie</em> (printed Rouen 1610), ff. 79–80 (Source ID: <code>histoire-chronique-normandie-1610</code>); (b) Gabriel Dumoulin, <em>Histoire générale de Normandie</em> (1631), p. 153 (Source ID: <code>dumoulin-histoire-generale-normandie-1631</code>); (c) the <em>Chronique Manuscrite de Normandie</em> as cited at FMG MedLands [888] (Source ID: <code>fmg-medlands-normacre</code>). The three versions are juxtaposed in Pierre Potin de la Mairie, <em>Recherches historiques sur la ville de Gournay-en-Bray</em> (1842) pp. 94–95 (Source ID: <code>potin-recherches-ville-gournay-1842</code>). James Hannay, <em>Three Hundred Years of a Norman House</em> (1867) pp. 69–71 records Hugh as <em>Hugo Miles</em> in a pre-1035 charter (Source ID: <code>three-hundred-years-norman-house</code>). The composite list of fleet captains: Walter Giffard Count of Longueville, Néel Vicomte of the Cotentin, Robert Count of Mortain "Taillefer," the lord of Guérarville, and the lord of Gournay (Hugh II). <a class="citation-back" href="#ref-6">↩</a></li>
```

**JSON alignment.** None.

---

## 12. G35 — Renaud de Gournay (`fact-sheets/g35-renaud-de-gournay-fact-sheet.md`)

**Audit finding.** Citation n5 already references FMG MedLands [884]/[885] for the La Ferté charter. **Add explicit FMG sourceId tag**, and add NRP-I 1852 / Pattou as parity confirmations for the 989–996 dating window. Most of the existing citation text is appropriate; the upgrade is purely citation-handle promotion.

**Proposed edit.**

**12.1 Citation n5 — promote NRP-I / Pattou / FMG as explicit Source IDs.** Find:

```
  <li id="n5">DG-I, p. 25; DG-Supp Note 8 p. 731 (Delisle's confirmation that the original charter is not in the Évreux archives); FMG MedLands [884]/[885] explicitly notes the original charter no longer exists. NRP-I 1852 p. 77–78 gives the fuller witness list: Richard I; Richard II; Robert Archbishop of Rouen; an unnamed Count Robert; and the dedicating Bishop Hugues, who consecrated the priory under the name of Saints Peter and Paul. Pattou (*Racines Histoire* p. 2) hedges with "ou cette fondation peut-être légèrement antérieure à 1026 sous Richard II?" but the dual presence of Richard I and Archbishop Robert ties the foundation to 989–996. <a class="citation-back" href="#ref-5">↩</a></li>
```

Replace with:

```
  <li id="n5">The la Ferté priory foundation charter [989/96] is the primary attestation for Renaud and his wife Alberade. The original is lost; the charter survives only in transcription via M. de Gondeville's MS <em>Histoire de Gournay</em>. Léopold Delisle (DG-Supp Note 8 p. 731) confirmed the original is not in the Évreux archives. Daniel Gurney, <em>Record</em> (1845), p. 25 (Source ID: <code>dg-rec-pt1</code>); FMG MedLands [884]/[885] (Source ID: <code>fmg-medlands-normacre</code>); N.-R. P. de la Mairie, <em>Recherches…sur les Possessions des Sires Normands de Gournay</em>, Tome I (1852), pp. 77–78 (Source ID: <code>nrp-recherches-possessions-1852</code>) — give the fuller witness list: Richard I, Duke of Normandy (d. 996); his son Richard II; Robert, Archbishop of Rouen (appointed 989); a Count also named Robert (distinct from the Archbishop); and a dedicating Bishop Hugues, who consecrated the priory under Saints Peter and Paul. The dual presence of Richard I and Archbishop Robert brackets the date to 989–996. Étienne Pattou, <em>Racines Histoire</em> "Seigneurs de Gournay" p. 2 (Source ID: <code>pattou-racines-histoire-gournay-2025</code>) hedges with "ou cette fondation peut-être légèrement antérieure à 1026 sous Richard II?" but the bracketed witness window is the better-supported reading. <a class="citation-back" href="#ref-5">↩</a></li>
```

**12.2 Citation n7 (numbered for the new G34/G36 numbering footnote).** Building on v53 §12.1's children-table row 1 re-label, add a footnote elaborating the FMG-vs-repo numbering offset for future readers consulting FMG. After n7 (line ~138), insert a new note:

```
  <li id="n7b">The repo numbering G34 = "Hugh II" follows DG's pedigree p. 286 numbering and represents the second Lord of Gournay called Hugh: the Mortemer (1054) commander and Hastings (1066) "Le Vieil Huon." FMG MedLands (Cawley) Normandy section labels the same person "Hugues [I] de Gournay (-after 989)" because FMG's numbering excludes the earlier traditional Hugh (the fortifier, who in repo numbering is G36). The offset propagates one generation through subsequent Hughs (FMG's Hugues II = repo G33 = the Bec monk; FMG's Hugues III = repo G33, etc., subject to source-by-source verification). Readers cross-referencing FMG should add 1 to repo numbering to match FMG numbering at the Hugh-name level. <a class="citation-back" href="#ref-7b">↩</a></li>
```

And update the children-table row 1 footnote ref to point at `n7b` instead of `n7`. **At apply time the applier may consolidate the new note into the existing `n7` body if preferred; either pattern works.**

**JSON alignment.** None.

---

## 13. G36 — Hugh de Gournay I (`fact-sheets/g36-hugh-de-gournay-i-fact-sheet.md`)

**Audit finding.** Citation n7 references William Brito's *Philippide* lib. xi (c. 1224) for the citadel and tower description. The standard published edition is Delaborde, *Oeuvres de Rigord et de Guillaume le Breton* (Paris 1882–1885), 2 vols. — the research companion §2.1 already records this. Adding the Delaborde edition reference to n5 (the fortification citation) is a non-DG parity improvement.

**Proposed edit.**

**13.1 Citation n5 — surface Brito Delaborde edition.** Find:

```
  <li id="n5">DG-I, p. 24, citing William Brito (Guillaume le Breton) *Philippide* lib. xi (c. 1224): the citadel was "surrounded by a triple wall and a double ditch which rendered it inaccessible, and fortified with a tower called after him, 'La Tour Hue.'" The fullest local-tradition account is in Pierre Potin de la Mairie, *Recherches historiques sur la ville de Gournay-en-Bray* (1842), pp. 75–81, drawing on Père du Plessis's *Description de la Haute Normandie* and Nicolas Cordier's MS *Histoire de Gournay* (c. 1710–1738). Survival: Potin 1842 places the demolition "au commencement du siècle dernier" (early 1700s); DG-Supp Note 7 (p. 730, 1858) places it "a century ago" (= c. 1750s) — the two dates bracket an early-to-mid-18th-century final demolition. Painchault, *Gaillefontaine* (PURH 2012), frames Gournay-La Ferté-Gaillefontaine as a coordinated frontier-fortification triad at the head of the Bresle valley. <a class="citation-back" href="#ref-5">↩</a></li>
```

Replace with:

```
  <li id="n5">William Brito (Guillaume le Breton), <em>Philippide</em>, Liber xi (c. 1224), standard edition Delaborde, <em>Oeuvres de Rigord et de Guillaume le Breton</em>, 2 vols. (Paris 1882–1885): describes the Gournay citadel as "<em>munitum triplice muro … inexpugnabilis</em>" — surrounded by a triple wall and double ditch, inaccessible, fortified with a tower "La Tour Hue." Daniel Gurney, <em>Record</em> (1848) p. 24 quotes the verse. The fullest local-tradition account is in Pierre Potin de la Mairie, <em>Recherches historiques sur la ville de Gournay-en-Bray</em> (1842) pp. 75–81 (Source ID: <code>potin-recherches-ville-gournay-1842</code>), drawing on Père du Plessis's <em>Description de la Haute Normandie</em> and Nicolas Cordier's MS <em>Histoire de Gournay</em> (c. 1710–1738). Survival: Potin 1842 places the demolition "<em>au commencement du siècle dernier</em>" (early 1700s); DG-Supp Note 7 (p. 730, 1858) places it "a century ago" (= c. 1750s) — the two dates bracket an early-to-mid-18th-century final demolition. Aude Painchault, <em>Gaillefontaine</em> (PURH 2012), Source ID: <code>painchault-gaillefontaine-2012</code>, frames Gournay–La Ferté–Gaillefontaine as a coordinated frontier-fortification triad at the head of the Bresle valley. <a class="citation-back" href="#ref-5">↩</a></li>
```

**JSON alignment.** None.

---

## 14. G37 — Eudes (Odon) de Gournay (`fact-sheets/g37-eudes-de-gournay-fact-sheet.md`)

**Audit finding.** The existing citation chain is already balanced between DG, Hannay, Pattou, Potin, and Dudo of Saint-Quentin. The principal parity addition is **explicit Source ID tagging** of the existing references rather than substantive new findings.

**Proposed edit.**

**14.1 Citation n3 — promote Dudo and modern-scholarship reassessment to Source IDs.** Find:

```
  <li id="n3">On Rollo's treaty stipulation requiring baptism of his followers: DG-I, Preface, pp. 3–4. The "funiculo divisit" quotation from Dudo of Saint-Quentin (c. 996–1015) is in Hannay, <em>Three Hundred Years of a Norman House</em> (1867), p. 34 [hereafter Hannay]. Modern scholars have progressively reassessed Dudo's reliability: his chronicle is propaganda, not neutral history, but the land-division tradition is broadly accepted. <a class="citation-back" href="#ref-3">↩</a></li>
```

Replace with:

```
  <li id="n3">Rollo's treaty stipulation requiring baptism of his followers: Daniel Gurney, <em>Record</em> (1848), Preface, pp. 3–4 (Source ID: <code>dg-rec-pt1</code>). The "<em>terram fidelibus suis funiculo divisit</em>" land-division quotation is from Dudo of Saint-Quentin, <em>De moribus et actis primorum Normanniae ducum</em> (c. 996–1015), ed. Lair Caen 1865; English translation Christiansen, Boydell 1998 (Source ID: <code>dudo-historia</code>); cited at James Hannay, <em>Three Hundred Years of a Norman House</em> (1867) p. 34 (Source ID: <code>three-hundred-years-norman-house</code>). Modern scholars (Prentout 1916, Searle 1984, Shopkow 1989) have progressively reassessed Dudo's reliability as hagiographic propaganda rather than neutral history; the land-division tradition is broadly accepted but no contemporary document names individual recipients including Eudes. <a class="citation-back" href="#ref-3">↩</a></li>
```

**14.2 Citation n7 — promote Delisle reference to its existing Source ID.** Find:

```
  <li id="n7">DG-I, p. 24: "rests upon traditional evidence only; but there is every reason to believe that this tradition is founded on fact." Hannay, pp. 36–37: "a name supplied by tradition to somebody whose existence is, after all, a matter of certainty." French Wikipedia, "Famille de Gournay": Daniel Gurney's genealogy "a vite été critiquée par des érudits normands comme Léopold Delisle" — Delisle (1826–1910), director of the Bibliothèque nationale, challenged the undocumented early generations. <a class="citation-back" href="#ref-7">↩</a></li>
```

Replace with:

```
  <li id="n7">Daniel Gurney, <em>Record</em> (1848) p. 24 (Source ID: <code>dg-rec-pt1</code>): "rests upon traditional evidence only; but there is every reason to believe that this tradition is founded on fact." James Hannay, <em>Three Hundred Years</em> (1867) pp. 36–37 (Source ID: <code>three-hundred-years-norman-house</code>): "a name supplied by tradition to somebody whose existence is, after all, a matter of certainty." Léopold Delisle's critique of Daniel Gurney's early generations is preserved in French Wikipedia, "Famille de Gournay" (Source ID: <code>wikipedia-fr-famille-de-gournay</code>): Daniel Gurney's genealogy "<em>a vite été critiquée par des érudits normands comme Léopold Delisle</em>." Delisle's specific critique is at Source ID: <code>delisle-critique-of-dg</code>. <a class="citation-back" href="#ref-7">↩</a></li>
```

**JSON alignment.** None.

---

## 15. Cross-cutting: lineage-status label normalisation

**Audit finding.** v53 §13 noted the inconsistency. Across G35/G36/G37 the same conceptual status is variously labelled "Confirmed" / "Limited Historical Record" / "Uncertain" / "Minimal historical record" / "Tradition." This is a structural data issue, not a vital-stat issue per se, but it affects how a FS reviewer will read the four labels. The repo should adopt a single controlled vocabulary.

**Proposed resolution (Phase-2 task, not in this patchset apply scope):** standardise on the four-tier vocabulary already implicit in the JSON:

- `Confirmed` — multiple independent primary or near-primary sources.
- `Probable` — single primary source or strong scholarly consensus.
- `Limited Historical Record` — local-tradition with some scholarly retention; minimum corroboration but not contemporary documentation.
- `Tradition` — local-tradition only; no contemporary documentation; modern scholars (e.g., Delisle) actively dispute.

Under this vocabulary:

| Ancestor | Current JSON lineageStatus | Current fact-sheet narrative status | Proposed unified status |
|---|---|---|---|
| G37 Eudes | Minimal historical record | Tradition | **Tradition** |
| G36 Hugh I | Limited Historical Record | Uncertain | **Limited Historical Record** |
| G35 Renaud | Confirmed | Confirmed | **Confirmed** |
| G34 Hugh II | Confirmed | Confirmed | **Confirmed** |
| G33 Hugh III | Confirmed | Confirmed | **Confirmed** |
| G32 Gerard | Confirmed | Confirmed | **Confirmed** |
| G31 Walter | Confirmed | Confirmed | **Probable** (Richardson's SGM 2002 dissent on Gerard-paternity warrants the qualified label) |
| G24–G30 | Confirmed | Confirmed | **Confirmed** |

**No edit proposed in v54.** The vocabulary change touches both fact-sheet narrative prose and JSON `lineageStatus` fields and should be staged as a separate normalisation patchset (v55 or later) with apply-time review of every changed value.

---

## 16. Proposed new `data/sources.json` entries

Apply by inserting these blocks into the `"sources": { ... }` object of `data/sources.json` (preserve alphabetical order within the file as much as possible). All seven blocks below are formatted to match the existing schema; the apply session should validate JSON syntax after insertion.

```json
    "opendomesday-org": {
      "shortTitle": "Open Domesday",
      "citation": "Powell-Smith, Anna. Open Domesday: a modern digital edition of the Domesday Book (1086). University of Hull / opendomesday.org.",
      "archive": "Open Domesday (opendomesday.org)",
      "url": "https://opendomesday.org/",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Free online edition of the Domesday Book with searchable place, person, and tenant indexes. Used for verifying Hugh of Gournai's Essex Domesday holdings: Liston (sub-tenant Geoffrey Talbot), Fordham, Ardleigh — see https://opendomesday.org/place/TL9228/fordham/. Complements primary-source citation `domesday-1086`."
    },
    "fmg-medlands-normacre": {
      "shortTitle": "FMG MedLands — Normandy (Cawley)",
      "citation": "Cawley, Charles. Medieval Lands: a prosopography of medieval European noble and royal families, Normandy section (NORMANDY — AUMÂLE, ROUEN, EU). Foundation for Medieval Genealogy.",
      "archive": "fmg.ac (Foundation for Medieval Genealogy)",
      "url": "https://fmg.ac/Projects/MedLands/normacre.htm",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Charles Cawley's encyclopaedia of medieval European noble families on the Foundation for Medieval Genealogy site. Contains the Seigneurs de Gournay section with bracketed primary-source citations [875]–[896] including Orderic Vitalis, Guillaume de Jumièges, Albert of Aix, Baudry of Dol, charters of William I and Henry II, the *Chronicon Beccensis*. Frequently referenced in research companions. URL above is the principal Normandy section; the Gournay subsection is at Chapter 3 Section E of that page."
    },
    "pattou-racines-histoire-gournay-2025": {
      "shortTitle": "Pattou Racines Histoire — Gournay",
      "citation": "Pattou, Étienne. Seigneurs de Gournay (-en-Bray) & Gurney, Normandie, Angleterre. Racines & Histoire chart genealogy, last updated 2025-08-11.",
      "archive": "racineshistoire.free.fr",
      "url": "http://racineshistoire.free.fr/LGN/PDF/Gournay.pdf",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Étienne Pattou's chart-genealogy of the Gournay seigneurial line and its Norfolk and Somerset cadet branches. Independent of DG and of Cawley's MedLands; draws on Potin 1842, NRP-I 1852, and modern French scholarship. Companion chart referenced extensively in research companions for G31–G37. Note TLS-certificate issue when fetching via WebFetch (ERR_TLS_CERT_ALTNAME_INVALID on 2026-05-23); browser download works."
    },
    "history-of-parliament-online-gurney-1386-1421": {
      "shortTitle": "HoP Online — Gurney John d.1408",
      "citation": "Roskell, J. S., L. Clark, and C. Rawcliffe, eds. The House of Commons 1386–1421. The History of Parliament Trust. Biography of GURNEY, John (d.1408), of Harpley and West Barsham, Norf.",
      "archive": "historyofparliamentonline.org",
      "url": "https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Principal modern scholarly biography of Sir John Gurney (d. 5 Dec 1408), the collateral son of Edmund Gournay (G23) and Katherine de Wauncy. Corroborates Edmund G23's 1387 death, his Harpley/Hardingham/Saxthorpe-Loundhall holdings, the Wauncy West Barsham inheritance, and the Gurney-family establishment in Norfolk since the 12th century. Distinct from existing sourceId `hop-gurney`; the latter may already cover this entry — confirm at apply time and consolidate if duplicate."
    },
    "wikipedia-en-hamelin-de-warenne": {
      "shortTitle": "Wikipedia — Hamelin de Warenne",
      "citation": "English Wikipedia, \"Hamelin de Warenne, Earl of Surrey.\"",
      "archive": "en.wikipedia.org",
      "url": "https://en.wikipedia.org/wiki/Hamelin_de_Warenne,_Earl_of_Surrey",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Independent encyclopaedic biography of Hamelin Plantagenet (c. 1130 – 7 May 1202), Earl Warren/Surrey. Confirms illegitimate son of Geoffrey of Anjou; elder half-brother of King Henry II; married Isabel de Warenne, 4th Countess of Surrey, April 1164. Used for G29 (Matthew de Gournay) marriage-arranger citation. Wikipedia is a tertiary source but the article itself cites Wace, Robert of Torigni, and modern Anglo-Norman scholarship."
    },
    "wikipedia-fr-famille-de-gournay": {
      "shortTitle": "Wikipédia FR — Famille de Gournay",
      "citation": "Wikipédia français, \"Famille de Gournay.\"",
      "archive": "fr.wikipedia.org",
      "url": "https://fr.wikipedia.org/wiki/Famille_de_Gournay",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Modern French encyclopaedic summary of the Gournay seigneurial line. Notable for explicitly recording Léopold Delisle's critique of Daniel Gurney's 1848 early-generation claims (\"a vite été critiquée par des érudits normands comme Léopold Delisle\"). Useful for non-DG parity at G37 and G36. The article carries the modern position rejecting Eudes as document-confirmed and treating Hugh I (G36) as tradition-only."
    },
    "richardson-sgm-soc-genealogy-medieval-2002": {
      "shortTitle": "Richardson SGM 2002 — Walter not son of Gerard",
      "citation": "Richardson, Douglas. soc.genealogy.medieval (SGM) Usenet post, 11 September 2002. Corrected pedigree post archived in Google Groups thread cPiFbsyHAa8.",
      "archive": "Google Groups soc.genealogy.medieval archive",
      "url": "https://groups.google.com/g/soc.genealogy.medieval/c/cPiFbsyHAa8",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Douglas Richardson's SGM post argues — drawing on Hasted vol. 4, Copinger Manors of Suffolk vol. 3, Loyd & Stenton Hatton Book of Seals, VCH Essex vol. 4, Genealogist vol. 15, Jenkins Cartulary of Missenden Abbey, Gervers Cartulary Knights of St John Essex, Power Norman Frontier 2004, Tanner Fams Friends & Allies 2004 — that Walter de Gournay (G31 in repo numbering) was NOT a son of Gerard de Gournay (G32) of the senior Norman baronial line. Richardson's pedigree starts from Hugh de Gournay III (G33) and treats earlier generations as tradition. The repo follows DG's contrary position; the dispute is documented at `research/case-files/walter-de-gournay-as-son-of-gerard.md`."
    }
```

---

## 17. New-discovery research leads (open items to pursue separately)

The audit pass surfaced these high-value research leads. None is required to apply v53 + v54, but all would substantively strengthen G24–G37 vitals if pursued in a separate session:

1. **TNA CP 40 series, *Placita de Banco*, Norfolk, 3 Edw. I (1274/5), "de Ecclesia de Harpeli."** Anderson 1742 vol. II p. 478 cites this for the Harpley advowson trial-by-battle between Sir John de Gournay (G27) and the Prior of Lewes. The original Common Pleas plea roll, if it survives at The National Archives, would (a) verbatim confirm Anderson's account, (b) pin G27 in the documentary record at a procedurally striking moment, (c) potentially name the king's writ that authorised the judicial duel. Search lead: TNA Discovery catalogue, reference series CP 40, 3 Edward I, Norfolk eyre.

2. **TNA IPM for Edmund Gournay (G23), d. 1387.** Inquisitions Post Mortem for a Norfolk landholder of Edmund's status would typically name (a) his immediate predecessor (i.e., John IV, G24 — if Edmund inherited from a living-then-deceased father), (b) his wife Katherine de Wauncy, (c) his minor heir if any, (d) the exact manor portfolio. Edmund's IPM is the single most likely document to (i) pin John IV's death date, and (ii) name John IV's wife. Search lead: TNA Discovery catalogue, IPM Edward III / Richard II, Edmund Gournay or Gurney, Norfolk.

3. **TNA Patent Rolls, 8 Richard II (1385), part 2, m. 15 — the Walsingham Priory benefaction.** Already identified in the G24 research companion. The patent confirms Edmund G23 as a co-grantor with Stephen de Hales, Oliver de Calthorpe, Ralph de Shelton (knights), and William de Walsham (clerk) of the manors of Great Riburgh and Little Riburgh (Woodhall) to the Prior and Convent of Walsingham. The patent body may name Edmund's wife and/or father. Search lead: TNA Discovery catalogue, C 66 (Patent Rolls), 8 Richard II.

4. **British Library Add. MSS. 8841, fol. 112.** The 1354 Harpley manorial court roll cited by DG-II p. 356 for G24's first court. A photograph or full transcription of fol. 112 would (a) verbatim confirm the 9 August 1354 court date, (b) potentially name jurors / tenants, (c) firmly distinguish G24's August 1354 court from any Blomefield-attributed January 1354 court that may belong to G23. Search lead: British Library digitised manuscripts catalogue, Add. MS 8841.

5. **Fauroux *Recueil des actes des ducs de Normandie de 911 à 1066* (Caen 1961) index check.** The pre-1066 charter witnesses for Hugh II (G34) — the *Liber Niger* Bernières grant and the [1060] "Brenerias" charter — should resolve to either one or two distinct acts. The standard Fauroux edition indexes all pre-1066 Norman ducal acts and would allow definitive identification. Research-companion §5.2 explicitly flags this as "not yet inspected."

6. **Cartulary of La Trinité de Rouen, ed. Deville, Tome III of *Cartulaires de France*, Charter No. 94.** Gerard de Gournay's seal "Signum Girardi de Gornaco" survives in this cartulary. Deville's edition is publicly accessible (Bibliothèque nationale de France / Gallica). A direct inspection would confirm the seal description, the witness list, and the date of the act being sealed. Research-companion §2.11 flags this as "not yet inspected by the repo."

7. **Anselm of Canterbury's *Opera Omnia* (Schmitt ed.), letters lib. iv epist. 7 et 26.** The Anselm-to-Bec letters mentioning "the Lord Hugh de Gournay" and "the Lady Basilia" are foundational for G33's character framing. The standard Schmitt edition is in print; a direct citation of letter numbers would replace the current DG-paraphrase.

8. **NRO (Norfolk Record Office) Harpley manorial records.** Norfolk Record Office holds substantial manorial archives for the Norfolk gentry; G24–G27 manorial holdings (Harpley, Hardingham, Runhall, Swathings, Hingham-Gurneys) likely have material beyond DG and Blomefield. Search lead: NRO online catalogue, parish search Harpley + Hardingham.

9. **The "Norwich Cathedral engrailed-cross coffin-lid"** described by DG-Supp Note 113 (p. 786). DG speculated it could be a Gournay, Ufford, or Ingoldesthorpe tomb. If it survives and has been attributed since 1858, modern art-historical literature (cathedral monumental brasses catalogues, *Norfolk Archaeology*) may have resolved it. A Gournay identification would be the earliest surviving physical memorial of the family in England.

10. **FMG MedLands Seigneurs de Gournay full text.** The session's WebFetch retrieval of `https://fmg.ac/Projects/MedLands/normacre.htm` returned the table-of-contents header for "Seigneurs de Gournay" (Chapter 3 Section E) but the document was truncated before the section body. The full FMG MedLands Gournay entry, with all bracketed primary-source citations [875]–[896], should be captured to `sources/corpus/` for offline reference, similar to the existing DG corpus.

11. **`http://racineshistoire.free.fr/LGN/PDF/Gournay.pdf`** — Pattou's PDF chart-genealogy. WebFetch returned a TLS-certificate error (ERR_TLS_CERT_ALTNAME_INVALID) on 2026-05-23. A browser download or curl-with-cert-relaxation should bring the file into `sources/corpus/` so it can be cited offline. The chart is already referenced extensively in research companions.

12. **Pattou's annexed "non connectés" pages.** Pattou pp. 12–14 cover the Somerset cadet line (Néel/Nigel de Gournay; the Edward II jailer Sir Thomas; Sir Matthew of Crécy/Poitiers d. 26 Sep 1406). These are collaterals, not direct line, but they substantiate the G34 → Néel collateral child entry in JSON (v53 §11.1) and would be useful for cross-references.

13. **Edmund Gournay G23's biographical entry on the History of Parliament Online**, if one exists in the 1386–1421 volume. The search located only the d.1408 collateral Sir John's biography. An Edmund-specific entry would be the single highest-value document for closing the G23–G24 transition.

14. **Léopold Delisle's specific critique of Daniel Gurney's early generations.** Already partially captured under sourceId `delisle-critique-of-dg`. The full Delisle text — likely a *Bibliothèque de l'École des chartes* article or letter — would let the repo absorb the modern-scholarship dissent at primary-source level rather than via the French Wikipedia summary.

15. **William Farrer, *Honors and Knights' Fees* vol. 3, full Norfolk Gurnay section.** The existing repo sourceId `farrer-honors-knights-fees-v3-gurnay-extracts` is described as "extracts." Capturing the full Honor of Arundel section into corpus would corroborate G27 (South Wootton seizure) and likely G29 (Harpley tenure under Warren).

---

## 18. Phase-2 application checklist for v54

When applying this patchset, after v53 has been applied and validated:

1. Apply Section 1.1 — G24 citation n2.
2. Apply Section 1.2 — G24 citation n4.
3. Apply Section 2.1 — G25 citation n4.
4. Apply Section 2.2 — G25 Vitals "Born" cell.
5. Apply Section 2.3 — G25 citation n1.
6. Apply Section 3.1 — G26 citation n4.
7. Apply Section 4.1 — G27 citation n5.
8. Apply Section 6.1 — G29 citation n5.
9. Apply Section 7.1 — G30 citation n5.
10. Apply Section 8.1 — G31 citation n8.
11. Apply Section 9.1, 9.2, 9.3 — G32 citations n4, n5, n6.
12. Apply Section 10.1, 10.2 — G33 citations n10, n2.
13. Apply Section 11.1, 11.2 — G34 citations n7, n6.
14. Apply Section 12.1 — G35 citation n5.
15. Apply Section 12.2 — G35 new citation n7b (or consolidate into n7).
16. Apply Section 13.1 — G36 citation n5.
17. Apply Section 14.1, 14.2 — G37 citations n3, n7.
18. Apply Section 16 — insert seven new entries into `data/sources.json`.
19. Re-validate `data/sources.json` syntax.
20. Re-validate fact-sheet HTML across G24–G37.
21. Confirm no broken `<sup>`/`<a href="#nN">` references.
22. Site mirrors under `site/website/fact-sheets/` are out of scope per the requesting task and should NOT be edited in this patch.
23. The Section 15 lineage-status vocabulary normalisation is deferred to a future patchset.

## 19. Unresolved / out-of-scope notes

- The Section 17 research leads are explicitly *not* required to apply v54; they are forward-looking pointers for the next research session.
- The FMG-vs-repo Hugh-numbering offset (v53 §12, v54 §12.2) is documented in the G35 children-table footnote but not resolved at the JSON `name` field level. Resolving it across all four affected ancestors (G33, G34, G35, G36) would require a coordinated rename pass.
- The G33 c.1093 / 1110 death-year update propagates to `data/familysearch-ids.csv` per v53 §10.1 but the FS-side person-record update is a Phase-2 FS-alignment task.
- The G19 IPM date correction (18 Jan → 16 Feb 1507/8 per DG-Supp Note 132) noted in the CSV is unrelated to G24–G37 and out of scope here.
- The Anderson 1742 trial-by-battle bullet was added to G27 in v53 §4.1; v54 strengthens citation n5 (Lewes/Evesham bullet 1) without affecting the v53 addition.
- Hamelin de Warenne's first wife Isabel de Warenne, 4th Countess of Surrey (married April 1164), is named in the v54 G29 citation n5 update; the repo does not need a separate Wikipedia citation for Isabel.
- The Walter-as-son-of-Gerard editorial choice (G31) remains adopted per DG; the v54 G31 citation n8 update flags the Richardson SGM 2002 dissent inline without changing the adopted position.
