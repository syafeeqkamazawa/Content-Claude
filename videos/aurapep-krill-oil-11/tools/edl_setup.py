"""EDL for aurapep-krill-oil-11 (VID_20261104_151832), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)


segs = [
    seg("S01", 4.40, 10.85, "Sekarang ni tengah viral guys, berkenaan dengan krill oil yang dikatakan lagi baik berbanding dengan omega biasa.", "HOOK"),
    seg("S02", 22.90, 28.45, "Saya dah cuba, alhamdulillah ada perubahan sejak saya amalkan krill oil daripada Aurapep ni.", "first take 11.8 dropped"),
    seg("S03", 28.55, 34.00, "Sebab apa? Dia sangat berkualiti dan ada kelulusan daripada KKM dan halal JAKIM tau."),
    seg("S04", 34.50, 40.90, "Krill oil ni memang dapat bantu untuk support kesihatan jantung kita, bantu support kesihatan mata kita,"),
    seg("S05", 44.60, 49.60, "dan juga bantu support kesihatan otak kita supaya daya ingatan kita jadi lebih baik."),
    seg("S06", 74.20, 76.60, "Dan juga support sistem saraf kita tau,", "stumbling takes 49.6-69.6 dropped"),
    seg("S07", 78.38, 81.40, "yang kita rasa selalu lenguh-lenguh dan kebas-kebas tu kan?"),
    seg("S08", 82.10, 91.20, "Dalam setiap kapsul ni mengandungi krill oil, mengandungi omega 3, mengandungi DHA dan juga EPA, astaxanthin, vitamin D3 dan juga vitamin K2.", "label: Rich in Astaxanthin & Vitamin D3 & K2"),
    seg("S09", 96.30, 98.50, "Kesemuanya dapat bantu support kesihatan kita."),
    seg("S10", 98.64, 107.82, "Harga dia sedikit mahal berbanding omega biasa, tapi berbaloi dengan manfaat yang dia boleh support mata, otak, jantung dan juga saraf kita."),
    seg("S11", 170.30, 174.75, "Satu botol ni ada 40 softgel. Satu hari cukup kita makan 2 softgel sahaja.", "quiet stretch 108-160 and takes 159-169 dropped"),
    seg("S12", 193.10, 200.90, "Sekarang ni banyak seller tengah buat promo 11.11 tau. Cuba tengok dekat beg kuning harga dia berapa. Aurapep ni antara yang termurah tau.", "first take 182.9 dropped"),
    seg("S13", 228.20, 234.00, "Kepada yang berminat nak cuba, boleh dapatkan segera dekat beg kuning, sementara masih ada stok dan harga dia masih murah.", "CTA, last of four takes (200.9-225.6)", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word2",
     "word2": {"top": 1640, "size": 64, "weight": 800, "stroke": "#2B1CF0", "stroke_w": 12}, "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: 'Video saya bercakap krill oil aurapep ada yang satu lagi. Buatkan juga yang tu' — second talking clip in Drive folder 1irOVOgs… with a second reference (TikDownloader…mp4, another creator's Aurapep video; the owner follows its script). Copied from that reference: a hook banner at the top — black condensed upper-case lines on bright green bars — for the opening seconds, then one upper-case white word at a time with a thick blue-violet outline low in the frame, hard cuts, and mostly talking head with product close-ups. The banner carries the owner's own hook (the reference's wording is not copied). 1 Nov: keep every point; product close-ups and the owner using the product.",
     "_note": "Aurapep Krill Oil #11 — A-roll assets/a.mp4 = VID_20261104_151832 (front camera, mirrored back in CSS). B-roll assets/b.mp4 = the krill-10 pool (hard link): P 0-33.91 = VID_20261104_151915 (#11 uses 15-33: drinking the softgel, thumbs up; #10 used 0-14), Q 33.91-73.24 = VID_20261021_091344, R 73.24-163.7 = VID_20261022_092840; picks avoid #10's (Q 36.2-38.8, 41-48.6, 55.2-57.7, 59.5-63.9, P 9.5-10.3, R 130.3-133.8). Clip -> video: 145248 -> #10, 151832 -> #11, 151915 split between them. Claims, dose (2 softgel sehari), 'termurah' and promo 11.11 are the owner's own words; no price figure.",
     "segments": segs,
     "banner": {"lines": ["Krill oil tengah viral,", "lagi baik dari omega biasa?"], "to": ["S02", "start"]},
     "punch": [["S13", "dapatkan", 1.06]],
     "broll": [br("B1", ["S02", "amalkan"], ["S02", "end"], 19.2, "151915: owner minum softgel (guna produk)", (1.0, 1.05)),
               br("B2", ["S03", "kelulusan"], ["S03", "end"], 49.6, "091344: buka botol Aurapep", (1.0, 1.06)),
               br("B3", ["S08", "start"], ["S08", "dha"], 64.0, "091344: softgel merah + botol", (1.0, 1.06)),
               br("B4", ["S08", "dha"], ["S08", "end"], 121.0, "092840: softgel ke kamera (guna produk)", (1.0, 1.05), "50% 55%"),
               br("B5", ["S11", "start"], ["S11", "end"], 110.3, "092840: botol dibuka, penutup ke kamera", (1.0, 1.05), "50% 55%"),
               br("B6", ["S12", "aurapep"], ["S12", "end"], 23.0, "151915: owner thumbs up", (1.0, 1.05))],
     "photos": [],
     "theme": {"key": "#3CEB2E", "brand": "#2B1CF0"},
     "brand_words": ["aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
