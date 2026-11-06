#!/bin/bash
# Generates the AI cutaways for Periuk nasi Giselle #1 (owner's ChatGPT/Codex account). Run from the project root.
# Subjects follow the owner's overlay reference (video rujukan.mp4 (Krill)); every person covers aurat.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, cinematic, natural light, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
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

NOPPL="No people anywhere in the frame, no hands, no faces."
PLAIN="No brand names, no logos, no readable text."
AUR="Every person fully covers aurat: women wear a loose hijab covering hair, neck and chest with loose long-sleeved clothing to the wrists and ankles; men wear long-sleeved baju Melayu or shirt and long trousers to the ankle; children in long sleeves and long trousers."
want keluarga && gen keluarga "A small Malaysian Malay family of five (father, mother and three young children under eight) eating a simple home-cooked rice dinner together at a small dining table, plates of white rice, warm evening light, cosy apartment. Framed from the chest up across the table so everyone is seated close to the table with legs hidden under the tablecloth; the little boy wears a long-sleeved baju Melayu with long trousers. $AUR $PLAIN"
want lebih && gen lebih "Close-up of a large open rice cooker pot with a lot of leftover cooked white rice inside, on a kitchen counter at night, slightly wasteful look. $NOPPL $PLAIN"
want plug && gen plug "Close-up of a white Malaysian three-pin (UK type G) plug being placed into a white wall socket on a clean kitchen wall, shallow depth of field. $NOPPL $PLAIN"
want hadiah && gen hadiah "A neatly wrapped gift box with a satin ribbon and a small blank card on a table in a bright Malaysian living room, soft festive light. $NOPPL $PLAIN"
echo DONE
