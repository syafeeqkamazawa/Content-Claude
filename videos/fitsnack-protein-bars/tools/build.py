#!/usr/bin/env python3
"""Build index.html + compositions/ for the Fitsnack protein bars (voiceover) edit from data/edl.json.

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
    return math.floor((n / FPS - 1e-6) * 1000) / 1000


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


def speech_islands(t0, t1, thr=-35, min_gap=0.12):
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


TIGHT = EDL.get("tighten")


def pieces_of(t_in, t_out):
    """Split a kept range around pauses longer than TIGHT['max_pause'] (keeping TIGHT['keep'] each side).

    Loud blips shorter than TIGHT['blip'] (breaths, clicks over the room noise) do not break a pause.
    """
    if not TIGHT:
        return [(t_in, t_out)]
    thr, mx, keep, blip = TIGHT["threshold_db"], TIGHT["max_pause"], TIGHT["keep"], TIGHT.get("blip", 0.1)
    k0 = int(t_in * 100)
    loud = [k < len(RMS) and RMS[k] >= thr for k in range(k0, int(t_out * 100))]
    i = 0
    while i < len(loud):
        j = i
        while j < len(loud) and loud[j] == loud[i]:
            j += 1
        if loud[i] and (j - i) / 100 < blip:
            loud[i:j] = [False] * (j - i)
        i = j
    out, cur, i = [], t_in, 0
    while i < len(loud):
        j = i
        while j < len(loud) and loud[j] == loud[i]:
            j += 1
        a, b = t_in + i / 100, t_in + j / 100
        if not loud[i] and b - a > mx and a - t_in > 0.2 and t_out - b > 0.2:
            out.append((cur, a + keep))
            cur = b - keep
        i = j
    out.append((cur, t_out))
    return out


vos, cursor_f = [], 0
for v in EDL["vo"]:
    seg = dict(v, start=fr(cursor_f), pieces=[])
    for a, b in pieces_of(v["in"], v["out"]):
        n = round((b - a) * FPS)
        seg["pieces"].append({"in": a, "out": b, "start": fr(cursor_f), "dur": fr_dur(n)})
        cursor_f += n
    seg["end"] = fr(cursor_f)

    def to_out(t, seg=seg):
        for pc in seg["pieces"]:
            if t <= pc["in"] + pc["dur"]:
                return pc["start"] + max(0.0, t - pc["in"])
        return seg["end"]

    seg["words"] = [
        {"text": t, "s": q(to_out(a)), "e": q(min(to_out(b), seg["end"]))}
        for t, a, b in time_words(v["text"], v["in"], v["out"])
    ]
    vos.append(seg)
VO_END = fr(cursor_f)
TOTAL = fr(cursor_f + round(EDL.get("tail", 0) * FPS))  # picture + music hold after the last word
VO = {v["id"]: v for v in vos}


def norm(w):
    return w.lower().strip(".,?!&")


def word_time(vid, word, which="s"):
    """Time of `word` in a voiceover range; 'word#2' is its second occurrence."""
    word, _, nth = word.partition("#")
    nth = int(nth or 1)
    for w in VO[vid]["words"]:
        if norm(w["text"]) == norm(word):
            nth -= 1
            if nth == 0:
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
    lengths = {"whoosh-short": 0.57, "pop": 0.72, "click-soft": 0.36, "ping": 1.3, "sparkle": 1.8, "impact-bass-1": 2.1, "chime": 2.5}
    t = q(max(0, t))
    d = min(lengths[name], TOTAL - t)
    n = len(sfx) + 1
    sfx.append(
        f'<audio id="sfx-{n:02d}-{name}" class="clip" src="assets/sfx/{name}.mp3" data-start="{t}" '
        f'data-duration="{q(d)}" data-track-index="{20 + n}" data-volume="{vol}"></audio>'
    )


for v in vos:
    for i, pc in enumerate(v["pieces"]):
        main_dom.append(
            f'<audio id="vo-{v["id"]}-{i + 1}" class="clip" src="assets/vo.m4a" data-start="{pc["start"]}" data-duration="{pc["dur"]}" '
            f'data-media-start="{round(pc["in"], 3)}" data-track-index="0" data-volume="1"></audio>'
        )

def rate_attr(shot):
    r = shot.get("rate")
    return f' data-playback-rate="{r}"' if r and r != 1 else ""


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
            f'muted playsinline data-start="{s["t0"]}" data-duration="{d}" data-media-start="{s["src"]}"{rate_attr(s)} data-track-index="1"></video></div>'
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

wt = word_time


def at(a):
    vid, what = a
    if what == "start":
        return VO[vid]["start"]
    if what == "end":
        return VO[vid]["end"]
    return word_time(vid, what) - 0.04


# One title per beat (data/edl.json "titles"); "pos": "top" keeps it off faces and the product.
for i, t in enumerate(EDL["titles"]):
    tid = f"tt-{i + 1}"
    t0, t1 = card(f"ov-{tid}", at(t["from"]), min(at(t["to"]), TOTAL),
                  f'<div class="{"cta" if t.get("cta") else "title " + t.get("pos", "low")}" id="{tid}">{html.escape(t["text"])}</div>')
    if t.get("cta"):
        gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "back.out(1.8)" }}, {t0});')
        gfx_js.append(
            f'tl.fromTo("#{tid}", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.4, ease: "sine.inOut", yoyo: true, '
            f'repeat: {max(1, int((t1 - t0 - 0.4) / 0.4) - 1)}, immediateRender: false }}, {q(t0 + 0.35)});'
        )
        add_sfx("ping", t0, 0.4)
    else:
        gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 0, scale: 0.6, y: -20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.32, ease: "back.out(2)" }}, {t0});')
        add_sfx(t.get("sfx", "pop"), t0 - 0.02, t.get("sfx_vol", 0.3))
        if t1 < TOTAL - 0.1 and t1 - t0 > 0.7:
            fade_out(f"#{tid}", t1)

# ── 4. Captions sub-composition ────────────────────────────────────────────
cap_dom, cap_js = [], []
cap_id = 0
for v in vos:
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
.hook {{ position: absolute; left: 60px; right: 60px; top: 960px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 6px;
  background: rgba(16,20,28,.66); padding: 26px 24px 30px; border-radius: 32px; }}
.hook-sm {{ font-family: "Plus Jakarta Sans"; font-weight: 700; font-size: 54px; color: #ffffff; text-shadow: 0 3px 14px rgba(0,0,0,.55); }}
.hook-big {{ font-family: "Archivo Black"; font-size: 100px; white-space: nowrap; line-height: 1; color: {ACCENT}; text-shadow: 0 8px 0 {CHOC}, 0 0 30px rgba(0,0,0,.4); transform-origin: 50% 60%; }}
.hook-md {{ font-family: "Plus Jakarta Sans"; font-weight: 800; font-size: 60px; line-height: 1.1; color: #ffffff; text-shadow: 0 4px 18px rgba(0,0,0,.6); }}
.stack {{ display: flex; flex-direction: column; align-items: flex-start; gap: 14px; }}
.kicker {{ font-weight: 800; font-size: 26px; letter-spacing: 3px; color: {CREAM}; background: rgba(30,24,20,.78); padding: 8px 16px; border-radius: 10px; }}
.chip {{ font-weight: 800; font-size: 48px; color: {CHOC}; background: {CREAM}; padding: 12px 28px; border-radius: 999px;
  box-shadow: 0 10px 24px rgba(0,0,0,.25); transform-origin: 0% 50%; }}
.chip.dark {{ color: {CHOC}; background: {ACCENT}; }}
.brand {{ position: absolute; left: 0; right: 0; top: 250px; margin: 0 auto; width: 800px; display: flex; flex-direction: column; align-items: center; gap: 4px;
  background: {CREAM}; padding: 26px 30px 30px; border-radius: 30px; box-shadow: 0 16px 34px rgba(0,0,0,.28); }}
.brand-lg {{ font-family: "Archivo Black"; font-size: 112px; line-height: 1; color: #1f2a3a; white-space: nowrap; }}
.brand-k {{ font-weight: 800; font-size: 26px; letter-spacing: 4px; color: #6b5a4a; }}
.brand-m {{ font-weight: 700; font-size: 32px; color: #1f2a3a; margin-top: 6px; }}
.brand-sm {{ font-weight: 800; font-size: 38px; color: #1f2a3a; background: {ACCENT}; padding: 8px 22px; border-radius: 999px; }}
.price {{ position: absolute; left: 60px; top: 240px; display: flex; flex-direction: column; align-items: flex-start; gap: 2px;
  background: {CREAM}; padding: 22px 34px 20px; border-radius: 28px; box-shadow: 0 16px 34px rgba(0,0,0,.3); transform-origin: 0% 50%; }}
.price-k {{ font-weight: 800; font-size: 28px; letter-spacing: 3px; color: #6b5a4a; }}
.price-v {{ font-family: "Archivo Black"; font-size: 128px; line-height: 1.02; color: {CHOC}; transform-origin: 0% 60%; }}
.price-n {{ font-weight: 700; font-size: 26px; color: #6b5a4a; }}
.thick {{ position: absolute; left: 910px; top: 236px; width: 80px; height: 1030px; }}
.t-line {{ position: absolute; left: 30px; top: 0; bottom: 0; width: 8px; background: {ACCENT}; border-radius: 4px; transform-origin: 50% 50%; box-shadow: 0 3px 10px rgba(0,0,0,.35); }}
.t-tick {{ position: absolute; left: -18px; width: 44px; height: 8px; background: {ACCENT}; border-radius: 4px; }}
.t-tick.t {{ top: 0; }}
.t-tick.b {{ bottom: 0; }}
.t-label {{ position: absolute; left: -250px; top: 440px; width: 220px; text-align: center; font-family: "Archivo Black"; font-size: 56px;
  color: {CHOC}; background: {ACCENT}; border-radius: 18px; padding: 4px 0 8px; }}
.sizes {{ position: absolute; left: 60px; right: 60px; top: 230px; display: flex; flex-direction: column; align-items: flex-start; gap: 14px; }}
.size-row {{ display: flex; flex-wrap: wrap; gap: 14px; }}
.title {{ position: absolute; left: 50px; right: 50px; top: 980px; text-align: center; font-family: "Archivo Black"; font-size: 62px; line-height: 1.08;
  color: #ffffff; background: rgba(74,32,20,.94); padding: 22px 28px 26px; border-radius: 28px; box-shadow: 0 14px 30px rgba(0,0,0,.3); transform-origin: 50% 50%; }}
.title.top {{ top: 230px; }}
.cta {{ position: absolute; left: 60px; bottom: 300px; font-family: "Archivo Black"; font-size: 54px; color: {CHOC}; background: {ACCENT};
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
    <title>Fitsnack Protein Bars — review</title>
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
    out.append(f"{v['start']:6.2f}-{v['end']:6.2f}  {v['id']}  vo {v['in']:6.2f}-{v['out']:6.2f}  ({len(v['pieces'])} pc)  {v['text']}")
out.append("")
for s in shots:
    what = (f"{s['clip']} @{s['src']:.1f}s" + (f" x{s['rate']}" if s.get("rate") else "")) if "clip" in s else f"photo {s['photo']}"
    out.append(f"{s['t0']:6.2f}-{s['t1']:6.2f}  {s['id']}  {what:16s} {s.get('note', '')}")
(ROOT / "data/cutlist.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))
