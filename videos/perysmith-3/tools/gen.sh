#!/bin/bash
# Generates the AI cutaways for PerySmith M2 Lite II #3 (owner's ChatGPT/Codex account). Run from the project root.
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

want kesan && gen kesan "Close-up of an old dried brown coffee stain set deep into a light cream carpet in a Malaysian living room, a Malay man's hand in a long-sleeved shirt with the cuff buttoned at the wrist rubbing it with a cloth without success, realistic, natural light."
want sofa && gen sofa "A Malay man in a long-sleeved shirt and long trousers cleaning a light grey fabric sofa cushion with a handheld spot cleaner nozzle (generic, unbranded, black with a clear head), dirty patch being lifted, bright living room, realistic. $PPL"
want kereta && gen kereta "Close-up of a hand in a long sleeve cleaning a fabric car seat with a handheld spot cleaner nozzle (generic, unbranded), a dirty stain being sucked up, car interior, realistic, natural daylight."
echo DONE
