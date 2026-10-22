#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #4 (owner's ChatGPT/Codex account). Run from the project root.
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
want kereta && gen kereta "A Malay man in his forties in a long-sleeved t-shirt and long trousers to the ankle proudly polishing his shiny car in the driveway of his house on a sunny morning, seen from a little distance so he and the car are in the lower half of the frame with open sky above. $SPACE $PPL"
want usia && gen usia "A Malay man in his fifties in a long-sleeved shirt looking closely at his greying hair in a bathroom mirror, thoughtful, soft morning light, plain wall above, seen from a little distance so he is in the lower half of the frame. $SPACE $PPL"
want jantung && gen jantung "A fit Malay man in his fifties cycling on a quiet park path in the early morning, wearing a helmet, long-sleeved cycling jersey and long cycling trousers to the ankle, smiling, seen from a distance so he is in the lower half of the frame with open morning sky and tree tops above. $SPACE $PPL"
want otak && gen otak "A Malay woman in her fifties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung, doing a crossword puzzle with a pencil at a dining table by a bright window, sharp and focused, wearing no glasses, seen from a little distance so she is in the lower half of the frame with a plain bright wall above. $FEET $SPACE $PPL"
want satu && gen satu "A Malay man in his forties in a long-sleeved sports top and long loose track pants to the ankle stretching his arms up at sunrise on a hilltop, healthy and grateful, seen from a distance so he is in the lower half of the frame with a wide golden sky above. $SPACE $PPL"
want harian && gen harian "A morning breakfast table at home seen from slightly above: a glass of water, a bowl of oats with fruit, a cup of tea and two glossy red softgel capsules on a small saucer, a hand in a long sleeve reaching for the glass at the bottom of the frame, sunlight from a window, no faces, no bottle, no labels, no text. $SPACE"
echo DONE
