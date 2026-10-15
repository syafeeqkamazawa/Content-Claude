#!/bin/bash
# Generates the AI cutaways for Titanz 180+ tablet (owner's ChatGPT/Codex account). Run from the project root.
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

want breakfast && gen breakfast "Morning in a Malaysian home kitchen: a caring Malay mother wearing a hijab covering hair, neck and chest and a loose long-sleeved baju kurung serving a healthy breakfast to her two teenagers in school uniform — a 15-year-old boy in a white long-sleeved shirt and long trousers and a 14-year-old girl in a white school hijab and long blue pinafore dress with long sleeves. $PPL"
want teens && gen teens "Two Malay teenagers walking to school in the morning sun, smiling: a 16-year-old boy in a white long-sleeved school shirt and long dark trousers and a 15-year-old girl in a white school hijab covering hair, neck and chest with a long blue pinafore and long sleeves, school bags on their backs. $PPL"
want sport && gen sport "A 16-year-old Malay boy in a long-sleeved sports jersey and long track pants jumping to shoot a basketball on an outdoor school court, afternoon light, energetic. $PPL"
want berries && gen berries "Macro food photo of mixed berries — blueberries, cranberries and elderberries — piled on a light wooden board with a few green tea leaves, soft daylight, no people, no text."
echo DONE
