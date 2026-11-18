"""EDL for lab-biotix-3 (18 Nov). Run tools/prep.py first. Talking clip kept, plain one-word caption, motion text in the
Lab Biotix theme (fx_theme "biotix"), visual overlays: realistic AI photos (tools/gen.sh) for the situations he describes,
the listing photos (assets/photos/P1-P2, from lab-biotix-2) and the grass B-roll of the box and sachets."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L, BI = T["lines"], T["broll"]


def bt(clip, t):
    """time inside the source B-roll clip -> time in assets/b.mp4"""
    return round(BI[clip]["offset"] + t - BI[clip]["in"], 3)


FIX = {"bag": "beg", "bagi": "beg", "baik": "beg", "nampakkan": "dapatkan", "halu": "hala", "jeli": "jelly", "biotix": "Biotix", "triple": "Triple", "diharung,": "harung,", "for": "FOMO"}
DROPW = {"aa", "ha", "hmm", "eh"}
REDO = []
SKIP = []


def words(path, offset=0.0):
    out = []
    for line in (P / path).read_text().splitlines():
        for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
            core = w.rstrip('.,?!')
            if core.lower() in FIX:
                w = FIX[core.lower()] + w[len(core):]
            if core.lower() in DROPW:
                continue
            s, e = float(s) + offset, float(e) + offset
            if out and w.startswith('-'):   # whisper splits 'biasa-biasa', 'siap-siap', 'pagi-pagi' at the hyphen
                pw, ps, _ = out.pop()
                w, s = pw + w, ps
            out.append((w, s, e))
    return out


SW = {"m": words(".media/wl-113459.txt")}
tr, used = [], set()
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            # whisper often starts a piece's first word early (silence before it): allow 0.8 s, clamp to the cut
            if a - 0.8 <= s < b - 0.2 and e - s < 3.0 and s not in used:
                used.add(s)
                s = max(s, a)
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(max(e, s + 0.05), b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"L1": "HOOK — 113459 8-17", "L5": "his own use (3rd-4th box)", "L8": "eats one (kept through the bite)", "L11": "CTA (143 + 196)"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
AI = {"A1": (["L1", "eloklah"], ["L1", "usus"], "AI: a Malaysian man in his forties jogging in a park (aurat-safe)"),
      "A2": (["L2", "makanan"], ["L2", "end"], "AI: night-market stall with trendy street food, a man holding a viral snack (aurat-safe)"),
      "A3": (["L3", "pemakanan"], ["L3", "end"], "AI: a late-night table of fast food (no people)"),
      "A4": (["L7", "rasa#2"], ["L7", "end"], "AI: mixed berries and fruit jelly cubes (no people)")}
photos = [{"id": k, "from": f, "to": t, "note": n} for k, (f, t, n) in AI.items() if (P / f"assets/photos/{k}.jpg").exists()]
photos += [{"id": "P1", "from": ["L6", "dia#3"], "to": ["L6", "probiotik"], "ai": False, "note": "listing photo: box and sachet (from lab-biotix-2)"},
           {"id": "P2", "from": ["L6", "probiotik"], "to": ["L6", "end"], "ai": False, "note": "listing photo: two boxes with berries (from lab-biotix-2)"}]
write(P, 3, "VID_20261118_113459 (tools/prep.py)", segs, zoom=1.0, origin="50% 40%",
      broll=[cu("C1", ["L4", "local"], ["L4", "end"], bt("110857", 4.5), "50% 50%", (1.0, 1.06), "the box front on the grass"),
             cu("C2", ["L5", "kali"], ["L5", "orang"], bt("110857", 25.0), "50% 50%", (1.0, 1.06), "a handful of sachets"),
             cu("C3", ["L10", "start"], ["L10", "end"], bt("110857", 18.0), "50% 50%", (1.0, 1.05), "the open box full of sachets"),
             cu("C4", ["L11", "start"], ["L11", "so"], bt("110857", 50.0), "50% 50%", (1.0, 1.05), "the box with the sachets on the grass")]
            + ([] if (P / "assets/photos/A4.jpg").exists() else [cu("C5", ["L7", "rasa#2"], ["L7", "end"], bt("110857", 29.0), "50% 50%", (1.0, 1.05), "sachets on the grass")]),
      photos=photos,
      kps=[kp("DAH MASUK 40-AN?", ["40-AN?"], ["L1", "start"], ["L1", "eloklah"], "zoom", 150, 100)],
      note_extra=" 18 Nov: talking kept; caption kept; motion text in the Lab Biotix theme; realistic AI visuals where needed.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "pill", "from": ["L1", "usus"], "to": ["L1", "end"], "text": "USUS KENA JAGA", "x": 60, "y": 1040},
    {"type": "tags", "from": ["L2", "inovasi"], "to": ["L2", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "INOVASI MAKANAN", "at": ["L2", "inovasi"]}, {"text": "FOMO", "at": ["L2", "fomo"]},
        {"text": "MAKANAN PELIK-PELIK", "at": ["L2", "pelik-pelik"]}]},
    {"type": "pill", "from": ["L3", "seimbangkan"], "to": ["L3", "end"], "text": "SEIMBANGKAN PEMAKANAN", "x": 60, "y": 250},
    {"type": "hud", "from": ["L4", "local"], "to": ["L4", "end"], "title": "LOCAL BRAND", "value": "TRIPLE BIOTIX", "sub": "JENAMA TEMPATAN", "x": 60, "y": 150},
    {"type": "pill", "from": ["L5", "kali"], "to": ["L5", "end"], "text": "DAH KALI KE-4 CONSUME", "x": 60, "y": 250},
    {"type": "tags", "from": ["L6", "probiotik"], "to": ["L6", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "PROBIOTIK", "at": ["L6", "probiotik"]}, {"text": "PREBIOTIK", "at": ["L6", "prebiotik"]},
        {"text": "POSTBIOTIK", "at": ["L6", "postbiotik"]}]},
    {"type": "pill", "from": ["L7", "start"], "to": ["L7", "end"], "text": "RASA JELLY, SENANG MAKAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["L9", "ambil#2"], "to": ["L9", "end"], "text": "AMBIL IKUT DOS", "x": 60, "y": 1040},
    {"type": "dial", "from": ["L10", "10"], "to": ["L10", "end"], "n": 10, "label": "SACHET SEKOTAK", "x": 540, "y": 330},
    {"type": "promo", "from": ["L11", "start"], "to": ["L11", "end"], "tag": "BEG KUNING", "title": "HARGA TAK MAHAL", "sub": "BELI SEKARANG", "y": 760},
]
e["_note"] = ("Lab Biotix Triple Biotix #3 — assets/a.mp4 built by tools/prep.py from VID_20261118_113459 (talking, picture synced). "
              "Cutaways: VID_20261114_110857 (grass B-roll; the owner put it in this folder too), the listing photos P1-P2 and realistic "
              "AI photos A1-A4 ('ILUSTRASI AI'). Clip -> video: 113459, 110857 -> this video. Dropped: " + T["dropped"] + ". No price; "
              "'harga pun tak mahal' is his own wording.")
e["theme"] = {"key": "#3DD3C8", "brand": "#C08BF0"}
e["fx_theme"] = "biotix"
e["fs_style"] = "cut"
e["mirror"] = False   # rear camera: the box reads correctly
e["brand_words"] = ["triple", "biotix"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
