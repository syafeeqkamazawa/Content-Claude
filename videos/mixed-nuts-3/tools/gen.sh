#!/bin/bash
# Generates the AI cutaways for Mixed Nuts #1/#2 (owner's ChatGPT/Codex account). Run from the project root.
# Subjects follow the owner's overlay reference (video rujukan.mp4 (Krill)); every person covers aurat.
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

NOPPL="No people anywhere in the frame, no hands, no faces."
KID="Every child is fully covered: girls in a hijab covering hair and neck, a long-sleeved loose dress or top and long trousers; boys in long sleeves and long trousers. No bare arms or legs."
MAN="A Malay man in his thirties fully clothed in a long-sleeved t-shirt and long trousers to the ankle."
PLAIN="No brand names, no logos, no readable text on any packaging."
want bekas && gen bekas "A tall clear plastic snack container filled to the top with roasted mixed nuts and dried fruit (walnuts, cashews, almonds, pumpkin seeds, raisins, cranberries) on a white marble table in a cosy living room, warm light. $NOPPL $PLAIN"
want tuang && gen tuang "Mixed nuts and dried fruit pouring from a plain unbranded kraft pouch into a clear plastic container on a white table, motion frozen, warm home light. $PLAIN Only a hand holding the pouch, in a long sleeve."
want anak && gen anak "A cheerful Malay girl about four years old wearing a pastel hijab and a long-sleeved dress sitting at a white table, happily eating a walnut from a clear container of mixed nuts, cartoons on a TV blurred behind her. $KID $PLAIN"
want walnut && gen walnut "Close-up of a clear food tray full of mixed nuts with many large walnut halves, cashews, almonds, pumpkin seeds and dark raisins, top-down, held by two hands in long sleeves, soft light. $PLAIN"
want jajan && gen jajan "A Malay boy about seven in a long-sleeved t-shirt and long trousers sitting on the sofa reaching past colourful unbranded chip packets towards a bowl of mixed nuts, warm home light. $KID $PLAIN"
want susu && gen susu "Top-down close-up of a white bowl of mixed nuts and dried fruit with fresh milk being poured in from a plain carton, a spoon in the bowl, wooden table, warm cafe light. $PLAIN Only a hand in a long sleeve."
want yogurt && gen yogurt "Close-up of a white bowl of thick plain yogurt topped with mixed nuts, walnuts, almonds, cashews and raisins, a spoon lifting a bite, wooden table, soft light. $NOPPL $PLAIN"
want maggi && gen maggi "A Malay man in his thirties in a long-sleeved t-shirt and long trousers sitting at the kitchen table late at night eating a bowl of instant noodles, dim warm light, tired, cinematic. $MAN $PLAIN"
want kacang && gen kacang "Three small heaps of raisins, almonds and cashews side by side on a white wooden board, crisp macro food photography, soft light. $NOPPL $PLAIN"
want sudu && gen sudu "Top-down close-up of a spoon scooping milk-soaked mixed nuts from a white bowl on a wooden table, cafe light. $PLAIN Only a hand in a long sleeve."
echo DONE
