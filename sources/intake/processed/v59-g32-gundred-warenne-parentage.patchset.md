# Intake patchset v59 - G32 Edith de Warenne / Gundred parentage cleanup

**Prepared:** 2026-05-24
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation). **Status:** Draft patchset for review. **Do NOT apply until approved.**
**Origin:** User request to memorialize the best accounting for Edith de Warenne's parentage: remove the discredited William-the-Conqueror descent claim from the public fact sheet, move the source-critical details to the G32 research companion, add authoritative sourcing, and inspect those sources for other Gournay/Gurney/Gourney variant findings.
**Prerequisite:** This patchset assumes v58 has landed because it edits text introduced or expanded in the current G32 fact sheet and companion.

## Scope

This patchset changes the treatment of Edith de Warenne's mother Gundred in the G32 materials.

1. The fact sheet should state the best-current parentage only: Edith was daughter of William de Warenne, 1st Earl of Surrey, and Gundred, sister of Gerbod the Fleming. It should not narrate the rejected royal-descent theory.
2. The research companion should preserve the full evidentiary accounting: how the older claim arose, why it fails, which sources are reliable for each part, and why Daniel Gurney's older statement should be treated as reception history rather than adopted genealogy.
3. New sourceIds should be added for the modern source-critical authorities actually consulted.
4. The parentage-specific sources should be checked for additional Gournay/Gurney/Gourney/Gornay variant findings. Result: no new direct Gournay finding appears in the Henry Project or Chris Phillips/Gerbod-Gundred source-document pages; the already-known G32 finding in Clay's *Early Yorkshire Charters* remains the productive Gournay-specific item.

## Decision summary

| Question | Best accounting |
|---|---|
| Who was Edith de Warenne? | Daughter of William de Warenne, 1st Earl of Surrey, and Gundred; wife of Gerard de Gournay; later wife of Drogo/Drew de Mouchy. |
| What directly links Edith to the Warenne family? | Guillaume de Jumieges / Gesta Normannorum tradition as quoted by FMG: Gerard went to Jerusalem with wife Edith, sister of William, count of Warenne. Clay, *Early Yorkshire Charters* vol. 8, pp. 6-7, independently treats Edith/Ediva as daughter of William de Warenne and Gundreda. |
| Who was Gundred? | Gundred, wife of William de Warenne, is best treated as sister of Gerbod the Fleming, earl of Chester, not as a daughter of William the Conqueror or of Queen Matilda. |
| Why reject the royal descent? | The positive evidence is late, altered, interpolated, or spurious; the negative evidence includes Orderic/Hyde for the Gerbod relationship, source criticism of the Lewes material, and Anselm's letter about the proposed Warenne-Henry I marriage, which gives fourth/sixth degree kinship rather than first-cousin kinship. |
| Public fact-sheet handling | Remove the royal-descent controversy from the fact-sheet body and citation n4. Keep only the parentage needed for a reader: Edith was Warenne/Gundred, with authoritative sourceIds. |
| Research companion handling | Add the full conflict explanation and keep Daniel Gurney's older claim as an explicitly rejected/legacy interpretation. |

## Sources / data referenced

**Existing sourceIds reused:** `dg-rec-pt1`, `dg-rec-supp`, `fmg-medlands-normacre`, `pattou-racines-histoire-gournay-2025`, `early-yorkshire-charters-vol-8-clay-1949`, `dhi-crusaders-leeds`.

**Proposed new sourceIds (full JSON in Section 3):**

- `henry-project-william-conqueror-gundred` - Stewart Baldwin, The Henry Project, William "the Conqueror" page; identifies Gundred as a falsely attributed daughter and as sister of Gherbod/Gerbod.
- `henry-project-matilda-flanders-gundred` - Stewart Baldwin, The Henry Project, Matilda of Flanders page; gives the detailed source-critical case against making Gundred a daughter of William or Matilda, including Lewes charter problems and Anselm's letter.
- `medievalgenealogy-gerbod-gundred-documents` - Chris Phillips, *Some Notes on Medieval English Genealogy*, source-document collection for Gerbod and Gundred; useful because it assembles the Orderic, Lewes, Anselm, Clay, and later-cartulary evidence in one source-critical page.

Do not add Wikipedia as a sourceId for this question.

---

## 1. Fact sheet edits

Target file:

`fact-sheets/g32-gerard-de-gournay-fact-sheet.md`

### 1.1 Marriage(s) cell - remove rejected theory from public prose

Find the Edith paragraph in the Marriage(s) cell, line ~64:

```html
        <div><strong><a href="https://en.wikipedia.org/wiki/De_Warenne_family">Edith de Warenne</a></strong> - daughter of <a href="https://en.wikipedia.org/wiki/William_de_Warenne,_1st_Earl_of_Surrey">William de Warenne, 1st Earl of Surrey</a>, the wealthiest Norman baron in England after the king (<a href="https://en.wikipedia.org/wiki/Domesday_Book">Domesday</a> holdings in 13 counties). According to the <a href="https://en.wikipedia.org/wiki/Gundred,_Countess_of_Surrey">Warren charters</a>, she was also a granddaughter of <a href="https://en.wikipedia.org/wiki/William_the_Conqueror">William the Conqueror</a> through his daughter Gundred - though modern scholarship rejects this descent. With Edith, Gerard received Norfolk manors "in <a href="https://en.wikipedia.org/wiki/Frankmarriage">frank marriage</a>." After Gerard's death Edith returned home and remarried <strong>Drogo (Dreux) de Mouchy</strong> - himself a First Crusader and lord of Mouchy-le-Chatel - who then governed the honour of Gournay during the minority of Edith's son Hugh. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```

Replace with:

```html
        <div><strong>Edith de Warenne</strong> - daughter of William de Warenne, 1st Earl of Surrey, and Gundred, sister of Gerbod the Fleming. William de Warenne was the wealthiest Norman baron in England after the king, with Domesday holdings in 13 counties. With Edith, Gerard received Norfolk manors "in frank marriage." After Gerard's death Edith returned home and remarried <strong>Drogo (Dreux) de Mouchy</strong> - himself a First Crusader and lord of Mouchy-le-Chatel - who then governed the honour of Gournay during the minority of Edith's son Hugh. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```

Rationale: the fact sheet should not explain the discredited royal-descent theory in the public marriage cell. That analysis belongs in the companion.

### 1.2 Citation n4 - cite best accounting, not the rejected theory

Find citation n4, line ~151:

```html
  <li id="n4">Daniel Gurney, <em>Record</em>, Part I (1848), p. 27: marriage and Warenne connection. Daniel Gurney, <em>Supplement</em> (1858), Note 16, p. 735: Gerard's seal - "Signum Girardi de Gornaco" - in the Cartulary of La Trinite de Rouen (ed. Deville, Tome III, Charter No. 94). Independently confirmed by Guillaume de Jumieges, <em>Historia Normannorum</em>, Liber VIII Section VIII (Duchesne ed., 1619, p. 296): "Giraldus tandem Hierusalem petens cum uxore sua Edithua sorore Willelmi comitis de Warenna" - naming Edith as sister of William (II) de Warenne, the second earl, i.e., daughter of William I, 1st Earl, by his first wife Gundred. The Foundation for Medieval Genealogy MedLands (Cawley) Normandy section, under "Seigneurs de Gournay," cross-references this passage. The Conqueror-descent claim via Gundred appears in the Warren charters but is rejected by modern scholarship: English Wikipedia, "Gundred, Countess of Surrey," and Etienne Pattou, <em>Racines Histoire</em>, both identify Gundred as sister of Gerbod the Fleming, 1st Earl of Chester, not as a daughter of William the Conqueror. Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>fmg-medlands-normacre</code>, <code>pattou-racines-histoire-gournay-2025</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

Replace with:

```html
  <li id="n4">Daniel Gurney, <em>Record</em>, Part I (1848), p. 27: marriage and Warenne connection. Daniel Gurney, <em>Supplement</em> (1858), Note 16, p. 735: Gerard's seal - "Signum Girardi de Gornaco" - in the Cartulary of La Trinite de Rouen (ed. Deville, Tome III, Charter No. 94). Guillaume de Jumieges, <em>Historia Normannorum</em>, Liber VIII Section VIII (Duchesne ed., 1619, p. 296), records Gerard's wife Edith as "sorore Willelmi comitis de Warenna," identifying her as sister of William de Warenne, second earl. Charles Travis Clay, ed., <em>Early Yorkshire Charters</em>, vol. 8: <em>The Honour of Warenne</em> (1949), pp. 6-7, treats Edith/Ediva as daughter of William de Warenne, 1st Earl of Surrey, and Gundreda, and notes her later marriage to Drew de Monchy. For Gundred's parentage as sister of Gerbod the Fleming, see Stewart Baldwin, The Henry Project, William "the Conqueror" and Matilda of Flanders pages, and Chris Phillips, "The family of Gerbod and Gundred: documents." Source IDs: <code>dg-rec-pt1</code>, <code>dg-rec-supp</code>, <code>fmg-medlands-normacre</code>, <code>early-yorkshire-charters-vol-8-clay-1949</code>, <code>henry-project-william-conqueror-gundred</code>, <code>henry-project-matilda-flanders-gundred</code>, <code>medievalgenealogy-gerbod-gundred-documents</code>. <a class="citation-back" href="#ref-4">↩</a></li>
```

Note: this public citation intentionally does not walk through the rejected theory. The companion will do that.

---

## 2. Research companion edits

Target file:

`research/people/g32-gerard-de-gournay-fact-sheet.research.md`

### 2.1 Snapshot wife line - add best-current Gundred identification

Find the wife bullet in Section 1, line ~14:

```markdown
- **Wife**: Edith (Edive / Editha) de Warenne, daughter of William de Warenne 1st Earl of Surrey + his first wife Gundred. Marriage [1084/92] per FMG. The marriage assumption Edith was c. 12 at marriage is FMG's chronological estimate. Edith's birth: [1072/80]; death: after 1155.
```

Replace with:

```markdown
- **Wife**: Edith (Edive / Editha) de Warenne, daughter of William de Warenne 1st Earl of Surrey and his first wife Gundred, now best identified as sister of Gerbod the Fleming rather than as a daughter of William the Conqueror or Queen Matilda. Marriage [1084/92] per FMG. The marriage assumption Edith was c. 12 at marriage is FMG's chronological estimate. Edith's birth: [1072/80]; death: after 1155. See Section 2.7 for the Gundred parentage evidence.
```

### 2.2 Add new source-critical subsection after Section 2.6

After the paragraph ending:

```markdown
DG 1845, working from the same Latin (DG p. 70), translates: *"Giraldus tandem Hierusalem petens cum uxore sua Editha, in ipso itinere mortuus est"* - *"Giraldus, finally seeking Jerusalem with his wife Editha, died on the very journey."*
```

Append this new subsection before Section 3:

```markdown
### 2.7 Edith's mother Gundred: parentage accounting

**Best-current conclusion.** Edith de Warenne remains well supported as daughter of William de Warenne, 1st Earl of Surrey, and Gundred. Gundred should not be treated as a daughter of William the Conqueror or Queen Matilda. The best-supported identification is Gundred as sister of Gerbod the Fleming, briefly earl of Chester.

**Direct G32 relevance.** The Gournay question only requires two steps: (1) Gerard's wife Edith was a Warenne; (2) Edith was a daughter of William de Warenne and Gundred. Guillaume de Jumieges gives the first step by calling Edith "sorore Willelmi comitis de Warenna" - sister of William, count of Warenne. Clay's *Early Yorkshire Charters*, vol. 8, pp. 6-7, gives the second step in a modern scholarly Warenne-charter edition: Edith/Ediva was daughter of William de Warenne and Gundreda, accompanied Gerard on the Jerusalem pilgrimage, then married Drew de Monchy.

**Evidence for Gundred as sister of Gerbod.** Orderic Vitalis says William de Warenne had as wife Gundred, sister of Gerbod: "Gundredam sororem Gherbodi." The Hyde chronicle also places Gerbod and Gundred as siblings. Chris Phillips's source-document collection prints and contextualizes these passages, and Stewart Baldwin's Henry Project treats Gundred as a falsely attributed daughter of William the Conqueror and as sister of Gherbod/Gerbod.

**Why the older royal-descent claim fails.** The positive case for making Gundred a daughter of William the Conqueror or Queen Matilda rests on weak Lewes material:

- In a William I confirmation to Lewes, the phrase "filie mee" after Gundred appears in a later hand over an erasure. It cannot carry the weight of making Gundred the king's daughter.
- A purported William de Warenne / Cluny charter appears to call Queen Matilda the mother of William de Warenne's wife, but Clay judged the charter spurious on stylistic grounds and because it contains statements contradicted by other evidence. Phillips summarizes Clay's conclusion that the charter was probably composed after 1201 and perhaps much later.
- A Carlton/Lewes phrase can be read as Queen Matilda giving Carlton to Gundred, not as naming Gundred as Queen Matilda's daughter. Waters's reading, accepted in the later source criticism, removes the need for a mother-daughter relationship.
- Later Lewes narrative pedigrees and cartulary notices calling Gundred daughter of the Conqueror are very late and internally problematic. One late notice also calls her countess of Surrey while placing her death before William de Warenne was made earl.

**Anselm's letter is the strongest negative test.** Anselm objected to the proposed marriage of Gundred's son William de Warenne the younger to a daughter of Henry I because the pair were related in the fourth generation on one side and the sixth on the other. If Gundred were Henry I's sister or half-sister, the proposed bride and groom would have been first cousins. Anselm's stated objection therefore does not fit the royal-daughter theory.

**How to treat Daniel Gurney.** Daniel Gurney repeats the older Warren-charter tradition at several points: Part I p. 27 says Edith was daughter of William de Warren by Gundred, "probably" daughter of William the Conqueror; the Part I pedigree p. 277 repeats Gundred as daughter of the Conqueror; and later notes explain that the claim rests chiefly on the Lewes Priory foundation material. Those passages should remain in the companion as a record of nineteenth-century reception and source transmission, not as the repo's adopted parentage.

**How to treat Pattou.** Pattou's main Gournay chart entry identifies Edith as daughter of William I, earl of Surrey, and "Gondree/Gundred de Chester," which aligns with the Gerbod/Chester identification. Pattou's marginal note making Hugh IV a nephew of Henry I conflicts with that main parentage and should be treated as an uncorrected survival of the older royal-descent theory, not as the controlling reading.

**Repo consequence.** Edith's Warenne marriage remains important for Gerard's Norfolk endowment and for the social status of the Gournay children. It does not supply a William-the-Conqueror descent through Gundred.

**Variant-name sweep within these sources.** The Henry Project William and Matilda pages and Phillips's Gerbod/Gundred source-document page were checked for Gournay/Gurney/Gourney/Gornay variant findings. They are parentage-evidence pages, not Gournay evidence pages, and no additional Gournay finding was found there. Clay's *Early Yorkshire Charters* vol. 8 remains the productive Gournay-specific source in this cluster: pp. 6-7 already support Edith/Ediva's marriage to Gerard, her Jerusalem pilgrimage, Gerard's death not earlier than 1104, her later Drew de Monchy marriage, and her daughter Gundreda's naming after grandmother Gundreda de Warenne.
```

### 2.3 Pattou analysis - correct the internal contradiction

Find the Pattou discussion currently beginning:

```markdown
The "richement dotee en Norfolk & Norwich" places Edith's Norfolk endowment specifically. Pattou identifies Edith's mother as "Gondree/Gundred de Chester" - i.e., sister of Gerbod the Fleming, 1st Earl of Chester. This matches modern scholarly consensus and rejects the older Warren-charters claim that Gundred was a daughter of William the Conqueror.

**Pattou's marginal annotation** (p. 3, blue):

> *"Par sa mere Edith, Hugues IV de Gournay est neveu du Roi Henri I d'Angleterre."*

Translation: *"Through his mother Edith, Hugues IV de Gournay is the nephew of King Henry I of England."*

This claim depends on the older view that Gundred was Conqueror's daughter - making Edith his granddaughter and Hugues IV great-grandnephew of Henry I. Modern Wikipedia and modern scholarship reject this descent. Pattou retains the older view; the repo follows the modern scholarly consensus.
```

Replace with:

```markdown
The "richement dotee en Norfolk & Norwich" places Edith's Norfolk endowment specifically. Pattou identifies Edith's mother as "Gondree/Gundred de Chester" - i.e., sister of Gerbod the Fleming, 1st Earl of Chester. This matches the modern scholarly reading followed here.

**Pattou's marginal annotation** (p. 3, blue):

> *"Par sa mere Edith, Hugues IV de Gournay est neveu du Roi Henri I d'Angleterre."*

Translation: *"Through his mother Edith, Hugues IV de Gournay is the nephew of King Henry I of England."*

This marginal note conflicts with Pattou's own main-line parentage for Edith's mother. It appears to preserve the older Warenne/Lewes tradition that made Gundred a daughter of the Conqueror or of Queen Matilda. Do not adopt the marginal note as a relationship statement. The repo follows the source-critical reading in Clay, Baldwin, and Phillips: Gundred was sister of Gerbod the Fleming, not Henry I's sister.
```

### 2.4 Sources-consulted table - add new sourceIds

In Section 16, add these rows near the existing Clay / FMG / Pattou entries:

```markdown
| Stewart Baldwin, The Henry Project, William "the Conqueror" page - Gundred treated as falsely attributed daughter and as sister of Gherbod/Gerbod | `henry-project-william-conqueror-gundred` |
| Stewart Baldwin, The Henry Project, Matilda of Flanders page - detailed source-critical discussion of Lewes charter problems and Anselm letter | `henry-project-matilda-flanders-gundred` |
| Chris Phillips, "The family of Gerbod and Gundred: documents," *Some Notes on Medieval English Genealogy* | `medievalgenealogy-gerbod-gundred-documents` |
```

---

## 3. Source registry edits

Target file:

`data/sources.json`

### 3.1 Add three sourceIds

Insert these entries under the top-level `sources` object near the other medieval web/prosopography sources:

```json
    "henry-project-william-conqueror-gundred": {
      "shortTitle": "Henry Project - William the Conqueror / Gundred",
      "citation": "Baldwin, Stewart. The Henry Project: The Ancestors of King Henry II of England, William \"the Conqueror\" page. American Society of Genealogists.",
      "archive": "fasg.org / The Henry Project",
      "url": "https://fasg.org/projects/henryproject/data/willi001.htm",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Modern source-critical prosopography page identifying Gundred, wife of William de Warenne, as a falsely attributed daughter of William the Conqueror and instead as sister of Gherbod/Gerbod, earl of Chester. Used in G32 research companion to correct Edith de Warenne's maternal ancestry and remove the rejected Conqueror-descent claim from the fact sheet."
    },
    "henry-project-matilda-flanders-gundred": {
      "shortTitle": "Henry Project - Matilda of Flanders / Gundred",
      "citation": "Baldwin, Stewart. The Henry Project: The Ancestors of King Henry II of England, Matilda of Flanders page. American Society of Genealogists.",
      "archive": "fasg.org / The Henry Project",
      "url": "https://fasg.org/projects/henryproject/data/matil000.htm",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Detailed source-critical discussion rejecting Gundred as a daughter of Queen Matilda or William the Conqueror. Summarizes the late/interpolated Lewes evidence, the spurious Warenne charter, the Carlton wording, Orderic/Hyde evidence for the Gerbod sibling relationship, and Anselm's letter about William de Warenne the younger's proposed marriage to Henry I's daughter."
    },
    "medievalgenealogy-gerbod-gundred-documents": {
      "shortTitle": "MedievalGenealogy.org.uk - Gerbod and Gundred documents",
      "citation": "Phillips, Chris. \"The family of Gerbod and Gundred: documents.\" Some Notes on Medieval English Genealogy.",
      "archive": "medievalgenealogy.org.uk",
      "url": "https://www.medievalgenealogy.org.uk/families/gundred/gundocs.shtml",
      "corpusStatus": "external",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Source-document collection for Gerbod, Gundred, and the early Warenne/Lewes evidence. Includes Orderic Vitalis naming Gundred as sister of Gerbod; Lewes Priory charter extracts; discussion of the later 'filie mee' insertion, the spurious Warenne/Cluny charter, the Carlton wording, Anselm's letter, late Lewes narrative pedigrees, and Clay's analysis in Early Yorkshire Charters vol. 8."
    },
```

### 3.2 Update existing Clay source notes

Find sourceId `early-yorkshire-charters-vol-8-clay-1949` and replace its `notes` value:

```json
      "notes": "Modern scholarly edition of charters relating to the honour of Warenne. Pages 6-7 give an independent scholarly statement of Edith / Ediva de Warenne's two marriages: (1) Gerard de Gournay, on whose Jerusalem pilgrimage 'he died not earlier than 1104'; (2) 'Drew de Monchy, by whom she had a son Drew the younger.' This is the strongest modern third-party confirmation of the corrected G32 chronology (death after 1104, not before), the Drogo I/Drogo II distinction, and Edith's role on the pilgrimage. Also notes that Edith named her daughter Gundreda after her grandmother Gundreda de Warenne."
```

Replace with:

```json
      "notes": "Modern scholarly edition of charters relating to the honour of Warenne. Pages 6-7 give an independent scholarly statement of Edith / Ediva de Warenne's two marriages: (1) Gerard de Gournay, on whose Jerusalem pilgrimage 'he died not earlier than 1104'; (2) 'Drew de Monchy, by whom she had a son Drew the younger.' This is the strongest modern third-party confirmation of the corrected G32 chronology (death after 1104, not before), the Drogo I/Drogo II distinction, Edith's role on the pilgrimage, and Edith's placement as daughter of William de Warenne and Gundreda. Also notes that Edith named her daughter Gundreda after her grandmother Gundreda de Warenne. Pages 40-46 / 50-62 are also relevant to the Gundred parentage controversy, including the Lewes evidence, the Gerbod relationship, and the source-critical rejection of the older royal-descent theory."
```

---

## 4. Companion source-hygiene notes

### 4.1 Daniel Gurney citations stay, but their role changes

Do not delete the DG passages from the companion. They are useful because they show exactly how the older theory entered the Gurney/Gournay tradition. The companion should explicitly mark them as:

- nineteenth-century reception / legacy tradition;
- dependent on the Lewes/Warenne charter material;
- not adopted by the repo after Clay/Baldwin/Phillips source criticism.

### 4.2 Wikipedia is not used as authority

Do not cite Wikipedia in the new fact-sheet citation or companion parentage analysis. Existing fact-sheet sidebar "Related Links" can be left untouched unless a separate general Wikipedia-link cleanup is requested. This patchset only removes Wikipedia from the source-critical parentage claim.

### 4.3 Variant sweep finding

Add the variant-sweep paragraph included in Section 2.2. The sweep is deliberately narrow: it covers the sources newly consulted for Gundred's parentage, not every Warenne source in existence.

Observed results:

- Henry Project William page: no new Gournay/Gurney/Gourney/Gornay finding located; useful only for Gundred's falsely attributed royal parentage.
- Henry Project Matilda page: no new Gournay/Gurney/Gourney/Gornay finding located; useful for the source-critical evidence, especially Lewes and Anselm.
- Phillips medievalgenealogy.org.uk Gerbod/Gundred documents page: searched for Gournay/Gurney/Gourney/Gornay variants; no match found.
- Clay, *Early Yorkshire Charters* vol. 8: already productive for G32 on pp. 6-7; no separate new Gournay finding from the Gundred parentage appendix beyond strengthening the Edith/Warenne/Gundred accounting.

---

## 5. Apply-time validation

After applying the patchset, run:

```powershell
.\.venv\Scripts\python.exe -c "import json; json.load(open('data/sources.json', encoding='utf-8'))"
Push-Location site\website
npm.cmd run validate
Pop-Location
```

Do not invoke `python` or `py` directly in this repository.

## 6. Expected outcome

After application:

- `fact-sheets/g32-gerard-de-gournay-fact-sheet.md` no longer tells readers that Edith was claimed as a granddaughter of William the Conqueror.
- `research/people/g32-gerard-de-gournay-fact-sheet.research.md` contains the full evidence trail explaining why that older claim is rejected.
- `data/sources.json` has authoritative non-Wikipedia source records for the Gundred parentage correction.
- The source role is clean: DG remains evidence for the Gournay tradition and for the older claim's transmission, while Clay/Baldwin/Phillips control the modern parentage conclusion.
