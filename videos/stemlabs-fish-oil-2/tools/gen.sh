#!/bin/bash
# Generates the AI cutaways for StemLabs Fish Oil #2 (owner's ChatGPT/Codex account). Run from the project root.
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
want nz && gen nz "Sweeping New Zealand landscape: green rolling hills and a clear blue coastline under a bright sky, pristine nature, aerial view. $NOPPL $PLAIN"
want farmasi && gen farmasi "Exterior of a modern community pharmacy in a Malaysian shoplot row, glass front with shelves of health products visible inside, evening light, street view. Signboard blank with no readable text. $NOPPL $PLAIN"
want budak && gen budak "A Malaysian mother wearing a loose long-sleeved baju kurung and a hijab fully covering her hair, neck and chest, handing a glass of water to her seven-year-old son who wears a long-sleeved shirt and long trousers to the ankle, at a bright home dining table, warm morning light. Modest, everyone fully clothed. $PLAIN"
echo DONE
