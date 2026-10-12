#!/usr/bin/env python3
"""Build index.html + compositions/ for the Jus Gout edit from data/edl.json.

Run from the project root:  python3 tools/build.py
Edit data/edl.json (cuts, B-roll picks) and re-run; never hand-edit index.html.
"""
import array
import json
import math
import re
import subprocess
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EDL = json.loads((ROOT / "data/edl.json").read_text())
FPS = EDL["fps"]
W, H = EDL["width"], EDL["height"]
KEYWORDS = {k.lower() for k in EDL["keywords"]}

YELLOW = "#FFC61A"


def q(t):
    """Quantize to the frame grid."""
    return round(round(t * FPS) / FPS, 4)


def fr(n):
    return round(n / FPS, 4)


def fr_dur(n):
    """Duration of n frames, floored to 3 dp so start + dur never passes the next start."""
    return math.floor(n / FPS * 1000) / 1000


# ── 1. Lay the kept A-roll segments end to end ─────────────────────────────
# Speech envelope of the A-roll (10 ms RMS), cached next to the EDL.
RMS_PATH = ROOT / "data/v1-rms.json"
if not RMS_PATH.exists():
    pcm = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(ROOT / "assets/v1.mp4"), "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
        check=True, capture_output=True,
    ).stdout
    a = array.array("h", pcm)
    rms = []
    for i in range(0, len(a) - 160, 160):
        blk = a[i : i + 160]
        rms.append(round(10 * math.log10(sum(x * x for x in blk) / 160 / 32768**2 + 1e-12), 1))
    RMS_PATH.write_text(json.dumps(rms))
RMS = json.loads(RMS_PATH.read_text())


def speech_islands(t0, t1, thr=-45, min_gap=0.12):
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
    return max(1, len(re.findall(r"[aeiou]+", word.lower())))


def time_words(text, t_in, t_out):
    """Spread words over the detected speech by syllable count (Malay is syllable-timed)."""
    words = text.split()
    isl = speech_islands(t_in, t_out)
    speech = sum(b - a for a, b in isl)
    syl = [syllables(w) for w in words]
    total = sum(syl)

    def at(frac):  # fraction of speech time -> source time
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


segs = []
cursor_f = 0
for s in EDL["segments"]:
    dur_f = round((s["out"] - s["in"]) * FPS)
    seg = dict(s, start=fr(cursor_f), dur=fr_dur(dur_f), end=fr(cursor_f + dur_f))
    ws = []
    for text, a, b in time_words(s["text"], s["in"], s["out"]):
        ws.append({"text": text, "s": q(seg["start"] + a - s["in"]), "e": q(seg["start"] + b - s["in"])})
    seg["words"] = ws
    segs.append(seg)
    cursor_f += dur_f
TOTAL = fr(cursor_f)
SEG = {s["id"]: s for s in segs}


def word_time(seg_id, word, which="s"):
    for w in SEG[seg_id]["words"]:
        if w["text"].lower().strip(".,?!") == word.lower().strip(".,?!"):
            return w[which]
    raise KeyError(f"{word!r} not in {seg_id}: {[w['text'] for w in SEG[seg_id]['words']]}")


def anchor(seg_id, a):
    if a == "start":
        return SEG[seg_id]["start"]
    if a == "end":
        return SEG[seg_id]["end"]
    return word_time(seg_id, a)


# ── 2. Build DOM + timeline pieces ─────────────────────────────────────────
dom, js, sfx = [], [], []
sfx_n = [0]


def add_sfx(name, t, vol, dur=None):
    lengths = {"whoosh-short": 0.57, "pop": 0.72, "impact-bass-1": 2.1, "chime": 2.5,
               "sparkle": 1.8, "ping": 1.3, "click-soft": 0.36, "whoosh": 0.57}
    d = dur or lengths[name]
    t = q(t)
    d = min(d, TOTAL - t)
    sfx_n[0] += 1
    sfx.append(
        f'<audio id="sfx-{sfx_n[0]:02d}-{name}" class="clip" src="assets/sfx/{name}.mp3" '
        f'data-start="{t}" data-duration="{q(d)}" data-track-index="{20 + sfx_n[0]}" data-volume="{vol}"></audio>'
    )


# A-roll: one <video> per kept segment, inside an untimed wrapper we can zoom.
for s in segs:
    dom.append(
        f'<div class="frame-wrap" id="wrap-{s["id"]}">'
        f'<video id="a-{s["id"]}" class="clip aroll" src="assets/v1.mp4" playsinline data-has-audio="true" '
        f'data-start="{s["start"]}" data-duration="{s["dur"]}" data-media-start="{s["in"]}" data-track-index="0"></video>'
        f"</div>"
    )
    js.append(f'tl.set("#wrap-{s["id"]}", {{ scale: {s["zoom"]} }}, 0);')

# Punch-ins on the emotional beats (jump-cut emphasis).
for seg_id, word, amount in [("S01", "gout?", 1.16), ("S04", "terseksa", 1.14), ("S11", "rekomen", 1.1)]:
    z = SEG[seg_id]["zoom"]
    t = word_time(seg_id, word)
    js.append(
        f'tl.fromTo("#wrap-{seg_id}", {{ scale: {z} }}, {{ scale: {round(z * amount, 3)}, duration: 0.22, ease: "power3.out", immediateRender: false }}, {t});'
    )

# B-roll overlays from video 2 (muted), with a whoosh-in and slow push.
for b in EDL["broll"]:
    t0 = q(anchor(b["seg"], b["from"]) - (0.05 if b["from"] != "start" else 0))
    t1 = anchor(b["seg"], b["to"])
    d = q(t1 - t0)
    dom.append(
        f'<div class="frame-wrap broll" id="bwrap-{b["id"]}">'
        f'<video id="b-{b["id"]}" class="clip" src="assets/v2.mp4" muted playsinline '
        f'data-start="{t0}" data-duration="{d}" data-media-start="{b["src"]}" data-track-index="1"></video>'
        f"</div>"
    )
    js.append(
        f'tl.fromTo("#bwrap-{b["id"]}", {{ scale: 1.2 }}, {{ scale: 1.02, duration: 0.32, ease: "power3.out" }}, {t0});'
    )
    js.append(
        f'tl.fromTo("#bwrap-{b["id"]}", {{ scale: 1.02 }}, {{ scale: 1.08, duration: {max(0.1, round(d - 0.32, 3))}, ease: "none", immediateRender: false }}, {q(t0 + 0.32)});'
    )
    add_sfx("whoosh-short", t0 - 0.08, 0.35)

main_dom, main_js = dom, js
dom, js = [], []  # graphics sub-composition from here


def overlay(oid, t0, t1, inner, track=2):
    t0, t1 = q(t0), q(min(t1, TOTAL))
    dom.append(
        f'<div id="{oid}" class="clip overlay" data-start="{t0}" data-duration="{q(t1 - t0)}" data-track-index="{track}">{inner}</div>'
    )
    return t0, t1


# HOOK — kinetic question synced to the words, GOUT? slams in.
s1 = SEG["S01"]
hook_inner = (
    '<div class="hook">'
    '<div class="hook-line" id="hk-1">SIAPA DEKAT SINI</div>'
    '<div class="hook-line" id="hk-2">YANG ADA</div>'
    '<div class="hook-big" id="hk-3">GOUT?</div>'
    "</div>"
)
h0, h1 = overlay("ov-hook", 0, s1["end"] + 0.5, hook_inner)
js += [
    f'tl.fromTo("#hk-1", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.18, ease: "power3.out" }}, {h0});',
    f'tl.fromTo("#hk-2", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.18, ease: "power3.out" }}, {word_time("S01", "yang")});',
    f'tl.fromTo("#hk-3", {{ opacity: 0, scale: 2.4, rotation: -10 }}, {{ opacity: 1, scale: 1, rotation: -4, duration: 0.28, ease: "back.out(2.2)" }}, {word_time("S01", "gout?")});',
    f'tl.to("#ov-hook .hook", {{ opacity: 0, y: -60, duration: 0.25, ease: "power2.in" }}, {q(h1 - 0.25)});',
]
add_sfx("whoosh-short", 0, 0.4)
add_sfx("impact-bass-1", word_time("S01", "gout?") - 0.02, 0.55)

# S03 — credibility tag.
s3 = SEG["S03"]
t0, t1 = overlay(
    "ov-cred", s3["start"] + 0.1, s3["end"] + 1.2,
    '<div class="tag top"><div class="tag-kicker" id="cr-k">PENGALAMAN SENDIRI</div>'
    '<div class="tag-main" id="cr-m">BERTAHUN-TAHUN<br/>HIDAP GOUT</div></div>',
)
js += [
    f'tl.fromTo("#cr-k", {{ opacity: 0, x: -60 }}, {{ opacity: 1, x: 0, duration: 0.25, ease: "power3.out" }}, {t0});',
    f'tl.fromTo("#cr-m", {{ opacity: 0, x: -80 }}, {{ opacity: 1, x: 0, duration: 0.3, ease: "power3.out" }}, {q(t0 + 0.08)});',
    f'tl.to("#ov-cred .tag", {{ opacity: 0, duration: 0.2 }}, {q(t1 - 0.2)});',
]
add_sfx("pop", t0, 0.45)

# S04 — pain flash on "terseksa".
t_pain = word_time("S04", "terseksa")
t0, t1 = overlay("ov-pain", t_pain, SEG["S04"]["end"], '<div class="pain-vignette" id="pain-v"></div>')
js += [
    f'tl.fromTo("#pain-v", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.15 }}, {t0});',
    f'tl.to("#pain-v", {{ opacity: 0.35, duration: 0.6, ease: "power2.out" }}, {q(t0 + 0.15)});',
]
add_sfx("impact-bass-1", t_pain - 0.02, 0.32)

# S06 — responsible note.
t_doc = word_time("S06", "rawatan")
t0, t1 = overlay(
    "ov-doc", t_doc, SEG["S06"]["end"] + 0.4,
    '<div class="note top" id="doc-card"><svg class="note-ico" viewBox="0 0 48 48"><rect x="18" y="4" width="12" height="40" rx="3"/>'
    '<rect x="4" y="18" width="40" height="12" rx="3"/></svg>'
    '<div class="note-txt">RAWATAN &amp; UBAT DOKTOR<br/>TETAP PENTING</div></div>',
)
js += [
    f'tl.fromTo("#doc-card", {{ opacity: 0, y: -40, scale: 0.9 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.3, ease: "back.out(1.8)" }}, {t0});',
    f'tl.to("#doc-card", {{ opacity: 0, duration: 0.2 }}, {q(t1 - 0.2)});',
]
add_sfx("click-soft", t0, 0.5)

# S07 — product name reveal over the front-label B-roll.
t_jus = word_time("S07", "jus")
t0, t1 = overlay(
    "ov-prod", t_jus, SEG["S07"]["end"],
    '<div class="prod top"><div class="prod-kicker" id="pd-k">PRODUK YANG SAYA JUMPA</div>'
    '<div class="prod-name" id="pd-n">JUS GOUT</div></div>',
)
js += [
    f'tl.fromTo("#pd-k", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.2, ease: "power3.out" }}, {t0});',
    f'tl.fromTo("#pd-n", {{ opacity: 0, scale: 0.5 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }}, {q(t0 + 0.06)});',
]
add_sfx("pop", t0, 0.5)

# S08 — ingredient chips.
t0, t1 = overlay(
    "ov-ingr", SEG["S08"]["start"] + 0.1, SEG["S08"]["end"],
    '<div class="ingr top"><div class="ingr-head" id="in-h">BAHAN DALAMNYA</div>'
    '<div class="chip" id="in-1"><img class="chip-ico" src="assets/visuals/pineapple.png" alt="" />BROMELAIN</div>'
    '<div class="chip" id="in-2"><img class="chip-ico" src="assets/visuals/herb.png" alt="" />MILK THISTLE</div></div>',
)
t_b, t_m = word_time("S08", "bromelain"), word_time("S08", "milk")
js += [
    f'tl.fromTo("#in-h", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.2, ease: "power3.out" }}, {t0});',
    f'tl.fromTo("#in-1", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.28, ease: "back.out(2.4)" }}, {t_b});',
    f'tl.fromTo("#in-2", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.28, ease: "back.out(2.4)" }}, {t_m});',
]
add_sfx("pop", t_b, 0.5)
add_sfx("pop", t_m, 0.5)

# S09 — "semak dulu" check chip.
t_semak = word_time("S09", "semak")
t0, t1 = overlay(
    "ov-semak", t_semak, SEG["S09"]["end"] + 0.2,
    '<div class="chip check top-chip" id="sm-c"><svg viewBox="0 0 48 48" class="chk"><path d="M8 25 L20 37 L40 11"/></svg>SEMAK DULU</div>',
)
js.append(f'tl.fromTo("#sm-c", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: 0.28, ease: "back.out(2.4)" }}, {t0});')
add_sfx("pop", t0, 0.45)

# S11 — "beg kuning" basket.
t_beg = word_time("S11", "beg")
t0, t1 = overlay(
    "ov-beg", t_beg, SEG["S11"]["end"] + 0.1,
    '<div class="beg" id="bg-c"><svg viewBox="0 0 64 64" class="basket"><path d="M10 24 H54 L49 52 H15 Z"/>'
    '<path class="handle" d="M22 24 L30 10 M42 24 L34 10"/></svg><div class="beg-txt">BEG KUNING</div></div>',
)
js.append(f'tl.fromTo("#bg-c", {{ opacity: 0, y: 80, scale: 0.6 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.35, ease: "back.out(2)" }}, {t0});')
add_sfx("chime", t0, 0.3)

# S12 — promo badge.
t_promo = word_time("S12", "promosi")
t0, t1 = overlay(
    "ov-promo", t_promo - 0.1, SEG["S13"]["end"],
    '<div class="promo" id="pr-b"><div class="promo-burst" id="pr-burst"></div><div class="promo-txt">HARGA<br/>PROMO</div></div>',
)
js += [
    f'tl.fromTo("#pr-b", {{ opacity: 0, scale: 0.3, rotation: -30 }}, {{ opacity: 1, scale: 1, rotation: 8, duration: 0.35, ease: "back.out(2.2)" }}, {t0});',
    f'tl.fromTo("#pr-burst", {{ rotation: 0 }}, {{ rotation: 90, duration: {q(t1 - t0)}, ease: "none" }}, {t0});',
]
add_sfx("sparkle", t0, 0.4)

# S13 → end — CTA button pointing at the yellow basket (bottom-left in TikTok).
t_check = word_time("S13", "check")
t0, t1 = overlay(
    "ov-cta", t_check - 0.1, TOTAL,
    '<div class="cta" id="cta-b"><svg viewBox="0 0 48 48" class="cta-arrow"><path d="M38 10 L12 36 M12 16 V36 H32"/></svg>'
    '<span>CHECK OUT SEKARANG</span></div>',
)
js += [
    f'tl.fromTo("#cta-b", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "back.out(1.8)" }}, {t0});',
    f'tl.fromTo("#cta-b", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.4, ease: "sine.inOut", yoyo: true, repeat: {max(1, int((t1 - t0 - 0.3) / 0.4) - 1)}, immediateRender: false }}, {q(t0 + 0.3)});',
]
add_sfx("ping", t0, 0.45)

gfx_dom, gfx_js = dom, js
dom, js = [], []  # visuals sub-composition from here

# ── 2b. Illustrated stickers (Fluent Emoji 3D, MIT) ─────────────────────────
# Placed only in the zones the speaker never occupies: the wall band above his
# head (y 200–650) and the kitchen counter to his left (x 40–440, y 700–1100).
LEFT = (70, 760)
TOP_R = (740, 250)


def sticker(sid, img, t0, t1, xy, size, rot=0, pop=True, float_amp=10, z=1):
    t0, t1 = q(t0), q(min(t1, TOTAL))
    x, y = xy
    dom.append(
        f'<div id="st-{sid}" class="clip st" data-start="{t0}" data-duration="{q(t1 - t0)}" data-track-index="4" '
        f'style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;z-index:{z}">'
        f'<div class="st-in" id="st-{sid}-in"><div class="st-img" style="background-image:url(assets/visuals/{img}.png)"></div></div></div>'
    )
    sel = f"#st-{sid}-in"
    js.append(f'tl.fromTo("{sel}", {{ scale: 0, rotation: {rot - 25} }}, {{ scale: 1, rotation: {rot}, duration: 0.34, ease: "back.out(2.2)" }}, {t0});')
    hold = t1 - t0 - 0.55
    if float_amp and hold > 0.5:
        reps = max(1, int(hold / 0.6) - 1)
        js.append(f'tl.fromTo("{sel}", {{ y: 0 }}, {{ y: -{float_amp}, duration: 0.6, ease: "sine.inOut", yoyo: true, repeat: {reps}, immediateRender: false }}, {q(t0 + 0.34)});')
    js.append(f'tl.to("{sel}", {{ scale: 0, duration: 0.18, ease: "power2.in" }}, {q(t1 - 0.18)});')
    if pop:
        add_sfx("pop", t0, 0.3)
    return t0, t1


# S01–S02: gout strikes the big toe.
t_g = word_time("S01", "gout?")
sticker("foot", "foot", t_g - 0.05, word_time("S02", "korang") + 0.9, LEFT, 300, rot=-6, pop=False)
sticker("foot-hit", "collision", t_g + 0.05, word_time("S02", "korang") + 0.9, (LEFT[0] - 30, LEFT[1] + 110), 150, rot=10, pop=False, float_amp=0)
js.append(f'tl.fromTo("#st-foot-hit-in", {{ scale: 1 }}, {{ scale: 1.25, duration: 0.25, ease: "sine.inOut", yoyo: true, repeat: 3, immediateRender: false }}, {q(t_g + 0.45)});')

t_sak = word_time("S02", "sakitnya")
sticker("face-pain", "persevering", t_sak - 0.05, SEG["S02"]["end"] + 0.1, TOP_R, 290, rot=4)
sticker("sweat-1", "sweat", t_sak + 0.15, SEG["S02"]["end"] + 0.1, (TOP_R[0] + 210, TOP_R[1] - 40), 120, rot=-10, pop=False)

t_men = word_time("S02", "menyerang.")
sticker("bolt", "voltage", t_men - 0.05, SEG["S03"]["start"] + 0.5, (LEFT[0] + 200, LEFT[1] - 30), 170, rot=12, pop=False, float_amp=0)
t0, t1 = q(t_men - 0.05), q(SEG["S03"]["start"] + 0.5)
dom.append(
    f'<div id="st-aduh" class="clip st" data-start="{t0}" data-duration="{q(t1 - t0)}" data-track-index="4" '
    f'style="left:{LEFT[0]}px;top:{LEFT[1] + 40}px;width:330px;height:220px">'
    f'<div class="st-in aduh" id="st-aduh-in"><span>ADUHH!</span></div></div>'
)
js.append(f'tl.fromTo("#st-aduh-in", {{ scale: 0, rotation: -18 }}, {{ scale: 1, rotation: -6, duration: 0.3, ease: "back.out(2.6)" }}, {t0});')
js.append(f'tl.fromTo("#st-aduh-in", {{ x: -6 }}, {{ x: 6, duration: 0.05, ease: "none", yoyo: true, repeat: 7, immediateRender: false }}, {q(t0 + 0.3)});')
add_sfx("impact-bass-1", t0, 0.3)

# S03: years of it.
sticker("calendar", "calendar", word_time("S03", "bertahun-tahun") - 0.1, SEG["S03"]["end"], TOP_R, 270, rot=6)

# S04: pain meter climbs to 10, faces get worse.
s4 = SEG["S04"]
t0, t1 = q(s4["start"] + 0.15), q(s4["end"])
dom.append(
    f'<div id="pm" class="clip pm" data-start="{t0}" data-duration="{q(t1 - t0)}" data-track-index="4">'
    '<div class="pm-in" id="pm-in">'
    '<div class="pm-title">TAHAP SAKIT</div>'
    '<div class="pm-num"><span id="pm-num">0</span><small>/10</small></div>'
    '<div class="pm-track"><div class="pm-fill" id="pm-fill"></div></div>'
    "</div></div>"
)
t_sakit, t_teruk = word_time("S04", "sakit"), word_time("S04", "teruk,")
js += [
    f'tl.fromTo("#pm-in", {{ opacity: 0, x: 80 }}, {{ opacity: 1, x: 0, duration: 0.3, ease: "power3.out" }}, {t0});',
    f'tl.fromTo("#pm-fill", {{ scaleY: 0.04 }}, {{ scaleY: 1, duration: {q(t_teruk + 0.3 - t_sakit)}, ease: "power2.in" }}, {t_sakit});',
    f'(function () {{ const o = {{ v: 0 }}; tl.to(o, {{ v: 10, duration: {q(t_teruk + 0.3 - t_sakit)}, ease: "power2.in", '
    f'onUpdate: function () {{ const el = document.getElementById("pm-num"); if (el) el.textContent = String(Math.round(o.v)); }} }}, {t_sakit}); }})();',
    f'tl.fromTo("#pm-in", {{ rotation: -2 }}, {{ rotation: 2, duration: 0.06, ease: "none", yoyo: true, repeat: 9, immediateRender: false }}, {q(t_teruk + 0.3)});',
    f'tl.to("#pm-in", {{ opacity: 0, x: 80, duration: 0.2, ease: "power2.in" }}, {q(t1 - 0.2)});',
]
add_sfx("click-soft", t0, 0.35)
add_sfx("impact-bass-1", t_teruk + 0.28, 0.25)
t_samp, t_ters = word_time("S04", "sampai"), word_time("S04", "terseksa")
sticker("face-bandage", "bandage", t_samp - 0.05, t_ters - 0.02, LEFT, 300, rot=-5)
sticker("face-tired", "tired", t_ters - 0.02, s4["end"] + 0.05, LEFT, 320, rot=5, pop=False)
sticker("sweat-2", "sweat", t_ters + 0.1, s4["end"] + 0.05, (LEFT[0] + 230, LEFT[1] - 50), 130, rot=-8, pop=False)

# S05: "cari macam-macam cara untuk jaga kesihatan".
t_cari, t_mac = word_time("S05", "cari"), word_time("S05", "macam-macam")
sticker("search", "magnifier", t_cari - 0.1, t_mac + 0.25, (400, 260), 250, rot=-8, float_amp=0)
js.append(f'tl.fromTo("#st-search", {{ x: -300 }}, {{ x: 260, duration: {q(t_mac + 0.25 - t_cari)}, ease: "sine.inOut", immediateRender: false }}, {q(t_cari - 0.1)});')
for i, (img, x) in enumerate([("herb", 70), ("droplet", 310), ("leafy", 550), ("pill", 790)]):
    sticker(f"way-{i}", img, t_mac + 0.3 + i * 0.22, SEG["S05"]["end"] + 0.05, (x, 300 + (i % 2) * 70), 210, rot=(-8, 6, -4, 10)[i], pop=i == 0)

# S06: doctor's treatment still matters.
sticker("pill-doc", "pill", word_time("S06", "ubat") - 0.05, SEG["S06"]["end"], (LEFT[0] + 190, LEFT[1] + 140), 180, rot=-20, pop=False)
sticker("steth", "stethoscope", word_time("S06", "doktor") - 0.05, SEG["S06"]["end"], LEFT, 270, rot=4)

# S07: the product reveal.
sticker("spark-1", "sparkles", word_time("S07", "produk") - 0.05, word_time("S07", "namanya") + 0.05, TOP_R, 230, rot=0)

# S10: ikhtiar.
t_ik = word_time("S10", "ikhtiar")
sticker("doa", "folded", t_ik - 0.1, SEG["S10"]["end"], LEFT, 290, rot=-4)
sticker("cup", "cup", word_time("S10", "cara") - 0.05, SEG["S10"]["end"], TOP_R, 260, rot=6)

# S11: "saya sangat rekomen".
t_rek = word_time("S11", "rekomen,")
sticker("thumb", "thumbsup", t_rek - 0.1, word_time("S11", "anda") + 0.1, LEFT, 310, rot=-8)
sticker("spark-2", "sparkles", t_rek, word_time("S11", "anda") + 0.1, TOP_R, 230, rot=0, pop=False)

# S14: enjoy.
sticker("spark-3", "sparkles", SEG["S14"]["start"] + 0.1, TOTAL, (780, 560), 220, rot=0, pop=False)

vis_dom, vis_js = dom, js
dom, js = [], []  # captions sub-composition from here

# ── 3. Captions: 1–3 word chunks, active word highlighted ───────────────────
cap_id = 0
for s in segs:
    if s["id"] == "S01":  # the hook title carries these words
        continue
    ws = s["words"]
    chunks, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) == 3 or w["text"][-1:] in ",.?!" or len("".join(x["text"] for x in cur)) > 15:
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    # Fold flash-length chunks (< 0.45 s on screen) into a neighbour.
    k = 0
    while k < len(chunks) and len(chunks) > 1:
        ch = chunks[k]
        end = chunks[k + 1][0]["s"] if k + 1 < len(chunks) else s["end"]
        if end - ch[0]["s"] < 0.45:
            if k > 0 and len(chunks[k - 1]) < 4:
                chunks[k - 1] += chunks.pop(k)
                continue
            if k + 1 < len(chunks):
                chunks[k + 1] = ch + chunks[k + 1]
                chunks.pop(k)
                continue
        k += 1
    for i, ch in enumerate(chunks):
        c0 = s["start"] if i == 0 else ch[0]["s"]
        c1 = chunks[i + 1][0]["s"] if i + 1 < len(chunks) else s["end"]
        if c1 - c0 < 0.1:
            continue
        cap_id += 1
        spans = []
        for j, w in enumerate(ch):
            txt = w["text"].strip(",.").upper().replace("...", "")
            kw = " kw" if w["text"].lower().strip(".,?!") in KEYWORDS or w["text"].lower() in KEYWORDS else ""
            spans.append(f'<span class="w{kw}" id="c{cap_id}-w{j}">{html.escape(txt)}</span>')
            js.append(f'tl.fromTo("#c{cap_id}-w{j}", {{ scale: 1 }}, {{ scale: 1.08, duration: 0.08, ease: "power2.out", immediateRender: false }}, {w["s"]});')
            js.append(f'tl.to("#c{cap_id}-w{j}", {{ scale: 1, duration: 0.1, ease: "power2.in" }}, {max(w["e"], q(w["s"] + 0.09))});')
        dom.append(
            f'<div id="cap-{cap_id}" class="clip cap" data-start="{q(c0)}" data-duration="{math.floor((c1 - c0) * 1000) / 1000}" data-track-index="3">'
            f'<div class="cap-in" id="cap-{cap_id}-in">{" ".join(spans)}</div></div>'
        )
        js.append(f'tl.fromTo("#cap-{cap_id}-in", {{ scale: 0.82, y: 18 }}, {{ scale: 1, y: 0, duration: 0.14, ease: "back.out(2)" }}, {q(c0)});')

cap_dom, cap_js = dom, js

# ── 4. Write index.html + the two sub-compositions ─────────────────────────
CSS = f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #0d0a05; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #0d0a05;
  font-family: "Montserrat", "Archivo Black", sans-serif; }}
.frame-wrap {{ position: absolute; inset: 0; overflow: hidden; transform-origin: 50% 30%; }}
.frame-wrap video {{ position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; }}
.frame-wrap video.aroll {{ transform: scaleX(-1); }}
.broll {{ transform-origin: 50% 45%; }}
/*SPLIT-GFX*/
#gfx-root {{ position: absolute; inset: 0; font-family: "Montserrat", "Archivo Black", sans-serif; }}
.overlay {{ position: absolute; inset: 0; pointer-events: none; }}

/* hook */
.hook {{ position: absolute; left: 70px; right: 130px; top: 240px; display: flex; flex-direction: column; align-items: flex-start; gap: 6px; }}
.hook-line {{ font-family: "Montserrat"; font-weight: 900; font-size: 74px; line-height: 1; color: #fff8e6;
  text-shadow: 0 6px 0 #1b1205, 0 0 24px rgba(0,0,0,.55); letter-spacing: -1px; }}
.hook-big {{ font-family: "Archivo Black"; font-size: 196px; line-height: .95; margin-top: 18px; color: {YELLOW};
  text-shadow: 0 10px 0 #1b1205, 0 0 40px rgba(0,0,0,.5); transform-origin: 20% 60%; }}

/* credibility tag */
.top {{ position: absolute; left: 60px; top: 230px; }}
.tag {{ display: flex; flex-direction: column; align-items: flex-start; gap: 10px; }}
.tag-kicker {{ font-weight: 900; font-size: 30px; letter-spacing: 3px; color: #1b1205; background: {YELLOW}; padding: 10px 18px; border-radius: 10px; }}
.tag-main {{ font-weight: 900; font-size: 64px; line-height: 1.02; color: #fff8e6; background: rgba(20,14,4,.82); padding: 18px 24px; border-radius: 16px; }}

/* pain */
.pain-vignette {{ position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 40%, rgba(0,0,0,0) 45%, rgba(170,20,10,.55) 100%); }}

/* doctor note */
.note {{ display: flex; align-items: center; gap: 22px; background: #fff8e6; padding: 22px 30px; border-radius: 22px; box-shadow: 0 14px 40px rgba(0,0,0,.35); }}
.note-ico {{ width: 72px; height: 72px; fill: #d62828; flex: none; }}
.note-txt {{ font-weight: 900; font-size: 44px; line-height: 1.08; color: #1b1205; }}

/* product */
.prod {{ display: flex; flex-direction: column; align-items: flex-start; gap: 8px; }}
.prod-kicker {{ font-weight: 900; font-size: 30px; letter-spacing: 3px; color: #fff8e6; background: rgba(20,14,4,.82); padding: 10px 18px; border-radius: 10px; }}
.prod-name {{ font-family: "Archivo Black"; font-size: 150px; line-height: 1; color: {YELLOW}; text-shadow: 0 8px 0 #1b1205; transform-origin: 0% 50%; }}

/* ingredients */
.ingr {{ display: flex; flex-direction: column; align-items: flex-start; gap: 16px; }}
.ingr-head {{ font-weight: 900; font-size: 30px; letter-spacing: 3px; color: #fff8e6; background: rgba(20,14,4,.82); padding: 10px 18px; border-radius: 10px; }}
.chip {{ font-weight: 900; font-size: 60px; color: #1b1205; background: {YELLOW}; padding: 14px 30px; border-radius: 999px;
  box-shadow: 0 10px 0 #1b1205; transform-origin: 0% 50%; display: flex; align-items: center; gap: 14px; }}
.top-chip {{ position: absolute; left: 60px; top: 260px; }}
.chk {{ width: 56px; height: 56px; fill: none; stroke: #1b1205; stroke-width: 7; stroke-linecap: round; stroke-linejoin: round; }}

/* beg kuning */
.beg {{ position: absolute; left: 60px; top: 230px; display: flex; align-items: center; gap: 18px; background: {YELLOW};
  padding: 18px 32px 18px 22px; border-radius: 24px; box-shadow: 0 12px 0 #1b1205; transform-origin: 0% 50%; }}
.basket {{ width: 96px; height: 96px; fill: #1b1205; stroke: #1b1205; stroke-width: 5; stroke-linecap: round; }}
.basket .handle {{ fill: none; }}
.beg-txt {{ font-family: "Archivo Black"; font-size: 72px; color: #1b1205; line-height: 1; }}

/* promo */
.promo {{ position: absolute; right: 150px; top: 420px; width: 300px; height: 300px; }}
.promo-burst {{ position: absolute; inset: 0; background: #d62828;
  clip-path: polygon(50% 0%, 61% 18%, 82% 10%, 80% 32%, 100% 40%, 85% 56%, 96% 76%, 74% 78%, 68% 100%, 50% 86%, 32% 100%, 26% 78%, 4% 76%, 15% 56%, 0% 40%, 20% 32%, 18% 10%, 39% 18%); }}
.promo-txt {{ position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; text-align: center;
  font-family: "Archivo Black"; font-size: 56px; line-height: 1; color: #fff8e6; }}

/* CTA */
.cta {{ position: absolute; left: 60px; bottom: 420px; display: flex; align-items: center; gap: 18px; background: {YELLOW};
  padding: 22px 34px 22px 24px; border-radius: 999px; box-shadow: 0 12px 0 #1b1205; transform-origin: 0% 50%; }}
.cta span {{ font-family: "Archivo Black"; font-size: 54px; color: #1b1205; line-height: 1; }}
.cta-arrow {{ width: 64px; height: 64px; fill: none; stroke: #1b1205; stroke-width: 7; stroke-linecap: round; stroke-linejoin: round; }}

.chip-ico {{ width: 78px; height: 78px; margin: -10px 0 -10px -12px; }}

/*SPLIT-VIS*/
#vis-root {{ position: absolute; inset: 0; font-family: "Archivo Black", "Montserrat", sans-serif; }}
.st {{ position: absolute; }}
.st-in {{ width: 100%; height: 100%; transform-origin: 50% 60%; }}
.st-img {{ width: 100%; height: 100%; background: center / contain no-repeat;
  filter: drop-shadow(4px 0 0 #fff) drop-shadow(-4px 0 0 #fff) drop-shadow(0 4px 0 #fff) drop-shadow(0 -4px 0 #fff) drop-shadow(0 14px 18px rgba(0,0,0,.35)); }}
.aduh {{ display: flex; align-items: center; justify-content: center; background: #fff8e6; border: 6px solid #1b1205; border-radius: 48% 52% 46% 54%;
  box-shadow: 0 10px 0 #1b1205; }}
.aduh span {{ font-family: "Archivo Black"; font-size: 72px; color: #d62828; line-height: 1; }}
.pm {{ position: absolute; left: 790px; top: 230px; width: 240px; height: 460px; }}
.pm-in {{ width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 18px 16px 20px;
  background: rgba(20,14,4,.84); border-radius: 26px; box-shadow: 0 14px 30px rgba(0,0,0,.35); }}
.pm-title {{ font-family: "Montserrat"; font-weight: 900; font-size: 26px; letter-spacing: 2px; color: #fff8e6; text-align: center; }}
.pm-num {{ font-family: "Archivo Black"; font-size: 76px; line-height: 1; color: #ff5a3c; }}
.pm-num small {{ font-size: 32px; color: #fff8e6; }}
.pm-track {{ position: relative; flex: 1; width: 74px; border-radius: 40px; background: rgba(255,248,230,.18); overflow: hidden; border: 4px solid #fff8e6; }}
.pm-fill {{ position: absolute; left: 0; right: 0; bottom: 0; height: 100%; transform-origin: 50% 100%;
  background: linear-gradient(to top, #2f9e44 0%, #ffc61a 50%, #e03131 100%); }}

/*SPLIT-CAP*/
#cap-root {{ position: absolute; inset: 0; font-family: "Montserrat", sans-serif; }}
.cap {{ position: absolute; left: 50px; right: 130px; top: 1150px; height: 260px; display: flex; align-items: center; justify-content: center; }}
.cap-in {{ display: flex; flex-wrap: wrap; justify-content: center; text-align: center; font-family: "Montserrat"; font-weight: 900; font-size: 78px; line-height: 1.08; color: #ffffff; letter-spacing: -1px;
  text-shadow: 0 5px 0 #000, 3px 0 0 #000, -3px 0 0 #000, 0 -3px 0 #000, 0 0 22px rgba(0,0,0,.6); }}
.cap .w {{ display: inline-block; margin: 0 17px; transform-origin: 50% 70%; }}
.cap .w.kw {{ color: {YELLOW}; }}
"""

CSS_MAIN, rest = CSS.split("/*SPLIT-GFX*/")
CSS_GFX, rest = rest.split("/*SPLIT-VIS*/")
CSS_VIS, CSS_CAP = rest.split("/*SPLIT-CAP*/")


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
(ROOT / "compositions/visuals.html").write_text(subcomp("visuals", "vis-root", CSS_VIS, vis_dom, vis_js))
(ROOT / "compositions/captions.html").write_text(subcomp("captions", "cap-root", CSS_CAP, cap_dom, cap_js))

hosts = [
    f'<div id="graphics" data-composition-id="graphics" data-composition-src="compositions/graphics.html" '
    f'data-start="0" data-duration="{TOTAL}" data-track-index="2" data-width="{W}" data-height="{H}"></div>',
    f'<div id="visuals" data-composition-id="visuals" data-composition-src="compositions/visuals.html" '
    f'data-start="0" data-duration="{TOTAL}" data-track-index="4" data-width="{W}" data-height="{H}"></div>',
    f'<div id="captions" data-track-kind="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" '
    f'data-start="0" data-duration="{TOTAL}" data-track-index="3" data-width="{W}" data-height="{H}"></div>',
]

html_out = f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <title>Jus Gout — edit</title>
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
"""
(ROOT / "index.html").write_text(html_out)

# A readable cut list + clean transcript for review.
lines = [f"TOTAL {TOTAL:.2f}s  ({len(segs)} A-roll segments, {len(EDL['broll'])} B-roll overlays, {sfx_n[0]} SFX, {cap_id} caption cards)", ""]
for s in segs:
    lines.append(f"{s['start']:6.2f}-{s['end']:6.2f}  {s['id']}  src {s['in']:6.2f}-{s['out']:6.2f}  {' '.join(w['text'] for w in s['words'])}")
(ROOT / "data/cutlist.txt").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
