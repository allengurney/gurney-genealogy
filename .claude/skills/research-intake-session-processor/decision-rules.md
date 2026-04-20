# Research intake decision rules

Use these rules when assigning the triage outcome.

## Outcomes

### `promote`
Use when:
- text extraction, OCR, or direct visual inspection was successful enough to understand the item at a useful level
- the item can be meaningfully connected to a person, place, topic, or case file
- there is enough value to justify adding it into working research now
- source tracking in `data/sources.json` can be resolved

Examples:
- likely obituary
- directory listing
- census hit with enough identity signal
- parish entry with readable core content
- article snippet with a clearly relevant fact

### `hold-review`
Use when:
- text extraction was not successful enough
- identification was not successful enough
- the item may matter but remains too uncertain
- handwriting, image quality, or OCR quality prevents useful confident insertion
- file matching is ambiguous
- a compliant `data/sources.json` source entry cannot yet be resolved

This is the default safe outcome for uncertain but potentially useful material.

### `duplicate`
Use when:
- the item materially overlaps an already tracked source file, validation note, or research note
- the item adds little new value

If the new item is clearly better:
- note that in the processed report
- preserve or promote the better one
- map it to the same or corrected source tracking

### `reject`
Use when:
- the item is clearly out of scope
- the item is accidental noise
- the item has no plausible project relevance

## General rules

- Bias toward `hold-review` over `reject`.
- Do not promote when extraction failed materially.
- Do not promote when identification failed materially.
- Do not bypass source tracking.
- Do not convert weak evidence into strong research prose.

## Research insertion threshold

A promoted item should be:
- intelligible
- traceable
- source-tracked
- useful enough that adding it to research now is better than leaving it only in the processed report

## JSON rule

A research insertion is blocked unless there is an applicable `data/sources.json` entry.

That can be:
- matched to an existing source entry, or
- created as a new compliant source entry

If neither is possible, use `hold-review`.
