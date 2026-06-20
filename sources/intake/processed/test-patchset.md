# Test patchset — compact, human-reviewable operation format

**Status:** Mock only — do not apply.

**Purpose.** Demonstrate a patchset format that remains easy to review while
avoiding large duplicated `old_string` / `new_string` blocks. The prose below
explains the proposed result; the operation blocks tell the Phase-2 tool
exactly how to make it and when it must stop.

## Review summary

| Item | File | Intended result |
|---|---|---|
| 1 | `research/people/example-person.md` | Add a sourced finding immediately before the Open Questions section. |
| 2 | `research/people/example-person.md` | Replace the current Residence subsection with an assimilated account. |
| 3 | `fact-sheets/example-person-fact-sheet.md` | Correct one short published sentence in place. |
| 4 | `sources/validations/example-source.md` | Create a thin source-validation note. |

No source IDs, structured data, media files, or research leads change in this
mock.

---

## Item 1 — Add a new finding before Open Questions

**Finding.** A parish entry places Example Person at Norwich in 1638. The
research companion should preserve the date, place, and source without
presenting the discovery process as part of the visible prose.

**Result for review:**

> A 1638 parish entry places Example Person at Norwich, where he witnessed the
> marriage of John Sample and Mary Test.[^example-parish-1638]
>
> [^example-parish-1638]: Norwich parish register, marriage of John Sample and
> Mary Test, 14 June 1638; Example Person named as witness. Source ID:
> `example-parish-register`.

```yaml patch-op
op: insert_before
path: research/people/example-person.md
anchor: "## Open Questions"
anchor_count: 1
anchor_sha256: "MOCK-SHA256-OF-EXACT-ANCHOR-AND-LOCAL-CONTEXT"
text: |
  ## Norwich parish appearance, 1638

  A 1638 parish entry places Example Person at Norwich, where he witnessed the
  marriage of John Sample and Mary Test.[^example-parish-1638]

  [^example-parish-1638]: Norwich parish register, marriage of John Sample and
  Mary Test, 14 June 1638; Example Person named as witness. Source ID:
  `example-parish-register`.

```

**Apply rule:** the tool inserts the text only if the heading occurs exactly
once and its stored context hash still matches. Otherwise it stops without
writing.

---

## Item 2 — Assimilate the Residence subsection

**Finding.** The existing subsection says only that Example Person probably
lived in Norfolk. The new evidence narrows that account to Norwich by 1638
while preserving the earlier uncertainty about his residence before that
date.

**Replacement subsection for review:**

```markdown
### Residence

Example Person's residence before 1638 remains uncertain, although the known
family and occupational connections point to Norfolk. A parish entry places
him specifically at Norwich on 14 June 1638, when he witnessed the marriage of
John Sample and Mary Test.[^example-parish-1638]
```

```yaml patch-op
op: replace_section
path: research/people/example-person.md
heading: "### Residence"
end_at_next_heading_level: 3
old_sha256: "MOCK-SHA256-OF-CURRENT-RESIDENCE-SECTION"
text: |
  ### Residence

  Example Person's residence before 1638 remains uncertain, although the known
  family and occupational connections point to Norfolk. A parish entry places
  him specifically at Norwich on 14 June 1638, when he witnessed the marriage
  of John Sample and Mary Test.[^example-parish-1638]
```

**Apply rule:** the tool locates the named subsection structurally, verifies
the complete current subsection against `old_sha256`, and replaces it. The old
subsection does not need to be reproduced in this patchset.

---

## Item 3 — Correct one published sentence

**Correction.** The fact sheet currently says Example Person was living in
Norwich by 1636. The source establishes Norwich only in 1638.

```yaml patch-op
op: replace_exact
path: fact-sheets/example-person-fact-sheet.md
old: "He was living in Norwich by 1636."
new: "He was in Norwich by 1638."
match_count: 1
```

This short literal replacement remains more readable than a hash-only
operation and lets the reviewer see the exact correction at a glance.

---

## Item 4 — Create a thin validation note

**New file for review:**

```markdown
# Validation — Example parish register

Source ID: `example-parish-register`

**Examined.** Marriage entry for John Sample and Mary Test, 14 June 1638.

**What it establishes.** Example Person was present at Norwich as a witness.

**Limits.** This entry does not establish his residence before 1638.

**Finding landed in.** `research/people/example-person.md`.
```

```yaml patch-op
op: write_file
path: sources/validations/example-source.md
must_not_exist: true
text: |
  # Validation — Example parish register

  Source ID: `example-parish-register`

  **Examined.** Marriage entry for John Sample and Mary Test, 14 June 1638.

  **What it establishes.** Example Person was present at Norwich as a witness.

  **Limits.** This entry does not establish his residence before 1638.

  **Finding landed in.** `research/people/example-person.md`.
```

---

## Phase-2 safeguards

Before writing, the executor must:

1. Parse every operation and confirm every target path is inside the repository.
2. Simulate all operations in order against an in-memory copy of the files.
3. Require every anchor, match count, and hash check to pass.
4. Stop the entire patchset if any operation fails; do not partially apply it.
5. Show the resulting unified diff for review or logging.

After writing, it must:

1. Verify that the resulting files equal the simulated versions.
2. Run the checks appropriate to the touched paths.
3. Report any structural failure without inventing a repair.

## Expected Phase-2 report

- 1 finding inserted in `research/people/example-person.md`
- 1 subsection replaced in the same file
- 1 sentence corrected in `fact-sheets/example-person-fact-sheet.md`
- 1 validation file created
- No source registry, structured-data, media, or lead changes

Because this is a mock, it has no completion stamp and must not be moved to
`sources/intake/done/`.
