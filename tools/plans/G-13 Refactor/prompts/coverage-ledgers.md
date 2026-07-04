# Prompt(s) — coverage ledgers + mechanized checker (Plan 02 §7)

Losslessness at scale (Plan 02 §14) depends on the three ledgers (§7.1–7.3) and a
mechanized checker (§7.4). Split by where errors are cheap: **Opus** freezes the
inventory and scaffolds the ledgers (judgment); **Fable** builds the checker
(frozen spec). Do Part 1 before Part 2 — the checker needs real inputs to test
against.

## Part 1 — Opus: freeze inventory + scaffold ledgers

```
Work in main. Establish the Plan 02 §7 coverage ledgers for the G13 refactor, in
the staging package. Read Plan 02 §7–§8 and §14.

1. Freeze the inventory per §8: pick a clean git commit ref as the cutoff; if the
   working tree is not clean, note the modified/untracked inputs so nothing is
   missed. Record the ref + method in a short coverage/README.md.
2. Create the three ledger CSVs under
   research/people/_staging/g13-john-gurney/coverage/ with the exact columns in
   §7.1 (legacy-companion-map.csv), §7.2 (dump-findings-map.csv), and §7.3
   (source-and-citation-map.csv). Use topicId, not numbered shorthand (§5).
3. Populate the rows for the TWO topics already authored
   (g13-colonial-arrival-chronology, g13-colonial-braintree-community): each legacy
   companion block and each dump finding they assimilated gets a disposition, the
   destination topicId, its G13-RI item ids, and source ids. Leave the rest of the
   companion/dump as un-dispositioned rows (that is the backlog the checker will
   report).
This is the ledger structure + first real rows; ongoing rows are added per topic
by the g13-graph-authoring skill. Do not touch the live companion or dump. Report
the coverage numbers you can already compute.
```

## Part 2 — Fable: build the checker (frozen spec §7.4)

```
Work in main. Build the mechanized coverage checker specified in Plan 02 §7.4. It
is a deterministic Python script (repo .venv), against a frozen spec — no
judgment, no research edits.

Read Plan 02 §7 (ledger column definitions) and the three CSVs under
research/people/_staging/g13-john-gurney/coverage/ (created by the Opus pass).

The checker reads the three ledgers plus the frozen inventory and:
- flags any legacy heading/block or dump finding with NO disposition;
- reports coverage as a percentage and lists the gaps;
- flags any staged unit that cites a sourceId absent from the source-and-citation
  map, and any sourceId not present in data/sources.json.

Output a compact report (counts, coverage %, and the gap lists). Exit nonzero when
there are un-dispositioned items or untracked citation gaps, so it can gate cutover
(Plan 02 §14–§15). Put it at tools/g13_coverage_check.py (or extend an existing
tool if one clearly fits); UTF-8 stdout; add a --json flag. Include a small unit
test with a synthetic ledger set. Do not modify the ledgers or any research/data
file. Do not commit unless asked.
```
