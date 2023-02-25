#!/bin/sh

for file in reduced*
do
    for hashtag in '#coronavirus' '#코로나바이러스'
    do
        ./src/visualize.py --input_path="$file" --key="$hashtag" &
    done
done    
