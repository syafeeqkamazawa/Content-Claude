#!/bin/bash
# Generates the AI cutaways for Careleaf pear gummies (owner's ChatGPT/Codex account). Run from the project root.
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

want jerebu && gen jerebu "A Malay woman in a hijab that fully covers her hair, neck and chest and loose long sleeves standing by a window in a Malaysian apartment, hazy grey smoggy city skyline outside (jerebu), she touches her throat with a slightly uncomfortable face, a glass of water nearby. $PPL"
want luar && gen luar "A Malay man in a long-sleeved shirt and long trousers to the ankles working outdoors on a hazy smoggy day in a Malaysian town, a delivery rider jacket, he clears his throat with a hand near his neck, grey haze in the air, motorcycle beside him. $PPL"
want bercakap && gen bercakap "A Malay woman teacher wearing a hijab that fully covers her hair, neck and chest and a loose long-sleeved baju kurung teaching and talking in front of a classroom whiteboard, hand gesturing, students' backs in the foreground wearing long-sleeved uniforms and tudung. $PPL"
want buah && gen buah "Still life on a light green tabletop: fresh yellow pears, one cut in half, orange loquats, small kumquats, a few fresh mint leaves and juicy droplets, soft natural light, no people, no text."
echo DONE
