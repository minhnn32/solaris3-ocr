#! /bin/zsh

tesseract tesstrain/data/Solaris-3-ground-truth/eng_1.tif stdout \
--tessdata-dir /Users/austringer/Workspace/my-repo/solaris3-ocr/tesstrain/data \
--psm 7 \
-l Solaris-3 \
--loglevel ALL

cat tesstrain/data/Solaris-3-ground-truth/eng_1.gt.txt