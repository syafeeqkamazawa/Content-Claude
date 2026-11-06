"""EDL for vteay-fish-oil-1 (VID_20261106_084402), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="60% 45%", push=(1.6, 1.75)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the bottle in the owner's hand (same moment)", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 2.20, 6.35, "Jangan kita beli Omega-3 Fish Oil sebelum kita cek 3 benda ni.", "HOOK"),
    seg("S02", 16.60, 21.10, "Jangan kita hanya tengok pada label, packaging, harga, terus kita nak beli.", "takes 7.1-13.6 dropped"),
    seg("S03", 29.60, 33.65, "3 benda yang saya maksudkan ialah: pertama, kena cek kandungan EPA dia.", "first take 21.5 dropped"),
    seg("S04", 34.40, 36.50, "Kedua, kena cek kandungan DHA dia."),
    seg("S05", 36.90, 40.40, "Dan ketiga, kena tengok ada tak kelulusan daripada KKM."),
    seg("S06", 61.80, 75.15, "Saya nak syorkan kepada ibu ayah, abang kakak, pak cik mak cik semua, Omega-3 Fish Oil daripada VTEAY yang menjadi pilihan ramai sekarang ni tau. Sebab apa?", "takes 47-59 dropped"),
    seg("S07", 75.40, 79.10, "Ada kelulusan daripada KKM dan sangat berkualiti."),
    seg("S08", 79.10, 85.90, "Cuba tengok, packaging dia pun sangat kemas. Baru sampai dekat saya ni."),
    seg("S09", 86.40, 92.40, "Macam ni punya packaging, barulah kita rasa selamat nak makan."),
    seg("S10", 154.50, 163.60, "Dalam satu botol ni ada 2,500 mg fish oil, 483 EPA dan 644 DHA tau.", "many stumbling takes 92-154 dropped"),
    seg("S11", 180.40, 189.25, "Kita nak memilih Omega-3 Fish Oil ni, biarlah yang berkualiti, kena tengok kandungan EPA dan DHA yang tinggi macam ni.", "repeat 163-180 dropped"),
    seg("S12", 194.80, 201.50, "Sebab EPA dan DHA yang tinggi bantu support kesihatan jantung kita, dapat bantu juga support kesihatan saraf kita.", "the 'lenguh, kebas-kebas … insya-Allah dapat bantu' line (201-208) dropped — TikTok health-claim risk"),
    seg("S13", 209.00, 213.35, "Juga dapat bantu support kesihatan otak kita, supaya lebih fokus dan daya ingatan yang lebih baik."),
    seg("S14", 221.40, 228.10, "Omega-3 Fish Oil VTEAY ni sekarang ni ada banyak promosi tau dekat beg kuning. Promo 11.11 pun ramai seller dah tengah buat sekarang."),
    seg("S15", 228.50, 230.30, "Harga sangat-sangat murah."),
    seg("S16", 230.70, 235.10, "Satu botol ni ada 60 softgel, satu hari cukup kita ambil 2 softgel sahaja."),
    seg("S17", 241.00, 247.05, "Kepada kawan-kawan, ibu ayah, abang kakak, pak cik mak cik yang berminat, boleh dapatkan segera dekat beg kuning, sementara masih ada stok.", "CTA (first take 235-240 dropped)", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1380}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Drive folder 1-HP8DmM… 'VTEAY Fish Oil'. Caption: the 6 Nov default (docs/caption-style-6nov.jpg, owner: 'Lepas ni always pakai caption style macam dalam gambar'). Overlays: 'Semua video ada overlay yang sesuai supaya viewer senang faham dan lebih mudah nak tengok video sampai habis' — close-ups of the bottle in the owner's hand whenever he shows it, a white checklist card for the 3 things to check (EPA, DHA, KKM), realistic AI photos (pharmacy shelf, softgels, x-ray heart / nerves / brain, focused man). Dropped as TikTok risk: 'lenguh, kebas-kebas … insya-Allah dapat bantu'.",
     "_note": "VTEAY Omega-3 Fish Oil #1 — A-roll assets/a.mp4 = VID_20261106_084402 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Figures (2,500 mg fish oil, 483 EPA, 644 DHA, 60 softgel, 2 a day), KKM, promo 11.11 are the owner's own words from the label; no price.",
     "segments": segs,
     "infocard": [{"from": ["S03", "start"], "to": ["S05", "end"], "body": "<b>3 benda</b> yang kena cek sebelum beli Omega-3 Fish Oil:",
                   "items": ["Kandungan EPA", "Kandungan DHA", "Kelulusan KKM"]}],
     "punch": [["S17", "dapatkan", 1.06]],
     "broll": [cu("C1", ["S06", "omega-3"], ["S06", "end"], 66.0), cu("C2", ["S07", "start"], ["S07", "end"], 75.40),
               cu("C3", ["S08", "start"], ["S09", "end"], 79.10, "55% 45%", (1.4, 1.55)), cu("C4", ["S10", "start"], ["S10", "end"], 154.50),
               cu("C5", ["S11", "start"], ["S11", "end"], 180.40), cu("C6", ["S16", "start"], ["S16", "end"], 230.70)],
     "photos": [ph("rak", ["S01", "start"], ["S02", "end"], "AI: rak suplemen di farmasi"),
                ph("softgel", ["S14", "start"], ["S15", "end"], "AI: softgel minyak ikan"),
                ph("x_jantung", ["S12", "start"], ["S12", "saraf"], "AI: x-ray jantung"),
                ph("x_saraf", ["S12", "saraf"], ["S12", "end"], "AI: x-ray saraf"),
                ph("x_otak", ["S13", "start"], ["S13", "supaya"], "AI: x-ray otak"),
                ph("fokus", ["S13", "supaya"], ["S13", "end"], "AI: lelaki fokus bekerja")],
     "theme": {"key": "#5FB8E0", "brand": "#FFFFFF"},
     "brand_words": ["vteay"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
