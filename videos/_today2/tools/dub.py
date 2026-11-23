"""Like combo.py, but the picture comes from other clips: speech parts give the audio (and word list / VAD), the
video parts give a face-free picture laid under it (owner, 23 Nov: "langsung tak nampak wajah anak anak saya" —
the clips filmed with his children are used for their sound only, over close-ups from the clip he filmed alone).
python3 dub.py NAME --a id:lo:hi [...] --v id:lo:hi [...]
Writes .media/combo-NAME.mp4, wl-combo-NAME.txt, vad-combo-NAME.txt (same names as combo.py, so specs use _combo)."""
import re, subprocess, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
M = D / ".media"
W2 = {"143318": 245.5, "152300": 29.9}
args = sys.argv[1:]
name = args.pop(0)
ia, iv = args.index("--a"), args.index("--v")
apart, vpart = args[ia + 1:iv], args[iv + 1:]


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)


off, wl, vad, al = 0.0, [], [], []
for k, p in enumerate(apart):
    f, lo, hi = p.split(":"); lo, hi = float(lo), float(hi)
    out = M / f"dpa-{name}-{k}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(lo), "-t", str(hi - lo), "-i", str(D / f"src/{f}.mp4"), "-vn",
                    "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", str(out)], check=True)
    d = dur(out)
    print(f"audio {k}: {f} {lo}-{hi} -> {off:.3f}-{off + d:.3f}")
    for src in [M / f"wl-{f}.txt"] + ([M / f"wl2-{f}.txt"] if f in W2 else []):
        cut0, cut1 = (W2[f], 1e9) if (f in W2 and src.name.startswith("wl-")) else (-1, W2.get(f, 1e9))
        for line in src.read_text().splitlines():
            ws = []
            for w, s, e in re.findall(r"(\S+?)\[([\d.]+)-([\d.]+)\]", line):
                s, e = float(s), float(e)
                if lo <= s and e <= hi + 0.2 and cut0 <= s < cut1 and not w.startswith("Terima") and w not in ("kasih", "kerana", "menonton!", "menonton."):
                    ws.append(f"{w}[{s - lo + off:.2f}-{min(e, hi) - lo + off:.2f}]")
            if ws: wl.append((float(re.search(r"\[([\d.]+)", ws[0]).group(1)), " ".join(ws)))
    for line in (M / f"vad-{f}.txt").read_text().split():
        a, c = map(float, line.split("-"))
        if c > lo and a < hi:
            vad.append(f"{max(a, lo) - lo + off:.2f}-{min(c, hi) - lo + off:.2f}")
    al.append(f"file '{out}'"); off += d
total = off
vl, voff = [], 0.0
for k, p in enumerate(vpart):
    f, lo, hi = p.split(":"); lo, hi = float(lo), float(hi)
    out = M / f"dpv-{name}-{k}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(lo), "-t", str(hi - lo), "-i", str(D / f"src/{f}.mp4"), "-an",
                    "-vf", "scale=1080:1920,setsar=1,fps=60", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-g", "30", str(out)], check=True)
    vl.append(f"file '{out}'"); voff += dur(out)
    print(f"video {k}: {f} {lo}-{hi}")
assert voff >= total - 0.05, f"picture {voff:.2f} s shorter than speech {total:.2f} s"
(M / f"dla-{name}.txt").write_text("\n".join(al) + "\n")
(M / f"dlv-{name}.txt").write_text("\n".join(vl) + "\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(M / f"dlv-{name}.txt"),
                "-f", "concat", "-safe", "0", "-i", str(M / f"dla-{name}.txt"), "-map", "0:v", "-map", "1:a", "-t", f"{total:.3f}",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", str(M / f"combo-{name}.mp4")], check=True)
for f in list(M.glob(f"dpa-{name}-*")) + list(M.glob(f"dpv-{name}-*")):
    f.unlink()
(M / f"wl-combo-{name}.txt").write_text("\n".join(l for _, l in sorted(wl)) + "\n")
(M / f"vad-combo-{name}.txt").write_text("\n".join(vad) + "\n")
(M / f"combo-{name}.log").write_text(f"total {total:.3f}\n")
print("total", round(total, 3))
