#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #6 (owner's ChatGPT/Codex account). Run from the project root.
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

SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, ceiling, sky or soft bokeh) with nothing important in it."
FEET="Every woman wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere."
want luaran && gen luaran "A stylish Malay man in his thirties in a long-sleeved shirt and long trousers styling his hair and spraying cologne in front of a mirror in a modern bedroom, seen from a little distance so he is in the lower half of the frame with a plain wall above. $SPACE $PPL"
want nutrisi && gen nutrisi "Food photograph on a light wooden table in the lower half of the frame: a grilled salmon fillet, a bowl of blueberries, boiled eggs, broccoli, walnuts and a carrot, bright soft daylight, plain light wall above, no people, no text, no labels. $SPACE"
want ibuayah && gen ibuayah "An elderly Malay couple sitting together in their garden on a bench under a frangipani tree, smiling: the mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung with socks, the father in a kopiah, long-sleeved baju melayu and long trousers to the ankle, seen from a distance so they sit in the lower half of the frame with leaves and sky above. $FEET $SPACE $PPL"
want jantung && gen jantung "A fit Malay man in his fifties in a long-sleeved shirt and long trousers climbing the stairs of a pedestrian bridge two steps at a time, energetic and smiling, seen from a distance so he is in the lower half of the frame with open sky above. $SPACE $PPL"
want otak && gen otak "A Malay woman in her fifties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung playing chess with her teenage son in long sleeves and long trousers at a table by a window, thinking hard, seen from a little distance so they are in the lower half of the frame with a plain wall above. $FEET $SPACE $PPL"
want makanan && gen makanan "A rushed lunch on an office desk seen from slightly above: a burger, fries, a sweet fizzy drink in a cup and a keyboard, a hand in a long sleeve holding the burger at the bottom of the frame, no fish, no faces, no text, no logos. $SPACE"
want keluarga && gen keluarga "A Malay family having breakfast together at a dining table at home: parents (mother in hijab covering her hair, neck and chest and a loose long-sleeved dress, father in a long-sleeved shirt and long trousers) and two children in long sleeves, the girl in a small hijab, laughing and passing food, seen from a little distance so they are in the lower half of the frame with a plain bright wall above. $FEET $SPACE $PPL"
want krill && gen krill "Underwater photograph of a swarm of Antarctic krill, small translucent pink-orange crustaceans, in the lower half of the frame, deep blue cold ocean water with light rays from the surface above, no people, no text. $SPACE"
want stok && gen stok "Several plain brown cardboard delivery boxes neatly stacked on a wooden floor by the front door of a bright house, just delivered, with packing tape, soft daylight, plain wall above, no logos, no labels, no text, no people. $SPACE"
echo DONE
