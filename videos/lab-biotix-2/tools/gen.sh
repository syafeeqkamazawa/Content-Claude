#!/bin/bash
# Generates the AI cutaways for Lab Biotix Triple Biotix #2 (owner, 14 Nov: "Ada juga overlay visual"). Run from the
# project root. Realistic only; every person covers aurat; no brand names (the product itself is shown with real photos).
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
want kembung && gen kembung "A Malaysian man sitting at a dining table after a big meal at home, one hand resting on his stomach, looking uncomfortable and full, empty plates in front of him, warm evening light, medium shot. $AURAT_M $PLAIN"
want kapsul && gen kapsul "Close-up still life on a white kitchen counter: a pile of plain white supplement capsules beside a spoon of plain powder and a glass of water with powder being stirred in, soft daylight. $NOPPL $PLAIN"
want buah && gen buah "Close-up of fresh mixed berries, strawberries, blueberries, raspberries and blackberries, next to small glossy purple fruit jelly cubes on a white plate, soft daylight, shallow depth of field. $NOPPL $PLAIN"
want kerja && gen kerja "A Malaysian man at an office desk with a laptop, putting a small slim sachet into the pocket of his work bag, bright modern office, medium shot. $AURAT_M $PLAIN"
want travel && gen travel "A Malaysian man walking through a bright airport terminal pulling a carry-on suitcase, a backpack on his shoulder, morning light through big windows, full body shot. $AURAT_M $PLAIN"
echo DONE
