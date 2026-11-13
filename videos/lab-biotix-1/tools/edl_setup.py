"""EDL for lab-biotix-1 (13 Nov). Run tools/prep.py first. Voiceover video: the owner's recorder takes over his car
clip VID_20261113_185850. Same look as electrova-waffle-maker-1: motion text (EDL "fx") + plain one-word caption from
the Jus Gout 'video contoh', visual overlays (close-ups from the same clip + the owner's two product photos)."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L = T["lines"]
F = "185850"


def bt(t):
    """time inside VID_20261113_185850 -> time in assets/b.mp4 (the whole clip)"""
    return round(T["broll"][F]["offset"] + t - T["broll"][F]["in"], 3)


FIX = {"sacet": "sachet", "bay": "beg", "bag": "beg", "rekomen.": "recommend.", "rekomen": "recommend"}
DROPW = {"aa", "ha", "hmm", "eh"}


def words(path):
    out = []
    for line in (P / path).read_text().splitlines():
        for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
            s, e = float(s), float(e)
            core = w.rstrip('.,?!')
            if core.lower() in FIX:
                w = FIX[core.lower()] + w[len(core):]
            if core.lower() in DROPW:
                continue
            # whisper splits 'korang' as 'Kau orang', 'ketiga-tiga' / 'L-carnitine' at the hyphen
            if out and (w.startswith('-') or (core.lower() == "orang" and out[-1][0].lower() == "kau")):
                pw, ps, _ = out.pop()
                w = ("Korang" + w[len(core):]) if core.lower() == "orang" else pw + w
                if w.lower().startswith("l-carnitin"):
                    w = "L-carnitine" + w[len(w.rstrip('.,?!')):]
                s = ps
            out.append((w, s, e))
    return out


SW = {"v": words(".media/wl-rec1904.txt"), "c": words(".media/wl-rec1907.txt")}
tr, used = [], set()
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            # whisper sometimes starts a line's first word early (silence before it): allow 0.8 s, clamp to the cut
            if a - 0.8 <= s < b and e - s < 1.8 and (d["src"], s) not in used:
                used.add((d["src"], s))
                s = max(s, a)
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(e, b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"V1": "HOOK — rec1904 2-8", "V8": "first 'ada 30 bilion CFU, ada 30' take dropped",
         "V12": "second, cleaner take", "C1": "CTA — rec1907 (clean take)"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 1, "voiceover rec1904 + rec1907 over VID_20261113_185850 (tools/prep.py)", segs, zoom=1.0, origin="50% 45%",
      broll=[cu("C1", ["V6", "jangan"], ["V6", "end"], bt(11.0), "50% 45%", (1.0, 1.06), "the box front close to camera — '30 Billion CFU'"),
             cu("C2", ["V10", "start"], ["V10", "end"], bt(102.0), "50% 50%", (1.0, 1.06), "tearing the sachet close to camera"),
             cu("C3", ["V12", "aku"], ["V12", "end"], bt(149.9), "50% 45%", (1.0, 1.04), "thumbs up after tasting")],
      photos=[{"id": "P1", "from": ["V7", "gabungkan"], "to": ["V7", "end"], "ai": False,
               "note": "owner's own photo of the sachet: PREBIOTIC / PROBIOTIC / POSTBIOTIC with L-Carnitine (image-1794567567790.jpg)"},
              {"id": "P2", "from": ["V8", "start"], "to": ["V8", "end"], "ai": False,
               "note": "owner's own photo of the box back: 30 Billion CFU, the seven strains, L-Carnitine (image-1794567584303.jpg)"}],
      kps=[kp("APA BEZA 3 BIOTIK?", ["3"], ["V1", "start"], ["V1", "end"], "zoom", 200, 104)],
      note_extra=" 12 Nov: motion text + caption from the Jus Gout 'video contoh'; visual overlays. 13 Nov Lab Biotix: voiceover over the car clip.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "hud", "from": ["V3", "start"], "to": ["V3", "end"], "title": "PREBIOTIK", "value": "MAKANAN", "sub": "UNTUK BAKTERIA BAIK", "x": 60, "y": 150},
    {"type": "hud", "from": ["V4", "start"], "to": ["V4", "end"], "title": "PROBIOTIK", "value": "BAKTERIA", "sub": "BAIK ITU SENDIRI", "x": 60, "y": 150},
    {"type": "hud", "from": ["V5", "start"], "to": ["V5", "end"], "title": "POSTBIOTIK", "value": "KOMPONEN", "sub": "MIKROORGANISMA TAK HIDUP", "x": 60, "y": 150},
    {"type": "pill", "from": ["V6", "jangan"], "to": ["V6", "end"], "text": "JANGAN TENGOK BILION JE", "x": 60, "y": 250},
    {"type": "dial", "from": ["V7", "ketiga-tiga"], "to": ["V7", "end"], "n": 3, "label": "DALAM 1 SACHET", "x": 540, "y": 330},
    {"type": "tags", "from": ["V8", "start"], "to": ["V8", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "30 BILION CFU", "at": ["V8", "start"]}, {"text": "7 JENIS BAKTERIA", "at": ["V8", "tujuh"]},
        {"text": "L-CARNITINE", "at": ["V8", "siap"]}]},
    {"type": "tags", "from": ["V9", "start"], "to": ["V9", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "MIXED BERRY", "at": ["V9", "mixed"]}, {"text": "20 G SATU SACHET", "at": ["V9", "satu"]},
        {"text": "10 SACHET SEKOTAK", "at": ["V9", "kotak"]}]},
    {"type": "pill", "from": ["V10", "rutin"], "to": ["V10", "end"], "text": "RUTIN HARIAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["V11", "start"], "to": ["V11", "rasanya"], "text": "SENANG MAKAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["V11", "rasanya"], "to": ["V11", "end"], "text": "RASA SEDAP", "x": 60, "y": 250},
    {"type": "pill", "from": ["V12", "aku"], "to": ["V12", "end"], "text": "SANGAT RECOMMEND", "x": 60, "y": 250},
    {"type": "promo", "from": ["C1", "start"], "to": ["C1", "end"], "tag": "BEG KUNING", "title": "HARGA TENGAH MURAH", "sub": "CHECK OUT SEKARANG", "y": 200},
]
e["_note"] = ("Lab Biotix Triple Biotix #1 — voiceover video. Sound: Recorder 20261113-1904.m4a (script) and Recorder "
              "20261113-1907.m4a (clean CTA take), cleaned with the tools/voice.sh chain. Picture: VID_20261113_185850 (car "
              "clip, no speech) cut to follow the words; close-up cutaways from the same clip (assets/b.mp4) and the owner's "
              "two photos (assets/photos/P1.jpg sachet front, P2.jpg box back — real photos, no AI tag). Clip -> video: every "
              "file in the folder -> this video. Dropped: " + T["dropped"] + ". No price; 30 billion CFU, seven strains, "
              "L-carnitine, mixed berry, 20 g, 10 sachets are printed on the pack.")
e["theme"] = {"key": "#3EC6BD", "brand": "#C08BF0"}
e["fs_style"] = "cut"
e["mirror"] = False   # rear camera: the box reads correctly
e["brand_words"] = ["triple", "biotix"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
