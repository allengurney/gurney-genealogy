**Done:** 2026-06-02 16:09 PT
# v82 patchset - SCRIPTA Gournay acts, "Apocryphal Book of Dan", Delisle, arms/pedigree leads

Prepared: 2026-06-02
Phase: 1 preparation
Scope: Add a selected SCRIPTA corpus supplement for Hugh de Gournay / Gerard / Basilia acts, route the new findings into G33/G32 and Bec-place research, record the "Apocryphal Book of Dan" reception note, update the arms/pedigree audit, and add only the highest-value new open leads to `research/future-research/research-leads.csv`.

## Intake summary

This patchset is intentionally broader than the first research pass. It treats the SCRIPTA act roster as a source cluster, not as isolated act snippets, and routes the findings in four directions:

- `sources/corpus_supplement/` receives a compact selected-act corpus for all SCRIPTA acts found in this pass that mention Gournay/Gornaco/Gurnai variants or the Hugh-Gerard-Basilia family cluster.
- `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` and `research/people/g32-gerard-de-gournay-fact-sheet.research.md` receive the English-side Bec/London findings, the 1077 Bec father-son donor clause, and the 1082 La Trinite witness correction.
- `research/places/g33-bec-gournay-endowment-cluster.md`, `research/places/le-bec-hellouin.md`, and `research/places/city-of-london.md` receive the place/revenue implications.
- `research/topics/dg-reception-delisle-critique.md` and `research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md` receive the Daniel Gurney nickname/reception evidence and the newly surfaced Norfolk pedigree/arms manuscript-source map.

## New source IDs proposed

Add these source IDs to `data/sources.json`.

### `unicaen-scripta-selected-gournay-acts`

Use after `normonde-hugues-1er-de-gournay`:

```json
    "unicaen-scripta-selected-gournay-acts": {
      "shortTitle": "SCRIPTA selected Gournay acts",
      "citation": "Universite de Caen Normandie / CRAHAM-MRSH, SCRIPTA: Base des actes normands medievaux, selected acts relating to Hugh de Gournay, Basilia, Gerard, and Gournay/Gornaco/Gurnai variants.",
      "archive": "SCRIPTA online act records",
      "url": "https://mrsh.unicaen.fr/scripta/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/unicaen-scripta-selected-gournay-acts.md",
      "mediaPath": null,
      "validationPath": "sources/validations/unicaen-scripta-selected-gournay-acts.md",
      "notes": "Selected SCRIPTA acts from the Normonde Hugues Ier de Gournay authority roster and follow-on act exploration. Includes Acts 151, 1633, 1661, 6458, 6463, 6466, 6467, 6472, 6511, 6512, 6520, 6523, 6538, and 6565. Key findings: Act 151 directly names Hugh, Basilia, and Gerard consenting to Raoul Havoth's Jumieges donation at Hugonis Silva/Boschyons; Act 6511 directly names Hugh de Gornaco and his son Gerard donating their domain in the same villa, contextually Bois Girard, to Bec; Act 6512 preserves William I's confirmation that Hugh gave Bec what he held of the king in London plus Fordham, Ardleigh, and Liston rights; Act 6538 provides modern SCRIPTA/Bates/Fauroux control for the Cauville/Montivilliers sale already printed by Daniel Gurney."
    },
```

### `rye-index-rerum-norfolk-antiquities-1910`

Add near the Norfolk visitation / Rye entries:

```json
    "rye-index-rerum-norfolk-antiquities-1910": {
      "shortTitle": "Index Rerum to Norfolk Antiquities (Rye, 1910)",
      "citation": "Rye, Walter, comp. An Index Rerum to Norfolk Antiquities. Norwich: 1910.",
      "archive": "Internet Archive / Wikimedia Commons PDF",
      "url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/An_index_rerum_to_Norfolk_antiquities_%28IA_indexrerumtonorf00ryewrich%29.pdf",
      "corpusStatus": "partial",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/rye-index-rerum-norfolk-antiquities-1910.md",
      "notes": "Norfolk antiquarian index source. Under Apocryphal Book of Dan it directs readers to the Gurney pedigree entry; under Gurney it lists Daniel Gurney's Record as otherwise known as the Apocryphal Book of Dan and collects manuscript pedigree leads including Harl. MS 4755 fo.81, Harl. MS 1552 p.48, and John H. Gurney of Keswick MSS."
    },
```

### `sanhs-excursions-1907-apocryphal-book-dan`

Add near Daniel Gurney / Somerset collateral source entries:

```json
    "sanhs-excursions-1907-apocryphal-book-dan": {
      "shortTitle": "SANHS Excursions: Apocryphal Book of Dan note",
      "citation": "Somerset Archaeological and Natural History Society, excursion report PDF, note on Daniel Gurney's mistaken use of a house as Sir Matthew Gournay's residence and the informal title 'Apocryphal Book of Dan.'",
      "archive": "SANHS online PDF",
      "url": "https://sanhs.org/wp-content/uploads/2020/08/02Excursions.pdf",
      "corpusStatus": "partial",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/sanhs-excursions-1907-apocryphal-book-dan.md",
      "notes": "Useful reception note: the report says Daniel Gurney's book was generally known among his friends as the 'Apocryphal Book of Dan,' citing The Bibliographer, I, 59. Treat as informal/friendly nickname, not as a separate edition or alternate text."
    },
```

### `potts-monastic-revival-regional-identity-1997`

Add near Norman ecclesiastical sources:

```json
    "potts-monastic-revival-regional-identity-1997": {
      "shortTitle": "Potts, Monastic Revival and Regional Identity (1997)",
      "citation": "Potts, Cassandra. Monastic Revival and Regional Identity in Early Normandy. Studies in the History of Medieval Religion 11. Woodbridge: Boydell Press, 1997.",
      "archive": "published monograph; online snippet consulted",
      "url": null,
      "corpusStatus": "not-captured",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/potts-monastic-revival-regional-identity-1997.md",
      "notes": "Modern scholarly control for the Montivilliers/Cauville transaction in SCRIPTA Act 6538. Potts pp. 42-43 treats the Cauville sale as an example of a sale later recast as ducal gift and cites Jean-Michel Bouvris, 'La renaissance de l'abbaye de Montivilliers autour de l'an mil,' in L'abbaye de Montivilliers a travers les ages (Montivilliers, 1988), pp. 67-84."
    },
```

## New corpus supplement

Create `sources/corpus_supplement/unicaen-scripta-selected-gournay-acts.md`.

```markdown
# SCRIPTA selected Gournay acts

Source ID: `unicaen-scripta-selected-gournay-acts`

This corpus supplement preserves selected Gournay-relevant extracts from SCRIPTA act records reached through the Normonde authority file for Hugues Ier de Gournay and follow-on act-roster exploration. It is not a full SCRIPTA corpus; it is a targeted extract set for Hugh de Gournay, Basilia, Gerard, Bec, Jumieges, Caen, Montivilliers, and variant spellings Gornaco/Gorniaco/Gurniaco/Gurnai/Gornaio.

## Act 151 - Raoul Havoth donation to Jumieges

URL: https://mrsh.unicaen.fr/scripta/doc/sc_151.html

Date: [1049-1087].

Summary: Raoul Havoth gives his son to Jumieges and gives land/tithes at the villa called Hugh's Wood / Hugonis Silva, with the assent of Hugh de Gournay, Hugh's son Gerard, and Basilia.

Relevant Latin:

> Dedi etiam sancto Petro Gemmeticensi apud villam quae vocatur Hugonis Silva centum jugera minus .X. et quicquid decimarum predicte ville ego possederam in dotem filii mei et in honorem sancti Petri Gemmeticensis, domino meo Hugone Gurnacensi et filio ejus Girardo et uxore ejus Basilia annuentibus et volentibus et laudantibus, quorum haec sunt signa. Signum H[ugonis] Gornacensis. Signum Basilie uxoris ejus. Signum Radulfi Havot. Ego vero Athelinus Gornacensis ecclesie tesaurarius confirmo.

English working extract: Raoul Havoth gives to Saint Peter of Jumieges land at the villa called Hugh's Wood and whatever tithes he held there, with Hugh de Gournay, Gerard his son, and Basilia his wife consenting, willing, and approving. The act's signa include Hugh Gornacensis, Basilia, Raoul Havoth, and Athelinus Gornacensis, treasurer of the church.

Research value: This is the cleanest SCRIPTA control for the Hugh-Basilia-Gerard triad already known via DG/FM G. It also strengthens Bosc-Hyons / Hugonis Silva as an early Gournay endowment locus.

## Act 1633 - Robert son of Erneys to Saint-Wandrille

URL: https://mrsh.unicaen.fr/scripta/doc/sc_1633.html

Date: [1049-1066].

Relevant Latin:

> Huic donationi interfuerunt testes : Odo Baiocensis episcopus et frater ejus Robertus comes Moretania, Hugo Gurnai, item Hugo Monfort.

English working extract: Hugh Gurnai appears as a witness with Odo bishop of Bayeux, Robert count of Mortain, and Hugh de Montfort.

Research value: Pre-Conquest/Conquest-era witness attestation for Hugh in a high-status Norman witness group.

## Act 1661 - William the Bastard for Bayeux / Bernieres

URL: https://mrsh.unicaen.fr/scripta/doc/sc_1661.html

Date: [1060-1066].

Relevant Latin:

> Guillelmus dux. Mathildis comitissa. Robertus filius Guillelmi ducis. Willelmus Ebrocensis episcopus. Rogerus de Monte Gomeri. Robertus comes de Moreton. Hugo de Gornai. Gerardus dapifer. Guillelmus de Curcella. Radulfus camerarius.

English working extract: Hugh de Gornai appears in the witness/subscription list with Duke William, Matilda, Robert son of William, William bishop of Evreux, Roger de Montgomery, Robert count of Mortain, Gerard the steward, William de Courcelles, and Ralph the chamberlain.

Research value: Another pre-1066 high-status attestation, useful for the G33 chronology.

## Act 6458 - William I confirmation to Saint-Etienne de Caen

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6458.html

Date: [1066-1077].

Relevant Latin:

> S(ignum) Rogeri de Bellomonte. S(ignum) Roberti de Bellomonte. S(ignum) Hugonis de Gorniaco. S(ignum) Walteri Gifardi.

English working extract: Hugh de Gorniaco subscribes with Roger and Robert de Beaumont and Walter Giffard.

Research value: Caen abbey attestation for Hugh in the Conqueror's circle.

## Act 6463 - William I for Saint-Etienne de Caen

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6463.html

Date: [1081-1082].

Relevant Latin:

> Signum comitis Hugonis. Signum Eudonis filii Huberti. Signum Radulfi de Todeneio. Signum Hugonis de Gorniaco. Signum Henrici de Ferreriis.

English working extract: Hugh de Gorniaco appears among the subscriptions with Earl Hugh, Eudo son of Hubert, Ralph de Tosny, and Henry de Ferrers.

## Act 6466 - Saint-Etienne de Caen acquisition notice

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6466.html

Date: [1080-1083].

Relevant Latin:

> Robertus comes de Moretonio, Hugo comes, Rogerius de Bello Monte, Robertus comes de Mellent, Willelmus de Bretuel, Hugo de Gorniaco, Hugo de Monte forti, Walterius Gifardus, Henricus de Ferrariis, Willelmus comes Ebroicensis.

English working extract: Hugh de Gorniaco appears in a high-status witness list among Mortain, Beaumont/Meulan, Breteuil, Montfort, Giffard, Ferrers, and Evreux names.

## Act 6467 - William I confirmation to Saint-Etienne de Caen

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6467.html

Date: [1081-1087].

Relevant Latin:

> S(ignum) Henrici de Bellomonte. S(ignum) Hugonis de Gorniaco. S(ignum) Walteri Gifardi. S(ignum) Ricardi Abrincensis vicecomitis.

English working extract: Hugh de Gorniaco subscribes with Henry de Beaumont, Walter Giffard, and Richard vicomte of Avranches.

## Act 6472 - William I / Matilda confirmation to La Trinite de Caen

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6472.html

Date: 1082.

Relevant Latin, version one:

> Signum Willelmi qui dicitur Caritas. Signum [Hugonis] de Gornayo. Signum Radulfi de Todenio. Signum Willelmi de Bretoil. Signum Girardi de Gornaio. Signum Willelmi camerarii filii Radulfi.

Relevant Latin, version two:

> Signum Willelmi de Bretuil. Signum Girardi de Gornaio. Signum Hugonis de Gornelio.

English working extract: SCRIPTA's two-version text places Hugh of Gournay and Gerard of Gournay in the La Trinite witness/subscription material. It does not plainly support the older "William de Gornai ... Girard de Gornai" reading used in some existing repo prose.

Research value: Corrects or at least destabilizes the prior brother-William inference. Keep William de Gournay as unresolved unless the edition behind the FMG/DG reading is checked directly.

## Act 6511 - William I confirmation / pancarte for Bec

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6511.html

Date: 1077.

Relevant Latin:

> Hugo de Bolbec, dimidiam moltam de Bosco Girardi. Hugo de Gornaco et filius eius Girardus, dominium suum in eadem villa, excepto bosco qui dicitur Ramerius et bosco sub domo Rodulfi.

English working extract: Hugh de Bolbec gave half the milling right of Bois Girard. Hugh de Gornaco and his son Gerard gave their domain in the same villa, except the wood called Ramerius and the wood below Rodulf's house.

Research value: Direct father-son proof for Hugh -> Gerard in a Bec donation context, and a stronger Bec-side control for the Bois Girard/Bosc-Girard endowment than the later summaries alone.

## Act 6512 - William I confirmation of Bec's English holdings

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6512.html

Date: [1081-1087].

Relevant Latin:

> Concedo etiam ipsi coenobio quod illi Hugo de Gornaco dedit, scilicet in London' quod ibi habebat de me ; et in Essex' ecclesiam de Fordham cum terra ecclesie, et totam decimam, et unum villanum ; in Erleiga scilicet decimam, et unum villanum ; in Liston' decimam de dimidia villa, et dimidiam ecclesiam, et unum villanum.

English working extract: William confirms to Bec what Hugh de Gornaco gave: in London whatever Hugh held there of the king; in Essex, the church of Fordham with church land, all tithe, and one villanus; at Ardleigh, the tithe and one villanus; and at Liston, the tithe of half the vill, half the church, and one villanus.

Research value: Adds a London holding/revenue item to Hugh's known Bec gifts. Existing repo summaries carry Fordham/Liston/Ardleigh; the London clause should be surfaced in G33 and the City of London place file.

## Act 6520 - Lessay foundation notice

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6520.html

Date: 1080-07-14.

Relevant Latin:

> signum Hugonis de Gornay. signum Roberti de Molbraio. signum Rogerii comitis de Montgomeri.

English working extract: Hugh de Gornay appears as a subscriber to the Lessay foundation notice.

## Act 6523 - Marmoutier / Guernsey donation confirmation

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6523.html

Date: [1073-1077].

Relevant Latin:

> Hugo episcopus de Luxovio. Hugo de Gurniaco. Ricardus de Curci. Rodulfus filius Herluini. Willelmus filius Hastenchi. Rotgerius, senescalcus episcopi Baiocacensis.

English working extract: Hugh de Gurniaco appears as a witness in the Marmoutier / Guernsey donation confirmation group.

## Act 6538 - Montivilliers / Cauville sale

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6538.html

Date: [1068-1076].

Relevant Latin:

> Emit eadem abbatissa Calvelvillam centum libras a Normanno de La Berliere, concedente Hugone de la Ferteit, et Hugone de Gornay, et Warnerio suo consanguineo, sub testimonio Guillelmi comitis de Archis, et Hugonis Luxoviensis episcopi.

English working extract: The abbess bought Cauville for 100 pounds from Normand de La Belliere, with Hugh de la Ferte, Hugh de Gournay, and Warnerius his kinsman consenting; the witnesses included William count of Arques and Hugh bishop of Lisieux.

Research value: Modern SCRIPTA control for the Cauville/Montivilliers act printed by Daniel Gurney. The antecedent of "his kinsman" should not be overclaimed. Cassandra Potts uses this sale as an example of a transaction later recast as ducal gift and points to Bouvris 1988 for the Montivilliers revival context.

## Act 6565 - Saint-Benoit-sur-Loire confirmation

URL: https://mrsh.unicaen.fr/scripta/doc/sc_6565.html

Date: 1067-04.

Relevant Latin:

> S(ignum) Hugonis de Gornaio. S(ignum) Giraldi de Novo Mercato. S(ignum) Stigandi dapiferi. S(ignum) Henrici de Ferreris.

English working extract: Hugh de Gornaio subscribes William's April 1067 confirmation for Saint-Benoit-sur-Loire at Le Vaudreuil.

Research value: Earliest precisely dated post-Conquest SCRIPTA attestation in this selected roster.
```

## New validation files

Create `sources/validations/unicaen-scripta-selected-gournay-acts.md`.

```markdown
# Validation - SCRIPTA selected Gournay acts

Source ID: `unicaen-scripta-selected-gournay-acts`

## Access

- SCRIPTA base: https://mrsh.unicaen.fr/scripta/
- Act URLs captured in `sources/corpus_supplement/unicaen-scripta-selected-gournay-acts.md`.
- Entry path began from the Normonde authority file for Hugues Ier de Gournay and the linked SCRIPTA act roster.

## Scope

This is a partial selected corpus, not a complete SCRIPTA harvest. It captures only Gournay-relevant act extracts found in this pass:

151, 1633, 1661, 6458, 6463, 6466, 6467, 6472, 6511, 6512, 6520, 6523, 6538, 6565.

## Main findings

- Act 151 directly names Hugh, Basilia, and Gerard in the Jumieges / Hugonis Silva donation.
- Act 6511 directly names Hugh de Gornaco and his son Gerard as Bec donors in the Bois Girard context.
- Act 6512 adds the London clause to Hugh's Bec gifts: whatever Hugh held of the king in London, plus Fordham, Ardleigh, and Liston rights.
- Act 6472 requires caution: SCRIPTA's modern text reads Hugh and Gerard forms in the Gournay witness slots, not the older "William de Gornai" reading currently reflected in places in the repo.
- Act 6538 is the modern SCRIPTA control for the Montivilliers/Cauville sale printed by Daniel Gurney.

## Use notes

Use SCRIPTA for act-level control and variant forms. Continue to cite Daniel Gurney where the repo is discussing DG's own extract, but add SCRIPTA where the modern act record materially improves the reading, dating, or source context.
```

Create `sources/validations/rye-index-rerum-norfolk-antiquities-1910.md`.

```markdown
# Validation - Rye Index Rerum to Norfolk Antiquities

Source ID: `rye-index-rerum-norfolk-antiquities-1910`

## Access

- PDF: https://upload.wikimedia.org/wikipedia/commons/9/9c/An_index_rerum_to_Norfolk_antiquities_%28IA_indexrerumtonorf00ryewrich%29.pdf

## Findings

- The index has an entry "Apocryphal Book of Dan. See sub Gurney in Index to Pedigrees."
- The Gurney pedigree entry lists Daniel Gurney's `Record of the House of Gournay` and gives the alternate informal title "otherwise known as the Apocryphal Book of Dan."
- The same source list surfaces pedigree/arms manuscript leads: Harl. MS 1552 p.48; Harl. MS 4755 fo.81; and the MSS of John H. Gurney of Keswick cited via the 12th Report of the Historical Manuscripts Commission, p.116.

## Use notes

Treat this as a reception/source-map source, not as independent genealogical proof. Its value is in recording the nickname and surfacing manuscript/source leads for the Norfolk pedigree apparatus.
```

Create `sources/validations/sanhs-excursions-1907-apocryphal-book-dan.md`.

```markdown
# Validation - SANHS excursion note on "Apocryphal Book of Dan"

Source ID: `sanhs-excursions-1907-apocryphal-book-dan`

## Access

- PDF: https://sanhs.org/wp-content/uploads/2020/08/02Excursions.pdf

## Finding

The excursion report says Daniel Gurney, under the mistaken idea that a house was Sir Matthew Gournay's residence, illustrated his large Gournay work with views of that house. It then says the book was generally known among his friends as the "Apocryphal Book of Dan" and cites `Bibliographer, I, 59`.

## Use notes

This is the strongest source found for the social meaning of the nickname: an informal or friendly joke-name among Daniel Gurney's circle. It does not indicate a separate edition, variant printing, or missing version of the `Record`.
```

Create `sources/validations/potts-monastic-revival-regional-identity-1997.md`.

```markdown
# Validation - Potts 1997, Montivilliers / Cauville

Source ID: `potts-monastic-revival-regional-identity-1997`

## Access

Published monograph; online snippet/search text consulted during the SCRIPTA Act 6538 pass. No local full corpus captured in this patchset.

## Finding

Potts, pp. 42-43, uses the Cauville / Montivilliers sale as an example of a sale later remembered or recast as a ducal gift. The note points to Jean-Michel Bouvris, "La renaissance de l'abbaye de Montivilliers autour de l'an mil," in `L'abbaye de Montivilliers a travers les ages` (Montivilliers, 1988), pp. 67-84.

## Use notes

Use Potts as modern scholarly context for SCRIPTA Act 6538 and Daniel Gurney Part I Appendix III. Do not cite Bouvris for a fact until the 1988 article has been obtained.
```

## Research-file updates

### G33 research companion

File: `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`

1. In section `5.2 1076 Bec charter - pre-Domesday tithe grant`, after the current DG-Supp quotation paragraph and before `Augerius / Ausger de Gournay`, add:

```markdown
SCRIPTA now gives two Bec-side controls that sharpen this section. First, the 1077 Bec pancarte names the father-son pair directly: Hugh de Gornaco and his son Gerard gave their domain in the same villa as Hugh de Bolbec's half milling right of Bois Girard, excepting the wood called Ramerius and the wood below Rodulf's house. The "same villa" wording makes Bois Girard / Bosc-Girard the contextual place, but the exact modern identification remains a place-file question.[^scripta-bec-6511]

Second, William I's [1081-1087] confirmation of Bec's English holdings gives the fuller English-side wording: the king confirmed to Bec what Hugh de Gornaco had given, including "in London' quod ibi habebat de me" - whatever Hugh held there of the king - and, in Essex, Fordham's church and church land with all tithe and one villanus, Ardleigh's tithe and one villanus, and Liston's half-vill tithe, half church, and one villanus. The London clause is not visible in the current DG-Supp summary and should be treated as a new English-side holding/revenue lead for Hugh.[^scripta-bec-6512]
```

2. In section `6.2 1077 + 1082 - Caen foundation charters`, replace the 1082 bullet:

```markdown
- **1082**: Foundation of La Trinite (the Abbaye-aux-Dames) at Caen - by William and Queen Matilda. Hugh III among the witnesses, alongside his brother William de Gornai and his son Gerard. Both abbey-churches survive in Caen.
```

with:

```markdown
- **1082**: Foundation of La Trinite (the Abbaye-aux-Dames) at Caen - by William and Queen Matilda. Hugh III and Gerard appear among the Gournay witnesses in SCRIPTA's two-version text. This is a useful check against the older FMG/DG-derived "William de Gornai" reading: SCRIPTA's modern transcription has `[Hugonis] de Gornayo` / `Hugonis de Gornelio` plus `Girardi de Gornaio`, not a separate William de Gornai in the Gournay witness slot. The brother-William point should be held as unresolved unless the underlying edition behind the older reading is rechecked.[^scripta-caen-6472]
```

3. In the children table, replace the Guillaume row:

```markdown
| Guillaume de Gournay | after 1082 | Basilea Flaitel | **Bracketed in FMG; corroborated by 1082 Caen witness** | "[William] de Gornai" co-witnessed the 1082 Trinite de Caen charter alongside "Girard de Gornai" - likely Gerard's brother. |
```

with:

```markdown
| Guillaume de Gournay | after 1082? | Basilea Flaitel? | **Bracketed in FMG; now needs recheck** | Older DG/FMG-derived summaries read a 1082 La Trinite witness as "[William] de Gornai" alongside Gerard, but SCRIPTA Act 6472 reads the Gournay witness pair as Hugh + Gerard. Keep Guillaume bracketed and unresolved pending direct check of the edition behind the older reading. |
```

4. Add footnotes near the existing G33 footnotes:

```markdown
[^scripta-bec-6511]: SCRIPTA Act 6511, William I confirmation/pancarte for Bec, 1077: Hugh de Gornaco and his son Gerard give their domain in the same villa as the Bois Girard milling-right clause. Source ID: `unicaen-scripta-selected-gournay-acts`.
[^scripta-bec-6512]: SCRIPTA Act 6512, William I confirmation of Bec's English holdings, [1081-1087], confirming Hugh de Gornaco's London holding from the king plus Fordham, Ardleigh, and Liston rights. Source ID: `unicaen-scripta-selected-gournay-acts`.
[^scripta-caen-6472]: SCRIPTA Act 6472, William I / Matilda confirmation to La Trinite de Caen, 1082; two-version text gives Hugh/Gerard Gournay forms rather than a clean William/Gerard pair. Source ID: `unicaen-scripta-selected-gournay-acts`.
```

5. Add a source-table row:

```markdown
| SCRIPTA selected Gournay acts, Acts 151, 6472, 6511, 6512, 6538, 6565 and related roster acts | `unicaen-scripta-selected-gournay-acts` |
```

### G32 research companion

File: `research/people/g32-gerard-de-gournay-fact-sheet.research.md`

1. Replace section `2.1 1082 - la Trinite de Caen foundation charter` with:

```markdown
### 2.1 1082 - la Trinite de Caen foundation charter

SCRIPTA Act 6472 gives the La Trinite witness forms as `[Hugonis] de Gornayo` / `Hugonis de Gornelio` and `Girardi de Gornaio` in its two-version text.[^scripta-caen-6472-g32]

This matters because the older FMG/DG tradition has been read in the repo as "William de Gornai ... Girard de Gornai." The modern SCRIPTA transcription does not show that William form in the Gournay witness slot; it supports Hugh + Gerard in the witness list and makes the brother-William inference unresolved pending a check of FMG's edition basis.
```

2. After section `2.2 Undated Jumieges charter - Radulphus Havoth's entry`, add:

```markdown
### 2.2.1 1077 Bec pancarte - Hugh and Gerard as father-son donors

SCRIPTA Act 6511 gives a separate Bec-side father-son attestation: after Hugh de Bolbec's half milling right of Bois Girard, the act says Hugh de Gornaco and his son Gerard gave their domain in the same villa, except the wood called Ramerius and the wood below Rodulf's house.[^scripta-bec-6511-g32]

This is important because it is not only a later royal recitation of earlier gifts. It directly names Hugh and Gerard in a donor clause and places Gerard inside the Bec patronage sequence before his later independent Lessingham and Bec-family role.
```

3. In section `2.10 [1181/89] - Henry II's Bec confirmation charter`, add after the current FMG quote:

```markdown
Delisle and Berger's Tome II edition now supplies the critical-edition control for this confirmation: act DCCXLIV, Delisle no. 552, dated 1181-1189 at Montfort. The relevant Bec clauses preserve the same chain and add the Hugues IV Ecouche clause already extracted in section 2.10.1. Use the Delisle source ID for the primary text and FMG only as the finding path / prosopographical index.[^delisle-bec-dccxliv-g32]
```

4. Add footnotes:

```markdown
[^scripta-caen-6472-g32]: SCRIPTA Act 6472, William I / Matilda confirmation to La Trinite de Caen, 1082. Source ID: `unicaen-scripta-selected-gournay-acts`.
[^scripta-bec-6511-g32]: SCRIPTA Act 6511, William I confirmation/pancarte for Bec, 1077. Source ID: `unicaen-scripta-selected-gournay-acts`.
[^delisle-bec-dccxliv-g32]: Leopold Delisle and Elie Berger, eds., `Recueil des actes de Henri II`, vol. 2, act DCCXLIV / Delisle no. 552, pp. 375-379. Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
```

5. Add source-table row:

```markdown
| SCRIPTA selected Gournay acts, especially Acts 6472 and 6511 | `unicaen-scripta-selected-gournay-acts` |
```

### Bec endowment cluster place file

File: `research/places/g33-bec-gournay-endowment-cluster.md`

Replace the Henry II bullet and footnote emphasis:

```markdown
- **[1181/89] - Henry II's royal confirmation** later restated the same chain at a royal level. Delisle and Berger's Tome II edition (act DCCXLIV / Delisle no. 552) gives the critical text: the Bec holdings include gifts from the first Hugh de Gornaco and Gerard his son, from Gerard de Gornaio and Basilia his mother, and from Hugues IV at Ecouche. This raises the Henry II confirmation from an FMG-only pointer to a primary-text-controlled source in the repo.[^delisle-henry-ii-bec]
```

Add after the two bullets:

```markdown
SCRIPTA adds an earlier 1077 Bec pancarte control: Hugh de Gornaco and his son Gerard gave their domain in the same villa as Hugh de Bolbec's Bois Girard milling-right clause, excepting two woods. This places the Hugh-Gerard donor pair directly in the Bec endowment record rather than only in later confirmations.[^scripta-bec-6511-place]
```

Replace footnote `[^fmg-henry-ii-bec]` with:

```markdown
[^delisle-henry-ii-bec]: Leopold Delisle and Elie Berger, eds., `Recueil des actes de Henri II`, vol. 2, act DCCXLIV / Delisle no. 552, pp. 375-379; source ID `recueil-actes-henri-ii-delisle-berger-vol-2`. FMG MedLands [885] remains the prosopographical finding path; source ID `fmg-medlands-normacre`.
[^scripta-bec-6511-place]: SCRIPTA Act 6511, William I Bec confirmation/pancarte, 1077. Source ID: `unicaen-scripta-selected-gournay-acts`.
```

### Le Bec-Hellouin place file

File: `research/places/le-bec-hellouin.md`

Replace:

```markdown
In 1076, Hugh III gave the tithes of his three Essex parishes (Fordham, Liston, Ardleigh) to Bec, establishing an ongoing English revenue stream for the abbey. Gerard (G32) continued the family's connection to Bec by founding Lessingham Priory in Norfolk as a daughter house.
```

with:

```markdown
In 1076/[1081-1087], Hugh III gave Bec an English revenue package: whatever he held of the king in London, plus Fordham's church and tithes, Ardleigh's tithe, and Liston's half-vill tithe and half church. Gerard (G32) continued the family's connection to Bec by founding Lessingham Priory in Norfolk as a daughter house.[^scripta-bec-english-le-bec]
```

Add footnote:

```markdown
[^scripta-bec-english-le-bec]: SCRIPTA Act 6512, William I confirmation of Bec's English holdings, [1081-1087]. Source ID: `unicaen-scripta-selected-gournay-acts`.
```

### City of London place file

File: `research/places/city-of-london.md`

Add a new opening section before `### St Augustine Watling Street and Old Change - Robert and John Gurney`:

```markdown
### Hugh de Gournay III - Domesday-era London holding

SCRIPTA Act 6512, William I's [1081-1087] confirmation of Bec's English holdings, says the king confirmed to Bec what Hugh de Gornaco had given, including "in London' quod ibi habebat de me" - whatever Hugh held there of the king - before listing the Essex church/tithe rights at Fordham, Ardleigh, and Liston. The clause does not identify the London site, but it gives the repo its earliest known Gurney/Gournay London holding or revenue reference, more than five centuries before the early-modern St Augustine / Old Change cluster.[^scripta-bec-london-place]
```

Add footnote:

```markdown
[^scripta-bec-london-place]: SCRIPTA Act 6512, William I confirmation of Bec's English holdings, [1081-1087]. Source ID: `unicaen-scripta-selected-gournay-acts`.
```

## Daniel Gurney reception update

File: `research/topics/dg-reception-delisle-critique.md`

Add a new subsection after `## 1. DG's project and its evidentiary base`:

```markdown
### 1.1 Informal nickname: "The Apocryphal Book of Dan"

A new reception lead explains the alternative title found in Norfolk source lists. Walter Rye's `Index Rerum to Norfolk Antiquities` indexes "Apocryphal Book of Dan" to the Gurney pedigree entry, and the Gurney entry glosses Daniel Gurney's `Record of the House of Gournay` as "otherwise known as the Apocryphal Book of Dan."[^rye-index-apocryphal-dan]

The stronger social-context note comes from the Somerset Archaeological and Natural History Society excursion report. In a footnote on Daniel Gurney's mistaken identification of a house as Sir Matthew Gournay's residence, the report says the book was generally known among his friends as the "Apocryphal Book of Dan," citing `The Bibliographer`, I, 59.[^sanhs-apocryphal-dan]

Treat this as an informal or joke-name among family/friends and antiquarian readers, not as evidence for a separate edition, missing version, or variant text of Daniel Gurney's work. It does, however, nicely reflects the mixed reception captured elsewhere in this topic file: Daniel Gurney's work was foundational, ambitious, and beloved inside the family circle, while its early legendary strata were already treated with affectionate skepticism.
```

Add footnotes:

```markdown
[^rye-index-apocryphal-dan]: Walter Rye, `An Index Rerum to Norfolk Antiquities` (Norwich, 1910), entries "Apocryphal Book of Dan" and "Gurney" in the Index to Pedigrees. Source ID: `rye-index-rerum-norfolk-antiquities-1910`.
[^sanhs-apocryphal-dan]: Somerset Archaeological and Natural History Society excursion report PDF, footnote citing `The Bibliographer`, I, 59, for the note that Daniel Gurney's book was generally known among his friends as the "Apocryphal Book of Dan." Source ID: `sanhs-excursions-1907-apocryphal-book-dan`.
```

Add source-table rows:

```markdown
| Rye, `Index Rerum to Norfolk Antiquities` (1910), "Apocryphal Book of Dan" / Gurney entries | `rye-index-rerum-norfolk-antiquities-1910` |
| SANHS excursion report note on "Apocryphal Book of Dan" | `sanhs-excursions-1907-apocryphal-book-dan` |
```

## Arms / pedigree topic update

File: `research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md`

Add after the `### Rye / Harleian Society Norfolk Visitations` section:

```markdown
### Index Rerum / Norfolk Pedigrees source-map leads

The newly surfaced `Index Rerum to Norfolk Antiquities` and `Index to Norfolk Pedigrees` source-list material should be treated as a map of manuscript pedigree witnesses, not as genealogical evidence in itself. It adds several arms/pedigree leads that sit beside Rye and Dashwood:

| Source-list item | Why it matters | Current status |
|---|---|---|
| Harl. MS 1552 p. 48, printed Harleian Society p. 132 | This is the Rye printed visitations source already used for the cadet / differentiated-arms Gurney heading. | Covered by `rye-visitacion-norffolk-1891`. |
| Visitation of 1563 by Harvey, Harl. MS 4755, fo. 81 | Likely a manuscript control or variant of the Harvey 1563 visitation separate from the printed Dashwood page already used for Kerville. | New lead. |
| MSS of the late John H. Gurney of Keswick, 12th Report of the Historical Manuscripts Commission, p. 116 | Potential family-paper or Keswick-glass source path, important because DG says Gurney's Place glass was preserved at Keswick. | New lead. |
| Norris' MS folio pedigrees, pp. 553-556; Morant's MS folio pedigrees, p. 175 | Manuscript pedigree controls that may preserve variant Gurney arms/matches outside Rye. | New lead. |
| Commonplace Book of Henry G., Tanner MSS, Bodleian Library, fo. 175 | Likely the same source-family as the existing Tanner 175/Henry Gurney lead; update that lead rather than duplicate it. | Existing lead refined. |
| Dawson Turner's illustrated Blomefield, vol. xv, fo. 182 | Could preserve visual/pedigree material absent from printed Blomefield. | New lead. |
| Ashmole MS 848, fo. 5, and Ashmole MS 792, vol. ii | Bodleian manuscript heraldic/pedigree leads. | New lead. |
| King's College, Oxford, lxxix / clxvii, p. 21 | College manuscript pedigree lead needing catalogue identification. | New lead. |

The value here is in triangulation. If any of these manuscript witnesses independently reproduce the Walsingham / West Barsham / Berryhall quarterings, they can either confirm DG's source chain or expose where a later reconstruction entered the tradition. Until inspected, they should stay in the leads CSV rather than in the evidence register.
```

Add source footnote rows near the existing Rye notes:

```markdown
[^rye-index-pedigree-leads]: Walter Rye, `An Index Rerum to Norfolk Antiquities` (Norwich, 1910), Gurney entry in Index to Pedigrees; source ID `rye-index-rerum-norfolk-antiquities-1910`.
```

## Future-research leads CSV

File: `research/future-research/research-leads.csv`

1. Replace L-25:

```csv
L-25,50,G15,"Henry Gurney","Bodleian MS Tanner 175 / Commonplace Book of Henry G., fo.175; Walter Rye, Church Heraldry of Norfolk","Heraldic and manuscript corroboration for the Great Ellingham / West Barsham Henry; the new Norfolk Pedigrees index wording identifies this as the Commonplace Book of Henry G. in Tanner MSS, fo.175. Rye is on archive.org.",Unk,Open,research/people/g15-henry-gurney-fact-sheet.research.md
```

2. Append rows after L-83:

```csv
L-84,52,Heraldic,"Norfolk Gurney pedigree / arms","Visitation of 1563 by Harvey, Harl. MS 4755, fo.81","Manuscript-control lead surfaced by Rye Index Rerum / Norfolk pedigree source list; may preserve a Harvey 1563 Gurney pedigree or arms variant separate from the printed Rye/Dashwood texts.",Unk,Open,research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md
L-85,50,Heraldic,"Keswick Gurney MSS / glass","MSS of the late John H. Gurney of Keswick, 12th Report of the Historical Manuscripts Commission, p.116","Potential family-paper and Keswick-glass source path; especially relevant because Daniel Gurney says Gurney's Place bay-window arms were preserved at Keswick.",Unk,Open,research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md
L-86,46,Heraldic,"Norfolk Gurney manuscript pedigrees","Norris' MS folio pedigrees pp.553-556 and Morant's MS folio pedigrees p.175","Manuscript pedigree controls surfaced in the Norfolk Pedigrees index; may preserve Gurney quarterings or variant descent statements outside Rye's printed visitations.",Unk,Open,research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md
L-87,44,Heraldic,"Dawson Turner illustrated Blomefield","Dawson Turner's illustrated Blomefield, vol. xv, fo.182","Potential visual/pedigree witness absent from printed Blomefield; compare against Walsingham, West Barsham, and Berryhall arms if reachable.",Unk,Open,research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md
L-88,44,Heraldic,"Bodleian Ashmole Gurney pedigree/arms leads","Ashmole MS 848, fo.5, and Ashmole MS 792, vol. ii","Bodleian manuscript leads from the Norfolk Pedigrees index; likely heraldic or pedigree content needing catalogue and image access check.",Unk,Open,research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md
L-89,40,Heraldic,"King's College Oxford Gurney pedigree lead","King's College, Oxford, lxxix / clxvii, p.21","College manuscript pedigree lead from Norfolk Pedigrees index; first task is to identify the catalogue item behind lxxix/clxvii and whether images or transcripts exist.",Unk,Open,research/topics/gurney-armorial-pedigree-and-visitations-evidence-audit.md
L-90,42,G33,"Montivilliers / Cauville sale context","Jean-Michel Bouvris, 'La renaissance de l'abbaye de Montivilliers autour de l'an mil,' in L'abbaye de Montivilliers a travers les ages (1988), pp.67-84","Potts cites Bouvris for the Montivilliers revival context behind the Cauville sale in SCRIPTA Act 6538; obtain before using the sale's later-memory / ducal-gift interpretation beyond Potts.",Unk,Open,research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md
L-91,45,G32/G33,"1082 La Trinite witness reading","Edition basis behind FMG/DG 'William de Gornai ... Girard de Gornai' versus SCRIPTA Act 6472 Hugh/Gerard reading","Resolve whether the older William de Gornai brother inference is an edition difference, misreading, or separate witness version; affects G33 children table and G32 chronology note.",Unk,Open,research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md
```

## Notes on directness and confidence

- The SCRIPTA 6511 and 6512 findings are strong enough for G33/G32 research companions and Bec/London place notes.
- The SCRIPTA 6472 finding should be framed as a correction/caution, not as proof that Guillaume did not exist.
- The "Apocryphal Book of Dan" finding belongs in reception/source history, not in the fact sheets.
- The Norfolk pedigree/arms manuscript list belongs in the arms topic and leads CSV until the actual manuscript witnesses are inspected.

