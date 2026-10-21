#!/bin/bash
# Generates the AI cutaways for StemLabs Fish Oil #7 (owner's ChatGPT/Codex account). Run from the project root.
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

want tangga && gen tangga "A Malay man in his fifties in a long-sleeved shirt and long trousers pausing halfway up a staircase at home, one hand on the railing, catching his breath and looking tired, afternoon light. $PPL"
want lemak && gen lemak "A flat lay of healthy-fat foods on a wooden table: a raw salmon fillet, sardines, mackerel, walnuts, chia seeds, an avocado cut in half and a small dish of olive oil, bright natural light, food photography, no people, no text."
want badminton && gen badminton "Two Malay men in their fifties playing a friendly game of badminton in a community hall, both in long-sleeved sports shirts and long track pants, energetic and smiling, mid-rally, bright indoor light. $PPL"
want puzzle && gen puzzle "A Malay grandfather in a kopiah, long-sleeved baju melayu and long trousers doing a jigsaw puzzle at the living-room table with his granddaughter in a small hijab covering her hair, neck and chest and a long-sleeved dress, both focused and happy, wearing no glasses, warm afternoon light. $PPL"
want ayam && gen ayam "A Malay family dinner table at home with fried chicken, burgers, fries and sweet drinks, no fish on the table, a father's hand in a long sleeve reaching for a piece of fried chicken, warm evening light, no faces visible."
want sarapan && gen sarapan "Three generations of a Malay family having a weekend breakfast together on the porch: grandparents (grandmother in a hijab covering her hair, neck and chest and a loose long dress, grandfather in a kopiah and long-sleeved shirt and long trousers), parents and children in long sleeves, girls in hijab, laughing, morning sunlight. $PPL"
echo DONE
