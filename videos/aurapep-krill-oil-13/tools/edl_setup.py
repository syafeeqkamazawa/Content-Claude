"""EDL for aurapep-krill-oil-13 (VID_20261107_164428), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="38% 64%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the Aurapep bottle in the owner's hand", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def lb(text, f, t): return {"text": text, "from": f, "to": t, "top": 170}


segs = [
    seg("S01", 3.70, 12.92, "Krill oil ni mahal tau sebenarnya. Tapi krill oil ni dia lebih padu daripada omega ataupun fish oil.", "HOOK"),
    seg("S02", 12.90, 15.55, "Tapi ramai tak tahu sebab apa."),
    seg("S03", 15.50, 17.26, "Krill oil ni,", "stumble 'ataupun kita nama' (17.3-19.6) dropped"),
    seg("S03b", 19.58, 21.42, "nama dia Antarctic krill oil ni."),
    seg("S04", 21.40, 31.00, "Antara fungsi dia boleh bagi untuk sihatkan jantung, otak kita, mata kita, tulang pun ia juga"),
    seg("S05", 35.80, 37.75, "perlindungan antioksidan.", "pause (31-35.8) dropped"),
    seg("S06", 37.72, 43.05, "Dan krill oil daripada Aurapep ni 1000 mg tau."),
    seg("S07", 44.05, 56.80, "Dia ada apa? Ada omega-3, EPA, DHA, masya-Allah. Ada vitamin D3 lagi, vitamin K2, masya-Allah."),
    seg("S08", 56.78, 69.20, "Semua ni dalam softgel yang kita boleh amalkan secara harian. Satu hari ambil dua softgel sahaja. Dalam satu botol ni ada 40 softgel.", "'betul tak tak perlu … betul-betul' (69-81.6) dropped — unclear"),
    seg("S09", 81.55, 92.98, "Kalau rasa ragu-ragu lagi, jangan risau. Boleh check Google, check GPT, tanya apa fungsi krill oil ni."),
    seg("S10", 92.98, 95.70, "Tapi krill oil ni boleh ikutkan mahal,", "repeated 'mahal' (95.7-96.8) dropped"),
    seg("S10b", 96.80, 97.66, "sangat mahal."),
    seg("S11", 119.15, 122.16, "Ada setengah krill oil tu boleh sampai 200 tau.", "moved up next to 'sangat mahal'"),
    seg("S12", 97.85, 103.96, "Tapi yang ni daripada Aurapep, cuba tengok dekat beg kuning. Sekarang ni pun ada promo 11.11 tau.", "repeated 'tengok dekat beg kuning' (104.2-105.4) dropped"),
    seg("S13", 105.45, 107.48, "Harga dia berapa? Mesti korang terkejut.", "'kalau ok terkejut ni' (107.5-119) and the repeated price question (122.6-128.5) dropped"),
    seg("S14", 136.85, 139.75, "Krill oil daripada Aurapep ni bukan fish oil biasa-biasa."),
    seg("S15", 140.60, 145.55, "Ok korang tengok kat beg kuning sekarang. Harga tengah ada promo tu, sementara harga tengah murah,", "false start 'krill oil' (135.6-136.8) before S14 dropped"),
    seg("S15b", 147.60, 149.32, "korang boleh check out awal-awal.", "first 'korang boleh' (145.6-147.6) dropped — said twice"),
    seg("S16", 149.32, 153.60, "Jangan beli satu botol, beli dua ke tiga botol, sebab stok dia tak tentu tau."),
    seg("S17", 154.25, 156.62, "Tiba-tiba boleh habis sekejap je, pasal", "repeated 'dah ramai yang beli' (156.6-161.5) dropped"),
    seg("S17b", 161.50, 165.30, "dah ramai sangat yang beli dari Aurapep ni."),
    seg("S18", 174.95, 183.62, "Okay guys, make sure korang try tau, sebab krill oil ni dah menggantikan keterujaan orang terhadap fish oil.", "'ok ok ok' (165-175) dropped"),
    seg("S19", 184.30, 186.60, "Okay, check out di beg kuning sekarang.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Ada 5 video baru' — VID_20261107_164428 in the Drive root → Aurapep Krill Oil #13 (165018/165405/165756 = VTEAY Fish Oil #2-#4, 170617 = StemLabs Fish Oil #2). Caption: the 6 Nov default on the wall above the head (top 300) — the bottle is held low in front of the chest. Overlays on every explanation (owner 6 Nov): close-ups of the bottle in the owner's hand, ingredient labels top-centre (Omega-3, EPA • DHA, D3 + K2) and realistic AI photos (Antarctic sea, x-ray heart / brain & eyes / body, red krill, softgels, phone search, pharmacy shelf, online shopping, boxes of stock, krill swarm) — mostly reused from earlier Krill videos, one new (carian).",
     "_note": "Aurapep Krill Oil #13 — A-roll assets/a.mp4 = VID_20261107_164428 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. 1000 mg, omega-3/EPA/DHA/D3/K2, 2 softgels a day, 40 softgels, 'sampai 200' for other krill oils and promo 11.11 are the owner's own words; no Aurapep price shown.",
     "segments": segs,
     "labels": [lb("Omega-3", ["S07", "omega-3,"], ["S07", "EPA,"]), lb("EPA • DHA", ["S07", "EPA,"], ["S07", "vitamin"]),
                lb("D3 + K2", ["S07", "vitamin"], ["S07", "end"])],
     "punch": [["S19", "check", 1.06]],
     "broll": [cu("C1", ["S06", "start"], ["S06", "end"], 39.5, "50% 75%"), cu("C2", ["S07", "start"], ["S07", "end"], 46.0, "42% 58%", (1.45, 1.55)),
               cu("C3", ["S12", "start"], ["S12", "end"], 100.0, "44% 74%"), cu("C4", ["S14", "start"], ["S14", "end"], 136.5, "43% 70%"),
               cu("C5", ["S16", "start"], ["S16", "end"], 150.0, "44% 69%")],
     "photos": [ph("fishoil", ["S01", "daripada"], ["S01", "end"], "AI: minyak ikan & ikan"),
                ph("laut", ["S03", "start"], ["S03b", "end"], "AI: laut Antartika (tiada orang)"),
                ph("x_jantung", ["S04", "start"], ["S04", "otak"], "AI: x-ray jantung"),
                ph("x_mata", ["S04", "otak"], ["S04", "tulang"], "AI: x-ray otak & mata"),
                ph("x_badan", ["S04", "tulang"], ["S04", "end"], "AI: x-ray badan"),
                ph("merah", ["S05", "start"], ["S05", "end"], "AI: krill merah (tiada orang)"),
                ph("softgel", ["S08", "start"], ["S08", "end"], "AI: softgel merah di tapak tangan (berlengan panjang)"),
                ph("carian", ["S09", "start"], ["S09", "end"], "AI: carian di telefon (berlengan panjang)"),
                ph("rak", ["S10", "start"], ["S11", "end"], "AI: rak suplemen di farmasi"),
                ph("belanja", ["S15", "start"], ["S15b", "end"], "AI: wanita bertudung membeli online"),
                ph("stok", ["S17", "start"], ["S17b", "end"], "AI: kotak stok (tiada orang)"),
                ph("krill", ["S18", "start"], ["S18", "end"], "AI: kawanan krill (tiada orang)")],
     "theme": {"key": "#E0342C", "brand": "#2C4A8C"},
     "brand_words": ["aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
