# Content-Claude — video editing preferences

Owner's standing instructions for every video edited in this repo (HyperFrames
projects live under `videos/<project>/`). Follow them unless the owner says
otherwise for a specific video.

## Overlays

- Visual overlays are **full-screen** cutaways (cover the whole 1080×1920
  frame) — not small cards or stickers beside the speaker.
- **Realistic visuals only.** No emoji, cartoon stickers or symbol icons.
- **Every person shown must fully cover aurat** (menutup aurat sempurna):
  - men: loose clothing from navel to below the knee at minimum — use long
    trousers to the ankle; no shorts, no bare torso;
  - women: hijab covering hair, neck and chest, loose clothing covering the
    whole body except face and hands.
  Check every generated or stock image for this before using it; regenerate
  anything that fails.
- **Overlays move** (owner, 16 Oct): AI photos are split into a cut-out
  subject and a background plate (`tools/plx.sh`, HyperFrames
  remove-background) and the two layers drift apart (2.5D parallax); photos
  with no subject get a camera pan. Real B-roll footage stays as video.
- AI-generated photos carry a small "ILUSTRASI AI" tag, and the owner should
  switch on TikTok's "AI-generated content" label when posting.

## Hero Hige (owner, 17 Oct — this product only)

- **No captions / subtitles.**
- Overlays are **only the key points**, as stylish moving text (zoom in / zoom
  out, slides, punches) — no AI photos.
- The clip of the owner using the product goes in the middle as a
  **fast-forward, full-screen overlay**.

## Captions

- **Split-flap "departure board" style** (owner, 21 Oct: "Caption style untuk
  content ini dan seterusnya gunakan style macam dalam video rujukan caption
  style" — reference in `videos/jus-gout-6/src/ref/`, Drive 1kmDeS6-…):
  two rows of dark flap tiles near the top of the frame, uppercase condensed
  letters (Barlow Condensed, OFL) that scramble left to right before settling;
  keywords in amber, brand names in coral, the rest white. Implemented in
  `videos/jus-gout-6/tools/build.py` (section 5, `brand_words` in the EDL);
  title panels sit below the board.
- Older videos (before 21 Oct) used softer sentence-case captions in Plus
  Jakarta Sans at about 56px; don't go back to that unless the owner asks.

## Workflow

- Transcribe first, cut repeated takes / false starts / long pauses, put the
  strongest hook first.
- **No draft step** (owner, 19 Oct: "Lepas ni terus render final"): check the
  edit yourself with snapshots, then render the final straight away and send it.

## Audio

- **No background music** (owner, 15 Oct: "Mulai sekarang tak perlu letak
  background music"). Voice only, plus light SFX where the edit has overlays.
