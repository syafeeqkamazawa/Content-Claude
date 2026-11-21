#!/bin/bash
# Renders the batch projects listed in videos/_today/queue.txt one by one (1440x2560, 60 fps, ~20 Mbps final).
S=/tmp/claude-0/-home-user-Content-Claude/41d1742a-4e75-532a-ab6a-7c00864fdcfc/scratchpad
cd /home/user/Content-Claude/videos/_today
while true; do
  slug=$(grep -v "^#" queue.txt | head -1); [ "$slug" = "END" ] && break; [ -z "$slug" ] && { sleep 30; continue; }
  P=/home/user/Content-Claude/videos/$slug
  rm -rf /tmp/hyperframes-extract-cache-0/hfcache-v6-* $P/.media/snap
  bash $S/render.sh $P > $S/render-$slug.log 2>&1
  rm -f $P/renders/P-master.mp4
  echo "$slug $(tail -1 $S/render-$slug.log)" >> done.txt
  sed -i "0,/^$slug\$/s//#$slug/" queue.txt
done
echo QUEUE-EMPTY
