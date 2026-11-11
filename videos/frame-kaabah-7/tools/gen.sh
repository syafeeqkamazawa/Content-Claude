#!/bin/bash
# Generates the AI cutaways for Frame Kaabah #6-#10 (11 Nov) (owner's ChatGPT/Codex account). Run from the project root.
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
want ukur && gen ukur "A Malaysian man wearing a loose long-sleeved shirt and long trousers measuring a bare living-room wall above a sofa with a yellow tape measure, seen from behind at an angle, bright daylight, clean modern home. Fully clothed, modest. $PLAIN"
want wayar && gen wayar "Messy tangled black electrical cables and power adapters hanging down a white living-room wall behind a TV console, untidy, realistic home interior, daylight. $NOPPL $PLAIN"
want bateri && gen bateri "Close-up of three plain AA batteries lying on a light wooden table, soft daylight, shallow depth of field, no labels. $NOPPL $PLAIN"
want paku && gen paku "Close-up of three small steel wall nails and a small hammer on a light wooden table next to a white wall, soft daylight, shallow depth of field. $NOPPL $PLAIN"
want pindah && gen pindah "A Malaysian family moving into a new house, a man in a loose long-sleeved shirt and long trousers and a woman in a loose long dress with a hijab covering hair, neck and chest carrying cardboard boxes into a bright empty living room, smiling. Fully clothed, modest. $PLAIN"
want hamper && gen hamper "A wrapped gift hamper basket with cellophane and a ribbon, filled with snacks and cups, on a wooden table in a bright home, close-up. $NOPPL $PLAIN"
echo DONE
