"""EDL for frame-kaabah-5 (VID_20261108_131730), 8 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb_edl import write

write(P, 5, "VID_20261108_131730", [
    ("S01", 0.00, 5.20, "Korang tengok ni, aku akan buka untuk korang tengok lebih actual dia bila kita", "HOOK"),
    ("S01b", 5.36, 6.05, "buka plastik ni.", "doubled 'buka' (5.2-5.36) dropped", "same"),
    ("S02", 6.05, 9.35, "Korang tengok eh, memang sangat lawa, sangat cantik eh,"),
    ("S03", 13.90, 15.65, "lawa guys, Masya-Allah.", "pause while unwrapping (9.4-13.9) dropped"),
    ("S04", 20.00, 25.00, "Tu dia, memang lawa, okey?", "pause (15.7-20) dropped"),
    ("S05", 27.00, 27.72, "Cuba korang tengok,", "stutter 'dia punya' (28.9-30.2) dropped"),
    ("S05b", 30.20, 36.80, "dia punya design dia sangat jelas, sangat terang, bukan design biasa-biasa tau,"),
    ("S06", 36.74, 47.45, "korang akan nampak lebih terang, tambah-tambah pula bila korang on je lampu LED tu, tengok, Masya-Allah, lawa tak? Memang lawa kan."),
    ("S07", 48.00, 50.35, "Korang beli awal-awal,", "stumble 'sebelum pula' (50.4-52.8) dropped"),
    ("S08", 52.90, 54.48, "bulan puasa pun dah tak lama guys.", "'bulan puasa bulan 2, sekarang bulan 11, 12, 1, dah 2, ok raya pun' (54.5-61) dropped as a stumble"),
    ("S08b", 61.00, 63.98, "Dah bulan 2 dah puasa, raya bulan 3 ni.", "", "same"),
    ("S09", 63.90, 72.00, "Cantik guys, memang cantik. Okay, korang belilah satu untuk rumah, boleh buat hadiah pun boleh, hadiah pun untuk parent, hadiah pun untuk pasangan."),
    ("S10", 73.30, 77.25, "Memang sangat sesuai nak jadikan hadiah pun, sangat sesuai, insya-Allah."),
    ("S11", 77.50, 80.40, "Okay, so dapatkan dia di beg kuning ni, harga dia murah je guys."),
    ("S12", 80.48, 87.60, "Okay, korang beli awal-awal sementara stok masih ada, sementara harga masih murah, korang beli terus. Mantap!", "CTA"),
], cap_top=170, origin="50% 50%",
   extra_note=" Caption set high (top 170) — the frame fills the lower two thirds and the head moves between 15% and 40% height.")
