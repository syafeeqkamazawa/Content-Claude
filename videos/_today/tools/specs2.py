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


FOC = {"tingkalkan": "tingkatkan", "telepon": "telefon", "iboyah": "Ibu ayah", "oya": "ayah", "banda": "Benda", "mass": "Maze", "ujur": "tujuh", "beko": "beg kuning", "adap": "Dapatkan", "-tambah": "", "seluruh": "seller", "pula": "pun", "pada": "ada"}

SPECS2 = {
    "n01": _combo("hoodie", ["141927 12-380"], slug="denim-hoodie-1", name="Hoodie Denim Lelaki #1",
                  pal=pal("#8EC5FF", bg="rgba(14,30,60,.88)", dark="#0E1E3C"), brand=["denim", "hoodie"],
                  keywords=["lawa", "quality", "XL", "lengan", "kemas", "harga", "berbaloi", "raya", "solat", "selesa"],
                  kp=("HOODIE DENIM LELAKI", ["DENIM"], S1, W("style.#1"), 200, 100),
                  drop=[(13.6, 78.0), (160.0, 191.0)],
                  dropnote="whisper noise while he unpacks (source 26-90 s, no speech) and the aside while changing ('wah, henti, sayang ... sorry tau', 172-203 s)",
                  fix={"76cm": "76kg", "sl": "XL", "burah": "murah", "buruk": "borong", "puati": "puas hati", "pering": "spring", "spine": "smart",
                       "terselap": "terselak", "kesiapan": "persiapan", "nama": "memang"},
                  cut=[(W("quality#1"), W("macam#4"), 46.0, "50% 45%", "unfolding the hoodie, fabric close"),
                       (W("tengok#4"), W("aku#4"), 45.0, "50% 45%", "the hoodie held up"),
                       (W("korang#6"), W("ha#1"), 62.0, "50% 45%", "the hoodie, front")],
                  fx=[tags(W("quality#1"), W("macam#4"), [("QUALITY PADU", W("quality#1")), ("BOLEH TARIK, SELESA", W("tarik-tarik#1"))]),
                      hud(W("tinggi#1"), W("black#1"), "SAIZ AKU", "XL", "165 CM  76 KG"),
                      pill(W("kemasan#1"), W("inilah#1"), "KEMASAN LENGAN KEMAS"),
                      pill(W("pelekat#1"), W("ok#9"), "ADA PELEKAT, LEBIH KEMAS"),
                      tags(W("bukan#2"), W("tengok#5"), [("RM100? BUKAN", W("100#1")), ("RM80? BUKAN", W("80#1")), ("RM60? BUKAN", W("60#1")),
                                                         ("RM50? BUKAN", W("50#1")), ("RM40? BELUM TENTU", W("40#1"))]),
                      pill(W("korang#6"), W("ok#12"), "SANGAT BERBALOI"),
                      pill(W("labuh#1"), W("solat#1"), "TAK LABUH, TAK SINGKAT"),
                      pill(W("solat#1"), W("ok#17"), "SOLAT TAK TERSELAK"),
                      pill(W("spring#1"), W("ok#22"), "SELESA, BOLEH TARIK"),
                      promo(W("jangan#1"), "BELI SEBELUM RAYA", "DAPATKAN DI BEG KUNING")]),
    "n02": _combo("perfume", ["145027 8.5-119.5"], slug="perfume-kereta-1", name="Perfume Kereta Gel #1",
                  pal=pal("#FF3B3B", bg="rgba(30,8,8,.88)", dark="#2A0808"), brand=["perfume"],
                  keywords=["woody", "mewah", "gel", "fresh", "citrus", "kayu", "murah", "tiga"],
                  kp=("BAU KERETA MEWAH", ["MEWAH"], S1, W("tau.#1"), 200, 100), drop=[],
                  fix={"cuci": "cecair", "sah": "susah"},
                  cut=[(W("tunjuk#1"), W("Oh,#1"), 16.5, "50% 50%", "the lid off, the gel inside"),
                       (W("Ocean#1"), W("Ha,#2"), 32.0, "50% 45%", "the blue fresh variant"),
                       (W("Ini,#3"), W("Memang,#2"), 48.0, "50% 45%", "the yellow citrus variant"),
                       (W("Sebab,#1"), W("Ok,#5"), 84.0, "50% 45%", "the red can with its box"),
                       (W("Korang#12"), W("Ok,#9"), 98.9, "50% 45%", "all three together")],
                  fx=[tags(W("Perfume#2"), W("Ha#1"), [("BUKAN BAU BUAH", W("bukannya#1")), ("BAU WOODY", W("woody.#1")), ("MACAM KERETA MEWAH", W("mewah#1"))]),
                      pill(W("Dia#2"), W("Oh,#1"), "BENTUK GEL"),
                      pill(W("Ocean#1"), W("Ha,#3"), "FRESH  BAU KERETA BARU"),
                      pill(W("bau#10"), W("Memang,#2"), "CITRUS + KAYU HUTAN"),
                      pill(W("tak#1"), W("Ok.#4"), "TAK KUAT, SELESA"),
                      dial(W("tiga#1"), W("Ok,#9"), 3, "AMBIL 3, LAGI MURAH"),
                      promo(W("Ok,#9"), "HARGA TENGAH MURAH", "CHECK OUT DI BEG KUNING")]),
    "n03": _combo("focus1", ["145505 27.5-104", "150734 20-54 (B-roll)"], slug="amazing-focus-book-1",
                  name="Amazing Focus Training Book #1", pal=pal("#FFC400", bg="rgba(18,18,28,.9)", dark="#14141E"),
                  brand=["amazing", "focus"], keywords=["300", "game", "fokus", "telefon", "10", "tahun", "murah"],
                  kp=("300 GAME FOKUS", ["300"], S1, W("ni.#1"), 200, 100), drop=[], fix=FOC,
                  cut=[(W("Ada#2"), W("Memang#2"), 53.5, "50% 45%", "the two books held up"),
                       (W("Dalam#2"), W("Memang#3"), 30.0, "50% 50%", "flipping the pages"),
                       (W("Untuk#2"), W("Memang#5"), 84.6, "50% 50%", "his daughter working on the book (B-roll)"),
                       (W("Jadi#3"), W("Ok.#2"), 95.0, "50% 50%", "his daughter with the book (B-roll)")],
                  fx=[dial(W("Untuk#1"), W("Saya#1"), 300, "GAME, 2 - 10 TAHUN"),
                      tags(W("Satu,#1"), W("Memang#2"), [("MAZE CHALLENGE", W("Maze#1")), ("COMPREHENSIVE CHALLENGE", W("Comprehensive#1"))]),
                      pill(W("Jadi#1"), W("Memang#5"), "TINGKATKAN FOKUS ANAK"),
                      pill(W("Bantu#2"), W("Ni#4"), "KURANG MASA DENGAN TELEFON"),
                      promo(W("Ibu ayah#1"), "HARGA TENGAH MURAH", "ANAK 2 - 10 TAHUN, BEG KUNING")]),
    "n04": _combo("focus2", ["150734 56-127"], slug="amazing-focus-book-2", name="Amazing Focus Training Book #2",
                  pal=pal("#FFC400", bg="rgba(18,18,28,.9)", dark="#14141E"), brand=["amazing", "focus"],
                  keywords=["game", "fokus", "telefon", "TV", "10", "tahun", "murah", "potongan"],
                  kp=("BUKU MACAM GAME", ["GAME"], S1, W("saja?#1"), 200, 100), drop=[(51.2, 58.5)],
                  dropnote="the retake 'dengar harga dia yang awak kata, so, ibu ayah' (he restarts the price line)", fix=FOC,
                  cut=[(W("Kena#1"), W("Oh,#2"), 30.0, "50% 55%", "the maze page close"),
                       (W("Buku#3"), W("Untuk#2"), 52.5, "50% 55%", "the book cover")],
                  fx=[pill(W("Buku#3"), W("Ok,#1"), "BUKU MACAM GAME, 2 - 10 TAHUN"),
                      tags(W("dia#5"), W("So,#2"), [("TAMBAH FOKUS", W("fokus#1")), ("KURANG TELEFON & TV", W("kurangkan#1"))]),
                      pill(W("dengar#1"), W("Tambah#1"), "HARGA MAMPU MILIK"),
                      promo(W("Sementara#1"), "HARGA MASIH MURAH", "DAPATKAN DI BEG KUNING")]),
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

AI2 = {
    "n01": [("A1", W("berniaga#1"), W("sebab#2"), f"A young Malaysian man at home packing neatly folded dark denim hoodies into parcels for his small online business. {M}"),
            ("A2", W("mana-mana#1"), W("usah#1"), f"A Malaysian man browsing clothing racks in a shopping mall store, looking unimpressed and empty-handed. {M}"),
            ("A3", W("raya#1"), W("benda#1"), f"Nearly empty clothing racks in a Malaysian menswear shop just before Hari Raya, only a few hoodies left, shoppers in the background. {M} {F}")],
    "n02": [("A1", W("Bau#3"), W("tunjuk#1"), f"A Malaysian man relaxing in the driver's seat of a clean luxury car, eyes closed, smiling as he enjoys a pleasant scent, warm evening light. {M}"),
            ("A2", W("bau#7"), W("Ocean#1"), "The spotless interior of a brand new car, fresh clean seats and dashboard, bright daylight, a plain green tree-lined road outside, no flags, no signs. No people."),
            ("A3", W("bau#19"), W("tapi#4"), "Fresh sliced oranges and lemons beside pieces of pine forest wood and green leaves on a wooden table, soft natural light. No people.")],
    "n03": [("A1", W("Bantu#2"), W("Sekarang#2"), f"A Malaysian girl about six years old on a sofa staring at a smartphone, the screen glow on her face, her mother watching worried in the background. {K} {F}"),
            ("A2", W("Ada#4"), W("Jadi#3"), f"A Malaysian boy about five crying in a tantrum on the living-room floor after his tablet was taken away, his mother kneeling calmly beside him. {K} {F}")],
    "n04": [("A1", W("Yang#2"), W("Ok.#2"), f"A Malaysian girl about six lying on a sofa at night staring at a tablet, the screen glow on her face, a dim living room. {K}"),
            ("A2", W("So,#2"), W("Ok,#3"), f"A Malaysian mother and her young daughter laughing together while solving a maze puzzle book at a wooden table, warm afternoon light. {F} {K}")],
}
for _k, _v in AI2.items():
    SPECS[_k]["ai"] = _v
