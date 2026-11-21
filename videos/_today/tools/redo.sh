#!/bin/bash
# Caption fix (bagi/baik had been mapped to 'beg'): rebuild media for the delivered videos once the source is back, then queue them.
cd /home/user/Content-Claude
SZ=6495225741
until [ "$(stat -c %s videos/_today/src/120947.mp4 2>/dev/null)" = "$SZ" ] && ! pgrep -f "download?id=11BGG" > /dev/null; do sleep 20; done
for k in p13 p12 p15 p11 p02 p04 p05 p07 p09; do
  python3 videos/_today/tools/make.py $k >> videos/_today/.media/redo.log 2>&1
  slug=$(python3 -c "import sys; sys.path.insert(0,'videos/_today/tools'); from specs import SPECS; print(SPECS['$k']['slug'])")
  if tail -3 videos/_today/.media/redo.log | grep -q Error; then echo "#needsfix-$slug" >> videos/_today/queue.txt; else echo "$slug" >> videos/_today/queue.txt; fi
done
echo REDO-BUILT >> videos/_today/.media/redo.log
