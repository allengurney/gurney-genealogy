# Intake patchset v12 - 1963 Gurney family handwritten notes

```yaml
patchset_id: v12
created: 2026-05-04
intake_file: C:\Users\allen\Downloads\1963_gurney_family_handwritten_notes_revised_findings_v3.md
phase: 1 intake preparation only
phase_2_rule: Execute the operations below. The source reasoning, destination decisions, sourceId, and proposed research/fact-sheet blocks are already resolved here.
```

## Standard

- One retained source package: eight photographed handwritten Gurney family notebook pages, with a revised findings memorandum prepared 4 May 2026.
- Outcome: promote.
- Treatment: over-inclusive. Preserve the family-note variants, interpretation notes, and open research leads in research files; publish only stable, reader-ready G3 material in the new fact sheet.
- Weighting rule: pages 5-8, in Dana Gurney's hand, should carry more interpretive weight than pages 1-4 where they clarify ambiguous readings. Where Dana's notes conflict with stronger civil/vital records already in the repo, preserve the note as a family-note variant and do not overwrite the established fact without record review.
- G3 receives a new fact sheet and a paired research companion.
- No handwritten page image files were supplied in this phase. The supplied markdown memorandum is preserved as the intake/archive artifact and source-associated working reference; the page photographs should be copied later if/when available.

## Coverage inventory

| Lead | Outcome | Source handling | Research destinations |
| --- | --- | --- | --- |
| Eight handwritten Gurney family notes pages; revised findings v3 | Promote | Add `gurney-family-handwritten-notes-1963`; archive the supplied MD; create corpus transcription; create validation | `research/people/g03-lester-sawyer-gurney-iii-fact-sheet.research.md`; `fact-sheets/g03-lester-sawyer-gurney-iii-fact-sheet.md`; `research/people/g02-lester-hayes-gurney-fact-sheet.research.md`; `research/people/g04-lester-sawyer-gurney-jr-fact-sheet.research.md`; `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`; `research/people/edith-walberg-scott-gurney.md`; `research/people/ethel-june-hayes.md`; `research/people/helen-hill-helene-ransome-gurney-obrien.md`; `research/topics/gurney-engineering-continuity.md` |

## Source registry operations

Update `data/sources.json` in place. Update `meta.lastUpdated` to the phase 2 application date. Insert the new source near the modern-family and Rigler/FairHaven entries.

```json
"gurney-family-handwritten-notes-1963": {
  "shortTitle": "1963 Gurney family handwritten notes",
  "citation": "Gurney family handwritten oral-history and research notes, eight photographed notebook pages; revised findings memorandum v3 prepared 4 May 2026 from page photographs. Pages 1-4 are earlier loose family notes; pages 5-8 are later cleaner notes in the hand of Dana Gurney.",
  "archive": "Allen Gurney family papers / user-supplied revised findings memorandum",
  "url": null,
  "corpusStatus": "partial",
  "corpusPath": "sources/corpus_supplement/1963-gurney-family-handwritten-notes-transcription.md",
  "mediaPath": "sources/media/gurney-family-handwritten-notes-1963/1963_gurney_family_handwritten_notes_revised_findings_v3.md",
  "validationPath": "sources/validations/gurney-family-handwritten-notes-1963.md",
  "notes": "Close-family handwritten notes and later revised findings for G2 Lester Hayes Gurney, G3 Lester Sawyer Gurney III, Edith Walberg Scott Gurney, G4 Lester Sawyer Gurney Jr., Ethel June Hayes, G5 Lester Sawyer Gurney, Helen Hill / Helene Ransome / Helen Gurney / Helen O'Brien, Lawrence Branch O'Brien, Edward Godfrey Walberg, Mildred Nora Thursby, and related family chronology. Key retained findings: G3 born 10 Jun 1923 Wellesley Hills; G3 and Edith married 23 Nov 1942 NYC; G3 was a lieutenant, commissioned Jun/Jul 1944, served with Air Service Command at Robins Field and 536th Signal Heavy Construction Company at Manila when G2 was born; G2 born 16 Nov 1945 at St. Vincent's Hospital, NYC; G3 second marriage to Dorothy Lillian Haben/Haden on 6 Jun 1965; Edith died 27 Dec 1963 Chatham NJ; Edith completed a New York Stock Exchange Institute course for 'Customers' Men' 8 Jun 1939; Edith's parents Edward Godfrey Walberg and Mildred Nora Thursby named; G4 date variants and 'dropped the S'; Ethel's father Albert C. Hayes, master car builder for Boston & Albany RR; Helen identity chain to Lawrence Branch O'Brien. Treat conflicts as family-note variants pending original-record review."
}
```

## File operations

Create the source-media folder and copy the supplied memorandum into it:

```powershell
New-Item -ItemType Directory -Force -Path 'sources\media\gurney-family-handwritten-notes-1963'
Copy-Item -LiteralPath 'C:\Users\allen\Downloads\1963_gurney_family_handwritten_notes_revised_findings_v3.md' -Destination 'sources\media\gurney-family-handwritten-notes-1963\1963_gurney_family_handwritten_notes_revised_findings_v3.md'
```

Copy the raw intake memorandum into the archive after the phase 2 content edits are applied:

```powershell
Copy-Item -LiteralPath 'C:\Users\allen\Downloads\1963_gurney_family_handwritten_notes_revised_findings_v3.md' -Destination 'sources\intake\archive\v12-gurney-family-handwritten-notes-1963.md'
```

Create `sources/corpus_supplement/1963-gurney-family-handwritten-notes-transcription.md`:

````markdown
# 1963 Gurney family handwritten notes - page transcriptions

Source ID: `gurney-family-handwritten-notes-1963`
Scope: Appendix A transcriptions from `1963_gurney_family_handwritten_notes_revised_findings_v3.md`, prepared 4 May 2026 from eight photographed handwritten notebook pages. Pages 1-4 are earlier loose notes. Pages 5-8 are in Dana Gurney's hand.

## Page 1

```text
1920-21 Mom Born
Died 82 years old
lived with father
[?] - 102 years  got 18 or 19 years
to get away from Papa
He left him & divorced him

1943 - met at USO Dance
[?] go together
[Married? / Marine?] state side
Married 1 1/2 to 1 3/4 [years?]
Dad overseas - gone 1 1/2 years
Dad left for overseas July or Aug.
and Les born in November.
N.Y. City - November.

[Right margin]
Commission
1 year after
they married

[Arithmetic]
27
16
---
1911

1963
1911
----
52

Stock exchange before divorce
[?]

6 mos after custom marriage
[?] stayed and she quit
and [worked?] some

1st job teletype operator at stock
exchange

New England Electric [System?]

Mom hobbies
plants & gardening
housework

[First?] had
Cancer 46 or 47
Breast - 1 breast
remove[d].
No
recurren[ce]
until
Parkinson
[?]
```

## Page 2

```text
Raised
by [Aunt? / Hinton?]
Edith Walling

Helen O'Byrne [or O'Brien?] (last)
Gurney
18 or 19 years old
[holding? / working?] stage when
married - 1st [husband?] was
dramatic critic & post[?]

Lester S. Gurney born
(S. [Norcross? / Norwood?])
1882-1885 [prob. uncertain / erroneous]

Died when [??]
[?]
Married 21 or 22

Lost father
when 2 or 3
years

Mother went back
on stage to support

[Manuel? / Manual?] O[?]
later only

Married 1919-1928
?

Ethel June Hayes - Indianapolis or [Conn?]
Died 198[0/8?]
Born 1900

Dad - Mother

Cal. Mabel [?]
Aunt C. Hayes
RR
(sister)

Died when
Ethel 20
raised
family

[Arithmetic fragments]
1900 - 41
       20
       21

[?] 15
    30
    51

Dad - [Asplund? / Asphor?]
till 2028 [or 20?]
```

## Page 3

```text
Gurney - St. Andrews Episcopal
- [Drew / Down?] [Station?] (also raised)
Vietnam

Civil Engineer for N.E. Elect.
Syst[em]

Construction Manager

Average
Wanted to be writer but never made it.

Mother

Dad Cook - Housewife
Had a [colored?] maid - 6 years
to out of
high school

Norwich
2 or 3 years - left for same
employer

1963

1963 - 12
 62    11
 61    10
 60     9
 59     8
```

## Page 4

```text
- born 1923

Les & Edith -
Married      11 - [42/43]

Dad Gurney
commissioned June or July 1944

Helen Hill - maiden
" Gurney - (he died early)
" O'Brien - 2nd marriage
[Branch O'Brien?]

actress - returned to stage
1890s & again 1908-1910

Lester Gurney Jr. -
HS grad 1901 est
(dropped the S

Moved to Wellesly where
Dad Gurney was ca. 6 yr old
- maybe 1929
```

## Page 5 - Dana Gurney hand

```text
Lester Gurney III
Born June 10, 1923    Wellesley Hills, MA
Died Dec 19, 2011

Married Edith Walberg Scott
Nov 23, 1942
N.Y. City
Edith born 1920-21?
lived with father
At age 18-19, married

[Right side]
Married Dorothy
Lillian Haben [or Haden?]
June 6, 1965

Lester Gurney III
was Lt. & stationed at Manila
Commissioned June or July 1944
with 536th Signal Heavy Construction Co
when Lester Hayes Gurney was born 11-16-45
in NY City, St Vincent's Hospital

When he married Edith, he was serving with
the Air Service Command at Robins Field, GA
Had been class of '45 Norwich Univer[sity]
```

## Page 6 - Dana Gurney hand

```text
Lester S. Gurney                  dropped the S
Born 2-13-1890
Died Aug 5, 1958

[Left margin]
2nd wife

Married Ethel June Hayes
April 23, 1921 (see marriage certif)
Springfield, MA

[Right side]
Born Feb 1880
Died [Nov crossed out] Oct 1951

[Crossed out]
was niece of Mr & Mrs Charles [Boss? / Bross? / Ross?]

Ethel's parents
Albert C. Hayes
Master Car Builder for
Boston & Albany RR
```

## Page 7 - Dana Gurney hand

```text
Children of Lester Gurney Jr (II)

Lester Sawyer Gurney       son of Gen Wm Gurney
                            died 1899
[Movie/Music?] Critic

Helen Ransome Hill
Broadway Star    1890s & again 1906-1910
Married [Branch crossed?] Lawrence Branch O'Brien
on 4-12-1900
Branch died 4-12-1922
```

## Page 8 - Dana Gurney hand

```text
Edith Walberg Scott Gurney

Born
Died Dec 27, 1963 (Chatham, NJ)
Her mother died when she was 12
Married Scott to get away from Papa

Met Lester III at USO Dance    1943?

June 8, 1939 completed course for
"Customers' Men" New York Stock Exchange
Institute - foreign specialist?
About 6 mon later, foreign exchange closed
trading (due to war) - she quit

Edith's Parents
Edward Godfrey Walberg    Born 11-11-1889
Mildred Nora Thursby      Born 1-11-1888
```
````

## Validation file

Create `sources/validations/gurney-family-handwritten-notes-1963.md`:

```markdown
# Source validation: 1963 Gurney family handwritten notes

Source ID: `gurney-family-handwritten-notes-1963`
Patchset: `sources/intake/processed/v12-gurney-family-handwritten-notes-1963.patchset.md`

## Scope examined

- Supplied memorandum: `C:\Users\allen\Downloads\1963_gurney_family_handwritten_notes_revised_findings_v3.md`.
- Eight photographed handwritten notebook pages are represented through the supplied transcription and revised findings memo.
- Pages 1-4 are earlier loose notes. Pages 5-8 are later cleaner notes in Dana Gurney's hand.

## Status

Usable as close-family evidence and source-associated transcription. Original page photographs were not copied into the repo during phase 1; if available, they should be added later under `sources/media/gurney-family-handwritten-notes-1963/`.

## Findings landed

- `fact-sheets/g03-lester-sawyer-gurney-iii-fact-sheet.md`
- `research/people/g03-lester-sawyer-gurney-iii-fact-sheet.research.md`
- `research/people/g02-lester-hayes-gurney-fact-sheet.research.md`
- `research/people/g04-lester-sawyer-gurney-jr-fact-sheet.research.md`
- `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`
- `research/people/edith-walberg-scott-gurney.md`
- `research/people/ethel-june-hayes.md`
- `research/people/helen-hill-helene-ransome-gurney-obrien.md`
- `research/topics/gurney-engineering-continuity.md`
```

## Data operations

In `data/ancestors v26.json`, replace only the existing G3 object with the following. Do not reformat the whole file.

```json
{
  "type": "ancestor",
  "gen": "G3",
  "name": "Lester Sawyer Gurney III",
  "dates": "1923-2011",
  "geography": "Wellesley Hills, MA; New York City; Robins Field, GA; Manila; New Jersey",
  "eraId": "era-modern-america",
  "lineageStatus": "Confirmed",
  "summary": "Wellesley Hills-born power engineer and wartime Army/Air Service Command officer; father of Lester Hayes Gurney (G2). Family notes place him with the Air Service Command at Robins Field when he married Edith Walberg Scott and with the 536th Signal Heavy Construction Company at Manila when G2 was born.",
  "notables": "Born 10 June 1923 at Wellesley Hills, Massachusetts; died 19 December 2011. Married Edith Walberg Scott on 23 November 1942 in New York City; later married Dorothy Lillian Haben/Haden on 6 June 1965. Dana Gurney's notes identify him as a lieutenant, commissioned June or July 1944, formerly Norwich University class of 1945, and stationed at Manila with the 536th Signal Heavy Construction Company when Lester Hayes Gurney was born at St. Vincent's Hospital, New York City, on 16 November 1945. Family evidence also remembers his long McGraw Edison power-engineering career in New Jersey.",
  "landHoldings": "-",
  "spouses": [
    {
      "name": "Edith Walberg Scott",
      "dates": "m. 23 November 1942, New York City; d. 27 December 1963, Chatham, New Jersey",
      "notes": "Mother of Lester Hayes Gurney (G2); previously married to a man named Scott"
    },
    {
      "name": "Dorothy Lillian Haben/Haden",
      "dates": "m. 6 June 1965",
      "notes": "Surname uncertain in family notes; verify by marriage record"
    }
  ],
  "children": [
    {
      "name": "Lester Hayes Gurney",
      "dates": "1945-2025",
      "notes": "G2 in direct line"
    }
  ],
  "buttons": [
    {
      "label": "Fact sheet",
      "url": "/fact-sheets/g03-lester-sawyer-gurney-iii-fact-sheet.html",
      "style": "bio"
    }
  ],
  "recordId": "ancestor-g3-lester-sawyer-gurney-iii",
  "placeRefs": [
    "place-new-york-metropolitan-area-usa"
  ]
}
```

Do not add new place records in phase 2 unless the place registry already has matching IDs. The G3 data block keeps the existing broad New York metropolitan placeRef and leaves Robins Field, Manila, Wellesley Hills, Chatham, and St. Vincent's Hospital as research/fact-sheet text until the place registry is deliberately expanded.

## Fact sheet operation - create G3

Create `fact-sheets/g03-lester-sawyer-gurney-iii-fact-sheet.md` with the following exact content:

```markdown
---
layout: layouts/base.njk
permalink: /fact-sheets/g03-lester-sawyer-gurney-iii-fact-sheet.html
title: Lester Sawyer Gurney III Fact Sheet
pageHeading: Lester Sawyer Gurney III (1923-2011)
subtitle: "Ancestor fact sheet for G03 in the direct Gurney line. Wellesley Hills-born power engineer, wartime lieutenant, and father of Lester Hayes Gurney. Initial draft, May 2026."
description: "Compact fact sheet for Lester Sawyer Gurney III in the direct Gurney line."
bodyClass: bio-page factsheet-page
activeNav: factsheets
updated: 4 May 2026
factsheet:
  gen: G03
  slug: g03-lester-sawyer-gurney-iii-fact-sheet
  personName: Lester Sawyer Gurney III
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "name": "{{ factsheet.personName }} - Fact Sheet",
  "description": "{{ description }}",
  "mainEntity": {
    "@type": "Person",
    "name": "{{ factsheet.personName }}",
    "birthDate": "1923-06-10",
    "deathDate": "2011-12-19",
    "birthPlace": { "@type": "Place", "name": "Wellesley Hills, Massachusetts" },
    "description": "Power engineer and wartime lieutenant; husband of Edith Walberg Scott; father of Lester Hayes Gurney."
  }
}
</script>

<div class="factsheet-top">
  <div class="factsheet-main">

<section class="fact-section fact-section-vitals" id="vital-records">
<div class="facts-vitals-grid">
  <div class="fact-item">
    <div class="fact-label">Born</div>
    <div class="fact-value">10 June 1923, Wellesley Hills, Massachusetts. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Died</div>
    <div class="fact-value">19 December 2011. <sup class="fn"><a href="#n2" id="ref-2">2</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Education / Military</div>
    <div class="fact-value">Norwich University class of 1945 before wartime service; lieutenant, commissioned June or July 1944, with family notes placing him in the Air Service Command at Robins Field, Georgia, and later at Manila with the 536th Signal Heavy Construction Company. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
  </div>
  <div class="fact-item">
    <div class="fact-label">Occupation</div>
    <div class="fact-value">Power engineer, remembered in family evidence for a long McGraw Edison career in New Jersey. <sup class="fn"><a href="#n4" id="ref-4">4</a></sup></div>
  </div>
  <div class="fact-item fact-item-span-2">
    <div class="fact-label">Marriage(s)</div>
    <div class="fact-value">
      <div class="stacked-records">
        <div><strong>Edith Walberg Scott</strong> - married 23 November 1942, New York City. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
        <div><strong>Dorothy Lillian Haben/Haden</strong> - married 6 June 1965; surname uncertain in the handwritten note. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></div>
      </div>
    </div>
  </div>
</div>
</section>

<section class="fact-panel fact-panel-highlights" id="highlights">
<h2 class="unnumbered">Highlights</h2>
<ul>
  <li><strong>The wartime service clue is more specific than the older family reading.</strong> Dana Gurney's notes identify him as a lieutenant, commissioned in June or July 1944, serving with the Air Service Command at Robins Field, Georgia, when he married Edith, and later stationed at Manila with the 536th Signal Heavy Construction Company when his son Les was born. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></li>
  <li><strong>His marriage to Edith belongs in New York City in 1942.</strong> The family notes give the date as 23 November 1942, correcting the earlier ambiguous "11-42/43" reading. <sup class="fn"><a href="#n5" id="ref-5b">5</a></sup></li>
  <li><strong>He was absent overseas at the birth of G2.</strong> Lester Hayes Gurney was born 16 November 1945 at St. Vincent's Hospital in New York City while G3 was stationed at Manila. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>The engineering line runs through him.</strong> Family evidence remembers G3 as a McGraw Edison power engineer in New Jersey, between G4 Lester Sawyer Gurney Jr.'s civil-engineering career and G2 Lester Hayes Gurney's Indiana and Michigan Electric / AEP career. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
</ul>
</section>

<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Dates</th>
      <th>Mother</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Lester Hayes Gurney</td><td>1945-2025</td><td>Edith Walberg Scott</td><td>G2 in the direct line; born 16 November 1945 at St. Vincent's Hospital, New York City, while his father was stationed at Manila. <sup class="fn"><a href="#n7" id="ref-7b">7</a></sup></td></tr>
  </tbody>
</table>
</section>

<section class="fact-section fact-narrative" id="narrative">
<h2 class="unnumbered">Narrative</h2>

<p>Lester Sawyer Gurney III stands at the hinge between the Massachusetts/New York engineering world of his father and the Indiana utility career of his son. Dana Gurney's family notes place his birth at Wellesley Hills, Massachusetts, on 10 June 1923 and identify him as having been Norwich University class of 1945 before wartime service. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n3" id="ref-3c">3</a></sup></p>

<p>The notes give his marriage to Edith Walberg Scott as 23 November 1942 in New York City. They also clarify his military setting: when he married Edith, he was serving with the Air Service Command at Robins Field, Georgia; he was later a lieutenant, commissioned in June or July 1944, and stationed at Manila with the 536th Signal Heavy Construction Company when Lester Hayes Gurney was born in New York City on 16 November 1945. <sup class="fn"><a href="#n5" id="ref-5c">5</a></sup><sup class="fn"><a href="#n3" id="ref-3d">3</a></sup><sup class="fn"><a href="#n7" id="ref-7c">7</a></sup></p>

<p>That service context revises an earlier family-note reading that had suggested "Marine." The stronger reading is Army / Army Air Forces / Signal Corps context: Air Service Command, Robins Field, Manila, and the 536th Signal Heavy Construction Company. Unless a separate Marine record appears, G3 should not be described as a Marine. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></p>

<p>After the war, G3 belongs to the family's twentieth-century engineering continuity. Family evidence remembers him as a power engineer with McGraw Edison in New Jersey, between his father Lester Sawyer Gurney Jr.'s civil-engineering work and his son Lester Hayes Gurney's later utility career at Indiana and Michigan Electric / AEP. <sup class="fn"><a href="#n4" id="ref-4c">4</a></sup></p>
</section>

<section class="fact-section" id="citations">
<h2 class="unnumbered">Citations</h2>

<ol class="citation-list">
  <li id="n1">Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Page 5 transcription in Dana Gurney's hand: "Lester Gurney III / Born June 10, 1923 Wellesley Hills, MA." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-1">Back</a></li>
  <li id="n2">Gurney family handwritten notes, Page 5 transcription: "Died Dec 19, 2011." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-2">Back</a></li>
  <li id="n3">Gurney family handwritten notes, Page 5 transcription: "was Lt. & stationed at Manila"; "Commissioned June or July 1944"; "with 536th Signal Heavy Construction Co"; "serving with the Air Service Command at Robins Field, GA"; "Had been class of '45 Norwich University." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-3">Back</a></li>
  <li id="n4">Gurney family handwritten notes, revised findings memorandum v3, G3 consolidated interpretation and cross-generational engineering continuity section, recording Allen Gurney family evidence that G3 spent most of his career with McGraw Edison in New Jersey. Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-4">Back</a></li>
  <li id="n5">Gurney family handwritten notes, Page 5 transcription: "Married Edith Walberg Scott / Nov 23, 1942 / N.Y. City." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-5">Back</a></li>
  <li id="n6">Gurney family handwritten notes, Page 5 transcription, right-side note: "Married Dorothy / Lillian Haben [or Haden?] / June 6, 1965." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-6">Back</a></li>
  <li id="n7">Gurney family handwritten notes, Page 5 transcription: G3 was with the 536th Signal Heavy Construction Company "when Lester Hayes Gurney was born 11-16-45 / in NY City, St Vincent's Hospital." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-7">Back</a></li>
  <li id="n8">Gurney family handwritten notes, revised findings memorandum v3, "Major correction from earlier reading," explaining that the earlier "Marine state side" reading should be downgraded in favor of Army / Army Air Forces / Signal Corps context. Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-8">Back</a></li>
</ol>
</section>

  </div>

  <aside class="factsheet-side">

<div class="fact-panel">
  <h2>Related Links</h2>
  <div class="fact-buttons">
    <a href="/fact-sheets/g02-lester-hayes-gurney-fact-sheet.html">Lester Hayes Gurney (G2)</a>
    <a href="/fact-sheets/g04-lester-sawyer-gurney-jr-fact-sheet.html">Lester Sawyer Gurney Jr. (G4)</a>
    <a href="/maps-and-lists/ancestor-table.html">Ancestor Table</a>
  </div>
</div>

<div class="fact-panel">
  <h2>Timeline</h2>
  <table class="fact-timeline-table">
    <tbody>
      <tr><th>Year</th><th>Event</th></tr>
      <tr><td>1923</td><td>Born 10 June at Wellesley Hills, Massachusetts.</td></tr>
      <tr><td>1942</td><td>Marries Edith Walberg Scott in New York City, 23 November.</td></tr>
      <tr><td>1944</td><td>Commissioned in June or July, according to Dana Gurney's notes.</td></tr>
      <tr><td>1945</td><td>Stationed at Manila with the 536th Signal Heavy Construction Company when son Lester Hayes Gurney is born in New York City.</td></tr>
      <tr><td>1965</td><td>Marries Dorothy Lillian Haben/Haden, 6 June, according to the family notes.</td></tr>
      <tr><td>2011</td><td>Dies 19 December.</td></tr>
    </tbody>
  </table>
</div>

  </aside>
</div>
```

## Research file operations

### Create `research/people/g03-lester-sawyer-gurney-iii-fact-sheet.research.md`

```markdown
# Lester Sawyer Gurney III (G03) - Research Companion

Research companion for `g03-lester-sawyer-gurney-iii-fact-sheet.md`.

---

## Working Notes

### Family handwritten notes - birth, marriage, military service, and G2 birth context

Dana Gurney's later notes identify Lester Sawyer Gurney III as born 10 June 1923 at Wellesley Hills, Massachusetts, and deceased 19 December 2011. They state that he married Edith Walberg Scott on 23 November 1942 in New York City. When he married Edith, he was serving with the Air Service Command at Robins Field, Georgia, and had been Norwich University class of 1945. The notes further state that he was a lieutenant, commissioned in June or July 1944, and stationed at Manila with the 536th Signal Heavy Construction Company when Lester Hayes Gurney was born on 16 November 1945 at St. Vincent's Hospital in New York City. Family evidence supplied by Allen Gurney separately identifies Lester Sawyer Gurney III as a power engineer with a long McGraw Edison career in New Jersey.[^g03-notes]

The Page 5 marriage date should supersede the earlier ambiguous "11-[42/43]" reading on Page 4 unless the New York City marriage record proves otherwise. The Page 5 reading is fuller, specific to day/month/year, and fits the later military and G2 birth sequence better than an 11-43 date.[^g03-notes]

The earlier possible "Marine state side" reading should be downgraded. With Dana's notes, the better interpretation is Army / Army Air Forces / Signal Corps context: Air Service Command at Robins Field, a lieutenant's commission in June or July 1944, and service with the 536th Signal Heavy Construction Company at Manila. Unless separate Marine records are found, G3 should not be labeled as a Marine.[^g03-notes]

### Second marriage

Dana Gurney's Page 5 note records that Lester Sawyer Gurney III married Dorothy Lillian Haben or Haden on 6 June 1965. The event and date are strong enough to preserve; the surname requires confirmation from the marriage record before being treated as settled.[^g03-notes]

### Research actions

- Locate G3 birth record: Wellesley Hills, Massachusetts, 10 June 1923.
- Locate G3 and Edith Walberg Scott marriage record: New York City, 23 November 1942.
- Locate G3 military commission / personnel record.
- Search Robins Field / Air Service Command personnel context for late 1942.
- Search 536th Signal Heavy Construction Company and Manila assignment records.
- Search Norwich University class-of-1945 records.
- Locate McGraw Edison retirement or employment paperwork.
- Locate G3 and Dorothy Lillian Haben/Haden marriage record, 6 June 1965.

---

## Sources Consulted

- Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages. Source ID: `gurney-family-handwritten-notes-1963`.

[^g03-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, especially Appendix A, Pages 4-5 and the G3 revised person-by-person findings. Source ID: `gurney-family-handwritten-notes-1963`.
```

### Append to `research/people/g02-lester-hayes-gurney-fact-sheet.research.md`

Add under `## Working Notes`, after the FairHaven obituary section:

```markdown
### Family handwritten notes - St. Vincent's Hospital and wartime birth context

Dana Gurney's notes add a precise hospital-level birth detail for Lester Hayes Gurney: he was born 16 November 1945 in New York City at St. Vincent's Hospital, while his father, Lester Sawyer Gurney III, was stationed at Manila with the 536th Signal Heavy Construction Company. The note preserves a useful wartime family context: G3 was overseas/absent at G2's birth, and the family was still in the New York City orbit in November 1945.[^g02-family-notes]

[^g02-family-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Page 5 transcription in Dana Gurney's hand. Source ID: `gurney-family-handwritten-notes-1963`.
```

### Append to `research/people/g04-lester-sawyer-gurney-jr-fact-sheet.research.md`

Add under `## Working Notes`, replacing `*No entries yet.*` if it is still present:

```markdown
### Family handwritten notes - name, date variants, Ethel June Hayes, and engineering leads

Dana Gurney's notes write G4 as "Lester S. Gurney" and add the phrase "dropped the S," a useful name-variant clue for later record searches. The same note gives his birth as 13 February 1890 and death as 5 August 1958. Existing project data gives his birth as 13 May 1888, so the Dana birth date should be preserved as a family-note variant pending review of the original birth source and later self-reported documents.[^g04-family-notes]

The same Dana note gives his marriage to Ethel June Hayes as 23 April 1921 at Springfield, Massachusetts, with "see marriage certif." The current project date is 26 April 1921. The difference may be a license date, certificate date, ceremony date, transcription error, or family-note error; resolve from the original marriage certificate/register before changing the fact sheet.[^g04-family-notes]

Earlier loose notes add that the relevant Gurney man was a civil engineer for "N.E. Elect. Syst[em]" and a construction manager. Given the existing G4 civil-engineering profile, this is best treated as a G4 lead rather than a settled employment claim. Search New England Electric System, Cape Cod / Massachusetts engineering directories, and Long Island Rail Road electrification context before promoting it.[^g04-family-notes]

The Page 4 note that the family moved to Wellesley when "Dad Gurney" was about six, maybe 1929, aligns well with G3's 1923 birth and the existing Wellesley / Wellesley Hills trail for G4's household.[^g04-family-notes]

[^g04-family-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 3-4 and Page 6 transcription in Dana Gurney's hand. Source ID: `gurney-family-handwritten-notes-1963`.
```

### Append to `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`

Add under `## Working Notes`, replacing `*No entries yet.*` if it is still present:

```markdown
### Family handwritten notes - Helen identity chain and possible critic label

Dana Gurney's notes identify Lester Sawyer Gurney as the son of Gen. William Gurney and note his death in 1899. A nearby word appears to read "movie critic," "music critic," or simply "critic," but this is not yet consistent with the better-documented Actors' Fund / Actors' Order of Friendship profile and should be treated as an oral-history label or possible misreading pending corroboration.[^g05-family-notes]

The same notes strongly support the identity chain Helen Hill / Helene Ransome / Helen Gurney / Helen O'Brien. Page 7 gives "Helen Ransome Hill," describes her as a Broadway star in the 1890s and again 1906-1910, and states that she married Lawrence Branch O'Brien on 12 April 1900. Page 4 frames the sequence as Helen Hill as maiden name, Gurney as married name after which "he died early," and O'Brien as a second marriage. This makes Helen O'Brien probably identical with Helen Hill / Helene Ransome / Helen Gurney, pending formal proof from marriage and census records.[^g05-family-notes]

[^g05-family-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 4 and 7. Source ID: `gurney-family-handwritten-notes-1963`.
```

### Create `research/people/edith-walberg-scott-gurney.md`

```markdown
# Edith Walberg Scott Gurney

Working research file for Edith Walberg Scott Gurney, first wife of Lester Sawyer Gurney III (G3) and mother of Lester Hayes Gurney (G2).

---

## Working Notes

### Family handwritten notes - name, family, first marriage, NYSE training, and death

Dana Gurney's notes identify Edith as "Edith Walberg Scott Gurney," clarifying that Scott was likely a prior married name rather than a middle name. They state that Edith died 27 December 1963 in Chatham, New Jersey; that her mother died when she was 12; and that she married Scott to get away from "Papa." The notes also record that Edith completed a New York Stock Exchange Institute course for "Customers' Men" on 8 June 1939, apparently with a foreign-exchange or "foreign specialist" connection, and that about six months later foreign-exchange trading closed because of the war and she quit. She married Lester Sawyer Gurney III on 23 November 1942 in New York City.[^edith-notes]

The notes give Edith's parents as Edward Godfrey Walberg, born 11 November 1889, and Mildred Nora Thursby, born 11 January 1888. The note that Edith's mother died when Edith was 12 may make Mildred's death searchable around 1932-1933 if Edith was born about 1920-1921.[^edith-notes]

Page 8 says Edith met Lester III at a USO dance, possibly in 1943. Because Dana's Page 5 gives a marriage date of 23 November 1942, the 1943 note should not be treated as a firm first-meeting date. It may be a misremembered year, a later wartime social context, or an ambiguous note.[^edith-notes]

Earlier loose notes add that Edith's hobbies included plants, gardening, and housework. They also include a health note about breast cancer at age 46 or 47 with one breast removed, but this conflicts with the 1963 death date if Edith was born in 1920-1921. Preserve the note as a private-family research lead and do not publish it without a specific editorial decision.[^edith-notes]

The earlier "died 82 years old" note probably does not refer to Edith. Page 8 gives Edith's death in 1963 at about age 42-43 if she was born in 1920-1921.[^edith-notes]

### Research actions

- Locate Edith birth record, about 1920-1921.
- Locate Edith death record: Chatham, New Jersey, 27 December 1963.
- Locate first marriage to Scott, likely about 1938-1940.
- Locate divorce or annulment from Scott, if applicable.
- Locate marriage to Lester Sawyer Gurney III, New York City, 23 November 1942.
- Search New York Stock Exchange Institute course records for 8 June 1939.
- Search employment and city-directory records for securities, teletype, foreign exchange, or brokerage work.
- Search Edward Godfrey Walberg birth, marriage, death.
- Search Mildred Nora Thursby birth, marriage, death.
- Search Walberg/Thursby marriage record and Mildred's death around 1932-1933.

[^edith-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 1, 5, and 8. Source ID: `gurney-family-handwritten-notes-1963`.
```

### Create `research/people/ethel-june-hayes.md`

```markdown
# Ethel June Hayes

Working research file for Ethel June Hayes, second wife of Lester Sawyer Gurney Jr. (G4) and mother of Lester Sawyer Gurney III (G3).

---

## Working Notes

### Family handwritten notes - Hayes identity and railroad-family lead

Dana Gurney's notes identify Ethel June Hayes as the second wife of Lester S. Gurney, married 23 April 1921 at Springfield, Massachusetts, with a parenthetical "see marriage certif." The note gives Ethel as born February 1880 and deceased October 1951, though this conflicts with earlier rough notes suggesting "born 1900." Dana also identifies Ethel's father as Albert C. Hayes, a master car builder for the Boston & Albany Railroad. This is a strong research lead into Ethel's railroad-family background.[^ethel-notes]

Earlier loose notes say Ethel's father died when she was about 20 and mention "Aunt C. Hayes" with "RR" and "sister." Preserve these as clues, but resolve them against census, death, obituary, and railroad employment records before using them as settled family structure.[^ethel-notes]

### Research actions

- Locate Ethel's birth record and reconcile February 1880 vs "born 1900."
- Locate Ethel's death record, likely October 1951.
- Review G4 and Ethel marriage certificate/register for 23 April vs 26 April 1921.
- Search Albert C. Hayes in Boston & Albany Railroad employment references, city directories, census records, and obituaries.
- Determine whether Albert C. Hayes died when Ethel was about 20.
- Identify "Aunt C. Hayes" and the railroad/sister note.

[^ethel-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 2 and 6. Source ID: `gurney-family-handwritten-notes-1963`.
```

### Create `research/people/helen-hill-helene-ransome-gurney-obrien.md`

```markdown
# Helen Hill / Helene Ransome / Helen Gurney / Helen O'Brien

Working research file for Helen Hill, apparently the actress Helene Ransome, wife of Lester Sawyer Gurney (G5), and later wife of Lawrence Branch O'Brien.

---

## Working Notes

### Family handwritten notes - identity chain and second marriage

Dana Gurney's notes strongly support the identity chain Helen Hill / Helene Ransome / Helen Gurney / Helen O'Brien. One page gives "Helen Ransome Hill," describes her as a Broadway star in the 1890s and again 1906-1910, and states that she married Lawrence Branch O'Brien on 12 April 1900. Another page frames the sequence as Helen Hill as maiden name, Gurney as married name after which "he died early," and O'Brien as a second marriage. This makes Helen O'Brien probably identical with Helen Hill / Helene Ransome / Helen Gurney, pending formal proof from marriage and census records.[^helen-notes]

The note that Helen returned to the stage after Gurney died early fits the known chronology of G5 Lester Sawyer Gurney's death in 1899 and the Page 7 statement that she was active again 1906-1910. The Page 2 wording "Mother went back on stage to support" likely belongs to this same cluster.[^helen-notes]

Dana's notes identify Helen's later husband as Lawrence Branch O'Brien, married 12 April 1900, and state that Branch died 12 April 1922. These dates should be used to locate marriage and death records that can prove the Helen Hill / Ransome / Gurney / O'Brien identity chain.[^helen-notes]

### Research actions

- Find marriage record for Helen Gurney / Helen Hill / Helen Ransome to Lawrence Branch O'Brien, 12 April 1900.
- Find death record or obituary for Lawrence Branch O'Brien, 12 April 1922.
- Search theatrical press for Helen Ransome, Helene Ransome, Helen Ransome Hill, Helen Gurney, and Helen O'Brien.
- Focus theatrical search on the 1890s and 1906-1910.
- Review 1910 census for Branch and Helen O'Brien.

[^helen-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 2, 4, and 7. Source ID: `gurney-family-handwritten-notes-1963`.
```

### Create or append `research/topics/gurney-engineering-continuity.md`

If the file does not exist, create it. If it exists, append this section.

```markdown
# Gurney Engineering Continuity

Working topic file for the recurring engineering / infrastructure thread from G4 through G2.

---

## Working Notes

### Family handwritten notes - power, civil, railroad, and electrical infrastructure

The "third-generation power engineer" line is best framed as power, civil, railroad, and electrical-infrastructure engineering across three generations rather than identical job titles. G4 Lester Sawyer Gurney Jr. was a civil engineer with documented Cape Cod Canal and Cape Cod Construction Company context, and family notes add possible New England Electric System, construction manager, and Long Island Rail Road electrification leads. G3 Lester Sawyer Gurney III is remembered in family evidence as a McGraw Edison power engineer in New Jersey, with wartime technical service in Air Service Command / Signal Corps settings. G2 Lester Hayes Gurney was a power engineer at Indiana and Michigan Electric / AEP.[^engineering-notes]

The family phrase "third-generation power engineer" is therefore meaningful as family shorthand for sustained engineering work in power and infrastructure, even though G4's confirmed title is civil engineer and the specific New England Electric System / LIRR leads still require record proof.[^engineering-notes]

[^engineering-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, especially Page 3, Page 5, and the cross-generational engineering continuity section; FairHaven Funeral Home obituary for Lester Hayes Gurney, 2025. Source IDs: `gurney-family-handwritten-notes-1963`; `fairhaven-lester-obituary`.
```

## Optional fact-sheet edits for existing pages

Phase 2 may keep existing G2/G4/G5 fact sheets unchanged if the reviewer wants research-first intake only. If applying fact-sheet updates now, use only the following light-touch changes.

### `fact-sheets/g02-lester-hayes-gurney-fact-sheet.md`

- In the Born vital, revise "16 November 1945, New York City, New York" to "16 November 1945, St. Vincent's Hospital, New York City, New York".
- Add a citation to `gurney-family-handwritten-notes-1963` near that hospital claim.
- In the narrative first paragraph, add one sentence: "Family notes place his father, Lester Sawyer Gurney III, at Manila with the 536th Signal Heavy Construction Company when Les was born in New York City."

### `fact-sheets/g04-lester-sawyer-gurney-jr-fact-sheet.md`

- Do not change the established birth date or Ethel marriage date in the fact sheet in phase 2.
- Optionally add a concise research-link sentence only if desired: "Family notes preserve alternate dates for his birth and marriage to Ethel June Hayes; these remain research variants pending record review."

### `fact-sheets/g05-lester-sawyer-gurney-fact-sheet.md`

- Do not add the uncertain "critic" label to the fact sheet.
- Optionally add a concise sentence that family notes strengthen the Helen Hill / Helene Ransome / Helen O'Brien identity chain, but keep the detailed proof work in research.

## Open issues for phase 2 summary

- Original page photographs were not supplied/copied in phase 1.
- Dorothy Lillian's surname is uncertain: Haben vs Haden.
- G4 date conflicts remain unresolved: 13 May 1888 vs 13 February 1890; 26 April 1921 vs 23 April 1921.
- Ethel's birth year remains unresolved: February 1880 vs earlier rough "born 1900."
- The health note for Edith should stay in research only unless explicitly approved for publication.
- Do not label G3 as a Marine unless separate records support it.

## Phase 2 validation

After applying:

- Confirm `data/sources.json` parses as JSON.
- Confirm `data/ancestors v26.json` parses as JSON.
- Run the site validation from `site/website` with the repo's Windows-safe command:

```powershell
npm.cmd run validate
```
