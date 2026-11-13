"""Lab Biotix Triple Biotix #1 (13 Nov, folder "Lab Biotix Triple Biotix") — voiceover video.
Sound = the owner's voice recordings (Recorder 20261113-1904.m4a = the script, Recorder 20261113-1907.m4a = the clean CTA
take), denoised and cleaned with the tools/voice.sh chain. Picture = VID_20261113_185850 (owner in the car with the box:
showing it, opening it, the sachet close-ups, tearing it, eating the powder, thumbs up; no speech on it), cut to follow the
words. assets/b.mp4 = the same clip, muted, for close-up cutaways. Complete sentences ~0.5 s apart; repeated takes dropped.
Style (owner 12 Nov): motion overlay text + plain one-word caption of the Jus Gout 'video contoh', visual overlays.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"v": "src/rec1904.m4a", "c": "src/rec1907.m4a"}
NOISE = {"v": (58.2, 62.5), "c": (0.0, 0.9)}   # quiet stretches for the denoise profile
FOOT = "185850"
# id, source, [(start, end) speech ranges], text
LINES = [
    ("V1", "v", [(2.00, 8.26)], "Korang tahu tak, prebiotik, probiotik dengan postbiotik ni sebenarnya tiga benda yang berbeza tau."),
    ("V2", "v", [(9.12, 10.62)], "Ok, senang cerita macam ni."),
    ("V3", "v", [(11.26, 14.43)], "Prebiotik ni makanan untuk bakteria baik dalam usus kita."),
    ("V4", "v", [(15.20, 17.60)], "Probiotik pula, bakteria baik tu sendiri."),
    ("V5", "v", [(18.46, 19.62), (19.94, 22.88), (23.20, 25.44)], "Postbiotik pula, komponen daripada mikroorganisma yang dah tak hidup, tapi masih boleh beri manfaat tertentu."),
    ("V6", "v", [(26.14, 30.24)], "Sebab tu kalau nak pilih produk penjagaan usus, jangan tengok nombor bilion je."),
    ("V7", "v", [(30.72, 32.30), (32.82, 36.74)], "Contohnya Triple Biotix ni. Dia gabungkan ketiga-tiga komponen tadi dalam satu sachet tau."),
    ("V8", "v", [(42.78, 48.45)], "Ada 30 bilion CFU probiotik, tujuh jenis bakteria, siap dengan L-carnitine tau."),
    ("V9", "v", [(50.24, 54.50)], "Perisa dia mixed berry, satu sachet 20 gram dan satu kotak ada 10 sachet."),
    ("V10", "v", [(55.04, 57.82)], "Senang sangat nak jadikan sebahagian daripada rutin harian ni."),
    ("V11", "v", [(62.68, 66.91)], "Senang sangat nak makan. Rasanya pun sedap tau."),
    ("V12", "v", [(73.06, 78.46)], "Kalau korang tengah cari produk untuk bantu kesihatan usus, boleh consider yang ni. Aku sangat recommend."),
    ("C1", "c", [(0.92, 5.18)], "Link aku dah letak dekat beg kuning, sementara harga tengah murah tu korang check out sekarang."),
]
DROPPED = ("rec1904: the first 'ada 30 bilion CFU, ada 30' (37.3-41.8, repeated), the first 'kalau korang tengah cari ... "
           "sokongan kesihatan usus korang, boleh' take (67.9-72.1), the repeated CTA takes 'aku dah letak dekat beg kuning ni / "
           "link aku dah letak ... / sementara seller buat harga promo ...' (78.8-114.5; the clean take is rec1907); "
           "185850: its own audio (car noise, no speech), the idle driving stretch (17-27)")

# A-roll picture: (line, word/None = line start, footage in-time). Each shot runs until the next one.
SHOTS = [
    ("V1", None, 0.6),      # holding the box up beside his face
    ("V2", None, 8.6),      # brings the box to camera
    ("V3", None, 29.0),     # opening the box
    ("V5", None, 40.0),     # looking at the box, handling it
    ("V6", None, 59.0),     # box front to camera, opens it on the sachets
    ("V8", None, 47.5),     # handling the open box (mostly under the box-back photo)
    ("V9", None, 71.0),     # sachet close-up, front and back
    ("V10", None, 88.0),    # tearing the sachet
    ("V11", None, 110.0),   # pours the powder into his mouth, tastes it
    ("V12", None, 129.5),   # second sachet, eats it, thumbs up
    ("C1", None, 82.5),    # sachet held up to camera, label facing it
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
    for k, (lid, _, cin) in enumerate(SHOTS):
        a = L[lid]["e0"]
        b = L[SHOTS[k + 1][0]]["e0"] if k + 1 < len(SHOTS) else TOTAL
        dur = round(b - a, 3)
        print(f"{a:7.2f}-{b:7.2f}  {lid} {FOOT} @{cin}-{cin + dur:.2f}")
        out = tmp / f"s{k:02d}.mp4"
        run("ffmpeg", "-v", "error", "-y", "-ss", str(cin), "-t", str(round(dur + 0.1, 3)), "-i", str(P / f"src/{FOOT}.mp4"),
            "-vf", f"{VF},fps=60,trim=duration={dur}", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", str(out))
        lst.append(f"file '{out}'")
    (tmp / "list.txt").write_text("\n".join(lst) + "\n")
    run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-i", str(tmp / "voice.wav"),
        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-r", "60", "-g", "30",
        "-c:a", "aac", "-b:a", "192k", "-shortest", str(P / "assets/a.mp4"))
    if not (P / "assets/b.mp4").exists():
      run("ffmpeg", "-v", "error", "-y", "-i", str(P / f"src/{FOOT}.mp4"), "-vf", f"{VF},fps=60", "-an", "-c:v", "libx264", "-preset", "fast",
          "-crf", "17", "-pix_fmt", "yuv420p", "-g", "30", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED,
                                                      "broll": {FOOT: {"offset": 0.0, "in": 0.0}}}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
