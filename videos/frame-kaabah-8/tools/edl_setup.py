"""EDL for frame-kaabah-8 (VID_20261111_114256), 11 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

segs = [
    seg("S01", 43.53, 49.89, "Antara kesilapan paling biasa bila beli hiasan dinding ni, nampak cantik je, terus check out.", "HOOK — three false starts 'antara kesilapan' (25-42.5) dropped"),
    seg("S02", 55.43, 61.69, "Bila sampai rumah, rupa-rupanya saiz tak ngam dengan ruang yang kita nak letak."),
    seg("S03", 70.76, 88.83, "Untuk frame canvas LED, frame Kaabah ni, seller dah menyatakan dengan jelas. So jangan risau, ada 90 cm x 60 cm yang ada pada saya ni dan juga satu lagi saiz 60 cm x 40 cm."),
    seg("S04", 89.86, 95.33, "Boleh check dulu saiz ruang dengan saiz yang dah dinyatakan dalam beg kuning.", "first take 'contoh kalau nak letak dekat sofa' (108.9-113) dropped"),
    seg("S05", 119.81, 131.81, "Contohnya korang letak dekat atas sofa ke, ataupun dinding tu luas, boleh ukur dulu ruang yang kosong tu, kemudian barulah sesuaikan dengan pilihan yang ada dekat beg kuning tu."),
    seg("S06", 142.79, 150.30, "Dan juga ketebalan frame ni 60 mm, so tebal eh."),
    seg("S07", 161.64, 169.63, "Dan juga frame canvas Kaabah yang korang tengok ni ada lampu LED, sangat lawa, suis ada kat tepi ni."),
    seg("S08", 199.75, 207.23, "Jadi pesanan saya untuk korang kat luar sana, sebelum beli, ukur dinding dulu."),
    seg("S09", 211.40, 213.37, "Tengok variasi design,"),
    seg("S09b", 218.37, 220.93, "kemudian barulah pilih saiz."),
    seg("S10", 227.05, 245.57, "Yang berminat, saya dah letak link dekat beg kuning, boleh pilih design dan saiz kegemaran anda semua, dan seller tengah buat harga promo, sementara harga promo masih ada dan stok juga masih ada, boleh beli di beg kuning.", "CTA — false start 'saya dah letak' (225.9-226.5) dropped"),
]
write(P, 8, "VID_20261111_114256", segs, zoom=1.6, origin="93% 45%",
      broll=[cu("C1", ["S03", "so"], ["S03", "end"], 80.0, "79% 59%"),
             cu("C2", ["S06", "start"], ["S06", "end"], 146.0, "79% 59%", (2.4, 2.55), "close-up of the frame edge (thickness)"),
             cu("C3", ["S07", "start"], ["S07", "end"], 165.0, "79% 59%")],
      photos=[ph("belanja", ["S01", "nampak"], ["S01", "end"], "AI: membeli online (bertudung)"),
              ph("ukur", ["S05", "ukur"], ["S05", "end"], "AI: ukur dinding (berlengan panjang)"),
              ph("ukur", ["S08", "ukur"], ["S08", "end"], "AI: ukur dinding (berlengan panjang)")],
      kps=[kp("SAIZ TAK NGAM?", ["NGAM?"], ["S02", "saiz"], ["S02", "end"], "slam", 230, 112),
           kp("90 x 60 CM", ["90", "60"], ["S03", "90"], ["S03", "dan"], "slam", 230, 120),
           kp("60 x 40 CM", ["60", "40"], ["S03", "saiz"], ["S03", "end"], "slam", 230, 120),
           kp("TEBAL 60 MM", ["60"], ["S06", "ketebalan"], ["S06", "end"], "zoom", 230, 120),
           kp("LAMPU LED", ["LED"], ["S07", "lampu"], ["S07", "end"], "zoom", 230, 120),
           kp("UKUR DINDING DULU", ["UKUR"], ["S08", "ukur"], ["S09b", "end"], "rise", 230, 104)])
