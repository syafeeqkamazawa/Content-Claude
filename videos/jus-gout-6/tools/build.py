#!/usr/bin/env python3
"""Build index.html + compositions/ for the Promaxx Jus Gout #6 edit (split-flap captions, moving overlays, preparation B-roll, no music) from data/edl.json.

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

ACCENT = "#FFC24A"  # Jus Gout label yellow
BERRY = "#F28C1B"  # Jus Gout ankle orange (title edge)
INK = "#3A1E0C"  # Jus Gout label brown (title panel)
CREAM = "#FFFBEF"
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
SYL = {"titanz": 2, "180+": 6, "180": 5, "12": 4, "18": 3, "60": 3, "aquamin": 3, "menaq7": 4, "k2": 2, "c": 1, "mixed": 1, "berries": 2, "kid": 1, "kid180": 4, "2": 2, "elderberry": 4, "cranberry": 3, "blueberry": 3, "check": 1, "check": 1, "3": 2, "12": 4, "fluoride": 3, "synergy": 3, "lysozyme": 3, "parent": 2, "check": 1, "strawberi": 3, "berry": 2, "buddies": 2}


def syllables(word):
    w = word.lower().strip(".,?!")
    return SYL.get(w) or max(1, len(re.findall(r"[aeiouy]+", w)))


TRANSCRIPT = json.loads((ROOT / "data/transcript-a.json").read_text()) if (ROOT / "data/transcript-a.json").exists() else []


def time_words(text, t_in, t_out):
    """Word times from the whisper transcript when its word count in the range matches the
    script text; otherwise spread words over the detected speech by syllable count."""
    words = text.split()
    tw = []
    for w in TRANSCRIPT:
        if t_in - 0.05 <= w["s"] < t_out - 0.05:
            if tw and w["w"].strip().startswith("-"):  # "Lagi -lagi" is one word
                tw[-1] = dict(tw[-1], e=w["e"])
            else:
                tw.append(w)
    if len(tw) == len(words):
        return [(w, max(t_in, x["s"]), min(t_out, x["e"])) for w, x in zip(words, tw)]
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
for seg_id, word, amount in EDL.get("punch", []):
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
    z0, z1 = b.get("push", [1.0, 1.06])  # slow push; a larger end value zooms into the label
    origin = b.get("origin", "50% 50%")
    main_js.append(f'tl.set("#bw-{b["id"]}", {{ transformOrigin: "{origin}" }}, 0);')
    main_js.append(f'tl.fromTo("#bw-{b["id"]}", {{ scale: {round(z0 * 1.12, 3)} }}, {{ scale: {z0}, duration: 0.3, ease: "power3.out" }}, {t0});')
    main_js.append(
        f'tl.fromTo("#bw-{b["id"]}", {{ scale: {z0} }}, {{ scale: {z1}, duration: {q(max(0.1, d - 0.34))}, ease: "power1.inOut", immediateRender: false }}, {q(t0 + 0.34)});'
    )
    if b.get("ff"):  # owner (Hero Hige): the usage clip plays fast-forward, full screen
        main_dom.append(
            f'<div id="ff-{b["id"]}" class="clip ff" data-start="{t0}" data-duration="{d}" data-track-index="5">'
            f'<div class="ff-tag" id="ff-{b["id"]}-tag">{html.escape(b["ff"])}</div>'
            f'<div class="ff-bar"><div class="ff-fill" id="ff-{b["id"]}-fill"></div></div></div>'
        )
        main_js.append(f'tl.fromTo("#ff-{b["id"]}-tag", {{ scale: 1.6, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.5)" }}, {t0});')
        main_js.append(f'tl.fromTo("#ff-{b["id"]}-tag", {{ opacity: 1 }}, {{ opacity: 0.45, duration: 0.45, ease: "sine.inOut", yoyo: true, repeat: {max(1, int((d - 0.4) / 0.45) - 1)}, immediateRender: false }}, {q(t0 + 0.4)});')
        main_js.append(f'tl.fromTo("#ff-{b["id"]}-fill", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {d}, ease: "none" }}, {t0});')
    cover.append((t0, t1))

# ── 3. Visuals: full-screen realistic AI cutaways ──────────────────────────
# Owner's standing rules (see /CLAUDE.md): full-screen, realistic only, every
# person fully covers aurat, small "ILUSTRASI AI" tag.
vis_dom, vis_js = [], []
for k, p in enumerate(EDL["photos"]):
    t0, t1 = q(anchor(p["from"])), q(min(anchor(p["to"]), TOTAL))
    pid, d = p["id"], q(max(0.1, t1 - t0))
    side = 1 if k % 2 == 0 else -1  # alternate the drift direction photo to photo
    layered = (ROOT / f"assets/photos/{pid}-fg.png").exists() and (ROOT / f"assets/photos/{pid}-bg.jpg").exists()
    if layered:  # moving overlay: background plate and cut-out subject drift apart (2.5D parallax)
        inner = (f'<div class="fs-layer" id="fs-{pid}-bg" style="background-image:url(assets/photos/{pid}-bg.jpg)"></div>'
                 f'<div class="fs-layer fs-fg" id="fs-{pid}-fg" style="background-image:url(assets/photos/{pid}-fg.png)"></div>')
    else:
        inner = f'<div class="fs-layer" id="fs-{pid}-bg" style="background-image:url(assets/photos/{pid}.jpg)"></div>'
    vis_dom.append(
        f'<div id="fs-{pid}" class="clip fs" data-start="{t0}" data-duration="{fr_dur(round((t1 - t0) * FPS))}" data-track-index="4">'
        f'<div class="fs-in" id="fs-{pid}-in">{inner}</div>'
        + (f'<div class="fs-shine" id="fs-{pid}-sh"></div>' if p.get("fx") == "shine" else "")
        + '<div class="fs-tag">ILUSTRASI AI</div></div>'
    )
    if p.get("fx") == "shine":
        vis_js.append(f'tl.fromTo("#fs-{pid}-sh", {{ x: -1300, skewX: -18 }}, {{ x: 1300, skewX: -18, duration: 1.1, ease: "power2.inOut", repeat: 1, repeatDelay: 0.3 }}, {q(t0 + 0.3)});')
    # punch-in on the cut, then continuous motion for the whole shot
    vis_js.append(f'tl.fromTo("#fs-{pid}-in", {{ scale: 1.14, opacity: 0.6 }}, {{ scale: 1.0, opacity: 1, duration: 0.35, ease: "power3.out" }}, {t0});')
    if layered:
        vis_js.append(f'tl.fromTo("#fs-{pid}-bg", {{ scale: 1.1, x: {12 * side}, y: 0 }}, {{ scale: 1.15, x: {-12 * side}, y: -8, duration: {d}, ease: "none", immediateRender: false }}, {t0});')
        vis_js.append(f'tl.fromTo("#fs-{pid}-fg", {{ scale: 1.1, x: {-8 * side}, y: 6 }}, {{ scale: 1.18, x: {8 * side}, y: -10, duration: {d}, ease: "sine.inOut", immediateRender: false }}, {t0});')
    else:
        vis_js.append(f'tl.fromTo("#fs-{pid}-bg", {{ scale: 1.1, x: {36 * side}, y: 10 }}, {{ scale: 1.2, x: {-36 * side}, y: -10, duration: {d}, ease: "sine.inOut", immediateRender: false }}, {t0});')
    cover.append((t0, t1))

# A whoosh only where a cutaway starts from the talking head (not cutaway → cutaway).
cover.sort()
for i, (t0, t1) in enumerate(cover):
    if t0 > 0.1 and (i == 0 or abs(cover[i - 1][1] - t0) > 0.05):
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

# One title per beat, from the owner's visual plan (data/edl.json "titles").
for i, t in enumerate(EDL["titles"]):
    tid = f"tt-{i + 1}"
    t0, t1 = card(f"ov-{tid}", anchor(t["from"]) if t["from"][1] != "start" else SEG[t["from"][0]]["start"],
                  anchor(t["to"]) if t["to"][1] not in ("start", "end") else (SEG[t["to"][0]]["end"] if t["to"][1] == "end" else SEG[t["to"][0]]["start"]),
                  f'<div class="{"cta" if t.get("cta") else "title " + t.get("pos", "low") + (" " + t["cls"] if t.get("cls") else "")}" id="{tid}">{html.escape(t["text"])}</div>')
    if t.get("cta"):
        gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "back.out(1.8)" }}, {t0});')
        gfx_js.append(
            f'tl.fromTo("#{tid}", {{ scale: 1 }}, {{ scale: 1.06, duration: 0.4, ease: "sine.inOut", yoyo: true, '
            f'repeat: {max(1, int((t1 - t0 - 0.4) / 0.4) - 1)}, immediateRender: false }}, {q(t0 + 0.35)});'
        )
        add_sfx("ping", t0, 0.4)
    else:
        anim = t.get("anim", "pop")
        if anim == "zoom":  # zoom in from huge, keep creeping in
            gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 0, scale: 2.4 }}, {{ opacity: 1, scale: 1, duration: 0.38, ease: "expo.out" }}, {t0});')
            gfx_js.append(f'tl.fromTo("#{tid}", {{ scale: 1 }}, {{ scale: 1.08, duration: {q(max(0.2, t1 - t0 - 0.6))}, ease: "none", immediateRender: false }}, {q(t0 + 0.38)});')
        elif anim == "zoomout":  # starts close, pulls back slowly
            gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1.12, duration: 0.3, ease: "power3.out" }}, {t0});')
            gfx_js.append(f'tl.fromTo("#{tid}", {{ scale: 1.12 }}, {{ scale: 0.96, duration: {q(max(0.2, t1 - t0 - 0.5))}, ease: "power1.out", immediateRender: false }}, {q(t0 + 0.3)});')
        elif anim == "slam":  # drops in tilted and settles
            gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 0, scale: 1.8, rotation: -6, y: -60 }}, {{ opacity: 1, scale: 1, rotation: -2, y: 0, duration: 0.3, ease: "back.out(3)" }}, {t0});')
            gfx_js.append(f'tl.fromTo("#{tid}", {{ rotation: -2 }}, {{ rotation: 0, duration: 0.5, ease: "elastic.out(1, 0.4)", immediateRender: false }}, {q(t0 + 0.3)});')
        elif anim in ("slide", "slide-r"):  # sweeps across
            sx = -1100 if anim == "slide" else 1100
            gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 1, x: {sx}, skewX: {-12 if sx < 0 else 12} }}, {{ x: 0, skewX: 0, duration: 0.42, ease: "power4.out" }}, {t0});')
            gfx_js.append(f'tl.fromTo("#{tid}", {{ x: 0 }}, {{ x: {12 if sx < 0 else -12}, duration: {q(max(0.2, t1 - t0 - 0.7))}, ease: "none", immediateRender: false }}, {q(t0 + 0.42)});')
        else:
            gfx_js.append(f'tl.fromTo("#{tid}", {{ opacity: 0, scale: 0.6, y: -20 }}, {{ opacity: 1, scale: 1, y: 0, duration: 0.32, ease: "back.out(2)" }}, {t0});')
        add_sfx(t.get("sfx", "pop"), t0 - 0.02, t.get("sfx_vol", 0.32))
        if t1 < TOTAL - 0.1:
            fade_out(f"#{tid}", t1)


# ── 5. Captions ────────────────────────────────────────────────────────────
# Owner (21 Oct): captions in the split-flap "departure board" style of the
# reference video — two rows of flap tiles near the top, uppercase letters that
# scramble left to right before settling, keywords in amber and brand names in
# coral. Scramble glyphs are picked deterministically (no Math.random).
FLAP_COLS, FLAP_ROWS = 14, 2
FLAP_GLYPHS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%&?!+/"
FLAP_WHITE, FLAP_AMBER, FLAP_CORAL, FLAP_SCRAMBLE = "#F4F4F4", "#FFB627", "#FF6B57", "#8E9AA6"
BRAND = {norm(k) for k in EDL.get("brand_words", [])}
cap_dom, cap_js = [], []
cap_id = 0


def flap_text(w):
    return w["text"].strip().rstrip(",").upper()[:FLAP_COLS]


cards = []
for s in segs:
    lines, seg_cards = [[]], []
    for w in s["words"]:
        d = flap_text(w)
        cur = lines[-1]
        width = sum(len(flap_text(x)) for x in cur) + len(cur)
        if not cur or width + len(d) <= FLAP_COLS:
            cur.append(w)
        elif len(lines) < FLAP_ROWS:
            lines.append([w])
        else:
            seg_cards.append(lines)
            lines = [[w]]
        if w["text"].strip()[-1:] in ".?!":
            seg_cards.append(lines)
            lines = [[]]
    if lines[0]:
        seg_cards.append(lines)
    for i, ls in enumerate(seg_cards):
        c0 = ls[0][0]["s"] if i else s["start"]
        c1 = seg_cards[i + 1][0][0]["s"] if i + 1 < len(seg_cards) else s["end"]
        cards.append((q(c0), q(c1), ls))

cells = []
for r in range(FLAP_ROWS):
    for c in range(FLAP_COLS):
        cells.append(f'<div class="fl-cell"><span class="fl-ch" id="fl-{r}-{c}"></span></div>')
cap_dom.append(f'<div id="fl-board" class="clip fl-board" data-start="0" data-duration="{TOTAL}" data-track-index="3">{"".join(cells)}</div>')
state = {(r, c): (" ", FLAP_WHITE) for r in range(FLAP_ROWS) for c in range(FLAP_COLS)}
for k, (c0, c1, ls) in enumerate(cards):
    cap_id += 1
    target = {(r, c): (" ", FLAP_WHITE) for r in range(FLAP_ROWS) for c in range(FLAP_COLS)}
    rows = ls if len(ls) == FLAP_ROWS else ls + [[]] * (FLAP_ROWS - len(ls))
    for r, line in enumerate(rows):
        chars = []
        for j, w in enumerate(line):
            col = FLAP_CORAL if norm(w["text"]) in BRAND else FLAP_AMBER if norm(w["text"]) in KEYWORDS else FLAP_WHITE
            if j:
                chars.append((" ", FLAP_WHITE))
            chars += [(ch, col) for ch in flap_text(w)]
        off = (FLAP_COLS - len(chars)) // 2
        for c, v in enumerate(chars[:FLAP_COLS]):
            target[(r, off + c)] = v
    for (r, c), (ch, col) in target.items():
        if state[(r, c)] == (ch, col):
            continue
        t = c0 + c * 0.018 + r * 0.05
        if ch != " ":
            for n in range(3):
                g = FLAP_GLYPHS[(k * 131 + r * 17 + c * 7 + n * 29) % len(FLAP_GLYPHS)]
                cap_js.append(f'tl.set("#fl-{r}-{c}", {{ textContent: "{g}", color: "{FLAP_SCRAMBLE}" }}, {q(t + n * 0.045)});')
        cap_js.append(f'tl.set("#fl-{r}-{c}", {{ textContent: "{html.escape(ch) if ch != " " else ""}", color: "{col}" }}, {q(t + 0.14)});')
        cap_js.append(f'tl.fromTo("#fl-{r}-{c}", {{ scaleY: 0.25 }}, {{ scaleY: 1, duration: 0.09, ease: "power2.out", immediateRender: false }}, {q(t + 0.14)});')
        state[(r, c)] = (ch, col)

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

FLIP = ".frame-wrap video.aroll { transform: scaleX(-1); }\n" if EDL.get("mirror", True) else ""
CSS_MAIN = f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; background: #1c0f06; }}
#root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #1c0f06; font-family: "Montserrat", sans-serif; }}
.frame-wrap {{ position: absolute; inset: 0; overflow: hidden; transform-origin: 50% 35%; }}
.frame-wrap video {{ position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover; }}
{FLIP}.broll {{ transform-origin: 50% 50%; }}
.ff {{ position: absolute; inset: 0; pointer-events: none; }}
.ff-tag {{ position: absolute; right: 48px; top: 200px; font-family: "Archivo Black"; font-size: 46px; letter-spacing: 2px; color: {ACCENT};
  background: rgba(20,32,90,.82); padding: 10px 24px; border-radius: 12px; border: 3px solid {ACCENT}; transform-origin: 100% 50%; }}
.ff-bar {{ position: absolute; left: 0; right: 0; bottom: 0; height: 14px; background: rgba(0,0,0,.35); }}
.ff-fill {{ width: 100%; height: 100%; background: {ACCENT}; transform-origin: 0% 50%; }}
"""

CSS_VIS = f"""
#vis-root {{ position: absolute; inset: 0; }}
.fs {{ position: absolute; inset: 0; overflow: hidden; background: #1c0f06; }}
.fs-in {{ position: absolute; inset: 0; transform-origin: 50% 45%; }}
.fs-layer {{ position: absolute; inset: 0; background: center / cover no-repeat; transform-origin: 50% 55%; will-change: transform; }}
.fs-shine {{ position: absolute; top: -10%; bottom: -10%; left: 0; width: 100%; transform: translateX(-1300px) skewX(-18deg);
  background: linear-gradient(90deg, rgba(255,255,255,0) 30%, rgba(255,255,255,.45) 50%, rgba(255,255,255,0) 70%); }}
.fs-tag {{ position: absolute; right: 110px; top: 390px; font-family: "Montserrat"; font-weight: 700; font-size: 18px; letter-spacing: 1.5px;
  color: {CREAM}; background: rgba(40,20,8,.72); padding: 5px 10px; border-radius: 6px; }}
"""

CSS_GFX = FONT_FACE + f"""
#gfx-root {{ position: absolute; inset: 0; font-family: "Plus Jakarta Sans", sans-serif; }}
.overlay {{ position: absolute; inset: 0; pointer-events: none; }}
.title {{ position: absolute; left: 50px; right: 50px; top: 980px; text-align: center; font-family: "Archivo Black"; font-size: 62px; line-height: 1.08;
  color: #FFFFFF; background: {INK}; border-bottom: 10px solid {BERRY}; padding: 18px 30px 20px; border-radius: 14px; box-shadow: 0 14px 30px rgba(0,0,0,.35); transform-origin: 50% 50%; }}
.title.top {{ top: 430px; }}
.title.mid {{ top: 760px; }}
.title.big {{ font-size: 120px; line-height: 1.0; padding: 22px 30px 26px; }}
.title.narrow {{ left: 230px; right: 230px; }}
.title.small {{ font-size: 50px; }}
.title {{ white-space: pre-line; }}
.cta {{ position: absolute; left: 60px; bottom: 210px; font-family: "Archivo Black"; font-size: 54px; color: #2a1a05; background: {YELLOW};
  padding: 22px 36px; border-radius: 999px; box-shadow: 0 12px 0 #2a1a05; transform-origin: 0% 50%; }}
"""

CSS_CAP = """@font-face { font-family: "Barlow Condensed"; src: url("assets/fonts/BarlowCondensed-SemiBold-latin.woff2") format("woff2");
  font-weight: 600; font-style: normal; font-display: block; }""" + f"""
#cap-root {{ position: absolute; inset: 0; }}
.fl-board {{ position: absolute; left: 50%; top: 170px; width: auto; height: auto; transform: translateX(-50%); padding: 10px; background: #0b0b0b;
  border-radius: 14px; box-shadow: 0 16px 40px rgba(0,0,0,.45); display: grid; grid-template-columns: repeat({FLAP_COLS}, 56px);
  grid-auto-rows: 84px; gap: 6px 5px; }}
.fl-cell {{ position: relative; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(180deg, #2c2c2c 0%, #212121 49%, #0d0d0d 50%, #1d1d1d 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.07), inset 0 -1px 0 rgba(0,0,0,.6); }}
.fl-cell::after {{ content: ""; position: absolute; left: 0; right: 0; top: 50%; height: 2px; margin-top: -1px; background: rgba(0,0,0,.8); }}
.fl-ch {{ display: inline-block; font-family: "Barlow Condensed"; font-weight: 600; font-size: 64px; line-height: 1; color: {FLAP_WHITE};
  transform-origin: 50% 50%; }}
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
SHOW_CAPTIONS = EDL.get("captions", True)  # owner: this clip has no captions and no overlays
hosts = []
if vis_dom:
    (ROOT / "compositions/visuals.html").write_text(subcomp("visuals", "vis-root", CSS_VIS, vis_dom, vis_js))
    hosts.append(f'<div id="visuals" data-composition-id="visuals" data-composition-src="compositions/visuals.html" '
                 f'data-start="0" data-duration="{TOTAL}" data-track-index="4" data-width="{W}" data-height="{H}"></div>')
if gfx_dom:
    (ROOT / "compositions/graphics.html").write_text(subcomp("graphics", "gfx-root", CSS_GFX, gfx_dom, gfx_js))
    hosts.append(f'<div id="graphics" data-composition-id="graphics" data-composition-src="compositions/graphics.html" '
                 f'data-start="0" data-duration="{TOTAL}" data-track-index="2" data-width="{W}" data-height="{H}"></div>')
if SHOW_CAPTIONS:
    (ROOT / "compositions/captions.html").write_text(subcomp("captions", "cap-root", CSS_CAP, cap_dom, cap_js))
    hosts.append(f'<div id="captions" data-track-kind="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" '
                 f'data-start="0" data-duration="{TOTAL}" data-track-index="3" data-width="{W}" data-height="{H}"></div>')

(ROOT / "index.html").write_text(f"""<!doctype html>
<html lang="ms">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <title>Promaxx Jus Gout #6 — review</title>
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
