"""Lists the pool ranges each built Shilajit video plays (from its index.html) and flags overlaps."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
used = []
for n in range(2, 7):
    html = (ROOT / f"aurapep-shilajit-{n}/index.html").read_text()
    for tag in re.findall(r"<video[^>]*src=\"assets/b\.mp4\"[^>]*>", html):
        a = float(re.search(r'data-media-start="([\d.]+)"', tag).group(1))
        d = float(re.search(r'data-duration="([\d.]+)"', tag).group(1))
        used.append((a, a + d, n))
used.sort()
for a, b, n in used:
    print(f"#{n}  {a:6.2f}-{b:6.2f}")
bad = [(x, y) for i, x in enumerate(used) for y in used[i + 1:] if y[0] < x[1] - 0.01 and x[2] != y[2]]
print("OVERLAPS:", bad if bad else "none")
