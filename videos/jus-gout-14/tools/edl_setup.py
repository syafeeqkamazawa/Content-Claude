"""EDL for jus-gout-14 (12 Nov). Run tools/prep.py first (assets/a.mp4 + data/timeline.json).

Owner: "Ikut style editing video contoh" then "Sori bukan ikut keseluruhan gaya video contoh tu,
hanya ikut motion overlay text dan caption sahaja. Video saya bercakap masih dikekalkan".
So: the talking clip stays; the reference (src/contoh.mp4) gives the motion text (EDL "fx",
tools/build.py section 4c) and the caption (small white one-word caption at ~70 % height)."""
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


SW = {"clip": words(".media/wl-clip.txt", 45.0), "s1": words(".media/wl-s1.txt"), "s2": words(".media/wl-s2.txt")}
tr = []
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            if a <= s < b and e - s < 1.6:
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(e, b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"H1": "HOOK — fourth try of the hook (16-46 dropped)", "L4": "'kandungan dan cara penyediaan mesti kandungan' dropped",
         "L6": "'dalam ni, ok?' dropped", "L9": "'ok's between the pieces dropped", "L10": "'dua sudu, letaklah ni' dropped",
         "S1": "sambungan 1 (the clip's sound dies at 143 s)", "A": "sambungan 2; 'ikhtiar' framing kept as approved 27 Oct",
         "D": "the 9.3 s 'insyaAllah boleh ikhtiar, boleh cuba…' is the same line — this later take kept", "E": "CTA take 2 ('okay' dropped)"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 14, "VID_20261112_142940 + sambungan 1/2 (tools/prep.py)", segs, zoom=1.0, origin="50% 40%",
      broll=[cu("C1", ["H3", "jus"], ["H3", "end"], 3.0, "50% 50%", (1.0, 1.06), "jar front while he names the product"),
             cu("C2", ["L5", "campuran"], ["L5", "end"], 12.2, "50% 45%", (1.02, 1.1), "back label (ingredients) — six herbs"),
             cu("C3", ["L6", "start"], ["L6", "end"], 55.0, "50% 40%", (1.0, 1.06), "open jar top-down while he lists the herbs"),
             cu("C4", ["L9", "serbuk"], ["L9", "end"], 88.5, "50% 35%", (1.0, 1.08), "scooping the powder"),
             cu("C5", ["L10", "start"], ["L10", "end"], 100.5, "50% 50%", (1.0, 1.06), "two scoops in the cup"),
             cu("C6", ["L11", "start"], ["L11", "end"], 173.3, "50% 50%", (1.0, 1.06), "hot water poured, stirred")],
      photos=[ph("pain", ["C", "start"], ["C", "end"], "AI (reused from jus-gout): man on the bed holding his foot, long sleeves + long trousers")],
      kps=[kp("SAKIT SENDI?", ["SENDI?"], ["H1", "start"], ["H1", "end"], "zoom", 200, 120)],
      note_extra=" 12 Nov: reference src/contoh.mp4 for the motion text and the caption only; the talking clip stays.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}   # reference caption: white, thin outline, ~40 px/letter, centred ~1349 px (70 %)
e["fx"] = [
    {"type": "pill", "from": ["H2", "ikut"], "to": ["H2", "end"], "text": "IKUT MASALAH SEBENAR", "x": 90, "y": 250},
    {"type": "bracket", "from": ["H3", "jus"], "to": ["H3", "end"], "label": "JUS GOUT PRO MAX", "x": 560, "y": 860, "w": 620, "h": 640},
    {"type": "pill", "from": ["L4", "minuman"], "to": ["L4", "end"], "text": "MINUMAN HERBA", "x": 90, "y": 250},
    {"type": "dial", "from": ["L5", "campuran"], "to": ["L5", "end"], "n": 6, "label": "EKSTRAK HERBA", "x": 300, "y": 330},
    {"type": "tags", "from": ["L6", "start"], "to": ["L6", "end"], "y": 120, "cols": 2, "x0": 40, "dx": 540, "items": [
        {"text": "BROMELAIN (NANAS)", "at": ["L6", "bromelain"]}, {"text": "MILK THISTLE", "at": ["L6", "milk"]},
        {"text": "LEMON", "at": ["L6", "lemon,"]}, {"text": "HALIA", "at": ["L6", "halia,"]},
        {"text": "CURCUMA LONGA", "at": ["L6", "curcuma"]}, {"text": "OREN", "at": ["L6", "oren."]}]},
    {"type": "bracket", "from": ["L9", "serbuk"], "to": ["L9", "korang"], "label": "SERBUK", "x": 540, "y": 560, "w": 480, "h": 480},
    {"type": "hud", "from": ["L10", "start"], "to": ["L11", "end"], "title": "CARA BANCUH", "value": "2 SUDU", "sub": "250 ML AIR PANAS", "x": 470, "y": 170},
    {"type": "pill", "from": ["S1", "halia,"], "to": ["S1", "orang"], "text": "BAU HALIA & NANAS", "x": 90, "y": 260},
    {"type": "promo", "from": ["E", "promo"], "to": ["E", "end"], "tag": "PROMO", "title": "SEBELUM HARGA NAIK BALIK", "sub": "DI BEG KUNING", "y": 230},
]
e["_note"] = ("Jus Gout Pro Max #14 — assets/a.mp4 built by tools/prep.py: VID_20261112_142940 (the owner talking; its audio dies "
              "at 143 s) then 'sambungan 1.m4a' and 'sambungan 2.m4a' over VID_20261012_172341 product footage. Dropped: "
              + T["dropped"] + ". Herbs as spoken (bromelain, milk thistle, lemon, halia, curcuma longa, oren); no price.")
e["theme"] = {"key": "#FFC21A", "brand": "#FFFFFF"}
e["fs_style"] = "cut"   # the reference cuts hard
e["brand_words"] = ["jus", "gout"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
