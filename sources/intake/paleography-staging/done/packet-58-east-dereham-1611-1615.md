# Packet 58 — East Dereham register bills 1611–1615: CLOSED, the returns do not survive

**Status: answered 2026-07-27. No subcontracted transcription needed.** The question this packet was
written to ask — do the 1611–1615 East Dereham annual returns survive anywhere in PD 86/41? — was
settled by pulling the file's unexamined tail and reading the year at the head of every membrane.
Masters are at `sources/media/nro-pd-86-41/_local/`; the whole-file year map is in
[`sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md`](https://github.com/allengurney/gurney-genealogy/blob/main/sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md).

## The finding

**The East Dereham annual returns for 25 March 1611 – 25 March 1616 do not survive.** Five returns are
lost. This is a permanent evidentiary limit.

Three facts establish it, and together they close the question:

1. **The file is complete and its extent is fixed.** NRO catalogues **PD 86/41, "Indented register
   bills, 1593–1641"**, digitised as **110 contiguous images, `4034129-00692` – `4034129-00801`**. The
   March–July 2026 analysis used `00693`–`00768` — 76 of 110. The other 34 were pulled 2026-07-27.
   Nothing is left unexamined.
2. **The file is strictly chronological.** Every membrane carries a modern pencil year at its head; the
   sequence climbs monotonically 1593 → 1640/41 with no membrane out of place. The unexamined tail,
   which might in principle have held misfiled early membranes, is **1635–1641**. The sequence runs from
   the **1610** return (`00720`–`00725`, in-parchment "East Dereham 1610") directly to the **1616-17**
   return (`00726`, in-parchment "25 of march 1616 unto the 25 of march 1617").
3. **There is no second witness.** The archdeacon's counterpart series — FindMyPast, *Norfolk
   Archdeacon's Transcripts 1600–1812*, archive reference `AT EAST DEREHAM`, 243 images — begins at
   **1725** (film target card: "NORWICH DIOCESE / NORFOLK ARCHDEACONRY / HINGHAM DEANERY / ARCHDEACONS
   TRANSCRIPTS / ITEM 5 / EAST DEREHAM 1725—1811/12"). It cannot cover 1611–1615.

## What this means for the case

The natural birth window for a first child of the **23 September 1611** Gurney–Rybett marriage —
roughly 1612–1615 — is **permanently unobservable at East Dereham**. Deviation D9's counterweight
therefore stands, in a harder form than it was stated: Candidate B is not refuted by the absence of a
1612–1615 Gurney baptism, because the pages that would carry one are gone and will not turn up. But the
converse also holds — that absence can never now be converted into evidence either way, so this line of
enquiry is closed rather than pending.

The case file's expected **son Francis born at East Dereham c.1611–1618** (Entry F) falls partly in the
lost window; if he was born 1611–1615 his baptism is unrecoverable, and only a 1616–1618 birth remains
testable against surviving membranes.

## Corrections this pull forces

- **The chronology lattice is superseded.** Its interpolated rows (`00728/29/30 = 1617`,
  `00731/32 = 1618`, `00733/34 = 1619`) rest on a one-page-per-return assumption that is false. 00726–31
  are all the 1616-17 return; 00732–34 the 1618-19 return.
- **"Page 00725 = the 1615 register year" is wrong.** 00724/00725 are the marriages-and-burials
  membranes of the **1610** return. No 1615 return exists, so the assignment was never possible. This
  independently confirms D10's page reassignment, and every date derived from it — including the Marye
  and Agnes burial years — needs re-deriving.
- **The "Francis Garndy, burial, 8 November 1649, East Dereham" index row (Ancestry 61045) cannot come
  from this file**, which ends at 1640-41. Either the year is a mis-read of the FamilySearch-indexed
  **8 November 1633** burial (VNN2-H8S, Entry F), or it belongs to a different source. Open.

## Retrieval recipe, for the next person

FindMyPast, record set *Norfolk Parish Registers Browse* → parish **East Dereham** → row "Register Bills
/ 1593-1640 / PD 86/41 / 110". Viewer URL — `id` and `parentid` must be the **same** value or the
request 500s:

```bash
echo "https://search.findmypast.co.uk/record?id=gbprs%2fnorfolk%2fpd_86-41%2f00769&parentid=gbprs%2fnorfolk%2fpd_86-41%2f00769"
```

FindMyPast page *N* = image `00691 + N`. The viewer's page-number "Go" box does not respond to scripted
input; drive it by URL. Each record page exposes a direct, **non-cookie-bound** JPEG at
`/media/jpg/<id>/<id>/<per-image-hash>?download=true` — harvest the hashes from the record HTML, then
fetch them with PowerShell in one batch. Full mechanics in
[`.claude/skills/findmypast-record-search/SKILL.md`](https://github.com/allengurney/gurney-genealogy/blob/main/.claude/skills/findmypast-record-search/SKILL.md) §9.

## What is still worth reading in these images

The survival question is closed, but the 34 newly-pulled leaves have never been searched for Gurney
entries. They cover **1635-36 through 1640-41** — after Francis G14's documented move to London, but
within the window of Entry F (the 1633 Francis burial) and of any remaining East Dereham Gurney
household. A Gurney-variant sweep of `00769`–`00798` is a small, self-contained job and has not been
done.

<!-- Packet opened 2026-07-26 as a survival question; answered 2026-07-27 by pulling the tail from
     FindMyPast (Everything tier) and reading membrane-head years off contact sheets. Supersedes the
     2026-07-26 hypothesis that the 1611-1615 membranes might be filed out of order in the tail: they
     are not, and the file is complete. -->
