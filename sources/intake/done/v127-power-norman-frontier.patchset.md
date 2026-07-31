# Intake Patchset v127 -- Daniel Power, *The Norman Frontier* (2004)

**Outcome:** promote
**Done:** 2026-07-31 08:10 PT

## Intake material reviewed

Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge University Press, 2004), source ID `power-norman-frontier-2004`.

All **42 supplied scans** have been visually reviewed, including the p. 504 genealogy diagram and the duplicate capture of p. 11. The copyright-restricted scans are held locally in `sources/media/power-norman-frontier-2004/_local/`; the source registry, validation, and page-labelled extract were updated directly at the requester's direction. The extract is `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`.

## Finding

Power is a modern scholarly synthesis of the **senior Gournay lordship**, not a source on Walter's Norfolk junior branch. It supplies useful, independently supportive research material for Gerard (G32), Hugh III (G33), the senior baron's place and frontier context, and the source-critical treatment of Eudes (G37). It also reinforces the existing evidence for Edith de Warenne's remarriage to Dreux de Mouchy and the senior line's Coucy connections.

The scanned material does **not** name Walter de Gournay, establish his parentage, connect him with Montigny-sur-Andelle, or apply the *Conquests* inheritance custom to the junior Norfolk line. It likewise supplies no new, person-specific evidence for G34 Hugh II, G35 Renaud, or G36 Hugh I. Those are deliberate non-promotions, not omissions.

Power's internal Hugh numbering is not the repository's generation numbering. Retain the source's wording or identify its senior-line context; do not silently equate an ordinal Hugh in Power with a repository generation label.

## Actions

### 1. Record the source boundary in Walter's companion and remove the completed pull

**File:** `research/people/g31-walter-de-gournay-fact-sheet.research.md`

**Operation:** `str_replace`

**old_string**

```md
[^setting-kent]: Edward Hasted, *History of Kent*, 2nd ed., vol. 4 (1798), pp. 544–545 (Addington held of the Montchensies "as of his manor of Swanscombe"); carta of Walter de Meduana, 1166 (Manasser's three Kent fees). Source IDs: `hasted-kent-vol4`, `redbook-exchequer-hall-v1`.

## Cast — the people in this file
```

**new_string**

```md
[^setting-kent]: Edward Hasted, *History of Kent*, 2nd ed., vol. 4 (1798), pp. 544–545 (Addington held of the Montchensies "as of his manor of Swanscombe"); carta of Walter de Meduana, 1166 (Manasser's three Kent fees). Source IDs: `hasted-kent-vol4`, `redbook-exchequer-hall-v1`.

## Power's senior-lordship boundary

Daniel Power's modern study supplies valuable context for the senior Gournay lordship—its three-castle geography, Beauvaisis holdings, and frontier character—but it does **not** name Walter, connect him to Montigny-sur-Andelle, or apply *parage* to the Norfolk junior branch. The p. 504 genealogy diagram is likewise selective and senior-line only. Power is therefore a useful boundary on what this source can support, not independent evidence for Walter's parentage.[^power-walter-scope]

[^power-walter-scope]: Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge: Cambridge University Press, 2004), pp. 27, 188–191, 355–359, 368–369, 469, 504–505. Extract: `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`. Source ID: `power-norman-frontier-2004`.

## Cast — the people in this file
```

**Operation:** `str_replace`

**old_string**

```md
6. **Reference works still to be read:** Keats-Rohan, *Domesday Descendants*, p. 492 in full (snippets captured July 2026); Loyd, *Origins of Some Anglo-Norman Families* (Gurnai entry — no online route; library); Evans, "Dammartin" (1965); Cooke, *Early History of Mapledurham* pp. 9–11, 85; Power, *Norman Frontier* pp. 355–357 (on interlibrary loan); Tanner p. 315.<!-- L-208 through L-214 -->
```

**new_string**

```md
6. **Reference works still to be read:** Keats-Rohan, *Domesday Descendants*, p. 492 in full (snippets captured July 2026); Loyd, *Origins of Some Anglo-Norman Families* (Gurnai entry — no online route; library); Evans, "Dammartin" (1965); Cooke, *Early History of Mapledurham* pp. 9–11, 85; Tanner p. 315.<!-- L-214 -->
```

### 2. Add a modern synthesis alongside Gerard's primary 1089 evidence

**File:** `research/people/g32-gerard-de-gournay-fact-sheet.research.md`

**Operation:** `str_replace`

**old_string**

```md
### 2.4 [1089] — Orderic on Écouché: Gerard as son of Basilea daughter of Gerard Flaitel
```

**new_string**

```md
Power independently places Gerard among the five leading north-eastern frontier magnates who submitted to William Rufus in 1089. He reads Gerard's choice as part both of the contest for the Andelle valley and of the wider struggle among frontier lords, Robert Curthose, Rufus, and Count William of Évreux. This modern synthesis reinforces, but does not replace, Orderic's primary account.[^power-gerard-1089]

[^power-gerard-1089]: Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge: Cambridge University Press, 2004), pp. 368–369. Extract: `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`. Source ID: `power-norman-frontier-2004`.

### 2.4 [1089] — Orderic on Écouché: Gerard as son of Basilea daughter of Gerard Flaitel
```

### 3. Add Power's qualified territorial support to Hugh III's Gerberoy section

**File:** `research/people/g33-hugh-de-gournay-iii-fact-sheet.research.md`

**Operation:** `str_replace`

**old_string**

```md
### 6.4 1067 + 1073 — earlier ducal charter witnesses
```

**new_string**

```md
Power adds a qualified territorial observation to this existing Gerberoy evidence. He says that, before the 1078–79 war in which Gournay and Hugh de Gournay suffered defeat near Gerberoy, the Gournay men appear to have seized Beauvaisis parishes later known as the *Conquêts Hue de Gournay*. Power expressly says the dates of both events are open to challenge. This supports the existing association of Hugh III with the Conquests, but is not proof of a precisely dated seizure.[^power-hugh-gerberoy-conquests]

[^power-hugh-gerberoy-conquests]: Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge: Cambridge University Press, 2004), p. 162. Extract: `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`. Source ID: `power-norman-frontier-2004`.

### 6.4 1067 + 1073 — earlier ducal charter witnesses
```

### 4. Tighten the Eudes/Rollo source critique with Power's early-Normandy analysis

**File:** `research/people/g37-eudes-de-gournay-fact-sheet.research.md`

**Operation:** `str_replace`

**old_string**

```md
**No contemporary document names Eudes as a recipient.** The Eudes / Gournay attribution rests on the *MS. Histoire de Gournay* and DG's transcription thereof.
```

**new_string**

```md
**No contemporary document names Eudes as a recipient.** The Eudes / Gournay attribution rests on the *MS. Histoire de Gournay* and historian Daniel Gurney's transcription of it. Researcher Daniel Power's source-critical overview independently reinforces this: he says Dudo's broad territorial claim for Rollo has been disproved, that Rollo's authority was initially concentrated around Rouen, and that no single established Norman frontier existed in either 911 or 933. The Eudes tradition therefore cannot be converted into a documented personal grant of Gournay by Rollo.[^power-rollo-territory]

[^power-rollo-territory]: Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge: Cambridge University Press, 2004), pp. 11–12. Extract: `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`. Source ID: `power-norman-frontier-2004`.
```

### 5. Add Power's customary-law confirmation to the Conquests place file

**File:** `research/places/beauvaisis-frontier-acquisitions.md`

**Operation:** `str_replace`

**old_string**

```md
## Geographic interpretation now adopted in the library
```

**new_string**

```md
### Power 2004 — modern synthesis and limits

Power identifies the *Conquêts Hue de Gournay* as twenty-four villages and hamlets north and east of Gournay. He explains that they generally followed Norman custom while retaining some Beauvaisis practices, confirming that this was a frontier customary-law territory rather than simply a remembered list of villages. He also cautions that both the association with an earlier Hugh and the dating of the relevant evidence are open to challenge. This strengthens the aggregate-place model while preserving its chronological caution.[^power-conquests-place]

[^power-conquests-place]: Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge: Cambridge University Press, 2004), pp. 162, 188–191. Extract: `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`. Source ID: `power-norman-frontier-2004`.

## Geographic interpretation now adopted in the library
```

### 6. Add modern support to the Gournay-en-Bray place file

**File:** `research/places/gournay-en-bray.md`

**Operation:** `str_replace`

**old_string**

```md
This remains partly traditional rather than documentary history, but it is still worth preserving because it is the form in which both the Victorian family historians understood the origin of the seat. The place file should continue to distinguish between:
```

**new_string**

```md
This remains partly traditional rather than documentary history, but it is still worth preserving because it is the form in which both the Victorian family historians understood the origin of the seat. Power's modern study gives the reason for keeping that distinction firm: early ducal authority was not territorially fixed, and Gournay's later frontier character cannot retrospectively prove a 911 personal grant. The place file should continue to distinguish between:[^power-gournay-place-boundary]
```

**Operation:** `str_replace`

**old_string**

```md
## Hugh I and the fortifications
```

**new_string**

```md
[^power-gournay-place-boundary]: Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge: Cambridge University Press, 2004), pp. 11–13, 53, 118, 469. Extract: `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`. Source ID: `power-norman-frontier-2004`.

## Hugh I and the fortifications
```

### 7. Add Power's senior-line synthesis to the collateral topic

**File:** `research/topics/senior-gournay-baron-line-collateral.md`

**Operation:** `str_replace`

**old_string**

```md
## Hugues IV de Gournay (c. 1098 – c. 1180)
```

**new_string**

```md
## Power 2004 — senior-line context

Power's modern synthesis reinforces the senior-line framing used here. He treats Gerard's widow's remarriage to Dreux de Mouchy and the subsequent Coucy marriage as part of a durable network linking north-eastern Normandy, Picardy, and northern Champagne; he also identifies a senior Hugh's style *Dei permissione dominus Gorniaci* and the exceptional power of the Gournay lords. These observations support the existing primary and charter evidence for the Edith–Dreux and Coucy connections, while retaining the source's own Hugh numbering rather than imposing the repository's generation labels on it.[^power-senior-line]

[^power-senior-line]: Daniel Power, *The Norman Frontier in the Twelfth and Early Thirteenth Centuries* (Cambridge: Cambridge University Press, 2004), pp. 219, 233. Extract: `sources/corpus_supplement/power-norman-frontier-gournay-selected-pages.md`. Source ID: `power-norman-frontier-2004`.

## Hugues IV de Gournay (c. 1098 – c. 1180)
```

### 8. Close the completed Walter/Power lead

Run:

```powershell
.\.venv\Scripts\python.exe tools\research_leads.py close L-208 --disposition "Power fully reviewed: valuable senior Gournay, place, and frontier synthesis; no Walter, Montigny, or junior-branch parage evidence. Findings promoted in source extract and research patchset v127."
```

No successor lead is warranted. The book's relevant scanned scope is now known, and its limits are recorded in Walter's companion.

## No fact-sheet change

No published fact-sheet change is proposed. This source strengthens research evidence and source criticism, but the relevant published claims already rest on primary evidence or carefully marked tradition. G34–G36 receive no forced citation because the reviewed pages add no specific claim for them.

## Validation after application

```powershell
.\.venv\Scripts\python.exe tools\research_leads.py get L-208
.\.venv\Scripts\python.exe tools\repo_search.py infile research\people\g32-gerard-de-gournay-fact-sheet.research.md --terms "Power" "Rufus"
.\.venv\Scripts\python.exe tools\repo_search.py infile research\people\g33-hugh-de-gournay-iii-fact-sheet.research.md --terms "Power" "Conqu"
.\.venv\Scripts\python.exe tools\repo_search.py infile research\people\g37-eudes-de-gournay-fact-sheet.research.md --terms "Power" "Rollo"
.\.venv\Scripts\python.exe tools\repo_search.py infile research\places\beauvaisis-frontier-acquisitions.md --terms "Power" "Conqu"
git diff --check
```
