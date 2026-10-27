"""Build the 'Terima kasih Ummi' tribute (28 Oct 1986) from src/: photo slideshow + two park clips,
gentle Ken Burns, cross-dissolves, the owner's message as serif text cards, and the song
(audio of the 'Kaulah ibuku' clip the owner put in the folder) from start to end.
Run from the project root:  python3 tools/build.py   (needs ffmpeg + Pillow)."""
import json, pathlib, subprocess
from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
W, H, SC = 1080, 1920, 1.5          # composition size; stills are made at 1.5x for the zoom
TOTAL = 79.9
SONG = "1CcWJq3AAyaLPde7zho026-0IRPELdURj.mp4"    # owner: 'Lagu tu dari video'
PARK = "1cG6IkI2yi1pCF1U4YjO4NXNW81WU9WK6.mp4"    # selfie walk with Ummi in the park
IDX = {int(l.split(" ", 1)[0]): l.split(" ", 1)[1].strip() for l in (ROOT / "data/photo-index.txt").read_text().splitlines()}

# (kind, source, start, end): one distinct moment per burst of near-identical photos
SLIDES = [("p", 0, 0.0, 4.3), ("p", 5, 4.3, 8.5), ("p", 3, 8.5, 12.7), ("p", 32, 12.7, 16.9),
          ("p", 26, 16.9, 21.1), ("v", (0.0, 3.5), 21.1, 24.6), ("p", 39, 24.6, 28.8),
          ("p", 40, 28.8, 33.0), ("p", 12, 33.0, 37.2), ("p", 2, 37.2, 41.4), ("p", 29, 41.4, 45.6),
          ("p", 16, 45.6, 49.8), ("p", 23, 49.8, 54.0), ("p", 24, 54.0, 58.2), ("p", 10, 58.2, 62.4),
          ("v", (25.5, 29.5), 62.4, 66.4), ("p", 30, 66.4, 70.6), ("p", 41, 70.6, 74.8), ("p", 22, 74.8, TOTAL)]
XF = 0.9   # cross-dissolve

# Owner's message, tidied (27 Oct). 'big' lines are set in the script face.
CARDS = [(0.8, 7.6, [("date", "28 Oktober 1986"), ("", "Hari Ummi bertarung nyawa"), ("", "melahirkan apeq.")]),
         (9.6, 16.6, [("big", "Terima kasih, Ummi"), ("", "atas segala susah payah"), ("", "dan sakit melahirkan apeq.")]),
         (18.3, 27.2, [("", "Apeq banyak drama,"), ("", "banyak melukakan hati Ummi."), ("big", "Maafkan apeq, Ummi")]),
         (29.0, 36.0, [("", "Walau apa pun yang berlaku,"), ("", "apeq akan terus berusaha"), ("", "menjadi anak yang lebih baik.")]),
         (37.8, 46.8, [("", "Mungkin apeq tak mampu membalas dengan harta,"), ("", "tapi doa untuk Ummi dan Abah"), ("", "tak pernah putus, setiap hari.")]),
         (48.0, 56.0, [("", "Semoga syurga Firdaus"), ("", "untuk Ummi dan Abah,"), ("", "dan semoga kita bertemu di sana nanti.")]),
         (57.6, 65.8, [("big", "Ummi,"), ("", "doakan apeq"), ("", "dunia dan akhirat.")]),
         (68.2, 79.0, [("big", "Sayang Ummi"), ("big", "selamanya")])]


def still(n, out):
    """Photo fitted to the frame width over a blurred, darkened copy of itself."""
    im = ImageOps.exif_transpose(Image.open(SRC / IDX[n])).convert("RGB")
    w, h = int(W * SC), int(H * SC)
    r = max(w / im.width, h / im.height)
    bg = im.resize((int(im.width * r) + 1, int(im.height * r) + 1)).crop((0, 0, w, h))
    bg = ImageEnhance.Brightness(bg.filter(ImageFilter.GaussianBlur(60))).enhance(0.55)
    f = min(w / im.width, (h * 0.80) / im.height)
    fg = im.resize((int(im.width * f), int(im.height * f)), Image.LANCZOS)
    fg = ImageEnhance.Color(fg).enhance(1.06)
    top = max(0, int(h * 0.40 - fg.height / 2)) if fg.height < h * 0.62 else int((h * 0.80 - fg.height) / 2)
    bg.paste(fg, ((w - fg.width) // 2, top))
    bg.save(out, quality=92)


def clip(a, b, out):
    """Landscape park clip over its own blurred copy, 60 fps, silent."""
    vf = (f"split[x][y];[x]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=40:2,eq=brightness=-0.18[bg];"
          f"[y]scale={W}:-2,eq=saturation=1.06[fg];[bg][fg]overlay=0:{int(H*0.40)}-h/2,fps=60,setsar=1")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(a), "-t", str(b - a + 0.05), "-i", str(SRC / PARK),
                    "-filter_complex", vf, "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-pix_fmt", "yuv420p",
                    "-g", "30", "-movflags", "+faststart", str(out)], check=True)


def main():
    (ROOT / "assets/photos").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets/clips").mkdir(parents=True, exist_ok=True)
    song = ROOT / "assets/song.m4a"
    if not song.exists():
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(SRC / SONG), "-vn", "-t", str(TOTAL),
                        "-af", f"afade=t=in:d=0.6,afade=t=out:st={TOTAL-3.0}:d=3.0,loudnorm=I=-14:TP=-1.5",
                        "-c:a", "aac", "-b:a", "256k", str(song)], check=True)
    els, js = [], []
    for k, (kind, s, t0, t1) in enumerate(SLIDES):
        a = max(0.0, t0 - (XF if k else 0))
        d = round(t1 - a + (XF if k < len(SLIDES) - 1 else 0), 3)
        sid = f"s{k:02d}"
        if kind == "p":
            out = ROOT / f"assets/photos/p{s:02d}.jpg"
            if not out.exists():
                still(s, out)
            els.append(f'<div class="slide clip" id="{sid}" data-start="{a}" data-duration="{d}" data-track-index="{1 + k % 2}">'
                       f'<img src="assets/photos/{out.name}" /></div>')
        else:
            out = ROOT / f"assets/clips/park-{int(s[0])}.mp4"
            if not out.exists():
                clip(s[0], s[1], out)
            # the wrapper is an untimed container; the <video> alone carries the timing (lint: video_nested_in_timed_element)
            els.append(f'<div class="slide" id="{sid}">'
                       f'<video id="{sid}-v" class="clip" src="assets/clips/{out.name}" muted playsinline data-start="{a}" '
                       f'data-duration="{d}" data-track-index="{3 + k % 2}"></video></div>')
        ox = ["50% 40%", "35% 45%", "65% 45%", "50% 55%"][k % 4]
        js.append(f'tl.set("#{sid}", {{ transformOrigin: "{ox}" }}, 0);')
        js.append(f'tl.fromTo("#{sid}", {{ scale: {1.0 if k % 2 == 0 else 1.07} }}, {{ scale: {1.07 if k % 2 == 0 else 1.0}, duration: {d}, ease: "none" }}, {a});')
        if k:
            js.append(f'tl.fromTo("#{sid}", {{ opacity: 0 }}, {{ opacity: 1, duration: {XF}, ease: "sine.inOut" }}, {a});')
    for c, (t0, t1, lines) in enumerate(CARDS):
        cid = f"c{c}"
        html = "".join(f'<div class="ln {kind or "txt"}" id="{cid}-{i}">{txt}</div>' for i, (kind, txt) in enumerate(lines))
        els.append(f'<div class="card clip" id="{cid}" data-start="{t0}" data-duration="{round(t1 - t0, 3)}" data-track-index="10">{html}</div>')
        for i in range(len(lines)):
            js.append(f'tl.fromTo("#{cid}-{i}", {{ opacity: 0, y: 26, filter: "blur(10px)" }}, {{ opacity: 1, y: 0, filter: "blur(0px)", duration: 1.1, ease: "power2.out" }}, {round(t0 + 0.45 * i, 3)});')
        js.append(f'tl.to("#{cid}", {{ opacity: 0, filter: "blur(8px)", duration: 0.8, ease: "power1.in" }}, {round(t1 - 0.8, 3)});')
    js.append(f'tl.fromTo("#fade", {{ opacity: 1 }}, {{ opacity: 0, duration: 1.2, ease: "sine.out" }}, 0);')
    js.append(f'tl.to("#fade", {{ opacity: 1, duration: 1.4, ease: "sine.in" }}, {TOTAL - 1.4});')
    page = f'''<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <title>Terima kasih Ummi</title>
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
@font-face {{ font-family: "Cormorant Garamond"; src: url("assets/fonts/CormorantGaramond-500.woff2") format("woff2"); font-weight: 500; font-display: block; }}
@font-face {{ font-family: "Cormorant Garamond"; src: url("assets/fonts/CormorantGaramond-500i.woff2") format("woff2"); font-weight: 500; font-style: italic; font-display: block; }}
@font-face {{ font-family: "Great Vibes"; src: url("assets/fonts/GreatVibes-400.woff2") format("woff2"); font-display: block; }}
@font-face {{ font-family: "Montserrat"; src: url("assets/fonts/Montserrat-500.woff2") format("woff2"); font-weight: 500; font-display: block; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #000; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #000; }}
.slide {{ position: absolute; inset: 0; overflow: hidden; }}
.slide img, .slide video {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; }}
#grade {{ position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse at 50% 42%, rgba(255,214,170,0) 45%, rgba(20,8,0,.55) 100%),
              linear-gradient(to bottom, rgba(0,0,0,0) 58%, rgba(10,4,0,.78) 100%); mix-blend-mode: normal; }}
#warm {{ position: absolute; inset: 0; background: #ffb27a; opacity: .07; mix-blend-mode: soft-light; pointer-events: none; }}
.card {{ position: absolute; left: 70px; right: 70px; top: 1340px; height: 520px; display: flex; flex-direction: column;
  align-items: center; justify-content: center; text-align: center; color: #fff8ef; }}
.ln {{ text-shadow: 0 2px 18px rgba(0,0,0,.65), 0 0 2px rgba(0,0,0,.4); }}
.txt {{ font-family: "Cormorant Garamond"; font-weight: 500; font-size: 68px; line-height: 1.22; letter-spacing: .5px; }}
.big {{ font-family: "Great Vibes"; font-size: 132px; line-height: 1.12; color: #ffecd2; }}
.date {{ font-family: "Montserrat"; font-weight: 500; font-size: 38px; letter-spacing: 12px; color: #ffdcab; margin-bottom: 26px; text-transform: uppercase; }}
#fade {{ position: absolute; inset: 0; background: #000; pointer-events: none; }}
</style>
  </head>
  <body>
    <!-- GENERATED by tools/build.py — edit that, not this file. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-fps="60" data-width="{W}" data-height="{H}">
      {chr(10).join("      " + e for e in els).strip()}
      <div id="warm"></div>
      <div id="grade"></div>
      <audio id="song" class="clip" src="assets/song.m4a" data-start="0" data-duration="{TOTAL}" data-track-index="20" data-volume="1"></audio>
      <div id="fade"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {chr(10).join("      " + j for j in js).strip()}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''
    (ROOT / "index.html").write_text(page)
    print("built", len(SLIDES), "slides,", len(CARDS), "cards,", TOTAL, "s")


main()
