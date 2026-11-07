"""EDL for vteay-fish-oil-3 (VID_20261107_165405), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="44% 68%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the VTEAY bottle in the owner's hand", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def lb(text, f, t): return {"text": text, "from": f, "to": t, "top": 170}


segs = [
    seg("S01", 30.60, 34.98, "Yang ada pada saya ni Omega-3 fish oil yang sangat bagus untuk badan.", "HOOK — the opening 'boleh ambil 2 biji sehari kalau dah lupa, mata kabur, badan sakit' (0-30, several takes) dropped: symptoms tied to a dose = TikTok-risk claim (owner 5 Nov)"),
    seg("S02", 34.98, 40.95, "Satu supplement je dah baik untuk otak, jantung, lutut, hati, sendi, pembuluh darah."),
    seg("S03", 41.66, 44.95, "Yang ni korang, Omega-3 fish oil tau daripada VTEAY.", "'ok' (45-52) dropped"),
    seg("S04", 52.10, 54.95, "Dalam satu botol ni ada 30 biji."),
    seg("S05", 56.14, 60.10, "Korang juga boleh pilih yang ada 60 biji, ada 120 biji pun."),
    seg("S06", 61.18, 62.90, "Korang boleh pilih dekat beg kuning."),
    seg("S07", 64.00, 66.75, "Korang jangan risau tau, yang ni KKM dah approve tau."),
    seg("S08", 67.90, 71.40, "Awak amalkan je 2 biji sehari, rasa dia sedap je.", "pause (71.4-76) dropped"),
    seg("S09", 76.00, 81.40, "Nak kata sedap tu bukanlah, maksudnya tak ada bau hanyir, awak telan je."),
    seg("S10", 81.40, 90.40, "So siapa yang nak dapatkan, boleh dapatkan dekat beg kuning. Sekarang ni seller tengah buat promo tau, 11.11 punya promo, harga dia mungkin lebih rendah daripada biasa."),
    seg("S11", 90.65, 93.25, "Cuba tengok dekat beg kuning. Kalau ada voucher boleh claim terus."),
    seg("S12", 93.35, 101.60, "Kalau harga tu memang tengah murah dan stok masih ada, boleh ambil. Jangan ambil satu botol, ambil dua ke tiga botol sebab stok dia bila-bila masa dia boleh habis."),
    seg("S13", 102.20, 103.20, "Dapatkan di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Ada 5 video baru' — VID_20261107_165405 in the Drive root → VTEAY Fish Oil #3. Caption: the 6 Nov default on the wall above the head (top 300). The opening ('boleh ambil 2 biji sehari kalau dah lupa, mata kabur, badan rasa sakit') dropped as a TikTok-risk claim (owner 5 Nov); the video opens on 'Omega-3 fish oil yang sangat bagus untuk badan'. Overlays on every explanation (owner 6 Nov): close-ups of the bottle in the owner's hand and realistic AI photos (x-ray brain / heart / knee / body / blood vessels, softgels, a softgel with water, online shopping, boxes of stock).",
     "_note": "VTEAY Omega-3 Fish Oil #3 — A-roll assets/a.mp4 = VID_20261107_165405 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. 30 / 60 / 120 softgel packs, 2 a day, KKM, no fishy smell, promo 11.11, voucher are the owner's own words; no price.",
     "segments": segs,
     "labels": [lb("30 • 60 • 120 biji", ["S05", "60"], ["S05", "end"]), lb("KKM", ["S07", "KKM"], ["S07", "end"])],
     "punch": [["S13", "dapatkan", 1.06]],
     "broll": [cu("C1", ["S03", "start"], ["S03", "end"], 42.0), cu("C2", ["S04", "start"], ["S04", "end"], 52.5),
               cu("C3", ["S05", "start"], ["S06", "end"], 57.0), cu("C4", ["S07", "start"], ["S07", "end"], 64.5),
               cu("C5", ["S11", "start"], ["S11", "end"], 91.0), cu("C6", ["S12", "jangan"], ["S12", "end"], 97.5)],
     "photos": [ph("x_otak", ["S02", "start"], ["S02", "jantung,"], "AI: x-ray otak"),
                ph("x_jantung", ["S02", "jantung,"], ["S02", "lutut,"], "AI: x-ray jantung"),
                ph("x_lutut", ["S02", "lutut,"], ["S02", "hati,"], "AI: x-ray lutut"),
                ph("x_badan", ["S02", "hati,"], ["S02", "pembuluh"], "AI: x-ray badan"),
                ph("x_darah", ["S02", "pembuluh"], ["S02", "end"], "AI: x-ray salur darah"),
                ph("softgel", ["S08", "start"], ["S08", "end"], "AI: softgel minyak ikan"),
                ph("telan", ["S09", "start"], ["S09", "end"], "AI: softgel & air (tangan berlengan panjang)"),
                ph("belanja", ["S10", "sekarang"], ["S10", "end"], "AI: wanita bertudung membeli online"),
                ph("stok", ["S12", "start"], ["S12", "jangan"], "AI: kotak stok (tiada orang)")],
     "theme": {"key": "#5FB8E0", "brand": "#FFFFFF"},
     "brand_words": ["vteay"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
