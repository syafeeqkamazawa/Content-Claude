#!/bin/bash
# Generates the AI cutaways for Jubah Hitam #3 (owner's ChatGPT/Codex account). Run from the project root.
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
MEN="Men wearing long jubah or baju Melayu with long trousers and kopiah, fully covered, seen from behind."
want jemaah && gen jemaah "$MEN A row of men praying in congregation inside a calm Malaysian mosque, soft daylight through arched windows. $PLAIN"
want jumaat && gen jumaat "Exterior of a beautiful Malaysian mosque on a sunny Friday noon, white domes and minaret against blue sky, palm trees. $NOPPL $PLAIN"
want raya && gen raya "A Malaysian home on Hari Raya morning: ketupat, rendang and kuih on a dining table, green and gold decorations, warm festive light. $NOPPL $PLAIN"
echo DONE
