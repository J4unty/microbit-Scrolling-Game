#!/bin/bash

# strip typing hints, for easier minification
strip-hints ./out/scrolling_game.py > ./out/stripped.py

# minify the python source
# need to compare the efficency of the --obfuscate-import-methods and --obfuscate-builtins options
pyminifier \
    --outfile=./out/minified.py \
    --obfuscate-classes \
    --obfuscate-functions \
    --obfuscate-variables \
    --replacement-length=1 \
    ./out/stripped.py \
    1>/dev/null

# remove the last line with the link for the pyminifier repo
sed -i '' -e '$ d' ./out/minified.py

# generate the micropython.hex file
uflash ./out/minified.py ./out/
