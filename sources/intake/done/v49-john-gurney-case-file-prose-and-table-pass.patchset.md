# Intake patchset v49 — John Gurney case file prose, table, and citation pass

**Prepared:** 2026-05-18
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Target files:**
- `research/case-files/john-gurney-case-file-v4.md` — §1 source attributions; §2.1 + §1 hyperlinks; §6.1 rework with expanded table; §8.1/§8.2/§8.3 topic sentences; §8.1 two-Aylesbury-Johns paragraph removed; §8.3 inclusion-logic note + Amersham row; §8.4 + §8.5 internal-pointer footnote consolidation; §10 orphan paragraph removal; §10.1 For- and Against-tables reordered strongest-to-weakest; §10.1 Against row 1 reframed on the 1603/c.1609 age mismatch; action-item phrases removed throughout; global adjacent-footnote spacing pass
- `research/people/g13-john-gurney-fact-sheet.research.md` — Ryvett-parishes hypothesis added with negative-search result; action-item migrations from case file body

**Status:** DRAFT — awaiting application. Depends on v46 (already applied) and v48 (probability-table and §8 row baseline).

## Posture

This is the prose, table-order, and citation-tightening pass on the case file. No new evidence is introduced; the patchset reorganizes, re-anchors, and tightens what is already in place. Body prose continues to read as timeless statements of evidence — no "previously," "earlier indexing," "new finding," "case file update," or "see internal notes" pointers. All cross-references inside the case file remain section-anchored; pointers to companion files move into footnotes.

The §8.1 two-Aylesbury-Johns paragraph is removed entirely after the proof-by-eight-week-gap was reasoned out and found not to hold (premarital conception is permissible; the eight-week gap does not by itself rule Anne Cowheard out as the December 1638 baby's mother, so the "two Johns must exist" conclusion is not forced). The case file's argument does not require sorting out whether the Cowheard groom is Candidate A in a remarriage or a separate adult John; either reading still eliminates the Cowheard event as the colonial emigrant, and that elimination is carried by the §8 table row's "single-event, no continuation" reasoning alone.

The §10.1 Against row 1 is reframed on the **age mismatch** between the 1653 Wilson v. Faxon deposition (which fixes the colonial John's birth at c.1602/3) and Entry E's c.1609/10 date — the case file's reading of Entry E baptizes a baby roughly seven years too young to be the colonial John under a normal reading of "about 50." This is the actual hard tension in the Candidate B identification; paleographic confirmation is a secondary issue that survives under the new framing.

---

## 1. §1 facts table — source-attribution tightening

The §1 table currently routes "Braintree vital record …" through generic phrasing. The repo already has `braintree-records-1640-1793-1886` (Bates 1886) as a structured source with explicit page references in case-file n81. Tighten the §1 right-column attributions to name the actual primary publication and page.

**1a — Wife row (Mary Gurney death 20 Sept 1661):**

Old:
```
| **Wife** | Mary (maiden name unknown), d. 20 Sept 1661 | Braintree vital record death entry; Sprague<sup class="fn"><a href="#n6" id="ref-6">6</a> </sup> |
```

New:
```
| **Wife** | Mary (maiden name unknown), d. 20 Sept 1661 | Bates, *Records of the Town of Braintree* (1886), p. 638; Sprague p. 695<sup class="fn"><a href="#n6" id="ref-6">6</a></sup> |
```

**1b — Second wife row (Grizzell):**

Old:
```
| **Second wife** | Grizzell Fletcher/Kidbee, traditionally m. 12 Nov 1661; Braintree printed-record surname conflict | Braintree vital records, marriage entry + multiple others<sup class="fn"><a href="#n7" id="ref-7">7</a></sup> |
```

New:
```
| **Second wife** | Grizzell Fletcher/Kidbee, traditionally m. 12 Nov 1661; Braintree printed-record surname conflict | Bates, *Records of the Town of Braintree* (1886), p. 717; Holman, "Grissell of the Many Marriages," *The American Genealogist* 10 (1933), pp. 70-73<sup class="fn"><a href="#n7" id="ref-7">7</a></sup> |
```

**1c — Children row:**

Old:
```
| **Children** <br />(born in England) | Sarah (b unknown), Mary (bc.1628), Richard (bc.1630), John Jr. (bc.1633), Peter (bc.1635-40) + potentially Isaac (uncertain) | Sprague; compiled sources<sup class="fn"><a href="#n8" id="ref-8">8</a></sup> |
```

New:
```
| **Children** <br />(born in England) | Sarah (b unknown), Mary (bc.1628), Richard (bc.1630), John Jr. (bc.1633), Peter (bc.1635-40) + potentially Isaac (uncertain) | Sprague, *Genealogies of the Families of Braintree* (2001), p. 695; *History of Weymouth, Massachusetts* (1923), vol. 3, p. 251<sup class="fn"><a href="#n8" id="ref-8">8</a></sup> |
```

(Existing footnotes n6, n7, n8 already cite Bates page numbers and the *History of Weymouth* reference; no footnote-text changes required, only right-column display strings.)

**1d — n6 footnote expansion** (the footnote currently reads generically; align to Bates page):

Old:
```html
<li id="n6" value="6">Braintree, Massachusetts, town vital records, death entry for Mary Gurney, 20 Sept. 1661; Sprague, <em>Genealogies of the Families of Braintree</em>, p. 695, John Gurney entry, treating Mary's maiden name as unknown. Source ID: <code>sprague-braintree</code>. <a class="backref" href="#ref-6">↩</a></li>
```

New:
```html
<li id="n6" value="6">Braintree (Mass.), <em>Records of the Town of Braintree, 1640 to 1793</em>, ed. Samuel A. Bates (Randolph, Mass.: D. H. Huxford, printer, 1886), p. 638, death entry for Mary Gurney 7th month 20, 1661 (Old Style; 20 September 1661 New Style), <a href="https://archive.org/details/recordsoftownofb00brai">https://archive.org/details/recordsoftownofb00brai</a>; Sprague, <em>Genealogies of the Families of Braintree</em>, p. 695, John Gurney entry, treating Mary's maiden name as unknown. Source IDs: <code>braintree-records-1640-1793-1886</code>; <code>sprague-braintree</code>. <a class="backref" href="#ref-6">↩</a></li>
```

---

## 2. §1 and §2.1 — first-occurrence hyperlinks

**2a — §1 first paragraph, Robert Charles Anderson first occurrence.**

Old:
```
No known published authority including Robert Charles Anderson's *Great Migration Directory* (2025), which lists his origin as "Unknown", has identified his parents or home parish.
```

New:
```
No known published authority including <a href="https://www.americanancestors.org/robert-charles-anderson-fasg-0">Robert Charles Anderson</a>'s *Great Migration Directory* (2025), which lists his origin as "Unknown", has identified his parents or home parish.
```

**2b — §2.1 second paragraph, Daniel Gurney first occurrence.**

Old:
```
Genealogist Daniel Gurney noted that Francis's "commercial life began at Norwich."
```

New:
```
Genealogist <a href="https://en.wikipedia.org/wiki/Daniel_Gurney">Daniel Gurney</a> noted that Francis's "commercial life began at Norwich."
```

Subsequent occurrences of either name remain plain text — first-occurrence hyperlink only, per the fact-sheet style rule (no more than ten such hyperlinks per document).

---

## 3. §6.1 The Children Search Matrix — rework

Replace the entire §6.1 contents (from the `### 6.1` heading through the closing paragraph that ends "…the case file does not treat their absence from indexed collections as eliminating evidence for any specific origin hypothesis.") with:

```markdown
### 6.1 The Children Search Matrix

**No indexed English parish-register cluster matches the colonial John's full family signature.** A John Gurney + Mary household producing the colonial children — Sarah, Mary, Richard, John Jr, and Peter — in the right age window does not surface in any covered parish 1620-1640, despite over twenty Gurney baptisms reviewed across FamilySearch, Findmypast, and Ancestry indexed collections.

The marriage of John and Mary was in England before 1628. Mary Gurney, John's daughter, married Daniel Shed at Braintree in 1647; Daniel was baptized 25 June 1620 at Finchingfield, Essex, and the Braintree Book of Records preserves seven births to Daniel and Mary 1647-1658. Even at a minimum marriage age of 16, Mary Gurney was born by 1631; standard derivative tradition places her at c.1628.<sup class="fn"><a href="#n97" id="ref-97a">97</a></sup> No John Gurney + Mary marriage 1620-1635 surfaces in eastern-England parish-marriage indexes outside the eliminated Eythorne, Kent / Mary Marsh event. The absence is best read as a parish-register coverage gap rather than evidence against an English marriage.

The closest indexed clusters are weak matches on dates, mother's name, or both:

| Parish | County | Indexed Gurney baptisms | Father | Mother | Assessment |
|---|---|---|---|---|---|
| **Berkhamsted** | Herts | Henry 1610, Sara 1615, John 1624, Richard 1626, Elizabeth 1629, Michael 1631, Sarah 1634, Francis 1636 | John | Unknown | (2/5 names; wrong dates; eight-child family, see §8.2) — **Low probability; Candidate C eliminated** |
| **Aylesbury** | Bucks | John 1638, Sarah 1639, Daniell 1645, Jonathan 1647, Hannah 1653 | John | Alice Oliffe (per 1628 Bierton marriage) | (1/5 names; wrong dates; Candidate A continuing residence to 1650 Walgrave Northants) — **Low probability; Candidate A eliminated** |
| **Hitcham** | Bucks | Mary 1631 | John | Unknown | (1/5 names; wrong date; single indexed event) — **Low probability; see §8 table** |
| **Eythorne** | Kent | John 1638, Edward 1641 | John | Mary Marsh | (2/5 names; wrong dates; wife Mary; John buried Eythorne 1648) — **Low probability; eliminated** |
| **Toddington** | Beds | Elizabeth 1625, Anne 1628, John 1630, Audrey 1633 | John | Elizabeth Moreton | (1/5 names; wrong dates; John buried Toddington 1641) — **Low probability; eliminated** |
| **Ackworth** | Yorks | John Thomas 1637 | John Gurnoe | Mary Burton (per 1636 Ackworth marriage) | (1/5 names but wife is Mary in window; first child is John Thomas not Sarah; no Yorkshire continuation indexed) — **Low probability; see §8 table** |

The Berkhamsted, Aylesbury, and Eythorne clusters are eliminated as the colonial emigrant on continuing-English-residence grounds (see §8). The Hitcham and Ackworth clusters are held at Unlikely on single-event-with-no-continuation reasoning (see §8). The colonial John's first three children (Sarah, Mary, Richard) most plausibly sit in an unindexed eastern-England parish marriage and baptism record set; the case file does not treat their absence from indexed collections as eliminating evidence for any specific origin hypothesis.<sup class="fn"><a href="#n97" id="ref-97c">97</a></sup>
```

---

## 4. §7 — already addressed in v46

(Topic-sentence opener added in v46; no change in v49.)

---

## 5. §8.1 / §8.2 / §8.3 — topic sentences and the two-Aylesbury-Johns paragraph

### 5a. §8.1 — add topic sentence; remove "two Aylesbury Johns" paragraph

Insert as the new first sentence of §8.1, immediately after the heading `### 8.1 Candidate A — Aylesbury hundred Buckinghamshire and Walgrave Northamptonshire`:

```markdown
Candidate A is one John Gurney whose family appears in continuous indexed records in the Aylesbury hundred of Buckinghamshire and at Walgrave, Northamptonshire 1628-1653, eliminating him as the colonial emigrant on continuing-English-residence grounds.
```

**Delete the closing paragraph of §8.1** (the paragraph beginning "**The two Aylesbury Johns of 1638.**" — whatever wording is currently in place from v46 or earlier). The Cowheard marriage event is covered by its own §8 table row (Unlikely ~3% on single-event-no-continuation grounds), and the case file's argument does not require resolving whether the Cowheard groom is Candidate A in a post-Alice remarriage or a separate adult John.

### 5b. §8.2 — add topic sentence

Insert as the new first sentence of §8.2, immediately after the heading `### 8.2 Candidate C — Berkhamsted, Hertfordshire`:

```markdown
Candidate C is a Berkhamsted John Gurney whose eight-child family runs 1610-1636 — the chronology, child set, and absence of a Mary and a Peter all mismatch the colonial John, eliminating him.
```

### 5c. §8.3 — add topic sentence and inclusion-logic note

Insert as the new first sentence of §8.3, immediately after the heading `### 8.3 Buckinghamshire same-county cluster`:

```markdown
Buckinghamshire contains a dense cluster of other John Gurney households in the 17th century, each documented by a different parish, wife, and child set. The principal heads-of-household consistent with the emigrant age window appear as separate rows in the §8 table; the additional households below — generational predecessors (pre-1620 fathering), post-1660 baptisms, and single-name index events without household profile — are summarized here so the case file accounts for the full surfaced record set without inflating the table.
```

### 5d. §8.3 — add Amersham row to the §8 table

The current §8.3 narrative includes "Amersham, Bucks (John + Avis Garter): marriage 7 February 1638. Wife Avis Garter, not Mary; a separately documented Bucks John Gurney from Candidate A's 1628 Bierton marriage and from the 1638 Aylesbury Cowheard groom."

Promote to a §8 table row. Insert after the Aylesbury Cowheard row:

```
| Amersham, Bucks (John + Avis Garter) | Buckinghamshire | **Avis** Garter | **Unlikely (~3%)** | Marriage 7 February 1638 Amersham; single indexed event; no continuation of this couple's household and no emigration evidence.<sup class="fn"><a href="#n94" id="ref-94p">94</a></sup> |
```

(n94 already cites the Amersham marriage; back-ref preserved.)

Then **strike the Amersham bullet from the §8.3 narrative list** (since it is now in the table).

### 5e. §8.3 narrative — strip action-item phrases

In the Hitcham bullet, replace:
```
A Hitcham parish register pull would resolve whether further Gurney baptisms exist there.
```

with:
```
The household appears once in indexed records.
```

(The pull-target itself migrates to the G13 companion's "Target Source Pulls" list — see §11 of this patchset.)

Similarly scan §8.1, §8.2, §8.3 for any "...would resolve..." / "...pull is open..." / "...not yet pulled..." body-prose phrases and strip them. Underlying pull-targets continue to live in the G13 companion's Target Source Pulls list.

---

## 6. §8.4 + §8.5 — internal-pointer footnote consolidation

### 6a. §8.4 — strike body pointer; fold into n92

The §8.4 closing paragraph currently reads (post-v48 rewrite):
```
Depth is in `research/people/john-gurney-candidate-d.md` (full Drapers' corpus, Hunscott identity bridge, family reconstruction, gaps). Cross-link summary at `research/people/g13-john-gurney-fact-sheet.research.md`.
```

**Delete this paragraph from the §8.4 body.** Append the same content into n92 as a closing sentence (n92 already cites both companion files; the additional sentence consolidates the cross-link).

Add to n92 (after its existing "Research companion cross-link: `research/people/g13-john-gurney-fact-sheet.research.md`." closer):
```
Depth-of-detail file: <code>research/people/john-gurney-candidate-d.md</code> (full Drapers' corpus, Hunscott identity bridge, family reconstruction, and resolution path).
```

### 6b. §8.5 — strike body pointer; fold into n99

The §8.5 closing line currently reads:
```
Full deconflation in the companion at `research/people/g13-john-gurney-fact-sheet.research.md`.
```

**Delete this line from the §8.5 body.** Append into n99 (already cites the Newgate apprentice tradition):
```
Full deconflation of the Newgate-apprentice tradition from the colonial John of Braintree: <code>research/people/g13-john-gurney-fact-sheet.research.md</code>.
```

---

## 7. §10 — delete orphan companion-pointer paragraph

Locate the paragraph beginning:
```
For colonial-side context — Braintree burial location, the Cheney/Gurney 1661 vital-record question, the Torrey and *History of Weymouth* family-group cross-checks, the Weymouth/Braintree/Mendon land record, the Lysander Franklin Gurney manuscript pointer, and the American Gurney arms family-memory lead — see the companion file at `research/people/g13-john-gurney-fact-sheet.research.md`.
```

(Currently at the end of §10.1 in the v46-restructured layout, immediately before §10.2.)

**Delete the paragraph in full.** The companion file already houses the material; readers who want it can navigate from the case file's existing § references. The pointer adds friction without supplying the information it advertises.

---

## 8. §10.1 (Evidence Summary) — reorder For- and Against-tables strongest-to-weakest

### 8a. For Candidate B table — replace the row sequence

Replace the existing For-Candidate-B table body with the following ordered rows (strongest to weakest). Row numbers are reset and the cell content preserved verbatim from the current case file except where flagged.

```markdown
| # | Evidence | Weight | Explanation |
|---|----------|--------|--------|
| 1 | ★ Margaret Rybett marriage confirmed | Strong | Francis had a first wife — children from this 1611 marriage are exactly the right generation for the emigrant. |
| 2 | ★ John Gurney baptism record (Francis Gurney) | Moderate-strong | Primary source record of a John born to Francis Gurney in the target community. |
| 3 | Occupation: Merchant Taylor father → tailor son | Strong | Trades passed through family apprenticeship. Of the named candidates only Candidate D shares a textile-trade link, and D's continuing London residence to 1662 rules him out as the colonial John (see §8.4). |
| 4 | Geography: Norfolk/London = emigrant corridor | Strong | Francis lived in the region that produced the Great Migration — the same counties that sent the most settlers to Massachusetts. |
| 5 | 1634 forced sale of all lands | Strong | Francis sold everything through the Court of Wards. A son John would have had no inheritance to stay for. |
| 6 | Puritan uncle Edmund | Strong | Francis's brother was a militant Puritan clergyman — direct family exposure to the religious movement driving emigration. |
| 7 | Essex social network | Strong (cumulative) | John's colonial world (son-in-law Shed from Essex, landlord Ting/Tyng of Essex-connected property, Braintree MA named for Braintree Essex) maps to Francis's second wife's family connections. Suffolk Deeds adds a specific Braintree leasehold context for John in the Ting/Tyng estate. |
| 8 | Coleman Street emigrant hub | Strong (context) | Francis's parish adjoined London's most active Puritan emigration center — Davenport, Eaton, and the Hector voyage originated yards from St Benet Fink. |
| 9 | Francis named a second son John in the Anne Browning marriage (Maldon bachelor, d. 1681) | Moderate | Bernau documents a second John Gurney son of Francis G14, paying 1674 hearth tax on nine hearths at St Mary's Maldon and dying a bachelor 1681. Demonstrates that Francis used the name John for a son in his second marriage; rebuts the inverse of the "no son named Francis" naming-pattern concern.<sup class="fn"><a href="#n108" id="ref-108">108</a></sup> |
| 10 | Ann Gurney / Gilman connection at Hingham | Moderate | A probable sister to John married into a Norfolk textile family at Hingham — ancient Gurney family territory. Her son emigrated to New England. |
| 11 | Daniel Gurney hedged on "eldest" | Moderate | Daniel was uncertain whether Roger was truly Francis' firstborn — room for an older, unknown son from the first marriage. |
| 12 | Pease genealogy claim confirmed | Moderate | The Margaret Ryvett claim, long unverified family tradition, has now been validated by primary source evidence from NRO PD 12/1. Lends credence to other details in the genealogy that align with this case file. |
| 13 | William Gurney at Coleman Street | Moderate-suggestive | A Gurney living in the radical Puritan parish next to Francis's own — identity unknown but notable proximity. |
| 14 | Rivett cluster near East Dereham | Moderate | Margaret's Ryvett family had a documented presence near East Dereham — Richard Ryvett of Gressenhall could be the source of John's son Richard's name. |
| 15 | Banks placed John in East Anglia | Weak positive | Genealogist Banks pointed to Bury St. Edmunds — possibly the wrong specific person, but the right geographic corridor. |
| 16 | Child lists not exhaustive | Removes a negative | Daniel Gurney's *Record* (1848) and Bernau's *British Archivist* (1913) both note that the St Benet Fink / Anne Browning child list is fragmentary. Removes the argument-from-silence against an unrecorded first-marriage son.<sup class="fn"><a href="#n30" id="ref-30b">30</a></sup> |
| 17 | City of London Returns don't survive | Removes a negative | Francis's absence from Protestation Returns is explained by non-survival of City returns, not by his absence. |
| 18 | American Gurney arms | Weak | A 1926 American biographical entry reports that arms kept by American Gurneys connected them with the Norfolk Gurneys. Supports Candidate B only if an early American object or manuscript witness can be found. |
```

### 8b. Against Candidate B table — replace the row sequence

Replace the existing Against-Candidate-B table body with the following ordered rows (strongest to weakest). Row 1 is reframed onto the age-mismatch issue; the paleographic-confirmation concern survives as a secondary clause inside the same row.

```markdown
| # | Evidence | Weight | Explanation |
|---|----------|--------|--------|
| 1 | Entry E's c.1609/10 date predates the 1653 deposition's "aged about 50" by 6-8 years | Moderate-strong negative | Wilson v. Faxon (1653) places the colonial John's birth at c.1602/3 (deponent "aged about 50 years"). Entry E reads as a c.1609/10 baptism. If both are correct as written, the East Dereham baby is roughly seven years too young to be the colonial John — surviving the "about 50" testimony only under a wide age-rounding reading or a deponent age error. Paleographic confirmation of the Entry E reading would tighten but not close this gap. |
| 2 | No child of John named Francis | Moderate negative | The strongest naming-pattern argument against the hypothesis. |
| 3 | No record in England of John's marriage to Mary | Moderate negative | A marriage record would significantly strengthen probability. |
| 4 | Roger called "eldest sonne" in 1633 Visitation | Moderate negative | Visitation recorded only children Francis presented — but the record stands as written. |
| 5 | Common-name density and parish-coverage gaps | Moderate negative (cumulative) | Over forty distinct John Gurney heads-of-household across England 1600-1670; parish-register coverage gaps imply additional unidentified Johns. Even after elimination of the named candidates, the residual unknown-corridor candidate space is materially non-zero. Reflected in §11 residuals (Unknown corridor ~20%; Unknown other corridor ~10%). |
| 6 | Burke numbers sons Roger, Francis, Thomas — no John | Moderate negative | Burke relied on the visitation and Daniel Gurney — same limitation applies. |
| 7 | Lack of known baptism records for John's English-born children | Moderate-suggestive | Records may exist but have not been located. |
| 8 | Peter anomaly qualified | Neutral-to-weak negative | Indexed Peter-Gurney-variant baptisms 1632-1642 do not include a John-Gurney child. Peter remains distinctive for John-1 but not absolutely absent from Norfolk Gurney households (1641 Smallburgh Peter Gurney + father Peter). |
```

---

## 9. Global adjacent-footnote spacing pass

Apply a global substitution across the case file body and citation index to insert a space between adjacent footnote markers:

Find: `</sup><sup class="fn">`
Replace: `</sup> <sup class="fn">`

(Apply with `replace_all`. The footnote citation index `<a class="backref" href="#ref-XX">back</a> <a class="backref" href="#ref-YY">back</a>` style is already space-separated in most places; the same global replace will not affect those because the source pattern is different.)

---

## 10. Case-file action-item phrase strip

Scan the case file for any remaining body-prose phrases of the following kinds and either delete or reword to a fact-statement-only form:

- "would resolve whether…"
- "is the single most important next step…"
- "manuscript image not yet pulled"
- "pending direct image pulls"
- "pending direct script verification of the register page"
- "the Bury parish-register manuscript image is not yet pulled"
- "professional confirmation needed"
- "if possible given readability of entry"
- "is presently held in the project's foundation research notes at"
- "Source IDs pending direct image pulls"
- "(filename retains earlier target wording; line resolves to Marye, not Margaret)" — image-naming workflow noise inside n102

Recommended treatment per type:

- "would resolve…" phrases → delete; the underlying pull-target lives in the G13 companion's "Target Source Pulls" list.
- "single most important next step" (§5.2) → keep §5.2 but tighten to: "Professional paleographic examination of the original register at the Norfolk Record Office, The Archive Centre, Martineau Lane, Norwich NR1 2DQ, is the canonical path for confirming Entry E."
- "manuscript image not yet pulled" / "Source IDs pending direct image pulls" inside footnotes → delete the phrase; the existence of an unindexed register image is a research-notes concern, not a citation-text concern.
- Image-naming workflow notes inside footnotes (e.g., filename-retention parentheticals in n102) → delete.

This is a sweep, not a single edit; apply on a footnote-by-footnote and paragraph-by-paragraph basis.

---

## 11. G13 research companion additions

### 11a. Ryvett-parishes hypothesis with negative-search result

Add a new subsection in `research/people/g13-john-gurney-fact-sheet.research.md` under "Working Notes" (placement consistent with the existing topic-organized layout):

```markdown
### Ryvett-centric parishes — John living with maternal kin after Margaret's death

**Hypothesis.** Margaret Rybett, John's mother, died c.1616-1617. A son aged six to eight whose father was already engaged in commercial work between London and Norfolk might have been placed with maternal kin — particularly given the Ryvett/Rivett family's documented presence in parishes near East Dereham (Gressenhall, Garveston) and across Suffolk (Fritton, Rishangles, Rattlesden, Stowmarket, Bildeston). If so, indexed Gurney baptisms or burials in those Ryvett-centric parishes might surface in the 1610-1635 window.

**Negative search result.** A FamilySearch indexed-records pass for Gurney surname in Gressenhall and Garveston (Norfolk Ryvett-proximate parishes) returns no early-17th-century Gurney baptisms; the only Gressenhall Gurney records are 1881 census entries. A FamilySearch and Findmypast Buckinghamshire-style search for Suffolk Gurney baptisms 1600-1640 across the named Ryvett parishes returns no clean cluster — the surviving Rattlesden Gurney family is a post-1700 lineage unrelated to Margaret Rybett's family. The hypothesis is consistent with parish-coverage gaps but is not supported by surfaced indexed records. Held as speculation; not added to the case-file body.

The §2.2 mention "Richard Ryvett of Gressenhall could be the source of John's son Richard's name" stands on its own as a naming-source hypothesis, not as evidence that John lived with the Ryvetts.
```

### 11b. Migrate action-item phrases from case-file body into the Target Source Pulls list

Append to the existing "Target Source Pulls / Not Yet Searched" section (relocated from case-file §12 in v46):

```markdown
### Migrated from case-file body (v49)

These pull-targets were stripped from the case-file body prose as action-item phrases inconsistent with the case file's timeless-evidence posture. They remain valid research targets.

- **Hitcham, Buckinghamshire parish register, 1620-1665** (south Bucks). Pull the Centre for Buckinghamshire Studies register for Hitcham to test whether further Gurney baptisms, marriages, or burials surface alongside the lone indexed Mary Gurny baptism 22 January 1631 (father John Gurny, mother unindexed). Either further records confirm a continuing-residence household (move to ELIMINATED) or absence leaves the row at Unlikely.
- **Ackworth, Yorkshire parish register, 1635-1665**. Pull the West Yorkshire Archive Service register for Ackworth to test for further John Gurnoe / Mary Burton household activity after the son John Thomas Gurnoe baptism 19 January 1637. Either a continuing Yorkshire household confirms ELIMINATED, or absence leaves Ackworth at Unlikely with the closest non-Candidate-B wife-name match still on the table.
- **East Dereham parish register, Norfolk Record Office PD 86/41**. Professional paleographic examination of Entry E remains the canonical path for confirming the "John son of ffrancis Gurnie" reading, but does not resolve the more material chronological tension between Entry E's c.1609/10 date and the 1653 deposition's c.1602/3 birth implication (see §10.1 Against row 1).
- **Bury St Mary parish register (FL 541/4), Suffolk Record Office Bury branch**. Pull the underlying register pages for the three 1653-1656 Bury Gurney burials (John 11 December 1653; Gurney 6 April 1655; widow 13 May 1656) cited under n93. The §10.6 reading that the household stayed at Bury rests on the indexed National Burial Index entries; a register-image pull confirms the household structure (forenames, ages, family relationships) one level deeper.
- **St Benet Fink baptism register (LMA P69/BEN1/A/001 and /002), 1619-1638**. Pull to reconcile the children list across Daniel Gurney 1848, Bernau 1913, and the current G14 fact sheet. Open as a follow-up patchset once the LMA pull is in hand. Do not modify the G14 fact sheet without it.
```

---

## 12. Pre-apply integrity checks

- `grep -n "John-gurney-research-to-be-assessed" research/case-files/john-gurney-case-file-v4.md` should return zero hits.
- `grep -n "two Aylesbury Johns" research/case-files/john-gurney-case-file-v4.md` should return zero hits.
- `grep -n "For colonial-side context" research/case-files/john-gurney-case-file-v4.md` should return zero hits.
- `grep -n "Depth is in research/people\|Full deconflation in the companion" research/case-files/john-gurney-case-file-v4.md` should return zero hits (both pointers moved to footnotes).
- `grep -cE "</sup><sup class=\"fn\">" research/case-files/john-gurney-case-file-v4.md` should be zero after the global spacing pass.
- `grep -nE "<a href=\"https://en.wikipedia.org/wiki/Daniel_Gurney\">" research/case-files/john-gurney-case-file-v4.md` should return exactly one match (first-occurrence link).
- `grep -nE "<a href=\"https://www.americanancestors.org/robert-charles-anderson-fasg-0\">" research/case-files/john-gurney-case-file-v4.md` should return exactly one match.
- §6.1 table row count should be 6 (Berkhamsted, Aylesbury, Hitcham, Eythorne, Toddington, Ackworth).
- §8 table should include the Amersham John + Avis Garter row.
- §10.1 For-table row count should be 18 (after v46 deleted the Find a Grave row and added the Maldon-bachelor row).
- §10.1 Against-table row count should be 8.

## Reviewer checklist

- [ ] §1 facts table: three right-column source attributions tightened to name Bates 1886 pages and *History of Weymouth* citation directly; n6 expanded
- [ ] Robert Charles Anderson first occurrence (§1) gains AmericanAncestors hyperlink
- [ ] Daniel Gurney first occurrence (§2.1) gains Wikipedia hyperlink
- [ ] §6.1 rewritten: topic-sentence-up-front; Mary Shed bound explanation; six-row table covering all surfaced near-miss candidates including Ackworth
- [ ] §8.1 gains topic-sentence opener
- [ ] §8.1 closing "two Aylesbury Johns" paragraph removed in full
- [ ] §8.2 gains topic-sentence opener
- [ ] §8.3 gains topic-sentence opener with inclusion-logic note
- [ ] §8.3 Hitcham-pull action-item phrase stripped; Amersham bullet moved out of §8.3 narrative
- [ ] §8 table gains Amersham John + Avis Garter row
- [ ] §8.4 closing "Depth is in research/people/john-gurney-candidate-d.md..." paragraph deleted from body; equivalent content appended to n92
- [ ] §8.5 closing "Full deconflation in the companion at..." line deleted from body; equivalent content appended to n99
- [ ] §10.1 orphan "For colonial-side context..." paragraph deleted
- [ ] §10.1 For-table reordered strongest-to-weakest (18 rows in the new order specified)
- [ ] §10.1 Against-table reordered strongest-to-weakest (8 rows in the new order specified); row 1 reframed onto the 1602/3 vs c.1609/10 age mismatch
- [ ] Global adjacent-footnote spacing applied (no `</sup><sup` substring remains)
- [ ] Action-item phrases stripped across §5.2, §8.3, footnote bodies; corresponding pull-targets appear in the G13 companion's Target Source Pulls list
- [ ] G13 companion gains Ryvett-parishes-hypothesis subsection with negative-search result
- [ ] G13 companion gains "Migrated from case-file body (v49)" subsection capturing Hitcham / Ackworth / East Dereham / Bury / St Benet Fink pull-targets
- [ ] Integrity checks pass

## Notes for follow-up

- v50+: Bernau children-list reconciliation against the G14 fact sheet requires a direct LMA P69/BEN1/A baptism-register pull. Open as a separate focused patchset once that pull lands.
- v50+: Full §5.2 / §10.1 row 1 paleographic-vs-chronological framing can be tightened further if the East Dereham professional paleographic examination yields the "ffrancis Gurnie" reading conclusively — at which point the age mismatch becomes the sole remaining tension on Entry E and the For-table row 2 ("baptism record") can be promoted from Moderate-strong to Strong.
