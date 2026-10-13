#!/usr/bin/env python3
"""Build index.html + compositions/ for the Dr.Ritta Berry Buddies edit from data/edl.json.

Run from the project root:  python3 tools/build.py
Edit data/edl.json (cuts, B-roll picks, photos) and re-run; never hand-edit index.html.
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

ACCENT = "#FF9AB5"  # strawberry pink, from the Berry Buddies pack
BERRY = "#E8456B"
INK = "#4A1530"
CREAM = "#FFF6F8"
YELLOW = "#FFC61A"  # TikTok "beg kuning"


def q(t):
    """Quantize to the frame grid."""
    return round(round(t * FPS) / FPS, 4)


def fr(n):
    return round(n / FPS, 4)


def fr_dur(n):
    """Duration of n frames, floored so start + dur never passes the next start."""
    return math.floor((n / FPS - 1e-6) * 1000) / 1000


# ── 1. A-roll: kept ranges, tightened, laid end to end ─────────────────────
RMS_PATH = ROOT / "data/a-rms.json"
if not RMS_PATH.exists():
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(ROOT / "assets/a.mp4"), "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
        check=True, capture_output=True,
    ).stdout
    a = array.array("h", pcm)
    rms = []
    for i in range(0, len(a) - 160, 160):
        blk = a[i : i + 160]
        rms.append(round(10 * math.log10(sum(x * x for x in blk) / 160 / 32768**2 + 1e-12), 1))
    RMS_PATH.write_text(json.dumps(rms))
RMS = json.loads(RMS_PATH.read_text())
TIGHT = EDL["tighten"]


def speech_islands(t0, t1, thr=-40, min_gap=0.12):
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


# Spoken syllables for words the vowel count gets wrong.
SYL = {"dr.ritta": 4, "3": 2, "12": 4, "fluoride": 3, "synergy": 3, "lysozyme": 3, "parent": 2, "check": 1, "strawberi": 3}


def syllables(word):
    w = word.lower().strip(".,?!")
    return SYL.get(w) or max(1, len(re.findall(r"[aeiouy]+", w)))


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


def pieces_of(t_in, t_out):
    """Split a kept range around pauses longer than max_pause (keeping `keep` each side).

    Loud blips shorter than `blip` (breaths, clicks) do not break a pause.
    """
    thr, mx, keep, blip = TIGHT["threshold_db"], TIGHT["max_pause"], TIGHT["keep"], TIGHT["blip"]
    loud = [k < len(RMS) and RMS[k] >= thr for k in range(int(t_in * 100), int(t_out * 100))]
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


segs, cursor_f = [], 0
for s in EDL["segments"]:
    seg = dict(s, start=fr(cursor_f), pieces=[])
    for a, b in pieces_of(s["in"], s["out"]):
        n = round((b - a) * FPS)
        seg["pieces"].append({"in": a, "start": fr(cursor_f), "dur": fr_dur(n), "len": n / FPS})
        cursor_f += n
    seg["end"] = fr(cursor_f)

    def to_out(t, seg=seg):
        for pc in seg["pieces"]:
            if t <= pc["in"] + pc["len"]:
                return pc["start"] + max(0.0, t - pc["in"])
        return seg["end"]

    seg["words"] = [
        {"text": t, "s": q(to_out(a)), "e": q(min(to_out(b), seg["end"]))}
        for t, a, b in time_words(s["text"], s["in"], s["out"])
    ]
    segs.append(seg)
TOTAL = fr(cursor_f)
SEG = {s["id"]: s for s in segs}


def norm(w):
    return w.lower().strip(".,?!&")


def word_time(seg_id, word, which="s"):
    """Time of `word` in a segment; 'word#2' is its second occurrence."""
    word, _, nth = word.partition("#")
    nth = int(nth or 1)
    for w in SEG[seg_id]["words"]:
        if norm(w["text"]) == norm(word):
            nth -= 1
            if nth == 0:
                return w[which]
    raise KeyError(f"{word!r} not in {seg_id}: {[w['text'] for w in SEG[seg_id]['words']]}")


def anchor(a):
    seg_id, what = a
    if what == "start":
        return SEG[seg_id]["start"]
    if what == "end":
        return SEG[seg_id]["end"]
    return word_time(seg_id, what) - 0.04


# ── 2. Root: A-roll, B-roll, sfx ───────────────────────────────────────────
main_dom, main_js, sfx = [], [], []


def add_sfx(name, t, vol):
    lengths = {"whoosh-short": 0.57, "pop": 0.72, "click-soft": 0.36, "ping": 1.3, "sparkle": 1.8,
               "chime": 2.5, "impact-bass-1": 2.1}
    t = q(max(0, t))
    d = min(lengths[name], TOTAL - t)
    n = len(sfx) + 1
    sfx.append(
        f'<audio id="sfx-{n:02d}-{name}" class="clip" src="assets/sfx/{name}.mp3" data-start="{t}" '
        f'data-duration="{q(d)}" data-track-index="{20 + n}" data-volume="{vol}"></audio>'
    )


# One <video> per tightened piece; the wrapper per segment carries the zoom.
for s in segs:
    vids = []
    for i, pc in enumerate(s["pieces"]):
        vids.append(
            f'<video id="a-{s["id"]}-{i + 1}" class="clip aroll" src="assets/a.mp4" playsinline data-has-audio="true" '
            f'data-start="{pc["start"]}" data-duration="{pc["dur"]}" data-media-start="{round(pc["in"], 3)}" data-track-index="0"></video>'
        )
    main_dom.append(f'<div class="frame-wrap" id="wrap-{s["id"]}">' + "".join(vids) + "</div>")
    main_js.append(f'tl.set("#wrap-{s["id"]}", {{ scale: {s["zoom"]} }}, 0);')
    # Alternate the framing on the jump cuts inside a segment.
    for i, pc in enumerate(s["pieces"][1:], 1):
        z = s["zoom"] * (1.08 if i % 2 else 1.0)
        main_js.append(f'tl.set("#wrap-{s["id"]}", {{ scale: {round(z, 3)} }}, {pc["start"]});')

# Punch-ins on the emotional beats.
for seg_id, word, amount in [("S01", "drama", 1.12), ("S02", "risau", 1.1), ("S06", "tekan", 1.1)]:
    z = SEG[seg_id]["zoom"]
    t = word_time(seg_id, word)
    main_js.append(
        f'tl.fromTo("#wrap-{seg_id}", {{ scale: {z} }}, {{ scale: {round(z * amount, 3)}, duration: 0.22, ease: "power3.out", immediateRender: false }}, {t});'
    )

# B-roll from video 2 (hands only, muted).
cover = []  # (t0, t1) of everything full-screen over the A-roll
for b in EDL["broll"]:
    t0, t1 = q(anchor(b["from"])), q(min(anchor(b["to"]), TOTAL))
    d = fr_dur(round((t1 - t0) * FPS))
    main_dom.append(
        f'<div class="frame-wrap broll" id="bw-{b["id"]}"><video id="b-{b["id"]}" class="clip" src="assets/b.mp4" muted playsinline '
        f'data-start="{t0}" data-duration="{d}" data-media-start="{b["src"]}" data-track-index="1"></video></div>'
    )
    main_js.append(f'tl.fromTo("#bw-{b["id"]}", {{ scale: 1.12 }}, {{ scale: 1.0, duration: 0.3, ease: "power3.out" }}, {t0});')
    main_js.append(
        f'tl.fromTo("#bw-{b["id"]}", {{ scale: 1.0 }}, {{ scale: 1.06, duration: {q(max(0.1, d - 0.34))}, ease: "none", immediateRender: false }}, {q(t0 + 0.34)});'
    )
    cover.append((t0, t1))

# ── 3. Visuals: full-screen realistic AI cutaways ──────────────────────────
# Owner's standing rules (see /CLAUDE.md): full-screen, realistic only, every
# person fully covers aurat, small "ILUSTRASI AI" tag.
vis_dom, vis_js = [], []
for p in EDL["photos"]:
    t0, t1 = q(anchor(p["from"])), q(min(anchor(p["to"]), TOTAL))
    vis_dom.append(
        f'<div id="fs-{p["id"]}" class="clip fs" data-start="{t0}" data-duration="{fr_dur(round((t1 - t0) * FPS))}" data-track-index="4">'
        f'<div class="fs-in" id="fs-{p["id"]}-in" style="background-image:url(assets/photos/{p["id"]}.jpg)"></div>'
        f'<div class="fs-tag">ILUSTRASI AI</div></div>'
    )
    vis_js.append(f'tl.fromTo("#fs-{p["id"]}-in", {{ scale: 1.16 }}, {{ scale: 1.04, duration: 0.35, ease: "power3.out" }}, {t0});')
    vis_js.append(
        f'tl.fromTo("#fs-{p["id"]}-in", {{ scale: 1.04 }}, {{ scale: 1.1, duration: {q(max(0.1, t1 - t0 - 0.4))}, ease: "none", immediateRender: false }}, {q(t0 + 0.4)});'
    )
    cover.append((t0, t1))

# A whoosh only where a cutaway starts from the talking head (not cutaway → cutaway).
cover.sort()
for i, (t0, t1) in enumerate(cover):
    if i == 0 or abs(cover[i - 1][1] - t0) > 0.05:
        add_sfx("whoosh-short", t0 - 0.08, 0.3)

# ── 4. Graphics (text cards; no emoji or symbol icons) ─────────────────────
gfx_dom, gfx_js = [], []


def card(cid, t0, t1, inner):
    t0, t1 = q(t0), q(min(t1, TOTAL))
    gfx_dom.append(f'<div id="{cid}" class="clip overlay" data-start="{t0}" data-duration="{q(t1 - t0)}" data-track-index="2">{inner}</div>')
    return t0, t1


def pop_in(sel, t, from_scale=0.5, ease="back.out(2)"):
    gfx_js.append(f'tl.fromTo("{sel}", {{ opacity: 0, scale: {from_scale} }}, {{ opacity: 1, scale: 1, duration: 0.28, ease: "{ease}" }}, {q(t)});')


def fade_out(sel, t):
    gfx_js.append(f'tl.to("{sel}", {{ opacity: 0, duration: 0.2, ease: "power2.in" }}, {q(t - 0.2)});')


wt = word_time

# Hook: "Suruh anak gosok gigi… mesti ada DRAMA!"
t0, t1 = card(
    "ov-hook", 0, wt("S01", "ada#2") - 0.05,
    '<div class="hook"><div class="hook-sm" id="hk-1">Suruh anak gosok gigi…</div>'
    '<div class="hook-big" id="hk-2">MESTI ADA DRAMA!</div></div>',
)
gfx_js.append(f'tl.fromTo("#ov-hook .hook", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, ease: "power2.out" }}, 0);')
pop_in("#hk-1", 0.05, 0.8, "power3.out")
pop_in("#hk-2", wt("S01", "drama"), 0.4, "back.out(2.4)")
add_sfx("impact-bass-1", wt("S01", "drama") - 0.02, 0.35)
fade_out("#ov-hook .hook", t1)

# Brand reveal over the box shot.
s2 = SEG["S02"]
t_br = wt("S02", "dr.ritta")
t0, t1 = card(
    "ov-brand", t_br - 0.05, wt("S02", "ubat") - 0.05,
    '<div class="brand" id="br-card"><div class="brand-k">UBAT GIGI KANAK-KANAK</div>'
    '<div class="brand-lg">Dr.Ritta</div><div class="brand-sm" id="br-2">Berry Buddies</div></div>',
)
pop_in("#br-card", t0, 0.6, "back.out(1.8)")
pop_in("#br-2", wt("S02", "berry"), 0.8, "power3.out")
add_sfx("sparkle", t0, 0.3)
fade_out("#br-card", t1)

t0, t1 = card(
    "ov-age", wt("S02", "ubat") - 0.05, s2["end"] + 0.1,
    '<div class="stack top"><div class="kicker" id="ag-k">KHAS UNTUK KANAK-KANAK</div>'
    '<div class="chip dark" id="ag-1">Umur 3–12 tahun</div><div class="chip" id="ag-2">Perisa strawberi</div></div>',
)
pop_in("#ag-k", t0, 0.8, "power3.out")
pop_in("#ag-1", wt("S02", "umur"))
pop_in("#ag-2", wt("S02", "perisa"))
add_sfx("pop", wt("S02", "umur"), 0.3)
add_sfx("pop", wt("S02", "perisa"), 0.3)
fade_out("#ov-age .stack", t1)

# Fluoride.
s3 = SEG["S03"]
t0, t1 = card(
    "ov-fluo", wt("S03", "dual") - 0.1, s3["end"] + 0.1,
    '<div class="stack top"><div class="kicker" id="fl-k">FORMULA</div><div class="chip dark" id="fl-1">Dual fluoride synergy</div>'
    '<div class="chip" id="fl-2">Kuatkan enamel gigi</div><div class="chip" id="fl-3">Lindungi daripada kaviti</div></div>',
)
pop_in("#fl-k", t0, 0.8, "power3.out")
pop_in("#fl-1", wt("S03", "dual"))
pop_in("#fl-2", wt("S03", "menguatkan"))
pop_in("#fl-3", wt("S03", "perlindungan"))
for w in ("dual", "menguatkan", "perlindungan"):
    add_sfx("pop", wt("S03", w), 0.3)
fade_out("#ov-fluo .stack", t1)

# Enzymes.
s4 = SEG["S04"]
t0, t1 = card(
    "ov-enz", wt("S04", "dua") - 0.1, wt("S04", "sesuai") - 0.05,
    '<div class="stack top"><div class="kicker" id="en-k">DUA ENZIM</div><div class="chip dark" id="en-1">Papain</div>'
    '<div class="chip dark" id="en-2">Lysozyme</div><div class="chip" id="en-3">Bantu bersihkan gigi</div></div>',
)
pop_in("#en-k", t0, 0.8, "power3.out")
pop_in("#en-1", wt("S04", "papain"))
pop_in("#en-2", wt("S04", "lysozyme"))
pop_in("#en-3", wt("S04", "pembersihan"))
for w in ("papain", "lysozyme", "pembersihan"):
    add_sfx("pop", wt("S04", w), 0.3)
fade_out("#ov-enz .stack", t1)
t0, t1 = card("ov-daily", wt("S04", "rutin") - 0.1, s4["end"] + 0.1,
              '<div class="stack top"><div class="chip dark" id="dy-1">Rutin harian anak</div></div>')
pop_in("#dy-1", t0)
add_sfx("pop", t0, 0.3)
fade_out("#ov-daily .stack", t1)

# Texture + taste, with the label's under-6 usage note on the squeeze shot.
s5 = SEG["S05"]
t0, t1 = card(
    "ov-tex", wt("S05", "lembut") - 0.1, wt("S05", "jadi") - 0.05,
    '<div class="stack top"><div class="chip" id="tx-1">Tekstur lembut</div><div class="chip dark" id="tx-2">Perisa strawberi</div></div>'
    '<div class="safety" id="tx-n">Bawah 6 tahun: guna sebesar kacang pea, dengan pengawasan dewasa</div>',
)
pop_in("#tx-1", wt("S05", "lembut"))
pop_in("#tx-2", wt("S05", "perisa"))
gfx_js.append(f'tl.fromTo("#tx-n", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, {q(t0 + 0.3)});')
add_sfx("pop", wt("S05", "lembut"), 0.3)
add_sfx("pop", wt("S05", "perisa"), 0.3)
fade_out("#ov-tex .stack", t1)
fade_out("#tx-n", t1)
t0, t1 = card("ov-fun", wt("S05", "menyeronokkan") - 0.1, s5["end"] + 0.1,
              '<div class="stack top"><div class="chip dark" id="fn-1">Gosok gigi jadi seronok!</div></div>')
pop_in("#fn-1", t0)
add_sfx("sparkle", t0, 0.25)
fade_out("#ov-fun .stack", t1)

# CTA.
s6 = SEG["S06"]
t0, t1 = card(
    "ov-name", wt("S06", "dr.ritta") - 0.1, wt("S06", "tekan") - 0.05,
    '<div class="brand" id="nm-card"><div class="brand-k">CHECK OUT</div><div class="brand-lg">Dr.Ritta</div>'
    '<div class="brand-sm">Berry Buddies</div></div>',
)
pop_in("#nm-card", t0, 0.6, "back.out(1.8)")
add_sfx("pop", t0, 0.3)
fade_out("#nm-card", t1)
t_beg = wt("S06", "tekan")
t0, t1 = card("ov-cta", t_beg - 0.1, TOTAL, '<div class="cta" id="ct-btn">Tekan beg kuning</div>')
gfx_js.append(f'tl.fromTo("#ct-btn", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "back.out(1.8)" }}, {t0});')
gfx_js.append(
    f'tl.fromTo("#ct-btn", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.4, ease: "sine.inOut", yoyo: true, '
    f'repeat: {max(1, int((TOTAL - t0 - 0.4) / 0.4) - 1)}, immediateRender: false }}, {q(t0 + 0.35)});'
)
add_sfx("ping", t0, 0.4)

# ── 5. Captions ────────────────────────────────────────────────────────────
cap_dom, cap_js = [], []
cap_id = 0
hook_end = wt("S01", "ada#2")
for s in segs:
    ws = [w for w in s["words"] if not (s["id"] == "S01" and w["s"] < hook_end)]  # hook title carries these
    chunks, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) == 3 or w["text"][-1:] in ",.?!" or len("".join(x["text"] for x in cur)) > 16:
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    k = 0
    while k < len(chunks) and len(chunks) > 1:
        end = chunks[k + 1][0]["s"] if k + 1 < len(chunks) else s["end"]
        if end - chunks[k][0]["s"] < 0.45:
            # A sentence-final scrap joins the line before it, never the next sentence.
            ends = chunks[k][-1]["text"][-1:] in ".?!"
            if k > 0 and (len(chunks[k - 1]) < 4 or ends):
                chunks[k - 1] += chunks.pop(k)
                continue
            if k + 1 < len(chunks):
                chunks[k + 1] = chunks[k] + chunks[k + 1]
                chunks.pop(k)
                continue
        k += 1
    for i, ch in enumerate(chunks):
        c0 = ch[0]["s"] if (i or s["id"] == "S01") else s["start"]
        c1 = chunks[i + 1][0]["s"] if i + 1 < len(chunks) else s["end"]
        if c1 - c0 < 0.1:
            continue
        cap_id += 1
        spans = []
        for j, w in enumerate(ch):
            txt = w["text"].rstrip(",.")
            kw = " kw" if norm(w["text"]) in KEYWORDS else ""
            spans.append(f'<span class="w{kw}" id="c{cap_id}-w{j}">{html.escape(txt)}</span>')
            cap_js.append(f'tl.fromTo("#c{cap_id}-w{j}", {{ scale: 1 }}, {{ scale: 1.04, duration: 0.08, ease: "power2.out", immediateRender: false }}, {w["s"]});')
            cap_js.append(f'tl.to("#c{cap_id}-w{j}", {{ scale: 1, duration: 0.1, ease: "power2.in" }}, {max(w["e"], q(w["s"] + 0.09))});')
        cap_dom.append(
            f'<div id="cap-{cap_id}" class="clip cap" data-start="{q(c0)}" data-duration="{math.floor((c1 - c0) * 1000) / 1000}" data-track-index="3">'
            f'<div class="cap-in" id="cap-{cap_id}-in">{" ".join(spans)}</div></div>'
        )
        cap_js.append(f'tl.fromTo("#cap-{cap_id}-in", {{ scale: 0.9, y: 12 }}, {{ scale: 1, y: 0, duration: 0.14, ease: "back.out(2)" }}, {q(c0)});')

# ── 6. Music bed (HeyGen catalog), carved under the voice ──────────────────
CARVE_PATH = ROOT / "data/bgm-carve.json"
carve_attrs = ""
if CARVE_PATH.exists():
    carve_attrs = "".join(f" {k}='{v}'" for k, v in json.loads(CARVE_PATH.read_text()).items())
if (ROOT / "assets/audio/bgm-bed.m4a").exists():
    sfx.insert(0, f'<audio id="music-bed" class="clip" src="assets/audio/bgm-bed.m4a" data-start="0" data-duration="{TOTAL}" '
                  f'data-track-index="10" data-volume="1"{carve_attrs}></audio>')

# ── 7. Write files ─────────────────────────────────────────────────────────
FONT_FACE = """@font-face { font-family: "Plus Jakarta Sans"; src: url("assets/fonts/PlusJakartaSans-latin.woff2") format("woff2");
  font-weight: 200 800; font-style: normal; font-display: block; }"""

CSS_MAIN = f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #1a0b10; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #1a0b10; font-family: "Montserrat", sans-serif; }}
.frame-wrap {{ position: absolute; inset: 0; overflow: hidden; transform-origin: 50% 35%; }}
.frame-wrap video {{ position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; }}
.frame-wrap video.aroll {{ transform: scaleX(-1); }}
.broll {{ transform-origin: 50% 50%; }}
"""

CSS_VIS = f"""
#vis-root {{ position: absolute; inset: 0; }}
.fs {{ position: absolute; inset: 0; overflow: hidden; background: #1a0b10; }}
.fs-in {{ position: absolute; inset: 0; background: center / cover no-repeat; transform-origin: 50% 45%; }}
.fs-tag {{ position: absolute; left: 36px; top: 160px; font-family: "Montserrat"; font-weight: 700; font-size: 18px; letter-spacing: 1.5px;
  color: {CREAM}; background: rgba(30,10,16,.55); padding: 5px 10px; border-radius: 6px; }}
"""

CSS_GFX = FONT_FACE + f"""
#gfx-root {{ position: absolute; inset: 0; font-family: "Plus Jakarta Sans", sans-serif; }}
.overlay {{ position: absolute; inset: 0; pointer-events: none; }}
.top {{ position: absolute; left: 60px; top: 230px; }}
.hook {{ position: absolute; left: 60px; right: 60px; top: 220px; display: flex; flex-direction: column; align-items: center; text-align: center; gap: 10px;
  background: rgba(40,12,22,.72); padding: 26px 24px 32px; border-radius: 32px; }}
.hook-sm {{ font-weight: 700; font-size: 54px; color: #ffffff; }}
.hook-big {{ font-family: "Archivo Black"; font-size: 76px; white-space: nowrap; line-height: 1; color: {ACCENT}; text-shadow: 0 6px 0 {INK}; transform-origin: 50% 60%; }}
.stack {{ display: flex; flex-direction: column; align-items: flex-start; gap: 14px; }}
.kicker {{ font-weight: 800; font-size: 26px; letter-spacing: 3px; color: {CREAM}; background: rgba(60,16,32,.82); padding: 8px 16px; border-radius: 10px; }}
.chip {{ font-weight: 800; font-size: 48px; color: {INK}; background: {CREAM}; padding: 12px 28px; border-radius: 999px;
  box-shadow: 0 10px 24px rgba(0,0,0,.25); transform-origin: 0% 50%; white-space: nowrap; }}
.chip.dark {{ color: #ffffff; background: {BERRY}; }}
.brand {{ position: absolute; left: 0; right: 0; top: 200px; margin: 0 auto; width: 760px; display: flex; flex-direction: column; align-items: center; gap: 6px;
  background: {CREAM}; padding: 24px 30px 30px; border-radius: 30px; box-shadow: 0 16px 34px rgba(0,0,0,.28); }}
.brand-k {{ font-weight: 800; font-size: 26px; letter-spacing: 4px; color: #8a4a5e; }}
.brand-lg {{ font-family: "Archivo Black"; font-size: 120px; line-height: 1; color: {BERRY}; white-space: nowrap; }}
.brand-sm {{ font-weight: 800; font-size: 44px; color: #ffffff; background: {BERRY}; padding: 8px 26px; border-radius: 999px; white-space: nowrap; }}
.safety {{ position: absolute; left: 60px; right: 60px; top: 1050px; font-weight: 700; font-size: 30px; line-height: 1.3; text-align: center;
  color: {INK}; background: rgba(255,246,248,.92); padding: 12px 22px; border-radius: 16px; }}
.cta {{ position: absolute; left: 60px; bottom: 420px; font-family: "Archivo Black"; font-size: 54px; color: #2a1a05; background: {YELLOW};
  padding: 22px 36px; border-radius: 999px; box-shadow: 0 12px 0 #2a1a05; transform-origin: 0% 50%; }}
"""

CSS_CAP = FONT_FACE + f"""
#cap-root {{ position: absolute; inset: 0; font-family: "Plus Jakarta Sans", sans-serif; }}
.cap {{ position: absolute; left: 60px; right: 140px; top: 1210px; height: 200px; display: flex; align-items: center; justify-content: center; }}
.cap-in {{ display: flex; flex-wrap: wrap; justify-content: center; text-align: center; max-width: 820px;
  padding: 10px 22px 12px; border-radius: 20px; background: rgba(30,8,16,.55);
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
(ROOT / "compositions/visuals.html").write_text(subcomp("visuals", "vis-root", CSS_VIS, vis_dom, vis_js))
(ROOT / "compositions/graphics.html").write_text(subcomp("graphics", "gfx-root", CSS_GFX, gfx_dom, gfx_js))
(ROOT / "compositions/captions.html").write_text(subcomp("captions", "cap-root", CSS_CAP, cap_dom, cap_js))

hosts = [
    f'<div id="visuals" data-composition-id="visuals" data-composition-src="compositions/visuals.html" '
    f'data-start="0" data-duration="{TOTAL}" data-track-index="4" data-width="{W}" data-height="{H}"></div>',
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
    <title>Dr.Ritta Berry Buddies — review</title>
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

out = [f"TOTAL {TOTAL:.2f}s  ({len(segs)} A-roll segments, {len(EDL['broll'])} B-roll shots, {len(EDL['photos'])} photos, "
       f"{len(sfx)} audio fx, {cap_id} caption cards)", ""]
for s in segs:
    out.append(f"{s['start']:6.2f}-{s['end']:6.2f}  {s['id']}  src {s['in']:6.2f}-{s['out']:6.2f}  ({len(s['pieces'])} pc)  {s['text']}")
out.append("")
for t0, t1 in cover:
    out.append(f"  cutaway {t0:6.2f}-{t1:6.2f}")
(ROOT / "data/cutlist.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))
