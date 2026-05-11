# Intake patchset v24 - John Gurney Candidate C effectively eliminated; Ackworth Yorkshire qualified

```yaml
patchset_id: v24
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after v20, v21, v22, v23. v24 is the final non-paywall candidate-elimination patch in the current series.
```

## 0. Audit report

### 0.1 Scope

Pass 6 closes Candidate C (Berkhamsted, Herts) and Ackworth, Yorkshire (John + Mary Barton) — the two remaining non-Cand-A / non-Cand-B candidates still listed as "Open" or "Very unlikely" in §8 of the case file. Pass 6 also surfaces a small Cand A reconstruction detail from FS Records (a possible second Aylesbury marriage of Cand A to Anne Cowheard in 1638).

### 0.2 Cand C Berkhamsted family group (FMP Hertfordshire Baptism Index)

FMP Hertfordshire Baptism Index, surname Gurney (variants), father first name John (variants), place Berkhamsted, baptism year 1610-1650. **13 results, 8 unique children after spelling-variant dedup:**

| Year | Child | (variants) |
|---|---|---|
| 1610 | Henry | Gourney |
| 1615 | Sara | Gourney/Gurnie |
| 1624 | Jhon | Gourney |
| 1626 | Richard | Gourney (already in case file as Cand C child) |
| 1629 | Elizabeth | Gourney |
| 1631 | Michael | Gourney |
| 1634 | Sarah | Gourney/Gurnie (already in case file; second daughter named Sara, first having died) |
| 1636 | Francis | Gurney/Gourneye |

Mother field is unindexed in FMP Hertfordshire Baptism Index for this group; cannot directly identify Cand C's wife from this dataset.

### 0.3 Cand C — three-pronged elimination

1. **Age mismatch.** Cand C's John fathered Henry in 1610; the father was therefore born no later than ~1585-1590. The colonial John was born ~1603 per the 1653 deposition ("aged about 50 years," NEHGR 62:94 / Suffolk Court Files item 188). Cand C's John is too old by ~13-18 years to be the colonial John.
2. **Francis son 1636.** Cand C named a son Francis in 1636. The colonial John named no child Francis — the case file currently makes the absence-of-Francis argument the strongest naming-pattern argument against Cand B's "son of Francis G14" theory. Cand C is equally weakened by this naming pattern.
3. **No Mary, no Peter.** Cand C's children include no Mary and no Peter. The colonial John's two distinctive children (Mary, m. Daniel Shed; and Peter, the name foreign to every Gurney branch reviewed) are absent from the Berkhamsted family.

Even granting the alternative reading that 1610 Henry might be a separate older John Gurney's son (and a younger Cand C John fathered the 1624-1636 cluster only), the Francis 1636 + missing Mary/Peter arguments still hold.

**Cand C probability drops from ~3-5% (case file) to ~0-1% (effectively eliminated).**

### 0.4 Ackworth Yorkshire — qualified, not eliminated

FS Records search for John Gurney + spouse Barton (exact surname) in Yorkshire, England: **0 results.** Same search without place restriction: 15,970 noisy results, none precisely matching an Ackworth Yorkshire 1636 marriage in this dataset. FS Records search for John Gurney death in Ackworth Yorkshire 1640-1700: 2 results, both 18th-century Non-Conformist (Quaker) records (Henry Gurney marriage 1749, father John Gurney), not a 17th-century death.

The v2 case file's "Mary Barton/Burton (m. 1636)" claim was originally sourced by AI from primary records but the underlying citation chain is not preserved in the current repo. A negative result from FamilySearch Records alone is not adequate grounds for elimination, because Yorkshire Quaker monthly meeting records, FreeREG, Ancestry, FMP, and other regional indexes have patchwork coverage with different name-variant handling. The Ackworth row should be **qualified** (lead unconfirmed in this pass; underlying citation chain not preserved in repo; treat as "Unlikely" pending re-identification of the original source) rather than treated as eliminated.

### 0.5 Cand A reconstruction note (FS bonus)

FS Records: John Gurney + Anne Cowheard, married 25 Oct 1638, Saint Mary, Aylesbury, Buckinghamshire (FS ID `N2TD-Z9Z`, attached tree `M37F-R5D`). Either (a) a separately documented Aylesbury John, or (b) Cand A remarrying at Aylesbury after Alice Oliffe died (consistent with the 1639-1653 Aylesbury children documented in v23). Mother field is unindexed on the 1645 Daniell and 1647 Jonathan FS records, so the marriage-to-children link cannot be proven from FS Records alone.

### 0.6 Candidate implications after v24

Approximate post-v24 probability distribution:

| Candidate | Pre-v24 | Post-v24 |
|---|---|---|
| Cand B (Francis G14 + Margaret Rybett) | ~55-60% | ~55-60% |
| Cand A (Stewkley/Bierton/Aylesbury) | ~1-2% (v23) | ~1-2% |
| Cand C (Berkhamsted Herts) | ~3-5% | **~0-1%** |
| Ackworth Yorkshire | "Very unlikely" | **Unlikely; lead unconfirmed in this pass** |
| Unknown other origin | ~27-34% | ~37-44% (tightened, residual absorbed) |

## 1. Source registry operation

Add two source objects in `data/sources.json`:

```json
    "findmypast-hertfordshire-baptisms": {
      "shortTitle": "Findmypast Hertfordshire Baptisms",
      "fullTitle": "Hertfordshire Baptisms (parish-register baptism records, Hertfordshire Archives and Local Studies)",
      "publisher": "Findmypast / Hertfordshire Archives",
      "type": "parish register index (subscription)",
      "url": "https://search.findmypast.co.uk/search-world-records/hertfordshire-baptisms",
      "notes": "Used 2026-05-09 to assemble the Cand C Berkhamsted family group: Henry 1610, Sara 1615, Jhon 1624, Richard 1626, Elizabeth 1629, Michael 1631, Sarah 1634, Francis 1636 — all father John."
    },
    "findmypast-hertfordshire-burials": {
      "shortTitle": "Findmypast Hertfordshire Burials",
      "fullTitle": "Hertfordshire Burials (parish-register burial records, Hertfordshire Archives and Local Studies)",
      "publisher": "Findmypast / Hertfordshire Archives",
      "type": "parish register index (subscription)",
      "url": "https://search.findmypast.co.uk/search-world-records/hertfordshire-burials",
      "notes": "Used 2026-05-09 for John Gurney Hertfordshire burials walk. 48 results across the full 1538-present span; only two 17th-century Berkhamsted entries (Jhon Gourney 1612 and 1620), both predating Cand C's documented children. Zero John Gurney burials at Berkhamsted 1640-1700."
    }
```

## 2. Validation notes

Create thin `sources/validations/findmypast-hertfordshire-baptisms.md` and `sources/validations/findmypast-hertfordshire-burials.md` following the same shape as v22's `findmypast-bucks-*-index.md` files.

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 §8 elimination table — rewrite Cand C row

Old:

```markdown
| **Candidate C** | Berkhamsted, Herts | Unknown | **Open (~3–5%)** | Father of Richard (1626) and Sara (1634). No disqualifying evidence. |
```

New:

```markdown
| **Candidate C** | Berkhamsted, Herts | Unknown | **Effectively eliminated (~0-1%)** | FMP Hertfordshire Baptism Index documents a Berkhamsted family group of eight children to John Gurney father 1610-1636: Henry 1610, Sara 1615, Jhon 1624, Richard 1626, Elizabeth 1629, Michael 1631, Sarah 1634, Francis 1636. Three independent reasons for elimination: (a) the 1610 Henry baptism makes Cand C's John born ~1585-1590, ~13-18 years too old to be the colonial John (b. ~1603 per 1653 deposition); (b) Cand C named a son Francis 1636, whereas the colonial John named no child Francis (the case file's strongest naming-pattern argument against Cand B equally weakens Cand C); (c) Cand C's children include no Mary and no Peter, the colonial John's two distinctive children.<sup class="fn"><a href="#nZB" id="ref-ZB">ZB</a></sup> |
```

### 3.2 §8 elimination table — rewrite Ackworth row

Old:

```markdown
| Ackworth, Yorkshire | Yorkshire | **Mary** Barton | **Very unlikely** | Correct wife name but far outside emigrant corridor. |
```

New:

```markdown
| Ackworth, Yorkshire | Yorkshire | **Mary** Barton (claimed) | **Unlikely; lead unconfirmed in this pass** | The v2 case-file attribution "Mary Barton/Burton (m. 1636)" was originally sourced by AI from primary records but the citation chain is not preserved in the current repo. A FamilySearch Records search for John Gurney + spouse Barton in Yorkshire returned zero results in 2026-05-09, but FS Records is only one of several relevant indexes (Yorkshire Quaker monthly meetings, FreeREG, Ancestry, FMP) and negative coverage there does not eliminate the lead. Treat as "Unlikely" pending re-identification of the original source. The Yorkshire geographic outlier objection (far from the emigrant corridor) continues to hold independently.<sup class="fn"><a href="#nZB" id="ref-ZB">ZB</a></sup> |
```

Add new endnote covering both rows (number on application):

```html
<li id="nZB" value="ZB">Cand C: Findmypast Hertfordshire Baptisms search 2026-05-09, surname Gurney (variants), father John (variants), place Berkhamsted, baptism year 1610-1650, returning the eight-child Berkhamsted family group described above; source ID <code>findmypast-hertfordshire-baptisms</code>. Ackworth Yorkshire: FamilySearch Records search 2026-05-09 for John Gurney + spouse Barton in Yorkshire returning zero results; source ID <code>fs-england-births-christenings</code> (used as the broader Records collection probed). <a class="backref" href="#ref-ZB">↩</a></li>
```

### 3.3 §11 Probability Assessment table

Old:

```markdown
| **C — Berkhamsted, Herts** | ~3–5% | 2/5 children match. Lacks other data / records to support case |
```

New:

```markdown
| **C — Berkhamsted, Herts** | **~0-1%** | Eight-child Berkhamsted family group 1610-1636. Age mismatch (Cand C John b. ~1585-1590, colonial John b. ~1603), Francis son 1636 (colonial John has no Francis), no Mary and no Peter. |
```

Adjust "Unknown other origin" upward to absorb the freed probability.

## 4. Proposed G13 research-file edits

### 4.1 Insert "Candidate C Berkhamsted family group" section

Under "Origin Analysis and Elimination Work":

```markdown
### Candidate C Berkhamsted family group (FMP Hertfordshire Baptisms, 2026-05-09)

FMP Hertfordshire Baptism Index returns the following Cand C Berkhamsted family group to John Gurney father 1610-1636 (mother unindexed):

- Henry Gourney, 1610
- Sara Gourney, 1615 (first daughter Sara; presumably died young, replaced)
- Jhon Gourney, 1624
- Richard Gourney, 1626 (case-file standing)
- Elizabeth Gourney, 1629
- Michael Gourney, 1631
- Sarah Gourney, 1634 (case-file standing)
- Francis Gurney, 1636

Cand C is effectively eliminated for three reasons taken together: (a) the 1610 Henry baptism requires Cand C's John to be born ~1585-1590, ~13-18 years older than the colonial John (b. ~1603); (b) a Francis son 1636 (the colonial John named no child Francis); (c) no Mary, no Peter (the colonial John's distinctive children).[^findmypast-hertfordshire-2026-05-09]

[^findmypast-hertfordshire-2026-05-09]: Findmypast Hertfordshire Baptisms (source ID `findmypast-hertfordshire-baptisms`); Findmypast Hertfordshire Burials (source ID `findmypast-hertfordshire-burials`); FamilySearch Records for the Ackworth Yorkshire null search (source ID `fs-england-births-christenings`). Pulls executed 2026-05-09.
```

### 4.2 Insert Cand A reconstruction note (Anne Cowheard 1638 Aylesbury)

After the existing §"Candidate A Aylesbury family group" section added in v23, append:

```markdown
A separate FS Records entry surfaces John Gurney + Anne Cowheard, married 25 Oct 1638, Saint Mary, Aylesbury (FS ID `N2TD-Z9Z`, attached tree `M37F-R5D`). Either (a) a separately documented Aylesbury John, or (b) Cand A remarrying at Aylesbury after Alice Oliffe died, with the 1639-1653 Aylesbury children documented under the second marriage. Mother field is unindexed on the FS Records children entries, so the marriage-to-children link cannot be proven from FS alone. Retain as a Cand A wife-uncertainty note rather than a controlling fact.
```

### 4.3 Replace the existing Working Hypotheses Cand C line

Old:

```markdown
- **Candidate C** (Berkhamsted, Hertfordshire): **~3–5%**. Retained as a minor lead.
```

New:

```markdown
- **Candidate C** (Berkhamsted, Hertfordshire): **~0-1% (effectively eliminated)**. Eight-child Berkhamsted family group 1610-1636 with age mismatch, Francis son 1636, and absent Mary/Peter.
```

### 4.4 Add Ackworth note to "Negative Results and Exclusions"

```markdown
- **Ackworth Yorkshire "Mary Barton" claim unconfirmed in this pass.** FS Records search for John Gurney + spouse Barton in Yorkshire returned zero results on 2026-05-09. FS Records is one of several relevant indexes; FreeREG, Ancestry, FMP regional Yorkshire indexes, and Yorkshire Quaker monthly meeting records have not been walked. Do not treat the FS negative alone as elimination; the original source for the v2 "Mary Barton/Burton (m. 1636)" claim should be re-identified before further qualification.
```

## 5. Apply order

When approved (after v20, v21, v22, v23):

1. Add two source IDs to `data/sources.json`.
2. Create two thin validation files in `sources/validations/`.
3. Edit `research/case-files/john-gurney-case-file-v4.md` per §3.
4. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4.
5. Update `sources/intake/working/john-gurney-audit-state.md` to mark v24 as applied.
