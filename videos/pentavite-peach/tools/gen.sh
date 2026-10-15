#!/bin/bash
# Generates the AI cutaways for Pentavite Mixed Peach (owner's ChatGPT/Codex account). Run from the project root.
export PATH=$HOME/.local/bin:$PATH NODE_USE_ENV_PROXY=1
MOD="Photorealistic, natural light, candid lifestyle photography, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
PPL="Everyone is fully and modestly dressed: women and girls wear a hijab that fully covers the hair, neck and chest plus loose long sleeves and a long skirt or loose trousers to the ankles; men and boys wear long sleeves and long trousers to the ankles, never shorts. Malaysian Malay people."
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

want memilih && gen memilih "At a Malaysian family dinner table, a Malay girl about six years old wearing a hijab that fully covers her hair, neck and chest and a loose long-sleeved baju kurung pushes away a plate of green vegetables with a grumpy face, arms crossed, rice and lauk on the table. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want risau && gen risau "A Malay mother in a hijab and loose long-sleeved clothes sitting at the dining table, chin on her hand, looking worried at her young son who is barely eating his food, the boy in a long-sleeved t-shirt and long trousers. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want membesar && gen membesar "A Malay father in a long-sleeved shirt and long trousers marking his young daughter's height with a pencil on a door frame at home, the girl standing straight and smiling, wearing a hijab and a loose long-sleeved dress to the ankles, height pencil marks on the frame, the girl wears socks, framed from the knees up so no bare feet are visible. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want aktif && gen aktif "Three happy Malaysian children running and playing on a grassy field at a playground in the afternoon: a girl in a hijab with loose long-sleeved top and long trousers, two boys in long-sleeved t-shirts and long track pants, energetic motion. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want sekolah && gen sekolah "Morning outside a Malaysian primary school, a smiling Malay girl in a white tudung and blue school pinafore over a long-sleeved white baju kurung and a boy in a long-sleeved white shirt and long navy trousers walking in with school bags, cheerful and healthy. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want peach && gen peach "Close-up of ripe fresh peaches, one cut in half showing the juicy orange flesh and pit, on a light wooden table with soft morning light, no people."
want kunyah && gen kunyah "A Malay girl about five years old wearing a hijab that fully covers her hair, neck and chest and a loose long-sleeved top, smiling while chewing a small round pale chewable vitamin tablet at the kitchen table, her mother in a hijab beside her holding a small plain white supplement bottle with no label text. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want seimbang && gen seimbang "A Malaysian family having a balanced home-cooked meal at the dining table: rice, grilled fish, vegetables, fruit and water; Malay mother in a hijab, father in a long-sleeved baju melayu, a daughter in a hijab and a son in a long-sleeved shirt, everyone smiling. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
echo DONE
