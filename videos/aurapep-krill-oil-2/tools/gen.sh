#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #2 (owner's ChatGPT/Codex account). Run from the project root.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, natural light, candid lifestyle photography, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
PPL="Everyone is modestly dressed with full aurat coverage (no shorts, no bare arms or legs). Malaysian Malay people."
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

want pinggan && gen pinggan "A Malay man in his fifties in a long-sleeved shirt sitting alone at a home dining table, looking thoughtfully at his plate of white rice, fried chicken and very few vegetables, wondering if it is healthy enough, evening light, shallow depth of field. $PPL"
want fishoil && gen fishoil "Close-up food photograph of golden translucent fish oil softgel capsules spilling from a plain unlabeled glass jar onto a wooden board next to a fresh whole mackerel on crushed ice and a lemon wedge, bright natural light, no people, no text, no labels."
want krill && gen krill "Underwater macro photograph of a dense swarm of Antarctic krill, small translucent pinkish-orange crustaceans glowing in cold deep blue ocean water with shafts of sunlight from the surface, National Geographic style, no people, no text."
want jalan && gen jalan "A fit Malay man in his fifties brisk walking on a park jogging track in the early morning, wearing a long-sleeved sports top, long loose track pants down to the ankle and running shoes, smiling, energetic, green trees and soft golden sunrise light. $PPL"
want baca && gen baca "A Malay woman in her fifties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung, reading a book by a bright window at home without glasses, focused and alert, soft morning light, calm atmosphere. $PPL"
want ibubapa && gen ibubapa "An elderly Malay couple sitting together on a sofa at home smiling warmly at the camera: the mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung, the father in a kopiah, long-sleeved baju melayu and long trousers to the ankle, their adult son in a long-sleeved shirt and long trousers and adult daughter in a hijab and loose long dress sitting beside them, warm afternoon light. $PPL"
want keluarga && gen keluarga "Three generations of a Malay family walking together in a green park at sunset seen from the front, holding hands and laughing: grandparents (grandmother in a hijab covering her hair, neck and chest and a loose long dress, grandfather in a kopiah, long-sleeved shirt and long trousers), parents (mother in hijab and loose long dress, father in long-sleeved shirt and long trousers) and two young children in long sleeves and long pants, the girl in a small hijab. $PPL"
echo DONE
