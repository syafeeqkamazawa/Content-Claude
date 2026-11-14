"""Lab Biotix Triple Biotix #2 (14 Nov, same folder, new files) — voiceover video.
Sound = the owner's voice recording Recorder 20261114-1105.m4a, denoised and cleaned with the tools/voice.sh chain.
Picture = VID_20261114_100411 (owner at the table: the box, the sachet, tearing it, squeezing the jelly into his mouth;
no speech on it) and VID_20261114_110857 (box and sachets on the grass), cut to follow the words. assets/b.mp4 = both
clips back to back, muted, for cutaways (offsets in data/timeline.json). Complete sentences ~0.5 s apart; the
false starts and the repeated hook take dropped.
Style (owner 12 Nov): motion overlay text + plain one-word caption of the Jus Gout 'video contoh', visual overlays.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"v": "src/rec1105.m4a"}
NOISE = {"v": (27.2, 28.4)}   # quiet stretch for the denoise profile
CLIPS = ["100411", "110857"]   # assets/b.mp4 order
# id, source, [(start, end) speech ranges], text
LINES = [
    ("H1", "v", [(2.27, 9.31)], "Siapa dekat sini yang selalu perut kembung tu, banyak angin, rasa penuh lepas makan, kadang-kadang nak membuang pun susah?"),
    ("H2", "v", [(21.63, 25.31), (25.63, 27.14)], "Kalau korang ada masalah macam ni, boleh cuba consider ambil Triple Biotix ni."),
    ("B1", "v", [(30.75, 36.61)], "Dia punya base dalam satu sachet ni dah ada prebiotik, probiotik dengan postbiotik sekali tau."),
    ("B2", "v", [(37.41, 43.04)], "Probiotik dia pula 30 bilion CFU, ada tujuh jenis bakteria baik untuk sokongan kesihatan usus kita."),
    ("B3", "v", [(43.94, 47.07)], "Yang aku suka, dia bukan jenis kapsul atau serbuk yang kena bancuh tau."),
    ("B4", "v", [(47.39, 48.93), (49.34, 52.10)], "Dia datang dalam bentuk jelly tau, koyak je terus makan, tak payah bancuh dengan air."),
    ("B5", "v", [(52.51, 57.44)], "Lagi satu, rasa mixed berry dia memang sedap weh, macam makan jelly buah je."),
    ("B6", "v", [(58.05, 59.71)], "Tak rasa macam tengah ambil supplement pun."),
    ("B7", "v", [(60.61, 61.38), (61.82, 66.80)], "Dalam satu kotak ni korang dapat 10 sachet, nak bawa pergi kerja ke, travel ke, memang senang."),
    ("C1", "v", [(67.46, 73.70)], "Sekarang ni saya tengah buat harga promo tau. Better korang beli sekarang sebelum harga dia naik balik. Boleh check out dia beg kuning sekarang."),
]
DROPPED = ("rec1105: the false starts 'dia punya base tu' (28.5-30.0), 'kalau korang' (9.9-10.5) and 'siapa dekat sini yang selalu ...' (11.7-13.2), the second "
           "take of the hook (14.1-20.9; the first take is kept), whisper's 'terima kasih kerana menonton' at the end (silence); "
           "100411 / 110857: their own audio (room / outdoor noise, no speech)")

# A-roll picture: (line, clip, clip in-time). Each shot runs until the next one.
SHOTS = [
    ("H1", "100411", 4.5),      # sitting at the table with the box, looking at camera
    ("H2", "100411", 17.5),     # sachet held up to camera
    ("B1", "110857", 2.0),      # box front close-up on the grass, turning
    ("B2", "110857", 11.0),     # box top / front (under the hero photo)
    ("B3", "100411", 29.0),     # tearing the sachet
    ("B4", "100411", 60.5),     # squeezes the jelly into his mouth
    ("B5", "100411", 69.5),     # eats another one
    ("B6", "100411", 77.8),     # reaction after the jelly
    ("B7", "110857", 15.5),     # opens the box: sachets inside, a handful of sachets
    ("C1", "110857", 49.5),     # box with the sachets on the grass
]
VF = "scale=1080:1920,setsar=1"


def run(*a): subprocess.run(a, check=True)


def layout():
    t, out = 0.0, {}
    for lid, src, rng, txt in LINES:
        pieces = []
        for k, (a, b) in enumerate(rng):
            s0 = a - (PRE if k == 0 else GAP_IN)
            s1 = b + (POST if k == len(rng) - 1 else GAP_IN)
            pieces.append((round(max(0.0, s0), 3), round(s1, 3)))
        dur = sum(b - a for a, b in pieces)
        out[lid] = dict(src=src, pieces=pieces, e0=round(t, 3), e1=round(t + dur, 3), text=txt)
        t += dur
    return out, round(t, 3)


def main():
    L, TOTAL = layout()
    tmp = P / ".media/prep"; tmp.mkdir(parents=True, exist_ok=True)
    # 1. clean each recording (tools/voice.sh chain: denoise from a quiet stretch, EQ, de-ess, compressor, expander)
    clean = {}
    for src, inp in SRC.items():
        n0, n1 = NOISE[src]
        ch = (f"asendcmd=c='{n0} afftdn sn start; {n1} afftdn sn stop',highpass=f=90:poles=2,afftdn=nr=20:nf=-62:tn=1:gs=8,"
              "equalizer=f=320:t=q:w=1.1:g=-3.5,bass=g=1.5:f=120:w=0.7,equalizer=f=4200:t=q:w=1.4:g=3,treble=g=2:f=9500,"
              "deesser=i=0.35:m=0.5:f=0.5,acompressor=threshold=-26dB:ratio=3:attack=6:release=140:makeup=3,"
              "agate=threshold=0.012:ratio=2:range=0.25:attack=3:release=120")
        clean[src] = tmp / f"clean-{src}.wav"
        run("ffmpeg", "-v", "error", "-y", "-i", str(P / inp), "-ac", "1", "-ar", "48000", "-af", ch, "-c:a", "pcm_s16le", str(clean[src]))
    # 2. per-source gain so both recordings sit at the same loudness
    gain = {}
    for src in SRC:
        rng = [p for d in L.values() if d["src"] == src for p in d["pieces"]]
        sel = "+".join(f"between(t,{a},{b})" for a, b in rng)
        r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(clean[src]), "-af", f"aselect='{sel}',asetpts=N/SR/TB,loudnorm=I=-15:print_format=json",
                            "-f", "null", "-"], capture_output=True, text=True).stderr
        js = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
        gain[src] = round(-15.0 - float(js["input_i"]), 2)
    print("gain", gain)
    idx = {k: i for i, k in enumerate(SRC)}
    flt, parts, n = [], [], 0
    for lid, d in L.items():
        for a, b in d["pieces"]:
            dur = b - a
            flt.append(f"[{idx[d['src']]}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=mono,"
                       f"volume={gain[d['src']]}dB,afade=t=in:d=0.03,afade=t=out:st={dur-0.05:.3f}:d=0.05[p{n}]")
            parts.append(f"[p{n}]"); n += 1
    flt.append("".join(parts) + f"concat=n={n}:v=0:a=1,alimiter=limit=0.84:level=false:attack=3:release=60[a]")
    args = []
    for src in SRC:
        args += ["-i", str(clean[src])]
    run("ffmpeg", "-v", "error", "-y", *args, "-filter_complex", ";".join(flt), "-map", "[a]", "-ar", "48000", "-ac", "2",
        "-c:a", "pcm_s16le", str(tmp / "voice.wav"))
    # 3. picture: footage shots that follow the words
    lst = []
    for k, (lid, clip, cin) in enumerate(SHOTS):
        a = L[lid]["e0"]
        b = L[SHOTS[k + 1][0]]["e0"] if k + 1 < len(SHOTS) else TOTAL
        dur = round(b - a, 3)
        print(f"{a:7.2f}-{b:7.2f}  {lid} {clip} @{cin}-{cin + dur:.2f}")
        out = tmp / f"s{k:02d}.mp4"
        run("ffmpeg", "-v", "error", "-y", "-ss", str(cin), "-t", str(round(dur + 0.1, 3)), "-i", str(P / f"src/{clip}.mp4"),
            "-vf", f"{VF},fps=60,trim=duration={dur}", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", str(out))
        lst.append(f"file '{out}'")
    (tmp / "list.txt").write_text("\n".join(lst) + "\n")
    run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-i", str(tmp / "voice.wav"),
        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-r", "60", "-g", "30",
        "-c:a", "aac", "-b:a", "192k", "-shortest", str(P / "assets/a.mp4"))
    bidx, off = {}, 0.0
    for c in CLIPS:
        bidx[c] = {"offset": round(off, 3), "in": 0.0}
        off += float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                     str(P / f"src/{c}.mp4")], capture_output=True, text=True).stdout)
    if not (P / "assets/b.mp4").exists():
        inp = sum((["-i", str(P / f"src/{c}.mp4")] for c in CLIPS), [])
        fl = ";".join(f"[{k}:v]{VF},fps=60,setpts=PTS-STARTPTS[v{k}]" for k in range(len(CLIPS)))
        fl += ";" + "".join(f"[v{k}]" for k in range(len(CLIPS))) + f"concat=n={len(CLIPS)}:v=1:a=0[v]"
        run("ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", fl, "-map", "[v]", "-c:v", "libx264", "-preset", "fast",
            "-crf", "17", "-pix_fmt", "yuv420p", "-g", "30", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED,
                                                      "broll": bidx}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
