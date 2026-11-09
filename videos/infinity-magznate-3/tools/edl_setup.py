"""EDL for infinity-magznate-3 (VID_20261109_201010 224-289 s), 9 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="45% 45%", push=(1.25, 1.35), note="close-up of the Magznate bottle the owner holds up to the camera (same moment)"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=210, size=118): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


segs = [
    seg("S01", 19.10, 23.62, "Kalau badan dah rasa lesu ataupun tak boleh nak fokus,", "HOOK — false start 'kalau badan tengah' (17.7-19.1) dropped"),
    seg("S02", 24.90, 32.86, "tiba-tiba rasa pening ke, ataupun contohnya nak bangun tidur pun susah, nak tidur pun lambat, nak rehat tu kan macam tak boleh nak rehat,"),
    seg("S03", 33.38, 34.86, "boleh dapatkan Magnesium."),
    seg("S04", 35.60, 39.18, "Yang ni daripada Infinity Magnesium.", "'ok' (35-35.5) and the repeat 'Magnesium daripada Infinity, ok' (39.2-41.6) dropped"),
    seg("S05", 41.60, 44.10, "Brand ni yang sangat-sangat trusted lah,"),
    seg("S06", 45.94, 50.60, "ada KKM, ada hologram sekali dan ada halal JAKIM.", "first 'ada KKM, jangan risau' (44.1-45.9) dropped — said twice"),
    seg("S07", 50.60, 52.16, "So trusted, jangan risau, insya-Allah."),
    seg("S08", 52.78, 54.40, "Satu botol ni ada 60 tablet.", "filler 'ok' (52.2-52.7) dropped"),
    seg("S08b", 55.04, 57.58, "Sehari boleh ambil 1 ke 2 tablet lah.", "filler 'ok' (54.4-55) dropped"),
    seg("S09", 58.00, 60.26, "Dapatkan di beg kuning insya-Allah, harga tengah murah ni,"),
    seg("S09b", 61.00, 62.98, "seller banyak tengah buat promotion,", "first 'seller banyak tengah' (60.3-61) dropped — said twice"),
    seg("S10", 63.14, 64.25, "dapatkan di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1600}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.14, "threshold_db": -30, "blip": 0.03}, "titles": [],
     "_owner_decisions": "9 Nov: car talking clip VID_20261109_201010 → one video per product; this is the Infinity Magnesium (Magznate) part (224-289 s). 6 Nov caption set low (top 1600); full-screen realistic photos for each problem (lesu, tak fokus, pening, susah bangun, lambat tidur, tak boleh rehat); big kinetic key-point text (EDL kp) in the Magznate aqua on the car ceiling; no separate B-roll of this product in the Drive folder any more, so close-ups come from the moments the owner holds the bottle up to the camera; phone mic → tools/voice.sh.",
     "_note": "Infinity Magznate #3 — A-roll assets/a.mp4 = VID_20261109_201010 224-289 s (rear camera, not mirrored). assets/b.mp4 = the same clip, muted. KKM, hologram, halal JAKIM, 60 tablets, 1-2 a day and promo are the owner's own words; no price.",
     "segments": segs,
     "kp": [kp("LESU?", ["LESU?"], ["S01", "lesu"], ["S01", "ataupun"], "slam", 210, 150),
            kp("TAK BOLEH FOKUS", ["FOKUS"], ["S01", "ataupun"], ["S01", "end"], "split"),
            kp("PENING?", ["PENING?"], ["S02", "pening"], ["S02", "ataupun"], "slam", 210, 140),
            kp("SUSAH BANGUN", ["BANGUN"], ["S02", "ataupun"], ["S02", "nak#2"], "slide"),
            kp("LAMBAT TIDUR", ["TIDUR"], ["S02", "nak#2"], ["S02", "nak#3"], "slide"),
            kp("TAK BOLEH REHAT", ["REHAT"], ["S02", "nak#3"], ["S02", "end"], "zoom"),
            kp("INFINITY / MAGNESIUM", ["MAGNESIUM"], ["S04", "infinity"], ["S04", "end"], "rise"),
            kp("KKM • HOLOGRAM / HALAL JAKIM", ["KKM", "HALAL"], ["S06", "start"], ["S06", "end"], "rise", 180, 104),
            kp("60 TABLET", ["60"], ["S08", "60"], ["S08", "end"], "zoom", 210, 140),
            kp("1-2 SEHARI", ["1-2"], ["S08b", "start"], ["S08b", "end"], "slam", 210, 130)],
     "punch": [["S10", "dapatkan", 1.06]],
     "broll": [cu("C1", ["S04", "start"], ["S04", "end"], 36.0),
               cu("C2", ["S06", "start"], ["S06", "end"], 46.5, "62% 42%", (1.35, 1.45)),
               cu("C3", ["S08", "start"], ["S08b", "end"], 53.0, "55% 40%", (1.35, 1.45))],
     "photos": [ph("i_lesu", ["S01", "start"], ["S01", "ataupun"], "AI: lesu (berlengan panjang)"),
                ph("fog", ["S01", "ataupun"], ["S01", "end"], "AI: tak fokus (bertudung)"),
                ph("penat", ["S02", "start"], ["S02", "ataupun"], "AI: pening (berlengan panjang)"),
                ph("pagi", ["S02", "ataupun"], ["S02", "nak#2"], "AI: susah bangun (aurat ditutup)"),
                ph("insomnia", ["S02", "nak#2"], ["S02", "nak#3"], "AI: lambat tidur (aurat ditutup)"),
                ph("anxious", ["S02", "nak#3"], ["S02", "end"], "AI: tak boleh rehat (bertudung)"),
                ph("belanja", ["S09", "harga"], ["S09b", "end"], "AI: membeli online (bertudung)")],
     "theme": {"key": "#5FC7D4", "brand": "#A8E2EA"},
     "brand_words": ["infinity"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
