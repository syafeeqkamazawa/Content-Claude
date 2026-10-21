#!/bin/bash
# Generates the AI cutaways for Titanz Kid180 #3 (owner's ChatGPT/Codex account). Run from the project root.
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

want makan && gen makan "A Malay boy of about eight in a long-sleeved t-shirt and long pants eating breakfast at the kitchen table before school, his school bag beside him, morning sunlight, healthy and cheerful. $PPL"
want tanya && gen tanya "A Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved blouse in a supermarket aisle reading the nutrition label on a carton of milk with a thoughtful expression, shopping basket on her arm. $PPL"
want susu && gen susu "A Malay girl of about six in a small hijab covering her hair, neck and chest and a long-sleeved dress at the dining table pushing a full glass of milk away with a scrunched-up face, morning kitchen light. $PPL"
want pinggan && gen pinggan "Close-up of a child's hand in a long sleeve using a fork to push green vegetables to the edge of a dinner plate while keeping the rice and chicken, family dinner table, warm light, no face visible."
want tulang && gen tulang "Malay children climbing and swinging on a colourful school playground in the afternoon, boys in long-sleeved shirts and long pants, girls in tudung covering hair, neck and chest with long-sleeved tops and long pants, strong and energetic, sunny. $PPL"
want senyum && gen senyum "A Malay boy of about seven in long-sleeved pyjamas grinning widely at the bathroom mirror after brushing his teeth, showing a full set of white teeth, toothbrush in hand, bright morning light. $PPL"
want berebut && gen berebut "Two Malay siblings, a boy in a long-sleeved t-shirt and long pants and a girl in a small hijab covering her hair, neck and chest and a long-sleeved dress, eagerly reaching up towards their smiling mother's hand at the kitchen counter, the mother in a hijab covering her hair, neck and chest and a loose long-sleeved blouse, playful and happy, no product visible. $PPL"
want pagi && gen pagi "A Malay father in a long-sleeved shirt and long trousers helping his son in a long-sleeved school uniform and long trousers put on his school bag at the front door in the early morning, both smiling, routine before school. $PPL"
want basikal && gen basikal "A Malay father in a long-sleeved t-shirt and long track pants teaching his young daughter in a sports hijab covering her hair, neck and chest, a long-sleeved top and long pants to ride a small bicycle in a quiet park, running alongside holding the seat, golden hour. $PPL"
want tidur && gen tidur "A Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved robe kissing her young son's forehead as she tucks him into bed at night, the boy in long-sleeved pyjamas, warm bedside lamp, tender moment. $PPL"
echo DONE
