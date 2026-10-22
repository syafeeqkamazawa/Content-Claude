#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #5 (owner's ChatGPT/Codex account). Run from the project root.
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
want ikan && gen ikan "A home lunch table seen from slightly above with a plate of grilled ikan kembung (mackerel) with sambal, a plate of white rice, ulam vegetables and a glass of water, warm daylight, hands in long sleeves at the bottom edge, no faces, no text. $SPACE"
want sihat && gen sihat "A healthy Malay couple in their fifties walking together on a park path in the morning: the wife in a hijab covering her hair, neck and chest, a loose long-sleeved blouse and long loose skirt with socks and shoes, the husband in a long-sleeved shirt and long trousers to the ankle, smiling and chatting, seen from a distance so they are in the lower half of the frame with open sky and tree tops above. $FEET $SPACE $PPL"
want mata && gen mata "A Malay grandfather in a kopiah, long-sleeved baju melayu and long trousers to the ankle reading a picture book with his young grandson in long sleeves and long pants on the sofa, both looking at the pages, no glasses, seen from a little distance so they are in the lower half of the frame with a plain warm wall above, soft afternoon light. $SPACE $PPL"
want jantung && gen jantung "A fit Malay man in his forties jogging on a lakeside track at sunrise in a long-sleeved running top, long loose running pants to the ankle and running shoes, smiling, seen from a distance so he is in the lower half of the frame with a wide open sky above. $SPACE $PPL"
want otak && gen otak "A Malay woman in her forties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung, studying with books and a notebook at a desk by a bright window, focused and alert, seen from a little distance so she is in the lower half of the frame with a plain bright wall above. $FEET $SPACE $PPL"
want jarang && gen jarang "A busy Malay man in his thirties in a long-sleeved office shirt and long trousers eating a plate of fried noodles quickly at a roadside hawker stall table at night while checking his phone, seen from a little distance so he is in the lower half of the frame with the dark stall canopy above. $SPACE $PPL"
want harian && gen harian "A morning breakfast table at home seen from slightly above: a glass of water, a plate of nasi lemak with an egg, a cup of tea and two glossy red softgel capsules on a small saucer, a hand in a long sleeve reaching for the glass at the bottom of the frame, sunlight from a window, no faces, no bottle, no labels, no text. $SPACE"
echo DONE
