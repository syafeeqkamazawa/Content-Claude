# Sejadah Myna #1 (folder "Sejadah Myna", 25 Nov): VID_20261125_173047 (talking, 64 s) + 173825 (B-roll of the mat, 30 s).
# Owner: "Tak nak motion style lama. Buat motion style baru sesuai dengan vibe content produk" -> "mihrab" motion (EDL "mh",
# tools/build.py section 4d): gold arch that draws itself, a turning eight-point star, serif lines rising out of a mask,
# emerald plaques with a light sweep. No kp / fx cards. Combo source: videos/_myna/tools/combo.py myna1 173047:0:64.36 173825:0:29.96:b
E4 = ["LAST", "end"]
SPECS["myna1"] = {
    "src": "_myna/.media/combo-myna1.mp4", "wl": [("_myna/.media/wl-combo-myna1.txt", 0, 1e9)], "vad": "_myna/.media/vad-combo-myna1.txt",
    "range": (0.0, 94.319), "srcnote": "VID_20261125 173047 + 173825 (B-roll)",
    "slug": "sejadah-myna-1", "name": "Sejadah Myna #1",
    "pal": pal("#D8B46A", bg="rgba(9,52,47,.92)", dark="#0B3B36", cap="#FBF6EA"), "brand": ["myna"],
    "keywords": ["selesa", "desain", "anti", "slip", "grip", "getah", "lantai", "cantik", "promosi", "murah", "kuning"],
    "kp": ("SEJADAH MYNA", ["MYNA"], S1, W("Jangan#1"), 200, 100),
    "drop": [], "dropnote": "nothing (clean single take)",
    "fix": {"terdiri": "tersendiri"},
    "cut": [(W("Jangan#1"), W("Dengan#1"), 66.4, "50% 50%", "the mat from above (B-roll)"),
            (W("Dengan#1"), W("Dan#1"), 70.4, "50% 50%", "the mihrab design close up (B-roll)"),
            (W("Jadi#1"), W("Harga#1"), 76.4, "50% 50%", "the mat on the floor, pan (B-roll)"),
            (W("Harga#1"), E4, 82.4, "50% 50%", "the mat, full view (B-roll)")],
    "fx": [],
    "mh": [
        {"type": "hook", "from": S1, "to": W("Bila#2"), "kicker": "Solat lebih selesa", "lines": ["Sejadah", "tak bergerak"], "hi": ["tak", "bergerak"], "y": 110},
        {"type": "list", "from": W("sangat#1"), "to": W("Dan#1"), "y": 170,
         "items": [{"text": "Sangat selesa", "at": W("sangat#1")}, {"text": "Desain sedap mata", "at": W("desain#1")}]},
        {"type": "list", "from": W("anti#1"), "to": W("So#3"), "y": 100,
         "items": [{"text": "Anti slip", "at": W("anti#1")}, {"text": "Lapisan getah", "at": W("lapisan#1")}]},
        {"type": "point", "from": W("letak#1"), "to": W("Jadi#1"), "text": "Tak mudah bergerak", "y": 170},
        {"type": "point", "from": W("pelbagai#1"), "to": W("Harga#1"), "text": "Pelbagai desain", "y": 170},
        {"type": "cta", "from": W("Harga#1"), "to": E4, "tag": "BEG KUNING", "lines": ["Harga promosi,", "beli sekarang"], "hi": ["promosi,"],
         "sub": "Sementara harga masih murah", "y": 120},
    ],
    "ai": [("A1", W("Bila#2"), W("Jangan#1"), f"A Malaysian man about to pray at home, frowning as his thin prayer mat slides and bunches up on a shiny tiled floor under his feet. {M}"),
           ("A2", W("So#3"), W("Jadi#1"), f"A Malaysian man praying calmly in sujud on a flat emerald prayer mat lying firmly on a polished tiled floor, peaceful morning light. {M}")],
}

# Jam Kaabah #1 (folder "Jam Kaabah", 25 Nov): VID_20261125_192511 (talking, 64 s) + 192230 / 192306 (B-roll of the clock).
# Same brief (new motion style for the product's vibe) -> "haramain night" clock motion (EDL "jm"): gold dial that draws
# itself, hour marks lighting up like lamps, hands sweeping to 10:10 and ticking; small ticking dials on each point.
# Combo: videos/_jam/tools/combo.py jam1 192511:0:63.85 192230:0:25.17:b 192306:0:9.68:b
SPECS["jam1"] = {
    "src": "_jam/.media/combo-jam1.mp4", "wl": [("_jam/.media/wl-combo-jam1.txt", 0, 1e9)], "vad": "_jam/.media/vad-combo-jam1.txt",
    "range": (0.0, 98.702), "srcnote": "VID_20261125 192511 + 192230 / 192306 (B-roll)",
    "slug": "jam-kaabah-1", "name": "Jam Kaabah #1",
    "pal": pal("#E3B85A", bg="rgba(11,21,48,.92)", dark="#0B1530", cap="#FFFFFF"), "brand": ["kaabah"],
    "keywords": ["cantik", "tenang", "desain", "kaabah", "saiz", "islami", "ketenangan", "promosi", "murah", "kuning"],
    "kp": ("JAM KAABAH", ["KAABAH"], S1, W("Dia#1"), 200, 100),
    "drop": [(-1, 21.6), (29.5, 31.35)], "dropnote": "handling noise while he hangs the clock (0-21.6 s, no speech) and a breath between lines (29.5-31.35)",
    "fix": {"lawan": "lawa", "berinat": "berminat"},
    "cut": [(S1, W("Dia#1"), 93.0, "50% 50%", "the room with the clock on the wall (B-roll 192306)"),
            (W("Dia#1"), W("Korang#2"), 64.2, "50% 45%", "the clock close up (B-roll 192230)"),
            (W("Ada#3"), W("Yang#3"), 69.9, "50% 50%", "the clock on the wall (B-roll 192230)"),
            (W("Yang#3"), W("naik#1"), 71.5, "50% 50%", "the clock on the wall, slow pan (B-roll 192230)"),
            (W("So,#1"), E4, 75.9, "50% 50%", "the clock on the wall (B-roll 192230)")],
    "fx": [],
    "jm": [
        {"type": "hook", "from": S1, "to": W("Dia#1"), "kicker": "Jam Kaabah", "lines": ["Sangat cantik,", "vibe tenang"], "hi": ["cantik,", "tenang"], "y": 260},
        {"type": "tick", "from": W("Dia#1"), "to": W("Korang#2"), "text": "Vibe tenang", "hi": ["tenang"], "y": 240},
        {"type": "tick", "from": W("Ada#3"), "to": W("Yang#3"), "text": "Pelbagai saiz & desain", "y": 300},
        {"type": "tick", "from": W("Yang#3"), "to": W("naik#1"), "text": "Sangat cantik", "hi": ["cantik"], "y": 300},
        {"type": "tick", "from": W("naik#1"), "to": W("So,#1"), "text": "Vibe islami, tenang", "hi": ["islami,"], "y": 240, "side": "left"},
        {"type": "cta", "from": W("So,#1"), "to": E4, "tag": "BEG KUNING", "lines": ["Harga promosi,", "beli sekarang"], "hi": ["promosi,"],
         "sub": "Sementara harga masih murah", "y": 250},
    ],
    "ai": [("A1", W("naik#1"), W("So,#1"), f"A peaceful Malaysian Muslim home living room at night in warm lamp light, a man in baju melayu and songkok sitting on a prayer mat reading the Quran, calm atmosphere. {M}")],
}

# Buku Leveled Reading #2 (folder "Buku Leveled Reading", 25 Nov): VID_20261125_212521 (talking + demo, 245 s) + 212738
# (B-roll of the book's pages, 66 s). Same brief -> "storybook" motion (EDL "sb"): letter blocks that flip in, speech
# bubbles that pop, a CTA that opens like a book. Combo: videos/_lvl/tools/combo.py lvl1 212521:0:245.2 212738:0:65.77:b
SPECS["lvl1"] = {
    "src": "_lvl/.media/combo-lvl1.mp4",
    "wl": [("_lvl/.media/wl-212521.txt", 0, 58), ("_lvl/.media/wl2-212521.txt", 58, 144), ("_lvl/.media/wl-212521.txt", 144, 245.2)],
    "vad": "_lvl/.media/vad-combo-lvl1.txt",
    "range": (0.0, 310.97), "srcnote": "VID_20261125 212521 + 212738 (B-roll)",
    "slug": "leveled-reading-book-2", "name": "Buku Leveled Reading #2", "mirror": True,
    "pal": pal("#FFC531", bg="rgba(29,58,138,.92)", dark="#1D3A8A", cap="#FFFFFF"), "brand": ["leveled", "reading"],
    "keywords": ["telefon", "phone", "bahaya", "mengamuk", "aktiviti", "bunyi", "cerita", "perkataan", "lagu", "kualiti", "keluarga", "promo", "murah", "kuning"],
    "kp": ("LEVELED READING", ["READING"], S1, W("Kadang-kadang#1"), 200, 100),
    "drop": [(91.3, 144.0), (164.5, 179.8), (199.0, 212.7), (240.8, 246.0)],
    "dropnote": "the book reading its pages on its own (91-144 s, no speech of his), the song running on and 'shoulder ni' (164.5-180), "
                "two false starts of 'tapi bukanlah maksudnya terus...' (202-212.7; the third take is kept) and the trailing noise after the CTA",
    "fix": {"level": "Leveled", "gu": "Go", "backcuni": "beg kuning", "terasal": ""},
    "cut": [(W("Macam#2"), W("Sebab#6"), 245.7, "50% 50%", "the book cover (B-roll)"),
            (W("Sebab#6"), W("Tengok#1"), 271.2, "50% 50%", "a finger pressing the pet / bat page (B-roll)"),
            (W("tujuh#1"), W("Siap#1"), 279.2, "50% 50%", "the story pages (B-roll)"),
            (W("Siap#1"), W("Tekan#4"), 257.2, "50% 50%", "the children's songs page (B-roll)"),
            (W("Boleh#4"), W("Tapi#2"), 283.5, "50% 50%", "pressing the 'A beautiful dream' page (B-roll)"),
            (W("So#4"), W("Sebab#7"), 251.7, "50% 50%", "the cover and the ABC page (B-roll)"),
            (W("Sementara#1"), E4, 305.2, "50% 50%", "the book cover (B-roll)")],
    "fx": [],
    "sb": [
        {"type": "hook", "from": S1, "to": W("Kadang-kadang#1"), "blocks": "TELEFON", "line": "Anak susah nak lepas?", "y": 150},
        {"type": "bubble", "from": W("Itu#1"), "to": W("Sebab#4"), "text": "Bahaya untuk long term", "y": 260, "color": "#F2483C"},
        {"type": "bubble", "from": W("aktiviti#1"), "to": W("Macam#2"), "text": "Perlu aktiviti lain!", "y": 260, "side": "left", "color": "#3DBE5A"},
        {"type": "bubble", "from": W("tekan#1"), "to": W("Tengok#1"), "text": "Tekan & dengar bunyi", "y": 260, "color": "#2E9BF0"},
        {"type": "bubble", "from": W("tujuh#1"), "to": W("Lebih#1"), "text": "17 cerita", "y": 260, "side": "left", "color": "#FF5D8F"},
        {"type": "bubble", "from": W("Lebih#1"), "to": W("Siap#1"), "text": "200+ perkataan", "y": 260, "color": "#8C6CF0"},
        {"type": "bubble", "from": W("Siap#1"), "to": W("Tekan#4"), "text": "Lagu kanak-kanak", "y": 260, "side": "left", "color": "#FFC531"},
        {"type": "bubble", "from": W("kualiti#1"), "to": W("Boleh#4"), "text": "Masa berkualiti", "y": 260, "color": "#FF5D8F"},
        {"type": "bubble", "from": W("Boleh#4"), "to": W("Tapi#2"), "text": "Dengar & sebut sama-sama", "y": 260, "side": "left", "color": "#2E9BF0"},
        {"type": "bubble", "from": W("sekurang-kurangnya#1"), "to": W("So#4"), "text": "Ada pilihan aktiviti lain", "y": 260, "color": "#3DBE5A"},
        {"type": "bubble", "from": W("harga#1"), "to": W("Sementara#1"), "text": "Harga promo!", "y": 260, "side": "left", "color": "#F2483C"},
        {"type": "cta", "from": W("Sementara#1"), "to": E4, "tag": "BEG KUNING", "lines": ["Harga promo,", "beli sekarang!"],
         "sub": "Sementara harga tengah murah", "y": 200},
    ],
    "ai": [("A1", W("Kalau#1"), W("Kadang-kadang#1"), f"A Malaysian boy about five slumped on a sofa staring at a smartphone, the screen glow on his face, toys ignored beside him, evening living room. {K}"),
           ("A2", W("Sebab#2"), W("Tapi#1"), f"A busy Malaysian mother working on her laptop at the dining table while her young daughter sits beside her watching a phone. {F} {K}"),
           ("A3", W("bila#2"), W("Itu#1"), f"A Malaysian boy about four crying in a tantrum on the living-room floor after his phone was taken away, his mother kneeling calmly beside him. {F} {K}"),
           ("A4", W("Orang#1"), W("Boleh#4"), f"A Malaysian mother and father sitting on the living-room rug with their young son and daughter, all laughing while pressing the pictures of a colourful children's book together, warm light. {M} {F} {K}")],
}
