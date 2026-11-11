---
workflow: general-video
flow: automation
message: "Tilam Starryland Back-Wave 10 inci — sampai bergulung, TechFlex pocket spring, 3D mesh, single–king, promo di beg kuning"
destination: tiktok
aspect: 1440x2560 @ 60 fps
language: ms
length: 38s
angle: voiceover-review
---

## Intent

Owner, 11 Nov: "Audio untuk Tilam dah masuk, untuk Tilam pun sama, overlay yang perlu sahaja. Gunakan juga
klip yang lama untuk overlay contoh tilam bergulung dan tengok lah mana yang perlu lagi." Same rules as
Frame Kaabah #6-#10: the 11 Nov screenshot caption (Rubik Mono One, size 62, top 1328), complete sentences
with ~0.5 s between them, overlays only on the important points, close-ups whenever a feature is named.

## Build

1. `python3 tools/prep.py` — voiceover (src/voice.m4a) with silence added between sentences (~0.6 s gaps),
   light clean-up to −15 LUFS, over a montage of the owner's clips → assets/a.mp4, data/timeline.json.
2. `python3 tools/edl_setup.py && python3 tools/build.py` — captions, key-point text, AI cut-aways.

## Sources (Drive, not in git; symlinked in src/)

- Recorder - 20261111-1511.m4a — voiceover
- VID_20261111_121807 — close-ups (edge, mesh side, quilting, hand press)
- VID_20261111_122144 — owner lying / sitting on the mattress
- TikDownloader 7694908315205192966 — the old post: rolled mattress in the corridor and unrolling (cropped
  below its title sticker)

## AI photos

- tidur — reused from magnesium (man lying awake, under a blanket, long sleeves)
- spring — reused from tilam-bed-wave (pocket-spring cross-section, no people)
New AI generation was not available (the image-generation CLI is not installed after the container restart).
