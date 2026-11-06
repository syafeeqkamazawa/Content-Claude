#!/bin/bash
# Generates the AI cutaways for Aurapep Shilajit #7 (owner's ChatGPT/Codex account). Run from the project root.
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
PLAIN="No brand names, no logos, no readable text."
MAN="A Malaysian Malay man in his thirties wearing a long-sleeved shirt and long trousers to the ankle, fully covered."
want resin && gen resin "Close-up of raw dark shilajit resin, sticky and tar-like, on a small wooden spoon beside a small open glass jar, dark moody studio light. $NOPPL $PLAIN"
want reishi && gen reishi "Fresh glossy red reishi (lingzhi) mushrooms on a wooden board with a few dried slices, natural soft light, clean studio background. $NOPPL $PLAIN"
want pagi && gen pagi "$MAN He sits on the edge of his bed early in the morning rubbing his eyes, still sleepy, alarm clock on the bedside table, soft dawn light in a Malaysian bedroom. $PLAIN"
want petang && gen petang "$MAN He sits at an office desk at 2pm, tired and heavy-eyed, hand on his forehead, laptop open, afternoon light. $PLAIN"
echo DONE
