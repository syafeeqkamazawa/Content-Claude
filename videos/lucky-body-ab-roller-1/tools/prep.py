"""Lucky Body Ab Roller #1 (11 Nov) — builds assets/a.mp4 for a voiceover edit.

The owner sent a voiceover (src/voice.m4a, Recorder 20261111-1731, 151 s with repeated takes)
plus two silent-ish clips: src/v172759.mp4 (VID_20261111_172759, 8.5 min: on-camera hook,
unboxing, set-up, rolling, product shown to camera) and src/v173042.mp4 (VID_20261111_173042,
57 s: rolling with his daughter on his back). The hook is the owner's own on-camera line in
v172759; every other line is the best take from the voiceover. Each line keeps PRE s before
and POST s after its speech (Silero VAD), so lines sit ~0.6 s apart. The picture is a montage
laid on that timeline; tools/build.py then adds captions, key-point text and photos.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST = 0.25, 0.35
# id, source, speech start, speech end (VAD), text
LINES = [
    ("H",   "v172759", 7.39, 12.58, "Korang tahu tak, buat senaman setiap hari pun belum tentu lemak pada perut ni terus hilang."),
    ("L1",  "voice", 6.88, 12.00, "Sebab sebenarnya senaman perut ni bukan untuk bakar lemak dekat perut semata-mata."),
    ("L2",  "voice", 12.54, 15.36, "Dia lebih kepada melatih otot core kita."),
    ("L3",  "voice", 15.94, 21.09, "Nak kurangkan lemak badan, pemakanan dan aktiviti keseluruhan pun kena jaga juga."),
    ("L4",  "voice", 22.14, 26.85, "Kalau korang nak mula latih otot core dekat rumah, cuba tengok alat ni."),
    ("L5",  "voice", 28.83, 30.62, "Ini Lucky Body ab roller."),
    ("L6",  "voice", 38.78, 45.06, "Dia ada empat roda, jadi tapak dia lebih lebar dan boleh bantu bagi kestabilan masa kita buat pergerakan."),
    ("L7",  "voice", 45.98, 47.39, "Cara guna pun senang je."),
    ("L8",  "voice", 47.84, 53.66, "Mula dengan lutut atas mat, pegang handle, tolak perlahan-lahan ke depan, kemudian tarik balik."),
    ("L9",  "voice", 56.35, 60.74, "Tapi jangan terus pergi jauh. Mula dengan jarak pendek dulu. Ikut kemampuan badan."),
    ("L10", "voice", 68.26, 75.62, "Yang aku suka, dia siap ada pad siku setebal 12mm dan sistem auto rebound yang bantu pergerakan balik."),
    ("L11", "voice", 77.38, 82.75, "Jadi bukan sekadar roller biasa yang kita pegang dan tolak. Dia mudahkan kita bila kita nak undur balik."),
    ("L12", "voice", 86.50, 97.31, "Cuma ingat, alat ni bukan magic yang boleh kempiskan perut dalam beberapa hari tau. Tapi kalau korang konsisten berlatih, jaga teknik dan pemakanan, ini boleh jadi salah satu alat untuk bina rutin senaman korang."),
    ("L13", "voice", 103.52, 105.82, "Tak perlu terus beli macam-macam equipment mahal."),
    ("L14", "voice", 113.02, 119.46, "Kalau nak mula workout core dekat rumah, boleh klik beg kuning dan dapatkan ab roller empat roda ni."),
    ("L15", "voice", 145.22, 149.31, "Seller tengah buat promo sementara harga masih murah. Dapatkan sekarang."),
]
DROPPED = ("voice 1.5-3.0 'sebab sebenarnya' false start; 31.1-37.1 take 1 of the four-wheel line (take 2 ends the "
           "sentence); 61.3-67.2 two false starts of the elbow-pad line; 97.8-102.7 stumbles of 'tak perlu beli'; "
           "108.1-111.9 and 122.5-144.7 other CTA takes ('aku dah letak dekat beg kuning' repeats 'klik beg kuning'); "
           "'terima kasih kerana menonton' after 149.3 is whisper hallucination over silence")

# (line, source time the shot starts or None = line start, clip, clip in, speed, crop)
SHOTS = [
    ("H",   None,   "v172759", 7.14, 1, "hook"),    # on camera, own audio (picture synced)
    ("L1",  None,   "v172759", 353.0, 1, "low"),    # rolling out
    ("L2",  None,   "v173042", 5.0, 1, "low"),      # kneels, starts rolling, smiles at camera
    ("L3",  None,   "v172759", 314.0, 1, "low"),    # (AI photos on top from 'pemakanan')
    ("L4",  None,   "v172759", 103.0, 1, "hook"),   # opening the box
    ("L4",  25.32,  "v172759", 118.0, 1, "hook"),   # 'cuba tengok alat ni' — takes the roller out
    ("L5",  None,   "v172759", 481.5, 1, None),     # 'Ini Lucky Body ab roller' — shown to camera
    ("L6",  None,   "v172759", 437.3, 1, None),     # four wheels from below
    ("L6",  43.06,  "v173042", 14.5, 1, "low"),     # 'kestabilan' — rolling with his daughter on his back
    ("L7",  None,   "v172759", 455.5, 1, "low"),    # picks it up, kneels
    ("L8",  None,   "v172759", 299.5, 1, "low"),    # knees on mat, hands on handles, rolls out, back
    ("L9",  None,   "v172759", 359.0, 1, "low"),    # short rolls
    ("L10", None,   "v172759", 398.0, 1, None),     # finger on the elbow pads
    ("L10", 72.36,  "v173042", 19.0, 1, "low"),     # 'auto rebound' — rolls back
    ("L11", None,   "v172759", 316.0, 1, "low"),    # out and back
    ("L12", None,   "v172759", 460.0, 1, "low"),
    ("L12", 90.20,  "v172759", 338.0, 1, "low"),    # 'konsisten berlatih'
    ("L12", 93.94,  "v172759", 390.0, 1, None),     # 'rutin senaman' — gets up, walks to camera
    ("L13", None,   "v172759", 288.0, 1, None),     # product + knee pads to camera
    ("L14", None,   "v172759", 491.0, 1, None),     # handle / LUCKY BODY close
    ("L14", 117.04, "v172759", 484.5, 1, None),     # 'dapatkan ab roller empat roda ni'
    ("L15", None,   "v172759", 500.0, 1, None),     # product to camera, end
]
VF = {None: "scale=1080:1920,setsar=1",
      "low": "crop=940:1671:0:249,scale=1080:1920:flags=lanczos,setsar=1",
      "hook": "crop=800:1422:140:230,scale=1080:1920:flags=lanczos,setsar=1"}


def run(*a): subprocess.run(a, check=True)


def layout():
    t, out = 0.0, {}
    for lid, src, a, b, txt in LINES:
        s0, s1 = a - PRE, b + POST
        out[lid] = dict(src=src, s0=s0, s1=s1, e0=round(t, 3), e1=round(t + s1 - s0, 3), text=txt)
        t += s1 - s0
    return out, round(t, 3)


def main():
    L, TOTAL = layout()
    tmp = P / ".media/prep"; tmp.mkdir(parents=True, exist_ok=True)
    # audio: hook from the clip and the voiceover lines; each source is measured once and
    # gained to -15 LUFS (a per-piece loudnorm shifts timestamps), then a light chain + limiter
    gain = {}
    for src, inp in (("voice", "src/voice.m4a"), ("v172759", "src/v172759.mp4")):
        rng = [(d["s0"], d["s1"]) for d in L.values() if d["src"] == src]
        sel = "+".join(f"between(t,{a},{b})" for a, b in rng)
        r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(P / inp), "-vn", "-af",
                            f"aselect='{sel}',asetpts=N/SR/TB,highpass=f=75,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,"
                            "loudnorm=I=-15:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
        js = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
        gain[src] = round(-13.3 - float(js["input_i"]), 2)  # -13.3 here lands at ~-15 LUFS after the limiter
    print("gain", gain)
    flt, parts = [], []
    for k, (lid, d) in enumerate(L.items()):
        i = 0 if d["src"] == "voice" else 1
        dur = d["s1"] - d["s0"]
        flt.append(f"[{i}:a]atrim={d['s0']}:{d['s1']},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=mono,"
                   f"highpass=f=75,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,volume={gain[d['src']]}dB,"
                   f"afade=t=in:d=0.03,afade=t=out:st={dur-0.05:.3f}:d=0.05[p{k}]")
        parts.append(f"[p{k}]")
    flt.append("".join(parts) + f"concat=n={len(parts)}:v=0:a=1,alimiter=limit=0.89:level=false[a]")
    run("ffmpeg", "-v", "error", "-y", "-i", str(P / "src/voice.m4a"), "-i", str(P / "src/v172759.mp4"),
        "-filter_complex", ";".join(flt), "-map", "[a]", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(tmp / "voice.wav"))
    # picture
    st = []
    for lid, t, clip, cin, sp, crop in SHOTS:
        d = L[lid]
        st.append((d["e0"] if t is None else round(d["e0"] + t - d["s0"], 3), clip, cin, sp, crop))
    lst = []
    for k, (a, clip, cin, sp, crop) in enumerate(st):
        b = st[k + 1][0] if k + 1 < len(st) else TOTAL
        dur = round(b - a, 3)
        out = tmp / f"s{k:02d}.mp4"
        run("ffmpeg", "-v", "error", "-y", "-ss", str(cin), "-t", str(round(dur * sp + 0.1, 3)), "-i", str(P / f"src/{clip}.mp4"),
            "-vf", f"{VF[crop]},setpts=PTS/{sp},fps=60,trim=duration={dur}", "-an",
            "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", str(out))
        lst.append(f"file '{out}'")
        print(f"{a:7.2f}-{b:7.2f}  {clip} @{cin}")
    (tmp / "list.txt").write_text("\n".join(lst) + "\n")
    run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-i", str(tmp / "voice.wav"),
        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-r", "60", "-g", "30",
        "-c:a", "aac", "-b:a", "192k", "-shortest", str(P / "assets/a.mp4"))
    run("ffmpeg", "-v", "error", "-y", "-i", str(P / "assets/a.mp4"), "-an", "-c:v", "copy", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
