#!/usr/bin/env python3
"""Solution to Advent of Code problem (see file name)

Usage:
    <program> input_file
"""

# Modules
import sys

# Functions
def parse_crates(crates):
    """Return dictionary of stacks
    """
    crates = [x for x in crates.split("\n")][::-1]

    # Build dictionary
    stack_pos = {}
    crate_dict = {}

    for i, k in enumerate(crates[0]):
        if k.strip():
            stack_pos[i] = k
            crate_dict[k] = []

    for c in crates[1:]:
        for p in stack_pos:
            if c[p].strip():
                crate_dict[stack_pos[p]].append(c[p])

    return crate_dict

# Parse user input
try:
    input_file = sys.argv[1]
except:
    print(__doc__)
    sys.exit(1)

# Parse crates
crates, moves = open(input_file).read().split("\n\n")
crate_dict = parse_crates(crates)

# Solve problem
for m in moves.strip().split("\n"):
    m = m.split(" ")
    num = int(m[1])
    _from = m[3]
    _to = m[5]

    # Proceed to moves
    for _ in range(num):
        crate_dict[_to].append(crate_dict[_from].pop())

# Get answer
answer = []

for i in sorted(crate_dict):
    answer.append(crate_dict[i][-1])

print("".join(answer))
