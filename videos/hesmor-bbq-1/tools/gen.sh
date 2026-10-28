#!/bin/bash
# Generates the AI cutaways for Hesmor BBQ grill #1 (owner's ChatGPT/Codex account). Run from the project root.
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

SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, sky or soft bokeh) with nothing important in it."
NOPPL="No people anywhere in the frame, no hands, no faces."
want barang && gen barang "A cluttered porch of a Malaysian terrace house on an overcast afternoon: a big heavy standing barbecue grill, two sacks of charcoal, a folding table, tongs, skewers, a cooler box, bags of utensils and a tangled extension cord piled up waiting to be set up — it looks like a lot of work. $NOPPL $SPACE"
want ayam && gen ayam "Close-up of chicken wings and drumsticks grilling on a stainless steel BBQ grate, extreme close-up from slightly above so the food and grate fill the whole frame edge to edge (no grill body, rim or legs visible), glowing charcoal glimpsed underneath, light smoke rising, golden char marks, soft daylight. $NOPPL"
want udang && gen udang "Close-up of large prawns grilling on a stainless steel BBQ grate, extreme close-up from slightly above so the food and grate fill the whole frame edge to edge (no grill body, rim or legs visible), glowing charcoal glimpsed underneath, light smoke, orange shells with char marks, soft daylight. $NOPPL"
want daging && gen daging "Close-up of thick slices of marinated beef grilling on a stainless steel BBQ grate, extreme close-up from slightly above so the food and grate fill the whole frame edge to edge (no grill body, rim or legs visible), glowing charcoal glimpsed underneath, sizzling with light smoke, soft daylight. $NOPPL"
echo DONE
