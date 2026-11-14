"""EDL for lab-biotix-2 (14 Nov). Run tools/prep.py first. Voiceover video: the owner's recording Recorder
20261114-1105 over his table clip VID_20261114_100411 and grass clip VID_20261114_110857. Same look as lab-biotix-1:
motion text (EDL "fx") + plain one-word caption from the Jus Gout 'video contoh', visual overlays (the listing's
product photos from the owner's TikTok screenshots)."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L = T["lines"]


def bt(clip, t):
    """time inside a source clip -> time in assets/b.mp4"""
    return round(T["broll"][clip]["offset"] + t - T["broll"][clip]["in"], 3)


FIX = {"sacek": "sachet", "sacet": "sachet", "bay": "beg", "bag": "beg", "naikkan": "naik", "belly": "berry",
       "triple": "Triple", "biotix": "Biotix", "bes": "base", "best": "base"}
DROPW = {"aa", "ha", "hmm", "eh"}
REDO = [(21.2, 27.6), (30.5, 37.0)]   # whisper got these word times wrong; .media/wl-fix.txt re-times them
HALLU = [(73.6, 80.0)]                 # whisper's "terima kasih kerana menonton" over the silence at the end


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


SW = {"v": sorted(words(".media/wl-rec1105.txt", REDO + HALLU) + words(".media/wl-fix.txt"), key=lambda x: x[1])}
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

NOTES = {"H1": "HOOK — rec1105 2.3-9.3 (first take)", "B1": "retake after the 'dia punya base tu' false start",
         "C1": "CTA"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 2, "voiceover rec1105 over VID_20261114_100411 + VID_20261114_110857 (tools/prep.py)", segs, zoom=1.0, origin="50% 45%",
      broll=[],
      photos=[{"id": "A1", "from": ["H1", "banyak"], "to": ["H1", "kadang-kadang"], "note": "AI: man at the dining table, full and uncomfortable after a meal (aurat-safe)"},
              {"id": "A2", "from": ["B3", "kapsul"], "to": ["B3", "end"], "note": "AI: capsules and powder being stirred into water (no people)"},
              {"id": "A3", "from": ["B5", "macam"], "to": ["B5", "end"], "note": "AI: mixed berries and fruit jelly cubes (no people)"},
              {"id": "A4", "from": ["B7", "nak"], "to": ["B7", "travel"], "note": "AI: man at the office slipping a sachet into his work bag (aurat-safe)"},
              {"id": "A5", "from": ["B7", "travel"], "to": ["B7", "end"], "note": "AI: man pulling a carry-on through an airport (aurat-safe)"},
              {"id": "P1", "from": ["H2", "ambil"], "to": ["H2", "end"], "ai": False,
               "note": "listing photo of the box and sachet (owner's TikTok screenshot 105226, image 1/4)"},
              {"id": "P2", "from": ["B2", "start"], "to": ["B2", "end"], "ai": False,
               "note": "listing photo, two boxes with berries (screenshot 105231, image 3/4)"},
              {"id": "P3", "from": ["C1", "better"], "to": ["C1", "boleh"], "ai": False,
               "note": "listing photo, boxes packed with parcels (screenshot 105228, image 2/4)"}],
      kps=[kp("PERUT SELALU KEMBUNG?", ["KEMBUNG?"], ["H1", "start"], ["H1", "end"], "zoom", 200, 100)],
      note_extra=" 12 Nov: motion text + caption from the Jus Gout 'video contoh'; visual overlays. 14 Nov Lab Biotix #2: voiceover over the table and grass clips.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "pill", "from": ["H2", "triple"], "to": ["H2", "end"], "text": "TRIPLE BIOTIX", "x": 60, "y": 250},
    {"type": "tags", "from": ["B1", "dalam"], "to": ["B1", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "PREBIOTIK", "at": ["B1", "prebiotik"]}, {"text": "PROBIOTIK", "at": ["B1", "probiotik"]},
        {"text": "POSTBIOTIK", "at": ["B1", "postbiotik"]}]},
    {"type": "tags", "from": ["B2", "start"], "to": ["B2", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "30 BILION CFU", "at": ["B2", "30"]}, {"text": "7 JENIS BAKTERIA BAIK", "at": ["B2", "tujuh"]}]},
    {"type": "pill", "from": ["B3", "bukan"], "to": ["B3", "end"], "text": "BUKAN KAPSUL / SERBUK", "x": 60, "y": 250},
    {"type": "hud", "from": ["B4", "jelly"], "to": ["B4", "end"], "title": "BENTUK", "value": "JELLY", "sub": "KOYAK, TERUS MAKAN", "x": 60, "y": 150},
    {"type": "pill", "from": ["B5", "mixed"], "to": ["B5", "macam"], "text": "RASA MIXED BERRY", "x": 60, "y": 250},
    {"type": "pill", "from": ["B5", "macam"], "to": ["B5", "end"], "text": "MACAM JELLY BUAH", "x": 60, "y": 250},
    {"type": "pill", "from": ["B6", "start"], "to": ["B6", "end"], "text": "TAK RASA MACAM SUPPLEMENT", "x": 60, "y": 250},
    {"type": "dial", "from": ["B7", "10"], "to": ["B7", "nak"], "n": 10, "label": "SACHET SEKOTAK", "x": 540, "y": 330},
    {"type": "tags", "from": ["B7", "nak"], "to": ["B7", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "BAWA PERGI KERJA", "at": ["B7", "kerja"]}, {"text": "TRAVEL", "at": ["B7", "travel"]}]},
    {"type": "promo", "from": ["C1", "start"], "to": ["C1", "end"], "tag": "BEG KUNING", "title": "HARGA PROMO SEKARANG", "sub": "SEBELUM HARGA NAIK BALIK", "y": 200},
]
e["_note"] = ("Lab Biotix Triple Biotix #2 — voiceover video. Sound: Recorder 20261114-1105.m4a, cleaned with the tools/voice.sh "
              "chain. Picture: VID_20261114_100411 (table: box, sachet, tearing it, squeezing the jelly into his mouth) and "
              "VID_20261114_110857 (box and sachets on the grass), cut to follow the words; overlays = three listing photos from "
              "the owner's TikTok screenshots (assets/photos/P1-P3; no AI tag) and five realistic AI photos for the situations he describes "
              "(assets/photos/A1-A5, tools/gen.sh, 'ILUSTRASI AI' tag, split for parallax by tools/plx.sh; owner 14 Nov: 'Ada juga overlay visual'). Not used: screenshot 105233 (photo with a named "
              "doctor's 'recommended by' badge — a third-party endorsement) and the two description screenshots (reference only: "
              "jelly in a sachet, mixed berry, 20 g, 10 sachets, prebiotic + probiotic + postbiotic, L-carnitine). Clip -> video: "
              "the 14 Nov files -> this video; the 13 Nov files -> lab-biotix-1. Dropped: " + T["dropped"] + ". No price "
              "(the listing shows one but the owner does not say it); promo in his own words.")
e["theme"] = {"key": "#3EC6BD", "brand": "#C08BF0"}
e["fs_style"] = "cut"
e["mirror"] = False
e["brand_words"] = ["triple", "biotix"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
