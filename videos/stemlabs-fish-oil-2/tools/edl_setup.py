"""EDL for stemlabs-fish-oil-2 (VID_20261107_170617), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 75%", push=(1.45, 1.55)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the StemLabs bottle and the cup of softgels in the owner's hands", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def lb(text, f, t): return {"text": text, "from": f, "to": t, "top": 170}


segs = [
    seg("S01", 9.50, 15.24, "Supplement yang baik untuk kita punya otak, kita punya saraf, kita punya jantung,", "HOOK — 'kita punya tekanan darah' (15.2-17.5) dropped (TikTok risk, owner 5 Nov)"),
    seg("S01b", 17.55, 25.50, "kita punya mata, kita punya ingatan kita, sendi, kita punya lutut kita, ni adalah fish oil."),
    seg("S02", 34.80, 44.56, "Bila tengok harga tu mula-mula saya risau juga, kenapa murah sangat? Tapi memang bila saya dah check, dia adalah original, so jangan risau."),
    seg("S03", 44.56, 50.50, "Fish oil daripada StemLabs ni memang official daripada store dia.", "'ok' (50.5-55.4) dropped"),
    seg("S04", 55.40, 66.00, "Yang paling penting, dia ada hologram KKM tau. Maksudnya dia dah jual dekat offline dan dekat farmasi pun ada tau. Tapi harga dia lebih mahal lah."),
    seg("S05", 66.70, 74.00, "So kalau beli dekat beg kuning, jauh lebih murah. Dan dia juga ada halal JAKIM, korang boleh check juga dia punya nombor.", "repeated 'korang boleh cek juga' (74.9-85.6) dropped"),
    seg("S06", 85.60, 91.12, "Fish oil dari StemLabs ni made in New Zealand tau, manufacture dia dekat New Zealand juga."),
    seg("S06b", 94.80, 98.40, "Expired date pun dia ada tulis lah, so tak payah risau, memang legit."),
    seg("S07", 98.40, 106.70, "Fish oil daripada StemLabs ni, apa yang saya boleh kata, ini adalah fish oil yang harga dia memang sangat murah,", "'ok' (106.7-115) and the false start 'antara brand yang kau' (113.7-114.9) dropped"),
    seg("S07b", 115.06, 117.92, "antara brand yang jual fish oil yang sangat murah tau."),
    seg("S08", 124.90, 140.60, "Kalau dekat farmasi memang kena jual mahal sikit sebab farmasi itu pun sewa bangunan, memang dia akan jadi mahal. Tapi kalau beli dekat beg kuning memang jauh lebih murah, sebab dah tak ada dah kos-kos nak sewa bangunan dan sebagainya.", "first take (119.7-123) dropped"),
    seg("S09", 146.50, 150.40, "Jadi sebab tu harganya lebih murah. So korang jangan risau,"),
    seg("S09b", 153.90, 156.40, "ini adalah original daripada StemLabs tau.", "first 'ini adalah original daripada' (150.9-153.9) dropped — said twice"),
    seg("S10", 171.45, 191.00, "Yang saya pegang ni satu botol 30 biji. Boleh tengok dekat beg kuning kalau ada pilihan, boleh tengok mana yang korang lebih prefer. Harga dia ni sangat murah, kalau nak beli 100 biji atau 400 biji pun masih sangat-sangat berbaloi tau. Dalam beg kuning ada pilihan dia.", "pause (156.4-170.5) dropped"),
    seg("S11", 238.50, 244.25, "So fish oil daripada StemLabs ni, kandungan dia 1000 mg fish oil dan dia juga", "the stumbling figure takes (191-238) dropped"),
    seg("S11b", 248.40, 251.60, "EPA 300 dan juga DHA 200 lah.", "repeated 'ada EPA 300 dan juga dan dia juga ada' (244.3-248.4) dropped"),
    seg("S12", 255.90, 259.60, "Kalau dewasa tu biasanya makan 2 atau 3 biji,"),
    seg("S12b", 262.60, 268.50, "tapi kalau budak kan, sekitar umur 6 tahun dah boleh makan, tapi 1 biji je lah.", "'tapi kalau budak, tengok dekat sini' (259.6-262.6) dropped"),
    seg("S13", 271.00, 279.10, "DHA ni baik untuk otak tau dan baik untuk kita punya mata juga. Kalau EPA pula, kita punya sendi, baik untuk kita punya jantung.", "'tekanan darah, saluran pipe darah, siapa yang ada masalah darah sumbat … sangat digalakkan' (279-292) dropped — TikTok-risk claim"),
    seg("S14", 304.40, 307.90, "EPA pula dia berfungsi sebagai anti radang tau.", "three earlier takes (295-304) dropped"),
    seg("S15", 307.92, 320.40, "So dalam ni ada 30 biji boleh makan. Kalau 1 hari 2 biji, dalam 15 hari dah habislah. So better ambil 2 atau 3 botol buat stok awal, sebab stok dia sangat cepat habis tau."),
    seg("S16", 320.60, 328.70, "Boleh klik dekat beg kuning. Seller pun banyak tengah buat promo ni, promo 11.11 pun ada, dan harga dia sangat murah daripada biasa.", "the messy CTA retakes (328.7-362.6) dropped"),
    seg("S17", 365.35, 371.70, "Boleh tengok dekat beg kuning, kalau ada voucher tu boleh claim, kalau harga tu tengah murah daripada biasa, boleh borong 2-3 botol terus.", "CTA — first 'boleh tengok dekat beg kuning, kalau ada' (362.7-365.3) dropped, said twice", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Ada 5 video baru' — VID_20261107_170617 in the Drive root → StemLabs Fish Oil #2. Caption: the 6 Nov default on the wall above the head (top 300). Many repeated takes cut to the cleanest one each; 'tekanan darah', 'saluran pipe darah' and 'darah sumbat … sangat digalakkan' dropped (TikTok risk, owner 5 Nov). Overlays on every explanation (owner 6 Nov): close-ups of the bottle and the cup of softgels in the owner's hands, KKM / Halal / figure labels, realistic AI photos (x-ray brain / nerves / heart / eyes / knee, focused man, New Zealand, pharmacy shelf and shopfront, online shopping, mother and son, softgels, boxes of stock).",
     "_note": "StemLabs Fish Oil #2 — A-roll assets/a.mp4 = VID_20261107_170617 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. KKM hologram, halal JAKIM, made in New Zealand, 30 / 100 / 400 softgel packs, 1000 mg, EPA 300, DHA 200, 2-3 a day for adults / 1 for children from 6, promo 11.11, voucher are the owner's own words; no price.",
     "segments": segs,
     "labels": [lb("KKM", ["S04", "KKM"], ["S04", "maksudnya"]), lb("Halal JAKIM", ["S05", "halal"], ["S05", "end"]),
                lb("1000 mg Fish Oil", ["S11", "1000"], ["S11", "end"]), lb("EPA 300 • DHA 200", ["S11b", "start"], ["S11b", "end"])],
     "punch": [["S17", "borong", 1.06]],
     "broll": [cu("C1", ["S02", "tapi"], ["S02", "end"], 41.0), cu("C2", ["S04", "start"], ["S04", "maksudnya"], 56.0),
               cu("C3", ["S05", "dan"], ["S05", "end"], 70.0), cu("C4", ["S06b", "start"], ["S06b", "end"], 95.0),
               cu("C5", ["S09b", "start"], ["S09b", "end"], 154.0), cu("C6", ["S10", "start"], ["S10", "harga"], 171.0), cu("C6b", ["S10", "harga"], ["S10", "end"], 181.5, "62% 74%"),
               cu("C7", ["S11", "start"], ["S11", "end"], 239.0), cu("C7b", ["S11b", "start"], ["S11b", "end"], 248.5, "65% 78%"), cu("C8", ["S15", "start"], ["S15", "kalau"], 308.0),
               cu("C9", ["S17", "start"], ["S17", "kalau#2"], 365.5)],
     "photos": [ph("x_otak", ["S01", "otak,"], ["S01", "saraf,"], "AI: x-ray otak"),
                ph("x_saraf", ["S01", "saraf,"], ["S01", "jantung,"], "AI: x-ray saraf"),
                ph("x_jantung", ["S01", "jantung,"], ["S01", "end"], "AI: x-ray jantung"),
                ph("x_mata", ["S01b", "start"], ["S01b", "ingatan"], "AI: x-ray mata"),
                ph("fokus", ["S01b", "ingatan"], ["S01b", "sendi,"], "AI: lelaki fokus bekerja"),
                ph("x_lutut", ["S01b", "sendi,"], ["S01b", "ni"], "AI: x-ray lutut"),
                ph("belanja", ["S03", "start"], ["S03", "end"], "AI: wanita bertudung membeli online"),
                ph("rak", ["S04", "maksudnya"], ["S04", "end"], "AI: rak suplemen di farmasi"),
                ph("nz", ["S06", "start"], ["S06", "end"], "AI: pemandangan New Zealand (tiada orang)"),
                ph("softgel", ["S07", "start"], ["S07b", "end"], "AI: softgel minyak ikan"),
                ph("farmasi", ["S08", "start"], ["S08", "tapi"], "AI: kedai farmasi (tiada orang)"),
                ph("belanja", ["S08", "tapi"], ["S08", "end"], "AI: wanita bertudung membeli online"),
                ph("budak", ["S12", "start"], ["S12b", "end"], "AI: ibu bertudung & anak (aurat ditutup)"),
                ph("x_otak", ["S13", "start"], ["S13", "mata"], "AI: x-ray otak"),
                ph("x_mata", ["S13", "mata"], ["S13", "kalau"], "AI: x-ray mata"),
                ph("x_lutut", ["S13", "kalau"], ["S13", "baik#3"], "AI: x-ray lutut"),
                ph("x_jantung", ["S13", "baik#3"], ["S13", "end"], "AI: x-ray jantung"),
                ph("stok", ["S15", "kalau"], ["S15", "end"], "AI: kotak stok (tiada orang)")],
     "theme": {"key": "#2FA8E0", "brand": "#FFFFFF"},
     "brand_words": ["stemlabs"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
