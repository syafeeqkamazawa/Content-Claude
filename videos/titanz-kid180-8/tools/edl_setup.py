"""EDL for titanz-kid180-8 (VID_20261104_142139), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 3.70, 12.20, "Ibu ayah yang risau tumbesaran anak terbantut tu, kena pastikan nutrien intake anak tu lengkap.", "HOOK"),
    seg("S02", 21.00, 24.25, "Ada orang cakap, bukankah ketinggian ni faktor keturunan?", "doubled 'ada orang cakap' (17.8) dropped"),
    seg("S03", 24.45, 36.40, "Okey, menurut kajian, 80% daripada ketinggian seseorang tu memang disebabkan oleh faktor keturunan. Means kalau mak ayahnya tinggi, anaknya pun insya-Allah akan tinggi juga."),
    seg("S04", 40.90, 45.70, "Itu betul, tapi kita kena ingat, 20% lagi adalah disebabkan oleh faktor lain"),
    seg("S05", 45.74, 47.45, "seperti pemakanan.", "false start 47.7-54 dropped"),
    seg("S06", 55.10, 65.20, "Ibu ayah yang risau tumbesaran anak terbantut tu, kena pastikan nutrien intake anak tu lengkap.", "scripted repeat of the hook (as in the reference video)"),
    seg("S07", 91.20, 96.65, "Kalau anak-anak ibu ayah suka memilih makanan, ibu ayah boleh berikan supplement Kid180 ni kepada anak-anak.", "earlier takes 65-84 and the 'kalau ibu ayah ada anak-anak yang suka' stumble dropped"),
    seg("S08", 121.10, 128.95, "Supplement ni jangan risau, dia ada sijil halal, HACCP, GMP, MeSTI, insya-Allah selamat untuk anak-anak.", "last take (97-118 retakes dropped)"),
    seg("S09", 131.60, 134.15, "Paling penting, dia juga dapat kelulusan KKM.", "false start 129.5 dropped"),
    seg("S10", 148.70, 152.55, "Kid180 ni dia bagi nutrien yang diperlukan oleh badan untuk tumbesaran."),
    seg("S11", 152.85, 159.58, "Satu tablet ni bersamaan dengan tiga cawan susu, ataupun makan sayur dan buah, yang ada lebih 20 jenis.", "'vitamin, sebelum ni harga sebotol dalam…' has no price — cut after 'jenis'"),
    seg("S12", 183.90, 193.65, "Sekarang ni harga pun tengah murah, tapi untuk masa terhad. Banyak seller pun dah buat promo 11.11 tau. Cuba korang tengok dekat beg kuning.", "first take 165.9 dropped"),
    seg("S13", 202.00, 204.55, "Kid180 ni dah semakin viral dekat TikTok Shop.", "spoken 'Kid satu lapan kosong'"),
    seg("S14", 244.30, 250.85, "So ibu ayah yang risaukan tumbesaran anak tu, ataupun ada anak yang picky eater, boleh dapatkan Kid180 ni dekat link video ni sekarang.", "CTA, last of five takes (204.9-243)", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3", "fs_style": "box", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: Drive folder 1aleA_8B… 'Kid180 Tablet' with 'video rujukan.mp4' (a Kid180 review by another creator; the owner follows its script). Copied from the reference: captions of 2-3 upper-case heavy white words low in the frame with the spoken word in yellow, hard cuts; photo cutaways letterboxed on black; product close-ups full screen. The reference's comment-reply bubble is not copied (no real comment to answer) — a small top title sticker carries the hook instead (style of the owner's second reference). Aurat rule kept (the reference's family photo shows women without hijab). 1 Nov: keep every point; product close-ups and the owner's own footage.",
     "_note": "Tiny Titanz Kid180 #8 — A-roll assets/a.mp4 = VID_20261104_142139 (front camera saved mirrored — label reads backwards — flipped back in CSS). B-roll pool assets/b.mp4 (muted) = VID_20261014_153413 0-43.33 (box, bottle, tablets in palm) + VID_20260908_140338 43.33-87.0 (tablets poured into the cap) + VID_20260827_170307 87.0-131.6 (tablets into the children's hands; not used in #8 — bare feet in the background). Clip -> video: 142139 -> #8, 143358 -> #9; B-roll shared, different picks. No price shown (the owner's 'sebelum ni harga sebotol dalam…' trails off with no figure); promo 11.11 and 'semakin viral' are the owner's own words.",
     "segments": segs,
     "sticker": {"text": "Tinggi ikut keturunan?"},
     "punch": [["S14", "dapatkan", 1.06]],
     "broll": [br("B1", ["S06", "kena"], ["S06", "end"], 43.4, "140338: botol Kid180 di tangan", (1.0, 1.06)),
               br("B2", ["S07", "supplement"], ["S07", "end"], 19.0, "153413: botol Kid180 di tangan", (1.0, 1.08)),
               br("B3", ["S08", "start"], ["S08", "end"], 2.2, "153413: kotak di tangan (label)", (1.0, 1.08), "50% 40%"),
               br("B4", ["S10", "start"], ["S10", "diperlukan"], 33.5, "153413: tablet di tapak tangan + botol (guna produk)"),
               br("B4b", ["S10", "diperlukan"], ["S10", "end"], 20.5, "153413: botol Kid180 dipusing", (1.0, 1.08)),
               br("B5", ["S12", "start"], ["S12", "cuba"], 50.0, "140338: tablet dituang ke penutup (guna produk)")],
     "photos": [ph("lego", ["S03", "menurut"], ["S03", "means"], "AI: anak bermain blok"),
                ph("keluarga", ["S03", "means"], ["S03", "end"], "AI: keluarga tinggi (menutup aurat)"),
                ph("makan", ["S05", "start"], ["S05", "end"], "AI: pinggan makanan sihat"),
                ph("picky", ["S07", "start"], ["S07", "supplement"], "AI: anak tolak sayur"),
                ph("susu", ["S11", "tiga"], ["S11", "ataupun"], "AI: tiga gelas susu"),
                ph("buah", ["S11", "ataupun"], ["S11", "end"], "AI: sayur dan buah")],
     "theme": {"key": "#FFE600", "brand": "#7DDB6B"},
     "brand_words": ["kid180"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
