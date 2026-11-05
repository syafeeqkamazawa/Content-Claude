"""EDL for mixed-nuts-3 (VID_20261105_112003), 5 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
# Close-ups are the same moment of the owner's own clip (assets/b.mp4 = the A-roll flipped, muted), zoomed into his hands.
def cu(i, sid, x, origin="55% 60%", push=(1.7, 1.85)): return {"id": i, "from": [sid, "start"], "to": [sid, "end"], "src": x, "note": "close-up of the owner's hands / product (same moment)", "push": list(push), "origin": origin}


segs = [
    seg("S01", 16.00, 20.00, "Ya Allah sedapnya, ya Allah sedapnya.", "HOOK — owner eating the nuts", keep_pauses=True),
    seg("S02", 26.30, 33.25, "Kepada siapa yang tengah cari kudapan-kudapan sihat, nak makan malam-malam tu, korang boleh cuba mix nuts ni tau.", "first take 20.3 dropped"),
    seg("S03", 39.60, 44.70, "Macam yang saya beli dekat TikTok Shop ni. Mixed nuts ni, kacang campur tau.", "two false starts 34.8-38.9 dropped"),
    seg("S04", 45.10, 49.70, "Dalam ni ada tujuh jenis kacang berlainan"),
    seg("S05", 54.60, 56.10, "yang boleh kita makan terus.", "repeat 'yang boleh kita terus makan' dropped"),
    seg("S06", 70.30, 77.20, "Yang awak tengok saya pegang ni, setengah kilo tau, memang sangat banyak. Awak tengok dalam ni, memang banyak, berat tau.", "first take 59.1 dropped"),
    seg("S07", 87.00, 89.50, "Ini saya ambil lagi. Bismillahirrahmanirrahim.", "eating"),
    seg("S08", 90.20, 94.95, "Sedap, memang sedap. Ada macam-macam kacang dalam ni."),
    seg("S09", 112.60, 116.40, "Yang hijau-hijau semua ni biji labu tau.", "first take 108.3 dropped"),
    seg("S10", 116.90, 118.60, "InsyaAllah sedap.", "'lepas tu ada kacang almond juga' — said again at 126.4, kept there"),
    seg("S11", 126.40, 131.80, "Okey, ada kacang almond, lepas tu biji bunga matahari."),
    seg("S12", 132.20, 133.50, "Ada kismis."),
    seg("S13", 142.20, 143.14, "Manis, sedap."),
    seg("S14", 145.30, 146.95, "Lepas tu ada cranberry juga."),
    seg("S15", 150.78, 152.20, "Kalau beli ni, mesti nak repeat ni.", "repeated 'kalau beli ni' (149.4) dropped"),
    seg("S16", 157.10, 160.94, "Kacang dia segar-segar tau, tak ada langsung masuk angin ke apa."),
    seg("S17", 169.00, 171.70, "Rasa sedap, rangup krispi, rasa original."),
    seg("S18", 172.80, 174.95, "Tak ada langsung perisa tambahan."),
    seg("S19", 183.88, 189.00, "Siapa yang tengah cari makanan sihat tu untuk kudap-kudap malam, awak cubalah beli mix nuts ni, okey."),
    seg("S20", 192.80, 195.25, "Memang elok tau, beli setengah kilo terus, jimat.", "repeat of the same line dropped"),
    seg("S21", 197.50, 200.60, "Sekarang ni pun banyak seller tengah buat promo tau, 11.11 punya promo.", "false start 196 dropped"),
    seg("S22", 201.00, 205.65, "Cuba tengok dekat beg kuning, ada voucher ke tak, boleh claim. Kalau harga tengah murah tu, boleh beli terus.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 3, "chars": 18, "highlight": False, "box": True, "top": 1770, "size": 40}, "fs_style": "cut", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "5 Nov: 'Mixed Nuts ada satu lagi video ya … Buat overlay yang perlu sahaja atau closeup bila explain tentang produk' (reference TikDownloader…7466063042132888839: talking head with the product, close-ups of the nuts in hand). Overlays here are only close-ups of the owner's own hands and the nuts at the moments he explains the product (seven kinds, half a kilo, biji labu, almond, biji bunga matahari, kismis, cranberry, fresh and crispy); no AI photos. Captions as Mixed Nuts #1: small 2-3-word captions on a dark box below the product, plus a fixed line at the top.",
     "_note": "Mixed Nuts #3 — A-roll assets/a.mp4 = VID_20261105_112003 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted; each close-up plays the same moment zoomed into the owner's hands. All points kept; takes, false starts and repeats dropped. Promo 11.11 is the owner's own words; no price.",
     "segments": segs,
     "pin": {"text": "Mixed nuts kacang campur, 7 jenis dalam satu pek, setengah kilo!", "y": 330, "size": 40},
     "punch": [["S22", "beli", 1.06]],
     "broll": [cu("C1", "S04", 45.10), cu("C2", "S06", 70.30, "55% 70%", (1.5, 1.65)), cu("C3", "S09", 112.60), cu("C4", "S11", 126.40),
               cu("C5", "S12", 132.20), cu("C6", "S14", 145.30), cu("C7", "S16", 157.10), cu("C8", "S17", 169.00)],
     "photos": [],
     "theme": {"key": "#FFFFFF", "brand": "#E9C46A"},
     "brand_words": [], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
