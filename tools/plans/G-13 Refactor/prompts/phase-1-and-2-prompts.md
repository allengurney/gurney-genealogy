# Prompts — Phase 1 (source registrations) and Phase 2 (five revision increments)

Session-start prompts for the two phases of post-authoring G13 work. All 25 topic
units are authored and `increment-complete`; the `/g13-graph-authoring` **creation**
path is finished. Everything below is either that skill's **revision** path (editor
ops via `apply-graph-edits.py`, never `author-batch`), pure source registration, or
both.

Backlog at the time of writing: 85 rows (18 legacy, 56 dump, 11 supplemental).

## Sequence and ownership

| # | Work | Model | Depends on |
|---|---|---|---|
| Phase 1 | Register three gating sources | Sonnet | — |
| 2.1 | `g13-colonial-record-coverage` — colony-level negative catalogue | Opus | Phase 1 |
| 2.2 | `g13-colonial-braintree-community` — 1646 meadows petition + Brackett vector | Opus | Phase 1 |
| 2.3 | `g13-origin-wardship-network` — four English-network rows (+ Bury F-R3.11) | Opus | Phase 1 (for F-R3.11 only) |
| 2.4 | `g13-origin-migration-network` — Jenner, Ann Gurney × Gilman, Bucks cluster | Opus | — |
| 2.5 | `g13-identity-candidate-b` + `g13-identity-assessment` — case-file §6 and residual §10 | Opus | — |

Run Phase 1 first. 2.4 and 2.5 are unblocked today and can run in parallel with it.

## Standing rules that apply to every prompt below

- **The case file is not a source.** `research/case-files/john-gurney-case-file-v4.md`
  is a publication surface. Never cite it, the fact sheet, or any other repo artifact
  as the source of truth for evidence or a finding. Cross-references for reader
  convenience are welcome and must open with "Cross-reference, not a source." Every
  evidence footnote leads with a third-party record and a registered `Source ID`.
  (This rule was applied across the staged topics on 2026-07-10; do not regress it.)
- **The §8.6 collective-set exception.** The dense clearance list of eliminated same-name
  Johns is carried as one collective finding with the case file's §8.3/§8.6 tables named
  as the master list. Do not expand it into per-household items.
- Revision path, not creation: `author-batch` only *creates* and collides on an existing
  `item_id`. Use `.\.venv\Scripts\python.exe .claude/skills/g13-graph-authoring/apply-graph-edits.py <ops.json>`.
  Each op is its own transaction — there is no dry-run — so order ops so an earlier one
  cannot strand a later one, and pass `locator` in the same `add_source_link` op.
- Close out every session: `hash-sources` (if new local sources) → `export --snapshot` →
  `validate` (**0/0**) → `status` (tiers aligned) → coverage-ledger rows →
  `g13_coverage_check.py`. Per-increment gates must all read 0; the whole-refactor
  `RESULT: FAIL` on backlog is expected and is not yours to clear.
- Escalation valve: if a row cannot be dispositioned truthfully — the source will not
  support the claim, the destination is wrong, the finding is already homed elsewhere —
  **report it and leave it in backlog**. Do not false-close and do not invent a citation.

---

## Phase 1 — unblock the source registrations - DONE

*Model: Sonnet. Mechanical, enumerated worklist, hard gate is the lint.*

```
Work in main. Task: register three sources in data/sources.json that gate downstream G13
work. Registration + a validation worksheet each. No graph writes, no topic-prose edits.

Read first: .claude/rules/sources.md, .claude/rules/citations.md, and the memory note on
sources.json notes discipline — `notes` is a 2–4 sentence catalogue annotation (what the
source is, why it is relevant, what kinds of information it carries), never an evidence
surface. Never embed findings, transcripts, or negative-search results in `notes`.

Register exactly these three, and nothing else:

1. `csm-39-boston-first-church` — Publications of the Colonial Society of Massachusetts,
   vol. 39: The Records of the First Church in Boston, 1630–1868, ed. Richard D. Pierce
   (Boston: CSM, 1961). Gates dump finding F-R4.2, the Boston First Church zero — the
   negative that would close Anderson's "Boston" settlement attribution on the record
   rather than by inference.

2. Massachusetts Archives vol. 45 (Colonial series, "Military"). Gates F-R4.1, the imaged
   1646 Braintree meadows petition with Henry Adams as co-petitioner. Note that a generic
   `massachusetts-state-archives-colonial` entry already exists; decide whether the volume
   warrants its own id (it does if you are citing a specific imaged petition at folio
   level) and if so mint `massachusetts-archives-vol-45-...` rather than overloading the
   generic entry. State your decision in the report.

3. `muskett-suffolk-manorial-families-v3-1900` — Joseph James Muskett, Suffolk Manorial
   Families, vol. 3 pt. 1 (Chaplin of Semer/Bury pedigree). Gates F-R3.11 (the 1672 Bury
   will of Chaplin naming "Mary Gurney my servant", plus the Houchin New England debt).
   Volumes 1 and 2 are already registered — match their shape.

For each: a `sources/validations/<sourceId>.md` worksheet recording what was examined,
at what level (image / transcript / catalogue / index), the scope searched, and where the
findings will land. If you cannot confirm a bibliographic detail, say so in the worksheet
rather than guessing it.

Then: bump `data/sources.json` meta.version (minor) and lastUpdated; run
`.\.venv\Scripts\python.exe tools\lint_source_notes.py` (must PASS);
run `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --write` and re-verify;
run `.\.venv\Scripts\python.exe tools\g13_graph.py sync-sources` then `validate` (0/0).

Do NOT edit any topic prose, any research item, or any coverage ledger. Report: the three
ids, the vol.45 decision, the lint/validate/index results, and anything you could not
confirm. `muskett-…-v2` is already registered, so F-R3.9 needs no registration work.
```

---

## Phase 2.1 — `g13-colonial-record-coverage`: the colony-level negative catalogue - DONE

*Model: Opus. Nine rows; the largest single revision. Depends on Phase 1.*

```
Work in main. Task: one bounded REVISION increment on the already-authored, already-
committed topic unit `g13-colonial-record-coverage`
(research/people/_staging/g13-john-gurney/topics/colonial/06-record-coverage.md).

Read first: the "Revising an already-committed increment" section of the
/g13-graph-authoring skill (editor ops via apply-graph-edits.py — author-batch only
creates), plus tools/plans/G-13 Refactor/02b-source-lossless-topic-assimilation.md §8.

Assimilate the colony-level negative catalogue this unit deliberately left in backlog:
dump findings F6, F8, F-R4, F-R3.4, F-R4.2, F-R4.11, plus the record-coverage facets of
F11 and F-R6. Read each row's ledger annotation in
research/people/_staging/g13-john-gurney/coverage/dump-findings-map.csv before deciding
its kind — several are explicitly partial, with another unit already holding a sibling
facet, and those annotations are authoritative over any summary.

Scope discipline: this unit is the SHAPE of John's surviving colonial documentary
footprint, not the substance of any record. F-R4.2 (Boston First Church zero) is the
headline: it converts Anderson's "Boston" settlement attribution from an inference-level
qualification into a record-level negative. It needs `csm-39-boston-first-church`
registered — verify that Phase 1 landed before you start, and stop if it did not.

`negative_result` items each require a structured negative_result_scope. Through
apply-graph-edits.py's `set_negative_scope`, `limitations` is a real JSON list (the
runner encodes it) — unlike author-batch, where `limitations_json` must be a pre-encoded
string.

New items go in via author-batch (they are creations); statement edits, source links, and
relations on the seven existing items RI-000038..000042 go through editor ops. Mirror
every graph change into the topic prose and its marker tokens in the same pass.

Cross-check each new finding's direct item_sources against what the fact sheet and case
file actually cite for the same claim — a finding sourced only through its relation chain
can silently omit a witness, and g13_coverage_check.py will not catch it.

Close out per the skill. Report the item/marker ids, the revision range, the snapshot,
and any row you left in backlog with the reason.
```

---

## Phase 2.2 — `g13-colonial-braintree-community`: the 1646 petition and the Bracketts - DONE

*Model: Opus. Two rows. Depends on Phase 1.*

```
Work in main. Task: one bounded REVISION increment on `g13-colonial-braintree-community`
(topics/colonial/03-braintree-community.md), per the /g13-graph-authoring skill's
"Revising an already-committed increment" section.

Two backlog rows:

- F-R4.1 — the imaged 1646 Braintree meadows petition, with Henry Adams among the
  co-petitioners. The ledger notes this is DISTINCT from the 1645 plantation petition
  already carried in this unit (see the existing open_question on that petition's primary
  source) — do not conflate them. Needs the Massachusetts Archives vol. 45 source from
  Phase 1; verify it landed and stop if it did not. Cite the folio/image, not the volume.

- F-R4.6 — the Brackett brothers as a Sudbury/Gurdon relationship vector. Compiled-level
  evidence. Weigh it honestly: this is a network suggestion, not a documented tie to John,
  and the wardship unit already holds the Gurdon-Winthrop material. If its real home is
  `g13-origin-wardship-network` or `g13-origin-migration-network`, re-route it in the
  ledger and say so rather than forcing it in here.

Do not let a synthesis flourish outrun the evidence: residence, wealth, and standing
claims each need per-record support. Peter Brackett solemnized John's 1661 marriage — that
is a fact; a Gurdon relationship vector through his brothers is a hypothesis.

Close out per the skill (hash-sources → snapshot → validate 0/0 → status → ledgers →
g13_coverage_check.py, per-increment gates all 0). Report what you assimilated, what you
re-routed, and what stayed backlog.
```

---

## Phase 2.3 — `g13-origin-wardship-network`: four English-network rows - DONE

*Model: Opus. Four rows, one coherent unit. Phase 1 gates only the Bury fold-in.*

```
Work in main. Task: one bounded REVISION increment on `g13-origin-wardship-network`
(topics/origin/23-wardship-network.md), per the /g13-graph-authoring skill's
"Revising an already-committed increment" section.

Four backlog rows, all Norfolk senior-branch / Court of Wards material:

- F-R3.6 — the West Barsham advowson. Re-routed here off bury-connections on 2026-07-07.
  This is the patron-side lever on the 1627–28 "Warford" institution that the unit's own
  open_question RI-000085 leaves open. Blomefield records the Gurney advowson; the
  Clergy of the Church of England Database indexes the Norwich diocesan institution books.
- F-R3.7 — Adam Winthrop's diary (Lewkenor deaths, 1605). The Warford spelling-variant
  point is already reflected in RI-000085; the diary detail itself is not yet homed.
- F-R3.9 — the L'Estrange jest-book, kin-sourced: Sir Nicholas L'Estrange married Anne
  Lewkenor, niece of Martha (Lewkenor) Gurney and first cousin of Edward Gournay. This
  upgrades the Thoms anecdotes from hearsay to kin-sourced testimony. `muskett-…-v2` is
  already registered; no Phase 1 dependency.
- F-R3.2 — Martha Heigham's will. The Denham puritan-matrix bearing is already assimilated
  as RI-000082; read the ledger annotation and take only what is genuinely unhomed.

Then, IF Phase 1 registered `muskett-suffolk-manorial-families-v3-1900`, fold F-R3.11 into
`g13-origin-bury-connections` in the same session: the 1672 Bury will of Chaplin naming
"Mary Gurney my servant", plus the Houchin New England debt. If Phase 1 did not land,
leave F-R3.11 in backlog and say so.

Hold the line the unit already holds: this network attaches to the SENIOR West Barsham
branch, not to John. RI-000084 says so explicitly. Nothing here identifies the emigrant,
and no new item may imply that it does.

Close out per the skill. Report items, revisions, snapshot, and backlog left standing.
```

---

## Phase 2.4 — `g13-origin-migration-network`: Jenner, Ann Gurney, the Bucks cluster - DONE

*Model: Opus. Unblocked today.*

```
Work in main. Task: one bounded REVISION increment on `g13-origin-migration-network`
(topics/origin/22-migration-network.md), per the /g13-graph-authoring skill's
"Revising an already-committed increment" section.

Three inputs:

- F-R4.5 — Rev. Thomas Jenner. Read the ledger annotation first: Jenner's WEYMOUTH bearing
  is already carried in the Weymouth unit (RI-000020, the 1644 "Mr Ginner" bill;
  RI-000021, the credit tie). Take only the migration/corridor bearing, if there is one,
  and leave the rest where it lives. One home per conclusion.

- Case file §7 — Ann Gurney × John Gilman, married Hingham, Norfolk, 1 October 1626; a
  worsted-weaver's family; children baptised at West Dereham and Hingham; Ann buried
  Hingham 23 November 1651; their son John Jr. emigrated to Exeter, New Hampshire. If Ann
  was John's sister, this puts a second sibling on the Norfolk-to-New-England corridor.
  This section has NO staged home anywhere in the graph today — it is a genuine content
  gap, not a duplicate. Cite the Hingham register, Blomefield, Davis's Ancestry of Abel
  Lunt, and Pease directly (Source IDs `hingham-register`, `blomefield-norfolk`,
  `davis-abel-lunt-1963`, `pease-pennyghael`); the case file is a cross-reference only.
  Watch the West Dereham / East Dereham trap — twenty miles apart, different part of the
  county — and note the separately recorded Ann Gurney who married at West Dereham in
  1618/19 and may be a different woman. Ann's sisterhood is Pease's claim, not a record's:
  author it at the confidence the evidence carries, most likely a research_finding at
  moderate confidence or an open_question, not an established kinship.

- The immigration-by-association topic's Aylesbury-Vale Buckinghamshire neighbour cluster.
  Its Weymouth reception bearing is already RI-000046 in the Weymouth unit and RI-000090
  here; check before authoring, and take only what is unhomed.

Close out per the skill. Report what you took, what you left, and the confidence you gave
the Ann Gurney sisterhood with your reasoning.
```

---

## Phase 2.5 — `g13-identity-candidate-b` + `g13-identity-assessment`: case-file §6 and §10 - DONE

*Model: Opus. The last identity work. Unblocked today.*

```
Work in main. Task: one bounded REVISION increment across two already-authored units,
`g13-identity-candidate-b` (topics/identity/32-norfolk-parentage.md) and
`g13-identity-assessment` (topics/identity/37-identity-assessment.md), per the
/g13-graph-authoring skill's "Revising an already-committed increment" section.

The 2026-07-10 case-file-as-source repair confirmed that case file §6 is the one
substantive identity section with no staged home. Three sub-parts, all currently cited
only as cross-references:

- §6.1 The children search matrix. No indexed English parish cluster matches the colonial
  John's full family signature (Sarah, Mary, Richard, John Jr., Peter) 1620–1640, across
  20+ Gurney baptisms reviewed in FamilySearch, Findmypast, and Ancestry. The closest
  clusters (Berkhamsted, Aylesbury, Hitcham, Eythorne, Toddington, Ackworth) are weak on
  dates, mother's name, or both. This is a `negative_result` with a real
  negative_result_scope, NOT a finding that the children were born in Massachusetts.
  The wildcard-level marriage negative is already RI-000064 — do not re-author it.

- §6.2 The Peter naming gap. Of twelve indexed Peter-Gurney-variant baptisms 1632–1640
  across Findmypast UK Parish Baptisms, none was fathered by a John Gurney. Note the
  qualifier the case file's own §10.1 row 8 carries: Peter is not absolutely absent from
  Norfolk Gurney households (1641 Smallburgh, Peter Gurney son of Peter). The inference —
  that Peter most likely entered through Mary's kin — is an `analysis`, and it links to
  the standing open_question on Mary's identity, RI-000055.

- §6.3 The absence of a son named Francis. The strongest naming-pattern argument AGAINST
  Candidate B. It is currently named as an offset in both units' prose with no item of its
  own. Author it as a first-class item in `g13-identity-candidate-b` — a negative that
  QUALIFIES the parentage hypothesis RI-000145 — and let RI-000170's weighing depend on it.
  The case file's four candidate explanations (estrangement, the name's association with
  ruin, maternal naming priority, a dead earlier child) are hypotheses, not evidence:
  carry them as such or not at all.

Also sweep the residual case-file §10 identity facets still in backlog on the supplemental
ledger's s10 row — the trade/corridor/motive/network narrative recap, the Coleman Street
adjacency, and the John-of-Maldon second-son datum — and either home them or annotate why
they stay. Several are already carried; check RI-000145..000170 before authoring anything.

Two hard constraints. First, the ~65% probability model stays external-canonical to the
case file: cross-reference it, never restate it as a graph fact. Second, the case file is
not a source — every new item cites its own third-party record.

Close out per the skill. Report items, revisions, snapshot, the backlog rows you closed,
and whether the assessment unit's offsets footnote still reads correctly after the new
items land.
```

---

## After Phase 2

Phases 3–7 are drafted in [`phase-3-to-7-prompts.md`](phase-3-to-7-prompts.md): the
small-rows sweep (Sonnet), the false-friends registry (Sonnet), out-of-scope routing
(Sonnet — the cheapest large win, 35 dump rows to `routed`), the root hub plus
legacy/supplemental ledger closeout (Opus, two sub-phases), and cutover (Opus, gated,
irreversible; prompt in `cutover.md`). Allen took the two standing cutover decisions on
2026-07-10: the fact sheet's "roughly a sixty percent probability" is updated to the case
file's / topic files' ~65% as part of the cutover change, and the identity units stay
`public`.
