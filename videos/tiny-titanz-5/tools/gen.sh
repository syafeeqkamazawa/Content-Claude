#!/bin/bash
# Generates the AI cutaways for Tiny Titanz 180+ #5 (owner's ChatGPT/Codex account). Run from the project root.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, natural light, candid lifestyle photography, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
PPL="Everyone is modestly dressed with full aurat coverage (no shorts, no bare arms or legs). Malaysian Malay people."
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

want sihat && gen sihat "Healthy, cheerful Malay children playing tag on a school field in the morning: boys in long-sleeved school shirts and long trousers, girls in white tudung covering hair, neck and chest with long baju kurung school uniforms, energetic and laughing, bright sunlight. $PPL"
want risau && gen risau "A thoughtful Malay mother in a hijab covering her hair, neck and chest and a loose long-sleeved blouse sitting at the dining table at home, chin resting on her hand, watching her young son eat with a worried, wondering expression, soft daylight. $PPL"
want sayur && gen sayur "A Malay boy of about six in a long-sleeved t-shirt and long pants at the dinner table pushing away a plate of broccoli and carrots with a grumpy face, arms crossed, warm home lighting. $PPL"
want buah && gen buah "A little Malay girl of about five in a small hijab covering her hair, neck and chest and a long-sleeved dress turning her head away from a bowl of cut fruit her mother's hand offers, playful refusal, bright kitchen. $PPL"
want gigi && gen gigi "A happy Malay girl of about seven in a hijab covering her hair, neck and chest and long-sleeved pyjamas brushing her teeth at a bathroom sink, smiling with healthy white teeth in the mirror reflection, bright morning light. $PPL"
want sukan && gen sukan "Malay primary school children running a race on school sports day, boys in long-sleeved sports shirts and long track pants, girls in sports tudung covering hair, neck and chest with long-sleeved tops and long track pants, a teacher cheering, sunny field, energetic. $PPL"
want dukung && gen dukung "A Malay father in a long-sleeved shirt and long trousers carrying his laughing daughter on his shoulders in a park at golden hour, the daughter in a small hijab covering her hair, neck and chest and a long-sleeved dress with long pants, the mother in a hijab covering her hair, neck and chest and a loose long dress walking beside them smiling. $PPL"
echo DONE
