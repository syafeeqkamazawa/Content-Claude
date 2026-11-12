"""Kurma Ajwa Quba Food #6 (12 Nov) — builds assets/a.mp4 from the owner's two talking clips
VID_20261112_162407 (src/k162407.mp4: hook, the 1 kg pack, texture, quality, CTA) and VID_20261112_162533
(src/k162533.mp4: opens a date, tastes it, asks for comments), complete sentences ~0.5 s apart.
Style (owner 12 Nov): motion overlay text + caption of the Jus Gout 'video contoh', visual overlays, talking kept.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"k1": "src/k162407.mp4", "k2": "src/k162533.mp4"}
# id, source, [(start, end) speech ranges], text
LINES = [
    ("Q1", "k1", [(40.83, 45.28), (46.14, 48.42)], "Kalau korang ada masalah, contoh nak sarapan dengan lebih cepat dan mudah, tanpa perlu masa yang banyak,"),
    ("Q2", "k1", [(51.81, 53.12)], "jangan terus scroll dulu."),
    ("Q4", "k1", [(76.13, 79.23), (79.81, 81.34), (81.98, 83.84)], "Kalau korang ada masalah tadi tu, aku cadangkan korang boleh gantikan dengan ni, kurma ajwa daripada Quba Food ni."),
    ("Q5", "k1", [(90.27, 92.74)], "Yang aku pegang ni, kurma satu kilogram tau."),
    ("Q6", "k1", [(99.30, 104.10)], "Aku tunjuk dekat korang macam mana bentuk kurma dia, tekstur dia, macam mana kualiti dia."),
    ("Q7", "k1", [(110.85, 121.70)], "Ni kurma dia, korang tengok kurma dia, dengan tekstur macam ni, kurma ajwa eh, dengan harga macam ni kat luar susah tau nak dapat."),
    ("Q8", "k1", [(122.74, 123.48), (124.26, 125.30), (126.72, 128.54)], "Tengok tekstur dia. Masya Allah kan. Dan berat dia yang ni, satu kg."),
    ("Q9", "k1", [(133.30, 136.40), (136.66, 137.46), (138.60, 139.66), (140.86, 143.10), (143.52, 144.14)], "Lepas tu korang tengok ni, korang nilailah sendiri macam mana kualiti dia kan, memang sangat, orang kata kemas lah, dan dia tak terlalu basah, tak terlalu kering, sederhana tu."),
    ("R1", "k2", [(3.38, 4.70), (6.42, 7.98), (12.46, 13.52), (15.50, 17.10), (18.02, 20.00), (21.20, 24.30)], "Tekstur kurma ajwa ni, kat dalam dia, aku buka. Kat dalam dia, kemas je, kering, kat sini kering, dekat luar basah, chewy-chewy, ni macam chewy-chewy ni tu tau."),
    ("R2", "k2", [(26.52, 29.58), (30.70, 33.60), (34.04, 38.42), (38.98, 40.88), (41.38, 45.06)], "Bila kau makan, sedap. Macam kau, kau tak rasa macam kau makan kurma. Yang mana tak suka kurma tu, please, beli dekat beg kuning. Korang rasa sendiri, dan korang komen, macam mana feedback korang."),
    ("R3", "k2", [(66.62, 71.18), (72.14, 73.40), (73.90, 77.00)], "Yang mana dah pernah rasa kurma ajwa daripada Quba Food ni, korang drop komen. Memang insyaAllah lah, kat aku makan ni memang sangat sedap dan berkualiti."),
    ("Q10", "k1", [(162.10, 166.88), (167.70, 171.78)], "So korang yang mana nak sarapan dengan lebih pantas, aku dah sediakan link dekat beg kuning. Seller tengah buat harga promo tu, sementara harga murah, korang check out terus."),
]
DROPPED = ("162407: three earlier tries of the hook (0-39), 'ok', 'sebenarnya kan, ni antara sebab aku suka semak' "
           "(unfinished, 56-62), 'tau ya', the first try of 'kalau korang ada masalah' (74), the 'ok's / 'haa's between "
           "pieces, the first CTA take (152-160); 162533: the first two tries of the comment line (45.9-65.4), the doubled "
           "'kat', the 'terima kasih' whisper hallucinations at the end")

# (line, source time the shot starts or None = line start, clip, clip in, crop)
SHOTS = [(lid, None, {"k1": "k162407", "k2": "k162533"}[src], "sync", None) for lid, src, *_ in LINES]
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
    run("ffmpeg", "-v", "error", "-y", "-i", str(P / "assets/a.mp4"), "-an", "-c:v", "copy", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
