#!/bin/bash
# Generates the AI cutaways for Jus Gout Pro Max #10 (owner's ChatGPT/Codex account). Run from the project root.
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
want kaki && gen kaki "Early morning in a Malaysian bedroom: a Malay man about 40 in a long-sleeved t-shirt and long pyjama trousers to the ankle sitting on the edge of the bed, grimacing in pain, both hands holding his bare right foot near the big toe, just about to step on the floor, soft dawn light through the curtains. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want jalan && gen jalan "A Malay man about 40 in a long-sleeved t-shirt and long trousers to the ankle limping slowly along a home hallway, one hand pressed on the wall for support, his face tense with pain, morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want sibuk && gen sibuk "Busy weekday morning in a Malaysian home: two children in school uniform (a boy in a long-sleeved white shirt and long navy trousers, a girl in a white tudung covering her hair, neck and chest and a long blue pinafore baju kurung) waiting by the front door with school bags, the mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest hurrying to get ready, morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want bilik && gen bilik "A Malay man about 40 in a long-sleeved t-shirt and long pyjama trousers to the ankle sitting on the edge of his bed looking at the open bedroom door, unable to stand, one hand on his knee, his face tired and in pain, morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want sedih && gen sedih "A sad Malay father about 40 in a long-sleeved t-shirt and long trousers to the ankle sitting on the sofa watching through the window as his wife in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest walks their children in school uniform out to the car, quiet living room, morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want kerja && gen kerja "A Malay man about 40 in a long-sleeved office shirt and long trousers sitting at his office desk with a laptop, wincing and rubbing his foot under the desk, colleagues blurred in the background, bright office. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want air && gen air "A Malay man about 40 in a long-sleeved t-shirt and long trousers in a bright home kitchen drinking a tall glass of plain water, a healthy plate of rice, vegetables and grilled fish on the counter, a water jug beside it, soft daylight. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want doktor && gen doktor "A Malay man about 40 in a long-sleeved shirt and long trousers sitting in a clinic consultation room listening to a male Malay doctor in a white long-sleeved coat and long trousers who explains a blood test report, calm and professional, bright clinic. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
echo DONE
