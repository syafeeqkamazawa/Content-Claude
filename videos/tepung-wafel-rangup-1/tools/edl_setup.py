"""EDL for tepung-wafel-rangup-1 (13 Nov). Run tools/prep.py first. Same look as jus-gout-14 / kurma-ajwa-quba-6:
talking clip kept, motion text (EDL "fx") + plain one-word caption from the Jus Gout 'video contoh', visual overlays
(the owner's own B-roll: mixing the batter, the waffle on the plate, eating it)."""
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
FIX = {"wafer": "waffle", "bergurut": "berebut", "-gurut": "-rebut", "tiba": "tipu", "bali": "kuali", "bayi": "beg",
       "naikkan": "naik"}


def words(path, offset=0.0):
    out = []
    for line in (P / path).read_text().splitlines():
        for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
            core = w.rstrip('.,?!')
            if core.lower() in FIX:
                w = FIX[core.lower()] + w[len(core):]
            out.append((w, float(s) + offset, float(e) + offset))
    return out


SW = {"t": words(".media/wl-084758.txt"), "h": words(".media/wl-092656.txt")}
tr = []
for lid, d in L.items():
    acc = d["e0"]
    for a, b in d["pieces"]:
        for w, s, e in SW[d["src"]]:
            if a <= s < b and e - s < 1.6:
                tr.append({"w": w, "s": round(acc + s - a, 3), "e": round(acc + min(e, b) - a, 3)})
        acc += b - a
TR = json.dumps(tr, ensure_ascii=False)

NOTES = {"T1": "HOOK — 084758 28-36.6 (first 'anak-anak' stutter dropped)", "H1": "VID_20261113_092656 — opens the waffle maker",
         "T12": "CTA"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 1, "VID_20261113_084758 + VID_20261113_092656 (tools/prep.py)", segs, zoom=1.0, origin="50% 40%",
      broll=[cu("C1", ["T3", "memang"], ["T3", "end"], bt("095912", 82.0), "50% 45%", (1.0, 1.06), "owner eating the waffle"),
             cu("C2", ["T6", "start"], ["T6", "ni"], bt("095912", 52.0), "50% 55%", (1.0, 1.06), "holding up a piece of waffle"),
             cu("C3", ["T7", "campur#2"], ["T7", "lepas"], bt("091202", 2.0), "50% 50%", (1.0, 1.06), "batter in the bowl, top view"),
             cu("C4", ["T7", "lepas"], ["T7", "end"], bt("091251", 12.0), "50% 50%", (1.0, 1.06), "stirring the batter"),
             cu("C5", ["T8", "start"], ["T8", "end"], bt("091338", 6.0), "50% 50%", (1.0, 1.06), "batter ready"),
             cu("C6", ["T9", "memang"], ["T9", "end"], bt("095912", 64.0), "50% 50%", (1.0, 1.05), "the waffle in hand"),
             cu("C7", ["T10", "buat"], ["T10", "end"], bt("092709", 0.0), "50% 50%", (1.0, 1.08), "round waffle on the plate"),
             cu("C8", ["T11", "start"], ["T11", "end"], bt("095912", 20.0), "50% 55%", (1.0, 1.06), "cutting the waffle on the plate")],
      kps=[kp("TEPUNG WAFEL RANGUP", ["RANGUP"], ["T1", "start"], ["T1", "bila"], "zoom", 200, 112)],
      note_extra=" 12 Nov: motion text + caption from the Jus Gout 'video contoh'; visual overlays; talking kept.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["word"] = {"font": "Rubik Mono One", "size": 50, "top": 1243, "halo": False}
e["fx"] = [
    {"type": "dial", "from": ["T3", "kedua,"], "to": ["T3", "memang"], "n": 2, "label": "KALI RESTOCK", "x": 300, "y": 330},
    {"type": "pill", "from": ["T4", "packaging"], "to": ["T4", "end"], "text": "PACKAGING BARU", "x": 60, "y": 250},
    {"type": "hud", "from": ["T5", "menunjukkan"], "to": ["T5", "end"], "title": "SAMBUTAN", "value": "HIGH DEMAND", "sub": "RAMAI ORANG BELI", "x": 380, "y": 170},
    {"type": "pill", "from": ["T6", "beli"], "to": ["T6", "end"], "text": "ORANG BELI DUA", "x": 60, "y": 250},
    {"type": "pill", "from": ["T7", "cara"], "to": ["T7", "campur#2"], "text": "CARA MUDAH", "x": 60, "y": 250},
    {"type": "tags", "from": ["T7", "air,"], "to": ["T7", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "AIR", "at": ["T7", "air,"]}, {"text": "MINYAK", "at": ["T7", "minyak"]}, {"text": "TELUR", "at": ["T7", "telur"]}]},
    {"type": "tags", "from": ["T8", "acuan"], "to": ["T8", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "ACUAN WAFFLE", "at": ["T8", "acuan"]}, {"text": "KUALI", "at": ["T8", "kuali"]}]},
    {"type": "pill", "from": ["H1", "kalau"], "to": ["H1", "end"], "text": "NAK GARING? BIAR LAMA", "x": 60, "y": 250},
    {"type": "tags", "from": ["T10", "sarapan,"], "to": ["T10", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "SARAPAN", "at": ["T10", "sarapan,"]}, {"text": "BEKAL SEKOLAH", "at": ["T10", "bekal,"]}]},
    {"type": "tags", "from": ["T11", "start"], "to": ["T11", "end"], "y": 140, "cols": 1, "x0": 60, "dx": 0, "items": [
        {"text": "COKLAT", "at": ["T11", "coklat"]}, {"text": "KAYA", "at": ["T11", "kaya"]}]},
    {"type": "promo", "from": ["T12", "voucher"], "to": ["T12", "end"], "tag": "VOUCHER", "title": "CLAIM DI BEG KUNING", "sub": "SEBELUM HARGA NAIK", "y": 230},
]
e["_note"] = ("Tepung Wafel Rangup #1 — assets/a.mp4 built by tools/prep.py from VID_20261113_084758 (talking) and "
              "VID_20261113_092656 (voiced cooking clip; picture synced). B-roll (assets/b.mp4): 091202, 091251, 091338 "
              "(mixing), 092709 (waffle on plate), 095912 0-100 s (eating). Clip -> video: 084758, 092656, 091202, 091251, "
              "091338, 092709, 095912 (0-100 s) -> this video; 090052, 092819, 092000, 092406, 093613, 095047, 095121, 095912 "
              "(100-203 s) -> electrova-waffle-maker-1. Dropped: " + T["dropped"] + ". No price; voucher / promo are the owner's words.")
e["theme"] = {"key": "#F5A623", "brand": "#FFFFFF"}
e["fs_style"] = "cut"
e["mirror"] = False   # rear camera: the pack reads correctly
e["brand_words"] = ["rangup", "wafel"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
