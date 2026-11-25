"""Join ranges of several clips into one virtual source so make.py (single source) can cut it.
python3 combo.py NAME id:lo:hi[:b] ...   (":b" = B-roll only: its speech is left out of the word list / VAD)
Writes .media/combo-NAME.mp4, wl-combo-NAME.txt, vad-combo-NAME.txt and prints each part's offset."""
import re, subprocess, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
M = D / ".media"
W2 = {}
name, parts = sys.argv[1], sys.argv[2:]
off, wl, vad, lst = 0.0, [], [], []
for k, p in enumerate(parts):
    f, lo, hi, *fl = p.split(":"); lo, hi = float(lo), float(hi); b = bool(fl)
    out = M / f"cpart-{name}-{k}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(lo), "-t", str(hi - lo), "-i", str(D / f"src/{f}.mp4"),
                    "-vf", "scale=1080:1920,setsar=1,fps=60", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-g", "30",
                    "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-ac", "2", str(out)], check=True)
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)],
                             capture_output=True, text=True).stdout)
    print(f"part {k}: {f} {lo}-{hi} -> {off:.3f}-{off + d:.3f}{' (B-roll)' if b else ''}")
    if not b:
        for src in [M / f"wl-{f}.txt"] + ([M / f"wl2-{f}.txt"] if f in W2 else []):
            cut0, cut1 = (W2[f], 1e9) if (f in W2 and src.name.startswith("wl-")) else (-1, W2.get(f, 1e9))
            for line in src.read_text().splitlines():
                ws = []
                for w, s, e in re.findall(r"(\S+?)\[([\d.]+)-([\d.]+)\]", line):
                    s, e = float(s), float(e)
                    if lo <= s and e <= hi + 0.2 and cut0 <= s < cut1 and not w.startswith("Terima") and w not in ("kasih", "kerana", "menonton!"):
                        ws.append(f"{w}[{s - lo + off:.2f}-{min(e, hi) - lo + off:.2f}]")
                if ws: wl.append((float(re.search(r"\[([\d.]+)", ws[0]).group(1)), " ".join(ws)))
        for line in (M / f"vad-{f}.txt").read_text().split():
            a, c = map(float, line.split("-"))
            if c > lo and a < hi:
                vad.append(f"{max(a, lo) - lo + off:.2f}-{min(c, hi) - lo + off:.2f}")
    lst.append(f"file '{out}'"); off += d
(M / f"clist-{name}.txt").write_text("\n".join(lst) + "\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(M / f"clist-{name}.txt"), "-c", "copy",
                str(M / f"combo-{name}.mp4")], check=True)
for k in range(len(parts)): (M / f"cpart-{name}-{k}.mp4").unlink()
(M / f"wl-combo-{name}.txt").write_text("\n".join(l for _, l in sorted(wl)) + "\n")
(M / f"vad-combo-{name}.txt").write_text("\n".join(vad) + "\n")
print("total", round(off, 3))
