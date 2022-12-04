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
rucksacks = [set(x.strip()) for x in open(input_file).readlines()]
priorities = dict(zip(ascii_letters, range(1, len(ascii_letters) + 1)))

total = 0

while rucksacks:
    group = rucksacks[:3]
    rucksacks = rucksacks[3:]

    c = Counter(chain(*group))
    badge = c.most_common(1)[0][0]

    total += priorities[badge]

print(total)
