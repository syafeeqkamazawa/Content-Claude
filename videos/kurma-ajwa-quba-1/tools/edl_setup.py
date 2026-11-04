"""EDL for kurma-ajwa-quba-1 (VID_20261104_170514), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 27.00, 31.15, "Kurma Ajwa, kurma ni disebut Kurma Nabi tau,", "HOOK, second take (first, 3.3-22.7, stumbles)"),
    seg("S02", 33.10, 35.40, "sebab kurma ni berasal dari Madinah,", "'kerana kurma' false start dropped"),
    seg("S03", 36.30, 42.75, "dan sangat disukai oleh Nabi Muhammad SAW. Dan Nabi sebutkan beberapa keutamaan kurma Ajwa ni."),
    seg("S04", 43.30, 46.70, "Di antaranya, membentengi dari sihir dan racun."),
    seg("S05", 47.30, 53.60, "Dan secara sains pun ternyata, kurma ni kandungannya luar biasa tau."),
    seg("S06", 58.80, 62.40, "Antioksidannya, vitaminnya, mineralnya,"),
    seg("S07", 64.90, 67.45, "asid aminonya, lengkap sangat."),
    seg("S08", 72.00, 74.50, "Puasa pun dah tak lama."),
    seg("S09", 78.30, 80.50, "Bolehlah standby awal-awal kurma Ajwa ni.", "'bolehlah standby, bolehlah' stumbles dropped"),
    seg("S10", 81.90, 83.85, "Kalau kat luar, mungkin lagi mahal."),
    seg("S11", 95.80, 98.70, "Tambah pula ramai seller dah buat promo 11.11 tau.", "stumbling lines 84.8-94.4 dropped"),
    seg("S12", 106.00, 108.60, "Cuba tengok dekat beg kuning, berapa harga yang korang dapat.", "takes 99.3, 102.3, 109.4 dropped"),
    seg("S13", 113.85, 116.60, "Kalau harga tu tengah murah, bolehlah beli awal-awal.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 3, "chars": 18, "highlight": True, "on": "#3DD6F5", "top": 960, "size": 58}, "fs_style": "fade", "mirror": MIRROR,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: Drive folder 17vMTWca… 'Quba Food Kurma Ajwa' with 'Kurma ajwa rujukan overlay dan caption.mp4'. Copied from the reference: captions of 2-3 upper-case heavy white words with the spoken word in light blue, hard cuts, sitting above the product; overlays = product footage (pouch, opening, dates in hand, eating) and fitting full-screen shots that crossfade in. Not copied: the reference's 'Video Tips Sehat' watermark and the small red arrow icon (owner: no symbol icons). 1 Nov: keep every point; product close-ups and the owner using the product.",
     "_note": "Quba Food Kurma Ajwa #1 — A-roll assets/a.mp4 = VID_20261104_170514 (front camera). B-roll assets/b.mp4 = VID_20261104_171041 (muted; no speech): pouch 0-8, opening 8-12, dates close-up 12-20, a date in hand 20-24, eating 24-32, thumbs up 32-34, closing the pouch 36-44. Clip -> video: both clips in this one video. The keutamaan (sihir dan racun) line is the owner's own words; promo 11.11 his own words; no price.",
     "segments": segs,
     "punch": [["S13", "beli", 1.06]],
     "broll": [br("B1", ["S03", "dan#2"], ["S03", "end"], 2.0, "171041: pouch Kurma Ajwa", (1.0, 1.06), "50% 40%"),
               br("B2", ["S05", "kandungannya"], ["S05", "end"], 13.0, "171041: kurma dalam pouch (close-up)"),
               br("B3", ["S07", "start"], ["S07", "end"], 20.5, "171041: sebiji kurma di tangan"),
               br("B4", ["S09", "start"], ["S09", "end"], 24.5, "171041: makan kurma (guna produk)"),
               br("B5", ["S11", "start"], ["S11", "end"], 32.0, "171041: thumbs up"),
               br("B6", ["S12", "start"], ["S12", "end"], 9.0, "171041: buka pouch (guna produk)")],
     "photos": [ph("madinah", ["S02", "start"], ["S02", "end"], "AI: Masjid Nabawi, Madinah"),
                ph("ladang", ["S03", "start"], ["S03", "dan#2"], "AI: ladang kurma"),
                ph("sains", ["S06", "start"], ["S06", "end"], "AI: kurma ajwa macro"),
                ph("iftar", ["S08", "start"], ["S08", "end"], "AI: hidangan berbuka")],
     "theme": {"key": "#3DD6F5", "brand": "#E9C46A"},
     "brand_words": ["ajwa"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
