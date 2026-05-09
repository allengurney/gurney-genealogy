# West and North Barsham Former-Parish / Manor-Rights Proxy Overlays — Draft

This package contains a first-pass GeoJSON overlay for **West Barsham** and **North Barsham** only.

## Files

- `west_north_barsham_rights_proxy_overlays_draft.geojson`
- website-facing copy: `site/website/assets/data/west-north-barsham-rights-proxy-overlays.geojson`

## Included features

| Feature | Approx. area | Rights status | Certainty |
|---|---:|---|---|
| North Barsham Wauncy-Gurney Former-Parish Rights Proxy | 833.8 acres | direct Gurney/Wauncy rights proxy | medium-low |
| West Barsham Manor / Former-Parish Rights Proxy | 1571.0 acres | direct Gurney/Wauncy rights proxy | medium |

## Removed from prior draft

The prior draft also included East Barsham and Houghton St Giles as context-only layers. Those have been removed because they were not part of the requested Gurney/Wauncy rights overlay set.

## Important limitation

These polygons are **not** digitized medieval manor boundaries, exact former parish boundaries, or legal/cadastral boundaries.

They are draft proxy polygons built from:
- public locality coordinates for West Barsham and North Barsham;
- the published modern Barsham civil parish area used in the original partition model;
- the pasted Claude analysis recommending a West Barsham parish/manor proxy of about 1,571 acres;
- a generalized non-overlapping proxy split used only to create reviewable geometry.

West Barsham is area-calibrated to approximately **1,571 acres**. North Barsham is a lower-certainty adjacent Wauncy-Gurney rights proxy and should be replaced with a digitized former-parish or manor boundary when available.

## Map display

The ancestor map displays the default-on proxy polygons through the `barsham_former_parish_rights_proxies` overlay group. The source center points remain in the GeoJSON as review metadata with `display_default: false`.

The overlay should be read as a generation-specific rights proxy for the West Barsham / North Barsham Wauncy-Gurney inheritance geography, not as a canonical place record and not as a surveyed parish, manor, or cadastral boundary.

## Next improvement

Replace these draft generalized proxy cells with manually digitized boundaries from:
- NLS OS Six-Inch / 25-Inch historic maps,
- Vision of Britain boundary viewer,
- tithe map / apportionment if available,
- parish boundary data if licensable.
