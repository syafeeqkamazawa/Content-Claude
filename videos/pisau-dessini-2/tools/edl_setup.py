"""EDL for pisau-dessini-2 (VID_20261106_110642), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 60%", push=(1.2, 1.3)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own Dessini footage", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 12.55, 22.25, "Berita baik untuk ibu-ibu akak-akak yang dah lama nak beli set pisau Dessini ni tapi tunggu turun harga, hari ni Alhamdulillah harga turun banyak tau.", "HOOK"),
    seg("S02", 23.15, 31.65, "Kalau sebelum ni, kalau kat luar nak beli set 8 dalam 1 macam ni, paling-paling pun 100 lebih tau.", "the owner's own price comparison"),
    seg("S03", 31.70, 44.35, "Tapi ibu-ibu akak-akak cuba tengok dekat beg kuning berapa harga kat situ, sebab sekarang ni promo banyak tau. Seller tengah buat promo 11.11 pun ada lagi."),
    seg("S04", 47.35, 53.95, "Masya Allah, memang sangat-sangat murah ya, tapi tak pasti harga ni sampai bila.", "the repeated 'tengok dekat beg kuning, pergi order laju-laju' (54-57.7) dropped — the same CTA closes the video"),
    seg("S05", 72.20, 78.85, "Set pisau ni bukan jenis biasa-biasa ya, material stainless steel, anti karat, sangat berkualiti, sangat tebal tau.", "stutter 'set pisau' dropped"),
    seg("S06", 92.40, 95.55, "Dia datang dengan lima bilah pisau berlainan saiz macam ni.", "earlier takes (78.8-92.4, incl. the count and a repeat of this line) dropped"),
    seg("S07", 95.70, 97.20, "Ada pisau potong daging,", "repeat 'ada pisau potong daging' (99.8) dropped"),
    seg("S08", 102.05, 109.40, "ada pisau potong buah, ada pisau potong sayur, ada pisau potong bawang, macam-macam ni."),
    seg("S09", 115.75, 124.35, "Lepas tu ibu-ibu akak-akak, siap ada pengasah lagi tau, kalau tak tajam boleh asah guna yang ni, untuk tajamkan gunting dan pisau.", "stumbles 'lepas tu, lepas tu, ibu ayah' dropped"),
    seg("S10", 124.80, 132.15, "Dan jangan risau, tempat letak ni semua dah ada tempat masing-masing, boleh letak kat sini, dan dia siap boleh berpusing lagi tau, mudah."),
    seg("S11", 138.95, 147.75, "Paling penting, dia punya pisau ni tajam tau, sangatlah tajam, nak potong daging, korang nak potong sayur, semua memang sekali jalan je.", "first take (132.9-135.3) dropped"),
    seg("S12", 152.75, 160.50, "Lepas tu yang lagi best ni, takde hulu tau, dia dah bercantum daripada atas sampai bawah ni, dah bercantum sekali, so tak risau hulu tercabut."),
    seg("S13", 178.00, 184.55, "Memang lawa sangat korang, serious. Ni dia punya holder dia, memang lawa sangat, serious, murah sangat hari ni."),
    seg("S14", 160.50, 166.45, "Jadi kalau korang nak beli, memang saya sangat rekomen tau, belilah set pisau daripada Dessini ni.", "its promo 11.11 tail (167-175) repeats S03 — dropped"),
    seg("S15", 192.60, 200.00, "Boleh guna untuk standby puasa nanti, dan lagi-lagi hari raya pun banyak nak guna pisau ni."),
    seg("S16", 185.40, 191.90, "Ibu-ibu akak-akak, kalau tengok dekat beg kuning tu ada voucher boleh claim, kalau harga tu tengah murah daripada biasa, boleh beli terus.", "CTA", 1.04),
    seg("S17", 200.95, 202.10, "Dapatkan di beg kuning.", "", 1.06),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Set Pisau Dessini, Drive folder 16e_wkdi… (clip 110642; clip 093343 is pisau-dessini-1). Caption: the 6 Nov default (docs/caption-style-6nov.jpg) on the wall above the head (top 300), per-segment cap_top where the box would be covered. Overlays on every explanation (owner 6 Nov): close-ups of the owner's own box, holder and knives first; realistic AI photos (hands in long sleeves only, or no people) for the knife uses and Hari Raya.",
     "_note": "Pisau Dessini #2 — A-roll assets/a.mp4 = VID_20261106_110642 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Price talk ('harga turun', 'kat luar 100 lebih', promo 11.11) is the owner's own words; no price shown.",
     "segments": segs,
     "punch": [["S16", "voucher", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S02", "end"], 33.0, "50% 62%", (1.12, 1.2)),
               cu("C2", ["S05", "start"], ["S05", "end"], 72.2, "50% 62%", (1.12, 1.2)),
               cu("C3", ["S06", "start"], ["S07", "end"], 92.4, "50% 66%", (1.15, 1.25)),
               cu("C4", ["S09", "start"], ["S09", "end"], 113.5, "50% 62%", (1.15, 1.25)),
               cu("C5", ["S10", "start"], ["S10", "end"], 124.8, "50% 66%", (1.15, 1.25)),
               cu("C6", ["S12", "start"], ["S12", "end"], 156.0, "45% 62%", (1.12, 1.2)),
               cu("C7", ["S13", "start"], ["S13", "end"], 180.0, "50% 66%", (1.12, 1.2))],
     "photos": [ph("papan", ["S08", "start"], ["S08", "end"], "AI: papan potong — daging, buah, sayur, bawang"),
                ph("daging", ["S11", "nak"], ["S11", "end"], "AI: hiris daging (tangan berlengan panjang sahaja)"),
                ph("raya", ["S15", "start"], ["S15", "end"], "AI: persiapan Hari Raya")],
     "theme": {"key": "#D7263D", "brand": "#E9E9E9"},
     "brand_words": ["dessini"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
