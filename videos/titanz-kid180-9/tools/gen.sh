#!/bin/bash
# Generates the AI cutaways for Tiny Titanz Kid180 #9 (owner's ChatGPT/Codex account). Run from the project root.
# Subjects follow the owner's overlay reference (video rujukan 2.mp4); every person covers aurat.
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
NOPPL="No people anywhere in the frame, no hands, no faces."
want kelas && gen kelas "Cheerful Malay kindergarten children about five years old sitting at a low table in a bright classroom, smiling and active, playing with toys. $KID"
want rendah && gen rendah "Four Malay children about eight years old standing side by side against a white wall in a school corridor; one boy is clearly shorter than his friends and looks up at them, cinematic natural light. $KID"
want memilih && gen memilih "A Malay girl about six years old wearing a hijab and a long-sleeved top sitting at a dining table, turning her face away from a spoon of vegetables, picky eater, warm home light. $KID"
want susu9 && gen susu9 "Milk being poured from a glass jug into one of three tall glasses on a wooden breakfast table, splash, soft morning light. $NOPPL"
want buah9 && gen buah9 "A wicker basket overflowing with fresh fruits and vegetables: oranges, apples, strawberries, carrots, broccoli and spinach on a kitchen counter, vivid colours, natural light. $NOPPL"
echo DONE
