#!/usr/bin/env python3
"""Place the caption board and the status panel so they never cover a face or the product.

Owner (22 Oct, restated 21 Oct for Krill #2): captions must not cover people or the product.
For every caption card: render the frame without captions (FLAP_HIDE=1), cut out the
subject with HyperFrames remove-background, find faces (YuNet,
tools-shared/face_yunet.onnx), then pick
  - the board top (board + prompt bar) from a few candidate heights, and
  - the panel slot (phase 2 only) from left/right columns under or beside the board,
whichever misses every face and covers the least of the subject. The current spot is
kept while it stays clear, so the captions only jump when they must; a panel with no
clear slot ghosts out (null). Writes data/flap-pos.json for tools/build.py.
Run from the project root:  python3 tools/flap_place.py
"""
import json, os, pathlib, re, subprocess, sys
import cv2
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
CANDS = [150, 430, 720, 1010, 1300]          # board tops (px)
PANEL_TOPS = [380, 660, 940]                 # panel tops besides "right under the board"
PANEL_MAX_BOTTOM = 1460                      # keep clear of TikTok's caption / button area
ENV = dict(os.environ, NODE_USE_ENV_PROXY="1")
HF = ["npx", "--yes", "hyperframes@0.8.149"]
FACE_MODEL = str(ROOT.parent.parent / "tools-shared/face_yunet.onnx")


def faces(path):
    """Face boxes (x0, y0, x1, y1) widened to the whole head (hijab, cap, chin)."""
    img = cv2.imread(str(path))
    h, w = img.shape[:2]
    det = cv2.FaceDetectorYN.create(FACE_MODEL, "", (w, h), 0.7)
    _, fs = det.detect(img)
    out = []
    for f in [] if fs is None else fs:
        x, y, fw, fh = (float(v) for v in f[:4])
        out.append((x - 0.25 * fw, y - 0.45 * fh, x + 1.25 * fw, y + 1.2 * fh))
    return out


def cost(box, fb, px):
    """Share of the box (plus 30 px breathing room) on the subject mask; +1 if it touches a face."""
    x0, y0, x1, y1 = box
    y1 += 30
    hit = any(not (y1 < f[1] or y0 > f[3] or x1 < f[0] or x0 > f[2]) for f in fb)
    c = 0.0
    if px is not None:
        ys, xs = range(int(y0) // 10, min(int(y1) // 10, 192)), range(int(x0) // 10, min(int(x1) // 10, 108))
        n = sum(1 for y in ys for x in xs if px[x, y] > 128)
        c = n / max(1, len(ys) * len(xs))
    return round(c + (1.0 if hit else 0.0), 3)


subprocess.run([sys.executable, "tools/build.py"], cwd=ROOT, check=True, env=dict(ENV, FLAP_HIDE="1"), stdout=subprocess.DEVNULL)
info = json.loads((ROOT / "data/flap-cards.json").read_text())
BX, BW, BH1, BH2 = info["block"]
PW, PH = info["panel"] or (0, 0)
cards, cuts = info["cards"], info["cuts"]
times = [round(min(c0 + 0.45, (c0 + c1) / 2), 2) for c0, c1, _ in cards]
snap = ROOT / "snapshots"
fdir = ROOT / ".media/flap-frames"   # kept apart from snapshots/ so review snapshots don't wipe them
mdir = ROOT / ".media/flap-masks"
reuse = "--reuse" in sys.argv  # same edit, only the placement rules changed: keep frames and masks
if not reuse:
    for d in (fdir, mdir):
        for f in d.glob("*.png"):
            f.unlink()
    for f in snap.glob("frame-*.png"):
        f.unlink()
    subprocess.run(HF + ["snapshot", "--at", ",".join(str(t) for t in times), "--no-end", "--timeout", "20000"],
                   cwd=ROOT, env=ENV, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    fdir.mkdir(parents=True, exist_ok=True)
    for f in snap.glob("frame-*.png"):
        f.rename(fdir / f.name)
frames = sorted(fdir.glob("frame-*.png"), key=lambda p: int(re.search(r"frame-(\d+)", p.name).group(1)))
assert len(frames) == len(times), (len(frames), len(times))
mdir.mkdir(parents=True, exist_ok=True)

# Cost of every board top and panel slot on every card's frame.
samples = []
for i, fr in enumerate(frames):
    out = mdir / f"m{i:02d}.png"
    if not out.exists():
        subprocess.run(HF + ["remove-background", str(fr), "-o", str(out)], cwd=ROOT, env=ENV,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    fb = faces(fr)
    px = Image.open(out).convert("RGBA").split()[-1].resize((108, 192)).load() if out.exists() else None
    samples.append((fb, px))


COMPACT = 0.6      # board scale beside a face / the product when the full-width board fits nowhere
PANEL_COMPACT = 0.7
BOARDS = [(BX, t, 1.0) for t in CANDS] + [(x, t, COMPACT) for t in CANDS for x in (30, 1080 - 30 - round(BW * COMPACT))]


def board_box(b, i):
    x, t, sc = b
    return (x, t, x + BW * sc, t + (BH2 if cards[i][2] else BH1) * sc)


def board_cost(b, i):
    return cost(board_box(b, i), *samples[i]) + (0.02 if b[2] < 1 else 0)  # full width preferred


def panel_slots(bb):
    """Panel spots (x, y, scale) that keep clear of the board box bb."""
    out = []
    for sc in (1.0, PANEL_COMPACT):
        pw, ph = PW * sc, PH * sc
        for x in (round(1080 - 48 - pw), 48):
            for t in [round(bb[3] + 16), 150] + PANEL_TOPS:
                if t + ph > PANEL_MAX_BOTTOM or t < 120:
                    continue
                if not (x + pw + 16 < bb[0] or x > bb[2] + 16 or t + ph + 16 < bb[1] or t > bb[3] + 16):
                    continue
                if (x, t, sc) not in out:
                    out.append((x, t, sc))
    return out


# The board keeps one spot per shot (between two cuts), so it only jumps on a cut —
# the worst card of the shot decides; it prefers the full-width board at the top (like
# the reference) and the previous shot's spot. If no spot stays clear for the whole
# shot it follows the subject card by card. A compact board (scale 0.6) sits beside a
# face or the product when the full-width one fits nowhere. The panel is re-checked per
# card: it stays while clear, moves when it must and ghosts out while nothing is clear.
shot_of = [max(j for j, c in enumerate(cuts) if c <= t + 1e-6) for t in times]
pos, prev = [None] * len(cards), BOARDS[0]
for sh in sorted(set(shot_of)):
    idx = [i for i, s in enumerate(shot_of) if s == sh]
    worst = {b: max(board_cost(b, i) for i in idx) for b in BOARDS}
    best = min(BOARDS, key=lambda b: worst[b] + 0.002 * BOARDS.index(b) - (0.01 if b == prev else 0))
    if worst[best] <= 0.08:
        for i in idx:
            pos[i] = best
        print(f"shot {cuts[sh]:6.2f}  cards {len(idx):2d}  board {best} ({worst[best]:.3f})")
    else:
        cur = best
        for i in idx:
            row = {b: board_cost(b, i) for b in BOARDS}
            if row[cur] > 0.03:
                bb = min(BOARDS, key=lambda b: row[b] + 0.002 * BOARDS.index(b))
                if row[bb] < row[cur] - 0.02:
                    cur = bb
            pos[i] = cur
            print(f"shot {cuts[sh]:6.2f}  card {times[i]:6.2f}  board {cur} ({row[cur]:.3f})")
        best = cur
    prev = best
cur = None
out_pos = []
for i, (c0, c1, phase2) in enumerate(cards):
    b = pos[i]
    entry = {"x": b[0], "top": b[1], "s": b[2], "panel": None}
    if phase2 and PW:
        pw = {sl: cost((sl[0], sl[1], sl[0] + PW * sl[2], sl[1] + PH * sl[2]), *samples[i]) + (0.005 if sl[2] < 1 else 0)
              for sl in panel_slots(board_box(b, i))}
        if not (cur in pw and pw[cur] <= 0.015):
            slots = list(pw)
            best = min(slots, key=lambda sl: pw[sl] + 0.001 * slots.index(sl)) if slots else None
            cur = best if best and pw[best] <= 0.02 else None
        entry["panel"] = list(cur) if cur else None
        print(f"  {times[i]:6.2f}  panel {cur} ({pw.get(cur, 0):.3f})")
    out_pos.append(entry)
pos = out_pos
(ROOT / "data/flap-pos.json").write_text(json.dumps(pos))
subprocess.run([sys.executable, "tools/build.py"], cwd=ROOT, check=True, env=ENV, stdout=subprocess.DEVNULL)
