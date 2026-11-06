"""EDL for aurapep-shilajit-7 (VID_20261106_170843), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 62%", push=(1.3, 1.45)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own Shilajit bottle / box", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 5.40, 10.92, "Korang jangan main-main tau, ni Shilajit eh. Shilajit ni bukan biasa-biasa tau.", "HOOK"),
    seg("S02", 11.00, 13.00, "Dia punya rasa dia tak ada bau."),
    seg("S03", 13.75, 21.40, "Biasanya ada Shilajit yang ada bau, yang ni tak ada bau, tak menusuk dan tak susah untuk ditelan."),
    seg("S04", 22.25, 28.00, "InsyaAllah orang kata lebih mudah lah untuk gunakan Shilajit ni, dia dalam bentuk kapsul tau."),
    seg("S05", 31.85, 41.15, "Shilajit ni gabungan cendawan reishi, ada magnesium dan ada zinc sekali. Memang sangat bagus Shilajit ni.", "stumble 'dia ada gabungan eh' dropped"),
    seg("S06", 46.50, 54.02, "Siapa yang selalu pagi-pagi tu susah nak bangun, malam susah nak tidur kan,", "first take (41.9-46.2) dropped"),
    seg("S07", 83.90, 88.35, "petang-petang dah masuk pukul 2 tu, otak dah rasa berat tu kan? Ambil ni 2 biji.", "four earlier takes of the 'petang pukul 2' line (53.9-83) dropped"),
    seg("S08", 88.55, 97.85, "Sekarang seller dah buat promotion tau. Kalau beli kat luar mahal sikit ni, tapi kalau tengok dekat link tu ada special harga murah."),
    seg("S09", 98.15, 101.95, "Seller tengah buat promotion ni, 11.11 punya promotion."),
    seg("S10", 103.65, 112.95, "So ambil ni, sekarang ni tengah viral kat TikTok tau. Jangan tunggu lagi, takut nanti stok habis. Ni seller baru restock balik tau. Siapa nak grab, grab sekarang.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Aurapep Shilajit, Drive folder 12AIw3W3… — three new talking clips (170843 → #7, 171623 → #8, 172057 → #9); 090353/090625 already used in #1-#6. Caption: the 6 Nov default on the wall above the head (top 300) — bottle and box fill the lower frame. Overlays on every explanation (owner 6 Nov): close-ups of the owner's own bottle / box first, realistic aurat-safe AI photos for raw shilajit, reishi and the morning / 2 pm tiredness the owner describes (the same framing earlier Shilajit videos used).",
     "_note": "Aurapep Shilajit #7 — A-roll assets/a.mp4 = VID_20261106_170843 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Promo 11.11 / 'kat luar mahal sikit' / restock are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S10", "jangan", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S02", "end"], 11.0, "40% 66%"),
               cu("C2", ["S04", "start"], ["S04", "end"], 22.25, "60% 66%"),
               cu("C3", ["S05", "magnesium"], ["S05", "end"], 36.3, "62% 66%"),
               cu("C4", ["S09", "start"], ["S09", "end"], 98.15, "45% 66%")],
     "photos": [ph("resin", ["S03", "start"], ["S03", "bau,"], "AI: shilajit mentah (resin)"),
                ph("reishi", ["S05", "start"], ["S05", "magnesium"], "AI: cendawan reishi"),
                ph("pagi", ["S06", "start"], ["S06", "end"], "AI: susah bangun pagi (lelaki berpakaian penuh)"),
                ph("petang", ["S07", "start"], ["S07", "kan?"], "AI: letih petang di pejabat (lelaki berpakaian penuh)")],
     "theme": {"key": "#C9A227", "brand": "#E9E9E9"},
     "brand_words": ["shilajit", "aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
