#!/bin/bash
# Generates the AI cutaways for VTEAY Fish Oil #3 (owner's ChatGPT/Codex account). Run from the project root.
# Subjects follow the owner's overlay reference (video rujukan.mp4 (Krill)); every person covers aurat.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, cinematic, natural light, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
gen () {
  name=$1; shift
  for i in 1 2 3 4; do
    out=$(timeout 900 npx --yes hyperframes@0.8.149 media-use resolve --type image --provider codex --intent "$1 $MOD" --project . --json 2>&1 | grep -v UNDICI | grep -v trace-warn | tail -40)
    echo "== $name try $i"; echo "$out" | tail -2 | cut -c1-200
    p=$(echo "$out" | grep -o '"path": *"[^"]*"' | head -1 | sed 's/.*"\(.media[^"]*\)"/\1/')
    if [ -n "$p" ] && [ -f "$p" ]; then echo "$name $p" >> .media/gen-map.txt; return; fi
    sleep 25
  done
}
[ $# -gt 0 ] && ONLY=" $* " || ONLY=""
want () { [ -z "$ONLY" ] || [[ "$ONLY" == *" $1 "* ]]; }

NOPPL="No people anywhere in the frame, no hands, no faces."
PLAIN="No brand names, no logos, no readable text."
want x_lutut && gen x_lutut "Side view of a human knee joint, bones and cartilage glowing, Medical 3D x-ray hologram style render, glowing translucent blue body on a dark navy background, anatomically accurate, cinematic. $NOPPL $PLAIN"
want x_darah && gen x_darah "Close-up of a network of human blood vessels and arteries with red blood flowing, Medical 3D x-ray hologram style render, glowing translucent blue body on a dark navy background, anatomically accurate, cinematic. $NOPPL $PLAIN"
want telan && gen telan "Close-up of a hand in a long-sleeved navy shirt holding one golden translucent fish oil softgel capsule above a glass of water on a bright kitchen table, morning light, shallow depth of field. Only the hand and sleeved forearm visible, no face. $PLAIN"
echo DONE
