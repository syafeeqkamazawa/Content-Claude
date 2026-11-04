#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #10 (owner's ChatGPT/Codex account). Run from the project root.
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

MEN="A Malay man in his forties, fully clothed in a long-sleeved shirt and long trousers to the ankle (no bare skin except face, neck and hands)."
NOPPL="No people anywhere in the frame, no hands, no faces."
XR="Cinematic 3D medical render, translucent glowing blue x-ray human figure on a dark navy background, no text, no labels."
want x_badan && gen x_badan "$XR Full translucent human body standing, front view, softly glowing skeleton and organs."
want x_otak && gen x_otak "$XR Close-up of a translucent human head with a detailed pink brain glowing inside."
want x_mata && gen x_mata "$XR Close-up of the human brain and both eyeballs with glowing blue nerve connections between them."
want x_jantung && gen x_jantung "$XR Translucent human chest with a detailed red beating heart and glowing blood vessels."
want x_saraf && gen x_saraf "$XR Translucent human body with the whole nervous system glowing bright orange from the brain down the spine to the arms and legs."
want kebas && gen kebas "Close-up of the hands of a Malay man in his forties in a long-sleeved shirt, rubbing his numb tingling fingers and palm, soft window light, shallow depth of field. $MEN"
want lutut && gen lutut "A Malay man in his forties in a long-sleeved shirt and long trousers sitting on the edge of a sofa, holding his aching knee with both hands over his trousers, grimacing, warm home light. $MEN"
want ikan && gen ikan "Extreme macro of many glossy golden yellow fish oil softgel capsules piled together, soft blue background bokeh, studio lighting. $NOPPL"
want sendawa && gen sendawa "A Malay man in his forties in a long-sleeved shirt at a kitchen table, hand over his mouth, uncomfortable after swallowing a fish oil capsule, a glass of water in front of him. $MEN"
echo DONE
