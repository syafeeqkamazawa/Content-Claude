"""EDL for frame-kaabah-2 (VID_20261108_131000), 8 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb_edl import write

write(P, 2, "VID_20261108_131000", [
    ("S01", 2.10, 7.70, "Masya-Allah, korang tengok ni, frame untuk korang letak dekat dinding, dekat bahagian rumah korang,", "HOOK"),
    ("S02", 7.70, 13.90, "dekat ruang tangga pun boleh, dekat ruang tamu, semua sesuai.", "repeat 'dekat ruang tamu boleh, dekat bahagian tangga boleh' (16.8-20) and the stumble 'korang boleh letak dalam bahagian…' (20.3-25.6) dropped"),
    ("S03", 25.60, 29.10, "Korang boleh gantung dekat mana-mana ruang dalam rumah korang, memang lawa."),
    ("S04", 32.20, 36.85, "Dekat beg kuning bukan design ni sahaja ada tau, korang boleh tengok dekat beg kuning, ada pelbagai design lagi.", "first take (29-31) dropped"),
    ("S05", 36.85, 43.70, "Yang aku pegang ni saiz dia panjang 90 cm, lebar 60 cm. Memang sangat lawa, sangat cantik.", "'naik … apa' (43.7-46.4) dropped"),
    ("S06", 46.40, 49.00, "Bila korang gantung je dekat rumah korang, korang naik seri rumah tau."),
    ("S07", 49.70, 51.20, "Memang cantik korang tengok.", "false start 'dan bukan frame ni' (51.2-52.3) dropped"),
    ("S08", 52.33, 56.62, "Bukan frame macam ni sahaja tau, dia ada lampu LED sekali, bila korang on je lampu,"),
    ("S09", 56.75, 59.25, "dekat tepi ni ada suis tau, korang tengok,", "repeated 'ada suis tau' (59.3-60.8) dropped"),
    ("S10", 60.85, 64.25, "korang on je, makin berkelipan,"),
    ("S11", 65.35, 68.00, "makin berseri korang punya frame Kaabah,", "filler 'okay' (64.4-65.3) and the repeated 'makin berseri' (68-70.6) dropped"),
    ("S11b", 70.60, 75.40, "sebab dia akan ada macam cahaya di sebalik frame ni."),
    ("S12", 75.65, 77.52, "Dan di belakang ni ada hook sekali,", "stumble 'korang jangan, korang hanya perlu apa' (77.5-81.4) dropped"),
    ("S12b", 81.35, 84.70, "sini, kanan dan kiri, dua-dua dah ada."),
    ("S13", 85.75, 87.90, "Lepas tu ada bateri kat sini, korang letak je bateri kat sini."),
    ("S14", 88.95, 92.85, "Memang senang dan cantik guys, memang cantik."),
    ("S15", 92.80, 94.78, "Yang berminat tengok dekat beg kuning,", "'promo' false starts (94.8-101.4) dropped"),
    ("S16", 101.40, 103.25, "seller tengah buat promo guys."),
    ("S17", 103.65, 109.48, "Sekarang ni pun ada promotion 11.11, cuba korang tengok dekat beg kuning, harga pun memang murah."),
    ("S18", 109.50, 115.62, "Kalau korang berminat, korang tengok dekat beg kuning, harga tu kalau tengah murah daripada biasa, korang check out terus.", "CTA"),
], cap_top=1560,
   extra_note=" Caption set at top 1560 (over the legs) — 1380 touched the bottom edge of the frame when he holds it close.")
