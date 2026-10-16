# Promaxx Jus Gout #5 — A-roll + B-roll review

- A-roll: new recording (16 Oct, VID_20261016_230507, Drive 13QeNQ2H…), owner holding the jar; front camera so mirrored back in CSS. One clean take, already in the right order (hook first) — only pauses trimmed. The audio is gated (digital silence between phrases), so caption timing comes from speech islands (`data/transcript-a.json` is empty on purpose).
- B-roll: the drink being prepared (Drive 1MnocG_E…), the same clip used in videos/jus-gout (#1) and videos/jus-gout-4 — only ranges neither used (see `data/edl.json` `_note`).
- Product wording is only what the owner says: Jus Gout from Promaxx series, a supplementary drink, easy to prepare, part of a self-care routine, alongside watching diet, drinking enough water and monitoring uric acid ("ikhtiar").
- New look vs #1–#4: cream title panel, brown text, orange rule; seven new AI photos (night attack, swollen toe, doctor with foot X-ray, missing work, healthy meal, uric-acid meter, drinking water). No background music; overlays move (parallax).
- Rebuild: `python3 tools/build.py`; images: `tools/gen.sh [names…]` then `tools/plx.sh [names…]`.
