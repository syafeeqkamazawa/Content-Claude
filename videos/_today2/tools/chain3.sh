#!/bin/bash
# My First Book #1 + Leveled Reading: AI photos then builds, after chain2 finishes
cd /home/user/Content-Claude
L=videos/_today2/.media
until grep -q BUILD3-DONE $L/build3.log 2>/dev/null; do sleep 20; done
python3 videos/_today/tools/gen_ai.py n06 n09 > /dev/null 2>&1
for k in n06 n09; do python3 videos/_today/tools/make.py $k >> $L/build4.log 2>&1; done
echo BUILD4-DONE >> $L/build4.log
