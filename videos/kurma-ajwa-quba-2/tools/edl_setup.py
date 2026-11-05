"""EDL for kurma-ajwa-quba-2 (VID_20261105_113237), 5 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
O = 0.0  # assets/a.mp4 = VID_20261105_113237 only


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": round(x, 2), "out": round(y, 2), "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, sid, x, origin="55% 62%", push=(1.6, 1.75)): return {"id": i, "from": [sid, "start"], "to": [sid, "end"], "src": round(x, 2), "note": "close-up of the owner's hands / dates (same moment)", "push": list(push), "origin": origin}


segs = [
    seg("S01", 13.00, 20.14, "Kalau awak tengah cari kurma Ajwa yang harga murah, boleh beli daripada Quba Food ni. Kualiti memang premium tau.", "HOOK"),
    seg("S02", 23.80, 28.50, "Memang puas hati, kurma dia sangat sedap."),
    seg("S03", 36.20, 43.50, "Kurma dia memang sangat sedap, gemuk-gemuk, nampak ni besar-besar tau, hitam je. Saiz dia saiz grade A tau."),
    seg("S04", 69.90, 79.06, "Tahu tak kenapa saya suka sangat kurma ni? Sangat lembut tau kurma dia. Tengoklah. Bismillahirrahmanirrahim.", "eating"),
    seg("S05", 80.10, 88.30, "Kurma Ajwa, memang tak mengecewakan. Masya-Allah, tengoklah dia punya texture dia."),
    seg("S06", 90.20, 100.66, "Nampak tak? Memang sangat sedap. Juicy, tak kering. Lepas tu dia bersih tau."),
    seg("S07", 126.10, 128.90, "Rasa dia sangat sedap, manis berlemak."),
    seg("S08", 153.43, 156.00, "Awak pergilah beli dengan seller ni, antara yang termurah tau.", "first take 150.0 dropped"),
    seg("S09", 156.30, 174.20, "Yang saya beli ni, yang saya dapat, yang ada dengan saya ni satu kg tau, dapat dalam bentuk pek besar macam ni. Gemuk-gemuk je, grade A, harga dia antara yang termurah tau. Pergi beli cepat, berebut orang beli ni."),
    seg("S10", 180.70, 182.85, "Dah ramai seller buat promo 11.11 tau.", "first take 176.9 dropped"),
    seg("S11", 183.30, 188.15, "Cuba tengok dekat beg kuning, kalau harga tengah murah tu, boleh buat stok awal-awal.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 3, "chars": 18, "highlight": True, "on": "#3DD6F5", "top": 1690, "size": 58}, "fs_style": "cut", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "5 Nov: 'Buat overlay yang perlu sahaja atau closeup bila explain tentang produk. Ada satu lagi video kurma' — two new talking clips in Drive folder 17vMTWca…; owner then: 'Kurma Ajwa sepatutnya ada satu lagi' — one video per clip: this is VID_20261105_113237, #3 is VID_20261105_114618. Overlays are only close-ups of the owner's own hands and the dates while he explains them; no AI photos. Captions as Kurma Ajwa #1 (2-3 upper-case words, spoken word light blue).",
     "_note": "Kurma Ajwa #2 — A-roll assets/a.mp4 = VID_20261105_113237 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted; close-ups play the same moment zoomed into the hands. Clip -> video: 113237 -> #2, 114618 -> #3 (no part in both). Dropped: repeated takes, the unclear lines (29-35, 121.9-125.1, 143-149), filler haa. Promo 11.11, termurah, grade A 1 kg are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S11", "stok", 1.06]],
     "broll": [cu("C1", "S03", 36.20), cu("C2", "S05", 80.10), cu("C3", "S06", 90.20), cu("C4", "S09", 156.30, "50% 70%", (1.35, 1.5))],
     "photos": [],
     "theme": {"key": "#3DD6F5", "brand": "#E9C46A"},
     "brand_words": ["ajwa"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
