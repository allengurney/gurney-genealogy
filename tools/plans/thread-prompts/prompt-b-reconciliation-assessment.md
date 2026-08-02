# Prompt B — reconciliation assessment and plan

*Written 30 July 2026, before any work. Assessment required by
`prompt-b-repo-baseline-reconciliation.md` ("Produce the assessment first").*

**Verdict: the work is genuinely too large for one turn, by a wide margin.** It is not one
reconciliation but four, and two of them (the case-file rewrite; the refactor-unit disposition) are
each a full turn on their own. A split is proposed in §5. Nothing has been changed in the repo yet
apart from this file.

---

## 1. Precondition check

`git status --short --branch` → `## main...origin/main`, one modified file:
`tools/plans/thread-prompts/prompt-b-repo-baseline-reconciliation.md` — the prompt itself, carrying
the case-file revision paragraph added for this thread. The tree is otherwise clean and the
precondition is met.

## 2. Measured scope

Everything below was counted, not estimated.

| Surface | Measure |
|---|---|
| Case file v5 | **31,910 words**, 1,226 lines, ~130 numbered footnotes; target 15,000–25,000 → a **25–50% cut plus a rewrite of §1–§5** |
| Case file v4 | 21,362 words; to be retired |
| Refactor units `50-`–`75-` | **26 units, ~610 KB, ~4,700 lines** of research prose |
| Permanent identity units `30-`–`37-` | 7 units, ~136 KB — the destination |
| Inbound `…case-file-v4` references | **386 lines across ~150 files** |
| — of which frozen (do not rewrite) | ~60 files under `sources/intake/done/`, `sources/intake/archive/`, `data/context-graphs/g13/exports/website-r244/` |
| — of which live and must be swapped | ~90 files: fact sheets, research companions, topic files, place files, `sources/validations/`, `data/sources.json` |
| Open actions in `59-` | **76 `R-nn` rows** (the prompt says 73), of which 14 are Done/closed/part-done and 62 open |
| Leads catalogue | 193 rows, highest issued **L-265** |
| Sweep datasets awaiting routing | 3 dirs, 1,888 data rows + 3 `PROGRESS.md` ledgers (~25 KB of ledger) |
| Child-record catalogue | 210 rows |
| Context graph | live DB **rev 285**, schema v3 |
| Graph website export in repo | **r244** — 41 revisions stale |
| `tools/lint_source_notes.py` | FAIL, 2 flags (both pre-existing and named in the prompt) |

## 3. Corrections to the prompt's own scope statements

Found while grounding. Each changes what the work is.

1. **Fact-sheet patchset v126 is already applied.** `sources/intake/done/v126-incorporation-campaign-factsheet-edits.patchset.md`
   carries `**Done:** 2026-07-18 09:51 PT`, and `sources/intake/processed/` holds only `stub-v127.md`
   with `Ready/` and `on-hold/` empty. The G20 1471-will and G32–G34 charter facts are in the fact
   sheets. **This scope item is closed** and should be struck, not re-checked for shape.

2. **`59-` holds 76 rows, not 73**, and they are not all leads. A material subset are **repo-edit
   instructions for this reconciliation**, not research actions — R-25 ("Rewrite the §11 asymmetry
   rationale"), R-32 ("Replace §6.1's parish-by-parish child negative"), R-40 ("Apply the revised
   probability table to the case file and the 30–37 units"), R-56, R-30, and others. Minting those as
   `L-` numbers would put this thread's own worklist into the future-research catalogue. The rows must
   be triaged into three classes before any lead number is issued:
   **(a)** research actions → real `L-` numbers, open;
   **(b)** research actions already executed with the result in the row → `L-` numbers, **closed with a
   finding**;
   **(c)** repo-edit actions → executed by this reconciliation and struck, never minted.

3. **Unit `75-` carries no WIP HTML comment.** Units `50-`–`74-` open with the
   `<!-- WIP refactor unit, July 2026 … -->` marker; `75-` does not. Any disposition pass keyed on the
   marker will silently skip the final round.

4. **§11 of the case file already carries the final 18-row table, but the prose around it is stale.**
   The rows read no-record 22 / assembled 17 / B 11 / Ackworth 9 / Cheddington 6 / not-yet-searched 5 /
   C(ii) 4 / D 4 / Epping 3 / Newgate 3 / Weston Turville 3 / Hitcham 3 / Bucks-Herts-Beds 3 /
   A(1603) 2 / Gurley 2 / C(i) 1 / Stewkley 1611 1 / other 1 — correct. But the paragraph beneath it
   still says *"no record survives at 19"* and *"Ackworth rises to 9 and Hitcham to 5"*. The table and
   its own reading disagree inside one section.

5. **`37-identity-assessment.md`'s superseded banner is itself superseded.** It quotes the tenth-pass
   table (assembled 25 / no-record 18 / B 11) as "the current table, revised 2026-07-28". Eight passes
   have moved since.

6. **`32-norfolk-parentage.md` is the most damaging live file in the repo.** Its opening bold summary
   still presents the East Dereham baptism as one of *"two primary records"* carrying the Candidate B
   claim, and still puts the parentage at **"roughly 65 percent — probable, not proven."** It has no
   superseded banner. It is the canonical Candidate B topic unit and it is published to the site as
   `topic-identity--candidate-b-norfolk-parentage`.

## 4. The reconciliation, layer by layer

### 4.1 Research layer — disposition of the 26 refactor units

The largest single body of work. Per unit: promote into `30-`–`37-`, renumber into the permanent
sequence, or retire once its content has landed. Constraints that make this slow rather than
mechanical:

- **No double-authoring.** `30-`, `31-`, `32-`, `37-` carry claims the units *correct*. The edit is a
  rewrite of the existing sentence, not a new paragraph beside it.
- **Coverage qualifiers are load-bearing.** Every negative in this body is bounded by what the
  instrument reaches. A promotion that drops the qualifier converts a bounded negative into a false
  claim. This is the single easiest way to damage the work and it must be checked per negative, not
  per file.
- **Same-pass retractions in `67-` and `69-`** (and the pass-20 retraction inside `74-` feedback point
  1) promote as the *corrected* conclusion only; the retraction trail stays in the research layer.
- **`65-` is the method file** and governs future rounds — it is a keep-and-renumber, not a promote.
- **`74-`'s 15-attribute matrix** is the most reusable artefact produced and needs a permanent home of
  its own.
- **`59-` is a worklist, not research** — it dissolves into the leads catalogue (see 4.5).

### 4.2 The two carried-forward corrections

**The variant scale.** Surname *and* forename variants are a weighted scale. Any file asserting a
spelling "is not a Gurney", or that Margaret and Mary are distinct names, needs fixing. The
sixteen catalogue rows reclassified in `69-` are restated as weighted; none removed. Known live
instances to fix: `69-` item 3 as originally written (already corrected in place), and any
`data/search-variants.json` or `sources.json` note phrased as an exclusion.

**Void negatives (R-71), retroactive.** A year bound and a place keyword cannot be combined in a
FindMyPast single-dataset (`sid=103`) query — the pair fails closed. **Every negative anywhere in the
repo resting on both at once is void.** This is a repo-wide audit across `research/`, `sources/validations/`,
`data/sources.json` notes, the fact sheets and the child-record catalogue. It is not optional cleanup
and it cannot be done by keyword alone, because most such negatives are stated in prose without the
query.

### 4.3 The case file

Five distinct jobs, in dependency order:

1. **Front matter**: `Version: 4.3` → 5; `updated: 9 June 2026` → the real date; `caseMeta` date line.
2. **§1–§5 rewritten to current thinking.** §1's baseline child list must lose "born in England" for
   Peter and Isaac; §4–§5 currently argue an East Dereham baptism that does not exist.
3. **Streamline 31,910 → 15,000–25,000 words**, plainly spoken, consumable without expertise, search
   mechanics out, sources into footnotes. §6–§11 structure kept largely as designed.
4. **No evolutionary framing.** The file is currently full of it — "New row, and immediately reduced",
   "Reduced from ~30%", "This section formerly held", "A previously stated colonial-side check is
   withdrawn". All of it goes; the file must read as one instantaneous account.
5. **Re-home every trimmed passage.** Nothing lost. Footnotes whose content is removed and not
   referenced elsewhere go to a historical-reconciliation file so no source is orphaned.

Then **retire v4**. The repo's own convention for superseded artefacts is a `_legacy/` folder with a
`BASELINE.md` (`research/people/_legacy/g13-pre-refactor/`), with a secondary pattern of a
`-to-be-deleted` filename suffix (`walter-de-gournay-as-son-of-gerard-to-be-deleted.md`). Then swap
~90 live files' inbound references from v4 to v5, leaving the ~60 frozen ones alone.

### 4.4 Source and data layers

- Route the three sweep datasets; **the `PROGRESS.md` ledgers are the load-bearing part** and must
  survive archiving of the row data.
- `data/sources.json`: register what the refactor added, keep notes to catalogue annotation (the notes
  field is neither a summary of the source nor a store of evidence); the two pre-existing lint flags
  are fixable in passing, not blockers.
- `data/ancestors.json` and `data/indexes/`.
- `research/people/g13-john-gurney/coverage/child-record-catalog.csv` — 210 rows, the evidence base.

### 4.5 Leads

Triage the 76 `R-nn` rows per §3.2, then mint through `tools/research_leads.py` from L-266, preserving
the `Online` flags (`Y` / `Part` / `N`). Reconcile against existing leads — at least one is mis-based
and several are superseded. Remember that `research-leads.csv` Status lags the subject companion:
read the companion before deciding a lead's state.

### 4.6 Fact sheets, companions, places

G13 and G14 fact sheets and companions carry probability figures, parentage statements and East
Dereham dates the new baseline changes; some carry the disproved baptism reading. Place files: only
where the new work actually says something — Epping and North Weald Bassett are newly relevant; do not
manufacture changes elsewhere.

### 4.7 Context graph and published surfaces

- Author the increment from the breadcrumb's **twenty passes**. Derive live RI/PM ids from the DB at
  authoring time — every id quoted in older notes is stale. Expect retirements and restatements, not
  only additions. `G13-RI-000153` is a known carrier of a superseded claim.
- The graph must land on the **final 18-row** probability state, not an intermediate one.
- Re-export and re-sync the website package (repo export is r244 against DB rev 285).
- `site/website/key-research/east-dereham-ai-assistant-procedure.md` is the public page presenting the
  analysis of the disproved reading — **remove from the published site, keep in the repo.**
- `site/website/key-research/john-gurney-case-file.md` is the synced v4 copy and must become v5.
- Sweep the published surface for any other dependency on the old baseline, including probability
  figures — `site/website/research/topic-identity--*.md` and the ~320 generated node pages.

## 5. Proposed split

The prompt names one seam: research+sources+case-file, then graph+published. **That is still too big
on the first side**, because the case-file rewrite and the 26-unit disposition are each a turn. Four
tranches, in strict dependency order:

**A — Research layer.** Disposition of all 26 refactor units into `30-`–`37-`; the variant-scale fix;
the retroactive R-71 void-negative audit. *Why first: the case file should be written from a settled
research layer, not alongside one.*

**B — Case file.** Rewrite, streamline, front matter, re-home trimmed content, retire v4, swap ~90
inbound references.

**C — Source, data and leads layers.** Sweep routing, `sources.json`, `ancestors.json` + indexes,
child-record catalogue, the 76-row lead triage, fact sheets and companions, place files.

**D — Graph and published surfaces.** Graph increment from twenty passes, re-export, site sync, case
file swap on the site, removal of the disproved-reading page, probability figures across the site.

A→B is a hard dependency. C can run before or after B. D must be last.

**Decided 30 July 2026.** Four tranches, A executed first and in full. Case-file content trimmed in
tranche B is to be **distributed into the matching topic units** rather than collected into a single
historical-reconciliation file — so tranche A must leave the `30-`–`39-` sequence able to receive it.

## 5a. Tranche A — executed 30 July 2026

**Disposition decision.** The 26 refactor units are **promoted, not retired**: their findings are
rewritten into a permanent `30-`–`39-` identity sequence, and the units themselves are kept as the
working record with their correction trails intact and their headers restamped. Retiring them would
have destroyed the coverage qualifiers attached to every negative; consolidating them into a
round-by-round `50-`–`75-` permanent block would have left the research layer reading as a diary,
which the repo's own prose rules forbid.

| Unit | Action |
|---|---|
| `30-candidate-overview.md` | Rewritten. Superseded banner removed. The matching-criteria profile now points at the 15-attribute shape; the three procedural corrections (households ≠ men, the child-set threshold, the uncontrolled negative) are stated; the landscape table carries the current standing |
| `31-candidate-a-aylesbury.md` | Rewritten and widened to the whole Buckinghamshire cluster. A splits into A(i)/A(ii); the probate tier, the Stewkley corrections, the Cheddington prediction, the land records and the county marriage negative all land here |
| `32-norfolk-parentage.md` | Rewritten. The East Dereham baptism is gone; 65% → 11%; Margaret's family corrected to the Garveston copyholders; the marriage parish reopened; the local-family reading made symmetric; the Weymouth asymmetry withdrawn |
| **`33-berkhamsted-candidates.md`** | **New.** C(i)/C(ii) split out of `37-`, with the sixteen burials, the four households and the two query defects |
| `34-london-draper.md` | Edited. "Eliminated" → held at 4% on an address-continuity reading; the unsearched burial route added |
| `35-candidate-ackworth.md` | Rewritten. 3% → 9%; the second-marriage condition; the untestability finding |
| `36-other-eliminations.md` | Rewritten. The variant scale, Essex opened, the West Country swept, R-47 resolutions, the households read for the first time, the Gurley partial |
| `37-identity-assessment.md` | Rewritten. Superseded banner removed; the 18-row model carried in full; the two-family structure; the Sarah logical error retired |
| **`38-the-shape-and-the-two-families.md`** | **New.** The matrix and the eight corrections |
| **`39-child-inventory-method.md`** | **New.** The method, promoted from `65-` with its retraction scaffolding removed |
| `50-`–`75-` | Headers restamped from "WIP" to completed working rounds pointing at `30-`–`39-` |

**R-71 audit result: no live negative in the repository is void.** Every recorded query string was
enumerated — 45 `sid=103`, 19 `yearofbaptism`, 28 `yearofbirth=`, 203 `keywords=`. Only two
single-dataset queries combine a year bound with a place keyword, and both were already recorded as
void. The keyword-plus-year queries at `70-` and `63-` ran in cross-collection mode, where the
combination demonstrably binds. Residual named, not closed: prose negatives with no recorded query
cannot be audited this way.

## 5b. Tranche B — executed 30 July 2026

**The case file is rewritten, cut and swapped.** Section numbering `1`–`12` and every anchor id are
deliberately unchanged, because the research layer cross-references them heavily; the rewrite happened
inside them.

| Item | Result |
|---|---|
| Length | **31,910 → 20,934 words** (13,686 body, 7,248 notes) — inside the 15,000–25,000 band |
| Front matter | `Version: 4.3` → **5**; `updated: 9 June 2026` → **30 July 2026**; `caseMeta` date corrected; `caseNav` labels rewritten in plain English |
| §1 | Rewritten. Baseline table corrected: Peter and Isaac moved to New England births; Sarah flagged as having no primary record. A short-answer paragraph added at the top |
| §2 | Rewritten and reorganised: Francis, the 1611 marriage, Margaret's family, the collapse, room for an older son. The unsourced half of the Pease tradition stated plainly |
| §3 | Timeline corrected — John's birth row is now "born, place unknown, c.1603–1608"; the register-loss window marked in the table |
| §4 | Rewritten as what the register holds and what it lost, with both loss windows and the per-return confidence |
| §5 | **Repurposed** to "The baptism that is not there" — the anchor is retained, and the section now states the finding, its cost to the hypothesis, and what survives |
| §6 | Rewritten. Four search axes, five marriage instruments, how to read the negatives, the closest households, trade, and the naming pattern |
| §7 | Cut to a short section: the Ann Gilman link is a lead, not evidence |
| §8 | Table probabilities reconciled to §11 (they disagreed on six rows). Subsections `8.1`–`8.8` kept; the `8.3` bullet list and the `8.8` clearance table compressed and grouped |
| §9–§10 | Compressed; the for/against tables cut from 18+10 rows to 12+10, each shorter |
| §11 | Table kept at 18 rows; surrounding prose rewritten — it had said 19% and "Hitcham 5" against a table reading 22% and 3% |
| §12 | Rewritten as a readable source list, with a pointer to where the supporting research lives |
| Footnotes | **Renumbered 1–71** from a broken sequence (`n1, n2, n4 …` plus `nA1`, `n92a`, `n113b`, `n115b`). Operational query strings removed; every source identification and Source ID preserved |

**v4 retired** to `research/case-files/_legacy/john-gurney-case-file-v4/` with a `BASELINE.md` recording
its hash, why it was retired, and the two passages not carried forward. **261 inbound references were
swapped** across ~60 live files; ~300 files under `sources/intake/done/`, `archive/`, `_legacy/`,
`data/context-graphs/`, `tools/plans/` and `site/` were deliberately left frozen.

**Also fixed while in the files:** the two pre-existing `sources.json` note flags (`bucks-archives-catalogue`,
`england-wales-published-probate-indexes`) — the lint now passes at 0 flagged; `tools/repo_search_config.json`,
which pointed the search tool at the moved v4 path; and three section pointers that drifted (`§6.3a` → `§6.6`
in two working rounds, `§8.6` → `§8.8` for the clearance table).

## 5c. Tranche C — executed 30 July 2026

**Published surfaces**

| File | What changed |
|---|---|
| `fact-sheets/g13-john-gurney-fact-sheet.md` | Born corrected from "c. 1607–1612, at East Dereham" to **"about 1603, in England; the place is unknown"**; page heading, subtitle, description and structured-data block all follow. The parentage bullet and narrative rewritten — the ~65% figure is gone and the identification is stated as the leading candidate, unproven. Peter and Isaac moved to New England births with a new note 16; Sarah flagged as possibly not having existed; Mary's date changed to the primary bound "born by 1631" |
| `fact-sheets/g14-francis-gurney-fact-sheet.md` | The "probable father" bullet rewritten. **Five citations that pointed at "Entry E"/"Entry A"/"Entry B"/"Entry C"/"Entry D" replaced with real record citations**, since those pointed at a case-file numbering that no longer exists and cited a repo artefact as the source. Edward's date fixed to 27 May 1610 and his mother marked uncertain; the children table now states that no baptism of a John survives |

**Research companions and topic files**

- `research/people/g14-francis-gurney-fact-sheet.research.md` — lineage-status block rewritten; the two bounds on the identification stated with a new sourced footnote.
- `research/people/g13-john-gurney/README.md` — head replaced. It still described itself as a staging area awaiting cutover. Now carries a **where-to-start table and a current-baseline block**, with everything below explicitly labelled a build log, so its ten historic "~65%" mentions no longer read as current.
- `research/people/g13-john-gurney/topics/origin/20-age-baptism.md` — substantially rewritten. It carried the withdrawn baptism as one of four birth-year handles; now the deposition is the only handle, with the 1611-marriage friction stated plainly and the figure's alt text corrected.
- `research/topics/east-dereham-parish-register-paleography.md` — the "John (case-file Entry E)" entry rewritten as **withdrawn**, with the actual images and readings given.
- `research/topics/g13-john-gurney-immigration-by-association.md` — the Aylesbury-Vale paragraph no longer subordinates itself to a ~65% Candidate B.
- `research/places/essex.md` — new section on the seventeenth-century thread. **Epping and North Weald Bassett are recorded as newly relevant places**, with the naming alternation and the void coverage negative, plus the Maldon corroboration. Human narrative kept outside the generated place-registry block.

**Leads — the 76 `R-nn` rows are folded**

- **55 open leads, `L-281`–`L-335`**, including one new lead spun off the Upton upon Severn residue.
- **15 closed leads with a finding, `L-266`–`L-280`.**
- **7 struck, not minted** — repo-edit instructions for this reconciliation, all executed.
- Descriptions held to the validator's 360-character guidance; the full reasoning stays in `59-`, which now carries the mapping table and is relabelled as the working record behind the catalogue.
- **Two integrity problems found and fixed while doing it.** Descriptions first written at 700–900 characters were re-cut to the file's own convention. And every minted lead is now **born in the open CSV** before the executed ones are moved with `close`, because `next-id` reads only the open CSV — a closed lead numbered above the open maximum would have been re-issued. Executed leads take the lower id block so `max(open) > max(done)` holds.

**Data**

- `data/ancestors.json` — G13 dates, summary and four child notes; G14 summary, five child rows and the Margaret Rybett spouse note (which asserted a single identified Margaret where the register offers two). Edited through the parsed object after verifying the dump round-trips byte-identically; 20 lines changed.
- `data/indexes/` — regenerated; they were stale, and the newest sourceId `findmypast-county-baptism-sets-2026-07-sweep` was missing from the source index.
- `data/sources.json` — the `nro-pd-86-41` note described "the disputed Entry E baptism"; rewritten to state the register's two coverage limits instead. **Note lint passes at 0 flagged.**

**Sweeps routed.** All three datasets moved to `sources/intake/archive/g13-july-2026-sweeps/` with their `PROGRESS.md` ledgers intact, 23 citations repointed, and a README explaining that the ledgers matter more than the rows.

**Also fixed in passing:** six orphan citation anchors in the G13 fact sheet whose notes carried no matching back-link.

## 5d. Tranche D — executed 1 August 2026

**Context graph and published surfaces. All four tranches are now done; the prompt is closed.**

**Graph repair (rev 285 → 344).** Validation opened at **34 errors**; every one is now cleared.
All **26 publication mappings** pointed at the retired fourth edition of the case file. They were not
repointed blindly: each was tested against what the fifth edition actually asserts, all 26 were
removed, and **32 truthful mappings** written against v5. **Five were deliberately not re-added** —
the American-arms tradition (`RI-000101`, `RI-000102`), the 1699 Nevis-will thread (`RI-000135`), and
the Bury St Edmunds burial and birthplace-clearance rows (`RI-000095`, `RI-000096`) — because the
fifth edition no longer carries them. The items survive; only the claim that a published surface
asserts them is gone. Two `research_location_invalid` errors were heading-id drift from the Tranche A
rewrites of `31-` and `36-`. Three marker tokens lost in the same rewrites (`PM-000080`, `000081`,
`000082`) were restored to the surviving passages in `36-`.

**The increment (rev 344 → 381).** Three units registered, with items and markers authored in the
same pass:

| Unit | File | Items | Markers |
|---|---|---|---|
| `g13-identity-candidate-c` | `33-berkhamsted-candidates.md` | `RI-000211..000220` | `PM-000105`, `000130`, `000135..000137` |
| `g13-identity-shape-matrix` | `38-the-shape-and-the-two-families.md` | `RI-000221..000227` | `PM-000126..000129` |
| `g13-identity-inventory-method` | `39-child-inventory-method.md` | `RI-000228..000232` | `PM-000131..000133` |

One further item, `RI-000233`, homes the variant-weighting rule in `36-` under `PM-000134`.

**Retirements and restatements, as the prompt expected.** Marker `PM-000105` and items `RI-000171`
and `RI-000172` moved from `g13-identity-assessment` to the new Berkhamsted unit, which is their
canonical home now. Eleven items carrying the superseded baseline were restated: `RI-000065` (the
child roster — Peter and Isaac American-born, Sarah doubtful), `RI-000104`, `RI-000106`
(the "sole survivor" claim), `RI-000120`, `RI-000145` (two primary records → one; confidence
`moderate` → `low`), `RI-000170`, `RI-000171`, `RI-000172` (Candidate C "eliminated" → two men),
`RI-000174` (the sixties estimate → the three record-state rows at 44%), `RI-000177`, `RI-000178`
(the 65–70% band → the five records that would move specific rows) and `RI-000194`. `RI-000159`
rested entirely on the withdrawn East Dereham entry and was rewritten to record that no baptism date
remains to be reconciled. **The graph now carries the final 18-row state.**

**Coverage ledgers closed.** The Tranche A rewrites had left the refactor's own gates red: 66
citation gaps and 66 parity gaps, because the rewritten prose cited sources the graph items never
gained. 101 rows were added to `source-and-citation-map.csv`, each dispositioned by a stated rule —
the real role where the source is on an item in that unit, `cross_unit` where its items live
elsewhere, `context_only` where no item anywhere carries it. Nine frozen inputs that tranches B and C
edited were re-frozen with their prior baselines recorded, following the precedent already set in the
ledger README. **Every gate in `g13_coverage_check.py` now passes.**

**Published surfaces.** The case file page is the fifth edition; the website package is re-exported
at revision 381 (229 public findings, 118 markers, 312 edges) and placed at `website-r381`,
`website-current` and `website`. `npm run validate` passes — 565 public pages, no broken links.
**`/key-research/east-dereham-ai-assistant-procedure.html` is off the site and kept in the repo**, at
`research/topics/_legacy/east-dereham-ai-assistant-procedure/`, with a header stating that the reading
it documents is withdrawn and that nothing in it is evidence. Its redirect stub was deleted, its nav
entry removed, and the four live repo references repointed. The AI-in-genealogy essay's link to it was
replaced with the lesson itself, written so the page is not needed to understand it. **No page on the
built site carries a sixty-five percent figure.**

**What was deliberately not changed.** `exports/website-r244` is left in place as the audit record of
the superseded export. The `sources.json` `mediaPath` for `pcc-prob11-461-dyer-lewis-nevis` points at a
directory rather than a file, which the graph reports as one `source_content_missing` warning; it
predates this work and is a registry-shape question, not a baseline question. Nineteen `repo_only`
markers in `g13-identity-candidate-b` stay out of the public export, which is a pre-existing
visibility decision. `research/case-files/Initial foundation work for.../john-gurney-case-file-v2.md`
and the retired v4 keep their old links, being frozen surfaces.

## 6. Traps to carry into every tranche

- A negative that loses its coverage qualifier becomes a false claim.
- Do not reintroduce either binary — "that spelling is not a Gurney", "Margaret is not Mary".
- Do not carry pre-retraction numbers from the breadcrumb's earlier passes; only pass 20's table.
- Do not restate the three PCC elimination rows flagged at lead L-260 until that is settled.
- Do not rewrite `sources/intake/done/`, `sources/intake/archive/`, or `exports/website-r244/` —
  they are the audit trail, not live prose.
- Leave the identification **open** at 11% for the leading named candidate and 44% across three
  record-state rows, while still presenting Candidate B as the most probable lineage, without
  caveat-clutter in reader-facing prose.
