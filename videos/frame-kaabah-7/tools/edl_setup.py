"""EDL for frame-kaabah-7 (VID_20261111_113653), 11 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

segs = [
    seg("S01", 57.06, 58.33, "Tunggu sekejap!", "HOOK — earlier takes (42.6-56.7) and the pre-roll (0-25) dropped"),
    seg("S01b", 58.66, 64.73, "Kalau korang tengok frame Kaabah kan, mesti korang dah ingat frame Kaabah ni frame Kaabah yang biasa-biasa kan."),
    seg("S02", 81.13, 84.54, "Meh aku tunjukkan korang apa specialnya frame Kaabah ni."),
    seg("S03", 84.81, 89.02, "Dekat tepinya dia suis tau, korang on je, korang akan nampak lampu berkelipan."),
    seg("S04", 89.06, 97.79, "Dan kelipan dia tak statik tau, dia bergerak-gerak, sekejap menyala kat sini, sekejap menyala kat sini."),
    seg("S05", 97.86, 100.06, "So bila malam, memang nampak sangat cantik."),
    seg("S06", 139.75, 143.90, "Kalau korang tengok ni, cetakan dia sangat jelas dan terang."),
    seg("S07", 145.06, 159.17, "Dan yang saya pegang ni saiz 90 cm x 60 cm, juga ada pilihan yang lain lah, 60 cm x 40 cm. So boleh tengok mana yang sesuai untuk ruang, untuk ruang rumah korang."),
    seg("S08", 180.13, 191.20, "Yang menariknya, kita boleh dapatkan dua muka beza tau. Satu, nyalaan macam ni, dan juga satu lagi tanpa nyalaan. So ada variasi kat situ."),
    seg("S09", 205.00, 219.33, "Kalau korang suka deko-deko ada vibe Islami macam ni, korang boleh dapatkan dekat beg kuning, ada pelbagai design juga dan pelbagai saiz. Sementara seller tengah buat harga promo ni, korang grab awal-awal ni.", "CTA"),
]
write(P, 7, "VID_20261111_113653", segs, zoom=1.6, origin="100% 37%",
      broll=[cu("C1", ["S03", "start"], ["S05", "end"], 86.5, "87% 54%"),
             cu("C2", ["S06", "start"], ["S06", "end"], 141.0, "87% 54%"),
             cu("C3", ["S08", "satu,"], ["S08", "end"], 185.0, "87% 54%")],
      kps=[kp("TUNGGU SEKEJAP!", ["SEKEJAP!"], ["S01", "start"], ["S01", "end"], "slam", 230, 112),
           kp("LAMPU LED", ["LED"], ["S03", "suis"], ["S04", "end"], "zoom", 230, 120),
           kp("90 x 60 CM", ["90", "60"], ["S07", "saiz"], ["S07", "juga"], "slam", 230, 120),
           kp("60 x 40 CM", ["60", "40"], ["S07", "lah,"], ["S07", "so"], "slam", 230, 120),
           kp("2 VARIASI", ["2"], ["S08", "dua"], ["S08", "end"], "zoom", 230, 120)])
