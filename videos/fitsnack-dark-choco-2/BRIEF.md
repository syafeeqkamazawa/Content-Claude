# Fitsnack Dark Chocolate Protein Bar #2 — voiceover edit

- Owner's voiceover ("Recorder - 20261021-1546.m4a") over full-screen cutaways for the whole runtime; assets/a.mp4 is a black placeholder carrying the voiceover so the shared build works. First take of "jadi kalau korang tengah cari snack…" dropped.
- B-roll VID_20261021_153646 (owner unboxing and eating the bar; saved mirrored, hflipped on transcode). Three AI cutaways (woman hesitating over chocolate, sugar cubes + dark chocolate, woman taking a snack bar at the office) with parallax and "ILUSTRASI AI" tags.
- First video with the moving split-flap board (owner, 22 Oct): `tools/flap_place.py` checks each caption's frame for faces (YuNet) and the subject/product (remove-background) and moves the hanging board to the clearest height; the board swings in on strings like the reference. No CTA button, no background music.
- Rebuild: `python3 tools/build.py`; after changing the edit run `python3 tools/flap_place.py`.
