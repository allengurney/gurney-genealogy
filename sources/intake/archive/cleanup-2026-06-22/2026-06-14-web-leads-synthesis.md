# 2026-06-14 web-leads discovery — honest retrospective + salvage

## What this run got wrong
Most of it was duplicative. The headline "find" (L-118, Walter Rye, *The Gurneys of Norwich*) was **already held in full** — `sourceId rye-norfolk-antiquarian`, OCR extract at `sources/corpus/norfolk-antiquarian-gurneys-of-norwich.md`, already cited in the G14 Francis companion, `francis-gurney-of-maldon.md`, and the John Gurney case file. Everything the run "discovered" from Rye (the two-Francis distinction, the 1614 L'Estrange agency, Dorothy Gurney's 1641 sister-set, Sion/John-of-Earsham 1639) is in that extract — and the repo's OCR is *better* (it correctly reads **Earsham**, which the re-OCR garbled to "Barsham"). **L-118 closed as duplicative** (moved to `research-leads-done.csv`). **L-71 (Burke / Maldon)** is low-value: Maldon is a collateral / Rye-disputed branch, deprioritised to 30.

Root cause: no pre-pull check of existing holdings. Fixed going forward by the new pre-pull sanity check in `research/future-research/README.md`.

## What is genuinely net-new (salvage)

### L-82 — Gascon Rolls (C61) Gournay calendar — KEEP
The Gascon (C61) theatre is overwhelmingly the **Somerset** Gournays (Thomas the regicide line; **Sir Matthew de Gournay**, seneschal of the Landes, d.1406, and household). The one clear **Norfolk** signal: **John Gournay, 1394 (C61/104:50.10)** names **John Dru, parson of Harpley** (Norfolk), as his English attorney before going to Aquitaine — a Norfolk-line man on the 1394 expedition. **Edmund Gurney, 1365–70** acted as attorney-in-England (once co-attorney with the parson of Ingoldisthorpe, Norfolk) — ambiguous Norfolk lean. Useful for the soldier-database topic (L-76) and the Somerset/Norfolk de-confliction. Full calendar in `L-82-gascon-rolls-gournay.md`. This was an open lead; calendaring it is real progress.

### L-46 — Blomefield, Harpley — KEEP (corroboration)
Matthew de Gournay acquired Harpley via **Rose de Burnham** (gift of **Hameline Plantagenet, Earl Warenne**), c.30 Hen II; descent to **Anthony Gurnay 1511 → Sir John Allen c.1535**; rector-gravestone *"John de Gournay quondam rector et patronus"* (d.6 Edw III); church-window arms *"Gournay, argent, a cross ingrailed gules"* (cf. L-10); **Edmund Gurnay B.D. presented 1620** = the Divine. Detail in `L-46-blomefield-harpley.md`. (Cross-check against the G29 Matthew companion before promoting — some of this may already be held; Blomefield's Harpley descent likely overlaps existing content.)

## Note before any promotion
Even the two "keep" items must be checked against existing repo holdings (G29 Matthew companion, soldier-database topic, somerset-gournay-collateral) before a patchset — the same check that should have run first this turn.
