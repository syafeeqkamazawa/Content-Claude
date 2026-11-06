"""EDL for jubah-hitam-3 (VID_20261107_020132), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 42%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner wearing the jubah (fabric / sleeve)", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 13.85, 23.05, "Serius, aku rasa sangat berbaloi dengan harga yang kau tengok dekat beg kuning tu, aku dapat kualiti macam ni, memang aku rasa sangat puas hati.", "HOOK — first take (5.2-13.6) dropped"),
    seg("S02", 23.38, 24.58, "Sangat selesa guys."),
    seg("S03", 25.58, 27.10, "Kain dia sejuk tau."),
    seg("S04", 28.44, 35.65, "Dan kau tak rasa panas, tak tebal sangat, tak nipis sangat, just nice. Lengan 3 suku, senang nak ambil wuduk guys."),
    seg("S05", 37.66, 48.40, "Korang nak buat raya pun, pada aku memang ngam. Nak pergi solat jemaah, lagi cantik. Solat Jumaat pun memang kemas."),
    seg("S06", 49.82, 55.85, "Yang mana berkenan, dalam beg kuning tu rasanya ada pilihan warna juga, tengok dekat beg kuning.", "first take (49.9-51.1) dropped"),
    seg("S07", 55.86, 61.66, "Harga tu seller tengah buat promo ni, lagi-lagi sekarang ni tengah promosi 11.11."),
    seg("S08", 62.04, 66.60, "Cuba tengok dekat beg kuning berapa harga korang dapat, kalau tengah murah tu korang check out terus."),
    seg("S09", 72.56, 77.92, "Yang aku pakai ni saiz L, berat aku 76 kg, tinggi 165 cm.", "unclear tail (78.6-80.7) left out"),
    seg("S10", 68.04, 72.38, "Sementara stok masih ada, harga tengah murah tu, terus check out."),
    seg("S11", 81.44, 82.56, "So dapatkan di beg kuning.", "CTA", 1.04),
]
broll = [cu("C1", ["S03", "start"], ["S04", "nice."], 25.6, "50% 45%"),
         cu("C2", ["S09", "start"], ["S09", "end"], 72.6, "50% 55%", (1.2, 1.3))]
photos = [ph("raya", ["S05", "start"], ["S05", "pergi"], "AI: Hari Raya (tiada orang)"),
          ph("jemaah", ["S05", "pergi"], ["S05", "solat#2"], "AI: solat jemaah (lelaki berpakaian penuh, dari belakang)"),
          ph("jumaat", ["S05", "solat#2"], ["S05", "end"], "AI: masjid hari Jumaat (tiada orang)")]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1380}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Jubah hitam ada 3 video' — Drive folder 'Jubah Hitam' (1qxVqw_2…): 015650 → #1, 015936 → #2, 020132 → #3, one video per clip. Caption: the 6 Nov default at ~72% height (the owner is filmed full-body, so the face sits high; same placement as Kurta Zeke). Overlays on every explanation (owner 6 Nov): close-ups of the owner wearing the jubah first; realistic AI photos for solat jemaah (men fully covered, from behind), a mosque on Friday and a Hari Raya table.",
     "_note": "Jubah Hitam #3 — A-roll assets/a.mp4 = VID_20261107_020132 (rear camera, not mirrored). assets/b.mp4 = the same clip, muted. Price / promo 11.11 / stock talk are the owner's own words; no price shown. Size note (L, 165 cm, 76 kg) is the owner's own.",
     "segments": segs,
     "punch": [],
     "broll": broll,
     "photos": photos,
     "theme": {"key": "#C9A227", "brand": "#E9E9E9"},
     "brand_words": [], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
