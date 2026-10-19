#!/bin/bash
# Generates the AI cutaways for StemLabs Fish Oil #4 (owner's ChatGPT/Codex account). Run from the project root.
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

want aktif && gen aktif "A healthy Malay family of four on a morning walk in a green park: the father in a long-sleeved t-shirt and long track pants, the mother in a hijab covering her hair, neck and chest with a loose long-sleeved top and long loose trousers, a son in long sleeves and long pants and a daughter in a hijab and long dress, all smiling and energetic, soft morning light. $PPL"
want pilih && gen pilih "A Malay man in his thirties in a kopiah and long-sleeved shirt in a pharmacy aisle comparing the back labels of two plain unbranded white supplement bottles, one in each hand, thoughtful expression, shelves of unbranded boxes behind him. $PPL"
want belanja && gen belanja "A Malay woman in a hijab covering her hair, neck and chest and a loose long-sleeved blouse sitting on a sofa at home looking at her smartphone with a pleasantly surprised smile as if seeing a great price, the phone screen not visible to the camera, cosy living room, natural light. $PPL"
echo DONE
