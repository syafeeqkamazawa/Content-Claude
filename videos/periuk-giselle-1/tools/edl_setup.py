"""EDL for periuk-giselle-1 (VID_20261106_090321), 6 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="50% 68%", push=(1.3, 1.45)): return {"id": i, "from": f, "to": t, "src": x, "note": "close-up of the owner's own rice cooker footage", "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}


segs = [
    seg("S01", 52.35, 59.60, "Yang paling saya surprise, periuk nasi ni dia boleh masak sampai dua pot nasi tau.", "HOOK. The opening 'Periuk KA / Khairul Amin … actually tak payah' (0-18) is the owner's own scrapped intro — dropped"),
    seg("S02", 40.00, 47.10, "Family saya, saya, wife, anak saya tiga orang, bawah lapan tahun ke bawah.", "second take of the family line (take 1 at 20.6-24.1 dropped)"),
    seg("S03", 47.60, 51.30, "So, I think I need a rice cooker yang small lah, like this."),
    seg("S04", 24.40, 27.35, "Cukup-cukup memang just nice dengan periuk ni.", "only said in take 1 — kept"),
    seg("S05", 61.45, 66.25, "Dan seller siap bagi sekali pot, so korang tak perlu risau."),
    seg("S06", 75.40, 76.95, "So, kalau time puasa,"),
    seg("S07", 87.65, 92.06, "bila masak nasi tu ngam-ngam lah untuk family kecil saya, dan tak membazir."),
    seg("S07b", 92.06, 97.10, "Sebab selalunya kalau saya guna periuk nasi besar, selalunya mesti ada lebih."),
    seg("S08", 97.25, 106.50, "Yang paling saya suka dia punya colour. Nampak? Colour dia, colour beg Muji macam tu kan. Dan juga ada lagi beberapa pilihan colour yang lain lah dekat beg kuning."),
    seg("S09", 108.15, 114.50, "Dan colour ni actually is my favourite colour, colour green cream macam tu."),
    seg("S10", 120.40, 126.30, "Dan dia juga ada handle tau, nampak? Ada handle, senang nak angkat ke mana-mana."),
    seg("S11", 126.45, 131.48, "Dan rice cooker ni juga guna plug 3 pin, jangan risau."),
    seg("S12", 137.00, 138.80, "Very easy to plug in.", "repeat 'very easy untuk plug' (131.5-135.8) dropped"),
    seg("S13", 139.75, 142.40, "Dan gunakan periuk ni sangat senang."),
    seg("S14", 148.75, 152.05, "Dan juga dia ada bagi sekali dengan senduk nasi."),
    seg("S15", 159.80, 161.98, "Dan juga dia bagi sekali yang ni.", "repeated 'yang ni' dropped"),
    seg("S16", 164.40, 167.15, "Anda boleh letak je ke atas ni macam tu."),
    seg("S17", 168.00, 174.00, "So, nak panaskan lauk, nasi dekat bawah kan, bila nak start masak tu,"),
    seg("S17b", 174.55, 178.40, "beras dah kat bawah, letak je kat atas dan tutup.", "stumble 'nasi' dropped"),
    seg("S18", 180.80, 182.05, "So, senang kan?"),
    seg("S19", 186.50, 194.40, "And last but not least, saya paling suka sebab dia sangatlah jimat ruang. Sebab apa? Sebab dia kecil, just nice macam tu."),
    seg("S20", 195.10, 208.50, "So ibu ayah, abang kakak, acik-macik boleh tengok dekat beg kuning seller sekarang ni, ramai tengah buat promo 11.11 tau. Harga dia mesti turun banyak ni, kan?", "the repeated 'kalau harga tengah murah boleh terus beli' (208.8-211.7) dropped — said again in the CTA"),
    seg("S21", 212.20, 222.75, "Boleh buat hadiah untuk pasangan baru kahwin pun boleh, hadiah untuk ibu, keluarga, pasangan. Okay, sangat-sangat sesuai."),
    seg("S22", 223.40, 228.45, "So jangan tunggu lagi, tengok dekat beg kuning sekarang. Harga tengah murah, boleh beli terus.", "CTA", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 300}, "fs_style": "fade", "mirror": True,
     "tighten": {"max_pause": 0.35, "keep": 0.12, "threshold_db": -45, "blip": 0.03}, "titles": [],
     "_owner_decisions": "6 Nov: Periuk nasi Giselle, Drive folder 1UWCUgtn… (two talking clips → two videos; this is clip 090321). Caption: the 6 Nov default (docs/caption-style-6nov.jpg), moved up to the empty wall above the head (top 300) because at ~72% it would cover the pot and its logo. Overlays on every explanation (owner 6 Nov): close-ups of the owner's own rice-cooker footage first, realistic AI photos (no people except an aurat-safe family) for family, leftover rice, 3-pin plug and gift.",
     "_note": "Periuk Giselle #1 — A-roll assets/a.mp4 = VID_20261106_090321 (front camera, mirrored back in CSS). assets/b.mp4 = the same clip flipped and muted. Clip 091130 goes to periuk-giselle-2. Promo 11.11 is the owner's own words; no price.",
     "segments": segs,
     "punch": [["S22", "jangan", 1.06]],
     "broll": [cu("C1", ["S05", "start"], ["S05", "end"], 61.45, "62% 68%"),
               cu("C2", ["S06", "start"], ["S07", "end"], 76.0, "50% 65%"),
               cu("C3", ["S08", "start"], ["S08", "end"], 97.6, "40% 68%"),
               cu("C4", ["S09", "start"], ["S09", "end"], 108.45, "50% 66%"),
               cu("C5", ["S10", "start"], ["S10", "end"], 120.4, "50% 62%", (1.25, 1.35)),
               cu("C6", ["S13", "start"], ["S14", "end"], 139.75, "55% 72%"),
               cu("C7", ["S15", "start"], ["S16", "end"], 160.0, "40% 70%", (1.2, 1.3)),
               cu("C8", ["S19", "start"], ["S19", "end"], 186.75, "50% 72%")],
     "photos": [ph("keluarga", ["S02", "start"], ["S02", "end"], "AI: keluarga kecil makan nasi (aurat-safe)"),
                ph("lebih", ["S07b", "start"], ["S07b", "end"], "AI: nasi berlebihan dalam periuk besar"),
                ph("plug", ["S11", "start"], ["S12", "end"], "AI: plug 3 pin"),
                ph("hadiah", ["S21", "start"], ["S21", "end"], "AI: hadiah berbalut")],
     "theme": {"key": "#7FB8A4", "brand": "#E9DCC4"},
     "brand_words": ["giselle"], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
