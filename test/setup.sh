#!/bin/bash

# setup for the unittest

# Variables
microbitLibStubFile="./src/microbit.py"
commitHashOfStub="b761ed7b741a27d2e5670834129c6ab4606dcdd7"
microbitLibStubURL="https://raw.githubusercontent.com/makerbit/microbit-stub/${commitHashOfStub}/lib/microbit.py"

# download the micro:bit micropython stub lib if it doesn't exist yet
if [ ! -f $microbitLibStubFile ]
then
    touch $microbitLibStubFile
    curl $microbitLibStubURL --output $microbitLibStubFile
fi
