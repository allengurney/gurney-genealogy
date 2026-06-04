**Done:** 2026-06-04 16:30 PT

# v83 patchset - Gurney family papers from G3 to G2: certificates, clippings, Masonic letters

Prepared: 2026-06-04
Phase: 1 preparation
Scope: Promote the 2026-06-03 22:57 scan batch of Gurney family papers as a new source family; add a corpus supplement and validation; route the certificate, newspaper, Masonic, marriage, probate, and military details into G2-G5 research and fact sheets. Fact-sheet, research, and data edits are written here as literal operations ready for Phase 2.

## Intake summary

Source posture supplied by Allen: cite as family papers from G3 passed to G2, in possession of G1.

This batch includes thirty scans under `sources/intake/new/Family pages/Scanned_20260603-2257-*.jpg`: official certificates, military papers, grade reports, newspaper clippings, Masonic correspondence, a SAR ancestor chart, funeral/probate documents, and one handwritten 1900 letter. `Scanned_20260603-2257-02.jpg` has no substantive family text but is retained for scan-sequence integrity.

Allen resolved the pre-patchset questions as follows (see `sources/intake/new/Family pages/family-papers-20260603-2257-capture.md`):

- G3 commission date: certification documentation is primary; Dana/family June-July 1944 note retained as secondary memory.
- G3 birthplace: Springfield (city-clerk certificate) is primary; Wellesley Hills is the documented childhood home.
- G3-Dorothy marriage: 26 June 1965 printed certificate/invitation is primary; 6 June family-note variant noted but not dwelt on.
- G4 birth date: retain both current and variant dates; do not overwrite from the derivative SAR chart.
- Privacy: exclude G1 living-person details from public-facing updates.

Two handwritten-note extrapolations remain open for Allen's confirmation and are deliberately kept out of the published fact sheets pending his answer (the 1900 "My dear Blanche" letter identities; see the Helen research operation below, which files them as a transcription and hypothesis). They are detailed in the capture note.

## New source ID

Add to `data/sources.json`, near `gurney-family-handwritten-notes-1963`.

`new file write` (JSON object inserted into the `sources` map):

```json
    "gurney-family-papers-g3-to-g2-certificates-clippings": {
      "shortTitle": "Gurney family papers from G3 to G2",
      "citation": "Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); certificates, clippings, military papers, Masonic correspondence, and related family documents scanned 3 June 2026.",
      "archive": "Allen Gurney family papers",
      "url": null,
      "corpusStatus": "partial",
      "corpusPath": "sources/corpus_supplement/2026-gurney-family-papers-g3-to-g2-certificates-clippings.md",
      "mediaPath": "sources/media/gurney-family-papers-g3-to-g2-certificates-clippings/",
      "validationPath": "sources/validations/gurney-family-papers-g3-to-g2-certificates-clippings.md",
      "notes": "Thirty scanned family-paper pages. Major content: G3 Springfield birth certification (Wellesley Hills childhood home); G3 Norwich University civil-engineering attendance 1941-1943 and full wartime Signal Corps chronology, including outside-plant telephone-line construction on Luzon supervising 75 enlisted men, prisoner-of-war labor, and 75 civilian linemen; G3 pre-war employment as assistant construction engineer at New England Power Company, Boston; G3 St. Alban's Lodge No. 6 (Bristol, RI) junior-deacon notice and Bristol social life; G3 marriages to Edith W. Scott (1942) and Dorothy Lillian Hoben (1965); Dorothy Hoben birth/death/probate; G4 marriage to Ethel June Hayes (23 Apr. 1921); G4 1920 Worcester divorce from Nettie; G4 thirty-five-year New England Power System career and 1953 retirement; G5 marriage certificate to Helen Ransome Hill (1881); Helen Ransome Gurney-Lawrence Branch O'Brien marriage (1900); 1936 Masonic correspondence for G5/G6 Continental Lodge context. SAR chart includes G1 living-person details and is private/source context only."
    },
```

## Media promotion

Create `sources/media/gurney-family-papers-g3-to-g2-certificates-clippings/` and copy these from `sources/intake/new/Family pages/`, preserving filenames:

`Scanned_20260603-2257-01.jpg` through `Scanned_20260603-2257-30.jpg` (all thirty).

After copy and validation, leave the originals in the intake queue per the current workflow. Do not delete source media. The SAR chart (`-13`) carries living-person G1 detail; keep it as source context only.

## Corpus supplement

Create `sources/corpus_supplement/2026-gurney-family-papers-g3-to-g2-certificates-clippings.md`.

1. Start with this header:

```markdown
# 2026 Gurney family papers from G3 to G2 - certificates, clippings, and correspondence

Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`

Source posture: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); scanned 3 June 2026.

This is a targeted corpus supplement, not a diplomatic transcription of every certificate form word. Certificates and administrative papers are summarized for pertinent genealogical facts. Newspaper clippings and substantive correspondence are transcribed as completely as visible in the scans. Cropped or unreadable text is marked explicitly.

Privacy: the SAR chart includes G1 living-person detail; do not reproduce that detail in public-facing files.
```

2. Copy the `## Scan inventory and extracted details` section verbatim from `sources/intake/new/Family pages/family-papers-20260603-2257-capture.md` (the renamed capture note).
3. Keep the visible newspaper text exactly as captured.
4. Keep uncertainty markers ("uncertain reading", "clipping continues", "cut off") rather than guessing missing words.
5. Do not copy the capture note's `## Allen resolutions` or `## Handwritten-note extrapolations to validate` sections — those are staging-only.

## Validation file

Create `sources/validations/gurney-family-papers-g3-to-g2-certificates-clippings.md`.

```markdown
# Source validation: Gurney family papers from G3 to G2

Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`

Patchset: `sources/intake/done/v83-gurney-family-papers-g3-to-g2-certificates-clippings.patchset.md`

## Source examined

Thirty scanned family-paper pages in `sources/intake/new/Family pages/`, `Scanned_20260603-2257-01.jpg` through `-30.jpg`, promoted to `sources/media/gurney-family-papers-g3-to-g2-certificates-clippings/`.

Source posture supplied by Allen: family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1).

## Method

Visual review of each scan. Certificates and administrative forms were read for pertinent facts; newspaper clippings and substantive correspondence were transcribed as completely as visible; cropped or taped material was marked rather than inferred.

## Findings

Promote. The batch adds certificate-level and near-primary documentation for G3, G4, G5, and several spouses. Substantive findings are recorded on the subject research companions and fact sheets (G3, G4, G5, Ethel, Edith, Helen, and a new Dorothy Hoben file); rich transcriptions are in the corpus supplement.

## Limits

- `Scanned_20260603-2257-02.jpg` has no substantive family text.
- Several newspaper clippings are cropped; only visible text was transcribed.
- The SAR chart is derivative and carries living-person G1 detail; private/source context only, and not a basis for changing G4's birth date.
- The 1900 "My dear Blanche" letter's "Blanche" / "Will" identities are unconfirmed; held as a hypothesis on the Helen research file.
```

---

# Research, fact-sheet, and data operations (literal)

Phase 2 applies each `str_replace` against the verbatim `old_string`. New footnote handles use final numeric IDs, not `NEW` placeholders.

## G3 fact sheet — `fact-sheets/g03-lester-sawyer-gurney-iii-fact-sheet.md`

### OP G3-FS-1 — subtitle

`str_replace`

old_string:
```
subtitle: "Wellesley Hills-born power engineer, wartime lieutenant, and father of Lester Hayes Gurney."
```
new_string:
```
subtitle: "Springfield-born, Wellesley Hills-raised power engineer, wartime Signal Corps officer in the Pacific, and father of Lester Hayes Gurney."
```

### OP G3-FS-2 — JSON-LD birthPlace and description

`str_replace`

old_string:
```
    "birthPlace": { "@type": "Place", "name": "Wellesley Hills, Massachusetts" },
    "description": "Power engineer and wartime lieutenant; husband of Edith Walberg Scott; father of Lester Hayes Gurney."
```
new_string:
```
    "birthPlace": { "@type": "Place", "name": "Springfield, Massachusetts" },
    "description": "Power engineer and wartime Signal Corps officer; husband of Edith Walberg Scott; father of Lester Hayes Gurney."
```

### OP G3-FS-3 — Born vital

`str_replace`

old_string:
```
    <div class="fact-value">10 June 1923, Wellesley Hills, Massachusetts. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```
new_string:
```
    <div class="fact-value">10 June 1923, Springfield, Massachusetts; raised in Wellesley Hills. <sup class="fn"><a href="#n1" id="ref-1">1</a></sup></div>
```

### OP G3-FS-4 — Education / Military vital

`str_replace`

old_string:
```
    <div class="fact-value">Norwich University class of 1945 before wartime service; lieutenant, commissioned June or July 1944, with family notes placing him in the Air Service Command at Robins Field, Georgia, and later at Manila with the 536th Signal Heavy Construction Company. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
```
new_string:
```
    <div class="fact-value">Norwich University civil-engineering cadet, September 1941 to March 1943, leaving in his junior year for the Army; commissioned a Signal Corps second lieutenant in November 1944; served as a first lieutenant with the 536th Signal Heavy Construction Company in the Western Pacific, separating in September 1946. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
```

### OP G3-FS-5 — Marriage vitals

`str_replace`

old_string:
```
        <div><strong>Edith Walberg Scott</strong> - married 23 November 1942, New York City. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
        <div><strong>Dorothy Lillian Haben/Haden</strong> - married 6 June 1965; surname uncertain in the handwritten note. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></div>
```
new_string:
```
        <div><strong>Edith Walberg Scott</strong> - married 23 November 1942, Manhattan, New York City. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
        <div><strong>Dorothy Lillian Hoben</strong> - married 26 June 1965, Elizabeth, New Jersey. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></div>
```

### OP G3-FS-6 — Highlights block

`str_replace`

old_string:
```
<ul>
  <li><strong>The wartime service clue is more specific than the older family reading.</strong> Dana Gurney's notes identify him as a lieutenant, commissioned in June or July 1944, serving with the Air Service Command at Robins Field, Georgia, when he married Edith, and later stationed at Manila with the 536th Signal Heavy Construction Company when his son Les was born. <sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></li>
  <li><strong>His marriage to Edith belongs in New York City in 1942.</strong> The family notes give the date as 23 November 1942, correcting the earlier ambiguous "11-42/43" reading. <sup class="fn"><a href="#n5" id="ref-5b">5</a></sup></li>
  <li><strong>He was absent overseas at the birth of G2.</strong> Lester Hayes Gurney was born 16 November 1945 at St. Vincent's Hospital in New York City while G3 was stationed at Manila. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>The engineering line runs through him.</strong> Family evidence remembers G3 as a McGraw Edison power engineer in New Jersey, between G4 Lester Sawyer Gurney Jr.'s civil-engineering career and G2 Lester Hayes Gurney's Indiana and Michigan Electric / AEP career. <sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
</ul>
```
new_string:
```
<ul>
  <li><strong>Born in Springfield, raised in Wellesley Hills.</strong> A Springfield city-clerk certificate records his birth on 10 June 1923 to Lester and Ethel (Hayes) Gurney; Wellesley Hills was the family home of his boyhood. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup></li>
  <li><strong>He ran telephone-line construction across liberated Luzon.</strong> As a Signal Corps outside-plant officer with the 536th Signal Heavy Construction Company, he directed the building and maintenance of aerial and underground telephone cable in the Philippines, supervising 75 enlisted men, Japanese prisoner-of-war labor, and 75 civilian linemen and cable splicers. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></li>
  <li><strong>He was absent overseas at the birth of G2.</strong> Lester Hayes Gurney was born 16 November 1945 at St. Vincent's Hospital in New York City while his father was serving in the Pacific. <sup class="fn"><a href="#n7" id="ref-7">7</a></sup></li>
  <li><strong>The engineering line ran straight through him.</strong> Before the war he laid out transmission lines and submarine cable as an assistant construction engineer for the New England Power Company in Boston — his own father's firm — and he went on to a long career as a power engineer with McGraw Edison in New Jersey. <sup class="fn"><a href="#n9" id="ref-9">9</a></sup><sup class="fn"><a href="#n4" id="ref-4b">4</a></sup></li>
  <li><strong>He carried the family's Masonic tradition into Rhode Island.</strong> By December 1955 he was junior deacon of St. Alban's Lodge No. 6 in Bristol, Rhode Island — one of the five generations of Gurney Freemasons remembered at his son's death. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></li>
</ul>
```

### OP G3-FS-7 — Narrative

`str_replace`

old_string:
```
<p>Lester Sawyer Gurney III stands at the hinge between the Massachusetts/New York engineering world of his father and the Indiana utility career of his son. Dana Gurney's family notes place his birth at Wellesley Hills, Massachusetts, on 10 June 1923 and identify him as having been Norwich University class of 1945 before wartime service. <sup class="fn"><a href="#n1" id="ref-1b">1</a></sup><sup class="fn"><a href="#n3" id="ref-3c">3</a></sup></p>

<p>The notes give his marriage to Edith Walberg Scott as 23 November 1942 in New York City. They also clarify his military setting: when he married Edith, he was serving with the Air Service Command at Robins Field, Georgia; he was later a lieutenant, commissioned in June or July 1944, and stationed at Manila with the 536th Signal Heavy Construction Company when Lester Hayes Gurney was born in New York City on 16 November 1945. <sup class="fn"><a href="#n5" id="ref-5c">5</a></sup><sup class="fn"><a href="#n3" id="ref-3d">3</a></sup><sup class="fn"><a href="#n7" id="ref-7c">7</a></sup></p>

<p>That service context revises an earlier family-note reading that had suggested "Marine." The stronger reading is Army / Army Air Forces / Signal Corps context: Air Service Command, Robins Field, Manila, and the 536th Signal Heavy Construction Company. Unless a separate Marine record appears, G3 should not be described as a Marine. <sup class="fn"><a href="#n8" id="ref-8">8</a></sup></p>

<p>After the war, G3 belongs to the family's twentieth-century engineering continuity. Family evidence remembers him as a power engineer with McGraw Edison in New Jersey, between his father Lester Sawyer Gurney Jr.'s civil-engineering work and his son Lester Hayes Gurney's later utility career at Indiana and Michigan Electric / AEP. <sup class="fn"><a href="#n4" id="ref-4c">4</a></sup></p>
```
new_string:
```
<p>Lester Sawyer Gurney III stands at the hinge between the Massachusetts and New York engineering world of his father and the Indiana utility career of his son. He was born in Springfield, Massachusetts, on 10 June 1923, the son of Lester and Ethel June (Hayes) Gurney, and grew up in the family home at Wellesley Hills. In September 1941 he entered Norwich University in Vermont as a civil-engineering cadet, completed two years in the upper third of his class, rose to Cadet Sergeant in the Signal Corps, and left in March 1943 — partway through his junior year — to enter the Army. <sup class="fn"><a href="#n1" id="ref-1c">1</a></sup><sup class="fn"><a href="#n3" id="ref-3b">3</a></sup></p>

<p>His war took him from a New Jersey training post to the far side of the Pacific. He served first as an enlisted man, training in very-high-frequency radio repair, then passed through Signal Corps Officer Candidate School at Fort Monmouth and was commissioned a second lieutenant in November 1944. As a first lieutenant and telephone-and-telegraph outside-plant officer with the 536th Signal Heavy Construction Company, Army Forces Western Pacific, he was responsible for the design, construction, and maintenance of aerial and underground telephone cable on Luzon, in the Philippines, directing a workforce of 75 enlisted men, Japanese prisoner-of-war labor, and 75 civilian linemen and cable splicers; before shipping overseas he had trained line crews at Fort Dix. He came home among his decorations the Asiatic-Pacific and Philippine Liberation ribbons, and separated from active service in September 1946. <sup class="fn"><a href="#n8" id="ref-8b">8</a></sup></p>

<p>Engineering framed the rest of his life. Even before the war, in 1942, he had worked as an assistant construction engineer for the New England Power Company in Boston — the very firm his father served for thirty-five years — laying out power-transmission lines and underground and submarine cable, work strikingly close to the military telephone construction he would later direct. He kept building on it afterward, earning top marks in electrical-machinery and circuits courses at Worcester Junior College's evening division in 1948, and family memory places the bulk of his career with McGraw Edison in New Jersey. He is thus the middle link in three generations of power engineers, between his father's New England Power career and his son's later work at Indiana and Michigan Electric. <sup class="fn"><a href="#n9" id="ref-9b">9</a></sup><sup class="fn"><a href="#n4" id="ref-4c">4</a></sup></p>

<p>For a stretch of the late 1940s and 1950s the family lived at Bristol, Rhode Island, on Sowams Road, where Lester and his first wife Edith were woven into village life: the couple were elected presidents of the Co-Mar-Co Society, Edith hosted the Bayberry Garden Club and chaired a Parent-Teacher Association school-registration drive, and Lester served as junior deacon of St. Alban's Lodge No. 6 — the Masonic thread that runs through five Gurney generations. He had married Edith Walberg Scott in Manhattan on 23 November 1942; after her death in 1963 he married Dorothy Lillian Hoben at Elizabeth, New Jersey, on 26 June 1965. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup><sup class="fn"><a href="#n5" id="ref-5b">5</a></sup><sup class="fn"><a href="#n6" id="ref-6b">6</a></sup></p>
```

### OP G3-FS-8 — Citations list

`str_replace` the entire citation list.

old_string:
```
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
```
new_string:
```
<ol class="citation-list">
  <li id="n1">Springfield, Massachusetts, City Clerk birth certification (issued 14 February 1929) recording Lester Gurney's birth at Springfield on 10 June 1923 to Lester and Ethel J. Hayes; Wellesley Hills childhood-home context from the Gurney family handwritten notes, Page 5 ("Born June 10, 1923 Wellesley Hills, MA"). Source IDs: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>; <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-1">Back</a></li>
  <li id="n2">Gurney family handwritten notes, Page 5 transcription: "Died Dec 19, 2011." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-2">Back</a></li>
  <li id="n3">Norwich University enrollment certificate and dean's recommendation letter (7 December 1943): entry September 1941, two years of Civil Engineering in the upper third of the class, promotion to Cadet Sergeant in the Signal Corps, departure 27 March 1943; Eastern Signal Corps Training Center temporary appointment as Second Lieutenant effective 25 November 1944 (Fort Monmouth); Army of the United States Certificate of Service, 536 Signal Heavy Construction Company, Army Forces Western Pacific, 25 November 1944 to 8 September 1946. Dana Gurney's family notes separately recall a June or July 1944 commission, kept as family memory. Source IDs: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>; <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-3">Back</a></li>
  <li id="n4">Gurney family handwritten notes, revised findings memorandum v3, recording Allen Gurney family evidence that G3 spent most of his career with McGraw Edison in New Jersey. Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-4">Back</a></li>
  <li id="n5">New York City certificate of marriage: Lester Gurney III and Edith W. Scott, married 23 November 1942 in the Borough of Manhattan before Justice Emil W. Haas, license no. 29487. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-5">Back</a></li>
  <li id="n6">Wedding invitation and marriage certificate: Lester Gurney III of Chatham, New Jersey, and Dorothy Lillian Hoben of Elizabeth, New Jersey, married 26 June 1965 at Westminster Presbyterian Church, Elizabeth (minister Robert W. Ross; witness Lester H. Gurney); a Gurney family handwritten note gives a variant 6 June 1965 and an uncertain Haben/Haden surname. Source IDs: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>; <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-6">Back</a></li>
  <li id="n7">Gurney family handwritten notes, Page 5 transcription: G3 was with the 536th Signal Heavy Construction Company "when Lester Hayes Gurney was born 11-16-45 / in NY City, St Vincent's Hospital." Source ID: <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-7">Back</a></li>
  <li id="n8">Army of the United States Separation Qualification Record for Lester Gurney III, 1st Lt., Telephone &amp; Telegraph Officer (Outside Plant): responsibility for design, construction, and maintenance of open-wire and cable telephone plant on Luzon, supervising 75 enlisted men, Japanese prisoner-of-war labor, and 75 civilian linemen and cable splicers, with line-construction training duty at Fort Dix before overseas service; decorations include the Asiatic-Pacific Theater Ribbon and Philippine Liberation Ribbon. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-8">Back</a></li>
  <li id="n9">Separation Qualification Record civilian-occupation entry recording Lester Gurney III as an assistant construction engineer with the New England Power Company, Boston (1942), responsible for layout and construction of transmission lines and underground and submarine cable; Worcester Junior College evening-division grade reports (terms ending 31 January and 11 June 1948) for electrical-machinery and circuits courses; McGraw Edison career from the Gurney family handwritten notes. Source IDs: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>; <code>gurney-family-handwritten-notes-1963</code>. <a class="citation-back" href="#ref-9">Back</a></li>
  <li id="n10">Bristol, Rhode Island, newspaper clipping, "Southwick Master of St. Alban's" (continuation annotated 16 December 1955), naming Lester Gurney III as junior deacon of St. Alban's Lodge No. 6, F. &amp; A.M., at the 153rd annual communication, Masonic Temple, Hope Street, Bristol; First Army discharge order (24 August 1951) giving his residence as Sowams Drive, Bristol. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-10">Back</a></li>
  <li id="n11">Bristol, Rhode Island, newspaper clippings: "Couples Elected to Club Offices" (Mr. and Mrs. Lester Gurney III elected president of the Co-Mar-Co Society), "Seedman Speaks to Bayb'ry Club" (Bayberry Garden Club meeting at the home of Mrs. Lester Gurney III on Sowams Road), and "Check on New Pupils Begins" (Mrs. Lester Gurney 3rd chairing the Parent-Teacher Association roundup committee). Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-11">Back</a></li>
</ol>
```

### OP G3-FS-9 — Timeline

`str_replace`

old_string:
```
      <tr><td>1923</td><td>Born 10 June at Wellesley Hills, Massachusetts.</td></tr>
      <tr><td>1942</td><td>Marries Edith Walberg Scott in New York City, 23 November.</td></tr>
      <tr><td>1944</td><td>Commissioned in June or July, according to Dana Gurney's notes.</td></tr>
      <tr><td>1945</td><td>Stationed at Manila with the 536th Signal Heavy Construction Company when son Lester Hayes Gurney is born in New York City.</td></tr>
      <tr><td>1965</td><td>Marries Dorothy Lillian Haben/Haden, 6 June, according to the family notes.</td></tr>
      <tr><td>2011</td><td>Dies 19 December.</td></tr>
```
new_string:
```
      <tr><td>1923</td><td>Born 10 June at Springfield, Massachusetts; raised in Wellesley Hills.</td></tr>
      <tr><td>1941</td><td>Enters Norwich University as a civil-engineering cadet.</td></tr>
      <tr><td>1942</td><td>Marries Edith Walberg Scott in Manhattan, 23 November.</td></tr>
      <tr><td>1944</td><td>Commissioned a Signal Corps second lieutenant, 25 November.</td></tr>
      <tr><td>1945</td><td>Serving in the Pacific with the 536th Signal Heavy Construction Company when son Lester Hayes Gurney is born in New York City.</td></tr>
      <tr><td>1946</td><td>Separates from active service, 8 September.</td></tr>
      <tr><td>1955</td><td>Junior deacon of St. Alban's Lodge No. 6, Bristol, Rhode Island.</td></tr>
      <tr><td>1965</td><td>Marries Dorothy Lillian Hoben at Elizabeth, New Jersey, 26 June.</td></tr>
      <tr><td>2011</td><td>Dies 19 December.</td></tr>
```

## G3 research companion — `research/people/g03-lester-sawyer-gurney-iii-fact-sheet.research.md`

### OP G3-R-1 — replace the opening working-note paragraph

`str_replace`

old_string:
```
Dana Gurney's later notes identify Lester Sawyer Gurney III as born 10 June 1923 at Wellesley Hills, Massachusetts, and deceased 19 December 2011. They state that he married Edith Walberg Scott on 23 November 1942 in New York City. When he married Edith, he was serving with the Air Service Command at Robins Field, Georgia, and had been Norwich University class of 1945. The notes further state that he was a lieutenant, commissioned in June or July 1944, and stationed at Manila with the 536th Signal Heavy Construction Company when Lester Hayes Gurney was born on 16 November 1945 at St. Vincent's Hospital in New York City. Family evidence supplied by Allen Gurney separately identifies Lester Sawyer Gurney III as a power engineer with a long McGraw Edison career in New Jersey.[^g03-notes]

The Page 5 marriage date should supersede the earlier ambiguous "11-[42/43]" reading on Page 4 unless the New York City marriage record proves otherwise. The Page 5 reading is fuller, specific to day/month/year, and fits the later military and G2 birth sequence better than an 11-43 date.[^g03-notes]

The earlier possible "Marine state side" reading should be downgraded. With Dana's notes, the better interpretation is Army / Army Air Forces / Signal Corps context: Air Service Command at Robins Field, a lieutenant's commission in June or July 1944, and service with the 536th Signal Heavy Construction Company at Manila. Unless separate Marine records are found, G3 should not be labeled as a Marine.[^g03-notes]
```
new_string:
```
A Springfield city-clerk certificate records Lester Sawyer Gurney III as born at Springfield, Massachusetts, on 10 June 1923, son of Lester and Ethel J. Hayes; Wellesley Hills was the family home of his childhood, preserved in family memory and in the address of the household's later papers. He died 19 December 2011.[^g03-family-papers][^g03-notes]

A Norwich University certificate and a dean's letter of 7 December 1943 record that he entered Norwich in September 1941 on a diploma from Gamaliel Bradford Senior High School, Wellesley Hills, completed two years of Civil Engineering in the upper third of his class, was promoted to Cadet Sergeant in the Signal Corps at the end of his sophomore year, and left on 27 March 1943 for military service.[^g03-family-papers]

The military papers carry the chronology in detail and supersede the family-note commission date. He served as an enlisted man from March 1943, training in very-high-frequency radio repair, was honorably discharged as a corporal at Fort Monmouth on 24 November 1944, and was temporarily appointed Second Lieutenant effective 25 November 1944 after Signal Corps Officer Candidate School. His Certificate of Service and Separation Qualification Record show active service as a first lieutenant from 25 November 1944 to 8 September 1946 with the 536 Signal Heavy Construction Company, Army Forces Western Pacific, as a telephone-and-telegraph outside-plant officer responsible for aerial and underground telephone cable on Luzon, supervising 75 enlisted men, Japanese prisoner-of-war labor, and 75 civilian linemen and cable splicers; before overseas duty he trained line crews at Fort Dix. Decorations included the American Campaign Medal, Asiatic-Pacific Theater Ribbon, Meritorious Service Unit Plaque, World War II Victory Medal, and Philippine Liberation Ribbon. Dana Gurney's note of a June or July 1944 commission likely points to the OCS milestone and is kept as secondary family memory; the earlier "Marine" reading is set aside in favor of this Signal Corps record.[^g03-family-papers][^g03-notes]

His Separation Qualification Record names his 1942 civilian job as assistant construction engineer with the New England Power Company, Boston — his father's firm — laying out transmission lines and underground and submarine cable. After the war he earned top grades in electrical-machinery and circuits courses at Worcester Junior College's evening division (1948); family evidence places the bulk of his career with McGraw Edison in New Jersey. He is the middle of three generations of power engineers between G4 and G2.[^g03-family-papers][^g03-notes]
```

### OP G3-R-2 — replace the Second marriage section

`str_replace`

old_string:
```
### Second marriage

Dana Gurney's Page 5 note records that Lester Sawyer Gurney III married Dorothy Lillian Haben or Haden on 6 June 1965. The event and date are strong enough to preserve; the surname requires confirmation from the marriage record before being treated as settled.[^g03-notes]
```
new_string:
```
### Bristol, Rhode Island, and St. Alban's Lodge

The family lived at Bristol, Rhode Island, on Sowams Road into the early 1950s (a 1951 First Army discharge order gives "Sowams Drive, Bristol"). A December 1955 Bristol clipping names Lester Gurney III as junior deacon of St. Alban's Lodge No. 6, F. & A.M., at the lodge's 153rd annual communication — documenting G3 as one of the five generations in the family Masonic line described in G2's obituary. Related Bristol clippings record the couple as elected presidents of the Co-Mar-Co Society and Edith hosting the Bayberry Garden Club and chairing a Parent-Teacher Association registration drive.[^g03-family-papers]

### Second marriage

A wedding invitation and marriage certificate establish that Lester Sawyer Gurney III married Dorothy Lillian Hoben at Westminster Presbyterian Church, Elizabeth, New Jersey, on 26 June 1965. Dana Gurney's note gave 6 June 1965 and an uncertain Haben/Haden surname; the printed record settles both. Dorothy's birth, death, and probate are on her own research file.[^g03-family-papers][^g03-notes]
```

### OP G3-R-3 — trim completed research actions

`str_replace`

old_string:
```
- Locate G3 birth record: Wellesley Hills, Massachusetts, 10 June 1923.
- Locate G3 and Edith Walberg Scott marriage record: New York City, 23 November 1942.
- Locate G3 military commission / personnel record.
- Search Robins Field / Air Service Command personnel context for late 1942.
- Search 536th Signal Heavy Construction Company and Manila assignment records.
- Search Norwich University class-of-1945 records.
- Locate McGraw Edison retirement or employment paperwork.
- Locate G3 and Dorothy Lillian Haben/Haden marriage record, 6 June 1965.
```
new_string:
```
- Locate G3 full military personnel file (NPRC) for the 536th Signal Heavy Construction Company service and Luzon assignment dates. (Unknown online.)
- Confirm or set aside the family-note Robins Field / Air Service Command detail, which the certificates do not corroborate. (Unknown online.)
- Locate McGraw Edison retirement or employment paperwork for the New Jersey career. (Unknown online.)
- Locate G3 death record, 19 December 2011, and place of death. (Unknown online.)
```

### OP G3-R-4 — add source and footnote to Sources Consulted

`str_replace`

old_string:
```
- Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages. Source ID: `gurney-family-handwritten-notes-1963`.

[^g03-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, especially Appendix A, Pages 4-5 and the G3 revised person-by-person findings. Source ID: `gurney-family-handwritten-notes-1963`.
```
new_string:
```
- Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages. Source ID: `gurney-family-handwritten-notes-1963`.
- Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); certificates, clippings, military papers, Masonic correspondence, and related family documents scanned 3 June 2026. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.

[^g03-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, especially Appendix A, Pages 4-5 and the G3 revised person-by-person findings. Source ID: `gurney-family-handwritten-notes-1963`.

[^g03-family-papers]: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); especially the Springfield birth certification, Norwich University certificate and dean's letter, Fort Monmouth temporary appointment, Certificate of Service and Separation Qualification Record (536 Signal Heavy Construction Company), Worcester Junior College grade reports, marriage certificates, and the December 1955 St. Alban's Lodge and Bristol social clippings. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.
```

## G4 fact sheet — `fact-sheets/g04-lester-sawyer-gurney-jr-fact-sheet.md`

### OP G4-FS-1 — Ethel marriage vital date

`str_replace`

old_string:
```
        <div><strong>Ethel June Hayes</strong> — married 26 April 1921 at Springfield, Hampden County, Massachusetts. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></div>
```
new_string:
```
        <div><strong>Ethel June Hayes</strong> — married 23 April 1921 at Springfield, Hampden County, Massachusetts. <sup class="fn"><a href="#n6" id="ref-6">6</a></sup></div>
```

### OP G4-FS-2 — Occupation vital

`str_replace`

old_string:
```
    <div class="fact-value">Civil engineer; documented in 1910 with Cape Cod Canal work, in 1911 with the Cape Cod Construction Company, and in later years in Massachusetts communities including Northfield and Wellesley Hills. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup></div>
```
new_string:
```
    <div class="fact-value">Civil engineer; on the Cape Cod Canal by 1910 and with the Cape Cod Construction Company in 1911, he spent some thirty-five years with the New England Power System, rising to Construction Manager before retiring in 1953 to open a Boston consulting office. <sup class="fn"><a href="#n3" id="ref-3">3</a></sup><sup class="fn"><a href="#n20" id="ref-20">20</a></sup></div>
```

### OP G4-FS-3 — Highlights: consolidate two early bullets and add the power-career bullet

`str_replace`

old_string:
```
  <li><strong>His 1911 record shows a civil engineer already in motion toward Cape Cod.</strong> The engagement notice said he had a position with the Cape Cod Construction Company and would live in Bourne, while the marriage affidavit calls him plainly a civil engineer from Patchogue. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></li>
  <li><strong>He advertised himself as more than a desk engineer.</strong> In Buzzards Bay he offered property surveys, municipal engineering, roads, sub-divisions, estimates, and architectural drafting from the Linnell Building opposite the railroad station. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup></li>
```
new_string:
```
  <li><strong>By 1911 he was a working Cape Cod engineer, not just a title on a tree.</strong> His engagement notice placed him with the Cape Cod Construction Company bound for Bourne, and a Cape Cod Magazine advertisement offered property surveys, municipal engineering, roads, sub-divisions, estimates, and architectural drafting from the Linnell Building in Buzzards Bay, opposite the railroad station. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup><sup class="fn"><a href="#n12" id="ref-12">12</a></sup></li>
  <li><strong>He spent thirty-five years building the New England power grid.</strong> From a 1906 start as a rodman on electric-railway work and chief-of-party on the Cape Cod Canal, he joined the New England Power System in 1918 and worked up to Construction Manager — resident engineer on hydroelectric developments at Searsburg, Harriman, Sherman, and Zoar and on generating plants at Salem and White River Junction — before retiring in 1953 to open his own Boston consulting practice. <sup class="fn"><a href="#n20" id="ref-20">20</a></sup></li>
```

### OP G4-FS-4 — Narrative: insert career paragraph before the Massachusetts-chapter paragraph

`str_replace`

old_string:
```
<p>Later records trace a steady Massachusetts chapter. FamilySearch places him in Northfield by 1920, in Wellesley by 1930, still there in 1940, and at 133 Abbott Road, Wellesley Hills, by 1942 and 1951.
```
new_string:
```
<p>Behind the Cape Cod beginnings lay a long career on the New England power grid. Gurney had entered construction in 1906 as a rodman and instrumentman on electric-railway work, rose within three years to chief-of-party on the Cape Cod Canal, and served as assistant engineer for the city of Springfield in 1917 before joining the New England Power System in 1918. Over the next thirty-five years he was assistant resident engineer on the Searsburg development and the Hoosac Tunnel railroad relocation, resident engineer for the Sherman development, a field surveyor for the Zoar development, and assistant to the chief engineer for the Bellows Falls and Comerford plants; by 1947 he had taken on the duties of Construction Manager of the New England Power Service Company, with the generating plants at Salem, Massachusetts, and White River Junction, Vermont, among the works of his tenure. A life member of the American Society of Civil Engineers, he retired on 1 June 1953 — feted with a luncheon and a pair of binoculars at the Engineers' Club — and at once opened a consulting construction-engineering office at 271 Dartmouth Street, Boston. An earlier chapter had closed in a Worcester courtroom in 1920, when he was granted a divorce from his first wife, Nettie, after she left to pursue a career on the stage. <sup class="fn"><a href="#n20" id="ref-20b">20</a></sup><sup class="fn"><a href="#n21" id="ref-21">21</a></sup></p>

<p>Later records trace a steady Massachusetts chapter. FamilySearch places him in Northfield by 1920, in Wellesley by 1930, still there in 1940, and at 133 Abbott Road, Wellesley Hills, by 1942 and 1951.
```

### OP G4-FS-5 — citation n6 (marriage certificate)

`str_replace`

old_string:
```
  <li id="n6">FamilySearch, <em>Lester Sawyer Gurney Jr.</em> (ID MB48-LHV), print view, marriage to Ethel June Hayes, 26 April 1921, Springfield, Massachusetts. <a class="citation-back" href="#ref-6">↩</a></li>
```
new_string:
```
  <li id="n6">Holy-matrimony certificate, Lester Gurney of Worcester and Ethel June Hayes of Springfield, married 23 April 1921 at Springfield, Massachusetts, witnesses Albert C. and Irving C. Hayes; a FamilySearch index entry (ID MB48-LHV) gives 26 April 1921. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-6">↩</a></li>
```

### OP G4-FS-6 — add citations n20 and n21

`str_replace`

old_string:
```
  <li id="n19">FamilySearch print view, residences in Northfield (1920), Wellesley (1930, 1935, 1940), and Wellesley Hills / 133 Abbott Road (1942, 1951); death in Bristol, Rhode Island. <a class="citation-back" href="#ref-19">↩</a></li>
</ol>
```
new_string:
```
  <li id="n19">FamilySearch print view, residences in Northfield (1920), Wellesley (1930, 1935, 1940), and Wellesley Hills / 133 Abbott Road (1942, 1951); death in Bristol, Rhode Island. <a class="citation-back" href="#ref-19">↩</a></li>
  <li id="n20"><em>New England Construction Magazine</em>, "Opens Private Office" (15 June 1953), and the Boston "Contact" column "Lester Gurney Retires" by Clifford A. Needham, recounting his career from 1906 electric-railway work and Cape Cod Canal chief-of-party through thirty-five years with the New England Power System — Searsburg, Harriman, Sherman, Zoar, Bellows Falls, Comerford, Salem, and White River Junction — to Construction Manager, retirement on 1 June 1953, and a new consulting office at 271 Dartmouth Street, Boston. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-20">↩</a></li>
  <li id="n21"><em>Worcester Daily Telegram</em> (Worcester, Mass.), 12 October 1920, "Wife Seeks Career, Husband Gets Divorce," reporting Lester Gurney's decree nisi of divorce from Nettie L. Gurney on the ground of desertion. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-21">↩</a></li>
</ol>
```

### OP G4-FS-7 — Timeline: add 1918 and 1953 rows

`str_replace`

old_string:
```
      <tr><td>1915</td><td>Advertises engineering and drafting services in Buzzards Bay opposite the railroad station.</td></tr>
      <tr><td>1920–1951</td><td>Lives in Northfield and then Wellesley / Wellesley Hills, including 133 Abbott Road.</td></tr>
```
new_string:
```
      <tr><td>1915</td><td>Advertises engineering and drafting services in Buzzards Bay opposite the railroad station.</td></tr>
      <tr><td>1918</td><td>Joins the New England Power System.</td></tr>
      <tr><td>1920–1951</td><td>Lives in Northfield and then Wellesley / Wellesley Hills, including 133 Abbott Road.</td></tr>
      <tr><td>1953</td><td>Retires as Construction Manager of the New England Power Service Company; opens a Boston consulting office.</td></tr>
```

## G4 research companion — `research/people/g04-lester-sawyer-gurney-jr-fact-sheet.research.md`

### OP G4-R-1 — replace the Ethel marriage-date note

`str_replace`

old_string:
```
The same Dana note gives his marriage to Ethel June Hayes as 23 April 1921 at Springfield, Massachusetts, with "see marriage certif." The current project date is 26 April 1921. The difference may be a license date, certificate date, ceremony date, transcription error, or family-note error; resolve from the original marriage certificate/register before changing the fact sheet.[^g04-family-notes]

Earlier loose notes add that the relevant Gurney man was a civil engineer for "N.E. Elect. Syst[em]" and a construction manager. Given the existing G4 civil-engineering profile, this is best treated as a G4 lead rather than a settled employment claim. Search New England Electric System, Cape Cod / Massachusetts engineering directories, and Long Island Rail Road electrification context before promoting it.[^g04-family-notes]
```
new_string:
```
The holy-matrimony certificate confirms the marriage to Ethel June Hayes as 23 April 1921 at Springfield, Massachusetts — Lester Gurney of Worcester and Ethel June Hayes of Springfield, witnesses Albert C. and Irving C. Hayes — settling the date in favor of Dana's note over the 26 April 1921 FamilySearch index value, which is best treated as a derived or index date.[^g04-family-papers]

Dana's loose note that the Gurney man was a civil engineer for "N.E. Elect. Syst[em]" and a construction manager is now documented. Two 1953 trade clippings (New England Construction Magazine and the Boston "Contact" column) record Lester Gurney's thirty-five-year career with the New England Power System: a 1906 start as rodman and instrumentman on electric-railway work, chief-of-party on the Cape Cod Canal within three years, assistant engineer for the city of Springfield in 1917, joining the System in July 1918, then assistant resident engineer on the Searsburg development and Hoosac Tunnel relocation, resident engineer for the Sherman development, field surveyor for the Zoar development, assistant to the chief engineer (from August 1927) on the Bellows Falls and Comerford plants, executive assistant in April 1945, and Construction Manager of the New England Power Service Company from January 1947 until retirement on 1 June 1953, when he opened a consulting office at 271 Dartmouth Street, Boston. The generating plants at Salem, Massachusetts, and White River Junction, Vermont, are named among his works; he was a life member of the American Society of Civil Engineers. This documents the third-generation power-engineering line: G4 at New England Power, G3 at New England Power before the war, and G2 at Indiana and Michigan Electric.[^g04-family-papers]

### Nettie Levada Smith divorce

A Worcester Daily Telegram clipping of 12 October 1920 ("Wife Seeks Career, Husband Gets Divorce") reports that Lester Gurney of Worcester, a civil engineer employed by the New England Power Co., received a decree nisi of divorce from Nettie L. Gurney on the ground of desertion. He testified that she left in March 1917 after disagreements over her wish to study dramatic art and seek a career as an elocutionist. A compact life-context note, not a centerpiece of the public narrative.[^g04-family-papers]
```

### OP G4-R-2 — add the family-papers footnote

`str_replace`

old_string:
```
[^g04-family-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 3-4 and Page 6 transcription in Dana Gurney's hand. Source ID: `gurney-family-handwritten-notes-1963`.
```
new_string:
```
[^g04-family-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 3-4 and Page 6 transcription in Dana Gurney's hand. Source ID: `gurney-family-handwritten-notes-1963`.

[^g04-family-papers]: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); especially the 23 April 1921 Lester Gurney / Ethel June Hayes marriage certificate, the 12 October 1920 Worcester Daily Telegram divorce clipping, and the 1953 New England Power Service Company retirement clippings. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.
```

## G5 fact sheet — `fact-sheets/g05-lester-sawyer-gurney-fact-sheet.md`

### OP G5-FS-1 — Marriage vital names the certificate form

`str_replace`

old_string:
```
        <div><strong>Helen Hill / Helene Ransome</strong> — married 21 November 1881 in Manhattan. The surviving record indicates that Helen Hill and the actress Helene Ransome were the same woman, with “Helen Ransome” named as the mother of Lester Sawyer Gurney Jr. on the 1911 marriage affidavit. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```
new_string:
```
        <div><strong>Helen Ransome Hill</strong> — married 21 November 1881 at the Church of the Transfiguration, Manhattan. The marriage certificate names her Helen Ransome Hill; she was the actress known on stage as Helene Ransome, and “Helen Ransome” is named as the mother of Lester Sawyer Gurney Jr. on the 1911 marriage affidavit. <sup class="fn"><a href="#n5" id="ref-5">5</a></sup></div>
```

### OP G5-FS-2 — citation n5

`str_replace`

old_string:
```
  <li id="n5">FamilySearch, <em>Lester Sawyer Gurney</em> (ID 9ZML-HC9), print view, marriage to Helen Hill on 21 November 1881 in Manhattan; New York State affidavit for the marriage of Lester Gurney and Nettie Levada Smith, Hempstead, Nassau County, 7 April 1911, naming the groom’s mother as Helen Ransome. <a class="citation-back" href="#ref-5">↩</a></li>
```
new_string:
```
  <li id="n5">Marriage certificate, Lester Sawyer Gurney and Helen Ransome Hill, joined 21 November 1881 at the Church of the Transfiguration, New York City, by the Rev. George H. Houghton (certificate signed 31 January 1882); New York State affidavit for the marriage of Lester Gurney and Nettie Levada Smith, Hempstead, Nassau County, 7 April 1911, naming the groom’s mother as Helen Ransome; FamilySearch, <em>Lester Sawyer Gurney</em> (ID 9ZML-HC9), print view. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-5">↩</a></li>
```

### OP G5-FS-3 — citation n10 adds the 1936 lodge-history corroboration

`str_replace`

old_string:
```
  <li id="n10"><em>Brooklyn Daily Eagle</em>, 28 October 1899, p. 6; <a href="https://genealogy.allengurney.com/key-research/brigadier-general-william-gurney.html">Brigadier General William Gurney</a>, Gurney Genealogy Library, lodge-history discussion identifying William Gurney as principal organizer and “Father” of Continental Lodge No. 287. <a class="citation-back" href="#ref-10">↩</a></li>
```
new_string:
```
  <li id="n10"><em>Brooklyn Daily Eagle</em>, 28 October 1899, p. 6; <a href="https://genealogy.allengurney.com/key-research/brigadier-general-william-gurney.html">Brigadier General William Gurney</a>, Gurney Genealogy Library, lodge-history discussion identifying William Gurney as principal organizer and “Father” of Continental Lodge No. 287; Third Masonic District Association letter to Helen O’Brien, 19 March 1936, stating that Lester Gurney was Master of Continental Lodge No. 287 in 1891-92 and that his father General William Gurney organized the lodge in 1853 and held a District Deputy Grand Master commission in 1858. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-10">↩</a></li>
```

### OP G5-FS-4 — narrative closing sentence on the 1936 lodge-history request

`str_replace`

old_string:
```
Lester’s career therefore joined several of the family’s strongest recurrent themes — New York public life, theater, organized benevolence, summering on Long Island, and Freemasonry — in a single compact but unusually human record. <sup class="fn"><a href="#n17" id="ref-17">17</a></sup></p>
```
new_string:
```
Lester’s career therefore joined several of the family’s strongest recurrent themes — New York public life, theater, organized benevolence, summering on Long Island, and Freemasonry — in a single compact but unusually human record. <sup class="fn"><a href="#n17" id="ref-17">17</a></sup> As late as 1936, the Third Masonic District Association — then compiling a history of Continental Lodge — wrote to his widow Helen, by then living in Newton, Massachusetts, seeking a photograph of him for the lodge’s records. <sup class="fn"><a href="#n18" id="ref-18">18</a></sup></p>
```

### OP G5-FS-5 — add citation n18

`str_replace`

old_string:
```
  <li id="n17"><em>Brooklyn Daily Eagle</em>, 28 October 1899, p. 6; <a href="https://genealogy.allengurney.com/key-research/brigadier-general-william-gurney.html">Brigadier General William Gurney</a>, Gurney Genealogy Library. <a class="citation-back" href="#ref-17">↩</a></li>
</ol>
```
new_string:
```
  <li id="n17"><em>Brooklyn Daily Eagle</em>, 28 October 1899, p. 6; <a href="https://genealogy.allengurney.com/key-research/brigadier-general-william-gurney.html">Brigadier General William Gurney</a>, Gurney Genealogy Library. <a class="citation-back" href="#ref-17">↩</a></li>
  <li id="n18">Third Masonic District Association of Manhattan letter from Francis J. Arkins to Mrs. Helen O’Brien, 17 Braemore Road, Newton, Massachusetts, 19 March 1936, requesting a photograph of the late Lester Gurney, Master of Continental Lodge No. 287 in 1891-92, for a history of the lodge. Source ID: <code>gurney-family-papers-g3-to-g2-certificates-clippings</code>. <a class="citation-back" href="#ref-18">↩</a></li>
</ol>
```

## G5 research companion — `research/people/g05-lester-sawyer-gurney-fact-sheet.research.md`

### OP G5-R-1 — add certificate-level support after the Helen identity paragraph

`str_replace`

old_string:
```
The same notes strongly support the identity chain Helen Hill / Helene Ransome / Helen Gurney / Helen O'Brien. Page 7 gives "Helen Ransome Hill," describes her as a Broadway star in the 1890s and again 1906-1910, and states that she married Lawrence Branch O'Brien on 12 April 1900. Page 4 frames the sequence as Helen Hill as maiden name, Gurney as married name after which "he died early," and O'Brien as a second marriage. This makes Helen O'Brien probably identical with Helen Hill / Helene Ransome / Helen Gurney, pending formal proof from marriage and census records.[^g05-family-notes]
```
new_string:
```
The same notes strongly support the identity chain Helen Hill / Helene Ransome / Helen Gurney / Helen O'Brien. Page 7 gives "Helen Ransome Hill," describes her as a Broadway star in the 1890s and again 1906-1910, and states that she married Lawrence Branch O'Brien on 12 April 1900. Page 4 frames the sequence as Helen Hill as maiden name, Gurney as married name after which "he died early," and O'Brien as a second marriage. This makes Helen O'Brien probably identical with Helen Hill / Helene Ransome / Helen Gurney, pending formal proof from marriage and census records.[^g05-family-notes]

Two marriage certificates now anchor the identity chain at certificate level. A certificate from the Church of the Transfiguration, New York City, records Lester Sawyer Gurney's marriage to Helen Ransome Hill on 21 November 1881; a second records Lawrence Branch O'Brien's marriage to Helen Ransome Gurney on 12 April 1900. A 1936 Third Masonic District Association letter, addressed to Mrs. Helen O'Brien at 17 Braemore Road, Newton, Massachusetts, sought a photograph of the late Lester Gurney for a history of Continental Lodge — independently confirming Lester as Master of Continental Lodge No. 287 in 1891-92 and his father General William Gurney as the lodge's 1853 organizer and an 1858 District Deputy Grand Master, and placing Helen, alive and answering correspondence, in suburban Boston in 1936.[^g05-family-papers]
```

### OP G5-R-2 — add the family-papers footnote

`str_replace`

old_string:
```
[^g05-family-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 4 and 7. Source ID: `gurney-family-handwritten-notes-1963`.
```
new_string:
```
[^g05-family-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 4 and 7. Source ID: `gurney-family-handwritten-notes-1963`.

[^g05-family-papers]: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); especially the 1881 Lester Sawyer Gurney / Helen Ransome Hill marriage certificate, the 1900 Lawrence Branch O'Brien / Helen Ransome Gurney marriage certificate, and the 19 March 1936 Third Masonic District Association letter to Helen O'Brien. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.
```

## G2 research companion — `research/people/g02-lester-hayes-gurney-fact-sheet.research.md`

### OP G2-R-1 — close the three-generation power-engineer question

`str_replace`

old_string:
```
The obituary's "third-generation power engineer" claim is genealogically significant. It implies that both G3 (Lester Sawyer Gurney III, 1923–2011) and G4 (Lester Sawyer Gurney Jr., 1888–1958) also worked for in the same lineage of mid-Atlantic / midwestern power-engineering practice. G4's published fact sheet records him as a civil engineer working the Cape Cod Canal and Cape Cod Construction Company before settling in Massachusetts, with later residences in Northfield, Wellesley, and Wellesley Hills.
```
new_string:
```
The obituary's "third-generation power engineer" claim is now documented at all three links. G4 (Lester Sawyer Gurney Jr., 1888–1958) spent some thirty-five years with the New England Power System, rising to Construction Manager before retiring in 1953 (1953 trade clippings). G3 (Lester Sawyer Gurney III, 1923–2011) was an assistant construction engineer for the New England Power Company in Boston in 1942 (his wartime Separation Qualification Record) before a later New Jersey career remembered as McGraw Edison. G2 worked for Indiana and Michigan Electric. The three generations therefore run New England Power (G4, G3) into Indiana and Michigan Electric (G2).
```

### OP G2-R-2 — update the five-generation Masonic line

`str_replace`

old_string:
```
- **G2** Lester Hayes Gurney — Master Mason, McCulloch Lodge No. 737, Marion, IN; Scottish Rite; Salaam Shriners (FairHaven obituary).

That accounts for three of the five generations. The remaining two are presumably G3 and G4. Pursuing Masonic-lodge records in Massachusetts (G4) and the New York / Indiana corridor (G3) would close the chain.
```
new_string:
```
- **G3** Lester Sawyer Gurney III — junior deacon, St. Alban's Lodge No. 6, F. & A.M., Bristol, Rhode Island, December 1955 (2026 Gurney family-papers clipping).
- **G2** Lester Hayes Gurney — Master Mason, McCulloch Lodge No. 737, Marion, IN; Scottish Rite; Salaam Shriners (FairHaven obituary).

That accounts for four of the five generations. The remaining likely missing link is G4, probably in a Massachusetts lodge during the Wellesley / Wellesley Hills years.
```

### OP G2-R-3 — narrow Open Question 1

`str_replace`

old_string:
```
1. **The remaining two Masonic generations.** Is G3 documented at any specific lodge? Is G4 documented in any Massachusetts lodge during the Wellesley / Wellesley Hills years? Worth searching the *List of Lodges Masonic* annuals for the relevant years.
```
new_string:
```
1. **The remaining Masonic generation.** G3 is now documented as junior deacon of St. Alban's Lodge No. 6, Bristol, Rhode Island (December 1955). Is G4 documented in any Massachusetts lodge during the Wellesley / Wellesley Hills years? Worth searching the *List of Lodges Masonic* annuals for the relevant years.
```

## Ethel research — `research/people/ethel-june-hayes.md`

### OP ETHEL-R-1 — add certificate and vitals support

`str_replace`

old_string:
```
Earlier loose notes say Ethel's father died when she was about 20 and mention "Aunt C. Hayes" with "RR" and "sister." Preserve these as clues, but resolve them against census, death, obituary, and railroad employment records before using them as settled family structure.[^ethel-notes]
```
new_string:
```
Earlier loose notes say Ethel's father died when she was about 20 and mention "Aunt C. Hayes" with "RR" and "sister." Preserve these as clues, but resolve them against census, death, obituary, and railroad employment records before using them as settled family structure.[^ethel-notes]

The 1921 marriage certificate confirms the marriage to Lester Gurney on 23 April 1921 at Springfield, Massachusetts, and names Albert C. Hayes and Irving C. Hayes as witnesses — useful leads to Ethel's father and a likely brother. A SAR ancestor chart gives Ethel's birth as 10 February 1880 at Springfield and her death as 19 October 1951 at Wellesley Hills; a Brown & Son (Wellesley) funeral-directors statement for the funeral of Ethel J. Gurney, dated 1 November 1951 and addressed to Lester Gurney at 133 Abbott Road, Wellesley Hills, corroborates the death in autumn 1951. Treat the chart's exact dates as derivative pending a death record.[^ethel-family-papers]
```

### OP ETHEL-R-2 — add footnote

`str_replace`

old_string:
```
[^ethel-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 2 and 6. Source ID: `gurney-family-handwritten-notes-1963`.
```
new_string:
```
[^ethel-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 2 and 6. Source ID: `gurney-family-handwritten-notes-1963`.

[^ethel-family-papers]: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); especially the 23 April 1921 marriage certificate, the SAR ancestor chart, and the November 1951 Brown & Son funeral statement. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.
```

## Edith research — `research/people/edith-walberg-scott-gurney.md`

### OP EDITH-R-1 — add certificate-level marriage and Bristol community life

`str_replace`

old_string:
```
The earlier "died 82 years old" note probably does not refer to Edith. Page 8 gives Edith's death in 1963 at about age 42-43 if she was born in 1920-1921.[^edith-notes]
```
new_string:
```
The earlier "died 82 years old" note probably does not refer to Edith. Page 8 gives Edith's death in 1963 at about age 42-43 if she was born in 1920-1921.[^edith-notes]

A New York City certificate of marriage confirms that Edith W. Scott married Lester Gurney III on 23 November 1942 in the Borough of Manhattan, before Justice Emil W. Haas, license no. 29487. A SAR ancestor chart gives her birth as 15 February 1919 at New York and death as 27 December 1963 at Chatham, New Jersey — the 1919 birth would make her about three years older than the 1920-1921 estimate from the family notes; treat it as a derivative variant pending a birth record. Mid-1950s Bristol, Rhode Island, clippings show "Mrs. Lester Gurney 3rd" — Edith — active in village life: chairing the Bristol Parent-Teacher Association roundup committee, hosting the Bayberry Garden Club at the family home on Sowams Road, and, with Lester, elected president of the Co-Mar-Co Society.[^edith-family-papers]
```

### OP EDITH-R-2 — add footnote

`str_replace`

old_string:
```
[^edith-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 1, 5, and 8. Source ID: `gurney-family-handwritten-notes-1963`.
```
new_string:
```
[^edith-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 1, 5, and 8. Source ID: `gurney-family-handwritten-notes-1963`.

[^edith-family-papers]: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); especially the 23 November 1942 New York City marriage certificate, the SAR ancestor chart, and the mid-1950s Bristol, Rhode Island, social clippings. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.
```

## Helen research — `research/people/helen-hill-helene-ransome-gurney-obrien.md`

### OP HELEN-R-1 — add certificate support and the 1900 letter (with the open identity question)

`str_replace`

old_string:
```
Dana's notes identify Helen's later husband as Lawrence Branch O'Brien, married 12 April 1900, and state that Branch died 12 April 1922. These dates should be used to locate marriage and death records that can prove the Helen Hill / Ransome / Gurney / O'Brien identity chain.[^helen-notes]
```
new_string:
```
Dana's notes identify Helen's later husband as Lawrence Branch O'Brien, married 12 April 1900, and state that Branch died 12 April 1922. These dates should be used to locate marriage and death records that can prove the Helen Hill / Ransome / Gurney / O'Brien identity chain.[^helen-notes]

Two marriage certificates now anchor the chain. One records Lester Sawyer Gurney's marriage to Helen Ransome Hill on 21 November 1881 at the Church of the Transfiguration, New York City; the other records Lawrence Branch O'Brien's marriage to Helen Ransome Gurney on 12 April 1900 at New York City. Together with the 1911 affidavit naming G4's mother as Helen Ransome, they support one woman moving through maiden, professional, and married names. A 1936 Masonic letter addressed to Mrs. Helen O'Brien at 17 Braemore Road, Newton, Massachusetts, shows her alive and answering correspondence there.[^helen-family-papers]

### The 1900 "My dear Blanche" letter — open identity question

A handwritten letter on Jandus Filter Co. letterhead, dated Paris, 8 May 1900, congratulates its recipient on a recent marriage and closes "Dear Mrs. O'Brien, accept from me the sincerest wishes for your happiness"; it is addressed "My dear Blanche" and signed "Lovingly yours, Will." Because the only O'Brien marriage in the family papers is Helen Ransome Gurney's to Lawrence Branch O'Brien on 12 April 1900, the recipient is almost certainly Helen, here called "Blanche" — apparently a familiar or pet name. The writer "Will" speaks of "Willie" in the third person (so they are different men) and recalls hearing the recipient's opinion of "Willie" "eight years ago on the island" (≈1892, plausibly the Patchogue / Long Island summer world); "after two Gurneys deaths" fits the 1899 death of G5. **Open for Allen:** confirm whether "Blanche" was a known name for Helen, and identify "Will" (a Gurney relative, an O'Brien connection, or a family friend abroad). Until confirmed, this stays here as a transcription and hypothesis and is not stated in any fact sheet. Full transcription is in the corpus supplement.[^helen-family-papers]
```

### OP HELEN-R-2 — add footnote

`str_replace`

old_string:
```
[^helen-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 2, 4, and 7. Source ID: `gurney-family-handwritten-notes-1963`.
```
new_string:
```
[^helen-notes]: Gurney family handwritten oral-history and research notes, revised findings memorandum v3 prepared 4 May 2026 from eight photographed notebook pages, Appendix A, Pages 2, 4, and 7. Source ID: `gurney-family-handwritten-notes-1963`.

[^helen-family-papers]: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); especially the 1881 Lester Sawyer Gurney / Helen Ransome Hill marriage certificate, the 1900 Lawrence Branch O'Brien / Helen Ransome Gurney marriage certificate, the 1936 Third Masonic District Association letter, and the 8 May 1900 "My dear Blanche" letter. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.
```

## Dorothy research note — create `research/people/dorothy-lillian-hoben-gurney.md`

No existing Dorothy file (confirmed by glob). `new file write`:

```markdown
# Dorothy Lillian Hoben Gurney

Working research file for Dorothy Lillian Hoben, later Dorothy L. Gurney, second wife of Lester Sawyer Gurney III (G3).

---

## Working Notes

### Birth, marriage, death, and probate

A New York State birth certification names her Dorothy Lillian Hoben, born 20 February 1928 at New Rochelle, Westchester County, New York, filed 24 February 1928. A wedding invitation from Doctor and Mrs. D. Carl Gerardo and a marriage certificate record her marriage to Lester Gurney III of Chatham, New Jersey, at Westminster Presbyterian Church, Elizabeth, New Jersey, on 26 June 1965 (minister Robert W. Ross; witnesses Jane L. Ross and Lester H. Gurney). Dana Gurney's older family note gave 6 June 1965 and an uncertain Haben/Haden surname; the printed papers settle both.

Dorothy died 25 December 1994 at Morristown Memorial Hospital, Morristown, New Jersey. Her death certificate gives her residence as 540 Main Street, Apt. 3A, Chatham Borough, Morris County; surviving spouse and informant Lester Gurney III; occupation Secretary to the President in electrical manufacturing; last employer MultiAmp Corp., Cranford, New Jersey; father "(unknown) Hoben"; mother Frances Coy; disposition cremation at Somerset Hills Crematory, Bernards Township. The Morris County Surrogate's Court admitted her will and codicil to probate on 24 January 1995 and issued letters testamentary to Lester Gurney III as executor.[^dorothy-family-papers]

## Sources Consulted

- Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); certificates, clippings, military papers, Masonic correspondence, and related family documents scanned 3 June 2026. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.

[^dorothy-family-papers]: Gurney family papers from Lester Sawyer Gurney III (G3), passed to Lester Hayes Gurney (G2), in possession of Allen Gurney (G1); especially Dorothy Lillian Hoben's birth certification, wedding invitation, marriage certificate, New Jersey death certificate, and Morris County probate certificate. Source ID: `gurney-family-papers-g3-to-g2-certificates-clippings`.
```

## Data — `data/ancestors.json` (G3 entry only)

### OP DATA-1 — geography

`str_replace`

old_string:
```
    "geography": "Wellesley Hills, MA; New York City; Robins Field, GA; Manila; New Jersey",
```
new_string:
```
    "geography": "Springfield, MA; Wellesley Hills, MA; New York City; Fort Monmouth, NJ; Luzon, Philippines; Bristol, RI; New Jersey",
```

### OP DATA-2 — summary

`str_replace`

old_string:
```
    "summary": "Wellesley Hills-born power engineer and wartime Army/Air Service Command officer; father of Lester Hayes Gurney (G2). Family notes place him with the Air Service Command at Robins Field when he married Edith Walberg Scott and with the 536th Signal Heavy Construction Company at Manila when G2 was born.",
```
new_string:
```
    "summary": "Springfield-born, Wellesley Hills-raised power engineer and wartime Signal Corps officer; father of Lester Hayes Gurney (G2). A Norwich University civil-engineering cadet, he was commissioned in the Signal Corps in 1944 and served as a first lieutenant with the 536th Signal Heavy Construction Company in the Western Pacific, directing telephone-line construction on Luzon, before a long power-engineering career.",
```

### OP DATA-3 — notables

`str_replace`

old_string:
```
    "notables": "Born 10 June 1923 at Wellesley Hills, Massachusetts; died 19 December 2011. Married Edith Walberg Scott on 23 November 1942 in New York City; later married Dorothy Lillian Haben/Haden on 6 June 1965. Dana Gurney's notes identify him as a lieutenant, commissioned June or July 1944, formerly Norwich University class of 1945, and stationed at Manila with the 536th Signal Heavy Construction Company when Lester Hayes Gurney was born at St. Vincent's Hospital, New York City, on 16 November 1945. Family evidence also remembers his long McGraw Edison power-engineering career in New Jersey.",
```
new_string:
```
    "notables": "Born 10 June 1923 at Springfield, Massachusetts (city-clerk certificate), raised in Wellesley Hills; died 19 December 2011. A Norwich University civil-engineering cadet (1941-1943), he was commissioned a Signal Corps second lieutenant on 25 November 1944 and served as a first lieutenant and outside-plant officer with the 536th Signal Heavy Construction Company, Army Forces Western Pacific, directing telephone-line construction on Luzon and supervising 75 enlisted men, prisoner-of-war labor, and 75 civilian linemen before separating in 1946. Before the war he was an assistant construction engineer for the New England Power Company in Boston; family evidence remembers a long later career with McGraw Edison in New Jersey. Junior deacon of St. Alban's Lodge No. 6, Bristol, Rhode Island, in 1955. Married Edith Walberg Scott on 23 November 1942 in Manhattan and Dorothy Lillian Hoben on 26 June 1965 at Elizabeth, New Jersey.",
```

### OP DATA-4 — spouse 2

`str_replace`

old_string:
```
        "name": "Dorothy Lillian Haben/Haden",
        "dates": "m. 6 June 1965",
        "notes": "Surname uncertain in family notes; verify by marriage record"
```
new_string:
```
        "name": "Dorothy Lillian Hoben",
        "dates": "m. 26 June 1965, Elizabeth, New Jersey; d. 25 December 1994, Morristown, New Jersey",
        "notes": "Marriage certificate and invitation establish surname and date; a family note gives a variant 6 June 1965."
```

## Data / source hygiene

- Do not publish G1 details from the SAR chart.
- Do not use the SAR chart alone to change G4's birth date; preserve it as a derivative variant on the G4 companion.
- Certificates and military documents are primary for G3 commission chronology and marriage dates; cite the older family notes only for variant memory and context.
- Keep corpus-supplement file paths pointed at the promoted media directory once media are copied.

## After Phase 2 apply

Run from `site/website`:

```powershell
npm.cmd run validate
npm.cmd run package
```

Then from repo root:

```powershell
git diff --check
```

Footnote sweep before validation: confirm no `NEW` handles remain, every `href="#n..."` / `id="ref-..."` anchor resolves (G3 n1-n11; G4 through n21; G5 through n18), IDs are unique, and Narrative/Children sections retain nearby citation coverage.
