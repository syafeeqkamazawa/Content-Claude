#!/bin/bash
# after the first four builds: redo the perfume A2 photo, then AI + builds for n05/n07/n08
cd /home/user/Content-Claude
L=videos/_today2/.media
until grep -q BUILD1-DONE $L/build2.log 2>/dev/null; do sleep 20; done
python3 videos/_today/tools/gen_ai.py n02 > /dev/null 2>&1
python3 videos/_today/tools/make.py n02 --no-media >> $L/build2.log 2>&1
echo N02-REDONE >> $L/build2.log
python3 videos/_today/tools/gen_ai.py n05 n07 n08 > /dev/null 2>&1
for k in n05 n07 n08; do python3 videos/_today/tools/make.py $k >> $L/build3.log 2>&1; done
echo BUILD3-DONE >> $L/build3.log
