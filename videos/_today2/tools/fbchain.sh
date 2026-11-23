#!/bin/bash
cd /home/user/Content-Claude/videos
K=$(for n in $(seq -w 1 20); do echo fb$n; done)
python3 _today/tools/gen_ai.py $K > _today2/.media/fb-gen.out 2>&1
for k in $K; do python3 _today/tools/make.py $k >> _today2/.media/fb-build.log 2>&1; done
echo FB-BUILT >> _today2/.media/fb-build.log
