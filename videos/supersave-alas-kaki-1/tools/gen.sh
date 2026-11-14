#!/bin/bash
# Generates the AI cutaways for SuperSave Alas Kaki Dapur #1 (owner, 14 Nov: "Overlay visual ai realistik bila perlu"). Run from the
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
AURAT_F="Every woman wears a hijab covering her hair, neck and chest and a loose long baju kurung covering the whole body except face and hands."
AURAT_MM="Every man wears a loose long-sleeved baju melayu with long trousers to the ankle and a songkok, fully covered."
want A1 && gen A1 "A Malay family welcoming relatives at the front door of a decorated Malaysian terrace house on Hari Raya morning, warm smiles, pelita lights and ketupat decorations, medium shot. $AURAT_F $AURAT_MM $PLAIN"
want A2 && gen A2 "A freshly decorated Malaysian living room ready for Hari Raya: new elegant curtains, neat sofa with new cushion covers, ketupat ornaments, warm morning light, wide shot. $NOPPL $PLAIN"
want A3 && gen A3 "Close-up of an old, faded, worn and damp plain beige kitchen floor mat in front of a kitchen sink, frayed edges, water stains, a slightly dingy look, soft daylight. $NOPPL $PLAIN"
want A4 && gen A4 "A clean bright modern Malaysian kitchen freshly made over for Hari Raya, white cabinets, tidy counter with a jar of kuih raya and a small ketupat decoration, plain tiled floor, morning light, wide shot. $NOPPL $PLAIN"
echo DONE
