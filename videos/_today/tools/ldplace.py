"""Move each lidar card (EDL "ld": hook / chip / cta) to a height where it covers no face (owner rule: text never over
the face), then rebuild. Faces: YuNet on assets/a.mp4 (A-roll in output time) at 4 fps over the card's time window.
python3 ldplace.py SLUG [SLUG ...]"""
import json, re, subprocess, sys
from pathlib import Path
import cv2

V = Path(__file__).resolve().parents[1].parent
MODEL = str(V.parent / "tools-shared/face_yunet.onnx")
CAP_TOP = 1300                     # word caption band starts here; cards stay above it
H = {"hook": 350, "cta": 480, "chip": 115}
CAND = {"hook": [150, 330, 520, 700, 860], "cta": [170, 330, 520, 700, 800],
        "chip": [330, 150, 260, 450, 600, 760, 900, 1050, 1160]}


def photo_faces(img, det):
    fr = cv2.imread(str(img))
    if fr is None:
        return []
    s = max(1080 / fr.shape[1], 1920 / fr.shape[0])          # object-fit: cover onto 1080x1920
    fr = cv2.resize(fr, (round(fr.shape[1] * s), round(fr.shape[0] * s)))
    ox, oy = (fr.shape[1] - 1080) // 2, (fr.shape[0] - 1920) // 2
    sm = cv2.resize(fr, (round(fr.shape[1] * 720 / fr.shape[0]), 720))
    det.setInputSize((sm.shape[1], sm.shape[0]))
    _, fs = det.detect(sm)
    k = fr.shape[0] / 720
    return [(x * k - ox - 0.25 * w * k, y * k - oy - 0.45 * h * k, x * k - ox + 1.25 * w * k, y * k - oy + 1.2 * h * k)
            for x, y, w, h in ((f[:4]).tolist() for f in (fs if fs is not None else []))]


def faces(cap, det, t0, t1, fsw=()):
    out, t = [], t0 + 0.05
    while t < t1:
        cov = [w for w in fsw if w[0] <= t < w[1]]
        if cov:                                   # a full-screen cutaway hides the A-roll: use the photo's faces
            out += cov[0][2]
            t += 0.25
            continue
        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
        ok, fr = cap.read()
        if ok:
            s = 720 / fr.shape[0]
            sm = cv2.resize(fr, (round(fr.shape[1] * s), 720))
            det.setInputSize((sm.shape[1], sm.shape[0]))
            _, fs = det.detect(sm)
            for f in (fs if fs is not None else []):
                x, y, w, h = (f[:4] / s * 1920 / fr.shape[0]).tolist()
                out.append((x - 0.25 * w, y - 0.45 * h, x + 1.25 * w, y + 1.2 * h))   # hair + chin margin
        t += 0.25
    return out


def place(slug):
    P = V / slug
    e = json.loads((P / "data/edl.json").read_text())
    g = (P / "compositions/graphics.html").read_text()
    win = {int(k): (float(a), float(a) + float(d)) for k, a, d in
           re.findall(r'id="ov-ld(\d+)" class="clip overlay" data-start="([\d.]+)" data-duration="([\d.]+)"', g)}
    cap = cv2.VideoCapture(str(P / "assets/a.mp4"))
    det = cv2.FaceDetectorYN.create(MODEL, "", (405, 720), 0.6)
    vis = (P / "compositions/visuals.html").read_text() if (P / "compositions/visuals.html").exists() else ""
    fsw = []
    for i, a, d in re.findall(r'id="fs-([^"]+)" class="clip fs[^"]*" data-start="([\d.]+)" data-duration="([\d.]+)"', vis):
        img = P / f"assets/photos/{i}.jpg"
        fsw.append((float(a), float(a) + float(d), photo_faces(img, det) if img.exists() else []))
    ld = e.get("ld", [])
    cta0 = min([win[k][0] for k, m in enumerate(ld) if m["type"] == "cta" and k in win] or [1e9])
    for k, m in enumerate(ld):                     # a chip never runs on under the CTA card
        if m["type"] == "chip" and k in win and win[k][0] < cta0 < win[k][1]:
            if cta0 - win[k][0] < 1.5:
                del win[k]; m["to"] = list(m["from"]); continue
            m["to"] = ["@", round(cta0 - 0.1, 2)]; win[k] = (win[k][0], cta0 - 0.1)
    log, placed = [], []
    order = sorted(range(len(e.get("ld", []))), key=lambda k: e["ld"][k]["type"] == "chip")   # hook / cta first
    for k in order:
        m = e["ld"][k]
        if k not in win:
            continue
        typ, h = m["type"], H[m["type"]] + (45 if m.get("sub") and m["type"] == "chip" else 0)
        fb = faces(cap, det, *win[k], fsw)
        if typ == "chip":
            xr = (1080 - m.get("x", 50) - 720, 1080 - m.get("x", 50)) if m.get("side", "right") == "right" else (m.get("x", 50), m.get("x", 50) + 720)
        else:
            xr = (70, 1010)

        t0, t1 = win[k]

        def hit(y):
            n = sum(1 for (a, b, c, d) in fb if a < xr[1] and c > xr[0] and b < y + h + 20 and d > y - 20)
            return n + sum(100 for (u0, u1, py, ph, px) in placed       # never stack on another card
                           if u0 < t1 and u1 > t0 and px[0] < xr[1] and px[1] > xr[0] and py < y + h + 20 and py + ph > y - 20)
        y0 = m.get("y", CAND[typ][0])
        opts = [y0] + [y for y in CAND[typ] if y != y0 and y + h <= CAP_TOP]
        best = min(opts, key=lambda y: (hit(y), abs(y - y0)))
        log.append(f"ld{k} {typ} y {y0}->{best} (hits {hit(y0)}->{hit(best)}, {len(fb)} faces)")
        m["y"] = best
        placed.append((t0, t1, best, h, xr))
    (P / "data/edl.json").write_text(json.dumps(e, indent=1, ensure_ascii=False))
    r = subprocess.run(["python3", "tools/build.py"], cwd=P, capture_output=True, text=True)
    print(slug, "|", "; ".join(log), "|", (r.stdout + r.stderr).strip().splitlines()[-1])


for s in sys.argv[1:]:
    place(s)
