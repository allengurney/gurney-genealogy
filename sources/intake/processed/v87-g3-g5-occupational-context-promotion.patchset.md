# v87 — G3–G5 occupational/institutional context: source registration + fact-sheet promotion

**Type:** discovery-to-publication promotion (no new primary records; contextual/tertiary sourcing).
**Subjects:** G3 Lester Sawyer Gurney III, G4 Lester Sawyer Gurney Jr., G5 Lester Sawyer Gurney.
**Origin:** online-discovery pass (June 2026) on the employers, projects, and institutions named in the G3–G5 fact sheets; findings already landed in the three research companions in a prior turn. This patchset (a) registers the durable contextual sources in `data/sources.json`, (b) promotes the highest-value reader-facing colour into the G3/G4/G5 fact-sheet narratives, and (c) realigns the companion footnotes to the new source IDs.

**Sourcing posture:** every promoted statement here is *background/contextual colour* about an employer, project, or institution — none makes a new genealogical claim about the ancestor (identity, dates, kinship are untouched). Per the contextual-colour band in `.claude/rules/citations.md`, reputable tertiary/encyclopedic sources stand on their own, cited by title and URL. The substantive ancestor facts in each fact sheet retain their existing primary/family-paper citations.

**Outcomes:** all items `promote`.

---

## A. `data/sources.json` — register eight contextual sources

**Action A1 — `str_replace` in `data/sources.json`.** Insert the eight new entries immediately after the `elizabeth-stettler-walker-gurney-obituary` entry.

`old_string`:

```
chorister."
    },
    "us-census-1940": {
```

`new_string`:

```
chorister."
    },
    "great-river-hydro-deerfield-history": {
      "shortTitle": "Great River Hydro, 'Our History' (Deerfield/Connecticut developments)",
      "citation": "\"Our History,\" Great River Hydro, LLC (greatriverhydro.com), consulted June 2026.",
      "archive": "Great River Hydro (online)",
      "url": "https://www.greatriverhydro.com/our-history/",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual/operator history of the Deerfield and Connecticut River hydroelectric developments built by the New England Power Company / New England Power System (Great River Hydro is a later owner; the corporate line runs to National Grid). Dated build-out: Somerset reservoir (1911), Deerfield Nos. 2-5 (1911-1915), Searsburg (1922; 18,412-ft wood-stave penstock), Harriman (1924, 'largest hydroelectric facility east of Niagara Falls at the time'; 12,812-ft bedrock tunnel; reservoir still the largest man-made lake in Vermont), Sherman (1927), Bellows Falls (1928), Comerford/Fifteen Mile Falls (1930). Project context for G4 Lester Sawyer Gurney Jr.'s resident-engineer roles. Tertiary/contextual source per the contextual-colour band in citations.md."
    },
    "cape-cod-canal-history": {
      "shortTitle": "Cape Cod Canal history (Mass.gov; Wikipedia)",
      "citation": "\"History of the Cape Cod Canal and bridges,\" Commonwealth of Massachusetts (mass.gov), with \"Cape Cod Canal,\" Wikipedia; consulted June 2026.",
      "archive": "Commonwealth of Massachusetts; Wikipedia (online)",
      "url": "https://www.mass.gov/info-details/history-of-the-cape-cod-canal-and-bridges",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual history of the Cape Cod Canal: planned and financed by August Belmont II's Boston, Cape Cod & New York Canal Company to designs by the engineer William Barclay Parsons (the Belmont-Parsons partnership that built New York City's first subway); construction 1909-1914, officially completed 1916; a privately operated sea-level toll waterway opened seventeen days ahead of the Panama Canal. Context for G4's 1906-1911 Cape Cod Canal and Cape Cod Construction Company work. Tertiary/contextual source."
    },
    "hoosac-tunnel-wilmington-railroad": {
      "shortTitle": "Hoosac Tunnel & Wilmington Railroad (Wikipedia)",
      "citation": "\"Hoosac Tunnel and Wilmington Railroad,\" Wikipedia; consulted June 2026.",
      "archive": "Wikipedia (online)",
      "url": "https://en.wikipedia.org/wiki/Hoosac_Tunnel_and_Wilmington_Railroad",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual history of the Hoosac Tunnel & Wilmington Railroad (the narrow-gauge 'Hoot, Toot & Whistle'), bought by the New England Power Company to haul dam materials; Searsburg/Harriman construction required relocating its right-of-way to the west side of the Deerfield, and the 1924 Harriman impoundment drowned the village of Mountain Mills. Explains the 'Hoosac Tunnel railroad relocation' named among G4's New England Power assignments. Tertiary/contextual source."
    },
    "comerford-dam-history": {
      "shortTitle": "Frank D. Comerford Dam history (Wikipedia; North Star Monthly)",
      "citation": "\"Frank D. Comerford Dam,\" Wikipedia, with \"Comerford Dam: The Engine of New England's Power Grid,\" North Star Monthly; consulted June 2026.",
      "archive": "Wikipedia; North Star Monthly (online)",
      "url": "https://en.wikipedia.org/wiki/Frank_D._Comerford_Dam",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual history of the Frank D. Comerford Dam at Fifteen Mile Falls on the Connecticut River (1930-31): the largest hydroelectric development in New England when completed; its first generator started remotely by President Herbert Hoover, six years before Hoover Dam. Context for G4's role as assistant to the chief engineer on the Comerford plant. Tertiary/contextual source."
    },
    "mcgraw-edison-history": {
      "shortTitle": "McGraw-Edison company history (Wikipedia; Eaton/Cooper heritage)",
      "citation": "\"McGraw-Edison,\" Wikipedia, with \"Cooper power series product history,\" Eaton; consulted June 2026.",
      "archive": "Wikipedia; Eaton (online)",
      "url": "https://en.wikipedia.org/wiki/McGraw-Edison",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual corporate history of McGraw-Edison, formed 2 January 1957 by the merger of the McGraw Electric Company (Max McGraw, 1900) with Thomas A. Edison, Inc. (the Edison company rooted in West Orange, New Jersey); its power-systems business (Line Material / Kyle reclosers, transformers, switchgear) was sold to Cooper Power Systems in 1985. Context for G3 Lester Sawyer Gurney III's long New Jersey power-engineering career, remembered in family evidence as a McGraw Edison career. Tertiary/contextual source."
    },
    "norwich-university-history": {
      "shortTitle": "Norwich University history (Wikipedia; Norwich catalog)",
      "citation": "\"Norwich University,\" Wikipedia, with \"University History,\" Norwich University Catalog; consulted June 2026.",
      "archive": "Wikipedia; Norwich University (online)",
      "url": "https://en.wikipedia.org/wiki/Norwich_University",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual history of Norwich University, Northfield, Vermont: founded 1819 by Captain Alden Partridge, a former superintendent of West Point; the oldest private military college in the United States, recognized by the Department of Defense as the 'Birthplace of ROTC,' and the first private college in the nation to teach civil engineering. Context for G3's 1941-1943 attendance as a civil-engineering cadet. Tertiary/contextual source."
    },
    "actors-fund-of-america-history": {
      "shortTitle": "Actors' Fund of America history (Wikipedia; NYU finding aid)",
      "citation": "\"Actors' Fund of America\" / \"Entertainment Community Fund,\" Wikipedia, with the Actors' Fund of America Records finding aid, NYU Special Collections; consulted June 2026.",
      "archive": "Wikipedia; New York University Special Collections (online)",
      "url": "https://en.wikipedia.org/wiki/Actors_Fund_of_America",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual history of the Actors' Fund of America (now the Entertainment Community Fund), founded 1882 on the advocacy of the theatrical manager Harrison Grey Fiske; first officers Lester Wallack (president), A. M. Palmer (vice-president), Daniel Frohman (secretary), Theodore Moss (treasurer); relief, the Actors' Fund Home, and burial plots, much of it underwritten by the 1892 Actors' Fund Fair at Madison Square Garden. Context for G5 Lester Sawyer Gurney's assistant-secretaryship (1892). Tertiary/contextual source."
    },
    "actors-order-of-friendship-history": {
      "shortTitle": "Actors' Order of Friendship (Oxford Reference)",
      "citation": "\"Actors' Order of Friendship,\" Oxford Reference; consulted June 2026.",
      "archive": "Oxford Reference (online)",
      "url": "https://www.oxfordreference.com/view/10.1093/oi/authority.20110803095349204",
      "corpusStatus": "none",
      "corpusPath": null,
      "mediaPath": null,
      "validationPath": null,
      "notes": "Contextual history of the Actors' Order of Friendship, a theatrical fraternal benefit order chartered at Philadelphia in 1849 (first lodge the Shakespeare Lodge); its New York branch, the Edwin Forrest Lodge, was established in 1888 by Louis Aldrich, John Drew, and Otis Skinner; the order was the direct precursor of the Actors' Fund of America, which eclipsed it. Context for G5's secretaryship of the Actors' Order of Friendship. Tertiary/contextual source."
    },
    "us-census-1940": {
```

**Action A2 — bump `data/sources.json` meta.** `str_replace`:

`old_string`:

```
    "version": "1.6.0",
    "description": "Canonical source bibliography. Every citable document referenced in fact sheets, case files, or research notes.",
    "lastUpdated": "2026-05-28",
```

`new_string`:

```
    "version": "1.7.0",
    "description": "Canonical source bibliography. Every citable document referenced in fact sheets, case files, or research notes.",
    "lastUpdated": "2026-06-04",
```

---

## B. Fact sheet `fact-sheets/g03-lester-sawyer-gurney-iii-fact-sheet.md`

**Action B1 — Norwich context, Narrative.** `str_replace`:

`old_string`:

```
In September 1941 he entered Norwich University in Vermont as a civil-engineering cadet, completed two years in the upper third of his class, rose to Cadet Sergeant in the Signal Corps, and left in March 1943 — partway through his junior year — to enter the Army.
```

`new_string`:

```
In September 1941 he entered Norwich University in Vermont — the oldest private military college in the United States and the first American college to teach civil engineering <sup class="fn"><a href="#n19" id="ref-19">19</a></sup> — as a civil-engineering cadet, completed two years in the upper third of his class, rose to Cadet Sergeant in the Signal Corps, and left in March 1943 — partway through his junior year — to enter the Army.
```

**Action B2 — McGraw Edison context, Narrative.** `str_replace`:

`old_string`:

```
family memory places the bulk of his career with McGraw Edison in New Jersey.
```

`new_string`:

```
family memory places the bulk of his career with McGraw Edison in New Jersey — the electrical-equipment manufacturer formed in 1957 by the merger of the McGraw Electric Company with Thomas A. Edison's New Jersey company, whose power-systems works built transformers and switchgear for the electric utilities. <sup class="fn"><a href="#n20" id="ref-20">20</a></sup>
```

**Action B3 — add citations n19, n20.** `str_replace`:

`old_string`:

```
(last employer MultiAmp Corporation, Cranford, New Jersey). Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-18">Back</a></li>
</ol>
```

`new_string`:

```
(last employer MultiAmp Corporation, Cranford, New Jersey). Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-18">Back</a></li>
  <li id="n19"><a href="https://en.wikipedia.org/wiki/Norwich_University">"Norwich University,"</a> Wikipedia, and the <a href="https://catalog.norwich.edu/about/history">Norwich University history</a>: founded 1819 by Alden Partridge, a former superintendent of West Point; the oldest private military college in the United States, the Department of Defense's recognized "Birthplace of ROTC," and the first private American college to teach civil engineering. Source ID: <code>norwich-university-history</code>. <a class="citation-back" href="#ref-19">Back</a></li>
  <li id="n20"><a href="https://en.wikipedia.org/wiki/McGraw-Edison">"McGraw-Edison,"</a> Wikipedia, with the <a href="https://www.eaton.com/us/en-us/company/about-us/our-heritage/cooper-power-series.html">Eaton / Cooper power-series heritage</a>: the company was formed on 2 January 1957 by the merger of the McGraw Electric Company with Thomas A. Edison, Inc., the Edison firm rooted in West Orange, New Jersey; its power-systems business — the Line Material and Kyle lines of transformers, reclosers, and switchgear — passed to Cooper Power Systems in 1985. Source ID: <code>mcgraw-edison-history</code>. <a class="citation-back" href="#ref-20">Back</a></li>
</ol>
```

---

## C. Fact sheet `fact-sheets/g04-lester-sawyer-gurney-jr-fact-sheet.md`

**Action C1 — Cape Cod Canal context, Narrative.** `str_replace`:

`old_string`:

```
by age twenty-two he had already entered technical work tied to one of the most significant engineering landscapes in New England. <sup class="fn"><a href="#n16" id="ref-16">16</a></sup></p>
```

`new_string`:

```
by age twenty-two he had already entered technical work tied to one of the most significant engineering landscapes in New England. <sup class="fn"><a href="#n16" id="ref-16">16</a></sup> The canal then being cut across the Cape’s neck was a privately financed sea-level waterway, built by the New York financier August Belmont II to the designs of the engineer William Barclay Parsons — the same partnership that had driven New York City’s first subway — and its backers were racing to open it ahead of the Panama Canal, which it beat into service by seventeen days in 1914. <sup class="fn"><a href="#n22" id="ref-22">22</a></sup></p>
```

**Action C2 — Harriman / Mountain Mills / Comerford context, Narrative.** `str_replace`:

`old_string`:

```
Over the next thirty-five years he was assistant resident engineer on the Searsburg development and the Hoosac Tunnel railroad relocation, resident engineer for the Sherman development, a field surveyor for the Zoar development, and assistant to the chief engineer for the Bellows Falls and Comerford plants; by 1947 he had taken on the duties of Construction Manager of the New England Power Service Company, with the generating plants at Salem, Massachusetts, and White River Junction, Vermont, among the works of his tenure.
```

`new_string`:

```
Over the next thirty-five years he was assistant resident engineer on the Searsburg development and on the Hoosac Tunnel railroad relocation — the rerouting of a Deerfield-valley shortline around the reservoir of the company’s new Harriman dam, briefly the largest hydroelectric plant east of Niagara Falls, whose rising water drowned the little mill village of Mountain Mills in 1924 <sup class="fn"><a href="#n23" id="ref-23">23</a></sup><sup class="fn"><a href="#n24" id="ref-24">24</a></sup> — resident engineer for the Sherman development, a field surveyor for the Zoar development, and assistant to the chief engineer for the Bellows Falls and Comerford plants, the Comerford development at Fifteen Mile Falls on the Connecticut River being, when it opened, the largest hydroelectric plant in New England, its first generator set running by remote signal from President Herbert Hoover <sup class="fn"><a href="#n25" id="ref-25">25</a></sup>; by 1947 he had taken on the duties of Construction Manager of the New England Power Service Company, with the generating plants at Salem, Massachusetts, and White River Junction, Vermont, among the works of his tenure.
```

**Action C3 — add citations n22–n25.** `str_replace`:

`old_string`:

```
reporting Lester Gurney's decree nisi of divorce from Nettie L. Gurney on the ground of desertion. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-21">↩</a></li>
</ol>
```

`new_string`:

```
reporting Lester Gurney's decree nisi of divorce from Nettie L. Gurney on the ground of desertion. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-21">↩</a></li>
  <li id="n22"><a href="https://www.mass.gov/info-details/history-of-the-cape-cod-canal-and-bridges">"History of the Cape Cod Canal and bridges,"</a> Commonwealth of Massachusetts, and <a href="https://en.wikipedia.org/wiki/Cape_Cod_Canal">"Cape Cod Canal,"</a> Wikipedia: the Belmont–Parsons partnership, the 1909–1914 construction, the privately operated sea-level toll waterway, and the seventeen-day margin over the Panama Canal. Source ID: <code>cape-cod-canal-history</code>. <a class="citation-back" href="#ref-22">↩</a></li>
  <li id="n23"><a href="https://www.greatriverhydro.com/our-history/">"Our History,"</a> Great River Hydro, for the New England Power Company's Deerfield River developments: Searsburg (1922) and the Harriman station (1924), "the largest hydroelectric facility east of Niagara Falls at the time," whose reservoir remains the largest man-made lake in Vermont. Source ID: <code>great-river-hydro-deerfield-history</code>. <a class="citation-back" href="#ref-23">↩</a></li>
  <li id="n24"><a href="https://en.wikipedia.org/wiki/Hoosac_Tunnel_and_Wilmington_Railroad">"Hoosac Tunnel and Wilmington Railroad,"</a> Wikipedia: the New England Power Company bought the narrow-gauge line (the "Hoot, Toot &amp; Whistle") to haul dam materials and relocated its right-of-way to the west side of the Deerfield for the Harriman development, whose 1924 impoundment flooded the village of Mountain Mills. Source ID: <code>hoosac-tunnel-wilmington-railroad</code>. <a class="citation-back" href="#ref-24">↩</a></li>
  <li id="n25"><a href="https://en.wikipedia.org/wiki/Frank_D._Comerford_Dam">"Frank D. Comerford Dam,"</a> Wikipedia, with "Comerford Dam: The Engine of New England's Power Grid," <em>North Star Monthly</em>: the Comerford development at Fifteen Mile Falls (1930–31), the largest hydroelectric development in New England when completed, its first generator started remotely by President Herbert Hoover. Source ID: <code>comerford-dam-history</code>. <a class="citation-back" href="#ref-25">↩</a></li>
</ol>
```

---

## D. Fact sheet `fact-sheets/g05-lester-sawyer-gurney-fact-sheet.md`

**Action D1 — Actors' Fund / Order of Friendship context, Narrative.** `str_replace`:

`old_string`:

```
By 1892 Lester had become Assistant Secretary of the Actors’ Fund of America, the major benevolent institution serving the theatrical profession.
```

`new_string`:

```
By 1892 Lester had become Assistant Secretary of the Actors’ Fund of America, the major benevolent institution serving the theatrical profession — founded in 1882, and itself an outgrowth of the older Actors’ Order of Friendship, the theatrical fraternal order whose New York lodge had been organized only a few years earlier. <sup class="fn"><a href="#n19" id="ref-19">19</a></sup><sup class="fn"><a href="#n20" id="ref-20">20</a></sup>
```

**Action D2 — add citations n19, n20.** `str_replace`:

`old_string`:

```
requesting a photograph of the late Lester Gurney, Master of Continental Lodge No. 287 in 1891-92, for a history of the lodge. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-18">↩</a></li>
</ol>
```

`new_string`:

```
requesting a photograph of the late Lester Gurney, Master of Continental Lodge No. 287 in 1891-92, for a history of the lodge. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-18">↩</a></li>
  <li id="n19"><a href="https://en.wikipedia.org/wiki/Actors_Fund_of_America">"Actors' Fund of America" / "Entertainment Community Fund,"</a> Wikipedia, with the <a href="https://findingaids.library.nyu.edu/tamwag/wag_036/">Actors' Fund of America Records</a> finding aid, New York University: the Fund was founded in 1882 on the advocacy of the theatrical manager Harrison Grey Fiske, its first officers Lester Wallack, A. M. Palmer, Daniel Frohman, and Theodore Moss, much of its early relief underwritten by the 1892 fair at Madison Square Garden. Source ID: <code>actors-fund-of-america-history</code>. <a class="citation-back" href="#ref-19">↩</a></li>
  <li id="n20"><a href="https://www.oxfordreference.com/view/10.1093/oi/authority.20110803095349204">"Actors' Order of Friendship,"</a> Oxford Reference: a theatrical fraternal order chartered at Philadelphia in 1849, its New York branch (the Edwin Forrest Lodge) established in 1888 by Louis Aldrich, John Drew, and Otis Skinner; the order was the direct precursor of the Actors' Fund. Source ID: <code>actors-order-of-friendship-history</code>. <a class="citation-back" href="#ref-20">↩</a></li>
</ol>
```

---

## E. Realign research-companion footnotes to the new source IDs

These swap the placeholder "no `data/sources.json` entry yet" tail for the registered Source ID. One `str_replace` per footnote.

**Action E1 — `research/people/g04-lester-sawyer-gurney-jr-fact-sheet.research.md`** (five edits):

- E1a `old`: `opened seventeen days before the Panama Canal. Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `opened seventeen days before the Panama Canal. Source ID: \`cape-cod-canal-history\`.`
- E1b `old`: `successor line to National Grid. Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `successor line to National Grid. Source ID: \`great-river-hydro-deerfield-history\`.`
- E1c `old`: `Comerford/Fifteen Mile Falls (1930). Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `Comerford/Fifteen Mile Falls (1930). Source ID: \`great-river-hydro-deerfield-history\`.`
- E1d `old`: `drowned the village of Mountain Mills. Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `drowned the village of Mountain Mills. Source ID: \`hoosac-tunnel-wilmington-railroad\`.`
- E1e `old`: `started remotely by President Hoover. Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `started remotely by President Hoover. Source ID: \`comerford-dam-history\`.`

**Action E2 — `research/people/g03-lester-sawyer-gurney-iii-fact-sheet.research.md`** (two edits):

- E2a `old`: `sale of the power-systems business to Cooper. Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `sale of the power-systems business to Cooper. Source ID: \`mcgraw-edison-history\`.`
- E2b `old`: `first private U.S. college to teach civil engineering. Encyclopedic context; no \`data/sources.json\` entry yet.`
  `new`: `first private U.S. college to teach civil engineering. Source ID: \`norwich-university-history\`.`

(The `[^g03-536th-negative]` footnote stays unchanged — it is a documented negative result with no registrable source.)

**Action E3 — `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`** (two edits):

- E3a `old`: `office-staff listing already cited in the fact sheet. Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `office-staff listing already cited in the fact sheet. Source ID: \`actors-fund-of-america-history\`.`
- E3b `old`: `precursor of the Actors' Fund. Encyclopedic/collector context; no \`data/sources.json\` entry yet.`
  `new`: `precursor of the Actors' Fund. Source ID: \`actors-order-of-friendship-history\`.`

(The `[^g05-continental-lodge]` footnote stays unchanged — it is a repository pointer for lead L-1, not a fact-sheet-promoted source.)

---

## F. Source tracking and validation decisions

**New source IDs (8):** `great-river-hydro-deerfield-history`, `cape-cod-canal-history`, `hoosac-tunnel-wilmington-railroad`, `comerford-dam-history`, `mcgraw-edison-history`, `norwich-university-history`, `actors-fund-of-america-history`, `actors-order-of-friendship-history`.

**Validation files — deliberately skipped (all 8).** Per the contextual-colour band added to `.claude/rules/citations.md` and the user's direction to keep contextual sourcing lean, these are tertiary/encyclopedic context sources carrying no genealogical claim about an ancestor and no primary-record scope to log. They are fully traceable by title + URL in the `notes`. A per-source validation worksheet (page/folio/image scope, index-vs-image check) would add nothing. This is the documented exception to the default-on validation rule in `.claude/rules/sources.md`.

**No `corpus_supplement` extracts** — no quoted source material over ~150 words; the substance is summarized in the `notes` and the companion prose.

**No media** — no images captured.

## G. Phase-2 checklist
- [ ] Apply A1–A2 (`data/sources.json`: 8 entries + meta bump); confirm valid JSON.
- [ ] Apply B1–B3 (G3 fact sheet); confirm n19/n20 anchors resolve and `ref-19`/`ref-20` are unique.
- [ ] Apply C1–C3 (G4 fact sheet); confirm n22–n25 anchors resolve and `ref-22`–`ref-25` are unique.
- [ ] Apply D1–D2 (G5 fact sheet); confirm n19/n20 anchors resolve and `ref-19`/`ref-20` are unique.
- [ ] Apply E1–E3 (companion footnote realignment).
- [ ] Run `npm run validate` in `site/website` if available; the build mirrors fact-sheets automatically (do not hand-copy to `site/`).
- [ ] Stamp `**Done:** YYYY-MM-DD HH:MM PT` and move this file to `sources/intake/done/`.
