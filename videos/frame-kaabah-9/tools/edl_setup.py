"""EDL for frame-kaabah-9 (VID_20261111_114809), 11 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

segs = [
    seg("S01", 50.37, 58.11, "Korang yang suka hiasan dinding tapi tak suka wayar berselirat kat belakang, boleh tengok frame Kaabah daripada saya.", "HOOK — pre-roll (0-32) dropped"),
    seg("S02", 76.45, 88.03, "Frame Kaabah ni dah siap dengan suis kat sini, dia dilengkapi dengan suis dan juga bateri dekat belakang ni, bermakna wayar-wayar semua dah ada kat dalam ni, tak berselerak tau."),
    seg("S03", 111.37, 116.41, "Bateri yang digunakan saiz double A tau. So ada tiga yang perlu letak kat dalam ni.", "false start 'bateri' (105.3-106) dropped"),
    seg("S04", 130.09, 142.97, "Dan juga frame ni dah siap ada tempat untuk korang gantung, korang tak perlu pasang dah, extra dah ada siap kat sini, tinggal nak pasang cangkuk sahaja dekat dinding."),
    seg("S05", 148.93, 167.42, "Dan macam yang saya beritahu tadi, dia ada suis dan bateri untuk apa? Untuk nyalaan LED macam ni, insya-Allah cantik kan? Dan kelipan dia, kelipan yang tak statik, dia berkelip sebelah kanan, sekejap berkelip sebelah kiri. Kalau malam-malam memang nampak sangat cantik."),
    seg("S06", 191.24, 205.92, "Dan juga korang jangan risau, belian korang untuk frame Kaabah ni dah siap juga bersama dengan tiga paku untuk korang letak dekat dinding, dan boleh terus gantungkan frame Kaabah ni."),
    seg("S07", 227.01, 252.99, "Jadi kepada korang yang nak pasang frame Kaabah ni dekat ruang dinding korang, ruang tamu ke, bilik solat ke, ataupun di mana-mana ruang yang rasa sesuai, boleh tengok dekat beg kuning, ada pelbagai design dan saiz juga, harga tengah murah, sementara harga masih murah dan stok pun masih ada, boleh terus beli di beg kuning sekarang.", "CTA"),
]
write(P, 9, "VID_20261111_114809", segs, zoom=1.5, origin="35% 35%",
      broll=[cu("C1", ["S02", "start"], ["S02", "bermakna"], 78.0, "32% 37%"),
             cu("C2", ["S04", "start"], ["S04", "end"], 135.0, "32% 37%", (2.0, 2.15), "close-up of the hanging points on the back of the frame"),
             cu("C3", ["S05", "untuk#2"], ["S05", "end"], 156.0, "32% 37%")],
      photos=[ph("wayar", ["S01", "tak"], ["S01", "boleh"], "AI: wayar berselirat (tiada orang)"),
              ph("bateri", ["S03", "start"], ["S03", "end"], "AI: bateri AA (tiada orang)"),
              ph("paku", ["S06", "tiga"], ["S06", "end"], "AI: tiga paku dinding (tiada orang)"),
              ph("malam", ["S07", "bilik"], ["S07", "ataupun"], "AI: sudut solat (tiada orang)")],
      kps=[kp("TAK ADA WAYAR", ["WAYAR"], ["S02", "bermakna"], ["S02", "end"], "slam", 230, 112),
           kp("BATERI AA x3", ["AA", "x3"], ["S03", "start"], ["S03", "end"], "zoom", 230, 120),
           kp("SIAP TEMPAT GANTUNG", ["GANTUNG"], ["S04", "siap"], ["S04", "end"], "rise", 230, 100),
           kp("LAMPU LED", ["LED"], ["S05", "LED"], ["S05", "dan#2"], "zoom", 230, 120),
           kp("SIAP 3 PAKU", ["3"], ["S06", "tiga"], ["S06", "end"], "slam", 230, 120)])
