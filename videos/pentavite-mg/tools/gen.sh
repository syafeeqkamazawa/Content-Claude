#!/bin/bash
# Generates the AI cutaways for Pentavite Mg (owner's ChatGPT/Codex account). Run from the project root.
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

want office && gen office "Late afternoon in an office: an exhausted Malay man in his 30s in a long-sleeved shirt and long trousers slumped at his desk in front of a laptop, rubbing the back of his neck, tired face. $PPL"
want sofa && gen sofa "Night in a living room lit by a lamp: a tired Malay woman wearing a hijab that covers hair, neck and chest and loose long-sleeved home clothes sitting on the sofa, restless, unable to relax, looking at the clock. $PPL"
want alarm && gen alarm "Early morning bedroom: a groggy Malay man in long-sleeved pyjamas and long pyjama trousers sitting up on the edge of the bed reaching to switch off a ringing alarm clock, sleepy face, dawn light. $PPL"
want busy && gen busy "A busy Malaysian home kitchen: a Malay mother wearing a hijab covering hair, neck and chest and a loose long-sleeved baju kurung stirring a pot while checking a laptop on the counter, her small son in long sleeves and long trousers tugging her sleeve. $PPL"
want herbs && gen herbs "Still life photo on a light wooden table: fresh green lemon balm leaves, purple lavender flowers and a small amber glass dropper bottle of lavender oil with no label, a few fresh blueberries, soft natural light, no people, no text."
want selfcare && gen selfcare "Calm evening at home: a relaxed Malay woman wearing a hijab covering hair, neck and chest and loose long-sleeved clothes sitting by the window with a cup of tea, eyes gently closed, peaceful smile, warm light. $PPL"
echo DONE
