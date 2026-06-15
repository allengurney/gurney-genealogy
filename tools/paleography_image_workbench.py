r"""Paleography image preparation utilities.

Run from the repository root with the repo-local interpreter:

    .\.venv\Scripts\python.exe tools\paleography_image_workbench.py info path\image.jpg
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

try:
    import cv2  # type: ignore
except Exception:  # pragma: no cover - optional enhancement path
    cv2 = None

try:
    import fitz  # type: ignore
except Exception:  # pragma: no cover - optional PDF path
    fitz = None

try:
    import numpy as np  # type: ignore
except Exception:  # pragma: no cover - optional segmentation path
    np = None


Box = tuple[int, int, int, int]


@dataclass(frozen=True)
class OutputItem:
    label: str
    path: Path
    box_xywh: tuple[int, int, int, int] | None = None


def load_font(size: int) -> ImageFont.ImageFont:
    for name in ("arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            pass
    return ImageFont.load_default()


LABEL_FONT = load_font(24)
SMALL_FONT = load_font(18)


def parse_box(value: str) -> Box:
    parts = [int(p.strip()) for p in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be x,y,width,height")
    x, y, width, height = parts
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("box width and height must be positive")
    return (x, y, x + width, y + height)


def parse_named_box(value: str) -> tuple[str, Box]:
    if ":" in value:
        label, box_value = value.split(":", 1)
    else:
        label, box_value = "band", value
    label = label.strip() or "band"
    safe_label = "".join(ch if ch.isalnum() or ch in "-_" else "-" for ch in label)
    return safe_label, parse_box(box_value)


def box_to_xywh(box: Box) -> tuple[int, int, int, int]:
    left, top, right, bottom = box
    return (left, top, right - left, bottom - top)


def clamp_box(box: Box, size: tuple[int, int]) -> Box:
    width, height = size
    left, top, right, bottom = box
    left = max(0, min(width - 1, left))
    top = max(0, min(height - 1, top))
    right = max(left + 1, min(width, right))
    bottom = max(top + 1, min(height, bottom))
    return (left, top, right, bottom)


def expand_box(box: Box, size: tuple[int, int], x_pad: int, y_pad: int) -> Box:
    left, top, right, bottom = box
    return clamp_box((left - x_pad, top - y_pad, right + x_pad, bottom + y_pad), size)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def open_image(path: Path) -> Image.Image:
    Image.MAX_IMAGE_PIXELS = None
    return Image.open(path)


def save_image(im: Image.Image, path: Path) -> None:
    ensure_parent(path)
    im.save(path)


def scaled(im: Image.Image, scale: float) -> Image.Image:
    if scale == 1:
        return im.copy()
    width = max(1, round(im.width * scale))
    height = max(1, round(im.height * scale))
    return im.resize((width, height), Image.Resampling.LANCZOS)


def grayscale(im: Image.Image) -> Image.Image:
    return im.convert("L")


def autocontrast(im: Image.Image) -> Image.Image:
    return ImageOps.autocontrast(grayscale(im), cutoff=1)


def sharpen(im: Image.Image) -> Image.Image:
    out = ImageEnhance.Contrast(grayscale(im)).enhance(1.7)
    out = ImageEnhance.Sharpness(out).enhance(1.8)
    return out.filter(ImageFilter.UnsharpMask(radius=2, percent=160, threshold=3))


def clahe(im: Image.Image) -> Image.Image:
    gray = grayscale(im)
    if cv2 is not None and np is not None:
        arr = np.array(gray)
        engine = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
        return Image.fromarray(engine.apply(arr))
    blurred = gray.filter(ImageFilter.GaussianBlur(radius=18))
    flattened = Image.blend(gray, ImageOps.invert(blurred), 0.28)
    return ImageOps.autocontrast(flattened, cutoff=1)


def threshold(im: Image.Image) -> Image.Image:
    gray = grayscale(im)
    if cv2 is not None and np is not None:
        arr = np.array(gray)
        block = max(31, (min(gray.size) // 24) | 1)
        out = cv2.adaptiveThreshold(
            arr,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            block,
            11,
        )
        return Image.fromarray(out)
    auto = autocontrast(gray)
    return auto.point(lambda p: 0 if p < 170 else 255, mode="1").convert("L")


def enhancement_variants(im: Image.Image) -> list[tuple[str, Image.Image]]:
    gray = grayscale(im)
    return [
        ("raw", im.convert("RGB")),
        ("gray", gray),
        ("autocontrast", autocontrast(gray)),
        ("sharpen", sharpen(gray)),
        ("unsharp", gray.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=3))),
        ("clahe", clahe(gray)),
        ("threshold", threshold(gray)),
        ("invert-auto", ImageOps.invert(autocontrast(gray))),
    ]


def labelled_tile(label: str, im: Image.Image, max_width: int = 1100) -> Image.Image:
    tile = im.convert("RGB")
    if max_width > 0 and tile.width > max_width:
        ratio = max_width / tile.width
        tile = tile.resize((max_width, max(1, round(tile.height * ratio))), Image.Resampling.LANCZOS)
    label_height = 42
    out = Image.new("RGB", (tile.width, tile.height + label_height), "white")
    out.paste(tile, (0, label_height))
    draw = ImageDraw.Draw(out)
    draw.text((10, 8), label, fill="black", font=SMALL_FONT)
    return out


def contact_sheet(
    items: list[tuple[str, Image.Image]],
    out_path: Path,
    columns: int = 2,
    tile_max_width: int = 1100,
) -> None:
    tiles = [labelled_tile(label, im, tile_max_width) for label, im in items]
    if not tiles:
        raise ValueError("no images for contact sheet")
    columns = max(1, columns)
    rows = math.ceil(len(tiles) / columns)
    col_widths = [0] * columns
    row_heights = [0] * rows
    for idx, tile in enumerate(tiles):
        col = idx % columns
        row = idx // columns
        col_widths[col] = max(col_widths[col], tile.width)
        row_heights[row] = max(row_heights[row], tile.height)
    gutter = 24
    width = sum(col_widths) + gutter * (columns + 1)
    height = sum(row_heights) + gutter * (rows + 1)
    sheet = Image.new("RGB", (width, height), "white")
    y = gutter
    for row in range(rows):
        x = gutter
        for col in range(columns):
            idx = row * columns + col
            if idx < len(tiles):
                sheet.paste(tiles[idx], (x, y))
            x += col_widths[col] + gutter
        y += row_heights[row] + gutter
    save_image(sheet, out_path)


def draw_grid(im: Image.Image, step: int, label_step: int) -> Image.Image:
    out = im.convert("RGB")
    draw = ImageDraw.Draw(out)
    step = max(25, step)
    label_step = max(step, label_step)
    for x in range(0, out.width, step):
        color = (255, 0, 0) if x % label_step == 0 else (255, 180, 180)
        draw.line((x, 0, x, out.height), fill=color, width=2 if x % label_step == 0 else 1)
        if x % label_step == 0:
            draw.text((x + 4, 4), str(x), fill=(255, 0, 0), font=SMALL_FONT)
    for y in range(0, out.height, step):
        color = (0, 90, 255) if y % label_step == 0 else (170, 205, 255)
        draw.line((0, y, out.width, y), fill=color, width=2 if y % label_step == 0 else 1)
        if y % label_step == 0:
            draw.text((4, y + 4), str(y), fill=(0, 90, 255), font=SMALL_FONT)
    return out


def dark_mask(gray: Image.Image):
    if np is None:
        return None
    arr = np.array(ImageOps.autocontrast(gray.convert("L"), cutoff=1))
    cutoff = min(205, max(60, float(np.percentile(arr, 38))))
    mask = arr < cutoff
    if cv2 is not None:
        kernel = np.ones((2, 2), np.uint8)
        mask = cv2.morphologyEx(mask.astype("uint8"), cv2.MORPH_OPEN, kernel).astype(bool)
    return mask


def ink_expand_box(im: Image.Image, box: Box, search_pad: int, final_pad: int) -> Box:
    search = expand_box(box, im.size, search_pad, search_pad)
    crop = im.crop(search).convert("L")
    mask = dark_mask(crop)
    if mask is None or not mask.any():
        return expand_box(box, im.size, final_pad, final_pad)
    ys, xs = np.where(mask)
    left = search[0] + int(xs.min())
    right = search[0] + int(xs.max()) + 1
    top = search[1] + int(ys.min())
    bottom = search[1] + int(ys.max()) + 1
    expanded = expand_box((left, top, right, bottom), im.size, final_pad, final_pad)
    requested = expand_box(box, im.size, final_pad, final_pad)
    return (
        min(expanded[0], requested[0]),
        min(expanded[1], requested[1]),
        max(expanded[2], requested[2]),
        max(expanded[3], requested[3]),
    )


def smooth(values, window: int):
    if np is None:
        return values
    window = max(3, window | 1)
    kernel = np.ones(window) / window
    return np.convolve(values, kernel, mode="same")


def line_bands(im: Image.Image, min_height: int = 18) -> list[tuple[int, int]]:
    if np is None:
        h = im.height
        return [(0, h)]
    mask = dark_mask(im.convert("L"))
    if mask is None or not mask.any():
        return [(0, im.height)]
    projection = mask.sum(axis=1)
    smoothed = smooth(projection, max(5, im.height // 90))
    threshold_value = max(3, float(np.percentile(smoothed, 70)) * 0.45)
    active = smoothed > threshold_value
    bands: list[tuple[int, int]] = []
    start = None
    for idx, is_active in enumerate(active):
        if is_active and start is None:
            start = idx
        elif not is_active and start is not None:
            if idx - start >= min_height:
                bands.append((start, idx))
            start = None
    if start is not None and len(active) - start >= min_height:
        bands.append((start, len(active)))
    if not bands:
        return [(0, im.height)]
    merged: list[tuple[int, int]] = []
    gap_limit = max(8, im.height // 80)
    for top, bottom in bands:
        if merged and top - merged[-1][1] <= gap_limit:
            merged[-1] = (merged[-1][0], bottom)
        else:
            merged.append((top, bottom))
    return merged


def line_strip_boxes(im: Image.Image, box: Box, y_pad: int, x_pad: int) -> list[Box]:
    box = clamp_box(box, im.size)
    crop = im.crop(box)
    bands = line_bands(crop)
    out: list[Box] = []
    for top, bottom in bands:
        line_box = (
            box[0] - x_pad,
            box[1] + top - y_pad,
            box[2] + x_pad,
            box[1] + bottom + y_pad,
        )
        out.append(clamp_box(line_box, im.size))
    return out


def write_manifest(path: Path, source: Path, command: str, items: Iterable[OutputItem], metadata: dict[str, str]) -> None:
    ensure_parent(path)
    rows = [
        "# Paleography image workbench manifest",
        "",
        f"- Source image: `{source}`",
        f"- Command: `{command}`",
    ]
    for key, value in metadata.items():
        if value:
            rows.append(f"- {key}: {value}")
    rows.extend(["", "## Outputs", ""])
    for item in items:
        suffix = ""
        if item.box_xywh is not None:
            suffix = f" - box `{','.join(str(v) for v in item.box_xywh)}`"
        rows.append(f"- `{item.path}` - {item.label}{suffix}")
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def read_manifest_items(path: Path) -> list[OutputItem]:
    items: list[OutputItem] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line.startswith("- `") or "` - " not in line:
            continue
        path_text = line.split("`", 2)[1]
        rest = line.split("` - ", 1)[1]
        label = rest
        box = None
        if " - box `" in rest:
            label, box_text = rest.split(" - box `", 1)
            values = [int(part) for part in box_text.rstrip("`").split(",")]
            if len(values) == 4:
                box = tuple(values)  # type: ignore[assignment]
        items.append(OutputItem(label, Path(path_text), box))
    return items


def manifest_summary(manifest_paths: list[Path], selected_only: bool) -> str:
    rows = ["| Manifest | Label | Box | Output |", "|---|---|---|---|"]
    for manifest in manifest_paths:
        for item in read_manifest_items(manifest):
            if selected_only and item.box_xywh is None:
                continue
            box = ""
            if item.box_xywh is not None:
                box = ",".join(str(value) for value in item.box_xywh)
            rows.append(f"| `{manifest}` | {item.label} | `{box}` | `{item.path}` |")
    return "\n".join(rows) + "\n"


def command_info(args: argparse.Namespace) -> None:
    path = Path(args.image)
    im = open_image(path)
    print(f"path: {path}")
    print(f"format: {im.format}")
    print(f"mode: {im.mode}")
    print(f"width: {im.width}")
    print(f"height: {im.height}")
    print(f"file_size: {path.stat().st_size}")


def command_render_pdf(args: argparse.Namespace) -> None:
    if fitz is None:
        raise SystemExit("PyMuPDF is not installed; run tools\\bootstrap_python_toolchain.ps1")
    src = Path(args.pdf)
    out = Path(args.out)
    doc = fitz.open(src)
    page_index = args.page - 1
    if page_index < 0 or page_index >= len(doc):
        raise SystemExit(f"page out of range: {args.page}")
    page = doc[page_index]
    pix = page.get_pixmap(dpi=args.dpi, alpha=False)
    ensure_parent(out)
    pix.save(out)
    print(out)


def command_grid(args: argparse.Namespace) -> None:
    im = open_image(Path(args.image))
    out = draw_grid(im, args.step, args.label_step)
    save_image(out, Path(args.out))
    print(args.out)


def command_split_spread(args: argparse.Namespace) -> None:
    src = Path(args.image)
    im = open_image(src)
    split_x = args.x if args.x is not None else im.width // 2
    split_x = max(1, min(im.width - 1, split_x))
    overlap = max(0, args.overlap)
    left_box = clamp_box((0, 0, split_x + overlap, im.height), im.size)
    right_box = clamp_box((split_x - overlap, 0, im.width, im.height), im.size)
    out_dir = Path(args.out_dir)
    prefix = args.prefix
    items = []
    for label, box in (("left", left_box), ("right", right_box)):
        out = out_dir / f"{prefix}-{label}.png"
        save_image(im.crop(box), out)
        items.append(OutputItem(label, out, box_to_xywh(box)))
    manifest = out_dir / f"{prefix}-split-manifest.md"
    write_manifest(
        manifest,
        src,
        "split-spread",
        items,
        {"split_x": str(split_x), "overlap": str(overlap)},
    )
    print(manifest)


def command_crop(args: argparse.Namespace) -> None:
    src = Path(args.image)
    im = open_image(src)
    box = clamp_box(args.box, im.size)
    if args.ink_expand:
        box = ink_expand_box(im, box, args.search_pad, args.pad)
    crop = im.crop(box)
    out = Path(args.out)
    save_image(scaled(crop, args.scale), out)
    items = [OutputItem("crop", out, box_to_xywh(box))]
    if args.manifest:
        write_manifest(Path(args.manifest), src, "crop", items, vars(args))
    print(out)


def command_sheet(args: argparse.Namespace) -> None:
    im = open_image(Path(args.image))
    box = clamp_box(args.box, im.size) if args.box else (0, 0, im.width, im.height)
    crop = im.crop(box)
    variants = [(label, scaled(img, args.scale)) for label, img in enhancement_variants(crop)]
    contact_sheet(variants, Path(args.out), columns=args.columns, tile_max_width=args.tile_max_width)
    print(args.out)


def save_candidate_set(
    source: Path,
    im: Image.Image,
    boxes: list[tuple[str, Box]],
    out_dir: Path,
    prefix: str,
    scale: float,
    sheet_columns: int = 1,
    tile_max_width: int = 1100,
) -> list[OutputItem]:
    out_dir.mkdir(parents=True, exist_ok=True)
    items: list[OutputItem] = []
    sheet_items: list[tuple[str, Image.Image]] = []
    for label, box in boxes:
        crop = im.crop(box)
        out = out_dir / f"{prefix}-{label}.png"
        save_image(scaled(crop, scale), out)
        items.append(OutputItem(label, out, box_to_xywh(box)))
        sheet_items.append((f"{label} {box_to_xywh(box)}", scaled(crop, scale)))
    sheet_path = out_dir / f"{prefix}-contact-sheet.png"
    contact_sheet(sheet_items, sheet_path, columns=sheet_columns, tile_max_width=tile_max_width)
    items.append(OutputItem("contact-sheet", sheet_path, None))
    manifest_path = out_dir / f"{prefix}-manifest.md"
    write_manifest(manifest_path, source, "candidate-set", items, {})
    items.append(OutputItem("manifest", manifest_path, None))
    return items


def command_crop_ladder(args: argparse.Namespace) -> None:
    src = Path(args.image)
    im = open_image(src)
    base = clamp_box(args.box, im.size)
    x_pad = args.x_pad
    y_pad = args.y_pad
    wide = expand_box(base, im.size, x_pad * 2, y_pad * 2)
    ink = ink_expand_box(im, base, args.search_pad, args.pad)
    shifts = [
        ("base", base),
        ("wide", wide),
        ("ink-expanded", ink),
        ("higher", expand_box((base[0], base[1] - y_pad, base[2], base[3] - y_pad), im.size, x_pad, y_pad)),
        ("lower", expand_box((base[0], base[1] + y_pad, base[2], base[3] + y_pad), im.size, x_pad, y_pad)),
        ("left", expand_box((base[0] - x_pad, base[1], base[2] - x_pad, base[3]), im.size, x_pad, y_pad)),
        ("right", expand_box((base[0] + x_pad, base[1], base[2] + x_pad, base[3]), im.size, x_pad, y_pad)),
    ]
    if args.line_strips:
        for idx, line_box in enumerate(line_strip_boxes(im, wide, args.line_y_pad, args.line_x_pad), start=1):
            shifts.append((f"line-{idx:02d}", line_box))
    items = save_candidate_set(
        src,
        im,
        shifts,
        Path(args.out_dir),
        args.prefix,
        args.scale,
        args.sheet_columns,
        args.tile_max_width,
    )
    print(items[-1].path)


def command_line_strips(args: argparse.Namespace) -> None:
    src = Path(args.image)
    im = open_image(src)
    base = clamp_box(args.box, im.size)
    if args.line_height:
        bands = manual_line_bands(base, args.line_height, args.line_overlap)
        boxes = [(f"line-{idx:02d}", expand_box(box, im.size, args.x_pad, args.y_pad)) for idx, box in enumerate(bands, start=1)]
    elif args.line_count:
        bands = evenly_split_box(base, args.line_count, args.line_overlap)
        boxes = [(f"line-{idx:02d}", expand_box(box, im.size, args.x_pad, args.y_pad)) for idx, box in enumerate(bands, start=1)]
    else:
        boxes = [(f"line-{idx:02d}", box) for idx, box in enumerate(line_strip_boxes(im, base, args.y_pad, args.x_pad), start=1)]
    save_candidate_set(
        src,
        im,
        boxes,
        Path(args.out_dir),
        args.prefix,
        args.scale,
        args.sheet_columns,
        args.tile_max_width,
    )
    print(Path(args.out_dir) / f"{args.prefix}-contact-sheet.png")


def evenly_split_box(box: Box, count: int, overlap: int) -> list[Box]:
    left, top, right, bottom = box
    count = max(1, count)
    height = max(1, bottom - top)
    band_height = max(1, math.ceil(height / count))
    bands: list[Box] = []
    for idx in range(count):
        band_top = top + idx * band_height
        band_bottom = min(bottom, band_top + band_height)
        if band_top >= bottom:
            break
        bands.append((left, max(top, band_top - overlap), right, min(bottom, band_bottom + overlap)))
    return bands


def manual_line_bands(box: Box, line_height: int, overlap: int) -> list[Box]:
    left, top, right, bottom = box
    line_height = max(1, line_height)
    bands: list[Box] = []
    y = top
    while y < bottom:
        band_bottom = min(bottom, y + line_height)
        bands.append((left, max(top, y - overlap), right, min(bottom, band_bottom + overlap)))
        y += line_height
    return bands


def command_band_ladder(args: argparse.Namespace) -> None:
    src = Path(args.image)
    im = open_image(src)
    boxes = [(label, clamp_box(box, im.size)) for label, box in args.band]
    items = save_candidate_set(
        src,
        im,
        boxes,
        Path(args.out_dir),
        args.prefix,
        args.scale,
        args.sheet_columns,
        args.tile_max_width,
    )
    print(items[-1].path)


def command_manifest_summary(args: argparse.Namespace) -> None:
    text = manifest_summary([Path(path) for path in args.manifest], args.selected_only)
    if args.out:
        out = Path(args.out)
        ensure_parent(out)
        out.write_text(text, encoding="utf-8")
        print(out)
    else:
        print(text, end="")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prepare paleography crops, line strips, and enhancement sheets.")
    sub = parser.add_subparsers(dest="command", required=True)

    info = sub.add_parser("info")
    info.add_argument("image")
    info.set_defaults(func=command_info)

    render = sub.add_parser("render-pdf")
    render.add_argument("pdf")
    render.add_argument("--page", type=int, default=1)
    render.add_argument("--dpi", type=int, default=250)
    render.add_argument("--out", required=True)
    render.set_defaults(func=command_render_pdf)

    grid = sub.add_parser("grid")
    grid.add_argument("image")
    grid.add_argument("--out", required=True)
    grid.add_argument("--step", type=int, default=250)
    grid.add_argument("--label-step", type=int, default=500)
    grid.set_defaults(func=command_grid)

    split = sub.add_parser("split-spread")
    split.add_argument("image")
    split.add_argument("--out-dir", required=True)
    split.add_argument("--prefix", default="spread")
    split.add_argument("--x", type=int, help="vertical split coordinate; defaults to midpoint")
    split.add_argument("--overlap", type=int, default=80)
    split.set_defaults(func=command_split_spread)

    crop = sub.add_parser("crop")
    crop.add_argument("image")
    crop.add_argument("--box", type=parse_box, required=True, help="x,y,width,height")
    crop.add_argument("--out", required=True)
    crop.add_argument("--scale", type=float, default=1.0)
    crop.add_argument("--ink-expand", action="store_true")
    crop.add_argument("--search-pad", type=int, default=180)
    crop.add_argument("--pad", type=int, default=40)
    crop.add_argument("--manifest")
    crop.set_defaults(func=command_crop)

    sheet = sub.add_parser("sheet")
    sheet.add_argument("image")
    sheet.add_argument("--box", type=parse_box, help="x,y,width,height")
    sheet.add_argument("--out", required=True)
    sheet.add_argument("--scale", type=float, default=1.0)
    sheet.add_argument("--columns", type=int, default=2)
    sheet.add_argument("--tile-max-width", type=int, default=1100, help="maximum displayed tile width in the contact sheet; 0 keeps full width")
    sheet.set_defaults(func=command_sheet)

    ladder = sub.add_parser("crop-ladder")
    ladder.add_argument("image")
    ladder.add_argument("--box", type=parse_box, required=True, help="x,y,width,height")
    ladder.add_argument("--out-dir", required=True)
    ladder.add_argument("--prefix", default="crop")
    ladder.add_argument("--scale", type=float, default=1.0)
    ladder.add_argument("--x-pad", type=int, default=120)
    ladder.add_argument("--y-pad", type=int, default=90)
    ladder.add_argument("--search-pad", type=int, default=220)
    ladder.add_argument("--pad", type=int, default=50)
    ladder.add_argument("--line-strips", action="store_true")
    ladder.add_argument("--line-x-pad", type=int, default=80)
    ladder.add_argument("--line-y-pad", type=int, default=35)
    ladder.add_argument("--sheet-columns", type=int, default=1)
    ladder.add_argument("--tile-max-width", type=int, default=1100, help="maximum displayed tile width in the contact sheet; 0 keeps full width")
    ladder.set_defaults(func=command_crop_ladder)

    lines = sub.add_parser("line-strips")
    lines.add_argument("image")
    lines.add_argument("--box", type=parse_box, required=True, help="x,y,width,height")
    lines.add_argument("--out-dir", required=True)
    lines.add_argument("--prefix", default="line")
    lines.add_argument("--scale", type=float, default=1.0)
    lines.add_argument("--x-pad", type=int, default=80)
    lines.add_argument("--y-pad", type=int, default=35)
    lines.add_argument("--line-count", type=int, help="split the box into this many evenly spaced manual strips")
    lines.add_argument("--line-height", type=int, help="split the box into fixed-height manual strips")
    lines.add_argument("--line-overlap", type=int, default=25, help="vertical overlap for manual strips")
    lines.add_argument("--sheet-columns", type=int, default=1)
    lines.add_argument("--tile-max-width", type=int, default=1100, help="maximum displayed tile width in the contact sheet; 0 keeps full width")
    lines.set_defaults(func=command_line_strips)

    band = sub.add_parser("band-ladder")
    band.add_argument("image")
    band.add_argument("--band", action="append", type=parse_named_box, required=True, help="named full-image box as label:x,y,width,height; repeat for multiple bands")
    band.add_argument("--out-dir", required=True)
    band.add_argument("--prefix", default="band")
    band.add_argument("--scale", type=float, default=1.0)
    band.add_argument("--sheet-columns", type=int, default=1)
    band.add_argument("--tile-max-width", type=int, default=1100, help="maximum displayed tile width in the contact sheet; 0 keeps full width")
    band.set_defaults(func=command_band_ladder)

    summary = sub.add_parser("manifest-summary")
    summary.add_argument("manifest", nargs="+")
    summary.add_argument("--selected-only", action="store_true", help="omit contact-sheet and manifest rows without boxes")
    summary.add_argument("--out")
    summary.set_defaults(func=command_manifest_summary)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
