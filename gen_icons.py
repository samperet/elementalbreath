#!/usr/bin/env python3
"""Generate PWA icon PNGs for Elemental Breathing (a luminous breathing orb)."""
import cairosvg

C = 512  # design canvas

def star(cx, cy, R, inner=0.34):
    ri = R * inner * 0.7071
    pts = [
        (cx, cy - R), (cx + ri, cy - ri), (cx + R, cy), (cx + ri, cy + ri),
        (cx, cy + R), (cx - ri, cy + ri), (cx - R, cy), (cx - ri, cy - ri),
    ]
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
    return d

def svg(orbR=152, glowR=250, ringR=188, sparkleR=60, accent=True):
    cx = cy = C / 2
    accent_star = ""
    if accent:
        accent_star = (
            f'<circle cx="{cx+78:.0f}" cy="{cy-92:.0f}" r="26" fill="url(#sg)" opacity="0.7"/>'
            f'<path d="{star(cx+78, cy-92, 17)}" fill="#ffffff" opacity="0.85"/>'
        )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{C}" height="{C}" viewBox="0 0 {C} {C}">
  <defs>
    <radialGradient id="bg" cx="50%" cy="38%" r="75%">
      <stop offset="0%" stop-color="#15161f"/>
      <stop offset="60%" stop-color="#0a0b11"/>
      <stop offset="100%" stop-color="#06070b"/>
    </radialGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#e8c25a" stop-opacity="0.55"/>
      <stop offset="45%" stop-color="#e0b54f" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#e0b54f" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="sg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="orb" cx="38%" cy="30%" r="78%">
      <stop offset="0%" stop-color="#fff3d4"/>
      <stop offset="22%" stop-color="#ffe2a6"/>
      <stop offset="55%" stop-color="#e6ba53"/>
      <stop offset="82%" stop-color="#bd8a33"/>
      <stop offset="100%" stop-color="#7a571f"/>
    </radialGradient>
  </defs>
  <rect width="{C}" height="{C}" fill="url(#bg)"/>
  <circle cx="{cx}" cy="{cy}" r="{glowR}" fill="url(#glow)"/>
  <circle cx="{cx}" cy="{cy}" r="{ringR}" fill="none" stroke="#ffffff" stroke-opacity="0.16" stroke-width="2.5"/>
  <circle cx="{cx}" cy="{cy}" r="{orbR}" fill="url(#orb)"/>
  <circle cx="{cx}" cy="{cy}" r="{orbR}" fill="none" stroke="#ffffff" stroke-opacity="0.18" stroke-width="1.5"/>
  <circle cx="{cx}" cy="{cy}" r="{sparkleR*1.7:.0f}" fill="url(#sg)" opacity="0.55"/>
  <path d="{star(cx, cy, sparkleR)}" fill="#ffffff" opacity="0.95"/>
  {accent_star}
</svg>'''

STD = svg()
MASK = svg(orbR=118, glowR=190, ringR=148, sparkleR=46, accent=False)

def render(svg_str, size, path):
    cairosvg.svg2png(bytestring=svg_str.encode(), output_width=size, output_height=size, write_to=path)
    print("wrote", path, f"{size}x{size}")

render(STD, 512, "icon-512.png")
render(STD, 192, "icon-192.png")
render(STD, 180, "apple-touch-icon.png")
render(STD, 32,  "favicon-32.png")
render(MASK, 512, "icon-maskable-512.png")
render(MASK, 192, "icon-maskable-192.png")
print("done")
