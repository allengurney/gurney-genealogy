# Prompt template — G3 topic increment (Plan 2)

Short session-start prompt for authoring one bounded G13 topic increment. The
substance lives in the `g13-graph-authoring` skill, the `tools/g13_graph/README.md`,
and the Plan 01/02 design docs — this prompt just points there and fills the blanks.

Copy, fill the two blanks, send:

```
Work in main. Task: author a bounded G13 research-topic increment (Plan 2 / Phase G3)
using the /g13-graph-authoring skill.

Topic to author: <GROUP/SLUG, e.g. colonial/weymouth-community — or "you choose the
next well-bounded, low-disambiguation topic from the manifest gap">.
Scope: <1 topic unit | 2 topic units>. Depth and correctness over breadth.

Follow the skill: ground first (companion + dump + repo_search, work the delta),
verify every sourceId is registered, co-author staged prose + kind-neutral items +
evidence markers (Plan 2a M1 is live — place a graph-marker token per cluster and load
markers/marker_items in the same author-batch), dry-run the author-batch, then commit →
hash-sources → snapshot → validate (0 errors) → add coverage-ledger rows + run
g13_coverage_check.py → update the manifest. Non-destructive: staging only; do not touch
the live companion, dump, or site. Stop and report if the increment can't be made
materially smaller and as complete as loading the companion for the same task.
```

Notes:
- Leave "you choose" in if you want the model to pick the next topic from the
  `manifest.json` gap against Plan 02 §4's taxonomy; name a topic to pin it.
- For a **new source** encountered mid-authoring, expect the model to register it in
  `data/sources.json` (+ a `sources/validations/*.md` worksheet) before citing it.
- A ready-to-adapt batch example is in `example-batch.json` beside this file.
