"""EDL for aurapep-krill-oil-12 (Drive file 'Yang ini boleh refer video Ali untuk rujukan overlay.mp4'), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
BR = 558.12  # b.mp4 = A-roll flipped (0-558.12) + the owner's B-roll VID_20261106_173831 (558.12-594)


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="55% 72%", push=(1.3, 1.45), note="close-up of the owner's own Aurapep bottle / softgels"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def lb(text, f, t): return {"text": text, "from": f, "to": t, "top": 170}


segs = [
    seg("S01", 22.90, 29.10, "Kalau nak tengok beza krill oil original dengan krill oil palsu, boleh tengok yang ni dengan yang ni.", "HOOK — two earlier takes (9.5-21) dropped"),
    seg("S02", 39.10, 43.95, "Yang cawan krill oil tu dah larut bersama dengan seluruh air tu, itu yang original.", "stumbles 'yang cawan penuh dengan / yang cawan dah apa' dropped"),
    seg("S03", 53.40, 61.00, "Yang satu lagi cawan yang krill oil dia hanya terapung di permukaan sahaja, tak larut bersama air, itu adalah yang palsu.", "false starts (44.5-53.4) dropped"),
    seg("S04", 67.70, 72.80, "Kalau yang original, krill oil akan bawa sekali semua minyak tu ke dalam air."),
    seg("S05", 101.50, 112.32, "Tapi kalau minyak krill oil yang terapung di permukaan tu, maksudnya dia punya penyerapan tak berapa baik, sebab dia tak boleh serap minyak.", "stumbling takes (72.8-101.5) and 'tak boleh bersihkan kita punya darah' (112.3-121) dropped — cure-like claim; the second cup explanation (200-268) dropped as a repeat"),
    seg("S06", 137.45, 144.95, "Aurapep Krill Oil ni kita perlu tahulah baik untuk apa? Untuk otak dan mata. Sebab apa? Sebab dalam ni ada DHA.", "fillers (121-137) dropped"),
    seg("S07", 161.45, 172.75, "Krill oil baik untuk darah, jantung, saraf, sendi, lutut, sebab ada EPA tau. Dan dia jenis omega-3.", "first take (145.5-156.3) dropped"),
    seg("S08", 294.55, 303.70, "Lagi satu, krill oil ni kenapa dia warna merah? Sebab dia ada astaxanthin dekat dalam ni tau. Astaxanthin ni memang banyaklah kelebihan dia.", "earlier takes (280-293) and the unclear 304-323 dropped"),
    seg("S09", 324.60, 330.55, "Dan juga brand Aurapep ni punya krill oil ada vitamin D3 dan K2 sekali."),
    seg("S10", 343.10, 349.25, "So D3 dengan K2 ni baik untuk apa? Untuk kita punya immune system, baik untuk tulang sendi.", "'baik untuk pipe darah' (349.7) dropped"),
    seg("S11", 374.95, 380.75, "So saya amat cadangkan boleh ambil krill oil daripada Aurapep ni.", "false starts (362-375) dropped"),
    seg("S12", 394.75, 398.55, "Kandungan dia tinggi tau, 1000 mg setiap 2 biji tu."),
    seg("S13", 412.00, 420.35, "Satu botol pula ada 40 biji, sehari makan 2 biji cukup, boleh makan selama 20 hari, tapi harga dia tu lebih bajet sikit."),
    seg("S14", 434.30, 441.05, "Tapi yang paling penting, Aurapep ni ada KKM, halal."),
    seg("S15", 450.50, 457.40, "Tapi sekarang guys, sekarang ni seller tengah banyak buat promo tau, lagi-lagi sekarang ni promotion 11.11."),
    seg("S16", 467.36, 472.90, "So kalau boleh, tengok dekat beg kuning, jangan ambil satu botol, ambillah 2-3 botol.", "retakes (457.6-467.3) dropped"),
    seg("S17", 482.38, 487.10, "Satu botol baru tahan 20 hari, ambil 3 botol atau 6 botol tu simpan dekat rumah.", "'warga emas boleh makan 4 biji' (488-492.7) dropped — dose beyond the label"),
    seg("S18", 500.55, 504.00, "Yang ada ibu ayah, boleh belikan untuk ibu ayah.", "first take (497-500.6) dropped"),
    seg("S19", 511.65, 514.95, "Aurapep Krill Oil ni bukan sahaja orang muda tau perlu amalkan,", "first take (506-510) dropped"),
    seg("S20", 518.15, 521.85, "orang berusia pun lagilah patut amalkan."),
    seg("S21", 547.20, 555.15, "So guys, seller tengah buat promo 11.11 ni, bila-bila masa je boleh habis. Sebelum promo habis, boleh grab awal, check out dekat beg kuning.", "CTA — earlier takes (530-547) dropped", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 400}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Aurapep Krill Oil, Drive folder 1irOVOgs… — the owner's talking clip 'Yang ini boleh refer video Ali untuk rujukan overlay' (558 s), overlays following 'Guna overlay sama dengan video Ali ni' (another creator's video, reference only — none of its footage or its product infographic is used): a two-line white condensed title with a black outline at the top for the hook, and one-word ingredient labels top-centre when named (DHA, EPA, Omega-3, Astaxanthin, D3 + K2, 1000 mg, KKM • Halal). Caption: the 6 Nov default, set at top 400 below the labels (the bottle sits low in the frame). The cup comparison the owner describes is shown as a realistic AI photo. 'Bersihkan darah', 'pipe darah' and 'warga emas makan 4 biji' left out (owner 5 Nov: no TikTok-risk lines).",
     "_note": "Aurapep Krill Oil #12 — A-roll assets/a.mp4 = the talking clip (front camera, mirrored back in CSS). assets/b.mp4 = A-roll flipped and muted (0-558.12) + the owner's B-roll VID_20261106_173831 (taking a softgel, drinking, thumbs up; 558.12-594). Old clips 091344/091830/092840 already used in #1-#11 — not reused. Promo 11.11 / 'lebih bajet' are the owner's own words; no price.",
     "segments": segs,
     "toptitle": {"lines": ["Beza Krill Oil Original Vs Palsu", "(Cara nak tengok)"], "to": ["S01", "end"], "top": 150},
     "labels": [lb("DHA", ["S06", "DHA."], ["S06", "end"]), lb("EPA", ["S07", "EPA"], ["S07", "Dan"]), lb("Omega-3", ["S07", "Dan"], ["S07", "end"]),
                lb("Astaxanthin", ["S08", "astaxanthin"], ["S08", "end"]), lb("D3 + K2", ["S09", "D3"], ["S10", "end"]),
                lb("1000 mg", ["S12", "1000"], ["S12", "end"]), lb("KKM • Halal", ["S14", "KKM,"], ["S14", "end"])],
     "punch": [["S21", "sebelum", 1.06]],
     "broll": [cu("C1", ["S06", "start"], ["S06", "end"], 140.0),
               cu("C2", ["S08", "start"], ["S08", "end"], 296.0, "50% 72%"),
               cu("C3", ["S12", "start"], ["S12", "end"], 395.0),
               cu("C4", ["S13", "start"], ["S13", "end"], BR + 4.0, "50% 45%", (1.05, 1.12), "the owner's own B-roll: taking a softgel and drinking water"),
               cu("C5", ["S17", "start"], ["S17", "end"], BR + 22.0, "50% 45%", (1.05, 1.12), "the owner's own B-roll: thumbs up after the softgel"),
               cu("C6", ["S19", "start"], ["S20", "end"], 512.0)],
     "photos": [ph("cawan", ["S02", "start"], ["S05", "end"], "AI: ujian cawan — larut vs terapung (illustrasi, tiada orang)")],
     "theme": {"key": "#E0342C", "brand": "#2C4A8C"},
     "brand_words": ["aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
