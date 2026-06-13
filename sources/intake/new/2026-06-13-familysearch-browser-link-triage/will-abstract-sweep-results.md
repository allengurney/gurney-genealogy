# Will-abstract film sweep — results (2026-06-13)

Systematic Gurney-variant sweep of the **complete six-reel typescript will-extracts
series**, run against Allen's authenticated FamilySearch session. This is the broad-sweep
action recommended in `triage-of-triage-and-plan.md`, extended from the original two films
to the whole series after the catalog lookup revealed there were six. **Verdict: the sweep
paid off handsomely** — the standout new find is a **second top-gentry Gurney marriage
(Calthorpe, 1494)** to set beside the Lestrange one (1505); together they document the
late-medieval West Barsham Gurneys marrying into the same Norfolk gentry circle
(Calthorpe, Lestrange, Heydon, Townshend, Lovell, Spelman) the repo already tracks.

## The source — full series map

**"Norfolk wills extracts, 1370–1763"** (FamilySearch catalog `koha:1056823`): a typescript
abstract collection from the **Bradfer-Lawrence collection**, GSU microfilm of NRO
originals, on **6 reels filed alphabetically by testator surname**. Each entry abstracts one
will and cites its source register. Because the films are surname-ordered but FTS finds
"Gurney" *anywhere* in an abstract, a Gurney mention can surface under any testator — so the
whole series had to be swept, not just the "G" reel.

| Reel | Testator surnames | DGS | FTS coverage | Gurney hits |
|---|---|---|---|---|
| 1 | Aldrych → Bedingfeld | 008100792 | **NOT FTS-indexed** (a `wife` probe also returns 0) | unsearched — gap |
| 2 | Bedingfeld → Davy | 008480297 | yes | 4 (incl. **Calthorpe 1494**) |
| 3 | Davy → Hyrne | 008176838 | yes | 5 |
| 4 | Hyrne → Monndeforde | 008480296 | yes | 1 |
| 5 | Monndeforde → Smythe | 008085264 | yes | 5 |
| 6 | Smythe → Youngs | 008480295 | yes | 5 (incl. **Lestrange 1505**, **Smith 1643**) |

Reel 1 is the one coverage gap: not FTS-indexed, so any Gurney mention in an A–B testator's
will (Aldrych…Bedingfeld) is unsearched. Everything else is complete at `count=100`.

Query: `Gurn* Gourn* Gorn*` scoped by `q.groupName` to each DGS. The films are FTS-typed
abstracts (legible — no paleography needed). Citation form: "Norfolk wills extracts,
1370–1763 (Bradfer-Lawrence collection, typescript), FamilySearch film &lt;DGS&gt;, image
&lt;N&gt;, ark &lt;ARK&gt;, abstracting [register reference]." Source ID:
`familysearch-fulltext-search`.

## Film 008480295 — 5 hits (medieval–1640s)

| Ark (3:1:…) | Img | Reading | Disposition |
|---|---|---|---|
| **3Q9M-C39V-KLZH** | 251 | **Sir Roger Lestrange, Knt. — PCC Adeane fol. 2; buried Hunstanton Chancel; sisters "Heydon, Mrs. Townsend, Ann, Margaret, Gurnay"; proved 7 Oct 1505.** | **NEW — HIGH. Promote.** |
| **3Q9M-C39V-K2LV** | 41 | **William Smith of Gt. Massingham, Esq. — Norwich Cons. 1644-5 fol. 215; will 19 June 1643, proved 19 Aug 1645; names "Edm: Gurnay / Ellen Gournay" (bracketed as a pair).** | **NEW — MOD-HIGH. Promote.** |
| 3Q9M-C39V-KLWR | — | "Cecily Gurns, servant"; Benjamin Thompson; Mary Fowes; 1640. | New — LOW (a servant; no kinship). Note only. |
| 3Q9M-C39V-K2VN | 149 | Henry Spilman of St James Ellingham; "Antony Gurney and John Turrell, executors"; 1524. | **Duplicate** — already `spilman-1524` (L-101) on the G17 companion. |
| 3Q9M-C39V-KLFM | 806 | John Wymondham the elder, Esq., 1475; associates incl. "William Gurney," Henry Spelman, Southwell, Bokenham, Townshend. | **Duplicate** — already `wymondham-1475` on the G17 companion. (Note: explicitly names *William* Gurney among the gentry circle — worth folding into the existing footnote if not already there.) |

### Confirmed transcripts (read against full-res images)

**Lestrange 1505** — `images/sweep-lestrange-1505-pcc-adeane-KLZH-img251.jpg` (page 247):
> P.C.C. Adeane: 2.
> ROGER LESTRANGE Knt.
> to be buried in Hunstanton Chancel
> sister Heydon / Mrs. Townsend / sister Ann / sister Margaret / **sister Gurnay**
> (D: — — — ; 1505. (P: 7 Oct; 1505.

**Smith 1643** — `images/sweep-smith-massingham-1643-gurnay-K2LV-img41.jpg` (page 36):
> Norwich: 1644-5; 215.
> WILLIAM SMITH of Gt. Massingham Esqr.
> wife Martha executrix. / Mary Drew wife of Robert Drew
> ( Thomas son of Thomas Smith, Gentleman, my brother. / ( His sister Barbary Smith.
> **Edm: Gurnay ) / Ellen. Gournay )**  (D: 19 June; 1643. (P: 19 Aug; 1645.

## Film 008085264 — 5 hits (1605–1727; skews later)

| Ark (3:1:…) | Img | Reading | Disposition |
|---|---|---|---|
| 3Q9M-CSNP-DWRR | 846 | Henry Scarburgh the elder of North Walsham, 1605 (proved Jan 1605/6); among many grandchildren an ambiguous Harvye/Gurney legatee cluster ("Marye wife of Theophilus Harvye … John and Marye Gurney"). | New — LOW. North Walsham family, unconnected to the direct line; OCR-jumbled. Note only. |
| 3Q9M-CSNP-DWJT | — | Catharine Gurney, youngest dr of cousin Ann Bremden; widow Bridget (Tench); 1727/28. | New — LOW (18th-c. collateral). |
| 3Q9M-CSNP-DW2Q | — | a Gurney; brother-in-law Mr. William Tench; Benjamin Barwick; 1711/15. | New — LOW (18th-c.; same Tench/Gurney cluster as above). |
| 3Q9M-CSNP-D4Y4 | — | "sister Katherine Gurney"; friend William Balye of Honingham Esq., executor; 1711. | New — LOW (18th-c. collateral). |
| 3Q9M-CSNP-D7MW | — | Charles Preston of Barton Turf, Clerk; "Richd **Gurnel**"; 1714/15. | **False positive** — Gurnell, not Gurney. Reject. |

The three 1711–1727 Gurney mentions are post-emigration collateral (the direct English
line left c. 1630s) and below the threshold for promotion; logged here for completeness so
the sweep is not silently truncated.

## Film 008480297 (reel 2 — Bedingfeld→Davy) — 4 hits

| Ark (3:1:…) | Img | Reading | Disposition |
|---|---|---|---|
| **3Q9M-C39V-FS5W-X** + **3Q9M-C39V-FSPJ-W** | 489, 490 | **Sir William Calthorpe, Knt — one will in two probate copies (NCC reg. Wolman 1488-96 fol. 213, img 489; PCC reg. Vox fol. 23, img 490); dated 31 May 1494, proved 23 May 1495; buried White Friars, Norwich; names "Son Gurney … and my dr [daughter] his wife" as executor** alongside Calthorpe sons Francis/William/Edward and sons-in-law Drury and Haselden. | **NEW — HIGH. Promote.** A Calthorpe-Gurney marriage. |
| 3Q9M-C39V-FS5R-9 | — | "nephew **Gourney** Crowe, brother of a Christopher now beyond the sea"; Crowe of East Bilney Esq.; 1683/84. | New — MODERATE (onomastic). "Gourney" as a forename in the Crowe family of E. Bilney signals an earlier Gurney-Crowe marriage. |
| 3Q9M-C39V-FSP5-W | — | "kinswoman Mrs **Bridget Gournay**"; Mrs Mary Pierce of Wicklingham; 1682. | New — LOW (late collateral). |

**Confirmed transcript — Sir William Calthorpe 1494** (PCC copy, `images/sweep-calthorpe-1494-pcc-vox23-FSPJ-img490.jpg`; NCC copy, `images/sweep-calthorpe-1494-ncc-wolman213-FS5W-img489.jpg`):
> P.C.C. Vox 23. Sir William Calthorp, Knt — to be buried in the Church of the Whyte Friers in Norwich. Wife Dame Elizabeth. Cousin Philip. Sons, Francis, William, Edward; **Gurney and my dr [daughter] his wife**. Francis Hasilden and my dr his wife under 21. Robert Glore Esq. Walter Aslache Gent. Servant John Hasilden Esq. Dame Sibell Lowes. Master Richard Regill. (d: 31 May 1494. (P: 23 May 1495.

The abstract gives the son-in-law's surname only ("Gurney") — **no forename**. Pinning *which* Gurney married Sir William Calthorpe's daughter (c.1470s–80s) needs the full will (PCC PROB 11/10, reg. Vox; or the NCC reg. Wolman) or Calthorpe-pedigree work.

## Film 008176838 (reel 3 — Davy→Hyrne) — 5 hits

| Ark (3:1:…) | Reading | Disposition |
|---|---|---|
| 3Q9M-CS2G-J3YW-X | "sister **Joan Gurney** and her children under 21"; brother-in-law William Crispe; 1606. | New — MODERATE. A testator's sister married a Gurney; in-window. |
| 3Q9M-CS2G-J353-5 | "brother **John Gurneys of Kenton** [Suffolk] and Willm Donkin of Mendlesham, executors"; c.1514–17. | New — MODERATE. An early-16th-c. John Gurney of Kenton, Suffolk (likely collateral). |
| 3Q9M-CS2G-J3TW-5 | Martha Kett of Lynn, widow; "Edmund son of **Edmund Gurney of Norwich**, my son in law"; D: 11 Dec 1761. | New — LOW (18th-c. collateral). |
| 3Q9M-CS2G-J3TB-5 | "cosen **Katherin Gurnall**, widow" (Symon Cressy of London); 1637/1650. | LOW — likely **Gurnell**, not Gurney. |
| 3Q9M-CS2G-J3B7-Y | "**Catharine Gurnall** of Lynn, widow" (Robert Calthrop of Lynn, woollendraper); 1648/49. | **False positive** — Gurnell of Lynn (a distinct family; cf. `research/places/kings-lynn.md`). |

## Film 008480296 (reel 4 — Hyrne→Monndeforde) — 1 hit

| Ark (3:1:…) | Reading | Disposition |
|---|---|---|
| 3Q9M-C39V-F99H-W | testator's sisters incl. "**Elizabeth Gournay**"; John Jordan; Robt Bastard; D. 17 Oct 1654. | New — MODERATE-LOW. A 1654 Gournay marriage/sister; identity open. |

## What to promote (recommended — needs a Phase-1 patchset + placement decision)

1. **Calthorpe 1494 "Son Gurney"** → a documented **Calthorpe ⇄ Gurnay marriage** (a daughter of Sir William Calthorpe of Burnham Thorpe married a Gurney before 1494; the Gurney son-in-law was a will executor). Pairs with the Lestrange find below to establish that the late-medieval West Barsham Gurneys married into the first rank of Norfolk gentry. Open question: the Gurney's forename (abstract gives surname only) — sits in the G18/G19 window. Destination candidates: the relevant G18/G19 companion + `research/places/west-barsham.md`; cross-link the Calthorpe family. Underlying will *Available online* — PCC PROB 11/10 (reg. Vox fol. 23) via TNA Discovery, and the NCC reg. Wolman copy.
2. **Lestrange 1505 "sister Gurnay"** → a documented late-15th-c. **Lestrange-of-Hunstanton ⇄ Gurnay marriage**. The repo already leans heavily on the Gurney–Lestrange Hunstanton tie (Daniel Gurney's *Archaeologia* vol. 25 household accounts; L-29) but records the *employment/accounts* relationship, **not a blood marriage**. Open question for the patchset: *which* Gurnay did the Lestrange sister marry (this sits in the G17–G19 window — Anthony G17's forebears)? Destination candidates: the relevant G18/G19 companion and/or `research/places/west-barsham.md`; cross-link Hunstanton. The underlying will is **PCC register Adeane (proved 1505) = TNA PROB 11/14** — *Available online* (TNA Discovery image, and the abstract here).
3. **Smith of Gt. Massingham 1643 — "Edm: Gurnay / Ellen Gournay"** → most likely **Edmund Gurney the Divine** (rector of Harpley, ~5 mi from Gt Massingham; d.1648) and, paired with him, an **"Ellen"** — a candidate for the Divine's hitherto-unrecorded **wife's name** (his *mother* Ellen Blennerhasset was long dead by 1643). Destination: `research/people/edmund-gurney-divine.research.md` as a new documentary appearance + a wife-name lead (flag the identification as probable, not proven — could be a different Edmund). Underlying will: Norwich Consistory Court, register 1644-5 fol. 215 — *Available online* (FTS abstract; NCC register likely FTS-covered for an image read if wanted).

**Secondary (moderate) promotions worth a line each in the relevant file:** the 1606
"sister Joan Gurney," the c.1514–17 "John Gurney(s) of Kenton" (Suffolk collateral), the
1654 "Elizabeth Gournay," and the 1683 "Gourney Crowe" of East Bilney (onomastic evidence
of a Gurney-Crowe marriage). The Gurnell hits (Lynn, 1637–1761) and the 1605 Scarburgh are
notes-only; the 18th-c. Catharine/Katherine/Edmund Gurneys are post-emigration collateral.

None is promoted yet — they introduce new sourced claims with placement/identity calls that
belong in a reviewed patchset, not a silent companion edit.

## Method note / coverage caveat

The full six-reel Bradfer-Lawrence series was swept with `Gurn*/Gourn*/Gorn*` at
`count=100`; five reels are FTS-indexed and returned complete result sets (1–5 cards each),
**reel 1 (008100792, Aldrych→Bedingfeld) is not FTS-indexed** and is the one unsearched
segment. Not run anywhere: `Garn*` (swamped by *Garner* per the FTS skill) and exact-phrase
probes like `"de Gournay"`; the indexed reels are small enough to re-sweep with those in
minutes if a fuller pass is wanted. Reel 1's gap could be closed only by walking the film
images directly (no FTS) — low priority given A–B testators are unlikely to over-represent
Gurney mentions.

<!-- Sweep executed 2026-06-13 via Claude-in-Chrome against Allen's authenticated FamilySearch
session, per .claude/skills/familysearch-fulltext-research/SKILL.md (URL-scoped FTS, shadow-DOM
walker, das/v2 image pull). Full-res abstract images for the two promotable finds saved under
images/sweep-*.jpg. Signed S3 URLs discarded (expire ~1h). -->
