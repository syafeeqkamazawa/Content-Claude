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
