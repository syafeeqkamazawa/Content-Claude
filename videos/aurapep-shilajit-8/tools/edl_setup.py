"""EDL for aurapep-shilajit-8 (VID_20261106_171623), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="55% 60%", push=(1.3, 1.45)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own Shilajit bottle / box", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 73.40, 86.68, "Masalah dengan Shilajit ni, especially yang bentuk macam cecair likat tu, rasa dia aduh, memang tak sedap langsung. Rasa macam besi pun ada, macam tanah pun ada juga. So memang susah nak konsisten.", "HOOK — the owner's own problem line moved up (earlier takes 64.3-73.3 dropped); the opening 'soalan lelaki / supplement untuk kesihatan lelaki' (10.9-21.5) dropped: TikTok risk (owner 5 Nov)"),
    seg("S02", 86.85, 95.30, "Untuk abang-abang yang nak amalkan Shilajit ni, bolehlah cuba Shilajit dalam bentuk tablet macam ni, ya, daripada Aurapep ni, macam ni."),
    seg("S03", 24.35, 32.15, "Korang pernah tak try supplement Shilajit daripada Aurapep ni? Shilajit ni bagus untuk kesihatan badan kita tau, secara menyeluruh.", "'terutama sekali untuk masalah lelaki' (41.8-43.9) dropped"),
    seg("S04", 49.50, 52.80, "Shilajit ni dia tinggi dengan mineral, antioxidant.", "first take (44.4-48.9) and 'boost tenaga dan tingkatkan stamina' (52.9-56) dropped"),
    seg("S05", 101.10, 109.75, "Okey, so Aurapep Shilajit ni siap ada tambahan zinc tau, ada magnesium dan ganoderma extra."),
    seg("S06", 112.75, 116.25, "Kesemua bahan-bahan dalam ni bantu sokong nutrisi harian kita.", "its list of benefits incl. 'kesihatan lelaki' (116.2-124.2) dropped: TikTok risk"),
    seg("S07", 153.50, 155.28, "Ini adalah Aurapep"),
    seg("S07b", 156.90, 158.15, "Shilajit Complex Tablet.", "repeated 'Shilajit' (155.3-156.9) dropped"),
    seg("S08", 159.20, 164.00, "Jadi untuk abang-abang, ayah-ayah, pakcik-pakcik yang tengah cari suplemen,", "first take (128.9-143.6) dropped"),
    seg("S09", 167.98, 173.80, "boleh cuba Aurapep Shilajit Complex Tablet ini. Saya dah sediakan link dekat beg kuning.", "'untuk bantu boost tenaga dan tingkatkan kesihatan lelaki' (164-167.8) dropped: TikTok risk"),
    seg("S10", 183.85, 196.95, "Dan sekarang ni juga banyak seller tengah buat promosi tau, promosi 11.11, biasanya harga lebih murah daripada biasa. Cuba tengok beg kuning, tengok berapa harga dapat. Kalau memang tengah murah tu, boleh beli terus.", "false starts (174.4-183.8) dropped"),
    seg("S11", 214.20, 222.85, "Kalau boleh, jangan beli satu botol tau, beli dua tiga botol, boleh buat stok awal-awal. Nanti kalau stok habis, dah ada lebih dah, tak risau.", "CTA — first take (200.3-208.3) dropped", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Aurapep Shilajit, Drive folder 12AIw3W3… — clip 171623 → #8 (170843 → #7, 172057 → #9). Caption: the 6 Nov default on the wall above the head (top 300). Overlays on every explanation (owner 6 Nov): close-ups of the owner's own bottle / box first; realistic AI photos (no people) for liquid shilajit and the raw mineral rock. Men's-health / stamina / 'kesihatan lelaki' lines dropped (owner 5 Nov: no TikTok-risk health claims).",
     "_note": "Aurapep Shilajit #8 — A-roll assets/a.mp4 = VID_20261106_171623 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Promo 11.11 / 'beli dua tiga botol' are the owner's own words; no price.",
     "segments": segs,
     "punch": [["S11", "beli#2", 1.06]],
     "broll": [cu("C1", ["S02", "start"], ["S02", "end"], 88.0, "58% 60%"),
               cu("C2", ["S05", "start"], ["S06", "end"], 101.1, "60% 60%"),
               cu("C3", ["S07", "start"], ["S07b", "end"], 20.0, "45% 60%", (1.2, 1.3)),
               cu("C4", ["S09", "start"], ["S09", "end"], 168.0, "55% 60%")],
     "photos": [ph("likat", ["S01", "start"], ["S01", "So"], "AI: shilajit cecair likat"),
                ph("batu", ["S04", "start"], ["S04", "end"], "AI: batu mineral shilajit")],
     "theme": {"key": "#C9A227", "brand": "#E9E9E9"},
     "brand_words": ["shilajit", "aurapep"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
