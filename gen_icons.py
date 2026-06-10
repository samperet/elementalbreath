#!/usr/bin/env python3
"""Generate PWA icons + favicon: a square crop of the manuscript background
(the illuminated medallion), at full brightness."""
from PIL import Image

SRC = Image.open("manuscript.jpg").convert("RGB")
CX, CY, HALF = 280, 347, 123  # centered on the circular medallion
CROP = SRC.crop((CX - HALF, CY - HALF, CX + HALF, CY + HALF))

def make(size, path):
    CROP.resize((size, size), Image.LANCZOS).save(path)
    print("wrote", path, f"{size}x{size}")

make(512, "icon-512.png")
make(192, "icon-192.png")
make(180, "apple-touch-icon.png")
make(32,  "favicon-32.png")
# Full-bleed artwork doubles as the maskable variant — the medallion sits
# inside the safe zone, and any mask shape crops into decoration, not padding.
make(512, "icon-maskable-512.png")
make(192, "icon-maskable-192.png")
print("done")
