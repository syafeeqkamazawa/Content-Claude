#!/bin/bash
# Generates the AI cutaways for Tiny Titanz 180+ #4 (owner's ChatGPT/Codex account). Run from the project root.
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

want suap && gen suap "A Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung at the dining table watching her six-year-old son in a long-sleeved t-shirt eat a small plate of rice, her chin on her hand, quietly wondering, warm evening light, framed from the waist up. $PPL"
want tolak && gen tolak "A Malay boy about five in a long-sleeved shirt turning his face away and covering his mouth with both hands as his father in a long-sleeved shirt offers a spoon of green beans, home dining table, realistic, framed from the waist up. $PPL"
want pilih && gen pilih "A Malay girl about seven in a hijab covering her hair, neck and chest and a long-sleeved top picking out only grapes from a big bowl of mixed cut fruit and leaving the rest, kitchen counter, playful picky expression, realistic. $PPL"
want malam && gen malam "A Malay couple at the kitchen table at night talking quietly with concern, the husband in a kopiah and long-sleeved shirt, the wife in a hijab covering her hair, neck and chest and long sleeves, a child's school drawing and a glass of milk on the table, warm lamp light. $PPL"
want tinggi && gen tinggi "A Malay girl about nine in a hijab covering her hair, neck and chest, a long-sleeved top and long trousers to the ankles with socks standing against a door frame with pencil height marks, smiling proudly while her mother in a hijab and long sleeves marks her height. $PPL"
want peluk && gen peluk "A Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung hugging her young son in a long-sleeved school uniform and long trousers at the school gate in the morning, both smiling, warm sunlight. $PPL"
echo DONE
