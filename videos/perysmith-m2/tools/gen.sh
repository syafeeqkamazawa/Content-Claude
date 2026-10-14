#!/bin/bash
# Generates the AI cutaways for the PerySmith edit (owner's ChatGPT/Codex account). Run from the project root.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, natural light, candid lifestyle photography, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
PPL="Everyone is fully and modestly dressed: women wear a hijab that fully covers the hair, neck and chest plus loose long sleeves and a long skirt or loose trousers to the ankles; men wear long sleeves and long trousers to the ankles, never shorts. Malaysian Malay people."
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

want dobi && gen dobi "A tired Malay man in a long-sleeved t-shirt and long trousers carrying a big heavy rolled-up carpet on his shoulder into a small neighbourhood laundry shop (dobi) with washing machines inside. $PPL"
want angkat && gen angkat "A Malay husband in a long-sleeved shirt and long trousers and his wife in a hijab and loose long-sleeved baju kurung struggling together to lift a large heavy living-room carpet in their home, straining faces. $PPL"
want jemur && gen jemur "A large wet carpet hanging over the front gate railing of a Malaysian terrace house to dry, cloudy grey sky, a Malay woman in a hijab and loose long-sleeved clothes looking at it with a frustrated face. $PPL"
want sofa && gen sofa "A Malay woman in a hijab and loose long-sleeved clothes cleaning a light grey fabric sofa cushion at home with a small handheld upholstery cleaning nozzle on a hose, transparent nozzle head, the cleaned stripe visibly brighter, no brand. $PPL"
want tilam && gen tilam "A Malay man in a long-sleeved shirt and long trousers cleaning a white mattress on a bed with a small handheld upholstery cleaning nozzle on a hose, transparent nozzle head, the cleaned area visibly brighter, no brand. $PPL"
echo DONE
