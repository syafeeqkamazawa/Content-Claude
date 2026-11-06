"""EDL for jubah-hitam-2 (VID_20261107_015936), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 42%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner wearing the jubah (fabric / sleeve)", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 9.35, 14.48, "Kenapa nak beli yang mahal, kalau ada yang murah tapi nampak macam mahal?", "HOOK — first fragment 'kalau ada yang murah' (5.5-7.4) dropped"),
    seg("S02", 14.45, 27.62, "Korang tengok ni, jubah yang aku pakai ni sangat selesa, nampak premium, tapi tengok dekat beg kuning, confirm korang terkejut, harganya memang sangat murah. Seller tengah buat promo guys."),
    seg("S03", 27.55, 36.20, "Sekarang ni pun musim seller buat promo 11.11 guys, harga dia pun memang luar biasa juga, tengok."),
    seg("S04", 36.38, 50.65, "Memang cantik. Yang aku pakai ni jubah saiz L, tengok lengan dia, 3 suku, nak ambil wuduk senang guys, korang tarik sikit je dah boleh singsing lengan, dah boleh ambil wuduk sampai siku."),
    seg("S05", 51.10, 56.95, "Berat aku 76 kg, tinggi 165 cm, aku pakai saiz L.", "first take (51.7-55) dropped"),
    seg("S06", 57.40, 65.00, "Korang boleh tengok dekat beg kuning, ada pelbagai lagi warna, korang boleh tengok, yang mana berkenan boleh terus check out."),
    seg("S07", 65.35, 69.85, "Beli awal guys, kalau korang beli lewat, takut-takut stok dah habis."),
    seg("S08", 72.22, 76.30, "Sementara stok masih ada, harga tengah murah tu, korang terus check out di beg kuning.", "CTA", 1.04),
]
broll = [cu("C1", ["S02", "start"], ["S02", "premium,"], 15.0, "50% 45%", (1.35, 1.5)),
         cu("C2", ["S04", "tengok"], ["S04", "guys,"], 40.0, "50% 45%"),
         cu("C3", ["S06", "start"], ["S06", "end"], 57.4, "50% 50%", (1.25, 1.35))]
photos = [ph("wuduk", ["S04", "korang"], ["S04", "end"], "AI: ambil wuduk (lengan sahaja)")]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1380}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Jubah hitam ada 3 video' — Drive folder 'Jubah Hitam' (1qxVqw_2…): 015650 → #1, 015936 → #2, 020132 → #3, one video per clip. Caption: the 6 Nov default at ~72% height (the owner is filmed full-body, so the face sits high; same placement as Kurta Zeke). Overlays on every explanation (owner 6 Nov): close-ups of the owner wearing the jubah first; realistic AI photos for wuduk (forearms only).",
     "_note": "Jubah Hitam #2 — A-roll assets/a.mp4 = VID_20261107_015936 (rear camera, not mirrored). assets/b.mp4 = the same clip, muted. Price / promo 11.11 / stock talk are the owner's own words; no price shown. Size note (L, 165 cm, 76 kg) is the owner's own.",
     "segments": segs,
     "punch": [],
     "broll": broll,
     "photos": photos,
     "theme": {"key": "#C9A227", "brand": "#E9E9E9"},
     "brand_words": [], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
