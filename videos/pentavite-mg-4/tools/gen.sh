#!/bin/bash
# Generates the AI cutaways for Careleaf Pear #3 (owner's ChatGPT/Codex account). Run from the project root.
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
SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, ceiling, hazy sky or soft bokeh) with nothing important in it."
want langit && gen langit "View from a Malaysian housing area on a hazy morning: grey hazy sky, faint sun, terrace houses and trees fading into the haze, a few cars on the road, realistic photo, no people in focus. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want aktiviti && gen aktiviti "A Malaysian school field on a hazy day: a group of Malay children in long-sleeved school uniforms (boys in long trousers, girls in white tudung covering hair, neck and chest and long blue pinafores) doing outdoor activities, the sky grey with haze, a teacher in a hijab covering her hair, neck and chest watching, muted light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want risau && gen risau "A worried Malay mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest standing at the window of her home looking out at the grey hazy sky, holding her phone, soft light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
echo DONE
