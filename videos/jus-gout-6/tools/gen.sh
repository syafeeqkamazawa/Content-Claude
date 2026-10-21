#!/bin/bash
# Generates the AI cutaways for Promaxx Jus Gout #6 (owner's ChatGPT/Codex account). Run from the project root.
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

want tengahmalam && gen tengahmalam "A Malay man in his forties in a long-sleeved t-shirt and a kain pelikat sarong reaching his ankles sitting on the edge of his bed in the middle of the night grimacing in pain and holding his foot near the big toe, dim blue night light and a bedside lamp, wall clock showing 3 o'clock. $PPL"
want pijak && gen pijak "Close-up at floor level of a man's bare foot with a slightly red, swollen big toe joint hovering hesitantly above cold bedroom floor tiles beside a bed at night, the hem of his long sarong covering his ankle, his hand gripping the bed edge, dim light."
want anakajak && gen anakajak "A cheerful Malay boy of about seven in a long-sleeved t-shirt and long pants, wearing sneakers, tugging his father's hand towards the front door to go out, while the father in a long-sleeved shirt and long trousers sits on the sofa holding his sore foot, looking apologetic, bright living room. $PPL"
want bahan && gen bahan "A rustic wooden chopping board on a kitchen counter with a fresh pineapple cut in half, a few knobs of fresh ginger root and fresh turmeric roots with a little ground turmeric in a small bowl, soft natural window light, food photography, no people, no text."
want keluarga && gen keluarga "A happy Malay family having a picnic on a mat under a shady tree in a park in the late afternoon: the father in a long-sleeved shirt and long trousers laughing with his children, the mother in a hijab covering her hair, neck and chest and a loose long dress serving food, a son in long sleeves and long pants and a daughter in a hijab and long dress, golden light. $PPL"
echo DONE
