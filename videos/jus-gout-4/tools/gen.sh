#!/bin/bash
# Generates the AI cutaways for Jus Gout #4 (owner's ChatGPT/Codex account). Run from the project root.
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

want pijak && gen pijak "Close-up at floor level of a Malay man's bare foot with a red swollen big toe joint hovering hesitantly above cool floor tiles beside a bed, the hem of his long trousers at the ankle, his hand gripping the bed edge, early morning light, no face."
want tongkat && gen tongkat "A Malay man in his fifties wearing a kopiah, a long-sleeved baju melayu and long trousers to the ankles walking slowly and painfully with a walking cane along a house corridor, his wife in a hijab that fully covers her hair, neck and chest and a loose long-sleeved baju kurung supporting his arm. $PPL"
want bengkak && gen bengkak "Close-up of a swollen red ankle and foot resting on a cushion on a sofa with an ice pack wrapped in a towel on it, a Malay man's long trousers rolled up only to mid-shin, his hand holding the ice pack, no face."
want farmasi && gen farmasi "Inside a bright Malaysian community pharmacy, a Malay woman pharmacist wearing a hijab that fully covers her hair, neck and chest and a long-sleeved white coat handing a small paper bag of prescribed medicine across the counter to a Malay man in his fifties wearing a kopiah and long-sleeved shirt. $PPL"
want sayur && gen sayur "A healthy Malaysian home meal on a wooden dining table: a plate of brown rice, steamed fish, stir-fried green vegetables, sliced cucumber and a glass of plain water, a Malay man's hand in a long sleeve holding a spoon, no face, natural light."
want nenashalia && gen nenashalia "Close-up of a glass of pale yellow pineapple and ginger juice on a kitchen counter, beside fresh pineapple chunks and sliced ginger root on a wooden board, condensation on the glass, natural light, no people, no brand."
echo DONE
