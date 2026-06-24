**Done:** 2026-06-23 21:05 PT

# Patchset v116 — complementary BHO sources (Blomefield Hardingham extract; VCH Glos Gaunt's Hospital)

**Phase 1 draft. Supplemental to v115.** Adds two British History Online sources that corroborate / adjudicate findings already in the repo (per the standing direction: complementary, supportive, or conflict-resolving sources strengthen the research and should be retained, not skipped as "already covered").

- The **Blomefield vol. 10 Hardingham "Gurney's and Swathing's Manor"** extract was written **directly** to `sources/corpus_supplement/blomefield-norfolk-vol10-pp221-227-hardingham-swathing.md` (corpus = direct). It corroborates the Armstrong 1781 account of the same descent already in `research/places/hardingham.md`, and carries the **later** descent the companion did not yet record. SourceId `blomefield-norfolk` already exists.
- **VCH Gloucestershire vol. 2 (Gaunt's Hospital)** adjudicates the Rudder-vs-Pettigrew founder conflict already documented in `research/places/somerset-gournay-collateral.md`. New sourceId added here.

---

## Item 1 — hardingham.md: cite the Blomefield extract and add the later Swathing descent

**Outcome:** promote. **Destination:** `research/places/hardingham.md`. SourceId `blomefield-norfolk` (existing).

### 1a — `str_replace` (extend the descent paragraph with the later, previously-unrecorded entries)

- old_string:
```
The same descent records the tenure becoming locally concrete: in 52 Henry III William de Swathyng held of John de Gurney a messuage, 54 acres of land, 3 acres of wood, free grinding at John's mill called Ravensholm, and associated fold-course and pasture rights. William de Gurnay claimed free warren in 15 Edward I; John Gurney was lord in 9 Edward II; and in 43 Edward III the manor was granted for life to Sir Hamon Felton with remainder to Edmund Gournay, Catherine his wife, and John their son in tail.[^blomefield-hardingham]
```
- new_string:
```
The same descent records the tenure becoming locally concrete: in 52 Henry III William de Swathyng held of John de Gurney a messuage, 54 acres of land, 3 acres of wood, free grinding at John's mill called Ravensholm, and associated fold-course and pasture rights. William de Gurnay claimed free warren in 15 Edward I; John Gurney was lord in 9 Edward II; and in 43 Edward III the manor was granted for life to Sir Hamon Felton with remainder to Edmund Gournay, Catherine his wife, and John their son in tail.[^blomefield-hardingham]

Blomefield carries the descent on past the Felton life-grant. In 17 Richard II Edmund Swathing and Catherine his wife conveyed the manor of Swathing by fine to Ralph Bateman (with reservations); in the 3rd of Henry IV John Gurney was lord; and in 1469 Thomas Gournay of West Barsham, senior, esquire, by his will bequeathed his Swathing rents and services — "which he had bought of Catherine Sturmer" — to be sold, before the manor passed to the Thwaytes family. Blomefield also records, out of chronological sequence in the printed descent, that "William Gourney, Esq. son of Thomas, and his wife, daughter of Sir William Calthorp, held the manor of Swathing and Hardingham in the 2d of Richard II"; the regnal date sits inconsistently with the surrounding entries and most plausibly telescopes the documented mid-fifteenth-century marriage of William Gurney IV (G19) to Anne Calthorpe rather than evidencing a distinct fourteenth-century Gurney–Calthorpe match. The Swathing rents Thomas Gournay had bought from Catherine Sturmer are the same bequest itemised in his 1469/70 West Barsham will.[^blomefield-hardingham][^blomefield-westbarsham-will-xref]
```

### 1b — `str_replace` (point the Blomefield footnote at the new corpus extract)

- old_string:
```
[^blomefield-hardingham]: Francis Blomefield, ["Mitford Hundred and Half: Hardingham and Flockthorp,"](https://www.british-history.ac.uk/topographical-hist-norfolk/vol10/pp221-227) in *An Essay Towards A Topographical History of the County of Norfolk*, vol. 10 (London, 1809), pp. 221-227, British History Online. Source ID: `blomefield-norfolk`.
```
- new_string:
```
[^blomefield-hardingham]: Francis Blomefield, ["Mitford Hundred and Half: Hardingham and Flockthorp,"](https://www.british-history.ac.uk/topographical-hist-norfolk/vol10/pp221-227) in *An Essay Towards A Topographical History of the County of Norfolk*, vol. 10 (London, 1809), pp. 221-227, British History Online. Verbatim extract of the "Gurney's and Swathing's Manor" descent at `sources/corpus_supplement/blomefield-norfolk-vol10-pp221-227-hardingham-swathing.md`; corroborates the Armstrong 1781 account of the same descent. Source ID: `blomefield-norfolk`.

[^blomefield-westbarsham-will-xref]: The 1469/70 will of Thomas Gurnay, senior, of West Barsham (proved Norwich 27 July 1471), with the bequest of the Swathing rents "which he bought of Catherine Sturmer," is extracted at `sources/corpus_supplement/blomefield-norfolk-vol7-pp42-47-west-barsham.md`. Source ID: `blomefield-norfolk`.
```

---

## Item 2 — sources.json: note the Hardingham extract under `blomefield-norfolk`

**Outcome:** promote. **Destination:** `data/sources.json` (notes field of the existing `blomefield-norfolk` entry).

`str_replace` in `data/sources.json`:

- old_string:
```
`blomefield-norfolk-vol7-pp53-65-east-barsham.md` (East Barsham, 1434-35 Thomas Gournay I feoffment and 1499 Earl of Oxford grant to William junior)."
```
- new_string:
```
`blomefield-norfolk-vol7-pp53-65-east-barsham.md` (East Barsham, 1434-35 Thomas Gournay I feoffment and 1499 Earl of Oxford grant to William junior); `blomefield-norfolk-vol10-pp221-227-hardingham-swathing.md` (Hardingham, the full 'Gurney's and Swathing's Manor' descent, Matthew de Gurnay temp. King John through the 1469 Thomas Gournay will and the Thwaytes succession)."
```

---

## Item 3 — somerset-collateral: VCH Glos resolves the Gaunt's Hospital founder conflict

**Outcome:** promote. **Destination:** `research/places/somerset-gournay-collateral.md`. **New source:** `vch-glos-vol2-gaunts-hospital` (Item 4 registers it + validation).

`str_replace` in `research/places/somerset-gournay-collateral.md`:

- old_string:
```
Plausible reconciliations include (a) Rudder confused Richard with Robert, the more famous mid-13th-c. principal Gournay heir; (b) Pettigrew telescoped Robert and an earlier or younger Richard; (c) two distinct foundation acts (an original Richard-de-Gournay foundation later refounded or substantially endowed by Robert II) collapsed in both compilations. **Availability tag: Available online -- archive.org for both Rudder and Pettigrew; the Gaunt's Hospital foundation charter survives in the Berkeley / Bristol cartulary material and would resolve the conflict.**[^v73-rudder-gaunts-urcot]
```
- new_string:
```
Plausible reconciliations include (a) Rudder confused Richard with Robert, the more famous mid-13th-c. principal Gournay heir; (b) Pettigrew telescoped Robert and an earlier or younger Richard; (c) two distinct foundation acts (an original Richard-de-Gournay foundation later refounded or substantially endowed by Robert II) collapsed in both compilations. **Availability tag: Available online -- archive.org for both Rudder and Pettigrew; the Gaunt's Hospital foundation charter survives in the Berkeley / Bristol cartulary material and would resolve the conflict.**[^v73-rudder-gaunts-urcot]

The Victoria County History of Gloucestershire adjudicates toward reconciliation (a) and adds the missing first actor. VCH names **Maurice de Gaunt, great-grandson of Robert Fitzharding**, as the man who "built an almonry in Billeswick and entrusted the administration of his charity to the monastery of St. Augustine's, Bristol"; after Maurice's death on **30 April 1230**, "his nephew and heir, **Robert de Gurnay**," confirmed the endowment and then "made the hospital a separate foundation, independent of the monastery of St. Augustine, with a master and three chaplains as a governing body." No Richard de Gournay appears anywhere in the VCH account. This supports the Robert reading (Pettigrew) over Rudder's "Richard," and resolves the apparent founder conflict as a founder/refounder distinction: **Maurice de Gaunt founded the almonry; his Gournay nephew and heir Robert de Gurnay refounded it as the independent Gaunt's Hospital** — Rudder's "Richard de Gourney" is most economically an error for Robert.[^vch-glos-gaunts-hospital]

[^vch-glos-gaunts-hospital]: "Hospitals: St Mark, Billeswick, called Gaunt's Hospital," in *A History of the County of Gloucester: Volume 2* (London: VCH, 1907), pp. 114–118, British History Online, https://www.british-history.ac.uk/vch/glos/vol2/pp114-118. Maurice de Gaunt (great-grandson of Robert Fitzharding) built the Billeswick almonry under St Augustine's, Bristol; after his death 30 April 1230 his nephew and heir Robert de Gurnay confirmed the endowment and refounded it as an independent hospital with a master and three chaplains; no Richard de Gournay is named. Surfaced via a BHO full-text "Gurnay" sweep, June 2026. Source ID: `vch-glos-vol2-gaunts-hospital`.
```

---

## Item 4 — new source + validation: VCH Gloucestershire vol. 2 (Gaunt's Hospital)

### 4a — `str_replace` in `data/sources.json` (register after the `vch-bucks-vol2-bledlow` block added in v115)

> Apply after v115 Item 7a. Anchor on the `vch-bucks-vol2-bledlow` notes line.

- old_string:
```
      "notes": "Bledlow manor: granted by Henry II to Hugh de Gurnay before 1177; exchanged 1198 to Bec-Hellouin abbey; retained tenements to his daughter Juliana (m. William Bardolf), who with her husband sought recovery from the Abbot of Bec in 1285-6; Bardolf rents to the early 15th c. Adds the Bec-exchange + recovery specifics to the known Juliana-de-Gournay/Bardolf descent. Senior line. Surfaced via BHO full-text 'Gurnay' sweep, June 2026 (lead L-177)."
    },
```
- new_string:
```
      "notes": "Bledlow manor: granted by Henry II to Hugh de Gurnay before 1177; exchanged 1198 to Bec-Hellouin abbey; retained tenements to his daughter Juliana (m. William Bardolf), who with her husband sought recovery from the Abbot of Bec in 1285-6; Bardolf rents to the early 15th c. Adds the Bec-exchange + recovery specifics to the known Juliana-de-Gournay/Bardolf descent. Senior line. Surfaced via BHO full-text 'Gurnay' sweep, June 2026 (lead L-177)."
    },
    "vch-glos-vol2-gaunts-hospital": {
      "shortTitle": "VCH Gloucestershire vol. 2 - Gaunt's Hospital (St Mark, Billeswick)",
      "citation": "\"Hospitals: St Mark, Billeswick, called Gaunt's Hospital.\" A History of the County of Gloucester, Volume 2 (London: VCH, 1907), pp. 114-118. British History Online.",
      "archive": "British History Online",
      "url": "https://www.british-history.ac.uk/vch/glos/vol2/pp114-118",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/vch-glos-vol2-gaunts-hospital.md",
      "notes": "St Mark / Gaunt's Hospital, Bristol: Maurice de Gaunt (great-grandson of Robert Fitzharding) built the Billeswick almonry under St Augustine's; after his death 30 Apr 1230 his nephew and heir Robert de Gurnay confirmed it and refounded it as an independent hospital (master + 3 chaplains). No Richard de Gournay named. Adjudicates the Rudder (Richard) vs Pettigrew (Robert) founder conflict toward Robert de Gurnay as refounder, Maurice de Gaunt as original almonry founder. Collateral/West-Country Gournay. Surfaced via BHO full-text 'Gurnay' sweep, June 2026."
    },
```

### 4b — `new file write`: `sources/validations/vch-glos-vol2-gaunts-hospital.md`

```
# Validation — VCH Gloucestershire vol. 2, Gaunt's Hospital (`vch-glos-vol2-gaunts-hospital`)

- **Source examined:** "Hospitals: St Mark, Billeswick, called Gaunt's Hospital," VCH Gloucestershire vol. 2 (1907), pp. 114–118, British History Online (free series).
- **Portion examined:** the foundation/refoundation passage only — Maurice de Gaunt's almonry under St Augustine's, his death 30 April 1230, and Robert de Gurnay's (nephew and heir) confirmation and refoundation as an independent hospital with a master and three chaplains. Read to adjudicate the Rudder-vs-Pettigrew founder conflict.
- **Unexamined / uncertain:** the later hospital descent and dissolution; the underlying Berkeley/Bristol cartulary foundation charter (the primary tie-breaker) was not consulted.
- **Findings recorded at:** `research/places/somerset-gournay-collateral.md` (Gaunt's Urcot / founder-conflict section).
```

---

## Source-tracking

- **Reused:** `blomefield-norfolk` (Hardingham extract written directly; notes updated, Item 2).
- **New:** `vch-glos-vol2-gaunts-hospital` (+ validation, Item 4).
- **Corpus supplement written directly this arc:** `blomefield-norfolk-vol10-pp221-227-hardingham-swathing.md`.

## Note on scope

This supplements v115 with corroborating/adjudicating sources only; it introduces no new open questions (the residual Gaunt's Hospital primary-charter check and the West Wellow/Bledlow follow-ups already live in their leads). Apply v115 first (or together): Item 4a here anchors on the `vch-bucks-vol2-bledlow` entry that v115 adds.
