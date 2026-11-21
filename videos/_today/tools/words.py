"""Prints a built project's caption words with occurrence numbers (for fx anchors): python3 words.py <slug>"""
import json, sys, re, collections
t = json.load(open(f"/home/user/Content-Claude/videos/{sys.argv[1]}/data/transcript-a.json"))
c = collections.Counter(); out = []
for w in t:
    k = re.sub(r"[.,?!&]", "", w["w"].lower()); c[k] += 1
    out.append(f"{w['w']}#{c[k]}@{w['s']:.1f}")
print(" ".join(out))
