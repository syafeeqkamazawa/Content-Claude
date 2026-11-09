"""EDL for buku-tahajud-2 (VID_20261109_201010 372-630 s), 9 Nov."""
import json, pathlib
P = pathlib.Path(__file__).resolve().parents[1]


def seg(i, x, y, t, note="", zoom=1.0, **kw): return dict({"id": i, "in": x, "out": y, "zoom": zoom, "text": t, "note": note}, **kw)
def cu(i, f, t, x, origin="68% 50%", push=(1.55, 1.65), note="close-up of the book cover the owner holds up (same take)"): return {"id": i, "from": f, "to": t, "src": x, "note": note, "push": list(push), "origin": origin}
def ph(i, f, t, note): return {"id": i, "from": f, "to": t, "note": note}
def kp(text, hi, f, t, anim="rise", top=210, size=118): return {"text": text, "hi": hi, "from": f, "to": t, "anim": anim, "top": top, "size": size}


segs = [
    seg("S01", 35.70, 38.50, "Tahajud ni memang sangat penting sebenarnya.", "HOOK — moved up from the intro"),
    seg("S01b", 39.00, 40.35, "Kenapa penting tahajud?"),
    seg("S02", 8.85, 10.25, "Assalamualaikum warahmatullahi wabarakatuh.", "the tail of the previous product (0-0.7) dropped"),
    seg("S03", 14.00, 17.10, "Tahajud Journey bersama Syafiq, insya-Allah."),
    seg("S04", 17.75, 19.00, "Hari tu saya ada kongsi lah", "repeat 'Tahajud Journey' (17.2-17.7) dropped"),
    seg("S04b", 21.15, 25.25, "beberapa input daripada buku Hidup Dengan Tahajud daripada Iddin Ramli.", "'apa tu' (19.4-21.1) dropped"),
    seg("S05", 25.65, 33.65, "Insya-Allah buku ni memang sangat-sangat membantu kita untuk kita faham, daripada faham, kita rasa nak buat, insya-Allah.", "the repeated intro 'so … baru ni saya dah share … untuk kali kedua ni, err, iaitu Tahajud Journey kedua' (34-57.9; the hook was taken from it) dropped"),
    seg("S06", 57.95, 63.95, "Saya akan sharekan tentang kenapa perlu bangun malam.", "repeat 'so kenapa perlu bangun malam' and the silent book reading (64-145.6) dropped"),
    seg("S07", 145.60, 153.80, "Input yang kedua ni iaitu sebab, kat sini ada mention tujuh tau, tujuh sebab utama untuk saya bertahajud, tujuh sebab utama."),
    seg("S08", 154.00, 155.62, "Saya akan bagi satu dululah.", "'ok so apa dia sebab utama … ada tujuh sebab kat sini … saya bagi yang antaranya' (155.7-168.9) dropped — repeat"),
    seg("S09", 168.95, 172.05, "Antaranya ialah doa-doa akan dikabulkan."),
    seg("S10", 173.40, 176.80, "Banyak lagi sebab-sebab dia, tapi ni antara sebab utama dia.", "repeat 'pentingnya bertahajud doa-doa dikabulkan' (177.9-180.4) dropped"),
    seg("S11", 180.80, 182.00, "So hajat kita yang,"),
    seg("S11b", 185.70, 187.75, "entah bila kan Tuhan nak kabulkan sebenarnya,", "'apa tu' (184.3-185.6) dropped"),
    seg("S11c", 187.90, 188.60, "kita boleh"),
    seg("S11d", 191.90, 201.42, "jadikan tahajud ni sebagai kabel kita, sebagai perantara yang lebih dekat, supaya Allah SWT bantu apa yang kita hajati, insya-Allah.", "'orang kata' (190.4-191.8) dropped; the recap 'ni antara sebab utama dia … doa-doa akan dikabulkan' (201.5-209.7) dropped — repeat"),
    seg("S12", 210.00, 212.10, "Dan sentiasa bersangka baik dengan Allah."),
    seg("S13", 213.30, 221.65, "Even kita dah solat, kadang-kadang belum sampai lagi tu, kita kena bersangka baik dengan Allah. Allah lebih tahu yang terbaik untuk kita kan.", "repeat 'so sentiasa bersangka baik dengan Allah, ok' (222-225.6) dropped"),
    seg("S14", 226.15, 236.30, "Tapi kelebihan dia memang ada, bila kita tahajud ni memang seumpamanya kita dah macam ada shortcut. Ni untuk saya juga, insya-Allah."),
    seg("S15", 240.10, 240.95, "Yang tengok", "'ok so yang tengok, yang tengok' (236.4-240.1) dropped — said three times"),
    seg("S15b", 242.50, 248.55, "perkongsian saya ni daripada buku Hidup Dengan Tahajud daripada Iddin Ramli, boleh sama-sama insya-Allah,", "'apa tu' (241-242.4) dropped"),
    seg("S15c", 249.15, 253.32, "kita niat, kita azam untuk hidup dengan tahajud, insya-Allah."),
    seg("S16", 253.65, 257.95, "Saya akan kongsikan lagi dalam video-video yang akan datang. Yang belum follow saya, boleh follow, insya-Allah.", "end", 1.04),
]
(P / 'data/transcript-a.json').write_text('[]')
e = {"fps": 60, "width": 1080, "height": 1920, "captions": True, "caption_style": "word",
     "word": {"font": "Rubik Mono One", "size": 74, "top": 1600}, "fs_style": "fade", "mirror": False,
     "tighten": {"max_pause": 0.35, "keep": 0.14, "threshold_db": -30, "blip": 0.03}, "titles": [],
     "_owner_decisions": "9 Nov: car talking clip VID_20261109_201010 → one video per product; this is the Hidup Dengan Tahajud (Iddin Ramli) sharing, part 2 (372-630 s). 6 Nov caption set low (top 1600); full-screen realistic photos (night prayer, doa, waking at night, prayer mat); big kinetic key-point text (EDL kp) in the book's purple on the car ceiling; close-ups of the book cover from the moment the owner holds it up; phone mic → tools/voice.sh. Repeats, 'apa tu' fillers and the long silent reading pause cut.",
     "_note": "Buku Hidup Dengan Tahajud #2 — A-roll assets/a.mp4 = VID_20261109_201010 372-630 s (rear camera, not mirrored). assets/b.mp4 = the same clip, muted. 'Tahajud je ni' is heard as the owner's series name and captioned 'Tahajud Journey'. No price / CTA beyond 'follow' — the owner's own words.",
     "segments": segs,
     "kp": [kp("KENAPA PENTING / TAHAJUD?", ["TAHAJUD?"], ["S01b", "start"], ["S01b", "end"], "zoom", 180, 112),
            kp("HIDUP DENGAN TAHAJUD", ["TAHAJUD"], ["S04b", "buku"], ["S04b", "end"], "rise", 200, 104),
            kp("FAHAM → BUAT", ["BUAT"], ["S05", "faham,"], ["S05", "end"], "slide"),
            kp("KENAPA PERLU / BANGUN MALAM?", ["MALAM?"], ["S06", "kenapa"], ["S06", "end"], "slam", 180, 110),
            kp("7 SEBAB UTAMA", ["7"], ["S07", "tujuh#2"], ["S07", "end"], "zoom", 210, 130),
            kp("DOA DIKABULKAN", ["DIKABULKAN"], ["S09", "doa-doa"], ["S10", "end"], "split"),
            kp("PERANTARA / LEBIH DEKAT", ["DEKAT"], ["S11d", "sebagai#2"], ["S11d", "end"], "rise", 190, 112),
            kp("BERSANGKA BAIK / DENGAN ALLAH", ["BAIK"], ["S12", "start"], ["S13", "allah.#1"], "rise", 180, 104),
            kp("SHORTCUT", ["SHORTCUT"], ["S14", "shortcut."], ["S14", "end"], "slam", 210, 150),
            kp("NIAT • AZAM", ["NIAT", "AZAM"], ["S15c", "start"], ["S15c", "end"], "zoom")],
     "punch": [["S16", "yang", 1.06]],
     "broll": [cu("C1", ["S04b", "buku"], ["S04b", "end"], 244.4),
               cu("C2", ["S15b", "start"], ["S15b", "end"], 244.0)],
     "photos": [ph("tahajud", ["S01", "start"], ["S01b", "end"], "AI: solat tahajud (aurat ditutup)"),
                ph("tidur", ["S06", "kenapa"], ["S06", "end"], "AI: bangun malam (aurat ditutup)"),
                ph("doa", ["S09", "start"], ["S10", "end"], "AI: berdoa waktu malam (aurat ditutup)"),
                ph("malam", ["S11d", "start"], ["S11d", "end"], "AI: sejadah waktu malam (tiada orang)"),
                ph("tahajud", ["S14", "start"], ["S14", "ni"], "AI: solat tahajud (aurat ditutup)")],
     "theme": {"key": "#9B7ED1", "brand": "#E9E2F5"},
     "brand_words": [], "keywords": []}
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
print('edl written,', len(segs), 'segments')
