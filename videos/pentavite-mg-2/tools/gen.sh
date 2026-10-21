#!/bin/bash
# Generates the AI cutaways for Pentavite Mg #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want penat && gen penat "A tired Malay man in his late thirties in a long-sleeved office shirt and long trousers sitting at his desk late in the evening, rubbing the back of his neck with his eyes closed, laptop open, warm desk lamp, exhausted after a long workday. $PPL"
want katil && gen katil "A Malay man in his late thirties in long-sleeved pyjamas and long pyjama trousers lying awake in bed at night under a blanket, eyes open staring at the ceiling, restless and unable to switch off, dim blue night light from the window, phone glowing on the bedside table. $PPL"
want kerja && gen kerja "A busy Malay woman in her thirties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved blouse with long loose trousers, working late at a cluttered office desk with two monitors and stacks of files, holding her forehead, tired, office mostly empty and dark outside. $PPL"
want otot && gen otot "A Malay man in his forties in a long-sleeved sports top and long loose track pants down to the ankle stretching his calf muscles on a park bench after a morning walk, relaxed and healthy, soft morning light, green trees. $PPL"
want herba && gen herba "Close-up food and herb photograph of fresh lemon balm leaves, purple lavender sprigs, a small plain amber glass dropper bottle of oil with no label and a scatter of fresh blueberries and blackberries on a light wooden table, soft natural daylight, no people, no text, no labels."
want rehat && gen rehat "A Malay woman in her thirties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung, relaxing on a sofa at home in the evening with a cup of warm tea, eyes softly closed, smiling, calm and peaceful, warm lamp light. $PPL"
want keluarga && gen keluarga "A Malay husband and wife in their thirties relaxing together in their living room in the evening: the wife in a hijab covering her hair, neck and chest and a loose long-sleeved dress, the husband in a long-sleeved t-shirt and long trousers to the ankle, smiling and chatting on the sofa, warm cosy light. $PPL"
# Owner: captions never over people or the product — these leave the upper 40% of the frame empty for the caption board.
SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, ceiling, sky or soft bokeh) with nothing important in it."
want katil2 && gen katil2 "A Malay man in his late thirties in long-sleeved pyjamas and long pyjama trousers lying awake in bed at night under a blanket, eyes open staring upward, restless, seen from the side at a distance so the bed sits in the lower half of the frame with a plain dark bedroom wall above, dim blue night light, phone glowing on the bedside table. $SPACE $PPL"
want penat2 && gen penat2 "A tired Malay man in his late thirties in a long-sleeved office shirt and long trousers sitting at his desk late in the evening rubbing his neck, seen from a little distance so he and the desk sit in the lower half of the frame with a plain dark office wall above, warm desk lamp. $SPACE $PPL"
want keluarga2 && gen keluarga2 "A Malay husband and wife in their thirties relaxing together on a low sofa in their living room in the evening, seen from a distance so they sit in the lower half of the frame with a plain warm wall above: the wife in a hijab covering her hair, neck and chest and a loose long-sleeved dress, the husband in a long-sleeved t-shirt and long trousers to the ankle, smiling and chatting, cosy lamp light. $SPACE $PPL"
want otot2 && gen otot2 "A Malay man in his forties in a long-sleeved sports top and long loose track pants down to the ankle stretching his legs on a park path after a morning walk, seen from a distance so his whole body is in the lower half of the frame with open morning sky and tree tops above. $SPACE $PPL"
want rehat2 && gen rehat2 "A Malay woman in her thirties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung relaxing on a low sofa with a cup of warm tea, eyes softly closed, seen from a little distance so she sits in the lower half of the frame with a plain warm wall above, evening lamp light. $SPACE $PPL"
want rehat3 && gen rehat3 "A Malay woman in her thirties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved baju kurung reaching to the floor, sitting upright on a low sofa with both feet on the floor in socks fully covered by her long skirt, holding a cup of warm tea with eyes softly closed, calm and relaxed, seen from a little distance so she sits in the lower half of the frame with a plain warm wall above, evening lamp light. No bare feet. $SPACE $PPL"
echo DONE
