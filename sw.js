/* Service worker — offline-first app shell for Elemental Breathing */
const CACHE = "elemental-breath-v20";
const ASSETS = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./fonts.css",
  "./background.mp3",
  "./manuscript.jpg",
  "./sufiheart.png",
  "./icon-192.png",
  "./icon-512.png",
  "./icon-maskable-192.png",
  "./icon-maskable-512.png",
  "./apple-touch-icon.png",
  "./favicon-32.png",
  "./fonts/amiri-400-normal-arabic.woff2",
  "./fonts/amiri-400-normal-latin.woff2",
  "./fonts/amiri-700-normal-arabic.woff2",
  "./fonts/amiri-700-normal-latin.woff2",
  "./fonts/cormorant-garamond-400-normal-latin.woff2",
  "./fonts/cormorant-garamond-500-normal-latin.woff2",
  "./fonts/cormorant-garamond-600-normal-latin.woff2",
  "./fonts/cormorant-garamond-400-italic-latin.woff2",
  "./fonts/cormorant-garamond-500-italic-latin.woff2",
  "./fonts/cormorant-garamond-600-italic-latin.woff2",
  "./fonts/eb-garamond-400-normal-latin.woff2",
  "./fonts/eb-garamond-500-normal-latin.woff2",
  "./fonts/eb-garamond-400-italic-latin.woff2",
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => Promise.allSettled(ASSETS.map((a) => c.add(a))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  // Navigations are network-first so deploys land on the next launch;
  // the cached copy remains the offline fallback.
  if (req.mode === "navigate") {
    e.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
          return res;
        })
        .catch(() =>
          caches.match(req)
            .then((r) => r || caches.match("./index.html"))
            .then((r) => r || caches.match("./"))
        )
    );
    return;
  }
  e.respondWith(
    caches.match(req).then((cached) =>
      cached ||
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
          return res;
        })
        .catch(() => caches.match("./index.html"))
    )
  );
});
