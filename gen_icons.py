#!/usr/bin/env python3
"""Generate PWA icons + favicon: the Sufi winged heart centered on a black background."""
from PIL import Image

emblem = Image.open("sufiheart.png").convert("RGBA")
ew, eh = emblem.size  # 400 x 100

def make(size, frac, path):
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 255))
    tw = max(1, int(round(size * frac)))
    th = max(1, int(round(tw * eh / ew)))
    em = emblem.resize((tw, th), Image.LANCZOS)
    canvas.alpha_composite(em, ((size - tw) // 2, (size - th) // 2))
    canvas.convert("RGB").save(path)
    print("wrote", path, f"{size}x{size}")

# Standard icons (a touch of side padding)
make(512, 0.82, "icon-512.png")
make(192, 0.82, "icon-192.png")
make(180, 0.82, "apple-touch-icon.png")
make(32,  0.88, "favicon-32.png")
# Maskable icons (keep emblem inside the safe circle)
make(512, 0.68, "icon-maskable-512.png")
make(192, 0.68, "icon-maskable-192.png")
print("done")
