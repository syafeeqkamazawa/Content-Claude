#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #3 (owner's ChatGPT/Codex account). Run from the project root.
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
want sibuk && gen sibuk "A busy Malay mother in her forties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung, carrying a laundry basket while her phone is pinned to her shoulder and children's school bags lie around her in the living room, tired but still smiling, seen from a little distance so she is in the lower half of the frame with a plain wall above. $SPACE $PPL"
want nutrisi && gen nutrisi "A home dinner table seen from slightly above with a balanced Malaysian meal: grilled mackerel, brown rice, stir-fried green vegetables, a bowl of fruit and glasses of water, a family's hands in long sleeves reaching for the dishes at the bottom of the frame, warm evening light, no faces, no text. $SPACE"
want ibuayah && gen ibuayah "An elderly Malay couple sitting together on a wooden bench on the porch of their kampung house smiling warmly: the mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung, the father in a kopiah, long-sleeved baju melayu and long trousers to the ankle, seen from a distance so they sit in the lower half of the frame with the plain wooden house wall above, soft afternoon light. $SPACE $PPL"
want jalan && gen jalan "A fit Malay man in his fifties brisk walking toward the camera on a lakeside park path in the early morning, seen from a distance so his whole body is in the lower half of the frame, wearing a long-sleeved sports top, long loose track pants down to the ankle and running shoes, smiling, open morning sky above. $SPACE $PPL"
want baca && gen baca "A Malay woman in her fifties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung reaching to the floor, reading a book at a table by a bright window without glasses, focused and alert, seen from a little distance so she is in the lower half of the frame with a plain bright wall above, no bare feet. $SPACE $PPL"
want keluarga && gen keluarga "Three generations of a Malay family having a picnic on a mat under a big tree in a park, seen from a distance so they sit in the lower half of the frame with open sky and leaves above: grandparents (grandmother in a hijab covering her hair, neck and chest and a loose long dress, grandfather in a kopiah, long-sleeved shirt and long trousers), parents (mother in hijab and loose long dress, father in long-sleeved shirt and long trousers) and children in long sleeves and long pants, the girl in a small hijab, everyone's feet covered with socks or shoes, laughing together. $SPACE $PPL"
FEET="Every woman wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere."
want sibuk2 && gen sibuk2 "A busy Malay mother in her forties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung, carrying a laundry basket while talking on the phone, children's school bags around her in the living room, tired but smiling, seen from a little distance so she is in the lower half of the frame with a plain wall above. $FEET $SPACE $PPL"
want baca2 && gen baca2 "A Malay woman in her fifties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung, sitting in an armchair by a bright window reading a book without glasses, focused and alert, her feet in socks resting on a small rug, seen from a little distance so she is in the lower half of the frame with a plain bright wall above. $FEET $SPACE $PPL"
echo DONE
