#!/bin/bash
# Generates the AI cutaways for PerySmith #2 (sofa) (owner's ChatGPT/Codex account). Run from the project root.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, natural light, candid lifestyle photography, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
PPL="Everyone is fully and modestly dressed: women wear a hijab that fully covers the hair, neck and chest plus loose long sleeves and a long skirt or loose trousers to the ankles; men wear long sleeves and long trousers to the ankles, never shorts. Malaysian Malay people."
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

want sofabersih && gen sofabersih "A cosy Malaysian terrace-house living room with a light beige fabric three-seater sofa that looks clean and tidy at first glance, cushions neatly arranged, soft afternoon window light, a Malay mother in a hijab and loose long-sleeved baju kurung sitting on it reading her phone. $PPL"
want tumpah && gen tumpah "Close-up of a light beige fabric sofa seat as a small Malay boy's hand knocks over a plastic cup and orange juice splashes onto the fabric, droplets in mid air, motion, the boy wears a loose long-sleeved top and long trousers, his mother in a hijab reaching in from the side. $PPL Any child wears a loose long-sleeved top and long trousers to the ankles."
want jatuh && gen jatuh "Close-up of a light beige fabric sofa cushion with crumbs, a dropped piece of chocolate biscuit and a smear of chocolate and ketchup sauce on the fabric, a child's hand in a long sleeve visible at the edge, messy family living room, shallow depth of field. Any child wears a loose long-sleeved top and long trousers to the ankles."
want kotorlama && gen kotorlama "Close-up of an old light beige fabric sofa cushion with many old yellow-brown set-in stains and grey dirty patches along the armrest, a Malay woman in a hijab and loose long-sleeved clothes with sleeves down to the wrists scrubbing a stain with a wet cloth and a tired frustrated face, framed from the waist up, no feet in frame. $PPL"
want cucisofa && gen cucisofa "A Malay woman in a hijab and loose long-sleeved clothes kneeling beside a light beige fabric sofa, cleaning the seat cushion with a small handheld upholstery cleaning nozzle on a black hose, transparent nozzle head with dirty water inside, the cleaned stripe visibly brighter than the rest, no brand. $PPL"
want tilam && gen tilam "Close-up of a hand, the long sleeve reaching all the way down to the wrist so no forearm skin shows, cleaning a single mattress in a child's bedroom with a small handheld upholstery cleaning nozzle on a black hose, transparent nozzle head, a yellowish stain being lifted and the cleaned patch visibly brighter, no brand, no faces."
want kereta && gen kereta "Close-up through an open car door of a hand in a long sleeve cleaning a grey fabric car seat with a small handheld upholstery cleaning nozzle on a black hose, transparent nozzle head, the cleaned stripe visibly brighter than the dirty seat, no brand, no faces."
echo DONE
