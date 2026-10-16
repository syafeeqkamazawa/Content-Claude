#!/bin/bash
# Generates the AI cutaways for Promaxx Jus Gout #5 (owner's ChatGPT/Codex account). Run from the project root.
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

want malam && gen malam "A Malay man in his fifties in long-sleeved pyjamas and long pyjama trousers to the ankles sitting up in bed at night in pain, holding his foot, dim bedside lamp light, his wife in a hijab covering her hair, neck and chest and long sleeves waking up worried beside him. $PPL"
want bengkak && gen bengkak "Close-up of an adult man's bare foot resting on a bedsheet with a red, swollen big toe joint (gout flare), the hem of his long trousers covering the ankle, his hand hovering near the toe, soft morning light, realistic medical lifestyle photo."
want xray && gen xray "A Malay female doctor in a hijab covering her hair, neck and chest and a white coat with long sleeves pointing at a foot X-ray on a clinic screen while explaining to a Malay man in his fifties in a long-sleeved shirt and long trousers, bright clinic. $PPL"
want aktiviti && gen aktiviti "A Malay man in his forties in a long-sleeved office shirt and long trousers sitting on the front steps of his house in the morning holding his painful ankle, his office bag and car keys beside him, unable to go to work. $PPL"
want pantau && gen pantau "Close-up of a Malay man in a long-sleeved shirt checking his uric acid at home with a small handheld blood test meter and test strip on his fingertip, the meter screen blank, kitchen table, natural light. $PPL"
want jagamakan && gen jagamakan "A Malay man in a kopiah and long-sleeved baju melayu eating a healthy lunch at home: steamed fish, plenty of green vegetables, brown rice and a glass of plain water, his wife in a hijab covering her hair, neck and chest and long sleeves serving more vegetables. $PPL"
want air && gen air "A Malay man in his fifties in a kopiah and long-sleeved shirt drinking a tall glass of plain water in a bright home kitchen, healthy and relaxed, framed from the waist up. $PPL"
echo DONE
