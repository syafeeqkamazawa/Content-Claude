"""EDL for vteay-fish-oil-2 (VID_20261107_165018), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="45% 62%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the VTEAY bottle in the owner's hand", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def lb(text, f, t): return {"text": text, "from": f, "to": t, "top": 170}


segs = [
    seg("S01", 69.80, 76.26, "Saya pilih jenama ni daripada VTEAY sebab dia punya EPA dan DHA dia sangat tinggi.", "HOOK — the '4 tanda tekanan darah tinggi' opening (0-67) and 'sangatlah sesuai amalkan' dropped: blood-pressure symptoms sold with a supplement = TikTok-risk medical claim (owner 5 Nov)"),
    seg("S01b", 77.40, 79.85, "Dia adalah lebih konsentrat.", "repeated 'dia adalah' (76.3-77.4) dropped"),
    seg("S02", 94.56, 101.30, "Dalam dia ada 483 mg EPA dan juga 644 mg DHA tau, sangat tinggi.", "repeat take 'setiap hari kamu' (79.7-93.5) dropped"),
    seg("S03", 102.90, 108.28, "So setiap hari selepas kamu makan, ambil 1 ke 2 biji sahaja dah cukup.", "'bergantung kepada sejauh mana masalah yang kamu hadapi' (108.3-113.1) dropped — treatment framing; first 'so setiap hari selepas' (101.3-102.9) dropped — said twice"),
    seg("S04", 113.74, 117.75, "Setakat nak jaga kesihatan mata, jantung dan otak, untuk maintain kesihatan itu,", "two repeated takes (117.6-129) dropped"),
    seg("S04b", 129.10, 131.56, "setiap hari sebiji dah memadai.", "'kalau ada masalah yang agak tinggi boleh ambil dua sehari' (131.8-135.9) dropped — dose tied to a condition"),
    seg("S05", 136.34, 139.35, "Boleh order dekat link dekat beg kuning saya."),
    seg("S06", 144.28, 147.90, "Sekarang ni pun seller tengah buat promo 11.11 tau,", "'okey' (139.7-144) dropped"),
    seg("S06a", 149.30, 152.40, "harga dia jauh lebih rendah daripada biasa.", "first 'harga dia' (147.9-149.3) dropped — said twice"),
    seg("S06b", 153.45, 157.00, "Sementara harga tengah murah, boleh beli dekat beg kuning saya.", "false start 'boleh' (152.4-153.2) dropped"),
    seg("S07", 169.48, 177.60, "Jadi sekali lagi, yang belum pernah cuba, dapatkan di beg kuning, harga dia sangat-sangat murah.", "'fish oil … membantu untuk masalah sendi, siku, lutut' (157.6-169.5) dropped — TikTok-risk claim (as VTEAY #1)"),
    seg("S08", 177.60, 183.08, "Promo 11.11 ni bila-bila masa dia boleh habis, sementara masih ada stok."),
    seg("S09", 183.08, 188.86, "Boleh beli terus, jangan beli satu botol, beli dua-tiga botol sebab stok dia cepat sangat habis."),
    seg("S10", 188.86, 190.10, "Ok, beli di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Ada 5 video baru' — VID_20261107_165018 in the Drive root → VTEAY Fish Oil #2. Caption: the 6 Nov default on the wall above the head (top 300). The clip opens with '4 tanda tekanan darah tinggi' (headache, stiff neck, numbness, palpitations) and later says the dose depends on 'masalah' and that it helps joints — all dropped as TikTok-risk medical claims (owner 5 Nov), so the video opens on why he picked VTEAY (EPA/DHA). Overlays on every explanation (owner 6 Nov): close-ups of the bottle in the owner's hand, EPA / DHA labels, realistic AI photos (meal with softgels, x-ray eyes / heart / brain, softgels, online shopping, boxes of stock).",
     "_note": "VTEAY Omega-3 Fish Oil #2 — A-roll assets/a.mp4 = VID_20261107_165018 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. 483 mg EPA, 644 mg DHA, 1-2 a day after meals, promo 11.11 are the owner's own words; no price.",
     "segments": segs,
     "labels": [lb("483 mg EPA", ["S02", "483"], ["S02", "644"]), lb("644 mg DHA", ["S02", "644"], ["S02", "end"])],
     "punch": [["S10", "beli", 1.06]],
     "broll": [cu("C1", ["S01", "EPA"], ["S01b", "end"], 74.0, "42% 71%"), cu("C2", ["S02", "start"], ["S02", "end"], 96.0, "35% 72%"),
               cu("C3", ["S05", "start"], ["S05", "end"], 137.0, "34% 72%"), cu("C4", ["S06b", "start"], ["S06b", "end"], 154.0, "39% 80%", (1.5, 1.6)),
               cu("C5", ["S07", "start"], ["S07", "end"], 172.0, "37% 73%"), cu("C6", ["S09", "start"], ["S09", "end"], 185.0, "43% 72%")],
     "photos": [ph("makan", ["S03", "start"], ["S03", "end"], "AI: hidangan dengan softgel (tiada orang)"),
                ph("x_mata", ["S04", "start"], ["S04", "jantung"], "AI: x-ray mata"),
                ph("x_jantung", ["S04", "jantung"], ["S04", "otak,"], "AI: x-ray jantung"),
                ph("x_otak", ["S04", "otak,"], ["S04", "end"], "AI: x-ray otak"),
                ph("softgel", ["S04b", "start"], ["S04b", "end"], "AI: softgel minyak ikan"),
                ph("belanja", ["S06", "start"], ["S06a", "end"], "AI: wanita bertudung membeli online"),
                ph("stok", ["S08", "start"], ["S08", "end"], "AI: kotak stok (tiada orang)")],
     "theme": {"key": "#5FB8E0", "brand": "#FFFFFF"},
     "brand_words": ["vteay"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
