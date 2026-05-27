---
name: familysearch-tree-updates
description: Workflow for proposing and applying edits to FamilySearch Family Tree person records based on canonical repo research. Covers name standardization, vital cleanup, source attachment, conflict handling, and the post-update audit. Use whenever the task is updating FamilySearch person data for an ancestor in this lineage.
disable-model-invocation: true
---

Use this skill when editing a person record on FamilySearch.org based on the canonical research and structured ancestor data in this lineage. The output of a session under this skill is one or more FS person records updated, paired with a detailed audit shared back to the user.

## Read first
- `.claude/CLAUDE.md`
- `data/familysearch-ids.csv` for the FS PID and any known conflict notes
- `data/ancestors.json` for the canonical name, dates, and relationships
- The ancestor's fact sheet under `fact-sheets/g{NN}-*.md`
- The ancestor's research companion under `research/people/g{NN}-*.md`
- The ancestor's footnote list (key sources to attach alongside the biography)

## Workflow

1. **Inspect first, never write blind.** Open the FS person via Chrome MCP. Capture every visible field: header (name + date range), Vitals (Name, Sex, Birth, Christening, Death, Burial), Other Information (Alternate Names, Events, Facts), Spouses and Children, Parents and Siblings, Sources tab, Collaborate tab (existing discussions). Note who last edited what (the small contributor stamps).
2. **Draft the diff.** For each field where the canonical research differs from FS, list before/after. For fields FS already has right, mark "confirmed, no change". Surface every change to the user for explicit approval before any FS write.
3. **Get per-batch user approval.** The user is the final arbiter for public-facing edits. Default to one ancestor per approval cycle during a pilot; can broaden to a small batch (3–5) once cadence is established.
4. **Execute in this order:**
   1. **Add alternate names first.** Preserves old spellings as searchable variants before changing the primary.
   2. **Edit primary Name** (Last Names + Suffix as needed; First Names usually stays).
   3. **Edit vital dates/places** (Birth, then Death, then Burial/Christening if applicable).
   4. **Attach sources** (Biography + 2–5 additional key sources).
5. **Handle the "Quality Score Will Be Lowered" dialog deliberately.** When FS surfaces conflicts on a vital change, expand "View More" to see every conflict before deciding. Save with a detailed "Why are you confident this change is correct?" rationale when the new value is correct and the conflicts originate from stale downstream FS data. Flag each downstream conflict as a follow-up in the post-update audit.
6. **Produce a post-update audit.** Field-by-field before/after, the exact reason text saved, every source attached with its full citation/notes/reason and selected Vital Tags, what was intentionally not changed, and open follow-ups (with FS PIDs).

## FS-facing language rules

These apply to every text field a future FS reader will see: Name reasons, vital reasons, alternate-name reasons, source titles, source citations, source notes, source "reason to attach", and the conflict-dialog "Why are you confident" field.

- **Do not reference `G##` generation labels** (G20, G23, etc.). FS users do not know the lineage numbering. Use names + dates instead ("son of Thomas Gournay I (fl. c. 1408–1450)" not "son of Thomas Gournay I (G21)").
- **Do not reference "the repo"** or any internal terminology. Refer to "this person's record", "the attached biography", "the research", etc.
- **"Fact sheet" is not user-meaningful.** Always use "Biography" in source titles and references.
- **"Gurney Family Genealogy" alone is too generic** as a source title. Use the format: `[Name] Biography by Allen Gurney`. "Gurney Family Genealogy" is acceptable as the site/work name inside the citation body.
- **Avoid "drawing on"** as the opener for citation text. Use "based on", "synthesizes", "Primary sources include", etc.
- **When Daniel Gurney is mentioned, prefix with "historian Daniel Gurney" or "historical genealogist Daniel Gurney"** — his being a Gurney himself is confusing to readers without context.

## Source-attachment conventions

- **Biography source** (one per ancestor):
  - Title: `[Name] Biography by Allen Gurney`
  - Source Type: Web Page URL
  - URL: the published-site fact-sheet URL on `genealogy.allengurney.com` (the repo file slug, not the renamed display name — slugs are kept stable for URL persistence).
  - Event Date: birth year (or estimate, e.g., "about 1430").
  - Vital Tags: Name + Birth + Death. Skip Sex, Christening, Burial unless directly attested in the biography.
- **Additional sources: at least 2, not more than 5 per ancestor.** Drawn from the fact-sheet footnotes or research companion. Prioritize in this order:
  1. Primary sources (wills, IPMs, charters, parish records, royal records — Patent/Close Rolls, etc.).
  2. Antiquarian standards (Blomefield's *History of Norfolk*; historian Daniel Gurney's *Record* and *Supplement*; *History of Parliament Online*).
  3. Scholarly works (Foundation for Medieval Genealogy's MedLands; Pattou's *Racines Histoire*; modern peer-reviewed work).
- **For each additional source, include a stable URL when available** (Internet Archive, HathiTrust, British History Online, History of Parliament Online, etc.).
- **If no stable URL exists, leave the Web Page URL field blank.** FS accepts "Web Page URL" source type with an empty URL field. Never fabricate a URL pattern — a 404 link is worse than no link. Why: Daniel Gurney's 1858 *Supplement* has no canonical online edition; a constructed Google Books URL was rejected on review and removed.
- **Tag each source to the specific Vital Tags it supports.** A pedigree confirms Name + parent linkage; a will confirms Death + Burial. Don't over-tag.

### Field-by-field structure for the Create Source dialog

FS limits the Citation field to **1000 characters**. Split content as follows:

| Field | What goes here |
|---|---|
| **Source Title** | `[Name] Biography by Allen Gurney` (for the biography) or `[Author], [Work] — [section]` (for additional sources). |
| **Event Date** | Year or "about YYYY" tied to the most relevant event the source attests. Birth for the biography; death for a will; pedigree placement for genealogical works. |
| **Web Page (Link to the Record)** | Stable URL. |
| **Citation (Where The Record Is Found)** | Short bibliographic citation. Under 1000 chars. |
| **Notes (Describe The Record)** | What the source actually says: key extracts, dates, places, names mentioned. The "content" of the source. |
| **Reason to Attach Source** | One paragraph: why this source belongs on this person's record — which facts it supports. |
| **Vital Tags** | Click the tags this source corroborates (Name, Sex, Birth, Christening, Death, Burial). |

## Field discipline

- **Alternate Names**: add documented spelling variants *before* changing the primary name. Use "Also Known As" for spelling variants; "Birth Name" is for maiden/birth surname. Each alternate name needs a short Reason explaining the variant's documentary basis. Preserve pre-existing alternate names. **Verify each save before adding the next**: the alt-name dialog can occasionally stay open after a save that didn't bind, and the next form-fill will overwrite the unsaved values. Check the visible Alternate Names list (and the Latest Changes pane) for the new entry before clicking ADD ALTERNATE NAME again.
- **Primary Name**: include Suffix (II, III, Knt., Esq.) when the canonical name uses one. Reason field should cite the source for the chosen form.
- **Dates**: prefer the FS-standardized form ("about 1430" not "c. 1430"; "after 1430" not "Aft 1430"). After typing the date in the input, click the suggestion in the dropdown so the green "Standardized Date" checkmark appears. The dropdown may still show the *previous* standardization; click into the date input again to refresh, then click the new suggestion. Save will fail standardization checks otherwise.
- **Place**: prefer FS-standardized place names. Birth/Death places that already exist on FS and are correct should not be edited.
- **Sex**: rarely needs editing; leave alone.
- **Christening / Burial**: leave empty unless the source documents the specific event. Will-directed burial *intention* is not the same as a recorded burial.

## Risk handling

- **Every FS write is public.** Show diff → get approval → save → audit. Never skip the approval step for vital fields, names, or sources during a pilot.
- **"Quality Score Will Be Lowered" dialog**: advisory, not blocking. Expand "View More" to see all conflicts. Proceed when the canonical value is correct and the conflicts originate from stale downstream data. The "Why are you confident" rationale should be substantial and cite the primary or compiled source.
- **Downstream-stale conflicts** (e.g., child birth before parent, marriage before birth, mother's death before child's birth) are typical when correcting a single vital. They resolve as the related FS records are also touched. Log each downstream PID + conflict as a follow-up.
- **Never delete an existing source** without explicit user permission, even when the source looks low-quality.
- **Never modify parent/spouse/child relationship links** as part of a vital-update pass. Relationship edits warrant their own pass.
- **Pre-existing Alternate Names, Custom Events, Facts, Notes, Discussions, Memories**: leave untouched unless the user explicitly approves a change.
- **Pre-existing user-contributed Reason text on vitals**: replace with a more substantive reason that includes a source citation when changing a vital. Don't keep "Standardized Place" as the sole reason after a substantive vital edit.

## Open-item / data-conflict cleanup

When the user asks for a "data conflict" cleanup pass on records adjacent to the focus ancestor (spouse, mother, child), the same rules apply but the scope is narrower:

- **Replace** demonstrably wrong unsourced dates with the canonical research date when one exists.
- **Tighten loose bounds** when our research changes the reference. Example: a mother's death recorded as "after 1404" (the old child birth year) becomes "after 1430" (the corrected child birth year) — same kind of inference, stronger lower bound. The new Reason should cite the corrected reference and the canonical source.
- **Delete** demonstrably impossible unsourced dates only when no canonical replacement exists. FS preserves change-history records on delete.
- **Leave alone** dates that are plausible but unconfirmed.
- **Watch for duplicate events on Couple Relationships.** FS occasionally stores two Marriage events on the same couple at the same date. After updating the kept event, delete the duplicate with a clear "Reason for Deleting" note. Why: leaving a duplicate behind makes the timeline ambiguous on subsequent reads.
- **Apply the same source-attachment conventions** if adding a Biography or other source to the adjacent record falls within the user-approved scope.
- **Cross-reference the focus ancestor's PID in the Reason field** when an adjacent-record edit was triggered by a change to the focus ancestor. Example: "see his record (FS PID 9ZHT-HRP) for context." This gives future readers a navigation breadcrumb.

## Audit format

Output sections, in this order:

1. **Header**: person name + suffix, FS PID, editor (FS account), date, FS URL.
2. **Before/after summary** for header + Vitals (one row per field, only when something changed).
3. **Per-change detail**: a section for each saved change.
   - Alternate Names: table of added entries with Reasons.
   - Primary Name: before/after with full Reason text saved.
   - Each vital: before/after, FS-standardization status, full Reason text, conflicts dialog summary (if triggered).
   - Each new source: full citation, notes, reason, vital tags.
4. **"What was NOT changed (intentionally)"**: explicit list of fields/relationships left alone.
5. **"Open follow-ups discovered during pass"**: downstream FS data issues with PIDs and brief description. **Include structural attribution problems**, not only downstream-stale dates — when an FS field's value is internally consistent only if attached to a *different* ancestor (e.g. an IPM dated to a father appearing on the son's record), flag it as a structural follow-up rather than treating it as a stale-data conflict.

## Cadence and batching

- **Pilot first**: the first FS-edit pass on a new ancestor (or a new generation tier) is a single-ancestor pilot with full audit.
- **After successful pilot**: can batch 3–5 contiguous ancestors per session, still with per-batch user approval but combined diffs.
- **Always batch the Save → "Quality Score" confirmation Reason input**: the rationale used in the underlying edit's Reason field can be the same text in the conflict-dialog "Why are you confident" field.

## Self-update

This skill should be kept current with what we learn. After each FS-update session, review this file. Add or revise sections directly if new conventions emerged, or if a prior convention turned out to be wrong. **User approval is not required for these updates.** Updates should:

- Be additive when adding a new convention.
- Replace specific text only when a prior convention turned out to be wrong (note the why in the commit/edit).
- Always include a brief "Why" so the convention is portable to future ancestors.

## Cross-reference

- `.claude/skills/familysearch-export-review/SKILL.md` — Phase 0 of intake (FS export PDF review). Different workflow; complementary.
- `.claude/CLAUDE.md` — project-wide rules.
- `data/familysearch-ids.csv` — FS PID mapping per ancestor.
