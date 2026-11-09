"""EDL for natures-key-mg-3 (VID_20261109_201010 85-164.5 s), 9 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
N1 = 79.55            # b.mp4 = A-roll copy (0-79.55) + VID_20261014_153135 0-36 (Nature's Key label / capsules close-ups)


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 50%", push=(1.02, 1.1), note="the owner's own close-up of Nature's Key Magnesium Capsules"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=210, size=118): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


segs = [
    seg("S01", 13.00, 15.98, "Yang ada simptom, contoh,", "HOOK — the long pause before (0-13) dropped"),
    seg("S02", 18.55, 25.30, "susah nak bangun pagi, ataupun nak berehat waktu malam tu susah,", "first 'susah nak bangun' (16-18.5) dropped"),
    seg("S03", 28.10, 30.92, "kadang otak rasa penat,", "'ataupun' + pause (25.3-28.1) dropped"),
    seg("S04", 40.10, 42.80, "tiba-tiba rasa pening,", "'ataupun, apa lagi, contoh macam' (31-40) dropped"),
    seg("S05", 42.94, 45.40, "macam tak boleh nak fokus sangat.", "stutter 'macam tak' → one 'tak' (42.8-42.9) dropped"),
    seg("S06", 45.40, 50.50, "So boleh dapatkan Magnesium Capsule daripada Nature's Key ni, ada halal,"),
    seg("S07", 51.15, 58.35, "insya-Allah, so jangan risau. Okay, Nature's Key ni trusted brand lah, korang tengok dekat beg kuning, feedback pun memang padu-padu semua."),
    seg("S08", 59.95, 66.00, "Magnesium Capsule daripada Nature's Key ni memang sangat membantu kita untuk masalah-masalah yang saya sebutkan tadi."),
    seg("S09", 68.36, 69.40, "Untuk cover", "'ok, supaya' (66-68.3) dropped"),
    seg("S09b", 70.72, 73.95, "kita punya badan kita yang penat seharian bekerja kan.", "repeated 'kita punya' (69.4-70.7) dropped"),
    seg("S10", 74.40, 76.75, "Boleh dapatkan di beg kuning, harga pun tengah murah ni.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1600}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.14, "threshold_db": -30, "blip": 0.03}, "titles": [],
     "_owner_decisions": "9 Nov: car talking clip VID_20261109_201010 → one video per product; this is the Nature's Key Magnesium part (85-164.5 s). 6 Nov caption set low (top 1600); full-screen realistic photos for each problem the owner lists (owner: 'overlay full cover waktu nak visualkan masalah'); big kinetic key-point text (EDL kp) in the Nature's Key green on the car ceiling; the owner's own close-ups VID_20261014_153135 (label, capsules in the palm); phone mic → tools/voice.sh; night footage lifted slightly.",
     "_note": "Nature's Key Magnesium Capsules #3 — A-roll assets/a.mp4 = VID_20261109_201010 85-164.5 s (rear camera, not mirrored). Halal, 'trusted brand', 'feedback padu' are the owner's own words; no price.",
     "segments": segs,
     "kp": [kp("SUSAH BANGUN PAGI?", ["PAGI?"], ["S02", "start"], ["S02", "ataupun"], "slam"),
            kp("SUSAH NAK REHAT", ["REHAT"], ["S02", "ataupun"], ["S02", "end"], "slide"),
            kp("OTAK PENAT", ["PENAT"], ["S03", "otak"], ["S03", "end"], "zoom"),
            kp("PENING?", ["PENING?"], ["S04", "pening,"], ["S04", "end"], "slam"),
            kp("TAK FOKUS", ["FOKUS"], ["S05", "start"], ["S05", "end"], "split"),
            kp("MAGNESIUM / CAPSULE", ["MAGNESIUM"], ["S06", "magnesium"], ["S06", "end"], "rise"),
            kp("FEEDBACK PADU", ["PADU"], ["S07", "feedback"], ["S07", "end"], "zoom"),
            kp("PENAT SEHARIAN?", ["PENAT"], ["S09b", "penat"], ["S09b", "end"], "slide")],
     "punch": [["S10", "boleh", 1.06]],
     "broll": [cu("C1", ["S06", "magnesium"], ["S06", "end"], N1 + 1.0),
               cu("C2", ["S07", "okay,"], ["S07", "end"], N1 + 14.0),
               cu("C3", ["S08", "start"], ["S08", "end"], N1 + 24.0),
               cu("C4", ["S10", "start"], ["S10", "end"], 75.0, "35% 62%", (1.5, 1.6), "close-up of the bottle in the owner's hand (same moment)")],
     "photos": [ph("pagi", ["S02", "start"], ["S02", "ataupun"], "AI: susah bangun pagi (aurat ditutup)"),
                ph("insomnia", ["S02", "ataupun"], ["S02", "end"], "AI: susah tidur malam (aurat ditutup)"),
                ph("fog", ["S03", "start"], ["S03", "end"], "AI: otak penat (bertudung)"),
                ph("i_lesu", ["S04", "start"], ["S05", "end"], "AI: pening, tak fokus (berlengan panjang)"),
                ph("tired", ["S09", "start"], ["S09b", "end"], "AI: penat bekerja (berlengan panjang)")],
     "theme": {"key": "#8BC34A", "brand": "#FFFFFF"},
     "brand_words": ["nature's", "key"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
