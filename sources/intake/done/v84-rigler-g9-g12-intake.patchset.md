**Done:** 2026-06-04 12:57 PT

# v84 patchset — Rigler (1994) page scans: G9–G12 American-line intake (+ Rigler c. 1980 worksheets, Richard-2–Amos)

Prepared: 2026-06-04
Phase: 1 (preparation)

Scope: Promote the direct-line entries (Richard-2 through Benjamin-5) from Jean Gurney Rigler's *The Gurney Family from Aaron to Zuinglius* (rev. ed., 1994) into the G9–G12 research companions and fact sheets, and into a corpus-supplement transcription. The source already exists in `data/sources.json` (`rigler-gurney-family-aaron-zuinglius-1994`); this batch converts it from a future-pull bibliographic entry into a worked, page-cited source. Fact-sheet, research, validation, and `data/sources.json` edits are written here as literal operations for Phase 2. A folded addendum (operations A12–A19) adds an earlier Rigler source — five c. 1980 family-group worksheets (Richard-2 through Amos, G12–G8) — minting sourceId `rigler-genealogy-notes-c1980`, transcribing the sheets and their citation boxes, and capturing the worksheet-only deltas and corroborations onto the G9–G12 and G8 companions; the 1994 edition governs where they differ.

## Intake summary

Eight page scans of the 1994 revised-and-expanded edition (the author's signed gift copy) were supplied. Rigler is a compiled genealogy drawn largely from primary records — Weymouth, Abington, Middleborough, Rochester, and Kingston vital records; Suffolk and Plymouth probate and deeds; NEHGR; and named local historians (Cyrus Nash, Aaron Hobart) and family-paper collections (Anna Gurney papers). Her in-line citations are preserved in the transcription. The user's posture: the book was compiled almost exclusively from primary materials and should be treated as reliable fact.

The four in-scope entries map exactly onto the direct line:

- **RICHARD GURNEY-2** → G12 (`g12-richard-gurney-fact-sheet`)
- **BENJAMIN GURNEY-3** → G11 (`g11-benjamin-gurney-fact-sheet`)
- **BENJAMIN GURNEY-4** → G10 (`g10-benjamin-gurney-fact-sheet`)
- **BENJAMIN GURNEY-5** → G9 (`g09-benjamin-gurney-fact-sheet`)

Highest-value findings:

1. **Richard's death-year conflict is resolved.** Rigler states plainly that the *History of Weymouth* 1719 death date "was in error… which in fact, belonged to his son, Richard." Richard-2 died October 1691, intestate. This closes open question #6 on the G12 companion.
2. **The Mendon-massacre death is reattributed off Richard's son.** Rigler shows Richard's son John (b. c. 1654, m. Elizabeth Green) alive in 1691 and refusing administration of his father's estate. The 1675 Mendon victim John and the 1676 King-Philip's-War casualty Peter were sons of the emigrant John Gurney-1 (G13) — Richard's *brothers* — consistent with the G13 companion's own note (lead L-17) about "the conflated Mendon-1675 John attributed elsewhere to Richard G12." The current G12 fact sheet's "his son John was killed at the Mendon massacre" is corrected.
3. **Rebecca Taylor's parentage** is fixed: daughter of John and Rebecca Taylor of Weymouth; John Taylor's will (Suffolk Prob. 6:13, proved 22 May 1688) names "his daughter Rebecca, wife of Richard Gurney." (The *History of Weymouth* "Phebe Taylor" reading for the mother conflicts with the will's "Rebecca"; preserved as a conflict on the companion.)
4. **Rebecca Staples's parentage and the kinship-network land transfer** are confirmed: Rebecca Staples (b. 1682) was daughter of John-2 and Sarah (Atkins) Staples; the Samuel Staples of Scituate who sold G11 the Williams farm in 1726 was her brother — confirming the companion's kinship-transfer hypothesis.
5. **The "Granny Gurney's Swamp" story** has a named printed source at last: Cyrus Nash, quoted by Rigler, with the full anecdote text.
6. **Rigler independently confirms G10 as father of G9** by Jane (Jean) Harden — a second compiled-genealogy witness alongside *The Neverending Hobby*, drawn from the Anna Gurney papers and Abington records. Jane was daughter of Capt. John and Mary (Littlefield) Harden; she later married Ebenezer Spear (29 Dec. 1731). Sarah Morse, G10's wife, was daughter of Jonathan and Anna (Barden) Morse Jr.
7. **The aunt-upbringing tradition for G9 is corroborated with specifics:** "He was raised in Abington by Nathan-4 & Sarah (Harden) Gurney, his mother's sister." This is the same Sarah Harden Gurney the G9 companion already named as the strongest candidate — now stated directly by Rigler.
8. **The two-Benjamin problem is resolved cleanly:** G9 Benjamin (by Jane Harden; m. Elizabeth "Betsey" Harden, dau. of Samuel Harden) is distinct from the later Benjamin (by Sarah Morse, b. c. 1743–45, m. Thankful Ellis, a Revolutionary War private, d. 1828, will Plym. Prob. 66:215) who appears in the 1800 Rochester homestead division.
9. **G9's full child set and second marriage** are recovered: children Benjamin (1752), Betty (1756), Asa (1758), Jane, and Amos (G8, m. Ruth Gilbert); first wife Elizabeth Harden (m. 1 Jan. 1752, d. 30 July 1800), second wife Mercy Noyes (m. 17 Nov. 1800, d. 28 Mar. 1813).

## Source tracking

- **Existing sourceId:** `rigler-gurney-family-aaron-zuinglius-1994`. No new sourceId required. The entry currently has `corpusStatus: none`, `mediaPath: null`; operation **A1** updates it to reflect the page scans and the new corpus transcription. Sub-sources Rigler cites in-line (Cyrus Nash; Anna Gurney papers; Rev. Samuel Browne's Church Records; NEHGR; Suffolk/Plymouth probate and deeds) are cited *through Rigler* in fact-sheet and research footnotes — they are not minted as separate sourceIds. The John Harden 1751 will already has its own sourceId (`plymouth-probate-john-harden-1751-will`) and Rigler's citation of it (Plym. Prob. 12:383) aligns with the existing manuscript pp. 383–384 reference.
- **Validation:** `sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md` already exists; operation **A3** updates it from "bibliographic control only" to record the pages examined and where findings landed.
- **Media (already performed, Phase-1 exception at user direction):** the eight copyrighted page scans were moved out of `sources/intake/new/Rigler-pages/` into `sources/media/rigler-gurney-family-aaron-zuinglius-1994/_local/` (gitignored), with a committed `_local/README.md` stub listing each file. This deviates from the default Phase-1 boundary (no media moves) because the user explicitly directed the move and the pages are in-copyright. No further media operation is needed in Phase 2.
- **Worksheet source (new, operation A12):** `rigler-genealogy-notes-c1980` — five c. 1980 family-group worksheets signed Robert G. Rigler, M.D. (Honolulu), the earlier working draft behind the 1994 edition. The five scans were already moved to `sources/media/rigler-genealogy-notes-c1980/_local/` (gitignored, copyright) with a committed `_local/README.md`, mirroring the 1994 media handling. Transcription (incl. the citation boxes) is operation A14 (`sources/corpus_supplement/...worksheets-extract.md`); a thin validation is A13. Sub-authorities the worksheets cite — the Anna Gurney Papers (which the worksheets locate at the **Dyer Memorial Library, Abington**, where the 1994-entry transcription reads "NEHGS"); Nahum Mitchell, *History of Bridgewater*; town vital records — are cited through the worksheet, not minted separately. Note the worksheet byline (Robert G. Rigler, M.D.) differs from the 1994 book's credited author (Jean Gurney Rigler); same Honolulu household, flagged for the user.

---

# Operations (literal)

Phase 2 applies each `str_replace` against the verbatim `old_string`, and each `new file write` with the full body. No `NEW`-style placeholder footnote handles are used; footnote numbers are final.

## A1 — `data/sources.json`: update the Rigler entry

`str_replace`

old_string:
```
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": "sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md",
      "notes": "Key compiled genealogy for descendants of Richard Gurney of Weymouth, Massachusetts. Treat as a standing key source for G4-G13 American-line research companions and the G6 William Gurney case file. Internet Archive item text was not readable in v08; use as a source-control and future-pull entry until pages are checked."
```
new_string:
```
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md",
      "mediaPath": "sources/media/rigler-gurney-family-aaron-zuinglius-1994/",
      "validationPath": "sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md",
      "notes": "Key compiled genealogy for descendants of Richard Gurney of Weymouth, Massachusetts; compiled largely from primary records (town vital records, Suffolk and Plymouth probate and deeds, NEHGR). Standing key source for G4-G13 American-line research companions and the G6 William Gurney case file. The direct-line entries Richard-2 (G12) through Benjamin-5 (G9) are transcribed in the corpus supplement from 1994-edition page scans held local-only (copyright) under mediaPath. Internet Archive item gurneyfamilyfrom00rigl is an earlier edition."
```

## A2 — `new file write`: `sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`

```markdown
# Rigler, *The Gurney Family from Aaron to Zuinglius* (1994) — direct-line entries G9–G12

Source ID: `rigler-gurney-family-aaron-zuinglius-1994`

Working transcription of the four direct-line entries (Richard-2 → Benjamin-5) from Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary; Some Descendants of Richard Gurney Who Settled at Weymouth, MA before 1656*, rev. and expanded ed. (Honolulu: J. G. Rigler, 1994). Transcribed from page scans held local-only (copyright) at `sources/media/rigler-gurney-family-aaron-zuinglius-1994/_local/`. Rigler's in-line citations are preserved. Readings are faithful to the printed text; a handful of uncertain characters are marked `[?]`.

---

## RICHARD GURNEY-2 (p. 203)

RICHARD GURNEY-2 was b.c. 1630, England, probably the son of John Gurney-1 who was known to have settled in Weymouth & Braintree MA. He lived in Weymouth MA & there married Rebecca Taylor, d/o John & Rebecca Taylor of Weymouth. John Taylor's will, written 6 Jan., proved 22 May 1688 named his wife Rebecca & his daughter Rebecca, wife of Richard Gurney, & son John Taylor. (Suffolk Prob. 6:13) He was a freeman in 1681. (Savage 2:325)

> "Voted that Richard Gurney shall have 6 acres of the Town's Common land to build a house & fence to dwell thereon with his family in an absolute state of Inheritance. On the Town Common on the west side of the Pond. 1683."

Richard Gurney settled in Weymouth, but where it would perhaps be difficult now to determine, possibly on East Street towards Old Spain, and extending to Back River. (Hist. of Weymouth, p. 251)

Richard died Oct. 1691 intestate, in Weymouth MA (Weymouth VR). Suffolk Co. Probate 1691, Bond on the estate of Richard Gurney, Sr.; Administrators were Richard Gurney & Zachariah Gurney, John Gurney the eldest son refusing. Bondsmen were Joseph Green & John Richards. Hist. of Weymouth was in error in stating his death date as 1719 which in fact, belonged to his son, Richard.

Children: (Weymouth VR)
- + John, b.c. 1654, m. Elizabeth Green.
- Richard, b. 18 Jan. 1656, d. Oct. 1719 Weymouth, not married.
- + Zachariah, b.c. 1660, m. Mary Benson.
- Joseph, b.c. 22 Feb. 1664/5, d. 14 Dec. 1739, not married.
- Mary, b. 9 Sept. 1667, d. Feb. 1736 Weymouth, not married.
- + Benjamin, b.c. 1676, m. Rebecca Staples.

(The "+" prefix is Rigler's mark for children whose own descent she carries forward.)

Adjacent in the John Gurney-1 entry, two of Richard's siblings appear: **Peter**, of Weymouth, a soldier in Johnson's Co. Dec. 1675, killed in King Philip's War, Dec. 1676 (Savage 2:325); and **Sarah**, m. before 1675 John Vinson (d. 20 Sept. 1718), m. 2. in 1721 John Canterbery (d. 9 Dec. 1729) (NEHGR 46:188).

## BENJAMIN GURNEY-3 (Richard-2) (p. 19)

BENJAMIN GURNEY-3 (Richard-2) was b.c. 1676, probably in Weymouth, MA, s/o Richard & Rebecca (Taylor) Gurney. He m. 30 Dec. 1701 by Mr. Moses Fisk in First Church, Braintree MA, Rebecca Staples, b. 1682, d/o John-2 & Sarah (Atkins) Staples. (NEHGR 59:155, 116:20, 121:244) He moved from Weymouth to South Abington as early as 1707 & probably lived with his cousin, Samuel Gurney-3, who had married his wife's widowed mother. His name was listed on Axtell's accounts, list of hides, Feb. 1709 & 1710. He returned to Weymouth in 1710, but went back to Abington & on 8 Sept. 1726 purchased the Richard Williams farm on the Abington-Bridgewater line. (Plym. Deeds 25:79) This [was] bought from Samuel Staples of Scituate, also son of John & Sarah (Atkins) (Staples) (Gurney) Williams.

Cyrus Nash wrote (D 1:13) about "Benjamin not coming here at the right time. His wife Rebecca set out to look for him & found him lying asleep in a field. It made her so sore that she took the pipe out of her mouth & set fire to the grass around him to give him a good scare. She succeeded & also succeeded in causing one of the biggest fires of the time, burning over many acres of low ground, which thereafter was known as Granny Gurney's Swamp."

Benjamin sold his farm to Abraham Pierce on 20 Oct. 1730 & moved his family to Middleboro, MA. (Plym. Reg. 31:69, 70) Jointly with his son Benjamin, he bought land from Samuel Tinkham of Middleboro on 28 Oct. 1730 consisting of 3 lots of upland & 1 lot of meadow containing about 2 acres. (Plym. Reg. 39:79) His son later sold this on 3 May 1749 after his father's death.

He died in Middleboro, MA, his will dated 4 May 1738, proved 1739: "to my wife, Rebeckah Gurney, the [use] of all my homestead that is in partnership between myself & my son Benjamin Gurney; to son Benjamin all of that parcel of land bought of Joseph Richards; to daughter Rebecca Taylor, wife of Daniel Taylor, £40 to be paid to her out of my estate at her mother's decease; to son-in-law Daniel Taylor, 20 shillings; moveables to my wife." (Plym. Probate 8:98)

Children: (b. Weymouth MA)
- Rebecca, b. 22 Nov. 1702, m. 24 Aug. 1731 by Joshua Cushing, J.P., Daniel Taylor of Kingston MA. (Kingston VR)
- + Benjamin, b. probably c. 1704, & Jane (Jean) Harden; m. 1731 Sarah Morse.

## BENJAMIN GURNEY-4 (Benjamin-3, Richard-2) (pp. 19–21)

BENJAMIN GURNEY-4 (Benjamin-3, Richard-2) was b.c. 1704, Weymouth MA, s/o Benjamin & Rebecca (Staples) Gurney. He moved about 1707 with his father's family from Weymouth to Abington MA & settled in that part which is now Whitman, probably on South Washington St. (Anna Gurney papers, NEHGS)

He became enamoured of Jane (Jean) Harden & apparently fathered her son, Benjamin who was bpt. 30 May 1730 in Abington. Jane was b. 19 Nov. 1709 in Abington, d/o of Cap't. John & Mary (Littlefield) Harden (Abington VR), bpt. 1711 in Braintree. Her baptism is interesting in local records because it was the earliest known proof that the "Little Comfort Mill" was used as a landmark to describe that area of Abington which now comprises Whitman. John Gurney-3 (Richard-2) had started the Little Comfort mill. Her parents took her back to their home town of Braintree to be baptized in 1711 because there was no church until the following year, 1712, when Abington was incorporated. Rev. Samuel Niles baptized John Harden in the records as "of Little Comfort". Jane Harden m. 29 Dec. 1731, Ebenezer Spear.

Benjamin moved with his parents to Middleboro MA & there married 14 June 1731 by Rev. Benjamin Ruggles, Sarah Morse, b. 7 Feb. 1711/12, d/o Jonathan & Anna (Barden) Morse, Jr. (Middleboro VR) With his father he bought land of Samuel Tinkham on 26 Oct. 1730 which he & Sarah sold 3 May 1749 after his father's death. (Plym. Reg. 39:79) He also bought 8 acres of Middleboro land from Sam Eddy, Jr. on 7 Nov. 1731 & was a subscriber to the church in what is now Carver, MA.

He moved to Rochester MA where he died before 13 Dec. 1771, when his son Lemuel mortgaged "a certain tract in Rochester in the easternmost part of said town, it being the estate of my father, Benjamin Gurney, late of Rochester." (Plym. Reg. 57:47) Lemuel, Benjamin, & Levi Gurney, all of Rochester MA agreed 1 Jan. 1800, to divide the homestead farm which they owned in common, it being the estate of their father, Benjamin Gurney, late of Rochester deceased. (Plym. Co. land deed 95:139, GS film 559,140)

Child: (b. Abington MA, by Jane Harden)
- + Benjamin, bpt 30 May 1730 (Rev. Samuel Browne's Church Records, Hist. Soc. of Old Abington), m. Elizabeth "Betsey" "Betty" Harden.

Children: (b. Middleboro MA, by Sarah (Morse) Gurney) — Susannah (m. 26 July 1752 Jabez Benson of Wareham); Grace (m. int. 28 Nov. 1757 Joshua Ramon/Raymond); + Lemuel (b.c. 1738, m. Elizabeth Wrightington); + Benjamin (b.c. 1745, m. Thankful Ellis); + Levi (b.c. 1746, m. 1. Mary Hathaway, 2. Rebecca Hathaway); perhaps Sarah; perhaps Jemima.

## BENJAMIN GURNEY-5 (Benjamin-4,3, Richard-2) (pp. 21–22)

BENJAMIN GURNEY-5 (Benjamin-4,3, Richard-2) was bpt. 30 May 1730 in Abington MA, s/o Benjamin Gurney & Jane "Jean" Harden. (Abington VR; Rev. Samuel Browne's Church Records in the Hist. Society of Old Abington) He was raised in Abington by Nathan-4 & Sarah (Harden) Gurney, his mother's sister & was named in his grandfather John Harden's will of 17 Sept. 1751. (Plym. Prob. 12:383: John Harden of Bridgewater, blacksmith, "to my wife the improvement of all my estate & income from same during her life, after her decease, to my 4 daughters & unto heirs of daughter Rebecca Noyes, deceased. The above said estate to be equally divided 1/5 to Mary Hobart; 1/5 to Sarah Gurney; 1/5 to Jane Spear; 1/5 to children of Rebecca N. Noyes, deceased; & 1/5 to Lydia Dawes. To my son John Harden, blacksmith's tools & chains. To grandson Benjamin Gurney, 20 shillings to be paid by executors, wife Mary & son-in-law Robert Dawes.")

He m. 1. 1 Jan. 1752 Abington, Elizabeth Harden, b.c. 1730, d/o Samuel Harden. (Abington VR) Elizabeth d. 30 July 1800 in her 70th year in Cummington MA & was bur. in Dawes Cem. He m. 2. 17 Nov. 1800 Cummington, Mercy Noyes, b.c. 1740/41. (Cummington Town Rec.)

Benjamin lived in Northville MA, a small community between East Bridgewater & what is now Whitman, which was within the bounds of East Bridgewater. The boundary was changed 3 times & it sometimes was part of South Abington, now Whitman.

About June 1770 he sold land in Abington & moved his family to Town # 5, now Cummington, Hampshire Co. MA. Records at Springfield MA show Benjamin Gurney & Silas Reed bought land in Town # 5 on 5 Nov. 1770 & he was described in the deed as yeoman of Town # 5, formerly of Bridgewater. In 1787 Benjamin Gurney & Philip Shaw purchased each others farms. ("Only One Cummington", H.H. Foster & William Streeter, 1974, p. 390; "Hampshire Co. MA Biographies", 1896, p. 196) He was listed in the 1790 Fed. Census, 3-0-3.

Benjamin d.c. 28 Sept. 1805 in his 76th year & Mercy d. 28 Mar. 1813; both were bur. Dawes Cemetery, Cummington MA. (Cummington Town Rec.)

Children:
- Benjamin, b. 25 Aug. 1752, Bridgewater, d. 1 Mar. 1804, Cummington, m. 20 July 1802 Cummington, Esther Cole (b.c. 1760, d. 5 Feb. 1837, age 77, Cummington). They had 1 daughter, Clarissa Gurney, b. 30 Sept. 1803, d. 23 Jan. 1813, age 9. (Cummington VR)
- Betty "Betsey", b. 15 Nov. 1756 Bridgewater, d. 12 May 1805 Cummington.
- + Asa, b. 24 Oct. 1758 Bridgewater, m. Molly Reed.
- Jane.
- + Amos, m. Ruth Gilbert. [G8 in the direct line]

## The "second Benjamin" (collateral) — for the two-Benjamin disambiguation

BENJAMIN GURNEY-5 (Benjamin-4,3, Richard-2) — the half-brother by Sarah Morse — was b.c. 1743–1745, Middleboro, Plymouth Co. MA, s/o Benjamin & Sarah (Morse) Gurney. Published 11 Aug. & m. 23 Aug. 1781 by Rev. Asa Hunt, Thankful Ellis (b. 1 Apr., bpt. 26 July 1761 Middleboro, d/o Mathias-5 & Rachel (Tupper) Ellis; NEHGR 121:40). He served in the War of the Revolution, Private, with several enlistments (Mass. Soldiers & Sailors; DAR Patriot Index 1:291); his pension file (W-14837) gives his age as 73 in 1818, and his widow Thankful received a pension. A yeoman of Rochester for more than 40 years; on 18 Sept. 1770 some 16 acres were laid out to Benjamin Gurney (father), Levi Gurney, Benjamin Gurney 2nd, & Lemuel Gurney (brothers). He wrote his will 16 Dec. 1826, proved 11 Aug. 1828, naming children Samuel, Heman, Hannah Briggs, Nancy Hathaway, Rachel White, & Thankful Tabor (Plym. Prob. 66:215). He d. 4 July 1828 in his 85th year; Thankful d. 19 June 1845 in her 84th year, bur. Pierceville (now Woodside) Cem., Rochester.
```

## A3 — `sources/validations/rigler-gurney-family-aaron-zuinglius-1994.md`: full rewrite

`new file write` (overwrite existing):

```markdown
# Rigler, *Gurney Family from Aaron to Zuinglius* (1994) — validation

Source ID: `rigler-gurney-family-aaron-zuinglius-1994`

Patchset: `sources/intake/done/v84-rigler-g9-g12-intake.patchset.md`

## Source examined
Eight page scans of the 1994 revised-and-expanded edition (author's signed gift copy), held local-only (copyright) at `sources/media/rigler-gurney-family-aaron-zuinglius-1994/_local/`. Pages cover the direct-line entries Richard-2 (G12), Benjamin-3 (G11), Benjamin-4 (G10), and Benjamin-5 (G9), the title page, and adjacent fragments of the John Gurney-1 children list and the collateral "second Benjamin."

## Scope examined
The four direct-line entries (G9–G12) and the immediately adjacent children lists. Not examined: the bulk of the dictionary (other branches, Aaron-to-Zuinglius alphabetical descendants).

## Method
The supplied screenshots are low-resolution; legibility was recovered by cropping and upscaling each page before transcription. Rigler's in-line citations were preserved. A few uncertain characters are flagged in the corpus transcription.

## Findings
Promote. The four entries were transcribed to `sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md` and the substantive findings recorded on the G9–G12 research companions and fact sheets. Key resolutions: Richard's 1691 (not 1719) death; Mendon-massacre death reattributed off Richard's son; Rebecca Taylor and Rebecca Staples parentage; the Granny Gurney's Swamp source (Cyrus Nash); independent confirmation of G10 as father of G9; the aunt-upbringing (Nathan & Sarah Harden Gurney); and the two-Benjamin resolution.

## Limits
- 1994 compiled secondary source; treat as reliable but cite Rigler's underlying primary records (Suffolk/Plymouth probate and deeds, town vital records) where they are independently reachable.
- The *History of Weymouth* "Phebe Taylor" mother-name and Rigler's "Rebecca Taylor" mother-name conflict (preserved on the G12 companion).
- Page numbering on the supplied scans is mixed (a "203" page among the Benjamin entries' pp. 19–23); cite by entry as well as page.
```

---

## A4 — G12 research companion — `research/people/g12-richard-gurney-fact-sheet.research.md`

### A4-1 — insert a Rigler findings section above Sources Consulted

`str_replace`

old_string:
```
## Sources Consulted
```
new_string:
```
## Rigler (1994) findings — direct page audit

Jean Gurney Rigler's *Gurney Family from Aaron to Zuinglius* (1994) carries a full Richard-2 entry, transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md). It resolves several open points on this person.

**Death year — 1691, not 1719.** Rigler: "Hist. of Weymouth was in error in stating his death date as 1719 which in fact, belonged to his son, Richard." Richard-2 died Oct. 1691, intestate; the 1719 date belongs to son Richard (b. 18 Jan. 1656, d. Oct. 1719, unmarried).[^rigler-g12]

**Administration, 1691.** Suffolk Co. Probate, 1691; bond on the estate of Richard Gurney, Sr.; administrators were sons Richard and Zachariah Gurney, "John Gurney the eldest son refusing"; bondsmen Joseph Green and John Richards. The eldest son John being alive in 1691 is the key datum reattributing the Mendon death below.[^rigler-g12]

**Mendon massacre reattributed off Richard's son.** Because the eldest son John (b. c. 1654, m. Elizabeth Green) was alive to refuse administration in 1691, the 1675 Mendon victim John was not Richard's son but a son of the emigrant John Gurney-1 (G13) — Richard's brother — as is Peter, "a soldier in Johnson's Co. Dec. 1675, killed in King Philip's War, Dec. 1676." This matches the G13 companion's lead L-17 note about the conflated Mendon-1675 John, and corrects the G12 fact sheet's earlier "his son John was killed at the Mendon massacre."[^rigler-g12]

**Rebecca Taylor's parentage.** Daughter of John and Rebecca Taylor of Weymouth; John Taylor's will (Suffolk Prob. 6:13, written 6 Jan., proved 22 May 1688) names "his daughter Rebecca, wife of Richard Gurney," alongside wife Rebecca and son John Taylor. The mother's name conflicts with the *History of Weymouth* "Phebe Taylor" reading — Rebecca per the will, Phebe per Weymouth — so preserve both.[^rigler-g12][^history-of-weymouth-g12]

**Children of Richard-2 (Weymouth VR).** A fuller, reconciled set, ending the Weymouth-vs-companion children conflict: John (b. c. 1654, m. Elizabeth Green); Richard (b. 18 Jan. 1656, d. 1719, unmarried); Zachariah (b. c. 1660, m. Mary Benson); Joseph (b. 22 Feb. 1664/5, d. 1739, unmarried); Mary (b. 9 Sept. 1667, d. 1736, unmarried); and Benjamin (G11, b. c. 1676, m. Rebecca Staples).[^rigler-g12]

[^rigler-g12]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary*, rev. ed. (Honolulu: J. G. Rigler, 1994), Richard-2 entry (p. 203), with the adjacent John Gurney-1 children Peter and Sarah. Transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.

---

## Sources Consulted
```

### A4-2 — mark open question #6 resolved

`str_replace`

old_string:
```
6. **Reconcile Richard's death year**: Torrey gives -1691; *History of Weymouth* gives Oct. 1719. Plymouth County and Suffolk County probate, plus Weymouth town-meeting and vital records, are the right places to test which year belongs to Richard2 the father and which (if either) belongs to Richard3 his son b. 18 Jan. 1656.
```
new_string:
```
6. **Richard's death year — resolved (1691).** Rigler states the *History of Weymouth* 1719 date "was in error… which in fact, belonged to his son, Richard" (b. 18 Jan. 1656, d. Oct. 1719, unmarried). Richard-2 died Oct. 1691, intestate; the 1691 Suffolk Co. administration named sons Richard and Zachariah, with eldest son John refusing. See the Rigler findings section.
```

### A4-3 — replace the stale "audit pending" Rigler line in Sources Consulted

`str_replace`

old_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994). Key compiled genealogy for the G4-G13 direct line; source ID `rigler-gurney-family-aaron-zuinglius-1994`. Full page-level audit still pending.
- *History of Weymouth, Massachusetts*, Vol. 3 Genealogy of Weymouth families, Richard Gurney entry. Source ID `history-of-weymouth`. Transcribed extract at [`sources/corpus_supplement/history-of-weymouth-vol3-gurney.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/history-of-weymouth-vol3-gurney.md).
```
new_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994), Richard-2 entry (p. 203); audited — see the Rigler findings section above. Source ID `rigler-gurney-family-aaron-zuinglius-1994`. Transcribed extract at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md).
- *History of Weymouth, Massachusetts*, Vol. 3 Genealogy of Weymouth families, Richard Gurney entry. Source ID `history-of-weymouth`. Transcribed extract at [`sources/corpus_supplement/history-of-weymouth-vol3-gurney.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/history-of-weymouth-vol3-gurney.md).
```

---

## A5 — G12 fact sheet — `fact-sheets/g12-richard-gurney-fact-sheet.md`

### A5-1 — subtitle: brother, not son, at Mendon

`str_replace`

old_string:
```
subtitle: "Weymouth, Massachusetts proprietor and Freeman 1681; son of John Gurney-1, the colonial emigrant; one of his sons died at the Mendon massacre of 1675."
```
new_string:
```
subtitle: "Weymouth, Massachusetts proprietor and Freeman 1681; son of John Gurney-1, the colonial emigrant; his brother died in the Mendon massacre of 1675."
```

### A5-2 — Died vital cell

`str_replace`

old_string:
```
    <div class="fact-value">October 1691, Weymouth, Massachusetts. Died intestate. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```
new_string:
```
    <div class="fact-value">October 1691, Weymouth, Massachusetts. Died intestate; his estate was administered by his sons Richard and Zachariah. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

### A5-3 — Marriage vital cell

`str_replace`

old_string:
```
        <div><strong>Rebecca Taylor</strong> — named in Taylor's will, proved 1688. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```
new_string:
```
        <div><strong>Rebecca Taylor</strong> — daughter of John and Rebecca Taylor of Weymouth; named in her father's will, proved 1688. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```

### A5-3b — Highlights: proprietor bullet (story-led; inline page ref to footnote)

`str_replace`

old_string:
```
  <li><strong>One of the early proprietors of Weymouth.</strong> The published <em>History of Weymouth</em> records Richard Gurney holding lands in the town from before 1642–44 — "in the East field," "in the mill field," and "on the east side of Great Pond." A 1683 town meeting voted him a six-acre town common grant on the west side of the Pond "to build a house &amp; fence" (<em>Hist. of Weymouth</em>, p. 251). He is one of a handful of named landholders in seventeenth-century Weymouth from whom the family's continued Plymouth County presence directly descends. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```
new_string:
```
  <li><strong>One of the early proprietors of Weymouth.</strong> Richard held lands in the town from before 1642–44 — "in the East field," "in the mill field," and "on the east side of Great Pond" — and in 1683 a town meeting granted him six acres of common land on the west side of the Pond "to build a house &amp; fence." He stands among a handful of named landholders in seventeenth-century Weymouth from whom the family's continued Plymouth County presence directly descends. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
```

### A5-4 — Highlights: King Philip's War bullet

`str_replace`

old_string:
```
  <li><strong>His son John was killed at the Mendon massacre of 1675.</strong> The Mendon attack of 14 July 1675 was the first major violence of King Philip's War. John Gurney Jr. (G12's son) was among the dead. A second son, Zachariah, served in a King Philip's War relief company. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```
new_string:
```
  <li><strong>King Philip's War struck the wider family hard.</strong> Richard's brother John was among the dead in the Mendon massacre of 14 July 1675 — the first major bloodshed of the war — and a second brother, Peter, a soldier in Captain Johnson's company, was killed in the fighting late in 1676. Richard himself stayed at Weymouth, and his own children all outlived the war. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
```

### A5-5 — Children table

`str_replace`

old_string:
```
  <tbody>
    <tr><td>Benjamin Gurney</td><td>c. 1676 – 1738/9</td><td>G11 in direct line. <sup class="fn"><a href="#n7" id="ref-7b">7</a></sup></td></tr>
    <tr><td>John Gurney Jr.</td><td>– d. July 1675</td><td>Killed at the Mendon massacre, 14 July 1675. <sup class="fn"><a href="#n6" id="ref-6b">6</a></sup></td></tr>
    <tr><td>Zachariah Gurney</td><td></td><td>Served in a King Philip's War relief company. <sup class="fn"><a href="#n6" id="ref-6c">6</a></sup></td></tr>
  </tbody>
```
new_string:
```
  <tbody>
    <tr><td>John Gurney</td><td>c. 1654 – after 1691</td><td>Married Elizabeth Green; as eldest son, declined to administer his father's estate in 1691. <sup class="fn"><a href="#n7" id="ref-7c">7</a></sup></td></tr>
    <tr><td>Richard Gurney</td><td>1656 – 1719</td><td>Born 18 January 1656; died unmarried at Weymouth — the source of the 1719 date once mistakenly given for his father. <sup class="fn"><a href="#n7" id="ref-7d">7</a></sup></td></tr>
    <tr><td>Zachariah Gurney</td><td>c. 1660</td><td>Married Mary Benson; co-administrator of his father's estate in 1691. <sup class="fn"><a href="#n7" id="ref-7e">7</a></sup></td></tr>
    <tr><td>Joseph Gurney</td><td>1664/5 – 1739</td><td>Born 22 February 1664/5; died unmarried. <sup class="fn"><a href="#n7" id="ref-7f">7</a></sup></td></tr>
    <tr><td>Mary Gurney</td><td>1667 – 1736</td><td>Born 9 September 1667; died unmarried at Weymouth. <sup class="fn"><a href="#n7" id="ref-7g">7</a></sup></td></tr>
    <tr><td>Benjamin Gurney</td><td>c. 1676 – 1738/9</td><td>G11 in the direct line; married Rebecca Staples. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></td></tr>
  </tbody>
```

### A5-6 — Narrative paragraph 2 (King Philip's War)

`str_replace`

old_string:
```
<p>The most personal mark of those years on the family is bleak. Richard's son John Gurney Jr. was among the dead at the Mendon massacre of 14 July 1675, the first major violence of King Philip's War, when a group of Nipmucs attacked the small frontier town of Mendon and killed several inhabitants. A second son, Zachariah, served in the colony's relief companies during the same conflict. Richard himself remained in Weymouth, neither soldier nor displaced, until he died intestate in October 1691.</p>
```
new_string:
```
<p>The most personal mark of those years on the family is bleak, though it fell on Richard's brothers rather than his sons. His brother John was among the dead at the Mendon massacre of 14 July 1675 — the first major violence of King Philip's War, when Nipmuc fighters attacked the small frontier town of Mendon and killed several inhabitants — and another brother, Peter, a soldier in Captain Johnson's company, was killed in the war late in 1676. Richard himself remained at Weymouth through it all, neither soldier nor displaced. He died intestate in October 1691, his estate administered by two of his sons, Richard and Zachariah, after the eldest son John declined the duty — the very record that finally untangles Richard from the 1719 death date long misattributed to him from his same-named son.</p>
```

### A5-7 — Narrative paragraph 3 (son/grandson correction)

`str_replace`

old_string:
```
<p>The land that linked Richard's generation to his grandson and great-grandson Benjamins (G11 and G10) is the small but persistent Plymouth County thread of the family's seventeenth- and eighteenth-century life. The land near the Abington–Bridgewater line that passed to son Benjamin (G11) — and that gave rise to "Granny Gurney's Swamp" two generations later — was likely an inherited piece of John Gurney-1's New England estate, channelled through Richard. Without that line of descent, none of the Cummington / New York / Indiana chapters of this family would exist.</p>
```
new_string:
```
<p>The land that linked Richard's generation to his son and grandson Benjamins (G11 and G10) is the small but persistent Plymouth County thread of the family's seventeenth- and eighteenth-century life. The land near the Abington–Bridgewater line that passed to his son Benjamin (G11) — on which "Granny Gurney's Swamp" got its name a generation later — was likely an inherited piece of John Gurney-1's New England estate, channelled through Richard. Without that line of descent, none of the Cummington, New York, or Indiana chapters of this family would exist.</p>
```

### A5-8 — Citations list (full replace; removes data-file references, adds Rigler/Taylor/children notes)

`str_replace`

old_string:
```
<ol class="citation-list">
  <li id="n1">Birth c. 1630–1634 in England, son of John Gurney (G13) and Mary. <code>data/ancestors v26.json</code>, G12 and G13 entries. For G13's emigration and family see <a href="/key-research/john-gurney-case-file.html">John Gurney case file</a>. <a class="citation-back" href="#ref-1">↩</a></li>
  <li id="n2">Died October 1691, Weymouth, Massachusetts, intestate. <code>data/ancestors v26.json</code>, G12 entry. <a class="citation-back" href="#ref-2">↩</a></li>
  <li id="n3">Admitted Freeman 1681; land grants from before 1642–44. <em>History of Weymouth</em>, Massachusetts (the 1923 four-volume town history). Source ID: <code>history-of-weymouth</code>. <a class="citation-back" href="#ref-3">↩</a></li>
  <li id="n4">Rebecca Taylor named in her father's will, proved 1688. <code>data/ancestors v26.json</code>, G12 entry. Specific Taylor will reference and Plymouth Probate citation not yet captured here. <a class="citation-back" href="#ref-4">↩</a></li>
  <li id="n5"><em>History of Weymouth</em>, particularly p. 251 for the 1683 town-meeting grant of six acres on the west side of the Pond. Source ID: <code>history-of-weymouth</code>. <a class="citation-back" href="#ref-5">↩</a></li>
  <li id="n6">Mendon massacre, 14 July 1675 — opening of King Philip's War. John Gurney Jr.'s death and Zachariah Gurney's service in relief companies recorded in <code>data/ancestors v26.json</code>, G12 entry; corroborated by Sprague, <em>Genealogies of Braintree</em> (Source ID: <code>sprague-braintree</code>) for the John Gurney-1 family. <a class="citation-back" href="#ref-6">↩</a></li>
  <li id="n7">See <a href="/fact-sheets/g11-benjamin-gurney-fact-sheet.html">Benjamin Gurney (G11) fact sheet</a> for the Abington-line continuation. <a class="citation-back" href="#ref-7">↩</a></li>
</ol>
```
new_string:
```
<ol class="citation-list">
  <li id="n1">Born c. 1630 in England, probably a son of the colonial emigrant John Gurney (G13). Jean Gurney Rigler, <em>The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary</em>, rev. ed. (Honolulu: J. G. Rigler, 1994), Richard-2 entry. For G13's emigration and family see the <a href="/key-research/john-gurney-case-file.html">John Gurney case file</a>. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-1">↩</a></li>
  <li id="n2">Died October 1691, Weymouth, Massachusetts, intestate; Suffolk County probate, 1691, bond on the estate of Richard Gurney, Sr., with sons Richard and Zachariah Gurney as administrators and the eldest son John declining. Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Richard-2 entry. Rigler notes that the 1719 death date given in the <em>History of Weymouth</em> belongs instead to Richard's same-named son. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>history-of-weymouth</code>. <a class="citation-back" href="#ref-2">↩</a></li>
  <li id="n3">Admitted Freeman of Massachusetts Bay, 1681 (James Savage, <em>A Genealogical Dictionary of the First Settlers of New England</em>, vol. 2, p. 325, via Rigler); land grants in Weymouth from before 1642–44 per the <em>History of Weymouth</em>, Massachusetts (the 1923 four-volume town history). Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>history-of-weymouth</code>. <a class="citation-back" href="#ref-3">↩</a></li>
  <li id="n4">Rebecca Taylor, daughter of John and Rebecca Taylor of Weymouth; her father John Taylor's will (Suffolk County Probate 6:13, written 6 January, proved 22 May 1688) names "his daughter Rebecca, wife of Richard Gurney." Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Richard-2 entry. The <em>History of Weymouth</em> gives the mother's name as Phebe rather than Rebecca; the two readings conflict. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>history-of-weymouth</code>. <a class="citation-back" href="#ref-4">↩</a></li>
  <li id="n5"><em>History of Weymouth</em>, particularly p. 251 for the 1683 town-meeting grant of six acres on the west side of the Pond "to build a house &amp; fence," quoted in Rigler's Richard-2 entry. Source IDs: <code>history-of-weymouth</code>; <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-5">↩</a></li>
  <li id="n6">The Mendon massacre of 14 July 1675 opened King Philip's War. The John Gurney killed there, and Peter Gurney, "a soldier in Johnson's Co.… killed in King Philip's War, Dec. 1676," were sons of the emigrant John Gurney-1 (G13) — Richard's brothers, not his sons — as shown by Rigler's John Gurney-1 children and by the eldest son John of Richard being alive to refuse administration in 1691. See the <a href="/key-research/john-gurney-case-file.html">John Gurney case file</a> and Rigler, <em>Gurney Family from Aaron to Zuinglius</em>. Corroborated for the John Gurney-1 family group by Sprague, <em>Genealogies of Braintree</em>. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>sprague-braintree</code>. <a class="citation-back" href="#ref-6">↩</a></li>
  <li id="n7">Children of Richard Gurney from the Weymouth vital records, as compiled in Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Richard-2 entry: John (b. c. 1654, m. Elizabeth Green), Richard (b. 18 January 1656, d. 1719, unmarried), Zachariah (b. c. 1660, m. Mary Benson), Joseph (b. 22 February 1664/5, d. 1739, unmarried), and Mary (b. 9 September 1667, d. 1736, unmarried). Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-7">↩</a></li>
  <li id="n8">See the <a href="/fact-sheets/g11-benjamin-gurney-fact-sheet.html">Benjamin Gurney (G11) fact sheet</a> for the Abington-line continuation; Rigler gives his marriage to Rebecca Staples. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-8">↩</a></li>
</ol>
```

### A5-9 — Timeline: King Philip's War row

`str_replace`

old_string:
```
      <tr><td>1675</td><td>Son John Gurney Jr. killed at the Mendon massacre, 14 July; son Zachariah serves in a King Philip's War relief company.</td></tr>
```
new_string:
```
      <tr><td>1675–76</td><td>Brother John killed at the Mendon massacre (14 July 1675); brother Peter killed in King Philip's War (1676).</td></tr>
```

---

## A6 — G11 research companion — `research/people/g11-benjamin-gurney-fact-sheet.research.md`

### A6-1 — insert a Rigler findings section above Sources Consulted

`str_replace`

old_string:
```
## Sources Consulted
```
new_string:
```
## Rigler (1994) findings — direct page audit

Rigler's Benjamin-3 (Richard-2) entry, transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md), supplies parentage, a named source for the swamp story, and the will text.

**Rebecca Staples's parentage.** Born 1682, daughter of John-2 and Sarah (Atkins) Staples (NEHGR 59:155, 116:20, 121:244). This confirms the kinship reading: the Samuel Staples of Scituate who sold Benjamin the Williams farm in 1726 was "also son of John & Sarah (Atkins)" — Rebecca's brother — making the 1726 purchase a within-family transfer rather than an arm's-length sale.[^rigler-g11]

**Marriage officiant and the early moves.** Married 30 Dec. 1701 by Mr. Moses Fisk at the First Church, Braintree. Benjamin moved from Weymouth to South Abington as early as 1707, probably living with his cousin Samuel Gurney-3 — who had married Rebecca's widowed mother, Sarah (Atkins) Staples; he was listed on Axtell's hide accounts in Feb. 1709 and 1710, returned to Weymouth in 1710, then went back to Abington.[^rigler-g11]

**The Joseph Richards land — bought, not bequeathed.** The will clause "to son Benjamin all of that parcel of land bought of Joseph Richards" shows the land was purchased from Joseph Richards and willed by G11 to his son Benjamin (G10). The earlier reading of a Joseph Richards *bequest to G11* is corrected — Richards was a grantor, not a benefactor.[^rigler-g11]

**Will text (Plym. Probate 8:98).** Dated 4 May 1738, proved 1739: wife Rebeckah the use of the homestead held in partnership with son Benjamin; son Benjamin the Joseph Richards parcel; daughter Rebecca Taylor (wife of Daniel Taylor) £40 at her mother's decease; son-in-law Daniel Taylor 20 shillings; moveables to the wife.[^rigler-g11]

**"Granny Gurney's Swamp" — the named source.** Cyrus Nash (cited by Rigler as "D 1:13") is the printed source long sought for this story: Rebecca went looking for Benjamin, found him "lying asleep in a field," and "took the pipe out of her mouth & set fire to the grass around him to give him a good scare," starting "one of the biggest fires of the time, burning over many acres of low ground, which thereafter was known as Granny Gurney's Swamp." Full quote in the corpus extract.[^rigler-g11]

**A daughter, Rebecca.** Rebecca Gurney, b. 22 Nov. 1702, m. 24 Aug. 1731 (by Joshua Cushing, J.P.) Daniel Taylor of Kingston (Kingston VR) — not previously recorded in this companion; the only sibling of G10 that Rigler carries.[^rigler-g11]

[^rigler-g11]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary*, rev. ed. (Honolulu: J. G. Rigler, 1994), Benjamin-3 (Richard-2) entry (p. 19), quoting Cyrus Nash for the Granny Gurney's Swamp story and the will of 4 May 1738 (Plymouth Probate 8:98). Transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.

---

## Sources Consulted
```

### A6-2 — resolve open questions 4, 5, 6

`str_replace`

old_string:
```
4. **"Granny Gurney's Swamp" — exact published references.** Hobart, Mitchell, or local place-name sources.
5. **The Joseph Richards bequest.** Whose will, what relationship to G11?
6. **Rebecca Staples's family.** Likely kin of Samuel Staples of Scituate (1726 grantor of the Williams farm); a Staples genealogy would clarify.
```
new_string:
```
4. **"Granny Gurney's Swamp" — resolved (named source).** Cyrus Nash, quoted by Rigler ("D 1:13"). The underlying Nash text (a Weymouth/Abington local history) would be worth a direct pull, but the story now has a printed attribution. (Unknown online.)
5. **The Joseph Richards land — resolved.** Not a bequest to G11. The will shows the parcel was "bought of Joseph Richards" and passed by G11 to his son Benjamin. Joseph Richards was the seller.
6. **Rebecca Staples's family — resolved.** Daughter of John-2 and Sarah (Atkins) Staples, b. 1682; Samuel Staples of Scituate, the 1726 grantor, was her brother. The 1726 purchase was a within-family transfer. (NEHGR 59:155, 116:20, 121:244.)
```

### A6-3 — replace the stale "audit pending" Rigler line in Sources Consulted

`str_replace`

old_string:
```
- <code>data/ancestors v26.json</code>, G11 entry.
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994). Key compiled genealogy for the G4-G13 direct line; source ID `rigler-gurney-family-aaron-zuinglius-1994`. Full page-level audit still pending.
```
new_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994), Benjamin-3 entry (p. 19); audited — see the Rigler findings section above. Source ID `rigler-gurney-family-aaron-zuinglius-1994`. Transcribed extract at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md).
```

---

## A7 — G11 fact sheet — `fact-sheets/g11-benjamin-gurney-fact-sheet.md`

### A7-1 — Marriage vital cell

`str_replace`

old_string:
```
        <div><strong>Rebecca Staples</strong> — married 30 December 1701, First Church Braintree, Massachusetts. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```
new_string:
```
        <div><strong>Rebecca Staples</strong> — born 1682, daughter of John and Sarah (Atkins) Staples; married 30 December 1701 at the First Church of Braintree, Massachusetts, by the Rev. Moses Fiske. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
```

### A7-2 — Highlights block (all four bullets)

`str_replace`

old_string:
```
  <li><strong>"Granny Gurney's Swamp."</strong> A small piece of low ground near the Abington–Bridgewater line was named for the family after a fire incident involving Rebecca Staples (Granny Gurney). The story is independently confirmed in two local-history sources. The site is not a property the family owned, but the local-place-name memorial of an early-eighteenth-century moment in Rebecca's life. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>Three documented Plymouth County land transactions.</strong> Bought the Richard Williams farm on the Abington–Bridgewater line on 8 September 1726 from Samuel Staples of Scituate (Plymouth Deeds 25:79). Sold the same to Abraham Pierce on 20 October 1730 upon moving to Middleboro (Plymouth Registry 31:69, 70). Earlier, received land from Joseph Richards bequeathed in his will to son Benjamin. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></li>
  <li><strong>Will proved 1739 — the firm closing record of his life.</strong> Plymouth Probate 8:98 preserves his will, proved in 1739. The will is the immediate documentary anchor for his death year and for his recognition of his children. <sup class="fn"><a href="#n2" id="ref-2b">2</a></sup></li>
  <li><strong>Married at the First Church of Braintree.</strong> The 30 December 1701 marriage at First Church Braintree places him within the Massachusetts Bay Puritan congregational record system at exactly the kind of well-documented parish that survives today. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
```
new_string:
```
  <li><strong>"Granny Gurney's Swamp."</strong> A stretch of low ground near the Abington–Bridgewater line still carried the family's name generations later. As the local historian Cyrus Nash told it, Rebecca — "Granny Gurney" — went looking for Benjamin, found him asleep in a field, and in vexation tipped her lit pipe into the dry grass to give him a scare; the blaze got away from her and burned over many acres, leaving the swamp its name. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></li>
  <li><strong>A working farmer's land trail across Plymouth County.</strong> On 8 September 1726 he bought the Richard Williams farm on the Abington–Bridgewater line from Samuel Staples of Scituate — his wife's own brother — and sold it to Abraham Pierce in October 1730 when he moved to Middleboro. He also held a parcel bought from Joseph Richards that his will later left to his son Benjamin. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></li>
  <li><strong>A will that names his household.</strong> Dated 4 May 1738 and proved in 1739, his will gave wife Rebeckah the use of the homestead, left son Benjamin the land bought of Joseph Richards, and set aside forty pounds for daughter Rebecca, wife of Daniel Taylor — the documentary anchor for his death year and his children. <sup class="fn"><a href="#n2" id="ref-2b">2</a></sup></li>
  <li><strong>Married into the Staples family at Braintree.</strong> His 30 December 1701 marriage to Rebecca Staples was performed by the Rev. Moses Fiske at the First Church of Braintree, the kind of well-documented Massachusetts Bay congregation whose registers survive today. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
```

### A7-3 — Children table

`str_replace`

old_string:
```
  <tbody>
    <tr><td>Benjamin Gurney</td><td>c. 1704 – before 1772</td><td>G10 in direct line. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></td></tr>
  </tbody>
```
new_string:
```
  <tbody>
    <tr><td>Rebecca Gurney</td><td>b. 22 November 1702</td><td>Married Daniel Taylor of Kingston, 24 August 1731; named in her father's will. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></td></tr>
    <tr><td>Benjamin Gurney</td><td>c. 1704 – before 1771</td><td>G10 in the direct line. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></td></tr>
  </tbody>
```

### A7-4 — Narrative (all three paragraphs)

`str_replace`

old_string:
```
<p>Benjamin Gurney G11 lived his life within the working farms of the Abington–Bridgewater corridor of Plymouth County. He was born around 1676 at Weymouth, the son of Richard Gurney (G12) and Rebecca Taylor, and on 30 December 1701 he married Rebecca Staples at the First Church of Braintree — a marriage record that places him squarely in the Massachusetts Bay congregational record system.</p>

<p>His traceable property dealings are concrete and small in scale. On 8 September 1726 he bought the Richard Williams farm on the Abington–Bridgewater line from Samuel Staples of Scituate (Plymouth Deeds 25:79). When he moved to Middleboro in 1730, he sold that farm to Abraham Pierce on 20 October (Plymouth Registry 31:69, 70). His father-in-law (or kinsman) Joseph Richards had earlier bequeathed land to him by name. With his son Benjamin (G10) he jointly bought Samuel Tinkham's Middleboro land on 28 October 1730 — an indirect record of the household's continued working partnership into the next generation.</p>

<p>The most distinctive single trace of the household is "Granny Gurney's Swamp," a low ground near the Abington–Bridgewater line named for the family after a fire incident involving Rebecca Staples. The naming is preserved in two independent local-history accounts. It is the kind of small, unverifiable, but persistent name that ties a family memorably to a stretch of land — a kind of memorial that survives even when the actual deeds and probates have eroded away. Benjamin's will, proved at Plymouth in 1739 (Plymouth Probate 8:98), is the formal close of the record.</p>
```
new_string:
```
<p>Benjamin Gurney G11 lived his life among the working farms of the Abington–Bridgewater corridor of Plymouth County. He was born around 1676 at Weymouth, the son of Richard Gurney (G12) and Rebecca Taylor, and on 30 December 1701 he married Rebecca Staples — born 1682, daughter of John and Sarah (Atkins) Staples — at the First Church of Braintree, the Rev. Moses Fiske officiating. As a young married man he moved to South Abington around 1707, lodging for a time with his cousin Samuel Gurney, who had married Rebecca's widowed mother; he slipped back to Weymouth about 1710 and then settled for good on the Abington side.</p>

<p>His traceable property dealings are concrete and small in scale. On 8 September 1726 he bought the Richard Williams farm on the Abington–Bridgewater line from Samuel Staples of Scituate — his wife's brother, so a transfer kept within the family (Plymouth Deeds 25:79). When he moved to Middleboro in 1730 he sold that farm to Abraham Pierce on 20 October (Plymouth Registry 31:69, 70). He also held a parcel he had bought from Joseph Richards, which his will would pass to his son Benjamin. With that son, Benjamin (G10), he jointly bought Samuel Tinkham's Middleboro land on 28 October 1730 — a glimpse of the household's working partnership carrying into the next generation.</p>

<p>The most distinctive single trace of the household is "Granny Gurney's Swamp," a stretch of low ground near the Abington–Bridgewater line that took the family's name from a moment in Rebecca's life. The local historian Cyrus Nash preserved the story: Rebecca went out to find Benjamin, who had not come home when he was expected, and discovered him asleep in a field; exasperated, she tipped the lit pipe from her mouth into the dry grass to startle him awake, and the fire ran away from her, burning over many acres of low ground that was known ever after as Granny Gurney's Swamp. It is the kind of small, unverifiable, but persistent name that ties a family to a stretch of land long after the deeds and probates have eroded away. Benjamin's will — dated 4 May 1738 and proved at Plymouth in 1739 (Plymouth Probate 8:98) — is the formal close of the record.</p>
```

### A7-5 — Citations list (full replace; removes data-file references)

`str_replace`

old_string:
```
<ol class="citation-list">
  <li id="n1">Born c. 1676, Weymouth, Massachusetts. Parentage from <code>data/ancestors v26.json</code>, G11 entry. <a class="citation-back" href="#ref-1">↩</a></li>
  <li id="n2">Will proved 1739, Plymouth Probate 8:98. <code>data/ancestors v26.json</code>, G11 entry. <a class="citation-back" href="#ref-2">↩</a></li>
  <li id="n3">Plymouth Deeds 25:79 (Richard Williams farm purchase from Samuel Staples, 8 September 1726); Plymouth Registry 31:69, 70 (sale to Abraham Pierce, 20 October 1730); Joseph Richards's bequest to Benjamin (cited in <code>data/ancestors v26.json</code>, G11 entry). <a class="citation-back" href="#ref-3">↩</a></li>
  <li id="n4">Marriage 30 December 1701, First Church Braintree, Massachusetts. <code>data/ancestors v26.json</code>, G11 entry. <a class="citation-back" href="#ref-4">↩</a></li>
  <li id="n5">"Granny Gurney's Swamp" — story confirmed independently per <code>data/ancestors v26.json</code>, G11 entry. <a class="citation-back" href="#ref-5">↩</a></li>
  <li id="n6">See <a href="/fact-sheets/g10-benjamin-gurney-fact-sheet.html">Benjamin Gurney (G10) fact sheet</a>. <a class="citation-back" href="#ref-6">↩</a></li>
</ol>
```
new_string:
```
<ol class="citation-list">
  <li id="n1">Born c. 1676, probably at Weymouth, Massachusetts, son of Richard Gurney (G12) and Rebecca Taylor. Jean Gurney Rigler, <em>The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary</em>, rev. ed. (Honolulu: J. G. Rigler, 1994), Benjamin-3 (Richard-2) entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-1">↩</a></li>
  <li id="n2">Will dated 4 May 1738, proved 1739, Plymouth County Probate 8:98, leaving wife Rebeckah the use of the homestead, son Benjamin the parcel bought of Joseph Richards, and forty pounds to daughter Rebecca, wife of Daniel Taylor; quoted in Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-3 entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-2">↩</a></li>
  <li id="n3">Plymouth County Deeds 25:79 (Richard Williams farm bought from Samuel Staples of Scituate — Rebecca's brother — 8 September 1726); Plymouth Registry 31:69, 70 (sale to Abraham Pierce, 20 October 1730); Plymouth Registry 39:79 (Samuel Tinkham land bought jointly with son Benjamin, 28 October 1730); and the parcel bought of Joseph Richards passed to son Benjamin by the 1738 will — all as compiled in Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-3 entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-3">↩</a></li>
  <li id="n4">Married 30 December 1701 at the First Church of Braintree, Massachusetts, by the Rev. Moses Fiske, to Rebecca Staples (b. 1682, daughter of John and Sarah (Atkins) Staples). Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-3 entry (citing NEHGR 59:155, 116:20, 121:244). Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-4">↩</a></li>
  <li id="n5">"Granny Gurney's Swamp," as recounted by the local historian Cyrus Nash and quoted in Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-3 entry: Rebecca found Benjamin "lying asleep in a field" and "set fire to the grass around him to give him a good scare," starting a fire that "burn[ed] over many acres of low ground, which thereafter was known as Granny Gurney's Swamp." Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-5">↩</a></li>
  <li id="n6">See the <a href="/fact-sheets/g10-benjamin-gurney-fact-sheet.html">Benjamin Gurney (G10) fact sheet</a>. <a class="citation-back" href="#ref-6">↩</a></li>
  <li id="n7">Daughter Rebecca Gurney, b. 22 November 1702, married Daniel Taylor of Kingston on 24 August 1731 (Kingston, Massachusetts, vital records) and is named in her father's 1738 will; Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-3 entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-7">↩</a></li>
</ol>
```

### A7-6 — Timeline: add the c. 1707 Abington move row

`str_replace`

old_string:
```
      <tr><td>1701</td><td>Married Rebecca Staples, 30 December, First Church Braintree.</td></tr>
      <tr><td>1726</td><td>Bought the Richard Williams farm on the Abington–Bridgewater line (Plymouth Deeds 25:79).</td></tr>
```
new_string:
```
      <tr><td>1701</td><td>Married Rebecca Staples, 30 December, First Church Braintree.</td></tr>
      <tr><td>c. 1707</td><td>Moved to South Abington, living for a time with his cousin Samuel Gurney.</td></tr>
      <tr><td>1726</td><td>Bought the Richard Williams farm on the Abington–Bridgewater line (Plymouth Deeds 25:79).</td></tr>
```

### A7-7 — Timeline: will-date row

`str_replace`

old_string:
```
      <tr><td>1738/9</td><td>Died; will proved 1739 (Plymouth Probate 8:98).</td></tr>
```
new_string:
```
      <tr><td>1738/9</td><td>Will dated 4 May 1738; died; will proved 1739 (Plymouth Probate 8:98).</td></tr>
```

---

## A8 — G10 research companion — `research/people/g10-benjamin-gurney-fact-sheet.research.md`

### A8-1 — insert a Rigler findings section above Sources consulted

`str_replace`

old_string:
```
## Sources consulted
```
new_string:
```
## Rigler (1994) findings — direct page audit

Rigler's Benjamin-4 (Benjamin-3, Richard-2) entry, transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md), adds a second compiled-genealogy witness and several parentage facts.

**Independent confirmation of the paternity.** Rigler states Benjamin G10 "became enamoured of Jane (Jean) Harden & apparently fathered her son, Benjamin who was bpt. 30 May 1730 in Abington" — a second compiled genealogy, drawn from the Anna Gurney papers and Abington records, agreeing with *The Neverending Hobby*. Neither names the father from the baptism itself, so the careful phrasing stands; but the identification now rests on two independent compiled sources rather than one.[^rigler-g10]

**Jane (Jean) Harden's parentage.** Daughter of Capt. John and Mary (Littlefield) Harden, b. 19 Nov. 1709 Abington, bpt. 1711 Braintree; she married Ebenezer Spear on 29 Dec. 1731. (Mary Littlefield is the mother-name not previously held here.) The Harden home stood near the "Little Comfort Mill," which John Gurney-3 — Richard-2's son — had started.[^rigler-g10]

**Sarah Morse's parentage.** Daughter of Jonathan and Anna (Barden) Morse Jr., b. 7 Feb. 1711/12; married 14 June 1731 by Rev. Benjamin Ruggles.[^rigler-g10]

**Death before 13 Dec. 1771.** Sharper than the prior "before December 1772": Rigler dates it from his son Lemuel's mortgage of "a certain tract in Rochester… it being the estate of my father, Benjamin Gurney, late of Rochester" (Plym. Reg. 57:47).[^rigler-g10]

**The second Benjamin — resolved.** The Sarah Morse son Benjamin (b. c. 1743–45) married Thankful Ellis (bpt. 26 July 1761, d/o Mathias and Rachel (Tupper) Ellis) on 23 Aug. 1781; he was a Revolutionary War private (DAR Patriot Index 1:291; pension W-14837), a Rochester yeoman, wrote his will 16 Dec. 1826 (proved 11 Aug. 1828, Plym. Prob. 66:215), and died 4 July 1828 in his 85th year. He is the Benjamin in the 1800 Rochester homestead division — definitively not G9. The full Sarah Morse child set per Rigler: Susannah, Grace, Lemuel, Benjamin, Levi, and (uncertain) Sarah and Jemima.[^rigler-g10]

Minor variant to flag for the eventual deed check: Rigler's Benjamin-4 entry dates the joint Samuel Tinkham purchase "26 Oct. 1730," while her Benjamin-3 entry gives "28 Oct. 1730" (Plym. Reg. 39:79); the project keeps 28 October pending the deed.

[^rigler-g10]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary*, rev. ed. (Honolulu: J. G. Rigler, 1994), Benjamin-4 (Benjamin-3, Richard-2) entry (pp. 19–21), with the adjacent "second Benjamin" (Sarah Morse son) entry (pp. 21–22). Transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.

---

## Sources consulted
```

### A8-2 — resolve open question 5

`str_replace`

old_string:
```
5. **Second Benjamin's life course.** The later Benjamin likely fits some later Middleborough/Rochester records, possibly including the 1781 Thankfull Ellis marriage, but this requires direct disambiguation.
```
new_string:
```
5. **Second Benjamin's life course — largely resolved.** Rigler carries the later Benjamin (b. c. 1743–45) marrying Thankful Ellis on 23 Aug. 1781, his Revolutionary War service, and his 1828 Rochester will (Plym. Prob. 66:215). The 1781 Thankful Ellis marriage belongs to him, not G9. Remaining work is only deed-level confirmation of which same-name records are his.
```

### A8-3 — fix the data-file reference in the Rochester-deed footnote

`str_replace`

old_string:
```
[^rochester-deed]: Plymouth County land deed 95:139, GS film 559,140, Rochester homestead farm divided among Lemuel, Benjamin, and Levi Gurney, 1 January 1800; currently cited through `data/ancestors v26.json`, G10 entry. Direct image still needed before finalizing all relationship language.
```
new_string:
```
[^rochester-deed]: Plymouth County land deed 95:139, GS film 559,140, Rochester homestead farm divided among Lemuel, Benjamin, and Levi Gurney, 1 January 1800; compiled in Rigler, *Gurney Family from Aaron to Zuinglius* (1994), Benjamin-4 entry. Source ID: `rigler-gurney-family-aaron-zuinglius-1994`. Direct deed image still needed before finalizing all relationship language.
```

### A8-4 — replace the stale "audit pending" Rigler line in Sources consulted

`str_replace`

old_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994). Key compiled genealogy for the G4-G13 direct line; source ID `rigler-gurney-family-aaron-zuinglius-1994`. Full page-level audit still pending.
```
new_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994), Benjamin-4 entry (pp. 19–21); audited — see the Rigler findings section above. Source ID `rigler-gurney-family-aaron-zuinglius-1994`. Transcribed extract at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md).
```

---

## A9 — G10 fact sheet — `fact-sheets/g10-benjamin-gurney-fact-sheet.md`

### A9-1 — Died vital cell

`str_replace`

old_string:
```
    <div class="fact-value">Before December 1772, at Rochester, Plymouth County, Massachusetts. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```
new_string:
```
    <div class="fact-value">Before 13 December 1771, at Rochester, Plymouth County, Massachusetts. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
```

### A9-2 — Marriage / Liaisons vital cell

`str_replace`

old_string:
```
        <div><strong>Jane / Jean Harden</strong> &mdash; likely non-marital liaison prior to marriage; best-supported mother of Benjamin (G9). The Abington baptism names Benjamin as son of Jean but does not name the father; John Harden's will confirms Benjamin as Harden grandson. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup><sup class="fn"><a href="#n8" id="ref-8">8</a></sup></div>
        <div><strong>Sarah Morse</strong> &mdash; married 14 June 1731, Middleborough, Massachusetts, per marriage index. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```
new_string:
```
        <div><strong>Jane / Jean Harden</strong> &mdash; daughter of Capt. John and Mary (Littlefield) Harden; a liaison before marriage and the best-supported mother of Benjamin (G9). The Abington baptism names Benjamin as son of Jean but not the father; John Harden's will confirms Benjamin as his grandson. Jane later married Ebenezer Spear in 1731. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup><sup class="fn"><a href="#n8" id="ref-8">8</a></sup></div>
        <div><strong>Sarah Morse</strong> &mdash; daughter of Jonathan and Anna (Barden) Morse; married 14 June 1731 at Middleborough, Massachusetts, by the Rev. Benjamin Ruggles. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```

### A9-3 — Highlights: father bullet and corridor bullet

`str_replace`

old_string:
```
  <li><strong>Likely father of Benjamin (G9) through Jane/Jean Harden.</strong> Secondary compiled genealogy identifies G10 as the father of Benjamin (G9), baptized at Abington in 1730 as Benjamin, son of Jean. The primary baptism does not name the father, so this should be treated as a strong compiled-genealogy identification supported by the Harden-side record chain, not as a direct baptismal statement. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></li>
```
new_string:
```
  <li><strong>Father of Benjamin (G9) through Jane/Jean Harden.</strong> Two independent compiled genealogies — Rigler's and <em>The Neverending Hobby</em>'s — name G10 as the father of Benjamin (G9), baptized at Abington in 1730 as Benjamin, son of Jean, through a liaison before his marriage. The baptism names only the mother, so the paternity rests on the compiled genealogies and the Harden-side record chain rather than on a direct baptismal statement. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></li>
```

`str_replace`

old_string:
```
  <li><strong>Moved from the Bridgewater–Abington corridor into the Middleboro–Rochester corridor.</strong> The traceable arc of his life runs from a Weymouth birth, through the Abington–Whitman area in early adulthood, into Middleboro from 1730–31, and finally to Rochester, where he died before December 1772. <sup class="fn"><a href="#n2" id="ref-2b">2</a></sup></li>
```
new_string:
```
  <li><strong>Moved from the Bridgewater–Abington corridor into the Middleboro–Rochester corridor.</strong> The traceable arc of his life runs from a Weymouth birth, through the Abington–Whitman area in early adulthood, into Middleboro from 1730–31, and finally to Rochester, where he died before 13 December 1771. <sup class="fn"><a href="#n2" id="ref-2b">2</a></sup></li>
```

### A9-4 — Children table

`str_replace`

old_string:
```
    <tr><td>Benjamin Gurney</td><td>bpt. 30 May 1730 &ndash; d. 28 Sept. 1805</td><td>Jane / Jean Harden</td><td>G9 in direct line; baptized as Benjamin, son of Jean; later confirmed as John Harden's grandson. Father identification rests on secondary compiled genealogy and the broader evidence chain. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup><sup class="fn"><a href="#n8" id="ref-8d">8</a></sup></td></tr>
    <tr><td>Lemuel Gurney</td><td></td><td>Sarah Morse</td><td>With his brothers, divided the Rochester homestead farm 1 January 1800. <sup class="fn"><a href="#n6" id="ref-6b">6</a></sup></td></tr>
    <tr><td>Benjamin Gurney</td><td>b. c. 1743</td><td>Sarah Morse</td><td>Later same-name half-brother; likely distinct from G9 and relevant to the Rochester homestead / two-Benjamin disambiguation problem. <sup class="fn"><a href="#n4" id="ref-4d">4</a></sup></td></tr>
    <tr><td>Levi Gurney</td><td></td><td>Sarah Morse</td><td>With his brothers, divided the Rochester homestead farm 1 January 1800. <sup class="fn"><a href="#n6" id="ref-6c">6</a></sup></td></tr>
```
new_string:
```
    <tr><td>Benjamin Gurney</td><td>bpt. 30 May 1730 &ndash; d. 28 Sept. 1805</td><td>Jane / Jean Harden</td><td>G9 in the direct line; baptized as Benjamin, son of Jean; confirmed as John Harden's grandson. Father identification rests on the compiled genealogies and the broader evidence chain. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup><sup class="fn"><a href="#n8" id="ref-8d">8</a></sup></td></tr>
    <tr><td>Susannah Gurney</td><td></td><td>Sarah Morse</td><td>Married Jabez Benson of Wareham, 26 July 1752. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></td></tr>
    <tr><td>Lemuel Gurney</td><td>c. 1738</td><td>Sarah Morse</td><td>Married Elizabeth Wrightington; with his brothers, divided the Rochester homestead farm 1 January 1800. <sup class="fn"><a href="#n6" id="ref-6b">6</a></sup></td></tr>
    <tr><td>Benjamin Gurney</td><td>c. 1743–45 &ndash; 1828</td><td>Sarah Morse</td><td>Later same-name half-brother; married Thankful Ellis and served as a Revolutionary War private; the Benjamin in the Rochester homestead division, distinct from G9. <sup class="fn"><a href="#n4" id="ref-4d">4</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup></td></tr>
    <tr><td>Levi Gurney</td><td>c. 1746</td><td>Sarah Morse</td><td>Married Mary, then Rebecca, Hathaway; with his brothers, divided the Rochester homestead farm 1 January 1800. <sup class="fn"><a href="#n6" id="ref-6c">6</a></sup></td></tr>
```

### A9-5 — two-Benjamin note paragraph

`str_replace`

old_string:
```
<p><em>The family has a two-Benjamin problem. Benjamin G9, baptized in 1730 as son of Jean/Jane Harden, is distinct from the later Benjamin in the Sarah Morse child set who appears to fit the Rochester homestead division and later Middleborough/Rochester records. <sup class="fn"><a href="#n4" id="ref-4e">4</a></sup><sup class="fn"><a href="#n6" id="ref-6d">6</a></sup><sup class="fn"><a href="#n8" id="ref-8e">8</a></sup></em></p>
```
new_string:
```
<p><em>The family has a two-Benjamin problem. Benjamin (G9), baptized in 1730 as son of Jean/Jane Harden and the direct-line ancestor, is distinct from the later Benjamin in the Sarah Morse child set — born about 1743–45, married Thankful Ellis, a Revolutionary War private who lived out his life at Rochester (died 1828) — who fits the 1800 homestead division and the later Middleborough/Rochester records. <sup class="fn"><a href="#n4" id="ref-4e">4</a></sup><sup class="fn"><a href="#n6" id="ref-6d">6</a></sup><sup class="fn"><a href="#n9" id="ref-9c">9</a></sup></em></p>
```

### A9-6 — Narrative paragraph 1 (remove discovery-sequence framing)

`str_replace`

old_string:
```
<p>Benjamin Gurney G10 lived his entire life within the working farms and small towns of eastern Plymouth County, Massachusetts. He was born around 1704 at Weymouth, into the household of his father Benjamin G11 and Rebecca Staples; he reached adulthood in the Abington&ndash;Whitman line area, where the family had held land since the previous generation. The difficult opening event of his adult life should now be stated with sharper evidence discipline: secondary compiled genealogy identifies him as the father of Benjamin (G9), who was baptized at Abington on 30 May 1730 as Benjamin, son of Jean. The newly located John Harden will confirms that the child later known as Benjamin Gurney was John Harden's grandson and makes Jane/Jean Harden Spear the best-supported mother, but neither the baptism nor the will directly names G10 as father. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n4" id="ref-4c">4</a></sup><sup class="fn"><a href="#n8" id="ref-8c">8</a></sup></p>
```
new_string:
```
<p>Benjamin Gurney G10 lived his entire life among the working farms and small towns of eastern Plymouth County, Massachusetts. He was born around 1704 at Weymouth, into the household of his father Benjamin (G11) and Rebecca Staples, and grew up in the Abington–Whitman area where the family had held land since the previous generation. Two independent compiled genealogies — Jean Gurney Rigler's and the public <em>Neverending Hobby</em> — identify him as the father of Benjamin (G9), who was baptized at Abington on 30 May 1730 as Benjamin, son of Jean, through a liaison with Jane (Jean) Harden before his own marriage. John Harden's 1751 will confirms that this child was John Harden's grandson, which makes Jane/Jean Harden the best-supported mother; neither the baptism nor the will, however, names the father outright, so the paternity rests on the compiled genealogies and the surrounding record chain. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n4" id="ref-4c">4</a></sup><sup class="fn"><a href="#n8" id="ref-8c">8</a></sup></p>
```

### A9-7 — Narrative paragraph 2 (Sarah Morse parentage; death year)

`str_replace`

old_string:
```
<p>His married life with Sarah Morse from 1731 onward generated a family group that Plymouth County deeds preserve in fragments. With his father he bought Middleboro land from Samuel Tinkham on 28 October 1730 (Plymouth Registry 39:79) — three lots of upland and a small meadow lot of about two acres — and sold it on 3 May 1749 after his father's death. He purchased eight further acres at Middleboro from Samuel Eddy Jr. on 7 November 1731, presumably the family's working farm in that town. By the latter part of his life he had moved on to Rochester, where he died before December 1772.</p>
```
new_string:
```
<p>His married life with Sarah Morse — daughter of Jonathan and Anna (Barden) Morse, whom he married at Middleboro on 14 June 1731 — generated a family group that Plymouth County deeds preserve in fragments. With his father he bought Middleboro land from Samuel Tinkham on 28 October 1730 (Plymouth Registry 39:79) — three lots of upland and a small meadow lot of about two acres — and sold it on 3 May 1749 after his father's death. He bought eight further acres at Middleboro from Samuel Eddy Jr. on 7 November 1731, presumably the family's working farm in that town, and subscribed to the church in what is now Carver. By the latter part of his life he had moved on to Rochester, where he died before 13 December 1771.</p>
```

### A9-8 — Narrative paragraph 3 (Lemuel mortgage; second-Benjamin clarity)

`str_replace`

old_string:
```
<p>The fullest after-death record is a 1 January 1800 land deed (Plymouth County 95:139) by which his sons Lemuel, Benjamin, and Levi divided the Rochester homestead. It is from this deed that his sons by Sarah Morse are known. The deed also implies that Benjamin (G9) — the son by Jane Harden — was treated as a separate descent: by 1800 G9 was already established in Cummington, having sold his own Abington land in 1770 and purchased into Town No. 5 the same year. The split between the Plymouth County and Hampshire County branches of his children's families therefore traces back to Benjamin G10's two relationships, with the Cummington / New York / Indiana line in this project descending exclusively from the earlier liaison with Jane Harden.</p>
```
new_string:
```
<p>The fullest after-death records are his son Lemuel's 1771 mortgage of "a certain tract in Rochester… it being the estate of my father, Benjamin Gurney, late of Rochester" (Plymouth Registry 57:47), and the 1 January 1800 deed (Plymouth County 95:139) by which sons Lemuel, Benjamin, and Levi divided the Rochester homestead. It is from these that his sons by Sarah Morse are known. The Benjamin in that division was the later son by Sarah Morse — not Benjamin (G9), who by 1800 was long established in Cummington, having sold his Abington land and bought into Town No. 5 in 1770. The split between the Plymouth County and Hampshire County branches of the family therefore traces back to Benjamin G10's two relationships, with the Cummington, New York, and Indiana line descending exclusively from the earlier liaison with Jane Harden.</p>
```

### A9-9 — Citations: replace data-file references and add Rigler; add note n9

`str_replace`

old_string:
```
  <li id="n1">Birth c. 1704 at Weymouth, parentage from <code>data/ancestors v26.json</code>, G10 entry. <a class="citation-back" href="#ref-1">↩</a></li>
  <li id="n2">"Died before December 1772" inferred from absence in subsequent Plymouth County records. <code>data/ancestors v26.json</code>, G10 entry. <a class="citation-back" href="#ref-2">↩</a></li>
  <li id="n3">Plymouth Registry 39:79 (Tinkham purchase, 28 October 1730; sold 3 May 1749); Plymouth Registry, 7 November 1731 (Eddy purchase, 8 acres Middleboro); Plymouth County land deed 95:139 (Rochester homestead division, 1 January 1800), GS film 559,140. Cited in <code>data/ancestors v26.json</code>, G10 entry. <a class="citation-back" href="#ref-3">↩</a></li>
  <li id="n4"><a href="https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636">"John Gurney, US 1636,"</a> <em>The Neverending Hobby</em>, public compiled genealogy. Use as secondary compiled genealogy for the G10 / Jane Harden relationship, G10's identification as father of Benjamin G9, the Sarah Morse child set, and the later same-name Benjamin. Source ID: <code>neverending-hobby-john-gurney-us-1636</code>. <a class="citation-back" href="#ref-4">&#8617;</a></li>
  <li id="n5">Middleborough Public Library, "Marriages by Men's Name," marriage index PDF, entry for Benjamin Gurney and Sarah Morse, 14 June 1731; <a href="https://midlib.org/sites/midlib.org/files/images/marriages%20by%20mens%20name.pdf">marriage index PDF</a>. Source ID: <code>middleborough-marriages-by-mens-name</code>. <a class="citation-back" href="#ref-5">&#8617;</a></li>
  <li id="n6">Plymouth County land deed 95:139, GS film 559,140 — Rochester homestead farm divided among sons Lemuel, Benjamin, and Levi, 1 January 1800. Cited in <code>data/ancestors v26.json</code>, G10 entry. <a class="citation-back" href="#ref-6">↩</a></li>
```
new_string:
```
  <li id="n1">Born c. 1704 at Weymouth, Massachusetts, son of Benjamin Gurney (G11) and Rebecca Staples. Jean Gurney Rigler, <em>The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary</em>, rev. ed. (Honolulu: J. G. Rigler, 1994), Benjamin-4 (Benjamin-3, Richard-2) entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-1">↩</a></li>
  <li id="n2">Died before 13 December 1771 at Rochester — the date his son Lemuel mortgaged the tract "it being the estate of my father, Benjamin Gurney, late of Rochester" (Plymouth Registry 57:47); Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-4 entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-2">↩</a></li>
  <li id="n3">Plymouth Registry 39:79 (Samuel Tinkham purchase with his father, 28 October 1730; sold 3 May 1749); Plymouth Registry, 7 November 1731 (Samuel Eddy Jr. purchase, 8 acres Middleboro); Plymouth County land deed 95:139 (Rochester homestead division, 1 January 1800), GS film 559,140 — as compiled in Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-4 entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-3">↩</a></li>
  <li id="n4">Two independent compiled genealogies identify Benjamin Gurney G10 as the father of Benjamin G9 through Jane (Jean) Harden: Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-4 entry, which states he "became enamoured of Jane (Jean) Harden &amp; apparently fathered her son, Benjamin," and <a href="https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636">"John Gurney, US 1636,"</a> <em>The Neverending Hobby</em>. Both also carry the Sarah Morse child set and the later same-name Benjamin; the Abington baptism itself names only the mother, Jean. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>neverending-hobby-john-gurney-us-1636</code>. <a class="citation-back" href="#ref-4">&#8617;</a></li>
  <li id="n5">Married 14 June 1731 at Middleborough, Massachusetts, by the Rev. Benjamin Ruggles, to Sarah Morse (b. 7 February 1711/12, daughter of Jonathan and Anna (Barden) Morse); Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-4 entry, with the Middleborough Public Library <a href="https://midlib.org/sites/midlib.org/files/images/marriages%20by%20mens%20name.pdf">"Marriages by Men's Name"</a> index also recording the 14 June 1731 date. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>middleborough-marriages-by-mens-name</code>. <a class="citation-back" href="#ref-5">&#8617;</a></li>
  <li id="n6">Rochester homestead farm divided among sons Lemuel, Benjamin, and Levi, 1 January 1800; Plymouth County land deed 95:139, GS film 559,140, as compiled in Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-4 entry. Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-6">↩</a></li>
```

`str_replace`

old_string:
```
  <li id="n8">Massachusetts. Probate Court (Plymouth County), <em>Probate records, 1686&ndash;1903; with index and docket, 1685&ndash;1967</em>, Plymouth County Probate Court record book, manuscript pp. 383&ndash;384, will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751; <a href="https://www.familysearch.org/en/search/catalog/277512">FamilySearch catalog</a>; <a href="https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW">p. 383 image</a>; <a href="https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF">p. 384 image</a>. The will confirms Benjamin Gurney as John Harden's grandson and names daughter Jane Spear; it does not name Benjamin Gurney G10 as father. Source ID: <code>plymouth-probate-john-harden-1751-will</code>. <a class="citation-back" href="#ref-8">&#8617;</a></li>
</ol>
```
new_string:
```
  <li id="n8">Massachusetts. Probate Court (Plymouth County), <em>Probate records, 1686&ndash;1903; with index and docket, 1685&ndash;1967</em>, Plymouth County Probate Court record book, manuscript pp. 383&ndash;384 (Plym. Prob. 12:383), will of John Harden of Bridgewater, Plymouth County, Massachusetts, blacksmith, dated 17 September 1751, proved 7 October 1751; <a href="https://www.familysearch.org/en/search/catalog/277512">FamilySearch catalog</a>; <a href="https://www.familysearch.org/ark:/61903/3:1:3QSQ-G97D-F6PW">p. 383 image</a>; <a href="https://www.familysearch.org/ark:/61903/3:1:3QS7-897D-FXDF">p. 384 image</a>. The will confirms Benjamin Gurney as John Harden's grandson and names daughter Jane Spear; it does not name Benjamin Gurney G10 as father. Source ID: <code>plymouth-probate-john-harden-1751-will</code>. <a class="citation-back" href="#ref-8">&#8617;</a></li>
  <li id="n9">Children of Benjamin Gurney G10 by Sarah Morse, and the later "second Benjamin," from Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-4 entry: Susannah (married Jabez Benson of Wareham, 26 July 1752), Lemuel (married Elizabeth Wrightington), Benjamin (b. c. 1743&ndash;45, married Thankful Ellis; a Revolutionary War private; d. 1828, will Plymouth Probate 66:215), and Levi (married Mary, then Rebecca, Hathaway). Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-9">&#8617;</a></li>
</ol>
```

### A9-10 — Timeline: death-year row

`str_replace`

old_string:
```
      <tr><td>before 1772</td><td>Died at Rochester, Plymouth County.</td></tr>
```
new_string:
```
      <tr><td>1771</td><td>Died at Rochester before 13 December (revealed by son Lemuel's mortgage of the estate).</td></tr>
```

---

## A10 — G9 research companion — `research/people/g09-benjamin-gurney-fact-sheet.research.md`

### A10-1 — insert a Rigler findings section above Sources consulted

`str_replace`

old_string:
```
## Sources consulted
```
new_string:
```
## Rigler (1994) findings — direct page audit

Rigler's Benjamin-5 (Benjamin-4,3, Richard-2) entry, transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md), corroborates the aunt-upbringing and supplies the marriages, the full child set, and several life details.

**Aunt-upbringing corroborated by name.** "He was raised in Abington by Nathan-4 & Sarah (Harden) Gurney, his mother's sister." This is the same Sarah Harden Gurney this companion already identified as the strongest aunt-household candidate (b. 9 Apr. 1707; m. Nathan Gurney; "daughter Sarah Gurney" in John Harden's 1751 will). The tradition that Benjamin was raised by a maternal aunt now has a direct compiled-genealogy statement and a named household.[^rigler-g9]

**Marriages.** First, 1 Jan. 1752 at Abington, Elizabeth Harden (b. c. 1730, d/o Samuel Harden), who died 30 July 1800 in her 70th year at Cummington, bur. Dawes Cem. Second, 17 Nov. 1800 at Cummington, Mercy Noyes (b. c. 1740/41), d. 28 Mar. 1813, bur. Dawes Cem. Note that G9's wife Elizabeth Harden, daughter of Samuel Harden, is a different Elizabeth from the witness in John Harden's will — the name recurs in the Harden family and should not be conflated.[^rigler-g9]

**Children (by Elizabeth Harden).** Benjamin (b. 25 Aug. 1752 Bridgewater, d. 1804 Cummington, m. Esther Cole 1802; one daughter Clarissa, 1803–1813); Betty "Betsey" (b. 15 Nov. 1756, d. 12 May 1805 Cummington); Asa (b. 24 Oct. 1758, m. Molly Reed); Jane; and Amos (m. Ruth Gilbert) — G8.[^rigler-g9]

**Residence and the Cummington move.** Benjamin lived at Northville, a small community between East Bridgewater and present Whitman. About June 1770 he sold his Abington land; Springfield records show he and Silas Reed bought land in Town No. 5 on 5 Nov. 1770, where the deed described him as "yeoman of Town # 5, formerly of Bridgewater." In 1787 he and Philip Shaw exchanged farms (Foster & Streeter, *Only One Cummington*, p. 390; *Hampshire Co. MA Biographies*, 1896, p. 196). The 1790 census gives 3-0-3.[^rigler-g9]

**Death.** Died 28 Sept. 1805 in his 76th year, bur. Dawes Cem., Cummington.[^rigler-g9]

[^rigler-g9]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary*, rev. ed. (Honolulu: J. G. Rigler, 1994), Benjamin-5 (Benjamin-4,3, Richard-2) entry (pp. 21–22). Transcribed at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.

---

## Sources consulted
```

### A10-2 — resolve open questions 1 and 5

`str_replace`

old_string:
```
1. **Direct aunt-household proof.** Search guardianship, church, deed, probate-distribution, and loose estate-file records for evidence that Sarah Harden Gurney, Mary Harden Hobart, or another aunt raised Benjamin.
```
new_string:
```
1. **Aunt-household — corroborated, not yet proved at primary level.** Rigler states directly that Benjamin "was raised in Abington by Nathan & Sarah (Harden) Gurney, his mother's sister," naming the household and matching the reconstruction here. A primary guardianship, church, or estate-distribution record would still upgrade it from compiled-genealogy statement to documented fact. (Unknown online.)
```

`str_replace`

old_string:
```
5. **G9 marriage records.** Elizabeth Harden and Mercy Noyes remain underdocumented in this companion.
```
new_string:
```
5. **G9 marriage records — dates recovered.** Rigler gives Elizabeth Harden (m. 1 Jan. 1752 Abington, daughter of Samuel Harden) and Mercy Noyes (m. 17 Nov. 1800 Cummington). The original Abington and Cummington marriage registers would confirm the compiled dates. (Unknown online.)
```

### A10-3 — replace the stale "audit pending" Rigler line in Sources consulted

`str_replace`

old_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994). Key compiled genealogy for the G4-G13 direct line; source ID `rigler-gurney-family-aaron-zuinglius-1994`. Full page-level audit still pending.
```
new_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994), Benjamin-5 entry (pp. 21–22); audited — see the Rigler findings section above. Source ID `rigler-gurney-family-aaron-zuinglius-1994`. Transcribed extract at [`sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-gurney-aaron-zuinglius-g9-g12-extract.md).
```

---

## A11 — G9 fact sheet — `fact-sheets/g09-benjamin-gurney-fact-sheet.md`

### A11-1 — subtitle: aunt named

`str_replace`

old_string:
```
subtitle: "Plymouth County farmer born of an unmarried liaison and reportedly raised by his maternal aunt; sold Abington land in 1770 and bought into Cummington with Silas Reed."
```
new_string:
```
subtitle: "Plymouth County farmer born of an unmarried liaison and raised by his maternal aunt, Sarah Harden Gurney; sold Abington land in 1770 and bought into Cummington with Silas Reed."
```

### A11-2 — Marriage(s) vital cell

`str_replace`

old_string:
```
        <div><strong>Elizabeth Harden</strong> — first wife. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
        <div><strong>Mercy Noyes</strong> — second wife. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></div>
```
new_string:
```
        <div><strong>Elizabeth "Betsey" Harden</strong> — daughter of Samuel Harden; married 1 January 1752 at Abington; died 30 July 1800 at Cummington. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
        <div><strong>Mercy Noyes</strong> — married 17 November 1800 at Cummington; died 28 March 1813. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></div>
```

### A11-3 — Highlights: aunt-upbringing bullet upgraded

`str_replace`

old_string:
```
  <li><strong>The aunt-upbringing tradition is plausible but not proved.</strong> Family tradition says Benjamin was raised by his mother's sister. The will confirms the Harden kinship but does not name a guardian or caregiver. Sarah Harden Gurney, a Harden daughter who married into the Gurney family, is the strongest aunt-household candidate, but no direct guardianship or household record has yet been found. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```
new_string:
```
  <li><strong>Raised by his maternal aunt, Sarah Harden Gurney.</strong> Born of an unmarried liaison, Benjamin was brought up in Abington by his mother's sister Sarah and her husband Nathan Gurney — keeping the boy within his father's Gurney kin as well as his mother's. Sarah, a daughter of John Harden, had married into the Gurney family a few years before Benjamin's birth. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup></li>
```

### A11-4 — Children table

`str_replace`

old_string:
```
  <tbody>
    <tr><td>Amos Gurney</td><td>1770 – before 1850</td><td>G8 in direct line; born around the time of the family's move to Cummington. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></td></tr>
  </tbody>
```
new_string:
```
  <tbody>
    <tr><td>Benjamin Gurney</td><td>1752 – 1804</td><td>Born at Bridgewater; married Esther Cole at Cummington in 1802. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></td></tr>
    <tr><td>Betty "Betsey" Gurney</td><td>1756 – 1805</td><td>Born at Bridgewater; died at Cummington. <sup class="fn"><a href="#n11" id="ref-11b">11</a></sup></td></tr>
    <tr><td>Asa Gurney</td><td>b. 1758</td><td>Born at Bridgewater; married Molly Reed. <sup class="fn"><a href="#n11" id="ref-11c">11</a></sup></td></tr>
    <tr><td>Jane Gurney</td><td></td><td>Named in the family genealogy. <sup class="fn"><a href="#n11" id="ref-11d">11</a></sup></td></tr>
    <tr><td>Amos Gurney</td><td>c. 1770 – before 1850</td><td>G8 in the direct line; married Ruth Gilbert; born around the time of the family's move to Cummington. All five children were by his first wife, Elizabeth Harden. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup><sup class="fn"><a href="#n11" id="ref-11e">11</a></sup></td></tr>
  </tbody>
```

### A11-5 — Narrative paragraph 1 (remove discovery-sequence framing; fold in aunt)

`str_replace`

old_string:
```
<p>Benjamin Gurney is the man who moved the family from old Plymouth County into the Massachusetts hill country. The newly located John Harden will materially strengthens the opening chapter of his life: he was baptized at Abington on 30 May 1730 as Benjamin, son of Jean, and John Harden's 1751 Plymouth County will later named "my grandson Benjamin Gurney." The combined record chain points to Jane/Jean Harden Spear as his likely mother, while Benjamin Gurney G10 remains the father identified by secondary compiled genealogy rather than by the baptismal entry itself. The older Elizabeth-Harden reading should be set aside unless new evidence appears, because Elizabeth Harden is a witness in the will, not a daughter or heir. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup><sup class="fn"><a href="#n10" id="ref-10">10</a></sup></p>
```
new_string:
```
<p>Benjamin Gurney is the man who moved the family from old Plymouth County into the Massachusetts hill country. He was baptized at Abington on 30 May 1730 as Benjamin, son of Jean, and his grandfather John Harden's 1751 Plymouth County will names "my grandson Benjamin Gurney." Read together, the records point to Jane (Jean) Harden as his mother; his father, Benjamin Gurney (G10), is identified by two compiled genealogies rather than by the baptismal entry itself. Born of that unmarried liaison, Benjamin was raised in Abington by his mother's sister Sarah and her husband Nathan Gurney. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup><sup class="fn"><a href="#n9" id="ref-9b">9</a></sup><sup class="fn"><a href="#n10" id="ref-10">10</a></sup></p>
```

### A11-6 — Narrative paragraph 3 (marriages with dates; child set)

`str_replace`

old_string:
```
<p>He married twice — first Elizabeth Harden, then Mercy Noyes — and his son Amos (G8), the bridge to the New York chapter, was born in 1770, almost exactly at the moment of the Cummington move. Benjamin died at Cummington on 28 September 1805 and was buried in Dawes Cemetery, where his marker survives. He is the last firmly-documented Cummington-resident generation in the direct line: his son Amos remained in Cummington only to about 1802, and the family's western Massachusetts chapter effectively ends with Benjamin's death.</p>
```
new_string:
```
<p>He married twice. His first wife, Elizabeth "Betsey" Harden, daughter of Samuel Harden, he married at Abington on 1 January 1752; she bore his five children — Benjamin (1752), Betty (1756), Asa (1758), Jane, and Amos (G8) — and died at Cummington on 30 July 1800. Months later, on 17 November 1800, he married Mercy Noyes. Amos, the bridge to the New York chapter, was born around the time of the 1770 move to Cummington. Benjamin died at Cummington on 28 September 1805, in his seventy-sixth year, and was buried in Dawes Cemetery, where his marker survives; Mercy followed in 1813 and lies beside him. He is the last firmly-documented Cummington-resident generation in the direct line: his son Amos remained in Cummington only to about 1802, and the family's western Massachusetts chapter effectively ends with Benjamin's death.</p>
```

### A11-7 — Citations: n2 and n4 (remove data-file references)

`str_replace`

old_string:
```
  <li id="n2">Death and burial: <code>data/ancestors v26.json</code>, G9 entry (28 September 1805, Cummington; buried Dawes Cemetery). <a class="citation-back" href="#ref-2">↩</a></li>
```
new_string:
```
  <li id="n2">Died 28 September 1805 in his seventy-sixth year and buried in Dawes Cemetery, Cummington, Hampshire County, Massachusetts; his second wife Mercy died 28 March 1813 and was buried beside him. Jean Gurney Rigler, <em>The Gurney Family from Aaron to Zuinglius: A Genealogical Dictionary</em>, rev. ed. (Honolulu: J. G. Rigler, 1994), Benjamin-5 entry (Cummington Town Records). Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-2">↩</a></li>
```

`str_replace`

old_string:
```
  <li id="n4">Two marriages &mdash; to Elizabeth Harden and to Mercy Noyes &mdash; recorded in <code>data/ancestors v26.json</code>, G9 entry; specific dates and marriage records not yet captured here. <a class="citation-back" href="#ref-4">&#8617;</a></li>
```
new_string:
```
  <li id="n4">Married first, on 1 January 1752 at Abington, Elizabeth "Betsey" Harden (b. c. 1730, daughter of Samuel Harden), who died 30 July 1800 at Cummington in her seventieth year; married second, on 17 November 1800 at Cummington, Mercy Noyes (b. c. 1740/41). Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-5 entry (Abington and Cummington records). Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-4">&#8617;</a></li>
```

### A11-8 — Citations: n9 (aunt) gains the direct Rigler statement; add n11 (children)

`str_replace`

old_string:
```
  <li id="n9"><em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1, John and Mary Harden/Hardin family entries for Mary, Sarah, Jean, Rebecca/Rebacka, Lydia, and John; John Harden will, pp. 383&ndash;384, naming daughter Sarah Gurney. Sarah Harden Gurney is a plausible aunt-household candidate, but the current evidence does not prove guardianship or upbringing. Source IDs: <code>abington-vr-1850-vol1</code>; <code>plymouth-probate-john-harden-1751-will</code>. <a class="citation-back" href="#ref-9">&#8617;</a></li>
```
new_string:
```
  <li id="n9">Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-5 entry, records that Benjamin "was raised in Abington by Nathan &amp; Sarah (Harden) Gurney, his mother's sister." Sarah Harden — born 9 April 1707, daughter of John and Mary Harden — married Nathan Gurney and is named "daughter Sarah Gurney" in John Harden's 1751 will. <em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1 (John and Mary Harden family entries); John Harden will, pp. 383&ndash;384. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>; <code>abington-vr-1850-vol1</code>; <code>plymouth-probate-john-harden-1751-will</code>. <a class="citation-back" href="#ref-9">&#8617;</a></li>
```

`str_replace`

old_string:
```
  <li id="n10"><a href="https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636">"John Gurney, US 1636,"</a> <em>The Neverending Hobby</em>, public compiled genealogy. Use as secondary compiled genealogy for the identification of Benjamin Gurney G10 as father through Jane/Jean Harden; the Abington baptism itself does not name the father. Source ID: <code>neverending-hobby-john-gurney-us-1636</code>. <a class="citation-back" href="#ref-10">&#8617;</a></li>
</ol>
```
new_string:
```
  <li id="n10"><a href="https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636">"John Gurney, US 1636,"</a> <em>The Neverending Hobby</em>, public compiled genealogy, identifying Benjamin Gurney G10 as father through Jane/Jean Harden — agreeing with Rigler's compiled account; the Abington baptism itself names only the mother. Source ID: <code>neverending-hobby-john-gurney-us-1636</code>. <a class="citation-back" href="#ref-10">&#8617;</a></li>
  <li id="n11">Children of Benjamin Gurney and Elizabeth Harden, from Rigler, <em>Gurney Family from Aaron to Zuinglius</em>, Benjamin-5 entry (Cummington and Bridgewater records): Benjamin (b. 25 August 1752, Bridgewater; d. 1804, Cummington; m. Esther Cole 1802), Betty "Betsey" (b. 15 November 1756; d. 12 May 1805, Cummington), Asa (b. 24 October 1758; m. Molly Reed), Jane, and Amos (m. Ruth Gilbert). Source ID: <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-11">&#8617;</a></li>
</ol>
```

### A11-9 — Timeline: add 1752 marriage and 1800 rows

`str_replace`

old_string:
```
      <tr><td>1751</td><td>Named in grandfather John Harden's will.</td></tr>
      <tr><td>1770</td><td>Sold Abington land in June; purchased into Cummington (Town No. 5) with Silas Reed, 5 November.</td></tr>
```
new_string:
```
      <tr><td>1751</td><td>Named in grandfather John Harden's will.</td></tr>
      <tr><td>1752</td><td>Married Elizabeth "Betsey" Harden at Abington, 1 January.</td></tr>
      <tr><td>1770</td><td>Sold Abington land in June; purchased into Cummington (Town No. 5) with Silas Reed, 5 November.</td></tr>
```

`str_replace`

old_string:
```
      <tr><td>1790</td><td>Listed as head of household in the federal census, Cummington (3-0-3).</td></tr>
      <tr><td>1805</td><td>Died 28 September at Cummington; buried Dawes Cemetery.</td></tr>
```
new_string:
```
      <tr><td>1790</td><td>Listed as head of household in the federal census, Cummington (3-0-3).</td></tr>
      <tr><td>1800</td><td>First wife Elizabeth dies (30 July); marries Mercy Noyes (17 November).</td></tr>
      <tr><td>1805</td><td>Died 28 September at Cummington; buried Dawes Cemetery.</td></tr>
```

---

# Addendum operations (A12–A19) — Rigler c. 1980 worksheets

Folds in a second, earlier Rigler source: five Family Group Record worksheets (signed Robert G. Rigler, M.D., Honolulu; undated, c. 1980) covering Richard-2 (G12) through Amos (G8). The 1994 edition supersedes them; worksheet-only details absent from the 1994 edition are carried at lower weight per the superseded-drafts rule in `.claude/rules/citations.md`. The five page images were already moved to `sources/media/rigler-genealogy-notes-c1980/_local/` (gitignored; copyright) with a committed `_local/README.md`, mirroring the v84 media handling — no media op remains. The G8 (Amos) capture lands in the research companion only, per user direction.

## A12 — `data/sources.json`: add the worksheet source entry

`str_replace`

old_string:
```
    "anderson-great-migration-begins-v1-baxter": {
```
new_string:
```
    "rigler-genealogy-notes-c1980": {
      "shortTitle": "Rigler genealogy notes (worksheets, c. 1980)",
      "citation": "Rigler, Robert G., M.D. Gurney family group record worksheets (Richard-2 through Amos Gurney), c. 1980. Honolulu, Hawaii. Unpublished manuscript worksheets; the earlier working draft behind Jean Gurney Rigler, The Gurney Family from Aaron to Zuinglius (rev. and expanded ed., 1994).",
      "archive": "User-supplied scans of the physical worksheets",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md",
      "mediaPath": "sources/media/rigler-genealogy-notes-c1980/",
      "validationPath": "sources/validations/rigler-genealogy-notes-c1980.md",
      "notes": "Five Family Group Record worksheets compiling the direct American line Richard-2 (G12) through Amos (G8), signed Robert G. Rigler, M.D., of Honolulu - the earlier working draft behind Jean Gurney Rigler's 1994 published edition (rigler-gurney-family-aaron-zuinglius-1994), which supersedes them where they differ. Page images held local-only (copyright) under mediaPath/_local; transcription including the worksheets' Sources-of-Information boxes at corpusPath. Worksheet-only details absent from the 1994 edition are carried at lower weight per the superseded-drafts citation rule. Sub-authorities the worksheets cite (Anna Gurney Papers at the Dyer Memorial Library, Abington; Nahum Mitchell, History of Bridgewater; town vital records) are cited through the worksheet, not minted separately."
    },
    "anderson-great-migration-begins-v1-baxter": {
```

## A13 — `new file write`: `sources/validations/rigler-genealogy-notes-c1980.md`

```markdown
# Rigler — Gurney family-group worksheets (c. 1980) — validation

Source ID: `rigler-genealogy-notes-c1980`

Patchset: `sources/intake/done/v84-rigler-g9-g12-intake.patchset.md`

## Source examined
Five scanned Family Group Record worksheets signed Robert G. Rigler, M.D. (Honolulu), held local-only (copyright) at `sources/media/rigler-genealogy-notes-c1980/_local/`. One sheet each for Richard-2 (G12), Benjamin-3 (G11), Benjamin-4 (G10), Benjamin-5 (G9), and Amos (G8). The worksheets are the earlier working draft behind Jean Gurney Rigler's 1994 published edition (`rigler-gurney-family-aaron-zuinglius-1994`).

## Scope examined
All five sheets, including each sheet's "Sources of Information" box. Full transcription at `sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md`.

## Where findings landed
- G12 companion: the pre-revision arrangement (Peter and Sarah listed as Richard's children) corroborating the 1994 reattribution to the John Gurney-1 sibling set.
- G11 companion: Rebecca Staples "died before 18 Sept. 1745" (worksheet-only; provisional).
- G10 companion: the aunt-upbringing statement in the Sources box; the since-dropped speculative child "perhaps George."
- G9 companion: Asa's 30 Oct. 1782 marriage date; the Elizabeth-death 1801-vs-1800 conflict; Mitchell's *History of Bridgewater* and the Dyer Memorial Library repository for the Anna Gurney Papers.
- G8 companion: the named child set, the 29 Dec. 1790 marriage, and the post-1802 Long Island/Flushing destination.

## Limits
- Superseded by the 1994 edition; where the worksheet and the book conflict, the book governs. Worksheet-only deltas are caveated and carried at lower weight.
- The 1994 edition's Amos (G8) entry was not examined, so the G8 worksheet details could not be tested against the published edition.
- The G8 sheet's child birth-years are internally inconsistent (Amos b. 5 Nov. 1792 and Willis b. 25 Feb. 1793 cannot both be birth children) and conflict with the G8 companion's working Willis estimate; treated as suspect pending Cummington Vital Records.
- The G12 sheet's "Sources of Information" box is blank.
- The worksheets locate the Anna Gurney Papers at the Dyer Memorial Library, Abington, where the v84 transcription of the 1994 Benjamin-4 entry reads "NEHGS"; reconcile when the 1994 page is rechecked.
```

## A14 — `new file write`: `sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md`

```markdown
# Rigler — Gurney family-group worksheets (c. 1980) — transcription

Source ID: `rigler-genealogy-notes-c1980`

Working transcription of five Family Group Record worksheet forms compiling the direct American line, signed **Robert G. Rigler, M.D., 2117 Puuali'i Place, Honolulu, Hawaii**. Undated; the earlier working draft behind Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. ed., 1994), which supersedes them. Page images held local-only (copyright) at `sources/media/rigler-genealogy-notes-c1980/_local/`. The superscript generation numbers (Richard², … Amos⁶) are Rigler's own descent-from-Richard numbering, the reverse of the project's G-numbers (Richard = G12 … Amos = G8). Uncertain readings are marked `[?]`; bracketed expansions are editorial.

---

## Richard² Gurney (G12) — `rigler-c1980-worksheet-g12-richard-2-gurney.jpg`

- **Husband:** Richard² Gurney; "freem[an] 1681."
- **Born:** about 1630, England.
- **Died:** Oct. 1691, Weymouth, Mass. (Weymouth VR).
- **Husband's father:** "Perhaps John."
- **Wife:** Rebecca Taylor; her father John Taylor of Weymouth; her mother Rebecca.
- **Children** (marked "not in order"):
  - John (eldest), b. about 1654, Weymouth ("of Little Comfort"), Mass. — Elizabeth Green.
  - Richard, b. 18 Jan. 1656, Weymouth VR — unmarried.
  - Zachariah, b. abt. 1660 — "soldier in King Phillips War" — Mary Benson.
  - Joseph, b. 22 Feb. 1664/5, Weymouth — unmarried.
  - Mary, b. 9 Sept. 1667, Weymouth — unmarried.
  - Benjamin, b. about 1676 — Rebecca Staples.
  - Peter — "killed in King Phillips War, Dec. 1676."
  - Sarah — John Vinson.
- **Sources of Information:** *(blank)*

Note: Peter and Sarah appear here as Richard's own children; the 1994 edition moves both to the John Gurney-1 (G13) sibling set. This sheet captures the pre-revision arrangement.

---

## Benjamin³ Gurney (G11) — `rigler-c1980-worksheet-g11-benjamin-3-gurney.jpg`

- **Husband:** Benjamin³ Gurney, b. about 1676, "of Weymouth, Mass."
- **Married:** 30 Dec. 1701, First Church by Mr. Moses Fisk, Braintree, Mass.
- **Died:** "Will dated 4 May 1738," Middleboro, Mass.
- **Husband's father:** Richard Gurney; mother: Rebecca Taylor.
- **Wife:** Rebecca Staples, "of Braintree, Mass"; b. abt. 1682; **d. before 18 Sept. 1745**; her father John²[?] Staples; mother Sarah Atkins.
- **Children:**
  - Rebecca, b. 22 Nov. 1702, Weymouth VR — Daniel Taylor.
  - Benjamin, b. about 1704 — Sarah Morse.
- **Sources of Information:** "to Abington about 1707 then to Middleboro about 1730/31. Weymouth, Middleboro VR. Anna Gurney Papers — Dyer [Memorial] Gen[ealogical] Lib[rary] — Abington."

---

## Benjamin⁴ Gurney (G10) — `rigler-c1980-worksheet-g10-benjamin-4-gurney.jpg`

- **Husband:** Benjamin⁴ Gurney, "of Middleboro & Rochester," b. about 1704, "probably Weymouth, Mass."
- **Married:** 14 June 1731, by Rev. Benjamin Ruggles, Middleboro, Mass. (VR).
- **Died:** "before 1772"; lived Rochester.
- **Husband's father:** Benjamin³ Gurney; mother: Rebecca Staples.
- **Wife:** Sarah Morse.
- **Children:**
  - (by Jane (Jean) Harden — "dr. of John & Mary (Littlefield) Harden — she was born 19 Nov. 1709, Abington VR; married 29 Dec. 1731 to Ebenezer Spear, Abington VR"):
    - Benjamin, "bapt. 30 May 1730, Abington VR under Harding, and also Rev. Samuel Browne's Church record" — Elizabeth Harden.
  - Benjamin.
  - Levi.
  - Grace — [m.] 28 Nov. 1757, Joshua Ramon [Raymond].
  - Susannah — [m.] 26 July 1752, Jabez Benson.
  - Lemuel.
  - "Perhaps George (or else a grandson)."
- **Sources of Information:** "Benjamin — bapt. 1730, was raised by Nathan⁴ Gurney and his wife Sarah (Harden) Gurney, sister of Jean (Jane) Harden, in Abington, Mass. Rochester, Abington VR. Anna Gurney Papers — Dyer [Memorial] Gen[ealogical] Lib[rary] — Abington."

---

## Benjamin⁵ Gurney (G9) — `rigler-c1980-worksheet-g09-benjamin-5-gurney.jpg`

- **Husband:** Benjamin⁵ Gurney, b. "abt. 30 May 1730," "Abington VR under Harding & Rev. Sam'l Browne's Church Record."
- **Married:** 1 Jan. 1752, Abington VR.
- **Died:** 28 Sept. 1805, "in 76 yrs," Cummington, Mass.; bur. Dawes Cem., Cummington.
- **Husband's father:** Benjamin⁴ Gurney; mother: Jean (Jane) Harding (Harden). **Other wives:** 2) Mercy Noyes.
- **Wife 1):** Elizabeth (Betsey) Harden, b. about 1730; **d. 30 July 1801, "in [the] 70[th] yr,"** Cummington, Mass.; bur. Dawes Cem. Her father: Samuel Harden.
- **Children:**
  - Benjamin, b. 25 Aug. 1752, Bridgewater VR — [m.] 20 July 1802, Esther Cole.
  - Betty, b. 15 Nov. 1756 — not married.
  - Asa, b. 24 Oct. 1758 — **[m.] 30 Oct. 1782, Molly Reed.**
  - Jane.
  - Amos, b. "about 1770[?]" — [m.] 29 Dec. 1790, Ruth Gilbert.
  - Benjamin.
- **Sources of Information:** "Bridgewater, Abington, Cummington VR. Hist[ory] of Bridgewater, Mitchell. Anna Gurney Papers — Dyer [Memorial] Gen[ealogical] Lib[rary] — Abington. Moved from Abington to Cummington about 1770."

Note: the worksheet's Elizabeth-death year (30 July 1801) conflicts with the 1994 edition's 30 July 1800; the book governs.

---

## Amos⁶ Gurney (G8) — `rigler-c1980-worksheet-g08-amos-gurney.jpg`

- **Husband:** Amos⁶ Gurney, b. "about 1770[?]."
- **Married:** 29 Dec. 1790, "(some records give 1792)," Cummington, Mass.
- **Husband's father:** Benjamin Gurney; mother: Elizabeth (Betsey) Harden.
- **Wife:** Ruth Gilbert, b. "[c.] 1772[?]," Mass.
- **Children** (b. Cummington, Hampshire Co., Mass.):
  - Amos, b. 5 Nov. 1792 — "died young," 9 Nov. 1796.
  - **Willis G.**, b. 25 Feb. 1793 — *(marked as the direct-line child)*.
  - Willard, b. 6 Mar. 1794 — "died young," 6 Mar. 1794.
  - Hannah, b. 7 May 1795.
  - Ruth, b. 4 Jan. 1800.
  - Nathan, b. 2 Apr. 1802.
  - "(perhaps more)."
- **Sources of Information:** "Cummington Town Records (Town Clerk). Anna Gurney Papers — Dyer [Memorial] Gen[ealogical] Lib[rary] — Abington. He moved from Cummington to Long Island, NY, after 1802 (probably Flushing)."

Note: the birth-years here are internally inconsistent — Amos (5 Nov. 1792) and Willis (25 Feb. 1793) cannot both be birth children — and Willis-1793 conflicts with the G8 companion's working estimate of Willis c. 1796–98. The 1994 edition's Amos entry was not examined.

---

## Recurring citations across the worksheets (the "Sources of Information" boxes)

- **Anna Gurney Papers**, located by these worksheets at the **Dyer Memorial Library, Abington, Massachusetts** (on four of the five sheets). The v84 transcription of Rigler's 1994 Benjamin-4 entry reads "NEHGS" for the same papers; reconcile when the 1994 page is rechecked.
- **Town vital records:** Weymouth, Braintree, Abington, Bridgewater, Middleboro, Rochester, Cummington.
- **Nahum Mitchell, *History of the Early Settlement of Bridgewater*** (cited on the G9 sheet).
- **Cummington Town Records (Town Clerk)** (G8 sheet).
- **Rev. Samuel Browne's Church Record**, Old Abington (G9, G10 sheets), for the 1730 Benjamin baptism.

These sub-authorities are cited through the worksheet; none is minted as a separate `data/sources.json` entry.
```

## A15 — G12 companion — `research/people/g12-richard-gurney-fact-sheet.research.md`

`str_replace`

old_string:
```
## Sources Consulted
```
new_string:
```
## Rigler worksheet (c. 1980) — pre-revision draft of the Richard-2 entry

An earlier Rigler family-group worksheet for Richard-2 (signed Robert G. Rigler, M.D.) predates the 1994 entry and shows the children before the reattribution: it lists **Peter** ("killed in King Phillips War, Dec. 1676") and **Sarah** (m. John Vinson) as Richard's *own* children, and tags Zachariah a King Philip's War soldier. The 1994 edition moves Peter and Sarah to the John Gurney-1 (G13) sibling set — so the worksheet captures the superseded arrangement and shows that the reattribution adopted above was the author's own later correction, not an outside emendation. The worksheet also calls eldest son John "of Little Comfort," Weymouth; its "Sources of Information" box is blank.[^rigler-ws-g12]

[^rigler-ws-g12]: Robert G. Rigler, M.D., Gurney family-group worksheet for Richard² Gurney, c. 1980 (Honolulu); the earlier working draft behind the 1994 edition, which supersedes it. Image held local-only at `sources/media/rigler-genealogy-notes-c1980/_local/`; transcription at [`sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md). Source ID: `rigler-genealogy-notes-c1980`.

## Sources Consulted
```

## A16 — G11 companion — `research/people/g11-benjamin-gurney-fact-sheet.research.md`

`str_replace`

old_string:
```
## Sources Consulted
```
new_string:
```
## Rigler worksheet (c. 1980) — a death-date not carried into 1994

The earlier Rigler family-group worksheet for Benjamin-3 records **Rebecca (Staples) Gurney "died before 18 Sept. 1745"** — a death bracket the 1994 edition does not give. Because the published edition could have included it and did not, treat the 1745 bound as provisional, pending the underlying record (likely a 1745 deed or probate), rather than as established fact. The worksheet otherwise agrees with the 1994 entry (marriage 30 Dec. 1701 by Moses Fisk; to Abington c. 1707, Middleboro c. 1730/31; will dated 4 May 1738).[^rigler-ws-g11]

[^rigler-ws-g11]: Robert G. Rigler, M.D., Gurney family-group worksheet for Benjamin³ Gurney, c. 1980 (Honolulu). Image local-only at `sources/media/rigler-genealogy-notes-c1980/_local/`; transcription at [`sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md). Source ID: `rigler-genealogy-notes-c1980`. Worksheet-only details absent from the 1994 edition are carried at lower weight per `.claude/rules/citations.md`.

## Sources Consulted
```

## A17 — G10 companion — `research/people/g10-benjamin-gurney-fact-sheet.research.md`

`str_replace`

old_string:
```
## Sources consulted
```
new_string:
```
## Rigler worksheet (c. 1980)

The earlier Rigler family-group worksheet for Benjamin-4 agrees with the 1994 entry on Jane (Jean) Harden's parentage (daughter of Capt. John and Mary (Littlefield) Harden, b. 19 Nov. 1709; m. Ebenezer Spear 29 Dec. 1731) and states directly, in its Sources box, that the son Benjamin (bapt. 1730) "was raised by Nathan-4 Gurney and his wife Sarah (Harden) Gurney, sister of Jean (Jane) Harden, in Abington" — the same aunt-upbringing carried on the G9 work. Its one extra, since-dropped item is a speculative child, "perhaps George (or else a grandson)," not carried into the 1994 child set; record it only as a discarded lead.[^rigler-ws-g10]

[^rigler-ws-g10]: Robert G. Rigler, M.D., Gurney family-group worksheet for Benjamin⁴ Gurney, c. 1980 (Honolulu). Image local-only at `sources/media/rigler-genealogy-notes-c1980/_local/`; transcription at [`sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md). Source ID: `rigler-genealogy-notes-c1980`.

## Sources consulted
```

## A18 — G9 companion — `research/people/g09-benjamin-gurney-fact-sheet.research.md`

`str_replace`

old_string:
```
## Sources consulted
```
new_string:
```
## Rigler worksheet (c. 1980) — corroboration, a date, and a one-year conflict

The earlier Rigler family-group worksheet for Benjamin-5 confirms the core frame (bapt. 30 May 1730; m. 1 Jan. 1752 Elizabeth/Betsey Harden, daughter of Samuel Harden; 2) Mercy Noyes; d. 28 Sept. 1805 "in 76 yrs," bur. Dawes Cemetery, Cummington) and adds two things the 1994 entry does not:

- **Asa's marriage date.** Son Asa (b. 24 Oct. 1758) married **Molly Reed on 30 Oct. 1782**; the 1994 entry names the marriage but not the date. Carry the date as provisional (worksheet-only delta).
- **A cited authority and a repository.** The Sources box adds **Nahum Mitchell, *History of [the Early Settlement of] Bridgewater*** alongside the Bridgewater/Abington/Cummington vital records, and locates the **Anna Gurney Papers at the Dyer Memorial Library, Abington**.

One conflict: the worksheet gives Elizabeth (Harden) Gurney's death as **30 July 1801** "in [the] 70th yr," while the 1994 edition gives **30 July 1800**. The published edition supersedes, so keep 1800; the 1801 reading is noted only as the earlier draft.

The worksheet also restates the aunt-upbringing directly (on the Benjamin-4 sheet): Benjamin "was raised by Nathan-4 Gurney and his wife Sarah (Harden) Gurney, sister of Jean (Jane) Harden" — independent support for Sarah Harden Gurney as the caregiving aunt discussed above.[^rigler-ws-g9]

[^rigler-ws-g9]: Robert G. Rigler, M.D., Gurney family-group worksheets for Benjamin⁵ and Benjamin⁴ Gurney, c. 1980 (Honolulu); the earlier working draft behind the 1994 edition, which supersedes it. Images local-only at `sources/media/rigler-genealogy-notes-c1980/_local/`; transcription at [`sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md). Source ID: `rigler-genealogy-notes-c1980`.

## Sources consulted
```

## A19 — G8 companion — `research/people/g08-amos-gurney-fact-sheet.research.md`

### A19-1 — insert a worksheet working-note before Negative results

`str_replace`

old_string:
```
### Negative results
```
new_string:
```
### Rigler worksheet (c. 1980): a named child set, a marriage date, and a Long Island destination

An earlier Rigler family-group worksheet for Amos (signed Robert G. Rigler, M.D.) — the working draft behind the 1994 published genealogy — supplies the first compiled child set and a destination for the post-Cummington move. The 1994 edition's own Amos entry was not examined, so these cannot be tested against the published edition; treat them as a single compiled-source lead.[^rigler-ws-g8]

- **Where Amos went after 1802.** The Sources box states he "moved from Cummington to Long Island NY after 1802 (probably Flushing)" — pointing the same direction as son Willis's later Flushing household and making Amos's own removal to Queens County the leading hypothesis for open questions 1 and 2.
- **Marriage.** Amos married Ruth Gilbert (b. c. 1772) on **29 Dec. 1790** at Cummington, "some records give 1792."
- **Children** (worksheet, all said b. Cummington): Amos (5 Nov. 1792, d. young 9 Nov. 1796); **Willis G.** (25 Feb. 1793, the direct line); Willard (6 Mar. 1794, d. the same day); Hannah (7 May 1795); Ruth (4 Jan. 1800); Nathan (2 Apr. 1802); "perhaps more." This names the five children beyond Willis that the fact sheet currently leaves as a placeholder.

Caveats: the birth-years are internally inconsistent — Amos (5 Nov. 1792) and Willis (25 Feb. 1793) cannot both be birth children three months apart — and the worksheet's Willis-1793 conflicts with this companion's working estimate of Willis c. 1796–98. Carry the names as worksheet leads and the dates as suspect pending Cummington Vital Records.[^rigler-ws-g8]

[^rigler-ws-g8]: Robert G. Rigler, M.D., Gurney family-group worksheet for Amos Gurney, c. 1980 (Honolulu); the earlier working draft behind Jean Gurney Rigler's 1994 edition. Image held local-only at `sources/media/rigler-genealogy-notes-c1980/_local/`; transcription at [`sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/corpus_supplement/rigler-genealogy-notes-c1980-worksheets-extract.md). Source ID: `rigler-genealogy-notes-c1980`.

### Negative results
```

### A19-2 — add the worksheet to Sources Consulted

`str_replace`

old_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994). Key compiled genealogy for the G4-G13 direct line; source ID `rigler-gurney-family-aaron-zuinglius-1994`. Full page-level audit still pending.
```
new_string:
```
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. and expanded ed., 1994). Key compiled genealogy for the G4-G13 direct line; source ID `rigler-gurney-family-aaron-zuinglius-1994`. The 1994 Amos/G8 entry has not yet been examined.
- Robert G. Rigler, M.D., Gurney family-group worksheet for Amos Gurney, c. 1980 — earlier working draft; names the child set and gives the post-1802 Long Island/Flushing destination. Source ID `rigler-genealogy-notes-c1980`. See the worksheet note above.
```

---

# Open items and future pulls

- **Two-Benjamin Tinkham-date variant.** Rigler's own entries disagree on the joint Samuel Tinkham purchase date (26 Oct. vs 28 Oct. 1730, Plym. Reg. 39:79). The project keeps 28 October pending a direct deed image. (Unknown online.)
- **Rebecca Taylor's mother — Rebecca vs Phebe.** Rigler/the John Taylor will give Rebecca; *History of Weymouth* gives Phebe. Suffolk County probate (the John Taylor will, Suffolk Prob. 6:13, proved 1688) would settle it directly. (Unknown online.)
- **Cyrus Nash's Weymouth/Abington local history** (cited by Rigler as "D 1:13") for the Granny Gurney's Swamp story — worth a direct pull to quote the original. (Unknown online.)
- **Zachariah Gurney's King-Philip's-War "relief company" service**, previously asserted on the G12 fact sheet, was removed in this batch because it had become entangled with the Mendon misattribution and is not in Rigler; if a primary muster/relief-company record naming Richard's son Zachariah surfaces, it can be restored. (Unknown online.)
- **Broader data-file-reference cleanup.** Several `data/ancestors v26.json` references remain in the G9–G12 companions' older Working Notes sections (outside the cells edited here). A separate light pass should convert them to proper source citations per `citations.md`. (N/A — internal.)
- **Pre-existing Highlights shelfmarks.** The G10 fact sheet's first Highlights bullet still carries inline registry/deed codes (Plymouth Registry 39:79; Plymouth County land deed 95:139, GS film 559,140) that `fact-sheets.md` would move to the footnote; left untouched in this batch because the bullet was not otherwise rewritten. Worth a light citation-rigour pass. (N/A — internal.)

Worksheet-surfaced (c. 1980 sheets):
- **Anna Gurney Papers — repository reconciliation.** The worksheets place them at the **Dyer Memorial Library, Abington, Massachusetts**; the v84 transcription of the 1994 Benjamin-4 entry reads "NEHGS." Recheck the 1994 page and, if the worksheet repository is right, correct the G10 finding. The Dyer Memorial Library holds Abington-area family papers. (Unknown online.)
- **Nahum Mitchell, *History of the Early Settlement of Bridgewater*** (cited on the G9 worksheet) — a direct pull would let the Bridgewater-era G9/G10 facts cite Mitchell rather than Rigler-through-worksheet. (Unknown online — almost certainly digitised as an 1840 public-domain work, but not verified this session.)
- **Rebecca Staples death bracket (G11).** The worksheet's "died before 18 Sept. 1745" implies an underlying 1745 Plymouth deed or probate naming Benjamin-3's widow; locating it would convert the worksheet-only delta into a documented fact. (Unknown online.)
- **Amos (G8) to Long Island / Flushing.** The worksheet's "moved to Long Island NY after 1802 (probably Flushing)" is the strongest lead yet for the post-Cummington move; test against Queens County / Flushing records and the 1810–1840 censuses (already an open question on the G8 companion). (Unknown online.)

# Phase 2 checklist
- Apply A1 (sources.json), A2 (corpus supplement new file), A3 (validation rewrite), A4–A11 (research + fact-sheet str_replace ops).
- Then apply the worksheet addendum: A12 (sources.json entry), A13–A14 (validation + transcription new files), A15–A19 (companion str_replace ops). A15–A18 anchor on each companion's `## Sources [Cc]onsulted` heading and so must run after the A4/A6/A8/A10 "Rigler (1994) findings" inserts that share that anchor.
- Media (both sources) already moved to `_local` at user direction; no media operation remains.
- Normalize/verify footnote anchors after applying the fact-sheet edits (G12 now n1–n8; G11 n1–n7; G10 n1–n9; G9 n1–n11). The worksheet companion notes add self-contained footnotes (`[^rigler-ws-g8]` … `[^rigler-ws-g12]`) that need no renumbering.
- Stamp `**Done:** YYYY-MM-DD HH:MM PT` and move this file to `sources/intake/done/`.
