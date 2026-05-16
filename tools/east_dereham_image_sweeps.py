"""Generate East Dereham parish-register crop and enhancement sheets.

This utility preserves the image-processing workflow used for the East
Dereham PD 86/41 pre-analysis artifacts under
sources/media/Parish_Register_East_Dereham.

Typical use from the repository root:

    python tools/east_dereham_image_sweeps.py next-pulls
    python tools/east_dereham_image_sweeps.py scan-737-plus

The default command writes the next-pull artifacts requested in
sources/media/Parish_Register_East_Dereham/next-pull-specifications.md.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

try:
    import cv2  # type: ignore
except Exception:  # pragma: no cover - optional local enhancement path
    cv2 = None

try:
    import numpy as np  # type: ignore
except Exception:  # pragma: no cover - optional local crop path
    np = None


REPO_ROOT = Path(__file__).resolve().parents[1]
MEDIA_DIR = REPO_ROOT / "sources" / "media" / "Parish_Register_East_Dereham"


@dataclass(frozen=True)
class CropInfo:
    box: tuple[int, int, int, int]
    enhanced_size: tuple[int, int]


CROP_INDEX: dict[str, CropInfo] = {
    "00725": CropInfo((1605, 650, 3135, 3355), (2295, 4058)),
    "00728": CropInfo((1760, 560, 2957, 3815), (1796, 4882)),
    "00729": CropInfo((1755, 560, 2920, 3815), (1748, 4882)),
    "00730": CropInfo((1751, 450, 2909, 3815), (1737, 5048)),
    "00731": CropInfo((1772, 450, 2937, 3810), (1748, 5040)),
    "00732": CropInfo((935, 330, 2245, 3810), (1965, 5220)),
    "00733": CropInfo((2515, 360, 3873, 3740), (2037, 5070)),
    "00734": CropInfo((1636, 330, 2993, 3805), (2036, 5212)),
    "00735": CropInfo((1618, 350, 2974, 3815), (2034, 5198)),
    "00736": CropInfo((425, 350, 1769, 3800), (2016, 5175)),
    "00750": CropInfo((1605, 920, 2908, 2850), (1954, 2895)),
    "00751": CropInfo((1575, 930, 2871, 2860), (1944, 2895)),
    "00752": CropInfo((1560, 400, 2886, 3810), (1989, 5115)),
    "00753": CropInfo((1702, 390, 3030, 3785), (1992, 5092)),
    "00754": CropInfo((1655, 400, 3005, 3780), (2025, 5070)),
    "00755": CropInfo((1671, 360, 3019, 3750), (2022, 5085)),
    "00756": CropInfo((2563, 350, 3928, 3815), (2048, 5198)),
    "00757": CropInfo((2586, 330, 3966, 3815), (2070, 5228)),
    "00758": CropInfo((1489, 390, 2988, 3810), (2248, 5130)),
    "00759": CropInfo((1482, 390, 2950, 3810), (2202, 5130)),
    "00760": CropInfo((1660, 400, 3145, 3815), (2228, 5122)),
    "00761": CropInfo((1504, 390, 3216, 3815), (2568, 5138)),
    "00762": CropInfo((1646, 380, 3094, 3810), (2172, 5145)),
    "00763": CropInfo((1610, 390, 3050, 3815), (2160, 5138)),
    "00764": CropInfo((1679, 350, 3079, 3815), (2100, 5198)),
    "00765": CropInfo((3018, 360, 4380, 3815), (2043, 5182)),
    "00766": CropInfo((1719, 330, 3039, 3815), (1980, 5228)),
    "00767": CropInfo((1703, 360, 3015, 3810), (1968, 5175)),
    "00768": CropInfo((1778, 390, 3100, 3785), (1983, 5092)),
}


def load_font(size: int) -> ImageFont.ImageFont:
    for name in ("arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            pass
    return ImageFont.load_default()


TITLE_FONT = load_font(34)
LABEL_FONT = load_font(24)
SMALL_FONT = load_font(18)


def raw_path(page: str) -> Path:
    return MEDIA_DIR / f"gbprs_norfolk_pd_86-41_{page}.jpg"


def enhanced_path(page: str) -> Path:
    return MEDIA_DIR / f"crop_{page}_enhanced.png"


def open_gray(path: Path) -> Image.Image:
    return Image.open(path).convert("L")


def contrast_sharp(im: Image.Image) -> Image.Image:
    out = ImageEnhance.Contrast(im.convert("L")).enhance(1.9)
    out = ImageEnhance.Sharpness(out).enhance(1.8)
    return out.filter(ImageFilter.UnsharpMask(radius=2, percent=170, threshold=3))


def clahe_blur(im: Image.Image) -> Image.Image:
    gray = im.convert("L")
    if cv2 is not None and np is not None:
        arr = np.array(gray)
        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
        out = clahe.apply(arr)
        out = cv2.GaussianBlur(out, (0, 0), sigmaX=0.6)
        return Image.fromarray(out)
    bg = gray.filter(ImageFilter.GaussianBlur(radius=16))
    flattened = Image.blend(gray, ImageOps.invert(bg), 0.30)
    return ImageOps.autocontrast(flattened, cutoff=1)


def adaptive_threshold(im: Image.Image) -> Image.Image:
    gray = im.convert("L")
    if cv2 is not None and np is not None:
        arr = np.array(gray)
        out = cv2.adaptiveThreshold(
            arr,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            41,
            12,
        )
        return Image.fromarray(out)
    auto = ImageOps.autocontrast(gray, cutoff=1)
    return auto.point(lambda p: 0 if p < 172 else 255, mode="1").convert("L")


def synthetic_existing_enhanced(raw_crop: Image.Image) -> Image.Image:
    out = ImageEnhance.Contrast(raw_crop.convert("L")).enhance(1.6)
    return ImageOps.autocontrast(out, cutoff=1)


def enhanced_equivalent(page: str, original_box: tuple[int, int, int, int]) -> Optional[Image.Image]:
    path = enhanced_path(page)
    info = CROP_INDEX.get(page)
    if not path.exists() or info is None:
        return None
    crop_left, crop_top, crop_right, crop_bottom = info.box
    sx = info.enhanced_size[0] / (crop_right - crop_left)
    sy = info.enhanced_size[1] / (crop_bottom - crop_top)
    left, top, right, bottom = original_box
    eq = (
        round((left - crop_left) * sx),
        round((top - crop_top) * sy),
        round((right - crop_left) * sx),
        round((bottom - crop_top) * sy),
    )
    enhanced = open_gray(path)
    eq = clamp_box(eq, enhanced.size)
    return enhanced.crop(eq)


def clamp_box(box: tuple[int, int, int, int], size: tuple[int, int]) -> tuple[int, int, int, int]:
    width, height = size
    left, top, right, bottom = box
    left = max(0, min(width - 1, left))
    top = max(0, min(height - 1, top))
    right = max(left + 1, min(width, right))
    bottom = max(top + 1, min(height, bottom))
    return left, top, right, bottom


def auto_parchment_box(page: str) -> tuple[int, int, int, int]:
    """Find the main register strip for raw-only pages.

    The East Dereham frames include a gray board and handling markers. This
    finder deliberately favors the tall, bright parchment component and rejects
    small bright cards. It is a navigation aid, not a paleographic classifier.
    """
    im = open_gray(raw_path(page))
    small = im.resize((im.width // 8, im.height // 8), Image.Resampling.BILINEAR)
    if np is None:
        mask = small.point(lambda px: 255 if px > 165 else 0, mode="1")
        box = mask.getbbox()
        if box is None:
            return (0, 0, im.width, im.height)
        left, top, right, bottom = box
        return clamp_box((left * 8, top * 8, right * 8, bottom * 8), im.size)

    arr = np.array(small)
    mask = arr > 165
    height, width = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    best: Optional[tuple[int, int, int, int, int]] = None
    for y in range(height):
        for x in range(width):
            if not mask[y, x] or seen[y, x]:
                continue
            stack = [(x, y)]
            seen[y, x] = True
            xs: list[int] = []
            ys: list[int] = []
            while stack:
                cx, cy = stack.pop()
                xs.append(cx)
                ys.append(cy)
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < width and 0 <= ny < height and mask[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        stack.append((nx, ny))
            left, top, right, bottom = min(xs), min(ys), max(xs) + 1, max(ys) + 1
            component_w = right - left
            component_h = bottom - top
            area = len(xs)
            if component_h < 150 or component_w < 60 or area < 3000:
                continue
            if best is None or area > best[0]:
                best = (area, left, top, right, bottom)
    if best is None:
        return (0, 0, im.width, im.height)
    _, left, top, right, bottom = best
    pad = 18
    return clamp_box(((left * 8) - pad, (top * 8) - pad, (right * 8) + pad, (bottom * 8) + pad), im.size)


def review_box(page: str) -> tuple[int, int, int, int]:
    info = CROP_INDEX.get(page)
    if info is not None:
        return info.box
    return auto_parchment_box(page)


def crop_raw(page: str, box: tuple[int, int, int, int]) -> Image.Image:
    raw = open_gray(raw_path(page))
    return raw.crop(clamp_box(box, raw.size))


def save_enhanced_crop(page: str, box: tuple[int, int, int, int], out_path: Path) -> None:
    crop = crop_raw(page, box)
    out = synthetic_existing_enhanced(crop).resize(
        (round(crop.width * 1.5), round(crop.height * 1.5)),
        Image.Resampling.LANCZOS,
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path)


def states_for(page: str, box: tuple[int, int, int, int]) -> list[tuple[str, Image.Image]]:
    raw = crop_raw(page, box)
    existing = enhanced_equivalent(page, box) or synthetic_existing_enhanced(raw)
    return [
        ("raw-resized", raw),
        ("existing-enhanced", existing),
        ("autocontrast", ImageOps.autocontrast(raw, cutoff=1)),
        ("contrast+sharp", contrast_sharp(raw)),
        ("background flatten", clahe_blur(raw)),
        ("support threshold", adaptive_threshold(raw)),
    ]


def fit_panel(im: Image.Image, width: int, height: int) -> Image.Image:
    rgb = im.convert("RGB")
    ratio = min(width / rgb.width, height / rgb.height)
    new_size = (max(1, round(rgb.width * ratio)), max(1, round(rgb.height * ratio)))
    resized = rgb.resize(new_size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (width, height), (250, 250, 248))
    canvas.paste(resized, ((width - resized.width) // 2, (height - resized.height) // 2))
    return canvas


def draw_labelled_panel(
    im: Image.Image,
    label: str,
    panel_size: tuple[int, int],
) -> Image.Image:
    width, height = panel_size
    label_h = 34
    canvas = Image.new("RGB", (width, height + label_h), (242, 242, 240))
    d = ImageDraw.Draw(canvas)
    d.text((8, 4), label, fill=(0, 0, 0), font=LABEL_FONT)
    canvas.paste(fit_panel(im, width, height), (0, label_h))
    return canvas


def six_state_sheet(
    specs: Iterable[tuple[str, str, tuple[int, int, int, int]]],
    out_path: Path,
    title: str,
    panel_size: tuple[int, int] = (1250, 520),
) -> None:
    rows: list[Image.Image] = []
    gap = 18
    margin = 26
    header_h = 80
    sheet_width = panel_size[0] * 3 + gap * 2 + margin * 2
    for page, description, box in specs:
        state_panels = [
            draw_labelled_panel(im, label, panel_size)
            for label, im in states_for(page, box)
        ]
        row_header_h = 42
        row_h = row_header_h + state_panels[0].height * 2 + gap
        row = Image.new("RGB", (sheet_width, row_h), (242, 242, 240))
        d = ImageDraw.Draw(row)
        d.text(
            (margin, 4),
            f"page {page} - {description} - crop box {box}",
            fill=(0, 0, 0),
            font=SMALL_FONT,
        )
        y0 = row_header_h
        for idx, panel in enumerate(state_panels):
            col = idx % 3
            rr = idx // 3
            x = margin + col * (panel_size[0] + gap)
            y = y0 + rr * (panel.height + gap)
            row.paste(panel, (x, y))
        rows.append(row)
    sheet_height = header_h + sum(row.height for row in rows) + gap * (len(rows) - 1) + margin
    sheet = Image.new("RGB", (sheet_width, sheet_height), (242, 242, 240))
    d = ImageDraw.Draw(sheet)
    d.text((margin, 18), title, fill=(0, 0, 0), font=TITLE_FONT)
    y = header_h
    for row in rows:
        sheet.paste(row, (0, y))
        y += row.height + gap
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path)


def crop_from_enhanced_coords(page: str, box: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    info = CROP_INDEX[page]
    crop_left, crop_top, crop_right, crop_bottom = info.box
    sx = (crop_right - crop_left) / info.enhanced_size[0]
    sy = (crop_bottom - crop_top) / info.enhanced_size[1]
    left, top, right, bottom = box
    return (
        round(crop_left + left * sx),
        round(crop_top + top * sy),
        round(crop_left + right * sx),
        round(crop_top + bottom * sy),
    )


def contrast_scan_row(page: str, box: tuple[int, int, int, int], label: str) -> Image.Image:
    raw = crop_raw(page, box)
    sharp = contrast_sharp(raw)
    panel_h = 1120
    panel_w = 1750
    label_h = 38
    gap = 20
    row = Image.new("RGB", (panel_w * 2 + gap + 52, panel_h + label_h + 26), (242, 242, 240))
    d = ImageDraw.Draw(row)
    d.text((26, 6), f"{label} - page {page} - crop box {box}", fill=(0, 0, 0), font=SMALL_FONT)
    left = draw_labelled_panel(raw, "raw-resized", (panel_w, panel_h))
    right = draw_labelled_panel(sharp, "contrast+sharp", (panel_w, panel_h))
    row.paste(left, (26, label_h))
    row.paste(right, (26 + panel_w + gap, label_h))
    return row


def marriages_scan_sheet(out_path: Path) -> None:
    boxes = {
        "00728": CROP_INDEX["00728"].box,
        "00729": crop_from_enhanced_coords("00729", (0, 1400, CROP_INDEX["00729"].enhanced_size[0], 3250)),
        "00730": CROP_INDEX["00730"].box,
    }
    rows = [
        contrast_scan_row("00728", boxes["00728"], "full enhanced-crop equivalent scan"),
        contrast_scan_row("00729", boxes["00729"], "Mariages-section band scan"),
        contrast_scan_row("00730", boxes["00730"], "full enhanced-crop equivalent scan"),
    ]
    margin = 26
    gap = 18
    header_h = 74
    width = max(row.width for row in rows)
    height = header_h + sum(row.height for row in rows) + gap * (len(rows) - 1) + margin
    sheet = Image.new("RGB", (width, height), (242, 242, 240))
    d = ImageDraw.Draw(sheet)
    d.text((margin, 16), "Pages 00728-00730 marriages-section scan sheet", fill=(0, 0, 0), font=TITLE_FONT)
    y = header_h
    for row in rows:
        sheet.paste(row, (0, y))
        y += row.height + gap
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path)


def page_review_panel(page: str, box: tuple[int, int, int, int]) -> Image.Image:
    raw = crop_raw(page, box)
    enhanced = synthetic_existing_enhanced(raw)
    if enhanced_path(page).exists():
        enhanced = open_gray(enhanced_path(page))
    sharp = contrast_sharp(raw)
    panel_w = 820
    panel_h = 1850
    gap = 16
    label_h = 40
    row = Image.new("RGB", (panel_w * 2 + gap + 52, panel_h + label_h + 32), (242, 242, 240))
    d = ImageDraw.Draw(row)
    d.text((26, 8), f"page {page} - review box {box}", fill=(0, 0, 0), font=SMALL_FONT)
    row.paste(draw_labelled_panel(enhanced, "enhanced crop", (panel_w, panel_h)), (26, label_h))
    row.paste(draw_labelled_panel(sharp, "contrast+sharp raw", (panel_w, panel_h)), (26 + panel_w + gap, label_h))
    return row


def review_scan_sheet(pages: list[str], out_path: Path, title: str) -> None:
    rows = [page_review_panel(page, review_box(page)) for page in pages]
    margin = 26
    gap = 18
    header_h = 74
    width = max(row.width for row in rows)
    height = header_h + sum(row.height for row in rows) + gap * (len(rows) - 1) + margin
    sheet = Image.new("RGB", (width, height), (242, 242, 240))
    d = ImageDraw.Draw(sheet)
    d.text((margin, 16), title, fill=(0, 0, 0), font=TITLE_FONT)
    y = header_h
    for row in rows:
        sheet.paste(row, (0, y))
        y += row.height + gap
    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path)


def generate_737_plus_review() -> None:
    for page_number in range(737, 750):
        page = f"{page_number:05d}"
        save_enhanced_crop(page, review_box(page), enhanced_path(page))
    batches = [
        (range(737, 741), "pages_00737_00740_gurney_review_sheet.png"),
        (range(741, 745), "pages_00741_00744_gurney_review_sheet.png"),
        (range(745, 749), "pages_00745_00748_gurney_review_sheet.png"),
        (range(749, 753), "pages_00749_00752_gurney_review_sheet.png"),
        (range(753, 757), "pages_00753_00756_gurney_review_sheet.png"),
        (range(757, 761), "pages_00757_00760_gurney_review_sheet.png"),
        (range(761, 765), "pages_00761_00764_gurney_review_sheet.png"),
        (range(765, 769), "pages_00765_00768_gurney_review_sheet.png"),
    ]
    for page_range, filename in batches:
        pages = [f"{page_number:05d}" for page_number in page_range]
        review_scan_sheet(
            pages,
            MEDIA_DIR / filename,
            f"Pages {pages[0]}-{pages[-1]} Gurney and Francis review sheet",
        )


def generate_next_pulls() -> None:
    six_state_sheet(
        [
            ("00726", "heading/year block", (1500, 250, 3050, 1450)),
            ("00727", "heading/year block", (1500, 250, 3050, 1450)),
        ],
        MEDIA_DIR / "page_00726_00727_heading_year_sweep.png",
        "Pages 00726 and 00727 heading/year sweep",
        panel_size=(1200, 620),
    )
    marriages_scan_sheet(MEDIA_DIR / "pages_00728_00729_00730_marriages_section_sweep.png")
    six_state_sheet(
        [("00735", "heading/year block", (1500, 350, 3050, 1500))],
        MEDIA_DIR / "page_00735_heading_year_sweep.png",
        "Page 00735 heading/year sweep",
        panel_size=(1300, 760),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("next-pulls", help="generate the pending next-pull artifacts")
    sub.add_parser("scan-737-plus", help="generate review sheets for pages 00737-00768")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command in (None, "next-pulls"):
        generate_next_pulls()
    elif args.command == "scan-737-plus":
        generate_737_plus_review()


if __name__ == "__main__":
    main()
