# Context Graphs for Genealogy

A context graph is a research map. It stores the important pieces of evidence, the people and places they mention, and the reasons one piece matters to another. It is not meant to replace the written story. It helps keep the story honest.

Think of a spreadsheet where each row is a fact, clue, conflict, or question. A context graph adds one more thing: named links between the rows.

```text
Source record
  supports
Research finding
  qualifies
Open question
  depends on
Another finding
```

That link is the point. Genealogy rarely turns on one record by itself. It turns on clusters: a deposition, a land record, a neighbor, a probate file, a missing baptism, and a same-name person who must be ruled out. A context graph lets us preserve that cluster without making every public page read like a legal brief.

## How this differs from RAG

RAG means "retrieval augmented generation." In plain English, it is a way to give an AI a pile of relevant text before it answers. It is useful, but it usually retrieves passages. The passages may be right, but the AI still has to infer how they fit together.

A context graph does more of that work ahead of time.

```text
RAG:
question -> find related text -> ask AI to reason from the text

Context graph:
question -> find related evidence + named relationships -> reason from the map
```

For this project, that matters because the hard part is not only finding every mention of John Gurney. The hard part is remembering which mentions support his timeline, which qualify it, which contradict a candidate identity, which are only background, and which still need review.

## The G13 Context Map

Our first context graph is for John Gurney of early Massachusetts, generation G13, 13 generations back from Allen. It sits beside the normal research writing. The public page remains readable; the graph carries the supporting structure behind it.[^g13-graph-readme]

The map has a few basic objects:

- **Research units:** small topic pages, such as arrival, Weymouth, Braintree, family, origin, and open questions.
- **Entities:** people, places, sources, ships, organizations, events, and hypotheses.
- **Research items:** individual claims, pieces of source evidence, analyses, conflicts, negative results, and open questions.
- **Sources:** the registered books, records, images, extracts, and validations behind the items.
- **Relations:** named links such as supports, contradicts, qualifies, depends on, eliminates, contextualizes, or informs.
- **Prose markers:** hidden tags in the writing that connect a paragraph to the graph items behind it.

```text
Topic page paragraph
        |
        v
Prose marker
        |
        v
Research item ----- cites -----> Source
     |   |
     |   +-- mentions ----------> Person / place / event
     |
     +-- supports / qualifies / contradicts / depends on
                                |
                                v
                         Other research item
```

A normal footnote says, "Here is the source." The graph can also say, "Here is why this source matters, what it supports, what it weakens, and what question remains." That is the practical benefit: less hidden reasoning, fewer duplicated explanations, and a cleaner path from a short public statement to the evidence behind it.

For readers, the goal is simple. Start with the story. When a claim looks important or surprising, open the evidence trail. See the source, the related facts, the conflicts, and the open questions without having to read the whole research archive.

For the research process, the benefit is just as plain. The graph makes the project better at remembering its own reasoning.

[^g13-graph-readme]: Local implementation details are in [`tools/g13_graph/README.md`](https://github.com/allengurney/gurney-genealogy/blob/main/tools/g13_graph/README.md). The current schema defines these objects in `tools/g13_graph/schema/migrations/0001_initial.sql` and `tools/g13_graph/schema/migrations/0003_prose_markers.sql`.
