"""EDL for vteay-fish-oil-5 (VID_20261109_201010 287.5-373.5 s), 9 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 57%", push=(1.5, 1.6), note="close-up of the VTEAY bottle in the owner's hand (same moment)"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=210, size=118): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


segs = [
    seg("S01", 9.30, 11.36, "Seller baru restock korang!", "HOOK — the tail of the previous product (0-6) and a pause dropped"),
    seg("S02", 15.00, 19.95, "Hari tu lama juga stock dah sold out, sekarang seller dah restock balik.", "first take 'hari tu lama juga seller dah sold out' (11.4-15) dropped"),
    seg("S03", 19.95, 25.75, "Masya-Allah korang, ni fish oil antara yang termurah di dalam TikTok."),
    seg("S04", 27.45, 30.42, "Walaupun dia murah, jangan risau, ada dia punya", "stumble 'apa tu' (30.4-32.2) dropped"),
    seg("S04b", 32.20, 38.38, "halal, ada, dan KKM pun ada. Boleh tengok dekat beg kuning, dan feedback pun memang padu-padu.", "'fish oil ni dia boleh bantu … kalau rasa lenguh-lenguh, kebas-kebas' (38.4-44.2) dropped — TikTok risk (as VTEAY #1-#4)"),
    seg("S05", 44.55, 50.88, "Lepas tu dalam fish oil VTEAY ni ada EPA dan DHA sekali tau,"),
    seg("S06", 55.10, 56.28, "kandungan dia tu banyak.", "stumble 'dan banyak dia punya' (50.9-55.1) dropped"),
    seg("S07", 56.28, 64.62, "So dia EPA DHA ni dia boleh bantu juga untuk bantu kita punya sistem otak, kita punya jantung, mata.", "'untuk bantu kita punya bahagian-bahagian yang saya sebutkan tadi' (64.6-70) dropped — repeat"),
    seg("S08", 70.88, 74.32, "Dapatkan di beg kuning, memang harga tengah murah ni, seller tengah buat promosi."),
    seg("S09", 75.00, 82.18, "Stok pun cepat habis ni. Sementara stok ada tu, beli 2-3 botol terus. Nanti bila dah sold out, kita dah ada stand by kan."),
    seg("S10", 83.58, 85.25, "Abang kakak, dapatkan di beg kuning sekarang.", "CTA — 'ok, so, ibu ya' (82.5-83.6) dropped", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1600}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.14, "threshold_db": -30, "blip": 0.03}, "titles": [],
     "_owner_decisions": "9 Nov: car talking clip VID_20261109_201010 → one video per product; this is the VTEAY Fish Oil part (287.5-373.5 s). 6 Nov caption set low (top 1600); full-screen realistic photos (shopping, softgels, x-ray brain / heart / eyes, boxes of stock); big kinetic key-point text (EDL kp) in the VTEAY blue on the car ceiling; no separate B-roll of this product in Drive, so close-ups come from the owner holding the bottle up; phone mic → tools/voice.sh.",
     "_note": "VTEAY Omega-3 Fish Oil #5 — A-roll assets/a.mp4 = VID_20261109_201010 287.5-373.5 s (rear camera, not mirrored). assets/b.mp4 = the same clip, muted. Restock, 'antara yang termurah di TikTok', halal, KKM, EPA/DHA, promo are the owner's own words; no price.",
     "segments": segs,
     "kp": [kp("RESTOCK!", ["RESTOCK!"], ["S01", "restock"], ["S01", "end"], "slam", 210, 150),
            kp("SOLD OUT → RESTOCK", ["RESTOCK"], ["S02", "sold"], ["S02", "end"], "slide", 210, 104),
            kp("ANTARA TERMURAH / DI TIKTOK", ["TERMURAH"], ["S03", "antara"], ["S03", "end"], "zoom", 180, 108),
            kp("HALAL • KKM", ["HALAL", "KKM"], ["S04b", "start"], ["S04b", "boleh"], "rise", 210, 130),
            kp("FEEDBACK PADU", ["PADU"], ["S04b", "feedback"], ["S04b", "end"], "split"),
            kp("EPA • DHA", ["EPA", "DHA"], ["S05", "EPA"], ["S06", "end"], "slam", 210, 140),
            kp("OTAK • JANTUNG / MATA", ["OTAK", "JANTUNG", "MATA"], ["S07", "sistem"], ["S07", "end"], "rise", 180, 110),
            kp("BELI 2-3 BOTOL", ["2-3"], ["S09", "beli"], ["S09", "nanti"], "zoom")],
     "punch": [["S10", "dapatkan", 1.06]],
     "broll": [cu("C1", ["S04", "start"], ["S04b", "feedback"], 34.0, "48% 58%"),
               cu("C2", ["S08", "start"], ["S08", "end"], 72.0, "57% 55%"),
               cu("C3", ["S09", "nanti"], ["S09", "end"], 79.0, "53% 55%")],
     "photos": [ph("belanja", ["S03", "start"], ["S03", "end"], "AI: membeli di TikTok (bertudung)"),
                ph("softgel", ["S05", "start"], ["S06", "end"], "AI: softgel minyak ikan"),
                ph("x_otak", ["S07", "sistem"], ["S07", "jantung,"], "AI: x-ray otak"),
                ph("x_jantung", ["S07", "jantung,"], ["S07", "mata."], "AI: x-ray jantung"),
                ph("x_mata", ["S07", "mata."], ["S07", "end"], "AI: x-ray mata"),
                ph("stok", ["S09", "start"], ["S09", "nanti"], "AI: kotak stok (tiada orang)")],
     "theme": {"key": "#5FB8E0", "brand": "#FFFFFF"},
     "brand_words": ["vteay"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
