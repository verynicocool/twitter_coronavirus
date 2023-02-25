#!/bin/sh

for file in /data/Twitter\ dataset/geoTwitter20*; do
    /home/nvillalba/proj/twitter_coronavirus/src/map.py --input_path="$file" &
done
