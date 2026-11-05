"""EDL for kurma-ajwa-quba-3 (VID_20261105_114618), 5 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
O = 0.0  # assets/a.mp4 = VID_20261105_114618 only


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": round(x, 2), "out": round(y, 2), "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, sid, x, origin="55% 62%", push=(1.6, 1.75)): return {"id": i, "from": [sid, "start"], "to": [sid, "end"], "src": round(x, 2), "note": "close-up of the owner's hands / dates (same moment)", "push": list(push), "origin": origin}


segs = [
    seg("S01", 3.20, 13.95, "Kurma Ajwa tengah buat promosi! Abang-abang, akak-akak, pak cik, mak cik, ayah-ayah, ibu-ibu semua, rugi tau kalau tak beli, sebab kita dah nak masuk bulan Ramadan, tak lama dah tau, bulan dua.", "HOOK"),
    seg("S02", 14.60, 22.95, "Dah Ramadan dah. Sekarang 11, 12, 1, sekejap sangat. Kalau tengok ni, Kurma Ajwa ni grade A tau, satu kilo yang saya ambil ni."),
    seg("S03", 23.20, 25.65, "Dia punya tekstur sangat-sangat sedap."),
    seg("S04", 62.00, 64.90, "Kurma ni, kurma grade A tau.", "unclear lines 26-61 dropped"),
    seg("S05", 74.30, 76.90, "Bismillahirrahmanirrahim.", "eating", keep_pauses=True),
    seg("S06", 79.30, 85.50, "Sedap, berlemak. Rugi sangat, Kurma Ajwa ni, rugi sangat kalau tak grab."),
    seg("S07", 86.70, 91.30, "Kurma Ajwa by Quba Food, memang sangat best.", "repeated 'Kurma Ajwa memang best' takes dropped"),
    seg("S08", 107.76, 110.20, "Kalau berminat, boleh tekan beg kuning kat bawah."),
    seg("S09", 111.85, 114.95, "Sekarang ni ramai seller dah tengah buat promo 11.11 tau."),
    seg("S10", 115.40, 119.65, "Cuba tengok dekat beg kuning, berapa harga korang dapat. Kalau tengah murah tu, beli sekarang.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 3, "chars": 18, "highlight": True, "on": "#3DD6F5", "top": 1690, "size": 58}, "fs_style": "cut", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "5 Nov: 'Buat overlay yang perlu sahaja atau closeup bila explain tentang produk. Ada satu lagi video kurma' — two new talking clips in Drive folder 17vMTWca…; owner then: 'Kurma Ajwa sepatutnya ada satu lagi' — one video per clip: this is VID_20261105_114618, #2 is VID_20261105_113237. Overlays are only close-ups of the owner's own hands and the dates while he explains them; no AI photos. Captions as Kurma Ajwa #1 (2-3 upper-case words, spoken word light blue).",
     "_note": "Kurma Ajwa #3 — A-roll assets/a.mp4 = VID_20261105_114618 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted; close-ups play the same moment zoomed into the hands. Clip -> video: 113237 -> #2, 114618 -> #3 (no part in both). Dropped: repeated takes, the unclear lines (26-61, 65-73, 92-107), filler haa. Promo 11.11, grade A 1 kg and the Ramadan line are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S10", "beli", 1.06]],
     "broll": [cu("C1", "S03", 23.20), cu("C2", "S04", 62.00)],
     "photos": [],
     "theme": {"key": "#3DD6F5", "brand": "#E9C46A"},
     "brand_words": ["ajwa"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
