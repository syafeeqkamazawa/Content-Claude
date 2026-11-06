"""EDL for jubah-hitam-1 (VID_20261107_015650), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 42%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner wearing the jubah (fabric / sleeve)", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 18.70, 29.20, "Jubah yang korang tengok ni, dengan kualiti macam ni, mesti korang terkejut bila korang tengok dekat beg kuning berapa harga dia, memang sangat-sangat murah guys.", "HOOK — set-up (0-18) dropped"),
    seg("S02", 29.95, 31.40, "Sekarang ni seller tengah buat promo."),
    seg("S03", 31.85, 37.50, "Korang tengok, jubah yang sangat selesa macam ni, kain dia sejuk tau."),
    seg("S04", 38.18, 39.50, "Lengan 3 suku."),
    seg("S05", 39.75, 46.40, "Aku tunjuk dekat-dekat korang, buat macam ni, nampak, tak ada kedut pun."),
    seg("S06", 47.05, 48.55, "Selesa sangat."),
    seg("S07", 49.88, 53.55, "Macam ni punya selesa, korang tengok dekat beg kuning."),
    seg("S08", 58.95, 63.75, "Kalau harga tu korang rasa betul-betul murah, korang terus check out, jangan tunggu lagi.", "first take (55-58.6) dropped"),
    seg("S09", 65.72, 74.55, "Kalau stok tu korang nampak macam banyak kan, percayalah, dekat-dekat nanti, lagi-lagi dekat nak raya, habis dah, tak sampai raya.", "false start 'stok ni nampak' (64.3) dropped"),
    seg("S10", 76.08, 80.45, "Baru masuk bulan puasa, silap-silap dah habis dah. Baik korang ambil awal-awal.", "repeated 'bulan puasa' dropped"),
    seg("S11", 81.12, 82.48, "Serius selesa aku cakap korang."),
    seg("S12", 83.58, 92.12, "Yang aku pakai ni saiz L, tinggi aku 165 cm, berat 76 kg, macam ni punya saiz memang sangat cantik, sangat selesa."),
    seg("S13", 93.68, 99.85, "So, sementara promo masih ada, sementara harga murah tu, korang grab awal-awal, check out terus di beg kuning.", "CTA", 1.04),
]
broll = [cu("C1", ["S03", "kain"], ["S04", "end"], 36.4, "50% 45%"),
         cu("C2", ["S05", "buat"], ["S05", "end"], 43.0, "50% 50%", (1.3, 1.45)),
         cu("C3", ["S12", "start"], ["S12", "end"], 83.6, "50% 55%", (1.2, 1.3))]
photos = [ph("raya", ["S09", "lagi-lagi"], ["S09", "end"], "AI: Hari Raya (tiada orang)"),
          ph("puasa", ["S10", "start"], ["S10", "end"], "AI: bazar Ramadan (tiada wajah)")]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1380}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Jubah hitam ada 3 video' — Drive folder 'Jubah Hitam' (1qxVqw_2…): 015650 → #1, 015936 → #2, 020132 → #3, one video per clip. Caption: the 6 Nov default at ~72% height (the owner is filmed full-body, so the face sits high; same placement as Kurta Zeke). Overlays on every explanation (owner 6 Nov): close-ups of the owner wearing the jubah first; realistic AI photos for a Hari Raya table and a Ramadan bazaar (no people).",
     "_note": "Jubah Hitam #1 — A-roll assets/a.mp4 = VID_20261107_015650 (rear camera, not mirrored). assets/b.mp4 = the same clip, muted. Price / promo 11.11 / stock talk are the owner's own words; no price shown. Size note (L, 165 cm, 76 kg) is the owner's own.",
     "segments": segs,
     "punch": [],
     "broll": broll,
     "photos": photos,
     "theme": {"key": "#C9A227", "brand": "#E9E9E9"},
     "brand_words": [], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
