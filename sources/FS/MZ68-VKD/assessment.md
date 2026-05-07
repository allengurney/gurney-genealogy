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

**Correction after careful re-read of Pattou p. 2 with line-style attention** (see also §8 addendum below). My earlier claim that "Pattou's chart omits Renaud entirely between Hugues 1er and Hue II" was wrong. The corrected reading:

Pattou's page 2 chart uses **two distinct line styles** to encode certainty:
- **Solid lines** for the main chain Pattou treats as documented: Eudes → ?Hugues de Gournay (an unnamed intermediate generation, with `?`) → Hugues 1er → Hue II → Hugues III
- **Dashed lines** branching off Eudes diagonally to a separate `?` marker, then dashed down to "? Renaud, seigneur de Gournay ép. Albérade" → solid line from Renaud down to Gauthier de La Ferté

So Pattou **does include Renaud**, but as a **parallel uncertain figure** at roughly the same horizontal level as Hugues 1er, connected to Eudes through a chain of dashed `?` connectors rather than the solid main chain. The visual encoding tracks the textual narrative on the same page: *"Daniel Gurney suggère un lien familial entre les maisons de La Ferté et de Gournay. Il fait d'Hugues de Gournay un des descendants de Renaud et Aubrée (Alberade), parents du fondateur de la collégiale de La Ferté."* (Translation: *Daniel Gurney suggests a family link between the houses of La Ferté and Gournay. He makes Hugues de Gournay one of the descendants of Renaud and Aubrée [Alberade], parents of the founder of the collegiate church of La Ferté.*) Pattou is presenting DG's chain (Renaud → Hugues de Gournay) as a hypothesis Pattou is unwilling to fully endorse — hence the dashed lines.

The repo's chain (G34=Hugh II, G35=Renaud, G36=Hugh I, G37=Eudes) puts Renaud in the main vertical line per FMG. Pattou treats this same Renaud as parallel-and-uncertain rather than ancestor-and-uncertain. The structural conflict is real — Pattou's `?` figure called "? Hugues de Gournay" at the position between Eudes and Hugues 1er does not correspond to any generation in the repo's chain. If Pattou's Eudes → ?Hugues → Hugues 1er chain is correct, then either (a) the repo's G37=Eudes is right but the repo is missing Pattou's intermediate ?Hugues; or (b) the repo's G36=Hugh I and Pattou's "Hugues 1er" map to the same person, and Pattou's "?Hugues de Gournay" is a separate phantom generation not in the repo. The la Ferté charter only attests Renaud and his sons Hugues + Gauthier — it doesn't constrain whether other Hugues figures sit between Renaud and the fortifier.

**Bottom line**: Pattou is *more* cautious than I previously stated — he tags both Renaud's chain AND the Hugues-1er chain with `?` markers and shows both in the chart. French Wikipedia goes further: *"la numérotation des Hugues est peut-être erronée"* (*the numbering of the Hugues may be erroneous*) and *"Renaud (douteux)"* (*Renaud [doubtful]*). The repo's "Confirmed" classification for G35 Renaud follows FMG, which keeps Renaud as the bridge based on the la Ferté charter. Pattou and French Wikipedia would both classify Renaud as Uncertain. The repo's choice is defensible (the la Ferté charter is a primary attestation, even if preserved only in transcription via the lost Gondeville MS) but should be made consciously.

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

**Updated 2026-05-06 after first collaborative URL pass.** Items moved to Bucket A or C as noted.

| URL | Status | Outcome |
|---|---|---|
| https://www.geni.com/people/Hugues-de-Gournay-III/6000000000154070463 | **Moved to Bucket A** | See §9 below — substantial yield including new sibling claims, Mellcene Smith narrative, R.B. Stewart entry. |
| https://familysearch.org/ark:/61903/3:1:3QS7-L9QB-X7F5?cc=2060211&wc=WWF8-FW3:352086301,352553201&i=81 | **Moved to Bucket C** | URL no longer exists (FS image-server returned 404). Skip. |
| https://books.google.fr/books?id=Hp9rQFd3ILgC&hl=fr&pg=RA2-PR200 | **Moved to Bucket A** | Histoire de Lorraine downloaded as 116MB PDF at `sources/FS/Histoire_de_Lorraine_depuis_l_entrée_de.pdf` (gitignored due to GitHub size limit). Text extract committed at `sources/FS/lorraine-maison-de-gournay-extract.txt`. See §9 below. |
| https://www.thepeerage.com/p73110.htm | Bucket B (deferred) | Lundy/Harmsen entry; relevant content already partially embedded in PDF p. 4 | Browser visit; only paste back if page contains content beyond the FS-embedded extract |
| http://familysearch.org/patron/source/photoId/203028445 | Bucket C — skip | FamilySearch Memories upload of the Pattou PDF; companion PDF already in `sources/FS/MZ68-VKD/`. |
| https://gw.geneanet.org/jeanlev?lang=en&pz=jean+arsene+henri&nz=levallois&p=hugues&n=de+gournay+en+bray | Bucket B (deferred) | Jean Levallois's Geneanet tree. Browser visit; only worth pasting back if it cites a primary source not already in MedLands or Pattou. |
| http://search.ancestry.com/cgi-bin/sse.dll?dbid=70699&h=4725483 | Bucket B (deferred) | Web International FindAGrave Index entry. Ancestry login required. Likely redundant. |
| http://www.lewisfamilytree.com/suggest.php?enttype=I&ID=I345&tree=lewis | Bucket B (deferred) | TNG-style "Lewis-Powers Family History" entry. Low priority. |

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

---

## 8. Pattou Re-Read Addendum (after careful re-read with line-style attention)

The original Pattou ingestion in §3 above relied primarily on text extraction and missed several visual cues. A careful re-read of the chart-genealogy with attention to line styles (solid vs. dashed/dotted), color coding (red text = hypothesis-tagged), positional placement, and `?` markers surfaced the following corrections and net-new findings.

### 8.1 Corrections to original Pattou ingestion (§3)

1. **§3.2 "Pattou's chart omits Renaud entirely"** — corrected in §3.2 above. Pattou actually shows Renaud via dashed-line parallel branch from Eudes; he is included with `?` markers, not omitted.
2. **§3.1 item 7 "Edwige de Gournay … sits in Pattou's 'Non connectés' annex"** — addition: Pattou's p. 18 entry on Edwige names her husband **Hédouin de Gerberoy** in **red text** (Pattou's hypothesis-tagging color). The full Pattou entry on Edwige reads: *"? Edwige de Gournay ° ~1049 + 1098 ép. Hédouin de Gerberoy, chevalier, seigneur de Gerberoy et Martincourt, croisé (1096) ° 1045 + 1108"* (Translation: *"? Edwige de Gournay, born ~1049, died 1098, married Hédouin de Gerberoy, knight, lord of Gerberoy and Martincourt, crusader (1096), born 1045, died 1108"*). **This is the historical Hédouin de Gerberoy.** It explains the FS-tree confusion at G34: FS attached a "Hedouin er de Gerberoy" (PID `GYL7-YRW`) as the *father* of Berthilde de Gerberoy at G34's wife slot — this is wrong on two counts: (a) the historical Hédouin was Edwige de Gournay's *husband* (not Berthilde's father), and (b) Bathilde de Gerberoy belongs at the Hugues 1er level per Pattou and French Wikipedia, not at Hugues II.
3. **§3.1 (Hawise as Hugh III's daughter)** — addition: Pattou's p. 3 chart shows Hawise via a **dashed horizontal line** with the explicit annotation *"(peut-être fille d'Hugues IV)"* in BLUE (cross-reference color). Translation: *"(perhaps daughter of Hugues IV)"*. So Pattou is hedging Hawise's parentage between Hugues III (where FS places her) and Hugues IV (alternative). FMG places her as Hugues III's child but with brackets `[HAWISE]`.
4. **§3.1 (Amicie / Talbot)** — addition: Pattou's p. 3 chart shows Amicie via a connector with annotation *"(peut-être fille d'Hugues III)"* in BLUE under "1) Amicie de Gournay ° avant 1085 + après 1100". Translation: *"(perhaps daughter of Hugues III)"*. So Pattou places her primarily as Girard's first-marriage daughter but explicitly entertains the FMG third-hypothesis (daughter of Hugues III) as alternative.

### 8.2 Net-new findings from careful re-read (not in §3)

1. **The 1335 Philippe de Valois charter** (Pattou p. 2 sidebar narrative, missed in first pass):

   > *"Hugues de La Ferté (Hugone) et Hugues de Gournay sont nommés dans une charte de Philippe de Valois de 1335 comme contemporains de Guillaume, comte d'Arques + après 1052"*

   Translation: *"Hugues de La Ferté (Hugone) and Hugues de Gournay are named in a charter of Philippe de Valois of 1335 as contemporaries of Guillaume, count of Arques [who died] after 1052."*

   This is a **14th-century retrospective document** in which Philippe VI of France (Philippe de Valois, r. 1328–1350) refers back to a Hugues de La Ferté and a Hugues de Gournay as having been contemporaries of William, Count of Arques (the Conqueror's uncle, exiled to Boulogne after 1053, d. after 1052). The charter implies a shared 11th-century context for the La Ferté and Gournay families. **Worth searching for**: locate the 1335 Philippe de Valois charter in the *Actes de Philippe VI* or the Trésor des Chartes (AN J series) — would be a primary citation tying La Ferté and Gournay to the Conquest era.

2. **"Hugues II reçoit des fiefs en Essex et en Suffolk; Néel reçoit plusieurs domaines en Somerset près Bristol et Bath."** (Pattou p. 2 sidebar) — Translation: *"Hugues II receives fiefs in Essex and Suffolk; Néel receives several domains in Somerset near Bristol and Bath."* Pattou treats the post-Conquest Essex/Suffolk fiefs as awarded to **Hugues II** (the Cardiff-1074 generation) and the Somerset domains as a separate cadet share to **Néel** (Hugues II's other son). Hugues III then inherited the Essex/Suffolk fiefs by 1086 Domesday. This is a different chronology from the repo's narrative which has Hugh III at Hastings and receiving the Essex manors directly. **Note the repo's `familysearch-ids.csv` line for G34 already says "Hannay says Hugh II killed at Cardiff 1074, fact-sheet keeps as died c. 1074 from wounds";** Pattou's chronology is consistent with that.

3. **Pattou main solid chain includes an unnamed "?Hugues de Gournay"** between Eudes and Hugues 1er (see §3.2 corrected). Pattou's chart positions this person as a separate boxed name with `?` marker. **The repo does not have this generation.** If Pattou is right, the repo's G37 → G36 jump skips an intermediate. The repo's G37 entry already classifies Eudes as "Tradition" — a similar treatment is defensible for the Pattou ?Hugues if adopted. Most parsimoniously: leave the repo as-is and footnote Pattou's variant.

4. **Adelaide de Gournay / Yves II de Beaumont — Pattou's full chart entry** (p. 2):

   > *"? Adélaïde (Adelhide) de Gournay + 08/04/1099 (selon J. Depoin) ép. avant 1081 (1075 ?) Yves II, comte de Beaumont (-sur-Oise, 95) seigneur de Conflans + un 22/05 entre 1083 et 1095 (fils de Yves 1er + 22/05/1089, et d'Emma ; veuf de Judith, selon Orderic Vital)"*

   Translation: *"? Adélaïde (Adelhide) de Gournay, died 8 April 1099 (per J. Depoin), married before 1081 (1075?) Yves II, count of Beaumont(-sur-Oise, postal dept. 95), lord of Conflans, died on a 22 May between 1083 and 1095 (son of Yves I, who died 22 May 1089, and of Emma; widower of Judith, per Orderic Vital)."*

   Pattou places her as **`?` daughter of Hugues II** (positioned at the Hugues-II generation in the chart), not as daughter of Hugues III. So three positions exist: FS = daughter of Hugues III; Pattou = `?` daughter of Hugues II; FMG = rejects the Depoin hypothesis altogether ("the data on which the hypothesis rests is too imprecise to suggest that it is probable"). Pattou's chart has the `?` marker as a hedge.

5. **Néel/Nigel de Gournay — Pattou's full chart entry** (p. 2):

   > *"? Néel (Nigel) de Gournay participe à la conquête en 1066"*

   Translation: *"? Néel (Nigel) de Gournay participates in the [English] conquest of 1066"*

   Positioned at the Hugues-II generation, with `?` marker indicating uncertainty about his parentage. He is identified as the founder of the Somerset Gurney cadet line (Pattou pp. 12–14 expand). The `?` is on his identity *as a Gournay son*, not on his existence — Pattou clearly treats Néel as a real historical Domesday landholder in Somerset.

6. **Henry "Le Jeune" King of England sacks Gournay c. 1073** (Pattou p. 2 sidebar):

   > *"Henry «Le Jeune», Roi d'Angleterre, s'empare de Gournay ~1073 qu'il ravage et dont il rançonne le seigneur, son fils, 24 chevaliers et quelques bourgeois"*

   Translation: *"Henry 'the Young', King of England, seizes Gournay ~1073 which he ravages, and ransoms the lord, his son, 24 knights, and several burghers."*

   **Note the chronological problem**: there was no Henry "the Young King" in 1073 (Henry the Young King is the son of Henry II, crowned co-king 1170, d. 1183). This must be a Pattou typesetting error — likely refers either to William II Rufus or to Robert Curthose. The "ransoms 24 knights and burghers" detail is interesting and should be checked against DG and the Roman de Rou. The "24 knights" number echoes the "24 villages" of the Conquêts Hue de Gournay, possibly via confused recall.

7. **Hugues III "fait donation de Laudencourt à l'Abbaye du Bec"** (Pattou p. 2). Translation: *"makes donation of Laudencourt to the Abbey of Bec."* Concordant with the existing G33 research companion (line 40, Pettigrew note: gifts to Bec included "Laudencourt"). Pattou uses the same place name spelling.

8. **Pattou's Hugues III description fully reproduced** (p. 2):

   > *"Hugues III de Gournay ° ~1030 + 1093 (une source anglaise donne 18/10/1101) seigneur de Gournay, établi en Angleterre (cité dans une charte de Jumièges ~1040) (investi de Liston, Ardleigh et Fordham (Essex) après la conquête selon le Domesday Book de 1084), moine à l'Abbaye du Bec puis Prieur de Saint-Nicaise de Meulan (fait donation de Laudencourt à l'Abbaye du Bec) ép. après 1051 Basilie Flaitel (alias Flaiteau, Wilteln) ° ~1025 + 16/01/1100 ns (fille de Gérard ; veuve de Raoul de Gacé (fils cadet de Robert Archevêque de Rouen et comte d'Evreux) ; soeur d'Agnès, épouse de Walter Giffard, 1er comte de Buckingham ; & soeur de Guillaume, Evêque d'Evreux et d'Anselme de Ribemont)"*

   Translation: *"Hugues III de Gournay, born ~1030, died 1093 (an English source gives 18/10/1101), lord of Gournay, established in England (cited in a charter of Jumièges ~1040) (invested with Liston, Ardleigh and Fordham [Essex] after the conquest per the Domesday Book of 1084), monk at the Abbey of Bec then Prior of Saint-Nicaise de Meulan (makes donation of Laudencourt to the Abbey of Bec), married after 1051 Basilie Flaitel (alias Flaiteau, Wilteln), born ~1025, died 16 January 1100 [new style] (daughter of Gérard; widow of Raoul de Gacé [younger son of Robert Archbishop of Rouen and count of Évreux]; sister of Agnès, wife of Walter Giffard, 1st earl of Buckingham; and sister of Guillaume, Bishop of Évreux, and of Anselme de Ribemont)."*

   **New surnames/aliases for Basilia**: Pattou notes her family name is recorded variously as "Flaitel," "Flaiteau," and "Wilteln" — three orthographic variants the repo's research companion can adopt as aliases.
   **New sibling for Basilia**: "Anselme de Ribemont" is named alongside Guillaume Bishop of Évreux as Basilia's brother. Anselme de Ribemont (d. 1099) was a known crusader and chronicler — if confirmed as Basilia's brother, this is a new collateral connection. The existing repo notes Agnès (m. Walter Giffard) and Guillaume (Bp Évreux) but not Anselme de Ribemont. Note: FMG MedLands does NOT list Anselme de Ribemont among Gerard Flaitel's children (only Guillaume, Anscher, Robert, son(s), Albert, Ermengarde, Basilie). So Pattou's claim diverges from FMG. **Hold as a candidate sibling, do not adopt without further verification.**

9. **The "écu noir" (black shield) origin legend** — Pattou p. 2 sidebar:

   > *"Selon la légende familiale, Rollon aurait confié le territoire de Gournay-en-Bray à un certain Eudes, chevalier à l'écu noir, point de départ de la lignée. Ceci n'est pas ou peu attesté."*

   Translation: *"According to family legend, Rollon would have entrusted the territory of Gournay-en-Bray to a certain Eudes, the knight with the black shield, starting point of the lineage. This is not or barely attested."*

   Confirms the repo's G37 "tradition only" classification. The "écu noir" detail also explains the Pattou heraldry note on p. 1: *"Gournay (origine) : «De sable plein»"* — the original Gournay arms were plain sable, matching the legend's "knight with the black shield."

### 8.3 Source Materials — Full Verbatim Extracts

#### 8.3.1 Foundation for Medieval Genealogy (FMG MedLands) — Hugues III de Gournay

Reproduced verbatim from FS PDF pp. 5–7 (web.archive.org snapshot of `fmg.ac/Projects/MedLands/normacre.htm#AmicieGournayMRichardTalbot`):

> HUGUES [III] de Gournay (-[1093]). "Domino meo Hugone Gurnacensi et filio eius Girardo et uxore eius Basilia" consented to the donation by "Radulfus cognomine Havoth" to Jumièges by charter dated to [1040][893], although presumably the document is misdated. The Chronique de Normandie, based on le Roman de Rou, names "Hue de Gournay sire de Bray" and "le Conte Hue de Gournay" among those who took part in the conquest of England in 1066, the two similar names suggesting that they were father and son[894]. "…Hugonis de Gornaio…" subscribed the charter dated Apr 1067 under which "Willelmus…dux Normannorum…Anglorum rex" confirmed rights to the abbey of Saint-Benoît-sur-Loire[895]. "…Hugo de Gurniaco, Ricardus de Curci, Rodulfus filius Herluini, Willelmus filius Hastenchi…" witnessed the charter dated to [1073] under which William I King of England confirmed the donation by "Nielli filii alterius Nielli" to the abbey of Marmoutier[896].
>
> Domesday Book records "Hugh de Gournai" holding Liston, Ardleigh and Fordham in Essex[897]. Henry II King of England confirmed the possessions of the abbey of Bec, including donations by "Hugonis de Gornaco et Girardi filii", by charter dated to [1181/89][898].
>
> m (after 1051) as her second husband, BASILIE, widow of RAOUL de Gacé, daughter of GERARD Flaitel & his wife --- (-16 Jan [1099/1100]). Guillaume de Jumièges records that "Galterium Giffardum primum" married "unam filiarum Girardi Flatelli" and that "alteram...Basiliam relictam Rodulphi de Waceio" married [secondly] "Hugo de Gornaco"[899]. "Domino meo Hugone Gurnacensi et filio eius Girardo et uxore eius Basilia" consented to the donation by "Radulfus cognomine Havoth" to Jumièges by charter dated to [1040][900], although presumably the document is misdated. Anselm Archbishop of Canterbury wrote to "Basiliæ amicæ Filiæ in Domino", dated to after 1093[901]. The Chronicon Beccensis Abbatiæ records that "tempore S. Anselmi abbatis Becci tres matronæ nobiles…Basilia uxor Hugonis de Gornaco, et Amfrida neptis ipsius Basiliæ, et Eva uxor Guillelmi Crispini" entered Bec and lived at the abbey, adding that they died on three consecutive Sundays "Amfrida Basiliæ neptis...minor...ætate, virgo…IV Non Jan, qua sepulta…Basilia domina eius…XVII Kal Feb…tertia Eva…X Kal Feb...post mortem...viri sui Guillermi Crispini...Beccique usque ad finem vitæ...perseuerauit"[902]. Gurney dates the passage to [1099/1100][903]. Henry II King of England confirmed the possessions of the abbey of Bec, including donations by "Hugonis de Gornaco et Girardi filii…Girardi de Gornaio et Basilie matris sue", by charter dated to [1181/89][904]. Hugues [III] & his wive(s) had [three] children:
>
>  a) [GUILLAUME de Gournay (-after 1082). "…William de Gornai…Girard de Gornai…" witnessed the charter dated 1082 under which William I King of England donated property to the abbey of la Trinité de Caen[457].]
>
>  b) GERARD de Gournay (-Palestine after 1104). [— full entry transcribed at G32 assessment §8.3]
>
>  c) [HAWISE de Gournay (-after 1112).

**Translation of key Latin charter excerpts**:

- *"Domino meo Hugone Gurnacensi et filio eius Girardo et uxore eius Basilia"* — *"My lord Hugues of Gournay and his son Girard and his wife Basilia"* (the formula used in the [1040, presumed misdated] Jumièges charter for Radulfus Havoth's entry as a monk — the family was named as the donor's overlord whose consent was required).
- *"Hue de Gournay sire de Bray"* and *"le Conte Hue de Gournay"* — *"Hue de Gournay, lord of Bray"* and *"the Count Hue de Gournay"* — the two names from the Roman de Rou that suggest father and son both at Hastings.
- *"Hugonis de Gornaio"* — *"of Hugues of Gournay"* (subscribing the April 1067 Saint-Benoît-sur-Loire confirmation by William as Duke of Normandy and King of the English).
- *"Hugo de Gurniaco, Ricardus de Curci, Rodulfus filius Herluini, Willelmus filius Hastenchi"* — *"Hugo de Gournay, Richard de Courcy, Rodulf fitz Herluin, William fitz Hastenc"* — the witness list of the [1073] Marmoutier confirmation.
- *"Hugh de Gournai"* — *"Hugh of Gournay"* (Domesday Book entry).
- *"Hugonis de Gornaco et Girardi filii"* — *"of Hugues of Gournay and his son Girard"* (Henry II's [1181/89] Bec confirmation).
- *"Galterium Giffardum primum"* and *"unam filiarum Girardi Flatelli"* — *"Walter Giffard the first"* and *"one of the daughters of Girard Flaitel"* (Guillaume of Jumièges on Walter Giffard's marriage to Basilia's sister).
- *"alteram…Basiliam relictam Rodulphi de Waceio"* — *"the other [daughter]…Basilia, widow of Rodulph of Gacé"* (Guillaume of Jumièges on Basilia's first widowing).
- *"Hugo de Gornaco"* — *"Hugues of Gournay"* (Basilia's second husband per Guillaume of Jumièges).
- *"Basiliæ amicæ Filiæ in Domino"* — *"To Basilia, beloved Daughter in the Lord"* — Anselm's letter salutation to Basilia, dated post-1093 (i.e., after Anselm became Archbishop of Canterbury).
- *"tempore S. Anselmi abbatis Becci tres matronæ nobiles…Basilia uxor Hugonis de Gornaco, et Amfrida neptis ipsius Basiliæ, et Eva uxor Guillelmi Crispini"* — *"In the time of St. Anselm, abbot of Bec, three noble matrons… Basilia wife of Hugues of Gournay, and Amfrida niece of the same Basilia, and Eva wife of William Crispin"* — the Chronicon Beccensis triple-death sequence at Bec.
- *"Amfrida Basiliæ neptis...minor...ætate, virgo…IV Non Jan, qua sepulta…Basilia domina eius…XVII Kal Feb…tertia Eva…X Kal Feb"* — *"Amfrida, niece of Basilia, the youngest in age, a virgin, [died] on the 4th day before the Nones of January [= 2 January], on which day she was buried; Basilia her mistress [died] on the 17th day before the Kalends of February [= 16 January]; the third, Eva, [died] on the 10th day before the Kalends of February [= 23 January]"* — the three consecutive Sundays.
- *"post mortem...viri sui Guillermi Crispini...Beccique usque ad finem vitæ...perseuerauit"* — *"after the death of her husband William Crispin, [Eva] persevered at Bec until the end of her life"* — the Eva continuation.
- *"Hugonis de Gornaco et Girardi filii…Girardi de Gornaio et Basilie matris sue"* — *"of Hugues of Gournay and his son Girard…of Girard of Gournay and Basilia his mother"* (the [1181/89] Henry II Bec charter naming all three Gournay donors across generations).

#### 8.3.2 FMG MedLands — Amicie de Gournay / Talbot parentage problem (full)

Reproduced verbatim from FS PDF p. 5 (also pp. 5–6 G32 export):

>  i) [AMICIE de Gournay (before [1085]-[after 1100]). Her marriage and family connection are indicated by Orderic Vitalis who records that "Hugo filius Girardi de Gornaco" rebelled against King Henry I after the marriage of his sister Gundred in Jun [1118], and captured "municipium...Plessicii" which he granted to "nepoti eius Hugoni Talabot"[888]. The passage indicates that Hugh Talbot was at least a young adult at the time, so not born later than [1100], which would place his mother's birth no later than [1085]. There are therefore at least three possibilities for her parentage. Firstly, if she was the child of Gérard de Gournay by his known wife Edive de Warenne, Edive would have been born in the early part of her estimated birth date range shown above and Amicie born soon after the marriage. Secondly, given that that chronology is tight, Amicie could have been the daughter of Gérard by an earlier otherwise unrecorded marriage. Thirdly, the word "nepos" in Orderic could indicate a more distant family relationship than nephew, maybe first cousin, in which case Amicie could have been the daughter of Hugues [III] de Gournay, although the more remote the relationship the less likely the appointment of Richard Talbot as custodian of the castle by Hugues [IV] de Gournay. On balance, the most likely case appears to be the second. Her name is indicated by two charters of King Henry II: Henry II King of England confirmed the possessions of the abbey of Valmont, including donations by "…Richardi Tallebot et Amicie uxoris eius et Hugonis et Willelmi filiorum suorum…", by charter dated to [1181/83][889]. Henry II King of England confirmed the possessions of the priory of Sainte-Foi de Longueville, including donations by "Ricardi Thalebot et Avitie uxoris sue et Hugonis filii sui", by charter dated to [Mar/Jun] 1189[890]. m RICHARD Talbot, son of ---.]

**Translation of key Latin / Old French**:
- *"Hugo filius Girardi de Gornaco"* — *"Hugues, son of Girard of Gournay"* (= Hugues IV).
- *"municipium...Plessicii"* — *"the fortified place...of Le Plessis"* — castle Hugues IV captured during his 1118 rebellion against Henry I.
- *"nepoti eius Hugoni Talabot"* — *"to his nephew Hugh Talbot"* — but as FMG notes, *nepos* can also mean "grandson" or more distant kin like first cousin, which is the source of the parentage ambiguity.
- *"Richardi Tallebot et Amicie uxoris eius et Hugonis et Willelmi filiorum suorum"* — *"of Richard Talbot and Amicia his wife and Hugues and William their sons"* (Henry II's [1181/83] Valmont confirmation).
- *"Ricardi Thalebot et Avitie uxoris sue et Hugonis filii sui"* — *"of Richard Talbot and Avicia [variant of Amicia] his wife and Hugues his son"* (Henry II's [Mar/Jun] 1189 Sainte-Foi de Longueville confirmation).

#### 8.3.3 FMG MedLands footnote references for the Hugues III entry

Reproduced verbatim from FS PDF pp. 6–7:

> [875] Jumièges, Tome I, XXI, p. 66.
> [876] Gurney (1845), p. 57, quoting "an old copy in a paper Cartulary of Jumieges", Rouen Archives.
> [877] Regesta Regum Anglo-Normannorum (1913), Vol. I, 150, p. 41.
> [878] Dugdale Monasticon III, York St Mary, V, p. 548.
> [879] Orderic Vitalis (Prévost), Vol. III, Liber VIII, IX, p. 319.
> [880] Orderic Vitalis (Prévost), Vol. III, Liber VIII, X, p. 321.
> [881] Domesday Descendants, p. 492.
> [882] Albert of Aix (RHC), Liber II, Cap. XXIII, p. 316.
> [883] Baudry (RHC) II.I, p. 33.
> [884] Willelmi Gemmetencis Historiæ (Duchesne, 1619), Liber VIII, VIII, p. 296.
> [885] Actes Henri II, Tome II, DCCXLIV, p. 375.
> [886] Willelmi Gemmetencis Historiæ (Duchesne, 1619), Liber VIII, VIII, p. 296.
> [887] Orderic Vitalis (Prévost), Vol. IV, Liber XII, III, p. 317.
> [888] Orderic Vitalis (Prévost), Vol. IV, Liber XII, III, p. 318.
> [889] Actes Henri II, Tome II, DCXXXVI, p. 246.
> [890] Actes Henri II, Tome II, DCCLXVIII, p. 421.
> [891] Orderic Vitalis (Prévost), Vol. IV, Liber XII, III, p. 317.
> [892] Willelmi Gemmetencis Historiæ (Duchesne, 1619), Liber VIII, VIII, p. 296.
> [893] Orderic Vitalis (Prévost), Vol. IV, Liber XII, III, p. 318.
> [894] Orderic Vitalis (Chibnall), Vol. VI, Book XII, p. 193.
> [895] Pipe Roll 31 Hen I (1129/30), Leicestershire, p. 87.
> [896] Dugdale Monasticon VI.2, Hospital of St Leonard, York VII, p. 609.
> [897] Dugdale Monasticon I, Whitby Monastery, Northumberland XL, p. 420.
> [898] Annales de Bermundeseia, p. 431.
> [899] Orderic Vitalis (Prévost), Vol. IV, Liber XII, III, p. 317.
> [900] Matthew Paris Vol. VI, 22, p. 36.
> [901] Gurney (1845), pp. 123-4, quoting Cartulary of Saint-Sauveur, in the possession of M. de Gerville de Valognes.
> [902] Esserent Saint-Leu, XLVI, p. 48.
> [903] Lannoy, Tome X, XIV, p. 639.
> [904] Gurney (1845), p. 35, quoting History of the Abbey of St Ouen at Rouen, p. 463.
> [905] Gurney (1845), pp. 111-2, quoting Cartulary of the priory of Clairruissel, Archives of Rouen.
> [906] Red Book Exchequer, Part II, Infeudationes militum…duci Normanniæ…1172, p. 628.
> [907] Gurney (1858), Supplement, 23, p. 737.

Note the reference numbers in the body text use a different numbering scheme [875]–[907] than the inline references [457] etc. that appeared in the per-child section. The discrepancy reflects FMG's internal cross-reference structure where the Amicie/Talbot subsection uses one block of references and the broader "SEIGNEURS de GOURNAY" section uses another.

#### 8.3.4 FS structured-field contributor notes (verbatim, for FS-tree-noise documentation)

These short contributor notes from FS PDF pp. 8, 10–11, 16, 18–19 are reproduced verbatim because they document the *kind* of unsourced material the FS Family Tree carries, useful for calibrating future passes:

> Title: My 27th Great Grandfather
> My 27th Great Grandfather

> Title: M E Sorley: The Sorley Pedigrees P. 27
> M E Sorley: The Sorley Pedigrees P. 27
> M L Call: The Royal Ancestry Bible Vol 3: 2585

> Title: Teresa Burden made note of this
> none

> Title: !Brown book 5, P C 251. Died a Monk. Mar
> !Brown book 5, P C 251. Died a Monk. Married 1st & had 2 sons. Married 2nd and had 1 daughter.

> Title: !Information from United Ancestries
> !Information from United Ancestries

For Basilia specifically:

> Title: She is the wife to William the 1st
> Her name is also known as Matilda of Flanders

> Title: My 27th Great Grandmother
> My 27th Great Grandmother

> Title: FTM disc 1 Tree # 0986
> FTM disc 1 Tree # 0986

> Title: Source: Kraentzler 1353, 1371.
> [no body — title-only]

> Title: record altered
> record altered

> Title: M E Sorley: The Sorley Pedigrees P. 15
> M E Sorley: The Sorley Pedigrees P. 15

> Title: Line in Record @I04489@ (RIN 14103) from
> Line in Record @I04489@ (RIN 14103) from GEDCOM file not recognized: BAPM

> Title: !LDS Computer Library
> !LDS Computer Library

> Title: !GENERAL:Pedigree Resource File CD 4, Pe
> !GENERAL:Pedigree Resource File CD 4, Pedigree Resource File CD 4, (Salt Lake City, UT: Intellectual Reserve, Inc., 1999) !GENERAL:Pedigree Resource File CD 4, Pedigree Resource File CD 4, (Salt Lake City, UT: Intellectual Reserve, Inc., 1999)

> Title: PED OF AUGUSTINE H. AYERS
> PED OF AUGUSTINE H. AYERS

> Title: Note: !dau of Gerard de Fleitell; same a
> Note: !dau of Gerard de Fleitell; same as Gerald Flaitel?

> Title: !Name,Spouse,Son-IGI of son Name,BD(1018
> !Name,Spouse,Son-IGI of son Name,BD(1018),Bpla co,parents,Bap-IGI Name,Bd(1053),Bplco,SP-IGI addendum from Gs 1063701 Name,Spouse,dd,Children,father,End-TIB FHL 884562(Mrs) Bd also listed as 1046,1019,1016,1082,1012;Bpla as Battlesdon,Bed from Gs 451143; Of Wormingay, Norf;Essex;Normandy;Md as <1103;Mpl as <Worminggay,Norf

> Title: !Royal Ancestors !Complete Peerage
> !Royal Ancestors !Complete Peerage

> Title: !Brown book 5, P C 274 & 318.
> !Brown book 5, P C 274 & 318.

> Title: From Ancestral File (TM), data as of 2 J
> From Ancestral File (TM), data as of 2 January 1996.From Ancestral File (TM), data as of 2 January 1996.

The note "She is the wife to William the 1st / Her name is also known as Matilda of Flanders" is particularly egregious — a contributor has literally confused Basilia Flaitel with Queen Matilda of Flanders. The "FTM disc 1 Tree # 0986", "Pedigree Resource File CD 4", "FHL 884562" pattern documents that the FS tree at this PID has accumulated material from at least three different LDS-genealogy data sources of varying quality.

#### 8.3.5 Pattou page 2 — full Hugues III chart entry verbatim (French) with translation

See §8.2 item 8 above for the full quoted Pattou entry on Hugues III with translation.

The accompanying chart annotations on the same page:
> *"Hugues III, seigneur de Gournay conquiert quelques terres (24 villages dits «Les Conquets») en Beauvaisis en 1078 (proches de Gerberoy)"*

Translation: *"Hugues III, lord of Gournay, conquers some lands (24 villages called 'Les Conquets') in Beauvaisis in 1078 (near Gerberoy)."*

> *"Domesday Book (1084): «XLVII. — Terra Hugonis de Gurnay, hundredum de Hidnigaforda. hundredum de Tendring. hundredum de Lessendena.»"*

Translation: *"Domesday Book (1084): 'XLVII. — Land of Hugues de Gournay, hundred of Hinckford [Hidnigaforda], hundred of Tendring, hundred of Lexden [Lessendena].'"*

The three Essex hundreds match Liston (Hinckford hundred), Ardleigh (Tendring hundred), Fordham (Lexden hundred) — providing the precise Domesday administrative context.

(Note: Pattou writes "Domesday Book (1084)" — actual Domesday is 1086. The 1084 date may reflect the start of survey commissioning in 1085 or a typo.)

#### 8.3.6 Pattou page 18 — "Non connectés" / unconnected Gournay figures (full)

> *"? Amicie de Gournay ° ~1023 + 1075 ép. Rigobert de Saint-Saëns, chevalier ° 998 + 1054"*

Translation: *"? Amicie de Gournay, born ~1023, died 1075, married Rigobert de Saint-Saëns, knight, born 998, died 1054."*

This Amicie is **NOT** the same as the Amicie / Talbot of FMG. This is a separate earlier "? Amicie de Gournay" who married into the Saint-Saëns family. (Saint-Saëns is a town in the Pays de Bray, between Rouen and Gournay.) Pattou's `?` flags her as an unconnected Gournay; the dates suggest she would be a daughter of Hugues II generation if the Gournay attribution is correct.

> *"? Edwige de Gournay ° ~1049 + 1098 ép. Hédouin de Gerberoy [in red text], chevalier, seigneur de Gerberoy et Martincourt, croisé (1096) ° 1045 + 1108"*

Translation: *"? Edwige de Gournay, born ~1049, died 1098, married Hédouin de Gerberoy, knight, lord of Gerberoy and Martincourt, crusader (1096), born 1045, died 1108."*

This is the historical Edwige. The husband's name "Hédouin de Gerberoy" appears in **red** in Pattou's chart — Pattou's hypothesis-tagging color. He is identified as crusader (1096, the First Crusade — same expedition as Gerard de Gournay). The Edwige PID in the FS tree is `GKWN-3GT` (per the G33 export structured field).

> *"alternative à la p.13 [in blue header]: ? Renaud (Reginald) de Gournay ép. Joan"*
> *"Anselme (Ansel) de Gournay + 1286 ép. 1246 Sibylle de Vivonne + après 15/07/1269 (fille d'Hugues et de Mabel Malet)"*
> *"Jeanne de Gournay ° ~1252 + ~1321 ép. ~1268 Pierre des Quesnes ° ~1245 + ~1312"*

Translation of the blue header: *"alternative to p. 13"*. The "alternative" is that Anselme de Gournay (the Somerset cadet) — shown on p. 13 as son of Robert de Gournay + Hawise de Longchamp — might instead be son of a **"? Renaud (Reginald) de Gournay ép. Joan"** (a different Renaud, late-13th-century not 10th-century, with English wife "Joan"). This is a competing hypothesis Pattou records but does not endorse. Worth noting because the existing repo G27 / G26 area (Sir John, Sir William III) references Anselmes that may overlap.

#### 8.3.7 Wikipedia (en) — William de Warenne, 1st Earl of Surrey — relevant excerpt

Reproduced verbatim from FS PDF p. 8:

> William de Warenne, 1st Earl of Surrey, Lord of Lewes, Seigneur de Varennes (died 1088), was a Norman nobleman created Earl of Surrey under William II Rufus. He is among the few known from documents to have fought under William the Conqueror at the Battle of Hastings in 1066. At the time of the Domesday Survey in 1086, he held extensive lands in 13 counties, including the Rape of Lewes, a tract now divided between the ceremonial counties of East Sussex and West Sussex.

And the family / issue section (FS PDF p. 10):

> Family
> William de Warenne married first, before 1070, Gundred, Countess of Surrey,[29][30] sister of Gerbod the Fleming, 1st Earl of Chester.[31]
> William married secondly a sister of Richard Gouet, who survived him.[32]
>
> Issue
> By Gundred, William had:
> William de Warenne, 2nd Earl of Surrey (died 1138), who married Elisabeth (Isabelle) de Vermandois, widow of Robert de Beaumont, 1st Earl of Leicester[33]
> Edith de Warenne, who married first Gerard de Gournay, lord of Gournay-en-Bray, and then Drew de Monchy[34]
> Reynold de Warenne, who inherited lands from his mother in Flanders[34] and died c. 1106–1108[35]
> A daughter of unknown name, who married Ernise de Coulonces.[36]
> He had no issue by his second wife.

**Note**: modern Wikipedia identifies Gundred as "sister of Gerbod the Fleming, 1st Earl of Chester," **not** as a daughter of William the Conqueror. This is the modern scholarly view (the older Conqueror-descent claim has been substantially abandoned). Pattou retains the older view via the annotation "Hugues IV de Gournay est le neveu du Roi Henry 1er d'Angleterre" through Edith. The repo's G32 fact sheet should be updated to reflect modern consensus.

---

## 9. First Bucket B Collaborative Pass — 2026-05-06

### 9.1 Geni Hugh III profile (URL #1, moved Bucket B → A)

URL: https://www.geni.com/people/Hugues-de-Gournay-III/6000000000154070463

Substantial yield. The Geni profile aggregates four distinct narrative blocks plus a Find-a-Grave entry plus the FMG MedLands transcript. Several net-new claims, several confirmations, and several FS-tree-style noise items.

#### 9.1.1 Net-new claims worth investigation

1. **Basilia's mother named "Herleve d'EVEREAUX"** — i.e., Herleva of Évreux. This is a NEW maternal-line claim:
   > "Basilia was the daughter of Gerald FLEITEL and Herleve d'EVEREAUX and widow of Raoul de GACE (b abt 1000), one of the tutors of Duke William in his youth"

   FMG names Gerard Flaitel's wife only as "---" (unknown). The "Herleve d'Évreux" attribution would make Basilia's grandfather Robert, Count of Évreux (Archbishop of Rouen, son of Richard I of Normandy) — i.e., Basilia would be a great-granddaughter of Richard I and a first cousin once removed of Duke William the Conqueror. **This is a major collateral elevation.** Not in FMG, not in Pattou, not in DG. **Treat as candidate, do not adopt without primary citation.**

   Consistent with this claim, the same Geni narrative says Raoul de Gacé (Basilia's first husband) was "one of the tutors of Duke William in his youth" — Raoul de Gacé is historically attested as William's guardian/tutor c. 1037–1040, so the chronological window is plausible.

2. **Death dates: 1110 (per the Mellcene Smith narrative)** — matches Richardson's TNG entry (which §2.3 of this assessment had flagged as outlier vs. FMG's [1093]):
   > "He died 1110 and was buried by the side of Basilia."

   Two independent sources now give 1110: (a) Richardson via TNG's `our-royal-titled-noble-and-commoner-ancestors.com/p197.htm`; (b) Mellcene Thurman Smith, *Kin of* p. 469 (cited in the Geni profile). **The 1110 date is no longer a single-source outlier.** Resolution still requires a primary source — Anselm's letter to Basilia "after 1093" is the soft constraint; if Hugh died 1110 he survived until 17 years after Anselm became Archbishop of Canterbury (1093), which is internally consistent. Both 1093 and 1110 are now defensible scholarly positions.

3. **Three-children claim from the Mellcene Smith narrative**:
   > "They had Raoul, Gerard and Basilia."

   Names two children unattested elsewhere: **Raoul** (a son named for Basilia's first husband) and **Basilia** (a daughter named for the mother). Plus Gerard (the documented heir). FMG names only Guillaume / Gerard / Hawise (latter two bracketed). **Smith's "Raoul, Gerard and Basilia" is novel.** Plausible as a pious Norman naming pattern (named for first-husband and for mother) but unattested in primary sources. Treat as candidate.

4. **Find-a-Grave entry — birth 1030, death 18 Oct 1101**:
   > "Birth 1030 Gournay-en-Bray, Departement de la Seine-Maritime, Haute-Normandie, France"
   > "Death 18 Oct 1101 (aged 70–71) Le Bec-Hellouin, Departement de l'Eure, Haute-Normandie, France"
   > "Burial Bec Abbey"
   > "Memorial ID 99917539"

   The 1030 birth matches Pattou's "° ~1030." The 18 Oct 1101 death matches Pattou's "(une source anglaise donne 18/10/1101)" — i.e., this Find-a-Grave entry is the "English source" Pattou himself referenced. So the 18/10/1101 date traces to Find-a-Grave Memorial 99917539 and back through whatever its contributor cited.

5. **The 1080 retirement-to-Bec date** (Mellcene Smith narrative):
   > "In 1080 he and his wife quit Gournay, took the habit of St. Benoit, and with two sisters of Basilia entered the Abbey of Bec."

   Earlier than the c. 1082 / pre-1093 dates. Specifies "two sisters of Basilia" entered Bec with them — plausibly identifying Agnes (m. Walter Giffard) and the unnamed Pattou-claimed Anselme de Ribemont sister. Also explicit: "took the habit of St. Benoit" — i.e., Benedictine habit.

6. **Hugues built a hermitage in the forest before becoming Prior of Saint-Nicaise de Meulan** (Mellcene Smith):
   > "In their old age Basilia died and then Hugues built himself a hut deep in the forest until the Abbe ordained his obedience to leave his hermitage and become Prior of the monastery of St. Nicaise de Meulan. The monk Hugues bowed his head and went."

   This is a vivid hagiographic detail. Pattou asserts the Prior of Saint-Nicaise de Meulan claim; Pettigrew is cautious. Smith's narrative is the most detailed account but is third-hand. **The "hermitage in the forest" detail is novel and worth tracking down to its primary source.**

7. **R.B. Stewart "My Lines" curio** — Stewart's TNG entry includes the cryptic line:
   > "Inexplicably, Hugh I was the son of Hugh II."

   This sentence reads as a numbering joke or self-deprecating note about the contradictory generational labels in 19th-century sources. Not adoptable as content; useful as a marker of Stewart's self-awareness about the numbering chaos.

#### 9.1.2 Specific FS-tree noise items in the Geni profile

- **"Basilia (b abt 1025 Linton Herfordshire)"** — "Linton, Herefordshire" as Basilia's birthplace. There is no documentary basis for this. Linton is a small Herefordshire village. This is the kind of community-tree confabulation the FS-tree carries; do not adopt.
- The R.B. Stewart entry gives Basilia three children "Raoul, Gerard and Basilia" but the Stewart entry header says "by Mellcene Thurman Smith, page 469" — i.e., the source is Smith's *Kin of* compilation, a 20th-century descendant pedigree. Smith's source for "Raoul" and "Basilia" as children is unstated.
- The Geni profile lists three children with the heading "Children of Hugh and Basilia": **9a William, 10 Gerald, 11 Julia Adela**. The "Julia Adela" is novel and possibly identifies the same person as Pattou's bracketed "Adélaïde de Gournay" or Mellcene Smith's "Basilia" daughter. Multiple confabulations chasing the same hypothetical child.

#### 9.1.3 Confirmations from the Geni profile

- **1077 charter for St Stephens at Caen** (not 1067) — matches Richardson SGM 2003: "In 1077, he witnessed the foundation charter of the monastery of St. Stephens at Caen by King William the Conqueror."
- **1082 charter for Holy Trinity Caen** — matches FMG.
- **Letter from Anselm to Basilia preserved** — matches FMG [928].
- **Both buried at Abbey of Bec** — matches FMG / Chronicon Beccensis.

#### 9.1.4 Verbatim Geni content (key passages reproduced for fidelity)

The Mellcene Smith narrative on the monastic retirement (verbatim):

> Hugues II married Basilia, or Basille, daughter of Gerard de Flaitel and his wife, who was the daughter of Robert, Count of Evereux, who was son of Richard I, Duke of Normandy. Hugues II took part in the foundation of St. Etienne (Stephen) at Caen, established by William the Conqueror at his marriage to Matilda of Flanders. Hugues had been at Hastings in 1066. In 1080 he and his wife quit Gournay, took the habit of St. Benoit, and with two sisters of Basilia entered the Abbey of Bec. In their old age Basilia died and then Hugues built himself a hut deep in the forest until the Abbe ordained his obedience to leave his hermitage and become Prior of the monastery of St. Nicaise de Meulan. The monk Hugues bowed his head and went. He died 1110 and was buried by the side of Basilia. They had Raoul, Gerard and Basilia.
>
> (Kin of Mellcene Thurman Smith, page 469)

The Find-a-Grave entry for Memorial 99917539 (verbatim):

> Hugues III de Gournay
> Birth 1030 Gournay-en-Bray, Departement de la Seine-Maritime, Haute-Normandie, France
> Death 18 Oct 1101 (aged 70–71) Le Bec-Hellouin, Departement de l'Eure, Haute-Normandie, France
> Burial Bec Abbey, Le Bec-Hellouin, Departement de l'Eure, Haute-Normandie, France
> Memorial ID 99917539
>
> Hugh de Gournay was a man of high military renown and was very likely at the battle of Hastings since he was given lands by William the Conqueror. Some of these lands were the manors of Liston, Fordham, and Ardley in Essex, all of which appear in the Domesday Survey.
>
> He married Basile Flaitel, widow of Raoul de Gace, Constable of Normandy, and daughter of Gerard Flaitel. Her maritagium was the castle of Ecouche, near Falaise in Normandy. They had two sons, Gerard and Hugh. In 1077, he witnessed the foundation charter of the monastery of St. Stephens at Caen by King William the Conqueror and in 1082 the foundation charter of the nunnery of Holy Trinity Caen by King William the Conqueror and his wife, Queen Maud. Hugh and his wife, Basile, retired to the Abbey of Bec in France c. 1082 with her niece, Ansfride. They were still living c. 1093, when St. Anselm was consecrated Archbishop of Canterbury. A letter from Anselm to Basile has been preserved. Both are buried at the Abbey of Bec.

The R.B. Stewart "My Lines" entry (verbatim, with Stewart's compiler attribution):

> Hugh de Gournay was a man of high military renown. He married Basilia Flatel, and was very likely at the battle of Hastings since he was given lands by William the Conqueror. Some of these lands were the manors of Liston, Fordham, and Ardley in Essex, all of which appear in the Domesday Survey. [Morants's Essex, vol. ii p.31; Domesday, vol. ii. p. 89]. Afterwards, considerable estates in England were either given to the Gourney family or were acquired by marriage. Hugh de Gournay became a monk at Bec before 1093. ~ The Record of the House of Gournay, p. 16, 22
>
> From Gen-Medieval Archives. 193
> From: royalancestryATmsn.com (Douglas Richardson)
> Subject: Gournay Family Pedigree
> Date: 19 Jan 2003 17:36:28 -0800
>
> Hugh de Gournay, seigneur of Gournay-en-Brie, Normandy, Domesday tenant of Liston, Ardley, and Fordham, Essex, son and heir. He married Basile Flaitel, widow of Raoul de Gace, Constable of Normandy, and daughter of Gerard Flaitel. Her maritagium was the castle of Ecouche, near Falaise in Normandy. They had two sons, Gerard and Hugh. In 1077, he witnessed the foundation charter of the monastery of St. Stephens at Caen by King William the Conqueror and in 1082 the foundation charter of the nunnery of Holy Trinity Caen by King William the Conqueror and his wife, Queen Maud. Hugh and his wife, Basile, retired to the Abbey of Bec in France c. 1082 with her niece, Ansfride. They were still living c. 1093, when St. Anselm was consecrated Archbishop of Canterbury. A letter from Anselm to Basile has been preserved. He predeceased his wife. Both are buried at the Abbey of Bec.
>
> [Sources cited by the author: Daniel Gurney, Record of the House of Gournay (1948), pp. 22 (chart), 46-62; Bedfordshire Historical Record Society 7 (1922): 153-157; 19 (1937): charts fol. pg. 99. Oxfordshire Record Society 7 (1925): 7-15. Paget (1957), 266: 1-4 (sub Gurnay).]

The Compiler attribution: *R. B. Stewart, Evans, GA*, at `http://homepages.rootsweb.ancestry.com/~cousin/html/p353.htm#i19730`.

The R Green ChildrenList (verbatim):
> Children of Hugh and Basilia
> 9a......William dob unknown William witnessed the charter dated 1082 under which William I King of England donated property to the abbey of la TrinitŽ de Caen
> 10......Gerald b abt 1035 d 10 May 1097 Nice, Asia Minor on crusade
> 11......Julia Adela dob unknown
> http://www.rgreen.org.uk/Gournay.html#1

Note: "Gerald b abt 1035 d 10 May 1097 Nice, Asia Minor on crusade" — this conflates the elder son Gerald (G32, b. ~1043, d. after 1104 in Palestine) with the younger Gerald who died at Nicaea 1097 (the *vit. pat.* son). DG-I p. 277 distinguishes them; R Green collapses them. This is the same Gerard-father-vs-Gerard-son confusion the existing G32 research companion (line 23) flags.

### 9.2 Histoire de Lorraine (URL #4, moved Bucket B → A)

URL: https://books.google.fr/books?id=Hp9rQFd3ILgC&hl=fr&pg=RA2-PR200

The full multi-volume work has been downloaded as `sources/FS/Histoire_de_Lorraine_depuis_l_entrée_de.pdf` (116MB; gitignored due to GitHub's 100MB hard file size limit). The relevant Maison de Gournay introduction section has been extracted as committable text at `sources/FS/lorraine-maison-de-gournay-extract.txt`.

The PDF is the Calmet *Histoire ecclésiastique et civile de Lorraine*, with the Maison de Gournay genealogy in the introductory matter (volume V or appendix). The genealogy is signed by **M. Palain de Mongnigny**.

#### 9.2.1 The Lorraine Gournay genealogy — opening

Verbatim French (from `lorraine-maison-de-gournay-extract.txt`, with normalized OCR spelling where the long-s "f" was misread):

> *"Généalogie de la Maison de Gournay ou Gronaix.*
>
> *Par M. Palain de Mongnigny.*
>
> *La Maison de Gournay porte de gueules à trois tours d'argent, maçonnées de sable, posées en bande. Cimier un Croissant d'or, supporté d'un Anneau de gueules, et surmonté d'une queue de Paon au naturel.*
>
> *Cette Maison est une des plus anciennes de la Ville de Metz, où elle a rempli les premières dignités militaires et civiles ; et dans le temps que cet État était régi par ses propres Loix, ou gouverné sous l'autorité des Empereurs, la Maison de Gournay a eu la meilleure part dans l'administration de la Justice, et dans la conduite des Armées; deux fonctions qu'attiroit après soi la dignité de Maître-Échevin de Metz."*

Translation:

> *Genealogy of the House of Gournay or Gronaix.*
>
> *By M. Palain de Mongnigny.*
>
> *The House of Gournay bears: gules, three towers of silver, masoned of sable, set in bend. Crest: a crescent of gold, supported by a ring of gules, and surmounted by a peacock's tail in natural colours.*
>
> *This House is one of the most ancient of the City of Metz, where it has filled the first military and civil dignities; and during the time when this State was governed by its own Laws, or under the authority of the Emperors, the House of Gournay had the greatest share in the administration of Justice and in the conduct of Armies; two functions that the dignity of Maître-Échevin [chief magistrate] of Metz brought with it.*

**This is a different Gournay family** — the **Metz / Lorraine Gournays** — with **different arms** (three silver towers on red, not the engrailed cross of the Norman Gournays or the plain sable of the Norman origin). Their genealogy claims descent from the Norman Gournays of Bray via a "Vuldus de Gournay" who left Metz c. 960 to serve William the Conqueror.

#### 9.2.2 The Vuldus origin claim and Hugues "Comte de Gournay"

> *"Vuldus de Gournay partit de Metz vers l'an 960. pour aller trouver Guillaume le Conquérant, qu'il servit avec tant de courage et de fidélité, qu'il en reçut pour récompense la Ville de Gournay en Normandie, avec dix-huit Villages pour lui et Hugues de Gournay, son fils, qui suit."*

Translation:
> *"Vuldus de Gournay left Metz around the year 960 to go find William the Conqueror, whom he served with such courage and fidelity that he received as reward the Town of Gournay in Normandy, with eighteen villages for himself and Hugues de Gournay, his son, who follows."*

**Anachronism**: William the Conqueror was born c. 1028 — there was no "William the Conqueror" in 960. This is either a Lorraine-family confabulation of a prestigious Norman descent, or a confusion with William Longsword (d. 942) or Richard I (d. 996). The Lorraine source's foundation story is **chronologically broken** at its starting point. **Do not adopt the Vuldus claim.** But: it is interesting evidence of a Metz family asserting Norman Gournay ancestry in the 17th century.

> *"Hugues de Gournay, premier Chef et Commandant l'Armée Navale de Guillaume, le Conquérant, contre Conrade Roi de Norveck en 1074. s'acquitta si dignement de cette charge, que Guillaume lui donna l'Évêché entier de Norveck, où il fonda la Collégiale de S. Hildebert de Gournay. Ce Hugues, Comte de Gournay, épousa Basile de Flatelly, Comtesse de Varenne et de Sury en Angleterre, dont il eut Gerard de Gournay…"*

Translation:
> *"Hugues de Gournay, first Chief and Commander of the Naval Army of William the Conqueror, against Conrad King of Norveck in 1074, acquitted himself so worthily of this charge that William gave him the entire Bishopric of Norveck, where he founded the Collegiate Church of St. Hildebert of Gournay. This Hugues, Count of Gournay, married Basile de Flatelly, Countess of Varenne and Surrey in England, of whom he had Gerard de Gournay…"*

**Several material findings packed into this passage**:
1. **"Conrade Roi de Norveck en 1074"** = Conrad King of Norwich/Norfolk in 1074 — **the Lorraine source explicitly identifies the 1074 conflict as being against a "Norveck" figure**, supporting the DG hypothesis that the "Cardiff" tradition is a corruption of "Norvic / Norwich / Norfolk." There was no King Conrad of Norwich in 1074, but there was a 1075 East Anglian rebellion (Earl Ralph de Gaël) involving Danish reinforcements; the Lorraine source has garbled this into "Conrad King of Norveck." This is the same kind of garbling FMG flags about "Canut roi de Norvège," but with a different proper-noun corruption pattern ("Conrad" instead of "Canut", "Norveck" instead of "Norvège").
2. **"Comte de Gournay"** — the Lorraine source elevates Hugues to Count, not just Lord/Sieur. (FMG and Pattou treat him as Seigneur.)
3. **"Bishopric of Norveck" granted by William** — historically impossible (William did not grant bishoprics to laymen as fiefs); this is more confabulation, possibly a confused recollection of the Norfolk fiefs Hugh actually received.
4. **"Collégiale de S. Hildebert de Gournay"** — the **Saint-Hildevert collegiate church at Gournay-en-Bray** is a real church, traditionally associated with the Hugh-the-Fortifier of an earlier generation (G36 in the repo) — see DG-Supp Note 7. The Lorraine source attributes the foundation to *this* Hugues (the Conqueror-era one). Either a different Hildevert church or a confused attribution.
5. **"Basile de Flatelly, Comtesse de Varenne et de Sury en Angleterre"** — the Lorraine source **conflates Basilia (Hugh's wife) with Edith de Warenne (Hugh's daughter-in-law)**, treating her as Countess of Warren and Surrey. This is a clear genealogical confusion — Basilia was a Norman of the Flaitel family; Edith was the Warenne. The Lorraine source has merged two generations of women into one.
6. The "Bacoloin" abbey to which Gerard gave benefactions (in the next-generation paragraph) is almost certainly **Bec** (Bec-Hellouin) — the Lorraine source's spelling.

#### 9.2.3 The Lorraine source on Hugues II (= repo's Hugh IV)

> *"Hugues de Gournay II du nom, épousa la sœur de Rodolphe de Péronne, Comte de Vermandois, Princesse du sang Royal, fille de Hugues de France, dit le Grand, Comte de Vermandois, frere du Roi Philippe I. dont il eut Thiedric de Gournay…"*

Translation:
> *"Hugues de Gournay II of the name married the sister of Rodolphe de Péronne, Count of Vermandois, Princess of the Royal blood, daughter of Hugues of France called 'le Grand', Count of Vermandois, brother of King Philippe I, of whom he had Thiedric de Gournay…"*

The Lorraine source's "Hugues II" is the repo's **Hugues IV** (the one who married Beatrice de Vermandois, daughter of Hugues le Grand). The Vermandois marriage matches Richardson and Pattou. The Lorraine source's numbering scheme:
- Lorraine "Hugues I" = repo's Hugh III (the Conqueror-era figure, married Basile)
- Lorraine "Hugues II" = repo's Hugh IV (married Vermandois)

**Yet a third numbering scheme** — Pattou uses III and IV for the same two men; FMG uses [III] and [IV] with brackets. The Lorraine source's I/II scheme runs the documented Norman line from the Conqueror generation forward without numbering the three earlier (uncertain) generations.

#### 9.2.4 Lorraine source structural finding — Thiedric de Gournay as Metz progenitor

> *"Thiedric de Gournay, l'un des vingt- un Échevins nobles d'Etienne de Bar, Évêque de Metz. Il vivoit en 1106. et épousa N…. Il eut pour fils Nicolas de Gournay, dit le Viel, Maître Échevin de la Ville de Metz en 1230."*

Translation:
> *"Thiedric de Gournay, one of the twenty-one noble Échevins of Étienne de Bar, Bishop of Metz. He was living in 1106 and married [name unknown]. He had as son Nicolas de Gournay, called 'the Old', Maître-Échevin of the City of Metz in 1230."*

The Lorraine source claims **Thiedric de Gournay** (active 1106 in Metz under Bishop Étienne de Bar) was the founder of the Metz Gournay line. He is presented as son of "Hugues II" (= repo's Hugh IV) and the Vermandois Princess. FMG and Richardson do not list a Thiedric among Hugues IV's children (they list only the children of his second marriage to Mélisende de Coucy: Gérard and Hugues). **The Thiedric attribution is a Lorraine-family claim of Norman descent that lacks corroboration in the Norman-side sources.**

The Metz line then runs: Thiedric (1106) → Nicolas "le Viel" (1230) → Jacques (1285) → Nicolas II "le Géant" (1270) → Poince/Pierre des Changes (1290) → Baudouin → Poince II "l'Aveugle" (1348) → multiple generations through to 17th-century descendants. **None of this affects the repo's direct line** but documents that a 17th-century Metz family (the Lorraine Gournays / Gronaix) actively claimed Norman descent. **Worth flagging as a potential namesake-confusion source for any future Metz-area research.**

#### 9.2.5 What the Lorraine source DOES NOT contradict the repo on

- The Vermandois marriage of Hugues IV (matches Richardson, Pattou).
- The general post-Conquest reward narrative (Gournay rewarded with lands).
- The Bec abbey association (with the spelling "Bacoloin").

#### 9.2.6 Bottom line on the Lorraine source

The Calmet / Palain de Mongnigny *Maison de Gournay* genealogy is a **17th-century Metz family genealogy** (signed 1674 per the text reference: *"Jugement qui a été imprimé et rendu à Metz le II. Août 1674. par M. Poncet de la Riviere"*) claiming Norman descent. It contains:
- **One materially useful corroboration**: the "Norveck" (Norwich) identification supporting the DG hypothesis that the 1074 Cardiff tradition is a name corruption.
- **Several confused conflations**: Basilia confused with Edith de Warenne; Hugues "Comte" elevated above his actual rank; "Bishopric of Norveck" anachronism.
- **A complete Metz-line genealogy** that the repo has no need to adopt but should be aware of as a parallel "Gournay" family.

**Action**: do not adopt any Lorraine-source claim as a fact for the repo's direct-line ancestors. Use only as supporting evidence for the Norwich-corruption hypothesis and as documentation of a parallel Metz family.




