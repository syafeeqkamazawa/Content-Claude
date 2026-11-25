"""21 Nov batch ("Video today", VID_20261121_120947, 36:49, ~22 products in one take) — builds one project per product.

Owner, 21 Nov: "Jangan skip mana mana part saya cakap walaupun awak rasa ada risiko violation ke, hanya potong bahagian
yang berulang ulang, yang ada bunyi err, atau bahagian yang tak sesuai ... Pastikan tak skip semua yang saya cakap dan
biar ada gap 0.5 saat untuk setiap klip supaya percakapan saya tu jelas ... jangan potong dekat sangat. Caption dan text
motion sesuaikan ikut tema produk."

So every Silero-VAD speech stretch inside the product's range is kept except the spans listed in DROP (retakes, a
fluffed line, an off-topic aside). Stretches closer than 0.5 s stay joined; every cut keeps 0.2 s before / 0.3 s after
the speech, i.e. a 0.5 s gap between clips. Usage (repo root): python3 videos/_today/tools/make.py <key> [--no-media]
"""
import json, pathlib, re, shutil, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from specs import SPECS

T = pathlib.Path(__file__).resolve().parents[1]           # videos/_today
SRC = T / "src/120947.mp4"
PRE, POST, JOIN = 0.2, 0.3, 0.5
FIX = {"bag": "beg", "back": "beg", "backcone": "beg", "backcoding": "beg", "bagun": "beg",
       "debit": "beg", "debat": "beg", "kuning,": "kuning,", "sacek": "sachet", "sacet": "sachet", "gamis": "gummies",
       "rekomen": "recommend", "korang.": "korang."}
DROPW = {"aa", "eh", "hmm", "err"}


CUR = {}   # per-spec source override: {"src", "wl", "vad"} (paths relative to videos/)


def vad():
    f = (T.parent / CUR["vad"]) if CUR.get("vad") else (T / ".media/vad.txt")
    return [tuple(map(float, l.strip().split("-"))) for l in f.read_text().splitlines() if l.strip()]


def words(extra=None):
    fx = dict(FIX, **(extra or {}))
    out = []
    files = [(T.parent / f, lo, hi) for f, lo, hi in CUR["wl"]] if CUR.get("wl") else \
            [(T / ".media/wl-120947.txt", 0, 1430), (T / ".media/wl-late.txt", 1430, 1e9)]
    for name, lo, hi in files:
        for line in name.read_text().splitlines():
            if line.startswith("#"):
                continue
            for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
                s, e = float(s), float(e)
                if not (lo <= s < hi):
                    continue
                core = w.rstrip(".,?!").lower()
                if core in DROPW or "menonton" in core:
                    continue
                if core in fx:
                    w = fx[core] + w[len(core):]
                if not w.rstrip(".,?!"):
                    continue
                if out and w.startswith("-"):
                    pw, ps, _ = out.pop(); w, s = pw + w, ps
                elif out and core == "orang" and out[-1][0].lower() == "kau":   # whisper splits 'korang' as 'Kau orang'
                    _, ps, _ = out.pop(); w, s = "Korang" + w[len(core):], ps
                out.append((w, s, e))
    return out


def pieces(spec):
    a0, b0 = spec["range"]
    drop = spec.get("drop", [])
    keep = []
    WS = words()
    for a, b in vad():
        if b <= a0 or a >= b0:
            continue
        a, b = max(a, a0), min(b, b0)
        # cut out dropped spans
        segs = [(a, b)]
        for da, db in drop:
            nxt = []
            for x, y in segs:
                if db <= x or da >= y:
                    nxt.append((x, y))
                else:
                    if da > x: nxt.append((x, da))
                    if db < y: nxt.append((db, y))
            segs = nxt
        keep += [(x, y) for x, y in segs if y - x > 0.25 and (y - x >= 1.0 or any(x - 0.1 <= ws < y + 0.1 for _, ws, _ in WS))]
    # whisper word spans too: Silero VAD sometimes misses a soft word ("Yang", "berdenyut-denyut")
    for w, s, e in words():
        if s < a0 or e > b0 + 0.3:
            continue
        if e - s > 1.0:
            s = e - 0.8   # a word stretched over a pause: its start is unreliable
        if any(not (e <= da or s >= db) for da, db in drop):
            continue
        keep.append((s, min(e, b0)))
    keep.sort()
    for x, y in spec.get("add", []):
        keep.append((x, y))
    keep.sort()
    merged = []
    for x, y in keep:
        if merged and x - merged[-1][1] <= JOIN:
            merged[-1] = (merged[-1][0], max(merged[-1][1], y))
        else:
            merged.append((x, y))
    out = []
    for x, y in merged:
        s0, s1 = x - PRE, y + POST
        if out and s0 < out[-1][1]:
            s0 = out[-1][1]
        out.append((round(s0, 3), round(s1, 3)))
    return out


def run(*a): subprocess.run(a, check=True)


def main(key, media=True):
    global SRC
    spec = SPECS[key]
    CUR.clear(); CUR.update({k: spec[k] for k in ("src", "wl", "vad") if k in spec})
    if spec.get("src"):
        SRC = T.parent / spec["src"]
    P = T.parent / spec["slug"]
    if not (P / "tools/kb2.py").exists():   # gen_ai.py may have created the folder (photos only) first
        shutil.copytree(T / "tpl", P, dirs_exist_ok=True)
    for f in ("build.py", "plx.sh", "plx_plate.py"):
        shutil.copy(T / "tpl/tools" / f, P / "tools" / f)   # keep every project on the latest template
    for d in ("data", ".media", "assets"):
        (P / d).mkdir(exist_ok=True)
    (P / "meta.json").write_text(json.dumps({"id": spec["slug"], "name": spec["slug"], "createdAt": "2026-11-21T05:00:00.000Z"}, indent=2))
    pcs = pieces(spec)
    a0 = spec["range"][0]
    # edit layout
    L, t = [], 0.0
    for k, (x, y) in enumerate(pcs):
        L.append({"id": f"S{k + 1}", "src": [x, y], "e0": round(t, 3), "e1": round(t + y - x, 3)})
        t += y - x
    TOTAL = round(t, 3)
    W = words(spec.get("fix"))
    tr = []
    for seg in L:
        x, y = seg["src"]
        ws = [(w, s, e) for w, s, e in W if x - 0.15 <= s < y - 0.1]
        seg["text"] = " ".join(w for w, _, _ in ws)
        for w, s, e in ws:
            s = max(s, x)
            tr.append({"w": w, "s": round(seg["e0"] + s - x, 3), "e": round(seg["e0"] + min(max(e, s + 0.05), y) - x, 3)})
    if media:
        tmp = P / ".media/prep"; tmp.mkdir(parents=True, exist_ok=True)
        # voice: per-piece cut, light clean-up (high-pass, compressor), one loudness gain for the whole video
        sel = "+".join(f"between(t,{x},{y})" for x, y in pcs)
        r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(SRC), "-vn", "-af",
                            f"aselect='{sel}',asetpts=N/SR/TB,highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,"
                            "loudnorm=I=-15:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
        js = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
        gain = round(-14.0 - float(js["input_i"]), 2)
        lst = []
        for k, (x, y) in enumerate(pcs):
            d = round(y - x, 3)
            out = tmp / f"p{k:03d}.mp4"
            run("ffmpeg", "-v", "error", "-y", "-ss", str(x), "-t", str(d + 0.05), "-i", str(SRC),
                "-vf", f"scale=1080:1920,setsar=1,fps=60,trim=duration={d}",
                "-af", f"atrim=duration={d},highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,volume={gain}dB,"
                       f"afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.05):.3f}:d=0.05,aresample=48000",
                "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le", "-ac", "2", str(out))
            lst.append(f"file '{out}'")
        (tmp / "list.txt").write_text("\n".join(lst) + "\n")
        run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"),
            "-af", "alimiter=limit=0.89:level=false", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-r", "60", "-g", "30",
            "-c:a", "aac", "-b:a", "192k", str(P / "assets/a.mp4"))
        b0, b1 = spec["range"]
        run("ffmpeg", "-v", "error", "-y", "-ss", str(b0), "-t", str(b1 - b0), "-i", str(SRC), "-vf", "scale=1080:1920,setsar=1,fps=60",
            "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "17", "-pix_fmt", "yuv420p", "-g", "30", str(P / "assets/b.mp4"))
        shutil.rmtree(tmp)
    # EDL
    sys.path.insert(0, str(P / "tools"))
    from kb2 import seg, cu, kp, write
    segs = [seg(s["id"], s["e0"], s["e1"], s["text"] or ".", f"src {s['src'][0]:.2f}-{s['src'][1]:.2f}") for s in L]
    broll = [cu(f"C{k + 1}", f, to, round(src - a0, 3), origin, (1.0, 1.07), note)
             for k, (f, to, src, origin, note) in enumerate(spec.get("cut", []))]
    k0 = spec["kp"]
    srcn = spec.get("srcnote", "VID_20261121_120947")
    write(P, 1, f"{srcn} {a0}-{spec['range'][1]} s (videos/_today/tools/make.py)", segs, zoom=1.0, origin="50% 42%",
          broll=broll, photos=[{"id": pid, "from": f, "to": to, "note": "AI: " + pr[:90]} for pid, f, to, pr in spec.get("ai", [])
                               if (P / f"assets/photos/{pid}.jpg").exists()],
          kps=[] if (spec.get("mh") or spec.get("jm") or spec.get("sb")) else [kp(k0[0], k0[1], k0[2], k0[3], "zoom", k0[4] if len(k0) > 4 else 200, k0[5] if len(k0) > 5 else 100)],
          note_extra=" 21 Nov batch: keep every point (only repeats / err / unsuitable bits cut), 0.5 s between clips, caption + motion text in the product theme.")
    (P / "data/transcript-a.json").write_text(json.dumps(tr, ensure_ascii=False))
    e = json.loads((P / "data/edl.json").read_text())
    pal = spec["pal"]
    e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False, "fill": pal.get("cap", "#FFFFFF"),
                 "stroke": pal.get("dark", "#121212"), "hot": pal["key"]}
    e["fx"] = spec.get("fx", [])
    e["mh"] = spec.get("mh", [])   # 25 Nov "mihrab" motion (Sejadah Myna), replaces kp/fx when set
    e["jm"] = spec.get("jm", [])   # 25 Nov "haramain night" clock motion (Jam Kaabah)
    e["sb"] = spec.get("sb", [])   # 25 Nov "storybook" motion (Buku Leveled Reading)
    e["theme"] = {"key": pal["key"], "brand": "#FFFFFF"}
    e["pal"] = pal
    e["fs_style"] = "cut"
    e["mirror"] = spec.get("mirror", False)   # selfie-camera clips (text reads backwards) set True
    e["tighten"] = {"max_pause": 2.0, "keep": 0.5, "threshold_db": -45, "blip": 0.03}
    e["keywords"] = spec.get("keywords", [])
    e["brand_words"] = spec.get("brand", [])
    e["_note"] = (f"{spec['name']} — from {srcn} {a0}-{spec['range'][1]} s (folder 'Video today'). Kept every VAD speech "
                  f"stretch; dropped only: {spec.get('dropnote', 'nothing')}. Pieces: {len(pcs)}, total {TOTAL} s.")
    (P / "data/edl.json").write_text(json.dumps(e, indent=1, ensure_ascii=False))
    (P / "data/timeline.json").write_text(json.dumps({"pieces": pcs, "total": TOTAL, "lines": L}, indent=1, ensure_ascii=False))
    r = subprocess.run(["python3", str(P / "tools/build.py")], capture_output=True, text=True, cwd=P)
    print(r.stdout.strip().splitlines()[0] if r.stdout.strip() else "", r.stderr[-600:])
    print(spec["slug"], "pieces", len(pcs), "total", TOTAL)


if __name__ == "__main__":
    main(sys.argv[1], "--no-media" not in sys.argv)
