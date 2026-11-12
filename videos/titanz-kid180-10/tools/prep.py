"""Titanz Kid180 #10 (12 Nov) — builds assets/a.mp4 (the owner's talking clip VID_20261112_151248, cut to
complete sentences ~0.5 s apart; stumbles, 'okay's and the off-camera part with his children left out) and
assets/b.mp4 (B-roll for the cut-aways: VID_20260908_140338 bottle + tablets at 0-43.67 s, then
VID_20260827_170307 his children taking the tablets from 43.67 s).
Style (owner 12 Nov): the motion overlay text and the caption of the Jus Gout 'video contoh', plus visual
overlays ("Overlay visual juga masih diperlukan"); the talking video stays.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"clip": "src/a151248.mp4"}
# id, source, [(start, end) speech ranges], text
LINES = [
    ("K1", "clip", [(30.82, 35.78)], "Kalau korang tengah cari suplemen untuk anak-anak, jangan tengok je nama atau harga je tau."),
    ("K2", "clip", [(36.45, 41.54)], "Ada 3 benda penting yang ibu ayah kena tahu dulu sebelum beli suplemen."),
    ("K3", "clip", [(42.24, 45.18)], "Pertama, kenapa kalsium penting untuk anak?"),
    ("K4", "clip", [(46.08, 54.75)], "Anak-anak ni tengah membesar tau, jadi badan mereka perlukan kalsium yang mencukupi untuk membantu pembentukan tulang dan gigi yang kuat."),
    ("K5", "clip", [(71.81, 77.44)], "Sebab tu, kita kena pastikan pemakanan harian anak-anak cukup nutrisinya termasuk kalsium."),
    ("K6", "clip", [(78.30, 78.82), (79.42, 82.18)], "Kedua, apa yang menarik tentang Titanz Kid180 ni,"),
    ("K7", "clip", [(82.78, 86.05)], "produk ni merupakan tablet kunyah yang mengandungi kalsium."),
    ("K8", "clip", [(86.69, 94.72)], "Pada kotak dia juga ada nyatakan ada beri biru, teh hijau dan vitamin C. Jadi bukan sekadar kalsium sahaja tau."),
    ("K9", "clip", [(98.98, 108.45)], "Lagi satu, bentuk dia tablet kunyah, tak perlu telan macam kapsul biasa. Untuk anak yang susah nak telan tablet tu, bentuk macam ni mungkin lebih mudah."),
    ("K10", "clip", [(110.34, 115.62)], "So, macam ni bentuk dia, boleh dikunyah. Memang sangat sedap lah."),
    ("K11", "clip", [(116.70, 119.90), (120.88, 121.70)], "Anak-anak saya pun memang sangat menyukai tablet ni. Alhamdulillah."),
    ("K12", "clip", [(157.45, 161.84), (162.30, 162.80), (163.50, 164.70)], "So, tablet dia memang macam anak-anak kita makan candy lah. Sedap. Rasa beri-beri macam tu."),
    ("K13", "clip", [(166.36, 168.32), (168.86, 169.22), (170.00, 171.70)], "Ketiga, sesuai tak untuk anak kita? Sesuai lah, macam saya tadi, saya baru je bagi ke anak saya."),
    ("K14", "clip", [(172.70, 176.98), (179.48, 181.12), (185.44, 187.36)], "Yang ni penting tau sebab sebelum beli, semak dulu umur yang disyorkan, sukatan dia kena ambil banyak-banyak, kandungan penuh pada label botol ni."),
    ("K15", "clip", [(188.74, 190.20), (192.36, 193.66), (194.72, 201.26), (201.86, 202.76)], "Dalam botol ni dinyatakan lah energinya berapa, karbohidrat, total sugar, fat, lemak, protein. Ada sodium, natrium, vitamin C, kalsium dan vitamin K. Complete insyaAllah."),
    ("K16", "clip", [(203.76, 205.80)], "So, bantu seimbangkan nutrisi anak kita."),
    ("K17", "clip", [(209.84, 210.52), (211.44, 222.48)], "Sebab penting kita cek juga sebab keperluan setiap anak ni tak semestinya sama. Kena ingat, suplemen ni bukan pengganti makanan seimbang, dia bantu lengkapkan pengambilan nutrisi bila diperlukan."),
    ("K18", "clip", [(222.62, 239.07)], "Sebab kita sedia maklum, anak-anak kita ni memang masalah bila nak makan sayur, nak makan benda-benda yang berkhasiat ni, memang mencabar sikit. Jadi, inilah antara option alternatif yang kita boleh ambil insyaAllah."),
    ("K19", "clip", [(240.70, 247.07)], "Jadi, kalau korang tengah survey suplemen kalsium untuk anak, boleh pertimbangkan Titanz Kid180 tablet ni."),
    ("K20", "clip", [(255.22, 262.76)], "Saya dah letak dekat beg kuning. Sementara seller tengah buat harga promo, boleh dapatkan awal-awal sebelum harga naik."),
]
DROPPED = ("'kalau ana…' (12.2); 'sebab tu kita' false start (70.3); the 'okay's and 'haa's between pieces; 123-155 "
           "(off camera with his children: 'Fatima', 'vitamin', 'bismillah'…); 'sukatan ambil apa?' and the first 'kandungan "
           "penuh pada tablet ni' (said again right after); CTA take 1 (247.8-249.1) and 'selamat menikmati' hallucination")

# (line, source time the shot starts or None = line start, clip, clip in, crop)
SHOTS = [(lid, None, "a151248", "sync", None) for lid, *_ in LINES]
VF = {None: "scale=1080:1920,setsar=1"}


def run(*a): subprocess.run(a, check=True)


def layout():
    t, out = 0.0, {}
    for lid, src, rng, txt in LINES:
        pieces = []
        for k, (a, b) in enumerate(rng):
            s0 = a - (PRE if k == 0 else GAP_IN)
            s1 = b + (POST if k == len(rng) - 1 else GAP_IN)
            pieces.append((round(s0, 3), round(s1, 3)))
        dur = sum(b - a for a, b in pieces)
        out[lid] = dict(src=src, pieces=pieces, e0=round(t, 3), e1=round(t + dur, 3), text=txt)
        t += dur
    return out, round(t, 3)


def e_of(L, lid, s):
    """source time inside line lid -> edit time"""
    acc = L[lid]["e0"]
    for a, b in L[lid]["pieces"]:
        if s <= b:
            return round(acc + max(0.0, s - a), 3)
        acc += b - a
    return round(acc, 3)


def main():
    L, TOTAL = layout()
    tmp = P / ".media/prep"; tmp.mkdir(parents=True, exist_ok=True)
    gain = {}
    for src, inp in SRC.items():
        rng = [p for d in L.values() if d["src"] == src for p in d["pieces"]]
        sel = "+".join(f"between(t,{a},{b})" for a, b in rng)
        r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(P / inp), "-vn", "-af",
                            f"aselect='{sel}',asetpts=N/SR/TB,highpass=f=75,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,"
                            "loudnorm=I=-15:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
        js = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
        gain[src] = round(-13.3 - float(js["input_i"]), 2)
    print("gain", gain)
    idx = {k: i for i, k in enumerate(SRC)}
    flt, parts, n = [], [], 0
    for lid, d in L.items():
        for a, b in d["pieces"]:
            dur = b - a
            flt.append(f"[{idx[d['src']]}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=mono,"
                       f"highpass=f=75,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,volume={gain[d['src']]}dB,"
                       f"afade=t=in:d=0.03,afade=t=out:st={dur-0.05:.3f}:d=0.05[p{n}]")
            parts.append(f"[p{n}]"); n += 1
    flt.append("".join(parts) + f"concat=n={n}:v=0:a=1,alimiter=limit=0.89:level=false[a]")
    args = []
    for inp in SRC.values():
        args += ["-i", str(P / inp)]
    run("ffmpeg", "-v", "error", "-y", *args, "-filter_complex", ";".join(flt), "-map", "[a]", "-ar", "48000", "-ac", "2",
        "-c:a", "pcm_s16le", str(tmp / "voice.wav"))
    # picture: synced shots follow the line's own pieces; others play straight
    segs = []
    for k, (lid, t, clip, cin, crop) in enumerate(SHOTS):
        a = L[lid]["e0"] if t is None else e_of(L, lid, t)
        b = (L[SHOTS[k + 1][0]]["e0"] if SHOTS[k + 1][1] is None else e_of(L, SHOTS[k + 1][0], SHOTS[k + 1][1])) if k + 1 < len(SHOTS) else TOTAL
        if cin == "sync":
            for pa, pb in L[lid]["pieces"]:
                segs.append((clip, pa, round(pb - pa, 3), crop))
        else:
            segs.append((clip, cin, round(b - a, 3), crop))
        print(f"{a:7.2f}-{b:7.2f}  {lid} {clip} @{cin}")
    lst = []
    for k, (clip, cin, dur, crop) in enumerate(segs):
        out = tmp / f"s{k:02d}.mp4"
        run("ffmpeg", "-v", "error", "-y", "-ss", str(cin), "-t", str(round(dur + 0.1, 3)), "-i", str(P / f"src/{clip}.mp4"),
            "-vf", f"{VF[crop]},fps=60,trim=duration={dur}", "-an",
            "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", str(out))
        lst.append(f"file '{out}'")
    (tmp / "list.txt").write_text("\n".join(lst) + "\n")
    run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-i", str(tmp / "voice.wav"),
        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-r", "60", "-g", "30",
        "-c:a", "aac", "-b:a", "192k", str(P / "assets/a.mp4"))
    # B-roll for the cut-aways: bottle + tablets, then his children taking them
    run("ffmpeg", "-v", "error", "-y", "-i", str(P / "src/b140338.mp4"), "-i", str(P / "src/b170307.mp4"), "-filter_complex",
        "[0:v]scale=1080:1920,setsar=1,fps=60[a];[1:v]scale=1080:1920,setsar=1,fps=60[b];[a][b]concat=n=2:v=1:a=0[v]",
        "-map", "[v]", "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-pix_fmt", "yuv420p", "-g", "30", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
