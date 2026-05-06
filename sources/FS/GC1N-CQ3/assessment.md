# G35 — FamilySearch Intake Assessment (Renaud de Gournay, GC1N-CQ3)

**Source artifact**: `sources/FS/20260506FamilyGC1N-CQ3.pdf` (7 pp., printed 6 May 2026)
**Companion artifacts**: shared with G33 — `sources/FS/MZ68-VKD/racineshistoire_free_fr_LGN_PDF_Gournay.pdf` (Pattou). Pattou p. 2 covers Renaud's generation.
**Subject FS PID**: GC1N-CQ3
**Repo target**: G35 (`research/people/g35-renaud-de-gournay-fact-sheet.research.md`, `fact-sheets/g35-renaud-de-gournay-fact-sheet.md`)
**Assessment date**: 2026-05-06
**Disposition**: Phase-0 review per `.claude/skills/familysearch-export-review/SKILL.md`. Precursor to a Phase-1 intake patchset.

---

## 1. Source-format anatomy

7-page Family Group Record. Three layers:
- **Structured FGR** (pp. 1–2): husband Renaud de Gournay (GC1N-CQ3, b. 0961, d. 1022), wife **Albérade de Montdidier (G8C3-VY8)** with detailed dates (b. about 0971 Saint-Riquier Somme Picardie, d. 1029 Gournay-en-Bray), 5 children listed: Nocher (G5KJ-XTT), Blanche (GR62-DVF), **Hugues de Gournay II (LVSH-KBM)**, Gauthier de Gournay (GKWN-ZD1), Alix de Gournay (G5KJ-XTY).
- **Sources** (pp. 3–6): the FMG MedLands entry for Renaud is short and reproduced verbatim on p. 3; Pattou referenced via FS Memories ID 203028445; Geneanet Foullon for Nocher; "Legacy NFS Source" pasted note.
- **Notes** (pp. 4–6): one striking note about Gauthier — *"There is no evidence that Gauthier de la Ferté married Isabelle de Ponthieu… In Racines Histoire there is no mention of anybody named Isabell de Ponthieu; There is an Elizabeth de Ponthieu born to Guillaume I, Comte de Ponthieu et Montreuil, but she became an abbess at St Austreberthe, Montreuil and never married."* This is a contributor explicitly correcting an FS-tree error — useful pattern.

**Layer peculiarity**: short export by total page count, but unusually clean — the FMG entry on Renaud is only 5 sentences and the contributor-notes layer is small. This makes the export easier to assess. The downstream Hugh II content (pp. 3–5) is duplicated from the LVSH-KBM export.

The repo's existing G35 research companion observes that Delisle could not find the original La Ferté charter in the Evreux archives (DG-Supp Note 8) — the charter's existence rests on DG's transcription of the *MS. Histoire des Seigneurs de Gournay*. **The FS export embeds the FMG citation chain that confirms this provenance limitation:**
> [884] Gurney (1845), pp. 26 and 31, citing M. de Gondeville's MS Histoire de Gournay, but adding that the original charter no longer exists.

This explicit "the original charter no longer exists" admission, embedded in MedLands references [884] and [885] (visible on FS p. 5), is **highly useful** — it converts the existing companion's open question into a documented fact: **the original 989/96 La Ferté charter has not survived; what survives is DG's transcription via the MS. Histoire de Gournay.**

---

## 2. Cross-walk: FS export vs. repo

### 2.1 Concordant facts (FS confirms repo)

- Renaud Seigneur de Gournay; wife Alberade.
- Two sons named in FMG: Hugues [I] de Gournay (older) and Gauthier de la Ferté (younger).
- Charter date 989/96 for the La Ferté priory foundation by Gauthier "at the command of his brother Hugh."
- The "command" of his brother suggests Hugues was the older son (FMG note [884]).

### 2.2 Net-new content worth promoting

1. **The Gurney 1845 / MS de Gondeville citation chain confirming the lost charter**:
   > [884] Gurney (1845), pp. 26 and 31, citing M. de Gondeville's MS Histoire de Gournay, but adding that the original charter no longer exists.
   > [885] Gurney (1845), pp. 26 and 31, citing M. de Gondeville's MS Histoire de Gournay, but adding that the original charter no longer exists.

   This **resolves Open Question #1 in the existing G35 companion** ("Charter location: Where did DG see it?"). Answer: DG saw it via M. de Gondeville's MS *Histoire de Gournay*; the original charter no longer exists. Adopt as a research-tier footnote making the provenance explicit.

2. **Pattou's structural placement of Renaud** (companion p. 2):
   > "? Renaud, seigneur de Gournay ép. Albérade [...] Gauthier de La Ferté + après 989"
   > *(Translation: "? Renaud, lord of Gournay, married Albérade [...] Gauthier de La Ferté, died after 989")*

   Note Pattou marks Renaud with `?` — Pattou treats Renaud's existence as tentative. French Wikipedia goes further: *"Renaud (douteux), épouse Albérade, vivent au milieu du xe siècle"* (*Renaud [doubtful], married Albérade, living in the middle of the 10th century*) — explicit "douteux" (doubtful) tag. This is a **scholarly downgrade** of Renaud relative to the repo's "Confirmed" classification. Repo classifies G35 as Confirmed because the la Ferté charter names him; Pattou and French Wikipedia treat the charter's authority as `?` because the original is lost.

3. **Pattou's chart structure (corrected after careful re-read with line-style attention)**: my earlier claim that "Pattou's main chart on p. 2 omits Renaud as a generation between Hugues 1er and Hugues II" was **wrong**. Pattou's actual treatment is more nuanced and uses two distinct line styles:

   - **Solid-line main chain**: Eudes → "? Hugues de Gournay" (an unnamed intermediate uncertain figure) → Hugues 1er (with wife Bathilde de Gerberoy in red, also `?`) → Hue II
   - **Dashed-line parallel chain**: Eudes → "?" (separate question mark marker) → "? Renaud, seigneur de Gournay ép. Albérade" → solid line down from Renaud to Gauthier de La Ferté

   So Pattou **does include Renaud**, but as a *parallel uncertain figure* at roughly the same horizontal level as Hugues 1er, connected to Eudes via a chain of dashed connectors rather than the main solid line. The visual encoding mirrors Pattou's narrative on the same page: *"Daniel Gurney suggère un lien familial entre les maisons de La Ferté et de Gournay. Il fait d'Hugues de Gournay un des descendants de Renaud et Aubrée (Alberade), parents du fondateur de la collégiale de La Ferté."* (Translation: *Daniel Gurney suggests a family link between the houses of La Ferté and Gournay. He makes Hugues de Gournay one of the descendants of Renaud and Aubrée [Alberade], parents of the founder of the collegiate church of La Ferté.*) — Pattou is presenting DG's chain as a hypothesis (Renaud → Hugues de Gournay) while reserving the right not to endorse it, hence the dashed lines.

   The repo's chain (G34 Hugh II ← G35 Renaud ← G36 Hugh I ← G37 Eudes) follows FMG, which keeps Renaud as the bridge. Pattou's chart includes Renaud but as a parallel-and-uncertain figure, NOT as a parallel-and-omitted figure. The structural disagreement is therefore not "Pattou omits Renaud" but rather "Pattou has more uncertainty markers around Renaud's place in the chain than FMG/repo does." Pattou's main solid chain also includes an unnamed "? Hugues de Gournay" between Eudes and Hugues 1er, which the repo does not have — that uncertain intermediate generation is the *new* structural element Pattou raises.

4. **Pattou notes the la Ferté foundation may be slightly later than the 989–996 window**: "ou cette fondation peut-être légèrement antérieure à 1026 sous Richard II ?" — i.e., possibly under Richard II (r. 996–1026), making it possibly closer to 1000–1010 than to the 989–996 window. This is a small but real chronological adjustment Pattou raises with `?`. Adopt as a research-tier note: the la Ferté charter date *range* is 989/996–c.1026, not strictly 989/996.

5. **Pattou ascribes the Sigy priory connection to Hugh III** (companion p. 2 narrative line, also confirmed by French Wikipedia): "Il établit vers 1037-1045 l'abbaye de Sigy-en-Bray, qu'il soumet à l'abbaye Saint-Ouen de Rouen." This is a *Hugh III* attribution — relevant to G33 file. Sigy-en-Bray and La Ferté-en-Bray are **different houses** with different founders, easily confused.

### 2.3 FS conflicts with repo (FS likely wrong)

| Item | FS export | Repo | FS sourced? | Disposition |
|---|---|---|---|---|
| Wife | "Albérade de Montdidier (G8C3-VY8)" with specific dates | Repo: Alberade (no surname; la Ferté charter only names "Alberade") | No (within this PDF); Pattou names her only as "Albérade" without surname | "de Montdidier" attribution unsupported. The Montdidier comital family of the Vermandois region was prominent c. 990–1010 and a marriage into Gournay would not be implausible, but no primary source attests it. Hold as candidate, do not adopt. |
| Wife's birthplace | "Saint-Riquier, Somme, Picardie, France" | Repo: not specified | No | Saint-Riquier was a Vermandois-orbit place in the late 10th century but no source ties Alberade there. Likely community-tree extrapolation from a tentative Montdidier (= Vermandois region) attribution. |
| Wife's death | "1029 Gournay-en-Bray" | Repo: not specified | No | No source. |
| Renaud's father | "Eudes ou Hugues de GOURNAY EN BRAY (PWPZ-VK1)" | Repo: G36 = Hugh I, G37 = Eudes (separate generations) | Yes (FS structured) | **Critical structural finding**: FS conflates Eudes (G37) and Hugues 1er (G36) into a single PID `PWPZ-VK1` labeled "Eudes ou Hugues" ("Eudes or Hugh"). The repo treats them as separate generations. See §3 and §6. |
| Renaud's mother | "Marthe de Foucarmont (L2TC-TFZ)" | Repo: not specified for Hugh I or Eudes | Yes (FS) | Marthe de Foucarmont is named in the PWPZ-VK1 (G36) export as wife of Eudes/Hugues. The "Foucarmont" attribution is specific (Foucarmont is a real place near Eu/Aumale, with a 12th-century abbey) and Pattou's chart p. 2 explicitly entertains this with `?`: "ép. ? (Marthe de Foucarmont ?)". Genuinely uncertain. |
| Renaud's birth | "0961" | Repo: c. 970 | No (FS) | 9-year drift; not material. |
| Renaud's death | "1022" | Repo: dates uncertain | No (FS) | No source for 1022 specifically. Pattou and FMG silent on Renaud's death year. |
| Children | Nocher, Blanche, Hugues II, Gauthier, Alix | Repo: Hugues II + Gauthier de la Ferté (per la Ferté charter) | Mixed | The la Ferté charter names *only* Hugues and Gauthier. The other three FS children (Nocher, Blanche, Alix) are FS-tree additions: |
| Child #1 Nocher de Gournay (G5KJ-XTT) b. 0987 | "Born about 0987 - Gournay-en-Bray, Deceased in 1039, aged about 52 years old" via Geneanet (foullon tree) | Not in repo, not in FMG, not in Pattou main chart | Yes (Geneanet) | Geneanet community tree only. FMG doesn't mention. Pattou doesn't mention. **Spurious or "non connecté."** |
| Child #2 Blanche de Gournay (GR62-DVF) b. 0988, m. 1005 Osmond 1er Tyrel de Poix, d. 1032 Poix-de-Picardie | Not in repo, not in FMG, not in Pattou | No (FS structured) | Spurious. The Tyrel de Poix family is real (Walter Tirel famously shot William Rufus in 1100) but no documented marriage to a Gournay daughter. |
| Child #5 Alix de Gournay (G5KJ-XTY) b. 0990, m. Eudes de Foucarmont, d. 1038 Foucarmont | Not in repo, not in FMG, **but mentioned by Pattou companion p. 2** | No (FS structured) | Pattou's chart p. 2 includes "? Alix de Gournay ép. ? Eudes de Foucarmont" with `?` — i.e., Pattou treats this as tentative. Pattou places her at the **Hugues 1er** generation (as sister of Hugues 1er), not as daughter of Renaud. FS again slides one generation. |
| Gauthier de Gournay (GKWN-ZD1) status | Listed as son of Renaud, b. after 0989 | Repo: yes, Gauthier de la Ferté is son of Renaud (la Ferté charter names him) | Yes | Concordant with the la Ferté charter. |

### 2.4 Spurious / over-claimed structured-field content

- **Albérade's "de Montdidier" surname**, birthplace, death date — community-tree extrapolation; the la Ferté charter gives only "Alberade."
- **Children Nocher and Blanche** as confirmed children of Renaud — community-tree additions with no scholarly support.
- **Alix de Gournay** as daughter of Renaud — Pattou places her one generation later (sister of Hugues 1er), not daughter of Renaud.
- **The Eudes/Hugues conflation in the father field** — fundamental structural finding; see §6.

---

## 3. FS Tree update suggestions

| FS field (PID GC1N-CQ3) | Current FS value | Suggested correction | Repo / scholarly citation |
|---|---|---|---|
| Wife | "Albérade de Montdidier (G8C3-VY8)" with detailed dates | Strip "de Montdidier" surname; strip detailed dates; keep "Albérade" as unconfirmed-family | la Ferté charter (DG / FMG [883]) names only "Alberade." |
| Renaud's birth | "0961" | "c. 960–970, dates uncertain" | No primary source for 961 specifically. |
| Renaud's death | "1022" | "dates uncertain" | No primary source. |
| Children | Nocher, Blanche, Hugues II, Gauthier, Alix | Keep only Hugues II (LVSH-KBM) and Gauthier (GKWN-ZD1). Remove Nocher and Blanche. **Move Alix up one generation** (sister of Hugues 1er, not daughter of Renaud) per Pattou. | la Ferté charter and FMG; Pattou companion p. 2. |
| Father | "Eudes ou Hugues de GOURNAY EN BRAY (PWPZ-VK1)" | Split this PID into two separate persons: Eudes (G37 territory) and Hugues 1er (G36 territory). Renaud's father should be Hugues 1er (the new G36-only PID). | Repo treats them as separate generations; FMG explicitly treats Eudes and Hugues as two generations. See §6. |

(Note: the Eudes-vs-Hugues splitting is a major FS Tree restructuring proposal; it spans the G36/G37 boundary and may need to be coordinated with the future G37 export.)

---

## 4. URL triage

### Bucket A — auto-fetched
| URL | Status | Net-new content |
|---|---|---|
| http://racineshistoire.free.fr/LGN/PDF/Gournay.pdf | already in repo (companion PDF) | Pattou marks Renaud `?`; treats him as possibly part of the chain but tentatively. |
| https://fmg.ac/Projects/MedLands/normacre.htm#_Toc108863566 | substantively embedded p. 3 | FMG entry on Renaud is short but includes the Gurney (1845) / MS de Gondeville citation chain confirming the original charter is lost. |

### Bucket B — needs human / login

| URL | Expected content | Failure mode | Suggested human action |
|---|---|---|---|
| https://gw.geneanet.org/foullon?lang=en&n=de+gournay&oc=0&p=nocher+de+gournay+en+bray | Geneanet community tree for Nocher de Gournay | Likely login wall | Browser visit; only worth opening if a primary source is cited. (Nocher is most likely a community-tree fabrication; a primary source would change that.) |
| https://www.familysearch.org/photos/artifacts/203028445 | FS Memories upload of Pattou PDF | Authenticated FS session | Skip — PDF already in `sources/FS/MZ68-VKD/`. |

### Bucket C — redundant / low-value
| URL | Reason for skip |
|---|---|
| http://familysearch.org/patron/source/photoId/203028445 | Same FS Memories link. |
| http://www.lewisfamilytree.com/... (referenced via G33 export) | Generic TNG site, low-value. |

---

## 5. Patchset readiness sketch

**Probable adopt** (research companion edits):
1. Add the **Gurney (1845) / MS de Gondeville citation chain** as a research-tier footnote making the la Ferté charter provenance explicit — "the original charter no longer exists" (FMG [884]/[885]). Resolves Open Question #1 in the existing companion.
2. Add **Pattou's date-range adjustment** (la Ferté foundation possibly under Richard II r. 996–1026) as a research-tier "date may be slightly later" note.
3. **Open a structural-conflict note** in the G35/G36 research companions surfacing the FMG-vs-Pattou disagreement on whether Renaud is a generation between Hugues 1er and Hugues II (FMG) or above Hugues 1er (Pattou). The repo follows FMG; this needs to be a documented, conscious choice.
4. **Forward Alix de Gournay m. Eudes de Foucarmont** to G36 territory as a candidate sister of Hugues 1er (not as daughter of Renaud).
5. **Forward the Eudes/Hugues conflation** to G36/G37 pass.

**Decline / quarantine**:
- Albérade's "de Montdidier" surname and detailed dates.
- Children Nocher and Blanche.
- Alix as daughter of Renaud (move up one generation).
- The Geneanet "foullon" tree as a basis for adopting Nocher.

**`data/sources.json` bookkeeping**:
- New: `gondeville-ms-histoire-de-gournay` — the M. de Gondeville MS *Histoire de Gournay* cited via DG (1845) and FMG. Note that the original charter is lost; what we have is DG's transcription via this MS.
- Refresh or note in `daniel-gurney-1845` — Daniel Gurney, *The Record of the House of Gournay*, 1845 edition (the *first* edition / Supplement, vs. the 1848 second edition that the repo currently labels DG-I).

---

## 6. Open items still requiring human judgment

1. **The Eudes / Hugues 1er conflation**: FS PID `PWPZ-VK1` is labeled "Eudes ou Hugues de GOURNAY EN BRAY" — i.e., FS treats the two as a single uncertain person. The repo treats them as separate generations (G37 = Eudes, G36 = Hugues 1er). Pattou's chart p. 2 places them as separate generations too: "? Eudes (de Gournay)…" → blank → "? Hugues de Gournay" → "Hugues 1er de Gournay." But Pattou's structure has Hugues 1er as "vivant en 984" — i.e., an early adult contemporary with Renaud's la Ferté charter, not a generation earlier. **The chronological arithmetic on this question is the key open item for the G35–G37 stretch.**
2. **Pattou's `?` on Renaud's existence**: French Wikipedia goes further with "douteux." The repo classifies G35 as "Confirmed." Resolution: the la Ferté charter (cited via DG via Gondeville MS, original lost) is the only primary attestation, and FS / Pattou / French Wikipedia all treat it more cautiously than the repo. The repo's "Confirmed" classification should be reviewed.
3. **The la Ferté foundation date**: 989/96 vs. possibly 1000–1026 under Richard II per Pattou's `?`. The witnesses Richard I + Richard II + Robert Archbishop of Rouen would technically cover the 989/96 window (Richard I died 996; Robert was Archbishop from 989). If the foundation extended into Richard II's reign, all three witnesses cannot be present together post-996 (Richard I dead). The 989/96 window is therefore tighter than Pattou's `?` suggests.
4. **The "Albérade de Montdidier" attribution**: implausible without primary support. The Montdidier comital family of Vermandois was prominent c. 990–1010, but no source ties Alberade to it. Treat as a quarantine candidate.
5. **Whether Pattou's `?` Renaud should make the repo downgrade G35 from Confirmed to Uncertain**: a meaningful editorial decision. The la Ferté charter names Renaud explicitly (per DG / FMG [883]), so "Confirmed" in the repo's sense (named in a primary document, even one preserved only in transcription) is defensible. Pattou's `?` is more cautious because the original charter is lost. Both positions are reasonable; the repo should make the choice consciously.

---

## 7. Pattou Re-Read Addendum (after careful re-read with line-style attention)

The original Pattou ingestion in §2.2 was substantially corrected in §2.2 item 3 above. This section adds the full verbatim Pattou content with translations.

### 7.1 Pattou's full chart entry on Renaud — verbatim French + English translation

(p. 2, dashed-line parallel branch off Eudes)

> *"? Renaud, seigneur de Gournay ép. Albérade"*

Translation: *"? Renaud, lord of Gournay, married Albérade"*

Bare entry; no dates. The `?` and the dashed-line connection encode Pattou's uncertainty about Renaud's place in the chain.

The accompanying Gauthier de La Ferté entry (Renaud's son):

> *"Gauthier de La Ferté + après 989 (fonde le Prieuré de La Ferté-en-Bray par charte entre 989 & 996, en présence de Richard 1er, duc de Normandie, et Robert, Archevêque de Rouen ; ou cette fondation peut-être légérement antérieure à 1026 sous Richard II ?)"*

Translation: *"Gauthier de La Ferté, died after 989 (founds the Priory of La Ferté-en-Bray by charter between 989 and 996, in the presence of Richard I, duke of Normandy, and Robert, Archbishop of Rouen; or this foundation perhaps slightly later, around 1026 under Richard II?)"*

Pattou raises the possibility the foundation is later than the canonical 989/96 window — possibly as late as 1026 under Richard II. This is a `?` hedge, not a flat claim.

### 7.2 Pattou's narrative on the DG–La Ferté–Gournay link

(p. 2 sidebar, French):

> *"Daniel Gurney suggère un lien familial entre les maisons de La Ferté et de Gournay. Il fait d'Hugues de Gournay un des descendants de Renaud et Aubrée (Alberade), parents du fondateur de la collégiale de La Ferté."*

Translation: *"Daniel Gurney suggests a family link between the houses of La Ferté and Gournay. He makes Hugues de Gournay one of the descendants of Renaud and Aubrée (Alberade), parents of the founder of the collegiate church of La Ferté."*

> *"Hugues de La Ferté (Hugone) et Hugues de Gournay sont nommés dans une charte de Philippe de Valois de 1335 comme contemporains de Guillaume, comte d'Arques + après 1052"*

Translation: *"Hugues de La Ferté (Hugone) and Hugues de Gournay are named in a charter of Philippe de Valois of 1335 as contemporaries of Guillaume, count of Arques [who died] after 1052"*

This 1335 Philippe VI charter is a 14th-century retrospective document referring back to 11th-century figures. **Worth pursuing as a primary source.** Likely lives in the Trésor des Chartes (Archives Nationales J series) or the *Actes de Philippe VI* edition.

### 7.3 Pattou's narrative on Daniel Gurney and the Delisle critique

> *"Au milieu du XIXe siècle, Daniel Gurney a établi une généalogie souvent reprise dans les ouvrages d'histoire sur la région mais ses travaux ont vite été critiqués par des érudits normands comme Léopold Delisle."*

Translation: *"In the middle of the 19th century, Daniel Gurney established a genealogy often reprinted in regional history works, but his work was quickly criticized by Norman scholars such as Léopold Delisle."*

This critique is also the direct backdrop for the existing G35 research companion's note (line 9, DG-Supp Note 8) that "M. Leopold Delisle has also examined in detail the archives at Evreux, and is quite certain this charter is not there." Delisle's critique applied at multiple levels: the la Ferté charter's archival absence is one specific instance; Pattou suggests the broader DG framework was challenged.

### 7.4 Pattou's full chart entry on the la Ferté side-line (sons of Gauthier)

(p. 2, descending from Gauthier de La Ferté)

> *"Hugues (I) de La Ferté + avant 1047 (fonde le Prieuré de Sigy par charte co-signée par Guillaume (futur Conquérant) entre 1030 & 1035)"*

Translation: *"Hugues (I) de La Ferté, died before 1047 (founds the Priory of Sigy by charter co-signed by William [the future Conqueror] between 1030 and 1035)"*

> *"Hugues (II) de La Ferté + avant 1047 moine à Saint-Ouen de Rouen (confirme la fondation du Prieuré de Sigy par charte, avant le 06/03/1047)"*

Translation: *"Hugues (II) de La Ferté, died before 1047, monk at Saint-Ouen de Rouen (confirms the foundation of the Priory of Sigy by charter, before 6 March 1047)"*

These are Renaud's grandsons (sons of Gauthier de La Ferté). Note: French Wikipedia (already fetched in G33 §4) places "Sigy" foundation by Hugues III ~1037–1045 — Pattou attributes Sigy to Hugues (I) de La Ferté (Renaud's grandson) c. 1030–1035, with Hugues (II) de La Ferté confirming before 1047. **There may be two separate Sigy events** — original foundation by the La Ferté line, later patronage/reaffirmation by the Gournay line.

### 7.5 The Foucarmont sister-branch placement

(p. 2, side annotation):

> *"Fiefs des seigneurs de La Ferté autour de La Ferté, à Gaillefontaine, Beaussault, Pont-de-l'Arche, et Poses"*

Translation: *"Fiefs of the lords of La Ferté around La Ferté [-en-Bray], at Gaillefontaine, Beaussault, Pont-de-l'Arche, and Poses"*

These are the documented La Ferté holdings — **the same Gaillefontaine and Beaussault later associated with Hugues IV de Gournay's titles** (per Pattou p. 3: "seigneur de Gournay, La Ferté, Beaussault et Gaillefontaine"). The La Ferté holdings flowed back to the Gournay senior line by Hugues IV's generation. Pettigrew (already cited in the existing G35 companion line 23) makes this reversion explicit: "By these acts, Pettigrew says, the seignories and lands of La Ferte reverted to the elder branch."

### 7.6 Source Materials — Full Verbatim Extracts

#### 7.6.1 FMG MedLands — Renaud (full)

Reproduced verbatim from FS PDF p. 3:

> 2. RENAUD . Seigneur de Gournay. m ALBERADE, daughter of ---. Gauthier de la Ferté founded the priory of La Ferté en Brai, at the command of "fratre Hugone", by charter dated to [989/96], which names his father Renaud and his mother Alberade[883]. Renaud & his wife had two children:
>
>  a) HUGUES [I] de Gournay (-after 989). Gauthier de la Ferté founded the priory of La Ferté en Brai, at the command of "fratre Hugone", by charter dated to [989/96], which names his father Renaud and his mother Alberade[884]. The "command" of his brother suggests that Hugues was the older son, and presumably also Seigneur de Gournay.
>
>  b) GAUTHIER de la Ferté (-after 989). Gauthier de la Ferté founded the priory of La Ferté en Brai, at the command of "fratre Hugone", by charter dated to [989/96], which names his father Renaud and his mother Alberade[885].

**Translation of Latin**:
- *"fratre Hugone"* — *"his brother Hugh"* (the older brother whose authority/command Gauthier acted on).

**FMG footnote references for Renaud (verbatim from FS PDF p. 5)**:

> [884] Gurney (1845), pp. 26 and 31, citing M. de Gondeville's MS Histoire de Gournay, but adding that the original charter no longer exists.
> [885] Gurney (1845), pp. 26 and 31, citing M. de Gondeville's MS Histoire de Gournay, but adding that the original charter no longer exists.

This is the **explicit FMG admission** that the charter substantiating Renaud's existence is preserved only in DG's transcription via the Gondeville MS *Histoire de Gournay* — the original is lost. **Direct primary-source attestation for Renaud is therefore unavailable**; what we have is DG's 1845 reading of a 19th-century manuscript that purportedly transcribed an earlier (10th-century?) copy of the original.

#### 7.6.2 The "Isabelle de Ponthieu" contributor correction note (verbatim, from FS PDF p. 6)

A contributor flagged an FS-tree error and added a correction note. Reproduced verbatim:

> Title: There is no evidence that Gauthier de la Ferté married Isabelle de Ponthieu
> In Racines Histoire there is no mention of anybody named Isabell de Ponthieu; There is an Elizabeth de Ponthieu born to Guillaume I, Comte de Ponthieu et Montreuil, but she became an abbess at St Austreberthe, Montreuil and never married.

This is a useful **example of a constructive contributor note**: the contributor cross-checked Pattou (Racines Histoire) against an FS-tree claim (that Gauthier de la Ferté married an Isabelle de Ponthieu), found no match in Pattou, and identified the likely source of the FS-tree error (Elizabeth de Ponthieu, born to Guillaume I count of Ponthieu — but she became an abbess and never married, so she cannot be Gauthier's wife). **Adopt as documentation that Gauthier de la Ferté's wife is unknown to Pattou and the FS-tree's "Isabelle de Ponthieu" attribution is unsupported.**

#### 7.6.3 FS "Legacy NFS" structured note

> Title: Legacy NFS Source: Renoud De Gourney of La Ferte Lord of Gourney - Published information: birth-name: Renoud De Gourney of La Ferte Lord of Gourney
> Notes: Published information: birth-name: Renoud De Gourney of La Ferte Lord of Gourney
> Published information: male
> Published information: birth: about 0970; Normandie, France

The "Renoud De Gourney of La Ferte" label is itself revealing — a Legacy NFS (New FamilySearch, the predecessor system) source merged "Renaud" with "of La Ferté" as a single name-form, which conflates *Renaud de Gournay* (the seigneur named in the charter) with *Renaud's son Gauthier de La Ferté* (who actually held La Ferté). The FS-tree carries this conflation as a "birth-name."

#### 7.6.4 FS structured-field children with provenance analysis

The FS structured table lists 5 children for Renaud (p. 1–2):

1. **Nocher de Gournay (G5KJ-XTT)** — b. 0987, m. Berthilde de Gamaches (G8F7-CLP), d. 1039 Gournay-en-Bray. Source: Geneanet (foullon tree). **Not in FMG, not in Pattou main chart.** Spurious.
2. **Blanche de Gournay (GR62-DVF)** — b. 0988, m. 1005 Osmond 1er Tyrel de Poix (PZY9-QYJ), d. 1032 Poix-de-Picardie. **Not in FMG, not in Pattou.** Spurious. The Tyrel de Poix family is real (Walter Tirel famously shot William Rufus in 1100) but no documented marriage to a Gournay daughter c. 1005.
3. **Hugues de Gournay II (LVSH-KBM)** — b. after 0989, m. before 1016 Berthilde de Gerberoy, d. 1074 Gournay-en-Bray. **Confirmed via la Ferté charter (FMG [884]).**
4. **Gauthier de Gournay (GKWN-ZD1)** — b. after 0989. **Confirmed via la Ferté charter (FMG [885]).**
5. **Alix de Gournay (G5KJ-XTY)** — b. 0990, m. Eudes de Foucarmont (G52R-SJX), d. 1038 Foucarmont. **Pattou places her at Hugues 1er level**, not Renaud level: *"? Alix de Gournay ép. ? Eudes de Foucarmont"* (chart p. 2, sibling of Hugues 1er, with `?` markers). FS slides her down one generation.

Of the five FS children, only two (Hugues II and Gauthier) are corroborated by FMG. Two are spurious (Nocher, Blanche). One (Alix) is generationally misplaced.


