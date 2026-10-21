#!/bin/bash
# Generates the AI cutaways for Agro Farm Baja Rumput #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want pasang && gen pasang "Two Malaysian landscape workers in long-sleeved work shirts, long work trousers and wide-brimmed hats laying fresh rolls of green carpet grass turf on bare soil in the front yard of a modern Malaysian terrace house, morning light, stacks of turf rolls beside them. $PPL"
want laman && gen laman "A Malay father in a long-sleeved t-shirt and long trousers and his young son in long sleeves and long pants playing ball barefoot on a lush, even, bright green lawn in front of a modern Malaysian terrace house, the mother in a hijab covering her hair, neck and chest and a loose long dress watching from the porch, late afternoon golden light. $PPL"
echo DONE
