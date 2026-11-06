"""EDL for kurta-zeke-1 (VID_20261106_083553), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin, push=(1.7, 1.85), note="close-up of the kurta on the owner (same moment)"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 69.50, 72.50, "Kurta ni kalau korang pakai, memang auto handsome, guys.", "HOOK (moved up)"),
    seg("S02", 5.40, 24.35, "Guys, pakai kurta ni kalau nak pergi kenduri, kalau nak pergi event, ataupun puasa pun dah tak lama kan, nak pergi tarawih pun cantik."),
    seg("S03", 24.35, 36.70, "Pakai kurta daripada Zeke ni. Yang ni jenis V macam ni, lengan tiga suku, nak ambil wuduk pun senang tau. Memang cantik, memang nice."),
    seg("S04", 43.30, 45.80, "Sangat selesa pakai, memang sangat selesa."),
    seg("S05", 49.90, 51.30, "Kain dia ni scuba tau."),
    seg("S06", 59.20, 60.90, "Pakai baju ni, sejuk je rasa.", "first take 54.3 dropped"),
    seg("S07", 80.30, 84.65, "Lepas tu baju ni dia yang licin tau, anti-kedut."),
    seg("S08", 84.65, 87.30, "Kalau buat macam ni pun, kalau buat macam ni je, tu tak nampak kedut dia.", "demo"),
    seg("S09", 100.40, 103.40, "Yang lagi penting, harga dia murah tau. Cuba korang tengok dekat beg kuning.", "'yang lagi penting' stumbles dropped"),
    seg("S10", 108.50, 111.30, "Sekarang ni pun ramai seller dah buat promo 11.11 tau.", "first take 103.9 dropped"),
    seg("S11", 111.70, 113.55, "Cuba tengok dekat beg kuning, harga dia berapa."),
    seg("S12", 155.60, 158.90, "Hari tu, hari tu pernah aku tengok stok habis tau.", "repeated price / promo takes 113.6-151 dropped"),
    seg("S13", 174.75, 177.25, "Nak tunggu, tak tahu bila seller nak stok balik.", "takes 159-173.7 dropped"),
    seg("S14", 180.70, 183.30, "So korang kena beli awal-awal sebelum stok habis."),
    seg("S15", 190.00, 193.80, "Untuk abang-abang, pak cik-pak cik di luar sana nak nampak smart kan,", "first take 183-189 dropped"),
    seg("S16", 194.00, 196.30, "auto handsome, beli kurta macam ni."),
    seg("S17", 196.30, 201.55, "Harga dia murah sangat. Memang murah, tapi lawa, kemas."),
    seg("S18", 210.70, 213.60, "Kurta ni dari Zeke tau, memang sangat best.", "'pakai ni auto handsome' repeat (204.8) dropped"),
    seg("S19", 213.60, 216.30, "Okey, jangan lupa, boleh check out terus di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1380}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Drive folder 1nA5GNqX… 'Kurta Zeke V1'. Caption: 'Guna caption style sama seperti dalam gambar mesti sama 100%' + 'Lepas ni always pakai caption style macam dalam gambar' (docs/caption-style-6nov.jpg): one upper-case word, Rubik Mono One, off-white with a thin black outline and a halftone-dot halo, hard cuts. Overlays: 'Semua video ada overlay yang sesuai supaya viewer senang faham dan lebih mudah nak tengok video sampai habis' — close-ups of the kurta on the owner for every feature (V neck, 3/4 sleeve, scuba fabric, anti-wrinkle demo), realistic aurat-safe AI photos for the occasions and situations he describes.",
     "_note": "Kurta Zeke #1 — A-roll assets/a.mp4 = VID_20261106_083553 (front camera saved mirrored, flipped back in CSS as in the owner's other front-camera clips). assets/b.mp4 = the same clip flipped and muted; close-ups play the same moment zoomed into the kurta. Promo 11.11 and 'murah' are the owner's own words; no price. Dropped: repeated takes of the price / promo / stock lines, stutters.",
     "segments": segs,
     "punch": [["S19", "check", 1.06]],
     "broll": [cu("C1", ["S03", "pakai"], ["S03", "lengan"], 24.35, "50% 68%"),
               cu("C2", ["S03", "lengan"], ["S03", "nak"], 29.00, "25% 75%"),
               cu("C3", ["S05", "start"], ["S05", "end"], 49.90, "50% 75%"),
               cu("C4", ["S07", "start"], ["S08", "end"], 80.30, "50% 55%", (1.5, 1.65))],
     "photos": [ph("kenduri", ["S02", "kenduri"], ["S02", "puasa"], "AI: ke kenduri berkurta"),
                ph("tarawih", ["S02", "puasa"], ["S02", "end"], "AI: ke masjid untuk tarawih"),
                ph("wuduk", ["S03", "nak"], ["S03", "memang"], "AI: ambil wuduk, lengan tiga suku"),
                ph("selesa", ["S04", "start"], ["S04", "end"], "AI: selesa berkurta"),
                ph("stok", ["S12", "start"], ["S13", "end"], "AI: rak baju hampir kosong (stok habis)"),
                ph("smart", ["S15", "start"], ["S16", "end"], "AI: nampak smart berkurta")],
     "theme": {"key": "#FFFFFF", "brand": "#FFFFFF"},
     "brand_words": ["zeke"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
