#!/bin/bash
# Generates the AI cutaways for Tiny Titanz 180+ #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want broccoli && gen broccoli "A 5-year-old Malay boy in a long-sleeved t-shirt and long trousers at the dining table covering his mouth with both hands and turning away from a spoonful of broccoli held out by his mother in a hijab and loose long-sleeved baju kurung. $PPL"
want sayur && gen sayur "A 7-year-old Malay girl wearing a children's hijab covering hair and neck and a long-sleeved dress pushing away a plate of mixed vegetables at the dinner table with a stubborn frown. $PPL"
want buah && gen buah "A 6-year-old Malay boy in a long-sleeved shirt and long trousers sitting at a kitchen table, arms crossed and pouting at a plate of sliced fresh fruits in front of him. $PPL"
want main && gen main "Malay children aged 8 to 11 playing football happily on a green school field in the afternoon, boys in long-sleeved jerseys and long track pants, a girl in a sports hijab and long-sleeved top with long track pants. $PPL"
want aquamin && gen aquamin "Underwater macro photo of pink-red coralline red algae (calcified seaweed) on the seabed in clear cold Atlantic water with soft sunlight rays, no people, no text."
want tuna && gen tuna "Food photo of a fresh whole tuna fish and thick fresh tuna steaks on crushed ice at a clean seafood market counter, no people, no text."
want fruits && gen fruits "Food photo on a wooden table: a bowl of fresh blueberries, red acerola cherries, dried prunes, dark elderberries and a few fresh vegetables (spinach, carrot, broccoli), soft natural light, no people, no text."
want ages && gen ages "A cheerful 2-year-old Malay toddler boy in a long-sleeved top and long pants sitting on the lap of his 16-year-old brother in a long-sleeved t-shirt and long trousers, both smiling on a living room sofa. $PPL"
want family && gen family "A loving Malay family in a bright living room: the mother in a hijab and loose long-sleeved baju kurung and the father in a long-sleeved baju melayu and long trousers hugging their two children, a boy in long sleeves and long trousers and a girl in a children's hijab and long-sleeved dress, all smiling. $PPL"
echo DONE
