// Road Check service worker: keeps the app itself available; never caches camera images or traffic data.
const SHELL='road-check-v4.8';
const FILES=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(SHELL).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==SHELL).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(e.request.method!=='GET'||u.origin!==location.origin)return; // cameras, FDOT and TomTom always go to the network
  e.respondWith(fetch(e.request).then(r=>{const copy=r.clone();caches.open(SHELL).then(c=>c.put(e.request,copy));return r;}).catch(()=>caches.match(e.request).then(m=>m||caches.match('./index.html'))));
});
