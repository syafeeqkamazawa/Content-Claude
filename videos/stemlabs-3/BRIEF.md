# StemLabs Fish Oil #3: A-roll and B-roll review, with moving overlays

- **A-roll:** the owner holding the bottle (VID_20261016_231703, Drive 15s_zXSp…). The front camera saved it mirrored; it is flipped back in CSS.
- **Script:** the recording is a single clean take, with only hesitations cut.
  - hook: everyone takes fish oil, but what does omega-3 actually do?
  - good fats when you rarely eat fish;
  - EPA and DHA;
  - EPA for the heart, DHA for brain function and the eyes;
  - more important with age;
  - StemLabs Fish Oil double strength gives EPA and DHA in one capsule;
  - add it to your daily routine;
  - CTA.
- **B-roll:** both clips have been used before (see `data/edl.json` `_note`), so only the unused parts are taken.
  - VID_20261013_180342: the bottle on the grass, used before in stemlabs-omega3.
  - VID_20261014_153135: the fish-oil part, used before in stemlabs-2.
- **Moving overlays** (new standing style): `tools/plx.sh` cuts out the person in each AI photo and fills the gap in the background with a soft blur. `tools/build.py` then moves the background and the cut-out at different speeds. Photos with no person get a camera pan.
- **No background music** (standing rule). Light SFX on titles and cutaways.
- **AI photos:** a family eating fish, a morning walk, a student, a woman reading, grandparents with a grandchild, a man taking a capsule at breakfast. All are full-screen, realistic, aurat covered and tagged "ILUSTRASI AI".
- **Rebuild:** `python3 tools/build.py`. Images: `tools/gen.sh [names…]`, then `tools/plx.sh [names…]`.
