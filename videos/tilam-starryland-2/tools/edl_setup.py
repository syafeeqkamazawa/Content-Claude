"""EDL for tilam-starryland-2 (Starryland Back-Wave voiceover, 11 Nov).

Run tools/prep.py first: it builds assets/a.mp4 (montage of the owner's footage + the voiceover
with ~0.6 s between sentences) and data/timeline.json (where each sentence starts)."""
import json, pathlib, sys
P = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(P / 'tools'))
from kb2 import seg, ph, kp, write

L = json.loads((P / 'data/timeline.json').read_text())
E = L["lines_edit"] + [L["total"]]
TEXT = [
    ("Weh, kalau tilam rumah korang dah lama, lembek, tidur pun rasa tak selesa, mungkin dah sampai masa tukar.", "HOOK — problem; AI photo of a man who can't sleep"),
    ("Korang tengok Starryland Back-Wave ni, tebal 10 inci tau, tapi yang bestnya, tilam ni datang bergulung dalam kotak tau.", "names per the owner's product info (voice sounds like 'Starryland Back-Wave')"),
    ("Bila buka plastik, dia akan mengembang sampai jadi tilam.", "old TikTok clip, unrolling fast-forward"),
    ("Dalam dia ada TechFlex pocket spring untuk sokongan badan tau.", ""),
    ("Cloud Motion Foam bagi rasa lebih selesa dengan 3D mesh fabric yang bantu pengudaraan.", "'Cloud Motion Foam' as heard (whisper agrees across settings)"),
    ("Lagi satu, ada pilihan size, single sampai king.", ""),
    ("Kalau dah lama pula nak tukar tilam tu, cuba tengok harga dekat beg kuning.", "CTA"),
    ("Seller tengah buat promo tau, memang berbaloi grab sekarang.", "CTA"),
]
segs = [seg(f"S{k+1}", round(E[k], 3), round(E[k + 1], 3), t, n) for k, (t, n) in enumerate(TEXT)]
tr = (P / 'data/transcript-a.json').read_text()
write(P, 2, "montage (tools/prep.py)", segs, zoom=1.0, origin="50% 50%",
      photos=[ph("tidur", ["S1", "start"], ["S1", "mungkin"], "AI (reused from magnesium): man lying awake, covered by blanket, long sleeves"),
              ph("spring", ["S4", "start"], ["S4", "untuk"], "AI (from tilam-bed-wave): pocket-spring cross-section, no people")],
      kps=[kp("TILAM DAH LEMBEK?", ["LEMBEK?"], ["S1", "start"], ["S1", "mungkin"], "rise", 230, 104),
           kp("TEBAL 10 INCI", ["10", "INCI"], ["S2", "tebal"], ["S2", "tapi"], "zoom", 230, 120),
           kp("SAMPAI BERGULUNG", ["BERGULUNG"], ["S2", "tilam"], ["S2", "end"], "slide", 230, 104),
           kp("TECHFLEX POCKET SPRING", ["POCKET", "SPRING"], ["S4", "start"], ["S4", "end"], "rise", 230, 96),
           kp("3D MESH FABRIC", ["3D", "MESH"], ["S5", "dengan"], ["S5", "end"], "zoom", 230, 110),
           kp("SINGLE SAMPAI KING", ["SINGLE", "KING"], ["S6", "pilihan"], ["S6", "end"], "split", 230, 104),
           kp("TENGAH PROMO", ["PROMO"], ["S8", "promo"], ["S8", "end"], "slam", 230, 120)],
      note_extra=" Tilam (owner, 11 Nov): 'untuk Tilam pun sama, overlay yang perlu sahaja. Gunakan juga klip yang lama untuk overlay contoh tilam bergulung dan tengok lah mana yang perlu lagi.' Voiceover over the owner's footage; close-ups of the mattress (quilting, mesh side, hand press) whenever a feature is named.")
(P / 'data/transcript-a.json').write_text(tr)
e = json.loads((P / 'data/edl.json').read_text())
e["_note"] = ("Tilam Starryland Back-Wave #2 — voiceover edit. assets/a.mp4 is built by tools/prep.py: the voiceover src/voice.m4a "
              "(Recorder 20261111-1511) with silence added so sentences sit ~0.6 s apart, over a montage of VID_20261111_121807 "
              "(close-ups), VID_20261111_122144 (owner lying/sitting) and the old TikTok post 7694908315205192966 (rolled mattress, "
              "cropped below its title sticker). assets/b.mp4 = a.mp4 muted. Sizes, promo and features are the owner's own words; no price.")
e["theme"] = {"key": "#7FB8E6", "brand": "#FFFFFF"}
e["brand_words"] = ["starryland", "back-wave"]
(P / 'data/edl.json').write_text(json.dumps(e, indent=1, ensure_ascii=False))
