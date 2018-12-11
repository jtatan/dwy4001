
var staticCacheName = 'djangopwa-v1';



self.addEventListener('install', function(event) {
event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {

      return cache.addAll([

        '/'
        // y las otras cosas que quieres sean cacheadas como imagenes, etc
        // a nosotros con solo colocar la url del base (o index) nos atrapaba todo lo static, aca habría que probar pero si tienes en el base.html el LOAD STATIC FROM STATICFILES debería funcionar
        // sino , agregar aqui las cosas minimas para hacer el shell de cosas minimas
      ]);

    })

  );

});



self.addEventListener('fetch', function(event) {

  var requestUrl = new URL(event.request.url);

    if (requestUrl.origin === location.origin) {

      if ((requestUrl.pathname === '/')) {

        event.respondWith(caches.match('/'));

        return;

      }

    }

    event.respondWith(

      caches.match(event.request).then(function(response) {

        return response || fetch(event.request);

      })

    );

});