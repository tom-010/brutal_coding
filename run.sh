#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "please give the path to the project"; exit 1
fi


while true
do
    clear
    python3 src/coverage_delete.py $1
    inotifywait -r -e modify . > /dev/null 2> /dev/null
done