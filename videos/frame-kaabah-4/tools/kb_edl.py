"""Shared EDL writer for the Frame Kaabah batch (8 Nov): no overlays, captions only, alternating zoom on cuts."""
import json


def write(P, n, clip, segs_raw, cap_top=1380, origin="45% 42%", zooms=(1.0, 1.1), extra_note=""):
    segs = []
    k = 0
    for s in segs_raw:
        i, x, y, t = s[:4]
        note = s[4] if len(s) > 4 else ""
        same = len(s) > 5 and s[5] == "same"  # continues the previous segment mid-sentence: keep its zoom
        if not same and segs:
            k += 1
        segs.append({"id": i, "in": x, "out": y, "zoom": zooms[k % 2], "text": t, "note": note})
    (P / 'data/transcript-a.json').write_text('[]')
    e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
         "word": {"font": "Rubik Mono One", "size": 74, "top": cap_top}, "fs_style": "fade", "mirror": False,
         "zoom_origin": origin,
         "tighten": {"max_pause": 0.4, "keep": 0.16, "threshold_db": -45, "blip": 0.03}, "titles": [],
         "_owner_decisions": "8 Nov: 'Ada 5 video frame Kaabah. Jangan buat overlay untuk video ni, pastikan potong percakapan sangkut sangkut dan berulang. Bagi video nampak smooth dan setiap perkataan disebut dengan jelas sebelum pergi klip seterusnya' — Drive folder 'Frame Kaabah' (1hILJi_e…), 5 clips → 5 videos. No overlays (no B-roll, photos, labels or hook text) — only the 6 Nov default caption. Stumbles, repeats and fillers cut; every cut lands after the word has finished (tighten keep 0.16 s, joins checked by ear-transcript). Zoom alternates 100% / 110% between segments so the jump cuts read as camera changes." + extra_note,
         "_note": f"Frame Kaabah #{n} — A-roll assets/a.mp4 = {clip} (rear camera, not mirrored). Sizes, LED, hooks, battery, prices and promo 11.11 are the owner's own words.",
         "segments": segs, "punch": [], "broll": [], "photos": [],
         "theme": {"key": "#D4AF37", "brand": "#FFFFFF"}, "brand_words": ["kaabah"], "keywords": []}
    (P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
    print('edl written,', len(segs), 'segments')
