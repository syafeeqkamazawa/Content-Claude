#!/bin/bash
# Generates the AI cutaways for Kurta Zeke #1 (owner's ChatGPT/Codex account). Run from the project root.
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
MAN="A Malay man in his thirties wearing a plain black long kurta tunic with a V neck and three-quarter sleeves over long loose black trousers to the ankle, songkok or no hat. No logos, no readable text."
want kenduri && gen kenduri "$MAN He is smiling and greeting guests at a Malay wedding kenduri under a white canopy, warm daylight, other guests in modest baju Melayu and hijab blurred behind. Everyone fully covered."
want tarawih && gen tarawih "$MAN He is walking into a mosque at night for tarawih prayers, warm lights, carpeted hall, other men in long robes and trousers behind, cinematic."
want wuduk && gen wuduk "Close-up of a Malay man in a black three-quarter sleeve kurta and long trousers washing his forearms at a mosque ablution tap, water splashing, the short sleeves stay dry above the elbow. Face partly visible. No logos."
want selesa && gen selesa "$MAN He is standing relaxed and comfortable on a breezy evening terrace, gentle wind, smiling, warm golden light, cinematic."
want smart && gen smart "$MAN He is standing confidently in front of a modern house, looking sharp and well groomed, adjusting his sleeve, golden hour light, full body with ankle-length trousers visible."
want stok && gen stok "An almost empty clothing rack in a small modern boutique with only a few empty hangers left, soft daylight, minimal. $NOPPL"
echo DONE
