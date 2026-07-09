# Context Graphs for Genealogy

A context graph is a kind of content graph: a way to store information by meaning, not just by location. Instead of saying "this sentence lives in file 14" or "this row is in column C," it says "this claim is about this person, comes from this source, supports this conclusion, conflicts with that clue, and still leaves this question open."

That sounds technical, but the idea is familiar. A spreadsheet is good at rows and columns. A folder of topic pages is good at readable prose. A search box is good at finding words. A context graph is good at preserving relationships.

<figure aria-labelledby="context-graph-figure-title" style="margin: 1.5rem 0;">
  <svg viewBox="0 0 920 390" role="img" aria-describedby="context-graph-figure-desc" style="max-width: 100%; height: auto;">
    <title id="context-graph-figure-title">Flat content compared with a context graph</title>
    <desc id="context-graph-figure-desc">A flat table stores rows. A context graph stores connected research items with source, date, confidence, and question metadata.</desc>
    <rect width="920" height="390" fill="#ffffff"/>
    <text x="460" y="38" text-anchor="middle" font-family="Arial, sans-serif" font-size="25" font-weight="700">Flat Content vs. Context Graph</text>

    <g transform="translate(55 80)">
      <text x="150" y="0" text-anchor="middle" font-family="Arial, sans-serif" font-size="19" font-weight="700">Flat file, table, or notes</text>
      <rect x="0" y="35" width="300" height="210" fill="#f8fafc" stroke="#111827" stroke-width="3"/>
      <rect x="0" y="35" width="300" height="42" fill="#0ea5e9" stroke="#111827" stroke-width="3"/>
      <line x1="78" y1="35" x2="78" y2="245" stroke="#111827" stroke-width="3"/>
      <line x1="205" y1="35" x2="205" y2="245" stroke="#111827" stroke-width="3"/>
      <line x1="0" y1="77" x2="300" y2="77" stroke="#111827" stroke-width="3"/>
      <line x1="0" y1="112" x2="300" y2="112" stroke="#111827" stroke-width="2"/>
      <line x1="0" y1="147" x2="300" y2="147" stroke="#111827" stroke-width="2"/>
      <line x1="0" y1="182" x2="300" y2="182" stroke="#111827" stroke-width="2"/>
      <line x1="0" y1="217" x2="300" y2="217" stroke="#111827" stroke-width="2"/>
      <g stroke="#94a3b8" stroke-width="4" stroke-linecap="round">
        <line x1="18" y1="96" x2="58" y2="96"/>
        <line x1="96" y1="96" x2="178" y2="96"/>
        <line x1="224" y1="96" x2="282" y2="96"/>
        <line x1="18" y1="131" x2="58" y2="131"/>
        <line x1="96" y1="131" x2="178" y2="131"/>
        <line x1="224" y1="131" x2="282" y2="131"/>
        <line x1="18" y1="166" x2="58" y2="166"/>
        <line x1="96" y1="166" x2="178" y2="166"/>
        <line x1="224" y1="166" x2="282" y2="166"/>
        <line x1="18" y1="201" x2="58" y2="201"/>
        <line x1="96" y1="201" x2="178" y2="201"/>
        <line x1="224" y1="201" x2="282" y2="201"/>
      </g>
      <text x="150" y="285" text-anchor="middle" font-family="Arial, sans-serif" font-size="16">Good for storage and sorting</text>
      <text x="150" y="307" text-anchor="middle" font-family="Arial, sans-serif" font-size="16">Weak at explaining relationships</text>
    </g>

    <g transform="translate(515 80)">
      <text x="165" y="0" text-anchor="middle" font-family="Arial, sans-serif" font-size="19" font-weight="700">Context graph</text>
      <g stroke="#111827" stroke-width="4">
        <line x1="165" y1="55" x2="70" y2="120"/>
        <line x1="165" y1="55" x2="255" y2="120"/>
        <line x1="70" y1="120" x2="165" y2="175"/>
        <line x1="255" y1="120" x2="165" y2="175"/>
        <line x1="70" y1="120" x2="70" y2="245"/>
        <line x1="255" y1="120" x2="255" y2="245"/>
        <line x1="70" y1="245" x2="165" y2="175"/>
        <line x1="255" y1="245" x2="165" y2="175"/>
        <line x1="70" y1="245" x2="255" y2="245"/>
      </g>
      <g fill="#ffffff" stroke="#111827" stroke-width="4">
        <circle cx="165" cy="55" r="26"/>
        <circle cx="70" cy="120" r="26"/>
        <circle cx="255" cy="120" r="26"/>
        <circle cx="165" cy="175" r="26"/>
        <circle cx="70" cy="245" r="26"/>
        <circle cx="255" cy="245" r="26"/>
      </g>
      <circle cx="165" cy="55" r="42" fill="#bfdbfe" stroke="#0284c7" stroke-width="5" opacity=".85"/>
      <circle cx="255" cy="120" r="42" fill="#bbf7d0" stroke="#10b981" stroke-width="5" opacity=".85"/>
      <circle cx="70" cy="245" r="42" fill="#ddd6fe" stroke="#8b5cf6" stroke-width="5" opacity=".85"/>
      <circle cx="255" cy="245" r="42" fill="#fecaca" stroke="#ef4444" stroke-width="5" opacity=".85"/>
      <g fill="#ffffff" stroke="#111827" stroke-width="4">
        <circle cx="165" cy="55" r="22"/>
        <circle cx="70" cy="120" r="22"/>
        <circle cx="255" cy="120" r="22"/>
        <circle cx="165" cy="175" r="22"/>
        <circle cx="70" cy="245" r="22"/>
        <circle cx="255" cy="245" r="22"/>
      </g>
      <g font-family="Arial, sans-serif" font-size="15">
        <rect x="330" y="58" width="28" height="18" rx="8" fill="#bfdbfe" stroke="#0284c7" stroke-width="3"/>
        <text x="368" y="73">date / time</text>
        <rect x="330" y="90" width="28" height="18" rx="8" fill="#bbf7d0" stroke="#10b981" stroke-width="3"/>
        <text x="368" y="105">confidence</text>
        <rect x="330" y="122" width="28" height="18" rx="8" fill="#ddd6fe" stroke="#8b5cf6" stroke-width="3"/>
        <text x="368" y="137">source</text>
        <rect x="330" y="154" width="28" height="18" rx="8" fill="#fecaca" stroke="#ef4444" stroke-width="3"/>
        <text x="368" y="169">open question</text>
      </g>
      <text x="165" y="285" text-anchor="middle" font-family="Arial, sans-serif" font-size="16">Good for following meaning</text>
      <text x="165" y="307" text-anchor="middle" font-family="Arial, sans-serif" font-size="16">Shows evidence, questions, and why they connect</text>
    </g>
  </svg>
</figure>

## What a Context Graph Adds

A graph is made of nodes and edges. A node is a thing: a person, place, source, claim, event, or question. An edge is a named relationship between two things: supports, contradicts, mentions, depends on, qualifies, or is distinct from.

A context graph adds the surrounding research context. It can store when a clue applies, how confident we are, where the source came from, whether the source can be published, what question the clue helps answer, and what other clues it must be read with. The result is not just "this is connected to that." It is "this is connected to that for this reason, with this strength, under these limits."

That matters because a reader, researcher, or AI assistant often needs more than a matching paragraph. It needs the shape of the reasoning.

## How This Differs from RAG

RAG means "retrieval augmented generation." In plain English, it is a way to give an AI relevant text before it answers. A RAG system might search a library, pull the top passages, and ask the AI to write from them.

That can be useful. It is much better than asking an AI to rely on memory. But RAG usually returns text snippets. The AI still has to infer which snippet is strong evidence, which is background, which is a duplicate, which conflicts with another source, and which only matters because of a relationship three steps away.

A context graph does some of that organizing before the AI begins.

```text
RAG:
question -> matching passages -> AI infers the relationships

Context graph:
question -> evidence + relationships + limits -> AI reasons from the map
```

The difference is subtle but important. RAG says, "Here are the most relevant pages." A context graph says, "Here are the relevant claims, the sources behind them, the reasons they connect, and the unresolved problems you must not skip."

## Why Genealogy Needs This

Genealogy is relationship work. A single record may be useful, but the real argument often sits between records. One land entry may place a man in a town. A probate file may show his trade. A deposition may estimate his age. A missing passenger-list entry may be meaningful only after we know which lists survive. A same-name man in another county may matter because he has to be ruled out.

Those connections are hard to preserve in ordinary files.

- **One big file** keeps everything together, but it becomes hard to read, hard to search precisely, and hard for an AI to use without drowning in detail.
- **Many topic-sized files** are easier for people, but the reasoning can split across pages. The AI may read one page and miss the related conflict on another.
- **Full-text search** finds words, not meaning. It can find "Braintree" or "Gurney," but it does not know whether the hit supports residence, trade, identity, family structure, or a negative result.
- **RAG over the files** can retrieve better passages, but it still has to guess how the passages fit together unless the relationships are stored somewhere.

A context graph is that "somewhere."

## The G13 Context Map

Our first context graph is for John Gurney of early Massachusetts, generation G13, 13 generations back from Allen. It does not replace the written research. It sits underneath it, like a structured evidence map for the hardest parts of the case.[^g13-graph-readme]

The graph stores the content we most need to remember when reasoning about John:

- where a claim appears in the research;
- what person, place, source, event, or hypothesis it concerns;
- whether the item is source evidence, a finding, an analysis, a conflict, a negative result, or an open question;
- which sources support, qualify, contradict, or merely mention it;
- which other items it supports, weakens, depends on, eliminates, or contextualizes;
- what dates, confidence level, and publication limits belong with it.

In practical terms, the graph turns the G13 research from a pile of excellent but separate reading surfaces into a connected map.

```text
John Gurney question
        |
        +-- arrival timeline
        |       +-- Weymouth records
        |       +-- passenger-list limits
        |       +-- first known Massachusetts appearances
        |
        +-- identity candidates
        |       +-- supporting clues
        |       +-- ruled-out same-name men
        |       +-- unresolved origin questions
        |
        +-- community context
                +-- neighbors
                +-- land and probate records
                +-- trade, family, and town ties
```

That is more compelling than a plain database row because the connection is part of the data. "This source mentions John" is useful. "This source supports the arrival window, qualifies the passenger-list silence, and depends on the Weymouth land chronology" is much better.

For a human reader, the benefit is a cleaner public story with a better evidence trail behind it. You can start with the narrative, then open the supporting map when a claim looks important, surprising, or uncertain.

For AI work, the benefit is grounding without overload. Instead of feeding an AI one giant companion file, or hoping a search result finds the right paragraph, we can ask for the focused neighborhood around a question. The graph can return the relevant findings, source links, cautions, conflicts, and open questions together.

The goal is not to make the research look more technical. The goal is to make the reasoning harder to lose.

[^g13-graph-readme]: Local implementation details are in [`tools/g13_graph/README.md`](https://github.com/allengurney/gurney-genealogy/blob/main/tools/g13_graph/README.md). The current G13 graph is a SQLite context graph with research items, source links, item relationships, publication controls, source-hash checks, and an AI-grounding context compiler.
