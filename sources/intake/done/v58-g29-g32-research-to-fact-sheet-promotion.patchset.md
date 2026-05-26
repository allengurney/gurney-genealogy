# Intake patchset v58 — G29–G32 research-to-fact-sheet promotion candidates

**Prepared:** 2026-05-24
**Applied:** 2026-05-24 (same session)
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation) — now applied directly per user direction.
**Status:** APPLIED. All six candidates landed on `main` and mirrored to `site/website/fact-sheets/`.
**Origin:** In-session review of G29–G32 research companions, not from `sources/intake/new/`. No raw intake to archive.

## Application notes
- **G32-A (Beauvais 8 May death day)** — landed; but in the same session the user supplied a new project research handoff (`sources/corpus_supplement/g32-gerard-de-gournay-drogo-edith-pilgrimage-death-window.md`) showing that the prior G32 Died vital phrasing "Before 1104" was backwards. The fact sheet now reads "8 May, after 1104 and before 1112 — probably 1104 or 1105," with footnote n2 expanded to cover the bracket apparatus and pilgrimage-duration analysis.
- **G32-B (Decorde Hugues IV Bec confirmation)** — landed; appended to existing footnote n6 as drafted.
- **G32-C (possible first wife)** — landed with the user's override: a brief reference is included in the Marriage(s) vital, and footnote n12 records the Foundation for Medieval Genealogy / Pattou preferred reading.
- **G31-A (Les Olim gloss)** — Highlight 2 now reads "the official records of the French royal court (Curia Regis / Parlement)."
- **G30-A** — no-op (already in main).
- **G29-A (Anderson 1742)** — landed as a new Highlight + new footnote n11.
- **Additional landed in same session, beyond v58:**
  - G32 page heading updated from "d. before 1104" to "d. 8 May, c. 1104–1105."
  - G32 schema.org `deathDate` updated.
  - G32 Marriage cell now also names Drogo (Dreux) de Mouchy as Edith's second husband and stepfather of Hugh.
  - New G32 Highlight: "Death, remarriage, and a king's wardship — all before 1112," summarising the Drogo / Henry I / Hugh sequence with a new footnote n13.
  - G32 narrative paragraph on death replaced with a fuller chronology including the bracket reasoning; a second new paragraph added covering Edith's return, Drogo's stewardship, and Henry I's raising of Hugh.
  - G32 Timeline entries extended (c. 1104 sets out; 8 May c. 1104–1105 dies; after 1104 Edith remarries Drogo; 1112 Hugh confirms Bec donations).
  - G32 research companion (`research/people/g32-gerard-de-gournay-fact-sheet.research.md`) gained four new sections (§10 Drogo I de Mouchy, §11 the death-date bracket, §12 the wardship sequence, §13 Drogo II Second Crusader, §14 source tensions). Existing §8 (Open questions) and §9 (Sources consulted) renumbered to §15 and §16, with the new sources added to the bibliography table.
- **Sources added to `data/sources.json`** (meta.version bumped 1.5.1 → 1.6.0): `gurney-drogo-pilgrimage-research-2026`, `dhi-crusaders-leeds`, `orderic-vitalis-chibnall-vol-5`, `orderic-vitalis-chibnall-vol-6`, `william-of-tyre-historia`, `suger-vie-louis-le-gros`, `saint-leu-esserent-cartulary-muller`, `hurlock-oldfield-crusading-pilgrimage-norman-2015`, `park-royal-holloway-thesis-2013`.

## Scope

Companion to v57 (G33–G37 promotion). Reviews G29 (Matthew de Gournay), G30 (William de Gournay I), G31 (Walter de Gournay), and G32 (Gerard de Gournay) research files for substantive findings that meet the fact-sheet promotion standard.

The G29–G32 research files are tighter and shorter than G33–G37 (mostly under 100 lines apiece, except G32 at 272). Most strong material is already in the published fact sheets. The candidate list is therefore shorter than v57.

Per the updated `.claude/rules/fact-sheets.md` "Finding-in-main, sources-in-footnote" rule, candidates here distinguish the **finding** (which belongs in body text) from the **source apparatus** (which belongs in footnotes).

Out of scope: writing-style corrections, repo-vocabulary cleanup, COLLATERAL removal, and acronym expansion across G29–G32 — all of those are precision edits already applied directly to `main` ahead of this patchset.

## Sources / data referenced

All candidates anchor to existing `data/sources.json` entries:

- `dg-rec-pt1`, `dg-rec-supp` — Daniel Gurney 1848 and Supplement 1858
- `potin-recherches-ville-gournay-1842`
- `decorde-essai-canton-gournay-1861` (already in canonical sources)
- `anderson-yvery-1742` — Anderson, *Genealogical History of the House of Yvery*, Vol. II (1742)
- `fmg-medlands-normacre` — Foundation for Medieval Genealogy MedLands (Cawley)

No new `sourceId` entries are required.

## How to read each candidate

Each candidate has:

- **Source in research:** which research-companion section the finding comes from.
- **Why promote:** the reader value, including whether it satisfies the "core finding in main" rule.
- **Proposed location:** where it would go on the fact sheet.
- **Proposed text (verbatim):** exact markup to insert if approved.
- **Approval gate:** explicit `[ ] APPROVED / [ ] REJECTED / [ ] DEFER` line for the user.

---

## G32 — Gerard de Gournay

### Candidate G32-A — The Beauvais obituary: a documented death day

**Source in research:** `g32-gerard-de-gournay-fact-sheet.research.md` §2.8.

**Why promote:** The current fact sheet says "Before 1104, Palestine" without a death day. The Beauvais church preserved an ancient obituary recording Gerard's death on **8 May** (VIII Idus Maii) — a specific calendar day that survived because Beauvais commemorated him on its anniversary list. The year remains uncertain (Daniel Gurney's 1845 argument that 1097 must belong to the eldest-son Gerard, since Orderic places the father at Nicaea after May 1097, is sound), but a documented death-day for an 11th-century Norman lord is a concrete reader-facing detail.

The core finding ("8 May, on a second pilgrimage to the Holy Land") belongs in main content; the obituary apparatus belongs in the footnote.

**Proposed location:** Replace existing Died cell text; add to Highlight 1; new footnote.

**Proposed Died cell text (replaces current):**

```html
    <div class="fact-value">8 May, before 1104, on a second pilgrimage to the <a href="https://en.wikipedia.org/wiki/Holy_Land">Holy Land</a> with his wife Edith — died <em>en route</em>. The day is preserved on the Beauvais church's anniversary list; the year is uncertain. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

**Proposed Highlight 1 enrichment** (append one sentence to the current Crusade highlight):

```
The Beauvais church preserved his death-day on its anniversary list — 8 May, year uncertain — one of the more remarkably specific calendar facts to survive from any 11th-century Norman lord's death abroad.
```

**Proposed footnote n2 update** (replace existing):

```html
<li id="n2">Daniel Gurney, <em>Record</em>, Part I (1848), p. 27: "Gerard de Gournay d. about the year 1104, in the Holy Land, and Editha, his widow, re-married Dreux de Monceaux." Death day preserved as "VIII Idus Maii ob. Girardus de Gornaco" (8 May) in an ancient obituary of the church of Beauvais, quoted in Pierre Potin de la Mairie, <em>Recherches historiques sur la ville de Gournay-en-Bray</em> (1842), p. 124, and reproduced in Daniel Gurney, <em>Record</em>, Part I (1848), p. 68 footnote. Daniel Gurney's 1845 reasoning (<em>Record</em>, Part I, p. 68): the 8 May day is right; the 1097 year attached to it in some traditions is wrong as applied to the father, since Orderic Vitalis places Gerard at the siege of Nicaea after May 1097. Source IDs: <code>dg-rec-pt1</code>, <code>potin-recherches-ville-gournay-1842</code>. <a class="citation-back" href="#ref-2">↩</a></li>
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G32-B — The Hugues IV Bec confirmation [c. 1112/22] — independent twelfth-century corroboration

**Source in research:** `g32-gerard-de-gournay-fact-sheet.research.md` §2.13 (Decorde 1861).

**Why promote:** Hugues IV (Gerard's eldest son) confirmed gifts to the Abbey of Bec made by "his ancestors Hugues and Basilie, and by Gérard, his father," explicitly including the church of Brémontier. This sits a full generation earlier than the [1181/89] Henry II royal confirmation and is independent of it. Together the two confirmations document the same donation chain (Hugh III → Basilie → Gerard → Hugues IV) in two distinct twelfth-century attestations.

This is supporting apparatus rather than a stand-alone finding — better as a footnote addition than as a new Highlight.

**Proposed location:** Append to existing footnote n6 (the Bec/Saint-Wandrille footnote on Gerard's seigneurial activity).

**Proposed text — append to existing footnote n6:**

```
A separate twelfth-century confirmation independently anchors the same donation chain: J.-E. Decorde, <em>Essai historique et archéologique sur le Canton de Gournay</em> (Paris: Derache and Didron; Rouen: Lebrument, 1861), preserves an early-twelfth-century document dated c. 1112 or 1122 in the local tradition, in which Hugues IV (Gerard's eldest son and successor in the senior barony) confirmed gifts to the Abbey of Bec made by "his ancestors Hugues and Basilie, and by Gérard, his father," explicitly including the church of Brémontier. Together with the [1181/89] Henry II royal confirmation, this places the Gournay–Bec patronage chain on two distinct twelfth-century witnesses, one familial and one royal. Source ID: <code>decorde-essai-canton-gournay-1861</code>.
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

### Candidate G32-C — Possible first wife (mother of Amicie Talbot)

**Source in research:** `g32-gerard-de-gournay-fact-sheet.research.md` §3.2.

**Why promote:** Foundation for Medieval Genealogy MedLands canvasses three options for Amicie de Gournay's parentage; the preferred reading (also Étienne Pattou's preferred reading) is that Gerard had an earlier unrecorded marriage that produced Amicie before his marriage to Edith de Warenne. This is a candidate identity that has scholarly support but is not currently visible on the fact sheet.

**Recommendation:** Keep in research only. The "possible first wife" framing is too tentative to publish on the fact sheet without overclaiming. The Amicie Talbot connection itself can stay in research.

**Approval gate:** `[X] APPROVED (add a brief footnote)  [ ] REJECTED (keep in research only — recommended default)  [ ] DEFER`

---

## G31 — Walter de Gournay

### Candidate G31-A — Three independent evidentiary chains for blood descent

**Source in research:** `g31-walter-de-gournay-fact-sheet.research.md` Working Notes (Les Olim section).

**Why promote:** The fact sheet's Highlight 2 already references "three independent evidentiary chains" — the *Liber Niger*, the parage tenure, and the *Les Olim* ruling. The research adds that *Les Olim* is the French royal court's records (the Curia Regis / Parlement registry), giving the term plain-English context for a reader who might not recognise it.

**Recommendation:** Already in main; minor enrichment only. Add a one-line gloss in Highlight 2 explaining what *Les Olim* is.

**Proposed text — replace Highlight 2:**

```html
  <li><strong>Confirmed as Gournay blood by a French royal court.</strong> The <em>Les Olim</em> — the official records of the French royal court (Curia Regis / Parlement) — formally recognized the Swathings Gurneys as legitimate blood descendants of the Lords of Gournay. Combined with the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a> entry and the <a href="https://en.wikipedia.org/wiki/Parage">parage</a> tenure of Montigny-sur-Andelle held by Walter's son, the junior branch's descent from Gerard is established through three independent evidentiary chains. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
```

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

## G30 — William de Gournay I

### Candidate G30-A — Provost of Paris namesake already in main

**Source in research:** `g30-william-de-gournay-i-fact-sheet.research.md` Working Notes.

**Why promote:** Already on the fact sheet's Narrative section. No new promotion needed.

**Recommendation:** No-op.

**Approval gate:** `[X] APPROVED (no-op)  [ ] REJECTED  [ ] DEFER`

---

## G29 — Matthew de Gournay

### Candidate G29-A — Anderson 1742 *House of Yvery* as independent corroboration

**Source in research:** `g29-matthew-de-gournay-fact-sheet.research.md` Conflicting Information table.

**Why promote:** The G29 research file documents an interesting cross-tradition corroboration: James Anderson's *Genealogical History of the House of Yvery* (1742), p. 478 — published a full 106 years before Daniel Gurney's *Record* — names a Norfolk Gournay pedigree Matthew → William → John in the same order as Daniel Gurney's G29 → G28 → G27. Anderson's "Time of Henry the First" dating is too early (most likely a slip for Henry III, given that Anderson's preceding narrative was on early-13th-century events), but the name sequence is identical. This is genuine independent corroboration of the junior-Norfolk pedigree's name chain, predating Daniel Gurney's work by over a century.

The finding (an earlier antiquarian source corroborating the same name sequence) is substantive enough to be visible on the fact sheet, not buried in research.

**Proposed location:** New short Highlight bullet between the existing "Charitable acts" and "Living 1217" highlights.

**Proposed text (new highlight):**

```html
  <li><strong>Corroborated by a different antiquarian tradition — and a century before Daniel Gurney.</strong> James Anderson's <em>Genealogical History of the House of Yvery</em> (1742) — published 106 years before Daniel Gurney's <em>Record</em> — names the same Norfolk Gournay sequence Matthew → William → John in the same order. Anderson's dating slips (he places this group "in the Time of Henry the First," likely a copy-error for Henry III), but the independent name sequence corroborates the pedigree from a source Daniel Gurney did not himself rely on. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></li>
```

**Proposed text — new footnote n11 (append to citation list):**

```html
<li id="n11">James Anderson, <em>Genealogical History of the House of Yvery</em>, vol. II (London: Edward Symon, 1742), p. 478, names the Norfolk Gournays in the sequence Matthew → William → John, with the John identified as "of Hingham." Anderson's date placement ("the Time of Henry the First") is too early — John (G27) is documented at the battle of Lewes 1264 and the Crusade of 1270 — and is most plausibly a slip for Henry III, since Anderson's preceding narrative concerned events of the early thirteenth century. Anderson explicitly hedges on the link to the senior Norman line ("doubtless of the same Stock"). The same name sequence appearing 106 years before Daniel Gurney's <em>Record</em>, in an independent antiquarian compilation, is a useful corroboration that the junior-Norfolk Matthew–William–John sequence pre-dates Daniel Gurney's pedigree work. Source ID: <code>anderson-yvery-1742</code>. <a class="citation-back" href="#ref-11">↩</a></li>
```

(Existing footnote anchors `ref-11` through `n11` are not currently used on this fact sheet; the next free numeric is `n11`.)

**Approval gate:** `[X] APPROVED  [ ] REJECTED  [ ] DEFER`

---

## Summary table

| Candidate | Ancestor | Type | Recommended |
|---|---|---|---|
| G32-A | Gerard | Vitals Died revision + Highlight enrichment + footnote (Beauvais obituary 8 May death day) | **Promote** |
| G32-B | Gerard | Footnote append (Decorde 1861 Hugues IV Bec confirmation as twelfth-century corroboration) | **Promote** |
| G32-C | Gerard | (No body text — possible first wife / Amicie Talbot mother) | Keep in research |
| G31-A | Walter | Highlight 2 gloss expansion (one-line definition of *Les Olim*) | **Promote** |
| G30-A | William I | (No change — already in main) | No-op |
| G29-A | Matthew | New Highlight + new footnote n11 (Anderson 1742 corroboration) | **Promote** |

## Phase 2 application notes

When approved candidates are applied:

1. Apply each candidate exactly as the proposed text above shows, preserving footnote numbering offsets where new footnotes are added.
2. Mirror every fact-sheet edit to `site/website/fact-sheets/`.
3. No `data/ancestors v26.json` changes are required by any candidate.
4. No `data/sources.json` additions are required; every source cited already has a canonical entry.
5. After application, verify footnote anchors and that no `.html` links or canonical tags are broken.
