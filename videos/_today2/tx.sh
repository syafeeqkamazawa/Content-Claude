#!/bin/bash
S=/tmp/claude-0/-home-user-Content-Claude/41d1742a-4e75-532a-ab6a-7c00864fdcfc/scratchpad
cd /home/user/Content-Claude/videos/_today2
for f in 141927 143318 145027 145505 150449 150734 151016 151316 151856 152300; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 src/$f.mp4); st=$(python3 -c "print(max(3,$d/24))")
  ffmpeg -v error -y -i src/$f.mp4 -vf "fps=1/$st,scale=-2:200,drawtext=text='%{pts\:flt}':x=3:y=3:fontsize=16:fontcolor=yellow:box=1:boxcolor=black,tile=12x2" -frames:v 1 .media/cs/$f.jpg
  ffmpeg -v error -y -i src/$f.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le .media/$f.wav
  python3 $S/wl.py .media/$f.wav "Beg kuning, harga promo." > .media/wl-$f.txt 2>/dev/null
  python3 $S/vad.py .media/$f.wav 350 2>/dev/null | sed 's/ //g' > .media/vad-$f.txt
  echo "$f done" >> .media/tx.log
done
echo ALL >> .media/tx.log
