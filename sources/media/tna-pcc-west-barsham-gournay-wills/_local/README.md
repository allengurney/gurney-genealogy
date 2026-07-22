# sources/media/tna-pcc-west-barsham-gournay-wills/_local/

Local-only masters for `tna-pcc-west-barsham-gournay-wills`. Contents are **gitignored**
and never pushed to GitHub.

**Reason: copyright-restricted.** The TNA facsimile pages carry the footer
*"COPYRIGHT PHOTOGRAPH — NOT TO BE REPRODUCED PHOTOGRAPHICALLY WITHOUT PERMISSION."*
The underlying wills are public records, but these photographic reproductions are not
redistributable, so the bytes stay local.

| File | Size | What it is |
|---|---|---|
| `PROB-11-188-136.pdf` | 2.7 MB | TNA download — will of Edward Gournay of West Barsham, esq., proved 8 Feb 1642 |
| `PROB-11-303-284.pdf` | 2.5 MB | TNA download — will of Henry Gourney of West Barsham, esq., proved 11 Feb 1661 |
| `packet-55-edward-gournay-1642-p001.png` / `-p002.png` | ~21 MB | 300 dpi page renders of PROB 11/188/136 |
| `packet-54-henry-gourney-1661-p001.png` / `-p002.png` | ~17 MB | 300 dpi page renders of PROB 11/303/284 |

**Canonical source.** The National Archives, Kew. Order or re-download from Discovery:

- PROB 11/188/136 — https://discovery.nationalarchives.gov.uk/details/r/D856077
- PROB 11/303/284 — https://discovery.nationalarchives.gov.uk/details/r/D837411

Both are free to download for signed-in Discovery account holders.

**Regenerating the page images.** From either PDF:

```
.\.venv\Scripts\python.exe tools\paleography_image_workbench.py render-pdf <file>.pdf --page 1 --dpi 300 --out <out>.png
```

Analysis crops, line strips and enhancement sheets used for the transcription are
regenerable from these masters and were not retained.

## Cross-reference
- Transcriptions: `sources/corpus_supplement/tna-pcc-west-barsham-gournay-wills.md`
- Validation: `sources/validations/tna-pcc-west-barsham-gournay-wills.md`
