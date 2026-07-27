# East Dereham PD 86/41 — deviation audit of the March–May 2026 analysis

> **STATUS 2026-07-26 — read this box first.**
>
> **The finding.** The March 2026 "John the sonne of ffrancis Gurnie" baptism — the case file's
> "strongest single anchor" for Candidate B — **does not exist.** The analysis adjudicated a
> letterform on page 00722, in a line that reads *"Amorye the daughter of Robart Enderby, Ianuarij
> 10."* The record the FindMyPast index actually describes is on page 00726 and reads **"John the
> sonne off Nicholas Horne bapt — Janua 10"** (10 January 1617). The index was right; the re-reading
> was wrong.
>
> **The scale.** Ten deviations (D1–D10), eight root causes (R1–R8). No repo edits have been made to
> `research/`, the case file, or the public procedure page — all of which still publish the
> disproven reading at ~65% confidence. **That is the outstanding action.**
>
> **What survived re-testing:** the 1611 Gurney–Rybett marriage (re-read and confirmed), Edward's
> 1610 baptism (now *upgraded* to D-class by an in-parchment heading), Marye 1618, and the
> Agnes/"Susan" and Marye-relationship refutations.
>
> **Current probabilities:** Candidate B **22%** (was ~65%). No option exceeds 22%. See §Probability.

## Navigation

| § | Section | What it holds |
|---|---|---|
| 1 | [Summary](#summary) | The one-paragraph version |
| 2 | [D1–D8 — the deviations](#d1--the-canonical-crop-is-from-00722-and-it-is-not-the-john-entry-confirmed) | Numbered, evidenced errors in the March–May work |
| 3 | [D9–D10](#two-further-deviations-surfaced-by-the-crawl-2026-07-22) | The 1611–1615 register gap; the "Prudy" burials |
| 4 | [Root-cause chain R1–R8](#root-cause-chain) | *Why* it happened — the reusable lesson |
| 5 | [Marriage re-read](#the-margaret-rybett-marriage--re-read-and-confirmed-2026-07-22) | Gurney–Rybett 1611, CONFIRMED |
| 6 | [Parish crawl](#parish-register-crawl-for-a-john-gurney-baptism-2026-07-22) | Coverage ledger; no John Gurney baptism exists |
| 7 | [Candidate elimination audit](#elimination-audit-of-candidates-a-c-d-e--how-complete-is-each) | A, C, D, "E" — which eliminations are inferred |
| 8 | [Iterations 2–3](#iteration-2--corrections-to-my-own-reassessment-after-reading-the-g13-topic-units) | Self-corrections; apprenticeship constraint; masking effect |
| 9 | [New evidence 2026-07-26](#new-evidence-2026-07-26) | Pease's actual claim; naming convention; FS mother-indexing |
| 10 | [Probability](#probability-table) | The current table and its category definitions |
| 11 | [Next actions](#highest-value-next-work) | Ranked, with access notes |

## Summary

A hypothesis-directed paleographic reading identified a target line **by date alone**, never
transcribed it, and scored one pre-named token against a permissive alternative. Four letterform
tests all "favoured ffrancis" because the test design guaranteed it, not because of the ink. The
crop lost its coordinates, then became the object of study for three model families in sequence —
so three independent reviews re-confirmed one mislocated input. The resulting reading propagated
into a research topic file, a case file at 65% confidence, and a public web page.

Re-run against the full page range with recorded coordinates, the entry is not there; the indexed
record is six years later and belongs to a Horne family. The consequence for the wider case is that
**Candidate B lost its only positive document and now rests entirely on elimination of rivals plus
an auxiliary hypothesis that predicts the absence of evidence** — a structure that cannot be checked
against any record naming the man.

---

Worked 2026-07-22 against the full page run `00693`–`00768` supplied in
`original-content/Parish_Register/`, the April 2026 notebook bundle in
`original-content/april-1-2026-john-notebook-bundle/`, and the two downstream documents
(`research/topics/east-dereham-parish-register-paleography.md`,
`site/website/key-research/east-dereham-ai-assistant-procedure.md`).

All crops cut from the masters with `tools/paleography_image_workbench.py`. Working crops in
`wip/`. Boxes are `x,y,width,height` in master coordinates.

---

## Summary

The March 2026 analysis identified the target line by **date alone**. Asked to find a
FindMyPast record indexed as *John / Gorne / father Nicholas / 10 Jan / PD 86/41*, it located a
line reading `Ianuarij 10` on page **00722** and treated it as the record. That line is

> **Amorye the daughter of Robart Enderby — Ianuarij 10**

— a daughter, not a son; no John, no Gorne. The four letterform tests then adjudicated
`ffrancis` against `Nicholas` on the father-name of *that* line, which is `Robart Enderby`.
Every downstream conclusion about "John Entry E" rests on it.

The record the index actually describes is on page **00726** (re-shot at 00727, and its foot
re-shot again at 00730/00731):

> **John the sonne off Nicholas Horne bapt — Janua 10**

(The surname is `Horne`, not the index's `Gorne` — see D8. I read it as `Gorne` on first pass,
following the index, and was wrong.)

It is legible, in a clean round italic, and it matches the index on every field. It is the last
entry on the christenings sheet of the 1616–17 annual return, so its date is **10 January
1616/17 = 10 January 1617 modern** — not c.1609–1610.

Seven deviations are itemised below. Five are confirmed errors of fact; two are structural
assumptions that produced them.

---

## D1 — The canonical crop is from 00722, and it is not the John entry (CONFIRMED)

`line_05_enh_x3.png` and `john_gurney_715_enhancement_sweep_v1.png` are the same crop in
different enhancement states. Reproduced exactly from page 00722 at box `1880,1055,1120,190`
(`wip/p00722/verify-vs-line05.png`) — identical strokes, identical stain pattern, identical
three-line stack.

The crop spans the tails of three consecutive entries:

| Line | Reading | Date |
|---|---|---|
| 3 | Elizabeth the daughter of Tomb Lowis | december 30 |
| 4 | **Amorye the daughter of Robart Enderby** | **Ianuarij 10** |
| 5 | Mary the daughter of Iohn Ramplinge | Ianuarij 6 |

Line 4 is the one the crop centres, and it is the only `Ianuarij 10` in the vicinity — the reason
it was selected. The word the four tests adjudicated as "ffrancis vs Nicholas" is in the
father-name position of line 4: `Robart Enderby`. Neither candidate reading was ever on the page.

The label "00715" was carried through every artifact and both downstream documents. It was
wrong from the first crop.

## D2 — The real record is on 00726/00727 (CONFIRMED)

Page 00726 is a complete sheet: the 1616–17 certificate heading, then `Christninges`, running
march 27 → Janua 10. Its last nine entries are, in order:

Thomas / Tho: Woode (Septem 8) · Barnard / Willm Wigginton · Roger / John Mayes (October 13) ·
Willm / Martine Darbye · Susane / George Harvie (desem 8) · Willm / **John Nicholas** (desemb 15) ·
Robt / James Ellwood · Roberta / John Bartlebye (Januari 5) · **John / Nicholas Gorne (Janua 10)**.

Those same nine entries, same order, same hand, appear as the lower membrane of the 00730 and
00731 frames — those frames photograph the burials sheet lying on top of this christenings
sheet, with its foot showing beneath. `wip/p00726-foot.png` shows the sheet ending immediately
below the Gorne line.

Reading at scale 10 (`../working-snippets/packet-56/pass0/p00730/target-fathername-x10.png`):
`Nicholas` shows a single-stroke capital N, a clear `h` ascender, a clear `l` ascender and a
`-las` terminal. The same scribe writes `Nicholas` again three lines above as the surname in
`Willm the sonne off John Nicholas` — a same-hand, same-word exemplar rather than a letterform
argument. The surname is `G-o-r-n-e`, a round `o` where this hand's `u` shows two minims.

The FindMyPast index was correct.

## D3 — The date is 1617, not c.1609–1610 (CONFIRMED)

00726 carries an in-parchment heading: *"A Trewe Certificate or Register Bill Endented of all the
Christninges, Marriages and Burialls in the towne of East Dereham from the 25 of march 1616 unto
the 25 of march 1617; Mr John Bretton being then Vicar and parson…"*

The Gorne baptism is the last christening on that sheet. 10 January in a 25 March – 25 March year
beginning 1616 is **10 January 1616/17 = 10 January 1617 modern**.

The topic file dates the entry "c.January 10, 1609–1610" with a ±2–3 year margin. The true date is
outside that margin by about seven years. Any chronological argument built on the c.1609–10
placement needs rebuilding.

## D4 — 00721 carries a contemporaneous 1610 heading (CONFIRMED)

`wip/p00721-heading.png`, box `1650,600,2000,560`, shows **inside the parchment**, in the
contemporary hand and ink:

> East Dereham
> 1610
> A true certificat of all the mariages, christninge and buriall[s] for the yeare abovesayd
> Christninge

Separately, on the modern mount outside the parchment edge, a modern hand has written `1610`
(top right) and `PD 86/41/6` (top left). Both exist; the analysis saw only the modern one.

The topic file states that "the FS-indexed 1610 year derives from a modern marginal annotation,
not from an in-parchment heading" and holds Edward's year at ±2–3 years on that basis. This is
wrong. **Edward the sonne of ffrancis Gurney, baptised may 27, is 27 May 1610, D-class**, fixed by
a contemporaneous heading on the same sheet. The FS index was right here too, and the repo
downgraded it on a false premise.

## D5 — The "one page per annual return" assumption is wrong (CONFIRMED)

The topic file builds its chronology lattice "assuming one register page per annual return with
paired duplicate scans". The register does not work that way. Each annual return runs across
**several sheets**, and each sheet is photographed **twice**. In the 00721–00732 stretch:

| Sheets | Return | Basis |
|---|---|---|
| 00721 (+00722/00723) | 1610 | in-parchment "East Dereham 1610" |
| 00726/00727 → 00728/00729 | 1616–17 | in-parchment "25 of march 1616 unto the 25 of march 1617" |
| 00730/00731 | 1616–17 burials sheet, over the foot of the 00726/00727 christenings sheet | entry-for-entry match with 00726 |
| 00732 | 1618–19 | in-parchment "from the 25 of march 1618 untill the 25 of march 1619" |

The lattice rows `00728/00729/00730 = 1617` and `00731/00732 = 1618` are therefore mis-assigned:
00728–00731 all belong to the 1616–17 return. 00732's year is right, but by its own heading, not
by interpolation.

The duplicate-pairing itself was partly right — the topic file lists 00726/00727 and others as
probable pairs — but 00714/00715, 00722/00723, 00728/00729 and 00730/00731 are also pairs, and
the pairing was never used to correct the page-per-year assumption.

## D6 — The *filia populi* control is real but does not apply (CONFIRMED)

`Alyce the daughter of Iane Iewell filia populi bapt: ffebr 11` is genuinely on page 00715, at
y≈1988 (the July prompt pack's y 1955 is ~30 px high). The reading is sound.

But it cannot do the work asked of it. The John entry is not on 00715, and 00715's secretary hand
is a different scribe from the 00726/00730 round italic. The inference "this clerk marked status
when it applied, so a plain entry on this page is positive evidence of legitimacy" is void on both
counts. Whether the 1616–17 scribe had a status convention is untested; the one candidate in that
hand is the damaged first burial on the 00730/00731 upper membrane.

## D7 — The singleton argument is refuted on the analysis's own page (CONFIRMED)

The notebook §15.3 records, as contextual support for `ffrancis` over `Nicholas`:

> `Nicholas` as father name: exactly one occurrence in the reviewed corpus (the John entry only)

`Nicholas` is a common name in this register. On **page 00715 itself** — the page the analysis
believed it was working on — line 18 reads `Godfrey the sonne of Nicholas Terry bapt ffebruary 11`.
On 00722, the page the crop actually came from, an entry three lines below the adjudicated line
reads `… the sonne of Nicholas Lee Ianuarij 20`. On 00726, the sheet carrying the real record,
`Nicholas` appears as a surname in `Willm the sonne off John Nicholas`.

The frequency claim was asserted rather than counted, and it is false. `Gorne` may still be
uncommon; that has not been tested here and should not be assumed either way.

## D8 — The surname is `Horne`, not `Gorne` — and my own first reading repeated the error

Allen's independent observation that `Gorne` does not occur as a surname in the wider record set
of the period prompted this test. It is correct, and the reason is that the surname is not `Gorne`.

Same page, same hand, three initials at scale 12 (`wip/initials/init-contact-sheet.png`):

| Exemplar | Form | Box |
|---|---|---|
| `George` (in `George Harvie`) | closed bowl sitting on the baseline, small curl at top right, **no descender** | `2390,3350,180,130` |
| `Harvie` (same line) | tall looped ascender + **large descending loop below the baseline, swinging left** | `2520,3350,190,130` |
| target surname initial | tall looped ascender + **large descending loop below the baseline, swinging left** | `2380,3645,200,130` |

The target initial matches the `H`, not the `G`. Corroborated by three further same-hand capital
`H` forms in the first three christenings on the same sheet — `Henrye` (twice, line 1) and
`Harling` (line 2), at `1800,1180,1700,300` — all showing the same loop-plus-descender
architecture. The only `G` available on the sheet is `George`, and it is a different letter.

**The line reads `John the sonne off Nicholas Horne bapt — Janua 10`.** `Horne` is a common
Norfolk surname; `Gorne` is a FindMyPast indexer's misreading of `H` as `G`, which is why it never
turns up elsewhere.

This also matters as a control on *this* audit. On first pass I read the surname as `Gorne`
because the index said `Gorne` — the same anchoring failure documented in R1 below, at smaller
scale. It survived until an external fact (Allen's knowledge of period surnames) forced a test
that the reading could fail. The correction did not come from looking harder at the strokes; it
came from a check the reading could lose.

---

## Root-cause chain

**R1 — The premise was supplied, not tested.** The opening prompt was "This record is reportedly
on this image." That asserts both that the record exists and that it is on that page. The task
became *locate*, not *verify*. No step in the workflow could return "not on this page."

**R2 — Match on the weakest field.** The index offered five checkable fields: forename `John`,
relationship `sonne`, father `Nicholas`, surname `Gorne`, date `10 Jan`. The date is the least
discriminating — the register has a 10 January most years — and the easiest to spot, because
numerals stand out in secretary hand. It matched on that one and stopped. The four fields that
would have falsified the identification were never compared to the line.

**R3 — Forced binary with no null option.** Every test asked "does this behave more like
`Nicholas` or like `ffrancis`?" A token that is neither still scores, and it scores for whichever
hypothesis is more permissive. `ffrancis` is the permissive one: a fused, loop-heavy, low-
information shape, so "not a clean capital N" resolves as "favours ffrancis". `Enderby` is not a
clean capital N. Hence four tests out of four. **The unanimity was a property of the test design,
not of the ink** — and running more tests made it more confident, not more correct.

**R4 — The crop became the object of study and lost its address.** Notebook §6.3 records that the
crop coordinates are "not recoverable". After that, every pass — the enhancement sweep, the
comparator composite, the Codex six-state rebuild, the Claude spot-checks — operated on the crop
rather than the page. A crop cannot be re-contextualised. The words `the daughter of` sit inside
the crop, four words left of the adjudicated token, and were never read, because nobody was
transcribing a line; they were scoring a token.

**R5 — Reconstruction presented as procedure.** The notebook was written after the fact and says
so. It is precise about enhancement families, CLAHE clip limits and "25+ state-inspections", but
every one of those numbers is downstream of the line identification. §5.2 lists "lower-register
target search for John line" as *reconstructed likely* — so the one load-bearing step is the only
one with no evidence behind it, inside a document whose density reads as rigour. Effort was
concentrated where it could not help.

**R6 — Independence illusion across models.** ChatGPT produced the crop; Claude reviewed the crop;
Codex rebuilt the sweep from the crop. Three model families, one input. Agreement on a shared
mislocated input is the same error counted three times, and because each pass was read as
corroboration, the review mechanism actively raised confidence in the error.

**R7 — Assertion in place of counting.** The singleton claim (§15.3) was presented as a corpus
statistic. Nobody counted. It is false on the page the analysis believed it was reading.

**R8 — Labels became facts.** "00715" was attached before the target was located and never
re-derived. The comparator artifacts are honestly named after their true pages
(`candidate_721_…`, `candidate_724_725_…`); only the target lost its address, and only the target
was never re-checked.

### Why the cross-page `ffrancis` comparison did not catch it

The comparator work across 00721 / 00725 / 00732 was sound in itself — those entries hold up, and
00721's Edward line re-verifies today. The failure is that its *conclusion* was transferred to a
token on a different line. The transfer felt safe because 00722 is in the same 1610-era hand as
the comparators, so the letterforms genuinely were commensurable. A same-hand comparator set can
validate itself and still be applied to the wrong word. **Comparator validity is not target
validity.**

Note also that the comparator method cannot be run on the true record at all: 00726 is a different
scribe six years later, writing `off` for `of` in a round italic. The evidence there is instead
*within-page, within-hand* — the same scribe writes `Nicholas` again fourteen entries above, and
the `G`/`H` contrast in D8 comes from the same sheet. That is stronger than cross-page comparison,
because it removes the scribe variable rather than assuming it away.

---

## What survives

Not everything in the May 2026 pass is affected. These findings were made on correctly identified
pages and are untouched by the above:

- **Marye, 00732** — `Marye the daughter of ffrancis Gurnoe bapt may 25`, 25 May 1618. 00732's
  in-parchment heading independently confirms the 1618–19 return, so the date holds.
- **Agnes, 00725** — the refutation of the FS-indexed "Susan" on capital-letter architecture.
- **Marye, 00725** — the refutation of `daughter` in the relationship token.
- **1620 anchor, 00735/00736** — in-parchment "Christings Anno Dom 1620".
- **Edward, 00721** — the line reading itself. Only its *year confidence* changes, and it
  improves: from ±2–3 inferred to 1610 direct.

The May 2026 second-opinion pass also declined to confirm the John reading, recording it as
UNCERTAIN and noting it had not been supplied with the canonical crop. That caution was correct.
The failure was that the reading stayed in the topic file at "Probable" regardless.

## The Margaret Rybett marriage — re-read and CONFIRMED (2026-07-22)

Allen supplied the Ancestry image of the Norwich St Martin at Palace register
(`4143432_01883.jpg`, 4604×3452; caption "NORWICH ST MARTIN AT PALACE bapt. marr. and bur.
1538–1639"). The repo held no copy — `nro-pd-12-1` has `mediaPath: null` — so this is the first
time the marriage image has been examined since March 2026.

The entry is on the left page, sixth line of the top membrane block, master y≈710:

> **franc: Gurney et Margarett Rybett nupt 23 Sept**

Verified at scale 10–12 (`wip/marriage/tok-francgurney.png`, `tok-rybett-date.png`): the surname
`Gurney` is legible; `Rybett` is legible with a clear capital `R` and `-bett` terminal; the verb
is `nupt` (nupserunt, "were married"); the day is `23`. The entry sits above the in-register
`Anno Dm 1612` block, in the September run of the prior year, fixing it to **23 September 1611**.

**This reading holds where the John reading failed, and the contrast is the whole point.** This is
a Latin marriage entry read as a complete unit: both surnames independently legible, the marriage
verb present, the date present, the year bounded by the next year-block. Five fields, all read off
the ink, all mutually consistent. The John "reading" was one pre-named token scored for shape. The
marriage is what a sound paleographic identification looks like; the John entry never was one.

Caveat retained: the surname is an abbreviated `franc:` forename plus `Gurney`; the image is a
microfilm frame and the ink is light, but nothing in the strokes resists the reading and every
field corroborates. The March 2026 conclusion on the marriage is upheld.

## Parish-register crawl for a John Gurney baptism (2026-07-22)

Allen directed an over-inclusive crawl of PD 86/41 from the earliest pages through 1618. Worked
from the full run in `original-content/Parish_Register/` (00693–00768). Readable christenings
crops in `wip/crawl/`. The register runs as combined annual returns, each membrane shot twice, so
coverage is stated per return.

**Result: no John Gurney baptism exists in this register. The only two Gurney baptisms are Edward
(1610) and Marye (1618); the only Gurney events are those plus the two 1615 burials.**

| Return | Pages (dup pairs) | Depth | Gurney entries |
|---|---|---|---|
| 1595–96 fair copy | 00700 (+early run) | sampled, legible fair-copy hand | none |
| pre-1608 (1590s–1607) | 00693–00709 | **triage only** — not line-complete | none flagged |
| 1608 | 00710/00711 | marriages + burials read; christenings (≈00708) not read | none in marriages/burials |
| **1609** | 00712/00713 + 00714/00715 | **full christenings, both halves** | **none** |
| **1610** | 00720/00721 + 00722/00723 | **full christenings** | **Edward s. of ffrancis Gurney, May 27** — the only Gurney; the one other John is "John s. of Tomb Lawrence, July 29" |
| 1615 burials | 00724/00725 | prior work, not re-read today | Marye + Agnes Gurney burials |
| 1616 | 00726/00727 (+00730/00731 foot) | last 9 christenings full; top read at overview | none Gurney — the last entry is John s. of **Nicholas Horne** (D8) |
| 1617–1618 | 00728–00732 | not line-read this pass | Marye s.… 1618 on 00732 (prior work) |

The two returns in the hypothesis window — 1609 and 1610 — are line-verified across both membranes
and contain **no John Gurney**. The 1609 return has no Gurney at all; the 1610 return has only
Edward. A John Gurney baptism "c.1609/10" does not exist in this register.

### Two further deviations surfaced by the crawl (2026-07-22)

**D9 — The image set jumps from the 1610 return straight to the 1616 return; 1611–1615 are absent.**
The 1610 annual return occupies images 00720–00725 (each of its three membranes shot twice):
00720/00721 summer christenings (incl. Edward Gurney, May 27), 00722/00723 winter christenings +
`Mariages`, 00724/00725 `Burialls`. The next image, 00726/00727, carries the in-parchment
"25 of march 1616 unto the 25 of march 1617" heading. **There is no 1611, 1612, 1613, 1614, or 1615
christening membrane in this image run.** So the natural birth window for a first child of the
September 1611 Norwich marriage — roughly 1612–1615 — is **not observable in this image set at all**.
A "no John Gurney baptism found" for those years reflects missing pages, not a searched negative.

**D10 — The "Marye / Agnes Gurney burials" on 00725 are almost certainly a misread of "ffrancis
Prudy," and the page is the 1610 return's burials, not 1615.** 00724/00725 is a duplicate pair and
is the `Burialls` section of the **1610 return** (it opens "Mariages ffinished / Burialls" directly
after the 1610 marriages on 00723) — not, as the topic file has it, the 1615 burial subsection sitting
before 00726. On this page the only two burials naming a father "ffrancis" read, at scale 6,
**"Mary the daughter of ffrancis Prudy, January 25"** and **"Constance the daughter of ffrancis Prudy,
[Feb] 31"** — a tall-looped initial then `r-u-d-y`, two daughters of one ffrancis Prudy, with no
G-initial surname anywhere on the page. This matches the prior work's "Marye … of ffrancis Gurny …
25" and "Agnes … of ffrancis Gurny … 31" in forename-cluster, father-forename, and day, and is the
same failure signature as the John entry: a "ffrancis" father plus a searched-for surname, read onto
a line whose surname is something else. Flagged, not yet closed — the FS index also carries these as
"Gurny" burials (VNN2-WR2, VNN2-WRG), so a dedicated high-resolution re-read (and a check of what
image those FS ARKs point to) is needed before the burials are formally withdrawn. But the surname on
this page is not Gurny.

If D10 holds, the only Gurney events in the entire register are **Edward's baptism (1610)** and
**Marye's baptism (1618)** — and Edward (May 1610) predates the September 1611 marriage, so he cannot
be Margaret Rybett's child. That in turn raises an identity question the case file has not tested:
whether the "ffrancis Gurney" fathering children at East Dereham (1610, 1618) is the same man as the
gentry Francis Gurney of West Barsham who married at Norwich in 1611 and lived in London — or a
distinct local namesake.

Honesty on depth: the pre-1608 pages (1593–1607, sampled clean as legible fair copies with no Gurney)
and the 1616–1618 christenings (other than the 1616 tail) were not read line-by-line at readable
scale this pass. Given Francis did not marry until September
1611 and appears at East Dereham only from 1610, a pre-1608 John-Gurney baptism would be
chronologically incoherent, and the 1595–96 sample confirms no Gurney family presence in the early
section. To *close* the negative rather than rest it on the hypothesis window, those remaining
christenings pages need a readable pass.

## Probability reassessment — the John Gurney origin options (2026-07-22)

The colonial John Gurney identification runs on four named candidates plus the null. Today's
findings move only one of them, but they move it materially.

**Candidate B — son of Francis Gurney & Margaret Rybett (the case-file thesis): downgraded from
leading hypothesis to a live-but-undocumented one.** Candidate B rested on two ★ primary-source
discoveries. One of them — the "John son of ffrancis Gurnie" baptism, the case file's own
"strongest single anchor for placing the colonial John Gurney's birth family at East Dereham" —
does not exist. What that removes:

1. *The only record of a John connected to this family.* The marriage (confirmed today) establishes
   that Francis had a first wife and *could* have had children c.1612–1617. It is a necessary
   condition, not evidence of a son John. Candidate B now has no documentary John at all — it has a
   marriage plus a family tradition (Pease) plus a circumstantial web (Merchant-Taylor trade
   lineage, Norfolk→London corridor, 1634 land sale as motive, Puritan network). That web is intact
   and still distinguishes B from the eliminated candidates, but it no longer rests on a record of
   the man himself.
2. *The reconciliation of the age tension.* The colonial John deposed "aged about 50" in 1653 →
   born c.1603. The baptism (Jan 1609/10) let the case file pull the birth later to c.1607–1612;
   even so it sat *before* the September 1611 marriage, the acknowledged pre-marital-birth problem.
   Remove the baptism and a legitimate child of the 1611 marriage is c.1612+, i.e. ~41 or younger in
   1653 against a deposed ~50 — the age fit gets *worse*, not better.
3. *Part of the Norfolk corroboration.* The East Dereham Gurney children used to show Francis
   fathering children in Norfolk in the right window are now: Edward (May 1610, which predates the
   1611 marriage, so not Margaret's), Marye (1618, not re-verified today), and the "Marye/Agnes
   Gurney burials" that read as **ffrancis Prudy** (D10). And a new identity question sits under all
   of it (D10): whether the East Dereham "ffrancis Gurney" is the gentry Francis of West Barsham /
   Norwich / London at all.

   *Counterweight, and it is real:* the 1611–1615 register gap (D9) means the natural birth window
   for a first child of the marriage is **unobservable in this image set**. So Candidate B is not
   *refuted* — the disproof removes the positive evidence without supplying negative evidence. The
   honest position is that B can likely be neither confirmed nor excluded from East Dereham, because
   the pages that would carry a c.1612–1615 John are not here.

   Net: B falls from "two primary anchors + circumstantial web" to "one marriage that only proves
   possibility + a family tradition + a circumstantial web," with the age tension worsened. It
   remains the best-supported of the *named* candidates, because the circumstantial case is real and
   the rivals are independently eliminated — but its lead over the null is now small, and it is no
   longer a documentary identification.

**Candidates A (Aylesbury/Walgrave), C (Berkhamsted), D (London textile): unchanged — still
eliminated.** Their eliminations rest on continuing-English-residence and child-set mismatches
that never depended on the East Dereham baptism. Today's findings neither revive nor further weaken
them.

**The null — origin undetermined: upgraded.** With B's distinguishing document gone, the gap between
"Candidate B" and "we have not documented where the colonial John was born" narrows sharply. The
defensible current state is that the emigrant's English origin is **not established by a record of
him**; Candidate B is the leading circumstantial reading, not a proven descent.

### Elimination audit of Candidates A, C, D, E — how complete is each?

Re-reviewed §8.1–8.6 against the user's question: where several John Gurneys occupy one region, is
the elimination *documented* or *inferred*? Two of the four have soft joints, and both soft joints
matter more now that B has lost its anchor.

**Candidate A (Aylesbury hundred → Walgrave) — INCOMPLETE. The 1603 Stewkley baptism is not
independently eliminated.** The post-1628 household is soundly eliminated: the Bierton 1628 marriage
to Alice Oliffe, five St Mary Aylesbury baptisms 1638–1653, the 1641 certificate of residence
(TNA E 115/180/113) and the 1650 Walgrave tenancy put that man in England throughout the colonial
John's American window. That holds.

But the chain's *first* link is joined by inference, and the case file says so in its own words:
"the 1603 baby is Candidate A only if the same person also marries at Bierton in 1628; even if
those two events belong to different individuals, the post-1628 chain stands on its own." The
post-1628 chain does stand — but severing the link leaves the 1603 baptism unaccounted for, and
**the 21 February 1603 Stewkley baptism is the single closest age match to the colonial John in the
entire corpus.** "Aged about 50" deposed in 1653 implies c.1603. Nothing else surveyed lands on the
year that squarely. Eliminating the best age match in the file by merging it into a household it
may not belong to is exactly the inference class this audit is about.

What the merge rests on: same hundred, plausible age at marriage (25 in 1628), and no competing
trail. What weakens it: Aylesbury St Mary alone carries a *second* John Gurney marrying Anne
Cowheard in 1638 — the same year and parish where the Oliffe household's baptisms begin — plus
further John Gurney marriages there in 1644 and 1669. The parish demonstrably held more than one
John Gurney at once, so "one household" is a reconstruction, not an observation. **Open action:** a
Stewkley/Aylesbury-hundred burial and probate search for a John Gurney b.1603 who is *not* the
Oliffe husband. If he is found dead or resident in England, A closes completely; until then the
1603 baby is a live loose end.

**Candidate C (Berkhamsted) — COMPLETE. No change.** The elimination is documentary and independent
of anything East Dereham: fathering from 1610 puts the Berkhamsted John's own birth at c.1585–90,
thirteen to eighteen years off the colonial John, and the eight-child set 1610–1636 mismatches on
names (Henry, Michael, Francis present; Mary and Peter absent) and on dates for all three shared
names. The household's own son John (b.1624) is separately too young — 29 in 1653, not "about 50."
Two independent grounds, neither inferred. C stays eliminated.

**Candidate D (London, Old Change / St Augustine Watling Street) — PARTLY INFERRED, and the weakest
elimination in the file.** The load-bearing evidence is a **1662 hearth-tax entry** at 1 hearth
"poore" in the St Augustine precinct, read as the same man as the **1638** T.C. Dale return at £10
rent. That is a name-plus-parish identity asserted across a **24-year gap**, in two tax lists that
carry no patronymic, occupation, or age. It is the same inference class — name matches, therefore
same person — that produced the John-baptism error.

If the 1662 entry is a different John Gurney (a son, nephew, or unrelated parishioner), Candidate
D's documented trail ends in **1638** — and the colonial John first appears in America in **June
1641**. That is a clean three-year emigration window.

D also has the strongest independent profile of any rival, which the case file partly obscures by
eliminating it early:
- **Trade:** the colonial John was a *tailor*. D was a Draper by redemption (Feb 1623/4) and his
  father Robert was "described as a tailor at Old Change." This is a direct occupational match, not
  the inherited-trade inference B relies on.
- **Age:** admission by redemption in 1623/4 implies birth c.1598–1603 — a *better* fit to "aged
  about 50" in 1653 than Candidate B's post-1611-marriage window.
- **Corridor:** London, the emigration hub itself.

Against D: no London marriage to a Mary, no baptisms of Sarah/Mary/Richard/John/Peter in the parish,
no Puritan or Massachusetts bridge in the Old Change record set, and no Drapers' turnover for any
Gurney 1620–1670 (though a man who emigrated would simply stop appearing, so absence of turnover is
weak). **Open action:** verify whether the 1638 and 1662 entries are one man — a St Augustine
Watling Street burial search 1640–1670, and any Drapers' or parish record naming John Gurney between
1638 and 1662. A single intervening record closes D; continued silence 1638–1662 reopens it.

**"Candidate E" — no such label exists in the case file.** The candidate roster is A, B, C, D plus
the §8 "Unlikely" rows and the §8.6 clearance sweep. The nearest thing to an E is **§8.5, the 1636
Newgate apprentice** — a second John Gurney physically in Massachusetts, brought before the Boston
governor 21 July 1636, service ordered to age 24 (implying birth c.29 September 1615). Treating that
as E: **elimination is sound in structure but leans on compiled-source dates.** The two tests are
(a) family status — the Braintree John had married Mary by c.1627 with three or four English-born
children, incompatible with an indentured servant; and (b) chronology — 1615 birth vs c.1602/3 from
the deposition. Test (b) is solid. Test (a) is only as good as the colonial children's birth years,
which come from Sprague (2001) and the *History of Weymouth* (1923) as estimates ("bc.1628",
"bc.1630"), not from primary records. If those estimates are soft, the apprentice — who finished
service in September 1639, eighteen months before the colonial John's first American record —
becomes harder to separate. Held eliminated, with that dependency named.

**Regional multiple-John problem, generally.** §8.3 lists roughly twenty further Buckinghamshire and
Hertfordshire John Gurney households, and the sorting of the Aylesbury Vale cluster into discrete
households is done from wife names and child names. That method is reasonable and mostly persuasive,
but it means several §8.6 "ELIMINATED" verdicts are properly read as *"the household as
reconstructed is eliminated"* — not as a person-level clearance. This does not overturn any single
row; it argues for a modest residual probability spread across the surveyed set rather than zero.

### Iteration 2 — corrections to my own reassessment, after reading the G13 topic units

The first reassessment was made from the case file alone. Reading the `g13-john-gurney/topics/`
units corrects two of my own errors and surfaces one argument neither surface makes.

**I was wrong about Candidate D, and wrong the same way the March analysis was wrong.** I wrote
that D's elimination rested on "a 24-year name-and-parish identity with nothing between." That is
false, and I would have known it had I read `identity/34-london-draper.md` instead of only case-file
§8.4. The elimination actually rests on three points plus a second independent ground:

- 1638 — T. C. Dale's London rents return, John Gurney at £10, St Augustine, in the same manuscript
  section as Joseph Huntscott (the overseer of Robert Gurney's 1625 will) at £12.
- 1661 — a **Boyd's Inhabitants of London card** for "John Gurny of S Augustine" carrying, in one
  card, "1661 poll tax [unclear] Old Change 1638 rent £10." An independent compiler tied the two
  returns to one man at one street.
- 1662 — Merry's hearth-tax database, John Gurney "in St Austins precinct," 1 hearth, "poore."
- Plus: no London marriage to a Mary and no baptisms of Sarah/Mary/Richard/John/Peter in any London
  parish, company, or index record 1620–1641.

Same parish *and* same street across the span, with a middle datum. The surviving softness is that
the 1661 reading is second-hand through a partly-illegible card and the underlying TNA E 179
1660–61 return has not been retrieved at image level. That is a real but minor gap.

**This is worth naming as a process failure, not just a wrong number.** I criticised an elimination
without reading its fullest treatment, then published a probability off that partial read. That is
the identical failure mode this audit documents — reasoning from a partial artifact instead of the
primary one. It argues the corrective discipline has to be *routine*, not something applied only
when someone is watching. **D: 10% → 3%.**

**I overstated the D10 identity question.** `identity/32-norfolk-parentage.md` already separates two
contemporaneous Francis Gurneys — Francis-A (West Barsham gentleman, Merchant Taylor, freed 1606)
from Francis-B (Norwich plebeian laceweaver of St Peter Mountergate) — by simultaneous independent
record: in 1627 Francis-B's son James was apprenticed at Norwich while Francis-A was baptising
children at St Benet Fink in London. That is sound work I did not credit. A smaller residue
survives: what positively places **Francis-A** at East Dereham is the East Dereham children
themselves, supported by context (Great Ellingham five miles off, the Margery Gurney widow
precedent, Rivett kin two to three miles away) rather than by any record naming him in the parish.
The inference is reasonable; it is still an inference.

**Candidate A(1603) was also too high.** `identity/31-candidate-a-aylesbury.md` documents five to
seven simultaneous John Gurney households in Buckinghamshire — "the county was simply not short of
Gurneys named John" — and the Stewkley manor itself passes to the Cublington John + Mary line. A
John Gurney born at Stewkley in 1603 to a John Gurney Sr. most plausibly grew into one of the many
Bucks households that demonstrably stayed put. The merge remains undocumented, but the alternative
is not emigration to Massachusetts with no trade, corridor, or network link. **A(1603): 6% → 3%.**

### The argument neither surface makes: Francis's apprenticeship bounds John's birth

This is the sharpest surviving problem for Candidate B, and it is not in the case file, the topic
units, or my first pass.

Francis Gurney was bound apprentice in London on **14 May 1599** for a seven-year term, assigned
over to William Smooth on 3 February 1605, and admitted to the freedom of the Merchant Taylors on
**30 June 1606**. London livery companies prohibited apprentices from marrying, and enforced it.
**Francis could not have married, and could not ordinarily have fathered a legitimate child, before
mid-1606.**

Set that against the age evidence. The 1653 deposition — "aged 50 or thereabouts" — reads c.1602/3
strictly, c.1603–1608 once age-heaping is allowed. Daughter Mary's 1647 marriage to Daniel Shed
bounds John as an adult by about 1625. The topic file's own synthesis is a probable window of
**1604–1608**.

Candidate B can only occupy the **1606–1608 sliver** — the overlap between "after Francis was free
to marry" and "early enough to satisfy the deposition." Below 1606 the father is a bound apprentice;
above 1608 the deposition age strains past its rounding allowance. And every year in that sliver is
still **three to five years before the September 1611 marriage**, so B continues to require a
pre-marital birth — no longer the "year or two" the parentage file absorbs as unremarkable, but a
half-decade, from a father who was in London and not yet free at the start of it.

Two readings survive, and they point opposite ways:

- **Pro-B:** Francis had an *earlier, unfound* marriage between 1606 and 1611. Margaret Rybett is
  called his "first wife" only because hers is the earliest marriage anyone has located. An earlier
  wife would place a legitimate John at 1607–1610 and dissolve the pre-marital problem entirely.
  This is testable — a Norwich/Norfolk marriage sweep for Francis Gurney 1606–1611 — and nobody has
  run it. It is the single highest-value untried search for B.
- **Anti-B:** the East Dereham household is simply not Francis-A's. Today's firm dating makes this
  sharper: Edward's baptism, which the topic file dates "about 1611/12," is fixed by the
  in-parchment "East Dereham 1610" heading on image 00721 to **27 May 1610** — sixteen months before
  Francis-A's marriage. The East Dereham Francis was fathering children while Francis-A was, on the
  record, four years free of apprenticeship and not yet married to anyone we can find.

### The unfalsifiability problem

`identity/37-identity-assessment.md` states B's evidentiary shape plainly: B "predicts a man who
would leave almost no English paper — a motherless son raised by his mother's kin, trained outside
both the guild registers that would have recorded him — so the absence of a confirming document is
exactly what the hypothesis expects, and cannot be counted against it."

That auxiliary is not baseless: it rests on two genuine negative searches (the Merchant Taylors'
apprentice rolls and the Norwich freemen and apprentice registers, both empty) and a documented
circumstance (Margaret died c.1616–17, Francis remarried and moved to London). But it is
structurally immunising, and while Entry E existed there was one positive document holding the
hypothesis to the record. **With Entry E gone, Candidate B consists entirely of: an argument from
elimination, a circumstantial fit, a marriage that establishes possibility, and an auxiliary that
converts every absence of evidence into expected silence.** No surviving component can be checked
against a document that names John.

An unfalsifiable auxiliary should not add confidence, and the elimination it leans on cannot be
exhaustive in principle — `37-identity-assessment.md` itself records more than forty distinct John
Gurney heads of household in England 1600–1670, in a parish-register field patchy enough that
others certainly went unrecorded. External calibration agrees: Anderson's *Great Migration
Directory* (2nd ed., 2025) still gives John's origin as **"Unknown"** — and that verdict was already
in place while Entry E was believed.

**What genuinely holds B up, stated at full strength.** The Pease tradition made one checkable
claim — that Francis's first wife was a "Margaret Ryvett" — which no genealogist from Daniel Gurney
through Bernau had ever found, and in March 2026 it checked out against the register. A tradition
that survives its only available test is worth materially more than an untested one, and that
verified prediction now carries more of B's weight than anything else. Around it sit real things:
Francis demonstrably had a Norfolk family in the right window; the 1634 total land sale is a
documented motive; the Rivett kin were two to three miles from the baptism parish; and the rivals
really are eliminated, three of them well.

### Revised probabilities

The case file currently carries Candidate B at **PROBABLE (~65%)**. These are subjective credences
over "who was the Braintree John Gurney," not frequencies, and the bands are wide on purpose — the
error being audited was false precision. They are stated because a reassessment without numbers is
not auditable.

### Iteration 3 — the Null was doing work it hadn't earned

**Criticism accepted: my 52% Null was a residual dump, not an estimate.** I set it by subtraction —
what was left after the named candidates — rather than by asking what proposition it actually
asserts. Asserting "no record of this man survives or is indexed anywhere" is a strong empirical
claim, and it has to be argued against the searches actually run, which are far broader than parish
registers: livery-company rolls (Drapers', Stationers', Merchant Taylors' apprentices), the Norwich
freemen and apprentice registers, PCC and archdeaconry probate, the Norfolk probate census
1585–1650, London hearth tax and the 1638 rents return, Boyd's Inhabitants, Exchequer certificates
of residence, the 1633 Visitation, Phillimore's printed registers, and a twelve-variant same-name
sweep across eighteen collections. A man with a baptism, a marriage, five children, and a trade has
seven or eight chances to surface across those classes. Requiring *all* of them to fail is a much
narrower claim than "one-third of parish registers are missing." **Null: 52% → 24%.**

But the second observation cuts the other way, and it identifies a real mechanism I had not named.

### The dense-cluster masking effect — why the Bucks eliminations are weakest where they look strongest

The elimination method is: *a John Gurney is documented in region R across the emigrant's American
years, therefore the John Gurney of region R did not emigrate.* **That inference is valid only if
region R held one John Gurney.** Buckinghamshire held five to seven simultaneously — Candidate A's
line, East Claydon, Chesham, Wing, Cublington, Hitcham, plus the Aylesbury, Ivinghoe, Marsworth,
Chenies and Edlesborough events. Where a name is that dense, **one man's departure is invisible,
because his same-named neighbours keep the name in the register continuously.** The record looks
unbroken whether or not somebody left.

So confidence in that region comes from record density — and density is precisely what creates the
masking. The eliminations are weakest exactly where they read as strongest.

Two pieces of the repo's own evidence show the individuation actually failing:

1. **Within a single parish.** `identity/31-candidate-a-aylesbury.md` cannot decide whether the 1638
   John Gurney × Anne Cowheard marriage at St Mary Aylesbury is a second John or Candidate A
   remarrying — "FamilySearch does not index a mother's name on the children's baptisms, so the
   point cannot be settled from these records alone." If individuation fails inside one parish, it
   cannot be assumed to hold across a county, still less across forty households.
2. **The "no wife Mary" filter is much weaker than it is used as.** It eliminates or downgrades
   several candidates, but where mothers are routinely unindexed, "no John + Mary household found"
   partly measures **index metadata, not historical reality**. A John Gurney household with a wife
   Mary could sit inside the surveyed set and be invisible as such. The children's names compound
   this: Sarah, Mary, Richard, John, Peter are among the commonest names of the period, so a partial
   match looks like any other household rather than like a signature.

**The consequence is a category error in my own table.** A conflated, split, or unrecognised John is
*not* a Null — he is in the surveyed record set, mis-accounted. That belongs in a Shadow row, and it
is much larger than the 13% Residual I gave it. **Shadow: 13% → 32%.**

Net effect of both corrections: "not a correctly-assessed named candidate" falls from 65% to 56%,
and its composition shifts decisively from *absent* to *present but mis-read* — which is a different
research problem with different remedies. Absence is answered by finding new records; mis-reading is
answered by re-individuating households already in hand, which is cheaper.

**Where I hold the line, as supporter of the existing work.** The masking effect does not dissolve
every elimination, because several do not rest on name-continuity at all:

- Candidate C is eliminated by the *father's own age* — he was fathering from 1610, so born
  c.1585–90. Immune to masking; a shadow John cannot make him younger.
- Candidate D rests on one man's tax entries tied across 23 years at one street by an independent
  compiler's card, plus a probate identification as Robert's son and executor.
- Candidate A's household has a 1641 Exchequer certificate of residence — a government record of a
  *specific individual's* move, not a parish name-continuity.
- Probate eliminations (Toddington, Winkfield, Earsham, the PCC corpus) each fix a *named
  individual's* death in England.

Individuating records — probate, certificates, licences, company admissions — resist masking.
Name-continuity in a register does not. The Bucks cluster is disproportionately the second kind,
which is why the correction concentrates there.

## New evidence 2026-07-26

### Pease does name a son John — and that is both B's best support and a circularity

`research/future-research/l-71-burke-landed-gentry-gurney.md` records what the Pease genealogy
actually says: Charles E. G. Pease, *The Descendants of Anthony Gurney*, has Francis "married first
Margaret Ryvett (**children: John b. c.1610, Anne b. c.1610**), then Anne Browning." So the
tradition does not merely supply a wife — **it names a son John and dates him c.1610.** I had
under-credited this: B's tradition makes two claims, one of which (the wife) was verified against
the register in March 2026.

**But the case file then uses the two claims to corroborate each other.** §11 row 12 reasons that
the verified Ryvett claim "lends credence to other details in the genealogy… such as John Gurney's
1610 birth (stated in genealogy and aligns to discovered baptism record)." The baptism was read as
c.1609/10 *by an analyst who already knew Pease claimed a John b. c.1610* — that is the R1/R2
failure, not independent convergence. Pease supplied the expected answer; the search found something
date-shaped; each was then cited as support for the other. With the baptism gone, Pease's c.1610
stands alone and unverified.

Two live questions follow, and the first is high-value:

- **What was Philis Wainford's source?** The Ryvett claim reached Pease from an American researcher
  via Sir Joseph Gurney Pease. An American researcher naming a 1611 Norwich marriage that Daniel
  Gurney and Bernau both missed either had a real source or made a lucky construction. If a source
  exists, it may also document the son John — and it would be the first independent evidence for B
  since the baptism failed. Pease cites Burke (1894) as source #177 for the Francis entry generally;
  whether the Ryvett/John detail comes from Burke or from Wainford is not established.
- **Pease dates *Anne* to c.1610 as well** — the same year as John. Two children both "c.1610" reads
  like a compiler's placeholder for "born around then," not two researched dates.

### The naming convention runs against B

Under the standard English naming custom of the period, a couple's **eldest son takes the paternal
grandfather's name**. The colonial John's sons, in order, are **Richard** (c.1630), John Jr.
(c.1633), and Peter (c.1635–40).

If John's father were Francis Gurney, the expected eldest son is **Francis**. There is no Francis
among the five children — already carried in the repo as a first-class negative (G13-RI-000193) —
but the convention sharpens it: the objection is not merely that Francis is *absent*, it is that the
**one slot the convention most strongly governs is occupied by another name.**

It gets slightly worse under B's own reconstruction. `identity/32-norfolk-parentage.md` identifies
Margaret as most likely the Garveston Margaret Rivet baptised 1586, **daughter of Francis Rivet**.
On that reading John's paternal grandfather *and* his maternal grandfather were both named Francis —
and he named no son Francis at all. The case file's explanation, that Richard honours Richard Ryvett
of Gressenhall, does not resolve this: Richard Ryvett is Margaret's brother or first cousin, i.e.
John's uncle or first cousin once removed — not a grandfather, and so not the person the eldest-son
slot conventionally names.

This is not decisive. Naming customs were followed loosely, and estrangement after Francis's 1634
financial collapse is a real explanation the case file already offers. But it is an independent
strand pointing the same way as the age evidence, and it costs nothing to check.

### FamilySearch does index mothers in the Buckinghamshire collection — the re-individuation is cheaper than I said

Checked live 2026-07-26. `identity/31-candidate-a-aylesbury.md` states that "FamilySearch does not
index a mother's name on the children's baptisms," and I built the masking argument partly on that.
It is true of **England, Births and Christenings, 1538–1975** (the older, thinner index the Aylesbury
work used) but **not** of **England, Buckinghamshire, Church Records, 1217–1994**, which does carry
mothers:

- Samuel Gurney, East Claydon, 20 Feb 1636 — parents **Elizabeth, John Gurney**
- Isaac Gurney, Cublington, 27 Jan 1664 — parents **John Gurney, Mary**
- Jane Gurney, Cheddington, 3 Mar 1636 — parents **Martha, Isaac Gurney**
- Frances Gurney, Linslade, 31 Jul 1636 — parents **Alice, Ezechiell Gurney**

So much of the Bucks re-individuation can be done **from a better FamilySearch collection without
pulling a single image.** That materially lowers the Unassembled estimate — the data largely exists
and was simply queried in the wrong collection — and it changes the top recommended action from an
image pull to an index re-query, with images reserved for the parishes the collection misses.

The same query surfaced **five Bucks Gurney households the case file has never assessed** —
Wingrave (Robert 1631; John 1624 s. of Thomas), Waddesdon (William + Elizabeth 1638), Mursley
(Richard + Anne 1646), Linslade (Ezechiell + Alice 1636; Henery 1660), and Cheddington (Isaac +
Martha 1636; Richard 1606, 1612) — plus **Simeon Gurney, baptised Stewkley 25 February 1604, son of
John Gurney**, a sibling of the 1603 Stewkley baby that confirms a settled Stewkley household.
"More than forty households" was an undercount.

### Access mechanisms, validated 2026-07-26

- **FamilySearch** — authenticated, working. The record-search URL pattern is unchanged, **but
  `q.surname.exact=on` combined with `f.recordCounty` returns "Something Went Wrong."** Drop both;
  filter by `f.recordCountry=England` and narrow with `q.birthLikeDate.from/to`, then read the place
  column. Working example:
  `familysearch.org/search/record/results?q.surname=Gurney&q.birthLikeDate.from=1600&q.birthLikeDate.to=1670&f.recordCountry=England`
- **FindMypast** — authenticated, working. URLs now redirect from `search.findmypast.co.uk/results/…`
  to **`www.findmypast.co.uk/search/results?…`**; use the new form. Category counts and record-set
  names render in page text without opening paywalled images.
- **Ancestry** — authenticated (the St Martin at Palace marriage image was pulled from collection
  61045 this session). Not separately re-tested.

## Probability table

**Category definitions — mutually exclusive, and every row names a *person*, not an error mode.**
The previous "Shadow" row was rightly criticised for overlapping the named rows: "in the surveyed
set" is a property most named candidates also have. It has been decomposed and reallocated, named
candidates first.

- **Named-and-assessed rows** (B, A(household), A(1603), C, D, Ackworth, apprentice) — each is one
  specific reconstructed man who has been individually weighed.
- **Bucks/Herts household heads** — each is also a specific reconstructed man, but was cleared *as
  part of a group* in §8.3/§8.6 rather than individually. Distinct from the rows above by depth of
  assessment, not by kind.
- **Unassembled** — a John Gurney whose records *do* appear in the surveyed sources but who has
  never been assembled into a person: scattered single events never linked to each other (Ivinghoe
  1640, Marsworth 1642, Aylesbury 1644/1669, Weston Turville 1627, Haddenham 1620/1622, Great Kimble
  1619), or a man whose records were wrongly merged into another household's reconstruction. He
  corresponds to no row above, because no row has ever named him.
- **Null** — no record of him survives or is indexed anywhere. Disjoint from Unassembled by whether
  records exist at all; the distinction matters because the remedies differ (re-query vs. new
  discovery).

| Option | Case file | It.1 | It.2 | It.3 | **It.4** | Basis |
|---|---:|---:|---:|---:|---:|---|
| **B — son of Francis & Margaret Rybett** | ~65% | 25% | 20% | 22% | **22%** | Pease does name a son John (support), but its date corroborated the baptism circularly (offset). No positive document; immunising auxiliary; 1606–1608 birth sliver forced by Francis's apprenticeship; 3–5 year pre-marital birth; eldest son named Richard, not Francis |
| **Null — no record survives or is indexed** | small | 38% | 52% | 24% | **22%** | Holds. Searches span probate, livery, tax, freemen and government classes; a man with ~8 record events must fail in all of them |
| **Unassembled — records exist, never linked into a person** | ~0 | 12% | 13% | (32%) | **20%** | Down from the old Shadow row: FS *does* index mothers in the Bucks Church Records collection, so the cluster is far more resolvable than I claimed. Residue is the genuine single-event tail and possible wrong merges |
| **Bucks/Herts household heads cleared as a group** | ~0 | — | — | — | **13%** | East Claydon, Chesham, Wing, Cublington, Hitcham, Weston Turville, Haddenham, Great Kimble + 5 households first surfaced 2026-07-26 (Wingrave, Waddesdon, Mursley, Linslade, Cheddington). Most have individuating burials; none was individually weighed |
| **Ackworth, Yorks (Gurnoe + Mary Burton)** | ~3% | 4% | 4% | 5% | **6%** | The one household with a documented wife *Mary* and an emigrant-shaped disappearance; blocked mainly by compiled-source colonial dates |
| **A(1603) — Stewkley baptism, if distinct** | elim. | 6% | 3% | 4% | **5%** | Best age match in the corpus. A sibling Simeon (1604) now confirms a settled Stewkley household — which cuts both ways: more reason he stayed, but also a documented family he could be lost inside |
| **D — London Old Change draper** | elim. | 10% | 3% | 4% | **4%** | Best trade and age fit of any rival; elimination is individuating (Boyd's card, probate), but the 1661 datum is second-hand through a partly-illegible card |
| **A(household) — the Oliffe husband** | elim. | <1% | <1% | 1% | **4%** | Raised: its individuating record, the 1641 certificate of residence, is flagged in the repo as **unverified** (never examined at image or catalogue level), and the 1650 Walgrave tenancy is an admitted sourcing gap. Without them it rests on name-continuity |
| **§8.5 Newgate apprentice** | elim. | 3% | 3% | 3% | **3%** | Structurally sound, dependent on compiled child birth years |
| **C — Berkhamsted** | elim. | <1% | <1% | 1% | **1%** | Eliminated by the father's own age — immune to every effect discussed here |

**Reading of the table.** B has held at 20–25% across four iterations while everything around it was
rebuilt twice — mild evidence the estimate tracks the evidence rather than the mood of the pass. It
remains the leading *named* candidate.

But no option now exceeds 22%, and the three leading rows — B, Null, Unassembled — are within two
points of each other. **The honest reading is that the identification is open**, with three roughly
equal possibilities: Francis's son, a man who left no record, and a man sitting in the records
already gathered whom nobody has assembled. That is a materially different statement from the
case file's published "probable, ~65%."

The practical value of the decomposition is that the three imply different work: B is tested by the
Francis 1606–1611 marriage sweep; Unassembled by re-querying and re-sorting records already in hand
(cheap, never attempted); Null only by new discovery or by DNA, which bypasses records entirely.

**Falsifiability note on these numbers.** A probability table is exactly the kind of artifact that
looks like rigour while resting on judgement, which is the failure this audit documents. Two guards:
each row above names the evidence it turns on rather than a feeling, and the numbers are stated so
they can be *attacked* — if the Francis 1606–1611 marriage sweep returns a first wife, B should jump
sharply and Null should fall; if the East Dereham household proves to be a different Francis, B
should collapse toward the Residual row.

## Highest-value next work

Paleography is no longer top of the list; it has been run to the limit of these images and produced
a reversal.

1. **A household re-individuation pass over the dense clusters** — highest-value record work,
   targeting the 20% Unassembled row and the 13% group-cleared row together. **Do it first as an
   index re-query, not an image pull:** the FamilySearch *England, Buckinghamshire, Church Records,
   1217–1994* collection carries mothers' names that the older *England Births and Christenings*
   index omits, so most of the Bucks cluster can be sorted into distinct households from the index
   alone. Reserve image pulls for the parishes that collection misses — St Mary Aylesbury above all,
   where the 1638–1653 baptisms and the Cowheard/Oliffe wife question sit.
2. **Y-DNA.** Braintree-line kit 576097 against the untested English-line kit 365744 in the FTDNA
   Gurney project. Wholly independent of every record argument, and the only lever that can move the
   Null row. Should have been first before this audit and certainly is now.
3. **A Francis Gurney marriage sweep, Norwich and Norfolk, 1606–1611.** Tests the pro-B reading of
   the apprenticeship constraint. Cheap, never run, and the single search most able to raise B.
4. **A departure-shaped-gap search.** Invert the method: instead of asking "which John Gurney can be
   eliminated," ask "which John Gurney household's records *stop* between 1635 and 1641 without a
   burial or probate?" That is the signature emigration leaves, and no pass has looked for it.
5. **The 1611–1615 East Dereham returns**, wherever those membranes survive — the natural birth
   window for a child of the 1611 marriage, and simply not in this image set.
6. **The Prudy re-read (D10)** and a check of what images the FS ARKs VNN2-WR2 / VNN2-WRG actually
   point to, to settle whether the "Marye and Agnes Gurney burials" exist at all.

These numbers rest on work still open — the Prudy reading wants a dedicated re-read, Marye 1618 was
not re-verified, and the crawl is not line-complete.

## What is now unsettled

- **The John Entry E attribution.** There is no `John son of ffrancis Gurnie` baptism in evidence.
  The line that carried that reading does not exist. Whether Francis Gurney G14 had a son John
  baptised at East Dereham is an open question again, and the pre-00726 pages (00693–00720) have
  never been line-scanned.
- **~~Whether `Gorne` relates to the Gurney cluster.~~ CLOSED by D8** — the surname is `Horne`, not
  `Gorne`. No name-history question arises; the index's `Gorne` is an H-read-as-G error, which is
  why the surname could never be found elsewhere.
- **The 00725 = 1615 assignment**, which was derived from the same page-per-year assumption.
- **The colonial John Gurney's birth family**, to the extent the case file leans on Entry E as
  "the strongest single anchor".

## Recommended next steps

1. Correct `research/topics/east-dereham-parish-register-paleography.md` — Entry E, the year
   anchors section, the chronology lattice, and the *filia populi* consequences paragraph.
2. Correct `site/website/key-research/east-dereham-ai-assistant-procedure.md`, which is public.
   It currently presents a four-test adjudication of a line that was never the target.
3. Re-open the John baptism as a research question and line-scan 00693–00720 for Gurney entries.
4. Re-derive the chronology lattice from in-parchment headings only, treating each return as
   multi-sheet and each sheet as twice-shot.

## Method note

The single check that would have caught all of this at any point: **re-locate the target line on
the master and read the whole line**, rather than adjudicating a token inside an inherited crop.
The crop's own text says `the daughter of` four words before the adjudicated token.

---

## Outstanding repo actions (nothing below has been done)

No edits have been made to `research/`, `fact-sheets/`, the case file, or the site. The only repo
changes from this work are the marriage image (`sources/media/nro-pd-12-1/_local/`), its
`data/sources.json` record, and `sources/validations/nro-pd-12-1-gurney-rybett-marriage-1611.md`.

| # | File | What is wrong now |
|---|---|---|
| 1 | `research/topics/east-dereham-parish-register-paleography.md` | Entry E stated as "Probable"; year anchors; chronology lattice (page-per-return); the *filia populi* consequences paragraph; Edward's year held at ±2–3 when it is now D-class 1610 |
| 2 | `site/website/key-research/east-dereham-ai-assistant-procedure.md` | **Public.** Presents a four-test adjudication of a line that was never the target |
| 3 | `research/case-files/john-gurney-case-file-v4.md` | §2 ★ baptism row; §8.1/§8.4 elimination grounds; §11 probability model at ~65% |
| 4 | `fact-sheets/g13-john-gurney-fact-sheet.md` | Note 8 publishes the same ~65% |
| 5 | `research/people/g13-john-gurney/topics/…` | `32-norfolk-parentage.md` (Entry E; Edward "about 1611/12"), `20-age-baptism.md` (baptism handle), `37-identity-assessment.md` (the four-candidate elimination summary), `31-candidate-a-aylesbury.md` (the mother-indexing claim) |
| 6 | G13 SQLite context graph | Items G13-RI-000158, G13-PM-000100, G13-PM-000109 and the probability passages carry the disproven reading |

Correcting these is a coordinated patchset, not a set of independent edits — the same claim appears
in six places at three confidence levels.

## Durable method lessons

Written to survive this thread. These generalise beyond East Dereham.

1. **Transcribe the whole line before adjudicating any token.** The disconfirming evidence was inside
   the crop the whole time — `the daughter of`, four words left of the token under test. A token
   scored for shape cannot falsify an identification; a line read left-to-right can.
2. **A record is identified by its fields, not by one field.** The index offered five checkable
   fields; the match was made on the least discriminating one (a date that recurs annually) and the
   other four were never compared. Match on the *most* discriminating field available.
3. **A forced binary with no null option manufactures its own answer.** "Is this N or ff?" scores a
   token that is neither, and scores it for whichever alternative is more permissive. Always allow
   "neither," and prefer the *less* permissive hypothesis when a shape is ambiguous.
4. **A crop without recorded coordinates stops being evidence.** It cannot be re-contextualised, and
   it silently becomes the object of study in place of the document. The workbench manifest exists
   for this; use it every time.
5. **Model diversity is not independence.** Three model families reviewing one mislocated crop
   produce one error counted three times, and the agreement actively raises confidence in it. Vary
   the *input*, not just the reader.
6. **Reconstructed procedure is not evidence of procedure.** Precision about enhancement parameters
   and pass counts, all downstream of an unevidenced identification step, reads as rigour while
   being decorative. Ask which step is load-bearing and whether *it* has evidence.
7. **Count before asserting a frequency.** The "Nicholas is a singleton" claim was false on the very
   page the analysis believed it was reading.
8. **An auxiliary hypothesis that predicts absence of evidence must not add confidence.** If a
   hypothesis explains why no record exists, no missing record can count against it — so it can only
   be supported by positive evidence, never by continued silence.
9. **Elimination by name-continuity fails in dense same-name clusters.** "Someone of this name is
   recorded here throughout" does not mean "no one of this name left," when five to seven bearers
   share the parish. Individuating records — probate, certificates, licences, company admissions —
   resist this; register continuity does not.
10. **Check which collection you are searching, not just which site.** Two FamilySearch collections
    covering the same parishes differ on whether mothers are indexed, and a methodological claim
    ("individuation is impossible here") was built on the weaker one.
11. **Verify an elimination against its fullest treatment before challenging it.** I criticised
    Candidate D from the case-file summary without reading the topic unit that carried the Boyd's
    card, and published a probability off that partial read — the same failure mode, one level up.
