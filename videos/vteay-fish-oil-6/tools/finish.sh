#!/bin/bash
# VTEAY #6 (owner 10 Nov: only add problem/benefit overlays, leave caption / voice / cuts alone).
# Puts the owner's burned-in caption back on top of the full-screen overlays: the white caption text is
# keyed from the original edit (bright AND colour-neutral pixels in the caption band — grass is green and
# skin is red, so neither passes), given a soft dark shadow like the original, and laid over the render
# only while an overlay is up. The original audio stream is copied unchanged.
# Usage (project root): tools/finish.sh renders/<name>-final.mp4 assets/a.mp4 "<enable expr>"
set -e
R=$1; O=$2; EN=$3; OUT=${R%.mp4}-cap.mp4
KEY="lum='if(gt(lum(X,Y),160)*lt(abs(cb(X,Y)-128),14)*lt(abs(cr(X,Y)-128),14)*gt(X,215)*lt(X,865),255,0)':cb=128:cr=128"
ffmpeg -nostdin -v error -y -i "$R" -i "$O" -filter_complex "\
[1:v]crop=1080:200:0:1280,format=yuv444p,geq=$KEY,format=gray,erosion,erosion,dilation,dilation,scale=1440:267,gblur=sigma=0.7,split[m1][m2];\
[m2]dilation,dilation,dilation,gblur=sigma=5,lut=y='val*0.75'[ms];\
color=c=0xF7F3E6:s=1440x267:r=60,format=rgba[w];color=c=black:s=1440x267:r=60,format=rgba[k];\
[w][m1]alphamerge[txt];[k][ms]alphamerge[sh];\
[0:v][sh]overlay=x=5:y=1713:shortest=1:enable='$EN'[a1];[a1][txt]overlay=x=0:y=1707:shortest=1:enable='$EN'[v]" \
  -map "[v]" -map 1:a -c:v libx264 -preset slow -b:v 20M -maxrate 24M -bufsize 40M -pix_fmt yuv420p -c:a copy -movflags +faststart "$OUT"
mv "$OUT" "$R"
echo "finished $R"
