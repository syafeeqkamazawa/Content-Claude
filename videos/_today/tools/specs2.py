# Second upload of 21 Nov (folder "Video today", VID_20261121_141927 ... 152300). exec'd at the end of specs.py, so pal(), pill(),
# hud(), dial(), tags(), promo(), W, S1, M, F, K and SPECS are in scope. Each video cuts a virtual source joined by
# videos/_today2/tools/combo.py (":b" parts are B-roll only: their audio is never used as speech). Times = combo seconds.
import re as _re
from pathlib import Path as _P


def _combo(cname, parts, **kw):
    log = _P(__file__).resolve().parents[2] / f"_today2/.media/combo-{cname}.log"
    m = _re.search(r"total ([\d.]+)", log.read_text()) if log.exists() else None
    d = {"src": f"_today2/.media/combo-{cname}.mp4", "wl": [(f"_today2/.media/wl-combo-{cname}.txt", 0, 1e9)],
         "vad": f"_today2/.media/vad-combo-{cname}.txt", "range": (0.0, float(m.group(1)) if m else 9999.0),
         "srcnote": "VID_20261121 " + " + ".join(parts)}
    d.update(kw)
    return d


SPECS2 = {
    "n01": _combo("hoodie", ["141927 12-380"], slug="denim-hoodie-1", name="Hoodie Denim Lelaki #1",
                  pal=pal("#8EC5FF", bg="rgba(14,30,60,.88)", dark="#0E1E3C"), brand=["denim", "hoodie"],
                  keywords=["lawa", "quality", "XL", "lengan", "kemas", "harga", "berbaloi", "raya", "solat", "selesa"],
                  kp=("HOODIE DENIM LELAKI", ["DENIM"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n02": _combo("perfume", ["145027 8.5-119.5"], slug="perfume-kereta-1", name="Perfume Kereta Gel #1",
                  pal=pal("#FF3B3B", bg="rgba(30,8,8,.88)", dark="#2A0808"), brand=["perfume"],
                  keywords=["woody", "mewah", "gel", "fresh", "citrus", "kayu", "murah", "tiga"],
                  kp=("BAU KERETA MEWAH", ["MEWAH"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n03": _combo("focus1", ["145505 27.5-104", "150734 20-54 (B-roll)"], slug="amazing-focus-book-1",
                  name="Amazing Focus Training Book #1", pal=pal("#FFC400", bg="rgba(18,18,28,.9)", dark="#14141E"),
                  brand=["amazing", "focus"], keywords=["300", "game", "fokus", "telefon", "10", "tahun", "murah"],
                  kp=("300 GAME FOKUS", ["300"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n04": _combo("focus2", ["150734 56-127"], slug="amazing-focus-book-2", name="Amazing Focus Training Book #2",
                  pal=pal("#FFC400", bg="rgba(18,18,28,.9)", dark="#14141E"), brand=["amazing", "focus"],
                  keywords=["game", "fokus", "telefon", "TV", "10", "tahun", "murah", "potongan"],
                  kp=("BUKU MACAM GAME", ["GAME"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n05": _combo("focus3", ["151856 272-320.7", "151856 24-250 (B-roll)"], slug="amazing-focus-book-3",
                  name="Amazing Focus Training Book #3", pal=pal("#FFC400", bg="rgba(18,18,28,.9)", dark="#14141E"),
                  brand=["amazing", "focus"], keywords=["bonding", "keluarga", "kualiti", "masa", "promosi", "best"],
                  kp=("BINA BONDING DENGAN ANAK", ["BONDING"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n07": _combo("mfb2", ["150449 0-166"], slug="my-first-book-2", name="My First Book #2",
                  pal=pal("#FF5FB0", bg="rgba(62,15,107,.9)", dark="#3E0F6B"), brand=["my", "first", "book"],
                  keywords=["newborn", "6", "tahun", "pen", "pemadam", "senang", "ABC"],
                  kp=("BUKU BERCAKAP 0-6 TAHUN", ["0-6"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n08": _combo("mfb3", ["150449 166-436.6"], slug="my-first-book-3", name="My First Book #3",
                  pal=pal("#FF5FB0", bg="rgba(62,15,107,.9)", dark="#3E0F6B"), brand=["my", "first", "book"],
                  keywords=["kenderaan", "hijaiyah", "warna", "nombor", "haiwan", "lagu", "malaikat", "solat", "promosi"],
                  kp=("BELAJAR SAMBIL MAIN", ["MAIN"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n06": _combo("mfb1", ["143318 0-340.5", "151316 1.3-10.6", "151016 0-51 (B-roll)", "151316 10.6-154.5 (B-roll)"],
                  slug="my-first-book-1", name="My First Book #1", pal=pal("#FF5FB0", bg="rgba(62,15,107,.9)", dark="#3E0F6B"),
                  brand=["my", "first", "book"], keywords=["tahun", "waranti", "pen", "marker", "hijaiyah", "warna", "memori", "padamkan"],
                  kp=("MY FIRST BOOK", ["FIRST"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
    "n09": _combo("leveled", ["152300 6-192.5"], slug="leveled-reading-book-1", name="Leveled Reading Book #1",
                  pal=pal("#FF8A1F", bg="rgba(15,60,140,.9)", dark="#0F3C8C"), brand=["leveled", "reading"],
                  keywords=["huruf", "perkataan", "ayat", "lagu", "alfabet", "Inggeris", "Melayu", "murah", "promosi"],
                  kp=("ANAK 3 TAHUN KE ATAS", ["3"], S1, ["@", 3.5], 200, 100), drop=[], cut=[], fx=[]),
}
SPECS.update(SPECS2)
