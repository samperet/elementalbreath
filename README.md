# Elemental Breathing

A guided breathing exercise based on the **Sufi purification breaths** (Inayat Khan tradition), cycling through the five elements — Earth, Water, Fire, Air, and Ether.

It's a self-contained `index.html` — no build step, no dependencies, works offline. Just open it in a browser, or **install it as a PWA** (Add to Home Screen) for a full-screen, offline app.

**Live:** https://samperet.github.io/elementalbreath/

## The practice

Each element has its own traditional breath method (5 breaths each) and a color to visualize:

| Element | Breath method | Visualize |
| --- | --- | --- |
| **Earth** | in through the nose, out through the nose | the color **gold** |
| **Water** | in through the nose, out through the mouth | the color **green** |
| **Fire** | in through the mouth, out through the nose | the color **red** |
| **Air** | in through the mouth, out through the mouth | the color **blue** |
| **Ether** | in through the nose, out through the nose — very refined | the color **grey**, or transparency |

**Dhikr.** Silently say **Ya Shafee** (the Healer) on the in-breath, and **Ya Kafee** (the Remedy) on the out-breath. These cues are shown with each breath by default; you can toggle them off in settings.

## Features

- **Minimal home** with a large *Begin* button, an always-visible **music toggle**, and a hero orb that gently fades between the element icons
- **Settings page** (⚙) for all timing: breaths per element (default 5, range 1–20), breath length, independent inhale / exhale durations, optional holds, element selection, and volume
- **Element icon & glowing orb** that expands on the inhale and contracts on the exhale, themed to each element's color
- **Dhikr cues** — *Ya Shafee* (the Healer) on the in-breath, *Ya Kafee* (the Remedy) on the out-breath; shown by default
- **Background music** — a looping ambient track plays through the whole practice. A music toggle is available on the home screen **and during the session**, plus a volume control. A single chime resolves the practice at the end.
- **Installable PWA** — web manifest + service worker, fully offline after first load (audio included)
- Settings persist via `localStorage`; smooth color cross-fades between elements and a resolving completion chime

## Project files

| File | Purpose |
| --- | --- |
| `index.html` | The entire app (UI, audio engine, session logic) |
| `background.mp3` | Looping background music |
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

> Music starts only after you press **Begin** — browsers block audio until a user interaction.

## Run it

Open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8731
# then visit http://localhost:8731
```

## License

MIT
