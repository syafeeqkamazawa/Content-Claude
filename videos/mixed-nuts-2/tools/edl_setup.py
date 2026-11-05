"""EDL for mixed-nuts-2 (VID_20261105_110040 + 110249, pouch shots from 110137), 5 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
O = 63.622  # 110249 starts here in assets/a.mp4


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": round(x, 2), "out": round(y, 2), "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.35), origin="45% 70%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 6.30, 13.80, "Bagi yang baru order kacang mixed nuts ni, ataupun yang tengah jaga makan, kalau nak sedap, korang campurkan dengan susu full cream ataupun dengan yogurt.", "HOOK (110040)"),
    seg("S02", 14.00, 20.10, "Kadang-kadang bila nak kudap waktu malam tu, nak kena makan Maggi. Tapi sekarang ni dah ada kacang yang sihat macam ni."),
    seg("S03", 25.00, 31.50, "Dalam dia pun ada kismis, badam, gajus. Yang penting, protein dia pun tinggi tau.", "'ada kismis' false start (20.4) dropped"),
    seg("S04", O + 15.10, O + 18.55, "Lagi satu, harga dia murah je tau untuk satu pack 500 gram macam ni.", "110249 take 3 (110040 35-43 and 110249 takes 1-2 dropped)"),
    seg("S05", O + 34.20, O + 40.90, "Untuk yang baru nak try, sekarang ni aku suggestkan korang beli dua. Sebab apa? Sebab seller tengah buat offer. Lagi-lagi yang tengah jaga makan tu,", "takes 110249 18.9-32.3 dropped"),
    seg("S06", O + 41.10, O + 43.60, "kacang mixed nuts macam ni memang sesuai untuk korang."),
    seg("S07", O + 55.10, O + 60.36, "Sekarang ni pun dah ramai seller tengah buat promo 11.11 tau. Cuba korang tengok beg kuning, berapa harga korang dapat.", "takes 48.2-53.1 dropped"),
    seg("S08", O + 60.40, O + 63.15, "Kalau tengah murah tu, jangan tunggu lagi. Beli terus.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": False, "caption_style": "word2", "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "5 Nov: Drive folder 1PmTRs8K… 'Mixed Nuts' — the second content is several files joined: VID_20261105_110040 (susu / yogurt, kismis badam gajus) + VID_20261105_110249 (harga 500 g, beli dua, promo, CTA), with the owner's pouch shots from VID_20261105_110137 as B-roll. It follows TikDownloader…7593974540527537416 (Mixed Nuts in a bowl of milk, the same script): product shots for almost the whole video — pouch, open pouch, a bowl of nuts with milk, yogurt, spoon — crossfading, a white rounded text card near the top, and no running subtitles (the reference has none). The reference's 'Reply to … comment' bubble is not faked: the card carries the owner's own line instead. Aurat rule kept.",
     "_note": "Mixed Nuts #2 — A-roll assets/a.mp4 = VID_20261105_110040 0-63.6 + VID_20261105_110249 from 63.622 s (front camera, mirrored back in CSS). B-roll assets/b.mp4 (flipped, muted) = 110137 0-5.5 (pouch to camera, opening) at 0-5.5, 110137 45.5-52.5 (open pouch full of nuts) at 5.5-12.5, 110249 23.3-30 (open pouch, silent) at 12.5-19.2. 105911 is camera set-up only (no usable speech; another person walks in) and is not used. Claims are the owner's own words (kismis, badam, gajus, protein tinggi, 500 g, beli dua, promo 11.11); no price.",
     "segments": segs,
     "pin": {"text": "Campur dengan susu full cream atau yogurt, baru sedap!", "y": 300, "size": 40, "card": True},
     "punch": [["S08", "beli", 1.06]],
     "broll": [br("B1", ["S01", "start"], ["S01", "ataupun"], 0.6, "110137: pouch ke kamera", (1.8, 1.95), "55% 100%"),
               br("B2", ["S01", "ataupun"], ["S01", "susu"], 6.5, "110137: pouch terbuka penuh kacang (guna produk)", (1.8, 1.95), "62% 100%"),
               br("B3", ["S02", "tapi"], ["S02", "end"], 13.0, "110249: kacang dalam pouch", (1.8, 1.95), "88% 100%"),
               br("B4", ["S04", "start"], ["S04", "end"], 1.5, "110137: pouch depan (500 g)", (1.8, 1.95), "55% 100%"),
               br("B5", ["S05", "sebab"], ["S05", "end"], 15.5, "110249: pouch terbuka", (1.8, 1.95), "60% 100%"),
               br("B6", ["S07", "start"], ["S07", "end"], 8.5, "110137: kacang dalam pouch (guna produk)", (1.8, 1.95), "68% 100%")],
     "photos": [ph("susu", ["S01", "susu"], ["S01", "yogurt"], "AI: mangkuk kacang dengan susu"),
                ph("yogurt", ["S01", "yogurt"], ["S01", "end"], "AI: yogurt dengan kacang"),
                ph("maggi", ["S02", "start"], ["S02", "tapi"], "AI: makan mi segera waktu malam"),
                ph("kacang", ["S03", "start"], ["S03", "end"], "AI: kismis, badam, gajus"),
                ph("sudu", ["S06", "start"], ["S06", "end"], "AI: sudu kacang dalam susu")],
     "theme": {"key": "#E9A23B", "brand": "#FFFFFF"},
     "brand_words": [], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
