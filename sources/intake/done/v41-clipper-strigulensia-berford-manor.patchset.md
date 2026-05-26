# Intake patchset v41 — Clipper 1895 (Lester Gurney), Ormerod Strigulensia (Thomas son of Hugh de Gournay), Blomefield/BHO Berford's Manor (Edmund Gurney feoffee)

**Prepared:** 2026-05-16
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Source materials:** `sources/intake/new/NewIntake_Batch1.md`, `sources/intake/new/Screenshot 2026-04-20 204336.png`, `sources/intake/new/uc1--b751193-139-1776799225.txt`.

## Scope

Three independent items, one patchset. Each promotes a single new sourceId, lands a substantive finding in a research file, and (where the finding is durable) touches a fact-sheet timeline or narrative line. Validations stay thin; corpus supplements hold short verbatim extracts only.

- **Item 1 — New York Clipper, 24 August 1895, Patchogue "Little Lord Fauntleroy" cast notice.** Adds Lester Gurney (G05) to the Patchogue summer-theatrical cast of 7 August 1895, three years earlier than the previously documented *May Blossom* appearance of August 1898.
- **Item 2 — Ormerod, *Strigulensia* (1861), p. 103.** Preserves a 4 June 1329 demise from Thomas ap Adam to "Thomas son of Hugh de Gournay" of the manor of East Harptree, the manor of Gorste near Strigoil, the vill of Netherwere, and rents in Panbere and Willewe. Materially relevant to the Somerset Gournay collateral file and to the disputed parentage of Sir Thomas de Gournay the regicide.
- **Item 3 — Blomefield, *Topographical History of Norfolk*, vol. 5, pp. 33–39 (BHO transcription).** Names Edmund Gournay (G23) as one of four De la Pole feoffees of Berford's Manor at Cringleford, with John le Latimer of Norwich, William de Boyton, and Thomas Spynk, c. 1370.

---

## 1. `data/sources.json`

### 1.1 Metadata

Set:

```json
"lastUpdated": "2026-05-16"
```

### 1.2 Add source entry — New York Clipper, August 1895 (Patchogue Lord Fauntleroy notice)

Insert near other Gurney-related newspaper or theatrical sources:

```json
    "nyclipper-1895-08-patchogue-fauntleroy": {
      "shortTitle": "New York Clipper, August 1895 — Patchogue Lord Fauntleroy notice",
      "citation": "\"Mabel Walsh is to appear in the title role.\" The New York Clipper, vol. 43 (August 1895). Internet Archive item clipper43-1895-08.",
      "archive": "Internet Archive scan of The New York Clipper, vol. 43, August 1895",
      "url": "https://archive.org/details/clipper43-1895-08",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/nyclipper-1895-08-patchogue-fauntleroy.md",
      "mediaPath": "sources/media/nyclipper-1895-08-patchogue-fauntleroy/",
      "validationPath": "sources/validations/nyclipper-1895-08-patchogue-fauntleroy.md",
      "notes": "Trade-paper notice announcing a Mabel Walsh production of Little Lord Fauntleroy at the New Lyceum Theatre, Patchogue, Long Island, for 7 August 1895. Names Lester Gurney in the supporting company alongside J. D. Walsh, Charles Drake, Jerome Cammeyer, George Watson, Frank Heald, Annie L. Walsh, and Anna Morton. Earliest documented stage appearance for Lester Sawyer Gurney (G05); complements the September 1895 Clipper Helene Ransome / Margaret Mather notice already cited on the G05 fact sheet."
    },
```

### 1.3 Add source entry — Ormerod, *Strigulensia* (1861)

Insert near other 19th-century Gournay antiquarian sources:

```json
    "ormerod-strigulensia-1861": {
      "shortTitle": "Ormerod, Strigulensia (1861)",
      "citation": "Ormerod, George. Strigulensia: Archaeological Memoirs Relating to the District Adjacent to the Confluence of the Severn and the Wye. London: T. Richards, 1861.",
      "archive": "HathiTrust Digital Library / University of California copy (uc1.$b751193)",
      "url": "https://hdl.handle.net/2027/uc1.$b751193",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/ormerod-strigulensia-1861-thomas-de-gournay-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/ormerod-strigulensia-1861.md",
      "notes": "Antiquarian topographic study of the lower Severn/Wye district. Page 103 catalogues Thomas ap Adam's alienations of his maternal inheritance. Item 4 of that list records a 4 June 1329 (3 Edward III) demise for life from Thomas ap Adam to 'Thomas son of Hugh de Gournay' of rents in Panbere and Willewe, the vill of Netherwere, the manor of Gorste near Strigoil (Chepstow), and the manor of East Harptree, in exchange for Thomas ap Adam's life interest in the manor of Dunheved, Somerset, and 'la Hamele de Beteslè, ensemblement ove le Passage' (the hamlet of Beachley with the Severn passage). Confirmed in Chancery 24 June 1329. Cites Rot. Claus. M. 18. Primary-derived datum naming the father of this Thomas de Gournay as Hugh, distinct from Pettigrew's Anselm → Thomas of Inglishcombe → Sir Thomas the regicide reconstruction."
    },
```

### 1.4 Add source entry — Blomefield (BHO transcription), Norfolk vol. 5 pp. 33–39 (Cringleford / Berford's Manor)

The umbrella `blomefield-norfolk` source already exists. Add a focused page-level entry for the Cringleford / Berford's Manor extract used in this patchset, modeled on existing per-volume Blomefield extract entries:

```json
    "blomefield-norfolk-vol5-pp33-cringleford-berford": {
      "shortTitle": "Blomefield, Norfolk vol. 5 (BHO) — Cringleford, Berford's Manor",
      "citation": "Blomefield, Francis. An Essay Towards a Topographical History of the County of Norfolk. Vol. 5. London: W. Miller, 1806, pp. 33–39, \"Cringleford\" / \"Berford's Manor.\"",
      "archive": "British History Online transcription",
      "url": "https://www.british-history.ac.uk/topographical-hist-norfolk/vol5/pp33-39",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/blomefield-norfolk-vol5-pp33-cringleford-berford.md",
      "mediaPath": null,
      "validationPath": "sources/validations/blomefield-norfolk-vol5-pp33-cringleford-berford.md",
      "notes": "Page-level Blomefield/BHO extract for Cringleford's Berford's Manor descent. Records that after the De la Poles obtained the manor in trust, they settled it on Edmund Gourney, William de Boyton, Thomas Spynk, and John le Latimer of Norwich as feoffees; the manor extended into Hethersett, Eaton, Earlham, Little Melton, Colney, and Cringleford watermill; by 1381 John le Latimer was sole lord with view of frankpledge, weyf, and strey; in the same year Gournay and the other De la Pole feoffees released their right to him. Adds Edmund Gurney (G23) to the documented De la Pole / Latimer feoffee network in the 1370s."
    },
```

---

## 2. New corpus / validation / media files

### 2.1 Create `sources/corpus_supplement/nyclipper-1895-08-patchogue-fauntleroy.md`

```markdown
# New York Clipper, August 1895 — Patchogue "Little Lord Fauntleroy" notice

**Source ID:** `nyclipper-1895-08-patchogue-fauntleroy`
**Citation:** *The New York Clipper*, vol. 43 (August 1895). Internet Archive item `clipper43-1895-08`.

## Extract

> Mabel Walsh is to appear in the title role in a performance of "Lord Fauntleroy," to be given at the New Lyceum Theatre, Patchogue, L. I., on Aug. 7, by a company composed, beside the little star, of J. D. Walsh, Charles Drake, Jerome Cammeyer, George Watson, Frank Heald, Lester Gurney, Annie L. Walsh and Anna Morton.

Transcribed from the user-supplied page-image screenshot (`sources/media/nyclipper-1895-08-patchogue-fauntleroy/clipper-1895-08-fauntleroy.png`). Spelling and capitalization follow the printed clipping.

## Identification

"Lester Gurney" in this cast list is Lester Sawyer Gurney (G05), then resident in Patchogue summers and already part of the village's theatrical-colony circle. The same volume of the *Clipper* (September 1895) carries the separate Helene Ransome / Margaret Mather company notice already cited on the G05 fact sheet.
```

### 2.2 Create `sources/corpus_supplement/ormerod-strigulensia-1861-thomas-de-gournay-extract.md`

```markdown
# Ormerod, Strigulensia (1861) — Thomas de Gournay extract

**Source ID:** `ormerod-strigulensia-1861`
**Citation:** George Ormerod, *Strigulensia: Archæological Memoirs Relating to the District Adjacent to the Confluence of the Severn and the Wye* (London: T. Richards, 1861), p. 103.
**Scope:** page 103, "Ap Adam of Beverstone," items 1–6 of the Thomas ap Adam alienation list; Gournay material is item 4.

## Extract — Thomas ap Adam alienations, p. 103

Item 4 of Ormerod's catalogue of Thomas ap Adam's grants:

> 4. June 4, 3 Edw. III, 1329. Demise for life "apres plusieurs debatz et dissentions" — "pour bone pees et quiete" to Thomas son of Hugh de Gournay, for life, of rents in Panbere and Willewe, also of the vill of Netherwere, the manor of Gorste near Strogoil, and the manor of East Harptre, the grantor receiving back in consideration of this, and of a payment in money, a previously granted life-interest in the manor of Dunheved, co. Somerset, and in "la Hamele de Beteslè, ensemblement ove le Passage." (Confirmation in Chancery, June 24.)

Cited authority: Rot. Claus. M. 18, in dorso, confirmed in Chancery.

Context (items 1–3, 5–6): the same series records Thomas ap Adam's parallel alienations of Monewdon (Suffolk) to Isabella de Hastings, Puriton to John de Wallonia, Penyard / La Lee / Esthamptonet to John Inge, Kings Weston and Ailberton (Elberton) to Maurice de Berkeley, and Beverston and Overe to Thomas de Berkeley and his wife Margaret.

## Identification

"Thomas son of Hugh de Gournay" is the recipient. Strogoil = Striguil = Chepstow. Beteslè = Beachley, the Severn passage point. Gorste near Strogoil is a Gurney/Gournay holding in the Chepstow march. East Harptree is the principal Somerset Gournay seat. The parentage clause — "son of Hugh" — is the primary-derived datum that materially affects the Pettigrew reconstruction (which derives Sir Thomas de Gournay the regicide from Anselm → Thomas of Inglishcombe → Thomas the regicide, with no Hugh in the immediate paternal line). See `research/places/somerset-gournay-collateral.md` for discussion.
```

### 2.3 Create `sources/corpus_supplement/blomefield-norfolk-vol5-pp33-cringleford-berford.md`

```markdown
# Blomefield, Norfolk vol. 5 (BHO) — Cringleford / Berford's Manor extract

**Source ID:** `blomefield-norfolk-vol5-pp33-cringleford-berford`
**Citation:** Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. 5 (London: W. Miller, 1806), pp. 33–39, "Cringleford" / "Berford's Manor."
**URL:** https://www.british-history.ac.uk/topographical-hist-norfolk/vol5/pp33-39

## Extract — Edmund Gournay as De la Pole feoffee, c. 1370

After tracing the Berford / De la Pole descent of the manor, Blomefield writes that following the 1370 release by the Berford co-heirs:

> by which means it was absolutely vested in the De la Poles, who settled it soon after on Edmund Gourney, Will. de Boyton, Tho. Spynk, and John le Latimer of Norwich, when it extended into Hethersete, Eaton, Erlham, Little-Melton, Colneye, and Cringleford watermill belonged to it; in 1381, John le Latimer was sole lord, and had view of frankpledge, weyf, and strey, belonging to his manor of Cringleford and Surlingham; and the same year, Gournay and the other feoffees of the Poles, released all right to him.

## Identification

"Edmund Gourney" / "Gournay" in the 1370s De la Pole feoffee group is Edmund Gurney G23 of Harpley (c. 1340/50 – 1387), already documented as a long-serving feoffee for Norfolk magnates (e.g., the 1382 Close Rolls trust for John de Plays' manors of Feltwell and Mundford). The Berford's Manor settlement extends Edmund's documented trustee network southward from his Harpley / West Barsham / King's Lynn base into the Cringleford / Hethersett / Earlham cluster south-west of Norwich, and ties him directly to John le Latimer of Norwich — a connection worth tracking against Edmund's other Norwich and Norfolk principal-counsel work.
```

### 2.4 Create `sources/media/nyclipper-1895-08-patchogue-fauntleroy/clipper-1895-08-fauntleroy.png`

File operation: copy the user-supplied screenshot into the media folder. Source file:

```
sources/intake/done/Screenshot 2026-04-20 204336.png
```

Target file:

```
sources/media/nyclipper-1895-08-patchogue-fauntleroy/clipper-1895-08-fauntleroy.png
```

(The file moves were performed earlier in this audit; the screenshot already sits under `done/` rather than `new/` because the wider Batch 1 raw note was retained but the screenshot has been cleared from the active intake queue. Phase 2 should simply copy it into the new media folder using its current `done/` path.)

### 2.5 Create `sources/validations/nyclipper-1895-08-patchogue-fauntleroy.md`

```markdown
# Source validation — New York Clipper, August 1895 (Patchogue Lord Fauntleroy notice)

**Source ID:** `nyclipper-1895-08-patchogue-fauntleroy`

## Examined

User-supplied page-image clipping from *The New York Clipper*, vol. 43 (August 1895), reporting the 7 August 1895 Patchogue "Little Lord Fauntleroy" cast.

## Scope

Single column-paragraph clipping. Surrounding cast list and date verified against the screenshot only; the full *Clipper* page has not been re-read in this pass.

## Findings recorded in

- `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`
- `fact-sheets/g05-lester-sawyer-gurney-fact-sheet.md` (timeline + n15 update)

## Detailed execution trail

`sources/intake/processed/v41-clipper-strigulensia-berford-manor.patchset.md`
```

### 2.6 Create `sources/validations/ormerod-strigulensia-1861.md`

```markdown
# Source validation — Ormerod, Strigulensia (1861)

**Source ID:** `ormerod-strigulensia-1861`

## Examined

George Ormerod, *Strigulensia* (London: T. Richards, 1861), p. 103, items 1–6 of the Thomas ap Adam alienation list. HathiTrust copy (`uc1.$b751193`).

## Scope

Page 103 only. Cited authority Rot. Claus. M. 18 (in dorso) not independently checked against the manuscript roll in this pass.

## Findings recorded in

- `research/places/somerset-gournay-collateral.md`

## Detailed execution trail

`sources/intake/processed/v41-clipper-strigulensia-berford-manor.patchset.md`
```

### 2.7 Create `sources/validations/blomefield-norfolk-vol5-pp33-cringleford-berford.md`

```markdown
# Source validation — Blomefield, Norfolk vol. 5 pp. 33–39 (Cringleford / Berford's Manor)

**Source ID:** `blomefield-norfolk-vol5-pp33-cringleford-berford`

## Examined

British History Online transcription of Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. 5, pp. 33–39, "Cringleford" / "Berford's Manor."

## Scope

Single descent paragraph for Berford's Manor; the surrounding manorial descent for Cringleford as a whole was read but not re-extracted in this pass. The print edition has not been re-checked against the BHO transcription.

## Findings recorded in

- `research/people/g23-edmund-gurney-fact-sheet.research.md`
- `fact-sheets/g23-edmund-gurney-fact-sheet.md` (timeline / minor holdings update)

## Detailed execution trail

`sources/intake/processed/v41-clipper-strigulensia-berford-manor.patchset.md`
```

---

## 3. Research file edits

### 3.1 `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`

Add a new working-notes subsection above the `## Research Appendix` heading:

```markdown
### Patchogue stage debut, August 1895 — *Little Lord Fauntleroy*

*The New York Clipper* for August 1895 announced that Mabel Walsh would appear in the title role of *Little Lord Fauntleroy* at the New Lyceum Theatre, Patchogue, on 7 August, with a supporting company of J. D. Walsh, Charles Drake, Jerome Cammeyer, George Watson, Frank Heald, **Lester Gurney**, Annie L. Walsh, and Anna Morton.[^g05-clipper-fauntleroy-1895] This is the earliest documented stage appearance for Lester Sawyer Gurney himself, three summers before the 1898 *May Blossom* cast in which he and his son shared the stage. It pushes the Gurney household's hands-on involvement in the Patchogue theatrical colony back into the same season as Mrs. Lester Gurney's documented presence at Winona's hop (July 1895) and Helene Ransome's separately announced engagement with Margaret Mather's company (September 1895 *Clipper*), and reframes the 1898 *May Blossom* appearance as the continuation of a habit rather than a one-off.

[^g05-clipper-fauntleroy-1895]: *The New York Clipper*, vol. 43 (August 1895), Patchogue Lord Fauntleroy cast notice, [Internet Archive scan](https://archive.org/details/clipper43-1895-08); user-supplied page-image clipping. Source ID: `nyclipper-1895-08-patchogue-fauntleroy`.
```

### 3.2 `fact-sheets/g05-lester-sawyer-gurney-fact-sheet.md`

#### 3.2.1 Narrative line — extend the existing Patchogue paragraph

Use `str_replace` on this exact sentence in the Patchogue narrative paragraph:

`old_str`:
```
The family appeared in village social notices as well: in 1895 Mrs. Lester Gurney led the opening march at a Wednesday-evening hop at Winona’s, and in 1898 father and son shared the stage in the local production of <em>May Blossom</em>.
```

`new_str`:
```
The family appeared in village social notices as well: in 1895 Mrs. Lester Gurney led the opening march at a Wednesday-evening hop at Winona’s; Lester himself was in the Patchogue cast of <em>Little Lord Fauntleroy</em> at the New Lyceum Theatre on 7 August 1895, supporting Mabel Walsh in the title role; and in 1898 father and son shared the stage in the local production of <em>May Blossom</em>. <sup class="fn"><a href="#n15b" id="ref-15b">15b</a></sup>
```

#### 3.2.2 Add the matching footnote

`str_replace`:

`old_str`:
```
  <li id="n15"><a href="https://history.pmlib.org/patchoguemedfordareahistory/patchogue/historicperiods/1866-1897">Patchogue – 1866–1897</a>, Celia M. Hastings Local History Room; <em>Brooklyn Daily Eagle</em>, 21 July 1895, p. 14; <em>Brooklyn Daily Eagle</em>, 7 August 1898, p. 12; <a href="https://www.britannica.com/technology/phaeton-carriage">Encyclopaedia Britannica, “phaeton”</a>; <em>Brooklyn Daily Eagle</em>, 16 August 1898, p. 11. <a class="citation-back" href="#ref-15">↩</a></li>
```

`new_str`:
```
  <li id="n15"><a href="https://history.pmlib.org/patchoguemedfordareahistory/patchogue/historicperiods/1866-1897">Patchogue – 1866–1897</a>, Celia M. Hastings Local History Room; <em>Brooklyn Daily Eagle</em>, 21 July 1895, p. 14; <em>Brooklyn Daily Eagle</em>, 7 August 1898, p. 12; <a href="https://www.britannica.com/technology/phaeton-carriage">Encyclopaedia Britannica, “phaeton”</a>; <em>Brooklyn Daily Eagle</em>, 16 August 1898, p. 11. <a class="citation-back" href="#ref-15">↩</a></li>
  <li id="n15b"><em>The New York Clipper</em>, vol. 43 (August 1895), Patchogue "Little Lord Fauntleroy" cast notice naming Mabel Walsh, J. D. Walsh, Charles Drake, Jerome Cammeyer, George Watson, Frank Heald, Lester Gurney, Annie L. Walsh, and Anna Morton, performance at the New Lyceum Theatre, Patchogue, 7 August 1895; <a href="https://archive.org/details/clipper43-1895-08">Internet Archive scan</a>. Source ID: <code>nyclipper-1895-08-patchogue-fauntleroy</code>. <a class="citation-back" href="#ref-15b">↩</a></li>
```

#### 3.2.3 Timeline insertion

Use `str_replace` on the existing timeline row block:

`old_str`:
```
      <tr><td>1895–1898</td><td>Visible in Patchogue summer social life and theatrical circles.</td></tr>
```

`new_str`:
```
      <tr><td>7 August 1895</td><td>In the Patchogue cast of <em>Little Lord Fauntleroy</em> at the New Lyceum Theatre, supporting Mabel Walsh in the title role.</td></tr>
      <tr><td>1895–1898</td><td>Visible in Patchogue summer social life and theatrical circles.</td></tr>
```

### 3.3 `research/places/somerset-gournay-collateral.md`

Add a new subsection immediately after the existing paragraph that discusses Sir Thomas de Gournay the regicide and his descent (the paragraph beginning "Robert de Gournay, Eva's son, bore paly of six…" and the lines that follow on the regicide and his sons). Place it before the existing `## Place / record context` or comparable next-section heading; if no such heading exists in the immediate area, append after the closest paragraph that discusses Sir Thomas's lineage.

```markdown
### Ormerod 1861: the 1329 Beverston demise to "Thomas son of Hugh de Gournay"

George Ormerod's *Strigulensia* (1861) catalogues the alienations by which Thomas ap Adam of Beverston disposed of his maternal inheritance after coming of age. Item 4 of that list records a demise for life, dated 4 June 1329 and confirmed in Chancery on 24 June, from Thomas ap Adam to "Thomas son of Hugh de Gournay" of rents in Panbere and Willewe, the vill of Netherwere, the manor of Gorste near Strogoil (Striguil / Chepstow), and the manor of East Harptree, in consideration of money and the return to Thomas ap Adam of a previously granted life-interest in the manor of Dunheved, Somerset, and "la Hamele de Beteslè, ensemblement ove le Passage" — the hamlet of Beachley with the Severn passage point.[^ormerod-strigulensia-1329-east-harptree] The deed framing — *apres plusieurs debatz et dissentions, pour bone pees et quiete* — suggests the transaction settled an active dispute rather than a simple grant. Ormerod cites Rot. Claus. M. 18, in dorso, confirmed in Chancery.

The Gournay parentage clause is the point of interest. The transaction places East Harptree, the principal Somerset Gournay seat, in the life-tenure of a Thomas de Gournay whose father is named as Hugh. The Pettigrew reconstruction summarized above derives Sir Thomas de Gournay the regicide from Anselm → Thomas of Inglishcombe → Thomas the regicide, with no Hugh in the immediate paternal line; the regicide himself was active and at large in 1329 between Edward II's murder (1327) and his own capture (1331/2). Several readings of Ormerod's 1329 "Thomas son of Hugh de Gournay" are possible and each is worth pursuing rather than collapsing prematurely:

- If "Thomas son of Hugh" is in fact Sir Thomas the regicide, Ormerod's clause is direct primary-derived testimony that the regicide's father was a Hugh, not Pettigrew's Thomas of Inglishcombe. That would be a substantial correction to the standard Somerset reconstruction.
- If "Thomas son of Hugh" is a different contemporary Thomas de Gournay holding East Harptree from Thomas ap Adam during the regicide's flight years, the deed identifies a separate Gournay heir not previously visible in the Somerset chronology; the regicide's fall would still have to be reconciled with the family's continued possession of East Harptree by another Thomas.
- If the regicide's son Matthew (G29) or another close kinsman is being placed in this life-tenure as proxy for the regicide himself, the formal clause "son of Hugh" still has to be explained.

The 8 Edward III (1334) restoration of Farington, Inglescombe, and West Harptree to Joan, widow of Sir Thomas the regicide, already in this file, sits five years later than the Ormerod demise and does not directly resolve the question. The 1329 deed deserves a separate working pull from the Close Roll and Patent Roll evidence for Edward II and early Edward III before it is folded into the published Somerset narrative.

[^ormerod-strigulensia-1329-east-harptree]: George Ormerod, *Strigulensia: Archæological Memoirs Relating to the District Adjacent to the Confluence of the Severn and the Wye* (London: T. Richards, 1861), p. 103, item 4 of the Thomas ap Adam alienation list, citing Rot. Claus. M. 18 (in dorso), confirmation in Chancery 24 June 3 Edw. III; [HathiTrust copy](https://hdl.handle.net/2027/uc1.$b751193). Source ID: `ormerod-strigulensia-1861`.
```

### 3.4 `research/people/g23-edmund-gurney-fact-sheet.research.md`

Add a new working-notes subsection. The existing file uses date-stamped subsections (e.g., "2026-04-18 — …") inside an open "Working notes" area; if the file's structure is unchanged from the read at preparation time, append the block beneath the most recent dated entry. If the file's structure has been refactored, place this block under whatever current heading covers Edmund's trustee / feoffee activity for Norfolk magnates.

```markdown
### Berford's Manor, Cringleford — De la Pole feoffee, c. 1370

Blomefield's Norfolk volume 5 records that after the Berford co-heirs released their rights in 1370, Berford's Manor at Cringleford was "absolutely vested in the De la Poles, who settled it soon after on Edmund Gourney, Will. de Boyton, Tho. Spynk, and John le Latimer of Norwich" as feoffees, the manor then extending into Hethersett, Eaton, Earlham, Little Melton, Colney, and the Cringleford watermill.[^blomefield-cringleford-berford] By 1381 John le Latimer of Norwich was sole lord with view of frankpledge, weyf, and strey, and Edmund Gurney with the other De la Pole feoffees released all right to him in the same year.[^blomefield-cringleford-berford]

This is independent of the 1382 Close Rolls trust by John de Plays already documented here, and it predates it. It places Edmund in a De la Pole–linked Norfolk feoffee network in the early 1370s — the De la Poles being one of the dominant late-fourteenth-century magnate houses, with the merchant William de la Pole's son Michael soon to be created earl of Suffolk under Richard II — and ties him directly to John le Latimer of Norwich, who already appears in the manor of Berford's Manor before becoming sole lord in 1381. The Cringleford / Hethersett / Earlham cluster sits south-west of Norwich, broadening Edmund's documented service footprint beyond his Harpley, West Barsham, Hardingham, and King's Lynn principal-counsel work.

[^blomefield-cringleford-berford]: Francis Blomefield, *An Essay Towards a Topographical History of the County of Norfolk*, vol. 5 (London: W. Miller, 1806), pp. 33–39, "Cringleford" / "Berford's Manor"; [British History Online transcription](https://www.british-history.ac.uk/topographical-hist-norfolk/vol5/pp33-39). Source ID: `blomefield-norfolk-vol5-pp33-cringleford-berford`.
```

### 3.5 `fact-sheets/g23-edmund-gurney-fact-sheet.md`

Light touch only. Find the existing children / holdings or chronology section and insert one timeline row alongside the existing trustee references. The fact sheet structure was read at preparation time; use whichever of the following matches the current file:

- **If the fact sheet has a `<table class="fact-timeline-table">` block**, insert a row consistent with the existing date conventions:

```html
      <tr><td>c. 1370</td><td>Named as one of four De la Pole feoffees of Berford's Manor in Cringleford, with William de Boyton, Thomas Spynk, and John le Latimer of Norwich; released his right to John le Latimer in 1381. <sup class="fn"><a href="#nXX" id="ref-XX">XX</a></sup></td></tr>
```

- **If the fact sheet has a `Holdings` table** with rows like the existing Feltwell / Mundford trust row, insert:

```html
      <tr><td>Berford's Manor, Cringleford (Norfolk)</td><td>c. 1370–1381 (feoffee)</td><td>De la Pole feoffee with William de Boyton, Thomas Spynk, and John le Latimer of Norwich; released to John le Latimer in 1381. <sup class="fn"><a href="#nXX" id="ref-XX">XX</a></sup></td></tr>
```

In either case, add a matching footnote in the citation list using the next available footnote number:

```html
  <li id="nXX">Francis Blomefield, <em>An Essay Towards a Topographical History of the County of Norfolk</em>, vol. 5 (London: W. Miller, 1806), pp. 33–39, "Cringleford" / "Berford's Manor"; <a href="https://www.british-history.ac.uk/topographical-hist-norfolk/vol5/pp33-39">British History Online</a>. Source ID: <code>blomefield-norfolk-vol5-pp33-cringleford-berford</code>. <a class="citation-back" href="#ref-XX">↩</a></li>
```

If the fact sheet has neither a timeline nor a holdings table at the time of application, drop the fact-sheet edit and rely on the research-companion entry alone — do not invent new structural sections to host the row.

---

## 4. Archive / cleanup operations

### 4.1 Move `NewIntake_Batch1.md` to `done/`

`NewIntake_Batch1.md` has now been promoted in full. The British Archivist Francis Gurney biography (Item 2) was covered earlier under `british-archivist-bernau-1913`; the BHO vol. 8 *Gourney's Manor* page (Item 4) was covered by v06 and downstream research/places work; this patchset covers Items 1 and 3.

File operation:

```
git mv "sources/intake/new/NewIntake_Batch1.md" "sources/intake/done/NewIntake_Batch1.md"
```

### 4.2 Move the Lester Gurney screenshot into media

Already located under `sources/intake/done/Screenshot 2026-04-20 204336.png`. Copy (not move) into the new media folder so the screenshot remains traceable from its original intake path; Phase 2 may then re-evaluate whether to retain the `done/` copy.

```
mkdir -p sources/media/nyclipper-1895-08-patchogue-fauntleroy
cp "sources/intake/done/Screenshot 2026-04-20 204336.png" sources/media/nyclipper-1895-08-patchogue-fauntleroy/clipper-1895-08-fauntleroy.png
```

---

## 5. Unresolved

- The Ormerod 1329 demise is presented in the Somerset collateral file with three alternative readings rather than a single resolution. A targeted pull of Rot. Claus. M. 18 (3 Edw. III, in dorso) is the natural next step but is out of scope for this intake.
- The fact-sheet edit for G23 is conditional on the current structure of `fact-sheets/g23-edmund-gurney-fact-sheet.md`. Phase 2 should follow the explicit branching instruction in §3.5 rather than invent a new structural section.
