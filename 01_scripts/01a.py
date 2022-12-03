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
elves = [sum([int(y) for y in x.strip().split("\n")])
        for x in open(input_file).read().strip().split("\n\n")]

print(max(elves))
