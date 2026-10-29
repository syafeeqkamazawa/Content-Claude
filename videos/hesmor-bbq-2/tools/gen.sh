#!/bin/bash
# Generates the AI cutaways for Hesmor BBQ grill #2 (owner's ChatGPT/Codex account). Run from the project root.
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

FEET="Every woman and girl wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere. Every man and boy wears a long-sleeved top and long trousers to the ankle with shoes or socks (no shorts, no bare arms, no bare feet)."
SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (sky, trees or soft bokeh) with nothing important in it."
NOPPL="No people anywhere in the frame, no hands, no faces."
want alatan && gen alatan "A garage corner in a Malaysian terrace house: a big dusty standing barbecue grill, sacks of charcoal, folding tables, skewers, tongs, a cooler box and tangled cords piled up — clearly a hassle to set up. No grill brand visible. $NOPPL $SPACE"
want family && gen family "A happy Malay family having grilled chicken together at a garden table at dusk: a father in a long-sleeved baju melayu and long trousers, a mother in a loose baju kurung and a hijab covering her hair, neck and chest, two children (a boy in long sleeves and long trousers, a girl in a tudung and long dress), plates of ayam bakar on the table, fairy lights, no grill visible. $FEET $SPACE $PPL"
want tasik && gen tasik "A calm Malaysian lakeside picnic spot in the late afternoon: a mat with a basket on the grass by the water, palm trees and hills reflected in the lake, golden light, no grill and no barbecue equipment visible. $NOPPL $SPACE"
echo DONE
