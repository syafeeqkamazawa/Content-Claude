#!/bin/bash
# Owner (21 Oct): the A-roll was recorded on the phone mic, no lavalier — make it sound like a mic.
# Denoise (noise profile from a quiet stretch), cut room boxiness, add warmth and presence,
# de-ess, compress, gently expand the room tail between words, then -15 LUFS / -1.5 dBTP.
# Usage (project root):  tools/voice.sh assets/a.mp4 [noise_start noise_end]
# The video stream is copied untouched; the original audio is kept in .media/audio/a-raw.wav.
set -e
IN=$1; N0=${2:-1.4}; N1=${3:-1.85}
mkdir -p .media/audio
[ -f .media/audio/a-raw.wav ] || ffmpeg -v error -y -i "$IN" -vn -ac 1 -ar 48000 -c:a pcm_s16le .media/audio/a-raw.wav
CH="asendcmd=c='$N0 afftdn sn start; $N1 afftdn sn stop',highpass=f=90:poles=2,afftdn=nr=20:nf=-62:tn=1:gs=8,\
equalizer=f=320:t=q:w=1.1:g=-3.5,bass=g=1.5:f=120:w=0.7,equalizer=f=4200:t=q:w=1.4:g=3,treble=g=2:f=9500,\
deesser=i=0.35:m=0.5:f=0.5,acompressor=threshold=-26dB:ratio=3:attack=6:release=140:makeup=3,\
agate=threshold=0.012:ratio=2:range=0.25:attack=3:release=120"
ffmpeg -v error -y -i .media/audio/a-raw.wav -af "$CH" .media/audio/a-chain.wav
I=$(ffmpeg -nostats -i .media/audio/a-chain.wav -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | awk '{print $2}')
G=$(python3 -c "print(round(-15 - ($I), 1))")
ffmpeg -v error -y -i .media/audio/a-chain.wav -af "volume=${G}dB,alimiter=limit=0.84:level=false:attack=3:release=60" .media/audio/a-enh.wav
ffmpeg -v error -y -i "$IN" -i .media/audio/a-enh.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ac 2 -movflags +faststart "${IN%.mp4}-enh.mp4"
mv "${IN%.mp4}-enh.mp4" "$IN"
rm -f data/a-rms.json
echo "voice: $I LUFS -> gain ${G} dB"
