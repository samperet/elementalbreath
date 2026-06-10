# Elemental Breathing

A guided breathing exercise based on the **Sufi purification breaths** (Inayat Khan tradition), cycling through the five elements — Earth, Water, Fire, Air, and Ether.

It's a self-contained `index.html` — no build step, no dependencies, works offline. Just open it in a browser, or **install it as a PWA** (Add to Home Screen) for a full-screen, offline app.

**Live:** https://samperet.github.io/elementalbreath/

## The practice

Each element has its own traditional breath method, quality, and a synthesized soundscape:

| Element | Breath method | Quality | Sound |
| --- | --- | --- | --- |
| **Earth** | in & out through the nose | stability · grounding | deep low drone |
| **Water** | in through nose, out through mouth | flow · purification | flowing stream + drips |
| **Fire** | in through mouth, out through nose | energy · transformation | low roar + crackle |
| **Air** | in & out through the mouth | freedom · expansion | gusting wind |
| **Ether** | soft breath, parted lips | spaciousness · peace | high shimmer + bells |

## Features

- **Minimal home** with a large *Begin* button, an always-visible **sound toggle**, and a hero orb that gently fades between the element icons
- **Settings page** (⚙) for all timing: breaths per element (default 5, range 1–20), breath length, independent inhale / exhale durations, optional holds, element selection, and volume
- **Element icon & glowing orb** that expands on the inhale and contracts on the exhale
- **Synthesized element sounds** via the Web Audio API — no audio files, no network, no licensing concerns; each element's texture is generated live. Toggle + volume.
- **Installable PWA** — web manifest + service worker, fully offline after first load
- Settings persist via `localStorage`; smooth color cross-fades between elements and a resolving completion chime

## Project files

| File | Purpose |
| --- | --- |
| `index.html` | The entire app (UI, audio engine, session logic) |
| `manifest.webmanifest` | PWA manifest |
| `sw.js` | Service worker (offline app shell) |
| `icon-*.png`, `apple-touch-icon.png`, `favicon-32.png` | App icons |
| `gen_icons.py` | Regenerates the icons from SVG (`python3 gen_icons.py`) |

## Controls

| Action | Key | Button |
| --- | --- | --- |
| Pause / resume | `Space` | center |
| Next element | `→` | right |
| End session | `Esc` | left |

> Sound starts only after you press **Begin** — browsers block audio until a user interaction.

## Run it

Open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8731
# then visit http://localhost:8731
```

## License

MIT
