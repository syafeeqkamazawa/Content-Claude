#!/bin/bash
# Moving overlays (owner, 16 Oct: "overlay bergerak"): split each AI photo into a
# foreground cut-out (person / main subject) and a background plate whose subject
# area is filled with its surroundings (tools/plx_plate.py), so tools/build.py can move the two layers at
# different speeds (2.5D parallax). Photos with no detectable subject keep a
# single layer and get a camera pan instead. Run from the project root:
#   tools/plx.sh [names…]   (default: every assets/photos/*.jpg)
export NODE_USE_ENV_PROXY=1
cd assets/photos || exit 1
names="$*"; [ -z "$names" ] && names=$(ls *.jpg | grep -v -- '-bg.jpg' | sed 's/\.jpg$//')
for n in $names; do
  [ -f "$n.jpg" ] || continue
  timeout 900 npx --yes hyperframes@0.8.149 remove-background "$n.jpg" -o "$n-fg.png" >/dev/null 2>&1
  [ -f "$n-fg.png" ] || { echo "$n: no cut-out"; continue; }
  cover=$(ffmpeg -nostdin -v error -i "$n-fg.png" -vf "alphaextract,scale=108:192,format=gray" -f rawvideo - | python3 -c "import sys; b=sys.stdin.buffer.read(); print(round(sum(1 for x in b if x>128)/len(b),3))")
  if python3 -c "import sys; sys.exit(0 if 0.03 < $cover < 0.75 else 1)"; then
    python3 ../../tools/plx_plate.py "$n.jpg" "$n-fg.png" "$n-bg.jpg"
    echo "$n: layered (subject covers $cover of the frame)"
  else
    rm -f "$n-fg.png" "$n-bg.jpg"; echo "$n: single layer (cover $cover)"
  fi
done
