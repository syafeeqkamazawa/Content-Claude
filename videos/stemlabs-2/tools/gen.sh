#!/bin/bash
# Generates the AI cutaways for StemLabs Fish Oil #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want compare && gen compare "A Malay woman wearing a hijab that covers hair, neck and chest and a loose long-sleeved baju kurung in a pharmacy supplement aisle holding two different plain white fish oil supplement bottles side by side, comparing them with a thoughtful face, labels blank or unreadable. $PPL"
want label && gen label "A Malay man in his 40s in a long-sleeved shirt and long trousers in a pharmacy holding a plain white supplement bottle close to his face, squinting to read the small print on the back label, shelves blurred behind, label unreadable. $PPL"
want oil && gen oil "Macro photo of golden omega-3 fish oil: translucent golden softgel capsules and a drop of golden oil falling into a small pool of oil, warm backlight, dark blue background, no people, no text."
want nz && gen nz "Landscape photo of New Zealand: snow-capped Southern Alps mountains above a calm turquoise lake with green hills, clear blue sky, no people, no text."
echo DONE
