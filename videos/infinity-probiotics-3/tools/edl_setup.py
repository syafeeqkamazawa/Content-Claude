"""EDL for infinity-probiotics-3 (VID_20261102_233818), 2 Nov."""
import json, pathlib
P = pathlib.Path('/home/user/Content-Claude/videos/infinity-probiotics-3')


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 8.70, 23.35, "Kalau najis korang berketul macam ni, dan muka korang macam ni, badan korang ada water retention tau, dan ada banyak toksin yang tersangkut dalam badan korang. Dan bila korang mula nampak muka makin bloated,", "HOOK"),
    seg("S02", 27.85, 36.15, "ya korang minum banyak air, tapi korang masih dahaga. Itulah tanda badan korang tak cukup nutrien yang diperlukan.", "false start 'ya korang minum banyak' (23.9-25.4) dropped"),
    seg("S03", 41.80, 45.90, "Itu yang jadi kembung perut dan lately korang sentiasa rasa penat."),
    seg("S04", 57.20, 71.00, "Dan mungkin korang fikir minum air lebih banyak dan makan lebih sihat tu akan bantu. Tapi tak. Sebab kebanyakan makanan kita dan sayuran kita beracun dan tak cukup nutrien yang badan kita perlukan.", "second take (first cut off at 46.4-49.7)"),
    seg("S05", 77.90, 82.40, "Even air filter pun yang kita minum dekat rumah tu tak cukup mineral.", "'Even air filter pun' false start (75.2) dropped"),
    seg("S06", 97.50, 104.35, "So sebelum korang minum air lagi banyak, yang mana saya tak recommend korang buat macam tu, korang cuba Infinity Probiotic Plus.", "second take (first, 82.9-92.4, trails off)"),
    seg("S07", 105.40, 113.65, "Probiotic ni akan bantu untuk bersihkan usus. Dan ramai tak tahu yang usus kita ni berkaitan dengan 80% masalah yang badan kita ada."),
    seg("S08", 119.00, 136.50, "Bila usus kita sihat, dia akan bantu untuk flush toksin daripada badan kita. Bantu dengan sistem imun kita. Bantu dengan kolesterol kita. Even fokus kita, mood kita. Muka breakout ni pun berkaitan dengan kesihatan usus."),
    seg("S09", 144.60, 157.10, "Probiotic Plus daripada Infinity ni dah komplit dengan probiotic dan prebiotic sekali. Jadi memang sangat sesuai untuk orang yang ada masalah water retention, masalah muka sembab, perut bloated."),
    seg("S10", 157.45, 164.15, "Brand Infinity ni dah lebih 400 ribu dah terjual. So insya-Allah memang dah berkesan untuk ramai orang."),
    seg("S11", 173.25, 175.90, "Dan lebih convenient untuk konsisten ambil setiap hari.", "second take (first at 167.6)"),
    seg("S12", 187.60, 194.20, "So kalau korang dah rasa penat, hadap muka breakout, boleh try probiotic daripada Infinity ni.", "two false starts (175.9, 184.2) dropped"),
    seg("S13", 213.36, 216.70, "Kalau stok masih ada dan korang ada rezeki, beg kuning ada dekat bawah.", "CTA (earlier takes 194-210 and the 'Ni' dropped)", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')  # word times spread over the detected speech by syllables
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word2", "fs_style": "ref", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "2 Nov: Drive folder 1xPV9TTz… 'Infinity Probiotics Plus' — 'Kali ni caption style ikut sama seratus peratus macam dalam gambar title Guna caption style sama macam ni.jpg. Dan style overlay mesti sama seratus peratus dengan video title Ikut video ni untuk overlay.mp4' (aurat rule still applies). Caption copied from the still: one upper-case word at a time, plain white heavy sans (Montserrat ExtraBold, OFL), soft dark shadow, no outline, centred at ~68 % height, hard cuts. Overlay style copied from the reference: frequent full-screen cutaways that land with a zoom blur (watercolour gut illustration, lifestyle shots, macro food and water, acne close-up), product macro in hands, a bold italic 'INFINITY / PROBIOTIK PLUS' title with a yellow bar when the product is named, a white article card dropping from the top, and small italic '400 ribu telah terjual' sales text beside the head. 1 Nov: keep every point; product close-ups and the owner using the product. 28 Oct: premium motion-text hook, no transition effect.",
     "_note": "Infinity Probiotics Plus #3 — A-roll assets/a.mp4 = VID_20261102_233818 (front camera saved mirrored — label reads 'sulP scitoiborP' — flipped back in CSS; audio gated, already clean). B-roll assets/b.mp4 = VID_20261014_001726 (muted; also used in infinity-probiotics-plus and -2): box front 3-10, bottle in hand 14-34, opening 35-38, capsules into the cap and palm 40-68. Every point kept; only repeats/false starts dropped. The info card only restates the owner's own line (usus ↔ 80% masalah). '400 ribu terjual' and 'berkesan untuk ramai orang' are the owner's own words.",
     "segments": segs,
     "hook_text": {"kicker": "Infinity Probiotic Plus", "lines": ["Badan simpan air", "& toksin?"], "accent_words": ["toksin?"],
                   "to": 3.4, "accent": "#F2B705", "accent2": "#2BB3C0", "top": 140},
     "punch": [["S13", "beg", 1.06]],
     "broll": [br("B1", ["S07", "bersihkan"], ["S07", "dan"], 14.5, "001726: botol di tangan (product close-up)", (1.0, 1.08)),
               br("B2", ["S09", "start"], ["S09", "jadi"], 49.0, "001726: botol + kapsul di tapak tangan", (1.0, 1.06), "50% 55%"),
               br("B3", ["S10", "so"], ["S10", "end"], 7.0, "001726: kotak depan", (1.0, 1.08), "50% 40%"),
               br("B4", ["S11", "start"], ["S11", "end"], 60.0, "001726: kapsul di penutup + botol di tapak tangan (guna produk; zoomed so the shelf behind stays soft)", (1.22, 1.3), "50% 60%"),
               br("B5", ["S12", "boleh"], ["S12", "end"], 26.0, "001726: botol di tapak tangan", (1.0, 1.08))],
     "photos": [ph("najis", ["S01", "najis"], ["S01", "muka"], "AI: najis berketul (abstrak, studio putih)"),
                ph("muka", ["S01", "muka"], ["S01", "badan"], "AI: muka sembab (profil)"),
                ph("usus", ["S01", "banyak"], ["S01", "dan#3"], "AI: ilustrasi usus + toksin (watercolour)"),
                ph("sembab", ["S01", "nampak"], ["S02", "tapi"], "AI: muka sembab di cermin"),
                ph("dahaga", ["S02", "tapi"], ["S02", "itulah"], "AI: minum air, masih dahaga"),
                ph("kembung", ["S03", "kembung"], ["S03", "dan"], "AI: kembung perut"),
                ph("penat", ["S03", "lately"], ["S03", "end"], "AI: penat"),
                ph("air", ["S04", "minum"], ["S04", "makan"], "AI: air dituang ke gelas"),
                ph("makan", ["S04", "makan"], ["S04", "tapi"], "AI: makan sihat"),
                ph("sayur", ["S04", "makanan"], ["S04", "beracun"], "AI: sayur dipotong"),
                ph("racun", ["S04", "beracun"], ["S04", "end"], "AI: racun perosak disembur"),
                ph("filter", ["S05", "air"], ["S05", "end"], "AI: air penapis di rumah"),
                ph("flush", ["S08", "flush"], ["S08", "bantu#2"], "AI: ilustrasi usus dibersihkan"),
                ph("imun", ["S08", "bantu#2"], ["S08", "bantu#3"], "AI: sel imun (3D)"),
                ph("kolesterol", ["S08", "bantu#3"], ["S08", "even"], "AI: kolesterol dalam salur darah (3D)"),
                ph("fokus", ["S08", "even"], ["S08", "mood"], "AI: fokus bekerja"),
                ph("mood", ["S08", "mood"], ["S08", "muka"], "AI: mood tenang"),
                ph("jerawat", ["S08", "muka"], ["S08", "end"], "AI: muka breakout"),
                ph("bloated", ["S09", "retention"], ["S09", "end"], "AI: perut bloated")],
     "brand_title": [{"from": ["S06", "infinity"], "to": ["S07", "bantu"], "top": "INFINITY", "bar": "PROBIOTIK PLUS", "y": 820}],
     "infocard": [{"from": ["S07", "ramai"], "to": ["S07", "end"],
                   "body": "Ramai tak tahu, <b>usus</b> kita berkaitan dengan <b>80%</b> masalah yang badan kita ada. Bila usus sihat, ia bantu:", "items": ["Flush toksin daripada badan", "Sistem imun", "Kolesterol", "Fokus dan mood", "Muka breakout"]}],
     "stamp": [{"from": ["S10", "400"], "to": ["S10", "so"], "text": "400 ribu telah terjual", "x": 430, "y": 860}],
     "theme": {"key": "#F2B705", "brand": "#2BB3C0"},
     "brand_words": ["infinity", "probiotic", "plus"], "keywords": []}
old = P / 'data/edl.json'
if old.exists():
    e["flap_force"] = json.loads(old.read_text()).get("flap_force", [])
old.write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
