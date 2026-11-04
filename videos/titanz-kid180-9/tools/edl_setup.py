"""EDL for titanz-kid180-9 (VID_20261104_143358), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 1.40, 6.55, "Kalau ibu ayah nak anak-anak tinggi, kena bantu mereka sebelum umur 18 tahun.", "HOOK"),
    seg("S02", 7.00, 11.45, "Sebab tumbesaran anak-anak paling aktif sebelum umur mereka mencapai 18 tahun."),
    seg("S03", 11.60, 13.98, "Selepas daripada tu, dah agak terlambat."),
    seg("S04", 14.45, 20.30, "Kalau anak-anak ada masalah rendah berbanding kawan-kawan dia yang sama umur, lepas tu dia pula jenis memilih makanan,"),
    seg("S05", 38.40, 43.72, "ibu ayah boleh bagi anak-anak makan supplement Kid180 ni.", "earlier takes 20-34 dropped"),
    seg("S06", 52.20, 63.50, "Supplement ni, ibu ayah jangan risau, supplement ni ada sijil halal, HACCP, GMP dan juga MeSTI. Insya-Allah selamat untuk anak-anak kita.", "first take 44-50 dropped"),
    seg("S07", 63.80, 65.90, "Paling penting, dia ada kelulusan KKM juga."),
    seg("S08", 70.30, 75.55, "Kid180 ni dia bagi nutrisi yang diperlukan oleh anak-anak kita untuk tumbesaran."),
    seg("S09", 88.80, 95.15, "Satu tablet ni bersamaan dengan tiga cawan susu tau, ataupun makan sayur dan buah yang ada lebih 20 jenis vitamin.", "takes 75.9 and 99.4 dropped; 'bukan, bukan' dropped"),
    seg("S10", 115.40, 124.55, "Kid180 ni, sebelum ni harga dia mahal sikit tau. Sekarang saya tengah buat promo untuk masa yang terhad.", "spoken 'Kid satu lapan kosong'"),
    seg("S11", 124.64, 127.35, "Kid180 ni dah makin viral dekat TikTok Shop."),
    seg("S12", 127.75, 130.10, "So kalau ibu ayah yang risaukan tumbesaran anak,"),
    seg("S13", 137.58, 142.50, "atau ada anak yang picky eater, boleh dapatkan Kid180 ni dekat link video ni.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word3", "fs_style": "box", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: 'Ada satu lagi video saya bercakap, yang tu buat juga' — second talking clip in Drive folder 1aleA_8B… 'Kid180 Tablet', with 'video rujukan 2.mp4' (same creator as reference 1). Copied from reference 2: a small italic title sticker on a coral label top-centre for the whole video ('Nak anak2 tinggi?'), captions of 2-3 upper-case heavy white words with the spoken word in yellow, one TV colour-bar glitch frame on an early cut, letterboxed photo cutaways on black, product close-ups. Aurat rule kept. 1 Nov: keep every point; product close-ups and the owner's own footage.",
     "_note": "Tiny Titanz Kid180 #9 — A-roll assets/a.mp4 = VID_20261104_143358 (front camera saved mirrored — label reads backwards — flipped back in CSS). B-roll pool assets/b.mp4 = the same pool as titanz-kid180-8 (hard link); the children's-hands shot (87-104) is not used (bare feet in the background); picks differ from #8 (#8 uses 2.2-9.7, 19-26, 33.5-38.3, 43.4-47, 50-56, 92-94.5). Clip -> video: 142139 -> #8, 143358 -> #9. 'Sebelum ni harga dia mahal sikit' and 'saya tengah buat promo' are the owner's own words; no figure quoted.",
     "segments": segs,
     "sticker": {"text": "Nak anak-anak tinggi?"},
     "glitch": [["S02", "start"]],
     "punch": [["S13", "dapatkan", 1.06]],
     "broll": [br("B1", ["S05", "supplement"], ["S05", "end"], 27.2, "153413: buka botol Kid180 (guna produk)", (1.0, 1.06)),
               br("B2", ["S06", "sijil"], ["S06", "insya-allah"], 72.5, "140338: tablet dituang ke penutup (guna produk)"),
               br("B3", ["S08", "start"], ["S08", "end"], 37.9, "153413: tablet di tapak tangan + botol", (1.0, 1.08)),
               br("B4", ["S10", "sekarang"], ["S10", "end"], 7.9, "153413: kotak depan", (1.0, 1.08), "50% 40%")],
     "photos": [ph("kelas", ["S02", "start"], ["S02", "end"], "AI: kanak-kanak aktif di tadika"),
                ph("rendah", ["S04", "masalah"], ["S04", "lepas"], "AI: anak lebih rendah daripada kawan"),
                ph("memilih", ["S04", "lepas"], ["S04", "end"], "AI: anak memilih makanan"),
                ph("susu9", ["S09", "tiga"], ["S09", "ataupun"], "AI: susu dituang"),
                ph("buah9", ["S09", "ataupun"], ["S09", "end"], "AI: sayur dan buah")],
     "theme": {"key": "#FFE600", "brand": "#7DDB6B"},
     "brand_words": ["kid180"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
