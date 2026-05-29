**Done:** 2026-05-29 16:30 PT — edits applied directly to the 20 fact sheets during the batch-by-batch review session, not via Phase 2 patchset replay. This file is retained as an audit record of the operations performed; the `str_replace` blocks document what was changed and are not intended to be replayed against the source files (their `old_string` values no longer match).

# v74 patchset — light-touch fact-sheet revision pass, G18–G37

Prepared: 2026-05-29
Phase: 1 preparation
Scope: 89 narrow `str_replace` edits across 20 fact sheets (G18 through G37) applying the Plain-English reader contract, Read-as-if-written-all-at-once, Story-led-not-source-led, and Dates-in-years rules from `.claude/rules/fact-sheets.md`. Light touch — no full rewrites; paragraph-level revisions only where the original paragraph was genuinely unsalvageable.

## Scope and architecture

The work spans the entire pre-Tudor Norfolk and Norman section of the direct line — twenty consecutive ancestor fact sheets from William Gurney V (G18, c. 1465) back to Eudes/Odon de Gournay (G37, c. 860). Edits accumulated batch-by-batch in seven batches (3 fact sheets each, last batch G36–G37), each batch user-approved before the next began.

Triggers picked up:

- **Unexplained Latin and Norman French**: *vita patris*, *dilectissimum nostrum*, *caput baroniae*, *la belle Gondrée*, *Hierosolymam petens in ipso itinere mortuus est*, *fortissimi viri*, "La Selde Coronata", "Premières armoiries" / "Secondes armoiries".
- **Pre-1900 legal and heraldic terms** flagged by the rule: engrailed, feoffment, feoffee, advowson, in tail, warren, disseised, parage.
- **Internal classification labels** embedded in reader-facing prose: `COLLATERAL` in children tables; `**Confirmed**`, `**Tradition**`, `**Uncertain**` in narratives.
- **Repo-internal acronyms and meta-vocabulary**: `DG`, `DG-I`, `DG-Supp`, "source layer", "citation layer", "G20 companion", "G20 research companion", "See Research Appendix", "the prize to pull", "pre-DG witness".
- **Project-discovery / evidence-base framing**: "a named primary-source attestation of the alliance independent of the chronicle tradition", "three independent evidentiary chains", "established through three independent evidentiary chains", "an independent primary-source document, separate from the Daniel Gurney narrative".
- **Source-led openings** where the story can carry the weight directly: "Daniel Gurney, *Supplement* (1858) p. 355 notes that…", "Anderson, *House of Yvery* Vol. II (1742), p. 478, records that…", "Modern Heydon scholarship reads…", "Mostyn John Armstrong, in his 1781 Norfolk volumes, lists…".
- **Named authors/researchers without role modifiers**: Daniel Gurney, Hannay, Armstrong, Anderson all picked up role modifiers ("genealogist", "historian", "antiquary") on first body use.
- One **regnal-year shorthand without absolute-year gloss** (G23 vitals: "44 and 49 Edw. III").
- One **capitalization typo** (G20 Highlights bullet 2).

Total: 89 `str_replace` operations across 20 fact sheets.

**Embedded mid-pass research update.** The G28 marriage block additionally absorbs a user-directed research revision identifying Katherine as `de Ingoldesthorpe` rather than `probably a Baconsthorpe`, based on the wording of the 1243 North Wootton fine ("*de se et heredibus ipsius Katarine*"). Operations 76–83 implement this revision; operations 54–55 (the earlier Batch-4 fix that still used the Baconsthorpe framing) are superseded by the Ingoldesthorpe operations and are retained in the operation log for traceability only.

## Source tracking

No new source IDs. No `data/sources.json` changes. All edits are prose revisions and footnote rephrasings against existing, already-registered sources.

## Stub housekeeping

`sources/intake/processed/stub-v74.md` is renamed/promoted to this patchset. `sources/intake/processed/stub-v75.md` is created in the same step.

## Outcomes

| Item | Outcome | Destination |
|---|---|---|
| Fact-sheet light-review revisions, G18–G37 | promote | 20 files under `fact-sheets/` |
| Working staging file | discard at Phase 2 | `sources/intake/processed/_v74-fs-light-review-staging.md` removed on Phase 2 close |
| Stub housekeeping | promote | `stub-v74.md` retired; `stub-v75.md` created |

No item rejected.

---

## Phase 2 operations

Operations are grouped by fact-sheet file in generation order (G18 → G37). Within each file, operations follow the order of the original batch tables. Each block is a single `str_replace` against the file named in the section header.

---

### G18 — William Gurney V

**File:** `fact-sheets/g18-william-gurney-v-fact-sheet.md`

#### Op 1 — Vitals Status: Latin gloss

```str_replace
old_string: Never inherited as the principal lord; died <em>vita patris</em>.
new_string: Never inherited as the principal lord; died during his father's lifetime (<em>vita patris</em>).
```

#### Op 2 — Vitals Died: source-led trim

```str_replace
old_string: Modern Heydon scholarship reads Anne Heydon's marriages as: (1) William Gurney "shortly after 28 May 1484"; (2) Sir Lionel Dymoke. Anne survived William V and remarried.
new_string: Anne Heydon married him shortly after 28 May 1484 and later remarried Sir Lionel Dymoke.
```

#### Op 3 — Marriage cell: Armstrong attribution removed

```str_replace
old_string: Mostyn John Armstrong, in his 1781 Norfolk volumes, lists Anne Heydon's four sisters and their husbands in a single paragraph: Amy (Sir Roger Townshend of Hunstanton), Dorothy (Sir Thomas Brook, heir of Lord Cobham), Elizabeth (Walter Hobart of Hales-hall), and Bridget (Sir William Paston) — placing William V's marriage inside one of the densest North Norfolk gentry-alliance networks of the late 15th century.
new_string: Anne's four sisters married into one of the densest North Norfolk gentry-alliance networks of the late 15th century — Amy to Sir Roger Townshend of Hunstanton, Dorothy to Sir Thomas Brook, heir of Lord Cobham, Elizabeth to Walter Hobart of Hales-hall, and Bridget to Sir William Paston.
```

#### Op 4 — Highlights bullet 4: source-led reframe

```str_replace
old_string: <strong>"Of Irstead" — the Norfolk Broads identification.</strong> Daniel Gurney's pedigree identifies William V as "of Irstead." The connection to Irstead manor came in through his Heydon father-in-law:
new_string: <strong>"Of Irstead" — the Norfolk Broads identification.</strong> William V was known as "of Irstead." The connection to Irstead manor came in through his Heydon father-in-law:
```

#### Op 5 — Narrative para 1: source-led aside trimmed

```str_replace
old_string: Around 1484 — modern Heydon scholarship reads Sir Henry Heydon's surviving will of 1503/4 as placing the marriage "shortly after 28 May 1484" — William V married Anne Heydon, daughter of Sir Henry Heydon of Baconsthorpe Castle.
new_string: Shortly after 28 May 1484, William V married Anne Heydon, daughter of Sir Henry Heydon of Baconsthorpe Castle.
```

#### Op 6 — Narrative para 4: repo-internal "source layer"

```str_replace
old_string: Two generations later, Francis Gurney (G14) appears in the source layer as a merchant or agent handling Lestrange business;
new_string: Two generations later, Francis Gurney (G14) appears as a merchant or agent handling Lestrange business;
```

#### Op 7 — Narrative para 5: source-led reframe (mirror of Op 4)

```str_replace
old_string: Daniel Gurney's pedigree identifies William V as "of Irstead." The connection to Irstead manor came in through his Heydon father-in-law: per Francis Blomefield's parish entry for Irstead in volume xi,
new_string: William V was known as "of Irstead." The connection to Irstead manor came in through his Heydon father-in-law: per Francis Blomefield's parish entry for Irstead in volume xi,
```

#### Op 8 — Narrative para 6: repo-internal "citation layer"

```str_replace
old_string: The surviving citation layer does not identify the guardians or prove that Anthony's wardship was administered by Heydon kin.
new_string: The surviving records do not identify the guardians or prove that Anthony's wardship was administered by Heydon kin.
```

#### Op 9 — Narrative para 7: source attribution trimmed

```str_replace
old_string: Anne Heydon survived her son's eventual marriage and her grandson's birth, and died around 1521. Her remarriage to Sir Lionel Dymoke and her death are independently documented in modern Dymoke and Heydon family literature.
new_string: Anne Heydon survived her son's eventual marriage and her grandson's birth. She remarried Sir Lionel Dymoke of Ashby, Lincolnshire, and died around 1521.
```

---

### G19 — William Gurney IV

**File:** `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

#### Op 10 — Children table: Latin shorthand glossed

```str_replace
old_string: fl. late 15th c. – d. <em>vita patris</em> before 1508
new_string: fl. late 15th c. – d. before his father, before 1508
```

#### Op 11 — Narrative para 6: Latin gloss on first body use

```str_replace
old_string: His eldest son William V had already died <em>vita patris</em>; his nine-year-old grandson Anthony succeeded as direct heir.
new_string: His eldest son William V had already died in his father's lifetime (<em>vita patris</em>); his nine-year-old grandson Anthony succeeded as direct heir.
```

---

### G20 — Thomas Gournay II

**File:** `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

#### Op 12 — Highlights bullet 2: capitalization typo

```str_replace
old_string: and a Norwich town house in St Gregory's parish. genealogist Daniel Gurney used this as evidence
new_string: and a Norwich town house in St Gregory's parish. Genealogist Daniel Gurney used this as evidence
```

#### Op 13 — Narrative para 2: feoffment gloss + repo-internal "G20 companion" + italicize *Supplement*

```str_replace
old_string: By 1445, a Thomas Gurnay, Esq., was one of the sealers of an East Barsham feoffment preserved at Hunstanton Hall; because Daniel Gurney's Supplement separately says Thomas I was probably dead before 1444, the G20 companion treats this as Thomas II's first known adult attestation and evidence that he was already acting in the family network by the mid-1440s.
new_string: By 1445, a Thomas Gurnay, Esq., was one of the sealers of an East Barsham feoffment (land-transfer deed) preserved at Hunstanton Hall; because Daniel Gurney's <em>Supplement</em> separately says Thomas I was probably dead before 1444, this is most likely Thomas II's first known adult attestation, showing him already acting in the family network by the mid-1440s.
```

#### Op 14 — Footnote 15: repo-internal "G20 research companion" + "DG-Supp"

```str_replace
old_string: The G20 research companion assigns this to Thomas II because DG-Supp Note 123 says Thomas I was probably dead before 1444.
new_string: Daniel Gurney's <em>Supplement</em>, Note 123, separately states Thomas I was probably dead before 1444, so the 1445 sealer is most likely Thomas II.
```

---

### G21 — Thomas Gournay I

**File:** `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

#### Op 15 — Narrative para 5: role modifier

```str_replace
old_string: He probably died before 1444, if Daniel Gurney's reading of the Boking fine is correct,
new_string: He probably died before 1444, if genealogist Daniel Gurney's reading of the Boking fine is correct,
```

#### Op 16 — Timeline: role modifier

```str_replace
old_string: Dies before the Boking fine if Daniel Gurney's attribution of that fine to Thomas II is correct.
new_string: Dies before the Boking fine if genealogist Daniel Gurney's attribution of that fine to Thomas II is correct.
```

#### Op 17 — Narrative para 4 (paragraph): repo-internal aside, project-discovery framing, feoffee gloss

```str_replace
old_string: What has been found is a narrower but real record: service as a man-at-arms in France in 1415, 1418, and 1441, followed by a 1434-35 East Barsham feoffee appearance with John Hunt. The 1445 Hunstanton Hall seal belongs in the G20 Thomas II fact sheet, not here, because the G20 companion already treats it as evidence that Thomas II was acting as head of the family by 1444-45. The cumulative picture for Thomas I is therefore still of a quietly active Norfolk gentleman, but the evidence should stop at the 1441/1434-35 cluster unless a direct record ties the 1445 deed back to him.
new_string: What has been found is a narrower but real record: service as a man-at-arms in France in 1415, 1418, and 1441, and a 1434-35 appearance as a feoffee (trustee) on an East Barsham land transfer with John Hunt. The cumulative picture is of a quietly active Norfolk gentleman.
```

---

### G22 — Robert Gournay

**File:** `fact-sheets/g22-robert-gournay-fact-sheet.md`

#### Op 18 — Vitals Marriage: source-led citation trimmed

```str_replace
old_string: <strong>Joan de Norwich</strong> — per Daniel Gurney's Record, Part I, p. 280. No further details on her family, parentage, or dates in sources consulted.
new_string: <strong>Joan de Norwich</strong>. No further details on her family, parentage, or dates have been found.
```

#### Op 19 — Highlights bullet 2: Latin term gloss

```str_replace
old_string: houses in Norwich, and the great London warehouse "La Selde Coronata."
new_string: houses in Norwich, and the great London warehouse known as "La Selde Coronata" (a merchant's storehouse).
```

#### Op 20 — Highlights bullet 1 (paragraph): repo-internal meta + missing role modifier

```str_replace
old_string: <li><strong>His very name is uncertain — Daniel Gurney hedged it.</strong> In Edmund Gournay's will chapter, Daniel Gurney writes of "a second son, whom we believe was named Robert." This is an explicit editorial hedge in the primary compiled source: Daniel Gurney was not certain of the name. The only other source Daniel Gurney cites for the children of Edmund is the 1622 pedigree by Cook, Clarenceux King of Arms. The name Robert is treated as the most probable but not the confirmed identification. This page uses "Robert" while flagging the uncertainty prominently. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
new_string: <li><strong>Even his given name is uncertain.</strong> In his Edmund Gournay chapter, the genealogist Daniel Gurney wrote of "a second son, whom we believe was named Robert" — an explicit editorial hedge. The only other source he cites for Edmund's children is the 1622 pedigree by Cook, Clarenceux King of Arms. Robert is the most probable identification, not a confirmed one. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

#### Op 21 — Narrative para 1: role modifier on first body use

```str_replace
old_string: yet Daniel Gurney himself was uncertain enough about his name
new_string: yet the genealogist Daniel Gurney himself was uncertain enough about his name
```

#### Op 22 — Narrative para 2: project-discovery framing

```str_replace
old_string: while Robert has not yet been found in a deed, will, court appearance, or land transaction under his own name.
new_string: while no deed, will, court appearance, or land transaction has been found that names Robert in his own right.
```

#### Op 23 — Narrative para 4: source-led meta-prose

```str_replace
old_string: What is clear is that the descent through Robert is supported by Daniel Gurney's pedigree and by the modern History of Parliament account of Sir John's succession crisis:
new_string: The descent through Robert is supported by Daniel Gurney's pedigree and by the modern History of Parliament account of Sir John's succession crisis:
```

---

### G23 — Edmund Gournay

**File:** `fact-sheets/g23-edmund-gurney-fact-sheet.md`

#### Op 24 — Vitals Occupation: regnal-year shorthand → absolute years

```str_replace
old_string: Justice of the peace for Norfolk (44 and 49 Edw. III).
new_string: Justice of the peace for Norfolk (1370 and 1375).
```

#### Op 25 — Highlights bullet 2: source-led aside trimmed

```str_replace
old_string: This is a History of Parliament attestation: Edmund was not merely a local gentleman;
new_string: Edmund was not merely a local gentleman;
```

#### Op 26 — Highlights bullet 3: source-led opening reframed

```str_replace
old_string: Daniel Gurney records that Edmund and his colleague Edmund de Clipesby "were the standing council for the city of Norwich, in the nature of recorder and steward."
new_string: Edmund and his colleague Edmund de Clipesby served as "the standing council for the city of Norwich, in the nature of recorder and steward."
```

#### Op 27 — Highlights bullet 4: heraldic gloss for "engrailed"

```str_replace
old_string: Edmund's arms (the engrailed cross, argent) impaling the Wauncy coat
new_string: Edmund's arms (an <a href="https://en.wikipedia.org/wiki/Engrailed">engrailed</a> cross, argent — that is, a silver cross with a scalloped edge) impaling the Wauncy coat
```

#### Op 28 — Highlights bullet 4: DG acronym expanded

```str_replace
old_string: The same impaled coat was still visible in a window of Denton church, Norfolk, as of DG's writing in 1848.
new_string: The same impaled coat was still visible in a window of Denton church, Norfolk, as of Daniel Gurney's writing in 1848.
```

#### Op 29 — Highlights bullet 5: DG acronym expanded

```str_replace
old_string: DG catalogues Edmund's appearances across at least fifteen separate royal instruments:
new_string: Daniel Gurney catalogues Edmund's appearances across at least fifteen separate royal instruments:
```

#### Op 30 — Children table Sir John row: COLLATERAL removed

```str_replace
old_string: His son Edmond died under age — line extinct. COLLATERAL.
new_string: His son Edmond died under age — line extinct.
```

#### Op 31 — Children table Robert row: DG acronym expanded

```str_replace
old_string: Second son. DG notes "whom we believe was named Robert."
new_string: Second son. Daniel Gurney notes "whom we believe was named Robert."
```

#### Op 32 — Children table Jeanne row: COLLATERAL removed

```str_replace
old_string: Married Osbert Mundeford of Hockwold, Esq., who was also one of Edmund's executors. COLLATERAL.
new_string: Married Osbert Mundeford of Hockwold, Esq., who was also one of Edmund's executors.
```

#### Op 33 — Narrative para 4: pre-1900 legal term ("disseised") glossed

```str_replace
old_string: anyone he had unjustly disseised, injured, extorted, or wrongfully detained property from.
new_string: anyone he had unjustly dispossessed of land (disseised), injured, extorted, or wrongfully detained property from.
```

---

### G24 — John de Gournay IV

**File:** `fact-sheets/g24-john-de-gournay-iv-fact-sheet.md`

#### Op 34 — Vitals Marriage: DG acronym + source-led citation trimmed

```str_replace
old_string: <strong>Unknown.</strong> No wife named in DG or any other source consulted.
new_string: <strong>Unknown.</strong> No wife is named in any source consulted.
```

#### Op 35 — Highlights bullet 3: source-led opening trimmed + advowson gloss

```str_replace
old_string: Daniel Gurney, <em>Supplement</em> (1858) p. 355 notes that in 1332 "either he or his father presented to the church of Harpley; but more probably this John de Gurney [IV], as he is called John de Gurney junior" in the deed. If so, John IV exercised advowson as a very young man
new_string: In 1332, "either he or his father presented to the church of Harpley; but more probably this John de Gurney [IV], as he is called John de Gurney junior" in the deed. If so, John IV exercised the right of advowson (the right to nominate a parish clergyman) as a very young man
```

---

### G25 — John de Gournay III

**File:** `fact-sheets/g25-john-de-gournay-iii-fact-sheet.md`

#### Op 36 — Highlights bullet 3: DG acronym + role modifier

```str_replace
old_string: The DG pedigree records that Jane was the daughter of Edmund de Lexham
new_string: Genealogist Daniel Gurney's pedigree records that Jane was the daughter of Edmund de Lexham
```

#### Op 37 — Narrative para 2: "settled in tail" → plain-language verb + gloss

```str_replace
old_string: had already settled the Harpley estate on John and his wife Jane in tail.
new_string: had already granted the Harpley estate to John and his wife Jane, to pass only to their direct heirs.
```

---

### G26 — Sir William de Gournay III

**File:** `fact-sheets/g26-sir-william-de-gournay-iii-fact-sheet.md`

#### Op 38 — Highlights bullet 1: engrailed gloss + role modifier

```str_replace
old_string: was sealed by William with an engrailed cross. Daniel Gurney identified this as
new_string: was sealed by William with an <a href="https://en.wikipedia.org/wiki/Engrailed">engrailed</a> cross (a cross with a scalloped edge). The genealogist Daniel Gurney identified this as
```

#### Op 39 — Children table Edmund row: DG acronym + COLLATERAL removed

```str_replace
old_string: Named in DG pedigree p. 286 alongside John III. Further details not documented in sources consulted. COLLATERAL.
new_string: Named in Daniel Gurney's pedigree alongside John III. Further details not documented in sources consulted.
```

#### Op 40 — Children table William row: DG acronym + COLLATERAL removed

```str_replace
old_string: Named in DG pedigree p. 286 alongside John III. Further details not documented. COLLATERAL.
new_string: Named in Daniel Gurney's pedigree alongside John III. Further details not documented.
```

#### Op 41 — Narrative para 1: role modifier + italic *Supplement* + warren gloss

```str_replace
old_string: Daniel Gurney's pedigree places him in 14 Edward I (1286) as lord of Gurney's manor in Harpley, Hardingham, and Hingham; the Supplement adds an earlier 1274 warren claim at Hardingham,
new_string: The genealogist Daniel Gurney's pedigree places him in 14 Edward I (1286) as lord of Gurney's manor in Harpley, Hardingham, and Hingham; the <em>Supplement</em> adds an earlier 1274 claim to free warren (the right to hunt small game) at Hardingham,
```

#### Op 42 — Narrative para 2: informal "Daniel" trimmed

```str_replace
old_string: his seal, an engrailed cross, the earliest surviving physical impression of the Gournay arms Daniel could identify.
new_string: his seal, an engrailed cross, the earliest surviving physical impression of the Gournay arms.
```

#### Op 43 — Narrative para 2: informal "Daniel" trimmed

```str_replace
old_string: but William's seal is the first document Daniel found with the family cross pressed into wax.
new_string: but William's seal is the earliest surviving document with the family cross pressed into wax.
```

#### Op 44 — Highlights bullet 3 (paragraph): project-discovery framing + DG acronym

```str_replace
old_string: <li><strong>The Baconsthorpe marriage resolved a long-running puzzle.</strong> His father William II's wife was identified by DG only as "probably a Baconsthorpe." William III's wife Katherine is confirmed as "daughter of Edmund Baconsthorpe" — establishing a definite Baconsthorpe connection in this generation, and explaining why DG made the inference about the previous one. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
new_string: <li><strong>A documented Baconsthorpe marriage.</strong> William III's wife Katherine is recorded as "daughter of Edmund Baconsthorpe," anchoring the family into the Baconsthorpe gentry. (For William's father William II, the genealogist Daniel Gurney could only suggest the wife was "probably a Baconsthorpe" — an inference the William III match helps to explain.) <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

---

### G27 — Sir John de Gournay I

**File:** `fact-sheets/g27-sir-john-de-gournay-i-fact-sheet.md`

#### Op 45 — Vitals Marriage: DG acronym + source-led trim

```str_replace
old_string: <strong>Unknown.</strong> No wife named in DG or any other source consulted.
new_string: <strong>Unknown.</strong> No wife is named in any source consulted.
```

#### Op 46 — Highlights bullet 2: DG acronym

```str_replace
old_string: DG proposed the Crusade as the probable moment of adoption,
new_string: Daniel Gurney proposed the Crusade as the probable moment of adoption,
```

#### Op 47 — Highlights bullet 5: source-led opening trimmed

```str_replace
old_string: Anderson, <em>House of Yvery</em> Vol. II (1742), p. 478, records that John "had a Suit with the Prior of Lewes, for the Right of Presentation to the Church of Harpeli ... whereupon a Trial by Battle was appointed, and the said John de Gournay and the Prior came armed into the Field, where the Prior yielded full Seizin of the said Advowson, to the said John de Gournay, for himself and his Successors for ever."
new_string: In 1274/5, John "had a Suit with the Prior of Lewes, for the Right of Presentation to the Church of Harpeli ... whereupon a Trial by Battle was appointed, and the said John de Gournay and the Prior came armed into the Field, where the Prior yielded full Seizin of the said Advowson, to the said John de Gournay, for himself and his Successors for ever."
```

#### Op 48 — Children table John II row: COLLATERAL removed

```str_replace
old_string: Died 1332; buried Harpley chancel. COLLATERAL.
new_string: Died 1332; buried Harpley chancel.
```

#### Op 49 — Narrative para 4: source-led + repo-internal "prize to pull" + "pre-DG witness"

```str_replace
old_string: In 3 Edward I (1274/5), James Anderson's 1742 <em>House of Yvery</em> says John and the Prior of Lewes came armed into the field over the right to present the rector of Harpley. The Prior yielded, and the advowson passed to John and his successors. The original plea roll is still the prize to pull, but Anderson's account is an independent pre-DG witness and fits the Harpley tenure pattern documented in the Hundred Rolls.
new_string: In 1274/5, John and the Prior of Lewes came armed into the field over the right to present the rector of Harpley. The Prior yielded, and the advowson passed to John and his successors. The antiquary James Anderson's 1742 <em>House of Yvery</em> preserves the story, and it fits the Harpley tenure pattern documented in the Hundred Rolls.
```

---

### G28 — William de Gournay II

**File:** `fact-sheets/g28-william-de-gournay-ii-fact-sheet.md`

*Note: Ops 54 and 55 in the original batch sequence were a first-pass Baconsthorpe-framing fix; they are superseded by Ops 76–83 (the Ingoldesthorpe revision) below. The original Ops 54/55 strings are not replayed at Phase 2; only the final Ingoldesthorpe state is applied.*

#### Op 50 — Highlights bullet 2: DG acronym

```str_replace
old_string: The DG pedigree cites two independent Norfolk records for William II,
new_string: Daniel Gurney's pedigree cites two independent Norfolk records for William II,
```

#### Op 51 — Children table Edmund row: DG acronym + COLLATERAL removed

```str_replace
old_string: Named in DG pedigree. Held a quarter of a knight's fee in Houghton of the honour of Wormegay, 1303. COLLATERAL.
new_string: Named in Daniel Gurney's pedigree. Held a quarter of a knight's fee in Houghton of the honour of Wormegay, 1303.
```

#### Op 52 — Children table Thomas row: pedigree mention removed (citation lives in footnote)

```str_replace
old_string: Named in a Norfolk fine (DG pedigree). COLLATERAL.
new_string: Named in a Norfolk fine.
```

#### Op 53 — Narrative para 4: internal status-classification meta sentence deleted

```str_replace
old_string: 

He is classified as **Confirmed** on the basis of the two independent Norfolk records (1234 and 1243) and the DG pedigree's consistent documentation.

new_string: 

```

#### Op 54 (superseded; see Op 76) — Vitals Marriage: first-pass DG/DG-Supp/DG-I + reconciliation framing

*This operation produced an intermediate Baconsthorpe-vs-Ingoldesthorpe two-reading framing that was superseded mid-pass by the user's research revision. Phase 2 should skip this op and apply Op 76 directly.*

```str_replace
old_string: <strong>Katherine</strong> -- surname unresolved. DG pedigree p. 286 calls her "probably a Baconsthorpe"; DG-Supp Note 113 (1858) -- DG's later, more considered view -- proposes she was a daughter or sister of Thomas de Ingoldesthorpe, based on the fine at DG-I p. 325. The two identifications are not yet reconciled. By Katherine, William was father of Sir John de Gournay I (G27).
new_string: <strong>Katherine de Ingoldesthorpe</strong> — almost certainly a daughter or sister of Thomas de Ingoldesthorpe, on the wording of the 1243 fine they levied together with him over forty acres of marsh at North Wootton, Norfolk. By Katherine, William was father of Sir John de Gournay I (G27).
```

#### Op 55 (superseded; see Op 78) — Highlights bullet 3: first-pass DG acronym + "See Research Appendix"

*Superseded mid-pass by the Ingoldesthorpe revision. Phase 2 should skip this op and apply Op 78 directly.*

```str_replace
old_string: <li><strong>Wife Katherine "probably a Baconsthorpe."</strong> The Baconsthorpe family (of Baconsthorpe, Norfolk) were established Norfolk gentry closely connected to the Gournay network. Daniel Gurney flags this identification as probable but not confirmed — Katherine's surname is not explicitly stated in any surviving primary source reviewed. DG notes her son Sir William III (William II's grandson) married "Katherine, daughter of Edmund Baconsthorpe" — which may indicate a family pattern or DG's inference that Katherine the wife was also a Baconsthorpe. See Research Appendix. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
new_string: <li><strong>Wife Katherine, of the Ingoldesthorpes of Norfolk.</strong> Identified from the wording of a 1243 fine that William and Katherine levied with Thomas de Ingoldesthorpe over marshland at North Wootton; the quitclaim's reference to "the heirs of the said Katherine" makes Thomas her father or brother. The Ingoldesthorpes were leading Norfolk gentry — Thomas the Sheriff of Norfolk under Henry III; later heiresses of the line married into the Jernegan and Neville families. Their arms — a cross engrailed, gules and argent reversed from Gurney's — placed them in the same small heraldic cousinage of cross-engrailed Norfolk knights (Gurney, Ufford, Ingoldesthorpe) who all sent men with Edward I on the 1270 crusade. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

#### Op 76 — G28 Vitals Marriage (final): Ingoldesthorpe identification

```str_replace
old_string: <strong>Katherine</strong> -- surname unresolved. DG pedigree p. 286 calls her "probably a Baconsthorpe"; DG-Supp Note 113 (1858) -- DG's later, more considered view -- proposes she was a daughter or sister of Thomas de Ingoldesthorpe, based on the fine at DG-I p. 325. The two identifications are not yet reconciled. By Katherine, William was father of Sir John de Gournay I (G27).
new_string: <strong>Katherine de Ingoldesthorpe</strong> — almost certainly a daughter or sister of Thomas de Ingoldesthorpe, on the wording of the 1243 fine they levied together with him over forty acres of marsh at North Wootton, Norfolk. By Katherine, William was father of Sir John de Gournay I (G27).
```

*Phase 2 collapses Ops 54 and 76 into the single Op 76 application.*

#### Op 77 — Footnote n4: full replacement, Ingoldesthorpe apparatus

```str_replace
old_string:   <li id="n4">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: "KATHARINE, probably a Baconsthorpe." No maiden name stated. DG's identification of her as "probably a Baconsthorpe" is inferred rather than documented. <a class="citation-back" href="#ref-4">↩</a></li>
new_string:   <li id="n4">Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, pp. 325–326 and Appendix LVI no. 3. The 1243 fine (27 Henry III) is between Thomas de Ingaldestorp on one side and William de Gurnay and Katherine his wife on the other; the quitclaim runs "<em>de se et heredibus ipsius Katarine</em>" — "of themselves and the heirs of the said Katherine" — a standard medieval signal that the lands traced through her family. Daniel Gurney concludes Katherine was "of the family of Ingoldesthorpe," a reading restated and sharpened in the 1858 <em>Supplement</em> (Note 113, p. 786). Heraldically corroborated: the Ingoldesthorpes bore gules, a cross engrailed argent — the Gurney coat with the colours reversed (Daniel Gurney, <em>Record</em>, Part I, p. 326). An earlier cell label in Daniel Gurney's own pedigree table on p. 286 reads "probably a Baconsthorpe," but is hard to support independently — no Baconsthorpe family of standing is documented in Norfolk in the 1240s, and the label appears to have been retro-applied from a later, separately documented Katherine Baconsthorpe (daughter of Edmund Baconsthorpe) who married G28's grandson Sir William III. <a class="citation-back" href="#ref-4">↩</a></li>
```

#### Op 78 — G28 Highlights bullet 3 (final): Ingoldesthorpe story

```str_replace
old_string: <li><strong>Wife Katherine "probably a Baconsthorpe."</strong> The Baconsthorpe family (of Baconsthorpe, Norfolk) were established Norfolk gentry closely connected to the Gournay network. Daniel Gurney flags this identification as probable but not confirmed — Katherine's surname is not explicitly stated in any surviving primary source reviewed. DG notes her son Sir William III (William II's grandson) married "Katherine, daughter of Edmund Baconsthorpe" — which may indicate a family pattern or DG's inference that Katherine the wife was also a Baconsthorpe. See Research Appendix. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
new_string: <li><strong>Wife Katherine, of the Ingoldesthorpes of Norfolk.</strong> Identified from the wording of a 1243 fine that William and Katherine levied with Thomas de Ingoldesthorpe over marshland at North Wootton; the quitclaim's reference to "the heirs of the said Katherine" makes Thomas her father or brother. The Ingoldesthorpes were leading Norfolk gentry — Thomas the Sheriff of Norfolk under Henry III; later heiresses of the line married into the Jernegan and Neville families. Their arms — a cross engrailed, gules and argent reversed from Gurney's — placed them in the same small heraldic cousinage of cross-engrailed Norfolk knights (Gurney, Ufford, Ingoldesthorpe) who all sent men with Edward I on the 1270 crusade. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

*Phase 2 collapses Ops 55 and 78 into the single Op 78 application.*

#### Op 79 — Footnote n7: full replacement, Ingoldesthorpe apparatus

```str_replace
old_string:   <li id="n7">Daniel Gurney, <em>Record</em> (1848), pedigree p. 286: Katherine "probably a Baconsthorpe." Sir William III (William II's grandson, not son) married Katherine, daughter of Edmund Baconsthorpe — a different Katherine. The Baconsthorpe identification of William II's wife appears to rest on DG's inference from the family pattern. <a class="citation-back" href="#ref-7">↩</a></li>
new_string:   <li id="n7">Daniel Gurney, <em>Record of the House of Gournay</em> (1848), Part II, pp. 325–326 (narrative and Latin transcription of the 1243 North Wootton fine at Appendix LVI no. 3); <em>Supplement to the Record of the House of Gournay</em> (1858), Note 113, p. 786 (Ingoldesthorpe pedigree sketch — "Redde Thomas" in the time of Richard I; his son sheriff of Norfolk in 1236; Ela m. Sir Hugh Jernegan c. 1250; Isabel m. John Neville, Marquis Montacute, under Henry VI; engrailed-cross arms shared with Gurney and Ufford; all three houses represented on Edward I's 1270 crusade). Source records the 1243 fine as TNA-class Pedes Finium for Norfolk, 21–41 Henry III (now in CP 25/1). <a class="citation-back" href="#ref-7">↩</a></li>
```

#### Op 80 — Children table mother column: all three rows updated

`replace_all = true` for this op.

```str_replace
old_string: Katherine (prob. Baconsthorpe)
new_string: Katherine (de Ingoldesthorpe)
```

#### Op 81 — Narrative para 2 lead sentence: Ingoldesthorpe framing

```str_replace
old_string: His wife Katherine — probably, but not certainly, a Baconsthorpe — gave him at least three children.
new_string: His wife Katherine — a daughter or sister of Thomas de Ingoldesthorpe, the Norfolk knight whose family bore the cross engrailed in reversed colours from the Gurneys — gave him at least three children.
```

#### Op 82 — Narrative para 2: forward-pointer sentence inserted

```str_replace
old_string: John was a rebel, a penitent, a Crusader, and ultimately the man who established the heraldic identity that the family carried for the rest of its English history. William's second son Edmund held a minor knight's fee in 1303.
new_string: John was a rebel, a penitent, a Crusader, and ultimately the man who established the heraldic identity that the family carried for the rest of its English history. The shared engrailed-cross arms of Gurney, Ufford, and Ingoldesthorpe — three Norfolk houses who all sent men on Edward I's crusade — suggest a small, allied cousinage of Norfolk knights into which Katherine's marriage had brought William a generation before. William's second son Edmund held a minor knight's fee in 1303.
```

#### Op 83 — Timeline 1243 row: Ingoldesthorpe attestation

```str_replace
old_string:       <tr><td>1243</td><td>Attested again in a Norfolk record.</td></tr>
new_string:       <tr><td>1243</td><td>Joined with Katherine in a fine at Westminster with Thomas de Ingoldesthorpe over forty acres of marsh at North Wootton, the record from which Katherine's Ingoldesthorpe identity is read.</td></tr>
```

---

### G29 — Sir Matthew de Gournay

**File:** `fact-sheets/g29-matthew-de-gournay-fact-sheet.md`

#### Op 56 — Highlights bullet 3: project-discovery / evidence-base framing trimmed

```str_replace
old_string: Matthew gave the tithes of Hardingham to the church there — recorded in Harl. MSS. 970 (British Library Harleian manuscripts). This is an independent primary-source document, separate from the Daniel Gurney narrative, confirming Matthew's landholding and his name.
new_string: Matthew gave the tithes of Hardingham to the church there — an act recorded in the British Library Harleian Manuscripts (Harl. MSS. 970).
```

#### Op 57 — Timeline: 1206/1217 rows — DG-I/DG-Supp acronyms removed, 1206 row deleted, 1217 row uses footnote anchor

```str_replace
old_string:       <tr><td>1206</td><td>Living per DG-I pedigree p. 286.</td></tr>
      <tr><td>1217</td><td>Last attested. Pays 20 marks for a writ of attaint concerning his Swathings tenement (Fine Roll 2 Henry III, Norfolk) -- DG-Supp Note 109 (p. 780).</td></tr>
new_string:       <tr><td>1217</td><td>Last attested. Pays 20 marks for a writ of attaint concerning his Swathings tenement. <sup class="fn"><a href="#n2" id="ref-2c">2</a></sup></td></tr>
```

---

### G30 — William de Gournay I

**File:** `fact-sheets/g30-william-de-gournay-i-fact-sheet.md`

#### Op 58 — Highlights bullet 1: role modifier added

```str_replace
old_string: Daniel Gurney called this "an incontestable proof of his descent in blood from the Barons of Gournay"
new_string: The genealogist Daniel Gurney called this "an incontestable proof of his descent in blood from the Barons of Gournay"
```

#### Op 59 — Highlights bullet 3: DG acronym

```str_replace
old_string: DG identified this as "in all probability the William de Gournay 1st of our Record."
new_string: Daniel Gurney identified this as "in all probability the William de Gournay 1st of our Record."
```

#### Op 60 — Narrative para 4: DG acronym

```str_replace
old_string: DG correctly distinguishes the two Williams:
new_string: Daniel Gurney correctly distinguishes the two Williams:
```

#### Op 61 — Timeline 1167 row: DG-I acronym removed

```str_replace
old_string: Attested as living (DG-I reference).
new_string: Attested as living.
```

---

### G31 — Walter de Gournay

**File:** `fact-sheets/g31-walter-de-gournay-fact-sheet.md`

#### Op 62 — Vitals Born: role modifier

```str_replace
old_string: Daniel Gurney suggested he may have been named after his father's kinsman <a href="https://en.wikipedia.org/wiki/Walter_Giffard,_1st_Earl_of_Buckingham">Walter Giffard, Earl of Buckingham</a>, or after Walter de la Ferté.
new_string: The genealogist Daniel Gurney suggested he may have been named after his father's kinsman <a href="https://en.wikipedia.org/wiki/Walter_Giffard,_1st_Earl_of_Buckingham">Walter Giffard, Earl of Buckingham</a>, or after Walter de la Ferté.
```

#### Op 63 — Highlights bullet 2: evidence-base meta trimmed

```str_replace
old_string: Combined with the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a> entry and the <a href="https://en.wikipedia.org/wiki/Parage">parage</a> tenure of Montigny-sur-Andelle held by Walter's son, the junior branch's descent from Gerard is established through three independent evidentiary chains.
new_string: The same Gournay-blood descent is independently anchored by Walter's <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a> entry and by the <a href="https://en.wikipedia.org/wiki/Parage">parage</a> tenure of Montigny-sur-Andelle that his son later held.
```

#### Op 64 — Narrative para 3: evidence-base meta trimmed

```str_replace
old_string: Three independent evidentiary chains — the *Liber Niger*, the parage tenure, and the *Les Olim* ruling — converge to confirm Walter's descent from Gerard.
new_string: The *Liber Niger*, the parage tenure, and the *Les Olim* ruling independently confirm Walter's descent from Gerard.
```

#### Op 65 — Narrative para 5: "Confirmed" classification sentence deleted

```str_replace
old_string: 

He is classified as **Confirmed** on the basis of these converging evidence streams.

new_string: 

```

---

### G32 — Gerard de Gournay

**File:** `fact-sheets/g32-gerard-de-gournay-fact-sheet.md`

#### Op 66 — Highlights bullet 1: Latin gloss added

```str_replace
old_string: and died <em>en route</em>: "<em>Hierosolymam petens in ipso itinere mortuus est</em>." The Beauvais church preserved his death-day
new_string: and died <em>en route</em>: "<em>Hierosolymam petens in ipso itinere mortuus est</em>" — "Seeking Jerusalem, he died on the journey itself." The Beauvais church preserved his death-day
```

#### Op 67 — Highlights bullet 3 header: Norman French gloss

```str_replace
old_string: <strong>His daughter *la belle Gondrée* married into the Mowbray line.</strong>
new_string: <strong>His daughter Gundred — *la belle Gondrée* (the beautiful Gondred) — married into the Mowbray line.</strong>
```

#### Op 68 — Narrative para 2: caput baroniae gloss

```str_replace
old_string: the barony centred on <a href="https://en.wikipedia.org/wiki/Caister-on-Sea">Caister-by-the-Sea</a> became the Gournay *caput baroniae* in England.
new_string: the barony centred on <a href="https://en.wikipedia.org/wiki/Caister-on-Sea">Caister-by-the-Sea</a> became the Gournay *caput baroniae* (chief seat of the barony) in England.
```

---

### G33 — Hugh de Gournay III

**File:** `fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`

#### Op 69 — Highlights bullet 4: Latin gloss

```str_replace
old_string: "Salute the Lord Hugh de Gournay, *dilectissimum nostrum*, and the Lady Basilia, on my part, as sweetly as you can."
new_string: "Salute the Lord Hugh de Gournay, *dilectissimum nostrum* (our most beloved), and the Lady Basilia, on my part, as sweetly as you can."
```

---

### G34 — Hugh de Gournay II

**File:** `fact-sheets/g34-hugh-de-gournay-ii-fact-sheet.md`

#### Op 70 — Vitals Marriage: role modifier

```str_replace
old_string: Hannay noted: "Who his wife was — Frank or Norman — we cannot tell."
new_string: The historian Hannay observed: "Who his wife was — Frank or Norman — we cannot tell."
```

#### Op 71 — Highlights bullet 1: evidence-base meta trimmed

```str_replace
old_string: The Conqueror's own biographer, <a href="https://en.wikipedia.org/wiki/William_of_Poitiers">William of Poitou</a>, names Hugh ("Hugonis Gornacensis") as ally of Robert d'Eu in the years right after Mortemer — a named primary-source attestation of the alliance independent of the chronicle tradition.
new_string: The Conqueror's own biographer, <a href="https://en.wikipedia.org/wiki/William_of_Poitiers">William of Poitou</a>, names Hugh ("Hugonis Gornacensis") as ally of Robert d'Eu in the years right after Mortemer.
```

#### Op 72 — Narrative para 3: Latin gloss

```str_replace
old_string: Duke William personally chose Hugh as one of his *fortissimi viri*
new_string: Duke William personally chose Hugh as one of his *fortissimi viri* (strongest men)
```

#### Op 73 — Narrative para 6: role modifier added

```str_replace
old_string: Daniel Gurney himself doubted the attribution, proposing that "Cardiff" was a scribal corruption for Norwich or Caistor
new_string: The genealogist Daniel Gurney himself doubted the attribution, proposing that "Cardiff" was a scribal corruption for Norwich or Caistor
```

---

### G35 — Renaud de Gournay

**File:** `fact-sheets/g35-renaud-de-gournay-fact-sheet.md`

#### Op 74 — Highlights bullet 4: role modifier added

```str_replace
old_string: Hannay placed Renaud "just into the transition time
new_string: The historian Hannay placed Renaud "just into the transition time
```

#### Op 75 — Narrative para 2: internal classification labels removed

```str_replace
old_string: The charter is close enough in time to Renaud's active years to be reliable, and it is the benchmark against which his status is classified as **Confirmed** rather than Uncertain or Tradition.
new_string: The charter is close enough in time to Renaud's active years to be reliable evidence that he held the lordship.
```

---

### G36 — Hugh de Gournay I

**File:** `fact-sheets/g36-hugh-de-gournay-i-fact-sheet.md`

#### Op 84 — Highlights bullet 1: Hannay role modifier

```str_replace
old_string: Hannay described how "feudalism could do nothing without castles.
new_string: The historian Hannay described how "feudalism could do nothing without castles.
```

#### Op 85 — Highlights bullet 1: Daniel Gurney role modifier + italic *Supplement*

```str_replace
old_string: Daniel Gurney's 1858 Supplement confirms the tower was still standing "a century ago"
new_string: Genealogist Daniel Gurney's 1858 <em>Supplement</em> confirms the tower was still standing "a century ago"
```

---

### G37 — Eudes (Odon) de Gournay

**File:** `fact-sheets/g37-eudes-de-gournay-fact-sheet.md`

#### Op 86 — Highlights bullet 1: Hannay role modifier

```str_replace
old_string: James Hannay, writing in 1867, called the Gournay pedigree one of the longest Norse pedigrees extant
new_string: The historian James Hannay, writing in 1867, called the Gournay pedigree one of the longest Norse pedigrees extant
```

#### Op 87 — Highlights bullet 6: French gloss

```str_replace
old_string: the 1844 N.-R. P. de la Mairie engraving series explicitly contrasts the two phases as "Premières armoiries" and "Secondes armoiries."
new_string: the 1844 N.-R. P. de la Mairie engraving series explicitly contrasts the two phases as "Premières armoiries" (first arms) and "Secondes armoiries" (second arms).
```

#### Op 88 — Narrative para 5: Daniel Gurney role modifier

```str_replace
old_string: <a href="https://en.wikipedia.org/wiki/Daniel_Gurney">Daniel Gurney</a>, writing in 1848 after years of research in Norman archives, explicitly acknowledged
new_string: The genealogist <a href="https://en.wikipedia.org/wiki/Daniel_Gurney">Daniel Gurney</a>, writing in 1848 after years of research in Norman archives, explicitly acknowledged
```

#### Op 89 — Narrative para 5: internal classification labels removed

```str_replace
old_string: The tradition is classified here as **Tradition** rather than Confirmed, but the case for Eudes's real existence is strong.
new_string: Eudes's existence rests on later tradition rather than contemporary document, but the case for him as a real person is strong.
```

---

## Validation checklist (Phase 2)

After the str_replace operations have been applied, verify:

- [ ] All 20 fact-sheet files render without broken HTML (footnote anchors, `<sup>` / `<a>` tags, `<em>` / `<strong>` balanced).
- [ ] No remaining `DG` / `DG-I` / `DG-Supp` acronyms in visible body or footnote text of any of the 20 fact sheets (grep `\bDG\b`, `DG-I`, `DG-Supp` under `fact-sheets/g1[8-9]*`, `fact-sheets/g2*`, `fact-sheets/g3[0-7]*`).
- [ ] No remaining `COLLATERAL` labels in any of the 20 children tables (grep `COLLATERAL`).
- [ ] No remaining `**Confirmed**` / `**Tradition**` / `**Uncertain**` classification meta in narrative prose of the 20 fact sheets.
- [ ] No remaining "source layer" / "citation layer" / "See Research Appendix" / "G20 companion" / "G20 research companion" / "prize to pull" / "pre-DG witness" repo-internal vocabulary in the 20 fact sheets.
- [ ] G28 children-table mother column reads "Katherine (de Ingoldesthorpe)" in all three rows; vitals marriage cell, highlights bullet, narrative para 2 lead, and timeline 1243 row all reflect the Ingoldesthorpe identification; footnotes n4 and n7 carry the new apparatus.
- [ ] No `nNEW`-style footnote placeholders introduced.
- [ ] All in-body footnote anchor links resolve to a defined `id` in the same fact sheet.

## Phase 2 completion step

After the validation checklist passes:

1. Delete `sources/intake/processed/_v74-fs-light-review-staging.md` (working file; the patchset captures the final operation log).
2. Confirm `sources/intake/processed/stub-v75.md` exists (created when this patchset was promoted from `stub-v74.md`).
3. Prepend a top-line `**Done:** YYYY-MM-DD HH:MM PT` stamp to this file.
4. Move this file from `sources/intake/processed/` to `sources/intake/done/`.

No `data/sources.json`, validation, or research-companion edits are needed; this is a prose-revision patchset only.
