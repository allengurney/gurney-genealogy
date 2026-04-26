# v01anderson.patchset.md

Source intake: manual provided (originally sourced from`sources/intake/new/NewIntake_Batch2.md`, entries 2 (deep-research-report.md) and 3 (Screenshot 2026-04-21 065104.png — page 28).

Scope: Anderson 1742 Vol. I (Yvery/Perceval/Harpetre origins, surname adoption to Gournay) plus residual Vol. II direct-line citation work to fully close out the Anderson source. Pairs with the existing Vol. II Book VII corpus extract.

Closure intent: this patchset finishes Anderson 1742 (both volumes) so the next intake batch can move on to other sources without revisiting Anderson.

---

## Item 1 — sourceId for Vol. I

Outcome: **promote**. Add new sourceId. Existing `anderson-yvery-1742` covers Vol. II only; do not modify its corpusPath.

Destination: `data/sources.json`, alongside existing `anderson-yvery-1742`.

New entry to add:

```json
"anderson-yvery-1742-vol-i": {
  "shortTitle": "Anderson, Genealogical History of the House of Yvery, Vol. I",
  "citation": "Anderson, James. Genealogical History of the House of Yvery: In its Different Branches of Yvery, Luvel, Perceval, and Gournay. Vol. I. London: H. Woodfall, Jun., 1742.",
  "archive": "Internet Archive (genealogicalhist01ande)",
  "url": "https://archive.org/details/genealogicalhist01ande",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus/anderson-yvery-1742-vol-i-extract.md",
  "mediaPath": "sources/media/anderson-yvery-1742-vol-i/",
  "validationPath": "sources/validations/anderson-yvery-1742-vol-i.md",
  "notes": "Vol. I covers the House of Yvery proper, with the Harpetre→Gournay surname-adoption material relevant to the collateral Somerset Gournays. Direct-line de Gournays of Normandy and Norfolk are treated in Vol. II (sourceId anderson-yvery-1742). Key pages: printed p. 4 (Ascelin's seven sons; John de Harpetre); p. 21 (surname progression Yvery/Gouel/Percheval/Lupus → Harpetre → Gournay); p. 39 (heraldry: sceptres saltier, then paley of six Or and Azure); p. 78 (Robert de Yvery's Somerset land cluster); pp. 191–193 (children of Ascelin and Isabella de Breteuil, including conjectural John de Yvery and Hugh de Yvery); pp. 199–200 (Stephen-period siege of Kary and Harpetre castles). Anderson died before completion; revised by William Whiston Jr. of the Exchequer. College of Arms attestation referenced in front matter."
}
```

Also update existing `anderson-yvery-1742` `notes` field, appending the sentence:

```
Vol. I (collateral Yvery/Perceval/Harpetre origins) is registered separately as sourceId anderson-yvery-1742-vol-i.
```

---

## Item 2 — Vol. I corpus extract

Outcome: **promote**.

Destination: new file `sources/corpus/anderson-yvery-1742-vol-i-extract.md`.

File operation: create with the content block below. Phase 2 should pull the verbatim transcript bodies from the corresponding "Cleaned transcript" sections of `sources/intake/new/deep-research-report.md` (sections explicitly headed "Cleaned transcript from PDF p. N, printed p. N"). Strip every `fileciteturnNfileN`, `citeturnNsearchN`, and similar deep-research artifact. Preserve 18th-c long-s and OCR oddities only where they do not corrupt meaning.

```markdown
# Yvery / Harpetre-Gournay Extract — *A Genealogical History of the House of Yvery*, Vol. I

**Citation:** Anderson, James. *A Genealogical History of the House of Yvery: In its Different Branches of Yvery, Luvel, Perceval, and Gournay*. Vol. I. London: H. Woodfall, Jun., 1742. Internet Archive item: `genealogicalhist01ande` (https://archive.org/details/genealogicalhist01ande).

**Pair:** This file covers Vol. I material relating to the Yvery/Perceval house and the cadet line that adopted the surname Gournay. The continuous Book VII Gournay descent (Vol. II, printed pp. 474–533) is in `sources/corpus/agenealogical-history-gournay-extract.md`.

**Scope of this extract:** discrete passages bearing on (a) Ascelin Gouel de Perceval's children and surnames, (b) the Harpetre→Gournay surname transition, (c) the Somerset land cluster of Robert de Yvery and Ascelin, (d) heraldic assignments, (e) the Stephen-period siege of Kary and Harpetre. Not a continuous chapter extract; a curated set of named-page passages.

**Method note.** Cleaned transcripts derived initially from a deep-research preliminary read of the PDF (`sources/media/anderson-yvery-1742-vol-i/genealogicalhist01ande.pdf`); page references are to the printed page (book page) with the PDF scan page in parentheses. Long-s and 18th-c spellings retained where readable.

---

## p. 4 (PDF p. 28) — Ascelin's seven sons; John de Harpetre

[Insert verbatim the cleaned transcript block headed "Extract on the origin of the Harpetre-Gournay branch" from `sources/intake/new/deep-research-report.md`. Strip all `fileciteturn…` markers.]

## p. 21 (PDF p. 107) — Surname progression Yvery / Gouel / Percheval / Lupus → Harpetre → Gournay

[Insert verbatim the cleaned transcript block headed "Extract on surname formation."]

## p. 39 (PDF p. 125) — Heraldry attributed to John de Harpetre

[Insert verbatim the cleaned transcript block headed "Extract on heraldry."]

## p. 78 (PDF p. 164) — Somerset land cluster of Robert de Yvery and Ascelin

[Insert verbatim the cleaned transcript block headed "Extract on place-cluster in Somerset."]

## pp. 191–193 (PDF pp. 277–279) — Children of Ascelin Gouel de Perceval and Isabella de Breteuil

[Insert verbatim the cleaned transcript block headed "Extract on the children of Ascelin." Preserve Anderson's explicit conjectural language for John de Yvery and Hugh de Yvery — these are 18th-c hypotheses, not findings.]

## pp. 199–200 (PDF pp. 287–288) — Stephen-period siege of Kary and Harpetre

[Insert verbatim the cleaned transcript block headed "Extract on the Stephen-period castle warfare."]
```

---

## Item 3 — Move Vol. I PDF and screenshot to media

Outcome: **promote**.

File operations:

```
mkdir -p sources/media/anderson-yvery-1742-vol-i/
git mv sources/intake/new/genealogicalhist01ande.pdf \
       sources/media/anderson-yvery-1742-vol-i/genealogicalhist01ande.pdf
git mv "sources/intake/new/Screenshot 2026-04-21 065104.png" \
       sources/media/anderson-yvery-1742-vol-i/p4-printed-john-de-harpetre.png
```

Note on the screenshot: it is page 28 of the PDF scan = printed p. 4 of Vol. I, the same passage transcribed in the Item 2 corpus file under "p. 4 (PDF p. 28)." It is not a separate intake item; do not register it as a duplicate source.

---

## Item 4 — Validation note

Outcome: **promote**.

Destination: new file `sources/validations/anderson-yvery-1742-vol-i.md`.

Body (deliberately thin per `.claude/rules/sources-validations.md`):

```markdown
# Anderson 1742 Vol. I — validation

Source: `anderson-yvery-1742-vol-i` (`data/sources.json`).
Media: `sources/media/anderson-yvery-1742-vol-i/genealogicalhist01ande.pdf`.
Corpus: `sources/corpus/anderson-yvery-1742-vol-i-extract.md`.

Examined: discrete passages on printed pp. 4, 21, 39, 78, 191–193, 199–200. Surrounding chapter context not yet transcribed; the chapter on Ascelin Gouel de Perceval (Book V) and the chapter introducing the Harpetre line (Book VI start) remain unexamined for now and are open for follow-up. Findings landed in `research/topics/anderson-yvery-harpetre-gournay-collateral.md` and (where applicable) the relevant Somerset place files.

OCR/extraction: cleaned transcripts derived from a preliminary AI-assisted read of the PDF. Long-s normalized only for readability; spellings preserved otherwise. Source-specific limitation: Anderson died before completion; Vol. II's front matter notes William Whiston Jr. revised, so style and depth vary across volumes.

Processed via: `sources/intake/processed/v01.patchset.md`.
```

---

## Item 5 — Topic file: Harpetre-Gournay as collateral, not direct

Outcome: **promote**.

Destination: new file `research/topics/anderson-yvery-harpetre-gournay-collateral.md`.

This addresses Allen's note in `NewIntake_Batch2.md` ("If it doesn't belong, consider adding as a topic in research") and provides the disambiguation any future researcher needs the moment they encounter Anderson 1742.

```markdown
# Anderson 1742 — the Harpetre-Gournay collateral line

Anderson 1742 contains two separate Gournay narratives, and conflating them is the cardinal error any reader should expect.

## The two narratives

**Vol. II, Book VII (printed pp. 474–533).** The de Gournay barons proper, beginning with Hugh de Gorniaco (at Mortemer 1054, Domesday tenant of Liston, Fordham, Ardleigh in Essex, retired to Bec). This is the senior line that maps to the direct ancestral sequence in this project: G37 (Eudes, tradition), G36 (Hugh I), G35 (Renaud), G34 (Hugh II), G33 (Hugh III, the Domesday and Conqueror's-companion figure to whom Anderson gives the name "Hugh de Gorniaco"), G32 (Gerard / Girald). After Gerard, Anderson tracks the senior baronial line through successive Hughs (educated by Henry I, at Acon 1191, surrendered Montfort 1203) — these later Hughs are collateral; the direct line passes through Gerard's youngest son Walter (G31), whom Anderson does not cover. Anderson's brief Norfolk aside on Vol. II p. 478 names a three-generation sequence Matthew → William → John, which corroborates DG's G29 → G28 → G27 with the chronological caveats discussed below. Corpus: `sources/corpus/agenealogical-history-gournay-extract.md`.

**Vol. I, Book V/VI material (passages on printed pp. 4, 21, 39, 78, 191–193, 199–200).** A *different* Gournay — the cadet line descended from John, a younger son of Ascelin Gouel de Perceval, Earl of Yvery. This John was given the manor of Harpetre in Somerset, his descendants were known as "de Harpetre" or "de Harpetree," and Robert de Harpetree (grandson of John) was the first to assume the surname Gournay (Anderson Vol. II p. 489). This line ends in the senior heiress at Elizabeth de Gournay, who married John Ap-Adam (late 13th c.) and squandered the inheritance, with a later cadet branch through Sir Matthew de Gournay (d. 1405, Stoke-sub-Hamdon monument) leaving no issue. Corpus: `sources/corpus/anderson-yvery-1742-vol-i-extract.md`.

## Why this matters for the direct line

The Vol. I "Gournay" surname is **not inherited** from the Norman de Gournays of Gournay-en-Bray. It is a 13th-c. **adoption** of the name by a Yvery/Perceval cadet. Anderson is explicit (Vol. II p. 491): the Harpetre line "first assumed the Name of Gournay … after which it continued with all his Descendants," choosing it over the equally available "de Gant." Any place-name, heraldic, or biographical evidence in Vol. I — Harpetre, Kary, Stowey, Inglescombe, Farringdon, Wedmore — belongs to this Yvery cadet, not to the direct line.

## Norfolk aside (Vol. II p. 478)

Anderson interrupts the Vol. II Book VII narrative with a brief Norfolk aside: a Matthew de Gournay "in the Time of Henry the First," with sons Thomas and William, and a grandson John de Gournay who in 3 Edw. I (1274/5) had a suit against the Prior of Lewes for the right of presentation to the church of Harpley. The suit was settled on the field of judicial combat, with the Prior yielding the advowson "to the said John de Gournay … for himself and his Successors for ever." Anderson concludes "of this Line there is nothing farther known."

The three-generation sequence Matthew → William → John is **compatible** with DG's junior Norfolk pedigree at G29 → G28 → G27 in names and order. Anderson omits the two earlier Norfolk generations (Walter G31 and William I G30), explicitly admitting the link to the senior line is uncertain ("doubtless of the same Stock"). Anderson's chronological placement "Time of Henry the First" is too early — DG's Pipe Roll, Liber Niger, and Fine Roll evidence places Matthew fl. c. 1180–1217 (DG-Supp Note 109 has Matthew alive in 2 Hen. III = 1217), and the John in 3 Edw. I (1274/5) fits cleanly with the documented activity of G27 (battle of Lewes 1264, Crusade 1270, Rotuli Hundredorum 1274). Anderson's "Henry the First" is most plausibly a slip for Henry III given his immediately preceding narrative had been on early-13th-century events. The Harpley advowson detail itself is **independent 1742 testimony** for G27's tenure of Harpley — predating DG's 1848 treatment by 106 years. Treat Anderson Vol. II p. 478 as corroborating the G29→G28→G27 sequence with a chronological caveat, not as a competing pedigree. The underlying record (*Placita de Banco*, Norfolk, 3 Edw. I, "de Ecclesia de Harpeli," cited by Anderson) is a primary source worth pursuing on G27's file as an Open Question.

## Heraldic note (Vol. I p. 39)

Anderson reports that John de Harpetre, ancestor of the Harpetre-Gournays, "is said to have borne two sceptres cross'd, per saltier," but that the Harpetre-Gournay line later certainly bore "Paley of six, Or and Azure." This is a Yvery-cadet device, not a direct-line de Gournay coat. Burke's *Ancient Family of Gurney* gives the direct-line arms as "Argent, a cross engrailed gules, quartering Gournay, Warren, and Barclay." The two devices are unrelated and should not be conflated when reading antiquarian heraldry.

## Somerset place leads (deferred — collateral)

Vol. I p. 78 lists the Yvery/Harpetre Somerset estate cluster: Kary, Ferentone, Brismartin, Easton, Weston, [Laneverei?], the two Harpetres, Hetune, Tillebere, Biscopewide, Millescot, Babington, Stacewell, Estide, and a portion of Yvil (= Ilchester). Strong identifications: **Stacewell → Stawell**, **Yvil → Ilchester**, **Babington → Babington**, **Ferentone → Farrington Gurney** (confirmed by Vol. II's "Farringdon" usage on printed pp. 498, 510, where the manor is settled on Thomas de Gournay, youngest son of Anselm). Weaker: Brismartin, Hetune, Tillebere, Biscopewide, Estide. These are collateral places — relevant if a Somerset-Gournay topic ever opens, irrelevant to the direct-line project. No place files are being created from these leads.

## Conjectural sons of Ascelin (Vol. I pp. 191–193)

Anderson names six children of Ascelin Gouel de Perceval and Isabella de Breteuil — Robert, William (Lupellus), Roger (Balbus), John (de Harpetre), and a daughter married to Radulfus Rufus — then explicitly says "Three sons more issued from this marriage … but of these we do not certainly know the names. It is only presumed, that John de Yvery … was one of them. Hugh de Yvery … is likewise supposed to be another of them." These are Anderson's own 18th-c. hypotheses. Preserve the lead; do not promote either name to a stated relationship without contemporary documentation.

## Sources

- Vol. I extract: `sources/corpus/anderson-yvery-1742-vol-i-extract.md` (sourceId `anderson-yvery-1742-vol-i`).
- Vol. II extract: `sources/corpus/agenealogical-history-gournay-extract.md` (sourceId `anderson-yvery-1742`).
- Daniel Gurney 1848: junior Norfolk branch in DG-II; Somerset Gournays in DG-IV (sourceIds `dg-rec-pt2`, `dg-rec-pt4`).
```

---

## Item 6 — Anderson Vol. II direct-line citation surfacing (closure)

Outcome: **promote**. This item closes out Anderson Vol. II by ensuring every direct-line ancestor it independently witnesses carries the citation. Verification walk-through follows.

Anderson Vol. II Book VII covers, in direct-line terms, only:
- **G33 Hugh III** (Anderson's "first Hugh de Gorniaco", at Mortemer, Domesday tenant)
- **G32 Gerard** (Anderson's "Girald", Crusader, Edith de Warenne)
- **G29 Matthew, G28 William II, G27 John I** (the Norfolk aside on Vol. II p. 478)

After Gerard, Anderson's narrative continues with the senior baronial line (Hugh IV at Acon 1191, Hugh V surrendering Montfort 1203) — these are collateral, not direct, and require no citation in direct-line files. G37, G36, G35, G34, G31 (Walter), G30 (William I), and all post-G27 ancestors are not covered by Anderson Vol. II and need no citation here.

### 6a. G33 Hugh III — already cited

File: `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`.
Status: Anderson Vol. II pp. 474–475 already cited in "Sources Consulted" with the Domesday/Bec/Basilia content. **No change needed.**

### 6b. G32 Gerard — already cited

File: `research/people/g32-gerard-de-gournay-fact-sheet.research.md`.
Status: Anderson Vol. II pp. 475–476 already cited in "Sources Consulted" with the Crusade/Edith/Dru de Monceaux content. **No change needed.**

### 6c. G29 Matthew — refine framing

File: `research/people/g29-matthew-de-gournay-fact-sheet.research.md`.

Reason: the existing "Conflicting Information" entry frames Anderson Vol. II p. 478 as a competing pedigree. Closer reading shows Anderson's Matthew → William → John sequence is compatible with DG's G29 → G28 → G27 in names and order. The actual differences are (i) Anderson omits the two earlier Norfolk generations Walter G31 and William I G30, and (ii) Anderson's "Time of Henry the First" date for Matthew is too early — almost certainly a slip for Henry III given the immediately preceding narrative.

File operation: replace the second row of the "Conflicting Information" table (the row whose first column reads "Norfolk pedigree sequence") with the corroboration-with-caveats row below.

Old row to replace (verbatim from existing file):

```
| Norfolk pedigree sequence | DG-I (1848): Walter → William I → Matthew → William II | Anderson, *House of Yvery* (1742), p. 478: "Matthew de Gournay, in the Time of Henry the First; which Matthew had two Sons, Thomas, and William" | **DG is better sourced.** Anderson's 1742 Norfolk pedigree is compressed and does not match DG's more detailed Walter→William→Matthew sequence. Anderson predates DG by 106 years but lacks the Liber Niger, Les Olim, and Supplement evidence that DG assembled. The discrepancy should be noted but DG's genealogy prevails. |
```

New row to insert in its place:

```
| Norfolk pedigree sequence | Anderson, *House of Yvery* (1742), p. 478: Matthew → William → John (3 Edw. I), placed "in the Time of Henry the First" | DG-I (1848): Walter G31 → William I G30 → Matthew G29 → William II G28 → John I G27 (with Liber Niger, Les Olim, Pipe Roll, and Fine Roll evidence) | **Compatible, not in conflict.** Anderson's three-generation sequence corroborates DG's G29→G28→G27 in names and order, and predates DG by 106 years. Anderson omits the two earlier Norfolk generations (Walter G31 and William I G30), explicitly admitting the link to the senior line is uncertain ("doubtless of the same Stock"). Anderson's "Time of Henry the First" placement is too early — DG-Supp Note 109 has Matthew alive in 2 Hen. III (1217) and the John in 3 Edw. I (1274/5) fits G27's documented activity (Lewes 1264, Crusade 1270, Rot. Hund. 1274). The "Henry the First" is most plausibly a slip for Henry III; Anderson's narrative immediately preceding the digression had been on early-13th-c. events. Net: Anderson Vol. II p. 478 is corroborating evidence, not a competing pedigree. |
```

### 6d. G28 William II — already cited

File: `research/people/g28-william-de-gournay-ii-fact-sheet.research.md`.
Status: Anderson Vol. II p. 478 already cited in "Sources Consulted" ("Compressed Norfolk pedigree mentioning Matthew with sons 'Thomas and William.'"). **No change needed.**

### 6e. G27 John I — add citation, working note, and open question

File: `research/people/g27-sir-john-de-gournay-i-fact-sheet.research.md`.

Reason: Anderson Vol. II p. 478 contains a specific direct-line datum — the 1274/5 lawsuit between John de Gournay and the Prior of Lewes over the Harpley advowson, settled by judicial combat with the Prior yielding the advowson "for himself and his Successors for ever." This is independent 1742 testimony predating DG by 106 years and is currently uncited at G27.

File operations:

(i) In the "Working Notes" section, append the following block at the end (before the `---` separator that precedes the "Landholdings" section):

```markdown
### Anderson 1742 — Harpley advowson resolved by trial by battle, 3 Edw. I

2026-04-26 — Anderson, *House of Yvery* Vol. II (1742), p. 478, records the Harpley advowson resolution under John (3 Edw. I = 1274/5):

> "John de Gournay, who in the third of King Edward the First had a Suit with the Prior of Lewes, for the Right of Presentation to the Church of Harpeli, in the same County of Norfolk; whereupon a Trial by Battle was appointed, and the said John de Gournay and the Prior came armed into the Field, where the Prior yielded full Seizin of the said Advowson, to the said John de Gournay, for himself and his Successors for ever."

Anderson cites *Placita de Banco*, Norfolk, 3 Edw. I, "de Ecclesia de Harpeli." This is independent 1742 print testimony predating DG by 106 years. It complements the Rotuli Hundredorum 1274 entry already on this file (which establishes the Harpley tenure chain King → Earl Warren → Caletorp → Gournay) by identifying the parallel ecclesiastical-patronage dispute and its resolution. The trial-by-battle resolution is striking — judicial combat for advowson disputes was already archaic by 1274/5, and its use here suggests both parties were prepared to press the matter to its medieval extreme. The Prior's yielding "in the field" gave John and his successors permanent right of presentation to Harpley church, which would have transmitted to G26, G25, G24, G23 Edmund and forward.
```

(ii) In the "Open Questions" section, append a new numbered question (the existing list ends at item 4):

```markdown
5. **Placita de Banco, Norfolk, 3 Edw. I, "de Ecclesia de Harpeli":** Anderson Vol. II p. 478 cites this primary source for the Harpley advowson trial-by-battle resolution between John and the Prior of Lewes. The original record, if it survives at TNA among the Common Pleas plea rolls (CP 40 series for Edward I), would provide the definitive primary text. Locating it would (a) confirm Anderson's account verbatim, (b) potentially resolve any remaining doubt about whether Anderson's "John" is G27 or a different figure, (c) document the specific procedural form (judicial duel, advowson dispute) used.
```

(iii) In the "Sources Consulted" section, append the following entry before the `### Sources to obtain` subheading (i.e. immediately after the *Excerpta Historica* line):

```markdown
- Anderson, James, *Genealogical History of the House of Yvery*, Vol. II (London, 1742), p. 478: independent 1742 record of the Harpley advowson dispute between John de Gournay and the Prior of Lewes in 3 Edw. I (1274/5), settled by judicial combat with the Prior yielding the advowson to John "for himself and his Successors for ever." Cites *Placita de Banco*, Norfolk, 3 Edw. I, "de Ecclesia de Harpeli." Predates DG by 106 years. Source ID: `anderson-yvery-1742`. [Anderson-Yvery]
```

(iv) In the "Sources to obtain" subsection, append:

```markdown
- *Placita de Banco*, Norfolk, 3 Edw. I, "de Ecclesia de Harpeli" — the original Common Pleas record of the Harpley advowson dispute. TNA CP 40 series.
```

(v) In the "Fact Sheet Improvement Notes" section, append a new numbered note:

```markdown
6. **Harpley advowson trial-by-battle (Anderson Vol. II p. 478):** The 1274/5 judicial-combat resolution of the Lewes Priory dispute, with the Prior yielding the advowson "for himself and his Successors for ever," is a vivid and datable narrative anchor. It pairs naturally with the Rotuli Hundredorum 1274 tenure-chain entry to give a complete picture of John's Harpley position — landholding *and* ecclesiastical patronage, both secured in the same year.
```

---

## Item 7 — Archive the report and the session

Outcome: **archive after Phase 2 application**.

File operations (Phase 2 only, after the corpus extract is written and Item 6 edits are applied):

```
mkdir -p sources/intake/archive/v01/
git mv sources/intake/new/deep-research-report.md \
       sources/intake/archive/v01/deep-research-report-anderson-yvery-vol-i.md
```

Do **not** delete or move `sources/intake/new/NewIntake_Batch2.md` yet — it contains other unprocessed entries (HoP John Gurney d.1408; Thoms anecdotes; Edmund Gurney divine; Strigulensia Hugh de Gournay; Gurnay Redivivus; Norfolk topographical material; Domesday Hugh of Gournay; Hardingham parish history). Those are separate intake items for future patchsets.

The duplicate `The_British_Archivist.pdf` at `sources/intake/new/The_British_Archivist.pdf` is identical to the one already in `sources/media/The_British_Archivist.pdf` (same SHA `30cd8098…`); delete the intake copy:

```
git rm sources/intake/new/The_British_Archivist.pdf
```

---

## Items intentionally excluded as collateral

Per Allen's direction (focus on direct ancestors; if too tangential, leave out). The following deferred follow-ups have been evaluated and are **not** being written into the repo because they bear only on the collateral Yvery/Harpetre/Somerset Gournays:

1. **Somerset place files** for Harpetre, Stowey, Farringdon Gurney, Inglescombe, Wedmore, etc. — collateral. The place names are preserved in the Vol. I corpus extract (Item 2) and in the topic file's "Somerset place leads" section (Item 5). No `research/places/*.md` files are being opened.

2. **DG Vol. IV (Gournays of Somersetshire) cross-read against Anderson Vol. I + Vol. II Somerset material** — collateral. DG-IV is already in corpus as `dg-rec-pt4`; the cross-read would only refine the Yvery-cadet pedigree, which the topic file (Item 5) already explains is collateral. No action.

3. **Standalone Norfolk Anderson-vs-DG topic file** — already captured in two places: (a) G29's "Conflicting Information" table as refined in Item 6c, and (b) the "Norfolk aside" section of the collateral topic file (Item 5). No third location needed.

The single direct-line item from the deferred list — pursuing the *Placita de Banco* primary record cited by Anderson Vol. II p. 478 — has been written into G27's Open Questions and "Sources to obtain" via Item 6e, where any researcher working on G27 will find it.

---

## Open questions / hold-review (none)

No items in this patchset are hold-review. Identification is solid; sources align; destinations are unambiguous. Anderson 1742 (both volumes) is fully closed out by this patchset.