"""EDL for kurma-ajwa-quba-2 (VID_20261105_114618 + VID_20261105_113237), 5 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
O = float((P / '.media/offset.txt').read_text())  # 113237 starts here in assets/a.mp4


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": round(x, 2), "out": round(y, 2), "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, sid, x, origin="55% 62%", push=(1.6, 1.75)): return {"id": i, "from": [sid, "start"], "to": [sid, "end"], "src": round(x, 2), "note": "close-up of the owner's hands / dates (same moment)", "push": list(push), "origin": origin}


segs = [
    seg("S01", 3.20, 13.95, "Kurma Ajwa tengah buat promosi! Abang-abang, akak-akak, pak cik, mak cik, ayah-ayah, ibu-ibu semua, rugi tau kalau tak beli, sebab kita dah nak masuk bulan Ramadan, tak lama dah tau, bulan dua.", "HOOK (114618)"),
    seg("S02", 14.60, 22.95, "Dah Ramadan dah. Sekarang 11, 12, 1, sekejap sangat. Kalau tengok ni, Kurma Ajwa ni grade A tau, satu kilo yang saya ambil ni."),
    seg("S03", O + 13.00, O + 20.00, "Kalau awak tengah cari kurma Ajwa yang harga murah, boleh beli daripada Quba Food ni. Kualiti memang premium tau.", "113237 from here"),
    seg("S04", O + 23.80, O + 28.50, "Memang puas hati, kurma dia sangat sedap."),
    seg("S05", O + 36.20, O + 43.50, "Kurma dia memang sangat sedap, gemuk-gemuk, nampak ni besar-besar tau, hitam je. Saiz dia saiz grade A tau."),
    seg("S06", O + 69.90, O + 78.60, "Tahu tak kenapa saya suka sangat kurma ni? Sangat lembut tau kurma dia. Tengoklah. Bismillahirrahmanirrahim.", "eating"),
    seg("S07", O + 80.10, O + 88.30, "Kurma Ajwa, memang tak mengecewakan. Masya-Allah, tengoklah dia punya texture dia."),
    seg("S08", O + 90.20, O + 100.50, "Nampak tak? Memang sangat sedap. Juicy, tak kering. Lepas tu dia bersih tau."),
    seg("S09", O + 121.90, O + 125.10, "Lembut, lepas tu bersih je, dekat bahagian dalam ni tak ada habuk pun."),
    seg("S10", O + 126.10, O + 128.90, "Rasa dia sangat sedap, manis berlemak.", "the unclear 'kalau makan dengan …' line (143.6) dropped"),
    seg("S11", O + 150.00, O + 156.00, "Awak pergilah beli dengan seller ni, paling murah."),
    seg("S12", O + 156.30, O + 174.20, "Yang saya beli ni, yang saya dapat, yang ada dengan saya ni satu kg tau, dapat dalam bentuk pek besar macam ni. Gemuk-gemuk je, grade A, harga dia antara yang termurah tau. Pergi beli cepat, berebut orang beli ni."),
    seg("S13", 86.70, 91.30, "Kurma Ajwa by Quba Food, memang sangat best.", "back to 114618"),
    seg("S14", 110.60, 114.95, "Sekarang ni ramai seller dah tengah buat promo 11.11 tau."),
    seg("S15", 115.40, 119.65, "Cuba tengok dekat beg kuning, berapa harga korang dapat. Kalau tengah murah tu, beli sekarang.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 3, "chars": 18, "highlight": True, "on": "#3DD6F5", "top": 1690, "size": 58}, "fs_style": "cut", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "5 Nov: 'Buat overlay yang perlu sahaja atau closeup bila explain tentang produk. Ada satu lagi video kurma' — two new talking clips in Drive folder 17vMTWca… joined into one video: the hook and CTA from VID_20261105_114618, the product explanation from VID_20261105_113237. Overlays are only close-ups of the owner's own hands and the dates while he explains them; no AI photos. Captions as Kurma Ajwa #1 (2-3 upper-case words, spoken word light blue).",
     "_note": "Kurma Ajwa #2 — A-roll assets/a.mp4 = VID_20261105_114618 then VID_20261105_113237 from .media/offset.txt (front camera, mirrored back in CSS). assets/b.mp4 = the same joined clip flipped and muted; close-ups play the same moment zoomed into the hands. Dropped: repeated 'Kurma Ajwa memang best' takes, the unclear lines (113237 29-35 and 143-149), filler 'haa'. Promo 11.11, 'paling murah / termurah' and 'grade A, 1 kg' are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S15", "beli", 1.06]],
     "broll": [cu("C1", "S05", O + 36.20), cu("C2", "S07", O + 80.10), cu("C3", "S08", O + 90.20), cu("C4", "S09", O + 121.90), cu("C5", "S12", O + 156.30, "50% 70%", (1.35, 1.5))],
     "photos": [],
     "theme": {"key": "#3DD6F5", "brand": "#E9C46A"},
     "brand_words": ["ajwa"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
