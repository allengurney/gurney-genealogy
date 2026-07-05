# G13 Gephi export

`g13_gephi_export.py` creates read-only GEXF 1.3 views of the canonical G13
SQLite context graph for Gephi Desktop. It does not edit the database and its
output is not a backup, restore format, or source of truth.

## Run

From the repository root:

```powershell
.\.venv\Scripts\python.exe tools\g13_gephi_export.py
```

The default command writes two revision-stamped files below
`data/context-graphs/g13/exports/gephi/`:

- `g13-research-flow-rNNNNNN.gexf` — start here. It contains research items and
  the explicit relations among them.
- `g13-provenance-rNNNNNN.gexf` — adds only the sources actually linked by the
  graph, plus linked entities, research units, prose markers, and soft evidence
  groups.

Export one view or choose a different destination:

```powershell
.\.venv\Scripts\python.exe tools\g13_gephi_export.py `
    --view research-flow `
    --out-dir "$env:TEMP\g13-gephi"
```

`--db` overrides the canonical database path for staging or testing.

## Suggested first use in Gephi

Open the research-flow file first. In **Appearance**:

1. Color nodes by `item_kind`.
2. Partition or filter nodes by `research_unit_id`.
3. Color edges by `relation_type`.
4. Size nodes modestly by Gephi's degree statistic.
5. Use a force-directed layout such as ForceAtlas 2, then turn on labels.

The provenance view is deliberately denser. Filter `edge_class` to isolate
`item_relation`, `item_source`, `item_entity`, `unit_item`, or `marker_item`
connections. The John Gurney entity and research-unit nodes are expected hubs;
hide their edge classes when they obscure the evidence structure.

## Interpretation limits

- `strength` and `confidence_label` are categorical research judgments. The
  exporter does **not** convert them to GEXF weights or probabilities.
- All edges are directed. Item relations retain their stored direction;
  provenance edges run from source/entity/unit/marker/group to the item.
- Dates are static attributes, not a Gephi dynamic timeline. `date_summary`
  preserves the human-readable envelope and `chronology_key` is available for
  ordering where the graph defines one.
- The export is for local analysis and includes non-public graph items. Do not
  publish it without a separate visibility review.
- Evidence excerpts, private notes, revision bodies, and source-registry
  entries unlinked to the G13 graph are not exported.

For an unchanged database revision, repeated exports are byte-identical.
