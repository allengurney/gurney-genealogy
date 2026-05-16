# Intake status audit — 2026-05-16

Reviewer: Claude Code (Opus 4.7) per user request on branch `main`.

Scope of this audit:
1. Detect any **phase 2 patchset that was completely skipped** (phase 1 produced, but no phase 2 application ever ran). Per the user's framing, partially applied patchsets are treated as completed phase 2.
2. Identify content in `sources/intake/new/` (and adjacent staging) that was **never promoted into a patchset**.
3. Move patchsets with any phase-2 application into `sources/intake/done/` to improve tracking.

Method: walked each patchset, pulled a representative `sourceId`, file path, or string operation, and grepped for it in `data/sources.json`, `sources/corpus_supplement/`, `sources/validations/`, `data/places.json`, `research/`, and `fact-sheets/`. A single confirmed hit was treated as sufficient evidence of phase-2 application.

---

## Patchsets yet to be applied

### Confirmed-skipped phase 2

- **`sources/intake/processed/Ready/v05-patchset-highlight-updates.md`** — direct-line ancestor fact-sheet highlight refinements (G16–G37).
  - Spot-checked unique strings from the proposed `new_str` blocks across `fact-sheets/`:
    - `"Heir-apparent who never inherited — and died in the last weeks of Catholic England"` — absent.
    - `"Boy lord at nine, second cousin of a future queen"` — absent.
    - `"marriage that explains a great-great-grandson"` — absent.
    - `"Seven hundred sheep at West Barsham"` — absent.
  - None of the planned `str_replace` operations on `fact-sheets/g16…g37-*.md` have landed.
  - Action: this file is the **only patchset that has had phase 2 entirely skipped**. Left in `processed/Ready/` for future phase-2 application.

### Held intentionally (not moved)

- **`sources/intake/processed/on-hold/v01.patchset.md`** — Anderson 1742 Vol. I (Yvery/Perceval/Harpetre origins, Vol. II citation close-out).
  - Spot check shows the work is in fact applied:
    - `anderson-yvery-1742-vol-i` exists in `data/sources.json`.
    - `sources/corpus/anderson-yvery-1742-vol-i-extract.md` exists.
    - `sources/validations/anderson-yvery-1742-vol-i.md` exists.
    - `sources/media/anderson-yvery-1742-vol-i/genealogicalhist01ande.pdf` and `p4-printed-john-de-harpetre.png` exist.
  - The directory label says "on-hold," but the contents say "done." Flagging for the user — leaving in place pending a call on whether it should be moved to `done/` or remain on-hold by deliberate choice.

---

## `sources/intake/new/` content needing a new patchset

These items remain in `new/` and have **no corresponding `data/sources.json` entry, corpus extract, or research-file insertion**. They should be picked up in a new intake session (phase 1).

1. **`NewIntake_Batch1.md`** — partially processed. Two entries still need promotion:
   - **The Era / Clipper newspaper, 1895 — Lester S. Gurney Sr.** Source URL: `https://dn710909.ca.archive.org/0/items/clipper43-1895-08/clipper43-1895-08.pdf`. Linked file: `Screenshot 2026-04-20 204336.png`. No matching sourceId, validation, or research promotion found.
   - **BHO, *Topographical History of Norfolk*, vol. 5, pp. 33-39 — Berford's Manor / Cringleford / Edmund Gournay.** `Berford` / `Cringleford` appear in no repo file outside the intake markdown itself.
   - (Two further entries in this file are already processed: the British Archivist *Francis Gurney* biography → `british-archivist-bernau-1913`; the BHO vol. 8 *Gourney's Manor* page → covered by v06 and downstream research/places.)

2. **`Screenshot 2026-04-20 204336.png`** — the Lester S. Gurney Sr. screenshot referenced by Batch1 entry 1. Same status as item 1.1.

3. **`uc1--b751193-139-1776799225.txt`** — HathiTrust download of Ormerod, *Strigulensia: Archæological memoirs relating to the district adjacent to the confluence of the Severn and the Wye* (London, 1861). Contains substantial extracts on Thomas de Gournay (the Edward II regicide), Penyard, Beverston, Kings Weston, etc. No `ormerod-strigulensia` or comparable sourceId in `data/sources.json`; no research promotion found.

4. **`deep-research-report-Gournay-Ancestors-in-Decordes-Essai-1861.md`** — Decorde, *Essai sur le Canton de Gournay* (1861) deep-research synthesis covering Hugues III/IV/V Bellosanne, Jumièges, Gaillefontaine, Beaubec, etc. The underlying source IS registered (`decorde-essai-canton-gournay-1861`) and the raw `.txt` is in `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`, but no research file in `research/people/` or `research/places/` cites the sourceId, and the structured findings from this deep-research report (Bellosanne 1198 foundation, Saint-Aubin priory 1200, the 1082 Jumièges 190-arpent charter, the 1112/22 Bec confirmation, the 1164 Gaillefontaine endowment, the *chevaliers aux armes noires* note, etc.) have not been promoted. **A targeted research-promotion patchset against `g32`–`g35` companions and the relevant `research/places/` files is needed.**

### Already processed (kept in `new/` only because not yet archived)

For tracking purposes — these `new/` files have had their content promoted and need only routine archival:

- `Essai historique et archéologique sur le Canton de Gournay par lAbbe.txt` → registered as `decorde-essai-canton-gournay-1861`, body lives in `sources/corpus_supplement/essai-historique-archeologique-canton-de-gournay-decorde-1861.txt`. (Note: the *raw* source is processed; the *deep-research findings on top of it* are not — see item 4 above.)
- `deep-research-report-gurney-redivivus.md` → applied by v01 Edmund Gurney patchset; mirror at `sources/corpus_supplement/deep-research-report-gurney-redivivus.md`.
- `benjamin_gurney_harden_research_tables_updated.md` → applied by v07; mirror at `sources/corpus_supplement/benjamin-gurney-harden-research-tables-2026-04.md`.
- `john_harden_1751_will_evidence_package.md` → applied by v07; corpus + validation under `plymouth-probate-john-harden-1751-will`.
- `3QSQ-G97D-F6PW.jpg` and `3QS7-897D-FXDF.jpg` → Plymouth probate p. 383 / p. 384 images referenced inside the v07 sourceId notes.
- `NewIntake_Batch2.md` → entries covered by v01 (Edmund Gurnay 1619/1624/1631/1639 imprints, Thoms *Anecdotes and Traditions*), on-hold v01 (Anderson Vol. I), v06/v39 (BHO and *History of Parliament* John Gurney d.1408), and Hingham/Morley material in `research/places/hingham-norfolk.md`. No residual gap identified by this audit.

---

## Patchsets moved to `sources/intake/done/`

All of the following had at least one verifiable phase-2 artifact in the canonical repo layers and were moved out of `processed/` (and `processed/Ready/`) into `done/`.

From `sources/intake/processed/` (top level):

- v03, v04, v06-future-research-urls, v08, v08a, v09, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29 (probate-creditor-network), v29 (section8-cleanup), v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40 (37 files in total).

From `sources/intake/processed/Ready/`:

- v01 (Edmund Gurney divine), v02-1 (John Gurney Domesday Hardingham), v06-great-ellingham (Old Hall / G37 cleanup), v07 (Benjamin Gurney / Harden), v15a (Bates Braintree cleanup), v15b (colonial extracts promotion).

Remaining in `processed/`:

- `Ready/v05-patchset-highlight-updates.md` — phase 2 not yet run (see above).
- `on-hold/v01.patchset.md` — contents already applied, but the on-hold label was deliberate; not moved without user direction.
