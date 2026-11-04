#!/bin/bash
# Generates the AI cutaways for Infinity Probiotics Plus #4 (owner's ChatGPT/Codex account). Run from the project root.
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

MEN="A Malay man in his thirties, fully clothed in a long-sleeved shirt and long trousers to the ankle (no bare skin except face, neck and hands)."
NOPPL="No people anywhere in the frame, no hands, no faces."
want stres && gen stres "A Malay man in his thirties in a long-sleeved shirt and long trousers sitting up in bed at night unable to sleep, holding his head, stressed, phone glowing on the bedside table, moody cinematic blue light. $MEN"
want sembelit && gen sembelit "A Malay man in his thirties in a long-sleeved t-shirt and long trousers standing outside a bathroom door at home, one hand on his lower belly, uncomfortable constipated expression, soft morning light. $MEN"
want antibiotik && gen antibiotik "Close-up of blister packs of white antibiotic capsules and a plain amber pharmacy pill bottle on a white table, soft clinical light, no readable text, no labels. $NOPPL"
echo DONE
