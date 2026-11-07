#!/bin/bash
# Generates the AI cutaways for Set Pisau Dessini #3 (owner's ChatGPT/Codex account). Run from the project root.
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
HANDS="Only two hands visible, wearing long sleeves down to the wrists; no face, no other body parts."
want ikan && gen ikan "Close-up of a stainless steel knife cutting a fresh whole fish and chicken pieces on a wooden chopping board in a Malaysian home kitchen. $HANDS $PLAIN"
want gunting && gen gunting "Close-up of stainless steel kitchen scissors snipping fresh lemongrass and spring onions over a bowl, Malaysian kitchen counter. $HANDS $PLAIN"
want hadiah && gen hadiah "A neatly wrapped gift box with a satin ribbon and a small blank card on a dining table in a warm Malaysian home, soft festive light. No knives, no kitchen tools. $NOPPL $PLAIN"
echo DONE
