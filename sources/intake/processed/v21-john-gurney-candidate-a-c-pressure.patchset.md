# Intake patchset v21 - John Gurney Candidate A and C pressure

```yaml
patchset_id: v21
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after review and after v20. Do not create corpus-supplement files for the Phillimore extract; it lives in research with a thin validation.
```

## 0. Audit report

### 0.1 Scope

Pass 3 was scoped to find online evidence that lowers or eliminates Candidate A (Stewkley/Edlesborough Bucks, b. 1602/3, wife Alice Collindridge) and the residual non-B candidates. Two concrete pulls warrant case-file edits:

1. **Phillimore *Buckinghamshire Parish Registers - Marriages*, vol. 1** (Internet Archive `buckinghamshirep01phil`). The Edlesborough section yields a marriage of "Joh. Gurney & Mary Kidgell" in 1661 plus three other Bucks Gurney marriages 1660-1685.
2. **Older repo notes (V6/V7/Protestation Returns Analysis)** preserve two strong but unpublished-in-the-case-file Cand A eliminators: TNA E 115/180/113 (1641 certificate of residence, John Gurney moving from Aylesbury half-hundred to Northamptonshire) and a 1650 John Gurney tenancy at Walgrave, Northamptonshire. These are dated, repo-internal datapoints; v21 would surface them in the case file's §8 elimination row.

### 0.2 Lead triage outcome

| Lead | Work done | Outcome | Incorporation decision |
|---|---|---|---|
| Phillimore Bucks vol. 1 (Edlesborough/Cheddington/etc.) | Full text read on archive.org | **Obtained.** Edlesborough marriages section: `Joh. Gurney & Mary Kidgell` 1661; `Wm. Gurney & Martha Halsey` 1660; `Saml. Gurney, of Bierton, & Elizab. Bunce, of Padbury` 1662; `Tho. Gurney, of Hockliffe, & Frances Norman, of Houghton Regis` 1680; `Geo. Hill, of Chesham, & Mary Gurney` 1685. | Add row to §8 elimination table for "Edlesborough Bucks, John Gurney & Mary Kidgell 1661"; add Phillimore source + thin validation. |
| TNA E 115/180/113 (1641 cert of residence Aylesbury → Northants) | Cited in `Gurney_ProtestationReturns_Analysis.md`; not yet pulled to TNA Discovery image | Repo-internal datapoint without an attached image. Surfacable as a Cand A eliminator in the case file with a "noted but image not yet pulled" qualifier. | Surface in §8 Cand A row replacing the bare "Moved to Northants" phrase. Keep the source as a research note, not a primary footnote, until the TNA image is pulled. |
| 1650 John Gurney tenant at Walgrave, Northamptonshire | Cited in `Gurney_ProtestationReturns_Analysis.md`; underlying source not in repo | Same status as above: repo-internal datapoint. | Surface in §8 Cand A row alongside TNA E 115/180/113. |
| Stewkley parish register (Dickson/Putnam 1897) | Located. Covers baptisms 1545-1653, marriages 1599-1646, burials 1599-1653 — the full Cand A diagnostic window. Free-online text not located; available paywalled on Geneanet Premium and Genealogy Store. | **High-value but paywalled.** Cannot be folded into v21. | Add to G13 target source pull list as Tier-1 paywall target with explicit Geneanet handle and Genealogy Store handle. |
| VCH Bucks vol. 3 Stewkley | Re-read; only post-1687 manor-holding Gurney material; no Cand A diagnostic content. | No new finding for Cand A. | No change. |
| VCH Bucks vol. 3 Edlesborough | Read in full. **Zero Gurney landholders.** Edlesborough Gurney presence is yeoman/non-manorial. | Useful negative result for context. | One-sentence note in G13 against the Edlesborough cluster. |
| Berkhamsted Cand C, FreeREG/parish | FreeREG indexes Gurney surname at St Peter Berkhamsted but does not surface the 1626 Richard / 1634 Sara baptisms in a freely usable record-level view in this pass. Hertfordshire Archives / Findmypast required. | Inaccessible in this pass. | No change. Park as paywall target. |
| Ackworth Yorkshire John + Mary Barton | No online context found | Inaccessible | No change. Park. |
| Alice Collindridge marriage / burial | No primary or printed-transcription record found in this pass | Inaccessible without paid Bucks parish access | No change. Park. |

### 0.3 Candidate implications

- **Candidate A (Stewkley/Edlesborough, Bucks, b. 1602/3, wife Alice Collindridge):** The 1661 Edlesborough "John Gurney + Mary Kidgell" marriage is a direct active-Bucks-John-marrying-a-Mary record in the same year the colonial John buried his Mary in Massachusetts. Whether this is the same individual as Cand A or a different Bucks John, it tightens the elimination context. Combined with the existing repo-internal TNA E 115/180/113 / Walgrave Northants 1650 datapoints, the case for Cand A elimination is materially stronger than the case file currently expresses. Recommendation: keep the ~8-10% probability for now (the Stewkley register is the discriminating pull) and surface the new evidence so the next reader sees the actual basis for the low number rather than a thin elimination row.
- **Candidate C (Berkhamsted, Herts):** No new evidence in this pass. Probability unchanged at ~3-5%.
- **Residual "Unknown other origin":** The 1661 Mary Kidgell marriage and the 1660-1685 Bucks Gurney marriage cluster reduce the residual bucket marginally by adding a previously unseen Bucks "John + Mary" household to the elimination pool. Not enough to revise the table.

## 1. Source registry operation

Before applying, verify the proposed source ID is still absent:

```powershell
Select-String -Path data\sources.json -Pattern "phillimore-bucks-marriages-vol1"
```

Add this object near the existing England parish-register sources in `data/sources.json`:

```json
    "phillimore-bucks-marriages-vol1": {
      "shortTitle": "Phillimore Bucks parish registers, marriages, vol. 1",
      "fullTitle": "Buckinghamshire Parish Registers: Marriages, Volume I",
      "editor": "W. P. W. Phillimore and Thomas M. Blagg",
      "publisher": "Phillimore & Co., London",
      "year": 1902,
      "type": "parish register (printed transcription)",
      "url": "https://archive.org/details/buckinghamshirep01phil",
      "notes": "Marriages for Cheddington, Cholesbury, Edlesborough, Hawridge, Marsworth, Mentmore, Pitstone, Slapton, Soulbury. Includes 1660-1685 Edlesborough Gurney marriage cluster: Joh. Gurney & Mary Kidgell 1661; Wm. Gurney & Martha Halsey 1660; Saml. Gurney of Bierton & Elizab. Bunce of Padbury 1662; Tho. Gurney of Hockliffe & Frances Norman of Houghton Regis 1680; Geo. Hill of Chesham & Mary Gurney 1685."
    }
```

## 2. Validation note (proposed thin file)

Create `sources/validations/phillimore-bucks-marriages-vol1.md`:

```markdown
# Validation - Phillimore Bucks parish registers, marriages, vol. 1

- Source ID: `phillimore-bucks-marriages-vol1`
- Title: *Buckinghamshire Parish Registers: Marriages, Volume I*, ed. W. P. W. Phillimore and Thomas M. Blagg.
- Online: https://archive.org/details/buckinghamshirep01phil
- Method: Internet Archive full-text OCR derivative searched for `Gurney`, `Gourney`, `Gurny`, `Gurnie`.
- Use in Gurney research: cited in `research/case-files/john-gurney-case-file-v4.md` §8 elimination table (Edlesborough 1661 John Gurney + Mary Kidgell row) and in `research/people/g13-john-gurney-fact-sheet.research.md` for the broader 1660-1685 Bucks Gurney marriage cluster. Page-image verification of each entry recommended before quoting in published narrative.
```

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 Add a row to the §8 elimination table

Insert after the existing "Edlesborough"-relevant rows in the §8 table (i.e., near the existing Cand A row or at the end of the eliminator block):

```markdown
| Edlesborough, Bucks (Joh. Gurney & Mary Kidgell, 1661) | Bucks | **Mary** Kidgell | **ELIMINATED** | A John Gurney married Mary Kidgell at Edlesborough, 12-month window 1661. The colonial John buried his wife Mary at Braintree on 20 Sept. 1661 and married Grizzell Fletcher at Braintree on 12 Nov. 1661, so this Bucks John cannot be the same person. Provides a previously unseen Bucks "John + Mary" household for the elimination pool and tightens the post-1641 Bucks Gurney activity record relevant to Candidate A.<sup class="fn"><a href="#nXX" id="ref-XX">XX</a></sup> |
```

Add new endnote (number to assign on application; current endnotes run through `n71` and v20 already proposes one new note):

```html
<li id="nXX" value="XX">Phillimore Bucks parish registers, marriages, vol. 1, Edlesborough section, marriage entry "Joh. Gurney & Mary Kidgell" 1661; W. P. W. Phillimore and Thomas M. Blagg, eds., <em>Buckinghamshire Parish Registers: Marriages, Volume I</em> (London: Phillimore & Co.), Internet Archive, <a href="https://archive.org/details/buckinghamshirep01phil">https://archive.org/details/buckinghamshirep01phil</a>. Source ID: <code>phillimore-bucks-marriages-vol1</code>. <a class="backref" href="#ref-XX">↩</a></li>
```

### 3.2 Replace the existing Candidate A row's "Moved to Northants" phrase with the actual cited sources

Old §8 Cand A row "Primary Elimination Reason" cell:

```
Wife named Alice, not Mary. Son Jonathan baptized 1647 = still in England. Moved to Northants.
```

New cell:

```
Wife named Alice, not Mary. Son Jonathan baptized at Aylesbury 22 Nov. 1647 (parish register, Aylesbury, Bucks) — a John Gurney still fathering children in England six years after the colonial John's first Massachusetts record. Continuing presence in England documented by TNA E 115/180/113 (1641 certificate of residence for John Gurney moving from Aylesbury half-hundred to Northamptonshire) and by John Gurney as a tenant at Walgrave, Northamptonshire in 1650. Whether the Stewkley-baptized Cand A is the same person as the Aylesbury-Walgrave John or a separate household, both lines of evidence keep an English John Gurney active in this geographic corridor through the 1640s and 1650s.<sup class="fn"><a href="#nYY" id="ref-YY">YY</a></sup>
```

Add new endnote (number to assign on application):

```html
<li id="nYY" value="YY">Aylesbury parish register, Buckinghamshire, baptism entry for Jonathan Gurney son of John Gurney, 22 November 1647, as recorded in the project research notes at <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_ProtestationReturns_Analysis.md</code>; The National Archives, Kew, E 115/180/113, certificate of residence for John Gurney moving from Aylesbury half-hundred to Northamptonshire, 1641, recorded in the same research note; John Gurney as tenant at Walgrave, Northamptonshire, 1650, recorded in <code>research/case-files/Initial foundation work for john-gurney-case-file/Gurney_Research_Findings_V7.md</code>. The underlying TNA image and the Walgrave tenancy source have not been independently pulled in this pass; promote either to a footnoted primary record only after the originating image or document is examined. <a class="backref" href="#ref-YY">↩</a></li>
```

### 3.3 §13.2 Primary Sources table — add a Phillimore row

Add a row to the existing §13.2 table:

```markdown
| 12 | Edlesborough Bucks marriage, John Gurney & Mary Kidgell, 1661 | Phillimore Bucks Marriages vol. I (1902); Internet Archive `buckinghamshirep01phil` | Parish register (printed) |
```

## 4. Proposed G13 research-file edits (research/people/g13-john-gurney-fact-sheet.research.md)

### 4.1 Append a new section under "Origin Analysis and Elimination Work"

Insert after the existing "TNA probate - context records" subsection:

```markdown
### Bucks Gurney marriage cluster, 1660-1685 (Phillimore vol. I)

Phillimore *Buckinghamshire Parish Registers - Marriages*, vol. I, Edlesborough section, prints a tight cluster of Gurney marriages in the second half of the seventeenth century:

- Wm. Gurney & Martha Halsey, 1660
- Joh. Gurney & Mary Kidgell, 1661
- Saml. Gurney, of Bierton, & Elizab. Bunce, of Padbury, 1662
- Tho. Gurney, of Hockliffe, & Frances Norman, of Houghton Regis, 1680
- Geo. Hill, of Chesham, & Mary Gurney, 1685

The 1661 John-and-Mary marriage is materially incompatible with the colonial John Gurney-1: the colonial John buried his first wife Mary at Braintree on 20 September 1661 and married Grizzell Fletcher on 12 November 1661 at Braintree. Either this Edlesborough John is the same person as Candidate A (in which case Candidate A is eliminated outright by the 1661 Bucks marriage), or he is a separately documented Bucks John Gurney with a Mary wife — in which case he depletes the residual "Unknown other origin" bucket by accounting for one more Bucks "John + Mary" household. The cluster also corroborates the 1642 Bucks Contributions for Ireland reading of a continuing Edlesborough yeoman Gurney presence and is consistent with VCH Bucks vol. 3 Edlesborough showing zero Gurney landholders at the manorial level — i.e., the Edlesborough Gurneys were yeoman, not gentry.[^phillimore-bucks-vol1]

[^phillimore-bucks-vol1]: W. P. W. Phillimore and Thomas M. Blagg, eds., *Buckinghamshire Parish Registers: Marriages, Volume I* (London: Phillimore & Co.), Edlesborough section; Internet Archive, https://archive.org/details/buckinghamshirep01phil. Source ID: `phillimore-bucks-marriages-vol1`.
```

### 4.2 Add the Stewkley Dickson/Putnam 1897 register to the target source pull list

Insert into the §"Target Source Pulls / Not Yet Searched" Tier 1B block:

```markdown
- **Stewkley parish register (Dickson/Putnam 1897 print)** — Rev. R. Bruce Dickson, *The Parish Register of Stewkeley, Buckinghamshire, 1545-1653* (Salem, Mass.: Eben Putnam, 1897), covering baptisms 1545-1653, marriages 1599-1646, burials 1599-1653. Covers the entire Candidate A diagnostic window. Paywalled in this pass at Geneanet Premium (https://en.geneanet.org/library/doc/5574493/...) and at the Genealogy Store (https://www.thegenealogystore.co.uk/index.php?main_page=product_info&products_id=1204). Highest single discriminating pull for closing or strengthening Candidate A.
```

### 4.3 Refine the existing "Open Questions" list

Replace the bullet:

```markdown
- [ ] Reassess whether **Candidate C (Berkhamsted John)** can be tied to or excluded from the emigrant.
```

With:

```markdown
- [ ] Pull Hertfordshire Archives / Findmypast Berkhamsted St Peter parish register for: (a) any John Gurney + Mary marriage 1620-1640; (b) burial of Richard Gurney baptised 1626; (c) burial of Sara Gurney baptised 1634; (d) any further John Gurney activity post-1641. FreeREG indexes the surname at St Peter Berkhamsted but did not surface the 1626/1634 baptisms or any post-1641 entries in the 2026-05-09 pass.
```

## 5. Apply order

When approved (after v20 is applied):

1. Add `phillimore-bucks-marriages-vol1` to `data/sources.json`.
2. Create `sources/validations/phillimore-bucks-marriages-vol1.md` (thin).
3. Edit `research/case-files/john-gurney-case-file-v4.md` per §3 (new elimination row + Cand A row text + §13.2 table row).
4. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4 (Phillimore cluster section + Stewkley register pull-list entry + Berkhamsted Open Questions wording).
5. Update `sources/intake/working/john-gurney-audit-state.md` to mark v21 as applied.
