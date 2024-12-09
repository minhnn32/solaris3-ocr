#! /bin/zsh

cd tesstrain

TESSDATA_PREFIX=../tesseract/tessdata gmake training \
MODEL_NAME=Solaris-3 \
START_MODEL=eng \
TESSDATA=../tesseract/tessdata \
MAX_ITERATIONS=100000