#!/bin/bash
# Generates the AI cutaways for Infinity Probiotics #5 / Buku Tahajud #2 (9 Nov) (owner's ChatGPT/Codex account). Run from the project root.
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
want nafas && gen nafas "A Malaysian man in his thirties wearing a loose long-sleeved shirt and long trousers, cupping his hand in front of his mouth to check his breath, a slightly worried expression, standing in a bright modern bathroom by the mirror, natural light. Fully clothed, modest. $PLAIN"
want gigi && gen gigi "Close-up of a toothbrush with fresh toothpaste resting on the edge of a clean white bathroom sink beside a glass of water, soft morning light, shallow depth of field. $NOPPL $PLAIN"
want doa && gen doa "A Malaysian Muslim man wearing a loose white baju melayu with long sleeves, long trousers and a white kopiah, sitting on a prayer mat in a dim bedroom at night, raising both hands in doa, warm lamp light, moonlight through the window, peaceful, seen from the side. Fully clothed, modest. $PLAIN"
echo DONE
