var LANGUAGE_CACHE = "mq-language-v2";
var COVER_CACHE = "mq-covers-v1";
var COVER_URLS = [
  "/assets/cover-ai-v2.webp",
  "/assets/cover-ai-v2-en.webp"
];

self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(COVER_CACHE).then(function (cache) {
      return cache.addAll(COVER_URLS);
    }).then(function () {
      return self.skipWaiting();
    })
  );
});

self.addEventListener("activate", function (event) {
  event.waitUntil(self.clients.claim());
});

self.addEventListener("fetch", function (event) {
  var url = new URL(event.request.url);
  var isCover =
    url.origin === self.location.origin &&
    COVER_URLS.indexOf(url.pathname) !== -1;

  if (isCover) {
    event.respondWith(
      caches.open(COVER_CACHE).then(function (cache) {
        return cache.match(event.request).then(function (cachedCover) {
          if (cachedCover) return cachedCover;
          return fetch(event.request).then(function (response) {
            if (response.ok) cache.put(event.request, response.clone());
            return response;
          });
        });
      })
    );
    return;
  }

  if (event.request.mode !== "navigate") return;

  var isLanguageSwitch =
    url.origin === self.location.origin &&
    url.search === "?switch=1" &&
    (url.pathname === "/" || url.pathname === "/en/");

  if (!isLanguageSwitch) return;

  event.respondWith(
    caches.open(LANGUAGE_CACHE).then(function (cache) {
      return cache.match(url.pathname).then(function (cachedPage) {
        return cachedPage || fetch(event.request);
      });
    })
  );
});
