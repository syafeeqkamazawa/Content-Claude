#!/bin/bash
# Generates the AI cutaways for Nature's Key Magnesium (owner's ChatGPT/Codex account). Run from the project root.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, natural light, candid lifestyle photography, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
PPL="Everyone is fully and modestly dressed: women and girls wear a hijab that fully covers the hair, neck and chest plus loose long sleeves and a long skirt or loose trousers to the ankles; men and boys wear long sleeves and long trousers to the ankles, never shorts. Malaysian Malay people."
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

want insomnia && gen insomnia "Night, dim bedroom lit by a bedside lamp: a tired Malay man in his 30s in long-sleeved pyjamas and long pyjama trousers lying in bed wide awake, staring at the ceiling, exhausted but unable to sleep, blanket over him. $PPL"
want night && gen night "Late night in a dim bedroom: a tired Malay woman wearing a hijab that covers hair, neck and chest and loose long-sleeved sleepwear sitting on the edge of the bed rubbing her tired eyes, bedside lamp on. $PPL"
want foods && gen foods "Overhead food photo of magnesium-rich foods on a light wooden table: fresh spinach, almonds, pumpkin seeds, cashews, a sliced avocado, bananas, dark chocolate pieces and a bowl of oats, soft daylight, no people, no text."
want otot && gen otot "Morning in a Malaysian park: a fit Malay man in his 30s wearing a long-sleeved sports top and long track pants stretching his leg muscles after jogging, sunrise light. $PPL"
want tenaga && gen tenaga "Morning in a Malaysian park: an energetic smiling Malay woman wearing a sports hijab covering hair, neck and chest, a loose long-sleeved sports top and loose long track pants riding a bicycle along a tree-lined path. $PPL"
echo DONE
