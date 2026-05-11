# Intake patchset v26 - Cand A Stewkley 1603 baptism FS-indexed; Medmenham Bucks lead

```yaml
patchset_id: v26
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after v20-v25.
```

## 0. Audit report

### 0.1 Scope

Pass 8 (2026-05-09) used FamilySearch Family Tree Search to find the FS Tree profile for the colonial John Gurney (LT9Z-KQ1) and walked its 8 attached sources. Two case-file-relevant outcomes:

1. **The Stewkley 1602/3 baptism on which Cand A is built is now FS-indexed** (FS ID `JMRS-DX6`): Jhon Gurney, son of Jhon Gurney, christened 21 February 1603 at Stewkley, Buckinghamshire. This upgrades the Cand A citation from "per Sprague, not image-verified" (v22/v23 wording) to a primary indexed record.
2. **A Medmenham, Buckinghamshire parish register source** is attached to LT9Z-KQ1 with the user note "Richard gurney marriage." The FS image is restricted, but the source title indicates the published Wethered (1898) parish register, retrievable on Internet Archive in a later pass.

### 0.2 FS Tree profile LT9Z-KQ1 internal inconsistency

LT9Z-KQ1 states birthplace Bury Saint Edmunds, Suffolk (Banks Mss attribution) but the only baptism source attached is the Stewkley, Bucks 1603 entry (Sprague attribution). The Tree profile conflates the two candidate identification theories the case file has been working to disentangle. No change is needed in v26 to address the Tree profile itself — the conflation is consistent with the case file's ongoing Cand A vs Cand B vs "Unknown other origin" framing.

### 0.3 Other 6 sources on LT9Z-KQ1

The remaining 6 sources are mostly already case-file-cited: The Puritan Great Migration Project (worth future inspection for the Bury St Edmunds basis), Pope's *The Pioneers of Massachusetts*, *History of Weymouth* vol. 3, MA Town and Vital Records, the Find a Grave Index, and Banks's *Topographical Dictionary*. Pass-8 work does not re-pull these; they remain in scope for future patchsets only if they yield new content.

### 0.4 Candidate implications

- **Cand A:** The FS-indexed Stewkley 1603 baptism (FS ID `JMRS-DX6`) firms the Cand A birth identification. Combined with the v22 Bierton 1628 marriage and the v23 Aylesbury 1639-1653 family group, Cand A's English-residence chain is now end-to-end FS- and FMP-indexed except for his burial. Probability table is unchanged: Cand A remains effectively eliminated (~1-2%).
- **Cand B:** No direct effect from Pass 8.
- **Cand C, Ackworth:** No direct effect from Pass 8.
- **Unknown other origin:** Unchanged.

## 1. Source registry operation

**No new source ID is added in v26.** The Stewkley 1603 baptism is a primary indexed record in FS England Births and Christenings (FS ID `JMRS-DX6`); use the existing source ID `fs-england-births-christenings` already added in v23. The FS Family Tree profile `LT9Z-KQ1` is not itself a citable source — it is a user-contributed tree that points to primary records (one of which is the Stewkley 1603 entry). The tree profile is recorded in the G13 research companion as a research-context note, not in `data/sources.json`.

## 2. Validation note

No new validation file is required in v26. The existing `sources/validations/fs-england-births-christenings.md` (proposed in v23) covers the Stewkley 1603 baptism via FS ID `JMRS-DX6`. Update its "Key entries used" list to add the Stewkley baptism alongside the Aylesbury family group.

## 3. Proposed case-file edits

### 3.1 §1 baseline-facts table — no change required

The Cand A baptism is not in the baseline facts table; it appears in the §8 elimination row.

### 3.2 §8 Cand A row — upgrade Stewkley citation

Old (after v22/v23 applied):

```markdown
| **Candidate A** | Stewkley (1602/3 bapt., per Sprague, not image-verified); married Bierton with Broughton, Bucks (1628); Aylesbury family group 1639-1653; Aylesbury hundred → Northamptonshire (1641-1650) | **Alice Oliffe** ... |
```

New:

```markdown
| **Candidate A** | Stewkley, Bucks (Jhon Gurney son of Jhon Gurney bapt. 21 Feb 1603, FS England Births and Christenings 1538-1975, FS ID `JMRS-DX6`); married Bierton with Broughton, Bucks (1628); Aylesbury family group 1639-1653; Aylesbury hundred → Northamptonshire (1641-1650) | **Alice Oliffe** ... |
```

Add to the existing Cand A endnote (or append a new sentence to the v23-proposed `nZA` endnote):

```html
... Stewkley 1603 baptism FS-indexed: FamilySearch, "England, Births and Christenings, 1538-1975," Jhon Gurney son of Jhon Gurney christened 21 February 1603 Stewkley, Buckinghamshire, England, FS ID `JMRS-DX6`, <a href="https://www.familysearch.org/ark:/61903/1:1:JMRS-DX6">https://www.familysearch.org/ark:/61903/1:1:JMRS-DX6</a>. Source ID: <code>fs-england-births-christenings</code>. ...
```

### 3.3 §13 What's Still Needed — replace the Stewkley Dickson/Putnam pull priority

Old (after v21/v22):

```markdown
- **Stewkley parish register (Dickson/Putnam 1897 print)** — covers baptisms 1545-1653, marriages 1599-1646, burials 1599-1653. Paywalled at Geneanet Premium and Genealogy Store. Highest single discriminating pull for closing or strengthening Candidate A.
```

New:

```markdown
- **Stewkley parish register (Dickson/Putnam 1897 print)** — Cand A's 1603 baptism is now FS-indexed (FS ID `JMRS-DX6`), so the Stewkley register pull is no longer the discriminating instrument for closing Cand A. The 1897 print remains useful for: (a) confirming the indexed entry against the original page image; (b) finding Cand A's siblings and parents context; (c) locating any later Cand A appearance (e.g., a Stewkley burial) that would complete the English-residence chain. Demote from Tier 1B to Tier 2.
```

### 3.4 §13 Other Leads — add Medmenham parked lead

```markdown
- **Medmenham, Buckinghamshire parish register, "Richard gurney marriage" entry.** Attached to the colonial John's FS Tree profile (LT9Z-KQ1) by user Mary8225 in December 2023 with note "Richard gurney marriage." The FS image is restricted, but the source title points to *The Parsons and Parish Registers of Medmenham, Buckinghamshire* (F. T. Wethered, 1898), retrievable on Internet Archive. Medmenham is in SE Bucks, ~30 miles from Stewkley but same county as Cand A's documented activity at Stewkley, Bierton, Aylesbury, and East Claydon. The Richard could be a son of Cand A or an unrelated Bucks Richard; the published Wethered transcription will resolve it without the FS image restriction.
```

## 4. Proposed G13 research-file edits

### 4.1 New section under "Origin Analysis and Elimination Work"

```markdown
### FS Tree profile LT9Z-KQ1 (colonial John Gurney) — 2026-05-09 walk

FamilySearch Family Tree profile LT9Z-KQ1 represents the colonial John Gurney: b. 21 Feb 1603, d. 16 Mar 1663 at Braintree, Massachusetts. 8 sources attached as of 2026-05-09. The profile is internally inconsistent on the birthplace: it states Bury Saint Edmunds, Suffolk (matching Banks Mss) but the only attached baptism source is the Stewkley, Bucks 1603 record (matching Sprague). This conflation is the same disentanglement work this case file has been doing through v20-v25.

Two LT9Z-KQ1 attachments are case-file-actionable:

- **Jhon Gurney baptism 21 February 1603 Stewkley, Buckinghamshire.** FS ID `JMRS-DX6`, England Births and Christenings 1538-1975, son of Jhon Gurney. This is Cand A's baptism, now FS-indexed primary rather than Sprague-derivative. Upgrade the Cand A citation accordingly.
- **The Parsons and Parish Registers of Medmenham, Buckinghamshire** (Wethered, 1898 — restored Internet Archive citation). User note "Richard gurney marriage." FS image restricted; the published Wethered transcription is retrievable on Internet Archive in a later pass.

The remaining 6 sources (Puritan Great Migration Project; Pioneers of Massachusetts; History of Weymouth; MA Town and Vital Records; Find a Grave Index; Banks Topographical Dictionary) are mostly already cited in the case file; only the Puritan Great Migration Project entry (attached January 2024 by Monica Pendleton) warrants future inspection to identify the published basis for the Bury St Edmunds birthplace claim on LT9Z-KQ1.[^fs-tree-lt9z-kq1-2026-05-09]

[^fs-tree-lt9z-kq1-2026-05-09]: FamilySearch Family Tree person LT9Z-KQ1 (Source ID `fs-tree-lt9z-kq1-colonial-john`); Jhon Gurney baptism Stewkley 1603 (Source ID `fs-england-births-christenings`, FS ID `JMRS-DX6`); pulls executed 2026-05-09.
```

## 5. Apply order

When approved (after v20-v25):

1. Update `sources/validations/fs-england-births-christenings.md` (proposed in v23) to add Stewkley 1603 to the "Key entries used" list.
2. Edit `research/case-files/john-gurney-case-file-v4.md` per §3 — note that the §8 Cand A row text proposed here is superseded by v27's §8 consolidation patchset; the §13 demotion and the §13 Medmenham parked-lead bullet stand.
3. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4.
4. Update `sources/intake/working/john-gurney-audit-state.md` to mark v26 as applied.
