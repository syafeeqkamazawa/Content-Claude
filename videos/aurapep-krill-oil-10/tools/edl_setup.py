"""EDL for aurapep-krill-oil-10 (VID_20261104_145248), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 24.80, 27.15, "Makan yang ni sehari maksimum dua biji je.", "HOOK, third take (11.2, 19.4 dropped)"),
    seg("S02", 27.25, 36.50, "Dia bagus untuk sendi kita, bagus untuk kita punya mata, untuk otak, kuatkan ingatan kita, bagus juga untuk kesihatan jantung."),
    seg("S03", 37.00, 39.60, "So ini adalah krill oil daripada Aurapep."),
    seg("S04", 43.00, 48.30, "Dia lagi power daripada omega fish oil yang biasa, dan dia lagi power daripada astaxanthin yang biasa.", "first take 39.9 ('omega fish biasa') dropped"),
    seg("S05", 61.40, 66.55, "Yang ni, dalam ni dah siap ada omega 3, omega 6, omega 9.", "stumbling take 51-58.7 dropped"),
    seg("S06", 70.20, 72.85, "So dia sangat bagus untuk kesihatan kita secara keseluruhan.", "repeat 66.7-70 dropped"),
    seg("S07", 77.80, 80.10, "Dan dia juga sangat bagus untuk sistem saraf kita.", "first take 73.1 dropped"),
    seg("S08", 95.80, 99.70, "Terutamanya untuk akak abang yang selalu rasa kebas-kebas dekat tangan dan kaki kan?", "takes 80.6 and 91.6 dropped"),
    seg("S09", 99.90, 103.90, "Yang sendi-sendi selalu rasa lenguh tu, nak bergerak pun sakit, nak solat pun sakit."),
    seg("S10", 114.08, 116.10, "Rukuk sujud pun tak selesa kan?", "first take 104-112 dropped"),
    seg("S11", 120.20, 124.55, "Juga ada astaxanthin, sejenis antioksidan yang sangat kuat."),
    seg("S12", 154.40, 157.05, "Satu lagi yang ramai suka, dia tak ada bau hanyir tau.", "takes 125-152 dropped"),
    seg("S13", 157.10, 159.75, "Kalau lepas makan pun, bila sendawa tak keluar bau ikan."),
    seg("S14", 178.10, 181.60, "Kalau sesetengah fish oil atau krill oil tu, ada yang bau tau.", "takes 159.8-177.6 dropped"),
    seg("S15", 182.00, 182.80, "Yang ni tak ada."),
    seg("S16", 193.70, 196.50, "Dalam banyak-banyak supplement, yang ni harga dia tinggi sikit,", "first take 183.5-192.6 dropped"),
    seg("S17", 197.90, 204.00, "tapi kualiti dia sangat berbaloi dengan harga dia. Jenama Aurapep ni antara krill oil yang harga dia sangat berpatutan,"),
    seg("S18", 204.10, 207.35, "mampu milik, ada halal, lulus KKM juga."),
    seg("S19", 220.35, 224.30, "Jadi ibu ayah, abang, kakak boleh cuba beli yang ni, lagi berbaloi.", "takes 207.7-219 dropped"),
    seg("S20", 246.20, 249.60, "Sekarang ni banyak seller dah buat harga promo 11.11 tau.", "first takes 231-238 dropped"),
    seg("S21", 249.90, 253.90, "Cuba tengok dekat beg kuning, kalau nampak harga tengah murah tu, terus check out, okey?", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 2, "chars": 16, "highlight": False, "top": 1600, "size": 60}, "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: Drive folder 1irOVOgs… 'Aurapep Krill Oil' with 'video rujukan.mp4' (another creator's Aurapep review; the owner follows its script). Copied from the reference: captions of two upper-case heavy white words low in the frame with a soft shadow, hard cuts; full-screen cutaways — glowing blue x-ray renders (body, brain, eyes + brain, heart, nervous system), numb hands, aching knee, fish-oil softgels — and product close-ups. The reference's brand infographics (Astaxanthin Antioxidant Support, Advanced Formula, KKM certificate) are not available and are not recreated. Aurat: the x-ray bodies are cropped to head-to-chest; every man wears long sleeves and long trousers. 1 Nov: keep every point; product close-ups and the owner using the product.",
     "_note": "Aurapep Krill Oil #10 — A-roll assets/a.mp4 = VID_20261104_145248 (front camera saved mirrored — 'aurapep' reads backwards — flipped back in CSS). B-roll pool assets/b.mp4 (muted): P 0-33.91 = VID_20261104_151915 (owner shows a softgel 3-14 and drinks it 15-27; #10 uses 0-14 only, 15-33 is kept for #11), Q 33.91-73.24 = VID_20261021_091344 (bottle and softgels on grass), R 73.24-163.7 = VID_20261022_092840 (owner at the table). Clip -> video: 145248 -> #10, 151832 -> #11. Claims and dose are the owner's own words ('maksimum dua biji', omega 3/6/9, astaxanthin, halal, lulus KKM, promo 11.11); no price figure quoted.",
     "segments": segs,
     "hook_text": {"kicker": "Aurapep Krill Oil", "lines": ["Lagi power", "dari fish oil?"], "accent_words": ["power", "fish", "oil?"],
                   "to": 2.3, "accent": "#E8B44C", "accent2": "#7FA8FF", "top": 140},
     "punch": [["S21", "check", 1.06]],
     "broll": [br("B2", ["S03", "start"], ["S03", "end"], 36.2, "091344: botol Aurapep atas rumput", (1.0, 1.08), "50% 40%"),
               br("B3", ["S04", "astaxanthin"], ["S04", "end"], 55.2, "091344: botol + softgel merah dalam penutup"),
               br("B4", ["S05", "start"], ["S05", "end"], 41.0, "091344: botol Aurapep di tangan", (1.0, 1.08), "50% 40%"),
               br("B5", ["S11", "start"], ["S11", "end"], 59.5, "091344: softgel merah dalam penutup + botol"),
               br("B6", ["S15", "start"], ["S15", "end"], 9.5, "151915: softgel di jari", (1.0, 1.05)),
               br("B7", ["S17", "jenama"], ["S17", "end"], 44.0, "091344: botol depan", (1.0, 1.08), "50% 40%"),
               br("B8", ["S19", "start"], ["S19", "end"], 130.3, "092840: softgel di tapak tangan (guna produk)", (1.0, 1.06), "50% 55%")],
     "photos": [ph("lutut", ["S02", "start"], ["S02", "mata"], "AI: sendi lutut"),
                ph("x_mata", ["S02", "mata"], ["S02", "otak"], "AI: x-ray mata + otak"),
                ph("x_otak", ["S02", "otak"], ["S02", "jantung"], "AI: x-ray otak"),
                ph("x_jantung", ["S02", "jantung"], ["S02", "end"], "AI: x-ray jantung"),
                ph("ikan", ["S04", "start"], ["S04", "astaxanthin"], "AI: softgel minyak ikan"),
                ph("x_badan", ["S06", "start"], ["S06", "end"], "AI: x-ray badan (kepala-dada)"),
                ph("x_saraf", ["S07", "start"], ["S07", "end"], "AI: sistem saraf (kepala-dada)"),
                ph("kebas", ["S08", "kebas-kebas"], ["S08", "end"], "AI: tangan kebas"),
                ph("sendawa", ["S13", "start"], ["S13", "end"], "AI: sendawa selepas makan")],
     "theme": {"key": "#E8B44C", "brand": "#7FA8FF"},
     "brand_words": ["aurapep", "aurapep."], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
