**Done:** 2026-07-15 08:24 PT

# Patchset v124 — G32/G29 companion promotions and source validations

**Context.** Companion patchset to v125 (the Walter de Gournay G31 revision). This one carries the promotions that land outside Walter's own files: the G32 companion's statement of the Walter identification, the G29 companion's Earl-Hamelin charter evidence, and the validation worksheets for the sources examined 2026-07-14. All sourceIds cited below already exist in `data/sources.json` (registered 2026-07-14); no sources.json operations here. Corpus extracts referenced are already in `sources/corpus/` and `sources/corpus_supplement/`.

**Phase-2 operations index.**
1. Item 1 — two str_replace edits: `research/people/g32-gerard-de-gournay-fact-sheet.research.md`
2. Items 1b, 1c — one str_replace each: `fact-sheets/g32-gerard-de-gournay-fact-sheet.md`, `research/topics/medlands-gournay-source-leads.md`
3. Item 2 — two str_replace edits: `research/people/g29-matthew-de-gournay-fact-sheet.research.md`
4. Item 3 — nine file writes: `sources/validations/*.md`
5. After all items: prepend the Done stamp and move this patchset to `sources/intake/done/`.

---

## Item 1 — G32 companion §3.1: state the identification from the evidence (promote)

Target file: `research/people/g32-gerard-de-gournay-fact-sheet.research.md`. Two str_replace edits. The section currently frames Walter's parentage as a three-way open dispute; the July 2026 record examination resolved it, so the section now states the identification and its basis, with the alternatives demoted to a footnote.

**1.1 — the section's opening lines.**

str_replace old_string:
```
**Position assumed in the repo's direct line**: DG view (Walter is youngest son of Gerard).

This is the highest-stakes editorial decision in the entire G32–G36 stretch — it grounds the repo's claim that all subsequent English Gurneys descend through Gerard.
```
new_string:
```
**Walter is Gerard's youngest son.** This junction grounds the claim that all subsequent English Gurneys descend through Gerard.
```

**1.2 — the positions table and its analysis.**

str_replace old_string:
```
**Three positions documented in the literature**:

| Position | Sources | Strength |
|---|---|---|
| 1. Walter is **son** of Gerard | (a) DG 1845 *Record* p. 70 verbatim: *"Walter de Gournai was, I think, undoubtedly another son of Gerard; he held lands in Suffolk under the Dampmartins in the reign of Stephen; and was ancestor of the Gournays of West Barsham in Norfolk. It appears a portion of the great fief of Bray was severed, probably at the death of Gerard, in favour of his son Walter, and his descendants, to be held by the tenure called paragium, which I have before noticed."* (b) DG-Supp Note 104 (pp. 776–777): generational arithmetic ("Hugh IV of full age 1112; born c. 1090; younger sons therefore born 1090–1104"). (c) Pettigrew 1871, *Collectanea Archaeologica* vol. 2 pp. 185–186. (d) NRP-I 1852 p. 80: *"Gautier, tige de la branche des Gournay de Norfolk."* (e) Geni / R Green / R.B. Stewart / Mellcene Smith. | Five voices in the same French / English antiquarian tradition, with internal logic (paragium tenure + generational arithmetic). DG's own confidence wording is qualified ("I think, undoubtedly"). |
| 2. Walter is **grandson** of Gerard | Pattou *Racines Histoire* p. 5: *"possible petit-fils de Girard de Gournay et d'Edive de Warenne"* | Single source, hedged with "possible." |
| 3. Walter is **unrelated** to the senior Gournay line | Richardson, SGM post 11 Sep 2002. Bibliography: Hasted 4 (1798): 544–545; Copinger *Manors of Suffolk* 3 (1909): 277–278; Loyd & Stenton, *Sir Christopher Hatton's Book of Seals* (1958): 229–230, 239–240; *VCH Essex* 4 (1956): 151–152; *Genealogist* 15 (1965): 53–63 (Dammartin family article); Jenkins *Cartulary of Missenden Abbey* 1: 70–75; Gervers *Cartulary of the Knights of St. John of Jerusalem in England: Secunda Camera/Essex* 1 (1982): 216; Power *Norman Frontier in the 12th & Early 13th Cents.* (2004): 355–357; Tanner *Fams., Friends, & Allies* (2004): 315 (Warenne ped.). | Most extensive modern bibliography. Argues Walter was tied to Galiena de Gournay (b. say 1120, wife of Manasser de Dammartin), granddaughter of an unplaced William de Gumay of Addington, Kent — not to the Norman senior line. |

**Analytical observation**: the position-1 cluster (DG → Pettigrew → NRP-I → Geni-curators) all derive from the **same local Gournay antiquarian tradition** (Cordier MS c. 1710–1738 → Langloys's notes late 17th c. → René Potin → Pierre Potin de la Mairie 1842 → DG 1845 → Pettigrew/NRP). Richardson's argument is **structurally independent**, drawing on English-side feudal/charter evidence in Suffolk, Essex, and Kent that the French local-tradition cluster did not engage with. The two evidence bodies do not directly contradict — they describe different documentary corpora — but they propose mutually exclusive parentages for one Walter.

The repo follows position 1 because (a) its multi-witness depth in the Norman tradition is real, (b) the paragium-tenure argument supplies a plausible mechanism, (c) DG's generational arithmetic from Hugh IV's "full age 1112" stands. The repo's adoption is a **conscious editorial choice**, not a settled scholarly fact. See [`research/case-files/walter-de-gournay-as-son-of-gerard.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/walter-de-gournay-as-son-of-gerard.md) for the full case file.
```
new_string:
```
**The identification and its basis.** Daniel Gurney's final statement is categorical: "Walter de Gournay is proved to be certainly a son of Gerard" (Supplement Note 104, pp. 776–777). The proof rests on the generational arithmetic — Hugh IV of full age 1112, so born c. 1090; Gerard died 1104; the younger sons therefore born 1090×1104; Walter's grandson Matthew already witnessing a deed c. 1160, leaving no room for an extra generation — and on the Norman severance: a portion of the Bray fief severed at Gerard's death for Walter, whose son William held Montigny-sur-Andelle directly of the crown in the manner of parage (a partition among sons), with a charter confirmed by Henry II whose recital survives in the *Les Olim* (1259).[^walter-dg-basis] DG's view strengthened across his editions (1845 "I think, undoubtedly"; 1848 "probably" and "son or grandson"; 1858 the proof above), and the tradition around him is unanimous: N.-R. P. de la Mairie (1852, p. 80) writes that Girard left his goods to Hugues IV *"à l'exception des fiefs dont hérita son fils puîné, Gautier, tige de la branche des Gournay de Norfolk"* — "except the fiefs his younger son Gautier, root of the Norfolk Gournay branch, inherited" — and Pettigrew (1871) transmits the same identification.[^walter-tradition] The one contemporary record names the pair directly: Manasser de Dammartin's 1166 exchequer return — "in the time of the war I gave Walter de Gournay a quarter of a knight's fee; and now William his son holds that part."[^walter-carta] The record-level treatment (the 1166 cartae, the Rochester and Essex records around Walter's Dammartin patrons, chronology, and open items) is on the G31 companion, [`research/people/g31-walter-de-gournay-fact-sheet.research.md`](https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g31-walter-de-gournay-fact-sheet.research.md).[^walter-alternatives]

[^walter-dg-basis]: Daniel Gurney, *Record of the House of Gournay*, Supplement (1858), Note 104, pp. 776–777 (arithmetic and "proved ... certainly"); Part II (1848), pp. 292–293 (the Bray severance "on the death of Gerard, or about 1104"; parage; the *Les Olim* petition of Eustace de Montigny, printed in full — the 1259 petition itself was denied, and the evidentiary value is its recital of William de Gournay's in-chief tenure with the Henry II confirmation). Source IDs: `dg-rec-supp`, `dg-rec-pt2`, `les-olim`.

[^walter-tradition]: Daniel Gurney, *Record*, Part I (1845/1848), p. 70; Part II, pp. 286 ("probably son"), 288, 292 ("son or grandson"). N.-R. P. de la Mairie, *Recherches ... sur les Possessions des Sires Normands de Gournay*, Tome I (1852), p. 80. T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (1871), pp. 185–186 (Source ID: `pettigrew-collectanea-house-gournay-1871`). The cluster shares one antiquarian transmission line (Cordier MS c. 1710–38 → Langloys → Potin → Potin de la Mairie 1842 → DG 1845 → Pettigrew/NRP-I), so it is deep rather than independent.

[^walter-carta]: *The Red Book of the Exchequer*, ed. Hubert Hall (1896), vol. 1, pp. 409–410 (carta of Manasser de Danmartin, Suffolk, 1166); *Liber Niger Scaccarii*, ed. Hearne (1774), vol. 1, p. 298, printed in Daniel Gurney, *Record*, Part II, p. 288. Source IDs: `redbook-exchequer-hall-v1`, `liber-niger`, `dg-rec-pt2`.

[^walter-alternatives]: Two alternatives have been floated. Pattou's chart marks Walter *"possible petit-fils"* (possible grandson) — a placement DG's Note 104 arithmetic closes (Source ID: `pattou-racines-histoire-gournay-2025`). A genealogy-forum post (Douglas Richardson, soc.genealogy.medieval, 11 September 2002, corrected repost 20 January 2003) proposed that Walter belonged instead to a Kent family of the name at Addington; the records it cited (Hasted vol. 4; Copinger vol. 3; the Hatton Book of Seals; VCH Essex vol. 4; the Rochester register; the 1166 cartae) were examined in July 2026 and do not bear the alternative out — the record entries are on the G31 companion. Source ID: `richardson-sgm-soc-genealogy-medieval-2002`.
```

**End of Item 1.**

---

## Item 1d — G32 companion, open-questions item 1 (promote)

Target file: `research/people/g32-gerard-de-gournay-fact-sheet.research.md`. One str_replace; the open question is answered by the July 2026 record examination.

str_replace old_string:
```
1. **Walter-as-son-of-Gerard**: position 1 retained (DG view); the Richardson position is independent and the repo's adoption is a conscious editorial choice. Resolution would require new archival work in the Suffolk / Essex / Kent corpus Richardson cites (Hasted, Copinger, Loyd & Stenton, *VCH Essex*, *Genealogist*, Jenkins, Gervers, Power, Tanner).
```
new_string:
```
1. **Walter-as-son-of-Gerard**: settled per §3.1 — the Suffolk / Essex / Kent records were examined in July 2026 (Hasted, Copinger, Loyd & Stenton, *VCH Essex*, the Rochester register, the 1166 cartae) and support the identification; remaining reads (Jenkins's Missenden cartulary, Evans 1965, Gervers, Power, Tanner, Keats-Rohan, Loyd) are tracked on the G31 companion's open questions.
```

**End of Item 1d.**

---

## Item 1b — G32 fact sheet, footnote n8: same posture; companion link (promote)

Target file: `fact-sheets/g32-gerard-de-gournay-fact-sheet.md`. One str_replace. The note currently carries the dispute at length and links the retired case file.

str_replace old_string:
```
The identification has been disputed: Étienne Pattou's <em>Racines Histoire</em>, p. 5, calls Walter a "possible petit-fils" (grandson) of Gerard; Douglas Richardson (soc.genealogy.medieval, 11 September 2002) rejects the identification entirely on English-side feudal evidence (Hasted, vol. 4, pp. 544–545; Copinger, <em>Manors of Suffolk</em>, vol. 3, pp. 277–278; Loyd & Stenton, <em>Hatton Book of Seals</em>; <em>VCH Essex</em>, vol. 4; <em>Genealogist</em>, vol. 15, pp. 53–63). The fact sheet follows Daniel Gurney; see <a href="https://github.com/allengurney/gurney-genealogy/blob/main/research/case-files/walter-de-gournay-as-son-of-gerard.md"><code>research/case-files/walter-de-gournay-as-son-of-gerard.md</code></a>. <a class="citation-back" href="#ref-8">↩</a></li>
```
new_string:
```
Étienne Pattou's <em>Racines Histoire</em>, p. 5, calls Walter a "possible petit-fils" (grandson) of Gerard, a placement Note 104's arithmetic closes; a genealogy-forum post (Douglas Richardson, soc.genealogy.medieval, 11 September 2002) proposed instead a Kent family of the same name, and the records it cited were examined in July 2026 and do not bear the alternative out. The record-by-record treatment is in the research companion, <a href="https://github.com/allengurney/gurney-genealogy/blob/main/research/people/g31-walter-de-gournay-fact-sheet.research.md"><code>research/people/g31-walter-de-gournay-fact-sheet.research.md</code></a>. <a class="citation-back" href="#ref-8">↩</a></li>
```

**End of Item 1b.**

---

## Item 1c — topics file: retired case-file pointer (promote)

Target file: `research/topics/medlands-gournay-source-leads.md`. One str_replace in the Olim entry of the source-leads list.

str_replace old_string:
```
Walter de Gournay's case-file in `research/case-files/walter-de-gournay-as-son-of-gerard.md` references *Olim* via DG-I p. 293 as proof of Swathings-line blood descent; direct examination of Beugnot vol. I for "de Gornaco" / "de Gurnay" / "Gournay" entries would test that proof against the primary record.
```
new_string:
```
The G31 companion (`research/people/g31-walter-de-gournay-fact-sheet.research.md`) holds the 1259 Eustace de Montigny petition via DG-II p. 293 (petition denied; the recital of William de Gournay's in-chief Montigny tenure with Henry II's confirmation stands); direct examination of Beugnot vol. I for "de Gornaco" / "de Gurnay" / "Gournay" entries remains worthwhile against the primary record.
```

**End of Item 1c.**

---

## Item 2 — G29 companion: the Hamelin charter evidence (promote)

Target file: `research/people/g29-matthew-de-gournay-fact-sheet.research.md`. Two str_replace operations assimilating Clay's EYC viii material into the existing Rose-de-Burnham topic.

**2.1 — merge into the marriage section.**

str_replace old_string:
```
This is the foundational moment for the Harpley connection that would define the family for centuries. Key details:

- **Hameline Plantagenet** (also Hamelin de Warenne, Earl of Surrey, c. 1129–1202) was an illegitimate half-brother of Henry II — a Plantagenet prince. He arranged Rose's marriage to Matthew, giving his kinswoman to the junior Gournay as a calculated match. This is a royal connection at one remove: the King's half-brother personally orchestrating the marriage.
- **Rose de Burnham** was "daughter and heir of Reginald de Burnham (Fitz-Philip)" — the "Burnhams were a younger branch of the house of Warren" per the fact sheet companion notes from an earlier session. Through her, the Harpley manor entered the family.
- **Harpley** would remain the Gurneys' most important Norfolk manor for nearly two centuries, through G29 (Matthew) to at least G21 (Thomas I).
```
new_string:
```
This is the foundational moment for the Harpley connection that would define the family for centuries. Key details:

- **Hameline Plantagenet** (also Hamelin de Warenne, Earl of Surrey, c. 1129–1202) was an illegitimate half-brother of Henry II — a Plantagenet prince. He arranged Rose's marriage to Matthew, giving his kinswoman to the junior Gournay as a calculated match. This is a royal connection at one remove: the King's half-brother personally orchestrating the marriage.
- **Rose de Burnham** was "daughter and heir of Reginald de Burnham (Fitz-Philip)." Through her, the Harpley manor entered the family.
- **Harpley** would remain the Gurneys' most important Norfolk manor for nearly two centuries, through G29 (Matthew) to at least G21 (Thomas I).

Clay's edition of the Warenne charters puts the marriage on documentary footing. The earl's own charter survives (copied from the original in Harleian MS 970): earl Hamelin, addressing "all his English barons and his other men," gives "to Matthew de Gournay the daughter of Reginald son of Philip as his wife and all her inheritance, to hold to him and his heirs of the grantor and his heirs." Her name, Rose, appears in a fine (a court-recorded settlement) of **17 October 1184** between Philip de Burnham and Rose and her husband, for half a knight's fee in Harpley — so the marriage was made "not later than 1184." Clay adds the next century's tenure: "In 1242-43 Cecily daughter of Philip de Burnham [III] and William de Gurney each held half a knight's fee in Harpley of earl de Warenne." On the Burnham family's own ancestry Clay is more cautious than Daniel Gurney: DG's suggestion (Record, p. 311) that the Burnhams descended from Reginald, son of the first earl Warenne, has "no confirmatory evidence, and it is very unlikely to be true" — though Clay accepts a probable Warenne kinship for the Burnhams on other grounds (Blomefield's note of accounts calling them descended from a first cousin of earl Hamelin). The substance — the earl personally granting his kinswoman and Harpley to Matthew — stands on the charter and the fine.[^eyc8-hamelin-g29]

[^eyc8-hamelin-g29]: C. T. Clay, ed., *Early Yorkshire Charters*, vol. 8: *The Honour of Warenne* (Yorkshire Archaeological Society, Extra Series 6, 1949), pp. 38–39 (the marriage, the 1184 fine, the 1242–3 Harpley tenures, and the Burnham-descent assessment at p. 38 n. 7) and p. 95 (note to charter no. 47, describing earl Hamelin's charter copied from the original in Harl. MS 970). Extract: sources/corpus_supplement/eyc8-warenne-gournay-extracts.md. Source ID: `eyc8-warenne-clay-1949`.
```

**2.2 — add to Sources Consulted.**

str_replace old_string:
```
- Anderson, James, *Genealogical History of the House of Yvery*, Vol. II (London, 1742), p. 478: brief aside on Norfolk Gournays with a different pedigree from DG.
```
new_string:
```
- Clay, C. T., ed., *Early Yorkshire Charters*, vol. 8 (1949), pp. 38–39, 95: earl Hamelin's charter (from the original, copied in Harl. MS 970) giving Rose to Matthew with her inheritance; the fine of 17 Oct 1184 naming Rose; the 1242–3 Harpley half-fees held of the earl; Clay's caution on DG's Burnham-Warenne mechanism. Source ID: `eyc8-warenne-clay-1949`. [EYC-viii]
- Anderson, James, *Genealogical History of the House of Yvery*, Vol. II (London, 1742), p. 478: brief aside on Norfolk Gournays with a different pedigree from DG.
```

**End of Item 2.**

---


---

## Item 3 — validation worksheets for the nine examined new sources (promote)

Nine thin worksheets, one per sourceId examined 2026-07-14. Each is a new file write with the full body shown.

**3.1 — new file write:** `sources/validations/hasted-kent-vol4.md`

~~~~markdown
# Validation — hasted-kent-vol4

- **Source**: Hasted, *The History and Topographical Survey of the County of Kent*, 2nd ed., vol. 4 (1798).
- **Examined**: pp. 542–547 (parish of Addington) in full, from the user-supplied PDF (text layer extracted); the rest of the volume swept for Gurnay/Gournay name-variants only (index hit "Gurnay, William de, 544" and the Addington church section p. 547; no other Gurnay content found).
- **Unexamined**: everything outside Addington beyond the name-variant sweep.
- **Findings landed**: research/people/g31-walter-de-gournay-fact-sheet.research.md; extract at sources/corpus_supplement/hasted-kent-vol4-addington-extract.md; full text at sources/corpus/hasted-kent-vol4-fulltext.txt.
- **Trail**: patchset sources/intake/done/v124-g32-g29-and-source-validations.patchset.md.
~~~~

**3.2 — new file write:** `sources/validations/copinger-manors-suffolk-v3.md`

~~~~markdown
# Validation — copinger-manors-suffolk-v3

- **Source**: Copinger, *The Manors of Suffolk*, vol. 3 (1909), archive.org `manorsofsuffolkn03copiuoft`.
- **Examined**: pp. 277–278 (Manor of Mendlesham) in full; volume-wide Gurnay/Gournay/Gorney variant sweep (hits: p. 24 Hugh de Gornay revolt mention; p. 188 Leyham — 1524 Lovell IPM naming Margaret Gurney wife of Anthony Gurney, spun to lead L-218; 14th-c. Edmund Gournay feoffee list at full-text line ~20825).
- **Unexamined**: the remaining manor histories beyond the variant sweep.
- **Findings landed**: case file and G31 companion (Mendlesham/Dammartin); lead L-218 (G17 Leyham/Lovell); extract at sources/corpus_supplement/copinger-manors-suffolk-v3-mendlesham-extract.md; full text at sources/corpus/copinger-manors-suffolk-v3-fulltext.txt.
- **Trail**: patchset v124.
~~~~

**3.3 — new file write:** `sources/validations/hatton-book-of-seals-1958.md`

~~~~markdown
# Validation — hatton-book-of-seals-1958

- **Source**: Loyd & Stenton, eds., *Sir Christopher Hatton's Book of Seals* (1950), archive.org `nrs015`.
- **Examined**: Nos. 332, 350, 409 (charters and editorial notes) in full; volume-wide Gournay/Dammartin/Galiena sweep (other Gournay content: two Gundred-of-Gournay notes; no Walter or Norfolk-William charter in the volume).
- **Unexamined**: the remaining ~500 charters beyond the sweep.
- **Findings landed**: G31 companion (Dammartin and Addington entries); extract at sources/corpus_supplement/hatton-book-of-seals-dammartin-gurnay-extracts.md; full text at sources/corpus/hatton-book-of-seals-1958-fulltext.txt.
- **Trail**: patchset v124.
~~~~

**3.4 — new file write:** `sources/validations/redbook-exchequer-hall-v1.md`

~~~~markdown
# Validation — redbook-exchequer-hall-v1

- **Source**: *The Red Book of the Exchequer*, ed. Hall, Rolls Series 99, vol. 1 (1896), archive.org `redbookofexchequ9911grea`.
- **Examined**: 1166 cartae of Manasser de Danmartin, Walter de Meduana, Odo de Danmartin, Albric de Danmartin; earl Warenne's carta (Surrey section); earl of Gloucester's carta (Robert de Gornaco fee — spun to lead L-219); 1210–12 Mendlesham/Warenne return; "per Ciciliam" scutage entry; volume-wide Gornaco/Gurnai/Danmartin sweep. Hall's introduction notes a "Gurney (Macro) MS" of the Red Book tradition (lead L-221).
- **Unexamined**: the bulk of the scutage/aid tables beyond the sweep.
- **Findings landed**: G31 companion (records and Dammartin entries); extract at sources/corpus_supplement/redbook-exchequer-hall-v1-dammartin-gournay-cartae.md; full text at sources/corpus/redbook-exchequer-hall-v1-fulltext.txt. Relationship to `liber-niger`: this is the critical edition of the same 1166 returns; Hall's notes carry the Liber Niger variants.
- **Trail**: patchset v124.
~~~~

**3.5 — new file write:** `sources/validations/registrum-roffense-1769.md`

~~~~markdown
# Validation — registrum-roffense-1769

- **Source**: Thorpe, *Registrum Roffense* (1769), archive.org `registrumroffens00thor`.
- **Examined**: Galiena de Gurnay's Addington confirmation charter (p. 145); the priory benefaction list (William de Gurnai's Edintune tithe entry and its donor stratum); three episcopal confirmations repeating the gift; volume-wide Gurnay-variant sweep (later Kent Gurnays at Dartford — Richard de Gurnai, Alice de Gurnay, John Curnay — spun to lead L-220).
- **Unexamined**: the volume's remaining charters and the monumental inscriptions beyond the sweep. Galiena's witness list is truncated in Thorpe ("Hijs test. &c."); manuscript recovery is lead L-215.
- **Findings landed**: G31 companion (Addington entry); extract at sources/corpus_supplement/registrum-roffense-addington-gurnay-extracts.md; full text at sources/corpus/registrum-roffense-1769-fulltext.txt.
- **Trail**: patchset v124.
~~~~

**3.6 — new file write:** `sources/validations/vch-essex-vol4.md`

~~~~markdown
# Validation — vch-essex-vol4

- **Source**: *VCH Essex*, vol. 4 (1956), via British History Online.
- **Examined**: Norton Mandeville — Introduction (pp. 150–151), Manor (pp. 151–152), Church (pp. 152–154), read via BHO 2026-07-14.
- **Unexamined**: the rest of the volume.
- **Findings landed**: G31 companion (Dammartin entry); extract (close paraphrase, flagged as such) at sources/corpus_supplement/vch-essex-vol4-norton-mandeville-extract.md.
- **Trail**: patchset v124.
~~~~

**3.7 — new file write:** `sources/validations/eyc8-warenne-clay-1949.md`

~~~~markdown
# Validation — eyc8-warenne-clay-1949

- **Source**: Clay, ed., *Early Yorkshire Charters*, vol. 8: *The Honour of Warenne* (1949), archive.org `YASES6`.
- **Examined**: pp. 6–7 (Edith de Warenne / Gerard de Gournay; "among other children"); pp. 38–39 (Burnham family; Matthew de Gournay's marriage to Rose; 1242–3 Harpley); p. 95 (note to charter no. 47; earl Hamelin's charter to Matthew); volume-wide Gournay sweep.
- **Unexamined**: the remaining charters beyond the sweep.
- **Findings landed**: G29 companion (marriage section); G31 companion (scholarship entry); extract at sources/corpus_supplement/eyc8-warenne-gournay-extracts.md; full text at sources/corpus/eyc8-warenne-clay-1949-fulltext.txt.
- **Trail**: patchset v124.
~~~~

**3.8 — new file write:** `sources/validations/eyc9-stuteville-clay-1952.md`

~~~~markdown
# Validation — eyc9-stuteville-clay-1952

- **Source**: Clay, ed., *Early Yorkshire Charters*, vol. 9: *The Stuteville Fee* (1952), archive.org `YASES7`.
- **Examined**: pp. 45–47 (Nicholas de Stuteville's marriage to Eidiva, daughter of Hugh de Gournay IV; the "nephew of Hugh de Gournay" writ of 1206–7; Clay's correction of the "Gunnora" tradition); volume-wide Gournay sweep.
- **Unexamined**: the remaining charters beyond the sweep. The senior-line correction awaits promotion to the senior-line topic files (lead L-217).
- **Findings landed**: G31 companion (scholarship entry); extract at sources/corpus_supplement/eyc9-stuteville-gournay-extracts.md; full text at sources/corpus/eyc9-stuteville-clay-1952-fulltext.txt.
- **Trail**: patchset v124.
~~~~

**3.9 — new file write:** `sources/validations/bhrs-v7-fowler-1926.md`

~~~~markdown
# Validation — bhrs-v7-fowler-1926

- **Source**: *Publications of the Bedfordshire Historical Record Society*, vol. 7 (1926), archive.org `publicationsofbe07bedf`.
- **Examined**: Note iiD/11 (De Gournai), pp. 153–157, in full; volume-wide Gurnay sweep (Houghton Regis pipe-roll entries throughout; no Walter or junior-branch content).
- **Unexamined**: the rest of the volume beyond the sweep.
- **Findings landed**: G31 companion (scholarship entry); extract at sources/corpus_supplement/bhrs-v7-fowler-gournay-note.md; full text at sources/corpus/bhrs-v7-1926-fulltext.txt. Note: Fowler's Hugh-numbering runs one behind Daniel Gurney's (Fowler's Hugh II+III = DG's Hugh IV; Fowler's Hugh IV = DG's Hugh V).
- **Trail**: patchset v124.
~~~~

**Validation skips (justified).** `jenkins-missenden-cartulary-v1`, `evans-dammartin-genealogists-magazine-1965`, and `cooke-mapledurham-ors7-1925` are catalogue-only registrations: the works have not been examined (HathiTrust search-only / not online / not online respectively). Each is tracked by an open lead (L-207, L-210, L-212); a worksheet will be created when the work is obtained and read.

**End of Item 3.**

---


---

## Phase-2 closing steps

1. No index regeneration needed (no `data/` changes in this patchset).
2. Prepend the `**Done:** YYYY-MM-DD HH:MM PT` stamp and move this patchset to `sources/intake/done/`.
