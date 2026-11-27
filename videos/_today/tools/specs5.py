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


E5 = ["LAST", "end"]
CTA0 = ["-", 5.2]


def H(lines, hi=(), kicker="ECOVACS DEEBOT T30C", to=None, y=150):
    return {"type": "hook", "from": S1, "to": to or ["@", 4.2], "kicker": kicker, "lines": lines, "hi": list(hi), "y": y}


def C(text, f, t, sub=None, y=330, side="right"):
    d = {"type": "chip", "from": W(f), "to": W(t) if isinstance(t, str) else t, "text": text, "y": y, "side": side}
    if sub: d["sub"] = sub
    return d


def CTA(lines=("Dapatkan di", "beg kuning"), sub="Harga promo, sementara masih murah", hi=("kuning",)):
    return {"type": "cta", "from": CTA0, "to": E5, "tag": "BEG KUNING", "lines": list(lines), "hi": list(hi), "sub": sub, "y": 170}


SPECS5 = {
    "e01": _eco(1, "172852 0-29.6 + 172320 (B-roll) + 172852 57-71.2",
                ld=[H(["Belum ada", "robot vacuum?"], ["robot", "vacuum?"]), C("Deebot T30C Max Omni", "robot#3", "Haa,#1"),
                    C("Berat & solid", "berat#1", "dan#1"), CTA()],
                cut=[(W("izinkan#1"), W("ok,#2"), 29.8, "50% 50%", "the T30C box (B-roll)")]),
    "e02": _eco(2, "172852 30-56 + 71.2-86",
                ld=[H(["Jom unboxing", "sama-sama"], ["unboxing"]), C("Product guide & quick setup", "produk#1", "ok,#4"),
                    C("Dokumen & waranti", "dokumen#1", "ok,#7"), C("Semua aksesori ada", "ada#3", "ok,#8"), CTA()]),
    "e03": _eco(3, "172852 126-146.5 + 293-316 + 181833 (B-roll)",
                ld=[H(["Station dia", "besar & lengkap"], ["besar"]), C("Tangki air bersih & kotor", "Tangki#1", "So#1"),
                    C("Tayar boleh panjat", "tayar#1", "dia#5"), C("Radar kesan halangan", "boleh#1", E5), CTA()],
                cut=[(W("So#1"), W("So#2"), 43.4, "50% 50%", "the robot gliding between the chairs (B-roll)")]),
    "e04": _eco(4, "173945 1.5-42.5 + 174023 20-35",
                ld=[H(["Cara set up", "senang je"], ["senang"]), C("Buang semua pelindung", "Satu#1", "Lepas#1"),
                    C("Pasang side brush", "install#1", "So#2"), C("Kanan: air bersih", "sebelah#1", "Dan#1"),
                    C("Kiri: air kotor", "Dan#1", E5, side="left"), CTA()],
                drop=[(18.5, 20.6)], dropnote="two extra 'remove' (said three times)"),
    "e05": _eco(5, "174507 0-30 + 44-56.2",
                ld=[H(["Tip penting", "letak robot"], ["penting"]), C("Dekat Wi-Fi yang kuat", "strong#1", "Okay,#1"),
                    C("Connection lebih stabil", "Okay,#1", "So#3"), C("Air bersih dah isi", "air#1", E5), CTA()],
                drop=[(-1, 2.6)], dropnote="'apa tu, dah dah dah' before he starts"),
    "e06": _eco(6, "174507 56.2-70 + 119-130.2 + s174528 30-60.2",
                ld=[H(["Siap air,", "jom set up app"], ["app"]), C("Station siap", "rumah#1", "Sekarang#1"),
                    C("Download Ecovacs Home", "search#1", "Ambil#1"), C("Pilih region Malaysia", "Ambil#1", E5), CTA()]),
    "e07": _eco(7, "s174528 60.2-117.2 + s175353 3.5-8.5",
                ld=[H(["Daftar app", "dalam 1 minit"], ["1"]), C("Agree & continue", "agree#1", "kita#1"),
                    C("Daftar dengan email", "email#1", "register#2"), C("Scan to connect", "scan#1", "Okey#1"),
                    C("Berjaya!", "berjaya,#1", E5), CTA()],
                drop=[(30.0, 37.2)], dropnote="'saya suruh ni lah, suruh apa, suruh apa tu' (looking for the button)"),
    "e08": _eco(8, "s174528 118.5-147 + 175307 1-36",
                ld=[H(["Connect robot", "ke phone"], ["phone"]), C("Scan QR di robot", "scan#3", "Bila#1"),
                    C("Tekan reset 1 saat", "reset#1", "Macam#1"), C("Sambung network baru", "connect#2", "So,#3"), CTA()]),
    "e09": _eco(9, "s182610 4-53.5",
                ld=[H(["Robot ni", "mapping rumah"], ["mapping"]), C("Start mapping dulu", "Start#1", "So#2"),
                    C("Peta setiap tingkat", "floor-floor#1", E5), CTA()]),
    "e10": _eco(10, "s183350 1-33.2",
                ld=[H(["Peta rumah", "terus dalam app"], ["app"]), C("Tetapkan lokasi station", "letak#1", "So#1"),
                    C("Namakan setiap ruang", "area#1", E5), CTA()]),
    "e11": _eco(11, "s183350 33.2-58.3 + 60-97.6",
                ld=[H(["Namakan", "setiap bilik"], ["bilik"]), C("Living room", "living#1", "Lepas#1"), C("Dapur / kitchen", "dapur.#1", "lepas#2"),
                    C("Bilik belakang", "bilik#1", "Ok,#5"), C("Divide: ruang makan", "divide.#1", E5), CTA()],
                drop=[(31.0, 47.6), (58.0, 59.3)], dropnote="working out the divide button ('kalau nak pilih untuk... macam mana aku nak buat... confirm room, dah') and a second 'macam mana aku buat eh?'"),
    "e12": _eco(12, "s183350 97.6-170",
                ld=[H(["Pilih mod", "ikut ruang"], ["mod"]), C("Dining & living room", "Dining#1", "So.#1"),
                    C("Vacuum + mop serentak", "Mod#1", "Dan#1"), C("Atur aliran air", "Water#1", E5), CTA()],
                drop=[(14.0, 18.0), (27.8, 31.6), (42.9, 45.7), (47.6, 48.8), (58.2, 58.9)],
                dropnote="the first 'room 2 ni adalah' (said again), 'so, ok' fillers, 'kita beli living room... start dengan David ni' and 'kita give back' slips, 'apa?'"),
    "e13": _eco(13, "s183350 170-261.6",
                ld=[H(["Deep cleaning", "2 pusingan"], ["2"]), C("Cleaning passes: 2", "Cleaning#1", "Aku#1"),
                    C("Vacuum & mop serentak", "Serentak.#1", "Ni#1"), C("Basahkan mop dulu", "basahkan#1", E5), CTA()],
                drop=[(15.4, 22.6), (26.6, 36.8), (59.4, 60.7), (63.4, 67.5), (75.4, 78.6), (79.3, 81.1)],
                dropnote="'aku start guys, kita start dengan... stesen' slip, 'ni korang tengok eh', the second 'air bersih dia akan pergilah, dia akan basahkan', 'ok, ok, ok so' fillers, the repeated 'ok so bila aku buat macam tu... aku akan' and 'dia akan dia akan orang kata'"),
    "e14": _eco(14, "175623 0.9-50 + 180354 0.8-4.6 + 175759 / 181734 (B-roll)",
                ld=[H(["Robot ni", "tak langgar barang"], ["tak", "langgar"]), C("Scan ruang dulu", "scan,#1", "So#1"),
                    C("Cari sampah sendiri", "cari#1", "dia#6"), C("Elak halangan", "langgar,#1", "Dia#1"), C("Masuk bawah perabot", "bawah-bawah#1", E5), CTA()],
                cut=[(W("So#1"), W("Ok,#1"), 54.0, "50% 50%", "the robot moving round the room (B-roll)")]),
    "e15": _eco(15, "180033 14-25.2 + 78-110.5 + 222049 1.7-26 + 184518 (B-roll)",
                ld=[H(["Boleh naik", "sejadah!"], ["sejadah!"]), C("Naik ke sejadah", "sejadah#1", "Mantap.#1"),
                    C("Lalu bawah kerusi", "lalu#1", "saya#1"), C("Bersih ikut bilik", "bilik#1", E5), CTA()],
                cut=[(W("Mantap.#1"), W("saya#1"), 72.0, "50% 50%", "the robot sliding under the cabinet (B-roll)")]),
    "e16": _eco(16, "181947 3.8-14.8 + 182026 0-14.8 + 185737 5-17 + 180751 / 182200 (B-roll)",
                ld=[H(["Habis kerja,", "balik sendiri"], ["sendiri"]), C("Auto balik ke station", "balik#1", "guys,#2"),
                    C("Habuk dibuang auto", "habuk#1", "So,#1"), C("Station kosongkan habuk", "buang#1", E5), CTA()],
                cut=[(W("So,#1"), W("guys,#3"), 40.0, "50% 50%", "the station and the robot (B-roll)")]),
    "e17": _eco(17, "184055 0-46.5 + wa0055 (B-roll)",
                ld=[H(["Mop sampai", "ke bucu"], ["bucu"]), C("Pad mop keluar ke tepi", "keluar#1", "Tapi#1"),
                    C("Mop betul-betul", "betul-betul#1", "Ni,#1"), C("Sampai ke bucu", "kebucu#2", "Haa,#2"), CTA()]),
    "e18": _eco(18, "213127 1-28.5 + 51.2-71.2",
                ld=[H(["Tepi dinding", "pun bersih"], ["bersih"]), C("Mop keluar ke tepi", "keluar#1", "memang#1"),
                    C("Mop betul-betul", "mod#3", "Tak,#1"), C("Atur tahap basah di app", "setting#1", "Nampak?#1"), CTA()]),
    "e19": _eco(19, "hn215609 6-38.5 + 123-128.1",
                ld=[H(["Vacuum & mop", "serentak"], ["serentak"]), C("Banyak pilihan mod", "option#1", "Boleh#1"),
                    C("Vacuum dulu, mop kemudian", "vacuum#2", "Boleh#1"), C("Atau serentak", "mop#3", "Memang#1"),
                    {"type": "cta", "from": W("Jadi#1"), "to": E5, "tag": "BEG KUNING", "lines": ["Harga promo", "& payday"], "hi": ["payday"], "sub": "Jangan tunggu lagi", "y": 170}]),
    "e20": _eco(20, "220403 1-30.2 + 84-95.8",
                ld=[H(["Anak kecil", "makan bersepah?"], ["bersepah?"], kicker="IBU AYAH"), C("Habuk & makanan tumpah", "penat#1", "Ok.#3"),
                    C("Ecovacs boleh bantu", "Ecovacs.#1", "Ok.#4"), CTA(("Banyak promo", "sekarang"), "Dapatkan di beg kuning", ("promo",))],
                ai=[("A1", W("penat#1"), W("Ok.#3"), f"A Malaysian toddler in a high chair spilling rice and food onto the tiled floor around the dining table, a tired mother kneeling to wipe it up, warm daylight. {F} {K}")]),
    "e21": _eco(21, "220403 34-66 + 67-84",
                ld=[H(["Nak beli", "robot vacuum?"], ["robot", "vacuum?"], kicker="TIP 1"), C("Pilih yang betul-betul mop", "Beli#1", "Bukan#2"),
                    C("Bukan sekadar lalu", "Bukan#2", "Korang#2"), C("Mop sampai tepi dinding", "tepi-tepi#1", E5), CTA()],
                ai=[("A1", W("Sebab#1"), W("Yang#1"), f"A tired Malaysian woman mopping the living-room floor by hand with a bucket and mop, wiping sweat from her forehead, afternoon light. {F}")]),
    "e22": _eco(22, "hn220921 0.3-45.3 + hn215609 113.9-122.6",
                ld=[H(["Ada anak kecil", "di rumah?"], ["anak", "kecil"], kicker="IBU AYAH"), C("Bersihkan kawasan ditanda", "bersihkan#1", "Ok,#1"),
                    C("Kualiti padu", "kualiti#1", "dia#5"), C("Fungsi tak dinafikan", "fungsi#1", E5), CTA()],
                ai=[("A1", W("yang#2"), W("Apa#1"), f"A happy Malaysian little boy at the dining table with rice and crumbs scattered around his plate and on the floor, his smiling mother beside him. {F} {K}")]),
    "e23": _eco(23, "hn215609 59.7-84 + 222642 0-8.5", voice="strong",
                ld=[H(["Saya guarantee", "puas hati"], ["puas"], kicker="REVIEW JUJUR"), C("Quality & function padu", "quality#1", "Tak#1"),
                    C("Bukan sekadar lalu", "bukan#1", "Memang#3"), C("Meja makan bersih", "meja#1", E5), CTA()]),
    "e24": _eco(24, "222049 26-53.2 + 222642 24.5-47", voice="strong",
                ld=[H(["Dining & kitchen", "dia sapu habis"], ["habis"]), C("Bawah meja makan", "meja#1", "So,#2"),
                    C("Pad mop keluar ke tepi", "keluar#1", "kalau#1"), C("Dinding pun bersih", "dinding,#1", "Baik.#1"), CTA()]),
    "e25": _eco(25, "s221823 30-72.9",
                ld=[H(["Dia cover", "satu rumah"], ["satu", "rumah"]), C("Dining & kitchen", "dining#1", "so#1"),
                    C("Bawah katil pun", "katil#1", "macam#1"), {"type": "cta", "from": W("overall#1"), "to": E5, "tag": "BEG KUNING", "lines": ["Belilah satu,", "memang terbaik"], "hi": ["terbaik"], "sub": "Dapatkan di beg kuning", "y": 170}]),
    "e26": _eco(26, "s221823 1.3-29.1 + 222642 59.5-70",
                ld=[H(["Vacuum & mop", "satu kali jalan"], ["satu"]), C("Peta ruang yang dah dibersih", "tempat#1", "so#1"),
                    {"type": "cta", "from": W("harga#1"), "to": E5, "tag": "BEG KUNING", "lines": ["Harga tengah", "murah"], "hi": ["murah"], "sub": "Banyak promo, payday pun ada", "y": 170}]),
}
SPECS.update(SPECS5)
