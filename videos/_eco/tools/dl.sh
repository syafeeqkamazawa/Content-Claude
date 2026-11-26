#!/bin/bash
# Download every clip, then contact sheet + 16 kHz wav + VAD + whisper word list per clip.
S=/tmp/claude-0/-home-user-Content-Claude/41d1742a-4e75-532a-ab6a-7c00864fdcfc/scratchpad
cd /home/user/Content-Claude/videos/_eco
while read id n; do
  [ -s src/$n.mp4 ] || curl -sL -o src/$n.mp4 "https://drive.usercontent.google.com/download?id=$id&export=download&confirm=t"
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 src/$n.mp4); echo "$n $d" >> .media/dur.txt
done < ids.txt
echo DL-DONE >> .media/dl.log
while read id n; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 src/$n.mp4); st=$(python3 -c "print(max(1.5,$d/30))")
  ffmpeg -nostdin -v error -y -i src/$n.mp4 -vf "fps=1/$st,scale=-2:240,drawtext=text='%{pts\:flt}':x=3:y=3:fontsize=16:fontcolor=yellow:box=1:boxcolor=black,tile=10x3" -frames:v 1 .media/cs-$n.jpg
  ffmpeg -nostdin -v error -y -i src/$n.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le .media/$n.wav
  python3 $S/vad.py .media/$n.wav 350 2>/dev/null | sed 's/ //g' > .media/vad-$n.txt < /dev/null
  python3 $S/wl.py .media/$n.wav "Robot vacuum Ecovacs, beg kuning, harga promo." > .media/wl-$n.txt 2>/dev/null < /dev/null
  echo "$n" >> .media/dl.log
done < ids.txt
echo ALL-DONE >> .media/dl.log
