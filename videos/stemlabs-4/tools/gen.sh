#!/bin/bash
# Generates the AI cutaways for Aurapep Shilajit Complex #1 (owner's ChatGPT/Codex account). Run from the project root.
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

want penat && gen penat "A tired Malay man in his thirties in a long-sleeved office shirt and long trousers slumped at his office desk at midday, rubbing his eyes, laptop and papers in front of him, afternoon light through the window, exhausted. $PPL"
want lesu && gen lesu "A tired Malay father in a long-sleeved office shirt and long trousers arriving home in the evening and sinking onto the living-room sofa with his work bag, while his young son in a long-sleeved t-shirt and long pants holds a football hoping to play, the father too exhausted. $PPL"
want rutin && gen rutin "A Malay man in his thirties in a kopiah and long-sleeved shirt at a bright breakfast table in the morning holding a small brown supplement tablet and a glass of plain water, healthy breakfast of oats and fruit on the table, unbranded, no bottle label visible. $PPL"
want keluarga && gen keluarga "An energetic Malay father in a long-sleeved t-shirt and long trousers to the ankles playing football with his young son in long sleeves and long pants at a park in the late afternoon, his wife in a loose long dress and a hijab covering her hair, neck and chest watching and smiling with their daughter in a hijab and long dress, golden hour light. $PPL"
echo DONE
