#!/bin/bash
cd /home/user/Content-Claude/videos/_today2
curl -sL "https://drive.usercontent.google.com/download?id=1kNKd0woVZZLv-MBb7HFYCR9g-1wwdjKP&export=download&confirm=t" -o src/141927.mp4
python3 tools/combo.py hoodie 141927:12:380 > .media/combo-hoodie.log 2>&1
cd /home/user/Content-Claude
python3 videos/_today/tools/make.py n01 >> videos/_today2/.media/build6.log 2>&1 && echo denim-hoodie-1 >> videos/_today/queue.txt
echo HOODIE-DONE >> videos/_today2/.media/build6.log
