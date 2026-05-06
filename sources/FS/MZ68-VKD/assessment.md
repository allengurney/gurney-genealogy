# G33 — FamilySearch Intake Assessment (Hugh de Gournay III, MZ68-VKD)

**Source artifact**: `sources/FS/20260506FamilyMZ68-VKD.pdf` (22 pp., printed 6 May 2026)
**Companion artifacts**: `sources/FS/MZ68-VKD/racineshistoire_free_fr_LGN_PDF_Gournay.pdf` (Etienne Pattou, *Seigneurs de Gournay (-en-Bray) & Gurney*, 18 pp., last update 11 Aug 2025)
**Subject FS PID**: MZ68-VKD
**Repo target**: G33 (`research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`, `fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`)
**Assessment date**: 2026-05-06
**Disposition**: Phase-0 POC (initial pass) plus Phase-0 supplement after companion ingestion. Precursor to a Phase-1 intake patchset.
**Skill**: `.claude/skills/familysearch-export-review/SKILL.md`

---

## 0. Two-pass structure

This file preserves both the original POC pass (Pass A, before the Pattou companion was available) and the supplement after Pattou was ingested (Pass B). The Pattou companion materially changed several conclusions — those changes are noted explicitly in Pass B and a combined disposition is given at the end.

The two-pass structure is preserved deliberately as the POC reference for how a single-source pass differs from a multi-source pass; the operational input to a Phase-1 patchset is the Combined Disposition in §6.

---

## 1. Source-format anatomy

The export bundles three layers in one PDF, with very different trust profiles per the Phase-0 skill discipline:

| Layer | Pages | Character | Trust |
|---|---|---|---|
| Structured Family Group Record table | pp. 1–3 | Husband / Wife / Children fields scraped from FS Family Tree | Low |
| Sources sections per person | pp. 4–20 | Aggregated source titles, URLs, and full-text notes | Mixed — embedded MedLands transcripts are gold; user-pasted notes are noise |
| Trailing Notes sections | pp. 8, 10–11, 16, 18–19 | Free-form contributor notes (Sorley, Brown book, Kraentzler, AGBI, etc.) | Very low |

**Dominant scholarly tradition embedded**: Foundation for Medieval Genealogy / MedLands (Cawley) for the Latin charter substrate; Daniel Gurney 1848 (HathiTrust mirror) for the English-language synthesis; Racines Histoire / Pattou (companion PDF) for the French chart-genealogy with critical apparatus. Reference numbers `[875]`–`[907]` on pp. 6–7 are MedLands footnotes preserved verbatim.

**Layer peculiarities for this export**:
- Sources section duplicates the FMG MedLands transcript twice (pp. 4–7 and pp. 8–9) — once via the FMG canonical URL, once via a `web.archive.org/web/20240826200046/...` snapshot URL. The Wayback URL is the more stable retrieval target.
- The FS structured field on p. 1 lists Hugh III's father as `Hugues de Gournay II (LVSH-KBM)` (correct) and his mother as `Berthilde de Gerberoy (PM9Z-R79)` — the Berthilde attribution is the export's single most consequential structured-field claim and is unsupported by any of the embedded scholarly transcripts in this PDF (see §3 and §5).

---

## 2. Pass A — original POC analysis (before Pattou companion)

### 2.1 Concordant facts (FS confirms repo)

- Birth at Gournay-en-Bray, Normandy.
- Death 1093, in/near Le Bec-Hellouin, Eure.
- Wife: Basilie Flaitel (LY72-MRC), daughter of Gerard Flaitel, previously widow of Raoul de Gacé.
- Basilia died **16 January 1099/1100** — matches the repo's Chronicon Beccensis date "XVII Kal Feb."
- Burial at Abbey of Bec (Le Bec-Hellouin).
- Direct-line son **Gerard de Gournay** (LBGV-H99, b. ~1043, d. after 1104 Holy Land), m. **Edith de Warenne**.
- Gerard's children: **Hugues IV** (1098/1100–1180), **Gundred** (m. Nigel d'Aubigny Jun 1118, mother of Roger de Mowbray).
- Domesday holdings: Liston, Ardleigh, Fordham (Essex).
- Witnessed Caen charters 1082 — independently noted in MedLands.

### 2.2 Net-new content worth promoting

Each item supported by the **MedLands transcripts embedded in the FS PDF** (FMG citation reachable):

1. **1067 ducal charter to Saint-Benoît-sur-Loire** subscribed by `"…Hugonis de Gornaio…"` — earlier than the 1076 Bec charter the repo currently treats as the earliest datable Hugh-III appearance.
   > "…Hugonis de Gornaio…" subscribed the charter dated Apr 1067 under which "Willelmus…dux Normannorum…Anglorum rex" confirmed rights to the abbey of Saint-Benoît-sur-Loire[895].

2. **[1073] confirmation charter to Marmoutier** witnessed by Hugh III alongside Richard de Courcy, Rodulf fitz Herluin, William fitz Hastenc.
   > "…Hugo de Gurniaco, Ricardus de Curci, Rodulfus filius Herluini, Willelmus filius Hastenchi…" witnessed the charter dated to [1073] under which William I King of England confirmed the donation by "Nielli filii alterius Nielli" to the abbey of Marmoutier[896].

3. **[1089/90] Orderic Vitalis on Gerard delivering Gournay, La Ferté-en-Brai, and Gaillefontaine to William II Rufus** (Gerard's allegiance moment, but bookends Hugh III's Gerberoi-mediator role from 1079):
   > Orderic Vitalis records that "primus Normannorum Stephanus de Albamarla filius Odonis Campaniæ comitis" fortified "castellum suum super Aucium flumen" at the expense of William II King of England and placed there a garrison against "ducem" [Robert III Duke of Normandy] and that "Gornacensis Girardus" followed his example and delivered "Gornacum et Firmitatem et Goisleni Fontem" [Gournay, La Ferté-en-Brai, Gaillefontaine] to the king, dated to [1089/90][879].

4. **[1089] Orderic on Pont-Saint-Pierre / Écouché custody** — confirms Écouché was held by Gerard de Gournay, identified explicitly via Basilia. **Resolves Open Question #4 in the existing G33 research companion:**
   > Orderic Vitalis records that "comes Ebroicensis" requested Robert [III] Duke of Normandy to return "Bathventum et Nogionem, Vaceium et Craventionem, Scoceium [Bavent, near Troarn, Noyon-sur-Andelle, Gacé, Gravençon, Ecouché], aliosque fundos Radulfi patrui mei…Caput Asini" to him and grant "Pontem Sancti Petri" [Pont Saint-Pierre] to "nepoti…meo Guillelmo Bretoliensi", which the duke agreed to, except "Scoceium" which was held by "Girardus de Gornaco…qui de eadem parentela prodierat, filius…Basiliæ Girardi Fleitelli filiæ", dated to [1089][880].

5. **[1181/89] Henry II confirmation charter to Bec** explicitly naming `"Hugonis de Gornaco et Girardi filii…Girardi de Gornaio et Basilie matris sue"` — independent twelfth-century corroboration of the Hugh III → Gerard → Basilia donations. *Destination*: research companion footnote, fact-sheet citation strengthening.

6. **Anselm's letter "Basiliæ amicæ Filiæ in Domino" dated to after 1093** — discrete documentary anchor for the Anselm-friendship highlight currently relying on a secondary paraphrase. Note: the letter is to Basilia (not to Hugh) and the dating "after 1093" is part of the supporting reasoning that Hugh was already dead by the date of the letter.

7. **Amicie de Gournay / Talbot parentage problem** — substantive collateral question. FMG canvasses three hypotheses for the mother of Hugh Talbot (whose maternal uncle Hugh, son of Gerard, called him *nepos*): (a) Amicie was daughter of Gerard by Edith de Warenne; (b) daughter of Gerard by an earlier unrecorded wife (FMG's preferred reading); or (c) daughter of Hugh III himself, in which case she belongs in this file. *Destination*: new collateral case-file thread, not a person record.

8. **Gerard's First-Crusade attestation by name in two independent crusade chronicles**: Albert of Aix names "Gerardus de Gorna" at the siege of Nicaea (mid-1097); Baudry names "Girardus de Gornaio" among 1097 crusaders. Strengthens G32's narrative; not for this G33 file but flag back to G32.

### 2.3 FS conflicts with repo (FS likely wrong)

| Item | FS export | Repo | Disposition (Pass A) |
|---|---|---|---|
| Birth year | "about 1025" | c. 1020 | Repo retains. FS's own embedded ThePeerage entry says 1025 belongs to **Hugues II** (the father) — FS structured field has slid one generation. |
| Marriage date | "before 1050" | After 1051 (per FMG) | Repo correct. Raoul de Gacé died 1051; remarriage cannot precede that. FS's own embedded MedLands explicitly says "m (after 1051)". The structured field contradicts the source on the same person's page. |
| Burial date | "after 18 October 1101" | c. 1093 burial at Bec | FS's "1101" comes from FindAGrave Index entry on p. 8; this is a memorial-record-year, not a burial date. Repo retains. |
| Basilia's death **place** | "Gournay-en-Bray, Seine-Maritime" | Bec abbey | Repo correct. Chronicon Beccensis explicitly places her death at Bec; she had retired there with her niece Ansfride. |
| Number of children | 10 named (12 slots) | 1 in repo (Gerard) + 2 grandchildren via Gerard | FS over-shares. Of the FS list, only **Gerard**, **Guillaume** ([d.] after 1082), and **Hawise** (after 1112) are corroborated by FMG, all bracketed as uncertain. |
| Hugh III's mother | "Berthilde de Gerberoy" (PM9Z-R79) | repo G34 has no wife named | Pass-A verdict: **unsubstantiated** by FMG, DG, Hannay, Pettigrew, Farrer; flag as candidate to investigate. (Pass B revises this — see §3.) |
| "Hugues II killed at Cardiff 1074" applied to Hugh III on FS | FS embedded ThePeerage record on p. 4 | Repo's father chain is consistent | Repo correct. ThePeerage's "Hugues II" b. 1025 d. 1074 is mis-numbered; the repo's `familysearch-ids.csv` already flags numbering disagreement. |
| Wife's "third spouse" "Wiliam de Talbot I" (1030–1066) | FS structured field p. 1 | Not in repo | Spurious. No scholarly support; likely conflates the Talbot-Gournay relationship (Goisfred Talbot was sub-tenant at Liston in Domesday; later Richard Talbot married Amicie de Gournay). |

### 2.4 Spurious / over-claimed structured-field content

FS lists ten children for Hugh III. FMG/MedLands lists only **three** (`[Guillaume]`, Gerard, `[Hawise]`) and brackets two of those three as uncertain. The FS additions almost certainly arise from descendant trees collapsing two or three generations:

- **Hugues IV (G2QT-Z65, b. 1043)** — listed as son of Hugh III. **Wrong**: per MedLands, Hugues IV is *grandson* of Hugh III, son of Gerard, born c. 1098/1100. The 1043 birth date is a copy of his uncle Gerard's birth.
- **Adelaide de Gournay (LVKC-WC1, b. 1055)** — Joseph Depoin (early-1900s) speculated she belonged to "the house of Gournay" as wife of Yves II of Beaumont-sur-Oise. FMG explicitly rejects: *"the data on which the hypothesis rests is too imprecise to suggest that it is probable."*
- **Judith de Gournay (LK55-ZLY)** — duplicates Adelaide (b. 1055, Beaumont-sur-Oise) — appears to be a dup-record from FS tree merging.
- **Octave de Gournay** (m. Blandine de Chaumont 1077), **Edwige** (m. Hedouin de Gerberoy 1065), **Hugh** (b. ~1050 d. 1092), **Gunnora** (d. 1087 England) — none in FMG. Look like Geni / community-tree accretion.

**Heuristic**: trust the embedded MedLands transcripts, not the children list in the structured table.

---

## 3. Pass B — Racines Histoire (Pattou) supplement

The Racines Histoire pedigree (Etienne Pattou, *Seigneurs de Gournay (-en-Bray) & Gurney*, last update 2025-08-11) is **not** a thin community page; it is an 18-page scholarly chart-genealogy citing MedLands, Depoin, Pillet (1679), the 1844 *Recherches* of NRP de La Mairie, Daniel Gurney, and Wikipedia, with explicit critique of DG via Léopold Delisle. Several items I treated as "FS speculation" in Pass A actually have scholarly traction at a *different generation* than FS placed them.

### 3.1 Material updates to Pass A

1. **"Bathilde / Berthilde de Gerberoy" is real, but two generations up.** Pattou (p. 2) tentatively names "**? Bathilde de Gerberoy** (+1059)" as wife of **Hugues 1er de Gournay** (d. after 989/1046?), who fortified Gournay from 984. In repo terms this maps to roughly **G36 / G35 territory, not G34**. FS slid the name down two generations onto Hugh III's mother. Pass-A "unsubstantiated" verdict is revised to: name has scholarly traction (with `?` mark in red, indicating tentative attribution), but at G35–G36 level, not G33.
   > "Hugues 1er de Gournay + après 989 (1046 ?) seigneur de Gournay (fortifie Gournay dès 984) ép. ? Bathilde de Gerberoy + 1059"

   French Wikipedia confirms: "Hugues Ier de Gournay, vivant en 984, décédé après 989 (peut-être en 1046), épouse Bathilde de Gerberoy (morte en 1059)."

2. **The "Senex / Le Vieux / Le Vieil Huon" epithet belongs to Hugh II in Pattou, not Hugh III.** Pattou (p. 2) gives the epithet stack to **Hue II "L'Ancien / Le Vieux / Senex / Le Vieil Huon en 1050"** (X 1074 Cardiff). The repo's G33 fact sheet attributes "Hugo Senex" to Hugh III. **This is a possible mis-assignment** worth checking against DG's primary text.
   > "Hue (Hugues) II de Gournay dit «L'Ancien» ou «Le Vieux» ou «Senex» & «Le Vieil Huon» en 1050) +X 1074 (Cardiff, de ses blessures)"

3. **Pattou treats "Hugh II killed at Cardiff 1074" as fact**, in direct conflict with MedLands's `"the historical basis of the account is uncertain"`. Repo G34 narrative may be relying on the Cardiff legend; worth a check at G34 pass.

4. **Hugh III birth Pattou says ~1030**, repo c. 1020, FS 1025. Three-way disagreement. Pattou's 1030 is internally tightest given father d. 1074.
   > "Hugues III de Gournay ° ~1030 + 1093 (une source anglaise donne 18/10/1101)"

5. **Pattou asserts Hugh III became Prior of Saint-Nicaise de Meulan after Bec.** The repo's Pettigrew note is cautious about this. **Live conflict in scholarship** — keep both.
   > "moine à l'Abbaye du Bec puis Prieur de Saint-Nicaise de Meulan (fait donation de Laudencourt à l'Abbaye du Bec)"

6. **Domesday Latin entry headers** reproduced by Pattou (p. 2): useful for the repo's Open Domesday cross-reference.
   > "Domesday Book (1084): «XLVII. — Terra Hugonis de Gurnay, hundredum de Hidnigaforda. hundredum de Tendring. hundredum de Lessendena.»"

7. **Edwige de Gournay (m. Hédouin de Gerberoy)** sits in Pattou's **"Non connectés"** annex (p. 18) with explicit `?` — *not* in the main Hugh III children list. So FS over-claims, but Pattou doesn't reject either. Status: candidate collateral, not spurious.

8. **Adélaïde de Gournay (Depoin's hypothesis)**: Pattou places her as **possible sister** of Hugh III (i.e., daughter of Hugh II), not daughter, with `?` retained. FS places her as Hugh III's daughter. MedLands rejects the Depoin hypothesis altogether. **Three-way scholarly disagreement** to preserve.
   > "? Adélaïde (Adelhide) de Gournay + 08/04/1099 (selon J. Depoin) ép. avant 1081 (1075 ?) Yves II, comte de Beaumont (-sur-Oise, 95) seigneur de Conflans"

9. **Hugh II also fathered Néel/Nigel de Gournay**, who took the **Somerset line** (Barrow-Gurney, Inglishcombe, held of Bishop of Coutances; Domesday 1084). Pattou gives this collateral branch its own four pages (pp. 12–14), including Sir Thomas de Gournay (jailer of Edward II, 1327) and Sir Matthew of Crécy/Poitiers/Stoke-sub-Hamdon (b. 1310, d. 26/09/1406, "élogieusement cité par Froissart"). Useful disambiguation context.

10. **Daniel Gurney critique by Léopold Delisle** (Pattou p. 2; French Wikipedia confirms): *"ses travaux ont vite été critiqués par des érudits normands comme Léopold Delisle."* Delisle (1826–1910) was the leading 19th-century French medievalist. The repo relies heavily on DG. The **Delisle critique** is a research-topic thread the repo should track.

11. **The Norfolk junior line is fully charted by Pattou (pp. 5–11)**, including:
    - Walter de Gournay (Suffolk, Stephen's reign, ~1140) **"possible petit-fils de Girard de Gournay et d'Edive de Warenne"** — directly relevant to the repo's Walter-de-Gournay parentage problem in the G33 research file (line 99: Richardson rejected DG's claim).
    - **John III de Gournay m. Jeanne de Lexham, daughter of Edmond** — gives a wife and father-in-law for repo's **G25** that may not currently be recorded.
    - Antoine de Gournay (1511) → François (b. 20/08/1521, m. 06/08/1543 Helen Holditch) → Henry I (b. 21/01/1548 m. Ellene Blennerhasset) → Norfolk line down to Edward (1608–1641) and Henry II (1632–1661, branch extinction); then the cadet Francis of Maldon → John (Quaker, 1655–1721) → Joseph (1692–1750, bought Keswick 1747) → John (1716–1770) → Richard (b. 1743) → Hudson Gurney of Keswick (b. 1775).

    This material is **directly relevant to the repo's G7–G15 Norfolk-side chain** and should be cross-walked carefully in a separate intake pass per the user's batched-segment strategy.

12. **Heraldic annex** (pp. 15–17) reproduces the 1844 NRP de La Mairie *Recherches* engravings: Hugues V's seals (Nos. 1, 2), Mathieu de Gournay's seal (No. 3), the Gournay-Norfolk arms (No. 5), and the impaled-arms quarterings — Gournay-Baconsthorpe, Gournay-Middleton, Gournay-Kett, Gournay-Kerville, Gournay-Jerningham, Gournay-Calthorpe, Gournay-Heydon, Gournay-Holditch, Gournay-Blennerhasset, Gournay-Lewknor, Gournay-Hovel — plus seals of Robert de Gournay (No. 20) and Sibylle de Gournay (No. 21). **Research/topics or sources/media candidates** for a future heraldry pass.

### 3.2 Structural Pattou disagreement worth recording

- Pattou's chart on p. 2 places "Hugues 1er" → "Hue II" → "Hugues III" as a strict linear chain with Hugues I = the fortifier (d. after 989, possibly 1046). The repo treats Hugh I and Hugh II as **two separate generations** with Renaud (G35) between them. Pattou's chart **omits Renaud entirely** between Hugues 1er and Hue II. French Wikipedia treats Renaud as "douteux" (doubtful). FMG MedLands keeps Renaud as the bridge. The repo's chain (G34=Hugh II, G35=Renaud, G36=Hugh I) follows FMG. This is a structural conflict to surface at G35 and G36 passes.

---

## 4. FS Tree update suggestions

For discrepancies where the repo's value is better and FS is unsourced, so the user can update the FS Family Tree to reduce future-pass friction.

| FS field (PID MZ68-VKD) | Current FS value | Suggested correction | Repo / scholarly citation |
|---|---|---|---|
| Birth | "about 1025" | "c. 1020" or "c. 1030" range — both are scholarly options; FS's "1025" is unsupported | Repo: c. 1020 (DG); Pattou: ~1030 |
| Marriage | "before 1050, France" | "after 1051" (Raoul de Gacé died 1051) | FMG/MedLands explicitly "m (after 1051)"; embedded in this same export at p. 5 |
| Burial date | "after 18 October 1101" | Remove — this is a FindAGrave memorial-creation artifact, not a burial date | FindAGrave entry FAGI QVLX-4TM1 |
| Mother | "Berthilde de Gerberoy (PM9Z-R79)" | Detach. Move PM9Z-R79 up two generations to Hugues 1er (G36 territory), with `?` qualifier | French Wikipedia and Pattou place Bathilde de Gerberoy as wife of Hugues Ier, not Hugues II |
| "Other spouses" of wife | "Wiliam de Talbot I (GDLQ-MX5), 1030–1066" | Remove — spurious | No scholarly support; likely confusion with later Talbot-Gournay marriage (Amicie m. Richard Talbot) |
| Children #2 (Hugues IV b. 1043) | b. 1043, son of Hugh III | Move down one generation: Hugues IV is son of Gerard (LBGV-H99), b. [1098/1100] | FMG: "ii) HUGUES [IV] de Gournay ([1098/1100]-1180). Orderic Vitalis names 'Hugo filius Girardi de Gornaco'" |
| Children #6/7 (Adelaide / Judith) | daughters of Hugh III | Detach or move up one generation as candidate sister of Hugh III; quality of Depoin hypothesis is "non probable" per FMG | FMG: Depoin hypothesis explicitly rejected as not "probable" |
| Children #4 (Octave), #3 (Edwige), #5 (Hugh), #8 (Gunnora), #9 (Guillaume), #10 (Hawise) | listed as children of Hugh III | Of these, only Guillaume (after 1082) and Hawise (after 1112) are corroborated by FMG (bracketed as uncertain). Others should be detached or moved to "non connectés" status. | FMG names only 3 children for Hugues III, with 2 of 3 bracketed |

For discrepancies where FS is sourced (not many in this export):

| FS field | FS-cited source | Repo source | Recommended action |
|---|---|---|---|
| Hugh III as Hugues II b. 1025 d. 1074 (ThePeerage entry on p. 4) | Hans Harmsen e-mail to Darryl Lundy 2008 [S3268] | DG / FMG / Pattou | The Peerage entry is mis-numbered relative to MedLands. Hold open as a numbering footnote, do not adopt. |

---

## 5. URL triage

### Bucket A — auto-fetched
| URL | Status | Net-new content |
|---|---|---|
| https://www.wikitree.com/wiki/Gournay-10 | fetched (initial pass) | Calls subject "Hugh IV" rather than Hugh III; otherwise concordant. Useful detail: "retired with niece Ansfride c. 1082" matches Chronicon Beccensis triple-death sequence. |
| http://racineshistoire.free.fr/LGN/PDF/Gournay.pdf | fetched (companion PDF in repo at `sources/FS/MZ68-VKD/`) | Materially richer than expected — see §3 in full. **Highest-yield single URL in this export.** |
| https://fr.wikipedia.org/wiki/Famille_de_Gournay | fetched | Confirms Pattou's Bathilde de Gerberoy attribution at Hugues 1er level; states explicit Delisle critique of DG; explicit numbering caveat: *"la numérotation des Hugues est peut-être erronée."* |
| https://en.wikipedia.org/wiki/William_de_Warenne,_1st_Earl_of_Surrey | fetched | Confirms Edith m. Gerard de Gournay first then Drew de Monchy; modern scholarship silent on Conqueror-descent for Gundred. |

### Bucket B — needs human / login (handoff list)

| URL | Expected content | Failure mode | Suggested human action |
|---|---|---|---|
| https://www.geni.com/people/Hugues-de-Gournay-III/6000000000154070463 | Geni community profile aggregating multiple trees | Login wall typical for full-profile data | Browser visit while logged into Geni; paste any non-Geni-tree-derived sources into chat |
| https://www.thepeerage.com/p73110.htm | Lundy/Harmsen entry; relevant content already partially embedded in PDF p. 4 | Page may render but is mostly redundant with the embedded extract | Browser visit; only paste back if page contains content beyond the FS-embedded extract |
| https://familysearch.org/ark:/61903/3:1:3QS7-L9QB-X7F5?cc=2060211&wc=WWF8-FW3:352086301,352553201&i=81 | "Family Group Records Collection 1942–1969" image 82 of 1330 — LDS Archives Section card on Gerard de Gourney/Warren | Requires authenticated FS session for image viewer | Logged-in FS image fetch; download as `sources/FS/MZ68-VKD/fs-fgr-collection-1942-1969-img82.png` (or PDF), document what is on the card |
| http://familysearch.org/patron/source/photoId/203028445 | FamilySearch Memories upload of the Pattou PDF | Same FS auth path as above; redundant since we have the PDF directly | Skip — companion PDF already in `sources/FS/MZ68-VKD/` |
| https://gw.geneanet.org/jeanlev?lang=en&pz=jean+arsene+henri&nz=levallois&p=hugues&n=de+gournay+en+bray | Jean Levallois's Geneanet tree | Geneanet usually requires account for full tree access | Browser visit; only worth pasting back if it cites a primary source not already in MedLands or Pattou |
| http://search.ancestry.com/cgi-bin/sse.dll?dbid=70699&h=4725483 | Web International FindAGrave Index entry | Ancestry login required | Logged-in Ancestry visit; index entry only — likely redundant with the FS-side FindAGrave index already shown |
| https://books.google.fr/books?id=Hp9rQFd3ILgC&hl=fr&pg=RA2-PR200 | Histoire de Lorraine Vol. V — Maison de Gournay introduction starting p. cxcix | Google Books may show snippet only depending on copyright | Browser visit; download/screenshot pp. cxcix–cciii if shown |
| http://www.lewisfamilytree.com/suggest.php?enttype=I&ID=I345&tree=lewis | TNG-style "Lewis-Powers Family History" entry | TNG sites often work but may aggregate community sources | Browser visit; low priority, very unlikely to add primary-source value |

### Bucket C — redundant / low-value (justified skips)

| URL | Reason for skip |
|---|---|
| https://fmg.ac/Projects/MedLands/normacre.htm# | Substantively embedded in the FS PDF (pp. 4–7 and pp. 8–9). The Wayback URL `https://web.archive.org/web/20240826200046/...` is the more stable retrieval target if needed. |
| https://babel.hathitrust.org/cgi/pt?id=yale.39002006511357 | Daniel Gurney 1848 — already in repo source canon (DG-I, DG-Supp). |
| https://familysearch.org/ark:/61903/1:1:QVLX-4TM1 (FindAGrave Index for Hugues III, 1101) | Memorial-record-only; no biographical detail beyond what's already extracted. |
| https://familysearch.org/ark:/61903/1:1:QVLX-4T9M (FindAGrave Index for Basila Flaitel, 1099) | Memorial-record-only. |
| http://search.ancestry.com/cgi-bin/sse.dll?dbid=3599&h=2772993 (AGBI for Basila Flaitel) | American Genealogical-Biographical Index — too modern/derivative. |
| http://search.ancestry.com/cgi-bin/sse.dll?dbid=60541&h=2813093 (Global FindAGrave for Basila) | Same as above. |

---

## 6. Combined disposition (Pass A + Pass B)

**Probable adopt** (research companion edits, citing FMG MedLands as primary; needs `data/sources.json` entry for `fmg-medlands-normandy-acre` if not present):
1. Add the **1067 Saint-Benoît-sur-Loire** and **1073 Marmoutier** charter witnesses to the research companion's "Working Notes" / "Open Questions #1" (Orderic/charter index).
2. Add the **[1181/89] Henry II Bec confirmation charter** as independent corroboration in the "1076 Bec charter" working note.
3. Resolve **Open Question #4 (Écouché)** using the [1089] Orderic passage on Gerard's custody. This converts an open question into a confirmed fact: Gerard (and by extension Hugh III's family) retained Écouché after Basilia's death.
4. Add **Anselm's post-1093 letter to Basilia** as a discrete documentary anchor for the Anselm-friendship highlight.
5. Add the **Domesday Latin hundred-headers from Pattou** ("hundredum de Hidnigaforda. hundredum de Tendring. hundredum de Lessendena.") as a direct citation aid for the Open Domesday cross-reference.
6. Open a new collateral case-file thread for **Amicie de Gournay / Talbot** (parentage problem with three FMG hypotheses).
7. **Surface the "Senex" epithet conflict**: research companion should record that Pattou applies the "Le Vieux / Senex / Le Vieil Huon" epithet stack to Hugh II not Hugh III. The fact-sheet currently attributes "Hugo Senex" to Hugh III. The DG primary should be re-checked at the G34 pass to resolve.
8. **Open a Delisle-critique thread**: a `research/topics/dg-reception-delisle-critique.md` (or similar) tracking that DG was challenged by Delisle and that Pattou treats DG with explicit caution.

**Decline / quarantine**:
- All ten "extra" FS children except the three FMG-attested (Guillaume, Gerard, Hawise — last two bracketed).
- "Berthilde de Gerberoy" as Hugh III's mother. (But: forward this name to the **G35/G36 pass** as a candidate at that level.)
- 18 Oct 1101 burial date.
- Wife's third-spouse "Wiliam de Talbot I" entry.

**`data/sources.json` bookkeeping** (if this becomes a real patch):
- Add `fmg-medlands-normandy-acre` (URL `https://fmg.ac/Projects/MedLands/normacre.htm`, with Wayback `https://web.archive.org/web/20240826200046/...` as fallback).
- Add `pattou-racines-histoire-gournay-2025` for the companion PDF (URL `http://racineshistoire.free.fr/LGN/PDF/Gournay.pdf`, last-update 2025-08-11 known).
- Add `chronicon-beccensis-abbatiae` for the Bec necrology / chronicle entries on Basilia and Ansfride.
- Add `orderic-vitalis-historia-ecclesiastica-prevost` and `-chibnall` for the two main critical editions cited by FMG ([879], [880], [887], [888], etc.).

---

## 7. Open items still requiring human judgment

1. **Numbering**: FS calls him Hugh **III**, WikiTree calls him Hugh **IV**, MedLands brackets him `[III]`, French Wikipedia says numbering is "peut-être erronée." The repo uses III consistently; recommend keeping but adopt French Wikipedia's caveat language ("numbering of the Hugues may be erroneous") in a research note.
2. **"Senex" epithet at which generation**: Pattou applies it to Hugh II. Repo applies it to Hugh III. Resolution requires DG-I p. 24 close re-reading and possibly Hannay pp. 71–91. Until resolved, the fact sheet's "Hugo Senex" highlight should be either softened or moved.
3. **"Hugh II killed at Cardiff 1074"**: MedLands explicitly says "the historical basis of the account is uncertain." Pattou treats it as fact. Repo G34 currently retains the tradition with caveat. Resolution: see G34 pass.
4. **Hugh III as Prior of Saint-Nicaise de Meulan**: Pattou asserts; Pettigrew is cautious. Resolution requires checking DG-I primary text and Pettigrew vol. 2 pp. 183–185.
5. **Two-vs-three sons question**: The "Brown book" note in the FS PDF (p. 8) says Hugh III "Married 1st & had 2 sons. Married 2nd and had 1 daughter." This contradicts FMG (one wife, three children). The Brown book is undocumented; should be discounted.
6. **Norfolk junior line junction**: FS embedded note from "Royal Ancestry life sketch" (pp. 7, 13) explicitly disputes DG's Walter-as-son-of-Gerard claim, citing Hasted, Copinger, Loyd & Stenton, Gervers, Power, Tanner. This is a major thread for the G31/G32 transition and should be surfaced in the G32 pass and in any case file on the Norfolk-junior-line origin.
