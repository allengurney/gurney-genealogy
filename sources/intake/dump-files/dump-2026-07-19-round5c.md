# Round 5c online-discovery dump — 2026-07-19

**Assimilation status:** raw-source staging only; no existing repository content edited. All captured source text, image captures, grids, and staging notes are in the sibling folder `dump-2026-07-19-files-round5c/`. This round deliberately made **no request to the Norfolk Record Office catalogue** (`https://nrocatalogue.norfolk.gov.uk/`), per the current outage instruction.

## What this round added

| Placement label | Lead / subject | Raw acquisition | Outcome boundary |
| --- | --- | --- | --- |
| `research/people/g13-john-gurney-fact-sheet.research.md` (review before promotion) | **L-238/L-239**, Whinburgh-with-Members tenure | Two authenticated FamilySearch ARK viewer captures, with reproducible grids and a paleography staging note. | The records are now staged but not read: this round does **not** assert that any target person appears in either capture. |
| `research/people/g13-john-gurney-fact-sheet.research.md` / lead ledger | **L-129**, Garveston Rivett/Podmer origin search | Two raw Ancestry collection result extracts, including spelling/model behavior. | Bounded negative: neither target query returned a 1584 Garveston Francis Rivet(t) marriage. This does not prove the register lacks it. |
| `research/people/g13-john-gurney-fact-sheet.research.md` / lead ledger | **L-240**, Margaret Gurney / East Dereham death window | Raw Ancestry collection result extract. | Bounded negative: no 1616–1618 East Dereham burial appeared in the 12 results. It is an index result only, not an image/page sweep. |
| `research/topics/` only if a separate identity-separation note is wanted; otherwise `L-237` evidence ledger | **L-237**, Providence collateral John Gurney | New digitized-book discovery route plus saved raw extract. | A printed genealogy describes a different Providence John Gurney married to Sarah (Thornton) Field. It is a useful identity-separation lead, not evidence for the English John. |

## Captured web objects and artifacts

### L-239 — Whinburgh-with-Members court-roll comparator packet (priority 85)

1. FamilySearch: *Manorial court rolls on the part of Garvestone, Reymerston, Thuxton, Mattishall and Yaxham, 1595–1790*; DGS 004389244; viewer showed image 1 of 2,301 and no index.

   Human URL: https://www.familysearch.org/ark:/61903/3:1:S3HT-6X4K-X5?lang=en

   Saved image: `L-239-whinburgh-1639-ark-3-1-S3HT-6X4K-X5.png`  
   Saved locator grid: `L-239-whinburgh-1639-grid.png`

2. Same collection / DGS, comparison target.

   Human URL: https://www.familysearch.org/ark:/61903/3:1:S3HT-6X45-XZ?lang=en

   Saved image: `L-239-whinburgh-1648-ark-3-1-S3HT-6X45-XZ.png`  
   Saved locator grid: `L-239-whinburgh-1648-grid.png`

3. Packet and reproducibility/read-status note: `L-239-paleography-staging.md`.

**Research read:** The two captures are deliberately held at “untranscribed.” Their stored 1536 × 791 viewer snapshots cannot support a defensible personal-name reading. The next high-value action is an image-level walk on each ARK to reach the identified dated leaf, then full-page grid + target line strips for `Gurney`, `Rivet(t)`, `Allen`, and `Mary` before transcription. This is a materially better next action than repeating generic surname indexes.

### L-129 — Garveston Francis Rivet(t) / Podmer hypothesis (priority 80)

1. Ancestry collection query: *Norfolk, England, Church of England Baptisms, Marriages, and Burials, 1535–1812*.

   Human URL: https://www.ancestry.com/search/collections/61045/?name=Francis_Rivett&event=1584_Norfolk%2C%20England

   Saved raw result extract: `L-129-ancestry-61045-francis-rivett-1584-search.txt`

   The capture reports 16 results. It supplies real Francis/Frances/Franciscus Rivett index variants, including a Francis Rivett marriage dated 1 Oct 1620 and Garveston baptisms for Frances Rivet (20 Nov 1547; 1 Apr 1578), but no 1584 Garveston marriage result.

2. Ancestry collection query using the putative spouse surname/token.

   Human URL: https://www.ancestry.com/search/collections/61045/?name=Podmer&event=1584_Norfolk%2C%20England

   Saved raw result extract: `L-129-ancestry-61045-podmer-1584-search.txt`

   The capture reports 62 results (first 20 shown). Its closest 1584 result is an unreadable `P??` / rendered `Pothumer` **burial**, 5 Sep 1584, Norwich St Simon and St Jude—not a Garveston marriage. No claim is made about relationship or identity from that result.

**Bounded negative ledger:** These are two independently designed collection-index probes (Rivett variant and transitive Podmer token). Neither surfaces the proposed 1584 Garveston marriage. Stop this exact mechanism here; next move should be the known parish-register leaf/image window, not another broad Ancestry name form.

### L-240 — East Dereham Margaret Gurney / Rivett burial continuation (priority 80)

Ancestry collection query: *Norfolk, England, Church of England Baptisms, Marriages, and Burials, 1535–1812*.

Human URL: https://www.ancestry.com/search/collections/61045/?name=Margaret_Gurney&event=1616_Norfolk%2C%20England

Saved raw result extract: `L-240-ancestry-61045-margaret-gurney-1616-search.txt`

The capture reports 12 results. It returns, among others, Margaret Gurney baptised 1 Mar 1589 at Tasburgh (parents indexed Alexander and Johan), Margrett Gurnie baptised 25 Apr 1596, and Margaretta Gurny buried 29 Nov 1653 at Great Dunham. It does **not** return a 1616–1618 East Dereham burial. The date parameter clearly did not fully constrain all displayed results, so preserve this only as an index negative—not a rejection of the East Dereham hypothesis.

### L-237 — Providence collateral identity separation (priority 65)

1. Geneanet catalogue record for *The early records of the town of Providence, Vol. 7*.

   Human URL: https://en.geneanet.org/library/doc/5583135/the-early-records-of-the-town-of-providence-vol-7

   The public catalogue reports six Gurney citations in the 1892, 270-page volume; it is a new locator route for a controlled later page-level sweep.

2. Digitized *Field Genealogy*, volume 1.

   Human URL: https://upload.wikimedia.org/wikipedia/commons/f/f4/Books_from_the_Library_of_Congress_%28IA_fieldgenealogybe01pier%29.pdf

   Saved raw discovery extract / retrieval ledger: `L-237-web-discovery-extracts.md`

   The captured passage says Sarah Thornton, widow of Zachariah Field, married second John Gurney and refers to *Early Providence records*, Book 2, p. 200. This identifies a Providence couple that must remain separate from the uncertain English G13 John Gurney candidate unless primary evidence later connects them.

## Artifact manifest

`sources/intake/dump-files/dump-2026-07-19-files-round5c/`

- `L-129-ancestry-61045-francis-rivett-1584-search.txt`
- `L-129-ancestry-61045-podmer-1584-search.txt`
- `L-237-web-discovery-extracts.md`
- `L-239-paleography-staging.md`
- `L-239-whinburgh-1639-ark-3-1-S3HT-6X4K-X5.png`
- `L-239-whinburgh-1639-grid.png`
- `L-239-whinburgh-1648-ark-3-1-S3HT-6X45-XZ.png`
- `L-239-whinburgh-1648-grid.png`
- `L-240-ancestry-61045-margaret-gurney-1616-search.txt`

## Gated / failed retrieval ledger

| Object / mechanism | Status | Retained response / action |
| --- | --- | --- |
| Wikimedia *Field Genealogy* PDF direct binary retrieval | Gated by local Windows TLS credential failure (`SEC_E_NO_CREDENTIALS`) on first try | No further same-mechanism retry. The human PDF URL and raw search extract are preserved in `L-237-web-discovery-extracts.md`. |
| Geneanet detailed page retrieval | Cache-miss gate | Public catalogue search extract retained; no assertion about its six entries. |
| NRO catalogue | Intentionally skipped | No NRO request was made in this round. |

## Suggested immediate assimilation actions

1. Add the two **bounded index negatives** to L-129 and L-240 only; do not alter the underlying relationships or dates.
2. Keep L-239 open at priority 85. Promote neither image capture as evidence until high-resolution leaves are staged and read.
3. Add the L-237 Providence John/Sarah Field couple to an exclusion/comparator ledger, not to the ancestor line.

## Round-6 kickoff prompt (campaign wrap-up)

> Work in main. Read `AGENTS.md`, the applicable source/research rules, the online-discovery strategy skill, FS-FTS and FMP skills, `data/search-variants.json`, and `tools/research_leads_README.md`. Do not edit existing repo content. Create only a new dated Round-6 dump and sibling artifact folder. First inspect all Round 5 / 5b / 5c dumps and use `tools/research_leads.py` plus `repo_search.py` to build a **master list of every lead worked across all discovery rounds**, with priority, mechanisms attempted, raw artifacts, result/negative/gated status, and exact next action. Then conduct a final breadth-to-depth research pass: prioritize direct ancestor evidence and the G13 John Gurney/Rivett corridor, perform image-level work for L-239 and the known Garveston/East Dereham leaf windows, and use at least one new creative source. Record all actual human URLs, raw text extracts, images/ARK staging, a negative ledger, and a campaign closeout that classifies every lead as advanced, exhausted-for-now, gated, or deferred. Skip `https://nrocatalogue.norfolk.gov.uk/` while it remains down.

**Dump complete (structured for assimilation, placement labels).**
