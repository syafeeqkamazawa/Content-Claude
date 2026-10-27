#!/bin/bash
# Generates the AI cutaways for Careleaf Bursting Pear Paste Gummies (owner's ChatGPT/Codex account). Run from the project root.
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
want suap && gen suap "A Malay mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest sitting at the dining table trying to spoon-feed rice and vegetables to her son about five, who turns his face away refusing to eat, wearing a long-sleeved t-shirt and long trousers, home dining room, warm light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want risau && gen risau "A worried Malay mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest looking at a nearly full plate of food her young daughter left on the table, the girl about six in a small hijab covering her hair, neck and chest and a long-sleeved dress walking away, home kitchen, soft daylight. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
echo DONE
