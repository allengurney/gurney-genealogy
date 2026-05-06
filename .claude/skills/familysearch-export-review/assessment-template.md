# G{NN} — FamilySearch Intake Assessment ({Person Name}, {FS PID})

**Source artifact**: `sources/FS/{YYYYMMDD}Family{PID}.pdf` ({page count} pp., printed {date})
**Companion artifacts**: `sources/FS/{PID}/...` ({list, if any})
**Subject FS PID**: {PID}
**Repo target**: G{NN} (`research/people/g{NN}-{slug}-fact-sheet.research.md`, `fact-sheets/g{NN}-{slug}-fact-sheet.md`)
**Assessment date**: {YYYY-MM-DD}
**Disposition**: Read-only Phase 0. Precursor to a Phase-1 intake patchset.

---

## 1. Source-format anatomy

{One paragraph: dominant scholarly tradition embedded in the export (DG / FMG / Pattou / Richardson / etc.); peculiarities of this specific export; observed era-fit of the Sources layer; companion artifacts and what they add.}

---

## 2. Cross-walk: FS export vs. repo

### 2.1 Concordant facts (FS confirms repo)

- {Bullet list of facts the FS export and the repo agree on. Be specific — names, dates, places. Do not omit detail just because it is concordant.}

### 2.2 Net-new content worth promoting

For each item: state the finding in plain prose, then quote the supporting transcript verbatim (with FMG / Pattou / charter-edition reference numbers preserved), then note the destination layer (research companion, fact sheet, sources.json, places.json).

1. **{Short finding label}** — {one-sentence finding}.
   > {verbatim transcript or charter excerpt, with reference numbers like [875]}
   *Destination*: {repo file or layer}.

2. ...

### 2.3 FS conflicts with repo

| Item | FS export value | Repo value | FS sourced? | Disposition |
|---|---|---|---|---|
| {field} | {verbatim FS value} | {repo value with citation} | {Yes — cites X / No} | {repo retains / open conflict / etc.} |

### 2.4 Spurious / over-claimed structured-field content

{The "extra children" problem and similar. Identify each spurious entry and explain the likely error mode (generation slide, community-tree accretion, conflation with collateral, etc.). Cite the scholarly source that contradicts it.}

---

## 3. FS Tree update suggestions

For discrepancies where the repo's value is better and FS is unsourced, so the user can update the FS Family Tree to reduce future-pass friction.

| FS field (PID) | Current FS value | Suggested correction | Repo citation |
|---|---|---|---|
| {field on PID {x}} | {value} | {value} | {citation} |

For discrepancies where FS *is* sourced, list separately:

| FS field | FS-cited source | Repo source | Recommended action |
|---|---|---|---|
| {field} | {source} | {source} | {hold open / further research / etc.} |

---

## 4. URL triage

### Bucket A — auto-fetched
| URL | Status | Net-new content |
|---|---|---|
| {url} | fetched | {one-line summary; "redundant" if nothing new} |

### Bucket B — needs human / login (handoff list)
| URL | Expected content | Failure mode | Suggested human action |
|---|---|---|---|
| {url} | {what we expect to find} | {auth wall / JS render / cert error / FS session / paywall} | {browser visit / FS-logged-in fetch / paste back into chat} |

### Bucket C — redundant / low-value (justified skips)
| URL | Reason for skip |
|---|---|
| {url} | {already in DG / already embedded / known-aggregator / etc.} |

---

## 5. Patchset readiness sketch

Sketch only — the actual patchset belongs to `research-intake-prep` (Phase 1).

**Probable adopt**:
- {bullet list of changes by destination file, with one-line rationale}

**Decline / quarantine**:
- {bullet list with one-line reason}

**`data/sources.json` bookkeeping**:
- {new sourceIds to add, with proposed slug and URL; or "no changes"}

**Companion-file moves** (if any):
- {file move proposals; "none" if files are already in their final location}

---

## 6. Open items still requiring human judgment

1. {Three-way scholarly disagreements, claims that depend on primary sources not yet obtained, identification questions that need additional records, etc. Each item should state what would resolve it.}
