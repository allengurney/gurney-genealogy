# G13 Cutover Difference Report

**Cutover date:** 2026-07-13  
**Scope:** promotion of the reviewed John Gurney package only. This report is
retained with the package through Allen's acceptance window and supplements the
three detailed coverage ledgers.

## Content coverage

| Surface | Result | Difference retained |
|---|---:|---|
| Legacy companion | 41/41 blocks dispositioned | Exact pre-cutover copy retained at `research/people/_legacy/g13-pre-refactor/`; conventional root is now a pointer to the library. |
| Intake dumps | 83/83 findings dispositioned | Raw dumps remain unchanged; destinations and exceptions remain in `dump-findings-map.csv`. |
| Supplemental publication/case-file surfaces | 60/60 dispositioned | The fact sheet, case file, and retained legacy map remain crosswalked in `supplemental-surfaces-map.csv`. |

There are zero un-dispositioned blocks, zero citation gaps, and no missing or
un-enumerated frozen inputs. The promoted library is the substantive front door:
`topics/00-research-library.md`.

## Evidence coverage

The final coverage check reports zero input-source-set, source-journey,
topic/graph source-parity, publication-mapping, and source-registration gaps.
The canonical graph is revision 244, with its recovery export and versioned
snapshot current. Graph validation has zero errors; it retains one pre-existing
warning for content drift in `tna-ward-c142-west-barsham-gurney-inquisitions`.

The approved publication edit does not add sources. It makes the fact sheet's
parentage wording agree with the existing case-file synthesis, so the source
stack remains unchanged.

## Conclusion comparison

The only approved public conclusion change is the parentage estimate: the fact
sheet's parentage highlight, narrative parentage paragraph, and note n8 now say
about sixty-five percent, matching case-file section 11. It remains an indirect,
caveated synthesis rather than a direct-record claim.

The three confidence/publication-wording friction annotations are resolved in
the two fact-sheet rows and case-file section 11 row; the retained legacy
Working Hypotheses mapping records the same resolution. Graph item
`G13-RI-000178` and its topic prose now describe the aligned estimate rather
than a stale fact-sheet lag. No other identity, chronology, conflict-status, or
open-question conclusion was changed by the cutover.

## Website comparison

| Item | Legacy / rollback state | Cutover state |
|---|---|---|
| Default mode | legacy when `G13_PACKAGE` was unset | production package mode when unset; `G13_PACKAGE=legacy` or `off` remains Level-1 rollback. |
| Public research-library route | — | `/research/notes/g13-john-gurney.html` (stable inbound route). |
| Graph export | protected `exports/website/` pre-cutover output | refreshed revision-244 `exports/website-current/` output. |
| Site verification | — | production build and site validation passed; 520 public HTML pages were finalized. |

The package adapter generated 331 annex, evidence, and finding pages. The site
validator passed research-item, source, footnote, and link checks. Nineteen
non-public graph markers remain intentionally without public Evidence links;
they are reported by the build and are not validation failures.

## Retention and rollback

`_legacy/g13-pre-refactor/BASELINE.md` records the pre-cutover companion hash
and graph baselines. The legacy companion, protected pre-cutover website export,
staging graph archive, current recovery export, versioned graph snapshot, mode
switch, and this report remain until Allen accepts the cutover. See
`post-cutover-cleanup-manifest.md` for the separately authorized later hygiene
work.
