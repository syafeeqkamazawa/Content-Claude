"""EDL for pisau-dessini-1 (VID_20261106_093343), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 60%", push=(1.2, 1.3)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own Dessini footage", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 17.35, 28.40, "Pisau daripada Dessini guys, kalau korang guna ni buat potong bawang, korang sekali hiris dia, tak perasan kalau tiba-tiba dah terpotong dah, dia punya tajam pisau ni.", "HOOK. The repeated 'dia punya tajam pisau ni / bismillah' takes (30-39) dropped"),
    seg("S02", 39.70, 42.45, "Memang sangat tajam je set pisau Dessini ni,", cap_top=220),
    seg("S03", 60.50, 68.60, "yang paling ramai mak-mak tengah cari dekat TikTok Shop ni tau, tak lain tak bukan, set pisau daripada Dessini ni, lapan dalam satu tau.", cap_top=220, note="second, clean take (first take 42.5-51 and false start 57.2 dropped)"),
    seg("S04", 68.70, 74.45, "So kita buka, tengok dulu, jom. Tengok packaging dia cantik kan."),
    seg("S05", 80.95, 84.85, "Dia dah buat macam ni, so lebih selamat lah."),
    seg("S06", 85.75, 92.55, "Dan ni tempat dia, ni tempat letak pisau, cantik kan, oh cantik guys."),
    seg("S07", 95.60, 100.25, "So pisau boleh letak kat dalam ni lah, ok, semua pisau, lapan pisau ada kat dalam ni.", "repeat 'pisau semua gunting semua ada kat dalam ni' (108.7) dropped"),
    seg("S08", 143.40, 150.10, "Yang ni kita panggil holder atau pemegang dia tau, jadi dia ada lima bilah semua.", "earlier stumbling takes of the holder line (117-140) dropped"),
    seg("S09", 155.40, 159.70, "Pisau yang paling besar, pisau potong daging, macam ni."),
    seg("S10", 161.25, 166.55, "Ya Allah memang nampak premium sangat, pisau semua duduk dalam ni eh, jangan risau, cukup lengkap.", "repeated 'memang nampak premium' (171-177) dropped"),
    seg("S11", 181.50, 184.50, "Semua pisau dia ada tulis kat sini,", "repeat 'semua pisau ada tulis kat sini' dropped"),
    seg("S12", 186.25, 191.70, "dapat satu pisau chef, satu pisau slicer, dan yang ni yang sederhana kecil."),
    seg("S13", 194.00, 198.90, "Sesuai lah kalau kita nak buat potong buah kan, dan yang paling kecil ni nak kupas bawang."),
    seg("S14", 200.40, 203.45, "Dapat satu gunting, gunting pun ada."),
    seg("S15", 207.85, 210.35, "Yang menarik dia dekat tengah ada rubber tau,", "stumbles 'yang menarik dia ada, dia ada' and the retakes (213-225, 245-258) dropped"),
    seg("S16", 225.80, 227.95, "jadi dia tak menyakitkan tangan kita lah."),
    seg("S17", 259.45, 268.20, "Dan last sekali dapat satu pengasah, ni, ni pengasah dia dapat juga, so kita nak asah pisau senang je, pakai je pengasah yang ni."),
    seg("S18", 290.95, 294.15, "So, setiap rumah mesti ada satu set pisau daripada Dessini ni tau.", "the long run of 'so' (278-291) dropped"),
    seg("S19", 297.45, 306.25, "InsyaAllah bila korang dapat nanti korang try potong, contohnya korang potong ubi, memang korang potong tu senang sangat sebab pisau ni tajam tau."),
    seg("S20", 313.30, 316.85, "Ya Allah korang, patutlah ramai orang beli set pisau Dessini ni."),
    seg("S21", 319.25, 324.30, "Dah lah cantik atas bawah dengan stylish dia. Jadi tak risau tau hulu dia tercabut ke tak.", "first take 'dah lah cantik atas bawah sama' (316.9) dropped"),
    seg("S22", 402.55, 405.25, "Ibu-ibu akak-akak, yang ni dia tak berkarat tau,", "repeat of the hulu / stylish lines (368-415) dropped"),
    seg("S23", 449.10, 452.35, "sebab pisau ni pisau stainless steel tau."),
    seg("S24", 468.35, 470.20, "Yang ni pula ni boleh berpusing tau."),
    seg("S25", 458.60, 462.85, "Siapa yang nak cari pisau ni, boleh beli daripada Dessini ni, memang recommend sangat-sangat."),
    seg("S26", 537.50, 539.05, "Cantik ni kalau buat raya,"),
    seg("S26b", 543.20, 552.10, "puasa pun dah dekat, nak masak juadah puasa tu sesuai sangat nak guna ni. Lagi-lagi raya lagi lah nak guna kan.", "false starts 'untuk apa, puasa, puasa pun dah' (539-543.2) dropped"),
    seg("S27", 519.40, 536.35, "Ya Allah korang, pergilah order dekat beg kuning tu. Sebab sekarang ni seller pun tengah buat promo tau, banyak promo sekarang sebab apa? Sempena promotion 11.11 pun seller tengah banyak buat dah. Cuba tengok dekat beg kuning, kalau ada voucher claim sekali, kalau nampak harga tengah murah daripada biasa tu, boleh check out terus.", "CTA — the first CTA take (480-500) and 'saya sangat recommend' repeat (510-518) dropped", 1.04),
    seg("S28", 552.95, 554.15, "So dapatkan di beg kuning.", "", 1.06),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Set Pisau Dessini, Drive folder 16e_wkdi… (clip 093343; clip 110642 is pisau-dessini-2). Caption: the 6 Nov default (docs/caption-style-6nov.jpg) placed on the wall above the head (top 300) because the box / holder / knives fill the lower frame; per-segment cap_top where needed. Overlays on every explanation (owner 6 Nov): close-ups of the owner's own box, holder and knives first; realistic AI photos (hands in long sleeves only, or no people) for slicing onion, cutting ubi, a home kitchen and juadah puasa. 9-minute ramble cut to the points; every point kept.",
     "_note": "Pisau Dessini #1 — A-roll assets/a.mp4 = VID_20261106_093343 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Promo 11.11 / vouchers are the owner's own words; no price. 'Tak berkarat' is tied to the box's own 'STAINLESS STEEL' print.",
     "segments": segs,
     "punch": [["S27", "cuba", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S03", "end"], 18.0, "55% 0%", (1.04, 1.1)),
               cu("C2", ["S04", "start"], ["S05", "end"], 70.0, "50% 58%", (1.12, 1.2)),
               cu("C3", ["S07", "start"], ["S07", "end"], 95.6, "70% 66%", (1.3, 1.4)),
               cu("C4", ["S08", "start"], ["S08", "end"], 143.6, "45% 60%", (1.15, 1.25)),
               cu("C5", ["S09", "start"], ["S10", "end"], 432.0, "55% 72%", (1.15, 1.25)),
               cu("C6", ["S11", "start"], ["S13", "end"], 184.0, "82% 0%", (1.3, 1.4)),
               cu("C7", ["S14", "start"], ["S16", "end"], 246.0, "82% 0%", (1.3, 1.4)),
               cu("C8", ["S21", "start"], ["S21", "end"], 383.0, "35% 58%", (1.15, 1.25)),
               cu("C9", ["S22", "start"], ["S23", "end"], 402.5, "30% 58%", (1.15, 1.25)),
               cu("C10", ["S24", "start"], ["S24", "end"], 467.5, "48% 72%", (1.12, 1.2))],
     "photos": [ph("bawang", ["S01", "sekali"], ["S01", "end"], "AI: hiris bawang (tangan berlengan panjang sahaja)"),
                ph("dapur", ["S18", "start"], ["S18", "end"], "AI: dapur rumah"),
                ph("ubi", ["S19", "contohnya"], ["S19", "end"], "AI: potong ubi kayu"),
                ph("juadah", ["S26b", "start"], ["S26b", "end"], "AI: juadah berbuka")],
     "theme": {"key": "#D7263D", "brand": "#E9E9E9"},
     "brand_words": ["dessini"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
