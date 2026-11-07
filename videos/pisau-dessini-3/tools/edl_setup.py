"""EDL for pisau-dessini-3 (VID_20261107_094425), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]
Z = 1.75  # filmed wide across the kitchen: every segment is zoomed toward the counter (EDL zoom_origin)


def seg(i, x, y, t, note="", zoom=Z, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 70%", push=(2.5, 2.7)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own Dessini set on the counter", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 18.75, 40.30, "Set pisau Dessini, harga dia masya-Allah murah sangat. Sekarang ni promotion 11.11, seller buat promotion harga kau-kau. Cuba tengok dekat beg kuning berapa harga dia, mesti terkejut. Okay, sementara harga murah, baik ibu-ibu, akak-akak, beli terus.", "HOOK — greeting and the unclear 'saya nak …' (10-17.7) dropped"),
    seg("S02", 42.50, 49.45, "Kita ada satu, dua, tiga, empat, lima. Lima pisau, satu pengasah, satu gunting.", "the recounting (50-63.7) dropped"),
    seg("S03", 63.75, 66.35, "Lapan tu termasuk holder."),
    seg("S04", 73.50, 77.05, "Jom kita buka dulu, bismillah.", "doubled 'jom' dropped"),
    seg("S05", 94.00, 98.50, "Masya-Allah, tengok eh, boleh pusing.", "repeated 'boleh pusing' dropped"),
    seg("S06", 100.45, 108.95, "Kalau kita pegang ni kan, tapak dia boleh pusing."),
    seg("S07", 110.35, 114.95, "Lepas tu kita pasang pisau dulu, pisau yang kecil sekali.", "unclear 'pisau apa ni, ketik pisau dia' (115.9-122.5) dropped"),
    seg("S08", 125.90, 132.20, "Okay next, pengasah. Ini pengasah pisau tau.", "unclear tail (133.5-140.7) dropped"),
    seg("S09", 144.00, 145.62, "Yang seterusnya,"),
    seg("S10", 148.20, 149.22, "pisau pemotong daging.", "stumble 'abad, abad sayang' dropped"),
    seg("S11", 150.85, 153.40, "Semua pisau ni, hulu dia tak ada,"),
    seg("S12", 159.45, 163.52, "dia hulu ke hujung ni dia bercantum, dia stainless steel,", "hesitation 'apa tu orang kata, tak, tak separuh-separuh' dropped"),
    seg("S13", 165.60, 170.50, "so memang tak risau lah hulu tercabut, insya-Allah.", "repeated 'orang kata tak' dropped"),
    seg("S14", 179.55, 184.35, "Pisau memotong ikan pun boleh kot, ayam juga kan."),
    seg("S15", 189.95, 200.80, "Gunting dia kat tengah ni ada getah tau, korang tak rasa sakit bila korang nak potong apa-apa berkaitan dengan masakan ni. Korang nak potong tak sakit sebab ada getah kat tengah ni.", "first 'gunting' and the search for the scissors' slot (202-217) dropped"),
    seg("S16", 220.25, 227.70, "Seterusnya, pisau yang macam nak potong ikan kot, potong ikan tu, potong sayur boleh juga ni, dia panjang sikit tu."),
    seg("S17", 237.90, 244.26, "Yang terakhir, pisau sederhana lah, potong sayur boleh, potong bawang kan."),
    seg("S18", 249.45, 251.10, "So complete."),
    seg("S19", 262.40, 264.90, "Baru lah nampak style."),
    seg("S20", 274.00, 283.55, "So nampak tak ibu-ibu akak-akak, kalau lawa macam ni pun kau tak beli lagi tak tahulah, dengan harga yang sangat mampu milik."),
    seg("S21", 284.62, 285.84, "Harga tu masih", "'teman-teman' dropped"),
    seg("S22", 287.14, 304.50, "dalam tempoh promosi, harga yang sangat murah. Ibu-ibu kakak-kakak beli terus, ataupun abang-abang ayah-ayah belikan lah untuk ibu-ibu, belikan untuk pasangan, insya-Allah memang sangat gembira dia orang. So boleh check out di beg kuning sekarang.", "CTA", 1.82),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": False,
     "zoom_origin": "50% 62%",
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Set Pisau Dessini' — new clip VID_20261107_094425 in Drive folder 16e_wkdi… → #3 (093343 = #1, 110642 = #2). Filmed wide across the kitchen, so the A-roll is zoomed ×1.75 toward the counter (zoom_origin 50% 62%). Caption: the 6 Nov default on the wall above the head (top 300) — the set sits on the counter low in the frame. Overlays on every explanation (owner 6 Nov): tight close-ups of the owner's own set first; realistic AI photos (hands in long sleeves only, or no people) for cutting fish / chicken, the scissors and a gift.",
     "_note": "Pisau Dessini #3 — A-roll assets/a.mp4 = VID_20261107_094425 (rear camera, not mirrored). assets/b.mp4 = the same clip, muted. Price talk and promo 11.11 are the owner's own words; no price shown.",
     "segments": segs,
     "punch": [],
     "broll": [cu("C1", ["S05", "start"], ["S06", "end"], 96.0, "50% 70%", (2.3, 2.5)),
               cu("C2", ["S07", "start"], ["S08", "end"], 112.0, "50% 70%"),
               cu("C3", ["S10", "start"], ["S13", "end"], 150.0, "50% 68%", (2.3, 2.5)),
               cu("C4", ["S16", "start"], ["S17", "end"], 222.0, "50% 68%"),
               cu("C5", ["S18", "start"], ["S19", "end"], 262.4, "50% 68%", (2.2, 2.4))],
     "photos": [ph("ikan", ["S14", "start"], ["S14", "end"], "AI: potong ikan & ayam (tangan berlengan panjang)"),
                ph("gunting", ["S15", "korang"], ["S15", "end"], "AI: gunting dapur (tangan berlengan panjang)"),
                ph("hadiah", ["S22", "ataupun"], ["S22", "insya-Allah"], "AI: hadiah (tiada orang)")],
     "theme": {"key": "#D7263D", "brand": "#E9E9E9"},
     "brand_words": ["dessini"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
