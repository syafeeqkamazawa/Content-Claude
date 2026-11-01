#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #9 (owner's ChatGPT/Codex account). Run from the project root.
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

FEET="Every woman wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere. Every man wears a long-sleeved top and long trousers to the ankle with shoes or socks (no shorts, no bare arms, no bare feet)."
SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, sky or soft bokeh) with nothing important in it."
want futsal && gen futsal "Malay men in their thirties playing futsal on an indoor court at night, all wearing long-sleeved jerseys and long track pants to the ankle with socks and futsal shoes, one player stopping and holding his chest looking tired, floodlights, motion. No logos. $FEET $SPACE $PPL"
want doktor && gen doktor "A Malay doctor in a white coat and long trousers listening to the heart of a Malay man in his forties (long-sleeved shirt, long trousers) with a stethoscope in a bright clinic room, calm and reassuring. No medicine bottles. $FEET $SPACE $PPL"
want memandu && gen memandu "A Malay woman in her thirties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved blouse driving a car at night, squinting at the bright headlights of oncoming traffic, rubbing her tired eyes, city lights blurred outside. $FEET $SPACE $PPL"
echo DONE
