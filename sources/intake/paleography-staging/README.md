# Paleography staging — open brief

This folder stages manuscript-image briefs for outsourced transcription. 

> **Source terms:** all images are FamilySearch-sourced (17th-c. manuscript, public-domain content under FamilySearch viewing terms). Masters live in `sources/media/<set>/_local/` (off GitHub) or, for in-progress packets, in `images/`.

## Packet 20 — NCC will 1631/32 naming "Clement Gurney Gent" — the full will (extends Packet 16a) — **OPEN**

Packet 16a captured only the **continuation page** (image 365, ark YRB3) bearing the "Clement Gurney Gent" bond, and so could not name the testator. This packet adds the two preceding pages — the will's **opening** (image 363) and **soul-bequest/early-bequest page** (image 364) — which carry the testator's name, parish, and the family structure. The will runs continuously across images **363 → 364 → 365**. From the NCC registered-copy will register **"Norwich. Wills 1632, 1631"** (vol. 124–125, 1631–32), FamilySearch DGS **008076514**. OCR is secretary-hand salad — snippets are locators only, and the testator's name in particular reads as salad and **must** be recovered from the image.

What is already established from the machine transcript and the packet-16a image read (to confirm/correct against the images):
- The testator is a **yeoman**, of a parish **in the County of Norfolk, Diocese of Norwich**; the will is dated in **7 Charles I (1631/32)**.
- Wife **Grissell / Crissell** (Grizell).
- A legatee **Clement** ("Clement my sonne"), plus **John Powles** and **Thomas Rowles**, with bequests conditioned on completing **apprenticeship** ("at the end of their apprentishood").
- The testator holds a **bond of £40 (penal sum), dated 21 November 1622, in which "Clement Gurney, Gent" is bound to him** (confirmed by the packet-16a image read), and bequeaths that bond to "Clement my sonne."

### 20a — will opening (testator name + parish) — the headline
- **Image:** `images/packet20-clement-will/img363-YTWS-will-opening.jpg` · ark **3:1:3Q9M-CSN8-YTWS** · image **363** of DGS 008076514
- **Finding-aid snippet (salad, foot of the right-hand page):** "…In the name of God Amen, [Twentieth] dai[e of] … in the yeare of the [reign of our] … Lord Charles by the [grace] of God of England[,] [Sc]otland and Ireland King Defender of the [Faith] … the **Seaventh** [= 7 Chas I], Anno d[omini 1631/32] … I [NAME] … of [PARISH] in the County of [Norfolk] **yeoman** … and in the Diocese of No[rwich] … of good and [perfect] memorie…"
- **Questions:** (1) **The testator's full name and parish** — the single most important answer; the OCR loses both exactly where the name sits. (2) The exact day/month and regnal/AD dating. (3) Any occupation/abode beyond "yeoman."

### 20b — soul bequest + early bequests (wife Grissell; Clement; the apprentices) — page 2
- **Image:** `images/packet20-clement-will/img364-YT9K-soul-bequest.jpg` · ark **3:1:3Q9M-CSN8-YT9K** · image **364**
- **Finding-aid snippet (salad):** "…and my Body [to] the Earth … in hope … of a joyfull [Re]surrection … I give and bequeath unto **Clement** and **John Powles** … to eyther of them the sum of fiftie [pounds] … to be [paid] … at the end of their apprentishood … [or] … after the decease of **Crissell my welbeloved wife** … Item I give and bequeath unto **Thomas Rowles** … fiftie pounds…"
- **Questions:** (1) Transcribe the bequests and the **relationship of each legatee** — are Clement, John Powles, and Thomas Rowles **sons**, **servants/apprentices**, or a mix? (2) Confirm the wife **Grissell/Crissell** and any surname for her. (3) Any other names on the page.

### 20c — the "Clement Gurney Gent" bond (continuation) — page 3 (= Packet 16a image)
- **Image:** `images/packet20-clement-will/img365-YRB3-clement-bond.jpg` · ark **3:1:3Q9M-CSN8-YRB3** · image **365** *(same page as Packet 16a)*
- **Finding-aid snippet (salad):** "…wherein **[Cl]ement Gurne[y] Gent [is] bounden** unto me for the [same] … Item I give and bequeath unto **[Cl]ement my [sonne]** [the] … obligatorie bearing date the **one and twenty day of November Anno Dm 1622** conteyning the penall sume of **forty pounds**…"
- **Questions — the genealogical crux:** (1) **Is "Clement my sonne" the same person as "Clement Gurney, Gent"?** — i.e. is the **testator himself a Gurney** (forgiving/assigning his son Clement Gurney the bond), or are these **two different Clements** (the testator's son Clement [other surname], and an unrelated gentleman debtor Clement Gurney)? Resolving this decides whether the will is a **Gurney testator's** will. (2) Any **residence or further style** for Clement Gurney, Gent (rare Gurney forename — high tracing value for the West Barsham / Great Ellingham Gurneys). (3) The probate clause (date/court) if it falls on this page.

**Return format:** a `packet-20-clement-gurney-will.md` report transcribing the will across the three pages, answering 20a (testator name/parish) and the 20c crux (one Clement or two) explicitly.

(Follow-ups surfaced by the completed reads live with their subjects — as open questions on the relevant `research/people/*.md` file or as leads in `research/future-research/research-leads.csv` — not as a second list here.)

---

## Process notes (read before staging or incorporating a batch)

Two distinct roles run through this folder. Keep them separate.

**Outsourcer (this repo / the maintainer) — staging a brief and incorporating the result:**
- **Give the subcontractor every image the question needs.** When the question is "who is the testator," the brief must include the will's **opening** page, not only the continuation that carries the name of interest — packets 16a/16b could not name their testators because only continuation pages were staged (the fix became Packet 20). Rather than costly over-analysis to determine exact pages, it is acceptable to include pages before or after the target (no more than 10 buffer images total). When available, provide the machine transcription text for location purposes-only. The outsourcer should include questions that the transcription may answer and may include context, terminology, or names that may help in the paleographic work.
- **Masters belong in `sources/media/<set>/_local/`, never long-term in this folder's `images/`.** `images/` is a transient handoff staging area; FamilySearch masters must not sit committed here. On incorporation, move every relied-on master into the right `sources/media/<set>/_local/` folder (gitignored) and document it in that folder's committed `README.md`.
- **When incorporating into research after analysis, each promoted finding needs the full chain:** a citation in the research/corpus file → a `sourceId` in `data/sources.json` (the `familysearch-fulltext-search` catch-all is fine for FTS image reads; mint a dedicated sourceId only for a discrete named document, e.g. a specific will) → a corpus extract in `sources/corpus_supplement/` for any rich primary text → the relied-on images in `sources/media/<set>/_local/`. **The packet report in `done/` is transient — preserve full transcriptions in `corpus_supplement`, not only in the report.**
- **Record negatives and false positives as findings** (e.g. packet 16c = Robert Webber, not a Gurney; packet 14f "Cropley" = formulaic Latin), and route open follow-ups to the subject file or a lead — do not accumulate a parallel to-do list in this README.
- When the subcontractor self-locates a missing image (packet 21b admon, packet 23 1758 recital), **verify the located page actually matches the intended record** (parish, name, date) before trusting it.

**Subcontracted paleography (the outsourced AI reader) — its job and its limits:**
- It transcribes the provided images, attempts to find any images the brief left out, and returns a `packet-NN-*.md` report with best-effort transcription, confidence notes, and explicit negatives. Its report is a finding aid for the outsourcer to verify and incorporate — not itself a citable source layer.
- **Dense Latin manorial/secretary court hand routinely defeats it** (Cawston death presentments, the East Dereham 1662/65 page). Treat "blocked / unresolved" as an expected outcome for those and either flag for a specialist or accept the negative; do not re-stage the same hard page expecting a different result.
- **Watch the Syon↔Lyon trap** (the looped opening long-S): the Earsham family forename is **Syon/Sion**, repeatedly misreadable as Lyon (recognition note already logged).
- Treat machine/OCR snippets as locators only; the surname/forename at the exact point of interest is usually where the OCR fails, so it must come from the image.
