# NRO PD 86/41 — local-only masters

**Reason held locally:** paywalled subscription content. These are FindMyPast deliveries of the Norfolk
Record Office's digitisation of PD 86/41, under the NRO/FindMyPast licence.

**Source:** Norfolk Record Office, **PD 86/41, "Indented register bills, 1593–1641"**, East Dereham
parish records (PD 86 › Registration Papers, 1593–1954). Digitised as **110 contiguous images,
`4034129-00692` – `4034129-00801`**, each catalogued individually in the NRO online catalogue.
Source ID: `nro-pd-86-41`.

**Retrieval.** FindMyPast, record set *Norfolk Parish Registers Browse*, "East Dereham / Register Bills /
1593-1640 / PD 86/41 / 110 images". Viewer URL pattern — `id` and `parentid` must be the **same** value
or the request 500s:

```bash
echo "https://search.findmypast.co.uk/record?id=gbprs%2fnorfolk%2fpd_86-41%2f00769&parentid=gbprs%2fnorfolk%2fpd_86-41%2f00769"
```

FindMyPast page *N* = NRO image `006` + `(691 + N)` — page 1 is `00692`, page 110 is `00801`. The same
images are served by Ancestry collection 61045 under media ids `4034129_00nnn`.

## What is held here

**34 files, `pd_86-41_00692.jpg` and `pd_86-41_00769.jpg` – `pd_86-41_00801.jpg`** (~34 MB), pulled
2026-07-27. These are the leaves the March–July 2026 analysis never reached: its run was
`00693`–`00768`, which is 76 of the file's 110 images. The earlier 76 are held separately at
`sources/intake/paleography-staging/east-dereham-re-review-july-2026/original-content/Parish_Register/`
(same FindMyPast delivery, filenames `gbprs_norfolk_pd_86-41_000nn.jpg`).

Between them the two sets are the complete file.

## Year map of the tail (read from the membrane heads, 2026-07-27)

| Images | Content |
|---|---|
| 00692 | film target card — "NORFOLK RECORD OFFICE… EAST DEREHAM… PARISH REGISTERS… REGISTER BILLS" |
| 00769 | foot of the preceding return |
| 00770 / 00771 | **1635-36** (pencil annotation, head of membrane) |
| 00772–00776 | 1635–1636 continuation |
| 00777 / 00778 | **1635/6**, endorsed *Duplicate* |
| 00779 / 00780 | **1636-37** — "Bills indented… 1636 unto the 25 of march 1637, John Bretton being vicar" |
| 00781–00782 | 1636-37 continuation |
| 00783 / 00784 | **1637-38** |
| 00785–00792 | 1637–1640 continuation |
| 00793 / 00794 | **1640-41** (PD 86/41/20) |
| 00795–00798 | 1640-41 continuation; 00798 is the last membrane |
| 00799 | **END OF ITEM** target card |
| 00800 / 00801 | leader / blank frames |

The tail is strictly chronological and carries nothing before 1635.

**See** `sources/validations/east-dereham-pd-86-41-register-structure-and-chronology.md` for the
whole-file year map and the 1611–1615 finding.
