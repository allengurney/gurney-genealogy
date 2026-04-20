# Freeform intake guidance

The intake session markdown file is intentionally freeform.

The only hard boundary is:
- `---` separates entries

## Expected reality

An entry may contain:
- a pasted URL
- a filename
- a short note
- an ancestor name
- a place
- a question
- an observation
- a copied sentence or clue
- any mixture of the above

This skill must tolerate that looseness.

## Parsing approach

For each entry:

1. Identify obvious URLs.
2. Identify obvious filenames or file-like references.
3. Identify obvious person/place/topic hints.
4. Use the surrounding text to infer intent.
5. Look for an unclaimed matching file in `sources/intake/new/` when a filename is not explicitly stated.

## File matching rules

### Best case
The entry explicitly names the file.

### Acceptable case
The entry does not name the file, but exactly one new or unclaimed file in the session folder obviously matches.

### Hold-review case
If file matching is ambiguous, do not guess aggressively.
Use `hold-review`.

## Minimal practical guidance for the human user

The intake format is freeform, but it helps if an entry usually includes at least:
- a URL when available
- enough wording to identify the item
- a filename or obvious association when the folder contains multiple new files

This is guidance, not a hard template.

## Good freeform examples

### Example 1
Possible obituary for William Gurney.  
https://example.com/nyt-obituary-page  
Need to confirm identity.  
file william-snippet-1.png

---

### Example 2
East Dereham parish register snippet. Looks like John or Francis.  
Question: does the surname ending match earlier comparator entries?  
dereham-crop.jpg

---

### Example 3
PDF from archive search results. May contain Gurney references.  
https://example.com/archive-pdf
Need extraction and triage.

## Weak entries

An entry is weak when it has:
- no clear file
- no clear URL
- no interpretable note
- no matchable context

Weak entries should generally become `hold-review`, not silently skipped.
