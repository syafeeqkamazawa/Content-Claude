"""EDL for vteay-fish-oil-4 (VID_20261107_165756), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="45% 75%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the VTEAY bottle in the owner's hand", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def lb(text, f, t): return {"text": text, "from": f, "to": t, "top": 170}


segs = [
    seg("S01", 4.22, 10.85, "Petua untuk kita nak pilih Omega-3 fish oil yang berkualiti, kena tengok kandungan EPA dan DHA.", "HOOK"),
    seg("S02", 24.88, 29.35, "Jangan tengok pada label, packaging ataupun pada harga semata-mata je.", "two earlier takes (10.6-24.9) dropped"),
    seg("S03", 29.54, 36.48, "Saya nak syorkan kepada anda semua Omega-3 fish oil ni daripada VTEAY ni, ada kelulusan daripada KKM tau."),
    seg("S04", 36.48, 41.78, "So jangan risau, maknanya kita boleh gunakan secara selamat, yakin dan berkualiti tau.", "'omega 3 fish oil ni' false start (41.8-45.5) and the stumbling figure takes (45.5-64) dropped"),
    seg("S05", 64.00, 73.78, "Dalam satu botol ni ada 2500 mg fish oil, 483 EPA dan juga 644 DHA, dan DHA yang tinggi macam ni"),
    seg("S06", 73.78, 79.50, "dapat bantu untuk support kesihatan jantung kita, dapat bantu untuk support kesihatan saraf kita.", "'yang kita rasa selalu lenguh-lenguh, kebas … dapat bantu' (79.5-84.4) dropped — TikTok-risk claim (as VTEAY #1); first take of the brain line (85.9-89.2) dropped"),
    seg("S07", 92.36, 98.16, "Dan juga dapat bantu untuk support sistem otak kita tau, supaya lebih fokus dan daya ingatan yang lebih baik."),
    seg("S08", 117.10, 120.66, "Omega-3 fish oil dari VTEAY ni sekarang harga tengah murah tau,", "repeated takes (98.2-117) dropped"),
    seg("S09", 120.78, 123.48, "seller tengah buat promo, banyak sekarang ni."),
    seg("S10", 123.40, 132.40, "Tambah pula sekarang ni promo 11.11 sedang berlangsung tau. Cuba tengok dekat beg kuning, kalau ada voucher claim terus, kalau harga tu tengah murah daripada biasa,"),
    seg("S11", 133.18, 141.65, "jangan tunggu lagi, terus check out, dan jangan beli satu botol, beli dua tiga botol terus, sebab apa stok dia cepat sangat habis, bila-bila masa dia boleh habis."),
    seg("S12", 142.36, 149.10, "So kepada kawan-kawan, ibu ayah, abang-abang, pakcik-pakcik, kakak-kakak,"),
    seg("S13", 149.08, 154.25, "boleh klik segera sementara ada stok dan masih lagi harga promosi itu, boleh dapatkan terus di beg kuning ni.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Ada 5 video baru' — VID_20261107_165756 in the Drive root → VTEAY Fish Oil #4 (petua memilih omega-3). Caption: the 6 Nov default on the wall above the head (top 300). Many repeated takes cut to the cleanest one each; 'lenguh-lenguh, kebas … dapat bantu' dropped (TikTok risk, owner 5 Nov). Overlays on every explanation (owner 6 Nov): close-ups of the bottle in the owner's hand, EPA / DHA / KKM / figure labels, realistic AI photos (pharmacy shelf, x-ray heart / nerves / brain, focused man, online shopping, boxes of stock, family).",
     "_note": "VTEAY Omega-3 Fish Oil #4 — A-roll assets/a.mp4 = VID_20261107_165756 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. 2500 mg fish oil, 483 EPA, 644 DHA, KKM, promo 11.11, voucher are the owner's own words; no price.",
     "segments": segs,
     "labels": [lb("EPA • DHA", ["S01", "EPA"], ["S01", "end"]), lb("KKM", ["S03", "KKM"], ["S03", "end"]),
                lb("2500 mg Fish Oil", ["S05", "2500"], ["S05", "483"]), lb("483 mg EPA", ["S05", "483"], ["S05", "644"]),
                lb("644 mg DHA", ["S05", "644"], ["S05", "end"])],
     "punch": [["S13", "boleh", 1.06]],
     "broll": [cu("C1", ["S03", "start"], ["S03", "end"], 31.0, "50% 79%", (1.5, 1.6)), cu("C2", ["S04", "start"], ["S04", "end"], 37.5, "50% 77%"),
               cu("C3", ["S05", "start"], ["S05", "end"], 66.0, "43% 69%"), cu("C4", ["S08", "start"], ["S08", "end"], 117.5, "38% 75%"),
               cu("C5", ["S11", "start"], ["S11", "dan"], 134.0, "41% 79%", (1.5, 1.6))],
     "photos": [ph("rak", ["S02", "start"], ["S02", "end"], "AI: rak suplemen di farmasi"),
                ph("x_jantung", ["S06", "start"], ["S06", "saraf"], "AI: x-ray jantung"),
                ph("x_saraf", ["S06", "saraf"], ["S06", "end"], "AI: x-ray saraf"),
                ph("x_otak", ["S07", "start"], ["S07", "supaya"], "AI: x-ray otak"),
                ph("fokus", ["S07", "supaya"], ["S07", "end"], "AI: lelaki fokus bekerja"),
                ph("belanja", ["S09", "start"], ["S10", "end"], "AI: wanita bertudung membeli online"),
                ph("stok", ["S11", "dan"], ["S11", "end"], "AI: kotak stok (tiada orang)"),
                ph("keluarga", ["S12", "start"], ["S12", "abang-abang,"], "AI: keluarga (aurat ditutup)"),
                ph("ibubapa2", ["S12", "abang-abang,"], ["S12", "end"], "AI: keluarga di rumah (aurat ditutup)")],
     "theme": {"key": "#5FB8E0", "brand": "#FFFFFF"},
     "brand_words": ["vteay"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
