# v14 Norman geo research-contribution patchset

## Application instruction

Apply this patchset as a Phase 2 research promotion from the Norman geographic-overlay source review. Do not redo the source search unless a cited URL has materially changed or is unavailable. Keep the existing v13 bundle source entries; they remain useful for comprehensive overlay source tracking. Where this patchset promotes a bundled source into an ancestor research companion, use the individual source IDs added in `data/sources.json`.

The highest-value work is ancestor companion promotion. Place-file promotion is included where it preserves source detail without creating thin or over-precise place records.

## Source records already added for this promotion

These individual records now exist in `data/sources.json`:

- `projet-conde-conquets-hue-gournay`
- `ferrieres-en-bray-official-history`
- `gancourt-saint-etienne-bulletin-2023`
- `gaillefontaine-official-history`
- `bauduin-franchises-normandie-orientale-2001`
- `openedition-abbayes-seigneurs-normands-annexe`

Retain the existing bundle records too:

- `norman-geo-controlling-sources-2026`
- `norman-geo-archives76-commune-dossiers-2026`
- `norman-geo-local-history-tourism-2026`
- `norman-geo-institutional-localities-2026`
- `norman-geo-locator-saint-quentin-hericourt-2026`
- `norman-geo-locator-criquiers-torchy-2026`
- `norman-geo-locator-southern-boundary-2026`

## 1. Promote to `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`

Outcome: promote.

Reason: ConDE, Ferrieres, and Gancourt give ancestor-level support for the Beauvaisis / Conquets Hue de Gournay block already assigned in the repo to Hugh de Gournay III. These sources do not prove the original conquest event by themselves, but they substantially strengthen the legal-memory and local-history detail around the block.

Exact operation: after the existing section `### 5.5 Additional Norman holdings`, add:

```md
### 5.6 ConDE, Ferrieres, and Gancourt witnesses for the Beauvaisis block

The later legal-memory sources make the Beauvaisis acquisition more concrete than a bare "twenty-four villages" label. Projet ConDE preserves the local-custom heading for the twenty-four parishes, hamlets, and villages under the jurisdiction of Gournay beyond the Epte, called the "Conquets Hue de Gournay" and held through the châtellenie and high justice of Gournay.[^conde-conquets-g33] The list in that heading is valuable because it treats the block as a customary-law geography: Ferriere with Laudencourt la Forest, Hardencourt, and Anchy in part; Monthois with Iencourt; Saint-Quentin and Beaulevrier / Hincourt; Hericourt with Beaumont and la Haus-saye; Saint-Sanson sous le Rain; Doudeauville; Royay; Loyenses; Songeons; Raincourt; Torchy; Sullys; Moullonguies; Humermont; and Boymont in the terroir of Ganicourt.[^conde-conquets-g33]

Modern local witnesses reinforce several of the list's western and south-western anchors. The Ferrieres-en-Bray municipal history places Ferrieres and the adjacent parishes Le Foret, Hardencourt, and Laudencourt in the conquests of Hugues de Gournay and says they were administered by a seneschal.[^ferrieres-conquets-g33] The same page also preserves a later Bellozanne connection: Adam de Ferrieres, owner of the twelfth-century seigneurial manor at Le Manais, is described as vassal of Hugues V de Gournay and a subscriber to the foundation charter of Bellozanne.[^ferrieres-conquets-g33] Gancourt-Saint-Etienne's 2023 municipal bulletin places Gancourt among the twenty-four conquests of Hugues de Gournay, notes the form Ganicourt in the Norman custom tradition, and says the pre-Revolution commune belonged to the left-bank Epte parishes known as the Conquets Hue de Gournay and depended on the high justice of Gournay.[^gancourt-conquets-g33]

These are not independent proof that Hugh III personally seized every component locality; they are best used with Decorde, Planché, and the existing place file. Their contribution is tighter: they show that the acquisition block survived in legal, seigneurial, and local-place memory as a jurisdictional geography attached to Gournay, not merely as a nineteenth-century genealogical flourish.
```

Exact footnotes to add near the file's existing footnotes or at end:

```md
[^conde-conquets-g33]: Projet ConDE, Universite de Caen Normandie, "Coutumes et usages locaux des vingt quatre Paroisses, Hameaux & Villages... Conquets Hue de Gournay," digital Norman custom-law passage, https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html. Source ID: `projet-conde-conquets-hue-gournay`.
[^ferrieres-conquets-g33]: Commune de Ferrieres-en-Bray, "Histoire de la ville," municipal history page, especially "Les origines" and "Les Seigneuries de Ferrieres," https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville. Source ID: `ferrieres-en-bray-official-history`.
[^gancourt-conquets-g33]: Commune de Gancourt-Saint-Etienne, Bulletin municipal 2023, "Un peu d'historique de Gancourt-Saint-Etienne," p. 9 in the PDF extraction, source credited to research by Marjorie Thurin, https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf. Source ID: `gancourt-saint-etienne-bulletin-2023`.
```

## 2. Promote to `research/people/g36-hugh-de-gournay-i-fact-sheet.research.md`

Outcome: promote with caveat.

Reason: the Gaillefontaine official history is useful precisely because it complicates the earlier broad "Hugh I coordinated the triad" language. It ties Gaillefontaine to Gournay and La Ferte, but places the probable fortress-builder in the La Ferte cadet sequence. That should sharpen, not weaken, the G36 treatment.

Exact operation: in section `### 2.4 NRP-I 1852 + Painchault 2012 - the wider fortification triad`, after the existing Painchault paragraph and before `---`, add:

```md
The Gaillefontaine municipal history should be used as a local-history refinement rather than as proof that G36 himself built Gaillefontaine. It says Gaillefontaine's history is tied to Gournay and La Ferte, then gives a cadet-line sequence: Eudes de Gournay receives the Pays de Bray, Renaud marries Alberede, Gautier receives La Ferte and Gaillefontaine, Turold succeeds him, and Turold's son Hugues I probably has the Gaillefontaine fortress built around 1050.[^gaillefontaine-official-g36] That means the official page supports the family frontier system, the Gournay-La Ferte-Gaillefontaine relationship, the motte, the triple enceinte, and the 1050 horizon, but it should not be cited as a direct attestation that Hugh de Gournay I personally built Gaillefontaine.[^gaillefontaine-official-g36]
```

Exact footnote:

```md
[^gaillefontaine-official-g36]: Commune de Gaillefontaine, "Histoire de Gaillefontaine," "Haute epoque et Moyen Age," municipal history page, https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html. Source ID: `gaillefontaine-official-history`.
```

## 3. Promote to `research/people/g32-gerard-de-gournay-fact-sheet.research.md`

Outcome: promote.

Reason: Gaillefontaine official history gives physical and local-history texture to Orderic's `Goisleni Fontem` in the 1089/90 castle-delivery triad.

Exact operation: in section `### 2.3 [1089/90] - Orderic Vitalis: Gerard delivers three castles to William Rufus`, after the existing Painchault paragraph, add:

```md
The modern Gaillefontaine municipal history gives useful site texture for Orderic's `Goisleni Fontem`. It places the medieval fortress between the present chateau and the town, says the motte remains visible, describes a triple enceinte with very thick walls, and says the fortress commanded the surrounding countryside. Its later chronology also matches the "strategic frontier place" reading: in 1151 Henry II burned Gournay and La Ferte but did not take Gaillefontaine; in 1472 Charles the Bold dismantled and burned the fortress, ending Gaillefontaine's political power.[^gaillefontaine-official-g32]
```

Exact footnote:

```md
[^gaillefontaine-official-g32]: Commune de Gaillefontaine, "Histoire de Gaillefontaine," "Haute epoque et Moyen Age," municipal history page, https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html. Source ID: `gaillefontaine-official-history`.
```

## 4. Promote to `research/people/g35-renaud-de-gournay-fact-sheet.research.md`

Outcome: promote as corroborating context.

Reason: the OpenEdition abbey-foundation table is a compact independent control for Sigy as a Gournay / La Ferte ecclesiastical site. It should not replace Pettigrew, NRP, or charter-derived analysis, but it is useful in the Renaud / La Ferte cadet-line context.

Exact operation: after section `## 7. Argueil tithes (990 charter)` and before `## 8. La Ferte reverts to senior Gournay line`, add:

```md
## 7A. OpenEdition abbey table as a control for Sigy and later Gournay foundations

An OpenEdition appendix of abbeys founded by Norman lords independently places Saint-Martin and Saint-Vulgain de Sigy in 1040 with Hugues de Gournay as founder.[^openedition-abbayes-g35] This is not as detailed as Pettigrew or the NRP / la Ferte charter tradition, and it compresses the Hugues name without resolving the Gournay-versus-La-Ferte numbering problem. Its value is as a compact external control: Sigy was remembered in a wider Norman monastic-foundation table as a Gournay foundation, and it belongs in the same La Ferte cadet-line research environment as Renaud, Alberade, Gautier, and the later reversion of La Ferte to the senior line.[^openedition-abbayes-g35]

The same table lists Saint-Laurent de Beaubec, dated 1127, under Hugues II de Gournay, and Notre-Dame de Bellozanne, dated 1198, under Hugues V de Gournay.[^openedition-abbayes-g35] Those later entries should not be back-projected into Renaud's generation, but they are useful as a reminder that the Gournay family continued to use monastic foundation and patronage as a seigneurial strategy in the same Pays de Bray / eastern Norman world.
```

Exact footnote:

```md
[^openedition-abbayes-g35]: "Annexe I. Abbayes fondees par des seigneurs normands (XIe-mi XIIIe siecles)," in *De gre ou de force*, Presses universitaires de Rennes, OpenEdition Books, https://books.openedition.org/pur/49267. Source ID: `openedition-abbayes-seigneurs-normands-annexe`.
```

## 5. Promote to `research/places/beauvaisis-frontier-acquisitions.md`

Outcome: promote.

Reason: this is the canonical aggregate place file for the Conquets / twenty-four villages. Do not create twenty-four thin village files.

Exact operation A: under `## Legal / customary-law significance`, replace the two short existing paragraphs beginning `Projet ConDE preserves...` and `The same heading lists...` with:

```md
Projet ConDE preserves the heading of the local customs for the twenty-four parishes, hamlets, and villages under the jurisdiction of Gournay, seated beyond the river Epte, and called the Conquets Hue de Gournay and specialties of Beauvaisis. The heading also says the block was held through the Duke of Longueville because of the châtellenie and high justice of Gournay. This matters because the Conquets were remembered as a legal and jurisdictional territory, not merely as a family-history phrase.[^conde-conquets-place]

The same heading preserves the component list in a form that partly differs from Decorde's later normalized list. It gives Ferriere and its hamlets Laudencourt la Forest, Hardencourt, and Anchy in part; Monthois with Iencourt; Saint-Quentin and Beaulevrier / Hincourt; Hericourt with Beaumont and la Haus-saye; Saint-Sanson sous le Rain; Doudeauville; Royay; Loyenses; Songeons; Raincourt; Torchy; Sullys; Moullonguies; Humermont; and Boymont in the terroir of Ganicourt.[^conde-conquets-place] This supports the file's aggregate approach: preserve the territorial block first, then promote individual places only when identification and genealogical use justify it.
```

Exact operation B: after `## Map overlay note`, add:

```md
## Local witnesses from Ferrieres and Gancourt

Ferrieres-en-Bray is now more than a coordinate anchor. The municipal history says Ferrieres and the neighboring parishes Le Foret, Hardencourt, and Laudencourt belonged to the conquests of Hugues de Gournay and were administered by a seneschal.[^ferrieres-conquets-place] It also says Ferrieres' primitive eleventh-century church was within the jurisdiction of the lord of Gournay, while the parish remained in the diocese of Beauvais until the 1802 Concordat.[^ferrieres-conquets-place] That combination is useful: seigneurial jurisdiction, Beauvaisis ecclesiastical orientation, and local-place continuity all align with the Conquets model.

Gancourt-Saint-Etienne supplies the strongest local witness for the south-western / Boimont-Ganicourt edge. The 2023 municipal bulletin gives medieval forms including Gadonis Curtis, Guencort, Gaencuria, and Ganicourt, then places Gancourt among the twenty-four conquests of Hugues de Gournay.[^gancourt-conquets-place] It also says that before the Revolution, Gancourt belonged to the left-bank Epte parishes called the Conquets Hue de Gournay and depended on the high justice of Gournay.[^gancourt-conquets-place] This makes Gancourt a historically meaningful anchor for the ConDE `Boymont terroir de Ganicourt` clause, even if Boimont itself should remain a deferred identification.
```

Exact operation C: after the new Local witnesses section, add:

```md
## Cuy / Quesnoy connector outside the Conquets polygon

Cuy-Saint-Fiacre should stay outside the Conquets polygon unless stronger evidence places it inside the twenty-four-village list. Its value is different: it is a connector between the older Gournay core and the Beauvaisis edge. The Cuy-Saint-Fiacre history page says that in the middle of the twelfth century there was a full fief of haubert at Cuy, with its chief manor at the hamlet of Quesnoy, dependent on the châtellenie of Gournay.[^cuy-quesnoy-place] The Seine76 local-heritage page gives the same practical locality frame: the Manoir du Quesnoy at Cuy-Saint-Fiacre belonged to an important seigneurie depending on the châtellenie of Gournay.[^cuy-seine76-place]

Use this as châtellenie-dependency context, not as proof that Cuy or Quesnoy formed one of the Conquets Hue de Gournay.
```

Exact footnotes:

```md
[^conde-conquets-place]: Projet ConDE, Universite de Caen Normandie, "Coutumes et usages locaux des vingt quatre Paroisses, Hameaux & Villages... Conquets Hue de Gournay," https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html. Source ID: `projet-conde-conquets-hue-gournay`.
[^ferrieres-conquets-place]: Commune de Ferrieres-en-Bray, "Histoire de la ville," municipal history page, especially "Les origines," "Les Seigneuries de Ferrieres," and "L'eglise Saint Martin de Ferrieres," https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville. Source ID: `ferrieres-en-bray-official-history`.
[^gancourt-conquets-place]: Commune de Gancourt-Saint-Etienne, Bulletin municipal 2023, "Un peu d'historique de Gancourt-Saint-Etienne," p. 9 in the PDF extraction, source credited to research by Marjorie Thurin, https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf. Source ID: `gancourt-saint-etienne-bulletin-2023`.
[^cuy-quesnoy-place]: "Cuy-Saint-Fiacre," French Wikipedia, history section, https://fr.wikipedia.org/wiki/Cuy-Saint-Fiacre. Source ID: `norman-geo-local-history-tourism-2026`.
[^cuy-seine76-place]: Seine76, "Cuy-Saint-Fiacre," local heritage page, Manoir du Quesnoy entry, https://seine76.fr/communes/communes_result.php?var=CUY-SAINT-FIACRE. Source ID: `norman-geo-local-history-tourism-2026`.
```

## 6. Promote to `research/places/gaillefontaine.md`

Outcome: promote.

Reason: this place file currently uses POP / Merimee and Orderic. The Gaillefontaine official page adds local narrative: the Gournay / La Ferte relationship, cadet-line attribution, fortress position, visible motte, triple enceinte, 1151 and 1472 events.

Exact operation: after `## What remains from the medieval frontier site`, add:

```md
## Local-history detail from the commune

The Gaillefontaine municipal history ties the place explicitly to Gournay and La Ferte. It gives a local-tradition sequence in which Eudes de Gournay receives the Pays de Bray from Rollo; Renaud marries Alberede; Gautier receives La Ferte and Gaillefontaine; Turold succeeds; and Turold's son Hugues I probably has the Gaillefontaine fortress built around 1050.[^gaillefontaine-official-place] This should be treated as local-history tradition, not as a replacement for the stricter G36/G35/G32 ancestor companion analysis.

The page is still highly useful for site interpretation. It places the fortress between the modern chateau and the bourg, says the motte remains visible and wooded, describes a triple enceinte with walls of substantial thickness, and says the fortress commanded the surrounding countryside.[^gaillefontaine-official-place] It also gives a later political sequence: in 1151 the English king burned Gournay and La Ferte but failed to take Gaillefontaine; in 1204 Philip Augustus attached the fortress to the royal domain; and in 1472 Charles the Bold dismantled and burned the fortress, ending Gaillefontaine's political power.[^gaillefontaine-official-place]
```

Exact footnote:

```md
[^gaillefontaine-official-place]: Commune de Gaillefontaine, "Histoire de Gaillefontaine," "Haute epoque et Moyen Age," municipal history page, https://www.mairiegaillefontaine.fr/pages/decouvrir-et-bouger/histoire/historique.html. Source ID: `gaillefontaine-official-history`.
```

## 7. Promote to `research/places/sigy-normandy.md`

Outcome: promote.

Reason: OpenEdition gives compact external confirmation for Sigy in the Norman abbey-foundation table.

Exact operation: after the paragraph ending `it became a priory.`, add:

```md
An OpenEdition appendix of abbeys founded by Norman lords provides a useful outside control for this placement. It lists Saint-Martin and Saint-Vulgain de Sigy, dated 1040, with Hugues de Gournay as founder and Sigy-en-Bray as the locality.[^openedition-sigy-place] The entry is brief and does not solve the Hugues numbering issue, so it should be read alongside Pettigrew, NRP, and the La Ferte cadet-line material. Its value is corroborative: Sigy belongs with Gournay / La Ferte seigneurial ecclesiastical patronage, not merely with generic parish history.[^openedition-sigy-place]
```

Exact footnote:

```md
[^openedition-sigy-place]: "Annexe I. Abbayes fondees par des seigneurs normands (XIe-mi XIIIe siecles)," in *De gre ou de force*, Presses universitaires de Rennes, OpenEdition Books, https://books.openedition.org/pur/49267. Source ID: `openedition-abbayes-seigneurs-normands-annexe`.
```

## 8. Promote to `research/places/g33-bec-gournay-endowment-cluster.md`

Outcome: promote.

Reason: Archives 76 helps with Massy / Esclavelles / Morimont identity, and the Bellozanne / Brémontier / OpenEdition institutional sources help place the later abbey geography around the same Pays de Bray ecclesiastical network. These are place-file contributions, not ancestor proof.

Exact operation: after `## Candidate individual follow-ups`, add:

```md
## Morimont / Massy / Esclavelles identity support

Archives 76 gives a useful caution for the Morimont / Massy / Esclavelles endowment anchor. The Massy dossier preserves medieval forms for Massy and explicitly places Massy in the châtellerie of La Ferte-en-Bray in a 1390 reference; it also lists Bellozanne as a hamlet of Massy and Esclavelles, now in Massy.[^archives76-massy-esclavelles] The Esclavelles dossier shows why a single modern-place identification is hazardous: Clos-de-l'Essart is an Esclavelles locality at the hamlet of Morimont; Fontaine Hornoys is at Morimont, now Mont-Remond, at Esclavelles or Montrimont at Massy; and Mont-Remond / Montrimont is a hamlet, lieu-dit, and fief in both Esclavelles and Massy.[^archives76-massy-esclavelles]

Use this to keep Morimont as a cross-commune Massy / Esclavelles candidate until the exact medieval endowment language is pinned to a stronger charter or cartulary source. Do not collapse the Bec / Gournay endowment cluster into one modern Massy point.

## Bellozanne and Brémontier-Merval institutional context

The Brémontier-Merval official history places Bellozanne at the local level: it treats Bellozanne as a place-name tied to an abbey site and says that at the end of the twelfth century Hugues V, lord of Gournay, founded the abbey and entrusted it to the Premonstratensians.[^bremontier-bellozanne-place] The same page says that in the eighteenth century the abbey administered the parishes of Bellozanne, Brémontier, Merval, and Elbeuf-en-Bray.[^bremontier-bellozanne-place]

Jean Fournee's OpenEdition chapter on the 1768 Edict of Regulars gives a tighter institutional list: Bellozanne had seven benefices with cure of souls, including Sainte-Marguerite de Bellozanne, Saint-Martin de Brémontier with Saint-Leonard de Merval, Saint-Lucien, Saint-Pierre d'Elbeuf-en-Bray, and Notre-Dame du Thil-en-Bray with Riberpre.[^fournee-bellozanne-place] This belongs in the endowment cluster because it explains why the overlay anchors around Brémontier-Merval, Elbeuf-en-Bray, Saint-Lucien, Le Thil, and Riberpre are ecclesiastically connected. It does not, by itself, prove a G33 Bec donation component.
```

Exact footnotes:

```md
[^archives76-massy-esclavelles]: Archives departementales de Seine-Maritime, commune dossiers for Massy and Esclavelles, https://www.archivesdepartementales76.net/archive/catalogue/communes76/massy/n%3A168 and https://www.archivesdepartementales76.net/archive/catalogue/communes76/esclavelles. Source ID: `norman-geo-archives76-commune-dossiers-2026`.
[^bremontier-bellozanne-place]: Commune de Brémontier-Merval, "Histoire," official municipal page, https://www.bremontier-merval.fr/vie-culturelle/histoire. Source ID: `norman-geo-local-history-tourism-2026`.
[^fournee-bellozanne-place]: Jean Fournee, "L'edit des Reguliers (mars 1768) et les abbayes premontrees de Normandie," in *Droit prive et Institutions regionales*, Presses universitaires de Rouen et du Havre, OpenEdition Books, https://books.openedition.org/purh/12434?lang=en. Source ID: `norman-geo-institutional-localities-2026`.
```

## 9. Promote to `research/places/pays-de-bray.md`

Outcome: promote.

Reason: Bauduin's article is best handled as regional context, not as a new thin Criquiers/Haucourt place file. It supports the northern Gournay-honor context around Haucourt, Pierrement, Mesnil-Odon, Gourchelles, Beaubec, and Criquiers.

Exact operation: after `## Frontier interpretation`, add:

```md
## Northern honor context: Haucourt, Gourchelles, Criquiers

Pierre Bauduin's study of Villedieu-la-Montagne, Gourchelles, and Criquiers adds a northern frontier layer to the Pays de Bray record. The article explains that the Villedieu and Gourchelles settlement/franchise charters preceded the Beaubec foundation of the villeneuve of Criquiers, and that all three projects sit on the Normandy / Picardy confins.[^bauduin-pays-bray] The Haucourt lineage is especially relevant to the Gournay map: Bauduin places Haucourt, Pierrement, and Mesnil-Odon in the family's territorial base and says the lineage was implanted on La Montagne and the Pays de Bray edge, mainly on lands dependent on the honor of Gournay.[^bauduin-pays-bray]

The same passage ties the later Beaubec dossier back to the Gournay senior line: in the great confirmation charter that Hugues III de Gournay gave to Beaubec after 1180, Guillaume de Haucourt appears alongside Gila de Gourchelles.[^bauduin-pays-bray] This is not direct-line ancestor proof for G32-G36, but it is important place context: it shows the Gournay honor's northern dependency environment still structuring aristocratic and monastic action in the later twelfth and early thirteenth centuries.
```

Exact footnote:

```md
[^bauduin-pays-bray]: Pierre Bauduin, "Trois cas de peuplement en franchises en Normandie orientale: Villedieu-la-Montagne, Gourchelles et Criquiers," *Histoire & Societes Rurales* 15, no. 1 (2001): 131-176, especially the discussion of Villedieu, Haucourt, Beaubec, Gourchelles, and Criquiers, https://shs.cairn.info/revue-histoire-et-societes-rurales-2001-1-page-131?lang=fr. Source ID: `bauduin-franchises-normandie-orientale-2001`.
```

## 10. Optional place-file micro-addition to `research/places/gournay-en-bray.md`

Outcome: optional promote.

Reason: this is lower priority than the aggregate Beauvaisis and Gaillefontaine files. Use only if the Gournay-en-Bray file is being touched in the Phase 2 pass.

Exact operation: in `## Hugh III and the Beauvaisis acquisitions`, after the existing paragraph, add:

```md
The ConDE local-custom heading strengthens this outward link because it frames the Conquets as a Gournay jurisdiction beyond the Epte, held through the châtellenie and high justice of Gournay.[^conde-gournay-place] Ferrieres and Gancourt local histories then show that this legal geography still had local-place memory at the western and south-western edges of the block.[^ferrieres-gournay-place][^gancourt-gournay-place]
```

Exact footnotes:

```md
[^conde-gournay-place]: Projet ConDE, Universite de Caen Normandie, "Coutumes et usages locaux des vingt quatre Paroisses, Hameaux & Villages... Conquets Hue de Gournay," https://pdn-lingua.unicaen.fr/coutumiers/conde/pesnelle_lighter.xml/pesnelle-lighter-beta-002-007.html. Source ID: `projet-conde-conquets-hue-gournay`.
[^ferrieres-gournay-place]: Commune de Ferrieres-en-Bray, "Histoire de la ville," https://www.ferrieres-en-bray.fr/page/la-commune/l-histoire-de-ferrieres/histoire-de-la-ville. Source ID: `ferrieres-en-bray-official-history`.
[^gancourt-gournay-place]: Commune de Gancourt-Saint-Etienne, Bulletin municipal 2023, "Un peu d'historique de Gancourt-Saint-Etienne," p. 9 in the PDF extraction, https://gancourtsaintetienne.com/wp-content/uploads/2023/12/bm2023-1.pdf. Source ID: `gancourt-saint-etienne-bulletin-2023`.
```

## 11. Hold-review / do not promote yet

Outcome: hold-review.

Items:

- Ferrieres tourism URL in the v5 register returned 404 during this pass. Use the Ferrieres official municipal history instead.
- Elbeuf-en-Bray and Le Thil-Riberpre tourism URLs in the v5 register returned 404 during this pass. Use Brémontier-Merval and Fournee/OpenEdition for the Bellozanne institutional network until replacement stable URLs are found.
- Archives 76 Avesnes and Ferrieres are useful for fief and châtellenie references, but they are place-topography dossiers. Keep them in `norman-geo-archives76-commune-dossiers-2026` unless a later pass builds a specific Avesnes/Ferrieres place block.
- Archives 76 Criquiers is useful for Beaubec's fourteenth-century village foundation and Haucourt / Pierrement localities, but Bauduin is the stronger interpretive source for research prose.
- Locator-only pages for Saint-Quentin-des-Pres, Hericourt-sur-Therain, Doudeauville, Molagnies, Criquiers, Haucourt, Fontenay-Torcy, Torchy, Saint-Germer-de-Fly, Saint-Pierre-es-Champs, and Puiseux-en-Bray should remain geo support only unless the claim is specifically modern identification or coordinate support.

## 12. Validation after Phase 2 application

Run:

```powershell
npm.cmd run validate
git diff --check
```

If Phase 2 edits touch generated site data, also refresh the site package according to the repo's current site-generation rule before committing.
