#!/bin/bash
# need to compare the efficency of the --obfuscate-import-methods and --obfuscate-builtins options
pyminifier --outfile=./out/minified.py --obfuscate-classes --obfuscate-functions --obfuscate-variables --replacement-length=1 scrolling_game.py 1>/dev/null
sed -i '' -e '$ d' ./out/minified.py
uflash ./out/minified.py ./out/
