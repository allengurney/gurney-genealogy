# Paleography bundle 01 — Norfolk Gurney leads (2026-06-13 batch)

Self-contained hand-off for an external paleography agent (or a fresh session after a
timeout). All three tasks are Norfolk Consistory/Archdeaconry manuscript material on
FamilySearch. Read order of priority: **A (primary) → B (cheap confirm) → C (optional)**.

## Working method (all tasks)

1. The committed `images/*.jpg` are 2-page spreads at moderate resolution — likely **too
   low for confident secretary-hand reading**. Re-pull full-resolution **single-page**
   images via the download recipe in
   `.claude/skills/familysearch-fulltext-research/SKILL.md` (presigned-S3 image API),
   using the ARK + image number + DGS given below. Requires an authenticated FamilySearch
   session (Allen's Chrome/Edge are logged in).
2. Work from the manuscript image, not the machine transcript — the FTS transcripts here
   are corrupt and must not be quoted as readings.
3. Deliver back into this folder as `paleography-bundle-01-RESULTS.md`: a working
   transcription (mark illegible spans `[…]`, doubtful readings `[word?]`), the specific
   answers requested, and any crops worth keeping.

---

## Task A (primary) — the "Anne Gurney my daughter" will, c. 1599–1601

- **Source:** Archdeaconry of Norwich, Court probate register, **vol. 28** (English).
- **Film / DGS:** `008077025`.
- **Images:** the will spans roughly **img 338 → 339 → 340**. The will *opens* on the
  right-hand page imaged at img 339 ("In the name of God Amen…"); the "Anne Gurney"
  bequest falls on img 340. Read 338 (tail of the prior will + a `Probatum` clause) for
  context, then 339–340 for this will in full.
- **ARKs:** img 340 = `3Q9M-CSND-LGXV`; the prior leaf = `3Q9M-CSND-LGF9`.
- **Local images:** `images/01-norfolk-wills-1599-1601-3Q9M-CSND-LGXV.jpg`,
  `images/01a-norfolk-wills-1599-1601-image-339-prior-3Q9M-CSND-LGF9.jpg`.
- **Record capture:** `records/01-norfolk-wills-1599-1601-3Q9M-CSND-LGXV.md`.

**What is already established (do not re-derive):**
- The testator is **not** a Gurney. The display-script name at the head of the will
  (img 339) reads as a **"Robert Gr—"** (Grewe / Grene / Greue — *resolve the surname*).
  He names a wife **Jane** and devises a tenement he dwells in.
- The will contains the phrase **"…Anne Gurney my Daughter…"**. Because the testator is
  not a Gurney, **Anne is a married-in Gurney** — i.e. the testator is the father-in-law
  of a Gurney man whose wife is Anne. (This means Allen's working guess "daughter of
  Henry G15" is unlikely — that would make Anne a Gurney by birth.)

**Questions to answer:**
1. **Testator's full name, status, parish, and the will/probate dates.** (The capture
   implies a July date and a 1599 probate clause — confirm.)
2. **The exact "Anne Gurney" clause, transcribed verbatim**, plus any words naming or
   hinting at **Anne's Gurney husband** (forename, occupation, residence) or her children.
3. **Any other Gurney name** anywhere in the will (witness, overseer, debtor, neighbour).
4. The other daughters named ("Elizabeth, Anne and Margaret"?) and the "sister Anne" —
   enough to fix the family so the Gurney marriage can be placed.

**Why it matters:** a securely-read Gurney marriage in the Archdeaconry of Norwich
c. 1600 could attach to the West Barsham / Norwich Gurney network around Henry G15's
generation. Identity is open — the value is in *which* Gurney Anne married.

---

## Task B (cheap confirm-and-reject) — Great Ellingham "Harney/Gurney", 1660–61

- **Source:** Norwich Consistory Court wills, **vol. 135**. **DGS** `008472225`, **img 175**,
  ARK `3Q9M-C39Z-T9PR-F`. Local: `images/23-…-3Q9M-C39Z-T9PR-F.jpg`;
  capture `records/23-…-3Q9M-C39Z-T9PR-F.md`.
- **My assessment: this is the Harvey/Harney family of Great Ellingham, not Gurney**
  — the page names Isacke / James / Abraham "Harney" alongside James / Mary / Sarah
  "Harvey." Allen flagged it "Gurney??".
- **Single question:** read the surname of **"Isacke ___ of Great Ellingham"** and his son
  **"James ___"**. Is it **Harney/Harvey** (→ confirm reject) or genuinely **Gurney**
  (→ escalate)? One careful reading settles it. Do **not** transcribe the whole will
  unless it turns out to be Gurney.

---

## Task C (optional, only with spare capacity) — Norwich deposition, 1608

- **Source:** Norwich Deposition Records 1608. **DGS** `004389252`, **img 104**,
  ARK `S3HY-696W-GL6`. Local: `images/17-…-S3HY-696W-GL6.jpg`;
  capture `records/17-…-S3HY-696W-GL6.md`.
- The FTS transcript shows a lone **"said Gurney"** in a deposition. Depositions can
  preserve neighbourhood, age, and litigation detail.
- **Question:** read the clause around "said Gurney" — is a Gurney a **deponent, party, or
  merely mentioned**, and is a forename / residence / age given? If it is only an
  incidental mention with no forename, stop and mark it low-value.

---

<!-- Bundle prepared 2026-06-13 from the second-pass triage (triage-of-triage-and-plan.md).
Items 1, 23, 17 of the browser-link batch. Item 20 (Spilman 1524) deliberately excluded —
already in repo (g17 spilman-1524) and is a typed abstract, not paleography. -->
