"""EDL for infinity-magznate-2 (VID_20261104_144251), 4 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def br(i, f, t, src, note, push=(1.0, 1.06), origin="50% 45%", **kw): return dict({"id": i, "from": f, "to": t, "src": src, "note": note, "push": list(push), "origin": origin}, **kw)


segs = [
    seg("S01", 31.10, 39.15, "Siapa kat sini yang ada masalah susah nak tidur malam, berjaga sampai 2-3 pagi? Kadang-kadang 4 pagi baru dapat tidur.", "HOOK (three false starts 13-27 dropped)"),
    seg("S02", 39.70, 43.25, "Saya boleh cadangkan alternatif, iaitu magnesium Magznate."),
    seg("S03", 48.90, 52.50, "Magnesium ni dia bantu untuk tenangkan kita, relakskan kita.", "second take (first, 43.8, says 'anda')"),
    seg("S04", 52.90, 59.10, "Sesiapa yang ada masalah anxiety, overthinking, stres, tak boleh tidur, insomnia,"),
    seg("S05", 61.80, 64.75, "anda boleh cuba magnesium ni lah."),
    seg("S06", 70.85, 76.50, "Dia membantu dan menyokong diri kita untuk lebih tenang dan lebih relaks.", "first take 65.3 dropped"),
    seg("S07", 105.50, 114.85, "Ubat tidur memang ada, tapi ubat tidur tak boleh dapat dekat TikTok, dekat online ke, pergi farmasi pun tak boleh beli ubat tidur.", "earlier take 77.2 dropped"),
    seg("S08", 124.60, 130.50, "Ataupun kita panggil sebagai ubat penenang.", "'especially ubat penenang (ni)' x2 dropped"),
    seg("S09", 137.00, 143.85, "Ubat tidur ni boleh dapat dengan konsultasi doktor sahaja, ataupun di klinik untuk kes-kes tertentu.", "first take 132.6 dropped"),
    seg("S10", 143.90, 150.30, "Bukan untuk semua orang. Tapi untuk masalah tak boleh tidur secara umumnya,"),
    seg("S11", 161.30, 164.25, "saya sangat recommend anda boleh gunakan magnesium ni.", "'saya sangat cadangkan boleh dapat / saya sangat, saya sangat' stumbles dropped"),
    seg("S12", 169.30, 173.40, "So kalau anda ada masalah tidur, stres, anxiety, overthinking,", "'so kalau, so kalau' stumbles dropped"),
    seg("S13", 175.60, 179.40, "selalu fikir benda yang bukan-bukan, mungkin,"),
    seg("S14", 179.90, 186.10, "saya cadangkan anda boleh dapatkan Magznate ni."),
    seg("S15", 215.80, 218.90, "Sekarang ni kebanyakan seller dah buat promo 11.11 tau.", "'beg kuning kalau ada / kalau saya tengah buat promo' takes 186-213 dropped"),
    seg("S16", 221.30, 224.80, "Cuba tengok dekat beg kuning, kalau harga tengah murah tu, boleh beli terus.", "CTA (first take 219.1 dropped)", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word2",
     "word2": {"top": 1170, "size": 48, "weight": 800, "punct": True}, "mirror": MIRROR,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "4 Nov: Drive folder 1aM-W0W3… 'Infinity Magznate' with 'video rujukan.mp4' (a doctor's talking-head answer about sleeping pills; the owner follows its script). Copied from the reference: a plain talking head, captions one upper-case white word at a time with its comma / full stop, small and centred at ~62 % height with a soft shadow, hard cuts, no photo cutaways. Not copied: the reference's comment-reply bubble (no real comment to answer) — the opening uses the owner's premium motion-text hook instead (28 Oct). Kept the owner's 1 Nov rule: a few product close-ups from his B-roll where he names the product.",
     "_note": "Infinity Magznate #2 — A-roll assets/a.mp4 = VID_20261104_144251. B-roll assets/b.mp4 = VID_20261014_010649 (muted; also used in videos/infinity-magznate: 8 label, 12.5 label, 24.5 pouring, 36 bottle + tablets). No AI photos. 'Promo 11.11' and the ubat tidur / konsultasi doktor lines are the owner's own words.",
     "segments": segs,
     "hook_text": {"kicker": "Infinity Magznate", "lines": ["Susah nak", "tidur malam?"], "accent_words": ["tidur", "malam?"],
                   "to": 3.4, "accent": "#5FC7D4", "accent2": "#A8E2EA", "top": 140},
     "punch": [["S16", "beli", 1.06]],
     "broll": [br("B1", ["S02", "magnesium"], ["S02", "end"], 8.0, "010649: botol Magznate, label", (1.0, 1.08), "50% 40%"),
               br("B2", ["S05", "start"], ["S05", "end"], 36.0, "010649: botol + tablet di tangan (guna produk)"),
               br("B3", ["S11", "gunakan"], ["S11", "end"], 24.5, "010649: tuang tablet (guna produk)"),
               br("B4", ["S14", "dapatkan"], ["S14", "end"], 12.5, "010649: label Magnesium Bisglycinate & Zinc", (1.0, 1.08), "50% 40%")],
     "photos": [],
     "theme": {"key": "#5FC7D4", "brand": "#A8E2EA"},
     "brand_words": ["magznate"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
