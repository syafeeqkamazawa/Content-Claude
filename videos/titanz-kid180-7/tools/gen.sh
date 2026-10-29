#!/bin/bash
# Generates the AI cutaways for Tiny Titanz Kid180 #7 (owner's ChatGPT/Codex account). Run from the project root.
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

FEET="Every woman and girl wears socks and her long skirt or long trousers reach the floor; no bare feet or ankles visible anywhere. Every man and boy wears a long-sleeved top and long trousers to the ankle with socks (no shorts, no bare arms, no bare feet)."
SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, ceiling or soft bokeh) with nothing important in it."
want sayur && gen sayur "A Malay boy about 7 years old in a long-sleeved shirt and long trousers sitting at a home dining table, pushing away a plate of broccoli and green vegetables with a reluctant face, his mother in a loose baju kurung and a hijab covering her hair, neck and chest sitting beside him, warm kitchen light. $FEET $SPACE $PPL"
want jajan && gen jajan "A Malay girl about 8 years old wearing a tudung covering her hair, neck and chest and a loose long-sleeved dress, happily reaching for colourful packets of chips and sweets on a living-room coffee table, unbranded plain snack packets with no readable text, soft daylight. $FEET $SPACE $PPL"
want membesar && gen membesar "A Malay mother in a loose baju kurung and a hijab covering her hair, neck and chest measuring the height of her smiling young son (long-sleeved shirt, long trousers, socks) against pencil marks on a white wall at home, a younger daughter in a tudung and long dress watching, warm soft light. $FEET $SPACE $PPL"
echo DONE
