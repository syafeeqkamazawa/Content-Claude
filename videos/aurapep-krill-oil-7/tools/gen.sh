#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #7 (owner's ChatGPT/Codex account). Run from the project root.
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
want umur && gen umur "A young Malay man in his twenties and his grandfather in a kopiah laughing together on the porch of a kampung house, both in long-sleeved baju melayu and long trousers to the ankle, seen from a little distance so they are in the lower half of the frame with the plain wooden wall above, warm afternoon light. $SPACE $PPL"
want ibuayah && gen ibuayah "An elderly Malay couple sitting side by side at a dining table at home smiling at the camera with cups of tea: the mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung, the father in a kopiah and long-sleeved baju melayu, seen from a little distance so they are in the lower half of the frame with a plain cream wall above. $FEET $SPACE $PPL"
want laut && gen laut "Wide photograph of the Antarctic ocean with floating sea ice and icebergs under a clear pale blue sky, calm deep blue water in the lower half of the frame, open sky above, no people, no text. $SPACE"
want softgel && gen softgel "Macro product photograph of glossy translucent deep red krill oil softgel capsules piled in a small white ceramic dish on a light marble surface in the lower half of the frame, soft daylight glowing through the red capsules, plain light background above, no bottle, no labels, no people, no text. $SPACE"
want jantung && gen jantung "A fit Malay man in his forties hiking up a forest trail in the morning in a long-sleeved hiking shirt, long hiking trousers to the ankle and boots, smiling and energetic, seen from a distance so he is in the lower half of the frame with tall trees and sky above. $SPACE $PPL"
want otak && gen otak "A Malay woman in her fifties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung reading a newspaper at a cafe table by a window without glasses, sharp and alert, seen from a little distance so she is in the lower half of the frame with a plain wall above. $FEET $SPACE $PPL"
want merah && gen merah "Underwater macro photograph of a single Antarctic krill, a small translucent crustacean with bright red-orange pigment, in the lower half of the frame against deep blue water, rays of light from above, no people, no text. $SPACE"
want jarang && gen jarang "A plate of fried chicken rice with cucumber and a glass of iced syrup drink on a coffee-shop table, no fish, a hand in a long sleeve holding a spoon at the bottom of the frame, warm light, plain wall above, no faces, no text, no logos. $SPACE"
want suplemen && gen suplemen "A hand in a long sleeve holding one glossy red softgel capsule above a glass of water on a bright kitchen counter in the lower half of the frame, morning sunlight, plain light wall above, no bottle, no labels, no faces, no text. $SPACE"
echo DONE
