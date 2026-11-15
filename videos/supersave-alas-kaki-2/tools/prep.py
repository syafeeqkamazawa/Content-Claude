"""SuperSave Alas Kaki Dapur #2 (15 Nov, folder "Footage hari ini") — voiceover video in the shape of the owner's
"Video contoh" (faceless: the mat in the kitchen, walking on it, its rubber base, pushing it, water on it, a CTA).
Sound = the owner's recording Recorder 20261115-1513.m4a (best complete take of each point; the retakes dropped), cleaned
with the tools/voice.sh chain. Picture = his eight clips VID_20261115_113747 ... 114959, cut to follow the words.
assets/b.mp4 = all eight clips back to back, muted, for cutaways (offsets in data/timeline.json).
Style: caption kept (owner 14 Nov), motion text themed after the black-and-white tile mat (fx_theme "tile").
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"v": "src/rec1513.m4a"}
NOISE = {"v": (18.95, 21.80)}   # quiet stretch for the denoise profile
CLIPS = ["113747", "113948", "114541", "114641", "114747", "114834", "114930", "114959"]   # assets/b.mp4 order
# id, source, [(start, end) speech ranges], text
LINES = [
    ("V1", "v", [(0.99, 3.81)], "Tak payah beli mahal-mahal, beli murah macam ni je."),
    ("V2", "v", [(4.16, 10.66)], "Anti-slip, serap air, dia ada tiga saiz tau, saiz L, saiz M dan saiz S. Corak ni cantik-cantik tau."),
    ("V3", "v", [(11.23, 13.15)], "Yang saya punya ni code Moroccan Mix."),
    ("V4", "v", [(42.82, 43.68), (44.77, 50.62)], "Bila korang jalan je atas alas ni, memang selesa weh, sebab tak licin, and anti-slip juga tau. Tengok ni."),
    ("V5", "v", [(51.17, 53.22)], "Saya gerak-gerakkan pun memang tak bergerak terus."),
    ("V6", "v", [(57.28, 59.39)], "Ada yang ni, terus lawa ruang dapur weh."),
    ("V7", "v", [(59.68, 62.37), (62.66, 65.82)], "Penyerapan dia pun pantas tau, kalau kena air, terus serap air macam ni. Bahagian belakang pun tak tembus tau."),
    ("V8", "v", [(84.90, 88.40)], "So korang, harga tengah murah tau, macam-macam corak ada, semua cantik-cantik."),
    ("V9", "v", [(110.08, 112.90)], "Tekan beg kuning kat bawah ni sekarang, sementara harga tu masih murah."),
]
DROPPED = ("rec1513: the first 'bila pakai tu memang selesa sebab tak licin and anti-slip, tengok ni' (13.4-18.9) and its "
           "retakes 'bila pakai tu memang selesa weh' / 'bila (korang) jalan atas alas ni' (21-42; the complete take at 42.8 is "
           "kept), the false start 'lawa' (54.4), the CTA retakes 'so korang harga tengah murah tau, corak cantik-cantik ...' "
           "(67-84) and 'tekan beg kuning (kat bawah ni) sekarang, sementara harga masih murah' (88.5-110; the last take is kept); "
           "the eight clips: their own audio (no speech)")

# A-roll picture: (line, clip, clip in-time). Each shot runs until the next one; cutaways in the EDL split the longer lines.
SHOTS = [
    ("V1", "114641", 3.0),      # walking barefoot on the mat
    ("V2", "114834", 0.5),      # the mats along the kitchen floor
    ("V3", "113948", 3.0),      # holding the mat up: the Moroccan Mix pattern
    ("V4", "114641", 11.0),     # walking on it again
    ("V5", "114930", 4.4),      # pushing the mat by hand — it stays put
    ("V6", "114747", 0.3),      # the kitchen with the mat
    ("V7", "114959", 1.0),      # water on the mat, wiping it
    ("V8", "113747", 1.3),      # standing on the mat at the sink
    ("V9", "114834", 6.0),      # the mats in the kitchen
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
