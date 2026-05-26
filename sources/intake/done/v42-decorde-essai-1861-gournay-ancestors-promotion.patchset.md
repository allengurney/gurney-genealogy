# Intake patchset v42 — Decorde, Essai sur le Canton de Gournay (1861): deep-research promotion to people, places, and topics

**Prepared:** 2026-05-16
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Source material:** `sources/intake/new/deep-research-report-Gournay-Ancestors-in-Decordes-Essai-1861.md` (synthesis over `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`).

## Scope

The Decorde 1861 OCR text was already registered as `decorde-essai-canton-gournay-1861` and the validation file exists, but the substantive Gournay-line and place findings from the canonical text — and from the deep-research synthesis prepared in 2026-04 — have **not** been promoted into the research layer. This patchset closes that gap.

The findings touch four direct-line / collateral threads:

1. **G33 Hugh de Gournay III + Basilie Flaitel** — the 1082 Jumièges 190-arpent charter at Boshyon (the new direct-line donation event Decorde anchors), plus the Boshyon/*Boscus Hugonis* territorial base.
2. **G32 Gerard de Gournay** — the Hugues IV [c. 1112/22] Bec confirmation that explicitly names Gerard as the middle-generation donor in the ancestor chain Hugues III → Basilie → Gerard.
3. **Senior baron line collateral after Gerard — Hugues IV (m. Mélisende) and Hugues V** — Gaillefontaine 1164 endowment; Brémontier / Bellosanne 1198 foundation; Saint-Aubin 1200 priory; 1202 loss to Philip II Augustus; 1214 death in English exile; the *Chevaliers aux armes noires* heraldic tradition.
4. **Place library expansions** — Boshyon (new file), Bellosanne abbey (new file), Cottentray-Avesnes-en-Bray (new file), plus targeted Decorde-sourced additions to existing Gournay-en-Bray, Collégiale Saint-Hildevert, Gaillefontaine, and G33-Bec endowment-cluster files.

Findings live in research files. The OCR text and the deep-research synthesis remain in `sources/corpus_supplement/` solely as the source-anchored extract layer; they are not the home of the findings.

## What this patchset does **not** do

- It does **not** introduce a new ancestor fact sheet for Hugues IV or Hugues V. Both are collateral to the repo's direct line, which descends through G32 Gerard → G31 Walter (junior Norfolk branch). Their narrative lands in a new `research/topics/` file plus targeted additions to existing place files.
- It does **not** rewrite existing Decorde citations in `research/places/gournay-en-bray.md` or `research/places/beauvaisis-frontier-acquisitions.md`; those remain unchanged.
- It does **not** redraw the `gournay-norman-holdings` GeoJSON overlay polygons. §8 below records the overlay implications and queues the changes as a separate overlay refresh; the existing v5 institutional layer already anchors Bellozanne and Brémontier-Merval and the existing v5 western-dependency layer already anchors Avesnes-en-Bray.

---

## 1. `data/sources.json`

### 1.1 Metadata

Set:

```json
"lastUpdated": "2026-05-16"
```

### 1.2 No new sourceId

`decorde-essai-canton-gournay-1861` already exists. Do **not** create a second entry for the deep-research synthesis; it is a working analysis layer, not a primary source.

### 1.3 Update existing `decorde-essai-canton-gournay-1861.notes`

Replace the current `notes` value with the following, to record that the deep-research findings have been promoted and to broaden the "Findings recorded in" pointer:

```text
French local history and archaeology of the canton of Gournay. Important for Gournay-en-Bray, Beauvaisis frontier acquisitions, Boshyon/Bois-Hugues, Bremontier-Merval / Bellosanne, Gaillefontaine, the Collegiate Saint-Hildevert at Gournay, and Cottentray/Avesnes-en-Bray. Findings from the 2026 deep-research synthesis are now promoted into research/people/g33, research/people/g32, research/places/gournay-en-bray.md, research/places/collegiale-saint-hildevert-gournay.md, research/places/g33-bec-gournay-endowment-cluster.md, research/places/gaillefontaine.md, research/places/bosc-hyons.md, research/places/bellosanne-abbey.md, research/places/cottentray-avesnes-en-bray.md, and research/topics/senior-gournay-baron-line-collateral.md. The OCR text in sources/corpus_supplement is visibly noisy; cite exact French phrasing only after checking page images or cleaner scans for delicate claims.
```

---

## 2. Corpus / validation housekeeping

### 2.1 Copy the deep-research synthesis into `sources/corpus_supplement/`

The 2026-04 deep-research synthesis already sits at `sources/intake/done/deep-research-report-Gournay-Ancestors-in-Decordes-Essai-1861.md`. Copy it into the corpus supplement layer so research footnotes can reference the synthesis when convenient, and add a short header explaining its status. **The findings have already been promoted into research files; the corpus_supplement copy is for source-anchored extract-checking, not for findings.**

File operation:

```
cp "sources/intake/done/deep-research-report-Gournay-Ancestors-in-Decordes-Essai-1861.md" \
   "sources/corpus_supplement/deep-research-report-decorde-essai-gournay-ancestors.md"
```

Prepend the following header to the new corpus_supplement copy (replace the deep-research file's existing top heading):

```markdown
# Deep-research synthesis — Decorde, Essai sur le Canton de Gournay (1861) — Gournay-line ancestors

**Status:** Working synthesis prepared 2026-04 from the Decorde 1861 OCR text and routine reference-work context. Citation markers in the body (e.g., 【25†L1002-L1010】) are internal indices into the OCR text, not page references; do not propagate them into research prose. Findings are promoted into research files; this supplement holds the extract layer only.

**Primary source:** Decorde 1861, OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. Source ID: `decorde-essai-canton-gournay-1861`.
```

### 2.2 Update validation `sources/validations/decorde-essai-canton-gournay-1861.md`

Replace the `## Findings recorded` section with:

```markdown
## Findings recorded

Direct-line and senior-collateral Gournay findings from the 2026-04 deep-research synthesis over Decorde 1861 are now in:

- `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`
- `research/people/g32-gerard-de-gournay-fact-sheet.research.md`
- `research/places/gournay-en-bray.md`
- `research/places/collegiale-saint-hildevert-gournay.md`
- `research/places/g33-bec-gournay-endowment-cluster.md`
- `research/places/gaillefontaine.md`
- `research/places/bosc-hyons.md` (new)
- `research/places/bellosanne-abbey.md` (new)
- `research/places/cottentray-avesnes-en-bray.md` (new)
- `research/topics/senior-gournay-baron-line-collateral.md` (new)

Earlier Decorde citations remain in:

- `research/places/gournay-en-bray.md`
- `research/places/beauvaisis-frontier-acquisitions.md`
```

Leave the rest of the validation file (source identification, examined scope, remaining cautions) unchanged.

---

## 3. Direct-line research additions

### 3.1 `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`

Add a new subsection **2.13** at the end of the `## 2. Documentary attestations` block, before `## 3. Wife and family connections`. The new block adds the 1082 Jumièges 190-arpent charter and the Boshyon territorial base, both of which sit alongside the §2.2 undated Jumièges Radulphus Havoth charter already in the file.

```markdown
### 2.13 1082 — Jumièges 190-arpent charter at Boshyon (Decorde 1861)

Abbé J.-E. Decorde reports a separate Jumièges charter dated c. 1082 in which Hugh III de Gournay and his wife Basilie ratified the donation of one hundred and ninety arpents of land at **Boshyon** — the *Boscus Hugonis*, "Hugues's wood," lying south-south-west of Gournay-en-Bray (the modern commune of Bosc-Hyons, Seine-Maritime, INSEE 76124) — to the abbey of Jumièges, made by their vassal Raoul Havot. Decorde's text frames the place explicitly as *apud villam quæ vocatur Hugonis silva*.[^decorde-jumieges-1082-boshyon] This is the same charter as the undated Radulphus Havoth Jumièges charter preserved in the Rouen Archives paper cartulary (§2.2 above), now dated by Decorde to c. 1082 and located at Boshyon; the §2.2 entry's "undated" framing should be read against this Decorde dating and place-anchoring.

Boshyon matters for the territorial reconstruction. It is the toponym from which the family's woodland holding takes its name (*Boscus Hugonis* = Hugues's wood, almost certainly Hugh I de Gournay), and the same place will reappear in two later Gournay-side endowments: in 1164 Hugues IV and Mélisende will assign three boisseaux of wheat and five of oats from their manor at Boshyon to the new church of Gaillefontaine, ratified by Archbishop Rotrou of Rouen; and in 1195 a neighbour, Manassès de Bully, will endow one *muid* of oats from the Boshyon mill for a perpetual altar lamp before St Hildevert's relic at the Gournay collegiate church. The 1082 charter is the earliest documented use of Boshyon as a Gournay-family endowment base. The detailed place narrative now lives at `research/places/bosc-hyons.md`.[^decorde-boshyon-endowment-chain]

[^decorde-jumieges-1082-boshyon]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (Paris: Derache and Didron; Rouen: Lebrument, 1861); OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. 1082 charter recorded by Decorde in the Boshyon parish entry; the deep-research synthesis (`sources/corpus_supplement/deep-research-report-decorde-essai-gournay-ancestors.md`) cleans the citation. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-endowment-chain]: Decorde 1861, Boshyon parish entry; same source. The 1195 lamp endowment is by Manassès de Bully, not by a Gournay; it is included here because the *Boshyon* mill remained the local revenue stock for Gournay-area ecclesiastical patronage well after the Gournay seigneurial gift sequence began. Source ID: `decorde-essai-canton-gournay-1861`.
```

### 3.2 `research/people/g32-gerard-de-gournay-fact-sheet.research.md`

Add a new subsection **2.13** at the end of the `## 2. Documentary attestations` block, after §2.12 and before `## 3. Three pedigree / interpretive questions`. The new block records the [c. 1112/22] Hugues IV confirmation that explicitly names the Hugh III → Basilie → Gerard ancestor chain — a separate event from the Henry II [1181/89] royal confirmation already in §2.9.

```markdown
### 2.13 [c. 1112/22] — Hugues IV's Bec confirmation naming the ancestor chain (Decorde 1861)

Decorde preserves an early-twelfth-century confirmation, dated c. 1112 or 1122 in the local tradition he transmits, in which "Hugues de Gournay" — i.e., Hugues IV, Gerard's eldest son and successor in the senior barony — confirmed gifts to the Abbey of Bec made by "his ancestors Hugues and Basilie, and by Gérard, his father," and explicitly included the church of **Brémontier** and its tithes in that confirmation.[^decorde-hugues-iv-bec-confirmation]

This sits a generation earlier than the [1181/89] Henry II royal confirmation already recorded in §2.9, and it is independent of it. Together the two confirmations document the same donation chain — Hugh III → Basilie → Gerard → continued patronage under Hugues IV — in two distinct twelfth-century attestations, one familial (c. 1112/22) and one royal (1181/89). For the direct-line argument this strengthens Gerard's middle-generation role in the Gournay-Bec patronage relationship and supplies the immediate documentary context for §2.9 Henry II's later wholesale confirmation.

[^decorde-hugues-iv-bec-confirmation]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (Paris: Derache and Didron; Rouen: Lebrument, 1861); deep-research synthesis at `sources/corpus_supplement/deep-research-report-decorde-essai-gournay-ancestors.md`. Decorde's local-tradition dating is c. 1112 or 1122; the c. 1180s Henry II confirmation at §2.9 above is a distinct, later event. Source ID: `decorde-essai-canton-gournay-1861`.
```

---

## 4. Place-file additions and updates

### 4.1 `research/places/gournay-en-bray.md` — three small additions

This file already references Decorde for the Beauvaisis acquisitions narrative and lists Decorde in the Sources section. Add a new subsection — placed after the existing "Hugh II and the military frontier" / Mortemer narrative and before whichever section currently follows it — covering the Decorde-sourced material that belongs at the *seat* rather than the abbey or topic level:

```markdown
## Saint-Hildevert relics, *Chevaliers aux armes noires*, and the 1202 loss

Three Gournay-en-Bray features sit naturally at the seat level rather than in a daughter file.

**The arrival of Saint Hildevert's relics, twelfth century.** Decorde recounts that when an earlier monastic community at Brémontier was reorganized as a collegiate church, the canons were "transferred to Gournay, where the body of Saint Hildevert had just been brought," and that Hugues IV de Gournay then confirmed the Brémontier church to Bec, with explicit reference to Hildevert's body. The collégiale Notre-Dame at Gournay thereby acquired the relics for which it became the principal regional pilgrimage focus; the relics are still associated with the crypt of the surviving collegiate church.[^decorde-saint-hildevert-translation]

**Black heraldry — *Chevaliers aux armes noires*.** Local tradition preserved by Decorde gave the senior barons of Gournay sable arms and the regional nickname *Chevaliers aux armes noires* — "knights of the black arms" — through the senior line. The black-shield tradition aligns with the earlier Eudes / Rollo black-shield motif already in this file as a foundation-myth element, and shows the same colour signature persisting in local memory through the senior line's twelfth-century floruit.[^decorde-armes-noires]

**The 1202 loss and the silver-knight overlay.** Decorde describes the dramatic end of the senior baron line at Gournay: after Philippe Auguste's 1202 victory the arms of Gournay were reblazoned to include the figure of a silver knight, marking the Capetian conquest. Philippe's young daughter Marie, fiancée of Arthur of Brittany, was knighted in the Gournay collegiate church; thereafter Decorde says *"le pouvoir des premiers seigneurs de Gournay"* faded as the senior baron line lost the honour. The senior baron Hugues V, last "Hugues de Gournay" mentioned by Decorde at the seat, died in English exile in 1214.[^decorde-1202-silver-knight]

[^decorde-saint-hildevert-translation]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (Paris: Derache and Didron; Rouen: Lebrument, 1861); OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. Source ID: `decorde-essai-canton-gournay-1861`. See also `research/places/collegiale-saint-hildevert-gournay.md` for the church-side detail.
[^decorde-armes-noires]: Decorde 1861, same source. Cross-link: the black-shield foundation tradition already documented for Eudes / Rollo earlier in this file.
[^decorde-1202-silver-knight]: Decorde 1861, same source. The full collateral senior-line narrative — Hugues IV (Mélisende), Hugues V (Bellosanne, Saint-Aubin, 1202 loss, 1214 death in English exile) — lives in `research/topics/senior-gournay-baron-line-collateral.md`.
```

### 4.2 `research/places/collegiale-saint-hildevert-gournay.md` — Hildevert translation and Manassès lamp

The current file describes the surviving twelfth-century church but does not record the Hildevert translation or the 1195 lamp. Add a new section between the existing "Architectural and historical context" and "What remains from the Gournay period":

```markdown
## Saint Hildevert's relics and the Brémontier translation

Local tradition preserved by Decorde reports that the body of Saint Hildevert was translated from an earlier monastic site at Brémontier to the Gournay collegiate church in the twelfth century, in connection with the Brémontier community's reorganization as a collegiate body and its transfer to Gournay. Hugues IV de Gournay subsequently confirmed the Brémontier church and its tithes to the Abbey of Bec, with explicit reference to the saint's body. From this period forward the Gournay collegiate church is the regional pilgrimage focus for Hildevert.[^decorde-hildevert-translation]

A later twelfth-century witness ties the relic into the local revenue economy. In 1195 Manassès de Bully — a neighbour of the Gournays at Boshyon (*Boscus Hugonis*) — endowed one *muid* of oats per year from the Boshyon mill to maintain a perpetual altar lamp before St Hildevert's relic in the Gournay church.[^decorde-manasses-lamp-1195]

[^decorde-hildevert-translation]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861); OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-manasses-lamp-1195]: Decorde 1861, Boshyon parish entry. The Boshyon mill and surrounding holdings are documented in `research/places/bosc-hyons.md`. Source ID: `decorde-essai-canton-gournay-1861`.
```

### 4.3 `research/places/g33-bec-gournay-endowment-cluster.md` — c. 1112/22 confirmation paragraph

Add a new short subsection after the "Why this cluster matters" paragraph and before the "Component places and rights" table:

```markdown
## Twelfth-century confirmation events

Two later confirmations preserve the donation chain for this cluster:

- **c. 1112 or 1122 — Hugues IV de Gournay's confirmation** records that Hugues IV confirmed gifts to Bec made by "his ancestors Hugues and Basilie, and by Gérard, his father," explicitly naming the Brémontier church and its tithes within the confirmed package. This is the earliest *familial* confirmation of the full Hugh III → Basilie → Gerard donation chain.[^decorde-hugues-iv-bec]
- **[1181/89] — Henry II's royal confirmation** later restated the same chain at a royal level, naming "Hugonis de Gornaco et Girardi filii…Girardi de Gornaio et Basilie matris sue" and confirming the Bec possessions.[^fmg-henry-ii-bec]

Together the two confirmations establish that the Gournay-Bec relationship was renewed at the family level within a single generation of Gerard's death and again at the royal level under Henry II, both with the explicit ancestor recitation that anchors Brémontier in the cluster.

[^decorde-hugues-iv-bec]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861); deep-research synthesis at `sources/corpus_supplement/deep-research-report-decorde-essai-gournay-ancestors.md`. Source ID: `decorde-essai-canton-gournay-1861`.
[^fmg-henry-ii-bec]: Foundation for Medieval Genealogy, Norman Nobility — Hugh III de Gournay, citation [885] (Henry II's confirmation charter, [1181/89]). Already documented in `research/people/g32-gerard-de-gournay-fact-sheet.research.md` §2.9. Source ID: `fmg-medlands-normacre` (existing).
```

### 4.4 `research/places/gaillefontaine.md` — 1164 church endowment

The current file documents Gaillefontaine as the third site of the Gerard / William Rufus 1089/90 castle delivery and as a motte castrale. It does not document the 1164 ecclesiastical endowment. Add a new section between "Frontier geography" and "What remains from the medieval frontier site":

```markdown
## Hugues IV and Mélisende — the 1164 church endowment

A separate dossier of Decorde-sourced material concerns the parish church rather than the motte. In 1164 Hugues IV de Gournay and his wife Mélisende — almost certainly Mélisende de Vermandois — endowed the newly built church of Gaillefontaine with *three boisseaux de froment et cinq boisseaux d'avoine* (three bushels of wheat and five of oats) taken at Boshyon (*Boscus Hugonis*, modern Bosc-Hyons, south-south-west of Gournay-en-Bray). The grant was ratified by Rotrou, archbishop of Rouen, in 1164. The endowment supports the dating of the church to the mid-twelfth century and confirms that the Gournay senior line, in the generation after the Crusader Gerard, was continuing the family's pattern of converting seigneurial revenues from named woodland holdings into parish-church support.[^decorde-gaillefontaine-1164]

Gaillefontaine therefore sits in the place library under two distinct Gournay-relevance threads: a fortified motte delivered to William Rufus in 1089/90 by Gerard (§"Frontier geography"), and a parish church endowed by Gerard's eldest son Hugues IV and his wife Mélisende in 1164. The motte and the parish church are different aspects of the same place under Gournay influence across roughly seventy-five years.

[^decorde-gaillefontaine-1164]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861), Gaillefontaine parish entry; OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. Source ID: `decorde-essai-canton-gournay-1861`. The Boshyon revenue base is documented in `research/places/bosc-hyons.md`.
```

### 4.5 New file — `research/places/bosc-hyons.md`

```markdown
# Bosc-Hyons (medieval Boshyon / *Boscus Hugonis*)

Bosc-Hyons is a small commune in the canton of Gournay-en-Bray (Seine-Maritime), south-south-west of Gournay itself. The modern name is a worn descendant of the medieval Latin *Boscus Hugonis* — "Hugues's wood" — which Decorde 1861 catalogues across several medieval spellings: Boshyon, Boschyon, Bos-Huon, Bos-Hyon, Bos-Hyvon. Decorde recommended that the modern name *should* properly be Bois-Hugues or Bosc-Hugon, while noting that local usage had settled on Bosc-Hyons. The personal name Hugues almost certainly refers to Hugh I de Gournay, "The Fortifier," whose generation gave the Gournay woodland its lasting toponym.

## Why this place matters

Bosc-Hyons is the most economically substantive Gournay-line landholding documented for the eleventh and twelfth centuries. It supplied the revenue stock — woodland, manor, and mill — for at least three documented Gournay-area ecclesiastical endowments, and its parish church was given by a Gournay lord to the Gournay collegiate chapter in the twelfth century. The chapter held the patronage until 1623. Decorde 1861 carries the fullest concise Boshyon entry of any source consulted.

## Endowment history

- **c. 1066 — Bohon at Hastings.** Decorde, citing Gabriel Dumoulin's *Histoire générale de Normandie*, records that "le sieur de Bohon" — the Boshyon seigneur — fought for Duke William at the conquest of England in 1066.[^decorde-boshyon-hastings]
- **c. 1082 — Jumièges 190-arpent charter.** Hugh III de Gournay and his wife Basilie ratified the donation of one hundred and ninety arpents of land at Boshyon, *apud villam quæ vocatur Hugonis silva*, to the abbey of Jumièges, made by their vassal Raoul Havot.[^decorde-boshyon-1082]
- **c. 1164 — Gaillefontaine grain endowment.** Hugues IV de Gournay and his wife Mélisende endowed the newly built church of Gaillefontaine with three boisseaux of wheat and five of oats taken at Boshyon, *apud Boscum Hugonis*. The grant was ratified by Rotrou, archbishop of Rouen, in 1164.[^decorde-boshyon-1164]
- **1195 — Manassès de Bully lamp endowment.** Manassès de Bully gave one *muid* of oats per year, drawn from his Boshyon mill, to the Gournay chapter for the upkeep of a perpetual altar lamp burning before the body of Saint Hildevert — *"pour l'entretien d'une lampe ardente devant le corps de saint Hildevert."*[^decorde-boshyon-1195]
- **Twelfth century — Saint-Michel parish church given to Gournay chapter.** A sire de Gournay gave the Boshyon parish church to the Gournay collegiate chapter; the chapter held the patronage and presented to the cure until 1623, when it exchanged the patronage for that of the chapel of Villers-sur-Andely.[^decorde-boshyon-st-michel-gift]

## Mortemer's Mont-Rôti grange

A separate twelfth-century arrangement deserves noting. The Cistercian abbey of Mortemer owned a *métairie* (farmstead) within the medieval Boshyon parish called the *grange du Mont-Rôti*, for which it paid the Gournay chapter seven *muids* of grain per year, half wheat and half oats. In 1243, after a dispute over the grain measure, the render was commuted to a cash rent of seven *livres parisis*. The Mont-Rôti grange is internal to the Boshyon parish and is not the modern continuator of the locality.[^decorde-boshyon-mont-roti]

## What remains today

Bosc-Hyons survives as a distinct commune (INSEE 76124, postal 76220) at approximately 49.446 N, 1.659 E. The parish church of Saint-Michel was reduced to a *succursale* (subordinate parish chapel) in 1826; Decorde reports the surviving tower as twelfth-century Romanesque: *"L'aspect du clocher annonce une construction du XIIe siècle."* The historic Boshyon parish also contained the named hamlets of *les Carreaux* and *le Bus*.[^decorde-boshyon-survival]

## Later seigneurial succession (post-medieval)

Decorde records the post-medieval seigneurial succession at Boshyon through the families de Moy, des Courtils, de Bonissent, and Bouvier; these belong to the early-modern history of the place rather than the Gournay record, but they are worth noting here because the Decorde entry is unusually full and may be useful for any future Bosc-Hyons place-history work.[^decorde-boshyon-post-medieval]

## Crosslinks

- `research/places/gournay-en-bray.md`
- `research/places/collegiale-saint-hildevert-gournay.md`
- `research/places/gaillefontaine.md`
- `research/places/g33-bec-gournay-endowment-cluster.md`
- `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`
- `research/topics/senior-gournay-baron-line-collateral.md`

[^decorde-boshyon-hastings]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (Paris: Derache and Didron; Rouen: Lebrument, 1861), Boshyon parish entry, citing Gabriel Dumoulin, *Histoire générale de Normandie*, pp. 184 and 185; OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-1082]: Decorde 1861, same Boshyon entry; Decorde further cross-refers to Daniel Gurney, *The Record of the House of Gournay*, pp. 57, 63, 113, 114, 117, 202, 754. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-1164]: Decorde 1861, same source. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-1195]: Decorde 1861, same source. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-st-michel-gift]: Decorde 1861, same source. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-mont-roti]: Decorde 1861, same source: *"L'abbaye de Mortemer y possédait une métairie, la grange du Mont-Rôti…"* The earlier 2026-04 deep-research synthesis misread this medieval grange name as a modern locality 'Mont-Bôty / Mont-Bosy'; that misreading is corrected here. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-survival]: Decorde 1861, same source: *"L'église de Boshyon est sous le vocable de saint Michel. L'aspect du clocher annonce une construction du XIIe siècle… L'église de Boshyon a été érigée en succursale en 1826."* Modern coordinate verified via Cartes France / db-city / Archives départementales 76 (Bosc-Hyons commune dossier). Source IDs: `decorde-essai-canton-gournay-1861`.
[^decorde-boshyon-post-medieval]: Decorde 1861, same source; succession through de Moy, des Courtils, de Bonissent, Bouvier families. Source ID: `decorde-essai-canton-gournay-1861`.
```

### 4.6 New file — `research/places/bellosanne-abbey.md`

```markdown
# Bellosanne Abbey (Notre-Dame de Bellozanne, Brémontier-Merval)

Bellosanne (also Bellozanne) is the Premonstratensian abbey founded by Hugues V de Gournay in 1198 at Brémontier (now Brémontier-Merval, Seine-Maritime). It is the principal religious foundation of the senior Gournay baron line in its last generation and the most consequential Gournay-side ecclesiastical site after the Gournay collegiate church itself.

## Why this place matters

Bellosanne anchors the closing chapter of the senior-line story. Hugues V — the last "Hugues de Gournay" mentioned by Decorde at the seat — founded the abbey just four years before he lost Gournay to Philippe Auguste in 1202. The foundation is the senior baron's most durable religious legacy, and the place sits at the centre of the Pays de Bray patronage geography linking the senior line to Bec, Jumièges, and the Gournay collegiate church.

## Foundation and dedication

The foundation date is given as 1198 by Decorde, though local tradition occasionally gives 1193; the modern *OpenEdition* table of abbeys founded by Norman lords settles on 1198. The dedication is to Notre-Dame. Modern site archaeology shows the abbey lay between two former ponds on the Pays de Bray plateau.[^decorde-bellosanne-foundation][^openedition-bellozanne-1198]

The founder's signatories included Adam de Ferrières as a Hugues V vassal, per the modern Ferrières-en-Bray municipal history page already in `data/sources.json`.[^ferrieres-bellozanne-1198]

## Suppression, demolition, and the 1827 château

During the Revolution Bellosanne was suppressed. By 1797 the church and cloister had been sold and a buyer had begun demolishing the buildings. In 1827 a new château erased what remained of the medieval ruins on the site; nothing medieval remains visible on the surface today.[^decorde-bellosanne-suppression]

## Place-library framing

Bellosanne is collateral relative to the repo's direct line (the senior baron line ended at Hugues V; the repo descends through G32 Gerard's youngest son Walter G31), but it is the most consequential single building project documented for the senior line in its last fifty years. Treat Bellosanne as part of the Pays de Bray monastic patronage cluster (Bec, Jumièges, Gaillefontaine parish, Gournay collegiate church) anchored at the seat at Gournay-en-Bray.

## Crosslinks

- `research/places/gournay-en-bray.md`
- `research/places/collegiale-saint-hildevert-gournay.md`
- `research/places/g33-bec-gournay-endowment-cluster.md`
- `research/topics/senior-gournay-baron-line-collateral.md`

[^decorde-bellosanne-foundation]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861); OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. Source ID: `decorde-essai-canton-gournay-1861`.
[^openedition-bellozanne-1198]: OpenEdition, table of abbeys founded by Norman lords, "Notre-Dame de Bellozanne — 1198, Hugues V de Gournay." Source ID: `openedition-abbayes-seigneurs-normands-annexe`.
[^ferrieres-bellozanne-1198]: Ferrières-en-Bray municipal history page, "Adam de Ferrières, vassal of Hugues V de Gournay and signatory to the Bellozanne foundation." Source ID: `ferrieres-en-bray-official-history`.
[^decorde-bellosanne-suppression]: Decorde 1861, same source; suppression/demolition timeline reported by Decorde and corroborated in modern Brémontier-Merval municipal history. Source IDs: `decorde-essai-canton-gournay-1861`, `norman-geo-local-history-tourism-2026` (Brémontier-Merval municipal-history page in the bundle).
```

### 4.7 New file — `research/places/cottentray-avesnes-en-bray.md`

```markdown
# Cottentray (Avesnes-en-Bray)

Cottentray is a hamlet in the modern commune of Avesnes-en-Bray (Seine-Maritime), east of Gournay-en-Bray. Decorde 1861 preserves two distinct Cottentray episodes that bear on the Gournay record.

## Quarter-fief of Gournay

Until the fifteenth century the seigneury of Cottentray was held in parts; one quarter-fief — *"un quart de fief appartenant originellement aux seigneurs de Gournay"* — descended from the senior Gournay barons. In the fifteenth century Marie de Bourbon sold that quarter to the Potin family, who henceforth held it under their own name.[^decorde-cottentray-quarter-fief] This is the only Decorde-documented case of a quarter-share fragment of Gournay holdings surviving as a distinct sub-fief after the 1202 Capetian conquest and the senior line's extinction.

## The 1682 *Clos des Anglais* tomb discovery

In 1682 labourers turned up eight to ten stone tombs ("huit à dix tombeaux en pierre") in a Cottentray field locally known as the *Clos des Anglais* — "the close of the English." No inscription survived. Decorde, drawing on the local antiquary G. de la Mairie, treats the burials as plausibly *"des chevaliers tués pendant nos guerres avec l'Angleterre"* — knights killed in the wars with England — without committing to whether the relevant English wars are the Hundred Years' War campaigns or earlier Anglo-Norman conflicts.[^decorde-cottentray-clos-des-anglais] The tombs are no longer locatable on the modern landscape.

## Why these episodes are recorded here

The quarter-fief preserves a tail-end of the senior-line territorial inheritance into the fifteenth century, after the 1202 loss of Gournay itself. The 1682 tomb discovery is post-medieval but reflects local memory of Anglo-Norman conflict in a Gournay-adjacent field. Both belong in the place library at Cottentray rather than in the seat file.

## Crosslinks

- `research/places/gournay-en-bray.md`
- `research/topics/senior-gournay-baron-line-collateral.md`

[^decorde-cottentray-quarter-fief]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861), Avesnes / Cottentray parish entry; OCR text at `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-cottentray-clos-des-anglais]: Decorde 1861, same source, citing G. de la Mairie. Source ID: `decorde-essai-canton-gournay-1861`.
```

---

## 5. Collateral topic file

### 5.1 New file — `research/topics/senior-gournay-baron-line-collateral.md`

The repo's direct line descends through G32 Gerard de Gournay → G31 Walter de Gournay (junior Norfolk branch). The **senior** baron line — Gerard's eldest son Hugues IV and his son Hugues V, last lord of Gournay — is collateral. The senior line's last two generations matter for the repo's story because they hold Gournay-en-Bray itself through the twelfth century, fund Bellosanne and Saint-Aubin priory, and end at the 1202 Capetian conquest. Decorde 1861 carries the fullest concise narrative of those two generations.

```markdown
# Senior Gournay baron line — Hugues IV and Hugues V (collateral)

The repo's direct line descends through Gerard de Gournay (G32) and his youngest son Walter de Gournay (G31), founder of the junior Norfolk branch. The **senior** Gournay baron line passed through Gerard's eldest son Hugues IV and ended at Hugues V, the last lord of Gournay before the Capetian conquest of Normandy. Both are collateral to the direct line, but the senior line holds the Norman seat itself, and its closing chapter shapes the place library at Gournay-en-Bray, Bellosanne, Cottentray, and Gaillefontaine. This topic file consolidates the senior-line narrative as it appears in Decorde 1861 and adjacent sources.

## Hugues IV de Gournay (c. 1098 – c. 1180)

Hugues IV inherited the senior barony from Gerard. He held Gournay-en-Bray through the long mid-twelfth century — the reigns of Louis VI and Louis VII of France, Henry I and Henry II of England — and was the family figure responsible for the major twelfth-century consolidation of the senior line.

- **Marriage to Mélisende.** Decorde names Hugues IV's wife as *"Millesende,"* a local spelling for Mélisende. Standard reference-work identification is Mélisende de Vermandois, daughter of Thomas de Marle.[^decorde-hugues-iv-melisende]
- **1112 / 1122 Bec confirmation.** Hugues IV confirmed gifts to Bec by his ancestors Hugues III and Basilie, and by his father Gerard, including the Brémontier church and tithes. See `research/people/g32-gerard-de-gournay-fact-sheet.research.md` §2.13 and `research/places/g33-bec-gournay-endowment-cluster.md`.[^decorde-hugues-iv-bec]
- **1127 Beaubec foundation.** Hugues IV is credited by the *OpenEdition* table of Norman abbey foundations with co-founding Beaubec in 1127. The foundation date and identification are independent of Decorde.[^openedition-beaubec-1127]
- **1164 Gaillefontaine endowment.** Hugues IV and Mélisende assigned three boisseaux of wheat and five of oats from their manor at Boshyon to the new church of Gaillefontaine. See `research/places/gaillefontaine.md` and `research/places/bosc-hyons.md`.[^decorde-hugues-iv-gaillefontaine]
- **Death.** Decorde gives a death date of 1182 for Hugues IV. The earlier Henry II Bec confirmation [1181/89] cited in the Gerard companion §2.9 (covering "Hugonis de Gornaco et Girardi filii") is best read as confirming the gifts of Hugh III + Gerard rather than naming a still-living Hugues IV, consistent with the 1182 death date.[^decorde-hugues-iv-death]

## Hugues V de Gournay (c. 1140 – 1214)

Hugues V was the last "Hugues de Gournay" at the seat. His career maps onto the closing decades of Plantagenet Normandy, his foundations are the largest religious imprint of the senior line at its end, and his loss of Gournay marks the formal break between the family name and the family seat.

- **1190 Third Crusade.** Genealogical reference works place Hugues V at Acre on the Third Crusade in 1190. Decorde does not directly attest the crusade but his narrative is consistent with it.[^crusade-1190-hugues-v]
- **1198 Bellosanne foundation.** Hugues V founded Notre-Dame de Bellozanne at Brémontier (now Brémontier-Merval), the Premonstratensian abbey that became the senior line's signature religious foundation. See `research/places/bellosanne-abbey.md`.[^decorde-hugues-v-bellosanne]
- **1200 Saint-Aubin priory.** Hugues V founded a priory at Saint-Aubin in 1200.[^decorde-hugues-v-saint-aubin]
- **1202 loss of Gournay.** Philippe Auguste's 1202 conquest of Normandy took Gournay from the senior line. Decorde records the dramatic moment: Philippe's daughter Marie, fiancée of Arthur of Brittany, was knighted in the Gournay collegiate church, and Gournay's arms were reblazoned to include the figure of a silver knight to mark the Capetian conquest. The senior line's territorial power at Gournay-en-Bray ended in this transfer.[^decorde-1202-loss]
- **1214 death in English exile.** Hugues V died in 1214 in English exile. Decorde frames the moment as the close of the senior-line story: *"le pouvoir des premiers seigneurs de Gournay"* faded, and the senior baron name ceased to be attached to Gournay-en-Bray itself.[^decorde-hugues-v-death]

## *Chevaliers aux armes noires*

Decorde preserves the regional epithet for the senior barons: *Chevaliers aux armes noires*, "knights of the black arms," from their sable (black) coat of arms. The epithet had passed into local memory by the nineteenth century and the post-1202 silver-knight overlay was understood as the heraldic mark of Capetian conquest. The black-arms tradition aligns with the earlier Eudes / Rollo black-shield foundation motif preserved in the seat file.[^decorde-armes-noires-topic]

## Why this stays a topic, not a fact sheet

Neither Hugues IV nor Hugues V is in the repo's direct line; the junction is at G32 Gerard, whose youngest son Walter G31 founds the Norfolk junior branch from which the published line descends. A topic file lets the place files (Gournay-en-Bray, Bellosanne, Gaillefontaine, Cottentray, Boshyon) crosslink to a single senior-line narrative without scattering it across collateral person files.

## Crosslinks

- `research/people/g32-gerard-de-gournay-fact-sheet.research.md` §2.13
- `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` §2.13
- `research/places/gournay-en-bray.md`
- `research/places/collegiale-saint-hildevert-gournay.md`
- `research/places/g33-bec-gournay-endowment-cluster.md`
- `research/places/gaillefontaine.md`
- `research/places/bosc-hyons.md`
- `research/places/bellosanne-abbey.md`
- `research/places/cottentray-avesnes-en-bray.md`

[^decorde-hugues-iv-melisende]: J.-E. Decorde, *Essai historique et archéologique sur le Canton de Gournay* (1861); Mélisende de Vermandois identification is standard reference-work synthesis. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-hugues-iv-bec]: Decorde 1861, same source. Cross-references as listed in the body. Source ID: `decorde-essai-canton-gournay-1861`.
[^openedition-beaubec-1127]: OpenEdition, table of abbeys founded by Norman lords, "Saint-Laurent de Beaubec — 1127, Hugues II de Gournay." Decorde's "Hugues IV" and OpenEdition's "Hugues II" refer to the same person under different numbering conventions. Source ID: `openedition-abbayes-seigneurs-normands-annexe`.
[^decorde-hugues-iv-gaillefontaine]: Decorde 1861, Gaillefontaine parish entry. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-hugues-iv-death]: Decorde 1861. The Henry II [1181/89] Bec confirmation cited in the G32 companion §2.9 names the donations of Hugh III and Gerard rather than Hugues IV; the 1182 death date is consistent with Henry II's mid-1180s confirmation of the earlier ancestor chain. Source ID: `decorde-essai-canton-gournay-1861`.
[^crusade-1190-hugues-v]: Reference-work synthesis (Wikipedia and adjacent biographical pages on the family); Decorde does not directly attest the crusade. Treat as standard collateral context. Source ID: `decorde-essai-canton-gournay-1861` (anchor), supplemented by general reference-work knowledge.
[^decorde-hugues-v-bellosanne]: Decorde 1861, Brémontier / Bellosanne entry. See `research/places/bellosanne-abbey.md`. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-hugues-v-saint-aubin]: Decorde 1861, same source. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-1202-loss]: Decorde 1861, same source. The silver-knight overlay narrative is also referenced in `research/places/gournay-en-bray.md`. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-hugues-v-death]: Decorde 1861, same source. Source ID: `decorde-essai-canton-gournay-1861`.
[^decorde-armes-noires-topic]: Decorde 1861, same source. Cross-link: the black-shield foundation tradition for Eudes / Rollo in `research/places/gournay-en-bray.md`. Source ID: `decorde-essai-canton-gournay-1861`.
```

---

## 6. `data/places.json` and `data/places_detail.json` additions

Three new canonical place records are added so the new research files have proper structured-data anchors. All three are placed in the Pays de Bray / Normandy cluster, near the existing `place-gournay-en-bray-normandy-france`, `place-collegiale-saint-hildevert-gournay-en-bray-normandy-france`, and `place-gaillefontaine-castle-domain-normandy-france` records. Preserve existing ordering for the surrounding records; only insert.

### 6.1 New `places.json` entries

Insert near other Pays de Bray entries (after `place-collegiale-saint-hildevert-gournay-en-bray-normandy-france` is a natural spot for Bellosanne; Boshyon and Cottentray fit naturally after Gaillefontaine in the same cluster):

```json
  {
    "placeId": "place-bellosanne-abbey-bremontier-merval-normandy-france",
    "name": "Notre-Dame de Bellozanne abbey, Brémontier-Merval, Normandy, France",
    "aliases": [
      "Bellosanne",
      "Bellozanne",
      "Notre-Dame de Bellozanne",
      "Abbaye Notre-Dame de Bellozanne",
      "Abbaye de Bellosanne",
      "Brémontier-Merval abbey"
    ],
    "shortDescription": "Premonstratensian abbey founded by Hugues V de Gournay in 1198",
    "placeType": "abbey / religious foundation",
    "coordinate": {
      "lat": 49.505556,
      "lng": 1.611111
    },
    "coordinatePrecision": "high",
    "roles": [
      "ecclesiastical foundation",
      "monastic patronage",
      "senior-line religious legacy",
      "Pays de Bray institutional anchor"
    ],
    "ancestorLinks": [
      {
        "recordId": "collateral-hugues-v-de-gournay",
        "role": "founder, 1198"
      }
    ],
    "filename": "bellosanne-abbey.md"
  },
  {
    "placeId": "place-bosc-hyons-boshyon-normandy-france",
    "name": "Bosc-Hyons (medieval Boshyon / Boscus Hugonis), Seine-Maritime, Normandy, France",
    "aliases": [
      "Bosc-Hyons",
      "Boshyon",
      "Boscus Hugonis",
      "Bosc-Hugon",
      "Bois-Hugues",
      "Bois Hugues",
      "Boschyon",
      "Bos-Huon",
      "Bos-Hyon",
      "Bos-Hyvon",
      "Saint-Michel du Boschyon"
    ],
    "shortDescription": "Medieval Gournay-family woodland, manor, and mill commune south-south-west of Gournay-en-Bray",
    "placeType": "commune / former manor and woodland",
    "coordinate": {
      "lat": 49.446,
      "lng": 1.659
    },
    "coordinatePrecision": "high",
    "roles": [
      "Gournay direct landholding",
      "endowment revenue base",
      "parish (continuing)",
      "name etymology (Hugues's wood)"
    ],
    "ancestorLinks": [
      {
        "recordId": "ancestor-g33-hugh-de-gournay-iii",
        "role": "1082 Jumièges 190-arpent endowment base"
      },
      {
        "recordId": "collateral-hugues-iv-de-gournay",
        "role": "1164 Gaillefontaine grain endowment from manor"
      }
    ],
    "filename": "bosc-hyons.md"
  },
  {
    "placeId": "place-cottentray-avesnes-en-bray-normandy-france",
    "name": "Cottentray (Avesnes-en-Bray), Normandy, France",
    "aliases": [
      "Cottentray",
      "Cottentray hamlet",
      "Avesnes-en-Bray Cottentray quarter-fief",
      "Clos des Anglais"
    ],
    "shortDescription": "Hamlet in Avesnes-en-Bray; medieval quarter-fief of Gournay surviving to 15th century",
    "placeType": "hamlet / fief fragment",
    "coordinate": {
      "lat": 49.4697,
      "lng": 1.6733
    },
    "coordinatePrecision": "medium",
    "roles": [
      "Gournay quarter-fief (medieval through 15c)",
      "post-medieval Anglo-Norman tomb-discovery site",
      "western Gournay dependency context"
    ],
    "ancestorLinks": [
      {
        "recordId": "collateral-senior-gournay-baron-line",
        "role": "quarter-fief held until 15c sale to Potin family"
      }
    ],
    "filename": "cottentray-avesnes-en-bray.md"
  }
```

Use `"recordId"` values consistent with the conventions already in `places.json`. If the existing schema does not yet carry collateral-line `recordId` strings (`collateral-hugues-iv-de-gournay`, `collateral-hugues-v-de-gournay`, `collateral-senior-gournay-baron-line`), Phase 2 should either omit those `ancestorLinks` entries entirely or add the strings as new collateral keys consistent with the existing pattern — but do **not** invent new direct-line `recordId` strings.

### 6.2 New `places_detail.json` entries

Insert in the same cluster order. Match the existing key set (`placeName`, `longDescription`, `siteName`, `streetAddress`, `extantStatus`, `extantStatusDescription`, `coordinateBasis`, `imageUrl`, `imageTitle`, `heritageUrl`, `heritageLabel`, `reviewNotes`).

```json
  {
    "placeId": "place-bellosanne-abbey-bremontier-merval-normandy-france",
    "placeName": "Notre-Dame de Bellozanne abbey, Brémontier-Merval, Normandy, France",
    "longDescription": "Premonstratensian abbey founded by Hugues V de Gournay in 1198 at Brémontier (now Brémontier-Merval, Seine-Maritime), dedicated to Notre-Dame, sited between two former ponds on the Pays de Bray plateau. The signal religious foundation of the senior Gournay baron line in its last generation, and the most consequential Gournay-side ecclesiastical site after the Gournay collegiate church itself.",
    "siteName": "Abbaye Notre-Dame de Bellozanne",
    "streetAddress": "",
    "extantStatus": "demolished; no medieval fabric on surface",
    "extantStatusDescription": "Bellozanne was suppressed during the Revolution. By 1797 the church and cloister had been sold and a buyer had begun demolishing the buildings. In 1827 a new château erased what remained of the medieval ruins on the site. Modern archaeology locates the abbey between two former ponds on the plateau.",
    "coordinateBasis": "Existing Gournay institutional overlay anchor point for Abbaye Notre-Dame de Bellozanne",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "https://fr.wikipedia.org/wiki/Abbaye_Notre-Dame_de_Bellozanne",
    "heritageLabel": "Abbaye Notre-Dame de Bellozanne — French Wikipedia",
    "reviewNotes": [
      "Promote from overlay anchor to canonical place record; the v5 institutional overlay already carries the same coordinate.",
      "Foundation date 1198 follows Decorde 1861 and OpenEdition; the parenthetical 1193 in Decorde is left unresolved.",
      "Patronage cluster includes Brémontier-Merval, Elbeuf-en-Bray, Saint-Lucien, Le Thil, Riberpré — see existing overlay anchor metadata."
    ]
  },
  {
    "placeId": "place-bosc-hyons-boshyon-normandy-france",
    "placeName": "Bosc-Hyons (medieval Boshyon / Boscus Hugonis), Seine-Maritime, Normandy, France",
    "longDescription": "Modern Bosc-Hyons (INSEE 76124, postal 76220), the medieval Boshyon / Boscus Hugonis — 'Hugues's wood,' almost certainly named for Hugh I de Gournay. A small commune in the canton of Gournay, south-south-west of Gournay-en-Bray. Decorde 1861 catalogues medieval spellings Boshyon, Boschyon, Bos-Huon, Bos-Hyon, Bos-Hyvon and the recommended modern French rendering Bois-Hugues or Bosc-Hugon. The medieval parish was the revenue base for at least three Gournay-area endowments — the 1082 Jumièges 190-arpent charter by Hugh III and Basilie, *apud villam quæ vocatur Hugonis silva*; the 1164 grain endowment by Hugues IV and Mélisende for the church of Gaillefontaine (three boisseaux of wheat, five of oats, *apud Boscum Hugonis*), ratified by Archbishop Rotrou of Rouen; and the 1195 Manassès de Bully one-*muid*-of-oats endowment from the Boshyon mill for a perpetual altar lamp before St Hildevert's relic at the Gournay collegiate church. The parish church of Saint-Michel was given to the Gournay chapter by a sire de Gournay in the twelfth century; the chapter held the patronage until 1623.",
    "siteName": "Église Saint-Michel de Bosc-Hyons",
    "streetAddress": "",
    "extantStatus": "commune extant; church reduced to succursale in 1826",
    "extantStatusDescription": "Bosc-Hyons remains a distinct commune in the canton of Gournay (Seine-Maritime). The medieval parish church of Saint-Michel was reduced to a succursale (subordinate parish chapel) in 1826 after a long medieval and early-modern history as an independent parish. Decorde reports the church under the patronage of Saint Michel, with the tower in twelfth-century Romanesque style: *'L'aspect du clocher annonce une construction du XIIe siècle.'* The medieval parish also contained the named hamlets *les Carreaux* and *le Bus*, plus the *grange du Mont-Rôti* — a farmstead owned by Mortemer Abbey, paying the Gournay chapter seven *muids* of grain (half wheat, half oats) until commuted in 1243 to seven *livres parisis* in cash.",
    "coordinateBasis": "GPS coordinate for modern Bosc-Hyons (INSEE 76124); verified against Cartes France / db-city / Archives départementales 76",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "https://www.archivesdepartementales76.net/archive/catalogue/communes76/bosc-hyons/n:168",
    "heritageLabel": "Archives départementales 76 — Bosc-Hyons commune dossier",
    "reviewNotes": [
      "The deep-research synthesis from 2026-04 misread 'Mont-Rôti' (a medieval Mortemer-abbey grange within the Boshyon parish, recorded by Decorde) as a modern locality 'Mont-Bôty / Mont-Bosy.' That misreading is corrected here; Boshyon's modern continuator is Bosc-Hyons commune, not an Ernemont-la-Villette / Avesnes-en-Bray sub-hamlet.",
      "Bosc-Hyons is the most economically substantive direct-line Gournay landholding documented in Decorde for the eleventh and twelfth centuries; promote into the older Gournay core overlay layer in the v43 overlay refresh."
    ]
  },
  {
    "placeId": "place-cottentray-avesnes-en-bray-normandy-france",
    "placeName": "Cottentray (Avesnes-en-Bray), Normandy, France",
    "longDescription": "Hamlet in the modern commune of Avesnes-en-Bray, east of Gournay-en-Bray. Decorde 1861 records that until the fifteenth century the seigneury of Cottentray was held in parts and that one quarter-fief descended from the senior Gournay barons before Marie de Bourbon sold it to the Potin family. In 1682 labourers turned up eight to ten stone tombs in a Cottentray field known locally as the Clos des Anglais; no inscription survived.",
    "siteName": "Cottentray (hamlet of Avesnes-en-Bray)",
    "streetAddress": "",
    "extantStatus": "hamlet / fields extant; tombs no longer locatable",
    "extantStatusDescription": "The hamlet of Cottentray is preserved within Avesnes-en-Bray as fields and woods east of Gournay-en-Bray. The 1682 tomb discovery field has no surviving marker. The medieval Gournay quarter-fief is no longer a distinct holding; the Potin family of the fifteenth century later succeeded to the share.",
    "coordinateBasis": "Same coordinate as the existing v5 overlay anchor anchor_avesnes_en_bray_gournay_dependency_context",
    "imageUrl": "",
    "imageTitle": "",
    "heritageUrl": "https://www.archivesdepartementales76.net/archive/catalogue/communes76/avesnes-en-bray/n%3A168",
    "heritageLabel": "Archives départementales 76 — Avesnes-en-Bray commune dossier",
    "reviewNotes": [
      "The coordinate is commune-level rather than hamlet-precise; consider tightening to the modern Cottentray hamlet location in a future overlay refresh.",
      "The 1503 Avesnes fief language already noted on the Avesnes-en-Bray overlay anchor reinforces Cottentray as part of the wider Avesnes-Ferrières western dependency rather than a separate fief; the quarter-fief language belongs specifically to Cottentray."
    ]
  }
```

### 6.3 `data/places.json` validation posture

After insertion, Phase 2 should confirm:

- the file remains valid JSON;
- the three new `placeId` values are unique;
- the three new `filename` values match the new research files in `research/places/`;
- the new records do not break any consumer that walks the file (`tools/normalize_places_v1.py` if still in use; site builders under `site/website/_data/`).

---

## 7. Ancestor data linkage (`data/ancestors v26.json`)

The new place records add Boshyon as a direct-line Gournay landholding that should appear under the place-references for G33 Hugh de Gournay III. The senior collateral references (Bellosanne foundation by Hugues V; Cottentray quarter-fief into the 15th century) sit outside the direct line and should **not** be added to direct-line ancestor `placeRefs`.

Add a `placeRefs` entry for Boshyon to `ancestor-g33-hugh-de-gournay-iii` in `data/ancestors v26.json`, modeled on the existing `placeRefs` shape for Gaillefontaine on that record. If the schema's `placeRef` entry requires a `sourceId`, use `decorde-essai-canton-gournay-1861`; if it requires a date range, use the Decorde-attested 1082 charter year. Do not invent fields.

If the existing `placeRefs` shape on the G33 record cannot accommodate the Boshyon entry without schema invention, drop this step and rely on `place-bosc-hyons-boshyon-normandy-france`'s `ancestorLinks` block alone.

---

## 8. Region / overlay implications

The existing v5 GeoJSON at `research/geo/gournay_norman_holdings_recommended_overlay_v5_source_informed.geojson` and its website mirror at `site/website/assets/data/gournay-norman-holdings-overlays.geojson` already cover most of the institutional and dependency geography this patchset touches. **No overlay redraw is performed in this patchset.** What follows is a punch list for the next overlay refresh, to be done in a separate Phase 1 against the overlay file.

### 8.1 Anchors already present — no change needed

- `anchor_abbaye_notre_dame_de_bellozanne_institutional` at (1.611111, 49.505556) already maps the Bellosanne foundation; the v42 `place-bellosanne-abbey-bremontier-merval-normandy-france` record is the canonical place pair to that anchor.
- `anchor_bremontier_merval_bellozanne_institutional`, `anchor_saint_lucien_bellozanne_patronage`, `anchor_le_thil_riberpre_bellozanne_patronage`, and `anchor_elbeuf_en_bray_bellozanne_institutional` already populate the Bellozanne patronage finger.
- `anchor_avesnes_en_bray_gournay_dependency_context` at (1.6733, 49.4697) already maps the Avesnes / Cottentray dependency; the v42 `place-cottentray-avesnes-en-bray-normandy-france` record sits at the same coordinate and can be cross-linked to the same anchor in metadata.

### 8.2 Anchors that should be added in the next overlay refresh

- **Boshyon / Bosc-Hyons (`Boscus Hugonis`) anchor.** Boshyon is not on the v5 overlay. It is the most substantive direct-line Gournay landholding documented by Decorde — woodland, manor, and mill, revenue base for the 1082 Jumièges charter, the 1164 Gaillefontaine endowment, and the 1195 Manassès de Bully lamp endowment. The modern continuator is Bosc-Hyons (Seine-Maritime, INSEE 76124) at 49.446 N, 1.659 E, south-south-west of Gournay-en-Bray. It belongs in the older Gournay core layer.
- **Refinements at the existing Bellosanne and Avesnes anchors.** Cross-reference the new canonical place records and the Hugues V founder attribution in anchor metadata. No coordinate change.

### 8.3 Polygon implications

- **Direct frontier corridor / older core layer.** Adding Bosc-Hyons (Boshyon) expands the documented inner-domain revenue base south-south-west of Gournay-en-Bray. The next overlay refresh should consider whether the older Gournay core polygon already covers the Bosc-Hyons point (49.446 N, 1.659 E) or whether a small south-south-westward extension to the polygon is justified.
- **Western dependency / Avesnes-Ferrières layer.** The Cottentray quarter-fief survival into the fifteenth century is a tail-end fragment under Avesnes; it reinforces, but does not expand, the existing Avesnes / Ferrières western dependency context. No polygon change.
- **Institutional / senior-collateral layer.** Bellosanne is already in this layer. No polygon change.
- **24-village Beauvaisis block.** Unaffected by this patchset. Decorde's 24-village Beauvaisis material is already promoted in `research/places/beauvaisis-frontier-acquisitions.md`.

### 8.4 Queue this as a separate Phase 1

The overlay refresh — adding the Bosc-Hyons / Boshyon anchor at the verified coordinate (49.446 N, 1.659 E), updating anchor metadata for Bellosanne and Avesnes to reference the new canonical place records, and rebuilding the website mirror at `site/website/assets/data/gournay-norman-holdings-overlays.geojson` — is queued as a separate Phase 1 patchset (`v43-overlay-refresh-bosc-hyons-and-decorde-cross-references.patchset.md`). Do **not** redraw polygons in this Phase 2.

---

## 9. Archive / cleanup operations

The Decorde deep-research-report has already been moved to `sources/intake/done/` in the prior audit step. The corpus_supplement copy created in §2.1 keeps a working extract layer available for future research footnotes. No further archive operations are required for this patchset.

---

## 10. Unresolved

- The Bellosanne foundation date (1198 vs. 1193) is not resolved here; the body uses 1198 with a parenthetical 1193 alternate. A later patchset can pull the Bremontier-Merval municipal source and the OpenEdition table to fix the date.
- The Decorde dating of the Hugues IV Bec confirmation (1112 or 1122) is given as a Decorde-attested range; verification against the original Bec cartulary text is out of scope.
- Hugues V's 1190 Acre crusade attestation is left as standard reference-work context rather than a Decorde-primary claim; if a direct chronicle citation is wanted it should be picked up in a later patchset targeting the senior baron-line collateral file.
- No new fact sheet is created for Hugues IV or Hugues V; both remain at the topic level. If the repo later decides to publish collateral fact sheets for the senior line, the §5.1 topic file is the natural seed.
- The Bosc-Hyons coordinate in `data/places.json` is high-precision (49.446 N, 1.659 E, verified against modern commune gazetteers). The overlay refresh in v43 can use this point directly.
- The `ancestor-g33-hugh-de-gournay-iii` `placeRefs` addition for Boshyon (§7) is conditional on the existing `placeRefs` shape; Phase 2 should drop the addition rather than invent schema fields.
- The collateral `recordId` strings used in the new `places.json` `ancestorLinks` (e.g., `collateral-hugues-iv-de-gournay`) are conventional placeholders. If the schema does not already carry collateral-line `recordId` values, omit those `ancestorLinks` entries rather than add new direct-line keys.
