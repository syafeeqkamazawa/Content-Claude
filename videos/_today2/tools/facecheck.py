"""Face audit of a final render (owner, 23 Nov: his children's faces must never appear). Samples every 0.1 s, runs
YuNet, and writes a contact sheet of every detected face crop (with its time) so each one can be checked by eye.
python3 facecheck.py video.mp4 out.jpg"""
import sys
from pathlib import Path
import cv2
import numpy as np

vid, out = sys.argv[1], sys.argv[2]
model = str(Path(__file__).resolve().parents[3] / "tools-shared/face_yunet.onnx")
cap = cv2.VideoCapture(vid)
fps = cap.get(cv2.CAP_PROP_FPS) or 60
step = max(1, round(fps / 10))
det = None
crops, n, k = [], 0, 0
while True:
    ok, fr = cap.read()
    if not ok:
        break
    if k % step == 0:
        h, w = fr.shape[:2]
        s = 720 / h
        sm = cv2.resize(fr, (round(w * s), 720))
        if det is None:
            det = cv2.FaceDetectorYN.create(model, "", (sm.shape[1], sm.shape[0]), 0.6)
        _, faces = det.detect(sm)
        n += 1
        for f in (faces if faces is not None else []):
            x, y, fw, fh = (f[:4] / s).astype(int)
            pad = int(max(fw, fh) * 0.4)
            c = fr[max(0, y - pad):y + fh + pad, max(0, x - pad):x + fw + pad]
            if c.size:
                c = cv2.resize(c, (160, 160))
                cv2.putText(c, f"{k / fps:.1f} {f[14]:.2f}", (3, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 1)
                crops.append(c)
    k += 1
print(f"{vid}: {n} frames sampled, {len(crops)} face detections")
if crops:
    crops = crops[::-(-len(crops) // 120)][:120]   # thin out long runs of the same face
    rows = [np.hstack(crops[i:i + 12] + [np.zeros_like(crops[0])] * (12 - len(crops[i:i + 12]))) for i in range(0, len(crops), 12)]
    cv2.imwrite(out, np.vstack(rows))
