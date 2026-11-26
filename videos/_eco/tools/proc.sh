#!/bin/bash
# (Re)process clips that have no transcript yet: contact sheet, wav, VAD, word list. Reads ids.txt + ids2.txt.
S=/tmp/claude-0/-home-user-Content-Claude/41d1742a-4e75-532a-ab6a-7c00864fdcfc/scratchpad
cd /home/user/Content-Claude/videos/_eco
cat ids.txt ids2.txt > .media/allids.txt
while read id n; do
  [ -s src/$n.mp4 ] || curl -sL -o src/$n.mp4 "https://drive.usercontent.google.com/download?id=$id&export=download&confirm=t" < /dev/null
  [ -s .media/wl-$n.txt ] && [ -s .media/cs-$n.jpg ] && continue
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 src/$n.mp4 < /dev/null); st=$(python3 -c "print(max(1.5,$d/30))")
  grep -q "^$n " .media/dur.txt || echo "$n $d" >> .media/dur.txt
  ffmpeg -nostdin -v error -y -i src/$n.mp4 -vf "fps=1/$st,scale=-2:240,drawtext=text='%{pts\:flt}':x=3:y=3:fontsize=16:fontcolor=yellow:box=1:boxcolor=black,tile=10x3" -frames:v 1 .media/cs-$n.jpg
  ffmpeg -nostdin -v error -y -i src/$n.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le .media/$n.wav
  python3 $S/vad.py .media/$n.wav 350 2>/dev/null < /dev/null | sed 's/ //g' > .media/vad-$n.txt
  python3 $S/wl.py .media/$n.wav "Robot vacuum Ecovacs, beg kuning, harga promo." > .media/wl-$n.txt 2>/dev/null < /dev/null
  [ -s .media/wl-$n.txt ] || echo "#empty" > .media/wl-$n.txt
  echo "$n" >> .media/proc.log
done < .media/allids.txt
echo PROC-DONE >> .media/proc.log
