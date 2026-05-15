# Intake patchset v36 - Candidate D v35 amendments and v13 gap-fill

```yaml
patchset_id: v36
created: 2026-05-14
repo_scope: gurney-genealogy
phase: phase_2_amendment_and_gap_fill
input_packets:
  - sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
  - sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-ai-ready-v15.md
depends_on:
  - v32-john-gurney-candidate-d-source-foundation.patchset.md
  - v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md
  - v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md
  - v35-john-gurney-case-file-candidate-d-section-8.patchset.md
phase_2_rule: Apply this patchset AFTER v34 and v35. Sections 1-4 supersede the corresponding sections of v35 (without editing v35). Sections 5-7 add the v13 facts and findings that v34 did not capture into research.
supersedes:
  - v35 Section 1 (Section 8 row insertion) - shortened row
  - v35 Section 2 (Section 8.4 subsection) - conclusion-first rewrite with technical detail moved to footnotes
  - v35 Section 3 (Section 11 row insertion) - unchanged, but explicitly preserved here
extends:
  - v35 by adding a Section 8 candidate-table region-sort reorder operation
  - v34/v35 by adding Section 13.2 Primary Source Records entries for Candidate D
  - v34 by filling the v13 gap (Boyd cards 1-3, Robert will full transcription, Harleian St Vedast / St Michael le Quern findings, Grine/Grone/Grene comparators)
```

## 0. Scope

This patchset does two things.

**Optimization of v34/v35 case-file work.** Four targeted improvements to the Candidate D case-file edits:

1. Shortens the Section 8 candidate-table row for Candidate D so its Primary Elimination Reason cell is under ~20 words. Content moves to Section 8.4.
2. Rewrites Section 8.4 conclusion-first and shifts record-analysis detail (image-level reads, MS. 67a label, TNA E179 reference) into footnotes.
3. Reorders the Section 8 candidate-table so that immediately after Candidate D, the non-eliminated comparator rows come first (sorted by region, then by parish), then the eliminated rows (sorted by region, then by parish). Word content of each row is preserved verbatim.
4. Adds three Section 13.2 Primary Source Records entries for the Candidate D source set.

**Audit gap-fill.** Three substantive content blocks from v13 that v34 did not migrate into research files are landed now:

5. The full semi-diplomatic Robert Gurney 1625 will transcription, including witness clause and probate clause, plus the prior-pass uncertainties about the duplicate-looking shop/cellar/hall passage, appended to the Candidate D topic file.
6. A new London Gurney comparator research file covering Boyd cards 1-3 (Dorothy Reading, William Shipman / Mary Garney, Jane/Joan Waring grocer), the Harleian St Vedast / St Michael le Quern findings (Anne Gourney 1626, Richard Cobham + Jane Gurney 1658, Joshua Little + Elizabeth Gurney 1728 with the St Stephen Coleman Street reading, Elizabeth Gurney wife of Sir Richard Gurney monument, Hannah Gurney burial), the pre-1666 St Michael le Quern register-loss note, and the late 1764 Ann Morris of St Michael le Quern marriage anti-conflation guard.
7. A new London Grine/Grone/Grene comparator research file covering Jhon Grine St Mary-at-Hill 1603/4, John Grone St Magnus 1625 exclusionary, John Grine + Mary St Swithin London Stone 1640/1, John Grone St Giles Cripplegate 1630, John Grene son of Jeames Grene St Mary Magdalen Old Fish Street 1634, John Grene son of Robart Grene All Hallows Bread Street 1600, John Grene son of Rich Grene St Mary Whitechapel 1610/11.

The audit checklist at the end of this patchset confirms every block of v13 substantive content is captured in research files after v34, v35, and v36 are applied in order.

## 1. Section 8 candidate-table row for Candidate D (supersedes v35 §1)

When v35 §1 directs insertion of a Candidate D row after the Candidate C row and before the Aylesbury (John + Anne Cowheard) row, use this shorter row instead. The full content moves to Section 8.4 (rewritten in §2 below).

```markdown
| **Candidate D** | St Augustine Watling Street and Old Change, London | Unknown | **Unlikely (~3-5%)** | London Drapers' father-son; continuing London record set through 1638 and (cued) 1661; no matching wife or children (see 8.4). |
```

## 2. Section 8.4 subsection (supersedes v35 §2)

Use this rewritten subsection in place of the v35 §2 text. Insertion location is unchanged: immediately after Section 8.3 and before the Section 9 H2.

```markdown
### 8.4 Candidate D — London Drapers' / Old Change

Candidate D is held as Unlikely (~3-5%) as the Massachusetts emigrant. The Old Change household meets the "father in a textile trade" criterion that previously favoured Candidate B alone, but post-1625 evidence keeps John Gurney in London through at least 1638 and probably 1661, with no wife Mary and no matching child set.

Candidate D is John Gurney, son and executor of Robert Gurney, citizen and draper of London, of Old Change. John was admitted to the Drapers' Company by redemption on 11 February 1623/4 and proved Robert's will on 23 September 1625.<sup class="fn"><a href="#n92" id="ref-92a">92</a></sup>

Robert was a Drapers' freeman from 16 December 1581 and described as a tailor at Old Change from his admission. He worked as a Drapers' apprenticeship- or freedom-master across about 14 events between 1597 and 1622 and bound apprentices from Buckinghamshire and Yorkshire. He married Anne Morris by licence at St Magnus the Martyr on 4 April 1611, after an earlier wife produced three children at St Augustine in the 1590s.<sup class="fn"><a href="#n92" id="ref-92b">92</a></sup>

John was admitted by redemption rather than patrimony, despite Robert's long-standing Drapers' freedom. The cleanest explanation is that John served apprenticeship in a different company before taking up the family business. A 1613 Stationers' record places a John Gurney apprentice to master James Boler with no later Stationers' freedom; if this is the same John, the 1623/4 Drapers' redemption is the natural consequence, and Robert's choice of the Stationer Joseph Henscott as a will overseer becomes a professional courtesy rather than a coincidence.<sup class="fn"><a href="#n92" id="ref-92c">92</a></sup>

On 3 November 1630, John Gurney bound Henry Smith of Kilton, Suffolk, as a Drapers' apprentice for seven years. Smith does not surface as a freed Drapers' Smith 1635-1645, and no Drapers' turnover for any Gurney is recorded 1620-1670, so the trail terminates without confirmation of John's residence at completion.<sup class="fn"><a href="#n92" id="ref-92d">92</a></sup>

The 1638 T. C. Dale St Augustine return lists John Gurney at £10. On the same return, Joseph Huntscott appears at £12. Huntscott is the documented Stationer Joseph Hunscott — an active apprenticeship master 1612-1646, the father of John Hunscott (Stationer 1641), and the author of the 1646 royalist petition Wing H3728 — who was named overseer in Robert's 1625 will. The Robert Gurney will-network was still in the same parish thirteen years after his death; the most economical reading is that the 1638 John Gurney is the John who took the Old Change shop under that will.<sup class="fn"><a href="#n92" id="ref-92e">92</a></sup>

Boyd's Inhabitants of London card for John Gurny of S Augustine carries a partly-legible free-note reading "1661 poll tax [unclear] Old Change." If a Gurney entry can be confirmed at Old Change in 1661, Candidate D is essentially eliminated as the Massachusetts John, who died at Boston about March 1662/3. No image has yet been retrieved.<sup class="fn"><a href="#n92" id="ref-92f">92</a></sup>

Robert's will preamble uses Reformed vocabulary ("elect children of God") consistent with a godly-Protestant milieu but too weak to prove nonconformity. No Puritan minister, lecturer, Coleman-Street-network associate, or Massachusetts bridge appears in the Old Change record set. No London-parish marriage of John Gurney to a wife named Mary, and no baptisms of Sarah, Mary, Richard, John, or Peter to a John Gurney + Mary household 1620-1641, have been located; the closest John Gurney + Mary marriage in window (Eythorne, Kent, 6 November 1632 to Mary Marsh) belongs to a Kent couple who stayed in Kent.<sup class="fn"><a href="#n92" id="ref-92g">92</a></sup>

Depth is in `research/people/john-gurney-candidate-d.md` (full Drapers' corpus, Hunscott identity bridge, family reconstruction, gaps). Cross-link summary at `research/people/g13-john-gurney-fact-sheet.research.md`.
```

### 2.1 Footnote definitions

Replace the v35 §2 footnote definition with these denser, more technical footnotes. Each absorbs the image-level and reference-number detail that the body no longer carries.

```markdown
[^n92a]: <a id="n92"></a>Robert Gurney, citizen and draper of London, will written 18 January 1621/2 and proved 23 September 1625, Archdeaconry Court of London; user-supplied image `31787_A002570-00422.jpg`; Source ID `acl-robert-gurney-will-1625`. ROLLCO Drapers' Company event DREW5638 (11 February 1623/4 freedom by redemption, John Gurney new freeman, Robert Gurney father of freeman in the same event row); Source ID `rollco-drapers-gurney-old-change-cluster`.

[^n92b]: ROLLCO Drapers' Company events for Robert Gurney 1581-1622: DREW4826 (16 December 1581 freedom by servitude, "Tailor, Old Change", master Robert Furnes — corrects the Boyd card 5 reading "Robert Mason[?]"); DREB5398 (1597 freedom master); DREB972, DRHT2178, DREB6664 (1603-1604 apprenticeship master events); DRLL837 (1 August 1604 freedom witness "Tailor, Old Change", new freeman Richard Sebrineke by servitude); DREB6662 and DREB3081 (1605 freedom and apprenticeship master events); DREW68 (1609); DREB6663 (1611 freedom master); DRLL2652 (1612 apprenticeship master); DREB2377 and DRHT1660 (1614 freedom and apprenticeship master events); DRHT1669 (1617 apprenticeship master "tailor, Old Change", new apprentice John Lee of Shenley Bucks, father Edward Lee yeoman, 7-year bond); DREW7982 (30 May 1622 apprenticeship master, new apprentice William Holdsworth of Sowerby Bridge Yorkshire, father William Holdsworth tailor, 7-year bond); Source ID `rollco-drapers-gurney-old-change-cluster`. St Magnus the Martyr marriage register, 4 April 1611, Robert Gourney of St Augustine in Watling Street and Anne Morris of St Michael in the Querne by licence; user-supplied image `31281_a101911-00014.jpg`; Source ID `lma-st-magnus-martyr-register-candidate-d-images`. St Augustine Watling Street parish register, 1595-1601 child events (John bapt 18 February 1595/6, Marye bapt 12 March 1597/8, stillborn son bur 8 April 1601); Source ID `lma-st-augustine-watling-register-candidate-d-images`.

[^n92c]: ROLLCO Stationers' Company event STMM8981, 25 March 1613 apprenticeship, master James Boler Co Stationer, new apprentice John Gurney, reference ST/1:0812; no recorded subsequent Stationers' freedom under Boler; no father field captured by ROLLCO; Source ID `rollco-stationers-gurney-1613-1626`. Hypothesis H-D1 detail in `research/people/john-gurney-candidate-d.md`. Robert Gurney's 1625 will named Joseph Henscott, stationer and citizen of London, as one of two overseers (Thomas Dunnell, brother-in-law, was the other); Source ID `acl-robert-gurney-will-1625`.

[^n92d]: ROLLCO Drapers' Company event DRLL2060, 3 November 1630 apprenticeship, master John Gurney, new apprentice Henry Smith, father Thomas Smith yeoman (deceased) of Kilton Suffolk, 7-year bond. ROLLCO Drapers' surname Smith forename Henry 1635-1645 search returned a different Henry Smith (master Thomas Faroe, father Henry Smith Citizen and Innholder deceased of London, freed 1639 by servitude, event DRLL2058). No Drapers' turnover events involving any Gurney 1620-1670 (event_type filter sweep). Source ID `rollco-drapers-gurney-old-change-cluster`.

[^n92e]: T. C. Dale, "Inhabitants of London in 1638: St. Augustine," in *The Inhabitants of London in 1638* (Society of Genealogists, 1931), British History Online, https://www.british-history.ac.uk/no-series/london-inhabitants/1638/pp34-35; the return is a rents/tithe assessment in three manuscript sections (MS. 67, MS. 67a, MS. 68); total £1,700 yielding £233 5s tithe at 2/9 per £; John Gurney in MS. 67a at £10 between Christopher Hunlock £2 and George Browne £10; Joseph Huntscott in MS. p. 68 at £12; Source ID `bho-london-inhabitants-st-augustine-1638`. ROLLCO Stationers' Company event corpus for Joseph Hunscott 1612-1646 (14 events as apprenticeship master, plus 1641 freedom event STMM... admitting son John Hunscott by servitude); Source ID `rollco-stationers-hunscott-cluster`. Joseph Hunscot, *The Humble Petition and Information of Joseph Hunscot Stationer, To the Honourable Houses of Parliament Assembled* (London, 1646), Wing H3728; Source ID `arber-stationers-bsoc-petition-1646-hunscott`.

[^n92f]: Findmypast Boyd's Inhabitants of London card `GBOR/BIL/SOG59/0240` (John Gurny of S Augustine) with free-note line "1661 poll tax [unclear] Old Change    1638 rent £10"; Source ID `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards`. The underlying 1660-1661 poll-tax record most likely sits in The National Archives, Kew, E179 series (especially the E179/253 sequence for the City) under the Free and Voluntary Present granted 8 July 1661 (13 Car. II); no online image confirmed in this pass; Source ID `tna-e179-1661-london-poll-tax-deferred`.

[^n92g]: Robert Gurney's will preamble ("the elect children of god in the kingdome of heaven") quoted in working packet v13 section 8 transcription; Source ID `acl-robert-gurney-will-1625`. FamilySearch records search, surname Gurney, given name John, spouse Mary, marriage 1620-1640 with marriage place England, returned 211 hits with no London-parish John Gurney + Mary marriage in window; closest in-window match is John Gurney + Mary Marsh at Eythorne, Kent, 6 November 1632, with a son John baptized Eythorne 13 May 1638 (incompatible with the colonial John family's first child Mary about 1628); Source ID `fs-england-births-christenings`.
```

If the case-file footnote pattern requires per-ref anchor IDs (n92a, n92b, ...), repeat each footnote with its specific anchor; otherwise keep the consolidated `<a id="n92"></a>` anchor on `[^n92a]` so all seven body references resolve to it.

## 3. Section 8 candidate-table region-sort reorder

After applying v35 §1 (modified by v36 §1 above) the Section 8 table runs Candidate B, Candidate A, Candidate C, Candidate D, then the same-name comparator rows in their current legacy order.

Replace the entire same-name section of the table (every row AFTER Candidate D's row and BEFORE the Section 8.1 H3) with the following block. Each row is pasted verbatim from the existing case-file; only the row order changes. The four labeled-candidate rows (B, A, C, D) stay where they are at the head of the table.

**Order: non-eliminated rows by region (alphabetical), then eliminated rows by region (alphabetical); within each region, alphabetical by parish.**

```markdown
| Aylesbury, Bucks (John + Anne Cowheard) | Buckinghamshire | **Anne Cowheard** | **Unlikely (~3%)** | Aylesbury marriage to Anne Cowheard 25 October 1638; no later record reached in the present pass. Wife name and 1638 timing make a colonial-John match unlikely (see 8.1).<sup class="fn"><a href="#n88" id="ref-88d">88</a></sup> |
| Cheddington, Bucks | Buckinghamshire | Unknown | **Unlikely (~3%)** | Johannes Gurney baptized 1608, son of Richard Gurney. |
| Hitcham, Bucks (John) | Buckinghamshire | Unknown | **Unlikely (~2%)** | Alive in 1631 England (Hitcham parish baptism); single primary record, mother and siblings unknown (see 8.3). |
| Norwich (m. 1639) | Norfolk | **Jane** Wright | **Unlikely (~3%)** | Wife Jane, not Mary. St Benedict, Norwich parish marriage 9 March 1639; no later record reached in the present pass. |
| Ackworth, Yorkshire | Yorkshire | **Mary** Barton (claimed) | **Unlikely (~2%)** | Yorkshire is outside the emigrant corridor; the 1636 Mary Barton / Burton marriage attribution is not supported by a primary record reachable in the present pass.<sup class="fn"><a href="#n86" id="ref-86b">86</a></sup> |
| Toddington, Beds | Bedfordshire | **Elizabeth** Moreton | **ELIMINATED** | Died in England (buried Toddington September 1641); wife Elizabeth, not Mary; non-matching children.<sup class="fn"><a href="#n90" id="ref-90">90</a></sup> |
| Winkfield, Berkshire | Berkshire | **Alice / Ellice** | **ELIMINATED** | Died in England (will proved 1682, PROB 11/372/123); yeoman.<sup class="fn"><a href="#n60" id="ref-60c">60</a></sup> |
| Aylesbury, Bucks (probate) | Buckinghamshire | **Sarah** (probable) | **ELIMINATED** | Died in England (probate sentence PROB 11/337/37).<sup class="fn"><a href="#n60" id="ref-60d">60</a></sup> |
| Chesham, Bucks (John + Elizabeth) | Buckinghamshire | **Elizabeth** | **ELIMINATED** | Died in England (buried Chesham July 1672 and 11 June 1678); wife Elizabeth (see 8.3). |
| Cublington, Bucks (John + Mary) | Buckinghamshire | **Mary** | **ELIMINATED** | Alive in 1664 England (son Isaac baptized Cublington); held Stewkley manor by 1687 (see 8.3). |
| East Claydon, Bucks (John + Elizabeth) | Buckinghamshire | **Elizabeth** | **ELIMINATED** | Died in England (buried East Claydon 17 April 1654); wife Elizabeth (see 8.3). |
| Haddenham, Bucks (John) | Buckinghamshire | Unknown | **ELIMINATED** | Alive in 1620-1622 England (Haddenham parish baptisms); fathering in 1620 requires a birth by about 1600, while the colonial John was born about 1603 (aged about 50 in 1653), making him only about 17 in 1620 and biologically incompatible with fathering (see 8.3). |
| Wing, Bucks (John + Anne) | Buckinghamshire | **Anne** | **ELIMINATED** | Alive in 1650-1652 England (Wing parish baptisms); wife Anne (see 8.3). |
| Maldon, Essex (bachelor) | Essex | (unmarried) | **ELIMINATED** | Alive in 1674 England (Essex hearth tax); bachelor; died in England 1681.<sup class="fn"><a href="#n65" id="ref-65">65</a></sup> |
| Albury, Herts | Hertfordshire | **Jane** | **ELIMINATED** | Died in England (will proved 1676, PROB 11/335/425); husbandman.<sup class="fn"><a href="#n60" id="ref-60f">60</a></sup> |
| Eythorne, Kent | Kent | **Mary** Marsh | **ELIMINATED** | Died in England (buried Eythorne 1648); married Eythorne 6 November 1632. |
| St Botolph Aldgate, London | London | **Mary** | **ELIMINATED** | Died in England (will proved 1666, PROB 11/382/271); merchant.<sup class="fn"><a href="#n60" id="ref-60b">60</a></sup> |
| St Giles Cripplegate, London (Francis B) | London | - | **ELIMINATED** | Died in England (buried St Giles Cripplegate as an infant aged 2 days, son of Francis B the laceweaver). |
| St Giles Cripplegate (Francis Garney joiner) | London | - | **ELIMINATED** | Died in England (buried St Giles Cripplegate December 1640, son of Francis Garney joiner).<sup class="fn"><a href="#n70" id="ref-70">70</a></sup> |
| Harrow on the Hill / Okington | Middlesex | **Mary** | **ELIMINATED** | Alive in 1669 England (Saint Mary Harrow parish burials of children); wife Mary.<sup class="fn"><a href="#n69" id="ref-69">69</a></sup> |
| Denton, Norfolk | Norfolk | **Rachell / Rachelle** | **ELIMINATED** | Wife is not Mary. Child Mary age does not align with the colonial Mary's 1620s birth window.<sup class="fn"><a href="#n87" id="ref-87a">87</a></sup><sup class="fn"><a href="#n89" id="ref-89a">89</a></sup> |
| Earsham, Norfolk | Norfolk | **Elizabeth** Singler | **ELIMINATED** | Died in England (will proved 1639).<sup class="fn"><a href="#n60" id="ref-60a">60</a></sup> |
| Hempnall, Norfolk | Norfolk | Unknown | **ELIMINATED** | Alive in 1640-1641 England (Hempnall parish baptisms of Anna 1640 and Elizabeth 1641; earlier Anna buried Hempnall 6 April 1639).<sup class="fn"><a href="#n87" id="ref-87b">87</a></sup> |
| Norwich, Saint Peter Mancroft | Norfolk | - | **ELIMINATED** | Died in England (buried Saint Peter Mancroft, Norwich 10 February 1639).<sup class="fn"><a href="#n91" id="ref-91">91</a></sup> |
| East Chiltington, Sussex | Sussex | Unknown | **ELIMINATED** | Died in England (probate PROB 11/241/246 and PROB 11/242/723); shepherd.<sup class="fn"><a href="#n60" id="ref-60g">60</a></sup> |
| East Grinstead, Sussex | Sussex | **Dorothy** | **ELIMINATED** | Died in England (will proved 1654, PROB 11/252/319); yeoman.<sup class="fn"><a href="#n60" id="ref-60e">60</a></sup> |
```

Row count check: original same-name rows in the table are 26 (lines 249-274 of the v4 case file). The reordered block above contains 26 rows. No row dropped, none added, no word changed.

## 4. Section 13.2 Primary Source Records additions

Append the following three rows to the existing Section 13.2 numbered table immediately after row 11 (the existing "John Gurney burial - Elm Street Cemetery, Braintree" row).

```markdown
| 12 | Robert Gurney will, 1625 (Candidate D anchor) | Archdeaconry Court of London; image `31787_A002570-00422.jpg` | Will/probate ★ |
| 13 | ROLLCO Drapers' Company event corpus, Robert and John Gurney 1581-1630 (Candidate D anchor) | ROLLCO / Boyd's *Roll of the Drapers' Company* (1934) | Livery-company records |
| 14 | T. C. Dale, *Inhabitants of London in 1638*: St. Augustine | Society of Genealogists 1931; British History Online | Rents return |
```

## 5. Robert Gurney 1625 will appendix - append to `research/people/john-gurney-candidate-d.md`

Append the following new section AFTER the existing "Next steps, ranked by tractability and value" section and BEFORE the closing "Cross-references" section. This brings the full v13 §8 will transcription and witness/probate clauses into research, where v34 captured only the summary.

```markdown
## Appendix - Robert Gurney 1625 will, working semi-diplomatic transcription

The will is the controlling primary record for Candidate D. Robert Gurney's will was written 18 January 1621/2 (Old Style 1621), proved at the Archdeaconry Court of London on 23 September 1625 by John Gurney as son and executor, and survives as an Ancestry-imaged folio supplied by the user as `31787_A002570-00422.jpg`. Full transcription with v13 reading conventions preserved (`[unclear]`, `[?]`, and bracketed alternatives marking uncertain readings, lineation regularised for readability):

```text
In the name of God Amen the eighteenth day of January in the yeare of
our Lord god one thousand six hundred twenty and one And in the yeare of
the raigne of our soveraigne Lord James by the grace of God kinge of
England Scotland ffrance and Ireland defender of the faith &c viz
of England ffrance and Ireland the nineteenth And of Scotland the five and fiftieth
I Robert Gurney Citizen and Draper of London being of good health of body and of perfect memory
praise be given to god doe make and declare this my last will and Testament in manner and forme following
that is to say

First and principally I commend and commit my soule and body into the hands of Almighty god my Creator
and of Jesus Christ my only Saviour and redeemer by whose mercy and meritts I doe believe assuredly
to have obteyned full and free remission pardon for all my sinnes and offences whatsoever and to enjoy
eternall life with others the elect children of god in the kingdome of heaven. And my body I will shall
be buried in Christian buriall at the discretion of the overseers of this my last will and Testament
hereunder named.

Item I will and my minde and true meaning is that all my goods chattells and debts
whatsoever which I shall possesse shall at the tyme of my decease be valued and appraised by
indifferent men thereunto to be appointed in that behalfe according to the laudable custome of the
City of London. And after such valuation and appraisement thereof given and bequeathed unto my loving wife
Anne Gurney one full third parte thereof for her full third parte of in and to my said goods and chattells
which she may have or claime of me or to all and every my said goods and chattells by virtue of the said
custome or otherwise howsoever.

One other third parte of my goods and chattells aforesaid I give and
bequeath unto my loving sonne John Gurney for his full third parte and portion to [aforesaid? / be allotted?]
and the other third parte I will shall be payd and discharged the debts funerall expenses and legacies by
me in this my last will and Testament to be paid or given and bequeathed.

Item I will and my
minde is that my aforesaid wife shall during her naturall life she continuing her selfe my widow
and not after my decease marry againe dwell in and have the roome of the two uppermost
roomes in my house in the Old Change wherein I now dwell, if she desire there to have
of the said house soe long continue. But if she shall at any tyme after my decease marry
then my minde and will is that the benefitt which she may claime of in or to the said [house/rooms]
by virtue of this my testament and last will shall cease and that then my said wife shall
thereupon suffer my said sonne John Gurney quietly to enjoy the same.

Item my will and my minde is that my sonne
John Gurney shall have and enjoy to his owne use the shoppe cellar and hall over the same
house [...] and quietly to enjoy the same. Item my will and minde is that my sonne
John Gurney shall have and enjoy to his owne use the shoppe cellar and hall over the same house
[...]
and during all the terme of yeares which shall happen in and to the same house. The summe of all
and singular my goods and chattells whatsoever, my debts being paid and funerall expenses discharged
and all my legacies herein given all satisfied and paid, I give and bequeath to my said loving
sonne John Gurney whom I doe make and ordaine full and sole executor of this my last will
desiring god to blesse him and make him his faithfull servant.

And I doe make overseers
of this my last will my loving and kind friends Thomas Dunnell brother in lawe and Joseph
Henscott Stationer Citizen of London desiring them soe far as in them lyeth to see that
my last will and Testament in every part performed as my trust is in them. And I doe give unto the
said overseers [forty] shillings a peece. In witness whereof to this my last will and
testament I have sett to my hand and seale yeoven the day and yeare first above
written.
```

The testator's signature reads `Robert Gurney`. The witness clause is:

```text
Signed sealed pronounced and declared
the day and yeare first above written
for the Testator's last will and Testament
above said in the presence of me Edward [Romney/Romney?] scr[ivener]
and of me William Lloyd apprentice to scr[ivener]
William Symons[?]
```

The probate clause is:

```text
Probatum fuit suprascriptum testamentum
apud London vicesimo tertio die Septembris
Anno Domini 1625 [coram ...] Thoma
[Langley?] Surrogato juramento Johannis
Gurney filii et executoris in hujusmodi
testamento nominati [...]
```

Working translation of the probate clause: "The above-written testament was proved at London on the twenty-third day of September in the year of the Lord 1625, by the oath of John Gurney, son and executor named in this testament."

### Will-clause uncertainty notes

The house-use and shop/cellar/hall passage is the least clean portion of the v13 transcription. The will gives Anne widowhood use of upper rooms in the Old Change house and gives John control or enjoyment of the shop/cellar/hall or lower commercial portion. The image appears to contain repeated or overlapping phrasing about John's enjoyment of the shop/cellar/hall, which may be legal drafting style or genuine duplication; resolving this requires a higher-resolution image.

### High-confidence extracted facts

| Fact | Reading |
|---|---|
| Testator | Robert Gurney |
| Civic/company style | Citizen and Draper of London |
| Will date | 18 January 1621/2, written as 1621 Old Style |
| Probate date | 23 September 1625 |
| Wife | Anne Gurney |
| Son | John Gurney |
| Executor | John Gurney, son |
| Dwelling/business location | Old Change |
| Business/working premises | Shop, cellar, and hall associated with the house |
| Overseer | Thomas Dunnell, brother-in-law |
| Overseer | Joseph Henscott, stationer and citizen of London |
| Witness | Edward Romney, scrivener |
| Witness | William Lloyd, apprentice to the scrivener |
| Witness | William Symons |
| Religious formula | Christ as Saviour and Redeemer; remission of sins by mercy and merits; "elect children of God"; Christian burial |

Source ID: `acl-robert-gurney-will-1625`.
```

## 6. Create `research/topics/london-gurney-comparators-1595-1670.md`

Create this new research-topics file. It captures the Boyd cards 1-3 detail and the Harleian St Vedast / St Michael le Quern findings from v13 sections 1-3 and 13.

```markdown
# London Gurney / Gourney / Garney comparators, 1595-1670

This file holds same-surname London Gurney households that surfaced from Boyd's Inhabitants of London cards and from the Harleian Society register volumes for St Vedast Foster Lane and St Michael le Quern during the 2026-05 Candidate D pass. None of these households are the colonial John Gurney of Braintree, and none belong to the Robert / John of Old Change household covered by Candidate D, but each is a real London Gurney trace that should remain visible when same-name London searches are extended.

## Boyd's Inhabitants of London cards (Candidate D pass)

Five Boyd's Inhabitants of London cards were transcribed in 2026-05 for the Candidate D pass. Two of the five (the John Gurny of S Augustine card and the Robert Gurny of S Augustine card) belong to the Candidate D household and are covered in `research/people/john-gurney-candidate-d.md`. The remaining three are comparator London Gurney households without a current direct line to the Candidate D household.

### John Gourney of S Dionis Backchurch, merchant, 1655

Boyd card `GBOR/BIL/SOG25/0595`, indexed under GURNY John 1655 with internal reference number 11703. The body of the card spells the surname `Gourney`; the upper-right index box gives `GURNY`. Findmypast transcript URL `https://www.findmypast.com/transcript?id=GBPRS%2FBIL%2F00131781&tab=this`.[^boyd-cards-cd]

| Field | Entry |
|---|---|
| Name | John Gourney |
| Of | S Dionis Backchurch |
| Married | 1655 at S Lawrence Pountney, banns |
| Wife | Dorothy Reading of Northampton |
| Wife daughter of | Reading |
| Wife died | 1658 Jan. 31 at S Dionis |
| Profession | merchant |
| Children | Anne, baptised 1656 Sep. 29; Dorothy, [baptised] 1658 Feb. 23 |

This is a separate London Gurney trade household: John Gourney, merchant, of St Dionis Backchurch, married Dorothy Reading of Northampton in 1655 at St Lawrence Pountney; wife died 31 January 1658 at St Dionis; daughters Anne 1656 and Dorothy 1658. The 1655 marriage and 1656-1658 baptisms are too late to be the colonial John Gurney of Braintree (who died about March 1662/3 in Boston with no daughter named Dorothy) and the trade is merchant, not tailor.

### Mary Garney / Gurney, daughter of John Garney, wife of William Shipman, 1660

Boyd card `GBOR/BIL/SOG26/0392`, indexed under SHIPMAN William 1660 with internal reference number 12337, and a free note at top center reading `see 18059`. The card is headed William Shipman of All Hallows Barking; the wife's surname on the card is most legible as `Garney`, though the Findmypast metadata associates the entry with `Gurney`. Findmypast transcript URL `https://www.findmypast.com/transcript?id=GBPRS%2FBIL%2F00138914&tab=this`.[^boyd-cards-cd]

| Field | Entry |
|---|---|
| Name | William Shipman, of All Hallows Barking |
| Father | William Shipman of Scarrington Notts |
| Born | 1633 c. |
| Wife | Mary Garney, of England Nat[?] |
| Wife daughter of | John Garney |
| Profession | merchant |
| Died | 1681 Sept. 14, aged 48 |
| Buried at | All Hallows Barking |
| Children | Thomas |
| Arms | AR bend betw 6 crosslets GU impaling AR chevron engr AZ betw 3 scallops SA |

A Mary Garney / Gurney as wife of William Shipman the merchant, daughter of a John Garney / Gurney, is a collateral lead for any wider research into the John Gurney + Mary problem in London. The card does not give Mary's birth date, place, or parish. The heraldic note uses standard abbreviations (AR = Argent, GU = Gules, AZ = Azure, SA = Sable). The arms are not those of the Norfolk Gurney cross-engrailed family known to the case-file, but they preserve the impaled-coat structure typical of a heralded London merchant marriage.

### John Gurney citizen and grocer, wife Jane / Joan Waring, 1640

Boyd card `GBOR/BIL/SOG36/0477`, indexed under GURNY John 1640 with internal reference number `2054[?]`. The image is degraded; the parish after "of" reads most like S Botolph Aldgate. Findmypast record URL `https://search.findmypast.com/record?id=GBOR%2FBIL%2FSOG36%2F0477&parentid=GBPRS%2FBIL%2F00213440`.[^boyd-cards-cd]

| Field | Entry |
|---|---|
| Name | John Gurney |
| Of | [prob. S Botolph Aldgate; unclear] |
| Wife | Jane [or Joan] Waring (1) |
| Profession | citizen + grocer |
| Free-note above Died line | 1638 rent £10 S Augustine |
| Died | [with 1657?] |
| Children / notes | Richard, died 1615; [ux?] mother Jane; John probably age 21 in Aug 1641 |

This is a London Gurney citizen-and-grocer household, distinct from the Candidate D Old Change draper-tailor household. The card's free-note "1638 rent £10 S Augustine" is the same Boyd index reference that appears on the Candidate D John Gurny of S Augustine card; Boyd's compiler attached the same 1638 entry to two different John Gurney cards, presumably because the compiler had not yet resolved which John the 1638 entry belonged to. The post-1601 cross-reference cannot be Candidate D's wife in a household where John appears as a son "probably age 21 in Aug 1641" of an earlier-born John Gurney + Jane Waring couple.

[^boyd-cards-cd]: Boyd's Inhabitants of London & Family Units 1200-1946, cards captured 2026-05 in the Candidate D working packet; transcriptions in `sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md` sections 1-3; Source ID `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards`.

## Harleian Society register findings - St Vedast and St Michael le Quern

The Harleian Society Registers volumes XXIX (christenings) and XXX (marriages and burials) for St Vedast Foster Lane and St Michael le Quern, ed. Willoughby A. Littledale (London: Harleian Society, 1902-1903), were searched in 2026-05. The volumes are the printed register edition for the parish union that includes Anne Morris's home parish of St Michael le Quern, and remain useful for collateral Gurney / Gourney London comparators.[^harleian-cd]

### Parish register survival

Volume XXIX's preface states that St Michael le Quern stood at the angle of Paternoster Row and St Paul's Churchyard, was destroyed in the Great Fire of 1666, and that its earlier register was probably destroyed at the same time. The parish was afterwards united with St Vedast Foster Lane. Surviving St Michael register material begins only 1685-6 for baptisms and burials, with a few marriages at various dates. The implication for Candidate D is that no 1611-era Anne Morris baptism, no Robert / Anne early marriage entry, and no early child entries are recoverable from the St Michael le Quern register.[^harleian-cd]

St Vedast Volume I covers 1558-1685 and includes baptisms, marriages, and burials. The Harleian transcription is described as a copy from the old register made *verbatim et literatim* by Miss P. E. Gertrude Girdlestone, with an index.[^harleian-cd]

### Anne Gourney, daughter of Richard Gourney, baptised January 1626 St Vedast

Volume XXIX records:

```text
Anne Gourney ye daughter of Richard Gourney was baptised January, 1626.
```

A separate Richard Gourney family in St Vedast Foster Lane. The printed index gives Gourney under the broader Gurney-related surname cluster and associates Anne and Richard with the relevant pages. This Anne is not connected by the printed record to the Robert Gurney / Old Change household; the geographic proximity is real (St Vedast Foster Lane is in the same Cheapside / Paternoster Row orbit), but no kinship is stated. Worth preserving as a same-neighbourhood / same-decade Gourney comparator.[^harleian-cd]

### Richard Cobham and Jane Gurney, married 23 November 1658 St Vedast

Volume XXX records:

```text
Richard Cobham & Jane Gurney were Married November the 23d, 1658.
```

Later than the Candidate D decision window. The entry does not identify Jane's father, residence beyond the register context, or relationship to Robert / John Gurney of Old Change. Treat as a later St Vedast Gurney occurrence only.[^harleian-cd]

### Joshua Little and Elizabeth Gurney, married 31 December 1728 St Vedast

Volume XXX records:

```text
Joshua Little of Saint Gregorys and Elizabeth Gurney of Saint Stephen, Coleman-street,
was married ye 31 December 1728 by lycence.
```

Much later and probably unrelated to Candidate D, but notable because St Stephen Coleman Street is the canonical Puritan / emigration parish discussed in the case file's Section 10.4 (William Gurney at Coleman Street). An eighteenth-century Elizabeth Gurney "of St Stephen Coleman Street" implies a Coleman Street Gurney household that persisted long after the 1641 emigration window.[^harleian-cd]

### Elizabeth Gurney, wife of Sir Richard Gurney, monument note at St Vedast

Volume XXX includes an editor's burial-section note:

```text
There is a monument on the south wall of the Church to the memory of Robert South
and various members of his family, including Elizabeth Gurney the wife of Sir Richard Gurney,
"that loyal Lord Mayor."
```

Belongs to the well-known Sir Richard Gurney civic line (Lord Mayor of London 1641-1642). Useful only as evidence that later prominent Gurneys had a memorial association with St Vedast.[^harleian-cd]

### Hannah Gurney burial at St Vedast

Volume XXX records:

```text
Hannah Gurney was Buried in the Ch. Yard.
```

Late and not Candidate D. The index lists Hannah under Gurney. Preserve as a logged occurrence only.[^harleian-cd]

### Late Ann Morris of St Michael le Quern - anti-conflation guard

Volume XXX includes:

```text
11 June 1764: Abraham Collinson of St Mary Abchurch, bachelor, and Ann Morris of St Michael le Quern,
spinster, by banns.
```

More than a century after Candidate D's window. Listed here only so that future researchers do not conflate it with Anne Morris, wife of Robert Gurney (married 1611, St Magnus the Martyr). The Morris surname remained visible in the St Vedast / St Michael le Quern orbit long after Candidate D's window without bridging Anne Morris of 1611 into a recoverable family group.[^harleian-cd]

## Dunnell and Henscott search

The Robert Gurney 1625 will named Thomas Dunnell (brother-in-law) and Joseph Henscott (stationer and citizen of London) as overseers. Searches of the two Harleian volumes did not produce a clean early-modern Dunnell or Henscott match relevant to the will. Apparent later "Dunnett" entries are not treated as the same name. Henscott / Hunscott / Hencott did not produce a relevant St Vedast or St Michael le Quern register match in this pass; the Joseph Hunscott Stationers' Company / 1638 St Augustine identification is handled in `research/people/john-gurney-candidate-d.md`.[^harleian-cd]

## Cross-references

- Candidate D topic file: `research/people/john-gurney-candidate-d.md`.
- Research companion: `research/people/g13-john-gurney-fact-sheet.research.md`.
- Place note: `research/places/city-of-london.md`.
- Validation note: `sources/validations/harleian-st-vedast-st-michael-le-quern-registers.md`.

[^harleian-cd]: Willoughby A. Littledale, ed., *The Registers of St. Vedast, Foster Lane, and of St. Michael le Quern, London*, Harleian Society Registers vols. XXIX (christenings) and XXX (marriages and burials) (London: Harleian Society, 1902-1903); user-supplied PDFs `FL3830041_284895_29.pdf` and `FL3830150_284895_30.pdf` searched 2026-05; Source ID `harleian-st-vedast-st-michael-le-quern-registers`.
```

## 7. Create `research/topics/london-grine-grene-grone-comparators.md`

Create this new research-topics file. It captures the Grine / Grene / Grone / Garney comparator records from v13 sections 19-23 — same-name density evidence in the broader City-of-London search ring that should not be conflated with the Candidate D Gurney household.

```markdown
# London Grine / Grene / Grone same-name comparators, 1600-1641

This file holds the London Grine / Grene / Grone records surfaced during the 2026-05 Candidate D pass. None of these are the colonial John Gurney of Braintree, and none belong to the Robert / John of Old Change household covered by Candidate D, but each is a real London same-name occurrence that should remain visible when comparator-density work is extended.

The records are organised by geographic proximity to Old Change and by chronological order, with parish-geography and Candidate-D-impact notes.

## Jhon Grine, baptised 6 March 1603/4, St Mary-at-Hill

Indexed record (no image reviewed in this pass): Jhon Grine, male, baptism date 6 March 1603, baptism place Saint Mary At Hill, London. FHL Film 374485.[^grine-mary-at-hill-1604]

| Field | Value |
|---|---|
| Subject | Jhon Grine |
| Event | Baptism / christening |
| Date | 6 Mar. 1603/4 |
| Parish | St Mary-at-Hill, City of London |
| Father | not indexed |

The indexed surname `Grine` is potentially a transcription error of Gurney, although no image has been seen. The date 6 March 1603/4 aligns with the approximate birthdate inferable for the Massachusetts John Gurney from his 1653 Wilson v. Faxon deposition aged about 50. The parish St Mary-at-Hill (in Billingsgate Ward, near Eastcheap) is geographically plausible within the broader City of London search ring but is not in the core Candidate D Old Change / Watling Street cluster. Keep as a possible false-positive lead pending image inspection.

## John Grone, buried 5 July 1625, St Magnus the Martyr

Indexed and image-reviewed in 2026-05 from St Magnus the Martyr burial register image `31281_a101911-00131.jpg`, right page, under "Burialls Anno Domini 1625", July section. Working image transcription:

```text
5  John Grone buried
```

The image does not show a father, wife, occupation, or residence beyond the bare name, date, and burial event. Reference number 24253143; additional reference 1856855.[^grone-magnus-1625]

This burial is **probably not Candidate D John**, on chronology: Candidate D John was alive to prove Robert Gurney's will on 23 September 1625 as son and executor, more than two months after this John Grone's 5 July 1625 burial. Although St Magnus the Martyr was the 1611 marriage venue for Robert Gourney and Anne Morris, no kinship to Robert is recorded in this 1625 burial entry. Useful only as an exclusionary record demonstrating that at least one different-name John Grone died in St Magnus parish in 1625, preventing accidental conflation.

## John Grine and Mary, married 24 January 1640/1, St Swithin London Stone

Indexed and image-reviewed in 2026-05 from London Metropolitan Archives reference `P69/SWI/A/001/MS04311`. The Ancestry index gives spouse name Mary Jones, reference number 24930171; additional reference 1888376. The original image (`31281_a102288-00110.jpg`) is upside down; reviewed after mental rotation. Working transcription:

```text
John grine of the pish & mary
of the same pish were maryed by me
Owen W[?] cler[ke?] the 24th of January 1640
```

| Field | Value |
|---|---|
| Groom | John Grine |
| Bride | Mary (index gives Jones; image surname not clearly readable) |
| Event | Marriage |
| Date | 24 Jan. 1640/1 |
| Parish | St Swithin, London Stone |
| Officiant | "by me Owen W[?] cler[ke?]" |
| Licence/banns | not clearly stated |

The visible surname looks more like `grine` than `gurney` and lacks the internal `urn`/`ourn` pattern seen in other Gurney records. The lead is preserved because the bride is named Mary, the date is chronologically tight but not impossible before a 1641 New England appearance, and St Swithin London Stone lies in the Cannon Street / Walbrook commercial zone not far from St Augustine Watling Street. But there is no father, occupation, or company clue, no link to Robert Gurney, the Drapers' Company, or Old Change, and the surname does not visibly read as a Gurney variant. The January 1640/1 date also leaves a very tight migration window before the colonial John's June 1641 Weymouth fine.[^grine-swithin-1640]

Treat as a broad-area lead, low-value as evidence, until a stronger bridge appears (subsequent St Swithin baptisms or burials for John Grine / Gurney / Mary, marriage licence detail, or a livery / probate trace).

## John Grone son of John Grone, baptised 4 August 1630, St Giles Cripplegate

Indexed record: John Grone, male, baptism date 4 August 1630, baptism place Saint Giles Cripplegate, City of London, father John Grone. Reference number 23300657; additional reference 1813505.[^grone-cripplegate-1630]

The supplied image is the St Giles Cripplegate 1630 register page with mixed monthly sections, crowded and faded; the indexed line could be located approximately but not transcribed with high confidence in the present image. The indexed surname `Grone` should be treated as uncertain pending a tighter crop or higher-resolution image. Possible readings worth testing on a better image are Grone, Gron[e], Grome, Gorne, Groune, Gurne.

The colonial John Gurney reportedly had a son John born in England about the early 1630s, so a baptism of John, son of John, in 1630 London is worth preserving as a comparator lead. But the record lacks Gurney spelling, mother / wife Mary, father Robert, St Augustine / Old Change / Drapers context, and an image clear enough to confirm a Gurney variant. St Giles Cripplegate (Fore Street / Barbican area) is north of the core Candidate D parishes and is in the broader City of London search ring rather than the immediate Old Change neighborhood.

## John Grene son of Jeames Grene, baptised 16 November 1634, St Mary Magdalen Old Fish Street

Indexed and image-reviewed in 2026-05 from St Mary Magdalen Old Fish Street parish register, left page under "Anno domini 1634"; image `31281_a101952-00044.jpg`. Working transcription:

```text
John Grene the sonne of Jeames Grene was christened
the 16th of November.
```

Reference number 24296258; additional reference 1860129. Father indexed and image-confirmed as Jeames / James Grene.[^grene-old-fish-street-1634]

This is not Candidate D and not a son of John (the colonial John Gurney's first-known son John was named after himself, not James). St Mary Magdalen Old Fish Street stood at Old Fish Street and Old Change, making it directly in the Old Change neighbourhood; the parish should remain on the high-priority search list for Gurney / Gurny / Gorney / Gourney variants 1625-1641, but this specific Grene household belongs to a James Grene, not the Old Change Robert Gurney household.

## John Grene son of Robart Grene, baptised 31 August 1600, All Hallows Bread Street

Indexed record (no image available in this pass): John Grene, male, baptism date 31 August 1600, baptism place Allhallows Bread Street, London, father Robart Grene. FHL Film 94511.[^grene-bread-street-1600]

| Field | Value |
|---|---|
| Subject | John Grene |
| Event | Baptism |
| Date | 31 Aug. 1600 |
| Parish | All Hallows Bread Street |
| Father | Robart Grene |

The father reading `Robart` could be a transcription of Robert, the date falls after the first St Augustine John was buried 4 February 1599/1600, and All Hallows Bread Street is geographically very close to St Augustine Watling Street / Old Change. But Robert Gurney's stillborn son was buried at St Augustine on 8 April 1601, which compresses any pregnancy chronology if the same Robert is to be father of a 31 August 1600 child at the neighboring parish. The indexed surname `Grene` reads more naturally as Greene unless the original register image shows otherwise. Preserve as a moderate adjacent-parish lead, not a Candidate D event, pending image access.

## John Grene son of Rich Grene, baptised 1 January 1610/11, St Mary Whitechapel

Indexed record (no image available in this pass): John Grene, male, baptism date 1 January 1610, baptism place St Mary Whitechapel, Stepney, London, father Rich Grene. FHL Film 94691.[^grene-whitechapel-1611]

| Field | Value |
|---|---|
| Subject | John Grene |
| Event | Baptism |
| Date | 1 Jan. 1610/11 |
| Parish | St Mary Whitechapel (St Mary Matfelon), Stepney |
| Father | Rich Grene |

Low Candidate D value. The father is Rich, not Robert or John; the surname is indexed Grene; the date is too late to fit Candidate D John (born by about 1601-1604 to fit a 1623/4 adult freedom and a 1625 executor role) and would make the subject only about 13 at the 1623/4 freedom event; the parish is outside Aldgate in the East End rather than the Old Change / Watling Street / Cheapside cluster. Preserve as a broad London Grene / Greene comparator only.

## Comparator summary

| Record | Geography | Name/family fit | Candidate D value |
|---|---|---|---|
| Jhon Grine baptism, St Mary-at-Hill, 6 Mar 1603/4 | Eastcheap / Billingsgate; outside core Candidate D parishes | Surname could be Gurney transcription error; no father indexed | Possible false positive lead; check image |
| John Grone burial, St Magnus the Martyr, 5 Jul 1625 | St Magnus = Robert / Anne 1611 marriage venue | Surname does not visibly read as Gurney; no kinship stated | Exclusionary; not Candidate D because Candidate D John proved Robert's will 23 Sep 1625 |
| John Grine + Mary marriage, St Swithin London Stone, 24 Jan 1640/1 | Cannon Street / Walbrook, plausible City zone | Visible surname looks like `grine`, not Gurney; bride Mary is attractive | Low to moderate as a search lead; very tight migration window |
| John Grone son of John Grone, St Giles Cripplegate, 4 Aug 1630 | Cripplegate, outside core Candidate D parishes | Surname uncertain; father John not Robert; no wife / mother Mary | Broad-area comparator only |
| John Grene son of Jeames Grene, St Mary Magdalen Old Fish Street, 16 Nov 1634 | Old Fish Street at Old Change, core Candidate D neighbourhood | Father Jeames / James, not John or Robert; surname Grene image-confirmed | Same-neighbourhood non-Gurney comparator |
| John Grene son of Robart Grene, All Hallows Bread Street, 31 Aug 1600 | Bread Street at Watling Street, core Candidate D neighbourhood | Father Robart (= Robert?), surname Grene unverified by image | Moderate adjacent-parish lead; image pull deferred |
| John Grene son of Rich Grene, St Mary Whitechapel, 1 Jan 1610/11 | Stepney / Whitechapel, outside core City | Father Rich, surname Grene; date too late for Candidate D adult freedom | Low; broad London Greene comparator only |

## Cross-references

- Candidate D topic file: `research/people/john-gurney-candidate-d.md`.
- Research companion: `research/people/g13-john-gurney-fact-sheet.research.md`.
- Validation notes: `sources/validations/lma-st-swithin-london-stone-register-john-grine-1640.md`, `sources/validations/lma-st-giles-cripplegate-register-john-grone-1630.md`, `sources/validations/lma-st-magnus-martyr-register-candidate-d-images.md`, `sources/validations/lma-st-mary-magdalen-old-fish-street-john-grene-1634.md`, `sources/validations/candidate-d-london-grine-grene-index-leads-bundle.md`.

[^grine-mary-at-hill-1604]: Ancestry.com. *England, Select Births and Christenings, 1538-1975* (Provo, UT: Ancestry.com Operations, Inc., 2014), index entry for Jhon Grine, FHL Film 374485; Source ID `candidate-d-london-grine-grene-index-leads-bundle`.
[^grone-magnus-1625]: Parish register, St Magnus the Martyr, City of London, burial register; user-supplied image `31281_a101911-00131.jpg` reviewed 2026-05; reference 24253143 / 1856855; Source ID `lma-st-magnus-martyr-register-candidate-d-images`.
[^grine-swithin-1640]: Parish register, St Swithin London Stone, City of London, marriage register, London Metropolitan Archives reference `P69/SWI/A/001/MS04311`; user-supplied image `31281_a102288-00110.jpg` reviewed 2026-05; Ancestry index reference 24930171 / 1888376; Source ID `lma-st-swithin-london-stone-register-john-grine-1640`.
[^grone-cripplegate-1630]: Parish register, St Giles Cripplegate, City of London, baptism register; user-supplied image `31281_a101526-00185.jpg` reviewed 2026-05 (image faded and crowded; index-led extraction only); reference 23300657 / 1813505; Source ID `lma-st-giles-cripplegate-register-john-grone-1630`.
[^grene-old-fish-street-1634]: Parish register, St Mary Magdalen Old Fish Street, City of London, baptism register; user-supplied image `31281_a101952-00044.jpg` reviewed 2026-05; reference 24296258 / 1860129; Source ID `lma-st-mary-magdalen-old-fish-street-john-grene-1634`.
[^grene-bread-street-1600]: Ancestry.com index entry for John Grene son of Robart Grene, baptism 31 August 1600, All Hallows Bread Street, FHL Film 94511; no image pulled in this pass; Source ID `candidate-d-london-grine-grene-index-leads-bundle`.
[^grene-whitechapel-1611]: Ancestry.com index entry for John Grene son of Rich Grene, baptism 1 January 1610, St Mary Whitechapel, Stepney, FHL Film 94691; no image pulled in this pass; Source ID `candidate-d-london-grine-grene-index-leads-bundle`.
```

## 8. Validation note pointer updates

The v32 / v33 validation files for the per-parish sources currently say "findings recorded in: ..." with topic / case-file targets that did not yet exist. Update the following validation files to point at the new research files created by this patchset.

### 8.1 Update `sources/validations/harleian-st-vedast-st-michael-le-quern-registers.md`

Replace the existing body with:

```markdown
# Harleian Society - St Vedast Foster Lane and St Michael le Quern register volumes validation

- Source ID: `harleian-st-vedast-st-michael-le-quern-registers`.
- Examined: user-supplied PDFs `FL3830041_284895_29.pdf` (Vol. XXIX, christenings) and `FL3830150_284895_30.pdf` (Vol. XXX, marriages and burials) reviewed 2026-05.
- Scope: searched both volumes for surname-cluster Gurney / Gurny / Gurnie / Gourney / Gournay / Garney, plus Morris / Anne Morris / Ann Morris, Dunnell, Henscott, Romney, Symons, Lloyd, and place-cluster Old Change / Old Chainge.
- Findings recorded in: `research/topics/london-gurney-comparators-1595-1670.md` (Anne Gourney 1626, Richard Cobham + Jane Gurney 1658, Joshua Little + Elizabeth Gurney 1728 with the St Stephen Coleman Street reading, Elizabeth Gurney wife of Sir Richard Gurney monument, Hannah Gurney burial, late Ann Morris of St Michael le Quern 1764 anti-conflation guard, pre-1666 St Michael le Quern register-loss note, Dunnell / Henscott search outcome).
- Detailed phase 1 setup: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`, with v13 gap-fill in `sources/intake/processed/v36-john-gurney-candidate-d-v35-amendments-and-v13-gap-fill.patchset.md`.
```

### 8.2 Update `sources/validations/findmypast-boyds-inhabitants-london-candidate-d-gurney-cards.md`

Replace the existing body with:

```markdown
# Findmypast Boyd's Inhabitants of London - Candidate D Gurney cards validation

- Source ID: `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards`.
- Examined: five user-supplied Boyd card images reviewed 2026-05 - `gbor_bil_sog25_0595.jpg` (John Gourney of S Dionis Backchurch 1655), `gbor_bil_sog26_0392.jpg` (William Shipman / Mary Garney 1660), `gbor_bil_sog36_0477.jpg` (John Gurney citizen+grocer / Jane Waring 1640), `gbor_bil_sog59_0240.jpg` (John Gurny of S Augustine, Candidate D), `gbor_bil_sog82_0603.jpg` (Robert Gurny of S Augustine, Candidate D parent card).
- Findings recorded in: `research/people/john-gurney-candidate-d.md` (cards sog59 and sog82, plus the "1661 poll tax... Old Change" and "1638 rent £10" free-notes from card sog59); `research/topics/london-gurney-comparators-1595-1670.md` (cards sog25, sog26, sog36 - separate non-Old-Change London Gurney households).
- Detailed phase 1 setup: `sources/intake/processed/v32-john-gurney-candidate-d-source-foundation.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`, with v13 gap-fill in `sources/intake/processed/v36-john-gurney-candidate-d-v35-amendments-and-v13-gap-fill.patchset.md`.
```

### 8.3 Update each of the five v33 Grine / Grene / Grone validation files

For each of these five validation files, replace the body with the matching content below.

#### `sources/validations/lma-st-magnus-martyr-register-candidate-d-images.md`

```markdown
# LMA St Magnus the Martyr register - Candidate D images validation

- Source ID: `lma-st-magnus-martyr-register-candidate-d-images`.
- Examined: user-supplied images `31281_a101911-00014.jpg` (Robert Gourney + Anne Morris marriage 4 April 1611) and `31281_a101911-00131.jpg` (John Grone burial 5 July 1625), reviewed 2026-05.
- Findings recorded in: `research/people/john-gurney-candidate-d.md` (1611 marriage); `research/topics/london-grine-grene-grone-comparators.md` (1625 burial as exclusionary / different-name comparator).
- Detailed phase 1 setup: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v36-john-gurney-candidate-d-v35-amendments-and-v13-gap-fill.patchset.md`.
```

#### `sources/validations/lma-st-swithin-london-stone-register-john-grine-1640.md`

```markdown
# LMA St Swithin London Stone - John Grine + Mary 1640/1 validation

- Source ID: `lma-st-swithin-london-stone-register-john-grine-1640`.
- Examined: user-supplied image `31281_a102288-00110.jpg` reviewed 2026-05 after mental rotation of the upside-down page; LMA reference `P69/SWI/A/001/MS04311`; Ancestry index reference 24930171 / 1888376.
- Findings recorded in: `research/topics/london-grine-grene-grone-comparators.md` (treated as broad-area lead, not Candidate D).
- Detailed phase 1 setup: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v36-john-gurney-candidate-d-v35-amendments-and-v13-gap-fill.patchset.md`.
```

#### `sources/validations/lma-st-giles-cripplegate-register-john-grone-1630.md`

```markdown
# LMA St Giles Cripplegate - John Grone son of John Grone 1630 validation

- Source ID: `lma-st-giles-cripplegate-register-john-grone-1630`.
- Examined: user-supplied image `31281_a101526-00185.jpg` reviewed 2026-05; image faded and crowded; index-led extraction only.
- Findings recorded in: `research/topics/london-grine-grene-grone-comparators.md` (broad-area comparator).
- Detailed phase 1 setup: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v36-john-gurney-candidate-d-v35-amendments-and-v13-gap-fill.patchset.md`.
```

#### `sources/validations/lma-st-mary-magdalen-old-fish-street-john-grene-1634.md`

```markdown
# LMA St Mary Magdalen Old Fish Street - John Grene son of Jeames 1634 validation

- Source ID: `lma-st-mary-magdalen-old-fish-street-john-grene-1634`.
- Examined: user-supplied image `31281_a101952-00044.jpg` reviewed 2026-05; reference 24296258 / 1860129.
- Findings recorded in: `research/topics/london-grine-grene-grone-comparators.md` (same-neighbourhood non-Gurney comparator).
- Detailed phase 1 setup: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v36-john-gurney-candidate-d-v35-amendments-and-v13-gap-fill.patchset.md`.
```

#### `sources/validations/candidate-d-london-grine-grene-index-leads-bundle.md`

```markdown
# Candidate D - London Grine / Grene index-only comparator leads validation

- Source ID: `candidate-d-london-grine-grene-index-leads-bundle`.
- Examined: index-only entries (no image pull in this pass) for Jhon Grine bapt 6 March 1603/4 St Mary-at-Hill (FHL 374485); John Grene son of Robart Grene bapt 31 August 1600 All Hallows Bread Street (FHL 94511); John Grene son of Rich Grene bapt 1 January 1610/11 St Mary Whitechapel Stepney (FHL 94691).
- Findings recorded in: `research/topics/london-grine-grene-grone-comparators.md`.
- Detailed phase 1 setup: `sources/intake/processed/v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md`.
- Phase 2 deep-research extraction: `sources/intake/processed/v36-john-gurney-candidate-d-v35-amendments-and-v13-gap-fill.patchset.md`.
```

## 9. Audit checklist - full v13 / v15 coverage

This patchset, taken together with v34 and v35, should now cover every substantive fact and finding in v13 and v15. Each item below is mapped to its landing place.

| v13 / v15 content | Landing |
|---|---|
| §1 Boyd card sog25 - John Gourney of S Dionis Backchurch, Dorothy Reading, children Anne and Dorothy, merchant | `research/topics/london-gurney-comparators-1595-1670.md` |
| §2 Boyd card sog26 - William Shipman + Mary Garney d/o John Garney, All Hallows Barking, arms | `research/topics/london-gurney-comparators-1595-1670.md` |
| §3 Boyd card sog36 - John Gurney citizen+grocer, Jane/Joan Waring, "1638 rent £10 S Augustine" cross-note, Richard d.1615, John about 21 in Aug 1641 | `research/topics/london-gurney-comparators-1595-1670.md` |
| §4 Boyd card sog59 - John Gurny of S Augustine, father Robert, mother Anne Morris, citizen draper, "1661 poll tax... Old Change", "1638 rent £10" | `research/people/john-gurney-candidate-d.md` (v34) + 1661 cue captured as deferred source |
| §5 Boyd card sog82 - Robert Gurny of S Augustine, will-note overseers Dunnell + Henscott, witnesses Romney/Symons/Lloyd, 1611 Apr 4 marriage at S Magnus, 1581 Dec 16 freedom, Tailor Old Change | Topic file (v34); §5 will-note witnesses now in Robert will appendix (this patchset §5) |
| §6 ROLLCO John Gurney freedom by redemption 1623/4, father Robert | Topic file + research companion (v34) |
| §7 ROLLCO Robert 1617 tailor Old Change apprenticeship master; 1629 Drapers' master event; John 1630 apprenticeship master | Topic file + corpus (v34) |
| §8 Robert Gurney 1625 will - full transcription, signature, witness clause, probate clause, working translation | Robert will appendix in topic file (this patchset §5) |
| §9 Religious-language assessment | Topic file (v34) |
| §10 Old Change neighborhood, parishes, recordsets | Place file (v34) and topic file |
| §11 Candidate D designation and correlation with repo case-file framework | Case file Section 8.4 (v35 + v36 §2) |
| §12 Audit of retained evidence and non-loss check | Process-level - retained in v13 packet itself, not migrated to research |
| §13 Harleian St Vedast / St Michael le Quern findings - Anne Gourney 1626, Richard Cobham + Jane Gurney 1658, Joshua Little + Elizabeth Gurney 1728, Elizabeth Gurney wife of Sir Richard Gurney monument, Hannah Gurney burial, late 1764 Ann Morris guard, pre-1666 St Michael register-loss note, Dunnell/Henscott search outcome | `research/topics/london-gurney-comparators-1595-1670.md` |
| §14-§17 St Augustine register reviews - early children 1595-1601, negative replacement-John baptism search 1601-1610, negative first-wife burial search 1601-1612 | Topic file (v34) |
| §18 St Magnus marriage image - Robert Gourney + Anne Morris 4 April 1611 by licence | Topic file (v34) + place file |
| §19.1 Jhon Grine baptism St Mary-at-Hill 6 March 1603/4 | `research/topics/london-grine-grene-grone-comparators.md` |
| §19.2 John Grone burial St Magnus 5 July 1625 - exclusionary | `research/topics/london-grine-grene-grone-comparators.md` |
| §20 John Grine + Mary marriage St Swithin London Stone 24 January 1640/1 | `research/topics/london-grine-grene-grone-comparators.md` |
| §21 John Grone son of John Grone baptism St Giles Cripplegate 4 August 1630 | `research/topics/london-grine-grene-grone-comparators.md` |
| §22.1 John Grene son of Jeames Grene baptism St Mary Magdalen Old Fish Street 16 November 1634 | `research/topics/london-grine-grene-grone-comparators.md` |
| §22.2 John Grene son of Robart Grene baptism All Hallows Bread Street 31 August 1600 | `research/topics/london-grine-grene-grone-comparators.md` |
| §23 John Grene son of Rich Grene baptism St Mary Whitechapel 1 January 1610/11 | `research/topics/london-grine-grene-grone-comparators.md` |
| v15 phase-2 priorities and Tier 1-3 research plan | Topic file next-steps section (v34) and case file Section 12 "For Candidate D" (v35) |
| Round 1 BHO 1638 details, Joseph Huntscott = Henscott bridge | Topic file + place file + research companion (v34); additionally clarified in Section 8.4 footnote n92e (this patchset §2.1) |
| Round 1 ROLLCO Drapers' corpus 1581-1654 with event IDs | Corpus supplement and topic file (v34) |
| Round 2 1604 push-back of "Tailor Old Change" identification | Topic file (v34) |
| Round 2 Resolution of "second Robert" puzzle (1616 Stationer apprentice + 1626 Stationer freeman = separate Robert) | Topic file + new corpus supplement (v34) |
| Round 2 Joseph Hunscott Stationer identity bridge (Henscott / Huntscott / Hunscott + Wing H3728) | Topic file + new corpus supplement (v34) |
| Round 2 H-D1 redemption-via-Stationers hypothesis | Topic file dedicated section + Section 8.4 (this patchset §2) |
| Round 3 PCC Wills 1625-1670 Anne Gurney null result | Topic file next-steps + footnote |
| Round 3 An Gurney + George Bucher 27 April 1640 Essex weak remarriage lead | Topic file footnote |
| Round 3 Hanging Houghton John Gourney 1647 / 1654 Northants gentry comparator | Topic file (v34) |
| Round 3 Arber Stationers' Registers deferred target | New source + new validation + topic file next-steps |
| Round 3 1640 W. J. Harvey Principal Inhabitants deferred target | New source + new validation + topic file next-steps |
| Round 3 1661 TNA E179 Free and Voluntary Present deferred target | New source + new validation + topic file next-steps |

Items deliberately not migrated:

- v13 §12 audit/non-loss check is process-state about the v13 packet itself.
- v13 §11 "case-file correlation" narrative reproduced in essence inside Section 8.4 of the case file (this patchset §2); the full v13 §11 candidate-comparison table is not reproduced because the case-file Section 9 and Section 11 already carry the structured comparator framing.

## 10. Sibling patchset hand-off

Apply order: v32, v33, v34, v35, v36. Where v36 supersedes a v35 section (§1, §2), the v35 instruction is replaced wholesale; v35 sections that v36 does not touch (§3 Probability Assessment row, §4 Section 12 "For Candidate D" subsection, §5 audit checklist) remain authoritative.
