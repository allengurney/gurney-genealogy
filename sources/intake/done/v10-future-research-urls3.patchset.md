# Intake patchset v10 - Future research URLs 3, corrected execution packet

```yaml
patchset_id: v10
created: 2026-05-02
corrected: 2026-05-03
intake_file: C:\Users\allen\Downloads\Future research urls3.md
repo_ref_inspected: codex/1066-gurney-gournay-intake @ 7776deb142859b8ac9de33ea4246db2b3f14a1b2
phase: 1 intake preparation only
phase_2_rule: Execute the operations below. The source reasoning, person/place placement, and G32-G37 generation mapping have already been resolved here.
```

## Correction standard

- Corpus files are source text or tightly trimmed source extracts. Do not use corpus files as the home for analysis.
- Substantive findings go into `research/people`, `research/places`, `research/topics`, and `research/case-files`.
- Validation files stay thin: source examined, scope, limitations, destinations, and pointer back to this patchset.
- All four intake leads are retained and promoted.
- The only non-blocking limitations are: the Wansey PDF is image-only in the current tooling, and the American Biography full page image was not retrieved. Both are still usable from the user-supplied/source-associated text and snippets.

## Coverage inventory

| Lead | Outcome | Source handling | Research destinations |
| --- | --- | --- | --- |
| WikiTree Wauncy-5 plus Wansey PDF | Promote | Add `wansey-medieval-genealogy-1925`; no corpus until the image-only PDF is manually transcribed or OCRed | `research/people/g23-edmund-gurney-fact-sheet.research.md` |
| Pettigrew, "On the House of Gournay," in `Collectanea Archaeologica` | Promote | Add `pettigrew-collectanea-house-gournay-1871`; create raw extracted corpus from printed pp. 174-218 | G37, G36, G35, G34, G33, G32 people files; senior/collateral topic; Gournay, La Ferte, Sigy, Somerset collateral place files; G13/case file for Francis/Keswick/heraldry context |
| `American Biography`, vol. 26, Gurney entry | Promote | Add `american-biography-cyclopedia-v26-gurney-1926`; no corpus unless full page images are later obtained | `research/people/g13-john-gurney-fact-sheet.research.md`; `research/case-files/john-gurney-case-file-v4.md` |
| Farrer, `Honors and Knights' Fees`, vol. 3, Hathi extract | Promote | Add `farrer-honors-knights-fees-v3-gurnay-extracts`; create raw extracted corpus from the supplied PDF extract | G33/G32/senior topic; G27; Bedingham, Oxfordshire, Buckinghamshire, Bedfordshire, Cantley, Caister, Hardingham/Swathings |

## Source registry operations

Update `data/sources.json` in place. Preserve local ordering and update `meta.lastUpdated` to the phase 2 application date. Insert the following entries near related Gurnay, source-extract, and American-line sources.

```json
"wansey-medieval-genealogy-1925": {
  "shortTitle": "Wansey, ancient family of the Wanseys",
  "citation": "\"Genealogy of the ancient Family of the Wanseys olim Waunci,\" copied from William Wansey, F.S.A., manuscript books on the Wansey family, 1873; PDF hosted by Nick Delves, 1925 file naming.",
  "archive": "Nick Delves Wansey family site / local media",
  "url": "https://www.nickdelves.co.uk/wansey/wansey/1925_08Wansey_Family_Tree_Medieval_Genealogy.pdf",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": "sources/media/1925_08Wansey_Family_Tree_Medieval_Genealogy.pdf",
  "validationPath": "sources/validations/wansey-medieval-genealogy-1925.md",
  "notes": "Image-only four-page Wansey/Wauncy pedigree PDF. User-supplied source-associated extract reports Edmund Gorney d. 1387; Katherine surviving until 3 Henry IV; son John Gurney married Alice Bavard, was knight of the shire in 6 Henry IV, and died in 9 Henry IV. Use as a direct conflict note against HoP/DG wife-name and date details."
}
```

```json
"pettigrew-collectanea-house-gournay-1871": {
  "shortTitle": "Pettigrew, On the House of Gournay",
  "citation": "Pettigrew, T. J. \"On the House of Gournay.\" Collectanea Archaeologica: Communications Made to the British Archaeological Association, vol. 2. London: Longmans, Green, and Co., 1871, pp. 174-218.",
  "archive": "Google Books / local media PDF",
  "url": "https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/pettigrew-collectanea-house-gournay-1871.txt",
  "mediaPath": "sources/media/Collectanea_Archaeologica.pdf",
  "validationPath": "sources/validations/pettigrew-collectanea-house-gournay-1871.md",
  "notes": "Public-domain British Archaeological Association paper reviewing Daniel Gurney's privately printed Record of the House of Gournay. Useful as an accessible page-scoped digest for the Gournay-en-Bray church/fortification landscape, La Ferte and Sigy charter complex, early G32-G37 genealogy, Norfolk merchant/Keswick line, heraldry, and the Somerset collateral Gournays."
}
```

```json
"american-biography-cyclopedia-v26-gurney-1926": {
  "shortTitle": "American Biography, vol. 26 - Gurney",
  "citation": "American Biography: A New Cyclopedia. Illustrated vol. 26. New York: The American Historical Society, Inc., 1926, David Allston Gurney/Gurney family entry, pp. 230-255.",
  "archive": "Google Books; user-supplied extract",
  "url": "https://www.google.com/books/edition/American_Biography/tnkKAQAAMAAJ",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": "sources/validations/american-biography-cyclopedia-v26-gurney-1926.md",
  "notes": "Derivative American-line biographical/genealogical entry. User extract includes John Gurney of Braintree, a probable Southwark origin tradition, and the statement that arms kept by American Gurneys show connection with the Norfolk Gurneys. Use the arms statement as a moderate positive family-memory/heraldic lead for Candidate B; do not use the birth/Southwark assertions as controlling facts."
}
```

```json
"farrer-honors-knights-fees-v3-gurnay-extracts": {
  "shortTitle": "Farrer, Honors and Knights' Fees, vol. 3 - Gurnay extracts",
  "citation": "Farrer, William. Honors and Knights' Fees: An Attempt to Identify the Component Parts of Certain Honors and to Trace the Descent of the Tenants of the Same Who Held by Knight's Service or Serjeanty from the Eleventh to the Fourteenth Century. Vol. 3. London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925, selected Gurnay/Gournay pages.",
  "archive": "HathiTrust public-domain PDF extract",
  "url": "https://hdl.handle.net/2027/mdp.39015032992151",
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/farrer-honors-knights-fees-v3-gurnay-extracts.txt",
  "mediaPath": "sources/media/mdp-39015032992151-158-312-314-333-406-407-436-439-1777765448.pdf",
  "validationPath": "sources/validations/farrer-honors-knights-fees-v3-gurnay-extracts.md",
  "notes": "Public-domain HathiTrust extract pages for Gurnay/Gournay/Gurney entries. Especially useful for the Stutevill/Gurnai fee in South Wootton, Bedingham, and Kimberley; John de Gurney at Evesham; Honor of Warenne tenant table; Mapledurham/Wendover/Houghton Regis/Bledlow/Cantley/Caister/Swathings evidence."
}
```

If phase 2 touches the existing HoP Sir John Gurney source, update only the URL field:

```json
"url": "https://www.historyofparliamentonline.org/volume/1386-1421/member/gurney-john-1408"
```

## File operations

Copy the raw lead file into the archive after the phase 2 content edits are applied:

```powershell
Copy-Item -LiteralPath 'C:\Users\allen\Downloads\Future research urls3.md' -Destination 'sources\intake\archive\v10-future-research-urls3.md'
```

Keep/stage these media files:

```text
sources/media/1925_08Wansey_Family_Tree_Medieval_Genealogy.pdf
sources/media/Collectanea_Archaeologica.pdf
sources/media/mdp-39015032992151-158-312-314-333-406-407-436-439-1777765448.pdf
```

Create these corpus files as source text extracts, not analysis. Use the bundled Python runtime if normal Python is not on PATH; replace `$py` with the actual runtime path from `load_workspace_dependencies` if needed.

```powershell
$py = 'C:\Users\allen\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
@'
from pathlib import Path
from pypdf import PdfReader

pdf = Path("sources/media/Collectanea_Archaeologica.pdf")
out = Path("sources/corpus_supplement/pettigrew-collectanea-house-gournay-1871.txt")
reader = PdfReader(str(pdf))
pages = []
for i in range(214, 289):  # PDF pages 215-289, containing printed pp. 174-218.
    pages.append(f"\n\n--- PDF page {i+1} ---\n")
    pages.append(reader.pages[i].extract_text() or "")
out.write_text("Source ID: pettigrew-collectanea-house-gournay-1871\nScope: Collectanea Archaeologica, vol. 2, printed pp. 174-218 / PDF pp. 215-289.\n\n" + "".join(pages), encoding="utf-8")

pdf = Path("sources/media/mdp-39015032992151-158-312-314-333-406-407-436-439-1777765448.pdf")
out = Path("sources/corpus_supplement/farrer-honors-knights-fees-v3-gurnay-extracts.txt")
reader = PdfReader(str(pdf))
pages = []
for i, page in enumerate(reader.pages):
    pages.append(f"\n\n--- PDF page {i+1} ---\n")
    pages.append(page.extract_text() or "")
out.write_text("Source ID: farrer-honors-knights-fees-v3-gurnay-extracts\nScope: user-supplied HathiTrust Gurnay/Gournay/Gurney extract pages.\n\n" + "".join(pages), encoding="utf-8")
'@ | & $py -
```

Do not create a Wansey corpus file in phase 2 unless the image-only PDF is manually transcribed or OCRed.

## Validation files

Create `sources/validations/wansey-medieval-genealogy-1925.md`:

```markdown
# Source validation: Wansey medieval genealogy PDF

Source ID: `wansey-medieval-genealogy-1925`
Patchset: `sources/intake/processed/v10-future-research-urls3.patchset.md`

## Scope examined

- URL lead: https://www.wikitree.com/wiki/Wauncy-5
- Source PDF: `sources/media/1925_08Wansey_Family_Tree_Medieval_Genealogy.pdf`
- User-supplied transcription attached to the intake file.

## Status

Usable for a conflict note in `research/people/g23-edmund-gurney-fact-sheet.research.md`. The PDF is image-only in this environment, so no verbatim quotation from the page image is added.

## Findings landed

- `research/people/g23-edmund-gurney-fact-sheet.research.md`
```

Create `sources/validations/pettigrew-collectanea-house-gournay-1871.md`:

```markdown
# Source validation: Pettigrew, "On the House of Gournay"

Source ID: `pettigrew-collectanea-house-gournay-1871`
Patchset: `sources/intake/processed/v10-future-research-urls3.patchset.md`

## Scope examined

- Google Books URL: https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ
- Local PDF: `sources/media/Collectanea_Archaeologica.pdf`
- Examined printed pp. 174-218 / PDF pp. 215-289, the full article "On the House of Gournay."

## Status

Usable. Full text extract is in `sources/corpus_supplement/pettigrew-collectanea-house-gournay-1871.txt`.

## Findings landed

- G32-G37 research companions
- `research/topics/anderson-yvery-harpetre-gournay-collateral.md`
- `research/places/gournay-en-bray.md`
- `research/places/la-ferte-en-bray.md`
- `research/places/sigy-normandy.md`
- `research/places/somerset-gournay-collateral.md`
- G13/case-file arms and Norfolk-line context
```

Create `sources/validations/american-biography-cyclopedia-v26-gurney-1926.md`:

```markdown
# Source validation: American Biography, vol. 26 - Gurney

Source ID: `american-biography-cyclopedia-v26-gurney-1926`
Patchset: `sources/intake/processed/v10-future-research-urls3.patchset.md`

## Scope examined

- Google Books URL: https://www.google.com/books/edition/American_Biography/tnkKAQAAMAAJ
- User-supplied extract in the intake file.
- Google Books snippets confirming the Gurney entry around p. 230 and source list around p. 255.

## Status

Usable for derivative-source and family-arms lead. Full page images were not retrieved in phase 1, so the Southwark and 1615 claims are not promoted as controlling facts.

## Findings landed

- `research/people/g13-john-gurney-fact-sheet.research.md`
- `research/case-files/john-gurney-case-file-v4.md`
```

Create `sources/validations/farrer-honors-knights-fees-v3-gurnay-extracts.md`:

```markdown
# Source validation: Farrer, Honors and Knights' Fees, vol. 3 - Gurnay extracts

Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`
Patchset: `sources/intake/processed/v10-future-research-urls3.patchset.md`

## Scope examined

- HathiTrust URL: https://hdl.handle.net/2027/mdp.39015032992151
- Local PDF extract: `sources/media/mdp-39015032992151-158-312-314-333-406-407-436-439-1777765448.pdf`
- All pages in the supplied extract PDF.

## Status

Usable. Full text extract is in `sources/corpus_supplement/farrer-honors-knights-fees-v3-gurnay-extracts.txt`.

## Findings landed

- `research/topics/anderson-yvery-harpetre-gournay-collateral.md`
- `research/people/g27-sir-john-de-gournay-i-fact-sheet.research.md`
- `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`
- `research/people/g32-gerard-de-gournay-fact-sheet.research.md`
- Bedingham, Oxfordshire, Buckinghamshire, Bedfordshire, Cantley, Caister, and Hardingham/Swathings place files
```

## Research operations - G23 Edmund and Sir John d. 1408

Append this block to `research/people/g23-edmund-gurney-fact-sheet.research.md` under `## Conflicting Information`, before the table if possible; otherwise append immediately before `## Fact Sheet Improvement Notes`.

```markdown
### Wansey pedigree conflict: Alice Bavard, Katherine's death date, and Sir John's regnal dates

The Wansey/Wauncy pedigree lead preserves a close but conflicting collateral-line version of Edmund Gurney's family. It agrees with the settled frame that Edmund Gorney died in 1387 and that his son John died in 9 Henry IV, but it says Katherine survived Edmund until 3 Henry IV (1401/2), identifies John's wife as Alice Bavard, and says John was knight of the shire in 6 Henry IV. The wife's name is the material conflict: HoP identifies Sir John's wife as Alice Heylesdon, while the Wansey pedigree supplies Alice Bavard. Keep the Wansey form beside the HoP and DG material as a real pedigree witness, but do not replace Heylesdon unless the Bavard/Heylesdon discrepancy can be resolved by alias, remarriage, or a page-image transcription error.[^wansey-pedigree-g23]

[^wansey-pedigree-g23]: "Genealogy of the ancient Family of the Wanseys olim Waunci," copied from William Wansey, F.S.A., manuscript books on the Wansey family, 1873, PDF hosted by Nick Delves, https://www.nickdelves.co.uk/wansey/wansey/1925_08Wansey_Family_Tree_Medieval_Genealogy.pdf; user-supplied transcription in `C:\Users\allen\Downloads\Future research urls3.md`. Source ID: `wansey-medieval-genealogy-1925`.
```

Add this row to the G23 conflict table if the table remains immediately below the new section:

```markdown
| Sir John Gurney's wife | HoP: Alice Heylesdon | Wansey pedigree: Alice Bavard | Preserve both. Check for alias/remarriage/transcription before changing the preferred HoP form. |
```

## Research operations - G13 John Gurney and Candidate B

In `research/people/g13-john-gurney-fact-sheet.research.md`, insert this subsection after `### External compiler assessments (Anderson, Banks)` and before `### Combined Anderson + Banks assessment`.

```markdown
### American Biography, colonial arms, and the Norfolk-line memory

The 1926 *American Biography* entry for David Allston Gurney is derivative on colonial vital details, but it preserves one family-memory claim that belongs in the Candidate B evidence set: "The Gurney arms kept by the American Gurneys show connection with Norfolk (England) Gurneys." The same extract gives the familiar but problematic tradition that John Gurney was born in England on 29 September 1615, came "probably from Southwark, near London Bridge," settled at Braintree, died in 1663, and had sons Richard and John at Weymouth. Those vital and origin statements conflict with this file's older-father chronology and two-Johns/Newgate deconflation, so they should not be treated as controlling facts.[^american-biography-g13]

The arms statement is different. It is not proof of parentage, but if the American arms can be traced to an early object, seal, Bible, bookplate, gravestone, manuscript, or family paper belonging to the Braintree/Weymouth line, it would be a moderate positive indicator for Candidate B. Francis Gurney's family belonged to the Norfolk line whose arms were argent, a cross engrailed gules; a genuinely inherited American use of that arms tradition would fit the Norfolk hypothesis better than the Bucks, Herts, Kent, or separate London same-name candidates. If the arms prove to be copied from Burke, Daniel Gurney, or late nineteenth-century antiquarian print, the evidentiary value drops to near zero.[^american-biography-g13][^pettigrew-heraldry-g13]

[^american-biography-g13]: *American Biography: A New Cyclopedia*, illustrated vol. 26 (New York: The American Historical Society, Inc., 1926), David Allston Gurney/Gurney family entry, pp. 230-255; Google Books, https://www.google.com/books/edition/American_Biography/tnkKAQAAMAAJ; user-supplied extract in `C:\Users\allen\Downloads\Future research urls3.md`. Source ID: `american-biography-cyclopedia-v26-gurney-1926`.
[^pettigrew-heraldry-g13]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), p. 206, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Append this item to the `## Target Source Pulls / Not Yet Searched` section in the same G13 file:

```markdown
| American Gurney arms object or earliest citation | Locate the earliest physical or manuscript witness for the arms "kept by the American Gurneys"; record blazon, owner, date, and whether it predates Daniel Gurney/Burke-style antiquarian copying | High for Candidate B corroboration |
```

In `research/case-files/john-gurney-case-file-v4.md`, insert this subsection in `### 10.7 Evidence Summary`, immediately after the `#### For Candidate B` table. Preserve the existing HTML/citation style by adding the next available note number in place of `NN`.

```html
<h4>Supplemental heraldic family-memory lead: American Gurney arms</h4>
<p>A 1926 American biographical entry for David Allston Gurney repeats the colonial Gurney descent and states that arms kept by the American Gurneys connected the family with the Norfolk Gurneys. This is not parentage proof: the entry is derivative, repeats the problematic 1615/Southwark tradition, and the arms themselves have not yet been traced to an object, seal, bookplate, gravestone, Bible, or family paper. Still, if the American arms can be shown to descend from the Braintree/Weymouth line rather than from nineteenth-century antiquarian copying, they would be a moderate positive indicator for Candidate B because Francis Gurney's family belonged to the Norfolk line using the cross engrailed arms.<sup class="fn"><a href="#nNN" id="ref-NN">NN</a></sup></p>
```

Add this row to the `#### For Candidate B` evidence table in the same case file:

```markdown
| 10 | American Gurney arms | Moderate if early; weak if late | A 1926 American biographical entry says arms kept by American Gurneys connected them with the Norfolk Gurneys. The lead supports Candidate B only if an early American object or manuscript witness can be found. |
```

Add this item to `### For Strong Supporting Evidence`:

```html
<li><strong>American Gurney arms:</strong> locate the earliest object, seal, Bible, bookplate, gravestone, manuscript, or family paper preserving the arms used by the American Gurneys; determine the exact blazon and whether the usage predates printed antiquarian borrowing.</li>
```

Add this citation note to the case-file citation list, renumbered to the `NN` used above:

```html
<li id="nNN"><em>American Biography: A New Cyclopedia</em>, illustrated vol. 26 (New York: The American Historical Society, Inc., 1926), David Allston Gurney/Gurney family entry, pp. 230-255; Google Books, <a href="https://www.google.com/books/edition/American_Biography/tnkKAQAAMAAJ">https://www.google.com/books/edition/American_Biography/tnkKAQAAMAAJ</a>. Source ID: <code>american-biography-cyclopedia-v26-gurney-1926</code>. Pettigrew separately summarizes the Norfolk arms as argent, a cross engrailed gules: T. J. Pettigrew, "On the House of Gournay," <em>Collectanea Archaeologica</em>, vol. 2 (London: Longmans, Green, and Co., 1871), p. 206. Source ID: <code>pettigrew-collectanea-house-gournay-1871</code>. <a class="backref" href="#ref-NN">↩</a></li>
```

## Research operations - Pettigrew and Farrer generation mapping

Use this mapping while applying the person-file edits:

```text
Pettigrew Eudes / Rollo tradition -> G37 Eudes (tradition only)
Pettigrew Hugh son of Eudes / La Tour Hue -> G36 Hugh I
Pettigrew Renaud/Reginald, Alberarda, sons Hugh and Gautier -> G35 Renaud
Pettigrew Hugh de Gournay II, 1035/1066/witnesses/Cardiff problem -> G34 Hugh II
Pettigrew Hugh de Gournay III, Domesday Essex, Basilia Flaitel, Bec -> G33 Hugh III
Pettigrew Gerard, Edith/Ediva de Warenne, Crusade, children incl. Walter -> G32 Gerard
Farrer Mapledurham first paragraph, Hugh held Liston/Ardleigh/Fordham and became monk at Bec -> G33 Hugh III
Farrer Gerard and Edith had several children including Hugh II (Farrer's numbering) -> G32 Gerard and the senior collateral topic, because that Hugh is the elder senior-line successor, not Allen's direct G31 Walter
Farrer Stephen/John-era Wendover-Houghton-Cantley-Caister sequence -> senior collateral topic and place files, not a direct G31-G27 person file
Farrer 1265 South Wootton/Evesham John de Gurney -> G27 Sir John de Gournay I
```

## Research operations - G37 Eudes

Append this subsection to `research/people/g37-eudes-de-gournay-fact-sheet.research.md` after the existing Planché/Le Brai note.

```markdown
### Pettigrew on Eudes, Le Bray, and the Rollo grant tradition

Pettigrew repeats the same traditional origin frame as DG and Hannay but with useful place detail. In his summary, Rollo divided Neustria among his chieftains in return for homage and military service; Eudes was named as a leader in Rollo's army; and the town of Gournay with the Norman part of Le Bray was assigned to him. Pettigrew describes Le Bray as "for the most part of forest and morass," matching the marshy frontier landscape already attached to the Gournay name. This remains a nineteenth-century transmission of local/family tradition, not a contemporary charter for Eudes, but it is a clean additional witness to the same origin story.[^pettigrew-eudes]

[^pettigrew-eudes]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 176, 180, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Add `pettigrew-collectanea-house-gournay-1871` to the G37 Sources Consulted list.

## Research operations - G36 Hugh I

Append this subsection to `research/people/g36-hugh-de-gournay-i-fact-sheet.research.md` after the existing Planché fortification note.

```markdown
### Pettigrew on La Tour Hue and the fortified town

Pettigrew strengthens the existing Hugh I fortification note by placing the tower inside a broader town landscape. He says the town of Gournay was fortified by "Hugh son of Eudes" and that a citadel secured by the tower known as La Tour Hue continued as late as the seventeenth century. He also lists the defensive and religious geography associated with the lords of Gournay: La Ferte, Gaillefontaine, Argueil, Bref-Moutier, Beaubec, Bellozane, Chair-ruissel, St Aubin, Sigi, St Laurent, La Ferte, and religious houses in the town itself. The point for Hugh I is not that all later institutions belonged to his lifetime, but that the tradition remembered his work as the first fortification layer around which the later Gournay landscape grew.[^pettigrew-hugh1]

[^pettigrew-hugh1]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 176, 180, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Add `pettigrew-collectanea-house-gournay-1871` to the G36 Sources Consulted list.

## Research operations - G35 Renaud

Append this subsection to `research/people/g35-renaud-de-gournay-fact-sheet.research.md` after `### Planché on Renaud, Alberada, and La Ferté`.

```markdown
### Pettigrew on Renaud, Alberarda, La Ferte, and Sigy

Pettigrew's account is especially useful for Renaud because it restates the family cluster in one connected passage. He says Renaud or Reginald is the first lord of Gournay named in any written deed or instrument; his name occurs in Gautier de la Ferte's foundation deed for the Priory of La Ferte-en-Bray; the deed was made at the command of Gautier's brother Hugh; and the witness/dating frame places it between 989 and 996. Pettigrew then says the charter proves that Renaud married Alberarda and had two sons, Hugh and Gautier.[^pettigrew-renaud]

The same passage resolves the Sigy relationship without changing the direct line. Hugh, Renaud's elder son, was lord of Gournay. Gautier, the younger son, had a son Hugh de la Ferte, founder of Sigi; a later Hugh de la Ferte became a monk at St Ouen at Rouen, gave the priory of Sigi to that abbey, and confirmed his father's gifts. By these acts, Pettigrew says, the seignories and lands of La Ferte reverted to the elder branch. This keeps La Ferte and Sigy as early cadet-line documentary places while preserving the direct Renaud -> Hugh line.[^pettigrew-renaud]

[^pettigrew-renaud]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 180-182, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Add `pettigrew-collectanea-house-gournay-1871` to the G35 Sources Consulted list.

## Research operations - G34 Hugh II

Append this subsection to `research/people/g34-hugh-de-gournay-ii-fact-sheet.research.md` after `### Planché and Palgrave on Hugh II's pre-Conquest role`.

```markdown
### Pettigrew on Hugh II, 1035, Hastings, and the Cardiff/Norwich problem

Pettigrew's Hugh II section tracks the same difficult evidence cluster already preserved from DG, Hannay, and Planché. He identifies Hugh de Gournay II as probably the son of Hugh I, one of the Norman leaders of the fleet of forty ships that accompanied Edward the Saxon prince to England on Canute's death in 1035, and the Gournay who accompanied William against Harold in 1066 with men of Bray. Pettigrew quotes the *Roman de Rou* passage for "le viel Hue de Gournai" and notes two charter appearances: one in April 1067 and another before 1066.[^pettigrew-hugh2]

The value of Pettigrew here is not a new conclusion but a sharper statement of uncertainty. He repeats the manuscript tradition that this Hugh was wounded at Cardiff in 1074 and carried to Normandy, but immediately explains the chronological and source problems. He notes DG's lack of confidence in the story, the possibility that "Cardiff" could be "Nortwic" or Norwich, and the parallel suggestion that the event may belong near the rebellion of Ralf Guader and the eastern counties. Keep the fact-sheet line cautious: Hugh II is a pre-Conquest and Conquest-era Gournay, but the Cardiff/Norwich death tradition remains unresolved.[^pettigrew-hugh2]

[^pettigrew-hugh2]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 182-184, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Add `pettigrew-collectanea-house-gournay-1871` to the G34 Sources Consulted list.

## Research operations - G33 Hugh III

Append these subsections to `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md` after `### Planché on Basilia and the Hastings-generation problem`.

```markdown
### Pettigrew on Basilia, Bec, and Hugh III's last years

Pettigrew places Basilia in the same high Norman kin network used by DG: she was daughter of Gerard Flaitel or Flaiteaux, widow of Raoul de Vace or Gace, and sister of Walter Giffard's wife; William, Bishop of Evreux, and Anscherius were her brothers. Pettigrew also gives the monastic ending of the couple's life: Hugh became a monk at Bec, Basilia retired there and received the veil from the Archbishop of Rouen, Anselm held them in affection, and Hugh was buried in the abbey church with Basilia entombed near him. He notes DG's own caution that Hugh may not actually have been prior of St Nicaise de Meulan, because Anselm's letter to Basilia does not mention Hugh and he may already have died.[^pettigrew-hugh3-basilia]

Pettigrew's account of Hugh's gifts to Bec is also useful for the place network. Hugh gave the church of Massy, the tithe of Gournay, Elboeuf, Brefmoutier, Merval, Laudencourt, the tithes of his three English manors, and half the *molta*, a tax paid by vassals for grinding corn at the lord's mill. These were confirmed by Basilia and their son Gerard. The three English manors are the same Domesday Essex cluster: Fordham, Liston, and Ardleigh.[^pettigrew-hugh3-basilia]

[^pettigrew-hugh3-basilia]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 183-185, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

```markdown
### Farrer on Hugh III's English holdings and the Warenne connection

Farrer's Mapledurham section independently controls the English-tenure side of the Hugh III file. He says the Gournay-sur-Epte family in the Pays de Bray held much of its English property through the marriage connection with Ediva/Edith de Warenne, but he first identifies Hugh as holder of the three Domesday Essex manors of Liston, Ardleigh, and Fordham, none of which descended in his line. Farrer also says Hugh became a monk at Bec, and assigns to Basilia and her son Hugh the gifts to Bec of a moiety of Longueil and Le Bois de Girard. This is useful because it separates Hugh III's Domesday Essex holdings from the later Mapledurham/Wendover/Houghton Regis senior-line descent.[^farrer-hugh3]

[^farrer-hugh3]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, extracted PDF pp. 10-12, HathiTrust, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

Add `pettigrew-collectanea-house-gournay-1871` and `farrer-honors-knights-fees-v3-gurnay-extracts` to the G33 Sources Consulted list.

## Research operations - G32 Gerard

Append these subsections to `research/people/g32-gerard-de-gournay-fact-sheet.research.md` after `### Planché collateral and Norman-command notes`.

```markdown
### Pettigrew on Gerard, Edith de Warenne, and the younger-son branch

Pettigrew gives Gerard a fuller connective role between the senior Norman barons and the later Norfolk line. He says Gerard first appears in the 1082 foundation deed of Holy Trinity at Caen and made many donations to Bec. He married Editha or Ediva, daughter of William de Warenne, first Earl of Surrey, by Gundred. Pettigrew emphasizes the Warenne scale: William de Warenne held 296 manors at Domesday, including 139 in Norfolk, founded Lewes and Castle Acre priories, and died in 1089.[^pettigrew-gerard]

For Gerard's death and children, Pettigrew follows DG's two-journey solution. Gerard joined the Crusade in September 1096, reached Jerusalem, returned to Normandy, was living in 1104, and died on a second journey to Jerusalem accompanied by Edith, who returned and married Dreux de Monceaux. Pettigrew names one son Hugh and two daughters, one married to Richard de Talbot and the other to Neil d'Albini, then adds that another son Renaud has been ascribed to him and that DG thought Walter de Gournai was another. That last sentence is the direct-line junction: Walter, holder of Suffolk lands in Stephen's reign, was ancestor of the Gurneys of West Barsham in Norfolk.[^pettigrew-gerard]

[^pettigrew-gerard]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 185-186, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

```markdown
### Farrer on Gerard, Edith, and the senior collateral inheritance

Farrer agrees with the core Gerard/Edith framework but uses it to explain later feudal holdings rather than family narrative. He says Gerard and Edith had several children, including Hugh II in Farrer's numbering, and that Edith married Drew de Monceaux after Gerard died in the Crusades. The same section then follows the senior successor Hugh into Wendover, Houghton Regis, Mapledurham, Bledlow, Cantley, Caister, and Swathings. For this file, the point is that Gerard's Warenne marriage is the hinge between Hugh III's Domesday/Bec world and the later senior-line English fee descent; the detailed later holdings belong in the senior/collateral topic and place files rather than under Allen's direct G31-G27 line.[^farrer-gerard]

[^farrer-gerard]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, extracted PDF pp. 10-12, HathiTrust, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

Add `pettigrew-collectanea-house-gournay-1871` and `farrer-honors-knights-fees-v3-gurnay-extracts` to the G32 Sources Consulted list.

## Research operations - G27 Sir John de Gournay I

Append this subsection to `research/people/g27-sir-john-de-gournay-i-fact-sheet.research.md` after `### South Wootton seizure - full plea text (DG-Supp Note 112)`.

```markdown
### Farrer corroboration: South Wootton, Evesham, and the rebel seizure

Farrer gives a compact independent control for the South Wootton seizure. In his account of the Gurnai fee after Bardolf, he says that in 1265 John de Bulemer was attached to answer Alice de Balesham for taking her goods in Wootton. Bulemer answered that he went to the manor of John de Gurney in South Wootton and seized it because John "was in the conflict of Evesham against the king," treating the manor as that of the king's enemy. Farrer's wording names Evesham where DG's longer plea emphasizes Lewes and resistance after Lewes; together they show the same rebel arc from Montfortian conflict to post-Evesham forfeiture pressure.[^farrer-g27-wootton]

[^farrer-g27-wootton]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Honor of Arundel, p. 142, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

Add `farrer-honors-knights-fees-v3-gurnay-extracts` to the G27 Sources Consulted list.

## Research operations - senior/collateral topic

Append this section to `research/topics/anderson-yvery-harpetre-gournay-collateral.md` before `## Sources`.

```markdown
## Pettigrew and Farrer additions from Future Research URLs 3

### Pettigrew's Collectanea article as detailed DG digest

Pettigrew's 1871 "On the House of Gournay" is a derivative article, but it is not disposable. It is an unusually dense public digest of Daniel Gurney's privately printed *Record*, preserving the sequence of early Norman places, religious houses, monuments, heraldry, and collateral branches in a form that can be cited page by page. It is especially useful for Gournay-en-Bray's St Hildevert church and La Tour Hue, the La Ferte/Sigy charter complex, the Basilia/Bec material, the Gerard/Edith de Warenne marriage network, and the Somerset collateral Gournays.[^topic-pettigrew-v10]

For the direct line, Pettigrew maps cleanly onto the existing G37-G32 structure: Eudes as Rollo-era tradition; Hugh son of Eudes as the fortifier; Renaud with wife Alberarda and sons Hugh and Gautier; Hugh II as the 1035/1066 figure with the Cardiff/Norwich death problem; Hugh III as the Domesday Essex/Basilia/Bec figure; and Gerard as the Warenne-married Crusader whose probable younger son Walter begins the later West Barsham/Norfolk line. The senior collateral lords after Gerard belong in this topic file and place files, not in the direct-line person sequence.[^topic-pettigrew-v10]

### Farrer as feudal-tenure control

Farrer's *Honors and Knights' Fees*, vol. 3, gives a stronger control source for land descent than the narrative antiquaries. On the Honor of Arundel page, he treats the fee of Gurnai after Bardolf in South Wootton, Bedingham, and Kimberley, held by the Stutevills. The same section records the 1207 restoration of Kimberley and Bedingham to Nicholas de Stutevill, grandson of Hugh de Gurnai, and the 1265 South Wootton seizure against John de Gurney as a king's enemy after Evesham.[^topic-farrer-v10]

In the Honor of Warenne material, Farrer connects Mapledurham to the Gournay-sur-Epte family and the Warenne marriage. He identifies Hugh's Domesday Essex manors of Liston, Ardleigh, and Fordham; Gerard and Edith de Warenne's children; Stephen's grant of Wendover to the senior successor Hugh; Houghton Regis and Wendover passing in and out of royal hands; Bledlow exchanged with Bec; Gaille-Fontaine, Bellozanne, and St Aubin foundations; the 1203 seizure of Cantley, Caister, and other Hugh de Gurnay lands after withdrawal from King John's service; Swathings as land of the same fee; and Juliana de Gurnay's Mapledurham inheritance passing to the Bardolfs.[^topic-farrer-mapledurham-v10]

This source does not change the direct Norfolk junior-branch descent. It sharpens the distinction between inherited senior-line fees and the later junior Norfolk line. The South Wootton/Evesham item belongs with G27 because it is the same rebel-era John already documented by DG; the Mapledurham/Wendover/Houghton Regis/Cantley/Caister/Swathings sequence belongs primarily to the senior collateral topic and place files.

### Pettigrew's Somerset Gournays as collateral comparison

Pettigrew's Somerset section belongs here as collateral comparison, not in the direct line. It traces the Somerset Gournays from Nigellus de Gurnai in the Exon Domesday through Hawisa de Gournay, who held Barew and Inglishcombe in the reigns of Stephen and Henry II and retained her paternal surname through three marriages. Her daughter Eva, wife of Thomas son of William de Harptree, also retained and transmitted the Gournay name. Robert de Gournay then united the Somerset Gournay, Harptree, and FitzHarding of Weare inheritances, and Anselm's sons divided the houses of Harptree, Overwere, and Inglishcombe.[^topic-pettigrew-somerset-v10]

The later collateral details are genealogically rich but separate: Sir Thomas de Gournay the regicide descends from the Inglishcombe branch; Joan his widow recovered Farington, Inglescombe, and West Harptree in 8 Edward III; Sir Matthew de Gournay, fourth son of the regicide, fought at Sluys, Crecy, Poitiers, and Najera, governed Brest, was imprisoned in the Tower in 1363 with John de St Lo, returned wealthy, and lived at Stoke Hamdon. Pettigrew also preserves Leland's description of the Stoke manor/castle, chapel tombs, and Matthew's long French epitaph. Keep these places together in `research/places/somerset-gournay-collateral.md` unless later work needs separate files.[^topic-pettigrew-somerset-v10]

[^topic-pettigrew-v10]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 174-218, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
[^topic-farrer-v10]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Honor of Arundel, p. 142, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
[^topic-farrer-mapledurham-v10]: Farrer, *Honors and Knights' Fees*, vol. 3, Mapledurham section, extracted PDF pp. 10-12. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
[^topic-pettigrew-somerset-v10]: Pettigrew, "On the House of Gournay," pp. 210-216. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

## Place operations - Gournay-en-Bray

In `research/places/gournay-en-bray.md`, insert this section after `## The church and the surviving site`.

```markdown
## St Hildevert, La Tour Hue, and the religious landscape in Pettigrew

Pettigrew's *Collectanea* article makes the built and religious landscape of Gournay-en-Bray much more concrete. He repeats the tradition that Hugh son of Eudes fortified the town and that a citadel tower known as La Tour Hue survived into the seventeenth century. He also lists the wider Gournay lordship's fortifications and religious houses: La Ferte, Gaillefontaine, Argueil, Bref-Moutier, Beaubec, Bellozane, Chair-ruissel, St Aubin, Sigi, St Laurent, La Ferte, and houses in the town of Gournay itself.[^pettigrew-gournay-place]

The article gives especially rich detail for St Hildevert. Pettigrew says no records of the church before 1180 were then known, but he places the standing fabric in a sequence of Gournay patronage: Hugh IV repaired and beautified the church; Hugh V took the lordship in 1180 as the pointed style was emerging; Walter, Archbishop of Rouen, and Hubert, Archbishop of Canterbury, attended the dedication and translation of St Hildevert's relics into a silver shrine around 1201; and Hugh's banishment/confiscation soon after deprived the canons of their protector and slowed the building campaign. This gives the church more than a generic site role: it is the visible monument of the senior barons' last Norman generation before the Capetian loss.[^pettigrew-gournay-place]

[^pettigrew-gournay-place]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 176-179, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Add `pettigrew-collectanea-house-gournay-1871` to the Sources list.

## Place operations - La Ferte-en-Bray

In `research/places/la-ferte-en-bray.md`, insert this section after `## Planché's La Ferté caution`.

```markdown
## Pettigrew on the La Ferte priory and its distinction from the Cistercian La Ferte

Pettigrew sharpens the La Ferte file in two ways. First, he restates the family proof: Renaud married Alberarda and had sons Hugh and Gautier; Gautier's son Hugh de la Ferte founded Sigi; a later Hugh de la Ferte became a monk at St Ouen at Rouen, gave Sigi to that abbey, and confirmed his father's gifts, after which the seignories and lands of La Ferte reverted to the elder Gournay branch.[^pettigrew-laferte]

Second, he distinguishes the early Gournay-related priory from a similarly named institution. He says a priory of canons and church dedicated to St Peter and St Paul were founded before 990; about 1151 the canons were transferred to St Laurent-en-Lions; and the ancient priory of La Ferte is not to be confused with the Cistercian monastery of La Ferte, founded in 1113, destroyed in 1567, and afterwards revived. That distinction should stay visible because otherwise a later Cistercian La Ferte can be accidentally substituted for the early Gournay document-place.[^pettigrew-laferte]

[^pettigrew-laferte]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 180-181, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Add `pettigrew-collectanea-house-gournay-1871` to the Sources list.

## Place operations - create Sigy

Create `research/places/sigy-normandy.md`:

```markdown
# Sigy, Normandy - Research Notes

Sigy belongs in the place library as an early Gournay cadet-line priory and charter site, not as a generic Norman locality. Pettigrew places it on the eastern border of the lordship of Gournay, three or four miles from La Ferte, and says the church was dedicated to St Martin. He treats its pre-1035 foundation charter as "the earliest known charter of the Lords of Gournay," with another charter of 1047 and a confirmation by Henry II of England.[^pettigrew-sigy]

The genealogical value is the La Ferte cadet sequence. Renaud de Gournay married Alberarda and had sons Hugh and Gautier. Gautier's son Hugh de la Ferte founded Sigi; another Hugh de la Ferte became a monk at St Ouen at Rouen and gave the priory of Sigi to that abbey, confirming his father's gifts. Pettigrew says those acts caused the seignories and lands of La Ferte to revert to the elder branch of the Gournay family.[^pettigrew-sigy]

Sigy also has architectural/site value. Pettigrew prints exterior and interior views and says the church then shown was clearly rebuilt in the time of Hugh V or about 1190. The site therefore preserves two different layers: an early-eleventh-century charter foundation and a later-twelfth-century senior-baron rebuilding context.[^pettigrew-sigy]

## Crosslinks

- `research/people/g35-renaud-de-gournay-fact-sheet.research.md`
- `research/places/la-ferte-en-bray.md`
- `research/places/gournay-en-bray.md`

[^pettigrew-sigy]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 181-182, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Do not add Sigy to `data/places.json` in this phase unless the phase 2 task also updates the place registry and generated place pages.

## Place operations - Bedingham

In `research/places/bedingham.md`, append this section before the footnote.

```markdown
## Farrer on the Gurnai fee, Stutevill descent, and South Wootton

Farrer gives Bedingham a tighter feudal frame than Blomefield alone. He places Bedingham with South Wootton and Kimberley in "the fee of Gurnai (after Bardolf)" held by the Stutevills, and says there is no evidence that the Bulmers were Stutevill feoffees. The early sequence is specific: in Michaelmas term 1194 Benedict de Bedingham avowed Nicholas de Stutevill in the advowson dispute over St Mary of Bedingham; in 1197 part of Ralph de Aubigny's land was assigned to Nicholas de Stutevill and Gunnora his wife; in 1205 Kimberley and Bedingham, late of William de Stutevill, were committed to the Cantilupos; and on 3 January 1207 the lands were restored to Nicholas de Stutevill, grandson of Hugh de Gurnai, whose father had been disseised because of the disseisin of the Normans.[^farrer-bedingham]

The later claims keep the Gurnay interest visible even after Stutevill possession. In 1234/5 a fine over land in Kimberley between Roger Buteaute and Nicholas de Stutevill drew a claim from Hugh de Gurnay; in 1239/40 Nicholas was demandant in a fine over the advowson of Bedingham church; and in 1241 he asserted a villeinage claim in a Kimberley fine. Bedingham therefore sits at the junction of senior Gournay inheritance, Stutevill marriage descent through Gunnora, and later Bardolf succession.[^farrer-bedingham]

[^farrer-bedingham]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Honor of Arundel, p. 142, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

Add `farrer-honors-knights-fees-v3-gurnay-extracts` to the Bedingham source list if one is added later.

## Place operations - Oxfordshire

In `research/places/oxfordshire.md`, append this section after `### Mapledurham and the Bardolf/Gournay inheritance`.

```markdown
### Farrer on Mapledurham Gornay

Farrer makes Mapledurham a more detailed senior-line inheritance place. He explains that the Gournay-sur-Epte family of the Pays de Bray held English property through the Warenne marriage network, and then follows Mapledurham through senior Gournay and Bardolf descent. Hugh and Milicent gave the church of Mapledurham and two marks of silver yearly from Caister to the Gaille-Fontaine/Clair-Ruissel nunnery with the assent of their sons Gerard and Hugh. Farrer's 1212 Great Inquest discussion also says Henry II confirmed to Milicent de Gurnay dower including Gaille-Fontaine, Wendover, Houghton Regis, and land that Edith/Ediva mother of Hugh had in England, "possibly a reference to Mapledurham."[^farrer-mapledurham]

The Bardolf succession is exact enough to retain. Matilda, late wife of Hugh de Gurnay, held Mapledurham in dower in 1239. Juliana, daughter and heir of Hugh de Gornay, married William Bardolf the younger. In 1272 William Bardolf and Juliana sued John de Chausy over common of pasture in Mapledurham Chauzey, of which Hugh de Gurnay, Juliana's father, had been seised as belonging to his free tenement in Mapledurham Gornay. William Bardolf died in 1290 holding the manor of Mapledurham as part of Juliana de Gurnay's inheritance, held of the Earl Warenne for one fee. John Bardolf had free warren at Mapledurham in 1304 and was returned as lord of Mapledurham Gornay in 1316.[^farrer-mapledurham]

[^farrer-mapledurham]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

## Place operations - Buckinghamshire

In `research/places/buckinghamshire.md`, append this subsection after the existing `### Wendover and Bledlow in senior Gournay context`.

```markdown
### Farrer on Wendover and Bledlow

Farrer gives the fuller tenure sequence behind the Wendover/Bledlow notes. He says Stephen granted Hugh de Gurnay the important crown manor of Wendover. In 1155 and 1156 Hugh's manors of Wendover and Houghton Regis were in the king's hands at a yearly farm of 60 pounds, and the king then granted Wendover away. In 1173 the king granted Hugh de Gurnay the younger lands in Houghton Regis and in Norfolk and Suffolk worth 50 pounds yearly, but that grant lasted only three months after Hugh's serjeants carried away stock and implements from Wickham and Hintlesham and the sheriff of Buckingham received the farm of Bledlow for the king.[^farrer-bucks]

Farrer also explains the Bec exchange: because of Hugh's loss of Bledlow, Richard I in 1197 confirmed to St Mary of Bec an exchange made by Hugh de Gurnay of rent and tithe in Norman lands for land previously given in his manor of Bledlow. In 1202 King John restored Wendover to Hugh, saving the year's corn crop to Felicia widow of Ingram de Fiennes, and Hugh obtained a yearly fair at Wendover in 1214. This belongs to the senior collateral line and should not be treated as a junior Norfolk holding.[^farrer-bucks]

[^farrer-bucks]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

## Place operations - Bedfordshire

In `research/places/bedfordshire.md`, append this section before the generated registry block.

```markdown
## Houghton Regis in senior Gournay tenure

Farrer ties Houghton Regis to the same senior-line sequence as Wendover and Bledlow. In 1155 and 1156, Hugh de Gurnay's manors of Wendover and Houghton Regis were in the king's hands at a yearly farm of 60 pounds. At Midsummer 1173, Hugh de Gurnay the younger received lands in Houghton Regis and in Norfolk and Suffolk worth 50 pounds yearly, though the grant lasted only three months. Farrer's 1212 Great Inquest discussion says Henry II had confirmed to Milicent de Gurnay dower including the new land Stephen gave to Hugh in augmentation of his inheritance, namely Wendover and Houghton Regis. Richard I restored Houghton Regis to Hugh at his accession, and in 1201 Hugh held it as 40 librates of land.[^farrer-houghton-regis]

This is senior collateral geography. It explains why Bedfordshire appears in the Gournay map, but it does not belong to the direct junior Norfolk line unless a later direct-branch record is found.

[^farrer-houghton-regis]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

## Place operations - Cantley

In `research/places/cantley.md`, append this paragraph to the end of `### Cantley after Gerard: senior Gournay and Bardolf descent`, before the footnotes.

```markdown
Farrer adds the 1203 forfeiture frame. When Hugh de Gurnay withdrew from King John's service, writs were issued for seizure of his lands in Normandy and England. Hugh's land in Cantley and Caister, the land of Hugh de Agee in Norfolk, and all other lands of Hugh de Gurnay "betrayor" in Norfolk and Suffolk were committed to John Marshal, son of William Marshal, Earl of Pembroke. This turns Cantley into one of the named English places affected by the senior baron's break with John, just before the final loss of the Norman lordship.[^farrer-cantley-1203]

[^farrer-cantley-1203]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

## Place operations - Caister-on-Sea

In `research/places/caister-on-sea.md`, append this section before the generated registry block.

```markdown
## Caister in the 1203 senior-line seizure

Farrer gives Caister a precise King John-era seizure context. In May 1203, after Hugh de Gurnay withdrew from John's service, writs were issued to seize his lands in Normandy and England. Hugh's land in Cantley and Caister, the land of Hugh de Agee in Norfolk, and all other lands of Hugh de Gurnay "betrayor" in Norfolk and Suffolk were committed to John Marshal, son of William Marshal, Earl of Pembroke.[^farrer-caister-1203]

The same Mapledurham section also records two marks of silver yearly from Caister as part of the gift to the Gaille-Fontaine/Clair-Ruissel nunnery by Hugh and Milicent, with the assent of their sons Gerard and Hugh. Caister therefore appears both as an income source in senior-line religious patronage and as a named place in the 1203 forfeiture crisis.[^farrer-caister-1203]

[^farrer-caister-1203]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

## Place operations - Hardingham / Swathings

In `research/places/hardingham.md`, append this subsection near the existing Swathings section.

```markdown
### Farrer on Swathings in the senior Gurnay fee

Farrer places Swathings within the senior Gurnay fee after the 1203 seizure of Hugh de Gurnay's lands. After naming Cantley and Caister among the lands committed to John Marshal, he adds that other land in Norfolk of this fee lay in Swathings, where Hugh de Gurnay II had given a manor to Robert de Burgeinuin and Hugh son of the donor confirmed it to Hugh son of Robert de Burguinuin. He also records a grant by Hugh de Gurnay II and Milicent his wife of five librates of land in Bledlow, witnessed by William de Merlo, Oliver de Age, Hodus de Brumustier, Hugh de Burgeinuin, and others.[^farrer-swathings]

This does not displace the later junior-branch Hardingham/Swathings evidence. It adds an earlier senior-line fee layer showing why Swathings belongs in the broader Gurnay place network before the better documented G27-G23 Norfolk descent.

[^farrer-swathings]: William Farrer, *Honors and Knights' Fees*, vol. 3 (London: printed for the author by Spottiswoode, Ballantyne & Co., 1923-1925), Mapledurham section, HathiTrust extract, https://hdl.handle.net/2027/mdp.39015032992151. Source ID: `farrer-honors-knights-fees-v3-gurnay-extracts`.
```

## Place operations - create Somerset collateral aggregate

Create `research/places/somerset-gournay-collateral.md`:

```markdown
# Somerset Gournay Collateral Places - Research Notes

This file gathers collateral Somerset Gournay places that are relevant to surname, heraldry, and comparison work but are not part of Allen's direct Norfolk line. Keep them together unless later research needs a separate place file for a site with enough direct evidence.

## Pettigrew's Somerset collateral sequence

Pettigrew treats the Somerset Gournays as a separate collateral branch beginning with Nigellus de Gurnai in the Exon Domesday. Robert de Gournay is presumed to have been Nigellus's son and father of Hawisa de Gournay. Hawisa held the manors of Barew and Inglishcombe in the reigns of Stephen and Henry II, married three times, and retained her paternal surname of Gournay. By her second husband she had a daughter Eva, wife of Thomas son of William de Harptree; Eva also retained the Gournay name and transmitted it to her descendants.[^pettigrew-somerset-place]

Robert de Gournay, Eva's son, bore paly of six with a label as eldest son and became one of the most powerful western nobles in Henry III's reign. Pettigrew says he eventually united the inheritances of the Somerset Gournays, the barons of Harptree, and the Fitz-Hardings of Weare, and married Hawisa de Longchamp. From Anselm, son of Robert, the Somerset inheritance divided among three houses: John of Harptree, husband of Olivia Lovel of Kari; Robert of Overwere; and Thomas of Inglishcombe, ancestor of Sir Thomas de Gournay the regicide.[^pettigrew-somerset-place]

## Locality leads retained together

- Barrow/Barew Gurney and Englishcombe/Inglishcombe: Hawisa held Barew and Inglishcombe in the reigns of Stephen and Henry II; Pettigrew says the Gournays obtained Inglishcombe immediately after the Norman Conquest.
- Harptree and Weare: Robert de Gournay united the Somerset Gournay, Harptree, and FitzHarding of Weare inheritances.
- Farington, Inglescombe, and West Harptree: restored in 8 Edward III to Joan, widow of Sir Thomas de Gournay the regicide.
- Stoke-sub-Hamdon: Sir Matthew de Gournay lived there after returning wealthy from war. Pettigrew preserves Leland's description of the ruined manor or castle, ancient chapel, tombs of armed men and women, blue-and-white vair shields, and Matthew's French epitaph.
- Bristol / Gaunt's Hospital and St Mark's: Robert de Gournay II confirmed the advowson of Inglishcombe to Bermondsey and was founder or principal benefactor of Gaunt's Hospital in Bristol, supporting a master, three chaplains, and daily relief for one hundred poor persons. His heart was buried at the Friars Preachers in Bristol and his body in St Mark's Chapel.
- Beverstone and Richemonte in Harptree: collateral castle/holding leads tied to later Somerset branches.

## Sir Matthew de Gournay

Sir Matthew de Gournay, fourth son of the regicide Sir Thomas, is a major collateral military figure. Pettigrew says he was about twenty at his father's death, fought from Sluys in 1340 through Crecy, Poitiers, Najera, and other campaigns, was appointed governor of Brest by the Duke of Lancaster with royal confirmation, served as a jurat for Edward III at the peace of Brittany in 1360, became a baron of Guienne with considerable possessions, was imprisoned in the Tower in 1363 with John de St Lo, later fought in Spain, was captured in Picardy in 1377, and returned to England with substantial wealth. His Stoke-sub-Hamdon monument, as copied by Leland, gave a death date of 26 September 1406 and styled him seneschal of Landes and captain of the castle of Dax for the king in Guienne.[^pettigrew-somerset-place]

## Crosslinks

- `research/topics/anderson-yvery-harpetre-gournay-collateral.md`
- `research/places/weare-somerset.md`

[^pettigrew-somerset-place]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 210-216, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Do not add separate `data/places.json` records for Barrow Gurney, Englishcombe, Harptree, Stoke-sub-Hamdon, Bristol, or Beverstone in this patchset. The corrected phase 1 decision is to keep them in one compact aggregate research place file.

## Optional place cross-reference - Weare, Somerset

In `research/places/weare-somerset.md`, append this sentence if it does not duplicate existing text:

```markdown
Pettigrew's Somerset Gournay section places Weare inside the collateral inheritance bundle united by Robert de Gournay, who combined the Somerset Gournay, Harptree, and FitzHarding of Weare inheritances; detailed collateral locality notes are gathered in `research/places/somerset-gournay-collateral.md`.[^pettigrew-weare-v10]

[^pettigrew-weare-v10]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 210-211, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

## Pettigrew/Keswick line operation

In `research/people/g14-francis-gurney-fact-sheet.research.md`, insert this subsection immediately after `### King's Lynn worsted-yarn venture, 1622` and before `### Lestrange household references`.

```markdown
### Pettigrew on Francis Gurnay of London and the Keswick commercial line

Pettigrew's digest of DG gives a useful public-domain restatement of Francis Gurnay of London's place in the later Norfolk/Keswick branch. Francis was the sixth son of Henry Gurnay of West Barsham and Great Ellingham by Ellen Blennerhassett, was admitted to the Merchant Taylors' Company on 16 June 1606, lived in St Benet Fink, and married a daughter of William Browning, merchant of Norwich. Pettigrew also prints the King's Lynn worsted-yarn enterprise terms, including the corporation's loan to Francis Gurnay of London, Ambrose Tompson of Thetford, and Martyne Hill of Ellingham to provide wool and materials and teach poor children and poor inhabitants to spin worsted yarn and do related work.[^pettigrew-francis-g14]

The same section connects Francis to the later commercial Gurneys without making them part of the American-line proof. Francis's second son Francis of Maldon had an eldest son John, born in 1655, apprenticed to Daniel Gilman of Norwich, who entered the silk trade, married Elizabeth Swanton, became a Quaker, suffered imprisonment at Norwich in 1683/4, and laid the commercial foundation of the Gurneys of Keswick. This is useful background for the Norfolk textile/commercial world around Candidate B, but it is not direct evidence that John Gurney-1 of Braintree was Francis's son.[^pettigrew-francis-g14]

[^pettigrew-francis-g14]: T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (London: Longmans, Green, and Co., 1871), pp. 207-210, Google Books, https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ. Source ID: `pettigrew-collectanea-house-gournay-1871`.
```

Add this bullet to G14 `### Sources consulted`:

```markdown
- `pettigrew-collectanea-house-gournay-1871` - T. J. Pettigrew, "On the House of Gournay," *Collectanea Archaeologica*, vol. 2 (1871), pp. 207-210. Public-domain digest of DG's Francis Gurnay of London, King's Lynn worsted-yarn, John Gurney of Norwich, and Keswick commercial-line material.
```

## Research source lists

Where each target file has a `Sources Consulted`, `Sources`, or source table, add the new source IDs used in that file:

```text
wansey-medieval-genealogy-1925
pettigrew-collectanea-house-gournay-1871
american-biography-cyclopedia-v26-gurney-1926
farrer-honors-knights-fees-v3-gurnay-extracts
```

Only add IDs actually cited in that specific file.

## Validation commands

After applying the patchset:

```powershell
node -e "JSON.parse(require('fs').readFileSync('data/sources.json','utf8')); console.log('sources ok')"
```

If generated site files are updated in phase 2, run:

```powershell
Push-Location site\website
npm.cmd run build
npm.cmd run validate
Pop-Location
```

## Source URLs

- https://www.wikitree.com/wiki/Wauncy-5
- https://www.nickdelves.co.uk/wansey/wansey/1925_08Wansey_Family_Tree_Medieval_Genealogy.pdf
- https://www.google.com/books/edition/Collectanea_Archaeologica/xjcGAAAAQAAJ
- https://www.google.com/books/edition/American_Biography/tnkKAQAAMAAJ
- https://babel.hathitrust.org/cgi/pt?id=mdp.39015032992151
- https://hdl.handle.net/2027/mdp.39015032992151
