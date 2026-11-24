import json, re, pathlib
from PIL import Image, ImageDraw, ImageFont
B = pathlib.Path(__file__).parent; D = B.parent / 'road_check_v4'; D.mkdir(exist_ok=True)
rows = []
for line in (B/'cameras.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'): continue
    road, cid, desc, d, lat, lon, chan = line.split('|')
    assert road in ('I95','TPK','JTB') and d in ('N','S','E','W',''), line
    rows.append([road, cid, desc, d, float(lat), float(lon), int(chan)])
html = (B/'app.html').read_text().replace('__CAMERAS__', json.dumps(rows, separators=(',',':')))
assert '__CAMERAS__' not in html
(D/'index.html').write_text(html)
(D/'manifest.webmanifest').write_text(json.dumps({
  "name":"Road Check","short_name":"Road Check","description":"Pre-drive check of FL511 cameras and reported delays",
  "start_url":"./","scope":"./","display":"standalone","background_color":"#0b1020","theme_color":"#0b1020",
  "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"},
           {"src":"icon-512-maskable.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]}, indent=1))
(D/'sw.js').write_text("""// Road Check service worker: keeps the app itself available; never caches camera images or traffic data.
const SHELL='road-check-v4.2';
const FILES=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(SHELL).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==SHELL).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const u=new URL(e.request.url);
  if(e.request.method!=='GET'||u.origin!==location.origin)return; // cameras, FDOT and TomTom always go to the network
  e.respondWith(fetch(e.request).then(r=>{const copy=r.clone();caches.open(SHELL).then(c=>c.put(e.request,copy));return r;}).catch(()=>caches.match(e.request).then(m=>m||caches.match('./index.html'))));
});
""")
def icon(size, pad_frac, name):
    im = Image.new('RGB', (size, size), '#0b1020'); d = ImageDraw.Draw(im)
    p = int(size*pad_frac); w = size - 2*p
    # road: perspective trapezoid
    d.polygon([(p+w*0.36,p+w*0.08),(p+w*0.64,p+w*0.08),(p+w*0.95,p+w*0.95),(p+w*0.05,p+w*0.95)], fill='#26405c')
    for k in range(4):  # center dashes
        y0 = p+w*(0.16+k*0.2); y1 = y0+w*0.1
        d.polygon([(p+w*0.485,y0),(p+w*0.515,y0),(p+w*(0.52+k*0.004),y1),(p+w*(0.48-k*0.004),y1)], fill='#f3c548')
    # camera lens dot
    r = w*0.14; cx, cy = p+w*0.78, p+w*0.22
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill='#62d2ef'); d.ellipse([cx-r*0.45,cy-r*0.45,cx+r*0.45,cy+r*0.45], fill='#0b1020')
    im.save(D/name)
icon(192, 0.06, 'icon-192.png'); icon(512, 0.06, 'icon-512.png'); icon(512, 0.18, 'icon-512-maskable.png'); icon(180, 0.08, 'apple-touch-icon.png')
counts = {}
for r in rows: counts[r[0]] = counts.get(r[0],0)+1
print('cameras', counts, 'index.html bytes', len(html))
