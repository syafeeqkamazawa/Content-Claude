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
    ("CARD", "biodata", ""),
    ("CARD", "didik", ""),
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
    ("CARD", "nikah", ""),
    ("scan.jpg", "24 November 1996", "Hari bahagia bersama Mohamad Rizal bin Long"),
    ("IMG_0005.jpg", "", "Memulakan hidup berdua"),
    ("CARD", "khidmat", ""),
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
    ("CARD", "sumbang", ""),
    ("IMG_0027.jpg", "2022", "Anugerah Perkhidmatan Cemerlang sekali lagi"),
    ("CARD", "anugerah", ""),
    ("06.jpg", "", "Syawal di SMK Taman Jasmin 2"),
    ("07.jpg", "", "Rakan sekerja, rakan seperjuangan"),
    ("08.jpg", "", "Senyum yang dirindui"),
    ("n08.jpg", "", "Taman Puteri Jasmin"),
    ("n02.jpg", "", "Teman sejiwa di SMK Taman Jasmin 2"),
    ("n01.jpg", "", "Duduk bersama, berkongsi cerita"),
    ("n03.jpg", "", "We love TJ2"),
    ("n05.jpg", "", "Keluarga besar warga guru"),
    ("n06.jpg", "", "Jamuan bersama rakan-rakan"),
    ("n07.jpg", "", "Kenangan di meja makan"),
    ("n04.jpg", "", "Tanda kasih seorang sahabat"),
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


# Info cards — text from the owner's biodata (5_6337059159590053365.docx), owner 19 Nov: "Gunakan info dari Microsoft word
# sebagai text overlay". (marker, kicker, title, lines, source photo blurred behind the card)
CARDS = {
    "biodata": ("Biodata", "Zaiton binti Mat Isa", ["Lahir 5 November 1971", "Kg Belat, Pendang, Kedah", "Anak ke-5 daripada 6 adik-beradik"], "IMG_0009.jpg"),
    "didik": ("Latar Belakang Pendidikan", "Perjalanan Ilmu", ["SK Pokok Asam, Kubur Panjang  ·  1978 – 1983", "SMA Raudhatul Ulum, Langgar  ·  1984 – 1985",
              "Maktab Mahmud, Alor Setar  ·  1986 – 1989", "Kolej Islam Sultan Alam Shah (KISAS)  ·  1990 – 1991",
              "Ijazah Sarjana Muda Sastera (Pengajian Islam & Sejarah)  ·  1992 – 1995", "Diploma Pendidikan  ·  1996"], "IMG_0001.jpg"),
    "nikah": ("Keluarga", "24 November 1996", ["Bernikah dengan Mohamad Rizal bin Long", "rakan sekelas di KISAS", "Dikurniakan 6 orang cahaya mata"], "scan.jpg"),
    "khidmat": ("Sejarah Perkhidmatan", "Mula Berkhidmat 1 Ogos 1997", ["SMK Perempuan Pudu, Kuala Lumpur  ·  1997 – 2001", "SMK Abdul Jalil, Hulu Langat  ·  2002 – 2009",
                "SMK Bandar Tun Hussein Onn 2  ·  2010 – Mac 2018", "SMK Taman Jasmin 2  ·  Mac 2018 – November 2026"], "IMG_0021.jpg"),
    "sumbang": ("Sumbangan", "Jurulatih & Hakim", ["Jurulatih Bahas Bahasa Melayu Ala Parlimen, Zon Cheras  ·  2005",
                "Hakim Bahas Ala Parlimen, Zon Cheras  ·  2005 & 2008", "Hakim Pesta Pantun, Zon Cheras  ·  2004",
                "Hakim Bahas Maal Hijrah Peringkat Negeri Selangor  ·  2010",
                "Hakim Tadarus & Mahrajan Al-Quran, Hulu Langat  ·  2012, 2013, 2019 & 2020"], "IMG_0023.jpg"),
    "anugerah": ("Pencapaian", "Anugerah", ["Anugerah Perkhidmatan Cemerlang  ·  2009 & 2022", "Anugerah Kehadiran Terbaik (tanpa MC)  ·  2011, 2016 & 2024",
                 "Anugerah RPH Terbaik  ·  2022"], "IMG_0027.jpg"),
}

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


def card_bg(src, out):
    im = Image.open(src).convert("RGB")
    if src.name in TRIM:
        im = trim_white(im)
    s = max(W / im.width, H / im.height)
    bg = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = ImageEnhance.Brightness(ImageEnhance.Color(bg.filter(ImageFilter.GaussianBlur(26))).enhance(0.6)).enhance(0.38)
    bg.save(out, quality=90)


def main():
    out = P / "assets/photos"; out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("*.jpg"):
        f.unlink()
    seq, n = [], 0
    for src, a, b in SEQ:
        if src == "CARD":
            kick, title, lines, bgsrc = CARDS[a]
            card_bg(P / "src" / bgsrc, out / f"card-{a}.jpg")
            seq.append({"type": "card", "id": a, "file": f"assets/photos/card-{a}.jpg", "kicker": kick, "title": title, "lines": lines})
        else:
            frame(P / "src" / src, out / f"{n:02d}.jpg")
            seq.append({"type": "photo", "file": f"assets/photos/{n:02d}.jpg", "src": src, "chapter": a, "caption": b})
            n += 1
    (P / "data/sequence.json").write_text(json.dumps(seq, indent=1, ensure_ascii=False))
    # owner 19 Nov: the extra clip VID_20261119_123949 goes at the very end; its own sound kept (lifted), music ducked
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(P / "src/end.mp4"), "-filter_complex",
                    "[0:v]split[a][b];[a]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,gblur=sigma=30,eq=brightness=-0.12[bg];"
                    "[b]scale=-2:1080[fg];[bg][fg]overlay=(W-w)/2:0,fps=60,format=yuv420p[v];"
                    "[0:a]highpass=f=80,volume=12dB,alimiter=limit=0.8,afade=t=in:d=0.4,afade=t=out:st=17.2:d=0.7[au]",
                    "-map", "[v]", "-map", "[au]", "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-g", "30",
                    "-c:a", "aac", "-b:a", "192k", str(P / "assets/end.mp4")], check=True)
    # music: the song (0-73.3 s) three times with 2.5 s crossfades, cut to the video length, faded out
    T = json.loads((P / "data/timeline.json").read_text()) if (P / "data/timeline.json").exists() else None
    total = T["total"] if T else 180.0
    vs = T.get("video_start", total - 18) if T else total - 18
    m = str(P / "src/music.mp4")
    loops = 4   # the song is 73.3 s; enough copies for the whole video
    fc = ";".join(f"[{k}:a]atrim=0:73.3,asetpts=PTS-STARTPTS[s{k}]" for k in range(loops))
    prev = "s0"
    for k in range(1, loops):
        fc += f";[{prev}][s{k}]acrossfade=d=2.5:c1=tri:c2=tri[x{k}]"; prev = f"x{k}"
    fc += (f";[{prev}]atrim=0:{total},afade=t=in:d=0.6,"
           f"volume='if(lt(t,{vs}),1,if(lt(t,{vs}+1.5),1-0.78*(t-{vs})/1.5,0.22))':eval=frame,afade=t=out:st={total - 3.5}:d=3,"
           "volume=-3dB,alimiter=limit=0.9[m]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *sum((["-i", m] for _ in range(loops)), []), "-filter_complex", fc,
                    "-map", "[m]", "-c:a", "aac", "-b:a", "256k", str(P / "assets/music.m4a")], check=True)
    print(n, "photos,", len(seq) - n, "info cards")


if __name__ == "__main__":
    main()
