# Plan 02c — Source-registry notes remediation (G13 campaign)

Status: approved plan, not yet executed. Authored 2026-07-07 (Fable planning
session) from a grounded audit of `data/sources.json` against the pre-campaign
baseline (`e604a8d6`). Execution model: **Sonnet** for both phases (all judgment
calls are pre-made below; escalation valves included).

## 1. Problem

During the Plan 2 / Phase G3 graph-authoring campaign, source registrations in
`data/sources.json` accreted **evidence into the `notes` field**: transcription
extracts, catalogue readings, negative-search results, and project-original
identifications. The registry is a catalogue, not an evidence surface
(`.claude/rules/data-json.md`: "Do not duplicate long narrative discussion
inside JSON"). Evidence lives in the research plane (topic files, companions,
fact sheets) or the source plane (`sources/corpus_supplement/`); validations
record scope and where findings landed, not the findings themselves.

Grounded damage assessment (diff vs `e604a8d6`, confirmed 2026-07-07):

- 13 new sources registered in-campaign (~8.2k chars of notes) + 1 grown
  (`alumni-cantabrigienses-venn`, +111) + 3 campaign-adjacent from the
  `e604a8d6` property-sources commit.
- Only **4 entries exceed the 600-char lint threshold**, and spot-reads
  confirmed their content is **already carried** in the staged topic prose,
  footnotes, and validation worksheets — with **one exception**: Pope's
  "[Arch. 45]" 1646 Braintree meadows-petition lead exists **only** in the
  notes + Pope validation file (not in `research-leads.csv`, not in any topic).
- 70 **pre-existing** entries exceed 600 chars (max 2693). These are explicitly
  **out of scope** (user direction: fix only the G13-campaign entries) and are
  grandfathered via a frozen allowlist.

## 2. Principles (restated for the executor)

- Registry `notes` = 2–4 sentences: what the source is, why it is relevant,
  what kinds of information it carries. A one-line finding is permitted **only
  if the same finding is already carried in a research-plane file**.
- A finding must appear in **narrative prose** of a research file. A verbatim
  source extract quoted in a footnote is fine **when the finding it supports is
  in the narrative** (that is the normal citations.md pattern). Footnote-only
  carriage of a finding does not count as "carried."
- Validations must not be the sole home of a finding or lead.
- Best-effort standard: minimal churn beats ideal state. Do not rewrite
  entries that already comply; do not touch the 70 grandfathered entries.

## 3. Phase 1 — Guardrails (go-forward fix; run before any further increment)

### 3.1 Create `tools/lint_source_notes.py`

Write exactly this reference implementation:

```python
#!/usr/bin/env python3
"""Lint data/sources.json notes fields for evidence bloat.

Registry notes are brief catalogue annotations (what the source is, why it is
relevant, what kinds of information it carries). Evidence, transcriptions,
negative-search results, and findings live in the research plane (topic files,
companions, fact sheets) or in sources/corpus_supplement/ - never in the
registry. This lint flags notes above the threshold unless the sourceId is in
the frozen allowlist of pre-existing long entries (grandfathered 2026-07; do
not add new ids without explicit user approval).

Usage:
  .\.venv\Scripts\python.exe tools\lint_source_notes.py                 # check; exit 1 on flags
  .\.venv\Scripts\python.exe tools\lint_source_notes.py --write-allowlist
"""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCES = REPO / "data" / "sources.json"
ALLOWLIST = REPO / "tools" / "lint_source_notes_allowlist.txt"
DEFAULT_THRESHOLD = 600


def notes_len(entry):
    return len(str(entry.get("notes", "") or ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    ap.add_argument(
        "--write-allowlist",
        action="store_true",
        help="Freeze every id currently over the threshold into the allowlist.",
    )
    args = ap.parse_args()

    sources = json.loads(SOURCES.read_text(encoding="utf-8"))["sources"]
    over = sorted(
        [(sid, notes_len(s)) for sid, s in sources.items() if notes_len(s) > args.threshold],
        key=lambda x: -x[1],
    )

    if args.write_allowlist:
        lines = [
            "# Grandfathered pre-existing long-notes sources (frozen 2026-07).",
            "# Do not add new ids without explicit user approval.",
            "",
        ]
        lines += [sid for sid, _ in over]
        ALLOWLIST.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"allowlist frozen: {len(over)} ids > {args.threshold} chars")
        return 0

    allow = set()
    if ALLOWLIST.exists():
        allow = {
            ln.strip()
            for ln in ALLOWLIST.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")
        }

    flagged = [(sid, n) for sid, n in over if sid not in allow]
    for sid, n in flagged:
        print(f"FLAG {sid}: notes {n} chars > {args.threshold}")
    print(
        f"RESULT: {'FAIL' if flagged else 'PASS'} - {len(flagged)} flagged, "
        f"{len(over) - len(flagged)} grandfathered"
    )
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
```

### 3.2 Freeze the allowlist, excluding the remediation targets

1. Run `.\.venv\Scripts\python.exe tools\lint_source_notes.py --write-allowlist`
   (expect ~70 ids frozen).
2. Edit `tools/lint_source_notes_allowlist.txt` and **delete these four lines**
   (they must not be grandfathered — Phase 2 fixes them):
   - `tna-ward-c142-west-barsham-gurney-inquisitions`
   - `pope-pioneers-of-massachusetts-1900`
   - `mhs-winthrop-papers-gurdon-to-winthrop-1627`
   - `muskett-suffolk-manorial-families-v1-1900`
3. Run the lint again: it must **FAIL flagging exactly those four ids** and
   report ~66 grandfathered. (Expected state until Phase 2 completes.)

### 3.3 Edit `.claude/skills/g13-graph-authoring/SKILL.md` (three verbatim edits)

**Edit A** — in workflow step 3, after the sentence ending `— do not invent IDs.`,
append (same indentation):

```
   **Registry `notes` are a catalogue annotation, not an evidence surface** — 2–4
   sentences (soft target ≤500 chars; lint threshold 600) saying what the source is,
   why it is relevant, and what kinds of information it carries. Transcriptions,
   extracts, catalogue readings, negative-search results, and project-original
   identifications go in the topic prose/footnotes (or `sources/corpus_supplement/`);
   the validation worksheet records scope and where findings landed. A one-line
   finding may appear in `notes` only when the same finding is already carried in a
   research-plane file. After any registry edit, run
   `.\.venv\Scripts\python.exe tools\lint_source_notes.py` (expect PASS).
```

**Edit B** — in workflow step 8, extend the close-out sentence so it ends:
`…DB not ahead of recovery/snapshot), and — if the increment registered or
edited any source — tools\lint_source_notes.py (PASS).`

**Edit C** — in `## Guardrails / lessons`, insert as the **first** bullet:

```
- **Never write evidence into `data/sources.json` `notes`.** The 2026-07 remediation
  (plan 02c) relocated campaign findings that had accreted there. The registry note
  states relevance and content-type only; `tools/lint_source_notes.py` enforces the
  cap. If you are writing dates, quoted text, or reasoning into `notes`, stop — it
  belongs in the topic file.
```

### 3.4 Edit `.claude/rules/data-json.md`

Under `## Source discipline`, append this bullet:

```
- `sources.json` `notes` fields are brief catalogue annotations (what the source is,
  why it is relevant, what kinds of information it carries — roughly 2–4 sentences).
  Evidence, extracts, negative-search results, and findings belong in research
  markdown or `sources/corpus_supplement/`; a short finding may be duplicated into
  `notes` only when it is already carried in a research file.
  `tools/lint_source_notes.py` enforces a soft cap (600 chars) with a frozen
  allowlist for grandfathered pre-existing entries.
```

### 3.5 Phase 1 acceptance

- Lint runs and flags exactly the four §3.2 ids; ~66 grandfathered.
- The two rule/skill files contain the verbatim additions; no other content
  changed.
- Disclose the rule updates in the session report (continual-improvement rule).

## 4. Phase 2 — Cleanup (bounded; no graph item edits, no ledger edits)

### 4.1 Worklist (grounded 2026-07-07; sizes = notes chars)

**Rewrite (4)** — content verified duplicated in the staged topics; replace
notes with the pre-drafted texts in §4.2:

| sourceId | chars | carried in |
|---|---|---|
| `tna-ward-c142-west-barsham-gurney-inquisitions` | 1184 | `topics/origin/23-wardship-network.md` narrative + `[^ward]` + validation |
| `pope-pioneers-of-massachusetts-1900` | 1158 | `topics/family/10-wives-marriages.md` narrative + `[^pope]` (verbatim entry quoted); Newgate conflation in `topics/origin/24-bury-connections.md`; **Arch. 45 lead orphaned — see §4.3** |
| `mhs-winthrop-papers-gurdon-to-winthrop-1627` | 1121 | `topics/origin/23-wardship-network.md` narrative + `[^letter]` + validation |
| `muskett-suffolk-manorial-families-v1-1900` | 988 | `topics/origin/23-wardship-network.md` narrative + `[^muskett]` + validation |

**Verify-only (13)** — under the lint threshold; confirm each finding stated in
the notes appears in narrative prose of a research file, then leave the entry
**unedited**. If a finding is NOT carried, do **not** author narrative — record
it in the report and leave the entry unedited (escalation valve; the user
decides).

| sourceId | chars | expected home |
|---|---|---|
| `banks-planters-of-the-commonwealth-1930` | 559 | `topics/origin/22-migration-network.md` + validation |
| `alumni-cantabrigienses-venn` | 549 | `topics/origin/23-wardship-network.md` `[^warford]` (only the +111 appended Warford sentence is campaign growth) |
| `drake-result-of-researches-1860` | 546 | `topics/origin/22-migration-network.md` + validation |
| `nps-adams-nhp` | 531 | `topics/colonial/03-braintree-community.md` (Tyng farm) — campaign-adjacent (`e604a8d6`) |
| `boston-town-records-1634-1660` | 506 | colonial topics — campaign-adjacent (`e604a8d6`) |
| `shepard-spicksley-worth-age-2011` | 492 | `topics/origin/20-age-baptism.md` (methodological context) |
| `weymouth-land-grants-book-ms` | 456 | `topics/colonial/02-weymouth-community.md` — campaign-adjacent (`e604a8d6`) |
| `foster-alumni-oxonienses-1500-1714` | 452 | `topics/origin/23-wardship-network.md` `[^warford]` |
| `ancestry-english-adventurers-emigrants-1609-1660` | 428 | `topics/research-state/40-source-coverage.md` |
| `nehh-congregational-library-colonial-church-records` | 426 | `topics/research-state/40-source-coverage.md` |
| `digital-commonwealth` | 294 | `topics/research-state/40-source-coverage.md` |
| `ancestry-emigrants-in-bondage-1614-1775` | 268 | `topics/research-state/40-source-coverage.md` |
| `ancestry-child-apprentices-christs-hospital-1617-1778` | 247 | `topics/research-state/40-source-coverage.md` |

All topic paths are under `research/people/_staging/g13-john-gurney/`.

### 4.2 Pre-drafted replacement notes (use verbatim; preserve JSON escaping)

`tna-ward-c142-west-barsham-gurney-inquisitions`:

> Catalogue-level TNA Discovery descriptions of the Court of Wards (WARD 7) and
> Chancery (C 142) inquisitions post mortem for the Gurneys of West Barsham —
> the record class establishing the senior branch's tenure in capite and the
> minor-heir wardship. Key entry: Edward Gournay's inquisition C 142/613/60
> (17 Chas I). Read at catalogue level only (2026-07-01); document pulls queued
> as offline follow-ups. Findings, including the unresolved earlier 'Thomas
> Gurney' attributions, are carried in the John Gurney wardship-network
> research topic.

`pope-pioneers-of-massachusetts-1900`:

> Independent 1900 compilation of Massachusetts founders from colony, town, and
> church records; the 'GURNET, GORNET' main entry covers John of Braintree.
> Chief value: an explicit records-based ruling that the printed Braintree
> 'John Cheny, Sen.' is a typographical error for John Gurney — carried, with
> the entry text, in the wives-and-marriages research topic — plus a
> Massachusetts Archives vol. 45 meadows-petition lead (research-leads
> catalogue). Pope conflates the 1636 Newgate apprentice with the Braintree
> John; the two-Johns de-conflation post-dates him.

`mhs-winthrop-papers-gurdon-to-winthrop-1627`:

> Brampton Gurdon's 20 Oct. 1627 letter to John Winthrop (Winthrop Papers
> I:363; MHS digital edition PWF01d256) — the only Gurney-variant document in
> the Winthrop Family Papers, placing the widowed 'mrs. Gurny' and her
> near-of-age ward inside the Court of Wards circle of Winthrop and Downing.
> The full reading, the project's West Barsham identification, and its limits
> are carried in the wardship-network research topic; examination scope in the
> validation worksheet.

`muskett-suffolk-manorial-families-v1-1900`:

> Muskett's Suffolk Manorial Families vol. 1: the Gurdon-of-Assington pedigree
> (pp. 285–288) and the 1591 Martha Heigham will (pp. 289–290), grounding the
> Gurdon–Sedley–Lewkenor puritan matrix behind the 1627 Gurdon–Winthrop letter.
> No early-modern Gurney appears in the volume. Findings are carried in the
> wardship-network research topic; sweep scope in the validation worksheet.

(Each lands in the 400–560 char band. Apply with the Edit tool as a surgical
`"notes"` value replacement — do not reformat the file.)

### 4.3 Re-home the orphaned Pope lead

Add a new production lead via the tool (never hand-edit the CSV; this is a new
lead, so no `[G13-STAGING …]` tag):

1. `.\.venv\Scripts\python.exe tools\research_leads.py add --help` to get the
   field flags, then compose with `--dry-run` first.
2. Content: Massachusetts Archives vol. 45 ("[Arch. 45]" in Pope, *Pioneers of
   Massachusetts*, 1900, GURNET/GORNET entry): John Gurney signed a 1646
   Braintree petition about the meadows. Pull the petition from the
   Massachusetts State Archives colonial series (registered source
   `massachusetts-state-archives-colonial`) to confirm the signature and
   context. Subject: G13 John Gurney; source ref: Pope entry /
   `sources/validations/pope-pioneers-of-massachusetts-1900.md`.
3. Apply without `--dry-run`; record the assigned `L-###` in the report.

### 4.4 Close-out gates (all must pass)

1. **JSON validity**: `python -c "import json; json.load(open('data/sources.json', encoding='utf-8'))"`.
2. **Meta**: bump `meta.version` `1.12.0` → `1.12.1`; set `lastUpdated` to the
   execution date.
3. **Indexes**: `.\.venv\Scripts\python.exe tools\generate_id_indexes.py --check`;
   run `--write` only if it reports staleness.
4. **Graph mirror**: `.\.venv\Scripts\python.exe tools\g13_graph.py sync-sources`,
   then `validate` (expect 0 errors) and `status`. If `status` shows the DB
   ahead of recovery/snapshot, run `export --snapshot` per the skill close-out.
5. **Lint**: `tools\lint_source_notes.py` → `RESULT: PASS - 0 flagged`.
6. **Diff surface**: only `data/sources.json`, `research-leads.csv` (via tool),
   and graph export artifacts changed. Topic files, ledgers, manifest, and
   validations untouched (unless a verify-only escalation was recorded — which
   changes nothing, it is report-only).

### 4.5 Explicitly out of scope

- The ~66 grandfathered pre-existing long-notes entries.
- Thinning validation worksheets (the Pope validation carries the quoted entry
  and Arch. 45 note; acceptable as a bridge once the lead exists in the CSV).
- Coverage-ledger `notes` columns (process metadata, not reader-facing).
- Any graph item edit, marker edit, or topic-prose authoring.

## 5. Model strategy (why Sonnet for both phases)

Every judgment call is pre-made in this plan: replacement texts are drafted,
the worklist is enumerated with grounded verdicts, gates are mechanical, and
the verify-only pass has a report-don't-author escalation valve. Sonnet
succeeds when (a) the worklist is enumerated, (b) judgment is pre-made or
escapable, and (c) verification is deterministic — all true here. Hold Opus in
reserve for: reviewing the Phase 2 diff if any gate fails, and for authoring
work the valve escalates. Continue using Opus for net-new topic authoring in
the ongoing campaign.

## 6. Future work seeded by this remediation (not in scope now)

- **Batched close-out ("revision session mode")**: for multi-edit review
  campaigns, run snapshot/validate/ledger reconciliation once per session
  rather than per edit. Requires a small contract change in the skill's
  "Revising an already-committed increment" section — decide when the
  post-cutover graph-quality review is designed.
- **Graph-quality review pattern (post-cutover)**: reuse this plan's division
  of labor — deterministic inventory (local compute) → revision packet (ops
  JSON + MD edit list) authored by the strong model → mechanical application +
  gates by the cheap model. `apply-graph-edits.py` is already the application
  vehicle.

## 7. Prompts to run

**Prompt 1 (Sonnet — guardrails):**

> Read `tools/plans/G-13 Refactor/02c-source-registry-notes-remediation.md` and
> execute Phase 1 (§3) exactly: create `tools/lint_source_notes.py` from the
> embedded reference implementation, freeze the allowlist and remove the four
> §3.2 ids, and apply the verbatim edits in §3.3 and §3.4. Do not start
> Phase 2. Verify per §3.5: the lint must flag exactly the four §3.2 ids.
> Commit with message "G13 remediation Phase 1: source-notes guardrails (lint +
> skill/rule edits)". Report the lint output and a summary of each file edit,
> disclosing the rule updates.

**Prompt 2 (Sonnet — cleanup):**

> Read `tools/plans/G-13 Refactor/02c-source-registry-notes-remediation.md` and
> execute Phase 2 (§4) exactly: apply the four §4.2 replacement notes
> verbatim, add the §4.3 research lead via `tools/research_leads.py` (dry-run
> first), run the §4.1 verify-only pass over the remaining thirteen ids
> (confirm each notes-stated finding appears in narrative prose of the listed
> research file; leave entries unedited either way, recording any gap in the
> report instead of authoring), then run every §4.4 gate. Commit with message
> "G13 remediation Phase 2: relocate registry-notes evidence, trim to
> catalogue annotations". Report a before/after chars table for the four
> rewrites, the new lead id, the verify-only verdict table, and each gate
> result.
