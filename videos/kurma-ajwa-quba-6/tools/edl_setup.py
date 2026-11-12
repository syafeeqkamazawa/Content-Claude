"""EDL for kurma-ajwa-quba-6 (12 Nov). Run tools/prep.py first. Same look as jus-gout-14 / titanz-kid180-10:
talking clips kept, motion text (EDL "fx") + plain one-word caption from the Jus Gout 'video contoh', visual overlays."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L = T["lines"]


def words(path, offset=0.0):
    out = []
    if (P / path).exists():
        for line in (P / path).read_text().splitlines():
            for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
                out.append((w, float(s) + offset, float(e) + offset))
    return out


SW = {"k1": words(".media/wl-k1.txt", 18.0), "k2": words(".media/wl-k2.txt")}
tr = []
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            if a <= s < b and e - s < 1.6:
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(e, b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"Q1": "HOOK — fourth try (0-39 dropped)", "Q4": "first try at 74 dropped", "R1": "VID_20261112_162533 — opens and shows a date",
         "R3": "third try of the comment line", "Q10": "CTA take 2"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 6, "VID_20261112_162407 + VID_20261112_162533 (tools/prep.py)", segs, zoom=1.0, origin="50% 40%",
      photos=[ph("pagi7", ["Q1", "sarapan"], ["Q1", "end"], "AI (kurma-ajwa-quba-5): seven dates and water on the breakfast table, no people"),
              ph("pagi", ["Q10", "sarapan"], ["Q10", "aku"], "AI (kurma-ajwa-quba-4): dates and water by the window at sunrise, no people")],
      kps=[kp("SARAPAN CEPAT?", ["CEPAT?"], ["Q1", "start"], ["Q1", "sarapan"], "zoom", 200, 118)],
      note_extra=" 12 Nov: motion text + caption from the Jus Gout 'video contoh'; visual overlays; talking kept.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "pill", "from": ["Q4", "kurma"], "to": ["Q4", "end"], "text": "KURMA AJWA QUBA FOOD", "x": 60, "y": 250},
    {"type": "dial", "from": ["Q5", "kurma"], "to": ["Q5", "end"], "n": 1, "label": "KILOGRAM", "x": 300, "y": 330},
    {"type": "tags", "from": ["Q6", "bentuk"], "to": ["Q6", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "BENTUK", "at": ["Q6", "bentuk"]}, {"text": "TEKSTUR", "at": ["Q6", "tekstur"]}, {"text": "KUALITI", "at": ["Q6", "kualiti"]}]},
    {"type": "pill", "from": ["Q8", "berat"], "to": ["Q8", "end"], "text": "BERAT 1 KG", "x": 60, "y": 250},
    {"type": "hud", "from": ["Q9", "dan"], "to": ["Q9", "end"], "title": "TEKSTUR", "value": "SEDERHANA", "sub": "TAK TERLALU BASAH, TAK TERLALU KERING", "x": 380, "y": 170},
    {"type": "pill", "from": ["R1", "chewy-chewy,"], "to": ["R1", "end"], "text": "CHEWY-CHEWY", "x": 60, "y": 250},
    {"type": "pill", "from": ["R3", "start"], "to": ["R3", "memang"], "text": "DROP KOMEN", "x": 60, "y": 250},
    {"type": "promo", "from": ["Q10", "promo"], "to": ["Q10", "end"], "tag": "PROMO", "title": "SEMENTARA HARGA MURAH", "sub": "DI BEG KUNING", "y": 230},
]
e["_note"] = ("Kurma Ajwa Quba Food #6 — assets/a.mp4 built by tools/prep.py from VID_20261112_162407 and VID_20261112_162533 "
              "(both talking; picture synced). Dropped: " + T["dropped"] + ". 1 kg, texture and promo are the owner's own words; no price.")
e["theme"] = {"key": "#E8B04B", "brand": "#FFFFFF"}
e["fs_style"] = "cut"
e["brand_words"] = ["quba", "food", "ajwa"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
