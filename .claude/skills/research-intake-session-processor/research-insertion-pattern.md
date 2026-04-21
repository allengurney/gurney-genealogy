# Research insertion pattern

This skill should add ordinary research content, not a large custom workflow wrapper.

Use a small heading such as:
- `## New research intake`
- `### Intake new research — {short title}`

Keep the addition concise, useful, and easy to revise or delete later.

## Quiet traceability markers

Use HTML comment markers for machine traceability, but keep them visually unobtrusive.

Example:

```md
<!-- intake:v07:item-03:start -->
### Intake new research — William Gurney obituary notice

A clipped newspaper item appears to reference William Gurney in an obituary-style notice dated 1870.[^1]

{{text of obituary here or detailed summary if lengthy}}

The OCR is reasonably strong on the death-notice language, but identity confirmation should still be checked against the date, place, and associated family details.[^2]

See source file:
- `sources/media/william-gurney-obituary-nyt-1870/william-gurney-obituary-nyt-1870.png`
- `sources/media/william-gurney-obituary-nyt-1870/william-gurney-obituary-nyt-1870.ocr.txt`

Validation note:
- `sources/validations/william-gurney-obituary-nyt-1870.md`

[^1]: Full human-readable citation here, following the standard citation process and including URL where available.
[^2]: Additional supporting citation here if needed.
<!-- intake:v07:item-03:end -->
```

## Rules

- Write normal research prose.
- Do not label the block as provisional.
- Include full text of the research unless lengthy.  Text should be cleansed of OCR or related artifacts with reference to source text file for the unmodified version. If the text is lengthy, provide a detailed summary instead.
- Keep uncertainty in the prose when uncertainty is real.
- Use standard nearby citations.
- Prefer one compact research addition over a verbose intake wrapper.
- Do not overwrite mature narrative when a small additive note is sufficient.

## Placement

Append under an appropriate heading near the bottom of the target research file, such as:
- `## New research intake`
- `## Recent source leads`
- `## Additional research notes`

If no such heading exists, create one cleanly.

## Reversibility

The insertion should be:
- easy to locate
- easy to refine
- easy to move
- easy to delete

That is why the HTML markers remain useful even though the prose is ordinary research prose.
