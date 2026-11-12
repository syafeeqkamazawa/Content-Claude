"""EDL for titanz-kid180-10 (12 Nov). Run tools/prep.py first (assets/a.mp4, assets/b.mp4, data/timeline.json).
Same look as jus-gout-14: the talking clip stays; motion text (EDL "fx", build.py 4c) and the plain one-word
caption copied from the Jus Gout 'video contoh'; visual overlays on the key points (owner: "Overlay visual juga
masih diperlukan")."""
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


SW = {"clip": words(".media/wl-clip.txt", 30.0)}
tr = []
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            if a <= s < b and e - s < 1.6:
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(e, b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"K1": "HOOK", "K6": "'okay' between dropped", "K11": "'okay' dropped", "K12": "'okay guys' and the 'haa's dropped",
         "K14": "'sukatan ambil apa?' and the first 'kandungan penuh pada tablet ni' dropped", "K20": "CTA take 2"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
B2 = 43.67   # b.mp4: b140338 0-43.67 (bottle, tablets), then b170307 (children)
write(P, 10, "VID_20261112_151248 (tools/prep.py)", segs, zoom=1.0, origin="50% 40%",
      broll=[cu("C1", ["K7", "start"], ["K7", "end"], 0.2, "50% 55%", (1.0, 1.08), "bottle in hand, Kid180 label"),
             cu("C2", ["K9", "start"], ["K9", "telan#2"], 9.0, "50% 50%", (1.0, 1.06), "chewable tablets poured into the cap"),
             cu("C3", ["K9", "telan#2"], ["K9", "end"], 30.0, "50% 55%", (1.0, 1.08), "tablets close"),
             cu("C4", ["K11", "start"], ["K11", "end"], B2 + 24.5, "50% 45%", (1.0, 1.05), "his daughters after taking the tablets (hijab, covered)"),
             cu("C5", ["K13", "macam"], ["K13", "end"], B2 + 3.0, "50% 50%", (1.0, 1.06), "giving a tablet into the child's hand")],
      photos=[ph("membesar", ["K4", "start"], ["K4", "kalsium"], "AI (titanz-kid180-2): family walking, hijab + long clothes"),
              ph("gigi", ["K4", "tulang"], ["K4", "end"], "AI (titanz-kid180-2): boy brushing teeth, pyjamas"),
              ph("pinggan", ["K5", "pemakanan"], ["K5", "end"], "AI (titanz-kid180-3): balanced plate"),
              ph("beri", ["K8", "beri"], ["K8", "jadi,"], "AI (titanz-kid180-2): blueberries, green tea, orange — no people"),
              ph("memilih", ["K18", "masalah"], ["K18", "jadi,"], "AI (titanz-kid180-6): boy who won't eat, mother in hijab")],
      kps=[kp("SUPLEMEN ANAK?", ["ANAK?"], ["K1", "start"], ["K1", "end"], "zoom", 200, 118)],
      note_extra=" 12 Nov: motion text + caption from the Jus Gout 'video contoh'; visual overlays on the key points; talking clip stays.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "dial", "from": ["K2", "benda"], "to": ["K2", "end"], "n": 3, "label": "BENDA PENTING", "x": 540, "y": 330},
    {"type": "pill", "from": ["K3", "start"], "to": ["K3", "end"], "text": "1. KENAPA KALSIUM PENTING?", "x": 60, "y": 250},
    {"type": "pill", "from": ["K6", "start"], "to": ["K6", "end"], "text": "2. APA YANG MENARIK", "x": 60, "y": 250},
    {"type": "pill", "from": ["K7", "tablet"], "to": ["K7", "end"], "text": "TABLET KUNYAH", "x": 60, "y": 250, "ring": [560, 1000, 330]},
    {"type": "tags", "from": ["K8", "beri"], "to": ["K8", "jadi,"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "BERI BIRU", "at": ["K8", "beri"]}, {"text": "TEH HIJAU", "at": ["K8", "teh"]}, {"text": "VITAMIN C", "at": ["K8", "vitamin"]}]},
    {"type": "pill", "from": ["K9", "tak"], "to": ["K9", "untuk"], "text": "TAK PERLU TELAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["K13", "start"], "to": ["K13", "macam"], "text": "3. SESUAI TAK?", "x": 60, "y": 250},
    {"type": "hud", "from": ["K14", "semak"], "to": ["K14", "end"], "title": "SEMAK DULU", "value": "LABEL", "sub": "UMUR, SUKATAN, KANDUNGAN", "x": 470, "y": 170},
    {"type": "tags", "from": ["K15", "karbohidrat,"], "to": ["K15", "end"], "y": 120, "cols": 2, "x0": 40, "dx": 540, "items": [
        {"text": "KARBOHIDRAT", "at": ["K15", "karbohidrat,"]}, {"text": "PROTEIN", "at": ["K15", "protein."]},
        {"text": "VITAMIN C", "at": ["K15", "vitamin"]}, {"text": "KALSIUM", "at": ["K15", "kalsium"]},
        {"text": "VITAMIN K", "at": ["K15", "vitamin#2"]}]},
    {"type": "pill", "from": ["K17", "kena"], "to": ["K17", "end"], "text": "BUKAN PENGGANTI MAKANAN", "x": 60, "y": 250},
    {"type": "promo", "from": ["K20", "promo,"], "to": ["K20", "end"], "tag": "PROMO", "title": "SEBELUM HARGA NAIK", "sub": "DI BEG KUNING", "y": 230},
]
e["_note"] = ("Titanz Kid180 #10 — assets/a.mp4 built by tools/prep.py from VID_20261112_151248 (talking). assets/b.mp4 = "
              "VID_20260908_140338 (0-43.67 s, bottle + tablets) + VID_20260827_170307 (43.67 s on, his children). Dropped: "
              + T["dropped"] + ". Contents (blueberry, green tea, vitamin C; label nutrients) as the owner reads them; no price.")
e["theme"] = {"key": "#FFC21A", "brand": "#FFFFFF"}
e["fs_style"] = "cut"
e["mirror"] = True   # front camera saved mirrored (label reads backwards) — flipped back in CSS
e["brand_words"] = ["titanz", "kid180"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
