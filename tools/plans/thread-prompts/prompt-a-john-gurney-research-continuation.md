# Thread prompt A — continuing the John Gurney (G13) identification research

*Paste the block below as the opening message of a new thread. Recommended model: Opus 5. Nothing
below hard-codes a lead or a to-do; the live worklist lives in the repo and should be read at the
start of the thread, not carried in from here.*

---

I want to continue the John Gurney (G13) origin research. Before proposing anything, ground yourself
properly — this problem has a long history in this repo and a lot of the obvious moves have already
been made and, in some cases, already been made *and found to be wrong*.

## Ground yourself first

Read, in this order, and do not skim:

1. `research/case-files/john-gurney-case-file-v5.md` — the working case file. Sections 6 onward carry
   current state; sections 1–5 are being revised and may still contain superseded claims.
2. `research/people/g13-john-gurney/topics/identity/` — the `50-` through `59-` units are the July 2026
   refactor: register limits, the Francis first-marriage sweep and death record, the Buckinghamshire
   elimination pass, the naming-convention work, the childhood hypotheses, and the open-action list.
   The `30-` through `37-` units are the older graph-backed material, parts of which the refactor units
   supersede.
3. `sources/intake/paleography-staging/done/east-dereham-re-review-2026-07-FINDINGS-deviation-audit.md`
   — read the whole thing, including the root-cause chain. It documents how a confident, heavily
   "corroborated" reading turned out to be a different family on a different page, and why three model
   families agreeing on one mislocated crop raised confidence in an error. Treat it as a description of
   how *this* research fails, not as history.
4. `research/people/g13-john-gurney/topics/identity/59-refactor-open-actions.md` — the current worklist,
   including which items are confidently offline-only.
5. `sources/intake/g13-graph-breadcrumb.md` — what has changed but is not yet in the context graph.

Then use `tools/repo_search.py` (never grep) to check anything you are about to assert. This repo has
recorded negatives going back months; re-running a search someone already ran and logging it as new is
the most common way to waste a turn here.

## What the problem actually is

A tailor named John Gurney, married to a Mary by about 1627, with English-born children, appears at
Weymouth, Massachusetts in June 1641 and dies at Braintree in 1662/3. He deposed "aged 50 or
thereabouts" in 1653. No record states his English origin, and Anderson's *Great Migration Directory*
gives it as "Unknown". England held forty-plus John Gurney heads of household in the relevant decades,
five to seven of them simultaneously in Buckinghamshire alone.

The leading named candidate is a hypothesised son of Francis Gurney of West Barsham, Norwich and
London. It is currently well under 50% and shares the field with two record-state categories and
several documented but unaccounted-for men. **Do not treat the leading candidate as the answer and
work backwards to support it.** That failure mode has already cost this project one reversal.

## How I want you to work

**Be a detective, not a clerk.** The mechanical sweeps have largely been done. What moves this problem
now is *reframing*: asking what class of record would individuate a man rather than a surname; noticing
that a test's window was set for the wrong event; reading a naming custom forwards instead of
backwards; realising that a county's probate tier is online after the repo recorded it as a
record-office visit. Every recent advance here came from a change of question, not a change of query.

Specific habits I want:

- **Prefer individuating records to register continuity.** Probate, certificates of residence, licences,
  land conveyances, company admissions, tax returns — records that name a man, his wife, his parish, his
  trade, his heir. Surname continuity in a parish register proves almost nothing in a dense same-name
  county.
- **State coverage before stating a negative.** "Not found" is worthless without "in a source that would
  have held it". Several apparent negatives in this file turned out to be missing volumes or
  place-standardisation artefacts.
- **Look for the record that could kill a hypothesis**, not the one that could support it. If a
  hypothesis explains why no record exists, no missing record can count against it — so it can only be
  moved by positive evidence.
- **Generate hypotheses actively.** Ask what a person in this situation would have left behind and where.
  Consider record classes nobody has touched: manorial, quarter sessions, chancery, port books, muster
  rolls, apprenticeship outside the livery system, colonial-side records read for English clues.
  Propose several angles, say which you rate and why, then work the best one properly rather than all
  of them shallowly.
- **Say when you are speculating.** Label it, then keep going. I would rather have a labelled
  speculation than a hedge.

## Practical notes

FindMyPast, Ancestry and FamilySearch are authenticated in the browser (Everything tier on FindMyPast).
The relevant source mechanics — parameter quirks, wildcard behaviour, download recipes, known failure
modes — are in `.claude/skills/findmypast-record-search/` and the FamilySearch skills; read them before
deriving anything yourself, and add to them when you learn something new.

Findings go to `research/`, sources to `sources/`, per the repo rules. Anything substantive must be
written into the repo before the turn ends, not left in the conversation.

Tell me what you think the most promising unexplored angle is before you start working it.
