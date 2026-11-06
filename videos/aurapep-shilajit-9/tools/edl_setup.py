"""EDL for aurapep-shilajit-9 (VID_20261106_172057), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="55% 60%", push=(1.3, 1.45)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own Shilajit bottle", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 5.40, 9.60, "Sekarang ni tengah viral guys, Shilajit daripada Aurapep ni.", "HOOK — the 'dikatakan dapat bantu support dan boost stamina' claim (9.5-21.8, two takes) dropped: TikTok health-claim risk (owner 5 Nov)"),
    seg("S02", 33.55, 41.55, "Ramai dah cuba Aurapep Shilajit Complex Tablet ni dan kebanyakannya feedback yang sangat baik.", "earlier takes (22.5-27.3, 31.8-33.5) dropped"),
    seg("S03", 44.45, 49.18, "Tetapi macam mana kita nak pilih Shilajit yang berkualiti dalam pasaran sekarang?"),
    seg("S04", 50.35, 58.38, "Ini yang saya nak share kepada anda semua, Shilajit Complex Tablet daripada Aurapep ni, sebab sangat berkualiti.", "false start 'saya nak share' dropped"),
    seg("S05", 58.30, 62.55, "Ada kelulusan daripada KKM dan juga Halal JAKIM."),
    seg("S06", 67.15, 70.92, "Mengandungi Shilajit, magnesium, zinc dan juga ganoderma.", "'yang semuanya dapat bantu support boost stamina kita, tambah-tambah untuk tenaga dalam' (70.8-76.1) dropped: TikTok health-claim risk"),
    seg("S07", 76.32, 81.75, "Dalam satu botol ni ada 60 tablet, satu hari cukup kita makan satu tablet sahaja."),
    seg("S08", 82.00, 92.72, "Sekarang harga tengah murah tau, tengah promo yang banyak dekat beg kuning. Kenapa? Sebab sekarang ni promotion 11.11 pun dah mula berjalan, seller tengah buat harga special dekat beg kuning."),
    seg("S09", 97.90, 101.35, "Kepada kawan-kawan, abang-abang, pakcik-pakcik, ayah-ayah,", "stumble 'kepada kawan-kawan, ibu' dropped"),
    seg("S10", 103.40, 105.00, "dapatkan segera dekat beg kuning.", "'yang ada masalah yang sama nak mencuba' dropped: implies a health problem"),
    seg("S11", 105.02, 119.60, "Stok baru habis baru ni, sekarang dia dah restock balik. Sementara stok ada tu dan harga masih dalam promosi, grab awal-awal.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Aurapep Shilajit, Drive folder 12AIw3W3… — clip 172057 → #9 (170843 → #7, 171623 → #8). Caption: the 6 Nov default on the wall above the head (top 300). Overlays on every explanation (owner 6 Nov): close-ups of the owner's own bottle first; realistic AI photos (no people / one long-sleeved hand) for the crowded supplement shelf, ganoderma and the one-tablet dose. Stamina / 'tenaga dalam' / 'masalah yang sama' lines dropped (owner 5 Nov: no TikTok-risk health claims).",
     "_note": "Aurapep Shilajit #9 — A-roll assets/a.mp4 = VID_20261106_172057 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Promo 11.11 / restock / 'feedback sangat baik' are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S11", "grab", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S02", "end"], 33.55, "60% 62%"),
               cu("C2", ["S04", "start"], ["S05", "end"], 52.0, "58% 62%"),
               cu("C3", ["S07", "start"], ["S07", "satu#2"], 76.4, "60% 62%"),
               cu("C4", ["S09", "start"], ["S10", "end"], 98.0, "58% 62%")],
     "photos": [ph("rak", ["S03", "start"], ["S03", "end"], "AI: rak suplemen di farmasi (tanpa jenama)"),
                ph("ganoderma", ["S06", "start"], ["S06", "end"], "AI: ganoderma"),
                ph("dos", ["S07", "satu#2"], ["S07", "end"], "AI: satu tablet sehari (tangan berlengan panjang)")],
     "theme": {"key": "#C9A227", "brand": "#E9E9E9"},
     "brand_words": ["shilajit", "aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
