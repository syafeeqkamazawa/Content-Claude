#!/bin/bash
# Generates the AI cutaways for Infinity Probiotics Plus #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want jantung && gen jantung "A Malay man in his fifties in a long-sleeved shirt sitting at a home table checking his blood pressure with a digital arm cuff monitor, the monitor screen blank, his wife in a hijab covering her hair, neck and chest and long sleeves looking on with concern. $PPL"
want usus && gen usus "A realistic anatomical model of the human digestive system and intestines standing on a white clinic desk next to a stethoscope and a clipboard, soft clinical light, shallow depth of field, no people, no hands."
want kembung && gen kembung "A Malay woman in her thirties in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung sitting on a sofa holding her stomach with both hands, looking bloated and uncomfortable, fully clothed, home living room. $PPL"
want abai && gen abai "A Malay man in his thirties in a long-sleeved office shirt and long trousers at his office desk with a laptop, one hand pressed on his stomach in discomfort while he keeps working, busy office, natural light. $PPL"
want bakteria && gen bakteria "Microscope photograph of rod-shaped beneficial probiotic bacteria (lactobacillus) in soft blue and green tones, scientific micrograph, shallow depth of field, no text, no people."
want sihat && gen sihat "A Malay family at a bright breakfast table enjoying yogurt, fruit and oats together, father in a kopiah and long-sleeved shirt, mother in a hijab covering her hair, neck and chest and long sleeves, a daughter in a hijab and a son in long sleeves, all smiling and comfortable. $PPL"
want sibuk && gen sibuk "A busy Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved baju kurung to the ankles in a home kitchen holding a phone to her ear while stirring a pot, a toddler boy in long-sleeved pyjamas and long trousers with socks tugging her sleeve, a laptop open on the counter, tired but coping. $PPL"
echo DONE
