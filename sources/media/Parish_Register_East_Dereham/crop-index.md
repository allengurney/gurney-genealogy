# East Dereham burial-target crop index

Pre-work crops for the burial-detail review requested 2026-05-15.

Method: cropped the parchment/register sheet area from each target image, excluding the gray board and white "Soiled/Faded Document" handling markers as far as practical. Each crop was converted to grayscale, contrast-enhanced with `PIL ImageEnhance.Contrast(1.6)`, resized to 1.5x, and saved as PNG.

Target words for later close review: Margaret, Margt, ffrancis, Gurnie, Gurney, Gurnoy, Gurny, Rybett, Ryvett, and "wife of ffrancis" forms.

Visual impressions here are contact-sheet level only, not a full paleographic scan. I did not identify a confident Margaret/Rybett/Gurney burial candidate at this pass.

| Source image | Crop output | Crop box `(left, top, right, bottom)` | Visual impression |
|---|---|---:|---|
| `gbprs_norfolk_pd_86-41_00725.jpg` | `crop_00725_enhanced.png` | `(1605, 650, 3135, 3355)` | Dense, badly stained register page; useful for the Susan/Mary year-truncated burial context. |
| `gbprs_norfolk_pd_86-41_00728.jpg` | `crop_00728_enhanced.png` | `(1760, 560, 2957, 3815)` | Dense entries; upper and lower sections separated by damage/stain. |
| `gbprs_norfolk_pd_86-41_00729.jpg` | `crop_00729_enhanced.png` | `(1755, 560, 2920, 3815)` | Dense entries with heavy staining on left side. |
| `gbprs_norfolk_pd_86-41_00730.jpg` | `crop_00730_enhanced.png` | `(1751, 450, 2909, 3815)` | Dense entries; left margin is degraded but line structure is visible. |
| `gbprs_norfolk_pd_86-41_00731.jpg` | `crop_00731_enhanced.png` | `(1772, 450, 2937, 3810)` | Dense entries; lower section is more faded. |
| `gbprs_norfolk_pd_86-41_00732.jpg` | `crop_00732_enhanced.png` | `(935, 330, 2245, 3810)` | Tall, comparatively legible page; has a clear heading/date area. |
| `gbprs_norfolk_pd_86-41_00733.jpg` | `crop_00733_enhanced.png` | `(2515, 360, 3873, 3740)` | Dense entries with severe left-side staining. |
| `gbprs_norfolk_pd_86-41_00734.jpg` | `crop_00734_enhanced.png` | `(1636, 330, 2993, 3805)` | Faded but readable line layout; worth close review. |
| `gbprs_norfolk_pd_86-41_00735.jpg` | `crop_00735_enhanced.png` | `(1618, 350, 2974, 3815)` | Clear heading/date area and dense entries; high-priority bridge page before 00736. |
| `gbprs_norfolk_pd_86-41_00736.jpg` | `crop_00736_enhanced.png` | `(425, 350, 1769, 3800)` | Marye 1618 baptism page; nearby lines are reasonably visible. |
| `gbprs_norfolk_pd_86-41_00750.jpg` | `crop_00750_enhanced.png` | `(1605, 920, 2908, 2850)` | Sparse, partial page with faint short entries. |
| `gbprs_norfolk_pd_86-41_00751.jpg` | `crop_00751_enhanced.png` | `(1575, 930, 2871, 2860)` | Sparse, partial page similar to 00750; likely useful mainly for section/context. |
| `gbprs_norfolk_pd_86-41_00752.jpg` | `crop_00752_enhanced.png` | `(1560, 400, 2886, 3810)` | Back-of-volume page with heading/date area and dense list entries. |
| `gbprs_norfolk_pd_86-41_00753.jpg` | `crop_00753_enhanced.png` | `(1702, 390, 3030, 3785)` | Dense, relatively even page; good candidate for close zoom scanning. |
| `gbprs_norfolk_pd_86-41_00754.jpg` | `crop_00754_enhanced.png` | `(1655, 400, 3005, 3780)` | Dense page with visible heading/date area. |
| `gbprs_norfolk_pd_86-41_00755.jpg` | `crop_00755_enhanced.png` | `(1671, 360, 3019, 3750)` | Dense page; lower lines look comparatively clear. |
| `gbprs_norfolk_pd_86-41_00756.jpg` | `crop_00756_enhanced.png` | `(2563, 350, 3928, 3815)` | New heading/page start; heavy staining but a useful section marker. |
| `gbprs_norfolk_pd_86-41_00757.jpg` | `crop_00757_enhanced.png` | `(2586, 330, 3966, 3815)` | Similar to 00756; heading/date area and dense lower entries. |
| `gbprs_norfolk_pd_86-41_00758.jpg` | `crop_00758_enhanced.png` | `(1489, 390, 2988, 3810)` | Dense entries with right-side staining; some left-edge board shadow remains outside text. |
| `gbprs_norfolk_pd_86-41_00759.jpg` | `crop_00759_enhanced.png` | `(1482, 390, 2950, 3810)` | Dense entries, similar to 00758; target scan should focus beyond the upper stain. |
| `gbprs_norfolk_pd_86-41_00760.jpg` | `crop_00760_enhanced.png` | `(1660, 400, 3145, 3815)` | Dense entries with central stain; lower half may be more productive. |
| `gbprs_norfolk_pd_86-41_00761.jpg` | `crop_00761_enhanced.png` | `(1504, 390, 3216, 3815)` | Dense page; left margin includes slight board/shadow to preserve the page edge. |
| `gbprs_norfolk_pd_86-41_00762.jpg` | `crop_00762_enhanced.png` | `(1646, 380, 3094, 3810)` | Dense entries with pale ink; suitable for close enhancement comparison. |
| `gbprs_norfolk_pd_86-41_00763.jpg` | `crop_00763_enhanced.png` | `(1610, 390, 3050, 3815)` | Dense entries with heavy lower staining. |
| `gbprs_norfolk_pd_86-41_00764.jpg` | `crop_00764_enhanced.png` | `(1679, 350, 3079, 3815)` | Broken/sectioned page layout; title/date areas need close confirmation. |
| `gbprs_norfolk_pd_86-41_00765.jpg` | `crop_00765_enhanced.png` | `(3018, 360, 4380, 3815)` | Sectioned page with upper and lower groups; lower section may be useful. |
| `gbprs_norfolk_pd_86-41_00766.jpg` | `crop_00766_enhanced.png` | `(1719, 330, 3039, 3815)` | Dense page with pale upper writing and darker lower entries. |
| `gbprs_norfolk_pd_86-41_00767.jpg` | `crop_00767_enhanced.png` | `(1703, 360, 3015, 3810)` | Dense entries; lower stain overlaps some target zones. |
| `gbprs_norfolk_pd_86-41_00768.jpg` | `crop_00768_enhanced.png` | `(1778, 390, 3100, 3785)` | Dense page with split/offset lower section; close review needed for line continuity. |

## Supplemental 00737-00749 Gurney-review crops

Generated 2026-05-16 during the follow-on Gurney/Francis review of pages 00737-00768. These were auto-cropped to the tall parchment/register strip and contrast-enhanced at 1.5x scale using `tools/east_dereham_image_sweeps.py scan-737-plus`.

| Source image | Crop output | Crop box `(left, top, right, bottom)` | Visual impression |
|---|---|---:|---|
| `gbprs_norfolk_pd_86-41_00737.jpg` | `crop_00737_enhanced.png` | `(2278, 382, 3706, 3778)` | 1620 page with burial and marriage sections; probable Grisell Gurney marriage line identified in the lower section. |
| `gbprs_norfolk_pd_86-41_00738.jpg` | `crop_00738_enhanced.png` | `(1550, 358, 2962, 3786)` | Burial page; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00739.jpg` | `crop_00739_enhanced.png` | `(1598, 326, 2930, 3826)` | 1624 burial page; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00740.jpg` | `crop_00740_enhanced.png` | `(1574, 422, 2994, 3826)` | Faded/stained continuation page; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00741.jpg` | `crop_00741_enhanced.png` | `(1606, 350, 3034, 3834)` | Faded/stained continuation page; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00742.jpg` | `crop_00742_enhanced.png` | `(1654, 366, 3034, 3826)` | Burial page duplicate/near-duplicate view; William Gurney burial line identified. |
| `gbprs_norfolk_pd_86-41_00743.jpg` | `crop_00743_enhanced.png` | `(1630, 382, 3002, 3826)` | Burial page duplicate/near-duplicate view; William Gurney burial line identified. |
| `gbprs_norfolk_pd_86-41_00744.jpg` | `crop_00744_enhanced.png` | `(1558, 478, 2994, 3842)` | Lower page continuation; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00745.jpg` | `crop_00745_enhanced.png` | `(1582, 430, 3034, 3850)` | Duplicate/near-duplicate continuation view; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00746.jpg` | `crop_00746_enhanced.png` | `(1686, 334, 3010, 3826)` | Mixed marriage/burial page; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00747.jpg` | `crop_00747_enhanced.png` | `(1654, 342, 2978, 3834)` | Duplicate/near-duplicate of 00746; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00748.jpg` | `crop_00748_enhanced.png` | `(1742, 382, 3098, 3778)` | Burial page; no Gurney-family line flagged in this pass. |
| `gbprs_norfolk_pd_86-41_00749.jpg` | `crop_00749_enhanced.png` | `(1774, 382, 3130, 3802)` | Duplicate/near-duplicate of 00748; no Gurney-family line flagged in this pass. |
