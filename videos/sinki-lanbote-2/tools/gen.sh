#!/bin/bash
# Generates the AI cutaways for Lanbote sink strainer #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want jijik && gen jijik "Close-up of a Malay man's bare hand with a long sleeve reaching into a stainless kitchen sink drain to pick out soggy food scraps, rice and vegetable bits, grimacing, realistic, slightly gross, natural kitchen light."
want tong && gen tong "Close-up of a Malay man's hand in a long-sleeved shirt with the cuff buttoned at the wrist dropping a small white mesh sink strainer bag full of food scraps into a stainless pedal bin with the lid open, clean modern Malaysian kitchen, realistic, no brand names."
want kilat && gen kilat "A sparkling clean empty stainless steel kitchen sink with a shiny drain and water droplets, tidy Malaysian kitchen counter around it, bright morning light, realistic product-style photo, no people."
want ibu && gen ibu "A happy Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung washing dishes at a clean kitchen sink, her little daughter in a small hijab and long sleeves helping dry a plate beside her, warm daylight. $PPL"
echo DONE
