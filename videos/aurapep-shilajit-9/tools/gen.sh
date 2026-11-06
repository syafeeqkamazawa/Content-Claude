#!/bin/bash
# Generates the AI cutaways for Aurapep Shilajit #9 (owner's ChatGPT/Codex account). Run from the project root.
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
HANDS="Only one hand visible, wearing a long sleeve down to the wrist; no face, no other body parts."
want rak && gen rak "A pharmacy shelf in Malaysia crowded with many different plain unbranded supplement bottles and boxes, shallow depth of field, bright retail light. $NOPPL $PLAIN"
want ganoderma && gen ganoderma "Dried ganoderma (lingzhi) mushroom slices and a whole glossy red-brown ganoderma cap on a dark slate surface, moody side light. $NOPPL $PLAIN"
want dos && gen dos "Close-up of an open palm holding a single plain tablet beside a glass of water on a breakfast table in the morning, soft daylight. $HANDS $PLAIN"
echo DONE
