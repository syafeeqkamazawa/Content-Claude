"""Writes index.html for the Cikgu Zaiton retirement tribute from data/sequence.json (tools/prep.py).
Look: warm, elegant — each photo slowly pushes in (alternating drift), photos cross-dissolve, a chapter line in
gold Cormorant small caps + a Playfair caption on a soft dark band, gold particles-free (calm), title and closing
cards in Great Vibes script. 1920x1080, 60 fps. Re-run after editing tools/prep.py; never hand-edit index.html."""
import json, pathlib, html

P = pathlib.Path(__file__).resolve().parents[1]
FPS, W, H = 60, 1920, 1080
TITLE, PHOTO, XF, END = 6.0, 3.15, 0.8, 8.6
SEQ = json.loads((P / "data/sequence.json").read_text())
N = len(SEQ)
TOTAL = round(TITLE + N * PHOTO + END, 3)


def q(t): return round(round(t * FPS) / FPS, 4)


dom, js = [], []
# title card
dom.append(f'<div id="title" class="clip card" data-start="0" data-duration="{q(TITLE + XF)}" data-track-index="5">'
           '<div class="card-in" id="title-in"><div class="kicker" id="t-k">Sekalung Penghargaan</div>'
           '<div class="script" id="t-s">Cikgu Zaiton binti Mat Isa</div><div class="rule" id="t-r"></div>'
           '<div class="sub" id="t-sub">1 Ogos 1997 &nbsp;—&nbsp; 5 November 2026</div>'
           '<div class="sub2" id="t-sub2">29 tahun 3 bulan 4 hari mendidik anak bangsa</div></div></div>')
js += ['tl.fromTo("#t-k", { opacity: 0, scale: 1.12 }, { opacity: 1, scale: 1, duration: 1.4, ease: "power2.out" }, 0.3);',
       'tl.fromTo("#t-s", { opacity: 0, y: 30, filter: "blur(10px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 1.6, ease: "power3.out" }, 0.9);',
       'tl.fromTo("#t-r", { scaleX: 0 }, { scaleX: 1, duration: 1.2, ease: "power2.inOut" }, 1.9);',
       'tl.fromTo("#t-sub", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }, 2.5);',
       'tl.fromTo("#t-sub2", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }, 3.0);',
       f'tl.fromTo("#title-in", {{ scale: 1 }}, {{ scale: 1.04, duration: {TITLE + XF}, ease: "none", immediateRender: false }}, 0);',
       f'tl.to("#title", {{ opacity: 0, duration: {XF}, ease: "sine.inOut" }}, {q(TITLE)});']

for i, s in enumerate(SEQ):
    t0 = q(TITLE + i * PHOTO)
    d = q(PHOTO + XF)
    pid = f"p{i:02d}"
    side = 1 if i % 2 == 0 else -1
    chap = f'<div class="chap" id="{pid}-c">{html.escape(s["chapter"])}</div>' if s["chapter"] else ""
    dom.append(f'<div id="{pid}" class="clip photo" data-start="{t0}" data-duration="{d}" data-track-index="{1 + i % 2}">'
               f'<div class="ph" id="{pid}-i" style="background-image:url({s["file"]})"></div>'
               f'<div class="band"></div><div class="cap-wrap">{chap}<div class="cap" id="{pid}-t">{html.escape(s["caption"])}</div></div></div>')
    js.append(f'tl.fromTo("#{pid}", {{ opacity: 0 }}, {{ opacity: 1, duration: {XF}, ease: "sine.inOut" }}, {t0});')
    js.append(f'tl.fromTo("#{pid}-i", {{ scale: 1.0, x: {-10 * side} }}, {{ scale: 1.07, x: {10 * side}, duration: {d}, ease: "none", immediateRender: false }}, {t0});')
    if s["chapter"]:
        js.append(f'tl.fromTo("#{pid}-c", {{ opacity: 0, scale: 1.08 }}, {{ opacity: 1, scale: 1, duration: 1.0, ease: "power2.out" }}, {q(t0 + 0.35)});')
    js.append(f'tl.fromTo("#{pid}-t", {{ opacity: 0, y: 14 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }}, {q(t0 + 0.55)});')
    js.append(f'tl.to("#{pid}-t", {{ opacity: 0, duration: 0.4, ease: "power1.in" }}, {q(t0 + PHOTO - 0.1)});')

# closing card
c0 = q(TITLE + N * PHOTO)
dom.append(f'<div id="end" class="clip card" data-start="{c0}" data-duration="{q(TOTAL - c0)}" data-track-index="6">'
           '<div class="card-in" id="end-in"><div class="script big" id="e-s">Selamat Bersara</div><div class="rule" id="e-r"></div>'
           '<div class="sub" id="e-1">Terima kasih atas ilmu, kasih sayang dan pengorbanan, Cikgu.</div>'
           '<div class="sub2" id="e-2">SMK Perempuan Pudu &nbsp;·&nbsp; SMK Abdul Jalil &nbsp;·&nbsp; SMK Bandar Tun Hussein Onn 2 &nbsp;·&nbsp; SMK Taman Jasmin 2</div>'
           '<div class="sub2" id="e-3">Anugerah Perkhidmatan Cemerlang 2009 &amp; 2022</div></div></div>')
js += [f'tl.fromTo("#end", {{ opacity: 0 }}, {{ opacity: 1, duration: 1.0, ease: "sine.inOut" }}, {c0});',
       f'tl.fromTo("#e-s", {{ opacity: 0, y: 30, filter: "blur(10px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)", duration: 1.6, ease: "power3.out" }}, {q(c0 + 0.6)});',
       f'tl.fromTo("#e-r", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 1.2, ease: "power2.inOut" }}, {q(c0 + 1.5)});',
       f'tl.fromTo("#e-1", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, {q(c0 + 2.1)});',
       f'tl.fromTo("#e-2", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, {q(c0 + 2.7)});',
       f'tl.fromTo("#e-3", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, {q(c0 + 3.2)});',
       f'tl.fromTo("#end-in", {{ scale: 1 }}, {{ scale: 1.04, duration: {q(TOTAL - c0)}, ease: "none", immediateRender: false }}, {c0});',
       f'tl.to("#end-in", {{ opacity: 0, duration: 1.6, ease: "sine.in" }}, {q(TOTAL - 1.7)});']

dom.append(f'<audio id="music" class="clip" src="assets/music.m4a" data-start="0" data-duration="{TOTAL}" data-track-index="10" data-volume="1"></audio>')

CSS = f"""
@font-face {{ font-family: "Playfair Display"; src: url("assets/fonts/playfair-display-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-display: block; }}
@font-face {{ font-family: "Playfair Display"; src: url("assets/fonts/playfair-display-latin-700-normal.woff2") format("woff2"); font-weight: 700; font-display: block; }}
@font-face {{ font-family: "Great Vibes"; src: url("assets/fonts/great-vibes-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-display: block; }}
@font-face {{ font-family: "Cormorant Garamond"; src: url("assets/fonts/cormorant-garamond-latin-400-normal.woff2") format("woff2"); font-weight: 400; font-display: block; }}
@font-face {{ font-family: "Cormorant Garamond"; src: url("assets/fonts/cormorant-garamond-latin-600-normal.woff2") format("woff2"); font-weight: 600; font-display: block; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #120d09; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #120d09; }}
.photo, .card {{ position: absolute; inset: 0; overflow: hidden; }}
.ph {{ position: absolute; inset: 0; background: center / cover no-repeat; transform-origin: 50% 45%; will-change: transform; }}
.band {{ position: absolute; left: 0; right: 0; bottom: 0; height: 230px; background: linear-gradient(180deg, rgba(10,7,4,0) 0%, rgba(10,7,4,.62) 55%, rgba(10,7,4,.8) 100%); }}
.cap-wrap {{ position: absolute; left: 120px; right: 120px; bottom: 34px; text-align: center; }}
.chap {{ font-family: "Cormorant Garamond"; font-weight: 600; font-size: 34px; letter-spacing: 8px; color: #E7C27A; text-transform: uppercase; margin-bottom: 6px;
  text-shadow: 0 2px 10px rgba(0,0,0,.6); }}
.cap {{ font-family: "Playfair Display"; font-weight: 400; font-style: normal; font-size: 40px; line-height: 1.25; color: #FBF6EC; text-shadow: 0 2px 14px rgba(0,0,0,.75); }}
.card {{ background: radial-gradient(ellipse at 50% 45%, #3a2a1b 0%, #1d140c 55%, #0e0906 100%); }}
.card-in {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; transform-origin: 50% 50%; }}
.kicker {{ font-family: "Cormorant Garamond"; font-weight: 600; font-size: 40px; letter-spacing: 12px; color: #E7C27A; text-transform: uppercase; }}
.script {{ font-family: "Great Vibes"; font-size: 150px; line-height: 1.15; color: #F6E7C8; margin-top: 18px; text-shadow: 0 6px 30px rgba(0,0,0,.5); }}
.script.big {{ font-size: 190px; }}
.rule {{ width: 520px; height: 3px; margin: 26px 0 30px; background: linear-gradient(90deg, rgba(231,194,122,0), #E7C27A, rgba(231,194,122,0)); transform-origin: 50% 50%; }}
.sub {{ font-family: "Playfair Display"; font-size: 44px; color: #FBF6EC; }}
.sub2 {{ font-family: "Cormorant Garamond"; font-weight: 600; font-size: 34px; letter-spacing: 2px; color: #D9C29A; margin-top: 16px; }}
"""

page = f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <title>Selamat Bersara Cikgu Zaiton</title>
    <script src="assets/vendor/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <!-- GENERATED by tools/build.py from data/sequence.json — edit tools/prep.py, not this file. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-fps="{FPS}" data-width="{W}" data-height="{H}">
      {chr(10).join('      ' + d for d in dom).strip()}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {chr(10).join('      ' + j for j in js).strip()}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(page)
(P / "data/timeline.json").write_text(json.dumps({"total": TOTAL, "photos": N, "title": TITLE, "photo": PHOTO, "end": END}, indent=1))
print("TOTAL", TOTAL, "photos", N)
