#!/bin/bash
# Appends each product to queue.txt once its media build logs "pieces" (and no KeyError right before it).
cd /home/user/Content-Claude/videos/_today
seen=$(grep -c "pieces" .media/build-media.log)
while [ "$(grep -c pieces .media/build-media.log)" -lt 17 ]; do
  n=$(grep -c "pieces" .media/build-media.log)
  if [ "$n" -gt "$seen" ]; then
    python3 - "$seen" <<'P' >> queue.txt
import sys
L = open(".media/build-media.log").read().splitlines()
k = 0
for i, l in enumerate(L):
    if "pieces" in l:
        k += 1
        if k > int(sys.argv[1]):
            bad = i > 0 and "Error" in L[i - 1]
            print(("#needsfix-" if bad else "") + l.split()[0])
P
    seen=$n
  fi
  sleep 30
done
