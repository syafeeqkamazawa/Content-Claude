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
    det = cv2.FaceDetectorYN.create(FACE_MODEL, "", (w, h), 0.6)
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
cards = info["cards"]
times = [round(min(c0 + 0.45, (c0 + c1) / 2), 2) for c0, c1, _ in cards]
snap = ROOT / "snapshots"
for f in snap.glob("frame-*.png"):
    f.unlink()
subprocess.run(HF + ["snapshot", "--at", ",".join(str(t) for t in times), "--no-end", "--timeout", "20000"],
               cwd=ROOT, env=ENV, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
frames = sorted(snap.glob("frame-*.png"), key=lambda p: int(re.search(r"frame-(\d+)", p.name).group(1)))
assert len(frames) == len(times), (len(frames), len(times))

mdir = ROOT / ".media/flap-masks"
mdir.mkdir(parents=True, exist_ok=True)
pos, cur_top, cur_panel = [], CANDS[0], None
for i, (fr, (c0, c1, phase2)) in enumerate(zip(frames, cards)):
    out = mdir / f"m{i:02d}.png"
    subprocess.run(HF + ["remove-background", str(fr), "-o", str(out)], cwd=ROOT, env=ENV,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    fb = faces(fr)
    px = Image.open(out).convert("RGBA").split()[-1].resize((108, 192)).load() if out.exists() else None
    bh = BH2 if phase2 else BH1
    row = [cost((BX, t, BX + BW, t + bh), fb, px) for t in CANDS]
    here = row[CANDS.index(cur_top)]
    if here > 0.03:                                   # current spot hits the subject: move
        best = min(range(len(CANDS)), key=lambda j: row[j] + 0.002 * j)
        if row[best] < here - 0.02:
            cur_top = CANDS[best]
    panel, pc = None, None
    if phase2 and PW:
        slots = []
        for x in (1080 - 48 - PW, 48):
            for t in [cur_top + bh + 16] + PANEL_TOPS:
                if t + PH > PANEL_MAX_BOTTOM or not (t >= cur_top + bh + 16 or t + PH <= cur_top - 16):
                    continue
                slots.append((x, t))
        costs = {s: cost((s[0], s[1], s[0] + PW, s[1] + PH), fb, px) for s in slots}
        if cur_panel in costs and costs[cur_panel] <= 0.03:
            panel = cur_panel
        elif costs:
            best = min(costs, key=lambda s: costs[s] + 0.001 * slots.index(s))
            panel = best if costs[best] <= 0.08 else None
        pc = costs.get(panel)
        cur_panel = panel
    pos.append({"top": cur_top, "panel": list(panel) if panel else None})
    print(f"{times[i]:6.2f}  board {row} -> {cur_top}   panel {panel} ({pc})")
(ROOT / "data/flap-pos.json").write_text(json.dumps(pos))
subprocess.run([sys.executable, "tools/build.py"], cwd=ROOT, check=True, env=ENV, stdout=subprocess.DEVNULL)
