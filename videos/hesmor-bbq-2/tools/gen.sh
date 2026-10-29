#!/bin/bash
# Generates the AI cutaways for Habbatus Sauda Al Khair #1 (owner's ChatGPT/Codex account). Run from the project root.
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

SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, window light or soft bokeh) with nothing important in it."
NOPPL="No people anywhere in the frame, no hands, no faces, no bottles of medicine or supplements."
want sarapan && gen sarapan "A simple Malaysian breakfast on a wooden kitchen table in soft early-morning window light: a plate of nasi lemak, a cup of hot teh tarik and a glass of plain water, calm and homely. $NOPPL $SPACE"
want tidur && gen tidur "A calm Malaysian bedroom at night: a neatly made bed with white sheets, a bedside table with a warm lamp switched on and a glass of plain water, dark window with curtains drawn, peaceful mood. $NOPPL $SPACE"
echo DONE
