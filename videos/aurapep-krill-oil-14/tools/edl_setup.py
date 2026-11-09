"""EDL for aurapep-krill-oil-14 (VID_20261109_201010 163-225 s), 9 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
K1 = 62.0333          # b.mp4 = A-roll copy (0-62.03) + VID_20261106_173831 (the owner taking a softgel, drinking)


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="35% 52%", push=(1.5, 1.6), note="close-up of the Aurapep bottle in the owner's hand (same moment)"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=210, size=118): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


segs = [
    seg("S01", 6.85, 10.05, "Tahu tak korang, sebenarnya fish oil ni ada", "HOOK"),
    seg("S01b", 12.70, 17.62, "yang lebih, orang kata kesan tu extra daripada fish oil, iaitu krill oil.", "pause/stutter 'ada' (10-12.7) dropped", zoom=1.0),
    seg("S02", 17.62, 19.85, "Krill oil ni dia dah ada omega-3.", "'dan juga Aurapep ni' (19.9-21.4) dropped"),
    seg("S03", 21.60, 25.65, "Brand Aurapep krill oil ni dia ada DHA, EPA."),
    seg("S04", 26.05, 33.96, "Dua-dua ni fungsi dia untuk jaga kita punya mata, otak, kita punya sendi, saraf,", "'saluran darah' (34-35.3) dropped — TikTok risk (as Krill #12)"),
    seg("S04b", 50.75, 51.95, "kita punya jantung.", "moved up from the repeated list (37-53, said twice) — only 'jantung' was new"),
    seg("S04c", 35.28, 36.90, "Memang komplit lah ni."),
    seg("S05", 53.15, 61.45, "Insya-Allah, boleh beli di beg kuning, harga pun tengah ada promotion, seller tengah buat promosi, dapatkan di beg kuning sementara harga tengah murah.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1600}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.14, "threshold_db": -30, "blip": 0.03}, "titles": [],
     "_owner_decisions": "9 Nov: car talking clip VID_20261109_201010 → one video per product; this is the Aurapep Krill Oil part (163-225 s). 6 Nov caption set low (top 1600); full-screen realistic photos (fish oil vs krill, x-ray eyes / joints / nerves / heart); big kinetic key-point text (EDL kp) in the Aurapep red on the car ceiling; the owner's own B-roll VID_20261106_173831 (taking a softgel); phone mic → tools/voice.sh.",
     "_note": "Aurapep Krill Oil #14 — A-roll assets/a.mp4 = VID_20261109_201010 163-225 s (rear camera, not mirrored). Omega-3, DHA, EPA, promo are the owner's own words; no price.",
     "segments": segs,
     "kp": [kp("LEBIH PADU / DARIPADA FISH OIL", ["PADU"], ["S01b", "start"], ["S01b", "iaitu"], "slide", 190, 104),
            kp("KRILL OIL", ["KRILL"], ["S01b", "iaitu"], ["S02", "end"], "zoom", 210, 150),
            kp("DHA • EPA", ["DHA", "EPA"], ["S03", "DHA,"], ["S03", "end"], "slam", 210, 140),
            kp("MATA • OTAK / SENDI • SARAF", ["MATA", "OTAK", "SENDI", "SARAF"], ["S04", "mata,"], ["S04", "end"], "rise", 170, 108),
            kp("JANTUNG", ["JANTUNG"], ["S04b", "start"], ["S04b", "end"], "zoom"),
            kp("KOMPLIT!", ["KOMPLIT!"], ["S04c", "start"], ["S04c", "end"], "slam", 210, 150),
            kp("PROMO SEKARANG", ["PROMO"], ["S05", "promotion,"], ["S05", "dapatkan"], "split")],
     "punch": [["S05", "dapatkan", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S02", "end"], K1 + 4.5, "50% 45%", (1.05, 1.12), "the owner's own B-roll: showing a krill softgel"),
               cu("C2", ["S03", "start"], ["S03", "end"], 22.0),
               cu("C3", ["S04c", "start"], ["S04c", "end"], K1 + 14.0, "50% 45%", (1.05, 1.12), "the owner's own B-roll: taking the softgel with water")],
     "photos": [ph("fishoil", ["S01", "fish"], ["S01b", "iaitu"], "AI: minyak ikan"),
                ph("krill", ["S01b", "iaitu"], ["S01b", "end"], "AI: kawanan krill (tiada orang)"),
                ph("x_mata", ["S04", "mata,"], ["S04", "sendi,"], "AI: x-ray mata & otak"),
                ph("x_lutut", ["S04", "sendi,"], ["S04", "saraf,"], "AI: x-ray sendi lutut"),
                ph("x_saraf", ["S04", "saraf,"], ["S04", "end"], "AI: x-ray saraf"),
                ph("x_jantung", ["S04b", "start"], ["S04b", "end"], "AI: x-ray jantung"),
                ph("belanja", ["S05", "harga"], ["S05", "dapatkan"], "AI: membeli online (bertudung)")],
     "theme": {"key": "#E0342C", "brand": "#2C4A8C"},
     "brand_words": ["aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
