#!/bin/bash
# Generates the AI cutaways for Jus Gout #3 (owner's ChatGPT/Codex account). Run from the project root.
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

want tuam && gen tuam "A Malay man in his fifties wearing a kopiah, a loose long-sleeved baju melayu and long trousers to the ankles, sitting on a sofa at home holding his bare foot with both hands, the big toe joint visibly red and swollen, wincing in pain. $PPL"
want lantai && gen lantai "Early morning in a Malaysian bedroom, a Malay man in his fifties in a long-sleeved t-shirt and long pyjama trousers to the ankles sitting on the edge of the bed, carefully lowering one bare foot towards the floor with a pained, hesitant face, hand gripping the mattress. $PPL"
want kristal && gen kristal "Polarized light microscope photograph of needle-shaped monosodium urate crystals, bright yellow and blue birefringent needles on a dark background, scientific microscopy image, no people."
want terseliuh && gen terseliuh "A young Malay man in a long-sleeved sports jersey and long tracksuit trousers to the ankles sitting on the side of an indoor futsal court holding his twisted ankle in pain, a friend in a long-sleeved jersey and long trousers kneeling beside him. $PPL"
want milkthistle && gen milkthistle "Macro close-up photograph of a fresh purple milk thistle flower with spiky green leaves and a few dried milk thistle seeds on a wooden table, natural light, no people."
want nenas && gen nenas "Close-up photograph of a freshly cut ripe pineapple on a wooden chopping board, juicy yellow slices and the green crown, Malaysian kitchen, natural light, no people."
want halia && gen halia "Close-up photograph of fresh ginger roots, some sliced to show the pale yellow inside, on a rustic wooden board in a Malaysian kitchen, natural light, no people."
want kunyit && gen kunyit "Close-up photograph of fresh turmeric (kunyit) roots, a few cut open showing the bright orange inside, next to a small bowl of turmeric powder on a wooden board, natural light, no people."
want klinik && gen klinik "Inside a bright Malaysian clinic, a Malay woman doctor wearing a hijab that fully covers her hair, neck and chest and a long-sleeved white coat over loose clothing examines the swollen foot of a Malay man in his fifties wearing a kopiah, long-sleeved shirt and long trousers rolled to just above the ankle, sitting on the examination bed. $PPL"
echo DONE
