**Done:** 2026-05-25 23:59 PT

# Intake patchset v60 — FMG MedLands Normandy/Caux Gournay section: coverage audit + footnote-source lead catalog

**Prepared:** 2026-05-25
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation). **Status:** Draft patchset for review. **Do NOT apply until approved.**
**Origin:** User-supplied URL `https://fmg.ac/Projects/MedLands/normacre.htm`, with directive to (a) validate that all high-value ancestor and property content from this page has been extracted into the applicable research location, and (b) treat the page's footnoted citations as a catalogue of potential expansion leads — favoring sources whose broader content extends beyond what FMG quotes, with explicit online-availability tags per `.claude/rules/continual-improvement.md`. Updated within the same intake session after user query: the highest-priority single lead identified in §3 (the bulk catalogue) was Delisle and Berger, *Recueil des actes de Henri II*, **Tome II** (1920) — the source flagged to close seven open FMG citations. User asked whether Tome II was already in repo and, if not, to explore it. Tome II is **not** in repo (repo only holds Tome I as `sources/media/recueildesactesd01grea.pdf`). Tome II PDF was fetched from Internet Archive (`recueildesactesd02grea`, 28 MB, 22 517-line `pdftotext -layout` extract) and searched for every FMG Gournay-related act. The findings are integrated as new INCLUDE blocks §4–§7 below.
**Prerequisite:** None. `fmg-medlands-normacre` already exists in `data/sources.json` (entry at line 2497). One new `sourceId` is proposed here: `recueil-actes-henri-ii-delisle-berger-vol-2` for Tome II (parallel to the existing `recueil-actes-henri-ii-delisle-berger-vol-1`).

## Decision summary

The FMG MedLands "SEIGNEURS de GOURNAY" section (Chapter 3, Caux, Section E; page-text lines 4690–5148 of the cp1252→UTF-8 strip of `normacre.htm`) was extracted in full and cross-walked against the existing G32–G37 research companions (plus the senior-line collateral topic file). **The repo is broadly deeper than FMG on every direct-ancestor generation G32 through G37 except for three small, specific collateral-context items at G32's senior-line continuation.** The page's principal residual value is its footnote bibliography (entries [902]–[998]), which names twenty-plus underlying primary and high-grade secondary sources whose own coverage usually extends far past the single quotation FMG draws from each. The bulk of this patchset catalogues those leads with online-availability tags so the user can decide which to pursue immediately.

| # | FMG content block | Already in repo? | Decision |
|---|---|---|---|
| 1 | Section intro: Rollo grant (Eudes), 24 Beauvaisis parishes [1078], vassal-of-France framing | Yes — G37 §2, G36, G33 §5.5, `research/places/beauvaisis-frontier-acquisitions.md` | **EXCLUDE** |
| 2 | EUDES [902], [904], [905] | Yes — G37 §2 (deeper than FMG: Cordier MS, écu-noir tradition, Lorraine-source rejection) | **EXCLUDE** |
| 3 | [HUGUES de Gournay (bracketed son of Eudes)] [905] | Yes — G37 §3.1 (FMG itself brackets this figure) | **EXCLUDE** |
| 4 | RENAUD + ALBERADE, sons HUGUES [I] de Gournay and GAUTHIER de la Ferté [906]–[908] | Yes — G35 §2 (deeper: NRP-I 1852 fuller witness list with Robert Archbishop, Duke Richard II, Bishop Hugues; Raoul third son; Delisle critique) | **EXCLUDE** |
| 5 | HUGUES [I] de la Ferté and HUGUES [II] de la Ferté (Sigy foundation [1030/35]; pre-6 Mar 1047 confirmation) [909]–[910] | **Partial** — la Ferté collateral noted in G35 §3.1; Sigy foundation not in repo as la Ferté-collateral monastic patronage | **INCLUDE small** — surface Sigy as a la Ferté-collateral monastic foundation in `senior-gournay-baron-line-collateral.md` (see §1 below) |
| 6 | HUGUES [II] de Gournay [911]–[915] — 1035 expedition, 1053 Robert d'Eu, [1060] Brenerias, 1066 Hastings, 1074 Cardiff | Yes — G34 §2–§6 (deeper: Powell 1584 fifth tradition; Lorraine source; Dumoulin; Wace verbatim; Pattou stack) | **EXCLUDE** |
| 7 | HUGUES [III] de Gournay [916]–[927] — [1040] Jumièges Havoth (misdated), 1066 Wace, 1067 Saint-Benoît-sur-Loire, [1073] Marmoutier, Domesday Essex (Liston/Ardleigh/Fordham), Bec [1181/89], Basilia / Anselm letter / *Chronicon Beccensis* | Yes — G33 §2, §5, §6, §7 (deeper: Saint-Nicaise de Meulan priorate 1092; Anfrede/Ansfride; Caister + Saint-Hildevert link; 1079 Gerberoi mediator; Lorraine-source garbling) | **EXCLUDE** |
| 8 | GUILLAUME de Gournay (1082 Caen Trinité co-witness) [928] | Yes — G33 §6.2 / G32 §2.1 | **EXCLUDE** |
| 9 | GERARD de Gournay [929]–[940] — Jumièges Havoth, 1082 Caen, [1089/90] Orderic castle delivery, [1089] Écouché, Albert/Baudry/Jumièges crusade death, Bec [1181/89], Edith de Warenne marriage | Yes — G32 §2 (broader and deeper: St-Sauveur 1104 *terminus post quem*; Beauvais 8 May obit; St-Wandrille; Britolio dispute; Decorde 1112/22 Bec confirmation; Clay EYC vol. 8; Actes Henri II vol. 1 Edwa attestation; RHGF vol. 15 Suger letter on Drogo II) | **EXCLUDE** |
| 10 | [AMICIE de Gournay] [941]–[944] — Talbot marriage, Plessis 1118 episode | Yes — G32 §3.2 (deeper: case-file-grade alternatives; FMG canvases the three parentage options) | **EXCLUDE** |
| 11 | HUGUES [IV] de Gournay first-mention block [945] | Yes — G32 §7 children table; `senior-gournay-baron-line-collateral.md` | **EXCLUDE** |
| 12 | GUNDRED de Gournay × Nigel d'Aubigny [946]–[951] — 1118 marriage, 1130 Pipe Roll, Whitby + St Leonard's York donations | Yes — G32 §7 children table (the Dugdale charters are mentioned but the specific *Monasticon* page references and the Whitby endowment have not been transcribed; this is collateral) | **EXCLUDE** (no direct-ancestor gap; the *Monasticon* citations are catalogued as leads in §3 below) |
| 13 | [HAWISE de Gournay] [952] — 1112 Inglishcombe to Bermondsey | Yes — G33 §8 (treated as more likely Somerset-cadet-line Hawise) | **EXCLUDE** |
| 14 | HUGUES [IV] de Gournay detailed block [953]–[963] — 1116 St Albans Biscot witness, Saint-Sauveur confirmation for Beatrice + Hugh, 1144 Saint-Leu d'Esserent for Beatrice, 1149 Lannoy charter, Sigy transfer, Clairruissel foundation, Red Book 1172 (12 knights), 1173 Diceto father-and-son capture, [1172/78] Bec Pré-de-Rouen | **Partial** — Clairruissel, Diceto 1173, and Red Book 1172 are in the senior-line topic; **the 1149 Lannoy witness, the 1116 St Albans Biscot witness, and the Sigy-transfer charter are not** | **INCLUDE small** — append to `senior-gournay-baron-line-collateral.md` (see §1 below) |
| 15 | BEATRIX de Vermandois [964]–[967] (first wife of Hugues IV) | Yes — `senior-gournay-baron-line-collateral.md` (identification via Pattou + adjacent reference works) | **EXCLUDE** |
| 16 | MELISENDE de Coucy [968]–[970] (second wife of Hugues IV) | Yes — `senior-gournay-baron-line-collateral.md` (Mélisende-as-Coucy identification via Cawley; Gaillefontaine dower via Actes Henri II vol. 1) | **EXCLUDE** |
| 17 | HUGUES (-young) [971]–[972], GERARD (-young) [973], HUGUES [V] [974]–[986] — Bellosanne 1198, Fécamp 1202, Testa de Nevill [1208/10], Red Book 1210/12, 9 Sep 1214 Close Rolls illness/heir, Annales Dunstable Templar 1213 in Poitou, Bellosanne obit 25 Oct | Yes — `senior-gournay-baron-line-collateral.md` §"Hugues V" (deeper: TNA DL 42 Richard I Canville witness; 1202 King John Carta Gilde Telariorum at Gournay; 1190 Acre crusade; 1198 Bellosanne; 1200 Saint-Aubin) | **EXCLUDE** |
| 18 | JULIANE wife of Hugues V (per the Tresgoze letter pedigree, *Vitis Calthorpiana* Harl. MS 970) [985], [988] | Not in repo — collateral wife of a collateral baron; the same Tresgoze letter is the source for the next-generation MELISENDE de Gournay marriage to Amaury de Montfort Comte d'Evreux | **EXCLUDE** — direct-ancestor irrelevance, but the Harl. MS 970 letter is catalogued as a lead (see §3 below) |
| 19 | GERARD de Gournay (eldest son, [9 Sep 1214/22 Apr 1216]) [987]; MELISENDE de Gournay × Amaury [VI] de Montfort Comte d'Evreux then William [III] de Cauntelo [988]–[990] | No — collateral senior-line continuation post-1202 exile | **EXCLUDE** |
| 20 | HUGUES [VI] de Gournay of Mapledurham (d. 1239) [991]–[994], including the Lucy / Berkeley remarriage (Smyth, *Lives of the Berkeleys*) and the William Bardolf / Juliana de Gurnay marriage IPM | Not in repo — Mapledurham branch is the post-1202 English residue of the senior line, not a direct ancestor | **EXCLUDE** — but the Mapledurham branch's English-tenure sources are themselves leads for the senior-line story (see §3 below) |
| 21 | The collateral --- de Gournay × Aveline de Noerey + GUILLAUME de Gournay × Helisende (Notre-Dame de Paris cartulary 1200) [995]–[998] | Not in repo — small French-collateral branch, no documented direct-ancestor link | **EXCLUDE** |
| 22 | Brief later mentions in adjacent FMG sections: Henri d'Eu 1118 arrest at Rouen with Hugues de Gournay, "thrown into fetters" (Orderic, Chibnall vol. VI Book XII p. 191) [1524]; Saint-Hildebert de Gournay-en-Bray as endowment target of the Marigny / Saint-Léger / Portier families [1080]–[1088] | Partial — the 1118 fetters episode is **not in repo** (G32 §3.2 has the Plessis castle capture but stops there); the Saint-Hildebert endowment-target framing **is** covered at `research/places/collegiale-saint-hildevert-gournay.md` | **INCLUDE small** — surface the 1118 fetters episode in `senior-gournay-baron-line-collateral.md` (see §1 below) |

**Three small INCLUDEs from MedLands itself (§1–§2); one NEW topic file cataloguing the source-lead bibliography (§3); four ADDITIONAL INCLUDE blocks from the Tome II exploration (§4–§7) with one new sourceId (§8).**

The audit's headline finding: the repo's existing G32–G37 companions already preserve every direct-ancestor primary-source extract that FMG MedLands quotes, usually with deeper context and additional independent attestations. The remaining gaps from MedLands itself are all collateral senior-line continuation items (Hugues IV / Sigy / Lannoy / 1118 fetters). The Tome II exploration then surfaced one substantively new direct-ancestor finding (the Hugues IV continuing-Bec donation from Basilea's Écouché maritagium, attested 1181–89), plus three Hugues IV / Hugues V witness attestations, plus the Sigy founder identification — all preserved as INCLUDEs §4–§7 below.

---

## 1. INCLUDE — `senior-gournay-baron-line-collateral.md` — three small Hugues-IV-era additions

Append a new sub-section to `research/topics/senior-gournay-baron-line-collateral.md` after the existing "Hugues IV de Gournay (c. 1098 – c. 1180)" block (before the "Hugues V de Gournay" block). Find the line ending with "[^decorde-hugues-iv-death]" and append, in the same flow:

```
### Documentary attestations beyond Decorde

Three further mid-twelfth-century attestations of Hugues IV survive in the FMG MedLands footnote bibliography and the cited primary sources, none of them in Decorde or in the direct-line companions for G32/G33.

- **1116 St Albans Biscot witness.** Matthew Paris quotes a charter dated 1116 in which Henry I King of England granted Biscot, Bedfordshire, to the abbey of St Albans, with the witness list "Adam de Port, Thomas de Sancto Johanne, Willelmus frater eius, Hugo de Gornaio."[^matthew-paris-1116-biscot] This is the earliest datable post-minority appearance of Hugues IV after Henry I "raised him *ut filium*" and "of full age in 1112" (G32 §12). Hugues IV sits in elite Anglo-Norman court company at the king's confirmation to the kingdom's premier Benedictine house.
- **1118 arrest at Rouen — "thrown into fetters" with Henri d'Eu.** Orderic Vitalis records that Henri Comte d'Eu, who in 1118 supported the rebellion of Guillaume "Clito" de Normandie against Henry I, "was arrested at Rouen with Hugues de Gournay, thrown into fetters and forced to surrender his castles."[^orderic-1118-rouen-fetters] This is the immediate sequel to the rebellion narrative already preserved at G32 §3.2 (Hugo filius Girardi de Gornaco captured Plessis castle and granted it to his nephew Hugh Talbot per Orderic). The Plessis capture was the offensive moment; the Rouen arrest and forced castle-surrender was the resolution. Hugues IV's senior-baron status survived: he held Gournay through to his death c. 1180, and the 1118 episode is the only known direct break in his sixty-plus-year tenure.
- **1149 Lannoy charter — Pays-de-Bray monastic witness.** Hugues IV subscribed the 1149 charter of Henri Bishop of Beauvais confirming the donation of "territorii veteris Briostel" to Lannoy abbey (Notre-Dame-de-Lannoy, the Cistercian house founded 1137 in the Pays-de-Bray near Beauvais) — the gift being made by "Drogo filius Roeri et mater eius Isabelt." The witness list opens "Helias et Petrus vicedomini Gerbosreti, Hugo de Gornaco."[^lannoy-1149-charter] The witness ordering — the *vicedomini* of Gerberoy first, then Hugues — places Hugues IV in the Beauvais–Gerberoy regional monastic network in the same decade as the Bec confirmations and the Clairruissel and Saint-Leu d'Esserent foundations, sharpening the senior-line's Pays-de-Bray ecclesiastical footprint with one further regional house.

### Sigy priory — la-Ferté-collateral foundation, transferred by Hugues IV

The priory of Sigy was founded by "Hugues" of the la-Ferté collateral branch by charter dated to [1030/35], with the foundation confirmed by his son "Hugo Hugonis Firmentis filius" by charter dated before 6 Mar 1047. The la-Ferté-line founder is FMG's distinct figure "HUGUES [I] de la Ferté" (FMG #3 of the Renaud-branch list, possibly but not provably son of Gauthier de la Ferté G35's brother), and the son is "HUGUES [II] de la Ferté," who became a monk at St Ouen, Rouen.[^sigy-foundation-la-ferte] Sigy passed to the senior Gournay line by some twelfth-century inheritance not documented in surviving record, and Hugues IV de Gournay later transferred the priory to a new site by an undated charter of Henry II.[^sigy-transfer-hugues-iv] The site is at Sigy-en-Bray (modern commune, Seine-Maritime, INSEE 76685), within twelve kilometres of Gournay-en-Bray. The Sigy / Gournay relationship belongs to the same regional ecclesiastical-foundation network as Bellosanne, Clairruissel, and Gaillefontaine, and rounds out the senior-line monastic footprint with a Cluniac-tradition priory pre-dating Bellosanne by more than a century.

[^matthew-paris-1116-biscot]: Matthew Paris quotes the 1116 charter of King Henry I granting Biscot, Bedfordshire, to St Albans Abbey, with witness list including "Hugo de Gornaio." Cited in *Matthaei Parisiensis, monachi Sancti Albani, Chronica Majora*, ed. Henry Richards Luard, Rolls Series 57 (London, 1872–1883), vol. VI (*Additamenta*), 22, p. 36, per Charles Cawley, *Medieval Lands*, footnote [954] in the SEIGNEURS de GOURNAY section. Standard edition available online at archive.org; the *Gesta Abbatum Monasterii S. Albani* (Rolls Series 28, 1867–1869, ed. H.T. Riley) gives a fuller St Albans-house chronicle context for the same charter. Source ID: `fmg-medlands-normacre`.
[^orderic-1118-rouen-fetters]: Orderic Vitalis, *Historia Aecclesiastica*, ed. and trans. Marjorie Chibnall, vol. VI: *Books XI–XIII* (Oxford: Clarendon Press, 1978), Book XII, p. 191, per Charles Cawley, *Medieval Lands* footnote [1524] in the Comtes d'Eu section. The Plessis capture episode at G32 §3.2 is Orderic Book XII p. 318 (Prévost ed.); the Rouen arrest is the immediate sequel. Source ID: `fmg-medlands-normacre` (Cawley as transmitting reference); `orderic-vitalis-chibnall-vol-6` (primary text).
[^lannoy-1149-charter]: 1149 charter of Henri Bishop of Beauvais for Notre-Dame de Lannoy, in *Cartulaire de l'abbaye Notre-Dame de Lannoy*, Tome X, charter XIV, p. 639, per Charles Cawley, *Medieval Lands* footnote [957]. The "Tome X" placement suggests Cawley is citing the abbey cartulary as published in a regional charter-collection series (likely *Mémoires de la Société Académique de l'Oise* or an adjacent Beauvais-region historical-society publication). The cartulary edition has not yet been verified directly. Source ID: `fmg-medlands-normacre`.
[^sigy-foundation-la-ferte]: Sigy priory foundation [1030/35] by "Hugo" of the la-Ferté collateral and confirmation pre-6 Mar 1047 by "Hugo Hugonis Firmentis filius" (his son, monk at St Ouen Rouen), per Charles Cawley, *Medieval Lands* footnotes [909]–[910], citing Daniel Gurney, *Record of the House of Gournay* (1845), p. 32, quoting *Gallia Christiana*, Vol. XI, p. 12 (for the foundation), and the archives of Rouen (for the 1047 confirmation). Source ID: `fmg-medlands-normacre`.
[^sigy-transfer-hugues-iv]: Sigy priory transfer to a new site by Hugues IV de Gournay per an undated charter of Henry II King of England, per Charles Cawley, *Medieval Lands* footnote [958], citing Daniel Gurney, *Record of the House of Gournay* (1845), p. 35, quoting *History of the Abbey of St Ouen at Rouen*, p. 463. The Henry II charter is presumably one of those in Delisle and Berger, *Recueil des actes de Henri II* (vols. I–III); not located in vol. 1 in the user-supplied PDF at `sources/media/recueildesactesd01grea.pdf` (closed in v55–v59 work on G32–G33); a vol. II or III check would resolve the indexing. Source ID: `fmg-medlands-normacre`.
```

No new `sourceId` is required for §1; all four new footnotes anchor to existing `fmg-medlands-normacre` (with `orderic-vitalis-chibnall-vol-6` as secondary anchor for the fetters footnote).

---

## 2. INCLUDE — `research/places/collegiale-saint-hildevert-gournay.md` — Marigny endowment-target framing

The Saint-Hildebert (Saint-Hildevert) collegiate church at Gournay-en-Bray is already covered in the repo's place file (existing). The FMG MedLands page's lines 5630–5667 add a layer the current place file does not have: the church received recurring donations from the Marigny / Saint-Léger / [le] Portier families of the next generation after the 1202 Capetian conquest, documented by undated charters of Richard de Saint-Léger and Mathilde [de Marigny], the 1209 exchange charter of Hugues le Portier, and the Apr 1240 confirmation by Enguerrand [I] le Portier de Marigny.[^marigny-saint-hildevert-donations]

This is **place-level data, not direct-ancestor data**: the Marigny / Portier line is unrelated to the Gournays by blood. It documents that Saint-Hildebert continued to receive baronial endowments from neighbouring Pays-de-Bray houses after the senior Gournay barony was extinguished as a territorial power. Append a one-paragraph note in the place file's "Post-1202 endowment continuity" subsection (or, if no such subsection exists, append at the end of the body before the footnotes):

```
After the 1202 Capetian conquest stripped the senior Gournay line of its seat, Saint-Hildebert continued to receive baronial endowments from neighbouring Pays-de-Bray and Vexin houses. The Marigny / Saint-Léger / Portier (later Marigny) family, lords of Marigny and Dampnopetro in the Vexin and tenants in the Lyons area, made four documented gifts to Saint-Hildebert across the late twelfth and earlier thirteenth centuries: an undated charter of Richard de Saint-Léger and his wife Mathilde donating revenue from Marigny and Dampnopetro; an undated confirmation of the same by Hugo Portarius (Hugues le Portier), Mathilde's second husband; a 1209 confirmation by Hugues le Portier with the consent of his wife Mathilde and son Ingerrannus; and an Apr 1240 confirmation by Enguerrand [I] le Portier de Marigny (the eponym of the future royal-financier Marigny line).[^marigny-saint-hildevert-donations] The continued attraction of Saint-Hildebert as an endowment destination after the senior barony's collapse documents the chapter's institutional persistence past the conquest: Gournay-en-Bray's central religious institution outlived the territorial barony that founded it.
```

```
[^marigny-saint-hildevert-donations]: Documented by four charters quoted in Charles Cawley, *Medieval Lands*, Normandy section, Marigny/Portier sub-block (Chapter 6, Vexin-Beauvaisis, page text around l.5630–5667 of the section): the undated charter of "Richardus de Maregny et Matildis uxor mea et Petronilla filia mea" (footnote [1080]); the undated confirmation by "Hugo Portarius" (footnote [1081]); the 1209 exchange charter of "Hugo Portarius" with the church of Lyons Saint-Laurent (footnote [1082], "consentiente Matildis uxoris mea et Ingerrani filii mei"); the Apr 1240 confirmation by "Ingeranus de Marreigny" (footnote [1088]). The Marigny / Saint-Léger / [le] Portier family is unrelated to the Gournays by blood but illustrates Saint-Hildebert's persistence as a regional endowment target after 1202. Source ID: `fmg-medlands-normacre`.
```

No new `sourceId` is required.

---

## 3. NEW topic file — `research/topics/medlands-gournay-source-leads.md`

The principal deliverable for the user's "looking for sources that could be leads to expand the research" directive. This topic file catalogues every distinct primary or high-grade-secondary source named in the FMG MedLands "SEIGNEURS de GOURNAY" footnote block ([902]–[998]), with an online-availability tag per `.claude/rules/continual-improvement.md`, and a one-line annotation pointing to where the source's *broader* content extends past the single FMG quotation it supports. The intent is operational: any future research session that wants to deepen a particular Gournay sub-question can scan this file and immediately identify which sources are reachable today, which require library access, and which would, when fetched in full, deliver substantially more than what FMG already extracted.

Create at `research/topics/medlands-gournay-source-leads.md` with full body:

```
# Source leads from the FMG MedLands Gournay section

Catalogue of every distinct primary or high-grade secondary source named in the SEIGNEURS de GOURNAY footnote block ([902]–[998]) of Charles Cawley's *Medieval Lands* Normandy page (`https://fmg.ac/Projects/MedLands/normacre.htm`), with online-availability tag and a note on where the source's broader content extends past the single quotation Cawley extracted.

The catalogue is organised by source type. Each entry shows: FMG footnote numbers, full citation, online-availability tag (`Available online` / `Unknown online` / `Not online`), URL when verified, and the source's broader-content scope relative to the Gournay-specific extract.

The entries are not in priority order; they are the underlying source bibliography for the senior Gournay line c. 911 – c. 1240 as Cawley assembled it, surfaced here so any future Gournay-deepening session can pick from one consolidated list.

## A. Primary medieval chronicles and charters in published critical editions

1. **Orderic Vitalis, *Historia Aecclesiastica*, ed. A. Le Prévost (Société de l'Histoire de France, 5 vols., 1838–1855)** — FMG [933, 934, 941, 942, 945, 947, 1943]. *Available online* — Internet Archive holds all five Prévost volumes; vol. III (Books VII–IX) contains the [1089/90] castle-delivery and the [1089] Écouché passages and is the locus of nearly every direct G32 attestation. The Prévost edition is superseded for scholarly use by the Chibnall Oxford Medieval Texts edition (1969–1980) but Prévost remains the default citation in FMG. **Broader-content scope:** Books VII–XIII contain the entire Anglo-Norman political history of c. 1075–1141 — every Gournay-adjacent figure (Henri d'Eu, Robert d'Eu, William de Warenne, Stephen of Aumale, Robert Curthose, Henry I) has multiple attestations beyond what FMG extracted for the Gournay section. Already used heavily in G32–G34 companions. The next deepening pass on Hugues IV or Gundred's Aubigny marriage would draw directly from Books X–XII.

2. **Orderic Vitalis, *Historia Aecclesiastica*, ed./trans. Marjorie Chibnall (Oxford Medieval Texts, 6 vols., 1969–1980)** — FMG [948, 1524, 1888, 1891], plus heavy repo use at G32 §13. *Available online* — vol. V (Books IX–X) and vol. VI (Books XI–XIII) digitised at archive.org; the full set is also at OUP Scholarly Editions Online (paywall). **Broader-content scope:** the Chibnall edition supersedes Prévost with modern Latin text and facing English translation. Book XII (vol. VI) contains both the 1118 rebellion Plessis-and-fetters sequence (Hugues IV) and the 13-year imprisonment material relevant to the wider Eu / Gournay arrest network. Already in repo source set as `orderic-vitalis-chibnall-vol-6`.

3. **Guillaume de Jumièges, *Historiæ Normannorum Libri VIII* (Duchesne, *Historiæ Normannorum Scriptores Antiqui*, Paris 1619)** — FMG [922, 938, 940, 946, 965, 971, 1887, 1890, 1894]. *Available online* — Google Books has the Duchesne 1619 edition; Internet Archive has the Marx 1914 critical edition; Elisabeth van Houts's *Gesta Normannorum Ducum* (Oxford Medieval Texts, 2 vols., 1992–1995) is the modern critical edition with English translation, behind the Oxford paywall. **Broader-content scope:** Jumièges Liber VIII covers the post-1066 generation with named attestations of multiple Gournay figures (Hugues III, Basilea, Gerard, Edith, Hugues IV's first marriage to Beatrix de Vermandois, Gerard's death "in itinere"). The repo has the Duchesne 1619 quotations FMG transmits; the van Houts apparatus and notes would add modern scholarly context (van Houts vol. 2 p. 214 specifically discussed at G32 §14, Not online).

4. **Albert of Aix, *Historia Hierosolymitanae expeditionis*, in *Recueil des historiens des Croisades, Historiens Occidentaux*, vol. IV (Paris, 1879)** — FMG [936]. *Available online* — Gallica and archive.org both hold the *RHC Occ.* vol. IV. **Broader-content scope:** Albert is one of the four major First Crusade chronicles; his account of the 1097 siege of Nicaea names "Gerardus de Gorna" once in the FMG quotation but his fuller narrative of Crusader-army organisation includes adjacent Norman names that would refine the picture of Gerard's command position. The Edgington 2007 Oxford critical edition / translation supersedes for scholarly use but RHC is the FMG citation.

5. **Baudry of Dol, *Historia Hierosolymitana*, in *Recueil des historiens des Croisades, Historiens Occidentaux*, vol. IV (Paris, 1879)** — FMG [937]. *Available online* — Gallica, archive.org. **Broader-content scope:** Baudry's chronicle (composed c. 1108) is the second major First Crusade source after Albert. Like Albert, the broader command narrative is the value beyond the single "Girardus de Gornaio" attestation FMG quotes.

6. **William of Poitou (Guillaume de Poitiers), *Gesta Guillelmi ducis Normannorum et regis Anglorum*, ed. Davis & Chibnall, Oxford Medieval Texts (1998)** — FMG [912]. *Available online* (older editions) — Foreville's 1952 Belles Lettres edition is on Internet Archive; the 1998 Davis & Chibnall edition is paywalled at OUP. **Broader-content scope:** the official biography of William the Conqueror by his archdeacon-chaplain, the single most important pre-1066 ducal-court source. Beyond the "Hugonis Gornacensis…Roberti Aucensis comitis" alliance datum, Poitou is rich on the 1054 Mortemer command structure and the immediate pre-Hastings Norman magnate circle that Hugh II inhabited.

7. **Wace, *Le Roman de Rou*, in the *Extrait de la Chronique de Normandie*, in *Recueil des historiens des Gaules et de la France*, vol. XIII (1869)** — FMG [914, 917]. *Available online* — RHGF vol. XIII at archive.org and Gallica. Modern critical edition: Holden 1970–1973 (Société des anciens textes français). **Broader-content scope:** the "Hue de Gournay sire de Bray" and "le Conte Hue de Gournay" Hastings-fleet verses are already extracted at G33 and G34. The broader *Roman de Rou* contains the rich Normandy-foundation narrative (Rollo, the dukes, the 1054 Mortemer ride-through-the-night narrated at G34 §3.3) that adds context but no new Gournay names beyond the two already in repo. Use is closed.

8. **Ralph de Diceto, *Imagines Historiarum*, in *Recueil des historiens des Gaules et de la France*, vol. XIII** — FMG [962, 975]. *Available online* — RHGF vol. XIII at archive.org. Standard modern critical edition: William Stubbs, *Radulfi de Diceto Decani Lundoniensis Opera Historica*, Rolls Series 68 (London, 1876), 2 vols. — also at archive.org. **Broader-content scope:** Diceto's 1173 entry "Hugo de Gornai, tam pater quam filius" (Hugues IV and Hugues V both captured during the Young King's rebellion) is the FMG extract; the surrounding Diceto narrative of 1173–74 is the canonical Anglo-French chronicle account of that rebellion and would supply political-context detail for both Gournays.

9. **Annales de Bermondsey, in *Annales Monastici*, ed. H.R. Luard, Rolls Series 36 (1864–1869), vol. III** — FMG [952]. *Available online* — archive.org. **Broader-content scope:** the Bermondsey annal's 1112 Inglishcombe donation by Hawisia de Gurnay is the single FMG-quoted entry; the annal as a whole is a thin Southwark-priory chronicle but contains scattered Gournay-adjacent property notices.

10. **Annales de Dunstaplia, in *Annales Monastici*, ed. H.R. Luard, Rolls Series 36, vol. III (1866)** — FMG [982]. *Available online* — archive.org. **Broader-content scope:** the 1213 entry recording Hugo de Gurnaco becoming a Templar in Poitou and dying that year is one of the most striking Hugues V attestations; the wider Dunstable annals cover early-thirteenth-century English religious-house politics where Mapledurham (Hugues VI's English seat) intersected.

11. **Chronicon Beccensis Abbatiæ (1648)** — FMG [925]. *Available online* — Google Books / Gallica (the 1648 d'Achery edition or the *Patrologia Latina* vol. CL reprint). **Broader-content scope:** the Bec abbey chronicle's death-Sundays passage for Basilia + Amfrida + Eva Crispin is the single Gournay-specific extract; the wider Bec chronicle is rich on Hugues III's monastic patronage and the Anselm-era Bec network (G33 §7). Worth direct inspection for the years 1080–1110.

12. **Sancti Anselmi Opera Omnia, ed. F.S. Schmitt (Edinburgh / Rome, 1938–1968)** — FMG [924] (Anselm letter to Basilia, lib. iii ep. 138). *Available online* (older Patrologia Latina edition, PL 158–159, at archive.org); the Schmitt critical edition is in major theology libraries, partially online. **Broader-content scope:** Anselm's letter to Basilia is one of multiple Anselm letters touching the Gournay-Bec circle. The repo already uses the Schmitt-equivalent lib. iv ep. 7 and 26 references via *Neustria Pia*. A direct sweep of Schmitt for all "Hugo" / "Basilia" / "Gerardus de Gornaco" addressees would surface any further Anselm-Gournay correspondence.

13. **Chronicle of Alberic of Trois-Fontaines, *Chronica Albrici Monachi Trium Fontium*, in MGH Scriptores XXIII** — FMG [969, 1939]. *Available online* — MGH dMGH portal (`http://www.dmgh.de/`). **Broader-content scope:** Alberic's mid-thirteenth-century chronicle places "illam que data est Hugoni de Gornaio" (Mélisende de Coucy) in the Coucy succession; the surrounding chronicle is encyclopaedic on the Capetian / Plantagenet political world of the late twelfth and early thirteenth centuries and contains scattered Hugues V / Capetian-conquest material.

14. **Genealogiæ Scriptoris Fusniacensis, in MGH Scriptores XIII, p. 253** — FMG [968]. *Available online* — MGH dMGH portal. **Broader-content scope:** the Fusniacensis genealogy is the source for Mélisende as daughter of Thomas de Marle Comte d'Amiens; it is a single short pedigree text containing little beyond the FMG quotation but is the canonical primary source for the Coucy-Gournay marriage.

15. **De Genere Comitum Flandrensium, Notæ Parisienses, in MGH Scriptores, p. 257** — FMG [964]. *Available online* — MGH dMGH portal. **Broader-content scope:** the "comite Hugone et Adela uxore" daughter named only as wife of "comes Garentie" is the Hugues IV first-marriage problem; FMG flags the Warenne-vs-Vermandois ambiguity. Broader Flandrian genealogy material adjacent.

16. **Robert of Torigny, *Chronique de Robert de Torigny*** — FMG [1526]. *Available online* — Léopold Delisle's 1872–1873 Société de l'Histoire de Normandie edition at archive.org; the modern Howlett edition (Rolls Series 82 vol. IV, 1889) is also at archive.org. **Broader-content scope:** Torigny's mid-twelfth-century continuation of Sigebert of Gembloux is the canonical Anglo-Norman chronicle of the 1130s–1180s, with Gournay-adjacent material spanning Hugues IV's entire mature life.

## B. Twelfth-century royal-chancery charter editions

17. **Léopold Delisle and Élie Berger, *Recueil des actes de Henri II Roi d'Angleterre et Duc de Normandie, concernant les provinces françaises et les affaires de France*, 3 vols. (Paris, 1916–1927)** — FMG cites Tome I [1001, 1004, 1006] and Tome II [921, 927, 939, 943, 944, 963, 976]. *Available online* — Tome I at archive.org (`recueildesactesd01grea`, already in repo as `sources/media/recueildesactesd01grea.pdf` per G32 §14 v55–v59 work). Tomes II and III are at archive.org and Gallica. **Broader-content scope:** vol. II contains seven separate Gournay-relevant Henry II charters not yet in repo: the [1181/89] Bec confirmation naming the Hugues-III / Gerard donation chain (FMG [921, 927, 939]) — the same act as the G32 §2.10 extract but in primary form rather than via Decorde; the [1181/83] Valmont confirmation naming Amicie de Gournay's Talbot donations (FMG [943]); the [Mar/Jun] 1189 Sainte-Foi de Longueville charter naming Amicie de Gournay again (FMG [944]); the [1172/78] Bec Pré-de-Rouen confirmation subscribed by Hugues IV (FMG [963]); the [1182/89] Barbery confirmation subscribed by Hugues V (FMG [976]). The Sigy-transfer charter for Hugues IV (FMG [958] via Gurney 1845 p. 35) is probably also in this collection if not in vol. I. **Highest-priority single lead**: vol. II would close seven open citations in one pull.

18. **Léopold Delisle, *Histoire du Château et des Sires de Saint-Sauveur-le-Vicomte* (Valognes, 1867), Pièces justificatives** — FMG [913, 919, 1946]. *Available online* — archive.org and Gallica. **Broader-content scope:** Delisle's 1867 monograph is the foundational nineteenth-century edition of the Saint-Sauveur archive. Pièces justificatives no. 30 (the [1060] Bayeux Brenerias charter witnessed by Hugues II), no. 33 (the [1073] Marmoutier charter witnessed by Hugues III), and no. 31 (Saint-Wandrille apud Aucium) all appear here. The volume is the canonical published collection of Cotentin pre-conquest charters and would supply a far richer set of named witness-list cross-references for Hugues II and Hugues III than the single Cawley extracts.

19. **H.W.C. Davis and R.J. Whitwell, *Regesta Regum Anglo-Normannorum*, vol. I: 1066–1100 (Oxford: Clarendon, 1913)** — FMG [928, 931]. *Available online* — archive.org. Superseded for William I by David Bates, *Regesta Regum Anglo-Normannorum: The Acta of William I (1066–1087)* (Oxford: Clarendon, 1998), partially online via OUP Scholarly Editions. **Broader-content scope:** entry no. 150 (the 1082 Caen Trinité confirmation listing "William de Gornai…Girard de Gornai" as witnesses) is the FMG extract; the wider *Regesta* is the canonical hand-list of every post-Conquest William I charter, with index entries that would surface any further "Hugo de Gornai" or "Hugo de Gurniaco" witness appearances not picked up by Cawley.

20. **Joseph Hunter, *Magnum Rotulum Scaccarii vel Magnum Rotulum Pipæ de anno tricesimo-primo regni Henrici Primi*, Record Commission (London, 1833)** — FMG [949]. *Available online* — archive.org / HathiTrust. **Broader-content scope:** the 1129/30 Pipe Roll (the earliest surviving English Exchequer roll). FMG quotes the single Leicestershire entry "Gunderede uxori Nig de Albin"; the full roll has scattered Gournay-adjacent entries for the Albini / Mowbray honour and for Norfolk holdings that may not have been picked out for the Gournay section but are reachable via a standard name-index search.

21. **Hubert Hall, ed., *The Red Book of the Exchequer*, Rolls Series 99, 3 vols. (London, 1896)** — FMG [960, 980]. *Available online* — archive.org (all three volumes). **Broader-content scope:** Hugo de Gurnaio with 12 knights in [1172] (Normandy infeudations) and 3 knights' fees in Norfolk in [1210/12] are the FMG extracts; the full *Red Book* is the canonical mid-thirteenth-century Exchequer compilation of Norman and English knight-service returns, with a comprehensive index. Walter de Gournay's "Liber Niger Scaccarii" entry in G31 §3 is from a parallel Exchequer compilation (the Liber Niger Scaccarii) edited by Thomas Hearne (Oxford, 1728); the two editions are different physical books but cover overlapping material.

22. **Thomas Duffus Hardy (or successor ed.), *Rotuli de Oblatis et Finibus in Turri Londinensi asservati, tempore regis Iohannis*, Record Commission (London, 1835)** — FMG [991]. *Available online* — archive.org / HathiTrust. **Broader-content scope:** 22 Apr 1216 fine of Hug de Gurnay fil Hug de Gurnay for his Norfolk-Suffolk fees (Hugues VI's earliest documented appearance). Broader content: every fine paid to King John for relief / wardship / forest licence; the Mapledurham senior-line continuation is here.

23. **Thomas Duffus Hardy, ed., *Rotuli Litterarum Clausarum in Turri Londinensi asservati*, Record Commission (London, 1833–1844), 2 vols.** — FMG [990]. *Available online* — archive.org / HathiTrust. **Broader-content scope:** 15 Mar 1217 entry concerning Mélisende de Gournay's dower at Mapledurham / Petersfield; broader content covers the daily administrative record of John's and the early Henry III chancery.

24. **William Hardy, ed. (or Calendar of Patent Rolls Henry III 1215–1225, HMSO 1901)** — FMG [989]. *Available online* — archive.org / HathiTrust / British History Online. **Broader-content scope:** 14 Mar 1217 grant of Mapeldureham and Petersfield to Roger la Zouche; standard Plantagenet chancery enrolment.

25. *Olim*, ed. Auguste-Arthur Beugnot, *Les Olim, ou Registres des arrêts rendus par la cour du Roi sous les règnes de Saint Louis, de Philippe le Hardi, de Philippe le Bel...*, 4 vols. (Paris, 1839–1848) — FMG [986]. *Available online* — Gallica / archive.org. **Broader-content scope:** Tome I entry VIII p. 261 (1267 inquiry on Mathilde Comtesse de Boulogne's heirs, naming Matheus comte de Dammartin and several Fiennes / Picquigny figures) is the FMG extract. Walter de Gournay's case-file in `research/case-files/walter-de-gournay-as-son-of-gerard.md` references *Olim* via DG-I p. 293 as proof of Swathings-line blood descent; direct examination of Beugnot vol. I for "de Gornaco" / "de Gurnay" / "Gournay" entries would test that proof against the primary record.

26. *Inquisitions Post Mortem*, Calendar of, vol. II Edward I (Public Record Office) — FMG [994]. *Available online* — HathiTrust / British History Online. **Broader-content scope:** entry 772, 23 Dec 18 Edward I (1289), naming "Hugh Bardolf aged 30 is his next heir...the inheritance of Juliana de Gurnay his wife" — the closing entry of the Mapledurham senior line. Broader content: late-thirteenth-century English landholding compendium.

27. *Liber Feodorum* / *Book of Fees* (= "Testa de Nevill"), HMSO 1920–1931 (or Record Commission 1807 ed.) — FMG [979, 993, 435]. *Available online* — archive.org. **Broader-content scope:** the [1208/10] Buckinghamshire-Bedfordshire entry listing Hugo de Gurnay holding Wendoun de dominico domini regis and the [1226/28] Gloucestershire entry recording Lucia uxor Roberti de Berkelay married to Hugoni de Gurney are FMG extracts; the full *Liber Feodorum* is the canonical early-thirteenth-century English landholding survey.

## C. Cartulary editions

28. **Cartulary of the abbey of Jumièges (Jumièges, Tome I)** — FMG [916, 923, 929]. *Available online* — partial via Gallica (Vernier 1916 critical edition: *Chartes de l'abbaye de Jumièges, v. 825 à 1204*, 2 vols.) and Lot's earlier 1908 work. **Broader-content scope:** the [1040]-dated (probably misdated) Radulphus Havoth charter naming "Hugone Gurnacensi et filio eius Girardo et uxore eius Basilia" is the central early-G33 / G32 attestation; the wider Jumièges cartulary is a major Norman monastic source with Gournay-adjacent grants throughout the eleventh and twelfth centuries.

29. **Cartulary of Saint-Benoît-sur-Loire / Fleury, ed. Maurice Prou and Alexandre Vidier, *Recueil des chartes de l'abbaye de Saint-Benoît-sur-Loire*, 2 vols. (Paris: Picard, 1907–1932)** — FMG [918]. *Available online* — Gallica and archive.org. **Broader-content scope:** charter LXXVIII p. 203 (April 1067 William I confirmation subscribed by "Hugonis de Gornaio") is the FMG extract; the cartulary as a whole is a major Loire-region Benedictine source whose ducal-charter witness lists would supply context for Hugh II's circle.

30. **Cartulaire du prieuré de Saint-Leu d'Esserent (1080–1538), ed. Eugène Müller (Pontoise, 1900–1901)** — FMG [956, 967]. *Available online* — Gallica. **Broader-content scope:** the [1144] charter of Hugues IV donating for "Beatricis…uxoris meæ" is the FMG extract; Saint-Leu d'Esserent in the Oise valley was a Cluniac priory with deep Picard-Beauvaisis connections; the cartulary contains scattered Gournay-Mouchy-Vermandois material relevant to Drogo I de Mouchy (Edith de Warenne's second husband — G32 §10).

31. **Cartulary of Saint-Wandrille (Saint-Wandrille, Appendice)** — FMG [1940, 1941]. *Available online* — Ferdinand Lot, *Études critiques sur l'abbaye de Saint-Wandrille* (Paris: Champion, 1913) at archive.org. Older Loth edition (1872) also at archive.org. **Broader-content scope:** referenced in the Eu / Aumale section for adjacent context. DG-Supp Note 17 already preserves the Gerard de Gournay "annuente Girardo de Gournai" charter from the Saint-Wandrille chartulary (G32 §2.11); the wider cartulary is rich on Pays-de-Caux ducal-grant material.

32. **Cartulary of the priory of Clairruissel (Archives of Rouen)** — FMG [959, 970, 973, 974]. *Unknown online* — the priory cartulary appears not to be in a standalone published edition; Cawley cites it via Gurney (1845) pp. 111–2. The Rouen archives (Archives départementales de la Seine-Maritime) hold the manuscript. **Broader-content scope:** the Hugues IV + Mélisende foundation charter with consent of sons Girard and Hugues is the FMG extract; the priory's full record would expand the senior-line monastic-patronage map.

33. **Cartulary of Saint-Sauveur (M. de Gerville de Valognes possession in DG's day; now Archives départementales de la Manche, H 4838, with copy at BnF Lat. 17137)** — FMG [955, 966]. *Not online* — see G32 §14 closing on this source. Standalone published edition does not exist; only partial editions (Delisle 1909). **Broader-content scope:** the FMG extract is the [undated] Hugues IV confirmation of "Girardus pater meus" donation for Beatricis and Hugonis; the underlying 1104 roll cited by DG 1845 p. 69 is the *terminus post quem* for Gerard's death and remains the single most important physical inspection target for tightening the G32 death-date bracket (G32 §11).

34. **Cartulary of Bec / Actes Henri II Tome II DCCXLIV p. 375** — FMG [921, 927, 939]. Already covered under #17 above; the same three FMG footnotes for the Bec [1181/89] confirmation point to the same Delisle-Berger Henry II vol. II entry. *Available online* — archive.org.

35. **Cartulary of la Trinité de Caen** — FMG [928, 931] via *Regesta Regum Anglo-Normannorum* vol. I no. 150. *Available online* (older editions of Caen Holy Trinity charters). Bates 1998 *Regesta* gives the modern critical text. **Broader-content scope:** the 1082 foundation charter is the canonical primary source for William and Girard de Gornai as joint witnesses.

36. **Cartulaire de l'église Notre-Dame de Paris, ed. Benjamin Guérard, Collection de documents inédits, 4 vols. (Paris: Crapelet, 1850)** — FMG [995, 996, 997, 998]. *Available online* — Gallica. **Broader-content scope:** Tome I charter XIII p. 428 (1200 Robertus comes Drocensis confirmation of Aveline de Noerey + Guillaume de Gornaio sale at Vitriacum) is the FMG extract; this is the source for the collateral --- de Gournay / Aveline branch noted in §1 #21 above. Broader: Notre-Dame's twelfth- and early-thirteenth-century property holdings record.

37. **Cartulaire de l'abbaye Notre-Dame de Lannoy, Tome X, charter XIV p. 639** — FMG [957]. *Unknown online* — published edition probably in a Beauvais-region Société Académique series; not located in this audit. **Broader-content scope:** the 1149 Henri Bishop of Beauvais charter subscribed by Hugues IV de Gournay is the FMG extract; the full cartulary would surface any further Hugues IV Lannoy-related witnessing.

38. **Marigny / Lyons Saint-Laurent / Mortemer cartulary material** — FMG [1080]–[1092]. *Unknown online* — published cartulary editions vary. **Broader-content scope:** the Marigny / Saint-Léger / [le] Portier endowments to Saint-Hildebert de Gournay-en-Bray and the Mortemer 1268 charter of Philippe de Marigny are the FMG extracts; these are place-level continuity data for Gournay-en-Bray after 1202 (see §2 above).

## D. Chronicles via *Recueil des historiens des Gaules et de la France* (RHGF)

39. **RHGF vols. XI, XIII, XV, XXIII** — used at FMG [911 (XI), 914, 917, 962, 975 (XIII), 423 (XXIII)]. *Available online* — Gallica and archive.org hold the full *RHGF* set; vol. XV is already in repo as `sources/media/rhgf-vol15-1878.pdf` (G32 §13 closure). **Broader-content scope:** the *Recueil* is the standard nineteenth-century compilation of medieval French chronicles. Vol. XI contains the *Chronique Manuscrite de Normandie* (FMG [911], the 1035 expedition source); vol. XIII contains Wace's Hastings list and Diceto's 1173 entry; vol. XV contains Suger's Louis VII correspondence on Drogo II de Mouchy (G32 §13).

## E. Sixteenth- through eighteenth-century antiquarian editions

40. **Daniel Gurney, *Record of the House of Gournay* (London, 1845/1848), Part I + Supplement (1858)** — FMG [902]–[908], [915], [924], [926], [930], [955], [958], [959], [961], [966], [970], [972], [973], [974], [977], [978], [981], [983], [984], [985], [987], [988]. *Available online* — archive.org / HathiTrust. **Broader-content scope:** the most-cited source in the FMG Gournay section (twenty-three footnotes). Already used as the foundational source in every repo G32–G37 companion. Closed for further extraction.

41. **Père du Plessis, *Description géographique et historique de la Haute-Normandie*, 2 vols. (Rouen, 1740)** — FMG [1040], referenced indirectly at G36 §2.1 via Potin 1842. *Available online* — Gallica and archive.org. **Broader-content scope:** the eighteenth-century topographical-and-historical compendium for upper Normandy; preserves the Brito *Philippide* Latin verses and adjacent Gournay-en-Bray fortification material (G36).

42. **André Duchesne, *Histoire généalogique de la maison de Châtillon-sur-Marne* (Paris, 1621)** — FMG [1025, 1029, 1032, 1034, 1037, 1039, 1046, 1050, 1051]. *Available online* — Gallica. **Broader-content scope:** the seventeenth-century Châtillon genealogy contains the post-Mapledurham English-residue Mallet line interlocking with Hugues VI's daughter's marriage chain.

43. **Père Anselme (Pierre de Guibours), *Histoire généalogique et chronologique de la Maison Royale de France*, 9 vols., 3rd ed. (Paris, 1726–1733)** — FMG [425, 441, 1016, 1023, 1030, 1031, 1033, 1038, 1047, 1049, 1052–1056, 1060, 1061, 1063–1065, 1067, 1068, 1069, 1073, 1074, 1076, 1077, 1079, 1084, 1096, 1097, 1111, 1126, 1131, 1134, 1135]. *Available online* — Gallica. **Broader-content scope:** the canonical eighteenth-century genealogical compilation for French royal and noble houses. The post-1202 Gournay material (Mapledurham continuation, Marigny family, Malet de Graville) traces back through Anselme.

44. **Gilles-André de La Roque, *Histoire généalogique de la maison de Harcourt*, 4 vols. (Paris, 1662)** — FMG [430, 437, 447, 1017, 1018, 1024, 1027, 1028, 1035, 1036, 1044, 1071]. *Available online* — Gallica (the Tome IV Supplément at end of book, "only found in digitised copy on Gallica website," per FMG). **Broader-content scope:** the Harcourt genealogy contains the Mapledurham-era Mallet and Marigny material as related-family context.

45. **Sir William Dugdale (et al.), *Monasticon Anglicanum*, 6 vols. in 8 (2nd ed., Caley/Ellis/Bandinel, London, 1817–1830)** — FMG [421 (Roche), 932 (York St Mary), 950 (Hospital of St Leonard York), 951 (Whitby)]. *Available online* — all six volumes at archive.org and HathiTrust. **Broader-content scope:** the canonical compendium of medieval English monastic foundations. Vol. III has the York St Mary entry citing "Odo comes et Stephanus filius eius" relevant to G32's Aumale frontier collaboration; vol. VI.2 has the St Leonard York entry recording Gunderede uxor Nigelli de Albini donating with mention of her son Roger de Molbray (G32 §7); vol. I has the Whitby entry for Hospitale Sancti Michaelis Archangeli at Gundreda's request, for the soul of son Roger de Moubray (also G32 §7). All three Dugdale citations could be extracted in full from the published *Monasticon* and would supply the institutional context for Gundred's twin Yorkshire monastic patronages.

46. **John Smyth of Nibley, *The Berkeley Manuscripts: The Lives of the Berkeleys*, ed. Sir John Maclean, 3 vols. (Gloucester: Bellows, 1883–1885)** — FMG [992]. *Available online* — archive.org. **Broader-content scope:** Smyth's Berkeley-house biographies preserve the Lucy (widow of Robert de Berkeley) → Hugues VI de Gournay remarriage and the 18 Jan 1234 Bristol St Augustine burial; the wider biography is rich on the Berkeley-Mapledurham connection.

47. **Reginald R. Sharpe, ed., *Calendar of Letter-Books of the City of London*, Series A–L (London, 1899–1912)** — already in repo at `senior-gournay-baron-line-collateral.md` footnote [^letter-book-c-john-weavers-1202]. *Available online* — British History Online. Closed.

48. **The National Archives (UK), Discovery Catalogue, Duchy of Lancaster series (DL 42)** — already in repo at `senior-gournay-baron-line-collateral.md` footnote [^tna-dl-42-richard-i-hugh-de-gurnai]. *Available online* — discovery.nationalarchives.gov.uk. Closed.

## F. Sources cited via mediating handbooks

49. *Domesday Descendants* (= Keats-Rohan, *Domesday Descendants: A Prosopography of Persons Occurring in English Documents 1066–1166*, Boydell, 2002) — FMG [935, 999, 1000]. *Not online* (paywalled or library-only). **Broader-content scope:** the modern prosopographical successor to Keats-Rohan's 1999 *Domesday People* (already in repo as `keates-rohan-domesday-people-1999`). The 2002 *Descendants* volume continues the prosopography through the Anglo-Norman generation and would refine Hugues IV / Hugues V identifications.

50. *Europäische Stammtafeln* (= Schwennicke, *Europäische Stammtafeln: Stammtafeln zur Geschichte der europäischen Staaten*, neue Folge) — FMG [427, 428, 1525]. *Not online (free)*. **Broader-content scope:** the standard modern German genealogical-charts compendium; vol. XIII contains the Gournay-adjacent French baronage. Library reference work.

51. **Domesday Translation, Essex, XLVII, pp. 1037–8** — FMG [920]. *Available online* — Open Domesday (`opendomesday.org/`), Phillimore translation, and the original Farley/Ellis Record Commission edition (1783). **Broader-content scope:** the three Hugh de Gournai Essex manors (Liston, Ardleigh, Fordham) are already extracted at G33 §5.1; the wider Essex Domesday return covers adjacent post-Conquest landholders and sub-tenants (Geoffrey Talbot etc.) whose relationships to the Gournay enfeoffment are reachable via Keats-Rohan and through the Essex hundred-by-hundred map.

## G. Manuscript sources not in published edition

52. **Cordier (Nicolas) MS *Histoire de Gournay* (c. 1710–1738; whereabouts unconfirmed)** — referenced via Potin 1842 throughout G34–G37. *Not online* — likely held in a private collection or a regional French archive (Bibliothèque municipale de Rouen, Archives départementales de la Seine-Maritime, or similar). **Broader-content scope:** the deepest local-tradition Gournay manuscript. Would close the loop on every "MS *Histoire de Gournay*" citation in DG, Potin, NRP-I, and Decorde. Archival work would be required.

53. **Gondeville (M. de) MS *Histoire de Gournay* (whereabouts unconfirmed)** — referenced via Gurney 1845 throughout G35–G36. *Not online*. **Broader-content scope:** the alternative MS tradition behind DG's la-Ferté charter transcription. Delisle's nineteenth-century failure to find the la-Ferté original at Évreux (G35 §4) means the Gondeville MS is the single thread back to that text.

54. **Vitis Calthorpiana, MS Harleian 970, British Library** — FMG [985, 988]. *Not online* (British Library MS catalogue holds the description; not digitised in BL Digitised Manuscripts as of mid-2026). **Broader-content scope:** the Tresgoze letter pedigree purporting to be from Juliana Tresgoze to her brother Thomas de Cantilupe, Bishop of Hereford. The letter is chronologically impossible at points (the "reyne Blanch" marriage for Hugues V is dismissed by FMG) but other parts are corroborated against external sources. Direct inspection of BL Harleian 970 would test which portions are reliable. Single-document archive visit.

55. **Liber niger capituli Baiocensis, MS of the 13th century, Cathedral Library of Bayeux** — referenced via DG-Supp Note 9 at G34 §5.1. *Not online* (the Bayeux chapter manuscript itself). The Fauroux 1961 *Recueil des actes des ducs de Normandie de 911 à 1066* may contain the charter in published edition. **Broader-content scope:** charter no. 5 of the Liber niger records "Hugo de Gornai" witnessing William's grant of Bernières to Bishop Odo of Bayeux; the wider manuscript is the canonical Bayeux cathedral cartulary.

## Provenance and method

The catalogue was compiled by full extraction of the FMG MedLands SEIGNEURS de GOURNAY section into the working text (HTML-stripped) and direct identification of every distinct source cited in footnotes [902]–[998], augmented by adjacent-section sources ([1080]–[1092], [1524]) where they touch Gournay-related places or events. Online-availability tags follow the discipline in `.claude/rules/continual-improvement.md`: `Available online` means a URL has been verified or the source is on a well-established free repository (Gallica, archive.org, HathiTrust, dMGH); `Not online` means the source is in a physical archive or behind a paywall with no free digital edition; `Unknown online` means no targeted check was made and the source's status is uncertain.

The bibliography intentionally does not duplicate sources already exhausted in earlier patchsets (v54–v59); rather, the surviving open leads are flagged for future deepening sessions.

[^matthew-paris-1116-biscot]: see entry #45 above (Matthew Paris Chronica Majora) and footnote in `senior-gournay-baron-line-collateral.md`.
[^orderic-1118-rouen-fetters]: see entry #2 above (Orderic Vitalis Chibnall vol. VI) and footnote in `senior-gournay-baron-line-collateral.md`.
[^lannoy-1149-charter]: see entry #37 above (Lannoy cartulary) and footnote in `senior-gournay-baron-line-collateral.md`.
[^sigy-foundation-la-ferte]: see footnote in `senior-gournay-baron-line-collateral.md`.
[^sigy-transfer-hugues-iv]: see footnote in `senior-gournay-baron-line-collateral.md`.
[^marigny-saint-hildevert-donations]: see footnote in `research/places/collegiale-saint-hildevert-gournay.md`.
```

No new `sourceId` is required for §3; the topic file is a meta-bibliography and anchors back to `fmg-medlands-normacre` as the catalogue's transmitting reference.

---

## 4. INCLUDE — G32 (Gerard de Gournay) §2 — Hugues IV's continuing Bec donation from Basilea's Écouché maritagium (Henry II act DCCXLIV)

The Tome II text of act DCCXLIV (the [1181–89] Henry II Bec confirmation, Delisle n° 552) preserves an "Ex dono" clause not visible in the FMG quotation chain or in the G32 / G33 / senior-line companions: a donation by Hugues de Gournay from his rights at Écouché.

### 4.1 The finding

DCCXLIV lists five separate Gournay-related "Ex dono" clauses confirmed in 1181–89. Three correspond to the Bec donation chain already in G32 §2.10 (the Fordham/Liston/Ardleigh tithes of Hugues III, the half-manor of Longueil from Gerard and Basilea, and the church of Brémontier with the manor of Boscus Girardi from Gerard and Basilea). Two are not yet in the repo's research:

> "**Ex dono Hugonis de Gornaio, decimam de prepositura et portione sua in villa de Escochei et pertinenciis suis.**"

Translation: *"From the gift of Hugh de Gournay, the tithe of his prevotage and of his portion in the township of Écouché, with its appurtenances."*

This "Hugues de Gournay" is Hugues IV (the donation forms part of the same 1181–89 royal confirmation in which the prior-generation Hugues III, Gerard, and Basilea donations are confirmed; the senior baron at donation time is Hugues IV). Écouché is the **same Norman township** that G33 §3.1 documents as Basilea Flaitel's first *maritagium* via her first husband Raoul de Gacé, and the same property at issue in the [1089] Orderic Écouché-custody dispute already at G32 §2.4 ("Scoceium…held by Girardus de Gornaco…qui de eadem parentela prodierat, filius Basiliæ Girardi Fleitelli filiæ"). The 1181–89 royal confirmation therefore preserves the Écouché-as-Gournay-property line **continuously across three generations** — Basilea (acquired 1051) → Gerard (held c. 1089 per Orderic) → Hugues IV (donating a portion to Bec by 1181–89). The Bec donation is a small piece of an Écouché residue, but its survival into the senior-line donation programme rules out any post-Gerard alienation of the maritagium.

### 4.2 Proposed edit to `research/people/g32-gerard-de-gournay-fact-sheet.research.md`

Find the §2.10 paragraph (lines around 114–118 of the existing file, ending with "Independent twelfth-century corroboration of the donation chain Hugh III → Gerard → Basilia."). Append a new sub-section §2.10.1 immediately after, before §2.11:

```
### 2.10.1 The DCCXLIV (Delisle/Berger Tome II) Écouché continuity attestation

The full 1181–89 Bec confirmation (DCCXLIV in Delisle and Berger, Tome II, p. 375; Delisle n° 552) preserves a fifth Gournay-related "Ex dono" clause beyond the four already recorded at §2.10:

> "Ex dono Hugonis de Gornaio, decimam de prepositura et portione sua in villa de Escochei et pertinenciis suis."[^dccxliv-ecouche]

Translation: *"From the gift of Hugh de Gournay, the tithe of his prevotage and his portion in the township of Écouché, with its appurtenances."*

This "Hugues de Gournay" is Hugues IV — Gerard's senior-line heir — donating from the **same Écouché township** that Basilea Flaitel acquired as *maritagium* by her first marriage to Raoul de Gacé before 1051 (G33 §3.1), and that Gerard held in [1089] when the Évreux count's reclamation dispute placed the custody on Orderic's record (§2.4 above, naming "Girardus de Gornaco" as the holder via his Basilea-Flaitel descent). The 1181–89 royal confirmation preserves the Écouché-Gournay line **across three documented generations** — Basilea (post-1051 acquisition) → Gerard ([1089] custody) → Hugues IV (1181–89 Bec donation from a *portio* and the *prepositura*'s tithe). The maritagium did not pass out of the family after Gerard's death; a meaningful share of its revenue was still in Gournay hands a century later and was being given to Bec by Hugues IV alongside the older Gerard-and-Basilea donations.

The DCCXLIV charter is the primary-source corroboration that the Écouché tenure recorded at §2.4 was durable, not contingent on Gerard's personal alignment with William Rufus in [1089/90]. It also strengthens the Bec donation chain at §2.10 with one further generation: Hugh III + Gerard + Basilea (§2.10) + Hugues IV (this §2.10.1), confirmed together in a single mid-1180s royal act.

[^dccxliv-ecouche]: Léopold Delisle and Élie Berger, eds., *Recueil des actes de Henri II, roi d'Angleterre et duc de Normandie, concernant les provinces françaises et les affaires de France*, vol. 2 (Paris: Imprimerie nationale; librairie C. Klincksieck, 1920), act DCCXLIV at pp. 375–379 (the relevant Écouché clause at p. 379). Delisle's editorial number: n° 552. The charter is dated 1181–89, place "Apud Montem Fortem"; the original is lost, the text reconstructed by Delisle from multiple medieval copies (BnF lat. 13905 fol. 117, Rouen ms. 1235 fol. 26, Archives de l'Eure G 122–123, Monasticon Anglicanum t. VI p. 1067, Neustria Pia p. 484). PDF available at Internet Archive (`recueildesactesd02grea`). Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
```

---

## 5. INCLUDE — `senior-gournay-baron-line-collateral.md` — three Hugues IV / Hugues V Tome II witness attestations

Append three further attestations to the "Documentary attestations beyond Decorde" subsection added at §1 above (i.e., the four bullets become seven).

```
- **Bec Pré-de-Rouen confirmation, 1172–1178** (DXXXII in Delisle and Berger, Tome II, p. 104; Delisle n° 365). Hugues IV de Gournay subscribed the Henry II confirmation of the monks of Bec established at the church of Pré at Rouen, with the witness list closing "Ricardo de Hommetis constabulario, Roberto comite Mellenti, Warino filio Geroldi camerario, magistro Alveredo, Gocelino Crispin et Guillelmo filio ejus, **Hugone de Guurnayo et Roberto de Haricuria**." The Henry II act reproduces and confirms an earlier Henry I charter dated 1122 at Winchester (also inset in DXXXII). Hugues IV's subscription places him at the Norman royal court in the same Hommet–Beaumont–Crispin company that recurs across the 1170s and confirms his active baronial role through his middle age.[^dxxxii-bec-pre]
- **Caen abbess fine, 20 January 1183** (DCXXXVIII in Delisle and Berger, Tome II, p. 250; Delisle n° 445 A). Hugues IV de Gournay subscribed the Henry II final concord between the abbess of La Trinité de Caen and Robert son of Richard de Scrotonia in the king's full assize at Caen, with the witness list including "Henrico de Novoburgo, comite Augi, Johanne de Solinneio, Waquelino de Ferrariis, **Hugone de Gornaiu**, Ricardo de Belfou, Engerranno Patrie, Wilielmo camerario Tancarville." This is the latest dated direct witness attestation for Hugues IV before the c. 1180/82 death range from the senior-line topic.[^dcxxxviii-caen-fine]
- **Barbery confirmation, 1182–1189 at Rouen** (DCCL in Delisle and Berger, Tome II, p. 392; Delisle n° 554). Hugues V de Gournay subscribed the Henry II confirmation of the abbey of Barbery, with the witness list opening "S. Cicestriensi et R. Lexoviensi episcopis…W. comit� Wilielmo de Mannevilla, R. comit� Mellenti, Rannulfo de Glanvilla, Wilielmo Filio Radulfi senescaiio Normannie, Hugone de Creissi, Walchelino de Ferrariis, **Hugone de Gurnai**, Rogerio de Mortuo Mari, Wilielmo de Mara, Richardo Silven." Glanvill's tenure as justiciar to 1189 narrows the range, and the post-1182 succession in the senior barony makes this Hugues V rather than Hugues IV. The attestation falls between Hugues V's father's death and the 1190 Acre crusade.[^dccl-barbery]
```

### Sigy founder identification — la-Ferté collateral confirmed by DCCLII

Append immediately after the existing "Sigy priory" paragraph created at §1 above. Find the sentence ending "Sigy passed to the senior Gournay line by some twelfth-century inheritance not documented in surviving record" and append a follow-on sentence and supporting citation:

```
The 1185–1189 Henry II confirmation of the priory (DCCLII at Argentan, in Delisle and Berger, Tome II, p. 396; Delisle n° 557) preserves the Sigy founder explicitly as "Hugo Feriensis" — "Hugh of la Ferté" — naming his original donation of the priory site itself plus six dependent churches: Belci, Brokedale, Frii, the chapel of Saint-Ouen, Soolmont, and the church of Sainte-Marie de Goislenifontaine (Gaillefontaine).[^dcclii-sigy] The Hugo Feriensis identification matches FMG's "HUGUES [I] de la Ferté" (founder per [1030/35] in Gallia Christiana XI p. 12). The DCCLII confirmation does not by itself attest a Sigy transfer by Hugues IV de Gournay — it confirms the existing priory possessions to its monks without naming a Gournay-side transfer act — so the "transfer to a new site" reading transmitted via Gurney 1845 p. 35 (from a *History of the Abbey of St Ouen at Rouen* p. 463) rests on a separate notice not captured in DCCLII itself. The DCCLII text does, however, confirm one substantive point: the Sigy possessions include the church at Gaillefontaine (B. Marie de Goisleni Fontenis), which places Sigy inside the same regional defensive-and-monastic triad documented at G36 §2.4 (Gournay / La Ferté / Gaillefontaine).
```

```
[^dxxxii-bec-pre]: Delisle and Berger, *Recueil des actes de Henri II*, vol. 2 (Paris, 1920), act DXXXII at pp. 105–108. Charter dated 1172–1178; place not named in surviving copies. The text reproduces an earlier Henry I charter dated 1122 at Winchester. PDF available at Internet Archive (`recueildesactesd02grea`). Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
[^dcxxxviii-caen-fine]: Delisle and Berger, *Recueil des actes de Henri II*, vol. 2 (Paris, 1920), act DCXXXVIII at pp. 250–251. Charter dated 20 January 1183 at Caen. Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
[^dccl-barbery]: Delisle and Berger, *Recueil des actes de Henri II*, vol. 2 (Paris, 1920), act DCCL at pp. 392–393. Charter dated 1182–1189 at Rouen. Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
[^dcclii-sigy]: Delisle and Berger, *Recueil des actes de Henri II*, vol. 2 (Paris, 1920), act DCCLII at pp. 396–397. Charter dated 1185–1189 at Argentan; subscription of Walter of Coutances as archbishop of Rouen narrows to post-early-1185. Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
```

---

## 6. INCLUDE — G32 §3.2 (Amicie Talbot) — Tome II primary-text corroboration

The Amicie Talbot identification at G32 §3.2 currently relies on the FMG MedLands extracts of [1181/83] Valmont (FMG [889]) and [1189] Sainte-Foi de Longueville (FMG [890]). Both acts are now in repo via Tome II direct extraction; the texts independently confirm the identification.

### 6.1 The acts in primary form

- **DCXXXVI (1181–1183, "Apud Selvi castrum") — Valmont confirmation** (Delisle and Berger, Tome II, p. 247; Delisle n° 452–453): "Ex dono Richardi Taliebot et **Amicie, uxoris ejus**, et **Hugonis et Willelmi filiomm suorum**, unum modium avene apud Belvayam, in mansura Hugonis, filii Jefrey Larduin."
- **DCCLXVIII (1188–1189 probably March–June 1189, Le Mans) — Sainte-Foi de Longueville confirmation** (Delisle and Berger, Tome II, p. 422; Delisle n° 528): "Ecclesiam Sancte Genovefe cum omnibus pertinentiis, et terram et homines suos ibidem, et imam carrucatam terre, et cultram terre que vocatur de Tilia Comitis, **de dono Ricardi Thalebot et Arilie [Avitie] uxoris sue et Hugonis filii sui**. Ecclesiam de Bosco Robardi, cum pertineniis suis…"

Both attestations name Amicie under the variant "Amicia" / "Avitia" / "Arilia" and name Hugh as a son; DCXXXVI additionally names William as a second son. The "Avitia" / "Arilia" variant in DCCLXVIII matches the FMG [890] transcription and confirms the name-variant range is internal to the Talbot acts, not a Cawley transcription slip.

### 6.2 Proposed edit to `research/people/g32-gerard-de-gournay-fact-sheet.research.md`

Find the existing §3.2 footnote-anchor block (the FMG [889] and [890] inline citations within §3.2). Append one footnote — `[^amicie-talbot-tome-ii]` — at the end of the §3.2 paragraph that closes with "(c) daughter of Hugues [III] de Gournay (more remote *nepos* sense).", and at that footnote anchor add:

```
[^amicie-talbot-tome-ii]: The two FMG-quoted Henry II acts for Amicie Talbot's identification (FMG [889] = act DCXXXVI at Selvi castrum 1181–1183; FMG [890] = act DCCLXVIII at Le Mans 1188–1189) are now in repo via direct Tome II extraction. The primary texts confirm Cawley's reading: DCXXXVI names "Amicie, uxoris ejus" with sons Hugh and William; DCCLXVIII names "Avitie uxoris sue" with son Hugh (the "Avitia"/"Arilia" variant is internal to the Talbot acts and matches Cawley's [890] transcription). The Tome II texts add no new content beyond what Cawley quoted, but they elevate the FMG citation chain to primary-source via the Delisle-Berger critical edition. Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.
```

---

## 7. NEW corpus_supplement file — Tome II Gournay-relevant text extracts

Parallel to the existing `sources/corpus_supplement/actes-henri-ii-delisle-berger-vol1-text.md`, create `sources/corpus_supplement/actes-henri-ii-delisle-berger-vol2-text.md` preserving the Gournay-relevant act extracts from Tome II (DXXXII, DCXXXVI, DCXXXVIII, DCCXLIV, DCCL, DCCLII, DCCLXVIII).

Body to write (preserves Latin extracts with editorial notes; mirrors the vol-1 file's structure):

```
# Delisle and Berger, *Recueil des actes de Henri II*, vol. 2 (1920) — Gournay-relevant act extracts

Source: Léopold Delisle and Élie Berger, eds., *Recueil des actes de Henri II, roi d'Angleterre et duc de Normandie, concernant les provinces françaises et les affaires de France*, vol. 2 (Paris: Imprimerie nationale; librairie C. Klincksieck, 1920). Internet Archive identifier: `recueildesactesd02grea`. Sibling file: `actes-henri-ii-delisle-berger-vol1-text.md` (vol. 1, 1916). Source ID: `recueil-actes-henri-ii-delisle-berger-vol-2`.

This file holds the Gournay-relevant Latin charter texts extracted from a `pdftotext -layout` pass over the volume. Pagination follows the printed Delisle-Berger edition; act numbers are the volume's continuous Roman-numeral numbering; Delisle's editorial numbers (n° 365, 452, etc.) are noted where they differ from the volume numbering.

## DXXXII — Bec Pré-de-Rouen confirmation, 1172–1178 (Delisle n° 365; pp. 105–108)

[Reproduce the Latin body of the act here from the PDF text; preserve the witness list including "Hugone de Guurnayo et Roberto de Haricuria" at the end. Note the inset Henry I 1122 Winchester charter that the Henry II act confirms.]

## DCXXXVI — Valmont confirmation, 1181–1183 at Selvi castrum (Delisle n° 452–453; p. 247)

[Reproduce the body including the "Ex dono Richardi Taliebot et Amicie uxoris ejus et Hugonis et Willelmi filiomm suorum, unum modium avene apud Belvayam" clause.]

## DCXXXVIII — Caen / Scrotonia fine, 20 January 1183 at Caen (Delisle n° 445 A; pp. 250–251)

[Reproduce the body with the witness list including "Hugone de Gornaiu."]

## DCCXLIV — Bec confirmation, 1181–1189 at Montfort (Delisle n° 552; pp. 375–379)

[Reproduce the body. Preserve the five Gournay-related "Ex dono" clauses: "Ex dono primi Hugonis de Gornaco et Girardi filii, decimam totius dominii sui de Fordeham, et Lislona et Alee et ecclesias ipsarum villarum"; "Ex dono Girardi de Gornaio et Basilie matris sue, medietatem totius manerii de Longolio"; "Ex dono ipsius Girardi et Basilie matris ejus, ecclesiam de Brannost cum terra et decima et omnibus que ad eam pertinent, et manerium de Bosco Girardi cum omnibus pertinenciis"; "Ex dono Hugonis de Gornaio, decimam de prepositura et portione sua in villa de Escochei et pertinenciis suis"; and the Hawisia de Monbaston clause that follows. Witness list closes "Johanne de Constanciis archidiacono Oxenefordie, Willelmo clerico de Camera, Willelmo Filio Radulfi senescallo Normannie, Eudone et Rogero de Fontibus. Apud Montem Fortem."]

## DCCL — Barbery confirmation, 1182–1189 at Rouen (Delisle n° 554; pp. 392–393)

[Reproduce the body, especially the witness list including "Walchelino de Ferrariis, Hugone de Gurnai, Rogerio de Mortuo Mari."]

## DCCLII — Sigy priory confirmation, 1185–1189 at Argentan (Delisle n° 557; pp. 396–397)

[Reproduce the body, especially: "Sciatis me concessisse et presenti carta confirmasse priori et monachis Sancti Martini de Sigeio omnes res et possessiones suas, quascunque Hugo Feriensis, pro salute anime sue et antecessorum suorum, eis in perpetuam elemosinam donavit, locum videlicet in quo fundatum est monasterium Sancti Martini, cum omnibus pertinentiis suis, ecclesiam de Belci, ecclesiam de Brokedale, ecclesiam de Frii, capellam Sancti Audoeni, ecclesiam de Soolmont et ecclesiam Beate Marie de Goisleni Fontenis, cum omnium predictarum ecclesiarum presentationibus, et quandam feriam in festo beati Martini de estate." Witness list: "Waltero archiepiscopo Rothomagensi, Johanne Ebroicensi episcopo, Radulfo Lexoviensi episcopo, comite Willelmo de Mandevilla, Seherio de Quenci, Hugone de Cressi, Johanne de Soligneio. Apud Argentomum."]

## DCCLXVIII — Sainte-Foi de Longueville confirmation, 1188–1189 probably March–June 1189 at Le Mans (Delisle n° 528; pp. 422–423)

[Reproduce the body, especially: "Apud Ansketevillam, ecclesiam cum pertinentiis suis, et terram, et homines quos habent de Hugone Thalebot et heredum suorum"; and "Ecclesiam Sancte Genovefe cum omnibus pertinentiis, et terram et homines suos ibidem, et imam carrucatam terre, et cultram terre que vocatur de Tilia Comitis, de dono Ricardi Thalebot et Avitie uxoris sue et Hugonis filii sui. Ecclesiam de Bosco Robardi…"]

## Cross-references

- Used at `research/people/g32-gerard-de-gournay-fact-sheet.research.md` §2.10.1 (DCCXLIV Écouché clause) and §3.2 (DCXXXVI and DCCLXVIII Amicie Talbot acts).
- Used at `research/topics/senior-gournay-baron-line-collateral.md` (DXXXII Bec Pré-de-Rouen, DCXXXVIII Caen Scrotonia fine, DCCL Barbery, DCCLII Sigy founder identification).
```

Phase-2 should populate the bracketed `[Reproduce the body…]` placeholders by copying the relevant Latin text from the downloaded PDF (currently at `C:/Users/allen/AppData/Local/Temp/recueild02.pdf`, 28 MB; should be moved to `sources/media/recueildesactesd02grea.pdf` per the vol-1 pattern) or from the IA-archive direct download. The text-extraction work was done in this intake phase; copying the verbatim Latin into the corpus_supplement file is a Phase-2 mechanical operation.

---

## 8. JSON alignment

**One new `sources.json` entry required**, mirroring the existing vol-1 entry at line 2739:

```json
    "recueil-actes-henri-ii-delisle-berger-vol-2": {
      "shortTitle": "Recueil des actes de Henri II, Delisle/Berger, vol. 2 (1920)",
      "citation": "Delisle, Léopold, and Élie Berger, eds. Recueil des actes de Henri II, roi d'Angleterre et duc de Normandie, concernant les provinces françaises et les affaires de France. Vol. 2. Paris: Imprimerie nationale; librairie C. Klincksieck, 1920.",
      "archive": "Internet Archive (recueildesactesd02grea); also Gallica",
      "url": "https://archive.org/details/recueildesactesd02grea",
      "corpusStatus": "full",
      "corpusPath": "sources/corpus_supplement/actes-henri-ii-delisle-berger-vol2-text.md",
      "mediaPath": "sources/media/recueildesactesd02grea.pdf",
      "validationPath": null,
      "notes": "Posthumous edition of Delisle's collection of Henry II's acts concerning the French provinces, completed by Élie Berger. Tome 2 covers acts CCCCXLVIII (act 448) onward through DCCC+ range, all c. 1170s–1189. Key Gournay-related acts: (a) DXXXII (Delisle n° 365), 1172–1178, Bec Pré-de-Rouen confirmation subscribed by Hugues IV de Gournay (witness list: Hommet, Beaumont, Crispin, 'Hugone de Guurnayo et Roberto de Haricuria'); (b) DCXXXVI (Delisle n° 452–453), 1181–1183 at Selvi castrum, Valmont confirmation naming 'Ex dono Richardi Taliebot et Amicie, uxoris ejus, et Hugonis et Willelmi filiomm suorum' — Amicie Talbot primary attestation; (c) DCXXXVIII (Delisle n° 445 A), 20 January 1183 at Caen, fine between abbess of La Trinité de Caen and Robert de Scrotonia, witnessed by 'Hugone de Gornaiu' — latest dated Hugues IV witness attestation before death; (d) DCCXLIV (Delisle n° 552), 1181–1189 at Montfort, Bec confirmation listing five Gournay 'Ex dono' clauses including 'Ex dono Hugonis de Gornaio, decimam de prepositura et portione sua in villa de Escochei et pertinenciis suis' — primary-source attestation of Hugues IV's continuing Bec donation from Basilea Flaitel's Écouché maritagium, preserving the Gournay-Écouché tenure across three generations; (e) DCCL (Delisle n° 554), 1182–1189 at Rouen, Barbery confirmation witnessed by 'Hugone de Gurnai' (Hugues V); (f) DCCLII (Delisle n° 557), 1185–1189 at Argentan, Sigy priory confirmation naming 'Hugo Feriensis' as founder (= FMG's HUGUES [I] de la Ferté collateral) and listing the priory's six dependent churches including the Gaillefontaine church; (g) DCCLXVIII (Delisle n° 528), 1188–1189 probably March–June 1189 at Le Mans, Sainte-Foi de Longueville confirmation naming 'Ricardi Thalebot et Avitie uxoris sue et Hugonis filii sui' as donors of the church of Sainte Geneviève. Fetched 2026-05-25 from Internet Archive recueildesactesd02grea. Full Gournay-relevant Latin extracts at sources/corpus_supplement/actes-henri-ii-delisle-berger-vol2-text.md (Phase-2 to populate)."
    },
```

Position the entry in `data/sources.json` immediately after the existing `recueil-actes-henri-ii-delisle-berger-vol-1` block (after line 2748).

All other INCLUDE blocks (§1, §2, §3) still use existing sourceIds:
- §1 — `fmg-medlands-normacre` (existing, line 2497) for the original-MedLands footnotes; `orderic-vitalis-chibnall-vol-6` (existing) as the primary anchor for the fetters episode.
- §2 — `fmg-medlands-normacre` (existing) for the Marigny endowments.
- §3 — `fmg-medlands-normacre` (existing) for the topic file's overall provenance anchor.

The §3 source-leads catalogue *names* fifty-five distinct sources, but they are listed as research leads — adoption into `sources.json` happens at the point each lead is actually pursued and used in a research insertion, per `.claude/rules/sources-intake.md` "no research content should be inserted from intake unless it ties to an existing or newly created `data/sources.json` entry."

---

## 5. EXCLUDE — coverage rationale

For each excluded FMG content block, the rationale is that the repo's existing companions are already deeper. The audit recorded the line-by-line cross-walk; the headline points are summarised here for traceability.

- **G37 (Eudes)**: FMG [902]–[905] are short and tradition-flagged. Repo G37 §2 has the Cordier MS, the écu-noir heraldic detail, the Lorraine-Vuldus rejection, and the Hannay framing — all absent from FMG.
- **G36 (Hugues I)**: FMG has nothing on Hugues I directly (the [HUGUES de Gournay (bracketed)] entry is the son-of-Eudes traditional figure, not the fortifier of la Tour Hue). Repo G36 §2.1–§2.3 has the Brito *Philippide* verses (via Potin), the Cordier topographical detail, La Tour Hue's eighteenth-century survival, and the Painchault 2012 strategic-triad context.
- **G35 (Renaud)**: FMG [906]–[908] gives only the la Ferté foundation. Repo G35 §2 adds the NRP-I 1852 fuller witness list (Robert Archbishop, Duke Richard II, Bishop Hugues, Saints Peter and Paul dedication, five founding churches), the third-son Raoul local tradition, the Pattou hedging on dating, and the Delisle-critique reception history.
- **G34 (Hugues II)**: FMG [911]–[915] covers four areas (1035 expedition, 1054 Mortemer indirect via the Robert d'Eu alliance, [1060] Brenerias, 1066 Hastings indirect, 1074 Cardiff). Repo G34 §2 catalogues four chronicle versions of the 1035 expedition with captain reconciliation; §3 catalogues two versions of the 1054 Mortemer command structure including the Eulde / Hugues name equivalence; §4 has Wace verbatim and the Dumoulin-corroborated "three Gournays at Hastings"; §5 has the Bayeux *Liber niger* charters and the April 1067 Vaudreuil Martene charter; §6 catalogues all four French / Norman / Lorraine traditions of the Cardiff narrative and the Powell 1584 Welsh-Chronicle fifth tradition.
- **G33 (Hugues III)**: FMG [916]–[927] covers the [1040] (misdated) Jumièges Havoth charter, the 1066 Wace verses, the 1067 Saint-Benoît charter, the [1073] Marmoutier charter, the Domesday three-manor Essex chapter, the Bec [1181/89] confirmation, the Basilia first-husband / Jumièges Galterium Giffardum charter, the Anselm letter, the *Chronicon Beccensis* death-Sundays, and the [1181/89] Bec confirmation again with Gerard / Basilie addition. Repo G33 covers all eleven, plus: the Saint-Nicaise de Meulan priorate (Potin 1842 / Pattou), the Anfrede / Ansfride mother / niece tangle (G33 §3.3), the Caister + Saint-Hildevert Channel-spanning ecclesiastical link (G33 §5.3), the broader Bec endowment programme (G33 §5.4 — Bois Girard, Brémontier, Elboeuf, La Rozière, La Ferté / Gaillefontaine / Gournay / Merval / Lodencourt tithes), and the 1079 Gerberoi mediator role (G33 §6.3).
- **G32 (Gerard)**: FMG [929]–[940] covers the Jumièges Havoth charter, the 1082 Caen Trinité, the [1089/90] Orderic three-castle delivery, the [1089] Écouché custody passage, the Albert / Baudry / Jumièges crusade attestations, the Bec [1181/89] confirmation, and the Edith de Warenne Jumièges passage with Drogo de Monceio. Repo G32 covers all seven, plus: Pattou's chart-genealogy entry with the political-alignment narrative (G32 §4); the St-Sauveur 1104 *terminus post quem* (G32 §2.8); the Beauvais 8 May obituary (G32 §2.9); the St-Wandrille charter from DG-Supp Note 17 (G32 §2.11); Gerard's seal at La Trinité de Rouen Cartulary (§2.12); the Britolio dispute from Évreux MS 132 (G32 §2.13); the Decorde Hugues IV Bec confirmation at c. 1112/22 (G32 §2.14); the Clay *Early Yorkshire Charters* vol. 8 closure of the post-1104 death-date bracket (G32 §11); the Actes Henri II vol. I Edwa-in-Anglia attestation (G32 §14); and the RHGF vol. 15 Suger-on-Drogo-II 1148 letter (G32 §13).
- **Amicie, Hugues IV, Gundred, Hawise [941]–[952]**: collateral or junction-level; covered at G32 §3.2 (case-file referenced) and G33 §8.
- **Hugues IV detailed block [953]–[963]**: senior-line collateral; covered in `senior-gournay-baron-line-collateral.md` (Mélisende identification, Bellosanne, Bec, Clairruissel) — with the three small gaps from §1 above now flagged for insertion.
- **Beatrix de Vermandois, Mélisende de Coucy, Hugues V, the post-1202 Mapledurham continuation [964]–[994]**: senior-line collateral; covered in `senior-gournay-baron-line-collateral.md`.
- **The collateral --- de Gournay × Aveline de Noerey branch [995]–[998]**: no documented link to direct-ancestor line; no insertion warranted; the Notre-Dame de Paris cartulary is catalogued in §3 #36 above as an available-online source for any future investigation.

---

## 9. Phase-2 application checklist

1. **§1** — Append the four-paragraph "Documentary attestations beyond Decorde" + "Sigy priory" addition to `research/topics/senior-gournay-baron-line-collateral.md`, with the five new footnotes anchored to `fmg-medlands-normacre` and `orderic-vitalis-chibnall-vol-6`. Insertion point: immediately after the Hugues IV death footnote `[^decorde-hugues-iv-death]`, before the "Hugues V de Gournay" heading.
2. **§2** — Append the Marigny endowment-target paragraph + footnote to `research/places/collegiale-saint-hildevert-gournay.md`. Read the existing place file before insertion to choose the correct anchor (a "Post-1202 endowment continuity" subsection if it exists, otherwise the end of the body before footnotes). If the place file does not exist yet, create it as a stub with the standard place-file header structure and place the new paragraph as §1, with a note that earlier Saint-Hildevert content from G33 §5.3 and G32 §6 should be migrated in a subsequent pass.
3. **§3** — Create the new file `research/topics/medlands-gournay-source-leads.md` with the full body specified in §3 above. The five back-pointer footnotes at file end should resolve cleanly because each is referenced from a separately-written companion footnote. The §3 catalogue should also be updated at the time of application to mark entry #17 (Delisle-Berger *Recueil des actes de Henri II* vol. II) as **Closed** — its pursuit is now landed in §4–§7 — and entry #29 (Saint-Benoît-sur-Loire) and entry #36 (Notre-Dame de Paris cartulary) should be re-checked to make sure they were not also fetched in this session (they were not; remain as open leads).
4. **§4** — Insert the §2.10.1 sub-section into `research/people/g32-gerard-de-gournay-fact-sheet.research.md` immediately after the existing §2.10 paragraph ending "Independent twelfth-century corroboration of the donation chain Hugh III → Gerard → Basilia." Add the `[^dccxliv-ecouche]` footnote in the file's existing footnote area.
5. **§5** — Extend the same `senior-gournay-baron-line-collateral.md` block from §1 with three additional bullets (DXXXII, DCXXXVIII, DCCL) and the Sigy DCCLII follow-on sentence, plus the four supporting footnotes anchored to `recueil-actes-henri-ii-delisle-berger-vol-2`.
6. **§6** — Add the `[^amicie-talbot-tome-ii]` footnote to G32 §3.2.
7. **§7** — Create `sources/corpus_supplement/actes-henri-ii-delisle-berger-vol2-text.md` with the structure outlined in §7 above; populate each `[Reproduce the body…]` placeholder with the verbatim Latin from the PDF text extract.
8. **§8** — Insert the `recueil-actes-henri-ii-delisle-berger-vol-2` entry in `data/sources.json` immediately after the existing `recueil-actes-henri-ii-delisle-berger-vol-1` block (after line 2748). Re-validate JSON syntax.
9. **File move** — Copy the Tome II PDF from `C:/Users/allen/AppData/Local/Temp/recueild02.pdf` (downloaded 2026-05-25 in this intake session, 28 MB) to `sources/media/recueildesactesd02grea.pdf`, parallel to the existing `recueildesactesd01grea.pdf`. Alternative: re-download from `https://archive.org/download/recueildesactesd02grea/recueildesactesd02grea.pdf` if the temp file is no longer present at Phase-2 application time. The mediaPath in the new sourceId entry assumes the standard `sources/media/recueildesactesd02grea.pdf` location.

## 10. Unresolved

- **Lannoy cartulary "Tome X charter XIV p. 639"** (FMG [957]): publication identity remains uncertain; not pursued in this session.
- **Sigy priory Henry II "transfer to a new site by Hugo de Gornaio" attribution** (FMG [958] via Gurney 1845 p. 35): the Tome II Sigy confirmation DCCLII does **not** record a Hugues IV transfer of the priory site (it confirms existing possessions to "Hugo Feriensis" as original founder). The "transfer" language Gurney transmitted from *History of the Abbey of St Ouen at Rouen* p. 463 therefore points to a different document, not yet identified. The St Ouen abbey history is likely Pommeraye's 1662 *Histoire de l'abbaye royale de Saint-Ouen de Rouen* (online at Gallica) — a Phase-3 pull on that specific page would close the citation chain.
- **Cordier MS *Histoire de Gournay***: deepest archival lead (§3 #52); requires manuscript-level archive work.
- **Walter de Gournay (G31) / *Olim***: §3 #25 above showed Beugnot 1839–1848 is on Gallica. A future patchset could pull the Beugnot vol. I entry directly to confirm the DG-citation chain.
- **Tome III of Delisle-Berger** (1927, posthumously published, includes the general introduction and final acts): not pursued in this session. Worth a quick check whether any Gournay-related acts above DCCC are in Tome III.
