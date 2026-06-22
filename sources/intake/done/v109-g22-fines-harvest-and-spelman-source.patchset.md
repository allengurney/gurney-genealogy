**Done:** 2026-06-21 19:08 PT

# Patchset v109 — G22 Robert: Norfolk feet-of-fines harvest, Joan de Norwich, + Spelman-pedigree source

Phase-1 patchset, supplemental to v108. Promotes the medieval-fines remediation into the **G22 companion**, resolves the Joan-de-Norwich open question, and registers the HMC source behind the located Spelman Gurney pedigree (L-5/L-85). Raw extracts already written directly: `sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md` (revised) and `sources/corpus_supplement/gurney-of-keswick-spelman-pedigree-hmc-1891.md`; the Rye Part I PDF is at `sources/corpus/rye-feet-of-fines-norfolk-part1.pdf`. Leads already updated directly: L-158 (fines), L-159, L-157, L-160, L-8; new leads L-162–L-165 (Germye/Tharston, Gereneye/Saxthorpe, Thomas Gurnay Armiger+Margaret, John Gurnay rector of Harpley).

**L-5 prose note:** the Spelman pedigree's promotion prose is now included as **Item 5** below — the armorial-pedigree topic (`research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md`) was read and two verbatim `str_replace` edits land the located-MS finding into its Keswick/HMC source-map row and its "Spelman 1639 family-paper pedigree" subsection. The source is registered in Item 1; the raw extract is in the corpus supplement.

---

## Item 1 — new source: HMC 12th Report App. IX (Gurney of Keswick MSS / Spelman pedigree)

**Outcome: promote.**

### 1a. `data/sources.json` — add entry under `sources`

```json
"hmc-12th-report-appendix-ix-1891": {
  "citation": "Historical Manuscripts Commission, Twelfth Report, Appendix, Part IX: The Manuscripts of the Duke of Beaufort, K.G., the Earl of Donoughmore, and Others (London: HMSO, 1891) — manuscripts of J. H. Gurney of Keswick Hall, Norfolk",
  "archive": "Internet Archive; the manuscripts themselves in the Gurney-of-Keswick deposit (Norfolk Record Office)",
  "url": "https://archive.org/details/manuscriptsduke00enggoog",
  "corpusStatus": "extract",
  "corpusPath": "sources/corpus_supplement/gurney-of-keswick-spelman-pedigree-hmc-1891.md",
  "validationPath": "sources/validations/hmc-12th-report-appendix-ix-1891.md",
  "notes": "pp. 116 (collection provenance: Cox Macro -> Hudson Gurney -> Keswick; 14 vols tied to Sir Henry Spelman) and 161 (MS 122/16, pp. 1-124: pedigrees with arms of Bardolf, Calthrop, Gurney, and especially Spelman; Spelman wills 1485-1641). Confirms the Spelman-circle Gurney pedigree survives. Page images supplied by Allen Gurney."
}
```

### 1b. New file — `sources/validations/hmc-12th-report-appendix-ix-1891.md`

```markdown
# Validation — HMC 12th Report, Appendix IX (1891): Gurney of Keswick MSS

- **Source examined:** the J. H. Gurney of Keswick section of HMC 12th Report, App. IX, pp. 116 and 161 (page images supplied by Allen Gurney; cross-checked against the Internet Archive full text).
- **What it establishes:** the Spelman-circle pedigree volume survives — MS 122/16, pp. 1–124, "Numerous pedigrees, with arms … Bardolf, Calthrop, Gurney, and especially Spelman; … Spelman wills 1485–1641" — and the collection's provenance (Cox Macro → Hudson Gurney → Keswick; fourteen Spelman volumes).
- **What remains:** the pedigree's internal generations are not transcribed in the HMC entry; reading them needs the NRO Gurney-of-Keswick MS (lead L-85).
- **Findings recorded in:** lead L-85; corpus extract `sources/corpus_supplement/gurney-of-keswick-spelman-pedigree-hmc-1891.md`; prose promotion to the armorial-pedigree topic held pending that file's read.
```

---

## Item 2 — G22 companion: Norfolk feet-of-fines Gurnay/Gournay harvest (Rye Pts I & II)

**Outcome: promote.** Replace the open "not yet undertaken" lead item with the completed harvest.

`str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md`:

**old_string:**
`3. **Norfolk feet of fines, Henry IV (CP 25/1/168 series).** A search of these fines for \`Robert Gurney\`/\`Gurnay\`/\`Gournay\` as querent, deforciant, or trustee in the 1399–1413 window has not yet been undertaken.`

**new_string:**
`3. **Norfolk feet of fines (Rye, Parts I & II) — searched and harvested (2026-06).** Walter Rye's *Short Calendar of the Feet of Fines for Norfolk* was read in full for Gurnay/Gournay across both parts (Pt I, Ric I–Edw I, local copy [`sources/corpus/rye-feet-of-fines-norfolk-part1.pdf`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus/rye-feet-of-fines-norfolk-part1.pdf); Pt II, Edw II–Ric III incl. Henry IV). **Robert's 1405 fine is confirmed in Part II, entry 64** — but the OCR mangles the surname to "Qximay," so it was recovered not by spelling but by anchoring on the cleanly-printed co-party and places (Stodhagh, Cressingham, Hopton, Howard); it recites no parentage, identifying Robert only as "of Parva Cressingham." The wider Gurnay landholding harvest (full list and entry numbers in [`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md)) adds several **direct-line** records previously unseen: **Thomas Gurnay, Esq. ("Armiger"), and Margaret his wife** in Westlexham, Eastlexham, Castleacre, Newton, and Great Dunham (Pt II #200 — a primary attestation of a gentry Thomas of the G20/G21 generation *and his wife's name*, lead L-164); **John Gurnay, rector of Harpley**, holding the manor of Harpley and land in Gaywood (Pt II #489, lead L-165); **John Gournay and Alicia his wife**, manors of Heylesdon and Drayton (Pt II #262 — Sir John Gurney V × Alice Heylesdon, the fine behind the Heylesdon settlement); **Edmund Gournay**, manor of Hingham (Pt II #1526); and the earlier-line Harpley/Saxthorpe/Hardingham/Hillington Gurnays in Part I (Matthew de Gurnay at Harpley #236; John de Gurney of Saxthorpe #837; John de Gurney in Hardingham #1593; Hillington #1059). Two variant-spelling entries are flagged for image verification as possible Gournays: **"Wm. Germye, Chivaler" of Tharston** (Pt II #329 — possibly the Paston "William Gurney esq. of Tharston," lead L-162) and **"Rad. Gereneye," parson, of the manors of Saxthorp and Swatthing** (Pt II #432, lead L-163); "Geney" of Gunton and "Gene" of Tilney were read and excluded as distinct surnames.[^rye-fines-harvest-2026-06]

[^rye-fines-harvest-2026-06]: Walter Rye, *A Short Calendar of the Feet of Fines for Norfolk*, Parts I (Internet Archive [\`ashortcalendarf02ryegoog\`](https://archive.org/details/ashortcalendarf02ryegoog); local PDF [\`sources/corpus/rye-feet-of-fines-norfolk-part1.pdf\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus/rye-feet-of-fines-norfolk-part1.pdf)) and II (Internet Archive [\`ashortcalendarf00ryegoog\`](https://archive.org/details/ashortcalendarf00ryegoog)); Gurnay/Gournay entries and method (place/party anchoring around degraded OCR) transcribed at [\`sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/norfolk-feet-of-fines-gurnay-entries-rye.md). The underlying manuscript fines are TNA CP 25/1 (Norfolk), images at AALT. Source ID: \`rye-feet-of-fines-norfolk\`.`

---

## Item 3 — G22 companion: Open Question on Joan de Norwich (resolved-negative)

**Outcome: promote.**

`str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md`:

**old_string:**
`2. **Joan de Norwich:** Is there a Norwich merchant family "de Norwich" in Blomefield or Rye's *Norfolk Antiquarian*?`

**new_string:**
`2. **Joan de Norwich** (Robert's wife per DG-I pedigree p. 286): the *territorial* de Norwich (de Norwico) barony of Mettingham and Raveningham is **not** her source — that male line failed and its estates passed by 1375 to the heiress **Catharine de Brews** (daughter of Thomas de Norwich) and thence to the **Uffords**, leaving no marriageable Joan de Norwich of Robert's generation (Blomefield; the Mettingham/Raveningham descent). So "de Norwich" most plausibly denotes an **urban/locative Norwich family** (consistent with Edmund G23's Norwich legal-civic standing), or is simply unrecoverable; no candidate Joan has been found in the gentry/baronial line.`

---

## Item 4 — G22 companion: Open Question on Robert-naming fines (now answered)

**Outcome: promote.**

`str_replace` in `research/people/g22-robert-gournay-fact-sheet.research.md`:

**old_string:**
`3. **Any Norfolk fines or rolls naming Robert Gurney c. 1390–1420?**`

**new_string:**
`3. **Norfolk fines naming Robert Gurney c. 1390–1420:** yes — the single such fine is the 1405 Little Cressingham/Hopton fine (Rye Pt II #64, with Thomas Stodhagh, v. Edward Howard), now confirmed at text level (see the feet-of-fines harvest under *Remaining open primary-source leads* above); it recites no parentage, so it neither confirms nor refutes the West Barsham descent.`

---

## Item 5 — armorial-pedigree topic: the Spelman Gurney pedigree located (L-5)

**Outcome: promote.** Two edits to `research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md`.

### 5a. Update the Keswick/HMC source-map row from "New lead" to "Located"

`str_replace`:

**old_string:**
`| MSS of the late John H. Gurney of Keswick, 12th Report of the Historical Manuscripts Commission, p. 116 | Potential family-paper or Keswick-glass source path, important because DG says Gurney's Place glass was preserved at Keswick. | New lead. |`

**new_string:**
`| MSS of the late John H. Gurney of Keswick, HMC 12th Report, App. IX (1891), pp. 116, **161** | **Read at description level (2026-06).** The collection (Cox Macro → Hudson Gurney → Keswick; fourteen volumes tied to Sir Henry Spelman) includes **MS 122/16, pp. 1–124 — "Numerous pedigrees, with arms … Bardolf, Calthrop, Gurney, and especially Spelman; Spelman wills 1485–1641"** — the surviving Spelman-circle Gurney pedigree, which corroborates DG's Spelman source-chain. | **Located; the pedigree's generations still need the NRO Keswick MS itself (lead L-85).**[^hmc-keswick-spelman-2026] |`

### 5b. Note the located MS in the "Spelman 1639 family-paper pedigree" subsection

`str_replace`:

**old_string:**
`DG says it was transcribed by Spelman from one given to him by Francis Gurnay in 1639; it was compiled from original deeds then in the family possession, now lost; DG calls it valuable though imperfect.[^dg-spelman-context]`

**new_string:**
`DG says it was transcribed by Spelman from one given to him by Francis Gurnay in 1639; it was compiled from original deeds then in the family possession, now lost; DG calls it valuable though imperfect.[^dg-spelman-context] The Spelman pedigree itself is now **located and confirmed extant**: it survives in the J. H. Gurney of Keswick deposit as **MS 122/16** (HMC 12th Report, App. IX, 1891, p. 161 — pedigrees with arms of Bardolf, Calthrop, Gurney, and especially Spelman, plus copies of Spelman wills 1485–1641). So the "now-lost original deeds" sit behind a pedigree compilation that does survive; reading its Gurney generations requires the NRO Keswick manuscript (lead L-85).[^hmc-keswick-spelman-2026]

[^hmc-keswick-spelman-2026]: Historical Manuscripts Commission, *Twelfth Report, Appendix, Part IX: The Manuscripts of the Duke of Beaufort, K.G., the Earl of Donoughmore, and Others* (London: HMSO, 1891), pp. 116 (collection provenance) and 161 (MS 122/16); [Internet Archive](https://archive.org/details/manuscriptsduke00enggoog); page images supplied by Allen Gurney. Extract: [\`sources/corpus_supplement/gurney-of-keswick-spelman-pedigree-hmc-1891.md\`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/gurney-of-keswick-spelman-pedigree-hmc-1891.md). Source ID: \`hmc-12th-report-appendix-ix-1891\`.`
