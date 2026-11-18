"""Lab Biotix Triple Biotix #3 (18 Nov, folder "Video hari ini") — builds assets/a.mp4 from the owner's talking clip
VID_20261118_113459 (src/113459.mp4: 40s hook, modern food habits, balance, local brand, his 3rd-4th box, pre/pro/postbiotic,
jelly taste, eating one, dose, 10 sachets, CTA), complete sentences ~0.5 s apart. The health / medical claims are dropped
(owner's 5 Nov rule: no TikTok-risk lines). assets/b.mp4 = the grass B-roll VID_20261114_110857 (box and sachets) followed
by the talking clip itself, for cutaways.
Style: talking kept, plain one-word caption, motion text in the product's theme (EDL fx_theme "biotix"), realistic AI
visuals where needed (owner 14 Nov).
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"m": "src/113459.mp4"}
CLIP = {"m": "113459"}
# id, source, [(start, end) speech ranges], text
LINES = [
    ("L1", "m", [(7.97, 9.47), (10.40, 13.09), (13.66, 16.64)], "Umur dah masuk 40-an ni, eloklah jaga apa yang patut. Usus tu memang kena banyak jaga tau, usus-usus ni."),
    ("L2", "m", [(54.53, 58.72), (59.26, 60.03), (60.48, 60.86), (61.44, 62.34), (62.75, 64.29), (65.02, 65.60), (66.05, 68.67), (69.09, 70.59)],
     "Benda ni macam sebagai basic lah, sebab kita pun sedia maklum hari ni, makanan pun banyak dah, orang kata inovasi makanan. Kita pula FOMO, pantang ada makanan pelik-pelik, kita lah yang dulu."),
    ("L3", "m", [(70.98, 73.95), (74.59, 76.32), (76.86, 80.96)], "So bila macam tu dah berlaku dalam kita ni, kenalah ada juga benda yang kita kena seimbangkan dengan pemakanan kita yang tak tentu hala tu."),
    ("L4", "m", [(81.38, 82.94), (88.10, 90.05)], "So ni antara salah satu. Ni local brand eh, local brand."),
    ("L5", "m", [(121.82, 126.69), (127.58, 129.44), (130.40, 132.60)], "Saya sendiri pun dah, masa ni dia dah kali ketiga sampai keempat saya dah consume, Alhamdulillah. Orang kata memang macam kita punya maintenance lah ni."),
    ("L6", "m", [(146.30, 147.81), (148.19, 152.96), (153.54, 154.82), (155.33, 156.38)], "Dengan khasiat dia, dengan kelebihan dia. Tengoklah, dia ada apa? Dia ada triple tau. Probiotik, prebiotik, postbiotik, tiga. Triple Biotix."),
    ("L7", "m", [(157.34, 159.20), (159.84, 162.62), (163.26, 165.89)], "Dan rasa dia senang nak makan. Rasa dia jelly-jelly macam tu, macam kita punya jelly je."),
    ("L8", "m", [(167.30, 169.22), (169.63, 170.30), (170.94, 171.81), (172.38, 175.60)], "Saya tunjukkan sikit, ada bentuk dia. Okay je, sedap. Bismillah."),
    ("L9", "m", [(177.54, 180.58), (182.59, 183.36)], "Kalau ikutkan nak ambil sekali harung, tak boleh. Ambil ikut dos lah."),
    ("L10", "m", [(190.46, 191.78), (193.15, 195.07)], "Dalam ni ada 10 sachet. 10 sachet, insyaAllah."),
    ("L11", "m", [(142.75, 145.79), (195.52, 198.69)], "Dapatkan di beg kuning, insyaAllah harga pun tak mahal lah. So boleh, beli dia beg kuning sekarang."),
]
DROPPED = ("113459 — TikTok-risk health / medical claims (owner's 5 Nov rule): 'kebanyakan masalah penyakit yang keluar daripada "
           "badan kita ni dari usus' (17-29), the symptom list 'kulit kusam, perut kembung, muka bloated / sembab, nafas berbau' "
           "(30-54), 'certified', the doctor and the ambassadors who 'mengesahkan triple biotix ni selamat dan efektif' (90-119), "
           "'mencegah, prevention is better than cure' (132.9-137.8), 'kita ikhtiar' (140.6-142.3); unclear: 'tambahkan lagi "
           "cluster' (83-88), the dose words 'ambil ... sebelum ...' (184-189); fillers 'insyaAllah, okay' and 'terima kasih'")
# B-roll for the cutaways, concatenated into assets/b.mp4 in this order: (clip, in, out)
BROLL = [("110857", 0.0, 72.1), ("113459", 0.0, 218.0)]

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
    if not (P / "assets/b.mp4").exists():
        run("ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fl), "-map", "[v]", "-c:v", "libx264", "-preset", "fast",
            "-crf", "17", "-pix_fmt", "yuv420p", "-g", "30", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED, "broll": bidx}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
