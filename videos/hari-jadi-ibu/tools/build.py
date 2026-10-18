"""Build index.html (photo memory slideshow) from data/edl.json."""
import json
from PIL import Image

EDL = json.load(open("data/edl.json"))
T, XF, LAST = EDL["duration"], EDL["xf"], EDL["last_hold"]
seq = EDL["sequence"]
n_photos = sum(isinstance(s, str) for s in seq)
clip_strides = sum(s["dur"] - XF for s in seq if isinstance(s, dict))
STRIDE = (T - LAST - clip_strides) / (n_photos - 1)
assert STRIDE - XF >= 5.0, STRIDE

ROT = [-1.6, 1.3, -0.8, 1.7, -1.2, 0.9]
MAXW, MAXH, CY, PAD = 930, 1150, 860, 16
f = lambda x: round(x, 4)

els, js = [], []
t, pi = 0.0, 0
slots = []
for i, s in enumerate(seq):
    last = i == len(seq) - 1
    if isinstance(s, str):
        dur = LAST if last else STRIDE + XF
        slots.append(("photo", s, t, dur)); t += STRIDE
    else:
        slots.append(("clip", s["clip"], t, s["dur"])); t += s["dur"] - XF
assert abs(slots[-1][2] + slots[-1][3] - T) < 0.01, slots[-1]

for i, (kind, src, st, dur) in enumerate(slots):
    sid = f"s{i:02d}"
    prev_clip = i > 0 and slots[i - 1][0] == "clip"
    if kind == "photo":
        w, h = Image.open(f"assets/photos/{src}.jpg").size
        sc = min(MAXW / w, MAXH / h); pw, ph = round(w * sc), round(h * sc)
        cy = CY if i in (0, len(slots) - 1) else 950  # intro/outro photos sit higher to leave room for text
        left, top = (1080 - pw) // 2 - PAD, cy - ph // 2 - PAD
        rot = ROT[pi % len(ROT)]
        els.append(
            f'<div id="{sid}" class="slide clip" data-start="{f(st)}" data-duration="{f(dur)}" data-track-index="1">'
            f'<img class="bg" id="{sid}-bg" src="assets/photos/{src}-bg.jpg" alt="">'
            f'<div class="print" id="{sid}-pr" style="left:{left}px;top:{top}px;width:{pw + 2 * PAD}px;height:{ph + 2 * PAD}px">'
            f'<div class="frame" id="{sid}-fr" style="transform:rotate({rot}deg)"><div class="pic">'
            f'<img id="{sid}-im" src="assets/photos/{src}.jpg" alt="" style="width:{pw}px;height:{ph}px"></div></div></div></div>')
        ox = ["50% 40%", "35% 50%", "65% 50%", "50% 60%"][pi % 4]
        js.append(f'tl.set("#{sid}-im", {{ transformOrigin: "{ox}" }}, 0);')
        js.append(f'tl.fromTo("#{sid}-im", {{ scale: 1.0 }}, {{ scale: 1.09, duration: {f(dur)}, ease: "none" }}, {f(st)});')
        js.append(f'tl.fromTo("#{sid}-bg", {{ scale: 1.08 }}, {{ scale: 1.18, duration: {f(dur)}, ease: "none" }}, {f(st)});')
        js.append(f'tl.fromTo("#{sid}-fr", {{ y: 14 }}, {{ y: -14, duration: {f(dur)}, ease: "sine.inOut" }}, {f(st)});')
        tr = "leak" if prev_clip else EDL["transitions"][(pi - 1) % len(EDL["transitions"])]
        pi += 1
    else:
        els.append(
            f'<div id="{sid}" class="slide">'
            f'<video id="{sid}-v" class="clip" src="{src}" muted playsinline data-start="{f(st)}" data-duration="{f(dur)}" '
            f'data-media-start="0" data-track-index="2"></video>'
            f'<div class="vig clip" data-start="{f(st)}" data-duration="{f(dur)}" data-track-index="3"></div></div>')
        js.append(f'tl.fromTo("#{sid}-v", {{ scale: 1.0 }}, {{ scale: 1.06, duration: {f(dur)}, ease: "none" }}, {f(st)});')
        tr = "leak"
    if i == 0:
        continue
    js.append(f'tl.fromTo("#{sid}", {{ opacity: 0 }}, {{ opacity: 1, duration: {XF}, ease: "sine.inOut" }}, {f(st)});')
    if tr == "blur":
        js.append(f'tl.fromTo("#{sid}", {{ filter: "blur(18px)" }}, {{ filter: "blur(0px)", duration: {f(XF + 0.3)}, ease: "sine.out" }}, {f(st)});')
    elif tr == "zoom" and kind == "photo":
        js.append(f'tl.fromTo("#{sid}-pr", {{ scale: 1.16 }}, {{ scale: 1.0, duration: {f(XF + 0.6)}, ease: "power2.out" }}, {f(st)});')
    elif tr == "rise" and kind == "photo":
        js.append(f'tl.fromTo("#{sid}-pr", {{ y: 160, rotation: -3 }}, {{ y: 0, rotation: 0, duration: {f(XF + 0.6)}, ease: "power3.out" }}, {f(st)});')
    elif tr == "leak":
        js.append(f'tl.fromTo("#leak", {{ opacity: 0 }}, {{ opacity: 0.85, duration: {f(XF * 0.6)}, ease: "sine.in" }}, {f(st - XF * 0.2)});')
        js.append(f'tl.to("#leak", {{ opacity: 0, duration: {f(XF * 1.4)}, ease: "sine.out" }}, {f(st + XF * 0.4)});')

# intro text over the first photo
I, O = EDL["intro"], EDL["outro"]
it0, it1 = 0.7, STRIDE - 0.35
els.append(
    f'<div id="intro" class="txt clip" data-start="0" data-duration="{f(STRIDE)}" data-track-index="5">'
    f'<div class="script" id="in-a">{I["script"]}</div><div class="name" id="in-b">{I["name"]}</div>'
    f'<div class="line" id="in-c">{I["line"]}</div></div>')
js += [
    f'tl.fromTo("#in-a", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 1.2, ease: "power2.out" }}, {it0});',
    f'tl.fromTo("#in-b", {{ opacity: 0, scale: 0.86 }}, {{ opacity: 1, scale: 1, duration: 1.4, ease: "power2.out" }}, {it0 + 0.5});',
    f'tl.fromTo("#in-c", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "sine.out" }}, {it0 + 1.3});',
    f'tl.to("#intro", {{ opacity: 0, duration: 0.6, ease: "sine.in" }}, {f(it1 - 0.6)});',
]
ls = slots[-1][2]
els.append(
    f'<div id="outro" class="txt clip" data-start="{f(ls)}" data-duration="{f(LAST)}" data-track-index="5">'
    f'<div class="script" id="out-a">{O["script"]}</div><div class="line big" id="out-b">{O["line"]}</div>'
    f'<div class="sign" id="out-c">{O["sign"]}</div></div>')
js += [
    f'tl.fromTo("#out-a", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 1.4, ease: "power2.out" }}, {f(ls + 1.0)});',
    f'tl.fromTo("#out-b", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 1.2, ease: "sine.out" }}, {f(ls + 2.2)});',
    f'tl.fromTo("#out-c", {{ opacity: 0, scale: 0.9 }}, {{ opacity: 1, scale: 1, duration: 1.2, ease: "power2.out" }}, {f(ls + 3.4)});',
    f'tl.fromTo("#black", {{ opacity: 1 }}, {{ opacity: 0, duration: 1.4, ease: "sine.out" }}, 0);',
    f'tl.to("#black", {{ opacity: 1, duration: 2.0, ease: "sine.in" }}, {f(T - 2.0)});',
]

html = f'''<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>Hari Jadi Ibu — memori</title>
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
@font-face {{ font-family: "Great Vibes"; src: url(assets/fonts/GreatVibes-latin.woff2) format("woff2"); font-weight: 400; }}
@font-face {{ font-family: "Playfair Display"; src: url(assets/fonts/PlayfairDisplay-latin.woff2) format("woff2"); font-weight: 400 900; font-style: normal; }}
@font-face {{ font-family: "Playfair Display"; src: url(assets/fonts/PlayfairDisplay-Italic-latin.woff2) format("woff2"); font-weight: 400 900; font-style: italic; }}
@font-face {{ font-family: "Plus Jakarta Sans"; src: url(assets/fonts/PlusJakartaSans-latin.woff2) format("woff2"); font-weight: 200 800; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #0d0907; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #0d0907; }}
.slide {{ position: absolute; inset: 0; overflow: hidden; }}
.slide .bg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
.slide video {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
.print {{ position: absolute; }}
.frame {{ width: 100%; height: 100%; padding: {PAD}px; background: #fbf7ef; border-radius: 4px;
  box-shadow: 0 30px 70px rgba(0,0,0,.55), 0 6px 18px rgba(0,0,0,.35); }}
.pic {{ width: 100%; height: 100%; overflow: hidden; }}
.pic img {{ display: block; }}
.vig {{ position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.45) 100%); }}
#vignette {{ position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 60%, rgba(20,8,0,.35) 100%); }}
#leak {{ position: absolute; inset: 0; opacity: 0; mix-blend-mode: screen;
  background: radial-gradient(ellipse at 30% 35%, rgba(255,236,200,1) 0%, rgba(255,196,130,.75) 35%, rgba(255,160,90,.25) 65%, rgba(0,0,0,0) 85%); }}
#black {{ position: absolute; inset: 0; background: #000; }}
.txt {{ position: absolute; left: 0; right: 0; top: 0; bottom: 0; text-align: center; color: #fff7ea;
  background: linear-gradient(180deg, rgba(0,0,0,0) 62%, rgba(12,6,2,.78) 86%, rgba(12,6,2,.88) 100%);
  text-shadow: 0 4px 22px rgba(0,0,0,.6); }}
.txt > div {{ position: absolute; left: 60px; right: 60px; }}
.script {{ font-family: "Great Vibes", cursive; font-size: 118px; line-height: 1.1; color: #f6d9a8; top: 1430px; }}
.name {{ font-family: "Playfair Display", serif; font-style: italic; font-weight: 600; font-size: 170px; line-height: 1; top: 1555px; letter-spacing: 2px; }}
.line {{ font-family: "Plus Jakarta Sans", sans-serif; font-weight: 500; font-size: 44px; top: 1760px; letter-spacing: .5px; color: #f3e6d2; }}
.line.big {{ top: 1580px; font-size: 46px; line-height: 1.4; }}
.sign {{ font-family: "Playfair Display", serif; font-style: italic; font-weight: 500; font-size: 62px; top: 1735px; color: #f6d9a8; }}
</style>
  </head>
  <body>
    <!-- GENERATED by tools/build.py from data/edl.json — edit those, not this file. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-fps="30" data-width="1080" data-height="1920">
      <audio id="song" class="clip" src="{EDL["audio"]}" data-start="0" data-duration="{T}" data-track-index="0" data-volume="1"></audio>
      ''' + "\n      ".join(els) + f'''
      <div id="vignette" class="clip" data-start="0" data-duration="{T}" data-track-index="6"></div>
      <div id="leak" class="clip" data-start="0" data-duration="{T}" data-track-index="7"></div>
      <div id="black" class="clip" data-start="0" data-duration="{T}" data-track-index="8"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      ''' + "\n      ".join(js) + '''
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
open("index.html", "w").write(html)
print(f"stride {STRIDE:.3f}s (fully visible {STRIDE - XF:.2f}s); slots:")
for k, s_, st, d in slots: print(f"  {st:7.2f} {d:6.2f} {k} {s_}")
