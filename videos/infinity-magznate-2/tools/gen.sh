#!/bin/bash
# Generates the AI cutaways for Tiny Titanz Kid180 #8 (owner's ChatGPT/Codex account). Run from the project root.
# Subjects follow the owner's overlay reference (video rujukan.mp4); every person covers aurat.
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

KID="Every child is fully covered: boys in long-sleeved tops and long trousers to the ankle with socks; girls in a hijab covering hair and neck, long-sleeved loose top and long skirt or trousers. No bare arms or legs."
ADU="Adults fully cover aurat: the man in a long-sleeved shirt and long trousers to the ankle; the woman in a hijab covering hair, neck and chest and a loose long-sleeved baju kurung."
NOPPL="No people anywhere in the frame, no hands, no faces."
want lego && gen lego "A Malay boy about five years old in a long-sleeved t-shirt and long trousers with socks, sitting on a rug building a colourful toy block tower, warm window light, cosy living room, cinematic, horizontal-friendly centred composition. $KID"
want keluarga && gen keluarga "A tall Malay family portrait standing outdoors in a pine forest: a tall father, a tall mother wearing hijab, and their son and daughter, all smiling, warm afternoon light. $ADU $KID"
want makan && gen makan "Close-up of a colourful healthy children's lunch plate with rice, grilled chicken, broccoli, carrots and sliced fruit on a wooden table, natural light. $NOPPL"
want picky && gen picky "A Malay boy about six years old in a long-sleeved t-shirt sitting at a dining table, pushing away a plate of vegetables with a frown, picky eater, warm home light. $KID"
want susu && gen susu "Three tall glasses of fresh milk standing in a row on a white kitchen counter, soft morning light, clean and bright. $NOPPL"
want buah && gen buah "A wooden table filled with fresh fruits and vegetables: apples, oranges, bananas, grapes, broccoli, carrots and leafy greens, vivid colours, natural light. $NOPPL"
echo DONE
