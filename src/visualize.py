#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import matplotlib.pyplot as plt
import numpy as np
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

series = []
values = []

for k,v in items:
    series.append(k)
    values.append(v)
    print(k,':',v)

fig = plt.figure(figsize = (10, 5))

first_10s = series[:10]
first_10v = values[:10]

first_10s.reverse()
first_10v.reverse()

print(first_10s, first_10v)

# creating the bar plot
plt.bar(first_10s, first_10v, color = 'maroon', width = 0.4)

xLab = ""
if args.input_path == "reduced.lang":
    xLab = "Languages"
else:
    xLab = "Countries"

plt.xlabel(xLab)
plt.ylabel("No. of tweets with " + args.key)
plt.title(args.key + " tweets in different " + xLab)
plt.savefig("./graphs/" + args.input_path + args.key + ".png")
