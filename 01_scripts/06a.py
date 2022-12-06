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
wsize = 4
data = open(input_file).read().strip()

for i in range(len(data) - wsize):
    d = data[i: i+wsize]

    if len(set(d)) == wsize:
        print(i+wsize, d)
        sys.exit()
