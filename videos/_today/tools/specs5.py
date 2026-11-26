# Robot Vacuum Ecovacs batch (owner, 26 Nov: "Saya nak 15 video minimum dari semua klip ni, setiap video mesti lengkap ada
# hook ada penerangan produk ada CTA. Durasi maksimum 45 saat sahaja. Audio mic kebanyakan direct phone, naikkan kualiti
# audio biar betul betul jelas dalam TikTok"). 26 videos from 31 clips (every clip used, no part in two videos; clip ->
# video table in videos/_eco/tools/mkcombos.sh). Motion: the new "lidar" style (EDL "ld"). Voice: make.enhance_voice.
import re as _re
from pathlib import Path as _P

ECO_PAL = pal("#3FE0FF", bg="rgba(10,20,34,.9)", dark="#06121F", cap="#FFFFFF")
M5 = M
F5 = F
K5 = K


def _eco(n, parts, **kw):
    log = _P(__file__).resolve().parents[2] / f"_eco/.media/combo-e{n:02d}.log"
    m = _re.search(r"total ([\d.]+)", log.read_text()) if log.exists() else None
    d = {"src": f"_eco/.media/combo-e{n:02d}.mp4", "wl": [(f"_eco/.media/wl-combo-e{n:02d}.txt", 0, 1e9)],
         "vad": f"_eco/.media/vad-combo-e{n:02d}.txt", "range": (0.0, float(m.group(1)) if m else 9999.0),
         "srcnote": "VID_20261126 " + parts, "slug": f"ecovacs-t30c-{n}", "name": f"Ecovacs Deebot T30C #{n}",
         "pal": ECO_PAL, "brand": ["ecovacs", "deebot"], "voice": True, "fx": [], "cut": [], "drop": [], "dropnote": "nothing",
         "kp": ("ECOVACS", ["ECOVACS"], S1, ["@", 3.0], 200, 100),
         "keywords": ["mop", "vacuum", "habuk", "bersih", "mantap", "app", "station", "promo", "murah", "kuning", "air"],
         "fix": {"debat": "di beg", "bay": "beg", "backcuni": "beg kuning", "mok": "mop", "d-bot": "Deebot", "d-boat": "Deebot", "puan": "puas"},
         "ld": [], "ai": []}
    d.update(kw)
    return d


SPECS5 = {f"e{n:02d}": _eco(n, "") for n in range(1, 27)}
SPECS.update(SPECS5)
