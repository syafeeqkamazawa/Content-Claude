"""EDL for infinity-probiotics-4 (VID_20261104_153839), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 38.20, 41.70, "Guys, ini Probiotic Plus daripada Infinity.", "HOOK, third take (12.7, 28.1 dropped; 0-12.7 is unboxing noise)"),
    seg("S02", 42.10, 47.70, "Saya sarankan siapa-siapa yang ada 5 masalah ni untuk ambil produk ni segera."),
    seg("S03", 48.40, 52.65, "Yang pertama, orang yang susah nak tidur, overstress."),
    seg("S04", 58.10, 61.60, "Yang kedua, ada masalah sembelit, susah nak membuang.", "first take 53.2 dropped"),
    seg("S05", 62.10, 65.00, "Yang ketiga, perut selalu kembung, bloated."),
    seg("S06", 65.34, 69.50, "Yang keempat, orang yang ada masalah kulit, terutamanya jerawat.", "repeat 75.4 dropped"),
    seg("S07", 79.34, 83.05, "Dan yang kelima, siapa-siapa yang selalu ambil antibiotik.", "repeat 88.4 dropped"),
    seg("S08", 92.40, 96.70, "So please amalkan probiotic daripada Infinity sekarang."),
    seg("S09", 98.50, 101.60, "Sekarang seller banyak tengah buat promo 11.11.", "'boleh klik dekat beg kuning' (97.2) dropped — repeated in the CTA"),
    seg("S10", 101.95, 107.92, "Boleh check dekat beg kuning, kalau ada voucher boleh claim. Sementara harga tengah murah, boleh beli sekarang.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word2", "word2": {"top": 1540, "size": 68, "weight": 800}, "fs_style": "ref", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: Drive folder 1xPV9TTz… 'Infinity Probiotics Plus' — 'Buat semua video yang belum digunakan ya'. Unused clips: VID_20261104_153839 (talking, with unboxing) and VID_20261104_154051 (new B-roll on grass) -> one video. No new reference, so the product's last style (Infinity #3, owner 2 Nov) is reused: one white Montserrat ExtraBold word with a soft shadow at ~68 % height; cutaways landing with a zoom blur; the INFINITY / PROBIOTIK PLUS title on a yellow bar; a white card dropping from the top listing the owner's own five points. 1 Nov: keep every point; product close-ups and the owner using the product.",
     "_note": "Infinity Probiotics Plus #4 — A-roll assets/a.mp4 = VID_20261104_153839. B-roll assets/b.mp4 (muted) = VID_20261104_154051 0-74.32 (box 8-24, bottle 28-44, capsules in the cap 48-66, on grass) + VID_20261014_001726 74.32-171.2 (also used in #2/#3). AI photos penat, kembung, jerawat are reused from #3; stres, sembelit, antibiotik are new. The five problems and 'promo 11.11' are the owner's own words; no price.",
     "segments": segs,
     "brand_title": [{"from": ["S01", "ini"], "to": ["S01", "end"], "top": "INFINITY", "bar": "PROBIOTIK PLUS", "y": 820}],
     "infocard": [{"from": ["S02", "5"], "to": ["S02", "end"], "body": "Ambil <b>Probiotic Plus</b> kalau ada salah satu daripada <b>5 masalah</b> ni:",
                   "items": ["Susah nak tidur, overstress", "Sembelit, susah nak membuang", "Perut selalu kembung, bloated", "Kulit berjerawat", "Selalu ambil antibiotik"]}],
     "punch": [["S10", "beli", 1.06]],
     "broll": [br("B1", ["S08", "start"], ["S08", "end"], 50.0, "154051: botol + kapsul dalam penutup (guna produk)"),
               br("B2", ["S09", "start"], ["S09", "end"], 12.0, "154051: kotak depan", (1.0, 1.08), "50% 40%")],
     "photos": [ph("stres", ["S03", "start"], ["S03", "end"], "AI: susah tidur, stres (baru)"),
                ph("sembelit", ["S04", "start"], ["S04", "end"], "AI: sembelit (baru)"),
                ph("kembung", ["S05", "start"], ["S05", "end"], "AI: kembung (dari #3)"),
                ph("jerawat", ["S06", "start"], ["S06", "end"], "AI: jerawat (dari #3)"),
                ph("antibiotik", ["S07", "start"], ["S07", "end"], "AI: antibiotik (baru)")],
     "theme": {"key": "#F2B705", "brand": "#2BB3C0"},
     "brand_words": ["infinity", "probiotic", "plus"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
