"""EDL for buku-tahajud-1 (VID_20261107_014958), 7 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="55% 65%", push=(1.25, 1.4)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own copy of the book", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 63.45, 70.15, "Saya betul-betul dah lama tak amalkan solat tahajud.", "HOOK — the slow title reading (30-62.8) dropped"),
    seg("S02", 70.30, 79.75, "Insya-Allah saya nak mulakan satu journey, Day 1 Tahajud Journey bersama Syafiq Kamazawa."),
    seg("S03", 82.85, 85.90, "Setiap hari saya akan share", "stumble 'dan sebelum' dropped"),
    seg("S04", 93.90, 97.60, "sedikit input daripada buku ni, yang mana", "hesitation 'semoga, apa tu, yang mana' (97.6-102.6) dropped"),
    seg("S05", 102.60, 108.70, "tengok video ni pun dapat manfaat sekali, insya-Allah."),
    seg("S06", 110.80, 116.55, "Saya buka dulu plastik dia. Cantik packaging dia, macam ni."),
    seg("S07", 116.70, 127.20, "Insya-Allah, Hidup Dengan Tahajud. Dan di belakang ni ada review lah daripada Mufti Wilayah Persekutuan, Ustaz Haji Ahmad Fawaz bin Fazil juga."),
    seg("S08", 137.75, 142.25, "Buku ni jika tak silap saya, ia daripada Iddin Ramli.", "the unclear 'yang kenal … Malaysia pun dah kenal' (142.4-145.6) left out"),
    seg("S09", 160.15, 166.25, "Saya akan baca dahulu.", "'Day 1 Tahajud Journey' repeat (151-158) dropped"),
    seg("S10", 168.40, 177.15, "Sedikit lah, tak boleh semua kan. Sebab kalau nak baca semua, kena dapatkan lah di beg kuning tadi tu, insya-Allah."),
    seg("S11", 177.75, 179.50, "Jadi saya akan share sedikit"),
    seg("S11b", 180.60, 184.30, "daripada part-part yang ada lah.", "stutter 'lebih, dah sedikit' dropped"),
    seg("S12", 187.70, 188.62, "Pertama,"),
    seg("S13", 193.00, 195.75, "bila waktu dikira sebagai tahajud?"),
    seg("S14", 200.45, 202.20, "Ikut mazhab Syafie,", "first take 'untuk tahajud ni mesti tidur dahulu' (197.2-200) dropped"),
    seg("S14b", 203.15, 206.25, "tahajud tu mesti tidur dahulu selepas isyak.", "filler 'okay' dropped"),
    seg("S15", 208.55, 213.80, "So tidur sedikit pun tak menjadi masalah, janji tidur sebentar.", "the repeat of the same lesson (216-235) dropped"),
    seg("S16", 242.95, 244.42, "Kita akan share lagi", "stutter 'sedikit, sedikit' dropped"),
    seg("S17", 246.35, 249.90, "sedikit di hari-hari seterusnya."),
    seg("S18", 257.90, 260.00, "Semoga mendapat sedikit input.", "unclear 'daripada … saya' left out; 'Tahajud Day 1 bersama Syafiq' repeat (250-256) dropped"),
    seg("S19", 262.15, 266.50, "Kalau nak baca penuh, boleh dapatkan di beg kuning, insya-Allah."),
    seg("S20", 282.85, 294.85, "Semoga kita dapat hidup dengan tahajud, insya-Allah, dan Allah SWT perbaiki kehidupan kita, insya-Allah.", "hesitation (266.9-282.8) dropped"),
    seg("S21", 296.00, 298.10, "Dapatkan di beg kuning, insya-Allah.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "7 Nov: 'Video buku hidup dengan tahajud' — Drive folder 'Buku Hidup Dengan Tahajud By Iddin Ramli' (1RmjrBGH…), one clip VID_20261107_014958. Caption: the 6 Nov default, on the wall above the head (top 300). The owner frames it as a series ('Day 1 Tahajud Journey bersama Syafiq Kamazawa'), so a small series title sits at the top for the opening. Overlays on every explanation (owner 6 Nov): close-ups of the owner's own copy of the book first; realistic aurat-safe AI photos for tahajud at night and sleeping after isyak.",
     "_note": "Buku Hidup Dengan Tahajud #1 — A-roll assets/a.mp4 = VID_20261107_014958 (rear camera, NOT mirrored: the cover reads correctly). assets/b.mp4 = the same clip, muted, not flipped. No price; 'dapatkan di beg kuning' is the owner's own CTA.",
     "segments": segs,
     "toptitle": {"lines": ["Day 1 · Tahajud Journey"], "to": ["S05", "end"], "top": 150},
     "punch": [],
     "broll": [cu("C1", ["S06", "start"], ["S06", "end"], 112.0, "60% 72%"),
               cu("C2", ["S07", "Dan"], ["S07", "end"], 119.5, "45% 72%"),
               cu("C3", ["S08", "ia"], ["S08", "end"], 288.0, "50% 60%", (1.15, 1.22)),
               cu("C4", ["S09", "start"], ["S10", "end"], 172.0, "52% 62%", (1.2, 1.3)),
               cu("C5", ["S16", "start"], ["S19", "end"], 262.0, "55% 62%", (1.2, 1.3))],
     "photos": [ph("tahajud", ["S02", "start"], ["S02", "end"], "AI: solat tahajud waktu malam (lelaki berpakaian penuh)"),
                ph("tidur", ["S14b", "start"], ["S15", "end"], "AI: tidur selepas isyak (lelaki berpakaian penuh)"),
                ph("malam", ["S20", "start"], ["S20", "end"], "AI: sejadah waktu malam (tiada orang)")],
     "theme": {"key": "#7B5EA7", "brand": "#E9E2F5"},
     "brand_words": ["tahajud"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
