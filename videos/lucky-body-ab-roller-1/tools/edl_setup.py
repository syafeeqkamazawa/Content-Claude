"""EDL for lucky-body-ab-roller-1 (11 Nov). Run tools/prep.py first (assets/a.mp4 + data/timeline.json)."""
import json, pathlib, re, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, ph, kp, write

T = json.loads((P / 'data/timeline.json').read_text())
L = T["lines"]

# word times (whisper large-v3-turbo) mapped onto the edit timeline
def words(path, offset=0.0):
    out = []
    if (P / path).exists():
        for line in (P / path).read_text().splitlines():
            for w, s, e in re.findall(r'(\S+?)\[([\d.]+)-([\d.]+)\]', line):
                out.append((w, float(s) + offset, float(e) + offset))
    return out
src_words = {"voice": words(".media/wl-voice.txt"), "v172759": words(".media/wl-hook.txt", 6.5)}
tr = []
for lid, d in L.items():
    for w, s, e in src_words[d["src"]]:
        if d["s0"] <= s < d["s1"] and e - s < 2.0:
            tr.append({"w": w, "s": round(d["e0"] + s - d["s0"], 3), "e": round(d["e0"] + min(e, d["s1"]) - d["s0"], 3)})
if tr:
    (P / 'data/transcript-a.json').write_text(json.dumps(tr, ensure_ascii=False))
TR = (P / 'data/transcript-a.json').read_text()

NOTES = {"H": "HOOK — the owner on camera (his own audio, VID_20261111_172759 7.4-12.6)", "L6": "take 2 (take 1 stops at 'masa kita buat')",
         "L10": "'pad siku' (heard as 'peksiku'); two false starts before it dropped", "L13": "clean take after two stumbles",
         "L14": "CTA — the take that names the yellow bag", "L15": "CTA"}
segs = [seg(lid, d["e0"], d["e1"], d["text"], NOTES.get(lid, "")) for lid, d in L.items()]
write(P, 1, "montage (tools/prep.py)", segs, zoom=1.0, origin="50% 50%",
      photos=[ph("pemakanan", ["L3", "pemakanan"], ["L3", "keseluruhan"], "AI (reused from jus-gout-7): healthy home meal, hands only"),
              ph("senaman", ["L3", "keseluruhan"], ["L3", "end"], "AI (reused from stemlabs-5): man brisk-walking in a park, long sleeves + long trousers; woman behind in hijab")],
      kps=[kp("LEMAK PERUT TAK HILANG?", ["PERUT"], ["H", "start"], ["H", "end"], "rise", 230, 100),
           kp("LATIH OTOT CORE", ["CORE"], ["L2", "melatih"], ["L2", "end"], "zoom", 230, 112),
           kp("LUCKY BODY AB ROLLER", ["LUCKY", "BODY"], ["L5", "start"], ["L5", "end"], "slam", 230, 100),
           kp("4 RODA, TAPAK LEBAR", ["4", "RODA,"], ["L6", "empat"], ["L6", "kestabilan"], "rise", 230, 104),
           kp("PAD SIKU 12MM", ["12MM"], ["L10", "pad"], ["L10", "dan"], "zoom", 230, 116),
           kp("AUTO REBOUND", ["REBOUND"], ["L10", "auto"], ["L10", "end"], "slide", 230, 116),
           kp("KONSISTEN", ["KONSISTEN"], ["L12", "konsisten"], ["L12", "ini"], "split", 230, 120),
           kp("TENGAH PROMO", ["PROMO"], ["L15", "promo"], ["L15", "end"], "slam", 230, 120)],
      note_extra=" Lucky Body Ab Roller (owner sent the clips + a voiceover, no other instructions): the 11 Nov rules apply — screenshot caption, complete sentences ~0.6 s apart, overlays only on the key points, close-ups of the product when a feature is named.")
(P / 'data/transcript-a.json').write_text(TR)
e = json.loads((P / 'data/edl.json').read_text())
e["_note"] = ("Lucky Body Ab Roller #1 — voiceover edit. assets/a.mp4 is built by tools/prep.py: the owner's on-camera hook "
              "(VID_20261111_172759) + the best take of each voiceover line (Recorder 20261111-1731), ~0.6 s apart, over a montage "
              "of VID_20261111_172759 (unboxing, rolling, product to camera) and VID_20261111_173042 (rolling with his daughter on "
              "his back). Dropped: " + T["dropped"] + ". Features (4 wheels, 12 mm elbow pads, auto rebound) are the owner's own "
              "words and match the product page; no price.")
e["theme"] = {"key": "#FF8A1F", "brand": "#FFFFFF"}
e["brand_words"] = ["lucky", "body"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
