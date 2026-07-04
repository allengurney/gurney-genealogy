# Dump — G13 John Gurney colonial Massachusetts Bay discovery campaign (2026-07-01)

Raw research dump. Not repo-integrated; a synthesis worker will process this later.
Subject: John Gurney G13 (emigrant, Weymouth by 30 May 1641, Braintree, d. 1662/3).
Objective this turn: colonial-side discovery beyond the already-deep Weymouth/Braintree surname base —
(1) Massachusetts Bay Colony-level record collections; (2) county/Boston roll-up scope;
(3) Hingham-as-arrival delta; (4) broad name variants in colonial sources; (5) nearby-community
arrival points; (6) less-traveled sites/collections.

## 0. Scope map — what "county" means for these towns 

[AG][DIRECTIVE] Add this section to Weymouth Place file

County-scoped searching (recommend adding to a topic file or the companion as a methods note):

- **Suffolk County (created 1643)** contained Boston, Braintree, Weymouth, Hingham, Dorchester,
  Roxbury, Dedham, etc., for John's entire colonial life. All county-level court, deed, and probate
  records for John's towns 1643–1663 are SUFFOLK series (Suffolk Deeds, Suffolk Probate, Suffolk
  County Court files) — already the repo's main colonial spine. There is no separate 1640s–60s
  "Weymouth deeds" registry to find.
- **"Old" Norfolk County (1643–1679)** = Salisbury/Haverhill/Hampton etc. (north of the Merrimack).
  It has NOTHING to do with Braintree/Weymouth/Quincy. Colonial "Norfolk County" search hits are a
  false-friend trap.
- **Modern Norfolk County (1793)** is the one containing Braintree/Weymouth/Quincy/Randolph — only
  relevant for post-1793 record series (e.g. 19th-c. cemetery/vital transcriptions, Find a Grave's
  "Norfolk County" labels).
- **Plymouth County** — Hingham moved to Plymouth County only in 1803; in John's era Hingham was
  Suffolk. Plymouth COLONY records (separate jurisdiction) matter for Scituate (Isaac Gurney 1663/4)
  and the colony-boundary line just south of Hingham/Weymouth.
- **Before 1643** (John's 1641 first record) there were no counties: the roll-up is the colony
  itself — Massachusetts Bay General Court + Court of Assistants records, and Boston-centric
  notarial/church/land books. This is why colony-level and Boston-level sweeps are the correct
  "beyond Weymouth" widening for the arrival window.

## 1. Campaign design (Gate A/B per online-discovery-strategy)

Objective: find any record of John Gurney (any variant) in colony-level, Boston-level, or
neighboring-town collections 1636–1663 that (a) antedates 30 May 1641, (b) substantiates or
kills Anderson's "Boston" settlement attribution, (c) surfaces an arrival vector (Hingham or
other), or (d) adds network/kinship data usable for the English-origin question.

Source characterisation: these are mostly 19th-c. printed transcriptions of clerk manuscripts —
high capture fidelity print, but 17th-c. clerk spelling (Gurny, Gurnie, Gurnee, Gurnay, Garny,
Gorny, Gvrney) and OCR of old type (long-s not an issue for names; u/n confusion Gurnev/Gnrney
possible). Index model: most volumes have printed name indexes PLUS full OCR text — sweep BOTH
(index-head forms differ from body forms). Technique: download full djvu texts to scratch;
ripgrep-based variant sweep (repo_search locate --path) with wide net `G[aeiou]rn` + `Gurn`;
read hits in context; treat "Gurnet(t)" (Plymouth headland "the Gurnet") as a known false friend.

Variant net used for scratch sweeps (regex): `G[aeiouvy]rn[aeiouy]` + `Gourn` (case-insens.),
manually filtering Garner/Gurnet/Gurnsey-type collisions per search-variants.json collision notes.

## 2. Target collections this turn (worklist)

| # | Collection | Why | Status |
|---|---|---|---|
| T1 | Aspinwall Notarial Records, Boston 1644–1651 (Rec. Comm. vol 32) | Boston roll-up; deeds/depositions/powers of attorney incl. Atlantic-trade net; unswept (L-193) | pending |
| T2 | Lechford Note-Book 1638–1641 (Boston lawyer) | EXACT arrival window; unswept (L-193) | pending |
| T3 | Records of the Court of Assistants MBC 1630–1692 (3 vols) | Colony roll-up above MBCR; unswept | pending |
| T4 | MBCR (Shurtleff) vols 2–5 full variant sweep | Only v1:331 + v2:79 read point-wise; no systematic sweep; May 1645 Braintree petition (L-191) may be pinned here | pending |
| T5 | Plymouth Colony Records (Shurtleff/Pulsifer) sweep | Scituate/Isaac; colony south of Weymouth; unswept | pending |
| T6 | Pope, Pioneers of Massachusetts (1900) | Independent compiler vs Anderson/Banks; unchecked | pending |
| T7 | Suffolk Deeds Libers I–III (+ VI) | Libers IV & V read; I–III cover 1640–1660 Boston-recorded deeds | pending |
| T8 | Boston First Church / Winthrop Papers / other Boston-side | Anderson "Boston" attribution test | pending |
| T9 | Hingham delta: Hobart journal + Hingham town records beyond genealogies | Arrival-vector test (L-188 residual) | pending |
| T10 | FamilySearch FTS colonial films (Mass Archives colonial collection; Suffolk court files) | Manuscript-level roll-up search; 1641 petition doc itself (L-186) | pending |

STATUS AT END OF TURN: T1 done (negative, F6); T2 done (negative, F6); T3 done (negative, F6 —
volume-mapping caveat); T4 done (F5 + F6 negatives; L-191 petition NOT in printed MBCR);
T5 done (Isaac-only, F6); T6 done (F1/F2/F3 — major); T7 done (F4 resolved + F6 negatives);
T8 done (F9 — flagship Winthrop letter; First Church records still open, §6); T9 partial
(F11 — Hobart gated); T10 done for this turn (F7 breakthrough + F8; Arch-45 volume pull open,
§6). NEW source worked beyond plan: CSM Suffolk County Court 1671–80 (F10, one open thread).

## 3. Findings

### F1 — Pope's *Pioneers of Massachusetts* (1900): the Cheny/Gurney conflict resolved as a TYPO, plus a NEW 1646 petition record [T6 — MAJOR]

Source: Charles Henry Pope, *The Pioneers of Massachusetts* (Boston, 1900), main entry under
**"GURNET, GORNET"** (with index cross-refs "GORNET, see Gurney" and "GORNELL, see Gurnell and
Cornell"). Archive.org id `pioneersofmassac00pope`, `_djvu.txt` lines ~27264–27280. Accessed 2026-07-01.

Verbatim (OCR-corrected):

> GURNET, GORNET,
> John, Sen., tailor, Braintree. [N. B. He is called John Cheny, Sen., in the printed
> records of Braintree, by a typographical error.] Was an apprentice of John Newgate,
> 29 (7) 1636, ae. 21 years; had 3 years longer to serve. [W.] Signed a petition about
> the meadows in 1646. [Arch. 45.] Sold land in Br. 12 Feb. 1661. His wife d. 20 (7) 1661,
> and he m. 12 (9) 1661, Grizzell, widow of Henry Kibbee.
> He d. in 1662-3; inv. March 16, 1663. [Reg. XII, 53.]

Insights:
1. **L-11 (Braintree Cheny/Gurney conflict): Pope explicitly rules the 1886 printed Braintree
   record's "John Cheny, Sen." a typographical error for John Gurney** — and he reads BOTH the
   20 (7) 1661 wife-death line and the 12 (9) 1661 Grizzell marriage line as the Gurney family.
   This is an independent, records-based 1900 authority siding with the Torrey/Sprague/TAG
   tradition. It does not replace the manuscript check (FS film 940974 / DGS 7009769), but it
   materially raises confidence and should be added to the companion's Grizzell section.
2. **NEW PRIMARY-RECORD LEAD: "Signed a petition about the meadows in 1646. [Arch. 45.]"**
   "Arch. 45" = Massachusetts Archives Collection (Felt collection), vol. 45 (Lands, 1622–1726).
   A 1646 petition about meadows signed by John Gurney is NOT in the repo chronology. It may be
   the same document as (or sibling to) the May 1645 "new plantation at Braintree" petition
   (L-191, primary page never pinned) — Braintree's new-plantation petitions of 1645/46 concerned
   meadow allotments — or a separate Braintree/Weymouth meadows petition. Either way this gives a
   concrete manuscript volume target (Mass Archives v. 45) that is FILMED in the FamilySearch
   "Massachusetts State Archives collection, colonial period, 1622–1788" series already used for
   the 1641 gunpowder petition (film 007702977 etc.). Action: FTS/film-browse Mass Archives v45.
3. Pope conflates the 1636 Newgate apprentice with the Braintree John (repo's two-Johns
   de-conflation, case file §8.5, argues against; Pope 1900 predates that analysis). Pope's
   conflation is another data point on how the 1636/1615 tradition propagated into compilers.
4. Pope's head-form **"GURNET, GORNET"** documents colonial-era index/head variants for the
   emigrant himself that are NOT in `data/search-variants.json` Modern family: **Gurnet, Gornet**
   (and body-form "Gurner" — see F4). Recommend adding Gurnet/Gornet/Gurner as collision-prone
   broad additions (collision: "the Gurnet" headland at Plymouth; Garnet(t) surname).

### F2 — "Jane Gurney of Mendon" m. John Bundy Sr., 9 Jan 1676 — Pope vs Torrey's "Ruth" [T6 — new person-level datum]

Pope, *Pioneers*, BUNDY entry (`_djvu.txt` lines ~10310–10330): John Bundy (Plymouth apprentice
1635 → Boston → Taunton), wife Martha d. 1 May 1674; "he m. 9 Jan. 1676, **Jane Gurney of
Mendon**." Will April 1681, "Senior, ae. 64 years."

The repo (via Torrey p. 331) carries this same remarriage as **Ruth** (widow of John Gurney Jr.,
killed at Mendon July 1675): "GURNEY, John (-1675?) & Ruth ?RETCHELL, m/2 John BUNDY 1676."
The Mendon town book (primary) has "Samuel son of John & **Ruth** Gurney born March 14. 1671."
So Pope's "Jane" and Torrey's "Ruth" describe the same 1676 Bundy marriage with conflicting
forenames. Options: (a) Pope misread/typo for Ruth; (b) the Taunton/Plymouth record actually
reads Jane and Torrey normalized to the Mendon Ruth; (c) two marriages. Action: check the
primary marriage record (Taunton VR; the marriage was probably recorded at Taunton or in
Plymouth colony records — the Plymouth Colony Records sweep this turn found no Bundy×Gurney
marriage, so Taunton VR printed volumes are the next check).

### F3 — "Jane Gurnet," legatee in a 1664 Dorchester will whose co-legatees include Braintree's minister [T6 — NEW unplaced Gurney-family person]

Pope, *Pioneers*, LAVER entry (lines ~37210–37223): **Margery Laver** (LAVER, LAUER, LEVVER, see
Leaver), Dorchester church member c. 1639; will dated 4 (6) 1664, proved 10 (9) 1664:

> beq. to Mr. William Tompson, Mr. Richard Mather, Daniel Preston and his wife and children,
> **Jane Gurnet**, Mr. John and Thomas Wiswall. [Reg. XIII, 13.]

Insights: Mr. William Tompson = minister of BRAINTREE; Richard Mather = minister of Dorchester;
the Wiswalls = Dorchester elite. A "Jane Gurnet" receiving a bequest from a Dorchester widow in
1664, alongside Braintree's pastor, is a previously unrecorded Gurney-orbit woman — no Jane
exists in the reconstructed G13 family (children: Sarah, Mary, Richard, John Jr., Peter, Isaac).
Working hypotheses (untested): (i) Jane = the later "Jane Gurney of Mendon" (F2) — i.e., the
woman who married John Gurney Jr. c. 1670 was a Dorchester servant/kinswoman named Jane, and
the Mendon town book's "Ruth" vs Pope's "Jane" conflict resolves toward one woman with a
mis-recorded forename somewhere; (ii) Jane = an otherwise unrecorded daughter or kinswoman of
G13 placed in Dorchester service; (iii) Jane Gurnet here = a Garnet/Gurnell-family woman and
Pope's spelling misleads (but Pope himself separates GORNELL→Gurnell/Cornell from GORNET→Gurney).
Action: read the will abstract at NEHGR vol. 13 ("Reg. XIII"), p. 13, and ideally the Suffolk
probate original (Margery Laver/Leaver, Dorchester 1664) for the exact spelling and any
relationship language ("my servant," "my kinswoman," etc.).

### F4 — Suffolk Deeds Liber I index: "Gurner, James, 5" — an unexplained James Gurn- in earliest Boston deed registry [T7 — to resolve]

Suffolk Deeds Liber I (printed 1880; archive.org `suffolkdeeds01suff`), index line "Gurner,
James, 5." (adjacent "Gurdon, John, 5"). Body text on printed p. 5 needs reading — the OCR body
sweep did not surface a "James Gurner" line (OCR may have mangled it). Liber I covers 1640–1653
— IN the arrival window. If "Gurner" = Gurney variant, a James Gurner in earliest Boston records
would be a new same-surname colonial datum (compare the Norwich James Gurney, son of laceweaver
Francis, freed 1648 — case file two-Francis discussion). If it resolves to Garner/Gardner, it is
a false friend. Action: read printed page 5 (image or body text) — see §6 if image needed.

### F5 — MBCR v5 p. 540: Richard Gurney (G12) freeman-list entry pinned [T4 — corroboration]

*Records of the Governor and Company of the Massachusetts Bay*, vol. 5 (1674–1686), p. 540:
"Rich'd Gurney" in a sworn-freemen list (near Tho: White, Tho: Bayly, Joseph Dyer, Obadiah
Sajle, Jn° Shaw Jun. — a Weymouth cohort; list dated 1681 by position). Pins the G12 companion's
"Freeman 1681" to its primary printed citation: MBCR 5:540. Archive.org `recordsofgoverno05mass`.
Also in v5: "Jane Burg, some time wife of John Gurnell" (Dorchester Gurnell family — distinct
surname, but note the Burg(e) name collision with Grizzell's 5th husband John Burge; do not
conflate).

### F6 — Colony-level and Boston-level NEGATIVES from the full-text sweeps [T1–T5, T7 — first-class negatives]

Variant net: case-sensitive `G[aeiouvy]rn[aeiouy]|Gourn` AND case-insensitive
`(?i)g[aeiouvy]rn(ey|ay|y|ie|ee|e)\b` over full djvu texts (body + printed indexes), 2026-07-01.
Known false friends seen and excluded: Gurnet's Nose (Plymouth headland), Garnett/Garnet (Samuel,
Southwark, in Aspinwall; Symon, Suffolk Deeds I; John, Suffolk Deeds VI = Braintree-area GARNETT
family — NB abutting "country road" parcels, could be confused with Gurney in casual reading),
Garnesey/Guernsey (Wm, MBCR 4:129), Gurnell (John, of Dorchester — distinct family, Suffolk Deeds
I:34, III, MBCR 2:293, 5:xx), Gornell (Thomas, of Boston, sold 112 A. at Mount Wollaston —
Suffolk Deeds I:15 — NOTE: a *Mount Wollaston* landholder pre-1653; Pope says GORNELL may read
Gurnell OR Cornell; worth one look but almost certainly the Cornell family), Gurdon/Gurden,
Robert Garnill (Lechford index).

Genuine-Gurney absences (each a usable negative):
- **Aspinwall Notarial Records, Boston 1644–1651** (Rec. Comm. v32, `volumerelatingto32bost`):
  ZERO Gurney any variant. John had Boston-facing debts at death (1663 inventory: "Smith and
  Collins at Boston," "charges at Boston"), but no notarial instrument 1644–51 touches him.
- **Lechford Note-Book 1638–1641** (`notebookkeptbyth00lech`): ZERO Gurney any variant. The
  arrival-window Boston lawyer's practice did not touch John (or the Newgate apprentice, whose
  indenture ended c. Sept 1639 — Lechford silent on any Gurney).
- **Records of the Court of Assistants MBC** — copies swept: `recordscourtass01crongoog`,
  `recordsofcourtof02massuoft` (1630–1644), `recordsofcourtof03mass`: ZERO Gurney. (Caveat: the
  three archive.org copies' volume mapping should be re-verified if this negative is promoted.)
- **MBCR v1 sweep**: only the known 1:331 (index "Gurney, John, 331") — no second v1 entry.
- **MBCR v2 sweep**: only the known 2:79 Gurny bill (+ Gurnell 2:293, distinct). No 1645
  Braintree-petition Gurney entry printed in v2.
- **MBCR v3, v4 pt1, v4 pt2 sweeps**: ZERO Gurney 1644–1674 at colony level. Combined with v5
  (only Richard 1681), the colony-level print record for G13 is exactly two entries (1:331 fine
  remission 1641; 2:79 bill 1644). **John G13 was never admitted freeman** (no admission in any
  MBCR volume) — consistent with his mark-signature and with no church-membership record;
  worth stating in the companion as a social-status finding.
- **Plymouth Colony Records** (vols 1–8, 11–12 in the 6 combined archive.org items): the ONLY
  Gurney in the entire Plymouth colony record is Isacke Gurney's 1 March 1663/4 Scituate
  pilfering matter (already held; PCR 4:51 — index "Gurney, Isaac, punished for pilfering, 51" —
  including the certificate "These may certify, that Isacke Gurney, whoe was complained against
  by..." — the certificate text at lines ~24220ff adds detail worth transcribing for the Isaac
  file). No other Gurney: none in the land vols, none in the Bundy 1676 marriage context, no
  John/Richard/Peter. Hingham-adjacent Scituate/Marshfield land records: no Gurney.
- **Suffolk Deeds Liber I–III and VI sweeps** (`suffolkdeeds01/02/03/06suff`): beyond the known
  Liber IV/V Gurney material, NO John Gurney deed in Libers I–III (1640–1660) or VI — i.e., John
  recorded nothing at Boston before the 1661/2 Thayer deed (recorded 1668, Liber V). His
  Braintree freehold's own acquisition was therefore either unrecorded or recorded under a
  grantor's deed not indexed to him. The unexplained "Gurner, James, 5" (F4) is the single
  Liber I–III residue.

Interpretation for Anderson's "Boston": after this sweep the Boston-collection base rate for a
real Boston residence of the elder John is much weaker — Boston Town Records/Book of Possessions
(prior negative), Aspinwall (new negative), Lechford (new negative), Suffolk Deeds I–III (new
negative), Boston notarial/court print series (negative). Anderson's "Boston" attribution looks
increasingly like an artifact of the Newgate-apprentice conflation (the apprentice WAS in Boston
1636–c.1639, in Newgate's household). Remaining Boston-side checks: First Church records (gated,
see §6), Winthrop Papers (T8), Boston church admissions in NEHGR.

### F2-RESOLVED — The Bundy bride is RUTH (Pope's "Jane" is Pope's error); primary record found verbatim; two NEW colonial spelling variants attested

- **Plymouth Colony Records vol. 8 (Taunton returns, printed p. ~60):** "John Bundey married
  to Ruth **Surney**, of Mendum, this 9'th of January, 1676." (archive.org
  `recordsofcolonyo0708newp`, djvu lines ~4238–4240). This is the primary printed record.
- **Taunton VR to 1850, vol. 2 (marriages):** "BUNDY, John [dup. and t.p.r. John Bundy] and
  Ruth **Garney** [dup. and T.P.R. **Gurney**] of Mendun, Jan. 9, 1676.* [John Bundey and Ruth
  **Surney** of Mendun, P.C.R.]" — with the standalone cross-refs "GARNEY (see Gurney)" and
  "SURNEY, Ruth (see Ruth Gurney)". Archive.org `vitalrecordsofta02unse` / `vitalrecordsoftataun_5`.
- Conclusion: Ruth (widow of John Gurney Jr., killed at Mendon July 1675) m/2 John Bundy of
  Taunton 9 Jan 1676 — Torrey and the Mendon town book confirmed; **Pope's "Jane Gurney of
  Mendon" is an error in Pope** (do not create a Jane-of-Mendon person from it). This also
  decouples Pope's Bundy "Jane" from the 1664 Dorchester "Jane Gurnet" (F3) — the unify-them
  hypothesis in F3(i) is now unsupported; F3 stands alone.
- **Variant-registry recommendations:** colonial-attested forms **Garney** (already broad,
  collision-flagged) and NEW **Surney** (S/G initial-letter corruption in a primary colony
  record!) — a textbook first-character corruption per the discovery-strategy skill; also
  **Gurnet/Gornet** as compiler head-forms (Pope). Consider adding Surney/Gurnet/Gornet to
  the Modern broad set with collision warnings (Gurnet = Plymouth headland; Garnet surname).
- **NEW unplaced person: Elizabeth Gurney m. Timothy Cooper, Taunton, 16 Oct 1706** (Taunton VR
  v2 = "GURNEY (Garney), Elizabeth and Timothy Cooper"; independently in NEHGR 13:254,
  "Marriages in Taunton": "Timothy Cooper and Elisabeth Gurney married Oct. 16, 1706").
  Hypothesis: a child or granddaughter of John Gurney Jr. & Ruth carried to Taunton in Ruth's
  1676 Bundy household (known children of John Jr. & Ruth: John, Samuel b. 1671, Mary). Gives
  the John-Jr. line a Taunton continuation not currently in the repo. Follow-up: Taunton VR
  births/deaths for Gurney; Bundy will (April 1681, "beq. to wife and son James; other children
  by this wife") — check whether Gurney stepchildren appear in the probate file.

### F3-VERBATIM — the Laver will text (NEHGR 13:13): "to Jane Gurnet, 2s for a memorandum"

NEHGR vol. 13 (1859), p. 13, "Abstracts of Early Wills" (archive.org `newenglandhistor1318unse`,
djvu lines ~1763–1771), will of Margery Laver of Dorchester (dated 4 (6) 1664, prob. 10 (9) 1664):

> "And for Legacye & Giftes my will is, that M' William Tomson haue 10s, to M' Richard Mather,
> 10s, to John Wiswall, the youngest of the three, my siluer spoone, to Daniell Prestons
> Children, 5s in siluer, apeice, to his Wife a new p[air] of Cotton Cardes, **to Jane Gurnet,
> 2s for a memorandum**. To Mr John Wiswalls wife a little peice of Gold..."

Reading: a 2-shilling keepsake to a local woman among Dorchester/Braintree ministerial and
neighbor bequests. No relationship stated. Identity options: (a) kin/wife of the Dorchester
**Gurnell** family (John Gurnell of Dorchester is well attested in Suffolk Deeds I/III and MBCR;
Gurnell→Gurnet slip is easy) — NOTE the NEHGR v13 index keeps "Gurnet, 13" separate from
"Gurney, 145, 146, 254", and Pope indexed GORNET→Gurney vs GORNELL→Gurnell/Cornell, so the
compilers disagree; (b) an otherwise-unrecorded Gurney woman in Dorchester service. Given the
Dorchester locus and the Gurnell family's documented Dorchester presence, (a) is the more
economical reading (~60/40). Residual action: Suffolk probate original of Margery Laver/Leaver
(1664) for exact spelling; check Dorchester church/town records for Jane Gurnell/Gurnet.
Do NOT promote a new G13-family "Jane" without that image read.

(Also incidentally surfaced, out of scope: a Hartford, Conn. John Gurney m. Sarah Hubbard
2 Oct 1728, daughter Sarah b. 18 July 1729 — NEHGR 13:145–146, Hartford records; a separate
18th-c. Connecticut Gurney datum, park for the wider one-name map.)

### F7 — L-11 BREAKTHROUGH: the Braintree manuscript record stream read at image level — "Cheny" traces to a later pencil annotation; the fair copy's ink reads "John GIRNY, Senior"

Film: FamilySearch DGS **007009769** (Braintree town records; FS film 940974 series). FTS probes
scoped to this film (`q.groupName=007009769`): `+Grizell`→2, `+Cheny`→2, `+Girny`→0 (OCR reads
the fair-copy "Girny" as "Giry"/"Cheny" contexts), `+Gurney`→5 (all 1701–1839, later Braintree
Gurneys), `+Kidbee`→0. Images pulled full-res via das/v2, saved to
`sources/intake/dump-files/dump-2026-07-01-images/`. Accessed 2026-07-01.

1. **Marriage entry (19th-c. fair-copy register, page 174 "Marriages," ark `3:1:3QS7-8979-44FR`,
   file `braintree-ms-p174-marriages-...jpg` + crop `crop-girny-grizell-entry.png`):**
   ink main text reads: **"John Girny, Senior (and) Grizell ——X——, by Peter Brackett, 9mo 12,
   1661."** The bride's surname is left BLANK with a long dash and X (i.e., illegible in the
   17th-c. source the copyist worked from); "Girny" carries the copyist's underline convention
   used elsewhere on the page for uncertain readings. In the LEFT MARGIN a later pencil hand
   wrote **"Cheny / Kidbee"** — the same marginal-annotation pattern (pencil surnames beside
   blanks/uncertain names) appears down both pages. **The 1886 Bates print's "John Cheny Senior
   and Grizell Kidbee" therefore matches the pencil ANNOTATION, not the fair copy's ink text.**
   The copyist read the groom as GIRNY — an attested Gurney variant (cf. `search-variants.json`
   Girney/Girnye, Tudor-Stuart parish form). Pope 1900 ("called John Cheny... by a typographical
   error") aligns with the Girny/Gurney reading.
2. **Wife-death entry (17th-c. ORIGINAL town book deaths page, ark `3:1:3QS7-8979-4WF2`,
   file `braintree-ms-deaths-1661-...jpg` + crop `crop-wifedeath-1661-5x.png`):** the line reads
   "**[?]eny the wiffe of John [?]eny dyed the 7t Mo 20. 1661**" — the surname's initial
   letterform (both instances) is genuinely ambiguous between a secretary-hand "Ch" and "G"
   at 5x. NOT resolved by eye this session (deliberately not ground down — see §6 paleography
   packet spec). Note the film contains BOTH the original book and the fair copy.
3. **Grizell's first-family births page (fair copy, ark `3:1:3QS7-8979-478N`):** "Grizell Fell
   [Jewell] born the 15.2.1648, Mercy Fuell [Jewell] born the 19.1.1651, [___] born the
   14.2.1653, three children of Thomas Full [Jewell], Grizell his wife" — manuscript-level
   record of Grizell's Jewell family at Braintree (matches the Pope/Torrey Jewell→Griggs→
   Kibbee→Gurney→Burge chain).
4. **Prosopographic argument to write up:** the Cheny reading requires a "John Cheny, Senior"
   resident at Braintree in 1661 — no John Cheney family is otherwise attested in Braintree
   town records (Pope evidently checked; the known John Cheney was of Roxbury→Newbury). The
   Gurney reading fits: John's first wife's death 20 (7) 1661 immediately precedes the
   12 (9) 1661 remarriage; Peter Brackett (officiant) is John Gurney's documented associate
   (Billerica right-holder 1659, Thayer-deed witness 1661/2, estate creditor 1663); and the
   1663 probate follows. Weight now strongly favors Gurney (~85–90%) with the letterform
   packet as the residual.
5. Later Braintree Gurney pages in the same film flagged for the G11/G12 side (not read this
   turn): arks `3:1:3QSQ-G979-4W1D` and `3:1:3QSQ-G979-449L` (both dated ~1701), `-47CM` (1803),
   `-4WLT` (1804), `-4W67` (1839).

### F8 — FTS colony-level probe set (Mass Bay / State Archives films): no new John Gurney document; the "+meadow" hit is the volume index

JSON-API probes (authenticated, fullName baseline 348,392): `+Gurny +meadow`(13), `+Gurney
+meadow`(5,739), `+Gurny +Braintree`, `+Gurney +Braintree`, `+Gurny +Weymouth`, `+Gurney
+Weymouth`(4,629), `+Gurnie +Weymouth`, `+Gurny +petition`(224), `+Gurny/+Gurney +Hingham`,
`+Surney`(11,005 — noise, mostly Surrey/Sur- OCR), `+Garney +Mendon`(156 — the 18th-c. Mendon
Garney/Gurney descendants, 1739–1779 probate/land, arks logged in session), `+Gurnett
+Braintree`. Pre-1800 Massachusetts residue beyond known documents:
- `3:1:3QHV-V3DW-8999-G` ("1642–1649", Mass Bay colony records film) = the volume's analytical
  INDEX page reading "Gurny, John, 79" (meadow/Hingham are other index entries on the same
  page) — confirms the 1644 bill (p. 79) is the only Gurny in that volume; no new record.
- The 1645/1673-labelled "Military" hits = the KNOWN Mass Archives calendar images 947–948
  (gunpowder petition calendar, L-186). No new colony-level Gurney document surfaced by FTS.
- Braintree "new plantation" probes: `+Braintree +"new plantation"` (99) — colonial-era hits
  incl. `3:1:3QS7-L979-WWPY` (1657, US-MA Properties) and `3:1:3QHV-J3DW-8GYM` (1650–1660,
  Mass Bay colony records) flagged for a later read (Mendon-plantation / 1645-petition
  context); `+Braintree +meadowes` (11) — hits are Suffolk-deeds pages already known
  (3QS7-L9ZS-B2V7 = Lib. IV p.6 Tyng recital; 3QSQ-G9ZS-BVGP = Lib. V p.229) plus 1664/1690
  legal items worth one look (`3Q9M-C9YP-P29C`, `-P29P` (1664), `3Q9M-C9Y5-G2CF`,
  `3QS7-L9ZS-B6LD` (1690)).
- **Pope's "[Arch. 45]" 1646 meadows petition did NOT surface** under any Gurn-variant or
  token-anchored probe — consistent with Mass Archives vol. 45 (Lands) either not being
  FTS-covered or its OCR shattering the name. The volume-level pull remains open — see §6.

### F9 — FLAGSHIP: Brampton Gurdon to John Winthrop, 20 Oct 1627 — the West Barsham Gurney heir ("yong mr. gurney," b. c. 1607) inside Winthrop's personal network, four years before the Great Migration [T8 — MAJOR Candidate-B network finding]

Source: **Winthrop Family Papers Digital Edition** (Massachusetts Historical Society), document
**PWF01d256** — Brampton Gurdon to John Winthrop, dated "morly this 20 of 8ber [Oct] 1627";
editors' citation "W. 1. 29; L. and L., I. 220" (= *Winthrop Papers* vol. I p. 29 range; Life
and Letters I:220). URL: masshist.org/publications/winthrop/index.php/view/PWF01d256. The ONLY
Gurney-variant document in the whole digital edition (searches: gurney=1, gurny=1, gurnie=1 —
same document; girny/gourney=0). Accessed 2026-07-01.

Verbatim (from the digital edition text):

> "To my worthy good frend mr. winthrop at his chamber in the tempule lane near the cloyster
> giue thes. Good Sir let me intreat your favour to this bearrer mr. warford, who is a master
> of artes of 6 years standing, he haue spent 8 years hear in my brother Sedlyes house as a
> skolmaster whearin he haue wele aproued of him selfe. I haue some few tymes hard him preach
> in publick and often I haue hard him pray in the family for which he desaruethe wele to be
> aproued. my request is that you will helpe him in his seut to the master of the wardes, he
> hathe a presentatyon from **mrs. Gurny who is gardyon to her sonn who wantethe a few monthes
> of being of ful age** I know the master haue right to present **yong mr. gurney commethe with
> him to manyfest his good will for the furthering of** [Warford's suit] ... I pray be helpfule
> to mr. warford that he may be kindly delt with by the officers vnder whom he must pas. And so
> in hast with my commendatyons to yow and to mr. Downing ... Your verry louing frend Brampton
> Gurdon. morly this 20 of 8ber [1627]"

Editors' notes: "morly" = **Morley, co. Norfolk** ("my brother Sedlyes" = Martin Sedley the
younger of Morley, brother of Muriel, Brampton Gurdon's wife; cites Visitation of Norfolk
H.S. XXXII:243 and Muskett p. 285). Winthrop was at this date an attorney at the **Court of
Wards and Liveries** (his chamber in the Temple); "mr. Downing" = Emmanuel Downing, his
brother-in-law and fellow Wards attorney.

**Identification (to verify, but the fit is tight): "yong mr. gurney" = Edward Gournay of
West Barsham (d. 6 Aug 1641), John G13's first cousin under Candidate B.**
- Age: "wantethe a few monthes of being of ful age" in Oct 1627 → born c. late 1606–1607.
  The West Barsham chancel brass (Farrer, *Church Heraldry of Norfolk* II; Armstrong 1781)
  reads Edward Gournay d. 6 Aug 1641 "aetatis suae 33" → born c. 1607–08. **Match.**
- Wardship structure: Edward was son and heir of **Thomas Gurney III** (Henry G15's eldest
  son) and **Martha, daughter of Sir Edward Lewkenor of Denham, Suffolk**. A minor heir with
  his mother as guardian in 1627 requires Thomas III dead by then — consistent with the
  senior-branch chronology on `research/places/west-barsham.md` (Edward succeeded as the
  West Barsham heir; Henry G15 d. 1623). "Mrs. Gurny" = the widowed **Martha (Lewkenor)
  Gurney**. A Court of Wards wardship implies tenure in capite/knight service — fits the
  armigerous West Barsham estate.
- The presentation: the wardship estate carried an advowson; the widow presented Gurdon's
  protégé Warford; because the heir was in ward, the **Master of the Wards** had the formal
  right — hence the suit, and Winthrop as the family's court contact.
- Geography: written from **Morley, Norfolk — ~4 miles from Great Ellingham and Hingham,
  ~2 miles from Deopham** — the exact S-central-Norfolk Gurney gentry heartland (and the
  Hingham-corridor emigration heartland; cf. L-188).

**Why this matters for G13 (network-level, not identity-level):**
1. It is the first documented **personal link between the Candidate-B Gurney family and the
   Massachusetts Bay founding leadership**: the West Barsham Gurneys' widow and heir were
   working through Brampton Gurdon (Assington, Suffolk — leading puritan patron whose daughter
   Muriel married Richard Saltonstall Jr. 1633) to John Winthrop himself in 1627. Martha
   Lewkenor's Denham family were front-rank Suffolk puritans.
2. Under Candidate B, the 1636 Newgate-apprentice hearing was "before the governor" — Winthrop.
   The apprentice-John and Braintree-John questions aside, a Gurney youth appearing in
   Winthrop's Boston in the 1630s–41 would land in a colony whose governor personally knew the
   family's senior branch. It converts the "why Massachusetts?" question for a Norfolk Gurney
   from anomaly to network-consistent.
3. It supplies a NEW record class for the English side: a **Court of Wards wardship of Edward
   Gournay (father Thomas Gurney III, d. by 1627)** must exist in TNA WARD series (WARD 9
   miscellanea, WARD 7 inquisitions) — a dated, name-rich estate record of the senior branch
   in exactly the decade the emigrant left. Also a lead on the Blomefield "Edmund/Frances
   Hovell vs Edward/Martha Lewkenor" senior-branch tangle (the wardship file would name the
   father outright).
4. Mr. Warford (M.A., 8 years schoolmaster in Martin Sedley's Morley household, preacher):
   identify him and the living presented — candidate advowsons: West Barsham, Irstead, Great
   Ellingham-orbit livings. If Warford's institution is found (Norwich diocese institution
   books, c. 1627–28), it names the patron and the living — anchoring which advowson the
   wardship estate held.

### F10 — Records of the Suffolk County Court 1671–1680 (CSM Pubs 29–30, free at colonialsociety.org): an unresolved "Gurney, ——, 481" index entry [T-new — less-traveled source, partially worked]

The two-volume Suffolk County Court records (Boston sessions Oct 1671–Apr 1680) are online in
full at colonialsociety.org (vol 29 TOC = node/637; vol 30 TOC = node/274; General Index =
node/329). General Index Gurney-adjacent entries (read 2026-07-01): "Garner, Thomas";
"Garnitt, John"; "Garnsey, see Gearnsey" (Henry — juror; John); "Gornell / Gurnell, John —
party" (the Rawson v. Glover guardianship, 28 July 1674 session, vol 29 pp. 252–253, node/694
— John Gurnell was a court-appointed guardian of Nathaniel Glover's children — the DORCHESTER
Gurnell family again, which further supports reading the 1664 "Jane Gurnet" (F3) as
Gurnell-orbit); "Gurnell. See Gornell"; and **"Gurney, ——, 481"** — a Gurney with NO forename
at printed page 481.
- p. 481 could not be matched to a session node this session: all vol-29 session nodes
  1675–1678 (nodes 290, 298, 299, 300, 303, 305, 306, 308, 310, 312, 313, 314, 315) were
  fetched and contain no Gurn-variant string; node 303 (25 Apr 1676) carries a printed-page
  marker [368]. Either the online transcription renders the p. 481 name differently, or the
  entry sits in a session/footnote node not swept. Given ~p.368 = Apr 1676, p. 481 likely
  falls c. Jan 1676/7–Jul 1677 — the window of PETER GURNEY's King Philip's War death
  (Dec 1676) — so this may be a Peter-related (or Isaac-related) court item. **Concrete
  follow-up (§6): read the printed page 481 via HathiTrust (catalog record 006784537 —
  bot-gated to automation this session) or walk CSM nodes 308/310/312 footnotes manually.**

### F11 — Hingham arrival-vector delta (L-188): Hobart journal route identified but gated; FTS manuscript-level Hingham negative reinforced

- **Rev. Peter Hobart's journal** (Hingham baptisms/marriages/deaths 1635–1679, the closest
  thing to Hingham parish registers) is published serially in **NEHGR vol. 121 (1967)** and on
  AmericanAncestors (subscription) — the free rootsweb page (homepages.rootsweb.com/~hobart/
  hobart/hobart_journal.htm) is HOBART-FAMILY EXCERPTS ONLY (verified: 18.7K chars, zero
  Gurney-variant, explicitly excerpt-scoped) and is NOT usable as a Gurney negative. The
  journal remains the single best untested Hingham source for a transient Gurney presence
  1638–41. → §6 human/gated list.
- FTS probes `+Gurney +Hingham` (3,607 global) and `+Gurny +Hingham` (11) yield ZERO pre-1800
  Massachusetts Hingham-town hits beyond the known Mass-Archives calendar pages — a
  manuscript-level reinforcement of the compiled-source "no Gurney in Hingham" negative
  (coverage caveat: FTS coverage of the Hingham town books not separately confirmed).

## 4. Negative results ledger (consolidated; all 2026-07-01, variant net per §1)

| Source (identifier) | Coverage | Result |
|---|---|---|
| Aspinwall Notarial Records, Boston 1644–51 (`volumerelatingto32bost`) | body + index | NO Gurney any variant (Garnett Samuel of Southwark = distinct) |
| Lechford Note-Book Jun 1638–Jul 1641 (`notebookkeptbyth00lech`) | body + index | NO Gurney any variant (Robert Garnill = distinct) — the arrival-window Boston lawyer never touched a Gurney |
| Court of Assistants MBC records, 3 copies (`recordscourtass01crongoog`, `recordsofcourtof02massuoft`, `recordsofcourtof03mass`) | body + index | NO Gurney (re-verify volume mapping before promoting) |
| MBCR v1 (`recordsofgoverno01mass`) | full sweep | only 1:331 (1641 fine remission) |
| MBCR v2 (`cu31924091024582`) | full sweep | only 2:79 (1644 Gurny/Lake bill); Gurnell 2:293 distinct |
| MBCR v3, v4pt1, v4pt2 (`recordsofgoverno03mass`,`-41mass`,`-42mass`) | full sweep | ZERO Gurney 1644–1674; May-1645 Braintree petition not printed under his name; **John G13 never admitted freeman** |
| MBCR v5 (`recordsofgoverno05mass`) | full sweep | only Richard Gurney 5:540 (1681 freemen, F5); Gurnell/Burg distinct |
| Plymouth Colony Records vols 1–8, 11–12 (6 combined items) | full sweep incl. "Surney" recheck | ONLY Isaac 1663/4 (PCR 4:51) + the Ruth Surney×Bundy marriage return (PCR 8, Taunton, F2); no other Gurney in the whole Plymouth record |
| Suffolk Deeds Libers I, II, III, VI (`suffolkdeeds01/02/03/06suff`) | body + index | NO John Gurney deed 1640–1660s; Gurnell (Dorchester), Gornell (Boston, Mount Wollaston 112A — likely Cornell), Garnett (Braintree-area) all distinct; "Gurner, James, I:5" = John-and-Sara Scottish POW list (F4) |
| Winthrop Family Papers Digital Edition (masshist.org) | site search, 5 variants | exactly ONE Gurney document — PWF01d256, the 1627 Gurdon letter (F9) |
| Braintree town-record film DGS 007009769 | FTS scoped probes | no 17th-c. Gurney beyond the F7 pages; +Gurney hits are 1701+ (arks logged F7.5) |
| Hobart-journal rootsweb excerpts | full page | not a valid negative (excerpts only, F11) |
| CSM colonialsociety.org site (Google-indexed) | site: searches | no colonial Gurney beyond F10's index entry + Gurnell 1674 |

## 5. Recommended repo changes (do not edit repo this turn)

1. **G13 companion, Grizzell section (L-11):** add Pope's typo ruling (F1), the fair-copy
   "John Girny, Senior" image reading + pencil-margin provenance of "Cheny/Kidbee" (F7),
   and re-weight the Braintree-record conflict toward Gurney (~85–90%); keep the letterform
   packet as residual. Cite: Pope p. ~204 (GURNET entry); DGS 007009769 arks 3QS7-8979-44FR
   (marriages p.174), 3QS7-8979-4WF2 (deaths, original book), 3QS7-8979-478N (Jewell births).
2. **G13 companion / case file (Candidate B evidence set):** add F9 (Winthrop–Gurdon 1627
   letter; West Barsham heir in Winthrop's Wards orbit; Morley/Sedley/Lewkenor/Gurdon-
   Saltonstall network) as a network-level Candidate-B supporting item. Consider a small
   probability nudge or at least a "reception/network" subsection alongside the
   immigration-by-association topic file.
3. **G13 companion, colonial chronology:** add Pope's "[Arch. 45]" 1646 meadows petition as a
   distinct record row (pending the vol-45 pull, L-191-adjacent); state the John-never-freeman
   finding (from the full MBCR sweep) as a social-status datum beside the mark-signature.
4. **G12 companion:** pin "Freeman 1681" to MBCR 5:540 (F5).
5. **John Jr. / Mendon line:** correct/confirm Ruth (not Jane) Bundy remarriage with the PCR 8
   verbatim + Taunton VR duplicates (F2); add Elizabeth Gurney m. Timothy Cooper (Taunton
   1706) as an unplaced probable John-Jr.-line descendant; flag the Bundy 1681 probate check.
6. **`data/search-variants.json` (Modern family, broad):** add colonial-attested forms
   **Garney** (already present — confirm), **Surney** (PCR 8 primary; S/G corruption),
   **Gurnet / Gornet** (Pope head-forms; collision: the Gurnet headland), and consider
   **Girny** exposure for colonial-era searches (currently only in English-family notes).
7. **Topic/methods:** add the §0 county roll-up scope map (Suffolk 1643 = the county for all
   of John's towns; "Old Norfolk" false friend; Plymouth-Colony boundary for Scituate) to a
   colonial-records methods note or the immigration-by-association topic.
8. **Leads catalog:** L-193 → major progress (this dump = the survey + sweeps; residual:
   First Church records, Arch-45); L-11 → near-resolution (residual: letterform packet);
   L-188 → Hobart journal gated-residual; new leads: CSM Suffolk-court p. 481 (F10), Court of
   Wards WARD 7/9 wardship of Edward Gournay (F9.3), Warford institution (F9.4), Margery
   Laver 1664 Suffolk probate original (F3).

## 6. Human-required / gated / outsourced follow-ups

1. **NEHGR 121 (1967) Hobart journal** — AmericanAncestors subscription (or NEHGS library):
   sweep all installments for Gurney variants 1635–1679 (the Hingham arrival test, L-188).
2. **CSM Suffolk County Court p. 481 "Gurney, ——"** — HathiTrust search-inside (catalog
   006784537; Cloudflare-gated to automation) or manual read of CSM nodes 308/310/312 (Jan
   1676/7–Jul 1677 sessions incl. footnotes); likely Peter- or Isaac-related (F10).
3. **Massachusetts Archives Collection vol. 45 (Lands, 1622–1726)** — the 1646 Braintree
   meadows petition with John Gurney's signature (Pope "[Arch. 45]", F1). Routes: FamilySearch
   films of vols 1–239 (linked from sec.state.ma.us volume list; use vol 45's own name index
   at front), or the Massachusetts Archives Digital Repository (digitalarchives.sec.state.
   ma.us). This is a signature-bearing document — if found, ALSO a second John-Gurney
   signature/mark exemplar for the paleography file.
4. **Paleography packet — Braintree Cheny/Girny letterforms:** using the three staged images
   (dump-2026-07-01-images/): compare the deaths-page "?eny" initial (both instances, crop
   provided) against the same scribe's uncontested G- and Ch- words on the same opening;
   also read the fair-copy underline conventions across pp. 174–175. Decide Gurny vs Cheny
   at letterform level. (Original book AND fair copy are both in DGS 007009769.)
5. **Court of Wards, TNA:** WARD 7 (inquisitions) / WARD 9 for the wardship of Edward Gournay
   son of Thomas Gurney III (d. by 1627), c. 1615–1628, Norfolk — would date Thomas III's
   death, name the estate and guardian (expect Martha née Lewkenor), and possibly the
   advowson (F9). Offline/TNA.
6. **Norwich diocese institution books c. 1627–29** — institution of Mr. Warford to a living
   on a Gurney presentation (identifies the advowson; F9.4). Possibly via NRO/CCEd (CCEd is
   online — a future AI turn could try clergydatabase search for Warford).
7. **Boston First Church records (CSM Pubs 39–41, 1961)** — not freely online; check NEHGS/
   library for any Gurney/Gurnell admission or baptism 1630–1665 (Anderson "Boston" test
   residual; L-193).
8. **Bundy probate, Taunton/Plymouth 1681** — whether John Bundy's estate papers name Gurney
   stepchildren (F2 follow-up).

## 7. Source tracking (citation-ready)

- Pope, Charles Henry. *The Pioneers of Massachusetts* (Boston, 1900): GURNET/GORNET main
  entry (~p. 204 of print; djvu lines 27264–27280); BUNDY entry; LAVER entry; index
  cross-refs. Archive.org `pioneersofmassac00pope`. Accessed 2026-07-01.
- *Records of the Colony of New Plymouth*, ed. Shurtleff/Pulsifer: vol. 8 p. ~60 (Taunton
  returns): "John Bundey married to Ruth Surney, of Mendum, this 9th of January, 1676";
  vol. 4 p. 51 (Isaac 1663/4). Archive.org `recordsofcolonyo0708newp`, `recordsofcolonyo0304newp`.
- *Vital Records of Taunton, Massachusetts, to the year 1850*, vol. 2 (Marriages): BUNDY/
  GURNEY/GARNEY/SURNEY entries as quoted in F2. Archive.org `vitalrecordsofta02unse` (also
  `vitalrecordsoftataun_5`).
- *NEHGR* 13 (1859): p. 13 (Margery Laver will abstract, "to Jane Gurnet, 2s for a
  memorandum"); pp. 145–146 (Hartford Gurney 1728–29); p. 254 (Taunton marriages, Cooper×
  Gurney 1706). Archive.org `newenglandhistor1318unse`.
- *Records of the Governor and Company of the Massachusetts Bay*, vols 1–5 (Shurtleff):
  sweeps as in §4; v5 p. 540 Richard Gurney. Archive.org ids in §4 table.
- Suffolk Deeds Libers I–III, VI (printed): sweeps as in §4; Lib. I pp. 5–6 John-and-Sara
  Scots list ("James Gurner"). Archive.org ids in §4 table.
- Aspinwall Notarial Records (Boston Record Commissioners vol. 32); Lechford Note-Book;
  Court of Assistants records — ids in §4 table.
- FamilySearch film DGS 007009769 (Braintree town records): arks 3:1:3QS7-8979-44FR,
  3:1:3QS7-8979-4WF2, 3:1:3QS7-8979-478N (images in `dump-2026-07-01-images/`); later-Gurney
  arks in F7.5. FTS JSON-API probes as logged in F8. Accessed 2026-07-01 (authenticated).
- Winthrop Family Papers Digital Edition, MHS: document PWF01d256 (Brampton Gurdon to John
  Winthrop, 20 Oct 1627, from Morley, Norfolk), with editors' notes. URL in F9.
- Colonial Society of Massachusetts, *Publications* 29–30 (Records of the Suffolk County
  Court 1671–1680): General Index node/329 ("Gurney, ——, 481"; Gornell/Gurnell entries);
  session node/694 (Rawson v. Glover, 28 Jul 1674, vol 29 pp. 252–253). colonialsociety.org.
- Massachusetts Archives volume list (sec.state.ma.us): vol 45 = "Lands, 1622–1726," with
  name index; FamilySearch film links for vols 1–239.
- Hobart journal availability: NEHGR 121 (1967) / AmericanAncestors; rootsweb excerpts page
  (Hobart-family-only).
