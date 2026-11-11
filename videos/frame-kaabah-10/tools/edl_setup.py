"""EDL for frame-kaabah-10 (VID_20261111_115325), 11 Nov."""
import pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, cu, ph, kp, write

segs = [
    seg("S01", 62.53, 71.92, "Cuba korang bayangkan ada kita punya adik-beradik ke, saudara-saudara kita ke kan yang baru pindah rumah. Kita nak bagi hadiah, tapi", "HOOK — off-camera chatter (0-61) dropped"),
    seg("S01b", 72.52, 88.93, "asyik-asyik ulang benda sama. Tak cawan, hamper. Tak hamper, benda-benda yang akhirnya tersimpan dalam rumah kita je. Cuba korang tukar kepada frame Kaabah macam ni, memang sangat lawa.", zoom=1.3),
    seg("S02", 104.55, 113.60, "Kalau yang mana suka dekor-dekor Islami tu kan, korang boleh consider untuk berikan hadiah macam frame Kaabah ni, memang sangat cantik."),
    seg("S03", 134.47, 153.34, "Frame Kaabah ni, cetakan dia sangat jelas. Ada Kaabah di belakang dia, ada bangunan-bangunan yang seperti di Mekah. Memang sangat cantik, sesuai nak gantung dekat sudut rumah, dalam bilik ke, dekat sudut solat, ruang tamu, semua sesuai. Memang sangat cantik.", "the stumbling 'lepas tu … di papan gambar … ruang tamu, bilik atau sudut solat' (119.8-133.2) dropped — the same rooms are listed here"),
    seg("S04", 164.74, 174.65, "Yang lagi best tau, ada lampu LED, suis ada kat tepi ni, korang on je, tengok, memang sangat cantik berkelipan macam ni, malam-malam lawa korang."),
    seg("S05", 188.55, 198.91, "Bukan sekadar cantik tau, tapi orang yang terima hadiah ni dia tengok-tengok hati tenang je. Haa, memang sangat menenangkan kita punya jiwa tau."),
    seg("S06", 221.22, 240.73, "Jadi sebelum korang pilih hadiah mana yang korang suka, tengok dekat beg kuning, ada pelbagai design juga dan ada pelbagai size, tengok mana yang sesuai untuk ruang rumah yang korang nak bagi hadiah tu. Dan harga ni tengah ada promotion tau, sementara harga masih murah korang boleh check out.", "CTA"),
]
write(P, 10, "VID_20261111_115325", segs, zoom=1.3, origin="10% 5%",
      broll=[cu("C1", ["S03", "start"], ["S03", "memang"], 140.0, "24% 20%", (1.9, 2.0)),
             cu("C2", ["S04", "start"], ["S04", "end"], 168.0, "24% 20%", (1.9, 2.0))],
      photos=[ph("pindah", ["S01", "baru"], ["S01", "end"], "AI: keluarga pindah rumah (aurat ditutup)"),
              ph("hamper", ["S01b", "tak"], ["S01b", "cuba"], "AI: hamper hadiah (tiada orang)"),
              ph("malam", ["S03", "sudut#2"], ["S03", "ruang"], "AI: sudut solat (tiada orang)")],
      kps=[kp("HADIAH PINDAH RUMAH", ["HADIAH"], ["S01", "hadiah,"], ["S01", "end"], "rise", 230, 100),
           kp("VIBE ISLAMI", ["ISLAMI"], ["S02", "dekor-dekor"], ["S02", "end"], "zoom", 230, 120),
           kp("LAMPU LED", ["LED"], ["S04", "lampu"], ["S04", "end"], "zoom", 230, 120),
           kp("MENENANGKAN JIWA", ["JIWA"], ["S05", "menenangkan"], ["S05", "end"], "split", 230, 104)])
