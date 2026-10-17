# Infinity Probiotics Plus #2 — A-roll + B-roll review

- A-roll: new recording (17 Oct, VID_20261017_000733, Drive 1p8GA003…), owner holding the box/bottle; front camera so mirrored back in CSS. One take, already hook-first ("Ramai orang risau pasal jantung… usus kita sendiri") — only pauses trimmed. Audio is gated, so caption timing comes from speech islands (`data/transcript-a.json` is empty on purpose).
- B-roll: box/bottle/capsules (Drive 13weypVw…), the same clip as videos/infinity-probiotics-plus — only ranges #1 did not use (see `data/edl.json` `_note`).
- Product wording is only what the owner says: probiotics = good bacteria that help support the balance of gut bacteria; looking after the gut supports digestion; one option to complete a daily health routine. (No halal/KKM/sales claims this time — the owner did not say them.)
- New look vs #1: deep-blue title panel with light-blue rule; seven new AI photos (blood-pressure check, gut model, bloating, ignoring discomfort at work, probiotic micrograph, family breakfast, busy mother). No background music; overlays move (parallax).
- Rebuild: `python3 tools/build.py`; images: `tools/gen.sh [names…]` then `tools/plx.sh [names…]`.
