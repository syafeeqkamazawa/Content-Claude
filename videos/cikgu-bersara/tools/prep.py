"""Cikgu Zaiton binti Mat Isa — retirement tribute (19 Nov 2026, Drive folder "Cikgu bersara").
Owner: "Video untuk cikgu bersara. Susun gambar ikut dari start gambar berkahwin sehingga meningkat tua"; asked
before building: 16:9, the photos fully by year (KISAS -> university -> wedding -> career -> retirement), music =
the audio of "music background.mp4" (its picture is another school's farewell clip, not used).

Builds assets/photos/NN.jpg (1920x1080: the photo fitted over a blurred, darkened copy of itself, soft shadow) and
assets/music.m4a (the song twice, crossfaded, faded out at the end). Facts in the captions come from the biodata
(5_6337059159590053365.docx) and from dates printed on the photos.
"""
import json, pathlib, subprocess
from PIL import Image, ImageFilter, ImageEnhance, ImageChops

P = pathlib.Path(__file__).resolve().parents[1]
W, H = 1920, 1080

# (source file, chapter shown above the caption or "", caption) — chronological
SEQ = [
    ("IMG_0001.jpg", "1990 – 1991", "Kolej Islam Sultan Alam Shah — rakan sekelas yang kelak menjadi teman hidup"),
    ("IMG_0002.jpg", "", "Kenangan zaman belajar"),
    ("IMG_0006.jpg", "1992 – 1995", "Ijazah Sarjana Muda Sastera (Pengajian Islam & Sejarah)"),
    ("IMG_0007.jpg", "", "Bersama sahabat seperjuangan"),
    ("IMG_0009.jpg", "", "Langkah demi langkah menuju cita-cita"),
    ("IMG_0003.jpg", "1996", "Hari graduasi"),
    ("IMG_0018.jpg", "", "Segulung ijazah, sejuta harapan"),
    ("IMG_0028.jpg", "", "Menerima skrol"),
    ("IMG_0004.jpg", "", "Universiti Malaya, 1996"),
    ("IMG_0011.jpg", "", "Kejayaan yang dikongsi bersama keluarga"),
    ("IMG_0026.jpg", "", "Restu keluarga"),
    ("scan.jpg", "24 November 1996", "Hari bahagia bersama Mohamad Rizal bin Long"),
    ("IMG_0005.jpg", "", "Memulakan hidup berdua"),
    ("IMG_0017.jpg", "1997 – 2001", "SMK Perempuan Pudu, Kuala Lumpur — permulaan kerjaya sejak 1 Ogos 1997"),
    ("IMG_0021.jpg", "", "Anak-anak murid pertama"),
    ("IMG_0010.jpg", "", "Ibu kepada anak-anak tercinta"),
    ("IMG_0020.jpg", "2002 – 2009", "SMK Abdul Jalil, Hulu Langat"),
    ("IMG_0024.jpg", "", "Warga guru SMK Abdul Jalil"),
    ("IMG_0022.jpg", "", "SMK Abdul Jalil, 2008"),
    ("IMG_0012.jpg", "", "Keluarga yang dibina dengan kasih sayang — enam cahaya mata"),
    ("IMG_0025.jpg", "2009", "Anugerah Perkhidmatan Cemerlang"),
    ("IMG_0023.jpg", "2010 – 2018", "SMK Bandar Tun Hussein Onn 2 — Kadet Remaja Sekolah, 2014"),
    ("IMG_0013.jpg", "", "Jamuan Akhir Tahun 2016"),
    ("IMG_0016.jpg", "", "Kelas 2 Inovatif, 2017"),
    ("IMG_0019.jpg", "", "Kelab Permainan Tradisional, 2017"),
    ("15.jpg", "2018 – 2026", "SMK Taman Jasmin 2"),
    ("16.jpg", "", "Semangat yang tidak pernah pudar"),
    ("12.jpg", "", "Bersama anak-anak murid"),
    ("IMG_0027.jpg", "2022", "Anugerah Perkhidmatan Cemerlang sekali lagi"),
    ("06.jpg", "", "Syawal di SMK Taman Jasmin 2"),
    ("07.jpg", "", "Rakan sekerja, rakan seperjuangan"),
    ("08.jpg", "", "Senyum yang dirindui"),
    ("04.jpg", "", "Kenangan bersama"),
    ("02.jpg", "", "Gelak tawa di sekolah"),
    ("03.jpg", "", "Sahabat sepanjang jalan"),
    ("05.jpg", "", "Detik-detik terakhir di sekolah"),
    ("09.jpg", "", "Kasih yang ditinggalkan"),
    ("11.jpg", "", "Majlis Persaraan"),
    ("IMG_0014.jpg", "31 Oktober 2026", "Meraikan kejayaan anak"),
    ("13.jpg", "5 November 2026", "Punch card terakhir — 29 tahun 3 bulan 4 hari berkhidmat"),
    ("14.jpg", "", "Terima kasih, Cikgu Zaiton"),
    ("01.jpg", "", "Kini masa untuk keluarga tercinta"),
]

TRIM = {"IMG_0024.jpg": 0.0, "IMG_0028.jpg": 0.0}   # scans with white margins: trim them


def trim_white(im, thr=235):
    g = im.convert("L").point(lambda v: 255 if v < thr else 0)
    box = g.getbbox()
    return im.crop(box) if box else im


def frame(src, out):
    im = Image.open(src).convert("RGB")
    if src.name in TRIM:
        im = trim_white(im)
    # background: cover + blur + darken
    s = max(W / im.width, H / im.height)
    bg = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = ImageEnhance.Brightness(bg.filter(ImageFilter.GaussianBlur(38))).enhance(0.55)
    # foreground: fit inside a margin (leaves room for the caption band)
    mw, mh = W - 260, H - 270
    f = min(mw / im.width, mh / im.height)
    fg = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
    x, y = (W - fg.width) // 2, (H - 215 - fg.height) // 2 + 28
    sh = Image.new("L", (W, H), 0)
    sh.paste(255, (x + 10, y + 16, x + fg.width + 10, y + fg.height + 16))
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    bg = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), bg, sh.point(lambda v: int(v * 0.6)))
    border = Image.new("RGB", (fg.width + 12, fg.height + 12), (246, 240, 228))
    bg.paste(border, (x - 6, y - 6))
    bg.paste(fg, (x, y))
    bg.save(out, quality=92)


def main():
    out = P / "assets/photos"; out.mkdir(parents=True, exist_ok=True)
    for i, (src, *_rest) in enumerate(SEQ):
        frame(P / "src" / src, out / f"{i:02d}.jpg")
    # music: the song (0-73.3 s) twice with a 2.5 s crossfade, then a fade-out — length set by data/timeline.json
    T = json.loads((P / "data/timeline.json").read_text()) if (P / "data/timeline.json").exists() else None
    total = T["total"] if T else 146.0
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(P / "src/music.mp4"), "-i", str(P / "src/music.mp4"), "-filter_complex",
                    "[0:a]atrim=0:73.3,asetpts=PTS-STARTPTS[a];[1:a]atrim=0:73.3,asetpts=PTS-STARTPTS[b];"
                    f"[a][b]acrossfade=d=2.5:c1=tri:c2=tri,apad,atrim=0:{total},afade=t=in:d=0.6,afade=t=out:st={total - 7.5}:d=5,"
                    "volume=-3dB,alimiter=limit=0.9[m]", "-map", "[m]", "-c:a", "aac", "-b:a", "256k", str(P / "assets/music.m4a")], check=True)
    (P / "data/sequence.json").write_text(json.dumps([{"file": f"assets/photos/{i:02d}.jpg", "src": s, "chapter": c, "caption": t}
                                                     for i, (s, c, t) in enumerate(SEQ)], indent=1, ensure_ascii=False))
    print(len(SEQ), "photos")


if __name__ == "__main__":
    main()
