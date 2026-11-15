"""EDL for supersave-alas-kaki-2 (15 Nov). Run tools/prep.py first. Voiceover video shaped like the owner's 'Video contoh':
plain one-word caption (style kept), motion text in the product's black-and-white tile theme (fx_theme "tile"), cutaways
from his eight clips."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L = T["lines"]


def bt(clip, t):
    """time inside a source clip -> time in assets/b.mp4"""
    return round(T["broll"][clip]["offset"] + t - T["broll"][clip]["in"], 3)


FIX = {"bag": "beg", "back": "beg", "bagi": "beg", "burah": "murah", "kod": "code"}
DROPW = {"aa", "ha", "hmm", "eh"}
REDO = []
HALLU = []


def words(path, skip=()):
    out = []
    for line in (P / path).read_text().splitlines():
        for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
            s, e = float(s), float(e)
            if any(a <= s < b for a, b in skip):
                continue
            core = w.rstrip('.,?!')
            if core.lower() in FIX:
                w = FIX[core.lower()] + w[len(core):]
            if core.lower() in DROPW:
                continue
            # whisper splits 'kadang-kadang' at the hyphen and 'prebiotik' as 'pre biotik'
            if out and (w.startswith('-') or (core.lower().lstrip('-').startswith("biotik") and out[-1][0].lower() in ("pre", "pro", "post"))):
                pw, ps, _ = out.pop()
                w = pw + (w if w.startswith('-') and not w[1:].lower().startswith("biotik") else w.lstrip('-'))
                s = ps
            out.append((w, s, e))
    return out


SW = {"v": words(".media/wl-rec1513.txt")}
tr, used = [], set()
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            # whisper sometimes starts a line's first word early (silence before it): allow 0.8 s, clamp to the cut
            if a - 0.8 <= s < b - 0.2 and e - s < 3.0 and (d["src"], s) not in used:
                used.add((d["src"], s))
                s = max(s, a)
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(e, b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"V1": "HOOK", "V4": "complete take after the retakes", "V8": "CTA take 6", "V9": "CTA — last take"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 2, "voiceover rec1513 over VID_20261115_113747 ... 114959 (tools/prep.py)", segs, zoom=1.0, origin="50% 50%",
      broll=[cu("C1", ["V2", "start"], ["V2", "dia"], bt("114541", 1.6), "50% 50%", (1.0, 1.06), "flipping the mat: the rubber base"),
             cu("C2", ["V2", "corak"], ["V2", "end"], bt("114930", 0.3), "50% 50%", (1.0, 1.06), "the tile pattern close up"),
             cu("C3", ["V4", "anti-slip"], ["V4", "end"], bt("114541", 2.6), "50% 50%", (1.0, 1.05), "a hand on the rubber base"),
             cu("C4", ["V7", "bahagian"], ["V7", "end"], bt("114959", 8.6), "50% 50%", (1.0, 1.05), "the base after the water: dry"),
             cu("C5", ["V9", "sementara"], ["V9", "end"], bt("113948", 12.5), "50% 50%", (1.0, 1.05), "the mat laid down in the kitchen")],
      photos=[],
      kps=[kp("TAK PAYAH BELI MAHAL-MAHAL", ["MAHAL-MAHAL"], ["V1", "start"], ["V1", "end"], "zoom", 640, 96)],
      note_extra=" 15 Nov: voiceover video shaped like the owner's 'Video contoh'; caption kept; motion text in the product's tile theme.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "tags", "from": ["V2", "start"], "to": ["V2", "corak"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "ANTI-SLIP", "at": ["V2", "start"]}, {"text": "SERAP AIR", "at": ["V2", "serap"]}]},
    {"type": "tags", "from": ["V2", "saiz#2"], "to": ["V2", "corak"], "y": 420, "cols": 3, "x0": 60, "dx": 330, "items": [
        {"text": "SAIZ L", "at": ["V2", "saiz#2"]}, {"text": "SAIZ M", "at": ["V2", "saiz#3"]}, {"text": "SAIZ S", "at": ["V2", "saiz#4"]}]},
    {"type": "pill", "from": ["V2", "corak"], "to": ["V2", "end"], "text": "CORAK CANTIK-CANTIK", "x": 60, "y": 250},
    {"type": "hud", "from": ["V3", "start"], "to": ["V3", "end"], "title": "CODE CORAK", "value": "MOROCCAN MIX", "sub": "YANG SAYA PUNYA", "x": 60, "y": 150},
    {"type": "pill", "from": ["V4", "memang"], "to": ["V4", "anti-slip"], "text": "SELESA, TAK LICIN", "x": 60, "y": 250},
    {"type": "pill", "from": ["V4", "anti-slip"], "to": ["V4", "end"], "text": "ANTI-SLIP", "x": 60, "y": 250},
    {"type": "pill", "from": ["V5", "start"], "to": ["V5", "end"], "text": "TAK BERGERAK", "x": 60, "y": 250},
    {"type": "pill", "from": ["V6", "terus"], "to": ["V6", "end"], "text": "TERUS LAWA RUANG DAPUR", "x": 60, "y": 250},
    {"type": "hud", "from": ["V7", "start"], "to": ["V7", "bahagian"], "title": "PENYERAPAN", "value": "PANTAS", "sub": "KENA AIR, TERUS SERAP", "x": 60, "y": 150},
    {"type": "pill", "from": ["V7", "bahagian"], "to": ["V7", "end"], "text": "BELAKANG TAK TEMBUS", "x": 60, "y": 250},
    {"type": "promo", "from": ["V8", "start"], "to": ["V9", "end"], "tag": "BEG KUNING", "title": "HARGA TENGAH MURAH", "sub": "MACAM-MACAM CORAK ADA", "y": 760},
]
e["_note"] = ("SuperSave Alas Kaki Dapur #2 — voiceover video. Sound: Recorder 20261115-1513.m4a (best take of each point). Picture: "
              "VID_20261115_113747, 113948, 114541, 114641, 114747, 114834, 114930, 114959 (every clip used) cut to the words, plus "
              "cutaways from the same clips. 'Video contoh.mp4' = the owner's reference for the shape (not used as footage); the "
              "screenshot is reference only. Dropped: " + T["dropped"] + ". No price; promo in his words.")
e["theme"] = {"key": "#111111", "brand": "#FFFFFF"}
e["fx_theme"] = "tile"
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fs_style"] = "cut"
e["mirror"] = False
e["brand_words"] = ["supersave"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
