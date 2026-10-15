#!/bin/bash
# Generates the AI cutaways for Tiny Titanz Kid180 (owner's ChatGPT/Codex account). Run from the project root.
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

want active && gen active "Energetic Malay children aged 6 to 9 playing on a colourful outdoor playground in the afternoon, running and climbing, boys in long-sleeved t-shirts and long trousers, girls in children's hijabs covering hair and neck with long sleeves and long trousers. $PPL"
want milk && gen milk "At a home dining table: a 6-year-old Malay girl wearing a children's hijab covering hair and neck and a long-sleeved top pushing away a glass of milk with a reluctant face, her mother's hand in a long sleeve offering it. $PPL"
want parents && gen parents "A thoughtful Malay mother wearing a hijab covering hair, neck and chest and loose long-sleeved baju kurung and a father in a long-sleeved shirt watching their 7-year-old son (long sleeves, long trousers) pick at his dinner plate, slightly worried faces, warm home lighting. $PPL"
want berries3 && gen berries3 "Food photo: three small white bowls of fresh blueberries, dark elderberries and red cranberries on a light green tablecloth, a few mint leaves, bright soft daylight, no people, no text."
want plate && gen plate "Top-down food photo of a balanced child's meal on a white plate: rice, grilled fish, steamed broccoli and carrots, sliced fruit and a glass of milk on a wooden table, bright daylight, no people, no text."
echo DONE
