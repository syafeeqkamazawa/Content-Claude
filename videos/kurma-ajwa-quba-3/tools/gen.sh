#!/bin/bash
# Generates the AI cutaways for Quba Food Kurma Ajwa #1 (owner's ChatGPT/Codex account). Run from the project root.
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
want madinah && gen madinah "The green dome and white minarets of the Prophet's Mosque in Madinah at golden hour, wide cinematic view, warm sky, no crowds in focus. $NOPPL"
want ladang && gen ladang "A lush date palm orchard in Madinah with heavy bunches of dark ajwa dates hanging from the palms, golden afternoon light, cinematic. $NOPPL"
want sains && gen sains "Extreme macro of glossy dark brown ajwa dates on a white surface, rich texture, soft studio light, shallow depth of field. $NOPPL"
want iftar && gen iftar "A Ramadan iftar table at sunset with a bowl of dark ajwa dates, glasses of water and dishes, warm lantern light, cinematic. $NOPPL"
echo DONE
