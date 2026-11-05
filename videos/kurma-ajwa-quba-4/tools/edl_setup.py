"""EDL for kurma-ajwa-quba-4 (VID_20261105_173905), 5 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="55% 62%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's hands / dates (same moment)", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 64.40, 70.55, "Korang tahu tak, ada yang tak suka makan kurma tau. Tapi bila makan je kurma Ajwa ni, terus jadi suka pula.", "HOOK (first take 55.9 dropped)"),
    seg("S02", 75.90, 80.30, "Sebab texture kurma dia macam ni tau. Masya-Allah.", "'sebab kurma dia' false start dropped"),
    seg("S03", 80.80, 87.95, "Dia cantik, dia lembut, dan dia tak terlalu basah tau. Dia sedang-sedang je."),
    seg("S04", 118.80, 125.20, "Kurma Ajwa ni, tekstur dia sangat-sangat lembut tau. Kemas, bersih je.", "earlier texture takes 92-105 dropped"),
    seg("S05", 128.80, 132.50, "Okey, yang daripada saya ni satu kg tau."),
    seg("S06", 137.00, 139.60, "Tapi dia comel, dia tak besar sangat, senang nak buat macam-macam."),
    seg("S07", 141.40, 143.90, "Dia macam chewy, lembut dan sedap."),
    seg("S08", 170.70, 175.85, "Pagi, letak kurma yang dah buang biji dalam susu. Insya-Allah sedap tau.", "the TTC line before it (147-167) dropped — TikTok health-claim risk"),
    seg("S09", 176.20, 177.30, "Kurma ni dia tak kering."),
    seg("S10", 181.70, 188.25, "So kalau korang yang tak suka kurma tu, bukannya sebab korang memang tak suka, tapi sebab korang mungkin belum jumpa kurma yang sedap macam ni."),
    seg("S11", 196.30, 202.95, "Bismillah. Sedap, memang sedap.", "eating", keep_pauses=True),
    seg("S12", 205.50, 209.15, "So korang try lah."),
    seg("S13", 340.18, 341.24, "Amalkan kurma Ajwa,", "all of 210-338 dropped — TTC, bersalin, servik, 'kajian' claims (TikTok health-claim risk)"),
    seg("S14", 342.20, 345.25, "bangun tidur je, minum air, kemudian makan kurma."),
    seg("S15", 348.88, 351.30, "So kalau korang nak juga kurma Ajwa ni,"),
    seg("S16", 353.40, 356.50, "Syafiq dah sediakan dekat beg kuning tu. Yang ni satu kg.", "'Syafiq dah letak dekat beg' false start dropped"),
    seg("S17", 362.80, 365.70, "Boleh tengok dekat beg kuning tu, kalau ada pilihan lain boleh pilih."),
    seg("S18", 370.30, 373.30, "Dan juga, sekarang ni ramai seller dah buat promo 11.11 tau.", "'dan juga seller sekarang ni' false start dropped"),
    seg("S19", 378.10, 382.95, "Kalau harga tu lebih murah dan ada voucher, boleh claim sekali. Boleh beli terus di beg kuning.", "CTA (first take 373.7 dropped)", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3",
     "word3": {"max": 3, "chars": 18, "highlight": True, "on": "#3DD6F5", "top": 1690, "size": 58}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "5 Nov: 'Ada video baru kurma Ajwa. Jangan guna bahagian yang mungkin kena violation TikTok, pastikan ada overlay untuk setiap penerangan yang perlukan overlay'. Dropped as TikTok risk (unverified health / medical claims): every line about easy childbirth ('senang bersalin, tak jahit, tak koyak'), TTC, softening the cervix and 'banyak kajian mengatakan' (0-46, 147-167, 210-338). Kept: taste, texture, size, 1 kg pack, serving ideas (in milk, after waking with water), promo 11.11. Overlays on every explanation: close-ups of the owner's own hands and dates for texture, size and the 1 kg pack; realistic AI photos for the serving ideas (no people). Captions as Kurma Ajwa #1-#3.",
     "_note": "Kurma Ajwa #4 — A-roll assets/a.mp4 = VID_20261105_173905 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted; close-ups play the same moment zoomed into the hands. Promo 11.11 and vouchers are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S19", "beli", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S02", "end"], 75.90), cu("C2", ["S03", "start"], ["S03", "end"], 80.80),
               cu("C3", ["S04", "start"], ["S04", "end"], 118.80), cu("C4", ["S05", "start"], ["S05", "end"], 128.80, "50% 66%", (1.3, 1.45)),
               cu("C5", ["S06", "start"], ["S07", "end"], 137.00), cu("C6", ["S16", "syafiq"], ["S16", "end"], 353.40, "50% 66%", (1.3, 1.45))],
     "photos": [ph("susu", ["S08", "start"], ["S09", "end"], "AI: kurma dalam susu"),
                ph("pagi", ["S13", "start"], ["S14", "end"], "AI: air dan kurma waktu pagi")],
     "theme": {"key": "#3DD6F5", "brand": "#E9C46A"},
     "brand_words": ["ajwa"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
