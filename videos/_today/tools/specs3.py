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


E = ["LAST", "end"]
CTA = lambda: promo(E, "MY FIRST BOOK", "DAPATKAN DI BEG KUNING")
SPECS3 = {
    "fb01": _fb(1, "143318 2-23 + 38.2-42", ("ANAK KEEMPAT SAYA PUN GUNA", ["KEEMPAT"], S1, W("Anak#1"), 200, 100),
                fix={"buah": "Ibu", "seahun": "setahun"}, drop=[(24.15, 25.0)], dropnote="the trailing 'tengok ni' (next sentence)",
                keywords=["tahun", "keempat", "recommended", "kuning"],
                fx=[pill(W("daripada#1"), W("Anak#1"), "1 - 6 TAHUN"), pill(W("Anak#1"), W("Memang#1"), "ANAK KEEMPAT, 1 TAHUN 4 BULAN"),
                    pill(W("Memang#1"), W("so#1"), "MEMANG RECOMMENDED"), CTA()],
                ai=[("A1", W("Anak#1"), W("Memang#1"), f"A Malaysian mother holding her one-year-old toddler on her lap in a bright living room, the toddler seen from behind looking at a colourful picture book. {F} {K} {NOFACE}")]),
    "fb02": _fb(2, "143318 23.8-46.3", ("SELEBRITI PUN GUNA UNTUK ANAK", ["SELEBRITI"], S1, W("Masya#1"), 200, 100),
                fix={"masalah": "MasyaAllah,"}, keywords=["celebrity", "kesan", "baik", "cantik", "proper", "kuning"],
                fx=[pill(W("Masya#1"), W("so#1"), "KESAN SANGAT BAIK"), CTA()],
                ai=[("A1", W("memang#1"), W("so#1"), f"Close-up of a small child's hands pressing a colourful picture on an interactive talking book on a living-room rug, warm light, only the hands visible. {NOFACE}")]),
    "fb03": _fb(3, "143318 51.5-82", ("UNBOXING MY FIRST BOOK", ["UNBOXING"], S1, W("sangat#1"), 200, 100),
                keywords=["lawa", "cantik", "kemas"],
                fx=[pill(W("my#1"), W("so,#2"), "BILAL & NILOFA"), pill(W("cantik#1"), W("ok,#6"), "JOM TENGOK DALAM"), CTA()]),
    "fb04": _fb(4, "143318 104.8-127.2", ("SELLER BAGI WARANTI 1 BULAN", ["WARANTI"], S1, W("importer#1"), 200, 100),
                keywords=["waranti", "importer", "bagus"],
                fx=[tags(W("importer#1"), W("seller#1"), [("IMPORTER NOTICE", W("importer#1")), ("WARANTI 1 BULAN", W("waranti#1"))]),
                    pill(W("seller#1"), W("ada#2"), "SELLER YANG BAGUS"), pill(W("ada#2"), W("MasyaAllah.#1"), "LOGIN & APPLY WARANTI"), CTA()]),
    "fb05": _fb(5, "143318 127.8-146.4", ("SIAP DENGAN PEN & MARKER", ["PEN", "MARKER"], S1, W("dengan#2"), 200, 100),
                keywords=["pen", "marker", "bateri", "packaging", "kemas", "lawa"],
                fx=[tags(W("dengan#2"), W("lepas#1"), [("PEN BERBUNYI", W("dengan#2")), ("MARKER", W("marker#1"))]),
                    pill(W("bateri#1"), W("buku#1"), "ADA BATERI"), pill(W("packaging#1"), W("insyaAllah#1"), "PACKAGING KEMAS & LAWA"), CTA()]),
    "fb06": _fb(6, "143318 146.8-167.2", ("ADA STICKER NAMA SEKALI", ["STICKER"], S1, W("ni#1"), 200, 100),
                fix={"bujuk-bujuk": ""}, keywords=["bunyi", "sticker", "pelekat"],
                fx=[pill(W("ni#1"), W("Nilofa#1"), "SIAP DENGAN STICKER"), pill(W("Buku#1"), E, "BUKU NI MILIK SIAPA?"), CTA()]),
    "fb07": _fb(7, "143318 169.3-190.5 + 229.2-238.4", ("PASANG BATERI & TERUS GUNA", ["BATERI"], S1, W("Rasanya#1"), 200, 100),
                fix={"terpansi": "terpasang"}, keywords=["bateri", "cuba", "tekan", "mula"],
                fx=[pill(W("Gaya#2"), W("Okay#2"), "TARIK, BATERI TERPASANG"), pill(W("Jom#1"), W("Assalamualaikum#1"), "JOM CUBA"),
                    pill(W("Assalamualaikum#1"), W("So,#3"), "BUKU BERSUARA"), pill(W("Tekan#1"), E, "TEKAN UNTUK MULA"), CTA()]),
    "fb08": _fb(8, "143318 255.3-283", ("BELAJAR MENULIS & HIJAIYAH", ["HIJAIYAH"], S1, W("Adik#1"), 200, 100),
                fix={"hija": "hijaiyah", "'iyah": "", "batal": ""}, keywords=["menulis", "hijaiyah"],
                fx=[pill(W("Adik#1"), W("Okey.#1"), "BELAJAR MENULIS"), pill(W("Mari#1"), W("Ba.#1"), "HURUF HIJAIYAH"), CTA()],
                ai=[("A1", W("menulis.#1"), W("Adik#2"), f"Close-up of a small child's hand holding a marker, tracing lines on a glossy wipe-clean activity page, top-down view, only the hand visible. {NOFACE}")]),
    "fb09": _fb(9, "143318 283-300.3", ("WARNA, HAIWAN & EKSPRESI", ["HAIWAN"], S1, W("Oh,#1"), 200, 100),
                fix={"eksperasi": "Ekspresi"}, keywords=["warna", "haiwan", "ekspresi", "islami", "sesuai"],
                fx=[tags(W("Oh,#1"), W("So,#1"), [("BUNYI HAIWAN", W("Oh,#1")), ("EKSPRESI MUKA", W("Ekspresi#1")), ("ANGGOTA BADAN", W("anggota#1")), ("UCAPAN ISLAMI", W("ucapan#1"))]),
                    pill(W("So,#1"), E, "SESUAI SEJAK 1 TAHUN"), CTA()],
                ai=[("A1", W("So,#1"), E, f"A Malaysian father sitting on a living-room rug with his one-year-old toddler on his lap, the toddler seen from behind, both looking at a colourful picture book, warm light. {M} {K} {NOFACE}")]),
    "fb10": _fb(10, "143318 300.5-319.3", ("MEMORI ANAK MULA SIMPAN SEJAK BABY", ["MEMORI"], S1, W("Yelah#1"), 200, 100),
                fix={"tertipat": "tersimpan"}, keywords=["memori", "baby", "penting", "awal", "sesuai"],
                fx=[pill(W("Itu#1"), W("So,#2"), "PENTING DARI AWAL"), pill(W("So,#2"), W("So,#3"), "2 - 3 TAHUN, KELUAR BALIK"), CTA()],
                ai=[("A1", W("Yelah#1"), W("Itu#1"), f"A Malaysian mother gently holding her baby against her shoulder, the baby's face hidden, reading a colourful picture book aloud, warm lamp light. {F} {NOFACE}"),
                    ("A2", W("So,#2"), W("So,#3"), f"A Malaysian toddler seen from behind pointing at pictures in a colourful book on a sofa, sunny living room. {K} {NOFACE}")]),
    "fb11": _fb(11, "143318 319.3-338.2", ("SESUAI 1 HINGGA 6 TAHUN", ["6"], S1, W("Satu#2"), 200, 100),
                fix={"bagi": "beg"}, keywords=["tahun", "sesuai", "berbaloi", "kuning"],
                fx=[pill(W("Satu#2"), W("Memang#1"), "1 - 6 TAHUN"), CTA()],
                ai=[("A1", W("Ibu#1"), W("Satu#2"), f"Three Malaysian siblings of different ages seen from behind, sitting close together on a sofa looking at a colourful book, sunny living room. {K} {NOFACE}")]),
    "fb12": _fb(12, "150449 1.5-32.4 (sound) over 143318 108-126, 162-180", ("NEWBORN HINGGA 6 TAHUN", ["NEWBORN"], S1, W("Ini#1"), 200, 100),
                keywords=["newborn", "recommended", "collab", "tahun"],
                fx=[pill(W("Sangat#1"), W("apa#1"), "SANGAT RECOMMENDED"), pill(W("collab#1"), W("Jadi#1"), "COLLAB MAMI HANA, NILOFA & BILAL"),
                    pill(W("Jadi#1"), E, "0 - 6 TAHUN BOLEH GUNA")],
                ai=[("A1", W("Yang#2"), W("Ini#1"), f"A Malaysian mother cradling her newborn baby wrapped in a soft blanket, the baby's face turned away against her chest, soft morning light. {F} {NOFACE}")]),
    "fb13": _fb(13, "150449 47.6-57.6 + 151316 1.3-10.6 (sound) over 143318 126-146", ("PEN, MARKER & PEMADAM", ["PEMADAM"], S1, W("So#2"), 200, 100),
                keywords=["marker", "pen", "pemadam", "padamkan", "banyak"],
                fx=[pill(W("So#2"), W("Dan#1"), "ADA PEMADAM"), pill(W("Dan#1"), W("boleh#4"), "PADAM & MATCH SEMULA"), pill(W("boleh#4"), E, "GUNA BANYAK KALI"), CTA()],
                ai=[("A1", W("Dan#1"), W("boleh#4"), f"Close-up of a small child's hand wiping marker lines off a glossy wipe-clean activity sheet with a little eraser, only the hand visible. {NOFACE}")]),
    "fb14": _fb(14, "150449 103.15-116.8, 128.45-136.2, 149.8-157.2 (sound) over 143318 176-208", ("CARA GUNA SANGAT SENANG", ["SENANG"], S1, W("Ok,#2"), 200, 100),
                fix={"tepang": ""}, keywords=["senang", "power", "button", "kuasai"],
                fx=[pill(W("Tekan#1"), W("Assalamualaikum.#1"), "TEKAN BUTTON POWER"), pill(W("Assalamualaikum.#1"), W("Ok,#4"), "BUKU TERUS BERSUARA"),
                    pill(W("Mari#1"), W("Ok,#5"), "MENGENAL A, B, C"), pill(W("lima#1"), E, "5 TAHUN, KUASAI A - Z"), CTA()],
                ai=[("A1", W("Ok,#2"), W("Tekan#1"), f"Close-up of a small child's finger pressing a big round button on a colourful children's talking book, only the hand visible. {NOFACE}")]),
    "fb15": _fb(15, "150449 187-195.4, 220-240.6 (sound) over 143318 228-258", ("MENGENAL KENDERAAN", ["KENDERAAN"], S1, W("Ok,#2"), 200, 100),
                fix={"pekan": "Tekan", "manafahan": "Manfaat", "aku": "", "suka": ""}, keywords=["kenderaan", "power", "tahun", "newborn", "sesuai"],
                fx=[pill(W("Kalau#1"), W("Manfaat#1"), "1 TAHUN, 5 TAHUN BOLEH GUNA"), pill(W("Manfaat#1"), W("Kan,#1"), "BUKAN UNTUK SEORANG SAJA"),
                    pill(W("daripada#1"), E, "NEWBORN - 6 TAHUN"), CTA()],
                ai=[("A1", W("Kalau#1"), W("Manfaat#1"), f"A Malaysian mother with a baby and a five-year-old girl, both children seen from behind, gathered around a colourful book on the living-room floor. {F} {K} {NOFACE}")]),
    "fb16": _fb(16, "150449 243.4-248.9, 253.8-264.3, 276.6-281.85 (sound) over 143318 258-288", ("MENGENAL ALIF BA TA", ["ALIF"], S1, W("Nak#1"), 200, 100),
                fix={"abata": "alif-ba-ta", "haris": "Alif", "arna": "Arnab", "beti": "peti", "alih": "alif", "batas": "ba-ta"},
                keywords=["alif-ba-ta", "huruf", "warna"],
                fx=[pill(W("Mari#1"), W("So,#1"), "HURUF HIJAIYAH"), pill(W("Mengenal#1"), E, "MENGENAL WARNA"), CTA()],
                ai=[("A1", W("Nak#1"), W("Mari#1"), f"Close-up of a small child's finger pointing at colourful pictures on a page of a children's learning book, only the hand visible. {NOFACE}")]),
    "fb17": _fb(17, "150449 281.85-300.4 (sound) over 143318 270-296", ("KIRA TAMBAH & TOLAK", ["TAMBAH"], S1, W("Haa,#1"), 200, 100),
                fix={"mau": "", "kiri": "Kira"}, keywords=["tambah", "tolak", "nombor"],
                fx=[pill(W("Haa,#1"), W("So,#1"), "MENGENAL NOMBOR"), pill(W("So,#1"), E, "BELAJAR TAMBAH"), CTA()],
                ai=[("A1", W("Fatima#2"), W("So,#1"), f"Close-up of a small child's hands counting colourful wooden beads on an abacus on a table, only the hands visible, no numbers, no text. {NOFACE}")]),
    "fb18": _fb(18, "150449 301-316.8, 327.4-336 (sound) over 143318 284-300, 186-200", ("HAIWAN, KUIS & LAGU", ["LAGU"], S1, W("Nak#1"), 200, 100),
                drop=[(12.3, 15.8)], dropnote="'ok, ok' while the song plays", keywords=["haiwan", "kuis", "lagu", "islamik"],
                fx=[pill(W("kuis#1"), W("Haa,#1"), "KUIS PADANKAN HAIWAN"), pill(W("lagu#1"), W("ada#6"), "ADA LAGU"), pill(W("ucapan#1"), E, "UCAPAN ISLAMIK"), CTA()],
                ai=[("A1", W("lagu#1"), W("ada#6"), f"A happy Malaysian toddler seen from behind dancing in a bright living room beside a colourful book on the rug. {K} {NOFACE}")]),
    "fb19": _fb(19, "150449 357.7-372.1, 404.3-412.7 (sound) over 143318 290-300, 196-208, 230-240", ("SIFAT ALLAH & 10 MALAIKAT", ["MALAIKAT"], S1, W("Kenal#1"), 200, 100),
                fix={"ma": "Malaikat", "'alaikat": "", "iqa": "Mikail", "'il": "", "jodatan": "biodata"},
                keywords=["sifat", "malaikat", "nabi", "biodata"],
                fx=[pill(W("Kenal#1"), W("Lagi,#1"), "KENAL 10 MALAIKAT"), pill(W("Lagi,#1"), E, "BIODATA NABI MUHAMMAD SAW"), CTA()],
                ai=[("A1", W("Belajar#1"), W("Kenal#1"), f"A Malaysian father in a baju melayu and songkok praying on a prayer mat with his young son beside him, the boy seen from behind, calm living room, soft morning light. {M} {K} {NOFACE}")]),
    "fb20": _fb(20, "150449 413.6-429.1 (sound) over 143318 140-146, 160-172", ("10 MUKJIZAT & RUKUN SOLAT", ["SOLAT"], S1, W("Oh,#1"), 200, 100),
                fix={"mujizat": "mukjizat", "boy": "Ibu", "lah": "ayah", "beko": "beg kuning"}, keywords=["mukjizat", "solat", "terbaik", "berbaloi", "promosi"],
                fx=[pill(W("Oh,#1"), W("Ibu#1"), "SANGAT TERBAIK"), promo(E, "HARGA BERBALOI, MASIH PROMOSI", "BELI DI BEG KUNING")],
                ai=[("A1", W("Ibu#1"), W("Sementara#1"), f"A smiling Malaysian mother placing a wrapped gift box on a table at home, warm afternoon light. {F}")]),
}
SPECS.update(SPECS3)
