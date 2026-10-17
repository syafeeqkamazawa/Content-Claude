# Tiny Titanz Kid180 #2 — A-roll + B-roll review

- A-roll: new recording (17 Oct, VID_20261017_001504, Drive 1s06_37L…), owner holding the box; front camera so mirrored back in CSS. Hook first ("Pernah tak ibu ayah tengok anak orang lain makin tinggi…"). Dropped the muddled "senang untuk… jadikan mudah" (retaken cleanly) and the CTA false start "Kalau tengah cari,". Audio is gated, so caption timing comes from speech islands (`data/transcript-a.json` is empty on purpose).
- B-roll: box / bottle / tablets (Drive 1yeUjbM-…), the same clip as videos/titanz-kid180 — only ranges #1 did not use (see `data/edl.json` `_note`).
- Claims checked against the box front: "Tinggi kalsium — kalsium membantu dalam perkembangan tulang dan gigi yang kuat"; "Tablet kunyah beri biru, teh hijau dan vitamin C". Nothing else is claimed.
- New look vs #1: Kid180-yellow title panel with Titanz-green text and rule; eight new AI photos (kids comparing height, thoughtful mother, refusing vegetables, refusing milk, brushing teeth, blueberries/green tea/orange, breakfast before school, family walk). No background music; overlays move (parallax).
- Rebuild: `python3 tools/build.py`; images: `tools/gen.sh [names…]` then `tools/plx.sh [names…]`.
