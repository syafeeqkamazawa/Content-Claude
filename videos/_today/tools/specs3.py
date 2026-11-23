# My First Book shorts (owner, 23 Nov: "Buat balik video my first book sebanyak mungkin durasi setiap video bawah 30
# saat. Paling penting kali ni langsung tak nampak wajah anak anak saya"). exec'd at the end of specs.py.
# Picture: only VID_20261121_143318 (the owner alone, unboxing and showing the pages). The clips filmed with his
# children (150449, 151316) give their SOUND only, laid over 143318 close-ups by videos/_today2/tools/dub.py
# (fb12-fb20). AI cutaways never show a child's face (children from behind / hands only). Sources: tools/mkfb.sh.

NOFACE = "No child's face is visible anywhere in the image: any child is seen from behind or only the hands are shown."
FBPAL = pal("#FF5FB0", bg="rgba(62,15,107,.9)", dark="#3E0F6B")
FBB = ["my", "first", "book"]


def _fb(n, src_note, kp, fx=(), ai=(), fix=None, drop=(), dropnote="nothing", keywords=(), cut=()):
    d = _combo(f"fb{n:02d}", [src_note], slug=f"my-first-book-s{n:02d}", name=f"My First Book Short #{n}", pal=FBPAL,
               brand=FBB, keywords=list(keywords), kp=kp, fx=list(fx), drop=list(drop), dropnote=dropnote,
               fix=dict({"bag": "beg", "lofa.": "Nilofa.", "lofa": "Nilofa", "nilo": "Nilofa", "fahadis": "dan",
                         "jilal": "Bilal", "ana": "Hana", "dilofa": "Nilofa", "ubi": "Umi", "maka": "marker", "maka.": "marker.",
                         "makanya": "markernya"}, **(fix or {})),
               cut=list(cut))
    d["ai"] = list(ai)
    return d


SPECS3 = {f"fb{n:02d}": _fb(n, "tmp", ("MY FIRST BOOK", ["FIRST"], S1, ["S1", "end"], 200, 100)) for n in range(1, 21)}
SPECS.update(SPECS3)
