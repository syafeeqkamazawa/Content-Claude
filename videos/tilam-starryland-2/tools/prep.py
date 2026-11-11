"""Tilam Starryland Back-Wave #2 (11 Nov) — builds assets/a.mp4 for a voiceover edit.

The voiceover (src/voice.m4a, Recorder 20261111-1511) is one continuous take with only
~0.2-0.4 s between sentences. The owner wants ~0.5 s between lines, so the take is cut in
the middle of each between-sentence silence and silence is inserted until every gap is
GAP s. The picture is a montage of the owner's footage laid on that new timeline, so the
normal A-roll pipeline (tools/build.py: segments, word captions, kp, photos) runs on top.

Sources (all 60 fps): src/v121807.mp4 close-ups (rear cam), src/v122144.mp4 owner lying /
sitting, src/tikold.mp4 = the old TikTok post (TikDownloader 7694908315205192966) with the
rolled mattress; its red/yellow title sticker sits at y 270-540, so it is cropped below it.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
GAP = 0.6
# speech end / next speech start at each sentence boundary (RMS < -45 dB), voice time
BOUNDS = [(7.68, 8.09), (15.01, 15.48), (18.52, 18.87), (22.06, 22.22), (27.13, 27.60), (30.79, 31.17), (34.64, 34.94)]
T0, T1 = 1.55, 38.15
cuts = [round((a + b) / 2, 3) for a, b in BOUNDS]
ins = [round(max(0.0, GAP - (b - a)), 3) for a, b in BOUNDS]


def N(t):
    """voice time -> edit time"""
    return round(t - T0 + sum(i for c, i in zip(cuts, ins) if c <= t), 3)


LINES = [T0] + cuts                     # line k starts at LINES[k] (voice time)
TOTAL = N(T1)
# (voice time the shot starts, clip, source in, speed, crop)  — each runs until the next one
SHOTS = [
    (LINES[0], "v122144", 0.5, 1, None),      # hook (AI 'tilam lama' photo on top)
    (6.00, "v121807", 62.0, 1, None),         # 'mungkin dah sampai masa tukar' -> the new mattress
    (LINES[1], "v121807", 0.5, 1, None),      # 'korang tengok Starryland Back-Wave ni'
    (9.80, "v121807", 27.6, 1, None),         # 'tebal 10 inci' — side view, thickness
    (12.70, "tikold", 6.0, 1, "tik"),         # 'datang bergulung' — the rolled mattress
    (LINES[2], "tikold", 17.0, 2.6, "tik"),   # 'buka plastik ... mengembang' — fast-forward
    (LINES[3], "v121807", 39.0, 1, None),     # pocket spring (AI cut-away on top)
    (20.50, "v121807", 41.2, 1, None),        # 'sokongan badan' — hand presses the mattress
    (LINES[4], "v121807", 48.0, 1, None),     # 'Cloud Motion Foam' — quilted top
    (24.06, "v121807", 35.6, 1, None),        # '3D mesh fabric' — mesh side panel
    (LINES[5], "v122144", 18.5, 1, None),     # 'pilihan size' — owner lying on it
    (LINES[6], "v122144", 194.0, 1, None),    # CTA — owner sitting on it
    (LINES[7], "v121807", 8.0, 1, None),     # promo — the mattress hero, ends on the product
]
VF = {None: "scale=1080:1920,setsar=1",
      "tik": "crop=765:1360:157:560,scale=1080:1920:flags=lanczos,setsar=1"}


def run(*a): subprocess.run(a, check=True)


def main():
    tmp = P / ".media/prep"; tmp.mkdir(parents=True, exist_ok=True)
    # voice: cut + gaps, light clean-up (rumble cut, gentle compression, -15 LUFS)
    parts, flt = [], []
    edges = [T0] + cuts + [T1]
    for k in range(len(edges) - 1):
        flt.append(f"[0:a]atrim={edges[k]}:{edges[k+1]},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={edges[k+1]-edges[k]-0.02}:d=0.02[p{k}]")
        parts.append(f"[p{k}]")
        if k < len(ins) and ins[k] > 0:
            flt.append(f"anullsrc=r=48000:cl=mono,atrim=0:{ins[k]}[z{k}]"); parts.append(f"[z{k}]")
    flt.append("".join(parts) + f"concat=n={len(parts)}:v=0:a=1,aformat=sample_rates=48000:channel_layouts=mono,"
               "highpass=f=75,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,loudnorm=I=-15:TP=-1.5:LRA=9[a]")
    run("ffmpeg", "-v", "error", "-y", "-i", str(P / "src/voice.m4a"), "-filter_complex", ";".join(flt),
        "-map", "[a]", "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(tmp / "voice.wav"))
    # picture
    lst = []
    for k, (t, clip, sin, sp, crop) in enumerate(SHOTS):
        a = N(t); b = N(SHOTS[k + 1][0]) if k + 1 < len(SHOTS) else TOTAL
        d = round(b - a, 3); src_d = round(d * sp + 0.1, 3)
        out = tmp / f"s{k:02d}.mp4"
        run("ffmpeg", "-v", "error", "-y", "-ss", str(sin), "-t", str(src_d), "-i", str(P / f"src/{clip}.mp4"),
            "-vf", f"{VF[crop]},setpts=PTS/{sp},fps=60,trim=duration={d}", "-an",
            "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", str(out))
        lst.append(f"file '{out}'")
        print(f"{a:6.2f}-{b:6.2f}  {clip} @{sin} x{sp}")
    (tmp / "list.txt").write_text("\n".join(lst) + "\n")
    run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-i", str(tmp / "voice.wav"),
        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-r", "60", "-g", "30",
        "-c:a", "aac", "-b:a", "192k", "-shortest", str(P / "assets/a.mp4"))
    run("ffmpeg", "-v", "error", "-y", "-i", str(P / "assets/a.mp4"), "-an", "-c:v", "copy", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines_edit": [N(t) for t in LINES], "total": TOTAL,
                                                       "cuts": cuts, "inserted": ins}, indent=1))
    print("TOTAL", TOTAL, "lines", [N(t) for t in LINES])


if __name__ == "__main__":
    main()
