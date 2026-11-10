"""EDL for vteay-fish-oil-6 (the owner's own finished edit lv_0_20261110231242.mp4), 10 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [{"id": "S01", "in": 0.0, "out": 30.79, "zoom": 1.0, "note": "the owner's finished edit, played whole and untouched",
         "text": "Yang ada masalah lemah-lemah badan kan, sakit satu sendi tu, mata dah start kabur dan mula dah start lupa tu kan. "
                 "Korang boleh amalkan omega fish oil, just ambil 2 biji sehari je. Omega fish oil ni bagus untuk support kita punya "
                 "pembuluh darah tau, kita punya jantung, mata dan juga sendi-sendi pulang. Cuma kalau ambil 2 biji je sehari korang dah "
                 "boleh nampak kesan dia tau. Untuk hari ni harga dia tengah promo tau, tu kalau korang nak kan, tekan dekat beg kuning "
                 "tu sekarang sebelum harga dia naikkan semula."}]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": False, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 62, "top": 1200}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 999, "keep": 0.0, "threshold_db": -90, "blip": 0.03}, "titles": [],
     "_owner_decisions": "10 Nov, VTEAY Fish Oil folder 1-HP8DmM…: 'Hanya tambah overlay visual masalah dan kelebihan sahaja. Yang lain, caption, suara, potong klip, semua tak perlu sentuh.' The owner's own finished edit (lv_0_20261110231242.mp4, 30.8 s, captions burned in) plays whole: no cuts, no captions added, no voice processing. Only full-screen realistic overlays on the problems (lemah badan, sakit sendi, mata kabur, mula lupa) and the benefits (pembuluh darah, jantung, mata, sendi, nampak kesan). After the render, tools/finish.sh puts the owner's burned-in caption back on top of the overlays (white text keyed from the original, with a soft shadow) and copies the original audio stream unchanged.",
     "_note": "VTEAY Fish Oil #6 — A-roll assets/a.mp4 = lv_0_20261110231242.mp4 as delivered (1080×1920, 60 fps). assets/b.mp4 = the same, muted.",
     "segments": segs, "punch": [], "broll": [],
     "photos": [ph("i_lesu", 0.00, 2.20, "AI: lemah badan (berlengan panjang)"),
                ph("lutut", 2.20, 3.40, "AI: sakit sendi lutut (seluar panjang)"),
                ph("kabur", 3.40, 5.12, "AI: mata kabur (berlengan panjang)"),
                ph("lupa", 5.12, 6.98, "AI: mula lupa (berlengan panjang)"),
                ph("x_darah", 13.40, 15.30, "AI: x-ray salur darah"),
                ph("x_jantung", 15.30, 16.15, "AI: x-ray jantung"),
                ph("x_mata", 16.15, 16.60, "AI: x-ray mata"),
                ph("x_lutut", 16.60, 18.28, "AI: x-ray sendi"),
                ph("sihat", 19.98, 21.88, "AI: badan sihat & aktif (aurat ditutup)")],
     "theme": {"key": "#5FB8E0", "brand": "#FFFFFF"},
     "brand_words": ["vteay"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written')
