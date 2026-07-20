# Round-3 raw extracts (traceability)

Zero images pulled this round (zero-token discipline; all image targets staged for packet 53).
This file holds the verbatim/structured extracts behind the round-3 dump findings.

---

## A. NRO catalogue entries (nrocatalogue.norfolk.gov.uk) — the three new-record references

**Margery Gurney (Gurnye), widow of East Dereham — will 1602-03**
- Reference: **ANF will register Liber 35 (Offwood) fo. 191** (Archdeaconry of NORFOLK, not Norwich)
- Microfilm: NRO **MF 197**
- Finding aid: *Norfolk Genealogy* vol. 10
- Access: "Not to be produced to the searchroom / Use microfilm MF 197"
- Permalink: http://nrocatalogue.norfolk.gov.uk/index.php/gurney-gurnye-margery-of-east-dereham-widow

**Alexander Gurney of Tasburgh — administration 1617**
- Reference: **ANF administration act book 1611-1619 fo. 101** (Archdeaconry of Norfolk)
- Microfilm: NRO **MF 501**
- Finding aid: "Typescript index: ANW and ANF wills and admons 1604-1686"
- Permalink: http://nrocatalogue.norfolk.gov.uk/index.php/gurney-alexander-of-tasburgh

**Thomas Gurnay, Esquire, of Great Ellingham — inventory 1615-16**
- NRO permalink 502'd all session (server down). Ancestry 62679/155780 record page confirms:
  Name "Thomas Gurnay", Record Type **Inventory**, Probate Date 1615-1616, Probate Place Norfolk;
  Notes "Gurnay, Thomas, Esquire, of Great Ellingham (Norfolk)".
- Court/register reference [REC] — pending NRO catalogue server recovery.
- Permalink (down): http://nrocatalogue.norfolk.gov.uk/index.php/gurnay-thomas-esquire-of-great-ellingham-norfolk

---

## B. FamilySearch catalogue chain — ANF register films (koha:291384)

`Wills and administrations, 1459-1857` — Church of England, **Archdeaconry of Norfolk. Court**;
177 microfilm reels; filmed 1957; original at District Probate Registry, Norwich.
Register-copy-wills volume list carries the "(book name)" in parentheses after each volume number:

- v. 32 (Bale), 1595-1598 — British Film 167088 / DGS 8045769
- v. 33 (Bradfild), 1597-1599 — Film 167089 / DGS 8045770
- v. 34 (Wright), 1599-1602 — Film 167090 / DGS 8045771
- **v. 35 (Offwood), 1602-1604 — British Film 167091 / DGS 8045772**  ← Margery Gurney fo. 191
- v. 36, 1604-1606 — Film 167092 / DGS 8045773
- v. 37, 1607-1609 — Film 167093 / DGS 7904830
- v. 38, 1610-1611 — Film 167094 / DGS 8045774

FTS coverage test on DGS 008045772 (JSON endpoint): `+wife` = 0 results, `Gurn*` = 0 results
→ this ANF register film is NOT full-text indexed on FamilySearch (image-only; confirms round-2 FTS negative).

Other catalog records surfaced (keyword "Archdeaconry of Norfolk wills", 13 hits):
- koha:121415 — Index of wills proved in the Norfolk Archdeaconry Court (Palgrave-Moore) [the index]
- koha:278818 — Probate records, Episcopal Consistory Court + Archdeaconry [NCC + arch]
- koha:504379 — Wills and administrations, 1469-1857 [second court's registers]
- **koha:84018 — Rutledge, "A Calendar of Great Yarmouth enrolled apprenticeship indentures, 1563-1665"** (L-245-relevant)

---

## C. Norwich Freemen Records Online (nfro.norwichfreemen.org.uk) — L-245

Database coverage confirmed: **only Phase 1 (1714-present) is loaded**; Phase 2 (1317-1713) NOT yet online.
- Search `surname=Rivett`: 6 results, all 1814-1830 (Trivett/Rivett; H.C. Rivett printer, apprenticeship 1820).
- Search `surname=Gurney`: 112 results, minimum year **1719**, max 1966 — no pre-1714 entries.
→ The 1548-1713 window (L-245 decisive freemen test) is NOT searchable on NFRO yet; Millican's printed register remains the route.

**Collateral: Norwich Gurney worsted-weaver freemen cluster (earliest entries):**
- Robert Gurney 1719 (Master, Apprenticeship)
- Andrew Gurney 1722 (Worstead Weaver, new freeman, apprenticeship)
- John Gurney 1723 (Worstead Weaver); Benjamin 1723; Edmund 1723; Joseph 1723 (all Worstead Weaver, new freemen)
- John Gurney 1725 (Worstead Weaver, patrimony); Andrew Gurney 1725 (father of freeman, patrimony)
- John Gurney 1738 (patrimony); Joseph Gurney 1738 (father, patrimony); Benjamin Gurney 1739 (Hotpresser)
Each record's detail page carries father/master + method (apprenticeship/patrimony/purchase).

---

## D. British History Online (L-174) — accessible this session (no CAPTCHA); authenticated/subscribed

- `"Edmund Gurnay"` = 12 hits. The modern-era one: **Cecil Papers: December 1602, 16-25 = cal-cecil-papers/vol12/pp518-528** (the Dec-1602 entry L-174 sought). Others = Close Rolls (a different medieval Edmund) + held Blomefield.
- `"Henry Gurnay"` = 2 hits, both Blomefield Norfolk topography (Harpham/Harpley, Attleborough) — held.
- `"Francis Gurnay"` = 0.
- `Gournay Norfolk` = 124 hits, overwhelmingly Blomefield + Close Rolls + CIPM (medieval, largely held).
→ Direct Tudor/Stuart line (Henry G15 / Francis G14) has NO modern-series footprint beyond Blomefield;
  family's only BHO modern-series appearances = the two Cecil Papers Edmund entries (Dec-1602 + 1606, both captured).

---

## E. FMP London Apprenticeship Abstracts 1442-1850 (Cliff Webb; covers ALL companies incl. Merchant Taylors')

- `lastname=Gurney` (all years) = **142 Results**.
- `firstname=John lastname=Gurney`, apprenticeship 1630 ±25 (≈1605-1655) = **12 Results**.
- Result rows render in cross-origin iframes; row detail (father / company / master) not scriptable —
  interactive record-opening required. [REC — read the 12 John rows for father="Francis" and/or company="Merchant Taylors'" patrimony.]

## F. ROLLCO (londonroll.org) — Records of London's Livery Companies Online
Companies covered: Bowyers', Clothworkers', Drapers', Founders', Girdlers', Goldsmiths', Mercers',
Musicians', Salters', Stationers', Tallow Chandlers'. **Merchant Taylors' NOT covered.**
Scripted all-company `surname=Gurney` search returned the form (results load interactively) — [REC] retry interactively; limited value (Francis's company absent).

## G. NEHH (New England's Hidden Histories) — migrated to Quartex
- Portal: congregationallibrary.org/nehh → digital collections at congregationallibrary.quartexcollections.com
- Full-text search: `/documents/search?search=<term>`
- `Gurney` surfaced collection-level hits incl. Braintree First Church (1697-1871) and **Abington, Mass. First Church (1714-1949)** — Abington sits in the G8-G12 Weymouth/Bridgewater orbit (NEW relevant set).
- No Gurney match visible in transcription snippets (many records image-only); per-record reads needed. Weymouth = confirmed NEHH gap.
