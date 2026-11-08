"""EDL for frame-kaabah-1 (VID_20261108_130736), 8 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb_edl import write

write(P, 1, "VID_20261108_130736", [
    ("S01", 12.20, 17.55, "Masya-Allah, korang tengok ni, memang lawa frame Kaabah untuk korang letak dekat dinding.", "HOOK — unfinished 'frame Kaabah daripada' (2.9-4.7) and the pause after it dropped"),
    ("S02", 17.50, 22.30, "Frame ni bukan frame biasa tau, korang tengok, ada suis kat sini."),
    ("S03", 23.50, 31.56, "Suis ni untuk apa? Sebab nanti bila korang on suis ni, korang akan nampak ada LED, dia akan jadi lebih menyala bila malam."),
    ("S04", 31.56, 36.50, "Korang pasang, korang on kat lampu ni, dia akan nampak lagi macam berkelipan tau."),
    ("S05", 37.45, 43.70, "Ada pelbagai design dekat beg kuning. Korang tengok dekat beg kuning tu, ada design, salah satunya design ni."),
    ("S06", 44.00, 52.90, "Okay, saiz yang aku pegang ni 90 cm x 60 cm. 90 cm panjang, 60 cm lebar. Memang sangat lawa."),
    ("S07", 52.86, 63.68, "Di belakang ni korang jangan risau, dah ada tempat gantung dia, hook kanan dan kiri. Dekat sini korang letak bateri untuk korang on-kan LED."),
    ("S08", 64.30, 66.45, "Tu memang lawa, memang cantik."),
    ("S09", 67.35, 71.78, "Dia punya cetakan jelas, dia punya design ni memang sangat jelas, korang tengok."),
    ("S10", 72.40, 76.30, "Yang berminat tengok dekat beg kuning, seller tengah buat promo ni guys.", "the repeated 'promo 11.11 pun … seller buat' (76.2-86.1) dropped"),
    ("S11", 86.15, 93.42, "Promo 11.11 pun masih berjalan tau. Korang tengok dekat beg kuning, kalau dapat harga murah, korang boleh check out terus.", "CTA"),
], cap_top=1560,
   extra_note=" Caption set at top 1560 (over the legs) — 1380 touched the bottom edge of the frame when he holds it close.")
