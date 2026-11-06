"""EDL for kurma-ajwa-quba-5 (VID_20261106_085511), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="55% 55%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's hands / dates / pouch (same moment)", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 47.90, 54.70, "Saya sangat rekomen pada anda semua tau, dapatkan kurma Ajwa, sebab dia tak manis sangat.", "HOOK — the opening pregnancy / HB / constipation lines (0-23) dropped as TikTok health-claim risk; first take 37-46 dropped"),
    seg("S02", 55.30, 59.15, "Bila kita gigit tu, gigi tak sakit tau."),
    seg("S03", 90.20, 92.40, "Cuba tengok, dia punya tekstur dia tu."),
    seg("S04", 97.50, 101.00, "Dia tak lembik sangat, dia tak keras sangat."),
    seg("S05", 102.35, 103.45, "Chewy-chewy macam tu."),
    seg("S06", 105.60, 109.60, "Bismillah. Hmm, sedap.", "eating", keep_pauses=True),
    seg("S07", 115.55, 117.10, "Senang nak jadikan amalan sunnah."),
    seg("S08", 175.40, 179.40, "Amalkan satu hari tujuh biji, ataupun tiga biji makan pagi.", "the 'ibu-ibu jaga dalaman, luaran, tenaga' lines (117-174) dropped as TikTok health-claim risk"),
    seg("S09", 25.00, 35.45, "Yang ada pada saya ni, puasa pun dah tak lama, boleh standby awal-awal. Masya-Allah."),
    seg("S10", 190.00, 192.95, "Yang penting dia punya kualiti, buah dia memang tak berkilat.", "unclear start 'trailer ni pun tak mahal' dropped"),
    seg("S11", 201.29, 202.80, "Buah lembut."),
    seg("S12", 214.55, 217.40, "Plastik pula dia macam ni tau, senang nak bawa.", "repeated 'plastik macam ni' dropped"),
    seg("S13", 218.85, 221.40, "Plastik dia macam ni, senang nak simpan dalam almari."),
    seg("S14", 228.25, 230.75, "Sekarang ni ramai seller dah buat promo 11.11 tau.", "false starts 'sekarang ni promo' (226.9-228.2) and 'ni saya' before S09 dropped"),
    seg("S15", 231.50, 233.80, "Cuba tengok dekat beg kuning, kalau ada voucher claim,", "repeated 'kalau harga tengah murah tu' dropped"),
    seg("S16", 235.90, 239.35, "kalau harga tengah kurang daripada biasa tu, beli awal-awal."),
    seg("S17", 240.25, 241.20, "Dapatkan di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1380}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: new Kurma clip in Drive folder 17vMTWca…. Caption: the 6 Nov default (docs/caption-style-6nov.jpg). Overlays on every explanation (owner 6 Nov) — close-ups of the owner's own hands, dates and pouch; realistic AI photos for berbuka puasa and the 7-dates morning habit. No TikTok-risk lines (owner 5 Nov): the pregnancy / HB / constipation hook and the 'jaga dalaman, luaran, tenaga' lines are dropped.",
     "_note": "Kurma Ajwa #5 — A-roll assets/a.mp4 = VID_20261106_085511 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Promo 11.11 and vouchers are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S17", "dapatkan", 1.06]],
     "broll": [cu("C1", ["S01", "kurma"], ["S01", "end"], 51.5, "55% 55%", (1.3, 1.45)), cu("C2", ["S03", "start"], ["S05", "end"], 90.2, "45% 45%"),
               cu("C3", ["S10", "start"], ["S11", "end"], 190.0, "50% 50%", (1.4, 1.55)), cu("C4", ["S12", "start"], ["S13", "end"], 212.6, "40% 55%", (1.3, 1.45))],
     "photos": [ph("pagi7", ["S07", "start"], ["S08", "end"], "AI: tujuh biji kurma waktu pagi"),
                ph("iftar", ["S09", "puasa"], ["S09", "end"], "AI: hidangan berbuka puasa")],
     "theme": {"key": "#3DD6F5", "brand": "#E9C46A"},
     "brand_words": ["ajwa"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
