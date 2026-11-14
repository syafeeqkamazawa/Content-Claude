"""EDL for electrova-waffle-maker-2 (14 Nov). Run tools/prep.py first. Same look as electrova-waffle-maker-1:
talking clip kept, motion text (EDL "fx") + plain one-word caption from the Jus Gout 'video contoh', visual overlays
(close-ups from the same clip: the toast, the plates, the machine, the timer knob)."""
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
FIX = {"wafer": "waffle", "waifu": "waffle", "bekunin": "beg kuning", "bagun": "beg kuning", "temanas": "pemanas",
       "krispil.": "crispy.", "krispil": "crispy", "marjirin": "marjerin", "kalor": "kaler", "elevtrova": "Electrova",
       "eletrova": "Electrova", "eritrova": "Electrova", "bag": "beg", "jadu": "jadi", "sekat": "cepat", "besambangkan": "best,", "kali": "kaler"}
DROPW = {"aa", "ha", "hmm", "eh", "nabuk", "buk", "amillahi", "wabarakat"}
SKIP = [(43.75, 44.6), (192.0, 192.5), (54.4, 55.3)]   # whisper words that belong to dropped speech
REDO = [(55.3, 60.5)]   # .media/wl-fix.txt


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


SW = {"m": sorted([w for w in words(".media/wl-130306.txt") if not any(a <= w[1] < b for a, b in REDO + SKIP)] + words(".media/wl-fix.txt"), key=lambda x: x[1])}
tr, used = [], set()
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            # whisper often starts a piece's first word early (silence before it): allow 0.8 s, clamp to the cut
            if a - 0.8 <= s < b and e - s < 1.8 and s not in used:
                used.add(s)
                s = max(s, a)
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(max(e, s + 0.05), b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"E1": "HOOK — 130306 3.5-28", "E4": "toppings; one word unclear (not captioned)", "E10": "swapping a plate",
         "E17": "colours + crispy result", "E18": "CTA"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 2, "VID_20261114_130306 (tools/prep.py)", segs, zoom=1.0, origin="50% 40%",
      broll=[cu("C1", ["E1", "roti#2"], ["E1", "boleh"], bt("130306", 36.5), "50% 45%", (1.0, 1.06), "cutting the toast on the board"),
             cu("C2", ["E1", "boleh"], ["E1", "dia"], bt("130306", 126.5), "50% 50%", (1.0, 1.06), "the open machine on the toast plate"),
             cu("C3", ["E1", "waffle#2"], ["E1", "dia#2"], bt("130306", 81.5), "50% 50%", (1.0, 1.06), "the plates spread on the table"),
             cu("C4", ["E8", "start"], ["E8", "end"], bt("130306", 234.5), "50% 50%", (1.0, 1.06), "the cream machine close up"),
             cu("C5", ["E16", "timer"], ["E16", "end"], bt("130306", 228.0), "50% 55%", (1.0, 1.08), "the timer knob close up"),
             cu("C6", ["E17", "warna"], ["E17", "macam#2"], bt("130306", 233.0), "50% 50%", (1.0, 1.05), "the cream machine"),
             cu("C7", ["E17", "suka"], ["E17", "end"], bt("130306", 54.0), "50% 50%", (1.0, 1.06), "the crispy toast lifted up")],
      kps=[kp("ROTI BAKAR + WAFFLE", ["WAFFLE"], ["E1", "start"], ["E1", "roti#2"], "zoom", 60, 84)],
      note_extra=" 12 Nov: motion text + caption from the Jus Gout 'video contoh'; visual overlays; talking kept.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "pill", "from": ["E1", "pelbagai"], "to": ["E1", "end"], "text": "PELBAGAI ACUAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["E2", "acuan"], "to": ["E2", "end"], "text": "ACUAN ROTI BAKAR", "x": 60, "y": 250},
    {"type": "pill", "from": ["E3", "boleh"], "to": ["E3", "end"], "text": "BOLEH POTONG SIAP-SIAP", "x": 60, "y": 250},
    {"type": "dial", "from": ["E5", "empat"], "to": ["E5", "end"], "n": 4, "label": "JENIS ACUAN", "x": 540, "y": 330},
    {"type": "tags", "from": ["E6", "start"], "to": ["E6", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "DONAT", "at": ["E6", "donat"]}, {"text": "BEBOLA KECIL", "at": ["E6", "berbola"]}]},
    {"type": "pill", "from": ["E10", "tarik"], "to": ["E10", "end"], "text": "TARIK & CABUT", "x": 60, "y": 250},
    {"type": "pill", "from": ["E12", "tekan"], "to": ["E12", "end"], "text": "TEKAN SAMPAI BUNYI", "x": 60, "y": 250},
    {"type": "pill", "from": ["E13", "tekan"], "to": ["E13", "end"], "text": "TEKAN SIKIT, BARU CABUT", "x": 60, "y": 250},
    {"type": "hud", "from": ["E14", "pemanas"], "to": ["E14", "end"], "title": "PEMANAS", "value": "ATAS & BAWAH", "sub": "BUKAN BAWAH SAHAJA", "x": 60, "y": 150},
    {"type": "hud", "from": ["E15", "timer"], "to": ["E15", "end"], "title": "TIMER", "value": "SET IKUT SUKA", "sub": "NAK LEBIH GARING, CRISPY", "x": 60, "y": 150},
    {"type": "pill", "from": ["E16", "function."], "to": ["E16", "end"], "text": "SANGAT FUNCTION", "x": 60, "y": 250},
    {"type": "pill", "from": ["E17", "dua"], "to": ["E17", "saya"], "text": "2 WARNA: KRIM & MERAH", "x": 60, "y": 1060},
    {"type": "pill", "from": ["E17", "suka"], "to": ["E17", "end"], "text": "SUKA GARING? LAMAKAN TIMER", "x": 60, "y": 250},
    {"type": "promo", "from": ["E18", "start"], "to": ["E18", "end"], "tag": "BEG KUNING", "title": "HARGA TENGAH DISKAUN", "sub": "SEMENTARA HARGA MASIH MURAH", "y": 720},
]
e["_note"] = ("Electrova Waffle Maker #2 — assets/a.mp4 built by tools/prep.py from VID_20261114_130306 (talking + demo, picture "
              "synced). Cutaways (assets/b.mp4) = close-ups from the same clip. Clip -> video: 130306 -> this video (folder 'Footage "
              "hari ni' holds only this clip). Dropped: " + T["dropped"] + ". No price; plates, heating, timer, colours and promo are "
              "the owner's own words. One topping word in E4 is unclear and left out of the caption (the audio is kept).")
e["theme"] = {"key": "#E3A94B", "brand": "#FFFFFF"}
e["fs_style"] = "cut"
e["mirror"] = False   # rear camera: the box reads correctly
e["brand_words"] = ["electrova"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
