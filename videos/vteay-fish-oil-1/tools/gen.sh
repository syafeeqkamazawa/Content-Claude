#!/bin/bash
# Generates the AI cutaways for VTEAY Omega-3 Fish Oil #1 (owner's ChatGPT/Codex account). Run from the project root.
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
MAN="A Malay man in his thirties fully clothed in a long-sleeved shirt and long trousers to the ankle."
XR="Cinematic 3D medical render, translucent glowing blue x-ray human figure on a dark navy background, no text, no labels."
want rak && gen rak "A pharmacy shelf with rows of plain white and amber supplement bottles, a hand in a long sleeve picking one up to read the back label, shallow depth of field. $PLAIN"
want softgel && gen softgel "Extreme macro of golden translucent fish oil softgel capsules on a white surface, soft studio light, shallow depth of field. $NOPPL $PLAIN"
want x_jantung && gen x_jantung "$XR Translucent human chest with a detailed red heart and glowing blood vessels."
want x_saraf && gen x_saraf "$XR Close-up of a translucent human head and upper chest with the nervous system glowing orange."
want x_otak && gen x_otak "$XR Close-up of a translucent human head with a detailed pink brain glowing inside."
want fokus && gen fokus "$MAN He is sitting at a desk with a laptop, focused and alert, warm window light, cinematic. No logos."
echo DONE
