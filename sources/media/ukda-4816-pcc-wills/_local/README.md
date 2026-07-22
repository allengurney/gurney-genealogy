# UKDS SN 4816 — Prerogative Court of Canterbury Wills, 1384–1858 (local-only)

Full name-index to the wills proved in the Prerogative Court of Canterbury (PCC),
i.e. The National Archives series **PROB 11**. Deposited at the UK Data Service as
Study Number **4816**. The `.tab` files in this folder are the tab-delimited index
tables; the actual will images live at TNA / Discovery.

## Why this is local-only
UK Data Service data is released under the **UKDS End User Licence**; redistribution
is restricted. The bytes are therefore **gitignored** (`sources/media/*/_local/*`)
and must never be committed or pushed. This README is the committed stub; the data
stays on this machine only.

- **Canonical source:** UK Data Service, https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=4816 (SN 4816).
- **Underlying records:** TNA PROB 11 (register copies of PCC wills), searchable image-by-image at Discovery (nationalarchives.gov.uk).
- **Access level:** Safeguarded (UKDS registration + EUL acceptance required).

## Files
Period-sharded index tables plus one linking table:

- `wills_pre1400.tab`, `wills_1400_1499.tab`, `wills_1500_1599.tab`,
  `wills_1600_1624.tab`, `wills_1625_1649.tab`, … through `wills_1850_1858.tab`
  — one row per will, sharded by proving date.
- `wills_piece_data.tab` — maps each `cat_id` to its TNA catalogue reference
  (`PROB 11/<piece>`), register name, and quire range.

### Will-row columns
`cat_id · will_sentence · title · forename · surname · occupation · geog_info ·
parish_place · county_country · date · first_date · last_date · edoc_id ·
image_id · year`

### Piece-data columns
`catalogue_ref · piece_ref · name_of_register_or_volume_number · quire_number · cat_id`

Join on `cat_id` to turn an index hit into an orderable `PROB 11/<piece>` reference.

## Searching (token-efficient, via repo_search)
These files are gitignored, so they are **not** in the shared search index and
are invisible to `repo_search.py search` / `locate` (both honour `.gitignore`).
Search them directly with the `infile` subcommand, which reads named files from
disk — pass this folder as the target:

```
# exact surname sweep, one clean row per hit across every period shard
python tools/repo_search.py infile sources/media/ukda-4816-pcc-wills/_local \
  --terms Gurney --no-fuzzy --window 1 --context 0

# with curated Gurney/Gournay/Gurnay surname-family expansion
python tools/repo_search.py infile sources/media/ukda-4816-pcc-wills/_local \
  --terms Gurney --variants conservative --name-variants english --no-fuzzy --window 1 --context 0
```

Notes:
- `--window 1 --context 0` yields exactly one `.tab` row per match (each row is a
  self-contained will record). Drop `--window 1` to also see the adjacent row.
- Narrow to one shard by naming the `.tab` file instead of the folder (much faster
  than the full ~137 MB sweep, which takes ~30 s in Python).
- `.tab` is registered in `tools/repo_search_config.json` `textExtensions`, so the
  folder argument expands to all shards. These files are gitignored, so `search`
  and `locate` cannot see them — `infile` is the access path.
