"""EDL specs for the five Shilajit batch videos (see plan.md). Source times: assets/a.mp4 = the talking
clip, assets/b.mp4 = pool.mp4 (VID_20261019_090353 0-22.33 + VID_20261019_090625 22.33-114.72)."""


def seg(i, a, b, text, note="", zoom=1.0):
    return {"id": i, "in": a, "out": b, "zoom": zoom, "text": text, "note": note}


def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%"):
    return {"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}


def ph(i, f, t, note):
    return {"id": i, "from": f, "to": t, "note": note}


CARD = lambda f, t: [{"id": "kotak", "from": f, "to": t, "img": "assets/products/kotak.png", "bg": "assets/products/kotak-bg.jpg"}]

COMMON = {
    "fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "flap", "mirror": True,
    "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03},
    "titles": [],
    "theme": {"key": "#F5C451", "brand": "#9FD3FF"},
    "brand_words": ["aurapep", "shilajit", "complex"],
    "keywords": ["penat", "penat,", "lesu", "lesu,", "letih", "nutrisi", "magnesium", "tenaga", "tenaga,", "zinc", "imun", "imun,",
                 "reishi", "reishi.", "reishi,", "kkm", "kkm,", "halal", "gmp", "iso", "iso.", "sekarang", "sekarang,", "promo", "promosi",
                 "promosi.", "murah", "murah,", "stok", "kesihatan", "kesihatan.", "keluarga", "60."],
    "_owner_decisions": "26 Okt: brief premium (2K 60fps 20Mbps, klip bernilai sahaja, hook klip pertama, 3D overlay, kapsyen ikut tema, tiada muzik). Folder Shilajit 12AIw3W3…: 5 klip bercakap → 5 video, setiap klip diguna, tiada julat B-roll berulang (videos/_batch-shilajit/plan.md).",
}

PANEL4 = lambda title, items: {"title": title, "from": items[0][1], "items": [
    {"text": t, "from": f, "done": d} for t, f, d in items]}

NOTE = ("Aurapep Shilajit Complex #{n} — video {k} of the 5-clip batch in Drive folder 12AIw3W3… (videos/_batch-shilajit/plan.md). "
        "A-roll assets/a.mp4 = {clip} (front camera saved mirrored — box reads backwards — flipped back in CSS; lavalier mic). "
        "B-roll assets/b.mp4 = batch pool (VID_20261019_090353 0-22.33 + VID_20261019_090625 22.33-114.72; static box-on-grass shots skipped). "
        "Pool ranges used here: {ranges}. {extra} Owner 26 Oct brief: 2K 60 fps, hook on first clip only, gentle motion, whip transitions, 3D product card, no music.")

SPECS = {
    2: {
        "clip": "VID_20261022_094054",
        "flap_force": [{"from": 12.98, "to": 16.05, "panel": False, "why": "3D product card"}],
        "fix": [(50.86, 51.26, ["Aurapep"]), (51.26, 51.56, ["Shilajit"])],
        "segments": [
            seg("S01", 2.38, 10.32, "Baru tengah hari dah rasa penat, balik kerja pula badan lesu sampai nak luangkan masa dengan keluarga pun dah rasa tak larat.", "HOOK", 1.04),
            seg("S02", 10.32, 18.68, "Jangan abaikan keperluan nutrisi badan kita. Ini Aurapep Shilajit Complex, gabungan Shilajit, Magnesium, Zinc dan Reishi."),
            seg("S03", 23.68, 28.80, "Magnesium membantu badan menghasilkan tenaga, manakala Zinc menyokong sistem imun."),
            seg("S04", 32.32, 36.95, "Jangan risau, produk ni juga dah ada label KKM, sijil halal antarabangsa,", "take 1"),
            seg("S05", 44.50, 46.30, "GMP dan juga ISO."),
            seg("S06", 46.90, 49.80, "Kesihatan kita penting, keluarga pun perlukan kita."),
            seg("S07", 49.80, 56.04, "Nak cuba Aurapep Shilajit Complex, tekan di beg kuning sekarang, harga tengah ada promo, grab terus.", "CTA (spoken only)", 1.04),
        ],
        "hook": {"seg": "S01", "word": "penat,"},
        "punch": [["S07", "terus.", 1.06]],
        "broll": [
            br("B1", ["S02", "ini"], ["S02", "gabungan"], 58.0, "pool: kotak depan dipegang"),
            br("B2", ["S03", "start"], ["S03", "manakala"], 100.0, "pool: buka botol, tablet"),
            br("B3", ["S03", "manakala"], ["S03", "end"], 82.3, "pool: botol dipegang"),
            br("B4", ["S04", "kkm,"], ["S04", "end"], 49.6, "pool: label belakang"),
            br("B5", ["S05", "start"], ["S05", "end"], 109.4, "pool: botol depan"),
        ],
        "photos": [ph("penat", ["S01", "balik"], ["S01", "sampai"], "AI: lelaki letih di pejabat tengah hari"),
                   ph("keluarga", ["S01", "sampai"], ["S01", "end"], "AI: ayah letih di sofa, keluarga bermain")],
        "cards": CARD(["S02", "gabungan"], ["S02", "end"]),
        "panel": PANEL4("SEMAK NUTRISI", [("MAGNESIUM", ["S03", "start"], ["S03", "manakala"]), ("ZINC", ["S03", "manakala"], ["S03", "end"]),
                                          ("LABEL KKM", ["S04", "label"], ["S04", "end"]), ("HALAL GMP ISO", ["S05", "start"], ["S05", "end"])]),
        "_note": NOTE.format(n=2, k=1, clip="VID_20261022_094054 (Drive 1IUVvOG9…)", ranges="49.6, 58.0, 82.3, 100.0, 109.4 (durations in plan.md)",
                             extra="Kept takes: 2.38-10.36, 10.26-18.68, 23.68-28.84, 32.32-36.95 (take 1 of 'jangan risau…'), 44.50-46.30, 46.90-49.84, 49.74-56.04. Dropped the unclear 'memampalkan dokumen…' line (28.8-31.5) and take 2 of 'jangan risau'."),
    },
    3: {
        "clip": "VID_20261022_094207",
        "flap_force": [{"from": 15.95, "to": 19.27, "panel": False, "why": "3D product card"}],
        "segments": [
            seg("S01", 1.02, 8.42, "Pernah tak balik kerja anak ajak main, tapi badan terlalu penat sampai kita cuma mampu cakap, nanti dulu ya.", "HOOK", 1.04),
            seg("S02", 8.40, 13.76, "Kadang-kadang kita terlalu sibuk cari rezeki untuk keluarga sampai terlupa nak jaga kesihatan sendiri."),
            seg("S03", 13.76, 23.86, "Sebab tu saya nak kongsikan Aurapep Shilajit Complex ni. Ada magnesium yang bantu badan menghasilkan tenaga dan zinc untuk menyokong sistem imun kita."),
            seg("S04", 29.48, 39.06, "Produk ni juga turut mengandungi Shilajit dan Reishi, dan juga ada label KKM serta sijil halal antarabangsa, GMP dan juga ISO."),
            seg("S05", 39.06, 48.12, "Keluarga bukan cuma perlukan duit kita je, mereka juga perlukan masa dan perhatian kita. Tekan beg kuning sekarang, harga tengah murah, boleh check out terus.", "CTA (spoken only)", 1.04),
        ],
        "hook": {"seg": "S01", "word": "penat"},
        "punch": [["S05", "terus.", 1.06]],
        "broll": [
            br("B1", ["S03", "aurapep"], ["S03", "ada"], 43.6, "pool: ambil kotak, depan"),
            br("B2", ["S03", "dan"], ["S03", "end"], 90.0, "pool: botol berpusing"),
            br("B3", ["S04", "shilajit"], ["S04", "dan#2"], 65.4, "pool: buka kotak"),
            br("B4", ["S04", "ada"], ["S04", "halal"], 51.7, "pool: label belakang"),
            br("B5", ["S04", "antarabangsa,"], ["S04", "end"], 111.9, "pool: botol depan"),
        ],
        "photos": [ph("anak", ["S01", "tapi"], ["S01", "end"], "AI: anak ajak ayah yang letih bermain"),
                   ph("s1penat", ["S02", "sibuk"], ["S02", "end"], "AI (dari Shilajit #1): lelaki letih di pejabat"),
                   ph("s1keluarga", ["S05", "mereka"], ["S05", "tekan"], "AI (dari Shilajit #1): keluarga bermain di taman")],
        "cards": CARD(["S03", "ada"], ["S03", "dan"]),
        "panel": PANEL4("SEMAK NUTRISI", [("MAGNESIUM", ["S03", "ada"], ["S03", "dan"]), ("ZINC", ["S03", "dan"], ["S03", "end"]),
                                          ("SHILAJIT REISHI", ["S04", "start"], ["S04", "dan#2"]), ("KKM HALAL", ["S04", "ada"], ["S04", "end"])]),
        "_note": NOTE.format(n=3, k=2, clip="VID_20261022_094207 (Drive 1d-auJr_…)", ranges="43.6, 51.7, 65.4, 90.0, 111.9 (durations in plan.md)",
                             extra="Kept takes: 1.02-8.46, 8.40-13.80, 13.70-23.86, 29.48-39.10 (after the false start 'turut mengandungi' 28.2), 39.04-48.12."),
    },
    4: {
        "clip": "VID_20261022_094336",
        "flap_force": [{"from": 16.18, "to": 20.55, "panel": False, "why": "3D product card"}],
        "fixw": [(1.5, 16.5, [('Lelaki',9.46,9.98),('ni',9.98,10.12),('kadang',10.12,10.38),('-kadang',10.38,10.60),('pelik,',10.60,10.98),('kereta',11.32,12.04),('kita',12.04,12.26),('servis',12.26,12.64),('ikut',12.64,12.86),('masa,',12.86,13.10),('tapi',13.10,13.90),('badan',13.90,14.26),('sendiri',14.26,14.46),('dah',14.46,14.64),('selalu',14.64,14.90),('penat,',14.90,15.20),('kita',15.20,15.46),('buat',15.46,15.62),('tak',15.62,15.76),('tahu',15.76,16.06),('je',16.06,16.34)])],
        "segments": [
            seg("S01", 9.40, 16.40, "Lelaki ni kadang-kadang pelik, kereta kita servis ikut masa, tapi badan sendiri dah selalu penat, kita buat tak tahu je.", "HOOK (take 2)", 1.04),
            seg("S02", 17.00, 24.62, "Pagi kerja, petang balik lesu, esok ulang benda yang sama. Sebab tu penting untuk kita jaga pengambilan nutrisi harian kita."),
            seg("S03", 27.96, 36.76, "Ini Aurapep Shilajit Complex. Ada magnesium yang bantu badan menghasilkan tenaga dan zinc untuk menyokong sistem imun, turut mengandungi Shilajit dan Reishi."),
            seg("S04", 39.90, 44.96, "Produk ni juga ada label KKM serta sijil halal antarabangsa, GMP dan juga ISO."),
            seg("S05", 52.90, 56.32, "Kereta rosak boleh tukar, tapi badan kita cuma ada satu je."),
            seg("S06", 60.28, 64.80, "Tekan beg kuning sekarang, sementara stok ada tu, dan harga pun tengah promosi tu,", "CTA (spoken only)"),
            seg("S07", 71.52, 72.60, "grab terus!", "", 1.04),
        ],
        "hook": {"seg": "S01", "word": "pelik,"},
        "punch": [["S07", "terus!", 1.06]],
        "broll": [
            br("B1", ["S02", "penting"], ["S02", "end"], 19.3, "pool (090353): ambil kotak, depan"),
            br("B2", ["S03", "start"], ["S03", "ada"], 60.5, "pool: kotak depan dipegang"),
            br("B3", ["S03", "turut"], ["S03", "end"], 102.9, "pool: tablet dalam botol"),
            br("B4", ["S04", "label"], ["S04", "antarabangsa,"], 53.8, "pool: label belakang"),
            br("B5", ["S04", "antarabangsa,"], ["S04", "end"], 67.1, "pool: buka kotak, keluarkan botol"),
        ],
        "photos": [ph("servis", ["S01", "kereta"], ["S01", "tapi"], "AI: kereta diservis di bengkel"),
                   ph("jem", ["S02", "start"], ["S02", "sebab"], "AI: lelaki letih memandu balik kerja")],
        "cards": CARD(["S03", "ada"], ["S03", "turut"]),
        "panel": PANEL4("SEMAK NUTRISI", [("MAGNESIUM", ["S03", "ada"], ["S03", "dan"]), ("ZINC", ["S03", "dan"], ["S03", "turut"]),
                                          ("SHILAJIT REISHI", ["S03", "turut"], ["S03", "end"]), ("KKM HALAL", ["S04", "label"], ["S04", "end"])]),
        "_note": NOTE.format(n=4, k=3, clip="VID_20261022_094336 (Drive 1eqj6qxL…)", ranges="19.3, 53.8, 60.5, 67.1, 102.9 (durations in plan.md)",
                             extra="Kept takes: 9.40-16.40 (take 2 of the hook; take 1 1.9-7.4 dropped), 17.00-24.62, 27.96-36.80, 39.90-44.96, 52.90-56.32 (after 'kereta rosak' false start 51.1), 60.28-64.80, 71.52-72.60. Dropped the unclear 'memaparkan dokumen…' line (36.7-39.1) and the repeated CTA takes."),
    },
    5: {
        "clip": "VID_20261022_094551",
        "flap_force": [{"from": 17.05, "to": 21.35, "panel": False, "why": "3D product card"}],
        "fix": [(19.30, 19.66, ["lesu", "tu"]), (62.80, 63.14, ["beg", "kuning"])],
        "fixw": [(8.9, 14.4, [('Pagi',12.04,12.72),('bangun',12.72,13.08),('rasa',13.08,13.40),('tak',13.40,13.62),('segar,',13.62,14.14),('tengah',14.40,14.68)])],
        "segments": [
            seg("S01", 3.16, 8.02, "Umur baru 30-an atau 40-an tapi badan dah rasa macam umur 60.", "HOOK", 1.04),
            seg("S02", 11.98, 21.92, "Pagi bangun rasa tak segar, tengah hari dah penat, balik kerja pula asyik nak baring je. Jangan anggap badan lesu tu perkara biasa kalau selalu sangat berlaku."),
            seg("S03", 21.92, 24.40, "Ini Aurapep Shilajit Complex."),
            seg("S04", 29.22, 35.32, "Ada magnesium yang bantu menghasilkan tenaga, zinc untuk menyokong sistem imun, bersama Shilajit dan juga Reishi."),
            seg("S05", 35.32, 42.66, "Produk ni ada KKM serta sijil halal antarabangsa, GMP dan ISO."),
            seg("S06", 46.92, 50.64, "Jangan tunggu badan makin tak bermaya baru nak ambil berat tentang kesihatan."),
            seg("S07", 62.18, 67.86, "Tekan beg kuning sekarang guys. Stok cepat habis guys. Harga pun tengah promosi ni. Boleh check out terus.", "CTA (spoken only)", 1.04),
        ],
        "hook": {"seg": "S01", "word": "60."},
        "punch": [["S07", "terus.", 1.06]],
        "broll": [
            br("B1", ["S03", "start"], ["S03", "end"], 70.5, "pool: keluarkan botol dari kotak"),
            br("B2", ["S04", "bersama"], ["S04", "end"], 105.6, "pool: tablet dalam botol"),
            br("B3", ["S05", "kkm"], ["S05", "halal"], 55.42, "pool: label belakang"),
            br("B4", ["S05", "halal"], ["S05", "end"], 85.0, "pool: botol dipegang"),
            br("B5", ["S07", "stok"], ["S07", "boleh"], 78.95, "pool: botol depan, kotak"),
        ],
        "photos": [ph("bangun", ["S02", "start"], ["S02", "tengah"], "AI: lelaki bangun pagi tak segar"),
                   ph("baring", ["S02", "balik"], ["S02", "jangan"], "AI: lelaki baring letih lepas kerja")],
        "cards": CARD(["S04", "start"], ["S04", "bersama"]),
        "panel": PANEL4("SEMAK NUTRISI", [("MAGNESIUM", ["S04", "start"], ["S04", "zinc"]), ("ZINC", ["S04", "zinc"], ["S04", "bersama"]),
                                          ("SHILAJIT REISHI", ["S04", "bersama"], ["S04", "end"]), ("KKM HALAL", ["S05", "kkm"], ["S05", "end"])]),
        "_note": NOTE.format(n=5, k=4, clip="VID_20261022_094551 (Drive 12QkPXDh…)", ranges="55.42, 70.5, 78.95, 85.0, 105.6 (durations in plan.md)",
                             extra="Kept takes: 3.16-8.02, 11.98-21.92 (take 2 of 'pagi bangun…'), 21.84-24.40, 29.22-35.36, 35.24-42.66, 46.92-50.68, 62.18-67.86 (last CTA take)."),
    },
    6: {
        "clip": "VID_20261022_094748",
        "flap_force": [{"from": 12.5, "to": 16.03, "panel": False, "why": "3D product card"}],
        "segments": [
            seg("S01", 11.80, 20.20, "Kita kerja siang malam nak bagi keluarga hidup senang, tapi pernah tak terfikir kalau kesihatan kita terabai, siapa nak jaga keluarga kita nanti?", "HOOK (take 2)", 1.04),
            seg("S02", 21.26, 26.04, "Badan kita pun perlukan nutrisi yang mencukupi guys, ini Aurapep Shilajit Complex,"),
            seg("S03", 40.38, 45.34, "magnesium yang bantu badan menghasilkan tenaga, zinc untuk sokong sistem imun bersama Shilajit dan Reishi."),
            seg("S04", 54.90, 61.46, "Ibu ayah, abang kakak, jangan risau tau, produk ni dah ada label KKM, sijil halal antarabangsa, GMP dan juga ISO."),
            seg("S05", 62.08, 64.92, "Ingat, duit boleh cari tapi kesihatan jangan abaikan."),
            seg("S06", 74.22, 80.76, "Nak cuba Aurapep Shilajit ni, tekan beg kuning sekarang. Harga tengah promosi. Stok pun tak banyak tu. Check out terus.", "CTA (spoken only)", 1.04),
        ],
        "hook": {"seg": "S01", "word": "terfikir"},
        "punch": [["S06", "terus.", 1.06]],
        "broll": [
            br("B1", ["S02", "ini"], ["S02", "end"], 46.4, "pool: kotak depan"),
            br("B2", ["S03", "bersama"], ["S03", "end"], 77.5, "pool: botol dan kotak"),
            br("B3", ["S04", "label"], ["S04", "antarabangsa,"], 88.0, "pool: botol depan"),
            br("B4", ["S04", "antarabangsa,"], ["S04", "end"], 93.1, "pool: penutup botol"),
            br("B5", ["S06", "harga"], ["S06", "check"], 96.6, "pool: botol dipegang"),
        ],
        "photos": [ph("malam", ["S01", "siang"], ["S01", "tapi"], "AI: lelaki kerja lewat malam"),
                   ph("jaga", ["S01", "siapa"], ["S01", "end"], "AI: ayah bersama keluarga")],
        "cards": CARD(["S03", "start"], ["S03", "bersama"]),
        "panel": PANEL4("SEMAK NUTRISI", [("MAGNESIUM", ["S03", "start"], ["S03", "zinc"]), ("ZINC", ["S03", "zinc"], ["S03", "bersama"]),
                                          ("SHILAJIT REISHI", ["S03", "bersama"], ["S03", "end"]), ("KKM HALAL", ["S04", "label"], ["S04", "end"])]),
        "_note": NOTE.format(n=6, k=5, clip="VID_20261022_094748 (Drive 1yFtcb94…)", ranges="46.4, 77.5, 88.0, 93.1, 96.6 (durations in plan.md)",
                             extra="Kept takes: 11.80-20.20 (take 2 of the hook, after 'badan kita pun' false start), 21.26-26.04, 40.38-45.34 (clean take of the magnesium line), 54.90-61.46 (take 2), 62.08-64.92, 74.22-80.76. Dropped the stumbling magnesium takes 26-40 and 'nak tahu lebih lanjut'."),
    },
}
