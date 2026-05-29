**Done:** 2026-05-28 19:17 PT

# v73 patchset — five pre-19c printed witnesses (Holinshed 1577, Daniel 1613, Echard-tradition Complete History 1706, Rudder 1779, Tyrwhitt 1798) — corroborating and supplementary Gurney/Gourney references

Prepared: 2026-05-28
Phase: 1 preparation
Scope: register five hitherto-unrecorded printed witnesses spanning 1577–1798 as new project sources; absorb the substantively new findings into the senior-collateral topic file, the Somerset/Gloucestershire collateral place file, and the G34 Hugh II research companion; capture the verbatim primary extracts (most importantly Leland's full French epitaph for Sir Matheu de Gourney d. 1406 and Rudder's Gloucestershire-side Gaunt → Robert/Anselm/John → Elizabeth → John ap Adam descent for Over, Redwick, Northwick, and the Bristol Bilswick / Gaunt's Hospital foundation) in dedicated corpus-supplement files.

Companion in spirit to v69 (Armstrong 1781): a small bundle of derivative-but-source-traceable antiquarian witnesses that corroborate already-documented senior-line and collateral material and supply a few specific new findings, principally for the Hugh II "old Hugh died before the Conqueror" tradition, the Sir Matthew de Gournay (d. 1406, Stoke-sub-Hamdon) chapter, and the Maurice-de-Gaunt → Robert/Anselm/John → Elizabeth → John ap Adam Gloucestershire descent.

## Scope and architecture

User supplied (a) a free-standing pre-analysis note for Holinshed 1577 already in `sources/intake/processed/holinshed_1577_gurney_variant_research_notes.md`, plus (b) five URL-supplied leads with OCR extracts:

1. **Samuel Daniel**, *The First Part of the History of England* (London, 1613), p. ~142 — Hugh de Gourney named in the catalogue of Conqueror's "especial actors" who died before him.
2. **Thomas Tyrwhitt** (ed./annotator), *The Canterbury Tales of Chaucer* (London, 1798), vol. ii (Notes), p. 392 — full French Leland-derived epitaph for Sir Matheu de Gourney d. 1406, age 96.
3. ***A Complete History of England***, vol. 1 (London, 1706), p. 158 — Hugh de Gourney in the Richard I Holy Land valorous-men list.
4. ***A Complete History of England***, vol. 1 (London, 1706), p. 244 — Sir Mathew Gourney named with Edmund Earl of Cambridge in the 1381 Portugal expedition.
5. **Samuel Rudder**, *A New History of Gloucestershire* (Cirencester, 1779) — Almondsbury parish (Over manor + Gaunt's Urcot/Bilswick + Redwick) descent of the senior Gloucestershire-Somerset Gournay collateral through Maurice de Gaunt → Robert/Anselm/John de Gourney → Elizabeth → John ap Adam → Berkeley.

Holinshed 1577 (item 0) and Daniel 1613 (item 1) both transmit the broad Norman / Conquest / Angevin-war tradition for Hugh de Gourney; Tyrwhitt 1798 (item 2) preserves the Leland Sir-Matthew epitaph at length; *Complete History of England* (items 3–4) is a low-weight early-Hanoverian compendium worth capturing only as a corroborating-citation source; Rudder 1779 (item 5) is the substantively most important new finding, supplying an independent Gloucestershire-side 1779 witness to the senior-collateral chain already documented from Pettigrew (Somerset side), with one named-actor conflict (Rudder "Richard de Gourney" vs. Pettigrew's "Robert de Gournay II" as founder of the Bristol Bilswick / Gaunt's Hospital).

Per the patchset standard (one work = one source ID, bundle a research arc into one patchset), all five new printed sources land in one v73 patchset. Holinshed itself becomes the sixth new source — the prep-notes file is the working transcription layer behind it.

## Stub-state housekeeping

On entry: `sources/intake/processed/stub-v67.md` is the only live stub file, even though v67 through v72 have been promoted to live patchset files in the same directory. v72 plans to remove `stub-v67.md` and create `stub-v73.md`. v73 supersedes that name-creation step and instead idempotently clears any stale stubs and creates `stub-v74.md` per `.claude/rules/sources.md` ("If the stub is missing or stale, repair it with a one-time shallow scan and take the highest `vNN` found across processed/, processed/Ready/, processed/on-hold/, and done/").

## Source tracking

Six new source IDs:

- **`holinshed-chronicles-1577`** — Raphael Holinshed, *The laste volume of the Chronicles of England, Scotlande, and Irelande…*, vol. 2 (London, 1577). Internet Archive item `bim_early-english-books-1475-1640_the-laste-volume-of-the-_holinshed-raphael_1577`. The 1577 first edition; vol. 2 only (the IA copy lacks L3 of the index; pages torn and tightly bound with some loss of text; Fraktur/blackletter OCR is unreliable). The Oxford Holinshed Project's keyed 1577 transcription is the working searchable text layer. Useful as an Elizabethan printed witness to the Norman-Conquest-list, the late-12th-c. Hugh de Gourney as territorial-marker, the King-John-era Château Gaillard captaincy + Mountfort defection of Hugh de Gourney, the Edward-II-murder narrative naming "Thomas Gourney" (regicide), and the Sir Mathew Gourney 14th-c. campaign + procedural-legal references.
- **`daniel-history-england-1613-pt1`** — Samuel Daniel, *The First Part of the Historie of England* (London: Nicholas Okes, 1613). Internet Archive item `bim_early-english-books-1475-1640_the-first-part-of-the-hi_daniel-samuel_1613`. Daniel's narrative history; the p. ~142 passage names Hugh de Gourney in the catalogue of Conqueror's "especial actors" who died before him (alongside Beaumont, Harcourt, Vicount Neele, Hugh de Mortimer, Comte de Vennes) — an early-17th-c. printed witness to the same Norman-tradition material the G34 Hugh II companion already tracks across Powell 1584 (Welsh-chronicle 1094 reading), the *Histoire et Chronique de Normandie* (printed Rouen 1610, "1074" reading), Dumoulin 1631, and Calmet *Histoire de Lorraine*.
- **`complete-history-england-1706-v1`** — *A Complete History of England*, vol. 1 (London: Brab. Aylmer, A. and J. Churchill, etc., 1706). Internet Archive item `bim_eighteenth-century_a-complete-history-of-en_1706_1`. The three-volume 1706 *Complete History* compendium (compilation often associated with John Hughes and continuators including White Kennett); authorship of the early-medieval narrative chapters is unattributed in the volume. Useful only as a corroborating Hanoverian-era citation; the two Gurney references at p. 158 (Hugh de Gourney in the Richard I Holy Land list) and p. 244 (Sir Mathew Gourney in the 1381 Portugal expedition under Edmund Earl of Cambridge) repeat the pre-existing Holinshed / Pettigrew / chronicle tradition without adding new fact.
- **`rudder-gloucestershire-1779`** — Samuel Rudder, *A New History of Gloucestershire* (Cirencester: printed by Samuel Rudder, 1779). Internet Archive item `bim_eighteenth-century_a-new-history-of-glouces_rudder-samuel_1779`. The standard pre-Bigland antiquarian county history of Gloucestershire. Substantively important for the senior-collateral Gloucestershire descent: the Almondsbury parish entries record the descent of Over (= "Oure"), Gaunt's Urcot, and Redwick from Maurice de Gaunt (d. 1230, 14 H. III) to his sister's son Robert de Gourney (d. 53 H. III = 1268-69) and through Anselm → John → Elizabeth → John ap Adam → Thomas ap Adam → Berkeley. Provides one named-actor conflict with Pettigrew (Bristol Bilswick / Gaunt's Hospital founder: Rudder "Richard de Gourney" vs. Pettigrew "Robert de Gournay II").
- **`tyrwhitt-canterbury-tales-1798-v2`** — Thomas Tyrwhitt, ed., *The Canterbury Tales of Chaucer*, vol. ii (London, 1798) — the Notes volume of the standard late-18th-c. critical edition. Internet Archive item `bim_eighteenth-century_the-canterbury-tales-of-_chaucer-geoffrey_1798_2`. The note to *General Prologue* v. 43 (the Knight) at p. 392 reproduces the full French epitaph of Sir Matheu de Gourney from Leland's *Itinerary* (vol. iii p. xi) — "Icy gist le noble et vaillant Chivaler Matheu de Gourney … qui en sa vie fu a la bajaille de Benamaryn, et ala apres a la siege d'Algezire sur les Sarazines et aussi a les batailles de L'Escluse, de Crefcy, de Deyngeneffe, de Peyteres, de Nazare, d'Ozrey et a plusours autres batailles et affeges en les quex il gaigna noblement graunt los et honour" — and supplies the death year (1406) and age at death (96). Independent 18th-c. literary-critical witness to the same Leland epitaph already known to the project through Pettigrew 1871; the Tyrwhitt version is closer to Leland and supplies the verbatim French text in printed form.

The original 1577 Holinshed prep-notes file `sources/intake/processed/holinshed_1577_gurney_variant_research_notes.md` is the working transcription layer behind the `holinshed-chronicles-1577` source ID; Phase 2 moves it to `sources/intake/done/` alongside this patchset.

## Research-value assessment

Listed in order of weight.

### Substantively new

1. **Rudder 1779 — Maurice de Gaunt → Robert/Anselm/John de Gourney → Elizabeth → John ap Adam — Gloucestershire-side descent for Over, Redwick, Northwick.** Pettigrew 1871 already documents the Somerset-side same-chain descent (Anselm de Gournay's sons dividing the Harptree-Overwere-Inglishcombe houses; Robert II's union of Somerset Gournay + Harptree + FitzHarding-of-Weare inheritances). Rudder 1779 is the **independent Gloucestershire-side witness** for the same chain, applied to the Almondsbury parish manors:
   - Over: Maurice de A[wdele / Gaunt] d. 14 H. III (1229/30); to his sister's son Robert de Gourney d. 53 H. III (1268/9); Anselm de Gourney held it 14 Edw. I (1285/6); John de Gourney died seized 19 Edw. I (1290/1); to John ap Adam by marriage to Elizabeth daughter and heir of John de Gourney; Thomas ap Adam sold to Thomas lord Berkeley 4 Edw. III (1330/1).
   - Redwick: Maurice de Gaunt d. seized 6 H. III (1221/2); Robert de Gourney d. 53 H. III; son Anselm succeeded by John de Gourney; daughter Elizabeth married John Ap Adam; John and Elizabeth levied a fine of the manors of Redwick and Northwick 25 Edw. I (1296/7).
2. **Rudder 1779 — Gilbert de Gaunt → Richard de Gourney → Bilswick / Gaunt's Hospital, Bristol.** Rudder names *Richard* de Gourney as the founder of Gaunt's Hospital in his manor-house at Bilswick (Bristol), which Gilbert de Gaunt's nephew-and-heir founded for one hundred poor people. Pettigrew gives the corresponding founder as *Robert de Gournay II* in the Somerset collateral file. This is a **named-actor conflict** worth recording verbatim; both Rudder 1779 and Pettigrew 1871 are antiquarian compilations, the underlying primary record (the foundation charter) is the only authoritative tie-breaker.
3. **Tyrwhitt 1798 — full French Leland epitaph for Sir Matheu de Gourney, d. 1406 age 96.** Pettigrew 1871 already preserves a description of the Leland epitaph for the Stoke-sub-Hamdon monument, but Tyrwhitt prints the verbatim French text at length in his Canterbury-Tales note, supplies the death year (1406) and age (96), and frames Sir Matthew as a near-contemporary of Chaucer's fictional Knight. The verbatim French text, the named battles (Benamaryn = the Marinid campaign of c. 1340 in North Africa; siege of Algeciras 1342–44; L'Ecluse = Sluys 1340; Crécy 1346; Deyngenesse = Winchelsea 1350?; Peyteres = Poitiers 1356; Nazare = Nájera 1367; Ozrey = Auray 1364), and the explicit "et a plusours autres batailles et affeges" together constitute a primary-text anchor for the Sir Matthew campaign list that Pettigrew only summarises.
4. **Holinshed 1577 — Hugh de Gourney's castle "Fert" (= La Ferté) burned by Henry, Duke of Normandy** (vol. 4 p. 364, mid-1150s during Henry II's pre-accession Norman war against Stephen + French king). Names a **specific Hugh-de-Gournay-held castle** in the Vexin called "Fert" lost in the Angevin-Capetian conflict in the mid-1150s. The Hugh in question is most parsimoniously **Hugh IV** (the post-Hugh-III senior baron, the Bec-educated figure already covered in `anderson-yvery-harpetre-gournay-collateral.md`'s Anderson Vol. II material). The "Fert" reading likely points to **La Ferté-en-Bray** (already a known senior-collateral seat — see `research/places/la-ferte-en-bray.md`) — i.e., Holinshed preserves a 1150s-era loss of one of the la-Ferté castles by the Gournay senior line. **New senior-collateral attestation**.
5. **Holinshed 1577 — Hugh Gourney's lands as captivity site for Robert Earl of Leicester (Richard I era)** (vol. 4 p. 473). Robert Earl of Leicester is taken prisoner riding "unaduisedly" through Hugh Gourney's lands during Richard I's Norman war. Another late-12th-c. territorial-marker attestation for Hugh IV's Norman holdings. New for the senior-collateral topic file.
6. **Holinshed 1577 — Hugh de Gourney's Mountfort defection** (vol. 4 p. 557). Holinshed says Hugh de Gourney, having defended Château Gaillard for a month + against the French king during the 1203/4 siege, eventually defected to King Philip and **delivered the castle of Mountfort to the French king**. The Château Gaillard defense and the eventual fall are already documented; the Mountfort delivery as a specific defection-act of Hugh V is **new operational detail**. Note: this entry concerns Hugh V (d. 1214, forfeited 1205 — already extensively in the project).
7. **Holinshed 1577 — "Hue de Gourney alias Geneuay" (Conquest-list variant)** (vol. 4 p. 291). The unusual alias "Geneuay" attached to "Hue de Gourney" in Holinshed's Conquest-actor list is otherwise unattested in the project's name-variant catalogue (which already covers Gournay/Gurney/Gornay + the Eulde-Hugues equivalence at G34 §3.1, the Norse-Norman cluster, and the spelling cluster at G34 §16). The "Geneuay" form is likely an Elizabethan-era OCR/typographic corruption of an underlying source name; capture it as a documented variant but do not promote it to a working alias.
8. **Holinshed 1577 — Sir Mathew Gourney in legal-procedural role under the king** (vol. 4 p. 1118). Holinshed records Sir Mathew Gourney "sitting under the king" delivering a procedural ruling against the Earl of Salisbury in the Salisbury-vs-Morley protestation dispute: Salisbury cannot retroactively add a protestation that was not in his first answer. **New later-career office attestation for Sir Matthew de Gournay** beyond the military and Iberian-campaign material in Pettigrew + `somerset-gournay-collateral.md`.

### Corroborating-only (low weight)

9. **Daniel 1613** — Hugh de Gourney named among the Conqueror's "especial actors" who died before him. Adds a 1613 printed witness to the same "old Hugh died before 1087 in Normandy" tradition the G34 Hugh II companion §6 already tracks across multiple Norman / Lorraine / Welsh sources. Footnote-level corroboration.
10. **Complete History of England 1706 vol. 1 p. 158** — Hugh de Gourney in the Richard I Holy Land valorous-men list. Same content as Holinshed 1577 vol. 4 p. 473. Pure Hanoverian-era repetition of older chronicle material; footnote-level corroboration.
11. **Complete History of England 1706 vol. 1 p. 244** — Sir Mathew Gourney in the 1381 Portugal expedition under Edmund Earl of Cambridge. Same content as the *Calendar of Patent Rolls Henry IV* and Pettigrew already in `somerset-gournay-collateral.md`. Footnote-level corroboration.

### Already-published facts (no new content; cite optionally)

- Holinshed 1577 — Thomas Gourney as keeper of Edward II at Berkeley, the murder narrative, the flight to Marseilles, and the death-at-sea (vol. 4 p. 846). Long-known regicide narrative; already substantially treated through Pettigrew and modern Edward-II scholarship; v73 captures the verbatim Holinshed passage in the corpus supplement for completeness but does not introduce it to the senior- or Somerset-collateral research files.
- Holinshed 1577 — Sir Mathew Gourney in the second division at Auray (vol. 4 p. 884); Sir Mathew with Cambridge / Beauchamp / Botreux to Portugal (vol. 4 p. 1003). Already covered (Pettigrew, CPR Henry IV).
- Holinshed 1577 — Gourney (place) in King John, Henry V, Henry VI Norman / Vexin campaigns (vol. 4 pp. 541, 553, 1164, 1219). These are about the Norman town of **Gournay-en-Bray** as a contested military objective, not about the family; already in the project place-history layer. The v73 corpus supplement preserves the verbatim passages; no research-file edits.

## Outcomes

| Item | Outcome | Destination |
|---|---|---|
| Holinshed 1577 | promote as new source ID | `data/sources.json`; `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md`; `sources/validations/holinshed-chronicles-1577.md`; downstream routing to `research/topics/senior-gournay-baron-line-collateral.md` (Hugh "Fert" castle + Hugh Gourney's lands + Mountfort defection), `research/places/somerset-gournay-collateral.md` (Sir Matthew procedural-legal role), and `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md` (Hue de Gourney alias Geneuay) |
| Daniel 1613 | promote as new source ID | `data/sources.json`; `sources/corpus_supplement/daniel-history-england-1613-pt1-gurney-extract.md`; `sources/validations/daniel-history-england-1613-pt1.md`; downstream to G34 companion §6 |
| Complete History of England 1706 v1 | promote as new source ID (low weight) | `data/sources.json`; `sources/corpus_supplement/complete-history-england-1706-v1-gurney-extracts.md`; `sources/validations/complete-history-england-1706-v1.md`; one-line footnote-corroboration additions in senior-collateral topic + Somerset-collateral place file |
| Rudder 1779 | promote as new source ID | `data/sources.json`; `sources/corpus_supplement/rudder-gloucestershire-1779-gurney-extracts.md`; `sources/validations/rudder-gloucestershire-1779.md`; downstream to `research/places/somerset-gournay-collateral.md` (Gloucestershire-side descent of Over, Redwick, Northwick, Gaunt's Urcot/Bilswick) |
| Tyrwhitt 1798 | promote as new source ID | `data/sources.json`; `sources/corpus_supplement/tyrwhitt-canterbury-tales-1798-v2-matheu-gourney-epitaph.md`; `sources/validations/tyrwhitt-canterbury-tales-1798-v2.md`; downstream to `research/places/somerset-gournay-collateral.md` (verbatim French Leland epitaph for Sir Matheu de Gourney d. 1406 age 96) |
| Holinshed prep-notes file | retain in `sources/intake/` and move to `done/` alongside this patchset in Phase 2 | `sources/intake/done/holinshed_1577_gurney_variant_research_notes.md` |

No item rejected.

## Phase 2 operations

### 1. Add six new source IDs to `data/sources.json`

File: `data/sources.json`.

Insert the six new entries inside the closing brace of the `"sources"` object. Anchor on the last existing entry (`norwich-records-hudson-tingey-vol2`):

```str_replace
old_string:     "norwich-records-hudson-tingey-vol2": {
      "shortTitle": "Hudson and Tingey -- Records of the City of Norwich, vol. ii (1910)",
      "citation": "William Hudson and John Cottingham Tingey, eds., The Records of the City of Norwich (Norwich and London: Jarrold, 1910), vol. ii.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/recordsofcityofn02norwuoft",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Vol. ii of the Hudson-Tingey edition. Used in v63 for the City Treasurers' Accounts entries at pp. 44 and 47 recording two annual fee payments of 20 shillings each to 'Edmund Gornay', paid in the same fee paragraph as the 20s paid to Edmund de Clipesby. Direct primary attestation behind Blomefield's general standing-counsel reference and the History of Parliament biography of Sir John Gurney V."
    }
  }
}
new_string:     "norwich-records-hudson-tingey-vol2": {
      "shortTitle": "Hudson and Tingey -- Records of the City of Norwich, vol. ii (1910)",
      "citation": "William Hudson and John Cottingham Tingey, eds., The Records of the City of Norwich (Norwich and London: Jarrold, 1910), vol. ii.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/recordsofcityofn02norwuoft",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/norwich-records-hudson-tingey-vol2-edmund-gornay-fees.md",
      "mediaPath": null,
      "validationPath": null,
      "notes": "Vol. ii of the Hudson-Tingey edition. Used in v63 for the City Treasurers' Accounts entries at pp. 44 and 47 recording two annual fee payments of 20 shillings each to 'Edmund Gornay', paid in the same fee paragraph as the 20s paid to Edmund de Clipesby. Direct primary attestation behind Blomefield's general standing-counsel reference and the History of Parliament biography of Sir John Gurney V."
    },
    "holinshed-chronicles-1577": {
      "shortTitle": "Holinshed, Chronicles of England, Scotlande, and Irelande (1577) -- laste volume",
      "citation": "Raphael Holinshed, The laste volume of the Chronicles of England, Scotlande, and Irelande, with their descriptions (London, 1577), vol. 2.",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/bim_early-english-books-1475-1640_the-laste-volume-of-the-_holinshed-raphael_1577",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/holinshed-1577-selected-gurney-references.md",
      "mediaPath": null,
      "validationPath": "sources/validations/holinshed-chronicles-1577.md",
      "notes": "First edition of the laste volume; vol. 2 only. The IA copy lacks L3 of the index; pages torn and tightly bound with some loss of text; OCR (Tesseract, detected Fraktur/blackletter) is unreliable. The Oxford Holinshed Project's keyed 1577 transcription is the working searchable text layer. v73 captures 14 Gurney-variant loci under the spellings Gourney / Gournay / Gurnay / Gurney / Gorney / Geneuay (alias). Substantively new findings: Hugh de Gourney's castle 'Fert' (= La Ferte) burned by Duke Henry of Normandy mid-1150s; Hugh Gourney's lands as captivity site for Robert Earl of Leicester (Richard I era); Hugh's delivery of the castle of Mountfort to the French king after Chateau Gaillard 1204; the unusual alias 'Geneuay' attached to Hue de Gourney in the Conquest-list; Sir Mathew Gourney's procedural-legal role under the king (Salisbury vs Morley). Already-known content captured in the corpus supplement for completeness: the Thomas Gourney regicide narrative, Sir Mathew at Auray and Portugal, and the Gournay-en-Bray place references in the Henry V / Henry VI Norman/Vexin campaigns."
    },
    "daniel-history-england-1613-pt1": {
      "shortTitle": "Daniel, First Part of the Historie of England (1613)",
      "citation": "Samuel Daniel, The First Part of the Historie of England (London: Nicholas Okes, 1613).",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/bim_early-english-books-1475-1640_the-first-part-of-the-hi_daniel-samuel_1613",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/daniel-history-england-1613-pt1-gurney-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/daniel-history-england-1613-pt1.md",
      "notes": "Early-17th-c. narrative history. The p. ~142 passage groups Hugh de Gourney with Beaumont, Harcourt, Vicount Neele, Hugh de Mortimer, and the Comte de Vennes as 'especial actors' of the Conquest who died before the Conqueror (d. 1087). One more printed witness to the same 'old Hugh died before the Conqueror' Norman tradition already tracked at G34 Hugh II companion section 6 across Powell 1584, the Histoire et Chronique de Normandie (printed Rouen 1610), Dumoulin 1631, and Calmet's Histoire de Lorraine."
    },
    "complete-history-england-1706-v1": {
      "shortTitle": "A Complete History of England, vol. 1 (1706)",
      "citation": "A Complete History of England, with the Lives of all the Kings and Queens thereof, vol. 1 (London: Brab. Aylmer, A. and J. Churchill, etc., 1706).",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/bim_eighteenth-century_a-complete-history-of-en_1706_1",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/complete-history-england-1706-v1-gurney-extracts.md",
      "mediaPath": null,
      "validationPath": "sources/validations/complete-history-england-1706-v1.md",
      "notes": "Three-volume compilation often associated with John Hughes and continuators (later editions incorporating White Kennett's continuation). Authorship of the early-medieval narrative chapters is unattributed in the volume. Used in v73 only as a Hanoverian-era corroborating-citation source for two known Gurney references: p. 158 (Hugh de Gourney in the Richard I Holy Land valorous-men list, same content as Holinshed 1577 vol. 4 p. 473) and p. 244 (Sir Mathew Gourney in the 1381 Portugal expedition under Edmund Earl of Cambridge, same content as the CPR Henry IV and Pettigrew). No new fact."
    },
    "rudder-gloucestershire-1779": {
      "shortTitle": "Rudder, A New History of Gloucestershire (1779)",
      "citation": "Samuel Rudder, A New History of Gloucestershire (Cirencester: printed by Samuel Rudder, 1779).",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/bim_eighteenth-century_a-new-history-of-glouces_rudder-samuel_1779",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/rudder-gloucestershire-1779-gurney-extracts.md",
      "mediaPath": null,
      "validationPath": "sources/validations/rudder-gloucestershire-1779.md",
      "notes": "The standard pre-Bigland antiquarian county history of Gloucestershire, single folio volume. Substantively important for the senior-collateral Gloucestershire descent. The Almondsbury parish entries record: (a) Over manor descent from Maurice de A[wdele / Gaunt] d. 14 H. III via his sister's son Robert de Gourney (d. 53 H. III), then Anselm 14 Edw. I, then John d. 19 Edw. I, then Elizabeth and John ap Adam, then sale to Berkeley 4 Edw. III; (b) Gaunt's Urcot descent from Gilbert de Gaunt to his sister's son and heir Richard de Gourney, who founded an hospital at Bilswick (= Gaunt's Hospital, Bristol) for one hundred poor; (c) Redwick manor descent in the same Gaunt -> Gourney -> Elizabeth -> ap Adam chain, with the Redwick + Northwick fine levied 25 Edw. I. The Bristol Bilswick / Gaunt's Hospital founder named by Rudder as 'Richard de Gourney' conflicts with Pettigrew 1871's 'Robert de Gournay II' attribution; preserved as a documented name conflict pending primary-record check."
    },
    "tyrwhitt-canterbury-tales-1798-v2": {
      "shortTitle": "Tyrwhitt ed., Canterbury Tales of Chaucer, vol. ii Notes (1798)",
      "citation": "Thomas Tyrwhitt, ed., The Canterbury Tales of Chaucer, vol. ii (London, 1798).",
      "archive": "Internet Archive",
      "url": "https://archive.org/details/bim_eighteenth-century_the-canterbury-tales-of-_chaucer-geoffrey_1798_2",
      "corpusStatus": "supplement",
      "corpusPath": "sources/corpus_supplement/tyrwhitt-canterbury-tales-1798-v2-matheu-gourney-epitaph.md",
      "mediaPath": null,
      "validationPath": "sources/validations/tyrwhitt-canterbury-tales-1798-v2.md",
      "notes": "Notes volume of Tyrwhitt's standard late-18th-c. critical edition of Chaucer. The note to General Prologue v. 43 (the Knight) at p. 392 reproduces the full French epitaph of Sir Matheu de Gourney from Leland's Itinerary (vol. iii p. xi), names the campaigns (Benamaryn, siege of Algezire, L'Escluse, Crefcy, Deyngeneffe, Peyteres, Nazare, Ozrey, et plusours autres batailles), and supplies the death year 1406 and age 96. Closer to Leland than Pettigrew's later paraphrase; supplies verbatim French text. Tyrwhitt frames Sir Matthew as a near-contemporary of Chaucer's fictional Knight and notes Chaucer's puzzling choice of Alexandria + Lettowe rather than Crecy + Poitiers as the Knight's listed campaigns."
    }
  }
}
```

### 2. Write the Holinshed 1577 corpus supplement

New file write: `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md`.

```markdown
# Holinshed, Chronicles of England, Scotlande, and Irelande (1577), laste volume -- selected Gurney references

Source ID: `holinshed-chronicles-1577`

Source: Raphael Holinshed, *The laste volume of the Chronicles of England, Scotlande, and Irelande, with their descriptions*, vol. 2 (London, 1577). Internet Archive item `bim_early-english-books-1475-1640_the-laste-volume-of-the-_holinshed-raphael_1577`. The IA copy lacks L3 of the index; pages torn and tightly bound with some loss of text; Fraktur/blackletter OCR is unreliable. The verbatim transcriptions below are normalised from the Oxford Holinshed Project's keyed 1577 transcription, cross-checked against the IA target. Long-s is normalised to modern `s`; obvious OCR slips are silently corrected when they touch a Gurney reading and are flagged inline where they materially affect interpretation.

Volume hit-index: see `sources/intake/done/holinshed_1577_gurney_variant_research_notes.md` for the 14-locus working triage (Conquest list at p. 291; Hugh's "Fert" castle at p. 364; Holy Land valorous-men list and Earl of Leicester captivity at p. 473; King-John-era place references at pp. 541, 553; Chateau Gaillard + Mountfort defection at p. 557; Edward II murder narrative at p. 846; Sir Mathew at Auray at p. 884; Sir Mathew to Portugal at p. 1003; Sir Mathew procedural-legal role at p. 1118; Henry V Vexin places at p. 1164; Henry VI Normandy places at p. 1219).

---

## Vol. 4, p. 291 -- Conquest list, Battle Abbey Roll, name variants

Holinshed prints a catalogue of the noble captains and gentlemen who, per William Tailleur, assisted Duke William at the Conquest. Within that list:

> Hue de Gourney, alias Geneuay.

A little later in the same catalogue:

> Hue erle of Gournay.

In the following Battle Abbey Roll section, under the letter G, the forms include:

> Gurnay.
> Gurney.

Annotation: The alias `Geneuay` attached to Hue de Gourney is otherwise unattested in the project's name-variant catalogue and is most plausibly an Elizabethan-era OCR/typographic corruption of an underlying source name (compare the Eulde-Hugues equivalence already in G34 Hugh II companion section 3.1, and the Gournay/Gurney/Gornay spelling cluster). Capture as a documented variant; do not promote to a working alias without corroboration.

---

## Vol. 4, p. 364 -- Hugh de Gourney's castle "Fert" burned by Duke Henry of Normandy

After Henry Duke of Normandy married Eleanor of Aquitaine, the French king made war on him. Henry retaliated by burning several castles, including one belonging to Hugh de Gourney named `Fert`:

> After this, Duke Henry entred into the territories of King Stephan, and brent certeine Castels that belonged to the sayde King, and also a Castell that belonged to Hugh de Gourney called Fert, but the French king tooke Vernon...

Annotation: Mid-1150s, in the Angevin-Capetian-Norman conflict environment that precedes Henry II's English accession. The "Fert" reading most plausibly points to **La Ferte-en-Bray** -- already a documented senior-collateral seat in this project (see `research/places/la-ferte-en-bray.md`). The Hugh in question is most parsimoniously **Hugh IV** (the post-Hugh-III senior baron, the Bec-educated figure already covered in `research/topics/anderson-yvery-harpetre-gournay-collateral.md`'s Anderson Vol. II material).

---

## Vol. 4, p. 473 -- Hugh de Gourney in the Richard I Holy Land valorous-men list

After narrating Richard I's successful caravan-seizure during the Third Crusade, Holinshed adds the list of men whose Holy Land exploits "deserue of righte to be registred in bookes of perpetuall memorie":

> ... Robert Earl of Leicester, Hugh Bardolph, William Marshal Earl of Pembroke, ... **Hugh de Gourney**, William de Borrez, Wakeline de Ferrers, Roger ... and William Teutch the King's Standard-Bearer, who all shewed their Valour in the Holy Land.

---

## Vol. 4, p. 473 -- Robert Earl of Leicester captured in Hugh Gourney's lands

In a later Richard I context after the king came into Normandy:

> In the same season Robert Erle of Leicester, with a small companye of Souldiers, came unto the Castel of Passey, which Castel hee wanne ... and as he adventured himselfe somewhat unadvysedly in the **landes of Hugh Gourney**, he was taken prisoner ...

Annotation: Late-12th-c. territorial-marker attestation. Hugh Gourney here = Hugh IV. The passage implies Hugh's Norman lands were a recognised zone of contested military movement during Richard I's conflict with Philip Augustus.

---

## Vol. 4, p. 541 -- Gorney in the King John / Arthur of Brittany Norman war

> In an other part, an army of Britaines with great diligence wanne the Townes of Gorney, Butenant and Gensolin...

Annotation: Place reference (Norman town, almost certainly Gournay-en-Bray). The unusual `Gorney` spelling is documented but not treated as a Gurney-family form. The 1577 text then says the victorious Bretons went on toward Angers and took the city.

---

## Vol. 4, p. 541 / p. 553 -- French king wins Gourney during the war against King John

> After this ... the French K. wan Gourney, and then returning to the Citie of Mans, he appoynted Arthur duke of Britaine, to go into Poictou...

Annotation: Part of Philip Augustus's 1202-1204 campaign sequence that culminated in the loss of Normandy. Place reference to the Norman town.

---

## Vol. 4, p. 557 -- Hugh de Gourney defends Chateau Gaillard then defects, delivering Mountfort to the French king

The French king besieges Chateau Gaillard. Holinshed credits Hugh de Gourney with a stout defence:

> ... he went to Castel Galiard, which he besieged; and though by the high valiancie of Hugh de Gourney the Captayne there, the French men were manfully beaten backe, and kept out for a month and more...

The castle eventually fell. Holinshed then says:

> Hugh de Gourney revolteth from king John. And in the ende the sayde Hugh Gourney reuolted from his obedience, delivering also the **Castell of Mountforte** unto the Frenche King...

Annotation: This is **Hugh V** (forfeited 1205, d. 1214) -- the figure extensively documented in `research/topics/anderson-yvery-harpetre-gournay-collateral.md`, the Farrer feudal-tenure material, and Anderson Vol. II Book VII. The Chateau Gaillard defence and the eventual fall are already on the project's senior-line record. The Mountfort delivery as a specific defection-act of Hugh V is new operational detail.

---

## Vol. 4, p. 846 -- Thomas Gourney as keeper of Edward II at Berkeley, murder narrative

Holinshed records that Berkeley was removed as Edward II's keeper because he treated the deposed king too gently, and that Thomas Gourney replaced him as one of the harsher keepers. With Lord Matreuers, Gourney moved Edward from place to place and ultimately brought him back to Berkeley, where Edward was murdered at night. After the murder, the Queen and the Bishop proclaimed that any man accusing the doers should be killed. Thomas Gourney fled to Marseille, was eventually captured, and was killed at sea on the way back to England.

Annotation: Long-known Edward II regicide narrative. Already substantially treated through Pettigrew, `research/places/somerset-gournay-collateral.md`, and modern Edward-II scholarship. Captured verbatim here for completeness; no research-file edits in v73. The spelling `Gourney` is clear in this Holinshed witness.

---

## Vol. 4, p. 884 -- Sir Mathew Gourney commands second division at Auray (1364)

In a Brittany campaign involving Mountford and Charles of Blois:

> The second battaile was led by Sir Oliver de Clisson, Sir Eustace Daubreticourt, and **sir Mathew Gourney**.

Annotation: Already on the project record via Pettigrew + `research/places/somerset-gournay-collateral.md`. Likely the Battle of Auray, 1364.

---

## Vol. 4, p. 1003 -- Sir Mathew Gourney sent to Portugal (1381)

> The Earle of Cambridge, the Lorde William de Beauchampe, the Lorde Botreux, and **sir Mathew Gourney**, were sent into Portugall with fiue hundred armed men, and fiue hundred Archers, to aide the king of Portugall against the king of Castile...

Annotation: Already on the project record via Pettigrew, the *Calendar of Patent Rolls Henry IV*, and `research/places/somerset-gournay-collateral.md`. Tied to John of Gaunt's Castile-claim via Constance.

---

## Vol. 4, p. 1118 -- Sir Mathew Gourney in legal-procedural role under the king

In a proceeding involving the Earl of Salisbury and Lord Morley, Salisbury tries to have a protestation entered. Lord Morley objects that no such protestation was included in Salisbury's first answer. Holinshed then has Sir Mathew Gourney speak:

> Sir Mathew Gourney sitting under the king, said to the Erle of Salisbury, that sith hee had made no such protestation in his first answer ... he was now past the aduantage thereof ...

Gourney asks whether Salisbury has anything else to say.

Annotation: **New later-career office attestation** for Sir Matthew de Gournay beyond the existing military / Iberian-campaign material. Suggests he held standing or judicial authority in a high-level proceeding -- consistent with the procedural / standing-counsel role Pettigrew documents for his Stoke-sub-Hamdon Somerset career and the four Henry IV commission-of-the-peace / commission-of-array attestations 1399-1400 already captured in `research/places/somerset-gournay-collateral.md` notes 40-41.

---

## Vol. 4, p. 1164 -- Gourney yields to Henry V; Sir Gilbert Umfreville made captain

During Henry V's Vexin campaigns after the fall of Gisors and Chateau Gaillard:

> ... divers other Townes and Castels within the Countrey of Veulquessine yielded themselves to the obedience of the Englishmen, as **Gourney**, Chaumount, Neaufie, Dangu ...

> ... sir Gilbert Umfrevile was made Captaine ...

Annotation: Place reference (Norman town).

---

## Vol. 4, p. 1219 -- Sir Thomas Kiriell departs from Gourney; Warwick before Gourney; Arundel comes to Gourney before Gerberoy

> Sir Thomas Kiriell departed from Gourney in Normandie, with four hundred Englishmen ... and came before the Towne of Cleremont ...

> Richard Beauchampe Earle of Warwicke ... had a great skyrmishe before the towne of Gourney ...

> ... the Erle of Arundel ... came to Gourney, where hee heard tell how there was a Castell newly fortified at Gerboroy ...

Annotation: Three Henry-VI-era place references at Gourney-en-Bray as an English-held base in the late Hundred Years' War. Useful for any future Gournay-en-Bray place-history expansion.
```

### 3. Write the Daniel 1613 corpus supplement

New file write: `sources/corpus_supplement/daniel-history-england-1613-pt1-gurney-extract.md`.

```markdown
# Daniel, The First Part of the Historie of England (1613) -- Gurney extract

Source ID: `daniel-history-england-1613-pt1`

Source: Samuel Daniel, *The First Part of the Historie of England* (London: Nicholas Okes, 1613). Internet Archive item `bim_early-english-books-1475-1640_the-first-part-of-the-hi_daniel-samuel_1613`. OCR is mediocre but legible; long-s and obvious OCR slips silently normalised below.

## p. ~142 -- Hugh de Gourney named among Conqueror's "especial actors" who died before him

Daniel narrates the closing years of the Conqueror's reign. Among the laments for the men who died "before him" (i.e., in his lifetime, having been the chief actors of the Conquest):

> And this was in the fate of the Conquerour, to see most of all these men who had bene the especial actors in [the Conquest] ... extinct before him: As Beaumont, Harcourte, **Hugh de Gourney**, Vicount Neele, Hugh de Mortimer, Conte de Vennes, &c. And now [he] disposing [of his affairs] ended it [his life] in the 74. yeere of his age, and the 21. of his raigne.

Annotation: Independent early-17th-c. printed witness to the same Norman-tradition material the G34 Hugh II companion section 6 already tracks across Powell 1584 (the Welsh-chronicle "1094" reading), the *Histoire et Chronique de Normandie* (printed Rouen 1610, the "1074" reading), Dumoulin 1631, and Calmet's *Histoire de Lorraine*. Daniel's list (Beaumont, Harcourt, Hugh de Gourney, Vicount Neele, Hugh de Mortimer, Comte de Vennes) overlaps strongly with the same named-companion cluster that recurs across the Cardiff / Norveck legend: the "especial actors" of the Conquest who all died before William.
```

### 4. Write the Complete History of England 1706 v1 corpus supplement

New file write: `sources/corpus_supplement/complete-history-england-1706-v1-gurney-extracts.md`.

```markdown
# A Complete History of England, vol. 1 (1706) -- Gurney extracts

Source ID: `complete-history-england-1706-v1`

Source: *A Complete History of England, with the Lives of all the Kings and Queens thereof*, vol. 1 (London: Brab. Aylmer, A. and J. Churchill, etc., 1706). Internet Archive item `bim_eighteenth-century_a-complete-history-of-en_1706_1`. Three-volume compilation; authorship of early-medieval narrative chapters is unattributed in the volume (compilation often associated with John Hughes and continuators; White Kennett supplied the William-and-Anne continuation in later editions). OCR fair; long-s normalised.

## p. 158 -- Hugh de Gourney in the Richard I "Remarkable Occurrences" list of valorous men in the Holy Land

After narrating the eclipse and double-sun portents of Richard I's reign and the famine + pestilence of years 3 and 7:

> Eminent in his Time for their Courage were Robert Earl of Leicester, Hugh Bardolph, and his Brother Henry, William Marshal Earl [of] Chepstow, Gerard de Glanville, **Hugh de Gourney**, William de Borrez, Walcline de Ferrers, Roger [-- and a long list] and William Teutch the King's Standard-Bearer, who all shewed their Valour in the Holy Land.

Annotation: Same content as Holinshed 1577 vol. 4 p. 473. Hanoverian-era repetition of older chronicle material. Footnote-level corroboration for the senior-line crusade tradition; no new fact.

## p. 244 -- Sir Mathew Gourney in the 1381 Portugal expedition under Edmund Earl of Cambridge

In a passage on the truce with Scotland and the Duke of Lancaster's intervention in the Portugal-Castile war:

> The former [Portugal] had sent to [England], [and the king sent] **Edmund Earl of Cambridge**, with [Lord] William [de] Beauchamp and Botreux, and **Sir Marthew Gourney**, with a considerable Force to help him, intending to follow himself with greater Strength as soon as things were put into a settled Posture at home ...

Annotation: Same content as Holinshed 1577 vol. 4 p. 1003, the *Calendar of Patent Rolls Henry IV*, and Pettigrew. The misprint "Marthew" for "Mathew" is preserved verbatim. Hanoverian-era corroboration; no new fact.
```

### 5. Write the Rudder 1779 corpus supplement

New file write: `sources/corpus_supplement/rudder-gloucestershire-1779-gurney-extracts.md`.

```markdown
# Rudder, A New History of Gloucestershire (1779) -- selected Gurney extracts

Source ID: `rudder-gloucestershire-1779`

Source: Samuel Rudder, *A New History of Gloucestershire* (Cirencester: printed by Samuel Rudder, 1779). Internet Archive item `bim_eighteenth-century_a-new-history-of-glouces_rudder-samuel_1779`. Single-folio antiquarian county history; the standard pre-Bigland Gloucestershire compilation. OCR fair to mediocre; long-s normalised; obvious OCR slips silently corrected when they touch a Gurney reading and flagged inline where they materially affect interpretation.

Page numbers below are to the printed pages preserved in the IA derivative; the extracts come from the **Almondsbury parish** entries (Henbury Hundred for Gaunt's Urcot; Langley + Swineshead Hundred for Over; Almondsbury for Redwick). The full Almondsbury parish entry spans roughly pp. 230s through 493 in the printed volume; the Redwick extract is explicitly at p. 493.

---

## Almondsbury, tithing of Over -- Maurice de Gaunt -> Robert de Gourney -> Anselm -> John -> Elizabeth -> John ap Adam -> Berkeley

Rudder treats the descent of Over (in the hundred of Langley and Swineshead, about a mile and a half west from the parish church). After establishing that the manor was not expressly named in Domesday but was probably comprehended in Roger fitz Ralph's holding, Rudder narrates the post-Domesday tenurial chain:

> Maurice de A[wdele?] died seized of Oure 14 H. [III], which afterwards came to **Robert de Gourney, his sister's son**, who died seized of it in the fifty-third year of that reign [53 H. III = 1268-69]. **Anselm de Gourney** held Over 14 E. 1 [1285-86], and **John de Gourney died seized thereof 19 E. 1** [1290-91]. From him it went to **John ap Adam, who had married Elizabeth, the daughter and heir of John de Gourney**. Thomas ap Adam, his son, sold it to Thomas lord Berkeley, and Margaret his wife, 4 E. 3 [1330-31].

The subsequent post-Berkeley descent (Catherine widow of Thomas de Berkeley of Beverstone, then through to Sir William Berkeley attainted of treason 1483, the Brian grant 2 R. 3, etc.) is preserved in the same Rudder Almondsbury entry but is post-Gournay and is not transcribed here.

Annotation: Rudder's "Maurice de A." is most plausibly **Maurice de Gaunt** (Maurice de Gandavo, the famous Bristol-area magnate d. 1230 = 14 H. III). The "sister's son" relationship to Robert de Gourney is consistent with the Pettigrew Somerset-side reconstruction, which has Robert de Gourney emerging as the principal Gournay heir of the senior Somerset-Gloucestershire collateral cluster in the mid-13th c. The Maurice de Gaunt -> Robert de Gourney -> Anselm de Gourney -> John de Gourney -> Elizabeth -> John ap Adam -> Thomas ap Adam -> Berkeley chain is an **independent Gloucestershire-side 1779 witness** to the Somerset-side Pettigrew 1871 reconstruction, with one Gloucestershire-specific dated waypoint (the John de Gourney d. seized 19 Edw. I = 1290-91, applied to the Over manor) that Pettigrew does not give.

---

## Almondsbury, tithing of Gaunt's Urcot -- Gilbert de Gaunt -> Richard de Gourney -> Bilswick / Gaunt's Hospital Bristol

In the same Almondsbury entry, Rudder treats Gaunt's Urcot (in the hundred of Thornbury, near three measured miles east from the parish church):

> This manor anciently belonged to **Gilbert de Gaunt**, whose sister's son and heir, **Richard de Gourney**, founded an hospital in his manor-house called Bilswick, and gave this manor to it; which hospital being dissolved, the manor of Gaunt's Urcot was granted to the city of Bristol, for public uses, 33 H. 8 [1541-42], and the mayor and commonalty of that city are the present lords of this manor.

Rudder then adds:

> The Gaunt's hospital was originally founded for a hundred poor people. It stands within the liberties of the city of Bristol, was refounded in the reign of queen Elizabeth, and now entertains the blue-coat-boys.

Annotation: **Named-actor conflict** worth recording verbatim. Pettigrew 1871 (Somerset side; see `research/places/somerset-gournay-collateral.md`) attributes the Bristol Bilswick / Gaunt's Hospital foundation to **Robert de Gournay II** -- the principal mid-13th-c. senior Gournay heir in the same Somerset cluster -- with the further note that Robert's heart was buried at the Friars Preachers in Bristol and his body in St Mark's Chapel (which became the chapel of Gaunt's Hospital itself). Rudder 1779 gives the founder as **Richard de Gourney**. Both writers are antiquarian compilations; the underlying primary record (the Gaunt's Hospital foundation charter, and the names of "Richard" / "Robert" in surviving Bristol cartulary material) is the only authoritative tie-breaker. The conflict is preserved in `research/places/somerset-gournay-collateral.md`.

---

## Almondsbury, Redwick -- Maurice de Gaunt -> Robert de Gourney -> Anselm -> John -> Elizabeth -> John ap Adam (the Redwick + Northwick fine 25 Edw. I)

At p. 493, Rudder treats the manor of Redwick (along the Severn, about three measured miles from the parish church):

> [Redwick] was a member of the large manor of Westbury, and ... the New Passage over the Severn is in this tithing. **Maurice de Gaunt** died seized of the manor of Redwick, with markets and fairs, 6 H. 3 [1221-22], as did **Robert de Gourney 53 H. 3** [1268-69], whose son Anselm was succeeded by **John de Gourney**, whose daughter, **Elizabeth, was married to John Ap Adam**, (sometimes called John de Badenham), which John and Elizabeth levied a fine of the manors of Redwick and Northwick **25 E. 1** [1296-97].

Annotation: Third Almondsbury-parish manor in the same Gaunt -> Gourney -> Elizabeth -> ap Adam chain, with two further specific waypoints: (a) Maurice de Gaunt died seized of Redwick (with markets and fairs) 6 Henry III = 1221-22 -- earlier than the 14 Henry III death-seized date applied to Over; (b) the John ap Adam / Elizabeth fine of Redwick + Northwick 25 Edw. I = 1296-97 dates the Elizabeth -> John ap Adam transmission for these specific manors. The alternative surname "John de Badenham" applied to John ap Adam by some sources is preserved verbatim from Rudder.

---

## Cross-reference table

| Manor | Tithing / Hundred | Gaunt death-seized | Gournay descent | Final dated Gournay waypoint | Berkeley / ap Adam outcome |
|---|---|---|---|---|---|
| Over | Langley + Swineshead | Maurice de Gaunt d. 14 H. III (1229/30) | Robert de Gourney (sister's son) d. 53 H. III (1268/9); Anselm 14 Edw. I; John d. 19 Edw. I (1290/1) | John d. seized 19 Edw. I | Elizabeth -> John ap Adam -> sale to Thomas lord Berkeley 4 Edw. III (1330/1) |
| Gaunt's Urcot | Thornbury | -- (Gilbert de Gaunt, not Maurice) | "Richard de Gourney" (sister's son and heir of Gilbert de Gaunt) | Foundation of Gaunt's Hospital, Bilswick, Bristol | Hospital granted to city of Bristol 33 H. 8 (1541-42) |
| Redwick | Almondsbury (Westbury sub-member) | Maurice de Gaunt d. 6 H. III (1221/2) | Robert de Gourney d. 53 H. III; Anselm; John | John ap Adam + Elizabeth fine 25 Edw. I (1296/7) | John ap Adam (= John de Badenham) tenure |
```

### 6. Write the Tyrwhitt 1798 corpus supplement (full Leland epitaph + Chaucer context)

New file write: `sources/corpus_supplement/tyrwhitt-canterbury-tales-1798-v2-matheu-gourney-epitaph.md`.

```markdown
# Tyrwhitt ed., Canterbury Tales of Chaucer, vol. ii Notes (1798) -- Sir Matheu de Gourney Leland epitaph

Source ID: `tyrwhitt-canterbury-tales-1798-v2`

Source: Thomas Tyrwhitt, ed., *The Canterbury Tales of Chaucer*, vol. ii (London, 1798). Internet Archive item `bim_eighteenth-century_the-canterbury-tales-of-_chaucer-geoffrey_1798_2`. The Notes volume of the standard late-18th-c. critical edition. The relevant material is in the note to General Prologue v. 43 (the Knight) at p. 392, drawing on John Leland's *Itinerary* (vol. iii p. xi) for the verbatim French epitaph of Sir Matheu de Gourney.

## The verbatim Leland epitaph at p. 392

Tyrwhitt prints the epitaph in his note to the Knight:

> Icy gist le noble et vaillant Chivaler Matheu de Gourney &c. -- qui en sa vie fu a la bajaille de Benamaryn, et ala apres a la siege d'Algezire sur les Sarazines et aussi a les batailles de L'Escluse, de Crefcy, de Deyngeneffe, de Peyteres, de Nazare, d'Ozrey et a plusours autres batailles et affeges en les quex il gaigna noblement graunt los et honour --, He died in 1406, at the age of 96.

Translation and identifications:

- **Icy gist le noble et vaillant Chivaler Matheu de Gourney** -- "Here lies the noble and valiant Knight Matthew de Gournay" -- the standard medieval-French monumental opening.
- **bataille de Benamaryn** -- the campaign against the Marinids in North Africa, c. 1340 (the *Banu Marin*); the Castile-Marinid war that culminated in the Battle of Rio Salado 30 October 1340. Matthew presumably served with the Castilian or Anglo-Castilian force.
- **siege d'Algezire** -- the siege of Algeciras 1342-44, undertaken by Alfonso XI of Castile after Rio Salado. English and other crusading knights, including Henry of Grosmont (Earl of Derby, later Duke of Lancaster), participated.
- **L'Escluse** -- the Battle of Sluys, 24 June 1340. The English naval victory in the Zwin estuary.
- **Crefcy** -- the Battle of Crecy, 26 August 1346.
- **Deyngeneffe** -- the Battle of Winchelsea (or Espagnols-sur-Mer / "Les Espagnols-sur-Mer"), 29 August 1350 -- the English naval action against the Castilian fleet (Tyrwhitt's "Deyngenesse" appears to be a Leland-side garbled reading; later editors emend variously).
- **Peyteres** -- the Battle of Poitiers, 19 September 1356.
- **Nazare** -- the Battle of Najera, 3 April 1367 -- the English-Black-Prince victory over Henry of Trastamara on behalf of Pedro the Cruel of Castile.
- **Ozrey** -- the Battle of Auray, 29 September 1364 -- the engagement that ended the Breton War of Succession in favor of John IV de Montfort.
- **et a plusours autres batailles et affeges** -- "and at several other battles and sieges"; the open-ended closing acknowledges that the eight named campaigns are an exemplary subset, not an exhaustive list.

## Tyrwhitt's Chaucer-context observation at p. 392

Tyrwhitt continues immediately after the epitaph:

> [Sir Matheu de Gourney] died in 1406, at the age of 96. Why Chaucer should have chosen to bring his Knight from Alexandria and Lettowe rather than from Cresfsy and Poitiers, is a problem difficult to resolve, except by supposing that the slightest services against Infidels were in those days more honourable than the most splendid victories over Christians.

Annotation: Tyrwhitt's framing is significant for the project's Sir Matthew biography: it confirms (i) that by 1798 Sir Matthew was already a culturally-canonical figure of the Hundred-Years-War English military elite -- a near-contemporary of Chaucer whose real campaigns could plausibly have been the model for the fictional Knight's; and (ii) that Tyrwhitt himself draws directly on Leland's *Itinerary* (vol. iii p. xi) for the epitaph text rather than on any intermediate 17th-c. compilation, putting his transcription one step closer to the Stoke-sub-Hamdon monument than Pettigrew's 1871 paraphrase.

The death year **1406** and the age **96** are both Tyrwhitt-preserved Leland-derived. These match the 26 September 1406 death date from Pettigrew (via Leland) and the *Calendar of Fine Rolls* Henry IV terminus ante quem of 5 November 1406 already in `research/places/somerset-gournay-collateral.md`. The age 96 implies a birth year of c. 1310 -- consistent with the Sir Matthew = fourth son of the regicide Sir Thomas de Gourney already in `research/places/somerset-gournay-collateral.md`.
```

### 7. Write the five new validation files

New file write: `sources/validations/holinshed-chronicles-1577.md`.

```markdown
# Validation -- Holinshed, Chronicles (1577), laste volume

Source ID: `holinshed-chronicles-1577`

## Examined

Oxford Holinshed Project keyed 1577 transcription (full vol. 2), cross-checked against the Internet Archive copy `bim_early-english-books-1475-1640_the-laste-volume-of-the-_holinshed-raphael_1577`. The IA scan's OCR is unreliable (Tesseract on Fraktur/blackletter); the Oxford keyed text is the working searchable layer.

Variant cluster screened: Gurney / Gurneie / Gurnie / Gurny / Gurnay / Gurnai / Gurnaye / Gourney / Gourneie / Gournei / Gourny / Gournee / Gournay / Gournai / Gournaye / Gorney / Gornay / Gorneay / Gorny; fragment searches `Gurn`, `Gour`, `Gorn`, `Gur`, `Gor`; person-name pairings `Hue`, `Hugh`, `Hugo`, `Thomas`, `Mathew`, `Matthew`, `Matheu`, `Sir`, `de`, `Erle`, `Earl`. The unusual alias `Geneuay` attached to `Hue de Gourney` was also screened independently.

Variants actually found in this 1577 target: `Gourney`, `Gournay`, `Gurnay`, `Gurney`, `Gorney`, plus `Geneuay` as the Conquest-list alias. `Gurry` and `Gurley` appear nearby in the Battle Abbey Roll listing but are not treated as Gurney variants without corroboration.

14 Gurney-variant loci identified across vol. 4, transcribed verbatim in `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md`.

## Caveats

The IA copy is vol. 2 only; lacks L3 of the index; pages torn and tightly bound with some loss of text. The Oxford Holinshed Project transcription remains the more authoritative searchable text. The 1587 second-edition Holinshed (not pulled in this round) often has cleaner or expanded wording for the same passages and is the standard scholarly reference; future work may benefit from cross-checking each 1577 hit against the 1587 reading.

## Findings landed

- Senior-line + senior-collateral: G34 Hugh II companion (Geneuay alias note); `research/topics/senior-gournay-baron-line-collateral.md` (Hugh's "Fert" castle 1150s; Hugh Gourney's lands as Leicester captivity site; Mountfort defection 1204).
- Somerset / Hundred-Years-War: `research/places/somerset-gournay-collateral.md` (Sir Mathew procedural-legal role).
- Verbatim extract: `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md`.
- Operational record: `sources/intake/done/v73-1577-1798-printed-witnesses-gourney-references.patchset.md` (after Phase 2).
- Prep-notes working file: `sources/intake/done/holinshed_1577_gurney_variant_research_notes.md` (after Phase 2).
```

New file write: `sources/validations/daniel-history-england-1613-pt1.md`.

```markdown
# Validation -- Daniel, First Part of the Historie of England (1613)

Source ID: `daniel-history-england-1613-pt1`

## Examined

Internet Archive item `bim_early-english-books-1475-1640_the-first-part-of-the-hi_daniel-samuel_1613`. Targeted search for `gourney` and Gourney/Gurney/Gornay variants returned the p. ~142 passage on the Conqueror's "especial actors" who died before him; no other Gurney-variant hits found in this volume.

## Findings landed

- G34 Hugh II companion section 6 (one more printed witness to the "old Hugh died before the Conqueror" Norman tradition).
- Verbatim extract: `sources/corpus_supplement/daniel-history-england-1613-pt1-gurney-extract.md`.
- Operational record: `sources/intake/done/v73-1577-1798-printed-witnesses-gourney-references.patchset.md` (after Phase 2).
```

New file write: `sources/validations/complete-history-england-1706-v1.md`.

```markdown
# Validation -- A Complete History of England, vol. 1 (1706)

Source ID: `complete-history-england-1706-v1`

## Examined

Internet Archive item `bim_eighteenth-century_a-complete-history-of-en_1706_1`. Targeted search for `gourney` returned two hits: p. 158 (Hugh de Gourney in the Richard I Holy Land list) and p. 244 (Sir Mathew Gourney in the 1381 Portugal expedition). Both repeat content already on the project record via Holinshed 1577 / Pettigrew / *Calendar of Patent Rolls Henry IV*. No further Gurney content found in this volume.

## Caveats

Hanoverian-era compilation; authorship of the early-medieval chapters unattributed in the volume. Useful only as a corroborating-citation source, not as a primary or first-tier secondary witness.

## Findings landed

- Footnote-level corroboration in `research/topics/senior-gournay-baron-line-collateral.md` (Hugh in Richard I Holy Land list) and `research/places/somerset-gournay-collateral.md` (Sir Mathew Portugal expedition).
- Verbatim extracts: `sources/corpus_supplement/complete-history-england-1706-v1-gurney-extracts.md`.
- Operational record: `sources/intake/done/v73-1577-1798-printed-witnesses-gourney-references.patchset.md` (after Phase 2).
```

New file write: `sources/validations/rudder-gloucestershire-1779.md`.

```markdown
# Validation -- Rudder, A New History of Gloucestershire (1779)

Source ID: `rudder-gloucestershire-1779`

## Examined

Internet Archive item `bim_eighteenth-century_a-new-history-of-glouces_rudder-samuel_1779`. The Almondsbury parish entries (Henbury Hundred for Gaunt's Urcot; Langley + Swineshead for Over; Almondsbury proper for Redwick) supplied the substantively new material. Page anchors: Over and Gaunt's Urcot in the Almondsbury entry's manor-section pages; Redwick at p. 493. Other Gloucestershire parishes were not separately swept for Gurney variants in this round; future passes may benefit from a full-volume sweep.

## Caveats

Pre-Bigland antiquarian county history; single-folio volume. Strong primary-record citations within parish entries (Domesday paraphrases, Inquisitions Post Mortem references, Close Roll / Patent Roll references) but no primary-record reproductions; treat as derivative.

The named-actor conflict with Pettigrew 1871 over the Bristol Bilswick / Gaunt's Hospital founder (Rudder "Richard de Gourney" vs. Pettigrew "Robert de Gournay II") is preserved in `research/places/somerset-gournay-collateral.md` pending primary-record check.

## Findings landed

- `research/places/somerset-gournay-collateral.md` (Gloucestershire-side Almondsbury parish descent of Over, Redwick, Northwick; Gaunt's Urcot / Bilswick / Gaunt's Hospital with named-actor conflict).
- Verbatim extracts: `sources/corpus_supplement/rudder-gloucestershire-1779-gurney-extracts.md`.
- Operational record: `sources/intake/done/v73-1577-1798-printed-witnesses-gourney-references.patchset.md` (after Phase 2).
```

New file write: `sources/validations/tyrwhitt-canterbury-tales-1798-v2.md`.

```markdown
# Validation -- Tyrwhitt ed., Canterbury Tales of Chaucer, vol. ii Notes (1798)

Source ID: `tyrwhitt-canterbury-tales-1798-v2`

## Examined

Internet Archive item `bim_eighteenth-century_the-canterbury-tales-of-_chaucer-geoffrey_1798_2`. The note to General Prologue v. 43 (the Knight) at p. 392 reproduces the full French Leland epitaph for Sir Matheu de Gourney. No other Gurney material identified in this volume; Tyrwhitt's other notes touch on contemporary 14th-c. military figures but not on Gurney specifically.

## Caveats

Tyrwhitt's transcription is at one remove from Leland's *Itinerary* (vol. iii p. xi); the actual Stoke-sub-Hamdon monument was no longer accessible in 1798 except via Leland's transcription. Several place-name forms in the epitaph (Deyngenesse, Ozrey) are Leland-side renderings of medieval-French versions of place-names that later scholars have variously emended.

## Findings landed

- `research/places/somerset-gournay-collateral.md` Sir Matthew section (verbatim French epitaph at length; close-to-Leland 18th-c. literary-critical witness).
- Verbatim extract: `sources/corpus_supplement/tyrwhitt-canterbury-tales-1798-v2-matheu-gourney-epitaph.md`.
- Operational record: `sources/intake/done/v73-1577-1798-printed-witnesses-gourney-references.patchset.md` (after Phase 2).
```

### 8. Senior-collateral topic file -- Holinshed 1577 + Complete History 1706 additions

File: `research/topics/senior-gournay-baron-line-collateral.md`.

Anchor on the stable inner-block boundary between the `## *Chevaliers aux armes noires*` paragraph and the `## Why this stays a topic, not a fact sheet` section. This anchor is independent of v72's Armstrong-1781 append (which v72 plans to make at the very end of the file, after `[^dcclii-sigy]`) and is stable in both v72-applied and not-yet-applied states.

```str_replace
old_string: Decorde preserves the regional epithet for the senior barons: *Chevaliers aux armes noires*, "knights of the black arms," from their sable (black) coat of arms. The epithet had passed into local memory by the nineteenth century and the post-1202 silver-knight overlay was understood as the heraldic mark of Capetian conquest. The black-arms tradition aligns with the earlier Eudes / Rollo black-shield foundation motif preserved in the seat file.[^decorde-armes-noires-topic]

## Why this stays a topic, not a fact sheet
new_string: Decorde preserves the regional epithet for the senior barons: *Chevaliers aux armes noires*, "knights of the black arms," from their sable (black) coat of arms. The epithet had passed into local memory by the nineteenth century and the post-1202 silver-knight overlay was understood as the heraldic mark of Capetian conquest. The black-arms tradition aligns with the earlier Eudes / Rollo black-shield foundation motif preserved in the seat file.[^decorde-armes-noires-topic]

## Holinshed 1577 -- mid-12th-c. La Ferte loss; Richard-I-era territorial markers; King-John-era Mountfort defection

Raphael Holinshed's *laste volume of the Chronicles* (London, 1577), vol. 2 supplies three senior-line attestations across vol. 4 (the running division by reign).

**Hugh de Gourney's castle "Fert" burned by Duke Henry of Normandy, mid-1150s (vol. 4 p. 364).** After Henry, Duke of Normandy, married Eleanor of Aquitaine, the French king made war on him; Henry retaliated by burning several castles, including one belonging to Hugh de Gourney named *Fert*: "Duke Henry entred into the territories of King Stephan, and brent certeine Castels that belonged to the sayde King, and also a Castell that belonged to Hugh de Gourney called Fert, but the French king tooke Vernon ..." The "Fert" reading most plausibly points to **La Ferte-en-Bray** (already a documented senior-collateral seat -- see `research/places/la-ferte-en-bray.md`). The Hugh in question is most parsimoniously **Hugh IV** (the post-Hugh-III senior baron, the Bec-educated figure already covered above in the Anderson Vol. II material).[^v73-holinshed-fert]

**Hugh Gourney's lands as captivity site for Robert Earl of Leicester, Richard I era (vol. 4 p. 473).** "In the same season Robert Erle of Leicester, with a small companye of Souldiers, came unto the Castel of Passey, which Castel hee wanne ... and as he adventured himselfe somewhat unaduysedly in the landes of Hugh Gourney, he was taken prisoner ..." A late-12th-c. territorial-marker attestation: Hugh IV's Norman lands were a recognised zone of contested military movement during Richard I's conflict with Philip Augustus.[^v73-holinshed-leicester-captivity]

**Hugh de Gourney's defection from King John -- the Mountfort delivery, 1203/4 (vol. 4 p. 557).** Holinshed credits Hugh with a stout month-long defence of Chateau Gaillard against the French king ("by the high valiancie of Hugh de Gourney the Captayne there, the French men were manfully beaten backe, and kept out for a month and more"), then says: "Hugh de Gourney revolteth from king John. And in the ende the sayde Hugh Gourney reuolted from his obedience, delivering also the **Castell of Mountforte** unto the Frenche King ..." This is **Hugh V** (forfeited 1205, d. 1214). The Chateau Gaillard defence and the eventual fall are already on the project's senior-line record (Farrer; Anderson Vol. II Book VII); the Mountfort delivery as a specific defection-act of Hugh V is new operational detail.[^v73-holinshed-mountfort]

Holinshed also gives a Hugh-de-Gourney attestation in the Richard I Holy Land valorous-men list at vol. 4 p. 473; the same content is repeated at vol. 1 p. 158 of the anonymous *Complete History of England* (London, 1706), which adds nothing new but supplies a Hanoverian-era corroborating-citation source.[^v73-complete-history-1706-crusade]

[^v73-holinshed-fert]: Raphael Holinshed, *The laste volume of the Chronicles of England, Scotlande, and Irelande, with their descriptions*, vol. 2 (London, 1577), vol. 4 p. 364. Verbatim extract in `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md`. Source ID: `holinshed-chronicles-1577`.

[^v73-holinshed-leicester-captivity]: Holinshed, *Chronicles* (1577), vol. 4 p. 473. Source ID: `holinshed-chronicles-1577`.

[^v73-holinshed-mountfort]: Holinshed, *Chronicles* (1577), vol. 4 p. 557. Source ID: `holinshed-chronicles-1577`.

[^v73-complete-history-1706-crusade]: *A Complete History of England, with the Lives of all the Kings and Queens thereof*, vol. 1 (London, 1706), p. 158. Hanoverian-era compilation; authorship of the early-medieval chapters unattributed. Source ID: `complete-history-england-1706-v1`.

## Why this stays a topic, not a fact sheet
```

### 9. Somerset / Gloucestershire collateral place file -- Tyrwhitt 1798 + Holinshed 1577 + Rudder 1779 + Complete History 1706 additions

File: `research/places/somerset-gournay-collateral.md`.

#### 9a. Tyrwhitt 1798 -- verbatim Leland epitaph for Sir Matheu de Gourney d. 1406 age 96

Anchor on the existing Sir Matthew section's end (after the CFR Henry IV terminus-ante-quem footnote `[^cfr-1406-matthew-gournay-dead-by]`).

```str_replace
old_string: [^cfr-1406-matthew-gournay-dead-by]: *Calendar of the Fine Rolls Preserved in the Public Record Office, Henry IV, A.D. 1405-1413*, vol. 13 (London: HMSO, 1934), p. 78, recording that Sir Matthew de Gournay had died by 5 November 1406. Source ID: `cfr-henry-iv-1405-13`.

## Crosslinks
new_string: [^cfr-1406-matthew-gournay-dead-by]: *Calendar of the Fine Rolls Preserved in the Public Record Office, Henry IV, A.D. 1405-1413*, vol. 13 (London: HMSO, 1934), p. 78, recording that Sir Matthew de Gournay had died by 5 November 1406. Source ID: `cfr-henry-iv-1405-13`.

### Tyrwhitt 1798 -- the verbatim Leland epitaph at Stoke-sub-Hamdon

Tyrwhitt's notes to Chaucer's *Canterbury Tales* (London, 1798), vol. ii p. 392, in the note to *General Prologue* v. 43 (the Knight), prints the full French Leland-derived epitaph from the Stoke-sub-Hamdon monument:

> Icy gist le noble et vaillant Chivaler Matheu de Gourney &c. -- qui en sa vie fu a la bajaille de Benamaryn, et ala apres a la siege d'Algezire sur les Sarazines et aussi a les batailles de L'Escluse, de Crefcy, de Deyngeneffe, de Peyteres, de Nazare, d'Ozrey et a plusours autres batailles et affeges en les quex il gaigna noblement graunt los et honour --, He died in 1406, at the age of 96.

The eight named campaigns map to: **Benamaryn** = Marinid war c. 1340 (Castile-Marinid Battle of Rio Salado 30 Oct 1340); **siege d'Algezire** = siege of Algeciras 1342-44 under Alfonso XI of Castile; **L'Escluse** = Sluys 24 June 1340; **Crefcy** = Crecy 26 August 1346; **Deyngeneffe** = Winchelsea / Espagnols-sur-Mer 29 August 1350 (Leland-side garbled form); **Peyteres** = Poitiers 19 September 1356; **Nazare** = Najera 3 April 1367; **Ozrey** = Auray 29 September 1364. The closing "et a plusours autres batailles et affeges" acknowledges the eight named campaigns as an exemplary subset, not exhaustive.

Tyrwhitt frames Sir Matthew as a near-contemporary of Chaucer's fictional Knight ("died in 1406, at the age of 96 ... Why Chaucer should have chosen to bring his Knight from Alexandria and Lettowe rather than from Cresfsy and Poitiers, is a problem difficult to resolve"). The age 96 implies a birth year of c. 1310 -- consistent with the project's identification of Sir Matthew as the fourth son of the regicide Sir Thomas de Gourney. Tyrwhitt's text is at one remove from Leland's *Itinerary* (vol. iii p. xi), one step closer than Pettigrew's 1871 paraphrase.[^v73-tyrwhitt-matheu-epitaph]

### Holinshed 1577 -- Sir Mathew Gourney in a procedural / legal role under the king

Holinshed (vol. 4 p. 1118) records Sir Mathew Gourney delivering a procedural ruling against the Earl of Salisbury in a Salisbury-vs-Morley protestation dispute: Salisbury cannot retroactively add a protestation that was not in his first answer.

> Sir Mathew Gourney sitting under the king, said to the Erle of Salisbury, that sith hee had made no such protestation in his first answer ... he was now past the aduantage thereof ...

A new later-career office attestation for Sir Matthew beyond the existing Pettigrew + CPR Henry IV military / commission-of-the-peace material. Suggests Sir Matthew held standing or judicial authority in a high-level proceeding -- consistent with the standing-counsel pattern of his post-1399 Henry IV commissions for Somerset already documented above.[^v73-holinshed-sir-matheu-procedural]

### Holinshed 1577 and Complete History 1706 -- corroborations of already-known Sir Matthew campaign records

Holinshed independently attests Sir Mathew at Auray (vol. 4 p. 884, in the second division under Clisson and Daubreticourt) and on the 1381 Portugal expedition under Edmund Earl of Cambridge (vol. 4 p. 1003, "with fiue hundred armed men, and fiue hundred Archers, to aide the king of Portugall against the king of Castile").[^v73-holinshed-sir-matheu-auray-portugal] The anonymous *Complete History of England* (London, 1706), vol. 1 p. 244, repeats the same Portugal-expedition content (with the spelling "Marthew" for Mathew); pure Hanoverian-era corroboration, no new fact.[^v73-complete-history-1706-portugal]

[^v73-tyrwhitt-matheu-epitaph]: Thomas Tyrwhitt, ed., *The Canterbury Tales of Chaucer*, vol. ii (London, 1798), note to General Prologue v. 43 at p. 392, drawing on John Leland's *Itinerary*, vol. iii p. xi. Verbatim transcription and gloss at `sources/corpus_supplement/tyrwhitt-canterbury-tales-1798-v2-matheu-gourney-epitaph.md`. Source ID: `tyrwhitt-canterbury-tales-1798-v2`.

[^v73-holinshed-sir-matheu-procedural]: Raphael Holinshed, *Chronicles* (1577), vol. 4 p. 1118. Verbatim extract in `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md`. Source ID: `holinshed-chronicles-1577`.

[^v73-holinshed-sir-matheu-auray-portugal]: Holinshed, *Chronicles* (1577), vol. 4 pp. 884 (Auray) and 1003 (Portugal). Source ID: `holinshed-chronicles-1577`.

[^v73-complete-history-1706-portugal]: *A Complete History of England*, vol. 1 (London, 1706), p. 244. Source ID: `complete-history-england-1706-v1`.

## Crosslinks
```

#### 9b. Rudder 1779 -- Almondsbury (Gloucestershire) descent of Over, Redwick/Northwick, Gaunt's Urcot/Bilswick

Anchor at the end of the file (after the existing `[^pettigrew-somerset-place]` footnote which is the last item per the file as read).

```str_replace
old_string: [^pettigrew-somerset-place]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 210-216, [Google Books](https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ). Source ID: `pettigrew-collectanea-house-gournay-1871`.
new_string: [^pettigrew-somerset-place]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 210-216, [Google Books](https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ). Source ID: `pettigrew-collectanea-house-gournay-1871`.

## Rudder 1779 -- Gloucestershire-side descent of Almondsbury parish manors (Over, Redwick, Gaunt's Urcot)

Samuel Rudder's *A New History of Gloucestershire* (Cirencester, 1779) supplies a Gloucestershire-side independent witness to the Maurice-de-Gaunt -> Robert/Anselm/John de Gourney -> Elizabeth -> John ap Adam descent already documented from the Somerset side by Pettigrew 1871. The relevant material lies in the Almondsbury parish entry; the verbatim extracts and a cross-reference table are preserved at `sources/corpus_supplement/rudder-gloucestershire-1779-gurney-extracts.md`.

**Over (Almondsbury, Langley + Swineshead Hundred).** Rudder gives the post-Domesday descent of Over: "Maurice de A[wdele / Gaunt] died seized of Oure 14 H. [III] [1229/30], which afterwards came to Robert de Gourney, his sister's son, who died seized of it in the fifty-third year of that reign [53 H. III = 1268/9]. Anselm de Gourney held Over 14 E. 1 [1285/6], and John de Gourney died seized thereof 19 E. 1 [1290/1]. From him it went to John ap Adam, who had married Elizabeth, the daughter and heir of John de Gourney. Thomas ap Adam, his son, sold it to Thomas lord Berkeley, and Margaret his wife, 4 E. 3 [1330/1]." The John-de-Gourney d. seized 19 Edw. I = 1290/1 dating, applied specifically to Over, is **new** -- Pettigrew does not give this Gloucestershire-side waypoint.[^v73-rudder-over]

**Redwick (Almondsbury proper, p. 493).** Rudder gives the descent of Redwick, a sub-member of the great Westbury manor: "Maurice de Gaunt died seized of the manor of Redwick, with markets and fairs, 6 H. 3 [1221/2], as did Robert de Gourney 53 H. 3 [1268/9], whose son Anselm was succeeded by John de Gourney, whose daughter, Elizabeth, was married to John Ap Adam, (sometimes called John de Badenham), which John and Elizabeth levied a fine of the manors of Redwick and Northwick 25 E. 1 [1296/7]." The Maurice de Gaunt d. seized of Redwick 6 H. III (1221/2) is earlier than the 14 H. III date applied to Over; the John ap Adam / Elizabeth fine of Redwick + Northwick 25 Edw. I (1296/7) dates the Elizabeth -> John ap Adam transmission for these specific manors. The alternative surname "John de Badenham" for John ap Adam is preserved verbatim from Rudder.[^v73-rudder-redwick]

**Gaunt's Urcot (Almondsbury, Thornbury Hundred) and the Bristol Bilswick / Gaunt's Hospital foundation -- a named-actor conflict with Pettigrew.** Rudder says: "This manor anciently belonged to Gilbert de Gaunt, whose sister's son and heir, **Richard de Gourney**, founded an hospital in his manor-house called Bilswick, and gave this manor to it; which hospital being dissolved, the manor of Gaunt's Urcot was granted to the city of Bristol, for public uses, 33 H. 8 [1541/2], and the mayor and commonalty of that city are the present lords of this manor. The Gaunt's hospital was originally founded for a hundred poor people. It stands within the liberties of the city of Bristol, was refounded in the reign of queen Elizabeth, and now entertains the blue-coat-boys."

Pettigrew 1871 (the existing Somerset-side narrative captured at the top of this file) attributes the foundation of the same Bristol Bilswick hospital -- known as Gaunt's Hospital, later St Mark's, later the Bristol Bluecoat school -- to **Robert de Gournay II**, with the further note that Robert's heart was buried at the Friars Preachers in Bristol and his body in St Mark's Chapel itself. Rudder 1779 gives the founder as Richard de Gourney; the founder-name conflict is **preserved as a documented antiquarian disagreement** pending primary-record check. Both writers are 18th- and 19th-c. compilations; the underlying primary record (the Gaunt's Hospital foundation charter, and the names "Richard" / "Robert" in surviving Bristol cartulary material) is the only authoritative tie-breaker. Plausible reconciliations include (a) Rudder confused Richard with Robert, the more famous mid-13th-c. principal Gournay heir; (b) Pettigrew telescoped Robert and an earlier or younger Richard; (c) two distinct foundation acts (an original Richard-de-Gournay foundation later refounded or substantially endowed by Robert II) collapsed in both compilations. **Availability tag: Available online -- archive.org for both Rudder and Pettigrew; the Gaunt's Hospital foundation charter survives in the Berkeley / Bristol cartulary material and would resolve the conflict.**[^v73-rudder-gaunts-urcot]

These three Almondsbury extracts together constitute an **independent Gloucestershire-side 1779 witness** to Pettigrew's Somerset-side senior-collateral reconstruction, adding two specific Gloucestershire dated waypoints (John de Gourney d. 19 Edw. I; John ap Adam + Elizabeth fine of Redwick + Northwick 25 Edw. I) and one named-actor conflict (Bristol Gaunt's Hospital founder).

[^v73-rudder-over]: Samuel Rudder, *A New History of Gloucestershire* (Cirencester, 1779), Almondsbury parish entry, tithing of Over (Langley + Swineshead Hundred). Internet Archive item `bim_eighteenth-century_a-new-history-of-glouces_rudder-samuel_1779`. Verbatim extract in `sources/corpus_supplement/rudder-gloucestershire-1779-gurney-extracts.md`. Source ID: `rudder-gloucestershire-1779`.

[^v73-rudder-redwick]: Rudder, *Gloucestershire* (1779), Almondsbury parish entry, Redwick section, p. 493. Source ID: `rudder-gloucestershire-1779`.

[^v73-rudder-gaunts-urcot]: Rudder, *Gloucestershire* (1779), Almondsbury parish entry, Gaunt's Urcot section (Thornbury Hundred). Compare T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London, 1871), pp. 210-216, which gives the same Bilswick / Gaunt's Hospital foundation under Robert de Gournay II rather than Richard de Gourney. Source IDs: `rudder-gloucestershire-1779`, `pettigrew-collectanea-house-gournay-1871`.
```

### 10. G34 Hugh II research companion -- Holinshed "Geneuay" alias note + Daniel 1613 witness for section 6

File: `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`.

#### 10a. Holinshed "Geneuay" alias note

The companion's section 11 (Sources consulted table) is the natural footer; add a brief variant-spellings paragraph immediately before it. Anchor on the existing section 10 closing and the "11. Sources consulted" header.

```str_replace
old_string: 7. **The Eulde / Hugues name equivalence**: Potin's two-version juxtaposition (Dumoulin "Hugues" vs. *Histoire et Chronique* "Eulde") is direct textual evidence for Hannay's observation. Carries forward to G36/G37 where the same equivalence is the basis for the FS-tree's "Eudes ou Hugues" PID conflation.

---

## 11. Sources consulted
new_string: 7. **The Eulde / Hugues name equivalence**: Potin's two-version juxtaposition (Dumoulin "Hugues" vs. *Histoire et Chronique* "Eulde") is direct textual evidence for Hannay's observation. Carries forward to G36/G37 where the same equivalence is the basis for the FS-tree's "Eudes ou Hugues" PID conflation.

8. **Holinshed 1577 -- the "Geneuay" alias attached to Hue de Gourney in the Conquest-list (vol. 4 p. 291)**. Raphael Holinshed prints "Hue de Gourney, alias Geneuay" within his Conquest-actor catalogue and, separately, "Hue erle of Gournay" -- the only Earl form recorded. The alias `Geneuay` is otherwise unattested in the project's name-variant catalogue and is most plausibly an Elizabethan-era OCR/typographic corruption of an underlying source name. Captured as a documented variant in `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md` but not promoted to a working alias.[^v73-holinshed-geneuay]

[^v73-holinshed-geneuay]: Raphael Holinshed, *The laste volume of the Chronicles of England, Scotlande, and Irelande, with their descriptions*, vol. 2 (London, 1577), vol. 4 p. 291. Source ID: `holinshed-chronicles-1577`.

---

## 11. Sources consulted
```

#### 10b. Daniel 1613 witness for section 6 (Cardiff tradition)

Anchor at the end of section 6.7 (the Powell 1584 Welsh-chronicle subsection) before the existing `[^powell-1584-welsh-1094]` footnote.

```str_replace
old_string: [^powell-1584-welsh-1094]: David Powell, *The Historie of Cambria, now called Wales: a part of the most famous Yland of Brytaine* (London: Rafe Newberie and Henrie Denham, 1584), continuing the unfinished English translation by Humphrey Llwyd of medieval Welsh chronicle material (principally *Brut y Tywysogion*). The passage is quoted in full at <https://patp.us/reading/companions-of-the-conqueror/hugh-de-gournay>. The Powell first edition is at Early English Books Online (STC 2nd ed. 20089) and at the British Library (shelfmark G.6056); the standard modern edition is the 1811 Wynne re-edition. Source ID: `powell-historie-cambria-1584`.
new_string: [^powell-1584-welsh-1094]: David Powell, *The Historie of Cambria, now called Wales: a part of the most famous Yland of Brytaine* (London: Rafe Newberie and Henrie Denham, 1584), continuing the unfinished English translation by Humphrey Llwyd of medieval Welsh chronicle material (principally *Brut y Tywysogion*). The passage is quoted in full at <https://patp.us/reading/companions-of-the-conqueror/hugh-de-gournay>. The Powell first edition is at Early English Books Online (STC 2nd ed. 20089) and at the British Library (shelfmark G.6056); the standard modern edition is the 1811 Wynne re-edition. Source ID: `powell-historie-cambria-1584`.

### 6.8 Daniel 1613 -- Hugh de Gourney in the Conqueror's "especial actors" died-before-him list

Samuel Daniel's *The First Part of the Historie of England* (London, 1613) at p. ~142 supplies a sixth named-source witness to the same Norman tradition. Daniel groups Hugh de Gourney with Beaumont, Harcourt, Vicount Neele, Hugh de Mortimer, and the Comte de Vennes as the "especial actors in [the Conquest]" who died "before" the Conqueror (d. 1087):

> And this was in the fate of the Conquerour, to see most of all these men who had bene the especial actors in [the Conquest] ... extinct before him: As Beaumont, Harcourte, **Hugh de Gourney**, Vicount Neele, Hugh de Mortimer, Conte de Vennes, &c. And now [he] disposing [of his affairs] ended it [his life] in the 74. yeere of his age, and the 21. of his raigne.

The Daniel list overlaps strongly with the French / Norman / Welsh tradition cluster already captured above: Neele le Vicomte, Harcourt, and the Comte de Vennes all reappear from the *Histoire et Chronique de Normandie* (Rouen 1610) and Powell 1584 readings, and Beaumont and Hugh de Mortimer are the standard Conquest-generation collaterals.[^v73-daniel-1613-conqueror-actors]

[^v73-daniel-1613-conqueror-actors]: Samuel Daniel, *The First Part of the Historie of England* (London: Nicholas Okes, 1613), p. ~142. Verbatim extract in `sources/corpus_supplement/daniel-history-england-1613-pt1-gurney-extract.md`. Source ID: `daniel-history-england-1613-pt1`.
```

### 11. Intake-stub housekeeping

Remove any stale stub files and create `stub-v74.md`. Idempotent for the cases where v72 has or has not already run.

```bash
# Idempotent stale-stub removal
rm -f sources/intake/processed/stub-v67.md
rm -f sources/intake/processed/stub-v70.md
rm -f sources/intake/processed/stub-v71.md
rm -f sources/intake/processed/stub-v72.md
rm -f sources/intake/processed/stub-v73.md

# Create the post-v73 stub
cat > sources/intake/processed/stub-v74.md <<'EOF'
Next patchset stub.

Rename this file to `v74-topic.patchset.md` when creating the next patchset, then immediately create `stub-v75.md`.
EOF
```

### 12. Move the Holinshed prep-notes working file to `done/`

The prep-notes file is the working transcription layer behind the `holinshed-chronicles-1577` source ID. Move alongside this patchset in Phase 2.

```bash
mv sources/intake/processed/holinshed_1577_gurney_variant_research_notes.md \
   sources/intake/done/holinshed_1577_gurney_variant_research_notes.md
```

## Validation checklist

- [ ] `data/sources.json` -- six new entries added (`holinshed-chronicles-1577`, `daniel-history-england-1613-pt1`, `complete-history-england-1706-v1`, `rudder-gloucestershire-1779`, `tyrwhitt-canterbury-tales-1798-v2`).
- [ ] `sources/corpus_supplement/holinshed-1577-selected-gurney-references.md` -- new file with 14-locus verbatim extracts.
- [ ] `sources/corpus_supplement/daniel-history-england-1613-pt1-gurney-extract.md` -- new file.
- [ ] `sources/corpus_supplement/complete-history-england-1706-v1-gurney-extracts.md` -- new file.
- [ ] `sources/corpus_supplement/rudder-gloucestershire-1779-gurney-extracts.md` -- new file with three Almondsbury extracts + cross-reference table.
- [ ] `sources/corpus_supplement/tyrwhitt-canterbury-tales-1798-v2-matheu-gourney-epitaph.md` -- new file with verbatim French epitaph + gloss.
- [ ] `sources/validations/holinshed-chronicles-1577.md` -- new validation worksheet.
- [ ] `sources/validations/daniel-history-england-1613-pt1.md` -- new validation worksheet.
- [ ] `sources/validations/complete-history-england-1706-v1.md` -- new validation worksheet.
- [ ] `sources/validations/rudder-gloucestershire-1779.md` -- new validation worksheet.
- [ ] `sources/validations/tyrwhitt-canterbury-tales-1798-v2.md` -- new validation worksheet.
- [ ] `research/topics/senior-gournay-baron-line-collateral.md` -- gains Holinshed 1577 section (Fert castle, Leicester captivity, Mountfort defection) + Complete History 1706 corroborating footnote.
- [ ] `research/places/somerset-gournay-collateral.md` -- gains Tyrwhitt 1798 verbatim epitaph + Holinshed 1577 procedural-role + Holinshed 1577 + Complete History 1706 Auray/Portugal corroborating section, and Rudder 1779 Almondsbury Over/Redwick/Gaunt's-Urcot section with the Pettigrew "Robert" vs Rudder "Richard" named-actor conflict.
- [ ] `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md` -- gains section 6.8 (Daniel 1613 witness) and Open-Question item 8 (Holinshed "Geneuay" alias note).
- [ ] `sources/intake/processed/stub-v67.md` and any later stale stubs (v70/v71/v72/v73) removed.
- [ ] `sources/intake/processed/stub-v74.md` -- created with standard next-stub template.
- [ ] `sources/intake/done/holinshed_1577_gurney_variant_research_notes.md` -- prep-notes working file moved alongside the patchset.

## Phase 2 completion step

After application:

```bash
python - <<'PY'
from pathlib import Path
src = Path("sources/intake/processed/v73-1577-1798-printed-witnesses-gourney-references.patchset.md")
dst = Path("sources/intake/done/v73-1577-1798-printed-witnesses-gourney-references.patchset.md")
body = src.read_text(encoding="utf-8")
dst.write_text("**Done:** 2026-05-28 HH:MM PT\n\n" + body, encoding="utf-8")
src.unlink()
PY
```

Replace `HH:MM` with the actual completion time.
