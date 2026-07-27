"""Stack the top band of each register page into one labelled sheet.

Orientation aid for the July 2026 re-review: finds which pages carry an
in-parchment annual-return heading. Not a substitute for the workbench --
adjudicate from workbench crops of the master, not from this sheet.

Usage:
    .venv/Scripts/python.exe heading_montage.py <first> <last> <out.png>
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

SRC = Path(__file__).resolve().parent.parent / "original-content" / "Parish_Register"
BAND = (1500, 400, 3400, 1150)  # x0, y0, x1, y1 in master coords
TILE_W = 1100
LABEL_H = 34


def main() -> int:
    first, last, out = int(sys.argv[1]), int(sys.argv[2]), Path(sys.argv[3])
    tiles = []
    for n in range(first, last + 1):
        path = SRC / f"gbprs_norfolk_pd_86-41_{n:05d}.jpg"
        if not path.exists():
            continue
        with Image.open(path) as im:
            box = (BAND[0], BAND[1], min(BAND[2], im.width), min(BAND[3], im.height))
            crop = im.crop(box).convert("L")
        scale = TILE_W / crop.width
        crop = crop.resize((TILE_W, max(1, int(crop.height * scale))))
        tiles.append((f"{n:05d}  band {box}", crop))

    if not tiles:
        print("no pages found", file=sys.stderr)
        return 1

    height = sum(t.height + LABEL_H for _, t in tiles)
    sheet = Image.new("L", (TILE_W, height), 255)
    draw = ImageDraw.Draw(sheet)
    y = 0
    for label, tile in tiles:
        draw.text((6, y + 8), label, fill=0)
        y += LABEL_H
        sheet.paste(tile, (0, y))
        y += tile.height
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
