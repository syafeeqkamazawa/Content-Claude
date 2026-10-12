#!/usr/bin/env python3
"""Build index.html + compositions/ for the Dadaus brookies review from data/edl.json.

Run from the project root:  python3 tools/build.py
Edit data/edl.json (voiceover ranges, shot list) and re-run; never hand-edit the HTML.
Owner's standing rules live in /CLAUDE.md (full-screen realistic overlays only,
aurat fully covered, small Plus Jakarta Sans captions, preview before final).
"""
import array
import html
import json
import math
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
EDL = json.loads((ROOT / "data/edl.json").read_text())
FPS = EDL["fps"]
W, H = EDL["width"], EDL["height"]
KEYWORDS = {k.lower() for k in EDL["keywords"]}

ACCENT = "#FFC61A"  # TikTok "beg kuning" yellow
CREAM = "#FFF6E6"
CHOC = "#3B2416"


def q(t):
    return round(round(t * FPS) / FPS, 4)


def fr(n):
    return round(n / FPS, 4)


def fr_dur(n):
    """Duration of n frames, floored so start + dur never passes the next start."""
    return math.floor(n / FPS * 1000) / 1000


# ── 1. Voiceover: kept ranges laid end to end ──────────────────────────────
RMS_PATH = ROOT / "data/vo-rms.json"
if not RMS_PATH.exists():
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(ROOT / "assets/vo.m4a"), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
        check=True, capture_output=True,
    ).stdout
    a = array.array("h", pcm)
    rms = []
    for i in range(0, len(a) - 160, 160):
        blk = a[i : i + 160]
        rms.append(round(10 * math.log10(sum(x * x for x in blk) / 160 / 32768**2 + 1e-12), 1))
    RMS_PATH.write_text(json.dumps(rms))
RMS = json.loads(RMS_PATH.read_text())


def speech_islands(t0, t1, thr=-42, min_gap=0.12):
    out, start, last = [], None, None
    for k in range(int(t0 * 100), int(t1 * 100)):
        if k < len(RMS) and RMS[k] > thr:
            t = k / 100
            if start is None:
                start = t
            elif t - last > min_gap:
                out.append([start, last + 0.01])
                start = t
            last = t
    if start is not None:
        out.append([start, last + 0.01])
    return [i for i in out if i[1] - i[0] > 0.05] or [[t0, t1]]


def syllables(word):
    return max(1, len(re.findall(r"[aeiouy]+", word.lower())))


def time_words(text, t_in, t_out):
    """Spread words over the detected speech by syllable count (Malay is syllable-timed)."""
    words = text.split()
    isl = speech_islands(t_in, t_out)
    speech = sum(b - a for a, b in isl)
    syl = [syllables(w) for w in words]
    total = sum(syl)

    def at(frac):
        rem = frac * speech
        for a, b in isl:
            if rem <= b - a:
                return a + rem
            rem -= b - a
        return isl[-1][1]

    out, acc = [], 0
    for w, n in zip(words, syl):
        out.append((w, at(acc / total), at((acc + n) / total)))
        acc += n
    return out


vos, cursor_f = [], 0
for v in EDL["vo"]:
    dur_f = round((v["out"] - v["in"]) * FPS)
    seg = dict(v, start=fr(cursor_f), dur=fr_dur(dur_f), end=fr(cursor_f + dur_f))
    seg["words"] = [
        {"text": t, "s": q(seg["start"] + a - v["in"]), "e": q(seg["start"] + b - v["in"])}
        for t, a, b in time_words(v["text"], v["in"], v["out"])
    ]
    vos.append(seg)
    cursor_f += dur_f
TOTAL = fr(cursor_f)
VO = {v["id"]: v for v in vos}


def norm(w):
    return w.lower().strip(".,?!&")


def word_time(vid, word, which="s"):
    for w in VO[vid]["words"]:
        if norm(w["text"]) == norm(word):
            return w[which]
    raise KeyError(f"{word!r} not in {vid}: {[w['text'] for w in VO[vid]['words']]}")


def anchor(a):
    vid, what = a
    if what == "start":
        return VO[vid]["start"]
    if what == "end":
        return VO[vid]["end"]
    return word_time(vid, what)


# ── 2. Root: voiceover, picture, sfx ───────────────────────────────────────
main_dom, main_js, sfx = [], [], []


def add_sfx(name, t, vol):
    lengths = {"whoosh-short": 0.57, "pop": 0.72, "click-soft": 0.36, "ping": 1.3, "sparkle": 1.8}
    t = q(max(0, t))
    d = min(lengths[name], TOTAL - t)
    n = len(sfx) + 1
    sfx.append(
        f'<audio id="sfx-{n:02d}-{name}" class="clip" src="assets/sfx/{name}.mp3" data-start="{t}" '
        f'data-duration="{q(d)}" data-track-index="{20 + n}" data-volume="{vol}"></audio>'
    )


for v in vos:
    main_dom.append(
        f'<audio id="vo-{v["id"]}" class="clip" src="assets/vo.m4a" data-start="{v["start"]}" data-duration="{v["dur"]}" '
        f'data-media-start="{v["in"]}" data-track-index="0" data-volume="1"></audio>'
    )

shots, ai_tags = [], []
for s in EDL["shots"]:
    shots.append(dict(s, t0=q(anchor(s["at"]))))
for i, s in enumerate(shots):
    s["t1"] = shots[i + 1]["t0"] if i + 1 < len(shots) else TOTAL
    s["id"] = f"P{i + 1:02d}"

for s in shots:
    d = fr_dur(round((s["t1"] - s["t0"]) * FPS))
    sel = f'#pw-{s["id"]}'
    if "clip" in s:
        main_dom.append(
            f'<div class="frame-wrap" id="pw-{s["id"]}"><video id="v-{s["id"]}" class="clip" src="assets/{s["clip"]}.mp4" '
            f'muted playsinline data-start="{s["t0"]}" data-duration="{d}" data-media-start="{s["src"]}" data-track-index="1"></video></div>'
        )
    else:
        main_dom.append(
            f'<div class="frame-wrap" id="pw-{s["id"]}"><div id="v-{s["id"]}" class="clip photo" data-start="{s["t0"]}" '
            f'data-duration="{d}" data-track-index="1" style="background-image:url(assets/photos/{s["photo"]}.jpg)"></div></div>'
        )
        ai_tags.append((s["id"], s["t0"], s["t0"] + d))
        add_sfx("whoosh-short", s["t0"] - 0.08, 0.28)
    # gentle punch on the cut, then a slow push for the rest of the shot
    main_js.append(f'tl.fromTo("{sel}", {{ scale: 1.08 }}, {{ scale: 1.0, duration: 0.3, ease: "power3.out" }}, {s["t0"]});')
    main_js.append(
        f'tl.fromTo("{sel}", {{ scale: 1.0 }}, {{ scale: 1.06, duration: {q(max(0.1, d - 0.34))}, ease: "none", immediateRender: false }}, {q(s["t0"] + 0.34)});'
    )

# ── 3. Graphics sub-composition (text-only cards; no emoji or symbol icons) ─
gfx_dom, gfx_js = [], []


def card(cid, t0, t1, inner):
    t0, t1 = q(t0), q(min(t1, TOTAL))
    gfx_dom.append(f'<div id="{cid}" class="clip overlay" data-start="{t0}" data-duration="{q(t1 - t0)}" data-track-index="2">{inner}</div>')
    return t0, t1


def pop_in(sel, t, from_scale=0.5, ease="back.out(2)"):
    gfx_js.append(f'tl.fromTo("{sel}", {{ opacity: 0, scale: {from_scale} }}, {{ opacity: 1, scale: 1, duration: 0.28, ease: "{ease}" }}, {q(t)});')


def fade_out(sel, t):
    gfx_js.append(f'tl.to("{sel}", {{ opacity: 0, duration: 0.2, ease: "power2.in" }}, {q(t - 0.2)});')


# AI photos carry a small "ILUSTRASI AI" tag for their whole shot.
for pid, a, b in ai_tags:
    card(f"ov-ai-{pid}", a, b, '<div class="ai-tag">ILUSTRASI AI</div>')

# Hook: "Brookies ni tak semua orang buat jadi… tapi yang ni SEDAP BETUL!"
v1, v2 = VO["V01"], VO["V02"]
t0, t1 = card(
    "ov-hook", 0, v2["end"],
    '<div class="hook">'
    '<div class="hook-sm" id="hk-1">Brookies ni</div>'
    '<div class="hook-md" id="hk-2">tak semua orang<br/>buat jadi…</div>'
    '<div class="hook-sm" id="hk-3">tapi yang ni</div>'
    '<div class="hook-big" id="hk-4">SEDAP BETUL!</div>'
    "</div>",
)
pop_in("#hk-1", 0.0, 0.8, "power3.out")
pop_in("#hk-2", word_time("V01", "tak"), 0.8, "power3.out")
pop_in("#hk-3", v2["start"], 0.8, "power3.out")
pop_in("#hk-4", word_time("V02", "sedap"), 0.4, "back.out(2.4)")
fade_out("#ov-hook .hook", t1)
add_sfx("sparkle", word_time("V02", "sedap") - 0.05, 0.35)

# Flavours.
v6 = VO["V06"]
t0, t1 = card(
    "ov-flav", VO["V05"]["start"], VO["V07"]["end"],
    '<div class="stack top"><div class="kicker" id="fl-k">PILIHAN FLAVOUR</div>'
    '<div class="chip" id="fl-1">Original</div><div class="chip" id="fl-2">Hazelnut</div>'
    '<div class="chip" id="fl-3">Cookies &amp; Cream</div><div class="chip dark" id="fl-4">Boleh mix!</div></div>',
)
pop_in("#fl-k", t0, 0.8, "power3.out")
for sel, w in [("#fl-1", "original,"), ("#fl-2", "hazelnut"), ("#fl-3", "cookies")]:
    pop_in(sel, word_time("V06", w))
    add_sfx("pop", word_time("V06", w), 0.35)
pop_in("#fl-4", word_time("V07", "mix"))
add_sfx("pop", word_time("V07", "mix"), 0.35)
fade_out("#ov-flav .stack", t1)

# Reviews → pure butter.
t0, t1 = card("ov-rev", VO["V08"]["start"] + 0.1, word_time("V08", "patutlah"),
              '<div class="stack top"><div class="chip" id="rv-1">Tengok review dulu</div></div>')
pop_in("#rv-1", t0)
fade_out("#ov-rev .stack", t1)
t_pure = word_time("V08", "pure")
t0, t1 = card("ov-butter", t_pure - 0.05, VO["V08"]["end"],
              '<div class="badge" id="bt-1"><span class="badge-sm">GUNA</span><span class="badge-lg">PURE BUTTER</span></div>')
pop_in("#bt-1", t0, 0.4, "back.out(2.4)")
add_sfx("pop", t0, 0.4)

# 5 inci measurement across the brookie (overhead shot).
t5 = word_time("V09", "5")
t0, t1 = card(
    "ov-size", t5 - 0.1, word_time("V09", "tapi"),
    '<div class="measure"><div class="m-line" id="ms-line"><i class="m-tick l"></i><i class="m-tick r"></i></div>'
    '<div class="m-label" id="ms-lab">5 inci</div></div>',
)
gfx_js.append(f'tl.fromTo("#ms-line", {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.4, ease: "power3.out" }}, {t0});')
pop_in("#ms-lab", t0 + 0.25)
add_sfx("click-soft", t0, 0.4)
fade_out("#ov-size .measure", t1)

# "Kena beli lebih".
t_lebih = word_time("V09", "lebih")
t0, t1 = card("ov-lebih", t_lebih - 0.1, VO["V09"]["end"],
              '<div class="stack top"><div class="chip dark" id="lb-1">Confirm tak cukup satu!</div></div>')
pop_in("#lb-1", t0)
add_sfx("pop", t0, 0.35)
fade_out("#ov-lebih .stack", t1)

# Sweetness.
t_ngam = word_time("V11", "ngam-ngam")
t0, t1 = card("ov-manis", VO["V10"]["start"] + 0.2, VO["V11"]["end"],
              '<div class="stack top"><div class="kicker" id="mn-k">TAHAP MANIS</div>'
              '<div class="chip" id="mn-1">Tak terlalu manis</div><div class="chip dark" id="mn-2">Ngam-ngam je</div></div>')
pop_in("#mn-k", t0, 0.8, "power3.out")
pop_in("#mn-1", word_time("V10", "terlalu"))
pop_in("#mn-2", t_ngam)
add_sfx("pop", t_ngam, 0.35)
fade_out("#ov-manis .stack", t1)

# CTA checklist + beg kuning.
v12 = VO["V12"]
t0, t1 = card(
    "ov-cta", word_time("V12", "freshly") - 0.1, TOTAL,
    '<div class="stack top"><div class="chip" id="ct-1">Freshly baked</div><div class="chip" id="ct-2">Tak terlalu manis</div>'
    '<div class="chip" id="ct-3">Pure butter</div></div>'
    '<div class="cta" id="ct-btn">Beli dekat beg kuning</div>',
)
for sel, w in [("#ct-1", "freshly"), ("#ct-2", "terlalu"), ("#ct-3", "pure")]:
    pop_in(sel, word_time("V12", w))
    add_sfx("pop", word_time("V12", w), 0.3)
t_beg = word_time("V12", "beg")
gfx_js.append(f'tl.fromTo("#ct-btn", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "back.out(1.8)" }}, {q(t_beg - 0.1)});')
gfx_js.append(
    f'tl.fromTo("#ct-btn", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.4, ease: "sine.inOut", yoyo: true, '
    f'repeat: {max(1, int((TOTAL - t_beg - 0.4) / 0.4) - 1)}, immediateRender: false }}, {q(t_beg + 0.25)});'
)
add_sfx("ping", t_beg - 0.1, 0.4)

# ── 4. Captions sub-composition ────────────────────────────────────────────
cap_dom, cap_js = [], []
cap_id = 0
for v in vos:
    if v["id"] in ("V01", "V02"):  # the hook title carries these lines
        continue
    chunks, cur = [], []
    for w in v["words"]:
        cur.append(w)
        if len(cur) == 3 or w["text"][-1:] in ",.?!" or len("".join(x["text"] for x in cur)) > 16:
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    k = 0
    while k < len(chunks) and len(chunks) > 1:
        end = chunks[k + 1][0]["s"] if k + 1 < len(chunks) else v["end"]
        if end - chunks[k][0]["s"] < 0.45:
            if k > 0 and len(chunks[k - 1]) < 4:
                chunks[k - 1] += chunks.pop(k)
                continue
            if k + 1 < len(chunks):
                chunks[k + 1] = chunks[k] + chunks[k + 1]
                chunks.pop(k)
                continue
        k += 1
    for i, ch in enumerate(chunks):
        c0 = v["start"] if i == 0 else ch[0]["s"]
        c1 = chunks[i + 1][0]["s"] if i + 1 < len(chunks) else v["end"]
        if c1 - c0 < 0.1:
            continue
        cap_id += 1
        spans = []
        for j, w in enumerate(ch):
            txt = w["text"].strip(",.")
            kw = " kw" if norm(w["text"]) in KEYWORDS else ""
            spans.append(f'<span class="w{kw}" id="c{cap_id}-w{j}">{html.escape(txt)}</span>')
            cap_js.append(f'tl.fromTo("#c{cap_id}-w{j}", {{ scale: 1 }}, {{ scale: 1.04, duration: 0.08, ease: "power2.out", immediateRender: false }}, {w["s"]});')
            cap_js.append(f'tl.to("#c{cap_id}-w{j}", {{ scale: 1, duration: 0.1, ease: "power2.in" }}, {max(w["e"], q(w["s"] + 0.09))});')
        cap_dom.append(
            f'<div id="cap-{cap_id}" class="clip cap" data-start="{q(c0)}" data-duration="{math.floor((c1 - c0) * 1000) / 1000}" data-track-index="3">'
            f'<div class="cap-in" id="cap-{cap_id}-in">{" ".join(spans)}</div></div>'
        )
        cap_js.append(f'tl.fromTo("#cap-{cap_id}-in", {{ scale: 0.9, y: 12 }}, {{ scale: 1, y: 0, duration: 0.14, ease: "back.out(2)" }}, {q(c0)});')

# ── 5. Music bed (HeyGen catalog), carved under the voiceover ──────────────
CARVE_PATH = ROOT / "data/bgm-carve.json"
carve_attrs = ""
if CARVE_PATH.exists():
    carve_attrs = "".join(f" {k}='{v}'" for k, v in json.loads(CARVE_PATH.read_text()).items())
if (ROOT / "assets/audio/bgm-bed.m4a").exists():
    sfx.insert(0, f'<audio id="music-bed" class="clip" src="assets/audio/bgm-bed.m4a" data-start="0" data-duration="{TOTAL}" '
                  f'data-track-index="10" data-volume="1"{carve_attrs}></audio>')

# ── 6. Write files ─────────────────────────────────────────────────────────
FONT_FACE = """@font-face { font-family: "Plus Jakarta Sans"; src: url("assets/fonts/PlusJakartaSans-latin.woff2") format("woff2");
  font-weight: 200 800; font-style: normal; font-display: block; }"""

CSS_MAIN = f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #120b06; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #120b06; font-family: "Montserrat", sans-serif; }}
.frame-wrap {{ position: absolute; inset: 0; overflow: hidden; transform-origin: 50% 45%; }}
.frame-wrap video {{ position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; }}
.frame-wrap .photo {{ position: absolute; inset: 0; background: center / cover no-repeat; }}
"""

CSS_GFX = FONT_FACE + f"""
#gfx-root {{ position: absolute; inset: 0; font-family: "Plus Jakarta Sans", sans-serif; }}
.overlay {{ position: absolute; inset: 0; pointer-events: none; }}
.ai-tag {{ position: absolute; left: 36px; top: 160px; font-family: "Montserrat"; font-weight: 700; font-size: 18px; letter-spacing: 1.5px;
  color: {CREAM}; background: rgba(20,12,6,.55); padding: 5px 10px; border-radius: 6px; }}
.top {{ position: absolute; left: 60px; top: 230px; }}
.hook {{ position: absolute; left: 60px; right: 60px; top: 1040px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 4px; }}
.hook-sm {{ font-family: "Plus Jakarta Sans"; font-weight: 700; font-size: 54px; color: {CREAM}; text-shadow: 0 3px 14px rgba(0,0,0,.6); }}
.hook-md {{ font-family: "Plus Jakarta Sans"; font-weight: 800; font-size: 76px; line-height: 1.05; color: #ffffff; text-shadow: 0 4px 18px rgba(0,0,0,.6); margin-bottom: 18px; }}
.hook-big {{ font-family: "Archivo Black"; font-size: 120px; line-height: 1; color: {ACCENT}; text-shadow: 0 8px 0 {CHOC}, 0 0 30px rgba(0,0,0,.45); transform-origin: 50% 60%; }}
.stack {{ display: flex; flex-direction: column; align-items: flex-start; gap: 14px; }}
.kicker {{ font-weight: 800; font-size: 26px; letter-spacing: 3px; color: {CREAM}; background: rgba(30,18,10,.78); padding: 8px 16px; border-radius: 10px; }}
.chip {{ font-weight: 800; font-size: 50px; color: {CHOC}; background: {CREAM}; padding: 12px 28px; border-radius: 999px;
  box-shadow: 0 10px 24px rgba(0,0,0,.28); transform-origin: 0% 50%; }}
.chip.dark {{ color: {CHOC}; background: {ACCENT}; }}
.badge {{ position: absolute; left: 60px; top: 260px; display: flex; flex-direction: column; align-items: flex-start; gap: 6px;
  background: {CREAM}; padding: 20px 30px 24px; border-radius: 26px; box-shadow: 0 16px 34px rgba(0,0,0,.32); transform-origin: 0% 50%; }}
.badge-sm {{ font-weight: 800; font-size: 26px; letter-spacing: 4px; color: #9a6a3a; }}
.badge-lg {{ font-family: "Archivo Black"; font-size: 84px; line-height: 1; color: {CHOC}; }}
.measure {{ position: absolute; left: 320px; width: 470px; top: 950px; height: 130px; }}
.m-line {{ position: absolute; left: 0; right: 0; top: 0; height: 8px; background: {ACCENT}; border-radius: 4px; transform-origin: 50% 50%;
  box-shadow: 0 3px 10px rgba(0,0,0,.35); }}
.m-tick {{ position: absolute; top: -18px; width: 8px; height: 44px; background: {ACCENT}; border-radius: 4px; }}
.m-tick.l {{ left: 0; }}
.m-tick.r {{ right: 0; }}
.m-label {{ position: absolute; left: 0; right: 0; top: 30px; margin: 0 auto; width: 230px; text-align: center; font-family: "Archivo Black"; font-size: 64px;
  color: {CHOC}; background: {ACCENT}; border-radius: 18px; padding: 4px 0 8px; }}
.cta {{ position: absolute; left: 60px; bottom: 420px; font-family: "Archivo Black"; font-size: 54px; color: {CHOC}; background: {ACCENT};
  padding: 22px 36px; border-radius: 999px; box-shadow: 0 12px 0 {CHOC}; transform-origin: 0% 50%; }}
"""

CSS_CAP = FONT_FACE + f"""
#cap-root {{ position: absolute; inset: 0; font-family: "Plus Jakarta Sans", sans-serif; }}
.cap {{ position: absolute; left: 60px; right: 140px; top: 1210px; height: 200px; display: flex; align-items: center; justify-content: center; }}
.cap-in {{ display: flex; flex-wrap: wrap; justify-content: center; text-align: center; max-width: 820px;
  padding: 10px 22px 12px; border-radius: 20px; background: rgba(15,10,3,.40);
  font-family: "Plus Jakarta Sans"; font-weight: 800; font-size: 56px; line-height: 1.22; color: #ffffff; letter-spacing: -0.5px;
  text-shadow: 0 2px 10px rgba(0,0,0,.45); }}
.cap .w {{ display: inline-block; margin: 0 12px; transform-origin: 50% 70%; }}
.cap .w.kw {{ color: {ACCENT}; }}
"""


def lines(items, indent):
    return ("\n" + " " * indent).join(items)


def subcomp(comp_id, root_id, css, dom_items, js_items):
    return f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <!-- GENERATED by tools/build.py from data/edl.json — edit those, not this file. -->
    <template>
      <style>{css}</style>
      <div id="{root_id}" data-composition-id="{comp_id}" data-width="{W}" data-height="{H}">
        {lines(dom_items, 8)}
      </div>
      <script>
        (function () {{
          const tl = gsap.timeline({{ paused: true }});
          {lines(js_items, 10)}
          window.__timelines["{comp_id}"] = tl;
        }})();
      </script>
    </template>
  </body>
</html>
"""


(ROOT / "compositions").mkdir(exist_ok=True)
(ROOT / "compositions/graphics.html").write_text(subcomp("graphics", "gfx-root", CSS_GFX, gfx_dom, gfx_js))
(ROOT / "compositions/captions.html").write_text(subcomp("captions", "cap-root", CSS_CAP, cap_dom, cap_js))

hosts = [
    f'<div id="graphics" data-composition-id="graphics" data-composition-src="compositions/graphics.html" '
    f'data-start="0" data-duration="{TOTAL}" data-track-index="2" data-width="{W}" data-height="{H}"></div>',
    f'<div id="captions" data-track-kind="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" '
    f'data-start="0" data-duration="{TOTAL}" data-track-index="3" data-width="{W}" data-height="{H}"></div>',
]

(ROOT / "index.html").write_text(f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <title>Brookies Dadaus — review</title>
    <script src="assets/vendor/gsap.min.js"></script>
    <style>{CSS_MAIN}</style>
  </head>
  <body>
    <!-- GENERATED by tools/build.py from data/edl.json — edit those, not this file. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-fps="{FPS}" data-width="{W}" data-height="{H}">
      {lines(main_dom, 6)}
      {lines(hosts, 6)}
      {lines(sfx, 6)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
      {lines(main_js, 6)}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
""")

out = [f"TOTAL {TOTAL:.2f}s  ({len(vos)} voiceover ranges, {len(shots)} shots, {len(sfx)} audio fx, {cap_id} caption cards)", ""]
for v in vos:
    out.append(f"{v['start']:6.2f}-{v['end']:6.2f}  {v['id']}  vo {v['in']:6.2f}-{v['out']:6.2f}  {v['text']}")
out.append("")
for s in shots:
    what = f"{s['clip']} @{s['src']:.1f}s" if "clip" in s else f"photo {s['photo']}"
    out.append(f"{s['t0']:6.2f}-{s['t1']:6.2f}  {s['id']}  {what:16s} {s.get('note', '')}")
(ROOT / "data/cutlist.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))
