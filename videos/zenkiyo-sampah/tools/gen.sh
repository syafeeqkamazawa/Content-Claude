#!/bin/bash
# Generates the AI cutaways for Zenkiyo garbage bags (owner's ChatGPT/Codex account). Run from the project root.
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

want koyak && gen koyak "Close-up of a thin white kitchen garbage bag tearing open at the bottom as it is lifted out of a bin, food scraps and liquid spilling onto a clean Malaysian kitchen floor tiles, only a hand in a long sleeve visible, realistic, slightly messy."
want lantai && gen lantai "Close-up of dirty garbage water dripping and pooling on a light kitchen floor next to a kitchen bin, a torn plastic bag on the floor, realistic home kitchen, no people."
want geram && gen geram "A frustrated Malay woman in her thirties wearing a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung to the ankles standing in her kitchen with hands on her hips, looking down at spilled garbage and a torn bin bag on the floor, annoyed expression. $PPL"
want dapur && gen dapur "An overflowing kitchen trash bin full of food waste, vegetable peels and packaging in a Malaysian home kitchen after cooking, a thin flimsy bin bag stretched to the limit, realistic, no people."
want nipis && gen nipis "A Malay man in a long-sleeved t-shirt and long trousers in a kitchen awkwardly double-bagging rubbish, pulling a second thin plastic bag over a sagging torn one, mildly annoyed, realistic, framed from the waist up. $PPL"
want stok && gen stok "A tidy Malaysian home storage cabinet neatly stocked with household supplies: rolls of rubbish bags, kitchen towels, dish soap and cleaning bottles, a Malay woman in a hijab covering her hair, neck and chest and long sleeves placing a pack on the shelf, smiling, bright light, no readable brand names. $PPL"
echo DONE
