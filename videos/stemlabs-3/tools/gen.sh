#!/bin/bash
# Generates the AI cutaways for StemLabs Fish Oil #3 (owner's ChatGPT/Codex account). Run from the project root.
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

want ikan && gen ikan "A Malaysian family at a home dining table enjoying grilled mackerel fish, rice and vegetables; the father in a long-sleeved baju melayu, the mother in a hijab that fully covers her hair, neck and chest, a teenage daughter in a hijab and a son in a long-sleeved shirt, warm natural light, the fish dish in the foreground. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want jantung && gen jantung "A healthy Malay couple in their sixties taking a brisk morning walk in a green Malaysian park; the husband in a kopiah, long-sleeved t-shirt and long track pants to the ankles, the wife in a hijab that fully covers her hair, neck and chest with a loose long-sleeved top and long loose trousers, both smiling, sunrise light. $PPL"
want otak && gen otak "A Malay teenage girl wearing a hijab that fully covers her hair, neck and chest and a loose long-sleeved baju kurung studying at a desk with books and a laptop, focused and alert, writing notes, warm desk lamp, home study room. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want mata && gen mata "A Malay woman in her forties wearing a hijab that fully covers her hair, neck and chest and loose long sleeves reading a book comfortably by a bright window, clear relaxed eyes, close medium shot of her face and the book, soft daylight. $PPL"
want warga && gen warga "A Malay grandfather in a kopiah, long-sleeved baju melayu and long trousers and a grandmother in a hijab that fully covers her hair, neck and chest and a loose long baju kurung playing happily with their young grandson in a long-sleeved shirt and long trousers in a home garden, energetic and healthy. $PPL Girls wear a hijab that fully covers the hair, neck and chest with loose long sleeves and a long skirt or loose trousers to the ankles; boys wear long sleeves and long trousers to the ankles."
want rutin && gen rutin "A Malay man in his forties wearing a kopiah and a long-sleeved shirt sitting at a breakfast table holding one golden fish oil softgel capsule between his fingers with a glass of water, a plain white supplement bottle with no label text on the table, morning kitchen light. $PPL"
echo DONE
