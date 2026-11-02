#!/bin/bash
# Generates the AI cutaways for Nature's Key Magnesium #2 (owner's ChatGPT/Codex account). Run from the project root.
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

MEN="A Malay man in his thirties, fully clothed in a long-sleeved shirt and long trousers to the ankle (no bare skin except face, neck and hands)."
SQ="Square 1:1 crop composition, subject centred, clean soft background."
NOPPL="No people anywhere in the frame, no hands, no faces."
STUDIO="Seamless pure white studio background, soft diffused light, gentle shadows, crisp macro product photography, no text, no labels, no logos."
want i_muka && gen i_muka "Close-up portrait of a Malay man in his thirties with a puffy round swollen face and full cheeks, wearing a long-sleeved shirt, neutral expression, plain light wall. $MEN $SQ"
want i_perut && gen i_perut "A Malay man in his thirties standing side-on, his round belly bulging under a tight long-sleeved shirt tucked into long trousers with a belt, no skin showing, plain light room. $MEN $SQ"
want i_dagu && gen i_dagu "Side profile close-up of a Malay man in his thirties with a double chin, wearing a buttoned long-sleeved shirt with collar, plain light wall. $MEN $SQ"
want i_bawahmata && gen i_bawahmata "Extreme close-up of the tired eyes of a Malay man with dark circles and puffy eye bags under the eyes, natural skin texture, soft light. $SQ"
want i_tengkuk && gen i_tengkuk "A Malay man in his thirties seen from behind and slightly to the side, thick neck and rounded upper back under a long-sleeved polo shirt, hand rubbing the back of his neck, plain light room. $MEN $SQ"
want i_lesu && gen i_lesu "A Malay man in his thirties in a long-sleeved shirt slumped on a sofa with low energy, rubbing his forehead, afternoon light, living room. $MEN $SQ"
want f_tidur && gen f_tidur "A Malay man in his thirties wearing long-sleeved pyjamas lying awake in bed at night staring at the ceiling, eyes open, bedside clock glowing, moonlight, blanket covering him up to the chest. Cinematic, vertical 9:16. $MEN"
want f_mata && gen f_mata "Extreme macro close-up of one eye of a Malay man, the lower eyelid twitching, natural skin texture, cinematic shallow depth of field, vertical 9:16."
want f_telinga && gen f_telinga "Close-up of a Malay man in his thirties wearing a long-sleeved shirt pressing his hand against his ear with a pained expression as if hearing a ringing sound, shallow depth of field, cinematic, vertical 9:16. $MEN"
want f_stres && gen f_stres "A Malay man in his thirties in a long-sleeved office shirt and long trousers at his desk, head in his hands, stressed and frustrated, papers and laptop, moody window light, cinematic, vertical 9:16. $MEN"
want p_kapsul && gen p_kapsul "Several white capsules tumbling out of a tilted plain white supplement bottle onto a white surface, frozen in mid-air, $STUDIO Vertical 9:16. $NOPPL"
want p_zinc && gen p_zinc "Cream-coloured round tablets falling out of a tilted plain amber glass bottle onto a white surface, frozen in mid-air, $STUDIO Vertical 9:16. $NOPPL"
want p_softgel && gen p_softgel "Golden softgel capsules falling out of a tilted plain amber glass bottle onto a white surface, frozen in mid-air, $STUDIO Vertical 9:16. $NOPPL"
want i_berat && gen i_berat "A Malay man in his thirties in a long-sleeved shirt and long trousers to the ankle with socks standing on a bathroom weighing scale, looking down at it worried, clean bathroom. $MEN $SQ"
echo DONE
