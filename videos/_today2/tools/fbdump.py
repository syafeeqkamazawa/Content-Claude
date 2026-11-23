"""Print each My First Book short's kept pieces, total length and words with occurrence numbers (for fx anchors).
python3 fbdump.py fb01 [...]"""
import collections, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_today/tools"))
import make
from specs import SPECS
for key in sys.argv[1:]:
    sp = SPECS[key]
    make.CUR.clear(); make.CUR.update({k: sp[k] for k in ("src", "wl", "vad")})
    pcs = make.pieces(sp)
    tot = sum(y - x for x, y in pcs)
    W = make.words(sp.get("fix"))
    cnt = collections.Counter()
    out, t = [], 0.0
    for x, y in pcs:
        ws = []
        for w, s, e in W:
            if x - 0.15 <= s < y - 0.1:
                n = w.rstrip(".,?!").lower(); cnt[n] += 1
                ws.append(f"{w}#{cnt[n]}@{t + s - x:.1f}")
        out.append(f"  [{t:5.1f}] " + " ".join(ws))
        t += y - x
    print(f"{key} {sp['slug']} pieces {len(pcs)} total {tot:.2f}")
    print("\n".join(out))
