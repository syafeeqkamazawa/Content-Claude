#!/bin/bash
# Generates the AI cutaways for Periuk nasi Giselle #2 (owner's ChatGPT/Codex account). Run from the project root.
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
want piknik && gen piknik "A family picnic set-up on a woven mat under a shady tree in a green Malaysian park: lunch boxes of white rice and lauk, a thermos and fruit, warm afternoon light. $NOPPL $PLAIN"
want sotong && gen sotong "Close-up of a plate of hot steaming white rice with Malaysian sambal sotong (squid in red chilli sambal) on a home dining table, appetising, steam rising. $NOPPL $PLAIN"
want kampung && gen kampung "A traditional Malay kampung-style dining spread on a wooden table in a rustic open-air restaurant: white rice, gulai, sambal, ulam and fried fish on banana leaves, warm evening light. $NOPPL $PLAIN"
echo DONE
