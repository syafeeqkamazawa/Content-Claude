#!/bin/bash
# Generates the AI cutaways (Kid180 #6) for Careleaf Bursting Pear Paste Gummies (owner's ChatGPT/Codex account). Run from the project root.
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
want memilih && gen memilih "A Malay boy about six in a long-sleeved t-shirt and long trousers at the dining table pushing away a plate of rice with broccoli and carrots, arms crossed, picky eater, his mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest sitting beside him looking patient, home dining room, warm evening light. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want sayur && gen sayur "Close-up of a child's dinner plate on a wooden dining table: rice and chicken eaten but the green vegetables (sawi, broccoli) left untouched and pushed to the side, a small spoon resting on the plate, a child's hand in a long sleeve pulling away, home dining room, warm light. No faces. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want sarapan && gen sarapan "Morning breakfast at a Malaysian home: a Malay girl about five in a small hijab covering her hair, neck and chest and a long-sleeved dress sitting at the table, chin on her hand, bored, a plate of nasi lemak and a glass of milk barely touched in front of her, school bag on the next chair, soft morning daylight from the window. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want buah && gen buah "A Malay mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest holding out a bowl of cut fruit (apple, orange, grapes) to her son about six in a long-sleeved t-shirt and long trousers who shakes his head and turns away, living room, soft daylight. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want nutrisi && gen nutrisi "A thoughtful Malay mother in a loose long-sleeved baju kurung and a hijab covering her hair, neck and chest standing in the kitchen holding a child's leftover plate of food with vegetables uneaten, looking at it worried, home kitchen, soft daylight. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
want tumbesaran && gen tumbesaran "A smiling Malay father in a long-sleeved shirt and long trousers measuring the height of his son about seven in a long-sleeved t-shirt and long trousers against a white wall with a pencil mark and a wall height chart, the boy standing straight and proud, bright home hallway. Every man and boy wears a long-sleeved top and long trousers to the ankle (no shorts, no bare arms). $FEET $SPACE $PPL"
echo DONE
