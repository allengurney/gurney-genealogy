**Done:** 2026-07-15 08:24 PT

# Patchset v125 — Walter de Gournay (G31): companion assimilation, fact-sheet corrections, places

**Context.** Promotes the July 2026 record examination into Walter's own files. The records were acquired 2026-07-14 (full texts in `sources/corpus/`, curated extracts in `sources/corpus_supplement/`, sourceIds registered in `data/sources.json`; leads L-207–L-221). The former case file `research/case-files/walter-de-gournay-as-son-of-gerard.md` has been retired (renamed with a `-to-be-deleted` suffix pending the user's review); its evidence and quotations are carried into the companion by the operations below, and the fact-sheet cross-link now points at the companion. Companion patchset v124 carries the G32/G29 promotions and validation worksheets.

**Editorial posture.** The records are stated as what they are. Walter's identification as Gerard's son is carried as established (Daniel Gurney's Supplement Note 104 proof plus the record base); alternatives appear once, in a footnote.

**Phase-2 operations index.**
1. Item 1 — eleven str_replace edits: `research/people/g31-walter-de-gournay-fact-sheet.research.md`
2. Item 2 — sixteen str_replace edits: `fact-sheets/g31-walter-de-gournay-fact-sheet.md`
3. Item 3 — three str_replace edits: `data/ancestors.json`
4. Item 4 — four str_replace edits: `data/places.json`, `data/places_detail.json`; two str_replace edits: `research/places/suffolk.md`
5. Closing: run `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write`; do not mirror to `site/`; Done stamp; move to `sources/intake/done/`.

---

## Item 1 — G31 research companion (promote)

Target file: `research/people/g31-walter-de-gournay-fact-sheet.research.md`. Eleven str_replace edits. Existing entries are kept and extended; two thin entries (Les Olim; Dampmartin) are rewritten in place because the new records correct or subsume them.

**1.1 — Setting, cast, and records-summary sections (inserted between the intro line and Working Notes).**

str_replace old_string:
```
Research companion for `g31-walter-de-gournay-fact-sheet.md`. See `.claude/rules/research-files.md` for the paired-file rule.

---

## Working Notes
```
new_string:
```
Research companion for `g31-walter-de-gournay-fact-sheet.md`. See `.claude/rules/research-files.md` for the paired-file rule.

---

## Setting — the geography in plain English

Walter's world had two theatres. In **England**, the family's manors of Swathings and Hingham Gurney's (with the hamlet of Runhall, in and around Hardingham, Norfolk) lay inside the senior Gournay lords' Norfolk holdings, which sat within the earl of Warenne's great lordship; the junior branch held them under the senior line.[^setting-norfolk] Walter's own recorded holding was in **Suffolk**: a quarter of a knight's fee granted out of the Dammartin family's fee of Mendlesham (with Cotton and Wickham Skeith nearby, Hartismere hundred).[^setting-suffolk] In **Normandy**, the senior family's homeland was the pays de Bray — Gournay-en-Bray, La Ferté, Gaillefontaine, Argueil — and the junior line's Norman traces cluster there: Montigny-sur-Andelle (held by Walter's son William directly of the crown), its dependency Massy (formerly part of Gerard's own honour), and the hamlet of Bois Gautier ("Walter's wood") beside Montigny.[^setting-bray] A third landscape supplies context rather than holdings: **Kent**, where a separate Gurnay family held Addington (Larkfield hundred) within the honour of Swanscombe, and where Walter's patron Manasser de Dammartin also held three knights' fees of the same honour.[^setting-kent]

[^setting-norfolk]: Daniel Gurney, *Record of the House of Gournay*, Part II (1848), pp. 277, 295 (mesne tenure under the elder line before the 1205 forfeiture; Swathings/Runhall geography, citing Blomefield); William Farrer, *Honors and Knights' Fees*, vol. 3 (1925), p. 422 (Swathings within the senior Gournays' Warenne-honour fee). Source IDs: `dg-rec-pt2`, `farrer-honors-knights-fees-v3-gurnay-extracts`.

[^setting-suffolk]: Carta of Manasser de Danmartin, 1166 (see the records table); Daniel Gurney, *Record*, Part II, p. 289 ("The fiefs of the Dammartins in Suffolk were at Mendlesham and Cotton, in the Hartesmere hundred"); Wickham Skeith from *Sir Christopher Hatton's Book of Seals*, ed. Loyd & Stenton (1950), No. 350. Source IDs: `dg-rec-pt2`, `hatton-book-of-seals-1958`, `redbook-exchequer-hall-v1`.

[^setting-bray]: Daniel Gurney, *Record*, Part II, pp. 292–293 (Montigny, Massy, Argueil); Supplement (1858), Note 104, pp. 776–777 (Bois Gautier). Source IDs: `dg-rec-pt2`, `dg-rec-supp`.

[^setting-kent]: Edward Hasted, *History of Kent*, 2nd ed., vol. 4 (1798), pp. 544–545 (Addington held of the Montchensies "as of his manor of Swanscombe"); carta of Walter de Meduana, 1166 (Manasser's three Kent fees). Source IDs: `hasted-kent-vol4`, `redbook-exchequer-hall-v1`.

## Cast — the people in this file

| Name | Who they are |
|---|---|
| Gerard de Gournay (G32) | Walter's father; lord of Gournay-en-Bray; crusader; died on pilgrimage by 1104 |
| Edith (Ediva) de Warenne | Walter's mother; daughter of William de Warenne, first earl of Surrey; remarried Drew de Monceaux |
| Hugh de Gournay IV | Walter's elder brother; heir to the barony; of full age 1112 |
| Hugh de Gournay V | Walter's nephew; last senior lord in England; forfeited 1205 |
| Gundred de Gournay | Walter's sister; married Nigel d'Aubigny 1118 |
| (Daughter of Gerard) | Walter's sister; married Richard Talbot |
| Renaud de Gournay | A further son "some authors give to Gerard" (De la Mairie) |
| William de Gournay I (G30) | Walter's son; held the Suffolk quarter-fee by 1166; lord of Runhall; the Montigny grantor |
| Matthew de Gournay (G29) | Walter's grandson; first occurs c. 1160; married Rose of Harpley by 1184 |
| Manasser de Dammartin | Walter's Suffolk lord (d. 1178/9); lord of Mendlesham; also held 3 Kent fees; married Galiena |
| Odo de Dammartin (d. 1131) | Manasser's father; enfeoffed of Mendlesham by Henry I; Lewes priory donor |
| Basilia | Odo's widow (dower payment 1130); possibly a Gournay by birth (DG's name-conjecture) |
| Galiena (I) de Gurnay | Manasser's wife; heiress of Addington, Kent; granddaughter of William de Gurnay of Addington |
| William de Gurnay of Addington | Kent landholder of Henry I's generation; gave Addington tithes to Rochester priory |
| Bartholomew and William de Dammartin | Manasser and Galiena's sons; successive lords of Mendlesham (d. bef. 1190; d. 1195) |
| Galiena (II) de Dammartin | William de Dammartin's daughter and heir; her third marriage (Ernald de Mandeville) carried Mendlesham and Addington to the Mandevilles |
| Geoffrey Talbot | Held the twenty-knight Kent honour (later "Talbot of Swanscombe") in chief at Henry I's death; the Talbots were Gournay tenants at Domesday and in-laws by marriage |
| Walter de Mayenne and Cecily | Held the Talbot honour in 1166 "by the king's grace ... per Ciciliam" (through Cecily) |
| William de Gornaco (Kent) | Held a half-fee of that honour's demesne, service-free, granted in Stephen's reign; identity unresolved (Walter's son, per DG's suggestion, or an Addington kinsman) |
| Earl Hamelin de Warenne | Head of the Warenne family, half-brother of Henry II; gave Rose of Harpley to Matthew (see the G29 companion) |
| Eustace de Montigny | Petitioner of 1259 whose recital preserves William de Gournay's Montigny tenure |

Identifications are documented in the records table and working notes below, where each carries its citation.

## The records — plain-English summary (in order of the events they record)

| Date | Record | What it says | Source |
|---|---|---|---|
| 1086 | Domesday Book (Essex) | Geoffrey Talbot holds Liston under Hugh de Gournay III — the Talbot-Gournay tie a generation before Walter | [^rec-domesday] |
| c. 1090s–1120s | Rochester priory benefaction list (monastic register) | "William de Gurnai gave the tithe of Addington" — listed among donors of Henry I's generation (Henry I himself; Hugh Maminot) | [^rec-donorlist] |
| 1121 | Lewes priory confirmation | Odo de Dammartin has given half a virgate at Gatton, Surrey, to the Warenne family's own monastery | [^rec-lewes] |
| 1135×1154 | Enfeoffment recalled in the 1166 return | Manasser de Dammartin grants Walter a quarter knight's fee out of his Mendlesham fee "in the time of the war" | [^rec-carta] |
| 1135×1154 | New feoffment recalled in the Kent return | A William de Gornaco receives a half-fee of the Talbot-honour demesne, owing no service | [^rec-meduana] |
| 1150 | Missenden Abbey charter (monastic cartulary) | Walter de Gournay witnesses for Manasser de Dammartin and his wife Galiena | [^rec-missenden] |
| 1166 | Carta of Manasser de Danmartin (exchequer survey return) | Names Walter and states that "now William his son holds that part" — Walter dead or retired by Michaelmas 1166 | [^rec-carta] |
| 1166 | Carta of Walter de Meduana (exchequer survey return) | The Talbot-of-Swanscombe honour roster: Geoffrey Talbot's 20 fees in 1135; Manasser's 3 fees; the Gornaco half-fee | [^rec-meduana] |
| undated (episcopate of Gilbert de Glanville, 1185–1214, for the confirmations) | Charter of Galiena de Gurnay (Rochester register) | Confirms "the gift my grandfather William de Gurnay made" of Addington tithes, commuted to 5s. yearly from Addington's parson | [^rec-galiena] |
| c. 1181–90 | Norton Mandeville church grant (per VCH) | Bartholomew de Dammartin and "Galiena his mother" grant the church — the elder Galiena attested as Manasser's widow | [^rec-norton] |
| 17 Oct 1184 | Fine, with earl Hamelin's charter | Matthew de Gournay's marriage to Rose of Harpley, arranged by the earl (grandson's generation; details on the G29 companion) | [^rec-hamelin] |
| 1259 | Petition of Eustace de Montigny (*Les Olim*, French royal court register) | Recites that a William de Gournay held Montigny-sur-Andelle directly of the king, with a charter confirmed by Henry II; the petition itself was denied | [^rec-olim] |

[^rec-domesday]: Little Domesday (Essex), Liston; identification of "Goisfredus Talbot" per K. S. B. Keats-Rohan, *Domesday People* (1999), p. 126. Cross-reference, not a source: the verified Domesday table is at research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md §5.1.

[^rec-donorlist]: John Thorpe, *Registrum Roffense* (1769), priory benefaction list: "Willelmus de Gurnai dedit decimam de Edintune," in sequence with "Hugo pater Walkelini Maminot" and "Henricus rex primus." Extract: sources/corpus_supplement/registrum-roffense-addington-gurnay-extracts.md. Source ID: `registrum-roffense-1769`.

[^rec-lewes]: William Farrer, *Honors and Knights' Fees*, vol. 3 (1925), p. 313 (the 1121 confirmation of Lewes priory's possessions: "½ virgate given by Odo de Donmartin" at Gatton). Extract: sources/corpus_supplement/farrer-hkf-v3-swanscombe-warenne-dammartin-extracts.md. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.

[^rec-carta]: *The Red Book of the Exchequer*, ed. Hubert Hall, Rolls Series 99, vol. 1 (1896), pp. 409–410; *Liber Niger Scaccarii*, ed. Hearne (1774), vol. 1, p. 298, printed in Daniel Gurney, *Record*, Part II (1848), p. 288. Extract with translation: sources/corpus_supplement/redbook-exchequer-hall-v1-dammartin-gournay-cartae.md. Source IDs: `redbook-exchequer-hall-v1`, `liber-niger`, `dg-rec-pt2`.

[^rec-meduana]: Red Book, vol. 1, pp. 195–196 (carta of Walter de Meduana, Kent, 1166); quoted with the Talbot identification in Daniel Gurney, *Record*, Part II, p. 296 note (from Liber Niger vol. 1, p. 58). The honour's later history: Farrer, *Honors and Knights' Fees*, vol. 3 (1187 Mayenne/Munchensy moieties of "the honor of Talbot of Swanscombe"); Red Book scutage table ("Honor Walteri de Meduana ... per Ciciliam"). Source IDs: `redbook-exchequer-hall-v1`, `dg-rec-pt2`, `farrer-honors-knights-fees-v3-gurnay-extracts`.

[^rec-missenden]: J. G. Jenkins, ed., *The Cartulary of Missenden Abbey*, vol. 1 (Buckinghamshire Archaeological Society Records Branch 2, 1938), pp. 70–75, as reported by Douglas Richardson, soc.genealogy.medieval, 11 September 2002; the edition's witness list remains to be read.<!-- L-207 --> Source IDs: `jenkins-missenden-cartulary-v1`, `richardson-sgm-soc-genealogy-medieval-2002`.

[^rec-galiena]: Thorpe, *Registrum Roffense* (1769), p. 145, from BL Cotton MS Domitian A.X, f. 91; first quoted for this family in Daniel Gurney, *Record*, Part II, p. 296 note. The witness list is truncated ("Hijs test. &c.") in both prints.<!-- L-215 --> The 5s. composition recurs in the priory's episcopal confirmations, including Bishop Gilbert de Glanville's (1185–1214). Extract: sources/corpus_supplement/registrum-roffense-addington-gurnay-extracts.md. Source IDs: `registrum-roffense-1769`, `dg-rec-pt2`.

[^rec-norton]: *VCH Essex*, vol. 4 (1956), Norton Mandeville, pp. 152–154 (church). Extract: sources/corpus_supplement/vch-essex-vol4-norton-mandeville-extract.md. Source ID: `vch-essex-vol4`.

[^rec-hamelin]: C. T. Clay, ed., *Early Yorkshire Charters*, vol. 8 (1949), pp. 38–39 and 95. Extract: sources/corpus_supplement/eyc8-warenne-gournay-extracts.md. Source ID: `eyc8-warenne-clay-1949`. Full treatment: research/people/g29-matthew-de-gournay-fact-sheet.research.md (cross-reference, not a source).

[^rec-olim]: *Les Olim*, ed. Beugnot, vol. 1 (1839), p. 85, printed in full in Daniel Gurney, *Record*, Part II, p. 293. Source IDs: `les-olim`, `dg-rec-pt2`.

---

## Working Notes
```

**1.2 — DG-II Preface entry: add the 1166 return itself (Latin and English).**

str_replace old_string:
```
DG continues: "This Walter was, it appears, a son of Gerard de Gournay and Editha de Warren. The fiefs of the Gournays in Norfolk and Suffolk had been probably given in frank marriage to Gerard de Gournay by William second Earl Warren, on Gerard's marriage with his sister Editha, which took place about the year 1090."
```
new_string:
```
DG continues: "This Walter was, it appears, a son of Gerard de Gournay and Editha de Warren. The fiefs of the Gournays in Norfolk and Suffolk had been probably given in frank marriage to Gerard de Gournay by William second Earl Warren, on Gerard's marriage with his sister Editha, which took place about the year 1090."

The return itself, which DG prints at p. 288, reads:

> "Notum vobis facio, quod vobis facio servitium j militis de dominio meo, et tantum fecit pater meus in tota vita sua, et ego, post illius obitum, tantum feci die, qua Rex H[enricus] fuit vivus et mortuus. Et in tempore Gwerrae de illo feodo dedi Waltero de Gornaco j quartum militis. Et nunc illam partem tenet Willelmus, filius suus, in auxilium mihi illud servitium faciendo. Et de novo feffamento nichil habeo."

In plain English: "I do you the service of one knight from my demesne, as my father did all his life and as I have done since his death, as on the day King Henry [I] was alive and dead [1 December 1135]. And in the time of the war I gave Walter de Gournay a quarter of a knight's fee out of that fee. And now William his son holds that part, aiding me in performing that service. And of new feoffment I have nothing." The one surviving record of Walter's own century therefore names father and son together, dates the grant to the civil war of Stephen's reign (1135–54), and shows Walter dead or retired by Michaelmas 1166. DG worked from Hearne's 1774 edition of the Liber Niger; Hall's 1896 Rolls Series edition of the Red Book gives the critical text ("Waltero de Cornaco" with the Liber Niger reading "Gornaco" in the notes).[^rec-carta]
```

**1.3 — Note 104 entry: DG's ending position and the surrounding tradition.**

str_replace old_string:
```
M. De la Mairie conjectures that the village of "Bois Gautier" (near Montigny-sur-Andelle) was named after Walter de Gournay. This is geographically significant — Bois Gautier is in the Pays de Bray, near the family's Norman seat, suggesting Walter may have held a small parcel there before the junior line became primarily English.
```
new_string:
```
M. De la Mairie conjectures that the village of "Bois Gautier" (near Montigny-sur-Andelle) was named after Walter de Gournay. This is geographically significant — Bois Gautier is in the Pays de Bray, near the family's Norman seat, suggesting Walter may have held a small parcel there before the junior line became primarily English.

Note 104 is DG's ending position — "Walter de Gournay is proved to be certainly a son of Gerard" — and his view had strengthened steadily to reach it: 1845, "Walter de Gournai was, I think, undoubtedly another son of Gerard" (Part I p. 70); 1848, "it appears he was a younger son" (Part II p. 288), "probably son of Gerard" (pedigree p. 286), and, from the Norman severance alone, "must have been a son or grandson of Gerard" (p. 292); 1858, the proof above.[^dg-trajectory] The arithmetic also fixes Walter's birth between about 1090 and 1104 (Gerard was dead by 1104), and his death between 1150 (the Missenden witnessing) and Michaelmas 1166 (son William holding the quarter-fee). The tradition around DG carries the same identification: N.-R. P. de la Mairie (1852) writes that Girard left his goods to Hugues IV *"à l'exception des fiefs dont hérita son fils puîné, Gautier, tige de la branche des Gournay de Norfolk"* — "except the fiefs his younger son Gautier, root of the Norfolk Gournay branch, inherited" — and Pettigrew (1871) records the same, alongside Gerard's other children (Hugh; a daughter married to Richard Talbot; Gundred, wife of Neil d'Albini; and a son Renaud "ascribed to him").[^dg-tradition][^walter-alternatives-g31]

[^dg-trajectory]: Daniel Gurney, *Record of the House of Gournay*, Part I (1845/1848), p. 70; Part II (1848), pp. 286, 288, 292; Supplement (1858), Note 104, pp. 776–777. Source IDs: `dg-rec-pt1`, `dg-rec-pt2`, `dg-rec-supp`.

[^dg-tradition]: N.-R. P. de la Mairie, *Recherches Historiques ... sur les Possessions des Sires Normands de Gournay*, Tome I (Gournay-en-Bray, 1852), p. 80. T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (1871), pp. 185–186 (Source ID: `pettigrew-collectanea-house-gournay-1871`). The cluster shares one antiquarian transmission line (Cordier MS c. 1710–38 → Langloys → Potin → Potin de la Mairie 1842 → DG 1845 → Pettigrew/NRP-I), so it is deep rather than mutually independent. Renaud: Daniel Gurney, *Record*, Part I, p. 69 ("M. De La Mairie says ... some authors give to Gerard another son, Renaud de Gournay, who had a son Hugh"). Source ID: `dg-rec-pt1`. Geni curators (R Green, R.B. Stewart, Mellcene Smith) carry the same identification of Walter; Stewart's five-children list for Gerard reads "Hugues III, Gautier, Anseau, Gonnor and Gundred" (compiled-pedigree collector, noted as tradition only; profile https://www.geni.com/people/Gerard-de-Gournay-Baron-of-Gournay/6000000006582994318).

[^walter-alternatives-g31]: Two alternatives have been floated. Pattou's chart marks Walter *"possible petit-fils"* (possible grandson) of Gerard — a placement the Note 104 arithmetic closes (Source ID: `pattou-racines-histoire-gournay-2025`). A genealogy-forum post (Douglas Richardson, soc.genealogy.medieval, 11 September 2002; corrected repost 20 January 2003, Google Groups thread cPiFbsyHAa8) proposed that Walter belonged instead to the Addington, Kent, family of the name; the records it cited (Hasted vol. 4 pp. 544–545; Copinger vol. 3 pp. 277–278; the Hatton Book of Seals Nos. 332, 350, 409; VCH Essex vol. 4 pp. 151–154; the Rochester register; the 1166 cartae; with C. F. H. Evans, "Dammartin," *Genealogists' Magazine* 15 (1965), 53–63, and Jenkins's Missenden cartulary still to be read) were examined in July 2026 and do not bear the alternative out — see the Dammartin and Addington entries below. Source ID: `richardson-sgm-soc-genealogy-medieval-2002`.
```

**1.4 — Les Olim entry: corrected to what the record is.**

str_replace old_string:
```
### Les Olim — proof of blood descent (DG-I p. 293)
2026-04-18 — DG-I p. 293 cites "Les Olim" (French royal court records) for proving "the Gurneys of Swathings to be of the blood of the Lords of Gournay." This is a legal record — an official French court determination recognizing the junior branch as legitimate Gournay blood. Combined with the Liber Niger entry and the Montigny-sur-Andelle parage holding (see G30), this constitutes a robust evidentiary chain for the junior branch's descent from Gerard.
```
new_string:
```
### Les Olim and Montigny-sur-Andelle — the Norman severance (DG-II pp. 292–293)
In 1259 Eustace de Montigny petitioned the French crown to sell wood from his fief of Montigny-sur-Andelle free of the *tiers et danger* tax (a ducal levy of roughly a third plus a tenth on wood sales). His recital, printed in full by DG at p. 293:

> "...prout antecessores sui semper fecerunt et tenuerunt de dono domini Guilielmi de Gornaio, qui sibi dedit ita libere et quitte, sicut ipsemet tenebat a Domino Rege, de quo sibi fecit cartam quam Rex Henricus confirmavit."

"...as his ancestors always did and held, of the gift of the lord William de Gournay, who gave it to them as freely and quit as he himself held it of our lord the king, of which he made them a charter, which King Henry [II of England, as duke of Normandy] confirmed." The court denied the petition itself — "Non probat idem Eustachius ... nec vendat" ("Eustace does not prove it; let him not sell") — so the record is a denied wood-sale request, not a court declaration about the Gurneys; its evidentiary value is the recital, which preserves that a William de Gournay held Montigny directly of the duke-king before 1204, with royal confirmation.[^rec-olim] DG identified that William as Walter's son (the senior line had no William in that generation — its heads were Hugh IV, then Hugh V), read the tenure as *parage* — the Norman custom by which a younger son held his severed share of the family fief "pari conditione," on equal terms with his elder brother, a partition among sons rather than a grant to outsiders — and called it "an undoubted proof of his descent in blood from the Barons of Gournay."[^olim-parage] Two anchors tie Montigny to Gerard's own estate: its dependency Massy had been part of Gerard's honour (Gerard confirmed his father Hugh III's gift of Massy church to Bec abbey), and Thomas Stapleton, editor of the Norman exchequer rolls, held that the castle of Argueil and its dependencies were the portion of the great Bray fief severed for Walter at Gerard's death, about 1104; DG dates the severance to that death because Walter and William both lived before 1180, and no severance was possible while Hugh IV held the undivided fief (1104–1180).[^olim-anchors]

[^olim-parage]: Daniel Gurney, *Record*, Part II, pp. 292 and 298 (Appendix XLVI, "On the tenure in parage," with Ducange's definition and the Grand Coutumier de Normandie); "incontestable proof": Part II preface, p. 278. Source ID: `dg-rec-pt2`.

[^olim-anchors]: Daniel Gurney, *Record*, Part II, pp. 292–293 (Massy, citing *Histoire de Haute Normandie*, vol. 1, p. 583; Stapleton's opinion; the 1104–1180 dating argument; Argueil taken and destroyed by Philip Augustus in 1202). Source ID: `dg-rec-pt2`.
```

**1.5 — Dampmartin entry: the patron family as the records show it.**

str_replace old_string:
```
2026-04-18 — Walter held his Suffolk quarter-fee under Manasser de Dampmartin. The Dampmartins (or Dammartin) were a significant Anglo-Norman family. DG-I p. 278 notes that this tenure arrangement connects Walter to the broader post-Conquest feudal network. The French Wikipedia article on the Gournay family mentions the Dampmartins as having a specific relationship to the Gournays, and the tenure of land under them (rather than directly from the crown) is consistent with Walter being a younger son without independent baronial status.
```
new_string:
```
Walter held his Suffolk quarter-fee under Manasser de Dammartin, and the patron family is well documented. Odo de Dammartin (d. 1131) was enfeoffed of Mendlesham by Henry I; his widow Basilia paid sixty marks for her dower in 1130, and DG conjectured from her name that she "might possibly ... be a daughter of Hugh de Gournay and Basilia Flaitel" — which, if right, would make Manasser Walter's first cousin.[^damm-odo] Manasser (d. 1178/9) succeeded; his sons Bartholomew (d. before 1190, without children) and William de Dammartin (d. 1195, holding Mendlesham and Norton Mandeville, Essex) followed; William's daughter and heir Galiena de Dammartin (underage at her first marriage c. 1197; d. after 1258) married thirdly Ernald de Mandeville, and her Mandeville sons took the estates.[^damm-descent] The family stood inside the Warenne circle — the lordship of Walter's mother's family: Odo gave land at Gatton, Surrey, to Lewes priory (the Warennes' own monastery) by 1121; a William de Dammartin held eleven and a half knights' fees of Earl Warenne in Surrey in 1166, the largest Surrey tenancy in the earl's return; and the Mendlesham fee "which was William de Danmartin's" was in Warenne hands by 1210–12.[^damm-warenne] Manasser also held three knights' fees in Kent, of the honour Geoffrey Talbot had held in chief at Henry I's death — the Talbots being the Gournays' Domesday tenants at Liston, Essex, and in-laws through Richard Talbot's marriage to Gerard's daughter.[^damm-talbot] Tenure under such a lord, rather than directly from the crown, is consistent with Walter being a younger son without independent baronial status, provided for within his mother's and sister's family networks.

**Manasser's wife Galiena and the Addington Gurnays.** Manasser married a woman named Galiena: she appears beside him in the 1150 Missenden charter Walter witnessed, and as "Galiena his mother" beside her son Bartholomew granting Norton Mandeville church c. 1181–90.[^rec-missenden][^rec-norton] She was a Gurnay of Addington, Kent: an undated charter of "Galiena de Gurnay" in the Rochester register confirms "the gift my grandfather William de Gurnay made" of Addington tithes — "Willelmus de Gurnay, avus meus ... dedit ecclesie sancti Andree Rowcestr. ... quasdam decimas in villa sua de Edintune" — commuted to five shillings yearly from Addington's parson.[^rec-galiena] Her grandfather William de Gurnay held Addington from about the 1090s (the manor had been Bishop Odo of Bayeux's until his 1088 forfeiture), and his tithe gift sits in the Rochester benefaction list among donors of Henry I's generation — so he was of Gerard's generation.[^rec-donorlist][^addington-hasted] Hasted's descent of Addington — "held as one manor, by William de Gurnay, and afterwards by Galiena de Gurnay, his grandchild; they were succeeded in the possession of this place by the family of Mandeville ... who held it of the family of Montchensie, as capital lords of the fee" — compresses the same chain the Dammartin records supply in full: William of Addington → Galiena (I), wife of Manasser → her granddaughter Galiena (II), whose Mandeville marriage carried Addington and Mendlesham together to the Mandevilles.[^addington-hasted][^damm-descent] There were two Galienas, grandmother and granddaughter; the elder married Manasser by 1150, so her grandfather cannot have been Walter's son William (born c. 1120) — DG's tentative suggestion to that effect ("It seems likely that it was this same William de Gurnay who held the manor of Edintune") fails on chronology, and DG himself flagged the loose end: "Why this Kentish fief did not descend in the same line as those in Norfolk I do not discover. There were Gournays at a later period in Kent. The will of John Gurney, of Northfleet, Kent, was proved in 1475."[^dg-addington-note] In the same Kent honour, the 1166 return records a William de Gornaco holding a half-fee of the lord's demesne, granted during Stephen's reign, owing no service; DG read him as Walter's son, "enfeoffed by the Talbots, his relations," and an Addington kinsman is the other candidate — either way the holding sits among the family's connections.[^rec-meduana][^dg-addington-note]

[^damm-odo]: Daniel Gurney, *Record*, Part II, p. 290 (Appendix XLV, "On the Dammartins in England"): Odo's death; Basilia's dower payment (Mag. Rot. Pip. 31 Hen. I, p. 94); Odo the younger's 100-mark relief; the Basilia name-conjecture; Manasser as justice itinerant under Henry II; the family's later FitzOtho / Botetourt descent at Mendlesham and Strumshaw. Source ID: `dg-rec-pt2`.

[^damm-descent]: *Sir Christopher Hatton's Book of Seals*, ed. Loyd & Stenton (1950), editorial notes to Nos. 332 and 409 (the full descent, with Pipe Roll, Curia Regis, Rotuli Hundredorum, and Book of Fees references); *VCH Essex*, vol. 4 (1956), pp. 151–152; W. A. Copinger, *The Manors of Suffolk*, vol. 3 (1909), pp. 277–278 (including the Hundred Rolls' compressed version and the two contemporary Dammartin branches at Mendlesham). Extracts: sources/corpus_supplement/hatton-book-of-seals-dammartin-gurnay-extracts.md, vch-essex-vol4-norton-mandeville-extract.md, copinger-manors-suffolk-v3-mendlesham-extract.md. Source IDs: `hatton-book-of-seals-1958`, `vch-essex-vol4`, `copinger-manors-suffolk-v3`.

[^damm-warenne]: Farrer, *Honors and Knights' Fees*, vol. 3, p. 313 (Gatton/Lewes, 1121); Red Book, vol. 1, earl Warenne's carta of 1166 ("In Surreia: Willelmus de Danmartin, xj milites et dimidium") and 1210–12 returns ("Willelmus de Warenna, j militem in Mendlesham quod fuit Willelmi de Danmartin"). Source IDs: `farrer-honors-knights-fees-v3-gurnay-extracts`, `redbook-exchequer-hall-v1`.

[^damm-talbot]: Carta of Walter de Meduana, Red Book, vol. 1, pp. 195–196 ("Manasser de Danmartin, iij milites" under the fee Geoffrey Talbot held in chief in 1135). The Talbot–Gournay ties: Daniel Gurney, *Record*, Part I, pp. 69–70 (the Talbot marriage; "The family of Talebot held a large fee under the Gournays at Buchy, Beaubec, &c.; and Geoffrey Talebot held lands in Essex under Hugh de Gournay III., as appears by Domesday"). Source IDs: `redbook-exchequer-hall-v1`, `dg-rec-pt1`.

[^addington-hasted]: Edward Hasted, *The History and Topographical Survey of the County of Kent*, 2nd ed., vol. 4 (1798), pp. 544–545 (descent; Montchensies as capital lords "as of his manor of Swanscombe") and p. 547 (the church account of the tithe gift and its post-Dissolution fate). Extract: sources/corpus_supplement/hasted-kent-vol4-addington-extract.md. Source ID: `hasted-kent-vol4`.

[^dg-addington-note]: Daniel Gurney, *Record*, Part II, pp. 296–297 note. Source ID: `dg-rec-pt2`.
```

**1.6 — Stephen's-reign entry: the war-time grant fact.**

str_replace old_string:
```
2026-04-18 — Walter's documented activity falls within the reign of Stephen (1135–1154), the period of English civil war known as "The Anarchy." This was a dangerous time for minor landholders. The fact sheet notes this but could emphasize it more — Walter's survival as a mesne tenant during this period shows practical resilience. His elder brother Hugh IV (senior line) was more directly involved in the political upheavals.
```
new_string:
```
Walter's documented activity falls within the reign of Stephen (1135–1154), the period of English civil war known as "The Anarchy." His one grant of land came "in tempore Gwerrae" — in the war itself — and the parallel Kent grant to a William de Gornaco was likewise "in tempore Regis Stephani."[^rec-carta][^rec-meduana] This was a dangerous time for minor landholders; there is no record of Walter in any political or military event. His elder brother Hugh IV (senior line) was more directly involved in the political upheavals.
```

**1.7 — Landholdings table.**

str_replace old_string:
```
| Place | Period | Notes |
|---|---|---|
| Suffolk (quarter knight's fee) | Reign of Stephen (1135–1154) | Under Manasser de Dampmartin. Liber Niger Scaccarii, vol. i, p. 298. |
| [Hardingham/Swathings, Norfolk](../places/hardingham.md) | fl. c. 1108–1154 | Held as mesne lord under the senior Gournay line |
| [Runhall, Norfolk](../places/runhall.md) | fl. c. 1108–1154 | Hamlet/berewic to Swathings |
| Bois Gautier, Normandy (?) | Uncertain | M. De la Mairie conjectures the village was named after Walter (DG-Supp Note 104) |
```
new_string:
```
| Place | Period | Notes |
|---|---|---|
| Quarter knight's fee out of the Dammartin fee of Mendlesham, Suffolk | granted 1135×1154; held by son William by 1166 | "In tempore Gwerrae de illo feodo dedi Waltero de Gornaco j quartum militis" — Manasser's 1166 return. The Dammartin Suffolk fiefs were at Mendlesham and Cotton, Hartismere hundred; the quarter-fee's own vill is not named.[^rec-carta] |
| [Hardingham/Swathings, Norfolk](../places/hardingham.md) | attribution to Walter himself uncertain | DG: "It does not appear whether Walter de Gournay held the manors of Swathings and Hingham Gurney's, possessed by his descendants"; the manors were "given by the Norman Gourneys to this younger branch ... either to this William de Gournay, or his father Walter."[^landhold-swathings] |
| [Runhall, Norfolk](../places/runhall.md) | attribution to Walter himself uncertain | Hamlet/berewic to Swathings; first securely documented with son William, lord of Runhall under Henry II.[^landhold-swathings] |
| Portion of the Bray fief, Normandy (Argueil / Montigny) | severed c. 1104 (inference) | Stapleton's opinion: Argueil and dependencies were the Bray portion severed for Walter at Gerard's death; son William held Montigny-sur-Andelle directly of the crown.[^olim-anchors][^rec-olim] |
| Bois Gautier, Normandy (?) | Uncertain | M. De la Mairie conjectures the village was named after Walter (DG-Supp Note 104) |

[^landhold-swathings]: Daniel Gurney, *Record*, Part II, pp. 288 and 295; Runhall under Henry II: same volume, p. 294, citing Blomefield (Runhall, vol. ii, p. 474). Source ID: `dg-rec-pt2`.
```

**1.8 — Open Questions.**

str_replace old_string:
```
1. **Bois Gautier:** Can this place-name attribution be verified in published Norman toponymy? De la Mairie's conjecture (cited in DG-Supp Note 104) would link Walter to a specific Norman location.
2. **Les Olim passage:** The specific text of the Les Olim ruling recognizing the Swathings Gurneys as Gournay blood should be located. Beugnot's 1839–1848 edition is the standard publication.
3. **Walter's wife:** No wife is named in any source. Son William is documented, but the mother is unknown.
4. **Dampmartin pedigree:** What was the specific relationship between the Dampmartins and the Gournays? DG-I p. 278 implies a feudal connection; French Wikipedia suggests something closer.
```
new_string:
```
1. **Bois Gautier:** Can this place-name attribution be verified in published Norman toponymy? De la Mairie's conjecture (cited in DG-Supp Note 104) would link Walter to a specific Norman location.
2. **Les Olim on Gallica:** The petition text is held via DG's print (Part II p. 293); verify Beugnot's vol. 1 p. 85 directly.<!-- L-48 -->
3. **Walter's wife:** No wife is named in any source. Son William is documented, but the mother is unknown.
4. **Missenden witness list:** Jenkins's edition (vol. 1, pp. 70–75) remains to be read for the 1150 charter's witnesses and Walter's style.<!-- L-207 -->
5. **Galiena's witnesses:** the truncated witness list of Galiena de Gurnay's Rochester charter (BL Cotton MS Domitian A.X, f. 91).<!-- L-215 -->
6. **The Kent William de Gornaco of 1166:** Walter's son (DG's suggestion) or an Addington kinsman?
7. **Basilia de Dammartin:** Can DG's name-conjecture (a daughter of Hugh de Gournay III) be tested in the Bec or pipe-roll material?
8. **Reference works still to be read:** Keats-Rohan, *Domesday Descendants*; Loyd, *Origins of Some Anglo-Norman Families* (Gurnai entry); Evans, "Dammartin" (1965); Cooke, *Early History of Mapledurham* pp. 9–11, 85; Power, *Norman Frontier* pp. 355–357 (on interlibrary loan); Tanner p. 315; Gervers p. 216.<!-- L-208 through L-214 -->
```

**1.9 — Sources Consulted: add the newly examined sources (existing lines kept).**

str_replace old_string:
```
- Hannay, *Three Hundred Years* (1867): Walter confirmed as "the proved ancestor of the Gournays, afterwards Gurneys, of Swathing and West Barsham in Norfolk." [Hannay]
```
new_string:
```
- Hannay, *Three Hundred Years* (1867): Walter confirmed as "the proved ancestor of the Gournays, afterwards Gurneys, of Swathing and West Barsham in Norfolk." [Hannay]
- Red Book of the Exchequer, ed. Hall (1896), vol. 1: cartae of Manasser de Danmartin (pp. 409–410) and Walter de Meduana (pp. 195–196); Odo and Aubrey de Danmartin; earl Warenne's carta; 1210–12 Mendlesham return. Extract: sources/corpus_supplement/redbook-exchequer-hall-v1-dammartin-gournay-cartae.md. [redbook-exchequer-hall-v1]
- Thorpe, Registrum Roffense (1769): Galiena de Gurnay's charter (p. 145); the benefaction list; episcopal confirmations. Extract: sources/corpus_supplement/registrum-roffense-addington-gurnay-extracts.md. [registrum-roffense-1769]
- Hasted, History of Kent, 2nd ed., vol. 4 (1798), pp. 542–547 (Addington). Extract: sources/corpus_supplement/hasted-kent-vol4-addington-extract.md. [hasted-kent-vol4]
- Loyd & Stenton, Sir Christopher Hatton's Book of Seals (1950), Nos. 332, 350, 409 with editorial notes. Extract: sources/corpus_supplement/hatton-book-of-seals-dammartin-gurnay-extracts.md. [hatton-book-of-seals-1958]
- VCH Essex, vol. 4 (1956), Norton Mandeville, pp. 150–154. Extract: sources/corpus_supplement/vch-essex-vol4-norton-mandeville-extract.md. [vch-essex-vol4]
- Copinger, Manors of Suffolk, vol. 3 (1909), pp. 277–278 (Mendlesham). Extract: sources/corpus_supplement/copinger-manors-suffolk-v3-mendlesham-extract.md. [copinger-manors-suffolk-v3]
- Farrer, Honors and Knights' Fees, vol. 3 (1925): Swanscombe moieties; Lewes priory 1121; Swathings in the Warenne fee (p. 422); the Gournay account (pp. 420–423). Extracts: sources/corpus_supplement/farrer-hkf-v3-swanscombe-warenne-dammartin-extracts.md and farrer-honors-knights-fees-v3-gurnay-extracts.txt. [farrer-honors-knights-fees-v3-gurnay-extracts]
- Clay, Early Yorkshire Charters, vol. 8 (1949), pp. 6–7 (Gerard and Edith "among other children"), 38–39, 95 (the Hamelin/Rose charter — see the G29 companion); vol. 9 (1952), pp. 45–47 (Stuteville marriage: Eidiva daughter of Hugh IV, correcting the older "Gunnora"). Extracts: sources/corpus_supplement/eyc8-warenne-gournay-extracts.md, eyc9-stuteville-gournay-extracts.md. [eyc8-warenne-clay-1949; eyc9-stuteville-clay-1952]
- Fowler, Note iiD/11 (De Gournai), Bedfordshire Historical Record Society vol. 7 (1926), pp. 153–157: the senior baronial succession only; names no children of Gerard beyond Hugh and Gundred. Extract: sources/corpus_supplement/bhrs-v7-fowler-gournay-note.md. [bhrs-v7-fowler-1926]
- Richardson, soc.genealogy.medieval posts (11 Sep 2002; corrected 20 Jan 2003). [richardson-sgm-soc-genealogy-medieval-2002]
- NRP de la Mairie (1852), p. 80; Pettigrew (1871), pp. 185–186; Pattou, Racines & Histoire, p. 5. [pettigrew-collectanea-house-gournay-1871; pattou-racines-histoire-gournay-2025]
- Les Olim, ed. Beugnot, vol. 1, p. 85, via DG-II p. 293 print. [les-olim]
```

**1.10 — Conflicting Information: record the corrections.**

str_replace old_string:
```
None identified. Walter's genealogical position is well-established by DG's generational proof (Note 104) and the independent Liber Niger entry.
```
new_string:
```
Walter's genealogical position is well-established by DG's generational proof (Note 104) and the independent 1166 return. Three older statements have been corrected against the records:

| Claim | Older statement | Corrected reading | Basis |
|---|---|---|---|
| Walter's birth | "c. 1108" | Between about 1090 and 1104 | Gerard died 1104; DG-Supp Note 104 places the younger sons 1090×1104.[^dg-trajectory] |
| Walter's death | "c. 1150–1165" (from William "living 1167") | Between 1150 and Michaelmas 1166 | Witness in 1150; son William holds the quarter-fee in the 1166 return.[^rec-carta][^rec-missenden] |
| The *Les Olim* record | "a French court determination recognizing the junior branch as legitimate Gournay blood" | A denied 1259 petition whose recital preserves William de Gournay's in-chief Montigny tenure with Henry II's confirmation; the blood argument is DG's inference from the recital, parage, and Massy | The petition text itself.[^rec-olim] |
| Addington's William de Gurnay | DG's suggestion: the same man as Walter's son William | A Kent Gurnay of Gerard's generation — Galiena (I) was a wife by 1150, so her grandfather cannot be a man born c. 1120 | Rochester benefaction-list dating; the Dammartin descent.[^rec-donorlist][^damm-descent] |
```

**1.11 — Fact Sheet Improvement Notes: retire the promoted items.**

str_replace old_string:
```
1. **Les Olim:** The fact sheet could note that a French royal court ruling formally recognized the Swathings Gurneys as Gournay blood. This strengthens the "junction point" narrative.
2. **Bois Gautier:** If verified, this place-name attribution adds a tangible Norman footprint for an ancestor otherwise known only through English records.
3. **Naming origin:** DG-Supp Note 104's suggestion that Walter was named after Walter Giffard (Earl of Buckingham) or Walter de la Ferté is a humanizing detail.
4. **Anarchy context:** The narrative could draw out the significance of surviving as a minor landholder during Stephen's reign.
```
new_string:
```
1. The earlier notes here (Les Olim, Bois Gautier, naming origin, Anarchy context) are in the fact sheet. The Les Olim item is superseded as phrased — the fact sheet now presents the 1259 petition's recital of the Montigny tenure rather than a court "recognition" (see Conflicting Information above).
2. **Bois Gautier** remains conjectural; if toponymy ever verifies it, the fact-sheet bullet can firm up.
```

**End of Item 1.**

---

## Item 2 — G31 fact sheet edits (promote)

Target file: `fact-sheets/g31-walter-de-gournay-fact-sheet.md`. Sixteen str_replace operations (2.1–2.16), each with verbatim old/new strings. Two are factual corrections (birth window; the *Les Olim* framing); the rest promote the 1166 return, the family-network findings, and the sharpened death window. Do not mirror to `site/`.

**2.1 — pageHeading (birth-window correction).**

str_replace old_string:
```
pageHeading: Walter de Gournay (fl. c. 1108–1154)
```
new_string:
```
pageHeading: Walter de Gournay (born c. 1090–1104, died by 1166)
```

**2.2 — JSON-LD birthDate (same correction).**

str_replace old_string:
```
    "birthDate": "c. 1108",
```
new_string:
```
    "birthDate": "c. 1090/1104",
```

**2.3 — Born vital.**

str_replace old_string:
```
    <div class="fact-value">c. 1108, probably England or Normandy. Youngest son of Gerard de Gournay (G32) and <a href="https://en.wikipedia.org/wiki/De_Warenne_family">Edith de Warenne</a>. The genealogist Daniel Gurney suggested he may have been named after his father's kinsman <a href="https://en.wikipedia.org/wiki/Walter_Giffard,_1st_Earl_of_Buckingham">Walter Giffard, Earl of Buckingham</a>, or after Walter de la Ferté. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```
new_string:
```
    <div class="fact-value">Between about 1090 and 1104, Normandy or England. Youngest son of Gerard de Gournay (G32) and <a href="https://en.wikipedia.org/wiki/De_Warenne_family">Edith (Ediva) de Warenne</a> — Gerard's heir Hugh was born about 1090 and Gerard died in 1104, so the younger sons fall in that window. The genealogist Daniel Gurney suggested he may have been named after his father's kinsman <a href="https://en.wikipedia.org/wiki/Walter_Giffard,_1st_Earl_of_Buckingham">Walter Giffard, Earl of Buckingham</a>, or after Walter de la Ferté. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```

**2.4 — Died vital (sharpened window).**

str_replace old_string:
```
    <div class="fact-value">Dates uncertain. Active during the reign of <a href="https://en.wikipedia.org/wiki/Stephen,_King_of_England">King Stephen</a> (1135–1154). Son William I living 1167, suggesting Walter died c. 1150–1165. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```
new_string:
```
    <div class="fact-value">Between 1150 and 1166. He witnessed a charter in 1150; by the great survey of 1166 his son William held his Suffolk land in his place. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

**2.5 — Highlights bullet: the Norman foothold (replaces the Les Olim overstatement).**

str_replace old_string:
```
  <li><strong>Confirmed as Gournay blood by a French royal court.</strong> The <em>Les Olim</em> — the official records of the French royal court (Curia Regis / Parlement) — formally recognized the Swathings Gurneys as legitimate blood descendants of the Lords of Gournay. The same Gournay-blood descent is independently anchored by Walter's <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a> entry and by the <a href="https://en.wikipedia.org/wiki/Parage">parage</a> tenure of Montigny-sur-Andelle that his son later held. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```
new_string:
```
  <li><strong>His family's Norman foothold survives in the French crown's own records.</strong> Walter's son William held Montigny-sur-Andelle — in the Gournays' home country of Bray — directly of the crown, with a charter confirmed by King Henry II. A 1259 petition preserved in the <em>Les Olim</em>, the registers of the French royal court, recites that tenure; and the holding has the shape of <a href="https://en.wikipedia.org/wiki/Parage">parage</a>, the Norman custom by which a younger son held his share of the family estate on equal terms with his elder brother — a form of holding reserved for sons of the house. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

**2.6 — Highlights bullet: the 1166 return, with Manasser's own words.**

str_replace old_string:
```
  <li><strong>Documented in the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii">Black Book of the Exchequer</a>, c. 1166.</strong> The <em>Liber Niger Scaccarii</em> — one of the most authoritative financial records of medieval England — records Walter as holding a quarter knight's fee in Suffolk under Manasser de Dampmartin. This is the primary document that places Walter in the historical record as an identified, landed individual. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```
new_string:
```
  <li><strong>Named in the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii">Black Book of the Exchequer</a>, 1166.</strong> When Henry II surveyed every baron's knights, Walter's lord Manasser de Dampmartin reported in his own words: <em>"in the time of the war I gave Walter de Gournay a quarter of a knight's fee — and now William his son holds that part."</em> One sentence, but it fixes Walter's lordship, his civil-war enfeoffment, his son, and his death by 1166. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

**2.7 — Narrative paragraph 1.**

str_replace old_string:
```
Walter de Gournay occupies a peculiar position in this family history. He is, genealogically, one of the most important ancestors in the entire line — the single person through whom every English and American Gurney descends — and yet he is also one of the least documented. A single sentence in the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a>, the Black Book of the Exchequer compiled c. 1166, establishes that he held lands in Suffolk under Manasser de Dampmartin. Daniel Gurney's identification of him as the youngest son of Gerard de Gournay (G32) and Edith de Warenne rests on the pedigree's internal logic, the geographical pattern of the estates, and — most critically — the Montigny-sur-Andelle tenure that his son William inherited, which could only have been granted to a blood relative of the senior Gournay lords.
```
new_string:
```
Walter de Gournay occupies a peculiar position in this family history. He is, genealogically, one of the most important ancestors in the entire line — the single person through whom every English and American Gurney descends — and yet he is also one of the least documented. He appears once in the records of his own century: in 1166, when Henry II surveyed his barons' knights, Walter's lord Manasser de Dampmartin reported that "in the time of the war" — the civil war of Stephen's reign — "I gave Walter de Gournay a quarter of a knight's fee out of that fee; and now William his son holds that part, aiding me in performing that service." That single return, preserved in the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a> (the Black Book of the Exchequer), names father and son together and anchors the whole Norfolk branch that followed. <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup>
```

**2.8 — Narrative paragraph 2.**

str_replace old_string:
```
Walter appears to have received his portion of the family's English holdings as a younger son's share when his father Gerard died in Palestine before 1104. The estates he held — <a href="https://en.wikipedia.org/wiki/Runhall">Runhall</a> and Swathings in <a href="https://en.wikipedia.org/wiki/Hardingham">Hardingham</a>, Norfolk, and lands in Suffolk — were part of the Norfolk and Suffolk manors that had come into the Gournay family through Gerard's marriage to Edith de Warenne. Under Norman custom, a younger son could hold a portion of the fief "in <a href="https://en.wikipedia.org/wiki/Parage">parage</a>" — at equal tenure with his elder brother — and this is precisely the tenure William de Gournay I held for Montigny-sur-Andelle. Parage was not available to vassals or tenants; it required blood descent. Daniel Gurney called this "incontestable proof of his descent in blood from the Barons of Gournay."
```
new_string:
```
He was the youngest son of Gerard de Gournay (G32) and Edith de Warenne. The family's arithmetic places him: Gerard's heir Hugh was of full age in 1112 (so born about 1090), Gerard died in 1104, and Walter's grandson Matthew was already witnessing deeds around 1160 — leaving room for Walter only in the generation of Gerard's sons. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup> A younger son's share of the family estate followed him: a portion of the great Norman fief of Bray appears to have been severed at Gerard's death in Walter's favour, and his son William held Montigny-sur-Andelle — deep in the family's home country — directly of the crown, in the manner of "<a href="https://en.wikipedia.org/wiki/Parage">parage</a>," the Norman custom by which a younger son held his severed share on equal terms with his elder brother. Parage was a partition among sons, not a grant to outsiders; Daniel Gurney called the Montigny tenure "incontestable proof of his descent in blood from the Barons of Gournay." The Norfolk manors his descendants held — <a href="https://en.wikipedia.org/wiki/Runhall">Runhall</a> and Swathings in <a href="https://en.wikipedia.org/wiki/Hardingham">Hardingham</a> — they held under the senior Gournay lords, within the estates that had come to the family through Gerard's Warenne marriage. <sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>
```

**2.9 — Narrative paragraph 3 (replaces the Les Olim sentence; adds the family-network paragraph).**

str_replace old_string:
```
The proof is further strengthened by an entry in the <em>Les Olim</em>, the records of the French royal court, which formally recognized the Swathings Gurneys as being of the blood of the Lords of Gournay. The *Liber Niger*, the parage tenure, and the *Les Olim* ruling independently confirm Walter's descent from Gerard.
```
new_string:
```
The world Walter moved in was his mother's and sister's world. The Dampmartins who provided his Suffolk land were men of the Warenne circle — Manasser's father had endowed Lewes Priory, the Warenne family's own monastery, by 1121, and a Dampmartin was the largest Warenne tenant in Surrey in 1166 — so a younger son of Edith de Warenne settling on a Dampmartin fee was being provided for inside his mother's family's network. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup> The same pattern shows in Kent, where Walter's sister had married Richard Talbot: in the Talbot honour of Swanscombe, a William de Gournay received a half knight's fee, free of all service, during the same civil war. A generation later the head of the Warenne family himself — Earl Hamelin, half-brother of King Henry II — personally gave Walter's grandson Matthew an heiress in marriage, and with her the manor of Harpley that anchored the family for two centuries. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup>
```

**2.10 — Citation n2 (died).**

str_replace old_string:
```
  <li id="n2">No death date in any source. Son William I living 1167 (Daniel Gurney, <em>Record</em>, Part I (1848), p. 278); active generation therefore c. 1108–c. 1155. <a class="citation-back" href="#ref-2">↩</a></li>
```
new_string:
```
  <li id="n2">Living 1150: witness to a Missenden Abbey charter for Manasser de Dampmartin and his wife Galiena (Douglas Richardson, soc.genealogy.medieval, 11 September 2002, citing J. G. Jenkins, ed., <em>The Cartulary of Missenden Abbey</em>, vol. 1 (1938), pp. 70–75). Dead or retired by Michaelmas 1166: his son William held the quarter-fee in Manasser de Dampmartin's return of that year (<em>Red Book of the Exchequer</em>, ed. Hubert Hall (1896), vol. 1, pp. 409–410; <em>Liber Niger Scaccarii</em>, ed. Hearne (1774), vol. 1, p. 298). Source IDs: <code>richardson-sgm-soc-genealogy-medieval-2002</code>, <code>redbook-exchequer-hall-v1</code>, <code>liber-niger</code>. <a class="citation-back" href="#ref-2">↩</a></li>
```

**2.11 — Citation n7 (Les Olim / Montigny, corrected).**

str_replace old_string:
```
  <li id="n7">Daniel Gurney, <em>Record</em>, Part I (1848), p. 293: <em>Les Olim</em> cited for proving "the Gurneys of Swathings to be of the blood of the Lords of Gournay." Same volume, p. 278: Montigny-sur-Andelle parage tenure as "incontestable proof." <a class="citation-back" href="#ref-7">↩</a></li>
```
new_string:
```
  <li id="n7"><em>Les Olim</em> (registers of the French royal court), ed. Beugnot, vol. 1 (1839), p. 85: the 1259 petition of Eustace de Montigny, printed in full in Daniel Gurney, <em>Record</em>, Part II (1848), p. 293 — its recital states that his ancestors held Montigny "of the gift of the lord William de Gournay, who gave it to them as freely as he himself had held it of our lord the king, for which gift he made them a charter, which King Henry [II] confirmed." The court denied the petition itself; the tenure recital is the evidence. Parage and the "incontestable proof" phrasing: Daniel Gurney, <em>Record</em>, Part II, pp. 278, 292, and Appendix XLVI (p. 298); the severance of the Bray portion at Gerard's death and Stapleton's Argueil opinion, same volume, pp. 292–293. Descendants' tenure of Swathings under the senior lords: Daniel Gurney, <em>Record</em>, Part II, p. 295; William Farrer, <em>Honors and Knights' Fees</em>, vol. 3 (1925), p. 422. Source IDs: <code>les-olim</code>, <code>dg-rec-pt2</code>, <code>farrer-honors-knights-fees-v3-gurnay-extracts</code>. <a class="citation-back" href="#ref-7">↩</a></li>
```

**2.12 — Citation n8 (the dispute, updated).**

str_replace old_string:
```
  <li id="n8">Daniel Gurney, <em>Record</em>, Part I (1848), pp. 277–278 and pedigree p. 286. The adoption on this site of Daniel Gurney's "Walter as son of Gerard" identification is a conscious editorial choice; an independent line of modern scholarship — most fully argued by Douglas Richardson, soc.genealogy.medieval, 11 September 2002 (Google Groups thread <code>cPiFbsyHAa8</code>), drawing on Hasted vol. 4, Copinger <em>Manors of Suffolk</em> vol. 3, Loyd & Stenton <em>Hatton Book of Seals</em>, <em>VCH Essex</em> vol. 4, and <em>Genealogist</em> vol. 15 — rejects the Gerard-paternity identification on English-side feudal evidence. The full case is at <a href="https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/walter-de-gournay-as-son-of-gerard.md"><code>research/case-files/walter-de-gournay-as-son-of-gerard.md</code></a>. Source IDs: <code>dg-rec-pt1</code>, <code>richardson-sgm-soc-genealogy-medieval-2002</code>. <a class="citation-back" href="#ref-8">↩</a></li>
```
new_string:
```
  <li id="n8">Daniel Gurney, <em>Record</em>, Part I (1848), pp. 277–278 and pedigree p. 286; Part II (1848), p. 288; Supplement (1858), Note 104, pp. 776–777 (the generational proof). A genealogy-forum post (Douglas Richardson, soc.genealogy.medieval, 11 September 2002) proposed instead that Walter belonged to a Kent family of the same name at Addington; the records it cited were examined in July 2026 and do not bear the alternative out. The record-by-record treatment is in the research companion, <a href="https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g31-walter-de-gournay-fact-sheet.research.md"><code>research/people/g31-walter-de-gournay-fact-sheet.research.md</code></a>. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>richardson-sgm-soc-genealogy-medieval-2002</code>. <a class="citation-back" href="#ref-8">↩</a></li>
```

**2.13 — New citations n9–n11 (insert before the closing `</ol>`; order-independent of 3.12 — the anchor is the unchanged tail of note n8).**

str_replace old_string:
```
 <a class="citation-back" href="#ref-8">↩</a></li>
</ol>
```
new_string:
```
 <a class="citation-back" href="#ref-8">↩</a></li>
  <li id="n9">Carta of Manasser de Danmartin (Suffolk, 1166): "Et in tempore Gwerrae de illo feodo dedi Waltero de Gornaco j quartum militis. Et nunc illam partem tenet Willelmus, filius suus, in auxilium mihi illud servitium faciendo." <em>The Red Book of the Exchequer</em>, ed. Hubert Hall, Rolls Series 99, vol. 1 (1896), pp. 409–410; <em>Liber Niger Scaccarii</em>, ed. Thomas Hearne (1774), vol. 1, p. 298, printed in Daniel Gurney, <em>Record</em>, Part II (1848), p. 288. Source IDs: <code>redbook-exchequer-hall-v1</code>, <code>liber-niger</code>, <code>dg-rec-pt2</code>. <a class="citation-back" href="#ref-9">↩</a></li>
  <li id="n10">Odo de Dammartin's gift at Gatton, Surrey, in the 1121 confirmation of Lewes Priory's possessions: William Farrer, <em>Honors and Knights' Fees</em>, vol. 3 (1925), p. 313. William de Dammartin holding eleven and a half knights' fees of Earl Warenne in Surrey, 1166: <em>Red Book of the Exchequer</em>, vol. 1 (earl Warenne's carta). The Dammartin descent (Odo, enfeoffed of Mendlesham by Henry I; Manasser d. 1178/9): Lewis C. Loyd and Doris M. Stenton, eds., <em>Sir Christopher Hatton's Book of Seals</em> (1950), notes to Nos. 332 and 409. Source IDs: <code>farrer-honors-knights-fees-v3-gurnay-extracts</code>, <code>redbook-exchequer-hall-v1</code>, <code>hatton-book-of-seals-1958</code>. <a class="citation-back" href="#ref-10">↩</a></li>
  <li id="n11">The Talbot marriage: Daniel Gurney, <em>Record</em>, Part I (1848), pp. 69–70. The Kent honour and the Stephen-era half-fee: carta of Walter de Meduana (Kent, 1166) — "De novo feffamento in tempore Regis Stephani: Willelmus de Gornaco tenet de dominio meo dimidium militem unde nullum servitium habeo" — <em>Red Book of the Exchequer</em>, vol. 1, pp. 195–196, quoted with the Talbot identification in Daniel Gurney, <em>Record</em>, Part II, p. 296 note ("William de Gournay had probably been enfeoffed of this by the Talbots, his relations"). Earl Hamelin's grant of Rose of Harpley to Matthew de Gournay, with the fine of 17 October 1184: C. T. Clay, ed., <em>Early Yorkshire Charters</em>, vol. 8 (1949), pp. 38–39 and 95; Daniel Gurney, <em>Record</em>, Part I, p. 278; Francis Blomefield, <em>History of Norfolk</em>, vol. 8 (Harpley), pp. 452–459. Source IDs: <code>redbook-exchequer-hall-v1</code>, <code>dg-rec-pt2</code>, <code>eyc8-warenne-clay-1949</code>, <code>blomefield-norfolk</code>. <a class="citation-back" href="#ref-11">↩</a></li>
</ol>
```

**2.14 — Children table dates for William.**

str_replace old_string:
```
      <td>William de Gournay I</td>
      <td>fl. c. 1150–1180</td>
```
new_string:
```
      <td>William de Gournay I</td>
      <td>c. 1120 – after 1167</td>
```

**2.15 — Timeline table.**

str_replace old_string:
```
      <tr><th>Year</th><th>Event</th></tr>
      <tr><td>c. 1108</td><td>Born — youngest son of Gerard de Gournay and Edith de Warenne.</td></tr>
      <tr><td>1135–1154</td><td>Active during "The Anarchy" — Stephen's civil war. Holds lands in Suffolk (Liber Niger Scaccarii).</td></tr>
      <tr><td>c. 1150</td><td>Son William I (G30) born.</td></tr>
      <tr><td>c. 1150–1165</td><td>Death. No record.</td></tr>
```
new_string:
```
      <tr><th>Year</th><th>Event</th></tr>
      <tr><td>c. 1090–1104</td><td>Born — youngest son of Gerard de Gournay and Edith (Ediva) de Warenne.</td></tr>
      <tr><td>1104</td><td>His father Gerard dies on pilgrimage; a portion of the Norman fief of Bray appears to have been severed for Walter.</td></tr>
      <tr><td>c. 1120</td><td>Son William I (G30) born.</td></tr>
      <tr><td>1135–1154</td><td>"The Anarchy" — Stephen's civil war. Enfeoffed by Manasser de Dampmartin of a quarter knight's fee in Suffolk "in the time of the war."</td></tr>
      <tr><td>1150</td><td>Witnesses a charter to Missenden Abbey for Manasser and his wife Galiena.</td></tr>
      <tr><td>by 1166</td><td>Dead — his son William holds the Suffolk quarter-fee in the barons' returns of 1166.</td></tr>
```

**End of Item 2 (2.1–2.15; 2.16 follows).**

**2.16 — Anarchy narrative paragraph gains its citation.**

Target file: `fact-sheets/g31-walter-de-gournay-fact-sheet.md`.

str_replace old_string:
```
Walter lived his adult years during "<a href="https://en.wikipedia.org/wiki/The_Anarchy">The Anarchy</a>," Stephen's reign (1135–1154), when the breakdown of royal authority left many English lords navigating a dangerous landscape of shifting loyalties and local violence. He navigated it quietly — there is no record of Walter in any political or military event, which was probably the wisest course for a minor Norfolk landlord.
```
new_string:
```
Walter lived his adult years during "<a href="https://en.wikipedia.org/wiki/The_Anarchy">The Anarchy</a>," Stephen's reign (1135–1154), when the breakdown of royal authority left many English lords navigating a dangerous landscape of shifting loyalties and local violence. His one grant of land came "in the time of the war" itself. He navigated it quietly — there is no record of Walter in any political or military event, which was probably the wisest course for a minor East Anglian landholder. <sup class="fn"><a href="#n6" id="ref-6c">6</a></sup><sup>, </sup><sup class="fn"><a href="#n9" id="ref-9c">9</a></sup>
```

---

## Item 3 — data/ancestors.json G31 corrections (promote)

Target file: `data/ancestors.json`. Three str_replace operations matching the fact-sheet corrections. After applying, run `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write` (the dates field feeds `data/indexes/ancestor-ids.csv`).

**3.1 — dates field on the G31 record (the bare dates string occurs twice in the file; the name line disambiguates).**

str_replace old_string:
```
    "name": "Walter de Gournay",
    "dates": "fl. c. 1108–1154",
```
new_string:
```
    "name": "Walter de Gournay",
    "dates": "b. c. 1090/1104 – d. by 1166",
```

**3.2 — dates on Walter's row in the G32 record's children array (deeper indent).**

str_replace old_string:
```
        "name": "Walter de Gournay",
        "dates": "fl. c. 1108–1154",
```
new_string:
```
        "name": "Walter de Gournay",
        "dates": "b. c. 1090/1104 – d. by 1166",
```

**3.3 — notables field: the 1166 return quoted; the Les Olim sentence corrected.**

str_replace old_string:
```
Documented in the *Liber Niger Scaccarii* — the Black Book of the Exchequer, c. 1166 — as holding a quarter knight's fee in Suffolk under Manasser de Dampmartin. Three independent evidentiary chains converge to confirm his Gournay blood-descent: (1) the *Liber Niger* entry; (2) his son William I's parage tenure of Montigny-sur-Andelle in Normandy (parage tenure being available only to blood relatives of the senior lord); (3) a *Les Olim* entry — official records of the French royal court — formally recognising the Swathings Gurneys as legitimate descendants of the Lords of Gournay.
```
new_string:
```
Named in the *Liber Niger Scaccarii* — the Black Book of the Exchequer, 1166 — where his lord Manasser de Dampmartin reported: 'in the time of the war I gave Walter de Gournay a quarter of a knight's fee — and now William his son holds that part.' His son William I held Montigny-sur-Andelle, in the family's Norman home country of Bray, directly of the crown in the manner of parage (a partition among sons, not a grant to outsiders), with a charter confirmed by Henry II whose recital survives in the *Les Olim*, the registers of the French royal court (1259); the family's Norfolk manors were held under the senior Gournay lords.
```

**End of Item 3.**

---

## Item 4 — places: the Suffolk holding identified; Montigny recital (promote)

The 1166 return identifies Walter's Suffolk holding as a quarter-fee out of the Dammartin fee of Mendlesham (with Cotton and Wickham Skeith, Hartismere hundred). The quarter-fee's own vill is not named, so no new canonical place is created — the county umbrella stays, now anchored to the Mendlesham fee (same posture as the Bois Gautier "candidate, not canonical" note on the Montigny record). Addington, Kent, is not an ancestor landholding (it belonged to the related Kent Gurnay family) and gets no place record; it is treated on the G31 companion. Harpley needs no change from this campaign.

**4.1 — data/places.json, Suffolk shortDescription (anchored by the placeId block; the bare shortDescription string is shared by other county records).**

Target file: `data/places.json`.

str_replace old_string:
```
    "placeId": "place-suffolk-england",
    "name": "Suffolk, England",
    "aliases": [
      "Suffolk"
    ],
    "shortDescription": "Regional holdings context",
```
new_string:
```
    "placeId": "place-suffolk-england",
    "name": "Suffolk, England",
    "aliases": [
      "Suffolk"
    ],
    "shortDescription": "Quarter-fee out of the Dammartin fee of Mendlesham",
```

**4.2 — data/places_detail.json, Suffolk longDescription.**

Target file: `data/places_detail.json`.

str_replace old_string:
```
    "longDescription": "County-level record for Suffolk holdings held under Manasser de Dampmartin.",
```
new_string:
```
    "longDescription": "County-level record for the early Suffolk holding: Walter de Gournay's quarter knight's fee, granted 1135-1154 out of Manasser de Dampmartin's fee of Mendlesham (with Cotton and Wickham Skeith, Hartismere hundred) per the 1166 carta; the quarter-fee's own vill is not named, so the county umbrella stands in for it. Also covers the later-medieval Suffolk interests (the 1408 manor; Depden via the Wauncy inheritance).",
```

**4.3 — data/places_detail.json, Montigny longDescription (the recital fact).**

Target file: `data/places_detail.json`.

str_replace old_string:
```
    "longDescription": "Montigny-sur-Andelle parage tenure, cited by Daniel Gurney and Hannay as strong legal proof that William de Gournay I and the junior Norfolk line were of the blood of the Barons of Gournay.",
```
new_string:
```
    "longDescription": "Montigny-sur-Andelle parage tenure, cited by Daniel Gurney and Hannay as strong legal proof that William de Gournay I and the junior Norfolk line were of the blood of the Barons of Gournay. The 1259 petition of Eustace de Montigny in the Registres Olim (denied on its own request) recites that a William de Gournay held Montigny directly of the king, with a charter confirmed by Henry II.",
```

**4.4 — data/places_detail.json, Montigny review note (the Olim entry is now held via DG's print).**

Target file: `data/places_detail.json`.

str_replace old_string:
```
      "Locate Beugnot's Registres Olim entry and verify modern Montigny-sur-Andelle identity before coordinate upgrade.",
```
new_string:
```
      "Olim entry held via DG-II p. 293 print (Beugnot vol. 1 p. 85; petition denied, recital stands); verify on Gallica and confirm modern Montigny-sur-Andelle identity before coordinate upgrade.",
```

**4.5 — research/places/suffolk.md: the fee identified.**

Target file: `research/places/suffolk.md`.

str_replace old_string:
```
At present, however, the county file is standing in for more specific manors that have not yet been separated. Until the Liber Niger entry is pulled directly and the named Suffolk places identified, Suffolk should remain a **county-level placeholder for early holdings**, not a claim that the family held the whole county in any broad sense.
```
new_string:
```
The Liber Niger entry has now been pulled directly: Manasser de Dampmartin's 1166 return states that "in the time of the war" (1135–1154) he gave Walter a quarter of a knight's fee out of his own fee — the Dammartin fee of **Mendlesham**, with Cotton and Wickham Skeith nearby, in Hartismere hundred. [Red Book, ed. Hall (1896), vol. 1, pp. 409–410; DG-II p. 289; Hatton Book of Seals No. 350] The quarter-fee's own vill is not named in the return, so Suffolk remains a **county-level umbrella** for this holding — now anchored to the Mendlesham fee rather than to the county at large. A separate Mendlesham place file becomes worthwhile only if a later record localizes the quarter-fee.
```

**4.6 — research/places/suffolk.md: the open item resolved.**

Target file: `research/places/suffolk.md`.

str_replace old_string:
```
- [ ] Pull the **Liber Niger Scaccarii** entry and identify Walter's specific Suffolk holdings under Manasser de Dampmartin.
```
new_string:
```
- [x] Pull the **Liber Niger Scaccarii** entry and identify Walter's specific Suffolk holdings under Manasser de Dampmartin. **Done 2026-07** — quarter-fee out of the Dammartin fee of Mendlesham (Hartismere hundred); vill not named. See the Walter section above.
```

**End of Item 4.**

---

## Phase-2 closing steps

1. Run `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write` (the `data/ancestors.json` dates change feeds `data/indexes/ancestor-ids.csv`).
2. Do not manually mirror the fact sheet into `site/` (the build handles it); the generated place-registry block in `research/places/suffolk.md` refreshes via the site sync — do not hand-edit it.
3. The former case file was renamed to `research/case-files/walter-de-gournay-as-son-of-gerard-to-be-deleted.md` on 2026-07-14, pending the user's review and deletion; no Phase-2 action on it.
4. Prepend the `**Done:** YYYY-MM-DD HH:MM PT` stamp and move this patchset to `sources/intake/done/`.
