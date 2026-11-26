#!/bin/bash
# Privacy blur applied to Ecovacs finals after render (re-run after any re-render of #7 / #9).
#  #7: owner's e-mail + generated password in the app sign-up screen recording (17.9-31.0 s, band y 560-1760).
#  #9: phone home screen / wallpaper flashes between recordings (29.7-31.98 s); CTA card + caption kept sharp.
V=/home/user/Content-Claude/videos
ENC="-c:v libx264 -preset slow -profile:v high -b:v 19M -maxrate 23M -bufsize 40M -r 60 -pix_fmt yuv420p -c:a copy -movflags +faststart"
f=$V/ecovacs-t30c-7/renders/ecovacs-t30c-7-final.mp4
[ -f $f ] && ffmpeg -nostdin -v error -y -i $f -filter_complex "[0:v]crop=1440:1200:0:560,boxblur=28:3[b];[0:v][b]overlay=0:560:enable='between(t,17.9,31.0)'" $ENC ${f%.mp4}-b.mp4 && mv ${f%.mp4}-b.mp4 $f
f=$V/ecovacs-t30c-9/renders/ecovacs-t30c-9-final.mp4
[ -f $f ] && ffmpeg -nostdin -v error -y -i $f -filter_complex "[0:v]split=4[a][b][c][d];[b]boxblur=40:4[bl];[c]crop=1320:635:60:930[card];[d]crop=680:110:380:1735[cap];[a][bl]overlay=0:0:enable='between(t,29.7,31.98)'[x];[x][card]overlay=60:930:enable='between(t,29.7,31.98)'[y];[y][cap]overlay=380:1735:enable='between(t,29.7,31.98)'" $ENC ${f%.mp4}-b.mp4 && mv ${f%.mp4}-b.mp4 $f
