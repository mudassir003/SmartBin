self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('smartbin-v3').then((cache) => {
      return cache.addAll(['./', './index.html', './manifest.json', './paho-mqtt.js', './audio.mp3', './icons/icon-192.png', './icons/icon-512.png']);
    })
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== 'smartbin-v3') {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => response || fetch(e.request))
  );
});
