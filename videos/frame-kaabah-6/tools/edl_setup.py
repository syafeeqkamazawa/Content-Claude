"""EDL for frame-kaabah-6 (VID_20261111_113209), 11 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

segs = [
    seg("S01", 16.20, 25.10, "Korang pernah tak, dah susun meja, dah susun sofa, tapi bila tengok dekat ruang tamu ni macam ada yang kurang?", "HOOK"),
    seg("S02", 38.95, 53.65, "Sebenarnya bukan kita perlu tukar semua perabot pun, tetapi kita perlu ada satu benda yang bila orang masuk tu, dia jadi satu benda yang semua orang boleh tengok."),
    seg("S03", 70.55, 71.84, "Cuba korang tengok,", "repeated 'frame Kaabah ni' (71.8-72.9) dropped"),
    seg("S03b", 72.86, 76.50, "frame Kaabah ni, cetakan dia sangat jelas."),
    seg("S04", 76.42, 82.30, "Dan yang part paling best, frame Kaabah ni ada lampu LED tau."),
    seg("S04b", 89.55, 94.60, "Sangat cantik tau, kelipan dia ni bergerak-gerak tau, tak statik.", "unclear muttering (84.2-89.1) dropped"),
    seg("S05", 113.70, 119.15, "Suis dia dekat sini, dekat tepi ni suis dia, lepas tu bateri dia kat belakang ni lah.", "'ok' (119.4-119.8) dropped"),
    seg("S06", 120.85, 129.90, "Dan ada cangkuk kanan dan kiri, dah siap bagi, dah tinggal korang letak tempat untuk gantung sahaja."),
    seg("S07", 144.20, 151.80, "Bila korang on je switch LED ni, bila sebelah malam, korang akan nampak lain sangat, lawa, cantik."),
    seg("S08", 165.40, 180.30, "Yang saya pegang ni 90 cm x 60 cm. Ada juga dekat beg kuning pilihan saiz yang lain iaitu 60 cm x 40 cm. So boleh pilih berdasarkan ruang yang korang nak letak lah."),
    seg("S09", 254.40, 258.90, "Boleh tengok di beg kuning, ada pelbagai design tau dan juga ada pelbagai saiz.", "the messy first take (242.8-252.3) dropped; its 'sementara seller tengah buat harga promo, boleh check out sekarang' repeats the CTA below"),
    seg("S10", 206.85, 225.30, "So kepada korang yang tengah cari hiasan untuk letak di dalam ruang rumah korang ataupun dekat homestay ataupun pejabat, boleh tekan dekat beg kuning sekarang, seller tengah buat harga promo tau, sementara harga masih murah tu boleh check out sekarang.", "CTA (moved after the design/size line)"),
]
write(P, 6, "VID_20261111_113209", segs, zoom=1.6, origin="100% 37%",
      broll=[cu("C1", ["S02", "satu"], ["S02", "end"], 46.0, "100% 48%"),
             cu("C2", ["S03", "start"], ["S03b", "end"], 73.5, "100% 48%"),
             cu("C3", ["S04", "frame"], ["S04b", "end"], 78.5, "100% 48%"),
             cu("C4", ["S05", "start"], ["S05", "end"], 115.5, "100% 45%", (2.6, 2.75), "close-up of the switch / battery side of the frame"),
             cu("C5", ["S06", "start"], ["S06", "end"], 122.5, "100% 50%", (2.2, 2.35), "close-up of the hooks on the back of the frame"),
             cu("C6", ["S07", "start"], ["S07", "end"], 145.0, "100% 48%")],
      photos=[ph("ruangtamu", ["S01", "bila"], ["S01", "end"], "AI: ruang tamu kemas, dinding kosong (tiada orang)")],
      kps=[kp("LAMPU LED", ["LED"], ["S04", "lampu"], ["S04", "end"], "zoom", 230, 120),
           kp("SUIS • BATERI", ["SUIS", "BATERI"], ["S05", "start"], ["S05", "end"], "slide"),
           kp("CANGKUK SIAP", ["CANGKUK"], ["S06", "cangkuk"], ["S06", "end"], "rise"),
           kp("90 x 60 CM", ["90", "60"], ["S08", "90"], ["S08", "ada"], "slam", 230, 120),
           kp("60 x 40 CM", ["60", "40"], ["S08", "iaitu"], ["S08", "so"], "slam", 230, 120)])
