#!/bin/bash
# Generates the AI cutaways for Tiny Titanz 180+ IP (owner's ChatGPT/Codex account). Run from the project root.
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
FEET="Every woman and girl wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere."
want tulang && gen tulang "Two cheerful Malay children playing actively in a sunny garden: a girl about eight in a small hijab covering her hair, neck and chest with a loose long-sleeved top and long loose trousers and socks with shoes, and a boy about ten in a long-sleeved t-shirt and long trousers, running and laughing, healthy and energetic, seen from a little distance so they are in the lower half of the frame with sky and leaves above. $FEET $SPACE $PPL"
want adik && gen adik "Malay siblings of different ages sitting together at a bright breakfast table smiling, each holding a small cup: a toddler boy in long sleeves and long pants, a girl about nine in a small hijab covering her hair, neck and chest and a long-sleeved baju kurung, and a teenage boy in a long-sleeved shirt, warm morning light, seen from a little distance so they are in the lower half of the frame with a plain bright wall above, no labels, no text. $FEET $SPACE $PPL"
echo DONE
