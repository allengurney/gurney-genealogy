# Intake patchset v25 - Qualify Peter Anomaly + add Norfolk John Gurney cluster

```yaml
patchset_id: v25
created: 2026-05-09
repo_scope: gurney-genealogy
phase: phase_1_patchset_only
primary_case_file: research/case-files/john-gurney-case-file-v4.md
primary_research_file: research/people/g13-john-gurney-fact-sheet.research.md
working_memo: sources/intake/working/john-gurney-audit-state.md
phase_2_rule: Apply only after v20, v21, v22, v23, v24. v25 qualifies the case file's Peter Anomaly claim and adds new Norfolk John Gurney households to the §8 elimination table.
```

## 0. Audit report

### 0.1 Scope

Pass 7 (2026-05-09) pivoted English-side searches to child-cluster matching, per user direction to stop using negative results as definitive eliminators and instead look for: (a) any English John Gurney household whose children match the colonial John's distinctive set (Sarah, Mary, Richard, John Jr., Peter, possibly Isaac), and (b) evidence that the case file's "Peter Anomaly" claim should be qualified.

### 0.2 Peter Anomaly qualified

The standing case-file claim (G13, §6.2, §11) is that "An exhaustive England-wide search found ZERO Peter Gurney baptisms 1620-1645 in any branch, any spelling variant. The name is completely foreign to the Gurney surname universe across 500 years."

A Findmypast Britain-wide Parish Baptisms search for first name Peter, last name Gurney (variants on both), year of birth 1632-1642 returns **12 results.** The most diagnostic of these is:

- **Peter G.**, christened 27 February 1641, **Smallburgh, Norfolk, England.** Father: Peter G. Mother: unindexed. Record set: England Births & Baptisms 1538-1975. FMP transcript ID `R_880200102`.

The "G." surname truncation is partial — the FMP record indexes only the first letter — but the spelling-variant universe for Gurney explicitly includes Garney, Gourney, Gurnay, Gunney, etc. The Smallburgh Peter G. entry's Peter-father naming pattern shows that Peter was in use in a Norfolk Gurney-variant household contemporary with the colonial John's lifetime.

This does not contradict Cand B (Francis G14 + Margaret Rybett) — Francis G14's children were not at Smallburgh — but it does weaken the case file's strong "Peter is completely absent from every documented Gurney branch" framing. The Peter Anomaly should be qualified, not retracted.

### 0.3 Norfolk John Gurney households (FMP UK-wide Parish Baptisms, 2026-05-09)

A Findmypast UK-wide Parish Baptisms search for surname Gurney, father first name John (variants on both), year 1623-1643, restricted to Norfolk, returns 14 results. Households visible:

| Household | Parish | Children indexed | Notes |
|---|---|---|---|
| **John Gurney + Rachell** | Denton, Norfolk | Mary 10 Aug 1638 (FS ID `NNDF-V9K`, mother Rachell on index record); Thomas 24 Jan 1639; Sarah 1644 | NEW. Wife is Rachell, not Mary. Children dates 10 years too late for colonial John's Mary c.1628 / Sarah c.1625-1632. Add to §8 elimination row. |
| **John Gurney** | Hempnall and the Hempnall Group of Parishes, Norfolk | Anna 1640, Elizabeth 1641 | NEW. South Norfolk. No Mary/Peter/Richard/John Jr in this index window. |
| John Gurney (case file standing: Earsham) | Earsham, Norfolk | John Gerney 1635, John Girney 1636, Henry Girney 1638, Susan Girney 1638 | Already eliminated in case file (PROB 11/260/14 area). FMP corroborates the Earsham John + Elizabeth Singler family group. |
| John Gurney | Stanfield, Norfolk | Mary G?tiner 1634 | Stanfield is mid-Norfolk near East Dereham (Cand B father Francis G14's parish). Single indexed child. |
| John Gurney | Norwich, St Margaret & St Swithin, Norfolk | "G?" 1630 | Norwich parish — Cand B father Francis G14's commercial-life city. Single indexed child. |
| John Gurney | North Runcton, Norfolk | Beniamin G? 1625, Frances G? 1628 | West Norfolk near King's Lynn (where Francis G14 had a failed 1622-25 manufacturing venture). |

None of these Norfolk John Gurney households match the colonial John's full children pattern (Sarah + Mary + Richard + John Jr. + Peter + possibly Isaac) by name + date. The Denton John + Rachell has Mary + Sarah but wife is Rachell and dates are late. None is a strengthener for Cand B; all add to the residual "Unknown other origin" elimination pool.

### 0.4 Strategic implication

The Norfolk Gurney density (six distinct John Gurney households in mid-17th-century Norfolk) is consistent with Cand B's geographic plausibility but doesn't directly strengthen Cand B because none of the Norfolk Johns match the colonial John's children. Cand B remains a Francis-G14-son inference, not a Norfolk-John-Gurney-with-matching-children inference.

## 1. Source registry operation

Add two source objects in `data/sources.json`:

```json
    "findmypast-uk-parish-baptisms": {
      "shortTitle": "Findmypast UK Parish Baptisms (BMD)",
      "fullTitle": "Findmypast UK Parish Baptisms aggregated dataset within Birth, Marriage, Death & Parish Records",
      "publisher": "Findmypast",
      "type": "parish register aggregated index (subscription)",
      "url": "https://search.findmypast.co.uk/search-united-kingdom-records-in-birth-marriage-death-and-parish-records/and_parish-baptisms",
      "notes": "Used 2026-05-09 for Peter Gurney 1632-1642 Britain-wide search (12 results; Peter G. 1641 Smallburgh Norfolk transcript R_880200102) and for the Norfolk Gurney + father John 1623-1643 cluster (14 results, including Denton, Hempnall, Stanfield, Norwich, North Runcton, and Earsham households)."
    }
```

(Reuse the existing `fs-england-births-christenings` source ID for the FS Mary Gurney Denton 1638 record.)

## 2. Validation note

Create `sources/validations/findmypast-uk-parish-baptisms.md` (thin), following the v22/v24 shape, citing the two 2026-05-09 search results above.

## 3. Proposed case-file edits (research/case-files/john-gurney-case-file-v4.md)

### 3.1 Qualify the Peter Anomaly in §6.2 and the related §11 endnote

Old §6.2:

```markdown
### 6.2 The Peter Anomaly

An exhaustive England-wide search found ZERO Peter Gurney baptisms 1620–1645 in any branch, any spelling variant. The name is completely foreign to the Gurney surname universe across 500 years. Peter almost certainly derives from wife Mary's family — a maternal grandfather, uncle, or godfather. Identifying Mary's maiden name and finding a "Peter" in her family would provide strong independent confirmation of John-1's origin.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>
```

New §6.2:

```markdown
### 6.2 The Peter Anomaly (qualified)

An England-wide FamilySearch search found zero Peter Gurney baptisms 1620-1645. A subsequent Findmypast UK Parish Baptisms search 1632-1642 with surname variants returned twelve Peter Gurney baptism results, including a Peter G., father Peter G., christened 27 February 1641 at Smallburgh, Norfolk (FMP transcript R_880200102; "G." is a partial surname index). The Smallburgh entry is a Norfolk Gurney-variant household using the name Peter in the same decade the colonial John named his son Peter, so the case-file's earlier "Peter is completely foreign to the Gurney surname universe" framing is weakened. Peter as a child of the colonial John remains distinctive — none of the twelve FMP results match a John-Gurney-father pattern — but the name was not absolutely absent from Norfolk Gurney households. Mary's maiden family remains the most likely source of the colonial son Peter's name; identifying her maiden name and a Peter in her family would still provide independent confirmation of John-1's origin.<sup class="fn"><a href="#n55" id="ref-55">55</a></sup>
```

### 3.2 Add two Norfolk rows to the §8 elimination table

```markdown
| Denton, Norfolk (John + Rachell) | Norfolk | **Rachell** | **ELIMINATED** | FMP UK Parish Baptisms and FS England Births and Christenings 1538-1975 (FS ID JM `NNDF-V9K`): Mary Gurney christened 10 Aug 1638 Denton Norfolk, father John Gurney, mother Rachell; Thomas Gurney 24 Jan 1639 Denton Norfolk, father John; Sarah Gurney 1644 Denton Norfolk, father John. Wife Rachell (not Mary), and the Mary + Sarah children's dates are ~10 years too late for the colonial John's children. Separate Norfolk John Gurney household.<sup class="fn"><a href="#nZC" id="ref-ZC">ZC</a></sup> |
| Hempnall (and the Hempnall Group of Parishes), Norfolk | Norfolk | Unknown | **ELIMINATED** | FMP Norfolk Baptisms: Anna Gurney 1640 and Elizabeth Gurney 1641, father John. No Mary, no Peter, no Richard among indexed children. Separate Norfolk John Gurney household.<sup class="fn"><a href="#nZC" id="ref-ZC">ZC</a></sup> |
```

Add new endnote (number on application):

```html
<li id="nZC" value="ZC">Findmypast UK Parish Baptisms search 2026-05-09, surname Gurney (variants), father John (variants), year of birth 1623-1643, place keyword Norfolk; FamilySearch, "England, Births and Christenings, 1538-1975," Mary Gurney christening 10 August 1638 Denton, Norfolk, mother Rachell (FS ID `NNDF-V9K`, <a href="https://www.familysearch.org/ark:/61903/1:1:NNDF-V9K">https://www.familysearch.org/ark:/61903/1:1:NNDF-V9K</a>). Source IDs: <code>findmypast-uk-parish-baptisms</code>; <code>fs-england-births-christenings</code>. <a class="backref" href="#ref-ZC">↩</a></li>
```

## 4. Proposed G13 research-file edits

### 4.1 Qualify the Peter Anomaly section

Update the existing "Peter" subsection under "Children — working notes" with parallel qualifying language to §3.1 above.

### 4.2 Add a "Norfolk John Gurney density" section

```markdown
### Norfolk John Gurney household density (FMP UK Parish Baptisms, 2026-05-09)

A Findmypast UK Parish Baptisms search restricted to Norfolk for surname Gurney + father John, year 1623-1643, returns 14 results across six distinct Norfolk parishes: Denton (John + Rachell, children Mary 1638, Thomas 1639, Sarah 1644), Hempnall (Anna 1640, Elizabeth 1641), Stanfield (Mary 1634), Norwich St Margaret & St Swithin (a 1630 child), North Runcton (Beniamin 1625, Frances 1628), and Earsham (already case-file eliminated; John + Elizabeth Singler).

None of these Norfolk John Gurney households match the colonial John's full distinctive children pattern (Sarah + Mary + Richard + John Jr. + Peter + possibly Isaac) by name + date. The density of Norfolk John Gurney households is nevertheless consistent with Cand B's geographic plausibility: Norfolk was a Gurney heartland with multiple parish-level Johns in the same decade.[^fmp-norfolk-cluster-2026-05-09]

[^fmp-norfolk-cluster-2026-05-09]: Findmypast UK Parish Baptisms search 2026-05-09; FamilySearch Mary Gurney Denton 1638 (FS ID `NNDF-V9K`); source IDs `findmypast-uk-parish-baptisms` and `fs-england-births-christenings`.
```

## 5. Apply order

When approved (after v20-v24):

1. Add `findmypast-uk-parish-baptisms` to `data/sources.json`.
2. Create `sources/validations/findmypast-uk-parish-baptisms.md` (thin).
3. Edit `research/case-files/john-gurney-case-file-v4.md` per §3.
4. Edit `research/people/g13-john-gurney-fact-sheet.research.md` per §4.
5. Update `sources/intake/working/john-gurney-audit-state.md` to mark v25 as applied.
