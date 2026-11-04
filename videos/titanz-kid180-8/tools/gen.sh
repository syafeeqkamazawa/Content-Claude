#!/bin/bash
# Generates the AI cutaways for Infinity Probiotics Plus #3 (owner's ChatGPT/Codex account). Run from the project root.
# Subjects follow the owner's overlay reference (Ikut video ni untuk overlay.mp4); every person covers aurat.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, cinematic, natural light, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
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

MEN="A Malay man in his thirties, fully clothed in a long-sleeved shirt and long trousers to the ankle (no bare skin except face, neck and hands)."
NOPPL="No people anywhere in the frame, no hands, no faces."
want dahaga && gen dahaga "A Malay man in his thirties in a long-sleeved t-shirt and long trousers standing in a bright kitchen, gulping a big glass of water, still looking thirsty, morning light. $MEN"
want kembung && gen kembung "A Malay man in his thirties in a long-sleeved hoodie and long trousers to the ankle sitting on a white sofa, both hands pressing his bloated stomach, uncomfortable grimace, bright living room. $MEN"
want penat && gen penat "A Malay man in his thirties wearing long-sleeved pyjamas and long pyjama trousers sitting on the edge of his bed at night, exhausted, head lowered, warm dim bedside lamp, moody cinematic bedroom. $MEN"
want air && gen air "Close-up of clear water being poured from a glass jug into a tall clear drinking glass on a white table, splashes and bubbles, bright clean soft light. $NOPPL"
want makan && gen makan "A Malay man in his thirties in a long-sleeved sweater eating a healthy salad with grilled chicken at a dining table, fork in hand, warm soft light, plates and water glass on the table. $MEN"
want sayur && gen sayur "Overhead close-up of freshly chopped tomatoes, green peppers and cucumbers in a large bowl, vivid colours, natural light. $NOPPL"
want racun && gen racun "A farm worker fully covered in a long-sleeved protective suit, long trousers, boots, gloves, mask and hat spraying pesticide mist over rows of leafy green vegetables in a greenhouse, cinematic haze. Face covered by the mask."
want filter && gen filter "A home kitchen water filter tap filling a clear glass with water, stainless steel sink, soft daylight, close-up. $NOPPL"
want usus && gen usus "Soft watercolour medical illustration of the human digestive system, stomach and intestines in pink and purple tones, dark green clouds of toxins drifting around the gut, a pale translucent body outline, white background, artistic and clean. No text, no labels."
want flush && gen flush "Soft watercolour medical illustration of healthy pink human intestines glowing gently, clear light flowing through the gut as dark toxin particles are washed out and away, white background, artistic and clean. No text, no labels."
want imun && gen imun "Cinematic 3D microscopic render of round white immune cells and tiny glowing probiotic bacteria inside the soft pink lining of the gut, shallow depth of field. No text, no labels."
want kolesterol && gen kolesterol "Cinematic 3D medical render of a blood vessel cross-section with red blood cells flowing and yellow fatty cholesterol plaque on the artery wall, shallow depth of field. No text, no labels."
want fokus && gen fokus "A Malay man in his thirties in a long-sleeved shirt sitting at a wooden desk with a laptop and a cup of coffee, hand on his chin, deep in thought, warm window light, bookshelf behind. $MEN"
want mood && gen mood "A Malay man in his thirties in a long-sleeved shirt sitting by a sunny window at home, relaxed calm smile, holding a mug, warm golden morning light. $MEN"
want jerawat && gen jerawat "Extreme close-up of the cheek of a Malay man in his thirties with red acne breakout pimples on his skin, natural skin texture, soft side light, shallow depth of field."
want sembab && gen sembab "A Malay man in his thirties in a long-sleeved shirt looking at his puffy swollen face in the bathroom mirror in the morning, touching his cheek, soft light. $MEN"
want bloated && gen bloated "A Malay man in his thirties in a long-sleeved shirt and long trousers standing in a kitchen, one hand on his swollen bloated belly over his shirt, uncomfortable, after a meal, plates on the counter. $MEN"
want najis && gen najis "Studio photo of small dark brown hard round lumpy pellets scattered and floating on a seamless pure white background, soft shadows, clean minimal composition, abstract and not gross. $NOPPL"
want muka && gen muka "Side profile close-up of the lower face and neck of a Malay man in his thirties with a puffy swollen face and a double chin, wearing a crew-neck long-sleeved white t-shirt, plain bright blue studio background. $MEN"
echo DONE
