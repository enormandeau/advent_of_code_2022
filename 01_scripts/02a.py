#!/usr/bin/env python3
"""Solution to Advent of Code problem (see file name)

Usage:
    <program> input_file
"""

# Modules
import sys

# Parse user input
try:
    input_file = sys.argv[1]
except:
    print(__doc__)
    sys.exit(1)

# Solve problem
inputs = [x.strip().split(" ") for x in open(input_file).readlines()]

# Logic
abc = dict(zip("ABC", (1, 2, 3)))
xyz = dict(zip("XYZ", (1, 2, 3)))
#rpc = dict(zip((1, 2, 3), "RPC"))

# Score
total = 0

for game in inputs:
    p1 = abc[game[0]]
    p2 = xyz[game[1]]

    score = p2

    # Implement Rock Papers Scisors...
    # TODO debug
    if p1 == p2:
        #print("draw")
        score += 3

    elif p1 % 3 + 1 == p2:
        #print("win!", rpc[p1], rpc[p2])
        score += 6

    else:
        #print("lost")
        pass

    total += score
    print(p1, p2, score, total)
