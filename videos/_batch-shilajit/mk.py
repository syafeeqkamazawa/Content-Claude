"""Shared EDL writer for the Shilajit batch: python3 mk.py <n> writes aurapep-shilajit-<n>/data/edl.json
from the spec in specs.py, copies the clip's transcript (with token fixes) and checks that every
segment's script word count matches the transcript (so caption timing follows the real words)."""
import json, pathlib, sys
from specs import SPECS, COMMON

ROOT = pathlib.Path(__file__).resolve().parent
n = int(sys.argv[1])
sp = SPECS[n]
proj = ROOT.parent / f"aurapep-shilajit-{n}"
tx = json.loads((ROOT / f"tx/{sp['clip']}.json").read_text())
# token fixes: (start time, [new tokens]) replaces the tokens starting at that time span
for t0, t1, toks in sp.get("fix", []):
    keep = [w for w in tx if not (t0 <= w["s"] < t1)]
    span = t1 - t0
    new = [dict(w=" " + tk, s=round(t0 + span * k / len(toks), 2), e=round(t0 + span * (k + 1) / len(toks), 2))
           for k, tk in enumerate(toks)]
    tx = sorted(keep + new, key=lambda w: w["s"])
for t0, t1, words in sp.get("fixw", []):  # exact re-transcribed words for a region
    tx = sorted([w for w in tx if not (t0 <= w["s"] < t1)] + [dict(w=" " + a, s=b, e=c) for a, b, c in words], key=lambda w: w["s"])
(proj / "data").mkdir(exist_ok=True)
(proj / "data/transcript-a.json").write_text(json.dumps(tx, ensure_ascii=False))
ok = True
for s in sp["segments"]:
    words = [w for w in tx if s["in"] - 0.05 <= w["s"] < s["out"] - 0.05]
    merged = []
    for w in words:
        if merged and w["w"].strip().startswith("-"):
            continue
        merged.append(w)
    if len(merged) != len(s["text"].split()):
        ok = False
        print(f"{s['id']}: transcript {len(merged)} vs text {len(s['text'].split())}: {' '.join(w['w'].strip() for w in merged)}")
edl = dict(COMMON)
edl.update({k: v for k, v in sp.items() if k not in ("clip", "fix", "fixw")})
(proj / "data/edl.json").write_text(json.dumps(edl, indent=1, ensure_ascii=False))
print("OK" if ok else "word-count mismatches above", proj.name)
