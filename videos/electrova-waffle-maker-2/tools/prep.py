"""Electrova Waffle Maker #2 (14 Nov, folder "Footage hari ni") — builds assets/a.mp4 from the owner's single talking +
demo clip VID_20261114_130306 (src/130306.mp4: breakfast hook, the toast plate, cutting the toast, the four plates, donut and
small-ball plates, eating the toast, how to swap the plates, heating top and bottom, the timer, two colours, promo),
complete sentences ~0.5 s apart. assets/b.mp4 = the same clip, muted, for close-up cutaways.
Style (owner 12 Nov): motion overlay text + caption of the Jus Gout 'video contoh', visual overlays, talking kept.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"m": "src/130306.mp4"}
CLIP = {"m": "130306"}
# id, source, [(start, end) speech ranges], text
LINES = [
    ("E1", "m", [(3.49, 10.14), (10.53, 11.87), (12.29, 15.42), (15.81, 17.86), (18.46, 21.79), (22.27, 25.34), (25.76, 27.90)],
     "Abang kakak yang mana selalu sarapan tu kan, contoh sarapan yang biasa dengan nasi lemak ke ataupun roti canai, tapi nak tukar dengan roti bakar ke ataupun waffle, boleh gunakan ni daripada Electrova. Dia ada, boleh buat roti bakar juga, boleh juga buat waffle dan pelbagai acuan tau. Dia bukan acuan yang biasa-biasa, korang tengok."),
    ("E2", "m", [(31.14, 33.22), (33.63, 36.86)], "Ha, ni roti bakar tau. Dia punya tempat acuan dia, acuan untuk roti bakar."),
    ("E3", "m", [(39.17, 40.29), (42.59, 44.19)], "Memang best, memang sedap. Boleh potong siap-siap."),
    ("E4", "m", [(55.46, 58.91), (59.42, 60.42)], "Letak marjerin, letak ..., letak gula, jadi."),
    ("E5", "m", [(60.83, 66.30), (66.75, 69.38), (69.79, 70.62), (71.10, 72.16)], "Dan juga korang bukan boleh buat roti bakar je tau, kat sini korang boleh tukar tau, kat ni kan korang just tukar je. Ada empat jenis. Satu jenis, dua jenis."),
    ("E6", "m", [(73.06, 74.82), (75.20, 76.35), (76.80, 78.05), (78.66, 80.51), (81.47, 85.63), (86.21, 86.91), (89.12, 93.73)],
     "Nak buat donat pun boleh tau. Ha, tadi anak saya buat donat, tepung dia ada lagi, bekas-bekas ni. Ni donat tau. Donat, dan juga ni macam berbola kecil lah. Berbola, ha ni berbola kecil, macam ni. Itu memang sangat best lah, sangat best."),
    ("E7", "m", [(95.20, 97.63)], "Ha, ni pagi-pagi boleh sarapan dengan roti bakar. Bismillahirrahmanirrahim."),
    ("E8", "m", [(109.28, 110.75), (112.51, 113.60)], "Ni cantik, memang sangat cantik, sangat lawa. Lawa tau."),
    ("E10", "m", [(120.10, 122.62), (123.94, 125.44), (126.14, 126.56), (128.13, 128.64), (129.60, 129.95), (130.46, 132.03), (132.51, 133.44)],
     "Ok, lepas tu nak tukar dia, kat sini ada tempat dia, tarik ke atas. Tengok yang ni, ha yang ni juga, bawah ni tarik ke bawah, ni tarik ke belakang. Ok, cabut, cabut."),
    ("E12", "m", [(155.55, 156.06), (157.09, 158.08), (158.69, 160.29), (161.12, 161.47), (161.98, 163.65), (164.64, 165.82), (166.66, 167.10), (168.96, 170.08), (170.56, 171.01), (172.26, 173.28)],
     "Ok, cabut ni kan, ni cabut kan. Ok, contoh dah buat waffle tu, nampak tak, ada macam ni, masuk je tempat tu, tempat letak tu dah ada dah, masuk macam tu, tekan sampai dia bunyi. Ni pun sama, ni pun boleh."),
    ("E13", "m", [(174.08, 176.86), (177.28, 178.11), (178.91, 179.74)], "Ok, kalau nak cabut ni, kalau nak mudah tekan sikit ke dalam baru cabut, baru dia mudah. Ok, cabut."),
    ("E14", "m", [(180.93, 182.46), (182.85, 187.68), (188.10, 189.47), (189.89, 192.10)], "Dan yang best ni, dua-dua pemanas ada tau, atas bawah dia panaskan, bukan bawah sahaja. So lagi cepat lah pembakaran dia."),
    ("E15", "m", [(224.80, 225.70), (226.40, 226.88), (227.42, 229.31), (230.21, 231.49), (232.06, 232.51), (233.47, 234.24), (234.75, 237.09)],
     "Yang lagi best, kat sini boleh setting timer, contohnya nak garing, nak lebih garing, nak lebih crispy, boleh lama kan, pusing tu lebih lama lah."),
    ("E16", "m", [(253.44, 255.39), (255.81, 256.83)], "Dengan ada timer kat sini, so memang sangat function."),
    ("E17", "m", [(261.95, 264.10), (264.64, 267.52), (268.06, 271.10), (271.68, 273.47)],
     "So ada dua kaler abang kak, warna krim macam ni dengan warna merah, saya letak kat beg kuning ni. Macam saya, saya suka garing-garing, so saya lamakan timer dia, so dapatlah garing macam ni."),
    ("E18", "m", [(274.24, 274.78), (275.36, 281.95)], "Jadi abang kak, saya tengah buat harga promo, harga tengah diskaun ni, sementara harga masih murah tu, abang kak boleh dapatkan di beg kuning ni sekarang."),
]
DROPPED = ("130306: the repeated 'potong siap-siap ok' (45-47), the unclear toast-eating murmurs (98-108: 'tengok sikit ... "
           "sekejap'), the first 'warna ada dua jenis' (116-118; said again in full at 262), the unclear plate-heating aside "
           "(134-154: 'letak ni panas sekejap, tepung masak ni ... saya tunjuk'), the silent closing / 'ok ok' / 'tutup' stretch "
           "(192-224), the repeated timer lines (237-253: 'nak lebih garing ataupun cukup-cukup je'), fillers")
# B-roll for the cutaways, concatenated into assets/b.mp4 in this order: (clip, in, out)
BROLL = [("130306", 0.0, 284.3)]

# (line, source time the shot starts or None = line start, clip, clip in, crop)
SHOTS = [(lid, None, CLIP[src], "sync", None) for lid, src, *_ in LINES]
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
    bidx, off, inp, fl = {}, 0.0, [], []
    for k, (clip, a, b) in enumerate(BROLL):
        inp += ["-ss", str(a), "-t", str(b - a), "-i", str(P / f"src/{clip}.mp4")]
        fl.append(f"[{k}:v]scale=1080:1920,setsar=1,fps=60,trim=duration={b - a},setpts=PTS-STARTPTS[v{k}]")
        bidx[clip] = {"offset": round(off, 3), "in": a}
        off += b - a
    fl.append("".join(f"[v{k}]" for k in range(len(BROLL))) + f"concat=n={len(BROLL)}:v=1:a=0[v]")
    run("ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fl), "-map", "[v]", "-c:v", "libx264", "-preset", "fast",
        "-crf", "17", "-pix_fmt", "yuv420p", "-g", "30", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED, "broll": bidx}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
