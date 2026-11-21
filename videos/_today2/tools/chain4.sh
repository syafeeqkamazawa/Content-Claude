#!/bin/bash
cd /home/user/Content-Claude
until grep -q BUILD4-DONE videos/_today2/.media/build4.log 2>/dev/null; do sleep 30; done
ls videos/my-first-book-3/assets/photos/A1.jpg >/dev/null 2>&1 || python3 videos/_today/tools/gen_ai.py n08 > /dev/null 2>&1
python3 videos/_today/tools/make.py n08 >> videos/_today2/.media/build5.log 2>&1
echo BUILD5-DONE >> videos/_today2/.media/build5.log
