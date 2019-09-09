#!/bin/bash

# File locations
outputFolder="./out/"
pythonSourceFile="scrolling_game.py"
strippedSourceFile="${outputFolder}stripped.py"
minifiedSourceFile="${outputFolder}minified.py"
timestamp="date +\"[%d-%m-%Y %H:%M:%S]\""

# variables
watchInterval=2
uploadParameterName="upload"
watchParameterName="watch"

# File watch if activated
if [ "$1" = $watchParameterName ] || [ "$2" = $watchParameterName ]
then
    lastHash=""
    additionalParameter=""

    # check if upload was also specified
    if [ "$1" = $uploadParameterName ] || [ "$2" = $uploadParameterName ]
    then
        additionalParameter=$uploadParameterName
    fi

    while [[ true ]]
    do
        currentHash=`shasum $pythonSourceFile | cut -d " " -f 1`
        if [[ $lastHash != $currentHash ]]
        then
            echo "$(eval $timestamp) Recompile..."
            echo "$(eval $timestamp) $(./$0 $additionalParameter)"
            lastHash=$currentHash
        fi
        sleep $watchInterval
    done
fi

# Create output Folder if it doesn't exist yet
if [ ! -d $outputFolder ]
then
    mkdir $outputFolder
fi

# strip typing hints, for easier minification
strip-hints $pythonSourceFile > $strippedSourceFile

# minify the python source
# need to compare the efficency of the --obfuscate-import-methods and --obfuscate-builtins options
pyminifier \
    --outfile=$minifiedSourceFile \
    --obfuscate-classes \
    --obfuscate-functions \
    --obfuscate-variables \
    --replacement-length=1 \
    $strippedSourceFile \
    1>/dev/null

# remove the last line with the link for the pyminifier repo
sed -i '' -e '$ d' $minifiedSourceFile

# generate the micropython.hex file
if [ "$1" = $uploadParameterName ] || [ "$2" = $uploadParameterName ]
then
    uflash $minifiedSourceFile
else
    uflash $minifiedSourceFile $outputFolder
fi
