---
layout: layouts/base.njk
permalink: /key-research/using-gen-ai-in-genealogy.html
title: Using Generative AI in Genealogy
pageHeading: Using Generative AI in Genealogy
subtitle: "What I actually did, what worked for me, and where I think AI helps most in genealogy. Updated 4 April 2026."
description: "Practical, first-person notes on how I used generative AI in genealogy research, writing, paleography, and website creation."
bodyClass: bio-page
activeNav: research
updated: 4 April 2026
---

I used generative AI heavily in this project, but not as a substitute for records, judgment, or source criticism. I used it as a **research assistant, drafting partner, formatting engine, and process recorder**. Below are the approaches that worked best for me.

## Best practices

- **I tag-team with AI.** I do the searching, skim the results, and gather the records. Then I paste the rough material into AI and have it help me sort, compare, summarize, and suggest next steps.
- **I often paste raw search results as-is.** If I have 3 to 12 candidate records, I usually just copy and paste the result list with minimal cleanup. AI is generally good at figuring out the structure.
- **I also paste screenshots.** A quick crop from a search result, index page, or parish register is often enough for AI to read the text and comment on it.
- **This is much faster than doing all triage manually.** In my experience it often made the first-pass review several times faster and sometimes surfaced a promising lead I might have skipped.
- **I ask AI to rank candidates.** I do not just ask "which one is right?" I ask it to sort them into strong, weak, and unlikely matches and explain why.
- **I keep separate chats by topic.** I found it works better to keep one thread per ancestor, record problem, or writing task than to force everything into one giant conversation.
- **I periodically have AI write out the work.** Context windows are finite, so I regularly ask AI to commit findings, open questions, and instructions into Markdown or JSON files.

## Claude vs. ChatGPT

- **My experience changed by task.** In March 2026, I found **Claude** stronger for broad online research, long-context authoring, and knowledge-building.
- **I found ChatGPT especially useful for production work.** I used it a lot for website building, file structuring, formatting, troubleshooting, and one-off technical tasks.
- **I often used both at the same time.** That helped with usage limits, gave me a second opinion, and reduced the risk of over-trusting one model.
- **I treat all such comparisons as temporary.** These tools change quickly.

## Instructions matter more than I expected

- **One of my best decisions was requiring AI to document its own process.**
- For any meaningful deliverable, I pushed AI to also produce a **detailed Markdown instructions file** explaining how it completed the task.
- I wanted those instructions to be:
  - detailed
  - current
  - repeatable
  - clear enough that another AI could reproduce the work later
- This improved consistency from run to run.
- It also made it easier for me to switch AI platforms without losing momentum.
- In a large genealogy project, I now view good instructions as part of the research asset base, not just temporary chat residue.

## Markdown and JSON became my working formats

- I found **[Markdown](https://www.markdownguide.org/getting-started/)** to be one of the most AI-friendly formats for genealogy work.
- I like Markdown because it is:
  - human-readable
  - easy to edit in any text editor
  - portable across tools and platforms
  - easy for AI to restructure and clean up
- I used Markdown for research notes, draft biographies, case files, workflow instructions, and website page content.
- I used **[JSON](https://www.json.org/json-en.html)** when I wanted structured, repeatable data such as ancestor lists, metadata, geography, and page-driving content.
- I found **Markdown templates** especially powerful. Once I had a good template, AI could fill it repeatedly with far more consistency.
- I often edited these files in **[Typora](https://typora.io/)**, which I found especially convenient for visually editing Markdown, though any text editor works.

## Online research

- AI was very effective for:
  - de-conflicting same-name candidates
  - comparing multiple record summaries
  - building research notes from scattered findings
  - spotting chronology problems or family-cluster inconsistencies
  - proposing follow-up searches I had not yet tried
- I still treated the records, not the AI summary, as the evidence.
- I also found AI helpful for building knowledge over time as a case developed, especially when I kept asking it to update written summaries.
- A few limits remained obvious:
  - paywalled sites and subscription databases are still a constraint
  - copied indexes can contain transcription errors
  - AI can flatten uncertainty unless I tell it not to
  - a confident answer is not the same thing as a sound conclusion

## Digital books and PDFs

- I found AI very effective at reading uploaded books, PDFs, scans, and compiled histories.
- This worked especially well with public-domain local histories, surname studies, compiled genealogies, and long scanned books.
- Good use cases included:
  - extracting every mention of a surname
  - building timelines from a book
  - comparing passages across volumes
  - turning a long book into structured notes
- If a file was too large, I often split it into smaller logical chunks.
- OCR quality mattered, but even when OCR was poor, AI could still do useful work from page images and partial text.

## Paleography and hard-to-read records

- I used AI for handwriting analysis, but carefully.
- I found it most helpful when I gave it:
  - a tight crop of the target entry
  - nearby same-hand comparators
  - multiple enhanced versions
  - a narrow question about specific letters or words
- I found AI stronger at **comparative analysis** than at blind transcription.
- I still treated ambiguous readings as ambiguous unless the comparison work became genuinely persuasive.
- For background on old handwriting, the **[UK National Archives palaeography tutorial](https://www.nationalarchives.gov.uk/education/resources/palaeography/)** is a useful resource.
- One example from this project is my [AI Assistant Procedure for Parish Record Analysis](/key-research/east-dereham-ai-assistant-procedure.html).

## Writing a narrative

- When I wanted narrative output, I found it worked best to give AI a crisp brief:
  - what I wanted it to produce
  - who the audience was
  - what tone I wanted
  - how much uncertainty should remain visible
- I often asked AI to draft in stages:
  - outline first
  - bullet summary second
  - prose last
- I also pushed it to keep evidence categories separate:
  - direct evidence
  - circumstantial evidence
  - interpretation
  - open questions
- For genealogy writing, I found AI especially good at converting messy notes into readable timelines, concise summaries, and first-draft narrative that I could then tighten.

## How I used AI to build the website

- I used AI not just for genealogy research, but also to help build the website itself.
- My basic model was simple: **I focused on the content and evidence; AI handled much of the formatting and production work.**
- In practice, I used **Markdown pages** and **Markdown templates** as the source content, and then used **[Eleventy (11ty)](https://www.11ty.dev/)** to turn that source material into static HTML pages.
- I found this approach useful because it let me keep the source material readable and editable while still producing a structured website.
- AI helped me with:
  - page formatting
  - YAML frontmatter
  - template consistency
  - HTML-ready sections
  - navigation and layout updates
  - troubleshooting site issues
- The project itself uses Eleventy as the static site generator and builds finished HTML from Markdown and templates. That fit my workflow very well because it kept content and presentation loosely separated.
- A big part of making this work was maintaining **detailed, repeatable instructions** so AI could follow the same page patterns over and over.

## AI-assisted fact sheets

- Another strong use case was ancestor fact sheets.
- I used a standardized Markdown fact-sheet template plus a separate instructions/handoff file so AI could build pages with a repeatable structure.
- That usually included sections such as:
  - vital records
  - highlights
  - children
  - narrative
  - citations
  - related links
  - research appendix
- I found this especially effective because the **research appendix** gave me a place to preserve institutional memory, not just polished conclusions.
- That meant AI was helping me create both the public-facing page and the deeper working notes behind it.
- A published example from this site is the [Francis Gurney fact sheet](/fact-sheets/g14-francis-gurney-fact-sheet.html).

## GEDCOMs and other structured outputs

- AI also helped me think through GEDCOMs and other structured exports.
- I found it useful for:
  - normalizing names and places
  - comparing one structured file against another
  - spotting obvious relationship or date inconsistencies
  - helping prepare import-ready content
- I still treat structured exports carefully because one small error can spread widely after import.
- For background, **[FamilySearch's GEDCOM overview](https://www.familysearch.org/en/help/helpcenter/article/what-is-a-gedcom-file)** is a reasonable starting point.

## Limits and cautions

- I do not trust AI just because it sounds polished.
- I have seen it overstate weak evidence, smooth over uncertainty, or make a fragile conclusion sound settled.
- I also found that long projects can lose coherence unless I keep forcing the work back into files, templates, and written summaries.
- My working rule is simple: **AI can accelerate the work, but I still need to control the evidence, the interpretation, and the final judgment.**

## Bottom line

- I have found generative AI genuinely useful in genealogy.
- For me, the best model is not "ask one question and trust the answer."
- It is:
  - I gather and judge the records
  - AI helps me sort, compare, summarize, draft, and format
  - I verify the result and decide what I actually believe
- Used that way, AI has saved me substantial time and made it much easier to manage a large genealogy research and publishing project.
