#!/bin/bash
# Generates the AI cutaways for Jus Gout Pro Max #11 (owner's ChatGPT/Codex account). Run from the project root.
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
FEET="Every woman and girl wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere."
SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, ceiling or soft bokeh) with nothing important in it."
want katil && gen katil "Morning in a Malaysian bedroom: a Malay man about 40 in a long-sleeved t-shirt and long pyjama trousers to the ankle sitting on the edge of the bed holding his foot in pain, through the open door his two children in school uniform (a boy in a long-sleeved white shirt and long trousers, a girl in a white tudung covering her hair, neck and chest and a long blue pinafore) wait with school bags, soft morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want rezeki && gen rezeki "A worried Malay father about 40 in a long-sleeved shirt and long trousers sitting at the dining table at dawn with his work bag and car keys beside him, rubbing his forehead, one foot raised on a small stool, quiet home, cool morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want makan && gen makan "A healthy home-cooked Malaysian meal on a wooden table: brown rice, grilled fish, steamed vegetables and a sliced cucumber salad, with a tall glass and a jug of plain water, soft daylight, no people. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
echo DONE
