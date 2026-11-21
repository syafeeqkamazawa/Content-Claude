"""Correct caption words of an already-built project (transcript-a.json + EDL segment text), then rebuild.
python3 fixcap.py SLUG '{"word": "new", "word#2": "new", "drop": ""}'   (exact token match, punctuation included; "" drops it)"""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).resolve().parents[2] / sys.argv[1]
rep = json.loads(sys.argv[2])
tr = json.loads((P / "data/transcript-a.json").read_text())
seen, out = {}, []
for w in tr:
    t = w["w"]; seen[t] = seen.get(t, 0) + 1
    key = f"{t}#{seen[t]}" if f"{t}#{seen[t]}" in rep else t
    if key in rep:
        if rep[key] == "":
            continue
        w["w"] = rep[key]
    out.append(w)
(P / "data/transcript-a.json").write_text(json.dumps(out, ensure_ascii=False))
e = json.loads((P / "data/edl.json").read_text())
for s in e["segments"]:
    s["text"] = " ".join(w["w"] for w in out if s["in"] - 0.15 <= w["s"] < s["out"] - 0.1) or "."
(P / "data/edl.json").write_text(json.dumps(e, indent=1, ensure_ascii=False))
r = subprocess.run(["python3", "tools/build.py"], cwd=P, capture_output=True, text=True)
print(" ".join(w["w"] for w in out)); print((r.stdout + r.stderr).strip().splitlines()[-1])
