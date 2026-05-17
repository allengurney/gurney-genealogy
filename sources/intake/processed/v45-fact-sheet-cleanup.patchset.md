# Intake patchset v45 — Fact-sheet cleanup (hyperlinks, subtitles, children tables)

**Prepared:** 2026-05-16
**Repo:** `allengurney/gurney-genealogy`
**Target branch:** `main`
**Phase:** 1 (preparation). **Status:** Draft patchset for review. **Do NOT apply until approved.**

## Scope

Three independent fact-sheet cleanup tasks, bundled into one patchset because each is small and they all touch `fact-sheets/*.md`:

1. **Hyperlink audit, G30–G37 main body** — repair or remove helper-hyperlinks whose Wikipedia targets are 404, disambiguation, or otherwise unhelpful.
2. **Subtitle cleanup, all fact sheets** — strip the leading "Ancestor fact sheet for GXX in the direct Gurney line." (and "Related fact sheet for GXX.") phrase and the trailing "Updated/Published/Initial draft …" provenance phrase.
3. **Children-table formatting, G19–G21** — convert these three sheets' 2-column children tables to the standard 4-column (Name / Dates / Mother / Notes) layout. The current 2-column variant inherits the `td:nth-child(2){white-space:nowrap}` rule meant for the standard layout's Dates column, which forces the Notes column to one un-wrapped line and pushes the table off the page.

## File-pair rule

Every fact-sheet edit below targets the canonical file under `fact-sheets/*.md` **and** its mirror under `site/website/fact-sheets/*.md`. The two were verified byte-identical on 2026-05-16 (e.g. `diff fact-sheets/g19-…md site/website/fact-sheets/g19-…md` → empty). Apply each edit twice, to both paths, to keep them in sync.

## Sources / data referenced

No new `data/sources.json` entry required. The Wikipedia link repoint targets were verified live on 2026-05-16. No research/data files are touched.

---

## 1. Hyperlink audit — G30 through G37 (main body only)

Scope: only links inside the visible main body (vitals, highlights, children, narrative). Sidebar "Related Links" panels and citation footnotes are out of scope for this task.

### 1.1 Verification log (audited 2026-05-16)

Targets confirmed **broken (404)** on en.wikipedia.org:

- `/wiki/Priory_of_Notre-Dame_du_Pr%C3%A9`
- `/wiki/Olim_(French_law)`
- `/wiki/Hardingham,_Norfolk`
- `/wiki/Montigny-sur-Andelle` (also 404 on fr.wikipedia.org; no equivalent French commune article — `Montigny,_Seine-Maritime` is a different village and is **not** a valid repoint)
- `/wiki/Hugh_IV_de_Gournay`
- `/wiki/Gurney_family`
- `/wiki/Mowbray_family`
- `/wiki/Talbot_family`
- `/wiki/Crispin_family`
- `/wiki/James_Hannay_(journalist)` (the disambig at `/wiki/James_Hannay` is not a useful target; remove rather than repoint)
- `/wiki/Danish_invasion_of_England_(1069%E2%80%9370)`
- `/wiki/Walter_I_Giffard`
- `/wiki/Ralph_III_de_Tosny`
- `/wiki/Manass%C3%A8s_de_Gournay`
- `/wiki/William_I,_Duke_of_Normandy_(Longsword)`

Targets confirmed **disambiguation only** (repoint to the correct village/commune):

- `/wiki/Gaywood` → `/wiki/Gaywood,_Norfolk` (substantive)
- `/wiki/Harpley` → `/wiki/Harpley,_Norfolk` (substantive)
- `/wiki/Vaudreuil` → `/wiki/Le_Vaudreuil` (the Eure commune)

Targets confirmed working and **preserved**:

- `/wiki/Hardingham` (substantive — the modern article without the `,_Norfolk` suffix)
- `/wiki/Walter_Giffard,_1st_Earl_of_Buckingham` (substantive)
- `/wiki/William_Longsword` (substantive — the modern article without the older qualified title)
- `/wiki/Harrying_of_the_North` (substantive — but **not** a clean equivalent for the 1069–70 Danish raids on the Norfolk coast, so the original 404 link is removed rather than repointed)
- `/wiki/Bishop_of_%C3%89vreux` and `/wiki/Bishop_of_Bayeux` (both redirect to substantive diocese articles — keep)
- `/wiki/Beauvaisis` (redirects to `/wiki/Beauvais`; not a clean match for the historical region but the only available target — keep)
- `/wiki/West_Barsham` (stub but a real article — keep)
- `/wiki/Phrygia` (general kingdom article — the "Burnt Phrygia" crusader subtopic has no standalone article; keep general target)

### 1.2 G30 — `fact-sheets/g30-william-de-gournay-i-fact-sheet.md`

Mirror: `site/website/fact-sheets/g30-william-de-gournay-i-fact-sheet.md`.

**1.2.a — Vitals → Occupation/Status (line ~52).** Remove the broken `Montigny-sur-Andelle` link **and** the broken `Hardingham,_Norfolk` link; repoint nothing because both targets are 404 (Hardingham has a working alternate). Apply two edits:

Find:
```
in <a href="https://en.wikipedia.org/wiki/Hardingham,_Norfolk">Hardingham</a>, Norfolk. Holder of <a href="https://en.wikipedia.org/wiki/Montigny-sur-Andelle">Montigny-sur-Andelle</a>, Normandy
```
Replace with:
```
in <a href="https://en.wikipedia.org/wiki/Hardingham">Hardingham</a>, Norfolk. Holder of Montigny-sur-Andelle, Normandy
```

**1.2.b — Highlights, first bullet (line ~73).** Remove the `Montigny-sur-Andelle` link only (keep "Pays de Bray" and "parage").

Find:
```
William held the lordship of <a href="https://en.wikipedia.org/wiki/Montigny-sur-Andelle">Montigny-sur-Andelle</a> in the
```
Replace with:
```
William held the lordship of Montigny-sur-Andelle in the
```

**1.2.c — Highlights, second bullet (line ~74).** Repoint Gaywood.

Find:
```
A deed of conveyance for lands in <a href="https://en.wikipedia.org/wiki/Gaywood">Gaywood</a>, Norfolk
```
Replace with:
```
A deed of conveyance for lands in <a href="https://en.wikipedia.org/wiki/Gaywood,_Norfolk">Gaywood</a>, Norfolk
```

**1.2.d — Highlights, third bullet (line ~75).** Remove the `Priory_of_Notre-Dame_du_Pr%C3%A9` link.

Find:
```
to the priory of <a href="https://en.wikipedia.org/wiki/Priory_of_Notre-Dame_du_Pr%C3%A9">Notre Dame du Pré</a> at
```
Replace with:
```
to the priory of Notre Dame du Pré at
```

**1.2.e — Highlights, fourth bullet (line ~76).** Repoint `Hardingham,_Norfolk` → `Hardingham`.

Find:
```
spanning parts of three modern parishes (<a href="https://en.wikipedia.org/wiki/Hardingham,_Norfolk">Hardingham</a>, Letton, and Cranworth)
```
Replace with:
```
spanning parts of three modern parishes (<a href="https://en.wikipedia.org/wiki/Hardingham">Hardingham</a>, Letton, and Cranworth)
```

**1.2.f — Children table, Matthew row (line ~98).** Repoint Harpley.

Find:
```
acquiring <a href="https://en.wikipedia.org/wiki/Harpley">Harpley</a> manor.
```
Replace with:
```
acquiring <a href="https://en.wikipedia.org/wiki/Harpley,_Norfolk">Harpley</a> manor.
```

**1.2.g — Narrative paragraph 1 (line ~107).** Three edits in one paragraph: Gaywood repoint, Montigny link removal, Olim link removal.

Find:
```
His knighthood is established by his designation as "Dominus Willelmus de Gurney" in a <a href="https://en.wikipedia.org/wiki/Gaywood">Gaywood</a> deed. His father-son relationship with Matthew is established by a plea recorded in DG's Appendix LIII. And his Norman holding at <a href="https://en.wikipedia.org/wiki/Montigny-sur-Andelle">Montigny-sur-Andelle</a> is established by the *<a href="https://en.wikipedia.org/wiki/Olim_(French_law)">Registres Olim</a>*
```
Replace with:
```
His knighthood is established by his designation as "Dominus Willelmus de Gurney" in a <a href="https://en.wikipedia.org/wiki/Gaywood,_Norfolk">Gaywood</a> deed. His father-son relationship with Matthew is established by a plea recorded in DG's Appendix LIII. And his Norman holding at Montigny-sur-Andelle is established by the *Registres Olim*
```

**1.2.h — Narrative paragraph 3 (line ~111).** Repoint Hardingham, repoint Runhall stays (Runhall article is substantive).

Find:
```
three modern parishes — <a href="https://en.wikipedia.org/wiki/Hardingham,_Norfolk">Hardingham</a>, Letton, and Cranworth
```
Replace with:
```
three modern parishes — <a href="https://en.wikipedia.org/wiki/Hardingham">Hardingham</a>, Letton, and Cranworth
```

**1.2.i — Narrative paragraph 4 (line ~115).** Repoint Harpley.

Find:
```
secured <a href="https://en.wikipedia.org/wiki/Harpley">Harpley</a> manor
```
Replace with:
```
secured <a href="https://en.wikipedia.org/wiki/Harpley,_Norfolk">Harpley</a> manor
```

### 1.3 G31 — `fact-sheets/g31-walter-de-gournay-fact-sheet.md`

Mirror: `site/website/fact-sheets/g31-walter-de-gournay-fact-sheet.md`.

**1.3.a — Highlights, first bullet (line ~73).** Three link issues: `Hugh_IV_de_Gournay` (404), `Harpley` (disambig), `Gurney_family` (404). The `West_Barsham` link is a stub but a real article — leave it linked.

Find:
```
Walter's elder brother <a href="https://en.wikipedia.org/wiki/Hugh_IV_de_Gournay">Hugh IV</a> inherited the great Norman barony. Walter received a younger son's share of the English estates. From this seemingly minor partition descend the <a href="https://en.wikipedia.org/wiki/Harpley">Harpley</a> Gournays, the <a href="https://en.wikipedia.org/wiki/West_Barsham">West Barsham</a> Gurneys, the <a href="https://en.wikipedia.org/wiki/Gurney_family">Quaker banking Gurneys</a>
```
Replace with:
```
Walter's elder brother Hugh IV inherited the great Norman barony. Walter received a younger son's share of the English estates. From this seemingly minor partition descend the <a href="https://en.wikipedia.org/wiki/Harpley,_Norfolk">Harpley</a> Gournays, the <a href="https://en.wikipedia.org/wiki/West_Barsham">West Barsham</a> Gurneys, the Quaker banking Gurneys
```

**1.3.b — Highlights, second bullet (line ~74).** Remove the `Olim_(French_law)` link, remove the `Montigny-sur-Andelle` link.

Find:
```
The <a href="https://en.wikipedia.org/wiki/Olim_(French_law)"><em>Les Olim</em></a> — official records of the French royal court — formally recognized the Swathings Gurneys as legitimate blood descendants of the Lords of Gournay. Combined with the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a> entry and the <a href="https://en.wikipedia.org/wiki/Parage">parage</a> tenure of <a href="https://en.wikipedia.org/wiki/Montigny-sur-Andelle">Montigny-sur-Andelle</a>
```
Replace with:
```
The <em>Les Olim</em> — official records of the French royal court — formally recognized the Swathings Gurneys as legitimate blood descendants of the Lords of Gournay. Combined with the <a href="https://en.wikipedia.org/wiki/Liber_Niger_Scaccarii"><em>Liber Niger Scaccarii</em></a> entry and the <a href="https://en.wikipedia.org/wiki/Parage">parage</a> tenure of Montigny-sur-Andelle
```

**1.3.c — Children table, William row (line ~99).** Remove the `Montigny-sur-Andelle` link only.

Find:
```
held <a href="https://en.wikipedia.org/wiki/Montigny-sur-Andelle">Montigny-sur-Andelle</a> in Normandy
```
Replace with:
```
held Montigny-sur-Andelle in Normandy
```

**1.3.d — Narrative paragraph 1 (line ~108).** Remove the `Montigny-sur-Andelle` link (appears twice in this paragraph).

Find:
```
the <a href="https://en.wikipedia.org/wiki/Montigny-sur-Andelle">Montigny-sur-Andelle</a> tenure that his son William inherited
```
Replace with:
```
the Montigny-sur-Andelle tenure that his son William inherited
```

**1.3.e — Narrative paragraph 2 (line ~110).** Repoint `Hardingham,_Norfolk` → `Hardingham`, then remove the `Montigny-sur-Andelle` link (appears twice in this paragraph: the in-text mention and "this is precisely the tenure William de Gournay I held for Montigny-sur-Andelle"). Apply as two edits:

Find:
```
<a href="https://en.wikipedia.org/wiki/Runhall">Runhall</a> and Swathings in <a href="https://en.wikipedia.org/wiki/Hardingham,_Norfolk">Hardingham</a>, Norfolk
```
Replace with:
```
<a href="https://en.wikipedia.org/wiki/Runhall">Runhall</a> and Swathings in <a href="https://en.wikipedia.org/wiki/Hardingham">Hardingham</a>, Norfolk
```

Find:
```
the tenure William de Gournay I held for <a href="https://en.wikipedia.org/wiki/Montigny-sur-Andelle">Montigny-sur-Andelle</a>
```
Replace with:
```
the tenure William de Gournay I held for Montigny-sur-Andelle
```

**1.3.f — Narrative paragraph 3 (line ~112).** Remove the `Olim_(French_law)` link.

Find:
```
an entry in the <a href="https://en.wikipedia.org/wiki/Olim_(French_law)"><em>Les Olim</em></a>, the records of the French royal court
```
Replace with:
```
an entry in the <em>Les Olim</em>, the records of the French royal court
```

### 1.4 G32 — `fact-sheets/g32-gerard-de-gournay-fact-sheet.md`

Mirror: `site/website/fact-sheets/g32-gerard-de-gournay-fact-sheet.md`.

**1.4.a — Highlights, third bullet "his daughter *la belle Gondrée*" (line ~77).** Remove `Mowbray_family` link.

Find:
```
<a href="https://en.wikipedia.org/wiki/Mowbray_family">Mowbray</a> line
```
Replace with:
```
Mowbray line
```

**1.4.b — Highlights, JUNCTION POINT bullet (line ~79).** Remove `Hugh_IV_de_Gournay` and `Gurney_family` links.

Find:
```
Gerard's eldest son <a href="https://en.wikipedia.org/wiki/Hugh_IV_de_Gournay">Hugh IV</a> continued the main Norman baron line
```
Replace with:
```
Gerard's eldest son Hugh IV continued the main Norman baron line
```

Find:
```
the <a href="https://en.wikipedia.org/wiki/Gurney_family">banking Gurneys</a>
```
Replace with:
```
the banking Gurneys
```

### 1.5 G33 — `fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`

Mirror: `site/website/fact-sheets/g33-hugh-de-gournay-iii-fact-sheet.md`.

**1.5.a — Highlights, Domesday bullet (line ~80).** Remove `Talbot_family` link.

Find:
```
with sub-tenant "Goisfredus Talbot" — a <a href="https://en.wikipedia.org/wiki/Talbot_family">Talbot</a> serving under a Gournay
```
Replace with:
```
with sub-tenant "Goisfredus Talbot" — a Talbot serving under a Gournay
```

**1.5.b — Narrative final paragraph (line ~121).** Remove `Crispin_family` link.

Find:
```
Eva, wife of <a href="https://en.wikipedia.org/wiki/Crispin_family">William Crispin</a>
```
Replace with:
```
Eva, wife of William Crispin
```

### 1.6 G34 — `fact-sheets/g34-hugh-de-gournay-ii-fact-sheet.md`

Mirror: `site/website/fact-sheets/g34-hugh-de-gournay-ii-fact-sheet.md`.

**1.6.a — Vitals → Died (line ~49).** Remove `Danish_invasion_of_England_(1069%E2%80%9370)` link.

Find:
```
placing the engagement among the <a href="https://en.wikipedia.org/wiki/Danish_invasion_of_England_(1069%E2%80%9370)">Danish raids on England's east coast</a> in 1069–1075
```
Replace with:
```
placing the engagement among the Danish raids on England's east coast in 1069–1075
```

**1.6.b — Vitals → Marriage(s) (line ~63).** Remove `James_Hannay_(journalist)` link.

Find:
```
<a href="https://en.wikipedia.org/wiki/James_Hannay_(journalist)">Hannay</a> noted: "Who his wife was — Frank or Norman — we cannot tell."
```
Replace with:
```
Hannay noted: "Who his wife was — Frank or Norman — we cannot tell."
```

**1.6.c — Highlights, Mortemer bullet (line ~74).** Remove `Ralph_III_de_Tosny` link.

Find:
```
William then sent <a href="https://en.wikipedia.org/wiki/Ralph_III_de_Tosny">Rodolf de Toeny</a> to ride
```
Replace with:
```
William then sent Rodolf de Toeny to ride
```

**1.6.d — Highlights, 1035 expedition bullet (line ~75).** Repoint `Walter_I_Giffard` → `Walter_Giffard,_1st_Earl_of_Buckingham`.

Find:
```
<a href="https://en.wikipedia.org/wiki/Walter_I_Giffard">Walter Giffard, Count of Longueville</a>
```
Replace with:
```
<a href="https://en.wikipedia.org/wiki/Walter_Giffard,_1st_Earl_of_Buckingham">Walter Giffard, Count of Longueville</a>
```

**1.6.e — Narrative paragraph 2 (line ~117).** Repoint `Walter_I_Giffard` (the "Giffart Count of Longueville" mention).

Find:
```
The fleet, including <a href="https://en.wikipedia.org/wiki/Walter_I_Giffard">Giffart Count of Longueville</a>
```
Replace with:
```
The fleet, including <a href="https://en.wikipedia.org/wiki/Walter_Giffard,_1st_Earl_of_Buckingham">Giffart Count of Longueville</a>
```

**1.6.f — Narrative paragraph 3 (line ~119).** Repoint `Walter_I_Giffard` (the Mortemer mention).

Find:
```
alongside the <a href="https://en.wikipedia.org/wiki/County_of_Eu">Count d'Eu</a> and <a href="https://en.wikipedia.org/wiki/Walter_I_Giffard">Walter Giffard</a>
```
Replace with:
```
alongside the <a href="https://en.wikipedia.org/wiki/County_of_Eu">Count d'Eu</a> and <a href="https://en.wikipedia.org/wiki/Walter_Giffard,_1st_Earl_of_Buckingham">Walter Giffard</a>
```

**1.6.g — Narrative paragraph 4 (line ~121).** Repoint `Vaudreuil` (disambiguation) → `Le_Vaudreuil`.

Find:
```
he witnessed another charter at <a href="https://en.wikipedia.org/wiki/Vaudreuil">Vaudreuil</a>
```
Replace with:
```
he witnessed another charter at <a href="https://en.wikipedia.org/wiki/Le_Vaudreuil">Vaudreuil</a>
```

**1.6.h — Narrative final paragraph (line ~127).** Remove `Manass%C3%A8s_de_Gournay` link.

Find:
```
name a <a href="https://en.wikipedia.org/wiki/Manass%C3%A8s_de_Gournay">Manassès de Gournay</a> as a son of Hugh II
```
Replace with:
```
name a Manassès de Gournay as a son of Hugh II
```

### 1.7 G35 — `fact-sheets/g35-renaud-de-gournay-fact-sheet.md`

No broken or unhelpful main-body links found. **No edits.**

### 1.8 G36 — `fact-sheets/g36-hugh-de-gournay-i-fact-sheet.md`

Mirror: `site/website/fact-sheets/g36-hugh-de-gournay-i-fact-sheet.md`.

**1.8.a — Highlights, second bullet (line ~74).** Repoint `William_I,_Duke_of_Normandy_(Longsword)` → `William_Longsword`.

Find:
```
contemporary with Duke <a href="https://en.wikipedia.org/wiki/William_I,_Duke_of_Normandy_(Longsword)">William Longsword</a> (d. 942)
```
Replace with:
```
contemporary with Duke <a href="https://en.wikipedia.org/wiki/William_Longsword">William Longsword</a> (d. 942)
```

**1.8.b — Highlights, fourth bullet (line ~76).** Repoint the second occurrence.

Find:
```
The reign of <a href="https://en.wikipedia.org/wiki/William_I,_Duke_of_Normandy_(Longsword)">William Longsword</a> (c. 927–942)
```
Replace with:
```
The reign of <a href="https://en.wikipedia.org/wiki/William_Longsword">William Longsword</a> (c. 927–942)
```

### 1.9 G37 — `fact-sheets/g37-eudes-de-gournay-fact-sheet.md`

Mirror: `site/website/fact-sheets/g37-eudes-de-gournay-fact-sheet.md`.

**1.9.a — Highlights, first bullet (line ~75).** Remove `James_Hannay_(journalist)` link.

Find:
```
<a href="https://en.wikipedia.org/wiki/James_Hannay_(journalist)">James Hannay</a>, writing in 1867
```
Replace with:
```
James Hannay, writing in 1867
```

---

## 2. Subtitle cleanup — all fact sheets

For each fact sheet listed below, the `subtitle:` front-matter line is replaced. The cleanup strips:

- the leading "Ancestor fact sheet for GXX in the direct Gurney line." sentence (or, for the two "related" sheets, the leading "Related fact sheet for GXX." sentence);
- the trailing provenance sentence (`Updated April 2026.`, `Published April 2026.`, `Published 2 April 2026.`, `Initial draft, April 2026.`, `Initial draft, May 2026.`, etc.).

Where stripping leaves the subtitle starting with a lower-case word or fragment, the first word is recapitalised. Two sheets (`g09`, `g10`) already lack a trailing provenance sentence; only the leading sentence is removed.

For each row: replace the existing `subtitle: "…"` line with the **new** value shown.

| File (also apply to mirror under `site/website/fact-sheets/`) | New `subtitle:` value |
|---|---|
| `g02-lester-hayes-gurney-fact-sheet.md` | `subtitle: "Indiana power engineer, third-generation engineer, Master Mason, Kiwanian, and lifelong Presbyterian."` |
| `g03-lester-sawyer-gurney-iii-fact-sheet.md` | `subtitle: "Wellesley Hills-born power engineer, wartime lieutenant, and father of Lester Hayes Gurney."` |
| `g04-lester-sawyer-gurney-jr-fact-sheet.md` | `subtitle: "Patchogue-raised civil engineer whose life ran from Long Island theatricals to Cape Cod construction work and a later Massachusetts chapter."` |
| `g05-lester-sawyer-gurney-fact-sheet.md` | `subtitle: "New York postal clerk turned Actors’ Fund official, Patchogue summer resident, and master of Continental Lodge No. 287."` |
| `g07-willis-gurney-fact-sheet.md` | `subtitle: "Tailor; first Gurney of the line to leave Massachusetts for New York; settled in Flushing, Queens."` |
| `g08-amos-gurney-fact-sheet.md` | `subtitle: "Cummington, Massachusetts farmer; married Ruth Gilbert; widow Ruth later joined son Willis at Flushing."` |
| `g09-benjamin-gurney-fact-sheet.md` | `subtitle: "Plymouth County farmer born of an unmarried liaison and reportedly raised by his maternal aunt; sold Abington land in 1770 and bought into Cummington with Silas Reed."` |
| `g10-benjamin-gurney-fact-sheet.md` | `subtitle: "Plymouth County farmer whose 1730 liaison with Jane Harden produced Benjamin (G9) before his 1731 marriage to Sarah Morse; the split sends Cummington and Rochester lines in different directions."` |
| `g11-benjamin-gurney-fact-sheet.md` | `subtitle: "Married Rebecca Staples at the First Church of Braintree in 1701; landholder at the Abington–Bridgewater line; will proved 1739."` |
| `g12-richard-gurney-fact-sheet.md` | `subtitle: "Weymouth, Massachusetts proprietor and Freeman 1681; son of John Gurney-1, the colonial emigrant; one of his sons died at the Mendon massacre of 1675."` |
| `g14-francis-gurney-fact-sheet.md` | `subtitle: "Merchant Taylor of London and probable father of John Gurney-1 of Massachusetts."` |
| `g14-edmund-gurney-divine-related-fact-sheet.md` | `subtitle: "Edmund Gurney was not a direct ancestor; he was Henry Gurney's son and Francis Gurney's brother."` |
| `g15-henry-gurney-fact-sheet.md` | `subtitle: "Last Gurney born Roman Catholic; Elizabethan poet and bibliophile of Great Ellingham; father of twelve, including Francis Gurney of London (G14) and Edmund Gurney the Puritan divine."` |
| `g16-francis-gurney-fact-sheet.md` | `subtitle: "Eldest son of Anthony Gurney (G17); died vita patris before his father; husband of Helen Holdich of Ranworth; father of Henry Gurney (G15) the Elizabethan poet."` |
| `g17-anthony-gurney-fact-sheet.md` | `subtitle: "Boy lord of West Barsham; second cousin of Anne Boleyn through his Heydon mother; brought Great Ellingham and the Mortimer of Attleborough lands into the family by marrying Margaret Lovell. Foreman of the Norfolk grand jury that indicted the Earl of Surrey in 1547."` |
| `g17-queen-anne-boleyn-related-fact-sheet.md` | `subtitle: "Queen Anne Boleyn was not a direct ancestor in this line; she was Anthony Gurney's second cousin through the Heydon-Boleyn branch, making her Allen Gurney's second cousin, 16 times removed."` |
| `g18-william-gurney-v-fact-sheet.md` | `subtitle: "Eldest son and heir-apparent of William Gurney IV (G19); died vita patris before his father; husband of Anne Heydon, daughter of Sir Henry Heydon of Baconsthorpe Castle and Anne Boleyn the elder. Brought the Heydon-Boleyn-Howard cousinage into the family."` |
| `g19-william-gurney-iv-fact-sheet.md` | `subtitle: "Of West Barsham and Pockthorpe; Escheator for Norfolk; of council to the Duke of Norfolk 1477; the lord whose 1507 will required 700 sheep to remain at West Barsham."` |
| `g20-thomas-gournay-ii-fact-sheet.md` | `subtitle: "Lord of West Barsham; married into the great recusant Jerningham family of Somerleyton; his will of 1471 survives."` |
| `g21-thomas-gournay-i-fact-sheet.md` | `subtitle: "Nephew and eventual heir of Sir John Gurney V, Sheriff of Norfolk and MP in the 1404 Coventry Parliament. Married Catherine Kerville of Watlington."` |
| `g22-robert-gournay-fact-sheet.md` | `subtitle: "Second son of Edmund Gurney; the line descends through him when his brother Sir John's son died without heirs."` |
| `g23-edmund-gurney-fact-sheet.md` | `subtitle: "Lawyer of eminence; steward of John of Gaunt's East Anglian estates; standing counsel to the city of Norwich; husband of the heiress who brought West Barsham into the family."` |
| `g24-john-de-gournay-iv-fact-sheet.md` | `subtitle: "Lord of Harpley 1354; father of Edmund Gurney, steward of John of Gaunt."` |
| `g25-john-de-gournay-iii-fact-sheet.md` | `subtitle: "Recovered the family estates from his uncle the Rector; Lord of Harpley 1332–c.1353."` |
| `g26-sir-william-de-gournay-iii-fact-sheet.md` | `subtitle: "Last Harpley lord in the direct male line; sold all estates to his brother the Rector; his seal bears the first documented engrailed cross."` |
| `g27-sir-john-de-gournay-i-fact-sheet.md` | `subtitle: "Rebel baron at Lewes, 1264. Crusader with Edward I, 1270. Established the family coat of arms still borne today."` |
| `g28-william-de-gournay-ii-fact-sheet.md` | `subtitle: "Knight; Lord of Harpley; father of the Crusader-turned-rebel Sir John de Gournay I."` |
| `g29-matthew-de-gournay-fact-sheet.md` | `subtitle: "Knight; acquired Harpley manor through a marriage arranged by Hameline Plantagenet, Earl Warren."` |
| `g30-william-de-gournay-i-fact-sheet.md` | `subtitle: "Knight; Lord of Runhall; holder of Montigny-sur-Andelle in Normandy — the parage tenure proving Gournay blood descent."` |
| `g31-walter-de-gournay-fact-sheet.md` | `subtitle: "Junction point: youngest son of Gerard de Gournay; ancestor of all English and American Gurneys."` |
| `g32-gerard-de-gournay-fact-sheet.md` | `subtitle: "Crusader. Married daughter of the wealthiest Norman earl. Died in the Holy Land after the First Crusade."` |
| `g33-hugh-de-gournay-iii-fact-sheet.md` | `subtitle: "At the Battle of Hastings, 1066. Domesday landholder in Essex and Norfolk. Personal friend of St. Anselm. Buried Abbey of Bec."` |
| `g34-hugh-de-gournay-ii-fact-sheet.md` | `subtitle: "Norman battle commander; ducal charter witness; one of the Conqueror's most trusted barons."` |
| `g35-renaud-de-gournay-fact-sheet.md` | `subtitle: "First Lord of Gournay confirmed in a surviving primary source document."` |
| `g36-hugh-de-gournay-i-fact-sheet.md` | `subtitle: "First lord born in Gournay; builder of the fortress that defined the town."` |
| `g37-eudes-de-gournay-fact-sheet.md` | `subtitle: "Viking warrior and traditional first lord of Gournay-en-Bray."` |

Note: G13 (`g13-…`) has no published fact sheet in `fact-sheets/`; it currently lives as research-only. No edit required.

The front-matter `updated:` field on each sheet is preserved as-is — it is a separate machine-readable field, not the subtitle.

---

## 3. Children-table conversion — G19, G20, G21

### 3.1 Why these three

The page CSS (`site/website/assets/site.css:587`) is:

```css
.factsheet-page .facts-children td:nth-child(2),
.factsheet-page .facts-children th:nth-child(2){white-space:nowrap}
```

In the project-standard 4-column children table (Name / Dates / Mother / Notes), column 2 is short Dates — `nowrap` is appropriate. G19, G20, and G21 use a non-standard 2-column children table (Name / Notes), so the same rule pins the long Notes column to a single un-wrapped line and pushes the table off the right edge. Conforming these three sheets to the 4-column layout used everywhere else fixes the overflow without touching CSS.

Dates and mothers populated below come from each sheet's own Vitals → Marriage(s) and from sibling fact sheets already in the repo. Where a child's dates are not given in any consulted source, the cell holds an em dash (`—`); leaving cells empty would create vertical alignment glitches.

### 3.2 G19 — `fact-sheets/g19-william-gurney-iv-fact-sheet.md`

Mirror: `site/website/fact-sheets/g19-william-gurney-iv-fact-sheet.md`.

William Gurney IV had one wife, Anne Calthorpe, so all eleven children share that mother. Only William V's dates are recoverable here (he died *vitae patris* before his father, who died 18 January 1508).

Find the entire children-section block (lines 86–143 in the canonical file):

```
<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>William Gurney V</strong></td>
      <td><strong>G18 in the direct line.</strong> Eldest son. Of Irstead. Married Anne Heydon of Baconsthorpe Castle, bringing Boleyn descent into the family. Died <em>vita patris</em> before his father. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></td>
    </tr>
    <tr>
      <td>John Gurney</td>
      <td>Named in Daniel Gurney, <em>Record</em> (1848), pedigree p. 287. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup></td>
    </tr>
    <tr>
      <td>Edmund Gurney</td>
      <td>Named in Daniel Gurney, <em>Record</em> (1848), pedigree p. 287. <sup class="fn"><a href="#n12" id="ref-12b">12</a></sup></td>
    </tr>
    <tr>
      <td>Walter Gurney of Cley-by-the-Sea</td>
      <td>Norfolk. Per DG, "ancestor of the Gurneys of Gawston and Aylsham." Founder of an extant collateral cadet branch. <sup class="fn"><a href="#n13" id="ref-13">13</a></sup></td>
    </tr>
    <tr>
      <td>Thomas Gurney</td>
      <td>Per DG: "his father's executor, ancestor of the Gurneys of Dartmouth, London, and Essex temp. Elizabeth, 1590; his grandson, Richard Gurney, was Sheriff of London." A significant collateral line. <sup class="fn"><a href="#n13" id="ref-13b">13</a></sup></td>
    </tr>
    <tr>
      <td>Christopher Gurney</td>
      <td>A priest, rector of Harpley. <sup class="fn"><a href="#n12" id="ref-12c">12</a></sup></td>
    </tr>
    <tr>
      <td>Constance Gurney</td>
      <td>Married (1) Ralf Blundeville, (2) William Bokenham. <sup class="fn"><a href="#n12" id="ref-12d">12</a></sup></td>
    </tr>
    <tr>
      <td>Frances Gurney</td>
      <td>Married a Gascoigne of Yorkshire. <sup class="fn"><a href="#n12" id="ref-12e">12</a></sup></td>
    </tr>
    <tr>
      <td>Alice Gurney</td>
      <td>Married Henry Dengaine, Esq., of Brunstead, Norfolk. <sup class="fn"><a href="#n12" id="ref-12f">12</a></sup></td>
    </tr>
    <tr>
      <td>Amy Gurney</td>
      <td>Married John Sybsey, Gent. <sup class="fn"><a href="#n12" id="ref-12g">12</a></sup></td>
    </tr>
    <tr>
      <td>Elizabeth Gurney</td>
      <td><strong>Prioress of Thetford, 1518.</strong> A significant ecclesiastical position — Thetford had been one of the great Norfolk monastic houses. Her election to the prioress role on the eve of the Henrician dissolutions is the most distinguished individual achievement of any of William IV's children. <sup class="fn"><a href="#n12" id="ref-12h">12</a></sup></td>
    </tr>
  </tbody>
</table>
</section>
```

Replace with:

```
<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Dates</th>
      <th>Mother</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>William Gurney V</strong></td>
      <td>fl. late 15th c. – d. <em>vita patris</em> before 1508</td>
      <td>Anne Calthorpe</td>
      <td><strong>G18 in the direct line.</strong> Eldest son. Of Irstead. Married Anne Heydon of Baconsthorpe Castle, bringing Boleyn descent into the family. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></td>
    </tr>
    <tr>
      <td>John Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Named in Daniel Gurney, <em>Record</em> (1848), pedigree p. 287. <sup class="fn"><a href="#n12" id="ref-12">12</a></sup></td>
    </tr>
    <tr>
      <td>Edmund Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Named in Daniel Gurney, <em>Record</em> (1848), pedigree p. 287. <sup class="fn"><a href="#n12" id="ref-12b">12</a></sup></td>
    </tr>
    <tr>
      <td>Walter Gurney of Cley-by-the-Sea</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Norfolk. Per DG, "ancestor of the Gurneys of Gawston and Aylsham." Founder of an extant collateral cadet branch. <sup class="fn"><a href="#n13" id="ref-13">13</a></sup></td>
    </tr>
    <tr>
      <td>Thomas Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Per DG: "his father's executor, ancestor of the Gurneys of Dartmouth, London, and Essex temp. Elizabeth, 1590; his grandson, Richard Gurney, was Sheriff of London." A significant collateral line. <sup class="fn"><a href="#n13" id="ref-13b">13</a></sup></td>
    </tr>
    <tr>
      <td>Christopher Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>A priest, rector of Harpley. <sup class="fn"><a href="#n12" id="ref-12c">12</a></sup></td>
    </tr>
    <tr>
      <td>Constance Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Married (1) Ralf Blundeville, (2) William Bokenham. <sup class="fn"><a href="#n12" id="ref-12d">12</a></sup></td>
    </tr>
    <tr>
      <td>Frances Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Married a Gascoigne of Yorkshire. <sup class="fn"><a href="#n12" id="ref-12e">12</a></sup></td>
    </tr>
    <tr>
      <td>Alice Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Married Henry Dengaine, Esq., of Brunstead, Norfolk. <sup class="fn"><a href="#n12" id="ref-12f">12</a></sup></td>
    </tr>
    <tr>
      <td>Amy Gurney</td>
      <td>—</td>
      <td>Anne Calthorpe</td>
      <td>Married John Sybsey, Gent. <sup class="fn"><a href="#n12" id="ref-12g">12</a></sup></td>
    </tr>
    <tr>
      <td>Elizabeth Gurney</td>
      <td>fl. 1518</td>
      <td>Anne Calthorpe</td>
      <td><strong>Prioress of Thetford, 1518.</strong> A significant ecclesiastical position — Thetford had been one of the great Norfolk monastic houses. Her election to the prioress role on the eve of the Henrician dissolutions is the most distinguished individual achievement of any of William IV's children. <sup class="fn"><a href="#n12" id="ref-12h">12</a></sup></td>
    </tr>
  </tbody>
</table>
</section>
```

### 3.3 G20 — `fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`

Mirror: `site/website/fact-sheets/g20-thomas-gournay-ii-fact-sheet.md`.

Find the entire children-section block (lines 85–104 in the canonical file):

```
<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>William Gurney IV</strong></td>
      <td><strong>G19 in the direct line.</strong> Son and heir. Of West Barsham and Pockthorpe-by-Norwich. Escheator for Norfolk under Edward IV; of council to the Duke of Norfolk 1477; married Anne Calthorpe, daughter of Sir William Calthorpe KB of Burnham Thorpe. Died 18 January 1508. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></td>
    </tr>
  </tbody>
</table>

<p><em>Daniel Gurney, <em>Record</em> (1848), pedigree p. 287 names only William IV as Thomas II's issue. Further children, if any, are not recorded in the sources consulted.</em></p>
</section>
```

Replace with:

```
<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Dates</th>
      <th>Mother</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>William Gurney IV</strong></td>
      <td>c. 1450 – 18 Jan 1508</td>
      <td>Margaret Jerningham</td>
      <td><strong>G19 in the direct line.</strong> Son and heir. Of West Barsham and Pockthorpe-by-Norwich. Escheator for Norfolk under Edward IV; of council to the Duke of Norfolk 1477; married Anne Calthorpe, daughter of Sir William Calthorpe KB of Burnham Thorpe. <sup class="fn"><a href="#n11" id="ref-11">11</a></sup></td>
    </tr>
  </tbody>
</table>

<p><em>Daniel Gurney, <em>Record</em> (1848), pedigree p. 287 names only William IV as Thomas II's issue. Further children, if any, are not recorded in the sources consulted.</em></p>
</section>
```

### 3.4 G21 — `fact-sheets/g21-thomas-gournay-i-fact-sheet.md`

Mirror: `site/website/fact-sheets/g21-thomas-gournay-i-fact-sheet.md`.

Find the entire children-section block (lines 85–104 in the canonical file):

```
<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Thomas Gournay II</strong></td>
      <td><strong>G20 in the direct line.</strong> Son and heir. Of West Barsham, Harpley, and a Norwich town house in St Gregory's parish. Married Margaret Jerningham of Somerleyton, Suffolk. Will proved 27 July 1471. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></td>
    </tr>
  </tbody>
</table>

<p><em>Daniel Gurney, <em>Record</em> (1848) pedigree p. 286 names only Thomas II as the issue of Thomas I's marriage. Further children, if any, are not recorded in the sources consulted.</em></p>
</section>
```

Replace with:

```
<section class="fact-section" id="children">
<h2 class="unnumbered">Children</h2>

<table class="facts-children">
  <thead>
    <tr>
      <th>Name</th>
      <th>Dates</th>
      <th>Mother</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Thomas Gournay II</strong></td>
      <td>c. 1430 – will proved 27 Jul 1471</td>
      <td>Catherine Kerville</td>
      <td><strong>G20 in the direct line.</strong> Son and heir. Of West Barsham, Harpley, and a Norwich town house in St Gregory's parish. Married Margaret Jerningham of Somerleyton, Suffolk. <sup class="fn"><a href="#n10" id="ref-10">10</a></sup></td>
    </tr>
  </tbody>
</table>

<p><em>Daniel Gurney, <em>Record</em> (1848) pedigree p. 286 names only Thomas II as the issue of Thomas I's marriage. Further children, if any, are not recorded in the sources consulted.</em></p>
</section>
```

---

## 4. Phase-2 application checklist

Phase 2 (apply) is a separate session. The applier should:

1. For each Section 1 find/replace pair: apply to both the `fact-sheets/` file and its `site/website/fact-sheets/` mirror.
2. For each Section 2 row: replace the existing `subtitle: "…"` front-matter line in both copies.
3. For each Section 3 block replacement: apply in both copies.
4. Re-verify the file pairs are still byte-identical after edits (`diff fact-sheets/gNN-…md site/website/fact-sheets/gNN-…md` → empty).
5. Spot-check the rendered G19 children table in a local preview — Notes column should now wrap rather than spill horizontally.
6. No `data/sources.json` edits. No `research/` edits. No file moves under `sources/`.
7. Do not archive any session — this patchset originated from an in-session task, not from `sources/intake/new/`.

## 5. Unresolved / out-of-scope notes

- The "Burnt Phrygia" reference in G32 still points to the general `/wiki/Phrygia` article. Acceptable because no standalone "Burnt Phrygia" article exists; the general article is the best available target.
- `/wiki/Beauvaisis` (G33 narrative) redirects to `/wiki/Beauvais`. Not a clean match for the historical region but the only target Wikipedia offers; left as-is.
- `/wiki/West_Barsham` is a stub article. Left linked because it is a real article with at least one substantive sentence; removing would lose a real (if minimal) target.
- The two-column Notes / Mother / Dates fill-in for G19's collateral children uses "—" rather than guessing. If additional dates surface in `research/people/` later, those cells can be filled in incrementally.
- Sidebar "Related Links" panels were not audited. They use a separate visual treatment and were out of scope per the request ("main body helper hyperlinks").
