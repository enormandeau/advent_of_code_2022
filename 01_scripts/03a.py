#!/usr/bin/env python3
"""Solution to Advent of Code problem (see file name)

Usage:
    <program> input_file
"""

# Modules
from string import ascii_letters
import sys

# Parse user input
try:
    input_file = sys.argv[1]
except:
    print(__doc__)
    sys.exit(1)

# Solve problem
rucksacks = [list(x.strip()) for x in open(input_file).readlines()]
priorities = dict(zip(ascii_letters, range(1, len(ascii_letters) + 1)))

total = 0

for r in rucksacks:
    l = len(r) // 2
    first = set(r[: l])
    second = set(r[l: ])
    both = list(first.intersection(second))[0]
    total += priorities[both]

print(total)
