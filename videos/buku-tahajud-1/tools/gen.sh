#!/bin/bash
# Generates the AI cutaways for Buku Hidup Dengan Tahajud #1 (owner's ChatGPT/Codex account). Run from the project root.
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
MAN="A Malaysian Malay man in his thirties wearing a long-sleeved baju Melayu, a kopiah and long trousers to the ankle, fully covered."
want tahajud && gen tahajud "$MAN He prays tahajud alone at night, standing on a prayer mat in a dim quiet bedroom lit by one warm lamp, peaceful, seen from behind at a respectful distance. $PLAIN"
want tidur && gen tidur "$MAN He sleeps peacefully in bed under a blanket after isyak, a folded prayer mat and an alarm clock showing 3:30 on the bedside table, dark blue night light. $PLAIN"
want malam && gen malam "A quiet Malaysian bedroom at 3am: a prayer mat laid out facing a window with moonlight, a small Quran stand and a warm lamp, calm spiritual mood. $NOPPL $PLAIN"
echo DONE
