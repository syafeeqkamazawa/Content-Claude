"""EDL for periuk-giselle-2 (VID_20261106_091130), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 68%", push=(1.3, 1.45)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own rice cooker footage", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 97.15, 102.45, "Boleh buat dua dalam satu. Nasi masak, lauk pun jadi panas.", "HOOK (moved up from the cooking result)"),
    seg("S02", 76.45, 81.25, "Periuk nasi daripada Giselle ni memang sangat comel tau. Serius tak tipu korang.", "opening 'beli periuk nasi yang macam Khairul Aming beli tu' (4.8-9.3) dropped — a celebrity name the owner chose not to use in clip 090321 ('actually tak payah'); aside 'saya tak payah' (73.9) dropped"),
    seg("S03", 81.60, 85.70, "Korang tengoklah sendiri. Memang lawa lah. Memang comel. Macam cute-cute je macam tu."),
    seg("S04", 14.05, 17.95, "So kalau korang nak pergi piknik kan, sangat sesuai.", "filler 'nah, ok' (11.7-12.8) dropped"),
    seg("S05", 20.20, 23.75, "Alang-alang saya nak share juga, apa kita boleh masak.", "repeated 'saya pun nak share juga / jom saya share / ok kita cuba masak nasi' (25-34.4) dropped"),
    seg("S06", 35.10, 37.05, "Kita masak nasi guna periuk Giselle."),
    seg("S07", 37.95, 46.25, "Masukkan dalam periuk ni dua pot. Lepas tu, contohnya ada lauk sotong, boleh panaskan dalam ni."),
    seg("S08", 49.20, 54.75, "Lauk sotong tu letak kat sini, letak kat atas tu.", "filler 'ni kan ada kan' dropped"),
    seg("S09", 55.20, 62.95, "Beras boleh letak kat bawah, tu boleh masak nasi bersama dengan panaskan sotong sekali, macam tu."),
    seg("S10", 70.00, 72.55, "Lepas tu kita tengoklah macam mana rupa dia ni."),
    seg("S11", 90.05, 96.95, "Bila dah siap masak, korang tengok, nasi dah siap masak. Sedap. Lauk pun boleh siap panas sekali."),
    seg("S12", 102.90, 104.75, "Memang sedap lah nak makan kan?"),
    seg("S13", 150.00, 153.75, "Mana tahu bila korang makan tu, rasa macam ala-ala makan dekat Rembayung.", "best of the seven takes (108-162)"),
    seg("S14", 169.05, 184.55, "So guys, seller sekarang ni tengah buat promo banyak tau, 11.11 punya promotion. Cuba tengok dekat beg kuning, kalau ada voucher boleh claim. Kalau harga tu tengah murah daripada biasa, korang boleh beli tu dekat beg kuning, ok?", "CTA — false start 'so guys seller tengah buat promo' (163.8-166.5) dropped", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Periuk nasi Giselle, Drive folder 1UWCUgtn… (two talking clips → two videos; this is clip 091130). Caption: the 6 Nov default (docs/caption-style-6nov.jpg), moved up to the wall (top 300) so it never covers the pot or its logo. Overlays on every explanation (owner 6 Nov): close-ups of the owner's own rice-cooker demo first, realistic AI photos (no people) for picnic, rice with sambal sotong and a kampung-style meal. The Khairul Aming line is left out (owner dropped it himself in clip 090321).",
     "_note": "Periuk Giselle #2 — A-roll assets/a.mp4 = VID_20261106_091130 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Clip 090321 is periuk-giselle-1. Promo 11.11 / vouchers are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S14", "cuba", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S03", "end"], 76.45, "35% 70%"),
               cu("C2", ["S05", "start"], ["S06", "end"], 31.5, "30% 62%"),
               cu("C3", ["S07", "start"], ["S07", "end"], 37.95, "40% 62%"),
               cu("C4", ["S08", "start"], ["S09", "end"], 49.2, "45% 58%", (1.2, 1.3)),
               cu("C5", ["S10", "start"], ["S10", "end"], 70.0, "45% 65%")],
     "photos": [ph("piknik", ["S04", "start"], ["S04", "end"], "AI: piknik keluarga (tiada orang)"),
                ph("sotong", ["S11", "start"], ["S12", "end"], "AI: nasi panas + sambal sotong"),
                ph("kampung", ["S13", "start"], ["S13", "end"], "AI: hidangan kampung (generic, bukan restoran sebenar)")],
     "theme": {"key": "#7FB8A4", "brand": "#E9DCC4"},
     "brand_words": ["giselle"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
