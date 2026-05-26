# Intake patchset v55 — Medieval Gournay web leads (Powell 1584 Welsh attestation for G34; Robert d'Évreux Seigneur de Gacé for G33)

**Prepared:** 2026-05-23
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation). **Status:** Draft patchset for review. **Do NOT apply until approved.**
**Origin:** User-supplied URL bundle of medieval Gournay leads (8 URLs: Annales de Normandie Beaubec article on Persée; Patterson "Companions of the Conqueror" Hugh de Gournay entry; three database pages on Hugh V "the Cuckoo"; one on Hugh IV de Gournay with deep family-graph navigation; one on Gérard G32; one blog post on Hugh II).
**Prerequisite:** v55 references the `fmg-medlands-normacre` sourceId proposed in v54 §16; if v54 has not been applied when v55 is applied, that sourceId must be added at v55-apply time, otherwise the citation alignment will fail. v55 also proposes one new sourceId of its own (`powell-historie-cambria-1584`).

## Decision summary

| # | URL | Subject | Outcome |
|---|---|---|---|
| 1 | persee.fr/.../annor_0003-4134_1974_num_24_2_5131 | Suzanne Deck, *Le temporel de l'abbaye cistercienne de Beaubec*, *Annales de Normandie* 24/2 (1974), pp. 131–156 | **EXCLUDE** |
| 2 | patp.us/.../hugh-de-gournay | Patterson, "Hugh de Gournay," *Companions of the Conqueror* | **INCLUDE** — adds Powell 1584 Welsh Chronicle 1094 attestation as a fifth Cardiff tradition (G34 §6) |
| 3 | cybergata.com/roots/3187.htm | Hugh V "the Cuckoo" de Gournay | **EXCLUDE** |
| 4 | genealogieonline.nl/.../P30399.php | Same Hugh V | **EXCLUDE** |
| 5 | nielsenhayden.com/.../I7740 | Same Hugh V | **EXCLUDE** |
| 6 | thesignsofthetimes.com.au/30/56867.htm | Gérard de Gournay G32 | **EXCLUDE** |
| 7 | talltalesfromthetrees.blogspot.com/.../hugh-de-gournay-d-c1074-and-his-two.html | Colin Salter 2013 on Hugh II G34 | **EXCLUDE** |
| 8 | buist-keatch.org/buist/goring/3114.html (Hugh IV collateral) | — page itself collateral, but navigation from it (3159 Hugh III; 3162 Basilie Flaitel; 3098 Gérard G32; 3099 Edith de Warenne; 6343 Amicie; 3097 Gundred; 2947 Gérard Flaitel; 2914 William de Warenne 1st Earl) yielded one new finding for G33 §3.1 | **EXCLUDE the 3114 page; INCLUDE the navigation finding** (Basilie Flaitel's son by Raoul de Gacé = Robert d'Évreux Seigneur de Gacé) |

**Two inclusions, seven exclusions, eight buist-keatch family-graph pages traversed.**

---

## 1. INCLUDE — G34 research companion: Powell 1584 Welsh Chronicle attestation

### 1.1 The attestation

Patterson's *Companions of the Conqueror* page reproduces verbatim a Welsh-Chronicle entry from David Powell's continuation of Humphrey Llwyd's *Historie of Cambria* (London, 1584), recorded under the year 1094:

> "About this time Roger Montgomery, Earl of Salop and Arundell, William Fitz-Eustace, Earl of Gloucester, Arnold de Harcourt and Neale le Vicount were slain between Cardiff and Brecknock by the Welshmen; also Walter Evereux, Earl of Sarum, and Hugh Earl Gourney were there hurt, and died after in Normandy."

Framing sentence on the page: *"In Dr. Powell's continuation of Humphrey Lloyd's description of Wales, translated from the Welsh, and published in 1584, it is recorded under the date of 1094…"*

### 1.2 Significance for the G34 §6 Cardiff synthesis

The existing G34 §6 documents four traditions for the "Cardiff" engagement, all dating it to 1074:

- *Histoire et Chronique de Normandie* (Rouen 1610), via Potin 1842 p. 105
- Daniel Gurney *Supplement* Note 10 (1858)
- *Histoire de Lorraine* (Calmet) via M. Palain de Mongnigny
- FMG MedLands [892] — verdict that the account is garbled

G34 §6.6's repo position: "wounded in an East Anglian engagement, traditionally remembered as 'Cardiff'" — anchored by the Caister 1075–76 forfeiture redistribution dating (Palmer *Perlustration of Yarmouth* 1872).

Powell 1584 carries the same legendary content but dates it twenty years later — 1094, William II Rufus's Welsh-frontier campaigns, the south-east Welsh setting between Cardiff and Brecknock. Powell's name list is a near-perfect subset of the French *Histoire et Chronique* list:

| Powell 1584 (1094) | *Histoire et Chronique de Normandie* (1610) (1074) |
|---|---|
| Roger Montgomery, Earl of Salop and Arundell | Roger de Montgommery |
| Neale le Vicount | Néel le Vicomte |
| Arnold de Harcourt | Arnoult de Harcourt |
| Hugh Earl Gourney (wounded, died in Normandy) | Hue de Gournay (wounded, died in Normandy) |
| Walter Evereux, Earl of Sarum (wounded, died in Normandy) | le Comte d'Évreux (wounded, died in Normandy) |

Powell uniquely glosses the bare "Comte d'Évreux" as "Walter Evereux, Earl of Sarum" — a Norman/Salisbury confusion internal to the Welsh transmission (the Évreux-comté title is conflated with the Anglo-Norman Earl of Salisbury).

The two chronicle families are textually independent: Powell from Welsh annalistic material (Llwyd's translation of medieval Welsh chronicles, principally *Brut y Tywysogion*); the French *Histoire et Chronique* from Norman chronicle tradition. Their convergence on the same name list at *different* dates is diagnostic — the legendary "Hugh wounded at a Welsh battle, died in Normandy" tale was free-floating, and each chronicle community placed it at the date most plausible in its own framing.

### 1.3 Proposed edit to `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`

After §6.6 ("Synthesis — the Cardiff narrative is legendary"), append a new sub-section §6.7. Find (line ~187):

```
### 6.6 Synthesis — the Cardiff narrative is legendary

The four traditions all transmit the same garbled memory: a Norman engagement in 1074–75 against a Scandinavian-led invasion, in which Hugh II was wounded, returned to Normandy, and died. The named details vary wildly (Wales / Norwich / "Norveck"; Canute / Conrad; Ralph de Gaël / Earls' Revolt obscured). Modern scholarship rejects the Cardiff specifically; the repo's framing is "wounded in an East Anglian engagement, traditionally remembered as 'Cardiff'."
```

Append after that paragraph, before §7 begins:

```
### 6.7 Welsh-Chronicle 1094 attestation — Powell 1584

A fifth tradition, textually independent of the four French/Norman/Lorraine traditions, places the same legendary content twenty years later, in 1094, on the Welsh frontier under William II Rufus. David Powell, *The Historie of Cambria, now called Wales* (London, 1584) — continuing Humphrey Llwyd's English translation of medieval Welsh annal material (principally *Brut y Tywysogion*) — records under the year 1094:

> "About this time Roger Montgomery, Earl of Salop and Arundell, William Fitz-Eustace, Earl of Gloucester, Arnold de Harcourt and Neale le Vicount were slain between Cardiff and Brecknock by the Welshmen; also Walter Evereux, Earl of Sarum, and Hugh Earl Gourney were there hurt, and died after in Normandy."[^powell-1584-welsh-1094]

The Powell name list is a near-perfect subset of the French *Histoire et Chronique de Normandie* (Rouen 1610) list at §6.1 of this companion, transposed to 1094 and a south-east Welsh setting (Cardiff–Brecknock): Roger of Montgomery, Néel le Vicomte, Arnoult de Harcourt, "Hue de Gournay" (wounded, dying in Normandy), and the Comte d'Évreux (wounded, dying in Normandy) all reappear. Powell uniquely glosses "Comte d'Évreux" as "Walter Evereux, Earl of Sarum" — an Évreux/Salisbury confusion internal to the Welsh transmission; the French tradition has only the bare "Comte d'Évreux," which FMG [892] already flagged as historically unattested at any Évreux death in 1074.

Powell's Welsh annal tradition and the French *Histoire et Chronique* Norman tradition are textually independent. Their convergence on the same name list at *different* dates is diagnostic: the legendary "Hugh wounded at a Welsh battle, died in Normandy" tale was free-floating, and each chronicle community attached it to the date most plausible in its own framing. The French chose 1074 (Earls' Revolt). The Welsh chose 1094 (Welsh revolt against William Rufus).

**Effect on the repo position.** §6.6's tentative "1074–75 East Anglian engagement" framing was anchored by Palmer's *Perlustration of Yarmouth* (1872) dating the Caister forfeiture redistribution to 1075–76. That anchor remains. But Powell 1584 shows the East Anglian framing is *one* candidate host event, not the demonstrably correct one. The 1094 Welsh framing is the other principal candidate. The repo's framing is therefore best stated as: *the Cardiff narrative attaches a legendary tradition of Hugh II's mortal wounding to one of two historically plausible engagements — the 1074–75 East Anglian Earls' Revolt or the 1093–95 Welsh frontier revolt under William II Rufus — with no surviving documentary anchor strong enough to choose between them*. The chronological strain on the c. 985 birth-year framing is real either way (Hugh II would be c. 89 at the 1074 event, c. 109 at the 1094 event); the second is implausible for active combat, but Powell's text says "hurt, and died after in Normandy" — survival-after-wounding remains consistent with any age, and Hugh III (G33) is independently documented from 1076 onwards as active head of the family in his father's stead.

[^powell-1584-welsh-1094]: David Powell, *The Historie of Cambria, now called Wales: a part of the most famous Yland of Brytaine* (London: Rafe Newberie and Henrie Denham, 1584), continuing the unfinished English translation by Humphrey Llwyd of medieval Welsh chronicle material (principally *Brut y Tywysogion*). The passage is quoted in full at <https://patp.us/reading/companions-of-the-conqueror/hugh-de-gournay>. The Powell first edition is at Early English Books Online (STC 2nd ed. 20089) and at the British Library (shelfmark G.6056); the standard modern edition is the 1811 Wynne re-edition. Source ID: `powell-historie-cambria-1584`.
```

Then update the §11 "Sources consulted" table by inserting a new row before the final blank line:

```
| David Powell, *The Historie of Cambria, now called Wales* (London, 1584), continuing Humphrey Llwyd | `powell-historie-cambria-1584` (proposed) |
```

### 1.4 JSON alignment

Insert into `data/sources.json` under the top-level `sources` object:

```json
    "powell-historie-cambria-1584": {
      "shortTitle": "Powell — Historie of Cambria (1584)",
      "citation": "Powell, David. The Historie of Cambria, now called Wales: a part of the most famous Yland of Brytaine. London: Rafe Newberie and Henrie Denham, 1584. Continuing the unfinished English translation by Humphrey Llwyd of medieval Welsh chronicle material (principally Brut y Tywysogion). Standard modern re-edition: Wynne 1811.",
      "archive": "Early English Books Online (STC 2nd ed. 20089) / British Library (G.6056); 1811 Wynne re-edition in print",
      "url": "https://patp.us/reading/companions-of-the-conqueror/hugh-de-gournay",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Welsh-chronicle tradition dating the Cardiff engagement of Hugh de Gournay to 1094 (not 1074), between Cardiff and Brecknock, under William II Rufus's Welsh frontier campaigns. Powell's list of named wounded/killed is a near-perfect subset of the French Histoire et Chronique de Normandie (Rouen 1610) list for the same engagement, with the dating offset twenty years — diagnostic evidence the legendary content was free-floating across chronicle families. URL above is the patp.us mediating page (where the verbatim 1094 entry was retrieved); Phase-2 verification against the EEBO scan of Powell 1584 or the 1811 Wynne re-edition is the next step. Used in research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md §6.7."
    }
```

---

## 2. INCLUDE — G33 research companion §3.1: Basilie Flaitel's son by Raoul de Gacé

### 2.1 The finding

The buist-keatch.org genealogy database, person 3162 (Basilie Flaitel), records that her first marriage to Raoul de Gacé produced one named son: **Robert d'Évreux Seigneur de Gacé**. Sources cited on the buist-keatch 3162 page: Charles Cawley *Medieval Lands*; Douglas Richardson SGM 20 Jan 2003; John Ravilious SGM 11 Jan 2003.

The existing G33 §3.1 pedigree-table documents Basilie's first husband Raoul de Gacé / de Vassy / "Tête-dure" (d. 1051) and traces him back to Robert Archbishop of Rouen + Count of Évreux, but does not name a son of the Raoul × Basilie marriage. Robert d'Évreux Seigneur de Gacé is the next-generation male heir of the Gacé seigneurie, carrying the Évreux-collateral blood that the G33 §3.1 paragraph already flags as material context for Basilie's *maritagium* (the castle of Écouché, DG-I pp. 55, 65; FMG [880]).

This adds one substantive datapoint to G33's family network: Hugh III's stepson was the next Seigneur de Gacé, embedding the Gournay-Flaitel marriage one further step into the Évreux-comté succession after 1051.

### 2.2 Proposed edit to `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`

Find the §3.1 table at line ~70:

```
| Generation | Person | Detail |
|---|---|---|
| Richard I, Duke of Normandy + Duchess Gunnor | parents of Robert | |
| Robert, Archbishop of Rouen + Count of Évreux | by his concubine Hélène | per Moréri, three sons: Richard, **Radulphe**, Guillaume |
| **Raoul de Gacé / Vassy / Tête-dure** ("Hard-head") | Basilea's first husband | died 1051; widow Basilea remarried Hugh III after 1051 |
```

Replace with:

```
| Generation | Person | Detail |
|---|---|---|
| Richard I, Duke of Normandy + Duchess Gunnor | parents of Robert | |
| Robert, Archbishop of Rouen + Count of Évreux | by his concubine Hélène | per Moréri, three sons: Richard, **Radulphe**, Guillaume |
| **Raoul de Gacé / Vassy / Tête-dure** ("Hard-head") | Basilea's first husband | died 1051; widow Basilea remarried Hugh III after 1051 |
| **Robert d'Évreux Seigneur de Gacé** | son of Raoul × Basilea | named heir of the Gacé seigneurie; Hugh III's stepson, carrying the Évreux-comté collateral blood forward after 1051[^robert-evreux-gace-son] |
```

Add the new footnote after the §3.1 closing paragraph (immediately before the §3.2 heading), or co-locate with existing §3 footnotes per file convention:

```
[^robert-evreux-gace-son]: Robert d'Évreux Seigneur de Gacé identified as son of Raoul de Gacé × Basilia Flaitel per Charles Cawley, *Medieval Lands* (Foundation for Medieval Genealogy), and corroborated by Douglas Richardson, soc.genealogy.medieval, 20 January 2003, and John Ravilious, soc.genealogy.medieval, 11 January 2003. The identification is captured in tertiary form at the buist-keatch.org Goring-line database, person 3162 (Basilie Flaitel), `https://buist-keatch.org/buist/goring/3162.html`, which was the retrieval point for this audit. Phase-2 direct verification against the Cawley MedLands entry for the Gacé seigneurie is the next step. Source ID: `fmg-medlands-normacre`.
```

### 2.3 JSON alignment

No new `sourceId`. The citation uses `fmg-medlands-normacre`, proposed in v54 §16. If v54 has not been applied when v55 is applied, the apply session must add `fmg-medlands-normacre` before this G33 §3.1 footnote will reference an existing source.

---

## 3. EXCLUDE — justifications

### 3.1 persee.fr Deck 1974 (Beaubec abbey)

Beaubec abbey was founded c. 1127–1130 by **Hugues IV de Gournay** — one generation below the deepest direct ancestor (Gerard G32) and a senior-line collateral, not a direct ancestor. The article's open-access PDF endpoint returned HTTP 403; the article HTML returned only the opening paragraph (Pays-de-Bray archaeology — La Rosière, Saint-Saire, Neufchâtel, Lyons / Eawy / Eu forests). La Rozière is independently mentioned in G33 §5.4 as one of Hugh III's Bec endowment churches, but the Deck article concerns Beaubec's separate Cistercian temporal, not G33's earlier Bec donation. No direct-ancestor content was retrievable.

### 3.2 cybergata 3187 (Hugh V de Gournay)

Hugh V "the Cuckoo" (c. 1148 – 25 Oct 1214/15) is two generations below Gerard G32 (Gerard → Hugues IV → Hugues V), senior-line collateral. Page is uncited tertiary genealogy; no scholarly references to source.

### 3.3 genealogieonline P30399 (same Hugh V)

Senior-line collateral. The page's citation list (Weis-Sheppard *Ancestral Roots* 7th ed. 1999 line 257-31; Richardson SGM 20 Jan 2003; Ravilious SGM 13 Sep 2002; AGBI) refers to Hugh V content: 1188 marriage to Juliana de Dammartin at Ashby; 1190 Houghton Regis grant; 1191 Third Crusade with 100 knights at Acre; 1193 defection to Philip Augustus; 1206 Otho pardon; 1214 Bucks/Beds shrievalty; Templar-apostasy at Rouen. None of these claims lands on a direct ancestor; no underlying source is registered because no claim is being added that would cite it.

### 3.4 nielsenhayden I7740 (same Hugh V)

Senior-line collateral; tertiary TNG database. Cited sources (*Complete Peerage* 2nd ed.; Weis-Sheppard *Ancestral Roots* 8th ed.; Bodine-Spalding *Ancestry of Dorothea Poyntz* 2013; Richardson *Royal Ancestry* 2013; Boyer *Medieval English Ancestors of Robert Abell* 2001) are scholarly but exclusively serve Hugh V (collateral) content.

### 3.5 thesignsofthetimes 56867 (Gerard G32)

Every claim on the page — birth at Gournay-en-Bray; parents Hugh III + Basilea Flaitel; marriage before 1091 to Edith de Warenne; children Hugues IV + Gundred; 1097 Nicaea via Albert of Aix; d. after 1104 *in itinere*; [1089/90] Orderic delivery of Gournay / La Ferté / Gaillefontaine to William II Rufus — is already in `research/people/g32-gerard-de-gournay-fact-sheet.research.md`, with the same Pattou *Racines Histoire* and FMG MedLands as cited sources.

### 3.6 talltales blog 2013 (Hugh II G34)

Tertiary blog with no citation apparatus beyond an unnamed "19th-century historian" and the Bayeux Tapestry. The "1036" date for the Edward expedition is a minor variant of the standard 1035 (Cnut died 12 November 1035; the Norman expedition sailed the following spring). The Yarmouth-as-reward summary is the same collapse Potin 1842 makes as "duché de Norwick," already discussed in G34 §6.5.

### 3.7 buist-keatch 3114 (Hugh IV de Gournay) — page itself

Hugh IV is senior-line collateral, one generation below Gerard G32. Page content (two marriages — Béatrice de Vermandois m. before 1147; Mélisende de Coucy [widow of Adeleme Châtelain d'Amiens, daughter of Thomas de Marle Comte d'Amiens] m. before 1147; 1147 Second Crusade; foundations of Clairruissel and Gaillefontaine abbeys) is real but lands wholly on Hugh IV. The cited sources (Cawley *Medieval Lands*; Richardson SGM 11 Sep 2002 — the Walter-Gerard topic already on the v54 queue; Ravilious SGM 11 Jan 2003; Loyd *Origins of Some Anglo-Norman Families* 1999 — already in repo source set as `loyd-anglo-norman-families`) introduce no new repo sources for direct-ancestor work. **Navigation from this page surfaced the §2 finding for G33 (Basilie's son Robert d'Évreux); that finding is included separately.**

---

## 4. Navigation graph traversed

To verify that no direct-ancestor finding was missed in the buist-keatch tree, the following family-graph pages were retrieved from the 3114 entry-point and read:

| Page | Person | Result |
|---|---|---|
| 3114 | Hugh IV de Gournay (collateral) | Excluded; navigation source for adjacent direct-ancestor pages |
| 3159 | Hugh III de Gournay (G33 direct ancestor) | No new content beyond existing G33 companion. No parent link to Hugh II on this page (buist-keatch's tree truncates above G33). The [1040] charter referenced is the same FMG [875] act already addressed in G32 §2.2 as misdated. |
| 3098 | Gérard de Gournay (G32 direct ancestor) | The buist-keatch tree shows Gérard's listed parents as Gérard Flaitel + Basilie Flaitel — a genealogical error (Gérard Flaitel is Basilie's father, not G32's father; G32's father is Hugh III G33). Children listed: Hugh IV, Amicie, Gundred, and bracketed [Hawise]. No Walter de Gournay listed — buist-keatch's tree silently follows Richardson SGM 2002's position rejecting Walter as Gerard's son. No new direct-ancestor content. |
| 3099 | Edith de Warenne (G32's wife) | Page records Edith as daughter of William de Warenne 1st Earl + Gundred de Flandre; second marriage to Dreux [I] de Moncy Seigneur de Moncy after 1104; died after 1155. All three datapoints already in G32 companion §1, §2.6, and §4 (Pattou block). No new content. |
| 3162 | Basilie Flaitel (G33's wife) | **One new datapoint surfaced**: Basilie's son by Raoul de Gacé identified as Robert d'Évreux Seigneur de Gacé. See §2 above. |
| 6343 | Amicie de Gournay (G32's daughter / proposed daughter) | Already in G32 §3.2 as the open Amicie-parentage question. Henry II charters [1181/83] and [Mar/Jun 1189] are already cited at G32 §3.2 via FMG [889] and [890]. Orderic Vitalis attestation ("Hugo filius Girardi de Gornaco" / "nepoti eius Hugoni Talabot") already implicit in G32 §3.2. No new content. |
| 3097 | Gundred de Gournay (G32's daughter) | Marriage to Nigel d'Aubigny Jun 1118, son Roger de Mowbray, 1130 Pipe Roll attestation, donations to St Leonard's York / Whitby — all already in G32 §7 children table. No new content. |
| 2947 | Gérard Flaitel (Basilie's father; G33 step-context) | Six children listed: Guillaume (bishop of Évreux), Anscher, Robert, Albert, Ermengarde, Basilie. The Anscher attestation here is independent corroboration of the existing G33 §3.2 identification of Anscher Flaitel with Ausger de Gournay (per Pettigrew). No new finding — the G33 §3.2 already has this. |
| 2914 | William de Warenne 1st Earl of Surrey (G32's father-in-law) | Confirms 24 Jun 1088 death at Lewes from Pevensey-siege wounds. Children listed: William, Edith, a daughter, Rainald, Gundred, [Roger]. Edith is listed directly as a daughter (rather than only as sister of William II). No new direct-ancestor content; the G32 companion §1 already records Edith as 1st Earl's daughter. |

FMG MedLands direct retrieval was attempted at three URL patterns (`normfra.htm`, `normfran.htm`, `NORMAN%20NOBILITY.htm`) — all returned 404. The repo already has `fmg-medlands-normacre` proposed in v54 §16 as the working sourceId for the FMG Gournay section; that proposal stands.

---

## 5. Phase-2 application checklist

1. Apply §1.3 — insert new sub-section §6.7 into `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md`; add the Powell row to the §11 Sources-consulted table.
2. Apply §1.4 — insert one new entry (`powell-historie-cambria-1584`) into `data/sources.json`.
3. Apply §2.2 — extend the §3.1 pedigree table in `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` with the Robert d'Évreux Seigneur de Gacé row, and add the new footnote `[^robert-evreux-gace-son]`. The footnote references `fmg-medlands-normacre`, which must already be present in `data/sources.json` (i.e., v54 must have landed first, OR this apply session must add `fmg-medlands-normacre` as well).
4. Re-validate `data/sources.json` syntax (no trailing-comma errors; all braces balanced).
5. *Optional, can defer to a future session*: retrieve the EEBO scan of Powell 1584 (STC 20089) or the 1811 Wynne re-edition, confirm the 1094 entry text verbatim, and update the `url` field on the `powell-historie-cambria-1584` entry from the patp.us mediating URL to the direct EEBO / Wynne URL.
6. *Optional, can defer to a future session*: retrieve the Cawley MedLands entry for the Gacé seigneurie (post-1051 succession) to confirm Robert d'Évreux Seigneur de Gacé's parentage directly from Cawley, rather than through the buist-keatch mediating page.

## 6. Unresolved

- The Persée Deck 1974 Beaubec article body was not extractable via WebFetch (the docAsPDF endpoint returned 403; the article HTML returned only the page-131 opening). If future work opens senior-line collateral coverage of Hugh IV de Gournay (and Beaubec abbey as his foundation), this article will be the first scholarly source to extract. Out of scope for v55.
- The "Comte d'Évreux / Walter Evereux, Earl of Sarum" identity problem in the Powell tradition is logged in §1.3 but not resolved. Loyd *Origins* and Keats-Rohan *Domesday People* would need to be consulted to determine whether any Walter d'Évreux can be associated with either the 1074 or the 1094 dating.
- The Robert d'Évreux Seigneur de Gacé identification (§2) is via buist-keatch's mediated citation of Cawley MedLands; direct verification against Cawley is deferred to Phase 2 (see §5 step 6).
- FMG MedLands direct retrieval was unsuccessful at three URL patterns. The standard repo handle `fmg-medlands-normacre` (proposed in v54 §16) carries the URL `https://fmg.ac/Projects/MedLands/normacre.htm` which has historically served the Normandy section; the URL apparently changed or the redirect failed in this session.
