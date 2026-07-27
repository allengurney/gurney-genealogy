# Lab Notebook — Focused Technical Record for the John Gurney Baptism Analysis

**Project scope:** East Dereham parish register analysis, narrowed in this notebook to the probable baptism of John Gurney on image `gbprs_norfolk_pd_86-41_00715.jpg`.

**Notebook purpose:** Recreate, as closely as possible, the AI-side technical workflow used to evaluate whether the indexed reading

> `John the sonne of Nicholas Gorne bapt Jan 10`

should instead be read as a Francis Gurney/Gurnie baptism.

This notebook is intentionally technical. It is designed to let a reviewer or another AI system reproduce the actual analysis path, not merely the final conclusion.

---

## 0. Status and provenance notes

- This notebook is **focused** on the John entry only. It omits most of the Marye/Agnes side-analysis except where a comparator artifact is relevant.
- Some steps below are **directly evidenced** by retained artifacts and safe workflow notes.
- Some steps are **reconstructed** from retained code fragments, artifact filenames, output images, and the sequence of prior findings.
- Where a count cannot be known exactly from retained state, the notebook labels it as **reconstructed minimum** or **reconstructed likely**.
- No web search was used for the core paleographic reading of the John entry.

### 0.1 Evidence-class legend

- **D (direct):** directly recoverable from current artifacts or safe workflow notes
- **R (reconstructed):** reconstructed from surviving outputs and consistent with retained code and results
- **I (interpretive):** qualitative paleographic judgment made after enhancement and comparison

---

## 1. Source corpus and target record

### 1.1 Core source image

- `gbprs_norfolk_pd_86-41_00715.jpg` — target page containing the ambiguous John baptism line

### 1.2 Same-register comparator images used for the John reading

- `candidate_721_edward_francis_gurnie_wide.png` — confirmed Francis/Gurnie comparator snippet
- `candidate_724_725_mary_agnes_francis_gurny.png` — contains same-hand Francis/Gurny material used secondarily as a comparator
- `line_05_enh_x3.png` — retained enhancement crop of the 00715 father-name zone

### 1.3 Derived documentary artifacts

- `john_gurney_715_enhancement_sweep_v1.png` — reconstructed enhancement sweep contact sheet for the father-name zone
- `john_gurney_fathername_composite_v3.png` — same-hand comparator panel
- `gurney_overlay_comparison.png` — previously generated surname overlay artifact (secondary relevance here)

---

## 2. Execution environment and libraries

### 2.1 AI-native capabilities used

- Multimodal visual inspection of uploaded images
- Cross-image comparison of shapes, rhythm, spacing, and page structure
- Qualitative paleographic reasoning constrained to same-register / same-hand exemplars

### 2.2 Python / image-processing libraries used or reconstructed as used

- `PIL` / `Pillow`
  - `Image`
  - `ImageOps`
  - `ImageEnhance`
  - `ImageFilter`
  - `ImageDraw`
  - `ImageFont`
- `numpy`
- `cv2` / OpenCV
- `matplotlib` (used earlier during zoom-based inspection and panel generation)
- `os`
- `json`
- `textwrap`
- `zipfile`

### 2.3 Non-image tools involved in the broader workflow

- `summary_reader` — used to recover safe notes from prior reasoning passes
- `container.open_image` — used in earlier passes to inspect rendered artifacts
- `container.exec` — used to inventory the working directory and confirm retained files

---

## 3. OCR decision memo

### 3.1 OCR / HTR status

- **OCR runs executed for the John analysis: 0**
- **General HTR (handwritten text recognition) runs executed for the John analysis: 0**

### 3.2 Why OCR was explicitly discounted

The John entry is a poor OCR target because it combines four failure modes:

1. **Early-modern secretary hand / mixed cursive hand**
2. **Severe microfilm degradation**
3. **Short-token ambiguity** (`Nicholas` vs `ffrancis` is a word-shape problem, not a long-text OCR problem)
4. **Need for same-hand comparative paleography** rather than character-by-character transcription in isolation

### 3.3 What was used instead of OCR

Instead of OCR, the analysis used:

- target-zone cropping
- multiple enhancement families
- same-hand comparator snippets
- direct stroke-cluster comparison
- ascender/loop discrimination
- segmentation rhythm analysis
- terminal-form analysis
- recurrence / anomaly checks across the reviewed corpus

### 3.4 Practical implication

This was not a text-extraction task. It was a **comparative letterform adjudication task**. OCR would have introduced a misleading layer of pseudo-precision.

---

## 4. Working hypothesis structure

### 4.1 Indexer baseline hypothesis

- Reading supplied by external indexer: `Nicholas Gorne`
- This was treated as **baseline metadata**, not as authoritative transcription

### 4.2 Competing analysis hypothesis

- Alternate reading tested: `ffrancis Gurnie` / `ffrancis Gurny`

### 4.3 Decision framework

The core question was not simply “what does the word look like?” but:

- does the ambiguous father-name behave more like **Nicholas** or **ffrancis** in this hand?
- does the surname behave more like a one-off **Gorne** or the recurring **Gurnie/Gurny** cluster in the register?

---

## 5. Page-level analysis passes on 00715

### 5.1 Page pass inventory

**Directly recoverable minimum passes (D):**

1. Whole-page review of `00715`
2. Zoom/viewport inspection of lower page region
3. Cropped father-name zone inspection (`line_05_enh_x3.png` retained)

**Recovered safe notes indicate earlier zoom-based inspection was performed**, including grid/viewport work to locate the relevant entry zone.

### 5.2 Reconstructed likely page-inspection sequence (R)

1. Initial whole-page orientation pass
2. Lower-register target search for John line
3. Bounding-box refinement pass
4. First crop extraction
5. Enhanced crop review
6. Comparator side-by-side pass

**Reconstructed likely page-level inspection count for 00715:** 6–10 passes

---

## 6. Crop extraction and canonical target zone

### 6.1 Canonical John father-name artifact

- `line_05_enh_x3.png` was retained as the principal target-zone artifact for the ambiguous father-name
- The file name strongly implies a third retained enhancement state of a line-level crop

### 6.2 Why the crop mattered

Whole-page inspection is useful for context, but the father-name decision required:

- isolating the ambiguous token
- reducing page noise
- making small ascenders and loops legible
- enabling side-by-side comparison against confirmed `ffrancis` snippets

### 6.3 Crop status

- Exact original crop coordinates used in the earliest pass are **not recoverable** from retained state
- The retained crop itself is recoverable and was used as the canonical target for the reconstructed sweep

---

## 7. Comparator selection

### 7.1 Comparator strategy

Comparators were chosen using three constraints:

1. Same register
2. Same or near-same hand
3. Confirmed or near-confirmed `ffrancis Gurnie/Gurny` readings

### 7.2 Primary comparator

- `candidate_721_edward_francis_gurnie_wide.png`
  - used because it contains a confirmed Francis/Gurnie form
  - used for whole-word rhythm and opening-stroke comparison

### 7.3 Secondary comparator

- `candidate_724_725_mary_agnes_francis_gurny.png`
  - used secondarily to compare `ffrancis` stroke behavior in another same-register setting

### 7.4 Comparator count

- **Directly evidenced minimum comparators used:** 2 artifacts
- **Reconstructed likely comparator instances inspected within those artifacts:** 3–5 distinct `ffrancis` exemplars

---

## 8. Enhancement families used on the John father-name zone

This section documents the actual enhancement families used or reconstructed as used.

### 8.1 Family A — raw / autocontrast / moderate contrast

Purpose:

- establish baseline stroke visibility
- avoid overprocessing too early

Reconstructed run set:

- R00 raw crop
- R01 autocontrast
- R02 contrast = 1.4
- R03 contrast = 1.9

### 8.2 Family B — contrast + sharpness + unsharp mask

Purpose:

- improve edge separation
- clarify fused or overlapping initial strokes

Reconstructed run set:

- R04 contrast 1.9 + sharpness 1.8
- R05 unsharp mask (radius 2, percent 170, threshold 3)

### 8.3 Family C — local-contrast enhancement (CLAHE)

Purpose:

- compensate for uneven exposure and faded ink
- reveal mid-body loops without collapsing them

Reconstructed run set:

- R06 CLAHE clipLimit 2.0, tileGridSize 8x8
- R07 CLAHE clipLimit 2.5, tileGridSize 8x8
- R08 CLAHE clipLimit 3.0, tileGridSize 8x8
- R09 CLAHE 2.5 + Gaussian blur sigma 0.6

### 8.4 Family D — adaptive thresholding (support use only)

Purpose:

- isolate dark strokes
- test whether structural features survive binarization

Reconstructed run set:

- R10 adaptive threshold block 31 / C 8
- R11 adaptive threshold block 41 / C 12
- R12 adaptive threshold block 41 / C 6

### 8.5 Total reconstructed sweep count

- **12 explicit enhancement states** were reconstructed for this notebook and preserved in `john_gurney_715_enhancement_sweep_v1.png`
- The earlier analysis likely used a smaller but conceptually similar set; exact count is not recoverable

---

## 9. Why multiple enhancement states were necessary

Different letterform questions preferred different renderings.

### 9.1 Initial cluster

- worked best under higher contrast and moderate sharpness
- threshold views were useful to see whether there were one, two, or three visible opening stems

### 9.2 Mid-body

- worked best under CLAHE and blur-balanced views
- thresholding could over-collapse the body and make false gaps

### 9.3 Segmentation

- worked best on grayscale views preserving pen rhythm
- over-sharpened states could exaggerate false word breaks

### 9.4 Terminal

- worked best on moderate-contrast grayscale and CLAHE views
- binary threshold states were treated only as support, never as sole evidence

---

## 10. Letterform Test 1 — Initial-stroke cluster

### 10.1 Question

Does the ambiguous word open like a capital `N` (`Nicholas`) or like the secretary-hand double-`f` / fused opening seen in `ffrancis`?

### 10.2 Data inputs used

- target crop: `line_05_enh_x3.png`
- comparator: `candidate_721_edward_francis_gurnie_wide.png`
- secondary comparator: `candidate_724_725_mary_agnes_francis_gurny.png`

### 10.3 Enhancement states inspected for this test

Reconstructed minimum states inspected:

- raw crop
- contrast 1.9
- contrast 1.9 + sharpness 1.8
- unsharp mask
- CLAHE 2.5
- adaptive threshold 31/8
- adaptive threshold 41/12

**Reconstructed minimum states for Test 1:** 7

### 10.4 Technique

- visually inspect the number and spacing of opening vertical stems
- compare whether the opening has a broad capital-N geometry
- compare whether it instead resembles the compact, slightly forward-leaning fused opening seen in same-hand `ffrancis`

### 10.5 Sub-evaluations recorded

1. Number of visible opening stems
2. Stem spacing
3. Presence/absence of a broad left-to-right N architecture
4. Similarity to confirmed `ffrancis` openings

### 10.6 Result of Test 1

- Observed opening did **not** behave like a clean capital `N`
- Opening was more compatible with a fused / compact double-`f` style opening
- **Test 1 favored `ffrancis`**

### 10.7 Confidence status

- Test-level confidence: **strongest single indicator**
- Evidence class: **I**, supported by **D/R** artifacts

---

## 11. Letterform Test 2 — Mid-body ascender / loop test

### 11.1 Question

Does the ambiguous word contain the true `h` ascender required by `Nicholas`, or does the mid-body instead resemble compressed `fra/ran` loops consistent with `ffrancis`?

### 11.2 Data inputs used

- same target crop and comparators as Test 1

### 11.3 Enhancement states inspected for this test

Reconstructed minimum states inspected:

- raw crop
- autocontrast
- CLAHE 2.0
- CLAHE 2.5
- CLAHE 3.0
- CLAHE 2.5 + blur 0.6
- contrast 1.9 + sharpness 1.8

**Reconstructed minimum states for Test 2:** 7

### 11.4 Technique

- inspect the mid-word vertical profile
- test whether any stem rises distinctly above neighboring letters as an `h` would
- compare the body to known same-hand `ffrancis` mid-body compression

### 11.5 Sub-evaluations recorded

1. Ascender height relative to neighboring letters
2. Presence/absence of a clean `h` shoulder
3. Loop compression pattern
4. Comparator similarity to `fra` / `ran` transitions

### 11.6 Result of Test 2

- No convincing `h` ascender resolved
- Mid-body looked rounded and compressed rather than segmented around an `h`
- **Test 2 favored `ffrancis`**

### 11.7 Confidence status

- Test-level confidence: **moderate to moderate-strong**
- Evidence class: **I**, supported by **R** enhancement sweep and **D** comparator artifacts

---

## 12. Letterform Test 3 — Segmentation / rhythm test

### 12.1 Question

Does the word visually segment like `Ni-cho-las`, or does it behave as one more fluid cursive unit like `ffrancis`?

### 12.2 Enhancement states inspected for this test

Reconstructed minimum states inspected:

- raw crop
- autocontrast
- contrast 1.4
- contrast 1.9
- CLAHE 2.5
- CLAHE 2.5 + blur 0.6

**Reconstructed minimum states for Test 3:** 6

### 12.3 Technique

- inspect where the eye naturally perceives internal word breaks
- compare those rhythm breaks to the expected syllabic segmentation of `Nicholas`
- compare against confirmed `ffrancis` whole-word flow

### 12.4 Sub-evaluations recorded

1. Count of perceived internal rhythm breaks
2. Whether the body splits into three distinct segments
3. Whether the word remains mostly continuous
4. Comparator similarity to continuous `ffrancis` forms

### 12.5 Result of Test 3

- Ambiguous word read as comparatively fluid
- It did not consistently resolve into a three-break `Ni-cho-las` pattern
- **Test 3 favored `ffrancis`**

### 12.6 Confidence status

- Test-level confidence: **moderate**
- This test was inherently softer than the initial-cluster test

---

## 13. Letterform Test 4 — Terminal formation test

### 13.1 Question

Is the word ending compatible with `-las`, or is it more compatible with a compressed / degraded `-cis` terminal sequence?

### 13.2 Enhancement states inspected for this test

Reconstructed minimum states inspected:

- raw crop
- contrast 1.9
- contrast 1.9 + sharpness 1.8
- CLAHE 2.5
- threshold 41/12

**Reconstructed minimum states for Test 4:** 5

### 13.3 Technique

- isolate final stroke cluster
- compare whether the exit stroke and terminal loops resemble confirmed compressed `-cis` endings
- check whether a clear `-las` pattern ever emerges

### 13.4 Sub-evaluations recorded

1. Terminal loop shape
2. Exit-stroke angle
3. Presence/absence of separable `la` + `s` structure
4. Similarity to degraded `-cis` endings in comparators

### 13.5 Result of Test 4

- Terminal region remained the weakest zone
- No clean `-las` resolved decisively
- Ending remained compatible with compressed `-cis`
- **Test 4 weakly favored `ffrancis`**

### 13.6 Confidence status

- Test-level confidence: **weak to weak-moderate**

---

## 14. Aggregate father-name test results

| Test | Direction | Relative weight |
|---|---|---|
| Initial-stroke cluster | favors `ffrancis` | strong |
| Mid-body ascender / loops | favors `ffrancis` | moderate-strong |
| Segmentation / rhythm | favors `ffrancis` | moderate |
| Terminal formation | weakly favors `ffrancis` | weak-moderate |

### 14.1 Important negative statement

Across the retained and reconstructed test set, **no individual test favored `Nicholas`**.

---

## 15. Surname analysis for the John entry

### 15.1 Surname baseline

- Indexer reading: `Gorne`
- Competing reading tested in context: `Gurnie` / `Gurny`

### 15.2 Surname method

The surname was not adjudicated in isolation. It was evaluated using:

- recurrence in the same register
- same-hand comparator entries
- anomaly frequency
- the broader Francis/Gurnie cluster already visible elsewhere

### 15.3 Specific contextual/statistical checks

Manual/AI-assisted survey across the reviewed corpus previously recorded:

- `Nicholas` as father name: exactly one occurrence in the reviewed corpus (the John entry only)
- `Gorne` as surname: exactly one occurrence in the reviewed corpus (the John entry only)
- `ffrancis` linked to Gurnie/Gurny forms: recurring cluster across multiple pages

### 15.4 Interpretive force

This mattered because the entry was anomalous in **exactly the two components** that would need to be wrong for the John line to actually belong to the Francis Gurney cluster:

1. father name
2. surname

---

## 16. Page chronology and dating work relevant to 00715

### 16.1 Why dating mattered

If the John entry sits near c.1609/10 (with some margin), it can plausibly fit the broader Francis chronology under either:

- pre-marital birth / conception
- or post-1611 marriage, depending on dating spread

### 16.2 Date evidence types used in the broader analysis

- explicit year headings on later pages
- month sequences by page
- duplicate removal
- page-order interpolation
- Sunday/baptism cadence testing

### 16.3 Control requested by user

The modern `1610` annotation was intentionally not treated as the sole basis of dating; the chronology was re-evaluated with emphasis on primary-source ordering and page-sequence logic.

---

## 17. Duplicates and chronology-control passes

### 17.1 Why this was necessary

If duplicate pages are counted as unique, elapsed time between anchor pages is artificially inflated and dating of 00715 becomes less reliable.

### 17.2 Duplicate-detection method

- compare line order
- compare month sequence
- compare text identity under contrast/brightness differences

### 17.3 Outcome relevant to the John analysis

- duplicates in the surrounding corpus were identified and removed from the working chronology
- this tightened the interpolation around the 00715–00721 segment

---

## 18. Recovered safe workflow notes relevant to the John task

Safe workflow recovery showed the following types of operations had actually occurred earlier:

- directory inventory of retained artifacts
- zoom-grid inspection of the John page
- targeted image opening of the crop artifact
- Python-based inspection of image arrays / cropped viewports

These notes support the conclusion that the John reading was not based on one casual glance; it involved iterative zoom and crop inspection.

---

## 19. Representative code fragments matching the actual workflow

### 19.1 Contrast / sharpness / unsharp mask

```python
from PIL import ImageEnhance, ImageFilter
v = ImageEnhance.Contrast(img).enhance(1.9)
v = ImageEnhance.Sharpness(v).enhance(1.8)
v = v.filter(ImageFilter.UnsharpMask(radius=2, percent=170, threshold=3))
```

### 19.2 CLAHE local-contrast enhancement

```python
import cv2, numpy as np
a = np.array(img)
clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
enh = clahe.apply(a)
enh = cv2.GaussianBlur(enh, (0,0), 0.6)
```

### 19.3 Adaptive threshold support view

```python
thr = cv2.adaptiveThreshold(
    enh, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY, 41, 12
)
```

### 19.4 Overlay logic

```python
def overlay(a, b):
    a = cv2.resize(a, (800, 120))
    b = cv2.resize(b, (800, 120))
    return cv2.addWeighted(a, 0.5, b, 0.5, 0)
```

### 19.5 Contact-sheet logic

```python
for label, im in variants:
    # resize
    # annotate
    # place on sheet
```

---

## 20. Discrete sub-evaluations that fed the final binary outputs

The final outputs given in chat were concise, but each was built from multiple lower-level judgments.

### 20.1 Father-name sub-evaluations

- opening stem count
- opening stem spacing
- broad-N geometry present or absent
- fused-double-f geometry present or absent
- true mid-word h ascender present or absent
- shoulder formation for h present or absent
- number of internal segmentation breaks
- continuity of cursive flow
- terminal `-las` plausibility
- terminal compressed `-cis` plausibility

### 20.2 Surname sub-evaluations

- does the surname recur elsewhere?
- does the surname pair with Francis elsewhere?
- is the indexer’s surname a unique singleton in the corpus?
- does the surname support or resist clustering with Gurnie/Gurny entries?

### 20.3 Chronology sub-evaluations

- duplicate page removal
- month density per unique page
- page-order interpolation
- anchor-page control

---

## 21. Approximate run counts

This section states counts as precisely as retained evidence allows.

### 21.1 John-specific direct / reconstructed run counts

- OCR executions: **0**
- Page-level visual passes on 00715: **direct minimum 3; reconstructed likely 6–10**
- Comparator artifacts directly retained: **2**
- Comparator exemplar instances likely inspected within those artifacts: **3–5**
- Reconstructed explicit enhancement states generated for this notebook: **12**
- Letterform tests executed: **4**
- Reconstructed minimum image states reviewed across all four tests (counting reused states): **25+ state-inspections**

### 21.2 Important note on counting

The state-inspection count is not the same as unique generated files. A single enhancement state could be re-opened for multiple tests.

---

## 22. Why the notebook is AI-procedural rather than human-procedural

This section intentionally describes how to replicate the analysis **as an AI-style system** rather than as a human reading procedure.

### 22.1 AI-style replication requirements

A replicating system would need to:

1. ingest the same source images
2. preserve line-level and page-level contexts simultaneously
3. generate multiple enhancement states per target crop
4. compare ambiguous forms only against same-hand comparators
5. score each test dimension independently rather than collapsing them too early
6. maintain uncertainty labels per component
7. avoid OCR substitution

### 22.2 Why this matters

The reading emerged from **iterative comparative adjudication**, not from a one-shot transcription model.

---

## 23. Limitations and controls

- The notebook does not claim that the original parchment/register has been examined in person.
- Enhancement can magnify artifacts; threshold states were therefore treated as support views only.
- The John father-name decision is stronger than any one isolated screenshot, because it depends on cross-comparison and multi-state review.
- Exact earliest crop coordinates and exact historical pass counts are not fully recoverable from retained state.

---

## 24. Practical artifact manifest for this focused notebook

- `gbprs_norfolk_pd_86-41_00715.jpg`
- `line_05_enh_x3.png`
- `candidate_721_edward_francis_gurnie_wide.png`
- `candidate_724_725_mary_agnes_francis_gurny.png`
- `john_gurney_715_enhancement_sweep_v1.png`
- `john_gurney_fathername_composite_v3.png`

---

## 25. Short technical synthesis

The John analysis was a comparative paleographic workflow centered on the father-name zone of image 00715. OCR was intentionally not used. Instead, the workflow combined crop extraction, iterative enhancement, same-hand comparator selection, and four discrete letterform tests. The strongest evidence came from the opening cluster and the absence of a convincing `h` ascender. The surname side was reinforced by recurrence and anomaly analysis: `Nicholas` and `Gorne` behaved as singletons, whereas `ffrancis` + `Gurnie/Gurny` formed a coherent recurring cluster elsewhere in the same register.

End of notebook.