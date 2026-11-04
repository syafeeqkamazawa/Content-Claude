"""EDL for jus-gout-13 (VID_20261104_153048), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)


segs = [
    seg("S01", 3.26, 5.30, "Dua skop sehari dah cukup.", "HOOK"),
    seg("S02", 7.00, 8.85, "Untuk korang yang ada sakit gout,"),
    seg("S02b", 12.10, 16.36, "saya nak rekomenkan sangat jus gout ni daripada Promaxx series.", "'saya nak rekomen kepada anda sangat' (9.2) repeat dropped"),
    seg("S03", 16.54, 24.85, "Jus gout dari Promaxx series ni adalah campuran dari 6 jenis bahan iaitu bromelain, milk thistle,"),
    seg("S03b", 25.90, 27.10, "lemon extract,", "'lemon' false start and the first 'curcuma longa' dropped"),
    seg("S03c", 29.80, 34.35, "curcuma longa root extract, ginger extract dan juga orange extract."),
    seg("S04", 41.30, 51.65, "Jus gout ni dapat bantu untuk halang penghasilan asid urik. Ada bahan milk thistle dan bromelain, dan ianya bebas gula serta ianya adalah organik."),
    seg("S05", 61.10, 66.25, "Jus gout ni bantu untuk halang penghasilan asid urik dan seimbangkan paras asid urik korang.", "first take 51.9 dropped"),
    seg("S06", 80.60, 86.60, "Cuma perlu campurkan dua skop jus gout ni dalam 250ml air panas dan kacau hingga larut.", "takes 66.8 and 76.5 dropped"),
    seg("S07", 87.20, 90.90, "Rasanya tu sangat sedap sebab perisa dia, perisa nenas."),
    seg("S08", 91.20, 93.65, "Dan ianya 100% natural tau."),
    seg("S09", 94.30, 97.75, "So kalau korang ada masalah gout, bolehlah cuba jus gout ni kat beg kuning."),
    seg("S10", 101.92, 106.20, "Sekarang ni banyak seller dah buat promo untuk 11 hari bulan 11 tau.", "first take 98.2 dropped"),
    seg("S11", 106.38, 113.58, "Cuba tengok dekat beg kuning ada voucher tak. Kalau ada boleh claim, dan sementara harga masih murah tu, korang boleh dapatkan terus di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": False, "caption_style": "word2", "fs_style": "cut", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: Drive folder 1R0pfbEi… 'Jus Gout' with 'video rujukan.mp4' (a faceless Jus Gout product video by another creator). Copied from the reference: product footage over the voice for almost the whole video (jar in hand, back label, opening, two scoops into the cup, hot water, stirring, the finished juice), hard cuts with a few quick white flashes / black dips, a 'Jus Gout Promaxx' title at the start, and no subtitles (the reference has none). The owner's face stays only where he holds the jar for the closing pitch and CTA. 1 Nov: keep every point; product close-ups and the owner using the product.",
     "_note": "Jus Gout Promaxx #13 — A-roll assets/a.mp4 = VID_20261104_153048 (front camera saved mirrored — 'GOUT' reads backwards — flipped back in CSS). B-roll assets/b.mp4 = VID_20261012_172341 (also in #11/#12; muted): jar in hand 2-24 (back label 12-17), top-down jar 28-40, opening 40-52, scoops into the cup 54-110, hot water and stirring 112-210. Ingredients as spoken: bromelain, milk thistle, lemon extract, curcuma longa root extract, ginger extract, orange extract (six). Promo '11 hari bulan 11' and vouchers are the owner's own words; no price.",
     "segments": segs,
     "stamp": [{"from": ["S01", "start"], "to": ["S02", "start"], "text": "Jus Gout Promaxx", "x": 330, "y": 210}],
     "flash": [[["S02", "start"], "#FFFFFF"], [["S04", "start"], "#000000"], [["S06", "start"], "#FFFFFF"], [["S09", "start"], "#FFFFFF"]],
     "punch": [["S11", "claim", 1.06]],
     "broll": [br("B1", ["S01", "start"], ["S02", "start"], 4.0, "172341: balang Jus Gout di tangan", (1.0, 1.06), "50% 40%"),
               br("B2", ["S02", "start"], ["S02b", "end"], 6.2, "172341: balang dipusing", (1.0, 1.06), "50% 40%"),
               br("B3", ["S03", "start"], ["S03", "bahan"], 12.4, "172341: label belakang", (1.05, 1.15), "50% 40%"),
               br("B4", ["S03", "bahan"], ["S03c", "end"], 28.5, "172341: balang dari atas", (1.0, 1.08)),
               br("B5", ["S04", "start"], ["S04", "ada"], 40.5, "172341: buka balang (guna produk)"),
               br("B6", ["S04", "ada"], ["S04", "end"], 18.0, "172341: balang depan", (1.0, 1.08), "50% 40%"),
               br("B7", ["S05", "start"], ["S05", "end"], 58.0, "172341: skop serbuk ke cawan (guna produk)"),
               br("B8", ["S06", "start"], ["S06", "dalam"], 70.0, "172341: skop kedua (guna produk)"),
               br("B9", ["S06", "dalam"], ["S06", "end"], 128.0, "172341: kacau dalam air panas (guna produk)"),
               br("B10", ["S07", "start"], ["S07", "end"], 196.0, "172341: jus siap dikacau"),
               br("B11", ["S08", "start"], ["S08", "end"], 20.5, "172341: balang depan", (1.0, 1.08), "50% 40%"),
               br("B12", ["S10", "start"], ["S10", "end"], 202.0, "172341: jus siap")],
     "photos": [],
     "theme": {"key": "#F2B705", "brand": "#C0392B"},
     "brand_words": ["promaxx"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
