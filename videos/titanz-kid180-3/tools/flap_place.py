#!/usr/bin/env python3
"""Place the split-flap board so it never covers the face or the product (owner, 22 Oct).

For every caption card: render the frame without the board (FLAP_HIDE=1),
cut out the subject with HyperFrames remove-background, and pick the board
top (from a few candidate heights) whose band misses every face (YuNet,
tools-shared/face_yunet.onnx) and covers the least of the subject. Writes
data/flap-pos.json, then tools/build.py animates the board between them.
Run from the project root:  python3 tools/flap_place.py
"""
import json, os, pathlib, re, subprocess, sys
import cv2
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
CANDS = [150, 430, 720, 1010, 1300]          # board tops (px); board is ~194 px tall
BOARD_H, X0, X1 = 194, 105, 975
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

subprocess.run([sys.executable, "tools/build.py"], cwd=ROOT, check=True, env=dict(ENV, FLAP_HIDE="1"), stdout=subprocess.DEVNULL)
cards = json.loads((ROOT / "data/flap-cards.json").read_text())
times = [round(min(c0 + 0.45, (c0 + c1) / 2), 2) for c0, c1 in cards]
snap = ROOT / "snapshots"
for f in snap.glob("frame-*.png"):
    f.unlink()
subprocess.run(HF + ["snapshot", "--at", ",".join(str(t) for t in times), "--no-end", "--timeout", "20000"],
               cwd=ROOT, env=ENV, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
frames = sorted(snap.glob("frame-*.png"), key=lambda p: int(re.search(r"frame-(\d+)", p.name).group(1)))
assert len(frames) == len(times), (len(frames), len(times))

mdir = ROOT / ".media/flap-masks"
mdir.mkdir(parents=True, exist_ok=True)
cover = []
for i, fr in enumerate(frames):
    out = mdir / f"m{i:02d}.png"
    subprocess.run(HF + ["remove-background", str(fr), "-o", str(out)], cwd=ROOT, env=ENV,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    fb = faces(fr)
    hits = [any(not (top + BOARD_H + 30 < f[1] or top > f[3] or X1 < f[0] or X0 > f[2]) for f in fb) for top in CANDS]
    if not out.exists():
        cover.append([1.0 if hit else 0.0 for hit in hits])
        continue
    a = Image.open(out).convert("RGBA").split()[-1].resize((108, 192))
    px = a.load()
    row = []
    for top in CANDS:
        y0, y1 = top // 10, (top + BOARD_H + 30) // 10   # +30 px breathing room under the board
        x0, x1 = X0 // 10, X1 // 10
        n = sum(1 for y in range(y0, min(y1, 192)) for x in range(x0, x1) if px[x, y] > 128)
        row.append(round(n / ((min(y1, 192) - y0) * (x1 - x0)), 3))
    cover.append([1.0 + c if hit else c for c, hit in zip(row, hits)])   # a face in the band rules it out

pos, cur = [], CANDS[0]
for row in cover:
    here = row[CANDS.index(cur)]
    if here > 0.03:                                   # current spot hits the subject: move
        best = min(range(len(CANDS)), key=lambda j: (row[j] + 0.002 * j))
        if row[best] < here - 0.02:
            cur = CANDS[best]
    pos.append(cur)
(ROOT / "data/flap-pos.json").write_text(json.dumps(pos))
for t, row, p in zip(times, cover, pos):
    print(f"{t:6.2f}  cover {row}  -> top {p}")
subprocess.run([sys.executable, "tools/build.py"], cwd=ROOT, check=True, env=ENV, stdout=subprocess.DEVNULL)
