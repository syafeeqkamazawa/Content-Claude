"""EDL for aurapep-shilajit-10 (VID_20261109_195852), 9 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
S1 = 50.7667          # b.mp4 = A-roll copy (0-50.77) + VID_20261019_090353 (box on the grass) + VID_20261019_090625 (box, bottle, tablets on the grass)
S2 = S1 + 22.3277


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 50%", push=(1.02, 1.1), note="the owner's own close-up of Aurapep Shilajit on the grass at home"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=210, size=118): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


segs = [
    seg("S01", 15.15, 16.62, "Abang-abang yang", "HOOK — false starts 'yang pada, yang ada pada' (9.5-12.2) dropped; 'tak cukup tenaga, mungkin' (16.6-19.8) dropped — TikTok risk"),
    seg("S01b", 19.78, 22.16, "rasa selalu lemau badan,", zoom=1.0),
    seg("S02", 22.16, 25.22, "boleh try dengan Shilajit daripada Aurapep ni.", "the repeat 'Shilajit daripada Aurapep ni' and 'insya-Allah bantu boost kita punya extra energy, supaya badan lebih bertenaga, lebih fokus' (25.2-37.3) dropped — energy / stamina claims are TikTok risk (owner 5 Nov; as Shilajit #8, #9)"),
    seg("S03", 38.75, 44.75, "So dekat beg kuning ni memang seller tengah buat promosi ni, sementara harga tengah murah, boleh check out di beg kuning.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1600}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.14, "threshold_db": -30, "blip": 0.03}, "titles": [],
     "_owner_decisions": "9 Nov: car talking clip VID_20261109_195852 (Aurapep Shilajit). 6 Nov caption set low (top 1600); full-screen realistic photo for 'lemau badan'; big kinetic key-point text (EDL kp) in the Aurapep gold on the car ceiling; the owner's own close-ups on the grass at home (VID_20261019_090353 / 090625 — 'produk close up dekat rumput rumah saya'); phone mic → tools/voice.sh. Most of the clip is an energy / stamina pitch, dropped as TikTok risk — the video is short.",
     "_note": "Aurapep Shilajit #10 — A-roll assets/a.mp4 = VID_20261109_195852 (rear camera, not mirrored). Promo is the owner's own words; no price.",
     "segments": segs,
     "kp": [kp("LEMAU BADAN?", ["LEMAU"], ["S01b", "start"], ["S01b", "end"], "slam"),
            kp("SHILAJIT / AURAPEP", ["SHILAJIT"], ["S02", "shilajit"], ["S02", "end"], "zoom", 190, 120),
            kp("PROMO SEKARANG", ["PROMO"], ["S03", "promosi"], ["S03", "boleh"], "split"),
            kp("CHECK OUT!", ["CHECK"], ["S03", "boleh"], ["S03", "end"], "slam")],
     "punch": [["S03", "boleh", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S02", "end"], S1 + 2.0),
               cu("C2", ["S03", "start"], ["S03", "sementara"], S2 + 44.0),
               cu("C3", ["S03", "sementara"], ["S03", "boleh"], S2 + 79.0, note="the owner's own close-up: tablets in the bottle")],
     "photos": [ph("tired", ["S01", "start"], ["S01b", "end"], "AI: lemau badan (berlengan panjang)")],
     "theme": {"key": "#C9A227", "brand": "#E9E9E9"},
     "brand_words": ["aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
