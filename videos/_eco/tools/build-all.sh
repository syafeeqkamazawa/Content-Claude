#!/bin/bash
cd /home/user/Content-Claude/videos
python3 _today/tools/gen_ai.py e20 e21 e22 > _eco/.media/gen.out 2>&1
for n in $(seq -w 1 26); do echo "== e$n" >> _eco/.media/build.log; python3 _today/tools/make.py e$n >> _eco/.media/build.log 2>&1; done
echo BUILD-DONE >> _eco/.media/build.log
