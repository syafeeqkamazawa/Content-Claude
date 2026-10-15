#!/bin/bash
# Generates the AI cutaways for the LANBOTE sink strainer bag (owner's ChatGPT/Codex account). Run from the project root.
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

want sumbat && gen sumbat "Close-up of a clogged stainless steel kitchen sink in a Malaysian home, murky grey water pooled and not draining, food scraps, rice grains, vegetable bits and noodles floating over the drain, unpleasant, realistic, no people, no brand."
want kutip && gen kutip "Close-up of a hand, the long sleeve reaching all the way down to the wrist so no forearm skin shows, picking soggy food scraps, rice and vegetable bits one by one out of a kitchen sink drain strainer with fingers, disgusted gesture, wet messy sink, no face, no brand."
want buang && gen buang "Close-up of a hand, the long sleeve reaching all the way down to the wrist so no forearm skin shows, lifting a white disposable mesh sink strainer bag full of food scraps out of a kitchen sink drain basket and dropping it into a small kitchen rubbish bin, clean and easy, no face, no brand, no text."
want dapur && gen dapur "A Malay woman in a hijab that fully covers her hair, neck and chest and loose long sleeves pushed down to the wrists happily washing dishes at a clean modern kitchen sink in a Malaysian home, water draining freely, bright kitchen. $PPL"
echo DONE
