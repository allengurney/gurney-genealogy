# FS Assessment → Research Companion Omission Audit

**Repo:** `allengurney/gurney-genealogy`  
**Ref inspected:** `main` via GitHub connector  
**Audit date:** 2026-05-07  
**Scope:** Five FamilySearch assessment files supplied by Allen, reconciled against the applicable `research/people/*fact-sheet.research.md` companions.

## Scope rules used

This audit checks whether substantive content from the FS assessment files made it into the applicable **research companion** files under:

`research/people/`

The following assessment sections were treated as **out of scope unless they carried substantive evidence**:

- `FS Tree update suggestions`
- `URL triage`
- routine processing / handoff mechanics
- low-value login triage or access notes

The following were treated as **in scope**:

- facts, findings, source extracts, quotations, translations
- conflicts between scholarly sources
- rejected / spurious FS claims when the rejection itself is useful research context
- collateral-line findings that the assessment explicitly said should be promoted or cross-walked
- place/topic material when the assessment expected it to inform a person companion

## Line-number note

The GitHub connector exposed these Markdown files as large single-line JSON payloads rather than normal line-addressable Markdown. Therefore this audit cites **file path + section / heading / exact search phrase** rather than numeric line numbers. Where absence was tested, the audit records the exact repository search phrase used.

## Files reviewed

| FS assessment | Primary research companion(s) checked |
|---|---|
| `sources/FS/GC1N-CQ3/assessment.md` | `research/people/g35-renaud-de-gournay-fact-sheet.research.md` |
| `sources/FS/LBGV-H99/assessment.md` | `research/people/g32-gerard-de-gournay-fact-sheet.research.md` |
| `sources/FS/LVSH-KBM/assessment.md` | `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md` |
| `sources/FS/MZ68-VKD/assessment.md` | `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` |
| `sources/FS/PWPZ-VK1/assessment.md` | `research/people/g36-hugh-de-gournay-i-fact-sheet.research.md`; `research/people/g37-eudes-de-gournay-fact-sheet.research.md` |

## Executive summary

The core Norman-line synthesis largely made it into the research companions. The strongest merges were:

- G32 Gerard: crusade evidence, Edith de Warenne, Walter-as-son dispute, Amicie/Talbot, St-Sauveur, Beauvais obituary.
- G33 Hugh III: death-year reconciliation, Basilia Flaitel, Domesday, Bec, Gerberoi, Anselm, Senex reassignment.
- G34 Hugh II: 1035 expedition, Mortemer, Wace, Cardiff skepticism, Bayeux charters, Néel/Nigel.
- G35 Renaud: lost La Ferté charter, Gondeville MS chain, Pattou caution, Delisle critique, Albérade surname problem.
- G36/G37: tradition-only status, Eudes/Hugh name-equivalence, Bathilde de Gerberoy candidate, Marthe de Foucarmont caveat, `écu noir`.

The remaining gaps fall into three categories:

1. **Substantive collateral findings omitted from person companions** — especially La Ferté/Sigy, Norfolk junior-line details, and heraldry.
2. **Source-level contradictions smoothed over** — especially Pattou’s claim that Hugh II, not Hugh III, received Essex/Suffolk rewards.
3. **Rejected FS claims not preserved as quarantine notes** — especially Isabelle de Ponthieu and Giselberthe de Gournay.

---

# Detailed exceptions

## GC1N-CQ3 / G35 Renaud de Gournay

### GC1N-CQ3-01 — Gauthier de la Ferté / Isabelle de Ponthieu correction note omitted

**Priority:** Medium  
**Source:** `sources/FS/GC1N-CQ3/assessment.md`  
**Assessment location:** `§1 Source-format anatomy`; `§7.6.2 The "Isabelle de Ponthieu" contributor correction note`  
**Expected destination:** `research/people/g35-renaud-de-gournay-fact-sheet.research.md`, likely under Gauthier de la Ferté collateral / declined claims.

**Missing detail:**

The assessment preserved a contributor correction that directly rejects an FS-tree spouse claim for Renaud’s son Gauthier de la Ferté:

> “There is no evidence that Gauthier de la Ferté married Isabelle de Ponthieu… In Racines Histoire there is no mention of anybody named Isabell[e] de Ponthieu; there is an Elizabeth de Ponthieu born to Guillaume I, Comte de Ponthieu et Montreuil, but she became an abbess at St Austreberthe, Montreuil and never married.”

**Why this matters:**

This is not just FS cleanup. It is a useful **negative finding** for Gauthier de la Ferté, a confirmed collateral son of Renaud. It prevents a future AI from re-importing a spurious Ponthieu marriage.

**Evidence of omission:**

Repository search for exact phrase:

`"Isabelle de Ponthieu"`

returned only:

- `sources/FS/GC1N-CQ3/assessment.md`

No `research/people/` companion was returned.

**Correction needed:**

Add a short declined-claim note to G35 under the Gauthier / La Ferté collateral discussion:

- no evidence Gauthier de la Ferté married Isabelle de Ponthieu;
- Pattou / Racines Histoire does not contain such a spouse;
- Elizabeth de Ponthieu, the superficially similar person, became abbess at St Austreberthe, Montreuil and did not marry.

---

### GC1N-CQ3-02 — La Ferté cadet-line Sigy details omitted

**Priority:** High  
**Source:** `sources/FS/GC1N-CQ3/assessment.md`  
**Assessment location:** `§7.4 Pattou's full chart entry on the la Ferté side-line (sons of Gauthier)`  
**Expected destination:** `research/people/g35-renaud-de-gournay-fact-sheet.research.md`; possibly cross-reference `research/places/sigy-normandy.md`.

**Missing detail:**

The G35 assessment captured detailed Pattou entries for Renaud’s La Ferté collateral line:

> “Hugues (I) de La Ferté + avant 1047 (fonde le Prieuré de Sigy par charte co-signée par Guillaume (futur Conquérant) entre 1030 & 1035)”

Translation:

> “Hugues (I) de La Ferté, died before 1047, founded the Priory of Sigy by charter co-signed by William, the future Conqueror, between 1030 and 1035.”

And:

> “Hugues (II) de La Ferté + avant 1047 moine à Saint-Ouen de Rouen (confirme la fondation du Prieuré de Sigy par charte, avant le 06/03/1047)”

Translation:

> “Hugues (II) de La Ferté, died before 1047, monk at Saint-Ouen de Rouen, confirmed the foundation of the Priory of Sigy by charter before 6 March 1047.”

**Why this matters:**

The G35 research companion does discuss La Ferté reversion, but it does not preserve the **specific Sigy foundation chain**:

- Hugues I de La Ferté founded Sigy;
- charter co-signed by William, future Conqueror;
- date range 1030–1035;
- Hugues II de La Ferté became a monk at Saint-Ouen de Rouen;
- confirmation charter before 6 March 1047.

This is a substantive collateral-line finding tied to Renaud’s son Gauthier and grandsons.

**Evidence of omission:**

Repository search for exact phrase:

`"confirme la fondation du Prieuré de Sigy"`

returned only:

- `sources/FS/GC1N-CQ3/assessment.md`

A broader search for `Sigy` found `research/places/sigy-normandy.md`, but no relevant `research/people/g35...` entry.

**Correction needed:**

Add a G35 collateral subsection such as:

`La Ferté cadet line and Sigy priory`

Include both Hugues I and Hugues II de La Ferté entries, with the co-signing by William and the before-6-March-1047 confirmation.

---

### GC1N-CQ3-03 — La Ferté fief list and later reversion geography only partially merged

**Priority:** Medium  
**Source:** `sources/FS/GC1N-CQ3/assessment.md`  
**Assessment location:** `§7.5 The Foucarmont sister-branch placement`; also tied to `§7.4` and G35 La Ferté discussion  
**Expected destination:** `research/people/g35-renaud-de-gournay-fact-sheet.research.md`

**Partially missing detail:**

The research companion records that La Ferté reverted to the senior Gournay line, but the assessment preserved a more specific fief geography:

> “Fiefs des seigneurs de La Ferté autour de La Ferté, à Gaillefontaine, Beaussault, Pont-de-l'Arche, et Poses”

Translation:

> “Fiefs of the lords of La Ferté around La Ferté, at Gaillefontaine, Beaussault, Pont-de-l'Arche, and Poses.”

The assessment also notes that the same **Gaillefontaine** and **Beaussault** names later appear in Hugues IV de Gournay’s title stack:

> “seigneur de Gournay, La Ferté, Beaussault et Gaillefontaine”

**Why this matters:**

This connects Renaud’s cadet La Ferté line to later senior-line territorial titles. The G35 research currently captures the reversion concept but not the fief list or its later-title significance.

**Correction needed:**

Add the fief list to G35 §8 or equivalent La Ferté reversion section, with a sentence explaining that these holdings help explain the later senior-line style including La Ferté, Beaussault, and Gaillefontaine.

---

## LBGV-H99 / G32 Gerard de Gournay

### LBGV-H99-01 — Sigy protection / Hugh exactions quotation not present in people companions

**Priority:** Medium  
**Source:** `sources/FS/LBGV-H99/assessment.md`  
**Assessment location:** `§2.2 Net-new content worth promoting`, item 9  
**Expected destination:** likely `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` or a cross-reference from G32/G33 to `research/places/sigy-normandy.md`.

**Missing detail:**

The LBGV assessment preserved a French Wikipedia quotation:

> “La famille de Gournay exerce longtemps une sorte de tutelle sur le prieuré de Sigy qu'Henri II d'Angleterre place sous sa protection pour le défendre des exactions d'Hugues de Gournay.”

Translation:

> “The family of Gournay long exercised a sort of tutelage over the priory of Sigy, which Henry II of England placed under his protection to defend it from the exactions of Hugues de Gournay.”

The same assessment also notes:

- Sigy-en-Bray was attributed to Hugh III;
- founded c. 1037–1045;
- made subject to Saint-Ouen de Rouen;
- this reinforces the later Norfolk / Lessingham connection.

**Why this matters:**

This is a substantive place-and-person finding. It is relevant to the G33/G35 Sigy problem and to the Gournay family’s patronage / control of religious houses.

**Evidence of partial routing:**

Repository search for `Sigy` found:

- `research/places/sigy-normandy.md`
- assessment files and other non-person files

But it did not surface a corresponding `research/people/g32...`, `g33...`, or `g35...` companion entry.

**Correction needed:**

Add at least a cross-reference note in G33 or G35 to the Sigy place file, preserving:

- the Henry II protection quote;
- the “exactions of Hugues de Gournay” point;
- the possible tension with the La Ferté-line Sigy foundation entries from GC1N-CQ3.

---

### LBGV-H99-02 — WikiTree Warenne detail only partially merged

**Priority:** Low  
**Source:** `sources/FS/LBGV-H99/assessment.md`  
**Assessment location:** `§2.2 Net-new content worth promoting`, item 10  
**Expected destination:** `research/people/g32-gerard-de-gournay-fact-sheet.research.md`

**Partially missing detail:**

The G32 research companion correctly notes Edith de Warenne’s second marriage to Drew / Drogo / Dreux de Monchy / Monceaux and includes the approximate 1107 date. However, the assessment carried a more specific WikiTree-derived detail:

- second marriage to Dreux / Drew / Drogo de Moncy in **1107**;
- one son, **Dreux II “the younger”**;
- Dreux II died after **1147**.

The G32 companion preserves the son as Drogo in the Guillaume / Orderic source context, but does not appear to retain the WikiTree-specific “Dreux II the younger, d. after 1147” detail.

**Why this matters:**

This is low evidentiary weight because WikiTree is not a primary source and the assessment itself says to downgrade it if contradicted. Still, the assessment identified it as a tighter chronology clue.

**Correction needed:**

Either:

- add a low-weight note in G32 under Edith’s second marriage, explicitly attributed to WikiTree and caveated; or
- add a footnote explaining that the “Dreux II the younger, after 1147” detail was reviewed but not adopted.

---

## LVSH-KBM / G34 Hugh de Gournay II

### LVSH-KBM-01 — Pattou’s post-Conquest reward attribution to Hugh II omitted

**Priority:** High  
**Source:** `sources/FS/LVSH-KBM/assessment.md`; also echoed in `sources/FS/MZ68-VKD/assessment.md`  
**Assessment location:** `§7.2 Pattou's full chart annotations on the Domesday-era Gournay rewards`  
**Expected destination:** `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`; likely also a caveat in `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`.

**Missing detail:**

The assessment preserved Pattou’s blue-text annotation:

> “Les Gournay sont récompensés après la conquête : Hugues II reçoit des fiefs en Essex et en Suffolk ; Néel reçoit plusieurs domaines en Somerset près Bristol et Bath.”

Translation:

> “The Gournays are rewarded after the conquest: Hugues II receives fiefs in Essex and Suffolk; Néel receives several domains in Somerset near Bristol and Bath.”

**Why this matters:**

The current G33 research companion assigns the Essex Domesday manors to Hugh III, following Domesday / Open Domesday / FMG. Pattou’s chart attributes post-Conquest Essex/Suffolk reward to **Hugh II**. That is a source-level contradiction worth preserving, even if the repo continues to follow the Domesday/FMG interpretation.

This is not merely an FS-tree correction; it is a documented scholarly disagreement from Pattou.

**Evidence of omission:**

Repository searches:

- `"Les Gournay sont récompensés"` returned only `sources/FS/LVSH-KBM/assessment.md`.
- `"Hugues II reçoit"` returned only the assessment files, not the research companions.

**Correction needed:**

Add a G34 note under the Hastings / post-Conquest rewards section:

- Pattou assigns Essex/Suffolk rewards to Hugues II;
- repo / Domesday / FMG treat the recorded Essex tenant-in-chief as Hugh III;
- likely explanation: Pattou compresses reward-to-family with later Domesday tenure or attributes initial grant to the father and possession to the son.

Also add a short cross-reference in G33 §5.1 noting the attribution conflict.

---

### LVSH-KBM-02 — Somerset cadet-line chain under Néel / Nigel not fully preserved

**Priority:** Medium  
**Source:** `sources/FS/LVSH-KBM/assessment.md`  
**Assessment location:** `§5 Patchset readiness sketch`, item 5; also Pattou pp. 12–14 as summarized in `§2.2` item 8  
**Expected destination:** `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`; possibly `research/case-files/somerset-gournay-cadet-line.md`.

**Partially missing detail:**

The G34 research companion includes Néel / Nigel de Gournay and notes he founded the Somerset cadet line, with Barrow-Gurney and Inglishcombe and later Sir Thomas / Sir Matthew descendants. However, the assessment’s more complete chain was not fully carried forward:

- Néel / Nigel de Gournay
- Robert
- Hawise
- Eva
- Robert, d. 1269
- Anselme, d. 1286
- Sir Thomas de Gournay, d. c. 1330, jailer of Edward II
- Sir Matthew de Gournay, b. 1310, d. 26 September 1406, associated with Crécy, Poitiers, Stoke-sub-Hamdon, praised by Froissart

**Why this matters:**

The assessment’s purpose was to disambiguate the “third Gournay at Hastings” and the Somerset cadet line. The people companion preserves the headline but not the chain detail. If the repo wants the research companion to be usable without re-opening the assessment, the chain nodes should be retained somewhere in the research layer.

**Correction needed:**

Either:

- expand the G34 Néel / Nigel children-table note with the chain; or
- create / populate `research/case-files/somerset-gournay-cadet-line.md` and add a cross-reference from G34.

---

## MZ68-VKD / G33 Hugh de Gournay III

### MZ68-VKD-01 — Pattou Norfolk junior-line chart details not promoted to person companions

**Priority:** High  
**Source:** `sources/FS/MZ68-VKD/assessment.md`  
**Assessment location:** `§3.1 Material updates to Pass A`, item 11  
**Expected destination:** later Gurney/Gournay people companions, especially G25 and the G7–G15 Norfolk-side chain; at minimum an index note from G33 or a dedicated crosswalk file.

**Missing detail:**

The assessment preserved substantial Norfolk junior-line detail from Pattou pp. 5–11. Some Walter-parentage material appears in the Walter case file, but the specific later-line person facts do not appear to have been promoted to the applicable `research/people/` companions.

Key omitted details include:

- Walter de Gournay of Suffolk / Norfolk as “possible petit-fils de Girard de Gournay et d'Edive de Warenne.”
- **John III de Gournay m. Jeanne de Lexham, daughter of Edmond** — directly relevant to repo G25.
- Antoine de Gournay (1511) → François:
  - François born **20 August 1521**
  - married **6 August 1543** Helen Holditch
- Henry I:
  - born **21 January 1548**
  - married Ellene Blennerhasset
- Norfolk line down to:
  - Edward, **1608–1641**
  - Henry II, **1632–1661**, branch extinction
- Cadet Francis of Maldon → John:
  - John, Quaker, **1655–1721**
  - Joseph, **1692–1750**, bought Keswick **1747**
  - John, **1716–1770**
  - Richard, born **1743**
  - Hudson Gurney of Keswick, born **1775**

**Evidence of omission / partial routing:**

Repository search for:

`"Jeanne de Lexham"`

returned:

- `sources/FS/MZ68-VKD/assessment.md`
- `research/case-files/walter-de-gournay-as-son-of-gerard.md`

It did **not** return the applicable `research/people/` companions.

**Why this matters:**

The assessment explicitly stated this material was “directly relevant to the repo's G7–G15 Norfolk-side chain” and should be cross-walked carefully. That did not occur in the `research/people/` layer.

**Correction needed:**

Create a follow-on intake note or patchset specifically for the Pattou Norfolk junior-line chart:

- crosswalk G25 John III de Gournay first;
- then crosswalk G15–G7 where names/dates match;
- keep the Walter-parentage uncertainty separate from the later Norfolk-line facts.

---

### MZ68-VKD-02 — Heraldic annex details not promoted to research layer

**Priority:** Medium / Deferred  
**Source:** `sources/FS/MZ68-VKD/assessment.md`  
**Assessment location:** `§3.1 Material updates to Pass A`, item 12  
**Expected destination:** likely `research/topics/gournay-heraldry.md`, `research/topics/coat-of-arms...`, or relevant people companions for Hugues V, Mathieu, Robert, Sibylle, and the Norfolk branch.

**Missing detail:**

The assessment summarized a detailed heraldic annex from Pattou pp. 15–17 / NRP de La Mairie 1844 engravings:

- Hugues V seals, Nos. 1 and 2
- Mathieu de Gournay seal, No. 3
- Gournay-Norfolk arms, No. 5
- impaled / quartered arms:
  - Gournay-Baconsthorpe
  - Gournay-Middleton
  - Gournay-Kett
  - Gournay-Kerville
  - Gournay-Jerningham
  - Gournay-Calthorpe
  - Gournay-Heydon
  - Gournay-Holditch
  - Gournay-Blennerhasset
  - Gournay-Lewknor
  - Gournay-Hovel
- Robert de Gournay seal, No. 20
- Sibylle de Gournay seal, No. 21

**Why this matters:**

This is source-rich heraldic content, and the assessment explicitly identified it as a future heraldry pass candidate. It does not necessarily belong in G33 alone, but it should not be lost.

**Correction needed:**

Create or update a heraldry topic file, then cross-reference relevant person companions:

- Hugues V
- Mathieu de Gournay
- Robert de Gournay
- Sibylle de Gournay
- Norfolk Gournay branch ancestors

If a heraldry topic file already exists, add this annex as a structured source inventory.

---

### MZ68-VKD-03 — Some Geni / later-source addendum content appears unmerged or only generally cited

**Priority:** Low / Needs targeted re-check  
**Source:** `sources/FS/MZ68-VKD/assessment.md`  
**Assessment location:** later addendum sections, especially Geni Hugues III profile / Lorraine source sections  
**Expected destination:** G33 research companion or applicable case/topic files.

**Potential missing detail:**

The MZ assessment includes a later URL-pass addendum referencing substantial Geni Hugues III yield, including:

- new sibling claims;
- Mellcene Smith narrative;
- R.B. Stewart entry.

The G33 research companion cites Geni / WikiTree generally, but the visible companion synthesis does not appear to preserve the specific addendum claims.

**Why this is lower confidence:**

The assessment response was truncated in the connector output during review, so this item should be verified directly against the full assessment file before editing.

**Correction needed:**

Re-open the full `sources/FS/MZ68-VKD/assessment.md` and compare all post-URL-pass addendum sections against G33 and the relevant case files. Promote only substantive claims with source value; ignore generic Geni profile boilerplate.

---

## PWPZ-VK1 / G36 Hugh I and G37 Eudes

### PWPZ-VK1-01 — Giselberthe de Gournay rejected-child claim omitted from quarantine notes

**Priority:** Medium  
**Source:** `sources/FS/PWPZ-VK1/assessment.md`  
**Assessment location:** `§2.3 FS conflicts with repo`; `§2.4 Spurious / over-claimed structured-field content`  
**Expected destination:** `research/people/g36-hugh-de-gournay-i-fact-sheet.research.md` or `research/people/g37-eudes-de-gournay-fact-sheet.research.md`, probably as a declined FS-tree claim.

**Missing detail:**

The assessment records a specific unsupported FS child:

- **Giselberthe de Gournay** (`G17J-BBT`)
- born **0957**
- married **Iton de Gisors d'Orléans d'Angleterre**
- died **1011**, Neufchâtel-en-Bray
- unsupported by FMG, Pattou, or French Wikipedia
- likely community-tree confabulation

**Evidence of omission:**

Repository search for exact phrase:

`"Giselberthe de Gournay"`

returned only:

- `sources/FS/PWPZ-VK1/assessment.md`

No `research/people/` companion was returned.

**Why this matters:**

This is a rejected structured FS claim, but the assessment treated it as a specific spurious child requiring quarantine. If the research companions are expected to preserve rejected but recurrent FS-tree accretions, this should be captured.

**Correction needed:**

Add a short “declined FS-tree child claim” note to G36 or G37:

- Giselberthe claim reviewed;
- no scholarly support found;
- Gisors family is real, but this specific 10th-century Gournay marriage is unsupported.

---

### PWPZ-VK1-02 — Alix de Gournay / Eudes de Foucarmont appears only as a misplaced G35 declined child, not promoted to correct generation

**Priority:** Medium  
**Source:** `sources/FS/GC1N-CQ3/assessment.md`; `sources/FS/PWPZ-VK1/assessment.md`  
**Assessment location:** GC1N-CQ3 `§2.3 FS conflicts`; PWPZ-VK1 `§7.4 The "Alix de Gournay m. Eudes de Foucarmont" sister attribution`  
**Expected destination:** `research/people/g36-hugh-de-gournay-i-fact-sheet.research.md` or G36/G37 collateral note.

**Partially missing detail:**

The G35 research companion correctly says FS misplaces Alix as Renaud’s daughter. However, the assessment says Pattou places her at the **Hugues 1er sibling level**, with `?` markers:

> “? Alix de Gournay ép. ? Eudes de Foucarmont”

The specific candidate should be retained in the generation where Pattou places it, not only as a declined child of Renaud.

**Evidence of partial routing:**

Repository search:

`Alix Gournay Foucarmont`

returned:

- `research/people/g35-renaud-de-gournay-fact-sheet.research.md`
- assessment files

It did not surface a corresponding G36/G37 person-companion note.

**Correction needed:**

Add a G36/G37 collateral note:

- Pattou tentatively places Alix de Gournay, wife of Eudes de Foucarmont, near Hugues 1er sibling level;
- FS wrongly moves her down to Renaud’s child generation;
- no adoption as direct-line fact.

---

### PWPZ-VK1-03 — Marthe de Foucarmont detailed FS-tree parents/dates intentionally not merged, but no explicit declined-detail record

**Priority:** Low  
**Source:** `sources/FS/PWPZ-VK1/assessment.md`  
**Assessment location:** `§2.3 FS conflicts`; `§2.4 Spurious / over-claimed structured-field content`  
**Expected destination:** optional declined-claim note in G37.

**Missing or intentionally summarized detail:**

The G36/G37 companions correctly preserve the high-level finding:

- Marthe de Foucarmont is a doubly tentative candidate at Eudes level;
- detailed dates and parents are community-tree extrapolation.

The assessment carried more specific rejected details:

- Marthe born **0944**, Foucarmont
- died **1000**, Gournay-en-Bray
- father **Clotaire / Clothaire de Foucarmont**
- mother **Sylvette de Sénarpont**

The research companions summarize these as unsupported and do not list every rejected value.

**Correction needed:**

No correction is required unless the repo’s convention is to preserve every rejected structured FS detail. If so, add a compact parenthetical declined list.

---

# Items that appear to have been successfully merged

This section is included so the correcting AI does not duplicate work.

## Successfully merged from GC1N-CQ3 / G35

- FMG / Gurney / Gondeville chain for the lost La Ferté charter.
- Original charter no longer exists.
- Renaud / Albérade / Hugues / Gauthier FMG extract.
- Pattou `? Renaud` caution and French Wikipedia “douteux.”
- Delisle critique.
- Pattou’s 989/96 vs possible Richard II / 1026 hedge.
- Albérade de Montdidier rejected.
- Nocher and Blanche rejected.
- Renaud’s local-tradition third son Raoul.
- La Ferté reversion to senior Gournay line.

## Successfully merged from LBGV-H99 / G32

- Jumièges Radulphus Havoth charter.
- Orderic [1089/90] Gournay / La Ferté / Gaillefontaine delivery.
- Orderic [1089] Écouché / Basilia identification.
- Albert of Aix / Baudry / Guillaume de Jumièges crusade attestations.
- Edith accompanying Gerard.
- Edith as sister of William de Warenne.
- Walter-as-son-of-Gerard dispute.
- Amicie / Talbot parentage problem.
- Henry II Valmont and Sainte-Foi charters.
- Pattou Gerard ~1073 rejected by 1082 charter constraint.
- St-Sauveur 1104 terminus.
- Beauvais obituary.
- Caister / Cantley / Saint-Hildevert tie.

## Successfully merged from LVSH-KBM / G34

- 1035 expedition captain list.
- William of Poitiers / Robert d’Eu alliance.
- Bayeux “Brenerias” / Bernières charter issue.
- Cardiff tradition and MedLands skepticism.
- No Canute in Norway / Denmark in 1074.
- Pattou epithet stack assigned to Hugh II.
- Wace “li vieil Hue de Gornai.”
- Berthilde de Gerberoy rejected at G34 and moved to G36 candidate.
- Basilie Flaitel duplicate spouse rejected.
- Judith / Amicie structured FS children rejected or caveated.
- Néel / Nigel recognized as Somerset cadet founder.

## Successfully merged from MZ68-VKD / G33

- Hugh III birth range c. 1020–1030.
- Mother unknown.
- Marriage after 1051 to Basilia Flaitel.
- Death-year reconciliation: entered Bec / priorate / 1110 death.
- Anselm letter ambiguity.
- Basilea’s first husband and ducal collateral context.
- Flaitel sibling network.
- Anfrede / Ansfride tangle.
- Senex moved from G33 to G34.
- Domesday Essex manors.
- Bec 1076 charter.
- Caister / Cantley tie.
- Caen 1077 / 1082 charters.
- Gerberoi mediator role.
- 1067 Saint-Benoît and 1073 Marmoutier charters.
- Hugh III children over-share trimmed.

## Successfully merged from PWPZ-VK1 / G36/G37

- FMG / DG “matter of tradition” status.
- Eudes and Hugues lack contemporary documents.
- Pattou / French Wikipedia structural caution.
- Pattou `?Hugues` not adopted.
- Bathilde de Gerberoy as tentative G36 candidate.
- Marthe de Foucarmont as doubly tentative G37 candidate.
- Hugh I birth range widened to c. 920–940.
- La Tour Hue / fortifier material.
- Eudes / Hugh name-equivalence.
- `écu noir` / original plain sable arms.
- Eudes death bracket after 911, before c. 932.
- Lorraine “Vuldus” alternative rejected.

---

# Recommended correction sequence

## 1. High-priority person-companion fixes

1. `research/people/g35-renaud-de-gournay-fact-sheet.research.md`
   - Add Gauthier / Isabelle de Ponthieu rejected-spouse note.
   - Add La Ferté cadet-line Sigy details.
   - Add La Ferté fief geography.

2. `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`
   - Preserve Pattou’s post-Conquest rewards attribution to Hugh II as a source-level conflict.
   - Expand or cross-reference the Néel / Nigel Somerset cadet chain.

3. `research/people/g36-hugh-de-gournay-i-fact-sheet.research.md`
   - Add Alix de Gournay / Eudes de Foucarmont as tentative sibling-level collateral if the repo wants to retain Pattou’s full sibling layer.

## 2. Cross-cutting follow-up files

1. Create / update a Sigy file or add people cross-references:
   - `research/places/sigy-normandy.md`
   - G33/G35 person companions

2. Create / update:
   - `research/case-files/somerset-gournay-cadet-line.md`

3. Create / update:
   - heraldry topic file for Pattou / NRP engravings and seal inventory.

4. Create a later-Norfolk-line intake pass:
   - G25 first, then G15–G7 as applicable.

## 3. Optional quarantine notes

Add one-line rejected FS-tree claim notes for:

- Giselberthe de Gournay / Iton de Gisors
- detailed Marthe de Foucarmont dates / parents
- if not already clear, Alix as misplaced daughter of Renaud

These are optional because they are FS-structured accretions, but preserving them helps prevent future re-import.
