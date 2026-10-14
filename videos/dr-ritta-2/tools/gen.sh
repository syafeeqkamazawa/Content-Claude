#!/bin/bash
# Generates the AI cutaways for Dr.Ritta #2 (owner's ChatGPT/Codex account). Run from the project root.
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

want aisle && gen aisle "A Malay mother wearing a hijab and a loose long-sleeved baju kurung in a pharmacy aisle, holding and reading a small pink children's toothpaste box (no readable text), shelves of oral care products blurred behind her. $PPL"
want sink && gen sink "Night time in a home bathroom: a 6-year-old Malay boy in long-sleeved pyjamas and long pyjama trousers stands at the sink turning his face away with a stubborn pout, while his mother's hand in a long sleeve holds out a small children's toothbrush toward him. $PPL"
want sulk && gen sulk "A 7-year-old Malay girl wearing a children's hijab covering hair and neck, long-sleeved pyjamas and long pyjama trousers, standing in a bright home bathroom with her arms crossed and a sulky face, refusing to brush her teeth. $PPL"
want run && gen run "A playful 5-year-old Malay boy in long-sleeved pyjamas and long pyjama trousers running away laughing down a home hallway, slight motion blur, his mother in a hijab and loose long-sleeved clothes behind him holding a small toothbrush. $PPL"
want grimace && gen grimace "Close-up of a 6-year-old Malay boy in a long-sleeved pyjama top with a toothbrush in his mouth making a disgusted face at the taste of the toothpaste, bathroom background. $PPL"
want siblings && gen siblings "A 4-year-old Malay boy in a long-sleeved top and long trousers and his 11-year-old sister wearing a hijab covering hair and neck with a long-sleeved top and long skirt, both smiling and holding colourful children's toothbrushes in a bright bathroom. $PPL"
want strawberry && gen strawberry "Macro food photo of fresh ripe red strawberries with water droplets on a light pink background, soft studio light, no people, no text."
want dentist && gen dentist "A Malay female dentist wearing a hijab, a surgical mask and a long-sleeved dental gown checking the teeth of a smiling 7-year-old Malay boy (long-sleeved shirt, long trousers) in a dental chair with a small dental mirror, bright clinic. $PPL"
want papaya && gen papaya "Macro food photo of a ripe papaya cut in half showing orange flesh and black seeds on a wooden board, fresh green leaves, soft daylight, no people, no text."
want school && gen school "Morning in a home bathroom: an 8-year-old Malay boy in a white long-sleeved school shirt and long dark blue school trousers brushing his teeth at the mirror, smiling, sunlight through the window. $PPL"
want nenek && gen nenek "A Malay grandmother wearing a hijab and a loose long-sleeved baju kurung and her 6-year-old granddaughter wearing a children's hijab and long-sleeved pyjamas brushing their teeth together in front of a bathroom mirror, both laughing. $PPL"
want timer && gen timer "A happy 7-year-old Malay boy in long-sleeved pyjamas and long pyjama trousers brushing his teeth, looking at a small pink sand timer on the bathroom counter, cheerful, bright bathroom. $PPL"
echo DONE
