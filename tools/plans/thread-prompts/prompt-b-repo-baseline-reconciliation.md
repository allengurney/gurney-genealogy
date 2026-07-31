# Thread prompt B — bringing the repo up to the new G13 baseline

> **STATUS, 30 July 2026 — this prompt is live, and one of four tranches is done.**
>
> The assessment this prompt asks for is at
> [`prompt-b-reconciliation-assessment.md`](prompt-b-reconciliation-assessment.md). It measured the work
> as four tranches, not one, and recorded three corrections to the scope described below.
>
> - **Tranche A — research layer: DONE.** The 26 refactor units are promoted into a permanent `30-`–`39-`
>   identity sequence (three new units authored); the seven pre-existing units are rewritten to the
>   current position and their superseded banners removed; the variant-scale binary is gone from every
>   live file; the R-71 void-negative audit is executed and returned no void negative.
> - **Tranche B — the case file: DONE.** Rewritten and cut from 31,910 to 20,934 words; front matter
>   corrected to version 5; §5 repurposed to state that no baptism of a John survives; footnotes
>   renumbered 1–71; v4 retired to `research/case-files/_legacy/` with a `BASELINE.md`; 261 inbound
>   references swapped across ~60 live files. Section numbering `1`–`12` and all anchors preserved.
> - **Tranche C — source, data and leads layers: DONE.** Both fact sheets and the research companions
>   corrected off the ~65% figure and the withdrawn East Dereham baptism; the 76 `R-nn` actions folded
>   into the lead catalogue as 55 open leads, 15 closed leads and 7 struck; the three sweep datasets
>   archived with their coverage ledgers; `ancestors.json`, `sources.json` and the ID indexes brought
>   current; Epping and North Weald Bassett recorded as newly relevant places.
> - **Tranche D — context graph and published surfaces.** Not started.
>
> **Scope corrections carried by the assessment:** fact-sheet patchset v126 is **already applied**
> (`sources/intake/done/`, stamped 18 July 2026) and should be struck from the scope below; `59-` holds
> **76** `R-nn` rows, not 73, and a material subset of them are repo-edit instructions for this
> reconciliation rather than research leads, so they must be triaged into three classes before any lead
> number is issued.

*Revised 29 July 2026, at the close of the research phase. The refactor is now **finished as research**
and unincorporated as repo state — this prompt is the incorporation. Recommended model: Opus 5. Work in
`main`, no patchset process — review will be by GitHub Desktop diff.*

**Precondition.** All open work in the repo is committed and pushed before this thread starts, so the
reconciliation lands as a clean, reviewable diff against a known baseline. Confirm that with
`git status --short --branch` before touching anything; if the tree is dirty, stop and say so.

**Scope warning.** This is a wide reconciliation across most layers of the repo, and the research body
grew substantially in the final rounds — **twenty-six refactor units, not the ten this prompt was
originally written for.** Produce the assessment first. If it shows the work is genuinely too large for
one turn, say so and propose a split before starting. The natural seam is **(1) research and source
layers plus the case-file swap**, then **(2) the context graph and the published surfaces**. Do not
start work you cannot finish and leave the repo half-reconciled.

---

The John Gurney (G13) research has reached a new baseline and the research phase is closed. The v5 case
file is the authority. A large body of supporting work sits in refactor units that were deliberately
kept out of the rest of the repo while the findings were still moving. They have stopped moving. I want
the whole repo brought into line with them.

## Ground yourself first

1. `research/case-files/john-gurney-case-file-v5.md` — §6 to §11 is the new authority. Note its §11 probability
   table: **18 rows summing to 100**, three of which are *record-state* rows rather than people and
   together hold 44%.
2. `research/people/g13-john-gurney/topics/identity/` — the **`50-` through `75-`** refactor units. Each
   names the older units it supersedes. Four of them are load-bearing for this reconciliation:
   - **`65-`** the child-inventory *method*, including the self-checks (C1–C5) and the §4a scoring
     corrections. This is the file that governs how any future round should work.
   - **`73-`** the split of the "documented but never assembled" row into two rows with different
     remedies.
   - **`74-`** the **15-attribute shape matrix** scoring every non-zero candidate, plus eight points of
     feedback on the shape. This matrix is the single most reusable artefact the refactor produced.
   - **`75-`** the final round: the Margaret retraction, the county-set sweep result, three eliminated
     households, and two instrument defects.
3. `sources/intake/g13-graph-breadcrumb.md` — the standing tracker, now **twenty passes**. It is a
   pointer file, not a content store; follow its pointers. Its "Standing note" states the
   promote-or-retire posture for the refactor units.
4. `research/people/g13-john-gurney/topics/identity/59-refactor-open-actions.md` — **73 provisional
   `R-nn` rows** in the leads CSV's own column format, awaiting real lead numbers. R-68 through R-73 are
   the newest and R-68 is the current highest-value action in the file.
5. `research/people/g13-john-gurney/coverage/child-record-catalog.csv` — **210 catalogued rows**, the
   evidence base under the child-inventory method.

**Do the assessment before the work.** Produce a written reconciliation plan first: what changes, where,
and what depends on what. Show it to me before executing if it looks larger than you expected.

## Two corrections the refactor made to itself — carry these forward

Both are retractions of claims the refactor itself published, and both matter beyond G13.

**The variant scale.** Surname and forename variants are a **weighted scale, not a binary**. An earlier
pass reclassified sixteen rows on the assertion that "Garne / Gurnett / Gurnard / Gurnel / Gurner are
other surnames"; that was conjecture from five data points across three generations with no paleographic
work, and the repo's own corpus refutes it — the 1634 Heralds' Visitation records "Richard Gurny, *alias
Gurnard*". The same error then recurred one field to the left, asserting that **Margaret is not a
variant of Mary**; that too is retracted, because `g` and `y` carry near-identical looping descenders in
this period and *Margaret* was routinely contracted to `Marg.` or `Mgt.`, so the distinguishing letter
is the ambiguous one and **the transcription chain corrupts in both directions**. Unit 74's feedback
point 1 and method §4a now carry the corrected weighting.

**Do not let reconciliation prose reintroduce either binary.** If you find a file stating that some
spelling "is not a Gurney" or that Margaret and Mary are distinct names, that file needs fixing, not
preserving.

**Void negatives.** A year bound and a place keyword **cannot be combined** in a FindMyPast
single-dataset query — the pair fails closed. **Any negative anywhere in this repo resting on both
parameters at once is void.** This is action R-71 and it is retroactive; the audit is part of this
reconciliation, not optional cleanup. Method check C2c and skill §0d record the proof.

## What needs reconciling

**The case file.** Retire v4 and make v5 the live case file — including every inbound reference across
the repo and the site. Check what the retirement convention is here rather than assuming; other
superseded artefacts in this repo have been handled in a particular way.

**The case file's own front matter is wrong** and I left it deliberately for this thread: it reads
`Version: 4.3` and `updated: 9 June 2026` on a file that is substantively v5 and was edited through late
July 2026. Fix it as part of the swap.

Case file revisions. The revisions are substantial and include updating §1 to §5 to current thinking.  The case file should be written as if all of the evidence and findings were derived instantaneously and not evolved over multiple iterations. While written objectively and balanced, the case file is intended to advocate for candidate B. If/when another candidate rises to candidate B's level, we will draft a case file for that candidate. We let the length of the case file grow as research evolved and it now needs to be streamlined from its near 37,000 words to something more readable in the 15,000 to 25,000 word range. All trimmed content should be re-homed and not lost. The wording of the case file also must be plainly spoken and consumable by an average human without expertise in the family or this repo. For footnotes or footnote content that is removed, if is it not referenced elsewhere in the repo, then add it to a historical reconciliation file (we do not want to create orphaned sources without references in research). The sections of the case file can be adjusted to fit what needs to be messaged and to aid a concise reading (although I generally like the design of sections 6 to 11 so changes in structure should be lighter in that area). The mechanics of *how* the searches were ran, discoveries made, etc. are generally not important to the case file messaging. Similarly, the sources are not generally core to the story and most references should be in footnote citations.

**The refactor units.** They carry `refactor` in the filename and an HTML comment marking them WIP and
graph-absent. Decide per unit whether to promote content into the existing `30-`–`37-` units, keep the
unit and renumber it into the permanent sequence, or retire it once its content has landed elsewhere.
**Do not double-author**: several supersede specific claims in `30-candidate-overview.md`,
`31-candidate-a-aylesbury.md`, `32-norfolk-parentage.md` and `37-identity-assessment.md` — the last two
of which already carry superseded banners — and correcting those claims is the point, not copying text
alongside them.

Two units contain **same-pass retractions in the body** (`67-` and `69-`, the latter retitled when the
variant retraction inverted its conclusion). When you promote them, promote the *corrected* conclusion
and do not carry the retraction scaffolding into reader-facing prose.

**The context graph.** Author the increment from the breadcrumb. Derive live RI/PM ids from the database
at authoring time — ids quoted in older notes are stale and must be verified before any edit. Expect
retirements and restatements, not only additions. The probability table changed repeatedly through July;
the graph should carry the final 18-row state, not an intermediate one.

**Structured data.** `data/ancestors.json` and the `data/indexes/` lookups; the sourceIds added by the
refactor work, of which the newest is `findmypast-county-baptism-sets-2026-07-sweep` (registered, with a
validation worksheet); `data/sources.json` notes discipline — catalogue annotation only, never evidence.
`tools/lint_source_notes.py` currently reports **two pre-existing flags**, `bucks-archives-catalogue`
(711 chars) and `england-wales-published-probate-indexes` (604 chars). Neither is refactor work; fix them
if you are in the file anyway, but they are not a blocker. Note that the notes field is not intended to be a summary of the source and our use and not as a listing of or repository for evidence.  

**Raw sweep data awaiting routing.** Three working datasets sit in `sources/intake/new/` and have been
cited from the research layer but never triaged:
`freereg-g13-sweep-2026-07-28/` (585 rows), `fmp-parent-sweep-2026-07-28/` (598 rows) and
`fmp-county-sweep-2026-07-29/` (705 rows). Each has a `PROGRESS.md` coverage ledger that is the
load-bearing part — it records which queries were capped, which sets do not exist, and which zeros are
uninterpretable. **Do not discard the ledgers when archiving the row data.**

**Fact sheets and research companions.** The G13 and G14 fact sheets and their research companions carry
probability figures, parentage statements, and East Dereham dates that the new baseline changes. Some
carry a specific baptism reading that has been disproved. There is also a **fact-sheet patchset v126**
outstanding from the earlier non-G13 campaign (G20 1471-will and G32–G34 charter facts); check whether
it is still the right shape before applying it, since the repo has moved since it was drafted.

**Place files.** Check whether any are affected — several parishes gained or lost significance, and
Epping and North Weald Bassett are newly relevant — but do not manufacture changes where the new work
says nothing new about a place.

**Leads.** Fold the 73 provisional `R-nn` rows into `research/future-research/research-leads.csv` with
real lead numbers issued by `tools/research_leads.py`, preserving the offline-only flags. Reconcile
against existing leads: at least one is known to be mis-based and several others are superseded. Note
that many `R-nn` rows are already **Done** with their result recorded in the row — those become closed
leads with a finding, not open ones.

**The site.** At least one public page presents an analysis of a reading that has been disproved (remove it from the published site but keep it in the repo). Check what else on the published surface depends on the old baseline, including any probability figure.

## Where the research actually stands — do not overstate it either way

The identification is **open**, and the reconciliation must leave it open:

- The leading *named* candidate (B, son of Francis and Margaret Rybett) is at **11%**.
- Three **record-state** rows — documented-but-unassembled 17%, no-record 22%, documented-in-an-unsearched-source
  5% — together hold **44%**, more than every named candidate combined.
- The central structural finding of unit 74 is that candidates split into **two disjoint families**:
  documented *households* with the wrong shape, and documented *men* with no household at all. **No
  candidate is in both.** The emigrant needs a man of the right age *and* his household, and every
  candidate supplies one half.

Files that still imply a settled identification need to stop implying it. Equally, do not inflate the
uncertainty into "nothing is known" — a great deal was eliminated, and the eliminations are findings.

The bottom line: With no other candidate above candidate B, he is still presented as the most probable lineage.  What I don't want to see is extensive "clutter" for the reader of our published material meaning extra prose, caveating, complicated wording, lengthy conditions, etc. for item after item in a narration. Genealogy (particularly going back hundreds of years) is an imprecise accounting so while we strive not to misrepresent, we should also recognize that there's inference needed and we do the best we can...and it has to be consumable for reading (and even enjoyment). If/when we have a candidate with a sufficiently higher probability, we can explore how we present that in the library at that time.    

## How I want you to work

- **Follow the repo's own layer discipline.** Findings in research, sources in sources, catalogue
  annotations in `sources.json` notes, evidence never sourced to the repo's own artefacts. Read the
  rules in `.claude/rules/` for the paths you touch.
- **Prose quality matters as much as correctness.** A reconciled file should read as one current account,
  not as a new paragraph bolted onto an old one. Where a finding corrects an earlier statement, rewrite
  that statement — do not leave both standing with a note. Preserve every citation through the merge.
- **No evolutionary framing in reader-facing prose.** Document current state. Not "this was previously
  thought" or "has now been revised" — just what is true, with the evidence. *(The refactor units
  themselves are the exception: their retraction trail is deliberate and belongs to the research layer.)*
- **Use `tools/repo_search.py`, never grep**, to find every inbound reference before you move or retire
  anything. `locate` does not accept alternation — one term per call.
- **Preserve the coverage statements.** Every negative in this body of work is qualified by what was
  searched and what the instrument can reach. A negative that loses its coverage qualifier during
  promotion becomes a false claim. This is the single easiest way to damage the work.

## Finishing

Report what changed, layer by layer, and — separately and explicitly — **what you deliberately did not
change and why**. If anything is left inconsistent, name it rather than letting me find it in a diff.

Then update this prompt file, or retire it, depending on what is left.
