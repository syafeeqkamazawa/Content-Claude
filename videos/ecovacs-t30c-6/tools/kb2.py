"""Shared EDL writer for Frame Kaabah #6-#10 (11 Nov)."""
import json

CAP = {"font": "Rubik Mono One", "size": 62, "top": 1328}   # calibrated to the owner's 11 Nov screenshot (see _owner_decisions)


def seg(i, x, y, t, note="", zoom=None, **kw):
    d = {"id": i, "in": x, "out": y, "text": t, "note": note}
    if zoom is not None:
        d["zoom"] = zoom
    d.update(kw); return d


def cu(i, f, t, x, origin, push=(2.3, 2.45), note="close-up of the Kaabah frame (same take) while the owner explains it"):
    return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}


def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=230, size=104): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


def write(P, n, clip, segs, zoom, origin, broll=(), photos=(), kps=(), note_extra=""):
    for k, s in enumerate(segs):
        s.setdefault("zoom", zoom if k % 2 == 0 else round(zoom * 1.06, 3))
    (P / 'data/transcript-a.json').write_text('[]')
    e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word", "word": dict(CAP),
         "fs_style": "fade", "mirror": False, "zoom_origin": origin,
         "tighten": {"max_pause": 0.6, "keep": 0.25, "threshold_db": -45, "blip": 0.03}, "titles": [],
         "_owner_decisions": "11 Nov: 'Guna caption style sama seperti dalam gambar. Kedudukan caption iaitu jarak caption dengan beg kuning pun mesti sama seperti dalam gambar. Frame Kaabah, semua percakapan yang lengkap mesti jelas, jangan potong terlalu dekat, bagi ada 0.5 saat gap sebelum masuk klip lain. Overlay cukup bahagian penting sahaja untuk bagi mudah faham. Close up produk bila explain tentang function produk.' Caption = the 6 Nov Rubik Mono One word style (the screenshot shows the same style), size/position matched to the screenshot (cap height ~52 px, centred at ~74 % = 1423 px, ~230 px above the yellow-bag label). Segments keep ~0.2 s before and ~0.3 s after the speech and pauses inside a line shrink to 0.5 s (tighten keep 0.25). The clip is a wide living-room shot, so the A-roll is zoomed toward the owner and the frame; close-ups of the frame (same take) whenever he explains a feature." + note_extra,
         "_note": f"Frame Kaabah #{n} — A-roll assets/a.mp4 = {clip} (rear camera, not mirrored; the audio is digital silence between lines). assets/b.mp4 = the same clip, muted. Sizes, LED, switch, battery, hooks and promo are the owner's own words; no price.",
         "segments": segs, "kp": list(kps), "punch": [], "broll": list(broll), "photos": list(photos),
         "theme": {"key": "#D4AF37", "brand": "#FFFFFF"}, "brand_words": ["kaabah"], "keywords": []}
    (P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
    print('edl written,', len(segs), 'segments')
