#!/bin/bash
# Generates the AI cutaways for Fitsnack Dark Choco #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want fikir && gen fikir "A young Malay woman in a hijab covering her hair, neck and chest and a loose long-sleeved blouse sitting on a sofa at night holding an unbranded chocolate bar in its wrapper, hesitating with a thoughtful, guilty expression, warm lamp light. $PPL"
want gula && gen gula "A pile of white sugar cubes and spilled granulated sugar next to broken pieces of dark chocolate on a dark slate board, moody food photography, soft side light, no people, no text, no brand."
want snack && gen snack "A young Malay woman in a hijab covering her hair, neck and chest and a loose long-sleeved blouse at her office desk in the afternoon taking a small unbranded snack bar out of a drawer, smiling, laptop and a glass of water on the desk, natural window light. $PPL"
echo DONE
