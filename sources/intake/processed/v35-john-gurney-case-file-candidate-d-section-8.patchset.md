# Intake patchset v35 - Candidate D case-file edits (Section 8.4 + 9 row + 11 row + 12 next-steps)

```yaml
patchset_id: v35
created: 2026-05-14
repo_scope: gurney-genealogy
phase: phase_2_case_file_integration
input_packet: sources/intake/john-gurney-2026May/john-gurney-candidate-d-working-packet-audited-v13.md
depends_on:
  - v32-john-gurney-candidate-d-source-foundation.patchset.md
  - v33-john-gurney-candidate-d-register-and-comparator-sources.patchset.md
  - v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md
target_file: research/case-files/john-gurney-case-file-v4.md
phase_2_rule: Apply the tight Candidate D summary into the case file. Depth and detail stay in the topic file `research/people/john-gurney-candidate-d.md`.
```

## 0. Scope

Add the Candidate D summary into the John Gurney case file at four discrete insertion points:

- Section 8 candidate-table: one new row for Candidate D, placed immediately after the Candidate C row.
- Section 8.4: a new tight Candidate D subsection placed immediately after the existing Section 8.3 Buckinghamshire same-county cluster.
- Section 11 Probability Assessment table: one new Candidate D row.
- Section 12 What's Still Needed: a new "For Candidate D" subsection inserted before the existing "For Enrichment" subsection.

All four edits keep the case-file body summarised and plain-spoken; researchers wanting depth and detail are pointed to `research/people/john-gurney-candidate-d.md`.

## 1. Section 8 candidate-table row insertion

In `research/case-files/john-gurney-case-file-v4.md`, find the row beginning `| **Candidate C** | Berkhamsted, Hertfordshire | Unknown | **ELIMINATED** | Age misalligned...`. Immediately AFTER that row and BEFORE the row beginning `| Aylesbury, Bucks (John + Anne Cowheard) |`, insert this new row:

```markdown
| **Candidate D** | St Augustine Watling Street and Old Change, London | Unknown | **Unlikely (~3-5%)** | Son and executor of Robert Gurney, citizen and draper of London; Drapers' Company freeman by redemption 11 Feb 1623/4; Drapers' apprenticeship master 3 Nov 1630 binding Henry Smith of Kilton, Suffolk; same-name John Gurney at £10 in the 1638 St Augustine rents return; Boyd's-card cue to a 1661 Old Change poll-tax entry not yet image-verified. No wife Mary, no matching child set found in London parish, livery, or probate records 1620-1641 (see 8.4). |
```

## 2. Section 8.4 new subsection insertion

In `research/case-files/john-gurney-case-file-v4.md`, find the heading `### 8.3 Buckinghamshire same-county cluster` and its trailing paragraphs (ending at the paragraph that begins `The Aylesbury Prerogative Court of Canterbury probate records show a further Buckinghamshire family with a Daniel Gurney who died 1669...`). Immediately AFTER that paragraph and BEFORE the next H2 heading `<h2 id="s10">9. SEPARATING THE TWO FRANCIS GURNEYS</h2>`, insert this new subsection:

```markdown
### 8.4 Candidate D — London Drapers' / Old Change

Candidate D is John Gurney, son and executor of Robert Gurney, citizen and draper of London / tailor of Old Change. He was admitted to the Drapers' Company by redemption on 11 February 1623/4 and proved Robert's will on 23 September 1625.<sup class="fn"><a href="#n92" id="ref-92a">92</a></sup>

Robert of Old Change was a long-tenured London draper-tailor: Drapers' freeman by servitude on 16 December 1581 under master Robert Furnes, already styled "Tailor, Old Change" at admission; active as Drapers' master across about 14 apprenticeship- or freedom-master events between 1597 and 1622; documented Old Change identifications in 1604, 1617, and 1622; married Anne Morris of St Michael in the Querne by licence at St Magnus the Martyr on 4 April 1611, after an earlier wife produced children at St Augustine in the 1590s. The 1581 master reading "Robert Furnes" corrects the Boyd's-card reading "Robert Mason[?]".<sup class="fn"><a href="#n92" id="ref-92b">92</a></sup>

John was admitted by redemption rather than patrimony despite Robert's 1581 freedom. The cleanest explanation is that John had served apprenticeship in a different company before taking up the family Drapers' business; a ROLLCO Stationers' record places a John Gurney apprentice bound to master James Boler on 25 March 1613 with no recorded Stationers' freedom — a candidate for the future Candidate D John, consistent with Robert's 1625 choice of Joseph Henscott Stationer as a will overseer. This is hypothesis H-D1; the Arber Stationers' Registers volume 3 raw entry would confirm or kill the link by naming the apprentice's father.<sup class="fn"><a href="#n92" id="ref-92c">92</a></sup>

On 3 November 1630, John Gurney appeared as a Drapers' master binding Henry Smith, son of late Thomas Smith yeoman of Kilton, Suffolk, for a seven-year term. Henry Smith does not surface as a freed Drapers' Smith 1635-1645 under John Gurney or any other master, and no Drapers' Turnover event for any Gurney is recorded 1620-1670. The trail terminates inconclusively.<sup class="fn"><a href="#n92" id="ref-92d">92</a></sup>

The 1638 T. C. Dale St Augustine return places one John Gurney at £10 in MS. 67a, between Christopher Hunlock £2 and George Browne £10. On MS. p. 68 of the same return, Joseph Huntscott appears at £12; this is the same Joseph Hunscott who was an active Stationers' apprenticeship master 1612-1646, who fathered John Hunscott (Stationer 1641), who published the 1646 royalist petition Wing H3728, and who was named as overseer in Robert Gurney's 1625 will. The 1638 return therefore places the Robert Gurney will-network still in the same parish 13 years after Robert's death; the most economical reading is that the 1638 John Gurney is the same John Gurney who took the Old Change shop under the 1625 will.<sup class="fn"><a href="#n92" id="ref-92e">92</a></sup>

Boyd's Inhabitants of London card for John Gurny of S Augustine carries a partly-legible free-note reading "1661 poll tax [unclear] Old Change". The most likely underlying record is the 1660-1661 Free and Voluntary Present in TNA E179. If a Gurney entry can be confirmed at Old Change in 1661 at image level, Candidate D is effectively eliminated as the Massachusetts John, who died at Boston about March 1662/3. No online image has yet been located.<sup class="fn"><a href="#n92" id="ref-92f">92</a></sup>

**Why Candidate D is held as a serious but unlikely comparator.** Old Change is a real textile-trade household and Robert Gurney's will leaves John the trade premises and the residuary estate, so Candidate D meets the "father in a textile trade" criterion that previously distinguished Candidate B. John's c.1600-1604 birth window is compatible with the colonial John's 1653 deposition aged about 50. The will preamble uses Reformed-vocabulary language ("elect children of God") consistent with a godly-Protestant milieu.

But the evidence against migration is now stronger than the evidence for:

- The 1630 Drapers' master role and 7-year apprenticeship bind John to a London tailoring business at exactly the wrong time for a 1636 New England arrival.
- The 1638 St Augustine £10 rent return, combined with Joseph Hunscott still being in the same parish, points to continuing London residence.
- The Boyd's-card 1661 poll-tax cue, if correct, would carry the household to within two years of the Massachusetts John's death in Boston.
- No marriage of John Gurney to a wife named Mary, and no baptisms of Sarah, Mary, Richard, John, or Peter to a John Gurney + Mary household, have been located in any London parish register 1620-1641. The closest John Gurney + Mary marriage (Eythorne, Kent, 6 November 1632 to Mary Marsh) is a Kent couple who stayed in Kent and whose first known child is John 1638, incompatible with the colonial child-naming sequence.
- The Old Change household has no demonstrated Puritan minister, lecturer, or Coleman-Street-network associate, and no Massachusetts bridge record.

The case-file depth-of-detail analysis lives in `research/people/john-gurney-candidate-d.md`, including the full ROLLCO event corpus, the Hunscott / Henscott / Huntscott identity bridge, the 1613 Stationers' apprenticeship lead, the Anne Morris first-wife / second-wife reconstruction, and the post-1625 St Augustine record gaps. The research companion `research/people/g13-john-gurney-fact-sheet.research.md` carries the cross-link summary.<sup class="fn"><a href="#n92" id="ref-92g">92</a></sup>

```

Insert the supporting footnote definition near the end of the case file's note block (typically alongside footnotes n85, n86, n87, n88, n89, n90, n91 — pick the existing footnote-block region). The footnote text is:

```markdown
[^n92]: <a id="n92"></a>Robert Gurney, citizen and draper of London, will written 18 January 1621/2 and proved 23 September 1625, Archdeaconry Court of London; Source ID `acl-robert-gurney-will-1625`. Drapers' Company event records via ROLLCO: DREW4826 (1581 freedom by servitude, Robert Furnes master), DREB5398 (1597 freedom master), DRLL837 (1604 witness "Tailor, Old Change"), DRHT1669 (1617 master, John Lee apprentice of Shenley Bucks), DREW7982 (1622 master, William Holdsworth apprentice of Sowerby Bridge Yorks), DREW5638 (11 Feb 1623/4 John new freeman by redemption, Robert father), DREB1311 (1629 Marten Backhurst freedom by servitude, Robert posthumous master), DRLL2060 (3 Nov 1630 John master, Henry Smith of Kilton Suffolk new apprentice, 7-year bond); Source ID `rollco-drapers-gurney-old-change-cluster`. Stationers' Company event STMM8981 (25 March 1613 John Gurney apprentice to James Boler, no later Stationers' freedom recorded), and Joseph Hunscott Stationers' apprenticeship-master events 1612-1646 plus son John Hunscott Stationer 1641; Source IDs `rollco-stationers-gurney-1613-1626`, `rollco-stationers-hunscott-cluster`; Hunscott petition 1646 Wing H3728 Source ID `arber-stationers-bsoc-petition-1646-hunscott`. T. C. Dale, "Inhabitants of London in 1638: St. Augustine," British History Online; John Gurney £10 in MS. 67a; Joseph Huntscott £12 in MS. p. 68; Source ID `bho-london-inhabitants-st-augustine-1638`. Boyd's Inhabitants of London card `GBOR/BIL/SOG59/0240` (John Gurny of S Augustine) with free-note reading "1661 poll tax [unclear] Old Change    1638 rent £10"; Source ID `findmypast-boyds-inhabitants-london-candidate-d-gurney-cards`. Depth-of-detail analysis: `research/people/john-gurney-candidate-d.md`. Research companion cross-link: `research/people/g13-john-gurney-fact-sheet.research.md`.
```

The footnote uses a single anchor `<a id="n92"></a>` because the body cites it as `#n92` from anchor IDs `ref-92a` through `ref-92g`. If the case file's existing footnote pattern uses one-anchor-per-reference (matching `#n88a`, `#n88b`, etc.), split the footnote into n92a-n92g following the same content, repeating the relevant clause(s).

## 3. Section 11 Probability Assessment row insertion

Find the existing Section 11 probability table beginning `| Candidate | Probability | Basis |`. Insert a Candidate D row immediately AFTER the row beginning `| **C — Berkhamsted, Herts** | **ELIMINATED** |` and BEFORE the row beginning `| **Other named candidates (Unlikely / Lead)** |`.

```markdown
| **D — Son of Robert Gurney, citizen and draper / tailor of Old Change** | **Unlikely (~3-5%)** | London Drapers' father-son trade match and plausible c.1600-1604 birth window. Strong post-1625 London continuity evidence (1630 Drapers' master, 1638 St Augustine £10 rent, Hunscott will-overseer still in same parish, Boyd's-card cue to 1661 Old Change poll-tax) argues against the migration profile. No wife Mary, no matching child set, no Puritan-corridor associate, no Massachusetts bridge. See 8.4 and `research/people/john-gurney-candidate-d.md`. |
```

Also revise the existing **Unknown other origin** row so that its `~25-30%` is reduced to absorb Candidate D's probability mass. Replace the existing row with:

```markdown
| **Unknown other origin** | ~22-27% | Residual after Candidates A, C, D and the other named candidates above are accounted for. The Peter anomaly is a qualified clue rather than an absolute surname-wide absence. |
```

(Treat the Probability Assessment as a rough working scale rather than a calibrated estimator. The Candidate D mass is deliberately small but non-zero because the redemption-pathway / 1613-Stationer-binding link could still be killed by primary record work, and because a 1640-1660 image-pull might re-open the question.)

## 4. Section 12 What's Still Needed - new "For Candidate D" subsection

Find the heading `### Other Leads` near the existing Section 12 structure. Immediately BEFORE that heading and AFTER the existing `### For Strong Supporting Evidence` block ends (after the "American Gurney arms" item), insert this new subsection:

```markdown
### For Candidate D (London Drapers' / Old Change)

These items either confirm or kill Candidate D as the colonial John of Braintree. Items 1-3 are online-tractable; items 4-7 require image-pull or paid-collection access.

1. **TNA E179 1661 Free and Voluntary Present, City of London.** Boyd's Inhabitants card carries the cue "1661 poll tax [unclear] Old Change" for John Gurny of S Augustine. The 1660-1661 collection (13 Car. II, royal assent 8 July 1661) survives in TNA E179, especially the E179/253 sequence for the City. A confirmed Gurney entry at Old Change in 1661 would essentially eliminate Candidate D, since the Massachusetts John died at Boston about March 1662/3. Source ID `tna-e179-1661-london-poll-tax-deferred`.
2. **W. J. Harvey, *List of the Principal Inhabitants of the City of London, 1640***. Lambeth Palace Library MS. 272, reprinted British Library Historical Print Editions 2011. A 1640 entry for a Gurney at St Augustine would be a clean midpoint between the 1638 Dale return and the 1661 poll-tax cue. Source ID `bho-1640-principal-inhabitants-london-deferred`.
3. **Arber, *Transcript of the Registers of the Stationers' Company 1554-1640*, volume 3**. The raw 25 March 1613 entry binding John Gurney to master James Boler may preserve a father name not surfaced in the ROLLCO summary. A father reading "Robert Gurney" would essentially confirm hypothesis H-D1 and explain the Drapers' freedom-by-redemption pathway. Source ID `arber-stationers-registers-1554-1640-deferred`.
4. **LMA P69/AUG St Augustine Watling Street parish-administrative records 1625-1665.** Vestry minutes, churchwardens' accounts, poor and tithe rate books, inhabitants lists. Existing repo source `lma-st-augustine-watling-register-candidate-d-images` covers baptisms and burials only. The administrative books would directly test post-1625 household continuity.
5. **Archdeaconry Court of London and Commissary Court of London admon/will indexes 1625-1670** for Anne Gurney widow of Robert and any London John Gurney draper/tailor. The PCC search 1625-1670 returned no Anne Gurney match in this pass; lesser-court coverage is required.
6. **Stationers' Court Books for John Gurney 1613-1625**, beyond the ROLLCO summary level: turnover events, registers of testimony, freedom-by-redemption parallel entries. Useful for confirming or killing the H-D1 redemption-pathway hypothesis.
7. **27 April 1640 An Gurney + George Bucher marriage, Essex.** Image-level confirmation for the only Anne-aged Anne Gurney marriage indexed in the supplied FamilySearch sweep that could plausibly correspond to a remarriage of Anne (Morris) Gurney, widow of Robert.

```

## 5. Audit checklist

Before declaring this patchset applied, confirm each of the following case-file edits has been made:

- Section 8 candidate-table: Candidate D row inserted between Candidate C and the same-name comparators. ✅
- Section 8.4 Candidate D subsection: inserted between Section 8.3 and the existing Section 9 (Separating the Two Francis Gurneys). ✅
- Footnote n92 (or split n92a-n92g): defined in the notes block. ✅
- Section 11 Probability Assessment table: Candidate D row added with `~3-5%`; "Unknown other origin" reduced from `~25-30%` to `~22-27%`. ✅
- Section 12 "For Candidate D" subsection: inserted before "Other Leads". ✅
- Depth-of-detail content kept in `research/people/john-gurney-candidate-d.md` per v34; case-file body remains tight. ✅

## 6. Sibling patchset hand-off

This patchset is the case-file companion to `v34-john-gurney-candidate-d-phase-2-sources-and-research.patchset.md`. Apply v34 first, then v35.
