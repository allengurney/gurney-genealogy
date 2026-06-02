**Done:** 2026-06-02 16:09 PT
# Intake Phase 1 Patchset v80 - Cleveland Battle Abbey Roll PDF-backed expansion

Prepared: 2026-06-01 PT
Branch mode: main
Outcome: promote
Raw intake file: `sources/intake/new/The_Battle_Abbey_Roll.pdf`
User URL: `https://www.google.com/books/edition/The_Battle_Abbey_Roll/Y18JAAAAIAAJ?hl=en&gbpv=1&dq=gournay&pg=PA76&printsec=frontcover`
Follow-up volume sweep: 2026-06-01 PT, volumes 1 and 3 electronic texts at 1066.co.nz

## Intake finding

This is not a brand-new source in the repo. The Cleveland/Battle Abbey Roll Gurnay material already exists as:

- `data/sources.json` sourceId `cleveland-battle-abbey-roll-v2-gurnay`
- `sources/corpus_supplement/cleveland-battle-abbey-roll-v2-gurnay.md`
- `sources/validations/cleveland-battle-abbey-roll-v2-gurnay.md`
- topical landing at `research/topics/anderson-yvery-harpetre-gournay-collateral.md`

The existing capture is still partial and web-transcription oriented. The local PDF is a public-domain facsimile under 35 MB, so Phase 2 should promote it into `sources/media/cleveland-battle-abbey-roll-v2-gurnay/` and broaden the existing source record/validation/corpus note. Do not create a duplicate sourceId.

The Robert de Gournay that prompted the intake check is not the direct Norfolk line. In Cleveland's account he belongs to the Somerset/Harptree collateral line: Eva de Berkeley/de Gant is said to have had no Gournay blood, yet her son Robert adopted the Gournay name; Robert then held twenty-two and a half knight's fees, served against the Welsh, founded Gaunt's Hospital near Bristol, and left Anselm as heir. This belongs in the existing Anderson/Yvery/Harpetre collateral topic, not in a direct-line person file.

## Variant/source sweep

Searched existing repo content and the public electronic text for: `Battle Abbey Roll`, `Duchess of Cleveland`, `Gurnay`, `Gournay`, `Gourney`, `Gurney`, `Gorniaco`, `Gornai`, `Gornay`, `Gornaiu`, `Gurnai`, `Harpetree`, `Harptree`, `Inglishcombe`, `Barew`, `Bardolph`, `Warenne`, `Stuteville`, `Monceaux`, `Botetourt`, `Wauncy`, `Harpley`, and `West Barsham`.

Promote the following source-value conclusions:

- Existing source coverage is real but partial; this patchset expands it.
- Cleveland is derivative and should stay below DG, Blomefield, Anderson, Farrer, IPM, and primary records.
- The Gurnay entry is valuable because it compresses several distinct lines that readers can easily conflate: senior Gournay barons, Somerset/Harptree collateral Gournays, and the Norfolk direct-line-relevant branch.
- The "Robert de Gournay" in this source is the Somerset/Harptree collateral Robert, not Robert G22 or another direct-line Robert.
- Cross-entry mentions in volumes 1-3 add network context: Bardolf/Wermegay, Botetourt/Norfolk tenure, Talbot descent from Gerard de Gournay's daughter, de Gant-to-Robert de Gournay inheritance, Wauncy-to-West Barsham descent, and the King John / Mirabeau prisoner-custody notice for Hugh de Gournay.

## Phase 2 operations

### 1. Promote the local PDF into source media

Binary file operation:

- Create directory if missing: `sources/media/cleveland-battle-abbey-roll-v2-gurnay/`
- Move `sources/intake/new/The_Battle_Abbey_Roll.pdf` to `sources/media/cleveland-battle-abbey-roll-v2-gurnay/The_Battle_Abbey_Roll.pdf`

New file write: `sources/media/cleveland-battle-abbey-roll-v2-gurnay/README.md`

```md
# Cleveland, Battle Abbey Roll - Gurnay media

Source ID: `cleveland-battle-abbey-roll-v2-gurnay`

## Files

- `The_Battle_Abbey_Roll.pdf` - public-domain PDF facsimile of the Cleveland *Battle Abbey Roll* volume containing the Gurnay entry. Supplied in intake on 2026-06-01. The user also supplied the Google Books page URL for the Gournay/Gurnay section: `https://www.google.com/books/edition/The_Battle_Abbey_Roll/Y18JAAAAIAAJ?hl=en&gbpv=1&dq=gournay&pg=PA76&printsec=frontcover`.

## Use

Use the PDF as the page-image control copy for the existing 1066.co.nz electronic transcription. The searchable corpus note remains at `sources/corpus_supplement/cleveland-battle-abbey-roll-v2-gurnay.md`.
```

### 2. Update `data/sources.json`

`str_replace`:

```json
    "cleveland-battle-abbey-roll-v2-gurnay": {
      "shortTitle": "Cleveland, Battle Abbey Roll - Gurnay",
      "citation": "Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 2. London: John Murray, 1889.",
      "archive": "Belnap PDF / 1066.co.nz transcription",
      "url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/cleveland-battle-abbey-roll-v2-gurnay.md",
      "mediaPath": null,
      "validationPath": "sources/validations/cleveland-battle-abbey-roll-v2-gurnay.md",
      "notes": "Late-19th-century derivative account of the Gurnay/Gournay lineage. Useful as a synthesis and cross-check, not primary authority. The exact 1066.co.nz Gurnay entry was supplied in v08a and includes substantial detail on the Pays de Bray, Mortemar, Domesday Essex holdings, Gerard/Edith Warenne, the senior line's end, Somerset collateral Gournays, and the Norfolk mesne-lord branch."
    },
```

with:

```json
    "cleveland-battle-abbey-roll-v2-gurnay": {
      "shortTitle": "Cleveland, Battle Abbey Roll - Gurnay",
      "citation": "Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 2. London: John Murray, 1889.",
      "archive": "Local public-domain PDF / Google Books / 1066.co.nz transcription",
      "url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/cleveland-battle-abbey-roll-v2-gurnay.md",
      "mediaPath": "sources/media/cleveland-battle-abbey-roll-v2-gurnay/The_Battle_Abbey_Roll.pdf",
      "validationPath": "sources/validations/cleveland-battle-abbey-roll-v2-gurnay.md",
      "notes": "Late-19th-century derivative account of the Gurnay/Gournay lineage. Useful as a synthesis and cross-check, not primary authority. The source covers the senior Gournay barons, Somerset/Harptree collateral Gournays, and the Norfolk mesne-lord branch. Local PDF promoted in v80; 1066.co.nz remains the convenient searchable transcription; Google Books page URL supplied for image control. The Robert de Gournay in this source is the Somerset/Harptree collateral Robert, not a direct-line Robert."
    },
```

### 2a. Add source IDs for volume 1 and volume 3 cross-reference notes

`str_replace`:

```json
    "cleveland-battle-abbey-roll-introduction": {
      "shortTitle": "Cleveland, Battle Abbey Roll introduction",
      "citation": "Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 1, introduction.",
      "archive": "1066.co.nz electronic edition / user-supplied markdown",
      "url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/introduction.html",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/cleveland-battle-abbey-roll-introduction-gurnay.md",
      "mediaPath": null,
      "validationPath": "sources/validations/cleveland-battle-abbey-roll-introduction.md",
      "notes": "Battle Abbey Roll introduction and list comparison. Relevant for Gournay/Gurnay/Gurney roll variants, duplicate Hue de Gourney/Hue earl of Gournay forms, and caution about roll incompleteness/interpolation."
    },
```

with:

```json
    "cleveland-battle-abbey-roll-introduction": {
      "shortTitle": "Cleveland, Battle Abbey Roll introduction",
      "citation": "Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 1, introduction.",
      "archive": "1066.co.nz electronic edition / user-supplied markdown",
      "url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/introduction.html",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/cleveland-battle-abbey-roll-introduction-gurnay.md",
      "mediaPath": null,
      "validationPath": "sources/validations/cleveland-battle-abbey-roll-introduction.md",
      "notes": "Battle Abbey Roll introduction and list comparison. Relevant for Gournay/Gurnay/Gurney roll variants, duplicate Hue de Gourney/Hue earl of Gournay forms, and caution about roll incompleteness/interpolation."
    },
    "cleveland-battle-abbey-roll-v1-crossrefs": {
      "shortTitle": "Cleveland, Battle Abbey Roll vol. 1 crossrefs",
      "citation": "Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 1. London: John Murray, 1889.",
      "archive": "1066.co.nz electronic edition",
      "url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol1.html",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/cleveland-battle-abbey-roll-v1-gurnay-crossrefs.md",
      "mediaPath": null,
      "validationPath": "sources/validations/cleveland-battle-abbey-roll-v1-crossrefs.md",
      "notes": "Derivative cross-reference sweep of volume 1 for Gurnay/Gurney variants and related family/place entries. Useful for roll-list duplication of Gurnay/Gurney, Bardolf/Wormegay context, and Botetourt lands held of the honour of Gournay. Use as corroborative/lead material only."
    },
    "cleveland-battle-abbey-roll-v3-crossrefs": {
      "shortTitle": "Cleveland, Battle Abbey Roll vol. 3 crossrefs",
      "citation": "Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 3. London: John Murray, 1889.",
      "archive": "1066.co.nz electronic edition",
      "url": "https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol3.html",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/cleveland-battle-abbey-roll-v3-gurnay-crossrefs.md",
      "mediaPath": null,
      "validationPath": "sources/validations/cleveland-battle-abbey-roll-v3-crossrefs.md",
      "notes": "Derivative cross-reference sweep of volume 3 for Gournay/Gourney/Wauncy/Talbot/Gant/Vipont material. Most useful items: Talbot marriage to Gerard de Gournay's daughter; Emma de Gant's son Robert de Gournay as Maurice de Gant's heir; Wauncy-to-West Barsham descent through Katherine wife of Edmund de Gournay; and a King John/Mirabeau prisoner-custody lead involving Hugh de Gournay. Use as corroborative/lead material only."
    },
```

### 3. Replace `sources/corpus_supplement/cleveland-battle-abbey-roll-v2-gurnay.md`

`str_replace` whole file:

```md
# Cleveland, Battle Abbey Roll - Gurnay

- Source ID: `cleveland-battle-abbey-roll-v2-gurnay`
- Citation: Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 2. London: John Murray, 1889.
- Archive: Belnap PDF / 1066.co.nz transcription
- URL: https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol2.html
- Intake patchset: `sources/intake/processed/v06.patchset.md`

## Extracted research value

Late-19th-century derivative account of the Gurnay/Gournay lineage. Useful as a synthesis and cross-check, not primary authority. Belnap PDF OCR was usable mainly for index; 1066.co.nz HTML exposed the Gurnay entry.

## Supplemental extraction - v08a

The user-supplied 1066.co.nz Gurnay entry supports a fuller derivative extraction:

- The family is placed in the Pays de Bray frontier district and tied to Gournay, the head of the barony.
- Cleveland says the fief was allotted to a Gournay ancestor by Rollo and held until Philip Augustus seized it in King John's time.
- The castle tradition includes "La Tour Hue," a triple wall and fosse, and a claim of extraordinary strength.
- Hugh/Hue de Gournay is placed at Mortemar in 1054 and at Hastings, with Wace's line on "li viel Hue de Gornai."
- Cleveland says Hugh had invaded England more than thirty years before Hastings with the fleet supporting the Saxon prince Edward after Canute's death.
- Cleveland preserves the heraldic tradition that the Gournays first bore pure sable and later changed to Argent, a cross engrailed Gules, by Sir John de Gurney in Henry III's time.
- Cleveland distinguishes "Hue le vieil" from the Domesday-era Hugh, treating the latter as probably the son.
- The second Hugh is said to have ended his life as a monk at Bec.
- Gerard de Gournay appears as baron of Yarmouth in 1089, supporter of William Rufus against Robert Curthose, and companion of Robert on the Holy Land journey in 1096, where he died.
- Edith/Editha de Warenne is named as Gerard's wife and mother of Hugh, Gundreda the Fair, and an unnamed Talbot ancestress.
- Later senior-line Hughs are tied to Henry I, Stephen's reign, the 1173 burning of Gournay castle, Acre under Richard I, and estate loss under King John.
- The principal line ends with Julian/Juliana de Gournay, wife of William Bardolph.
- Cleveland separates the Somerset collateral line from the Norfolk direct-line-relevant branch.
- The Norfolk Gurneys are described as mesne lords under their baronial cousins, first appearing in Norfolk in Henry II's time.
- Harpley is tied to Rose de Burnham or de Warenne; West Barsham is tied to the Wauncy heiress and Edmund Gourney.
- Cleveland jumps forward to John Gurney, Norwich silk merchant about 1679, and the later Quaker/Norwich banking Gurneys.

## Findings landed in

- `research/topics/anderson-yvery-harpetre-gournay-collateral.md`
```

with:

```md
# Cleveland, Battle Abbey Roll - Gurnay

- Source ID: `cleveland-battle-abbey-roll-v2-gurnay`
- Citation: Cleveland, Duchess of. The Battle Abbey Roll, with Some Account of the Norman Lineages. Vol. 2. London: John Murray, 1889.
- Archive: local public-domain PDF / Google Books / 1066.co.nz transcription
- URL: https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html
- Local media: `sources/media/cleveland-battle-abbey-roll-v2-gurnay/The_Battle_Abbey_Roll.pdf`
- Google Books page control: `https://www.google.com/books/edition/The_Battle_Abbey_Roll/Y18JAAAAIAAJ?hl=en&gbpv=1&dq=gournay&pg=PA76&printsec=frontcover`
- Intake patchsets: `sources/intake/done/v06-future-research-urls.patchset.md`; `sources/intake/done/v08a-future-research-urls2-audit-supplement.patchset.md`; `sources/intake/processed/v80-cleveland-battle-abbey-roll-pdf-expansion.patchset.md`

## Extracted research value

Late-19th-century derivative account of the Gurnay/Gournay lineage. Use it as a synthesis and comparison source, not as controlling authority over DG, Anderson, Blomefield, Farrer, IPM records, or primary charters. The useful value is not a new direct-line proof; it is the way Cleveland compresses three easily conflated traditions in one place:

1. the senior Gournay barons of Gournay-en-Bray;
2. the Somerset/Harptree collateral Gournays;
3. the Norfolk mesne-lord branch that leads toward Harpley and West Barsham.

## Variant sweep

Relevant spellings and forms in the source/transcription cluster include `Gurnay`, `Gournay`, `Gourney`, `Gurney`, `Gorniaco`, `Gornai`, `Gornay`, `Gurnai`, `Hue de Gourney`, `Hue earl of Gournay`, and `Gurnay et Greilly`. Treat the Battle Abbey Roll forms as name-variant and transmission evidence; do not make separate people or titles from variant roll forms without stronger support.

## Gurnay-entry findings

- The family is placed in the Pays de Bray frontier district and tied to Gournay, the head of the barony.
- Cleveland says the fief was allotted to a Gournay ancestor by Rollo and held until Philip Augustus seized it in King John's time.
- The castle tradition includes "La Tour Hue," a triple wall and fosse, and a claim of extraordinary strength.
- Hugh/Hue de Gournay is placed at Mortemar in 1054 and at Hastings, with Wace's line on old Hue of Gournay and his men of Bray.
- Cleveland says Hugh had invaded England more than thirty years before Hastings with the fleet supporting the Saxon prince Edward after Canute's death.
- Cleveland preserves the heraldic tradition that the Gournays first bore pure sable and later changed to Argent, a cross engrailed Gules, by Sir John de Gurney in Henry III's time.
- Cleveland distinguishes "Hue le vieil" from the Domesday-era Hugh, treating the latter as probably the son.
- The second Hugh is said to have ended his life as a monk at Bec.
- Gerard de Gournay appears as baron of Yarmouth in 1089, supporter of William Rufus against Robert Curthose, and companion of Robert on the Holy Land journey in 1096, where Cleveland says he died.
- Edith/Editha de Warenne is named as Gerard's wife and mother of Hugh, Gundreda the Fair, and an unnamed Talbot ancestress.
- Later senior-line Hughs are tied to Henry I, Stephen's reign, the 1173 burning of Gournay castle, Acre under Richard I, and estate loss under King John.
- The principal line ends with Julian/Juliana de Gournay, wife of William Bardolph.
- Cleveland separates the Somerset collateral line from the Norfolk direct-line-relevant branch.
- The Norfolk Gurneys are described as mesne lords under their baronial cousins, first appearing in Norfolk in Henry II's time.
- Harpley is tied to Rose de Burnham or de Warenne; West Barsham is tied to the Wauncy heiress and Edmund Gourney.
- Cleveland jumps forward to John Gurney, Norwich silk merchant about 1679, and the later Quaker/Norwich banking Gurneys.

## Robert de Gournay disposition

The Robert de Gournay in Cleveland's Gurnay entry is the Somerset/Harptree collateral Robert, not a direct-line Norfolk Robert. Cleveland says Eva de Berkeley/de Gant had no Gournay blood, yet her son Robert adopted the Gournay name rather than Berkeley, Gant, Paganel, or Dowai/Bahantune. Robert then held twenty-two and a half knight's fees, was summoned to serve against the Welsh, founded the hospital of Gaunt near Bristol for Maurice de Gant's soul, and left Anselm as heir by Hawise de Longchamp.

This supports the existing Anderson/Yvery/Harpetre topic framing: the Somerset Gournay surname is an adopted collateral name and should not be conflated with the direct Norfolk junior line.

## Cross-entry network notes

- Estouteville/Stuteville: the Estuteville entry says Nicholas de Stuteville married Gunnor de Gant, daughter of Hugh IV de Gournay, and received Beddingfield and Kimberley in Norfolk in dower. It also ties Estouteville to La Ferte-en-Brai, a dependency of the Gournay fief.
- Monceaux: the Monceaux entry repeats that Edith de Warenne first married Gerard de Gournay, then Dru de Monceaux; Dru possessed the honour of Gournay during the minority of Edith's son Hugh.
- Botetourt: the Botetourt entry in volume 1 says the Norfolk Botetourts settled on lands granted by Hugh de Gourney in Henry III's time, and that Guy de Botetourt held Uphall manor of Lord Bardolf as part of the honour of Gournay.
- Lovell/Harptree: the Lovell entry says John, youngest son of Ascelin Gouel, was portioned in Harptree, took that name, and later changed it to Gournay. This reinforces the adopted-name explanation for the Somerset collateral line.
- Bardolf: the volume 1 Bardolf entry gives the Bardolf/Wormegay background relevant to Julian/Juliana de Gournay's senior-line inheritance context, but it does not add a better source than existing Bardolf/Gournay materials.
- Talbot: the volume 3 Talbot entry repeats the tradition that Richard Talbot married a daughter of Gerard de Gournay and had sons Geoffrey, ancestor of the Talbots of Bashall, and Hugh, ancestor of the Earls of Shrewsbury. This is useful as derivative corroboration for the Talbot/Gournay marriage network already treated on G32.
- Gant: the volume 3 Gaunt/Gant entry says Maurice de Gant died without issue in 1229 and that his sister Emma's son Robert de Gournay was his heir, reinforcing the de Gant-to-Robert de Gournay inheritance path in the Somerset collateral line.
- Wauncy: the volume 3 Wauncy entry says Hugh and Osbern de Wanceio held Suffolk fiefs in 1086, Hugh was Earl Warenne's mesne-tenant at West Barsham, the line remained in Norfolk about three hundred years, Sir Edmund de Wauncy died in 1372, his young son died soon after, and the succession passed through Katherine wife of Edmund de Gournay, with West Barsham devolving on the Gournays because Joan wife of Sir Nicholas Damory was childless. This is the strongest new item from the volume 1/3 sweep.
- Vipont: the volume 3 Vipont entry says Robert de Vipont had custody of prisoners taken at Mirabeau in 4 John, including Arthur of Brittany, until ordered to deliver them to Hugh de Gournay. This is a striking King John / Hugh V comparison-source lead, but it is derivative and should be checked against Dugdale or the primary record before promotion beyond the senior-line topic.

## Findings landed in

- `research/topics/anderson-yvery-harpetre-gournay-collateral.md`
```

### 4. Update `sources/validations/cleveland-battle-abbey-roll-v2-gurnay.md`

`str_replace` whole file:

```md
# Cleveland, Battle Abbey Roll - Gurnay validation

- Examined: https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol2.html, accessed 2026-05-01; exact Gurnay-entry URL https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html supplied in v08/v08a.
- Scope: Gurnay entry in the Battle Abbey Roll derivative synthesis.
- Findings recorded in: `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v06.patchset.md`.
- v08/v08a follow-up: expanded derivative synthesis details are in `sources/corpus_supplement/cleveland-battle-abbey-roll-v2-gurnay.md`.
```

with:

```md
# Cleveland, Battle Abbey Roll - Gurnay validation

- Source ID: `cleveland-battle-abbey-roll-v2-gurnay`
- Examined: 1066.co.nz searchable transcription, exact Gurnay-entry URL `https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html`; local PDF supplied at `sources/intake/new/The_Battle_Abbey_Roll.pdf`; user-supplied Google Books page URL `https://www.google.com/books/edition/The_Battle_Abbey_Roll/Y18JAAAAIAAJ?hl=en&gbpv=1&dq=gournay&pg=PA76&printsec=frontcover`.
- Scope: Gurnay/Gournay/Gourney/Gurney variant sweep across the Gurnay entry and selected cross-entry mentions in Cleveland's *Battle Abbey Roll*, especially Estouteville/Stuteville, Monceaux, Botetourt, Lovell/Harptree, Bardolph, Warenne, Harpley, West Barsham, and Wauncy.
- Findings recorded in: `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.
- Corpus note: `sources/corpus_supplement/cleveland-battle-abbey-roll-v2-gurnay.md`.
- Media after v80 Phase 2: `sources/media/cleveland-battle-abbey-roll-v2-gurnay/The_Battle_Abbey_Roll.pdf`.
- Detailed phase 1 extraction and file operations: `sources/intake/done/v06-future-research-urls.patchset.md`; `sources/intake/done/v08a-future-research-urls2-audit-supplement.patchset.md`; `sources/intake/processed/v80-cleveland-battle-abbey-roll-pdf-expansion.patchset.md`.

## Limits

Cleveland is derivative. Use it as corroborative synthesis and as a guide to variant spelling and family-network relationships. Do not use it to override Daniel Gurney, Anderson, Blomefield, Farrer, IPM records, or primary charters. The Robert de Gournay in this source is the Somerset/Harptree collateral Robert, not a direct-line Robert.
```

### 4a. Write volume 1 and volume 3 corpus notes

New file write: `sources/corpus_supplement/cleveland-battle-abbey-roll-v1-gurnay-crossrefs.md`

```md
# Cleveland, Battle Abbey Roll vol. 1 - Gurnay cross-references

- Source ID: `cleveland-battle-abbey-roll-v1-crossrefs`
- Citation: Cleveland, Duchess of. *The Battle Abbey Roll, with Some Account of the Norman Lineages*. Vol. 1. London: John Murray, 1889.
- URL: https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol1.html
- Intake patchset: `sources/intake/processed/v80-cleveland-battle-abbey-roll-pdf-expansion.patchset.md`

## Extracted research value

Volume 1 adds derivative cross-reference value rather than new direct-line proof.

- The volume 1 roll-list table preserves both `Gurnay` and `Gurney` as separate forms under G. This supports the existing introduction-source conclusion that Battle Abbey Roll forms are variant/transmission evidence, not separate proof of people or titles.
- The Bardolf entry supplies Wormegay/Bardolf background relevant to the senior-line inheritance context, but it does not improve on stronger Bardolf/Gournay sources already in the repo.
- The Botetourt entry says the Norfolk Botetourts settled on lands granted by Hugh de Gourney in Henry III's time, and that Guy de Botetourt held Uphall manor of Lord Bardolf as part of the honour of Gournay. This is derivative support for the broader senior-line Norfolk tenure network.

## Disposition

Use as a corroborative and lead source only. Findings land in `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.
```

New file write: `sources/corpus_supplement/cleveland-battle-abbey-roll-v3-gurnay-crossrefs.md`

```md
# Cleveland, Battle Abbey Roll vol. 3 - Gurnay cross-references

- Source ID: `cleveland-battle-abbey-roll-v3-crossrefs`
- Citation: Cleveland, Duchess of. *The Battle Abbey Roll, with Some Account of the Norman Lineages*. Vol. 3. London: John Murray, 1889.
- URL: https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol3.html
- Intake patchset: `sources/intake/processed/v80-cleveland-battle-abbey-roll-pdf-expansion.patchset.md`

## Extracted research value

Volume 3 has several useful derivative cross-references:

- Talbot: the Talbot entry repeats that Richard Talbot married a daughter of Gerard de Gournay, baron of Yarmouth, and had Geoffrey, ancestor of the Talbots of Bashall, and Hugh, ancestor of the Earls of Shrewsbury. This is derivative corroboration for the Talbot/Gournay marriage network already treated on G32.
- Gant: the Gaunt/Gant entry says Maurice de Gant died without issue in 1229 and that his sister Emma's son Robert de Gournay was his heir. This reinforces the de Gant-to-Robert de Gournay inheritance path in the Somerset collateral line.
- Wauncy: the Wauncy entry says Hugh and Osbern de Wanceio held Suffolk fiefs in 1086, Hugh was Earl Warenne's mesne-tenant at West Barsham, the line remained in Norfolk about three hundred years, Sir Edmund de Wauncy died in 1372, his young son died soon after, and the succession passed through Katherine wife of Edmund de Gournay, with West Barsham devolving on the Gournays because Joan wife of Sir Nicholas Damory was childless. This is the strongest new item from the volume 1/3 sweep.
- Vipont: the Vipont entry says Robert de Vipont had custody of prisoners taken at Mirabeau in 4 John, including Arthur of Brittany, until ordered to deliver them to Hugh de Gournay. This is a King John / Hugh V comparison-source lead; check Dugdale or the primary record before using it as more than a lead.

## Disposition

Use as a corroborative and lead source only. Findings land in `research/topics/anderson-yvery-harpetre-gournay-collateral.md`; the Wauncy item may also support `research/places/west-barsham.md` in a future direct edit, but v80 does not patch that place file because Armstrong and DG/Blomefield already carry stronger West Barsham evidence there.
```

### 4b. Write volume 1 and volume 3 validation notes

New file write: `sources/validations/cleveland-battle-abbey-roll-v1-crossrefs.md`

```md
# Cleveland, Battle Abbey Roll vol. 1 crossrefs validation

- Source ID: `cleveland-battle-abbey-roll-v1-crossrefs`
- Examined: 1066.co.nz electronic text of volume 1, `https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol1.html`.
- Scope: Gurnay/Gurney roll-list forms and selected Bardolf/Botetourt cross-references.
- Findings recorded in: `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.
- Corpus note: `sources/corpus_supplement/cleveland-battle-abbey-roll-v1-gurnay-crossrefs.md`.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v80-cleveland-battle-abbey-roll-pdf-expansion.patchset.md`.

## Limits

Cleveland is derivative. Use volume 1 as variant/transmission and family-network evidence only, not as controlling proof.
```

New file write: `sources/validations/cleveland-battle-abbey-roll-v3-crossrefs.md`

```md
# Cleveland, Battle Abbey Roll vol. 3 crossrefs validation

- Source ID: `cleveland-battle-abbey-roll-v3-crossrefs`
- Examined: 1066.co.nz electronic text of volume 3, `https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol3.html`.
- Scope: Gournay/Gourney/Wauncy/Talbot/Gant/Vipont cross-references.
- Findings recorded in: `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.
- Corpus note: `sources/corpus_supplement/cleveland-battle-abbey-roll-v3-gurnay-crossrefs.md`.
- Detailed phase 1 extraction and file operations: `sources/intake/processed/v80-cleveland-battle-abbey-roll-pdf-expansion.patchset.md`.

## Limits

Cleveland is derivative. The Wauncy and Gant notes are useful corroborative summaries; the Vipont/Mirabeau prisoner-custody note is a lead until checked against Dugdale or a primary record.
```

### 5. Update `research/topics/anderson-yvery-harpetre-gournay-collateral.md`

`str_replace`:

```md
### Cleveland and the 1066 Mosaic pages as derivative Gournay syntheses

The Duchess of Cleveland's *Battle Abbey Roll* is derivative and should not override DG or primary records, but it is useful as a concise late-Victorian synthesis. It states that the Gournays held the Pays de Bray and Gournay as their barony, that Gerard de Gournay married Edith Warenne and died on pilgrimage, that the senior line ended through Julian/Juliana's marriage to William Bardolf, and that the Norfolk Gurneys were originally mesne-lords under their baronial cousins and first appear in Norfolk in Henry II's time. It also repeats the Harpley/Rose de Burnham or Warenne and West Barsham/Wauncy summaries.[^topic-cleveland]

The separate 1066 Mosaic "Hugue de Gournay" page compresses the same tradition in a Battle Abbey Roll framing. It says Hugo de Gournay, lord of Gournay in Normandy, bore "pure sable," commanded at Mortemer in 1054, came to England with Duke William, participated at Hastings, and held Essex manors at Domesday. It makes Gerard de Gournay, baron of Gournay in Normandy and Yarmouth in England, husband of Editha, daughter of William de Warenne; gives their children as Hugh, Gundred wife of Nigel de Albini, and a daughter who married Richard de Talbot; and says the principal male line ended with Julia/Julian de Gournay's marriage to William Bardolph of Wormegay. For the Norfolk branch, it says the Norfolk Gournays held manors as mesne lords under the baronial Gournays and that the Gurneys of Harpley and West Barsham descended from this branch, with the Norfolk Gurneys represented in the nineteenth century by Hudson Gurney of Keswick.[^topic-mosaic-hugue]

Use Cleveland as a comparison source only. Where it conflicts with DG or primary records, preserve the conflict and pursue the primary record.
```

with:

```md
### Cleveland and the 1066 Mosaic pages as derivative Gournay syntheses

The Duchess of Cleveland's *Battle Abbey Roll* is derivative and should not override DG, Anderson, Blomefield, Farrer, IPM records, or primary charters, but it is a useful late-Victorian compression of the three Gournay traditions most easily conflated: the senior Gournay barons of Gournay-en-Bray, the Somerset/Harptree collateral Gournays, and the Norfolk mesne-lord branch that leads toward Harpley and West Barsham.[^topic-cleveland]

Cleveland's Gurnay entry restates the senior-line frame: Gournay in the Pays de Bray; the Rollo allotment tradition; La Tour Hue; old Hue at Mortemar and Hastings; the pure-sable arms; the Domesday-era Hugh ending as a monk at Bec; Gerard de Gournay, Edith de Warenne, Gundreda, and the Talbot daughter; later senior Hughs in Henry I, Stephen, Acre, and King John contexts; and the senior line ending with Julian/Juliana de Gournay, wife of William Bardolph. This is useful as comparison synthesis, not as fresh proof where stronger sources already exist.[^topic-cleveland]

The Robert de Gournay that appears in Cleveland is the Somerset/Harptree collateral Robert, not a direct-line Norfolk Robert. Cleveland's explanation matches this file's Anderson/Yvery warning: Eva de Berkeley/de Gant had no Gournay blood, yet her son Robert adopted the Gournay name; Robert then held twenty-two and a half knight's fees, was summoned against the Welsh, founded the hospital of Gaunt near Bristol for Maurice de Gant's soul, and left Anselm as heir by Hawise de Longchamp. The point is valuable precisely because it prevents a false merge between the Somerset collateral line and the direct Norfolk line.[^topic-cleveland]

The other two volumes add network context in neighboring entries. Volume 1 preserves the roll-list duplication of `Gurnay` and `Gurney`; gives Bardolf/Wormegay background for the senior-line inheritance context; and says the Norfolk Botetourts settled on lands granted by Hugh de Gourney, with Guy de Botetourt holding Uphall manor of Lord Bardolf as part of the honour of Gournay. Volume 3 supplies the stronger collateral notes: the Talbot entry repeats Richard Talbot's marriage to Gerard de Gournay's daughter; the Gant entry says Maurice de Gant died without issue in 1229 and that his sister Emma's son Robert de Gournay was his heir; the Wauncy entry traces West Barsham from Hugh de Wanceio under Earl Warenne to Katherine wife of Edmund de Gournay; and the Vipont entry says King John's Mirabeau prisoners, including Arthur of Brittany, were ordered delivered to Hugh de Gournay. These are comparison-source notes and leads, not controlling proof.[^topic-cleveland-v1-crossrefs][^topic-cleveland-v3-crossrefs]

The separate 1066 Mosaic "Hugue de Gournay" page compresses the same tradition in a Battle Abbey Roll framing. It says Hugo de Gournay, lord of Gournay in Normandy, bore "pure sable," commanded at Mortemer in 1054, came to England with Duke William, participated at Hastings, and held Essex manors at Domesday. It makes Gerard de Gournay, baron of Gournay in Normandy and Yarmouth in England, husband of Editha, daughter of William de Warenne; gives their children as Hugh, Gundred wife of Nigel de Albini, and a daughter who married Richard de Talbot; and says the principal male line ended with Julia/Julian de Gournay's marriage to William Bardolph of Wormegay. For the Norfolk branch, it says the Norfolk Gournays held manors as mesne lords under the baronial Gournays and that the Gurneys of Harpley and West Barsham descended from this branch, with the Norfolk Gurneys represented in the nineteenth century by Hudson Gurney of Keswick.[^topic-mosaic-hugue]

Use Cleveland and the 1066 Mosaic pages as comparison sources only. Where they conflict with DG or primary records, preserve the conflict and pursue the primary record.
```

### 5a. Add footnote definitions for the new volume 1 and volume 3 topic citations

`str_replace`:

```md
[^topic-cleveland]: Duchess of Cleveland, *The Battle Abbey Roll, with Some Account of the Norman Lineages*, vol. 2 (London: John Murray, 1889), [Gurnay entry, 1066.co.nz transcription](https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html). Source ID: `cleveland-battle-abbey-roll-v2-gurnay`.
[^topic-mosaic-hugue]: ["Hugue de Gournay,"](https://www.1066.co.nz/Mosaic%20DVD/text/people/gournay.htm) 1066 Mosaic / Battle Abbey Roll derivative page. Source ID: `mosaic-dvd-hugue-de-gournay`.
```

with:

```md
[^topic-cleveland]: Duchess of Cleveland, *The Battle Abbey Roll, with Some Account of the Norman Lineages*, vol. 2 (London: John Murray, 1889), [Gurnay entry, 1066.co.nz transcription](https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/Gurnay.html). Source ID: `cleveland-battle-abbey-roll-v2-gurnay`.
[^topic-cleveland-v1-crossrefs]: Duchess of Cleveland, *The Battle Abbey Roll, with Some Account of the Norman Lineages*, vol. 1 (London: John Murray, 1889), selected roll-list, Bardolf, and Botetourt entries, [1066.co.nz electronic edition](https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol1.html). Source ID: `cleveland-battle-abbey-roll-v1-crossrefs`.
[^topic-cleveland-v3-crossrefs]: Duchess of Cleveland, *The Battle Abbey Roll, with Some Account of the Norman Lineages*, vol. 3 (London: John Murray, 1889), selected Talbot, Gant, Wauncy, and Vipont entries, [1066.co.nz electronic edition](https://www.1066.co.nz/Mosaic%20DVD/library/Battle%20Roll/battleabbeyroll%20vol3.html). Source ID: `cleveland-battle-abbey-roll-v3-crossrefs`.
[^topic-mosaic-hugue]: ["Hugue de Gournay,"](https://www.1066.co.nz/Mosaic%20DVD/text/people/gournay.htm) 1066 Mosaic / Battle Abbey Roll derivative page. Source ID: `mosaic-dvd-hugue-de-gournay`.
```

No fact-sheet changes in this patchset. The source is derivative and the new value is mainly disambiguation and source-control, not a stable new published ancestor fact.

## Post-apply checks

Run after Phase 2:

1. `git diff --check`
2. `npm.cmd run validate` from `site/website`

No package run is required unless Phase 2 also changes published fact sheets or site-rendered data beyond source catalog generation.
