"""EDL for frame-kaabah-4 (VID_20261108_131537), 8 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb_edl import write

write(P, 4, "VID_20261108_131537", [
    ("S01", 0.60, 7.92, "Masya-Allah, korang tengok ni, tak sampai 100, 90 pun bukan, 80 pun belum sampai lagi,", "HOOK — price talk is the owner's own words; the unclear '70 jangan …' (8.1-9.2) dropped"),
    ("S02", 9.30, 15.85, "Tengok dekat beg kuning, harga dia memang sangat murah guys, tapi dengan kualiti macam ni, korang tengok, lawa guys."),
    ("S03", 18.00, 21.28, "Sekali alang-alang, kita akan buka plastik dia,", "stumble 'ok, apa saya tunjuk dekat korang' (15.9-17.9) dropped"),
    ("S04", 21.65, 28.92, "korang akan nampak macam mana dia punya bentuk dia, packaging dia sangat kemas. Korang jangan risau, dia punya kotak dia pun sangat kemas.", "end — the rest is 'ok … pause dulu' (29-45)"),
], cap_top=1530, origin="50% 50%",
   extra_note=" Caption set lower (top 1530) — the frame is held low while unboxing; 1380 would cut across it.")
