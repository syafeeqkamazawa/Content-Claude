#!/bin/bash
# Generates the AI cutaways for Lab Biotix Triple Biotix #3 (owner, 14 Nov: "Overlay visual ai realistik bila perlu"). Run from the
# project root. Realistic only; every person covers aurat; the product itself is never generated (real B-roll shows it).
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
AURAT_M="The man is a Malay Muslim wearing a loose long-sleeved shirt and loose long trousers down to the ankles, fully covered, no shorts, no bare skin except face, hands and feet."
want A1 && gen A1 "A fit Malaysian man in his early forties jogging along a green park path on a bright morning, relaxed and healthy, medium-wide shot. $AURAT_M $PLAIN"
want A2 && gen A2 "A busy Malaysian night market food stall with trendy unusual street food: colourful skewers, cheese-pulled snacks, bright drinks, a Malaysian man holding a viral snack and smiling, warm lights, medium shot. $AURAT_M $PLAIN"
want A3 && gen A3 "A late-night table full of fast food: fried chicken, burgers, fries, instant noodles and sugary soft drinks, messy and greasy, warm lamp light, overhead angle. $NOPPL $PLAIN"
want A4 && gen A4 "Close-up of fresh mixed berries, strawberries, blueberries, raspberries and blackberries, next to small glossy purple fruit jelly cubes on a white plate, soft daylight, shallow depth of field. $NOPPL $PLAIN"
echo DONE
