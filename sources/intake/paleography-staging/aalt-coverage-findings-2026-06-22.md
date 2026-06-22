# AALT coverage findings — soldier membranes (Packets 26–29) and Norfolk feet-of-fines (Packets 33-to-be)

AALT (`aalt.law.uh.edu`) is **back online** (HTTP only — `http://`, not `https://`; WebFetch forces HTTPS and fails, so use curl). Navigating its actual holdings resolved the standing "retry AALT once it's reachable" question for the medieval packets. The answer for the soldier rolls is a **coverage gap, not a connectivity problem**.

## Soldier muster membranes (Packets 26–29) — NOT on AALT
AALT's class **E 101** (KR Accounts Various) is only **partially digitised**: the E101 index (`E101.html`) lists exactly four piece-ranges — **nos. 79–83, 249–255, 349–355, 458–504**. The structure is `AALT7/E101/E101no<piece>/E101no<piece>no<membrane>`. The soldier-packet pieces fall **outside every digitised range**:
- Packet 26 — Richard Gurney esq., 1387 Arundel naval: **E101/40/34 m1** and **E101/41/5 m5** — pieces 40, 41 **absent** (direct folder probe `…/E101_40_34/` → 404).
- Packet 27 — John Gournay, Harfleur 1417/18: **E101/48/17**, **E101/48/19** — piece 48 **absent**.
- Packet 29 — John Gurnay archer, 1385 Percy: **E101/40/39 m2** — piece 40 **absent**.

**Disposition:** these muster rolls are **image-only at TNA Kew (not online via AALT)**. The medievalsoldier.org index row remains the finding aid; the membrane read (neighbours + locative bynames) needs a TNA Kew visit/order or a different digitisation. Tag: **Not online (AALT does not hold pieces 40/41/48 of E101).** Packet 28 (John Gurnay 1422, BnF Fr. 25766) is unaffected by this — it was always a BnF/Gallica target, not AALT.

## Norfolk feet of fines (fines packets) — ON AALT, but a 350-image membrane hunt with no entry→membrane index
AALT **does** hold Norfolk **CP 25/1** feet of fines (`CP25(1)b.html` → `AALT6/CP25_1/Norf/…`). Norfolk pieces digitised: **168** (file 182-183, 117 images) and **169** (file 184 = 76 images; file 185 = 81; files 186-189 = 200) — ~357 membrane images for piece 169 alone. Images are wrapped in `IMG_NNNN.htm` viewer pages (extract the JPG from each htm).
- The **Henry IV Norfolk** fines (Robert Gurnay's 1405 fine = Rye Pt II #64; and the unread-regnal-year fines #200 Thomas Armiger+Margaret, #329 Germye/Tharston, #432 Gereneye/Saxthorpe, #489 John rector Harpley) sit in **CP 25/1/169** (the late-14th–early-15th-c. Norfolk bundle), files 184–189.
- **The obstacle:** Rye's calendar entry numbers (#64, #200…) are his **sequential calendar numbers, not membrane numbers** — AALT has no name index, so there is no mechanical jump from a Rye entry to its membrane. Locating one fine = reading membranes (each is one final concord) until the parties match, across up to ~357 images. This exceeds the 100-image staging cap and is not a clean targeted pull.
- **To make it tractable:** narrow by **regnal year** first. The CP 25/1/169 files are filed broadly chronologically; cross-reference TNA Discovery's per-file date ranges for CP 25/1/169/184…189 to bound the search to the file(s) covering the target regnal year (Robert = 6–7 Henry IV = 1405), then membrane-scan only that file (~76–81 images). The Thomas-Armiger #200 regnal year is unread, so it cannot yet be bounded — read Rye's reign header for #200 before attempting.

**Disposition:** fines are **Available online (AALT)** but require a regnal-year-bounded membrane scan, not a one-shot pull. Path + method documented here so the eventual pull is set up; not staged into `images/` this round (would blow the image cap on an un-indexed hunt).
