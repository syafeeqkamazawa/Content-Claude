"""EDL for mixed-nuts-1 (VID_20261105_105650), 5 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.35), origin="45% 72%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 12.20, 15.84, "Snek ni, snek yang sihat, anak pun suka makan tau.", "HOOK (false starts 3.8-12.0 and the unclear 'tempah je mix snack ni' dropped)"),
    seg("S02", 24.90, 29.97, "Yang ni healthy roasted mix snack tau, campuran tujuh jenis buah dan kekacang.", "'yang ni hel-' false start (17.6) dropped"),
    seg("S03", 29.97, 33.35, "Semua yang rangup, manis, semula jadi dan halal pula tu.", "continues S02 without a cut"),
    seg("S04", 33.50, 36.30, "Yang paling best, dalam ni banyak gila kacang walnut."),
    seg("S05", 36.60, 41.40, "Brand lain selalunya bagi dua tiga biji je, tapi yang ni penuh satu pack, pemurah betul."),
    seg("S06", 44.50, 48.85, "Kacang dia crispy, buah-buah dia manis tau, anak pun boleh makan tanpa rasa bersalah."),
    seg("S07", 49.68, 56.20, "At least bila nak snacking, dapat juga khasiat dari kekacang dan buah kering tu. Jadi kalau korang tengah cari snek sihat untuk anak-anak,"),
    seg("S08", 59.30, 62.35, "ni antara yang paling berbaloi tau. Try bagi anak korang yang ni.", "first take 56.4 dropped"),
    seg("S09", 85.40, 86.75, "Confirm tak cari jajan dah.", "takes 62.7-84.2 dropped"),
    seg("S10", 98.90, 102.65, "Apa lagi korang, sekarang ni seller dah banyak buat promo 11.11 tau.", "'apa lagi korang' false starts 86.7-97 dropped"),
    seg("S11", 115.90, 119.55, "Kalau berminat, korang grab sekarang. Tengok dekat beg kuning berapa harga dan terus beli.", "CTA (takes 104-115 dropped)", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 3, "chars": 18, "highlight": False, "box": True, "top": 1770, "size": 40}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "5 Nov: Drive folder 1PmTRs8K… 'Mixed Nuts' — 'Sepatutnya ada dua video akan disiapkan. Ada satu file video penuh dan untuk konten kedua ada beberapa file video yang perlu digabungkan. Rujuk video contoh dan buat overlay semirip mungkin dengan video contoh'. This full clip follows TikDownloader…7567006964455197972 (Lucky Deer mix nuts, the same script): a fixed white sentence with a dark outline near the top for the whole video, small 2-3-word captions on a dark box, and most of the talk covered by product shots that crossfade in — a tray / container full of nuts, nuts poured into a container, a child eating, plus the owner's own pouch close-ups. Aurat: the AI child wears a hijab and long sleeves; every person covers aurat.",
     "_note": "Mixed Nuts #1 — A-roll assets/a.mp4 = VID_20261105_105650 (front camera saved mirrored — 'MIXED NUTS' reads backwards — flipped back in CSS). B-roll assets/b.mp4 = flipped crops of the same clip (muted): pouch front 0-9 (src 38-47), open pouch full of nuts 9-21 (src 68-80) and 21-46 (src 88-113). Clip -> video: 105650 -> #1; 110040 + 110249 (+ 110137 pouch shots) -> #2; 105911 is camera set-up only. Claims are the owner's own words (7 jenis buah dan kekacang, halal, banyak walnut, promo 11.11); no price.",
     "segments": segs,
     "pin": {"text": "Snacking sihat untuk anak dengan mix nuts ni. Paling best walnut penuh satu pek!", "y": 330, "size": 40},
     "punch": [["S11", "grab", 1.06]],
     "broll": [br("B1", ["S02", "healthy"], ["S02", "end"], 0.5, "105650: pouch depan", (1.05, 1.4), "50% 70%"),
               br("B2", ["S05", "tapi"], ["S05", "end"], 11.5, "105650: pouch terbuka penuh kacang (guna produk)"),
               br("B3", ["S07", "start"], ["S07", "jadi"], 26.0, "105650: kacang dalam pouch"),
               br("B4", ["S08", "try"], ["S08", "end"], 6.2, "105650: pouch depan", (1.05, 1.4), "50% 70%"),
               br("B5", ["S10", "start"], ["S10", "end"], 15.0, "105650: kacang dalam pouch")],
     "photos": [ph("anak", ["S01", "anak"], ["S01", "end"], "AI: anak (bertudung) makan kacang"),
                ph("bekas", ["S03", "start"], ["S03", "end"], "AI: bekas penuh kacang"),
                ph("walnut", ["S04", "start"], ["S04", "end"], "AI: dulang kacang dengan walnut"),
                ph("tuang", ["S06", "start"], ["S06", "end"], "AI: kacang dituang ke bekas"),
                ph("jajan", ["S09", "start"], ["S09", "end"], "AI: anak pilih kacang, bukan jajan")],
     "theme": {"key": "#FFFFFF", "brand": "#E9C46A"},
     "brand_words": [], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
