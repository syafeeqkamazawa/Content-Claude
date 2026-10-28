#!/bin/bash
# Generates the AI cutaways (OLZZ Calcium) for Careleaf Bursting Pear Paste Gummies (owner's ChatGPT/Codex account). Run from the project root.
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
FEET="Every woman and girl wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere."
SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, ceiling or soft bokeh) with nothing important in it."
want sekolah && gen sekolah "Early morning at a Malaysian home: a Malay boy about eight in a white long-sleeved school shirt and long navy school trousers putting on his school bag at the front door, his mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest handing him a water bottle, soft morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want main && gen main "Late afternoon in a Malaysian housing area playground: a Malay boy about eight in a long-sleeved t-shirt and long track pants running and laughing with a football on the grass, warm golden light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want sayur && gen sayur "A Malay girl about seven in a small hijab covering her hair, neck and chest and a long-sleeved dress at the dinner table, pushing the green vegetables to the edge of her plate with a spoon, looking unimpressed, rice and chicken on the plate, home dining room, warm light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want susu && gen susu "Close-up of a glass of milk left half full on a wooden kitchen table beside a child's cereal bowl, a child's hand in a long sleeve sliding the glass away, morning light from the window, no faces. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
echo DONE
