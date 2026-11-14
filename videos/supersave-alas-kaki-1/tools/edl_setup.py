"""EDL for supersave-alas-kaki-1 (14 Nov). Run tools/prep.py first. Talking clip kept, plain one-word caption (style kept),
motion text (EDL "fx") restyled after the product's black-and-white tile pattern (fx_theme "tile"), visual overlays: the
owner's mat B-roll first, realistic AI photos (tools/gen.sh) where he describes a situation."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L, BI = T["lines"], T["broll"]


def bt(clip, t):
    """time inside the source B-roll clip -> time in assets/b.mp4"""
    return round(BI[clip]["offset"] + t - BI[clip]["in"], 3)


FIX = {"bagi": "beg", "bag": "beg", "udah": "dah", "tamu": "tetamu", "berkenaan": "berkenan", "-slip.": "-slip."}
DROPW = {"aa", "ha", "hmm", "eh", "oi."}
REDO = []
SKIP = [(196.5, 196.7)]   # "lebih" — unclear word before "buat promo"


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


SW = {"m": [w for w in words(".media/wl-172736.txt") if not any(a <= w[1] < b for a, b in SKIP)]}
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

NOTES = {"S1": "HOOK — final take (172736 29-32)", "S4": "retake after the first 'korang jangan risau'", "S13": "price in the owner's words", "S16": "CTA"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
AI = {"A1": (["S2", "time-time"], ["S2", "mesti"], "AI: Malay family guests arriving at a Hari Raya open house (aurat-safe)"),
      "A2": (["S3", "langsir"], ["S3", "tapi"], "AI: a freshly decorated Raya living room with new curtains (no people)"),
      "A3": (["S3", "ataupun"], ["S3", "end"], "AI: an old faded wet kitchen mat by the sink (no people)"),
      "A4": (["S15", "start"], ["S15", "korang"], "AI: a clean bright kitchen made over for Raya (no people)")}
photos = [{"id": k, "from": f, "to": t, "note": n} for k, (f, t, n) in AI.items() if (P / f"assets/photos/{k}.jpg").exists()]
write(P, 1, "VID_20261114_172736 (tools/prep.py)", segs, zoom=1.25, origin="68% 50%",
      broll=[cu("C1", ["S4", "alas"], ["S4", "end"], bt("172847", 0.5), "50% 50%", (1.0, 1.06), "the mat on the kitchen floor"),
             cu("C2", ["S6", "dia#2"], ["S6", "end"], bt("172847", 24.5), "50% 50%", (1.0, 1.06), "the tile pattern close up"),
             cu("C3", ["S7", "start"], ["S7", "bawah"], bt("172847", 20.3), "50% 50%", (1.0, 1.05), "a hand on the soft top"),
             cu("C4", ["S7", "bawah"], ["S7", "end"], bt("172847", 10.3), "50% 50%", (1.0, 1.05), "flipping the mat: the black rubber base"),
             cu("C5", ["S11", "start"], ["S11", "tak"], bt("172847", 18.0), "50% 50%", (1.0, 1.06), "the mat edge lifted — its thickness"),
             cu("C6", ["S12", "pelbagai"], ["S12", "end"], bt("172847", 38.5), "50% 50%", (1.0, 1.05), "the mat on the floor"),
             cu("C7", ["S16", "pilih"], ["S16", "dan"], bt("172847", 46.0), "50% 50%", (1.0, 1.05), "the mat on the floor")]
            + ([] if (P / "assets/photos/A4.jpg").exists() else [cu("C8", ["S15", "start"], ["S15", "korang"], bt("172847", 2.0), "50% 50%", (1.0, 1.05), "the mat in the kitchen")]),
      photos=photos,
      kps=[kp("JANGAN TUNGGU RAYA!", ["RAYA!"], ["S1", "start"], ["S1", "end"], "zoom", 120, 100)],
      note_extra=" 14 Nov: caption style kept; motion text themed after the product (black-and-white tile mat); AI visuals where needed.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "pill", "from": ["S2", "time-time"], "to": ["S2", "mesti"], "text": "TETAMU RAMAI DATANG", "x": 60, "y": 250},
    {"type": "pill", "from": ["S2", "mesti"], "to": ["S2", "end"], "text": "DAPUR NAMPAK KEMAS", "x": 60, "y": 250},
    {"type": "tags", "from": ["S3", "langsir"], "to": ["S3", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "LANGSIR DAH TUKAR", "at": ["S3", "langsir"]}, {"text": "RUMAH DAH CANTIK", "at": ["S3", "rumah"]},
        {"text": "ALAS KAKI KUSAM?", "at": ["S3", "ataupun"]}]},
    {"type": "pill", "from": ["S4", "teknologi"], "to": ["S4", "end"], "text": "TEKNOLOGI TERKINI", "x": 60, "y": 250},
    {"type": "hud", "from": ["S6", "mudah"], "to": ["S6", "end"], "title": "DESIGN", "value": "SERAP AIR", "sub": "CEPAT KERING", "x": 60, "y": 150},
    {"type": "tags", "from": ["S7", "start"], "to": ["S7", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "ATAS LEMBUT", "at": ["S7", "start"]}, {"text": "BAWAH GETAH", "at": ["S7", "bawah"]},
        {"text": "ANTI-SLIP", "at": ["S7", "anti-slip."]}]},
    {"type": "pill", "from": ["S8", "start"], "to": ["S8", "end"], "text": "TOLAK PUN TAK BERGERAK", "x": 60, "y": 250},
    {"type": "pill", "from": ["S9", "jadi"], "to": ["S9", "end"], "text": "FIRM BILA JALAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["S10", "ada"], "to": ["S10", "kalau"], "text": "PELBAGAI DESIGN", "x": 60, "y": 250},
    {"type": "pill", "from": ["S10", "kalau"], "to": ["S10", "end"], "text": "DESIGN ESTETIK", "x": 60, "y": 250},
    {"type": "dial", "from": ["S11", "3mm"], "to": ["S11", "end"], "n": 3, "label": "MM TEBAL", "x": 540, "y": 330},
    {"type": "pill", "from": ["S12", "so#2"], "to": ["S12", "end"], "text": "IKUT TEMA RUMAH", "x": 60, "y": 250},
    {"type": "hud", "from": ["S13", "harga"], "to": ["S13", "end"], "title": "HARGA", "value": "MURAH", "sub": "TAK SAMPAI RM20", "x": 60, "y": 150},
    {"type": "pill", "from": ["S14", "start"], "to": ["S14", "jangan"], "text": "PROMO HABIS-HABISAN", "x": 60, "y": 250},
    {"type": "pill", "from": ["S14", "jangan"], "to": ["S14", "korang"], "text": "TAKUT-TAKUT HABIS", "x": 60, "y": 250},
    {"type": "pill", "from": ["S15", "start"], "to": ["S15", "end"], "text": "MAKE OVER DAPUR SEBELUM RAYA", "x": 60, "y": 250},
    {"type": "promo", "from": ["S16", "start"], "to": ["S16", "end"], "tag": "BEG KUNING", "title": "HARGA PROMO", "sub": "PILIH DESIGN & SAIZ", "y": 200},
]
e["_note"] = ("SuperSave Alas Kaki Dapur #1 — assets/a.mp4 built by tools/prep.py from VID_20261114_172736 (talking, picture synced, "
              "zoomed toward the owner). Cutaways: VID_20261114_172847 (mat B-roll) and realistic AI photos when tools/gen.sh "
              "could run (assets/photos/A1-A4, 'ILUSTRASI AI'). Clip -> video: both clips -> this video. Dropped: " + T["dropped"] +
              ". Price only as the owner says it ('tak sampai 20 ... silap-silap 10 pun tak sampai'); promo in his words.")
e["theme"] = {"key": "#111111", "brand": "#FFFFFF"}
e["fx_theme"] = "tile"
e["fs_style"] = "cut"
e["mirror"] = False   # rear camera: the box reads correctly
e["brand_words"] = ["supersave"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
