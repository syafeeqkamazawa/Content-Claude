#!/bin/bash
# Generates the AI cutaways for Jus Gout Pro Max #12 (owner's ChatGPT/Codex account). Run from the project root.
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
want malam && gen malam "Night in a Malaysian bedroom lit only by a dim bedside lamp: a Malay man about 40 in a long-sleeved t-shirt and long pyjama trousers to the ankle sitting up awake in bed, holding his foot in pain while his wife in a hijab covering her hair, neck and chest sleeps beside him under the blanket, dark blue night light through the curtains. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want selimut && gen selimut "Close-up at night of a blanket edge lightly touching a man's foot on a bed, the man's hand in a long sleeve lifting the blanket away carefully, dim warm bedside lamp, dark bedroom, no faces. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want jam && gen jam "Close-up of a digital bedside alarm clock showing 3:00 in a dark bedroom, a glass of water beside it, a blurred man in a long-sleeved t-shirt sitting awake on the bed in the background, cool blue night light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want keluarga && gen keluarga "Early morning in a Malaysian kitchen: a tired Malay father about 40 in a long-sleeved shirt and long trousers sitting at the breakfast table rubbing his eyes, his wife in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest serving breakfast to their two children in school uniform, warm morning light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
echo DONE
