#!/usr/bin/env python3
"""Solution to Advent of Code problem (see file name)

Usage:
    <program> input_file
"""

# Modules
from string import ascii_letters
from collections import Counter
from itertools import chain
import sys

# Parse user input
try:
    input_file = sys.argv[1]
except:
    print(__doc__)
    sys.exit(1)

# Solve problem
pairs = [[tuple(y.split("-")) for y in x.strip().split(",")] for x in open(input_file).readlines()]
total = 0

for p in pairs:
    p1 = [int(x) for x in p[0]]
    p2 = [int(x) for x in p[1]]

    r1 = set(range(p1[0], p1[1]+1))
    r2 = set(range(p2[0], p2[1]+1))

    if len(r1.intersection(r2)):
        total+=1

print(f"{total} pairs with some overlap")
