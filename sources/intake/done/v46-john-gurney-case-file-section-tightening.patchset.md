# Intake patchset v46 — John Gurney case file: §6.2 / §7 / §8 / §10 / §11 / §12 tightening

**Prepared:** 2026-05-17
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `data/sources.json` (three new FS-collection source entries)
- `research/case-files/john-gurney-case-file-v4.md` (in-place edits — primary)
- `research/people/g13-john-gurney-fact-sheet.research.md` (receives the relocated §12 research-target list)

**Status:** DRAFT — awaiting application.

## Posture

Tighten and re-anchor in place. No relocation of substantive English-origin content. Body prose and footnote text inside the case file should read as timeless statements of evidence — no "previously," "earlier indexing," "new finding," "case file update," dated-pass language, or "see internal notes" pointers. Citations point to original sources (parish-register collection, indexed FS / Findmypast collection, printed work) rather than to internal repo files. The case file remains a single cohesive document.

The §10 restructure flows the For/Against ledger to the top of the section and replaces six topical subsections with one tight prose recap; the persuasion ledger remains the heart of the section. The §8 elimination table is re-anchored under the corrected discriminator rules: continuing English residence is the strongest eliminator; marriage timing incompatible with the colonial John's English-born-children chronology (Mary G by 1628) is the next; wife-name disagreement alone is not eliminative unless paired with continuation or timing.

## Discriminator rules used by §8 reasoning (informational, not for body text)

- **Eliminative:** continuing English residence (will, burial, ongoing baptisms, hearth tax, settled trade record).
- **Eliminative:** marriage / household-formation event geographically or chronologically incompatible with the colonial John's June 1641 Weymouth appearance, or with his English-born children already in place by ~1628.
- **Eliminative:** documented trade incompatible with the colonial tailor (yeoman, shepherd, husbandman, mariner, labourer).
- **Not eliminative on its own:** wife-name disagreement, since John could have remarried before or after a Mary, and colonial children are not all proven to be Mary's offspring.
- **Not eliminative on its own:** father-of-Francis disagreement, since "not Candidate B" is not the same as "not the colonial John."
- **Not eliminative on its own:** disappearance from indexed records after a single attested event, since that is symmetric between unindexed continuation and undocumented emigration.

---

## 1. `data/sources.json` — three new FS-collection source entries

The case file currently routes most FamilySearch-indexed evidence through a single `fs-england-births-christenings` sourceId regardless of the underlying FS collection. The collections actually used in the §8 elimination chain are distinct. Add three new source entries so per-row footnotes can cite the correct collection.

**1a — Insert after the existing `fs-england-births-christenings` entry:**

```json
"fs-england-marriages-1538-1973": {
  "shortTitle": "FamilySearch England Marriages, 1538-1973",
  "citation": "England, Marriages, 1538-1973. FamilySearch indexed records.",
  "archive": "FamilySearch International",
  "url": "https://www.familysearch.org/search/collection/1473013",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "FamilySearch-indexed marriage collection. Used for parish-marriage entries where the underlying register has not been pulled at the image level."
},
"fs-england-deaths-burials-1538-1991": {
  "shortTitle": "FamilySearch England Deaths and Burials, 1538-1991",
  "citation": "England, Deaths and Burials, 1538-1991. FamilySearch indexed records.",
  "archive": "FamilySearch International",
  "url": "https://www.familysearch.org/search/collection/1538041",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "FamilySearch-indexed burial collection. Used for parish-burial entries where the underlying register has not been pulled at the image level."
},
"fs-england-norfolk-parish-registers-1510-1997": {
  "shortTitle": "FamilySearch England, Norfolk, Parish Registers (County Record Office), 1510-1997",
  "citation": "England, Norfolk, Parish Registers (County Record Office), 1510-1997. FamilySearch indexed records and images, drawn from the Norfolk Record Office collection.",
  "archive": "FamilySearch International / Norfolk Record Office",
  "url": "https://www.familysearch.org/search/collection/3957957",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Indexed and partly imaged Norfolk parish-register collection from NRO."
},
"fs-england-buckinghamshire-church-records-1217-1994": {
  "shortTitle": "FamilySearch England, Buckinghamshire, Church Records, 1217-1994",
  "citation": "England, Buckinghamshire, Church Records, 1217-1994. FamilySearch indexed records and images, drawn from the Centre for Buckinghamshire Studies.",
  "archive": "FamilySearch International / Centre for Buckinghamshire Studies",
  "url": "https://www.familysearch.org/search/collection/2376818",
  "corpusStatus": "none",
  "corpusPath": null,
  "mediaPath": null,
  "validationPath": null,
  "notes": "Buckinghamshire baptisms, marriages, and burials indexed and partly imaged through FamilySearch from the Centre for Buckinghamshire Studies."
}
```

(URLs above are the public FamilySearch collection-catalog landing pages.)

---

## 2. §6.2 Peter naming gap — replace heading and paragraph

**Old heading:** `### 6.2 The Peter Anomaly (qualified)`

**New heading:** `### 6.2 The Peter Naming Gap`

**Old §6.2 paragraph:**

> **Peter is distinctive in the colonial John's family but is not absent from Norfolk Gurney households.** A 1641 Smallburgh, Norfolk baptism (Peter G., father Peter G.) sits in the same decade the colonial John named his son Peter. None of the twelve indexed Peter-Gurney-variant baptisms 1632–1642 fathered a John-Gurney child, so Peter as the colonial son's name still calls for explanation — most likely Mary's maiden family. Identifying Mary's surname and a Peter in her kin would remain independent confirmation of John-1's origin.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>

**New §6.2 paragraph:**

> Peter is rare first name across the wider Gurney record set under research. Of twelve indexed Peter-Gurney-variant baptisms 1632–1640 across Findmypast UK Parish Baptisms, none was fathered by a John Gurney. The name therefore did not enter the colonial son's branch through any indexed Gurney parallel; the most likely source is Mary's maiden family. Recovering Mary's surname and identifying a Peter in her kin would independently confirm John's origin regardless of his father's identity.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>

(n55 already covers the FMP Peter-Gurney-variant search; no footnote change.)

---

## 3. §7 Ann Gurney — add topic-sentence opener

**Insert as the new first sentence of §7, before the existing "Ann Gurney married John Gilman …" sentence:**

> If Ann Gurney was John's sister, her marriage at Hingham and her family's New England connections place a second sibling on the Norfolk-to-New-England corridor, strengthening the corridor reading of Candidate B.

No other §7 changes.

---

## 4. §8 elimination table — row-level re-anchoring and one new row

The four candidate-row updates below each carry a fresh individual footnote (n103–n107) tied to the underlying parish-register collection or printed work. Existing row footnotes are preserved.

**4a — Cheddington, Bucks row:** move from Unlikely to ELIMINATED on continuing English residence.

Old row:
```
| Cheddington, Bucks | Buckinghamshire | Unknown | **Unlikely (~3%)** | Johannes Gurney baptized 1608, son of Richard Gurney. |
```

New row:
```
| Cheddington, Bucks | Buckinghamshire | **Rebecka** Coker (Ivinghoe 1640) | **ELIMINATED** | Continuing Bucks household: Johannes Gurney b.1608, m. Rebecka Coker Ivinghoe 1640, buried Edlesborough 1688 (residence Northall).<sup class="fn"><a href="#n103" id="ref-103">103</a></sup> |
```

**4b — Norwich (m. 1639) row:** retain Unlikely; replace elimination-reason text and add new footnote.

Old row:
```
| Norwich (m. 1639) | Norfolk | **Jane** Wright | **Unlikely (~3%)** | Wife Jane, not Mary. St Benedict, Norwich parish marriage 9 March 1639 |
```

New row:
```
| Norwich (m. 1639) | Norfolk | **Jane** Wright | **Unlikely (~3%)** | Single indexed event: marriage 1639 at Saint Benedict, Norwich; no continuation of a John + Jane Norwich household and no emigration evidence indexed.<sup class="fn"><a href="#n104" id="ref-104">104</a></sup> |
```

**4c — Aylesbury (John + Anne Cowheard) row:** retain Unlikely; replace elimination-reason text and add new footnote.

Old row:
```
| Aylesbury, Bucks (John + Anne Cowheard) | Buckinghamshire | **Anne** Cowheard | **Unlikely (~3%)** | Wife name and 1638 marriage timing make a colonial-John match unlikely (see 8.1).<sup class="fn"><a href="#n88" id="ref-88d">88</a></sup> |
```

New row:
```
| Aylesbury, Bucks (John + Anne Cowheard) | Buckinghamshire | **Anne** Cowheard | **Unlikely (~3%)** | Single indexed event: marriage 1638 at Saint Mary, Aylesbury; no continuation of household indexed and no emigration evidence.<sup class="fn"><a href="#n105" id="ref-105">105</a></sup> |
```

**4d — Ackworth, Yorkshire row:** retain Unlikely; replace elimination-reason text and append new footnote alongside the existing n93.

Old row:
```
| Ackworth, Yorkshire | Yorkshire | **Mary** Burton | **Unlikely (~2%)** | Wife is Mary, marriage in emigration-cohort window; but first child John Thomas (not Sarah), continuing Yorkshire household, and corridor mismatch keep probability at Unlikely. 1636 John Gurnoe + Mary Burton marriage and 1637 John Thomas Gurnoe baptism.<sup class="fn"><a href="#n86" id="ref-86b">86</a></sup><sup class="fn"><a href="#n93" id="ref-93a">93</a></sup> |
```

New row:
```
| Ackworth, Yorkshire | Yorkshire | **Mary** Burton | **Unlikely (~2%)** | John Gurnoe + Mary Burton m. Ackworth 6 June 1636; son John Thomas bapt Ackworth 1637; first child is John Thomas not Sarah; no further indexed Yorkshire Gurnoe activity surfaces.<sup class="fn"><a href="#n93" id="ref-93a">93</a></sup><sup class="fn"><a href="#n106" id="ref-106">106</a></sup> |
```

**4e — Hitcham, Bucks row:** retain Unlikely; replace elimination-reason text and add new footnote alongside the existing n88.

Old row:
```
| Hitcham, Bucks (John) | Buckinghamshire | Unknown | **Unlikely (~2%)** | Alive in 1631 England (Hitcham parish baptism); single primary record, mother and siblings unknown (see 8.3). |
```

New row:
```
| Hitcham, Bucks (John) | Buckinghamshire | Unknown | **Unlikely (~2%)** | Single indexed event: Mary Gurny bapt 1631 at Hitcham, father John Gurny; mother and siblings unindexed; no further Hitcham Gurney activity surfaces 1620–1665.<sup class="fn"><a href="#n88" id="ref-88c">88</a></sup><sup class="fn"><a href="#n107" id="ref-107">107</a></sup> |
```

**4f — Denton, Norfolk row:** re-anchor on continuing residence rather than wife-name.

Old row:
```
| Denton, Norfolk | Norfolk | **Rachell / Rachelle** | **ELIMINATED** | Wife is not Mary. Child Mary age does not align with the colonial Mary's 1620s birth window.<sup class="fn"><a href="#n87" id="ref-87a">87</a></sup><sup class="fn"><a href="#n89" id="ref-89a">89</a></sup> |
```

New row:
```
| Denton, Norfolk | Norfolk | **Rachell / Rachelle** | **ELIMINATED** | Continuing Denton, Norfolk household 1638–1644: children Mary 1638, Thomas 1639, Sarah 1644.<sup class="fn"><a href="#n87" id="ref-87a">87</a></sup><sup class="fn"><a href="#n89" id="ref-89a">89</a></sup> |
```

**4g — Houghton Regis, Beds row:** re-anchor on geographic incompatibility with Weymouth June 1641.

Old row:
```
| Houghton Regis, Beds | Bedfordshire | **Elizabeth** | **ELIMINATED** | Alive in 1640/41 England (John Gurney + Elizabeth marriage at Houghton Regis All Saints, 23 June 1640/41; same event indexed twice across Bedfordshire Marriages and an All-Saints parish-register transcript). Wife Elizabeth, not Mary.<sup class="fn"><a href="#n94" id="ref-94h">94</a></sup> |
```

New row:
```
| Houghton Regis, Beds | Bedfordshire | **Elizabeth** | **ELIMINATED** | Geographically incompatible with the colonial John's June 1641 Weymouth appearance: John Gurney + Elizabeth m. Houghton Regis All Saints, 23 June 1640/41.<sup class="fn"><a href="#n94" id="ref-94h">94</a></sup> |
```

**4h — St Gregory by St Paul's row:** re-anchor on trade mismatch rather than wife-name.

Old row:
```
| St Gregory by St Paul's, London (licence) | London | **Jane** Underwood | **ELIMINATED** | Alive in 1626 England (yeoman of St Clement Danes, London; marriage licence 15 November 1626 to Jane Underwood, single of St Andrew, Holborn). Wife Jane, not Mary.<sup class="fn"><a href="#n94" id="ref-94c">94</a></sup> |
```

New row:
```
| St Gregory by St Paul's, London (licence) | London | **Jane** Underwood | **ELIMINATED** | Trade mismatch (yeoman of St Clement Danes, London) with the colonial tailor; 1626 marriage to Jane Underwood of St Andrew, Holborn.<sup class="fn"><a href="#n94" id="ref-94c">94</a></sup> |
```

**4i — New row: Maldon, Essex (John, bachelor, d. 1681 — Francis G14's son by Anne Browning):** insert immediately after the existing Maldon Essex bachelor row attributed to Bernau's separate "John of Maldon" Bernau-bachelor line. Place this new row immediately before the **East Chiltington, Sussex** row in the table.

```
| Maldon, Essex (John, bachelor s/o Francis G14) | Essex | (unmarried) | **ELIMINATED** | Bachelor of St Mary's Maldon: 1674 hearth tax on nine hearths; letters of administration granted to brother Thomas Gurney 1681; second son named John in Francis G14's Anne Browning marriage.<sup class="fn"><a href="#n108" id="ref-108">108</a></sup> |
```

**4j — §2 candidate-introduction table — clarifying tweak (optional but recommended).** In the "Occupational match" row, the line `Of the other named candidates, only Candidate D shares any textile-trade link but Candidate D stays in London (see §8.4) so is not a match.` reads cleanly. No change.

---

## 5. §8.1 — demote the 8-week-gap argument

**§8.1 last paragraph (the "two Aylesbury Johns of 1638" paragraph at line 319) — replace:**

Old:
> **The two Aylesbury Johns of 1638.** A separately indexed John Gurney married Anne Cowheard at Saint Mary, Aylesbury on 25 October 1638. About eight weeks later, Candidate A's son John was baptized at the same parish on 16 December 1638. The eight-week gap rules out the two events as one couple, so 1638 Aylesbury contains two simultaneous adult John Gurneys: Candidate A continuing his family with Alice Oliffe, and a second John beginning a marriage with Anne Cowheard. The Anne Cowheard groom is independently eliminated: his October 1638 Aylesbury marriage precedes the emigrant's June 1641 Weymouth appearance, and his wife is named Anne, not Mary.<sup class="fn"><a href="#n85" id="ref-85d">85</a></sup><sup class="fn"><a href="#n88" id="ref-88b">88</a></sup>

New:
> **The two Aylesbury Johns of 1638.** A separately indexed John Gurney married Anne Cowheard at Saint Mary, Aylesbury on 25 October 1638; eight weeks later Candidate A's son John was baptized at the same parish on 16 December 1638. The two events sit in the same parish in adjacent months but belong to two simultaneous adult John Gurneys: Candidate A continuing his family with Alice Oliffe, and a second John beginning a marriage with Anne Cowheard. The Anne Cowheard groom carries no continuation of household in indexed Aylesbury records (see the §8 table row).<sup class="fn"><a href="#n85" id="ref-85d">85</a></sup><sup class="fn"><a href="#n88" id="ref-88b">88</a></sup>

The 8-week-gap argument is preserved as a fact statement but no longer carries the eliminative load that it did in the prior wording.

---

## 6. §10 restructure — tables first, prose recap, remove §10.1–§10.6 subsections

**6a — Heading reorder.** Move §10.7 (Evidence Summary) immediately under the §10 section heading, then place the new prose recap below it. Drop the §10.1, §10.2, §10.3, §10.4, §10.5, §10.6 sub-section headings entirely.

**6b — New §10 opening block.** Replace everything between `<h2 id="s10">10. THE EVIDENCE: WHY JOHN IS PROBABLY FRANCIS'S SON</h2>` and `### 10.7 Evidence Summary` with the single paragraph:

```markdown
The For-and-Against tables below condense the argument; the narrative recap that follows them sketches the same evidence in connected form.
```

Then the For/Against tables (currently §10.7 contents) appear immediately, retaining their existing structure.

**6c — Rename `### 10.7 Evidence Summary` to `### 10.1 Evidence Summary`.** Keep the For/Against table content, except for the two §10.7 table-row edits described in §7 of this patchset below.

**6d — New `### 10.2 Narrative Recap` block** placed immediately after the existing §10.7 tables and the existing companion-pointer paragraph (the paragraph beginning "For colonial-side context — Braintree burial location …"). Insert this block:

```markdown
### 10.2 Narrative Recap

The argument for John as Francis's son rests on four connected lines: trade, corridor, motive, and network.

Francis was a Merchant Taylor; the colonial John was a tailor. Trades in this period passed through family apprenticeship — fathers to sons or to fellow guild members. Of the named candidates only Candidate D shares any textile-trade link, and Candidate D's continuing London residence keeps him in London through at least 1638 and probably 1661 (see §8.4); the remaining eliminated candidates were landholders, yeomen, or shepherds.

Francis's commercial life sat inside the East Anglia → London corridor that produced roughly sixty percent of Massachusetts Bay emigrants in the 1630s and under ten percent from London proper. His parish of St Benet Fink adjoined Coleman Street Ward, where John Davenport preached until 1633; a William Gurney is recorded at St Stephen Coleman Street in the 1641-42 Protestation Returns, and a Henry Browning — sharing the surname of Francis's second wife Anne Browning — appears among the Coleman Street emigrants of the same parish.<sup class="fn"><a href="#n62" id="ref-62">62</a></sup> Francis's brother Edmund was a Cambridge-educated militant Puritan rector. The Diligent of Ipswich (Norfolk-Hingham passengers, April–August 1638, settling at Hingham, Massachusetts under ten miles from Braintree-Weymouth) is the 1638 corridor event nearest in time and place to John's June 1641 Weymouth appearance.

The motive is documented. Francis's 1634 forced sale through the Court of Wards liquidated every acre in Norfolk and Suffolk for £1,000. A son trained in the textile trade but with no land to expect had a textbook reason to seek opportunity in New England. The colonial network confirms the placement: John's son-in-law Daniel Shed was from Finchingfield, Essex; the Braintree property John occupied "by lease" sat inside the William Tyng estate of Stanford Rivers, Essex (Suffolk Deeds Liber IV); Braintree, Massachusetts itself took its name from Braintree, Essex; and Francis's second wife Anne Browning was from the same Essex-and-Maldon network.

Banks's Bury St Edmunds attribution is consistent with Candidate B rather than refuting it. Banks placed the colonial John inside a documented Bury emigrant cluster but sourced the attribution only to "Banks Mss." A Norwich-born son of Francis who trained at Bury would fit Banks's note precisely. The continuing 1653–1656 Bury Gurney household (see §8 and §8.5) means Banks's memo most plausibly tracked an earlier-departing apprentice from that Bury household — the §8.5 reading of the 1636 Newgate apprentice — rather than its head.
```

**6e — Delete old §10.1 through §10.6 subsection content** (the seven paragraphs and inline `<p>` tags currently under those subheadings). All evidentiary content they carry is either preserved in the new prose recap (10.2) or in the For/Against tables. Specifically:

- §10.1 occupational paragraph (incl. the MT binding-book paragraph): preserved by For-table rows 1 and 6 and by §8.4. Drop body subsection.
- §10.2 corridor paragraph (incl. Fischer / Thompson / Diligent): folded into the new 10.2 prose. Drop body subsection.
- §10.3 Essex network (incl. Daniel Shed, Tyng leasehold `<p>`): folded into the new 10.2 prose. Drop body subsection.
- §10.4 Coleman Street William Gurney + Henry Browning: folded into the new 10.2 prose. Drop body subsection.
- §10.5 financial-collapse motive: folded into the new 10.2 prose. Drop body subsection. (§2.3 retains the underlying financial-collapse content with nA1 author's note already present.)
- §10.6 Banks attribution + Bury 1653–1656 burials: folded into the new 10.2 prose. The continuing-Bury-household burial detail is already an ELIMINATED §8 row with its own footnote; the §10 narrative now refers to §8 rather than re-stating burial dates.

Preserve all footnote anchors that were referenced from the dropped sections (n31, n32, n61, n62, n64, n75, n77, n93, n100); they remain referenced from the new prose, from the For/Against tables, and from §8.

---

## 7. §10.1 (was §10.7) For/Against table edits

The renumbered §10.1 contains the two table-row changes below.

**7a — For Candidate B: remove row 18 (Find a Grave).**

The colonial-side burial-place context lives in the companion. Find a Grave is not English-origin evidence, and the "weak positive (location); weak negative (1615/Brent tradition)" cell muddies the persuasion ledger. Delete the row outright. Renumber rows downward (row 17 becomes the last entry; the companion-pointer paragraph below the table already covers the burial-place colonial-side angle).

**7b — For Candidate B: reframe row 7 ("Child lists not exhaustive") as "Removes a negative."**

Old row 7 cell text:
```
Daniel and Bernau show that even the better-documented St Benet Fink / Anne Browning child list was incomplete. This weakens arguments from silence, though it does not by itself prove a first-marriage son John.
```

New row 7 cell text (no other column changes):
```
Daniel Gurney's *Record* (1848) and Bernau's *British Archivist* (1913) both note that the St Benet Fink / Anne Browning child list is fragmentary. Removes the argument-from-silence against an unrecorded first-marriage son.<sup class="fn"><a href="#n30" id="ref-30b">30</a></sup>
```

(n30 already cites Daniel Gurney and Bernau's children-list caveat.)

Also change row 7's **Weight** cell from `Opens possibility` to `Removes a negative` to make the ledger framing explicit.

**7c — For Candidate B: add a new row "Francis named a second son John (Maldon bachelor, d.1681)."**

Insert as new row immediately after row 14 ("Daniel Gurney hedged on 'eldest'") and before row 15 ("Rivett cluster near East Dereham"); renumber the rows below accordingly (or, if simpler, append at the end of the table). Suggested cell content:

```
| 15 | Francis named a second son John in the Anne Browning marriage (Maldon bachelor, d. 1681) | Moderate | Bernau documents a second John Gurney son of Francis G14, born after the 1634 Visitation, paying 1674 hearth tax on nine hearths at St Mary's Maldon and dying a bachelor 1681. Demonstrates that Francis used the name John for a son in his second marriage; rebuts the inverse of the "no son named Francis" naming-pattern concern.<sup class="fn"><a href="#n108" id="ref-108">108</a></sup> |
```

**7d — Against Candidate B: add a new row "Common-name density and parish-coverage gaps."**

Append as a new row at the bottom of the Against table:

```
| 8 | Common-name density: 40+ distinct John Gurney heads-of-household across England 1600–1670; parish-register coverage gaps imply additional unidentified Johns. | Moderate negative (cumulative) | Even after elimination of the named candidates, residual unknown-corridor candidate space is materially non-zero. Reflected in §11 residuals (Unknown corridor ~15%; Unknown other corridor ~10%). |
```

No footnote: this row summarizes the cumulative §8 record set already cited row-by-row.

---

## 8. §11 Probability Assessment — minor residual tightening

**8a — "Other named candidates (Unlikely / Lead)" row Basis cell — tighten to drop Cheddington and align with §8.**

Old Basis cell:
```
Aylesbury Cowheard groom 1638, Norwich m.1639 Jane Wright groom, Cheddington 1608 Johannes, Hitcham 1631, Ackworth Mary Burton, and similar single-attestation rows. Each has no current solid eliminator but no positive linkage to the colonial John either; see §8 for row-level reasoning.
```

New Basis cell:
```
Aylesbury Cowheard groom 1638, Norwich m.1639 Jane Wright groom, Hitcham 1631, Ackworth Mary Burton, and similar single-attestation rows; each is a one-event household in indexed records with no continuation and no positive emigration linkage to the colonial John. Probability dropped from ~5% to ~4% with Cheddington 1608 moving to ELIMINATED.
```

Probability cell update: `~5% combined` → `~4% combined`.

**8b — Unknown corridor residual rows: tighten Basis cells to reference common-name density explicitly.**

Old "Unknown corridor (East Anglia / London)" Basis:
```
Residual for an undiscovered candidate in the dominant emigration corridor. The recurring failure to find an indexed John+Mary marriage in eastern-England parish registers 1620-1635 reflects parish-coverage gaps and keeps this bucket open.
```

New Basis:
```
Residual for an undiscovered candidate in the dominant emigration corridor. Over forty distinct John Gurney heads-of-household are documented across English parishes 1600–1670, of which only a subset is covered by current indexed registers; the recurring failure to find an indexed John + Mary marriage in eastern-England parish registers 1620–1635 reflects parish-coverage gaps rather than absence.
```

(The "Unknown other corridor (Kent, Lincs, West Country)" row is unchanged.)

**8c — Numerical recheck.** B ~60 + D ~5 + Other named ~4 + Unknown corridor ~16 + Unknown other ~10 = ~95; with rounding the band still reads cleanly as approximately 100. Increase Unknown corridor from ~15% to ~16% in the Probability cell to keep the total within rounding.

---

## 9. §12 — relocate to the G13 research companion

§12 ("WHAT'S STILL NEEDED") is operational research planning, not part of the published case argument. Move its content out of the case file and into the G13 research companion under the existing "Target Source Pulls / Not Yet Searched" section.

**9a — Delete `<h2 id="s12">12. WHAT'S STILL NEEDED</h2>` and all subsections under it** in the case file. The bibliography section currently keeps id `s13`; renumber that anchor to `s12` to close the gap, and update the `caseNav` href list (`{ label: "Bibliography", href: "#s13" }` → `{ label: "Bibliography", href: "#s12" }`). Pre-apply check: `grep -r "#s12\|#s13\b" .` to catch external linkbacks.

**9b — Append into `research/people/g13-john-gurney-fact-sheet.research.md`** under the existing `## Target Source Pulls / Not Yet Searched` heading, after the existing "Anderson citation pull list" and "Broader source catalog" subsections. Insert the following new subsection (verbatim — content lifted from the case file's §12, with explicit "case file" and "round" framing stripped and dated-pass language removed):

```markdown
### Highest-leverage targets (relocated from the case file)

These targets sit beyond the freely-indexed online corpus and require paid pulls, archive visits, or research-services enquiries. Each item has the potential to materially move Candidate B above 80% confidence or to surface a competing positive attribution.

1. **NRO Norwich Consistory Court / Archdeaconry Court catalogue.** Edmund Gurney G14b (the Divine) will, d. 14 May 1648 buried St Peter Mancroft, Norwich. Henry Gurney G15 will, d. 23 February 1615 (probate 1623 per Daniel Gurney). Either will, if extant, could name nephews or grandchildren in New England.
2. **Commissary Court of London-Essex-Herts, 1681 admin file** for John Gurney of Maldon (Bernau's bachelor John, admin granted to brother Thomas). The grant may list other surviving siblings — including any reference to a previously-deceased "brother John of New England" if the Candidate B identification holds.
3. **Suffolk Record Office HD2418/88** Ryvett family pedigrees, plus Suffolk wills 1620-1660 for Ryvett witnesses naming Gurney nieces or grandchildren.
4. **East Dereham parish-register further image-walk.** Open items: year fields on the Marye and Agnes burials (year-truncated in the visible crop); Margaret Rybett burial 1615-1618 elsewhere in the register; confirmation of the preliminary "Margaret daughter of ffrancis Gurnoe/Gurney bapt may 25" reading.
5. **TNA Star Chamber STAC 8/281/24** (Trentham v Withes, November 1620): the named defendants include Henry Reade, his sister Mary Reade, and Henry Gurney. Plaintiff is Staffordshire-based; the Henry Gurney involved is most plausibly a Midlands Henry. A paid PDF or in-person pull would identify the Henry Gurney definitively and test any Reade-family-Gurney-connection lead.
6. **William Tyng probate** (d. 18 January 1653 Braintree, MA; will / inventory should be in Suffolk County MA Probate Liber 1). The inventory would itemize the Braintree leasehold to John Gurney as named tenant.
7. **Sir Henry Spelman manuscript pedigree.** Bernau (1913) reports that "a Francis Gournay" gave Sir Henry Spelman a manuscript Gourney pedigree; the 1616 Francis Spelman apprenticeship to Francis G14 (Scott 2024 UKDA-9263) supplies a concrete vector. Candidate repositories: CUL MS Add. (Spelman collection), Bodleian MS Eng. hist., BL Add. MSS (Spelman transcripts), College of Arms.
8. **NEHGR vol. 22 p. 44** John Gurney reference. Internet Archive coverage of NEHGR vol. 22 (1868) is patchy by web URL; a targeted FS-Library or Google Books pull should resolve it.
9. **Mary Anne of Yarmouth 1637 + Susan & Ellen of Yarmouth 1635 passenger lists** for Gurney variants. These two Yarmouth, Norfolk → Massachusetts ships span the John Gurney emigration window and have partial surviving passenger lists not yet pulled.

#### Strong supporting targets

1. **Margaret Rybett burial.** East Dereham, Norwich, Garveston, Gressenhall, or Shipdham c.1616–1617.
2. **Ryvett/Rivett pedigrees.** Suffolk Record Office, HD2418/88.
3. **Francis Gurney's will or administration.** PCC indexes 1637–1660; Archdeaconry of Norwich; London Commissary Court.
4. **American Gurney arms.** Locate the earliest object, seal, Bible, bookplate, gravestone, manuscript, or family paper preserving the arms used by the American Gurneys; determine the exact blazon and whether the usage predates printed antiquarian borrowing.

#### Candidate D (London Drapers' / Old Change) — confirmation or kill targets

1. **TNA E179 1661 Free and Voluntary Present, City of London.** Boyd's Inhabitants card carries the cue "1661 poll tax [unclear] Old Change" for John Gurny of S Augustine. A confirmed Gurney entry at Old Change in 1661 would essentially eliminate Candidate D, since the Massachusetts John died at Boston about March 1662/3.
2. **W. J. Harvey, *List of the Principal Inhabitants of the City of London, 1640.*** Lambeth Palace Library MS. 272, reprinted British Library Historical Print Editions 2011.
3. **Arber, *Transcript of the Registers of the Stationers' Company 1554-1640*, volume 3.** The raw 25 March 1613 entry binding John Gurney to master James Boler may preserve a father name not surfaced in the ROLLCO summary.
4. **LMA P69/AUG St Augustine Watling Street parish-administrative records 1625-1665.** Vestry minutes, churchwardens' accounts, poor and tithe rate books, inhabitants lists.
5. **Archdeaconry Court of London and Commissary Court of London admon/will indexes 1625-1670** for Anne Gurney widow of Robert and any London John Gurney draper/tailor.
6. **Stationers' Court Books for John Gurney 1613-1625** beyond ROLLCO summary level.
7. **27 April 1640 An Gurney + George Bucher marriage, Essex.** Image-level confirmation for the only Anne-aged Anne Gurney marriage indexed in the FamilySearch sweep that could plausibly correspond to a remarriage of Anne (Morris) Gurney, widow of Robert.

#### Other leads

1. **Haberdashers' Company 1632 apprentice.** A John Gurney was reportedly apprenticed to the Haberdashers' Company in 1632, but the Findmypast London Apprenticeship Abstracts walk returned zero Gurney results. Re-identify the original source.
2. **St Ann Blackfriars baptism, 1615.** A John Gurney baptism lists the father as "P Gurney." In early 17th-century handwriting, F and P are easily confused; the original register image has not been examined.
3. **Medmenham, Buckinghamshire parish register.** FamilySearch Tree profile LT9Z-KQ1 has a restricted attached item titled "The parsons and parish registers of Medmenham, Buckinghamshire" with user note "Richard gurney marriage."
4. **Gillingham, Norfolk, 5 November 1624 — Mary Garny daughter of Frances Garny.** Pull the Gillingham parish register context (other Garny/Gurney baptisms 1620-1640 at Gillingham) to test whether Frances Garny's other children match Francis G14's known family.

#### Non-leads

1. **"Mary Richards" maiden-name attribution.** Ancestry user-tree attribution with no primary record. Do not carry as an open lead unless a primary source for the Richards surname surfaces.

#### Enrichment

1. **Braintree town manuscript vital records, film 940974 / DGS 7009769** — original/copy manuscript pages behind the 7th month 20, 1661 wife-death entry and the 9th month 12, 1661 Grizell Kidbee marriage entry.
2. **Suffolk Probate Records Case #338** — full itemized inventory and debtor/creditor transcription.
3. **Suffolk Court Files item no. 188** — underlying file behind the 1652/3 Braintree age note.
4. **Original Braintree town/vital/deed entries** — especially the 1661 wife death/marriage context and the 12 Feb. 1661 Richard Thayer conveyance behind Bates.
5. **Lysander-family manuscript / arms object** — the 1912/AccessGenealogy tradition points to family-held material.
6. **St Stephen Coleman Street parish registers** — full Gurney search 1600–1660.
7. **Berkhamsted marriage registers** — further register work may clarify Candidate C's wife and household.
8. **Stewkley Dickson/Putnam 1897 register pull** — Tier 2 context.

#### Anderson reference-control checklist

Anderson's John Gurney sketch cites WJ 2:422, MBCR 1:331, NEHGR 62:94, SPR Case #338, Weymouth Hist 3:251, and TAG 10:70-73. WJ and MBCR are tied to Winthrop/Savage and Massachusetts Bay Records entries; Weymouth Hist and NEHGR 62:94 are partially incorporated; TAG 10:70-73 is Holman's Grissell marriage-chain article with no 1636 date for John Gurney; SPR Case #338 is image-verified at FamilySearch. Remaining pulls: full SPR Case #338 itemized transcription and the Braintree manuscript vital-record pages behind the 1661 wife-death and marriage conflict.
```

---

## 10. New case-file footnotes — insert before the closing `</ol>` of the citation index

These six footnotes carry the individual citations for the §8 row updates, the new Maldon-bachelor row, and the new For-table row.

```html
<li id="n103" value="103">FamilySearch, "England, Births and Christenings, 1538-1975," Johannes Gurney baptized 5 August 1608, Cheddington, Buckinghamshire, parents Richardi Gurney and Jana, religion Anglican; FamilySearch, "England, Marriages, 1538-1973," Johannes Gurney + Rebecka Coker, marriage 22 October 1640, Ivinghoe, Buckinghamshire; FamilySearch, "England, Buckinghamshire, Church Records, 1217-1994," Johannes Gurney burial 13 May 1688, Edlesborough, Buckinghamshire, religion Anglican, residence Northall. The same individual continues in indexed Buckinghamshire records from 1608 through 1688, ruling out emigration to Massachusetts by 1641. Source IDs <code>fs-england-births-christenings</code>, <code>fs-england-marriages-1538-1973</code>, <code>fs-england-buckinghamshire-church-records-1217-1994</code>. <a class="backref" href="#ref-103">↩</a></li>

<li id="n104" value="104">FamilySearch, "England, Norfolk, Parish Registers (County Record Office), 1510-1997," John Gurny + Jane Wright, marriage 9 March 1639, Saint Benedict, Norwich, Norfolk; cross-indexed in FamilySearch, "England, Marriages, 1538-1973." A surname-with-variants search of Findmypast Life Events (Births &amp; Baptisms, Deaths &amp; Burials) and FamilySearch Records for indexed Norwich Gurney baptisms 1639–1660 with father John and mother Jane, and for any Norwich John Gurney burial 1639–1680, returns no continuation of this household and no emigration evidence. Source IDs <code>fs-england-norfolk-parish-registers-1510-1997</code>, <code>fs-england-marriages-1538-1973</code>, <code>findmypast-uk-parish-baptisms</code>. <a class="backref" href="#ref-104">↩</a></li>

<li id="n105" value="105">FamilySearch, "England, Marriages, 1538-1973," Anne Cowheard + John Gurney, marriage 25 October 1638, Aylesbury, Buckinghamshire (FamilySearch ID <code>N2TD-Z9Z</code>). No subsequent baptisms or burials tying this John + Anne Cowheard couple together surface in Findmypast Buckinghamshire Baptism, Marriage, or Burial indexes or in FamilySearch indexed records. The separately documented Wing John + Anne Gurney household (Wing parish baptisms 1650–1652) is independently eliminated on continuing residence and is not this couple. Source IDs <code>fs-england-marriages-1538-1973</code>, <code>findmypast-bucks-baptism-index</code>, <code>findmypast-bucks-burial-index</code>, <code>findmypast-bucks-marriage-index</code>. <a class="backref" href="#ref-105">↩</a></li>

<li id="n106" value="106">Ackworth Yorkshire household continuation: no John Gurney/Gurnoe burial in Yorkshire 1637–1700 surfaces in Findmypast Life Events (Deaths &amp; Burials) or in the National Burial Index for England &amp; Wales (Yorkshire section); no further indexed Yorkshire Gurnoe baptisms after John Thomas Gurnoe (Ackworth, 19 January 1637) across Findmypast Yorkshire Baptisms or FamilySearch indexed records 1637–1665. The household disappearance is symmetric between unindexed parish-coverage continuation and undocumented emigration, so the Ackworth row is held at Unlikely rather than moved to ELIMINATED pending a parish-register image pull at Ackworth and surrounding Yorkshire parishes. Source IDs <code>findmypast-uk-parish-baptisms</code>, <code>fs-england-births-christenings</code>, <code>findmypast-ackworth-gurnoe-burton-marriage-1636</code>, <code>findmypast-ackworth-gurnoe-baptism-1637-john-thomas</code>. <a class="backref" href="#ref-106">↩</a></li>

<li id="n107" value="107">Hitcham Buckinghamshire household continuation: a search of Findmypast Buckinghamshire Baptism, Marriage, and Burial indexes and FamilySearch indexed records for further Hitcham Gurney activity 1620–1665 returns no additional entries beyond Mary Gurny baptism 22 January 1631 (father John Gurny, mother unindexed). The household appears once in indexed records; mother and siblings remain unindexed. Source IDs <code>findmypast-bucks-baptism-index</code>, <code>findmypast-bucks-burial-index</code>, <code>findmypast-bucks-marriage-index</code>, <code>fs-england-births-christenings</code>. <a class="backref" href="#ref-107">↩</a></li>

<li id="n108" value="108">Bernau, Charles A. "Unrecorded Biographies: Francis Gournay (or Gurney), of Maldon, Essex." <em>The British Archivist</em>, vol. I, no. 7 (September 1913), "His Parents' Children" section, item 9: "in 1681 letters of administration of the goods of John GURNEY, of Maldon, a bachelor, were granted to his brother, Thomas GURNEY"; same section, item 9: "in 1674 John GURNEY, of St. Mary's Maldon, paid the tax on nine hearths" (citing Lay Subsidy 246/22). A second son named John in Francis G14's marriage to Anne Browning, born after the 1633/4 Heralds' Visitation, continuing English residence through 1674 and dying a bachelor 1681; independently eliminated as the Massachusetts emigrant by bachelor status and by continuing English residence. Source ID <code>british-archivist-bernau-1913</code>. <a class="backref" href="#ref-108">↩</a></li>
```

---

## 11. Pre-apply integrity checks

- `grep -n "#n103\|#n104\|#n105\|#n106\|#n107\|#n108" research/case-files/john-gurney-case-file-v4.md` — confirms ref-anchor placement matches the new footnotes.
- `grep -nc "ELIMINATED\b" research/case-files/john-gurney-case-file-v4.md` should increase by 2 (Cheddington row moves to ELIMINATED; new Maldon-bachelor row added).
- `grep -n "Unlikely (~3%)\|Unlikely (~2%)" research/case-files/john-gurney-case-file-v4.md` after edits should still show four Unlikely rows (Norwich Jane Wright, Aylesbury Cowheard, Hitcham, Ackworth) plus Candidate D at Unlikely (~5%).
- `grep -nE "#s1[23]\b" research/case-files/john-gurney-case-file-v4.md` should return only the renumbered bibliography anchor `#s12` and the front-matter `caseNav` entry; no `#s13` remains.
- JSON validity check on `data/sources.json` after the four-entry insertion.
- `grep -n "10\\.1\|10\\.2\|10\\.3\|10\\.4\|10\\.5\|10\\.6\|10\\.7" research/case-files/john-gurney-case-file-v4.md` — confirms the old §10.1–§10.7 subsection headings are gone and only the new §10.1 (Evidence Summary) and §10.2 (Narrative Recap) remain.

## Reviewer checklist

- [ ] §6.2 heading renamed; paragraph rewritten with topic sentence up front
- [ ] §7 topic-sentence opener added
- [ ] §8 table — Cheddington row moves to ELIMINATED with n103
- [ ] §8 table — Norwich Jane Wright row reason re-anchored on single-event-no-continuation with n104
- [ ] §8 table — Aylesbury Cowheard row reason re-anchored with n105
- [ ] §8 table — Ackworth row reason tightened with n106
- [ ] §8 table — Hitcham row reason tightened with n107
- [ ] §8 table — Denton row re-anchored on continuing residence
- [ ] §8 table — Houghton Regis row re-anchored on geographic incompatibility
- [ ] §8 table — St Gregory by St Paul's row re-anchored on trade mismatch
- [ ] §8 table — new Maldon-bachelor row inserted with n108
- [ ] §8.1 — 8-week-gap argument demoted to fact-statement; no longer carries elimination load
- [ ] §10 restructure — tables moved to top; six subsections collapsed into 10.1 (tables) and 10.2 (prose recap)
- [ ] §10.1 For-table — row 18 (Find a Grave) deleted; row 7 reframed as "Removes a negative"; new Maldon-bachelor row inserted
- [ ] §10.1 Against-table — new common-name-density row appended
- [ ] §11 — residual cells tightened; Other named candidates drops to ~4%; Unknown corridor at ~16%
- [ ] §12 — heading and content removed from case file; bibliography anchor renumbered `s13` → `s12`; `caseNav` href updated; relocated content appended to `research/people/g13-john-gurney-fact-sheet.research.md` under "Target Source Pulls"
- [ ] Six new footnotes (n103-n108) inserted before the closing `</ol>`
- [ ] Four new sources added to `data/sources.json`
- [ ] Pre-apply integrity checks pass

## Notes for follow-up patchsets (not part of v46)

- **G14 fact sheet — Bernau children-list reconciliation.** The current `fact-sheets/g14-francis-gurney-fact-sheet.md` children table differs from Bernau's (1913) numbered list at five rows (Frances 1625/6 vs Francis 1625, Lucretia 1630 vs Margaret 1630, Margaret 1637 vs Mary 1637, missing Thomas 1636, missing post-1634 John). Reconciliation requires pulling the St Benet Fink baptism register directly (LMA P69/BEN1/A/001 and /002, indexed by FamilySearch and Ancestry through the London Metropolitan Archives parish-register collection). Open as a separate patchset once the LMA pull is in hand. Do not modify the G14 fact sheet in v46.
- **Bernau second-John row** in the case file (added as §8 4i above) carries an outside Bernau citation. Cross-link from `research/people/g14-francis-gurney-fact-sheet.research.md` already covers the same Bernau evidence under "The second John."
