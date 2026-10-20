#!/bin/bash
# Generates the AI cutaways for StemLabs Fish Oil #5 (owner's ChatGPT/Codex account). Run from the project root.
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

want berumur && gen berumur "A cheerful Malay couple in their late fifties walking side by side on a garden path in the morning, the husband in a kopiah, long-sleeved shirt and long trousers, the wife in a hijab covering her hair, neck and chest and a loose long dress with long sleeves, healthy and active, soft light. $PPL"
want senaman && gen senaman "A Malay man in his forties brisk-walking on a jogging track in the early morning, wearing a long-sleeved sports t-shirt and long track pants to the ankles and running shoes, determined and fit, misty park behind, golden light. $PPL"
want membaca && gen membaca "A Malay teenage girl in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung studying at a desk by a window, reading a book with focus, notebook and pencil on the desk, warm afternoon light. $PPL"
want makan && gen makan "A busy Malay office worker in his thirties in a long-sleeved shirt eating a quick packet of fried chicken and fries at his office desk while looking at his laptop, takeaway boxes on the desk, no fish on the table, fluorescent office light. $PPL"
echo DONE
