"""EDL for frame-kaabah-3 (VID_20261108_131431), 8 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb_edl import write

write(P, 3, "VID_20261108_131431", [
    ("S01", 1.05, 8.25, "Bukan 100, 80 pun bukan, 70 pun jauh sekali, tak sampai 60 guys.", "HOOK — price talk is the owner's own words (heard as 'bukan seratus, lapan puluh pun bukan, tujuh puluh pun jauh sekali, tak sampai 60')"),
    ("S02", 8.25, 11.85, "Korang tengok dekat beg kuning, seller tengah buat promo gila-gila punya,"),
    ("S03", 11.82, 18.44, "dan sekarang ni pun promo 11.11 pun berlangsung lagi tau, cuba tengok dekat beg kuning. Tengok ni,", "stutter 'frame,' (18.4-18.7) dropped"),
    ("S04b", 18.70, 21.72, "frame Kaabah pun ada, frame Ayat Kursi pun ada."),
    ("S05", 21.66, 31.95, "Saiz ada pelbagai saiz, korang tengok, yang aku pegang ni saiz 90 cm x 60 cm, ada juga saiz yang lebih kecil iaitu 60 cm x 40 cm."),
    ("S06", 31.92, 42.55, "Korang boleh tengok, sesuaikan dengan ruang rumah korang. Boleh letak dekat ruang tamu boleh, dekat tangga boleh, dekat ruang keluarga, semua sesuai. Memang cantik, korang tengok."),
    ("S07", 42.54, 48.48, "Dan yang lagi best, frame ni bukan sekadar frame, dia ada lampu LED sekali ni."),
    ("S08", 48.85, 57.20, "Korang tengok, ada suis kat sini, korang pasang je bateri kat belakang ni, dan bila korang on suis, Masya-Allah, korang akan nampak lagi berkelipan."),
    ("S09", 57.70, 62.45, "Korang tengok ni, lawa guys. Tengok tu, Masya-Allah."),
    ("S10", 62.44, 68.45, "Korang beli dekat beg kuning sekarang, sementara stok masih ada, harga masih murah tu, korang beli awal-awal."),
    ("S11", 69.00, 80.15, "Memang cantik. Bulan puasa nanti kalau ada frame ni, lagi menaikkan semangat, lagi naik seri bulan puasa nanti. Raya lagilah bertambah serinya, insya-Allah.", "filler 'okey' (68.5-69) dropped"),
    ("S12", 80.50, 82.78, "Jangan tunggu lagi, dapatkan di beg kuning.", "fillers 'ok so' (80.2-80.5) and 'ok' (82.8-83.2) dropped"),
    ("S12b", 83.25, 87.60, "Sementara promo masih ada, stok masih ada tu, boleh beli sekarang.", "CTA"),
], cap_top=1560,
   extra_note=" Caption set at top 1560 (over the legs) — 1380 touched the bottom edge of the frame when he holds it close.")
