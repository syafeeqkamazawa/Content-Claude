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
  `videos/jus-gout-6/tools/build.py` (section 5, `brand_words` in the EDL).
- **No other on-screen text panels** (owner, 21 Oct: "Caption lama dah boleh
  buang ya untuk content ni dan seterusnya, gunakan caption style yang baru
  sahaja"): no key-point title boxes — the flap board is the only text.
- **No "TEKAN BEG KUNING" button either** (owner, 22 Oct: "Lepas ni butang
  kuning Tekan beg kuning pun tak perlu ada dah"): EDL `titles` is empty.
- **More overlays** (owner, 22 Oct: "banyakkan overlay yang sesuai"): cover
  most of each sentence with a fitting full-screen cutaway — B-roll or a
  realistic AI photo — and keep the face on camera mainly for the hook and
  short beats in between.
- **Board moves, never covers the face or the product** (owner, 22 Oct:
  "caption pastikan tak menutup wajah dan produk, tak perlu stay di satu
  tempat sahaja"): the board jumps to a new height (150 / 430 / 720 / 1010 /
  1300 px top) whenever the current spot would hide a face (YuNet,
  `tools-shared/face_yunet.onnx`) or the subject/product (remove-background
  mask). Run `python3 tools/flap_place.py` after the edit and photos are
  final; needs `pip install opencv-python-headless`.
- **Reference motion, no hanging** (owner, 21 Oct, Krill #2: "Caption tak nak
  style gantung dah. Buat motion dia sebijik macam video rujukan tu … konsep
  pergerakan tu"): no strings, no swing. Copy the reference's whole concept:
  the board ghosts in (blur + fade); in the hook two rows alternate phrase by
  phrase; then the board drops to one row, a prompt bar under it types the
  spoken words with a blinking amber cursor, and a status panel drops in and
  ticks the key points (EDL `panel`) STANDBY → RUNNING → DONE with a running
  T+ timer. Board and panel ghost-jump (blur out, blur in) when they must
  move; the panel ghosts out if there is no clear spot. Template:
  `videos/aurapep-krill-oil-2/` (build.py section 5, flap_place.py).
- Older videos (before 21 Oct) used softer sentence-case captions in Plus
  Jakarta Sans at about 56px; don't go back to that unless the owner asks.

## Workflow

- Transcribe first, cut repeated takes / false starts / long pauses, put the
  strongest hook first.
- **No draft step** (owner, 19 Oct: "Lepas ni terus render final"): check the
  edit yourself with snapshots, then render the final straight away and send it.
- **Batch folders** (owner, 22 Oct): a folder may hold several talking clips
  (e.g. 5) mixed with usage clips and product close-ups. Make one video per
  talking clip, all in one go. **Every clip in the folder must be used**, and
  **no clip appears in two videos** — except a long clip may be cut into
  different, non-overlapping parts for different videos ("Boleh potong").
  Keep a clip → video table in each EDL `_note` and check nothing is left
  out; send each final as soon as it is done.
- Media of finished projects (sources, transcoded assets, renders — all
  git-ignored, originals on Drive) may be deleted to free disk (owner, 22 Oct).

## Audio

- **No background music** (owner, 15 Oct: "Mulai sekarang tak perlu letak
  background music"). Voice only, plus light SFX where the edit has overlays.
- **Phone-mic recordings get a mic-like voice** (owner, 21 Oct: "saya lupa
  pakai mic … bagi audio nice ya macam pakai mic juga"): run
  `tools/voice.sh assets/a.mp4 [noise_start noise_end]` (template:
  `videos/aurapep-krill-oil-2/`) before building — denoise from a quiet
  stretch, cut room boxiness, warmth + presence EQ, de-ess, compressor,
  light expander, −15 LUFS. Do it whenever the owner says the mic was off.
