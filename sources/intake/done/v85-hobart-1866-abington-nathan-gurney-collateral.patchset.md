**Done:** 2026-06-04 12:57 PT

# v85 patchset — Benjamin Hobart, *History of the Town of Abington* (1866): the Little Comfort Gurney register + the collateral Nathan Gurney (foster father of G9)

Prepared: 2026-06-04
Phase: 1 (preparation)

Scope: Promote Benjamin Hobart's *History of the Town of Abington, Plymouth County, Massachusetts* (1866) into the repo as a new cited source, and use its **Gurney family register** (Appendix, pp. 383–386) to create a collateral fact sheet and research companion for **Nathan Gurney of Little Comfort/South Abington**, the kinsman who raised the direct-line ancestor Benjamin Gurney (G9). Adds the Hobart 1866 source to `data/sources.json`, a verbatim corpus-supplement transcription of the Gurney register and adjacent Harden/Hobart passages, a thin validation, the Nathan collateral fact sheet + companion, a `data/ancestors.json` related-person entry, a Little Comfort place-file narrative, and one additive corroboration block on the G9 companion. All operations are literal for Phase 2.

**Relationship to v84.** Independent of, and complementary to, the unapplied `v84-rigler-g9-g12-intake.patchset.md`. v84 promotes Jean Gurney Rigler's 1994 compiled genealogy (which states the aunt-upbringing and names "Nathan-4 & Sarah (Harden) Gurney"); v85 promotes a **second, independent** primary-derived source (Hobart 1866) that documents the same Nathan household from Abington town records, and builds the standalone collateral artefacts for Nathan that the user requested. The two patchsets may be applied in either order: v85's only edit to a v84-touched file (the G9 companion, operation A8) is anchored on a sentence v84 does not modify, and all other v85 targets are new files or files v84 never touches.

## Intake summary

The user supplied `sources/intake/new/historyoftownofa00hoba.pdf` (Internet Archive item `historyoftownofa00hoba`; 1866; public domain). It is **Benjamin Hobart's** *History of the Town of Abington* (1866) — distinct from the already-registered **Aaron Hobart**, *Historical Sketch of Abington* (1839, `hobart-abington-1839`). The user noted few references to the direct line but many to "Nathan Gurney," and asked whether they are the same man.

**Finding.** Hobart's Appendix carries a dedicated **GURNEY** genealogical register (pp. 383–386) that resolves the question. It documents:

1. **The Abington Gurney ancestor.** "**John Gurney**, the ancestor of most of the name in Abington, came from Weymouth, and settled in the south part of this town, then a part of Bridgewater, about the year 1690. He died about 1715… intestate… children, among whom were Richard, David and Nathan." This is the same **John Gurney** that Rigler (v84) identifies as John-3, son of Richard Gurney-2 (G12) and founder of the **Little Comfort mill** — i.e., a brother of the direct-line Benjamin Gurney-3 (G11). The independent match (Weymouth origin, south-Abington/Little Comfort settlement, intestacy, a son Nathan) is strong.
2. **Nathan Gurney's household.** "Nathan had Rebecca, born October, 1727; Lemuel, born October, 1730; Elijah, born 1732; Noah, born May, 1735; Nathan, born November, 1739; Silas, born June, 1743; Sarah, born March, 1745; Jacob, born March, 1748; John, born May, 1751." This is the **Nathan-4** of Rigler's account — the man who married Sarah Harden (his first child Rebecca b. Oct 1727 corroborates the ~1725 marriage in the compiled genealogies) and who raised the young Benjamin (G9), baptized 30 May 1730. Nathan was **first cousin of G9's father, Benjamin Gurney-4 (G10)** (both grandsons of Richard-2/G12), and **husband of G9's maternal aunt Sarah Harden** — doubly kin to the boy he raised.
3. **The two-Benjamin/childhood frame.** Benjamin G9 (bpt. 1730) grew up alongside Nathan and Sarah's own children — Rebecca (1727), Lemuel (1730, the same year), Elijah, Noah, and the rest — at Little Comfort. This supplies the household and chronology of G9's childhood and young adulthood, which the direct-line sources lack because G9 later left for Bridgewater and Cummington.
4. **The "many Nathans" disambiguation.** The prominent **Nathan Gurney, Jr., Esq.** named all over Hobart's main text (selectman from 1799 for twenty-four years, state representative, delegate to the 1820 constitutional convention, later a Boston alderman and Suffolk County senator; d. 11 Jan. 1851; sons Nahum P. and Ephraim Whitman Gurney; daughters Dianthe and Marilla) is **not** the foster-father Nathan. He is the great-grandson of John Gurney — "Nathan, son of Nathan" in the register (p. 385) — who married a daughter of Elijah Shaw, then **Martha "Puling"/Pullman**, then Sarah Whitman. He is the namesake of MACRIS inventory **WHI.307**, "Gurney, Nathan and Martha Pullman House," 496 Plymouth St, Whitman (c. 1816). At least three Nathan Gurneys (the foster-father, his son b. 1739, and his great-grandson b. c. 1783) appear in old Abington.

The direct line is sparse in Hobart precisely because it migrated away: Hobart's register carries forward the **collateral** Abington/Whitman Gurneys (Nathan-4's descendants), not the Cummington line. The value of the source is (a) the collateral Nathan household, (b) G9's childhood context, and (c) independent corroboration of the Little Comfort origin and Harden links already in the companions.

## Source tracking

- **New sourceId:** `hobart-benjamin-history-abington-1866` (operation A1). Distinct from `hobart-abington-1839` (Aaron Hobart). Public-domain 1866 imprint; the Internet Archive item is the canonical online copy. Sub-authorities Hobart cites in the register (Abington town vital records; Nahum Mitchell) are cited through Hobart, not minted separately.
- **MACRIS sourceId:** `macris-mhc` (source-tracking note below) — added only if absent, for the built-environment leads.
- **Validation:** new `sources/validations/hobart-benjamin-history-abington-1866.md` (operation A3), default-on for the new sourceId.
- **Corpus:** new `sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md` (operation A2) — verbatim Gurney register (pp. 383–386) plus the Harden/Hobart corroboration (Isaac Hobart m. Mary Harden, 1724, Appendix p. 357) and the Nathan-Jr disambiguation passages from the main text.
- **Media (Phase 2):** the 27.9 MB intake PDF is redundant with the freely online Internet Archive copy and the extract. Phase 2 moves it to `sources/media/hobart-benjamin-history-abington-1866/_local/` (gitignored) with a committed `_local/README.md` stub pointing to the archive.org item, rather than committing the bytes. `mediaPath` stays `null` in the source entry (canonical copy is online).
- **No new place IDs.** The narrative attaches to the existing `place-abington-whitman-line-massachusetts-usa` (Little Comfort) registry entry (operation A7).

---

# Operations (literal)

## A1 — `data/sources.json`: add the Hobart 1866 entry

`str_replace`

old_string:
```
      "notes": "Secondary local history for old Abington and Little Comfort. Useful for John Harden's Little Comfort context and the 22 February 1711 baptism of Jane Harden, daughter of John Harden of Little Comfort, as recorded by Mr. Niles of Braintree. Hobart-derived wording about an Elizabeth should be treated cautiously because the original John Harden will shows Elizabeth Harden as a witness, not as a daughter/heir."
    },
    "neverending-hobby-john-gurney-us-1636": {
```
new_string:
```
      "notes": "Secondary local history for old Abington and Little Comfort. Useful for John Harden's Little Comfort context and the 22 February 1711 baptism of Jane Harden, daughter of John Harden of Little Comfort, as recorded by Mr. Niles of Braintree. Hobart-derived wording about an Elizabeth should be treated cautiously because the original John Harden will shows Elizabeth Harden as a witness, not as a daughter/heir."
    },
    "hobart-benjamin-history-abington-1866": {
      "shortTitle": "Hobart, History of the Town of Abington (1866)",
      "citation": "Hobart, Benjamin. History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement. Boston: T. H. Carter and Son, 1866.",
      "archive": "Internet Archive, item historyoftownofa00hoba",
      "url": "https://archive.org/details/historyoftownofa00hoba/",
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md",
      "mediaPath": null,
      "validationPath": "sources/validations/hobart-benjamin-history-abington-1866.md",
      "notes": "Benjamin Hobart's full town history of Abington (1866), distinct from Aaron Hobart's 1839 Historical Sketch (hobart-abington-1839). Its Appendix Gurney register (pp. 383-386) is the key content: 'John Gurney, the ancestor of most of the name in Abington, came from Weymouth and settled in the south part of this town... about 1690... died about 1715... intestate... children among whom were Richard, David and Nathan.' This John is the John-3 (son of Richard Gurney-2, G12) of Rigler's account, founder of the Little Comfort mill. His son Nathan (children Rebecca 1727, Lemuel 1730, Elijah 1732, Noah 1735, Nathan 1739, Silas 1743, Sarah 1745, Jacob 1748, John 1751) is the Nathan-4 who married Sarah Harden and raised the direct-line Benjamin Gurney (G9). The prominent 'Nathan Gurney, jr., Esq.' of the main text (selectman, legislator, d. 1851; MACRIS WHI.307) is a different, later Nathan (the foster-father's great-grandson). Public domain; the Internet Archive item is the canonical online copy."
    },
    "neverending-hobby-john-gurney-us-1636": {
```

## A2 — `new file write`: `sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md`

```markdown
# Hobart, *History of the Town of Abington* (1866) — Gurney family register and Harden/Hobart corroboration

Source ID: `hobart-benjamin-history-abington-1866`

Working transcription from Benjamin Hobart, *History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement* (Boston: T. H. Carter and Son, 1866), Appendix. Transcribed from the Internet Archive copy ([item `historyoftownofa00hoba`](https://archive.org/details/historyoftownofa00hoba/)). Obvious optical-character-recognition errors have been silently normalized to the plainly intended reading (e.g. "Gukney" to Gurney, "1G08" to 1698, "Puling" preserved with a bracketed note); these are working readings, not a character-for-character facsimile. Uncertain readings are marked [?].

---

## GURNEY register (Appendix, pp. 383–386)

> **1. John Gurney**, the ancestor of most of the name in Abington, came from Weymouth, and settled in the south part of this town, then a part of Bridgewater, about the year 1690. He died about 1715; and, it seems, intestate, as his estate was divided equally among his children, among whom were Richard, David and Nathan. Nothing is known of the posterity of Richard and David.
>
> **2. Nathan** had Rebecca, born October, 1727; Lemuel, born October, 1730; Elijah, born ____, 1732; Noah, born May, 1735; Nathan, born November, 1739; Silas, born June, 1743; Sarah, born March, 1745; Jacob, born March, 1748; John, born May, 1751.
>
> **3. Lemuel** left no posterity, so far as is known.
> **3. Elijah** married a Widow House, and had Sophia and Sylvia.
> **3. Noah** married a daughter of Samuel Pool, Esq.; and had Asa, Joseph Pool, Noah, Jeremiah, James, John and Olive.
> **3. Silas** married a Palmer; and had Sarah, Oliver, Huldah, Rebecca, Anna and Ephraim.
> **3. Nathan** married a Palmer (sister of Silas' wife); and had Nathan, Mary and Lebbeus.
> **3. Jacob** married a Reese; and had Elizabeth, Ruth, Mehitable, Jacob, William S., Phebe and Lucy.
> **3. John** married Sarah Norton, daughter of Samuel Norton, Esq., and had Polly, Elizabeth, Sarah, Hannah, John, Ira, Martha, Clarissa and Zenas.
> **3. Sarah** married John Tirrell; no issue.
> **3. Rebecca** is supposed to have removed to Weymouth.

Fourth-generation entries on pp. 385–386 carry the line forward, including the prominent town figure:

> **4. Nathan, son of Nathan**, married a daughter of the late Elijah Shaw, and had Diantha and Merilla L. He afterwards married Martha [Puling — i.e. Pullman/Pulling], and had Nathan P.; she dying, he married Sarah Whitman, and had Ephraim W.
> **4. Lebbeus, son of Nathan**, married Susanna Lazell; and had Lebbeus, Nathan and Nahum; after her decease he married Ruth Gurney, and had children.

Hobart closes the register by distinguishing a second, unrelated Abington Gurney stock:

> There are a few others in Abington by this name, who probably did not descend from the ancestor John Gurney, but from **Joseph Gurney**, who settled in this town about the close of the seventeenth century. Joseph G. had children, viz., Perkins, Benoni and Joseph…

## Harden / Hobart corroboration (Appendix, p. 357)

In the Hobart family pedigree, the same volume independently fixes a Harden marriage already known from John Harden's 1751 will:

> IV. Isaac Hobart, son of the preceding, removed to Abington. He was born in Hingham, July 15, 1700. His removal to Abington was in 1724. He married Mary, daughter of John Harden, in that year, and died in Abington in 1775. Their children were — Thomas, born 1725; (Col.) Aaron, born 1729; Mary, born 1735; John, born 1738.

This is the "daughter Mary Hobart" of John Harden's will — sister of Sarah Harden Gurney and of Jane/Jean Harden (mother of Benjamin G9).

## The "many Nathans" — prominent Nathan Gurney, Jr. (main text)

For disambiguation: the Nathan Gurney named repeatedly in Hobart's main text (town representatives list, militia, the "elegant hall") is the foster-father's **great-grandson**, the "4. Nathan, son of Nathan" of the register:

> Nathan Gurney, jr., was a very useful man in all town affairs. In his early days he taught in the public schools for a number of years. He served as one of the selectmen from 1799, twenty-four years — twenty-two of them in succession; was Moderator in town meetings for a great number of years; represented the town in the State Legislature ten years. He was one of the delegates from this town, Nov. 15, 1820, to revise the Constitution of the Commonwealth. Mr. Gurney removed to Boston before 1830, was a member of the Board of Aldermen, and was a member of the Senate for the County of Suffolk. He was married four times; he left a widow and two sons — Nahum P. Gurney and Ephraim Whitman Gurney… He had two daughters, Dianthe and Marilla… Mr. Gurney died January 11, 1851.

He is the "Nathan and Martha Pullman House," 496 Plymouth St, Whitman (MACRIS WHI.307, c. 1816). His brother Jeremiah's house (Jeremiah Gurney, son of Noah, who "married Mary Fullarton") survives as MACRIS WHI.325, "Gurney, Jeremiah and Mary Fullerton House," 213 Washington St, Whitman.

## Little Comfort context (main text, p. 3)

> To accomplish this purpose, saw-mills were erected very early: three about the close of the seventeenth century. The first in 1698, at South Abington, then called "Little Comfort"…

This is the milling district Rigler associates with John Gurney-3's "Little Comfort mill," the seat of the family into which Benjamin G9 was fostered.
```

## A3 — `new file write`: `sources/validations/hobart-benjamin-history-abington-1866.md`

```markdown
# Benjamin Hobart, *History of the Town of Abington* (1866) — validation

Source ID: `hobart-benjamin-history-abington-1866`

## Source examined
Benjamin Hobart, *History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement* (Boston: T. H. Carter and Son, 1866). Internet Archive item `historyoftownofa00hoba`. Public-domain full-text PDF.

## Scope examined
Full text searched for Gurney/Harden/Little Comfort. Read in detail: the Appendix **Gurney** register (pp. 383–386); the Hobart pedigree's Isaac Hobart / Mary Harden entry (Appendix p. 357); the main-text biography of Nathan Gurney, Jr.; the Little Comfort sawmill note (p. 3). Verbatim extracts captured in `sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md`.

## Where findings landed
- Collateral fact sheet and companion for Nathan Gurney: `fact-sheets/g09-nathan-gurney-related-fact-sheet.md`, `research/people/nathan-gurney-abington.research.md`.
- Childhood/foster-household corroboration on the G9 companion: `research/people/g09-benjamin-gurney-fact-sheet.research.md`.
- Little Comfort Gurney origins on the place file: `research/places/abington-whitman-line-ma.md`.
- Data spine: related-person entry in `data/ancestors.json` (`collateral-g9-nathan-gurney-abington`).

## Limits / cautions
- Compiled secondary history; the register's birth dates derive from Abington town records but were not individually re-checked against the original *Vital Records of Abington* page images in this pass.
- Hobart gives no death date for the foster-father Nathan; do not infer one.
- At least three Nathan Gurneys appear (foster-father; his son b. 1739; his great-grandson "Nathan Gurney, Jr.," d. 1851). The identification of the John-Gurney-of-Little-Comfort with Rigler's John-3 (son of Richard-2/G12) is strong but rests on convergence of independent compiled accounts, not a single primary deed.
```

## A4 — `new file write`: `research/people/nathan-gurney-abington.research.md`

```markdown
# Nathan Gurney of Little Comfort / South Abington — Research Companion

Research companion for `fact-sheets/g09-nathan-gurney-related-fact-sheet.md`. Nathan Gurney is a **collateral** figure tied to the direct line at G9: he and his wife Sarah Harden raised the direct-line ancestor **Benjamin Gurney (G9)**, baptized at Abington 30 May 1730.

---

## Who he was, and why he matters

Nathan Gurney lived at **Little Comfort** — the milling district of south Abington (within the old Bridgewater bounds, later South Abington, now **Whitman**). He was a son of **John Gurney**, the Weymouth man who settled there about 1690 and started the Little Comfort sawmill, and therefore a grandson of **Richard Gurney of Weymouth (G12)**. That makes Nathan a **first cousin of Benjamin Gurney-4 (G10)** — both were grandsons of Richard — and the cousin's household was where Benjamin (G10)'s out-of-wedlock son was raised.[^hobart-register][^rigler-g10]

Nathan married **Sarah Harden** (b. 9 Apr. 1707, Abington), a daughter of John Harden of Little Comfort, blacksmith, and Mary Littlefield, and a **sister of Jane/Jean Harden**, the mother of Benjamin G9. So when Benjamin was born in 1730, Nathan and Sarah were doubly his kin: **Sarah was his maternal aunt; Nathan was his father's first cousin.** Rigler states the upbringing directly — Benjamin "was raised in Abington by Nathan-4 & Sarah (Harden) Gurney, his mother's sister" — and Hobart independently documents the household that took him in.[^hobart-register][^rigler-g9][^john-harden-will]

## The household Benjamin grew up in

Hobart's Abington Gurney register gives Nathan and Sarah's children with birth months and years drawn from the town records:[^hobart-register]

- Rebecca, b. October 1727
- Lemuel, b. October 1730
- Elijah, b. 1732
- Noah, b. May 1735
- Nathan, b. November 1739
- Silas, b. June 1743
- Sarah, b. March 1745
- Jacob, b. March 1748
- John, b. May 1751

Benjamin G9 (bpt. 30 May 1730) was almost exactly the age of Lemuel and slightly younger than Rebecca; he grew up among roughly nine Gurney foster-siblings at Little Comfort. Rebecca's October-1727 birth corroborates the **12 May 1725** marriage date that the compiled genealogies give for Nathan and Sarah Harden.[^hobart-register][^neverending-hobby]

No death date for Nathan is recorded in the examined sources; his youngest documented child was born in 1751.[^hobart-register]

## The Little Comfort origin — John Gurney, the Abington ancestor

Hobart: "**John Gurney**, the ancestor of most of the name in Abington, came from Weymouth, and settled in the south part of this town, then a part of Bridgewater, about the year 1690. He died about 1715; and, it seems, intestate… children, among whom were Richard, David and Nathan."[^hobart-register]

This John is, on convergent evidence, the **John Gurney-3 (son of Richard-2/G12)** whom Rigler names as the founder of the **Little Comfort mill**: same Weymouth origin, same south-Abington settlement, same intestacy, a son Nathan. The identification ties the foster-household directly back into the direct line — Nathan's father John and the direct-line Benjamin Gurney-3 (G11) were brothers, both sons of Richard Gurney (G12).[^hobart-register][^rigler-g10]

## At least three Nathan Gurneys — disambiguation

The Abington/Whitman Gurneys produced several Nathans; conflating them is the obvious trap:

1. **The foster-father Nathan** (this subject) — son of John, m. Sarah Harden ~1725, children 1727–1751.
2. **Nathan, his son** (b. November 1739) — "married a Palmer (sister of Silas' wife); and had Nathan, Mary and Lebbeus."[^hobart-register]
3. **Nathan Gurney, Jr., Esq.** (d. 11 Jan. 1851) — the foster-father's **great-grandson**, the "Nathan, son of Nathan" of Hobart's fourth generation. A schoolteacher, selectman from 1799 (twenty-four years), state representative, delegate to the 1820 Massachusetts constitutional convention, later a Boston alderman and Suffolk County senator. He married a daughter of Elijah Shaw, then **Martha "Pullman/Pulling,"** then Sarah Whitman; sons Nahum P. and Ephraim Whitman Gurney; daughters Dianthe and Marilla.[^hobart-nathan-jr]

The famous Whitman house "**Gurney, Nathan and Martha Pullman House**," 496 Plymouth St (Massachusetts Historical Commission inventory **WHI.307**, c. 1816), belongs to #3, not to the foster-father.[^macris]

## MACRIS / built-environment leads

The Massachusetts Cultural Resource Information System (MACRIS, mhc-macris.net) lists several Gurney properties that map onto this family's footprint. Inventory forms (the "B-form" PDFs) often carry a builder genealogy worth pulling. (Availability: the MACRIS database and most inventory forms are **available online**.)

Collateral Abington/Whitman (Nathan's descendants), highest relevance:
- **WHI.307** — Gurney, Nathan and Martha Pullman House, 496 Plymouth St, Whitman, c. 1816 → Nathan Gurney, Jr. (d. 1851).
- **WHI.325** — Gurney, Jeremiah and Mary Fullerton House, 213 Washington St, Whitman, c. 1795 → Jeremiah Gurney, son of Noah, grandson of the foster-father.
- **WHI.283** — Gurney, Jonathan Reed and Deborah C. Reed House, 364 Franklin St, Whitman, c. 1816 → a Jonathan R. Gurney of this stock.
- Other Whitman Gurney entries (WHI.305 Daniel; WHI.314 Edwin; WHI.322 Hersey–Lydia Gurney; WHI.72 F. H. Gurney Building) are likely the same descent.

Direct-line leads (the Cummington migration of Benjamin G9), to pursue on the G8/G9 companions rather than here:
- **CUM.115** — Gurney, "Ase" House, 51 Main St, Cummington, 1816; **CUM.151** — Gurney, Asa House, 75 Mount Rd, Cummington, 1808. Candidate seats of G9's son **Asa Gurney** (b. 24 Oct. 1758, m. Molly Reed) or his descendants. **PLF.14** (Plainfield) and **ASF.241** (Ashfield) are neighboring-town Gurneys of the same Hampshire-County diaspora.

Two-Benjamin collateral (the Rochester half-brother line):
- **ROC.938** — East Rochester Cemetery, Gurney, Benjamin Stone, 1828 → a strong candidate for the gravestone of the Revolutionary-War Benjamin Gurney (d. 4 July 1828), the Sarah-Morse half-brother in the two-Benjamin problem.

## Open questions
1. **Nathan's vital dates.** Birth (implied c. 1700–1704), exact marriage record at Abington, and death/probate are not yet pinned to primary record images. (Unknown online.)
2. **Guardianship of Benjamin.** No primary guardianship, church, or estate record yet places Benjamin in Nathan's household; Hobart and Rigler are both compiled. A loose Plymouth County file or Abington church record would upgrade the fostering from compiled statement to documented fact. (Unknown online.)
3. **John Gurney-3's estate.** Hobart says he died "about 1715… intestate." A Plymouth County administration or division record would confirm the Little Comfort succession and the children Richard/David/Nathan. (Unknown online.)

---

## Sources consulted
- Benjamin Hobart, *History of the Town of Abington* (1866), Appendix Gurney register pp. 383–386 and main-text Nathan Gurney, Jr. biography.[^hobart-register][^hobart-nathan-jr]
- Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius* (rev. ed., 1994).[^rigler-g9][^rigler-g10]
- John Harden's 1751 Plymouth County will.[^john-harden-will]
- *The Neverending Hobby — John Gurney, US 1636*.[^neverending-hobby]
- Massachusetts Cultural Resource Information System (MACRIS).[^macris]

[^hobart-register]: Benjamin Hobart, *History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement* (Boston: T. H. Carter and Son, 1866), Appendix, "Gurney" family register, pp. 383–386; verbatim extract at `sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md`; [Internet Archive item historyoftownofa00hoba](https://archive.org/details/historyoftownofa00hoba/). Source ID: `hobart-benjamin-history-abington-1866`.
[^hobart-nathan-jr]: Hobart, *History of the Town of Abington* (1866), main-text biography of Nathan Gurney, Jr. (selectman from 1799, state representative, 1820 constitutional-convention delegate, Boston alderman and Suffolk senator, d. 11 Jan. 1851), with the fourth-generation register entry "Nathan, son of Nathan" (pp. 385–386). Source ID: `hobart-benjamin-history-abington-1866`.
[^rigler-g9]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius: Some Descendants of Richard Gurney Who Settled at Weymouth, MA before 1656*, rev. and expanded ed. (Honolulu: J. G. Rigler, 1994), entry BENJAMIN GURNEY-5, pp. 21–22 ("raised in Abington by Nathan-4 & Sarah (Harden) Gurney, his mother's sister"). Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.
[^rigler-g10]: Rigler, *Gurney Family from Aaron to Zuinglius* (1994), entries BENJAMIN GURNEY-3 and BENJAMIN GURNEY-4, pp. 19–21, identifying John Gurney-3 (Richard-2) as founder of the Little Comfort mill and the Weymouth-to-Abington Gurney settlement. Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.
[^john-harden-will]: Massachusetts. Probate Court (Plymouth County), record-book will of John Harden of Bridgewater, blacksmith, dated 17 September 1751, proved 7 October 1751, manuscript pp. 383–384; names daughter Sarah Gurney and daughter Jane Spear and grandson Benjamin Gurney. Source ID: `plymouth-probate-john-harden-1751-will`.
[^neverending-hobby]: ["John Gurney, US 1636,"](https://sites.google.com/site/theneverendinghobby/home/those-connected-to-more-than-one-family/john-gurney-us-1636) *The Neverending Hobby*, public compiled genealogy, giving Nathan Gurney's marriage to Sarah Harden on 12 May 1725. Use as secondary compiled genealogy. Source ID: `neverending-hobby-john-gurney-us-1636`.
[^macris]: Massachusetts Cultural Resource Information System (MACRIS), Massachusetts Historical Commission, [mhc-macris.net](https://mhc-macris.net/), inventory entries WHI.307, WHI.325, WHI.283, CUM.115, CUM.151, ROC.938 (Gurney properties). Source ID: `macris-mhc`.
```

## A5 — `new file write`: `fact-sheets/g09-nathan-gurney-related-fact-sheet.md`

```markdown
---
layout: layouts/base.njk
permalink: /fact-sheets/g09-nathan-gurney-related-fact-sheet.html
title: Nathan Gurney Related Fact Sheet
pageHeading: Nathan Gurney of Little Comfort (c.1700–after 1751)
subtitle: "Nathan Gurney was not a direct ancestor; he and his wife Sarah Harden raised the direct-line ancestor Benjamin Gurney (G9)."
description: "Related-person fact sheet for Nathan Gurney of Little Comfort (South Abington / Whitman), the kinsman who raised Benjamin Gurney (G9): grandson of Richard Gurney of Weymouth and husband of G9's maternal aunt Sarah Harden."
bodyClass: bio-page factsheet-page
activeNav: factsheets
factsheet:
  gen: G9
  slug: g09-nathan-gurney-related-fact-sheet
  personName: Nathan Gurney
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "name": "Nathan Gurney of Little Comfort - Related Fact Sheet",
  "description": "Related-person fact sheet for Nathan Gurney of Little Comfort (South Abington / Whitman), who with his wife Sarah Harden raised the direct-line ancestor Benjamin Gurney (G9).",
  "mainEntity": {
    "@type": "Person",
    "name": "Nathan Gurney",
    "birthDate": "1700",
    "description": "Little Comfort (South Abington / Whitman) farmer, grandson of Richard Gurney of Weymouth, husband of Sarah Harden, and foster father of the direct-line ancestor Benjamin Gurney (G9)."
  }
}
</script>

<div class="factsheet-top">
  <div class="factsheet-main">

<section class="fact-section fact-section-vitals" id="vital-records">
<div class="facts-vitals-grid">
  <div class="fact-item">
    <div class="fact-label">Born</div>
    <div class="fact-value">About 1700–1704, probably at Weymouth or the new Little Comfort settlement. No birth record survives; his 1725 marriage and his first child's 1727 birth place him in that bracket. He was a son of John Gurney, the Weymouth man who settled south Abington, and a grandson of Richard Gurney of Weymouth. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Died</div>
    <div class="fact-value">Not established in surviving records. His youngest recorded child was born in 1751, and he headed a Little Comfort household through the middle of the century. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Home</div>
    <div class="fact-value">Little Comfort, the milling district of south Abington — then within the bounds of Bridgewater, later South Abington, today Whitman. His father had started the Little Comfort sawmill there. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Marriage</div>
    <div class="fact-value">Married Sarah Harden (born 9 April 1707, Abington), daughter of John Harden of Little Comfort, blacksmith, and Mary Littlefield, on 12 May 1725. Sarah was the sister of Jane Harden, the mother of Benjamin Gurney (G9). <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Relationship</div>
    <div class="fact-value"><strong>Related, tied to G9.</strong> Nathan was a first cousin of Benjamin Gurney (G10) — both grandsons of Richard Gurney (G12) — and the husband of G9's maternal aunt. He and Sarah raised the young Benjamin (G9). He is not himself in the direct ancestor line. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
  </div>
</div>
</section>

<section class="fact-panel fact-panel-highlights" id="highlights">
<h2 class="unnumbered">Highlights</h2>

<ul>
  <li><strong>He raised a direct-line ancestor.</strong> Nathan and his wife Sarah Harden brought up Benjamin Gurney (G9), born in 1730 of an unmarried liaison, in their Little Comfort home. <sup class="fn"><a href="#n5" id="ref-5b">5</a></sup></li>
  <li><strong>Doubly kin to the boy.</strong> Sarah was Benjamin's mother's sister; Nathan was his father's first cousin. Fostering the child kept him inside both his Harden and his Gurney families. <sup class="fn"><a href="#n5" id="ref-5c">5</a></sup></li>
  <li><strong>Of the Little Comfort Gurneys.</strong> His father, John Gurney, came from Weymouth about 1690, settled the south part of old Abington, and started its first sawmill — the family seat for the next century. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></li>
  <li><strong>A large household.</strong> Nathan and Sarah had nine recorded children between 1727 and 1751 — Rebecca, Lemuel, Elijah, Noah, Nathan, Silas, Sarah, Jacob, and John — and Benjamin grew up among them. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></li>
  <li><strong>Ancestor of the Whitman Gurneys.</strong> His descendants anchored South Abington and Whitman for generations. One great-grandson, also Nathan Gurney, became a long-serving selectman and state legislator — a different man, often confused with the foster father. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
</ul>
</section>

<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

Nathan Gurney belongs to the Abington side of the family rather than the direct line, but he sits at one of its turning points: he and his wife raised the boy who carries the line forward. The Gurneys had reached old Abington a generation earlier, when Nathan's father, John Gurney, came over from Weymouth about 1690 and settled the south part of the town — then still within Bridgewater — at the milling hamlet called Little Comfort, where he built one of its first sawmills. John was a son of Richard Gurney of Weymouth (G12); his brother Benjamin (G11) is the direct ancestor, which makes Nathan and the direct-line Benjamin Gurney (G10) first cousins. <sup class="fn"><a href="#n3" id="ref-3c">3</a></sup><sup class="fn"><a href="#n5" id="ref-5d">5</a></sup>

In 1725 Nathan married Sarah Harden, a blacksmith's daughter from Little Comfort and a sister of Jane Harden. Five years later Jane gave birth to a son, Benjamin, baptized at the First Church of Abington on 30 May 1730 with only his mother named. The child was taken into Nathan and Sarah's household — a natural landing place, since Sarah was the baby's aunt and Nathan his father's cousin. Benjamin grew up there alongside the couple's own children: Rebecca, born in 1727; Lemuel, born the same year as Benjamin; and, in the years that followed, Elijah, Noah, Nathan, Silas, Sarah, Jacob, and John. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup>

What became of Nathan himself is not recorded; no death date or estate has yet surfaced, and the last of his children was born in 1751. His line, however, did not leave. While the direct-line Benjamin moved on to Bridgewater and ultimately to Cummington in the western hills, Nathan's sons and grandsons stayed in south Abington, gave their name to houses still standing in Whitman, and produced — three generations on — another Nathan Gurney prominent enough in town affairs that the two are easily mistaken for one another. <sup class="fn"><a href="#n2" id="ref-2b">2</a></sup><sup class="fn"><a href="#n7" id="ref-7b">7</a></sup>
</section>

<section class="fact-section" id="citations">
<h2 class="unnumbered">Citations</h2>

<ol class="citation-list">
  <li id="n1">Birth bracket inferred from his 1725 marriage and first child's 1727 birth; parentage and grandparentage from Benjamin Hobart, <em>History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement</em> (Boston: T. H. Carter and Son, 1866), Appendix Gurney register, pp. 383–384, and Jean Gurney Rigler, <em>The Gurney Family from Aaron to Zuinglius</em>, rev. ed. (Honolulu: J. G. Rigler, 1994). Source IDs: <code>hobart-benjamin-history-abington-1866</code>, <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-1">return</a></li>
  <li id="n2">Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 384 (youngest recorded child John, b. May 1751; no death recorded for Nathan). Source ID: <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-2">return</a></li>
  <li id="n3">Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 383 ("John Gurney… came from Weymouth, and settled in the south part of this town… about the year 1690") and p. 3 (first Little Comfort sawmill, 1698); Rigler, <em>Gurney Family</em> (1994), identifying John Gurney as founder of the Little Comfort mill. Source IDs: <code>hobart-benjamin-history-abington-1866</code>, <code>rigler-gurney-family-aaron-zuinglius-1994</code>. <a class="citation-back" href="#ref-3">return</a></li>
  <li id="n4">Sarah Harden's birth (9 April 1707) and parentage from <em>Vital Records of Abington, Massachusetts, to the Year 1850</em>, vol. 1, and John Harden's 1751 Plymouth County will (daughter Sarah Gurney); marriage of Nathan Gurney and Sarah Harden, 12 May 1725, from <em>The Neverending Hobby — John Gurney, US 1636</em>, corroborated by the October-1727 birth of their first child in Hobart's register. Source IDs: <code>abington-vr-1850-vol1</code>, <code>plymouth-probate-john-harden-1751-will</code>, <code>neverending-hobby-john-gurney-us-1636</code>, <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-4">return</a></li>
  <li id="n5">Relationship: Rigler, <em>Gurney Family</em> (1994), entry Benjamin Gurney-5, pp. 21–22 ("raised in Abington by Nathan-4 &amp; Sarah (Harden) Gurney, his mother's sister"); and the shared descent from Richard Gurney of Weymouth (G12) through John Gurney (Nathan's father) and Benjamin Gurney-3 (G11, the direct ancestor) in Hobart's register and Rigler. Source IDs: <code>rigler-gurney-family-aaron-zuinglius-1994</code>, <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-5">return</a></li>
  <li id="n6">Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, p. 384 (children of Nathan: Rebecca 1727, Lemuel 1730, Elijah 1732, Noah 1735, Nathan 1739, Silas 1743, Sarah 1745, Jacob 1748, John 1751). Source ID: <code>hobart-benjamin-history-abington-1866</code>. <a class="citation-back" href="#ref-6">return</a></li>
  <li id="n7">Hobart, <em>History of the Town of Abington</em> (1866), Appendix Gurney register, pp. 385–386, and main-text biography of Nathan Gurney, Jr. (d. 11 Jan. 1851); Massachusetts Cultural Resource Information System inventory WHI.307 ("Gurney, Nathan and Martha Pullman House," Whitman). Source IDs: <code>hobart-benjamin-history-abington-1866</code>, <code>macris-mhc</code>. <a class="citation-back" href="#ref-7">return</a></li>
</ol>
</section>

  </div>

  <aside class="factsheet-side">

<div class="fact-panel">
  <h2>Related Links</h2>
  <div class="fact-buttons">
    <a href="/maps-and-lists/ancestor-table.html">Ancestor Table</a>
    <a href="/fact-sheets/g09-benjamin-gurney-fact-sheet.html">G9 Benjamin Gurney</a>
    <a href="/fact-sheets/g10-benjamin-gurney-fact-sheet.html">G10 Benjamin Gurney</a>
    <a href="/research/companions/nathan-gurney-abington.html">Research notes</a>
    <a href="https://archive.org/details/historyoftownofa00hoba/">Hobart, History of Abington (1866)</a>
  </div>
</div>

<div class="fact-panel">
  <h2>Relationship Path</h2>
  <table class="fact-timeline-table">
    <tbody>
      <tr><th>Step</th><th>Line</th></tr>
      <tr><td>Grandfather</td><td>Richard Gurney of Weymouth (G12)</td></tr>
      <tr><td>Father</td><td>John Gurney, settler of Little Comfort</td></tr>
      <tr><td>Direct-line cousin</td><td>Benjamin Gurney (G10), father of G9</td></tr>
      <tr><td>Wife</td><td>Sarah Harden, maternal aunt of G9</td></tr>
      <tr><td>Role</td><td>Foster father of Benjamin Gurney (G9)</td></tr>
    </tbody>
  </table>
</div>

<div class="fact-panel">
  <h2>Timeline</h2>
  <table class="fact-timeline-table">
    <tbody>
      <tr><th>Year</th><th>Event</th></tr>
      <tr><td>c.1700–04</td><td>Born, a son of John Gurney of Little Comfort.</td></tr>
      <tr><td>1725</td><td>Married Sarah Harden, 12 May.</td></tr>
      <tr><td>1727</td><td>First child, Rebecca, born.</td></tr>
      <tr><td>1730</td><td>Took in his nephew Benjamin (G9), baptized 30 May; son Lemuel born the same year.</td></tr>
      <tr><td>1732–51</td><td>Seven more children: Elijah, Noah, Nathan, Silas, Sarah, Jacob, John.</td></tr>
      <tr><td>after 1751</td><td>Death not recorded; the Whitman Gurney line descends from him.</td></tr>
    </tbody>
  </table>
</div>

  </aside>
</div>
```

## A6 — `data/ancestors.json`: insert the Nathan related-person entry after G9

`str_replace`

old_string:
```
      "place-cummington-massachusetts-usa"
    ]
  },
  {
    "type": "ancestor",
    "gen": "G10",
    "name": "Benjamin Gurney",
```
new_string:
```
      "place-cummington-massachusetts-usa"
    ]
  },
  {
    "type": "related",
    "gen": "G9",
    "name": "Nathan Gurney (foster father of G9)",
    "dates": "c. 1700 — after 1751",
    "geography": "Weymouth → Little Comfort / South Abington (now Whitman), MA",
    "eraId": "era-massachusetts-farming-generations",
    "lineageStatus": "Related - foster father of G9 Benjamin Gurney; first cousin of G10 Benjamin Gurney",
    "summary": "Collateral figure tied to the direct line at G9. Nathan Gurney and his wife Sarah Harden raised the direct-line ancestor Benjamin Gurney (G9), baptized at Abington 30 May 1730. Nathan was doubly kin to the boy: a first cousin of G9's father, Benjamin Gurney (G10) - both grandsons of Richard Gurney (G12) - and the husband of G9's maternal aunt Sarah Harden.",
    "notables": "Of the Little Comfort Gurneys of south Abington. His father, John Gurney, came from Weymouth about 1690, settled the south part of old Abington (within Bridgewater bounds, later South Abington / Whitman), and started the Little Comfort sawmill. Nathan married Sarah Harden (b. 9 Apr. 1707), daughter of John Harden of Little Comfort, blacksmith, on 12 May 1725. Benjamin Hobart's History of Abington (1866) records their nine children from town records: Rebecca (Oct. 1727), Lemuel (Oct. 1730), Elijah (1732), Noah (May 1735), Nathan (Nov. 1739), Silas (June 1743), Sarah (Mar. 1745), Jacob (Mar. 1748), John (May 1751). Benjamin G9, baptized 1730, grew up among them. Not to be confused with his great-grandson Nathan Gurney, Jr. (d. 1851), the long-serving selectman and legislator and namesake of the Whitman 'Nathan and Martha Pullman House' (MACRIS WHI.307).",
    "landHoldings": "Little Comfort / south Abington (later Whitman), the Gurney family seat his father settled about 1690.",
    "spouses": [
      {
        "name": "Sarah Harden",
        "dates": "b. 9 Apr. 1707; m. 12 May 1725",
        "notes": "Daughter of John Harden of Little Comfort, blacksmith, and Mary Littlefield; sister of Jane Harden (mother of Benjamin G9); named 'daughter Sarah Gurney' in John Harden's 1751 will."
      }
    ],
    "children": [
      {
        "name": "Benjamin Gurney (G9, fostered)",
        "dates": "bpt. 30 May 1730",
        "notes": "Direct-line ancestor; Nathan's wife's nephew and his own first cousin's son, raised in this household."
      },
      {
        "name": "Rebecca Gurney",
        "dates": "b. Oct. 1727"
      },
      {
        "name": "Lemuel Gurney",
        "dates": "b. Oct. 1730"
      },
      {
        "name": "other children",
        "notes": "Elijah (1732), Noah (1735), Nathan (1739), Silas (1743), Sarah (1745), Jacob (1748), John (1751), per Hobart's Abington Gurney register."
      }
    ],
    "buttons": [
      {
        "label": "Related fact sheet",
        "url": "/fact-sheets/g09-nathan-gurney-related-fact-sheet.html",
        "style": "bio"
      },
      {
        "label": "Research notes",
        "url": "/research/companions/nathan-gurney-abington.html",
        "style": "research"
      },
      {
        "label": "Hobart, History of Abington (1866)",
        "url": "https://archive.org/details/historyoftownofa00hoba/",
        "style": "research"
      }
    ],
    "recordId": "collateral-g9-nathan-gurney-abington",
    "placeRefs": [
      "place-abington-massachusetts-usa",
      "place-abington-whitman-line-massachusetts-usa"
    ]
  },
  {
    "type": "ancestor",
    "gen": "G10",
    "name": "Benjamin Gurney",
```

## A7 — `research/places/abington-whitman-line-ma.md`: append Gurney-origins narrative below the generated block

`str_replace`

old_string:
```
<!-- GENERATED:PLACE-REGISTRY:END -->
```
new_string:
```
<!-- GENERATED:PLACE-REGISTRY:END -->

## Gurney origins at Little Comfort

Little Comfort — the milling hamlet of south Abington, then within the bounds of Bridgewater and later South Abington / Whitman — was the seat of the Abington Gurneys. **John Gurney** came from Weymouth and settled here about 1690, dying about 1715, intestate; his estate was divided among his children, among whom were Richard, David, and Nathan. He is, on convergent evidence, the John Gurney-3 (son of Richard Gurney of Weymouth, G12) whom Rigler names as founder of the **Little Comfort sawmill** — the first of the three south-Abington mills, built about 1698. John's brother Benjamin (G11) is the direct ancestor, so the Little Comfort Gurneys and the direct line spring from the same Weymouth household.[^hobart-little-comfort][^rigler-little-comfort]

John's son **Nathan Gurney** married **Sarah Harden** of Little Comfort (a blacksmith's daughter) about 1725 and raised here his wife's nephew **Benjamin Gurney (G9)**, baptized at Abington in 1730. While the direct line later moved west to Cummington, Nathan's descendants stayed: the Whitman Gurney houses recorded in the Massachusetts Cultural Resource Information System (e.g. the Nathan-and-Martha-Pullman house, WHI.307, and the Jeremiah-and-Mary-Fullerton house, WHI.325) mark their continued presence on this ground. See `research/people/nathan-gurney-abington.research.md`.[^hobart-little-comfort]

[^hobart-little-comfort]: Benjamin Hobart, *History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement* (Boston: T. H. Carter and Son, 1866), Appendix Gurney register pp. 383–386 and main-text Little Comfort sawmill note p. 3; [Internet Archive item historyoftownofa00hoba](https://archive.org/details/historyoftownofa00hoba/). Source ID: `hobart-benjamin-history-abington-1866`.
[^rigler-little-comfort]: Jean Gurney Rigler, *The Gurney Family from Aaron to Zuinglius*, rev. ed. (Honolulu: J. G. Rigler, 1994), identifying John Gurney-3 (Richard-2) as founder of the Little Comfort mill. Source ID: `rigler-gurney-family-aaron-zuinglius-1994`.
```

## A8 — `research/people/g09-benjamin-gurney-fact-sheet.research.md`: add a Hobart corroboration block to the aunt-upbringing section

Anchored on the closing sentence of the "Was Benjamin raised by a maternal aunt?" section, which `v84` does not modify; safe to apply before or after v84.

`str_replace`

old_string:
```
The fact sheet should not say Benjamin was raised by his aunt as a proved fact. A durable phrasing is: **Family tradition says Benjamin was raised by a maternal aunt; Sarah Harden Gurney is the strongest candidate, but no guardianship or household record has yet been found.**
```
new_string:
```
The fact sheet should not say Benjamin was raised by his aunt as a proved fact. A durable phrasing is: **Family tradition says Benjamin was raised by a maternal aunt; Sarah Harden Gurney is the strongest candidate, but no guardianship or household record has yet been found.**

### Hobart (1866) names the foster household

Benjamin Hobart's *History of the Town of Abington* (1866) independently documents the household. Its Abington Gurney register makes Sarah Harden's husband **Nathan Gurney** a son of **John Gurney**, the Weymouth man who settled Little Comfort about 1690 and started its sawmill — i.e., the John Gurney-3 (son of Richard-2/G12) of Rigler's account, and a brother of the direct-line Benjamin Gurney-3 (G11). That makes Nathan a **first cousin of Benjamin's father, Benjamin Gurney G10**, as well as the husband of Benjamin's aunt: the boy was kept inside his Gurney kin and his Harden kin at once. Hobart gives Nathan and Sarah's children from town records — Rebecca (Oct. 1727), Lemuel (Oct. 1730), Elijah (1732), Noah (May 1735), Nathan (Nov. 1739), Silas (June 1743), Sarah (Mar. 1745), Jacob (Mar. 1748), John (May 1751) — so the household Benjamin grew up in can be reconstructed: he was the near-twin in age of Lemuel and grew up among roughly nine foster-siblings at Little Comfort. Rebecca's 1727 birth corroborates the 12 May 1725 marriage date the compiled genealogies give for Nathan and Sarah. The full collateral treatment is in `research/people/nathan-gurney-abington.research.md` and the related fact sheet `fact-sheets/g09-nathan-gurney-related-fact-sheet.md`.[^hobart-abington-1866]
```

Then add the footnote definition. `str_replace`

old_string:
```
[^foster-cummington]: Foster and Streeter, *Only One Cummington* (1974), p. 390, Benjamin Gurney / Cummington land and farm-exchange context. Existing sourceId in repo may be `foster-streeter-cummington`; if absent, add a separate `data/sources.json` entry before citing.
```
new_string:
```
[^foster-cummington]: Foster and Streeter, *Only One Cummington* (1974), p. 390, Benjamin Gurney / Cummington land and farm-exchange context. Existing sourceId in repo may be `foster-streeter-cummington`; if absent, add a separate `data/sources.json` entry before citing.
[^hobart-abington-1866]: Benjamin Hobart, *History of the Town of Abington, Plymouth County, Massachusetts, from its First Settlement* (Boston: T. H. Carter and Son, 1866), Appendix Gurney register, pp. 383–386; verbatim extract at `sources/corpus_supplement/hobart-1866-abington-gurney-register-extract.md`; [Internet Archive item historyoftownofa00hoba](https://archive.org/details/historyoftownofa00hoba/). Source ID: `hobart-benjamin-history-abington-1866`.
```

---

# Source-tracking note: the MACRIS reference

The MACRIS leads above reference a Massachusetts Historical Commission database, not a single document. Operation A4 and the fact sheet cite it under a sourceId `macris-mhc`. If that sourceId does not already exist in `data/sources.json` at Phase 2, add it as part of this patchset:

`str_replace` (only if `macris-mhc` is absent)

old_string:
```
    "hobart-benjamin-history-abington-1866": {
      "shortTitle": "Hobart, History of the Town of Abington (1866)",
```
new_string:
```
    "macris-mhc": {
      "shortTitle": "MACRIS - Massachusetts Cultural Resource Information System",
      "citation": "Massachusetts Cultural Resource Information System (MACRIS). Massachusetts Historical Commission.",
      "archive": "MHC online inventory database",
      "url": "https://mhc-macris.net/",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "State inventory of historic properties. Gurney entries of interest: WHI.307 (Nathan and Martha Pullman House, Whitman) and WHI.325 (Jeremiah and Mary Fullerton House, Whitman) for the collateral Abington/Whitman Gurney descent; CUM.115 and CUM.151 (Asa Gurney houses, Cummington) as candidate seats of the direct line's Cummington branch; ROC.938 (East Rochester Cemetery, Benjamin Gurney stone, 1828) for the two-Benjamin half-brother line. Inventory 'B-form' PDFs frequently carry builder genealogies worth pulling."
    },
    "hobart-benjamin-history-abington-1866": {
      "shortTitle": "Hobart, History of the Town of Abington (1866)",
```

---

# Open items and future pulls
- **Primary fostering record.** Loose Plymouth County estate file for John Harden (1751) or Abington First Church records may name Benjamin's guardian/household. (Unknown online.)
- **John Gurney-3 estate.** Plymouth County administration/division, c. 1715, would confirm the Little Comfort succession (children Richard, David, Nathan). (Unknown online.)
- **Cummington direct-line built environment.** MACRIS CUM.115 and CUM.151 ("Asa Gurney" houses) — pull the inventory forms to test descent from G9's son Asa (b. 1758). (Available online — mhc-macris.net.)
- **Rochester half-brother grave.** MACRIS ROC.938 (East Rochester Cemetery, Benjamin Gurney stone, 1828) — likely the Revolutionary-War Benjamin, the two-Benjamin half-brother. (Available online — mhc-macris.net.)
- **Original Abington VR images.** Re-check Nathan/Sarah's children's birth entries against the *Vital Records of Abington* page images. (Available online — Internet Archive / Wikimedia Commons.)

---

# Phase 2 checklist
1. A1 — add the `hobart-benjamin-history-abington-1866` source entry; add `macris-mhc` if absent (source-tracking note).
2. A2 — write the corpus-supplement extract.
3. A3 — write the validation.
4. A4 — write the Nathan companion.
5. A5 — write the Nathan related fact sheet.
6. A6 — insert the Nathan related-person entry in `data/ancestors.json`; validate JSON.
7. A7 — append the Little Comfort Gurney-origins narrative to the place file.
8. A8 — add the Hobart corroboration block + footnote to the G9 companion (independent of v84 order).
9. Media — move `sources/intake/new/historyoftownofa00hoba.pdf` to `sources/media/hobart-benjamin-history-abington-1866/_local/` with a committed `_local/README.md` stub pointing to the Internet Archive item; remove the intake copy.
10. Confirm `data/ancestors.json` and `data/sources.json` are valid JSON and the new fact sheet's footnote anchors resolve.
11. Prepend `**Done:** YYYY-MM-DD HH:MM PT` and move this patchset to `sources/intake/done/`.
```
