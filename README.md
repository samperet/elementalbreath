# Elemental Breathing

A guided breathing exercise based on the **Sufi purification breaths** (Inayat Khan tradition), cycling through the five elements — Earth, Water, Fire, Air, and Ether.

It's a single, self-contained `index.html` — no build step, no dependencies, works offline. Just open it in a browser.

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

- **Element icon & glowing orb** that expands on the inhale and contracts on the exhale
- **Configurable breaths per element** (default 5, range 1–20)
- **Adjustable timing** — breath length, independent inhale / exhale durations, and optional holds
- **Toggle elements** in or out of the sequence
- **Synthesized element sounds** via the Web Audio API — no audio files, no network, no licensing concerns; each element's texture is generated live and paced to the breath. Master on/off + volume.
- Smooth color cross-fades between elements and a resolving completion chime

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
