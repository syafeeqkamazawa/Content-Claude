#!/bin/bash
# Generates the AI cutaways for Aurapep Krill Oil #8 (owner's ChatGPT/Codex account). Run from the project root.
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

SPACE="Composition: the subject sits in the lower 55% of the vertical frame and the upper 40% is calm empty background (plain wall, ceiling, sky or soft bokeh) with nothing important in it."
FEET="Every woman wears socks and her long skirt reaches the floor; no bare feet or ankles visible anywhere."
want kulit && gen kulit "A Malay woman in her thirties wearing a hijab that covers her hair, neck and chest and a loose long-sleeved blouse with a long skirt, choosing skincare products from a brightly lit pharmacy shelf with a shopping basket, seen from a little distance so she is in the lower half of the frame with the plain store ceiling above, no readable brand names. $FEET $SPACE $PPL"
want terlupa && gen terlupa "A busy Malay man in his thirties in a long-sleeved office shirt eating a cup of instant noodles at his cluttered office desk late at night while staring at his laptop, seen from a little distance so he is in the lower half of the frame with a plain dark wall above, no readable brand names. $SPACE $PPL"
want ais && gen ais "Wide photograph of Antarctic sea ice floes drifting on calm deep blue ocean water in the lower half of the frame under a soft pale sky, a few distant icebergs, no people, no text. $SPACE"
want jantung && gen jantung "A healthy Malay couple in their forties cycling side by side on a park path in the morning: the wife in a sports hijab covering her hair, neck and chest, a loose long-sleeved top and long loose pants with socks and shoes, the husband in a long-sleeved sports top and long track pants to the ankle, smiling, seen from a distance so they are in the lower half of the frame with open sky and tree tops above. $FEET $SPACE $PPL"
want otak && gen otak "A Malay grandfather in a kopiah, long-sleeved baju melayu and long trousers to the ankle playing a traditional congkak board game with his young granddaughter in a small hijab and long-sleeved baju kurung on a mat in the living room, both concentrating and smiling, seen from a little distance so they are in the lower half of the frame with a plain wall above. $FEET $SPACE $PPL"
want softgel && gen softgel "Close-up photograph of glossy translucent deep red softgel capsules being poured from a plain white unlabeled bottle into a cupped palm, a long sleeve visible at the wrist, in the lower half of the frame, soft daylight, plain light background above, no labels, no faces, no text. $SPACE"
want cermin && gen cermin "A Malay woman in her thirties adjusting her hijab, which covers her hair, neck and chest, in front of a bedroom mirror while wearing a loose long-sleeved baju kurung, seen from a little distance so she is in the lower half of the frame with a plain wall above, soft morning light. $FEET $SPACE $PPL"
want makan && gen makan "A Malay family having a balanced home dinner of grilled fish, vegetables, rice and fruit at the dining table: mother in a hijab covering her hair, neck and chest and a loose long-sleeved dress, father in a long-sleeved shirt and long trousers, two children in long sleeves, the girl in a small hijab, smiling, seen from a little distance so they are in the lower half of the frame with a plain warm wall above. $FEET $SPACE $PPL"
want belanja && gen belanja "A Malay woman wearing a hijab that covers her hair, neck and chest and a loose long-sleeved blouse sitting on a sofa at home, smiling while shopping online on her smartphone, the phone screen blurred and unreadable, seen from a little distance so she is in the lower half of the frame with a plain warm wall above, no logos, no text. $FEET $SPACE $PPL"
echo DONE
