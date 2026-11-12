"""Jus Gout #14 (12 Nov) — builds assets/a.mp4. The owner's 'video contoh.mp4' (src/contoh.mp4) is the
reference for the motion overlay text and the captions only (owner: "hanya ikut motion overlay text
dan caption sahaja. Video saya bercakap masih dikekalkan").

Sound: the owner's talk in VID_20261112_142940 (src/a142940.mp4; its audio goes silent at
143 s) continued by 'sambungan 1.m4a' and 'sambungan 2.m4a'. Each line is one or more source
ranges (stumbles / 'ok' between them left out); lines sit GAP s apart.
Picture: the talking clip itself while its audio plays; VID_20261012_172341 (src/b172341.mp4 —
jar in hand, top-down opening, scoops, hot water, stirring) under the 'sambungan' voice lines.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"clip": "src/a142940.mp4", "s1": "src/samb1.m4a", "s2": "src/samb2.m4a"}
# id, source, [(start, end) speech ranges], text
LINES = [
    ("H1", "clip", [(47.46, 50.11)], "Korang ada masalah sakit sendi tak? Jangan scroll lagi."),
    ("H2", "clip", [(50.85, 57.95)], "Ini antara sebab kenapa aku suka tengok barang ni ikut masalah sebenar, bukannya ikut video viral je."),
    ("H3", "clip", [(58.66, 65.02)], "Kali ni produk yang aku nak bagitahu, Jus Gout daripada Pro Max series."),
    ("L4", "clip", [(66.40, 69.36)], "Jus Gout Pro Max series ni minuman herba tau."),
    ("L5", "clip", [(79.65, 83.84)], "Dalam ni ada campuran 6 ekstrak herba terpilih lah."),
    ("L6", "clip", [(84.42, 93.20)], "Ada bromelain iaitu ekstrak nanas, milk thistle, lemon, halia, curcuma longa dan juga oren."),
    ("L7", "clip", [(96.86, 100.16)], "Cara penyediaan ni pun sangat mudah."),
    ("L9", "clip", [(114.18, 116.13), (118.70, 119.55), (120.40, 121.70)], "Dalam dia bentuk macam ni tau. Serbuk macam ni. Korang ambil je dua sudu."),
    ("L10", "clip", [(125.45, 128.60)], "Dua sudu untuk 250ml."),
    ("L11", "clip", [(129.78, 130.42), (131.72, 132.40)], "Air panas lah, dan kacau."),
    ("S1", "s1", [(2.62, 24.62)], "Korang kacau sampai larut, sampai sebati, lepas tu korang akan nampak, korang akan bau, bau dia ada bau halia, bau nanas, orang kata tak adalah kurang susah nak minum sebab dia ada bau-bau yang, orang kata bau-bau buah, bau yang senang kita nak minum setiap hari lah."),
    ("A", "s2", [(2.98, 8.74)], "Jadi, Jus Gout ni adalah alternatif lah kepada yang ada masalah sakit gout ni."),
    ("B", "s2", [(14.40, 21.12)], "Saya sendiri pun ada sakit gout ni, memang hanya orang yang ada sakit gout je faham betapa sakit ni."),
    ("C", "s2", [(21.79, 24.06)], "Sakit gout ni, dia punya denyut tu kan."),
    ("D", "s2", [(24.99, 29.15)], "So, boleh insyaAllah cuba Jus Gout ni daripada Pro Max series."),
    ("E", "s2", [(44.45, 51.58)], "Seller pun tengah buat harga promo tu sebelum harga tu naik balik, boleh grab awal-awal di beg kuning."),
]
DROPPED = ("clip 16-46: three earlier tries of the hook; 'kandungan dan cara penyediaan mesti kandungan' (69.4-76.2); "
           "'dalam ni, ok?' after the herb list; 'korang tengok ni'; the 'ok's between the powder lines; 'dua sudu, "
           "letaklah ni' (repeated); 'haa kacau, kacau sampai larut lah, lepas tu, bila dah korang kacau ni' (said again in "
           "sambungan 1); sambungan 1 'ok' at both ends; sambungan 2 'insyaAllah boleh ikhtiar, boleh cuba…' (9.3, said again "
           "at 25.0), CTA take 1 (29.8-36.7) and 'okay' before take 2")

# (line, source time the shot starts or None = line start, clip, clip in, crop)
SHOTS = [
    # the owner's talking clip, picture synced to its own audio (owner 12 Nov: "Video saya bercakap
    # masih dikekalkan" — only the reference's motion text and captions are copied)
    ("H1", None, "a142940", "sync", None),
    ("H2", None, "a142940", "sync", None),
    ("H3", None, "a142940", "sync", None),
    ("L4", None, "a142940", "sync", None),
    ("L5", None, "a142940", "sync", None),
    ("L6", None, "a142940", "sync", None),
    ("L7", None, "a142940", "sync", None),
    ("L9", None, "a142940", "sync", None),
    ("L10", None, "a142940", "sync", None),
    ("L11", None, "a142940", "sync", None),
    # the clip's sound dies at 143 s: the 'sambungan' voice lines run over the product footage
    ("S1", None, "b172341", 114.5, None),     # 'kacau sampai larut' — powder dissolving
    ("S1", 5.64, "b172341", 180.5, None),     # 'lepas tu korang akan nampak'
    ("S1", 7.98, "b172341", 196.0, None),     # 'korang akan bau' — golden juice
    ("S1", 14.26, "b172341", 161.0, None),
    ("S1", 19.28, "b172341", 203.0, None),
    ("A", None, "b172341", 66.0, None),       # open jar beside the cup
    ("B", None, "b172341", 204.5, None),      # finished juice
    ("C", None, "b172341", 133.0, None),      # (AI photo on top)
    ("D", None, "b172341", 19.5, None),       # jar front
    ("E", None, "b172341", 5.5, None),        # jar front (promo card on top)
]
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
