# East Dereham PD 86/41 page 00715 — re-read prompt pack

**Target.** The baptism entry currently read as "John the sonne of ffrancis Gurnie," Norfolk
Record Office PD 86/41, page 00715. Master image held at
`sources/media/Parish_Register_East_Dereham/gbprs_norfolk_pd_86-41_00715.jpg` (5048 × 4272,
8-bit grayscale JPEG).

**Why re-read.** The 2026 analysis adjudicated one question only — whether the father's name
reads `ffrancis` or `Nicholas` — across four letterform tests, all of which favoured
`ffrancis`. It never examined the **relationship and status wording**, because nobody was
looking for it. Three current questions turn on that wording: whether the clerk marked the
child's status, whether a mother is named, and what year the page belongs to.

---

## Two findings from this session that must be built into the re-read

### 1. This page contains a same-hand illegitimacy exemplar

About a third of the way down the christenings column, at approximately
`x 1800, y 1955, width 1250, height 80` in the master, sits:

> **"Alyce the daughter of Jane Iewell *filia populi* bapt: Febr 11"**

*Filia populi* — "daughter of the people" — is the standard Latin formula for an illegitimate
child. **The clerk of this page had a convention for marking illegitimacy and used it**, and
the shape of that convention is visible: **the mother is named, no father appears, and the
Latin tag follows the parent's name.**

This is the single most useful control available. Any assessment of the John entry should be
made *against* this exemplar rather than against general period practice. It also raises the
evidential weight of a plain entry: a clerk who marks status when it applies is a clerk whose
silence means something.

### 2. The page has a "Mariages" subsection — the layout claim needs revisiting

The current topic file states that pages before image 00726 "use a different layout (not yet
fully characterized)" and that the year-anchored chronology lattice cannot be extended back to
them. But page 00715 plainly shows a christenings column followed by an inline **"Mariages"**
header and marriage entries — the same combined-annual-return structure the lattice is built
on. If that structure runs back to 00715, the lattice logic may extend backwards, which bears
directly on the ±2–3 year margin around the birth date.

---

## Image constraints — read this before blaming the model

The master is 5048 × 4272, but **the parchment strip occupies only about a quarter of the
frame width**; the text column runs roughly `x 1700–3000`. Two archival caption cards ("Soiled
Document", "Faded Document") take up much of the left half. Effective resolution on the
writing is therefore far lower than the pixel dimensions suggest, and the file is a
heavily-compressed JPEG (1.3 MB for 21.5 megapixels), so fine stroke detail carries
compression artefacts.

**If the passes below come back indecisive, the binding constraint is the image, not the
prompt.** Better images to seek, in order: the FamilySearch image at full resolution; the
Ancestry image-backed Norfolk collection, which serves whole registers as high-quality pieces;
or the Norfolk Record Office original.

---

## Pass 0 — image preparation (no model judgement)

Run with the repo workbench so crops are reproducible:

```
.venv/Scripts/python.exe tools/paleography_image_workbench.py grid <master> --out <out>/p00715-grid.png
```

Then produce, from the master and not from any existing derived crop:

1. **Locator block** — the John line with the three lines above and below, for context and rhythm.
2. **Reading strip** — the John line alone, `--scale 5`, generous vertical padding for ascenders and descenders.
3. **Head-zone token crop** — from the left margin through the word `sonne`, `--scale 8`. This is where an inserted status word would sit.
4. **Tail-zone token crop** — from the surname through the end of line, `--scale 8`, to catch a second name, an `and`, or a marginal addition.
5. **Control strip** — the *filia populi* line at the same scale as (2).
6. **Comparator set** — six ordinary `the sonne of` / `the daughter of` lines from the same page at the same scale.
7. **Page head and foot** — any in-parchment heading, year, or regnal formula.

---

## Pass A — blind open transcription (run first, on 2–3 models independently)

Give **only** the reading strip from Pass 0 step 2. Give no names, no hypothesis, no project
context. Do not mention Gurney, Francis, Nicholas, or the possibility of illegitimacy.

> This is a single line from an English parish register of the early seventeenth century,
> written in secretary hand. Transcribe it word by word, exactly as written, preserving
> original spelling and abbreviation.
>
> For each word, state your confidence as high, medium, or low. Where you cannot read a word,
> write `[illegible]` and describe what you can see of it — how many letters or minims,
> ascenders, descenders, and any distinctive letterforms.
>
> Then answer three questions separately:
> 1. How many discrete word-units are on the line, counting `[illegible]` items?
> 2. Is any word abbreviated or superscripted, and if so which?
> 3. Is there anything written above, below, or in the margin beside this line?
>
> Do not guess at names to make the line read smoothly. If a word is ambiguous, say so and give
> the alternatives you can support from the strokes.

**Why blind.** The prior analysis was hypothesis-driven — it tested `ffrancis` against
`Nicholas`. A test framed that way cannot surface a word neither option contains. An open
transcription can.

## Pass B — structural spacing test (same models, still blind)

Give the **head-zone token crop** (Pass 0 step 3) plus **three of the comparator lines** (step
6), unlabelled and in randomised order.

> These are four crops from the same page of one parish register, in the same hand, each
> showing the opening of a baptism entry.
>
> For each crop, list the word-units between the child's forename and the word `sonne` or
> `daughter`. Then say whether all four crops have the same structure, or whether any one
> carries an extra word-unit the others lack.
>
> Judge on stroke groups and spacing, not on what you expect the sentence to say.

## Pass C — status-formula test (run only after A and B, hypothesis-aware)

Give the reading strip, the head- and tail-zone crops, **and the *filia populi* control strip**,
labelled this time.

> The final crop is an entry from the same page and hand recording an illegitimate child. It
> reads "Alyce the daughter of Jane Iewell filia populi bapt: Febr 11" — the mother is named,
> no father appears, and the Latin tag `filia populi` follows.
>
> Against that exemplar, assess the target entry:
> 1. Does the target name a father, a mother, or both?
> 2. Is any Latin tag present — `filius populi`, `filia populi`, `ignotus`, or similar?
> 3. Is any English qualifier present — `base`, `baseborne`, `bastard`, `begotten`?
> 4. Does the target's structure match the ordinary entries on the page, or the exemplar?
>
> State separately what the strokes **support**, what they **refute**, and what they **cannot
> decide**. Refutation is as valuable as confirmation here.

## Pass D — year and page-position test

Give the page head and foot crops, the grid, and the locator block.

> This page is from an English parish register kept in annual returns, each covering 25 March
> to 24 March. Identify any heading, year, regnal formula, or date sequence that would fix
> which year this page belongs to. Report the first and last dated entries visible in the
> christenings column and the order of months, so the year boundary can be located. Distinguish
> anything written on the parchment from anything written outside its edge, which will be a
> modern archivist's annotation and must not be used for dating.

---

## Model choice

The original analysis was done in **ChatGPT (March 2026)**. For a genuine second opinion,
independence of model family matters more than any single model's strength.

| Pass | Model | Reason |
|---|---|---|
| A, B | **Claude Opus 4.8**, **a GPT-5-class model**, and **Gemini 2.5/3 Pro** — run separately, results compared | Blind transcription is where model diversity pays. Agreement across families is strong evidence; disagreement localises the hard word. Weight the non-ChatGPT results, since ChatGPT produced the reading under test. |
| C | **Claude Opus 4.8** with the paleography workbench | Needs iterative crop generation against the control, which benefits from tool use and repo context. |
| D | **Claude Opus 4.8** | Structural and sequential reasoning over the whole page rather than fine letterform work. |

Run A and B **before** anyone sees Pass C's framing. Once a model has been told illegitimacy is
in question, its transcription is no longer independent evidence.

---

## What each outcome would mean

- **Plain entry, father named, no qualifier, structure matching the ordinary lines.** Given the
  *filia populi* control on the same page, this is positive evidence of legitimacy, not merely
  absence of evidence. The illegitimacy hypothesis in the childhood case file §5A should be
  withdrawn, and the birth date pushed back toward the marriage.
- **An extra word-unit before `sonne`, or a Latin tag, or a named mother.** The §5A hypothesis
  moves from speculation to a supported reading, and Margaret's motherhood needs re-examining.
- **Indecisive.** The image is the limit. Pursue a better scan before spending more model time.

---

## Cross-references

*Cross-references, not sources.*

- Prior procedure and the four letterform tests: `site/website/key-research/east-dereham-ai-assistant-procedure.md`
- Register structure, year anchors, household entries: `research/topics/east-dereham-parish-register-paleography.md`
- The hypothesis under test: `research/case-files/john-gurney-g13-childhood.md` §5A
- Working crops from this session: `sources/intake/paleography-staging/working-snippets/packet-56/`
