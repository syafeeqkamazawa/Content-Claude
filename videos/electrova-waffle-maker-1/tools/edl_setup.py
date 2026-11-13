"""EDL for electrova-waffle-maker-1 (13 Nov). Run tools/prep.py first. Same look as jus-gout-14 / kurma-ajwa-quba-6:
talking clip kept, motion text (EDL "fx") + plain one-word caption from the Jus Gout 'video contoh', visual overlays
(the owner's own B-roll: pouring, the timer knob, the lid opening, the finished waffle, eating it)."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L, BI = T["lines"], T["broll"]


def bt(clip, t):
    """time inside the source B-roll clip -> time in assets/b.mp4"""
    return round(BI[clip]["offset"] + t - BI[clip]["in"], 3)


# whisper spellings -> what the owner says (he pronounces 'waffle' as 'wafer')
FIX = {"wafer": "waffle", "waifu": "waffle", "kala": "kaler", "kesuai": "kesesuaian", "teman": "tema", "buni": "bunyi",
       "bag": "beg", "biasakan": "biasa", "li": "tengok", "elevtrova": "Electrova", "eletrova": "Electrova"}
DROPW = {"aa", "ha", "hmm", "eh"}


def words(path, offset=0.0):
    out = []
    for line in (P / path).read_text().splitlines():
        for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
            core = w.rstrip('.,?!')
            if core.lower() in FIX:
                w = FIX[core.lower()] + w[len(core):]
            if core.lower() not in DROPW:
                out.append((w, float(s) + offset, float(e) + offset))
    return out


SW = {"m": words(".media/wl-090052.txt"), "r": words(".media/wl-092819.txt")}
tr = []
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            if a <= s < b and e - s < 1.6:
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(e, b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"M1": "HOOK — 090052 5-25", "M8": "the four plates (counting stretch 147-252 dropped)", "M10": "swapping a plate",
         "R1": "VID_20261113_092819 — the moment of truth", "M14": "CTA"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 1, "VID_20261113_090052 + VID_20261113_092819 (tools/prep.py)", segs, zoom=1.0, origin="50% 40%",
      broll=[cu("C1", ["M1", "start"], ["M1", "tepung"], bt("095121", 0.3), "50% 50%", (1.0, 1.06), "lifting a golden waffle off the plate"),
             cu("C2", ["M1", "tepung"], ["M1", "yang"], bt("092000", 8.0), "50% 50%", (1.0, 1.06), "pouring batter into the open waffle maker"),
             cu("C3", ["M8", "seterusnya"], ["M8", "lepas"], bt("093613", 2.0), "50% 55%", (1.0, 1.06), "square waffle in the waffle plate"),
             cu("C4", ["M11", "start"], ["M11", "lepas"], bt("092000", 44.0), "50% 50%", (1.0, 1.05), "maker closed on the batter"),
             cu("C5", ["M11", "lepas"], ["M11", "end"], bt("092406", 4.0), "50% 60%", (1.0, 1.10), "timer knob close-up"),
             cu("C6", ["M12", "start"], ["M12", "end"], bt("095047", 0.2), "50% 50%", (1.0, 1.06), "lid opens on the golden waffle"),
             cu("C7", ["M14", "start"], ["M14", "seller"], bt("095912", 106.0), "50% 45%", (1.0, 1.05), "owner eating the waffle"),
             cu("C8", ["M14", "seller"], ["M14", "end"], bt("093613", 15.0), "50% 55%", (1.0, 1.06), "waffle lifted out with a fork")],
      kps=[kp("WAFFLE MAKER ELECTROVA", ["ELECTROVA"], ["M1", "start"], ["M1", "tepung"], "zoom", 200, 108)],
      note_extra=" 12 Nov: motion text + caption from the Jus Gout 'video contoh'; visual overlays; talking kept.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "pill", "from": ["M2", "warna"], "to": ["M2", "end"], "text": "WARNA ESTETIK", "x": 60, "y": 250},
    {"type": "dial", "from": ["M3", "dua"], "to": ["M3", "ok,"], "n": 2, "label": "PILIHAN WARNA", "x": 300, "y": 330},
    {"type": "hud", "from": ["M4", "berat"], "to": ["M4", "end"], "title": "BERAT", "value": "SOLID", "sub": "BADAN METAL", "x": 380, "y": 170},
    {"type": "pill", "from": ["M5", "start"], "to": ["M5", "end"], "text": "BUKU MANUAL ADA", "x": 60, "y": 250},
    {"type": "dial", "from": ["M7", "empat"], "to": ["M7", "end"], "n": 4, "label": "PATTERN", "x": 300, "y": 330},
    {"type": "tags", "from": ["M8", "start"], "to": ["M8", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "1. ACUAN PERTAMA", "at": ["M8", "start"]}, {"text": "2. DONAT", "at": ["M8", "donat"]},
        {"text": "3. WAFFLE", "at": ["M8", "seterusnya"]}, {"text": "4. BULAT", "at": ["M8", "keempat,"]}]},
    {"type": "pill", "from": ["M9", "banyak"], "to": ["M9", "end"], "text": "BANYAK PILIHAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["M10", "senang"], "to": ["M10", "tolak"], "text": "TUKAR ACUAN SENANG", "x": 60, "y": 250},
    {"type": "pill", "from": ["M10", "tolak"], "to": ["M10", "end"], "text": "TOLAK SAMPAI BUNYI", "x": 60, "y": 250},
    {"type": "hud", "from": ["M11", "timer"], "to": ["M11", "end"], "title": "TIMER", "value": "SET IKUT SUKA", "sub": "NAK GARING, NAK CRISPY", "x": 380, "y": 170},
    {"type": "pill", "from": ["M12", "berbaloi"], "to": ["M12", "end"], "text": "BERBALOI", "x": 60, "y": 250},
    {"type": "pill", "from": ["M13", "lock"], "to": ["M13", "end"], "text": "LOCK KUAT", "x": 60, "y": 250},
    {"type": "promo", "from": ["M14", "seller"], "to": ["M14", "end"], "tag": "PROMO", "title": "SEMENTARA ADA DISKAUN", "sub": "DI BEG KUNING", "y": 230},
]
e["_note"] = ("Electrova Waffle Maker #1 — assets/a.mp4 built by tools/prep.py from VID_20261113_090052 (talking, unboxing) and "
              "VID_20261113_092819 (voiced cooking clip; picture synced). B-roll (assets/b.mp4): 092000 (pouring, closing), "
              "092406 (timer knob), 093613 (waffle in the plate), 095047 (lid opens), 095121 (lifting the waffle), 095912 "
              "100-203 s (eating). Clip -> video: 090052, 092819, 092000, 092406, 093613, 095047, 095121, 095912 (100-203 s) -> "
              "this video; 084758, 092656, 091202, 091251, 091338, 092709, 095912 (0-100 s) -> tepung-wafel-rangup-1. Dropped: "
              + T["dropped"] + ". No price; colours, weight, four plates, timer, lock and promo are the owner's own words.")
e["theme"] = {"key": "#E3A94B", "brand": "#FFFFFF"}
e["fs_style"] = "cut"
e["mirror"] = False   # rear camera: the box reads correctly
e["brand_words"] = ["electrova"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
