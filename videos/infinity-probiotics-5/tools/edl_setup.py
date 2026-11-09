"""EDL for infinity-probiotics-5 (VID_20261109_201010 0-86.5 s), 9 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
P1 = 86.5167          # b.mp4 = A-roll copy (0-86.52) + VID_20261104_154051 (grass close-ups) + VID_20261014_001726 (shelf close-ups)
P2 = P1 + 74.316


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 50%", push=(1.02, 1.1), note="the owner's own close-up of Infinity Probiotics Plus (on the grass at home)"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=210, size=118): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


segs = [
    seg("S01", 10.80, 15.00, "Sebenarnya kita punya usus, kita kena jaga tau,", "HOOK — silence before (0-10.8) dropped"),
    seg("S02", 15.00, 15.95, "sebab", "stumbles 'hampir, kita punya' (15.9-19.7), 'kita punya, badan-' (21.2-23.4) and 'yang, apa' (26-27.8) dropped"),
    seg("S02b", 19.72, 21.16, "hampir keseluruhan,"),
    seg("S02c", 23.40, 26.00, "badan kita punya simptom"),
    seg("S02d", 27.85, 33.00, "yang ada pada badan kita, kebanyakannya berpunca daripada usus."),
    seg("S03", 33.00, 41.56, "Contoh macam nafas berbau, so kadang-kadang bukan sebab kita tak jaga gosok gigi, tapi sebenarnya daripada perut kita."),
    seg("S04", 41.56, 44.65, "So usus tu kita kena jaga."),
    seg("S05", 44.55, 45.15, "So", "stumble 'antara, apa, eh eh' (45.2-49.6) dropped"),
    seg("S05b", 49.60, 54.40, "antara yang saya boleh sarankan, boleh ambil ni, probiotik daripada Infinity ni."),
    seg("S06", 55.80, 63.42, "Lagi penting, ada halal tau. Ada halal JAKIM dan juga dia ada KKM punya nombor siri.", "stumble 'yang apa' (54.4-55.7) dropped"),
    seg("S07", 63.42, 65.50, "So jangan risau, trusted insya-Allah."),
    seg("S08", 66.10, 77.62, "Infinity Probiotic Plus ni insya-Allah, dia ada 5 probiotik, 1 prebiotik dan juga 3 digestive enzyme. Memang sangat trusted lah insya-Allah."),
    seg("S09", 77.62, 81.55, "So boleh dapatkan di beg kuning, harga tengah murah ni, promosi tengah berjalan,"),
    seg("S10", 82.80, 85.70, "promosi 11.11 pun masih ada. Okay, dapatkan di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1600}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.14, "threshold_db": -30, "blip": 0.03}, "titles": [],
     "_owner_decisions": "9 Nov: two talking clips filmed in the car (VID_20261109_201010 — six products — and 195852 — Shilajit), one video per product. Owner: 'Gunakan caption style latest' → the 6 Nov caption, set low (top 1600, on the shirt) since the face is mid-frame and the product is held in front of the chest; 'Buat overlay full cover waktu nak visualkan masalah' → full-screen realistic photos for each problem; 'highlight text dengan font huruf besar … motion … sesuai dengan tema produk' → EDL kp (big Anton words, key words in the Infinity yellow, colour bar wipe) on every key point, set on the car ceiling above the head; 'overlay dari klip … produk close up dekat rumput rumah saya' → VID_20261104_154051 (box, bottle, capsules on the grass) first, then the shelf close-ups VID_20261014_001726; phone mic → tools/voice.sh. The night car footage is lifted slightly (gamma 1.10).",
     "_note": "Infinity Probiotics Plus #5 — A-roll assets/a.mp4 = VID_20261109_201010 0-86.5 s (rear camera, not mirrored). 5 probiotik / 1 prebiotik / 3 digestive enzyme, halal JAKIM, KKM and promo 11.11 are the owner's own words; no price. Whisper hears the brand as 'Envora' — it is Infinity.",
     "segments": segs,
     "kp": [kp("JAGA USUS!", ["USUS!"], ["S01", "usus,"], ["S01", "end"], "zoom"),
            kp("PUNCA: USUS", ["USUS"], ["S02d", "kebanyakannya"], ["S02d", "end"], "slam"),
            kp("NAFAS BERBAU?", ["BERBAU?"], ["S03", "start"], ["S03", "bukan"], "slam"),
            kp("BUKAN SEBAB / GOSOK GIGI", ["GIGI"], ["S03", "bukan"], ["S03", "tapi"], "slide", 210, 104),
            kp("HALAL JAKIM / KKM", ["JAKIM", "KKM"], ["S06", "halal"], ["S06", "end"], "rise"),
            kp("5 PROBIOTIK / 1 PREBIOTIK / 3 ENZIM", ["5", "1", "3"], ["S08", "5"], ["S08", "memang"], "slide", 170, 104),
            kp("PROMO 11.11", ["11.11"], ["S10", "start"], ["S10", "okay,"], "zoom")],
     "punch": [["S10", "dapatkan", 1.06]],
     "broll": [cu("C1", ["S05b", "probiotik"], ["S05b", "end"], P1 + 9.5),
               cu("C2", ["S06", "start"], ["S07", "end"], P1 + 28.0),
               cu("C3", ["S08", "start"], ["S08", "memang"], P1 + 50.0),
               cu("C4", ["S08", "memang"], ["S08", "end"], P2 + 40.0, note="the owner's own close-up: capsules in the palm"),
               cu("C5", ["S09", "start"], ["S09", "end"], P2 + 14.0, note="the owner's own close-up: the bottle")],
     "photos": [ph("penat", ["S02", "start"], ["S02d", "kebanyakannya"], "AI: simptom badan (berlengan panjang)"),
                ph("usus", ["S02d", "kebanyakannya"], ["S02d", "end"], "AI: ilustrasi usus"),
                ph("nafas", ["S03", "start"], ["S03", "bukan"], "AI: nafas berbau (berlengan panjang)"),
                ph("gigi", ["S03", "bukan"], ["S03", "tapi"], "AI: berus gigi (tiada orang)"),
                ph("perut", ["S03", "tapi"], ["S03", "end"], "AI: model perut & usus (tiada orang)")],
     "theme": {"key": "#F2B705", "brand": "#2BB3C0"},
     "brand_words": ["infinity"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
