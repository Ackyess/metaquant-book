var LANGUAGE_CACHE = "mq-language-v2";

self.addEventListener("install", function () {
  self.skipWaiting();
});

self.addEventListener("activate", function (event) {
  event.waitUntil(self.clients.claim());
});

self.addEventListener("fetch", function (event) {
  if (event.request.mode !== "navigate") return;

  var url = new URL(event.request.url);
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
