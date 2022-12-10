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

# Functions
def increase_cycle(cycle, register, n):
    """Increase the cycle and report register if needed
    """
    global CRT

    for c in range(cycle, cycle+n):
        if not (c) % 40:
            CRT.append([])

        if c % 40 in range(register, register+3):
            CRT[-1].append("#")
        else:
            CRT[-1].append(" ")

    return cycle + n

# Load data
instructions = [x.strip().split(" ") for x in open(input_file).readlines()]

# Solve problem
cycle = 0
register = 0
CRT = [[]]

for ins in instructions:
    if ins[0] == "noop":
        cycle = increase_cycle(cycle, register, 1)

    if ins[0] == "addx":
        x = int(ins[1])
        cycle = increase_cycle(cycle, register, 2)
        register += x

# Solution 2
print("Solution to problem 2:\n")
for line in CRT:
    for pixel in line:
        print(pixel, end="")

    print()
