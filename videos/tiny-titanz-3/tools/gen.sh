#!/bin/bash
# Generates the AI cutaways for Tiny Titanz 180+ #3 (owner's ChatGPT/Codex account). Run from the project root.
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


want risau && gen risau "A worried Malay mother in a hijab that fully covers her hair, neck and chest and a loose long-sleeved baju kurung at a dining table, watching her young son in a long-sleeved shirt push his plate of vegetables away, framed from the waist up. $PPL"
want sayur && gen sayur "A little Malay girl in a small hijab covering her hair, neck and chest and a long-sleeved top turning her head away from a spoon of green vegetables held by her mother's hand in a long sleeve, home dining table. $PPL"
want buah && gen buah "A Malay boy about seven in a long-sleeved t-shirt sulking with arms crossed at a kitchen counter in front of a plate of cut fruit, framed from the waist up, morning light. $PPL"
want cuba && gen cuba "A Malay mother in a hijab covering her hair, neck and chest and long sleeves to the wrist preparing a colourful kids bento lunchbox with rice, vegetables and fruit in a home kitchen, warm light. $PPL"
want tulang && gen tulang "A happy Malay girl about eight in a hijab covering her hair, neck and chest, loose long sleeves, long loose trousers to the ankles and sneakers, laughing with healthy white teeth while skipping rope in a sunny school field. $PPL"
want membesar && gen membesar "A Malay father in a kopiah and long-sleeved shirt marking his son's height on a white wall with a pencil; the boy about nine in a long-sleeved t-shirt and long trousers to the ankles stands proudly against the wall. $PPL"
want aquamin && gen aquamin "Underwater photograph of red calcified seaweed (red marine algae) on rocks in clear blue tropical sea, sunlight rays, no people."
want praktikal && gen praktikal "A Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung handing a small cup of drink to her son in a long-sleeved school shirt and long trousers at the front door on a school morning, both smiling. $PPL"
want keluarga && gen keluarga "A Malay family hugging and laughing on a living-room sofa: father in a kopiah, long-sleeved baju melayu and long trousers, mother in a hijab covering her hair, neck and chest and a loose long baju kurung, a son in long sleeves and long trousers, a little daughter in a hijab and long sleeves. $PPL"
echo DONE
